# Metrikker, overvågning, alarmer

Indhold:

* [Resumé](#resumé)
  * [Problemstilling](#problemstilling)
  * [Beslutning](#beslutning)
  * [Status](#status)
* [Detaljer](#detaljer)
  * [Antagelser](#antagelser)
  * [Begrænsninger](#begrænsninger)
  * [Standpunkter](#standpunkter)
  * [Argument](#argument)
  * [Implikationer](#implikationer)
* [Relateret](#relateret)
  * [Relaterede beslutninger](#relaterede-beslutninger)
  * [Relaterede krav](#relaterede-krav)
  * [Relaterede artefakter](#relaterede-artefakter)
  * [Relaterede principper](#relaterede-principper)
* [Noter](#noter)
  * [Fritekstbeskeder versus strukturerede hændelsesbeskeder](#fritekstbeskeder-versus-strukturerede-hændelsesbeskeder)
  * [Graylog er nemmere](#graylog-er-nemmere)
  * [Prometheus har brug for lidt justering](#prometheus-har-brug-for-lidt-justering)
  * [AWS-tjenester er blandede](#aws-tjenester-er-blandede)
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
  * [Datadog versus Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack](#datadog-versus-site24x7--statuscake--pagerduty--sumologic--slack)
  * [Prometheus + AlertManager + Grafana + Stackdriver](#prometheus--alertmanager--grafana--stackdriver)
  * [Zabbix](#zabbix-1)


## Resumé


### Problemstilling

Vi vil bruge metrikker, overvågning og alarmer, fordi vi vil vide, hvor godt vores applikationer fungerer, og vide, når der er et problem.


### Beslutning

WIP.


### Status

Indsamler oplysninger. Vi starter med de rimelige yderpunkter af spektret: det mest anbefalede ældre gratis værktøj (Nagios) og det mest anbefalede nyere betalte værktøj (New Relic).


## Detaljer


### Antagelser

Vi vil skabe webapps, der er moderne, hurtige, pålidelige, responsive osv.

Vi vil hellere købe end bygge.


### Begrænsninger

Vi vil have værktøjer, der fungerer godt med vores devops-pipeline og med vores deploymentskyer.


### Standpunkter

Vi undersøger i øjeblikket standpunkter.


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

Indtil videre er Nagios og New Relic yderpunkterne af spektret. Nagios er det ældste, enkleste, gratis, brugbare værktøj. New Relic er værktøjet med de nyeste funktioner, det mest komplette, betalte, brugbare værktøj. Vi starter med evalueringer af disse. Efter behov bevæger vi os ind i spektret.  

Indtil videre har Zabbix de bedste anbefalinger og tilbyder også de mest komplette funktioner.

Indtil videre har ELK den bedste popularitet blandt open source, byg-selv-frem-for-køb.

Indtil videre har Prometheus + Graphana den bedste popularitet.


### Implikationer

TODO.


## Relateret


### Relaterede beslutninger

Valgene vil påvirke testbarhed, telemetri og sandsynligvis andre systemer, for eksempel til kundeservice, site reliability engineering osv.


### Relaterede krav

TODO.


### Relaterede artefakter

TODO.


### Relaterede principper

Let at gøre om.

Behov for hastighed.


## Noter


En ret god open source-stak er:

* Prometheus til metrikker og metrikbaserede alarmer

* Grafana til at vise metrikker

* Elasticsearch/Logstash/Kibana (ELK) til logs og strukturerede hændelser

* Pushover til mobilnotifikationer


### Fritekstbeskeder versus strukturerede hændelsesbeskeder

Fritekstbeskeder: for eksempel den slags tilfældige ting, du finder i /var/log/messages, og noget, der bevidst genereres af applikationen. Beskederne er nyttige til at identificere andre ting, der sker på maskinen, såsom hukommelsesmangel eller hardwarefejl, men indeholder meget skrald. 

Strukturerede hændelsesbeskeder: genereret af applikationen med et fast eller dynamisk sæt attributter, f.eks. en HTTP-forespørgselslog, en regnskabslog, et brugerlogin.

Generelt er det rart at logge detaljer om hver forespørgsel på en måde, der lader dig bore ned ud fra attributter. Så at tilføje f.eks. et userid eller sessionid til alt lader dig spore. Eksplicit sporing er selvfølgelig også godt. At bruge ELK til dette er en slags fattigmands https://www.honeycomb.io/


### Graylog er nemmere

Graylog er efter min erfaring nemmere at sætte op.



### Prometheus har brug for lidt justering


Jeg er generelt tilfreds med Prometheus til metrikker. Alarmering har brug for lidt justering, men er ret god. Det afhænger af din applikation. Jeg tror, det er bedst at alarmere på tilstande, der er synlige for slutbrugere, ikke underliggende årsager. For eksempel er sideindlæsningstid godt, antal forespørgsler pr. sekund er det ikke. Selv om nul forespørgsler pr. sekund indikerer, at der er noget galt.

Fordelen ved en tjeneste er, at de tilbyder yderligere intelligens fra start. Jeg kan generelt godt lide Datadog. Tjenesterne kan være skræmmende dyre, hvis du har mange data, og har nogle gange prismodeller, der ikke er cloudvenlige, f.eks. at opkræve pr. instans, når instanser er dynamiske. Der er også forskel på tjenester, hvor hver forespørgsel kommer fra en betalende bruger, og dem, der er reklamerelaterede, så kun en lille procentdel af forespørgslerne giver dig penge. Du kan ende med mange data og ikke så meget budget.

Jeg arbejder på nogle tjenester, der får 1 milliard forespørgsler om dagen, så det er rimeligt at hoste vores egen overvågning og logning. Hvis dine volumener er lavere, er hostede tjenester nemmere.


### AWS-tjenester er blandede

Min erfaring med AWS-tjenester har været blandet. Deres Elasticsearch-tjeneste har været ustabil, så vi kører vores egne instanser til det. CloudWatch-metrikker er dyre, så vi bruger dem generelt kun til metrikker på "infrastrukturniveau" frem for til applikationen, dvs. sundhedsrelaterede metrikker, hvor AWS kan vide bedre, hvad der sker, end softwaren, der kører på instansen. CloudWatch Logs kan være langsomme at opdatere og har ikke så mange metadata. At køre ELK hjælper med det. Hvis jeg virkelig vil have realtidsdata, er det bedre at bruge Kafka som transport til logs. Det understøttes ret godt af Logstash. Det er dog ikke for sarte sjæle at administrere en Kafka-klynge, der er meget bart blikkenslagerarbejde.


### Kafka

Kommentar: Kafka kan være superhårdt nogle gange, eller Kafka kan være så stenhårdt stabilt, at du næsten glemmer, at det er der og binder det hele sammen. 


Kommentar: Kafka har været stabilt, men det var overraskende meget arbejde at få det i gang. Jeg tænker på det som en relationsdatabase, men du arbejder kun på det "fysiske" lag, f.eks. tabelrum, filer og partitioner. Der var tidlige tidspunkter, hvor administrationsværktøjer manglede, og vi var nødt til at skrive programmer til f.eks. at nulstille en forbrugergruppe. http://howfuckedismydatabase.com/nosql/

Kommentar: Vi bruger Kafka som en "buffer" til logbeskeder og et sted, hvor vi kan lave realtidsstrømbehandling på data, der kommer fra flere servere. Hvis vi får et DDOS-angreb, har vi brug for en måde at analysere data på tværs af flere instanser. Hvis vi logger direkte fra serverne til ELK, kan belastningen sprænge Elasticsearch-klyngen.

Kommentar: Kafka er godt for os, fordi hvis vi får et DDOS-angreb, har vi brug for en måde at analysere data på tværs af flere instanser. Hvis vi logger direkte fra serverne til ELK, kan belastningen sprænge Elasticsearch-klyngen.


Kommentar: Kafka udfører mindre arbejde og er mere effektivt, så det kan håndtere belastningen bedre. Og vi sætter Kafka-arbejdet i kø og forsøger igen. Og at Kafka er overbelastet påvirker ikke brugere, der forsøger at lave interaktivt arbejde med Kibana, som det ville, hvis Elasticsearch har det svært.

Kommentar:  Strømbehandling leder mest efter misbrug, f.eks. for meget trafik fra en enkelt IP på tværs af klyngen, og deler så blokeringen på tværs af klyngen.

Kommentar: Pluginet logstash-output-kafka er dog ret upålideligt lige nu. Jeg har været ramt af flere af problemerne på dets GitHub-issuesside, som aldrig ser ud til at blive rettet. Jeg vil væk fra at bruge det og over til at sende direkte fra vores apps til Kafka.

Kommentar: Vi sender nu strukturerede hændelser direkte fra appen til Kafka. Den primære motivation var at røre logdataene færre gange og undgå at læse og skrive disken flere gange. I systemer med høj volumen kan logning tage mere arbejde end selve appen. Jeg overvejer også at få journald til at sende logs direkte fra et C-program.


### Loki

Hold øje med Loki. Det er ikke klar endnu, men når det er, forventer jeg, at det passer bedre i denne stak. Loki er en logaggregator lavet af grafana labs, der bruger lignende scraping- og tagsyntaks som Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager til metrikker. Elsker Prometheus.

Rollbar/Graylog til logning/fejlrapportering (der er nogen overlapning her; en lille tjeneste har sandsynligvis ikke brug for begge).

I øjeblikket går alarmer kun til en af nogle få Slack-kanaler, som interesserede parter har aktiveret notifikationer for. Hvis vi var mere seriøse omkring vagtdienst, ville de gå til PagerDuty/VictorOps/osv.

Grafana til grafer og dashboards. Ser også frem til at se, om deres kommende logningsfunktioner vil gøre Graylog overflødigt.


### Thanos

Vi bruger Thanos som frontend til vores HA-opsætning. Det ved, hvordan man fjerner dubletter fra HA-par.

Vi beholder i øjeblikket 6 måneders lokale Prometheus-data. Det fungerer ret godt for os. Men jeg er midt i at udrulle bucket-lagring til vores Thanos-opsætning til langsigtet datalagring. I teorien vil GCS-lagring være omkring 30 % billigere end den GCE-standardpersistente disk, vi bruger lige nu.

Vi tager ikke sikkerhedskopier af Prometheus-data lige nu. Dataene er simpelthen ikke særlig vigtige for os ud over at have nok til alarmer. Vores samlede flådedeployment ændrer sig så meget fra år til år, at historiske data ældre end et par måneder simpelthen ikke er så interessante. Det kan være interessant at have nogle kernestatistikker år for år; måske sætter jeg et sæt optagelsesregler op for kernestatistikker og gemmer dem med Federation eller lader bare Thanos håndtere det.

EDIT: En lille præcisering, jeg er Prometheus-udvikler.


### Prometheus HA

HA i Prometheus gøres ved duplikering: du kører flere indsamlere, og der er måder at forespørge flere og fjerne dubletter af dataene.

Skalering sker ved at bestemme netværk og lade forskellige Prometheus-instanser forespørge forskellige dele af netværket.

Langtidslagring er ikke Prometheus' styrke, men outsources til noget som influx eller timescaledb (som teknisk set også afkrydser HA). En artikel, jeg har læst om det https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Har ikke prøvet langtidsdelen endnu, fordi jeg stadig kun eksperimenterer og bruger det til kortsigtede grafer, mens librenms overvåger mit netværk på lang sigt


###  Datadog + PagerDuty + Threat Stack

Vi bruger Datadog (med PagerDuty) og Threat Stack og kunne ikke være gladere. Min eneste klage over DD er de relativt høje omkostninger ved lagring af metrikker.


### Zabbix

Zabbix med brugerdefinerede scripts til at overvåge næsten alt. Fungerer som en drøm.


### Outlyer

Jeg bruger Outlyer, men jeg skal præcisere, at jeg arbejder her, og at det at spise sin egen hundemad (dogfooding) er et must.

Har stadig brug for Graylog, Sentry og Statuscake for at forbedre.

Det lyder partisk, men efter med glæde at have kørt Nagios og andre overvågningssystemer internt ville jeg købe en hostet løsning på hvert nyt job og outsource den smerte.


### Nagios + Nagiosgraph

Vi kører Nagios til al overvågning og alarmering. Alarmering sker via e-mail (advarsler og kritiske notifikationer) og hørbare appnotifikationer (til kritiske alarmer).

Nagiosgraph bruges til visualiseringer.

Denne opsætning har været meget effektiv til at holde os omfattende informeret om, hvad der sker i vores miljø. Vi kører og overvåger omkring 110 forretningskritiske servere og omkring 760 datapunkter og har haft dette morgensystem på plads i over syv år.

Jeg vil også gerne på et tidspunkt aggregere logs med Graylog eller ELk.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager via det fantastiske helm-chart Prometheus Operator. Logs går stadig til LogDNA birch-planen, fordi vi opdagede, at ELK er for tungt til vores beskedne klynge med min 3 max 5 noder på GKE.


### DataDog + Sentry + PagerDuty.

Jeg plejede at køre alle mine egne overvågningsløsninger med alle mulige slags software, herunder Nagios, Icinga, Zabbix, ELK, Greylog2, Influx og mange andre værktøjer, men sandheden er, at det er alt for meget arbejde at køre sin egen overvågningsinfrastruktur, især når du kan betale en anden så lave priser for at gøre det for dig!

At betale andre for at køre overvågningsinfrastrukturen frigør mine kunder til at fokusere på at køre deres platforme frem for at overvåge overvågningen, hvilket betyder, at den værdi, de får ud af deres platforms stabilitet, langt overstiger enhver omkostning ved overvågning som en tjeneste.


### Sensu + Graphite + ELK

Min virksomhed er meget for selvhostede ting.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager til alarmering, mit team mener, at enkel overvågning er god overvågning.

Andre systemer som logning og sporing giver rig kontekst til diagnose, når vagthavende får en alarm, men vi bygger aldrig alarmering på dem.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Tjenester instrumenteret med Prometheus => Circonus-analyse og -visualisering


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Vi bruger følgende tjenester:

icinga2 til overvågning og VictorOps til alarmering

NewRelic til detaljeret overvågning af tjenesten

Sentry til fejlsporing i tjenesten

Slack/e-mail er en del af alarmeringen, der udløses fra NewRelic eller icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 med elasticsearch-integration til analyse og graphite+grafana-integration til grafer.

takket være fleksibiliteten i apply-regler i icinga2 kan udviklerne kun se services, de får notifikationer for.

og via icinga2 director kan programmører nemt definere deres egne kontroller (hvilket de gør, med få dages mellemrum – 100 kontroller går ud, 100 andre kontroller kommer ind) i stor skala uden besvær.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Hvad vi har nu:

DataDog til metrikker

New Relic til applikationsovervågning

ELK (Elastic Search + Logstash + Kibana) til logs

Sentry (selvhostet) til logning af undtagelser

E-mail + Slack + VictorOps til alarmering (baseret på alvorlighed)

Hvad vi vil have:

Prometheus til metrikker (Grafana til visualisering)

New Relic (sandsynligvis Elastic Search APM) til applikationsovervågningen

EFK (elastic search + fluentd + kibana) til logning. Sandsynligvis er Loki fra Grafana produktionsklar, når vi når dertil

Sentry til undtagelserne

Alertmanager + e-mail + VictorOps til alarmerne


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (præcisering: arbejder hos VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf til servermetrikker som CPU, disk, hukommelse og netværk. Vi bruger også Telegraf til SNMP-overvågning af vores netværksenheder.

Prometheus til applikationsmetrikker. Vi koder sundhedstjek i vores applikation, som Prometheus scraper.

InfluxDB til tidsserielagring. Hertil sendes vores Telegraf-data.

Grafana til dashboards og alarmer. Alarmmotoren er ikke supertålsom, men den gør sit arbejde. Vi sender også alarmer til Slack.

Hvad jeg ikke har lige nu, er en centraliseret logningsløsning. ELK er kraftfuldt, men svært at sætte op og administrere, og jeg kender ikke til nogen gratis alternativer, der er tæt nok på til at kigge på.


### Sematext + Logagent + Experience

Sematext til metrikker, til logs, til spor og snart også til overvågning af rigtige brugere. Enklere/billigere end at bruge N forskellige værktøjer/tjenester, efter min ydmyge mening.

Til logafsendelse brugte vi rsyslog og skiftede så til Logagent.

Til frontend-nedbrudsrapportering bruger vi Sentry, men skifter snart til Experience.

Præcisering: jeg er en Sematextser.


### Azure Monitor/Analytics + OpsGenie

Jeg ville ønske, at Log Analytics havde en bedre grænseflade. Vi bevæger os væk fra splunk, som var meget nemmere at navigere i.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Du vil virkelig ikke køre dit eget notifikationssystem. Du kan erstatte Splunk med ELK, medmindre dit sikkerhedsteam foretrækker Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf som indsamler, Prometheus + Alertmanager til overvågning og alarmering, integreret med slack-kanaler og pagerduty til kritiske alarmer. Grafana til visualisering af værtsmetrikker.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus til metrikker + alarmer

Grafana til Prometheus-dashboards

Cloudwatch overvåger Prometheus-instanser

sentry til sporing af undtagelser

kibana + elasticsearch

graylog

prometheus Push Gateway til batch/cronjobs

SOP https://github.com/rapidloop/sop til at "skubbe/videresende" metrikker fra 1 Prometheus-instans til en anden

klienter bruger enten Prometheus-klienterne. Vi forsøger at bruge opencensus.io på klientsiden


### PagerDuty + Monitis

PagerDuty + Monitis. Også nogle skræddersyede Azure Functions til at teste sundheden af visse tjenester.

Håber at kunne indføre Prometheus og Grafana i år


### Prometheus + Grafana + Bosun

Prometheus til at gemme tidsseriedataene. Grafana til visualisering. Bosun til alarmhåndtering.


### Azure Monitor/Analytics/Insights/Dashboards

Kun Azure: Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana til at overvåge containertjenester i Kubernetes via Prometheus

Monitis til end-to-end-overvågning af tjenester, primært til web-API'er og webapplikationer

OpsGenie til alarmhåndtering

Slack til at modtage statusoplysninger fra vores systemer


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Mangeårig (dev)ops-ingeniør her. Voksede op med Nagios. Vil meget gerne have meninger om min selvfinansierede SaaS https://checklyhq.com. Vi laver API-overvågning og overvågning af websitetransaktioner med ret dybdegående alarmering.

Jeg startede Checkly, fordi aktiv / syntetisk overvågning i API-området var lidt begrænset (og dyr). Browserbaseret / scriptet overvågning er endnu mere proprietær og dyr. Vi bruger Puppeteer og holder priserne så lave som muligt.

Vores overvågningsstak:

Checkly (dogfooding...)

AppOptics (brugerdefinerede grafer)

AWS Cloudwatch & SNS til sms-beskeder.

indbygget Heroku-alarmering.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana alarmerer os i slack om infrastrukturproblemer eller ydeevneforringelse, og vi har konfigureret logz.io til at alarmere i slack ved en vis volumen af fejlniveaulogs fra applikationslaget.


### SignalFX + Splunk + PagerDuty + Slack

Bruger i øjeblikket: SignalFX, Splunk, PagerDuty og Slack. Jeg er ikke en stor fan af SignalFX, selv om deres supportteam er supervenligt og responsivt. Jeg kan lide Splunk (det værd, hvis du har råd til det), PagerDuty og Slack.

Jeg plejede at bruge TICK-stakken, hvor det meste af C'et faktisk var G, dvs. Grafana, selv om jeg også brugte Chronograf lidt. Det var fantastisk, men en plage at administrere. Det klassiske dilemmaspørgsmål SaaS versus selvhosting.

Jeg har brugt DataDog, New Relic, Graylog, ELK og BugSnag. Jeg kan rigtig godt lide DataDog og New Relic, Graylog er ret godt. Jeg er ikke nogen stor ELK-fan. BugSnag er rart, jeg føler faktisk, at sporing af fejl/undtagelser i mange tilfælde er en ret god erstatning for fuld logovervågning.


### ELK + Prometheus + Grafana

Ligesom andre bruger vi ELK til logs og Prometheus+Grafana til alt andet.

At vedligeholde denne opsætning er nemt, hvis du tillader dig selv at miste data en gang imellem. Hvis for eksempel vores ElasticSearch-database havner i en dyk (hvilket desværre sker for os hver 2.–3. måned), er vi ligeglade med HA, men smider i stedet dataene ud og går videre med vores liv. Hvis du absolut skal have HA eller langtidslagring, held og lykke.


### Datadog + Prometheus + Grafana

Jeg satte Datadog op på månedsbasis, fordi der, da jeg kom hertil, ikke var nogen overvågning og ingen alarmering. Kun et par af vores websteder blev overvåget hvert 5. minut for oppetid. Datadog er uden tvivl nemmest at sætte op. Når jeg er færdig med at tage fat på alle de andre problemer, skifter jeg til Prometheus+Grafana. Ikke 100 % afklaret om loghåndtering endnu.

### Nagios + ELK

Vi understøtter over 100+ produkter.

Til on-prem er det mest Nagios og ELK. Til skyen migrerer vi fra DataDog til NewRelic.


### Datadog versus Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Vi plejede at bruge datadog, men fandt det alt for dyrt til vores behov. Misforstå mig ikke, det er fantastisk, men det har en enorm omkostning. Vi kunne sætte site24x7.com op med et årsabonnement for omkring 2–3 måneders omkostninger fra DD.

Vores overvågningsstak:

Site24x7 - APM, overvågning af eksterne URL'er, overvågning af SMTP-mailflow, ssl-udløbsdato og procesovervågning.

StatusCake - til URL-overvågning og bekræftelse - Det er vores reserve, hvis site24x7 overser noget (det gør det ikke), men SC er mere fleksibelt til overvågning af eksterne porte og tjenester til vores behov.

Begge værktøjer eskalerer til PagerDuty, og så modtager vi vores eskaleringer i slack.

SumoLogic - til logovervågning (det er et fantastisk værktøj, men lidt kompliceret til vores behov)

Fra slack kan vi kvittere for eller løse alarmen.

Så har vi mange site24x7-automatiseringer, der forbinder til commando.io til det, vi kalder 'BedOps' - hvor en alarm udløses, starter vi nogle scripts eller automatiseringer i et forsøg på at afhjælpe situationen (99 % af tiden holder automatiseringen + vores scripts os ude af problemer).

Vi har interne runbooks i vores KB til, når automatiseringerne fejler, eller hvis der er noget uden for omfanget, der skal løses.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana til metrikker i vores GKE-klynger og VM'er.

Google Stackdriver til logs (fordi det er inkluderet og aktivt som standard og i øjeblikket er tilstrækkeligt til vores behov).


### Zabbix

Zabbix til alt. Ingen yderligere software nødvendig.
