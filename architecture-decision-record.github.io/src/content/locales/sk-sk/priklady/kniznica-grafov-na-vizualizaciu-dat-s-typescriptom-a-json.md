# Záznam architektonického rozhodnutia: knižnica grafov na vizualizáciu dát s TypeScriptom a JSON

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

**Primárny cieľ:**  
Vybrať pokročilú sadu nástrojov pre grafy na tvorbu interaktívnych vizualizácií so zameraním na finančné, vedecké a vládne dáta pomocou TypeScriptu a JSON. Knižnica by mala poskytovať robustné funkcie, flexibilitu a byť open source. 

### Kontext a požiadavky:

1. **Agilný vývoj (vysoká priorita)**: Ako startup je nevyhnutná rýchla iterácia, prototypovanie a flexibilita vo vývoji. Knižnica grafov musí umožňovať rýchle vývojové cykly.
   
2. **Typy grafov (vysoká priorita)**:
   - **Prstencový graf (Doughnut Chart)**
   - **Radarový graf (Radar Chart)**
   - **Graf procesu zhlukovania (Clustering Process Chart)**
   - **Plošný graf s časovou osou (Area Chart with Time Axis)**
   - **Sviečkový graf (Candlestick Chart)**
   - **Nightingaleov graf (Nightingale Chart)**
   - **Geo SVG mapa (Geo SVG Map)**
   
   Tieto typy grafov sú obzvlášť dôležité pre vizualizáciu zložitých súborov dát, ako sú finančné trendy, vedecké metriky a geografické informácie.

3. **Zadarmo a open source (vysoká priorita)**: Sada nástrojov by mala byť open source, aby sa predišlo licenčným nákladom, zabezpečila transparentnosť a ponúkla flexibilitu prispôsobenia.

4. **Kritériá nízkej dôležitosti**:
   - **Rýchlosť behu**: Hoci je výkon dôležitý, nie je pre toto rozhodnutie najvyššou prioritou.
   - **Škálovateľnosť**: Hoci je škálovateľnosť vo všeobecnosti dôležitá, bezprostrednou potrebou je vybudovať MVP, ktoré môže časom rásť. Otázky škálovateľnosti možno riešiť neskôr.
   - **Spätná kompatibilita**: Nie je primárnou starosťou pri počiatočnom budovaní, pokiaľ je knižnica moderná a aktívne udržiavaná.

### Hodnotené knižnice:

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

**Prehľad**:  
Apache ECharts je výkonná, flexibilná knižnica grafov pre interaktívne, prispôsobiteľné vizualizácie. Poskytuje podporu širokej škály grafov a je obzvlášť silná v zložitých, dynamických vizualizáciách.

**Silné stránky**:
- **Pokročilá interaktivita**: ECharts vyniká v poskytovaní interaktívnych grafov a ponúka funkcie ako priblíženie, posúvanie a dynamické aktualizácie dát.
- **Prstencové, radarové, sviečkové grafy, Geo SVG mapy**: ECharts podporuje mnohé z požadovaných typov grafov vrátane prstencových, radarových, sviečkových a vizualizácií geografických máp.
- **Zadarmo a open source**: ECharts je knižnica s otvoreným zdrojovým kódom, čo zodpovedá rozpočtovo uvedomelej povahe startupu a poskytuje slobodu upravovať kód.
- **Flexibilita a rozšíriteľnosť**: Vysoko prispôsobiteľná s rozsiahlou podporou animácií, vlastných vizualizácií a pokročilých techník tvorby grafov.
  
**Slabé stránky**:
- **Krivka učenia**: ECharts, hoci je výkonný, môže mať strmšiu krivku učenia kvôli svojej flexibilite a rozsiahlemu API.
- **Zložitosť dokumentácie**: Dokumentácia je komplexná, ale môže byť zahlcujúca pre vývojárov, ktorí s ňou len začínajú.

**Verdikt**:  
ECharts je pre projekt veľmi vhodný vďaka podpore interaktívnych grafov vrátane všetkých požadovaných typov, ako sú sviečkové grafy, radarové grafy a geo mapy. Jeho open source povaha zodpovedá potrebe projektu flexibility a nákladovej efektívnosti.

---

### 2. **Chart.js**

**Prehľad**:  
Chart.js je jednoduchá, ľahko použiteľná knižnica grafov na tvorbu bežných typov grafov. Je známa svojou jednoduchosťou a ľahkou integráciou.

**Silné stránky**:
- **Jednoduchosť používania**: Chart.js sa veľmi jednoducho nastavuje a používa, s minimálnou krivkou učenia.
- **Open source**: Chart.js je zadarmo a open source, čo je kľúčové na zníženie nákladov.
- **Bežné typy grafov**: Podporuje základné grafy ako prstencové, plošné, radarové a čiarové, ktoré pokrývajú väčšinu primárnych potrieb.

**Slabé stránky**:
- **Obmedzené pokročilé grafy**: Chart.js natívne nepodporuje zložité typy grafov ako sviečkové grafy, geo SVG mapy alebo grafy procesu zhlukovania. Hoci tieto funkcie možno pridať pomocou doplnkov alebo prispôsobenia, nie je to také priamočiare ako pri iných knižniciach.
- **Interaktivita**: Hoci Chart.js podporuje základnú interaktivitu (napr. popisky a efekty pri prechode myšou), neponúka také pokročilé funkcie ako ECharts alebo D3.js.

**Verdikt**:  
Chart.js je skvelý pre jednoduché, rýchle projekty, ale nedostatok podpory zložitých typov grafov ho robí nevhodným pre aplikáciu s veľkým množstvom dát a pokročilými potrebami, ako sú sviečkové grafy a geo mapy. Je dobrou voľbou na prototypovanie, ale pre požadované typy grafov sa odporúčajú pokročilejšie nástroje.

---

### 3. **ApexCharts**

**Prehľad**:  
ApexCharts je moderná knižnica grafov, ktorá poskytuje rôzne typy grafov a zameriava sa na interaktívne vizualizácie s ľahko použiteľným API.

**Silné stránky**:
- **Interaktívne funkcie**: ApexCharts ponúka interaktívne grafy s popiskami, priblížením, posúvaním a aktualizáciami.
- **Podpora finančných a vedeckých grafov**: Podporuje širokú škálu typov grafov vrátane sviečkových, radarových a plošných grafov.
- **Jednoduchosť používania**: Má priamočiare API a ľahko sa integruje do projektu.
- **Zadarmo a open source**: ApexCharts ponúka bezplatnú open source verziu, ktorá je vhodná pre mnohé prípady použitia.
  
**Slabé stránky**:
- **Zložité prispôsobenie**: Hoci poskytuje mnoho funkcií, možnosti prispôsobenia nie sú také flexibilné ako pri ECharts alebo D3.js pre veľmi zložité alebo vlastné potreby grafov.
- **Geo mapy**: ApexCharts natívne nepodporuje geo mapy ani grafy procesu zhlukovania, ktoré sú pre tento projekt potrebné.

**Verdikt**:  
ApexCharts je silný kandidát vďaka jednoduchosti používania a interaktivite, ale nedostáva sa k určitým pokročilým typom grafov, najmä k potrebe geo máp a grafov zhlukovania. Je dobrou možnosťou pre jednoduchšie grafy, ale chýbajú mu niektoré požadované funkcie.

---

### 4. **AG Charts**

**Prehľad**:  
AG Charts je knižnica grafov komerčnej triedy navrhnutá pre výkon a presnosť. Je veľmi vhodná na tvorbu finančných, vedeckých a obchodných dashboardov.

**Silné stránky**:
- **Pokročilé typy grafov**: AG Charts podporuje mnohé pokročilé typy grafov vrátane sviečkových grafov, plošných grafov, radarových grafov a ďalších. Ponúka aj hlbokú integráciu s ďalšími produktmi AG-Grid.
- **Vysoký výkon**: Ponúka vynikajúci výkon, najmä pri práci s veľkými súbormi dát.
- **Interaktivita**: AG Charts podporuje rôzne interaktívne funkcie ako priblíženie, popisky a dynamické aktualizácie.

**Slabé stránky**:
- **Nie je úplne zadarmo**: Hoci AG Charts ponúka bezplatnú verziu, verzia s plnými funkciami je platená, čo by mohlo byť prekážkou pre startupy, ktoré chcú minimalizovať náklady.
- **Zložitosť**: Hoci je knižnica bohatá na funkcie, môže byť pre jednoduchšie projekty zbytočne rozsiahla a v porovnaní s inými možnosťami môže vyžadovať viac nastavovania a konfigurácie.

**Verdikt**:  
AG Charts je výkonná a bohatá na funkcie, ale nemusí byť najlepšou voľbou kvôli svojej komerčnej povahe a nákladovej štruktúre. Jej vhodnosť závisí od toho, či rozpočet pokryje platené verzie alebo sa uprednostňujú open source alternatívy.

---

### 5. **Highcharts**

**Prehľad**:  
Highcharts je populárna knižnica grafov známa širokou škálou typov grafov a výkonnými možnosťami prispôsobenia.

**Silné stránky**:
- **Komplexné typy grafov**: Highcharts podporuje širokú škálu grafov vrátane sviečkových, radarových, plošných a geo máp.
- **Interaktívne a dynamické**: Highcharts poskytuje bohaté interaktívne funkcie vrátane drill-down, priblíženia a posúvania.
- **Jednoduchosť používania**: Má používateľsky prívetivé API a dobrú dokumentáciu, vďaka čomu sa ľahko začína.

**Slabé stránky**:
- **Komerčná licencia**: Hoci Highcharts ponúka bezplatnú verziu pre nekomerčné použitie, komerčná licencia je drahá, čo by mohlo byť pre startupy významnou nevýhodou.
- **Krivka učenia**: Hoci nie je taká strmá ako pri ECharts, krivka učenia pre Highcharts môže byť pre začiatočníkov stále náročná.

**Verdikt**:  
Highcharts je knižnica bohatá na funkcie, ale jej komerčné licencovanie ju robí menej vhodnou pre open source projekty citlivé na náklady. Jej komplexné možnosti grafov sú plusom, ale otázka licencovania obmedzuje jej príťažlivosť pre tento prípad použitia.

---

### 6. **Carbon Charts**

**Prehľad**:  
Carbon Charts je knižnica grafov vyvinutá spoločnosťou IBM, navrhnutá na tvorbu vizuálne príťažlivých a vysoko prispôsobiteľných grafov.

**Silné stránky**:
- **Prispôsobiteľnosť**: Carbon Charts umožňuje rozsiahle prispôsobenie vzhľadu a správania grafov.
- **Open source**: Je zadarmo a open source, čo zodpovedá požiadavke projektu na rozpočtovo priaznivé riešenia.
- **Podpora bežných grafov**: Podporuje bežné typy grafov ako prstencové, radarové a plošné grafy, hoci jej chýba podpora pokročilejších typov ako geo mapy alebo sviečkové grafy.

**Slabé stránky**:
- **Obmedzené pokročilé typy grafov**: Nepodporuje geo mapy, grafy procesu zhlukovania ani sviečkové grafy, ktoré sú pre projekt nevyhnutné.
- **Menší ekosystém**: Carbon Charts má menšiu komunitu a ekosystém v porovnaní s väčšími knižnicami grafov ako ECharts alebo Highcharts.

**Verdikt**:  
Carbon Charts je open source a prispôsobiteľná, ale chýba jej podpora zložitejších typov grafov potrebných pre tento projekt. Je vhodnejšia pre jednoduchšie potreby grafov.

---

### 7. **Layer Cake**

**Prehľad**:  
Layer Cake je knižnica na vizualizáciu dát navrhnutá na tvorbu flexibilných, vrstvených vizualizácií.

**Silné stránky**:
- **Prispôsobiteľné vrstvy**: Poskytuje výkonné možnosti vrstvenia pre zložité vizualizácie.
- **Open source**: Je zadarmo a open source, čo ju robí životaschopnou možnosťou pre rozpočtovo uvedomelé projekty.

**Slabé stránky**:
- **Obmedzená dokumentácia**: Layer Cake chýba rozsiahla dokumentácia a podpora komunity, vďaka čomu sa s ňou pracuje ťažšie než s etablovanejšími knižnicami.
- **Nie je vytvorená pre grafy**: Layer Cake je vhodnejšia pre vizualizácie, ktoré nie sú grafmi, takže jej hotové možnosti grafov sú obmedzené.

**Verdikt**:  
Hoci je zaujímavá pre jedinečné vizualizácie, Layer Cake nie je ideálna pre tradičné požiadavky na grafy, ako sú sviečkové alebo radarové grafy. Je vhodnejšia pre vlastné vizualizácie mimo rozsahu štandardných grafov.

---

### 8. **D3.js**

**Prehľad**:  
D3.js je výkonná JavaScriptová knižnica na tvorbu vizualizácií riadených dátami cez HTML, SVG a CSS.

**Silné stránky**:
- **Bezkonkurenčná flexibilita**: D3.js umožňuje vytvárať prakticky akýkoľvek typ vlastnej vizualizácie, čo ju robí veľmi výkonnou pre pokročilé a interaktívne grafy.
- **Rozsiahle funkcie**: Podporuje všetky požadované typy grafov vrátane geo máp, grafov zhlukovania a ďalších.
- **Prispôsobiteľnosť**: Úroveň prispôsobenia v D3.js je nepredstihnuteľná a umožňuje vývojárom budovať vysoko prispôsobené vizualizácie.

**Slabé stránky**:
- **Strmá krivka učenia**: D3.js má strmú krivku učenia a v porovnaní s inými knižnicami sa zložitejšie integruje.
- **Časovo náročná**: Budovanie grafov v D3.js môže byť časovo náročné, najmä pri bežných grafoch ako sviečkové alebo prstencové.

**Verdikt**:  
D3.js je neuveriteľne výkonná pre pokročilé, vlastné grafy, ale je zbytočne rozsiahla pre mnohé typické prípady použitia kvôli strmej krivke učenia a času vývoja. Najlepšia je v situáciách, keď iné knižnice grafov neposkytujú požadovanú úroveň prispôsobenia.

---

### Záver

Po vyhodnotení knižníc na základe potrieb projektu sa ako najlepšia možnosť javí **Apache ECharts**. Podporuje celú škálu požadovaných grafov vrátane geo máp, sviečkových grafov a grafov zhlukovania. Je open source, bohatá na funkcie a vysoko interaktívna, čo dokonale zodpovedá cieľom projektu. Hoci **D3.js** ponúka najväčšiu flexibilitu, jej zložitosť a časová investícia ju robia menej ideálnou pre startup, ktorý chce rýchlo iterovať. **ApexCharts** a **Chart.js** sú dobré alternatívy pre jednoduchšie projekty, ale chýba im podpora pokročilých typov grafov.