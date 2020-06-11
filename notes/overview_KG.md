# Overview
[Knowledge Graphs-KG](#Knowledge-Graphs-KG)

[THE LINK PREDICTION PROBLEM](#THE-LINK-PREDICTION-PROBLEM)

[KEY TAKEAWAYS AND RESEARCH DIRECTIONS](#KEY_TAKEAWAYS_AND_RESEARCH_DIRECTIONS)

[Tầm quan trọng của cấu trúc đồ thị](#The_importance_of_the_graph_structure)
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

## KEY_TAKEAWAYS_AND_RESEARCH_DIRECTIONS
## Hiệu quả của các lựa chọn thiết kế
Bài báo thảo luận ở đây những quan sát toàn diện về hiệu suất của các mô hình cũng như sự mạnh mẽ của chúng trên các bộ dữ liệu và số liệu đánh giá. bài báo  báo cáo những phát hiện liên quan đến xu hướng nghiên cứu dựa trên các lựa chọn thiết kế cụ thể, cũng như những kỳ công độc đáo được hiển thị bởi các mô hình riêng lẻ.

Các mô hình Tensor Decomposition cho thấy kết quả chắc chắn nhất trên các tập dữ liệu. Trong các triển khai được so sánh, hầu hết các hệ thống này hiển thị hiệu suất thống nhất trên tất cả các số liệu đánh giá trên các bộ dữ liệu phân tích (với các *potential exceptions* của ANALOGY và SimplE, dường như có nhiều biến động hơn). Cụ thể, ComplEx với tính chính quy N3 của nó hiển thị kết quả tuyệt vời trên tất cả các số liệu trên tất cả các bộ dữ liệu, là mô hình dựa trên nhúng duy nhất-(embedding-based model consistently) luôn có thể so sánh với đường cơ sở AnykinaL.

Mặt khác, họ các phương pháp hình học cho thấy kết quả không ổn định hơn một chút. Trong những năm qua, nghiên cứu đã dành một lượng lớn đáng kể cho các mô hình tịnh tiến, từ **TransE** có nhiều người kế thừa các luật đa nhúng để xử lý các mối quan hệ nhiều-một, một-nhiều và nhiều-nhiều. Các mô hình cho thấy những kết quả thú vị, nhưng vẫn có một số bất thường trên các số liệu và bộ dữ liệu. Chẳng hạn, các mô hình như **TransE** và **STransE** dường như đặc biệt đấu tranh trên bộ dữ liệu **WN18RR**, đặc biệt là khi nói đến các số liệu H@1 và MRR. Nói chung, các mô hình chỉ dựa vào các bản dịch *translations* dường như đã bị vượt qua bởi các bản dịch roto **roto-translational** gần đây. Về vấn đề này, **RotatE** cho thấy hiệu suất ổn định đáng kể trên tất cả các bộ dữ liệu và nó đặc biệt tỏa sáng khi tính đến H@10.

Các mô hình Deep Learning, cuối cùng là họ các phương pháp đa dạng nhất, với kết quả khác nhau tùy thuộc vào sự lựa chọn kiến trúc của các mô hình và vào việc triển khai của họ. **ConvR** và **RSN** hiển thị cho kết quả tốt nhất trong họ này, đạt được hiệu suất rất giống nhau, state-of-the-art performance trong **FB15k**, **WN18** và **YAGO3-10**. Trong **FB15k-237** và **WN18RR**, có các quy trình lọc đã cắt đi các đường đi phù hợp nhất, **RSN** dường như có một thời gian khó khăn hơn, có lẽ là do công thức của nó thúc đẩy rõ ràng các đường đi. Mặt khác, các mô hình như **ConvKB** và **CapsE** đạt được kết quả đầy hứa hẹn trên các số liệu H@10 và MR, trong khi chúng dường như phải vật lộn với H@1 và MRR; hơn nữa, trong một số bộ dữ liệu, chúng bị cản trở rõ ràng bởi các vấn đề của chúng với các luật ràng buộc được mô tả trong Phần 5.4.1

Chúng tôi nhấn mạnh rằng trong nhiệm vụ LP, AnyburL dựa trên quy tắc chứng tỏ là một mô hình hoạt động tốt đáng chú ý, vì nó luôn được **xếp hạng** trong số các mô hình tốt nhất trên hầu hết các bộ dữ liệu và số liệu.
## The_importance_of_the_graph_structure
### Tầm quan trọng của cấu trúc đồ thị
Bài báo đã chỉ ra bằng chứng thực nghiệm nhất quán rằng các đặc điểm cấu trúc đồ thị có ảnh hưởng lớn đến những gì các mô hình quản lý để tìm hiểu và dự đoán.

Bài báo quan sát thấy rằng trong hầu hết tất cả các mô hình và bộ dữ liệu, các dự đoán dường như được tạo điều kiện thuận lợi bởi sự hiện diện của các **source peers** và bị cản trở bởi sự hiện diện của các **target peers**. Như đã đề cập, các **source peers** hoạt động như các ví dụ cho phép các mô hình mô tả rõ hơn mối quan hệ và mục tiêu để dự đoán, trong khi các **target peers** dẫn đến sự nhầm lẫn, khi họ cố gắng tối ưu hóa các **embeddings** để có quá nhiều câu trả lời khác nhau cho câu hỏi tương tự.

Bài báo cũng quan sát bằng chứng cho thấy rằng hầu hết tất cả các mô hình - ngay cả trên các mô hình chỉ học các sự kiện riêng lẻ trong đào tạo - dường như có thể tận dụng một số mức độ quan hệ và đường dẫn quan hệ.

Nói chung, các kịch bản khó khăn nhất cho các mô hình LP dường như diễn ra khi có các **target peers** tương đối nhiều hơn so với các **source peers**, kết hợp với sự hỗ trợ thấp được định hướng bởi các đường dẫn quan hệ **relational paths**. Trong những trường hợp này, mẫu dữ liệu thường có xu hướng thể hiện những màn biểu diễn khá không đạt yêu cầu. Bài báo tin rằng đây là những lĩnh vực mà nghiên cứu trong tương lai có nhiều cơ hội để cải thiện, và do đó, những thách thức lớn tiếp theo phải giải quyết trong lĩnh vực nghiên cứu LP.

Bài báo cũng chỉ ra những khác biệt thú vị trong hành vi và mối tương quan tùy thuộc vào các đặc trưng của bộ dữ liệu được sử dụng. Trong **FB15k** và **WN18**, cho thấy lỗ hỗng thử nghiệm mạnh, các hiệu suất mô hình cho thấy mối tương quan nổi bật với sự hỗ trợ được cung cấp bởi các đường dẫn quan hệ ngắn **shorter relational paths**, với độ dài 1 hoặc 2. Điều này có thể gây ra bởi các đường dẫn ngắn như vậy bao gồm các quan hệ có ý nghĩa nghịch đảo hoặc cùng ý nghĩa như các mối quan hệ trong các sự kiện **facts** để dự đoán. Ngược lại, trong **FB15k-237**, **WN18RR** và **YAGO3-10** của họ, không bị lỗ hổng thử nghiệm, các mô hình dường như cũng dựa vào các đường dẫn quan hệ dài hơn (3 bước), cũng như số lượng **source/target peers**.

Bài báo tin rằng điều này để lại chỗ cho những quan sát hấp dẫn. Với sự hiện diện của các **short patterns** rất ngắn cung cấp bằng chứng dự đoán áp đảo (ví dụ: các mối quan hệ nghịch đảo gây lỗ hỗng thử nghiệm **test leakage**), các mô hình dường như rất dễ tập trung vào chúng, coi thường các hình thức lý luận khác: đây có thể được coi là hậu quả không lành mạnh của kiểm tra sự cố rò rỉ **leakage**. Trong các kịch bản cân bằng hơn, ngược lại, các mô hình dường như điều tra ở một mức độ phụ thuộc dài hơn nhất định, cũng như tập trung nhiều hơn vào lý luận tương tự được hỗ trợ bởi các ví dụ (như các **source peers**).

Bài báo cũng quan sát rằng việc áp dụng các mô hình LP dựa trên **embeddings** để suy ra các mối quan hệ với số lượng lớn hơn 2 vẫn là một vấn đề mở. Như đã đề cập trong Phần 4.3.4, FreeBase KG đại diện cho các siêu cạnh **hyperedges** dưới dạng các node CVT. Hyperedges tạo thành phần lớn các cạnh trong FreeBase: như được lưu ý bởi **FHRi** [15] và **Wen** và cộng sự. [68], 61% các mối quan hệ FreeBase là ngoài nhị phân và **hyperedges** ứng liên quan đến hơn 1/3 các thực thể FreeBase. Các bộ dữ liệu **FB15k** và **FB15k-237** đã được xây dựng bằng cách thực hiện khai thác **S2C** trên các mẫu con FreeBase; điều này đã dẫn đến việc thay đổi đáng kể cả cấu trúc đồ thị và ngữ nghĩa của nó, với việc mất thông tin tổng thể. Bài báo tin rằng, để đánh giá hiệu quả của quá trình này, sẽ rất hiệu quả khi trích xuất các phiên bản mới của **FB15k** và **FB15k-237** trong cấu trúc ban đầu của chúng mà không áp dụng **S2C**. Bài báo cũng lưu ý rằng các mô hình như **m-TransH** [68] và **HypE** [15] gần đây đã cố gắng tránh các vấn đề này bằng cách phát triển các hệ thống có thể học hỏi rõ ràng các **hyperedges**. Mặc dù chúng có thể sử dụng về mặt kỹ thuật trên các bộ dữ liệu có quan hệ nhị phân, tất nhiên các đặc trưng độc đáo của chúng nổi lên tốt nhất khi xử lý các mối quan hệ ngoài nhị phân.

## The_importance _of_tie_policies
### Tầm quan trọng của các luật ràng buộc
Bài báo báo cáo rằng sự khác biệt trong các luật được sử dụng để xử lý các mối quan hệ điểm số có thể dẫn đến sự khác biệt lớn trong hiệu suất dự đoán trong đánh giá. Trên thực tế, các luật như vậy ngày nay được coi là chi tiết triển khai gần như không đáng kể và chúng hầu như không bao giờ được báo cáo khi trình bày các mô hình LP mới. Tuy nhiên, Bài báo cho thấy rằng các biểu diễn được tính toán dựa trên rủi ro luật khác nhau không thể so sánh trực tiếp với nhau và thậm chí có thể không phản ánh tính hiệu quả dự đoán thực tế của các mô hình. Vì vậy, bài báo khuyên các nhà nghiên cứu nên sử dụng luật tương tự trong tương lai; theo ý kiến ​​của trong bài báo, luật trung bình “average” có vẻ là sự lựa chọn hợp lý nhất. Bài báo cũng đã tìm thấy bằng chứng thực nghiệm mạnh mẽ cho thấy các chức hàm hoạt bão hòa, như **ReLU**, đóng vai trò chính trong các mô hình hàng đầu để gán cùng số điểm cho nhiều thực thể trong cùng một dự đoán; các xấp xỉ cũng có thể dẫn đến các hàm không bão hòa, như **Sigmoid**, hoạt động như bão hòa ở các khu vực nơi độ dốc của chúng đặc biệt gần bằng 0.

##  RELATED-WORKS
### CÔNG TRÌNH LIÊN QUAN