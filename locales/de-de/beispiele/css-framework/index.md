# Architecture Decision Record: CSS-Framework

Inhalt:

- [Zusammenfassung](#zusammenfassung)
  - [Problem](#problem)
  - [Entscheidung](#entscheidung)
  - [Status](#status)
- [Details](#details)
  - [Annahmen](#annahmen)
  - [Einschränkungen](#einschränkungen)
  - [Positionen](#positionen)
  - [Argument](#argument)
  - [Implikationen](#implikationen)
- [Zugehöriges](#zugehöriges)
  - [Zugehörige Entscheidungen](#zugehörige-entscheidungen)
  - [Zugehörige Anforderungen](#zugehörige-anforderungen)
  - [Zugehörige Artefakte](#zugehörige-artefakte)
  - [Zugehörige Prinzipien](#zugehörige-prinzipien)
- [Notizen](#notizen)


## Zusammenfassung


### Problem

Wir möchten ein CSS-Framework verwenden, um unsere Webanwendungen zu erstellen:

  * Wir möchten ein schnelles und zuverlässiges Benutzererlebnis auf allen gängigen Browsern und Bildschirmgrößen.

  * Wir möchten schnelle Iteration bei Design, Layout, UI/UX usw.

  * Wir möchten responsive Anwendungen, besonders für kleinere Bildschirme wie auf mobilen Geräten, größere Bildschirme wie 4K-Breitbildschirme und dynamische Bildschirme wie drehbare Displays.  


### Entscheidung

Für Bulma entschieden.


### Status

Für Bulma entschieden. Offen für neue CSS-Framework-Optionen, sobald sie erscheinen.


## Details


### Annahmen

Wir möchten Webanwendungen erstellen, die modern, schnell, zuverlässig, responsiv usw. sind.

Typische moderne Webanwendungen verringern oder eliminieren die Nutzung von jQuery aus mehreren Gründen: 

  * Modernes JavaScript übernimmt nach und nach viele Fähigkeiten, die jQuery bereitgestellt hat, sodass jQuery weniger gebraucht wird, und es gibt bessere/schnellere/kleinere Module, die bestimmte Implementierungen bieten

  * jQuerys breiter Ansatz besteht in direkter DOM-Manipulation, was für moderne JavaScript-Frameworks (z. B. React, Vue, Svelte) ein Anti-Pattern ist

  * jQuery stört sich selbst, wenn es zweimal geladen wird usw.


### Einschränkungen

Wenn wir ein CSS-Framework wählen, das jQuery verwendet, sind wir darauf festgelegt, jQuery einzubinden. Semantic UI verwendet zum Beispiel jQuery, Tachyons nicht.

Wenn wir ein minimales CSS-Framework wählen, verzichten wir auf Framework-Komponenten, die wir jetzt oder bald vielleicht möchten. Semantic UI bietet zum Beispiel ein Bild-Karussell, Tachyons nicht.


### Positionen

Wir haben erwogen, kein Framework zu verwenden. Das erscheint weiterhin machbar, besonders weil CSS Grid einen Großteil dessen bietet, was wir für unser Projekt brauchen..

Wir haben viele CSS-Frameworks mit einer schnellen Vorauswahl betrachtet: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons usw. Unsere beiden Auswahlen für eine tiefere Prüfung sind Semantic UI (weil es den semantischsten Ansatz hat) und Bulma (weil es den leichtgewichtigsten Ansatz hat, der die Komponenten bietet, die wir jetzt wollen).

Wir haben Semantic UI betrachtet. Es bietet viele Komponenten, darunter solche, die wir für unser Projekt wollen: Tabs, Raster, Schaltflächen usw. Wir haben mit Semantic UI auf zwei Arten einen Pilotversuch gemacht: mit typischen CDN-Dateien und mit NPM-Repositories. Wir hatten mit Semantic UI Erfolg in einer statischen HTML-Seite, aber nicht innerhalb unseres Zeitfensters für den Aufbau einer JavaScript-SPA (vor allem wegen Problemen beim Laden von jQuery). Wir haben festgestellt, dass andere Programmierer die Semantic-UI-Entwickler aus denselben Gründen wie wir gebeten haben, eine jQuery-freie Version zu erstellen. Andere Programmierer fordern seit vielen Jahren eine jQuery-freie Version, doch die Entwickler haben abgelehnt und erklärt, jede jQuery-freie Version wäre zu schwer zu schreiben, z. B. ~„das Semantic-UI-Projekt hat mehr als 22.000 Berührungspunkte, die jQuery verwenden“.

Beispiel mit Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Wir haben Bulma betrachtet. Bulma hat viele ähnliche Fähigkeiten wie Semantic UI, wenn auch nicht so viele anspruchsvolle Komponenten. Bulma ist mit modernen Techniken gebaut, etwa ohne jQuery. Bulma hat einige Komponenten von Drittanbietern, von denen wir einige vielleicht nutzen möchten.


Beispiel mit Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argument

Wie oben.

Konkret scheint Semantic UI sowohl technologisch (nämlich so viele jQuery-Berührungspunkte) als auch in Bezug auf die Führung (nämlich jQuery-frei war eine harte Absage, statt eine Roadmap, kontinuierliche Verbesserung, Spendensammlung usw. zu versuchen) ein Warnsignal zu haben.


### Implikationen

Wenn wir ein gutes Nicht-jQuery-CSS-Framework finden, ist das im Allgemeinen hilfreich und insgesamt gut.


## Zugehöriges


### Zugehörige Entscheidungen

Das von uns gewählte CSS-Framework kann die Testbarkeit beeinflussen.


### Zugehörige Anforderungen

Wir möchten schnell eine rein moderne App ausliefern. 

Wir möchten keine Zeit damit verbringen, an älteren Frameworks (insbesondere Semantic UI) mit älteren Abhängigkeiten (insbesondere jQuery) zu arbeiten.


### Zugehörige Artefakte

Betrifft das gesamte typische HTML, das das CSS verwenden wird.


### Zugehörige Prinzipien

Leicht umkehrbar.

Bedarf an Geschwindigkeit.


## Notizen

Beliebige Notizen hier.
