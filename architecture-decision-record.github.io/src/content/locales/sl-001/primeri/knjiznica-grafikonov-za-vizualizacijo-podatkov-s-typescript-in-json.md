# Zapis arhitekturne odločitve: knjižnica grafikonov za vizualizacijo podatkov s TypeScript in JSON

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
Izbrati napredno zbirko orodij za grafikone za ustvarjanje interaktivnih vizualizacij, s poudarkom na finančnih podatkih, znanstvenih podatkih in vladnih podatkih, z uporabo TypeScript in JSON. Knjižnica naj zagotavlja robustne funkcije, prilagodljivost in bo odprtokodna. 

### Kontekst in zahteve:

1. **Agilen razvoj (visoka prednost)**: Kot zagonsko podjetje so hitra iteracija, izdelava prototipov in prilagodljivost pri razvoju bistvene. Knjižnica grafikonov mora omogočati hitre razvojne cikle.
   
2. **Vrste grafikonov (visoka prednost)**:
   - **Kolobarni grafikon (doughnut)**
   - **Radarski grafikon**
   - **Grafikon procesa razvrščanja (clustering)**
   - **Ploskovni grafikon s časovno osjo**
   - **Svečni grafikon (candlestick)**
   - **Nightingalov grafikon**
   - **Geografski zemljevid SVG**
   
   Te vrste grafikonov so posebej pomembne za vizualizacijo zapletenih naborov podatkov, kot so finančni trendi, znanstvene metrike in geografske informacije.

3. **Brezplačno in odprtokodno (visoka prednost)**: Zbirka orodij naj bo odprtokodna, da se izognemo stroškom licenc, zagotovimo preglednost in ponudimo prilagodljivost za prilagajanje.

4. **Merila nizke pomembnosti**:
   - **Hitrost izvajanja**: Čeprav je zmogljivost pomembna, za to odločitev ni najpomembnejša.
   - **Razširljivost**: Čeprav je razširljivost na splošno pomembna, je neposredna potreba izgradnja MVP, ki bo sčasoma morda rasel. Skrbi glede razširljivosti je mogoče obravnavati pozneje.
   - **Združljivost za nazaj**: Ni primarna skrb za začetno gradnjo, dokler je knjižnica sodobna in dejavno vzdrževana.

### Ovrednotene knjižnice:

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
Apache ECharts je zmogljiva, prilagodljiva knjižnica grafikonov za interaktivne, prilagodljive vizualizacije. Podpira široko paleto grafikonov in je še posebej močna pri zapletenih, dinamičnih vizualizacijah.

**Prednosti**:
- **Napredna interaktivnost**: ECharts je odličen pri zagotavljanju interaktivnih grafikonov in ponuja funkcije, kot so povečava, premikanje in dinamične posodobitve podatkov.
- **Kolobarni, radarski, svečni grafikoni, geografski zemljevidi SVG**: ECharts podpira mnoge zahtevane vrste grafikonov, vključno s kolobarnimi, radarskimi, svečnimi grafikoni in vizualizacijami geografskih zemljevidov.
- **Brezplačno in odprtokodno**: ECharts je odprtokodna knjižnica, ki ustreza proračunsko ozaveščeni naravi zagonskega podjetja in zagotavlja svobodo spreminjanja kode.
- **Prilagodljivost in razširljivost z razširitvami**: Zelo prilagodljiva, z obsežno podporo za animacije, vizualizacije po meri in napredne tehnike grafikonov.
  
**Slabosti**:
- **Krivulja učenja**: ECharts je kljub zmogljivosti lahko zaradi svoje prilagodljivosti in obsežnega API strmejši za učenje.
- **Kompleksnost dokumentacije**: Dokumentacija je obsežna, vendar je lahko za razvijalce, ki šele začenjajo, preobsežna.

**Ocena**:  
ECharts je zelo primeren za projekt zaradi podpore za interaktivne grafikone, vključno z vsemi zahtevanimi vrstami, kot so svečni grafikoni, radarski grafikoni in geografski zemljevidi. Njegova odprtokodna narava se ujema s projektovo potrebo po prilagodljivosti in stroškovni učinkovitosti.

---

### 2. **Chart.js**

**Pregled**:  
Chart.js je preprosta, enostavna za uporabo knjižnica grafikonov za gradnjo običajnih vrst grafikonov. Znana je po svoji preprostosti in enostavni integraciji.

**Prednosti**:
- **Enostavnost uporabe**: Chart.js je zelo preprost za nastavitev in uporabo, z minimalno krivuljo učenja.
- **Odprtokodno**: Chart.js je brezplačen in odprtokoden, kar je ključno za zmanjšanje stroškov.
- **Običajne vrste grafikonov**: Podpira osnovne grafikone, kot so kolobarni, ploskovni, radarski in črtni grafikoni, ki pokrivajo večino primarnih potreb.

**Slabosti**:
- **Omejeni napredni grafikoni**: Chart.js izvorno ne podpira zapletenih vrst grafikonov, kot so svečni grafikoni, geografski zemljevidi SVG ali grafikoni procesa razvrščanja. Čeprav je te funkcije mogoče dodati z vtičniki ali prilagoditvijo, to ni tako preprosto kot pri drugih knjižnicah.
- **Interaktivnost**: Čeprav Chart.js podpira osnovno interaktivnost (npr. namige in učinke ob prehodu miške), ne ponuja tako naprednih funkcij kot ECharts ali D3.js.

**Ocena**:  
Chart.js je odličen za preproste, hitre projekte, vendar ga pomanjkanje podpore za zapletene vrste grafikonov dela neprimernega za aplikacijo z veliko podatki in naprednimi potrebami, kot so svečni grafikoni in geografski zemljevidi. Je dobra izbira za izdelavo prototipov, a za zahtevane vrste grafikonov so priporočena naprednejša orodja.

---

### 3. **ApexCharts**

**Pregled**:  
ApexCharts je sodobna knjižnica grafikonov, ki ponuja različne vrste grafikonov in se osredotoča na interaktivne vizualizacije z enostavnim API.

**Prednosti**:
- **Interaktivne funkcije**: ApexCharts ponuja interaktivne grafikone z namigi, povečavo, premikanjem in posodobitvami.
- **Podpora za finančne in znanstvene grafikone**: Podpira široko paleto vrst grafikonov, vključno s svečnimi, radarskimi in ploskovnimi grafikoni.
- **Enostavnost uporabe**: Ima preprost API in jo je enostavno vključiti v projekt.
- **Brezplačno in odprtokodno**: ApexCharts ponuja brezplačno odprtokodno različico, primerno za mnoge primere uporabe.
  
**Slabosti**:
- **Zapleteno prilagajanje**: Čeprav ponuja mnoge funkcije, možnosti prilagajanja niso tako prilagodljive kot pri ECharts ali D3.js za zelo zapletene ali prilagojene potrebe po grafikonih.
- **Geografski zemljevidi**: ApexCharts izvorno ne podpira geografskih zemljevidov ali grafikonov procesa razvrščanja, ki so za ta projekt zahtevani.

**Ocena**:  
ApexCharts je resen kandidat zaradi enostavnosti uporabe in interaktivnosti, vendar zaostaja pri nekaterih naprednih vrstah grafikonov, zlasti pri potrebi po geografskih zemljevidih in grafikonih razvrščanja. Je dobra možnost za preprostejše grafikone, vendar nima nekaterih zahtevanih funkcij.

---

### 4. **AG Charts**

**Pregled**:  
AG Charts je knjižnica grafikonov komercialne kakovosti, zasnovana za zmogljivost in natančnost. Zelo je primerna za ustvarjanje finančnih, znanstvenih in poslovnih nadzornih plošč.

**Prednosti**:
- **Napredne vrste grafikonov**: AG Charts podpira številne napredne vrste grafikonov, vključno s svečnimi, ploskovnimi, radarskimi grafikoni in drugimi. Ponuja tudi globoko integracijo z drugimi izdelki AG-Grid.
- **Visoka zmogljivost**: Ponuja odlično zmogljivost, zlasti pri delu z velikimi nabori podatkov.
- **Interaktivnost**: AG Charts podpira različne interaktivne funkcije, kot so povečava, namigi in dinamične posodobitve.

**Slabosti**:
- **Ni povsem brezplačno**: Čeprav AG Charts ponuja brezplačno različico, je različica s polnimi funkcijami plačljiva, kar je lahko ovira za zagonska podjetja, ki želijo zmanjšati stroške.
- **Kompleksnost**: Čeprav je knjižnica bogata s funkcijami, je lahko za preprostejše projekte pretirana in lahko zahteva več nastavitev in konfiguracije v primerjavi z drugimi možnostmi.

**Ocena**:  
AG Charts je zmogljiva in bogata s funkcijami, vendar morda zaradi svoje komercialne narave in cenovne strukture ni najboljša izbira. Njena primernost je odvisna od tega, ali proračun omogoča plačljive različice ali so prednostne odprtokodne alternative.

---

### 5. **Highcharts**

**Pregled**:  
Highcharts je priljubljena knjižnica grafikonov, znana po široki paleti vrst grafikonov in zmogljivih možnostih prilagajanja.

**Prednosti**:
- **Celovite vrste grafikonov**: Highcharts podpira široko paleto grafikonov, vključno s svečnimi, radarskimi, ploskovnimi grafikoni in geografskimi zemljevidi.
- **Interaktivno in dinamično**: Highcharts zagotavlja bogate interaktivne funkcije, vključno s poglabljanjem (drill-down), povečavo in premikanjem.
- **Enostavnost uporabe**: Ima uporabniku prijazen API in dobro dokumentacijo, zato je enostavno začeti.

**Slabosti**:
- **Komercialna licenca**: Čeprav Highcharts ponuja brezplačno različico za nekomercialno uporabo, je komercialna licenca draga, kar je lahko pomembna pomanjkljivost za zagonska podjetja.
- **Krivulja učenja**: Čeprav ni tako strma kot pri ECharts, je krivulja učenja za Highcharts za začetnike še vedno lahko zahtevna.

**Ocena**:  
Highcharts je knjižnica, bogata s funkcijami, vendar jo komercialno licenciranje dela manj primerno za odprtokodne, stroškovno občutljive projekte. Njene celovite možnosti grafikonov so prednost, vendar težava z licenciranjem omejuje njeno privlačnost za ta primer uporabe.

---

### 6. **Carbon Charts**

**Pregled**:  
Carbon Charts je knjižnica grafikonov, ki jo je razvil IBM, zasnovana za ustvarjanje vizualno privlačnih in zelo prilagodljivih grafikonov.

**Prednosti**:
- **Prilagodljivost**: Carbon Charts omogoča obsežno prilagajanje videza in obnašanja grafikonov.
- **Odprtokodno**: Brezplačna je in odprtokodna, kar se ujema z zahtevo projekta po proračunsko ugodnih rešitvah.
- **Podpora za običajne grafikone**: Podpira običajne vrste grafikonov, kot so kolobarni, radarski in ploskovni grafikoni, vendar nima podpore za naprednejše vrste, kot so geografski zemljevidi ali svečni grafikoni.

**Slabosti**:
- **Omejene napredne vrste grafikonov**: Ne podpira geografskih zemljevidov, grafikonov procesa razvrščanja ali svečnih grafikonov, ki so za projekt bistveni.
- **Manjši ekosistem**: Carbon Charts ima manjšo skupnost in ekosistem v primerjavi z večjimi knjižnicami grafikonov, kot sta ECharts ali Highcharts.

**Ocena**:  
Carbon Charts je odprtokoden in prilagodljiv, vendar nima podpore za zapletenejše vrste grafikonov, ki jih ta projekt potrebuje. Primernejši je za preprostejše potrebe po grafikonih.

---

### 7. **Layer Cake**

**Pregled**:  
Layer Cake je knjižnica za vizualizacijo podatkov, zasnovana za ustvarjanje prilagodljivih, plastnih vizualizacij.

**Prednosti**:
- **Prilagodljive plasti**: Zagotavlja zmogljive možnosti plastenja za zapletene vizualizacije.
- **Odprtokodno**: Brezplačna je in odprtokodna, zaradi česar je izvedljiva možnost za proračunsko ozaveščene projekte.

**Slabosti**:
- **Omejena dokumentacija**: Layer Cake nima obsežne dokumentacije in podpore skupnosti, zaradi česar je delo z njo težje v primerjavi z bolj uveljavljenimi knjižnicami.
- **Ni zgrajena za grafikone**: Layer Cake je bolj primerna za vizualizacije, ki niso grafikoni, zato so njene takojšnje možnosti grafikonov omejene.

**Ocena**:  
Čeprav je Layer Cake zanimiva za edinstvene vizualizacije, ni idealna za tradicionalne zahteve po grafikonih, kot so svečni ali radarski grafikoni. Bolj je primerna za vizualizacije po meri zunaj obsega standardnih grafikonov.

---

### 8. **D3.js**

**Pregled**:  
D3.js je zmogljiva JavaScriptna knjižnica za ustvarjanje vizualizacij, vodenih s podatki, prek HTML, SVG in CSS.

**Prednosti**:
- **Neprekosljiva prilagodljivost**: D3.js omogoča ustvarjanje praktično vsake vrste vizualizacije po meri, zaradi česar je zelo zmogljiv za napredne in interaktivne grafikone.
- **Obsežne funkcije**: Podpira vse zahtevane vrste grafikonov, vključno z geografskimi zemljevidi, grafikoni razvrščanja in drugimi.
- **Prilagodljivo**: Raven prilagajanja v D3.js je neprimerljiva in razvijalcem omogoča gradnjo zelo prilagojenih vizualizacij.

**Slabosti**:
- **Strma krivulja učenja**: D3.js ima strmo krivuljo učenja in je v primerjavi z drugimi knjižnicami zahtevnejši za integracijo.
- **Časovno potratno**: Gradnja grafikonov v D3.js je lahko časovno potratna, zlasti za običajne grafikone, kot so svečni ali kolobarni grafikoni.

**Ocena**:  
D3.js je neverjetno zmogljiv za napredne, prilagojene grafikone, vendar je za mnoge tipične primere uporabe pretiran zaradi strme krivulje učenja in razvojnega časa. Najboljši je v primerih, ko druge knjižnice grafikonov ne zagotavljajo zahtevane ravni prilagajanja.

---

### Sklep

Po vrednotenju knjižnic glede na potrebe projekta se kot najboljša možnost izkaže **Apache ECharts**. Podpira celoten nabor zahtevanih grafikonov, vključno z geografskimi zemljevidi, svečnimi grafikoni in grafikoni razvrščanja. Je odprtokoden, bogat s funkcijami in zelo interaktiven, kar se popolnoma ujema s cilji projekta. Čeprav **D3.js** ponuja največ prilagodljivosti, ga kompleksnost in časovna naložba delata manj idealnega za zagonsko podjetje, ki želi hitro iterirati. **ApexCharts** in **Chart.js** sta dobri alternativi za preprostejše projekte, vendar nimata podpore za napredne vrste grafikonov.
