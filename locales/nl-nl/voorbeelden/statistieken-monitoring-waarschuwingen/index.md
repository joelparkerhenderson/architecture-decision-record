# Statistieken, monitoring, waarschuwingen

Inhoud:

* [Samenvatting](#samenvatting)
  * [Kwestie](#kwestie)
  * [Beslissing](#beslissing)
  * [Status](#status)
* [Details](#details)
  * [Aannames](#aannames)
  * [Beperkingen](#beperkingen)
  * [Standpunten](#standpunten)
  * [Argument](#argument)
  * [Implicaties](#implicaties)
* [Gerelateerd](#gerelateerd)
  * [Gerelateerde beslissingen](#gerelateerde-beslissingen)
  * [Gerelateerde eisen](#gerelateerde-eisen)
  * [Gerelateerde artefacten](#gerelateerde-artefacten)
  * [Gerelateerde principes](#gerelateerde-principes)
* [Notities](#notities)
  * [Berichten in vrije tekst versus gestructureerde gebeurtenisberichten](#berichten-in-vrije-tekst-versus-gestructureerde-gebeurtenisberichten)
  * [Graylog is eenvoudiger](#graylog-is-eenvoudiger)
  * [Prometheus heeft wat afstemming nodig](#prometheus-heeft-wat-afstemming-nodig)
  * [AWS-diensten zijn wisselend](#aws-diensten-zijn-wisselend)
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


## Samenvatting


### Kwestie

We willen statistieken, monitoring en waarschuwingen gebruiken, omdat we willen weten hoe goed onze applicaties presteren en willen weten wanneer er een probleem is.


### Beslissing

WIP.


### Status

Informatie verzamelen. We beginnen met de redelijke uitersten van het spectrum: de meest aanbevolen oudere gratis tool (Nagios) en de meest aanbevolen nieuwere betaalde tool (New Relic).


## Details


### Aannames

We willen webapps maken die modern, snel, betrouwbaar, responsief enz. zijn.

We willen kopen in plaats van bouwen.


### Beperkingen

We willen tools die goed werken met onze devops-pijplijn en met onze deploymentclouds.


### Standpunten

We onderzoeken op dit moment standpunten.


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

Tot nu toe zijn Nagios en New Relic de uitersten van het spectrum. Nagios is de oudste, eenvoudigste, gratis, haalbare tool. New Relic is de tool met de nieuwste functies, de meest complete, betaalde, haalbare tool. We beginnen met evaluaties van deze twee. Naar behoefte bewegen we ons het spectrum in.  

Tot nu toe heeft Zabbix de beste aanbevelingen en biedt het ook de meest complete mogelijkheden.

Tot nu toe heeft ELK de beste populariteit onder open-source, zelf bouwen in plaats van kopen.

Tot nu toe heeft Prometheus + Graphana de beste populariteit.


### Implicaties

TODO.


## Gerelateerd


### Gerelateerde beslissingen

De keuzes zullen van invloed zijn op testbaarheid, telemetrie en waarschijnlijk andere systemen, bijvoorbeeld voor klantenservice, site reliability engineering enz.


### Gerelateerde eisen

TODO.


### Gerelateerde artefacten

TODO.


### Gerelateerde principes

Gemakkelijk omkeerbaar.

Behoefte aan snelheid.


## Notities


Een redelijk goede open-sourcestack is:

* Prometheus voor statistieken en op statistieken gebaseerde waarschuwingen

* Grafana om statistieken weer te geven

* Elasticsearch/Logstash/Kibana (ELK) voor logs en gestructureerde gebeurtenissen

* Pushover voor mobiele meldingen


### Berichten in vrije tekst versus gestructureerde gebeurtenisberichten

Berichten in vrije tekst: bijvoorbeeld het soort willekeurige dingen dat je in /var/log/messages vindt, en iets wat door de applicatie opzettelijk wordt gegenereerd. De berichten zijn nuttig om andere dingen te identificeren die op de machine gebeuren, zoals geheugentekort of hardwarefouten, maar bevatten veel rommel. 

Gestructureerde gebeurtenisberichten: gegenereerd door de applicatie, met een vaste of dynamische set attributen, bijv. een HTTP-verzoeklog, een boekhoudlog, een gebruikersaanmelding.

Over het algemeen is het prettig details over elk verzoek te loggen op een manier waarmee je op attributen kunt doorboren. Dus door bijvoorbeeld overal een userid of sessionid aan toe te voegen, kun je traceren. Expliciete tracering is natuurlijk ook goed. ELK hiervoor gebruiken is een soort goedkope variant van https://www.honeycomb.io/


### Graylog is eenvoudiger

Graylog is naar mijn ervaring eenvoudiger op te zetten.



### Prometheus heeft wat afstemming nodig


Ik ben over het algemeen tevreden met Prometheus voor statistieken. Het waarschuwen heeft wat afstemming nodig, maar is vrij goed. Het hangt af van je applicatie. Ik denk dat het het beste is te waarschuwen op voor eindgebruikers zichtbare condities, niet op onderliggende oorzaken. Paginalaadtijd is bijvoorbeeld goed, het aantal verzoeken per seconde niet. Hoewel nul verzoeken per seconde aangeeft dat er iets mis is.

Het voordeel van een dienst is dat die kant-en-klaar extra intelligentie biedt. Ik hou over het algemeen van Datadog. De diensten kunnen beangstigend duur zijn als je veel data hebt, en hebben soms prijsmodellen die niet cloudvriendelijk zijn, bijv. rekenen per instantie, terwijl instanties dynamisch zijn. Er is ook een verschil tussen diensten waarbij elk verzoek van een betalende gebruiker komt en diensten die advertentiegerelateerd zijn, zodat slechts een klein percentage van de verzoeken je geld oplevert. Je kunt eindigen met veel data en niet zoveel budget.

Ik werk aan enkele diensten die 1 miljard verzoeken per dag krijgen, dus het is redelijk om onze eigen monitoring en logging te hosten. Als je volumes lager zijn, zijn gehoste diensten eenvoudiger.


### AWS-diensten zijn wisselend

Mijn ervaring met AWS-diensten is wisselend geweest. Hun Elasticsearch-dienst is onstabiel gebleken, dus we draaien daarvoor onze eigen instanties. CloudWatch-statistieken zijn duur, dus we gebruiken ze over het algemeen alleen voor statistieken op "infrastructuurniveau" in plaats van voor de applicatie, dat wil zeggen gezondheidsgerelateerde statistieken waarbij AWS beter kan weten wat er gebeurt dan de software die op de instantie draait. CloudWatch Logs kunnen traag worden bijgewerkt en hebben niet veel metadata. ELK draaien helpt daarbij. Als ik echt realtimedata wil, is het beter Kafka als transport voor logs te gebruiken. Dat wordt vrij goed ondersteund door Logstash. Een Kafka-cluster beheren is echter niets voor bangeriken, er is veel kaal loodgieterswerk.


### Kafka

Opmerking: Kafka kan soms superlastig zijn, of Kafka kan zo keihard stabiel zijn dat je bijna vergeet dat het er is en alles aan elkaar knoopt. 


Opmerking: Kafka is stabiel geweest, maar het kostte verrassend veel werk om het aan de praat te krijgen. Ik zie het als een relationele database waarvan je alleen op de "fysieke" laag werkt, bijv. tablespaces, bestanden en partities. Er waren vroeger momenten waarop beheertools ontbraken, en we moesten programma's schrijven om bijvoorbeeld een consumentengroep te resetten. http://howfuckedismydatabase.com/nosql/

Opmerking: We gebruiken Kafka als "buffer" voor logberichten en als plek waar we realtime streamverwerking kunnen doen op data die van meerdere servers komt. Als we een DDOS-aanval krijgen, hebben we een manier nodig om data over meerdere instanties te analyseren. Als we rechtstreeks van de servers naar ELK loggen, kan de belasting het Elasticsearch-cluster opblazen.

Opmerking: Kafka is goed voor ons, want als we een DDOS-aanval krijgen, hebben we een manier nodig om data over meerdere instanties te analyseren. Als we rechtstreeks van de servers naar ELK loggen, kan de belasting het Elasticsearch-cluster opblazen.


Opmerking: Kafka doet minder werk en is efficiënter, dus het kan de belasting beter aan. En we zetten het Kafka-werk in de wachtrij en proberen het opnieuw. En dat Kafka overbelast is, raakt geen gebruikers die interactief met Kibana willen werken, zoals wel zou gebeuren als Elasticsearch het moeilijk heeft.

Opmerking:  Streamverwerking zoekt vooral naar misbruik, bijv. te veel verkeer van één IP over het hele cluster, en deelt dan de blokkade over het hele cluster.

Opmerking: De plug-in logstash-output-kafka is op dit moment echter vrij onbetrouwbaar. Ik heb last gehad van meerdere problemen op de GitHub-issuepagina die nooit lijken te worden opgelost. Ik wil er vanaf stappen en rechtstreeks vanuit onze apps naar Kafka sturen.

Opmerking: We sturen nu gestructureerde gebeurtenissen rechtstreeks van de app naar Kafka. De belangrijkste motivatie was de logdata minder vaak aan te raken en te vermijden dat de schijf meerdere keren wordt gelezen en geschreven. In systemen met een hoog volume kan loggen meer werk kosten dan de app zelf. Ik overweeg journald ook logs rechtstreeks te laten verzenden, vanuit een C-programma.


### Loki

Houd Loki in de gaten. Het is nog niet klaar, maar als het dat is, verwacht ik dat het beter in deze stack past. Loki is een logaggregator gemaakt door grafana labs, die een vergelijkbare scrape- en tagsyntaxis gebruikt als Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager voor statistieken. Dol op Prometheus.

Rollbar/Graylog voor logging/foutrapportage (er is hier enige overlap; een kleine dienst heeft waarschijnlijk niet beide nodig).

Op dit moment gaan waarschuwingen alleen naar een van enkele Slack-kanalen waarvoor geïnteresseerden meldingen hebben ingeschakeld. Als we serieuzer waren over storingsdienst, zouden ze naar PagerDuty/VictorOps/enz. gaan.

Grafana voor grafieken en dashboards. Ik kijk ook uit naar of hun aankomende loggingfuncties Graylog overbodig maken.


### Thanos

We gebruiken Thanos als frontend voor onze HA-opstelling. Het weet hoe HA-paren te ontdubbelen.

We bewaren momenteel 6 maanden lokale Prometheus-data. Dat werkt redelijk goed voor ons. Maar ik ben bezig bucketopslag uit te rollen voor onze Thanos-opstelling voor langetermijndataopslag. In theorie is GCS-opslag ongeveer 30% goedkoper dan de standaard persistente GCE-schijf die we nu gebruiken.

We maken op dit moment geen back-ups van Prometheus-data. De data zijn gewoon niet erg belangrijk voor ons, buiten het hebben van genoeg voor waarschuwingen. Onze algehele vlootdeployment verandert zoveel van jaar tot jaar dat historische data ouder dan een paar maanden gewoon niet zo interessant zijn. Het kan interessant zijn om enkele kernstatistieken jaar over jaar te hebben; misschien zet ik een set opnameregels op voor kernstatistieken en sla ze op met Federation of laat Thanos het afhandelen.

EDIT: een kleine verduidelijking, ik ben Prometheus-ontwikkelaar.


### Prometheus HA

HA in Prometheus gebeurt door duplicatie: je draait meerdere verzamelaars, en er zijn manieren om meerdere te bevragen en de data te ontdubbelen.

Schalen gebeurt door netwerken vast te stellen en verschillende Prometheus-instanties verschillende delen van het netwerk te laten bevragen.

Langetermijnopslag is niet de sterkte van Prometheus maar wordt uitbesteed aan iets als influx of timescaledb (dat technisch gezien ook HA afvinkt). Een artikel dat ik erover heb gelezen https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Het langetermijngedeelte nog niet geprobeerd, omdat ik nog steeds alleen experimenteer en het gebruik voor grafieken op korte termijn terwijl librenms mijn netwerk op lange termijn monitort


###  Datadog + PagerDuty + Threat Stack

We gebruiken Datadog (met PagerDuty) en Threat Stack en kunnen niet tevredener zijn. Mijn enige klacht over DD zijn de relatief hoge kosten van de opslag van statistieken.


### Zabbix

Zabbix met aangepaste scripts om bijna alles te monitoren. Werkt als een droom.


### Outlyer

Ik gebruik Outlyer, maar ik moet verduidelijken dat ik hier werk en dat het eten van je eigen hondenvoer (dogfooding) een must is.

Heb nog steeds Graylog, Sentry en Statuscake nodig om te verbeteren.

Klinkt bevooroordeeld, maar na met plezier intern Nagios en andere monitoringsystemen te hebben gedraaid, zou ik bij elke nieuwe baan een gehoste oplossing kopen en die pijn uitbesteden.


### Nagios + Nagiosgraph

We draaien Nagios voor alle monitoring en waarschuwingen. Waarschuwingen gaan via e-mail (waarschuwingen en kritieke meldingen) en hoorbare appmeldingen (voor kritieke waarschuwingen).

Nagiosgraph wordt gebruikt voor visualisaties.

Deze opstelling is zeer effectief geweest om ons uitgebreid op de hoogte te houden van wat er in onze omgeving gebeurt. We draaien en monitoren ongeveer 110 bedrijfskritieke servers en ongeveer 760 datapunten, en hebben dit ochtendsysteem al meer dan zeven jaar.

Ik zou ook ooit graag logs willen aggregeren met Graylog of ELk.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager via de geweldige helm-chart Prometheus Operator. Logs gaan nog steeds naar het LogDNA birch-abonnement omdat we merkten dat ELK te zwaar is voor ons bescheiden cluster met min 3 max 5 nodes op GKE.


### DataDog + Sentry + PagerDuty.

Ik draaide vroeger al mijn eigen monitoringoplossingen met allerlei soorten software, waaronder Nagios, Icinga, Zabbix, ELK, Greylog2, Influx en veel andere tools, maar de waarheid is dat het veel te veel werk is om je eigen monitoringinfrastructuur te draaien, vooral als je iemand anders zulke lage prijzen kunt betalen om het voor je te doen!

Anderen betalen om de monitoringinfrastructuur te draaien, laat mijn klanten zich richten op het draaien van hun platforms in plaats van het monitoren van de monitoring, wat betekent dat de waarde die ze halen uit de stabiliteit van hun platform ver uitstijgt boven eventuele kosten van monitoring als dienst.


### Sensu + Graphite + ELK

Mijn bedrijf is erg voor zelfgehoste dingen.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager voor waarschuwingen, mijn team gelooft dat eenvoudige monitoring goede monitoring is.

Andere systemen zoals logging en tracering geven rijke context voor diagnose wanneer de storingsdienst een waarschuwing krijgt, maar we bouwen waarschuwingen er nooit op.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Services geïnstrumenteerd met Prometheus => Circonus-analyse en -visualisatie


### icinga2 + VictorOps + NewRelic + Sentry + Slack

We gebruiken de volgende diensten:

icinga2 voor monitoring en VictorOps voor waarschuwingen

NewRelic voor gedetailleerde monitoring van de dienst

Sentry voor foutopsporing in de dienst

Slack/e-mail maakt deel uit van de waarschuwingen die worden geactiveerd vanuit NewRelic of icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 met elasticsearch-integratie voor analyse en graphite+grafana-integratie voor grafieken.

dankzij de flexibiliteit van apply-regels in icinga2 kunnen de ontwikkelaars alleen services zien waarvoor ze meldingen krijgen.

en via icinga2 director kunnen programmeurs zonder gedoe op grote schaal gemakkelijk hun eigen controles definiëren (wat ze doen, om de paar dagen – 100 controles gaan eruit, 100 andere controles komen erin).


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Wat we nu hebben:

DataDog voor statistieken

New Relic voor applicatiemonitoring

ELK (Elastic Search + Logstash + Kibana) voor de logs

Sentry (zelfgehost) voor het loggen van uitzonderingen

E-mail + Slack + VictorOps voor waarschuwingen (op basis van ernst)

Wat we willen:

Prometheus voor statistieken (Grafana voor visualisatie)

New Relic (waarschijnlijk Elastic Search APM) voor de applicatiemonitoring

EFK (elastic search + fluentd + kibana) voor logging. Waarschijnlijk is Loki van Grafana productieklaar tegen de tijd dat we daar zijn

Sentry voor de uitzonderingen

Alertmanager + e-mail + VictorOps voor de waarschuwingen


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (verduidelijking: werkt bij VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf voor serverstatistieken zoals CPU, schijf, geheugen en netwerk. We gebruiken Telegraf ook voor SNMP-monitoring van onze netwerkapparaten.

Prometheus voor applicatiestatistieken. We coderen gezondheidscontroles in onze applicatie die Prometheus scrapet.

InfluxDB voor tijdreeksopslag. Hierheen gaan onze Telegraf-data.

Grafana voor dashboards en waarschuwingen. De waarschuwingsengine is niet superrobuust, maar doet zijn werk. We sturen waarschuwingen ook naar Slack.

Wat ik op dit moment niet heb, is een gecentraliseerde loggingoplossing. ELK is krachtig maar moeilijk op te zetten en te beheren, en ik ken geen gratis alternatieven die dichtbij genoeg komen om naar te kijken.


### Sematext + Logagent + Experience

Sematext voor statistieken, voor logs, voor traces en binnenkort ook voor monitoring van echte gebruikers. Eenvoudiger/goedkoper dan N verschillende tools/diensten gebruiken, naar mijn bescheiden mening.

Voor het verzenden van logs gebruikten we rsyslog en stapten toen over op Logagent.

Voor frontend-crashrapportage gebruiken we Sentry, maar we stappen binnenkort over op Experience.

Verduidelijking: ik ben een Sematextser.


### Azure Monitor/Analytics + OpsGenie

Ik wou dat Log Analytics een betere interface had. We stappen over van splunk, dat veel gemakkelijker te navigeren was.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Je wilt echt geen eigen meldingssysteem draaien. Je kunt Splunk vervangen door ELK, tenzij je beveiligingsteam Splunk verkiest.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf als verzamelaar, Prometheus + Alertmanager voor monitoring en waarschuwingen, geïntegreerd met slack-kanalen en pagerduty voor kritieke waarschuwingen. Grafana voor visualisatie van hoststatistieken.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus voor statistieken + waarschuwingen

Grafana voor Prometheus-dashboards

Cloudwatch monitort Prometheus-instanties

sentry voor opsporing van uitzonderingen

kibana + elasticsearch

graylog

prometheus Push Gateway voor batch/cronjobs

SOP https://github.com/rapidloop/sop om statistieken van 1 Prometheus-instantie naar een andere te "pushen/doorsturen"

clients gebruiken ofwel de Prometheus-clients. We proberen opencensus.io aan de clientzijde te gebruiken


### PagerDuty + Monitis

PagerDuty + Monitis. Ook enkele op maat gemaakte Azure Functions om de gezondheid van bepaalde diensten te testen.

Hoop dit jaar Prometheus en Grafana te kunnen invoeren


### Prometheus + Grafana + Bosun

Prometheus om de tijdreeksdata op te slaan. Grafana voor visualisatie. Bosun voor waarschuwingsbeheer.


### Azure Monitor/Analytics/Insights/Dashboards

Alleen Azure: Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana om containerdiensten in Kubernetes te monitoren via Prometheus

Monitis voor end-to-end-monitoring van diensten, vooral voor web-API's en webapplicaties

OpsGenie voor waarschuwingsbeheer

Slack om statusinformatie van onze systemen te ontvangen


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Mijn eigen (dev)ops-ingenieur met jarenlange ervaring. Opgegroeid met Nagios. Ik hoor graag meningen over mijn zelf gefinancierde SaaS https://checklyhq.com. We doen API-monitoring en monitoring van websitetransacties met vrij diepgaande waarschuwingen.

Ik startte Checkly omdat actieve / synthetische monitoring in de API-ruimte nogal beperkt (en duur) was. Browsergebaseerde / gescripte monitoring is nog propriëtairder en duurder. We gebruiken Puppeteer en houden de prijzen zo laag mogelijk.

Onze monitoringstack:

Checkly (dogfooding...)

AppOptics (aangepaste grafieken)

AWS Cloudwatch & SNS voor sms-berichten.

ingebouwde Heroku-waarschuwingen.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana waarschuwt ons in slack bij infrastructuurproblemen of prestatievermindering, en we hebben logz.io zo geconfigureerd dat het in slack waarschuwt bij een bepaald volume aan foutniveau-logs uit de applicatielaag.


### SignalFX + Splunk + PagerDuty + Slack

Gebruik momenteel: SignalFX, Splunk, PagerDuty en Slack. Ik ben geen grote fan van SignalFX, ook al is hun supportteam supervriendelijk en responsief. Ik hou van Splunk (de moeite waard als je het kunt betalen), PagerDuty en Slack.

Ik gebruikte vroeger de TICK-stack waarbij het grootste deel van de C eigenlijk G was, dat wil zeggen Grafana, hoewel ik Chronograf ook een beetje gebruikte. Het was fantastisch maar een gedoe om te beheren. De klassieke dilemmavraag SaaS versus zelf hosten.

Ik heb DataDog, New Relic, Graylog, ELK en BugSnag gebruikt. Ik hou erg van DataDog en New Relic, Graylog is redelijk goed. Ik ben geen grote ELK-fan. BugSnag is prettig, ik vind eigenlijk dat het volgen van fouten/uitzonderingen in veel gevallen een redelijk goede vervanging is voor volledige logmonitoring.


### ELK + Prometheus + Grafana

Net als anderen gebruiken we ELK voor logs en Prometheus+Grafana voor al het andere.

Het onderhouden van deze opstelling is eenvoudig als je jezelf toestaat af en toe data te verliezen. Als onze ElasticSearch-database bijvoorbeeld in een dip belandt (wat helaas elke 2–3 maanden gebeurt), maken we ons niet druk om HA maar gooien we de data weg en gaan we verder met ons leven. Als je absoluut HA of langetermijnopslag moet hebben, veel succes.


### Datadog + Prometheus + Grafana

Ik heb Datadog op maandbasis opgezet omdat er, toen ik hier kwam, geen monitoring en geen waarschuwingen waren. Slechts een paar van onze sites werden elke 5 minuten gemonitord op uptime. Datadog is verreweg het gemakkelijkst op te zetten. Als ik klaar ben met alle andere problemen, stap ik over op Prometheus+Grafana. Nog niet 100% zeker over logbeheer.

### Nagios + ELK

We ondersteunen meer dan 100+ producten.

Voor on-prem is het meestal Nagios en ELK. Voor de cloud migreren we van DataDog naar NewRelic.


### Datadog versus Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

We gebruikten vroeger datadog, maar vonden het veel te duur voor onze behoeften. Begrijp me niet verkeerd, het is geweldig maar het heeft enorme kosten. We konden site24x7.com opzetten met een jaarabonnement voor ongeveer 2–3 maanden aan kosten van DD.

Onze monitoringstack:

Site24x7 - APM, monitoring van externe URL's, monitoring van SMTP-mailstroom, ssl-vervaldatum en procesmonitoring.

StatusCake - voor URL-monitoring en bevestiging - Het is onze back-up voor het geval site24x7 iets mist (dat doet het niet), maar SC is flexibeler voor het monitoren van externe poorten en diensten voor onze behoeften.

Beide tools escaleren naar PagerDuty, en dan ontvangen we onze escalaties in slack.

SumoLogic - voor logmonitoring (het is een geweldige tool maar een beetje ingewikkeld voor onze behoeften)

Vanuit slack kunnen we de waarschuwing bevestigen (ack) of oplossen.

Dan hebben we veel site24x7-automatiseringen die verbinden met commando.io voor wat we 'BedOps' noemen - waar een waarschuwing wordt geactiveerd, starten we enkele scripts of automatiseringen in een poging de situatie op te lossen (99% van de tijd houden de automatisering + onze scripts ons uit de problemen).

We hebben interne runbooks in onze KB voor wanneer de automatiseringen falen of als er iets buiten de reikwijdte valt dat moet worden opgelost.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana voor statistieken in onze GKE-clusters en VM's.

Google Stackdriver voor logs (omdat het is inbegrepen en standaard actief is en op dit moment voldoende is voor onze behoeften).


### Zabbix

Zabbix voor alles. Geen extra software nodig.
