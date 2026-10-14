# Bản ghi quyết định kiến trúc: Chọn công nghệ cơ sở dữ liệu

## Trạng thái

Đã chấp nhận

## Bối cảnh

Chúng tôi đang thiết kế một ứng dụng mới đòi hỏi lưu trữ và truy xuất dữ liệu theo cách có khả năng mở rộng và hiệu năng cao. Chúng tôi đã xác định ba loại công nghệ cơ sở dữ liệu thường được sử dụng: cơ sở dữ liệu quan hệ, cơ sở dữ liệu tài liệu và cơ sở dữ liệu sự kiện.

Cơ sở dữ liệu quan hệ lưu trữ dữ liệu trong các bảng với lược đồ cố định và áp dụng các ràng buộc toàn vẹn dữ liệu nghiêm ngặt. Chúng phù hợp với các ứng dụng cần các quan hệ dữ liệu phức tạp và giao dịch. Ví dụ gồm MySQL, PostgreSQL và Oracle.

Cơ sở dữ liệu tài liệu lưu trữ dữ liệu trong các tài liệu giống JSON và không có lược đồ. Chúng rất phù hợp với các ứng dụng cần mô hình dữ liệu linh hoạt và mở rộng theo chiều ngang. Ví dụ gồm MongoDB, Couchbase và Amazon DynamoDB.

Cơ sở dữ liệu sự kiện lưu trữ dữ liệu dưới dạng một chuỗi các sự kiện, ghi lại mọi thay đổi đối với dữ liệu. Chúng phù hợp với các ứng dụng cần kiểm toán, event sourcing và xử lý dữ liệu phức tạp. Ví dụ gồm Apache Kafka, Apache Pulsar và AWS Kinesis.
Quyết định

Sau khi đánh giá cẩn thận các yêu cầu và ràng buộc của ứng dụng, chúng tôi đã quyết định dùng cơ sở dữ liệu tài liệu.

## Cơ sở lý luận

Chúng tôi chọn cơ sở dữ liệu tài liệu vì:

1. Ứng dụng của chúng tôi cần một mô hình dữ liệu linh hoạt có thể phát triển theo thời gian. Cơ sở dữ liệu tài liệu cho phép chúng tôi lưu trữ dữ liệu ở định dạng không có lược đồ, nghĩa là chúng tôi có thể thêm trường mới hoặc thay đổi cấu trúc của các tài liệu hiện có mà không phải sửa đổi lược đồ cơ sở dữ liệu.

2. Ứng dụng của chúng tôi cần mở rộng theo chiều ngang để xử lý khối lượng dữ liệu và lưu lượng lớn. Cơ sở dữ liệu tài liệu cung cấp hỗ trợ tích hợp sẵn cho sharding và sao chép, cho phép chúng tôi phân phối dữ liệu qua nhiều máy chủ và xử lý thông lượng đọc và ghi cao.

3. Ứng dụng của chúng tôi cần truy xuất dữ liệu nhanh và hiệu quả. Cơ sở dữ liệu tài liệu cung cấp khả năng lập chỉ mục và truy vấn mạnh mẽ cho phép chúng tôi truy xuất dữ liệu nhanh chóng và hiệu quả.

4. Ứng dụng của chúng tôi không đòi hỏi các giao dịch hoặc quan hệ dữ liệu phức tạp. Trong khi cơ sở dữ liệu quan hệ xuất sắc trong việc áp dụng các ràng buộc toàn vẹn dữ liệu và xử lý các giao dịch phức tạp, ứng dụng của chúng tôi không có những yêu cầu như vậy. Cơ sở dữ liệu tài liệu có thể cung cấp các bảo đảm nhất quán và bền vững đủ cho trường hợp sử dụng của chúng tôi.

## Hệ quả

Khi chọn cơ sở dữ liệu tài liệu, chúng tôi sẽ cần đầu tư vào việc học và hiểu công nghệ cụ thể mà chúng tôi chọn dùng. Ngoài ra, chúng tôi sẽ cần bảo đảm rằng mô hình dữ liệu của ứng dụng phù hợp tốt với mô hình dữ liệu của cơ sở dữ liệu tài liệu để tối đa hóa hiệu năng và khả năng mở rộng.

Tuy nhiên, chúng tôi tin rằng lợi ích của việc dùng cơ sở dữ liệu tài liệu lớn hơn chi phí, và nó là lựa chọn phù hợp nhất với các yêu cầu và ràng buộc của ứng dụng chúng tôi.
