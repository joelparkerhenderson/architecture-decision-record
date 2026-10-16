# Metrikas, uzraudzība, brīdinājumi

Saturs:

* [Kopsavilkums](#kopsavilkums)
  * [Jautājums](#jautājums)
  * [Lēmums](#lēmums)
  * [Statuss](#statuss)
* [Detaļas](#detaļas)
  * [Pieņēmumi](#pieņēmumi)
  * [Ierobežojumi](#ierobežojumi)
  * [Pozīcijas](#pozīcijas)
  * [Arguments](#arguments)
  * [Sekas](#sekas)
* [Saistītais](#saistītais)
  * [Saistītie lēmumi](#saistītie-lēmumi)
  * [Saistītās prasības](#saistītās-prasības)
  * [Saistītie artefakti](#saistītie-artefakti)
  * [Saistītie principi](#saistītie-principi)
* [Piezīmes](#piezīmes)
  * [Brīvi teksta ziņojumi pret strukturētiem notikumu ziņojumiem](#brīvi-teksta-ziņojumi-pret-strukturētiem-notikumu-ziņojumiem)
  * [Graylog ir vienkāršāks](#graylog-ir-vienkāršāks)
  * [Prometheus prasa zināmu pielāgošanu](#prometheus-prasa-zināmu-pielāgošanu)
  * [AWS pakalpojumi ir dažādi](#aws-pakalpojumi-ir-dažādi)
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
  * [Datadog pret Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack](#datadog-pret-site24x7--statuscake--pagerduty--sumologic--slack)
  * [Prometheus + AlertManager + Grafana + Stackdriver](#prometheus--alertmanager--grafana--stackdriver)
  * [Zabbix](#zabbix-1)


## Kopsavilkums


### Jautājums

Mēs vēlamies izmantot metrikas, uzraudzību un brīdinājumus, jo vēlamies zināt, cik labi darbojas mūsu lietojumprogrammas, un zināt, kad rodas problēma.


### Lēmums

Darbs procesā (WIP).


### Statuss

Informācijas vākšana. Mēs sākam ar ticamiem spektra galiem: visvairāk ieteikto vecāko bezmaksas rīku (Nagios) un visvairāk ieteikto jaunāko maksas rīku (New Relic).


## Detaļas


### Pieņēmumi

Mēs vēlamies izveidot tīmekļa lietotnes, kas ir modernas, ātras, uzticamas, atsaucīgas utt.

Mēs vēlamies pirkt, nevis būvēt.


### Ierobežojumi

Mēs vēlamies rīkus, kas labi darbojas ar mūsu DevOps cauruļvadu un ar mūsu izvietošanas mākoņiem.


### Pozīcijas

Mēs pašlaik pētām pozīcijas.


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

  
### Arguments

Līdz šim Nagios un New Relic ir spektra gali. Nagios ir vecākais, vienkāršākais, bezmaksas, dzīvotspējīgais rīks. New Relic ir jaunākais pēc funkcijām, pilnīgākais, maksas, dzīvotspējīgais rīks. Mēs sāksim ar šo izvērtēšanu. Pēc vajadzības mēs pārvietosimies spektrā.  

Līdz šim Zabbix ir labākās rekomendācijas un piedāvā arī pilnīgākās iespējas.

Līdz šim ELK ir labākā atvērtā pirmkoda populāritāte pēc principa „būvēt, nevis pirkt”.

Līdz šim Prometheus + Graphana ir labākā populāritāte.


### Sekas

TODO.


## Saistītais


### Saistītie lēmumi

Izvēles ietekmēs testējamību, telemetriju un, visticamāk, citas sistēmas, piemēram, klientu apkalpošanai, vietņu uzticamības inženierijai utt.


### Saistītās prasības

TODO.


### Saistītie artefakti

TODO.


### Saistītie principi

Viegli atgriezenisks.

Nepieciešamība pēc ātruma.


## Piezīmes


Diezgan labs atvērtā pirmkoda steks ir:

* Prometheus metrikām un uz metrikām balstītiem brīdinājumiem

* Grafana metriku attēlošanai

* Elasticsearch/Logstash/Kibana (ELK) žurnāliem un strukturētiem notikumiem

* Pushover mobilajiem paziņojumiem


### Brīvi teksta ziņojumi pret strukturētiem notikumu ziņojumiem

Brīvi teksta ziņojumi: piemēram, nejauša satura veids, ko atradīsit /var/log/messages, un kaut kas, ko lietojumprogramma ģenerē tīši. Ziņojumi ir noderīgi citu notikumu apzināšanai uz mašīnas, piemēram, atmiņas trūkumam vai aparatūras kļūdām, bet satur daudz atkritumu. 

Strukturēti notikumu ziņojumi: ģenerē lietojumprogramma, ar fiksētu vai dinamisku atribūtu kopu, piem., HTTP pieprasījumu žurnāls, grāmatvedības žurnāls, lietotāja pieteikšanās.

Vispār ir jauki žurnalēt detaļas par katru pieprasījumu tā, lai varētu detalizēties pēc atribūtiem. Tātad, pievienojot, piem., userid vai sessionid visam, var izsekot. Skaidra izsekošana, protams, arī ir laba. ELK izmantošana šim nolūkam ir sava veida nabaga cilvēka https://www.honeycomb.io/


### Graylog ir vienkāršāks

Graylog pēc manas pieredzes ir vieglāk palaižams.



### Prometheus prasa zināmu pielāgošanu


Es kopumā esmu apmierināts ar Prometheus metrikām. Brīdināšana prasa zināmu pielāgošanu, bet ir diezgan laba. Tā ir atkarīga no jūsu lietojumprogrammas. Es uzskatu, ka vislabāk ir brīdināt par stāvokļiem, kas redzami gala lietotājam, nevis pamatā esošajiem cēloņiem. Piemēram, lapas ielādes laiks ir labs, pieprasījumu skaits sekundē nav. Lai gan nulle pieprasījumu sekundē norāda, ka kaut kas nav kārtībā.

Pakalpojuma priekšrocība ir tā, ka tie piedāvā papildu intelektu uzreiz. Man kopumā patīk Datadog. Pakalpojumi var būt biedējoši dārgi, ja jums ir daudz datu, un dažreiz tiem ir cenu modeļi, kas nav draudzīgi mākonim, piem., iekasē par instanci, kad instances ir dinamiskas. Pastāv arī atšķirība starp pakalpojumiem, kur katrs pieprasījums ir no maksājoša lietotāja, un tiem, kas ir saistīti ar reklāmu, tāpēc tikai neliels pieprasījumu procents nes naudu. Jūs varat nonākt pie daudz datu un ne tik liela budžeta.

Es strādāju pie dažiem pakalpojumiem, kas saņem 1 miljardu pieprasījumu dienā, tāpēc ir jēga mitināt savu uzraudzību un žurnalēšanu. Ja jūsu apjomi ir mazāki, mitinātie pakalpojumi ir vienkāršāki.


### AWS pakalpojumi ir dažādi

Mana pieredze ar AWS pakalpojumiem ir dažāda. Viņu Elasticsearch pakalpojums ir bijis nestabils, tāpēc mēs to darbinām ar savām instancēm. CloudWatch metrikas ir dārgas, tāpēc mēs tās parasti izmantojam tikai „infrastruktūras” līmeņa metrikām, nevis lietojumprogrammai, t. i., ar veselību saistītām metrikām, kur AWS var labāk zināt, kas notiek, nekā instancē darbojošamies programmatūrai. CloudWatch Logs var lēni atjaunināties un tiem nav daudz metadatu. ELK darbināšana tajā palīdz. Ja es patiešām vēlos reāllaika datus, tad Kafka izmantošana kā žurnālu transports ir labāka. To Logstash diezgan labi atbalsta. Tomēr Kafka klastera pārvaldība nav vājajiem, ir izvērsti daudz santehnikas.


### Kafka

Komentārs: Kafka dažreiz var būt ļoti sarežģīta, vai arī Kafka var būt stabila kā klints, un jūs gandrīz aizmirstat, ka tā tur ir un visu sasaista kopā. 


Komentārs: Kafka ir bijusi stabila, bet tās palaišana prasīja pārsteidzoši daudz darba. Es to uzskatu par relāciju datubāzi, bet jūs strādājat tikai „fiziskajā” slānī, piem., tabulu telpās, failos un nodalījumos. Agrīnā posmā bija laiki, kad pārvaldības utilītu trūka, un mums bija jāraksta programmas, piem., lai atiestatītu patērētāju grupu. http://howfuckedismydatabase.com/nosql/

Komentārs: Mēs izmantojam Kafka kā žurnālu ziņojumu „buferi” un vietu, kur varam veikt reāllaika straumes apstrādi datiem, kas nāk no vairākiem serveriem. Ja saņemam DDOS uzbrukumu, mums vajag veidu, kā analizēt datus pa vairākām instancēm. Ja žurnalējam tieši no serveriem uz ELK, slodze var uzspridzināt Elasticsearch klasteri.

Komentārs: Kafka mums ir laba, jo, ja saņemam DDOS uzbrukumu, mums vajag veidu, kā analizēt datus pa vairākām instancēm. Ja žurnalējam tieši no serveriem uz ELK, slodze var uzspridzināt Elasticsearch klasteri.


Komentārs: Kafka dara mazāk darba un ir efektīvāka, tāpēc var labāk apstrādāt slodzi. Un mēs ierindojam Kafka darbu rindā un mēģinām vēlreiz. Un Kafka pārslogošana neietekmē lietotājus, kuri mēģina strādāt interaktīvi ar Kibana, kā tas notiktu, ja Elasticsearch ciestu.

Komentārs:  Straumes apstrāde galvenokārt meklē ļaunprātīgu izmantošanu, piem., pārāk daudz datplūsmas no viena IP visā klasterī, un pēc tam kopīgo bloķēšanu visā klasterī.

Komentārs: Spraudnis logstash-output-kafka pašlaik ir diezgan nestabils. Mani ir skārušas vairākas problēmas tā GitHub issues lapā, kas, šķiet, nekad netiek novērstas. Es vēlos atteikties no tā izmantošanas un sūtīt tieši no mūsu lietotnēm uz Kafka.

Komentārs: Mēs tagad sūtām strukturētus notikumus tieši no lietotnes uz Kafka. Galvenā motivācija bija pieskarties žurnāla datiem mazāk reižu un izvairīties no diska vairākkārtējas lasīšanas un rakstīšanas. Augsta apjoma sistēmās žurnalēšana var prasīt vairāk darba nekā pati lietotne. Es domāju par to, lai journald arī sūtītu žurnālus tieši, no C programmas.


### Loki

Cieši sekojiet Loki. Tas vēl nav gatavs, bet, kad būs, es sagaidu, ka tas labāk iederēsies šajā stekā. Loki ir žurnālu agregators, ko izveidojis grafana labs, tas izmanto līdzīgu skrāpēšanas un birku sintaksi kā Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager metrikām. <3 Prometheus.

Rollbar/Graylog žurnalēšanai/kļūdu ziņošanai (šeit ir zināma pārklāšanās; maziem pakalpojumiem, iespējams, nevajag abus).

Pašlaik brīdinājumi iet tikai uz vienu no dažiem Slack kanāliem, kuros ieinteresētās puses ir ieslēgušas paziņojumus. Ja mēs būtu nopietnāki par dežūrēšanu, tie ietu uz PagerDuty/VictorOps/utt.

Grafana grafikiem un informācijas paneļiem. Arī nepacietīgi gaidu, vai viņu gaidāmās žurnalēšanas iespējas novērsīs Graylog nepieciešamību.


### Thanos

Mēs izmantojam Thanos kā priekšgalu mūsu HA iestatījumam. Tas zina, kā atdublēt HA pārus.

Pašlaik mēs glabājam 6 mēnešus lokālo Prometheus datu. Tas mums diezgan labi darbojas. Bet es esmu tieši vidū, ieviešot kausa glabāšanu (bucket storage) mūsu Thanos iestatījumā ilgtermiņa datu glabāšanai. Teorētiski GCS glabāšana būs apmēram par 30 % lētāka nekā GCE standarta pastāvīgais disks, ko izmantojam tagad.

Mēs pašlaik neveidojam Prometheus datu rezerves kopijas. Dati mums īsti nav svarīgi, izņemot to, lai pietiktu brīdināšanai. Mūsu kopējā flotes izvietošana tik daudz mainās gadu no gada, ka vēsturiski dati, kas vecāki par dažiem mēnešiem, vienkārši nav interesanti. Varētu būt interesanti, ja būtu daži galvenie statistikas rādītāji gadu no gada; es varētu iestatīt galveno rādītāju ierakstīšanas noteikumu kopu un glabāt tos ar Federation vai vienkārši ļaut Thanos par to parūpēties.

EDIT: neliels atrunas teikums: esmu Prometheus izstrādātājs.


### Prometheus HA

HA Prometheus tiek veikts ar dublēšanu; jūs darbināt vairākus aptaujātājus (pollers), un ir veidi, kā aptaujāt vairākus un atdublēt datus

Mērogošana notiek, lemjot par tīklu un ļaujot dažādiem Prometheus aptaujāt dažādas tīkla daļas

Ilgtermiņa glabāšana nav Prometheus stiprā puse, bet tiek nodota kaut kam līdzīgam kā influx vai timescaledb (kas tehniski arī izpilda HA ķeksīti); raksts, ko par to lasīju: https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Ilgtermiņa lietas vēl neesmu izmēģinājis, jo joprojām tikai eksperimentēju un izmantoju to īstermiņa grafikiem, kamēr librenms uzrauga manu tīklu ilgtermiņam


### Datadog + PagerDuty + Threat Stack

Mēs izmantojam Datadog (ar PagerDuty) un Threat Stack un nevarētu būt apmierinātāki. Mana vienīgā sūdzība par DD ir samērā augstās metriku glabāšanas izmaksas.


### Zabbix

Zabbix ar pielāgotiem skriptiem, lai uzraudzītu gandrīz visu. Darbojas kā pa sviestu.


### Outlyer

Es izmantoju Outlyer, bet man jāatklāj, ka es šeit strādāju, un paša produkta lietošana (dog fooding) ir obligāta.

Uzlabošanai joprojām vajag Graylog, Sentry un Statuscake.

Skan pretenciozi, bet, labprāt iekšēji darbinājis Nagios un citas uzraudzības sistēmas, es jebkurā jaunā darbā pirktu mitinātu risinājumu un atbrīvotos no šīm sāpēm.


### Nagios + Nagiosgraph

Mēs darbinām Nagios visai uzraudzībai un brīdināšanai. Brīdinājumi notiek pa e-pastu (brīdinājumi un kritiski paziņojumi) un dzirdamiem lietotnes paziņojumiem (kritiskiem brīdinājumiem).

Nagiosgraph tiek izmantots vizualizācijām.

Šis iestatījums ir bijis ļoti efektīvs, lai mūs visaptveroši informētu par to, kas notiek mūsu vidē. Mēs darbinām un uzraugām apmēram 110 misijai kritiskus serverus un apmēram 760 datu punktus, un šī rīta sistēma mums ir izveidota vairāk nekā septiņus gadus.

Es vēlētos kādreiz arī apkopot žurnālus ar Graylog vai ELK.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager, izmantojot lielisko Prometheus Operator helm diagrammu. Žurnāli joprojām iet uz LogDNA birch plānu, jo mēs pamanījām, ka ELK ir pārāk smags mūsu pazemīgajiem min 3 maks 5 mezgliem uz GKE.


### DataDog + Sentry + PagerDuty.

Agrāk es darbināju visus savus uzraudzības risinājumus, izmantojot visāda veida programmatūru, tostarp Nagios, Icinga, Zabbix, ELK, Greylog2, Influx un daudzus citus rīkus, taču patiesība ir tāda, ka savas uzraudzības infrastruktūras darbināšanā ir iesaistīts pārāk daudz pūļu, īpaši, kad varat citiem samaksāt tik zemas cenas, lai kāds cits to izdarītu jūsu vietā!

Citu maksāšana par uzraudzības infrastruktūras darbināšanu atbrīvo manus klientus, lai viņi koncentrētos uz savu platformu darbināšanu, nevis uzraudzības uzraudzību, kas nozīmē, ka vērtība, ko viņi iegūst no savas platformas stabilitātes, tālu pārsniedz jebkādas uzraudzības kā pakalpojuma izmaksas.


### Sensu + Graphite + ELK

Mans uzņēmums ļoti uzstāj uz pašmitinātām lietām.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager brīdināšanai; mana komanda uzskata, ka vienkārša uzraudzība ir laba uzraudzība.

Citas sistēmas, piemēram, žurnalēšana un izsekošana, nodrošinās bagātu kontekstu diagnostikai, kad dežurants saņem brīdinājumu, bet mēs nekad neveidojam brīdināšanu uz tām.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Prometheus instrumentēti pakalpojumi => Circonus analītika un vizualizācija


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Mēs izmantojam tālāk minētos pakalpojumus:

icinga2 uzraudzībai un VictorOps brīdināšanai

NewRelic pakalpojuma detalizētai uzraudzībai

Sentry kļūdu izsekošanai pakalpojumā

Slack/e-pasts ir brīdināšanas daļa, kas tiek ierosināta no NewRelic vai icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 ar elasticsearch integrāciju analīzei un graphite+grafana integrāciju grafikiem.

pateicoties icinga2 apply noteikumu elastībai, izstrādātāji redz tikai pakalpojumus, par kuriem viņi saņem paziņojumus.

un ar icinga2 director programmētāji var viegli definēt savas pārbaudes (ko viņi dara, ik pēc dažām dienām – 100 pārbaudes iziet, 100 citas pārbaudes ienāk) lielā mērogā bez problēmām.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Kas mums ir tagad:

DataDog metrikām

New Relic lietojumprogrammu uzraudzībai

ELK (Elastic Search + Logstash + Kibana) žurnāliem

Sentry (pašmitināts) izņēmumu žurnalēšanai

E-pasti + Slack + VictorOps brīdināšanai (atkarībā no nopietnības)

Ko mēs vēlamies:

Prometheus metrikām (Grafana vizualizācijai)

New Relic (iespējams, Elastic Search APM) lietojumprogrammu uzraudzībai

EFK (elastic search + fluentd + kibana) žurnalēšanai. Iespējams, Grafana Loki būs gatavs ražošanai līdz brīdim, kad mēs tur nonāksim

Sentry izņēmumiem

Alertmanager + e-pasts + VictorOps brīdinājumiem


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (atruna: strādā VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf servera metrikām, piemēram, CPU, diskam, atmiņai un tīklam. Mēs izmantojam Telegraf arī savu tīkla ierīču SNMP uzraudzībai.

Prometheus lietojumprogrammu metrikām. Mēs savā lietojumprogrammā iekodējam veselības pārbaudes, kuras Prometheus skrāpē.

InfluxDB laika rindu glabāšanai. Šeit tiek sūtīti mūsu Telegraf dati.

Grafana informācijas paneļiem un brīdinājumiem. Brīdināšanas dzinējs nav īpaši robusts, bet tas dara savu darbu. Mēs sūtām brīdinājumus arī uz Slack.

Tas, kā man pašlaik nav, ir centralizēts žurnalēšanas risinājums. ELK ir jaudīgs, bet grūti uzstādāms un pārvaldāms, un es nezinu nevienu bezmaksas alternatīvu, kas būtu pietiekami tuvu, lai tās izpētītu.


### Sematext + Logagent + Experience

Sematext metrikām, žurnāliem, izsekām, drīz arī reālo lietotāju uzraudzībai. Pēc manām domām, vienkāršāk/lētāk nekā N dažādu rīku/pakalpojumu izmantošana.

Žurnālu sūtīšanai mēs agrāk izmantojām rsyslog, un tad pārgājām uz Logagent.

Priekšpuses avāriju ziņošanai mēs izmantojam Sentry, bet drīz pāriesim uz Experience.

Atruna: esmu sematextietis.


### Azure Monitor/Analytics + OpsGenie

Es vēlētos, lai Log Analytics būtu labāka saskarne. Mēs attālināmies no splunk, kurā bija daudz vieglāk orientēties.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Jūs patiešām nevēlaties darbināt savu paziņojumu sistēmu. Splunk varat aizstāt ar ELK, ja vien jūsu drošības komanda nedod priekšroku Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf kā vācējs, Prometheus + Alertmanager uzraudzībai un brīdināšanai, integrēts ar slack kanāliem un pagerduty kritiskiem brīdinājumiem. Grafana resursdatoru metriku vizualizācijai.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus metrikām + brīdinājumiem

Grafana Prometheus informācijas paneļiem

Cloudwatch uzrauga Prometheus instances

sentry izņēmumu izsekošanai

kibana + elasticsearch

graylog

prometheus Push Gateway pakešu/cronjobs uzdevumiem

SOP https://github.com/rapidloop/sop, lai „pushotu/forwardotu” metrikas no vienas Prometheus instances uz citu

klienti izmanto Prometheus klientus. Mēs cenšamies klienta pusē izmantot opencensus.io


### PagerDuty + Monitis

PagerDuty + Monitis. Arī daži pielāgoti Azure Functions dažu pakalpojumu veselības pārbaudei.

Šogad plānoju ieviest Prometheus un Grafana


### Prometheus + Grafana + Bosun

Prometheus laika rindu datu glabāšanai. Grafana vizualizācijai. Bosun brīdinājumu pārvaldībai.


### Azure Monitor/Analytics/Insights/Dashboards

Tikai Azure uzņēmums, Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana konteineru pakalpojumu uzraudzībai Kubernetes, izmantojot Prometheus

Monitis pilna cikla pakalpojumu uzraudzībai, galvenokārt tīmekļa API un tīmekļa lietojumprogrammām

OpsGenie brīdinājumu pārvaldībai

Slack statusa informācijas saņemšanai no mūsu sistēmām


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Ilggadējs (dev)ops inženieris. Uzaugu ar Nagios. Ar prieku uzklausītu viedokļus par manu pašfinansēto SaaS https://checklyhq.com. Mēs veicam API uzraudzību un vietnes darījumu uzraudzību ar diezgan padziļinātu brīdināšanu.

Es sāku Checkly, jo aktīvā / sintētiskā uzraudzība API telpā bija nedaudz ierobežota (un dārga). Uz pārlūkprogrammu balstīta / skriptēta uzraudzība ir vēl patentētāka un dārgāka. Mēs izmantojam Puppeteer un cenas turam pēc iespējas zemākas.

Mūsu uzraudzības steks:

Checkly (dog fooding...)

AppOptics (pielāgoti grafiki)

AWS Cloudwatch un SNS SMS ziņojumiem.

iebūvētā Heroku brīdināšana.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana mūs brīdina slack par infrastruktūras problēmām vai veiktspējas pasliktināšanos, un mēs esam konfigurējuši logz.io brīdināt slack par noteiktu kļūdu līmeņa žurnālu apjomu no lietojumprogrammu slāņa.


### SignalFX + Splunk + PagerDuty + Slack

Pašlaik izmantoju: SignalFX, Splunk, PagerDuty un Slack. SignalFX nav man īpaši patīkams, lai gan viņu atbalsta komanda ir ļoti draudzīga un atsaucīga. Splunk man patīk (ir vērts, ja varat to atļauties), PagerDuty un Slack.

Agrāk es izmantoju TICK steku, kur lielākā daļa C patiesībā bija G, t. i., Grafana, lai gan es nedaudz izmantoju arī Chronograf. Tas bija lieliski, bet sāpīgi pārvaldāms. Klasiskā SaaS pret pašmitināšanu dilemma.

Esmu izmantojis DataDog, New Relic, Graylog, ELK un BugSnag. DataDog un New Relic man ļoti patīk, Graylog ir diezgan labs. ELK man īpaši nepatīk. BugSnag ir jauks; patiesībā uzskatu, ka kļūdu/izņēmumu izsekošana daudzos gadījumos ir diezgan labs pilnas žurnālu uzraudzības aizvietotājs.


### ELK + Prometheus + Grafana

Tāpat kā citi, mēs izmantojam ELK žurnāliem un Prometheus+Grafana visam pārējam.

Šī iestatījuma uzturēšana ir viegla, ja atļaujat sev laiku pa laikam zaudēt datus. Piemēram, ja mūsu ElasticSearch datubāze nonāk sliktā stāvoklī (kas mums diemžēl notiek ik pēc 2–3 mēnešiem), mēs neņemamies ar HA, bet izmetam datus un dzīvojam tālāk. Ja jums absolūti vajag HA vai ilgtermiņa glabāšanu, veiksmi.


### Datadog + Prometheus + Grafana

Es iestatīju Datadog mēnesi mēnesī, jo, kad es šeit nonācu, nebija ne uzraudzības, ne brīdināšanas. Tikai daži no mūsu vietnēm tika uzraudzītas ik pēc 5 minūtēm darbspējai. Datadog ir neapšaubāmi vieglāk iestatāms. Kad būšu pabeidzis risināt visas pārējās problēmas, pāriešu uz Prometheus+Grafana. Par žurnālu pārvaldību vēl neesmu 100 % izlēmis.

### Nagios + ELK

Mēs atbalstām vairāk nekā 100 produktus.

Lokālajam (on-prem) pārsvarā ir Nagios un ELK. Mākonim mēs migrējam no DataDog uz NewRelic.


### Datadog pret Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Mēs agrāk izmantojām datadog, bet atklājām, ka tas ir pārāk dārgs mūsu vajadzībām. Nesaprotiet mani nepareizi, tas ir pārsteidzošs, bet tam ir milzīgas izmaksas. Mēs varējām iestatīt site24x7.com ar gada abonementu par aptuveni 2–3 DD izmaksu mēnešiem.

Mūsu uzraudzības steks:

Site24x7 – APM, ārējo URL uzraudzība, SMTP pasta plūsmas uzraudzība, ssl derīguma termiņi un procesu uzraudzība.

StatusCake – URL uzraudzībai un apstiprināšanai – tā ir mūsu rezerve gadījumam, ja site24x7 kaut ko palaiž garām (nepalaiž), bet SC ir elastīgāks ārējo portu un pakalpojumu uzraudzībai mūsu vajadzībām.

Abi rīki eskalē uz PagerDuty, un tad mēs saņemam eskalācijas slack.

SumoLogic – žurnālu uzraudzībai (tas ir lielisks rīks, bet nedaudz sarežģīts mūsu vajadzībām)

No slack mēs varam apstiprināt vai novērst brīdinājumu.

Tad mums ir daudz site24x7 automatizāciju, kas savienojas ar commando.io „BedOps” (kā mēs to saucam) – kad tiek ierosināts brīdinājums, mēs palaižam dažus skriptus vai automatizācijas kā mēģinājumu novērst situāciju (99 % gadījumu automatizācija + mūsu skripti mūs notur ārpus nepatikšanām).

Mums ir iekšējās rokasgrāmatas (runbooks) mūsu zināšanu bāzē (KB) gadījumiem, kad automatizācijas neizdodas vai ir kaut kas ārpus apjoma, kas jālabo.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana metrikām mūsu GKE klasteros un VM.

Google Stackdriver žurnāliem (jo tas ir iekļauts un pēc noklusējuma aktīvs un pašlaik pietiek mūsu vajadzībām).


### Zabbix

Zabbix visam. Papildu programmatūra nav vajadzīga.
