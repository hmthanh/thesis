Đồ thị tri thức (***Knowledge Graphs-KG***) là các biểu diễn cấu trúc của thông tin thế giới thực.

Trong một node KG đại diện cho một entities(thực thể), chẳng hạn như người và địa điểm;

labels (nhãn) là loại quan hệ có thể kết nối 2 thực thể;

edges (cạnh) là các sự kiện cụ thể kết nối hai thực thể với một mối quan hệ.

Do khả năng mô hình hóa dữ liệu có cấu trúc, phức tạp theo cách dễ đọc bằng máy, KG hiện đang được sử dụng rộng rãi trong nhiều lĩnh vực khác nhau, từ trả lời câu hỏi đến truy xuất thông tin và hệ thống đề xuất dựa trên nội dung và chúng rất quan trọng đối với bất kỳ dự án (semantic web)web mining nào [ 23].

Ví dụ về các KG đáng chú ý là FreeBase [7], WikiData [62], DBPedia [4], Yago [54] và - trong ngành - Google KG [52], Microso ‰ Satori [48] và Đồ thị tìm kiếm của Facebook [53]. KG khổng lồ có thể chứa hàng triệu thực thể và hàng tỷ quan hệ(facts).

Mặc dù có những nỗ lực như vậy, nhưng ai cũng biết rằng ngay cả những chiếc KG hiện đại cũng không hoàn hảo (**incompleteness**). 

Ví dụ, người ta đã quan sát thấy rằng hơn 70% thực thể người không có nơi sinh và hơn 99% không có dân tộc được biết đến [12, 69] trong FreeBase một trong những KG lớn nhất và được sử dụng rộng rãi nhất cho mục đích nghiên cứu. Điều này đã khiến các nhà nghiên cứu đề xuất các kỹ thuật khác nhau để sửa lỗi cũng như thêm các sự kiện còn thiếu vào KG [47. Knowledge graph refinement A survey of approaches and evaluation methods](../paper/47_Knowledge_graph_refinement_A_survey_of_approaches_and_evaluation_methods.pdf), thường được gọi là nhiệm vụ Hoàn thành đồ thị tri thức hoặc Tăng cường đồ thị tri thức (***Knowledge Graph Completion or Knowledge Graph Augmentation***).

Việc phát triển một KG hiện có có thể được thực hiện bằng cách trích xuất các sự kiện mới từ các nguồn bên ngoài, chẳng hạn như **Web corpora** hoặc bằng cách suy ra các sự kiện còn thiếu từ những sự kiện đã có trong KG. Phương pháp tiếp cận, được gọi là Dự đoán liên kết (***Link Prediction-LP***).

LP là một lĩnh vực nghiên cứu ngày càngsôi nổi, gần đây đã phát triển mạnh mẽ từ sự bùng nổ của máy học (machine learning) và kỹ thuật học sâu (deep learning). Ngày nay, phần lớn các mô hình LP sử dụng KG làm gốc để tìm hiểu các biểu diễn đữ liệu với số chiều thấp được đặt tên là Nhúng biểu đồ tri thức (***Knowledge Graph Embeddings***), sau đó sử dụng chúng để suy ra các sự kiện mới.

Lấy cảm hứng từ một vài công trình tinh túy như [RESCAL](../paper/44_A_Three-Way_Model_for_Collective_Learning_on.pdf) và [TransE](../paper/8_Translating_Embeddings_for_Modeling.pdf), trong khoảng thời gian ngắn chỉ vài năm, các nhà nghiên cứu đã phát triển hàng chục mô hình tiểu thuyết dựa trên các kiến ​​trúc rất khác nhau. Một khía cạnh phổ biến đối với đại đa số các bài báo trong lĩnh vực này, nhưng cũng có vấn đề, là họ báo cáo kết quả tổng hợp qua một số lượng lớn các sự kiện thử nghiệm trong đó có ít thực thể ***over-represented***. Kết quả là, các phương thức LP có thể thể hiện hiệu suất tốt trên các điểm chuẩn này bằng cách chỉ gửi đến các thực thể đó trong khi bỏ qua các thực thể khác. Tức là có chỉ gửi đến các thực thể có ít quan hệ. 

Hơn nữa, những hạn chế của thực tiễn tốt nhất hiện nay có thể khiến người ta hiểu được cách các bài báo trong tài liệu này kết hợp với nhau và hình dung hướng nghiên cứu nào đáng để theo đuổi. Thêm vào đó, những điểm mạnh, điểm yếu và hạn chế của các kỹ thuật hiện tại vẫn chưa được biết, đó là hoàn cảnh cho phép các mô hình hoạt động tốt hơn hầu như không được điều tra hầu như không được nghiên cứu. Nói một cách đơn giản, chúng ta vẫn không thực sự biết điều gì làm cho một sự kiện (fact) dễ dàng hoặc khó học và dự đoán.

Để giảm thiểu các vấn đề được đề cập ở trên, chúng tôi thực hiện phân tích so sánh rộng rãi về một bộ mô hình LP đại diện dựa trên các nhúng KG. Chúng tôi đặc quyền các hệ thống hiện đại và xem xét các công trình thuộc một loạt các kiến trúc. Chúng tôi đào tạo và điều chỉnh các hệ thống như vậy từ đầu và cung cấp kết quả thử nghiệm vượt ra ngoài những gì có sẵn trong các bài viết gốc, bằng cách đề xuất các thực tiễn đánh giá mới và thông tin. Đặc biệt: