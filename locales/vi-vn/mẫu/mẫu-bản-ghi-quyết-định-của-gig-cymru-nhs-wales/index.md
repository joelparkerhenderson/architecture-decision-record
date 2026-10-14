# {Tiêu đề của bạn ở đây}

!!! info

    **Trạng thái**: { Proposed | Under Review | Accepted |  Rejected | Superseded | Deprecated }
    
    **Cập nhật**: {YYYY-MM-DD}

## Tóm tắt

{Đây là 'bản tóm tắt điều hành' hoặc 'bài giới thiệu ngắn gọn' cho ADR của bạn. Trong một vài
câu súc tích (thường 2-4 câu), hãy nêu rõ vấn đề cốt lõi, câu hỏi hoặc cơ hội mà ADR này
giải quyết. Bao gồm một gợi ý ngắn về quyết định đã đưa ra hoặc lĩnh vực trọng tâm. Mục tiêu
là giúp người đọc nhanh chóng hiểu ADR này nói về điều gì và quyết định xem nó có liên quan
đến họ hay không, mà không cần đọc toàn bộ tài liệu. Hãy coi nó như phần tóm tắt của một bài
báo kỹ thuật hoặc một phần giới thiệu rất ngắn về chủ đề chính.}

## Động lực

{Phần này giải thích **tại sao** quyết định này được đưa ra **vào lúc này**. Hãy trình bày rõ ràng
các động cơ, nhu cầu hoặc vấn đề chính đòi hỏi quyết định kiến trúc này. Hãy nghĩ về những lý do
và áp lực nền tảng.}

* {ví dụ: Chúng tôi đang phát triển một tính năng/khả năng mới cần...}

* {ví dụ: Chúng tôi cần cải thiện hiệu năng, khả năng tiếp cận, loại bỏ nợ...}

* {ví dụ: Phản hồi từ người dùng cho thấy...}

* {ví dụ: Cách tiếp cận hiện tại áp đặt những hạn chế sau...}

## Các lựa chọn

{Đây là nơi bạn liệt kê các lựa chọn khác nhau mà bạn đang cân nhắc. Hãy bám sát các sự kiện
và tránh ý kiến, phần tiếp theo sẽ đề cập đến phân tích. Bao gồm mô tả súc tích, liên kết đến
tài liệu hoặc ví dụ liên quan.

Bao gồm tất cả các phương án thay thế quan trọng mà bạn đã khám phá, ngay cả khi cuối cùng
chúng không được chọn. Mục tiêu là cho người đọc một sự hiểu biết rõ ràng, không thiên vị về
từng phương án trước khi bạn đi vào đánh giá.}

### {Tiêu đề Lựa chọn 1}

{Mô tả lựa chọn, đưa ra tóm tắt, liệt kê các sự kiện, cung cấp liên kết, v.v.}

### {Tiêu đề Lựa chọn n}

...

## Phân tích các lựa chọn

{Đây là nơi bạn đánh giá có phê phán từng lựa chọn được trình bày trong phần *Các lựa chọn*.
Với mỗi lựa chọn, hãy đưa ra cái nhìn cân bằng về ưu điểm, nhược điểm và bất kỳ cân nhắc hoặc
đánh đổi liên quan nào khác. Hãy cụ thể và, nếu có thể, liên hệ các điểm của bạn trở lại *Động lực*.

Hãy cân nhắc các khía cạnh như:

* Chi phí (phát triển, vận hành, cấp phép)

* Độ phức tạp (triển khai, bảo trì, đường cong học tập)

* Rủi ro (kỹ thuật, vận hành, bảo mật)

* Sự phù hợp với các nguyên tắc kiến trúc hoặc tiêu chuẩn hiện có

* Tác động đến hiệu năng, khả năng mở rộng, tính dễ sử dụng, khả năng bảo trì,
    bảo mật, v.v.

Bao gồm bao nhiêu nhận định Ưu/Nhược/Khác tùy theo yêu cầu.
}

### {Đánh giá Lựa chọn 1}

* Ưu: {Một ưu điểm hoặc lợi ích cụ thể của lựa chọn này.}

* Nhược: {Một nhược điểm, rủi ro hoặc chi phí cụ thể gắn với lựa chọn này.}

* Khác: {Một điểm liên quan nhưng không hẳn là ưu hay nhược.}

### {Đánh giá Lựa chọn n}

...

## Khuyến nghị

{Đây là nơi bạn nêu rõ quyết định cuối cùng, và nêu tên một cách tường minh lựa chọn đã được chọn.
Giải thích chi tiết **tại sao** lựa chọn này được chọn. Bạn nên trình bày rõ ràng lựa chọn đã chọn
đáp ứng tốt nhất *Động lực* như thế nào và đáp ứng các yêu cầu chính hoặc giải quyết vấn đề đã nêu.}

### Hệ quả

{Phần này là **tùy chọn**.}

{Giờ đây khi một quyết định đã được đưa ra, các kết quả và tác động dự kiến là gì, cả tích cực
lẫn tiêu cực? Những hạn chế, chi phí hoặc rủi ro đã biết nào đang được chấp nhận khi đưa ra
quyết định này? Quyết định này sẽ ảnh hưởng thế nào đến các bên liên quan khác nhau, các hệ
thống khác, thực hành phát triển, quy trình vận hành hoặc trải nghiệm người dùng?}

* Ưu: {Một kết quả hoặc lợi ích tích cực cụ thể được kỳ vọng từ quyết định này.}

* Nhược: {Một bất lợi, chi phí hoặc rủi ro cụ thể được chấp nhận do quyết định này. }

* Khác: {Một hệ quả không hẳn là ưu hay nhược.}

### Xác nhận

{Phần này là **tùy chọn**.}

{Phác thảo cách việc triển khai quyết định này sẽ được xác minh và cách bảo đảm tuân thủ liên
tục. Điều này giúp chứng minh rằng quyết định không chỉ là lý thuyết mà sẽ được đưa vào thực
tế và giám sát chủ động.

Bạn sẽ kiểm tra rằng quyết định đã được triển khai đúng như thế nào? (ví dụ: xem xét mã, các
bài kiểm thử cụ thể, trình diễn, đánh giá chéo).

Việc tuân thủ quyết định này sẽ được duy trì theo thời gian như thế nào? (ví dụ: kiểm tra tự
động, kiểm toán định kỳ, cập nhật hướng dẫn của nhóm, đào tạo).

Có các chỉ số hoặc chỉ báo cụ thể nào cho thấy quyết định đang đạt được kết quả tích cực dự
kiến không? (ví dụ: điểm chuẩn hiệu năng, tỷ lệ áp dụng, giảm các lỗi cụ thể, điểm phản hồi
người dùng).

Ai chịu trách nhiệm giám sát điều này, và điều gì xảy ra nếu quyết định không được tuân theo?}

## Thông tin thêm

{Phần này là **tùy chọn**.}

{Sử dụng phần này để cung cấp bất kỳ thông tin bổ sung nào hỗ trợ quyết định, bổ sung bối
cảnh hoặc định hướng các hành động trong tương lai. Các liên kết đến các quyết định và tài
nguyên khác cũng có thể xuất hiện ở đây.

Bạn có thể ghi chú ngắn gọn ai đã tham gia vào quá trình ra quyết định và sự đồng thuận đã đạt
được hay không và như thế nào. Bạn cũng có thể đề xuất một khung thời gian hoặc các sự kiện cụ
thể có thể thúc đẩy việc đánh giá lại quyết định này trong tương lai.}
