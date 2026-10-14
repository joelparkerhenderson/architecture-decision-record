# Bản ghi quyết định kiến trúc: snake_case so với camelCase cho một REST API?

Quyết định: quy ước đặt tên snake_case sẽ được dùng cho các endpoint REST API

Trạng thái: Đã chấp nhận

## Bối cảnh

Trong các quy ước đặt tên cho REST API, có hai định dạng phổ biến: snake_case và camelCase. Định dạng snake_case là khi mỗi từ trong tên được phân tách bằng dấu gạch dưới, còn camelCase là khi từ đầu tiên của tên viết thường, và các từ tiếp theo có chữ cái đầu viết hoa. Quyết định này sẽ xác định quy ước đặt tên nào nên được dùng cho một REST API.

## Các yếu tố thúc đẩy quyết định

- Nhất quán với các quy ước đặt tên hiện có trong dự án

- Dễ đọc và rõ ràng cho bất kỳ ai có thể làm việc với API

- Phù hợp với các thực hành tốt nhất của ngành cho quy ước đặt tên REST API

- Dễ triển khai và bảo trì

## Quyết định

Quy ước đặt tên snake_case sẽ được dùng cho các endpoint REST API. Lựa chọn này được thúc đẩy bởi các yếu tố sau:

1. **Tính nhất quán**: Dự án đã dùng quy ước đặt tên snake_case cho tất cả các endpoint, và sẽ có lợi khi duy trì quy ước này để đảm bảo tính nhất quán trong toàn dự án.

2. **Dễ đọc và rõ ràng**: Quy ước snake_case dễ đọc hơn và dễ hiểu hơn. Dấu gạch dưới tạo sự phân tách rõ ràng giữa các từ, giúp dễ phân tích và hiểu ý nghĩa của tên hơn.

3. **Phù hợp với các thực hành tốt nhất của ngành**: Quy ước snake_case được dùng rộng rãi trong ngành và được coi là thực hành tốt nhất cho REST API, khiến nó là lựa chọn tốt cho dự án.

4. **Dễ triển khai và bảo trì**: Giữ nguyên quy ước đặt tên hiện có dễ triển khai và bảo trì hơn vì mọi mã và tài liệu hiện có sẽ cần được cập nhật nếu chọn một quy ước mới.

## Hệ quả

Có những hệ quả tiềm ẩn của quyết định này. 

* Nếu bất kỳ thành viên mới nào tham gia dự án không quen với quy ước đặt tên snake_case, điều đó có thể dẫn đến nhầm lẫn và sai sót trong phát triển. Tuy nhiên, vì snake_case là một quy ước được dùng rộng rãi, rủi ro như vậy là tối thiểu. 
  
* Nếu các công cụ hoặc framework khác được dùng trong dự án dựa nhiều vào quy ước camelCase, có thể cần thêm công sức để chuyển đổi giữa các quy ước đặt tên. Tuy nhiên, đó không phải mối quan ngại đáng kể vì dự án đã chuẩn hóa theo quy ước snake_case. 
 
Nhìn chung, quyết định dùng quy ước đặt tên snake_case cho các endpoint REST API tạo ra một cách tiếp cận nhất quán, dễ đọc và theo tiêu chuẩn ngành đồng thời dễ triển khai và bảo trì.

<h6>Ghi công: trang này được tạo bởi ChatGPT, sau đó được chỉnh sửa cho rõ ràng và đúng định dạng.</h6>
