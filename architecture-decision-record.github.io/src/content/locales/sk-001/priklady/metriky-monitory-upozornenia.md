# Metriky, monitory, upozornenia

Obsah:

* [Zhrnutie](#zhrnutie)
  * [Problém](#problém)
  * [Rozhodnutie](#rozhodnutie)
  * [Stav](#stav)
* [Podrobnosti](#podrobnosti)
  * [Predpoklady](#predpoklady)
  * [Obmedzenia](#obmedzenia)
  * [Pozície](#pozície)
  * [Argument](#argument)
  * [Dôsledky](#dôsledky)
* [Súvisiace](#súvisiace)
  * [Súvisiace rozhodnutia](#súvisiace-rozhodnutia)
  * [Súvisiace požiadavky](#súvisiace-požiadavky)
  * [Súvisiace artefakty](#súvisiace-artefakty)
  * [Súvisiace princípy](#súvisiace-princípy)
* [Poznámky](#poznámky)
  * [Voľné textové správy oproti štruktúrovaným správam udalostí](#voľné-textové-správy-oproti-štruktúrovaným-správam-udalostí)
  * [Graylog je jednoduchší](#graylog-je-jednoduchší)
  * [Prometheus vyžaduje trochu ladenia](#prometheus-vyžaduje-trochu-ladenia)
  * [Služby AWS sú zmiešané](#služby-aws-sú-zmiešané)
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


## Zhrnutie


### Problém

Chceme používať metriky, monitory a upozornenia, pretože chceme vedieť, ako dobre naše aplikácie fungujú, a vedieť, kedy nastane problém.


### Rozhodnutie

Rozpracované (WIP).


### Stav

Zhromažďovanie informácií. Začíname pri pravdepodobných krajoch spektra: najodporúčanejší starší bezplatný nástroj (Nagios) a najodporúčanejší novší platený nástroj (New Relic).


## Podrobnosti


### Predpoklady

Chceme vytvárať webové aplikácie, ktoré sú moderné, rýchle, spoľahlivé, responzívne atď.

Chceme kupovať, nie budovať.


### Obmedzenia

Chceme nástroje, ktoré dobre fungujú s naším devops pipeline a s našimi cloudmi pre nasadenie.


### Pozície

Pozície teraz skúmame.


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

Zatiaľ sú Nagios a New Relic krajmi spektra. Nagios je najstarší, najjednoduchší, bezplatný, schodný nástroj. New Relic je nástroj s najnovšími funkciami, najúplnejší, platený, schodný. Začneme hodnotením týchto dvoch. Podľa potreby sa posunieme do vnútra spektra.  

Zatiaľ má Zabbix najlepšie odporúčania a ponúka tiež najúplnejšie schopnosti.

Zatiaľ má ELK najlepšiu obľubu medzi open source riešeniami uprednostňujúcimi budovanie pred nákupom.

Zatiaľ majú Prometheus + Grafana najlepšiu obľubu.


### Dôsledky

TODO.


## Súvisiace


### Súvisiace rozhodnutia

Voľby ovplyvnia testovateľnosť, telemetriu a pravdepodobne ďalšie systémy, napríklad pre zákaznícky servis, inžinierstvo spoľahlivosti webov (SRE) atď.


### Súvisiace požiadavky

TODO.


### Súvisiace artefakty

TODO.


### Súvisiace princípy

Ľahko vratné.

Potreba rýchlosti.


## Poznámky


Celkom dobrý open source stack je:

* Prometheus pre metriky a upozornenia založené na metrikách

* Grafana na zobrazenie metrík

* Elasticsearch/Logstash/Kibana (ELK) pre logy a štruktúrované udalosti

* Pushover pre mobilné oznámenia


### Voľné textové správy oproti štruktúrovaným správam udalostí

Voľné textové správy: napríklad druh náhodných vecí, ktoré nájdete v /var/log/messages, a niečo, čo aplikácie vytvárajú zámerne. Správy sú užitočné na identifikáciu iných vecí, ktoré sa na stroji dejú, ako nedostatok pamäte alebo hardvérové chyby, ale majú veľa odpadu. 

Štruktúrované správy udalostí: generované aplikáciou, s pevnou alebo dynamickou sadou atribútov, napr. log HTTP požiadaviek, účtovný log, prihlásenie používateľa.

Vo všeobecnosti je dobré logovať podrobnosti o každej požiadavke spôsobom, ktorý umožňuje preniknúť do hĺbky podľa atribútov. Pridanie napr. userid alebo sessionid ku všetkému teda umožňuje sledovanie. Explicitné trasovanie (tracing) je samozrejme tiež dobré. Použitie ELK na to je akási chudobná obdoba https://www.honeycomb.io/


### Graylog je jednoduchší

Graylog je podľa mojej skúsenosti jednoduchšie sprevádzkovať.



### Prometheus vyžaduje trochu ladenia


S Prometheom pre metriky som vo všeobecnosti spokojný. Upozornenia vyžadujú trochu ladenia, ale sú celkom dobré. Závisí od vašej aplikácie. Myslím, že najlepšie je upozorňovať na stavy viditeľné pre koncového používateľa, nie na základné príčiny. Napríklad čas načítania stránky je dobrý, počet požiadaviek za sekundu nie. Hoci nula požiadaviek za sekundu naznačuje, že niečo nie je v poriadku.

Výhodou služby je, že ponúka dodatočnú inteligenciu hneď z krabice. Vo všeobecnosti sa mi páči Datadog. Služby môžu byť desivo drahé, ak máte veľa dát, a niekedy majú cenové modely, ktoré nie sú priateľské k cloudu, napr. účtovanie za inštanciu, keď sú inštancie dynamické. Existuje aj rozdiel medzi službami, kde každá požiadavka pochádza od platiaceho používateľa, a tými súvisiacimi s reklamou, takže len malé percento požiadaviek zarába peniaze. Môžete skončiť s veľa dátami a nie tak veľkým rozpočtom.

Pracujem na niektorých službách, ktoré dostávajú 1 miliardu požiadaviek denne, takže dáva zmysel hostovať si vlastný monitoring a logovanie. Ak sú vaše objemy menšie, hostované služby sú jednoduchšie.


### Služby AWS sú zmiešané

Moja skúsenosť so službami AWS je zmiešaná. Ich služba Elasticsearch bola nespoľahlivá, takže prevádzkujeme vlastné inštancie. Metriky CloudWatch sú drahé, takže ich vo všeobecnosti používame len pre metriky na úrovni „infraštruktúry“, nie aplikácie, teda metriky súvisiace so zdravím, kde AWS môže vedieť lepšie, čo sa deje, než softvér bežiaci na inštancii. Logy CloudWatch môžu byť pomalé pri aktualizácii a nemajú toľko metadát. Prevádzka ELK s tým pomáha. Ak naozaj chcem dáta v reálnom čase, je lepšie použiť Kafku ako transport logov. To je Logstashom celkom dobre podporované. Správa klastra Kafka však nie je pre slabé povahy, je tam veľa odhalených rúr.


### Kafka

Komentár: Kafka môže byť niekedy nesmierne vrtošivá, alebo môže byť skalopevná a takmer zabudnete, že tam je a všetko spája. 


Komentár: Kafka bola solídna, ale sprevádzkovanie bolo prekvapivo veľa práce. Predstavujem si ju ako relačnú databázu, ale kde pracujete len na „fyzickej“ vrstve, napr. tabuľkové priestory, súbory a oddiely. Na začiatku boli chvíle, keď chýbali nástroje na správu, a museli sme písať programy, napr. na reset skupiny konzumentov. http://howfuckedismydatabase.com/nosql/

Komentár: Používame Kafku ako „vyrovnávaciu pamäť“ pre logovacie správy a miesto, kde môžeme vykonávať streamové spracovanie v reálnom čase na dátach prichádzajúcich z viacerých serverov. Ak nás zasiahne DDOS útok, potrebujeme spôsob analýzy dát naprieč viacerými inštanciami. Ak logujeme priamo zo serverov do ELK, záťaž môže zhodiť klaster Elasticsearch.

Komentár: Kafka je pre nás dobrá, pretože ak nás zasiahne DDOS útok, potrebujeme spôsob analýzy dát naprieč viacerými inštanciami. Ak logujeme priamo zo serverov do ELK, záťaž môže zhodiť klaster Elasticsearch.


Komentár: Kafka robí menej práce a je efektívnejšia, takže záťaž zvláda lepšie. A prácu Kafky radíme do frontu a opakujeme. A preťaženie Kafky neovplyvní používateľov, ktorí sa snažia interaktívne pracovať s Kibanou, ako by to bolo, keby Elasticsearch zápasil.

Komentár:  Streamové spracovanie väčšinou hľadá zneužitie, napr. príliš veľa prevádzky z jednej IP naprieč celým klastrom, a potom zdieľa blokovanie naprieč celým klastrom.

Komentár: Zásuvný modul logstash-output-kafka je však v tejto chvíli dosť nespoľahlivý. Pohrýzlo ma niekoľko problémov na jeho stránke issues na GitHube, ktoré sa zdajú byť nikdy neopravované. Chcem od jeho používania odísť a posielať priamo z našich aplikácií do Kafky.

Komentár: Teraz posielame štruktúrované udalosti priamo z aplikácie do Kafky. Hlavnou motiváciou bolo dotýkať sa logovacích dát menej často a vyhnúť sa opakovanému čítaniu a zápisu na disk. V systémoch s vysokým objemom môže logovanie vyžadovať viac práce než samotná aplikácia. Uvažujem o tom, že by journald tiež posielal logy priamo, z programu v C.


### Loki

Majte Loki na očiach. Ešte nie je hotové, ale keď bude, očakávam, že bude do tohto stacku lepšie zapadať. Loki je agregátor logov vytvorený Grafana Labs, používa podobnú syntax zberu a štítkov ako Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager pre metriky. <3 Prometheus.

Rollbar/Graylog pre logovanie/hlásenie chýb (je tu určité prekrývanie; malá služba pravdepodobne nepotrebuje oboje).

V súčasnosti upozornenia idú len do jedného z niekoľkých kanálov Slack, kde majú zainteresované strany zapnuté oznámenia. Keby sme pohotovosť (on-call) brali vážnejšie, išli by do PagerDuty/VictorOps atď.

Grafana pre grafy a dashboardy. Tiež sa nedočkavo teším, či ich pripravované možnosti logovania urobia Graylog zbytočným.


### Thanos

Thanos používame ako front-end pre naše HA nastavenie. Vie deduplikovať HA páry.

V súčasnosti uchovávame 6 mesiacov lokálnych dát Prometheus. Pre nás to funguje rozumne dobre. Ale som práve uprostred zavádzania úložiska bucket do nášho nastavenia Thanos pre dlhodobé ukladanie dát. Teoreticky bude úložisko GCS asi o 30 % lacnejšie než štandardný persistentný disk GCE, ktorý teraz používame.

V súčasnosti nezálohujeme dáta Prometheus. Dáta pre nás vlastne nie sú dôležité nad rámec toho, aby sme ich mali dosť na upozornenia. Naše celkové nasadenie flotily sa rok od roka mení tak veľmi, že historické dáta staršie než pár mesiacov nie sú skutočne zaujímavé. Mohlo by byť zaujímavé mať pár základných štatistík medziročne; môžem nastaviť sadu záznamových pravidiel pre základné štatistiky a ukladať ich pomocou Federation alebo jednoducho nechať Thanos, nech sa o to postará.

EDIT: Malé upozornenie, som vývojár Prometheus.


### Prometheus HA

HA v Prometheus sa robí duplikáciou — spúšťate viac zberných inštancií a existujú spôsoby, ako dopytovať viaceré z nich a deduplikovať dáta

Škálovanie sa robí rozdelením siete a tým, že rôzne Prometheusy dopytujú rôzne časti siete

Dlhodobé ukladanie nie je silnou stránkou Prometheus, ale prenáša sa na niečo ako Influx alebo timescaledb (ktorý technicky tiež odškrtne HA) článok, ktorý som o tom čítal https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Dlhodobé veci som zatiaľ nevyskúšal, pretože stále len experimentujem a používam to pre krátkodobé grafy, zatiaľ čo librenms monitoruje moju sieť dlhodobo


###  Datadog + PagerDuty + Threat Stack

Používame Datadog (s PagerDuty) a Threat Stack a nemohli by sme byť spokojnejší. Moja jediná výčitka voči DD sú relatívne vysoké náklady na ukladanie metrík.


### Zabbix

Zabbix s vlastnými skriptmi na monitorovanie takmer čohokoľvek. Funguje skvelo.


### Outlyer

Používam Outlyer, ale musím vyhlásiť, že tam pracujem a používanie vlastného produktu je povinnosť.

Na doplnenie stále potrebujem Graylog, Sentry a Statuscake.

Znie to zaujato, ale potom, čo som rád prevádzkoval Nagios a ďalšie monitorovacie systémy interne, pri každom novom angažmáne by som kúpil hostované riešenie a zbavil sa tej bolesti.


### Nagios + Nagiosgraph

Prevádzkujeme Nagios pre všetko monitorovanie a upozorňovanie. Upozornenia prebiehajú e-mailom (varovania a kritické oznámenia) a zvukovými oznámeniami aplikácie (pre kritické upozornenia).

Nagiosgraph sa používa na vizualizácie.

Toto nastavenie bolo veľmi účinné pri tom, aby nás komplexne informovalo o tom, čo sa deje v našom prostredí. Prevádzkujeme a monitorujeme asi 110 kritických serverov a asi 760 dátových bodov a tento systém máme zavedený cez sedem rokov.

Chcel by som tiež niekedy agregovať logy pomocou Graylog alebo ELK.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager cez skvelý helm chart Prometheus Operator. Logy stále idú do plánu birch LogDNA, pretože sme si všimli, že ELK je príliš ťažký pre náš skromný klaster s min. 3 a max. 5 uzlami na GKE.


### DataDog + Sentry + PagerDuty.

Predtým som prevádzkoval všetky svoje vlastné monitorovacie riešenia pomocou všetkých možných softvérov vrátane Nagios, Icinga, Zabbix, ELK, Greylog2, Influx a mnohých ďalších nástrojov, ale pravdou je, že prevádzkovať vlastnú monitorovaciu infraštruktúru je príliš veľké úsilie, najmä keď môžete niekomu inému zaplatiť tak nízke sadzby, aby to urobil za vás!

Platenie druhým za prevádzku monitorovacej infraštruktúry uvoľňuje ruky mojim klientom, aby sa sústredili na prevádzku svojich platforiem namiesto monitorovania monitoringu, čo znamená, že hodnota, ktorú získajú zo stability svojej platformy, ďaleko prevyšuje akékoľvek náklady na monitoring ako službu.


### Sensu + Graphite + ELK

Moja firma si veľmi potrpí na vlastné hostovanie.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager pre upozornenia, môj tím verí, že jednoduché monitorovanie je dobré monitorovanie.

Iné systémy ako logovanie a trasovanie poskytnú bohatý kontext pre diagnostiku, keď pohotovostný pracovník dostane upozornenie, ale nikdy na nich nestavíme upozornenia.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Služby inštrumentované Prometheom => analýza a vizualizácia Circonus


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Používame nižšie uvedené služby:

icinga2 na monitorovanie a VictorOps na upozornenia

NewRelic na podrobné monitorovanie služby

Sentry na sledovanie chýb v službe

Slack/e-mail sú súčasťou upozornení spúšťaných z NewRelic alebo icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 s integráciou elasticsearch na analýzu a integráciou graphite+grafana pre grafy.

vďaka flexibilite pravidiel apply v icinga2 vidia vývojári iba služby, o ktorých dostávajú oznámenia.

a cez icinga2 director môžu programátori ľahko definovať svoje vlastné kontroly (čo aj robia, každých pár dní — 100 kontrol odíde, ďalších 100 príde) vo veľkom rozsahu bez problémov.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Čo máme teraz:

DataDog pre metriky

New Relic pre monitorovanie aplikácií

ELK (Elastic Search + Logstash + Kibana) pre logy

Sentry (vlastné hostovanie) pre logovanie výnimiek

E-maily + Slack + VictorOps pre upozornenia (podľa závažnosti)

Čo chceme mať:

Prometheus pre metriky (Grafana na vizualizáciu)

New Relic (pravdepodobne Elastic Search APM) pre monitorovanie aplikácií

EFK (elastic search + fluentd + kibana) pre logovanie. Pravdepodobne Loki od Grafana bude pripravené pre produkciu, než sa k tomu dostaneme

Sentry pre výnimky

Alertmanager + e-mail + VictorOps pre upozornenia


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Upozornenie: pracujem vo VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf pre metriky servera ako CPU, disk, pamäť a sieť. Telegraf používame aj na monitorovanie SNMP našich sieťových zariadení.

Prometheus pre metriky aplikácie. Do našej aplikácie kódujeme kontroly stavu, ktoré Prometheus zbiera.

InfluxDB na ukladanie časových radov. Sem sa posielajú dáta z Telegrafu.

Grafana pre dashboardy a upozornenia. Mechanizmus upozornení nie je super robustný, ale svoju prácu robí. Upozornenia posielame aj do Slacku.

Čo teraz nemám, je centralizované riešenie logovania. ELK je výkonný, ale ťažko sa nastavuje a spravuje, a nepoznám žiadne bezplatné alternatívy, ktoré by boli dosť blízko, aby sa oplatilo ich skúmať.


### Sematext + Logagent + Experience

Sematext pre metriky, pre logy, pre stopy, čoskoro aj pre monitorovanie reálnych používateľov. Podľa môjho skromného názoru jednoduchšie/lacnejšie než používanie N rôznych nástrojov/služieb.

Na odosielanie logov sme predtým používali rsyslog a potom sme prešli na Logagent.

Na hlásenie pádov front-endu používame Sentry, ale čoskoro prejdeme na Experience.

Upozornenie: som Sematextan (zamestnanec Sematext).


### Azure Monitor/Analytics + OpsGenie

Prial by som si, aby Log Analytics mal lepšie rozhranie. Odchádzame od Splunku, v ktorom sa bolo oveľa jednoduchšie orientovať.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Naozaj nechcete prevádzkovať vlastný systém upozornení. Splunk môžete nahradiť ELK, ak váš bezpečnostný tím nepreferuje Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf ako zberač, Prometheus + Alertmanager pre monitorovanie a upozornenia, integrované s kanálmi slack a pagerduty pre kritické upozornenia. Grafana na vizualizáciu metrík hostiteľov.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus pre metriky + upozornenia

Grafana pre dashboardy Prometheus

Cloudwatch monitorujúci inštancie Prometheus

sentry na sledovanie výnimiek

kibana + elasticsearch

graylog

prometheus Push Gateway pre dávkové úlohy/cronjoby

SOP https://github.com/rapidloop/sop na „posielanie/preposielanie“ metrík z jednej inštancie Prometheus do druhej

klienti používajú klientov Prometheus. Snažíme sa používať opencensus.io na strane klienta


### PagerDuty + Monitis

PagerDuty + Monitis. Tiež nejaké vlastné Azure Functions na testovanie zdravia niektorých služieb.

Tento rok plánujeme zaviesť Prometheus a Grafanu


### Prometheus + Grafana + Bosun

Prometheus na ukladanie dát časových radov. Grafana na vizualizáciu. Bosun na správu upozornení.


### Azure Monitor/Analytics/Insights/Dashboards

Firma len s Azure: Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana na monitorovanie kontajnerizovaných služieb v Kubernetes cez Prometheus

Monitis na end-to-end monitorovanie služieb, hlavne pre webové API a webové aplikácie

OpsGenie na správu upozornení

Slack na príjem stavových informácií z našich systémov


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Dlhoročný (dev)ops inžinier. Vyrástol som na Nagiose. Rád by som počul názory na môj bootstrapped SaaS https://checklyhq.com. Robíme monitorovanie API a transakcií webu s dosť hlbokými upozorneniami.

Checkly som založil, pretože aktívne / syntetické monitorovanie v oblasti API bolo trochu obmedzené (a drahé). Monitorovanie založené na prehliadači / skriptoch je ešte proprietárnejšie a drahšie. Používame Puppeteer a držíme ceny čo najnižšie.

Náš monitorovací stack:

Checkly (jeme vlastné jedlo...)

AppOptics (vlastné grafy)

AWS Cloudwatch a SNS pre SMS správy.

vstavané upozornenia Heroku.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana nás upozorňuje v slacku na problémy s infraštruktúrou alebo zhoršenie výkonu a logz.io sme nakonfigurovali tak, aby upozorňovalo v slacku pri určitom objeme logov úrovne chyba z aplikačnej vrstvy.


### SignalFX + Splunk + PagerDuty + Slack

V súčasnosti používame: SignalFX, Splunk, PagerDuty a Slack. Nie som veľký fanúšik SignalFX, hoci ich tím podpory je super priateľský a reaguje rýchlo. Splunk sa mi páči (oplatí sa, ak si ho môžete dovoliť), PagerDuty a Slack tiež.

Predtým som používal stack TICK, kde väčšina C bola v skutočnosti G, teda Grafana, hoci som trochu používal aj Chronograf. Bolo to úžasné, ale bolestivé na správu. Klasická dilema SaaS verzus vlastné hostovanie.

Používal som DataDog, New Relic, Graylog, ELK a BugSnag. DataDog a New Relic sa mi veľmi páčia, Graylog je celkom dobrý. Nie som veľký fanúšik ELK. BugSnag je pekný, vlastne mám pocit, že sledovanie chýb/výnimiek je v mnohých prípadoch celkom dobrá náhrada plného monitorovania logov.


### ELK + Prometheus + Grafana

Ako ostatní používame ELK pre logy a Prometheus+Grafana pre všetko ostatné.

Údržba tohto nastavenia je jednoduchá, ak si môžete dovoliť občas prísť o dáta. Napríklad ak sa naša databáza ElasticSearch dostane do problémov (čo sa bohužiaľ stáva každé 2–3 mesiace), nezaoberáme sa HA, ale dáta zahodíme a ideme ďalej. Ak absolútne musíte mať HA alebo dlhodobé uchovávanie, veľa šťastia.


### Datadog + Prometheus + Grafana

Datadog som nastavil na mesačnej báze, pretože keď som sem prišiel, nebolo tu žiadne monitorovanie ani upozornenia. Len pár našich webov sa monitorovalo každých 5 minút na dostupnosť. Datadog je suverénne najjednoduchší na nastavenie. Keď dokončím riešenie všetkých ostatných problémov, prejdem na Prometheus+Grafana. Ohľadom správy logov ešte nie som 100 % rozhodnutý.

### Nagios + ELK

Podporujeme cez 100 produktov.

Pre on-prem je to väčšinou Nagios a ELK. V cloude migrujeme z DataDog na NewRelic.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Predtým sme používali datadog, ale zistili sme, že je pre naše potreby príliš drahý. Nechápte ma zle, je úžasný, ale má obrovské náklady. Podarilo sa nám nastaviť site24x7.com s ročným predplatným za asi 2–3 mesiace nákladov DD.

Náš monitorovací stack:

Site24x7 - APM, monitorovanie externých URL, monitorovanie toku pošty SMTP, vypršanie ssl a monitorovanie procesov.

StatusCake - na monitorovanie a potvrdzovanie URL - je to naša záloha pre prípad, že by site24x7 niečo prehliadlo (neprehliadne), ale SC je flexibilnejší pre monitorovanie externých portov a služieb pre naše potreby.

Oba nástroje eskalujú do PagerDuty a potom dostávame eskalácie v slacku.

SumoLogic - na monitorovanie logov (je to skvelý nástroj, ale trochu zložitý pre naše potreby)

Zo slacku môžeme upozornenie potvrdiť alebo napraviť.

Potom máme mnoho automatizácií site24x7, ktoré sa pripájajú ku commando.io pre „BedOps“, ako tomu hovoríme — kde sa spustí upozornenie, spustíme niekoľko skriptov alebo automatizácií v snahe situáciu napraviť (v 99 % prípadov nás automatizácia + naše skripty udržia mimo problémov).

Máme interné runbooky v našej znalostnej báze pre prípad, že automaty zlyhajú alebo treba opraviť niečo mimo rozsahu.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana pre metriky v našich klastroch GKE a na virtuálnych strojoch.

Google Stackdriver pre logy (pretože je zahrnutý a predvolene aktívny a v súčasnosti pre naše potreby postačuje).


### Zabbix

Zabbix pre všetko. Nie je potrebný žiadny iný softvér.


