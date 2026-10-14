# Metriky, monitory, upozornění

Obsah:

* [Shrnutí](#shrnutí)
  * [Problém](#problém)
  * [Rozhodnutí](#rozhodnutí)
  * [Stav](#stav)
* [Podrobnosti](#podrobnosti)
  * [Předpoklady](#předpoklady)
  * [Omezení](#omezení)
  * [Stanoviska](#stanoviska)
  * [Argument](#argument)
  * [Důsledky](#důsledky)
* [Související](#související)
  * [Související rozhodnutí](#související-rozhodnutí)
  * [Související požadavky](#související-požadavky)
  * [Související artefakty](#související-artefakty)
  * [Související principy](#související-principy)
* [Poznámky](#poznámky)
  * [Volné textové zprávy versus strukturované zprávy událostí](#volné-textové-zprávy-versus-strukturované-zprávy-událostí)
  * [Graylog je snazší](#graylog-je-snazší)
  * [Prometheus vyžaduje trochu ladění](#prometheus-vyžaduje-trochu-ladění)
  * [Služby AWS jsou smíšené](#služby-aws-jsou-smíšené)
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


## Shrnutí


### Problém

Chceme používat metriky, monitory a upozornění, protože chceme vědět, jak dobře naše aplikace fungují, a vědět, kdy nastane problém.


### Rozhodnutí

Rozpracováno (WIP).


### Stav

Shromažďování informací. Začínáme u pravděpodobných krajů spektra: nejdoporučovanější starší bezplatný nástroj (Nagios) a nejdoporučovanější novější placený nástroj (New Relic).


## Podrobnosti


### Předpoklady

Chceme vytvářet webové aplikace, které jsou moderní, rychlé, spolehlivé, responzivní atd.

Chceme kupovat, ne budovat.


### Omezení

Chceme nástroje, které dobře fungují s naším devops pipeline a s našimi cloudy pro nasazení.


### Stanoviska

Stanoviska nyní zkoumáme.


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

Zatím jsou Nagios a New Relic kraje spektra. Nagios je nejstarší, nejjednodušší, bezplatný, schůdný nástroj. New Relic je nástroj s nejnovějšími funkcemi, nejúplnější, placený, schůdný. Začneme hodnocením těchto dvou. Podle potřeby se posuneme do vnitřku spektra.  

Zatím má Zabbix nejlepší doporučení a nabízí také nejúplnější možnosti.

Zatím má ELK nejlepší oblibu mezi open source řešeními upřednostňujícími budování před nákupem.

Zatím mají Prometheus + Grafana nejlepší oblibu.


### Důsledky

TODO.


## Související


### Související rozhodnutí

Volby ovlivní testovatelnost, telemetrii a pravděpodobně další systémy, například pro zákaznický servis, inženýrství spolehlivosti webů (SRE) atd.


### Související požadavky

TODO.


### Související artefakty

TODO.


### Související principy

Snadno vratné.

Potřeba rychlosti.


## Poznámky


Docela dobrý open source stack je:

* Prometheus pro metriky a upozornění založená na metrikách

* Grafana pro zobrazení metrik

* Elasticsearch/Logstash/Kibana (ELK) pro logy a strukturované události

* Pushover pro mobilní oznámení


### Volné textové zprávy versus strukturované zprávy událostí

Volné textové zprávy: například druh náhodných věcí, které najdete v /var/log/messages, a něco, co aplikace vytváří záměrně. Zprávy jsou užitečné pro identifikaci jiných věcí, které se na stroji dějí, jako nedostatek paměti nebo hardwarové chyby, ale mají hodně odpadu. 

Strukturované zprávy událostí: generované aplikací, s pevnou nebo dynamickou sadou atributů, např. log požadavků HTTP, účetní log, přihlášení uživatele.

Obecně je dobré logovat podrobnosti o každém požadavku způsobem, kterým můžete proniknout do hloubky podle atributů. Přidání např. userid nebo sessionid ke všemu tedy umožňuje sledování. Explicitní trasování (tracing) je samozřejmě také dobré. Použití ELK k tomu je jakási chudá obdoba https://www.honeycomb.io/


### Graylog je snazší

Graylog je podle mé zkušenosti snazší zprovoznit.



### Prometheus vyžaduje trochu ladění


S Prometheem pro metriky jsem obecně spokojený. Upozornění vyžadují trochu ladění, ale jsou docela dobrá. Záleží na vaší aplikaci. Myslím, že nejlépe je upozorňovat na stavy viditelné pro koncového uživatele, ne na základní příčiny. Například doba načtení stránky je dobrá, počet požadavků za sekundu ne. I když nula požadavků za sekundu naznačuje, že něco není v pořádku.

Výhodou služby je, že nabízí dodatečnou inteligenci hned z krabice. Obecně se mi líbí Datadog. Služby mohou být děsivě drahé, pokud máte hodně dat, a někdy mají cenové modely, které nejsou přátelské k cloudu, např. účtování za instanci, když jsou instance dynamické. Existuje také rozdíl mezi službami, kde každý požadavek pochází od platícího uživatele, a těmi souvisejícími s reklamou, takže jen malé procento požadavků vydělává peníze. Můžete skončit s hodně daty a ne tak velkým rozpočtem.

Pracuji na některých službách, které dostávají 1 miliardu požadavků denně, takže dává smysl hostovat si vlastní monitoring a logování. Pokud jsou vaše objemy menší, hostované služby jsou snazší.


### Služby AWS jsou smíšené

Moje zkušenost se službami AWS je smíšená. Jejich služba Elasticsearch byla nespolehlivá, takže provozujeme vlastní instance. Metriky CloudWatch jsou drahé, takže je obecně používáme jen pro metriky na úrovni „infrastruktury“, ne aplikace, tedy metriky související se zdravím, kde AWS může vědět lépe, co se děje, než software běžící na instanci. Logy CloudWatch mohou být pomalé při aktualizaci a nemají tolik metadat. Provoz ELK s tím pomáhá. Pokud opravdu chci data v reálném čase, je lepší použít Kafku jako transport logů. To je Logstashem docela dobře podporováno. Správa clusteru Kafka však není pro slabé povahy, je tam hodně odhaleného potrubí.


### Kafka

Komentář: Kafka může být občas nesmírně záludná, nebo může být skálopevná a skoro zapomenete, že tam je a vše spojuje. 


Komentář: Kafka byla solidní, ale zprovoznění bylo překvapivě hodně práce. Představuji si ji jako relační databázi, ale kde pracujete jen na „fyzické“ vrstvě, např. tabulkové prostory, soubory a oddíly. Na počátku byly chvíle, kdy chyběly nástroje pro správu, a museli jsme psát programy např. k resetu skupiny konzumentů. http://howfuckedismydatabase.com/nosql/

Komentář: Používáme Kafku jako „vyrovnávací paměť“ pro logovací zprávy a místo, kde můžeme provádět streamové zpracování v reálném čase na datech přicházejících z více serverů. Pokud nás zasáhne útok DDOS, potřebujeme způsob analýzy dat napříč více instancemi. Pokud logujeme přímo ze serverů do ELK, zátěž může shodit cluster Elasticsearch.

Komentář: Kafka je pro nás dobrá, protože pokud nás zasáhne útok DDOS, potřebujeme způsob analýzy dat napříč více instancemi. Pokud logujeme přímo ze serverů do ELK, zátěž může shodit cluster Elasticsearch.


Komentář: Kafka dělá méně práce a je efektivnější, takže zátěž zvládá lépe. A práci Kafky řadíme do fronty a opakujeme. A přetížení Kafky neovlivní uživatele, kteří se snaží interaktivně pracovat s Kibanou, jak by tomu bylo, kdyby Elasticsearch zápasil.

Komentář:  Streamové zpracování většinou hledá zneužití, např. příliš mnoho provozu z jedné IP napříč celým clusterem, a pak sdílí blokaci napříč celým clusterem.

Komentář: Zásuvný modul logstash-output-kafka je však v tuto chvíli dost nespolehlivý. Pokousalo mě několik problémů na jeho stránce issues na GitHubu, které se zdají být nikdy neopravovány. Chci od jeho používání odejít a posílat přímo z našich aplikací do Kafky.

Komentář: Nyní posíláme strukturované události přímo z aplikace do Kafky. Hlavní motivací bylo dotýkat se logovacích dat méně často a vyhnout se opakovanému čtení a zápisu na disk. V systémech s vysokým objemem může logování vyžadovat víc práce než samotná aplikace. Přemýšlím o tom, že by journald také posílal logy přímo, z programu v C.


### Loki

Mějte Loki na očích. Ještě není hotové, ale až bude, očekávám, že bude do tohoto stacku lépe zapadat. Loki je agregátor logů vytvořený Grafana Labs, používá podobnou syntaxi sběru a štítků jako Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager pro metriky. <3 Prometheus.

Rollbar/Graylog pro logování/hlášení chyb (je tu určitý překryv; malá služba pravděpodobně nepotřebuje obojí).

V současnosti upozornění jdou jen do jednoho z několika kanálů Slack, kde mají zainteresované strany zapnutá oznámení. Pokud bychom to s pohotovostí (on-call) brali vážněji, šla by do PagerDuty/VictorOps atd.

Grafana pro grafy a dashboardy. Také se nedočkavě těším, zda jejich nadcházející možnosti logování učiní Graylog zbytečným.


### Thanos

Thanos používáme jako front-end pro naše nastavení HA. Umí deduplikovat páry HA.

V současnosti uchováváme 6 měsíců lokálních dat Prometheus. Pro nás to funguje rozumně dobře. Ale jsem právě uprostřed zavádění úložiště bucket do našeho nastavení Thanos pro dlouhodobé ukládání dat. Teoreticky bude úložiště GCS asi o 30 % levnější než standardní persistentní disk GCE, který nyní používáme.

V současnosti nezálohujeme data Prometheus. Data pro nás vlastně nejsou důležitá nad rámec toho, abychom jich měli dost pro upozornění. Naše celkové nasazení flotily se rok od roku mění tak moc, že historická data starší než pár měsíců nejsou skutečně zajímavá. Mohlo by být zajímavé mít pár základních statistik meziročně; mohu nastavit sadu záznamových pravidel pro základní statistiky a ukládat je pomocí Federation nebo prostě nechat Thanos, ať se o to postará.

EDIT: Drobné upozornění, jsem vývojář Prometheus.


### Prometheus HA

HA v Prometheus se dělá duplikací — spouštíte více sběrných instancí a existují způsoby, jak dotazovat více z nich a deduplikovat data

Škálování se dělá rozdělením sítě a tím, že různé Prometheusy dotazují různé části sítě

Dlouhodobé ukládání není silnou stránkou Prometheus, ale přenáší se na něco jako Influx nebo timescaledb (který technicky také odškrtne HA) článek, který jsem o tom četl https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Dlouhodobé věci jsem zatím nezkoušel, protože stále jen experimentuji a používám to pro krátkodobé grafy, zatímco librenms monitoruje mou síť dlouhodobě


###  Datadog + PagerDuty + Threat Stack

Používáme Datadog (s PagerDuty) a Threat Stack a nemohli bychom být spokojenější. Moje jediná výtka k DD jsou relativně vysoké náklady na ukládání metrik.


### Zabbix

Zabbix s vlastními skripty k monitorování téměř čehokoli. Funguje skvěle.


### Outlyer

Používám Outlyer, ale musím prohlásit, že tu pracuji a používání vlastního produktu je povinnost.

Pro vylepšení stále potřebuji Graylog, Sentry a Statuscake.

Zní to zaujatě, ale poté, co jsem rád provozoval Nagios a další monitorovací systémy interně, v každém novém angažmá bych koupil hostované řešení a zbavil se té bolesti.


### Nagios + Nagiosgraph

Provozujeme Nagios pro veškeré monitorování a upozornění. Upozornění probíhají e-mailem (varování a kritická oznámení) a zvukovými oznámeními aplikace (pro kritická upozornění).

Nagiosgraph se používá pro vizualizace.

Toto nastavení bylo velmi účinné při tom, aby nás komplexně informovalo o tom, co se děje v našem prostředí. Provozujeme a monitorujeme asi 110 kritických serverů a asi 760 datových bodů a tento systém máme zavedený přes sedm let.

Chtěl bych také někdy agregovat logy pomocí Graylog nebo ELK.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager přes skvělý helm chart Prometheus Operator. Logy stále jdou do plánu birch LogDNA, protože jsme si všimli, že ELK je příliš těžké pro náš skromný cluster s min. 3 a max. 5 uzly na GKE.


### DataDog + Sentry + PagerDuty.

Dříve jsem provozoval všechna svá vlastní monitorovací řešení pomocí všech možných softwarů, včetně Nagios, Icinga, Zabbix, ELK, Greylog2, Influx a mnoha dalších nástrojů, ale pravdou je, že provozovat vlastní monitorovací infrastrukturu je příliš velké úsilí, zvlášť když můžete někomu jinému zaplatit tak nízké sazby, aby to udělal za vás!

Placení druhým za provoz monitorovací infrastruktury uvolňuje mým klientům ruce, aby se soustředili na provoz svých platforem místo monitorování monitoringu, což znamená, že hodnota, kterou získají ze stability své platformy, daleko převyšuje jakékoli náklady na Monitoring jako službu.


### Sensu + Graphite + ELK

Moje firma si velmi potrpí na vlastní hostování.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager pro upozornění, můj tým věří, že jednoduché monitorování je dobré monitorování.

Jiné systémy jako logování a trasování poskytnou bohatý kontext pro diagnostiku, když pohotovostní pracovník obdrží upozornění, ale nikdy na nich nestavíme upozornění.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Služby instrumentované Prometheem => analýza a vizualizace Circonus


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Používáme níže uvedené služby:

icinga2 pro monitorování a VictorOps pro upozornění

NewRelic pro podrobné monitorování služby

Sentry pro sledování chyb ve službě

Slack/e-mail jsou součástí upozornění spouštěných z NewRelic nebo icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 s integrací elasticsearch pro analýzu a integrací graphite+grafana pro grafy.

díky flexibilitě pravidel apply v icinga2 vidí vývojáři jen služby, o kterých dostávají oznámení.

a přes icinga2 director mohou programátoři snadno definovat své vlastní kontroly (což dělají, každých pár dní — 100 kontrol odejde, 100 dalších přijde) ve velkém měřítku bez problémů.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Co máme nyní:

DataDog pro metriky

New Relic pro monitorování aplikací

ELK (Elastic Search + Logstash + Kibana) pro logy

Sentry (vlastní hostování) pro logování výjimek

E-maily + Slack + VictorOps pro upozornění (podle závažnosti)

Co chceme mít:

Prometheus pro metriky (Grafana pro vizualizaci)

New Relic (pravděpodobně Elastic Search APM) pro monitorování aplikací

EFK (elastic search + fluentd + kibana) pro logování. Pravděpodobně Loki od Grafana bude připraveno pro produkci, než se k tomu dostaneme

Sentry pro výjimky

Alertmanager + e-mail + VictorOps pro upozornění


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Upozornění: pracuji ve VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf pro metriky serveru jako CPU, disk, paměť a síť. Telegraf používáme také pro monitorování SNMP našich síťových zařízení.

Prometheus pro metriky aplikace. Do naší aplikace kódujeme kontroly stavu, které Prometheus sbírá.

InfluxDB pro ukládání časových řad. Sem se posílají data z Telegrafu.

Grafana pro dashboardy a upozornění. Mechanismus upozornění není super robustní, ale svou práci dělá. Upozornění posíláme i do Slacku.

Co teď nemám, je centralizované řešení logování. ELK je výkonné, ale obtížné nastavit a spravovat, a neznám žádné bezplatné alternativy, které by byly dost blízko, aby stálo za to je prozkoumat.


### Sematext + Logagent + Experience

Sematext pro metriky, pro logy, pro stopy, brzy i pro monitorování skutečných uživatelů. Podle mého skromného názoru jednodušší/levnější než používání N různých nástrojů/služeb.

K odesílání logů jsme dříve používali rsyslog a pak jsme přešli na Logagent.

Pro hlášení pádů front-endu používáme Sentry, ale brzy přejdeme na Experience.

Upozornění: jsem Sematextan (zaměstnanec Sematext).


### Azure Monitor/Analytics + OpsGenie

Přál bych si, aby Log Analytics měl lepší rozhraní. Odcházíme od Splunku, ve kterém se bylo mnohem snazší orientovat.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Opravdu nechcete provozovat vlastní systém upozornění. Splunk můžete nahradit ELK, pokud váš bezpečnostní tým nepreferuje Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf jako sběrač, Prometheus + Alertmanager pro monitorování a upozornění, integrované s kanály slack a pagerduty pro kritická upozornění. Grafana pro vizualizaci metrik hostitelů.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus pro metriky + upozornění

Grafana pro dashboardy Prometheus

Cloudwatch monitorující instance Prometheus

sentry pro sledování výjimek

kibana + elasticsearch

graylog

prometheus Push Gateway pro dávkové úlohy/cronjoby

SOP https://github.com/rapidloop/sop k „posílání/předávání“ metrik z jedné instance Prometheus do druhé

klienti používají klienty Prometheus. Snažíme se používat opencensus.io na straně klienta


### PagerDuty + Monitis

PagerDuty + Monitis. Také nějaké vlastní Azure Functions pro testování zdraví některých služeb.

Letos plánujeme zavést Prometheus a Grafana


### Prometheus + Grafana + Bosun

Prometheus pro ukládání dat časových řad. Grafana pro vizualizaci. Bosun pro správu upozornění.


### Azure Monitor/Analytics/Insights/Dashboards

Firma jen s Azure: Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana pro monitorování kontejnerových služeb v Kubernetes přes Prometheus

Monitis pro end-to-end monitorování služeb, hlavně pro webová API a webové aplikace

OpsGenie pro správu upozornění

Slack pro příjem stavových informací z našich systémů


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Dlouholetý (dev)ops inženýr. Vyrostl jsem na Nagiosu. Rád bych slyšel názory na mé bootstrapped SaaS https://checklyhq.com. Provádíme monitorování API a transakcí webu s docela hlubokými upozorněními.

Checkly jsem založil, protože aktivní / syntetické monitorování v oblasti API bylo poněkud omezené (a drahé). Monitorování založené na prohlížeči / skriptech je ještě proprietárnější a dražší. Používáme Puppeteer a držíme ceny co nejníže.

Náš monitorovací stack:

Checkly (jíme vlastní jídlo...)

AppOptics (vlastní grafy)

AWS Cloudwatch a SNS pro SMS zprávy.

vestavěná upozornění Heroku.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana nás upozorňuje ve slacku na problémy s infrastrukturou nebo zhoršení výkonu a logz.io jsme nakonfigurovali tak, aby upozorňovalo ve slacku při určitém objemu logů úrovně chyba z aplikační vrstvy.


### SignalFX + Splunk + PagerDuty + Slack

V současnosti používáme: SignalFX, Splunk, PagerDuty a Slack. Nejsem velký fanoušek SignalFX, ačkoli jejich tým podpory je super přátelský a reaguje rychle. Splunk se mi líbí (stojí za to, pokud si ho můžete dovolit), PagerDuty a Slack také.

Dříve jsem používal stack TICK, kde většina C bylo ve skutečnosti G, tedy Grafana, ačkoli jsem trochu používal i Chronograf. To bylo úžasné, ale bolestivé na správu. Klasické dilema SaaS versus vlastní hostování.

Používal jsem DataDog, New Relic, Graylog, ELK a BugSnag. DataDog a New Relic se mi moc líbí, Graylog je docela dobrý. Nejsem velký fanoušek ELK. BugSnag je hezký, vlastně mám pocit, že sledování chyb/výjimek je v mnoha případech docela dobrá náhrada plného monitorování logů.


### ELK + Prometheus + Grafana

Jako ostatní používáme ELK pro logy a Prometheus+Grafana pro všechno ostatní.

Údržba tohoto nastavení je snadná, pokud si dovolíte občas přijít o data. Například pokud se naše databáze ElasticSearch dostane do mindráku (což se nám bohužel stává každé 2–3 měsíce), neobtěžujeme se s HA, ale data zahodíme a jdeme dál. Pokud absolutně musíte mít HA nebo dlouhodobé uchovávání, hodně štěstí.


### Datadog + Prometheus + Grafana

Datadog jsem nastavil na měsíční bázi, protože když jsem sem přišel, nebylo tu žádné monitorování ani upozornění. Jen pár našich webů se monitorovalo každých 5 minut na dostupnost. Datadog je bezkonkurenčně nejsnazší na nastavení. Až dokončím řešení všech ostatních problémů, přejdu na Prometheus+Grafana. Ohledně správy logů ještě nejsem 100% rozhodnutý.

### Nagios + ELK

Podporujeme přes 100 produktů.

Pro on-prem je to většinou Nagios a ELK. V cloudu migrujeme z DataDog na NewRelic.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Dříve jsme používali datadog, ale zjistili jsme, že je pro naše potřeby příliš drahý. Nechápejte mě špatně, je úžasný, ale má obrovské náklady. Podařilo se nám nastavit site24x7.com s ročním předplatným za asi 2–3 měsíce nákladů DD.

Náš monitorovací stack:

Site24x7 - APM, monitorování externích URL, monitorování toku pošty SMTP, vypršení ssl a monitorování procesů.

StatusCake - pro monitorování a potvrzování URL - je to naše záloha pro případ, že by site24x7 něco přehlédlo (nepřehlédne), ale SC je flexibilnější pro monitorování externích portů a služeb pro naše potřeby.

Oba nástroje eskalují do PagerDuty a pak dostáváme eskalace ve slacku.

SumoLogic - pro monitorování logů (je to skvělý nástroj, ale trochu složitý pro naše potřeby)

Ze slacku můžeme upozornění potvrdit nebo napravit.

Pak máme mnoho automatizací site24x7, které se připojují k commando.io pro „BedOps“, jak tomu říkáme — kde se spustí upozornění, spustíme několik skriptů nebo automatizací ve snaze situaci napravit (v 99 % případů nás automatizace + naše skripty udrží mimo potíže).

Máme interní runbooky v naší znalostní bázi pro případ, že automaty selžou nebo je třeba opravit něco mimo rozsah.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana pro metriky v našich clusterech GKE a na virtuálních strojích.

Google Stackdriver pro logy (protože je zahrnut a ve výchozím stavu aktivní a v současnosti pro naše potřeby stačí).


### Zabbix

Zabbix pro všechno. Není potřeba žádný další software.


