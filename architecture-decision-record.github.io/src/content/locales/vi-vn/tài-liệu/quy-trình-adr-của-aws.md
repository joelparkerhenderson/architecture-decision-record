# Quy trình Bản ghi Quyết định Kiến trúc của AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Bản ghi quyết định kiến trúc (architectural decision record, ADR) là một tài liệu mô tả lựa chọn mà nhóm đưa ra về một khía cạnh quan trọng của kiến trúc phần mềm mà họ đang lên kế hoạch xây dựng. Mỗi ADR mô tả quyết định kiến trúc, bối cảnh và hệ quả của nó. ADR có các trạng thái và do đó tuân theo một vòng đời. Để xem ví dụ về ADR, hãy xem phụ lục.

Quy trình ADR tạo ra một tập hợp các bản ghi quyết định kiến trúc. Tập hợp này tạo thành nhật ký quyết định. Nhật ký quyết định cung cấp bối cảnh dự án cũng như thông tin chi tiết về triển khai và thiết kế. Các thành viên dự án đọc lướt tiêu đề của từng ADR để nắm tổng quan về bối cảnh dự án. Họ đọc các ADR để đi sâu vào việc triển khai dự án và các lựa chọn thiết kế.

Khi nhóm chấp nhận một ADR, ADR đó trở nên bất biến. Nếu những hiểu biết mới đòi hỏi một quyết định khác, nhóm đề xuất một ADR mới. Khi nhóm chấp nhận ADR mới, ADR mới sẽ thay thế ADR trước đó.

## Phạm vi của quy trình ADR

Các thành viên dự án nên tạo ADR cho mọi quyết định quan trọng về mặt kiến trúc ảnh hưởng đến dự án hoặc sản phẩm phần mềm, bao gồm những điều sau (Richards và Ford 2020):

* Cấu trúc (ví dụ, các mẫu hình như microservices)

* Yêu cầu phi chức năng (bảo mật, tính sẵn sàng cao và khả năng chịu lỗi)

* Phụ thuộc (sự ghép nối giữa các thành phần)

* Giao diện (API và các hợp đồng đã công bố)

* Kỹ thuật xây dựng (thư viện, framework, công cụ và quy trình)

* Các yêu cầu chức năng và phi chức năng là đầu vào phổ biến nhất của quy trình ADR.


## Nội dung của ADR

Khi nhóm xác định nhu cầu về một ADR, một thành viên trong nhóm bắt đầu viết ADR dựa trên mẫu áp dụng cho toàn dự án. (Xem tổ chức ADR trên GitHub để biết các mẫu ví dụ.) Mẫu giúp đơn giản hóa việc tạo ADR và đảm bảo ADR ghi lại mọi thông tin liên quan. Tối thiểu, mỗi ADR phải xác định bối cảnh của quyết định, bản thân quyết định, và hệ quả của quyết định đối với dự án và các sản phẩm bàn giao của nó. (Để xem ví dụ về các phần này, hãy xem phụ lục.) Một trong những khía cạnh mạnh mẽ nhất của cấu trúc ADR là nó tập trung vào lý do đằng sau quyết định thay vì cách nhóm triển khai nó. Hiểu được tại sao nhóm đưa ra quyết định giúp các thành viên khác dễ chấp nhận quyết định hơn, và ngăn các kiến trúc sư khác không tham gia vào quá trình ra quyết định bác bỏ quyết định đó trong tương lai.


## Quy trình áp dụng ADR

Mọi thành viên trong nhóm đều có thể tạo ADR, nhưng nhóm nên thiết lập một định nghĩa về quyền sở hữu đối với ADR. Mỗi tác giả là chủ sở hữu của một ADR nên chủ động duy trì và truyền đạt nội dung ADR. Để làm rõ quyền sở hữu này, hướng dẫn này gọi các tác giả ADR là chủ sở hữu ADR trong các phần sau. Các thành viên khác trong nhóm luôn có thể đóng góp cho một ADR. Nếu nội dung của ADR thay đổi trước khi nhóm chấp nhận ADR, chủ sở hữu nên phê duyệt những thay đổi này.

Sau khi nhóm xác định một quyết định kiến trúc và chủ sở hữu của nó, chủ sở hữu ADR đưa ra ADR ở trạng thái **Proposed** (Đã đề xuất) ngay từ đầu quy trình. Các ADR ở trạng thái Proposed đã sẵn sàng để được xem xét.

Sau đó, chủ sở hữu ADR bắt đầu quy trình xem xét ADR. Mục tiêu của quy trình xem xét ADR là quyết định xem nhóm có chấp nhận ADR, xác định rằng nó cần làm lại, hay bác bỏ ADR. Nhóm dự án, bao gồm cả chủ sở hữu, xem xét ADR. Cuộc họp xem xét nên bắt đầu bằng một khoảng thời gian riêng để đọc ADR. Trung bình, 10 đến 15 phút là đủ. Trong thời gian này, mỗi thành viên trong nhóm đọc tài liệu và thêm nhận xét và câu hỏi để đánh dấu các chủ đề chưa rõ ràng. Sau giai đoạn xem xét, chủ sở hữu ADR đọc to và thảo luận từng nhận xét với nhóm.

Nếu nhóm tìm thấy các đầu việc để cải thiện ADR, trạng thái của ADR vẫn là **Proposed**. Chủ sở hữu ADR đưa ra các hành động và, phối hợp với nhóm, giao người thực hiện cho từng hành động. Mỗi thành viên trong nhóm có thể đóng góp và giải quyết các đầu việc. Chủ sở hữu ADR có trách nhiệm lên lịch lại quy trình xem xét.

Nhóm cũng có thể quyết định bác bỏ ADR. Trong trường hợp này, chủ sở hữu ADR thêm lý do bác bỏ để ngăn các cuộc thảo luận tương tự về cùng chủ đề trong tương lai. Chủ sở hữu đổi trạng thái ADR thành **Rejected** (Đã bác bỏ).

Nếu nhóm phê duyệt ADR, chủ sở hữu thêm dấu thời gian, phiên bản và danh sách các bên liên quan. Sau đó chủ sở hữu cập nhật trạng thái thành **Accepted** (Đã chấp nhận).

Các ADR và nhật ký quyết định mà chúng tạo ra đại diện cho các quyết định do nhóm đưa ra và cung cấp lịch sử của mọi quyết định. Nhóm sử dụng các ADR làm tài liệu tham chiếu trong các buổi xem xét mã và kiến trúc khi có thể. Ngoài việc thực hiện xem xét mã, các nhiệm vụ thiết kế và triển khai, các thành viên trong nhóm nên tham khảo các ADR cho các quyết định chiến lược của sản phẩm.

Theo thông lệ tốt, mỗi thay đổi phần mềm nên trải qua đánh giá chéo và yêu cầu ít nhất một lần phê duyệt. Trong quá trình xem xét mã, người xem xét có thể phát hiện các thay đổi vi phạm một hoặc nhiều ADR. Trong trường hợp này, người xem xét yêu cầu tác giả của thay đổi mã cập nhật mã và chia sẻ liên kết tới ADR. Khi tác giả cập nhật mã, nó được các người đánh giá chéo phê duyệt và hợp nhất vào cơ sở mã chính.


## Quy trình xem xét ADR

Nhóm nên coi các ADR là tài liệu bất biến sau khi nhóm chấp nhận hoặc bác bỏ chúng. Việc thay đổi một ADR hiện có đòi hỏi phải tạo một ADR mới, thiết lập quy trình xem xét cho ADR mới và phê duyệt ADR đó. Nếu nhóm phê duyệt ADR mới, chủ sở hữu nên đổi trạng thái của ADR cũ thành **Superseded** (Đã bị thay thế). 
