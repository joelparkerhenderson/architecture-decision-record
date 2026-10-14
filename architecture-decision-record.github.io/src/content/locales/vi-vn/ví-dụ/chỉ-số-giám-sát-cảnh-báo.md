# Chỉ số, giám sát, cảnh báo

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
  * [Thông điệp văn bản tự do so với thông điệp sự kiện có cấu trúc](#thông-điệp-văn-bản-tự-do-so-với-thông-điệp-sự-kiện-có-cấu-trúc)
  * [Graylog dễ hơn](#graylog-dễ-hơn)
  * [Prometheus cần chỉnh một chút](#prometheus-cần-chỉnh-một-chút)
  * [Các dịch vụ AWS có lẫn lộn](#các-dịch-vụ-aws-có-lẫn-lộn)
  * [Kafka](#kafka)
  * [Loki](#loki)
  * [Prometheus + alertmanager + Rollbar + Graylog + Grafana](#prometheus--alertmanager--rollbar--graylog--grafana)
  * [Thanos](#thanos)
  * [Prometheus HA](#prometheus-ha)
  * [Datadog + PagerDuty + Threat Stack](#datadog--pagerduty--threat-stack)
  * [Zabbix](#zabbix)
  * [Outlyer](#outlyer)
  * [Nagios + Nagiosgraph](#nagios--nagiosgraph)
  * [Prometheus + Grafana + AlertManager](#prometheus--grafana--alertmanager)
  * [DataDog + Sentry + PagerDuty.](#datadog--sentry--pagerduty)
  * [Sensu + Graphite + ELK](#sensu--graphite--elk)
  * [Prometheus + Alertmanager](#prometheus--alertmanager)
  * [Sensu + Grafana + Graylog + Kibana + NewRelic.](#sensu--grafana--graylog--kibana--newrelic)
  * [Prometheus + Circonus](#prometheus--circonus)
  * [icinga2 + VictorOps + NewRelic + Sentry + Slack](#icinga2--victorops--newrelic--sentry--slack)
  * [AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver](#appdynamics--papertrail--pagerduty--healthchecksio--stackdriver)
  * [icinga2 + elasticsearch](#icinga2--elasticsearch)
  * [DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps](#datadog--new-relic--elk--efk--sentry--alertmanager--victorops)
  * [Wavefront + Scalyr + PagerDuty + Stackstorm + Slack](#wavefront--scalyr--pagerduty--stackstorm--slack)
  * [Telegraf + Prometheus + InfluxDB + Grafana](#telegraf--prometheus--influxdb--grafana)
  * [Sematext + Logagent + Experience](#sematext--logagent--experience)
  * [Azure Monitor/Analytics + OpsGenie](#azure-monitoranalytics--opsgenie)
  * [Prometheus + Alertmanager + Grafana + Splunk + PagerDuty](#prometheus--alertmanager--grafana--splunk--pagerduty)
  * [Telegraf + Prometheus + Grafana + Alertmanager](#telegraf--prometheus--grafana--alertmanager)
  * [Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch](#prometheus--grafana--cloudwatch--sentry--kibana--elasticsearch)
  * [PagerDuty + Monitis](#pagerduty--monitis)
  * [Prometheus + Grafana + Bosun](#prometheus--grafana--bosun)
  * [Azure Monitor/Analytics/Insights/Dashboards](#azure-monitoranalyticsinsightsdashboards)
  * [Grafana + Monitis + OpsGenie + Slack](#grafana--monitis--opsgenie--slack)
  * [Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail](#checkly--appoptics--cloudwatch--heroku--pagerduty--papertrail)
  * [Instana + Logz.io + slack](#instana--logzio--slack)
  * [SignalFX + Splunk + PagerDuty + Slack](#signalfx--splunk--pagerduty--slack)
  * [ELK + Prometheus + Grafana](#elk--prometheus--grafana)
  * [Datadog + Prometheus + Grafana](#datadog--prometheus--grafana)
  * [Nagios + ELK](#nagios--elk)
  * [Datadog so với Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack](#datadog-so-với-site24x7--statuscake--pagerduty--sumologic--slack)
  * [Prometheus + AlertManager + Grafana + Stackdriver](#prometheus--alertmanager--grafana--stackdriver)
  * [Zabbix](#zabbix-1)


## Tóm tắt


### Vấn đề

Chúng tôi muốn dùng các chỉ số, bộ giám sát và cảnh báo, vì chúng tôi muốn biết các ứng dụng của mình đang hoạt động tốt đến đâu, và biết khi nào có vấn đề.


### Quyết định

WIP.


### Trạng thái

Đang thu thập thông tin. Chúng tôi bắt đầu từ hai đầu hợp lý của phổ: công cụ miễn phí cũ được khuyên dùng nhiều nhất (Nagios) và công cụ trả phí mới được khuyên dùng nhiều nhất (New Relic).


## Chi tiết


### Giả định

Chúng tôi muốn tạo các ứng dụng web hiện đại, nhanh, đáng tin cậy, đáp ứng, v.v.

Chúng tôi muốn mua hơn là xây dựng.


### Ràng buộc

Chúng tôi muốn các công cụ hoạt động tốt với pipeline devops của chúng tôi và với các đám mây triển khai của chúng tôi.


### Lập trường

Chúng tôi hiện đang nghiên cứu các lập trường.


  * AlertManager

  * AppDynamics

  * AppOptics

  * Azure Monitor/Analytics/Insights/Dashboards

  * Bosun

  * Checkly

  * Circonus

  * Cloudwatch

  * EFK

  * ELK

  * Grafana

  * Grafana

  * Graphite

  * Graylog

  * Healthchecks.io

  * Heroku

  * icinga2

  * InfluxDB

  * Instana

  * Kafka

  * Logagent

  * Logz.io

  * Loki

  * Monitis

  * Nagios

  * Nagios

  * Nagiosgraph

  * NewRelic

  * OpsGenie

  * Outlyer

  * PagerDuty

  * Pagerduty

  * PagerDuty

  * Papertrail

  * Prometheus

  * Rollbar

  * Scalyr

  * Sematext Metrics, Logs, Experience, Tracing

  * Sensu

  * SignalFX

  * Slack

  * Splunk

  * Stackdriver

  * Stackstorm

  * Telegraf

  * Telegraf

  * Thanos

  * VictorOps

  * Wavefront

  * Zabbix

  
### Lập luận

Cho đến nay, Nagios và New Relic là hai đầu của phổ. Nagios là công cụ lâu đời nhất, đơn giản nhất, miễn phí, khả thi. New Relic là công cụ có tính năng mới nhất, đầy đủ nhất, trả phí, khả thi. Chúng tôi sẽ bắt đầu với việc đánh giá hai công cụ này. Khi cần, chúng tôi sẽ di chuyển vào bên trong phổ.  

Cho đến nay, Zabbix có các khuyến nghị tốt nhất, và cũng cung cấp các khả năng đầy đủ nhất.

Cho đến nay, ELK có độ phổ biến tốt nhất về mã nguồn mở tự xây so với mua.

Cho đến nay, Prometheus + Graphana có độ phổ biến tốt nhất.


### Hàm ý

TODO.


## Liên quan


### Các quyết định liên quan

Các lựa chọn sẽ ảnh hưởng đến khả năng kiểm thử, đo từ xa, và có khả năng các hệ thống khác như dịch vụ khách hàng, kỹ thuật độ tin cậy trang web, v.v.


### Các yêu cầu liên quan

TODO.


### Các tạo phẩm liên quan

TODO.


### Các nguyên tắc liên quan

Dễ đảo ngược.

Cần tốc độ.


## Ghi chú


Một ngăn xếp mã nguồn mở khá tốt là:

* Prometheus cho các chỉ số và cảnh báo dựa trên chỉ số

* Grafana để hiển thị các chỉ số

* Elasticsearch/Logstash/Kibana (ELK) cho nhật ký và các sự kiện có cấu trúc

* Pushover cho thông báo trên di động


### Thông điệp văn bản tự do so với thông điệp sự kiện có cấu trúc

Thông điệp văn bản tự do: ví dụ, loại thứ ngẫu nhiên bạn sẽ tìm thấy trong /var/log/messages, và thứ do ứng dụng cố ý tạo ra. Các thông điệp này hữu ích để xác định những thứ khác đang xảy ra trên máy như hết bộ nhớ hoặc lỗi phần cứng, nhưng có rất nhiều rác. 

Thông điệp sự kiện có cấu trúc: do ứng dụng tạo ra, với một tập thuộc tính cố định hoặc động, ví dụ nhật ký yêu cầu HTTP, nhật ký kế toán, đăng nhập người dùng.

Nói chung, sẽ tốt khi ghi lại chi tiết của mọi yêu cầu theo cách bạn có thể khoan sâu dựa trên các thuộc tính. Vì vậy việc thêm ví dụ userid hoặc sessionid vào mọi thứ cho phép bạn truy vết. Việc truy vết tường minh cũng tốt, tất nhiên. Dùng ELK cho việc này kiểu như phiên bản nghèo của https://www.honeycomb.io/


### Graylog dễ hơn

Graylog dễ dựng lên hơn theo kinh nghiệm của tôi.



### Prometheus cần chỉnh một chút


Tôi nhìn chung hài lòng với Prometheus cho các chỉ số. Phần cảnh báo cần chỉnh một chút, nhưng khá tốt. Nó phụ thuộc vào ứng dụng của bạn. Tôi nghĩ tốt nhất là cảnh báo về các điều kiện mà người dùng cuối nhìn thấy, không phải các nguyên nhân gốc. Ví dụ, thời gian tải trang là tốt, số yêu cầu mỗi giây thì không. Dù vậy không có yêu cầu nào mỗi giây cho thấy có điều gì đó sai.

Ưu điểm của một dịch vụ là họ cung cấp thêm trí tuệ ngay từ đầu. Tôi nhìn chung thích Datadog. Các dịch vụ có thể đắt đến đáng sợ nếu bạn có nhiều dữ liệu, và đôi khi có các mô hình giá không thân thiện với đám mây, ví dụ tính phí theo mỗi phiên bản, trong khi các phiên bản là động. Cũng có sự khác biệt giữa các dịch vụ mà mọi yêu cầu đều đến từ người dùng trả phí và những dịch vụ liên quan đến quảng cáo, nên chỉ một tỷ lệ nhỏ các yêu cầu kiếm ra tiền cho bạn. Bạn có thể có nhiều dữ liệu mà không có nhiều ngân sách.

Tôi làm việc trên một số dịch vụ nhận 1 tỷ yêu cầu mỗi ngày, nên việc tự lưu trữ giám sát và ghi nhật ký là hợp lý. Nếu khối lượng của bạn thấp hơn, các dịch vụ được lưu trữ sẽ dễ hơn.


### Các dịch vụ AWS có lẫn lộn

Trải nghiệm của tôi với các dịch vụ AWS là lẫn lộn. Dịch vụ Elasticsearch của họ không ổn định, nên chúng tôi chạy các phiên bản riêng cho việc đó. Các chỉ số CloudWatch đắt, nên chúng tôi nhìn chung chỉ dùng chúng cho các chỉ số mức "hạ tầng" thay vì ứng dụng, tức là các chỉ số liên quan đến sức khỏe mà AWS có thể biết rõ hơn điều gì đang xảy ra so với phần mềm chạy trên phiên bản. CloudWatch Logs có thể cập nhật chậm và không có nhiều siêu dữ liệu. Chạy ELK giúp việc đó. Nếu tôi thực sự muốn dữ liệu thời gian thực, thì dùng Kafka làm phương tiện vận chuyển cho nhật ký là tốt hơn. Điều đó được Logstash hỗ trợ khá tốt. Tuy vậy, quản lý một cụm Kafka không dành cho người yếu bóng vía, có rất nhiều đường ống lộ ra.


### Kafka

Bình luận: Kafka đôi khi có thể cực kỳ rắc rối, hoặc Kafka có thể vững như đá đến mức bạn gần như quên rằng nó đang ở đó gắn kết mọi thứ. 


Bình luận: Kafka vững chắc, nhưng việc làm cho nó chạy tốn một lượng công việc đáng ngạc nhiên. Tôi coi nó như một cơ sở dữ liệu quan hệ nhưng bạn chỉ làm việc ở tầng "vật lý", ví dụ không gian bảng, tệp và phân vùng. Có những lúc đầu tiên các tiện ích quản lý còn thiếu, và chúng tôi phải viết chương trình để ví dụ đặt lại một nhóm người tiêu thụ. http://howfuckedismydatabase.com/nosql/

Bình luận: Chúng tôi dùng Kafka như một "bộ đệm" cho các thông điệp nhật ký và một nơi chúng tôi có thể thực hiện xử lý luồng thời gian thực trên dữ liệu đến từ nhiều máy chủ. Nếu chúng tôi bị tấn công DDOS, thì chúng tôi cần một cách phân tích dữ liệu qua nhiều phiên bản. Nếu chúng tôi ghi nhật ký trực tiếp từ các máy chủ vào ELK, tải có thể làm sập cụm Elasticsearch.

Bình luận: Kafka tốt cho chúng tôi vì nếu chúng tôi bị tấn công DDOS, thì chúng tôi cần một cách phân tích dữ liệu qua nhiều phiên bản. Nếu chúng tôi ghi nhật ký trực tiếp từ các máy chủ vào ELK, tải có thể làm sập cụm Elasticsearch.


Bình luận: Kafka làm ít việc hơn và hiệu quả hơn, nên có thể xử lý tải tốt hơn. Và chúng tôi xếp hàng công việc Kafka và thử lại. Và việc Kafka bị quá tải không ảnh hưởng đến những người dùng đang cố làm việc tương tác với Kibana, như khi Elasticsearch đang vật lộn.

Bình luận:  Xử lý luồng chủ yếu tìm kiếm lạm dụng, ví dụ quá nhiều lưu lượng từ một IP duy nhất trên toàn cụm, và sau đó chia sẻ việc chặn trên toàn cụm.

Bình luận: Tuy nhiên, plugin logstash-output-kafka hiện khá không đáng tin cậy. Tôi đã bị ảnh hưởng bởi nhiều vấn đề trên trang GitHub issues của nó, dường như không bao giờ được sửa. Tôi muốn chuyển khỏi việc dùng nó, sang gửi trực tiếp từ các ứng dụng của chúng tôi tới Kafka.

Bình luận: Hiện chúng tôi đang gửi các sự kiện có cấu trúc trực tiếp từ ứng dụng tới Kafka. Động lực chính là chạm vào dữ liệu nhật ký ít lần hơn và tránh đọc và ghi đĩa nhiều lần. Trong các hệ thống khối lượng cao, việc ghi nhật ký có thể tốn nhiều công hơn chính ứng dụng. Tôi cũng đang nghĩ đến việc làm cho journald gửi nhật ký trực tiếp, từ một chương trình C.


### Loki

Hãy theo dõi sát Loki. Nó chưa sẵn sàng nhưng khi sẵn sàng tôi kỳ vọng nó sẽ phù hợp hơn trong ngăn xếp này. Loki là một bộ tổng hợp nhật ký do grafana labs tạo ra, dùng cú pháp thu thập và thẻ tương tự Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager cho các chỉ số. Yêu Prometheus.

Rollbar/Graylog cho ghi nhật ký/báo cáo lỗi (có một số chồng lấn ở đây; một dịch vụ nhỏ có lẽ không cần cả hai).

Hiện tại, các cảnh báo chỉ đi vào một trong vài kênh Slack mà các bên quan tâm đã bật thông báo. Nếu chúng tôi nghiêm túc hơn về trực on-call thì chúng sẽ đi vào PagerDuty/VictorOps/v.v.

Grafana cho đồ thị và bảng điều khiển. Cũng háo hức mong chờ xem các tiện ích ghi nhật ký sắp ra mắt của họ có làm Graylog trở nên không cần thiết hay không.


### Thanos

Chúng tôi dùng Thanos làm front-end cho thiết lập HA của chúng tôi. Nó biết cách loại bỏ trùng lặp các cặp HA.

Hiện chúng tôi đang giữ 6 tháng dữ liệu Prometheus cục bộ. Điều này hoạt động khá tốt với chúng tôi. Nhưng tôi đang ở giữa việc triển khai lưu trữ bucket cho thiết lập Thanos của chúng tôi để lưu trữ dữ liệu dài hạn. Về lý thuyết, lưu trữ GCS sẽ rẻ hơn khoảng 30% so với đĩa bền vững tiêu chuẩn GCE mà chúng tôi dùng hiện nay.

Hiện chúng tôi không sao lưu dữ liệu Prometheus. Dữ liệu thực sự không quan trọng với chúng tôi ngoài việc có đủ cho cảnh báo. Việc triển khai toàn bộ đội máy của chúng tôi thay đổi nhiều từ năm này sang năm khác đến mức dữ liệu lịch sử cũ hơn vài tháng không còn thú vị. Có thể thú vị khi có vài số liệu cốt lõi so năm trước, tôi có thể thiết lập một bộ quy tắc ghi số liệu cốt lõi và lưu chúng bằng Federation hoặc cứ để Thanos lo.

CHỈNH SỬA: Một tuyên bố nhỏ, tôi là một nhà phát triển Prometheus.


### Prometheus HA

HA trong Prometheus được thực hiện bằng cách nhân bản: bạn chạy nhiều bộ thu thập, có những cách thăm dò nhiều nơi và loại bỏ trùng lặp dữ liệu.

Việc mở rộng quy mô bằng cách quyết định mạng và để các Prometheus khác nhau thăm dò các phần khác nhau của mạng.

Lưu trữ dài hạn không phải thế mạnh của Prometheus mà được chuyển sang thứ như influx hoặc timescaledb (về mặt kỹ thuật cũng đánh dấu được ô HA). Bài viết tôi đã đọc về nó https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Chưa thử phần dài hạn vì tôi vẫn chỉ đang thử nghiệm và dùng nó cho đồ thị ngắn hạn trong khi librenms giám sát mạng của tôi cho dài hạn


###  Datadog + PagerDuty + Threat Stack

Chúng tôi dùng Datadog (cùng PagerDuty) và Threat Stack và không thể hài lòng hơn. Phàn nàn duy nhất của tôi về DD là chi phí lưu trữ chỉ số tương đối cao.


### Zabbix

Zabbix với các tập lệnh tùy chỉnh để giám sát hầu như mọi thứ. Hoạt động như một phép màu.


### Outlyer

Tôi đang dùng Outlyer, nhưng tôi phải tuyên bố rằng tôi làm việc ở đây, và dùng sản phẩm của chính mình (dog fooding) là bắt buộc.

Vẫn cần Graylog, Sentry và Statuscake để nâng cao.

Nghe có vẻ thiên vị, nhưng sau khi vui vẻ chạy Nagios và các hệ thống giám sát khác nội bộ, tôi sẽ mua một giải pháp được lưu trữ ở bất kỳ công việc mới nào và gạt bỏ nỗi đau đó đi.


### Nagios + Nagiosgraph

Chúng tôi chạy Nagios cho mọi giám sát và cảnh báo. Cảnh báo diễn ra qua email (cảnh báo và thông báo nghiêm trọng) và thông báo ứng dụng nghe được (cho các cảnh báo nghiêm trọng).

Nagiosgraph được dùng cho trực quan hóa.

Thiết lập này đã rất hiệu quả trong việc giúp chúng tôi nắm thông tin đầy đủ về những gì đang xảy ra trong môi trường của mình. Chúng tôi chạy và giám sát khoảng 110 máy chủ quan trọng sống còn và khoảng 760 điểm dữ liệu, và đã có hệ thống buổi sáng này hơn bảy năm.

Tôi cũng muốn tổng hợp nhật ký bằng Graylog hoặc ELk vào một lúc nào đó.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager qua helm chart Prometheus Operator tuyệt vời. Nhật ký vẫn đi vào gói LogDNA birch vì chúng tôi nhận thấy ELK quá nặng cho cụm khiêm tốn tối thiểu 3 tối đa 5 nút trên GKE của chúng tôi.


### DataDog + Sentry + PagerDuty.

Tôi từng tự chạy tất cả các giải pháp giám sát của mình dùng đủ loại phần mềm bao gồm Nagios, Icinga, Zabbix, ELK, Greylog2, Influx và nhiều công cụ khác, nhưng sự thật là có quá nhiều công sức trong việc chạy hạ tầng giám sát của riêng bạn, đặc biệt khi bạn có thể trả tiền cho người khác với mức giá thấp như vậy để làm việc đó cho bạn!

Trả tiền cho người khác chạy hạ tầng giám sát giải phóng các khách hàng của tôi để tập trung chạy nền tảng của họ thay vì giám sát việc giám sát, nghĩa là giá trị họ có được từ sự ổn định của nền tảng lớn hơn nhiều so với bất kỳ chi phí nào của Giám sát như một Dịch vụ.


### Sensu + Graphite + ELK

Công ty tôi rất thích những thứ tự lưu trữ.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager cho cảnh báo, nhóm của tôi tin rằng giám sát đơn giản là giám sát tốt.

Các hệ thống khác như ghi nhật ký và truy vết sẽ cung cấp ngữ cảnh phong phú để chẩn đoán khi người trực on-call nhận được cảnh báo, nhưng chúng tôi không bao giờ xây dựng cảnh báo dựa trên chúng.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Các dịch vụ được đo bằng Prometheus => phân tích và trực quan hóa Circonus


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Chúng tôi đang dùng các dịch vụ sau:

icinga2 cho giám sát và VictorOps cho cảnh báo

NewRelic cho giám sát chi tiết dịch vụ

Sentry để theo dõi lỗi trong dịch vụ

Slack/Email là một phần của cảnh báo được kích hoạt từ NewRelic hoặc icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 với tích hợp elasticsearch để phân tích và tích hợp graphite+grafana cho đồ thị.

nhờ sự linh hoạt của các quy tắc apply trong icinga2, các nhà phát triển chỉ có thể thấy các dịch vụ mà họ nhận thông báo.

và qua icinga2 director, các lập trình viên có thể dễ dàng định nghĩa các kiểm tra của riêng họ (mà họ làm, vài ngày một lần - 100 kiểm tra đi ra, 100 kiểm tra khác đi vào) ở quy mô lớn mà không rắc rối.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Những gì chúng tôi có bây giờ:

DataDog cho các chỉ số

New Relic cho giám sát ứng dụng

ELK (Elastic Search + Logstash + Kibana) cho nhật ký

Sentry (tự lưu trữ) để ghi lại ngoại lệ

Email + Slack + VictorOps cho cảnh báo (dựa trên mức độ nghiêm trọng)

Những gì chúng tôi muốn có:

Prometheus cho các chỉ số (Grafana để trực quan hóa)

New Relic (có lẽ Elastic Search APM) cho giám sát ứng dụng

EFK (elastic search + fluentd + kibana) cho ghi nhật ký. Có lẽ, Loki của Grafana sẽ sẵn sàng sản xuất vào lúc chúng tôi đến đó

Sentry cho các ngoại lệ

Alertmanager + email + VictorOps cho các cảnh báo


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Tuyên bố: làm việc tại VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf cho các chỉ số máy chủ như CPU, Đĩa, Bộ nhớ và Mạng. Chúng tôi cũng dùng Telegraf để giám sát SNMP các thiết bị mạng của mình.

Prometheus cho các chỉ số ứng dụng. Chúng tôi viết mã kiểm tra sức khỏe vào ứng dụng mà Prometheus thu thập.

InfluxDB cho lưu trữ chuỗi thời gian. Đây là nơi dữ liệu Telegraf của chúng tôi được gửi tới.

Grafana cho các bảng điều khiển và cảnh báo. Công cụ cảnh báo không quá mạnh, nhưng làm được việc. Chúng tôi cũng bắn cảnh báo vào Slack.

Thứ tôi chưa có lúc này là một giải pháp ghi nhật ký tập trung. ELK mạnh nhưng khó thiết lập và quản lý, và tôi không biết lựa chọn miễn phí nào đủ gần để tìm hiểu.


### Sematext + Logagent + Experience

Sematext cho các chỉ số, cho nhật ký, cho các dấu vết, và sắp tới cho cả giám sát người dùng thực. Đơn giản/rẻ hơn dùng N công cụ/dịch vụ khác nhau, theo ý kiến của tôi.

Để gửi nhật ký chúng tôi từng dùng rsyslog rồi chuyển sang Logagent.

Để báo cáo sự cố frontend chúng tôi dùng Sentry, nhưng sẽ sớm chuyển sang Experience.

Tuyên bố: Tôi là một Sematextan.


### Azure Monitor/Analytics + OpsGenie

Tôi ước Log Analytics có giao diện tốt hơn. Chúng tôi đang chuyển khỏi splunk, thứ dễ điều hướng hơn nhiều.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Bạn thực sự không muốn tự chạy hệ thống thông báo của mình. Bạn có thể thay Splunk bằng ELK trừ khi đội Bảo mật của bạn thích Splunk hơn.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf làm bộ thu thập, Prometheus + Alertmanager cho giám sát và cảnh báo, tích hợp với các kênh slack và pagerduty cho cảnh báo nghiêm trọng. Grafana để trực quan hóa chỉ số máy chủ.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus cho chỉ số + cảnh báo

Grafana cho các bảng điều khiển Prometheus

Cloudwatch giám sát các phiên bản Prometheus

sentry để theo dõi ngoại lệ

kibana + elasticsearch

graylog

prometheus Push Gateway cho batch/cronjob

SOP https://github.com/rapidloop/sop để "đẩy/chuyển tiếp" các chỉ số từ 1 phiên bản Prometheus sang phiên bản khác

các máy khách hoặc dùng máy khách Prometheus. Chúng tôi cố dùng opencensus.io ở phía máy khách


### PagerDuty + Monitis

PagerDuty + Monitis. Cũng một số Azure Functions đặt riêng để kiểm tra sức khỏe của một số dịch vụ.

Hy vọng đưa Prometheus và Grafana vào năm nay


### Prometheus + Grafana + Bosun

Prometheus để lưu dữ liệu chuỗi thời gian. Grafana để trực quan hóa. Bosun để quản lý cảnh báo.


### Azure Monitor/Analytics/Insights/Dashboards

Cửa hàng chỉ dùng Azure, Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana để giám sát các dịch vụ container trong Kubernetes qua Prometheus

Monitis để giám sát dịch vụ đầu-cuối chủ yếu cho API web và ứng dụng web

OpsGenie để quản lý cảnh báo

Slack để nhận thông tin trạng thái từ các hệ thống của chúng tôi


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Kỹ sư (dev)ops lâu năm ở đây. Lớn lên với Nagios. Rất muốn nghe ý kiến về SaaS tự gây vốn của tôi https://checklyhq.com. Chúng tôi làm giám sát API & giám sát giao dịch trang web với cảnh báo khá sâu.

Tôi bắt đầu Checkly vì giám sát chủ động / tổng hợp trong không gian API hơi hạn chế (và đắt). Giám sát dựa trên trình duyệt / theo kịch bản còn độc quyền và đắt hơn. Chúng tôi dùng Puppeteer và giữ giá thấp nhất có thể.

Ngăn xếp giám sát của chúng tôi:

Checkly (dog fooding...)

AppOptics (vẽ đồ thị tùy chỉnh)

AWS Cloudwatch & SNS cho tin nhắn SMS.

cảnh báo Heroku tích hợp sẵn.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana cảnh báo chúng tôi trong slack về các vấn đề hạ tầng hoặc suy giảm hiệu năng, và chúng tôi đã cấu hình logz.io để cảnh báo trong slack ở một lượng nhất định nhật ký mức lỗi từ tầng ứng dụng.


### SignalFX + Splunk + PagerDuty + Slack

Hiện đang dùng: SignalFX, Splunk, PagerDuty và Slack. Tôi không phải fan lớn của SignalFX mặc dù đội hỗ trợ của họ rất thân thiện và phản hồi nhanh. Tôi thích Splunk (đáng giá nếu bạn trả được), PagerDuty và Slack.

Tôi từng dùng ngăn xếp TICK trong đó phần lớn chữ C thực ra là G, tức Grafana mặc dù tôi cũng dùng Chronograf một chút. Nó tuyệt vời nhưng quản lý rất phiền. Tình thế khó xử kinh điển SaaS so với tự lưu trữ.

Tôi đã dùng DataDog, New Relic, Graylog, ELK và BugSnag. Tôi rất thích DataDog và New Relic, Graylog khá tốt. Tôi không phải fan lớn của ELK. BugSnag tốt, tôi thực sự cảm thấy việc theo dõi lỗi/ngoại lệ là một sự thay thế khá tốt cho giám sát nhật ký đầy đủ, trong nhiều trường hợp.


### ELK + Prometheus + Grafana

Giống những người khác, chúng tôi dùng ELK cho nhật ký và Prometheus+Grafana cho mọi thứ khác.

Việc duy trì thiết lập này dễ nếu bạn cho phép bản thân thỉnh thoảng mất dữ liệu. Ví dụ, nếu cơ sở dữ liệu ElasticSearch của chúng tôi rơi vào trạng thái tệ (rất tiếc xảy ra cứ 2-3 tháng với chúng tôi) chúng tôi không bận tâm HA mà thay vào đó bỏ dữ liệu và tiếp tục cuộc sống. Nếu bạn tuyệt đối phải có HA hoặc lưu giữ dài hạn, chúc may mắn.


### Datadog + Prometheus + Grafana

Tôi thiết lập Datadog theo tháng vì khi tôi đến đây, không có giám sát và không có cảnh báo. Chỉ một vài trang của chúng tôi được giám sát mỗi 5 phút về thời gian hoạt động. Datadog chắc chắn là dễ thiết lập nhất. Khi tôi xử lý xong mọi vấn đề khác, tôi sẽ chuyển sang Prometheus+Grafana. Chưa quyết định 100% về quản lý nhật ký.

### Nagios + ELK

Chúng tôi hỗ trợ hơn 100+ sản phẩm.

Với tại chỗ, chủ yếu là Nagios và ELK. Với đám mây, chúng tôi đang chuyển từ DataDog sang NewRelic.


### Datadog so với Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Chúng tôi từng dùng datadog nhưng thấy nó quá đắt cho nhu cầu của mình. Đừng hiểu lầm, nó tuyệt vời nhưng có chi phí rất lớn. Chúng tôi đã thiết lập được site24x7.com với đăng ký hằng năm khoảng 2-3 tháng chi phí của DD.

Ngăn xếp giám sát của chúng tôi:

Site24x7 - APM, giám sát URL bên ngoài, giám sát luồng thư SMTP, hết hạn ssl và giám sát tiến trình.

StatusCake - để giám sát và xác nhận URL - Đó là dự phòng của chúng tôi phòng khi site24x7 bỏ sót điều gì (nó không bỏ sót) nhưng SC linh hoạt hơn cho giám sát cổng và dịch vụ bên ngoài theo nhu cầu của chúng tôi.

Cả hai công cụ đều leo thang lên PagerDuty, và sau đó chúng tôi nhận các leo thang của mình trong slack.

SumoLogic - để giám sát nhật ký (đó là công cụ tuyệt vời nhưng hơi phức tạp cho nhu cầu của chúng tôi)

Từ slack chúng tôi có thể ack, hoặc khắc phục cảnh báo.

Sau đó chúng tôi có nhiều tự động hóa site24x7 kết nối với commando.io cho thứ mà chúng tôi gọi là 'BedOps' - nơi một cảnh báo được kích hoạt, chúng tôi khởi chạy vài tập lệnh hoặc tự động hóa như một nỗ lực khắc phục tình huống (99% thời gian tự động hóa + các tập lệnh của chúng tôi giữ chúng tôi tránh khỏi rắc rối).

Chúng tôi có các sổ tay vận hành nội bộ trong KB của mình cho khi tự động hóa thất bại hoặc có điều gì đó ngoài phạm vi cần sửa.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana cho các chỉ số trong các cụm GKE và VM của chúng tôi.

Google Stackdriver cho Nhật ký (vì nó được bao gồm và hoạt động theo mặc định và hiện đủ cho nhu cầu của chúng tôi).


### Zabbix

Zabbix cho mọi thứ. Không cần phần mềm bổ sung.
