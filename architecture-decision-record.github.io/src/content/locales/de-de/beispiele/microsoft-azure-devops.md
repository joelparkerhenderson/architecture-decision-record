# Microsoft Azure DevOps

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
  * [Microsoft Devops CI: An Unsatisfying Adventure](#microsoft-devops-ci-an-unsatisfying-adventure)
  * [Höhepunkte der Hacker-News-Diskussion](#höhepunkte-der-hacker-news-diskussion)
  * [Windows Development MVP](#windows-development-mvp)
  * [Zusammenfassung von Edward Thomson (Azure PM)](#zusammenfassung-von-edward-thomson-azure-pm)


## Zusammenfassung


### Problem

Wir möchten DevOps nutzen, um unsere Projekte zu bauen, zu integrieren, bereitzustellen und zu hosten. Wir erwägen Microsoft Azure DevOps.

  * Wir möchten, dass die Entwicklererfahrung schnell und zuverlässig ist, sowohl für die Einrichtung von DevOps, z. B. die Konfiguration, als auch für die laufende Nutzung, z. B. schnelle Build-Zeiten.
  
  * Wir möchten erwägen, Microsoft Azure als Ganzes zu nutzen, um die Projekt-Apps, Datenbanken usw. zu hosten.


### Entscheidung

Gegen Microsoft Azure DevOps entschieden.


### Status

Entschieden. Offen für eine Neubetrachtung, falls/wenn wichtige neue Informationen eintreffen.


## Details


### Annahmen

Alle üblichen DevOps-Annahmen, etwa im Buch Accelerate.

  * Schnelle Builds sind eine erhebliche Hilfe. Das beschleunigt die Feedback-Schleifen.

  * Wir können Teile von alternativen Anbietern ein-/austauschen, das heißt, wir möchten vielleicht unsere eigenen schnelleren Build-Server mitbringen, unser eigenes Versionskontrollsystem verwenden oder uns mit einem selbst gehosteten Continuous-Integration-Server abstimmen.
  
  * Eine schlanke Benutzbarkeit ist eine erhebliche Hilfe, für die Entwicklererfahrung und damit wiederum für subtile Bereiche wie Konsistenz, Klarheit, Sicherheit und eine leichte Lernkurve.

  * Wenn etwas kaputt oder problematisch ist, möchten wir einen wirksamen Weg, das Problem zu melden. Das ist besonders wichtig bei sicherheitsrelevanten Problemen.


### Einschränkungen

Keine bekannt. Azure hat eine veröffentlichte Zusage, gut mit externen Werkzeugen zusammenzuspielen.


### Positionen

Wir haben die Nutzung von Microsoft Azure Devops im Vergleich zu AWS erwogen, das der Platzhirsch ist.

Wir haben mit Azure DevOps, Azure Pipelines, Azure Repo und dem Hochfahren neuer Server in Azure per Terraform experimentiert.

Wir haben damit experimentiert, Support von Microsoft-Vertretern zu bekommen.

Wir haben Informationen von Kollegen in Blogs und auf Hacker News gesammelt.


### Argument

Azure DevOps bewirbt ein hervorragendes Angebot, doch es hält nicht, was es verspricht, die Teile arbeiten nicht gut zusammen, und der Support ist schlecht.

Unsere Erfahrungen aus erster Hand:

  * Die Azure-Einrichtung ist ein Durcheinander von UIs, von denen sich einige mit Microsoft-Konten überschneiden, andere nicht. Es gibt z. B. eine Azure-Anmeldung, eine Microsoft.com-Anmeldung, eine Live.com-Anmeldung usw., und alle sind gleichzeitig im Spiel.

  * Wir sind bei der Einrichtung auf ein kleineres Sicherheitsproblem gestoßen und haben keine Lösung gefunden. Wir haben vielfach versucht, es zu melden, bei vielen Microsoft-Vertretern, ohne Erfolg. Wir haben es erfolgreich an Microsoft Security gemeldet, das mit „won't fix“ antwortete.

  * Die Dokumentation ist oft entweder falsch oder veraltet. Zumindest ein Teil davon liegt an der schlechten Suchmaschine von Microsoft und ein Teil an unterdurchschnittlicher SEO.
  
  * Die Terraform-Einrichtung ist gut dokumentiert und funktioniert. Die Terraform-Unterstützung ist jedoch im Vergleich zu AWS schwach, weil Microsoft Geschäftsbeziehungen zu Anbietern aufbaut, um verkettete Terraform-Einrichtungsbeispiele zu erstellen.

Unsere Erfahrungen von Kollegen:

  * Nachdem wir unsere eigene Blindbewertung durchgeführt hatten, suchten wir nach Erfahrungen von Kollegen. Was wir fanden, bestätigte unsere Erfahrungen.

  * Kollegen berichteten von zusätzlichen Problemen mit Build-Zeiten und von Problemen mit dem Mitbringen eigener Build-Server. Diese Probleme sind erheblich schwerwiegender als UI-Probleme, denn das Ausführen von Builds ist der Kernzweck einer Build-Pipeline, und wir erwarten, viele pro Tag auszuführen.

  * Wir fanden eine hervorragende Beteiligung von Azure-Teammitgliedern in den Diskussionsbereichen. Ein Lob an Microsoft dafür. Besonders beeindruckt sind wir von Edward Thomson, Azure-PM und Programmierer, wegen seiner Beteiligung, Direktheit und technischen Erklärungen.


### Implikationen

Die Wahl von Microsoft Azure DevOps scheint an Zeit und Kosten wahrscheinlich teurer (~3-fach) zu sein, als Azure nicht zu wählen.


## Zugehöriges


### Zugehörige Entscheidungen

Wenn wir Azure DevOps wählen, gibt es viele zugehörige Angebote, darunter Azure Repo, Azure Pipeline usw. Wir glauben, dass die Wahl von Azure Devops es möglicherweise erleichtert, mehr Azure-Fähigkeiten zu nutzen, oder es erschweren kann, Fähigkeiten anderer Anbieter zu nutzen.

Wir glauben, dass Microsoft bei der Entwicklererfahrung große Fortschritte macht, und wir sehen, dass Microsoft große Übernahmen von Entwicklerwerkzeugen (z. B. GitHub) und Abhängigkeiten (z. B. Citus) tätigt.

Wenn wir Azure DevOps wählen, möchten wir möglicherweise die Wahl der von Microsoft übernommenen Angebote betonen, und wir möchten uns den übernommenen Angeboten möglicherweise mit mehr Sorgfalt/Bewertung nähern, wegen einer möglichen Gewebeabstoßung, z. B. des Risikos von Mitarbeiterfluktuation.


### Zugehörige Anforderungen

Wir möchten sehr schnelle Build-Zeiten. Wir akzeptieren, dafür einen hohen Aufpreis zu zahlen. Das liegt daran, dass wir sehr schnell iterieren möchten.

Wir möchten sehr hohe Zuverlässigkeit. Wir akzeptieren, dafür einen hohen Aufpreis zu zahlen. Das liegt daran, dass wir Anwendungsfälle mit hohem Wert testen, einschließlich Finanztransaktionen, vertraulicher Transaktionen usw.

Unsere vier wichtigsten DevOps-KPIs umfassen die mittlere Wiederherstellungszeit, die schnelle Builds und hohe Zuverlässigkeit erfordert.


### Zugehörige Artefakte

Wir möchten, dass das Build-System Artefakte ausgibt, die sich zur Verwendung in anderen Systemen wie Artifactory eignen.


### Zugehörige Prinzipien

Leicht umkehrbar. Wir können Azure DevOps parallel zum etablierten AWS bewerten.


## Notizen


### Microsoft Devops CI: An Unsatisfying Adventure

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Blogbeitrag.

„Als Softwareentwickler weiß ich aus erster Hand, wie schwierig es ist, Qualitätsprodukte schnell und günstig zu bauen. Es ist eine Kunstform, die uns manchmal gelingt und die zu anderen Zeiten in etwas wie die Regierungswebsite für die Gesundheitsversorgung der Obama-Ära abgleitet. Unser Maß an Kontrolle über das entstehende Produkt variiert, und die Schuld für das Scheitern fällt oft auf die falschen Leute in der Entscheidungshierarchie. Microsofts Azure DevOps (früher bekannt als Visual Studio Team Services) ist trotz klar guter Absichten ein perfekter Sturm aus schlechten Entscheidungen und mangelhafter Umsetzung.“


### Höhepunkte der Hacker-News-Diskussion

https://news.ycombinator.com/item?id=18983586

„Wir nutzen Azure DevOps bei meiner Arbeit ausgiebig, und nachdem ich GitHub, Gitlab, selbst gehostete Lösungen, Jenkins, TeamCity genutzt habe... landet Azure DevOps auf dem letzten Platz.“

„Die UI ist überall furchtbar sperrig. Am schlimmsten sind für mich Pull Requests. Es ist unglaublich mühsam, mit Leuten an einem Pull Request zu arbeiten. Ich kann nicht einmal auf „ein“ bestimmtes Problem zeigen – bei uns ist es überall kaputt.“

„Azure Devops ist etwas, das ich lieben möchte. Die UI ändert sich ständig, behebt aber nicht die zugrunde liegenden Fehler, die es seit Ewigkeiten gibt.“

„Die Werkzeuge sind nicht gut integriert, die UI ist wirklich langsam, es gibt keine Dashboard-Ansicht aktiver Pull Requests, Builds, Releases usw. für meine Lieblings-Repos. Build-/Deploy-Zeiten sind wahnsinnig langsam.“

„Wir haben auch versucht, Azure Boards (Work Items, Boards, Backlogs usw.) zu nutzen. Autsch. Es ist ein vollständiges UI-Chaos zusammenhangloser Ideen. Statt eine Sache gut umzusetzen, haben sie zwei Dutzend Dinge schlecht umgesetzt.“


### Windows Development MVP

Hier spricht ein Windows Development MVP. Ich habe das Gefühl, einen Teil der Verantwortung tragen zu müssen, weil ich nicht lauter auf diese Probleme hingewiesen habe. Ich muss aber sagen, ich bin enttäuscht zu hören, dass Sie „überrascht“ von den UX-Problemen sind. Ich habe Ihren Leuten gesagt, dass die UX furchtbar ist (z. B. schon vor dem Start) und habe immer wieder gehört „wir wissen es, wir beheben es“. Ich werde anfangen, das Feedback zu formalisieren und durch die Kanäle zu schieben, bleiben Sie dran. Ich bin auch vor Ort (Bellevue) und würde gern vorbeikommen und versuchen, unsere relativ einfache Open-Source-.NET/WPF/UWP-App in einer Pipeline zu bauen. Ich vermute, es wird uns beiden die Augen öffnen.

Einige Beispiele:

* Man kann keine Pipeline mit einem Git-Repo bauen, das Submodule enthält

* Ich fand es unmöglich, den PATH für einige eigene Werkzeuge zu bearbeiten

* Die Erfahrung mit „Neue Pipeline“ ergibt einfach nicht viel Sinn, neue Benutzer, die herumklicken, landen irgendwann in der falschen Dokumentation.


### Zusammenfassung von Edward Thomson (Azure PM)

Ich habe den Code geschrieben, der Ihre Pull Requests zusammenführt. Program Manager bei Microsoft für Azure DevOps; früher Softwareentwickler an Versionskontrollwerkzeugen bei GitHub, Microsoft, SourceGear.

https://www.edwardthomson.com/

Mitbetreuer von libgit2. https://libgit2.github.io

Mitmoderator von All Things Git, dem Podcast über Git. https://www.allthingsgit.com/

Kurator von Developer Tools Weekly, einem Newsletter über Entwicklungswerkzeuge. https://developertoolsweekly.com/
