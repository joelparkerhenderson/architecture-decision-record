# Metryki, monitory, alerty

Spis treści:

* [Podsumowanie](#podsumowanie)
  * [Problem](#problem)
  * [Decyzja](#decyzja)
  * [Status](#status)
* [Szczegóły](#szczegóły)
  * [Założenia](#założenia)
  * [Ograniczenia](#ograniczenia)
  * [Stanowiska](#stanowiska)
  * [Argument](#argument)
  * [Implikacje](#implikacje)
* [Powiązane](#powiązane)
  * [Powiązane decyzje](#powiązane-decyzje)
  * [Powiązane wymagania](#powiązane-wymagania)
  * [Powiązane artefakty](#powiązane-artefakty)
  * [Powiązane zasady](#powiązane-zasady)
* [Notatki](#notatki)
  * [Wiadomości tekstowe w dowolnej formie a ustrukturyzowane komunikaty zdarzeń](#wiadomości-tekstowe-w-dowolnej-formie-a-ustrukturyzowane-komunikaty-zdarzeń)
  * [Graylog jest łatwiejszy](#graylog-jest-łatwiejszy)
  * [Prometheus wymaga dostrojenia](#prometheus-wymaga-dostrojenia)
  * [Usługi AWS dają mieszane wrażenia](#usługi-aws-dają-mieszane-wrażenia)
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


## Podsumowanie


### Problem

Chcemy używać metryk, monitorów i alertów, ponieważ chcemy wiedzieć, jak dobrze działają nasze aplikacje, i wiedzieć, kiedy pojawia się problem.


### Decyzja

W toku (WIP).


### Status

Zbieranie informacji. Zaczynamy od prawdopodobnych krańców spektrum: najczęściej polecanego starszego bezpłatnego narzędzia (Nagios) i najczęściej polecanego nowszego płatnego narzędzia (New Relic).


## Szczegóły


### Założenia

Chcemy tworzyć aplikacje internetowe, które są nowoczesne, szybkie, niezawodne, responsywne itd.

Chcemy kupować, a nie budować.


### Ograniczenia

Chcemy narzędzi, które dobrze współpracują z naszym potokiem devops i z naszymi chmurami wdrożeniowymi.


### Stanowiska

Obecnie badamy stanowiska.


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

Jak dotąd Nagios i New Relic są krańcami spektrum. Nagios jest najstarszym, najprostszym, bezpłatnym, realnym narzędziem. New Relic jest narzędziem o najnowszych funkcjach, najpełniejszym, płatnym, realnym. Zaczniemy od oceny tych dwóch. W razie potrzeby przejdziemy do środka spektrum.  

Jak dotąd Zabbix ma najlepsze rekomendacje i oferuje też najpełniejsze możliwości.

Jak dotąd ELK ma najlepszą popularność wśród rozwiązań open source budowanych zamiast kupowanych.

Jak dotąd Prometheus + Grafana mają najlepszą popularność.


### Implikacje

Do zrobienia.


## Powiązane


### Powiązane decyzje

Wybory wpłyną na testowalność, telemetrię i prawdopodobnie inne systemy, takie jak obsługa klienta, inżynieria niezawodności witryn (SRE) itd.


### Powiązane wymagania

Do zrobienia.


### Powiązane artefakty

Do zrobienia.


### Powiązane zasady

Łatwo odwracalne.

Potrzeba szybkości.


## Notatki


Całkiem dobry stos open source to:

* Prometheus do metryk i alertów opartych na metrykach

* Grafana do wyświetlania metryk

* Elasticsearch/Logstash/Kibana (ELK) do logów i ustrukturyzowanych zdarzeń

* Pushover do powiadomień mobilnych


### Wiadomości tekstowe w dowolnej formie a ustrukturyzowane komunikaty zdarzeń

Wiadomości tekstowe w dowolnej formie: na przykład takie przypadkowe rzeczy, jakie znajdziesz w /var/log/messages, oraz coś, co jest generowane celowo przez aplikację. Te wiadomości są przydatne do identyfikowania innych zdarzeń na maszynie, takich jak brak pamięci lub błędy sprzętowe, ale zawierają dużo śmieci. 

Ustrukturyzowane komunikaty zdarzeń: generowane przez aplikację, ze stałym lub dynamicznym zestawem atrybutów, np. log żądań HTTP, log księgowy, logowanie użytkownika.

Ogólnie rzecz biorąc, dobrze jest logować szczegóły każdego żądania w sposób, który pozwala drążyć na podstawie atrybutów. Dodanie np. identyfikatora użytkownika lub sesji do wszystkiego umożliwia śledzenie. Jawne śledzenie (tracing) jest oczywiście również dobre. Użycie ELK do tego celu to w pewnym sensie ubogi odpowiednik https://www.honeycomb.io/


### Graylog jest łatwiejszy

Z mojego doświadczenia Graylog łatwiej uruchomić.



### Prometheus wymaga dostrojenia


Ogólnie jestem zadowolony z Prometheusa do metryk. Alerty wymagają dostrojenia, ale są całkiem dobre. To zależy od aplikacji. Uważam, że najlepiej alertować o warunkach widocznych dla użytkownika końcowego, a nie o przyczynach leżących u podstaw. Na przykład czas ładowania strony jest dobry, liczba żądań na sekundę nie. Choć zero żądań na sekundę wskazuje, że coś jest nie tak.

Zaletą usługi jest to, że oferuje dodatkową inteligencję od razu po wyjęciu z pudełka. Ogólnie lubię Datadog. Usługi mogą być przerażająco drogie, jeśli masz dużo danych, a czasem mają modele cenowe, które nie są przyjazne chmurze, np. naliczanie za instancję, gdy instancje są dynamiczne. Jest też różnica między usługami, w których każde żądanie pochodzi od płacącego użytkownika, a tymi związanymi z reklamą, w których tylko niewielki procent żądań przynosi pieniądze. Możesz skończyć z dużą ilością danych i niewielkim budżetem.

Pracuję nad usługami, które obsługują 1 mld żądań dziennie, więc sensowne jest hostowanie własnego monitoringu i logowania. Jeśli Twoje wolumeny są mniejsze, łatwiejsze są usługi hostowane.


### Usługi AWS dają mieszane wrażenia

Moje doświadczenia z usługami AWS są mieszane. Ich usługa Elasticsearch była zawodna, więc uruchamiamy własne instancje. Metryki CloudWatch są drogie, więc zwykle używamy ich tylko dla metryk poziomu „infrastruktury”, a nie aplikacji, czyli metryk związanych ze zdrowiem, w których AWS może wiedzieć lepiej, co się dzieje, niż oprogramowanie działające na instancji. Logi CloudWatch mogą być wolno aktualizowane i nie mają zbyt wielu metadanych. Uruchomienie ELK w tym pomaga. Jeśli naprawdę chcę danych w czasie rzeczywistym, lepiej użyć Kafki jako transportu logów. Jest to dobrze wspierane przez Logstash. Zarządzanie klastrem Kafka nie jest jednak dla osób o słabych nerwach, jest tam dużo odsłoniętej instalacji.


### Kafka

Komentarz: Kafka bywa czasem bardzo podchwytliwa albo może być solidna jak skała, tak że prawie zapominasz, że tam jest i wszystko spina. 


Komentarz: Kafka była solidna, ale uruchomienie jej wymagało zaskakująco dużo pracy. Myślę o niej jak o relacyjnej bazie danych, w której pracuje się tylko na warstwie „fizycznej”, np. przestrzenie tabel, pliki i partycje. Na początku bywały momenty, gdy brakowało narzędzi do zarządzania i musieliśmy pisać programy, np. do resetowania grupy konsumentów. http://howfuckedismydatabase.com/nosql/

Komentarz: Używamy Kafki jako „bufora” dla komunikatów logów i miejsca, w którym możemy przetwarzać strumieniowo w czasie rzeczywistym dane pochodzące z wielu serwerów. Jeśli dojdzie do ataku DDOS, potrzebujemy sposobu analizowania danych z wielu instancji. Jeśli logujemy bezpośrednio z serwerów do ELK, obciążenie może przeciążyć klaster Elasticsearch.

Komentarz: Kafka jest dla nas dobra, ponieważ jeśli dojdzie do ataku DDOS, potrzebujemy sposobu analizowania danych z wielu instancji. Jeśli logujemy bezpośrednio z serwerów do ELK, obciążenie może przeciążyć klaster Elasticsearch.


Komentarz: Kafka wykonuje mniej pracy i jest wydajniejsza, więc lepiej radzi sobie z obciążeniem. A pracę Kafki kolejkujemy i ponawiamy. Przeciążenie Kafki nie wpływa na użytkowników, którzy próbują interaktywnie pracować w Kibanie, tak jak byłoby, gdyby Elasticsearch miał trudności.

Komentarz:  Przetwarzanie strumieniowe polega głównie na szukaniu nadużyć, np. zbyt dużego ruchu z jednego IP w całym klastrze, a następnie współdzieleniu blokady w całym klastrze.

Komentarz: Wtyczka logstash-output-kafka jest jednak obecnie dość zawodna. Dotknęło mnie kilka problemów ze strony jej zgłoszeń na GitHubie, które chyba nigdy nie są naprawiane. Chcę przestać jej używać i wysyłać dane bezpośrednio z naszych aplikacji do Kafki.

Komentarz: Teraz wysyłamy ustrukturyzowane zdarzenia bezpośrednio z aplikacji do Kafki. Główną motywacją było rzadsze dotykanie danych logów i unikanie wielokrotnego odczytu i zapisu na dysku. W systemach o dużym wolumenie logowanie może wymagać więcej pracy niż sama aplikacja. Myślę o tym, by journald także wysyłał logi bezpośrednio, z programu w C.


### Loki

Miej Lokiego na oku. Nie jest jeszcze gotowy, ale gdy będzie, spodziewam się, że lepiej pasowałby do tego stosu. Loki to agregator logów stworzony przez Grafana Labs, używa podobnej do Prometheusa składni zbierania danych i tagów.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager do metryk. <3 Prometheus.

Rollbar/Graylog do logowania/raportowania błędów (jest tu pewne nakładanie się; mała usługa prawdopodobnie nie potrzebuje obu).

Obecnie alerty trafiają po prostu na jeden z kilku kanałów Slack, w których zainteresowane strony mają włączone powiadomienia. Gdybyśmy poważniej traktowali dyżury (on-call), trafiałyby do PagerDuty/VictorOps itp.

Grafana do wykresów i pulpitów. Z niecierpliwością czekam też na to, czy ich nadchodzące funkcje logowania zastąpią Graylog.


### Thanos

Używamy Thanosa jako front-endu naszej konfiguracji HA. Potrafi deduplikować pary HA.

Obecnie przechowujemy 6 miesięcy lokalnych danych Prometheusa. Działa to dla nas rozsądnie dobrze. Jestem jednak w trakcie wdrażania magazynu bucket w naszej konfiguracji Thanos do długoterminowego przechowywania danych. Teoretycznie magazyn GCS będzie około 30% tańszy niż standardowy dysk trwały GCE, którego używamy teraz.

Obecnie nie robimy kopii zapasowych danych Prometheusa. Dane nie są dla nas zbyt ważne poza tym, by było ich dość do alertowania. Nasze ogólne wdrożenie floty zmienia się tak bardzo z roku na rok, że dane historyczne starsze niż kilka miesięcy nie są szczególnie interesujące. Interesujące mogłoby być kilka podstawowych statystyk rok do roku; mogę skonfigurować zestaw reguł nagrywania podstawowych statystyk i przechowywać je przez Federation albo po prostu zostawić to Thanosowi.

EDIT: Małe zastrzeżenie: jestem programistą Prometheusa.


### Prometheus HA

HA w Prometheusie realizuje się przez duplikację — uruchamiasz wiele instancji zbierających dane i są sposoby, by odpytywać wiele z nich i deduplikować dane

Skalowanie polega na podziale sieci i odpytywaniu różnych części sieci przez różne instancje Prometheusa

Długoterminowe przechowywanie nie jest mocną stroną Prometheusa, ale jest przenoszone do czegoś takiego jak Influx czy timescaledb (który technicznie też spełnia wymóg HA) artykuł, który o tym czytałem https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Nie próbowałem jeszcze rozwiązań długoterminowych, bo nadal tylko eksperymentuję i używam go do krótkoterminowych wykresów, podczas gdy librenms monitoruje moją sieć w długim okresie


###  Datadog + PagerDuty + Threat Stack

Używamy Datadog (z PagerDuty) i Threat Stack i nie moglibyśmy być szczęśliwsi. Moje jedyne zastrzeżenie do DD to stosunkowo wysoki koszt przechowywania metryk.


### Zabbix

Zabbix z własnymi skryptami do monitorowania niemal wszystkiego. Działa jak złoto.


### Outlyer

Używam Outlyera, ale muszę zastrzec, że tu pracuję, a używanie własnego produktu to konieczność.

Do wzbogacenia nadal potrzebuję Graylog, Sentry i Statuscake.

Brzmi stronniczo, ale po szczęśliwym uruchamianiu Nagiosa i innych systemów monitoringu wewnętrznie w każdej nowej pracy kupiłbym rozwiązanie hostowane i pozbył się tego bólu.


### Nagios + Nagiosgraph

Używamy Nagiosa do całego monitoringu i alertów. Alerty przychodzą e-mailem (ostrzeżenia i powiadomienia krytyczne) oraz dźwiękowymi powiadomieniami aplikacji (dla alertów krytycznych).

Nagiosgraph służy do wizualizacji.

Ta konfiguracja bardzo skutecznie na bieżąco informuje nas o tym, co dzieje się w naszym środowisku. Uruchamiamy i monitorujemy około 110 serwerów krytycznych dla działalności i około 760 punktów danych, a ten system działa u nas od ponad siedmiu lat.

Chciałbym też w pewnym momencie agregować logi za pomocą Graylog lub ELK.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager za pomocą wspaniałego wykresu helm Prometheus Operator. Logi nadal trafiają do planu birch LogDNA, ponieważ zauważyliśmy, że ELK jest zbyt ciężki dla naszego skromnego klastra z min. 3 i maks. 5 węzłami na GKE.


### DataDog + Sentry + PagerDuty.

Kiedyś uruchamiałem własne rozwiązania monitoringu, używając różnego oprogramowania, w tym Nagios, Icinga, Zabbix, ELK, Greylog2, Influx i wielu innych narzędzi, ale prawda jest taka, że prowadzenie własnej infrastruktury monitoringu wymaga zbyt dużo wysiłku, zwłaszcza gdy można zapłacić komuś innemu tak niskie stawki, by zrobił to za nas!

Płacenie innym za prowadzenie infrastruktury monitoringu pozwala moim klientom skupić się na prowadzeniu swoich platform zamiast na monitorowaniu monitoringu, co oznacza, że wartość, jaką zyskują dzięki stabilności swojej platformy, znacznie przewyższa wszelkie koszty monitoringu jako usługi.


### Sensu + Graphite + ELK

Moja firma bardzo stawia na rozwiązania hostowane we własnym zakresie.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager do alertów; mój zespół uważa, że prosty monitoring to dobry monitoring.

Inne systemy, takie jak logowanie i śledzenie, zapewniają bogaty kontekst do diagnozy, gdy dyżurny otrzyma alert, ale nigdy nie budujemy na nich alertów.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Usługi zinstrumentowane Prometheusem => analityka i wizualizacja Circonus


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Używamy poniższych usług:

icinga2 do monitoringu i VictorOps do alertów

NewRelic do szczegółowego monitoringu usługi

Sentry do śledzenia błędów w usłudze

Slack/e-mail jako część alertów wyzwalanych z NewRelic lub icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 z integracją elasticsearch do analizy i integracją graphite+grafana do wykresów.

dzięki elastyczności reguł apply w icinga2 programiści widzą tylko te usługi, o których otrzymują powiadomienia.

a dzięki icinga2 director programiści mogą łatwo definiować własne kontrole (co robią co kilka dni — 100 kontroli wychodzi, 100 innych wchodzi) na dużą skalę bez żadnego kłopotu.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Co mamy teraz:

DataDog do metryk

New Relic do monitoringu aplikacji

ELK (Elastic Search + Logstash + Kibana) do logów

Sentry (hostowany samodzielnie) do logowania wyjątków

E-maile + Slack + VictorOps do alertów (w zależności od wagi)

Co chcemy mieć:

Prometheus do metryk (Grafana do wizualizacji)

New Relic (prawdopodobnie Elastic Search APM) do monitoringu aplikacji

EFK (elastic search + fluentd + kibana) do logowania. Prawdopodobnie Loki od Grafana będzie gotowy do produkcji, zanim do tego dojdziemy

Sentry do wyjątków

Alertmanager + e-mail + VictorOps do alertów


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Zastrzeżenie: pracuję w VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf do metryk serwera, takich jak CPU, dysk, pamięć i sieć. Telegrafa używamy też do monitoringu SNMP naszych urządzeń sieciowych.

Prometheus do metryk aplikacji. Wbudowujemy w naszą aplikację kontrole stanu, które Prometheus zbiera.

InfluxDB do przechowywania szeregów czasowych. Tam trafiają dane z Telegrafa.

Grafana do pulpitów i alertów. Silnik alertów nie jest super solidny, ale spełnia swoje zadanie. Wysyłamy też alerty do Slacka.

Czego teraz nie mam, to scentralizowanego rozwiązania do logowania. ELK jest potężny, ale trudny do skonfigurowania i zarządzania, a nie znam żadnych bezpłatnych alternatyw, które byłyby na tyle zbliżone, by je zbadać.


### Sematext + Logagent + Experience

Sematext do metryk, logów, śladów, wkrótce także do monitoringu rzeczywistych użytkowników. Prościej/taniej niż używanie N różnych narzędzi/usług, moim zdaniem.

Do przesyłania logów używaliśmy rsyslog, a potem przeszliśmy na Logagent.

Do raportowania awarii front-endu używamy Sentry, ale wkrótce przejdziemy na Experience.

Zastrzeżenie: jestem Sematextanem (pracownikiem Sematext).


### Azure Monitor/Analytics + OpsGenie

Chciałbym, żeby Log Analytics miał lepszy interfejs. Odchodzimy od Splunka, po którym było dużo łatwiej się poruszać.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Naprawdę nie chcesz uruchamiać własnego systemu powiadomień. Splunk możesz zastąpić ELK, chyba że Twój zespół bezpieczeństwa preferuje Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf jako kolektor, Prometheus + Alertmanager do monitoringu i alertów, zintegrowane z kanałami Slack i pagerduty dla alertów krytycznych. Grafana do wizualizacji metryk hostów.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus do metryk + alertów

Grafana do pulpitów Prometheusa

Cloudwatch monitorujący instancje Prometheusa

sentry do śledzenia wyjątków

kibana + elasticsearch

graylog

prometheus Push Gateway dla zadań wsadowych/cronjobów

SOP https://github.com/rapidloop/sop do „wypychania/przekazywania“ metryk z jednej instancji Prometheusa do drugiej

klienci używają klientów Prometheusa. Po stronie klienta staramy się używać opencensus.io


### PagerDuty + Monitis

PagerDuty + Monitis. Także kilka własnych Azure Functions do testowania stanu niektórych usług.

W tym roku chcemy wprowadzić Prometheus i Grafana


### Prometheus + Grafana + Bosun

Prometheus do przechowywania danych szeregów czasowych. Grafana do wizualizacji. Bosun do zarządzania alertami.


### Azure Monitor/Analytics/Insights/Dashboards

Firma tylko na Azure: Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana do monitorowania usług kontenerowych w Kubernetes przez Prometheus

Monitis do monitoringu usług end-to-end, głównie dla API internetowych i aplikacji internetowych

OpsGenie do zarządzania alertami

Slack do otrzymywania informacji o statusie naszych systemów


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Jestem od dawna inżynierem (dev)ops. Wychowałem się na Nagiosie. Chętnie poznam opinie o moim bootstrapowanym SaaS https://checklyhq.com. Zajmujemy się monitoringiem API i transakcji w witrynach z dość rozbudowanymi alertami.

Założyłem Checkly, ponieważ aktywny / syntetyczny monitoring w przestrzeni API był nieco ograniczony (i drogi). Monitoring oparty na przeglądarce / skryptach jest jeszcze bardziej zamknięty i drogi. Używamy Puppeteera i utrzymujemy ceny jak najniższe.

Nasz stos monitoringu:

Checkly (używamy własnego produktu...)

AppOptics (własne wykresy)

AWS Cloudwatch i SNS do wiadomości SMS.

wbudowane alerty Heroku.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana powiadamia nas na Slacku o problemach z infrastrukturą lub spadku wydajności, a logz.io skonfigurowaliśmy tak, by alertował na Slacku przy określonym wolumenie logów poziomu błędu z warstwy aplikacji.


### SignalFX + Splunk + PagerDuty + Slack

Obecnie używamy: SignalFX, Splunk, PagerDuty i Slack. Nie jestem wielkim fanem SignalFX, choć ich zespół wsparcia jest super przyjazny i szybko reaguje. Lubię Splunk (warto, jeśli możesz za niego zapłacić), PagerDuty i Slack.

Kiedyś używałem stosu TICK, w którym większość C była tak naprawdę G, czyli Grafana, choć trochę używałem też Chronografa. Było świetnie, ale kłopotliwie w zarządzaniu. Klasyczny dylemat SaaS kontra własny hosting.

Używałem DataDog, New Relic, Graylog, ELK i BugSnag. Bardzo lubię DataDog i New Relic, Graylog jest całkiem dobry. Nie jestem wielkim fanem ELK. BugSnag jest fajny, właściwie uważam, że śledzenie błędów/wyjątków w wielu przypadkach jest całkiem dobrym zamiennikiem pełnego monitoringu logów.


### ELK + Prometheus + Grafana

Tak jak inni, używamy ELK do logów, a Prometheus+Grafana do wszystkiego innego.

Utrzymanie tej konfiguracji jest łatwe, jeśli pozwolisz sobie na okazjonalną utratę danych. Na przykład jeśli nasza baza ElasticSearch wpadnie w kłopoty (co niestety zdarza się nam co 2–3 miesiące), nie bawimy się w HA, tylko zrzucamy dane i idziemy dalej. Jeśli absolutnie musisz mieć HA lub długoterminowe przechowywanie, powodzenia.


### Datadog + Prometheus + Grafana

Skonfigurowałem Datadog w abonamencie miesięcznym, ponieważ gdy tu przyszedłem, nie było monitoringu ani alertów. Tylko kilka naszych witryn było monitorowanych co 5 minut pod kątem dostępności. Datadog jest bezsprzecznie najłatwiejszy w konfiguracji. Gdy skończę zajmować się wszystkimi innymi problemami, przejdę na Prometheus+Grafana. Nie jestem jeszcze w 100% zdecydowany co do zarządzania logami.

### Nagios + ELK

Wspieramy ponad 100 produktów.

Lokalnie to głównie Nagios i ELK. W chmurze migrujemy z DataDog do NewRelic.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Kiedyś używaliśmy datadog, ale okazał się zbyt drogi jak na nasze potrzeby. Nie zrozumcie mnie źle, jest świetny, ale ma ogromny koszt. Udało nam się skonfigurować site24x7.com z rocznym abonamentem za około 2–3 miesiące kosztów DD.

Nasz stos monitoringu:

Site24x7 - APM, monitoring zewnętrznych adresów URL, monitoring przepływu poczty SMTP, wygasanie certyfikatów ssl i monitoring procesów.

StatusCake - do monitoringu i potwierdzania adresów URL - to nasza kopia zapasowa na wypadek, gdyby site24x7 coś przeoczył (nie przeoczy), ale SC jest elastyczniejszy w monitoringu zewnętrznych portów i usług na nasze potrzeby.

Oba narzędzia eskalują do PagerDuty, a potem eskalacje dostajemy na Slacku.

SumoLogic - do monitoringu logów (to świetne narzędzie, ale trochę skomplikowane jak na nasze potrzeby)

Ze Slacka możemy potwierdzić alert lub go naprawić.

Mamy też wiele automatyzacji site24x7, które łączą się z commando.io dla „BedOps”, jak to nazywamy — gdy zostanie wyzwolony alert, uruchamiamy kilka skryptów lub automatyzacji w próbie naprawienia sytuacji (w 99% przypadków automatyzacja + nasze skrypty chronią nas przed kłopotami).

Mamy wewnętrzne runbooki w naszej bazie wiedzy na wypadek, gdy automaty zawiodą lub gdy coś wykracza poza zakres i trzeba to naprawić.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana do metryk w naszych klastrach GKE i maszynach wirtualnych.

Google Stackdriver do logów (ponieważ jest wliczony i domyślnie aktywny, a obecnie wystarcza na nasze potrzeby).


### Zabbix

Zabbix do wszystkiego. Nie potrzeba żadnego dodatkowego oprogramowania.


