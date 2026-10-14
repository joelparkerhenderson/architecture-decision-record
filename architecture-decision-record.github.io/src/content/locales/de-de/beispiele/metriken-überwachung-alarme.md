# Metriken, Überwachung, Alarme

Inhalt:

* [Zusammenfassung](#zusammenfassung)
  * [Problem](#problem)
  * [Entscheidung](#entscheidung)
  * [Status](#status)
* [Details](#details)
  * [Annahmen](#annahmen)
  * [Einschränkungen](#einschränkungen)
  * [Positionen](#positionen)
  * [Argument](#argument)
  * [Implikationen](#implikationen)
* [Zugehöriges](#zugehöriges)
  * [Zugehörige Entscheidungen](#zugehörige-entscheidungen)
  * [Zugehörige Anforderungen](#zugehörige-anforderungen)
  * [Zugehörige Artefakte](#zugehörige-artefakte)
  * [Zugehörige Prinzipien](#zugehörige-prinzipien)
* [Notizen](#notizen)
  * [Freitext-Nachrichten gegenüber strukturierten Ereignisnachrichten](#freitext-nachrichten-gegenüber-strukturierten-ereignisnachrichten)
  * [Graylog ist einfacher](#graylog-ist-einfacher)
  * [Prometheus braucht etwas Feinabstimmung](#prometheus-braucht-etwas-feinabstimmung)
  * [AWS-Dienste sind gemischt](#aws-dienste-sind-gemischt)
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
  * [Datadog gegenüber Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack](#datadog-gegenüber-site24x7--statuscake--pagerduty--sumologic--slack)
  * [Prometheus + AlertManager + Grafana + Stackdriver](#prometheus--alertmanager--grafana--stackdriver)
  * [Zabbix](#zabbix-1)


## Zusammenfassung


### Problem

Wir möchten Metriken, Überwachung und Alarme nutzen, weil wir wissen möchten, wie gut unsere Anwendungen funktionieren, und wissen möchten, wann es ein Problem gibt.


### Entscheidung

WIP.


### Status

Informationen werden gesammelt. Wir beginnen mit den plausiblen Enden des Spektrums: dem am meisten empfohlenen älteren kostenlosen Werkzeug (Nagios) und dem am meisten empfohlenen neueren kostenpflichtigen Werkzeug (New Relic).


## Details


### Annahmen

Wir möchten Webanwendungen erstellen, die modern, schnell, zuverlässig, responsiv usw. sind.

Wir möchten kaufen statt bauen.


### Einschränkungen

Wir möchten Werkzeuge, die gut mit unserer DevOps-Pipeline und mit unseren Bereitstellungs-Clouds funktionieren.


### Positionen

Wir recherchieren derzeit Positionen.


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

Bisher sind Nagios und New Relic die Enden des Spektrums. Nagios ist das älteste, einfachste, kostenlose, tragfähige Werkzeug. New Relic ist das Werkzeug mit den neuesten Funktionen, das vollständigste, kostenpflichtige, tragfähige Werkzeug. Wir beginnen mit Bewertungen dieser beiden. Nach Bedarf bewegen wir uns in das Spektrum hinein.  

Bisher hat Zabbix die besten Empfehlungen und bietet auch die vollständigsten Fähigkeiten.

Bisher hat ELK die beste Beliebtheit bei Open Source, selbst bauen statt kaufen.

Bisher haben Prometheus + Graphana die beste Beliebtheit.


### Implikationen

TODO.


## Zugehöriges


### Zugehörige Entscheidungen

Die Auswahl beeinflusst Testbarkeit, Telemetrie und wahrscheinlich andere Systeme, etwa für den Kundenservice, Site Reliability Engineering usw.


### Zugehörige Anforderungen

TODO.


### Zugehörige Artefakte

TODO.


### Zugehörige Prinzipien

Leicht umkehrbar.

Bedarf an Geschwindigkeit.


## Notizen


Ein ziemlich guter Open-Source-Stack ist:

* Prometheus für Metriken und auf Metriken basierende Alarmierung

* Grafana zur Anzeige von Metriken

* Elasticsearch/Logstash/Kibana (ELK) für Protokolle und strukturierte Ereignisse

* Pushover für mobile Benachrichtigungen


### Freitext-Nachrichten gegenüber strukturierten Ereignisnachrichten

Freitext-Nachrichten: zum Beispiel die Art von zufälligem Zeug, das Sie in /var/log/messages finden, und etwas, das von der Anwendung absichtlich erzeugt wird. Die Nachrichten sind nützlich, um andere Dinge zu erkennen, die auf der Maschine geschehen, etwa Speichermangel oder Hardwarefehler, enthalten aber viel Müll. 

Strukturierte Ereignisnachrichten: von der Anwendung erzeugt, mit einem festen oder dynamischen Satz von Attributen, z. B. ein HTTP-Anfrageprotokoll, ein Buchhaltungsprotokoll, eine Benutzeranmeldung.

Allgemein ist es schön, Details zu jeder Anfrage so zu protokollieren, dass man anhand von Attributen in die Tiefe gehen kann. Wenn man also z. B. eine userid oder sessionid zu allem hinzufügt, kann man nachverfolgen. Explizites Tracing ist natürlich ebenfalls gut. ELK dafür zu verwenden, ist eine Art Honeycomb für Arme: https://www.honeycomb.io/


### Graylog ist einfacher

Graylog ist nach meiner Erfahrung einfacher aufzusetzen.



### Prometheus braucht etwas Feinabstimmung


Ich bin mit Prometheus für Metriken im Allgemeinen zufrieden. Die Alarmierung braucht etwas Feinabstimmung, ist aber ziemlich gut. Das hängt von Ihrer Anwendung ab. Ich denke, es ist am besten, auf für Endbenutzer sichtbare Zustände zu alarmieren, nicht auf zugrunde liegende Ursachen. Zum Beispiel ist die Seitenladezeit gut, die Anzahl der Anfragen pro Sekunde nicht. Allerdings deutet null Anfragen pro Sekunde darauf hin, dass etwas nicht stimmt.

Der Vorteil eines Dienstes ist, dass er zusätzliche Intelligenz von Haus aus bietet. Ich mag im Allgemeinen Datadog. Die Dienste können beängstigend teuer sein, wenn man viele Daten hat, und haben manchmal Preismodelle, die nicht Cloud-freundlich sind, z. B. Abrechnung pro Instanz, obwohl Instanzen dynamisch sind. Es gibt auch einen Unterschied zwischen Diensten, bei denen jede Anfrage von einem zahlenden Benutzer kommt, und solchen mit Werbebezug, bei denen nur ein kleiner Prozentsatz der Anfragen Geld einbringt. Man kann am Ende viele Daten und nicht so viel Budget haben.

Ich arbeite an einigen Diensten, die täglich 1 Mrd. Anfragen erhalten, daher ist es sinnvoll, Überwachung und Protokollierung selbst zu hosten. Wenn Ihre Volumina niedriger sind, sind gehostete Dienste einfacher.


### AWS-Dienste sind gemischt

Meine Erfahrung mit AWS-Diensten ist gemischt. Ihr Elasticsearch-Dienst war unzuverlässig, daher betreiben wir dafür eigene Instanzen. CloudWatch-Metriken sind teuer, daher verwenden wir sie im Allgemeinen nur für Metriken auf „Infrastruktur“-Ebene statt für die Anwendung, das heißt, gesundheitsbezogene Metriken, bei denen AWS besser wissen kann, was vor sich geht, als die auf der Instanz laufende Software. CloudWatch Logs können langsam aktualisiert werden und haben nicht so viele Metadaten. Der Betrieb von ELK hilft dabei. Wenn ich wirklich Echtzeitdaten will, ist es besser, Kafka als Transport für Protokolle zu verwenden. Das wird von Logstash ziemlich gut unterstützt. Einen Kafka-Cluster zu verwalten ist allerdings nichts für schwache Nerven, da liegt viel Installation offen.


### Kafka

Kommentar: Kafka kann manchmal äußerst knifflig sein, oder Kafka kann so felsenfest sein, dass man fast vergisst, dass es da ist und alles zusammenhält. 


Kommentar: Kafka war solide, aber es war überraschend viel Arbeit, es zum Laufen zu bringen. Ich betrachte es wie eine relationale Datenbank, aber man arbeitet nur auf der „physischen“ Ebene, z. B. Tablespaces, Dateien und Partitionen. Zu Beginn gab es Zeiten, in denen die Verwaltungswerkzeuge fehlten, und wir mussten Programme schreiben, um z. B. eine Consumer-Gruppe zurückzusetzen. http://howfuckedismydatabase.com/nosql/

Kommentar: Wir nutzen Kafka als „Puffer“ für Protokollnachrichten und als Ort, an dem wir Echtzeit-Stream-Verarbeitung auf Daten durchführen können, die von mehreren Servern kommen. Wenn wir einen DDOS-Angriff bekommen, brauchen wir eine Möglichkeit, Daten über mehrere Instanzen hinweg zu analysieren. Wenn wir direkt von den Servern nach ELK protokollieren, kann die Last den Elasticsearch-Cluster sprengen.

Kommentar: Kafka ist gut für uns, weil wir bei einem DDOS-Angriff eine Möglichkeit brauchen, Daten über mehrere Instanzen hinweg zu analysieren. Wenn wir direkt von den Servern nach ELK protokollieren, kann die Last den Elasticsearch-Cluster sprengen.


Kommentar: Kafka leistet weniger Arbeit und ist effizienter und kann daher die Last besser bewältigen. Und wir stellen die Kafka-Arbeit in eine Warteschlange und versuchen es erneut. Und eine Überlastung von Kafka beeinträchtigt keine Benutzer, die versuchen, interaktiv mit Kibana zu arbeiten, wie es der Fall wäre, wenn Elasticsearch kämpft.

Kommentar:  Die Stream-Verarbeitung sucht hauptsächlich nach Missbrauch, z. B. zu viel Verkehr von einer einzelnen IP im gesamten Cluster, und teilt dann die Sperre im gesamten Cluster.

Kommentar: Das Plugin logstash-output-kafka ist derzeit allerdings ziemlich unzuverlässig. Ich bin von mehreren der Probleme auf seiner GitHub-Issues-Seite betroffen gewesen, die nie behoben zu werden scheinen. Ich möchte davon wegkommen und direkt aus unseren Apps an Kafka senden.

Kommentar: Wir senden jetzt strukturierte Ereignisse direkt aus der App an Kafka. Die Hauptmotivation war, die Protokolldaten seltener anzufassen und mehrfaches Lesen und Schreiben der Festplatte zu vermeiden. In Systemen mit hohem Volumen kann die Protokollierung mehr Arbeit machen als die App selbst. Ich überlege, auch journald Protokolle direkt senden zu lassen, aus einem C-Programm.


### Loki

Behalten Sie Loki im Auge. Es ist noch nicht bereit, aber wenn es so weit ist, erwarte ich, dass es in diesen Stack besser passt. Loki ist ein von Grafana Labs erstellter Protokoll-Aggregator, der eine ähnliche Scraping- und Tag-Syntax wie Prometheus verwendet.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager für Metriken. Ich liebe Prometheus.

Rollbar/Graylog für Protokollierung/Fehlerberichte (hier gibt es etwas Überschneidung; ein kleiner Dienst braucht wahrscheinlich nicht beides).

Derzeit gehen Alarme nur an einen von wenigen Slack-Kanälen, für die interessierte Parteien Benachrichtigungen aktiviert haben. Wenn wir es mit der Bereitschaft ernster nähmen, gingen sie an PagerDuty/VictorOps/usw.

Grafana für Graphen und Dashboards. Ich bin auch gespannt, ob ihre kommenden Protokollierungsfunktionen Graylog überflüssig machen werden.


### Thanos

Wir verwenden Thanos als Frontend für unsere HA-Einrichtung. Es weiß, wie man HA-Paare dedupliziert.

Wir halten derzeit 6 Monate lokale Prometheus-Daten vor. Das funktioniert für uns einigermaßen gut. Aber ich bin gerade dabei, Bucket-Speicher für langfristige Datenspeicherung in unserer Thanos-Einrichtung einzuführen. Theoretisch wird GCS-Speicher etwa 30 % günstiger sein als der GCE-Standard-Persistent-Disk, den wir derzeit verwenden.

Wir sichern Prometheus-Daten derzeit nicht. Die Daten sind für uns über das Vorhalten für die Alarmierung hinaus nicht wirklich wichtig. Unsere gesamte Flottenbereitstellung ändert sich von Jahr zu Jahr so stark, dass historische Daten, die älter als einige Monate sind, einfach nicht so interessant sind. Es könnte interessant sein, einige Kernstatistiken im Jahresvergleich zu haben, ich könnte einen Satz Aufzeichnungsregeln für Kernstatistiken einrichten und diese mit Federation speichern oder Thanos einfach machen lassen.

EDIT: Ein kleiner Hinweis, ich bin Prometheus-Entwickler.


### Prometheus HA

HA in Prometheus wird durch Duplizierung erreicht: Man betreibt mehrere Sammler, und es gibt Wege, mehrere abzufragen und die Daten zu deduplizieren.

Die Skalierung erfolgt, indem man das Netzwerk festlegt und verschiedene Prometheus-Instanzen verschiedene Teile des Netzwerks abfragen lässt.

Langzeitspeicherung ist nicht die Stärke von Prometheus, sondern wird auf etwas wie influx oder timescaledb ausgelagert (was technisch gesehen auch das HA-Häkchen setzt). Ein Artikel, den ich dazu gelesen habe: https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Den Langzeitteil habe ich noch nicht ausprobiert, da ich bisher nur experimentiere und es für kurzfristige Graphen nutze, während librenms mein Netzwerk langfristig überwacht


###  Datadog + PagerDuty + Threat Stack

Wir nutzen Datadog (mit PagerDuty) und Threat Stack und könnten nicht glücklicher sein. Mein einziger Kritikpunkt an DD sind die relativ hohen Kosten der Metrikspeicherung.


### Zabbix

Zabbix mit eigenen Skripten, um fast alles zu überwachen. Funktioniert wie ein Zauber.


### Outlyer

Ich nutze Outlyer, muss aber dazusagen, dass ich hier arbeite und das Essen des eigenen Hundefutters (Dogfooding) ein Muss ist.

Ich brauche zur Ergänzung weiterhin Graylog, Sentry und Statuscake.

Klingt voreingenommen, aber nachdem ich Nagios und andere Überwachungssysteme intern gern betrieben habe, würde ich in jedem neuen Job eine gehostete Lösung kaufen und diese Last abgeben.


### Nagios + Nagiosgraph

Wir betreiben Nagios für die gesamte Überwachung und Alarmierung. Alarme erfolgen per E-Mail (Warnungen und kritische Benachrichtigungen) und hörbare App-Benachrichtigungen (für kritische Alarme).

Nagiosgraph wird für Visualisierungen verwendet.

Diese Einrichtung war sehr wirksam, um uns umfassend über das Geschehen in unserer Umgebung auf dem Laufenden zu halten. Wir betreiben und überwachen etwa 110 geschäftskritische Server und etwa 760 Datenpunkte und haben dieses Morgensystem seit über sieben Jahren im Einsatz.

Ich würde irgendwann auch gern Protokolle mit Graylog oder ELk aggregieren.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager über das großartige Helm-Chart Prometheus Operator. Protokolle gehen weiterhin an den LogDNA-birch-Plan, da wir festgestellt haben, dass ELK für unseren bescheidenen Cluster mit min. 3 max. 5 Knoten auf GKE zu schwergewichtig ist.


### DataDog + Sentry + PagerDuty.

Ich habe früher alle meine Überwachungslösungen selbst betrieben, mit allen möglichen Softwarearten, darunter Nagios, Icinga, Zabbix, ELK, Greylog2, Influx und viele andere Werkzeuge, aber die Wahrheit ist, dass der Betrieb einer eigenen Überwachungsinfrastruktur einfach zu viel Aufwand bedeutet, besonders wenn man jemand anderen zu so niedrigen Preisen dafür bezahlen kann, das für einen zu erledigen!

Andere dafür zu bezahlen, die Überwachungsinfrastruktur zu betreiben, befreit meine Kunden, sich auf den Betrieb ihrer Plattformen zu konzentrieren, statt die Überwachung zu überwachen, das heißt, der Wert, den sie aus der Stabilität ihrer Plattform ziehen, übersteigt etwaige Kosten von Monitoring as a Service bei Weitem.


### Sensu + Graphite + ELK

Meine Firma setzt stark auf selbst gehostete Dinge.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager für Alarmierung, mein Team glaubt, dass einfache Überwachung gute Überwachung ist.

Andere Systeme wie Protokollierung und Tracing liefern reichen Kontext für die Diagnose, wenn die Bereitschaft einen Alarm erhält, aber wir bauen nie Alarmierung darauf auf.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Mit Prometheus instrumentierte Dienste => Circonus-Analytik und -Visualisierung


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Wir verwenden die folgenden Dienste:

icinga2 für die Überwachung und VictorOps für die Alarmierung

NewRelic für die Detailüberwachung des Dienstes

Sentry für die Fehlerverfolgung im Dienst

Slack/E-Mail ist Teil der Alarmierung, die von NewRelic oder icinga2 ausgelöst wird


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 mit Elasticsearch-Integration für Analysen und graphite+grafana-Integration für Graphen.

Dank der Flexibilität der Apply-Regeln in icinga2 können die Entwickler nur Dienste sehen, für die sie Benachrichtigungen erhalten.

Und über den icinga2 Director können Programmierer ihre eigenen Prüfungen leicht definieren (was sie alle paar Tage tun – 100 Prüfungen gehen raus, 100 andere Prüfungen kommen rein), in großem Maßstab ohne Aufwand.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Was wir jetzt haben:

DataDog für Metriken

New Relic für die Anwendungsüberwachung

ELK (Elastic Search + Logstash + Kibana) für die Protokolle

Sentry (selbst gehostet) zum Protokollieren von Ausnahmen

E-Mails + Slack + VictorOps für die Alarmierung (nach Schweregrad)

Was wir haben möchten:

Prometheus für Metriken (Grafana zur Visualisierung)

New Relic (wahrscheinlich Elastic Search APM) für die Anwendungsüberwachung

EFK (elastic search + fluentd + kibana) für die Protokollierung. Wahrscheinlich ist Loki von Grafana bis dahin produktionsreif

Sentry für die Ausnahmen

Alertmanager + E-Mail + VictorOps für die Alarme


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Hinweis: arbeitet bei VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf für Servermetriken wie CPU, Festplatte, Speicher und Netzwerk. Wir verwenden Telegraf auch für die SNMP-Überwachung unserer Netzwerkgeräte.

Prometheus für Anwendungsmetriken. Wir programmieren Health-Checks in unsere Anwendung, die Prometheus abfragt.

InfluxDB für Zeitreihenspeicherung. Dorthin werden unsere Telegraf-Daten gesendet.

Grafana für Dashboards und Alarme. Die Alarm-Engine ist nicht übermäßig robust, erledigt aber die Aufgabe. Wir senden Alarme auch an Slack.

Was ich derzeit nicht habe, ist eine zentrale Protokollierungslösung. ELK ist leistungsfähig, aber schwer einzurichten und zu verwalten, und ich kenne keine kostenlosen Alternativen, die nah genug dran sind, um sie sich anzusehen.


### Sematext + Logagent + Experience

Sematext für Metriken, für Protokolle, für Traces, bald auch für Real User Monitoring. Einfacher/billiger, als N verschiedene Werkzeuge/Dienste zu verwenden, meiner bescheidenen Meinung nach.

Für den Versand von Protokollen haben wir früher rsyslog verwendet und sind dann zu Logagent gewechselt.

Für Frontend-Absturzberichte nutzen wir Sentry, werden aber in Kürze zu Experience wechseln.

Hinweis: Ich bin Sematextaner.


### Azure Monitor/Analytics + OpsGenie

Ich wünschte, Log Analytics hätte eine bessere Oberfläche. Wir wandern von Splunk ab, das viel einfacher zu navigieren war.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Sie wollen wirklich kein eigenes Benachrichtigungssystem betreiben. Sie können Splunk durch ELK ersetzen, es sei denn, Ihr Sicherheitsteam bevorzugt Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf als Sammler, Prometheus + Alertmanager für Überwachung und Alarmierung, integriert mit Slack-Kanälen und PagerDuty für kritische Alarme. Grafana zur Visualisierung von Host-Metriken.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus für Metriken + Alarme

Grafana für Prometheus-Dashboards

Cloudwatch überwacht Prometheus-Instanzen

sentry für die Ausnahmeverfolgung

kibana + elasticsearch

graylog

Prometheus Push Gateway für Batch/Cronjobs

SOP https://github.com/rapidloop/sop, um Metriken von 1 Prometheus-Instanz an eine andere zu „pushen/weiterzuleiten“

Clients verwenden entweder die Prometheus-Clients. Wir versuchen, auf der Client-Seite opencensus.io zu verwenden


### PagerDuty + Monitis

PagerDuty + Monitis. Außerdem einige maßgeschneiderte Azure Functions zum Testen der Gesundheit einiger Dienste.

Hoffe, dieses Jahr Prometheus und Grafana einzuführen


### Prometheus + Grafana + Bosun

Prometheus zum Speichern der Zeitreihendaten. Grafana zur Visualisierung. Bosun für das Alarm-Management.


### Azure Monitor/Analytics/Insights/Dashboards

Reiner Azure-Betrieb, Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana zur Überwachung von Container-Diensten in Kubernetes über Prometheus

Monitis für die Ende-zu-Ende-Dienstüberwachung, hauptsächlich für Web-APIs und Webanwendungen

OpsGenie für das Alarm-Management

Slack, um Statusinformationen aus unseren Systemen zu erhalten


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Langjähriger (Dev-)Ops-Ingenieur hier. Mit Nagios aufgewachsen. Würde gern Meinungen zu meinem selbstfinanzierten SaaS https://checklyhq.com hören. Wir machen API-Überwachung & Überwachung von Website-Transaktionen mit ziemlich tiefgehender Alarmierung.

Ich habe Checkly gegründet, weil aktives / synthetisches Monitoring im API-Bereich etwas begrenzt (und teuer) war. Browserbasiertes / skriptgesteuertes Monitoring ist noch proprietärer und teurer. Wir nutzen Puppeteer und halten die Preise so niedrig wie möglich.

Unser Überwachungs-Stack:

Checkly (Dogfooding...)

AppOptics (individuelle Graphen)

AWS Cloudwatch & SNS für SMS-Nachrichten.

integrierte Heroku-Alarmierung.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana alarmiert uns in Slack bei Infrastrukturproblemen oder Leistungsabfall, und wir haben logz.io so konfiguriert, dass es in Slack bei einem bestimmten Volumen an Protokollen der Fehlerstufe aus der Anwendungsschicht alarmiert.


### SignalFX + Splunk + PagerDuty + Slack

Derzeit im Einsatz: SignalFX, Splunk, PagerDuty und Slack. Ich bin kein großer Fan von SignalFX, obwohl ihr Support-Team super freundlich und reaktionsschnell ist. Ich mag Splunk (lohnt sich, wenn man es bezahlen kann), PagerDuty und Slack.

Früher habe ich den TICK-Stack verwendet, bei dem das C eigentlich ein G war, nämlich Grafana, obwohl ich Chronograf ein wenig genutzt habe. Das war großartig, aber mühsam zu verwalten. Das klassische Dilemma SaaS gegenüber Selbst-Hosting.

Ich habe DataDog, New Relic, Graylog, ELK und BugSnag genutzt. DataDog und New Relic mag ich sehr, Graylog ist ziemlich gut. Ich bin kein großer ELK-Fan. BugSnag ist nett, ich habe tatsächlich das Gefühl, dass das Verfolgen von Fehlern/Ausnahmen in vielen Fällen ein ziemlich guter Ersatz für vollständige Protokollüberwachung ist.


### ELK + Prometheus + Grafana

Wie andere nutzen wir ELK für Protokolle und Prometheus+Grafana für alles andere.

Diese Einrichtung zu pflegen ist einfach, wenn man sich erlaubt, gelegentlich Daten zu verlieren. Wenn zum Beispiel unsere ElasticSearch-Datenbank in eine Krise gerät (was uns leider alle 2–3 Monate passiert), kümmern wir uns nicht um HA, sondern werfen die Daten weg und machen mit unserem Leben weiter. Wenn Sie unbedingt HA oder Langzeitaufbewahrung brauchen, viel Glück.


### Datadog + Prometheus + Grafana

Ich habe Datadog im Monatsabo eingerichtet, weil es, als ich hierher kam, keine Überwachung und keine Alarmierung gab. Nur ein paar unserer Websites wurden alle 5 Minuten auf Verfügbarkeit überwacht. Datadog ist mit Abstand am einfachsten einzurichten. Wenn ich alle anderen Probleme beseitigt habe, wechsle ich zu Prometheus+Grafana. Beim Protokollmanagement noch nicht zu 100 % entschieden.

### Nagios + ELK

Wir unterstützen über 100 Produkte.

Vor Ort ist es überwiegend Nagios und ELK. Für die Cloud wechseln wir von DataDog zu NewRelic.


### Datadog gegenüber Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Wir haben früher Datadog verwendet, fanden es aber für unsere Bedürfnisse viel zu teuer. Verstehen Sie mich nicht falsch, es ist großartig, aber es hat enorme Kosten. Wir konnten site24x7.com mit einem Jahresabo für etwa 2–3 Monate der Kosten von DD einrichten.

Unser Überwachungs-Stack:

Site24x7 - APM, Überwachung externer URLs, Überwachung des SMTP-Mailflusses, SSL-Ablauf und Prozessüberwachung.

StatusCake - für URL-Überwachung und Bestätigung - Es ist unsere Sicherung, falls site24x7 etwas verpasst (tut es nicht), aber SC ist für unsere Bedürfnisse flexibler bei der Überwachung externer Ports und Dienste.

Beide Werkzeuge eskalieren an PagerDuty, und dann erhalten wir unsere Eskalationen in Slack.

SumoLogic - für Protokollüberwachung (es ist ein großartiges Werkzeug, aber für unsere Bedürfnisse etwas kompliziert)

Von Slack aus können wir den Alarm bestätigen (ack) oder beheben.

Dann haben wir viele site24x7-Automatisierungen, die sich mit commando.io verbinden, für das, was wir ‚BedOps‘ nennen – wenn ein Alarm ausgelöst wird, starten wir einige Skripte oder Automatisierungen als Versuch, die Situation zu beheben (in 99 % der Fälle halten uns die Automatisierung + unsere Skripte aus Schwierigkeiten heraus).

Wir haben interne Runbooks in unserer KB für den Fall, dass die Automatisierungen versagen oder etwas außerhalb des Rahmens behoben werden muss.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana für Metriken in unseren GKE-Clustern und VMs.

Google Stackdriver für Protokolle (weil es enthalten und standardmäßig aktiv ist und derzeit für unsere Bedürfnisse ausreicht).


### Zabbix

Zabbix für alles. Keine zusätzliche Software nötig.
