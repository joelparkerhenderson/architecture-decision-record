# Bản ghi quyết định kiến trúc: API dùng JSON so với gRPC

## Trạng thái

Đã chấp nhận

## Bối cảnh

Chúng tôi đang thiết kế một API cho một dịch vụ mới sẽ được nhiều máy khách sử dụng. Chúng tôi đã cân nhắc hai lựa chọn để triển khai API: dùng JSON qua HTTP hoặc dùng gRPC.

JSON qua HTTP là cách tiếp cận được sử dụng rộng rãi để xây dựng API và được nhiều ngôn ngữ lập trình và framework hỗ trợ. Cách tiếp cận này đơn giản, nhẹ và dễ hiểu, khiến nó trở thành lựa chọn tốt cho nhiều dự án. Tuy nhiên, nó có thể kém hiệu quả hơn các lựa chọn khác, đặc biệt khi xử lý lượng dữ liệu lớn.

gRPC, mặt khác, là một công nghệ mới hơn cung cấp cách xây dựng API hiệu quả hơn. Nó dùng tuần tự hóa nhị phân để truyền dữ liệu, có thể nhanh hơn và gọn hơn so với dùng JSON. gRPC cũng hỗ trợ streaming hai chiều, khiến nó là lựa chọn tốt cho các ứng dụng thời gian thực.

## Quyết định

Sau khi cân nhắc ưu và nhược điểm của cả hai lựa chọn, chúng tôi đã quyết định dùng gRPC cho API của mình. Mặc dù JSON qua HTTP là lựa chọn đơn giản hơn, chúng tôi tin rằng gRPC sẽ mang lại giải pháp hiệu quả và có khả năng mở rộng hơn cho dịch vụ của chúng tôi. Chúng tôi cũng dự đoán rằng API của mình sẽ xử lý lượng dữ liệu lớn, và tuần tự hóa nhị phân của gRPC sẽ hiệu quả hơn cho trường hợp sử dụng này.

Ngoài ra, chúng tôi tin rằng việc gRPC hỗ trợ streaming hai chiều sẽ có lợi cho các ứng dụng thời gian thực mà chúng tôi có thể phát triển trong tương lai.

## Hệ quả

Khi chọn gRPC, chúng tôi sẽ cần dùng một bộ công cụ và thư viện khác để xây dựng API so với dùng JSON qua HTTP. Điều này có thể đòi hỏi thêm thời gian và công sức để học và triển khai các công nghệ này. Ngoài ra, các máy khách muốn dùng API của chúng tôi sẽ cần dùng các thư viện tương thích gRPC, có thể không được hỗ trợ rộng rãi như các thư viện JSON qua HTTP.

Tuy nhiên, chúng tôi tin rằng lợi ích của việc dùng gRPC lớn hơn những nhược điểm tiềm ẩn này, và chúng tôi tự tin rằng quyết định này sẽ tạo ra một API hiệu quả và có khả năng mở rộng hơn.
