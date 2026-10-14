# Arkitekturbeslutspost: diagrambibliotek för datavisualisering med TypeScript och JSON

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

**Primärt mål:**  
Att välja ett avancerat diagramverktyg för att skapa interaktiva visualiseringar, med fokus på finansiell data, vetenskaplig data och myndighetsdata med TypeScript och JSON. Biblioteket bör erbjuda robusta funktioner och flexibilitet och vara öppen källkod. 

### Sammanhang och krav:

1. **Agil utveckling (hög prioritet)**: Som startup är snabb iteration, prototypframställning och flexibilitet i utvecklingen avgörande. Diagrambiblioteket måste möjliggöra snabba utvecklingscykler.
   
2. **Diagramtyper (hög prioritet)**:
   - **Munkdiagram (Doughnut Chart)**
   - **Radardiagram (Radar Chart)**
   - **Klustringsprocessdiagram (Clustering Process Chart)**
   - **Ytdiagram med tidsaxel (Area Chart with Time Axis)**
   - **Candlestick-diagram (Candlestick Chart)**
   - **Nightingale-diagram (Nightingale Chart)**
   - **Geo SVG-karta (Geo SVG Map)**
   
   Dessa diagramtyper är särskilt viktiga för att visualisera komplexa datamängder, såsom finansiella trender, vetenskapliga mått och geografisk information.

3. **Gratis och öppen källkod (hög prioritet)**: Verktyget bör vara öppen källkod för att undvika licenskostnader, ge transparens och erbjuda flexibilitet för anpassning.

4. **Kriterier med låg prioritet**:
   - **Körtidshastighet**: Även om prestanda är viktigt är det inte högsta prioritet för det här beslutet.
   - **Skalbarhet**: Även om skalbarhet generellt är viktigt är det omedelbara behovet att bygga en MVP som kan växa över tid. Skalbarhetsfrågor kan hanteras senare.
   - **Bakåtkompatibilitet**: Inte en primär oro för det första bygget, så länge biblioteket är modernt och aktivt underhålls.

### Utvärderade bibliotek:

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

**Översikt**:  
Apache ECharts är ett kraftfullt, flexibelt diagrambibliotek för interaktiva, anpassningsbara visualiseringar. Det ger stöd för ett brett utbud av diagram och är särskilt starkt på komplexa, dynamiska visualiseringar.

**Styrkor**:
- **Avancerad interaktivitet**: ECharts utmärker sig i att tillhandahålla interaktiva diagram och erbjuder funktioner som zoomning, panorering och dynamiska datauppdateringar.
- **Munk-, radar-, candlestick-diagram, Geo SVG-kartor**: ECharts stöder många av de nödvändiga diagramtyperna, inklusive visualiseringar av munk-, radar-, candlestick-diagram och geografiska kartor.
- **Gratis och öppen källkod**: ECharts är ett bibliotek med öppen källkod, vilket passar en startups budgetmedvetna natur och ger frihet att ändra koden.
- **Flexibilitet och utökningsbarhet**: Mycket anpassningsbart, med omfattande stöd för animationer, anpassade visualiseringar och avancerade diagramtekniker.
  
**Svagheter**:
- **Inlärningskurva**: ECharts kan, trots att det är kraftfullt, ha en brantare inlärningskurva på grund av dess flexibilitet och omfattande API.
- **Dokumentationens komplexitet**: Dokumentationen är omfattande men kan vara överväldigande för utvecklare som precis kommit igång.

**Utlåtande**:  
ECharts lämpar sig mycket väl för projektet tack vare dess stöd för interaktiva diagram, inklusive alla nödvändiga typer som candlestick-diagram, radardiagram och geokartor. Dess natur som öppen källkod stämmer överens med projektets behov av flexibilitet och kostnadseffektivitet.

---

### 2. **Chart.js**

**Översikt**:  
Chart.js är ett enkelt, lättanvänt diagrambibliotek för att bygga vanliga diagramtyper. Det är känt för sin enkelhet och sin enkla integration.

**Styrkor**:
- **Användarvänlighet**: Chart.js är mycket enkelt att ställa in och använda, med en minimal inlärningskurva.
- **Öppen källkod**: Chart.js är gratis och har öppen källkod, vilket är avgörande för att minska kostnaderna.
- **Vanliga diagramtyper**: Det stöder grundläggande diagram som munk-, yt-, radar- och linjediagram, som täcker de flesta av de primära behoven.

**Svagheter**:
- **Begränsade avancerade diagram**: Chart.js stöder inte komplexa diagramtyper som candlestick-diagram, Geo SVG-kartor eller klustringsprocessdiagram på ett inbyggt sätt. Även om dessa funktioner kan läggas till via insticksmoduler eller anpassning är det inte lika enkelt som med andra bibliotek.
- **Interaktivitet**: Även om Chart.js stöder grundläggande interaktivitet (t.ex. verktygstips och hovringseffekter) erbjuder det inte lika avancerade funktioner som ECharts eller D3.js.

**Utlåtande**:  
Chart.js är utmärkt för enkla, snabba projekt, men bristen på stöd för komplexa diagramtyper gör det olämpligt för en datatung applikation med avancerade behov som candlestick-diagram och geokartor. Det är ett bra val för prototypframställning, men för de nödvändiga diagramtyperna rekommenderas mer avancerade verktyg.

---

### 3. **ApexCharts**

**Översikt**:  
ApexCharts är ett modernt diagrambibliotek som erbjuder en mängd diagramtyper och fokuserar på interaktiva visualiseringar med ett lättanvänt API.

**Styrkor**:
- **Interaktiva funktioner**: ApexCharts erbjuder interaktiva diagram med verktygstips, zoomning, panorering och uppdateringar.
- **Stöd för finansiella och vetenskapliga diagram**: Det stöder ett brett utbud av diagramtyper, inklusive candlestick-diagram, radardiagram och ytdiagram.
- **Användarvänlighet**: Det har ett okomplicerat API och är enkelt att integrera i ett projekt.
- **Gratis och öppen källkod**: ApexCharts erbjuder en gratis version med öppen källkod som lämpar sig för många användningsfall.
  
**Svagheter**:
- **Komplex anpassning**: Även om det erbjuder många funktioner är anpassningsalternativen inte lika flexibla som ECharts eller D3.js för mycket komplexa eller egna diagrambehov.
- **Geokartor**: ApexCharts stöder inte geokartor eller klustringsprocessdiagram på ett inbyggt sätt, vilka krävs för det här projektet.

**Utlåtande**:  
ApexCharts är en stark kandidat på grund av dess användarvänlighet och interaktivitet, men faller kort på vissa avancerade diagramtyper, särskilt behovet av geokartor och klustringsdiagram. Det är ett bra alternativ för enklare diagram men saknar vissa nödvändiga funktioner.

---

### 4. **AG Charts**

**Översikt**:  
AG Charts är ett diagrambibliotek av kommersiell kvalitet, utformat för prestanda och precision. Det lämpar sig mycket väl för att skapa finansiella, vetenskapliga och affärsmässiga instrumentpaneler.

**Styrkor**:
- **Avancerade diagramtyper**: AG Charts stöder många avancerade diagramtyper, inklusive candlestick-diagram, ytdiagram, radardiagram och mer. Det erbjuder också djup integration med andra AG-Grid-produkter.
- **Hög prestanda**: Det erbjuder utmärkt prestanda, särskilt vid hantering av stora datamängder.
- **Interaktivitet**: AG Charts stöder en rad interaktiva funktioner som zoomning, verktygstips och dynamiska uppdateringar.

**Svagheter**:
- **Inte helt gratis**: Även om AG Charts erbjuder en gratis version är den fullfjädrade versionen betald, vilket kan vara ett hinder för startups som vill minimera kostnaderna.
- **Komplexitet**: Även om biblioteket är funktionsrikt kan det vara överdimensionerat för enklare projekt och kan kräva mer konfiguration och inställning jämfört med andra alternativ.

**Utlåtande**:  
AG Charts är kraftfullt och funktionsrikt men kanske inte den bästa passningen på grund av dess kommersiella natur och kostnadsstruktur. Dess lämplighet beror på om budgeten rymmer betalda versioner eller om alternativ med öppen källkod föredras.

---

### 5. **Highcharts**

**Översikt**:  
Highcharts är ett populärt diagrambibliotek känt för sitt breda utbud av diagramtyper och kraftfulla anpassningsalternativ.

**Styrkor**:
- **Omfattande diagramtyper**: Highcharts stöder ett brett utbud av diagram, inklusive candlestick-, radar-, yt-diagram och geokartor.
- **Interaktivt och dynamiskt**: Highcharts erbjuder rika interaktiva funktioner, inklusive drill-downs, zoomning och panorering.
- **Användarvänlighet**: Det har ett användarvänligt API och bra dokumentation, vilket gör det enkelt att komma igång.

**Svagheter**:
- **Kommersiell licens**: Även om Highcharts erbjuder en gratis version för icke-kommersiellt bruk är den kommersiella licensen dyr, vilket kan vara en betydande nackdel för startups.
- **Inlärningskurva**: Även om den inte är lika brant som ECharts kan inlärningskurvan för Highcharts fortfarande vara utmanande för nybörjare.

**Utlåtande**:  
Highcharts är ett funktionsrikt bibliotek, men dess kommersiella licensiering gör det mindre lämpligt för kostnadskänsliga projekt med öppen källkod. Dess omfattande diagramalternativ är ett plus, men licensfrågan begränsar dess attraktionskraft för det här användningsfallet.

---

### 6. **Carbon Charts**

**Översikt**:  
Carbon Charts är ett diagrambibliotek utvecklat av IBM, utformat för att skapa visuellt tilltalande och mycket anpassningsbara diagram.

**Styrkor**:
- **Anpassningsbarhet**: Carbon Charts möjliggör omfattande anpassning av diagrams utseende och beteende.
- **Öppen källkod**: Det är gratis och har öppen källkod, vilket stämmer överens med projektets krav på budgetvänliga lösningar.
- **Stöd för vanliga diagram**: Det stöder vanliga diagramtyper som munk-, radar- och ytdiagram, men saknar stöd för mer avancerade typer som geokartor eller candlestick-diagram.

**Svagheter**:
- **Begränsade avancerade diagramtyper**: Det stöder inte geokartor, klustringsprocessdiagram eller candlestick-diagram, som är nödvändiga för projektet.
- **Mindre ekosystem**: Carbon Charts har en mindre gemenskap och ett mindre ekosystem jämfört med större diagrambibliotek som ECharts eller Highcharts.

**Utlåtande**:  
Carbon Charts har öppen källkod och är anpassningsbart men saknar stöd för de mer komplexa diagramtyper som behövs för det här projektet. Det lämpar sig bättre för enklare diagrambehov.

---

### 7. **Layer Cake**

**Översikt**:  
Layer Cake är ett bibliotek för datavisualisering utformat för att skapa flexibla, skiktade visualiseringar.

**Styrkor**:
- **Anpassningsbara lager**: Det erbjuder kraftfulla alternativ för skiktning för komplexa visualiseringar.
- **Öppen källkod**: Det är gratis och har öppen källkod, vilket gör det till ett gångbart alternativ för budgetmedvetna projekt.

**Svagheter**:
- **Begränsad dokumentation**: Layer Cake saknar omfattande dokumentation och communitystöd, vilket gör det svårare att arbeta med jämfört med mer etablerade bibliotek.
- **Inte byggt för diagram**: Layer Cake lämpar sig bättre för visualiseringar som inte är diagram, så dess färdiga diagramalternativ är begränsade.

**Utlåtande**:  
Även om det är intressant för unika visualiseringar är Layer Cake inte idealiskt för traditionella diagramkrav som candlestick-diagram eller radardiagram. Det lämpar sig bättre för anpassade visualiseringar utanför omfånget för standarddiagram.

---

### 8. **D3.js**

**Översikt**:  
D3.js är ett kraftfullt JavaScript-bibliotek för att skapa datadrivna visualiseringar via HTML, SVG och CSS.

**Styrkor**:
- **Oöverträffad flexibilitet**: D3.js gör det möjligt att skapa i princip vilken typ av anpassad visualisering som helst, vilket gör det mycket kraftfullt för avancerade och interaktiva diagram.
- **Omfattande funktioner**: Det stöder alla nödvändiga diagramtyper, inklusive geokartor, klustringsdiagram och mer.
- **Anpassningsbart**: Nivån av anpassning i D3.js är oöverträffad, vilket gör att utvecklare kan bygga mycket skräddarsydda visualiseringar.

**Svagheter**:
- **Brant inlärningskurva**: D3.js har en brant inlärningskurva och är mer komplext att integrera jämfört med andra bibliotek.
- **Tidskrävande**: Att bygga diagram i D3.js kan vara tidskrävande, särskilt för vanliga diagram som candlestick- eller munkdiagram.

**Utlåtande**:  
D3.js är otroligt kraftfullt för avancerade, anpassade diagram men överdimensionerat för många typiska användningsfall på grund av dess branta inlärningskurva och utvecklingstid. Det är bäst för situationer där de andra diagrambiblioteken inte erbjuder den nödvändiga nivån av anpassning.

---

### Slutsats

Efter att ha utvärderat biblioteken utifrån projektets behov framstår **Apache ECharts** som det bästa alternativet. Det stöder hela spektrumet av nödvändiga diagram, inklusive geokartor, candlestick-diagram och klustringsdiagram. Det har öppen källkod, är funktionsrikt och mycket interaktivt, vilket stämmer perfekt överens med projektets mål. Även om **D3.js** erbjuder störst flexibilitet gör dess komplexitet och tidsinvestering det mindre idealiskt för en startup som vill iterera snabbt. **ApexCharts** och **Chart.js** är bra alternativ för enklare projekt men saknar stöd för avancerade diagramtyper.
