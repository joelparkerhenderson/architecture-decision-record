# Konfiguration über Umgebungsvariablen

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
  * [Implikationen ](#implikationen)
* [Zugehöriges](#zugehöriges)
  * [Zugehörige Entscheidungen](#zugehörige-entscheidungen)
  * [Zugehörige Anforderungen](#zugehörige-anforderungen)
  * [Zugehörige Artefakte](#zugehörige-artefakte)
  * [Zugehörige Prinzipien](#zugehörige-prinzipien)
* [Notizen](#notizen)


## Zusammenfassung


### Problem

Wir möchten, dass unsere Anwendungen über Artefakte/Binärdateien/Quellcode hinaus konfigurierbar sind, sodass sich ein Build je nach Bereitstellungsumgebung unterschiedlich verhalten kann.

  * Dazu möchten wir die Konfiguration über Umgebungsvariablen verwenden.

  * Wir möchten die Konfiguration mit Dateien verwalten, die wir versionieren können.

  * Wir möchten einen gewissen Entwicklerkomfort bieten, etwa zu wissen, was konfiguriert werden kann und welche Standardwerte relevant sind.


### Entscheidung

Für .env-Dateien mit zugehöriger Standardwert-Datei und Schema-Datei entschieden.


### Status

Entschieden. Offen für die Prüfung neuer Möglichkeiten, sobald sie aufkommen.


## Details


### Annahmen

Wir bevorzugen die Trennung von Anwendungscode und Umgebungscode. Wir nehmen an, dass die App in verschiedenen Umgebungen unterschiedlich funktionieren muss, etwa in einer Entwicklungsumgebung, Testumgebung, Demo-Umgebung, Produktionsumgebung usw.

Wir befürworten die Branchenpraxis der „12-Factor-App“ und noch mehr die verwandte Praxis der „15-Factor-App“.

Viele unserer früheren Projekte haben die Konvention einer `.env`-Datei oder eines ähnlichen `.env`-Verzeichnisses verwendet. Es ist üblich, diese aus der Versionskontrolle herauszuhalten und stattdessen auf andere Weise bereitzustellen, zu versionieren und zu verwalten.


### Einschränkungen

Wir möchten Geheimnisse aus unserem Versionskontrollsystem (VCS) der Quellcodeverwaltung (SCM) heraushalten.

Wir streben Kompatibilität mit gängigen Software-Frameworks und -Bibliotheken an. Node hat zum Beispiel ein Modul „dotenv“ zum Lesen der Konfiguration über Umgebungsvariablen.


### Positionen

Wir haben einige Ansätze erwogen:

  * Konfiguration in der App speichern, etwa in einer Datei `config.js`.

  * Konfiguration in der Umgebung speichern, etwa in einer Datei `.env`.

  * Konfiguration von einem bekannten Ort abrufen, etwa einem Lizenzserver.


### Argument

Wir haben uns für den Ansatz einer .env-Datei entschieden, weil:

  * Er beliebt ist, auch unter Experten.

  * Er dem Muster von `.env`-Dateien folgt, die unsere Teams in vielen Projekten oft erfolgreich eingesetzt haben.

  * Er einfach ist. Insbesondere sind wir vorerst mit den erheblichen Abwägungen einverstanden, die wir sehen, etwa dem Fehlen von Audit-Fähigkeiten im Vergleich zu einem Lizenzserver-Ansatz.


### Implikationen 

Wir müssen einen Weg finden, die öffentliche Konfiguration über Umgebungsvariablen vom Management von Geheimnissen zu trennen.


## Zugehöriges


### Zugehörige Entscheidungen

Wir erwarten, dass alle unsere Anwendungen diesen Ansatz verwenden.

Wir planen, alle unsere Anwendungen, die einen weniger leistungsfähigen Ansatz verwenden, etwa Hardcodierung in einer Binärdatei oder im Quellcode, aufzurüsten.

Wir lassen alle unsere Anwendungen, die einen leistungsfähigeren Ansatz verwenden, etwa einen Lizenzserver, unverändert.


### Zugehörige Anforderungen

Wir fügen DevOps-Fähigkeiten für die Dateien hinzu, einschließlich Hooks, Tests und kontinuierlicher Integration.

Wir müssen alle Entwickler-Teamkollegen zu dieser Entscheidung schulen.



### Zugehörige Artefakte

Jeder Bereich, in dem wir bereitstellen, benötigt seine eigene .env-Datei und zugehörige Dateien.


### Zugehörige Prinzipien

Leicht umkehrbar.


## Notizen


Beispieldatei `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Beispieldatei `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Beispieldatei `.env.schema` nur mit den Schlüsseln:

```env
NAME
EMAIL
```
