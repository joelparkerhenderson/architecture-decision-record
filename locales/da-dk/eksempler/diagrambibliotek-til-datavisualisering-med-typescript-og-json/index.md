# Arkitekturbeslutningspost: diagrambibliotek til datavisualisering med TypeScript og JSON

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

**Primært mål:**  
At vælge et avanceret diagramværktøj til at skabe interaktive visualiseringer, med fokus på finansielle data, videnskabelige data og offentlige data med TypeScript og JSON. Biblioteket bør tilbyde robuste funktioner og fleksibilitet og være open source. 

### Kontekst og krav:

1. **Agil udvikling (høj prioritet)**: som startup er hurtig iteration, prototyping og fleksibilitet i udviklingen afgørende. Diagrambiblioteket skal muliggøre hurtige udviklingscyklusser.
   
2. **Diagramtyper (høj prioritet)**:
   - **Donutdiagram (Doughnut Chart)**
   - **Radardiagram (Radar Chart)**
   - **Klyngeprocesdiagram (Clustering Process Chart)**
   - **Områdediagram med tidsakse (Area Chart with Time Axis)**
   - **Candlestick-diagram (Candlestick Chart)**
   - **Nightingale-diagram (Nightingale Chart)**
   - **Geo SVG-kort (Geo SVG Map)**
   
   Disse diagramtyper er særligt vigtige til at visualisere komplekse datasæt, såsom finansielle tendenser, videnskabelige målinger og geografisk information.

3. **Gratis og open source (høj prioritet)**: værktøjet bør være open source for at undgå licensomkostninger, give gennemsigtighed og tilbyde fleksibilitet til tilpasning.

4. **Kriterier med lav prioritet**:
   - **Kørselshastighed**: selv om ydeevne er vigtig, er det ikke højeste prioritet for denne beslutning.
   - **Skalerbarhed**: selv om skalerbarhed generelt er vigtig, er det umiddelbare behov at bygge en MVP, der kan vokse over tid. Skalerbarhedsproblemer kan håndteres senere.
   - **Bagudkompatibilitet**: ikke en primær bekymring for den indledende bygning, så længe biblioteket er moderne og aktivt vedligeholdes.

### Evaluerede biblioteker:

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

**Oversigt**:  
Apache ECharts er et kraftfuldt, fleksibelt diagrambibliotek til interaktive, tilpasselige visualiseringer. Det understøtter et bredt udvalg af diagrammer og er særligt stærkt til komplekse, dynamiske visualiseringer.

**Styrker**:
- **Avanceret interaktivitet**: ECharts udmærker sig ved at levere interaktive diagrammer og tilbyder funktioner som zoom, panorering og dynamiske dataopdateringer.
- **Donut-, radar-, candlestick-diagrammer, Geo SVG-kort**: ECharts understøtter mange af de nødvendige diagramtyper, herunder visualiseringer af donut-, radar-, candlestick-diagrammer og geografiske kort.
- **Gratis og open source**: ECharts er et open source-bibliotek, hvilket passer til en startups budgetbevidste natur og giver frihed til at ændre koden.
- **Fleksibilitet og udvidelsesmuligheder**: meget tilpasseligt med omfattende understøttelse af animationer, brugerdefinerede visualiseringer og avancerede diagramteknikker.
  
**Svagheder**:
- **Indlæringskurve**: ECharts kan, selv om det er kraftfuldt, have en stejlere indlæringskurve på grund af dets fleksibilitet og omfattende API.
- **Dokumentationens kompleksitet**: dokumentationen er omfattende, men kan være overvældende for udviklere, der lige er begyndt.

**Vurdering**:  
ECharts passer meget godt til projektet takket være understøttelsen af interaktive diagrammer, herunder alle nødvendige typer som candlestick-diagrammer, radardiagrammer og geokort. Dets open source-natur stemmer overens med projektets behov for fleksibilitet og omkostningseffektivitet.

---

### 2. **Chart.js**

**Oversigt**:  
Chart.js er et enkelt, letanvendeligt diagrambibliotek til at bygge almindelige diagramtyper. Det er kendt for sin enkelhed og nemme integration.

**Styrker**:
- **Brugervenlighed**: Chart.js er meget nemt at sætte op og bruge med en minimal indlæringskurve.
- **Open source**: Chart.js er gratis og open source, hvilket er afgørende for at reducere omkostningerne.
- **Almindelige diagramtyper**: det understøtter grundlæggende diagrammer som donut-, område-, radar- og liniediagrammer, der dækker de fleste af de primære behov.

**Svagheder**:
- **Begrænsede avancerede diagrammer**: Chart.js understøtter ikke komplekse diagramtyper som candlestick-diagrammer, Geo SVG-kort eller klyngeprocesdiagrammer nativt. Selv om disse funktioner kan tilføjes via plugins eller tilpasning, er det ikke lige så ligetil som med andre biblioteker.
- **Interaktivitet**: selv om Chart.js understøtter grundlæggende interaktivitet (f.eks. værktøjstip og hover-effekter), tilbyder det ikke lige så avancerede funktioner som ECharts eller D3.js.

**Vurdering**:  
Chart.js er fremragende til enkle, hurtige projekter, men manglen på understøttelse af komplekse diagramtyper gør det uegnet til en datatung applikation med avancerede behov som candlestick-diagrammer og geokort. Det er et godt valg til prototyping, men til de nødvendige diagramtyper anbefales mere avancerede værktøjer.

---

### 3. **ApexCharts**

**Oversigt**:  
ApexCharts er et moderne diagrambibliotek, der tilbyder en række diagramtyper og fokuserer på interaktive visualiseringer med et letanvendeligt API.

**Styrker**:
- **Interaktive funktioner**: ApexCharts tilbyder interaktive diagrammer med værktøjstip, zoom, panorering og opdateringer.
- **Understøttelse af finansielle og videnskabelige diagrammer**: det understøtter et bredt udvalg af diagramtyper, herunder candlestick-diagrammer, radardiagrammer og områdediagrammer.
- **Brugervenlighed**: det har et ligetil API og er nemt at integrere i et projekt.
- **Gratis og open source**: ApexCharts tilbyder en gratis open source-version, der er egnet til mange anvendelsestilfælde.
  
**Svagheder**:
- **Kompleks tilpasning**: selv om det tilbyder mange funktioner, er tilpasningsmulighederne ikke lige så fleksible som ECharts eller D3.js til meget komplekse eller brugerdefinerede diagrambehov.
- **Geokort**: ApexCharts understøtter ikke geokort eller klyngeprocesdiagrammer nativt, som kræves til dette projekt.

**Vurdering**:  
ApexCharts er en stærk kandidat på grund af dets brugervenlighed og interaktivitet, men kommer til kort på nogle avancerede diagramtyper, især behovet for geokort og klyngediagrammer. Det er et godt alternativ til enklere diagrammer, men mangler nogle nødvendige funktioner.

---

### 4. **AG Charts**

**Oversigt**:  
AG Charts er et diagrambibliotek af kommerciel kvalitet, designet til ydeevne og præcision. Det er meget velegnet til at skabe finansielle, videnskabelige og forretningsmæssige dashboards.

**Styrker**:
- **Avancerede diagramtyper**: AG Charts understøtter mange avancerede diagramtyper, herunder candlestick-diagrammer, områdediagrammer, radardiagrammer og mere. Det tilbyder også dyb integration med andre AG-Grid-produkter.
- **Høj ydeevne**: det tilbyder fremragende ydeevne, især ved håndtering af store datasæt.
- **Interaktivitet**: AG Charts understøtter en række interaktive funktioner som zoom, værktøjstip og dynamiske opdateringer.

**Svagheder**:
- **Ikke helt gratis**: selv om AG Charts tilbyder en gratis version, er den fuldt udstyrede version betalt, hvilket kan være en barriere for startups, der vil minimere omkostningerne.
- **Kompleksitet**: selv om biblioteket er funktionsrigt, kan det være overdimensioneret til enklere projekter og kan kræve mere konfiguration og opsætning sammenlignet med andre muligheder.

**Vurdering**:  
AG Charts er kraftfuldt og funktionsrigt, men måske ikke det bedste match på grund af dets kommercielle natur og omkostningsstruktur. Dets egnethed afhænger af, om budgettet kan rumme betalte versioner, eller om open source-alternativer foretrækkes.

---

### 5. **Highcharts**

**Oversigt**:  
Highcharts er et populært diagrambibliotek kendt for sit brede udvalg af diagramtyper og kraftfulde tilpasningsmuligheder.

**Styrker**:
- **Omfattende diagramtyper**: Highcharts understøtter et bredt udvalg af diagrammer, herunder candlestick-, radar-, områdediagrammer og geokort.
- **Interaktivt og dynamisk**: Highcharts tilbyder rige interaktive funktioner, herunder drill-downs, zoom og panorering.
- **Brugervenlighed**: det har et brugervenligt API og god dokumentation, hvilket gør det nemt at komme i gang.

**Svagheder**:
- **Kommerciel licens**: selv om Highcharts tilbyder en gratis version til ikke-kommerciel brug, er den kommercielle licens dyr, hvilket kan være en betydelig ulempe for startups.
- **Indlæringskurve**: selv om den ikke er så stejl som ECharts', kan Highcharts' indlæringskurve stadig være udfordrende for begyndere.

**Vurdering**:  
Highcharts er et funktionsrigt bibliotek, men dets kommercielle licensering gør det mindre egnet til omkostningsfølsomme open source-projekter. Dets omfattende diagrammuligheder er et plus, men licensspørgsmålet begrænser dets appel til dette anvendelsestilfælde.

---

### 6. **Carbon Charts**

**Oversigt**:  
Carbon Charts er et diagrambibliotek udviklet af IBM, designet til at skabe visuelt tiltalende og meget tilpasselige diagrammer.

**Styrker**:
- **Tilpasselighed**: Carbon Charts giver mulighed for omfattende tilpasning af diagrammers udseende og adfærd.
- **Open source**: det er gratis og open source, hvilket stemmer overens med projektets krav om budgetvenlige løsninger.
- **Understøttelse af almindelige diagrammer**: det understøtter almindelige diagramtyper som donut-, radar- og områdediagrammer, men mangler understøttelse af mere avancerede typer som geokort eller candlestick-diagrammer.

**Svagheder**:
- **Begrænsede avancerede diagramtyper**: det understøtter ikke geokort, klyngeprocesdiagrammer eller candlestick-diagrammer, som er nødvendige for projektet.
- **Mindre økosystem**: Carbon Charts har et mindre fællesskab og økosystem sammenlignet med større diagrambiblioteker som ECharts eller Highcharts.

**Vurdering**:  
Carbon Charts er open source og tilpasseligt, men mangler understøttelse af de mere komplekse diagramtyper, der er nødvendige for dette projekt. Det er bedre egnet til enklere diagrambehov.

---

### 7. **Layer Cake**

**Oversigt**:  
Layer Cake er et datavisualiseringsbibliotek designet til at skabe fleksible, lagdelte visualiseringer.

**Styrker**:
- **Tilpasselige lag**: det tilbyder kraftfulde lagdelingsmuligheder til komplekse visualiseringer.
- **Open source**: det er gratis og open source, hvilket gør det til en brugbar mulighed for budgetbevidste projekter.

**Svagheder**:
- **Begrænset dokumentation**: Layer Cake mangler omfattende dokumentation og fællesskabsstøtte, hvilket gør det sværere at arbejde med sammenlignet med mere etablerede biblioteker.
- **Ikke bygget til diagrammer**: Layer Cake er bedre egnet til visualiseringer, der ikke er diagrammer, så dets færdige diagrammuligheder er begrænsede.

**Vurdering**:  
Selv om det er interessant til unikke visualiseringer, er Layer Cake ikke ideelt til traditionelle diagramkrav som candlestick-diagrammer eller radardiagrammer. Det er bedre egnet til brugerdefinerede visualiseringer uden for standarddiagrammers omfang.

---

### 8. **D3.js**

**Oversigt**:  
D3.js er et kraftfuldt JavaScript-bibliotek til at skabe datadrevne visualiseringer via HTML, SVG og CSS.

**Styrker**:
- **Uovertruffen fleksibilitet**: D3.js gør det muligt at skabe stort set enhver type brugerdefineret visualisering, hvilket gør det meget kraftfuldt til avancerede og interaktive diagrammer.
- **Omfattende funktioner**: det understøtter alle nødvendige diagramtyper, herunder geokort, klyngediagrammer og mere.
- **Tilpasseligt**: niveauet af tilpasning i D3.js er uovertruffet, hvilket giver udviklere mulighed for at bygge meget skræddersyede visualiseringer.

**Svagheder**:
- **Stejl indlæringskurve**: D3.js har en stejl indlæringskurve og er mere komplekst at integrere sammenlignet med andre biblioteker.
- **Tidskrævende**: at bygge diagrammer i D3.js kan være tidskrævende, især til almindelige diagrammer som candlestick- eller donutdiagrammer.

**Vurdering**:  
D3.js er utroligt kraftfuldt til avancerede, brugerdefinerede diagrammer, men overdimensioneret til mange typiske anvendelsestilfælde på grund af dets stejle indlæringskurve og udviklingstid. Det er bedst til situationer, hvor de andre diagrambiblioteker ikke tilbyder det nødvendige niveau af tilpasning.

---

### Konklusion

Efter at have evalueret bibliotekerne ud fra projektets behov fremstår **Apache ECharts** som den bedste mulighed. Det understøtter hele spektret af nødvendige diagrammer, herunder geokort, candlestick-diagrammer og klyngediagrammer. Det er open source, funktionsrigt og meget interaktivt, hvilket passer perfekt til projektets mål. Selv om **D3.js** tilbyder størst fleksibilitet, gør dets kompleksitet og tidsinvestering det mindre ideelt til en startup, der vil iterere hurtigt. **ApexCharts** og **Chart.js** er gode alternativer til enklere projekter, men mangler understøttelse af avancerede diagramtyper.
