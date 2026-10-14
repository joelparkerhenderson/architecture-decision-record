# Bản ghi quyết định kiến trúc (ADR)

Bản ghi quyết định kiến trúc (ADR) là tài liệu ghi lại một quyết định kiến trúc quan trọng đã được đưa ra, cùng với bối cảnh và hệ quả của nó.

> [!IMPORTANT]
> Hãy tự thẩm định kỹ các tài nguyên này trước khi dùng chúng trong bất kỳ hệ thống quan trọng nào.

Mục lục:

- [Bản ghi quyết định kiến trúc là gì?](#bản-ghi-quyết-định-kiến-trúc-là-gì)
- [Cách bắt đầu sử dụng ADR](#cách-bắt-đầu-sử-dụng-adr)
- [Cách bắt đầu sử dụng ADR với công cụ](#cách-bắt-đầu-sử-dụng-adr-với-công-cụ)
- [Cách bắt đầu sử dụng ADR với git](#cách-bắt-đầu-sử-dụng-adr-với-git)
- [Kỹ năng Claude Code cho ADR](#kỹ-năng-claude-code-cho-adr)
- [Quy ước đặt tên tệp](#quy-ước-đặt-tên-tệp)
- [Gợi ý viết ADR tốt](#gợi-ý-viết-adr-tốt)
- [Các mẫu ADR ví dụ](#các-mẫu-adr-ví-dụ)
- [Lời khuyên làm việc nhóm cho ADR](#lời-khuyên-làm-việc-nhóm-cho-adr)
- [Câu hỏi về làm việc nhóm cho ADR](#câu-hỏi-về-làm-việc-nhóm-cho-adr)
- [Các khái niệm bước tiếp theo cho ADR](#các-khái-niệm-bước-tiếp-theo-cho-adr)
- [Sơ đồ, góc nhìn và quan điểm kiến trúc](#sơ-đồ-góc-nhìn-và-quan-điểm-kiến-trúc)
- [Hàm thích nghi cho quyết định dưới dạng mã](#hàm-thích-nghi-cho-quyết-định-dưới-dạng-mã)
- [Rào chắn quyết định cho pull request](#rào-chắn-quyết-định-cho-pull-request)
- [Thông tin thêm](#thông-tin-thêm)

Mẫu:

- [Mẫu bản ghi quyết định của Jeff Tyree và Art Akerman](mẫu/mẫu-bản-ghi-quyết-định-của-jeff-tyree-và-art-akerman/)
- [Mẫu bản ghi quyết định của Michael Nygard](mẫu/mẫu-bản-ghi-quyết-định-của-michael-nygard/)
- [Mẫu bản ghi quyết định của EdgeX](mẫu/mẫu-bản-ghi-quyết-định-của-edgex/)
- [Mẫu bản ghi quyết định của arc42](mẫu/mẫu-bản-ghi-quyết-định-của-arc42/)
- [Mẫu bản ghi quyết định cho mẫu hình Alexandrian](mẫu/mẫu-bản-ghi-quyết-định-cho-mẫu-hình-alexandrian/)
- [Mẫu bản ghi quyết định cho trường hợp kinh doanh](mẫu/mẫu-bản-ghi-quyết-định-cho-trường-hợp-kinh-doanh/)
- [Mẫu bản ghi quyết định của dự án MADR](mẫu/mẫu-bản-ghi-quyết-định-của-dự-án-madr/)
- [Mẫu bản ghi quyết định sử dụng Planguage](mẫu/mẫu-bản-ghi-quyết-định-sử-dụng-planguage/)
- [Mẫu bản ghi quyết định của Paulo Merson](https://github.com/pmerson/ADR-template)
- [Mẫu bản ghi quyết định của Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Mẫu bản ghi quyết định của Gareth Morgan](mẫu/mẫu-bản-ghi-quyết-định-của-gareth-morgan/)
- [Mẫu bản ghi quyết định của GIG Cymru NHS Wales](mẫu/mẫu-bản-ghi-quyết-định-của-gig-cymru-nhs-wales/)
- [Mẫu bản ghi quyết định cho các Quyết định Kỹ thuật Quan trọng (ITD) của Ignacio Larrañaga](mẫu/mẫu-bản-ghi-quyết-định-cho-các-quyết-định-kỹ-thuật-quan-trọng/)

Ví dụ:

- [Framework CSS](ví-dụ/framework-css/)
- [Cấu hình biến môi trường](ví-dụ/cấu-hình-biến-môi-trường/)
- [Chỉ số, giám sát, cảnh báo](ví-dụ/chỉ-số-giám-sát-cảnh-báo/)
- [Microsoft Azure DevOps](ví-dụ/microsoft-azure-devops/)
- [Monorepo so với multirepo](ví-dụ/monorepo-so-với-multirepo/)
- [Ngôn ngữ lập trình](ví-dụ/ngôn-ngữ-lập-trình/)
- [Lưu trữ bí mật](ví-dụ/lưu-trữ-bí-mật/)
- [Định dạng dấu thời gian](ví-dụ/định-dạng-dấu-thời-gian/)
- [Còn nhiều nữa...](ví-dụ/)

## Bản ghi quyết định kiến trúc là gì?

Một **bản ghi quyết định kiến trúc** (architecture decision record, ADR) là một tài liệu ghi lại một quyết định kiến trúc quan trọng đã đưa ra cùng với bối cảnh và hệ quả của nó.

Một **quyết định kiến trúc** (architecture decision, AD) là một lựa chọn thiết kế phần mềm giải quyết một yêu cầu quan trọng.

Một **nhật ký quyết định kiến trúc** (architecture decision log, ADL) là tập hợp tất cả các ADR được tạo ra và duy trì cho một dự án (hoặc tổ chức) cụ thể.

Một **yêu cầu quan trọng về mặt kiến trúc** (architecturally-significant requirement, ASR) là một yêu cầu có ảnh hưởng đo lường được đến kiến trúc của một hệ thống phần mềm.

Tất cả những điều này nằm trong chủ đề **quản lý tri thức kiến trúc** (architecture knowledge management, AKM).

Mục tiêu của tài liệu này là cung cấp một cái nhìn tổng quan nhanh về ADR, cách tạo chúng và nơi tìm thêm thông tin.

Các từ viết tắt:

  * **AD**: quyết định kiến trúc

  * **ADL**: nhật ký quyết định kiến trúc

  * **ADR**: bản ghi quyết định kiến trúc

  * **AKM**: quản lý tri thức kiến trúc

  * **ASR**: yêu cầu quan trọng về mặt kiến trúc

## Cách bắt đầu sử dụng ADR

Để bắt đầu sử dụng ADR, hãy trao đổi với đồng đội của bạn về các lĩnh vực sau.

Xác định quyết định:

  * AD này khẩn cấp và quan trọng đến mức nào?

  * Nó phải được đưa ra ngay bây giờ, hay có thể chờ đến khi biết nhiều hơn?

  * Cả kinh nghiệm cá nhân lẫn tập thể, cũng như các phương pháp và thực hành thiết kế được công nhận, đều có thể hỗ trợ việc xác định quyết định.

  * Lý tưởng là duy trì một danh sách việc cần làm về quyết định bổ sung cho danh sách việc cần làm của sản phẩm.

Ra quyết định:

  * Có nhiều kỹ thuật ra quyết định, cả kỹ thuật chung lẫn kỹ thuật dành riêng cho kiến trúc phần mềm, ví dụ như dialogue mapping.

  * Ra quyết định theo nhóm là một chủ đề nghiên cứu đang sôi động.

Ban hành và thực thi quyết định:

  * AD được dùng trong thiết kế phần mềm; do đó chúng phải được truyền đạt tới, và được chấp nhận bởi, các bên liên quan của hệ thống, những người tài trợ, phát triển và vận hành nó.

  * Phong cách viết mã thể hiện rõ kiến trúc và việc xem xét mã tập trung vào các mối quan tâm và quyết định kiến trúc là hai thực hành liên quan.

  * AD cũng phải được (xem xét lại) khi hiện đại hóa một hệ thống phần mềm trong quá trình tiến hóa phần mềm.

Chia sẻ quyết định (tùy chọn):

  * Nhiều AD lặp lại giữa các dự án.

  * Do đó, kinh nghiệm với các quyết định trong quá khứ, cả tốt lẫn xấu, có thể là tài sản có thể tái sử dụng quý giá khi áp dụng chiến lược quản lý tri thức tường minh.

Lập tài liệu quyết định:

  * Có nhiều mẫu và công cụ để ghi lại quyết định.

  * Xem các cộng đồng agile, ví dụ ADR của M. Nygard.

  * Xem các quy trình kỹ thuật phần mềm và thiết kế kiến trúc truyền thống, ví dụ bố cục bảng do IBM UMF và Tyree và Akerman của CapitalOne đề xuất.

Xem thêm:

  * Các bước trên được lấy từ mục Wikipedia về [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Cách bắt đầu sử dụng ADR với công cụ

- [MySpec](https://myspec.dev) — Nền tảng đặc tả và quyết định kiến trúc tự động, cấu trúc hóa hiến chương dự án, kiến trúc kỹ thuật và ADR thành Markdown sạch, cung cấp qua MCP.

Bạn có thể bắt đầu sử dụng ADR với các công cụ theo bất kỳ cách nào bạn muốn.

Ví dụ:

  * Nếu bạn thích dùng Google Drive và chỉnh sửa trực tuyến, bạn có thể tạo một Google Doc hoặc Google Sheet.

  * Nếu bạn thích dùng kiểm soát phiên bản mã nguồn, chẳng hạn git, bạn có thể tạo một tệp cho mỗi ADR.

  * Nếu bạn thích dùng các công cụ lập kế hoạch dự án, chẳng hạn Atlassian Jira, bạn có thể dùng công cụ theo dõi kế hoạch của công cụ đó.

  * Nếu bạn thích dùng wiki, chẳng hạn MediaWiki, bạn có thể tạo một wiki ADR.

## Cách bắt đầu sử dụng ADR với git

Nếu bạn thích dùng kiểm soát phiên bản git, đây là cách chúng tôi thích bắt đầu sử dụng ADR với git cho một dự án phần mềm điển hình có mã nguồn.

Tạo một thư mục cho các tệp ADR:

```sh
$ mkdir adr
```

Với mỗi ADR, tạo một tệp văn bản, chẳng hạn `database.txt`:

```sh
$ vi database.txt
```

Viết bất cứ điều gì bạn muốn vào ADR. Xem các mẫu trong kho lưu trữ này để lấy ý tưởng.

Commit ADR vào kho git của bạn.

## Kỹ năng Claude Code cho ADR

Kho mã này cung cấp hai kỹ năng (skill) [Claude Code](https://claude.com/claude-code) trong [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), để một tác tử lập trình AI có thể viết và duy trì ADR theo cách dự án này khuyến nghị:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — dùng chung, cho bất kỳ ai viết ADR trong bất kỳ dự án nào. Giúp quyết định xem một quyết định có cần ADR không, tạo thư mục `adr/` hoặc `decisions/`, đặt tên tệp, chọn một mẫu trong mười một bộ khung đi kèm và viết các phần Bối cảnh/Quyết định/Hệ quả chắc chắn.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — dành riêng cho người duy trì kho mã này. Ghi lại cách bố trí kho, quy ước phản chiếu README và locales, cùng các bước chính xác để thêm mẫu, ví dụ hoặc liên kết công cụ mới.

Để dùng một kỹ năng, hãy sao chép thư mục của nó vào `.claude/skills/` ở gốc kho mã bạn đang làm việc (hoặc vào `~/.claude/skills/` để dùng ở mọi dự án), rồi nhờ Claude Code viết hoặc xem xét một ADR.

## Quy ước đặt tên tệp

Nếu bạn chọn tạo các ADR bằng các tệp văn bản thông thường, bạn có thể muốn đưa ra quy ước đặt tên tệp ADR của riêng mình.

Chúng tôi thích sử dụng quy ước đặt tên tệp có định dạng cụ thể.

Ví dụ:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Quy ước đặt tên tệp của chúng tôi:

  * Tên có một cụm động từ mệnh lệnh ở thì hiện tại. Điều này giúp dễ đọc và khớp với định dạng thông điệp commit của chúng tôi.

  * Tên dùng chữ thường và dấu gạch ngang (giống kho lưu trữ này). Đây là sự cân bằng giữa khả năng đọc và tính tiện dụng của hệ thống.

  * Phần mở rộng là markdown. Điều này hữu ích để định dạng dễ dàng.

## Gợi ý viết ADR tốt

Đặc điểm của một ADR tốt:

* Lý do: Giải thích lý do thực hiện AD cụ thể đó. Điều này có thể bao gồm bối cảnh (xem bên dưới), ưu và nhược điểm của các lựa chọn tiềm năng khác nhau, so sánh tính năng, thảo luận chi phí/lợi ích, và nhiều hơn nữa.

* Cụ thể: Mỗi ADR nên nói về một AD, không phải nhiều AD.

* Dấu thời gian: Xác định thời điểm mỗi mục trong ADR được viết. Điều này đặc biệt quan trọng đối với các khía cạnh có thể thay đổi theo thời gian, như chi phí, lịch trình, mở rộng quy mô và những thứ tương tự.

* Bất biến: Đừng thay đổi thông tin hiện có trong ADR. Thay vào đó, hãy sửa đổi ADR bằng cách thêm thông tin mới, hoặc thay thế ADR bằng cách tạo một ADR mới.

Đặc điểm của một phần "Bối cảnh" tốt trong ADR:

* Giải thích tình hình của tổ chức bạn và các ưu tiên kinh doanh.

* Bao gồm lý do và các cân nhắc dựa trên cấu thành xã hội và kỹ năng của các nhóm của bạn.

* Bao gồm các ưu và nhược điểm liên quan, và mô tả chúng theo cách phù hợp với nhu cầu và mục tiêu của bạn.

Đặc điểm của một phần "Hệ quả" tốt trong ADR:

* Giải thích điều gì xảy ra sau khi đưa ra quyết định. Điều này có thể bao gồm các tác động, kết quả, đầu ra, việc theo dõi tiếp, và nhiều hơn nữa.

* Bao gồm thông tin về bất kỳ ADR tiếp theo nào. Khá phổ biến khi một ADR kích hoạt nhu cầu về thêm các ADR, chẳng hạn khi một ADR đưa ra một lựa chọn lớn bao trùm, từ đó tạo ra nhu cầu về nhiều quyết định nhỏ hơn.

* Bao gồm bất kỳ quy trình xem xét sau hành động nào. Thông thường các nhóm xem xét từng ADR một tháng sau, để so sánh thông tin ADR với những gì đã xảy ra trong thực tế, nhằm học hỏi và phát triển.

Một ADR mới có thể thay thế một ADR trước đó:

* Khi một AD được đưa ra thay thế hoặc làm mất hiệu lực một ADR trước đó, thì nên tạo một ADR mới

## Các mẫu ADR ví dụ

Các mẫu ADR ví dụ mà chúng tôi đã thu thập trên mạng:

- [Mẫu ADR của Michael Nygard](mẫu/mẫu-bản-ghi-quyết-định-của-michael-nygard/) (đơn giản và phổ biến)

- [Mẫu ADR của Jeff Tyree và Art Akerman](mẫu/mẫu-bản-ghi-quyết-định-của-jeff-tyree-và-art-akerman/) (tinh vi hơn)

- [Mẫu ADR cho mẫu hình Alexandrian](mẫu/mẫu-bản-ghi-quyết-định-cho-mẫu-hình-alexandrian/) (đơn giản, kèm chi tiết bối cảnh)

- [Mẫu ADR cho tình huống kinh doanh](mẫu/mẫu-bản-ghi-quyết-định-cho-trường-hợp-kinh-doanh/) (thiên về MBA hơn, có chi phí, SWOT và nhiều ý kiến hơn)

- [Mẫu ADR của dự án Markdown Any Decision Records (MADR)](mẫu/mẫu-bản-ghi-quyết-định-của-dự-án-madr/) (có cả bản đơn giản và bản chi tiết; bản sau nhấn mạnh các lựa chọn cùng ưu nhược điểm của chúng)

- [Mẫu ADR dùng Planguage](mẫu/mẫu-bản-ghi-quyết-định-sử-dụng-planguage/) (thiên về đảm bảo chất lượng hơn)

- [Mẫu cho các Quyết định Kỹ thuật Quan trọng (ITD) của Ignacio Larrañaga](mẫu/mẫu-bản-ghi-quyết-định-cho-các-quyết-định-kỹ-thuật-quan-trọng/) (gọn nhẹ và đặt quyết định lên trước, tối ưu cho việc lãnh đạo xem xét nhanh)

## Lời khuyên làm việc nhóm cho ADR

Nếu bạn đang cân nhắc sử dụng các bản ghi quyết định với nhóm của mình, đây là một số lời khuyên mà chúng tôi đã học được khi làm việc với nhiều nhóm.

Bạn có cơ hội dẫn dắt đồng đội bằng cách cùng nhau trao đổi về "tại sao", thay vì áp đặt "cái gì". Ví dụ, các bản ghi quyết định là một cách để các nhóm suy nghĩ thông minh hơn và giao tiếp tốt hơn; các bản ghi quyết định không có giá trị nếu chúng chỉ là một yêu cầu giấy tờ bị ép buộc sau sự việc.

Một số nhóm thích tên "decisions" (quyết định) hơn nhiều so với từ viết tắt "ADR". Khi một số nhóm dùng tên thư mục "decisions", dường như một bóng đèn bật sáng, và nhóm bắt đầu đưa nhiều thông tin hơn vào thư mục đó, chẳng hạn quyết định về nhà cung cấp, quyết định về kế hoạch, quyết định về lịch trình, v.v. Tất cả các loại thông tin này đều có thể dùng cùng một mẫu. Chúng tôi đưa ra giả thuyết rằng mọi người học nhanh hơn với từ ngữ ("quyết định") so với từ viết tắt ("ADR"), và mọi người có động lực viết các tài liệu đang thực hiện hơn khi bỏ từ "bản ghi", và cũng có một số nhà phát triển và một số quản lý không thích từ "kiến trúc".

Về lý thuyết, tính bất biến là lý tưởng. Trong thực tế, tính khả biến đã hiệu quả hơn với các nhóm của chúng tôi. Chúng tôi chèn thông tin mới vào ADR hiện có, kèm dấu ngày tháng, và một ghi chú rằng thông tin đến sau quyết định. Cách tiếp cận này dẫn đến một "tài liệu sống" mà tất cả chúng tôi đều có thể cập nhật. Các cập nhật điển hình là khi chúng tôi có được thông tin nhờ đồng đội mới, hoặc các dịch vụ mới, hoặc kết quả thực tế từ việc sử dụng của chúng tôi, hoặc sau những thay đổi của bên thứ ba sau sự việc như khả năng của nhà cung cấp, gói giá, thỏa thuận cấp phép, v.v.

## Câu hỏi về làm việc nhóm cho ADR

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

## Các khái niệm bước tiếp theo cho ADR

[Arc42](https://arc42.org/) trả lời hai câu hỏi một cách thực dụng và có thể điều chỉnh theo nhu cầu của bạn. Bạn nên ghi chép/truyền đạt điều gì về kiến trúc của mình? Nên ghi chép/truyền đạt như thế nào? Arc42 gồm các bản ghi quyết định kiến trúc cùng hướng dẫn về mục tiêu, ràng buộc, bối cảnh, chất lượng, rủi ro và hơn thế nữa.

[Mô hình C4](https://c4model.com/) là cách vẽ sơ đồ kiến trúc phần mềm dễ học và thân thiện với lập trình viên. C4 là một tập sơ đồ phân cấp cho bối cảnh, container, thành phần và mã, cùng các sơ đồ hỗ trợ cho bức tranh hệ thống, động và triển khai.

## Sơ đồ, góc nhìn và quan điểm kiến trúc

Một sơ đồ kiến trúc được gọi là "góc nhìn kiến trúc".

Một "góc nhìn kiến trúc" là một thể hiện của một "quan điểm kiến trúc".

Một "quan điểm kiến trúc" hướng tới một đối tượng cụ thể với những mối quan tâm cụ thể.

Ví dụ về quan điểm, góc nhìn và sơ đồ kiến trúc:

- Năng lực kinh doanh

- Quy trình kinh doanh cấp cao

- [Chuỗi giá trị](https://en.wikipedia.org/wiki/Value_stream)

- Chức năng phần mềm được ánh xạ tới các thành phần ứng dụng

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Sơ đồ ngữ cảnh (TO-BE / AS-IS)

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Sơ đồ container (TO-BE / AS-IS)

- [Sơ đồ thực thể-quan hệ](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) để ánh xạ các thực thể dữ liệu tới các thành phần ứng dụng

- [Sơ đồ tuần tự](https://en.wikipedia.org/wiki/Sequence_diagram) để mô tả các luồng chức năng trong hệ thống và cho các tích hợp

- [Mô hình và Ký hiệu Quy trình Kinh doanh](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) sơ đồ để mô tả luồng dữ liệu giữa các thành phần ứng dụng

- [Mô hình và Ký hiệu Quy trình Kinh doanh](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) sơ đồ để mô tả quy trình kinh doanh / kịch bản người dùng

- [Quản lý Danh tính và Truy cập](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) sơ đồ

- [Kiểm soát Truy cập Dựa trên Vai trò](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) sơ đồ với các vai trò theo từng thành phần ứng dụng

- [Kiểm soát Truy cập Dựa trên Thuộc tính](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) sơ đồ với các thuộc tính theo từng thành phần ứng dụng

- Sơ đồ quyền riêng tư

Các sơ đồ liên quan:

- Sơ đồ ca sử dụng cho ban quản lý/khách hàng thấy các ca sử dụng, đi trước các yêu cầu, và các yêu cầu đi trước kiến trúc phần mềm.

- Sơ đồ triển khai cho thấy phần cứng/máy tính vật lý mà các thành phần phần mềm được triển khai lên.
- Sơ đồ luồng dữ liệu cho thấy dữ liệu di chuyển qua hệ thống và được biến đổi ra sao.
- Sơ đồ tuần tự được dùng để cho thấy các giao thức như HTTP hoạt động trên trục thời gian ra sao.

- Sơ đồ hoạt động mô tả quy trình làm việc của các hoạt động mà một hệ thống phần mềm thực hiện, như AI của NPC.

## Hàm thích nghi cho quyết định dưới dạng mã

Hàm thích nghi (fitness function) là các kiểm tra tự động khách quan, được viết bằng mã lập trình, xác minh rằng các quyết định đang được duy trì.

- Hàm thích nghi giúp quyết định có thể kiểm thử và bảo đảm được.

- Hàm thích nghi cho quyết định có thể hỗ trợ rất nhiều cho đảm bảo chất lượng, các quy trình quản lý quy định và mục tiêu quản trị.

### Hàm thích nghi liên hệ với quyết định như thế nào

Bản ghi quyết định ghi lại quyết định, còn hàm thích nghi bảo đảm quyết định đó.

- Quyết định ví dụ: Chúng tôi dùng event sourcing để đáp ứng yêu cầu kiểm toán.

- Hàm thích nghi ví dụ: Chúng tôi dùng máy chủ tích hợp liên tục để kiểm thử rằng mọi thay đổi trạng thái đều phải tạo ra sự kiện.

### Vì sao hàm thích nghi giúp ích cho quyết định

Đo lường khách quan: Hàm thích nghi hoặc đạt hoặc không đạt, nên công việc được hiển thị và rõ ràng.

Sử dụng liên tục: Hàm thích nghi là các quy tắc sống của bạn, chạy trên mọi commit và bản build.

Tự tin để tái cấu trúc: Hàm thích nghi tự động phát hiện lỗi vi phạm quy tắc quyết định.

Quản trị có thể mở rộng: Hàm thích nghi bảo đảm các tiêu chuẩn mà không tạo ra nút thắt cổ chai.

### Hàm thích nghi có thể dùng AI không?

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

### Kiểm thử đơn vị kiến trúc

[ArchUnit](https://www.archunit.org/): kiểm tra các quy tắc kiến trúc của mã Java bằng bất kỳ framework kiểm thử đơn vị Java thông thường nào.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): kiểm tra các quy tắc kiến trúc của mã TypeScript và mã JavaScript bằng Jest, Vitest, Jasmine, v.v.

## Rào chắn quyết định cho pull request

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
tự động đưa ra đúng bản ghi quyết định vào đúng thời điểm, tức là khi
lập trình viên đang sửa mã mà các quyết định đó bao quát. Thay vì hy vọng lập trình viên
đọc thư mục tài liệu trước khi hợp nhất, bối cảnh liên quan xuất hiện ngay trên pull request.

Điều này áp dụng cho mọi loại bản ghi quyết định: quyết định kiến trúc, dữ liệu, tuân thủ, lâm sàng và y tế, bảo mật, và nhiều loại khác.

Hoạt động với mọi hệ thống CI (GitLab, Jenkins, CircleCI) và như một hook pre-commit.
Mã nguồn mở. Giấy phép MIT.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) là một GitHub
Action làm pull request thất bại khi các đường dẫn mã được theo dõi thay đổi mà không có bản ghi quyết định kiến trúc nào được thêm hoặc cập nhật. Các trường hợp miễn trừ rất rõ ràng: một dòng
`ADR-Exempt:` kèm lý do sẽ vượt qua cổng và được ghi vào tóm tắt công việc. Không phụ thuộc mẫu, không có phụ thuộc. Mã nguồn mở. Giấy phép MIT.

## Thông tin thêm

Giới thiệu:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Mẫu:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Chuyên sâu:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - bài học kiến trúc phần mềm hằng tháng miễn phí

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Công cụ:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Hướng dẫn riêng của từng công ty:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Ví dụ:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Video:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcast:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Sách:

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

Xem thêm:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Một định dạng YAML/JSON trung lập với nhà cung cấp, máy đọc được, để biểu diễn quyết định với lập luận tường minh, giả định, trạng thái nhận thức và các đánh đổi. Bổ sung cho ADR bằng cách thêm lập luận có cấu trúc, có thể kiểm chứng vào tài liệu quyết định.
