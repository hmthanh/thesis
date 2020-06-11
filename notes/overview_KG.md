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

Trong quá trình đào tạo, các *embeddings* thường được khởi tạo ngẫu nhiên và sau đó được cải thiện với các thuật toán tối ưu hóa như lan truyền ngược với độ dốc giảm dần. Các mẫu dương tính trong G_train bị hỏng ngẫu nhiên để tạo các mẫu âm tính. Quá trình tối ưu hóa nhằm mục đích tối đa hóa tính hợp lý của các sự kiện đúng cũng như giảm thiểu tính hợp lý của các sự kiện sai; đây là số tiền để sử dụng chức năng **triplet loss**. Theo thời gian, nhiều cách hiệu quả hơn để tạo ra bộ ba âm tính (sai) đã được đề xuất, chẳng hạn như lấy mẫu từ bản phân phối Bernouilli.hoặc tạo ra chúng bằng các thuật toán **adversarial** [55]. Ngoài các phần tử nhúng của các phần tử KG, các mô hình cũng có thể sử dụng các thuật toán tối ưu hóa tương tự để tìm hiểu các tham số bổ sung (ví dụ: trọng số của các neural layers). Các tham số như vậy, nếu có, được sử dụng trong hàm chấm điểm ϕ để xử lý các nhúng thực sự ** actual embeddings** của các thực thể và quan hệ. Vì chúng không được chỉ định cho bất kỳ phần tử KG nào, chúng được gọi là các tham số chia sẻ *shared parameters*.

Trong giai đoạn dự đoán, với một bộ ba không hoàn chỉnh <h, r, ?> tail bị thiếu được suy ra là thực thể, hoàn thành bộ ba, dẫn đến số điểm cao nhất. 
t = argmax ϕ(h, r, e) với e ∈ E

Head prediction được thực hiện tương tự.
Đánh giá được thực hiện bằng cách thực hiện cả Head prediction và Tail prediction trên tất cả các bộ ba thử nghiệm trong G_test và tính toán cho từng dự đoán về cách thực thể mục tiêu xếp hạng so với tất cả các dự đoán khác. Lý tưởng nhất, thực thể mục tiêu sẽ mang lại tính hợp lý cao nhất.

Ranks có thể được tính theo hai phần lớn khác nhau, được gọi là các kịch bản thô và đã lọc. Trên thực tế, một dự đoán có thể có nhiều câu trả lời hợp lệ: ví dụ, khi dự đoán Tail cho <Barack Obama, parent, Natasha Obama>, một mẫu có thể liên kết số điểm cao hơn với Malia Obama so với Natasha Obama. Tổng quát hơn, nếu liên kết dự đoán được chứa trong G (nghĩa là trong G_train hoặc trong G_valid hoặc trong G_test), câu trả lời là hợp lệ. Tùy thuộc vào việc câu trả lời hợp lệ có nên được xem là chấp nhận hay không, hai câu hỏi riêng biệt đã được đưa ra:
* Kịch bản thô: trong kịch bản này, các thực thể hợp lệ vượt quá mục tiêu được coi là sai lầm. Vì vậy, họ đóng góp vào tính toán Ranks. Với một thực tế thử nghiệm ⟨h, r, t⟩ Gtest, Ranks r_t thứ hạng thô của Tail mục tiêu t được tính là:

r_t = |{e ∈ E \ {t } : ϕ(h, r, e) > ϕ(h, r,t)}| + 1

phát biểu bằng lời: r_t được tính max của ϕ(h, r, e) trong đó e thuộc tập các node E trừ node t. 

Ranks thô trong Head prediction có thể được tính tương tự

* Kịch bản được lọc *Filtered Scenario*: trong kịch bản này, các thực thể hợp lệ vượt quá mục tiêu không được coi là sai lầm. Vì vậy, chúng sẽ bị bỏ qua khi tính toán Ranks. Với một thực tế thử nghiệm ⟨h, r, t⟩ G_test, r_t là Ranks của tail t được tính là:

r_t = |{e ∈ E \ {t } : ϕ(h, r, e) > ϕ(h, r,t) ∧ <h, r, e> not in G}| + 1

Head prediction có thể được tính tương tự

Để tính Ranks, cũng cần phải xác định các luật áp dụng khi thực thể mục tiêu đạt được số điểm tương tự như các điểm khác. Sự kiện này được gọi là *tie* (mối ràng buộc) và nó có thể được xử lý bằng các các luật khác nhau:
* min: mục tiêu có Ranks thấp nhất trong số các thực thể ràng buộc. Đây là luật được dễ dãi nhất nhất và nó có thể dẫn đến kết quả một cách giả tăng hiệu suất: như một ví dụ một mô hình đạt được một cách có hệ thống điểm số tương tự cho tất cả các thực thể sẽ đạt được kết quả hoàn hảo theo chính sách này.
* average: mục tiêu có Ranks trung bình trong số các thực thể ràng buộc.
* Random: mục tiêu có Ranks ngẫu nhiên trong số các thực thể trong tie. Trên các bộ thử nghiệm lớn, luật này sẽ có giá trị globally cho luật trung bình.
* ordinal: các thực thể trong tie được xếp hạng-Ranks dựa trên thứ tự mà chúng đã được truyền (duyệt) cho mô hình. Điều này thường phụ thuộc vào các định danh nội bộ của các thực thể, độc lập với điểm số của chúng: do đó luật này sẽ tương ứng trên globally với luật ngẫu nhiên.
* max: mục tiêu có Ranks cao nhất (tệ nhất) trong số các thực thể trong tie. Đây là luật nghiêm ngặt nhất.

Ranks Q thu được từ các dự đoán kiểm tra thường được sử dụng để tính toán các số liệu globally tiêu chuẩn. Các số liệu được sử dụng phổ biến nhất trong LP là:

Mean Rank (MR). Nó là trung bình của các ranks thu được:

MR = 1/Q sum{q | q in Q}

Nó luôn nằm trong khoảng từ 1 đến | E |, và càng thấp, kết quả mô hình càng tốt. Nó rất nhạy cảm với các ngoại lệ, do đó các nhà nghiên cứu gần đây đã bắt đầu tránh nó, thay vào đó, sử dụng Mean Reciprocal Rank (Xếp hạng đối ứng trung bình).

Mean Reciprocal Rank (MRR): Đây là trung bình nghịch đảo của các ranks thu được:

MRR = 1/Q sum {1/q | q in Q}

Nó luôn nằm trong khoảng từ 0 đến 1 và càng lớn, kết quả mô hình càng tốt

Hits@K (H@K). Đó là tỷ lệ dự đoán mà thứ hạng bằng hoặc nhỏ hơn ngưỡng *K*:

H@K = |{q ∈ Q : q ≤ K}| / |Q|

Các giá trị phổ biến cho K là 1, 3, 5, 10. H@K càng cao, kết quả mô hình càng cao. Cụ thể, khi K = 1, nó đo tỷ lệ của các sự kiện thử nghiệm trong đó mục tiêu được dự đoán chính xác trong lần thử đầu tiên. H@1 và MRR có liên quan chặt chẽ với nhau, bởi vì những dự đoán này cũng tương ứng với các phần bổ sung có liên quan nhất vào công thức MRR.

Số liệu có thể được tính riêng cho các tập hợp dự đoán (ví dụ: xem xét dự đoán head và tail riêng biệt) hoặc xem xét tất cả các dự đoán kiểm tra hoàn toàn.