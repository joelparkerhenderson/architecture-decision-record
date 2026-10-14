# Bản ghi quyết định kiến trúc: Trình soạn thảo mã lập trình

## Bối cảnh

Trình soạn thảo mã lập trình là công cụ thiết yếu để các nhà phát triển viết và chỉnh sửa mã. Có rất nhiều trình soạn thảo mã, mỗi trình có bộ tính năng, ưu điểm và nhược điểm riêng. Mục đích của ADR này là ghi lại các quyết định kiến trúc được đưa ra cho các trình soạn thảo mã lập trình.

## Các ưu tiên

Kiến trúc cho các trình soạn thảo mã lập trình nên ưu tiên những điều sau:

* **Tính mô-đun**: Trình soạn thảo mã nên được thiết kế theo cách mô-đun, cho phép các nhà phát triển tùy chỉnh và mở rộng nó khi cần. Điều này cho phép một kiến trúc linh hoạt có thể thích ứng với nhu cầu của các nhà phát triển và nhóm khác nhau.

* **Hiệu năng**: Trình soạn thảo mã nên có hiệu năng tốt và phản hồi nhanh, cho phép các nhà phát triển làm việc hiệu quả mà không bị công cụ họ đang dùng làm chậm lại.

* **Giao diện người dùng**: Giao diện người dùng nên trực quan và dễ dùng, cho phép các nhà phát triển tập trung vào mã của mình thay vì vật lộn với trình soạn thảo.

* **Khả năng mở rộng**: Trình soạn thảo mã nên được thiết kế để dễ dàng mở rộng bằng các plugin và tích hợp của bên thứ ba.

* **Tính tương thích**: Trình soạn thảo mã nên tương thích với nhiều loại ngôn ngữ lập trình và công nghệ, khiến nó là công cụ hữu ích cho nhiều nhà phát triển.

## Quyết định

Dựa trên các ưu tiên này, kiến trúc cho các trình soạn thảo mã lập trình nên được thiết kế với các thành phần sau:

* **Lõi**: Thành phần này cung cấp chức năng cơ bản của trình soạn thảo mã, như tô sáng cú pháp, chỉnh sửa văn bản và quản lý tệp.

* **UI**: Thành phần này cung cấp giao diện người dùng cho trình soạn thảo mã, bao gồm menu, thanh công cụ và phím tắt.

* **Plugin**: Thành phần này cho phép các nhà phát triển mở rộng chức năng của trình soạn thảo mã bằng cách cài đặt các plugin của bên thứ ba. Plugin có thể cung cấp các tính năng bổ sung, như hoàn thành mã, linting hoặc gỡ lỗi.

* **Tích hợp**: Thành phần này cho phép trình soạn thảo mã tích hợp với các công cụ và công nghệ khác, như hệ thống kiểm soát phiên bản, hệ thống build hoặc công cụ gỡ lỗi.

## Cơ sở lý luận

Tính mô-đun của trình soạn thảo mã cho phép các nhà phát triển tùy chỉnh và mở rộng nó khi cần. Điều này quan trọng vì các nhà phát triển và nhóm khác nhau có nhu cầu và quy trình làm việc khác nhau, và một kiến trúc linh hoạt có thể đáp ứng những khác biệt này.

* **Hiệu năng**: cốt yếu vì các nhà phát triển cần làm việc hiệu quả mà không bị công cụ làm chậm lại. Một trình soạn thảo mã có hiệu năng tốt là thiết yếu cho năng suất và có thể giúp các nhà phát triển duy trì sự tập trung và chú ý.

* **UI**: quan trọng vì nó cho phép các nhà phát triển tập trung vào mã của mình thay vì vật lộn với trình soạn thảo. Điều này có thể dẫn đến năng suất tốt hơn và ít khó chịu hơn cho các nhà phát triển.

* **Khả năng mở rộng**: mạnh mẽ vì nó cho phép trình soạn thảo mã được điều chỉnh theo các nhu cầu và quy trình làm việc khác nhau. Các plugin và tích hợp của bên thứ ba có thể cung cấp các tính năng và khả năng bổ sung không có trong trình soạn thảo lõi.

* **Tính tương thích**: có giá trị vì nó cho phép trình soạn thảo mã được dùng với nhiều loại ngôn ngữ lập trình và công nghệ. Điều này khiến trình soạn thảo trở thành công cụ hữu ích hơn cho nhiều nhà phát triển.

Các thành phần lõi, plugin, tích hợp và UI cung cấp sự tách biệt rõ ràng các mối quan tâm và cho phép một kiến trúc mô-đun có thể dễ dàng mở rộng và tùy chỉnh. Kiến trúc này linh hoạt, có hiệu năng tốt và tương thích với nhiều loại ngôn ngữ lập trình và công nghệ, khiến nó là một công cụ hữu ích cho các nhà phát triển.
