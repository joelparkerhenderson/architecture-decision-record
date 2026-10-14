# Ngôn ngữ lập trình

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


## Tóm tắt


### Vấn đề

Chúng tôi cần chọn các ngôn ngữ lập trình cho phần mềm của mình. Chúng tôi có hai nhu cầu chính: một ngôn ngữ lập trình front-end phù hợp với các ứng dụng web, và một ngôn ngữ lập trình back-end phù hợp với các ứng dụng máy chủ.


### Quyết định

Chúng tôi chọn TypeScript cho front-end.

Chúng tôi chọn Rust cho back-end.


### Trạng thái

Đã quyết định. Chúng tôi mở với các phương án thay thế mới khi chúng xuất hiện.


## Chi tiết


### Giả định

Các ứng dụng front-end là điển hình:

  * Người dùng và tương tác điển hình

  * Trình duyệt và hệ thống điển hình

  * Phát triển và triển khai điển hình

Các ứng dụng front-end có khả năng phát triển nhanh:

  * Chúng tôi muốn đảm bảo phát triển, triển khai, lặp, v.v. nhanh và dễ dàng.

  * Chúng tôi coi trọng khả năng chứng minh, chẳng hạn an toàn kiểu, và chúng tôi không ngại làm thêm một chút để đạt được nó.

  * Chúng tôi không cần tương thích với hệ thống kế thừa.

Các ứng dụng back-end cao hơn mức điển hình:

  * Các mục tiêu cao hơn mức điển hình về chất lượng, đặc biệt là khả năng chứng minh, độ tin cậy, bảo mật, v.v.

  * Các mục tiêu cao hơn mức điển hình về gần-thời-gian-thực, tức là chúng tôi không muốn các khoảng dừng do thu gom rác của máy ảo.

  * Các mục tiêu cao hơn mức điển hình về lập trình hàm, đặc biệt là xử lý song song, xử lý đa nhân và an toàn bộ nhớ.

Chúng tôi chấp nhận tốc độ biên dịch thấp hơn để đổi lấy an toàn lúc biên dịch và tốc độ lúc chạy.


### Ràng buộc

Chúng tôi có một ràng buộc mạnh về các ngôn ngữ dùng được với các dịch vụ hàm của các nhà cung cấp đám mây lớn, chẳng hạn Amazon Lambda.


### Lập trường

Chúng tôi đã cân nhắc các ngôn ngữ sau:

  * C

  * C++

  * Clojure
  
  * Elixir
  
  * Erlang
  
  * Elm
  
  * Flow
  
  * Go
  
  * Haskell
  
  * Java
  
  * JavaScript
  
  * Kotlin
  
  * Python
  
  * Ruby
  
  * Rust
  
  * TypeScript



### Lập luận

Tóm tắt theo từng ngôn ngữ:

  * C: bị loại vì độ an toàn thấp; Rust có thể làm gần như mọi thứ tốt hơn.

  * C++: bị loại vì nó là một mớ hỗn độn; Rust có thể làm gần như mọi thứ tốt hơn.

  * Clojure: mô hình hóa xuất sắc; xấp xỉ Lisp tốt nhất; môi trường chạy tuyệt vời trên JVM.
  
  * Elixir: môi trường chạy xuất sắc bao gồm khả năng triển khai và đồng thời; trải nghiệm nhà phát triển xuất sắc; hệ sinh thái tương đối nhỏ.

  * Erlang: môi trường chạy xuất sắc bao gồm khả năng triển khai và đồng thời; trải nghiệm nhà phát triển đầy thách thức; hệ sinh thái tương đối nhỏ.

  * Elm: trông rất hứa hẹn; IBM đang công bố các nghiên cứu điển hình lớn với kết quả tốt; hệ sinh thái nhỏ hơn.

  * Flow: một cải tiến thú vị so với JavaScript; tuy nhiên, các nhà phát triển đang rời bỏ nó.

  * Go: trải nghiệm nhà phát triển xuất sắc; đồng thời xuất sắc; nhưng có tiền sử các quyết định tồi làm tê liệt ngôn ngữ.

  * Haskell: ngôn ngữ hàm tốt nhất; cộng đồng nhà phát triển nhỏ hơn; chưa đạt đủ thành công sản xuất đã được công bố.

  * Java: môi trường chạy xuất sắc; hệ sinh thái xuất sắc; trải nghiệm nhà phát triển dưới mức trung bình.

  * JavaScript: ngôn ngữ phổ biến nhất từ trước đến nay; hệ sinh thái rộng khắp nhất.

  * Kotlin: sửa rất nhiều điểm của Java; được JetBrains hậu thuẫn xuất sắc; có các trường hợp được công bố tốt về việc chuyển từ Java sang Kotlin.
  
  * Python: ngôn ngữ phổ biến nhất cho quản trị hệ thống; công cụ phân tích tuyệt vời; các framework web tốt; nhưng bị Google bỏ để chuyển sang Go.

  * Ruby: trải nghiệm nhà phát triển tốt nhất từ trước đến nay; các framework web tốt nhất; cộng đồng dễ mến nhất; nhưng rất chậm; hơi khó đóng gói.

  * Rust: ngôn ngữ mới tốt nhất; nhấn mạnh trừu tượng bằng không; nhấn mạnh đồng thời; tuy nhiên hệ sinh thái tương đối nhỏ; và có các giới hạn cố ý đối với một số loại tăng tốc của trình biên dịch, ví dụ truy cập bộ nhớ trực tiếp phải được đánh dấu tường minh là không an toàn.

  * TypeScript: thêm kiểu vào JavaScript; trình chuyển mã tuyệt vời; sự nhấn mạnh ngày càng tăng của các nhà phát triển vào việc chuyển từ JavaScript sang TypeScript; được Microsoft hậu thuẫn mạnh mẽ.

Chúng tôi quyết định rằng các máy ảo có một loạt đánh đổi mà chúng tôi chưa cần lúc này, chẳng hạn độ phức tạp bổ sung cung cấp các khả năng lúc chạy.

Chúng tôi tin rằng quyết định cốt lõi của mình được thúc đẩy bởi hai mối quan tâm xuyên suốt:

  * Để có tốc độ chạy nhanh nhất và truy cập hệ thống chặt chẽ nhất, chúng tôi sẽ chọn JavaScript và C.

  * Để có tốc độ chạy gần nhanh nhất và truy cập hệ thống gần chặt chẽ nhất, chúng tôi chọn TypeScript và Rust.

Lời khen ngợi dành cho các ngôn ngữ máy ảo và các framework web mà chúng tôi sẽ chọn nếu muốn một ngôn ngữ máy ảo:

  * Clojure và Luminus

  * Java và Spring

  * Elixir và Phoenix


### Hàm ý

Các nhà phát triển front-end sẽ cần học TypeScript. Đây có thể là đường cong học tập dễ nếu kinh nghiệm chính của nhà phát triển là dùng JavaScript.

Các nhà phát triển back-end sẽ cần học Rust. Đây có thể là đường cong học tập trung bình nếu kinh nghiệm chính của nhà phát triển là dùng C/C++, và là đường cong học tập khó nếu kinh nghiệm chính của nhà phát triển là dùng Java, Python, Ruby hoặc các ngôn ngữ quản lý bộ nhớ tương tự. 

TypeScript và Rust đều tương đối mới. Điều này có nghĩa là nhiều công cụ chưa có tài liệu cho các ngôn ngữ này. Ví dụ, pipeline devops sẽ cần được thiết lập cho các ngôn ngữ này, và cho đến nay, không công cụ devops nào mà chúng tôi đang đánh giá có các ví dụ mặc định cho các ngôn ngữ này.

Thời gian biên dịch của TypeScript và Rust khá chậm. Một phần điều này có thể do các ngôn ngữ còn mới. Chúng tôi có thể muốn xem xét cách giảm thiểu thời gian biên dịch chậm, chẳng hạn biên dịch theo yêu cầu, biên dịch đồng thời, v.v.

Hỗ trợ IDE cho các ngôn ngữ này chưa phổ biến và chưa hạng nhất. Ví dụ, JetBrains bán IDE PyCharm với hỗ trợ hạng nhất cho Python, nhưng không bán IDE có hỗ trợ hạng nhất cho Rust; thay vào đó, JetBrains có thể dùng một plugin Rust cung cấp có lẽ 80% hỗ trợ ngôn ngữ Rust so với hỗ trợ ngôn ngữ Python.


## Liên quan


### Các quyết định liên quan

Chúng tôi sẽ hướng tới các lựa chọn hệ sinh thái phù hợp với các ngôn ngữ này.

Ví dụ, chúng tôi muốn chọn một IDE có khả năng tốt cho các ngôn ngữ này.

Ví dụ, đối với framework web front-end của chúng tôi, chúng tôi nhiều khả năng sẽ quyết định chọn một framework có xu hướng hướng tới TypeScript (ví dụ Vue) hơn là một framework có xu hướng hướng tới JavaScript thuần (ví dụ React).


### Các yêu cầu liên quan

Toàn bộ chuỗi công cụ của chúng tôi phải hỗ trợ các ngôn ngữ này.


### Các tạo phẩm liên quan

Chúng tôi kỳ vọng có thể xuất một số bí mật ra các biến môi trường.


### Các nguyên tắc liên quan

Đo hai lần, xây một lần. Chúng tôi ưu tiên một chút an toàn hơn một chút tốc độ.

Thời gian chạy có giá trị hơn thời gian biên dịch. Chúng tôi ưu tiên việc sử dụng của khách hàng hơn việc sử dụng của nhà phát triển.


## Ghi chú

Mọi ghi chú ở đây.
