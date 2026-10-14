# Architecture Decision Record (ADR)

Ein Architecture Decision Record (ADR) ist ein Dokument, das eine wichtige Architekturentscheidung zusammen mit ihrem Kontext und ihren Konsequenzen festhält.

> [!IMPORTANT]
> Führen Sie Ihre eigene Sorgfaltsprüfung dieser Ressourcen durch, bevor Sie sie in kritischen Systemen einsetzen.

Inhalt:

- [Was ist ein Architecture Decision Record?](#was-ist-ein-architecture-decision-record)
- [Erste Schritte mit ADRs](#erste-schritte-mit-adrs)
- [Erste Schritte mit ADRs und Werkzeugen](#erste-schritte-mit-adrs-und-werkzeugen)
- [Erste Schritte mit ADRs und Git](#erste-schritte-mit-adrs-und-git)
- [Claude-Code-Skills für ADRs](#claude-code-skills-für-adrs)
- [Dateinamenskonventionen](#dateinamenskonventionen)
- [Empfehlungen für gute ADRs](#empfehlungen-für-gute-adrs)
- [ADR-Beispielvorlagen](#adr-beispielvorlagen)
- [Ratschläge zur Teamarbeit für ADRs](#ratschläge-zur-teamarbeit-für-adrs)
- [Teamarbeit-Fragen für ADRs](#teamarbeit-fragen-für-adrs)
- [Konzepte für den nächsten Schritt bei ADRs](#konzepte-für-den-nächsten-schritt-bei-adrs)
- [Architekturdiagramme, Sichten und Blickwinkel](#architekturdiagramme-sichten-und-blickwinkel)
- [Fitnessfunktionen für Entscheidungen als Code](#fitnessfunktionen-für-entscheidungen-als-code)
- [Entscheidungs-Leitplanken für Pull Requests](#entscheidungs-leitplanken-für-pull-requests)
- [Weitere Informationen](#weitere-informationen)

Vorlagen:

- [Entscheidungsprotokoll-Vorlage von Jeff Tyree und Art Akerman](vorlagen/entscheidungsprotokoll-vorlage-von-jeff-tyree-und-art-akerman/)
- [Entscheidungsprotokoll-Vorlage von Michael Nygard](vorlagen/entscheidungsprotokoll-vorlage-von-michael-nygard/)
- [Entscheidungsprotokoll-Vorlage von EdgeX](vorlagen/entscheidungsprotokoll-vorlage-von-edgex/)
- [Entscheidungsprotokoll-Vorlage von arc42](vorlagen/entscheidungsprotokoll-vorlage-von-arc42/)
- [Entscheidungsprotokoll-Vorlage für das Alexandrian-Muster](vorlagen/entscheidungsprotokoll-vorlage-für-das-alexandrian-muster/)
- [Entscheidungsprotokoll-Vorlage für Business Cases](vorlagen/entscheidungsprotokoll-vorlage-für-business-cases/)
- [Entscheidungsprotokoll-Vorlage des MADR-Projekts](vorlagen/entscheidungsprotokoll-vorlage-des-madr-projekts/)
- [Entscheidungsprotokoll-Vorlage mit Planguage](vorlagen/entscheidungsprotokoll-vorlage-mit-planguage/)
- [Entscheidungsprotokoll-Vorlage von Paulo Merson](https://github.com/pmerson/ADR-template)
- [Entscheidungsprotokoll-Vorlage von Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Entscheidungsprotokoll-Vorlage von Gareth Morgan](vorlagen/entscheidungsprotokoll-vorlage-von-gareth-morgan/)
- [Entscheidungsprotokoll-Vorlage von GIG Cymru NHS Wales](vorlagen/entscheidungsprotokoll-vorlage-von-gig-cymru-nhs-wales/)
- [Entscheidungsprotokoll-Vorlage für Wichtige Technische Entscheidungen (ITDs) von Ignacio Larrañaga](vorlagen/entscheidungsprotokoll-vorlage-für-wichtige-technische-entscheidungen/)

Beispiele:

- [CSS-Framework](beispiele/css-framework/)
- [Konfiguration über Umgebungsvariablen](beispiele/konfiguration-über-umgebungsvariablen/)
- [Metriken, Überwachung, Alarme](beispiele/metriken-überwachung-alarme/)
- [Microsoft Azure DevOps](beispiele/microsoft-azure-devops/)
- [Monorepo oder Multirepo](beispiele/monorepo-oder-multirepo/)
- [Programmiersprachen](beispiele/programmiersprachen/)
- [Speicherung von Geheimnissen](beispiele/speicherung-von-geheimnissen/)
- [Zeitstempelformat](beispiele/zeitstempelformat/)
- [Viele weitere...](beispiele/)

## Was ist ein Architecture Decision Record?

Ein **Architecture Decision Record** (ADR) ist ein Dokument, das eine wichtige getroffene Architekturentscheidung zusammen mit ihrem Kontext und ihren Konsequenzen festhält.

Eine **Architekturentscheidung** (architecture decision, AD) ist eine Entwurfsentscheidung der Software, die eine wesentliche Anforderung adressiert.

Ein **Architekturentscheidungsprotokoll** (architecture decision log, ADL) ist die Sammlung aller ADRs, die für ein bestimmtes Projekt (oder eine Organisation) erstellt und gepflegt werden.

Eine **architektonisch bedeutsame Anforderung** (architecturally-significant requirement, ASR) ist eine Anforderung, die einen messbaren Einfluss auf die Architektur eines Softwaresystems hat.

All dies gehört zum Thema **Architekturwissensmanagement** (architecture knowledge management, AKM).

Ziel dieses Dokuments ist es, einen schnellen Überblick über ADRs zu geben, darüber, wie man sie erstellt, und wo man weitere Informationen findet.

Abkürzungen:

  * **AD**: Architekturentscheidung

  * **ADL**: Architekturentscheidungsprotokoll

  * **ADR**: Architecture Decision Record

  * **AKM**: Architekturwissensmanagement

  * **ASR**: architektonisch bedeutsame Anforderung

## Erste Schritte mit ADRs

Um mit ADRs zu beginnen, sprechen Sie mit Ihren Teamkollegen über diese Bereiche.

Entscheidungsidentifikation:

  * Wie dringend und wie wichtig ist die AD?

  * Muss sie jetzt getroffen werden, oder kann sie warten, bis mehr bekannt ist?

  * Sowohl persönliche als auch kollektive Erfahrung sowie anerkannte Entwurfsmethoden und -praktiken können bei der Entscheidungsidentifikation helfen.

  * Pflegen Sie idealerweise eine Entscheidungs-Aufgabenliste, die die Produkt-Aufgabenliste ergänzt.

Entscheidungsfindung:

  * Es gibt eine Reihe von Entscheidungstechniken, sowohl allgemeine als auch solche speziell für Softwarearchitektur, zum Beispiel Dialogue Mapping.

  * Gruppenentscheidungen sind ein aktives Forschungsthema.

Umsetzung und Durchsetzung von Entscheidungen:

  * ADs werden im Softwareentwurf verwendet; daher müssen sie den Stakeholdern des Systems, die es finanzieren, entwickeln und betreiben, vermittelt und von ihnen akzeptiert werden.

  * Architektonisch erkennbare Programmierstile und Code-Reviews, die sich auf architektonische Belange und Entscheidungen konzentrieren, sind zwei verwandte Praktiken.

  * ADs müssen auch (erneut) berücksichtigt werden, wenn ein Softwaresystem in der Softwareevolution modernisiert wird.

Entscheidungsaustausch (optional):

  * Viele ADs wiederholen sich in Projekten.

  * Daher können Erfahrungen mit früheren Entscheidungen, gute wie schlechte, wertvolle wiederverwendbare Assets sein, wenn eine explizite Wissensmanagementstrategie eingesetzt wird.

Entscheidungsdokumentation:

  * Es gibt viele Vorlagen und Werkzeuge zur Erfassung von Entscheidungen.

  * Siehe agile Communities, zum Beispiel die ADRs von M. Nygard.

  * Siehe traditionelle Softwareentwicklungs- und Architekturentwurfsprozesse, zum Beispiel die von IBM UMF und von Tyree und Akerman von CapitalOne vorgeschlagenen Tabellenlayouts.

Weitere Informationen:

  * Die obigen Schritte sind dem Wikipedia-Eintrag zu [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision) entnommen

## Erste Schritte mit ADRs und Werkzeugen

- [MySpec](https://myspec.dev) — Automatisierte Spezifikations- und Architekturentscheidungsplattform, die Projektverfassung, technische Architektur und ADRs in sauberem Markdown strukturiert, das über MCP bereitgestellt wird.

Sie können mit ADRs und Werkzeugen auf jede beliebige Weise beginnen.

Zum Beispiel:

  * Wenn Sie Google Drive und Online-Bearbeitung mögen, können Sie ein Google Doc oder Google Sheet erstellen.

  * Wenn Sie Quellcode-Versionskontrolle wie Git mögen, können Sie für jeden ADR eine Datei erstellen.

  * Wenn Sie Projektplanungswerkzeuge wie Atlassian Jira mögen, können Sie den Planungs-Tracker des Werkzeugs nutzen.

  * Wenn Sie Wikis wie MediaWiki mögen, können Sie ein ADR-Wiki erstellen.

## Erste Schritte mit ADRs und Git

Wenn Sie die Versionskontrolle mit Git mögen, so beginnen wir gern mit ADRs und Git für ein typisches Softwareprojekt mit Quellcode.

Erstellen Sie ein Verzeichnis für ADR-Dateien:

```sh
$ mkdir adr
```

Erstellen Sie für jeden ADR eine Textdatei, zum Beispiel `database.txt`:

```sh
$ vi database.txt
```

Schreiben Sie in den ADR, was immer Sie möchten. Ideen finden Sie in den Vorlagen in diesem Repository.

Committen Sie den ADR in Ihr Git-Repository.

## Claude-Code-Skills für ADRs

Dieses Repository liefert zwei [Claude-Code](https://claude.com/claude-code)-Skills unter [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/) mit, damit ein KI-Coding-Agent ADRs so schreiben und pflegen kann, wie dieses Projekt es empfiehlt:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — für den allgemeinen Gebrauch, für alle, die in einem beliebigen Projekt einen ADR schreiben. Hilft zu entscheiden, ob eine Entscheidung einen ADR braucht, legt ein Verzeichnis `adr/` oder `decisions/` an, benennt die Datei, wählt eine Vorlage aus den elf mitgelieferten Gerüsten und schreibt solide Abschnitte zu Kontext, Entscheidung und Konsequenzen.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — speziell für die Betreuer dieses Repositorys. Dokumentiert den Aufbau des Repositorys, die Konvention zur Spiegelung von README und locales sowie die genauen Schritte zum Hinzufügen einer neuen Vorlage, eines Beispiels oder eines Werkzeug-Links.

Um einen Skill zu verwenden, kopieren Sie seinen Ordner nach `.claude/skills/` im Wurzelverzeichnis des Repositorys, in dem Sie arbeiten (oder nach `~/.claude/skills/`, um ihn in jedem Projekt verfügbar zu machen), und bitten Sie dann Claude Code, einen ADR zu schreiben oder zu prüfen.

## Dateinamenskonventionen

Wenn Sie Ihre ADRs als gewöhnliche Textdateien erstellen, möchten Sie vielleicht eine eigene Dateinamenskonvention für ADR-Dateien festlegen.

Wir bevorzugen eine Dateinamenskonvention mit einem bestimmten Format.

Beispiele:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Unsere Dateinamenskonvention:

  * Der Name besteht aus einer Verbalphrase im Imperativ der Gegenwart. Das verbessert die Lesbarkeit und passt zu unserem Format für Commit-Nachrichten.

  * Der Name verwendet Kleinbuchstaben und Bindestriche (wie dieses Repository). Das ist ein Kompromiss zwischen Lesbarkeit und Systemtauglichkeit.

  * Die Erweiterung ist Markdown. Das kann für eine einfache Formatierung nützlich sein.

## Empfehlungen für gute ADRs

Merkmale eines guten ADRs:

* Begründung: Erklären Sie die Gründe für die jeweilige AD. Das kann den Kontext (siehe unten), Vor- und Nachteile verschiedener möglicher Optionen, Funktionsvergleiche, Kosten-Nutzen-Erörterungen und mehr umfassen.

* Spezifisch: Jeder ADR sollte sich auf eine AD beziehen, nicht auf mehrere ADs.

* Zeitstempel: Geben Sie an, wann jeder Punkt im ADR geschrieben wurde. Das ist besonders wichtig für Aspekte, die sich im Lauf der Zeit ändern können, wie Kosten, Zeitpläne, Skalierung und Ähnliches.

* Unveränderlich: Ändern Sie keine vorhandenen Informationen in einem ADR. Ergänzen Sie den ADR stattdessen durch neue Informationen oder ersetzen Sie ihn durch einen neuen ADR.

Merkmale eines guten Abschnitts „Kontext“ in einem ADR:

* Erklären Sie die Situation und die geschäftlichen Prioritäten Ihrer Organisation.

* Beziehen Sie Begründungen und Überlegungen ein, die auf der sozialen und fachlichen Zusammensetzung Ihrer Teams beruhen.

* Nennen Sie relevante Vor- und Nachteile und beschreiben Sie sie so, dass sie zu Ihren Bedürfnissen und Zielen passen.

Merkmale eines guten Abschnitts „Konsequenzen“ in einem ADR:

* Erklären Sie, was aus der Entscheidung folgt. Das kann Auswirkungen, Ergebnisse, Ausgaben, Folgemaßnahmen und mehr umfassen.

* Nennen Sie Informationen zu nachfolgenden ADRs. Es ist relativ üblich, dass ein ADR den Bedarf an weiteren ADRs auslöst, etwa wenn ein ADR eine große übergreifende Entscheidung trifft, die wiederum Bedarf an weiteren kleineren Entscheidungen schafft.

* Beziehen Sie Nachbetrachtungsprozesse ein. Es ist üblich, dass Teams jeden ADR einen Monat später überprüfen, um die ADR-Informationen mit dem zu vergleichen, was in der Praxis geschehen ist, um zu lernen und zu wachsen.

Ein neuer ADR kann einen früheren ADR ersetzen:

* Wenn eine AD getroffen wird, die einen früheren ADR ersetzt oder ungültig macht, sollte ein neuer ADR erstellt werden

## ADR-Beispielvorlagen

ADR-Beispielvorlagen, die wir im Netz gesammelt haben:

- [ADR-Vorlage von Michael Nygard](vorlagen/entscheidungsprotokoll-vorlage-von-michael-nygard/) (einfach und beliebt)

- [ADR-Vorlage von Jeff Tyree und Art Akerman](vorlagen/entscheidungsprotokoll-vorlage-von-jeff-tyree-und-art-akerman/) (anspruchsvoller)

- [ADR-Vorlage für das Alexandrian-Muster](vorlagen/entscheidungsprotokoll-vorlage-für-das-alexandrian-muster/) (einfach, mit Kontextdetails)

- [ADR-Vorlage für einen Business Case](vorlagen/entscheidungsprotokoll-vorlage-für-business-cases/) (stärker auf MBA ausgerichtet, mit Kosten, SWOT und mehr Meinungen)

- [ADR-Vorlage des Projekts Markdown Any Decision Records (MADR)](vorlagen/entscheidungsprotokoll-vorlage-des-madr-projekts/) (sowohl einfache als auch ausführliche Version; die letztere betont Optionen und ihre Vor- und Nachteile)

- [ADR-Vorlage mit Planguage](vorlagen/entscheidungsprotokoll-vorlage-mit-planguage/) (stärker auf Qualitätssicherung ausgerichtet)

- [Vorlage für Important Technical Decisions (ITDs) von Ignacio Larrañaga](vorlagen/entscheidungsprotokoll-vorlage-für-wichtige-technische-entscheidungen/) (schlank und entscheidungsorientiert, optimiert für schnelle Prüfung durch Führungskräfte)

## Ratschläge zur Teamarbeit für ADRs

Wenn Sie erwägen, Entscheidungsprotokolle mit Ihrem Team zu verwenden, finden Sie hier einige Ratschläge, die wir durch die Arbeit mit vielen Teams gelernt haben.

Sie haben die Gelegenheit, Ihre Teamkollegen zu führen, indem Sie gemeinsam über das „Warum“ sprechen, statt das „Was“ vorzuschreiben. Entscheidungsprotokolle sind zum Beispiel ein Weg für Teams, klüger zu denken und besser zu kommunizieren; Entscheidungsprotokolle sind nicht wertvoll, wenn sie nur eine nachträglich erzwungene Papierarbeit sind.

Manche Teams bevorzugen den Namen „Entscheidungen“ (decisions) deutlich gegenüber der Abkürzung „ADRs“. Wenn manche Teams den Verzeichnisnamen „decisions“ verwenden, geht ihnen gewissermaßen ein Licht auf, und das Team beginnt, mehr Informationen in das Verzeichnis zu legen, etwa Lieferantenentscheidungen, Planungsentscheidungen, Terminplanungsentscheidungen usw. All diese Arten von Informationen können dieselbe Vorlage nutzen. Wir vermuten, dass Menschen mit Wörtern („Entscheidungen“) schneller lernen als mit Abkürzungen („ADRs“), dass Menschen motivierter sind, Dokumente für laufende Arbeit zu schreiben, wenn das Wort „Protokoll“ (record) entfällt, und dass manche Entwickler und manche Manager das Wort „Architektur“ nicht mögen.

In der Theorie ist Unveränderlichkeit ideal. In der Praxis hat sich Veränderlichkeit für unsere Teams besser bewährt. Wir fügen die neue Information in den bestehenden ADR ein, mit einem Datumsstempel und einem Hinweis, dass die Information nach der Entscheidung eintraf. Ein solcher Ansatz führt zu einem „lebenden Dokument“, das wir alle aktualisieren können. Typische Aktualisierungen erfolgen, wenn wir Informationen dank neuer Teamkollegen oder neuer Angebote erhalten, oder durch reale Ergebnisse unserer Nutzung, oder nach nachträglichen Änderungen durch Dritte wie Fähigkeiten von Anbietern, Preismodelle, Lizenzvereinbarungen usw.

## Teamarbeit-Fragen für ADRs

### Wer kann einen ADR erstellen?

Berücksichtigen Sie Bereiche wie bestimmte Personen, bestimmte Rollen, bestimmte Teams oder bestimmte Abteilungen; erwägen Sie auch, ob es Personen, Rollen, Teams oder Abteilungen gibt, die einen ADR in Auftrag geben können, das heißt, einen anfordern, den jemand anderes verfasst. 

Beispielantwort: Jede Person in unserer Organisation, die die README-Seite zu Architecture Decision Records gelesen hat, kann einen ADR vorschlagen, das heißt, die Person kann anfangen, ihn zu schreiben, und ihn mit dem Team teilen.

### Was rechtfertigt es, einen ADR anzulegen?

Berücksichtigen Sie Bereiche wie die Arbeitsweisen Ihres Organisationsteams, die Struktur Ihres Softwaresystems, teamübergreifende Koordination, langfristige Wartbarkeit, externe Schnittstellen, wem Sie nutzen möchten, und Ähnliches. 

Beispielantwort: Wir möchten einen ADR erstellen, wenn künftige Entwickler das „Warum“ dessen verstehen sollen, was wir tun.

### Was rechtfertigt es, keinen ADR anzulegen?

Berücksichtigen Sie Bereiche wie Entscheidungen, die nicht die Architektur betreffen, oder winzig sind, etwa mit minimalem Risiko, in sich abgeschlossen oder für einen einzelnen Entwickler, oder bereits anderswo vollständig abgedeckt sind, etwa durch Standards, Richtlinien oder Dokumentation, oder vorübergehend sind, etwa Behelfslösungen, Machbarkeitsnachweise oder Experimente. 

Beispielantwort: Wir möchten einen ADR überspringen, wenn eine Entscheidung in Umfang, Zeit, Risiko und Kosten begrenzt ist oder bereits anderswo abgedeckt wird.

### Was ist der Lebenszyklus eines ADRs?

Berücksichtigen Sie Bereiche wie Erstellungsprozess, Recherche-Prozess, Entscheidungsprozess, Umsetzungsprozess und Außerbetriebnahmeprozess. Überlegen Sie, wie der ADR-Lebenszyklus im Zeitverlauf verfolgt wird, etwa wie der ADR von einem Zustand in den nächsten überführt wird, und auch wie dies den Stakeholdern mitgeteilt wird. 

Beispielantwort: Wir möchten, dass ein ADR fünf Lebenszyklusphasen hat: Initiieren (Initiating) → Recherchieren (Researching) → Bewerten (Evaluating) → Umsetzen (Implementing) → Pflegen (Maintaining) → Auslaufen lassen (Sunsetting).

### Was sind die Kriterien für die Lebenszyklusschritte eines ADRs?

Berücksichtigen Sie Bereiche wie Akzeptanzkriterien für einen ADR, das heißt, woran erkennen Sie, dass er gut genug ist, um vom einen Lebenszyklusschritt zum nächsten zu gelangen? Ist das Problem klar formuliert? Wurden die Alternativen erwogen? Sind die Kompromisse gut genug verstanden und dokumentiert?
Ist der gesamte relevante Kontext vorhanden? Sind alle relevanten Stakeholder eingebunden? Wurde alles Feedback eingearbeitet? 

Beispielantwort: Wir möchten, dass über einen ADR von den Stakeholdern abgestimmt wird, wenn das aktive Team 1) seine Recherche abgeschlossen hat, 2) seine Bewertung abgeschlossen hat, 3) den ADR-Vorschlag den Stakeholdern mit einer Bitte um Kommentare und einer Frist von einer Woche veröffentlicht hat, 4) alle Kommentare der Stakeholder eingearbeitet und behandelt wurden.

### Welche Rollen und Verantwortlichkeiten stehen im Zusammenhang mit einem ADR?

Berücksichtigen Sie Rollen wie Vorschlagender, Recherchierender, Bewertender, Prüfer, Genehmiger, Pfleger und Ähnliches. Berücksichtigen Sie Verantwortlichkeiten wie Kommunikation mit Stakeholdern, sicherstellen, dass Erwartungen erfüllt werden, Teilen auf der Website oder im Intranet und regelmäßige Überprüfung der Arbeit, insbesondere wenn relevante Änderungen eintreten.

Beispielantwort: Wir möchten, dass jeder ADR stets eine primäre Kontaktperson, eine sekundäre Kontaktperson und ein verantwortliches Team hat; diese sind verantwortlich für Kommunikation, Veröffentlichungen, Pflege, regelmäßige Überprüfung mindestens einmal pro Jahr und das schließliche Auslaufenlassen bei Bedarf.

### Wie steht die Governance im Zusammenhang mit einem ADR?

Berücksichtigen Sie Bereiche wie die Arbeitsweisen Ihrer Organisation, besondere Compliance-Anforderungen, etwa in rechtlicher oder personalbezogener Hinsicht, und wie Sie Konsens im Vergleich zu Konflikt im Vergleich zu Eskalation handhaben möchten. Gibt es Bereiche oder Personen oder Teams, die bei einem ADR mehr Einfluss haben können als andere, etwa indem sie ihn genehmigen, darüber abstimmen oder ein Veto einlegen können?

Beispielantwort: Die Governance eines ADRs folgt dieser Prioritätsreihenfolge: der CEO, der CTO, der CLO, das Team, das einen ADR umsetzt, die Experten im Team, die mit dem ADD am besten vertraut sind. Niemand sonst hat Governance, es sei denn, dies ist im ADR beschrieben. 

### Welche Prinzipien stehen im Zusammenhang mit einem ADR?

Berücksichtigen Sie Bereiche wie die Arbeitsweisen Ihrer Organisation, die schnelles Vorgehen im Vergleich zu langsamem Vorgehen, Entscheidungskonsens im Vergleich zu Entscheidungskonflikt, Risikopräferenzen im Vergleich zu Sicherheitspräferenzen, öffentliche Diskussion im Vergleich zu privater Diskussion und Ähnliches umfassen.

Beispielantwort: Wir verwenden die Führungsprinzipien Handlungsorientierung (bias for action), Widerspruch und Bekenntnis (disagree-and-commit), 70-%-Schätzungen sind gut genug für leicht umkehrbare und leicht isolierbare Entscheidungen, und öffentliche Arbeitsweisen mit Ausnahme vertraulicher Informationen, wie in der Vertraulichkeitsvereinbarung unserer Organisation beschrieben.

## Konzepte für den nächsten Schritt bei ADRs

[Arc42](https://arc42.org/) beantwortet zwei Fragen pragmatisch und lässt sich an Ihre konkreten Bedürfnisse anpassen. Was sollten Sie über Ihre Architektur dokumentieren/kommunizieren? Wie sollten Sie dokumentieren/kommunizieren? Arc42 umfasst Architecture Decision Records sowie Hinweise zu Zielen, Randbedingungen, Kontexten, Qualität, Risiken und mehr.

[Das C4-Modell](https://c4model.com/) ist ein leicht erlernbarer, entwicklerfreundlicher Ansatz zur Diagrammerstellung für Softwarearchitektur. C4 ist eine Reihe hierarchischer Diagramme für Kontext, Container, Komponenten und Code sowie unterstützender Diagramme für Systemlandschaft, Dynamik und Deployment.

## Architekturdiagramme, Sichten und Blickwinkel

Ein Architekturdiagramm heißt „Architektursicht“.

Eine „Architektursicht“ ist eine Instanz eines „Architekturblickwinkels“.

Ein „Architekturblickwinkel“ hat eine bestimmte Zielgruppe mit bestimmten Anliegen im Blick.

Beispiele für Architekturblickwinkel, Sichten und Diagramme:

- Geschäftsfähigkeiten

- Geschäftsprozesse auf hoher Ebene

- [Wertströme](https://en.wikipedia.org/wiki/Value_stream)

- Softwarefunktionen, zugeordnet zu Anwendungskomponenten

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Kontextdiagramm (TO-BE / AS-IS)

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Containerdiagramm (TO-BE / AS-IS)

- [Entity-Relationship-Diagramm](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) zur Zuordnung von Datenentitäten zu Anwendungskomponenten

- [Sequenzdiagramme](https://en.wikipedia.org/wiki/Sequence_diagram) zur Beschreibung funktionaler Abläufe in Systemen und bei Integrationen

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) Diagramme zur Beschreibung von Datenflüssen über Anwendungskomponenten hinweg

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) Diagramme zur Beschreibung von Geschäftsprozessen / Benutzerszenarien

- [Identity and Access Management](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) Diagramme

- [Rollenbasierte Zugriffskontrolle](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) Diagramme mit Rollen pro Anwendungskomponente

- [Attributbasierte Zugriffskontrolle](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) Diagramme mit Attributen pro Anwendungskomponente

- Datenschutzdiagramme

Verwandte Diagramme:

- Ein Anwendungsfalldiagramm zeigt dem Management/den Kunden die Anwendungsfälle, die den Anforderungen vorausgehen, die wiederum der Softwarearchitektur vorausgehen.

- Ein Verteilungsdiagramm zeigt die physische Hardware/die Rechner, auf denen die Softwarekomponenten bereitgestellt werden.
- Ein Datenflussdiagramm zeigt, wie Daten sich durch das System bewegen und umgewandelt werden.
- Ein Sequenzdiagramm zeigt, wie Protokolle wie HTTP auf einer Zeitachse funktionieren.

- Ein Aktivitätsdiagramm stellt den Arbeitsablauf der Aktivitäten dar, die ein Softwaresystem ausführt, etwa eine NPC-KI.

## Fitnessfunktionen für Entscheidungen als Code

Fitnessfunktionen sind objektive, automatisierte Prüfungen, die mit Programmcode geschrieben werden und verifizieren, dass Entscheidungen eingehalten werden.

- Fitnessfunktionen machen Entscheidungen testbar und absicherbar.

- Fitnessfunktionen für Entscheidungen können Qualitätssicherung, regulatorische Prozesse und Governance-Ziele erheblich unterstützen.

### Wie Fitnessfunktionen mit Entscheidungen zusammenhängen

Ein Entscheidungsprotokoll dokumentiert die Entscheidung, während eine Fitnessfunktion die Entscheidung absichert.

- Beispielentscheidung: Wir verwenden Event Sourcing für Auditanforderungen.

- Beispiel-Fitnessfunktion: Wir nutzen den Continuous-Integration-Server, um zu testen, dass alle Zustandsänderungen Ereignisse erzeugen müssen.

### Warum Fitnessfunktionen Entscheidungen helfen

Objektive Messungen: Fitnessfunktionen bestehen oder fallen durch, daher ist die Arbeit sichtbar und klar.

Kontinuierliche Nutzung: Fitnessfunktionen sind Ihre lebendigen Regeln und laufen bei jedem Commit und jedem Build.

Vertrauen beim Refactoring: Fitnessfunktionen fangen Fehler bei Entscheidungsregeln automatisch ab.

Skalierbare Governance: Fitnessfunktionen sichern Standards ab, ohne Engpässe zu schaffen.

### Können Fitnessfunktionen KI nutzen?

Fitnessfunktionen können KI-LLMs für Entscheidungen nutzen, indem sie Fragen zu Ihrer Arbeit stellen,
etwa zu Ihren Plänen, Code, Schemata, APIs und mehr:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Architektur-Unit-Tests

[ArchUnit](https://www.archunit.org/): Architekturregeln von Java-Code mit einem beliebigen einfachen Java-Unit-Test-Framework prüfen.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): Architekturregeln von TypeScript-Code und JavaScript-Code mit Jest, Vitest, Jasmine usw. prüfen.

## Entscheidungs-Leitplanken für Pull Requests

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
bringt automatisch die richtigen Entscheidungsprotokolle im richtigen Moment zum Vorschein, nämlich dann, wenn ein
Entwickler gerade den Code ändert, den diese Entscheidungen betreffen. Statt darauf zu hoffen, dass Entwickler
vor dem Mergen einen Dokumentenordner lesen, erscheint der relevante Kontext direkt im Pull Request.

Das funktioniert für jede Art von Entscheidungsprotokoll: Architekturentscheidungen, Datenentscheidungen, Compliance-Entscheidungen, klinische und medizinische Entscheidungen, Sicherheitsentscheidungen und mehr.

Funktioniert mit jedem CI-System (GitLab, Jenkins, CircleCI) und als Pre-Commit-Hook.
Open Source. MIT-Lizenz.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) ist eine GitHub
Action, die einen Pull Request scheitern lässt, wenn überwachte Codepfade geändert werden, ohne dass ein
Architecture Decision Record hinzugefügt oder aktualisiert wird. Ausnahmen sind ausdrücklich: Eine
`ADR-Exempt:`-Zeile mit Begründung lässt das Gate passieren und wird in die Job-Zusammenfassung geschrieben. Vorlagenunabhängig, ohne Abhängigkeiten. Open Source. MIT-Lizenz.

## Weitere Informationen

Einführung:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Vorlagen:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Vertiefung:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - kostenlose monatliche Lektion zur Softwarearchitektur

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Werkzeuge:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Unternehmensspezifische Hinweise:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Beispiele:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Videos:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcasts:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Bücher:

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

Siehe auch:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Ein herstellerneutrales, maschinenlesbares YAML/JSON-Format zur Darstellung von Entscheidungen mit ausdrücklicher Begründung, Annahmen, kognitivem Zustand und Abwägungen. Ergänzt ADRs, indem es der Entscheidungsdokumentation strukturierte, prüfbare Begründungen hinzufügt.
