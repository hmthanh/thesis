# Translating Embeddings for Modeling Multi-relational Data

Tóm lược paper : Paper này mô hình hóa một cạnh thành một $\overrightarrow{vector}$ trong không gian,  **Translation** (chuyển đổi) từ một entity (node) ~ $entity_{id}$ hoặc relation (cạnh) ~ $realtion_{id}$ trong KGs thành 1 vector không gian có k chiều $\overrightarrow{entity'}_k$ hoặc $\overrightarrow{relation'}_n$ (k tùy ý, trong mô hình KBAT k bằng 50) sao cho

$$\overrightarrow{entity'_{head}} + \overrightarrow{relation'} = \overrightarrow{entity'_{tail}}$$


Xem video sơ lược tại : https://www.youtube.com/watch?v=YQCG408wgLw

Xem sơ đoạn đầu thôi, trong đó không nói rõ đâu

> In this paper, we introduce TransE, an energy-based model for learning low-dimensional embeddings of entities.

## Mô tả thuật toán nhúng

The main motivation behind our translation-based parameterization is that hierarchical relationships are extremely common in KBs and translations are the natural transformations for representing them

Indeed, considering the natural representation of trees (i.e. embeddings of the nodes in dimension
2), the siblings are close to each other and nodes at a given height are organized on the x-axis,
the parent-child relationship corresponds to a translation on the y-axis. Since a null translation
vector corresponds to an equivalence relationship between entities, the model can then represent
the sibling relationship as well.
<hr/>
Motivation chính là quan hệ phân cấp cực kỳ phổ biến trong KGs và translations (biến đổi hóa) là một quá trình biến đổi hóa tự nhiên để biểu diễn chúng

Vì thế, ta xem một khi biểu diễn một cái cây tự nhiên (ví dụ nhúng một một node có 2 chiều [x, y]), siblings (những node cùng một cha) thì gần với nhau hơn, node có quan hệ quan hệ lớn bé thì sắp xếp theo trục x, quan hệ cha con thì sắp xếp theo trục y.

Từ đó một phép biển đổi null vector tương ứng với một quan hệ giữa chúng, mô hình cũng có thể biểu diễn **sibling relationship** (relationship có cùng cha, hay quan hệ gần giống nhau) nữa

## 2 Translation-based model

Given a training set $S$ of triplets $(h, l, t)$ composed of two entities $h, t ∈ E$ (the set of entities) and a
relationship $l ∈ L$ (the set of relationships), our model learns vector embeddings of the entities and
the relationships. The embeddings take values in $\mathbb{R}^k$ ($k$ is a model hyperparameter) and are denoted
with the same letters, in boldface characters. 

**The basic idea behind our model is that the functional relation induced by the $l$-labeled edges corresponds to a translation of the embeddings**
, i.e. we want that $h + l ≈ t$ when $(h, l, t)$ holds ($t$ should be a nearest neighbor of $h + l$), while $h + l$ should be
far away from $t$ otherwise. Following an energy-based framework, the energy of a triplet is equal to $d(h + l, t)$ for some dissimilarity measure $d$, which we take to be either the $L_1$ or the $L_2$-norm.

$d$ : giá trị đo sự khác nhau của $h + l$ so với $t$

$uniform(μ,σ^2)$ : phân phối chuẩn với trung bình $μ$ (kỳ vọng - giá trị trung bình) và phương sai $σ^2$ (thể hiện sự phân tán của thống kê đó)

## Thuật toán chính

![alt text](/img/TransE/TransE_alg.png)

margin $\gamma$ : chưa biết

$L$ :  set relation

$E$ : set entity

$k$ : số lượng chiều

### Bước 1 : 
Khởi tạo $l, e = uniform(-\frac{6}{\sqrt{k}}, \frac{6}{\sqrt{k}})$ :  là phân phối chuẩn với trung bình là $-\frac{6}{\sqrt{k}}$ và phương sai là $\frac{6}{\sqrt{k}}$

**Ghi nhớ** : $uniform + uniform = uniform$
Tức là phân phối chuẩn thì cộng với nhau thì nó vẫn là phân phối chuẩn

$l \leftarrow l / \|L\|$ :  loại bỏ cặp trùng

