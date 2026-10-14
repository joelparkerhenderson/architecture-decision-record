## Bản ghi quyết định kiến trúc: framework tự động hóa trình duyệt cho kiểm thử E2E (Playwright so với Selenium)

### 1. **Bối cảnh**

Chúng tôi đang trong quá trình chọn một framework tự động hóa trình duyệt cho pipeline kiểm thử đầu-cuối (E2E) của mình. Framework này sẽ là một phần không thể thiếu trong các quy trình CI/CD của chúng tôi, chạy các bài kiểm thử mô phỏng tương tác người dùng thực trên nền tảng của chúng tôi. Cụ thể, các bài kiểm thử sẽ bao quát các kịch bản như đăng ký/đăng nhập người dùng, tải tệp lên, tương tác bảng điều khiển và tải xuống báo cáo.

Là một **startup**, trọng tâm của chúng tôi là **phát triển agile**, với nhu cầu lặp và phát triển nhanh chóng. Nhóm của chúng tôi chủ yếu làm việc với **TypeScript** và **Python**, và khả năng viết kiểm thử bằng các ngôn ngữ này là thiết yếu. Ngoài ra, nền tảng có **biểu đồ và bảng điều khiển tương tác**, khiến điều then chốt là công cụ tự động hóa hỗ trợ tốt các UI phong phú, động.

Hai ứng viên cho nhiệm vụ này là **Playwright** và **Selenium**, mỗi bên có điểm mạnh và đánh đổi riêng. Chúng tôi cần đánh giá các framework này dựa trên các tính năng và yêu cầu nêu dưới đây.

### 2. **Các lựa chọn đã cân nhắc**

- **Playwright** (của Microsoft)
- **Selenium** (của Selenium Project)

### 3. **Các yếu tố thúc đẩy quyết định**

Các yếu tố ảnh hưởng đến quyết định của chúng tôi như sau:

1. **Phát triển Agile**: Công cụ được chọn phải cho phép các chu kỳ phát triển nhanh, linh hoạt.
2. **Hỗ trợ ngôn ngữ**: Nhóm của chúng tôi cần hỗ trợ cho cả **TypeScript** và **Python**.
3. **Kiểm thử UI tương tác**: Khả năng kiểm thử một cách đáng tin cậy các biểu đồ, bảng điều khiển và phần tử động tương tác là thiết yếu.
4. **Tốc độ thời gian chạy**: Mặc dù không phải mối quan tâm chính, hiệu năng trong các pipeline CI/CD là một cân nhắc.
5. **Khả năng mở rộng**: Chúng tôi không lên kế hoạch mở rộng quy mô lớn trong tương lai gần, nhưng chúng tôi muốn đảm bảo giải pháp có thể xử lý sự tăng trưởng trong tương lai.
6. **Tương thích ngược**: Các hệ thống kế thừa và khả năng tương thích với trình duyệt cũ không quan trọng đối với dự án của chúng tôi vào lúc này.
7. **Kiểm thử trên di động**: Mặc dù không phải trọng tâm trước mắt, framework nên có khả năng kiểm thử các tính năng đáp ứng trên di động hoặc có thể mở rộng cho các trường hợp sử dụng như vậy.
8. **Kiểm thử đa màn hình**: Hỗ trợ cấu hình đa màn hình là yêu cầu thứ cấp, đặc biệt nếu chúng tôi từng mở rộng sang kiểm thử các quy trình làm việc người dùng phức tạp hơn.
9. **Kiểm thử tải tệp lên**: Framework phải xử lý việc tải tệp lên hiệu quả, một yêu cầu cốt lõi trong nhu cầu kiểm thử của chúng tôi.

### 4. **Tiêu chí đánh giá**

- **Dễ dùng**: Viết và bảo trì kiểm thử dễ đến mức nào?
- **Hỗ trợ ngôn ngữ**: Framework có hỗ trợ TypeScript và Python, hai ngôn ngữ mà nhóm chúng tôi dùng thường xuyên nhất không?
- **Kiểm thử UI tương tác**: Framework xử lý các giao diện người dùng phức tạp, tương tác như biểu đồ, tải tệp lên và dữ liệu động tốt đến mức nào?
- **Tích hợp CI/CD**: Framework tích hợp tốt đến mức nào vào các công cụ và dịch vụ CI/CD phổ biến?
- **Hỗ trợ đa trình duyệt**: Những trình duyệt nào được hỗ trợ và chúng hoạt động tốt đến đâu?
- **Hiệu năng và tốc độ**: Các bài kiểm thử chạy nhanh đến mức nào, đặc biệt trong pipeline CI/CD?
- **Khả năng mở rộng**: Framework có thể mở rộng tốt đến mức nào nếu thêm nhiều bài kiểm thử hơn hoặc các kịch bản phức tạp hơn?
- **Cộng đồng và hệ sinh thái**: Cộng đồng của framework năng động đến mức nào? Có nhiều tích hợp và tiện ích mở rộng không?

### 5. **Cân nhắc**

#### 5.1 **Playwright**

##### **Ưu điểm**:
1. **API thông minh hơn cho tải tệp cục bộ lên**: API của Playwright để tương tác với tệp cục bộ và thực hiện tải tệp lên đơn giản và trực quan hơn. Điều này sẽ giúp việc triển khai và bảo trì kiểm thử tải tệp lên dễ hơn.
2. **Cú pháp và sinh mã**: Playwright có cú pháp ngắn hơn, súc tích hơn. Điều này dẫn đến ít mã khuôn mẫu hơn, cải thiện khả năng bảo trì và hiệu suất của nhà phát triển. Ngoài ra, cú pháp ngắn hơn này cải thiện chất lượng sinh mã của OpenAI, giúp việc tự động tạo các tập lệnh kiểm thử dễ hơn.
3. **Kiểm thử UI tương tác**: Playwright xuất sắc trong việc kiểm thử các ứng dụng web động, tương tác, như những ứng dụng có biểu đồ phong phú, tương tác người dùng phức tạp và cập nhật thời gian thực. Nó xử lý WebSockets, WebRTC, shadow DOM và các công nghệ web hiện đại khác rất hiệu quả.
4. **Hỗ trợ đa trình duyệt**: Playwright hỗ trợ **Chromium**, **WebKit** và **Firefox**. Nó có hiệu năng nhất quán trên các trình duyệt này, sẽ bao quát hầu hết nhu cầu kiểm thử của chúng tôi.
5. **Tích hợp CI/CD**: Playwright tích hợp liền mạch với các nền tảng CI/CD hiện đại (GitHub Actions, Jenkins, v.v.). Nó có thể chạy kiểm thử song song trên các trình duyệt khác nhau, tối ưu thời gian chạy kiểm thử và khiến nó phù hợp cho phát triển nhanh.
6. **Nhanh và đáng tin cậy**: Playwright nhìn chung nhanh hơn Selenium, đặc biệt ở chế độ headless, và bền bỉ hơn khi xử lý các phần tử web bất đồng bộ.

##### **Nhược điểm**:
1. **Kiểm thử trên di động hạn chế**: Mặc dù Playwright hỗ trợ giả lập di động cho trình duyệt, nó thiếu khả năng kiểm thử di động gốc như tích hợp của Selenium với Appium để kiểm thử di động thực sự.
2. **Hệ sinh thái nhỏ hơn**: Playwright vẫn mới hơn và kém thành lập hơn Selenium. Mặc dù có cộng đồng phát triển nhanh và tài liệu tốt, nó có thể chưa có hệ sinh thái plugin và tích hợp rộng lớn như Selenium cung cấp.
3. **Hỗ trợ trình duyệt hạn chế**: Mặc dù Playwright bao quát các trình duyệt hiện đại chính (Chrome, Safari, Firefox), hỗ trợ cho các trình duyệt cũ (ví dụ Internet Explorer) không mạnh bằng Selenium.

#### 5.2 **Selenium**

##### **Ưu điểm**:
1. **Lịch sử lâu hơn và sự trưởng thành**: Selenium đã tồn tại từ lâu và có thành tích đã được chứng minh. Nó được dùng rộng rãi ở nhiều nhóm và ngành, điều này đã tạo nên một hệ sinh thái rộng lớn gồm các plugin, tích hợp và tài nguyên.
2. **Hỗ trợ đa trình duyệt và đa nền tảng**: Selenium hỗ trợ **nhiều loại trình duyệt** và phiên bản, bao gồm **Internet Explorer**, và cũng có thể được tích hợp với nhiều công cụ như **Docker**, **Selenium Grid** và **dịch vụ đám mây** để kiểm thử phân tán.
3. **Kiểm thử trên di động**: Selenium, thông qua tích hợp với **Appium**, vững chắc hơn nhiều cho kiểm thử di động, bao gồm cả ứng dụng Android và iOS. Điều này khiến nó là lựa chọn tốt hơn cho các dự án ưu tiên di động hoặc nặng về di động.
4. **Kiểm thử đa màn hình**: Selenium cung cấp hỗ trợ tốt hơn cho các kịch bản liên quan đến **nhiều màn hình** hoặc các tương tác đa cửa sổ phức tạp.

##### **Nhược điểm**:
1. **Độ phức tạp**: API của Selenium dài dòng và tường minh hơn. Mặc dù điều này có thể là lợi thế trong một số trường hợp, nó có nghĩa là phải viết và bảo trì nhiều mã hơn, có thể làm giảm sự nhanh nhẹn của nhà phát triển, đặc biệt quan trọng trong môi trường startup.
2. **Hiệu năng**: Selenium nhìn chung chạy chậm hơn Playwright, đặc biệt ở chế độ headless. Điều này có thể ảnh hưởng đến các pipeline CI/CD, đặc biệt khi số lượng kiểm thử tăng lên.
3. **Kiểm thử UI tương tác**: Selenium không mượt mà bằng Playwright khi kiểm thử các UI web hiện đại, tương tác, đặc biệt với biểu đồ và cập nhật dữ liệu thời gian thực. Nó đòi hỏi nhiều thiết lập và xử lý hơn để tương tác đáng tin cậy với nội dung động.

### 6. **Tóm tắt so sánh**

| Tính năng                          | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Dễ dùng**                   | Cú pháp ngắn hơn, trực quan hơn cho UI hiện đại | Tường minh hơn, cần nhiều mã khuôn mẫu hơn  |
| **Hỗ trợ ngôn ngữ**              | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Kiểm thử UI tương tác**        | Xuất sắc cho UI động, thời gian thực          | Xử lý các UI cơ bản, nhưng dài dòng và phức tạp hơn cho các tương tác phong phú |
| **Kiểm thử tải tệp lên**           | API thông minh hơn cho tải tệp lên                  | Dài dòng hơn, API kém trực quan hơn         |
| **Tích hợp CI/CD**             | Tích hợp dễ với GitHub Actions, Jenkins | Tích hợp mạnh với nhiều công cụ CI    |
| **Kiểm thử trên di động**                | Hạn chế, chỉ giả lập                       | Hỗ trợ đầy đủ thông qua Appium               |
| **Hỗ trợ đa trình duyệt**         | Chromium, WebKit, Firefox                     | Hỗ trợ đầy đủ trên các trình duyệt chính và cũ |
| **Hiệu năng**                   | Nhanh, tối ưu cho kiểm thử headless          | Chậm hơn, đặc biệt ở chế độ headless       |
| **Kiểm thử đa màn hình**         | Hạn chế                                       | Hỗ trợ tốt cho các thiết lập đa màn hình    |
| **Cộng đồng và hệ sinh thái**       | Đang phát triển, tài liệu tốt                   | Lớn, trưởng thành, hệ sinh thái rộng lớn       |

### 7. **Quyết định**

Sau khi cân nhắc các yêu cầu và đánh đổi, **Playwright** là lựa chọn tốt hơn cho nhu cầu hiện tại của chúng tôi. API thông minh hơn của nó cho kiểm thử tải tệp cục bộ lên, cú pháp súc tích và hỗ trợ mạnh cho kiểm thử UI tương tác khiến nó là sự phù hợp lý tưởng cho chu kỳ phát triển agile của chúng tôi. Việc nó hỗ trợ cả **TypeScript** và **Python** là then chốt với nhóm của chúng tôi, và cách tiếp cận hiện đại của framework đối với kiểm thử sẽ cho phép chúng tôi viết mã sạch, dễ bảo trì.

Mặc dù **Selenium** vẫn là một công cụ tuyệt vời, đặc biệt cho kiểm thử di động, hỗ trợ trình duyệt cũ và thiết lập đa màn hình, nó kém phù hợp với nhu cầu hiện tại của chúng tôi. Sự dài dòng, hiệu năng chậm hơn và việc xử lý phức tạp hơn các UI động như biểu đồ khiến nó kém tối ưu cho trường hợp sử dụng của chúng tôi.

### 8. **Hệ quả**

- **Hành động ngay**: Chúng tôi sẽ áp dụng **Playwright** cho kiểm thử E2E của mình, tập trung vào việc kiểm thử các luồng người dùng liên quan đến đăng ký, đăng nhập, tải tệp lên, bảng điều khiển và tải xuống báo cáo.
- **Cân nhắc dài hạn**: Chúng tôi sẽ theo dõi sự phát triển của hệ sinh thái Playwright. Nếu nhu cầu của chúng tôi thay đổi, đặc biệt về kiểm thử di động hoặc hỗ trợ trình duyệt cũ, chúng tôi có thể xem xét lại Selenium.
- **Đào tạo và tài liệu**: Các nhóm phát triển sẽ cần làm quen với API của Playwright, đặc biệt để xử lý các UI động và tải tệp lên.
- **Di chuyển**: Các bài kiểm thử Selenium hiện có (nếu có) sẽ được dần dần di chuyển sang Playwright.

### 9. **Các cân nhắc trong tương lai**
