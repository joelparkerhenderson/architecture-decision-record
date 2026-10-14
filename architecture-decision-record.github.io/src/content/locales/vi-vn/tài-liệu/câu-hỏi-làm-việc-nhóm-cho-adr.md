### Ai có thể tạo một ADR?

Hãy cân nhắc các lĩnh vực như những người cụ thể, hoặc vai trò cụ thể, hoặc nhóm cụ thể, hoặc phòng ban cụ thể; đồng thời cân nhắc xem có người, vai trò, nhóm hay phòng ban nào có thể đặt hàng một ADR hay không, nghĩa là họ yêu cầu một ADR mà người khác sẽ viết. 

Câu trả lời ví dụ: Bất kỳ ai trong tổ chức của chúng tôi đã đọc trang README về bản ghi quyết định kiến trúc đều có thể đề xuất một ADR, nghĩa là người đó có thể bắt đầu viết nó và chia sẻ với nhóm.

### Điều gì biện minh cho việc nêu ra một ADR?

Hãy cân nhắc các lĩnh vực như cách làm việc của nhóm trong tổ chức, cấu trúc hệ thống phần mềm của bạn, phối hợp giữa các nhóm, khả năng bảo trì dài hạn, các giao diện bên ngoài, bạn muốn ai được hưởng lợi, và những thứ tương tự. 

Câu trả lời ví dụ: Chúng tôi muốn tạo một ADR khi chúng tôi muốn các nhà phát triển trong tương lai hiểu "tại sao" của những gì chúng tôi đang làm.

### Điều gì biện minh cho việc không nêu ra một ADR?

Hãy cân nhắc các lĩnh vực như các quyết định không liên quan đến kiến trúc, hoặc nhỏ nhặt như rủi ro tối thiểu hoặc khép kín hoặc chỉ liên quan một nhà phát triển, hoặc đã được bao quát đầy đủ ở nơi khác như bởi các tiêu chuẩn hoặc chính sách hoặc tài liệu, hoặc mang tính tạm thời như các giải pháp tạm, bằng chứng khái niệm hoặc thử nghiệm. 

Câu trả lời ví dụ: Chúng tôi muốn bỏ qua ADR khi một quyết định bị giới hạn về phạm vi, thời gian, rủi ro và chi phí, hoặc đã được bao quát ở nơi khác.

### Vòng đời của một ADR là gì?

Hãy cân nhắc các lĩnh vực như quy trình tạo, quy trình nghiên cứu, quy trình ra quyết định, quy trình triển khai và quy trình ngừng sử dụng. Hãy cân nhắc cách theo dõi vòng đời ADR theo thời gian, chẳng hạn cách chuyển ADR từ trạng thái này sang trạng thái tiếp theo, và cũng cách thông báo điều này cho các bên liên quan. 

Câu trả lời ví dụ: Chúng tôi muốn một ADR có năm giai đoạn vòng đời: Khởi xướng (Initiating) → Nghiên cứu (Researching) → Đánh giá (Evaluating) → Triển khai (Implementing) → Duy trì (Maintaining) → Ngừng sử dụng (Sunsetting).

### Tiêu chí cho các bước vòng đời của một ADR là gì?

Hãy cân nhắc các lĩnh vực như tiêu chí chấp nhận cho một ADR, nghĩa là làm sao bạn biết nó đủ tốt để chuyển từ bước vòng đời này sang bước tiếp theo? Vấn đề đã được trình bày rõ ràng chưa? Các phương án thay thế đã được xem xét chưa? Các đánh đổi đã được hiểu và lập tài liệu đủ rõ chưa?
Mọi bối cảnh liên quan đã đầy đủ chưa? Mọi bên liên quan có tham gia chưa? Mọi phản hồi đã được tiếp thu chưa? 

Câu trả lời ví dụ: Chúng tôi muốn một ADR được các bên liên quan bỏ phiếu khi nhóm đang thực hiện đã 1) hoàn thành nghiên cứu, 2) hoàn thành đánh giá, 3) công bố đề xuất ADR cho các bên liên quan kèm yêu cầu góp ý và khung thời gian một tuần, 4) mọi nhận xét của các bên liên quan đã được tiếp thu và xử lý.

### Những vai trò và trách nhiệm nào tương tác với một ADR?

Hãy cân nhắc các vai trò như người đề xuất, người nghiên cứu, người đánh giá, người xem xét, người phê duyệt, người bảo trì, và những vai trò tương tự. Hãy cân nhắc các trách nhiệm như giao tiếp với các bên liên quan, đảm bảo kỳ vọng được đáp ứng, chia sẻ trên trang web hoặc mạng nội bộ, và xem xét công việc định kỳ và đặc biệt khi có những thay đổi liên quan.

Câu trả lời ví dụ: Chúng tôi muốn mỗi ADR luôn có một người liên hệ chính, một người liên hệ phụ và một nhóm chịu trách nhiệm; những người này chịu trách nhiệm về giao tiếp, công bố, bảo trì, xem xét định kỳ ít nhất mỗi năm một lần, và việc ngừng sử dụng cuối cùng khi cần.

### Quản trị tương tác với một ADR như thế nào?

Hãy cân nhắc các lĩnh vực như cách làm việc của tổ chức bạn, bất kỳ nhu cầu tuân thủ đặc biệt nào như về khía cạnh pháp lý hoặc nhân sự, bạn muốn xử lý đồng thuận so với xung đột so với leo thang như thế nào. Có lĩnh vực, người hay nhóm nào có thể có ảnh hưởng lớn hơn những người khác đối với một ADR, chẳng hạn có thể phê duyệt nó, hoặc bỏ phiếu cho nó, hoặc phủ quyết nó không?

Câu trả lời ví dụ: Quản trị của một ADR theo thứ tự ưu tiên này: CEO, CTO, CLO, nhóm triển khai ADR, các chuyên gia trong nhóm hiểu biết nhất về ADD. Không ai khác có quyền quản trị trừ khi được mô tả trong ADR. 

### Những nguyên tắc nào tương tác với một ADR?

Hãy cân nhắc các lĩnh vực như cách làm việc của tổ chức bạn bao gồm di chuyển nhanh so với di chuyển chậm, đồng thuận quyết định so với xung đột quyết định, và ưu tiên rủi ro so với ưu tiên an toàn, thảo luận công khai so với thảo luận riêng tư, và những thứ tương tự.

Câu trả lời ví dụ: Chúng tôi dùng các nguyên tắc lãnh đạo là thiên về hành động, bất đồng-và-cam kết (disagree-and-commit), ước tính 70% là đủ tốt cho các quyết định dễ đảo ngược và dễ cô lập, và cách làm việc công khai ngoại trừ thông tin bí mật như mô tả trong thỏa thuận bảo mật của tổ chức chúng tôi.
