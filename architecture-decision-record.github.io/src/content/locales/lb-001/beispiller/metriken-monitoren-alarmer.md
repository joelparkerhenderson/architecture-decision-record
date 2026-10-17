# Metriken, Monitoren, Alarmer

Inhalt:

* [Zesummefaassung](#zesummefaassung)
  * [Problem](#problem)
  * [Decisioun](#decisioun)
  * [Zoustand](#zoustand)
* [Detailer](#detailer)
  * [Viraussetzungen](#viraussetzungen)
  * [Restriktiounen](#restriktiounen)
  * [Positiounen](#positiounen)
  * [Argument](#argument)
  * [Implikatiounen](#implikatiounen)
* [Verwandt](#verwandt)
  * [Verwandt Decisiounen](#verwandt-decisiounen)
  * [Verwandt Ufuerderungen](#verwandt-ufuerderungen)
  * [Verwandt Artefakten](#verwandt-artefakten)
  * [Verwandt Prinzipien](#verwandt-prinzipien)
* [Notizen](#notizen)
  * [Fräitext-Messagen vs strukturéiert Evenement-Messagen](#fräitext-messagen-vs-strukturéiert-evenement-messagen)
  * [Graylog ass méi einfach](#graylog-ass-méi-einfach)
  * [Prometheus brauch e bëssen Tuning](#prometheus-brauch-e-bëssen-tuning)
  * [AWS-Servicer si gemëscht](#aws-servicer-si-gemëscht)
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


## Zesummefaassung


### Problem

Mir wëllen Metriken, Monitoren an Alarmer benotzen, well mir wëssen wëllen, wéi gutt eis Applikatioune funktionéieren, a wëssen wëllen, wann et e Problem gëtt.


### Decisioun

WIP.


### Zoustand

Mir sammelen Informatiounen. Mir fänken mat de plausibelen Enneren vum Spektrum un: dat am meeschte recommandéiert méi alt gratis Tool (Nagios) an dat am meeschte recommandéiert méi neit bezuelt Tool (New Relic).


## Detailer


### Viraussetzungen

Mir wëllen Web-Apps erstellen, déi modern, séier, zouverlässeg, responsiv, asw. sinn.

Mir wëllen eher kafen wéi bauen.


### Restriktiounen

Mir wëllen Tooling, dat gutt mat eiser Devops-Pipeline a mat eise Deployment-Clouds funktionéiert.


### Positiounen

Mir recherchéieren elo Positiounen.


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

Bis elo sinn Nagios an New Relic d'Enner vum Spektrum. Nagios ass dat eelst, einfachst, gratis, machbart Tool. New Relic ass dat neist, am meeschten ausgestatt, komplettst, bezuelt, machbart Tool. Mir fänken mat Evaluatioune vun dësen un. Wann néideg, migréiere mir an de Spektrum eran.  

Bis elo huet Zabbix déi bescht Recommandatiounen an bitt och déi komplettst Fäegkeeten.

Bis elo huet ELK déi bescht Open-Source-Build-iwwer-Buy-Popularitéit.

Bis elo hunn Prometheus + Graphana déi bescht Popularitéit.


### Implikatiounen

TODO.


## Verwandt


### Verwandt Decisiounen

D'Choixe wäerten d'Testbarkeet, d'Telemetrie a wahrscheinlech aner Systemer beaflossen, wéi fir de Clientsservice, Site Reliability Engineering, asw.


### Verwandt Ufuerderungen

TODO.


### Verwandt Artefakten

TODO.


### Verwandt Prinzipien

Einfach réckgängeg ze maachen.

Besoin u Vitess.


## Notizen

E ziemlech gudde Open-Source-Stack ass:

* Prometheus fir Metriken a Metrik-baséiert Alarméierung

* Grafana, fir Metriken unzeweisen

* Elasticsearch/Logstash/Kibana (ELK) fir Logs a strukturéiert Evenementer

* Pushover fir mobil Notifikatiounen


### Fräitext-Messagen vs strukturéiert Evenement-Messagen

Fräitext-Messagen: zum Beispill déi Zort vun zoufällege Saachen, déi een a /var/log/messages fënnt, an eppes, wat bewosst vun der Applikatioun generéiert gëtt. D'Messagen si nëtzlech, fir aner Saachen z'identifizéieren, déi um Rechner geschéien, wéi Out-of-Memory oder Hardwarefeeler, hunn awer vill Mëll. 

Strukturéiert Evenement-Messagen: vun der Applikatioun generéiert, mat engem fixen oder dynamesche Set u Attributer, z.B. en HTTP-Request-Log, e Buchhaltungslog, eng Benotzerumeldung.

Allgemeng gesinn ass et schéin, Detailer iwwer all Ufro esou ze loggen, datt een no Attributer erakënne kann. Wann een zum Beispill eng Userid oder Sessionid bei alles derbäisetzt, kann een traceéieren. Explizit Tracing ass natierlech och gutt. ELK dofir ze benotzen ass eng Aart Aarme-Leit-Variant vu https://www.honeycomb.io/


### Graylog ass méi einfach

Graylog ass no menger Erfahrung méi einfach opzesetzen.


### Prometheus brauch e bëssen Tuning

Ech si mat Prometheus fir Metriken allgemeng zefridden. D'Alarméierung brauch e bëssen Tuning, ass awer ganz gutt. Et hänkt vun Ärer Applikatioun of. Ech mengen, et ass am beschten, op Konditioune ze alarméieren, déi fir den Endbenotzer siichtbar sinn, net op ënnerläiwend Ursaachen. Zum Beispill ass d'Luedzäit vun enger Säit gutt, d'Zuel vun den Ufroen pro Sekonn net. Awer null Ufroe pro Sekonn weist un, datt eppes net stëmmt.

De Virdeel vun engem Service ass, datt si zousätzlech Intelligenz direkt matbréngen. Ech mengen allgemeng gär Datadog. D'Servicer kënnen erschreckend deier ginn, wann een vill Daten huet, a hunn heiansdo Präismodeller, déi net cloud-frëndlech sinn, z.B. pro Instanz ze berechnen, wann d'Instanze dynamesch sinn. Et gëtt och en Ënnerscheed tëscht Servicer, wou all Ufro vun engem bezuelende Benotzer kënnt, an deene, déi mat Reklamm ze dinn hunn, wou nëmmen e klenge Prozentsaz vun den Ufroe Iech Geld bréngt. Dir kënnt mat vill Daten an net esou vill Budget do stoen.

Ech schaffen un e puer Servicer, déi 1 Mrd. Ufroen den Dag kréien, dofir mécht et Sënn, eis eege Monitoring a Logging ze hosten. Wann Är Volumen méi niddereg sinn, da si gehostte Servicer méi einfach.


### AWS-Servicer si gemëscht

Meng Erfahrung mat AWS-Servicer war gemëscht. Hire Elasticsearch-Service war onzouverlässeg, dofir loosse mir eis eege Instanzen dofir lafen. CloudWatch-Metriken si deier, dofir benotze mir se allgemeng nëmmen fir Metriken um "Infrastruktur"-Niveau amplaz fir d'Applikatioun, dat heescht gesondheetsbezunne Metriken, wou AWS besser wësse kann, wat lass ass, wéi Software, déi op der Instanz leeft. CloudWatch Logs kënne lues sinn, fir sech ze aktualiséieren, an hu net sou vill Metadaten. ELK ze lafen hëlleft dobäi. Wann ech wierklech Echtzäitdaten wëll, ass et besser, Kafka als Transport fir Logs ze benotzen. Dat gëtt vu Logstash zimlech gutt ënnerstëtzt. E Kafka-Cluster ze verwalten ass awer näischt fir Schwaachhäerzeg, et gëtt vill ausgesat Installatioun.


### Kafka

Kommentar: Kafka kann heiansdo super knifflech sinn, oder Kafka kann fiels-fest sinn, an een vergëtt bal, datt et do ass a alles zesumme hält. 


Kommentar: Kafka war zouverlässeg, awer et war iwwerraschend vill Aarbecht, et zum Lafe ze kréien. Ech denken un et wéi un eng relationell Datebank, awer Dir schafft just um "physesche" Layer, z.B. Tablespaces, Dateien a Partitiounen. Et gouf e puer Mol fréi, wou d'Management-Utilities gefeelt hunn, a mir hunn Programmer missen schreiwen, fir z.B. eng Consumer Group zeréckzesetzen. http://howfuckedismydatabase.com/nosql/

Kommentar: Mir benotzen Kafka als "Buffer" fir Log-Messagen an als Plaz, wou mir Echtzäit-Stream-Processing op Daten maache kënnen, déi vu verschiddene Server kommen. Wa mir en DDOS-Attack kréien, brauche mir e Wee, Daten iwwer verschidden Instanze ze analyséieren. Wa mir direkt vun de Server op ELK loggen, kann d'Laascht den Elasticsearch-Cluster opsprengen.

Kommentar: Kafka ass gutt fir eis, well wa mir en DDOS-Attack kréien, brauche mir e Wee, Daten iwwer verschidden Instanze ze analyséieren. Wa mir direkt vun de Server op ELK loggen, kann d'Laascht den Elasticsearch-Cluster opsprengen.


Kommentar: Kafka mécht manner Aarbecht a ass méi effizient, dofir kann et d'Laascht besser handhaben. A mir setzen d'Kafka-Aarbecht a Waardeschlaang a probéieren nach eng Kéier. A wann Kafka iwwerlaascht ass, beaflosst dat keng Benotzer, déi interaktiv mat Kibana schaffe wëllen, sou wéi et wier, wann Elasticsearch kämpft.

Kommentar:  Stream-Processing sicht meeschtens no Mëssbrauch, z.B. ze vill Verkéier vun enger eenzeger IP iwwer de ganze Cluster, an deelt dann de Block iwwer de ganze Cluster.

Kommentar: De logstash-output-kafka-Plugin ass momentan zimlech onzouverlässeg. Ech sinn u verschidde Probleemer op sengem GitHub-Issues-Säit gerannt, déi anscheinend ni gefixt ginn. Ech wëll vun der Notzung ewech goen a direkt vun eisen Apps un Kafka schécken.

Kommentar: Mir schécke jetzt strukturéiert Evenementer direkt vun der App un Kafka. De Haaptgrond war, d'Logdaten manner dacks unzefaassen an ze vermeiden, d'Disk méi Mol ze liesen a ze schreiwen. A Systemer mat héijem Volumen kann d'Logging méi Aarbecht huelen wéi d'App selwer. Ech denken driwwer no, journald och direkt Logs schécke ze loossen, vun engem C-Programm.


### Loki

Haalt Loki gutt am A. Et ass nach net prett, awer wann et do ass, erwaarden ech, datt et besser an dëse Stack passt. Loki ass e Log-Aggregator vu grafana labs erstallt, en benotzt eng ähnlech Scraping- an Tag-Syntax wéi Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

Prometheus + alertmanager fir Metriken. <3 Prometheus.

Rollbar/Graylog fir Logging/Feelerberichterstattung (et gëtt hei eng gewësse Iwwerlappung; e klenge Service brauch wahrscheinlech net béid).

Momentan ginn d'Alarmer just an ee vun e puer Slack-Kanäl, wou interesséiert Parteien d'Notifikatioune ageschalt hunn. Wa mir méi eescht iwwer On-Call wiere, géifen si u PagerDuty/VictorOps/etc. goen.

Grafana fir Graphen an Dashboards. Ech kucke mech och gespaant drop, ob hir kommend Logging-Funktioune Graylog iwwerflësseg maachen.


### Thanos

Mir benotzen Thanos als Front-End fir eis HA-Setup. Et weess, wéi een HA-Puer dedupliséiert.

Mir halen momentan 6 Méint lokal Prometheus-Daten. Dat funktionéiert fir eis raisonabel gutt. Awer ech sinn grad dobäi, Bucket-Storage fir eis Thanos-Setup fir laangfristeg Datespäicherung auszerollen. An der Theorie wäert GCS-Storage ongeféier 30% méi bëlleg sinn wéi déi GCE-Standard-Persistent-Disk, déi mir elo benotzen.

Mir maachen momentan keng Backups vun de Prometheus-Daten. D'Daten sinn eis einfach net wierklech wichteg, iwwer genuch fir Alarméierung eraus. Eis ganz Flott-Deployment ännert sech sou vill vu Joer zu Joer, datt historesch Daten, déi eelere wéi e puer Méint sinn, einfach net esou interessant sinn. Et kéint interessant sinn, e puer Kärstatistike vu Joer zu Joer ze hunn, ech kéint e Core-Stats-Set vu Recording Rules opsetzen a mat Federation späicheren oder einfach Thanos dat iwwerhuele loossen.

EDIT: Kleng Haftungsausschloss, ech sinn e Prometheus-Entwéckler.


### Prometheus HA

HA a Prometheus gëtt duerch Duplikatioun gemaach, Dir lafe méi Poller, et gëtt Weeër, méi ze pollen an d'Daten ze dedupliséieren

D'Skaléierung geschitt, andeems een d'Netz opdeelt a verschidde Prometheus verschidden Deeler vum Netz pollen

Laangzäitspäicherung ass net dem Prom seng Stäerkt, gëtt awer un eppes wéi Influx oder timescaledb (dat technesch och den HA-Haken setzt) ofgeluecht, Artikel, deen ech doriwwer gelies hunn https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Ech hunn déi Laangzäit-Saache nach net probéiert, well ech nach just experimentéieren an et fir kuerzzäiteg Graphe benotzen, während librenms mäin Netz fir laangzäiteg Iwwerwaachung iwwerwaacht


### Datadog + PagerDuty + Threat Stack

Mir benotzen Datadog (mat PagerDuty) an Threat Stack a kéinten net méi zefridden sinn. Meng eenzeg Beschwerd iwwer DD sinn déi relativ héich Käschte vun der Metrikespäicherung.


### Zabbix

Zabbix mat Custom-Scripte fir bal alles ze iwwerwaachen. Funktionéiert wéi geschmiert.


### Outlyer

Ech benotzen Outlyer, mee ech muss deklaréieren, datt ech hei schaffen, an Dogfooding ass e Muss.

Ech brauch nach ëmmer Graylog, Sentry a Statuscake, fir ze verbesseren.

Kléngt partiisch, awer nodeems ech intern frou Nagios an aner Monitoringsystemer gelaf hunn, géif ech an all neier Stell eng gehosten Léisung kafen an dee Péng ofginn.


### Nagios + Nagiosgraph

Mir lafen Nagios fir all Monitoring an Alarméierung. Alarmer geschéien iwwer E-Mail (Warnungen a kritesch Notifikatiounen) an héierbar App-Notifikatiounen (fir kritesch Alarmer).

Nagiosgraph gëtt fir Visualiséierunge benotzt.

Dëse Setup huet sech als ganz effektiv erwisen, fir eis ëmfaassend doriwwer ze informéieren, wat an eisem Ëmfeld geschitt. Mir lafen a iwwerwaachen ongeféier 110 missiounskritesch Server an ongeféier 760 Datepunkten, an hunn dëst System zënter iwwer siwe Joer an Place.

Ech géif zu engem gewësse Punkt och gär Logs mat Graylog oder ELK aggregéieren.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager iwwer de super Prometheus-Operator-Helm-Chart. Logs ginn nach ëmmer an de LogDNA-Birch-Plang, well mir gemierkt hunn, datt ELK ze schwéier fir eis bescheiden min 3 max 5 Noden op GKE ass.


### DataDog + Sentry + PagerDuty.

Ech hunn all meng eege Monitoring-Léisungen mat allen Zorte vu Software bedriwwen, dorënner Nagios, Icinga, Zabbix, ELK, Greylog2, Influx a vill aner Tools, awer d'Wouerecht ass, datt et einfach ze vill Effort ass, seng eege Monitoring-Infrastruktur ze betreiben, besonnesch wann een een aneren sou niddreg Tariffer bezuele kann, fir dat fir een ze maachen!

Anerer ze bezuelen, d'Monitoring-Infra ze bedreiwen, befreit meng Clienten, sech drop ze konzentréieren, hir Plattformen ze bedreiwen, amplaz de Monitoring ze iwwerwaachen, wat bedeit, datt de Wäert, deen si aus der Stabilitéit vun hirer Plattform gewannen, all Käschte vum Monitoring as a Service wäit iwwerwiegt.


### Sensu + Graphite + ELK

Meng Firma ass richteg grouss op Self-Hosted-Saachen.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager fir Alarméierung, mäin Team gleeft, datt einfachen Monitoring gudden Monitoring ass.

Aner Systemer wéi Logging an Tracing liwweren e räiche Kontext fir d'Diagnos, wann den On-Call en Alarm kritt, awer mir bauen ni Alarméierung drop.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Prometheus-instrumentéiert Servicer => Circonus-Analytik a Visualiséierung


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Mir benotzen d'Servicer hei ënnen:

icinga2 fir Monitoring a VictorOps fir Alarméierung

NewRelic fir den Detailmonitoring vum Service

Sentry fir Feeler-Tracking am Service

Slack/E-Mail ass Deel vun der Alarméierung, déi vun NewRelic oder icinga2 ausgeléist gëtt


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 mat Elasticsearch-Integratioun fir Analys a graphite+grafana-Integratioun fir Graphen.

dank der Flexibilitéit vun den Apply Rules an icinga2 kënnen d'Entwéckler nëmmen d'Servicer gesinn, fir déi si Notifikatioune kréien.

an duerch icinga2 Director kënnen d'Programméierer einfach hir eege Checks definéieren (wat si maachen, all puer Deeg - 100 Checks ginn eraus, 100 aner Checks ginn eran) op grousser Skala ouni Opreegung.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Wat hu mir elo:

DataDog fir Metriken

New Relic fir Applikatiounsmonitoring

ELK (Elastic Search + Logstash + Kibana) fir d'Logs

Sentry (self-hosted) fir d'Logge vun Ausnamen

E-Mailen + Slack + VictorOps fir Alarméierung (no Schwéierecht)

Wat wëlle mir hunn:

Prometheus fir Metriken (Grafana fir Visualiséierung)

New Relic (wahrscheinlech Elastic Search APM) fir den Applikatiounsmonitoring

EFK (elastic search + fluentd + kibana) fir Logging. Wahrscheinlech wier Loki vu Grafana produktiounsbereet, bis mir dohinner kommen

Sentry fir d'Ausnamen

Alertmanager + E-Mail + VictorOps fir d'Alarmer


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Haftungsausschloss: schafft bei VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf fir Servermetriken wéi CPU, Disk, Memory a Network. Mir benotzen Telegraf och fir SNMP-Monitoring vun eisen Netzwierkapparater.

Prometheus fir Applikatiounsmetriken. Mir codéieren Health Checks an eis Applikatioun, déi Prometheus scrapt.

InfluxDB fir Zäitreie-Späicherung. Hei ginn eis Telegraf-Daten higeschéckt.

Grafana fir Dashboards an Alarmer. D'Alarméierungsmotor ass net super robust, mécht awer säin Job. Mir schécke Alarmer och an Slack.

Wat ech elo net hunn, ass eng zentral Logging-Léisung. ELK ass mächteg, awer schwéier opzesetzen an ze verwalten, a mir kennen keng gratis Alternativen, déi no genuch dru sinn, fir se ukucken.


### Sematext + Logagent + Experience

Sematext fir Metriken, fir Logs, fir Traces, geschwënn och fir Real User Monitoring. Méi einfach/méi bëlleg wéi N verschidden Tools/Servicer ze benotzen, meng Meenung no.

Fir de Log-Versand hu mir rsyslog benotzt an dunn op Logagent gewiesselt.

Fir Frontend-Crash-Reporting benotze mir Sentry, awer mir wiesselen geschwënn op Experience.

Haftungsausschloss: Ech sinn e Sematextan.


### Azure Monitor/Analytics + OpsGenie

Ech wëll, datt Log Analytics eng besser Interface hätt. Mir wiesselen vu Splunk ewech, dat vill méi einfach ze navigéieren war.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Dir wëllt wierklech net Äert eegent Notifikatiounssystem bedreiwen. Dir kënnt Splunk duerch ELK ersetzen, ausser Är Sécherheetsteam bevirzugt Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf als Collector, Prometheus + Alertmanager fir Monitoring an Alarméierung, integréiert mat Slack-Kanäl a Pagerduty fir kritesch Alarmer. Grafana fir d'Visualiséierung vun den Host-Metriken.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus fir Metriken + Alarmer

Grafana fir Prometheus-Dashboards

Cloudwatch iwwerwaacht Prometheus-Instanzen

sentry fir Ausnam-Tracking

kibana + elasticsearch

graylog

prometheus Push Gateway fir Batch/Cronjobs

SOP https://github.com/rapidloop/sop fir Metriken vun enger Prometheus-Instanz op eng aner „ze drécken/weiderzeleeden“

Clienten benotzen entweder d'Prometheus-Clienten. Mir probéiere opencensus.io op der Client-Säit ze benotzen


### PagerDuty + Monitis

PagerDuty + Monitis. Och e puer maßgeschneidert Azure Functions, fir d'Gesondheet vun e puer Servicer ze testen.

Mir wëllen dëst Joer Prometheus a Grafana aféieren


### Prometheus + Grafana + Bosun

Prometheus fir d'Späichere vun den Zäitreiedaten. Grafana fir Visualiséierung. Bosun fir d'Alarmverwaltung.


### Azure Monitor/Analytics/Insights/Dashboards

Nëmmen Azure-Geschäft, Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana fir de Monitoring vu Container-Servicer a Kubernetes iwwer Prometheus

Monitis fir End-to-End-Service-Monitoring haaptsächlech fir Web-APIen a Webapplikatiounen

OpsGenie fir d'Alarmverwaltung

Slack, fir Statusinformatioun vun eise Systemer ze kréien


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Laangjärege (Dev)Ops-Ingenieur hei. Opgewuess mat Nagios. Ech hätt gär Meenunge zu mengem bootstrapped SaaS https://checklyhq.com. Mir maachen API-Monitoring & Site-Transaktiounsmonitoring mat zimlech déiwer Alarméierung.

Ech hunn Checkly gegrënnt, well aktiv / syntheteschen Monitoring am API-Beräich e bësse limitéiert (an deier) war. Browser-baséierten / skriptbaséierte Monitoring ass nach méi proprietär an deier. Mir benotzen Puppeteer a halen de Präis esou niddreg wéi méiglech.

Eise Monitoring-Stack:

Checkly (Dogfooding...)

AppOptics (eege Graphen)

AWS Cloudwatch & SNS fir SMS-Messagen.

agebaute Heroku-Alarméierung.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana alarméiert eis a Slack iwwer Infrastrukturproblemer oder Performance-Degradatioun, a mir hunn logz.io konfiguréiert, fir a Slack bei engem bestëmmte Volumen u Feeler-Level-Logs aus der Applikatiounsschicht ze alarméieren.


### SignalFX + Splunk + PagerDuty + Slack

Momentan benotzt: SignalFX, Splunk, PagerDuty a Slack. Ech sinn net e grousse Fan vu SignalFX, och wann hiren Support-Team super frëndlech a reaktiounsfäeg ass. Ech mengen Splunk (et ass et wäert, wann een et bezuele kann), PagerDuty a Slack.

Ech hunn de TICK-Stack benotzt, wou de gréissten Deel vum C wierklech e G war, dat heescht Grafana, och wann ech Chronograf e bëssen benotzt hunn. Dat war geneial, awer et war en Hiewel ze verwalten. Dat klassescht SaaS-vs.-Self-Hosting-Dilemma.

Ech hunn DataDog, New Relic, Graylog, ELK a BugSnag benotzt. Ech mengen DataDog a New Relic ganz gär, Graylog ass zimlech gutt. Ech sinn net e grousse ELK-Fan. BugSnag ass schéin, ech hunn tatsächlech d'Gefill, datt d'Tracking vu Feeler/Ausnamen a ville Fäll e zimlech gudde Stellvertrieder fir de vollen Log-Monitoring ass.


### ELK + Prometheus + Grafana

Genau wéi anerer benotze mir ELK fir Logs a Prometheus+Grafana fir alles aneres.

Dëse Setup ze erhalen ass einfach, wann een sech d'Erlaabnis gëtt, heiansdo Daten ze verléieren. Zum Beispill, wann eis ElasticSearch-Datebank an e Funk fält (wat bei eis leider all 2-3 Méint geschitt), bemellen mir eis net mat HA, mee dumpe amplaz d'Daten a maache mat eisem Liewen weider. Wann Dir ofsolut HA oder laangzäiteg Retention musst hunn, vill Gléck.


### Datadog + Prometheus + Grafana

Ech hunn Datadog op Mount-zu-Mount-Basis opgesat, well wéi ech heihinner koum, gouf et keen Monitoring a keng Alarméierung. Nëmmen e puer vun eise Sitte goufen all 5 Min. op Uptime iwwerwaacht. Datadog ass ouni Zweiwel dee einfachsten opzesetzen. Wann ech all déi aner Problemer ugeholl hunn, wiesselen ech op Prometheus+Grafana. Nach net 100% decidéiert iwwer d'Log-Verwaltung.


### Nagios + ELK

Mir hunn iwwer 100+ Produkter, déi mir ënnerstëtzen.

Fir On-Prem ass et haaptsächlech Nagios an ELK. Fir d'Cloud migréiere mir vun DataDog op NewRelic.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Mir hunn Datadog benotzt, hu mir awer fonnt, datt et ze deier fir eis Bedierfnisser war. Verstitt mech net falsch, et ass geil, awer et huet enorm Käschten. Mir hunn site24x7.com mat engem Joresabonnement fir ongeféier 2-3 Méint Käschte vun DD kënnen opsetzen.

Eise Monitoring-Stack:

Site24x7 - APM, Monitoring vun externen URLen, SMTP-Mailflow-Monitoring, SSL-Ablaf a Prozessmonitoring.

StatusCake - fir URL-Monitoring a Bestätegung - Et ass eise Backup, fir de Fall, datt site24x7 eppes verpasst (et mécht et net), awer SC ass méi flexibel fir externe Port- a Servicemonitoring fir eis Bedierfnisser.

Béid Tools eskaléieren op PagerDuty, an dann kréie mir eis Eskalatiounen a Slack.

SumoLogic - fir Log-Monitoring (et ass e super Tool, awer e bëssen ze kompliziert fir eis Bedierfnisser)

Vu Slack aus kënne mir den Alarm bestätegen oder behiewen.

Mir hunn dann vill site24x7-Automatiounen, déi sech dann mat commando.io fir 'BedOps' verbannen, wéi mir et nennen - wou en Alarm ausgeléist gëtt, starte mir e puer Scripten oder Automatiounen als Versuch, d'Situatioun ze behiewen (99% vun der Zäit halen d'Automatioun + eis Scripte eis aus Schwieregkeeten eraus)

Mir hunn intern Runbooks an eiser KB fir den Fall, datt d'Automate versoen oder wann et eppes ausserhalb vum Ëmfang gëtt, dat muss gefixt ginn.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana fir Metriken an eise GKE-Cluster a VMen.

Google Stackdriver fir Logs (well et abegraff an standardméisseg aktiv ass a momentan fir eis Bedierfnisser duergeet).


### Zabbix

Zabbix fir alles. Keng zousätzlech Software néideg.
