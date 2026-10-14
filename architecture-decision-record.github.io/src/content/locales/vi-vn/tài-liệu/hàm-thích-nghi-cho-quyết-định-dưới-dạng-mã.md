# Hàm thích nghi cho quyết định dưới dạng mã

Hàm thích nghi (fitness function) là các kiểm tra tự động khách quan, được viết bằng mã lập trình, xác minh rằng các quyết định đang được duy trì.

- Hàm thích nghi giúp quyết định có thể kiểm thử và bảo đảm được.

- Hàm thích nghi cho quyết định có thể hỗ trợ rất nhiều cho đảm bảo chất lượng, các quy trình quản lý quy định và mục tiêu quản trị.

## Hàm thích nghi liên hệ với quyết định như thế nào

Bản ghi quyết định ghi lại quyết định, còn hàm thích nghi bảo đảm quyết định đó.

- Quyết định ví dụ: Chúng tôi dùng event sourcing để đáp ứng yêu cầu kiểm toán.

- Hàm thích nghi ví dụ: Chúng tôi dùng máy chủ tích hợp liên tục để kiểm thử rằng mọi thay đổi trạng thái đều phải tạo ra sự kiện.

## Vì sao hàm thích nghi giúp ích cho quyết định

Đo lường khách quan: Hàm thích nghi hoặc đạt hoặc không đạt, nên công việc được hiển thị và rõ ràng.

Sử dụng liên tục: Hàm thích nghi là các quy tắc sống của bạn, chạy trên mọi commit và bản build.

Tự tin để tái cấu trúc: Hàm thích nghi tự động phát hiện lỗi vi phạm quy tắc quyết định.

Quản trị có thể mở rộng: Hàm thích nghi bảo đảm các tiêu chuẩn mà không tạo ra nút thắt cổ chai.

## Hàm thích nghi có thể dùng AI không?

Hàm thích nghi có thể tận dụng các LLM AI cho quyết định bằng cách đặt câu hỏi về công việc của bạn,
chẳng hạn như kế hoạch, mã, lược đồ, API, và nhiều thứ khác:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Kiểm thử đơn vị kiến trúc

[ArchUnit](https://www.archunit.org/): kiểm tra các quy tắc kiến trúc của mã Java bằng bất kỳ framework kiểm thử đơn vị Java thông thường nào.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): kiểm tra các quy tắc kiến trúc của mã TypeScript và mã JavaScript bằng Jest, Vitest, Jasmine, v.v.
