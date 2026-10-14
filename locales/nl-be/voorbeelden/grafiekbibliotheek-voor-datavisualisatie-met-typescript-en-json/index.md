# Architectuurbeslissingsdocument: grafiekbibliotheek voor datavisualisatie met TypeScript en JSON

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

**Primair doel:**  
Een geavanceerde grafiektoolkit selecteren voor het maken van interactieve visualisaties, met focus op financiële data, wetenschappelijke data en overheidsdata met TypeScript en JSON. De bibliotheek moet robuuste functies en flexibiliteit bieden en open source zijn. 

### Context en eisen:

1. **Agile ontwikkeling (hoge prioriteit)**: als startup zijn snelle iteratie, prototyping en flexibiliteit in ontwikkeling cruciaal. De grafiekbibliotheek moet snelle ontwikkelcycli mogelijk maken.
   
2. **Grafiektypen (hoge prioriteit)**:
   - **Donutdiagram (Doughnut Chart)**
   - **Radardiagram (Radar Chart)**
   - **Clusteringprocesdiagram (Clustering Process Chart)**
   - **Vlakdiagram met tijdas (Area Chart with Time Axis)**
   - **Candlestick-diagram (Candlestick Chart)**
   - **Nightingale-diagram (Nightingale Chart)**
   - **Geo SVG-kaart (Geo SVG Map)**
   
   Deze grafiektypen zijn bijzonder belangrijk voor het visualiseren van complexe datasets, zoals financiële trends, wetenschappelijke statistieken en geografische informatie.

3. **Gratis en open source (hoge prioriteit)**: de tool moet open source zijn om licentiekosten te vermijden, transparantie te bieden en flexibiliteit voor aanpassing te geven.

4. **Criteria met lage prioriteit**:
   - **Runtimesnelheid**: hoewel prestaties belangrijk zijn, is het niet de hoogste prioriteit voor deze beslissing.
   - **Schaalbaarheid**: hoewel schaalbaarheid over het algemeen belangrijk is, is de onmiddellijke behoefte het bouwen van een MVP die in de loop van de tijd kan groeien. Schaalbaarheidskwesties kunnen later worden aangepakt.
   - **Achterwaartse compatibiliteit**: geen primaire zorg voor de eerste bouw, zolang de bibliotheek modern is en actief wordt onderhouden.

### Geëvalueerde bibliotheken:

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

**Overzicht**:  
Apache ECharts is een krachtige, flexibele grafiekbibliotheek voor interactieve, aanpasbare visualisaties. Het ondersteunt een breed scala aan grafieken en is vooral sterk in complexe, dynamische visualisaties.

**Sterke punten**:
- **Geavanceerde interactiviteit**: ECharts blinkt uit in het bieden van interactieve grafieken en biedt functies zoals zoomen, pannen en dynamische data-updates.
- **Donut-, radar-, candlestick-diagrammen, Geo SVG-kaarten**: ECharts ondersteunt veel van de benodigde grafiektypen, waaronder visualisaties van donut-, radar-, candlestick-diagrammen en geografische kaarten.
- **Gratis en open source**: ECharts is een open-sourcebibliotheek, wat past bij het budgetbewuste karakter van een startup en de vrijheid geeft de code te wijzigen.
- **Flexibiliteit en uitbreidbaarheid**: zeer aanpasbaar, met uitgebreide ondersteuning voor animaties, aangepaste visualisaties en geavanceerde grafiektechnieken.
  
**Zwakke punten**:
- **Leercurve**: ECharts kan, hoewel krachtig, een steilere leercurve hebben vanwege de flexibiliteit en de uitgebreide API.
- **Complexiteit van de documentatie**: de documentatie is uitgebreid, maar kan overweldigend zijn voor ontwikkelaars die net beginnen.

**Oordeel**:  
ECharts is zeer geschikt voor het project dankzij de ondersteuning voor interactieve grafieken, inclusief alle benodigde typen zoals candlestick-diagrammen, radardiagrammen en geokaarten. Het open-sourcekarakter sluit aan bij de behoefte van het project aan flexibiliteit en kosteneffectiviteit.

---

### 2. **Chart.js**

**Overzicht**:  
Chart.js is een eenvoudige, gebruiksvriendelijke grafiekbibliotheek voor het bouwen van gangbare grafiektypen. Het staat bekend om zijn eenvoud en gemakkelijke integratie.

**Sterke punten**:
- **Gebruiksgemak**: Chart.js is zeer eenvoudig in te stellen en te gebruiken, met een minimale leercurve.
- **Open source**: Chart.js is gratis en open source, wat cruciaal is voor het verlagen van de kosten.
- **Gangbare grafiektypen**: het ondersteunt basisgrafieken zoals donut-, vlak-, radar- en lijndiagrammen, die de meeste primaire behoeften dekken.

**Zwakke punten**:
- **Beperkte geavanceerde grafieken**: Chart.js ondersteunt complexe grafiektypen zoals candlestick-diagrammen, Geo SVG-kaarten of clusteringprocesdiagrammen niet native. Hoewel deze functies via plug-ins of aanpassing kunnen worden toegevoegd, is dat niet zo eenvoudig als bij andere bibliotheken.
- **Interactiviteit**: hoewel Chart.js basisinteractiviteit ondersteunt (bijv. tooltips en hovereffecten), biedt het niet zulke geavanceerde functies als ECharts of D3.js.

**Oordeel**:  
Chart.js is uitstekend voor eenvoudige, snelle projecten, maar het gebrek aan ondersteuning voor complexe grafiektypen maakt het ongeschikt voor een datazware applicatie met geavanceerde behoeften zoals candlestick-diagrammen en geokaarten. Het is een goede keuze voor prototyping, maar voor de benodigde grafiektypen worden geavanceerdere tools aanbevolen.

---

### 3. **ApexCharts**

**Overzicht**:  
ApexCharts is een moderne grafiekbibliotheek die een scala aan grafiektypen biedt en zich richt op interactieve visualisaties met een gebruiksvriendelijke API.

**Sterke punten**:
- **Interactieve functies**: ApexCharts biedt interactieve grafieken met tooltips, zoomen, pannen en updates.
- **Ondersteuning voor financiële en wetenschappelijke grafieken**: het ondersteunt een breed scala aan grafiektypen, waaronder candlestick-diagrammen, radardiagrammen en vlakdiagrammen.
- **Gebruiksgemak**: het heeft een eenvoudige API en is gemakkelijk in een project te integreren.
- **Gratis en open source**: ApexCharts biedt een gratis open-sourceversie die geschikt is voor veel gebruiksscenario's.
  
**Zwakke punten**:
- **Complexe aanpassing**: hoewel het veel functies biedt, zijn de aanpassingsopties niet zo flexibel als ECharts of D3.js voor zeer complexe of aangepaste grafiekbehoeften.
- **Geokaarten**: ApexCharts ondersteunt geokaarten of clusteringprocesdiagrammen, die voor dit project vereist zijn, niet native.

**Oordeel**:  
ApexCharts is een sterke kandidaat vanwege het gebruiksgemak en de interactiviteit, maar schiet tekort bij sommige geavanceerde grafiektypen, vooral de behoefte aan geokaarten en clusteringdiagrammen. Het is een goed alternatief voor eenvoudigere grafieken, maar mist enkele benodigde functies.

---

### 4. **AG Charts**

**Overzicht**:  
AG Charts is een grafiekbibliotheek van commerciële kwaliteit, ontworpen voor prestaties en precisie. Het is zeer geschikt voor het maken van financiële, wetenschappelijke en zakelijke dashboards.

**Sterke punten**:
- **Geavanceerde grafiektypen**: AG Charts ondersteunt veel geavanceerde grafiektypen, waaronder candlestick-diagrammen, vlakdiagrammen, radardiagrammen en meer. Het biedt ook diepe integratie met andere AG-Grid-producten.
- **Hoge prestaties**: het biedt uitstekende prestaties, vooral bij het verwerken van grote datasets.
- **Interactiviteit**: AG Charts ondersteunt een reeks interactieve functies zoals zoomen, tooltips en dynamische updates.

**Zwakke punten**:
- **Niet volledig gratis**: hoewel AG Charts een gratis versie biedt, is de volledige versie betaald, wat een barrière kan zijn voor startups die kosten willen minimaliseren.
- **Complexiteit**: hoewel de bibliotheek functierijk is, kan ze overdreven zijn voor eenvoudigere projecten en meer configuratie en inrichting vereisen dan andere opties.

**Oordeel**:  
AG Charts is krachtig en functierijk, maar misschien niet de beste match vanwege het commerciële karakter en de kostenstructuur. De geschiktheid hangt ervan af of het budget betaalde versies toelaat of dat open-sourcealternatieven de voorkeur hebben.

---

### 5. **Highcharts**

**Overzicht**:  
Highcharts is een populaire grafiekbibliotheek die bekendstaat om zijn brede scala aan grafiektypen en krachtige aanpassingsopties.

**Sterke punten**:
- **Uitgebreide grafiektypen**: Highcharts ondersteunt een breed scala aan grafieken, waaronder candlestick-, radar-, vlakdiagrammen en geokaarten.
- **Interactief en dynamisch**: Highcharts biedt rijke interactieve functies, waaronder drill-downs, zoomen en pannen.
- **Gebruiksgemak**: het heeft een gebruiksvriendelijke API en goede documentatie, waardoor het gemakkelijk is om te beginnen.

**Zwakke punten**:
- **Commerciële licentie**: hoewel Highcharts een gratis versie biedt voor niet-commercieel gebruik, is de commerciële licentie duur, wat een aanzienlijk nadeel kan zijn voor startups.
- **Leercurve**: hoewel niet zo steil als die van ECharts, kan de leercurve van Highcharts nog steeds uitdagend zijn voor beginners.

**Oordeel**:  
Highcharts is een functierijke bibliotheek, maar de commerciële licentie maakt het minder geschikt voor kostengevoelige open-sourceprojecten. De uitgebreide grafiekopties zijn een pluspunt, maar de licentiekwestie beperkt de aantrekkingskracht voor dit gebruiksscenario.

---

### 6. **Carbon Charts**

**Overzicht**:  
Carbon Charts is een door IBM ontwikkelde grafiekbibliotheek, ontworpen om visueel aantrekkelijke en zeer aanpasbare grafieken te maken.

**Sterke punten**:
- **Aanpasbaarheid**: Carbon Charts maakt uitgebreide aanpassing van het uiterlijk en gedrag van grafieken mogelijk.
- **Open source**: het is gratis en open source, wat aansluit bij de projecteis van budgetvriendelijke oplossingen.
- **Ondersteuning voor gangbare grafieken**: het ondersteunt gangbare grafiektypen zoals donut-, radar- en vlakdiagrammen, maar mist ondersteuning voor geavanceerdere typen zoals geokaarten of candlestick-diagrammen.

**Zwakke punten**:
- **Beperkte geavanceerde grafiektypen**: het ondersteunt geen geokaarten, clusteringprocesdiagrammen of candlestick-diagrammen, die nodig zijn voor het project.
- **Kleiner ecosysteem**: Carbon Charts heeft een kleinere gemeenschap en een kleiner ecosysteem dan grotere grafiekbibliotheken zoals ECharts of Highcharts.

**Oordeel**:  
Carbon Charts is open source en aanpasbaar, maar mist ondersteuning voor de complexere grafiektypen die voor dit project nodig zijn. Het is beter geschikt voor eenvoudigere grafiekbehoeften.

---

### 7. **Layer Cake**

**Overzicht**:  
Layer Cake is een datavisualisatiebibliotheek ontworpen voor het maken van flexibele, gelaagde visualisaties.

**Sterke punten**:
- **Aanpasbare lagen**: het biedt krachtige gelaagdheidsopties voor complexe visualisaties.
- **Open source**: het is gratis en open source, wat het een haalbare optie maakt voor budgetbewuste projecten.

**Zwakke punten**:
- **Beperkte documentatie**: Layer Cake mist uitgebreide documentatie en ondersteuning door de gemeenschap, waardoor het moeilijker is mee te werken dan met meer gevestigde bibliotheken.
- **Niet gebouwd voor grafieken**: Layer Cake is beter geschikt voor visualisaties die geen grafieken zijn, dus de kant-en-klare grafiekopties zijn beperkt.

**Oordeel**:  
Hoewel interessant voor unieke visualisaties, is Layer Cake niet ideaal voor traditionele grafiekeisen zoals candlestick-diagrammen of radardiagrammen. Het is beter geschikt voor aangepaste visualisaties buiten de reikwijdte van standaardgrafieken.

---

### 8. **D3.js**

**Overzicht**:  
D3.js is een krachtige JavaScript-bibliotheek voor het maken van datagedreven visualisaties met HTML, SVG en CSS.

**Sterke punten**:
- **Ongeëvenaarde flexibiliteit**: met D3.js kun je vrijwel elk type aangepaste visualisatie maken, waardoor het zeer krachtig is voor geavanceerde en interactieve grafieken.
- **Uitgebreide functies**: het ondersteunt alle benodigde grafiektypen, waaronder geokaarten, clusteringdiagrammen en meer.
- **Aanpasbaar**: het niveau van aanpassing in D3.js is ongeëvenaard, waardoor ontwikkelaars sterk op maat gemaakte visualisaties kunnen bouwen.

**Zwakke punten**:
- **Steile leercurve**: D3.js heeft een steile leercurve en is complexer te integreren dan andere bibliotheken.
- **Tijdrovend**: het bouwen van grafieken in D3.js kan tijdrovend zijn, vooral voor gangbare grafieken zoals candlestick- of donutdiagrammen.

**Oordeel**:  
D3.js is ongelooflijk krachtig voor geavanceerde, aangepaste grafieken, maar overdreven voor veel typische gebruiksscenario's vanwege de steile leercurve en ontwikkeltijd. Het is het best voor situaties waarin de andere grafiekbibliotheken het benodigde niveau van aanpassing niet bieden.

---

### Conclusie

Na het evalueren van de bibliotheken op basis van de behoeften van het project komt **Apache ECharts** naar voren als de beste optie. Het ondersteunt het volledige spectrum van benodigde grafieken, waaronder geokaarten, candlestick-diagrammen en clusteringdiagrammen. Het is open source, functierijk en zeer interactief, wat perfect aansluit bij de doelen van het project. Hoewel **D3.js** de meeste flexibiliteit biedt, maken de complexiteit en tijdsinvestering het minder ideaal voor een startup die snel wil itereren. **ApexCharts** en **Chart.js** zijn goede alternatieven voor eenvoudigere projecten, maar missen ondersteuning voor geavanceerde grafiektypen.
