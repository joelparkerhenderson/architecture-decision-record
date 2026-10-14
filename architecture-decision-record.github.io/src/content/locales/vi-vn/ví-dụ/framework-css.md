# Bản ghi quyết định kiến trúc: Framework CSS

Nội dung:

- [Tóm tắt](#tóm-tắt)
  - [Vấn đề](#vấn-đề)
  - [Quyết định](#quyết-định)
  - [Trạng thái](#trạng-thái)
- [Chi tiết](#chi-tiết)
  - [Giả định](#giả-định)
  - [Ràng buộc](#ràng-buộc)
  - [Lập trường](#lập-trường)
  - [Lập luận](#lập-luận)
  - [Hàm ý](#hàm-ý)
- [Liên quan](#liên-quan)
  - [Các quyết định liên quan](#các-quyết-định-liên-quan)
  - [Các yêu cầu liên quan](#các-yêu-cầu-liên-quan)
  - [Các tạo phẩm liên quan](#các-tạo-phẩm-liên-quan)
  - [Các nguyên tắc liên quan](#các-nguyên-tắc-liên-quan)
- [Ghi chú](#ghi-chú)


## Tóm tắt


### Vấn đề

Chúng tôi muốn dùng một framework CSS để tạo các ứng dụng web của mình:

  * Chúng tôi muốn trải nghiệm người dùng nhanh và đáng tin cậy, trên tất cả các trình duyệt và kích thước màn hình phổ biến.

  * Chúng tôi muốn lặp nhanh về thiết kế, bố cục, UI/UX, v.v.

  * Chúng tôi muốn các ứng dụng đáp ứng (responsive), đặc biệt cho các màn hình nhỏ hơn như trên thiết bị di động, màn hình lớn hơn như màn hình rộng 4K, và các màn hình động như màn hình xoay được.  


### Quyết định

Đã quyết định chọn Bulma.


### Trạng thái

Đã quyết định chọn Bulma. Mở với các lựa chọn framework CSS mới khi chúng xuất hiện.


## Chi tiết


### Giả định

Chúng tôi muốn tạo các ứng dụng web hiện đại, nhanh, đáng tin cậy, đáp ứng, v.v.

Các ứng dụng web hiện đại điển hình đang giảm/loại bỏ việc dùng jQuery vì nhiều lý do: 

  * JavaScript hiện đại đang dần đưa vào nhiều khả năng mà jQuery đã cung cấp, nên jQuery ít cần thiết hơn, và có các mô-đun tốt hơn/nhanh hơn/nhỏ hơn cung cấp các triển khai cụ thể

  * Cách tiếp cận rộng của jQuery là thao tác DOM trực tiếp, vốn là một phản mẫu đối với các framework JavaScript hiện đại (ví dụ React, Vue, Svelte)

  * jQuery tự can thiệp vào chính nó nếu được tải hai lần, v.v.


### Ràng buộc

Nếu chúng tôi chọn một framework CSS dùng jQuery, chúng tôi sẽ buộc phải nhập jQuery. Ví dụ, Semantic UI dùng jQuery, còn Tachyons thì không.

Nếu chúng tôi chọn một framework CSS tối giản, chúng tôi sẽ từ bỏ các thành phần framework mà chúng tôi có thể muốn ngay bây giờ hoặc sớm. Ví dụ, Semantic UI cung cấp băng chuyền hình ảnh, còn Tachyons thì không.


### Lập trường

Chúng tôi đã cân nhắc không dùng framework nào. Điều này vẫn có vẻ khả thi, đặc biệt vì CSS grid cung cấp phần lớn những gì chúng tôi cần cho dự án..

Chúng tôi đã cân nhắc nhiều framework CSS bằng cách phân loại nhanh danh sách rút gọn: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons, v.v. Hai lựa chọn của chúng tôi để xem xét sâu hơn là Semantic UI (vì có cách tiếp cận ngữ nghĩa nhất) và Bulma (vì có cách tiếp cận nhẹ nhất cung cấp các thành phần chúng tôi muốn ngay bây giờ).

Chúng tôi đã cân nhắc Semantic UI. Nó cung cấp nhiều thành phần, bao gồm những thành phần chúng tôi muốn cho dự án: tab, lưới, nút, v.v. Chúng tôi đã thử nghiệm với Semantic UI theo hai cách: dùng các tệp CDN điển hình, và dùng các kho NPM. Chúng tôi đã thành công với Semantic UI trong một trang HTML tĩnh, nhưng không thành công trong khung thời gian của mình để xây dựng một SPA JavaScript (chủ yếu vì các vấn đề tải jQuery). Chúng tôi phát hiện các lập trình viên khác đã yêu cầu các nhà phát triển Semantic UI tạo một phiên bản không có jQuery, vì cùng lý do như chúng tôi. Các lập trình viên khác đã yêu cầu một phiên bản không có jQuery trong nhiều năm, nhưng các nhà phát triển đã từ chối, và nói rằng bất kỳ phiên bản không có jQuery nào cũng quá khó viết, ví dụ ~"dự án Semantic UI có hơn 22.000 điểm tiếp xúc dùng jQuery".

Ví dụ với Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Chúng tôi đã cân nhắc Bulma. Bulma có nhiều khả năng tương tự Semantic UI, mặc dù không có nhiều thành phần tinh vi bằng. Bulma được xây dựng bằng các kỹ thuật hiện đại, chẳng hạn không có jQuery. Bulma có một số thành phần của bên thứ ba, một số trong đó chúng tôi có thể muốn dùng.


Ví dụ với Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Lập luận

Như trên.

Cụ thể, Semantic UI dường như có một lá cờ cảnh báo cả về công nghệ (tức là quá nhiều điểm tiếp xúc jQuery) lẫn về sự lãnh đạo (tức là không jQuery bị từ chối thẳng thừng, thay vì cố gắng lập lộ trình, hoặc cải tiến liên tục, hoặc gây quỹ quyên góp, v.v.).


### Hàm ý

Nếu chúng tôi tìm được một framework CSS tốt không dùng jQuery, điều đó nhìn chung hữu ích và tốt.


## Liên quan


### Các quyết định liên quan

Framework CSS mà chúng tôi chọn có thể ảnh hưởng đến khả năng kiểm thử.


### Các yêu cầu liên quan

Chúng tôi muốn phát hành nhanh một ứng dụng thuần hiện đại. 

Chúng tôi không muốn dành thời gian làm việc với các framework cũ hơn (đặc biệt Semantic UI) dùng các phụ thuộc cũ hơn (đặc biệt jQuery).


### Các tạo phẩm liên quan

Ảnh hưởng đến tất cả các HTML điển hình sẽ dùng CSS đó.


### Các nguyên tắc liên quan

Dễ đảo ngược.

Cần tốc độ.


## Ghi chú

Mọi ghi chú ở đây.
