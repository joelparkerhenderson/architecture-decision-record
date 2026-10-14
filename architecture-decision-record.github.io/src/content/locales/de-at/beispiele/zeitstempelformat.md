# Zeitstempelformat

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


## Zusammenfassung


### Problem

Wir möchten nachverfolgen können, wann Dinge geschehen, indem wir Zeitstempel und ein einheitliches Zeitstempelformat verwenden, das in all unseren Systemen und in Drittanbietersystemen gut funktioniert.

Wir interagieren mit Systemen, die unterschiedliche Zeitstempelformate haben:

* JSON-Nachrichten haben kein natives Zeitstempelformat, daher müssen wir wählen, wie ein Zeitstempel in eine Zeichenfolge und eine Zeichenfolge in einen Zeitstempel umgewandelt wird, das heißt, wie serialisiert/deserialisiert wird.

* Manche Anwendungen sind auf Ortszeit statt auf UTC eingestellt. Das kann für Projekte praktisch sein, die sich an die Ortszeit anpassen müssen, etwa Projekte, die Ereignisse auslösen, die auf der Ortszeit beruhen.

* Manche Systeme haben unterschiedliche Anforderungen und Fähigkeiten bei der Zeitgenauigkeit, etwa die Verwendung einer Zeitauflösung von Sekunden gegenüber Millisekunden gegenüber Nanosekunden. Der Befehl `date` des Linux-Betriebssystems verwendet zum Beispiel standardmäßig eine Zeitgenauigkeit von Sekunden, während die Börse Nasdaq standardmäßig eine Zeitgenauigkeit von Nanosekunden wünscht.


### Entscheidung

Wir wählen das Standard-Zeitstempelformat ISO 8601 mit Nanosekunden-Genauigkeit, konkret „YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ“.

Das Format zeigt Jahr, Monat, Tag, Stunde, Minute, Sekunde, Nanosekunden und die Zulu-Zeitzone, auch bekannt als UTC, GMT.


### Status

Entschieden.


## Details


### Annahmen

Wir müssen diese Zeitstempel-Textzeichenfolgen verarbeiten, um von einem Zeitstempel in eine Zeichenfolge (auch Serialisieren) und von einer Zeichenfolge in einen Zeitstempel (auch Deserialisieren) umzuwandeln.

Wir möchten ein Format, das im Allgemeinen einfach zu verwenden, einfach umzuwandeln und für Menschen leicht lesbar ist.

Wir möchten Kompatibilität mit einer breiten Palette externer Systeme, die wir nicht kontrollieren können, etwa Analysesystemen, Datenbanksystemen und Finanzsystemen.


### Einschränkungen

Manche Systeme haben Einschränkungen bei der Zeitgenauigkeit. Der Befehl `date` des macOS-Betriebssystems kann zum Beispiel die Zeitgenauigkeit in Sekunden ausgeben, aber nicht in Nanosekunden.


### Positionen

Wir haben eine Reihe von Optionen erwogen:

* Unix-Epoche, das heißt eine einzelne hochzählende Zahl.

* Knappes Textformat „YYYYMMDDTHHMMSSNNNNNNNNN“.

* Verwendung einer lokalen Zeitzone gegenüber der Zeitzone UTC.


### Argument

Für die typische Nutzung legen wir mehr Wert auf leichtes Lesen/Schreiben durch Menschen als auf rohe Geschwindigkeit/Größe.

Für die typische Nutzung möchten wir ein Format, das in maschinellen Systemen gut funktioniert und auch manuell gut funktioniert, etwa beim Schreiben von Beispieldaten, Lesen von JSON-Ausgaben, Durchsuchen einer Protokolldatei mit grep usw.

Für untypische Nutzung, etwa Hochleistungsrechnen, erwarten wir, dass wir jedes gewählte Textformat optimieren wollen, indem wir den Text in ein schnelleres Format umwandeln, etwa den eingebauten Datumsobjekttyp einer Programmiersprache. Das Textformat spielt für HPC also keine große Rolle.


### Implikationen

Unsere verschiedenen Textsysteme und Zeitsysteme werden auf dieses Format zusammenlaufen.


## Zugehöriges


### Zugehörige Entscheidungen

Wir möchten möglicherweise auch einen schnellen/einfachen Weg, Zeitdifferenzen, auch Dauern genannt, zu verfolgen. Diese sind mit Unix-Epochen-Zeitstempeln einfach.


### Zugehörige Anforderungen

Wir möchten unsere Entscheidung möglicherweise anpassen, z. B. wenn wir eine zugehörige Anforderung für eine bestimmte Art von Protokollnachrichten-Stempel haben, etwa für Splunk, Sumo, ELK usw.


### Zugehörige Artefakte

Formatierer und Parser für Sprachen:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Rosetta-Code-Beispiele:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

SixArm-Beispiele:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Zugehörige Prinzipien

Leicht umkehrbar. Wir können recht leicht zu einem anderen Format wechseln, etwa zur Unix-Epoche.

Vorzeitige Optimierung aufschieben. Für typische Nutzung kümmern uns eine Handvoll zusätzlicher Zeichen, etwa bei einem Format mit Bindestrichen und Doppelpunkten, nicht sehr.


## Notizen

Fügen Sie hier Notizen hinzu.
