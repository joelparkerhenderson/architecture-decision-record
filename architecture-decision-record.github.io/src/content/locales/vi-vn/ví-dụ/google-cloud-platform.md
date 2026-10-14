# Bản ghi quyết định kiến trúc cho Google Cloud Platform

## Bối cảnh

Google Cloud Platform (GCP) là một nền tảng điện toán đám mây nổi bật cung cấp nhiều dịch vụ đám mây, bao gồm các giải pháp tính toán, lưu trữ và mạng. ADR này nhằm ghi lại các quyết định kiến trúc được đưa ra để phát triển và triển khai một hạ tầng dựa trên GCP cho tổ chức của chúng tôi.

## Quyết định

Tổ chức của chúng tôi đã quyết định dùng Google Cloud Platform làm hạ tầng đám mây cho ứng dụng của mình. Các cân nhắc chính cho quyết định này là:

   - Hiệu quả chi phí

   - Khả năng mở rộng

   - Độ tin cậy

   - Tính linh hoạt

## Lựa chọn

Các dịch vụ sau của GCP đã được chọn để đáp ứng yêu cầu của chúng tôi:

   - Compute Engine cho máy ảo và tài nguyên tính toán

   - Cloud Storage cho lưu trữ đối tượng và lưu trữ tệp

   - Cloud SQL cho dịch vụ cơ sở dữ liệu được quản lý

   - Firebase cho phát triển và lưu trữ ứng dụng

## Cơ sở lý luận

   - Hiệu quả chi phí: Google Cloud Platform có hiệu quả chi phí cao so với các nền tảng đám mây khác, khiến nó là lựa chọn hấp dẫn cho các tổ chức có ngân sách hạn chế.

   - Khả năng mở rộng: Hạ tầng dễ mở rộng của GCP cho phép xử lý bất kỳ lượng lưu lượng nào theo thời gian thực.

   - Độ tin cậy: Các dịch vụ được quản lý của GCP mang lại độ tin cậy cao, với sao lưu tự động và khả năng khôi phục sau thảm họa đảm bảo tính sẵn sàng cao của tài nguyên và dữ liệu.

   - Tính linh hoạt: Nền tảng cung cấp nhiều công cụ và dịch vụ trên các lĩnh vực khác nhau như AI, phân tích dữ liệu và IoT, khiến nó có tính đa dụng cao.

## Hệ quả

Việc di chuyển sang Google Cloud Platform sẽ đòi hỏi đào tạo các nhóm của chúng tôi về các dịch vụ GCP, thiết kế lại ứng dụng để tương thích với các dịch vụ đã chọn, và cập nhật mã hạ tầng để hỗ trợ các dịch vụ GCP. Tuy nhiên, dự kiến sau khi hoàn tất di chuyển, chúng tôi sẽ có một hạ tầng có khả năng mở rộng cao, đáng tin cậy và hiệu quả chi phí để lưu trữ ứng dụng của mình. Ngoài ra, chúng tôi sẽ cần quản lý các chi phí liên tục của việc cấp phát tài nguyên trên GCP.

## Kết luận

Google Cloud Platform là một lựa chọn tuyệt vời cho hạ tầng đám mây của chúng tôi nhờ hiệu quả chi phí, khả năng mở rộng, độ tin cậy và tính linh hoạt. Bằng cách sử dụng các dịch vụ đã chọn, chúng tôi có thể cung cấp một hạ tầng sẵn sàng cao và vững chắc cho ứng dụng của mình.
