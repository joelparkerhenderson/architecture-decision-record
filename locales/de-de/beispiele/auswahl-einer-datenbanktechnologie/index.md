# Architecture Decision Record: Auswahl einer Datenbanktechnologie

## Status

Angenommen

## Kontext

Wir entwerfen eine neue Anwendung, die Daten skalierbar und leistungsfähig speichern und abrufen muss. Wir haben drei Arten von Datenbanktechnologien identifiziert, die häufig verwendet werden: relationale Datenbanken, Dokumentdatenbanken und Ereignisdatenbanken.

Relationale Datenbanken speichern Daten in Tabellen mit festen Schemata und erzwingen strenge Datenintegritätsbedingungen. Sie eignen sich für Anwendungen, die komplexe Datenbeziehungen und Transaktionen benötigen. Beispiele sind MySQL, PostgreSQL und Oracle.

Dokumentdatenbanken speichern Daten in JSON-ähnlichen Dokumenten und sind schemalos. Sie eignen sich gut für Anwendungen, die flexible Datenmodelle und horizontale Skalierung benötigen. Beispiele sind MongoDB, Couchbase und Amazon DynamoDB.

Ereignisdatenbanken speichern Daten als Folge von Ereignissen und erfassen jede Änderung an den Daten. Sie eignen sich für Anwendungen, die Auditierung, Event Sourcing und komplexe Datenverarbeitung benötigen. Beispiele sind Apache Kafka, Apache Pulsar und AWS Kinesis.
Entscheidung

Nach sorgfältiger Bewertung der Anforderungen und Einschränkungen unserer Anwendung haben wir beschlossen, eine Dokumentdatenbank zu verwenden.

## Begründung

Wir haben uns für eine Dokumentdatenbank entschieden, weil:

1. Unsere Anwendung ein flexibles Datenmodell benötigt, das sich im Lauf der Zeit weiterentwickeln kann. Dokumentdatenbanken erlauben es uns, Daten in einem schemalosen Format zu speichern, sodass wir neue Felder hinzufügen oder die Struktur bestehender Dokumente ändern können, ohne das Datenbankschema zu ändern.

2. Unsere Anwendung horizontal skalieren muss, um große Daten- und Verkehrsmengen zu bewältigen. Dokumentdatenbanken bieten integrierte Unterstützung für Sharding und Replikation, wodurch wir Daten auf mehrere Server verteilen und hohen Lese- und Schreibdurchsatz bewältigen können.

3. Unsere Anwendung einen schnellen und effizienten Datenabruf benötigt. Dokumentdatenbanken bieten leistungsfähige Indexierungs- und Abfragefunktionen, mit denen wir Daten schnell und effizient abrufen können.

4. Unsere Anwendung keine komplexen Transaktionen oder Datenbeziehungen benötigt. Während relationale Datenbanken bei der Durchsetzung von Datenintegritätsbedingungen und der Bearbeitung komplexer Transaktionen glänzen, hat unsere Anwendung solche Anforderungen nicht. Dokumentdatenbanken können für unseren Anwendungsfall ausreichende Konsistenz- und Dauerhaftigkeitsgarantien bieten.

## Konsequenzen

Mit der Wahl einer Dokumentdatenbank müssen wir in das Erlernen und Verstehen der konkreten Technologie investieren, die wir einsetzen. Außerdem müssen wir sicherstellen, dass das Datenmodell unserer Anwendung gut zum Datenmodell der Dokumentdatenbank passt, um Leistung und Skalierbarkeit zu maximieren.

Wir glauben jedoch, dass die Vorteile einer Dokumentdatenbank die Kosten überwiegen und dass sie am besten zu den Anforderungen und Einschränkungen unserer Anwendung passt.
