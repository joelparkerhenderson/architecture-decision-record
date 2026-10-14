# Mẫu Bản ghi Quyết định Kiến trúc (ADR) <!-- Replace with ADR title -->

Đây là mẫu cho ADR của EdgeX Foundry.

Nguồn: https://docs.edgexfoundry.org/2.3/design/adr/template/


### Người đệ trình

Liệt kê những người đệ trình ADR.

Định dạng:

- Tên (Tổ chức)


## Nhật ký thay đổi

Liệt kê các thay đổi đối với tài liệu, bao gồm trạng thái, ngày và URL của PR.

Trạng thái là một trong: pending, approved, amended, deprecated.

Ngày là một chuỗi ISO 8601 (YYYY-MM-DD).

PR là pull request đã đệ trình thay đổi, bao gồm thông tin như diff, những người đóng góp và người xem xét.

Định dạng:

- \[Trạng thái của ADR, ví dụ approved, amended, v.v.\]\(URL của pull request\) YYYY-MM-DD


## Các trường hợp sử dụng được tham chiếu

Liệt kê tất cả các tài liệu trường hợp sử dụng / yêu cầu liên quan.

ADR yêu cầu ít nhất một trường hợp sử dụng liên quan và đã được phê duyệt.

Định dạng:

- \[Tên trường hợp sử dụng\]\(URL\)

Thêm giải thích nếu ADR không giải quyết tất cả các yêu cầu của một trường hợp sử dụng.


## Bối cảnh

Mô tả:

- thiết kế quan trọng về mặt kiến trúc như thế nào - đủ để cần một ADR (thay vì chỉ một issue và PR đơn giản để sửa một vấn đề)

- cách tiếp cận thiết kế ở mức cao (chi tiết được mô tả trong thiết kế đề xuất bên dưới)


## Thiết kế đề xuất

Chi tiết của thiết kế (không đi sâu vào triển khai nếu có thể).

Phác thảo:

- các dịch vụ/mô-đun bị ảnh hưởng (thay đổi)

- các dịch vụ/mô-đun mới được thêm vào

- tác động đến mô hình và DTO (thay đổi/thêm/xóa)

- tác động đến API (thay đổi/thêm/xóa)

- tác động đến cấu hình chung (thiết lập các phần mới, thay đổi/thêm/xóa)

- tác động đến devops


## Cân nhắc

Ghi lại các phương án thay thế, mối quan ngại, các vấn đề phụ trợ hoặc liên quan, và các câu hỏi nảy sinh trong cuộc tranh luận về ADR. 

Cho biết chúng đã được giải quyết hoặc giảm nhẹ hay không và bằng cách nào.


## Quyết định

Ghi lại bất kỳ chi tiết triển khai quan trọng nào đã được thống nhất, các lưu ý, các cân nhắc trong tương lai, các vấn đề thiết kế còn lại hoặc bị hoãn.

Ghi lại bất kỳ phần nào của yêu cầu không được thiết kế đề xuất đáp ứng.


## Các ADR liên quan khác

Liệt kê bất kỳ ADR liên quan nào - chẳng hạn một quyết định thiết kế cho một thành phần con của một tính năng, một thiết kế bị loại bỏ do thiết kế này, v.v.. 

Định dạng:

- \[Tiêu đề ADR\]\(URL\) - Mức độ liên quan


## Tài liệu tham khảo

Liệt kê các tài liệu tham khảo bổ sung.

Định dạng:

- \[Tiêu đề\]\(URL\)

