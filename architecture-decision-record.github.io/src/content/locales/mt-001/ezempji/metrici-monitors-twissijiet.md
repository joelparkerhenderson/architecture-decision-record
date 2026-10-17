# Metriċi, monitors, twissijiet

Werrej:

* [Sommarju](#sommarju)
  * [Kwistjoni](#kwistjoni)
  * [Deċiżjoni](#deċiżjoni)
  * [Stat](#stat)
* [Dettalji](#dettalji)
  * [Suppożizzjonijiet](#suppożizzjonijiet)
  * [Restrizzjonijiet](#restrizzjonijiet)
  * [Pożizzjonijiet](#pożizzjonijiet)
  * [Argument](#argument)
  * [Implikazzjonijiet](#implikazzjonijiet)
* [Relatati](#relatati)
  * [Deċiżjonijiet relatati](#deċiżjonijiet-relatati)
  * [Rekwiżiti relatati](#rekwiżiti-relatati)
  * [Artefatti relatati](#artefatti-relatati)
  * [Prinċipji relatati](#prinċipji-relatati)
* [Noti](#noti)
  * [Messaġġi tat-test b'forma libera vs messaġġi strutturati ta' avvenimenti](#messaġġi-tat-test-bforma-libera-vs-messaġġi-strutturati-ta-avvenimenti)
  * [Graylog huwa eħfef](#graylog-huwa-eħfef)
  * [Prometheus jeħtieġ ftit irfinar](#prometheus-jeħtieġ-ftit-irfinar)
  * [Is-servizzi ta' AWS huma taħlita](#is-servizzi-ta-aws-huma-taħlita)
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


## Sommarju


### Kwistjoni

Irridu nużaw metriċi, monitors, u twissijiet, għax irridu nkunu nafu kemm l-applikazzjonijiet tagħna qed jaħdmu tajjeb, u nkunu nafu meta jkun hemm problema.


### Deċiżjoni

WIP.


### Stat

Qed niġbru informazzjoni. Qed nibdew mit-truf plawżibbli tal-ispettru: l-aktar għodda b'xejn eqdem rakkomandata (Nagios) u l-aktar għodda ġdida bi ħlas rakkomandata (New Relic).


## Dettalji


### Suppożizzjonijiet

Irridu noħolqu web apps li huma moderni, mgħaġġla, affidabbli, responsivi, eċċ.

Irridu nixtru aktar milli nibnu.


### Restrizzjonijiet

Irridu għodod li jaħdmu tajjeb mal-pipeline devops tagħna u mal-clouds tad-deployment tagħna.


### Pożizzjonijiet

Qed nagħmlu riċerka dwar il-pożizzjonijiet issa.


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

  

  
### Argument

S'issa, Nagios u New Relic huma t-truf tal-ispettru. Nagios huwa l-eqdem, l-aktar sempliċi, b'xejn, għodda vijabbli. New Relic huwa l-aktar bil-karatteristiċi l-ġodda, l-aktar komplut, bi ħlas, għodda vijabbli. Se nibdew bl-evalwazzjonijiet ta' dawn. Kif meħtieġ, se nimxu fi ħdan l-ispettru.  

S'issa, Zabbix għandu l-aqwa rakkomandazzjonijiet, u joffri wkoll il-kapaċitajiet l-aktar kompluti.

S'issa, ELK għandu l-aqwa popolarità open-source ta' bini minflok xiri.

S'issa, Prometheus + Graphana għandhom l-aqwa popolarità.


### Implikazzjonijiet

TODO.


## Relatati


### Deċiżjonijiet relatati

L-għażliet se jaffettwaw l-ittestjabbiltà, it-telemetrija, u x'aktarx sistemi oħra bħal dawk għas-servizz tal-klijenti, l-inġinerija tal-affidabbiltà tas-sit, eċċ.


### Rekwiżiti relatati

TODO.


### Artefatti relatati

TODO.


### Prinċipji relatati

Faċilment riversibbli.

Il-ħtieġa tal-veloċità.


## Noti

Stack open source pjuttost tajjeb huwa:

* Prometheus għal metriċi u twissijiet ibbażati fuq il-metriċi

* Grafana biex turi l-metriċi

* Elasticsearch/Logstash/Kibana (ELK) għal logs u avvenimenti strutturati

* Pushover għal notifiki mobile


### Messaġġi tat-test b'forma libera vs messaġġi strutturati ta' avvenimenti

Messaġġi tat-test b'forma libera: pereżempju, it-tip ta' affarijiet każwali li ssib f'/var/log/messages, u xi ħaġa ġġenerata apposta mill-applikazzjoni. Il-messaġġi huma utli biex jiġu identifikati affarijiet oħra li qed jiġru fuq il-magna bħal out of memory jew żbalji tal-hardware, iżda fihom ħafna ċraret. 

Messaġġi strutturati ta' avvenimenti: iġġenerati mill-applikazzjoni, b'sett fiss jew dinamiku ta' attributi, eż. log ta' talba HTTP, log tal-kontabilità, dħul ta' utent.

B'mod ġenerali, huwa sabiħ li jinżammu f'log id-dettalji dwar kull talba b'mod li tkun tista' tidħol fil-fond abbażi ta' attributi. Allura li żżid eż. userid jew sessionid ma' kollox jippermettilek tittraċċa. It-traċċar espliċitu huwa tajjeb ukoll, ovvjament. L-użu ta' ELK għal dan huwa xi ħaġa bħal https://www.honeycomb.io/ tal-fqir


### Graylog huwa eħfef

Graylog huwa eħfef biex titnissel mill-esperjenza tiegħi.


### Prometheus jeħtieġ ftit irfinar

Ġeneralment inkun kuntent b'Prometheus għall-metriċi. It-twissijiet jeħtieġu ftit irfinar, iżda huma pjuttost tajbin. Jiddependi mill-applikazzjoni tiegħek. Naħseb li l-aħjar li titwissa dwar kundizzjonijiet li jidhru lill-utent aħħari, mhux dwar il-kawżi sottostanti. Pereżempju, il-ħin tat-tagħbija tal-paġna huwa tajjeb, in-numru ta' talbiet kull sekonda le. Għalkemm żero talbiet kull sekonda jindika li xi ħaġa mhix sewwa.

Il-vantaġġ ta' servizz huwa li joffru intelliġenza addizzjonali lesta għall-użu. Ġeneralment inħobb Datadog. Is-servizzi jistgħu jkunu għalja b'mod tal-biża' jekk għandek ħafna data, u kultant ikollhom mudelli ta' prezzijiet li mhumiex favorevoli għall-cloud, eż. jiċċarġjaw għal kull istanza, meta l-istanzi huma dinamiċi. Hemm ukoll differenza bejn servizzi fejn kull talba tiġi minn utent li jħallas u oħrajn relatati mar-reklamar, għalhekk persentaġġ żgħir biss tat-talbiet jaqligħlek il-flus. Tista' tispiċċa b'ħafna data u mhux daqstant baġit.

Naħdem fuq xi servizzi li jirċievu biljun talba kuljum, għalhekk għandu sens li nospitaw il-monitoraġġ u l-logging tagħna stess. Jekk il-volumi tiegħek huma aktar baxxi, allura s-servizzi ospitati huma eħfef.


### Is-servizzi ta' AWS huma taħlita

L-esperjenza tiegħi b'servizzi ta' AWS kienet taħlita. Is-servizz Elasticsearch tagħhom kien instabbli, għalhekk inħaddmu l-istanzi tagħna stess għal dan. Il-metriċi ta' CloudWatch huma għaljin, għalhekk ġeneralment nużawhom biss għal metriċi ta' livell ta' "infrastruttura" aktar milli għall-applikazzjoni, jiġifieri metriċi relatati mas-saħħa fejn AWS jista' jkun jaf aħjar x'qed jiġri milli software li jaħdem fuq l-istanza. CloudWatch Logs jistgħu jkunu bil-mod biex jiġu aġġornati u m'għandhomx daqstant metadata. It-tħaddim ta' ELK jgħin f'dan. Jekk verament irrid data fi żmien reali, allura l-użu ta' Kafka bħala t-trasport għal-logs huwa aħjar. Dan huwa appoġġat pjuttost tajjeb minn Logstash. L-immaniġġjar ta' cluster Kafka mhuwiex għal min għandu qalb dgħajfa, madankollu, hemm ħafna plumbing espost.


### Kafka

Kumment: Kafka kultant jista' jkun tricky ħafna, jew Kafka jista' jkun solidu daqs blata u kważi tinsa li hemm, jorbot kollox flimkien. 


Kumment: Kafka kien solidu, imma kien ammont sorprendenti ta' xogħol biex titlaq. Naħseb fih bħal database relazzjonali imma int taħdem biss fis-saff "fiżiku", eż. tablespaces, fajls u partizzjonijiet. Kien hemm xi drabi kmieni fejn l-utilitajiet tal-ġestjoni kienu nieqsa, u kellna niktbu programmi biex eż. nerġgħu nissettjaw consumer group. http://howfuckedismydatabase.com/nosql/

Kumment: Nużaw Kafka bħala "buffer" għall-messaġġi tal-log u post fejn nistgħu nagħmlu stream processing fi żmien reali fuq data li ġejja minn servers multipli. Jekk niġu taħt attakk DDOS, neħtieġu mod kif niżanu d-data fuq istanzi multipli. Jekk nilloggjaw direttament mis-servers għal ELK, it-tagħbija tista' tfarrak il-cluster Elasticsearch.

Kumment: Kafka huwa tajjeb għalina għax jekk niġu taħt attakk DDOS, neħtieġu mod kif niżanu d-data fuq istanzi multipli. Jekk nilloggjaw direttament mis-servers għal ELK, it-tagħbija tista' tfarrak il-cluster Elasticsearch.


Kumment: Kafka jagħmel inqas xogħol u huwa aktar effiċjenti, għalhekk jista' jlaħħaq aħjar mat-tagħbija. U aħna ninfilaw ix-xogħol ta' Kafka u nipprovaw mill-ġdid. U li Kafka jkun sovraċċarġjat ma jaffettwax l-utenti li qed jippruvaw jaħdmu b'mod interattiv ma' Kibana, kif ikun jiġri jekk Elasticsearch ikun qed jitħabat.

Kumment:  L-istream processing l-aktar ifittex użu ħażin, eż. wisq traffiku minn IP wieħed fuq il-cluster kollu, u mbagħad naqsmu l-blokk fuq il-cluster kollu.

Kumment: Il-plugin logstash-output-kafka huwa pjuttost mhux affidabbli bħalissa. Ġejt mgħammad minn diversi problemi fuq il-paġna tal-issues tiegħu fuq GitHub, li donnhom qatt ma jiġu rranġati. Irrid nitbiegħed milli nużah, u nibgħat direttament mill-apps tagħna għal Kafka.

Kumment: Issa qed nibagħtu avvenimenti strutturati direttament mill-app għal Kafka. Il-motivazzjoni ewlenija kienet li nmissu d-data tal-log inqas drabi u nevitaw li naqraw u niktbu d-disk drabi multipli. F'sistemi b'volum għoli, il-logging jista' jieħu aktar xogħol mill-app innifisha. Qed naħseb li nagħmel journald jibgħat il-logs direttament ukoll, minn programm bl-C.


### Loki

Żomm għajnejk fuq Loki. Għadu mhux lest imma meta jkun nistenna li jkun adattat aħjar f'dan l-istack. Loki huwa aggregatur tal-logs maħluq minn grafana labs, juża sintassi simili ta' scraping u tags bħal Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

Prometheus + alertmanager għal metriċi. <3 Prometheus.

Rollbar/Graylog għal logging/rappurtar tal-iżbalji (hemm xi sovrapposizzjoni hawnhekk; servizz żgħir probabbilment m'għandux bżonn it-tnejn).

Bħalissa, it-twissijiet sempliċement imorru f'wieħed minn ftit kanali Slack li l-partijiet interessati għandhom in-notifiki mixgħula għalihom. Kieku konna aktar serji dwar l-on-call imorru għal PagerDuty/VictorOps/eċċ.

Grafana għal graffs u dashboarding. Nistenna wkoll bil-ħerqa nara jekk il-faċilitajiet tal-logging li ġejjin tagħhom humiex se jeliminaw il-ħtieġa ta' Graylog.


### Thanos

Nużaw Thanos bħala front-end għas-setup HA tagħna. Jaf kif jneħħi d-duplikati ta' pari HA.

Bħalissa qed inżommu 6 xhur ta' data lokali ta' Prometheus. Dan jaħdem raġonevolment tajjeb għalina. Imma jien f'nofs it-tnedija ta' bucket storage għas-setup Thanos tagħna għall-ħażna tad-data fit-tul. Fit-teorija, il-ħażna GCS se tkun madwar 30% irħas mid-disk persistenti standard ta' GCE li nużaw bħalissa.

Ma nagħmlux backup tad-data ta' Prometheus bħalissa. Id-data sempliċement mhijiex verament importanti għalina lil hinn milli jkollna biżżejjed għat-twissijiet. Id-deployment tal-flotta kollha tagħna jinbidel tant minn sena għal sena li data storika eqdem minn ftit xhur sempliċement mhijiex interessanti. Jista' jkun interessanti li jkollna ftit statistiċi ewlenin sena wara sena, nista' nissettja sett ta' recording rules tal-statistiċi ewlenin u naħżenhom b'Federation jew inħalli lil Thanos jieħu ħsiebhom.

EDIT: Dikjarazzjoni żgħira, jien żviluppatur ta' Prometheus.


### Prometheus HA

L-HA f'Prometheus isir bid-duplikazzjoni, taħdem poppers multipli, hemm modi biex tagħmel poll ta' multipli u tneħħi d-duplikati tad-data

L-iskalar isir billi tiddeċiedi n-netwerk u jkollok Prometheus differenti jagħmlu poll ta' partijiet differenti tan-netwerk

L-ħażna fit-tul mhijiex il-punt qawwi ta' Prometheus iżda tiġi mgħoddija lil xi ħaġa bħal influxes jew timescaledb (li teknikament jagħmel il-ħaġa tal-HA ukoll) artiklu li qrajt dwaru https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Għadni ma pprovajtx l-affarijiet tal-fit-tul għax għadni qed nesperimenta biss u qed nużah għal graffs għal żmien qasir filwaqt li librenms jimmonitorja n-netwerk tiegħi għal żmien twil


### Datadog + PagerDuty + Threat Stack

Nużaw Datadog (ma' PagerDuty) u Threat Stack u ma jistax ikollna aktar kuntentizza. L-uniku ilment tiegħi dwar DD huwa l-ispiża relattivament għolja tal-ħażna tal-metriċi.


### Zabbix

Zabbix b'scripts personalizzati biex jimmonitorja kważi kollox. Jaħdem bħal sħaru.


### Outlyer

Qed nuża Outlyer, imma għandi niddikjara li naħdem hawn, u l-użu tal-prodott tagħna stess huwa obbligatorju.

Għadni neħtieġ Graylog, Sentry u Statuscake biex insaħħaħ.

Jinstema' partiġjan, imma wara li ħaddimt Nagios u sistemi oħra ta' monitoraġġ internament b'mod kuntent, nixtri soluzzjoni ospitata f'kull xogħol ġdid u ninħeles minn dak l-uġigħ.


### Nagios + Nagiosgraph

Inħaddmu Nagios għall-monitoraġġ u t-twissijiet kollha. It-twissijiet isiru bl-email (twissijiet u notifiki kritiċi) u notifiki audibbli tal-app (għal twissijiet kritiċi).

Nagiosgraph jintuża għall-viżwalizzazzjonijiet.

Dan is-setup kien effettiv ħafna biex iżommna informati b'mod komprensiv dwar dak li qed jiġri fl-ambjent tagħna. Inħaddmu u nimmonitorjaw madwar 110 servers kritiċi għall-missjoni u madwar 760 punt tad-data, u għandna din is-sistema tas-sabiħ f'postha għal aktar minn seba' snin.

Nixtieq ukoll naqbad il-logs b'Graylog jew ELK f'xi punt.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager permezz tal-helm chart tal-Prometheus Operator mill-aqwa. Il-log għadu jmur għall-pjan birch ta' LogDNA għax innutajna li ELK huwa tqil wisq għan-nodi umli tagħna ta' min 3 u max 5 fuq GKE.


### DataDog + Sentry + PagerDuty.

Kont inħaddem is-soluzzjonijiet kollha tal-monitoraġġ tiegħi stess bl-użu ta' kull tip ta' software inkluż Nagios, Icinga, Zabbix, ELK, Greylog2, Influx, u ħafna għodod oħra, imma l-verità hi li hemm sforz kbir wisq biex tħaddem infrastruttura tal-monitoraġġ tiegħek stess, speċjalment meta tista' tħallas lil xi ħadd ieħor rati daqshekk baxxi biex jagħmel dan għalik!

Il-ħlas lil oħrajn biex iħaddmu l-infra tal-monitoraġġ jeħles lill-klijenti tiegħi biex jiffokaw fuq it-tħaddim tal-pjattaformi tagħhom minflok ma jimmonitorjaw il-monitoraġġ, li jfisser li l-valur li jiksbu mill-istabbiltà tal-pjattaforma tagħhom jisbaq ferm kwalunkwe spiża ta' Monitoraġġ bħala Servizz.


### Sensu + Graphite + ELK

Il-kumpanija tiegħi hija kbira ħafna fuq affarijiet self-hosted.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager għat-twissijiet, it-tim tiegħi jemmen li l-monitoraġġ sempliċi huwa monitoraġġ tajjeb.

Sistemi oħra bħall-logging u t-traċċar se jipprovdu kuntest rikk għad-dijanjożi meta l-on-call jirċievi twissija, iżda qatt ma nibnu t-twissijiet fuq dawn.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Servizzi strumentati b'Prometheus => analitika u viżwalizzazzjoni ta' Circonus


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Qed nużaw is-servizzi t'hawn taħt:

icinga2 għall-monitoraġġ u VictorOps għat-twissijiet

NewRelic għall-monitoraġġ dettaljat tas-servizz

Sentry għat-traċċar tal-iżbalji fis-servizz

Slack/Email huwa parti mit-twissijiet li jiġu attivati minn NewRelic jew icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 b'integrazzjoni ma' elasticsearch għall-analiżi u integrazzjoni ma' graphite+grafana għall-graffs.

grazzi għall-flessibbiltà tal-apply rules f'icinga2, l-iżviluppaturi jistgħu jaraw biss is-servizzi li jirċievu notifiki għalihom.

u permezz ta' icinga2 director, il-programmaturi jistgħu faċilment jiddefinixxu l-kontrolli tagħhom stess (li jagħmlu, kull ftit jiem - joħorġu 100 kontroll, jidħlu 100 kontroll ieħor) fuq skala kbira mingħajr xkiel.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

X'għandna issa:

DataDog għall-metriċi

New Relic għall-monitoraġġ tal-applikazzjoni

ELK (Elastic Search + Logstash + Kibana) għal-logs

Sentry (self-hosted) għall-logging tal-eċċezzjonijiet

Emails + Slack + VictorOps għat-twissijiet (skont is-severità)

X'irridu li jkollna:

Prometheus għall-metriċi (Grafana għall-viżwalizzazzjoni)

New Relic (probabbilment Elastic Search APM) għall-monitoraġġ tal-applikazzjoni

EFK (elastic search + fluentd + kibana) għal-logging. Probabbilment, Loki minn Grafana jkun lest għall-produzzjoni sa meta naslu hawn

Sentry għall-eċċezzjonijiet

Alertmanager + email + VictorOps għat-twissijiet


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Dikjarazzjoni: naħdem għand VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf għal metriċi tas-server bħal CPU, Disk, Memory u Network. Nużaw ukoll Telegraf għall-monitoraġġ SNMP tal-apparati tan-netwerk tagħna.

Prometheus għal metriċi tal-applikazzjoni. Nikkodifikaw health checks fl-applikazzjoni tagħna li Prometheus jagħmel scraping tagħhom.

InfluxDB għall-ħażna ta' serje taż-żmien. Hawnhekk tintbagħat id-data ta' Telegraf tagħna.

Grafana għal dashboards u twissijiet. Il-magna tat-twissijiet mhix robusta ħafna, imma twettaq ix-xogħol. Nibagħtu wkoll twissijiet f'Slack.

Dak li m'għandix bħalissa huwa soluzzjoni ċentralizzata ta' logging. ELK huwa qawwi imma diffiċli biex jiġi ssettjat u mmaniġġjat, u ma nafx b'alternattivi b'xejn li huma qrib biżżejjed biex nifli.


### Sematext + Logagent + Experience

Sematext għal metriċi, għal logs, għal traċċi, dalwaqt għal monitoraġġ ta' utenti reali wkoll. Aktar sempliċi/rħas milli tuża N għodod/servizzi differenti, fl-opinjoni tiegħi.

Għat-trasport tal-logs konna nużaw rsyslog u mbagħad qlibna għal Logagent.

Għar-rappurtar tal-crashes tal-frontend nużaw Sentry, imma dalwaqt se nbiddlu għal Experience.

Dikjarazzjoni: jien Sematextan.


### Azure Monitor/Analytics + OpsGenie

Nixtieq li Log Analytics kellu interface aħjar. Qed nitbiegħdu minn splunk, li kien ħafna eħfef biex tinnaviga.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Verament ma tridx tħaddem is-sistema tan-notifiki tiegħek stess. Tista' tbiddel Splunk b'ELK sakemm it-tim tas-Sigurtà tiegħek ma jippreferix Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf bħala collector, Prometheus + Alertmanager għall-monitoraġġ u t-twissijiet, integrati ma' kanali slack u pagerduty għal twissijiet kritiċi. Grafana għall-viżwalizzazzjoni tal-metriċi tal-host.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus għal metriċi + twissijiet

Grafana għal dashboards ta' Prometheus

Cloudwatch jimmonitorja istanzi ta' Prometheus

sentry għat-traċċar tal-eċċezzjonijiet

kibana + elasticsearch

graylog

prometheus Push Gateway għal batch/cronjobs

SOP https://github.com/rapidloop/sop biex "tidfa'/tibgħat 'il quddiem" il-metriċi minn istanza ta' Prometheus għal oħra

il-klijenti jew jużaw il-Prometheus clients. Nippruvaw nużaw opencensus.io fuq in-naħa tal-klijent


### PagerDuty + Monitis

PagerDuty + Monitis. Ukoll xi Azure Functions magħmula apposta biex jittestjaw is-saħħa ta' xi servizzi.

Qed infittex li nintroduċi Prometheus u Grafana din is-sena


### Prometheus + Grafana + Bosun

Prometheus biex jaħżen id-data ta' serje taż-żmien. Grafana għall-viżwalizzazzjoni. Bosun għall-ġestjoni tat-twissijiet.


### Azure Monitor/Analytics/Insights/Dashboards

Ħanut Azure biss, Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana biex jimmonitorja servizzi tal-kontenituri f'Kubernetes permezz ta' Prometheus

Monitis għall-monitoraġġ end-to-end tas-servizzi l-aktar għal API tal-web u applikazzjonijiet tal-web

OpsGenie għall-ġestjoni tat-twissijiet

Slack biex niksbu informazzjoni dwar l-istatus mis-sistemi tagħna


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Inġinier (dev)ops ta' żmien twil hawnhekk. Kbirt fuq Nagios. Nixtieq nisma' opinjonijiet dwar is-SaaS bootstrapped tiegħi https://checklyhq.com. Nagħmlu monitoraġġ ta' API u monitoraġġ ta' tranżazzjonijiet tas-sit b'twissijiet pjuttost fil-fond.

Bdejt Checkly għax il-monitoraġġ attiv / sintetiku fl-ispazju tal-API kien kemmxejn limitat (u għali). Il-monitoraġġ ibbażat fuq il-browser / bi scripts huwa saħansitra aktar proprjetarju u għali. Nużaw Puppeteer u nżommu l-prezzijiet baxxi kemm jista' jkun.

L-istack tal-monitoraġġ tagħna:

Checkly (nużaw il-prodott tagħna stess...)

AppOptics (graffs personalizzati)

AWS Cloudwatch & SNS għal messaġġi SMS.

twissijiet integrati ta' Heroku.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana twissina f'slack dwar problemi tal-infrastruttura jew degradazzjoni tal-prestazzjoni, u kkonfigurajna logz.io biex iwissi f'slack dwar ċertu volum ta' logs tal-livell ta' żball mis-saff tal-applikazzjoni.


### SignalFX + Splunk + PagerDuty + Slack

Bħalissa qed nuża: SignalFX, Splunk, PagerDuty u Slack. Mhux ventilatur kbir ta' SignalFX għalkemm it-tim tal-appoġġ tagħhom huwa ħbieb u jwieġeb ħafna. Inħobb Splunk (jiswa jekk tista' tħallas għalih), PagerDuty u Slack.

Kont nuża l-istack TICK fejn il-biċċa l-kbira tal-C kienet verament G, jiġifieri Grafana għalkemm użajt Chronograf ftit. Dak kien tal-għaġeb imma kien uġigħ biex jiġi mmaniġġjat. Id-dilemma klassika SaaS vs self-hosting.

Użajt DataDog, New Relic, Graylog, ELK u BugSnag. Inħobb DataDog u New Relic ħafna, Graylog huwa pjuttost tajjeb. Mhux ventilatur kbir ta' ELK. BugSnag huwa sabiħ, verament inħoss li t-traċċar tal-iżbalji/eċċezzjonijiet huwa sostitut pjuttost tajjeb għall-monitoraġġ sħiħ tal-logs, f'ħafna każijiet.


### ELK + Prometheus + Grafana

Bħall-oħrajn, nużaw ELK għal-logs u Prometheus+Grafana għal kollox ieħor.

Iż-żamma ta' dan is-setup hija faċli jekk tagħti lilek innifsek permess li xi kultant titlef id-data. Pereżempju, jekk id-database ElasticSearch tagħna jidħol f'funk (li jiġri kull 2-3 xhur għalina sfortunatament) ma nitfixklux bl-HA u minflok inneħħu d-data u nkomplu bħajjitna. Jekk assolutament għandek bżonn HA jew żamma fit-tul, xorti.


### Datadog + Prometheus + Grafana

Waqqaft Datadog fuq bażi ta' xahar għal xahar għax meta wasalt hawn, ma kien hemm l-ebda monitoraġġ u l-ebda twissija. Ftit mis-siti tagħna biss kienu qed jiġu mmonitorjati kull 5 minuti għad-disponibbiltà. Datadog bla dubju huwa l-eħfef biex jiġi ssettjat. Meta nispiċċa nindirizza l-kwistjonijiet l-oħra kollha, se nbiddel għal Prometheus+Grafana. Għadni mhux deċiż 100% dwar il-ġestjoni tal-logs.


### Nagios + ELK

Għandna aktar minn 100+ prodott li nappoġġaw.

Għal on-prem, huwa l-aktar Nagios u ELK. Għall-cloud, qed nimigraw minn DataDog għal NewRelic.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Konna nużaw datadog imma sibnih għali wisq għall-ħtiġijiet tagħna. Tifhimnix ħażin, huwa tal-għaġeb imma għandu spiża enormi. Setajna nissettjaw site24x7.com b'abbonament annwali għal madwar 2-3 xhur ta' spiża minn DD.

L-istack tal-monitoraġġ tagħna:

Site24x7 - APM, monitoraġġ ta' URL esterni, monitoraġġ tal-mailflow SMTP, skadenzi ta' ssl u monitoraġġ tal-proċessi.

StatusCake - għal monitoraġġ u konferma ta' URL - Huwa l-backup tagħna f'każ li site24x7 jitlef xi ħaġa (ma jitlifx) imma SC huwa aktar flessibbli għal monitoraġġ ta' ports u servizzi esterni għall-ħtiġijiet tagħna.

It-tnejn jeskalaw għal PagerDuty, u mbagħad niksbu l-eskalazzjonijiet tagħna f'slack.

SumoLogic - għal monitoraġġ ta' logs (huwa għodda tajba imma kemmxejn ikkumplikata għall-ħtiġijiet tagħna)

Minn slack nistgħu nagħmlu ack, jew nirranġaw it-twissija.

Imbagħad għandna ħafna awtomazzjonijiet ta' site24x7 li mbagħad jikkonnettjaw ma' commando.io għal 'BedOps' kif insejħulu aħna - fejn titqanqal twissija, nibdew ftit scripts jew awtomazzjonijiet bħala tentattiv biex nirrimedjaw is-sitwazzjoni (99% tal-ħin l-awtomazzjoni + l-scripts tagħna jżommuna barra mill-inkwiet)

Għandna runbooks interni fil-KB tagħna għal meta l-awtomazzjonijiet jfallu jew jekk hemm xi ħaġa barra mill-ambitu li teħtieġ tiġi rranġata.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana għall-metriċi fil-clusters GKE u l-VMs tagħna.

Google Stackdriver għal Logs (billi huwa inkluż u attiv b'mod default u bħalissa huwa biżżejjed għall-ħtiġijiet tagħna).


### Zabbix

Zabbix għal kollox. M'hemmx bżonn software addizzjonali.
