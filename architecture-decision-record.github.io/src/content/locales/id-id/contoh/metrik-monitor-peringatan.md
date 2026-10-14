# Metrik, monitor, peringatan

Daftar isi:

* [Ringkasan](#ringkasan)
  * [Isu](#isu)
  * [Keputusan](#keputusan)
  * [Status](#status)
* [Rincian](#rincian)
  * [Asumsi](#asumsi)
  * [Batasan](#batasan)
  * [Posisi](#posisi)
  * [Argumen](#argumen)
  * [Implikasi](#implikasi)
* [Terkait](#terkait)
  * [Keputusan terkait](#keputusan-terkait)
  * [Persyaratan terkait](#persyaratan-terkait)
  * [Artefak terkait](#artefak-terkait)
  * [Prinsip terkait](#prinsip-terkait)
* [Catatan](#catatan)
  * [Pesan teks bebas vs pesan event terstruktur](#pesan-teks-bebas-vs-pesan-event-terstruktur)
  * [Graylog lebih mudah](#graylog-lebih-mudah)
  * [Prometheus perlu sedikit penyetelan](#prometheus-perlu-sedikit-penyetelan)
  * [Layanan AWS beragam hasilnya](#layanan-aws-beragam-hasilnya)
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
  * [Zabbix](#zabbix-1)


## Ringkasan


### Isu

Kami ingin menggunakan metrik, monitor, dan peringatan, karena kami ingin mengetahui seberapa baik aplikasi kami berfungsi, dan mengetahui kapan ada masalah.


### Keputusan

WIP.


### Status

Mengumpulkan informasi. Kami memulai dari ujung-ujung spektrum yang masuk akal: alat gratis lama yang paling banyak direkomendasikan (Nagios) dan alat berbayar baru yang paling banyak direkomendasikan (New Relic).


## Rincian


### Asumsi

Kami ingin membuat aplikasi web yang modern, cepat, andal, responsif, dll.

Kami ingin membeli daripada membangun.


### Batasan

Kami menginginkan perangkat yang bekerja dengan baik dengan pipeline devops kami dan dengan cloud deployment kami.


### Posisi

Kami sedang meneliti posisi-posisi saat ini.


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

  
### Argumen

Sejauh ini, Nagios dan New Relic adalah ujung-ujung spektrum. Nagios adalah alat yang paling lama, paling sederhana, gratis, dan layak. New Relic adalah alat dengan fitur terbaru, paling lengkap, berbayar, dan layak. Kami akan memulai dengan evaluasi keduanya. Sesuai kebutuhan, kami akan berpindah ke dalam spektrum.  

Sejauh ini, Zabbix memiliki rekomendasi terbaik, dan juga menawarkan kemampuan paling lengkap.

Sejauh ini, ELK memiliki popularitas terbaik untuk membangun sendiri sumber terbuka dibandingkan membeli.

Sejauh ini, Prometheus + Graphana memiliki popularitas terbaik.


### Implikasi

TODO.


## Terkait


### Keputusan terkait

Pilihan akan memengaruhi kemampuan pengujian, telemetri, dan kemungkinan sistem lain seperti untuk layanan pelanggan, rekayasa keandalan situs, dll.


### Persyaratan terkait

TODO.


### Artefak terkait

TODO.


### Prinsip terkait

Mudah dibatalkan.

Kebutuhan akan kecepatan.


## Catatan


Tumpukan sumber terbuka yang cukup bagus adalah:

* Prometheus untuk metrik dan peringatan berbasis metrik

* Grafana untuk menampilkan metrik

* Elasticsearch/Logstash/Kibana (ELK) untuk log dan event terstruktur

* Pushover untuk notifikasi seluler


### Pesan teks bebas vs pesan event terstruktur

Pesan teks bebas: misalnya, hal-hal acak yang akan Anda temukan di /var/log/messages, dan sesuatu yang dihasilkan dengan sengaja oleh aplikasi. Pesan-pesan ini berguna untuk mengidentifikasi hal-hal lain yang terjadi pada mesin seperti kehabisan memori atau kesalahan perangkat keras, tetapi banyak sampahnya. 

Pesan event terstruktur: dihasilkan oleh aplikasi, dengan sekumpulan atribut yang tetap atau dinamis, misalnya log permintaan HTTP, log akuntansi, login pengguna.

Secara umum, sebaiknya mencatat detail setiap permintaan dengan cara yang memungkinkan Anda menelusuri berdasarkan atribut. Jadi menambahkan misalnya userid atau sessionid ke segalanya memungkinkan Anda melacak. Pelacakan eksplisit juga baik, tentu saja. Menggunakan ELK untuk ini semacam versi orang miskin dari https://www.honeycomb.io/


### Graylog lebih mudah

Graylog lebih mudah dijalankan berdasarkan pengalaman saya.



### Prometheus perlu sedikit penyetelan


Saya secara umum senang dengan Prometheus untuk metrik. Peringatan memerlukan sedikit penyetelan, tetapi cukup bagus. Ini tergantung pada aplikasi Anda. Menurut saya sebaiknya memberi peringatan pada kondisi yang terlihat oleh pengguna akhir, bukan penyebab yang mendasarinya. Misalnya, waktu muat halaman itu bagus, jumlah permintaan per detik tidak. Meskipun nol permintaan per detik menunjukkan ada yang salah.

Keuntungan layanan adalah mereka menawarkan kecerdasan tambahan secara langsung. Saya umumnya menyukai Datadog. Layanan bisa sangat mahal jika Anda memiliki banyak data, dan terkadang memiliki model harga yang tidak ramah cloud, misalnya menagih per instans, padahal instans bersifat dinamis. Ada juga perbedaan antara layanan di mana setiap permintaan berasal dari pengguna berbayar dan yang terkait iklan, sehingga hanya persentase kecil permintaan yang menghasilkan uang. Anda bisa berakhir dengan banyak data dan anggaran yang tidak banyak.

Saya mengerjakan beberapa layanan yang menerima 1 miliar permintaan per hari, jadi masuk akal untuk meng-host sendiri pemantauan dan pencatatan log kami. Jika volume Anda lebih rendah, maka layanan yang di-hosting lebih mudah.


### Layanan AWS beragam hasilnya

Pengalaman saya dengan layanan AWS beragam. Layanan Elasticsearch mereka tidak stabil, jadi kami menjalankan instans sendiri untuk itu. Metrik CloudWatch mahal, jadi kami umumnya hanya menggunakannya untuk metrik tingkat "infrastruktur" bukan aplikasi, yaitu metrik terkait kesehatan di mana AWS dapat mengetahui lebih baik apa yang terjadi daripada perangkat lunak yang berjalan di instans. CloudWatch Logs bisa lambat diperbarui dan tidak memiliki banyak metadata. Menjalankan ELK membantu hal itu. Jika saya benar-benar menginginkan data real time, maka menggunakan Kafka sebagai transport untuk log lebih baik. Itu cukup baik didukung oleh Logstash. Mengelola klaster Kafka bukan untuk yang berhati lemah, banyak sekali pipa yang terekspos.


### Kafka

Komentar: Kafka kadang bisa sangat rumit, atau Kafka bisa sangat kokoh sehingga Anda hampir lupa bahwa ia ada di sana mengikat segalanya. 


Komentar: Kafka kokoh, tetapi butuh banyak pekerjaan yang mengejutkan untuk menjalankannya. Saya menganggapnya seperti basis data relasional tetapi Anda hanya bekerja pada lapisan "fisik", misalnya tablespace, file, dan partisi. Ada beberapa saat di awal ketika utilitas manajemen kurang, dan kami harus menulis program untuk misalnya mereset consumer group. http://howfuckedismydatabase.com/nosql/

Komentar: Kami menggunakan Kafka sebagai "buffer" untuk pesan log dan tempat di mana kami dapat melakukan pemrosesan aliran real time pada data yang berasal dari beberapa server. Jika kami mendapat serangan DDOS, maka kami membutuhkan cara menganalisis data di beberapa instans. Jika kami mencatat log langsung dari server ke ELK, beban dapat meledakkan klaster Elasticsearch.

Komentar: Kafka bagus untuk kami karena jika kami mendapat serangan DDOS, maka kami membutuhkan cara menganalisis data di beberapa instans. Jika kami mencatat log langsung dari server ke ELK, beban dapat meledakkan klaster Elasticsearch.


Komentar: Kafka bekerja lebih sedikit dan lebih efisien, sehingga dapat menangani beban dengan lebih baik. Dan kami mengantrekan pekerjaan Kafka dan mencoba ulang. Dan Kafka yang kelebihan beban tidak memengaruhi pengguna yang mencoba melakukan pekerjaan interaktif dengan Kibana, seperti yang terjadi jika Elasticsearch kesulitan.

Komentar:  Pemrosesan aliran sebagian besar mencari penyalahgunaan, misalnya terlalu banyak lalu lintas dari satu IP di seluruh klaster, lalu membagikan pemblokiran ke seluruh klaster.

Komentar: Plugin logstash-output-kafka cukup tidak andal saat ini. Saya telah terkena beberapa masalah di halaman GitHub issues-nya, yang tampaknya tidak pernah diperbaiki. Saya ingin beralih dari menggunakannya, ke mengirim langsung dari aplikasi kami ke Kafka.

Komentar: Kami sekarang mengirim event terstruktur langsung dari aplikasi ke Kafka. Motivasi utamanya adalah menyentuh data log lebih sedikit dan menghindari pembacaan dan penulisan disk berkali-kali. Pada sistem bervolume tinggi, pencatatan log dapat memerlukan kerja lebih banyak daripada aplikasinya sendiri. Saya juga berpikir untuk membuat journald mengirim log langsung, dari program C.


### Loki

Awasi Loki dengan saksama. Loki belum siap tetapi ketika sudah siap saya berharap akan lebih cocok dalam tumpukan ini. Loki adalah agregator log yang dibuat oleh grafana labs, menggunakan sintaks scraping dan tag yang serupa dengan Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager untuk metrik. Cinta Prometheus.

Rollbar/Graylog untuk pencatatan log/pelaporan kesalahan (ada sedikit tumpang tindih di sini; layanan kecil mungkin tidak membutuhkan keduanya).

Saat ini, peringatan hanya masuk ke salah satu dari beberapa saluran Slack yang notifikasinya diaktifkan oleh pihak-pihak yang berkepentingan. Jika kami lebih serius soal on-call, peringatan akan masuk ke PagerDuty/VictorOps/dll.

Grafana untuk grafik dan dasbor. Juga dengan antusias menantikan apakah fasilitas pencatatan log mereka yang akan datang akan membuat Graylog tidak diperlukan.


### Thanos

Kami menggunakan Thanos sebagai front-end untuk penyiapan HA kami. Thanos tahu cara menghilangkan duplikasi pasangan HA.

Saat ini kami menyimpan 6 bulan data Prometheus lokal. Ini bekerja cukup baik untuk kami. Tetapi saya sedang dalam proses meluncurkan penyimpanan bucket ke penyiapan Thanos kami untuk penyimpanan data jangka panjang. Secara teori, penyimpanan GCS akan sekitar 30% lebih murah daripada persistent disk standar GCE yang kami gunakan saat ini.

Kami tidak mencadangkan data Prometheus saat ini. Data tersebut sebenarnya tidak terlalu penting bagi kami selain cukup untuk peringatan. Deployment armada kami secara keseluruhan berubah begitu banyak dari tahun ke tahun sehingga data historis yang lebih tua dari beberapa bulan tidak terlalu menarik. Mungkin menarik untuk memiliki beberapa statistik inti dari tahun ke tahun, saya mungkin menyiapkan kumpulan aturan perekaman statistik inti dan menyimpannya dengan Federation atau membiarkan Thanos mengurusnya.

EDIT: Penafian kecil, saya pengembang Prometheus.


### Prometheus HA

HA di Prometheus dilakukan dengan duplikasi: Anda menjalankan beberapa pengumpul, ada cara untuk mengumpulkan dari beberapa dan menghilangkan duplikasi data.

Penskalaan dilakukan dengan menentukan jaringan dan meminta Prometheus yang berbeda mengumpulkan dari bagian jaringan yang berbeda.

Penyimpanan jangka panjang bukan kekuatan Prometheus tetapi dialihkan ke sesuatu seperti influx atau timescaledb (yang secara teknis juga memenuhi centang HA). Artikel yang saya baca tentang itu https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Belum mencoba bagian jangka panjang karena saya masih bereksperimen dan menggunakannya untuk grafik jangka pendek sementara librenms memantau jaringan saya untuk jangka panjang


###  Datadog + PagerDuty + Threat Stack

Kami menggunakan Datadog (dengan PagerDuty) dan Threat Stack dan tidak bisa lebih bahagia. Satu-satunya keluhan saya tentang DD adalah biaya penyimpanan metrik yang relatif tinggi.


### Zabbix

Zabbix dengan skrip kustom untuk memantau hampir segalanya. Bekerja seperti pesona.


### Outlyer

Saya menggunakan Outlyer, tetapi saya harus menyatakan bahwa saya bekerja di sini, dan memakai produk sendiri (dog fooding) itu wajib.

Masih membutuhkan Graylog, Sentry, dan Statuscake untuk meningkatkan.

Terdengar bias, tetapi setelah dengan senang hati menjalankan Nagios dan sistem pemantauan lain secara internal, saya akan membeli solusi yang di-hosting di pekerjaan baru mana pun dan melepaskan kerepotan itu.


### Nagios + Nagiosgraph

Kami menjalankan Nagios untuk semua pemantauan dan peringatan. Peringatan terjadi melalui e-mail (peringatan dan notifikasi kritis) dan notifikasi aplikasi yang dapat didengar (untuk peringatan kritis).

Nagiosgraph digunakan untuk visualisasi.

Penyiapan ini sangat efektif dalam menjaga kami tetap mendapat informasi secara menyeluruh tentang apa yang terjadi di lingkungan kami. Kami menjalankan dan memantau sekitar 110 server yang kritis bagi misi dan sekitar 760 titik data, dan telah memiliki sistem pagi ini selama lebih dari tujuh tahun.

Saya juga ingin mengagregasi log dengan Graylog atau ELk di suatu saat.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager melalui helm chart Prometheus Operator yang luar biasa. Log masih masuk ke paket LogDNA birch karena kami menyadari ELK terlalu berat untuk klaster kami yang sederhana dengan min 3 maks 5 node di GKE.


### DataDog + Sentry + PagerDuty.

Dulu saya menjalankan semua solusi pemantauan saya sendiri menggunakan berbagai macam perangkat lunak termasuk Nagios, Icinga, Zabbix, ELK, Greylog2, Influx, dan banyak alat lainnya, tetapi kenyataannya terlalu banyak upaya yang terlibat dalam menjalankan infrastruktur pemantauan sendiri, terutama ketika Anda dapat membayar orang lain dengan tarif yang sangat rendah untuk melakukannya bagi Anda!

Membayar orang lain untuk menjalankan infrastruktur pemantauan membebaskan klien saya untuk fokus menjalankan platform mereka daripada memantau pemantauan, yang berarti nilai yang mereka peroleh dari stabilitas platform mereka jauh melebihi biaya apa pun dari Pemantauan sebagai Layanan.


### Sensu + Graphite + ELK

Perusahaan saya sangat menyukai hal-hal yang di-hosting sendiri.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager untuk peringatan, tim saya percaya bahwa pemantauan yang sederhana adalah pemantauan yang baik.

Sistem lain seperti pencatatan log dan pelacakan (tracing) akan memberikan konteks yang kaya untuk diagnosis ketika orang yang bertugas on-call menerima peringatan, tetapi kami tidak pernah membangun peringatan di atasnya.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Layanan yang diinstrumentasi Prometheus => analitik dan visualisasi Circonus


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Kami menggunakan layanan berikut:

icinga2 untuk pemantauan dan VictorOps untuk peringatan

NewRelic untuk pemantauan rinci layanan

Sentry untuk pelacakan kesalahan dalam layanan

Slack/Email adalah bagian dari peringatan yang dipicu dari NewRelic atau icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 dengan integrasi elasticsearch untuk analisis dan integrasi graphite+grafana untuk grafik.

berkat fleksibilitas aturan apply di icinga2, pengembang hanya dapat melihat layanan yang notifikasinya mereka terima.

dan melalui icinga2 director, programmer dapat dengan mudah mendefinisikan pemeriksaan mereka sendiri (yang mereka lakukan, setiap beberapa hari - 100 pemeriksaan keluar, 100 pemeriksaan lain masuk) dalam skala besar tanpa repot.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Apa yang kami miliki sekarang:

DataDog untuk metrik

New Relic untuk pemantauan aplikasi

ELK (Elastic Search + Logstash + Kibana) untuk log

Sentry (di-hosting sendiri) untuk mencatat pengecualian

Email + Slack + VictorOps untuk peringatan (berdasarkan tingkat keparahan)

Apa yang ingin kami miliki:

Prometheus untuk metrik (Grafana untuk visualisasi)

New Relic (mungkin Elastic Search APM) untuk pemantauan aplikasi

EFK (elastic search + fluentd + kibana) untuk pencatatan log. Mungkin, Loki dari Grafana akan siap produksi pada saat kami sampai di sana

Sentry untuk pengecualian

Alertmanager + email + VictorOps untuk peringatan


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Penafian: bekerja di VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf untuk metrik server seperti CPU, Disk, Memori, dan Jaringan. Kami juga menggunakan Telegraf untuk pemantauan SNMP perangkat jaringan kami.

Prometheus untuk metrik aplikasi. Kami menulis kode pemeriksaan kesehatan ke dalam aplikasi kami yang di-scrape oleh Prometheus.

InfluxDB untuk penyimpanan deret waktu. Di sinilah data Telegraf kami dikirim.

Grafana untuk dasbor dan peringatan. Mesin peringatan tidak terlalu tangguh, tetapi cukup menjalankan tugasnya. Kami juga mengirim peringatan ke Slack.

Yang belum saya miliki saat ini adalah solusi pencatatan log terpusat. ELK kuat tetapi sulit disiapkan dan dikelola, dan saya tidak tahu alternatif gratis yang cukup dekat untuk diteliti.


### Sematext + Logagent + Experience

Sematext untuk metrik, untuk log, untuk trace, dan segera untuk pemantauan pengguna nyata juga. Lebih sederhana/murah daripada menggunakan N alat/layanan yang berbeda, menurut pendapat saya.

Untuk pengiriman log kami dulu menggunakan rsyslog dan kemudian beralih ke Logagent.

Untuk pelaporan crash frontend kami menggunakan Sentry, tetapi kami akan segera beralih ke Experience.

Penafian: Saya seorang Sematextan.


### Azure Monitor/Analytics + OpsGenie

Saya berharap Log Analytics memiliki antarmuka yang lebih baik. Kami beralih dari splunk, yang jauh lebih mudah dinavigasi.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Anda benar-benar tidak ingin menjalankan sistem notifikasi sendiri. Anda dapat mengganti Splunk dengan ELK kecuali tim Keamanan Anda lebih menyukai Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf sebagai pengumpul, Prometheus + Alertmanager untuk pemantauan dan peringatan, terintegrasi dengan saluran slack dan pagerduty untuk peringatan kritis. Grafana untuk visualisasi metrik host.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus untuk metrik + peringatan

Grafana untuk dasbor Prometheus

Cloudwatch memantau instans Prometheus

sentry untuk pelacakan pengecualian

kibana + elasticsearch

graylog

prometheus Push Gateway untuk batch/cronjob

SOP https://github.com/rapidloop/sop untuk "mendorong/meneruskan" metrik dari 1 instans Prometheus ke instans lain

klien menggunakan klien Prometheus. Kami mencoba menggunakan opencensus.io di sisi klien


### PagerDuty + Monitis

PagerDuty + Monitis. Juga beberapa Azure Functions khusus untuk menguji kesehatan beberapa layanan.

Berharap memperkenalkan Prometheus dan Grafana tahun ini


### Prometheus + Grafana + Bosun

Prometheus untuk menyimpan data deret waktu. Grafana untuk visualisasi. Bosun untuk manajemen peringatan.


### Azure Monitor/Analytics/Insights/Dashboards

Toko khusus Azure, Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana untuk memantau layanan kontainer di Kubernetes melalui Prometheus

Monitis untuk pemantauan layanan end-to-end terutama untuk API web dan aplikasi web

OpsGenie untuk manajemen peringatan

Slack untuk mendapatkan informasi status dari sistem kami


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Insinyur (dev)ops lama di sini. Dibesarkan dengan Nagios. Ingin sekali mendengar pendapat tentang SaaS saya yang dibiayai sendiri https://checklyhq.com. Kami melakukan pemantauan API & pemantauan transaksi situs dengan peringatan yang cukup mendalam.

Saya memulai Checkly karena pemantauan aktif / sintetis di ranah API agak terbatas (dan mahal). Pemantauan berbasis browser / berskrip bahkan lebih proprietari dan mahal. Kami menggunakan Puppeteer dan menjaga harga serendah mungkin.

Tumpukan pemantauan kami:

Checkly (dog fooding...)

AppOptics (grafik kustom)

AWS Cloudwatch & SNS untuk pesan SMS.

peringatan Heroku bawaan.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana memberi kami peringatan di slack tentang masalah infrastruktur atau penurunan kinerja, dan kami telah mengonfigurasi logz.io untuk memberi peringatan di slack pada volume tertentu log tingkat kesalahan dari lapisan aplikasi.


### SignalFX + Splunk + PagerDuty + Slack

Saat ini menggunakan: SignalFX, Splunk, PagerDuty, dan Slack. Saya bukan penggemar berat SignalFX meskipun tim dukungan mereka sangat ramah dan responsif. Saya menyukai Splunk (sepadan jika Anda mampu membayarnya), PagerDuty, dan Slack.

Dulu saya menggunakan tumpukan TICK di mana sebagian besar C sebenarnya adalah G, yaitu Grafana meskipun saya sedikit menggunakan Chronograf. Itu luar biasa tetapi merepotkan untuk dikelola. Dilema klasik SaaS vs hosting sendiri.

Saya telah menggunakan DataDog, New Relic, Graylog, ELK, dan BugSnag. Saya sangat menyukai DataDog dan New Relic, Graylog cukup bagus. Saya bukan penggemar berat ELK. BugSnag bagus, saya sebenarnya merasa bahwa pelacakan kesalahan/pengecualian adalah pengganti yang cukup baik untuk pemantauan log penuh, dalam banyak kasus.


### ELK + Prometheus + Grafana

Seperti yang lain, kami menggunakan ELK untuk log dan Prometheus+Grafana untuk yang lainnya.

Memelihara penyiapan ini mudah jika Anda mengizinkan diri sendiri sesekali kehilangan data. Misalnya, jika basis data ElasticSearch kami bermasalah (yang sayangnya terjadi setiap 2-3 bulan pada kami) kami tidak repot dengan HA dan sebagai gantinya membuang data dan melanjutkan hidup. Jika Anda mutlak harus memiliki HA atau retensi jangka panjang, semoga berhasil.


### Datadog + Prometheus + Grafana

Saya menyiapkan Datadog secara bulan ke bulan karena ketika saya tiba di sini, tidak ada pemantauan dan tidak ada peringatan. Hanya beberapa situs kami yang dipantau setiap 5 menit untuk uptime. Datadog tanpa ragu paling mudah disiapkan. Ketika saya selesai menangani semua masalah lainnya, saya akan beralih ke Prometheus+Grafana. Belum 100% memutuskan tentang manajemen log.

### Nagios + ELK

Kami mendukung lebih dari 100+ produk.

Untuk on-prem, kebanyakan Nagios dan ELK. Untuk cloud, kami bermigrasi dari DataDog ke NewRelic.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Kami dulu menggunakan datadog tetapi merasa terlalu mahal untuk kebutuhan kami. Jangan salah paham, ini luar biasa tetapi biayanya sangat besar. Kami berhasil menyiapkan site24x7.com dengan langganan tahunan sekitar 2-3 bulan biaya dari DD.

Tumpukan pemantauan kami:

Site24x7 - APM, pemantauan URL eksternal, pemantauan aliran email SMTP, kedaluwarsa ssl, dan pemantauan proses.

StatusCake - untuk pemantauan dan konfirmasi URL - Ini adalah cadangan kami seandainya site24x7 melewatkan sesuatu (tidak pernah) tetapi SC lebih fleksibel untuk pemantauan port dan layanan eksternal untuk kebutuhan kami.

Kedua alat mengeskalasi ke PagerDuty, dan kemudian kami mendapatkan eskalasi kami di slack.

SumoLogic - untuk pemantauan log (alat yang hebat tetapi agak rumit untuk kebutuhan kami)

Dari slack kami dapat ack, atau memperbaiki peringatan.

Kami kemudian memiliki banyak otomatisasi site24x7 yang terhubung ke commando.io untuk apa yang kami sebut 'BedOps' - di mana peringatan dipicu, kami menjalankan beberapa skrip atau otomatisasi sebagai upaya memperbaiki situasi (99% dari waktu otomatisasi + skrip kami menjauhkan kami dari masalah)

Kami memiliki runbook internal di KB kami untuk saat otomatisasi gagal atau ada sesuatu di luar cakupan yang perlu diperbaiki.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana untuk metrik di klaster GKE dan VM kami.

Google Stackdriver untuk Log (karena sudah termasuk dan aktif secara default dan saat ini cukup untuk kebutuhan kami).


### Zabbix

Zabbix untuk segalanya. Tidak perlu perangkat lunak tambahan.
