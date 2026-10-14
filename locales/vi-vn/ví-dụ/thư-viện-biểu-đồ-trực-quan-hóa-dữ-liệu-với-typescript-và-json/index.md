# Bản ghi quyết định kiến trúc: bộ công cụ thư viện biểu đồ để trực quan hóa dữ liệu dùng TypeScript và JSON

<!--

ChatGPT prompt:

Long software architecture decision record 
chart library toolkit for data visualization using TypeScript and JSON

Evaluate Charts: Apache ECharts, Chart.js, ApexCharts, AG Charts, Highcharts, Carbon Charts, Layer Cake, D3.

Primary need: advanced interactive charts, especially for financial data, scientific data, and government data.

High importance: 1. Agile development because this is for a startup. 2. Doughnut Chart, Radar Chart, Clustering Process
Chart, Area Chart with Time Axis, Candlestick Chart, Nightingale Chart, Geo SVG Map. 3. Free open source.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Mục tiêu chính:**  
Chọn một bộ công cụ biểu đồ nâng cao để tạo các trực quan hóa tương tác, tập trung vào dữ liệu tài chính, dữ liệu khoa học và dữ liệu chính phủ, dùng TypeScript và JSON. Thư viện nên cung cấp các tính năng vững chắc, tính linh hoạt và là mã nguồn mở. 

### Bối cảnh và Yêu cầu:

1. **Phát triển Agile (Ưu tiên cao)**: Là một startup, việc lặp nhanh, tạo mẫu và linh hoạt trong phát triển là thiết yếu. Thư viện biểu đồ phải cho phép các chu kỳ phát triển nhanh.
   
2. **Các loại biểu đồ (Ưu tiên cao)**:
   - **Biểu đồ Vành khuyên (Doughnut Chart)**
   - **Biểu đồ Radar (Radar Chart)**
   - **Biểu đồ Quy trình Phân cụm (Clustering Process Chart)**
   - **Biểu đồ Vùng với Trục thời gian (Area Chart with Time Axis)**
   - **Biểu đồ Nến (Candlestick Chart)**
   - **Biểu đồ Nightingale (Nightingale Chart)**
   - **Bản đồ SVG Địa lý (Geo SVG Map)**
   
   Các loại biểu đồ này đặc biệt quan trọng để trực quan hóa các tập dữ liệu phức tạp, như xu hướng tài chính, số liệu khoa học và thông tin địa lý.

3. **Miễn phí và Mã nguồn mở (Ưu tiên cao)**: Bộ công cụ nên là mã nguồn mở để tránh chi phí cấp phép, mang lại sự minh bạch và tính linh hoạt để tùy chỉnh.

4. **Tiêu chí ưu tiên thấp**:
   - **Tốc độ thời gian chạy**: Mặc dù hiệu năng quan trọng, nó không phải ưu tiên hàng đầu cho quyết định này.
   - **Khả năng mở rộng**: Mặc dù khả năng mở rộng nhìn chung quan trọng, nhu cầu trước mắt là xây dựng một MVP có thể phát triển theo thời gian. Các mối quan ngại về khả năng mở rộng có thể giải quyết sau.
   - **Tương thích ngược**: Không phải mối quan tâm chính cho bản dựng ban đầu, miễn là thư viện hiện đại và được bảo trì tích cực.

### Các thư viện được đánh giá:

1. **Apache ECharts**
2. **Chart.js**
3. **ApexCharts**
4. **AG Charts**
5. **Highcharts**
6. **Carbon Charts**
7. **Layer Cake**
8. **D3.js**

---

### 1. **Apache ECharts**

**Tổng quan**:  
Apache ECharts là một thư viện biểu đồ mạnh mẽ, linh hoạt cho các trực quan hóa tương tác, có thể tùy chỉnh. Nó hỗ trợ nhiều loại biểu đồ và đặc biệt mạnh ở các trực quan hóa phức tạp, động.

**Điểm mạnh**:
- **Tương tác nâng cao**: ECharts xuất sắc trong việc cung cấp các biểu đồ tương tác, với các tính năng như thu phóng, kéo, và cập nhật dữ liệu động.
- **Vành khuyên, Radar, Nến, Bản đồ SVG địa lý**: ECharts hỗ trợ nhiều loại biểu đồ cần thiết, bao gồm trực quan hóa vành khuyên, radar, nến và bản đồ địa lý.
- **Miễn phí và Mã nguồn mở**: ECharts là một thư viện mã nguồn mở, phù hợp với bản chất tiết kiệm ngân sách của một startup và mang lại tự do sửa đổi mã.
- **Linh hoạt và Khả năng mở rộng**: Có thể tùy chỉnh cao, với hỗ trợ rộng rãi cho hoạt ảnh, trực quan hóa tùy chỉnh và các kỹ thuật biểu đồ nâng cao.
  
**Điểm yếu**:
- **Đường cong học tập**: ECharts, dù mạnh mẽ, có thể có đường cong học tập dốc hơn do tính linh hoạt và API rộng của nó.
- **Độ phức tạp của tài liệu**: Tài liệu toàn diện nhưng có thể gây choáng ngợp cho các nhà phát triển mới bắt đầu.

**Nhận định**:  
ECharts rất phù hợp với dự án nhờ hỗ trợ các biểu đồ tương tác, bao gồm tất cả các loại cần thiết như biểu đồ nến, biểu đồ radar và bản đồ địa lý. Bản chất mã nguồn mở của nó phù hợp với nhu cầu của dự án về tính linh hoạt và hiệu quả chi phí.

---

### 2. **Chart.js**

**Tổng quan**:  
Chart.js là một thư viện biểu đồ đơn giản, dễ dùng để xây dựng các loại biểu đồ phổ biến. Nó được biết đến với sự đơn giản và dễ tích hợp.

**Điểm mạnh**:
- **Dễ dùng**: Chart.js rất đơn giản để thiết lập và sử dụng, với đường cong học tập tối thiểu.
- **Mã nguồn mở**: Chart.js miễn phí và mã nguồn mở, điều quan trọng để giảm chi phí.
- **Các loại biểu đồ phổ biến**: Nó hỗ trợ các biểu đồ cơ bản như vành khuyên, vùng, radar và đường, bao quát hầu hết các nhu cầu chính.

**Điểm yếu**:
- **Biểu đồ nâng cao hạn chế**: Chart.js không hỗ trợ gốc các loại biểu đồ phức tạp như biểu đồ nến, bản đồ SVG địa lý hoặc biểu đồ quy trình phân cụm. Mặc dù các tính năng này có thể được thêm qua plugin hoặc tùy chỉnh, nó không đơn giản như với các thư viện khác.
- **Tương tác**: Mặc dù Chart.js hỗ trợ tương tác cơ bản (ví dụ chú giải công cụ và hiệu ứng di chuột), nó không cung cấp các tính năng nâng cao như ECharts hoặc D3.js.

**Nhận định**:  
Chart.js tuyệt vời cho các dự án đơn giản, nhanh, nhưng việc thiếu hỗ trợ các loại biểu đồ phức tạp khiến nó không phù hợp với một ứng dụng nặng dữ liệu có nhu cầu nâng cao như biểu đồ nến và bản đồ địa lý. Đây là lựa chọn tốt để tạo mẫu, nhưng với các loại biểu đồ cần thiết, các công cụ nâng cao hơn được khuyến nghị.

---

### 3. **ApexCharts**

**Tổng quan**:  
ApexCharts là một thư viện biểu đồ hiện đại cung cấp nhiều loại biểu đồ và tập trung vào các trực quan hóa tương tác với API dễ dùng.

**Điểm mạnh**:
- **Tính năng tương tác**: ApexCharts cung cấp các biểu đồ tương tác với chú giải công cụ, thu phóng, kéo và cập nhật.
- **Hỗ trợ biểu đồ tài chính và khoa học**: Nó hỗ trợ nhiều loại biểu đồ, bao gồm biểu đồ nến, biểu đồ radar và biểu đồ vùng.
- **Dễ dùng**: Nó có một API đơn giản và dễ tích hợp vào dự án.
- **Miễn phí và Mã nguồn mở**: ApexCharts cung cấp một phiên bản mã nguồn mở miễn phí phù hợp với nhiều trường hợp sử dụng.
  
**Điểm yếu**:
- **Tùy chỉnh phức tạp**: Mặc dù cung cấp nhiều tính năng, các tùy chọn tùy chỉnh không linh hoạt bằng ECharts hoặc D3.js cho các nhu cầu biểu đồ rất phức tạp hoặc tùy biến.
- **Bản đồ địa lý**: ApexCharts không hỗ trợ gốc bản đồ địa lý hoặc biểu đồ quy trình phân cụm, vốn cần cho dự án này.

**Nhận định**:  
ApexCharts là ứng viên mạnh nhờ sự dễ dùng và tương tác, nhưng thiếu ở một số loại biểu đồ nâng cao nhất định, đặc biệt là nhu cầu về bản đồ địa lý và biểu đồ phân cụm. Đây là lựa chọn tốt cho các biểu đồ đơn giản hơn nhưng thiếu một số tính năng cần thiết.

---

### 4. **AG Charts**

**Tổng quan**:  
AG Charts là một thư viện biểu đồ cấp thương mại được thiết kế cho hiệu năng và độ chính xác. Nó rất phù hợp để tạo các bảng điều khiển tài chính, khoa học và kinh doanh.

**Điểm mạnh**:
- **Các loại biểu đồ nâng cao**: AG Charts hỗ trợ nhiều loại biểu đồ nâng cao, bao gồm biểu đồ nến, biểu đồ vùng, biểu đồ radar và hơn nữa. Nó cũng cung cấp tích hợp sâu với các sản phẩm AG-Grid khác.
- **Hiệu năng cao**: Nó mang lại hiệu năng xuất sắc, đặc biệt khi xử lý các tập dữ liệu lớn.
- **Tương tác**: AG Charts hỗ trợ nhiều tính năng tương tác như thu phóng, chú giải công cụ và cập nhật động.

**Điểm yếu**:
- **Không hoàn toàn miễn phí**: Mặc dù AG Charts cung cấp phiên bản miễn phí, phiên bản đầy đủ tính năng có phí, có thể là rào cản với các startup muốn giảm thiểu chi phí.
- **Độ phức tạp**: Mặc dù thư viện giàu tính năng, nó có thể là quá mức cần thiết cho các dự án đơn giản hơn và có thể đòi hỏi nhiều thiết lập và cấu hình hơn so với các lựa chọn khác.

**Nhận định**:  
AG Charts mạnh mẽ và giàu tính năng nhưng có thể không phải là lựa chọn phù hợp nhất do tính chất thương mại và cấu trúc chi phí của nó. Mức độ phù hợp phụ thuộc vào việc ngân sách có thể đáp ứng các phiên bản trả phí hay các lựa chọn mã nguồn mở được ưu tiên.

---

### 5. **Highcharts**

**Tổng quan**:  
Highcharts là một thư viện biểu đồ phổ biến được biết đến với nhiều loại biểu đồ và các tùy chọn tùy chỉnh mạnh mẽ.

**Điểm mạnh**:
- **Các loại biểu đồ toàn diện**: Highcharts hỗ trợ nhiều loại biểu đồ, bao gồm nến, radar, vùng và bản đồ địa lý.
- **Tương tác và động**: Highcharts cung cấp các tính năng tương tác phong phú, bao gồm khoan sâu (drill-down), thu phóng và kéo.
- **Dễ dùng**: Nó có API thân thiện với người dùng và tài liệu tốt, giúp dễ bắt đầu.

**Điểm yếu**:
- **Giấy phép thương mại**: Mặc dù Highcharts cung cấp phiên bản miễn phí cho mục đích phi thương mại, giấy phép thương mại đắt, có thể là bất lợi đáng kể với các startup.
- **Đường cong học tập**: Mặc dù không dốc bằng ECharts, đường cong học tập của Highcharts vẫn có thể thách thức với người mới.

**Nhận định**:  
Highcharts là một thư viện giàu tính năng, nhưng giấy phép thương mại của nó khiến nó kém phù hợp với các dự án mã nguồn mở, nhạy cảm về chi phí. Các tùy chọn biểu đồ toàn diện của nó là một điểm cộng, nhưng vấn đề cấp phép hạn chế sức hấp dẫn của nó với trường hợp sử dụng này.

---

### 6. **Carbon Charts**

**Tổng quan**:  
Carbon Charts là một thư viện biểu đồ do IBM phát triển, được thiết kế để tạo các biểu đồ hấp dẫn về mặt thị giác và có thể tùy chỉnh cao.

**Điểm mạnh**:
- **Khả năng tùy chỉnh**: Carbon Charts cho phép tùy chỉnh rộng rãi giao diện và hành vi của biểu đồ.
- **Mã nguồn mở**: Nó miễn phí và mã nguồn mở, phù hợp với yêu cầu của dự án về các giải pháp thân thiện với ngân sách.
- **Hỗ trợ các biểu đồ phổ biến**: Nó hỗ trợ các loại biểu đồ phổ biến như vành khuyên, radar và vùng, mặc dù thiếu hỗ trợ các loại nâng cao hơn như bản đồ địa lý hoặc biểu đồ nến.

**Điểm yếu**:
- **Các loại biểu đồ nâng cao hạn chế**: Nó không hỗ trợ bản đồ địa lý, biểu đồ quy trình phân cụm hoặc biểu đồ nến, vốn thiết yếu cho dự án.
- **Hệ sinh thái nhỏ hơn**: Carbon Charts có cộng đồng và hệ sinh thái nhỏ hơn so với các thư viện biểu đồ lớn hơn như ECharts hoặc Highcharts.

**Nhận định**:  
Carbon Charts là mã nguồn mở và có thể tùy chỉnh nhưng thiếu hỗ trợ cho các loại biểu đồ phức tạp hơn mà dự án này cần. Nó phù hợp hơn cho các nhu cầu biểu đồ đơn giản hơn.

---

### 7. **Layer Cake**

**Tổng quan**:  
Layer Cake là một thư viện trực quan hóa dữ liệu được thiết kế để tạo các trực quan hóa nhiều lớp, linh hoạt.

**Điểm mạnh**:
- **Các lớp có thể tùy chỉnh**: Nó cung cấp các tùy chọn phân lớp mạnh mẽ cho các trực quan hóa phức tạp.
- **Mã nguồn mở**: Nó miễn phí và mã nguồn mở, khiến nó là lựa chọn khả thi cho các dự án có ý thức về ngân sách.

**Điểm yếu**:
- **Tài liệu hạn chế**: Layer Cake thiếu tài liệu rộng rãi và hỗ trợ cộng đồng, khiến việc làm việc với nó khó hơn so với các thư viện đã thành lập hơn.
- **Không được xây dựng cho biểu đồ**: Layer Cake phù hợp hơn cho các trực quan hóa không phải biểu đồ, nên các tùy chọn biểu đồ có sẵn của nó bị hạn chế.

**Nhận định**:  
Mặc dù thú vị cho các trực quan hóa độc đáo, Layer Cake không lý tưởng cho các yêu cầu biểu đồ truyền thống như biểu đồ nến hoặc biểu đồ radar. Nó phù hợp hơn cho các trực quan hóa tùy chỉnh ngoài phạm vi các biểu đồ chuẩn.

---

### 8. **D3.js**

**Tổng quan**:  
D3.js là một thư viện JavaScript mạnh mẽ để tạo các trực quan hóa dựa trên dữ liệu thông qua HTML, SVG và CSS.

**Điểm mạnh**:
- **Tính linh hoạt vô song**: D3.js cho phép tạo hầu như mọi loại trực quan hóa tùy chỉnh, khiến nó rất mạnh cho các biểu đồ nâng cao và tương tác.
- **Tính năng rộng rãi**: Nó hỗ trợ tất cả các loại biểu đồ cần thiết, bao gồm bản đồ địa lý, biểu đồ phân cụm và hơn nữa.
- **Có thể tùy chỉnh**: Mức độ tùy chỉnh trong D3.js là vô song, cho phép các nhà phát triển xây dựng các trực quan hóa được điều chỉnh cao.

**Điểm yếu**:
- **Đường cong học tập dốc**: D3.js có đường cong học tập dốc và phức tạp hơn để tích hợp so với các thư viện khác.
- **Tốn thời gian**: Xây dựng biểu đồ trong D3.js có thể tốn thời gian, đặc biệt với các biểu đồ phổ biến như biểu đồ nến hoặc vành khuyên.

**Nhận định**:  
D3.js cực kỳ mạnh mẽ cho các biểu đồ nâng cao, tùy chỉnh nhưng là quá mức với nhiều trường hợp sử dụng điển hình do đường cong học tập dốc và thời gian phát triển. Nó tốt nhất cho các tình huống mà các thư viện biểu đồ khác không cung cấp mức độ tùy chỉnh cần thiết.

---

### Kết luận

Sau khi đánh giá các thư viện dựa trên nhu cầu của dự án, **Apache ECharts** nổi lên là lựa chọn tốt nhất. Nó hỗ trợ đầy đủ các biểu đồ cần thiết, bao gồm bản đồ địa lý, biểu đồ nến và biểu đồ phân cụm. Nó là mã nguồn mở, giàu tính năng và có tính tương tác cao, hoàn toàn phù hợp với mục tiêu của dự án. Mặc dù **D3.js** mang lại sự linh hoạt nhất, độ phức tạp và khoản đầu tư thời gian của nó khiến nó kém lý tưởng cho một startup muốn lặp nhanh. **ApexCharts** và **Chart.js** là các lựa chọn thay thế tốt cho các dự án đơn giản hơn nhưng thiếu hỗ trợ các loại biểu đồ nâng cao.
