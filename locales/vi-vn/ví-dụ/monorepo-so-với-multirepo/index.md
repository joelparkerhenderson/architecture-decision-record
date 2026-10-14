# Monorepo so với multirepo

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

Dự án của chúng tôi liên quan đến việc phát triển ba loại phần mềm chính:

  * GUI front-end
  * Dịch vụ middleware
  * Máy chủ back-end

Khi phát triển, hệ thống kiểm soát phiên bản (VCS) quản lý mã nguồn (SCM) của chúng tôi là git.

Chúng tôi cần chọn cách dùng git để tổ chức mã của mình.

Lựa chọn cấp cao nhất là tổ chức theo kiểu "monorepo" hoặc "polyrepo" hoặc "lai":

  * Monorepo nghĩa là chúng tôi đặt mọi thành phần vào một kho lớn
  * Polyrepo nghĩa là chúng tôi đặt mỗi thành phần vào kho riêng của nó
  * Lai nghĩa là một sự pha trộn nào đó giữa monorepo và polyrepo

Để biết thêm, xem https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Quyết định

Monorepo khi một tổ chức/nhóm/dự án còn tương đối nhỏ, và việc lặp nhanh được ưu tiên hơn việc duy trì sự ổn định.

Polyrepo khi một tổ chức/nhóm/dự án tương đối lớn, và việc duy trì sự ổn định được ưu tiên hơn việc lặp nhanh.


### Trạng thái

Đã quyết định. Mở để xem xét lại nếu/khi có công cụ mới để quản lý monorepo và/hoặc polyrepo.


## Chi tiết


### Giả định

Tất cả mã mà chúng tôi đang phát triển là cho các sản phẩm của một tổ chức, không phải cho công chúng. Tức là Công ty Môi giới-Đại lý không nhắm đến việc có thứ gì đó như các nhà phát triển tình nguyện từ công chúng.


### Ràng buộc

Các ràng buộc được ghi chép tốt tại https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Lập trường

Chúng tôi đã cân nhắc các monorepo theo phong cách Google, Facebook, v.v. Chúng tôi cho rằng mọi vấn đề mở rộng của monorepo còn rất xa trong tương lai nên chúng tôi sẽ có thể tận dụng các thực hành giống Google và Facebook khi cần đến chúng.

Chúng tôi đã cân nhắc các polyrepo theo phong cách các dự án mã nguồn mở Git điển hình, như Google Android, Facebook React, v.v. Chúng tôi cho rằng đây là lựa chọn tốt nhất cho sự tham gia của công chúng (ví dụ bất kỳ ai trên thế giới đều có thể làm việc với mã) và tính sẵn có riêng lẻ (ví dụ dự án được dùng độc lập, không cần bất kỳ thành phần nào khác).


### Lập luận

Khi một tổ chức/nhóm/dự án còn tương đối nhỏ, chúng tôi chọn monorepo, vì việc lặp nhanh được ưu tiên cao hơn đáng kể so với việc duy trì sự ổn định

Khi một tổ chức/nhóm/dự án tương đối lớn, chúng tôi chọn polyrepo, vì việc duy trì sự ổn định được ưu tiên cao hơn đáng kể so với việc lặp nhanh.


### Hàm ý

Nếu đã có sẵn một pipeline cho CI+CD, chúng tôi có thể cần điều chỉnh nó để kiểm thử nhiều dự án trong một kho.

CI+CD có thể mất nhiều thời gian hơn cho một bản build đầy đủ của monorepo, vì CI+CD có thể build tất cả các dự án trong monorepo.

Nếu một tổ chức/nhóm/dự án phát triển, monorepo sẽ có các vấn đề về mở rộng.

Các vấn đề mở rộng của monorepo có thể khiến việc chuyển sang polyrepo ngày càng có giá trị.

Việc chuyển từ monorepo sang polyrepo là một nhiệm vụ devops đáng kể, và sẽ cần được lên kế hoạch, quản lý và lập trình.


## Liên quan


### Các quyết định liên quan

Chúng tôi sẽ tạo các quyết định cho các công cụ liên quan để quản lý monorepo (ví dụ Google Bazel) và polyrepo (ví dụ Lyft Refactorator).


### Các yêu cầu liên quan

Chúng tôi cần phát triển pipeline CI+CD để hoạt động tốt với git.


### Các tạo phẩm liên quan

Chúng tôi kỳ vọng tổ chức kho có các tạo phẩm liên quan cho cấp phát, quản lý cấu hình, kiểm thử và các lĩnh vực devops tương tự. 


### Các nguyên tắc liên quan

Dễ đảo ngược. Nếu monorepo không hiệu quả trong thực tế, hoặc ban lãnh đạo không muốn, thì việc chuyển sang polyrepo rất đơn giản.

Ám ảnh khách hàng. Chúng tôi coi trọng việc đưa dự án đến tay khách hàng, và chúng tôi tin rằng monorepo có thể đưa chúng tôi đến đó nhanh hơn polyrepo, và cũng giúp chúng tôi lặp nhanh hơn.

Nghĩ lớn. Google và Facebook là những người ủng hộ rất mạnh mẽ monorepo hơn polyrepo, vì tất cả các sản phẩm cốt lõi có thể được phát triển/kiểm thử/triển khai đồng bộ.


## Ghi chú

Thêm bất kỳ ghi chú nào ở đây.
