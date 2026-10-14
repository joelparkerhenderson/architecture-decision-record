# [000] Tiêu đề
*Gán cho mỗi ADR một số để dễ tham chiếu và lập danh mục* \
*LƯU Ý: Tất cả văn bản in nghiêng chỉ là gợi ý và nên được xóa khi dùng chính thức*

## Trạng thái - DRAFT / ACTIVE /  DEPRECATED by [000] / SUPERSEDES [000]

## Bối cảnh
*Mô tả ngắn gọn (các) vấn đề mà ADR này nhằm giải quyết, và vì sao các vấn đề đó tồn tại.*

## Phương pháp đã quyết định
*Trình bày chi tiết quyết định quan trọng về mặt kiến trúc đã/sẽ được đưa ra và mô tả cách nó giải quyết các vấn đề nêu trong phần Bối cảnh.*

## Hệ quả
*Tác động của quyết định này đối với các đặc tính kiến trúc và yêu cầu chức năng của hệ thống là gì?*

## Quản trị
*Kết quả của quyết định này sẽ được giám sát như thế nào?* \
*Việc tuân thủ quyết định này sẽ được bảo đảm như thế nào?*

## Phân tích các lựa chọn
*Nếu áp dụng, hãy đưa vào hoặc liên kết tới bất kỳ phân tích đánh đổi nào đã được thực hiện để đi đến quyết định trong tài liệu này.*

### Chú giải
*Tùy chọn: Cung cấp các công cụ trực quan cho các bên liên quan giúp nhanh chóng nhận ra các đánh đổi tích cực và tiêu cực - ví dụ các màu đèn giao thông đơn giản với tiền tố tích cực hoặc tiêu cực.*

Nền <span style="background-color:#4bce97; color:black;">xanh lá</span> cho biết mức độ phù hợp tốt, giảm dần qua <span style="background-color:#f1c232; color:black;">hổ phách</span>, với <span style="background-color:#e06666; color:black;">đỏ</span> là mức phù hợp kém nhất. \
\+ cho biết nhận xét có tác động tích cực \
\- cho biết nhận xét có tác động tiêu cực

### Tổng quan cấp cao
*Mỗi lựa chọn phù hợp với bối cảnh vấn đề đến mức nào, nhìn thoáng qua?*

<table>
  <thead>
    <tr>
      <th>Tóm tắt</th>
      <th>Lựa chọn 1</th>
      <th>Lựa chọn 2</th>
      <th>Lựa chọn 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Mức độ dễ triển khai</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Cực kỳ dễ
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Khó nhằn
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Triển khai lớn đòi hỏi kiến thức chuyên gia
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Khung thời gian</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Rất nhanh
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Khá chậm
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Rất chậm
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Giá trị chiến lược</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Không có giá trị chiến lược, thuần túy chiến thuật
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Cải thiện đôi chút trải nghiệm tiếp nhận khách hàng
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Lý tưởng cho vụ sáp nhập sắp tới
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Yêu cầu chức năng
*Mỗi lựa chọn tiềm năng phù hợp với các yêu cầu chức năng mong muốn đến mức nào?*

<table>
  <thead>
    <tr>
      <th>Kịch bản</th>
      <th><i>Lựa chọn 1</i></th>
      <th><i>Lựa chọn 2</i></th>
      <th><i>Lựa chọn 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Kịch bản 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Kịch bản 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Kịch bản 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Tùy chọn: Thêm hàng / bảng khác để bao quát các kịch bản tương lai đã biết.*

### Yêu cầu phi chức năng
*Mỗi lựa chọn tiềm năng phù hợp với các đặc tính kiến trúc mong muốn đến mức nào?
Lưu ý: ‘Đặc tính kiến trúc’ sẽ là tiêu đề phù hợp hơn, nhưng hãy điều chỉnh theo ngôn ngữ quen thuộc với lĩnh vực kinh doanh của bạn.*

<table>
  <thead>
    <tr>
      <th>Đặc tính </br> kiến trúc</th>
      <th><i>Lựa chọn 1</i></th>
      <th><i>Lựa chọn 2</i></th>
      <th><i>Lựa chọn 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Khả năng mở rộng</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Hiệu năng</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Tính sẵn sàng</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Tùy chọn: Thêm hoặc liên kết tới định nghĩa các đặc tính kiến trúc liên quan đến doanh nghiệp / sản phẩm của bạn.*
