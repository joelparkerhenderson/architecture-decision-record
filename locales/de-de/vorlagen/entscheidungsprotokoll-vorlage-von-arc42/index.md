# Entscheidungsprotokoll-Vorlage von arc42

<https://arc42.org/overview>

## 1. Einführung und Ziele

Kurzbeschreibung der Anforderungen, treibenden Kräfte, Auszug (oder Abstrakt) der
Anforderungen. Die wichtigsten drei (maximal fünf) Qualitätsziele für die Architektur, die für
die wesentlichen Stakeholder höchste Priorität haben. Eine Tabelle wichtiger Stakeholder mit ihren
Erwartungen an die Architektur.

## 1.1 Aufgabenstellung

### Inhalt

Kurzbeschreibung der funktionalen Anforderungen, treibenden Kräfte, Auszug (oder Abstrakt) der
Anforderungen. Verweise auf (hoffentlich vorhandene) Anforderungsdokumente, mit Hinweisen, wo
diese zu finden sind. 

### Motivation

Aus Sicht der Endbenutzer wird ein System erstellt oder geändert, um die Unterstützung einer
Geschäftstätigkeit zu verbessern und/oder die Qualität zu steigern. 

### Form

Kurze Textbeschreibung, gegebenenfalls im tabellarischen Anwendungsfall-Format. Wenn
Anforderungsdokumente existieren, sollte diese Übersicht auf diese Dokumente verweisen.

Halten Sie diese Auszüge so kurz wie möglich. Wägen Sie die Lesbarkeit dieses Dokuments gegen
mögliche Redundanz zu den Anforderungsdokumenten ab. 

## 1.2 Qualitätsziele

### Inhalt

Die wichtigsten drei (maximal fünf) Qualitätsziele für die Architektur, deren Erfüllung für die
wesentlichen Stakeholder von höchster Bedeutung ist. Wir meinen wirklich Qualitätsziele für die
Architektur. Verwechseln Sie sie nicht mit Projektzielen. Sie sind nicht
notwendigerweise identisch. Die Norm ISO 25010 bietet einen guten Überblick über mögliche
Themen von Interesse.

### Motivation

Sie sollten die Qualitätsziele Ihrer wichtigsten Stakeholder kennen, da sie grundlegende
Architekturentscheidungen beeinflussen werden. Seien Sie bei diesen Qualitäten sehr
konkret und vermeiden Sie Schlagworte. Wenn Sie als Architekt nicht
wissen, wie die Qualität Ihrer Arbeit beurteilt wird …

### Form

Eine Tabelle mit den wichtigsten Qualitätszielen und konkreten Szenarien, nach Priorität geordnet.

## 1.3 Stakeholder

### Inhalt

Explizite Übersicht über die Stakeholder des Systems, das heißt alle Personen, Rollen oder
Organisationen, die

- die Architektur kennen sollten

- von der Architektur überzeugt werden müssen

- mit der Architektur oder mit Code arbeiten müssen

- die Dokumentation der Architektur für ihre Arbeit benötigen

- Entscheidungen über das System oder seine Entwicklung treffen müssen

### Motivation

Sie sollten alle an der Entwicklung des Systems beteiligten oder vom System betroffenen Parteien
kennen. Andernfalls erleben Sie später im Entwicklungsprozess möglicherweise unangenehme
Überraschungen. Diese Stakeholder bestimmen Umfang und Detaillierungsgrad Ihrer
Arbeit und ihrer Ergebnisse.

### Form

Tabelle mit Rollennamen, Personennamen und ihren Erwartungen an die
Architektur und ihre Dokumentation.

## 2. Randbedingungen

Alles, was Teams bei Entwurfs- und Implementierungsentscheidungen oder Entscheidungen über
verwandte Prozesse einschränkt. Kann manchmal über einzelne Systeme hinausgehen und
für ganze Organisationen und Unternehmen gelten.

### Inhalt

Alle Anforderungen, die Softwarearchitekten in ihrer Freiheit bei Entwurfs- und
Implementierungsentscheidungen oder Entscheidungen über den Entwicklungsprozess einschränken. Diese
Randbedingungen gehen manchmal über einzelne Systeme hinaus und gelten für ganze
Organisationen und Unternehmen.

### Motivation

Architekten sollten genau wissen, wo sie bei ihren Entwurfsentscheidungen frei sind und
wo sie Randbedingungen einhalten müssen. Randbedingungen müssen stets berücksichtigt werden;
sie können jedoch verhandelbar sein.

### Form

Einfache Tabellen mit Randbedingungen und Erläuterungen. Bei Bedarf können Sie sie
in technische Randbedingungen, organisatorische und politische Randbedingungen und
Konventionen (z. B. Programmier- oder Versionierungsrichtlinien, Dokumentations- oder Namenskonventionen) unterteilen

## 3. Kontextabgrenzung

Grenzt Ihr System von seinen (externen) Kommunikationspartnern (Nachbarsystemen
und Benutzern) ab. Legt die externen Schnittstellen fest. Dargestellt aus
fachlicher/domänenbezogener Sicht (immer) oder aus technischer Sicht (optional)

### Inhalt

Systemumfang und Kontext grenzen – wie der Name sagt – Ihr System (das heißt
Ihren Umfang) von allen seinen Kommunikationspartnern (Nachbarsystemen und Benutzern,
das heißt dem Kontext Ihres Systems) ab. Dadurch werden die externen Schnittstellen festgelegt.

Unterscheiden Sie bei Bedarf den fachlichen Kontext (domänenspezifische Ein- und
Ausgaben) vom technischen Kontext (Kanäle, Protokolle, Hardware).

### Motivation

Die fachlichen Schnittstellen und technischen Schnittstellen zu Kommunikationspartnern gehören
zu den kritischsten Aspekten Ihres Systems. Stellen Sie sicher, dass Sie sie vollständig
verstehen.

### Form

- Verschiedene Kontextdiagramme

- Listen von Kommunikationspartnern und ihren Schnittstellen.

## 3.1 Fachlicher Kontext

### Inhalt

Spezifikation aller Kommunikationspartner (Benutzer, IT-Systeme, …) mit
Erläuterungen zu domänenspezifischen Ein- und Ausgaben oder Schnittstellen. Optional können Sie
domänenspezifische Formate oder Kommunikationsprotokolle ergänzen.

### Motivation

Alle Stakeholder sollten verstehen, welche Daten mit der Umgebung
des Systems ausgetauscht werden.

### Form

Alle Arten von Diagrammen, die das System als Blackbox zeigen und die fachlichen
Schnittstellen zu Kommunikationspartnern festlegen.

Alternativ (oder zusätzlich) können Sie eine Tabelle verwenden. Der Titel der Tabelle ist
der Name Ihres Systems, die drei Spalten enthalten den Namen des Kommunikations-
partners, die Eingaben und die Ausgaben.

## 3.2 Technischer Kontext

### Inhalt

Technische Schnittstellen (Kanäle und Übertragungsmedien), die Ihr System mit
seiner Umgebung verbinden. Zusätzlich eine Zuordnung der domänenspezifischen Ein-/Ausgabe zu den
Kanälen, das heißt eine Erläuterung, welche Ein-/Ausgabe welchen Kanal nutzt.

### Motivation

Viele Stakeholder treffen Architekturentscheidungen auf Grundlage der technischen Schnittstellen
zwischen dem System und seinem Kontext. Insbesondere Infrastruktur- oder Hardware-
Entwerfer entscheiden diese technischen Schnittstellen.

### Form

Z. B. UML-Verteilungsdiagramm, das Kanäle zu Nachbarsystemen beschreibt, zusammen
mit einer Zuordnungstabelle, die die Beziehungen zwischen Kanälen und
Ein-/Ausgabe zeigt.

## 4. Lösungsstrategie

Zusammenfassung der grundlegenden Entscheidungen und Lösungsstrategien, die die
Architektur prägen. Kann Technologie, Zerlegung auf oberster Ebene, Ansätze zum Erreichen der
wichtigsten Qualitätsziele und relevante organisatorische Entscheidungen umfassen.

### Inhalt

Eine kurze Zusammenfassung und Erläuterung der grundlegenden Entscheidungen und Lösungsstrategien, die die Architektur des Systems prägen. Dazu gehören

- Technologieentscheidungen

- Entscheidungen zur Zerlegung des Systems auf oberster Ebene, z. B. die Verwendung eines Architekturmusters oder Entwurfsmusters

- Entscheidungen, wie zentrale Qualitätsziele erreicht werden

- relevante organisatorische Entscheidungen, z. B. die Wahl eines Entwicklungsprozesses oder die Delegation bestimmter Aufgaben an Dritte.

### Motivation

Diese Entscheidungen bilden die Eckpfeiler Ihrer Architektur. Sie sind die Grundlage
für viele weitere detaillierte Entscheidungen oder Implementierungsregeln.

### Form

Halten Sie die Erläuterung dieser Schlüsselentscheidungen kurz.

Begründen Sie, was Sie entschieden haben und warum Sie so entschieden haben, auf Grundlage Ihrer
Problemstellung, der Qualitätsziele und der wesentlichen Randbedingungen. Verweisen Sie auf Details in
den folgenden Abschnitten (Abschnitt 5 für strukturelle Details, Abschnitt 8 für
übergreifende Konzepte).

Sie können eine Liste von Lösungsansätzen oder eine Tabelle verwenden.

## 5. Bausteinsicht

Statische Zerlegung des Systems, Abstraktionen des Quellcodes, dargestellt als
Hierarchie von Whiteboxen (die Blackboxen enthalten), bis zum angemessenen Detaillierungsgrad.

### Inhalt

Die Bausteinsicht zeigt die statische Zerlegung des Systems in
Bausteine (Module, Komponenten, Subsysteme, Klassen, Schnittstellen, Pakete,
Bibliotheken, Frameworks, Schichten, Partitionen, Ebenen, Funktionen, Makros, Operationen,
Datenstrukturen, …) sowie ihre Abhängigkeiten (Beziehungen, Assoziationen,
…)

Diese Sicht ist für jede Architekturdokumentation verpflichtend. In Analogie zu einem
Haus ist dies der Grundriss.

### Motivation

Behalten Sie den Überblick über Ihren Quellcode, indem Sie seine Struktur durch
Abstraktion verständlich machen.

So können Sie mit Ihren Stakeholdern auf abstrakter Ebene kommunizieren,
ohne Implementierungsdetails offenzulegen.

### Form

Die Bausteinsicht ist eine hierarchische Sammlung von Blackboxen und Whiteboxen
(siehe Abbildung unten) und ihrer Beschreibungen.

## 5.1 Whitebox Gesamtsystem

Hier beschreiben Sie die Zerlegung des Gesamtsystems anhand der folgenden Whitebox-Vorlage. Sie enthält

- ein Übersichtsdiagramm

- eine Begründung für die Zerlegung

- Blackbox-Beschreibungen der enthaltenen Bausteine. Hierfür bieten wir Ihnen Alternativen an:

  - eine Tabelle für einen kurzen und pragmatischen Überblick über alle enthaltenen Bausteine und ihre Schnittstellen

  - eine Liste von Blackbox-Beschreibungen der Bausteine gemäß der Blackbox-Vorlage (siehe unten). Je nach Wahl Ihres Werkzeugs könnte diese Liste aus Unterkapiteln (in Textdateien), Unterseiten (in einem Wiki) oder verschachtelten Elementen (in einem Modellierungswerkzeug) bestehen.

  - (optional:) wichtige Schnittstellen, die in den Blackbox-Vorlagen eines Bausteins nicht erläutert werden, aber für das Verständnis der Whitebox sehr wichtig sind.

Da es so viele Möglichkeiten gibt, Schnittstellen zu spezifizieren, bieten wir dafür keine spezielle Vorlage an.

Im besten Fall kommen Sie mit Beispielen oder einfachen Signaturen aus.

## 5.2 Ebene 2

Hier können Sie die innere Struktur (einiger) Bausteine aus Ebene 1
als Whiteboxen spezifizieren.

Sie müssen entscheiden, welche Bausteine Ihres Systems wichtig genug sind, um
eine so detaillierte Beschreibung zu rechtfertigen. Bevorzugen Sie Relevanz vor Vollständigkeit.
Spezifizieren Sie wichtige, überraschende, riskante, komplexe oder volatile Bausteine. Lassen Sie
normale, einfache, langweilige oder standardisierte Teile Ihres Systems weg

### 5.2.1 Whitebox für Baustein 1

Spezifiziert die innere Struktur von Baustein 1.

Verwenden Sie die Whitebox-Vorlage (siehe oben).

## 6. Laufzeitsicht

Verhalten von Bausteinen als Szenarien, die wichtige Anwendungsfälle oder
Features, Interaktionen an kritischen externen Schnittstellen, Betrieb und
Administration sowie Fehler- und Ausnahmeverhalten abdecken.

### Inhalt

Die Laufzeitsicht beschreibt konkretes Verhalten und Interaktionen der Bausteine des Systems in Form von Szenarien aus den folgenden Bereichen:

- wichtige Anwendungsfälle oder Features: Wie führen Bausteine sie aus?

- Interaktionen an kritischen externen Schnittstellen: Wie arbeiten Bausteine mit Benutzern und Nachbarsystemen zusammen?

- Betrieb und Administration: Start, Hochfahren, Stoppen

- Fehler- und Ausnahmeszenarien

Anmerkung: Das wichtigste Kriterium für die Auswahl möglicher Szenarien (Abläufe, Workflows) ist ihre architektonische Relevanz. Es ist nicht wichtig, eine große Anzahl von Szenarien zu beschreiben. Dokumentieren Sie vielmehr eine repräsentative Auswahl.

### Motivation

Sie sollten verstehen, wie (Instanzen von) Bausteinen Ihres Systems ihre Aufgabe erfüllen und zur Laufzeit kommunizieren. Sie werden Szenarien vor allem in Ihrer Dokumentation erfassen, um Ihre Architektur Stakeholdern zu vermitteln, die weniger bereit oder in der Lage sind, die statischen Modelle (Bausteinsicht, Verteilungssicht) zu lesen und zu verstehen.

### Form

Es gibt viele Notationen zur Beschreibung von Szenarien, z. B.


- nummerierte Liste von Schritten (in natürlicher Sprache)

- Aktivitätsdiagramme oder Flussdiagramme

- Sequenzdiagramme

- BPMN oder EPKs (ereignisgesteuerte Prozessketten)

- Zustandsautomaten

- usw.

## 6.n Laufzeitszenario n (1, 2, 3 usw.)

Fügen Sie ein Laufzeitdiagramm oder eine Textbeschreibung des Szenarios ein.

Fügen Sie eine Beschreibung der bemerkenswerten Aspekte der Interaktionen zwischen den in diesem Diagramm dargestellten Bausteininstanzen ein.

## 7. Verteilungssicht

Technische Infrastruktur mit Umgebungen, Rechnern, Prozessoren, Topologien.
Zuordnung von (Software-)Bausteinen zu Infrastrukturelementen.

### Inhalt

Die Verteilungssicht beschreibt:

- die technische Infrastruktur, die zur Ausführung Ihres Systems verwendet wird, mit Infrastruktur-
  elementen wie geografischen Standorten, Umgebungen, Rechnern, Prozessoren,
  Kanälen und Netztopologien sowie anderen Infrastrukturelementen und

- die Zuordnung von (Software-)Bausteinen zu diesen Infrastrukturelementen.

Oft werden Systeme in verschiedenen Umgebungen ausgeführt, z. B. Entwicklungs-
umgebung, Testumgebung, Produktionsumgebung. In solchen Fällen sollten Sie
alle relevanten Umgebungen dokumentieren.

Dokumentieren Sie die Verteilungssicht insbesondere, wenn Ihre Software als
verteiltes System mit mehr als einem Rechner, Prozessor, Server oder Container ausgeführt wird
oder wenn Sie eigene Hardware-Prozessoren und Chips entwerfen und bauen.

Aus Softwaresicht genügt es, die Elemente der
Infrastruktur zu erfassen, die zur Darstellung der Verteilung Ihrer Bausteine benötigt werden.
Hardwarearchitekten können darüber hinausgehen und die Infrastruktur in jedem
Detaillierungsgrad beschreiben, den sie erfassen müssen. 

### Motivation

Software läuft nicht ohne Hardware. Diese zugrunde liegende Infrastruktur kann und
wird Ihr System und/oder einige übergreifende Konzepte beeinflussen. Daher
müssen Sie die Infrastruktur kennen.

### Form

Möglicherweise ist das Verteilungsdiagramm auf höchster Ebene bereits in Abschnitt 3.2 als technischer Kontext mit Ihrer eigenen Infrastruktur als EINE Blackbox enthalten. In diesem Abschnitt zoomen Sie mit zusätzlichen Verteilungsdiagrammen in diese Blackbox hinein.

- UML bietet Verteilungsdiagramme, um diese Sicht auszudrücken. Verwenden Sie sie, gegebenenfalls mit verschachtelten Diagrammen, wenn Ihre Infrastruktur komplexer ist.

- Wenn Ihre (Hardware-)Stakeholder andere Arten von Diagrammen gegenüber dem
  UML-Verteilungsdiagramm bevorzugen, lassen Sie sie jede Art verwenden, die Knoten und
  Kanäle der Infrastruktur darstellen kann.

## 7.1 Infrastruktur Ebene 1

Beschreiben Sie (üblicherweise in einer Kombination aus Diagrammen, Tabellen und Text):

- die Verteilung Ihres Systems auf mehrere Standorte, Umgebungen, Rechner, Prozessoren, .. sowie die physischen Verbindungen zwischen ihnen

- wichtige Begründung oder Motivation für diese Verteilungsstruktur

- Qualitäts- und/oder Leistungsmerkmale der Infrastruktur

- die Zuordnung von Softwareartefakten (Bausteinen) zu Elementen der Infrastruktur

Für mehrere Umgebungen oder alternative Verteilungen kopieren Sie bitte diesen Abschnitt von arc42 für alle relevanten Umgebungen. **

## 7.2 Infrastruktur Ebene 2

Hier können Sie die innere Struktur (einiger) Infrastrukturelemente aus Infrastruktur Ebene 1 aufnehmen.

Bitte kopieren Sie die Struktur aus Ebene 1 für jedes ausgewählte Element.

## 8. Querschnittliche Konzepte

Insgesamt grundlegende Regelungen und Lösungsansätze, die in mehreren
Teilen (→ querschnittlich) des Systems relevant sind. Konzepte beziehen sich oft auf mehrere
Bausteine. Beziehen Sie verschiedene Themen ein, wie Domänenmodelle, Architektur-
muster und -stile, Regeln für den Einsatz bestimmter Technologien und Implementierungs-
regeln.

### Inhalt

Dieser Abschnitt beschreibt querschnittliche Konzepte (Praktiken, Muster, Regelungen
oder Lösungsideen). Solche Konzepte beziehen sich oft auf mehrere Bausteine.
Sie können viele verschiedene Themen umfassen.

### Motivation

Konzepte bilden die Grundlage für die konzeptionelle Integrität (Konsistenz, Homogenität) der
Architektur. Damit sind sie ein wichtiger Beitrag, um die inneren
Qualitäten Ihres Systems zu erreichen.

Dies ist die Stelle in der Vorlage, die wir für eine zusammenhängende Spezifikation
solcher Konzepte vorgesehen haben.

Viele dieser Konzepte beziehen sich auf mehrere Ihrer Bausteine oder beeinflussen sie.

### Form

Die Form kann variieren:

- Konzeptpapiere mit beliebiger Struktur

- Beispielimplementierungen, insbesondere für technische Konzepte

- querschnittliche Modellauszüge oder Szenarien in der Notation der Architektursichten

### Struktur dieses Abschnitts

Wählen Sie nur die für Ihr System wichtigsten Themen aus und weisen Sie jedem eine Überschrift der Ebene 2 in diesem Abschnitt zu (z. B. 8.1, 8.2 usw.).

- VERSUCHEN SIE NICHT, alle Themen des oben genannten Diagramms abzudecken.

### Hintergrund

Manche Themen innerhalb von Systemen betreffen oft mehrere Bausteine, Hardware-
elemente oder Entwicklungsprozesse. Es kann einfacher sein, solche
querschnittlichen Themen an zentraler Stelle zu kommunizieren oder zu dokumentieren, statt sie in
der Beschreibung der betroffenen Bausteine, Hardwareelemente oder
Entwicklungsprozesse zu wiederholen.

Bestimmte Konzepte betreffen möglicherweise alle Elemente eines Systems, andere sind nur
für wenige relevant.

## 9. Architekturentscheidungen

Wichtige, teure, kritische, großskalige oder riskante Architekturentscheidungen
einschließlich Begründungen.

### Inhalt

Wichtige, teure, großskalige oder riskante Architekturentscheidungen einschließlich
Begründungen. Mit „Entscheidungen“ meinen wir die Auswahl einer Alternative anhand
vorgegebener Kriterien.

Bitte entscheiden Sie nach eigenem Ermessen, ob eine Architekturentscheidung
hier in diesem zentralen Abschnitt dokumentiert werden sollte oder ob Sie sie besser
lokal dokumentieren (z. B. innerhalb der Whitebox-Vorlage eines Bausteins). Vermeiden Sie
redundante Texte. Verweisen Sie auf Abschnitt 4, in dem Sie die wichtigsten
Entscheidungen Ihrer Architektur bereits erfasst haben.

### Motivation

Stakeholder Ihres Systems sollten Ihre Entscheidungen nachvollziehen und
zurückverfolgen können.

### Form

- ADR (Architecture Decision Record) für jede wichtige Entscheidung

- Liste oder Tabelle, geordnet nach Wichtigkeit und Konsequenzen oder

- ausführlicher in Form separater Abschnitte pro Entscheidung

### Hintergrund (zu ADRs)

Kleinere Dokumentationsstücke sind leichter zu lesen, zu erstellen und zu pflegen. Bei
Architekturentscheidungen werden Entwicklungsteams oft:

- die Entscheidung kennen, da sie z. B. im Quellcode sichtbar ist, aber

- die Motivation hinter dieser Entscheidung nicht kennen (siehe Nygard 2011)

Daher sollten Sie einige wichtige Entscheidungen zusammen mit ihrer
Motivation und Begründung dokumentieren

### Unser Vorschlag zu Entscheidungen

Führen Sie eine Sammlung architektonisch bedeutsamer Entscheidungen, also derjenigen Entscheidungen, die
die Struktur, Qualitätsmerkmale, wichtige (insbesondere externe)
Abhängigkeiten und Schnittstellen oder Konstruktionstechniken betreffen (Dank an Michael
Nygard für diesen Vorschlag).

## 10. Qualitätsanforderungen

Qualitätsanforderungen als Szenarien, mit einem Qualitätsbaum, der einen Überblick auf hoher Ebene gibt.
Die wichtigsten Qualitätsziele sollten bereits in Abschnitt
1.2. (Qualitätsziele) beschrieben worden sein.

### Inhalt

Dieser Abschnitt enthält alle relevanten Qualitätsanforderungen.

Die wichtigsten dieser Anforderungen wurden bereits in Abschnitt
1.2. (Qualitätsziele) beschrieben, daher sollten sie hier nur referenziert werden. In diesem
Abschnitt 10 sollten Sie auch Qualitätsanforderungen von geringerer Wichtigkeit erfassen,
die keine hohen Risiken erzeugen, wenn sie nicht vollständig erreicht werden (aber vielleicht
wünschenswert sind).

### Motivation

Da Qualitätsanforderungen großen Einfluss auf Architektur-
entscheidungen haben werden, sollten Sie wissen, welche Qualitäten für
Ihre Stakeholder wirklich wichtig sind, auf konkrete und messbare Weise.

### Weitere Informationen

Siehe das umfassende Q42-Qualitätsmodell auf https://quality.arc42.org.

## 10.1 Übersicht der Qualitätsanforderungen

### Inhalt

Eine Übersicht oder Zusammenfassung der Qualitätsanforderungen.

### Motivation

Oft begegnen uns Dutzende (oder sogar Hunderte) detaillierter Qualitätsanforderungen.
In diesem Übersichtsabschnitt sollten Sie versuchen, zusammenzufassen, z. B. indem Sie
Kategorien oder Themen beschreiben (wie von ISO 25010:2023 oder Q42 vorgeschlagen

Wenn diese zusammenfassenden Beschreibungen bereits präzise, spezifisch genug und
messbar sind, können Sie Abschnitt 10.2 überspringen.

### Form

Verwenden Sie eine einfache Tabelle, in der jede Zeile eine Kategorie oder ein Thema und eine kurze
Beschreibung der Qualitätsanforderung enthält. Alternativ können Sie eine Mindmap nutzen, um
diese Qualitätsanforderungen zu strukturieren.

In der Literatur wurde auch die Idee eines Qualitätsattribut-Baums beschrieben,
der den allgemeinen Begriff „Qualität“ als Wurzel setzt und eine baumartige
Verfeinerung des Begriffs „Qualität“ verwendet. [Bass+21] führte dafür den Begriff „Quality
Attribute Utility Tree“ ein.

## 10.2 Qualitätsszenarien

### Inhalt

Qualitätsszenarien machen Qualitätsanforderungen konkret und erlauben es zu entscheiden, ob
sie erfüllt sind (im Sinne von Abnahmekriterien). Stellen Sie sicher, dass Ihre
Szenarien spezifisch und messbar sind.

Zwei Arten von Szenarien sind besonders nützlich:

- Nutzungsszenarien (auch Anwendungsszenarien oder Anwendungsfallszenarien genannt)
  beschreiben die Laufzeitreaktion des Systems auf einen bestimmten Stimulus. Dazu
  gehören auch Szenarien, die die Effizienz oder Leistung des Systems beschreiben.
  Beispiel: Das System reagiert innerhalb einer Sekunde auf eine Benutzeranfrage.

- Änderungsszenarien beschreiben die gewünschte Wirkung einer Änderung oder Erweiterung
  des Systems oder seiner unmittelbaren Umgebung. Beispiel: Zusätzliche Funktionalität
  wird implementiert oder Anforderungen an ein Qualitätsattribut ändern sich, und der Aufwand oder
  die Dauer der Änderung wird gemessen.

### Form

Typische Informationen für detaillierte Szenarien umfassen Folgendes:

In Kurzform (im Q42-Modell bevorzugt):

- Kontext/Hintergrund: Welche Art von System oder Komponente, was ist die Umgebung oder Situation?

- Quelle/Stimulus: Wer oder was löst ein Verhalten, eine Reaktion oder eine Aktion aus.

- Metrik/Akzeptanzkriterium: Eine Reaktion einschließlich eines Maßes oder einer Metrik

Die Langform von Szenarien (vom SEI und [Bass+21] bevorzugt) ist detaillierter und enthält die folgenden Informationen:

- Szenario-ID: Ein eindeutiger Bezeichner für das Szenario.

- Szenarioname: Ein kurzer, beschreibender Name für das Szenario.

- Quelle: Die Entität (Benutzer, System oder Ereignis), die das Szenario auslöst.

- Stimulus: Das auslösende Ereignis oder die auslösende Bedingung, die das System behandeln muss.

- Umgebung: Der betriebliche Kontext oder die Bedingung, unter der das System den Stimulus erfährt.

- Artefakt: Die Bausteine oder anderen Elemente des Systems, die vom Stimulus betroffen sind.

- Reaktion: Das Ergebnis oder Verhalten, das das System als Reaktion auf den Stimulus zeigt.

- Reaktionsmaß: Das Kriterium oder die Metrik, anhand derer die Reaktion des Systems bewertet wird.

### Siehe auch

Seit Januar 2023 bietet arc42 ein pragmatisches Qualitätsmodell, das vorschlägt,
Qualitätsanforderungen mit Hashtags oder Labels wie #flexible, #efficient,
#usable, #operable, #testable, #secure, #safe, #reliable zu versehen.

## 11. Risiken und technische Schulden

Bekannte technische Risiken oder technische Schulden. Welche potenziellen Probleme gibt es im oder
um das System? Womit ist das Entwicklungsteam unzufrieden?

### Inhalt

Eine Liste identifizierter technischer Risiken oder technischer Schulden, nach Priorität geordnet

### Motivation

„Risikomanagement ist Projektmanagement für Erwachsene“ (Tim Lister, Atlantic
Systems Guild.)

Dies sollte Ihr Motto für die systematische Erkennung und Bewertung von Risiken und
technischen Schulden in der Architektur sein, die vom Management
(z. B. Projektmanager, Product Owner) als Teil der gesamten Risiko-
analyse und Maßnahmenplanung benötigt werden.

### Form

Liste von Risiken und/oder technischen Schulden, gegebenenfalls einschließlich vorgeschlagener Maßnahmen, um
Risiken zu minimieren, abzumildern oder zu vermeiden oder technische Schulden zu verringern.

