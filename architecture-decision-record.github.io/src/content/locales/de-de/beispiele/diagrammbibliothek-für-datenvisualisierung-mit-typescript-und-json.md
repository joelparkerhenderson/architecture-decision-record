# Architecture Decision Record: Diagrammbibliothek für Datenvisualisierung mit TypeScript und JSON

<!--

ChatGPT prompt:

Long software architecture decision record 
chart library toolkit for data visualization using TypeScript and JSON

Evaluate Charts: Apache ECharts, Chart.js, ApexCharts, AG Charts, Highcharts, Carbon Charts, Layer Cake, D3.

Primary need: advanced interactive charts, especially for financial data, scientific data, and government data.

High importance: 1. Agile development because this is for a startup. 2. Doughnut Chart, Radar Chart, Clustering Process
Chart, Area Chart with Time Axis, Candlestick Chart, Nightingale Chart, Geo SVG Map. 3. Free open source.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Hauptziel:**  
Auswahl eines fortgeschrittenen Diagramm-Toolkits zur Erstellung interaktiver Visualisierungen, mit Schwerpunkt auf Finanzdaten, wissenschaftlichen Daten und Behördendaten unter Verwendung von TypeScript und JSON. Die Bibliothek sollte robuste Funktionen und Flexibilität bieten und Open Source sein. 

### Kontext und Anforderungen:

1. **Agile Entwicklung (Hohe Priorität)**: Als Startup sind schnelle Iteration, Prototyping und Flexibilität bei der Entwicklung unerlässlich. Die Diagrammbibliothek muss schnelle Entwicklungszyklen erlauben.
   
2. **Diagrammtypen (Hohe Priorität)**:
   - **Ringdiagramm (Doughnut Chart)**
   - **Radardiagramm (Radar Chart)**
   - **Clustering-Prozess-Diagramm (Clustering Process Chart)**
   - **Flächendiagramm mit Zeitachse (Area Chart with Time Axis)**
   - **Kerzendiagramm (Candlestick Chart)**
   - **Nightingale-Diagramm (Nightingale Chart)**
   - **Geo-SVG-Karte (Geo SVG Map)**
   
   Diese Diagrammtypen sind besonders wichtig, um komplexe Datensätze zu visualisieren, etwa Finanztrends, wissenschaftliche Kennzahlen und geografische Informationen.

3. **Kostenlos und Open Source (Hohe Priorität)**: Das Toolkit sollte Open Source sein, um Lizenzkosten zu vermeiden, Transparenz zu bieten und Flexibilität bei der Anpassung zu ermöglichen.

4. **Kriterien niedriger Priorität**:
   - **Laufzeitgeschwindigkeit**: Obwohl Leistung wichtig ist, hat sie für diese Entscheidung keine oberste Priorität.
   - **Skalierbarkeit**: Obwohl Skalierbarkeit im Allgemeinen wichtig ist, besteht der unmittelbare Bedarf darin, ein MVP zu bauen, das mit der Zeit wachsen kann. Skalierbarkeitsbedenken können später angegangen werden.
   - **Abwärtskompatibilität**: Kein Hauptanliegen für den ersten Aufbau, solange die Bibliothek modern ist und aktiv gepflegt wird.

### Bewertete Bibliotheken:

1. **Apache ECharts**
2. **Chart.js**
3. **ApexCharts**
4. **AG Charts**
5. **Highcharts**
6. **Carbon Charts**
7. **Layer Cake**
8. **D3.js**

---

### 1. **Apache ECharts**

**Überblick**:  
Apache ECharts ist eine leistungsfähige, flexible Diagrammbibliothek für interaktive, anpassbare Visualisierungen. Sie unterstützt eine große Vielfalt an Diagrammen und ist besonders stark bei komplexen, dynamischen Visualisierungen.

**Stärken**:
- **Fortgeschrittene Interaktivität**: ECharts glänzt bei der Bereitstellung interaktiver Diagramme mit Funktionen wie Zoomen, Schwenken und dynamischen Datenaktualisierungen.
- **Ring-, Radar-, Kerzendiagramme, Geo-SVG-Karten**: ECharts unterstützt viele der erforderlichen Diagrammtypen, darunter Ring-, Radar-, Kerzendiagramme und Visualisierungen geografischer Karten.
- **Kostenlos und Open Source**: ECharts ist eine Open-Source-Bibliothek, was zur budgetbewussten Art eines Startups passt und die Freiheit bietet, den Code zu ändern.
- **Flexibilität und Erweiterbarkeit**: Sehr gut anpassbar, mit umfangreicher Unterstützung für Animationen, benutzerdefinierte Visualisierungen und fortgeschrittene Diagrammtechniken.
  
**Schwächen**:
- **Lernkurve**: ECharts kann, obwohl leistungsfähig, wegen seiner Flexibilität und umfangreichen API eine steilere Lernkurve haben.
- **Komplexität der Dokumentation**: Die Dokumentation ist umfassend, kann für Entwickler, die gerade erst anfangen, aber überwältigend sein.

**Urteil**:  
ECharts eignet sich sehr gut für das Projekt wegen seiner Unterstützung für interaktive Diagramme, einschließlich aller erforderlichen Typen wie Kerzendiagramme, Radardiagramme und Geo-Karten. Seine Open-Source-Natur entspricht dem Bedarf des Projekts an Flexibilität und Kosteneffizienz.

---

### 2. **Chart.js**

**Überblick**:  
Chart.js ist eine einfache, leicht zu verwendende Diagrammbibliothek zum Erstellen gängiger Diagrammtypen. Sie ist für ihre Einfachheit und leichte Integration bekannt.

**Stärken**:
- **Benutzerfreundlichkeit**: Chart.js ist sehr einfach einzurichten und zu verwenden, mit minimaler Lernkurve.
- **Open Source**: Chart.js ist kostenlos und Open Source, was entscheidend ist, um Kosten zu senken.
- **Gängige Diagrammtypen**: Es unterstützt grundlegende Diagramme wie Ring-, Flächen-, Radar- und Liniendiagramme, die die meisten primären Bedürfnisse abdecken.

**Schwächen**:
- **Eingeschränkte erweiterte Diagramme**: Chart.js unterstützt komplexe Diagrammtypen wie Kerzendiagramme, Geo-SVG-Karten oder Clustering-Prozess-Diagramme nicht nativ. Obwohl sich diese Funktionen über Plugins oder Anpassung hinzufügen lassen, ist es nicht so unkompliziert wie bei anderen Bibliotheken.
- **Interaktivität**: Obwohl Chart.js grundlegende Interaktivität (z. B. Tooltips und Hover-Effekte) unterstützt, bietet es nicht so fortgeschrittene Funktionen wie ECharts oder D3.js.

**Urteil**:  
Chart.js ist großartig für einfache, schnelle Projekte, aber das Fehlen von Unterstützung für komplexe Diagrammtypen macht es für eine datenlastige Anwendung mit fortgeschrittenen Bedürfnissen wie Kerzendiagrammen und Geo-Karten ungeeignet. Es ist eine gute Wahl fürs Prototyping, aber für die erforderlichen Diagrammtypen werden fortgeschrittenere Werkzeuge empfohlen.

---

### 3. **ApexCharts**

**Überblick**:  
ApexCharts ist eine moderne Diagrammbibliothek, die eine Vielzahl von Diagrammtypen bietet und sich mit einer leicht zu verwendenden API auf interaktive Visualisierungen konzentriert.

**Stärken**:
- **Interaktive Funktionen**: ApexCharts bietet interaktive Diagramme mit Tooltips, Zoomen, Schwenken und Aktualisierungen.
- **Unterstützung für Finanz- und wissenschaftliche Diagramme**: Es unterstützt eine große Vielfalt an Diagrammtypen, darunter Kerzendiagramme, Radardiagramme und Flächendiagramme.
- **Benutzerfreundlichkeit**: Es hat eine unkomplizierte API und ist einfach in ein Projekt zu integrieren.
- **Kostenlos und Open Source**: ApexCharts bietet eine kostenlose Open-Source-Version, die für viele Anwendungsfälle geeignet ist.
  
**Schwächen**:
- **Komplexe Anpassung**: Obwohl es viele Funktionen bietet, sind die Anpassungsoptionen für sehr komplexe oder individuelle Diagrammbedürfnisse nicht so flexibel wie bei ECharts oder D3.js.
- **Geo-Karten**: ApexCharts unterstützt Geo-Karten oder Clustering-Prozess-Diagramme, die für dieses Projekt erforderlich sind, nicht nativ.

**Urteil**:  
ApexCharts ist wegen seiner Benutzerfreundlichkeit und Interaktivität ein starker Kandidat, bleibt aber bei bestimmten erweiterten Diagrammtypen zurück, besonders beim Bedarf an Geo-Karten und Clustering-Diagrammen. Es ist eine gute Option für einfachere Diagramme, es fehlen aber einige erforderliche Funktionen.

---

### 4. **AG Charts**

**Überblick**:  
AG Charts ist eine Diagrammbibliothek in kommerzieller Qualität, entworfen für Leistung und Präzision. Sie eignet sich sehr gut zur Erstellung von Finanz-, wissenschaftlichen und Business-Dashboards.

**Stärken**:
- **Erweiterte Diagrammtypen**: AG Charts unterstützt viele erweiterte Diagrammtypen, darunter Kerzendiagramme, Flächendiagramme, Radardiagramme und mehr. Es bietet außerdem tiefe Integration mit anderen AG-Grid-Produkten.
- **Hohe Leistung**: Es bietet ausgezeichnete Leistung, besonders bei großen Datensätzen.
- **Interaktivität**: AG Charts unterstützt eine Vielzahl interaktiver Funktionen wie Zoomen, Tooltips und dynamische Aktualisierungen.

**Schwächen**:
- **Nicht vollständig kostenlos**: Obwohl AG Charts eine kostenlose Version anbietet, ist die voll ausgestattete Version kostenpflichtig, was für Startups, die Kosten minimieren möchten, eine Hürde sein könnte.
- **Komplexität**: Obwohl die Bibliothek funktionsreich ist, kann sie für einfachere Projekte überdimensioniert sein und im Vergleich zu anderen Optionen mehr Einrichtung und Konfiguration erfordern.

**Urteil**:  
AG Charts ist leistungsfähig und funktionsreich, aber wegen seiner kommerziellen Natur und Kostenstruktur möglicherweise nicht die beste Passung. Seine Eignung hängt davon ab, ob das Budget kostenpflichtige Versionen verkraftet oder Open-Source-Alternativen bevorzugt werden.

---

### 5. **Highcharts**

**Überblick**:  
Highcharts ist eine beliebte Diagrammbibliothek, die für ihre breite Palette an Diagrammtypen und leistungsfähigen Anpassungsoptionen bekannt ist.

**Stärken**:
- **Umfassende Diagrammtypen**: Highcharts unterstützt eine große Vielfalt an Diagrammen, darunter Kerzen-, Radar-, Flächendiagramme und Geo-Karten.
- **Interaktiv und dynamisch**: Highcharts bietet reichhaltige interaktive Funktionen, darunter Drilldowns, Zoomen und Schwenken.
- **Benutzerfreundlichkeit**: Es hat eine benutzerfreundliche API und gute Dokumentation, was den Einstieg erleichtert.

**Schwächen**:
- **Kommerzielle Lizenz**: Obwohl Highcharts eine kostenlose Version für nichtkommerzielle Nutzung anbietet, ist die kommerzielle Lizenz teuer, was für Startups ein erheblicher Nachteil sein könnte.
- **Lernkurve**: Obwohl nicht so steil wie bei ECharts, kann die Lernkurve von Highcharts für Anfänger dennoch herausfordernd sein.

**Urteil**:  
Highcharts ist eine funktionsreiche Bibliothek, aber seine kommerzielle Lizenzierung macht es für Open-Source-, kostenbewusste Projekte weniger geeignet. Seine umfassenden Diagrammoptionen sind ein Plus, aber das Lizenzproblem begrenzt seine Attraktivität für diesen Anwendungsfall.

---

### 6. **Carbon Charts**

**Überblick**:  
Carbon Charts ist eine von IBM entwickelte Diagrammbibliothek, entworfen zur Erstellung optisch ansprechender und sehr anpassbarer Diagramme.

**Stärken**:
- **Anpassbarkeit**: Carbon Charts erlaubt umfangreiche Anpassung von Aussehen und Verhalten der Diagramme.
- **Open Source**: Es ist kostenlos und Open Source, was zur Projektanforderung budgetfreundlicher Lösungen passt.
- **Unterstützung gängiger Diagramme**: Es unterstützt gängige Diagrammtypen wie Ring-, Radar- und Flächendiagramme, hat jedoch keine Unterstützung für fortgeschrittenere Typen wie Geo-Karten oder Kerzendiagramme.

**Schwächen**:
- **Eingeschränkte erweiterte Diagrammtypen**: Es unterstützt weder Geo-Karten, Clustering-Prozess-Diagramme noch Kerzendiagramme, die für das Projekt unerlässlich sind.
- **Kleineres Ökosystem**: Carbon Charts hat im Vergleich zu größeren Diagrammbibliotheken wie ECharts oder Highcharts eine kleinere Community und ein kleineres Ökosystem.

**Urteil**:  
Carbon Charts ist Open Source und anpassbar, es fehlt jedoch die Unterstützung für die komplexeren Diagrammtypen, die für dieses Projekt benötigt werden. Es eignet sich besser für einfachere Diagrammbedürfnisse.

---

### 7. **Layer Cake**

**Überblick**:  
Layer Cake ist eine Datenvisualisierungsbibliothek, die für die Erstellung flexibler, geschichteter Visualisierungen entworfen wurde.

**Stärken**:
- **Anpassbare Ebenen**: Es bietet leistungsfähige Schichtungsoptionen für komplexe Visualisierungen.
- **Open Source**: Es ist kostenlos und Open Source, was es zu einer tragfähigen Option für budgetbewusste Projekte macht.

**Schwächen**:
- **Begrenzte Dokumentation**: Layer Cake fehlt umfangreiche Dokumentation und Community-Unterstützung, was die Arbeit damit im Vergleich zu etablierteren Bibliotheken erschwert.
- **Nicht für Diagramme gebaut**: Layer Cake eignet sich besser für Nicht-Diagramm-Visualisierungen, daher sind seine sofort einsatzbereiten Diagrammoptionen begrenzt.

**Urteil**:  
Obwohl interessant für einzigartige Visualisierungen, ist Layer Cake für traditionelle Diagrammanforderungen wie Kerzendiagramme oder Radardiagramme nicht ideal. Es eignet sich eher für benutzerdefinierte Visualisierungen außerhalb des Rahmens von Standarddiagrammen.

---

### 8. **D3.js**

**Überblick**:  
D3.js ist eine leistungsfähige JavaScript-Bibliothek zur Erstellung datengetriebener Visualisierungen mit HTML, SVG und CSS.

**Stärken**:
- **Unübertroffene Flexibilität**: D3.js erlaubt die Erstellung praktisch jeder Art von benutzerdefinierter Visualisierung, was es für fortgeschrittene und interaktive Diagramme sehr leistungsfähig macht.
- **Umfangreiche Funktionen**: Es unterstützt alle erforderlichen Diagrammtypen, einschließlich Geo-Karten, Clustering-Diagrammen und mehr.
- **Anpassbar**: Der Grad der Anpassbarkeit in D3.js ist unübertroffen und erlaubt Entwicklern, hochgradig maßgeschneiderte Visualisierungen zu bauen.

**Schwächen**:
- **Steile Lernkurve**: D3.js hat eine steile Lernkurve und ist im Vergleich zu anderen Bibliotheken komplexer zu integrieren.
- **Zeitaufwendig**: Das Erstellen von Diagrammen in D3.js kann zeitaufwendig sein, besonders bei gängigen Diagrammen wie Kerzen- oder Ringdiagrammen.

**Urteil**:  
D3.js ist unglaublich leistungsfähig für fortgeschrittene, individuell gestaltete Diagramme, aber für viele typische Anwendungsfälle wegen seiner steilen Lernkurve und des Entwicklungsaufwands überdimensioniert. Es ist am besten für Situationen, in denen die anderen Diagrammbibliotheken nicht den erforderlichen Grad an Anpassung bieten.

---

### Fazit

Nach der Bewertung der Bibliotheken anhand der Projektbedürfnisse hebt sich **Apache ECharts** als beste Option ab. Es unterstützt die volle Bandbreite der erforderlichen Diagramme, einschließlich Geo-Karten, Kerzendiagrammen und Clustering-Diagrammen. Es ist Open Source, funktionsreich und hochgradig interaktiv, was perfekt zu den Zielen des Projekts passt. Obwohl **D3.js** die größte Flexibilität bietet, machen seine Komplexität und der Zeitaufwand es für ein Startup, das schnell iterieren möchte, weniger ideal. **ApexCharts** und **Chart.js** sind gute Alternativen für einfachere Projekte, es fehlt ihnen aber die Unterstützung für erweiterte Diagrammtypen.
