# Lưu trữ bí mật

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
  * [Hàm ý](#hàm-ý)
* [Liên quan](#liên-quan)
  * [Các quyết định liên quan](#các-quyết-định-liên-quan)
  * [Các yêu cầu liên quan](#các-yêu-cầu-liên-quan)
  * [Các tạo phẩm liên quan](#các-tạo-phẩm-liên-quan)
  * [Các nguyên tắc liên quan](#các-nguyên-tắc-liên-quan)
* [Ghi chú](#ghi-chú)
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Tóm tắt


### Vấn đề

Chúng tôi cần lưu trữ các bí mật, như mật khẩu, khóa riêng, token xác thực, v.v.

Một số bí mật hướng đến người dùng. Ví dụ, nhà phát triển của chúng tôi muốn có thể dùng điện thoại di động để tra cứu mật khẩu của một dịch vụ.

Một số bí mật hướng đến hệ thống. Ví dụ, pipeline phân phối liên tục của chúng tôi cần có thể tra cứu thông tin xác thực cho dịch vụ lưu trữ đám mây của chúng tôi.


### Quyết định

Bitwarden cho các bí mật hướng đến người dùng

Vault by HashiCorp cho các bí mật hướng đến hệ thống.


### Trạng thái

Đã quyết định. Chúng tôi mở với các phương án thay thế mới khi chúng xuất hiện.


## Chi tiết


### Giả định

Với mục đích này, và tình trạng hiện tại của chúng tôi, chúng tôi coi trọng sự tiện lợi hướng đến người dùng, như các ứng dụng di động dùng được.

  * Chúng tôi muốn đảm bảo truy cập nhanh và dễ dàng khi đang di chuyển, như cho một nhà phát triển làm kỹ thuật độ tin cậy hệ thống khi trực.

  * Chúng tôi muốn có thể chia sẻ một số bí mật giữa những người được chọn, như một nhóm.

Chúng tôi không cố giải quyết cho một nhà cung cấp duy nhất, như lưu trữ tất cả bí mật độc quyền trên Amazon hoặc Azure hoặc Google.

Chúng tôi không muốn các cách tiếp cận tùy tiện như "nhớ nó" hoặc "ghi vào một tờ giấy" hoặc "tự tìm cách lưu trữ của riêng bạn".

Mô hình bảo mật của chúng tôi cho mục đích này chấp nhận việc dùng các nhà cung cấp COTS được kính trọng, như các công cụ quản lý mật khẩu SaaS.


### Ràng buộc

Hiện tại chúng tôi muốn thứ gì đó dễ dàng, tức là không cần viết mã, không cần cài đặt máy chủ, không cần cam kết lớn, không cần chuẩn hóa mọi người.


### Lập trường

Chúng tôi đã cân nhắc:

1. Các trình quản lý mật khẩu dựng sẵn hướng đến người dùng: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG, v.v.

2. Các trình quản lý mật khẩu COTS hướng đến hệ thống: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Các cách tiếp cận hướng đến chia sẻ: dùng một tài liệu Google dùng chung, hoặc kênh Slack dùng chung, hoặc thư mục mạng dùng chung, v.v.

4. Các cách tiếp cận tùy tiện công nghệ thấp, như ghi nhớ, ghi một tờ giấy, hoặc dựa vào mỗi người dùng tự tìm cách của riêng họ.


### Lập luận

Bitwarden, LastPass, 1Password và Dashlane đều là các sản phẩm thương mại dựng sẵn.

  * Các loại tính năng tương tự cho người dùng, nhóm, tổ chức, v.v.

  * Khả năng trên máy tính để bàn cho Windows và Mac, và khả năng trên di động cho Android và iOS.

  * Các tiện ích mở rộng trình duyệt cho Chrome và Firefox, để tự động điền biểu mẫu, v.v.

Bitwarden có hai ưu điểm so với các sản phẩm khác:

  * Bitwarden là mã nguồn mở, nghĩa là bảo mật có thể được đánh giá chéo và công ty cũng được các nhà phát triển hướng đến bảo mật đánh giá cao rộng rãi.

  * Các giai thoại của những người làm phần mềm mô tả sự ưa thích đáng kể dành cho Bitwarden so với các sản phẩm khác.

Một bài viết tốt điển hình: https://jcs.org/2017/11/17/bitwarden

Một trang bình chọn song song điển hình: https://stackshare.io/stackups/bitwarden-vs-dashlane

Chúng tôi hoãn KeyPass, pass, GPG, v.v. vì có thêm độ phức tạp. Tất cả những thứ này trông như các giải pháp tốt cho người dùng kỹ thuật. GPG trông đặc biệt tốt cho những người dùng kỹ thuật muốn các khả năng hướng lệnh xuyên các hệ thống.

Chúng tôi hoãn KMS vì nó bị khóa vào một nhà cung cấp duy nhất.

Chúng tôi chọn Vault cho các nhu cầu hướng đến hệ thống, vì các đánh giá tích cực đến kinh ngạc, và vì HashiCorp có thành tích xuất sắc về phần mềm và hỗ trợ chất lượng hàng đầu.

Chúng tôi phủ quyết các cách tiếp cận chia sẻ như qua tài liệu dùng chung, kênh dùng chung, thư mục mạng dùng chung, v.v. Những cách này không mang lại các chất lượng bảo mật mà chúng tôi muốn.

Chúng tôi phủ quyết các cách tiếp cận tùy tiện công nghệ thấp, vì tất cả chúng tôi đều đồng ý đó không phải con đường dài hạn.


### Hàm ý

Các nhà phát triển có thể cần theo dõi bí mật ở hai nơi: Bitwarden cho truy cập hướng đến người dùng, và Vault cho truy cập hướng đến hệ thống.


## Liên quan


### Các quyết định liên quan

Quyết định chọn máy chủ CI/CD nào phải bao gồm bằng chứng về khả năng truy cập các bí mật.

Chúng tôi sẽ cần quyết định cách quản lý các bí mật, về mặt chính sách, luân phiên, tổ chức, v.v.


### Các yêu cầu liên quan

Các bí mật sẽ có các yêu cầu liên quan về tuân thủ, kiểm toán và tiếp nhận/thôi việc nhân sự.


### Các tạo phẩm liên quan

Chúng tôi kỳ vọng có thể xuất một số bí mật ra các biến môi trường.


### Các nguyên tắc liên quan

Dễ đảo ngược.

Dễ chạy song song, tức là dễ dùng nhiều loại trình quản lý mật khẩu.

Rẻ để thử, tức là có bản dùng thử miễn phí và không cam kết.


## Ghi chú

Các ghi chú đánh giá ở đây. Các ghi chú đều là bình luận công khai trên nhiều diễn đàn thảo luận devops.


### Vault by HashiCorp

Vault chính xác là thứ bạn muốn ở đây. 

Nhưng đừng cứ thế đưa Vault vào sản xuất, hãy dựng nó trong môi trường kiểm thử trước, vì tài liệu của HashiCorp có thể khá thiếu sót dù sản phẩm của họ tuyệt vời.

Đường cong học tập rất dốc và việc dựng lên không tầm thường. 

Việc thiết lập ban đầu hơi đau đầu. Nhưng hoàn toàn đáng giá, và cộng đồng sẽ hỗ trợ nó đủ để bạn xoay xở.

Tài liệu khủng khiếp nhưng có nhiều hướng dẫn trực tuyến của những người đã thiết lập nó và nếu bạn ghép một vài cái lại, bạn sẽ có một thiết lập hoạt động.

Việc thiết lập ban đầu phải mày mò với các helm chart của họ (vault và consul). Mặc dù về mặt kỹ thuật bạn có thể dùng nhiều back-end khác, tôi thực sự, thực sự không khuyên. Back-end/consul có thể rất nhỏ nếu bạn không có nhiều dữ liệu để lưu.

Chắc chắn hãy làm quen/thành thạo với việc dùng CLI, vì GUI giống một cổng minh chứng khái niệm/quảng cáo cho phiên bản doanh nghiệp của họ hơn.

Việc bạn không thể chỉ "điền đầy" nó là một điều đau đầu. Ví dụ nếu bạn có 5 trường, bạn phải thêm thủ công từng trường cho từng mục. Vì vậy không phải bạn định nghĩa trước các trường cho một danh mục cụ thể, và điền các trường đó cho tất cả các mục trong danh mục đó, mà giống như "bạn tạo mọi thứ mỗi lần", điều mà (theo tôi) rất phiền phức.

Bạn cũng có thể muốn xem goldfish như một UI đặt trên vault. Nó khiến việc thuyết phục nhóm của bạn dùng khá tốt. Họ cũng có một bản demo. 1. Thiết lập consul. 2. Thiết lập vault trỏ tới consul. 3. Thiết lập goldfish trỏ tới vault. 3. Thiết lập một cron job nào đó để chạy consul snapshot cho sao lưu.



### LastPass

LastPass Teams. Chúng tôi dùng nó, có các mẫu tùy chỉnh, ACL, theo tôi không thiếu gì.

Tôi đã triển khai LastPass ở tổ chức của mình và cho nó C+/B-. Vấn đề lớn nhất gần đây là thiếu độ tin cậy. Trong 90 ngày qua có nhiều giờ mà các kho bị buộc vào chế độ ngoại tuyến. Điều này không lý tưởng cho tổ chức của tôi vì chúng tôi, theo đúng nghĩa đen, lưu hơn 4.000 mật khẩu trong hơn 20 thư mục dùng chung. Như bạn có thể hình dung với nhiều mật khẩu như vậy ít nhất một vài cái được cập nhật hoặc thêm mỗi ngày. Chúng tôi có kế hoạch DR nếu sự cố kéo dài hơn một hoặc hai giờ: một tập lệnh ký và mã hóa một bản kết xuất CSV của kho mỗi đêm có thể nhập vào keepass.

LastPass đã có những lần suy giảm dịch vụ thoáng qua không được báo cáo: đăng nhập 'hoạt động' nhưng không kéo các trang, các tính năng ngẫu nhiên trong bảng quản trị bị hỏng, và không chia sẻ đúng khóa cho các thư mục dùng chung cấp cao nhất mới. Tôi có một người dùng 'đẩy khóa'/sao lưu cụ thể nằm trong mọi nhóm. Thường đăng nhập bằng người dùng đó sẽ khắc phục mọi vấn đề chia sẻ khóa nhưng không khi dịch vụ đang suy giảm bất kể trang trạng thái nói gì...

Về tích hợp, nó có thể dễ nếu bạn có các ACL phù hợp với mô hình đặc quyền tối thiểu, ví dụ nếu một người dùng có cả đọc & ghi và chỉ đọc trên một mục hoặc thư mục thì họ chỉ nhận quyền chỉ đọc. Tiếc là các ACL của tổ chức tôi không phải tốt nhất, nên tôi cuối cùng dùng API cấp phát JSON và ~500 dòng python vì bản chất phụ thuộc của hàng trăm ACL của chúng tôi không ánh xạ tốt vào mô hình đặc quyền tối thiểu. Cuối cùng tôi lấy tất cả các ACL mà một người dùng thuộc về và thực hiện một kiểu duyệt phụ thuộc.

Nếu cấu trúc ACL hoặc nhóm của bạn đã được xây dựng với cấu trúc đặc quyền tối thiểu trong đầu thì công cụ đồng bộ AD/LDAP cho Windows sẽ hoạt động tốt.

Liên hệ đội bán hàng của họ và họ có thể cho bạn bản dùng thử Enterprise dài hơn. Hãy chắc chắn bạn hiểu đầy đủ các hạn chế của nó trước khi quyết định. Chúng tôi đã gặp khá nhiều nỗi đau tăng trưởng nhưng ngoài các sự cố hoặc suy giảm phía máy chủ thì nó đã cực kỳ suôn sẻ.


### Bitwarden

Bitwarden có bộ công cụ tốt xung quanh (WebUI, CLI, Di động, Máy tính để bàn). Có thể tự lưu trữ và khá dễ thiết lập. Tài liệu khá tốt và là công cụ được PrivacyTools khuyên dùng.


### EnvKey

https://www.envkey.com/ là một saas. Thực sự dễ triển khai, tích hợp và quản lý.

Tính năng:

  * Bảo vệ khóa API và thông tin xác thực.

  * Giữ cấu hình đồng bộ ở mọi nơi.

  * Quản lý cấu hình và bí mật thông minh, mã hóa đầu-cuối. 

  * Ngăn chặn chia sẻ không an toàn và sự lan tràn cấu hình. 

  * Tích hợp trong vài phút.

Khả năng:

  * Quản lý cấu hình và các mức truy cập cho tất cả ứng dụng, môi trường và nhóm của bạn ở một nơi.

  * Cấu hình bất kỳ môi trường phát triển hoặc máy chủ nào chỉ với một biến môi trường duy nhất.

Ưu điểm:

  * Trang chủ tốt.

  * Đề xuất giá trị rõ ràng.

  * Ứng dụng web xuất sắc về mặt thị giác.

  * Dữ liệu mẫu vượt trội, ví dụ Algolia, AWS, Datadog, GitHub, Stripe, v.v.

  * Đã nói chuyện với người sáng lập 30 phút về công ty, UI, v.v. Dane nghe có vẻ am hiểu, trung thực về ưu/nhược điểm, và là một đối tác khả thi.

  * Công ty về cơ bản là một công ty Y Combinator điển hình, với 1 người sáng lập. Đã gọi được $120K vào 2018-01.

  * Trọng tâm là tiến tới các tính năng doanh nghiệp, đặc biệt là chuyển từ lưu trữ đám mây EnvKey sang tại chỗ hoặc BYOC.

  * Con đường tiềm năng phía trước: bắt đầu với EnvKey vì dễ dùng, rồi sau đó (hoặc song song) thêm Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant là một dịch vụ quản lý bí mật mã nguồn mở cung cấp khả năng lưu trữ và truy cập bí mật thân thiện với người dùng một cách an toàn, từ các nhà phát triển tại Lyft.

Xác thực KMS: Confidant giải quyết bài toán "con gà và quả trứng" của xác thực bằng cách dùng AWS KMS và IAM để cho phép các vai trò IAM tạo các token xác thực an toàn có thể được Confidant xác minh. Confidant cũng quản lý các grant KMS cho các vai trò IAM của bạn, cho phép các vai trò IAM tạo các token có thể dùng cho xác thực dịch vụ-với-dịch vụ, hoặc để truyền các thông điệp được mã hóa giữa các dịch vụ.

Mã hóa khi lưu trữ các bí mật có phiên bản: Confidant lưu các bí mật theo cách chỉ-thêm trong DynamoDB, tạo một khóa dữ liệu KMS duy nhất cho mọi bản sửa đổi của mọi bí mật, dùng mật mã xác thực đối xứng Fernet.

Một giao diện web thân thiện với người dùng để quản lý bí mật: Confidant cung cấp một giao diện web AngularJS cho phép người dùng cuối dễ dàng quản lý bí mật, ánh xạ bí mật tới dịch vụ và lịch sử thay đổi.


### Devolutions Password Server

https://server.devolutions.net/

Bảo mật, quản lý và giám sát quyền truy cập vào các tài khoản và phiên đặc quyền.

Một kho mật khẩu toàn diện, được bảo mật cao cho phép bạn kiểm soát quyền truy cập vào các tài khoản đặc quyền, đồng thời cải thiện khả năng quan sát mạng tổng thể cho các quản trị viên hệ thống và mang lại trải nghiệm liền mạch cho người dùng cuối.

Tính năng: kho mật khẩu tổ chức tập trung, kho riêng dành riêng cho người dùng, trình quản lý mật khẩu, chèn thông tin xác thực,
tích hợp Active Directory, kiểm soát truy cập dựa trên vai trò, xác thực hai yếu tố, sẵn sàng cho doanh nghiệp, hạn chế IP, khả năng quản lý, trình tạo mật khẩu tự động, truy cập ứng dụng di động, lịch sử mật khẩu, báo cáo truy cập, cảnh báo email.

  * hỗ trợ mã hóa dữ liệu

  * hỗ trợ nhiều lược đồ Xác thực bao gồm LDAP, O365 và người dùng Cục bộ CÓ hỗ trợ MFA từ nhiều nguồn

  * nhiều kho/két với kiểm soát truy cập chi tiết cho nhiều nhóm

  * Web UI hiện đại

  * các kho thông tin xác thực và kết nối riêng cho thông tin xác thực/kết nối cá nhân

  * ứng dụng di động cho IOS/Android

  * nhật ký kiểm toán cho từng mục, ai/cái gì/khi nào kèm một lời nhắc tùy chọn về lý do họ truy cập

  * các mẫu có thể tùy chỉnh (mặc dù chúng hỗ trợ gốc hàng trăm loại kết nối)

  * hàng tá tính năng khác và một ứng dụng khách nặng Windows/Mac (Remote Desktop Manager) mà bạn có thể đồng bộ vào và mở rộng đáng kể các tùy chọn...kết nối một cú nhấp

  * giá không quá tệ - tối đa 15 người dùng là $500 mỗi năm cho máy chủ mật khẩu


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Tính năng phiên bản tại chỗ: 

  * Toàn quyền kiểm soát các hệ thống và hạ tầng bảo mật đầu-cuối của bạn

  * Triển khai phần mềm trong trung tâm dữ liệu tại chỗ hoặc phiên bản đám mây riêng ảo của riêng bạn

  * Đáp ứng các nghĩa vụ pháp lý và quy định đòi hỏi mọi dữ liệu và hệ thống phải nằm tại chỗ

Tính năng phiên bản đám mây:

  * Mô hình phần mềm như một dịch vụ cho phép bạn đăng ký và bắt đầu ngay

  * Khả năng mở rộng linh hoạt khi bạn phát triển

  * Các biện pháp kiểm soát và dự phòng do Azure cung cấp với SLA thời gian hoạt động 99,9%

Phản hồi của người dùng:

  * Chúng tôi từng dùng sản phẩm đó. Nó rất dễ bị vượt qua và các quy tắc chỉ hiệu quả với người thông minh. Người dùng lười hoặc ngốc có thể dễ dàng làm hỏng nó trong khu vực nhóm. Giá có thể thương lượng khi bạn nói chuyện với họ.

  * Bạn có thể chạy nó bằng SQL express và một máy Win 7. 

  * Rẻ.
