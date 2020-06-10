# Overview
[Knowledge Graphs-KG](#Knowledge-Graphs-KG)

[THE LINK PREDICTION PROBLEM](#THE-LINK-PREDICTION-PROBLEM)
## Knowledge Graphs-KG
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

Để giảm thiểu các vấn đề được đề cập ở trên, bài báo thực hiện phân tích so sánh rộng rãi về một bộ mô hình LP đại diện dựa trên các ***KG embeddings***. Bài báo so sánh các hệ thống hiện đại và xem xét các công trình thuộc một loạt các kiến trúc. Bài báo đào tạo và điều chỉnh các hệ thống như vậy từ đầu và cung cấp kết quả thử nghiệm vượt ra ngoài những gì có sẵn trong các bài viết gốc, bằng cách đề xuất các thực tiễn đánh giá mới và thông tin mới. Đặc biệt:
* Bài báo tính đến 16 mô hình thuộc kiến trúc máy học đa dạng và kiến trúc học sâu; Bài báo cũng áp dụng đường cơ sở(baseline) cho một mô hình LP tiên tiến nhất dựa trên khai thác quy tắc (rule mining). Bài báo cung cấp một mô tả chi tiết về các phương pháp được xem xét để so sánh thử nghiệm và tóm tắt các tài liệu liên quan, cùng với phân loại giáo dục (***educational taxonomy***) cho các kỹ thuật Nhúng đồ thị tri thức ***Knowledge Graph Embedding***.
* Bài báo tính đến 5 bộ dữ liệu được sử dụng phổ biến nhất cũng như các số liệu phổ biến nhất hiện được sử dụng để đo điểm chuẩn; Bài báo phân tích chi tiết các đặc trứng và đặc thù của nó.
* Đối với mỗi mô hình, bài báo cung cấp kết quả định lượng cho tính chính xác và hiệu quả trên mỗi tập dữ liệu.
* Bài báo tạo ra một tập hợp các đặc trưng cấu trúc trong dữ liệu đào tạo và Bài báo đo lường cách chúng ảnh hưởng đến hiệu suất dự đoán của từng mô hình trên mỗi thực tế thử nghiệm.

## THE-LINK-PREDICTION-PROBLEM
Phần này cung cấp một phác thảo chi tiết cho nhiệm vụ LP trong ngữ cảnh KG, giới thiệu các khái niệm chính mà bài báo sẽ đề cập đến trong KG.

Bài báo định nghĩa một KG là một đồ thị đa hướng có nhãn KG = (E, R, G):

* E: một tập hợp nodes nút đại diện cho các *entities* (thực thể );
* R: một tập hợp nhãn-labels đại diện cho *relations* (quan hệ);
* G ⊆ E × R × E: một tập hợp các cạnh thể hiện các sự kiện *facts* kết nối các cặp thực thể-entities. Mỗi thực tế là một bộ ba ⟨h, r, t⟩ **triple ⟨h, r, t⟩**, trong đó h là head, r là relation và t là tail của sự kiện *facts*.

**Link Prediction** (LP) là nhiệm vụ khai thác ((***exploiting***) các sự kiện hiện có trong KG để suy ra những điều còn thiếu. Để đoán đúng thực thể hoàn thành ⟨h, r, ?⟩ (tail prediction) hoặc ⟨?, R, t⟩ (head prediction). Để đơn giản, khi nói về head and tail prediction trên toàn cục, bài báo gọi thực thể nguồn là thực thể đã biết trong dự đoán và thực thể đích là đối tượng dự đoán.

Trong thời gian, nhiều phương pháp đã được đề xuất để giải quyết nhiệm vụ LP. Một số phương pháp dựa trên các đặc trưng có thể quan sát và sử dụng các kỹ thuật, chẳng hạn như Khai thác quy tắc **Rule Mining** [17](../paper/17_AMIE_Association_Rule_Mining_under_Incomplete_Evidence.pdf) [16](../paper/16_Fast_rule_mining_in_ontological_knowledge_bases_with_AMI.pdf) [37](../paper/37_Fine-Grained_Evaluation_of_Ruleand_Embedding-Based_Systems.pdf) [24](../paper/24_Mining_Expressive_Rules_in_Knowledge_Graphs.pdf) hoặc Thuật toán xếp hạng đường dẫn **Path Ranking Algorithm** [31](../paper/31_Relational_retrieval_using_a_combination_of_path-constrained_random_walks.pdf) [32](../paper/32_Random_Walk_Inference_and_Learning_in_A_Large_Scale_Knowledge_Base.pdf) để xác định các bộ ba **triples** bị thiếu trong đồ thị. Gần đây, với sự phát triển của các kỹ thuật Machine Learning mới, các nhà nghiên cứu đã thử nghiệm để nắm bắt các đặc trưng tiềm ẩn của đồ thị với các biểu diễn được vector hóa, hoặc nhúng *embeddings* các thành phần của nó. Nói chung, *embeddings* là các vectơ của các giá trị số có thể được sử dụng để thể hiện bất kỳ loại phần tử nào (ví dụ: tùy thuộc vào miền: *words, people, products,...*).*Embeddings* được học tự động, dựa trên cách các yếu tố tương ứng xảy ra và tương tác với nhau trong bộ dữ liệu đại diện của thế giới thực.

Ví dụ, các *word embeddings* đã trở thành một cách tiêu chuẩn để biểu thị các từ trong từ vựng và chúng thường được học bằng cách sử dụng văn bản làm dữ liệu đầu vào. Khi nói đến KG, các *embeddings* thường được sử dụng để thể hiện các mối quan hệ các thực thể bằng cách sử dụng cấu trúc đồ thị; các vectơ kết quả, được đặt tên là *KG Embeddings*, thể hiện ngữ nghĩa của đồ thị gốc và có thể được sử dụng để xác định các liên kết mới bên trong nó, do đó giải quyết nhiệm vụ LP.

Trong phần sau đây, bài báo sử dụng các phần tử in nghiêng để xác định các phần tử **KG** (thực thể hoặc quan hệ) và phần tử in đậm **bold** để xác định các phần nhúng tương ứng. Ví dụ, được cho là một thực thể chung, chúng ta có thể sử dụng *e* khi tham chiếu đến phần tử của nó trong đồ thị và **e** khi đề cập đến việc nhúng nó.

Các bộ dữ liệu được sử dụng trong nghiên cứu LP thường thu được các mẫu KG thế giới thực; Do đó, mỗi tập dữ liệu có thể được coi là một KG nhỏ với các tập hợp thực thể E, quan hệ R và dữ liệu G. Để tạo điều kiện nghiên cứu, G được chia thành ba tập hợp rời rạc: tập huấn luyện G_train, tập xác thực G_valid và một bộ kiểm tra G_test.

Hầu hết các mô hình LP dựa trên các *embeddings* là một hàm cho điểm để ước tính tính hợp lý của bất kỳ fact <h, r, t> bằng cách sử dụng các *embeddings* của chúng: ϕ(h, r,t).

Trong quá trình đào tạo, các *embeddings* thường được khởi tạo ngẫu nhiên và sau đó được cải thiện với các thuật toán tối ưu hóa như lan truyền ngược với độ dốc giảm dần. Các mẫu dương tính trong G_train bị hỏng ngẫu nhiên để tạo các mẫu âm tính. Quá trình tối ưu hóa nhằm mục đích tối đa hóa tính hợp lý của các sự kiện tích cực cũng như giảm thiểu tính hợp lý của các sự kiện tiêu cực; đây là số tiền để sử dụng chức năng mất bộ ba. Theo thời gian, nhiều cách hiệu quả hơn để tạo ra bộ ba âm đã được đề xuất, chẳng hạn như lấy mẫu từ bản phân phối Bernouilli [66]