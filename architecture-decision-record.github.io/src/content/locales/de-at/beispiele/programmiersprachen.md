# Programmiersprachen

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

Wir müssen Programmiersprachen für unsere Software wählen. Wir haben zwei Hauptbedürfnisse: eine Frontend-Programmiersprache, die für Webanwendungen geeignet ist, und eine Backend-Programmiersprache, die für Serveranwendungen geeignet ist.


### Entscheidung

Wir wählen TypeScript für das Frontend.

Wir wählen Rust für das Backend.


### Status

Entschieden. Wir sind offen für neue Alternativen, sobald sie aufkommen.


## Details


### Annahmen

Die Frontend-Anwendungen sind typisch:

  * Typische Benutzer und Interaktionen

  * Typische Browser und Systeme

  * Typische Entwicklungen und Bereitstellungen

Die Frontend-Anwendungen werden sich voraussichtlich schnell weiterentwickeln:

  * Wir möchten schnelle, einfache Entwicklungen, Bereitstellungen, Iterationen usw. sicherstellen.

  * Wir schätzen Beweisbarkeit, etwa Typsicherheit, und nehmen dafür gern etwas mehr Arbeit in Kauf.

  * Wir brauchen keine Legacy-Kompatibilität.

Die Backend-Anwendungen liegen über dem Typischen:

  * Über dem Typischen liegende Ziele für Qualität, besonders Beweisbarkeit, Zuverlässigkeit, Sicherheit usw.

  * Über dem Typischen liegende Ziele für Nahe-Echtzeit, das heißt, wir wollen keine Pausen durch die Garbage Collection virtueller Maschinen.

  * Über dem Typischen liegende Ziele für funktionale Programmierung, besonders für Parallelisierung, Mehrkernverarbeitung und Speichersicherheit.

Wir akzeptieren geringere Kompilierzeit-Geschwindigkeiten zugunsten von Sicherheit zur Kompilierzeit und Geschwindigkeit zur Laufzeit.


### Einschränkungen

Wir haben eine starke Einschränkung bei Sprachen, die mit Funktionsdiensten großer Cloud-Anbieter, etwa Amazon Lambda, nutzbar sind.


### Positionen

Wir haben diese Sprachen erwogen:

  * C

  * C++

  * Clojure
  
  * Elixir
  
  * Erlang
  
  * Elm
  
  * Flow
  
  * Go
  
  * Haskell
  
  * Java
  
  * JavaScript
  
  * Kotlin
  
  * Python
  
  * Ruby
  
  * Rust
  
  * TypeScript



### Argument

Zusammenfassung pro Sprache:

  * C: abgelehnt wegen geringer Sicherheit; Rust kann nahezu alles besser.

  * C++: abgelehnt, weil es ein Durcheinander ist; Rust kann nahezu alles besser.

  * Clojure: hervorragende Modellierung; beste Lisp-Annäherung; großartige Laufzeit auf der JVM.
  
  * Elixir: hervorragende Laufzeit einschließlich Bereitstellbarkeit und Nebenläufigkeit; hervorragende Entwicklererfahrung; relativ kleines Ökosystem.

  * Erlang: hervorragende Laufzeit einschließlich Bereitstellbarkeit und Nebenläufigkeit; herausfordernde Entwicklererfahrung; relativ kleines Ökosystem.

  * Elm: sieht sehr vielversprechend aus; IBM veröffentlicht wichtige Fallstudien mit guten Ergebnissen; kleineres Ökosystem.

  * Flow: interessante Verbesserung gegenüber JavaScript; Entwickler wenden sich jedoch davon ab.

  * Go: hervorragende Entwicklererfahrung; hervorragende Nebenläufigkeit; aber eine Bilanz schlechter Entscheidungen, die die Sprache lähmen.

  * Haskell: beste funktionale Sprache; kleinere Entwickler-Community; hat nicht genug veröffentlichte Produktionserfolge erzielt.

  * Java: hervorragende Laufzeit; hervorragendes Ökosystem; unterdurchschnittliche Entwicklererfahrung.

  * JavaScript: beliebteste Sprache aller Zeiten; am weitesten verbreitetes Ökosystem.

  * Kotlin: behebt so vieles an Java; hervorragende Unterstützung durch JetBrains; gute veröffentlichte Fälle der Portierung von Java nach Kotlin.
  
  * Python: beliebteste Sprache für Systemadministration; großartige Analysewerkzeuge; gute Web-Frameworks; aber von Google zugunsten von Go aufgegeben.

  * Ruby: beste Entwicklererfahrung aller Zeiten; beste Web-Frameworks; netteste Community; aber sehr langsam; etwas schwer zu paketieren.

  * Rust: beste neue Sprache; Schwerpunkt auf Null-Abstraktion; Schwerpunkt auf Nebenläufigkeit; jedoch relativ kleines Ökosystem; und mit bewussten Grenzen bei manchen Arten von Compiler-Beschleunigungen, z. B. muss direkter Speicherzugriff ausdrücklich unsicher (unsafe) sein.

  * TypeScript: fügt JavaScript Typen hinzu; großartiger Transpiler; wachsender Entwicklerfokus auf der Portierung von JavaScript nach TypeScript; starke Unterstützung durch Microsoft.

Wir haben entschieden, dass VMs eine Reihe von Abwägungen haben, die wir derzeit nicht brauchen, etwa zusätzliche Komplexität, die Laufzeitfähigkeiten bietet.

Wir glauben, dass unsere Kernentscheidung von zwei übergreifenden Belangen getrieben wird:

  * Für die schnellste Laufzeitgeschwindigkeit und den engsten Systemzugriff würden wir JavaScript und C wählen.

  * Für nahezu schnellste Laufzeitgeschwindigkeit und nahezu engsten Systemzugriff wählen wir TypeScript und Rust.

Ehrenvolle Erwähnungen gehen an die VM-Sprachen und Web-Frameworks, die wir wählen würden, wenn wir eine VM-Sprache wollten:

  * Clojure und Luminus

  * Java und Spring

  * Elixir und Phoenix


### Implikationen

Frontend-Entwickler müssen TypeScript lernen. Das ist wahrscheinlich eine leichte Lernkurve, wenn die Hauptaufwand-Erfahrung des Entwicklers in der Nutzung von JavaScript besteht.

Backend-Entwickler müssen Rust lernen. Das ist wahrscheinlich eine mittlere Lernkurve, wenn die Haupterfahrung des Entwicklers in der Nutzung von C/C++ besteht, und eine harte Lernkurve, wenn die Haupterfahrung in der Nutzung von Java, Python, Ruby oder ähnlichen speicherverwalteten Sprachen besteht. 

TypeScript und Rust sind beide relativ neu. Das bedeutet, dass viele Werkzeuge noch keine Dokumentation für diese Sprachen haben. Zum Beispiel muss die DevOps-Pipeline für diese Sprachen eingerichtet werden, und bisher hat keines der DevOps-Werkzeuge, die wir bewerten, Standardbeispiele für diese Sprachen.

Die Kompilierzeiten für TypeScript und Rust sind recht langsam. Ein Teil davon mag auf die Neuheit der Sprachen zurückzuführen sein. Wir sollten uns ansehen, wie sich langsame Kompilierzeiten abmildern lassen, etwa durch Kompilierung bei Bedarf, nebenläufige Kompilierung usw.

Die IDE-Unterstützung für diese Sprachen ist noch nicht allgegenwärtig und noch nicht erstklassig. Zum Beispiel verkauft JetBrains die IDE PyCharm mit erstklassiger Unterstützung für Python, verkauft aber keine IDE mit erstklassiger Unterstützung für Rust; stattdessen kann JetBrains ein Rust-Plugin nutzen, das vielleicht 80 % der Rust-Sprachunterstützung im Vergleich zur Python-Sprachunterstützung bietet.


## Zugehöriges


### Zugehörige Entscheidungen

Wir streben Ökosystem-Entscheidungen an, die zu diesen Sprachen passen.

Zum Beispiel möchten wir eine IDE wählen, die gute Fähigkeiten für diese Sprachen hat.

Zum Beispiel werden wir uns für unser Frontend-Web-Framework eher für ein Framework entscheiden, das eher auf TypeScript ausgerichtet ist (z. B. Vue), als für eines, das eher auf reines JavaScript ausgerichtet ist (z. B. React).


### Zugehörige Anforderungen

Unsere gesamte Werkzeugkette muss diese Sprachen unterstützen.


### Zugehörige Artefakte

Wir erwarten, dass wir einige Geheimnisse in Umgebungsvariablen exportieren.


### Zugehörige Prinzipien

Zweimal messen, einmal bauen. Wir priorisieren etwas Sicherheit vor etwas Geschwindigkeit.

Laufzeit ist wertvoller als Kompilierzeit. Wir priorisieren die Nutzung durch Kunden vor der Nutzung durch Entwickler.


## Notizen

Beliebige Notizen hier.
