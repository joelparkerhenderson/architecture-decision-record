# Monorepo oder Multirepo

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

Unser Projekt umfasst die Entwicklung von drei Hauptkategorien von Software:

  * Frontend-GUIs
  * Middleware-Dienste
  * Backend-Server

Bei der Entwicklung ist unser Versionskontrollsystem (VCS) der Quellcodeverwaltung (SCM) Git.

Wir müssen wählen, wie wir Git zur Organisation unseres Codes nutzen.

Die Wahl auf oberster Ebene besteht darin, als „Monorepo“, „Polyrepo“ oder „Hybrid“ zu organisieren:

  * Monorepo bedeutet, dass wir alle Teile in ein großes Repository legen
  * Polyrepo bedeutet, dass wir jeden Teil in sein eigenes Repository legen
  * Hybrid bedeutet eine Mischung aus Monorepo und Polyrepo

Weitere Informationen finden Sie unter https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Entscheidung

Monorepo, wenn eine Organisation/ein Team/ein Projekt relativ klein ist und schnelle Iteration höhere Priorität hat als die Aufrechterhaltung der Stabilität.

Polyrepo, wenn eine Organisation/ein Team/ein Projekt relativ groß ist und die Aufrechterhaltung der Stabilität höhere Priorität hat als schnelle Iteration.


### Status

Entschieden. Offen für eine Neubetrachtung, falls/wenn neue Werkzeuge zur Verwaltung von Monorepos und/oder Polyrepos verfügbar werden.


## Details


### Annahmen

Der gesamte Code, den wir entwickeln, ist für die Angebote einer Organisation bestimmt und nicht für die Allgemeinheit. Das heißt, der Broker-Dealer strebt nichts an wie ehrenamtliche Entwickler aus der Allgemeinheit.


### Einschränkungen

Einschränkungen sind gut dokumentiert unter https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Positionen

Wir haben Monorepos im Stil von Google, Facebook usw. betrachtet. Wir glauben, dass etwaige Skalierungsprobleme von Monorepos so weit in der Zukunft liegen, dass wir, wenn wir sie brauchen, dieselben Praktiken wie Google und Facebook nutzen können.

Wir haben Polyrepos im Stil typischer Git-Open-Source-Projekte betrachtet, etwa Google Android, Facebook React usw. Wir halten diese für die beste Wahl für die Beteiligung der Allgemeinheit (z. B. kann jeder auf der Welt am Code mitarbeiten) und für die individuelle Verfügbarkeit (z. B. wird das Projekt für sich allein ohne weitere Teile genutzt).


### Argument

Wenn eine Organisation/ein Team/ein Projekt relativ klein ist, wählen wir Monorepo, weil schnelle Iteration eine deutlich höhere Priorität hat als die Aufrechterhaltung der Stabilität

Wenn eine Organisation/ein Team/ein Projekt relativ groß ist, wählen wir Polyrepo, weil die Aufrechterhaltung der Stabilität eine deutlich höhere Priorität hat als schnelle Iteration.


### Implikationen

Wenn bereits eine Pipeline für CI+CD existiert, müssen wir sie möglicherweise anpassen, um mehrere Projekte in einem Repository zu testen.

CI+CD kann für einen vollständigen Build bei einem Monorepo länger dauern, weil CI+CD alle Projekte im Monorepo bauen könnte.

Wenn eine Organisation/ein Team/ein Projekt wächst, wird ein Monorepo Skalierungsprobleme haben.

Skalierungsprobleme beim Monorepo können den Wechsel zu einem Polyrepo zunehmend wertvoll machen.

Der Wechsel von Monorepo zu Polyrepo ist eine bedeutende DevOps-Aufgabe und muss geplant, gesteuert und programmiert werden.


## Zugehöriges


### Zugehörige Entscheidungen

Wir werden Entscheidungen für zugehörige Werkzeuge zur Verwaltung von Monorepos (z. B. Google Bazel) und Polyrepos (z. B. Lyft Refactorator) treffen.


### Zugehörige Anforderungen

Wir müssen die CI+CD-Pipeline so entwickeln, dass sie gut mit Git funktioniert.


### Zugehörige Artefakte

Wir erwarten, dass die Repository-Organisation zugehörige Artefakte für Bereitstellung, Konfigurationsmanagement, Tests und ähnliche DevOps-Bereiche hat. 


### Zugehörige Prinzipien

Leicht umkehrbar. Wenn das Monorepo in der Praxis nicht funktioniert oder von der Führung nicht gewünscht wird, ist der Wechsel zum Polyrepo einfach.

Kundenfixierung. Wir legen Wert darauf, das Projekt in die Hände der Kunden zu bringen, und wir glauben, dass ein Monorepo uns schneller dorthin bringen kann als ein Polyrepo und uns auch hilft, schneller zu iterieren.

Groß denken. Google und Facebook sind sehr starke Befürworter von Monorepos gegenüber Polyrepos, weil alle Kernangebote gemeinsam entwickelt/getestet/bereitgestellt werden können.


## Notizen

Fügen Sie hier beliebige Notizen hinzu.
