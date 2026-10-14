# Metrikák, monitorok, riasztások

Tartalom:

* [Összefoglaló](#összefoglaló)
  * [Probléma](#probléma)
  * [Döntés](#döntés)
  * [Állapot](#állapot)
* [Részletek](#részletek)
  * [Feltevések](#feltevések)
  * [Megszorítások](#megszorítások)
  * [Álláspontok](#álláspontok)
  * [Érv](#érv)
  * [Következmények](#következmények)
* [Kapcsolódó](#kapcsolódó)
  * [Kapcsolódó döntések](#kapcsolódó-döntések)
  * [Kapcsolódó követelmények](#kapcsolódó-követelmények)
  * [Kapcsolódó artefaktumok](#kapcsolódó-artefaktumok)
  * [Kapcsolódó alapelvek](#kapcsolódó-alapelvek)
* [Megjegyzések](#megjegyzések)
  * [Szabad szöveges üzenetek és strukturált eseményüzenetek](#szabad-szöveges-üzenetek-és-strukturált-eseményüzenetek)
  * [A Graylog könnyebb](#a-graylog-könnyebb)
  * [A Prometheus némi hangolást igényel](#a-prometheus-némi-hangolást-igényel)
  * [Az AWS-szolgáltatások vegyes élményt nyújtanak](#az-aws-szolgáltatások-vegyes-élményt-nyújtanak)
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


## Összefoglaló


### Probléma

Metrikákat, monitorokat és riasztásokat szeretnénk használni, mert tudni akarjuk, mennyire jól működnek az alkalmazásaink, és mikor van probléma.


### Döntés

Folyamatban (WIP).


### Állapot

Információgyűjtés. A lehetséges szélsőségekkel kezdünk: a leginkább ajánlott régebbi ingyenes eszközzel (Nagios) és a leginkább ajánlott újabb fizetős eszközzel (New Relic).


## Részletek


### Feltevések

Modern, gyors, megbízható, reszponzív stb. webalkalmazásokat szeretnénk létrehozni.

Vásárolni szeretnénk építés helyett.


### Megszorítások

Olyan eszközöket szeretnénk, amelyek jól működnek a devops-folyamatunkkal és a telepítési felhőinkkel.


### Álláspontok

Jelenleg kutatjuk az álláspontokat.


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

  
### Érv

Eddig a Nagios és a New Relic a spektrum két vége. A Nagios a legrégebbi, legegyszerűbb, ingyenes, járható eszköz. A New Relic a legújabb funkciójú, legteljesebb, fizetős, járható eszköz. Ezek értékelésével kezdünk. Szükség szerint mozdulunk majd a spektrum belseje felé.  

Eddig a Zabbixnak vannak a legjobb ajánlásai, és a legteljesebb képességeket is kínálja.

Eddig az ELK-nak van a legjobb népszerűsége a nyílt forráskódú, építés-vásárlás helyett megoldások között.

Eddig a Prometheus + Grafana népszerűsége a legjobb.


### Következmények

TODO.


## Kapcsolódó


### Kapcsolódó döntések

A választások befolyásolják a tesztelhetőséget, a telemetriát és valószínűleg más rendszereket, például az ügyfélszolgálatét, a webhelymegbízhatósági mérnökségét (SRE) stb.


### Kapcsolódó követelmények

TODO.


### Kapcsolódó artefaktumok

TODO.


### Kapcsolódó alapelvek

Könnyen visszafordítható.

A sebesség szükségessége.


## Megjegyzések


Egy elég jó nyílt forráskódú stack:

* Prometheus metrikákhoz és metrikákon alapuló riasztáshoz

* Grafana a metrikák megjelenítéséhez

* Elasticsearch/Logstash/Kibana (ELK) naplókhoz és strukturált eseményekhez

* Pushover mobilértesítésekhez


### Szabad szöveges üzenetek és strukturált eseményüzenetek

Szabad szöveges üzenetek: például az a fajta véletlenszerű dolog, amit a /var/log/messages-ben talál, és amit az alkalmazás szándékosan állít elő. Az üzenetek hasznosak a gépen zajló más dolgok azonosítására, mint a memóriahiány vagy hardverhibák, de sok szemét van bennük. 

Strukturált eseményüzenetek: az alkalmazás állítja elő, rögzített vagy dinamikus attribútumkészlettel, pl. HTTP-kérésnapló, könyvelési napló, felhasználói bejelentkezés.

Általában jó az egyes kérések részleteit úgy naplózni, hogy attribútumok alapján le lehessen fúrni. Így például egy userid vagy sessionid hozzáadása mindenhez lehetővé teszi a nyomkövetést. A kifejezett nyomkövetés (tracing) természetesen szintén jó. Az ELK használata erre afféle szegény ember https://www.honeycomb.io/ megoldása


### A Graylog könnyebb

A Graylog tapasztalatom szerint könnyebben üzembe helyezhető.



### A Prometheus némi hangolást igényel


Általában elégedett vagyok a Prometheusszal a metrikákhoz. A riasztás némi hangolást igényel, de elég jó. Az alkalmazástól függ. Úgy gondolom, a legjobb a végfelhasználó számára látható állapotokra riasztani, nem a mögöttes okokra. Például az oldalbetöltési idő jó, a másodpercenkénti kérések száma nem. Bár a nulla kérés másodpercenként azt jelzi, hogy valami nincs rendben.

A szolgáltatás előnye, hogy extra intelligenciát kínál dobozból kivéve. Általában kedvelem a Datadogot. A szolgáltatások ijesztően drágák lehetnek, ha sok adatod van, és néha olyan árazási modelljeik vannak, amelyek nem felhőbarátok, pl. példányonkénti díjazás, amikor a példányok dinamikusak. Különbség van aközött is, hogy a szolgáltatásokban minden kérés fizető felhasználótól jön, vagy hirdetéshez kapcsolódnak, így a kéréseknek csak egy kis százaléka hoz pénzt. Sok adatod lehet és nem túl nagy költségvetésed.

Olyan szolgáltatásokon dolgozom, amelyek naponta 1 milliárd kérést kapnak, ezért van értelme a saját monitorozás és naplózás üzemeltetésének. Ha a mennyiségeid kisebbek, a hosztolt szolgáltatások könnyebbek.


### Az AWS-szolgáltatások vegyes élményt nyújtanak

Az AWS-szolgáltatásokkal kapcsolatos tapasztalataim vegyesek. Az Elasticsearch-szolgáltatásuk megbízhatatlan volt, ezért saját példányokat futtatunk. A CloudWatch-metrikák drágák, ezért általában csak „infrastruktúra” szintű metrikákhoz használjuk őket, nem az alkalmazáséhoz, azaz egészséggel kapcsolatos metrikákhoz, ahol az AWS jobban tudhatja, mi történik, mint a példányon futó szoftver. A CloudWatch Logs lassan frissülhet, és nincs sok metaadata. Az ELK futtatása segít ebben. Ha tényleg valós idejű adatot akarok, a Kafka naplószállítóként jobb. Ezt a Logstash elég jól támogatja. Egy Kafka-fürt kezelése azonban nem gyenge idegzetűeknek való, sok szabadon lévő csővezeték van.


### Kafka

Megjegyzés: A Kafka időnként szuperfurcsa lehet, vagy lehet sziklaszilárd, és szinte elfelejted, hogy ott van, és mindent összeköt. 


Megjegyzés: A Kafka szilárd volt, de meglepően sok munka volt beüzemelni. Úgy gondolok rá, mint egy relációs adatbázisra, de ahol csak a „fizikai” rétegen dolgozol, pl. táblaterek, fájlok és partíciók. Voltak korai időszakok, amikor hiányoztak a kezelőeszközök, és programokat kellett írnunk pl. egy fogyasztói csoport visszaállítására. http://howfuckedismydatabase.com/nosql/

Megjegyzés: A Kafkát „pufferként” használjuk naplóüzenetekhez, és helyként, ahol valós idejű adatfolyam-feldolgozást végezhetünk több kiszolgálóról érkező adatokon. Ha DDOS-támadást kapunk, szükségünk van egy módra az adatok elemzésére több példányon keresztül. Ha közvetlenül a kiszolgálókról naplózunk az ELK-ba, a terhelés felrobbanthatja az Elasticsearch-fürtöt.

Megjegyzés: A Kafka azért jó nekünk, mert ha DDOS-támadást kapunk, szükségünk van egy módra az adatok elemzésére több példányon keresztül. Ha közvetlenül a kiszolgálókról naplózunk az ELK-ba, a terhelés felrobbanthatja az Elasticsearch-fürtöt.


Megjegyzés: A Kafka kevesebb munkát végez és hatékonyabb, így jobban elbírja a terhelést. És a Kafka munkáját sorba állítjuk és újrapróbáljuk. És az, hogy a Kafka túlterhelt, nem érinti azokat a felhasználókat, akik interaktívan próbálnak dolgozni a Kibanával, ahogy tenné, ha az Elasticsearch küszködne.

Megjegyzés:  Az adatfolyam-feldolgozás többnyire visszaélések keresése, pl. túl sok forgalom egyetlen IP-ről az egész fürtben, majd a tiltás megosztása az egész fürtben.

Megjegyzés: A logstash-output-kafka bővítmény jelenleg elég megbízhatatlan. Megharaptak a GitHub issues oldalán lévő számos problémája, amelyeket úgy tűnik, soha nem javítanak. El akarok állni a használatától, és közvetlenül az alkalmazásainkból küldeni a Kafkának.

Megjegyzés: Most strukturált eseményeket küldünk közvetlenül az alkalmazásból a Kafkának. A fő motiváció az volt, hogy kevesebbszer érjünk hozzá a naplóadatokhoz, és elkerüljük a lemez többszöri olvasását és írását. Nagy forgalmú rendszerekben a naplózás több munkát igényelhet, mint maga az alkalmazás. Azon gondolkodom, hogy a journald is közvetlenül küldje a naplókat, egy C programból.


### Loki

Tartsd szemmel a Lokit. Még nem kész, de ha az lesz, azt várom, hogy jobban illeszkedik ebbe a stackbe. A Loki a Grafana Labs által létrehozott naplóaggregátor, a Prometheushoz hasonló gyűjtési és címkeszintaxist használ.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager metrikákhoz. <3 Prometheus.

Rollbar/Graylog naplózáshoz/hibajelentéshez (van itt némi átfedés; egy kis szolgáltatásnak valószínűleg nincs szüksége mindkettőre).

Jelenleg a riasztások csak néhány Slack-csatorna egyikére mennek, amelyeken az érdekelt felek bekapcsolták az értesítéseket. Ha komolyabban vennénk az ügyeletet (on-call), a PagerDuty/VictorOps stb. felé mennének.

Grafana grafikonokhoz és irányítópultokhoz. Lelkesen várom azt is, hogy a közelgő naplózási lehetőségeik feleslegessé teszik-e a Graylogot.


### Thanos

A Thanost használjuk előtérként a HA-beállításunkhoz. Tudja deduplikálni a HA-párokat.

Jelenleg 6 hónapnyi helyi Prometheus-adatot tartunk. Ez elég jól működik nekünk. De épp a Thanos-beállításunkba építem a bucket-tárolást a hosszú távú adattároláshoz. Elméletileg a GCS-tárolás körülbelül 30%-kal olcsóbb lesz, mint a GCE standard tartós lemez, amelyet most használunk.

Jelenleg nem készítünk biztonsági másolatot a Prometheus-adatokról. Az adatok egyszerűen nem igazán fontosak számunkra a riasztáshoz szükséges mennyiségen túl. Az általános flottatelepítésünk annyit változik évről évre, hogy a néhány hónapnál régebbi múltbeli adatok nem igazán érdekesek. Érdekes lehet néhány alapstatisztika évről évre; felállíthatok egy alapstatisztikai rögzítési szabályrendszert, és tárolhatom Federationnel, vagy egyszerűen hagyom, hogy a Thanos gondoskodjon róla.

EDIT: Kisebb nyilatkozat: a Prometheus fejlesztője vagyok.


### Prometheus HA

A HA a Prometheusban másolással történik — több gyűjtőpéldányt futtatsz, és vannak módok többet lekérdezni és deduplikálni az adatokat

A skálázás a hálózat felosztásával történik, és különböző Prometheusok kérdezik le a hálózat különböző részeit

A hosszú távú tárolás nem a Prometheus erőssége, hanem olyasmire hárul, mint az Influx vagy a timescaledb (amely technikailag a HA-pipát is kipipálja) cikk, amit erről olvastam https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

A hosszú távú dolgokat még nem próbáltam, mert még csak kísérletezem, és rövid távú grafikonokhoz használom, míg a librenms hosszú távon figyeli a hálózatomat


###  Datadog + PagerDuty + Threat Stack

Datadogot (PagerDutyval) és Threat Stacket használunk, és nem is lehetnénk elégedettebbek. Az egyetlen panaszom a DD-vel a metrikatárolás viszonylag magas költsége.


### Zabbix

Zabbix egyedi szkriptekkel szinte mindenhez. Remekül működik.


### Outlyer

Az Outlyert használom, de nyilatkoznom kell, hogy itt dolgozom, és a saját termék használata kötelező.

Még mindig szükségem van Graylogra, Sentryre és Statuscake-re a kiegészítéshez.

Elfogultan hangzik, de miután örömmel futtattam Nagiost és más monitorozórendszereket belsőleg, minden új helyen hosztolt megoldást vennék, és megszabadulnék ettől a fájdalomtól.


### Nagios + Nagiosgraph

A Nagiost futtatjuk az összes monitorozáshoz és riasztáshoz. A riasztások e-mailen (figyelmeztetések és kritikus értesítések) és hallható alkalmazásértesítéseken (kritikus riasztásokhoz) keresztül történnek.

A Nagiosgraphot vizualizációkhoz használjuk.

Ez a beállítás nagyon hatékony volt abban, hogy átfogóan tájékozottak legyünk a környezetünkben zajló eseményekről. Körülbelül 110 küldetéskritikus kiszolgálót és körülbelül 760 adatpontot futtatunk és figyelünk, és több mint hét éve működik nálunk ez a rendszer.

Szeretném is valamikor aggregálni a naplókat Graylog vagy ELK segítségével.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager a remek Prometheus Operator helm charton keresztül. A naplók továbbra is a LogDNA birch tervhez mennek, mert észrevettük, hogy az ELK túl nehéz a szerény, minimum 3 és maximum 5 csomópontos fürtünkhöz a GKE-n.


### DataDog + Sentry + PagerDuty.

Régebben minden saját monitorozási megoldásomat magam futtattam, mindenféle szoftverrel, többek között Nagios, Icinga, Zabbix, ELK, Greylog2, Influx és sok más eszközzel, de az igazság az, hogy túl sok erőfeszítés a saját monitorozási infrastruktúrát futtatni, különösen, amikor annyira alacsony díjakért fizethetsz valaki másnak, hogy megcsinálja helyetted!

Ha másoknak fizetek a monitorozási infrastruktúra futtatásáért, az ügyfeleim felszabadulnak, hogy a platformjaik futtatására összpontosítsanak a monitorozás monitorozása helyett, ami azt jelenti, hogy a platformjuk stabilitásából nyert érték messze meghaladja a Monitorozás mint szolgáltatás bármely költségét.


### Sensu + Graphite + ELK

A cégem nagyon rá van állva a saját üzemeltetésű dolgokra.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager riasztáshoz, a csapatom úgy hiszi, hogy az egyszerű monitorozás jó monitorozás.

Más rendszerek, mint a naplózás és a nyomkövetés, gazdag kontextust adnak a diagnózishoz, amikor az ügyeletes riasztást kap, de ezekre soha nem építünk riasztást.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Prometheusszal műszerezett szolgáltatások => Circonus-elemzés és vizualizáció


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Az alábbi szolgáltatásokat használjuk:

icinga2 a monitorozáshoz és VictorOps a riasztáshoz

NewRelic a szolgáltatás részletes monitorozásához

Sentry a hibakövetéshez a szolgáltatásban

A Slack/e-mail a riasztás része, amelyet a NewRelic vagy az icinga2 vált ki


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 elasticsearch-integrációval az elemzéshez és graphite+grafana integrációval a grafikonokhoz.

az icinga2 apply-szabályainak rugalmasságának köszönhetően a fejlesztők csak azokat a szolgáltatásokat látják, amelyekről értesítést kapnak.

és az icinga2 directoron keresztül a programozók könnyen definiálhatják saját ellenőrzéseiket (amit meg is tesznek, néhány naponta — 100 ellenőrzés ki, 100 másik be) nagy léptékben, gond nélkül.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Mink van most:

DataDog metrikákhoz

New Relic alkalmazásmonitorozáshoz

ELK (Elastic Search + Logstash + Kibana) a naplókhoz

Sentry (saját üzemeltetésű) kivételek naplózásához

E-mailek + Slack + VictorOps riasztáshoz (súlyosság alapján)

Mit szeretnénk:

Prometheus metrikákhoz (Grafana a vizualizációhoz)

New Relic (valószínűleg Elastic Search APM) az alkalmazásmonitorozáshoz

EFK (elastic search + fluentd + kibana) naplózáshoz. Valószínűleg a Grafana Lokija éles használatra kész lesz, mire idáig eljutunk

Sentry a kivételekhez

Alertmanager + e-mail + VictorOps a riasztásokhoz


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Nyilatkozat: a VMware-nél dolgozom)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf kiszolgálómetrikákhoz, mint a CPU, lemez, memória és hálózat. A Telegrafot a hálózati eszközeink SNMP-monitorozásához is használjuk.

Prometheus alkalmazásmetrikákhoz. Egészségellenőrzéseket kódolunk az alkalmazásunkba, amelyeket a Prometheus lekaparja.

InfluxDB idősor-tároláshoz. Ide kerülnek a Telegraf adatai.

Grafana irányítópultokhoz és riasztásokhoz. A riasztómotor nem szuperrobusztus, de elvégzi a dolgát. A riasztásokat Slackbe is küldjük.

Amim jelenleg nincs, az egy központosított naplózási megoldás. Az ELK erőteljes, de nehéz beállítani és kezelni, és nem ismerek elég közeli ingyenes alternatívákat, hogy megnézzem őket.


### Sematext + Logagent + Experience

Sematext metrikákhoz, naplókhoz, nyomokhoz, hamarosan valós felhasználói monitorozáshoz is. Egyszerűbb/olcsóbb, mint N különböző eszköz/szolgáltatás használata, szerény véleményem szerint.

A naplók szállításához régebben rsyslogot használtunk, aztán átváltottunk Logagentre.

A front-end összeomlásjelentéshez Sentryt használunk, de hamarosan átváltunk Experience-re.

Nyilatkozat: Sematextan (Sematext-alkalmazott) vagyok.


### Azure Monitor/Analytics + OpsGenie

Bárcsak a Log Analytics jobb felülettel rendelkezne. Elmegyünk a Splunktól, amelyben sokkal könnyebb volt navigálni.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Tényleg nem akarod a saját értesítőrendszeredet futtatni. A Splunkot lecserélheted ELK-ra, hacsak a biztonsági csapatod nem a Splunkot részesíti előnyben.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf gyűjtőként, Prometheus + Alertmanager monitorozáshoz és riasztáshoz, integrálva slack-csatornákkal és pagerdutyval a kritikus riasztásokhoz. Grafana a gazdagép-metrikák vizualizációjához.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus metrikákhoz + riasztásokhoz

Grafana a Prometheus-irányítópultokhoz

Cloudwatch a Prometheus-példányok monitorozásához

sentry a kivételkövetéshez

kibana + elasticsearch

graylog

prometheus Push Gateway a batch/cronjobokhoz

SOP https://github.com/rapidloop/sop a metrikák „továbbítására/továbbküldésére“ egyik Prometheus-példányról a másikra

a kliensek a Prometheus-klienseket használják. Megpróbáljuk használni az opencensus.io-t a kliensoldalon


### PagerDuty + Monitis

PagerDuty + Monitis. Plusz néhány egyedi Azure Functions egyes szolgáltatások állapotának tesztelésére.

Idén tervezzük bevezetni a Prometheust és a Grafanát


### Prometheus + Grafana + Bosun

Prometheus az idősoros adatok tárolásához. Grafana a vizualizációhoz. Bosun a riasztáskezeléshez.


### Azure Monitor/Analytics/Insights/Dashboards

Csak Azure-t használó cég: Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana a Kubernetesben futó konténerszolgáltatások monitorozásához Prometheuson keresztül

Monitis a végpontok közötti szolgáltatásmonitorozáshoz, főként webes API-khoz és webalkalmazásokhoz

OpsGenie a riasztáskezeléshez

Slack a rendszereinktől érkező állapotinformációk fogadásához


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Régi (dev)ops mérnök vagyok. A Nagioson nőttem fel. Szívesen hallanék véleményeket a bootstrapped SaaS-omról https://checklyhq.com. API-monitorozást és webhelytranzakció-monitorozást végzünk meglehetősen mélyre menő riasztással.

Azért kezdtem a Checklyt, mert az aktív / szintetikus monitorozás az API-k terén kissé korlátozott (és drága) volt. A böngészőalapú / szkriptelt monitorozás még zártabb és drágább. Puppeteert használunk, és az árakat a lehető legalacsonyabban tartjuk.

A monitorozási stackünk:

Checkly (a saját kutyaeledelünket esszük...)

AppOptics (egyedi grafikonok)

AWS Cloudwatch és SNS SMS-üzenetekhez.

beépített Heroku-riasztás.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Az Instana slacken értesít minket infrastruktúra-problémákról vagy teljesítményromlásról, a logz.io-t pedig úgy állítottuk be, hogy slacken riasszon az alkalmazásrétegből érkező hibaszintű naplók bizonyos mennyiségénél.


### SignalFX + Splunk + PagerDuty + Slack

Jelenleg használjuk: SignalFX, Splunk, PagerDuty és Slack. Nem vagyok nagy rajongója a SignalFX-nek, bár a támogatási csapatuk szuperbarátságos és gyorsan reagál. Szeretem a Splunkot (megéri, ha megengedheted magadnak), a PagerDutyt és a Slacket.

Régebben a TICK stacket használtam, ahol a C legnagyobb része valójában G volt, vagyis Grafana, bár kicsit a Chronografot is használtam. Fantasztikus volt, de fájdalmas volt kezelni. A klasszikus SaaS kontra saját üzemeltetés dilemma.

Használtam DataDogot, New Relicet, Graylogot, ELK-t és BugSnagot. Nagyon szeretem a DataDogot és a New Relicet, a Graylog elég jó. Az ELK-nak nem vagyok nagy rajongója. A BugSnag szép, valójában úgy érzem, hogy a hibák/kivételek követése sok esetben elég jó helyettesítője a teljes naplómonitorozásnak.


### ELK + Prometheus + Grafana

Mint mások, mi is ELK-t használunk naplókhoz, és Prometheus+Grafanát mindenhez máshoz.

E beállítás karbantartása könnyű, ha megengeded magadnak, hogy alkalmanként adatot veszíts. Például ha az ElasticSearch adatbázisunk rossz passzba kerül (ami nekünk sajnos 2–3 havonta megtörténik), nem foglalkozunk a HA-val, hanem kidobjuk az adatokat, és élünk tovább. Ha mindenképpen HA-ra vagy hosszú távú megőrzésre van szükséged, sok szerencsét.


### Datadog + Prometheus + Grafana

A Datadogot havi alapon állítottam be, mert amikor ideértem, nem volt monitorozás és riasztás. Csak néhány oldalunkat figyelték 5 percenként az elérhetőségre. A Datadogot nagy különbséggel a legkönnyebb beállítani. Amikor befejezem az összes többi probléma kezelését, átváltok Prometheus+Grafanára. A naplókezelésben még nem vagyok 100%-ig biztos.

### Nagios + ELK

Több mint 100 terméket támogatunk.

On-prem többnyire Nagios és ELK. A felhőben a DataDogról a NewRelicre költözünk.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Régebben datadogot használtunk, de túl drágának találtuk az igényeinkhez. Ne értsetek félre, csodálatos, de óriási költsége van. Sikerült beállítanunk a site24x7.com-ot éves előfizetéssel a DD költségének körülbelül 2–3 havi összegéért.

A monitorozási stackünk:

Site24x7 - APM, külső URL-monitorozás, SMTP-levélforgalom-monitorozás, ssl-lejáratok és folyamatmonitorozás.

StatusCake - URL-monitorozáshoz és megerősítéshez - ez a tartalékunk arra az esetre, ha a site24x7 kihagyna valamit (nem hagy ki), de az SC rugalmasabb a külső port- és szolgáltatásmonitorozáshoz az igényeinkre.

Mindkét eszköz a PagerDutyhoz eszkalál, aztán slacken kapjuk az eszkalációkat.

SumoLogic - naplómonitorozáshoz (nagyszerű eszköz, de egy kicsit bonyolult az igényeinkhez)

A slackből nyugtázhatjuk vagy elháríthatjuk a riasztást.

Aztán sok site24x7-automatizálásunk van, amelyek a commando.io-hoz kapcsolódnak a „BedOps”-hoz, ahogy mi nevezzük — ahol riasztás váltódik ki, elindítunk néhány szkriptet vagy automatizálást a helyzet orvoslására (az esetek 99%-ában az automatizálás + a szkriptjeink távol tartanak a bajtól).

Belső runbookjaink vannak a tudásbázisunkban arra az esetre, ha az automaták kudarcot vallanak, vagy ha valami hatókörön kívüli dolgot kell javítani.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana metrikákhoz a GKE-fürtjeinkben és virtuális gépeinken.

Google Stackdriver naplókhoz (mivel benne van és alapértelmezésben aktív, és jelenleg elég az igényeinkre).


### Zabbix

Zabbix mindenre. Nincs szükség további szoftverre.


