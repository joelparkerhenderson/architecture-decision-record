# Mõõdikud, seire, hoiatused

Sisukord:

* [Kokkuvõte](#kokkuvõte)
  * [Küsimus](#küsimus)
  * [Otsus](#otsus)
  * [Olek](#olek)
* [Üksikasjad](#üksikasjad)
  * [Eeldused](#eeldused)
  * [Piirangud](#piirangud)
  * [Seisukohad](#seisukohad)
  * [Argument](#argument)
  * [Tagajärjed](#tagajärjed)
* [Seotud](#seotud)
  * [Seotud otsused](#seotud-otsused)
  * [Seotud nõuded](#seotud-nõuded)
  * [Seotud artefaktid](#seotud-artefaktid)
  * [Seotud põhimõtted](#seotud-põhimõtted)
* [Märkmed](#märkmed)
  * [Vabatekstisõnumid versus struktureeritud sündmussõnumid](#vabatekstisõnumid-versus-struktureeritud-sündmussõnumid)
  * [Graylog on lihtsam](#graylog-on-lihtsam)
  * [Prometheus vajab mõningast häälestamist](#prometheus-vajab-mõningast-häälestamist)
  * [AWS-i teenused on segased](#aws-i-teenused-on-segased)
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


## Kokkuvõte


### Küsimus

Tahame kasutada mõõdikuid, seiret ja hoiatusi, sest tahame teada, kui hästi meie rakendused töötavad, ja teada, millal on probleem.


### Otsus

WIP.


### Olek

Kogume teavet. Alustame spektri mõistlikest äärmustest: kõige soovitatum vanem tasuta tööriist (Nagios) ja kõige soovitatum uuem tasuline tööriist (New Relic).


## Üksikasjad


### Eeldused

Tahame luua veebirakendusi, mis on kaasaegsed, kiired, töökindlad, reageerivad jne.

Tahame pigem osta kui ehitada.


### Piirangud

Tahame tööriistu, mis töötavad hästi meie devopsi torujuhtme ja meie kasutuselevõtupilvedega.


### Seisukohad

Uurime praegu seisukohti.


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

Siiani on Nagios ja New Relic spektri äärmused. Nagios on vanim, lihtsaim, tasuta, teostatav tööriist. New Relic on uusimate funktsioonidega, kõige täielikum, tasuline, teostatav tööriist. Alustame nende hindamisest. Vajaduse korral liigume spektrisse sissepoole.  

Siiani on Zabbixil parimad soovitused ja see pakub ka kõige täielikumaid võimalusi.

Siiani on ELK-l parim populaarsus avatud lähtekoodiga, ehita-ise-ostmise-asemel seas.

Siiani on Prometheus + Graphanal parim populaarsus.


### Tagajärjed

TODO.


## Seotud


### Seotud otsused

Valikud mõjutavad testitavust, telemeetriat ja tõenäoliselt teisi süsteeme, näiteks klienditoe, saidi töökindlusinseneeria jne jaoks.


### Seotud nõuded

TODO.


### Seotud artefaktid

TODO.


### Seotud põhimõtted

Hõlpsasti tagasipööratav.

Vajadus kiiruse järele.


## Märkmed


Üsna hea avatud lähtekoodiga pakett on:

* Prometheus mõõdikute ja mõõdikupõhiste hoiatuste jaoks

* Grafana mõõdikute kuvamiseks

* Elasticsearch/Logstash/Kibana (ELK) logide ja struktureeritud sündmuste jaoks

* Pushover mobiiliteavituste jaoks


### Vabatekstisõnumid versus struktureeritud sündmussõnumid

Vabatekstisõnumid: näiteks need juhuslikud asjad, mida leiad failist /var/log/messages, ja miski, mille rakendus tahtlikult genereerib. Sõnumid on kasulikud muude masinas toimuvate asjade tuvastamiseks, nagu mälupuudus või riistvaratõrked, kuid sisaldavad palju prahti. 

Struktureeritud sündmussõnumid: rakenduse genereeritud, fikseeritud või dünaamilise atribuutide komplektiga, nt HTTP päringulogi, raamatupidamislogi, kasutaja sisselogimine.

Üldiselt on mõnus logida iga päringu üksikasju viisil, mis võimaldab atribuutide järgi süvitsi minna. Nii et näiteks userid-i või sessionid-i lisamine kõigele võimaldab jälgida. Selgesõnaline jälgimine on loomulikult samuti hea. ELK kasutamine selleks on omamoodi vaese mehe https://www.honeycomb.io/


### Graylog on lihtsam

Graylog on minu kogemuse järgi lihtsam seadistada.



### Prometheus vajab mõningast häälestamist


Olen üldiselt Prometheusega mõõdikute osas rahul. Hoiatamine vajab mõningast häälestamist, kuid on üsna hea. See sõltub sinu rakendusest. Arvan, et parim on hoiatada lõppkasutajale nähtavate seisundite kohta, mitte aluseks olevate põhjuste kohta. Näiteks lehe laadimisaeg on hea, päringute arv sekundis ei ole. Kuigi null päringut sekundis viitab, et midagi on valesti.

Teenuse eelis on see, et nad pakuvad karbist välja lisaintelligentsi. Mulle meeldib üldiselt Datadog. Teenused võivad olla hirmutavalt kallid, kui sul on palju andmeid, ja neil on mõnikord hinnamudelid, mis ei ole pilvesõbralikud, nt arveldamine eksemplari kohta, kui eksemplarid on dünaamilised. On ka vahe teenuste vahel, kus iga päring tuleb maksvalt kasutajalt, ja nende vahel, mis on reklaamiga seotud, nii et ainult väike protsent päringutest toob sulle raha. Võid lõpetada palju andmete ja mitte nii palju eelarvega.

Töötan mõne teenuse kallal, mis saavad 1 miljard päringut päevas, seega on mõistlik hostida oma seiret ja logimist. Kui sinu mahud on väiksemad, on hostitud teenused lihtsamad.


### AWS-i teenused on segased

Minu kogemus AWS-i teenustega on olnud segane. Nende Elasticsearchi teenus on olnud ebastabiilne, seega käitame selle jaoks oma eksemplare. CloudWatchi mõõdikud on kallid, seega kasutame neid üldiselt ainult "taristutaseme" mõõdikute jaoks, mitte rakenduse jaoks, st tervisega seotud mõõdikud, kus AWS saab paremini teada, mis toimub, kui eksemplaris töötav tarkvara. CloudWatch Logs võib olla uuendamiseks aeglane ja neil pole palju metaandmeid. ELK käitamine aitab sellega. Kui tõesti tahan reaalajaandmeid, on parem kasutada Kafkat logide transpordiks. Seda toetab Logstash üsna hästi. Kafka klastri haldamine pole aga nõrganärvilistele, on palju paljast torutööd.


### Kafka

Kommentaar: Kafka võib mõnikord olla supertugev, või Kafka võib olla nii kivikõvalt stabiilne, et unustad peaaegu, et see seal on ja seob kõik kokku. 


Kommentaar: Kafka on olnud stabiilne, kuid selle tööle saamine võttis üllatavalt palju tööd. Mõtlen sellest kui relatsioonilisest andmebaasist, kuid sa töötad ainult "füüsilisel" kihil, nt tabeliruumid, failid ja partitsioonid. Algusaegadel oli hetki, kus haldustööriistad puudusid ja pidime kirjutama programme, et näiteks tarbijarühma lähtestada. http://howfuckedismydatabase.com/nosql/

Kommentaar: Kasutame Kafkat logisõnumite "puhvrina" ja kohana, kus saame teha reaalaja voogtöötlust mitmest serverist tulevatel andmetel. Kui saame DDOS-rünnaku, vajame viisi andmete analüüsimiseks mitme eksemplari lõikes. Kui logime otse serveritest ELK-sse, võib koormus Elasticsearchi klastri õhku lasta.

Kommentaar: Kafka on meile hea, sest kui saame DDOS-rünnaku, vajame viisi andmete analüüsimiseks mitme eksemplari lõikes. Kui logime otse serveritest ELK-sse, võib koormus Elasticsearchi klastri õhku lasta.


Kommentaar: Kafka teeb vähem tööd ja on tõhusam, seega suudab see koormust paremini käsitleda. Ja me paneme Kafka töö järjekorda ja proovime uuesti. Ja see, et Kafka on üle koormatud, ei mõjuta kasutajaid, kes üritavad Kibanaga interaktiivselt töötada, nagu see juhtuks, kui Elasticsearchil on raske.

Kommentaar:  Voogtöötlus otsib enamasti kuritarvitust, nt liiga palju liiklust ühelt IP-lt kogu klastris, ja jagab seejärel blokeeringut kogu klastris.

Kommentaar: Plugin logstash-output-kafka on praegu aga üsna ebausaldusväärne. Olen kokku puutunud mitme probleemiga selle GitHubi issue'de lehel, mida ei paista kunagi parandatavat. Tahan sellest loobuda ja saata otse oma rakendustest Kafkasse.

Kommentaar: Saadame nüüd struktureeritud sündmusi otse rakendusest Kafkasse. Peamine motivatsioon oli puutuda logiandmeid vähem kordi ja vältida ketta mitmekordset lugemist ja kirjutamist. Suure mahuga süsteemides võib logimine nõuda rohkem tööd kui rakendus ise. Kaalun ka journald'i panemist logisid otse saatma, C-programmist.


### Loki

Hoia Lokil silma peal. See pole veel valmis, kuid kui on, eeldan, et see sobib sellesse pakkidesse paremini. Loki on grafana labsi loodud logikoguja, mis kasutab sarnast kraapimise ja sildi süntaksit nagu Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager mõõdikute jaoks. Armastan Prometheust.

Rollbar/Graylog logimiseks/veaaruandluseks (siin on mõningane kattuvus; väike teenus ei vaja tõenäoliselt mõlemat).

Praegu lähevad hoiatused ainult ühte mõnest Slacki kanalist, mille jaoks huvilised on teavitused sisse lülitanud. Kui oleksime valvekorralduses tõsisemad, läheksid need PagerDuty/VictorOps/jne.

Grafana graafikute ja armatuurlaudade jaoks. Ootan ka põnevusega, kas nende tulevased logimisfunktsioonid muudavad Graylogi üleliigseks.


### Thanos

Kasutame Thanost oma HA-seadistuse esiotsana. See oskab HA-paare dubleerimisest vabastada.

Hoiame praegu 6 kuud kohalikke Prometheuse andmeid. See töötab meil üsna hästi. Aga olen parasjagu keset ämbrisalvestuse kasutuselevõttu meie Thanose seadistusele pikaajaliseks andmesalvestuseks. Teoorias on GCS-i salvestus umbes 30% odavam kui GCE standardne püsiketas, mida praegu kasutame.

Me ei tee praegu Prometheuse andmetest varukoopiaid. Andmed pole meile lihtsalt eriti olulised peale selle, et neid oleks piisavalt hoiatuste jaoks. Meie üldine laevastiku kasutuselevõtt muutub aastast aastasse nii palju, et ajaloolised andmed, mis on vanemad kui paar kuud, pole lihtsalt nii huvitavad. Võib olla huvitav omada mõningaid põhistatistikaid aasta aastalt, võib-olla seadistan salvestusreeglite komplekti põhistatistikate jaoks ja salvestan need Federationiga või lasen lihtsalt Thanosel seda käsitleda.

EDIT: Väike selgitus, ma olen Prometheuse arendaja.


### Prometheus HA

HA Prometheuses tehakse dubleerimisega: käitad mitut koguja, on viise mitut päringuida ja andmeid dubleerimisest vabastada.

Skaleerimine toimub võrkude määramisega ja erinevate Prometheuste laskmisega päringuid teha võrgu erinevatest osadest.

Pikaajaline salvestus ei ole Prometheuse tugevus, vaid see delegeeritakse millelegi nagu influx või timescaledb (mis tehniliselt märgib ära ka HA). Artikkel, mida selle kohta lugesin https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Pole pikaajalist osa veel proovinud, sest katsetan endiselt ainult ja kasutan seda lühiajaliste graafikute jaoks, kui librenms jälgib minu võrku pikaajaliselt


###  Datadog + PagerDuty + Threat Stack

Kasutame Datadogi (PagerDutyga) ja Threat Stacki ning ei saaks olla rahulolevamad. Minu ainus kaebus DD kohta on mõõdikute salvestuse suhteliselt kõrge hind.


### Zabbix

Zabbix kohandatud skriptidega peaaegu kõige jälgimiseks. Töötab nagu unistus.


### Outlyer

Kasutan Outlyerit, kuid pean selgitama, et töötan siin ja oma koerasöödat söömine (dogfooding) on kohustuslik.

Vajan endiselt Graylogi, Sentryt ja Statuscake'i täiustamiseks.

Kõlab erapoolikuna, kuid pärast Nagiose ja teiste seiresüsteemide mõnuga sisemiselt käitamist ostaksin igas uues töökohas hostitud lahenduse ja delegeeriksin selle valu.


### Nagios + Nagiosgraph

Käitame Nagiost kogu seire ja hoiatamise jaoks. Hoiatamine toimub e-posti (hoiatused ja kriitilised teavitused) ja kuuldavate rakenduse teavituste (kriitiliste hoiatuste jaoks) kaudu.

Nagiosgraphi kasutatakse visualiseerimisteks.

See seadistus on olnud väga tõhus, et hoida meid põhjalikult kursis sellega, mis meie keskkonnas toimub. Käitame ja jälgime umbes 110 äriliselt kriitilist serverit ja umbes 760 andmepunkti ning meil on see hommikusüsteem olnud kasutusel üle seitsme aasta.

Tahaksin ka mingil hetkel logisid koondada Graylogi või ELk-ga.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager suurepärase helm-diagrammi Prometheus Operatori kaudu. Logid lähevad endiselt LogDNA birch'i plaani, sest märkasime, et ELK on liiga raske meie tagasihoidliku klastri jaoks min 3 max 5 sõlmega GKE-s.


### DataDog + Sentry + PagerDuty.

Ma käitasin ennem kõiki oma seirelahendusi igasuguse tarkvaraga, sealhulgas Nagios, Icinga, Zabbix, ELK, Greylog2, Influx ja paljud teised tööriistad, kuid tõde on see, et omaenda seiretaristu käitamine on liiga palju tööd, eriti kui saad kellelegi teisele nii madalat hinda maksta, et ta seda sinu eest teeks!

Teistele maksmine seiretaristu käitamise eest vabastab minu kliendid keskenduma oma platvormide käitamisele, mitte seire jälgimisele, mis tähendab, et väärtus, mida nad saavad oma platvormi stabiilsusest, ületab kaugelt seire kui teenuse kulud.


### Sensu + Graphite + ELK

Minu ettevõte on isehostitavate asjade poolt.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager hoiatamiseks, minu meeskond usub, et lihtne seire on hea seire.

Muud süsteemid nagu logimine ja jälgimine annavad rikkaliku konteksti diagnoosiks, kui valvaja saab hoiatuse, kuid me ei ehita kunagi hoiatamist nende peale.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Prometheusega instrumenteeritud teenused => Circonuse analüüs ja visualiseerimine


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Kasutame järgmisi teenuseid:

icinga2 seireks ja VictorOps hoiatamiseks

NewRelic teenuse üksikasjalikuks seireks

Sentry teenuse veajälgimiseks

Slack/e-post on osa hoiatamisest, mis käivitatakse NewRelicust või icinga2-st


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 koos elasticsearchi integratsiooniga analüüsiks ja graphite+grafana integratsiooniga graafikute jaoks.

tänu icinga2 apply-reeglite paindlikkusele näevad arendajad ainult teenuseid, mille kohta nad teavitusi saavad.

ja icinga2 directori kaudu saavad programmeerijad hõlpsasti määratleda oma kontrolle (mida nad teevad, mõne päeva tagant – 100 kontrolli väljub, 100 muud kontrolli siseneb) suures mastaabis vaevata.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Mis meil praegu on:

DataDog mõõdikute jaoks

New Relic rakenduse seireks

ELK (Elastic Search + Logstash + Kibana) logide jaoks

Sentry (isehostitav) erandite logimiseks

E-post + Slack + VictorOps hoiatamiseks (tõsiduse alusel)

Mida me tahame:

Prometheus mõõdikute jaoks (Grafana visualiseerimiseks)

New Relic (tõenäoliselt Elastic Search APM) rakenduse seireks

EFK (elastic search + fluentd + kibana) logimiseks. Tõenäoliselt on Grafana Loki tootmiseks valmis selleks ajaks, kui sinna jõuame

Sentry erandite jaoks

Alertmanager + e-post + VictorOps hoiatuste jaoks


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (selgitus: töötab VMware'is)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf serverimõõdikute jaoks nagu CPU, ketas, mälu ja võrk. Kasutame Telegrafi ka oma võrguseadmete SNMP-seireks.

Prometheus rakenduse mõõdikute jaoks. Kodeerime oma rakendusse tervisekontrollid, mida Prometheus kraabib.

InfluxDB aegridade salvestuseks. Siia läheb meie Telegrafi andmed.

Grafana armatuurlaudade ja hoiatuste jaoks. Hoiatusmootor ei ole ülitugev, kuid teeb oma töö ära. Saadame hoiatusi ka Slacki.

Mida mul praegu pole, on tsentraliseeritud logimislahendus. ELK on võimas, kuid raske seadistada ja hallata ning ma ei tea ühtegi tasuta alternatiivi, mis oleks piisavalt lähedal, et vaadata.


### Sematext + Logagent + Experience

Sematext mõõdikute, logide, jälgede ja peagi ka päris kasutajate seire jaoks. Minu tagasihoidliku arvamuse kohaselt lihtsam/odavam kui N erineva tööriista/teenuse kasutamine.

Logide saatmiseks kasutasime rsyslogi ja läksime siis üle Logagentile.

Kasutajaliidese kokkujooksmise aruandluseks kasutame Sentryt, kuid läheme peagi üle Experience'ile.

Selgitus: ma olen Sematextlane.


### Azure Monitor/Analytics + OpsGenie

Soovin, et Log Analyticsil oleks parem liides. Liigume eemale splunkist, mis oli palju lihtsam navigeerida.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Sa ei taha tõesti oma teavitussüsteemi käitada. Splunki saab asendada ELK-ga, kui sinu turvameeskond ei eelista Splunki.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf koguja, Prometheus + Alertmanager seire ja hoiatamise jaoks, integreeritud slack-kanalite ja pagerdutyga kriitiliste hoiatuste jaoks. Grafana hostimõõdikute visualiseerimiseks.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus mõõdikute + hoiatuste jaoks

Grafana Prometheuse armatuurlaudade jaoks

Cloudwatch jälgib Prometheuse eksemplare

sentry erandite jälgimiseks

kibana + elasticsearch

graylog

prometheus Push Gateway partii/cronjobide jaoks

SOP https://github.com/rapidloop/sop mõõdikute "lükkamiseks/edastamiseks" ühelt Prometheuse eksemplarilt teisele

kliendid kasutavad kas Prometheuse kliente. Püüame kliendipoolel kasutada opencensus.io


### PagerDuty + Monitis

PagerDuty + Monitis. Ka mõned kohandatud Azure Functions mõnede teenuste tervise testimiseks.

Loodan sel aastal Prometheuse ja Grafana kasutusele võtta


### Prometheus + Grafana + Bosun

Prometheus aegridade andmete salvestamiseks. Grafana visualiseerimiseks. Bosun hoiatuste haldamiseks.


### Azure Monitor/Analytics/Insights/Dashboards

Ainult Azure: Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana konteinerteenuste jälgimiseks Kubernetes'es Prometheuse kaudu

Monitis teenuste otsast-otsani seireks, peamiselt veebi-API-de ja veebirakenduste jaoks

OpsGenie hoiatuste haldamiseks

Slack meie süsteemide olekuteabe saamiseks


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Kauaaegne (dev)ops-insener siin. Kasvasin üles Nagiosega. Tahaksin meelsasti arvamusi oma isefinantseeritud SaaS-i https://checklyhq.com kohta. Teeme API seiret ja veebisaidi tehingute seiret üsna sügavat hoiatamisega.

Alustasin Checklyt, sest aktiivne / sünteetiline seire API ruumis oli veidi piiratud (ja kallis). Brauseripõhine / skriptitud seire on veelgi rohkem omandiline ja kallis. Kasutame Puppeteerit ja hoiame hinnad nii madalal kui võimalik.

Meie seirepakett:

Checkly (dogfooding...)

AppOptics (kohandatud graafikud)

AWS Cloudwatch & SNS SMS-sõnumite jaoks.

sisseehitatud Heroku hoiatamine.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana hoiatab meid slackis taristuprobleemide või jõudluse halvenemise korral ning oleme seadistanud logz.io hoiatama slackis teatud mahu veataseme logide korral rakenduse kihist.


### SignalFX + Splunk + PagerDuty + Slack

Kasutan praegu: SignalFX, Splunk, PagerDuty ja Slack. Ma pole SignalFXi suur fänn, kuigi nende tugimeeskond on supersõbralik ja reageeriv. Mulle meeldib Splunk (väärt, kui sul on selleks raha), PagerDuty ja Slack.

Kasutasin ennem TICK-paketti, kus enamik C-st oli tegelikult G, st Grafana, kuigi kasutasin ka Chronografi veidi. See oli fantastiline, kuid tüütu hallata. Klassikaline dilemmaküsimus SaaS versus isehostimine.

Olen kasutanud DataDogi, New Relici, Graylogi, ELK-d ja BugSnagi. Mulle meeldib väga DataDog ja New Relic, Graylog on üsna hea. Ma pole suur ELK fänn. BugSnag on tore, mulle tundub tegelikult, et vigade/erandite jälgimine on paljudel juhtudel üsna hea asendus täielikule logiseirele.


### ELK + Prometheus + Grafana

Nagu teised, kasutame logide jaoks ELK-d ja kõige muu jaoks Prometheus+Grafanat.

Selle seadistuse hooldamine on lihtne, kui lubad endale aeg-ajalt andmeid kaotada. Kui näiteks meie ElasticSearchi andmebaas satub langusesse (mis meil kahjuks juhtub iga 2–3 kuu tagant), ei hooli me HA-st, vaid viskame andmed minema ja jätkame oma elu. Kui sa absoluutselt vajad HA-d või pikaajalist salvestust, õnn kaasa.


### Datadog + Prometheus + Grafana

Seadsin Datadogi üles kuupõhiselt, sest kui siia tulin, polnud seiret ega hoiatamist. Ainult paar meie saiti oli kontrollitud iga 5 minuti tagant tööaja osas. Datadog on kahtlemata kõige lihtsam seadistada. Kui olen kõigi teiste probleemidega tegelenud, lähen üle Prometheus+Grafanale. Pole logihalduse osas veel 100% kindel.

### Nagios + ELK

Toetame üle 100+ toote.

Kohapealse jaoks on see enamasti Nagios ja ELK. Pilve jaoks migreerume DataDogilt NewRelicule.


### Datadog versus Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Kasutasime ennem datadogi, kuid leidsime, et see on meie vajaduste jaoks liiga kallis. Ära mõista valesti, see on suurepärane, kuid sellel on tohutu kulu. Suutsime seadistada site24x7.com aastatellimusega umbes 2–3 kuu DD kulu eest.

Meie seirepakett:

Site24x7 - APM, väliste URL-ide seire, SMTP-posti voo seire, ssl aegumiskuupäev ja protsessiseire.

StatusCake - URL-i seire ja kinnitamise jaoks - See on meie varuvariant juhuks, kui site24x7 midagi kahe silma vahele jätab (ei jäta), kuid SC on paindlikum väliste portide ja teenuste seireks meie vajaduste jaoks.

Mõlemad tööriistad eskaleerivad PagerDutysse ja siis saame oma eskalatsioonid slackis.

SumoLogic - logiseireks (see on suurepärane tööriist, kuid veidi keeruline meie vajaduste jaoks)

Slackist saame hoiatust kinnitada (ack) või lahendada.

Siis on meil palju site24x7 automatiseerimisi, mis ühendavad commando.io-ga selle jaoks, mida nimetame 'BedOps' - kus hoiatuse käivitumisel alustame mõningaid skripte või automatiseerimisi katsena olukorda parandada (99% ajast hoiavad automatiseerimine + meie skriptid meid hädast eemal).

Meil on sisemised runbookid oma KB-s, kui automatiseerimised ebaõnnestuvad või kui on midagi ulatusest väljas, mida tuleb parandada.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana mõõdikute jaoks meie GKE klastrites ja VM-ides.

Google Stackdriver logide jaoks (sest see on kaasas ja vaikimisi aktiivne ning praegu meie vajaduste jaoks piisav).


### Zabbix

Zabbix kõige jaoks. Lisatarkvara pole vaja.
