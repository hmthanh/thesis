import numpy as np
import tensorflow as tf

def mask(inputs, queries=None, keys=None, type=None):
    """Masks paddings on keys or queries to inputs
    inputs: 3d tensor. (N, T_q, T_k)
    queries: 3d tensor. (N, T_q, d)
    keys: 3d tensor. (N, T_k, d)
    """
    padding_num = -2 ** 32 + 1
    if type in ("k", "key", "keys"):
        # Tọa ma trận mask
        # Dấu của tổng các dòng
        masks = tf.sign(tf.reduce_sum(tf.abs(keys), axis=-1))  # (N, T_k)
        # Mở rộng tổng thêm 1 chiều thứ 2
        masks = tf.expand_dims(masks, 1) # (N, 1, T_k)
        # Lặp lại chiều của dấu tổng các dòng T_q lần
        masks = tf.tile(masks, [1, tf.shape(queries)[1], 1])  # (N, T_q, T_k)

        # Tạo ma trận  paddings có kích thước như inputs và các phần tử đều bằng -2^32+1
        paddings = tf.ones_like(inputs) * padding_num
        # Tại 1 vị trí bất kì. Nếu bằng 0 thì lấy từ giá trị -2^32+1, nếu sai lấy từ inputs.
        outputs = tf.where(tf.equal(masks, 0), paddings, inputs)  # (N, T_q, T_k)
    elif type in ("q", "query", "queries"):
        # Generate masks
        masks = tf.sign(tf.reduce_sum(tf.abs(queries), axis=-1))  # (N, T_q)
        masks = tf.expand_dims(masks, -1)  # (N, T_q, 1)
        masks = tf.tile(masks, [1, 1, tf.shape(keys)[1]])  # (N, T_q, T_k)

        # Apply masks to inputs
        outputs = inputs*masks
    elif type in ("f", "future", "right"):
        diag_vals = tf.ones_like(inputs[0, :, :])  # (T_q, T_k)
        tril = tf.linalg.LinearOperatorLowerTriangular(diag_vals).to_dense()  # (T_q, T_k)
        masks = tf.tile(tf.expand_dims(tril, 0), [tf.shape(inputs)[0], 1, 1])  # (N, T_q, T_k)

        paddings = tf.ones_like(masks) * padding_num
        outputs = tf.where(tf.equal(masks, 0), paddings, inputs)
    else:
        print("Check if you entered type correctly!")
    return outputs


def scale_dot_product_attention(Q, K, V,
                                causality=False, dropout_rate=0.,
                                training=True,
                                scope='scaled_dot_product_attention'):
    '''
    Q: Ma trận queries kích thước [N, T_q, d_k]
    K: Ma trận keys kích thước    [N, T_k, d_k]
    V: Ma trận values kích thước  [N, T_k, d_v]
    causality: Quan hệ nhân quả. Nếu True, sẽ áp dụng masking cho những giá trị tương lai mà chưa được thấy.
    dropout_rate: Tỷ lệ dropout ở fully connected, nằm trong [0,1].
    training: kiểm soát dropout_rate.
    scope: Scope tùy chọn cho `variable_scope`
    '''
    with tf.variable_scope(scope, reuse=tf.AUTO_REUSE):
        d_k = Q.get_shape().as_list()[-1]

        # dot products
        outputs = tf.matmul(Q, tf.transpose(K, [0, 2, 1]))  # N, T_q, T_k
        # scale
        outputs /= d_k ** 0.5
        # key masking
        outputs = mask(outputs, Q, K, type='key')
        # causality or future binding masking
        if causality:
            outputs = mask(outputs, type="future")

        # softmax
        outputs = tf.nn.softmax(outputs)
        attention = tf.transpose(outputs, [0, 2, 1])
        tf.summary.image("attention", tf.expand_dims(attention[:1], -1))

        # query masking
        outputs = mask(outputs, Q, K, type="query")
        with tf.Session() as sess:
            print('Attention weight: \n', sess.run(outputs))
        # dropout
        outputs = tf.layers.dropout(outputs, rate=dropout_rate, training=training)
        # Mỗi 1 dòng của outputs là một phân phối xác xuất của attention.
        # weighted sum (context vectors)
        outputs = tf.matmul(outputs, V)  # (N, T_q, d_v)

    return outputs


queries = tf.constant([[[1.],
                [2.],
                [0.]]], tf.float32) # (1, 3, 1)
keys = tf.constant([[[4.],
             [0.]]], tf.float32)  # (1, 2, 1)
inputs = tf.constant([[[4., 0.],
                       [8., 0.],
                       [0., 0.]]], tf.float32) # (1, 3, 2)
y = mask(inputs, queries, keys, "key")

with tf.Session() as sess:
    print('mask function for key: \n ', sess.run(y))

# Q = tf.reshape(tf.random.normal(np.array([6]), mean = 0, stddev = 1.0, dtype = tf.float32), (1, 3, 2)) #[N, T_q, d_k]
# K = tf.reshape(tf.random.normal(np.array([6]), mean = 1, stddev = 2.0, dtype = tf.float32), (1, 3, 2)) #[N, T_k, d_k]
# V = tf.reshape(tf.range(0, 6, 1, dtype = tf.float32), (1, 3, 2)) #[N, T_k, d_v]
# with tf.Session() as sess:
#     print('Q matrix: \n', sess.run(Q))
#     print('K matrix: \n', sess.run(K))
#     print('V matrix: \n', sess.run(V))
#     print('Attention matrix by scale dot product: \n', sess.run(scale_dot_product_attention(Q, K, V)))
# 
# 
