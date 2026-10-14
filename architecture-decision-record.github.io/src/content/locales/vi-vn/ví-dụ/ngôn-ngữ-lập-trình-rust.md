# Bản ghi quyết định kiến trúc: Ngôn ngữ lập trình Rust

Số quyết định: AR-001

Tiêu đề quyết định: Áp dụng ngôn ngữ lập trình Rust

Ngày: 1 tháng 12 năm 2021

Trạng thái: Đã chấp nhận

### Phát biểu vấn đề

Khi tiếp tục phát triển các ứng dụng phần mềm, chúng tôi nhận thấy ngày càng khó giảm thiểu các lỗ hổng bảo mật tiềm ẩn và ngăn lỗi thời gian chạy. Với các ngôn ngữ lập trình hiện có, như C và C++, chúng tôi tiếp tục gặp các vấn đề như tràn bộ đệm, rò rỉ bộ nhớ và hành vi không xác định dẫn đến sự cố ứng dụng. Chúng tôi cần một ngôn ngữ lập trình đảm bảo an toàn bộ nhớ và đủ hiệu quả để hỗ trợ các ứng dụng đòi hỏi hiệu năng.

### Cân nhắc

Một số ngôn ngữ lập trình được thiết kế để giải quyết các vấn đề hiện có. Trong số đó, ngôn ngữ lập trình Rust đã thu hút sự chú ý đáng kể từ cộng đồng nhà phát triển nhờ các đặc điểm thiết kế độc đáo của nó. Các cân nhắc bao gồm;

1. An toàn bộ nhớ và bảo mật

2. Hiệu năng và hiệu quả

3. Hỗ trợ và áp dụng của cộng đồng

4. Đường cong học tập

5. Công cụ và hệ sinh thái

6. Tương thích với các hệ thống phần mềm hiện có.

### Ràng buộc

Việc áp dụng một ngôn ngữ lập trình mới đòi hỏi đào tạo lại các nhà phát triển, tốn thời gian và nguồn lực. Việc tích hợp ngôn ngữ vào quy trình phát triển hiện có có thể là một thách thức. Chúng tôi phải bảo đảm tương thích với các hệ thống hiện có và tránh các thay đổi gây gián đoạn để duy trì tính liên tục.

### Triển khai

1. Nhóm phát triển của chúng tôi sẽ trải qua đào tạo để học và làm quen với ngôn ngữ lập trình Rust.

2. Chúng tôi sẽ tạo một dự án mới dùng Rust trên cơ sở thử nghiệm để đánh giá tính tương thích và phù hợp của nó cho mục đích phát triển của chúng tôi.

3. Chúng tôi sẽ dần dần di chuyển các hệ thống hiện có viết bằng C và C++ sang Rust.

4. Chúng tôi sẽ hợp tác với cộng đồng Rust để khám phá các công cụ và thư viện hiện có có thể nâng cao quy trình phát triển của chúng tôi.

5. Chúng tôi sẽ giám sát hiệu năng của Rust và so sánh nó với hiệu năng của các ngôn ngữ lập trình hiện có một cách thường xuyên.

6. Chúng tôi sẽ áp dụng cách tiếp cận dài hạn cân bằng chi phí đào tạo, tích hợp và các lợi ích tiềm năng của việc dùng Rust.

### Cơ sở lý luận

Chúng tôi đã áp dụng Rust nhờ các tính năng độc đáo được thiết kế để đảm bảo an toàn bộ nhớ và bảo mật đồng thời duy trì hiệu năng và hiệu quả. Hệ thống kiểu vững chắc, trình kiểm tra mượn (borrow checker) và các khái niệm an toàn bộ nhớ của Rust khiến nó rất phù hợp để phát triển các ứng dụng đòi hỏi hiệu năng và an toàn. Hơn nữa, Rust có một cộng đồng nhà phát triển đáng kể, cho phép chúng tôi tiếp cận nhiều công cụ, thư viện và hệ sinh thái hỗ trợ quy trình phát triển của mình. Mặc dù Rust đi kèm đường cong học tập, chúng tôi tin rằng lợi ích của việc áp dụng Rust lớn hơn chi phí và mang lại cơ hội tuyệt vời để tiếp tục tăng trưởng và đổi mới.

### Hệ quả

1. Việc áp dụng Rust sẽ đòi hỏi khoản đầu tư đáng kể về thời gian và nguồn lực để đào tạo các nhà phát triển và tích hợp ngôn ngữ vào quy trình phát triển hiện có.

2. Việc áp dụng Rust có thể gây ra một mức độ vấn đề tương thích nào đó với các hệ thống hiện có, đòi hỏi tái cấu trúc và sửa đổi.

3. Việc áp dụng Rust có thể làm tăng số lượng nhà phát triển có thể đóng góp cho dự án của chúng tôi bằng cách thu hút các nhà phát triển Rust muốn làm việc trong các dự án thú vị.

4. Việc áp dụng có thể dẫn đến cải thiện hiệu năng, hiệu quả và an toàn so với các ngôn ngữ hiện có.

5. Cuối cùng, việc áp dụng Rust mang lại lợi ích tiềm năng là giảm các lỗ hổng bảo mật trong các ứng dụng của chúng tôi.
   
<h6>Ghi công: trang này được tạo bởi ChatGPT, sau đó được chỉnh sửa cho rõ ràng và đúng định dạng.</h6>
