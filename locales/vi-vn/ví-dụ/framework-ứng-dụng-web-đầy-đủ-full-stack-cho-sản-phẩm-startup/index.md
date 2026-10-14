# Bản ghi quyết định kiến trúc: framework ứng dụng web, đầy đủ (batteries included), full stack, cho sản phẩm startup

<!-- 

ChatGPT prompt

Long software architecture decision record 
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports. 

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Mục tiêu chính:**  
Xây dựng một ứng dụng web cho khách hàng trả phí đăng nhập, tải tệp lên, xử lý dữ liệu và xem báo cáo, tập trung vào phát triển agile, chức năng full-stack và khả năng tương thích mạnh với các công cụ AI/ML, đặc biệt là notebook Project Jupyter.

### Bối cảnh và Yêu cầu:

1. **Phát triển Agile (Ưu tiên cao)**: Là một startup, chúng tôi cần lặp nhanh và linh hoạt. Các thực hành agile, như tạo mẫu nhanh, phát triển lặp và khả năng thích ứng với thay đổi, là chìa khóa của chu kỳ phát triển của chúng tôi.

2. **Framework Full-Stack (Ưu tiên cao)**: Chúng tôi hướng tới giảm thiểu chi phí phụ bằng cách chọn một framework có thể xử lý hiệu quả cả backend lẫn frontend, giảm nhu cầu về các framework front-end riêng.

3. **Tương thích với các công cụ AI/ML (Ưu tiên cao)**: Khả năng tích hợp dễ dàng với các công cụ phân tích dữ liệu như notebook Jupyter và hệ sinh thái khoa học dữ liệu của Python (NumPy, Pandas, TensorFlow, v.v.) là thiết yếu. Điều này sẽ tạo thuận lợi cho việc xử lý dữ liệu và báo cáo hiệu quả.

4. **Tiêu chí ưu tiên thấp**:
   - **Tốc độ thời gian chạy**: Mặc dù hiệu năng có liên quan, nó không phải yếu tố quan trọng nhất lúc đầu vì chúng tôi quan tâm hơn đến tốc độ phát triển và độ hoàn thiện tính năng.
   - **Khả năng mở rộng**: Chúng tôi dự đoán sự tăng trưởng, nhưng các mối quan ngại về khả năng mở rộng có thể được giải quyết sau, và đây không phải yêu cầu chính lúc này.
   - **Tương thích ngược**: Chúng tôi tập trung vào các công nghệ hiện tại và không quá quan tâm đến tương thích ngược với các hệ thống kế thừa.

### Các framework được đánh giá:

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Tổng quan**:  
Django là một framework web cấp cao cho Python thúc đẩy phát triển nhanh và thiết kế sạch, thực dụng. Nó được biết đến với triết lý “batteries included” (đầy đủ), nghĩa là nó bao gồm nhiều tính năng như xác thực, định tuyến, ORM và xử lý biểu mẫu ngay từ đầu.

**Điểm mạnh**:  
- **Full-Stack**: Django là một framework full-stack toàn diện có thể xử lý cả nhu cầu backend và frontend với các tính năng tích hợp (ví dụ công cụ tạo mẫu, giao diện quản trị).
- **Phát triển Agile**: Cấu trúc và quy ước được xác định rõ của Django cho phép phát triển nhanh và khả năng thích ứng, rất quan trọng trong môi trường startup. Framework đi kèm tài liệu xuất sắc và một hệ sinh thái phong phú các gói của bên thứ ba, giúp đẩy nhanh phát triển.
- **Tích hợp AI/ML**: Hệ sinh thái của Python là vô song khi nói đến khoa học dữ liệu và học máy. Django, dựa trên Python, tích hợp liền mạch với các công cụ như notebook Jupyter, Pandas, NumPy, TensorFlow và scikit-learn.
- **Cộng đồng và hệ sinh thái**: Django có một cộng đồng rộng lớn, tài liệu vững chắc và nhiều loại plugin và tiện ích mở rộng, giúp tăng tốc đáng kể phát triển và khắc phục sự cố.
  
**Điểm yếu**:  
- **Tốc độ thời gian chạy**: Python có xu hướng chậm hơn so với các ngôn ngữ như Rust hoặc Elixir. Tuy nhiên, với trường hợp sử dụng này, nơi hiệu năng không phải mối quan tâm chính, điều này có thể không phải là điểm quyết định.
- **Khả năng mở rộng**: Mặc dù Django có khả năng mở rộng cao, có thể có thách thức ở quy mô rất cao nếu không tối ưu cẩn thận (ví dụ khi xử lý các yêu cầu đồng thời nặng). Tuy nhiên, Django vẫn có thể được mở rộng hiệu quả bằng các kỹ thuật cân bằng tải và bộ nhớ đệm.

**Nhận định**:  
Django phù hợp tốt với các yêu cầu về phát triển agile, hỗ trợ full-stack và tương thích AI/ML. Sự tích hợp Python của nó cho phép truy cập liền mạch các công cụ và thư viện khoa học dữ liệu cần thiết cho ứng dụng.

---

### 2. **Ruby on Rails (Ruby)**

**Tổng quan**:  
Ruby on Rails (RoR) là một framework ứng dụng web full-stack trưởng thành, được biết đến với cách tiếp cận quy ước hơn cấu hình, giúp phát triển nhanh.

**Điểm mạnh**:  
- **Full-Stack**: RoR đi kèm các công cụ tích hợp cho cả phát triển backend và frontend (ví dụ view, mẫu, scaffolding), và thư viện gem phong phú của nó cho phép triển khai nhanh các tính năng khác nhau.
- **Phát triển Agile**: Ruby on Rails đặc biệt được biết đến với các chu kỳ lặp nhanh, có lợi cho các startup muốn lặp nhanh các tính năng. RoR hỗ trợ phát triển hướng kiểm thử (TDD) và có hệ sinh thái đã thành lập cho các quy trình agile.
- **Cộng đồng và hệ sinh thái**: RoR có cộng đồng mạnh, đã thành lập tốt và một loạt gem có thể tăng tốc phát triển.
- **Dễ dùng**: Rails có cú pháp rất thân thiện với nhà phát triển và được biết đến với việc làm cho các tác vụ như di chuyển cơ sở dữ liệu, kiến trúc model-view-controller (MVC) và xử lý route nhanh và đơn giản.

**Điểm yếu**:  
- **Hiệu năng**: Ruby có xu hướng có hiệu năng thời gian chạy chậm hơn so với Python hoặc Elixir. Mặc dù RoR có thể mở rộng với hạ tầng phù hợp, hiệu năng của Ruby có thể trở thành điểm nghẽn đối với các ứng dụng đòi hỏi xử lý thời gian thực nặng hoặc lưu lượng đồng thời cao.
- **Tích hợp AI/ML**: Mặc dù Ruby có một số thư viện học máy, nó không được áp dụng rộng rãi trong cộng đồng AI/ML như Python. Tích hợp với các công cụ như notebook Jupyter không liền mạch bằng, khiến Python là lựa chọn mạnh hơn cho các ứng dụng nặng về dữ liệu.
  
**Nhận định**:  
Mặc dù Ruby on Rails xuất sắc trong phát triển agile và tạo mẫu nhanh, nó thua kém về khả năng tương thích AI/ML so với Python (Django). Đây là một lựa chọn khả thi cho các startup ưu tiên lặp nhanh hơn tích hợp phân tích dữ liệu sâu.

---

### 3. **Phoenix (Elixir)**

**Tổng quan**:  
Phoenix là một framework web được xây dựng bằng Elixir, một ngôn ngữ lập trình hàm được thiết kế cho khả năng mở rộng và đồng thời. Phoenix tận dụng Erlang VM, vốn được biết đến với việc xử lý đồng thời khổng lồ và các hệ thống chịu lỗi.

**Điểm mạnh**:  
- **Khả năng mở rộng và hiệu năng**: Phoenix tỏa sáng ở khả năng mở rộng và xử lý đồng thời cao. Nó được xây dựng trên Erlang VM, có thể hỗ trợ hàng nghìn (hoặc thậm chí hàng triệu) kết nối đồng thời, khiến nó là ứng viên mạnh cho các ứng dụng đòi hỏi xử lý dữ liệu thời gian thực hoặc lưu lượng khối lượng lớn.
- **Full-Stack**: Phoenix bao gồm mọi thứ cần thiết để xây dựng cả backend lẫn frontend của một ứng dụng. Nó hỗ trợ live view cho các cập nhật UI tương tác và bao gồm một công cụ tạo mẫu.
- **Phát triển Agile**: Phoenix rất mô-đun, cho phép lặp nhanh các tính năng. Nó rất phù hợp với các startup cần di chuyển nhanh.
- **Tương thích AI/ML**: Mặc dù Elixir có các thư viện học máy mới nổi, nó không được hỗ trợ rộng rãi cho các tác vụ AI/ML như Python. Tích hợp với các công cụ như notebook Jupyter sẽ đòi hỏi các giải pháp tạm, vì hệ sinh thái của Elixir cho khoa học dữ liệu chưa trưởng thành như của Python.

**Điểm yếu**:  
- **Hệ sinh thái AI/ML**: Elixir không phải ngôn ngữ chính dùng trong khoa học dữ liệu hay học máy, và hệ sinh thái không trưởng thành bằng Python. Do đó, tích hợp với các công cụ như notebook Jupyter hoặc các thư viện AI phổ biến (TensorFlow, PyTorch) sẽ rườm rà.
- **Đường cong học tập**: Nếu nhóm không quen với lập trình hàm và Elixir, có thể có đường cong học tập dốc hơn.

**Nhận định**:  
Phoenix là một lựa chọn xuất sắc nếu khả năng mở rộng và xử lý đồng thời là mối quan tâm chính. Tuy nhiên, với ưu tiên về khả năng tương thích AI/ML, Phoenix có thể không phải là lựa chọn phù hợp nhất do hệ sinh thái hạn chế của Elixir trong lĩnh vực này.

---

### 4. **Loco (Rust)**

**Tổng quan**:  
Loco là một framework web được xây dựng bằng Rust, một ngôn ngữ lập trình hệ thống được biết đến với hiệu năng, an toàn bộ nhớ và xử lý đồng thời. Rust ngày càng phổ biến để xây dựng các ứng dụng hiệu năng cao.

**Điểm mạnh**:  
- **Hiệu năng**: Điểm mạnh chính của Rust nằm ở hiệu năng cao và an toàn bộ nhớ, khiến nó là lựa chọn xuất sắc cho các ứng dụng đòi hỏi kiểm soát cấp thấp hoặc hiệu năng cực cao.
- **Xử lý đồng thời**: Hệ thống sở hữu (ownership) của Rust đảm bảo an toàn bộ nhớ đồng thời cho phép lập trình đồng thời an toàn, khiến nó lý tưởng cho các hệ thống cần mở rộng hiệu quả và xử lý song song.

**Điểm yếu**:  
- **Phát triển Full-Stack**: Loco, mặc dù đầy hứa hẹn, không trưởng thành bằng các framework khác về việc cung cấp một giải pháp full-stack hoàn chỉnh. Nó phù hợp hơn cho phát triển backend, và hệ sinh thái front-end quanh Rust vẫn đang nổi lên.
- **Phát triển Agile**: Phát triển bằng Rust có thể chậm hơn so với các ngôn ngữ cấp cao hơn như Python hoặc Ruby do bản chất cấp thấp hơn và đường cong học tập dốc hơn.
- **Hệ sinh thái AI/ML**: Rust không có hệ sinh thái rộng rãi như Python cho AI/ML. Mặc dù có các thư viện đang phát triển trong Rust cho tính toán số, chúng kém trưởng thành hơn nhiều so với những gì Python cung cấp, như notebook Jupyter hoặc các framework học máy.
  
**Nhận định**:  
Mặc dù Rust và framework Loco của nó mang lại hiệu năng đặc biệt, việc thiếu hỗ trợ full-stack, lợi ích phát triển agile và hệ sinh thái AI/ML khiến nó kém lý tưởng cho trường hợp sử dụng cụ thể này. Nó phù hợp hơn cho các ứng dụng đòi hỏi hiệu năng hơn là phát triển web nhanh với các công cụ khoa học dữ liệu tích hợp.

---

### Kết luận

Sau khi đánh giá các lựa chọn dựa trên yêu cầu của dự án, **Django (Python)** là lựa chọn phù hợp nhất. Nó mang lại các ưu điểm sau:

- **Khả năng Full-Stack**: Django là một framework full-stack tích hợp phát triển backend và frontend.
- **Phát triển Agile**: Framework rất phù hợp cho tạo mẫu và lặp nhanh, điều thiết yếu trong môi trường startup.
- **Tương thích AI/ML**: Python là ngôn ngữ hàng đầu trong AI/ML, và khả năng tương thích của Django với các thư viện như notebook Jupyter đảm bảo tích hợp suôn sẻ cho phân tích và xử lý dữ liệu.
- **Cộng đồng và hệ sinh thái**: Sự hỗ trợ mạnh của cộng đồng Django và hệ sinh thái thư viện rộng lớn cung cấp vô số công cụ để tăng tốc phát triển.

Mặc dù **Ruby on Rails** cũng là một ứng viên mạnh cho phát triển agile, hỗ trợ AI/ML hạn chế khiến nó kém lý tưởng cho trường hợp sử dụng cụ thể này. **Phoenix (Elixir)** và **Loco (Rust)**, mặc dù xuất sắc về khả năng mở rộng và hiệu năng, lại thua kém về tích hợp AI/ML và phát triển full-stack. Do đó, Django là framework được khuyến nghị cho dự án này.
