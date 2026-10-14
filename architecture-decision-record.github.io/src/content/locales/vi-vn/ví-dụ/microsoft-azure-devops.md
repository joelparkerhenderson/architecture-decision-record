# Microsoft Azure DevOps

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
  * [Microsoft Devops CI: An Unsatisfying Adventure](#microsoft-devops-ci-an-unsatisfying-adventure)
  * [Những điểm nổi bật của thảo luận trên Hacker News](#những-điểm-nổi-bật-của-thảo-luận-trên-hacker-news)
  * [Windows Development MVP](#windows-development-mvp)
  * [Tóm tắt về Edward Thomson (Azure PM)](#tóm-tắt-về-edward-thomson-azure-pm)


## Tóm tắt


### Vấn đề

Chúng tôi muốn dùng devops để build, tích hợp, triển khai và lưu trữ các dự án của mình. Chúng tôi đang cân nhắc Microsoft Azure DevOps.

  * Chúng tôi muốn trải nghiệm nhà phát triển nhanh và đáng tin cậy, cho việc thiết lập devops, ví dụ cấu hình, cũng như việc dùng liên tục, ví dụ thời gian build nhanh.
  
  * Chúng tôi muốn cân nhắc dùng Microsoft Azure như một tổng thể, để lưu trữ các ứng dụng dự án, cơ sở dữ liệu, v.v.


### Quyết định

Đã quyết định không chọn Microsoft Azure DevOps.


### Trạng thái

Đã quyết định. Mở để xem xét lại nếu/khi có thông tin quan trọng mới.


## Chi tiết


### Giả định

Tất cả các giả định devops thông thường, như trong cuốn sách Accelerate.

  * Các bản build nhanh là một sự trợ giúp đáng kể. Điều này đẩy nhanh các vòng phản hồi.

  * Chúng tôi có thể thay thế vào/ra các thành phần từ các nhà cung cấp khác, tức là chúng tôi có thể muốn mang theo các máy chủ build tốc độ cao hơn của mình, hoặc dùng hệ thống kiểm soát phiên bản do chúng tôi chọn, hoặc phối hợp với một máy chủ tích hợp liên tục tự lưu trữ.
  
  * Tính dễ dùng được tinh gọn là một sự trợ giúp đáng kể, cho trải nghiệm nhà phát triển, và đến lượt nó cho các khía cạnh tinh tế như tính nhất quán, sự rõ ràng, bảo mật và độ dễ của đường cong học tập.

  * Khi có bất cứ thứ gì hỏng hoặc có vấn đề, chúng tôi muốn có một cách hiệu quả để báo cáo vấn đề. Điều này đặc biệt quan trọng đối với mọi vấn đề liên quan đến bảo mật.


### Ràng buộc

Không có ràng buộc nào được biết. Azure có một cam kết đã công bố về việc hoạt động tốt với các công cụ bên ngoài.


### Lập trường

Chúng tôi đã cân nhắc việc dùng Microsoft Azure Devops so với AWS vốn là đương nhiệm.

Chúng tôi đã thử nghiệm với Azure DevOps, Azure Pipelines, Azure Repo và việc Azure khởi tạo máy chủ mới thông qua Terraform.

Chúng tôi đã thử nghiệm việc nhận hỗ trợ từ các đại diện của Microsoft.

Chúng tôi đã thu thập thông tin từ các đồng nghiệp trên blog và Hacker News.


### Lập luận

Azure DevOps quảng cáo một bộ sản phẩm xuất sắc, nhưng chúng không đúng như vậy, chúng không hoạt động tốt cùng nhau, và hỗ trợ kém.

Trải nghiệm trực tiếp của chúng tôi:

  * Việc thiết lập Azure là một mớ hỗn độn các UI, một số chồng lấn với tài khoản Microsoft, một số thì không. Ví dụ có đăng nhập Azure, đăng nhập Microsoft.com, đăng nhập Live.com, v.v. và tất cả đều đồng thời có hiệu lực.

  * Chúng tôi gặp một vấn đề bảo mật nhỏ trong quá trình thiết lập, và không tìm được cách giải quyết. Chúng tôi đã thử nhiều cách để báo cáo nó, tới nhiều đại diện Microsoft, nhưng không thành công. Chúng tôi đã báo cáo thành công cho bộ phận bảo mật của Microsoft, họ trả lời là won't fix.

  * Tài liệu thường sai hoặc lỗi thời. Ít nhất một phần trong số này là do công cụ tìm kiếm kém của Microsoft, và một phần do SEO dưới mức trung bình.
  
  * Việc thiết lập Terraform được ghi chép tốt, và hoạt động. Tuy nhiên, hỗ trợ Terraform yếu so với AWS vì Microsoft đang xây dựng các mối quan hệ kinh doanh với các nhà cung cấp để làm các ví dụ thiết lập Terraform xâu chuỗi.

Trải nghiệm của các đồng nghiệp:

  * Sau khi chúng tôi tự đánh giá mù, chúng tôi tìm kiếm trải nghiệm của đồng nghiệp. Những gì chúng tôi tìm thấy xác nhận trải nghiệm của chúng tôi.

  * Các đồng nghiệp báo cáo các vấn đề bổ sung về thời gian build, và các vấn đề với việc mang-theo-máy-chủ-build-riêng. Những vấn đề này nghiêm trọng hơn đáng kể so với các vấn đề UI, vì việc thực hiện build là mục đích cốt lõi của một pipeline build, và chúng tôi kỳ vọng thực hiện nhiều bản build mỗi ngày.

  * Chúng tôi thấy sự tham gia xuất sắc của các đồng đội Azure trong các khu vực thảo luận. Xin khen ngợi Microsoft về điều này. Chúng tôi đặc biệt ấn tượng với Edward Thomson, PM và lập trình viên Azure, vì sự tham gia, sự thẳng thắn và các giải thích kỹ thuật của anh ấy.


### Hàm ý

Việc chọn Microsoft Azure DevOps có vẻ sẽ tốn kém hơn (~3 lần) về thời gian và chi phí so với việc không chọn Azure.


## Liên quan


### Các quyết định liên quan

Nếu chúng tôi chọn Azure DevOps, có nhiều sản phẩm liên quan, bao gồm Azure Repo, Azure Pipeline, v.v. Chúng tôi tin rằng nếu chọn Azure Devops, điều này có thể giúp dùng nhiều khả năng Azure hơn dễ hơn, hoặc có thể làm cho việc dùng khả năng của các nhà cung cấp khác khó hơn.

Chúng tôi tin rằng Microsoft đang có những bước tiến lớn về trải nghiệm nhà phát triển, và chúng tôi thấy Microsoft thực hiện các thương vụ mua lại lớn các công cụ nhà phát triển (ví dụ GitHub) và các phụ thuộc (ví dụ Citus).

Nếu chúng tôi chọn Azure DevOps, chúng tôi có thể muốn nhấn mạnh việc chọn các sản phẩm do Microsoft mua lại, và chúng tôi cũng có thể muốn tiếp cận các sản phẩm được mua lại với sự thận trọng/đánh giá cao hơn do khả năng đào thải mô, ví dụ rủi ro nhân sự nghỉ việc.


### Các yêu cầu liên quan

Chúng tôi muốn thời gian build rất nhanh. Chúng tôi chấp nhận trả phí bảo hiểm cao cho điều này. Đó là vì chúng tôi muốn lặp rất nhanh.

Chúng tôi muốn độ tin cậy rất cao. Chúng tôi chấp nhận trả phí bảo hiểm cao cho điều này. Đó là vì chúng tôi đang kiểm thử các trường hợp sử dụng giá trị cao, bao gồm giao dịch tài chính, giao dịch bí mật, v.v.

4 KPI devops hàng đầu của chúng tôi bao gồm thời gian khôi phục trung bình, đòi hỏi các bản build nhanh và độ tin cậy cao.


### Các tạo phẩm liên quan

Chúng tôi muốn hệ thống build xuất ra các tạo phẩm phù hợp để dùng trong các hệ thống khác, như Artifactory.


### Các nguyên tắc liên quan

Dễ đảo ngược. Chúng tôi có thể đánh giá Azure DevOps song song với AWS đương nhiệm.


## Ghi chú


### Microsoft Devops CI: An Unsatisfying Adventure

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Bài đăng blog.

"Là một nhà phát triển phần mềm, tôi biết rõ từ trải nghiệm bản thân việc xây dựng các sản phẩm chất lượng nhanh chóng và rẻ khó đến mức nào. Đó là một loại hình nghệ thuật mà đôi khi chúng tôi làm đúng, và những lúc khác sa sút thành một thứ giống như trang web chính phủ về chăm sóc sức khỏe thời Obama. Mức độ kiểm soát của chúng tôi đối với sản phẩm cuối cùng rất khác nhau, và trách nhiệm cho thất bại thường đổ lên sai người trong hệ thống phân cấp ra quyết định. Azure DevOps của Microsoft (trước đây gọi là Visual Studio Team Services), dù rõ ràng có thiện chí, là một cơn bão hoàn hảo của các quyết định tồi và việc thực thi kém."


### Những điểm nổi bật của thảo luận trên Hacker News

https://news.ycombinator.com/item?id=18983586

"Chúng tôi dùng Azure DevOps rất nhiều ở chỗ làm của tôi và, sau khi đã dùng GitHub, Gitlab, các giải pháp tự lưu trữ, Jenkins, TeamCity... Azure DevOps xếp cuối cùng."

"UI vụng về khủng khiếp ở khắp nơi. Tệ nhất đối với tôi là các pull request. Cực kỳ khó làm việc với mọi người trên một pull request. Tôi thậm chí không thể chỉ ra "một" vấn đề cụ thể - với chúng tôi, nó hỏng ở khắp nơi."

"Azure Devops là thứ tôi muốn yêu thích. UI liên tục thay đổi, nhưng không sửa các lỗi nền tảng đã tồn tại từ lâu."

"Các công cụ không được tích hợp tốt, UI thực sự chậm, không có chế độ xem bảng điều khiển các pull request, build, bản phát hành, v.v. đang hoạt động cho các kho yêu thích của tôi. Thời gian Build/Deploy chậm đến mức điên rồ."

"Chúng tôi cũng đã thử dùng Azure Boards (Work Items, Boards, Backlogs, v.v.). Ôi. Đó là một mớ UI hỗn độn của các ý tưởng rời rạc. Thay vì triển khai một thứ thật tốt, họ triển khai hai chục thứ một cách tồi tệ."


### Windows Development MVP

Tôi là Windows Development MVP ở đây. Tôi cảm thấy mình phải gánh một phần trách nhiệm vì đã không lên tiếng mạnh hơn về những vấn đề này. Nhưng phải nói, tôi thất vọng khi nghe bạn "ngạc nhiên" về các vấn đề UX. Tôi đã nói với người của bạn rằng UX thật tệ (ví dụ từ trước cả khi ra mắt) và liên tục nghe lại "chúng tôi biết, chúng tôi đang sửa". Tôi sẽ bắt đầu chính thức hóa phản hồi và đẩy nó qua các đường ống, hãy chờ xem. Tôi cũng ở địa phương (Bellevue), rất muốn đến và thử xây dựng pipeline cho ứng dụng oss .net/wpf/uwp tương đối đơn giản của chúng tôi. Tôi nghi rằng nó sẽ mở mắt cho cả hai chúng ta.

Một số ví dụ:

* Bạn không thể xây dựng pipeline với một kho git chứa các submodule

* Tôi thấy không thể chỉnh sửa PATH cho một số công cụ tùy chỉnh

* Trải nghiệm Pipeline Mới hoàn toàn không có nhiều ý nghĩa, người dùng mới nhấp chuột lung tung cuối cùng sẽ đến nhầm Docs.


### Tóm tắt về Edward Thomson (Azure PM)

Tôi đã viết mã hợp nhất các pull request của bạn. Quản lý Chương trình tại Microsoft cho Azure DevOps; trước đây là kỹ sư phần mềm về các công cụ kiểm soát phiên bản tại GitHub, Microsoft, SourceGear.

https://www.edwardthomson.com/

Đồng bảo trì libgit2. https://libgit2.github.io

Đồng dẫn chương trình All Things Git, Podcast về Git. https://www.allthingsgit.com/

Người biên tập Developer Tools Weekly, bản tin về các công cụ phát triển. https://developertoolsweekly.com/
