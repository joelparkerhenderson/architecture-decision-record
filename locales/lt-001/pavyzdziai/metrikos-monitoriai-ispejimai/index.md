# Metrikos, monitoriai, įspėjimai

Turinys:

* [Santrauka](#santrauka)
  * [Problema](#problema)
  * [Sprendimas](#sprendimas)
  * [Būsena](#būsena)
* [Detalės](#detalės)
  * [Prielaidos](#prielaidos)
  * [Apribojimai](#apribojimai)
  * [Pozicijos](#pozicijos)
  * [Argumentas](#argumentas)
  * [Implikacijos](#implikacijos)
* [Susiję](#susiję)
  * [Susiję sprendimai](#susiję-sprendimai)
  * [Susiję reikalavimai](#susiję-reikalavimai)
  * [Susiję artefaktai](#susiję-artefaktai)
  * [Susiję principai](#susiję-principai)
* [Pastabos](#pastabos)
  * [Laisvos formos tekstiniai pranešimai ir struktūrizuoti įvykių pranešimai](#laisvos-formos-tekstiniai-pranešimai-ir-struktūrizuoti-įvykių-pranešimai)
  * [Graylog yra lengvesnis](#graylog-yra-lengvesnis)
  * [Prometheus reikia šiek tiek derinimo](#prometheus-reikia-šiek-tiek-derinimo)
  * [AWS paslaugos yra nevienodos](#aws-paslaugos-yra-nevienodos)
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
  * [Datadog ar Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack](#datadog-ar-site24x7--statuscake--pagerduty--sumologic--slack)
  * [Prometheus + AlertManager + Grafana + Stackdriver](#prometheus--alertmanager--grafana--stackdriver)
  * [Zabbix](#zabbix-1)


## Santrauka


### Problema

Norime naudoti metrikas, monitorius ir įspėjimus, nes norime žinoti, kaip gerai veikia mūsų programos, ir žinoti, kada iškyla problema.


### Sprendimas

Darbas vykdomas (WIP).


### Būsena

Renkame informaciją. Pradedame nuo tikėtinų spektro galų: labiausiai rekomenduojamo senesnio nemokamo įrankio (Nagios) ir labiausiai rekomenduojamo naujesnio mokamo įrankio (New Relic).


## Detalės


### Prielaidos

Norime kurti šiuolaikines, greitas, patikimas, prisitaikančias ir pan. interneto programas.

Norime pirkti, o ne kurti.


### Apribojimai

Norime įrankių, kurie gerai veiktų su mūsų devops konvejeriu ir mūsų diegimo debesimis.


### Pozicijos

Dabar tiriame pozicijas.


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

  
### Argumentas

Kol kas Nagios ir New Relic yra spektro galai. Nagios yra seniausias, paprasčiausias, nemokamas, gyvybingas įrankis. New Relic yra naujausių funkcijų, išsamiausias, mokamas, gyvybingas įrankis. Pradėsime nuo jų vertinimo. Prireikus pereisime prie spektro vidurio.  

Kol kas Zabbix turi geriausias rekomendacijas ir taip pat siūlo išsamiausias galimybes.

Kol kas ELK turi didžiausią atvirojo kodo „kurti, o ne pirkti“ populiarumą.

Kol kas Prometheus + Graphana turi didžiausią populiarumą.


### Implikacijos

Reikia padaryti (TODO).


## Susiję


### Susiję sprendimai

Pasirinkimai paveiks testuojamumą, telemetriją ir tikriausiai kitas sistemas, pavyzdžiui, klientų aptarnavimo, svetainių patikimumo inžinerijos ir kt.


### Susiję reikalavimai

Reikia padaryti (TODO).


### Susiję artefaktai

Reikia padaryti (TODO).


### Susiję principai

Lengvai atšaukiama.

Greičio poreikis.


## Pastabos


Gana gera atvirojo kodo paketo sudėtis:

* Prometheus metrikoms ir įspėjimams pagal metrikas

* Grafana metrikoms rodyti

* Elasticsearch/Logstash/Kibana (ELK) žurnalams ir struktūrizuotiems įvykiams

* Pushover pranešimams mobiliuosiuose įrenginiuose


### Laisvos formos tekstiniai pranešimai ir struktūrizuoti įvykių pranešimai

Laisvos formos tekstiniai pranešimai: pavyzdžiui, tokie atsitiktiniai dalykai, kuriuos rastumėte /var/log/messages, ir tai, ką programa sugeneruoja tyčia. Pranešimai naudingi kitiems kompiuteryje vykstantiems dalykams, pavyzdžiui, atminties trūkumui ar aparatinės įrangos klaidoms, nustatyti, bet juose daug šlamšto. 

Struktūrizuoti įvykių pranešimai: programos sugeneruoti, su fiksuotu arba dinamišku atributų rinkiniu, pvz., HTTP užklausų žurnalas, apskaitos žurnalas, naudotojo prisijungimas.

Apskritai kalbant, gera registruoti kiekvienos užklausos detales taip, kad galėtumėte gilintis pagal atributus. Todėl, pavyzdžiui, pridėjus naudotojo ID arba sesijos ID prie visko, galima atsekti. Aiški sekimo (angl. tracing) priemonė, žinoma, taip pat gera. ELK naudojimas tam yra tarsi vargšo žmogaus https://www.honeycomb.io/


### Graylog yra lengvesnis

Iš mano patirties Graylog lengviau paleisti.



### Prometheus reikia šiek tiek derinimo


Apskritai esu patenkintas Prometheus metrikoms. Įspėjimams reikia šiek tiek derinimo, bet jie gana geri. Tai priklauso nuo jūsų programos. Manau, geriausia įspėti apie galutiniam naudotojui matomas sąlygas, o ne apie pagrindines priežastis. Pavyzdžiui, puslapio įkėlimo laikas yra gera metrika, o užklausų per sekundę skaičius – ne. Nors nulis užklausų per sekundę rodo, kad kažkas negerai.

Paslaugos pranašumas yra tas, kad jos iškart siūlo papildomą intelektą. Man apskritai patinka Datadog. Paslaugos gali būti bauginančiai brangios, jei turite daug duomenų, ir kartais turi kainodaros modelius, kurie nėra palankūs debesijai, pvz., apmokestinimas už egzempliorių, kai egzemplioriai yra dinamiški. Taip pat yra skirtumas tarp paslaugų, kuriose kiekviena užklausa yra iš mokančio naudotojo, ir tų, kurios susijusios su reklama, todėl tik nedidelis užklausų procentas uždirba pinigų. Galite sulaukti daug duomenų ir nedidelio biudžeto.

Dirbu prie kai kurių paslaugų, gaunančių 1 mlrd. užklausų per dieną, todėl prasminga patiems talpinti stebėseną ir žurnalus. Jei jūsų apimtys mažesnės, talpinamos paslaugos yra lengvesnės.


### AWS paslaugos yra nevienodos

Mano patirtis su AWS paslaugomis nevienoda. Jų Elasticsearch paslauga buvo nepatikima, todėl tam naudojame savo egzempliorius. CloudWatch metrikos yra brangios, todėl jas paprastai naudojame tik „infrastruktūros“ lygio metrikoms, o ne programai, t. y. su sveikata susijusioms metrikoms, kai AWS gali geriau žinoti, kas vyksta, nei egzemplioriuje veikianti programinė įranga. CloudWatch Logs gali lėtai atsinaujinti ir neturi daug metaduomenų. ELK naudojimas tai padeda išspręsti. Jei tikrai noriu realiojo laiko duomenų, geriau žurnalų transportui naudoti Kafka. Tai gana gerai palaiko Logstash. Tačiau Kafka klasterio valdymas nėra silpnanerviams, nes yra daug atviros instaliacijos.


### Kafka

Komentaras: Kafka kartais gali būti labai sudėtinga, o kartais Kafka gali būti tvirta kaip uola ir beveik pamirštate, kad ji ten yra ir viską jungia. 


Komentaras: Kafka buvo patikima, bet jos paleidimas pareikalavo stebėtinai daug darbo. Aš ją suprantu kaip reliacinę duomenų bazę, bet dirbi tik „fiziniame“ sluoksnyje, pvz., lentelių erdvėse, failuose ir skaidiniuose. Pradžioje kartais trūko valdymo įrankių, ir turėjome rašyti programas, pvz., vartotojų grupei iš naujo nustatyti. http://howfuckedismydatabase.com/nosql/

Komentaras: Kafka naudojame kaip žurnalo pranešimų „buferį“ ir vietą, kur galime atlikti realaus laiko srauto apdorojimą duomenims, ateinantiems iš kelių serverių. Jei sulaukiame DDOS atakos, mums reikia būdo analizuoti duomenis keliuose egzemplioriuose. Jei registruojame tiesiai iš serverių į ELK, apkrova gali sugadinti Elasticsearch klasterį.

Komentaras: Kafka mums gera, nes jei sulaukiame DDOS atakos, mums reikia būdo analizuoti duomenis keliuose egzemplioriuose. Jei registruojame tiesiai iš serverių į ELK, apkrova gali sugadinti Elasticsearch klasterį.


Komentaras: Kafka atlieka mažiau darbo ir yra efektyvesnė, todėl geriau susidoroja su apkrova. O Kafka darbą statome į eilę ir kartojame. O tai, kad Kafka perkrauta, neveikia naudotojų, bandančių dirbti interaktyviai su Kibana, taip, kaip veiktų, jei Elasticsearch vargtų.

Komentaras:  Srauto apdorojimas daugiausia ieško piktnaudžiavimo, pvz., per daug srauto iš vieno IP visame klasteryje, o tada dalijamasi blokavimu visame klasteryje.

Komentaras: Tačiau logstash-output-kafka papildinys šiuo metu yra gana nepatikimas. Mane apkandžiojo keletas jo GitHub problemų puslapyje esančių problemų, kurios, atrodo, niekada nebus ištaisytos. Noriu nustoti jį naudoti ir siųsti tiesiai iš savo programų į Kafka.

Komentaras: Dabar siunčiame struktūrizuotus įvykius tiesiai iš programos į Kafka. Pagrindinė motyvacija buvo mažiau kartų liesti žurnalo duomenis ir išvengti kelių disko skaitymo bei rašymo veiksmų. Didelės apimties sistemose registravimas gali reikalauti daugiau darbo nei pati programa. Galvoju padaryti, kad journald taip pat siųstų žurnalus tiesiogiai, iš C programos.


### Loki

Atidžiai stebėkite Loki. Jis dar nėra paruoštas, bet kai bus, tikėčiausi, kad jis geriau tiks šiame pakete. Loki yra žurnalų kaupiklis, sukurtas grafana labs; jis naudoja panašų į Prometheus rinkimo ir žymų sintaksę.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager metrikoms. <3 Prometheus.

Rollbar/Graylog žurnalų registravimui / klaidų pranešimui (čia yra šiek tiek sutapimo; maža paslauga tikriausiai nereikalauja abiejų).

Šiuo metu įspėjimai tiesiog siunčiami į vieną iš kelių Slack kanalų, kuriuose suinteresuotos šalys yra įjungusios pranešimus. Jei labiau rimtai vertintume budėjimą, jie eitų į PagerDuty/VictorOps/ir pan.

Grafana grafikams ir skydeliams. Taip pat nekantriai laukiu, ar jų būsimos žurnalų registravimo galimybės pakeis Graylog.


### Thanos

Thanos naudojame kaip HA sąrankos priekinę dalį. Jis moka pašalinti HA porų dubliavimą.

Šiuo metu saugome 6 mėnesius vietinių Prometheus duomenų. Tai mums veikia pakankamai gerai. Tačiau kaip tik diegiu saugojimą kibiruose (angl. bucket storage) savo Thanos sąrankoje ilgalaikiam duomenų saugojimui. Teoriškai GCS saugojimas bus apie 30 % pigesnis nei GCE standartinis nuolatinis diskas, kurį naudojame dabar.

Šiuo metu nekuriame Prometheus duomenų atsarginių kopijų. Duomenys mums iš tikrųjų nėra svarbūs, išskyrus tiek, kiek reikia įspėjimams. Mūsų bendras parko diegimas taip pasikeičia kasmet, kad istoriniai duomenys, senesni nei keli mėnesiai, tiesiog nėra labai įdomūs. Gali būti įdomu turėti keletą pagrindinių statistikų metai iš metų, galbūt sukonfigūruosiu pagrindinės statistikos įrašymo taisyklių rinkinį ir saugosiu juos su Federation arba tiesiog leisiu Thanos tuo pasirūpinti.

REDAGAVIMAS: smulkus atsakomybės apribojimas – esu Prometheus programuotojas.


### Prometheus HA

HA Prometheus daromas dubliuojant – paleidžiate kelis rinkėjus, yra būdų apklausti kelis ir pašalinti duomenų dubliavimą

Mastelis keičiamas nusprendžiant dėl tinklo ir leidžiant skirtingiems Prometheus apklausti skirtingas tinklo dalis

Ilgalaikis saugojimas nėra Prometheus stiprybė, bet perkeliamas į tokius dalykus kaip influx ar timescaledb (kuris techniškai taip pat atitinka HA varnelę), straipsnis, kurį apie tai skaičiau: https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Ilgalaikių dalykų dar nebandžiau, nes vis dar tik eksperimentuoju ir naudoju jį trumpalaikiams grafikams, kol librenms stebi mano tinklą ilgalaikiui laikotarpiui


###  Datadog + PagerDuty + Threat Stack

Naudojame Datadog (su PagerDuty) ir Threat Stack ir negalėtume būti laimingesni. Vienintelis mano priekaištas DD yra gana didelė metrikų saugojimo kaina.


### Zabbix

Zabbix su pasirinktiniais scenarijais stebi beveik viską. Veikia kaip laikrodis.


### Outlyer

Naudoju Outlyer, bet turiu pareikšti atsakomybės apribojimą – čia dirbu, o savo produkto naudojimas (angl. dog fooding) yra būtinas.

Vis tiek reikia Graylog, Sentry ir Statuscake papildymui.

Skamba šališkai, bet, būdamas patenkintas Nagios ir kitų stebėsenos sistemų paleidimu viduje, bet kuriame naujame darbe pirkčiau talpinamą sprendimą ir atsikratyčiau to skausmo.


### Nagios + Nagiosgraph

Visai stebėsenai ir įspėjimams naudojame Nagios. Įspėjimai siunčiami el. paštu (įspėjimai ir kritiniai pranešimai) ir garsiniais programos pranešimais (kritiniams įspėjimams).

Nagiosgraph naudojamas vizualizacijoms.

Ši sąranka buvo labai veiksminga išsamiai informuojant mus apie tai, kas vyksta mūsų aplinkoje. Valdome ir stebime apie 110 kritinių serverių ir apie 760 duomenų taškų, o šią rytinę sistemą naudojame daugiau nei septynerius metus.

Taip pat norėčiau kada nors kaupti žurnalus su Graylog arba ELK.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager per nuostabų Prometheus Operator helm diagramą (angl. chart). Žurnalai vis dar eina į LogDNA birch planą, nes pastebėjome, kad ELK per sunkus mūsų kuklioms min. 3, maks. 5 mazgų GKE.


### DataDog + Sentry + PagerDuty.

Anksčiau pats valdydavau visus savo stebėsenos sprendimus naudodamas įvairią programinę įrangą, įskaitant Nagios, Icinga, Zabbix, ELK, Greylog2, Influx ir daugybę kitų įrankių, bet tiesa ta, kad savo stebėsenos infrastruktūros valdymas reikalauja per daug pastangų, ypač kai galite sumokėti kitam tokius mažus tarifus, kad jis tai padarytų už jus!

Mokėdamas kitiems už stebėsenos infrastruktūros valdymą, mano klientai gali sutelkti dėmesį į savo platformų valdymą, o ne į stebėsenos stebėjimą, o tai reiškia, kad vertė, kurią jie gauna iš savo platformos stabilumo, daug viršija bet kokias stebėsenos kaip paslaugos išlaidas.


### Sensu + Graphite + ELK

Mano įmonė labai mėgsta savarankiškai talpinamus dalykus.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager įspėjimams; mano komanda tiki, kad paprasta stebėsena yra gera stebėsena.

Kitos sistemos, tokios kaip žurnalų registravimas ir sekimas, suteiks turtingą kontekstą diagnozuojant, kai budintis gauna įspėjimą, bet mes niekada nekuriame įspėjimų pagal jas.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Prometheus instrumentuotos paslaugos => Circonus analitika ir vizualizacija


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Naudojame toliau nurodytas paslaugas:

icinga2 stebėsenai ir VictorOps įspėjimams

NewRelic išsamiai paslaugos stebėsenai

Sentry klaidų sekimui paslaugoje

Slack/el. paštas yra įspėjimų dalis, kuri aktyvuojama iš NewRelic arba icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 su elasticsearch integracija analizei ir graphite+grafana integracija grafikams.

dėl icinga2 taikymo taisyklių lankstumo programuotojai mato tik tas paslaugas, apie kurias gauna pranešimus.

o per icinga2 director programuotojai gali lengvai apibrėžti savo patikras (ką jie daro kas kelias dienas – 100 patikrų išeina, 100 kitų patikrų ateina) dideliu mastu be jokių rūpesčių.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Ką turime dabar:

DataDog metrikoms

New Relic programų stebėsenai

ELK (Elastic Search + Logstash + Kibana) žurnalams

Sentry (savarankiškai talpinamas) išimčių registravimui

El. paštas + Slack + VictorOps įspėjimams (pagal svarbą)

Ką norime turėti:

Prometheus metrikoms (Grafana vizualizacijai)

New Relic (tikriausiai Elastic Search APM) programų stebėsenai

EFK (elastic search + fluentd + kibana) žurnalų registravimui. Tikriausiai Grafana Loki iki to laiko, kai čia pasieksime, bus paruoštas gamybai

Sentry išimtims

Alertmanager + el. paštas + VictorOps įspėjimams


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (atsakomybės apribojimas: dirba VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf serverio metrikoms, tokioms kaip CPU, diskas, atmintis ir tinklas. Telegraf taip pat naudojame SNMP mūsų tinklo įrenginių stebėsenai.

Prometheus programų metrikoms. Į savo programą užkoduojame sveikatos patikras, kurias Prometheus surenka.

InfluxDB laiko eilučių saugojimui. Čia siunčiami mūsų Telegraf duomenys.

Grafana skydeliams ir įspėjimams. Įspėjimų variklis nėra labai tvirtas, bet savo darbą atlieka. Taip pat siunčiame įspėjimus į Slack.

Ko šiuo metu neturiu – centralizuoto žurnalų registravimo sprendimo. ELK galingas, bet sunku jį nustatyti ir valdyti, o nežinau jokių nemokamų alternatyvų, kurios būtų pakankamai artimos, kad verta būtų jas nagrinėti.


### Sematext + Logagent + Experience

Sematext metrikoms, žurnalams, sekimui, netrukus ir realių naudotojų stebėsenai. Mano nuomone, paprasčiau ir pigiau nei naudoti N skirtingų įrankių / paslaugų.

Žurnalų siuntimui anksčiau naudojome rsyslog, o paskui perėjome prie Logagent.

Priekinės dalies strigčių pranešimui naudojame Sentry, bet netrukus pereisime prie Experience.

Atsakomybės apribojimas: esu Sematext darbuotojas.


### Azure Monitor/Analytics + OpsGenie

Norėčiau, kad Log Analytics turėtų geresnę sąsają. Atsisakome splunk, kuriame buvo daug lengviau naršyti.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Tikrai nenorite valdyti savo pranešimų sistemos. Splunk galite pakeisti ELK, nebent jūsų saugumo komanda teikia pirmenybę Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf kaip rinkėjas, Prometheus + Alertmanager stebėsenai ir įspėjimams, integruoti su slack kanalais ir pagerduty kritiniams įspėjimams. Grafana kompiuterių metrikų vizualizacijai.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus metrikoms + įspėjimams

Grafana Prometheus skydeliams

Cloudwatch stebi Prometheus egzempliorius

sentry išimčių sekimui

kibana + elasticsearch

graylog

prometheus Push Gateway paketinėms užduotims / cronjobs

SOP https://github.com/rapidloop/sop metrikoms „stumti / persiųsti“ iš vieno Prometheus egzemplioriaus į kitą

klientai naudoja arba Prometheus klientus. Klientų pusėje stengiamės naudoti opencensus.io


### PagerDuty + Monitis

PagerDuty + Monitis. Taip pat keletas individualių Azure Functions kai kurių paslaugų sveikatai tikrinti.

Šiais metais planuojame įdiegti Prometheus ir Grafana


### Prometheus + Grafana + Bosun

Prometheus laiko eilučių duomenims saugoti. Grafana vizualizacijai. Bosun įspėjimų valdymui.


### Azure Monitor/Analytics/Insights/Dashboards

Tik Azure parduotuvė: Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana konteinerių paslaugoms Kubernetes stebėti per Prometheus

Monitis visapusiškai paslaugų stebėsenai, daugiausia žiniatinklio API ir žiniatinklio programoms

OpsGenie įspėjimų valdymui

Slack būsenos informacijai iš mūsų sistemų gauti


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Ilgametis (dev)ops inžinierius. Užaugau su Nagios. Norėčiau išgirsti nuomones apie savo pačių paleistą SaaS https://checklyhq.com. Atliekame API stebėseną ir svetainės transakcijų stebėseną su gana išsamiais įspėjimais.

Checkly sukūriau todėl, kad aktyvi / sintetinė stebėsena API srityje buvo šiek tiek ribota (ir brangi). Naršykle pagrįsta / scenarijais pagrįsta stebėsena yra dar labiau uždara ir brangi. Naudojame Puppeteer ir kainas išlaikome kuo žemesnes.

Mūsų stebėsenos paketas:

Checkly (naudojame savo produktą...)

AppOptics (individualūs grafikai)

AWS Cloudwatch ir SNS SMS žinutėms.

integruoti Heroku įspėjimai.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana praneša mums slack apie infrastruktūros problemas ar našumo sumažėjimą, o logz.io sukonfigūravome įspėti slack apie tam tikrą klaidų lygio žurnalų kiekį iš programos sluoksnio.


### SignalFX + Splunk + PagerDuty + Slack

Šiuo metu naudojame: SignalFX, Splunk, PagerDuty ir Slack. Nesu didelis SignalFX gerbėjas, nors jų palaikymo komanda labai draugiška ir greitai reaguoja. Man patinka Splunk (verta, jei galite sau leisti), PagerDuty ir Slack.

Anksčiau naudojau TICK paketą, kur didžioji dalis C iš tikrųjų buvo G, t. y. Grafana, nors šiek tiek naudojau ir Chronograf. Tai buvo nuostabu, bet sunku valdyti. Klasikinė SaaS ir savarankiško talpinimo dilema.

Esu naudojęs DataDog, New Relic, Graylog, ELK ir BugSnag. Man labai patinka DataDog ir New Relic, Graylog yra gana geras. Nesu didelis ELK gerbėjas. BugSnag malonus, iš tikrųjų jaučiu, kad klaidų / išimčių sekimas daugeliu atvejų yra gana geras viso žurnalų stebėjimo pakaitalas.


### ELK + Prometheus + Grafana

Kaip ir kiti, naudojame ELK žurnalams, o Prometheus+Grafana – visam kitam.

Šią sąranką prižiūrėti lengva, jei leidžiate sau retkarčiais prarasti duomenis. Pavyzdžiui, jei mūsų ElasticSearch duomenų bazė susimaišo (o tai, deja, mums nutinka kas 2–3 mėnesius), nesivarginame su HA, o tiesiog išmetame duomenis ir gyvename toliau. Jei absoliučiai privalote turėti HA arba ilgalaikį saugojimą, sėkmės.


### Datadog + Prometheus + Grafana

Datadog nustatiau mėnesiniu pagrindu, nes kai čia atėjau, nebuvo nei stebėsenos, nei įspėjimų. Tik kelios mūsų svetainės buvo stebimos kas 5 min. dėl veikimo laiko. Datadog be abejonės yra paprasčiausias nustatyti. Kai baigsiu spręsti visas kitas problemas, pereisiu prie Prometheus+Grafana. Dar nesu 100 % apsisprendęs dėl žurnalų valdymo.

### Nagios + ELK

Palaikome daugiau nei 100 produktų.

Vietiniam diegimui (on-prem) dažniausiai Nagios ir ELK. Debesijoje pereiname nuo DataDog prie NewRelic.


### Datadog ar Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Anksčiau naudojome datadog, bet radome, kad jis per brangus mūsų poreikiams. Nesuprask klaidingai, jis nuostabus, bet kainuoja labai daug. Site24x7.com sukonfigūravome su metine prenumerata už maždaug 2–3 mėnesių DD kainą.

Mūsų stebėsenos paketas:

Site24x7 – APM, išorinių URL stebėsena, SMTP pašto srauto stebėsena, ssl galiojimo pabaigos ir procesų stebėsena.

StatusCake – URL stebėsenai ir patvirtinimui – tai mūsų atsarginis variantas, jei site24x7 kažko nepastebėtų (nepraleidžia), bet SC lankstesnis išorinių prievadų ir paslaugų stebėsenai mūsų poreikiams.

Abu įrankiai eskaluoja į PagerDuty, o paskui eskalacijas gauname slack.

SumoLogic – žurnalų stebėsenai (puikus įrankis, bet šiek tiek per sudėtingas mūsų poreikiams)

Iš slack galime patvirtinti gavimą (angl. ack) arba ištaisyti įspėjimą.

Tada turime daug site24x7 automatizacijų, kurios jungiasi prie commando.io „BedOps“, kaip mes tai vadiname – kai įspėjimas suaktyvinamas, paleidžiame keletą scenarijų ar automatizacijų bandydami ištaisyti situaciją (99 % atvejų automatizacija + mūsų scenarijai neleidžia patekti į bėdą).

Savo žinių bazėje turime vidinius veiksmų vadovus (angl. runbooks) atvejams, kai automatizacijos nepavyksta arba yra kažko, kas nepatenka į aprėptį ir ką reikia ištaisyti.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana metrikoms mūsų GKE klasteriuose ir VM.

Google Stackdriver žurnalams (nes jis įtrauktas ir numatytai aktyvus ir šiuo metu mums pakanka).


### Zabbix

Zabbix viskam. Papildomos programinės įrangos nereikia.
