# Metrikak, monitoreak, alertak

Edukia:

* [Laburpena](#laburpena)
  * [Arazoa](#arazoa)
  * [Erabakia](#erabakia)
  * [Egoera](#egoera)
* [Xehetasunak](#xehetasunak)
  * [Hipotesiak](#hipotesiak)
  * [Murriztapenak](#murriztapenak)
  * [Jarrerak](#jarrerak)
  * [Arrazoibidea](#arrazoibidea)
  * [Ondorioak](#ondorioak)
* [Erlazionatuta](#erlazionatuta)
  * [Erlazionatutako erabakiak](#erlazionatutako-erabakiak)
  * [Erlazionatutako eskakizunak](#erlazionatutako-eskakizunak)
  * [Erlazionatutako artefaktuak](#erlazionatutako-artefaktuak)
  * [Erlazionatutako printzipioak](#erlazionatutako-printzipioak)
* [Oharrak](#oharrak)
  * [Testu libreko mezuak vs. gertaera-mezu egituratuak](#testu-libreko-mezuak-vs-gertaera-mezu-egituratuak)
  * [Graylog errazagoa da](#graylog-errazagoa-da)
  * [Prometheus-ek doikuntza batzuk behar ditu](#prometheus-ek-doikuntza-batzuk-behar-ditu)
  * [AWS zerbitzuak nahasiak dira](#aws-zerbitzuak-nahasiak-dira)
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


## Laburpena


### Arazoa

Metrikak, monitoreak eta alertak erabili nahi ditugu, gure aplikazioek zein ondo funtzionatzen duten eta arazoren bat noiz dagoen jakin nahi dugulako.


### Erabakia

WIP.


### Egoera

Informazioa biltzen. Espektroaren muturreko posible hauetatik hasten gara: gehien gomendatutako tresna doako zaharra (Nagios) eta gehien gomendatutako ordainpeko tresna berria (New Relic).


## Xehetasunak


### Hipotesiak

Web aplikazio modernoak, azkarrak, fidagarriak, erantzunkorrak eta abar sortu nahi ditugu.

Eraiki beharrean erosi nahi dugu.


### Murriztapenak

Gure devops hodiarekin eta gure hedapen-hodeiekin ondo funtzionatzen duten tresnak nahi ditugu.


### Jarrerak

Jarrerak ikertzen ari gara orain.


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

  

  
### Arrazoibidea

Orain arte, Nagios eta New Relic dira espektroaren muturrak. Nagios tresna zaharrena, sinpleena, doakoa eta bideragarria da. New Relic ezaugarri berrienak dituen tresna, osoena, ordainpekoa eta bideragarria da. Hauek ebaluatzen hasiko gara. Behar izanez gero, espektroaren barrura joango gara.  

Orain arte, Zabbix-ek du gomendio onena, eta gaitasun osoenak ere eskaintzen ditu.

Orain arte, ELK-k du eraiki-erosi aurrean kode irekiko ezagutza onena.

Orain arte, Prometheus + Graphana-k dute ezagutza onena.


### Ondorioak

TODO.


## Erlazionatuta


### Erlazionatutako erabakiak

Aukerek probagarritasunean, telemetrian eta, ziurrenik, bezeroarentzako arreta, gunearen fidagarritasun-ingeniaritza eta abar bezalako beste sistema batzuetan eragingo dute.


### Erlazionatutako eskakizunak

TODO.


### Erlazionatutako artefaktuak

TODO.


### Erlazionatutako printzipioak

Erraz atzera egin daitekeena.

Abiadura beharra.


## Oharrak

Kode irekiko pila nahiko ona hau da:

* Prometheus metrikak eta metriketan oinarritutako alertak egiteko

* Grafana metrikak bistaratzeko

* Elasticsearch/Logstash/Kibana (ELK) erregistroetarako eta gertaera egituratuetarako

* Pushover jakinarazpen mugikorretarako


### Testu libreko mezuak vs. gertaera-mezu egituratuak

Testu libreko mezuak: adibidez, /var/log/messages-en aurkituko zenukeen ausazko materiala, eta aplikazioak nahita sortutakoa. Mezu hauek baliagarriak dira kutxan gertatzen ari diren beste gauza batzuk identifikatzeko, hala nola memoria-faltak edo hardware-akatsak, baina zaborra asko dute. 

Gertaera-mezu egituratuak: aplikazioak sortuak, atributu-multzo finko edo dinamiko batekin, adib. HTTP eskaeren erregistroa, kontabilitate-erregistroa, erabiltzaile-saio-hasiera.

Orokorrean, polita da eskaera bakoitzaren xehetasunak erregistratzea atributuen arabera sakontzeko moduan. Beraz, adibidez userid edo sessionid bat guztiari gehitzeak jarraipena egiteko aukera ematen du. Jarraipen esplizitua ere ona da, jakina. Horretarako ELK erabiltzea https://www.honeycomb.io/ -ren pobreen bertsioa bezalakoa da


### Graylog errazagoa da

Graylog errazagoa da abian jartzeko nire esperientziaren arabera.


### Prometheus-ek doikuntza batzuk behar ditu

Orokorrean pozik nago Prometheus-ekin metrikatarako. Alertek doikuntza batzuk behar dituzte, baina nahiko onak dira. Zure aplikazioaren araberakoa da. Uste dut hobe dela azken erabiltzaileak ikus ditzakeen baldintzei buruz alertatzea, ez azpiko kausei buruz. Adibidez, orriaren karga-denbora ona da, segundoko eskaera kopurua ez. Nahiz eta segundoko zero eskaerak zerbait gaizki dagoela adierazten duen.

Zerbitzu baten abantaila da adimen gehigarria eskaintzen dutela kutxatik kanpo. Orokorrean Datadog gustatzen zait. Zerbitzuak izugarri garestiak izan daitezke datu asko badituzu, eta batzuetan hodei-lagunkoiak ez diren prezio-ereduak dituzte, adib. instantziako kobratzea, instantziak dinamikoak direnean. Erabiltzaile ordaintzaile batengandik datorren eskaera bakoitza duten zerbitzuen eta publizitatearekin lotutakoen arteko aldea ere badago, beraz eskaeren ehuneko txiki bat bakarrik dira dirua ematen dizutenak. Datu asko eta aurrekontu gutxi izatera irits zaitezke.

Egunean 1.000 milioi eskaera jasotzen dituzten zerbitzu batzuetan lan egiten dut, beraz zentzuzkoa da gure monitorizazioa eta erregistroa geuk ostatatzea. Zure bolumenak txikiagoak badira, ostatatutako zerbitzuak errazagoak dira.


### AWS zerbitzuak nahasiak dira

AWS zerbitzuekin izan dudan esperientzia nahasia izan da. Haien Elasticsearch zerbitzua ezegonkorra izan da, beraz gure instantziak exekutatzen ditugu horretarako. CloudWatch metrikak garestiak dira, beraz orokorrean "azpiegitura" mailako metrikatarako soilik erabiltzen ditugu aplikaziorako beharrean, hau da, osasunarekin lotutako metrikak non AWS-k instantzian exekutatzen ari den softwareak baino hobeto jakin dezakeen zer gertatzen ari den. CloudWatch Logs eguneratzeko motelak izan daitezke eta ez dute metadatu askorik. ELK exekutatzeak horretan laguntzen du. Denbora errealeko datuak benetan nahi baditut, Kafka erregistroen garraio gisa erabiltzea hobea da. Hori Logstash-ek nahiko ondo onartzen du. Kafka kluster bat kudeatzea ez da bihotz ahulentzat, ordea, hodiak asko agerian daude.


### Kafka

Iruzkina: Kafka izugarri tranpatsua izan daiteke batzuetan, edo Kafka harkaitza bezain sendoa izan daiteke eta ia ahaztuko duzu hor dagoela dena elkartzen.


Iruzkina: Kafka sendoa izan da, baina harrigarria izan zen martxan jartzeko behar izan zen lan kopurua. Datu-base erlazional baten antzera pentsatzen dut baina "fisikoko" geruzan bakarrik ari zara lanean, adib. taulaleku, fitxategi eta partizioetan. Hasieran batzuetan kudeaketa-tresnak falta ziren, eta programak idatzi behar izan genituen adib. consumer group bat berrezartzeko. http://howfuckedismydatabase.com/nosql/

Iruzkina: Kafka erregistro-mezuentzako "buffer" gisa erabiltzen dugu eta zerbitzari anitzetatik datozen datuen gaineko denbora errealeko stream prozesamendua egin dezakegun leku gisa. DDOS eraso bat jasotzen badugu, instantzia anitzen artean datuak aztertzeko modu bat behar dugu. Zerbitzarietatik zuzenean ELK-ra erregistratzen badugu, kargak Elasticsearch kluster-a lehertu dezake.

Iruzkina: Kafka ona da guretzat DDOS eraso bat jasotzen badugu, instantzia anitzen artean datuak aztertzeko modu bat behar dugulako. Zerbitzarietatik zuzenean ELK-ra erregistratzen badugu, kargak Elasticsearch kluster-a lehertu dezake.


Iruzkina: Kafka-k lan gutxiago egiten du eta eraginkorragoa da, beraz kargari hobeto aurre egin diezaioke. Eta Kafka-ren lana ilaran jartzen dugu eta berriz saiatzen gara. Eta Kafka gainkargatuta egoteak ez die eragiten Kibana-rekin lan interaktiboa egiten saiatzen ari diren erabiltzaileei, Elasticsearch lanpetuta balego gertatuko litzatekeen moduan.

Iruzkina:  Stream prozesamenduak batez ere abusua bilatzen du, adib. IP bakar batetik klusterrera trafiko gehiegi, eta gero blokeoa kluster osoan partekatzen du.

Iruzkina: logstash-output-kafka plugin-a nahiko ez-fidagarria da oraingoz. Bere GitHub issues orrian arazo batzuek kolpatu naute, inoiz konponduko ez direla ematen duenak. Hau erabiltzeari utzi eta gure aplikazioetatik zuzenean Kafka-ra bidaltzera pasatu nahi dut.

Iruzkina: Orain gertaera egituratuak aplikaziotik zuzenean Kafka-ra bidaltzen ari gara. Motibazio nagusia erregistro-datuak gutxiagotan ukitzea eta diskoa hainbat aldiz irakurtzea eta idaztea saihestea zen. Bolumen handiko sistemetan, erregistratzeak aplikazioak berak baino lan gehiago eska dezake. journald erregistroak zuzenean bidaltzea ere pentsatzen ari naiz, C programa batetik.


### Loki

Begiratu Loki-ri arreta handiz. Ez dago oraindik prest baina egon denean pila honetan hobeto egokituko dela espero dut. Loki grafana labs-ek sortutako erregistro-agregatzailea da, Prometheus-en antzeko scraping eta etiketa sintaxia erabiltzen duena.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

Prometheus + alertmanager metrikatarako. <3 Prometheus.

Rollbar/Graylog erregistrorako/errore-txostenetarako (gainjartze bat dago hemen; zerbitzu txiki batek ziurrenik ez ditu bi-biak behar).

Une honetan, alertak interesdunek jakinarazpenak aktibatuta dituzten Slack kanal gutxi batzuetara bakarrik doaz. Dei-zerbitzuaz (on-call) serioago bagina PagerDuty/VictorOps/eta abarretara joango lirateke.

Grafana grafikoetarako eta panelak egiteko. Gainera, irrikitan nago ikusteko haien datozen erregistro-instalazioek Graylog beharrezko izateari utziko dioten.


### Thanos

Thanos erabiltzen dugu gure HA konfigurazioaren front-end gisa. HA bikoteak deduplikatzen dakil.

Une honetan 6 hilabeteko Prometheus datu lokalak gordetzen ditugu. Honek nahiko ondo funtzionatzen du guretzat. Baina epe luzeko datu-biltegiratze bat gure Thanos konfiguraziora ezartzen ari naiz. Teorian, GCS biltegiratzea gaur erabiltzen dugun GCE disko iraunkor estandarra baino %30 inguru merkeagoa izango da.

Une honetan ez dugu Prometheus datuen babeskopiarik egiten. Datuak ez dira benetan garrantzitsuak guretzat alertarako nahikoa edukitzetik harago. Gure flota osoaren hedapena hainbeste aldatzen da urtez urte, non hilabete batzuk baino zaharragoak diren datu historikoak ez diren benetan interesgarriak. Interesgarria izan liteke estatistika nagusi batzuk urtez urte edukitzea, estatistika-nagusien grabazio-arauak konfiguratu eta Federation-ekin gorde ditzaket edo Thanos-ek ardura dezala utzi.

EDIT: Deskargu txiki bat, Prometheus garatzailea naiz.


### Prometheus HA

Prometheus-en HA bikoizketaren bidez egiten da, hainbat poller exekutatzen dituzu eta hainbat galdetzeko eta datuak deduplikatzeko moduak daude

Eskalatzea sarea erabakiz eta Prometheus desberdinek sarearen zati desberdinak galdetuz egiten da

Epe luzeko biltegiratzea ez da Prom-en indargunea baina influx edo timescaledb bezalakoetara deskargatzen da (teknikoki HA kontrol-laukia ere markatzen duena) irakurri nuen artikulua https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Epe luzeko gauzak oraindik ez ditut probatu oraindik esperimentatzen eta epe laburreko grafikoetarako erabiltzen ari naizelako librenms-ek nire sarea epe luzera monitorizatzen duen bitartean


### Datadog + PagerDuty + Threat Stack

Datadog (PagerDuty-rekin) eta Threat Stack erabiltzen ditugu eta ezin gaitezke pozikoagoak izan. DD-rekin dudan kexa bakarra metrika-biltegiratzearen kostu nahiko altua da.


### Zabbix

Zabbix script pertsonalizatuekin ia dena monitorizatzeko. Xarma bezala funtzionatzen du.


### Outlyer

Outlyer erabiltzen ari naiz, baina esan behar dut hemen lan egiten dudala, eta dog fooding-a ezinbestekoa dela.

Graylog, Sentry eta Statuscake behar dira oraindik hobetzeko.

Alboratua dirudi, baina Nagios eta beste monitorizazio sistemak barnean pozik exekutatu ondoren, edozein lan berrian ostatatutako irtenbide bat erosiko nuke eta min hori kanpora aterako nuke.


### Nagios + Nagiosgraph

Nagios exekutatzen dugu monitorizazio eta alerta guztietarako. Alertak posta elektronikoz (abisuak eta jakinarazpen kritikoak) eta aplikazio-jakinarazpen entzungarriz (alerta kritikoetarako) gertatzen dira.

Nagiosgraph bistaratzeetarako erabiltzen da.

Konfigurazio honek oso eraginkorra izan da gure ingurunean gertatzen ari denaz erabat jakinaren gainean mantentzeko. Misio-kritikoak diren 110 zerbitzari inguru eta 760 datu-puntu inguru exekutatzen eta monitorizatzen ditugu, eta goizeko sistema hau zazpi urte baino gehiagoz izan dugu.

Noizbait erregistroak Graylog edo ELk-rekin ere agregatu nahiko nuke.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager Prometheus Operator helm chart zoragarriaren bidez. Erregistroak oraindik LogDNA birch planera doaz ELK gure GKE-ko min 3 max 5 nodo xumeentzat astunegia dela ohartu ginelako.


### DataDog + Sentry + PagerDuty.

Nire monitorizazio-soluzio guztiak neuk exekutatzen nituen era guztietako softwarea erabiliz, Nagios, Icinga, Zabbix, ELK, Greylog2, Influx eta beste tresna asko barne, baina egia da monitorizazio-azpiegitura propioa exekutatzeko ahalegin handiegia dagoela, bereziki beste norbaiti hori egiteagatik tarifa hain baxuak ordain ditzakezunean!

Besteei monitorizazio-azpiegitura exekutatzeagatik ordaintzeak nire bezeroak libre uzten ditu beren plataformak exekutatzean zentratzeko monitorizazioa monitorizatu beharrean, hau da, beren plataformaren egonkortasunetik lortzen duten balioa Monitorizazioa Zerbitzu gisa den edozein kostu baino askoz handiagoa dela.


### Sensu + Graphite + ELK

Nire enpresa oso zalea da norberak ostatatutako gauzena.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager alertetarako, nire taldeak uste du monitorizazio sinplea monitorizazio ona dela.

Erregistro eta trazaketa bezalako beste sistemek testuinguru aberatsa emango dute diagnostikorako on-call-ak alerta bat jasotzen duenean, baina inoiz ez ditugu alertak hauetan oinarritzen.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Prometheus-ekin instrumentatutako zerbitzuak => Circonus analitika eta bistaratzea


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Zerbitzu hauek erabiltzen ari gara:

icinga2 monitorizaziorako eta VictorOps alertetarako

NewRelic zerbitzuaren monitorizazio xehatuetarako

Sentry zerbitzuko errore-jarraipenerako

Slack/Email alerten parte da NewRelic edo icinga2-tik abiarazten dena


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 elasticsearch integrazioarekin analisirako eta graphite+grafana integrazioarekin grafikoetarako.

icinga2-ren apply arauen malgutasunari esker, garatzaileek jakinarazpenak jasotzen dituzten zerbitzuak bakarrik ikus ditzakete.

eta icinga2 director-aren bidez, programatzaileek erraz defini ditzakete beren egiaztapenak (egunero egiten dituztenak - 100 egiaztapen ateratzen dira, 100 beste egiaztapen sartzen dira) eskala handian trabarik gabe.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Zer dugu orain:

DataDog metrikatarako

New Relic aplikazioen monitorizaziorako

ELK (Elastic Search + Logstash + Kibana) erregistroetarako

Sentry (norberak ostatatua) salbuespenak erregistratzeko

Posta elektronikoa + Slack + VictorOps alertetarako (larritasunaren arabera)

Zer izan nahi dugu:

Prometheus metrikatarako (Grafana bistaratzerako)

New Relic (agian Elastic Search APM) aplikazioen monitorizaziorako

EFK (elastic search + fluentd + kibana) erregistrorako. Agian, Grafana-ren Loki prod-prest egongo da hara iristen garen unerako

Sentry salbuespenetarako

Alertmanager + posta elektronikoa + VictorOps alertetarako


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Deskargua: VMware-n lan egiten du)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf zerbitzari-metrikak, hala nola CPU, Diskoa, Memoria eta Sarea, lortzeko. Telegraf gure sare-gailuen SNMP monitorizaziorako ere erabiltzen dugu.

Prometheus aplikazio-metrikatarako. Osasun-egiaztapenak kodetzen ditugu gure aplikazioan, Prometheus-ek scrape egiten dituenak.

InfluxDB denbora-serieen biltegiratzerako. Hor bidaltzen dira gure Telegraf datuak.

Grafana panelak eta alertak egiteko. Alerta-motorra ez da oso sendoa, baina lana egiten du. Alertak Slack-era ere bidaltzen ditugu.

Orain ez daukadana erregistro zentralizatuko irtenbide bat da. ELK ahaltsua da baina konfiguratzeko eta kudeatzeko zaila, eta ez dakit aztertzeko adina hurbil dagoen doako alternatibarik.


### Sematext + Logagent + Experience

Sematext metrikak, erregistroak, trazak lortzeko, laster erabiltzaile errealen monitorizaziorako ere. Sinpleagoa/merkeagoa N tresna/zerbitzu desberdin erabiltzea baino, nire ustez.

Erregistroak bidaltzeko rsyslog erabiltzen genuen eta gero Logagent-era aldatu ginen.

Front-end kraskatze-txostenetarako Sentry erabiltzen dugu, baina laster Experience-ra aldatuko gara.

Deskargua: Sematextan bat naiz.


### Azure Monitor/Analytics + OpsGenie

Log Analytics-ek interfaze hobea izatea nahiko nuke. Splunk-etik aldentzen ari gara, nabigatzeko askoz errazagoa zena.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Benetan ez duzu zure jakinarazpen-sistema propioa exekutatu nahi. Splunk ELK-rekin ordez dezakezu zure Segurtasun taldeak Splunk nahiago ez badu.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf bildumagile gisa, Prometheus + Alertmanager monitorizazio eta alertetarako, slack kanalekin eta pagerduty-rekin integratuta alerta kritikoetarako. Grafana ostalari-metriken bistaratzerako.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus metrikak + alertak egiteko

Grafana Prometheus panelak egiteko

Cloudwatch Prometheus instantziak monitorizatzeko

sentry salbuespenak jarraitzeko

kibana + elasticsearch

graylog

prometheus Push Gateway batch/cronjob-etarako

SOP https://github.com/rapidloop/sop metrikak Prometheus instantzia batetik bestera „push/forward“ egiteko

bezeroek Prometheus bezeroak erabiltzen dituzte. opencensus.io bezero aldean erabiltzen saiatzen gara


### PagerDuty + Monitis

PagerDuty + Monitis. Baita zerbitzu batzuen osasuna probatzeko Azure Functions neurrira eginak ere.

Aurten Prometheus eta Grafana sartzea bilatzen ari gara


### Prometheus + Grafana + Bosun

Prometheus denbora-serieen datuak gordetzeko. Grafana bistaratzeko. Bosun alerten kudeaketarako.


### Azure Monitor/Analytics/Insights/Dashboards

Azure bakarrik duen denda, Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana Kubernetes-eko ontzi-zerbitzuak Prometheus bidez monitorizatzeko

Monitis muturretik muturrerako zerbitzuen monitorizaziorako, batez ere web API-ak eta web aplikazioetarako

OpsGenie alerten kudeaketarako

Slack gure sistemen egoera-informazioa lortzeko


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

(Dev)ops ingeniari beterano bat naiz hemen. Nagios-ekin hazi nintzen. Nire bootstrap SaaS https://checklyhq.com-i buruzko iritziak jasotzea gustatuko litzaidake. API monitorizazioa eta guneko transakzio monitorizazioa egiten ditugu alerta nahiko sakonekin.

Checkly hasi nuen API-ko monitorizazio aktibo / sintetikoa apur bat mugatua (eta garestia) zelako. Nabigatzailean oinarritutako / script-etako monitorizazioa are jabeduna eta garestiagoa da. Puppeteer erabiltzen dugu eta prezioak ahalik eta baxuen mantentzen ditugu.

Gure monitorizazio-pila:

Checkly (dog fooding...)

AppOptics (grafikatze pertsonalizatua)

AWS Cloudwatch & SNS SMS mezuetarako.

Heroku alerta integratuak.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana-k slack-en alertatzen gaitu azpiegitura-arazoei edo errendimendu-narriadurari buruz, eta logz.io konfiguratu dugu aplikazio-geruzako errore-mailako erregistro-bolumen jakin batean slack-en alertatzeko.


### SignalFX + Splunk + PagerDuty + Slack

Une honetan erabiltzen: SignalFX, Splunk, PagerDuty eta Slack. Ez naiz SignalFX-en zale handia nahiz eta haien laguntza-taldea oso atsegina eta erantzunkorra den. Splunk gustatzen zait (ordaintzeko modua baduzu merezi du), PagerDuty eta Slack.

TICK pila erabiltzen nuen non C gehienak G ziren benetan, hau da Grafana nahiz eta Chronograf apur bat erabili nuen. Hori zoragarria zen baina kudeatzeko mina zen. SaaS vs. norberak ostatatzearen dilema klasikoa.

DataDog, New Relic, Graylog, ELK eta BugSnag erabili ditut. DataDog eta New Relic asko gustatzen zaizkit, Graylog nahiko ona da. Ez naiz ELK-ren zale handia. BugSnag polita da, benetan erroreak/salbuespenak jarraitzea erregistro-monitorizazio osoaren ordezko nahiko ona dela uste dut, kasu askotan.


### ELK + Prometheus + Grafana

Besteek bezala, ELK erabiltzen dugu erregistroetarako eta Prometheus+Grafana beste guztirako.

Konfigurazio hau mantentzea erraza da zeure buruari noizean behin datuak galtzeko baimena ematen badiozu. Adibidez, gure ElasticSearch datu-basea oker jartzen bada (gure kasuan 2-3 hilabetero gertatzen dena zoritxarrez) ez gara HA-rekin kezkatzen eta, horren ordez, datuak botatzen ditugu eta bizitzarekin jarraitzen dugu. HA edo epe luzeko atxikipena zinez behar baduzu, zorte on.


### Datadog + Prometheus + Grafana

Datadog hilabetez hilabete konfiguratu nuen hona iritsi nintzenean ez zegoelako monitorizaziorik ezta alertarik ere. Gure gune gutxi batzuk bakarrik monitorizatzen ziren 5 minuturo uptime-rako. Datadog nabarmen da konfiguratzeko errazena. Beste arazo guztiak konpontzen amaitzen dudanean, Prometheus+Grafana-ra aldatuko naiz. Ez dago %100 erabakita erregistroen kudeaketaz oraindik.


### Nagios + ELK

100+ produktu baino gehiago ditugu laguntza ematen diegunak.

On-prem-erako, gehienbat Nagios eta ELK. Hodeirako, DataDog-etik NewRelic-era migratzen ari gara.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Datadog erabiltzen genuen baina gure beharretarako oso garestia zela aurkitu genuen. Ez ulertu gaizki zoragarria da, baina kostu izugarria du. Site24x7.com urteko harpidetza batekin konfiguratu ahal izan genuen DD-ren 2-3 hilabeteko kostuaren inguruan.

Gure monitorizazio-pila:

Site24x7 - APM, kanpoko URL monitorizazioa, SMTP posta-fluxuaren monitorizazioa, ssl iraungitzeak eta prozesu monitorizazioa.

StatusCake - URL monitorizaziorako eta berrespenerako - Gure babeskopia da site24x7-ek zerbait galtzen badu (ez du galtzen) baina SC malguagoa da kanpoko ataka eta zerbitzu monitorizaziorako gure beharretarako.

Bi tresnek PagerDuty-ra eskalatzen dute, eta gero gure eskalatzeak slack-en jasotzen ditugu.

SumoLogic - erregistro-monitorizaziorako (tresna bikaina da baina apur bat konplexua gure beharretarako)

Slack-etik alerta ack egin edo konpon dezakegu.

Gero site24x7 automatizazio asko ditugu commando.io-ra konektatzen direnak 'BedOps'-erako, hala deitzen diogun bezala - alerta bat abiarazten denean, script edo automatizazio batzuk hasten ditugu egoera konpontzen saiatzeko (denboraren %99an automatizazioak + gure script-ek arazoetatik kanpo mantentzen gaituzte)

Barneko runbook-ak ditugu gure KB-an automatizazioek huts egiten dutenerako edo irismenetik kanpo zerbait konpondu behar denerako.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana gure GKE kluster eta VM-etako metrikatarako.

Google Stackdriver erregistroetarako (barne dagoelako eta lehenespenez aktibo dagoelako eta oraingoz gure beharretarako nahikoa delako).


### Zabbix

Zabbix dena egiteko. Ez da software gehigarririk behar.
