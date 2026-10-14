# Zapis arhitekturne odluke: biblioteka grafikona za vizualizaciju podataka s TypeScriptom i JSON-om

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

**Primarni cilj:**  
Odabrati napredan skup alata za grafikone za izradu interaktivnih vizualizacija, s fokusom na financijske, znanstvene i državne podatke, koristeći TypeScript i JSON. Biblioteka bi trebala pružati robusne značajke, fleksibilnost i biti otvorenog koda. 

### Kontekst i zahtjevi:

1. **Agilni razvoj (visoki prioritet)**: Kao startup, brza iteracija, prototipiranje i fleksibilnost u razvoju su ključni. Biblioteka grafikona mora omogućiti brze razvojne cikluse.
   
2. **Vrste grafikona (visoki prioritet)**:
   - **Doughnut grafikon**
   - **Radarski grafikon**
   - **Grafikon procesa grupiranja**
   - **Površinski grafikon s vremenskom osi**
   - **Svjećasti grafikon (candlestick)**
   - **Nightingaleov grafikon**
   - **Geo SVG karta**
   
   Ove su vrste grafikona posebno važne za vizualizaciju složenih skupova podataka, poput financijskih trendova, znanstvenih metrika i geografskih informacija.

3. **Besplatno i otvorenog koda (visoki prioritet)**: Skup alata trebao bi biti otvorenog koda kako bi se izbjegli troškovi licenciranja, pružila transparentnost i ponudila fleksibilnost prilagodbe.

4. **Kriteriji niske važnosti**:
   - **Brzina izvođenja**: Iako su performanse važne, nisu najviši prioritet za ovu odluku.
   - **Skalabilnost**: Iako je skalabilnost općenito važna, neposredna je potreba izgraditi MVP koji može rasti tijekom vremena. Pitanja skalabilnosti mogu se riješiti kasnije.
   - **Povratna kompatibilnost**: Nije primarna briga za početnu izgradnju, sve dok je biblioteka moderna i aktivno održavana.

### Vrednovane biblioteke:

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

**Pregled**:  
Apache ECharts je moćna, fleksibilna biblioteka grafikona za interaktivne, prilagodljive vizualizacije. Pruža podršku za široku paletu grafikona i osobito je jaka u složenim, dinamičnim vizualizacijama.

**Snage**:
- **Napredna interaktivnost**: ECharts se ističe pružanjem interaktivnih grafikona, nudeći značajke poput zumiranja, pomicanja i dinamičkih ažuriranja podataka.
- **Doughnut, radarski, svjećasti grafikoni, Geo SVG karte**: ECharts podržava mnoge od potrebnih vrsta grafikona, uključujući doughnut, radarske, svjećaste i vizualizacije zemljopisnih karata.
- **Besplatan i otvorenog koda**: ECharts je biblioteka otvorenog koda, što odgovara proračunski osviještenoj prirodi startupa i daje slobodu izmjene koda.
- **Fleksibilnost i proširivost**: Vrlo prilagodljiva, s opsežnom podrškom za animacije, prilagođene vizualizacije i napredne tehnike izrade grafikona.
  
**Slabosti**:
- **Krivulja učenja**: ECharts, iako moćan, može imati strmiju krivulju učenja zbog svoje fleksibilnosti i opsežnog API-ja.
- **Složenost dokumentacije**: Dokumentacija je sveobuhvatna, ali može biti zastrašujuća za programere koji tek počinju s njom.

**Presuda**:  
ECharts je vrlo prikladan za projekt zbog podrške za interaktivne grafikone, uključujući sve potrebne vrste poput svjećastih grafikona, radarskih grafikona i geo karata. Njegova otvorena priroda u skladu je s potrebom projekta za fleksibilnošću i isplativošću.

---

### 2. **Chart.js**

**Pregled**:  
Chart.js je jednostavna biblioteka grafikona, laka za uporabu, za izradu uobičajenih vrsta grafikona. Poznata je po jednostavnosti i lakoći integracije.

**Snage**:
- **Jednostavnost uporabe**: Chart.js je vrlo jednostavan za postavljanje i uporabu, s minimalnom krivuljom učenja.
- **Otvorenog koda**: Chart.js je besplatan i otvorenog koda, što je ključno za smanjenje troškova.
- **Uobičajene vrste grafikona**: Podržava osnovne grafikone poput doughnut, površinskih, radarskih i linijskih grafikona, koji pokrivaju većinu primarnih potreba.

**Slabosti**:
- **Ograničeni napredni grafikoni**: Chart.js izvorno ne podržava složene vrste grafikona poput svjećastih grafikona, geo SVG karata ili grafikona procesa grupiranja. Iako se te značajke mogu dodati putem dodataka ili prilagodbe, to nije tako jednostavno kao s drugim bibliotekama.
- **Interaktivnost**: Iako Chart.js podržava osnovnu interaktivnost (npr. opise i efekte prelaska mišem), ne nudi tako napredne značajke kao ECharts ili D3.js.

**Presuda**:  
Chart.js je izvrstan za jednostavne, brze projekte, ali nedostatak podrške za složene vrste grafikona čini ga neprikladnim za aplikaciju s mnogo podataka i naprednim potrebama poput svjećastih grafikona i geo karata. Dobar je izbor za prototipiranje, ali za potrebne vrste grafikona preporučuju se napredniji alati.

---

### 3. **ApexCharts**

**Pregled**:  
ApexCharts je moderna biblioteka grafikona koja pruža razne vrste grafikona i usredotočuje se na interaktivne vizualizacije s API-jem lakim za uporabu.

**Snage**:
- **Interaktivne značajke**: ApexCharts nudi interaktivne grafikone s opisima, zumiranjem, pomicanjem i ažuriranjima.
- **Podrška za financijske i znanstvene grafikone**: Podržava široku paletu vrsta grafikona, uključujući svjećaste, radarske i površinske grafikone.
- **Jednostavnost uporabe**: Ima jednostavan API i lako se integrira u projekt.
- **Besplatan i otvorenog koda**: ApexCharts nudi besplatnu verziju otvorenog koda koja je prikladna za mnoge slučajeve uporabe.
  
**Slabosti**:
- **Složena prilagodba**: Iako pruža mnoge značajke, mogućnosti prilagodbe nisu tako fleksibilne kao kod ECharts ili D3.js za vrlo složene ili prilagođene potrebe grafikona.
- **Geo karte**: ApexCharts izvorno ne podržava geo karte ili grafikone procesa grupiranja, koji su potrebni za ovaj projekt.

**Presuda**:  
ApexCharts je snažan kandidat zbog jednostavnosti uporabe i interaktivnosti, ali zaostaje kod određenih naprednih vrsta grafikona, osobito potrebe za geo kartama i grafikonima grupiranja. Dobra je opcija za jednostavnije grafikone, ali nedostaju joj neke potrebne značajke.

---

### 4. **AG Charts**

**Pregled**:  
AG Charts je biblioteka grafikona komercijalne razine dizajnirana za performanse i preciznost. Vrlo je prikladna za izradu financijskih, znanstvenih i poslovnih nadzornih ploča.

**Snage**:
- **Napredne vrste grafikona**: AG Charts podržava mnoge napredne vrste grafikona, uključujući svjećaste, površinske, radarske i druge. Nudi i duboku integraciju s drugim AG-Grid proizvodima.
- **Visoke performanse**: Nudi izvrsne performanse, osobito pri radu s velikim skupovima podataka.
- **Interaktivnost**: AG Charts podržava razne interaktivne značajke poput zumiranja, opisa i dinamičkih ažuriranja.

**Slabosti**:
- **Nije potpuno besplatna**: Iako AG Charts nudi besplatnu verziju, verzija s punim značajkama je plaćena, što bi moglo biti prepreka startupima koji žele minimizirati troškove.
- **Složenost**: Iako je biblioteka bogata značajkama, može biti prekomjerna za jednostavnije projekte i može zahtijevati više postavljanja i konfiguracije u usporedbi s drugim opcijama.

**Presuda**:  
AG Charts je moćna i bogata značajkama, ali možda nije najbolji izbor zbog svoje komercijalne prirode i strukture troškova. Njezina prikladnost ovisi o tome može li proračun podnijeti plaćene verzije ili se preferiraju alternative otvorenog koda.

---

### 5. **Highcharts**

**Pregled**:  
Highcharts je popularna biblioteka grafikona poznata po širokom rasponu vrsta grafikona i moćnim opcijama prilagodbe.

**Snage**:
- **Sveobuhvatne vrste grafikona**: Highcharts podržava široku paletu grafikona, uključujući svjećaste, radarske, površinske i geo karte.
- **Interaktivan i dinamičan**: Highcharts pruža bogate interaktivne značajke, uključujući drill-down, zumiranje i pomicanje.
- **Jednostavnost uporabe**: Ima API prilagođen korisniku i dobru dokumentaciju, što olakšava početak.

**Slabosti**:
- **Komercijalna licenca**: Iako Highcharts nudi besplatnu verziju za nekomercijalnu uporabu, komercijalna licenca je skupa, što bi moglo biti značajan nedostatak za startupe.
- **Krivulja učenja**: Iako nije tako strma kao kod ECharts, krivulja učenja za Highcharts i dalje može biti izazovna za početnike.

**Presuda**:  
Highcharts je biblioteka bogata značajkama, ali njezino komercijalno licenciranje čini je manje prikladnom za projekte otvorenog koda osjetljive na troškove. Sveobuhvatne opcije grafikona su prednost, ali pitanje licenciranja ograničava njezinu privlačnost za ovaj slučaj uporabe.

---

### 6. **Carbon Charts**

**Pregled**:  
Carbon Charts je biblioteka grafikona koju je razvio IBM, dizajnirana za izradu vizualno privlačnih i vrlo prilagodljivih grafikona.

**Snage**:
- **Prilagodljivost**: Carbon Charts omogućuje opsežnu prilagodbu izgleda i ponašanja grafikona.
- **Otvorenog koda**: Besplatna je i otvorenog koda, što je u skladu sa zahtjevom projekta za proračunski prihvatljivim rješenjima.
- **Podrška za uobičajene grafikone**: Podržava uobičajene vrste grafikona poput doughnut, radarskih i površinskih grafikona, iako joj nedostaje podrška za naprednije vrste poput geo karata ili svjećastih grafikona.

**Slabosti**:
- **Ograničene napredne vrste grafikona**: Ne podržava geo karte, grafikone procesa grupiranja ni svjećaste grafikone, koji su ključni za projekt.
- **Manji ekosustav**: Carbon Charts ima manju zajednicu i ekosustav u usporedbi s većim bibliotekama grafikona poput ECharts ili Highcharts.

**Presuda**:  
Carbon Charts je otvorenog koda i prilagodljiva, ali joj nedostaje podrška za složenije vrste grafikona potrebne za ovaj projekt. Prikladnija je za jednostavnije potrebe grafikona.

---

### 7. **Layer Cake**

**Pregled**:  
Layer Cake je biblioteka za vizualizaciju podataka dizajnirana za izradu fleksibilnih, slojevitih vizualizacija.

**Snage**:
- **Prilagodljivi slojevi**: Pruža moćne opcije slojeva za složene vizualizacije.
- **Otvorenog koda**: Besplatna je i otvorenog koda, što je čini održivom opcijom za proračunski osviještene projekte.

**Slabosti**:
- **Ograničena dokumentacija**: Layer Cake nema opsežnu dokumentaciju i podršku zajednice, zbog čega je teže raditi s njom u usporedbi s etabliranijim bibliotekama.
- **Nije izgrađena za grafikone**: Layer Cake je prikladnija za vizualizacije koje nisu grafikoni, pa su njezine gotove opcije grafikona ograničene.

**Presuda**:  
Iako je zanimljiva za jedinstvene vizualizacije, Layer Cake nije idealna za tradicionalne zahtjeve grafikona poput svjećastih ili radarskih grafikona. Prikladnija je za prilagođene vizualizacije izvan opsega standardnih grafikona.

---

### 8. **D3.js**

**Pregled**:  
D3.js je moćna JavaScript biblioteka za izradu vizualizacija vođenih podacima putem HTML-a, SVG-a i CSS-a.

**Snage**:
- **Neusporediva fleksibilnost**: D3.js omogućuje izradu praktički bilo koje vrste prilagođene vizualizacije, što je čini vrlo moćnom za napredne i interaktivne grafikone.
- **Opsežne značajke**: Podržava sve potrebne vrste grafikona, uključujući geo karte, grafikone grupiranja i više.
- **Prilagodljiva**: Razina prilagodbe u D3.js je nenadmašna, omogućujući programerima izgradnju vrlo prilagođenih vizualizacija.

**Slabosti**:
- **Strma krivulja učenja**: D3.js ima strmu krivulju učenja i složenija je za integraciju u usporedbi s drugim bibliotekama.
- **Oduzima vrijeme**: Izrada grafikona u D3.js može oduzimati mnogo vremena, osobito za uobičajene grafikone poput svjećastih ili doughnut grafikona.

**Presuda**:  
D3.js je nevjerojatno moćan za napredne, prilagođene grafikone, ali je prekomjeran za mnoge tipične slučajeve uporabe zbog strme krivulje učenja i vremena razvoja. Najbolji je za situacije u kojima druge biblioteke grafikona ne pružaju potrebnu razinu prilagodbe.

---

### Zaključak

Nakon vrednovanja biblioteka na temelju potreba projekta **Apache ECharts** se ističe kao najbolja opcija. Podržava cijeli raspon potrebnih grafikona, uključujući geo karte, svjećaste grafikone i grafikone grupiranja. Otvorenog je koda, bogat značajkama i vrlo interaktivan, što se savršeno uklapa u ciljeve projekta. Iako **D3.js** nudi najveću fleksibilnost, njegova složenost i potrebno ulaganje vremena čine ga manje idealnim za startup koji želi brzo iterirati. **ApexCharts** i **Chart.js** dobre su alternative za jednostavnije projekte, ali nemaju podršku za napredne vrste grafikona.