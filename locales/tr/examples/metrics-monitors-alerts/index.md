# Metrikler, monitörler, uyarılar

İçindekiler:

* [Özet](#özet)
  * [Sorun](#sorun)
  * [Karar](#karar)
  * [Durum](#durum)
* [Ayrıntılar](#ayrıntılar)
  * [Varsayımlar](#varsayımlar)
  * [Kısıtlamalar](#kısıtlamalar)
  * [Pozisyonlar](#pozisyonlar)
  * [Argüman](#argüman)
  * [Etkiler](#etkiler)
* [İlgili](#ilgili)
  * [İlgili kararlar](#ilgili-kararlar)
  * [İlgili gereksinimler](#ilgili-gereksinimler)
  * [İlgili eserler](#ilgili-eserler)
  * [İlgili ilkeler](#ilgili-ilkeler)
* [Notlar](#notlar)
  * [Serbest biçimli metin mesajları ve yapılandırılmış olay mesajları](#serbest-biçimli-metin-mesajları-ve-yapılandırılmış-olay-mesajları)
  * [Graylog daha kolay](#graylog-daha-kolay)
  * [Prometheus biraz ayar gerektirir](#prometheus-biraz-ayar-gerektirir)
  * [AWS hizmetleri karışıktır](#aws-hizmetleri-karışıktır)
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
  * [Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack](#datadog-vs-site24x7--statuscake--pagerduty--sumologic--slack)
  * [Prometheus + AlertManager + Grafana + Stackdriver](#prometheus--alertmanager--grafana--stackdriver)
  * [Zabbix](#zabbix)


## Özet


### Sorun

Uygulamalarımızın ne kadar iyi çalıştığını ve bir sorun olduğunda bilmek istediğimiz için metrikler, monitörler ve uyarılar kullanmak istiyoruz.


### Karar

WIP.


### Durum

Bilgi toplama. Spektrumun olası uçlarından başlıyoruz: en çok önerilen eski ücretsiz araç (Nagios) ve en çok önerilen yeni ücretli araç (New Relic).


## Ayrıntılar


### Varsayımlar

Modern, hızlı, güvenilir, duyarlı vb. web uygulamaları oluşturmak istiyoruz.

İnşa etmek yerine satın almak istiyoruz.


### Kısıtlamalar

Devops boru hattımız ve dağıtım bulutlarımızla iyi çalışan araçlar istiyoruz.


### Pozisyonlar

Şu anda pozisyonları araştırıyoruz.


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

  * Sematext Metrikler, Loglar, Deneyim, İzleme

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

  
### Argüman

Şimdiye kadar Nagios ve New Relic spektrumun uç noktalarıdır. Nagios en eski, en basit, ücretsiz, uygulanabilir araçtır. New Relic en yeni özelliklere sahip, en eksiksiz, ücretli, uygulanabilir araçtır. Bunların değerlendirmeleriyle başlayacağız. Gerektiğinde, spektruma geçeceğiz.

Şimdiye kadar Zabbix en iyi önerilere sahiptir ve en eksiksiz yetenekleri sunar.

Şimdiye kadar ELK, açık kaynaklı, satın almaktan daha iyi bir popülerliğe sahiptir.

Şimdiye kadar Prometheus + Graphana en iyi popülerliğe sahiptir.


### Etkiler

YAPILACAK.


## İlgili


### İlgili kararlar

Seçimler test edilebilirliği, telemetriyi ve müşteri hizmetleri, site güvenilirliği mühendisliği vb. gibi diğer sistemleri etkileyecektir.


### İlgili gereksinimler

YAPILACAK.


### İlgili eserler

YAPILACAK.


### İlgili ilkeler

Kolayca geri döndürülebilir.

Hız ihtiyacı.


## Notlar


Oldukça iyi bir açık kaynak yığını şunlardır:

* Metrikler ve metriklere dayalı uyarılar için Prometheus

* Metrikleri görüntülemek için Grafana

* Loglar ve yapılandırılmış olaylar için Elasticsearch/Logstash/Kibana (ELK)

* Mobil bildirimler için Pushover


### Serbest biçimli metin mesajları ve yapılandırılmış olay mesajları

Serbest biçimli metin mesajları: örneğin, /var/log/messages içinde bulabileceğiniz rastgele şeyler ve uygulama tarafından kasıtlı olarak oluşturulan bir şey. Mesajlar, bellek dışı veya donanım hataları gibi kutuda meydana gelen diğer şeyleri tanımlamak için yararlıdır, ancak çok fazla gereksiz bilgi içerir.

Yapılandırılmış olay mesajları: uygulama tarafından, sabit veya dinamik bir dizi öznitelikle oluşturulur, örneğin bir HTTP isteği günlüğü, bir muhasebe günlüğü, bir kullanıcı girişi.

Genel olarak konuşursak, her istek hakkında özniteliklere göre ayrıntılı olarak inceleyebileceğiniz bir şekilde ayrıntıları günlüğe kaydetmek güzeldir. Bu nedenle, her şeye örneğin bir kullanıcı kimliği veya oturum kimliği eklemek izlemenizi sağlar. Açık izleme de elbette iyidir. Bunun için ELK kullanmak, bir tür fakir adamın https://www.honeycomb.io/ sürümüdür.


### Graylog daha kolay

Deneyimlerime göre Graylog'u başlatmak daha kolay.



### Prometheus biraz ayar gerektirir


Genel olarak metrikler için Prometheus'tan memnunum. Uyarılar biraz ayar gerektirir, ancak oldukça iyidir. Uygulamanıza bağlıdır. Bence son kullanıcıya görünen koşullar hakkında uyarı vermek en iyisidir, temel nedenler hakkında değil. Örneğin, sayfa yükleme süresi iyidir, saniyedeki istek sayısı değildir. Ancak saniyedeki sıfır istek, bir şeylerin yanlış olduğunu gösterir.

Bir hizmetin avantajı, kutudan çıktığı gibi ek zeka sunmalarıdır. Genel olarak Datadog'u severim. Çok fazla veriniz varsa hizmetler korkutucu derecede pahalı olabilir ve bazen bulut dostu olmayan fiyatlandırma modellerine sahip olabilirler, örneğin örnek başına ücretlendirme, örnekler dinamik olduğunda. Her isteğin ücretli bir kullanıcıdan geldiği hizmetler ile reklamla ilgili olanlar arasında da bir fark vardır, bu nedenle isteklerin yalnızca küçük bir yüzdesi size para kazandırır. Çok fazla veriniz olabilir ve o kadar da bütçeniz olmayabilir.

Günde 1 milyar istek alan bazı hizmetler üzerinde çalışıyorum, bu nedenle kendi izleme ve günlük kaydımızı barındırmak mantıklı. Hacimleriniz daha düşükse, barındırılan hizmetler daha kolaydır.


### AWS hizmetleri karışıktır

AWS hizmetleriyle ilgili deneyimim karışıktı. Elasticsearch hizmetleri kararsızdı, bu yüzden bunun için kendi örneklerimizi çalıştırıyoruz. CloudWatch metrikleri pahalıdır, bu yüzden genellikle bunları uygulama yerine "altyapı" düzeyindeki metrikler için kullanırız, yani AWS'nin örnek üzerinde çalışan yazılımdan daha iyi bilebileceği sağlıkla ilgili metrikler. CloudWatch Logları yavaş güncellenebilir ve çok fazla meta veriye sahip değildir. ELK çalıştırmak buna yardımcı olur. Gerçek zamanlı verilere gerçekten ihtiyacım varsa, loglar için Kafka'yı taşıma olarak kullanmak daha iyidir. Bu, Logstash tarafından oldukça iyi desteklenir. Bir Kafka kümesini yönetmek cesaret isteyen bir iştir, ancak çok fazla açıkta boru hattı vardır.


### Kafka

Yorum: Kafka bazen çok zor olabilir veya Kafka kaya gibi sağlam olabilir ve her şeyi birbirine bağladığını neredeyse unutursunuz.


Yorum: Kafka sağlamdı, ancak onu çalıştırmak şaşırtıcı derecede çok işti. Bunu ilişkisel bir veritabanı gibi düşünüyorum, ancak yalnızca "fiziksel" katmanda, örneğin tablo alanları, dosyalar ve bölümler üzerinde çalışıyorsunuz. Başlangıçta yönetim yardımcı programlarının yetersiz olduğu ve örneğin bir tüketici grubunu sıfırlamak için programlar yazmak zorunda kaldığımız zamanlar oldu. http://howfuckedismydatabase.com/nosql/

Yorum: Kafka'yı günlük mesajları için bir "arabellek" ve birden çok sunucudan gelen veriler üzerinde gerçek zamanlı akış işleme yapabileceğimiz bir yer olarak kullanıyoruz. Bir DDOS saldırısı alırsak, verileri birden çok örnekte analiz etmenin bir yoluna ihtiyacımız var. Sunuculardan doğrudan ELK'ye günlük kaydı yapıyorsak, yük Elasticsearch kümesini patlatabilir.

Yorum: Kafka bizim için iyidir çünkü bir DDOS saldırısı alırsak, verileri birden çok örnekte analiz etmenin bir yoluna ihtiyacımız var. Sunuculardan doğrudan ELK'ye günlük kaydı yapıyorsak, yük Elasticsearch kümesini patlatabilir.


Yorum: Kafka daha az iş yapar ve daha verimlidir, bu nedenle yükü daha iyi kaldırabilir. Ve Kafka işini sıraya alır ve yeniden deneriz. Ve Kafka'nın aşırı yüklenmesi, Elasticsearch zorlanıyorsa olacağı gibi, Kibana ile etkileşimli çalışma yapmaya çalışan kullanıcıları etkilemez.

Yorum: Akış işleme çoğunlukla kötüye kullanımı arar, örneğin tüm küme genelinde tek bir IP'den çok fazla trafik ve ardından bloğu tüm küme genelinde paylaşır.

Yorum: logstash-output-kafka eklentisi şu anda oldukça güvenilmez. GitHub sorunlar sayfasındaki birkaç sorundan etkilendim, bunlar asla düzeltilmiyor gibi görünüyor. Onu kullanmaktan, uygulamalarımızdan doğrudan Kafka'ya göndermeye geçmek istiyorum.

Yorum: Artık yapılandırılmış olayları doğrudan uygulamadan Kafka'ya gönderiyoruz. Ana motivasyon, günlük verilerine daha az dokunmak ve diski birden çok kez okuma ve yazmaktan kaçınmaktı. Yüksek hacimli sistemlerde, günlük kaydı uygulamanın kendisinden daha fazla iş alabilir. journald'nin günlükleri doğrudan bir C programından da göndermesini sağlamayı düşünüyorum.


### Loki

Loki'yi yakından takip edin. Henüz hazır değil ama hazır olduğunda bu yığında daha iyi bir uyum olmasını bekliyorum. Loki, grafana laboratuvarları tarafından oluşturulan bir günlük toplayıcıdır, Prometheus ile benzer bir kazıma ve etiket sözdizimi kullanır.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Metrikler için Prometheus + alertmanager. <3 Prometheus.

Günlük kaydı/hata raporlama için Rollbar/Graylog (burada bazı çakışmalar var; küçük bir hizmetin muhtemelen ikisine de ihtiyacı yoktur).

Şu anda, uyarılar sadece ilgili tarafların bildirimlerini açtığı birkaç Slack kanalından birine gidiyor. Eğer daha ciddi bir nöbetçi olsaydık, PagerDuty/VictorOps/vb. gibi yerlere giderlerdi.

Grafikler ve gösterge tabloları için Grafana. Ayrıca, yaklaşan günlük kaydı tesislerinin Graylog'u gereksiz kılıp kılmayacağını görmek için sabırsızlanıyorum.


### Thanos

HA kurulumumuz için Thanos'u ön uç olarak kullanıyoruz. HA çiftlerini nasıl tekilleştireceğini biliyor.

Şu anda 6 aylık yerel Prometheus verilerini tutuyoruz. Bu bizim için oldukça iyi çalışıyor. Ancak uzun vadeli veri depolama için Thanos kurulumumuza kova depolamayı devreye alma sürecindeyim. Teorik olarak, GCS depolama, şu anda kullandığımız GCE standart kalıcı diskten yaklaşık %30 daha ucuz olacaktır.

Şu anda Prometheus verilerini yedeklemiyoruz. Veriler, uyarılar için yeterli olmanın ötesinde bizim için gerçekten önemli değil. Genel filo dağıtımımız yıldan yıla o kadar çok değişiyor ki, birkaç aydan eski geçmiş veriler o kadar da ilginç değil. Yıllık birkaç temel istatistiğe sahip olmak ilginç olabilir, bir çekirdek istatistik kayıt kuralları seti kurabilir ve bunları Federasyon ile depolayabilir veya sadece Thanos'un halletmesine izin verebilirim.

EDİT: Küçük bir uyarı, ben bir Prometheus geliştiricisiyim.


### Prometheus HA

Prometheus'ta HA, birden çok popper çalıştırdığınızda çoğaltma ile yapılır, birden çok popper'ı sorgulamanın ve verileri tekilleştirmenin yolları vardır.

Ölçeklendirme, ağı belirleyerek ve farklı Prometheus'ların ağın farklı kısımlarını sorgulamasıyla yapılır.

Uzun vadeli depolama, Prometheus'un güçlü yanı değildir, ancak influxes veya timescaledb (teknik olarak HA onay işaretini de yapar) gibi bir şeye aktarılır. Bununla ilgili okuduğum makale https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Uzun vadeli şeyleri henüz denemedim, çünkü hala sadece deney yapıyorum ve kısa vadeli grafikler için kullanıyorum, librenms ise ağımı uzun vadeli olarak izliyor.


### Datadog + PagerDuty + Threat Stack

Datadog (PagerDuty ile) ve Threat Stack kullanıyoruz ve daha mutlu olamazdık. DD ile ilgili tek şikayetim, metrik depolamanın nispeten yüksek maliyeti.


### Zabbix

Zabbix, neredeyse her şeyi izlemek için özel komut dosyalarıyla. Sorunsuz çalışıyor.


### Outlyer

Outlyer kullanıyorum, ancak burada çalıştığımı ve kendi ürünümüzü kullanmanın bir zorunluluk olduğunu belirtmeliyim.

Hala Graylog, Sentry ve Statuscake'i geliştirmem gerekiyor.

Önyargılı gelebilir, ancak Nagios ve diğer izleme sistemlerini dahili olarak başarıyla çalıştırdıktan sonra, herhangi bir yeni işte barındırılan bir çözüm satın alıp bu acıdan kurtulurdum.


### Nagios + Nagiosgraph

Tüm izleme ve uyarılar için Nagios kullanıyoruz. Uyarılar e-posta (uyarılar ve kritik bildirimler) ve sesli uygulama bildirimleri (kritik uyarılar için) aracılığıyla gerçekleşir.

Nagiosgraph görselleştirmeler için kullanılır.

Bu kurulum, ortamımızda neler olup bittiği hakkında bizi kapsamlı bir şekilde bilgilendirmede çok etkili oldu. Yaklaşık 110 kritik sunucuyu ve yaklaşık 760 veri noktasını çalıştırıyor ve izliyoruz ve bu izleme sistemi yedi yılı aşkın süredir yerinde.

Bir noktada günlükleri Graylog veya ELk ile de toplamak istiyorum.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager, harika Prometheus Operator helm grafiği aracılığıyla. ELK'nin GKE'deki mütevazı minimum 3 maksimum 5 düğümümüz için çok ağır olduğunu fark ettiğimiz için günlük hala LogDNA huş ağacı planına gidiyor.


### DataDog + Sentry + PagerDuty.

Nagios, Icinga, Zabbix, ELK, Greylog2, Influx ve diğer birçok araç dahil olmak üzere her türlü yazılımı kullanarak kendi izleme çözümlerimi çalıştırırdım, ancak gerçek şu ki, kendi izleme altyapınızı çalıştırmak için çok fazla çaba harcamak gerekiyor, özellikle de başkalarına bu kadar düşük ücretlerle yaptırabiliyorken!

İzleme altyapısını çalıştırmak için başkalarına ödeme yapmak, müşterilerimin izlemeyi izlemek yerine platformlarını çalıştırmaya odaklanmalarını sağlar, bu da platformlarının kararlılığından elde ettikleri değerin Hizmet Olarak İzleme maliyetlerinden çok daha ağır bastığı anlamına gelir.


### Sensu + Graphite + ELK

Şirketim kendi kendine barındırılan şeylere çok düşkün.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Uyarılar için Prometheus + Alertmanager, ekibim basit izlemenin iyi izleme olduğuna inanıyor.

Günlük kaydı ve izleme gibi diğer sistemler, nöbetçi bir uyarı aldığında teşhis için zengin bağlam sağlayacaktır, ancak bunlara asla uyarı oluşturmayız.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Prometheus enstrümanlı hizmetler => Circonus analizi ve görselleştirme


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Aşağıdaki hizmetleri kullanıyoruz:

İzleme için icinga2 ve uyarılar için VictorOps

Hizmetin ayrıntılı izlenmesi için NewRelic

Hizmette hata izleme için Sentry

Slack/E-posta, NewRelic veya icinga2'den tetiklenen uyarıların bir parçasıdır.


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

Analiz için elasticsearch entegrasyonlu icinga2 ve grafikler için graphite+grafana entegrasyonu.

icinga2'deki kuralları uygulama esnekliği sayesinde, geliştiriciler yalnızca bildirim aldıkları hizmetleri görebilirler.

ve icinga2 director aracılığıyla, programcılar kendi kontrollerini (her birkaç günde bir yaparlar - 100 kontrol dışarı, 100 kontrol içeri) büyük ölçekte sıfır sorunla kolayca tanımlayabilirler.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Şu anda sahip olduklarımız:

Metrikler için DataDog

Uygulama izleme için New Relic

Loglar için ELK (Elastic Search + Logstash + Kibana)

İstisnaları günlüğe kaydetmek için Sentry (kendi kendine barındırılan)

Uyarılar için E-postalar + Slack + VictorOps (önem derecesine göre)

Sahip olmak istediklerimiz:

Metrikler için Prometheus (görselleştirme için Grafana)

Uygulama izleme için New Relic (muhtemelen Elastic Search APM)

Loglama için EFK (elastic search + fluentd + kibana). Muhtemelen, Grafana'dan Loki, buraya geldiğimizde üretime hazır olacaktır.

İstisnalar için Sentry

Uyarılar için Alertmanager + e-posta + VictorOps


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Yasal Uyarı: VMware'de çalışır)


### Telegraf + Prometheus + InfluxDB + Grafana

CPU, Disk, Bellek ve Ağ gibi sunucu metrikleri için Telegraf. Ağ cihazlarımızın SNMP izlemesi için de Telegraf kullanıyoruz.

Uygulama metrikleri için Prometheus. Prometheus'un kazıdığı uygulamamıza sağlık kontrolleri kodluyoruz.

Zaman serisi depolama için InfluxDB. Telegraf verilerimizin gönderildiği yer burası.

Gösterge tabloları ve uyarılar için Grafana. Uyarı motoru süper sağlam değil, ancak işini yapıyor. Ayrıca Slack'e uyarılar gönderiyoruz.

Şu anda merkezi bir günlük kaydı çözümüm yok. ELK güçlü ama kurulumu ve yönetimi zor ve incelemeye değer yeterince yakın ücretsiz alternatif bilmiyorum.


### Sematext + Logagent + Experience

Metrikler, loglar, izler ve yakında gerçek kullanıcı izlemesi için Sematext. Bence N farklı araç/hizmet kullanmaktan daha basit/ucuz.

Log gönderimi için rsyslog kullanıyorduk ve sonra Logagent'a geçtik.

Ön uç çökme raporlaması için Sentry kullanıyoruz, ancak kısa süre içinde Experience'a geçeceğiz.

Yasal Uyarı: Ben bir Sematextan'ım.


### Azure Monitor/Analytics + OpsGenie

Keşke Log Analytics'in daha iyi bir arayüzü olsaydı. Splunk'tan uzaklaşıyoruz, ki bu çok daha kolay gezinilebilirdi.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Kendi bildirim sisteminizi çalıştırmak gerçekten istemezsiniz. Güvenlik ekibiniz Splunk'u tercih etmiyorsa Splunk'ı ELK ile değiştirebilirsiniz.


### Telegraf + Prometheus + Grafana + Alertmanager

Toplayıcı olarak Telegraf, izleme ve uyarılar için Prometheus + Alertmanager, kritik uyarılar için slack kanalları ve pagerduty ile entegre. Ana bilgisayar metrikleri görselleştirmesi için Grafana.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Metrikler + uyarılar için Prometheus

Prometheus gösterge tabloları için Grafana

Cloudwatch izleme Prometheus örnekleri

İstisna izleme için sentry

kibana + elasticsearch

graylog

toplu/cron işleri için prometheus Push Gateway

SOP https://github.com/rapidloop/sop, 1 Prometheus örneğinden diğerine metrikleri "itmek/iletmek" için

müşteriler Prometheus istemcilerini kullanır. İstemci tarafında opencensus.io kullanmaya çalışıyoruz.


### PagerDuty + Monitis

PagerDuty + Monitis. Ayrıca bazı hizmetlerin sağlığını test etmek için bazı özel Azure İşlevleri.

Bu yıl Prometheus ve Grafana'yı tanıtmayı düşünüyoruz.


### Prometheus + Grafana + Bosun

Zaman serisi verilerini depolamak için Prometheus. Görselleştirme için Grafana. Uyarı yönetimi için Bosun.


### Azure Monitor/Analytics/Insights/Dashboards

Sadece Azure mağazası, Azure Monitor, Log Analytics, App Insights, Azure Gösterge Tabloları + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Kubernetes'teki konteyner hizmetlerini Prometheus aracılığıyla izlemek için Grafana

Web API'leri ve web uygulamaları için uçtan uca hizmet izleme için Monitis

Uyarı yönetimi için OpsGenie

Sistemlerimizden durum bilgisi almak için Slack


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Uzun süredir (dev)ops mühendisiyim. Nagios ile büyüdüm. Başlangıç ​​SaaS'ım https://checklyhq.com hakkındaki görüşlerinizi almak isterim. Oldukça derinlemesine uyarılarla API izleme ve site işlem izleme yapıyoruz.

Checkly'yi, API alanındaki aktif / sentetik izlemenin biraz sınırlı (ve pahalı) olması nedeniyle başlattım. Tarayıcı tabanlı / betik tabanlı izleme daha da tescilli ve pahalıdır. Puppeteer kullanıyoruz ve fiyatları mümkün olduğunca düşük tutuyoruz.

İzleme yığınımız:

Checkly (kendi ürünümüzü kullanıyoruz...)

AppOptics (özel grafikleme)

SMS mesajları için AWS Cloudwatch ve SNS.

yerleşik Heroku uyarısı.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana, altyapı sorunları veya performans düşüşleri hakkında slack'te bizi uyarır ve uygulama katmanından belirli bir hacimde hata düzeyi günlükleri hakkında slack'te uyarı vermek için logz.io'yu yapılandırdık.


### SignalFX + Splunk + PagerDuty + Slack

Şu anda kullandıklarımız: SignalFX, Splunk, PagerDuty ve Slack. SignalFX'in destek ekibi süper arkadaş canlısı ve duyarlı olsa da, SignalFX'in büyük bir hayranı değilim. Splunk'ı seviyorum (ödeyebilirseniz değer), PagerDuty ve Slack.

Eskiden TICK yığınını kullanırdım, burada C'nin çoğu aslında G idi, yani Grafana idi, ancak Chronograf'ı da biraz kullandım. Bu harikaydı ama yönetmesi zordu. Klasik SaaS ve kendi kendine barındırma ikilemi.

DataDog, New Relic, Graylog, ELK ve BugSnag kullandım. DataDog ve New Relic'i çok seviyorum, Graylog oldukça iyi. Ancak büyük bir ELK hayranı değilim. BugSnag güzel, aslında hata/istisna izlemenin birçok durumda tam günlük izleme için oldukça iyi bir yedek olduğunu düşünüyorum.


### ELK + Prometheus + Grafana

Diğerleri gibi, loglar için ELK ve diğer her şey için Prometheus+Grafana kullanıyoruz.

Bu kurulumu sürdürmek, ara sıra veri kaybetme izni verirseniz kolaydır. Örneğin, Elasticsearch veritabanımız bir sorun yaşarsa (ki bu bizim için ne yazık ki her 2-3 ayda bir olur) HA ile uğraşmayız ve bunun yerine verileri boşaltıp hayatımıza devam ederiz. HA veya uzun vadeli saklama kesinlikle gerekiyorsa, iyi şanslar.


### Datadog + Prometheus + Grafana

Buraya geldiğimde izleme ve uyarı olmadığı için Datadog'u aylık olarak kurdum. Sadece birkaç sitemiz 5 dakikada bir çalışma süresi için izleniyordu. Datadog kurulumu en kolay olanıdır. Diğer tüm sorunları giderdiğimde Prometheus+Grafana'ya geçeceğim. Henüz günlük yönetimi konusunda %100 karar vermedim.

### Nagios + ELK

Desteklediğimiz 100'den fazla ürünümüz var.

Şirket içi için çoğunlukla Nagios ve ELK kullanıyoruz. Bulut için DataDog'dan NewRelic'e geçiş yapıyoruz.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Eskiden datadog kullanıyorduk ama ihtiyaçlarımız için çok pahalı olduğunu gördük. Yanlış anlamayın, harika ama çok büyük bir maliyeti var. Site24x7.com'u yıllık abonelikle DD'nin 2-3 aylık maliyetine kurabildik.

İzleme yığınımız:

Site24x7 - APM, Harici URL izleme, SMTP posta akışı izleme, ssl süre sonları ve süreç izleme.

StatusCake - URL izleme ve onay için - Site24x7 bir şeyi kaçırırsa (ki kaçırmaz) bizim yedeğimizdir, ancak SC ihtiyaçlarımız için harici bağlantı noktası ve hizmet izleme için daha esnektir.

Her iki araç da PagerDuty'ye yükselir ve ardından Slack'te yükseltmelerimizi alırız.

SumoLogic - günlük izleme için (harika bir araç ama ihtiyaçlarımız için biraz karmaşık)

Slack'ten bir uyarıyı onaylayabilir veya düzeltebiliriz.

Daha sonra, site24x7 otomasyonlarının çoğu, 'BedOps' dediğimiz commando.io'ya bağlanır - burada bir uyarı tetiklendiğinde, durumu düzeltmek için birkaç komut dosyası veya otomasyon başlatırız (zamanın %99'unda otomasyon + komut dosyalarımız bizi beladan uzak tutar)

Otomasyonlar başarısız olursa veya düzeltilmesi gereken kapsam dışı bir şey varsa, KB'mizde dahili çalışma kitaplarımız vardır.


### Prometheus + AlertManager + Grafana + Stackdriver

GKE kümelerimizde ve VM'lerimizde metrikler için Prometheus (Operatör) / AlertManager / Grafana.

Google Stackdriver for Logs (varsayılan olarak dahil olduğu ve aktif olduğu ve şu anda ihtiyaçlarımız için yeterli olduğu için).


### Zabbix

Her şey için Zabbix. Ek yazılıma gerek yok.