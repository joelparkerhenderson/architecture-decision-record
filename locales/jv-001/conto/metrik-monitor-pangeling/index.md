# Metrik, monitor, pangeling

Isi:

* [Ringkesan](#ringkesan)
  * [Masalah](#masalah)
  * [Keputusan](#keputusan)
  * [Status](#status)
* [Rincian](#rincian)
  * [Anggepan](#anggepan)
  * [Watesan](#watesan)
  * [Posisi](#posisi)
  * [Argumentasi](#argumentasi)
  * [Implikasi](#implikasi)
* [Gegayutan](#gegayutan)
  * [Keputusan gegayutan](#keputusan-gegayutan)
  * [Kabutuhan gegayutan](#kabutuhan-gegayutan)
  * [Artefak gegayutan](#artefak-gegayutan)
  * [Prinsip gegayutan](#prinsip-gegayutan)
* [Cathetan](#cathetan)
  * [Pesen teks bebas utawa pesen event terstruktur](#pesen-teks-bebas-utawa-pesen-event-terstruktur)
  * [Graylog luwih gampang](#graylog-luwih-gampang)
  * [Prometheus butuh sawetara penyetelan](#prometheus-butuh-sawetara-penyetelan)
  * [Layanan AWS campuran](#layanan-aws-campuran)
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


## Ringkesan


### Masalah

Kita pengin nggunakake metrik, monitor, lan pangeling, amarga kita pengin ngerti sepira apik aplikasi kita makarya, lan ngerti nalika ana masalah.


### Keputusan

WIP.


### Status

Ngumpulake informasi. Kita miwiti saka ujung-ujung spektrum sing masuk akal: piranti gratis lawas sing paling disaranake (Nagios) lan piranti mbayar anyar sing paling disaranake (New Relic).


## Rincian


### Anggepan

Kita pengin nggawe aplikasi web sing modern, cepet, bisa dipercaya, responsif, lan sapanunggalane.

Kita pengin tuku tinimbang mbangun.


### Watesan

Kita pengin piranti sing makarya apik karo pipeline devops lan cloud deployment kita.


### Posisi

Kita lagi nyinaoni posisi saiki.


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

  

  
### Argumentasi

Nganti saiki, Nagios lan New Relic yaiku ujung-ujung spektrum. Nagios piranti paling lawas, paling prasaja, gratis, lan bisa dilakoni. New Relic piranti paling anyar fitur, paling lengkap, mbayar, lan bisa dilakoni. Kita bakal miwiti kanthi ngevaluasi loro kuwi. Yen perlu, kita bakal pindhah menyang tengah spektrum.  

Nganti saiki, Zabbix nduwe rekomendasi paling apik, lan uga nawakake kemampuan paling lengkap.

Nganti saiki, ELK nduwe popularitas open-source build-tinimbang-tuku paling apik.

Nganti saiki, Prometheus + Graphana nduwe popularitas paling apik.


### Implikasi

TODO.


## Gegayutan


### Keputusan gegayutan

Pilihan-pilihan iki bakal mengaruhi kemampuan diuji, telemetri, lan mbok menawa sistem liyane kayata layanan pelanggan, rekayasa keandalan situs, lan sapanunggalane.


### Kabutuhan gegayutan

TODO.


### Artefak gegayutan

TODO.


### Prinsip gegayutan

Gampang dibatalake.

Perlu kacepetan.


## Cathetan

Tumpukan open source sing lumayan apik yaiku:

* Prometheus kanggo metrik lan pangeling adhedhasar metrik

* Grafana kanggo nuduhake metrik

* Elasticsearch/Logstash/Kibana (ELK) kanggo log lan event terstruktur

* Pushover kanggo kabar seluler


### Pesen teks bebas utawa pesen event terstruktur

Pesen teks bebas: upamane, perkara acak sing bakal kok temokake ing /var/log/messages, lan perkara sing digawe sengaja dening aplikasi. Pesen iki migunani kanggo ngenali perkara liya sing kedadeyan ing mesin kayata kehabisan memori utawa kesalahan hardware, nanging akeh sampah. 

Pesen event terstruktur: digawe dening aplikasi, kanthi kumpulan atribut tetep utawa dinamis, upamane log panjalukan HTTP, log akuntansi, login pangguna.

Umume, apik yen nyathet rincian saben panjalukan kanthi cara sing bisa kok telusuri adhedhasar atribut. Dadi nambah upamane userid utawa sessionid ing kabeh ngidini kowe nglacak. Pelacakan eksplisit uga apik, mesthi. Nggunakake ELK kanggo iki kaya versi mlarat saka https://www.honeycomb.io/


### Graylog luwih gampang

Graylog luwih gampang diuripake miturut pengalamanku.


### Prometheus butuh sawetara penyetelan

Aku umume seneng karo Prometheus kanggo metrik. Pangeling butuh sawetara penyetelan, nanging lumayan apik. Gumantung aplikasimu. Aku mikir paling apik ngeling kahanan sing katon marang pangguna pungkasan, dudu panyebab dhasare. Upamane, wektu pemuatan kaca apik, jumlah panjalukan saben detik ora. Sanajan nol panjalukan saben detik nuduhake ana sing salah.

Kaluwihan layanan yaiku dheweke nawakake kecerdasan tambahan langsung saka kothak. Aku umume seneng Datadog. Layanan bisa larang banget yen kowe nduwe data akeh, lan kadhang nduwe model rega sing ora ramah cloud, upamane nagih saben instans, nalika instans iku dinamis. Uga ana bedane antarane layanan ing ngendi saben panjalukan saka pangguna mbayar lan sing gegayutan karo iklan, mula mung persentase cilik panjalukan sing ngasilake dhuwit. Kowe bisa pungkasane duwe data akeh nanging anggaran ora sepira.

Aku makarya ing sawetara layanan sing nampa 1 milyar panjalukan saben dina, mula masuk akal ngosting monitoring lan logging dhewe. Yen volumemu luwih sithik, layanan hosted luwih gampang.


### Layanan AWS campuran

Pengalamanku karo layanan AWS campuran. Layanan Elasticsearch-e ora stabil, mula kita nglakokake instans dhewe kanggo kuwi. Metrik CloudWatch larang, mula kita umume mung nggunakake kanggo metrik tingkat "infrastruktur" tinimbang aplikasi, yaiku metrik gegayutan kesehatan ing ngendi AWS bisa luwih ngerti apa sing kedadeyan tinimbang piranti lunak sing mlaku ing instans. Log CloudWatch bisa alon dianyari lan ora nduwe metadata sepira. Nglakokake ELK mbiyantu babagan iki. Yen aku tenan pengin data real time, nggunakake Kafka minangka transpor kanggo log luwih apik. Iku didhukung cukup apik dening Logstash. Ngatur klaster Kafka ora kanggo wong sing atine ciut, amarga akeh pipa sing kapapar.


### Kafka

Komentar: Kafka bisa angel banget kadhang, utawa Kafka bisa kuwat kaya watu lan kowe meh lali yen ana sing nyambungake kabeh.


Komentar: Kafka wis kuwat, nanging butuh pagaweyan sing ngagetake kanggo miwiti. Aku nganggep kaya basis data relasional nanging kowe mung makarya ing lapisan "fisik", upamane tablespace, berkas lan partisi. Ana sawetara wektu ing awal ing ngendi utilitas manajemen kurang, lan kita kudu nulis program kanggo upamane ngreset consumer group. http://howfuckedismydatabase.com/nosql/

Komentar: Kita nggunakake Kafka minangka "buffer" kanggo pesen log lan panggonan ing ngendi kita bisa nindakake pangolahan stream real time marang data sing teka saka pirang-pirang server. Yen kita nampa serangan DDOS, kita butuh cara nganalisis data ing pirang-pirang instans. Yen kita nglog langsung saka server menyang ELK, beban bisa njeblugake klaster Elasticsearch.

Komentar: Kafka apik kanggo kita amarga yen kita nampa serangan DDOS, kita butuh cara nganalisis data ing pirang-pirang instans. Yen kita nglog langsung saka server menyang ELK, beban bisa njeblugake klaster Elasticsearch.


Komentar: Kafka nindakake pagaweyan luwih sithik lan luwih efisien, mula bisa nangani beban luwih apik. Lan kita antri pagaweyan Kafka lan nyoba maneh. Lan Kafka sing kebebanan ora mengaruhi pangguna sing nyoba makarya interaktif karo Kibana, kaya sing bakal kedadeyan yen Elasticsearch lagi kangelan.

Komentar:  Pangolahan stream umume nggoleki penyalahgunaan, upamane lalu lintas kakehan saka siji IP ing kabeh klaster, banjur nuduhake blokir ing kabeh klaster.

Komentar: Plugin logstash-output-kafka cukup ora bisa dipercaya saiki. Aku wis kena sawetara masalah ing kaca masalah GitHub-e, sing kayane ora tau didandani. Aku pengin ninggalake nggunakake kuwi, lan ngirim langsung saka aplikasi kita menyang Kafka.

Komentar: Saiki kita ngirim event terstruktur langsung saka aplikasi menyang Kafka. Motivasi utama yaiku nutul data log kanthi luwih sithik lan nyingkiri maca lan nulis disk kaping pirang-pirang. Ing sistem volume dhuwur, logging bisa mbutuhake pagaweyan luwih akeh tinimbang aplikasi dhewe. Aku lagi mikirake supaya journald ngirim log langsung uga, saka program C.


### Loki

Awasen Loki kanthi cedhak. Durung siap nanging yen wis, aku ngarepake dheweke luwih cocog ing tumpukan iki. Loki yaiku agregator log sing digawe dening grafana labs, nggunakake sintaksis scraping lan tag sing padha karo Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

Prometheus + alertmanager kanggo metrik. <3 Prometheus.

Rollbar/Graylog kanggo logging/pelaporan kesalahan (ana tumpang tindih ing kene; layanan cilik mbok menawa ora butuh loro-lorone).

Saiki, pangeling mung menyang salah sawijining saluran Slack sing pihak kasengsem ngaktifake kabar. Yen kita luwih serius babagan on-call, bakal menyang PagerDuty/VictorOps/lan sapanunggalane.

Grafana kanggo grafik lan dashboarding. Uga ngarep-arep ndeleng apa fasilitas logging sing bakal teka bakal ngilangi kabutuhan Graylog.


### Thanos

Kita nggunakake Thanos minangka front-end kanggo setelan HA kita. Dheweke ngerti carane de-duplikasi pasangan HA.

Saiki kita nyimpen 6 sasi data Prometheus lokal. Iki makarya cukup apik kanggo kita. Nanging aku lagi ing tengah nglakokake panyimpenan bucket menyang setelan Thanos kita kanggo panyimpenan data jangka dawa. Ing teori, panyimpenan GCS bakal kira-kira 30% luwih murah tinimbang disk persisten standar GCE sing kita gunakake saiki.

Kita ora nggawe backup data Prometheus saiki. Datane ora tenan penting kanggo kita ngluwihi cukup kanggo pangeling. Penyebaran armada kita sakabèhé owah akeh saben taun, mula data historis luwih saka sawetara sasi ora tenan menarik. Mbok menawa menarik duwe sawetara statistik inti taun-lawan-taun, aku mbok menawa nyetel kumpulan recording rule statistik-inti lan nyimpen karo Federation utawa mung supaya Thanos sing ngurus.

EDIT: Disklaimer cilik, aku pangembang Prometheus.


### Prometheus HA

HA ing Prometheus ditindakake kanthi duplikasi, kowe nglakokake pirang-pirang poller, ana cara kanggo poll pirang-pirang lan de-duplikasi data

Skala ditindakake kanthi mutusake jaringan lan duwe Prometheus beda sing poll bagean jaringan beda

Panyimpenan jangka dawa dudu kekuwatan Prometheus nanging dialihake menyang kayata influx utawa timescaledb (sing sacara teknis uga nyentang HA) artikel sing tak waca babagan iki https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Durung nyoba bab jangka dawa amarga aku isih mung eksperimen lan nggunakake kanggo grafik jangka cendhak nalika librenms ngawasi jaringanku kanggo jangka dawa


### Datadog + PagerDuty + Threat Stack

Kita nggunakake Datadog (karo PagerDuty) lan Threat Stack lan ora bisa luwih seneng. Siji-sijine keluhanku karo DD yaiku biaya panyimpenan metrik sing relatif dhuwur.


### Zabbix

Zabbix karo skrip khusus kanggo ngawasi meh kabeh. Makarya kaya pesona.


### Outlyer

Aku nggunakake Outlyer, nanging aku kudu ngaku yen aku makarya ing kene, lan dog fooding iku wajib.

Isih butuh Graylog, Sentry lan Statuscake kanggo nambah.

Muni bias, nanging sawise seneng nglakokake Nagios lan sistem monitoring liyane internal, aku bakal tuku solusi hosted ing pagaweyan anyar apa wae lan ngalih rasa sakit kuwi.


### Nagios + Nagiosgraph

Kita nglakokake Nagios kanggo kabeh monitoring lan pangeling. Pangeling kedadeyan liwat e-mail (kabar peringatan lan kritis) lan kabar aplikasi sing keprungu (kanggo pangeling kritis).

Nagiosgraph digunakake kanggo visualisasi.

Setelan iki wis efektif banget ing njaga kita tetep dikabari kanthi lengkap babagan apa sing kedadeyan ing lingkungan kita. Kita nglakokake lan ngawasi kira-kira 110 server kritis misi lan kira-kira 760 titik data, lan wis nduwe sistem esuk iki luwih saka pitung taun.

Aku uga pengin ngagregasi log karo Graylog utawa ELk ing sawetara titik.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager liwat helm chart Prometheus Operator sing apik banget. Log isih menyang plan birch LogDNA amarga kita weruh ELK kabotan banget kanggo min 3 max 5 simpul GKE kita sing sederhana.


### DataDog + Sentry + PagerDuty.

Aku biyen nglakokake kabeh solusi monitoring dhewe nggunakake macem-macem piranti lunak kalebu Nagios, Icinga, Zabbix, ELK, Greylog2, Influx, lan akeh piranti liyane, nanging sejatine upaya sing dibutuhake kanggo nglakokake infrastruktur monitoring dhewe kakehan, utamane yen kowe bisa mbayar wong liya kanthi rega murah supaya wong liya sing nindakake!

Mbayar wong liya kanggo nglakokake infra monitoring mbebasake klienku supaya fokus nglakokake platforme tinimbang ngawasi monitoring, tegese nilai sing dipikolehi saka stabilitas platforme ngungkuli biaya Monitoring as a Service.


### Sensu + Graphite + ELK

Perusahaanku seneng banget karo perkara self-hosted.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager kanggo pangeling, timku pitados yen monitoring prasaja iku monitoring apik.

Sistem liyane kayata logging lan tracing bakal nyedhiyakake konteks sugih kanggo diagnosis nalika on-call nampa pangeling, nanging kita ora tau mbangun pangeling ing kuwi.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Layanan sing diinstrumentasi Prometheus => analitik lan visualisasi Circonus


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Kita nggunakake layanan ing ngisor iki:

icinga2 kanggo monitoring lan VictorOps kanggo pangeling

NewRelic kanggo monitoring rinci layanan

Sentry kanggo nglacak kesalahan ing layanan

Slack/Email minangka bagean pangeling sing dipicu saka NewRelic utawa icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 karo integrasi elasticsearch kanggo analisis lan integrasi graphite+grafana kanggo grafik.

amarga keluwesan apply rule ing icinga2, pangembang mung bisa ndeleng layanan sing dheweke nampa kabar.

lan liwat icinga2 director, programmer bisa kanthi gampang nemtokake pamriksan dhewe (sing ditindakake saben pirang dina - 100 pamriksan metu, 100 pamriksan liyane mlebu) ing skala gedhe tanpa repot.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Apa sing kita duwe saiki:

DataDog kanggo metrik

New Relic kanggo monitoring aplikasi

ELK (Elastic Search + Logstash + Kibana) kanggo log

Sentry (self-hosted) kanggo nglog pengecualian

Email + Slack + VictorOps kanggo pangeling (adhedhasar keabotan)

Apa sing kita pengin duwe:

Prometheus kanggo metrik (Grafana kanggo visualisasi)

New Relic (mbok menawa Elastic Search APM) kanggo monitoring aplikasi

EFK (elastic search + fluentd + kibana) kanggo logging. Mbok menawa, Loki saka Grafana bakal siap-prod nalika kita tekan kana

Sentry kanggo pengecualian

Alertmanager + email + VictorOps kanggo pangeling


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Disklaimer: makarya ing VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf kanggo metrik server kayata CPU, Disk, Memori lan Jaringan. Kita uga nggunakake Telegraf kanggo monitoring SNMP piranti jaringan kita.

Prometheus kanggo metrik aplikasi. Kita nulis pamriksan kesehatan ing aplikasi kita sing di-scrape Prometheus.

InfluxDB kanggo panyimpenan time-series. Ing kene data Telegraf kita dikirim.

Grafana kanggo dashboard lan pangeling. Mesin pangeling ora kuwat banget, nanging bisa nindakake tugas. Kita uga ngirim pangeling menyang Slack.

Sing durung aku duwe saiki yaiku solusi logging terpusat. ELK kuwat nanging angel disetel lan diatur, lan aku ora ngerti alternatif gratis apa wae sing cukup cedhak kanggo dideleng.


### Sematext + Logagent + Experience

Sematext kanggo metrik, kanggo log, kanggo trace, enggal uga kanggo real user monitoring. Luwih prasaja/murah tinimbang nggunakake N piranti/layanan sing beda, miturut panemuku.

Kanggo ngirim log kita biyen nggunakake rsyslog banjur ngalih menyang Logagent.

Kanggo pelaporan crash frontend kita nggunakake Sentry, nanging kita bakal enggal ngalih menyang Experience.

Disklaimer: Aku wong Sematext.


### Azure Monitor/Analytics + OpsGenie

Muga-muga Log Analytics nduwe antarmuka sing luwih apik. Kita lagi ninggalake splunk, sing luwih gampang dinavigasi.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Kowe tenan ora pengin nglakokake sistem kabar dhewe. Kowe bisa ngganti Splunk karo ELK kajaba tim Keamananmu luwih seneng Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf minangka kolektor, Prometheus + Alertmanager kanggo monitoring lan pangeling, terintegrasi karo saluran slack lan pagerduty kanggo pangeling kritis. Grafana kanggo visualisasi metrik host.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus kanggo metrik + pangeling

Grafana kanggo dashboard Prometheus

Cloudwatch ngawasi instans Prometheus

sentry kanggo nglacak pengecualian

kibana + elasticsearch

graylog

prometheus Push Gateway kanggo batch/cronjob

SOP https://github.com/rapidloop/sop kanggo „push/forward“ metrik saka 1 instans Prometheus menyang liyane

klien nggunakake klien Prometheus. Kita nyoba nggunakake opencensus.io ing sisih klien


### PagerDuty + Monitis

PagerDuty + Monitis. Uga sawetara Azure Functions khusus kanggo nes kesehatan sawetara layanan.

Ngupayakake ngenalake Prometheus lan Grafana taun iki


### Prometheus + Grafana + Bosun

Prometheus kanggo nyimpen data time series. Grafana kanggo visualisasi. Bosun kanggo manajemen pangeling.


### Azure Monitor/Analytics/Insights/Dashboards

Toko mung Azure, Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana kanggo ngawasi layanan kontainer ing Kubernetes liwat Prometheus

Monitis kanggo monitoring layanan end-to-end utamane kanggo API web lan aplikasi web

OpsGenie kanggo manajemen pangeling

Slack kanggo entuk informasi status saka sistem kita


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Insinyur (dev)ops suwe ing kene. Digedhekake nganggo Nagios. Seneng entuk panemu babagan SaaS bootstrap-ku https://checklyhq.com. Kita nindakake monitoring API & monitoring transaksi situs kanthi pangeling sing cukup jero.

Aku miwiti Checkly amarga monitoring aktif / sintetis ing ruang API rada winates (lan larang). Monitoring adhedhasar browser / skrip malah luwih proprietari lan larang. Kita nggunakake Puppeteer lan njaga rega sakurang-kurange.

Tumpukan monitoring kita:

Checkly (dog fooding...)

AppOptics (grafik khusus)

AWS Cloudwatch & SNS kanggo pesen SMS.

pangeling Heroku bawaan.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana ngeling kita ing slack babagan masalah infrastruktur utawa degradasi kinerja, lan kita wis ngonfigurasi logz.io kanggo ngeling ing slack babagan volume log tingkat kesalahan tartamtu saka lapisan aplikasi.


### SignalFX + Splunk + PagerDuty + Slack

Saiki nggunakake: SignalFX, Splunk, PagerDuty lan Slack. Aku dudu penggemar gedhe SignalFX sanajan tim dhukungane ramah banget lan responsif. Aku seneng Splunk (sepadan yen kowe bisa mbayar), PagerDuty lan Slack.

Aku biyen nggunakake tumpukan TICK ing ngendi umume C sejatine G, yaiku Grafana sanajan aku nggunakake Chronograf sithik. Iku apik banget nanging angel diatur. Dilema klasik SaaS utawa self-hosting.

Aku wis nggunakake DataDog, New Relic, Graylog, ELK lan BugSnag. Aku seneng banget DataDog lan New Relic, Graylog lumayan apik. Aku dudu penggemar gedhe ELK. BugSnag apik, aku sejatine rumangsa nglacak kesalahan/pengecualian iku pengganti sing lumayan apik kanggo monitoring log lengkap, ing akeh kasus.


### ELK + Prometheus + Grafana

Kaya liyane, kita nggunakake ELK kanggo log lan Prometheus+Grafana kanggo kabeh liyane.

Njaga setelan iki gampang yen kowe menehi idin marang awakmu dhewe kanggo kadhang kelangan data. Upamane, yen basis data ElasticSearch kita kena masalah (sing kedadeyan saben 2-3 sasi kanggo kita sayange) kita ora repot karo HA lan malah mbuwang data lan nerusake urip. Yen kowe mesthi kudu duwe HA utawa retensi jangka dawa, sugeng ndhedher.


### Datadog + Prometheus + Grafana

Aku nyetel Datadog sasi-sasian amarga nalika aku teka ing kene, ora ana monitoring lan ora ana pangeling. Mung sawetara situs sing diawasi saben 5 menit kanggo uptime. Datadog tanpa mamang paling gampang disetel. Nalika aku rampung ngatasi kabeh masalah liyane, aku bakal ngalih menyang Prometheus+Grafana. Durung 100% mutusake babagan manajemen log.


### Nagios + ELK

Kita nduwe luwih saka 100+ produk sing didhukung.

Kanggo on-prem, umume Nagios lan ELK. Kanggo cloud, kita lagi migrasi saka DataDog menyang NewRelic.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Kita biyen nggunakake datadog nanging nemokake larang banget kanggo kabutuhan kita. Aja salah paham, iku apik banget nanging biayane gedhe. Kita bisa nyetel site24x7.com kanthi langganan taunan kira-kira 2-3 sasi biaya saka DD.

Tumpukan monitoring kita:

Site24x7 - APM, monitoring URL njaba, monitoring mailflow SMTP, kadaluwarsa ssl lan monitoring proses.

StatusCake - kanggo monitoring lan konfirmasi URL - Iki backup kita yen site24x7 kecolongan sawetara perkara (ora tau) nanging SC luwih fleksibel kanggo monitoring port lan layanan njaba kanggo kabutuhan kita.

Loro-lorone piranti eskalasi menyang PagerDuty, banjur kita nampa eskalasi ing slack.

SumoLogic - kanggo monitoring log (piranti apik nanging rada rumit kanggo kabutuhan kita)

Saka slack kita bisa ack, utawa ngatasi pangeling.

Kita banjur nduwe akeh otomatisasi site24x7 sing nyambung menyang commando.io kanggo 'BedOps' kaya sing kita sebut - ing ngendi pangeling kepicu, kita miwiti sawetara skrip utawa otomatisasi minangka upaya ngatasi kahanan (99% wektu otomatisasi + skrip kita njaga kita saka masalah)

Kita nduwe runbook internal ing KB kita kanggo nalika otomatisasi gagal utawa yen ana perkara ing njaba lingkup sing kudu didandani.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana kanggo metrik ing klaster GKE lan VM kita.

Google Stackdriver kanggo Log (amarga kalebu lan aktif kanthi bawaan lan saiki cukup kanggo kabutuhan kita).


### Zabbix

Zabbix kanggo kabeh. Ora perlu piranti lunak tambahan.
