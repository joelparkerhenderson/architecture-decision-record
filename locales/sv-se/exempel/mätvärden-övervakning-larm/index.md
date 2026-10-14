# Mätvärden, övervakning, larm

Innehåll:

* [Sammanfattning](#sammanfattning)
  * [Problem](#problem)
  * [Beslut](#beslut)
  * [Status](#status)
* [Detaljer](#detaljer)
  * [Antaganden](#antaganden)
  * [Begränsningar](#begränsningar)
  * [Ståndpunkter](#ståndpunkter)
  * [Argument](#argument)
  * [Implikationer](#implikationer)
* [Relaterat](#relaterat)
  * [Relaterade beslut](#relaterade-beslut)
  * [Relaterade krav](#relaterade-krav)
  * [Relaterade artefakter](#relaterade-artefakter)
  * [Relaterade principer](#relaterade-principer)
* [Anteckningar](#anteckningar)
  * [Meddelanden i fri text kontra strukturerade händelsemeddelanden](#meddelanden-i-fri-text-kontra-strukturerade-händelsemeddelanden)
  * [Graylog är enklare](#graylog-är-enklare)
  * [Prometheus behöver en del justering](#prometheus-behöver-en-del-justering)
  * [AWS-tjänster är blandade](#aws-tjänster-är-blandade)
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
  * [Datadog kontra Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack](#datadog-kontra-site24x7--statuscake--pagerduty--sumologic--slack)
  * [Prometheus + AlertManager + Grafana + Stackdriver](#prometheus--alertmanager--grafana--stackdriver)
  * [Zabbix](#zabbix-1)


## Sammanfattning


### Problem

Vi vill använda mätvärden, övervakning och larm, eftersom vi vill veta hur väl våra applikationer fungerar och veta när det finns ett problem.


### Beslut

WIP.


### Status

Samlar information. Vi börjar med de rimliga ytterligheterna av spektrumet: det mest rekommenderade äldre gratisverktyget (Nagios) och det mest rekommenderade nyare betalverktyget (New Relic).


## Detaljer


### Antaganden

Vi vill skapa webbappar som är moderna, snabba, pålitliga, responsiva osv.

Vi vill köpa i stället för att bygga.


### Begränsningar

Vi vill ha verktyg som fungerar bra med vår devops-pipeline och med våra driftsättningsmoln.


### Ståndpunkter

Vi undersöker ståndpunkter just nu.


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

Hittills är Nagios och New Relic ytterligheterna av spektrumet. Nagios är det äldsta, enklaste, gratis, gångbara verktyget. New Relic är verktyget med de nyaste funktionerna, det mest kompletta, betalda, gångbara verktyget. Vi börjar med utvärderingar av dessa. Efter behov rör vi oss in i spektrumet.  

Hittills har Zabbix de bästa rekommendationerna och erbjuder också de mest kompletta förmågorna.

Hittills har ELK den bästa populariteten bland öppen källkod, bygg-själv-framför-köp.

Hittills har Prometheus + Graphana den bästa populariteten.


### Implikationer

TODO.


## Relaterat


### Relaterade beslut

Valen kommer att påverka testbarhet, telemetri och sannolikt andra system, till exempel för kundtjänst, tillförlitlighetsteknik för webbplatser osv.


### Relaterade krav

TODO.


### Relaterade artefakter

TODO.


### Relaterade principer

Lätt att ångra.

Behov av snabbhet.


## Anteckningar


En ganska bra stack med öppen källkod är:

* Prometheus för mätvärden och larm baserade på mätvärden

* Grafana för att visa mätvärden

* Elasticsearch/Logstash/Kibana (ELK) för loggar och strukturerade händelser

* Pushover för mobilnotiser


### Meddelanden i fri text kontra strukturerade händelsemeddelanden

Meddelanden i fri text: till exempel den sorts slumpmässiga saker du hittar i /var/log/messages, och något som genereras avsiktligt av applikationen. Meddelandena är användbara för att identifiera andra saker som händer på maskinen som slut på minne eller hårdvarufel, men innehåller mycket skräp. 

Strukturerade händelsemeddelanden: genererade av applikationen, med en fast eller dynamisk uppsättning attribut, t.ex. en HTTP-förfrågningslogg, en bokföringslogg, en användarinloggning.

I allmänhet är det trevligt att logga detaljer om varje förfrågan på ett sätt som låter dig borra ner dig utifrån attribut. Så att lägga till t.ex. ett userid eller sessionid till allt låter dig spåra. Explicit spårning är naturligtvis också bra. Att använda ELK för detta är ett slags fattigmans https://www.honeycomb.io/


### Graylog är enklare

Graylog är enklare att sätta upp enligt min erfarenhet.



### Prometheus behöver en del justering


Jag är i allmänhet nöjd med Prometheus för mätvärden. Larmandet behöver en del justering, men är ganska bra. Det beror på din applikation. Jag tror att det är bäst att larma på tillstånd som syns för slutanvändare, inte underliggande orsaker. Till exempel är sidladdningstid bra, antal förfrågningar per sekund är det inte. Även om noll förfrågningar per sekund indikerar att något är fel.

Fördelen med en tjänst är att de erbjuder ytterligare intelligens direkt ur lådan. Jag gillar i allmänhet Datadog. Tjänsterna kan vara skrämmande dyra om du har mycket data, och har ibland prismodeller som inte är molnvänliga, t.ex. att debitera per instans, när instanser är dynamiska. Det finns också en skillnad mellan tjänster där varje förfrågan kommer från en betalande användare och sådana som är reklamrelaterade, så att bara en liten procentandel av förfrågningarna ger dig pengar. Du kan sluta med mycket data och inte så mycket budget.

Jag arbetar med några tjänster som får 1 miljard förfrågningar per dag, så det är rimligt att hosta vår egen övervakning och loggning. Om dina volymer är lägre är hostade tjänster enklare.


### AWS-tjänster är blandade

Min erfarenhet av AWS-tjänster har varit blandad. Deras Elasticsearch-tjänst har varit ostabil, så vi kör egna instanser för det. CloudWatch-mätvärden är dyra, så vi använder dem i allmänhet bara för mätvärden på ”infrastrukturnivå” snarare än för applikationen, dvs. hälsorelaterade mätvärden där AWS kan veta bättre vad som händer än programvaran som körs på instansen. CloudWatch Logs kan vara långsamma att uppdatera och har inte så mycket metadata. Att köra ELK hjälper med det. Om jag verkligen vill ha realtidsdata är det bättre att använda Kafka som transport för loggar. Det stöds ganska bra av Logstash. Att hantera ett Kafka-kluster är dock inget för svaga hjärtan, det finns mycket blottad rörmokeri.


### Kafka

Kommentar: Kafka kan vara supersvårt ibland, eller så kan Kafka vara stenhårt stabilt så att du nästan glömmer att det finns där och binder ihop allt. 


Kommentar: Kafka har varit stabilt, men det var förvånansvärt mycket arbete att få igång det. Jag tänker på det som en relationsdatabas men du arbetar bara på det ”fysiska” lagret, t.ex. tabellutrymmen, filer och partitioner. Det fanns tillfällen tidigt när hanteringsverktygen saknades, och vi var tvungna att skriva program för att t.ex. återställa en konsumentgrupp. http://howfuckedismydatabase.com/nosql/

Kommentar: Vi använder Kafka som en ”buffert” för loggmeddelanden och en plats där vi kan göra realtidsströmbehandling på data som kommer från flera servrar. Om vi får en DDOS-attack behöver vi ett sätt att analysera data över flera instanser. Om vi loggar direkt från servrarna till ELK kan belastningen spränga Elasticsearch-klustret.

Kommentar: Kafka är bra för oss eftersom om vi får en DDOS-attack behöver vi ett sätt att analysera data över flera instanser. Om vi loggar direkt från servrarna till ELK kan belastningen spränga Elasticsearch-klustret.


Kommentar: Kafka gör mindre arbete och är effektivare, så det kan hantera belastningen bättre. Och vi köar Kafka-arbetet och försöker igen. Och att Kafka är överbelastat påverkar inte användare som försöker göra interaktivt arbete med Kibana, som det skulle göra om Elasticsearch har det jobbigt.

Kommentar:  Strömbehandling letar mest efter missbruk, t.ex. för mycket trafik från en enskild IP över hela klustret, och delar sedan blockeringen över hela klustret.

Kommentar: Pluginet logstash-output-kafka är dock ganska opålitligt just nu. Jag har drabbats av flera av problemen på dess GitHub-ärendesida, som aldrig verkar bli åtgärdade. Jag vill gå bort från att använda det, till att skicka direkt från våra appar till Kafka.

Kommentar: Vi skickar nu strukturerade händelser direkt från appen till Kafka. Den främsta motivationen var att beröra loggdatan färre gånger och undvika att läsa och skriva disken flera gånger. I system med hög volym kan loggning ta mer arbete än själva appen. Jag funderar på att få journald att skicka loggar direkt också, från ett C-program.


### Loki

Håll ett öga på Loki. Det är inte redo än men när det är det förväntar jag mig att det passar bättre i den här stacken. Loki är en logg-aggregator skapad av grafana labs, den använder liknande skrapnings- och taggsyntax som Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager för mätvärden. Älskar Prometheus.

Rollbar/Graylog för loggning/felrapportering (det finns viss överlappning här; en liten tjänst behöver förmodligen inte båda).

För närvarande går larm bara till en av några Slack-kanaler som intresserade parter har aktiverat notiser för. Om vi var mer seriösa med jour skulle de gå till PagerDuty/VictorOps/osv.

Grafana för grafer och instrumentpaneler. Ser också med spänning fram emot att se om deras kommande loggningsfunktioner kommer att göra Graylog överflödigt.


### Thanos

Vi använder Thanos som frontend för vår HA-uppsättning. Det vet hur man avdubblerar HA-par.

Vi behåller för närvarande 6 månader lokal Prometheus-data. Det fungerar hyfsat bra för oss. Men jag är precis mitt i att rulla ut bucket-lagring till vår Thanos-uppsättning för långsiktig datalagring. I teorin kommer GCS-lagring att vara ungefär 30 % billigare än den GCE-standardpersistenta disk vi använder just nu.

Vi säkerhetskopierar inte Prometheus-data just nu. Datan är helt enkelt inte särskilt viktig för oss utöver att ha tillräckligt för larm. Vår övergripande flottedriftsättning förändras så mycket från år till år att historisk data äldre än några månader helt enkelt inte är så intressant. Det kan vara intressant att ha några kärnstatistik år för år, jag kanske sätter upp en uppsättning inspelningsregler för kärnstatistik och lagrar dem med Federation eller bara låter Thanos sköta det.

EDIT: Ett litet förtydligande, jag är Prometheus-utvecklare.


### Prometheus HA

HA i Prometheus görs genom duplicering: du kör flera insamlare, det finns sätt att avfråga flera och avdubblera datan.

Skalningen sker genom att bestämma nätverk och låta olika Prometheus avfråga olika delar av nätverket.

Långtidslagring är inte Prometheus styrka utan avlastas till något som influx eller timescaledb (som tekniskt sett också bockar av HA). En artikel jag läst om det https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Har inte provat långtidsdelen än eftersom jag fortfarande bara experimenterar och använder det för kortsiktiga grafer medan librenms övervakar mitt nätverk på lång sikt


###  Datadog + PagerDuty + Threat Stack

Vi använder Datadog (med PagerDuty) och Threat Stack och kunde inte vara nöjdare. Mitt enda klagomål på DD är den relativt höga kostnaden för lagring av mätvärden.


### Zabbix

Zabbix med anpassade skript för att övervaka nästan allt. Fungerar som en dröm.


### Outlyer

Jag använder Outlyer, men jag måste förtydliga att jag jobbar här, och att äta sin egen hundmat (dogfooding) är ett måste.

Behöver fortfarande Graylog, Sentry och Statuscake för att förbättra.

Låter partiskt, men efter att gärna ha kört Nagios och andra övervakningssystem internt skulle jag köpa en hostad lösning på varje nytt jobb och avlasta den smärtan.


### Nagios + Nagiosgraph

Vi kör Nagios för all övervakning och larmning. Larm sker via e-post (varningar och kritiska notiser) och hörbara appnotiser (för kritiska larm).

Nagiosgraph används för visualiseringar.

Den här uppsättningen har varit mycket effektiv för att hålla oss heltäckande informerade om vad som händer i vår miljö. Vi kör och övervakar cirka 110 verksamhetskritiska servrar och cirka 760 datapunkter, och har haft det här morgonsystemet på plats i över sju år.

Jag skulle också vilja aggregera loggar med Graylog eller ELk någon gång.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager via det fantastiska helm-diagrammet Prometheus Operator. Loggar går fortfarande till LogDNA birch-planen eftersom vi märkte att ELK är för tungt för vårt blygsamma kluster med min 3 max 5 noder på GKE.


### DataDog + Sentry + PagerDuty.

Jag brukade köra alla mina egna övervakningslösningar med alla möjliga slags programvara inklusive Nagios, Icinga, Zabbix, ELK, Greylog2, Influx och många andra verktyg, men sanningen är att det är alldeles för mycket arbete att köra sin egen övervakningsinfrastruktur, särskilt när du kan betala någon annan så låga priser för att göra det åt dig!

Att betala andra för att köra övervakningsinfrastrukturen frigör mina kunder att fokusera på att köra sina plattformar i stället för att övervaka övervakningen, vilket innebär att det värde de får av sin plattforms stabilitet vida överstiger eventuella kostnader för övervakning som en tjänst.


### Sensu + Graphite + ELK

Mitt företag är mycket för egenhostade saker.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager för larmning, mitt team tror att enkel övervakning är bra övervakning.

Andra system som loggning och spårning ger rikt sammanhang för diagnos när jouren får ett larm, men vi bygger aldrig larmning på dem.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Tjänster instrumenterade med Prometheus => Circonus analys och visualisering


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Vi använder följande tjänster:

icinga2 för övervakning och VictorOps för larmning

NewRelic för detaljerad övervakning av tjänsten

Sentry för felspårning i tjänsten

Slack/e-post är en del av larmningen som utlöses från NewRelic eller icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 med elasticsearch-integration för analys och graphite+grafana-integration för grafer.

tack vare flexibiliteten i apply-regler i icinga2 kan utvecklarna bara se tjänster de får notiser för.

och via icinga2 director kan programmerare enkelt definiera sina egna kontroller (vilket de gör, med några dagars mellanrum – 100 kontroller går ut, 100 andra kontroller kommer in) i stor skala utan krångel.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Vad vi har nu:

DataDog för mätvärden

New Relic för applikationsövervakning

ELK (Elastic Search + Logstash + Kibana) för loggarna

Sentry (egenhostat) för att logga undantag

E-post + Slack + VictorOps för larmning (baserat på allvarlighetsgrad)

Vad vi vill ha:

Prometheus för mätvärden (Grafana för visualisering)

New Relic (troligen Elastic Search APM) för applikationsövervakningen

EFK (elastic search + fluentd + kibana) för loggning. Troligen är Loki från Grafana produktionsklart tills vi kommer dit

Sentry för undantagen

Alertmanager + e-post + VictorOps för larmen


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Förtydligande: arbetar på VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf för servermätvärden som CPU, disk, minne och nätverk. Vi använder också Telegraf för SNMP-övervakning av våra nätverksenheter.

Prometheus för applikationsmätvärden. Vi kodar hälsokontroller i vår applikation som Prometheus skrapar.

InfluxDB för tidsserielagring. Hit skickas vår Telegraf-data.

Grafana för instrumentpaneler och larm. Larmmotorn är inte supertålig, men den gör jobbet. Vi skickar också larm till Slack.

Vad jag inte har just nu är en centraliserad loggningslösning. ELK är kraftfullt men svårt att sätta upp och hantera, och jag känner inte till några gratisalternativ som ligger tillräckligt nära för att titta på.


### Sematext + Logagent + Experience

Sematext för mätvärden, för loggar, för spår och snart för övervakning av riktiga användare också. Enklare/billigare än att använda N olika verktyg/tjänster, enligt min ödmjuka åsikt.

För loggskickning brukade vi använda rsyslog och bytte sedan till Logagent.

För frontend-kraschrapportering använder vi Sentry, men kommer snart att byta till Experience.

Förtydligande: Jag är en Sematextare.


### Azure Monitor/Analytics + OpsGenie

Jag önskar att Log Analytics hade ett bättre gränssnitt. Vi går bort från splunk, som var mycket enklare att navigera.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Du vill verkligen inte köra ditt eget notissystem. Du kan ersätta Splunk med ELK om inte ditt säkerhetsteam föredrar Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf som insamlare, Prometheus + Alertmanager för övervakning och larmning, integrerat med slack-kanaler och pagerduty för kritiska larm. Grafana för visualisering av värdmätvärden.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus för mätvärden + larm

Grafana för Prometheus-instrumentpaneler

Cloudwatch övervakar Prometheus-instanser

sentry för undantagsspårning

kibana + elasticsearch

graylog

prometheus Push Gateway för batch/cronjobs

SOP https://github.com/rapidloop/sop för att ”skicka/vidarebefordra” mätvärden från 1 Prometheus-instans till en annan

klienter använder antingen Prometheus-klienterna. Vi försöker använda opencensus.io på klientsidan


### PagerDuty + Monitis

PagerDuty + Monitis. Även några skräddarsydda Azure Functions för att testa hälsan hos vissa tjänster.

Hoppas kunna införa Prometheus och Grafana i år


### Prometheus + Grafana + Bosun

Prometheus för att lagra tidsseriedatan. Grafana för visualisering. Bosun för larmhantering.


### Azure Monitor/Analytics/Insights/Dashboards

Enbart Azure, Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana för att övervaka containertjänster i Kubernetes via Prometheus

Monitis för end-to-end-övervakning av tjänster, främst för webb-API:er och webbapplikationer

OpsGenie för larmhantering

Slack för att få statusinformation från våra system


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Mångårig (dev)ops-ingenjör här. Växte upp med Nagios. Skulle gärna vilja ha åsikter om min egenfinansierade SaaS https://checklyhq.com. Vi gör API-övervakning & övervakning av webbplatstransaktioner med ganska djupgående larmning.

Jag startade Checkly eftersom aktiv / syntetisk övervakning inom API-området var lite begränsad (och dyr). Webbläsarbaserad / skriptad övervakning är ännu mer proprietär och dyr. Vi använder Puppeteer och håller priserna så låga som möjligt.

Vår övervakningsstack:

Checkly (dogfooding...)

AppOptics (anpassade grafer)

AWS Cloudwatch & SNS för SMS-meddelanden.

inbyggd Heroku-larmning.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana larmar oss i slack om infrastrukturproblem eller prestandaförsämring, och vi har konfigurerat logz.io för att larma i slack vid en viss volym felnivåloggar från applikationslagret.


### SignalFX + Splunk + PagerDuty + Slack

Använder just nu: SignalFX, Splunk, PagerDuty och Slack. Jag är inte ett stort fan av SignalFX även om deras supportteam är supervänligt och responsivt. Jag gillar Splunk (värt det om du kan betala för det), PagerDuty och Slack.

Jag brukade använda TICK-stacken där det mesta av C faktiskt var G, dvs. Grafana även om jag använde Chronograf lite. Det var fantastiskt men en plåga att hantera. Den klassiska dilemma-frågan SaaS kontra egenhosting.

Jag har använt DataDog, New Relic, Graylog, ELK och BugSnag. Jag gillar DataDog och New Relic mycket, Graylog är ganska bra. Jag är inte något stort ELK-fan. BugSnag är trevligt, jag känner faktiskt att spårning av fel/undantag i många fall är en ganska bra ersättning för fullständig loggövervakning.


### ELK + Prometheus + Grafana

Precis som andra använder vi ELK för loggar och Prometheus+Grafana för allt annat.

Att underhålla den här uppsättningen är enkelt om du tillåter dig själv att ibland förlora data. Om till exempel vår ElasticSearch-databas hamnar i svacka (vilket tyvärr händer för oss var 2–3:e månad) bryr vi oss inte om HA utan slänger i stället datan och går vidare med våra liv. Om du absolut måste ha HA eller långtidslagring, lycka till.


### Datadog + Prometheus + Grafana

Jag satte upp Datadog på månadsbasis eftersom när jag kom hit fanns det ingen övervakning och ingen larmning. Bara ett par av våra webbplatser övervakades var 5:e minut för drifttid. Datadog är utan tvekan enklast att sätta upp. När jag är klar med att ta itu med alla andra problem byter jag till Prometheus+Grafana. Inte 100 % bestämd om loggshantering än.

### Nagios + ELK

Vi stödjer över 100+ produkter.

För on-prem är det mestadels Nagios och ELK. För molnet migrerar vi från DataDog till NewRelic.


### Datadog kontra Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Vi brukade använda datadog men fann det alldeles för dyrt för våra behov. Missförstå mig inte, det är fantastiskt men det har en enorm kostnad. Vi kunde sätta upp site24x7.com med en årsprenumeration för ungefär 2–3 månaders kostnad från DD.

Vår övervakningsstack:

Site24x7 - APM, övervakning av externa URL:er, övervakning av SMTP-mailflöde, ssl-utgångsdatum och processövervakning.

StatusCake - för URL-övervakning och bekräftelse - Det är vår reserv ifall site24x7 missar något (det gör det inte) men SC är mer flexibelt för övervakning av externa portar och tjänster för våra behov.

Båda verktygen eskalerar till PagerDuty, och sedan får vi våra eskaleringar i slack.

SumoLogic - för loggövervakning (det är ett fantastiskt verktyg men lite komplicerat för våra behov)

Från slack kan vi ack:a eller åtgärda larmet.

Sedan har vi många site24x7-automatiseringar som ansluter till commando.io för det vi kallar ’BedOps’ - där ett larm utlöses startar vi några skript eller automatiseringar som ett försök att åtgärda situationen (99 % av tiden håller automatiseringen + våra skript oss ur knipa).

Vi har interna driftböcker i vår KB för när automatiseringarna misslyckas eller om det är något som ligger utanför omfånget som behöver åtgärdas.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana för mätvärden i våra GKE-kluster och VM:ar.

Google Stackdriver för loggar (eftersom det ingår och är aktivt som standard och för närvarande räcker för våra behov).


### Zabbix

Zabbix för allt. Ingen ytterligare programvara behövs.
