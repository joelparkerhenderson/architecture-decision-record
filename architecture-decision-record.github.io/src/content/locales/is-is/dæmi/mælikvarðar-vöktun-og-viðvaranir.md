# Mælikvarðar, vöktun og viðvaranir

Efnisyfirlit:

* [Samantekt](#samantekt)
  * [Vandamál](#vandamál)
  * [Ákvörðun](#ákvörðun)
  * [Staða](#staða)
* [Nánar](#nánar)
  * [Forsendur](#forsendur)
  * [Takmarkanir](#takmarkanir)
  * [Afstöður](#afstöður)
  * [Röksemd](#röksemd)
  * [Afleiðingar](#afleiðingar)
* [Tengt](#tengt)
  * [Tengdar ákvarðanir](#tengdar-ákvarðanir)
  * [Tengdar kröfur](#tengdar-kröfur)
  * [Tengdar afurðir](#tengdar-afurðir)
  * [Tengdar meginreglur](#tengdar-meginreglur)
* [Athugasemdir](#athugasemdir)
  * [Frjáls textaskilaboð á móti skipulögðum atburðaskilaboðum](#frjáls-textaskilaboð-á-móti-skipulögðum-atburðaskilaboðum)
  * [Graylog er auðveldara](#graylog-er-auðveldara)
  * [Prometheus þarfnast fínstillingar](#prometheus-þarfnast-fínstillingar)
  * [AWS-þjónustur eru misjafnar](#aws-þjónustur-eru-misjafnar)
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
  * [Datadog á móti Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack](#datadog-á-móti-site24x7--statuscake--pagerduty--sumologic--slack)
  * [Prometheus + AlertManager + Grafana + Stackdriver](#prometheus--alertmanager--grafana--stackdriver)
  * [Zabbix](#zabbix-1)


## Samantekt


### Vandamál

Við viljum nota mælikvarða, vöktun og viðvaranir, því við viljum vita hversu vel forrit okkar virka og vita hvenær vandamál koma upp.


### Ákvörðun

Í vinnslu.


### Staða

Söfnum upplýsingum. Við byrjum á trúverðugum endum litrófsins: mest ráðlagða eldra ókeypis tólinu (Nagios) og mest ráðlagða nýrra greidda tólinu (New Relic).


## Nánar


### Forsendur

Við viljum búa til vefforrit sem eru nútímaleg, hröð, áreiðanleg, svörunarfús o.s.frv.

Við viljum kaupa frekar en smíða.


### Takmarkanir

Við viljum verkfæri sem virka vel með devops-leiðslu okkar og með skýjunum sem við setjum upp í.


### Afstöður

Við erum að rannsaka afstöður núna.


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

  
### Röksemd

Hingað til eru Nagios og New Relic endar litrófsins. Nagios er elsta, einfaldasta, ókeypis og raunhæfa tólið. New Relic er nýjasta, fullkomnasta, greidda og raunhæfa tólið með nýjustu eiginleikana. Við munum byrja á mati á þessum. Eftir þörfum munum við færa okkur inn í litrófið.  

Hingað til hefur Zabbix bestu meðmælin og býður einnig upp á fullkomnustu getuna.

Hingað til hefur ELK bestu vinsældirnar í opnum hugbúnaði þegar kemur að smíða-frekar-en-kaupa.

Hingað til hafa Prometheus + Graphana bestu vinsældirnar.


### Afleiðingar

Á eftir að gera.


## Tengt


### Tengdar ákvarðanir

Valið mun hafa áhrif á prófanleika, fjarmælingar og líklega önnur kerfi, svo sem fyrir þjónustu við viðskiptavini, áreiðanleikaverkfræði vefsvæða o.s.frv.


### Tengdar kröfur

Á eftir að gera.


### Tengdar afurðir

Á eftir að gera.


### Tengdar meginreglur

Auðafturkræft.

Þörf fyrir hraða.


## Athugasemdir


Ansi góður opinn stafli er:

* Prometheus fyrir mælikvarða og viðvaranir byggðar á mælikvörðum

* Grafana til að sýna mælikvarða

* Elasticsearch/Logstash/Kibana (ELK) fyrir logga og skipulagða atburði

* Pushover fyrir farsímatilkynningar


### Frjáls textaskilaboð á móti skipulögðum atburðaskilaboðum

Frjáls textaskilaboð: til dæmis það tilviljanakennda sem þú finnur í /var/log/messages, og eitthvað sem forritið býr til af ásettu ráði. Skilaboðin eru gagnleg til að bera kennsl á aðra hluti sem eru að gerast á vélinni eins og minnisskort eða vélbúnaðarvillur, en innihalda mikið rusl. 

Skipulögð atburðaskilaboð: búin til af forritinu, með föstu eða kviku safni eiginda, t.d. HTTP-beiðnalogg, bókhaldslogg, notendainnskráning.

Almennt séð er gott að skrá nákvæmar upplýsingar um hverja beiðni þannig að hægt sé að kafa niður eftir eigindum. Að bæta t.d. userid eða sessionid við allt gerir kleift að rekja. Skýr rekning er að sjálfsögðu líka góð. Að nota ELK fyrir þetta er eins konar fátækramanns útgáfa af https://www.honeycomb.io/


### Graylog er auðveldara

Graylog er auðveldara að koma í gang samkvæmt minni reynslu.



### Prometheus þarfnast fínstillingar


Ég er almennt ánægður með Prometheus fyrir mælikvarða. Viðvaranir þarfnast fínstillingar, en eru ansi góðar. Það fer eftir forritinu þínu. Ég held að best sé að senda viðvaranir um ástand sem endanotandi sér, ekki undirliggjandi orsakir. Til dæmis er hleðslutími síðu gott, fjöldi beiðna á sekúndu er það ekki. Þó gefur núll beiðnir á sekúndu til kynna að eitthvað sé að.

Kosturinn við þjónustu er að hún býður upp á aukna greind beint úr kassanum. Mér líkar almennt vel við Datadog. Þjónusturnar geta verið ógnvekjandi dýrar ef þú hefur mikið af gögnum og hafa stundum verðlíkön sem eru ekki skýjavæn, t.d. gjald á hvert tilvik þegar tilvik eru kvik. Einnig er munur á þjónustum þar sem hver beiðni kemur frá greiðandi notanda og þeim sem tengjast auglýsingum, þar sem aðeins lítið hlutfall beiðna aflar þér tekna. Þú getur endað með mikið af gögnum en ekki svo mikinn fjárhag.

Ég vinn við nokkrar þjónustur sem fá 1 milljarð beiðna á dag, svo það er skynsamlegt að hýsa okkar eigin vöktun og skráningu. Ef umfangið er minna eru hýstar þjónustur auðveldari.


### AWS-þjónustur eru misjafnar

Reynsla mín af AWS-þjónustum hefur verið misjöfn. Elasticsearch-þjónusta þeirra hefur verið óstöðug, svo við keyrum okkar eigin tilvik fyrir það. CloudWatch-mælikvarðar eru dýrir, svo við notum þá yfirleitt aðeins fyrir mælikvarða á „innviðastigi“ frekar en forritið, þ.e. heilsutengda mælikvarða þar sem AWS getur vitað betur hvað er að gerast en hugbúnaður sem keyrir á tilvikinu. CloudWatch Logs geta verið hægir að uppfærast og hafa ekki svo mikið af lýsigögnum. ELK hjálpar með það. Ef ég vil virkilega rauntímagögn er betra að nota Kafka sem flutning fyrir logga. Það er ansi vel stutt af Logstash. Að stýra Kafka-þyrpingu er þó ekki fyrir viðkvæma, þar er mikið af berskjölduðum lögnum.


### Kafka

Athugasemd: Kafka getur verið ofurvandasamt á köflum, eða Kafka getur verið traust sem klettur og þú gleymir næstum að það sé þarna og bindi allt saman. 


Athugasemd: Kafka hefur verið traust, en það var ótrúlega mikil vinna að koma því í gang. Ég hugsa um það eins og venslagagnagrunn en þú vinnur aðeins á „efnislega“ laginu, t.d. töflurýmum, skrám og hólfum. Það voru tímar snemma þar sem stjórnunarverkfærin voru ábótavant og við þurftum að skrifa forrit til að t.d. endurstilla neytendahóp. http://howfuckedismydatabase.com/nosql/

Athugasemd: Við notum Kafka sem „biðminni“ fyrir logga og stað þar sem við getum gert rauntíma straumvinnslu á gögnum sem koma frá mörgum þjónum. Ef við verðum fyrir DDOS-árás þurfum við leið til að greina gögn þvert á mörg tilvik. Ef við skráum beint frá þjónunum í ELK getur álagið sprengt Elasticsearch-þyrpinguna.

Athugasemd: Kafka er gott fyrir okkur því ef við verðum fyrir DDOS-árás þurfum við leið til að greina gögn þvert á mörg tilvik. Ef við skráum beint frá þjónunum í ELK getur álagið sprengt Elasticsearch-þyrpinguna.


Athugasemd: Kafka vinnur minna og er skilvirkara, svo það ræður betur við álagið. Og við röðum Kafka-vinnunni og reynum aftur. Og það að Kafka sé yfirálagað hefur ekki áhrif á notendur sem reyna að vinna gagnvirkt í Kibana, eins og það myndi gera ef Elasticsearch ætti í erfiðleikum.

Athugasemd:  Straumvinnsla leitar aðallega að misnotkun, t.d. of mikilli umferð frá einu IP-vistfangi þvert á alla þyrpinguna, og deilir svo lokuninni þvert á alla þyrpinguna.

Athugasemd: Logstash-output-kafka viðbótin er þó nokkuð óáreiðanleg eins og er. Ég hef orðið fyrir nokkrum vandamálum á GitHub issues síðu hennar, sem virðast aldrei verða lagfærð. Ég vil hætta að nota hana og senda beint frá forritum okkar til Kafka.

Athugasemd: Við sendum nú skipulagða atburði beint frá forritinu til Kafka. Helsta hvatningin var að snerta logggögnin sjaldnar og forðast að lesa og skrifa á diskinn mörgum sinnum. Í kerfum með miklu umfangi getur skráning tekið meiri vinnu en forritið sjálft. Ég er að íhuga að láta journald senda logga beint líka, frá C-forriti.


### Loki

Fylgstu vel með Loki. Það er ekki tilbúið enn en þegar það verður það býst ég við að það passi betur í þennan stafla. Loki er loggasafnari búinn til af grafana labs, hann notar áþekka söfnun og merkjasetningafræði og Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager fyrir mælikvarða. <3 Prometheus.

Rollbar/Graylog fyrir skráningu/villuskýrslugerð (það er einhver skörun hér; lítil þjónusta þarf líklega ekki bæði).

Núna fara viðvaranir bara á eina af nokkrum Slack-rásum sem áhugasamir aðilar hafa kveikt á tilkynningum fyrir. Ef við værum alvarlegri varðandi bakvakt færu þær til PagerDuty/VictorOps/o.s.frv.

Grafana fyrir línurit og mælaborð. Hlakka einnig ákaft til að sjá hvort væntanlegur skráningarbúnaður þeirra geri Graylog óþarft.


### Thanos

Við notum Thanos sem framenda fyrir HA-uppsetningu okkar. Það kann að afrita ekki tvítekin HA-pör.

Við geymum nú 6 mánuði af staðbundnum Prometheus-gögnum. Þetta virkar nokkuð vel fyrir okkur. En ég er einmitt í miðju kafi að innleiða fötugeymslu í Thanos-uppsetningu okkar fyrir langtímageymslu gagna. Í kenningu verður GCS-geymsla um 30% ódýrari en GCE staðlaði varanlegi diskurinn sem við notum núna.

Við tökum ekki afrit af Prometheus-gögnum núna. Gögnin eru einfaldlega ekki mikilvæg fyrir okkur umfram að hafa nóg fyrir viðvaranir. Heildaruppsetning flota okkar breytist svo mikið frá ári til árs að söguleg gögn eldri en nokkra mánuði eru ekki svo áhugaverð. Gæti verið áhugavert að hafa nokkra kjarnatölfræði milli ára, ég gæti sett upp safn skráningarreglna fyrir kjarnatölfræði og geymt þær með Federation eða bara látið Thanos sjá um það.

BREYTING: Smávægilegur fyrirvari, ég er Prometheus-þróunaraðili.


### Prometheus HA

HA í Prometheus er gert með afritun, þú keyrir marga sækjara, það eru leiðir til að sækja úr mörgum og afrita ekki gögnin tvisvar

Stækkun er gerð með því að skipta netinu og láta ólík Prometheus sækja úr ólíkum hlutum netsins

Langtímageymsla er ekki sterka hlið Prom en er færð yfir í eitthvað eins og influx eða timescaledb (sem tæknilega setur líka HA-hak) grein sem ég las um það https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Hef ekki prófað langtímahlutina enn því ég er enn bara að gera tilraunir og nota það fyrir skammtímalínurit á meðan librenms vaktar netið mitt til langtíma


###  Datadog + PagerDuty + Threat Stack

Við notum Datadog (með PagerDuty) og Threat Stack og gætum ekki verið ánægðari. Eina kvörtun mín um DD er tiltölulega hár kostnaður við geymslu mælikvarða.


### Zabbix

Zabbix með sérsniðnum skriftum til að vakta nánast allt. Virkar eins og í sögu.


### Outlyer

Ég nota Outlyer, en ég verð að taka fram að ég vinn hér, og að nota eigin vöru er skylda.

Þarf enn Graylog, Sentry og Statuscake til að bæta við.

Hljómar hlutdrægt, en eftir að hafa glaður rekið Nagios og önnur vöktunarkerfi innanhúss myndi ég kaupa hýsta lausn í hvaða nýju starfi sem er og losa mig við þá plágu.


### Nagios + Nagiosgraph

Við keyrum Nagios fyrir alla vöktun og viðvaranir. Viðvaranir berast með tölvupósti (viðvaranir og mikilvægar tilkynningar) og hljóðtilkynningum í forriti (fyrir mikilvægar viðvaranir).

Nagiosgraph er notað fyrir sjónrænar framsetningar.

Þessi uppsetning hefur verið mjög áhrifarík við að halda okkur ítarlega upplýstum um hvað er að gerast í umhverfi okkar. Við rekum og vöktum um 110 mikilvæga þjóna og um 760 gagnapunkta, og höfum haft þetta morgunkerfi á sínum stað í yfir sjö ár.

Mig langar einnig að safna loggum saman með Graylog eða ELk einhvern tímann.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager í gegnum frábæra Prometheus Operator helm chart. Loggar fara enn til LogDNA birch áætlunarinnar því við tókum eftir að ELK er of þungt fyrir okkar hógværu lágmark 3 hámark 5 hnúta á GKE.


### DataDog + Sentry + PagerDuty.

Ég rak áður allar mínar eigin vöktunarlausnir með alls konar hugbúnaði, þar á meðal Nagios, Icinga, Zabbix, ELK, Greylog2, Influx og mörgum öðrum verkfærum, en sannleikurinn er sá að það er einfaldlega of mikil fyrirhöfn fólgin í að reka eigin vöktunarinnviði, sérstaklega þegar þú getur greitt öðrum svo lágt verð fyrir að gera það fyrir þig!

Að greiða öðrum fyrir að reka vöktunarinnviðina losar viðskiptavini mína til að einbeita sér að rekstri vettvanga sinna í stað þess að vakta vöktunina, sem þýðir að verðmætið sem þeir fá af stöðugleika vettvangsins vegur langt þyngra en nokkur kostnaður við vöktun sem þjónustu.


### Sensu + Graphite + ELK

Fyrirtækið mitt er mjög hallt undir sjálfhýst kerfi.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager fyrir viðvaranir, teymið mitt trúir því að einföld vöktun sé góð vöktun.

Önnur kerfi eins og skráning og rekning veita ríkt samhengi til greiningar þegar bakvaktin fær viðvörun, en við byggjum aldrei viðvaranir á þeim.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Prometheus-mæld þjónusta => greining og sjónræn framsetning í Circonus


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Við notum eftirfarandi þjónustur:

icinga2 fyrir vöktun og VictorOps fyrir viðvaranir

NewRelic fyrir ítarlega vöktun þjónustunnar

Sentry fyrir villurakningu í þjónustunni

Slack/tölvupóstur er hluti af viðvörunum sem kveikt er á frá NewRelic eða icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 með elasticsearch-samþættingu fyrir greiningu og graphite+grafana-samþættingu fyrir línurit.

þökk sé sveigjanleika apply-reglna í icinga2 geta þróunaraðilar aðeins séð þjónustur sem þeir fá tilkynningar um.

og í gegnum icinga2 director geta forritarar auðveldlega skilgreint sínar eigin athuganir (sem þeir gera á nokkurra daga fresti - 100 athuganir fara út, 100 aðrar koma inn) í stórum stíl án nokkurs vesens.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Hvað höfum við núna:

DataDog fyrir mælikvarða

New Relic fyrir forritavöktun

ELK (Elastic Search + Logstash + Kibana) fyrir logga

Sentry (sjálfhýst) fyrir skráningu undantekninga

Tölvupóstur + Slack + VictorOps fyrir viðvaranir (eftir alvarleika)

Hvað viljum við hafa:

Prometheus fyrir mælikvarða (Grafana fyrir sjónræna framsetningu)

New Relic (líklega Elastic Search APM) fyrir forritavöktunina

EFK (elastic search + fluentd + kibana) fyrir skráningu. Líklega verður Loki frá Grafana tilbúið fyrir framleiðslu þegar við komumst þangað

Sentry fyrir undantekningarnar

Alertmanager + tölvupóstur + VictorOps fyrir viðvaranirnar


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Fyrirvari: vinn hjá VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf fyrir þjónamælikvarða eins og CPU, disk, minni og net. Við notum einnig Telegraf fyrir SNMP-vöktun á nettækjum okkar.

Prometheus fyrir forritamælikvarða. Við kóðum heilsuathuganir inn í forritið okkar sem Prometheus sækir.

InfluxDB fyrir tímaraðageymslu. Þangað eru Telegraf-gögnin okkar send.

Grafana fyrir mælaborð og viðvaranir. Viðvörunarvélin er ekki ofurölug, en hún dugar. Við sendum einnig viðvaranir í Slack.

Það sem ég hef ekki núna er miðlæg skráningarlausn. ELK er öflugt en erfitt að setja upp og stýra, og ég veit ekki um neina ókeypis valkosti sem eru nógu nálægt til að skoða.


### Sematext + Logagent + Experience

Sematext fyrir mælikvarða, fyrir logga, fyrir rakningu, bráðum fyrir vöktun raunverulegra notenda líka. Einfaldara/ódýrara en að nota N ólík verkfæri/þjónustur, að mínu mati.

Fyrir sendingu logga notuðum við rsyslog en skiptum svo yfir í Logagent.

Fyrir hrunskýrslugerð á framenda notum við Sentry, en við skiptum bráðlega yfir í Experience.

Fyrirvari: Ég er Sematextan.


### Azure Monitor/Analytics + OpsGenie

Ég vildi að Log Analytics hefði betra viðmót. Við erum að færa okkur frá splunk, sem var mun auðveldara að rata um.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Þú vilt í alvöru ekki reka þitt eigið tilkynningakerfi. Þú getur skipt Splunk út fyrir ELK nema öryggisteymið þitt kjósi Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf sem safnari, Prometheus + Alertmanager fyrir vöktun og viðvaranir, samþætt við slack-rásir og pagerduty fyrir mikilvægar viðvaranir. Grafana fyrir sjónræna framsetningu á mælikvörðum véla.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus fyrir mælikvarða + viðvaranir

Grafana fyrir Prometheus-mælaborð

Cloudwatch vaktar Prometheus-tilvik

sentry fyrir rakningu undantekninga

kibana + elasticsearch

graylog

prometheus Push Gateway fyrir lotuvinnslu/cronverk

SOP https://github.com/rapidloop/sop til að „ýta/framsenda“ mælikvarða frá einu Prometheus-tilviki til annars

biðlarar nota annaðhvort Prometheus-biðlarana. Við reynum að nota opencensus.io á biðlarahliðinni


### PagerDuty + Monitis

PagerDuty + Monitis. Einnig nokkur sérsmíðuð Azure Functions til að prófa heilsu sumra þjónusta.

Hyggst taka upp Prometheus og Grafana á þessu ári


### Prometheus + Grafana + Bosun

Prometheus til að geyma tímaraðagögnin. Grafana fyrir sjónræna framsetningu. Bosun fyrir stýringu viðvarana.


### Azure Monitor/Analytics/Insights/Dashboards

Eingöngu Azure fyrirtæki, Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana til að vakta gámaþjónustur í Kubernetes í gegnum Prometheus

Monitis fyrir enda-til-enda þjónustuvöktun, aðallega fyrir vef-API og vefforrit

OpsGenie fyrir stýringu viðvarana

Slack til að fá stöðuupplýsingar frá kerfum okkar


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Langtíma (dev)ops verkfræðingur hér. Ólst upp á Nagios. Myndi þiggja skoðanir á SaaS-verkefninu mínu sem ég byggði upp sjálfur https://checklyhq.com. Við gerum API-vöktun og vöktun á færslum á vefsvæðum með frekar ítarlegum viðvörunum.

Ég stofnaði Checkly því virk / gervivöktun á API-sviðinu var dálítið takmörkuð (og dýr). Vafrabyggð / skriftuð vöktun er enn séreignarlegri og dýrari. Við notum Puppeteer og höldum verðlagningu eins lágri og hægt er.

Vöktunarstafli okkar:

Checkly (nota eigin vöru...)

AppOptics (sérsniðin línurit)

AWS Cloudwatch & SNS fyrir SMS-skilaboð.

innbyggðar Heroku-viðvaranir.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana lætur okkur vita í slack um vandamál í innviðum eða afkastaskerðingu, og við höfum stillt logz.io til að senda viðvörun í slack við tiltekið magn villustigs-logga frá forritalaginu.


### SignalFX + Splunk + PagerDuty + Slack

Nota núna: SignalFX, Splunk, PagerDuty og Slack. Ég er ekki mikill aðdáandi SignalFX þótt stuðningsteymi þeirra sé afar vinalegt og fljótt að svara. Mér líkar Splunk (þess virði ef þú getur greitt fyrir það), PagerDuty og Slack.

Ég notaði áður TICK-stafla þar sem mest af C-inu var í raun G, það er Grafana þótt ég hafi notað Chronograf örlítið. Það var frábært en plága að stýra. Hin klassíska SaaS á móti sjálfhýsingu togstreita.

Ég hef notað DataDog, New Relic, Graylog, ELK og BugSnag. Mér líkar DataDog og New Relic mjög vel, Graylog er ansi gott. Ég er ekki mikill ELK aðdáandi. BugSnag er fínt, mér finnst raunar rakning villna/undantekninga vera ansi góður staðgengill fyrir fulla loggavöktun í mörgum tilvikum.


### ELK + Prometheus + Grafana

Eins og aðrir notum við ELK fyrir logga og Prometheus+Grafana fyrir allt annað.

Að viðhalda þessari uppsetningu er auðvelt ef þú gefur þér leyfi til að tapa stundum gögnum. Til dæmis, ef ElasticSearch gagnagrunnurinn okkar fer í lægð (sem gerist því miður á 2-3 mánaða fresti hjá okkur) nennum við ekki að nota HA og hendum í staðinn gögnunum og höldum áfram með lífið. Ef þú verður algerlega að hafa HA eða langtímageymslu, gangi þér vel.


### Datadog + Prometheus + Grafana

Ég setti upp Datadog mánuð í senn því þegar ég kom hingað var engin vöktun og engar viðvaranir. Aðeins nokkur vefsvæði okkar voru vöktuð á 5 mínútna fresti fyrir uppitíma. Datadog er hiklaust auðveldast í uppsetningu. Þegar ég er búinn að taka á öllum hinum vandamálunum mun ég skipta yfir í Prometheus+Grafana. Ekki 100% ákveðinn varðandi loggastýringu enn.

### Nagios + ELK

Við styðjum yfir 100+ vörur.

Á staðnum er það mest Nagios og ELK. Í skýinu erum við að flytja okkur frá DataDog yfir í NewRelic.


### Datadog á móti Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Við notuðum áður datadog en fannst það alltof dýrt fyrir þarfir okkar. Misskildu mig ekki, það er frábært en kostnaðurinn er gríðarlegur. Við gátum sett upp site24x7.com með ársáskrift fyrir um 2-3 mánaða kostnað hjá DD.

Vöktunarstafli okkar:

Site24x7 - APM, vöktun ytri vefslóða, vöktun SMTP-póstflæðis, rennur út SSL-vottorða og ferlavöktun.

StatusCake - fyrir vöktun og staðfestingu vefslóða - Það er varaleið okkar ef site24x7 skyldi missa af einhverju (það gerir það ekki) en SC er sveigjanlegra fyrir vöktun ytri gátta og þjónusta fyrir þarfir okkar.

Bæði verkfæri stigmagna til PagerDuty og svo fáum við stigmagnanir okkar í slack.

SumoLogic - fyrir loggavöktun (það er frábært tól en dálítið flókið fyrir þarfir okkar)

Frá slack getum við staðfest viðvörun eða brugðist við henni.

Við höfum síðan mikið af site24x7-sjálfvirkni sem tengist commando.io fyrir „BedOps“ eins og við köllum það - þar sem viðvörun kviknar ræsum við nokkur skrift eða sjálfvirkni sem tilraun til að bregðast við ástandinu (99% tímans halda sjálfvirknin + skriftin okkur frá vandræðum)

Við höfum innri verkferla (runbooks) í þekkingargrunninum okkar fyrir þegar sjálfvirknin bregst eða ef eitthvað utan umfangsins þarf að laga.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana fyrir mælikvarða í GKE-þyrpingum okkar og sýndarvélum.

Google Stackdriver fyrir logga (því það er innifalið og virkt sjálfgefið og er nú nóg fyrir þarfir okkar).


### Zabbix

Zabbix fyrir allt. Engan viðbótarhugbúnað þarf.
