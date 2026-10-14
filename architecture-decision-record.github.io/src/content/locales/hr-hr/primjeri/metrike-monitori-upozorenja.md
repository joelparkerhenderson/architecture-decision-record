# Metrike, monitori, upozorenja

Sadržaj:

* [Sažetak](#sažetak)
  * [Problem](#problem)
  * [Odluka](#odluka)
  * [Status](#status)
* [Pojedinosti](#pojedinosti)
  * [Pretpostavke](#pretpostavke)
  * [Ograničenja](#ograničenja)
  * [Pozicije](#pozicije)
  * [Argument](#argument)
  * [Implikacije](#implikacije)
* [Povezano](#povezano)
  * [Povezane odluke](#povezane-odluke)
  * [Povezani zahtjevi](#povezani-zahtjevi)
  * [Povezani artefakti](#povezani-artefakti)
  * [Povezana načela](#povezana-načela)
* [Bilješke](#bilješke)
  * [Slobodne tekstualne poruke naspram strukturiranih poruka događaja](#slobodne-tekstualne-poruke-naspram-strukturiranih-poruka-događaja)
  * [Graylog je lakši](#graylog-je-lakši)
  * [Prometheus zahtijeva malo podešavanja](#prometheus-zahtijeva-malo-podešavanja)
  * [AWS usluge su miješane](#aws-usluge-su-miješane)
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


## Sažetak


### Problem

Želimo koristiti metrike, monitore i upozorenja jer želimo znati koliko dobro rade naše aplikacije i znati kada se pojavi problem.


### Odluka

U tijeku (WIP).


### Status

Prikupljanje informacija. Počinjemo od vjerojatnih krajeva spektra: najpreporučeniji stariji besplatni alat (Nagios) i najpreporučeniji noviji plaćeni alat (New Relic).


## Pojedinosti


### Pretpostavke

Želimo stvarati web aplikacije koje su moderne, brze, pouzdane, responzivne itd.

Želimo kupovati, a ne graditi.


### Ograničenja

Želimo alate koji dobro rade s našim devops cjevovodom i našim cloudovima za implementaciju.


### Pozicije

Pozicije trenutačno istražujemo.


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

Za sada su Nagios i New Relic krajevi spektra. Nagios je najstariji, najjednostavniji, besplatan, održiv alat. New Relic je alat s najnovijim značajkama, najcjelovitiji, plaćen, održiv. Počet ćemo vrednovanjem ta dva. Prema potrebi ćemo se pomaknuti prema unutrašnjosti spektra.  

Za sada Zabbix ima najbolje preporuke i nudi također najcjelovitije mogućnosti.

Za sada ELK ima najbolju popularnost među rješenjima otvorenog koda koja preferiraju izgradnju pred kupnjom.

Za sada Prometheus + Grafana imaju najbolju popularnost.


### Implikacije

TODO.


## Povezano


### Povezane odluke

Izbori će utjecati na mogućnost testiranja, telemetriju i vjerojatno druge sustave, na primjer za korisničku podršku, inženjerstvo pouzdanosti web-mjesta (SRE) itd.


### Povezani zahtjevi

TODO.


### Povezani artefakti

TODO.


### Povezana načela

Lako reverzibilno.

Potreba za brzinom.


## Bilješke


Prilično dobar stog otvorenog koda je:

* Prometheus za metrike i upozorenja temeljena na metrikama

* Grafana za prikaz metrika

* Elasticsearch/Logstash/Kibana (ELK) za zapisnike i strukturirane događaje

* Pushover za mobilne obavijesti


### Slobodne tekstualne poruke naspram strukturiranih poruka događaja

Slobodne tekstualne poruke: na primjer, vrsta nasumičnih stvari koje ćete pronaći u /var/log/messages i nešto što aplikacije namjerno stvaraju. Poruke su korisne za identifikaciju drugih stvari koje se događaju na stroju, poput nedostatka memorije ili hardverskih pogrešaka, ali imaju mnogo smeća. 

Strukturirane poruke događaja: generira ih aplikacija, s fiksnim ili dinamičnim skupom atributa, npr. zapisnik HTTP zahtjeva, računovodstveni zapisnik, prijava korisnika.

Općenito je dobro bilježiti pojedinosti svakog zahtjeva na način koji omogućuje dubinsko istraživanje po atributima. Dodavanje npr. userid ili sessionid svemu stoga omogućuje praćenje. Eksplicitno praćenje (tracing) naravno je također dobro. Korištenje ELK-a za to svojevrsna je jadna verzija https://www.honeycomb.io/


### Graylog je lakši

Prema mom iskustvu, Graylog je lakše pokrenuti.



### Prometheus zahtijeva malo podešavanja


Općenito sam zadovoljan Prometheusom za metrike. Upozorenja zahtijevaju malo podešavanja, ali su prilično dobra. Ovisi o vašoj aplikaciji. Mislim da je najbolje upozoravati na stanja vidljiva krajnjem korisniku, a ne na temeljne uzroke. Na primjer, vrijeme učitavanja stranice je dobro, broj zahtjeva u sekundi nije. Iako nula zahtjeva u sekundi sugerira da nešto nije u redu.

Prednost usluge je što nudi dodatnu inteligenciju odmah po instalaciji. Općenito mi se sviđa Datadog. Usluge mogu biti zastrašujuće skupe ako imate mnogo podataka, a ponekad imaju cjenovne modele koji nisu prijateljski prema cloudu, npr. naplata po instanci kada su instance dinamične. Postoji i razlika između usluga gdje svaki zahtjev dolazi od korisnika koji plaća i onih povezanih s oglašavanjem, pa samo mali postotak zahtjeva zarađuje novac. Možete završiti s mnogo podataka i ne tako velikim proračunom.

Radim na nekim uslugama koje primaju 1 milijardu zahtjeva dnevno, pa ima smisla samostalno hostirati nadzor i zapisivanje. Ako su vaši obujmi manji, hostirane usluge su lakše.


### AWS usluge su miješane

Moje iskustvo s AWS uslugama je miješano. Njihova usluga Elasticsearch bila je nepouzdana, pa pokrećemo vlastite instance. CloudWatch metrike su skupe, pa ih općenito koristimo samo za metrike na razini „infrastrukture”, a ne aplikacije, tj. metrike povezane sa zdravljem, gdje AWS može bolje znati što se događa od softvera koji radi na instanci. CloudWatch zapisnici mogu se sporo ažurirati i nemaju toliko metapodataka. Pokretanje ELK-a pomaže s tim. Ako stvarno želim podatke u stvarnom vremenu, bolje je koristiti Kafku kao transport zapisnika. Logstash to prilično dobro podržava. Međutim, upravljanje Kafka klasterom nije za slabe živce, ima mnogo izloženih cijevi.


### Kafka

Komentar: Kafka ponekad može biti iznimno hirovita ili može biti čvrsta kao stijena pa gotovo zaboravite da postoji i da sve povezuje. 


Komentar: Kafka je bila solidna, ali pokretanje je bilo iznenađujuće puno posla. Zamišljam je kao relacijsku bazu podataka, ali u kojoj radite samo na „fizičkom” sloju, npr. tablični prostori, datoteke i particije. Na početku je bilo trenutaka kada su nedostajali alati za upravljanje pa smo morali pisati programe, primjerice za resetiranje grupe potrošača. http://howfuckedismydatabase.com/nosql/

Komentar: Koristimo Kafku kao „međuspremnik” za zapisničke poruke i mjesto gdje možemo obavljati obradu toka u stvarnom vremenu nad podacima koji dolaze s više poslužitelja. Ako nas pogodi DDOS napad, trebamo način za analizu podataka na više instanci. Ako zapisujemo izravno s poslužitelja u ELK, opterećenje može srušiti Elasticsearch klaster.

Komentar: Kafka je dobra za nas jer ako nas pogodi DDOS napad, trebamo način za analizu podataka na više instanci. Ako zapisujemo izravno s poslužitelja u ELK, opterećenje može srušiti Elasticsearch klaster.


Komentar: Kafka radi manje posla i učinkovitija je, pa bolje podnosi opterećenje. A posao Kafke stavljamo u red i ponavljamo. A preopterećenje Kafke ne utječe na korisnike koji pokušavaju interaktivno raditi s Kibanom, kao što bi bilo da se Elasticsearch muči.

Komentar:  Obrada toka uglavnom traži zlouporabu, npr. previše prometa s jednog IP-a kroz cijeli klaster, a zatim dijeli blokiranje kroz cijeli klaster.

Komentar: Dodatak logstash-output-kafka međutim je trenutačno prilično nepouzdan. Ugrizlo me nekoliko problema s njegove stranice issues na GitHubu koji se čini da se nikad ne popravljaju. Želim prestati koristiti ga i slati izravno iz naših aplikacija u Kafku.

Komentar: Sada šaljemo strukturirane događaje izravno iz aplikacije u Kafku. Glavna motivacija bila je rjeđe dodirivati podatke zapisnika i izbjeći višekratno čitanje i pisanje na disk. U sustavima velikog obujma zapisivanje može zahtijevati više posla od same aplikacije. Razmišljam i o tome da journald također šalje zapisnike izravno, iz programa u C-u.


### Loki

Pratite Loki. Još nije gotov, ali kad bude, očekujem da će bolje odgovarati ovom stogu. Loki je agregator zapisnika koji je izradio Grafana Labs, koristi sličnu sintaksu prikupljanja i oznaka kao Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager za metrike. <3 Prometheus.

Rollbar/Graylog za zapisivanje/izvješćivanje o pogreškama (postoji određeno preklapanje; mala usluga vjerojatno ne treba oboje).

Trenutačno upozorenja idu samo u jedan od nekoliko Slack kanala gdje zainteresirane strane imaju uključene obavijesti. Kad bismo dežurstvo (on-call) shvatili ozbiljnije, išla bi u PagerDuty/VictorOps itd.

Grafana za grafikone i nadzorne ploče. Također se veselim hoće li njihove nadolazeće mogućnosti zapisivanja učiniti Graylog nepotrebnim.


### Thanos

Koristimo Thanos kao front-end za našu HA postavu. Može deduplicirati HA parove.

Trenutačno čuvamo 6 mjeseci lokalnih podataka Prometheusa. Za nas to radi razumno dobro. Ali usred sam uvođenja pohrane bucket u našu postavu Thanosa za dugoročnu pohranu podataka. Teoretski će GCS pohrana biti oko 30 % jeftinija od standardnog trajnog diska GCE koji sada koristimo.

Trenutačno ne izrađujemo sigurnosne kopije podataka Prometheusa. Podaci za nas zapravo nisu važni osim što ih treba biti dovoljno za upozorenja. Naša ukupna implementacija flote mijenja se toliko iz godine u godinu da povijesni podaci stariji od nekoliko mjeseci nisu zaista zanimljivi. Moglo bi biti zanimljivo imati nekoliko osnovnih statistika iz godine u godinu; mogu postaviti skup pravila snimanja za osnovne statistike i pohranjivati ih pomoću Federation ili jednostavno pustiti Thanosu da se pobrine.

EDIT: Mala napomena, ja sam razvijatelj Prometheusa.


### Prometheus HA

HA u Prometheusu radi se dupliciranjem — pokrećete više instanci za prikupljanje i postoje načini da se upituje više njih i deduplicira podatke

Skaliranje se radi podjelom mreže i time da različiti Prometheusi upituju različite dijelove mreže

Dugoročna pohrana nije jaka strana Prometheusa, ali se prebacuje na nešto poput Influxa ili timescaledb (koji tehnički također označava HA) članak koji sam pročitao o tome https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Dugoročne stvari još nisam isprobao jer još samo eksperimentiram i koristim ga za kratkoročne grafikone dok librenms dugoročno nadzire moju mrežu


###  Datadog + PagerDuty + Threat Stack

Koristimo Datadog (s PagerDutyjem) i Threat Stack i ne bismo mogli biti zadovoljniji. Moja jedina zamjerka DD-u je relativno visok trošak pohrane metrika.


### Zabbix

Zabbix s prilagođenim skriptama za nadzor gotovo svega. Radi sjajno.


### Outlyer

Koristim Outlyer, ali moram izjaviti da tamo radim i da je korištenje vlastitog proizvoda obveza.

I dalje trebam Graylog, Sentry i Statuscake za nadopunu.

Zvuči pristrano, ali nakon što sam rado interno pokretao Nagios i druge sustave nadzora, na svakom bih novom angažmanu kupio hostirano rješenje i riješio se muke.


### Nagios + Nagiosgraph

Pokrećemo Nagios za sav nadzor i upozoravanje. Upozorenja idu e-poštom (upozorenja i kritične obavijesti) i zvučnim obavijestima aplikacije (za kritična upozorenja).

Nagiosgraph se koristi za vizualizacije.

Ova postava bila je vrlo učinkovita u cjelovitom informiranju o tome što se događa u našem okruženju. Pokrećemo i nadziremo oko 110 kritičnih poslužitelja i oko 760 podatkovnih točaka te imamo ovaj sustav više od sedam godina.

Također bih jednog dana želio agregirati zapisnike pomoću Graylog ili ELK.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager kroz sjajan helm chart Prometheus Operator. Zapisnici i dalje idu u plan birch tvrtke LogDNA jer smo primijetili da je ELK pretežak za naš skromni klaster s min. 3 i maks. 5 čvorova na GKE-u.


### DataDog + Sentry + PagerDuty.

Prije sam pokretao sva vlastita rješenja nadzora koristeći sve moguće softvere, uključujući Nagios, Icinga, Zabbix, ELK, Greylog2, Influx i mnoge druge alate, ali istina je da je pokretanje vlastite infrastrukture za nadzor prevelik napor, osobito kad možete platiti nekome drugome tako niske cijene da to učini umjesto vas!

Plaćanje drugima da pokreću infrastrukturu za nadzor oslobađa ruke mojim klijentima da se usredotoče na pokretanje svojih platformi umjesto nadzora nadzora, što znači da vrijednost koju dobivaju od stabilnosti svoje platforme daleko nadmašuje svaki trošak nadzora kao usluge.


### Sensu + Graphite + ELK

Moja tvrtka je vrlo za samostalno hostiranje.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager za upozorenja, moj tim vjeruje da je jednostavan nadzor dobar nadzor.

Drugi sustavi poput zapisivanja i praćenja pružit će bogat kontekst za dijagnostiku kada dežurni primi upozorenje, ali nikada na njima ne gradimo upozorenja.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Usluge instrumentirane Prometheusom => analiza i vizualizacija Circonus


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Koristimo dolje navedene usluge:

icinga2 za nadzor i VictorOps za upozorenja

NewRelic za detaljan nadzor usluge

Sentry za praćenje pogrešaka u usluzi

Slack/e-pošta dio su upozorenja pokrenutih iz NewRelica ili icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 s integracijom elasticsearcha za analitiku i integracijom graphite+grafana za grafikone.

zahvaljujući fleksibilnosti pravila apply u icinga2 programeri vide samo usluge o kojima primaju obavijesti.

a putem icinga2 directora programeri mogu lako definirati vlastite provjere (što i rade, svakih nekoliko dana — 100 provjera odlazi, dolazi još 100) u velikom opsegu bez problema.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Što imamo sada:

DataDog za metrike

New Relic za nadzor aplikacija

ELK (Elastic Search + Logstash + Kibana) za zapisnike

Sentry (samostalno hostiran) za zapisivanje iznimki

E-pošta + Slack + VictorOps za upozorenja (prema ozbiljnosti)

Što želimo imati:

Prometheus za metrike (Grafana za vizualizaciju)

New Relic (vjerojatno Elastic Search APM) za nadzor aplikacija

EFK (elastic search + fluentd + kibana) za zapisivanje. Vjerojatno će Loki iz Grafane biti spreman za produkciju prije nego što stignemo do toga

Sentry za iznimke

Alertmanager + e-pošta + VictorOps za upozorenja


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Odricanje: radim u VMwareu)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf za metrike poslužitelja poput CPU-a, diska, memorije i mreže. Telegraf koristimo i za SNMP nadzor naših mrežnih uređaja.

Prometheus za metrike aplikacije. U našu aplikaciju kodiramo provjere zdravlja koje Prometheus prikuplja.

InfluxDB za pohranu vremenskih nizova. Ovdje se šalju podaci iz Telegrafa.

Grafana za nadzorne ploče i upozorenja. Mehanizam upozorenja nije super robustan, ali obavlja posao. Upozorenja šaljemo i u Slack.

Ono što sada nemam je centralizirano rješenje zapisivanja. ELK je moćan, ali težak za postavljanje i upravljanje, a ne znam za besplatne alternative koje su dovoljno blizu da ih vrijedi istražiti.


### Sematext + Logagent + Experience

Sematext za metrike, za zapisnike, za tragove, uskoro i za nadzor stvarnih korisnika. Po mom skromnom mišljenju jednostavnije/jeftinije od korištenja N različitih alata/usluga.

Za slanje zapisnika prije smo koristili rsyslog, a zatim prešli na Logagent.

Za izvješćivanje o rušenjima front-enda koristimo Sentry, ali uskoro ćemo prijeći na Experience.

Odricanje: ja sam Sematextan (zaposlenik Sematexta).


### Azure Monitor/Analytics + OpsGenie

Volio bih da Log Analytics ima bolje sučelje. Odlazimo sa Splunka, u kojem je bilo mnogo lakše snalaziti se.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Stvarno ne želite pokretati vlastiti sustav upozorenja. Splunk možete zamijeniti ELK-om ako vaš sigurnosni tim ne preferira Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf kao prikupljač, Prometheus + Alertmanager za nadzor i upozorenja, integrirani s kanalima slack i pagerduty za kritična upozorenja. Grafana za vizualizaciju metrika hostova.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus za metrike + upozorenja

Grafana za nadzorne ploče Prometheusa

Cloudwatch koji nadzire instance Prometheusa

sentry za praćenje iznimki

kibana + elasticsearch

graylog

prometheus Push Gateway za skupne poslove/cronjobove

SOP https://github.com/rapidloop/sop za „guranje/prosljeđivanje” metrika iz jedne instance Prometheusa u drugu

klijenti koriste klijente Prometheusa. Pokušavamo koristiti opencensus.io na strani klijenta


### PagerDuty + Monitis

PagerDuty + Monitis. Također neke prilagođene Azure Functions za testiranje zdravlja nekih usluga.

Ove godine planiramo uvesti Prometheus i Grafanu


### Prometheus + Grafana + Bosun

Prometheus za pohranu podataka vremenskih nizova. Grafana za vizualizaciju. Bosun za upravljanje upozorenjima.


### Azure Monitor/Analytics/Insights/Dashboards

Tvrtka samo s Azureom: Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana za nadzor kontejneriziranih usluga u Kubernetesu preko Prometheusa

Monitis za end-to-end nadzor usluga, uglavnom za web API-je i web aplikacije

OpsGenie za upravljanje upozorenjima

Slack za primanje informacija o stanju iz naših sustava


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Dugogodišnji (dev)ops inženjer. Odrastao sam na Nagiosu. Volio bih čuti mišljenja o mom bootstrapped SaaS-u https://checklyhq.com. Radimo nadzor API-ja i transakcija web-mjesta s prilično dubokim upozorenjima.

Osnovao sam Checkly jer je aktivni / sintetički nadzor u području API-ja bio donekle ograničen (i skup). Nadzor temeljen na pregledniku / skriptama još je vlasničkiji i skuplji. Koristimo Puppeteer i držimo cijene što je moguće nižima.

Naš stog za nadzor:

Checkly (jedemo vlastitu hranu...)

AppOptics (prilagođeni grafikoni)

AWS Cloudwatch i SNS za SMS poruke.

ugrađena upozorenja Herokua.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana nas upozorava u slacku na probleme s infrastrukturom ili degradaciju performansi, a logz.io smo konfigurirali da upozorava u slacku pri određenom obujmu zapisnika razine pogreška iz aplikacijskog sloja.


### SignalFX + Splunk + PagerDuty + Slack

Trenutačno koristimo: SignalFX, Splunk, PagerDuty i Slack. Nisam veliki obožavatelj SignalFX-a, iako je njihov tim za podršku super prijateljski i brzo reagira. Splunk mi se sviđa (isplati se ako si ga možete priuštiti), PagerDuty i Slack također.

Prije sam koristio TICK stog, gdje je većina C-a zapravo bila G, tj. Grafana, iako sam malo koristio i Chronograf. Bilo je sjajno, ali mučno za upravljanje. Klasična dilema SaaS naspram samostalnog hostiranja.

Koristio sam DataDog, New Relic, Graylog, ELK i BugSnag. DataDog i New Relic mi se jako sviđaju, Graylog je prilično dobar. Nisam veliki obožavatelj ELK-a. BugSnag je lijep, zapravo imam osjećaj da je praćenje pogrešaka/iznimki u mnogim slučajevima prilično dobra zamjena za potpuni nadzor zapisnika.


### ELK + Prometheus + Grafana

Kao i drugi, koristimo ELK za zapisnike i Prometheus+Grafana za sve ostalo.

Održavanje ove postave je jednostavno ako si možete priuštiti povremeni gubitak podataka. Na primjer, ako naša ElasticSearch baza podataka zapadne u nevolju (što se nažalost događa svaka 2–3 mjeseca), ne zamaramo se s HA, nego odbacimo podatke i idemo dalje. Ako apsolutno morate imati HA ili dugoročno čuvanje, sretno.


### Datadog + Prometheus + Grafana

Datadog sam postavio na mjesečnoj osnovi jer kad sam došao ovdje, nije bilo nikakvog nadzora ni upozorenja. Samo je nekoliko naših web-mjesta nadzirano svakih 5 minuta radi dostupnosti. Datadog je daleko najlakši za postavljanje. Nakon što završim s rješavanjem svih ostalih problema, prijeći ću na Prometheus+Grafana. Još nisam 100 % odlučan oko upravljanja zapisnicima.

### Nagios + ELK

Podržavamo preko 100 proizvoda.

Za on-prem to su uglavnom Nagios i ELK. U cloudu migriramo s DataDoga na NewRelic.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Prije smo koristili datadog, ali utvrdili smo da je preskup za naše potrebe. Nemojte me krivo shvatiti, sjajan je, ali ima ogroman trošak. Uspjeli smo postaviti site24x7.com s godišnjom pretplatom za oko 2–3 mjeseca troška DD-a.

Naš stog za nadzor:

Site24x7 - APM, nadzor vanjskih URL-ova, nadzor toka pošte SMTP-om, istek ssl-a i nadzor procesa.

StatusCake - za nadzor i potvrdu URL-ova - to je naša rezerva u slučaju da site24x7 nešto propusti (ne propušta), ali SC je fleksibilniji za nadzor vanjskih portova i usluga za naše potrebe.

Oba alata eskaliraju u PagerDuty, a zatim eskalacije primamo u slacku.

SumoLogic - za nadzor zapisnika (sjajan je alat, ali malo složen za naše potrebe)

Iz slacka možemo potvrditi upozorenje ili ga otkloniti.

Zatim imamo mnogo automatizacija site24x7 koje se povezuju s commando.io za „BedOps” kako ga zovemo — gdje se pri pokretanju upozorenja pokreće nekoliko skripti ili automatizacija u pokušaju da se situacija ispravi (u 99 % slučajeva automatizacija + naše skripte drže nas izvan nevolje).

Imamo interne runbookove u našoj bazi znanja za slučaj da automati zakažu ili treba popraviti nešto izvan opsega.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana za metrike u našim GKE klasterima i na virtualnim strojevima.

Google Stackdriver za zapisnike (jer je uključen i aktivan prema zadanim postavkama i trenutačno dostatan za naše potrebe).


### Zabbix

Zabbix za sve. Nije potreban nikakav drugi softver.


