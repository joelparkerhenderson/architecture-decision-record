# Metrike, nadzor, opozorila

Vsebina:

* [Povzetek](#povzetek)
  * [Vprašanje](#vprašanje)
  * [Odločitev](#odločitev)
  * [Stanje](#stanje)
* [Podrobnosti](#podrobnosti)
  * [Predpostavke](#predpostavke)
  * [Omejitve](#omejitve)
  * [Stališča](#stališča)
  * [Argument](#argument)
  * [Posledice](#posledice)
* [Povezano](#povezano)
  * [Povezane odločitve](#povezane-odločitve)
  * [Povezane zahteve](#povezane-zahteve)
  * [Povezani artefakti](#povezani-artefakti)
  * [Povezana načela](#povezana-načela)
* [Opombe](#opombe)
  * [Prosta besedilna sporočila ali strukturirana sporočila dogodkov](#prosta-besedilna-sporočila-ali-strukturirana-sporočila-dogodkov)
  * [Graylog je enostavnejši](#graylog-je-enostavnejši)
  * [Prometheus zahteva nekaj uglaševanja](#prometheus-zahteva-nekaj-uglaševanja)
  * [Storitve AWS so mešane](#storitve-aws-so-mešane)
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
  * [Datadog ali Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack](#datadog-ali-site24x7--statuscake--pagerduty--sumologic--slack)
  * [Prometheus + AlertManager + Grafana + Stackdriver](#prometheus--alertmanager--grafana--stackdriver)
  * [Zabbix](#zabbix-1)


## Povzetek


### Vprašanje

Želimo uporabljati metrike, nadzor in opozorila, ker želimo vedeti, kako dobro delujejo naše aplikacije, in vedeti, kdaj pride do težave.


### Odločitev

V delu (WIP).


### Stanje

Zbiranje informacij. Začenjamo z verjetnima konceloma spektra: najbolj priporočanim starejšim brezplačnim orodjem (Nagios) in najbolj priporočanim novejšim plačljivim orodjem (New Relic).


## Podrobnosti


### Predpostavke

Želimo ustvariti spletne aplikacije, ki so sodobne, hitre, zanesljive, odzivne itd.

Želimo kupiti, namesto da bi gradili.


### Omejitve

Želimo orodja, ki dobro delujejo z našim cevovodom DevOps in z našimi oblaki za uvajanje.


### Stališča

Stališča trenutno raziskujemo.


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

Doslej sta Nagios in New Relic konca spektra. Nagios je najstarejše, najpreprostejše, brezplačno, izvedljivo orodje. New Relic je najnovejše po funkcijah, najcelovitejše, plačljivo, izvedljivo orodje. Začeli bomo z vrednotenjem teh dveh. Po potrebi se bomo premaknili v spekter.  

Doslej ima Zabbix najboljša priporočila in ponuja tudi najcelovitejše zmožnosti.

Doslej ima ELK najboljšo priljubljenost med odprtokodnimi rešitvami po načelu »zgradi namesto kupi«.

Doslej imata Prometheus + Graphana najboljšo priljubljenost.


### Posledice

TODO.


## Povezano


### Povezane odločitve

Izbire bodo vplivale na testabilnost, telemetrijo in verjetno tudi na druge sisteme, kot so tisti za podporo strankam, inženirstvo zanesljivosti spletnih mest itd.


### Povezane zahteve

TODO.


### Povezani artefakti

TODO.


### Povezana načela

Lahko povratljivo.

Potreba po hitrosti.


## Opombe


Precej dober odprtokodni sklad je:

* Prometheus za metrike in opozarjanje na podlagi metrik

* Grafana za prikaz metrik

* Elasticsearch/Logstash/Kibana (ELK) za dnevnike in strukturirane dogodke

* Pushover za mobilna obvestila


### Prosta besedilna sporočila ali strukturirana sporočila dogodkov

Prosta besedilna sporočila: na primer vrsta naključnih stvari, ki jih najdete v /var/log/messages, in nekaj, kar aplikacija ustvari namenoma. Sporočila so koristna za prepoznavanje drugih dogajanj v računalniku, kot so pomanjkanje pomnilnika ali napake strojne opreme, vendar vsebujejo veliko balasta. 

Strukturirana sporočila dogodkov: ustvari jih aplikacija, s fiksnim ali dinamičnim naborom atributov, npr. dnevnik zahtev HTTP, računovodski dnevnik, prijava uporabnika.

Na splošno je lepo beležiti podrobnosti o vsaki zahtevi na način, da se lahko poglobite glede na atribute. Dodajanje npr. userid ali sessionid vsemu omogoča sledenje. Izrecno sledenje je seveda tudi dobro. Uporaba ELK za to je nekakšen revni človekov https://www.honeycomb.io/


### Graylog je enostavnejši

Graylog je po mojih izkušnjah enostavnejši za zagon.



### Prometheus zahteva nekaj uglaševanja


Z Prometheusom za metrike sem na splošno zadovoljen. Opozarjanje zahteva nekaj uglaševanja, a je precej dobro. Odvisno je od vaše aplikacije. Menim, da je najbolje opozarjati na stanja, ki so vidna končnemu uporabniku, ne na osnovne vzroke. Na primer, čas nalaganja strani je dober, število zahtev na sekundo pa ne. Čeprav nič zahtev na sekundo kaže, da je nekaj narobe.

Prednost storitve je, da ponuja dodatno inteligenco takoj ob uporabi. Datadog mi je na splošno všeč. Storitve so lahko strašljivo drage, če imate veliko podatkov, včasih pa imajo cenovne modele, ki niso prijazni do oblaka, npr. zaračunavanje na instanco, ko so instance dinamične. Obstaja tudi razlika med storitvami, kjer je vsaka zahteva od plačujočega uporabnika, in tistimi, povezanimi z oglaševanjem, kjer le majhen odstotek zahtev prinaša denar. Lahko končate z veliko podatki in ne tako velikim proračunom.

Delam na nekaterih storitvah, ki prejmejo 1 milijardo zahtev na dan, zato je smiselno gostiti lasten nadzor in beleženje. Če so vaši obsegi manjši, so gostovane storitve enostavnejše.


### Storitve AWS so mešane

Moje izkušnje s storitvami AWS so mešane. Njihova storitev Elasticsearch je bila nezanesljiva, zato za to poganjamo lastne instance. Metrike CloudWatch so drage, zato jih na splošno uporabljamo le za metrike na ravni »infrastrukture« in ne aplikacije, tj. metrike, povezane z zdravjem, kjer AWS lahko bolje ve, kaj se dogaja, kot programska oprema, ki teče na instanci. Dnevniki CloudWatch se lahko počasi posodabljajo in nimajo veliko metapodatkov. Poganjanje ELK pri tem pomaga. Če res želim podatke v realnem času, je bolje uporabiti Kafko kot transport za dnevnike. To Logstash dokaj dobro podpira. Upravljanje gruče Kafka pa ni za šibke živce, saj je izpostavljenega veliko inštalaterskega dela.


### Kafka

Komentar: Kafka je lahko občasno zelo zahtevna ali pa trdna kot skala, da skoraj pozabite, da je tam in vse povezuje. 


Komentar: Kafka je bila trdna, vendar je bilo presenetljivo veliko dela, da smo jo spravili do delovanja. Predstavljam si jo kot relacijsko podatkovno bazo, pri kateri delate le na »fizični« plasti, npr. tabelarnih prostorih, datotekah in particijah. Na začetku so bili časi, ko so upravljalska orodja manjkala in smo morali pisati programe, npr. za ponastavitev skupine potrošnikov. http://howfuckedismydatabase.com/nosql/

Komentar: Kafko uporabljamo kot »medpomnilnik« za dnevniška sporočila in kraj, kjer lahko izvajamo obdelavo tokov v realnem času nad podatki, ki prihajajo iz več strežnikov. Če pride do napada DDOS, potrebujemo način za analizo podatkov v več instancah. Če beležimo neposredno iz strežnikov v ELK, lahko obremenitev uniči gručo Elasticsearch.

Komentar: Kafka je za nas dobra, ker če pride do napada DDOS, potrebujemo način za analizo podatkov v več instancah. Če beležimo neposredno iz strežnikov v ELK, lahko obremenitev uniči gručo Elasticsearch.


Komentar: Kafka opravi manj dela in je učinkovitejša, zato lahko bolje obvlada obremenitev. In delo Kafke postavimo v čakalno vrsto in poskusimo znova. In preobremenjena Kafka ne vpliva na uporabnike, ki poskušajo delati interaktivno s Kibano, kot bi vplivalo, če bi imel Elasticsearch težave.

Komentar:  Obdelava tokov večinoma išče zlorabe, npr. preveč prometa z enega IP v celotni gruči, nato pa blokado deli po celotni gruči.

Komentar: Vtičnik logstash-output-kafka je trenutno precej nezanesljiv. Prizadelo me je več težav na njegovi strani GitHub issues, ki se zdi, da se nikoli ne popravijo. Želim se odmakniti od njegove uporabe in pošiljati neposredno iz naših aplikacij v Kafko.

Komentar: Zdaj pošiljamo strukturirane dogodke neposredno iz aplikacije v Kafko. Glavna motivacija je bila, da se podatkov dnevnika dotaknemo manjkrat in se izognemo večkratnemu branju in pisanju na disk. V sistemih z velikim obsegom lahko beleženje zahteva več dela kot sama aplikacija. Razmišljam, da bi tudi journald pošiljal dnevnike neposredno, iz programa v C.


### Loki

Pozorno spremljajte Loki. Še ni pripravljen, ko pa bo, pričakujem, da bo v tem skladu boljša izbira. Loki je zbiralnik dnevnikov, ki so ga ustvarili grafana labs, in uporablja podobno sintakso zbiranja in oznak kot Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager za metrike. <3 Prometheus.

Rollbar/Graylog za beleženje/poročanje o napakah (tu je nekaj prekrivanja; majhna storitev verjetno ne potrebuje obeh).

Trenutno gredo opozorila le v enega od nekaj kanalov Slack, kjer imajo zainteresirane strani vklopljena obvestila. Če bi bili bolj resni glede dežurstva, bi šla v PagerDuty/VictorOps/itd.

Grafana za grafe in nadzorne plošče. Prav tako nestrpno čakam, da vidim, ali bodo njihove prihajajoče zmožnosti beleženja odpravile potrebo po Graylog.


### Thanos

Thanos uporabljamo kot sprednji del za našo nastavitev HA. Zna odstranjevati podvojene pare HA.

Trenutno hranimo 6 mesecev lokalnih podatkov Prometheus. To nam dokaj dobro ustreza. Vendar sem sredi uvajanja shranjevanja v vedrih (bucket storage) v naši nastavitvi Thanos za dolgoročno shranjevanje podatkov. Teoretično bo shranjevanje GCS približno 30 % cenejše od standardnega trajnega diska GCE, ki ga uporabljamo zdaj.

Podatkov Prometheus trenutno ne varnostno kopiramo. Podatki za nas niso zares pomembni, razen da imamo dovolj za opozarjanje. Naše celotno uvajanje flote se iz leta v leto tako spreminja, da zgodovinski podatki, starejši od nekaj mesecev, preprosto niso zanimivi. Morda bi bilo zanimivo imeti nekaj ključnih statistik iz leta v leto; morda bom nastavil nabor snemalnih pravil za ključne statistike in jih shranil z Federation ali pa to prepustil Thanosu.

EDIT: Manjše opozorilo: sem razvijalec Prometheusa.


### Prometheus HA

HA v Prometheusu se izvaja z podvajanjem; poganjate več zbiralnikov (pollerjev) in obstajajo načini za poizvedovanje po več njih in odstranjevanje podvojenih podatkov

Skaliranje poteka z razdelitvijo omrežja in z različnimi Prometheusi, ki poizvedujejo po različnih delih omrežja

Dolgoročno shranjevanje ni Prometheusova močna stran, vendar se prenese na nekaj, kot sta influx ali timescaledb (ki tehnično prav tako izpolnjuje zahtevo HA); članek, ki sem ga prebral o tem: https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Dolgoročnih stvari še nisem preizkusil, ker še vedno samo eksperimentiram in ga uporabljam za kratkoročne grafe, medtem ko librenms nadzoruje moje omrežje za dolgoročno


### Datadog + PagerDuty + Threat Stack

Uporabljamo Datadog (s PagerDuty) in Threat Stack in ne bi mogli biti bolj zadovoljni. Moja edina pritožba glede DD so razmeroma visoki stroški shranjevanja metrik.


### Zabbix

Zabbix s skripti po meri za nadzor skoraj vsega. Deluje kot po maslu.


### Outlyer

Uporabljam Outlyer, vendar moram razkriti, da tu delam, in uporaba lastnega izdelka (dog fooding) je obvezna.

Za izboljšavo še vedno potrebujem Graylog, Sentry in Statuscake.

Zveni pristransko, vendar bi po tem, ko sem z veseljem poganjal Nagios in druge sisteme za nadzor interno, v vsaki novi službi kupil gostovano rešitev in se rešil te muke.


### Nagios + Nagiosgraph

Za ves nadzor in opozarjanje poganjamo Nagios. Opozorila se zgodijo prek e-pošte (opozorila in kritična obvestila) in zvočnih obvestil aplikacije (za kritična opozorila).

Nagiosgraph se uporablja za vizualizacije.

Ta nastavitev je bila zelo učinkovita pri tem, da smo celovito obveščeni o dogajanju v našem okolju. Poganjamo in nadzorujemo približno 110 strežnikov, kritičnih za poslovanje, in približno 760 podatkovnih točk, ta sistem pa imamo vzpostavljen že več kot sedem let.

Rad bi nekoč tudi združil dnevnike z Graylog ali ELK.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager prek odličnega grafikona helm Prometheus Operator. Dnevniki še vedno gredo v načrt LogDNA birch, ker smo opazili, da je ELK pretežek za naših skromnih najmanj 3 in največ 5 vozlišč na GKE.


### DataDog + Sentry + PagerDuty.

Včasih sem poganjal vse svoje rešitve za nadzor z vsemi vrstami programske opreme, vključno z Nagios, Icinga, Zabbix, ELK, Greylog2, Influx in številnimi drugimi orodji, vendar je resnica, da je preveč truda vključenega v poganjanje lastne infrastrukture za nadzor, zlasti ko lahko drugim plačate tako nizke cene, da to storijo namesto vas!

Plačevanje drugih za poganjanje infrastrukture za nadzor moje stranke osvobaja, da se osredotočijo na poganjanje svojih platform namesto nadzora nadzora, kar pomeni, da vrednost, ki jo pridobijo iz stabilnosti svoje platforme, daleč presega vse stroške nadzora kot storitve.


### Sensu + Graphite + ELK

Moje podjetje zelo stavi na samostojno gostovane stvari.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager za opozarjanje; moja ekipa verjame, da je preprost nadzor dober nadzor.

Drugi sistemi, kot sta beleženje in sledenje, zagotavljajo bogat kontekst za diagnozo, ko dežurni prejme opozorilo, vendar na teh nikoli ne gradimo opozarjanja.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Storitve, opremljene s Prometheus => analitika in vizualizacija Circonus


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Uporabljamo spodnje storitve:

icinga2 za nadzor in VictorOps za opozarjanje

NewRelic za podroben nadzor storitve

Sentry za sledenje napakam v storitvi

Slack/e-pošta je del opozarjanja, ki se sproži iz NewRelic ali icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 z integracijo elasticsearch za analizo in integracijo graphite+grafana za grafe.

zahvaljujoč prilagodljivosti pravil apply v icinga2 razvijalci vidijo le storitve, za katere prejemajo obvestila.

in prek icinga2 director lahko programerji preprosto določijo lastna preverjanja (kar počnejo, vsakih nekaj dni – 100 preverjanj gre ven, 100 drugih preverjanj pride noter) v velikem obsegu brez težav.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Kaj imamo zdaj:

DataDog za metrike

New Relic za nadzor aplikacij

ELK (Elastic Search + Logstash + Kibana) za dnevnike

Sentry (samostojno gostovan) za beleženje izjem

E-pošta + Slack + VictorOps za opozarjanje (glede na resnost)

Kaj želimo imeti:

Prometheus za metrike (Grafana za vizualizacijo)

New Relic (verjetno Elastic Search APM) za nadzor aplikacij

EFK (elastic search + fluentd + kibana) za beleženje. Verjetno bo Loki podjetja Grafana do časa, ko pridemo do tja, pripravljen za produkcijo

Sentry za izjeme

Alertmanager + e-pošta + VictorOps za opozorila


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Razkritje: delam pri VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf za strežniške metrike, kot so CPU, disk, pomnilnik in omrežje. Telegraf uporabljamo tudi za nadzor SNMP naših omrežnih naprav.

Prometheus za aplikacijske metrike. V svojo aplikacijo vgradimo preverjanja zdravja, ki jih Prometheus zbira.

InfluxDB za shranjevanje časovnih vrst. Tja se pošiljajo podatki Telegraf.

Grafana za nadzorne plošče in opozorila. Mehanizem za opozarjanje ni zelo robusten, a opravi delo. Opozorila pošiljamo tudi v Slack.

Česar trenutno nimam, je centralizirana rešitev za beleženje. ELK je zmogljiv, a težak za postavitev in upravljanje, brezplačnih alternativ, ki bi bile dovolj blizu, da bi jih preučil, pa ne poznam.


### Sematext + Logagent + Experience

Sematext za metrike, za dnevnike, za sledi, kmalu tudi za nadzor resničnih uporabnikov. Po mojem mnenju preprostejše/cenejše kot uporaba N različnih orodij/storitev.

Za pošiljanje dnevnikov smo včasih uporabljali rsyslog, nato pa smo prešli na Logagent.

Za poročanje o sesutjih uporabniškega dela uporabljamo Sentry, vendar bomo kmalu prešli na Experience.

Razkritje: sem Sematextovec.


### Azure Monitor/Analytics + OpsGenie

Želim si, da bi imel Log Analytics boljši vmesnik. Odmikamo se od splunka, po katerem je bilo veliko lažje krmariti.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Res ne želite poganjati lastnega sistema obveščanja. Splunk lahko zamenjate z ELK, razen če vaša varnostna ekipa raje uporablja Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf kot zbiralnik, Prometheus + Alertmanager za nadzor in opozarjanje, integrirano s kanali Slack in pagerduty za kritična opozorila. Grafana za vizualizacijo metrik gostiteljev.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus za metrike + opozorila

Grafana za nadzorne plošče Prometheus

Cloudwatch nadzoruje instance Prometheus

sentry za sledenje izjemam

kibana + elasticsearch

graylog

prometheus Push Gateway za paketna opravila/cronjobs

SOP https://github.com/rapidloop/sop za „potiskanje/posredovanje“ metrik iz ene instance Prometheus v drugo

odjemalci uporabljajo odjemalce Prometheus. Na strani odjemalca poskušamo uporabljati opencensus.io


### PagerDuty + Monitis

PagerDuty + Monitis. Tudi nekaj Azure Functions po meri za testiranje zdravja nekaterih storitev.

Letos nameravam uvesti Prometheus in Grafana


### Prometheus + Grafana + Bosun

Prometheus za shranjevanje podatkov časovnih vrst. Grafana za vizualizacijo. Bosun za upravljanje opozoril.


### Azure Monitor/Analytics/Insights/Dashboards

Podjetje samo z Azure, Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana za nadzor storitev vsebnikov v Kubernetes prek Prometheus

Monitis za celovit nadzor storitev, predvsem za spletne API in spletne aplikacije

OpsGenie za upravljanje opozoril

Slack za prejemanje informacij o stanju naših sistemov


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Dolgoletni inženir (dev)ops. Zrasel sem na Nagios. Z veseljem bi slišal mnenja o mojem samofinanciranem SaaS https://checklyhq.com. Izvajamo nadzor API in nadzor transakcij na spletnem mestu s precej poglobljenim opozarjanjem.

Checkly sem začel, ker je bil aktivni/sintetični nadzor na področju API nekoliko omejen (in drag). Nadzor na podlagi brskalnika/skriptov je še bolj lastniški in drag. Uporabljamo Puppeteer in cene ohranjamo čim nižje.

Naš sklad za nadzor:

Checkly (dog fooding ...)

AppOptics (grafi po meri)

AWS Cloudwatch in SNS za sporočila SMS.

vgrajeno opozarjanje Heroku.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana nas v Slacku opozarja na težave z infrastrukturo ali poslabšanje zmogljivosti, logz.io pa smo konfigurirali tako, da opozarja v Slacku ob določenem obsegu dnevnikov na ravni napak iz aplikacijske plasti.


### SignalFX + Splunk + PagerDuty + Slack

Trenutno uporabljam: SignalFX, Splunk, PagerDuty in Slack. SignalFX mi ni všeč, čeprav je njihova podpora zelo prijazna in odzivna. Splunk mi je všeč (vreden je, če ga lahko plačate), prav tako PagerDuty in Slack.

Včasih sem uporabljal sklad TICK, kjer je bil večinoma C v resnici G, tj. Grafana, čeprav sem malo uporabljal tudi Chronograf. To je bilo odlično, vendar naporno za upravljanje. Klasična dilema SaaS ali samostojno gostovanje.

Uporabljal sem DataDog, New Relic, Graylog, ELK in BugSnag. DataDog in New Relic sta mi zelo všeč, Graylog je kar dober. ELK mi ni preveč všeč. BugSnag je lep; pravzaprav menim, da je sledenje napakam/izjemam v mnogih primerih kar dobra zamenjava za polni nadzor dnevnikov.


### ELK + Prometheus + Grafana

Tako kot drugi uporabljamo ELK za dnevnike in Prometheus+Grafana za vse ostalo.

Vzdrževanje te nastavitve je enostavno, če si dovolite, da občasno izgubite podatke. Na primer, če naša podatkovna baza ElasticSearch zaide v težave (kar se nam žal zgodi vsakih 2–3 mesece), se ne ukvarjamo z HA, temveč podatke zavržemo in gremo naprej. Če nujno potrebujete HA ali dolgoročno hrambo, srečno.


### Datadog + Prometheus + Grafana

Datadog sem nastavil mesec za mesecem, ker ko sem prišel sem, ni bilo nobenega nadzora in nobenega opozarjanja. Le nekaj naših spletnih mest je bilo nadzorovanih vsakih 5 minut glede delovanja. Datadog je brez dvoma najlažji za nastavitev. Ko bom rešil vse druge težave, bom prešel na Prometheus+Grafana. Glede upravljanja dnevnikov še nisem 100-odstotno odločen.

### Nagios + ELK

Podpiramo več kot 100 izdelkov.

Za lokalno (on-prem) je večinoma Nagios in ELK. Za oblak prehajamo z DataDog na NewRelic.


### Datadog ali Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Včasih smo uporabljali datadog, a smo ugotovili, da je za naše potrebe predrag. Ne razumite me narobe, je neverjeten, vendar ima ogromen strošek. Site24x7.com smo lahko nastavili z letno naročnino za približno 2–3 mesece stroškov DD.

Naš sklad za nadzor:

Site24x7 – APM, nadzor zunanjih URL, nadzor pretoka pošte SMTP, poteki SSL in nadzor procesov.

StatusCake – za nadzor URL in potrditev – je naša rezerva za primer, da bi site24x7 kaj spregledal (ne spregleda), vendar je SC prilagodljivejši za zunanji nadzor vrat in storitev za naše potrebe.

Obe orodji stopnjujeta v PagerDuty, nato pa stopnjevanja prejmemo v slacku.

SumoLogic – za nadzor dnevnikov (je odlično orodje, a nekoliko zapleteno za naše potrebe)

Iz slacka lahko opozorilo potrdimo ali odpravimo.

Nato imamo veliko avtomatizacij site24x7, ki se povezujejo s commando.io za »BedOps«, kot mu pravimo – ko se sproži opozorilo, zaženemo nekaj skriptov ali avtomatizacij kot poskus odprave stanja (99 % časa nas avtomatizacija + naši skripti obvarujejo pred težavami).

V svoji bazi znanja (KB) imamo notranje priročnike (runbooks) za primere, ko avtomatizacije odpovedo ali ko je treba popraviti nekaj, kar je zunaj obsega.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana za metrike v naših gručah GKE in VM.

Google Stackdriver za dnevnike (ker je vključen in privzeto aktiven ter trenutno zadošča našim potrebam).


### Zabbix

Zabbix za vse. Dodatna programska oprema ni potrebna.
