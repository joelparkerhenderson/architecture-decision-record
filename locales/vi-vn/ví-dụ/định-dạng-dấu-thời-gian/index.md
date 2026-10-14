# Định dạng dấu thời gian

Nội dung:

* [Tóm tắt](#tóm-tắt)
  * [Vấn đề](#vấn-đề)
  * [Quyết định](#quyết-định)
  * [Trạng thái](#trạng-thái)
* [Chi tiết](#chi-tiết)
  * [Giả định](#giả-định)
  * [Ràng buộc](#ràng-buộc)
  * [Lập trường](#lập-trường)
  * [Lập luận](#lập-luận)
  * [Hàm ý](#hàm-ý)
* [Liên quan](#liên-quan)
  * [Các quyết định liên quan](#các-quyết-định-liên-quan)
  * [Các yêu cầu liên quan](#các-yêu-cầu-liên-quan)
  * [Các tạo phẩm liên quan](#các-tạo-phẩm-liên-quan)
  * [Các nguyên tắc liên quan](#các-nguyên-tắc-liên-quan)
* [Ghi chú](#ghi-chú)


## Tóm tắt


### Vấn đề

Chúng tôi muốn có thể theo dõi khi nào sự việc xảy ra bằng cách dùng các dấu thời gian và bằng cách dùng một định dạng dấu thời gian nhất quán hoạt động tốt trên tất cả các hệ thống của chúng tôi và các hệ thống bên thứ ba.

Chúng tôi tương tác với các hệ thống có định dạng dấu thời gian khác nhau:

* Thông điệp JSON không có định dạng dấu thời gian gốc, nên chúng tôi cần chọn cách chuyển một dấu thời gian thành chuỗi, và chuyển một chuỗi thành dấu thời gian, tức là cách tuần tự hóa/giải tuần tự hóa.

* Một số ứng dụng được đặt để dùng giờ địa phương, thay vì giờ UTC. Điều này có thể thuận tiện cho các dự án phải điều chỉnh theo giờ địa phương, như các dự án kích hoạt các sự kiện dựa trên giờ địa phương.

* Một số hệ thống có nhu cầu và khả năng về độ chính xác thời gian khác nhau, như dùng độ phân giải thời gian giây so với mili giây so với nano giây. Ví dụ, lệnh `date` của hệ điều hành Linux dùng độ chính xác thời gian mặc định là giây, trong khi sàn giao dịch chứng khoán Nasdaq muốn độ chính xác thời gian mặc định là nano giây.


### Quyết định

Chúng tôi chọn định dạng chuẩn dấu thời gian ISO 8601 với độ chính xác nano giây, cụ thể là "YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ".

Định dạng này hiển thị năm, tháng, ngày, giờ, phút, giây, nano giây và múi giờ Zulu còn gọi là UTC, GMT.


### Trạng thái

Đã quyết định.


## Chi tiết


### Giả định

Chúng tôi cần xử lý các chuỗi văn bản dấu thời gian này, để chuyển từ dấu thời gian sang chuỗi (còn gọi là tuần tự hóa) và chuyển từ chuỗi sang dấu thời gian (còn gọi là giải tuần tự hóa).

Chúng tôi muốn một định dạng nhìn chung dễ dùng, dễ chuyển đổi và dễ đọc đối với con người.

Chúng tôi muốn tương thích với nhiều hệ thống bên ngoài mà chúng tôi không kiểm soát được, như hệ thống phân tích, hệ thống cơ sở dữ liệu, hệ thống tài chính.


### Ràng buộc

Một số hệ thống có giới hạn về độ chính xác thời gian. Ví dụ, lệnh `date` của hệ điều hành macOS có thể in độ chính xác thời gian theo giây, nhưng không theo nano giây.


### Lập trường

Chúng tôi đã cân nhắc một loạt lựa chọn:

* Unix epoch tức là một số tăng dần.

* Định dạng văn bản ngắn gọn "YYYYMMDDTHHMMSSNNNNNNNNN".

* Dùng múi giờ địa phương so với múi giờ UTC.


### Lập luận

Với việc dùng điển hình, chúng tôi coi trọng việc dễ đọc/viết bởi con người hơn tốc độ/kích thước thô.

Với việc dùng điển hình, chúng tôi muốn một định dạng hoạt động tốt trong các hệ thống máy, và cũng hoạt động tốt khi làm thủ công, như viết dữ liệu mẫu, đọc đầu ra JSON, grep một tệp nhật ký, v.v.

Với việc dùng không điển hình, như điện toán hiệu năng cao, chúng tôi kỳ vọng sẽ muốn tối ưu bất kỳ định dạng văn bản nào chúng tôi chọn bằng cách chuyển văn bản sang một định dạng nhanh hơn, như kiểu đối tượng ngày tháng tích hợp sẵn của một ngôn ngữ lập trình. Vì vậy định dạng văn bản không quan trọng lắm đối với HPC.


### Hàm ý

Các hệ thống văn bản và hệ thống thời gian khác nhau của chúng tôi sẽ hội tụ về định dạng này.


## Liên quan


### Các quyết định liên quan

Chúng tôi có thể muốn một cách nhanh/dễ để cũng theo dõi các độ lệch thời gian còn gọi là khoảng thời gian. Những thứ này dễ với các dấu thời gian Unix epoch.


### Các yêu cầu liên quan

Chúng tôi có thể muốn điều chỉnh quyết định của mình ví dụ nếu chúng tôi có yêu cầu liên quan đến một loại dấu thời gian thông điệp nhật ký cụ thể, như cho Splunk, Sumo, ELK, v.v.


### Các tạo phẩm liên quan

Bộ định dạng và bộ phân tích cú pháp ngôn ngữ:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Các ví dụ Rosetta Code:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Các ví dụ SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Các nguyên tắc liên quan

Dễ đảo ngược. Chúng tôi có thể đổi khá dễ sang một định dạng khác, như Unix epoch.

Hoãn tối ưu hóa sớm. Với việc dùng điển hình, chúng tôi không quan tâm nhiều đến vài ký tự thừa như một định dạng dùng dấu gạch ngang và dấu hai chấm.


## Ghi chú

Thêm ghi chú ở đây.
