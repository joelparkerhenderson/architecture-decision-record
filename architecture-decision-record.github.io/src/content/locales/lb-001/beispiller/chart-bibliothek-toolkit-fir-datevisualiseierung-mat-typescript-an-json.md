# Architektur-Decisiounsopzeechnung: Chart-Bibliothéik-Toolkit fir Datevisualiséierung mat TypeScript a JSON

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

**Haaptziel:**  
E fortgeschratt Chart-Toolkit fir d'Erstelle vun interaktive Visualiséierunge ze wielen, mat Fokus op Finanzdaten, wëssenschaftlech Daten a Regierungsdaten mat TypeScript a JSON. D'Bibliothéik soll robust Funktiounen, Flexibilitéit bidden an Open Source sinn. 

### Kontext an Ufuerderungen:

1. **Agil Entwécklung (Héich Prioritéit)**: Als Startup sinn séier Iteratioun, Prototyping a Flexibilitéit an der Entwécklung essenziell. D'Chart-Bibliothéik muss séier Entwécklungszyklen erméiglechen.
   
2. **Charttypen (Héich Prioritéit)**:
   - **Doughnut-Chart**
   - **Radar-Chart**
   - **Clustering-Process-Chart**
   - **Area-Chart mat Zäitachs**
   - **Candlestick-Chart**
   - **Nightingale-Chart**
   - **Geo-SVG-Kaart**
   
   Dës Charttypen si speziell wichteg, fir komplex Datesätz ze visualiséieren, wéi Finanztrends, wëssenschaftlech Metriken a geographesch Informatioun.

3. **Gratis an Open Source (Héich Prioritéit)**: D'Toolkit soll Open Source sinn, fir Lizenzkäschten ze vermeiden, Transparenz ze bidden a Flexibilitéit fir d'Upassung ze bidden.

4. **Critèrë mat niddreger Wichtegkeet**:
   - **Laufzäit-Vitess**: Och wann d'Performance wichteg ass, ass si keng Topprioritéit fir dës Decisioun.
   - **Skaléierbarkeet**: Och wann Skaléierbarkeet allgemeng wichteg ass, ass de direkte Besoin, e MVP ze bauen, dee mat der Zäit ka wuessen. Suergen iwwer d'Skaléierbarkeet kënne méi spéit adresséiert ginn.
   - **Réckwärtskompatibilitéit**: Keng Haaptsuerg fir de Prototyp, soulaang d'Bibliothéik modern ass an aktiv ënnerhale gëtt.

### Evaluéiert Bibliothéiken:

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

**Iwwerbléck**:  
Apache ECharts ass eng mächteg, flexibel Chart-Bibliothéik fir interaktiv, upassbar Visualiséierungen. Si ënnerstëtzt eng grouss Varietéit u Charts a ass besonnesch staark bei komplexen, dynamesche Visualiséierungen.

**Stäerkten**:
- **Fortgeschratt Interaktivitéit**: ECharts exzelléiert dran, interaktiv Charts ze bidden, mat Funktiounen wéi Zoomen, Panning an dynamesch Daten-Aktualiséierungen.
- **Doughnut, Radar, Candlestick, Geo-SVG-Kaarten**: ECharts ënnerstëtzt vill vun den néidege Charttypen, dorënner Doughnut-, Radar-, Candlestick- a geographesch Kaartevisualiséierungen.
- **Gratis an Open Source**: ECharts ass eng Open-Source-Bibliothéik, déi zum budgetbewosste Charakter vun engem Startup passt a d'Fräiheet gëtt, de Code z'änneren.
- **Flexibilitéit an Erweiderbarkeet**: Héich upassbar, mat ëmfangräicher Ënnerstëtzung fir Animatiounen, eege Visualiséierungen a fortgeschratt Charting-Techniken.
  
**Schwächten**:
- **Léierkurve**: ECharts kann, och wa se mächteg ass, wéinst hirer Flexibilitéit an ëmfangräicher API eng méi steil Léierkurve hunn.
- **Komplexitéit vun der Dokumentatioun**: D'Dokumentatioun ass ëmfaassend, kann awer fir Entwéckler, déi grad ufänken, iwwerwältegend sinn.

**Verdikt**:  
ECharts ass héich gëeegent fir de Projet wéinst hirer Ënnerstëtzung fir interaktiv Charts, dorënner all néideg Typen wéi Candlestick-Charts, Radar-Charts a Geo-Kaarten. Hir Open-Source-Natur passt zum Besoin vum Projet un Flexibilitéit a Käschteneffizienz.

---

### 2. **Chart.js**

**Iwwerbléck**:  
Chart.js ass eng einfach, einfach ze benotzen Chart-Bibliothéik fir gängeg Charttypen. Si ass bekannt fir hir Einfachheet a liicht Integratioun.

**Stäerkten**:
- **Einfach ze benotzen**: Chart.js ass ganz einfach opzesetzen a ze benotzen, mat enger minimaler Léierkurve.
- **Open Source**: Chart.js ass gratis an Open Source, wat entscheedend ass, fir Käschten ze reduzéieren.
- **Gängeg Charttypen**: Si ënnerstëtzt Basis-Charts wéi Doughnut-, Area-, Radar- a Linnecharts, déi déi meescht Haaptbedierfnisser ofdecken.

**Schwächten**:
- **Limitéiert fortgeschratt Charts**: Chart.js ënnerstëtzt komplex Charttypen wéi Candlestick-Charts, Geo-SVG-Kaarten oder Clustering-Process-Charts net nativ. Och wann dës Funktiounen duerch Plugins oder Upassung derbäi kënne bäigefüügt ginn, ass et net sou direkt wéi bei anere Bibliothéiken.
- **Interaktivitéit**: Och wann Chart.js Basis-Interaktivitéit ënnerstëtzt (z.B. Tooltips an Hover-Effekter), bitt se net sou fortgeschratt Funktiounen wéi ECharts oder D3.js.

**Verdikt**:  
Chart.js ass super fir einfach, séier Projeten, awer hire Mangel u Ënnerstëtzung fir komplex Charttypen mécht se ongëeegent fir eng dateniwwerfëllt Applikatioun mat fortgeschrattene Bedierfnisser wéi Candlestick-Charts a Geo-Kaarten. Si ass eng gutt Wiel fir Prototyping, awer fir déi néideg Charttypen ginn méi fortgeschratt Tools empfohlen.

---

### 3. **ApexCharts**

**Iwwerbléck**:  
ApexCharts ass eng modern Chart-Bibliothéik, déi eng Varietéit u Charttypen bitt a sech op interaktiv Visualiséierunge mat enger einfach ze benotzender API konzentréiert.

**Stäerkten**:
- **Interaktiv Funktiounen**: ApexCharts bitt interaktiv Charts mat Tooltips, Zoomen, Panning an Aktualiséierungen.
- **Ënnerstëtzung fir Finanz- a wëssenschaftlech Charts**: Si ënnerstëtzt eng grouss Varietéit u Charttypen, dorënner Candlestick-Charts, Radar-Charts an Area-Charts.
- **Einfach ze benotzen**: Si huet eng direkt API a léisst sech einfach an e Projet integréieren.
- **Gratis an Open Source**: ApexCharts bitt eng gratis Open-Source-Versioun, déi fir vill Notzungsfäll gëeegent ass.
  
**Schwächten**:
- **Komplex Upassung**: Och wann se vill Funktiounen bitt, sinn d'Upassungsoptiounen net esou flexibel wéi bei ECharts oder D3.js fir ganz komplex oder eege Charting-Bedierfnisser.
- **Geo-Kaarten**: ApexCharts ënnerstëtzt Geo-Kaarten oder Clustering-Process-Charts net nativ, déi fir dëse Projet néideg sinn.

**Verdikt**:  
ApexCharts ass e staarke Kandidat wéinst senger Einfachheet an Interaktivitéit, fält awer bei bestëmmten fortgeschratten Charttypen duerch, besonnesch beim Besoin u Geo-Kaarten a Clustering-Charts. Si ass eng gutt Optioun fir méi einfach Charts, awer et feelen e puer néideg Funktiounen.

---

### 4. **AG Charts**

**Iwwerbléck**:  
AG Charts ass eng kommerziell Chart-Bibliothéik, déi fir Performance a Präzisioun entworf gouf. Si ass héich gëeegent fir d'Erstelle vu Finanz-, wëssenschaftlechen a Business-Dashboards.

**Stäerkten**:
- **Fortgeschratt Charttypen**: AG Charts ënnerstëtzt vill fortgeschratt Charttypen, dorënner Candlestick-Charts, Area-Charts, Radar-Charts a méi. Si bitt och déif Integratioun mat anere AG-Grid-Produkter.
- **Héich Performance**: Si bitt exzellent Performance, besonnesch beim Ëmgang mat grousse Datesätz.
- **Interaktivitéit**: AG Charts ënnerstëtzt eng Varietéit u interaktive Funktiounen wéi Zoomen, Tooltips an dynamesch Aktualiséierungen.

**Schwächten**:
- **Net voll gratis**: Och wann AG Charts eng gratis Versioun bitt, ass déi voll ausgestatt Versioun bezuelt, wat fir Startups, déi Käschten minimiere wëllen, eng Barrière ka sinn.
- **Komplexitéit**: Och wann d'Bibliothéik funktiounsräich ass, kann se fir méi einfach Projeten iwwerdimensionéiert sinn a méi Setup a Konfiguratioun erfuerderen am Verglach mat anere Optiounen.

**Verdikt**:  
AG Charts ass mächteg a funktiounsräich, ass awer wéinst hirem kommerzielle Charakter a Käschtestruktur vläicht net déi bescht Passung. Hir Gëeegentheet hänkt dovun of, ob d'Budget bezuelt Versioune verkraaft oder ob Open-Source-Alternative bevirzugt ginn.

---

### 5. **Highcharts**

**Iwwerbléck**:  
Highcharts ass eng populär Chart-Bibliothéik, bekannt fir hir grouss Palette u Charttypen a mächteg Upassungsoptiounen.

**Stäerkten**:
- **Ëmfaassend Charttypen**: Highcharts ënnerstëtzt eng grouss Varietéit u Charts, dorënner Candlestick, Radar, Area a Geo-Kaarten.
- **Interaktiv an dynamesch**: Highcharts bitt räich interaktiv Funktiounen, dorënner Drill-downs, Zoomen a Panning.
- **Einfach ze benotzen**: Si huet eng benotzerfrëndlech API a gutt Dokumentatioun, wat den Ufank einfach mécht.

**Schwächten**:
- **Kommerziell Lizenz**: Och wann Highcharts eng gratis Versioun fir net-kommerziell Notzung bitt, ass déi kommerziell Lizenz deier, wat fir Startups en erhieflechen Nodeel ka sinn.
- **Léierkurve**: Och wann se net sou steil ass wéi bei ECharts, ka seng Léierkurve fir Ufänger nach ëmmer erausfuerderend sinn.

**Verdikt**:  
Highcharts ass eng funktiounsräich Bibliothéik, awer hir kommerziell Lizenzéierung mécht se manner gëeegent fir Open-Source-, käschtesensibel Projeten. Hir ëmfaassend Charting-Optioune sinn e Plus, awer d'Lizenzproblem limitéiert hir Attraktivitéit fir dëse Notzungsfall.

---

### 6. **Carbon Charts**

**Iwwerbléck**:  
Carbon Charts ass eng Chart-Bibliothéik, déi vun IBM entwéckelt gouf, fir visuell ugenehm an héich upassbar Charts ze erstellen.

**Stäerkten**:
- **Upassbarkeet**: Carbon Charts erlaabt ëmfangräich Upassung vun der Chartdarstellung a vum Verhalen.
- **Open Source**: Si ass gratis an Open Source, wat zum Projetsbesoin u budgetfrëndlech Léisunge passt.
- **Ënnerstëtzung fir gängeg Charts**: Si ënnerstëtzt gängeg Charttypen wéi Doughnut-, Radar- an Area-Charts, awer et feelt d'Ënnerstëtzung fir méi fortgeschratt Typen wéi Geo-Kaarten oder Candlestick-Charts.

**Schwächten**:
- **Limitéiert fortgeschratt Charttypen**: Si ënnerstëtzt keng Geo-Kaarten, Clustering-Process-Charts oder Candlestick-Charts, déi fir de Projet essenziell sinn.
- **Méi kleng Ökosystem**: Carbon Charts huet eng méi kleng Communautéit an en méi klenge Ökosystem am Verglach zu gréissere Chart-Bibliothéiken wéi ECharts oder Highcharts.

**Verdikt**:  
Carbon Charts ass Open Source an upassbar, mä et feelt d'Ënnerstëtzung fir déi méi komplex Charttypen, déi fir dëse Projet néideg sinn. Si ass méi gëeegent fir méi einfach Charting-Bedierfnisser.

---

### 7. **Layer Cake**

**Iwwerbléck**:  
Layer Cake ass eng Datevisualiséierungs-Bibliothéik, entworf fir flexibel, geschichtet Visualiséierungen ze erstellen.

**Stäerkten**:
- **Upassbar Schichten**: Si bitt mächteg Schichtoptiounen fir komplex Visualiséierungen.
- **Open Source**: Si ass gratis an Open Source, wat se zu enger vernünftegen Optioun fir budgetbewosst Projete mécht.

**Schwächten**:
- **Limitéiert Dokumentatioun**: Layer Cake feelt et un ëmfangräicher Dokumentatioun a Ënnerstëtzung vun der Communautéit, wouduerch et méi schwéier ass, domat ze schaffen am Verglach zu méi etabléierte Bibliothéiken.
- **Net fir Charts gebaut**: Layer Cake ass méi gëeegent fir Visualiséierungen, déi keng Charts sinn, dofir sinn hir fäerdeg Charting-Optioune limitéiert.

**Verdikt**:  
Och wann se interessant fir eenzegaarteg Visualiséierungen ass, ass Layer Cake net ideal fir traditionell Charting-Ufuerderungen wéi Candlestick-Charts oder Radar-Charts. Si ass méi gëeegent fir eege Visualiséierungen ausserhalb vum Ëmfang vu Standard-Charts.

---

### 8. **D3.js**

**Iwwerbléck**:  
D3.js ass eng mächteg JavaScript-Bibliothéik fir d'Erstelle vun datengedriwwene Visualiséierunge mat HTML, SVG a CSS.

**Stäerkten**:
- **Onerreecht Flexibilitéit**: D3.js erlaabt et, praktesch all Zort vun eeger Visualiséierung ze erstellen, wouduerch se héich mächteg fir fortgeschratt an interaktiv Charts ass.
- **Ëmfangräich Funktiounen**: Si ënnerstëtzt all néideg Charttypen, dorënner Geo-Kaarten, Clustering-Charts a méi.
- **Upassbar**: Den Niveau vun der Upassung an D3.js ass onerreecht a erlaabt Entwéckler, héich ugepasst Visualiséierungen ze bauen.

**Schwächten**:
- **Steil Léierkurve**: D3.js huet eng steil Léierkurve a ass méi komplex ze integréieren am Verglach zu anere Bibliothéiken.
- **Zäitopwänneg**: Charts an D3.js ze bauen kann zäitopwänneg sinn, besonnesch fir gängeg Charts wéi Candlestick- oder Doughnut-Charts.

**Verdikt**:  
D3.js ass ongemeng mächteg fir fortgeschratt, ugepasst Charts, ass awer wéinst senger steiler Léierkurve an Entwécklungszäit fir vill typesch Notzungsfäll iwwerdimensionéiert. Si ass am beschten a Situatiounen, wou déi aner Chart-Bibliothéike net den néidegen Niveau vun Upassung bidden.

---

### Conclusioun

Nodeems mir d'Bibliothéike baséierend op de Bedierfnisser vum Projet evaluéiert hunn, steet **Apache ECharts** als beschten Optioun eraus. Si ënnerstëtzt dat ganzt Spektrum u néidege Charts, dorënner Geo-Kaarten, Candlestick-Charts a Clustering-Charts. Si ass Open Source, funktiounsräich an héich interaktiv, wat perfekt zu de Projetsziler passt. Och wann **D3.js** déi gréisste Flexibilitéit bitt, maachen hir Komplexitéit an hiren Zäitopwand se manner ideal fir e Startup, dee séier wëll iteréieren. **ApexCharts** a **Chart.js** si gutt Alternativen fir méi einfach Projeten, awer et feelt hinnen d'Ënnerstëtzung fir fortgeschratt Charttypen.
