# Bản ghi quyết định kiến trúc: các lựa chọn xác thực và phân quyền

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Xác thực và phân quyền ứng dụng web là hai khái niệm quan trọng để bảo vệ quyền truy cập vào các ứng dụng và dịch vụ. Cả hai đều liên quan đến danh tính của người dùng và cách cấp quyền, nhưng tập trung vào các khía cạnh khác nhau:

- **Xác thực (Authentication)** là quá trình xác minh danh tính của một người dùng hoặc hệ thống.
- **Phân quyền (Authorization)** là quá trình xác định những tài nguyên hoặc hành động mà người dùng hoặc hệ thống đã được xác thực có thể truy cập.

Bây giờ, hãy đi sâu vào các giao thức và công nghệ cụ thể mà bạn đã đề cập, thường được dùng trong các ứng dụng web hiện đại để quản lý xác thực và phân quyền.

### 1. **OAuth (Open Authorization)**

**OAuth** là một chuẩn mở cho phân quyền. Nó cho phép người dùng cấp cho một ứng dụng bên thứ ba quyền truy cập hạn chế vào tài nguyên của họ mà không chia sẻ thông tin xác thực. Ý tưởng then chốt là **truy cập được ủy quyền**. OAuth thường được dùng trong các tình huống người dùng có thể đăng nhập vào dịch vụ bên thứ ba (ví dụ, đăng nhập bằng Google) mà không cung cấp trực tiếp tên người dùng và mật khẩu cho bên thứ ba.

- **Luồng**: OAuth thường theo luồng **dựa trên token**, trong đó một máy chủ phân quyền cấp một token truy cập cho ứng dụng bên thứ ba. Token này đại diện cho các quyền của người dùng, và ứng dụng dùng nó để truy cập dữ liệu hoặc tài nguyên của người dùng từ một API.
- **Ví dụ**: Một người dùng đăng nhập vào ứng dụng bên thứ ba bằng tài khoản Google của họ. Google xác minh danh tính người dùng rồi cấp một token cho phép ứng dụng bên thứ ba truy cập một số dữ liệu Google (ví dụ, Google Calendar).

OAuth **không** xử lý xác thực trực tiếp; nó là về việc cấp quyền truy cập. Để xác thực, OAuth thường được kết hợp với các giao thức khác, như **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** là một lớp danh tính được xây dựng trên **OAuth 2.0**, bổ sung xác thực vào khả năng phân quyền của OAuth. Về cơ bản, OpenID Connect mở rộng OAuth để xử lý **xác thực người dùng** và cung cấp cách thức chuẩn hóa để các ứng dụng xác minh danh tính người dùng.

- **Luồng**: Khi người dùng đăng nhập bằng OpenID Connect, ứng dụng bên thứ ba yêu cầu một token ID (ngoài token truy cập OAuth). Token ID chứa thông tin về người dùng (như tên người dùng, email và các claim khác). Điều này cho phép ứng dụng biết người dùng là ai và họ đã được xác thực hay chưa.
- **Ví dụ**: Đăng nhập vào một dịch vụ như Slack bằng tài khoản Google của bạn (Google là nhà cung cấp OpenID Connect) liên quan đến xác thực qua OpenID Connect, trong khi OAuth quản lý quyền truy cập vào tài nguyên Google của bạn.

OIDC giúp các ứng dụng bên thứ ba dễ dàng **xác thực người dùng** hơn đồng thời vẫn cho phép kiểm soát chi tiết các tài nguyên mà những ứng dụng đó có thể truy cập.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** là một chuẩn cũ hơn, dựa trên XML, dùng để trao đổi dữ liệu xác thực và phân quyền giữa các bên, đặc biệt trong các kịch bản **Đăng nhập một lần (SSO)**. Nó chủ yếu được dùng trong môi trường doanh nghiệp để cho phép người dùng xác thực một lần và truy cập nhiều ứng dụng mà không cần nhập lại thông tin xác thực.

- **Luồng**: Người dùng trước tiên xác thực với nhà cung cấp danh tính (IdP). IdP tạo ra một **khẳng định SAML** đã ký chứa danh tính người dùng và các thuộc tính liên quan. Khẳng định được gửi tới nhà cung cấp dịch vụ (SP), nơi dùng nó để phân quyền truy cập vào ứng dụng.
- **Ví dụ**: Một nhân viên đăng nhập vào cổng thông tin công ty (IdP) và tự động được đăng nhập vào các hệ thống khác như email, CRM, v.v. mà không cần nhập lại thông tin xác thực. Quá trình xác thực dựa trên khẳng định SAML do IdP gửi.

SAML thường được dùng trong **các giải pháp SSO doanh nghiệp** và hoạt động tốt cho các ứng dụng web trong môi trường doanh nghiệp, nhưng kém thân thiện với di động hơn so với OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** là một giao thức khác dùng cho **Đăng nhập một lần (SSO)**, đặc biệt trong môi trường doanh nghiệp dựa trên Microsoft. Nó là một phần của họ đặc tả **WS-* (Web Services)** và cho phép liên hiệp danh tính giữa các miền bảo mật khác nhau (như giữa các tổ chức khác nhau hoặc giữa các dịch vụ khác nhau).

- **Luồng**: WS-Federation cho phép một **nhà cung cấp danh tính (IdP) đáng tin cậy** xác thực người dùng và cấp các token mà nhà cung cấp dịch vụ có thể dùng để phân quyền. Nó tương tự SAML nhưng thường được dùng trong các kịch bản phụ thuộc nhiều vào công nghệ Microsoft.
- **Ví dụ**: Một người dùng đăng nhập vào một ứng dụng doanh nghiệp được lưu trữ trên Microsoft Azure Active Directory (AD), và danh tính của họ có thể được dùng để truy cập các dịch vụ liên hiệp khác, bao gồm các ứng dụng do nhà cung cấp bên thứ ba lưu trữ.

Mặc dù WS-Federation phần lớn đã được thay thế bằng các giao thức mới hơn như OAuth2.0 và OpenID Connect trong nhiều môi trường web hiện đại, nó vẫn được dùng trong các hệ thống kế thừa, đặc biệt trong các doanh nghiệp lấy Microsoft làm trung tâm.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** là một giao thức dùng để truy cập và quản lý các dịch vụ thư mục, thường được dùng để **lưu trữ thông tin xác thực người dùng** và quản lý kiểm soát truy cập trong một thư mục tập trung (thường gọi là **Dịch vụ Thư mục**). LDAP không đặc biệt về xác thực hay phân quyền mà được dùng để lưu trữ và truy xuất dữ liệu danh tính, sau đó được dùng trong các quy trình đó.

- **Xác thực**: LDAP cho phép một ứng dụng xác thực người dùng bằng cách truy vấn dịch vụ thư mục để lấy thông tin xác thực (như mật khẩu).
- **Phân quyền**: Nó cũng quản lý vai trò và quyền của người dùng, giúp xác định liệu người dùng có quyền truy cập các tài nguyên nhất định hay không.
- **Ví dụ**: Nhiều doanh nghiệp dùng các thư mục dựa trên LDAP (ví dụ **Active Directory**) cho xác thực và phân quyền, đặc biệt trong môi trường Windows.

LDAP rất quan trọng đối với các doanh nghiệp để quản lý quyền truy cập của người dùng trên các hệ thống nội bộ, nhưng trong bối cảnh web hiện đại, LDAP thường được tích hợp với các giao thức khác như SAML hoặc OAuth để quản lý danh tính đầy đủ hơn.

### 6. **Nhà cung cấp SSO mạng xã hội**

Các nhà cung cấp **Đăng nhập một lần (SSO)** mạng xã hội như **Facebook**, **Google**, **Twitter**, **GitHub** và những nhà cung cấp khác cho phép người dùng xác thực vào các ứng dụng bên thứ ba bằng thông tin xác thực mạng xã hội của họ. Đây là một loại **xác thực dựa trên OAuth** trong đó dịch vụ bên thứ ba (ví dụ Google) là nhà cung cấp danh tính.

- **Luồng**: Người dùng nhấp vào "Đăng nhập bằng Google" (ví dụ). Ứng dụng chuyển hướng tới Google, nơi người dùng đăng nhập (nếu chưa đăng nhập). Sau đó Google cung cấp một token truy cập hoặc token ID cho ứng dụng bên thứ ba, có thể dùng để xác thực người dùng và có thể truy cập dữ liệu của họ.
- **Ví dụ**: Nhiều ứng dụng cho phép bạn đăng nhập bằng thông tin xác thực Google hoặc Facebook. Ứng dụng sẽ dùng OAuth hoặc OpenID Connect ở phía sau để xác minh danh tính của bạn và, trong một số trường hợp, truy cập một số dữ liệu mạng xã hội nhất định.

SSO mạng xã hội là một phương pháp xác thực tiện lợi và được áp dụng rộng rãi vì nó giảm bớt rào cản cho người dùng, những người có thể không muốn tạo thêm một tên người dùng và mật khẩu nữa.

---

### Tóm tắt các khác biệt:

- **OAuth**: Dùng cho phân quyền, cho phép các ứng dụng bên thứ ba truy cập dữ liệu người dùng mà không để lộ thông tin xác thực.
- **OpenID Connect**: Mở rộng OAuth để cung cấp xác thực, cho phép các ứng dụng xác minh danh tính người dùng.
- **SAML**: Giao thức dựa trên XML dùng cho SSO, thường trong môi trường doanh nghiệp.
- **WS-Federation**: Một giao thức đặc thù của Microsoft để liên hiệp danh tính, dùng trong các hệ thống kế thừa.
- **LDAP**: Một giao thức để truy vấn các dịch vụ thư mục nhằm xác thực người dùng và quản lý phân quyền.
- **Nhà cung cấp SSO mạng xã hội**: Các hệ thống dựa trên OAuth (như Google, Facebook) cho phép các ứng dụng bên thứ ba xác thực người dùng bằng thông tin xác thực mạng xã hội của họ.

Mỗi công nghệ này đều có điểm mạnh và trường hợp sử dụng riêng, và trong các ứng dụng hiện đại, bạn có thể thấy sự kết hợp của chúng được dùng cho các khía cạnh khác nhau của bảo mật (ví dụ, OAuth/OIDC cho truy cập API, SAML cho SSO doanh nghiệp).
