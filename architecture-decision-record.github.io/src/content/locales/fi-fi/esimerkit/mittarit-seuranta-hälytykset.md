# Mittarit, seuranta, hälytykset

Sisällys:

* [Yhteenveto](#yhteenveto)
  * [Ongelma](#ongelma)
  * [Päätös](#päätös)
  * [Tila](#tila)
* [Yksityiskohdat](#yksityiskohdat)
  * [Oletukset](#oletukset)
  * [Rajoitteet](#rajoitteet)
  * [Kannat](#kannat)
  * [Perustelu](#perustelu)
  * [Seuraukset](#seuraukset)
* [Liittyvät](#liittyvät)
  * [Liittyvät päätökset](#liittyvät-päätökset)
  * [Liittyvät vaatimukset](#liittyvät-vaatimukset)
  * [Liittyvät artefaktit](#liittyvät-artefaktit)
  * [Liittyvät periaatteet](#liittyvät-periaatteet)
* [Huomiot](#huomiot)
  * [Vapaamuotoiset tekstiviestit vs. jäsennellyt tapahtumaviestit](#vapaamuotoiset-tekstiviestit-vs-jäsennellyt-tapahtumaviestit)
  * [Graylog on helpompi](#graylog-on-helpompi)
  * [Prometheus vaatii jonkin verran viritystä](#prometheus-vaatii-jonkin-verran-viritystä)
  * [AWS-palvelut ovat vaihtelevia](#aws-palvelut-ovat-vaihtelevia)
  * [Kafka](#kafka)
  * [Loki](#loki)
  * [Prometheus + alertmanager + Rollbar + Graylog + Grafana](#prometheus--alertmanager--rollbar--graylog--grafana)
  * [Thanos](#thanos)
  * [Prometheus HA](#prometheus-ha)
  * [ Datadog + PagerDuty + Threat Stack](#datadog--pagerduty--threat-stack)
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


## Yhteenveto


### Ongelma

Haluamme käyttää mittareita, seurantaa ja hälytyksiä, koska haluamme tietää, kuinka hyvin sovelluksemme toimivat, ja tietää, milloin on ongelma.


### Päätös

Työn alla.


### Tila

Tietojen keruu. Aloitamme uskottavista spektrin ääripäistä: suosituin vanhempi ilmainen työkalu (Nagios) ja suosituin uudempi maksullinen työkalu (New Relic).


## Yksityiskohdat


### Oletukset

Haluamme luoda nykyaikaisia, nopeita, luotettavia, responsiivisia jne. verkkosovelluksia.

Haluamme ostaa rakentamisen sijaan.


### Rajoitteet

Haluamme työkaluja, jotka toimivat hyvin devops-putkemme ja käyttöönottopilviemme kanssa.


### Kannat

Tutkimme kantoja parhaillaan.


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

  
### Perustelu

Toistaiseksi Nagios ja New Relic ovat spektrin ääripäät. Nagios on vanhin, yksinkertaisin, ilmainen, toteuttamiskelpoinen työkalu. New Relic on uusimmin varusteltu, kattavin, maksullinen, toteuttamiskelpoinen työkalu. Aloitamme näiden arvioinneilla. Tarvittaessa siirrymme spektrin sisäosiin.  

Toistaiseksi Zabbixilla on parhaat suositukset, ja se tarjoaa myös kattavimmat ominaisuudet.

Toistaiseksi ELK:lla on paras avoimen lähdekoodin rakenna-osta-sijaan-suosio.

Toistaiseksi Prometheus + Grafana ovat suosituimpia.


### Seuraukset

Tehtävä.


## Liittyvät


### Liittyvät päätökset

Valinnat vaikuttavat testattavuuteen, telemetriaan ja todennäköisesti muihin järjestelmiin, kuten asiakaspalveluun, sivuston luotettavuustekniikkaan jne.


### Liittyvät vaatimukset

Tehtävä.


### Liittyvät artefaktit

Tehtävä.


### Liittyvät periaatteet

Helposti peruttavissa.

Tarve nopeuteen.


## Huomiot


Melko hyvä avoimen lähdekoodin pino on:

* Prometheus mittareihin ja mittareihin perustuviin hälytyksiin

* Grafana mittarien näyttämiseen

* Elasticsearch/Logstash/Kibana (ELK) lokeihin ja jäsenneltyihin tapahtumiin

* Pushover mobiili-ilmoituksiin


### Vapaamuotoiset tekstiviestit vs. jäsennellyt tapahtumaviestit

Vapaamuotoiset tekstiviestit: esimerkiksi satunnaisia asioita, joita löytäisit tiedostosta /var/log/messages, ja jotain, mitä sovellus tuottaa tarkoituksella. Viestit ovat hyödyllisiä muiden koneella tapahtuvien asioiden, kuten muistin loppumisen tai laitteistovirheiden, tunnistamiseen, mutta niissä on paljon roskaa. 

Jäsennellyt tapahtumaviestit: sovelluksen tuottamia, kiinteällä tai dynaamisella joukolla attribuutteja, esim. HTTP-pyyntöloki, kirjanpitoloki, käyttäjän sisäänkirjautuminen.

Yleisesti ottaen on mukavaa kirjata jokaisen pyynnön yksityiskohdat tavalla, jonka avulla voit porautua attribuuttien perusteella. Joten esim. userid:n tai sessionid:n lisääminen kaikkeen mahdollistaa jäljittämisen. Eksplisiittinen jäljitys on tietysti myös hyvä. ELK:n käyttö tähän on eräänlainen köyhän miehen https://www.honeycomb.io/


### Graylog on helpompi

Graylog on kokemukseni mukaan helpompi saada käyntiin.



### Prometheus vaatii jonkin verran viritystä


Olen yleisesti tyytyväinen Prometheukseen mittareiden osalta. Hälytykset vaativat jonkin verran viritystä, mutta ovat melko hyviä. Se riippuu sovelluksestasi. Mielestäni on parasta hälyttää loppukäyttäjän näkemistä tiloista, ei taustalla olevista syistä. Esimerkiksi sivun latausaika on hyvä, pyyntöjen määrä sekunnissa ei ole. Vaikka nolla pyyntöä sekunnissa viittaa siihen, että jokin on vialla.

Palvelun etu on, että ne tarjoavat lisäälykkyyttä heti käyttöön otettaessa. Pidän yleisesti Datadogista. Palvelut voivat olla pelottavan kalliita, jos sinulla on paljon dataa, ja joskus niillä on hinnoittelumalleja, jotka eivät ole pilviystävällisiä, esim. veloittavat instanssia kohti, kun instanssit ovat dynaamisia. On myös ero palvelujen välillä, joissa jokainen pyyntö tulee maksavalta käyttäjältä, ja sellaisten välillä, jotka liittyvät mainontaan, jolloin vain pieni prosenttiosuus pyynnöistä tuottaa sinulle rahaa. Voit päätyä paljon dataan ja ei niin paljon budjettiin.

Työskentelen joidenkin palvelujen parissa, jotka saavat 1 miljardia pyyntöä päivässä, joten on järkevää isännöidä oma seuranta ja lokitus. Jos määräsi ovat pienempiä, isännöidyt palvelut ovat helpompia.


### AWS-palvelut ovat vaihtelevia

Kokemukseni AWS-palveluista on ollut vaihteleva. Heidän Elasticsearch-palvelunsa on ollut epävakaa, joten ajamme siihen omia instansseja. CloudWatch-mittarit ovat kalliita, joten käytämme niitä yleensä vain "infrastruktuuri"-tason mittareihin sovelluksen sijaan, eli terveyteen liittyviin mittareihin, joissa AWS voi tietää paremmin, mitä tapahtuu, kuin instanssilla ajettava ohjelmisto. CloudWatch Logs voi päivittyä hitaasti, eikä niissä ole niin paljon metadataa. ELK:n ajaminen auttaa tässä. Jos todella haluan reaaliaikaista dataa, Kafkan käyttö lokien kuljetuskanavana on parempi. Sitä tuetaan Logstashissa melko hyvin. Kafka-klusterin hallinta ei kuitenkaan ole heikkohermoisille, siinä on paljon paljastettua putkistoa.


### Kafka

Kommentti: Kafka voi olla ajoittain erittäin hankala, tai Kafka voi olla kallionvarma niin, että melkein unohdat sen olevan siellä sitomassa kaiken yhteen. 


Kommentti: Kafka on ollut vakaa, mutta sen käyttöönotossa oli yllättävän paljon työtä. Ajattelen sitä kuin relaatiotietokantaa, mutta työskentelet vain "fyysisellä" tasolla, esim. taulukkotiloilla, tiedostoilla ja osioilla. Alussa oli aikoja, jolloin hallintatyökaluja puuttui, ja jouduimme kirjoittamaan ohjelmia esim. kuluttajaryhmän nollaamiseen. http://howfuckedismydatabase.com/nosql/

Kommentti: Käytämme Kafkaa lokiviestien "puskurina" ja paikkana, jossa voimme tehdä reaaliaikaista virtakäsittelyä useilta palvelimilta tulevalle datalle. Jos saamme DDOS-hyökkäyksen, tarvitsemme tavan analysoida dataa usean instanssin yli. Jos kirjaamme suoraan palvelimilta ELK:hon, kuorma voi räjäyttää Elasticsearch-klusterin.

Kommentti: Kafka on meille hyvä, koska jos saamme DDOS-hyökkäyksen, tarvitsemme tavan analysoida dataa usean instanssin yli. Jos kirjaamme suoraan palvelimilta ELK:hon, kuorma voi räjäyttää Elasticsearch-klusterin.


Kommentti: Kafka tekee vähemmän työtä ja on tehokkaampi, joten se kestää kuorman paremmin. Ja jonotamme Kafka-työn ja yritämme uudelleen. Ja Kafkan ylikuormittuminen ei vaikuta käyttäjiin, jotka yrittävät tehdä interaktiivista työtä Kibanalla, kuten se tekisi, jos Elasticsearchilla olisi vaikeaa.

Kommentti:  Virtakäsittely etsii enimmäkseen väärinkäyttöä, esim. liikaa liikennettä yhdestä IP-osoitteesta koko klusterin yli, ja jakaa sitten eston koko klusterille.

Kommentti: logstash-output-kafka-lisäosa on tällä hetkellä melko epäluotettava. Olen purrut useista sen GitHub issues -sivun ongelmista, joita ei koskaan näytä korjattavan. Haluan luopua sen käytöstä ja lähettää suoraan sovelluksistamme Kafkaan.

Kommentti: Lähetämme nyt jäsenneltyjä tapahtumia suoraan sovelluksesta Kafkaan. Pääasiallinen motivaatio oli koskea lokidataan harvemmin ja välttää levyn lukemista ja kirjoittamista useita kertoja. Suuren volyymin järjestelmissä lokitus voi viedä enemmän työtä kuin itse sovellus. Mietin myös, että journald lähettäisi lokit suoraan, C-ohjelmasta.


### Loki

Pidä Lokia tarkasti silmällä. Se ei ole vielä valmis, mutta kun se on, odotan sen sopivan tähän pinoon paremmin. Loki on grafana labsin luoma lokien kokooja, joka käyttää samanlaista kaavintaa ja tunnistesyntaksia kuin Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager mittareille. <3 Prometheus.

Rollbar/Graylog lokitukseen/virheraportointiin (tässä on jotain päällekkäisyyttä; pieni palvelu ei todennäköisesti tarvitse molempia).

Tällä hetkellä hälytykset menevät vain yhdelle muutamasta Slack-kanavasta, joilla kiinnostuneet osapuolet ovat ottaneet ilmoitukset käyttöön. Jos olisimme vakavampia päivystyksen suhteen, ne menisivät PagerDuty/VictorOps/jne.

Grafana kaavioihin ja kojelautoihin. Odotan myös innolla, poistavatko heidän tulevat lokitusominaisuutensa Graylogin tarpeen.


### Thanos

Käytämme Thanosta HA-käyttöönottomme etuosana. Se osaa deduplikoida HA-parit.

Pidämme tällä hetkellä 6 kuukautta paikallista Prometheus-dataa. Tämä toimii meille kohtuullisen hyvin. Mutta olen juuri ottamassa käyttöön bucket-tallennusta Thanos-asetuksessamme pitkän aikavälin datan tallennusta varten. Teoriassa GCS-tallennus on noin 30 % halvempaa kuin GCE:n vakio-pysyvä levy, jota käytämme tällä hetkellä.

Emme varmuuskopioi Prometheus-dataa tällä hetkellä. Data ei vain ole meille oikeastaan tärkeää hälytyksiin riittävän määrän ylitse. Kokonaiskalustomme käyttöönotto muuttuu niin paljon vuodesta toiseen, että muutamaa kuukautta vanhempi historiallinen data ei ole kovin kiinnostavaa. Voisi olla kiinnostavaa saada muutamia ydintilastoja vuodesta toiseen, voin perustaa ydintilastojen tallennussääntöjoukon ja tallentaa ne Federationilla tai antaa Thanosin hoitaa sen.

MUOKKAUS: Pieni vastuuvapauslauseke, olen Prometheus-kehittäjä.


### Prometheus HA

HA Prometheuksessa tehdään monistamalla, ajat useita noutajia, ja on tapoja kysellä useita ja deduplikoida data.

Skaalaus tehdään päättämällä verkko ja antamalla eri Prometheusten noutaa eri osia verkosta.

Pitkäaikaistallennus ei ole promin vahva puoli, mutta se ladataan jonnekin kuten influxiin tai timescaledbiin (joka teknisesti rastittaa myös HA:n). Artikkeli, jonka luin aiheesta https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

En ole vielä kokeillut pitkäaikaistallennusosaa, koska vielä vain kokeilen ja käytän sitä lyhyen aikavälin kaavioihin, kun librenms valvoo verkkoani pitkällä aikavälillä


###  Datadog + PagerDuty + Threat Stack

Käytämme Datadogia (PagerDutyn kanssa) ja Threat Stackia emmekä voisi olla tyytyväisempiä. Ainoa valitukseni DD:stä on mittarien tallennuksen suhteellisen korkea hinta.


### Zabbix

Zabbix mukautetuilla skripteillä lähes kaiken valvontaan. Toimii kuin unelma.


### Outlyer

Käytän Outlyeria, mutta minun on ilmoitettava, että työskentelen täällä, ja oman tuotteen käyttö on pakollista.

Tarvitsen yhä Graylogia, Sentryä ja Statuscakea täydentämään.

Kuulostaa puolueelliselta, mutta ollessani iloisesti ajanut Nagiosta ja muita valvontajärjestelmiä sisäisesti, ostaisin isännöidyn ratkaisun missä tahansa uudessa työssä ja luopuisin tuosta tuskasta.


### Nagios + Nagiosgraph

Ajamme Nagiosta kaikkeen valvontaan ja hälyttämiseen. Hälytykset tapahtuvat sähköpostilla (varoitukset ja kriittiset ilmoitukset) ja kuuluvilla sovellusilmoituksilla (kriittisille hälytyksille).

Nagiosgraphia käytetään visualisointeihin.

Tämä asetelma on ollut erittäin tehokas pitämään meidät kattavasti ajan tasalla siitä, mitä ympäristössämme tapahtuu. Ajamme ja valvomme noin 110 tehtäväkriittistä palvelinta ja noin 760 datapistettä, ja meillä on ollut tämä valvontajärjestelmä käytössä yli seitsemän vuotta.

Haluaisin myös jossain vaiheessa koota lokit Graylogilla tai ELK:lla.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager mahtavan Prometheus Operator helm-kaavion kautta. Lokit menevät edelleen LogDNA:n birch-suunnitelmaan, koska huomasimme, että ELK on liian raskas vaatimattomalle GKE:llemme, jossa on vähintään 3 ja enintään 5 solmua.


### DataDog + Sentry + PagerDuty.

Ajoin ennen kaikki omat valvontaratkaisuni käyttäen kaikenlaisia ohjelmistoja, mukaan lukien Nagios, Icinga, Zabbix, ELK, Greylog2, Influx ja monet muut työkalut, mutta totuus on, että oman valvontainfrastruktuurin ajamiseen liittyy aivan liikaa vaivaa, varsinkin kun voit maksaa jollekin toiselle niin vähän siitä, että hän tekee sen puolestasi!

Valvontainfrastruktuurin ajamisesta maksaminen muille vapauttaa asiakkaani keskittymään alustojensa ajamiseen valvonnan valvomisen sijaan, mikä tarkoittaa, että arvo, jonka he saavat alustansa vakaudesta, ylittää reilusti kaikki valvonta palveluna -kustannukset.


### Sensu + Graphite + ELK

Yritykseni on todella innostunut itseisännöidyistä asioista.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager hälyttämiseen, tiimini uskoo, että yksinkertainen valvonta on hyvää valvontaa.

Muut järjestelmät kuten lokitus ja jäljitys tarjoavat rikkaan kontekstin diagnosointiin, kun päivystäjä saa hälytyksen, mutta emme koskaan rakenna hälytystä näiden varaan.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic


### Prometheus + Circonus

Prometheus-instrumentoidut palvelut => Circonus-analytiikka ja visualisointi


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Käytämme seuraavia palveluja:

icinga2 valvontaan ja VictorOps hälyttämiseen

NewRelic palvelun yksityiskohtaiseen valvontaan

Sentry virheiden seurantaan palvelussa

Slack/sähköposti on osa hälytystä, joka laukaistaan NewRelicistä tai icinga2:sta


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 elasticsearch-integraatiolla analyysiin ja graphite+grafana-integraatiolla kaavioihin.

icinga2:n apply-sääntöjen joustavuuden ansiosta kehittäjät näkevät vain palvelut, joista he saavat ilmoituksia.

ja icinga2 directorin kautta ohjelmoijat voivat helposti määritellä omat tarkistuksensa (mitä he tekevät, parin päivän välein - 100 tarkistusta lähtee, 100 muuta tulee) suuressa mittakaavassa ilman vaivaa.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Mitä meillä on nyt:

DataDog mittareille

New Relic sovellusvalvontaan

ELK (Elastic Search + Logstash + Kibana) lokeille

Sentry (itseisännöity) poikkeusten kirjaamiseen

Sähköpostit + Slack + VictorOps hälyttämiseen (vakavuuden mukaan)

Mitä haluamme:

Prometheus mittareille (Grafana visualisointiin)

New Relic (todennäköisesti Elastic Search APM) sovellusvalvontaan

EFK (elastic search + fluentd + kibana) lokitukseen. Luultavasti Grafanan Loki olisi tuotantovalmis siihen mennessä, kun pääsemme tähän

Sentry poikkeuksille

Alertmanager + sähköposti + VictorOps hälytyksille


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Vastuuvapauslauseke: työskentelee VMwarella)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf palvelinmittareille kuten CPU, levy, muisti ja verkko. Käytämme Telegrafia myös verkkolaitteidemme SNMP-valvontaan.

Prometheus sovellusmittareille. Koodaamme sovellukseemme terveystarkistuksia, joita Prometheus kaapii.

InfluxDB aikasarjojen tallennukseen. Tänne Telegraf-datamme lähetetään.

Grafana kojelautoihin ja hälytyksiin. Hälytysmoottori ei ole kovin vankka, mutta se hoitaa homman. Ammumme hälytyksiä myös Slackiin.

Se, mitä minulla ei tällä hetkellä ole, on keskitetty lokiratkaisu. ELK on tehokas mutta vaikea pystyttää ja hallita, enkä tiedä ilmaisia vaihtoehtoja, jotka olisivat riittävän lähellä tutkittaviksi.


### Sematext + Logagent + Experience

Sematext mittareille, lokeille, jäljille, pian myös todelliselle käyttäjävalvonnalle. Yksinkertaisempaa/halvempaa kuin N eri työkalun/palvelun käyttö, IMHO.

Lokien toimitukseen käytimme ennen rsyslogia ja sitten vaihdoimme Logagentiin.

Käyttöliittymän kaatumisraportointiin käytämme Sentryä, mutta vaihdamme pian Experienceen.

Vastuuvapauslauseke: olen sematextilainen.


### Azure Monitor/Analytics + OpsGenie

Toivoisin, että Log Analyticsilla olisi parempi käyttöliittymä. Siirrymme pois splunkista, jossa oli paljon helpompi navigoida.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Et todellakaan halua ajaa omaa ilmoitusjärjestelmääsi. Voit korvata Splunkin ELK:lla, ellei tietoturvatiimisi mieluummin halua Splunkia.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf keräimenä, Prometheus + Alertmanager valvontaan ja hälyttämiseen, integroituna slack-kanaviin ja pagerdutyyn kriittisiä hälytyksiä varten. Grafana isäntämittarien visualisointiin.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus mittareille + hälytyksille

Grafana Prometheus-kojelaudoille

Cloudwatch valvoo Prometheus-instansseja

sentry poikkeusten seurantaan

kibana + elasticsearch

graylog

prometheus Push Gateway eräajo-/cron-töille

SOP https://github.com/rapidloop/sop "työntämään/välittämään" mittareita yhdestä Prometheus-instanssista toiseen

asiakkaat käyttävät Prometheus-asiakkaita. Yritämme käyttää opencensus.io:ta asiakaspuolella


### PagerDuty + Monitis

PagerDuty + Monitis. Myös joitakin räätälöityjä Azure Functionseja joidenkin palvelujen terveyden testaamiseen.

Aiomme ottaa Prometheuksen ja Grafanan käyttöön tänä vuonna


### Prometheus + Grafana + Bosun

Prometheus aikasarjadatan tallennukseen. Grafana visualisointiin. Bosun hälytysten hallintaan.


### Azure Monitor/Analytics/Insights/Dashboards

Pelkkä Azure-kauppa, Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana konttipalvelujen valvontaan Kubernetesissa Prometheuksen kautta

Monitis päästä päähän -palvelujen valvontaan, pääasiassa verkko-API:lle ja verkkosovelluksille

OpsGenie hälytysten hallintaan

Slack tilatietojen saamiseen järjestelmistämme


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Pitkäaikainen (dev)ops-insinööri täällä. Kasvoin Nagiosin parissa. Kuulisin mielelläni mielipiteitä omarahoitteisesta SaaS:istani https://checklyhq.com. Teemme API-valvontaa ja sivustotransaktioiden valvontaa melko syvällisellä hälyttämisellä.

Aloitin Checklyn, koska aktiivinen / synteettinen valvonta API-tilassa oli hieman rajallista (ja kallista). Selainpohjainen / skriptattu valvonta on vielä suljetumpaa ja kalliimpaa. Käytämme Puppeteeria ja pidämme hinnoittelun mahdollisimman alhaisena.

Valvontapinomme:

Checkly (oman tuotteen käyttö...)

AppOptics (mukautettu kaavioiden piirto)

AWS Cloudwatch & SNS tekstiviesteille.

Herokun sisäänrakennetut hälytykset.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana hälyttää meitä slackissa infrastruktuuriongelmista tai suorituskyvyn heikkenemisestä, ja olemme konfiguroineet logz.io:n hälyttämään slackissa tietystä virhetason lokien määrästä sovelluskerroksesta.


### SignalFX + Splunk + PagerDuty + Slack

Käytän tällä hetkellä: SignalFX, Splunk, PagerDuty ja Slack. En ole suuri SignalFX-fani vaikka heidän tukitiiminsä on erittäin ystävällinen ja reagoiva. Pidän Splunkista (kannattaa, jos sinulla on varaa), PagerDutystä ja Slackista.

Käytin ennen TICK-pinoa, jossa suurin osa C:stä oli todellisuudessa G, eli Grafana, vaikka käytin hieman myös Chronografia. Se oli mahtava mutta vaivalloinen hallita. Klassinen SaaS vs. itseisännöinti -dilemma.

Olen käyttänyt DataDogia, New Relicia, Graylogia, ELK:ta ja BugSnagia. Pidän DataDogista ja New Relicistä paljon, Graylog on melko hyvä. En ole kuitenkaan suuri ELK-fani. BugSnag on mukava, minusta tuntuu, että virheiden/poikkeusten seuranta on monissa tapauksissa melko hyvä korvike täydelliselle lokien valvonnalle.


### ELK + Prometheus + Grafana

Kuten muutkin, käytämme ELK:ta lokeille ja Prometheus+Grafanaa kaikelle muulle.

Tämän asetelman ylläpito on helppoa, jos annat itsellesi luvan menettää joskus dataa. Esimerkiksi jos ElasticSearch-tietokantamme joutuu pahaan jamaan (mitä tapahtuu meille valitettavasti 2–3 kuukauden välein), emme vaivaudu HA:n kanssa vaan hävitämme datan ja jatkamme elämäämme. Jos sinulla ehdottomasti on oltava HA tai pitkäaikainen säilytys, onnea matkaan.


### Datadog + Prometheus + Grafana

Pystytin Datadogin kuukausi kuukaudelta, koska tänne tullessani ei ollut valvontaa eikä hälytyksiä. Vain pari sivustoamme valvottiin 5 minuutin välein käytettävyyden osalta. Datadog on ylivoimaisesti helpoin pystyttää. Kun olen saanut kaikki muut asiat hoidettua, vaihdan Prometheus+Grafanaan. En ole vielä 100 % päättänyt lokienhallinnasta.

### Nagios + ELK

Meillä on yli 100 tukemaamme tuotetta.

Paikallisesti se on enimmäkseen Nagios ja ELK. Pilvessä siirrymme DataDogista NewRelicille.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Käytimme ennen datadogia, mutta havaitsimme sen olevan aivan liian kallis tarpeisiimme. Älä ymmärrä väärin, se on mahtava, mutta sillä on valtava hinta. Onnistuimme pystyttämään site24x7.com:n vuosisopimuksella noin 2–3 kuukauden DD-kustannuksella.

Valvontapinomme:

Site24x7 - APM, ulkoisten URL-osoitteiden valvonta, SMTP-postivirran valvonta, ssl-voimassaolon päättymiset ja prosessien valvonta.

StatusCake - URL-valvontaan ja -vahvistukseen - Se on varmuuskopiomme siltä varalta, että site24x7 ohittaa jotain (ei ohita), mutta SC on joustavampi ulkoisten porttien ja palvelujen valvontaan tarpeisiimme.

Molemmat työkalut eskaloivat PagerDutyyn, ja sitten saamme eskalaatiomme slackissa.

SumoLogic - lokien valvontaan (se on mahtava työkalu mutta hieman monimutkainen tarpeisiimme)

Slackista voimme kuitata (ack) tai korjata hälytyksen.

Sitten meillä on paljon site24x7-automaatioita, jotka yhdistyvät commando.io:hon sille, mitä kutsumme 'BedOpsiksi' - jossa hälytyksen laukaisuessa käynnistämme muutaman skriptin tai automaation yrittäen korjata tilanteen (99 % ajasta automaatio + skriptimme pitävät meidät pulasta).

Meillä on sisäiset runbookit KB:ssamme siltä varalta, että automaatiot epäonnistuvat tai jos jokin laajuuden ulkopuolinen asia täytyy korjata.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana mittareille GKE-klustereissamme ja virtuaalikoneissamme.

Google Stackdriver lokeille (koska se on mukana ja oletuksena aktiivinen ja riittää tällä hetkellä tarpeisiimme).


### Zabbix

Zabbix kaikkeen. Ei tarvita lisäohjelmistoja.
