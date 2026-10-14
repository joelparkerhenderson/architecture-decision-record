# Înregistrare a deciziei de arhitectură: bibliotecă de grafice pentru vizualizarea datelor cu TypeScript și JSON

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

**Obiectiv principal:**  
Selectarea unui set avansat de instrumente pentru grafice, destinat creării de vizualizări interactive, axat pe date financiare, date științifice și date guvernamentale, folosind TypeScript și JSON. Biblioteca ar trebui să ofere funcționalități robuste, flexibilitate și să fie open source. 

### Context și cerințe:

1. **Dezvoltare agilă (prioritate ridicată)**: Ca startup, iterarea rapidă, prototiparea și flexibilitatea în dezvoltare sunt esențiale. Biblioteca de grafice trebuie să permită cicluri de dezvoltare rapide.
   
2. **Tipuri de grafice (prioritate ridicată)**:
   - **Grafic inelar (doughnut)**
   - **Grafic radar**
   - **Grafic al procesului de clustering**
   - **Grafic de arie cu axă temporală**
   - **Grafic cu lumânări (candlestick)**
   - **Grafic Nightingale**
   - **Hartă geografică SVG**
   
   Aceste tipuri de grafice sunt deosebit de importante pentru vizualizarea seturilor de date complexe, precum tendințe financiare, metrici științifice și informații geografice.

3. **Gratuită și open source (prioritate ridicată)**: Setul de instrumente ar trebui să fie open source pentru a evita costurile de licențiere, a oferi transparență și a permite flexibilitate în personalizare.

4. **Criterii cu importanță redusă**:
   - **Viteza de execuție**: Deși performanța este importantă, nu este o prioritate de top pentru această decizie.
   - **Scalabilitate**: Deși scalabilitatea este în general importantă, nevoia imediată este construirea unui MVP care poate crește în timp. Aspectele de scalabilitate pot fi abordate mai târziu.
   - **Compatibilitate retroactivă**: Nu este o preocupare principală pentru construcția inițială, atâta timp cât biblioteca este modernă și întreținută activ.

### Biblioteci evaluate:

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

**Prezentare**:  
Apache ECharts este o bibliotecă de grafice puternică și flexibilă pentru vizualizări interactive și personalizabile. Suportă o mare varietate de grafice și este deosebit de puternică în vizualizări complexe și dinamice.

**Puncte forte**:
- **Interactivitate avansată**: ECharts excelează în oferirea de grafice interactive, cu funcții precum mărire, deplasare și actualizări dinamice ale datelor.
- **Inelar, radar, cu lumânări, hărți geografice SVG**: ECharts suportă multe dintre tipurile de grafice necesare, inclusiv vizualizări inelare, radar, cu lumânări și hărți geografice.
- **Gratuită și open source**: ECharts este o bibliotecă open source, ceea ce se potrivește caracterului economic al unui startup și oferă libertatea de a modifica codul.
- **Flexibilitate și extensibilitate**: Foarte personalizabilă, cu suport extins pentru animații, vizualizări personalizate și tehnici avansate de grafice.
  
**Puncte slabe**:
- **Curba de învățare**: ECharts, deși puternică, poate avea o curbă de învățare mai abruptă din cauza flexibilității și a API-ului extins.
- **Complexitatea documentației**: Documentația este cuprinzătoare, dar poate copleși dezvoltatorii care abia încep să o folosească.

**Verdict**:  
ECharts este foarte potrivită pentru proiect datorită suportului pentru grafice interactive, inclusiv toate tipurile necesare, precum graficele cu lumânări, graficele radar și hărțile geografice. Caracterul său open source se aliniază nevoii proiectului de flexibilitate și eficiență a costurilor.

---

### 2. **Chart.js**

**Prezentare**:  
Chart.js este o bibliotecă de grafice simplă și ușor de folosit pentru construirea tipurilor obișnuite de grafice. Este cunoscută pentru simplitate și ușurința integrării.

**Puncte forte**:
- **Ușurința în utilizare**: Chart.js este foarte simplu de configurat și de folosit, cu o curbă de învățare minimă.
- **Open source**: Chart.js este gratuită și open source, ceea ce este esențial pentru reducerea costurilor.
- **Tipuri obișnuite de grafice**: Suportă grafice de bază precum inelar, arie, radar și liniare, care acoperă majoritatea nevoilor principale.

**Puncte slabe**:
- **Grafice avansate limitate**: Chart.js nu suportă nativ tipuri complexe de grafice precum graficele cu lumânări, hărțile geografice SVG sau graficele procesului de clustering. Deși aceste funcții pot fi adăugate prin pluginuri sau personalizare, nu este la fel de simplu ca la alte biblioteci.
- **Interactivitate**: Deși Chart.js suportă interactivitate de bază (de exemplu, sfaturi de instrumente și efecte la trecerea cursorului), nu oferă funcții la fel de avansate ca ECharts sau D3.js.

**Verdict**:  
Chart.js este excelentă pentru proiecte simple și rapide, dar lipsa suportului pentru tipuri complexe de grafice o face nepotrivită pentru o aplicație intensivă în date, cu nevoi avansate precum graficele cu lumânări și hărțile geografice. Este o alegere bună pentru prototipare, dar pentru tipurile de grafice necesare se recomandă instrumente mai avansate.

---

### 3. **ApexCharts**

**Prezentare**:  
ApexCharts este o bibliotecă modernă de grafice care oferă o varietate de tipuri de grafice și se concentrează pe vizualizări interactive, cu un API ușor de folosit.

**Puncte forte**:
- **Funcții interactive**: ApexCharts oferă grafice interactive cu sfaturi de instrumente, mărire, deplasare și actualizări.
- **Suport pentru grafice financiare și științifice**: Suportă o mare varietate de tipuri de grafice, inclusiv grafice cu lumânări, radar și de arie.
- **Ușurința în utilizare**: Are un API direct și este simplu de integrat într-un proiect.
- **Gratuită și open source**: ApexCharts oferă o versiune open source gratuită, potrivită pentru multe cazuri de utilizare.
  
**Puncte slabe**:
- **Personalizare complexă**: Deși oferă multe funcții, opțiunile de personalizare nu sunt la fel de flexibile ca la ECharts sau D3.js pentru nevoi foarte complexe sau personalizate de grafice.
- **Hărți geografice**: ApexCharts nu suportă nativ hărți geografice sau grafice ale procesului de clustering, necesare pentru acest proiect.

**Verdict**:  
ApexCharts este un candidat puternic datorită ușurinței în utilizare și interactivității, dar nu satisface anumite tipuri avansate de grafice, în special nevoia de hărți geografice și grafice de clustering. Este o opțiune bună pentru grafice mai simple, dar îi lipsesc unele funcții necesare.

---

### 4. **AG Charts**

**Prezentare**:  
AG Charts este o bibliotecă de grafice de nivel comercial, concepută pentru performanță și precizie. Este foarte potrivită pentru crearea de tablouri de bord financiare, științifice și de business.

**Puncte forte**:
- **Tipuri avansate de grafice**: AG Charts suportă multe tipuri avansate de grafice, inclusiv grafice cu lumânări, de arie, radar și altele. Oferă, de asemenea, o integrare profundă cu alte produse AG-Grid.
- **Performanță ridicată**: Oferă performanță excelentă, mai ales la seturi mari de date.
- **Interactivitate**: AG Charts suportă o varietate de funcții interactive, precum mărirea, sfaturile de instrumente și actualizările dinamice.

**Puncte slabe**:
- **Nu este pe deplin gratuită**: Deși AG Charts oferă o versiune gratuită, versiunea cu toate funcțiile este cu plată, ceea ce poate fi o barieră pentru startup-urile care vor să minimizeze costurile.
- **Complexitate**: Deși biblioteca este bogată în funcții, poate fi exagerată pentru proiecte mai simple și poate necesita mai multă configurare decât alte opțiuni.

**Verdict**:  
AG Charts este puternică și bogată în funcții, dar poate să nu fie cea mai bună alegere din cauza naturii comerciale și a structurii de costuri. Potrivirea depinde de dacă bugetul permite versiuni cu plată sau se preferă alternative open source.

---

### 5. **Highcharts**

**Prezentare**:  
Highcharts este o bibliotecă de grafice populară, cunoscută pentru gama largă de tipuri de grafice și opțiunile puternice de personalizare.

**Puncte forte**:
- **Tipuri cuprinzătoare de grafice**: Highcharts suportă o mare varietate de grafice, inclusiv cu lumânări, radar, de arie și hărți geografice.
- **Interactivă și dinamică**: Highcharts oferă funcții interactive bogate, inclusiv drill-down, mărire și deplasare.
- **Ușurința în utilizare**: Are un API prietenos și documentație bună, ceea ce face ușor de început.

**Puncte slabe**:
- **Licență comercială**: Deși Highcharts oferă o versiune gratuită pentru utilizare necomercială, licența comercială este scumpă, ceea ce poate fi un dezavantaj semnificativ pentru startup-uri.
- **Curba de învățare**: Deși nu atât de abruptă ca la ECharts, curba de învățare pentru Highcharts poate fi totuși dificilă pentru începători.

**Verdict**:  
Highcharts este o bibliotecă bogată în funcții, dar licențierea comercială o face mai puțin potrivită pentru proiecte open source sensibile la costuri. Opțiunile cuprinzătoare de grafice sunt un plus, dar problema licențierii îi limitează atractivitatea pentru acest caz de utilizare.

---

### 6. **Carbon Charts**

**Prezentare**:  
Carbon Charts este o bibliotecă de grafice dezvoltată de IBM, concepută pentru crearea de grafice atractive vizual și foarte personalizabile.

**Puncte forte**:
- **Personalizabilitate**: Carbon Charts permite personalizarea extinsă a aspectului și comportamentului graficelor.
- **Open source**: Este gratuită și open source, ceea ce se aliniază cerinței proiectului de soluții prietenoase cu bugetul.
- **Suport pentru grafice obișnuite**: Suportă tipuri obișnuite de grafice precum inelar, radar și de arie, deși nu suportă tipuri mai avansate precum hărțile geografice sau graficele cu lumânări.

**Puncte slabe**:
- **Tipuri avansate de grafice limitate**: Nu suportă hărți geografice, grafice ale procesului de clustering sau grafice cu lumânări, esențiale pentru proiect.
- **Ecosistem mai mic**: Carbon Charts are o comunitate și un ecosistem mai mici în comparație cu bibliotecile de grafice mai mari, precum ECharts sau Highcharts.

**Verdict**:  
Carbon Charts este open source și personalizabilă, dar îi lipsește suportul pentru tipurile mai complexe de grafice necesare acestui proiect. Este mai potrivită pentru nevoi mai simple de grafice.

---

### 7. **Layer Cake**

**Prezentare**:  
Layer Cake este o bibliotecă de vizualizare a datelor concepută pentru crearea de vizualizări flexibile, pe straturi.

**Puncte forte**:
- **Straturi personalizabile**: Oferă opțiuni puternice de stratificare pentru vizualizări complexe.
- **Open source**: Este gratuită și open source, ceea ce o face o opțiune viabilă pentru proiecte sensibile la buget.

**Puncte slabe**:
- **Documentație limitată**: Layer Cake nu are documentație extinsă și suport comunitar, ceea ce face mai dificilă lucrul cu ea în comparație cu bibliotecile mai consacrate.
- **Nu este construită pentru grafice**: Layer Cake este mai potrivită pentru vizualizări care nu sunt grafice, deci opțiunile sale de grafice gata de folosit sunt limitate.

**Verdict**:  
Deși interesantă pentru vizualizări unice, Layer Cake nu este ideală pentru cerințele tradiționale de grafice, precum graficele cu lumânări sau cele radar. Este mai potrivită pentru vizualizări personalizate în afara domeniului graficelor standard.

---

### 8. **D3.js**

**Prezentare**:  
D3.js este o bibliotecă JavaScript puternică pentru crearea de vizualizări bazate pe date prin HTML, SVG și CSS.

**Puncte forte**:
- **Flexibilitate fără egal**: D3.js permite crearea practic a oricărui tip de vizualizare personalizată, ceea ce o face foarte puternică pentru grafice avansate și interactive.
- **Funcții extinse**: Suportă toate tipurile de grafice necesare, inclusiv hărți geografice, grafice de clustering și altele.
- **Personalizabilă**: Nivelul de personalizare din D3.js este de neegalat, permițând dezvoltatorilor să construiască vizualizări extrem de adaptate.

**Puncte slabe**:
- **Curbă de învățare abruptă**: D3.js are o curbă de învățare abruptă și este mai complexă de integrat în comparație cu alte biblioteci.
- **Consumatoare de timp**: Construirea graficelor în D3.js poate consuma mult timp, mai ales pentru grafice obișnuite precum cele cu lumânări sau inelare.

**Verdict**:  
D3.js este incredibil de puternică pentru grafice avansate și personalizate, dar este exagerată pentru multe cazuri de utilizare tipice din cauza curbei de învățare abrupte și a timpului de dezvoltare. Este cel mai bună în situațiile în care celelalte biblioteci de grafice nu oferă nivelul necesar de personalizare.

---

### Concluzie

După evaluarea bibliotecilor în funcție de nevoile proiectului, **Apache ECharts** se remarcă drept cea mai bună opțiune. Suportă gama completă de grafice necesare, inclusiv hărți geografice, grafice cu lumânări și grafice de clustering. Este open source, bogată în funcții și foarte interactivă, ceea ce se aliniază perfect obiectivelor proiectului. Deși **D3.js** oferă cea mai mare flexibilitate, complexitatea și investiția de timp o fac mai puțin ideală pentru un startup care vrea să itereze rapid. **ApexCharts** și **Chart.js** sunt alternative bune pentru proiecte mai simple, dar le lipsește suportul pentru tipurile avansate de grafice.
