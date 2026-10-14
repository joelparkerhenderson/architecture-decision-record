# Cấu hình biến môi trường

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
  * [Hàm ý ](#hàm-ý)
* [Liên quan](#liên-quan)
  * [Các quyết định liên quan](#các-quyết-định-liên-quan)
  * [Các yêu cầu liên quan](#các-yêu-cầu-liên-quan)
  * [Các tạo phẩm liên quan](#các-tạo-phẩm-liên-quan)
  * [Các nguyên tắc liên quan](#các-nguyên-tắc-liên-quan)
* [Ghi chú](#ghi-chú)


## Tóm tắt


### Vấn đề

Chúng tôi muốn các ứng dụng của mình có thể cấu hình ngoài tạo phẩm/tệp nhị phân/mã nguồn, sao cho một bản build có thể hoạt động khác nhau tùy theo môi trường triển khai.

  * Để đạt được điều này, chúng tôi muốn dùng cấu hình biến môi trường.

  * Chúng tôi muốn quản lý cấu hình bằng các tệp mà chúng tôi có thể kiểm soát phiên bản.

  * Chúng tôi muốn cung cấp một số tiện dụng về trải nghiệm nhà phát triển, chẳng hạn biết những gì có thể cấu hình và các giá trị mặc định liên quan.


### Quyết định

Đã quyết định chọn các tệp .env kèm tệp mặc định và tệp lược đồ liên quan.


### Trạng thái

Đã quyết định. Mở để cân nhắc các khả năng mới khi chúng xuất hiện.


## Chi tiết


### Giả định

Chúng tôi ưu tiên tách mã ứng dụng khỏi mã môi trường. Chúng tôi giả định ứng dụng cần hoạt động khác nhau trong các môi trường khác nhau, chẳng hạn môi trường phát triển, môi trường kiểm thử, môi trường demo, môi trường sản xuất, v.v.

Chúng tôi ủng hộ thực hành của ngành là "12 factor app" và thậm chí hơn là thực hành liên quan "15 factor app".

Nhiều dự án trước đây của chúng tôi đã dùng quy ước một tệp `.env` hoặc một thư mục `.env` tương tự. Có một thực hành điển hình là giữ chúng ngoài kiểm soát phiên bản, và thay vào đó dùng một cách khác để triển khai, đánh phiên bản và quản lý chúng.


### Ràng buộc

Chúng tôi muốn giữ các bí mật ngoài hệ thống kiểm soát phiên bản (VCS) quản lý mã nguồn (SCM) của mình.

Chúng tôi muốn hướng tới khả năng tương thích với các framework và thư viện phần mềm phổ biến. Ví dụ, Node có mô-đun "dotenv" để đọc cấu hình biến môi trường.


### Lập trường

Chúng tôi đã cân nhắc một vài cách tiếp cận:

  * Lưu cấu hình trong ứng dụng, chẳng hạn trong một tệp `config.js`.

  * Lưu cấu hình trong môi trường, chẳng hạn trong một tệp `.env`.

  * Lấy cấu hình từ một vị trí đã biết, chẳng hạn máy chủ cấp phép.


### Lập luận

Chúng tôi chọn cách tiếp cận tệp .env vì:

  * Nó phổ biến, kể cả trong giới chuyên gia.

  * Nó theo mẫu các tệp `.env` mà các nhóm của chúng tôi đã dùng thành công nhiều lần trong nhiều dự án.

  * Nó đơn giản. Đáng chú ý, hiện tại chúng tôi chấp nhận được các đánh đổi đáng kể mà chúng tôi nhìn thấy, chẳng hạn thiếu khả năng kiểm toán so với cách tiếp cận máy chủ cấp phép.


### Hàm ý 

Chúng tôi cần tìm cách tách cấu hình biến môi trường công khai khỏi mọi việc quản lý bí mật.


## Liên quan


### Các quyết định liên quan

Chúng tôi kỳ vọng tất cả ứng dụng của mình dùng cách tiếp cận này.

Chúng tôi sẽ lên kế hoạch nâng cấp bất kỳ ứng dụng nào dùng cách tiếp cận kém khả năng hơn, chẳng hạn mã hóa cứng trong tệp nhị phân hoặc trong mã nguồn.

Chúng tôi sẽ giữ nguyên bất kỳ ứng dụng nào dùng cách tiếp cận có nhiều khả năng hơn, chẳng hạn máy chủ cấp phép.


### Các yêu cầu liên quan

Chúng tôi sẽ thêm các khả năng devops cho các tệp, bao gồm hook, kiểm thử và tích hợp liên tục.

Chúng tôi cần đào tạo tất cả đồng đội là nhà phát triển về quyết định này.



### Các tạo phẩm liên quan

Mỗi khu vực mà chúng tôi triển khai sẽ cần tệp .env riêng và các tệp liên quan.


### Các nguyên tắc liên quan

Dễ đảo ngược.


## Ghi chú


Tệp `.env` ví dụ:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Tệp `.env.defaults` ví dụ:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Tệp `.env.schema` ví dụ chỉ có các khóa:

```env
NAME
EMAIL
```
