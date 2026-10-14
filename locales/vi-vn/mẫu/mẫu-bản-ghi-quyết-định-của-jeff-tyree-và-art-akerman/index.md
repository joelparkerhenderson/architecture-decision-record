# Mẫu bản ghi quyết định của Jeff Tyree và Art Akerman

Đây là mẫu mô tả quyết định kiến trúc được công bố trong ["Architecture Decisions: Demystifying Architecture" của Jeff Tyree và Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Vấn đề (Issue)**: Mô tả vấn đề thiết kế kiến trúc mà bạn đang giải quyết, không để lại câu hỏi nào về lý do bạn giải quyết vấn đề này vào lúc này. Theo cách tiếp cận tối giản, chỉ giải quyết và lập tài liệu các vấn đề cần giải quyết tại các thời điểm khác nhau trong vòng đời.

* **Quyết định (Decision)**: Nêu rõ định hướng của kiến trúc, tức là lập trường mà bạn đã chọn.

* **Trạng thái (Status)**: Trạng thái của quyết định, chẳng hạn pending, decided hoặc approved.

* **Nhóm (Group)**: Bạn có thể dùng một cách phân nhóm đơn giản, chẳng hạn tích hợp, trình bày, dữ liệu, v.v., để giúp sắp xếp tập hợp các quyết định. Bạn cũng có thể dùng một bản thể luận kiến trúc tinh vi hơn, chẳng hạn của John Kyaruzi và Jan van Katwijk, bao gồm các danh mục trừu tượng hơn như sự kiện, lịch và vị trí. Ví dụ, với bản thể luận này, bạn sẽ nhóm các quyết định liên quan đến các sự việc mà hệ thống cần thông tin dưới mục sự kiện.

* **Giả định (Assumptions)**: Mô tả rõ ràng các giả định nền tảng trong môi trường mà bạn đưa ra quyết định, như chi phí, lịch trình, công nghệ, v.v. Lưu ý rằng các ràng buộc môi trường (như các tiêu chuẩn công nghệ được chấp nhận, kiến trúc doanh nghiệp, các mẫu hình thường dùng, v.v.) có thể hạn chế các phương án bạn cân nhắc.

* **Ràng buộc (Constraints)**: Ghi lại bất kỳ ràng buộc bổ sung nào đối với môi trường mà phương án được chọn (quyết định) có thể đặt ra.

* **Lập trường (Positions)**: Liệt kê các lập trường (các lựa chọn hoặc phương án khả thi) mà bạn đã cân nhắc. Những điều này thường đòi hỏi các giải thích dài, đôi khi cả mô hình và sơ đồ. Đây không phải là danh sách đầy đủ. Tuy nhiên, bạn không muốn nghe câu hỏi "Bạn đã nghĩ đến... chưa?" trong buổi xem xét cuối cùng; điều này dẫn đến mất uy tín và nghi ngờ các quyết định kiến trúc khác. Phần này cũng giúp đảm bảo rằng bạn đã lắng nghe ý kiến của người khác; việc nêu rõ các ý kiến khác giúp thu hút những người ủng hộ chúng vào quyết định của bạn.

* **Lập luận (Argument)**: Phác thảo lý do bạn chọn một lập trường, bao gồm các mục như chi phí triển khai, tổng chi phí sở hữu, thời gian đưa ra thị trường và tính sẵn có của các nguồn lực phát triển cần thiết. Điều này có lẽ quan trọng không kém bản thân quyết định.

* **Hàm ý (Implications)**: Một quyết định đi kèm nhiều hàm ý, như siêu mô hình REMAP chỉ ra. Ví dụ, một quyết định có thể đặt ra nhu cầu đưa ra các quyết định khác, tạo ra yêu cầu mới, hoặc sửa đổi các yêu cầu hiện có; đặt thêm các ràng buộc đối với môi trường; đòi hỏi thương lượng lại phạm vi hoặc lịch trình với khách hàng; hoặc đòi hỏi đào tạo nhân viên bổ sung. Hiểu rõ và nêu rõ các hàm ý của quyết định có thể rất hiệu quả trong việc tạo sự đồng thuận và xây dựng lộ trình thực thi kiến trúc.

* **Các quyết định liên quan**: Rõ ràng là nhiều quyết định có liên quan với nhau; bạn có thể liệt kê chúng ở đây. Tuy nhiên, chúng tôi nhận thấy trong thực tế, ma trận truy vết, cây quyết định hoặc siêu mô hình hữu ích hơn. Siêu mô hình hữu ích để thể hiện các mối quan hệ phức tạp dưới dạng sơ đồ (như các mô hình Rose).

* **Các yêu cầu liên quan**: Các quyết định nên được định hướng bởi kinh doanh. Để thể hiện trách nhiệm giải trình, hãy ánh xạ tường minh các quyết định của bạn tới các mục tiêu hoặc yêu cầu. Bạn có thể liệt kê các yêu cầu liên quan này ở đây, nhưng chúng tôi thấy tham chiếu tới một ma trận truy vết tiện hơn. Bạn có thể đánh giá đóng góp của từng quyết định kiến trúc vào việc đáp ứng từng yêu cầu, rồi đánh giá mức độ yêu cầu được đáp ứng qua tất cả các quyết định. Nếu một quyết định không đóng góp vào việc đáp ứng một yêu cầu, đừng đưa ra quyết định đó.

* **Các tạo phẩm liên quan**: Liệt kê các tài liệu kiến trúc, thiết kế hoặc phạm vi liên quan mà quyết định này ảnh hưởng.

* **Các nguyên tắc liên quan**: Nếu doanh nghiệp có một bộ nguyên tắc đã thống nhất, hãy bảo đảm quyết định nhất quán với một hoặc nhiều nguyên tắc đó. Điều này giúp bảo đảm sự phù hợp giữa các lĩnh vực hoặc hệ thống.

* **Ghi chú**: Vì quá trình ra quyết định có thể mất hàng tuần, chúng tôi thấy hữu ích khi ghi lại các ghi chú và vấn đề mà nhóm thảo luận trong quá trình phổ biến.

