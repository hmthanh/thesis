# summary week 1
Bài toán mà bài báo nghiên cứu: Phát triển một KG hiện có có thể được thực hiện bằng cách trích xuất các facts-(sự kiện mới) từ các nguồn bên ngoài, chẳng hạn như Web corpora hoặc bằng cách suy ra các facts còn thiếu từ những facts đã có trong KG. Phương pháp tiếp cận như vậy được gọi là Dự đoán liên kết (Link Prediction-LP).

Bài báo phân tích và so sánh 16 mô hình thuộc 3 kiến trúc chính:
* Tensor Decomposition Models, nổi bật là 2 mô hình ComplEx, TuckER:
    * ComplEx: cho kết quả tốt trên **FB15k**, **YAGO3-10**
    * TuckER: cho kết quả tốt trên **WN18**, **FB15k-237**
* Geometric Model nổi bật là mô hình RotatE:
    * RotatE: RotatE **WN18**, **WN18RR**
* Deep Learning	Models: Nỗi bật là 2 model **ConvKB**, **CapsE**
    * RotatE: cho kết quả tốt trên **WN18**
    * CapsE: cho kết quả tốt trên **WN18RR**

Bài báo khảo sát trên 5 bộ dữ liệu được sử dụng phổ biến nhất cũng như các số liệu phổ biến nhất hiện được sử dụng để đo điểm chuẩn:
* FB15k
* WN18
* FB15k-237
* WN18RR
* YAGO3-10

Vấn đề của các mô hình cũ là họ báo cáo kết quả tổng hợp qua một số lượng lớn các sự kiện thử nghiệm trong đó có ít thực thể over-represented. Kết quả là, các phương thức LP có thể thể hiện hiệu suất tốt trên các điểm chuẩn này bằng cách chỉ gửi đến các thực thể đó trong khi bỏ qua các thực thể khác. Tức là có chỉ gửi đến các thực thể over-represented. (có nhiều quan hệ, liên kết)

Các mô hình Tensor Decomposition cho thấy kết quả nhất quán nhất trên các tập dữ liệu. Trong các triển khai được so sánh, hầu hết các hệ thống này hiển thị hiệu suất thống nhất trên tất cả các số liệu đánh giá trên các bộ dữ liệu phân tích (với các potential exceptions của ANALOGY và SimplE, dường như có nhiều biến động hơn). Cụ thể, ComplEx với tính chuẩn hóa N3 của nó hiển thị kết quả tuyệt vời trên tất cả các số liệu trên tất cả các bộ dữ liệu, là mô hình dựa trên nhúng duy nhất-(embedding-based model consistently) luôn có thể so sánh với đường cơ sở AnykinaL.

Mặt khác, họ các phương pháp hình học(Geometric Models) cho thấy kết quả không ổn định hơn một chút. Trong những năm qua, nghiên cứu đã dành một lượng lớn đáng kể cho các mô hình tịnh tiến, từ TransE có nhiều người kế thừa các luật đa nhúng để xử lý các mối quan hệ nhiều-một, một-nhiều và nhiều-nhiều. Các mô hình cho thấy những kết quả thú vị, nhưng vẫn có một số bất thường trên các số liệu và bộ dữ liệu. Chẳng hạn, các mô hình như TransE và STransE dường như đặc biệt đấu tranh(loại trừ nhau) trên bộ dữ liệu WN18RR, đặc biệt là khi nói đến các số liệu H@1 và MRR. Nói chung, các mô hình chỉ dựa vào các bản dịch translations dường như đã bị vượt qua bởi các bản dịch roto roto-translational gần đây. Về vấn đề này, RotatE cho thấy hiệu suất ổn định đáng kể trên tất cả các bộ dữ liệu và nó đặc biệt tỏa sáng khi tính đến H@10.

Các mô hình Deep Learning, cuối cùng là họ các phương pháp đa dạng nhất, với kết quả khác nhau tùy thuộc vào sự lựa chọn kiến trúc của các mô hình và vào việc triển khai của họ. ConvR và RSN hiển thị cho kết quả tốt nhất trong họ này, đạt được hiệu suất rất giống nhau, state-of-the-art performance trong FB15k, WN18 và YAGO3-10. Trong FB15k-237 và WN18RR, có các quy trình lọc đã cắt đi các đường đi phù hợp nhất, RSN dường như có một thời gian khó khăn hơn, có lẽ là do công thức của nó thúc đẩy rõ ràng các đường đi. Mặt khác, các mô hình như ConvKB và CapsE đạt được kết quả đầy hứa hẹn trên các số liệu H@10 và MR, trong khi chúng dường như phải vật lộn với H@1 và MRR; hơn nữa, trong một số bộ dữ liệu, chúng bị cản trở rõ ràng bởi các vấn đề của chúng với các luật ràng buộc được mô tả trong Phần 5.4.1

## các bài báo liên quan
 Chandrahas et al. [51](../papers/51_Towards_Understanding_the_Geometry_of_Knowledge_Graph_Embeddings.pdf) nghiên cứu tính chất hình học của các embeddings được thu được trong không gian ẩn.

Wang và cộng sự. [64](../papers/64_On_Evaluating_Embedding_Models_for_Knowledge_Base_Completion.pdf) cung cấp một bài phê bình về các thử nghiệm đo điểm chuẩn hiện tại.

Akrami và cộng sự [2](../papers/2_Re-evaluating_Embedding-Based_Knowledg_Graph.pdf) sử dụng trực giác tương tự như Toutanova et al. để thực hiện phân tích có cấu trúc hơn một chút, vì họ sử dụng nhiều mô hình khác nhau để kiểm tra khoảng cách hiệu suất giữa FB15k và FB15K-237.

Kadlec et al. [26](../papers/26_Knowledge_Base_Completion_Bas_lines_Strike_Back.pdf) chứng minh rằng việc triển khai DistMult được điều chỉnh cẩn thận có thể đạt được các kết quả hiện đại, vượt qua hầu hết những người kế nhiệm của chính nó, đặt ra câu hỏi về việc chúng tôi đang phát triển các mô hình LP hay chỉ là điều chỉnh siêu tham số-hyperparameters.

Hung Nghiep Tran và cộng sự [59](../papers/59_Analyzing_Knowledge_Graph_Embedding_Methods_from_a_Multi-Embedding_Interaction_Perspective.pdf) diễn giải 4 mô hình dựa trên các thành phần ma trận như các trường hợp đặc biệt của cùng một cơ chế tương tác đa nhúng (multi-embedding). Trong công thức của họ, mỗi phần tử k trong KG được biểu thị dưới dạng một tập các vectơ {k (1), k (2), ..., k (n)}; các hàm chấm điểm kết hợp các vectơ như vậy bằng cách sử dụng các sản phẩm trilinear. Các tác giả cũng bao gồm các phân tích và so sánh theo kinh nghiệm giữa các mô hình đã nói và giới thiệu một mô hình đa nhúng mới dựa trên đại số bậc bốn.

## công việc dự kiến 2 tuần tiếp theo.
- Hiểu được phương pháp thực hiện của bài báo.
- Hiểu cách thực hiện của 5 bài báo liên quan.
- Tìm hiểu kích thước, các đặc trưng của 5 bộ dataset.
- Hoàn thành đề cương khóa luận