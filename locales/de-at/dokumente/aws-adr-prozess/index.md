# Prozess für Architecture Decision Records bei AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Ein Architecture Decision Record (ADR) ist ein Dokument, das eine Entscheidung beschreibt, die das Team zu einem wesentlichen Aspekt der Softwarearchitektur trifft, die es aufbauen möchte. Jeder ADR beschreibt die Architekturentscheidung, ihren Kontext und ihre Konsequenzen. ADRs haben Status und folgen daher einem Lebenszyklus. Ein Beispiel für einen ADR finden Sie im Anhang.

Der ADR-Prozess liefert eine Sammlung von Architecture Decision Records. Diese Sammlung bildet das Entscheidungsprotokoll. Das Entscheidungsprotokoll liefert den Projektkontext sowie detaillierte Informationen zu Implementierung und Entwurf. Projektmitglieder überfliegen die Überschriften der einzelnen ADRs, um sich einen Überblick über den Projektkontext zu verschaffen. Sie lesen die ADRs, um tief in die Projektimplementierung und die Entwurfsentscheidungen einzutauchen.

Sobald das Team einen ADR annimmt, wird er unveränderlich. Wenn neue Erkenntnisse eine andere Entscheidung erfordern, schlägt das Team einen neuen ADR vor. Sobald das Team den neuen ADR annimmt, ersetzt er den vorherigen ADR.

## Umfang des ADR-Prozesses

Projektmitglieder sollten für jede architektonisch bedeutsame Entscheidung, die das Softwareprojekt oder -produkt betrifft, einen ADR erstellen, unter anderem für Folgendes (Richards und Ford 2020):

* Struktur (zum Beispiel Muster wie Microservices)

* Nichtfunktionale Anforderungen (Sicherheit, Hochverfügbarkeit und Fehlertoleranz)

* Abhängigkeiten (Kopplung von Komponenten)

* Schnittstellen (APIs und veröffentlichte Verträge)

* Konstruktionstechniken (Bibliotheken, Frameworks, Werkzeuge und Prozesse)

* Funktionale und nichtfunktionale Anforderungen sind die häufigsten Eingaben für den ADR-Prozess.


## Inhalt von ADRs

Wenn das Team den Bedarf an einem ADR erkennt, beginnt ein Teammitglied, den ADR auf Grundlage einer projektweiten Vorlage zu schreiben. (Beispielvorlagen finden Sie in der ADR-Organisation auf GitHub.) Die Vorlage vereinfacht die Erstellung von ADRs und stellt sicher, dass der ADR alle relevanten Informationen enthält. Mindestens sollte jeder ADR den Kontext der Entscheidung, die Entscheidung selbst und die Konsequenzen der Entscheidung für das Projekt und seine Liefergegenstände definieren. (Beispiele für diese Abschnitte finden Sie im Anhang.) Einer der wirkungsvollsten Aspekte der ADR-Struktur ist, dass sie sich auf den Grund für die Entscheidung konzentriert und nicht darauf, wie das Team sie umgesetzt hat. Wenn man versteht, warum das Team die Entscheidung getroffen hat, fällt es anderen Teammitgliedern leichter, sie zu übernehmen, und es verhindert, dass andere Architekten, die nicht am Entscheidungsprozess beteiligt waren, die Entscheidung in Zukunft übergehen.


## ADR-Einführungsprozess

Jedes Teammitglied kann einen ADR erstellen, aber das Team sollte eine Definition der Eigentümerschaft für einen ADR festlegen. Jeder Autor, der Eigentümer eines ADRs ist, sollte den ADR-Inhalt aktiv pflegen und kommunizieren. Um diese Eigentümerschaft zu verdeutlichen, bezeichnet dieser Leitfaden ADR-Autoren in den folgenden Abschnitten als ADR-Eigentümer. Andere Teammitglieder können jederzeit zu einem ADR beitragen. Wenn sich der Inhalt eines ADRs ändert, bevor das Team ihn annimmt, sollte der Eigentümer diese Änderungen genehmigen.

Nachdem das Team eine Architekturentscheidung und ihren Eigentümer identifiziert hat, legt der ADR-Eigentümer den ADR zu Beginn des Prozesses im Status **Proposed** (Vorgeschlagen) vor. ADRs im Status Proposed sind bereit zur Überprüfung.

Der ADR-Eigentümer startet dann den Überprüfungsprozess für den ADR. Das Ziel des ADR-Überprüfungsprozesses ist es zu entscheiden, ob das Team den ADR annimmt, feststellt, dass er überarbeitet werden muss, oder den ADR ablehnt. Das Projektteam, einschließlich des Eigentümers, überprüft den ADR. Die Überprüfungssitzung sollte mit einem eigens dafür vorgesehenen Zeitfenster zum Lesen des ADRs beginnen. Im Durchschnitt sollten 10 bis 15 Minuten ausreichen. Während dieser Zeit liest jedes Teammitglied das Dokument und fügt Kommentare und Fragen hinzu, um unklare Themen zu markieren. Nach der Überprüfungsphase liest der ADR-Eigentümer jeden Kommentar vor und bespricht ihn mit dem Team.

Wenn das Team Aktionspunkte zur Verbesserung des ADRs findet, bleibt der Status des ADRs **Proposed**. Der ADR-Eigentümer formuliert die Aktionen und weist in Zusammenarbeit mit dem Team jeder Aktion eine verantwortliche Person zu. Jedes Teammitglied kann zu den Aktionspunkten beitragen und sie abschließen. Es liegt in der Verantwortung des ADR-Eigentümers, den Überprüfungsprozess neu zu terminieren.

Das Team kann auch beschließen, den ADR abzulehnen. In diesem Fall fügt der ADR-Eigentümer eine Begründung für die Ablehnung hinzu, um künftige Diskussionen zum selben Thema zu vermeiden. Der Eigentümer ändert den ADR-Status auf **Rejected** (Abgelehnt).

Wenn das Team den ADR genehmigt, fügt der Eigentümer einen Zeitstempel, eine Version und eine Liste der Stakeholder hinzu. Anschließend aktualisiert der Eigentümer den Status auf **Accepted** (Angenommen).

ADRs und das Entscheidungsprotokoll, das sie bilden, stellen die vom Team getroffenen Entscheidungen dar und liefern eine Historie aller Entscheidungen. Das Team nutzt die ADRs nach Möglichkeit als Referenz bei Code- und Architektur-Reviews. Zusätzlich zur Durchführung von Code-Reviews, Entwurfsaufgaben und Implementierungsaufgaben sollten Teammitglieder ADRs für strategische Entscheidungen zum Produkt heranziehen.

Als gute Praxis sollte jede Softwareänderung Peer-Reviews durchlaufen und mindestens eine Freigabe erfordern. Während des Code-Reviews kann ein Prüfer Änderungen finden, die gegen einen oder mehrere ADRs verstoßen. In diesem Fall bittet der Prüfer den Autor der Codeänderung, den Code zu aktualisieren, und teilt einen Link zum ADR. Wenn der Autor den Code aktualisiert, wird er von den Peer-Prüfern freigegeben und in die Hauptcodebasis zusammengeführt.


## ADR-Überprüfungsprozess

Das Team sollte ADRs als unveränderliche Dokumente behandeln, nachdem das Team sie angenommen oder abgelehnt hat. Änderungen an einem bestehenden ADR erfordern die Erstellung eines neuen ADRs, die Einrichtung eines Überprüfungsprozesses für den neuen ADR und die Genehmigung des ADRs. Wenn das Team den neuen ADR genehmigt, sollte der Eigentümer den Status des alten ADRs auf **Superseded** (Ersetzt) ändern. 
