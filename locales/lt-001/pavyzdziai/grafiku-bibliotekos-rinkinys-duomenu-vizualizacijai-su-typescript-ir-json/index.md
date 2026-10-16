# Architektūros sprendimo įrašas: grafikų bibliotekos rinkinys duomenų vizualizacijai naudojant TypeScript ir JSON

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

**Pagrindinis tikslas:**  
Pasirinkti pažangų grafikų rinkinį interaktyvioms vizualizacijoms kurti, sutelkiant dėmesį į finansinius duomenis, mokslinius duomenis ir vyriausybės duomenis naudojant TypeScript ir JSON. Biblioteka turėtų suteikti tvirtas funkcijas, lankstumą ir būti atvirojo kodo. 

### Kontekstas ir reikalavimai:

1. **Lankstusis kūrimas (aukštas prioritetas)**: kaip startuoliui, būtina greita iteracija, prototipų kūrimas ir kūrimo lankstumas. Grafikų biblioteka turi leisti greitus kūrimo ciklus.
   
2. **Grafikų tipai (aukštas prioritetas)**:
   - **Žiedinė diagrama (Doughnut)**
   - **Radaro diagrama (Radar)**
   - **Klasterizavimo proceso diagrama (Clustering Process)**
   - **Ploto diagrama su laiko ašimi**
   - **Žvakių diagrama (Candlestick)**
   - **Nightingale diagrama**
   - **Geografinis SVG žemėlapis**
   
   Šie grafikų tipai ypač svarbūs sudėtingiems duomenų rinkiniams vizualizuoti, pavyzdžiui, finansinėms tendencijoms, moksliniams rodikliams ir geografinei informacijai.

3. **Nemokama ir atvirojo kodo (aukštas prioritetas)**: rinkinys turėtų būti atvirojo kodo, kad būtų išvengta licencijų išlaidų, užtikrintas skaidrumas ir suteiktas pritaikymo lankstumas.

4. **Mažos svarbos kriterijai**:
   - **Vykdymo greitis**: nors našumas yra svarbus, šiam sprendimui jis nėra svarbiausias prioritetas.
   - **Mastelio keitimas**: nors mastelio keitimas apskritai svarbus, neatidėliotinas poreikis yra sukurti MVP, kuris laikui bėgant gali augti. Mastelio keitimo klausimus galima spręsti vėliau.
   - **Atgalinis suderinamumas**: pradiniam kūrimui nėra pagrindinis rūpestis, jei biblioteka yra moderni ir aktyviai prižiūrima.

### Įvertintos bibliotekos:

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

**Apžvalga**:  
Apache ECharts yra galinga, lanksti grafikų biblioteka interaktyvioms, pritaikomoms vizualizacijoms. Ji palaiko labai įvairius grafikus ir ypač stipri sudėtingose, dinamiškose vizualizacijose.

**Stiprybės**:
- **Pažangus interaktyvumas**: ECharts puikiai suteikia interaktyvius grafikus, siūlydama tokias funkcijas kaip priartinimas, slinkimas ir dinaminiai duomenų atnaujinimai.
- **Žiedinė, radaro, žvakių diagramos, geografiniai SVG žemėlapiai**: ECharts palaiko daugelį reikalaujamų grafikų tipų, įskaitant žiedines, radaro, žvakių diagramas ir geografinių žemėlapių vizualizacijas.
- **Nemokama ir atvirojo kodo**: ECharts yra atvirojo kodo biblioteka, atitinkanti startuolio taupumą ir suteikianti laisvę keisti kodą.
- **Lankstumas ir išplečiamumas**: labai pritaikoma, su plačiu animacijų, pasirinktinių vizualizacijų ir pažangių grafikų metodų palaikymu.
  
**Silpnybės**:
- **Mokymosi kreivė**: ECharts, nors ir galinga, dėl savo lankstumo ir plačios API gali turėti statesnę mokymosi kreivę.
- **Dokumentacijos sudėtingumas**: dokumentacija išsami, bet gali būti neįveikiama programuotojams, tik pradedantiems su ja dirbti.

**Išvada**:  
ECharts labai tinka projektui dėl interaktyvių grafikų palaikymo, įskaitant visus reikalaujamus tipus, tokius kaip žvakių diagramos, radaro diagramos ir geografiniai žemėlapiai. Jos atvirasis kodas atitinka projekto poreikį lankstumui ir ekonomiškumui.

---

### 2. **Chart.js**

**Apžvalga**:  
Chart.js yra paprasta, lengvai naudojama grafikų biblioteka įprastiems grafikų tipams kurti. Ji žinoma dėl paprastumo ir integravimo lengvumo.

**Stiprybės**:
- **Naudojimo paprastumas**: Chart.js labai paprasta nustatyti ir naudoti, su minimalia mokymosi kreive.
- **Atvirasis kodas**: Chart.js yra nemokama ir atvirojo kodo, o tai labai svarbu mažinant išlaidas.
- **Įprasti grafikų tipai**: ji palaiko pagrindinius grafikus, tokius kaip žiedinė, ploto, radaro ir linijinė diagramos, kurios apima daugumą pagrindinių poreikių.

**Silpnybės**:
- **Ribotos pažangios diagramos**: Chart.js savitai nepalaiko sudėtingų grafikų tipų, tokių kaip žvakių diagramos, geografiniai SVG žemėlapiai ar klasterizavimo proceso diagramos. Nors šias funkcijas galima pridėti per papildinius ar pritaikymą, tai nėra taip paprasta kaip su kitomis bibliotekomis.
- **Interaktyvumas**: nors Chart.js palaiko pagrindinį interaktyvumą (pvz., paaiškinimus ir užvedimo efektus), ji nesiūlo tokių pažangių funkcijų kaip ECharts ar D3.js.

**Išvada**:  
Chart.js puikiai tinka paprastiems, greitiems projektams, tačiau sudėtingų grafikų tipų palaikymo trūkumas daro ją netinkamą daug duomenų naudojančiai programai su pažangiais poreikiais, tokiais kaip žvakių diagramos ir geografiniai žemėlapiai. Tai geras pasirinkimas prototipams, bet reikalaujamiems grafikų tipams rekomenduojami pažangesni įrankiai.

---

### 3. **ApexCharts**

**Apžvalga**:  
ApexCharts yra moderni grafikų biblioteka, siūlanti įvairius grafikų tipus ir orientuota į interaktyvias vizualizacijas su lengvai naudojama API.

**Stiprybės**:
- **Interaktyvios funkcijos**: ApexCharts siūlo interaktyvius grafikus su paaiškinimais, priartinimu, slinkimu ir atnaujinimais.
- **Finansinių ir mokslinių grafikų palaikymas**: ji palaiko labai įvairius grafikų tipus, įskaitant žvakių diagramas, radaro diagramas ir ploto diagramas.
- **Naudojimo paprastumas**: ji turi paprastą API ir lengvai integruojama į projektą.
- **Nemokama ir atvirojo kodo**: ApexCharts siūlo nemokamą atvirojo kodo versiją, tinkamą daugeliui naudojimo atvejų.
  
**Silpnybės**:
- **Sudėtingas pritaikymas**: nors ji siūlo daug funkcijų, pritaikymo galimybės nėra tokios lanksčios kaip ECharts ar D3.js labai sudėtingiems ar pasirinktiniams grafikų poreikiams.
- **Geografiniai žemėlapiai**: ApexCharts savitai nepalaiko geografinių žemėlapių ar klasterizavimo proceso diagramų, kurių reikia šiam projektui.

**Išvada**:  
ApexCharts yra stiprus kandidatas dėl naudojimo paprastumo ir interaktyvumo, tačiau nusileidžia kai kuriais pažangiais grafikų tipais, ypač geografinių žemėlapių ir klasterizavimo diagramų poreikio atžvilgiu. Tai geras pasirinkimas paprastesniems grafikams, bet trūksta kai kurių reikalaujamų funkcijų.

---

### 4. **AG Charts**

**Apžvalga**:  
AG Charts yra komercinės klasės grafikų biblioteka, sukurta našumui ir tikslumui. Ji labai tinka finansiniams, moksliniams ir verslo skydeliams kurti.

**Stiprybės**:
- **Pažangūs grafikų tipai**: AG Charts palaiko daug pažangių grafikų tipų, įskaitant žvakių diagramas, ploto diagramas, radaro diagramas ir kt. Ji taip pat siūlo gilią integraciją su kitais AG-Grid produktais.
- **Aukštas našumas**: ji siūlo puikų našumą, ypač dirbant su dideliais duomenų rinkiniais.
- **Interaktyvumas**: AG Charts palaiko įvairias interaktyvias funkcijas, tokias kaip priartinimas, paaiškinimai ir dinaminiai atnaujinimai.

**Silpnybės**:
- **Ne visiškai nemokama**: nors AG Charts siūlo nemokamą versiją, pilnai funkcionali versija yra mokama, o tai gali būti kliūtis startuoliams, norintiems sumažinti išlaidas.
- **Sudėtingumas**: nors biblioteka turtinga funkcijomis, ji gali būti per galinga paprastesniems projektams ir gali reikalauti daugiau sąrankos bei konfigūravimo, palyginti su kitais variantais.

**Išvada**:  
AG Charts yra galinga ir turtinga funkcijomis, bet gali būti ne pats geriausias pasirinkimas dėl savo komercinio pobūdžio ir kainų struktūros. Jos tinkamumas priklauso nuo to, ar biudžetas gali sutalpinti mokamas versijas, ar teikiama pirmenybė atvirojo kodo alternatyvoms.

---

### 5. **Highcharts**

**Apžvalga**:  
Highcharts yra populiari grafikų biblioteka, žinoma dėl plataus grafikų tipų spektro ir galingų pritaikymo galimybių.

**Stiprybės**:
- **Išsamūs grafikų tipai**: Highcharts palaiko labai įvairius grafikus, įskaitant žvakių, radaro, ploto diagramas ir geografinius žemėlapius.
- **Interaktyvi ir dinamiška**: Highcharts siūlo turtingas interaktyvias funkcijas, įskaitant detalizavimą (drill-down), priartinimą ir slinkimą.
- **Naudojimo paprastumas**: ji turi naudotojui patogią API ir gerą dokumentaciją, todėl lengva pradėti.

**Silpnybės**:
- **Komercinė licencija**: nors Highcharts siūlo nemokamą versiją nekomerciniam naudojimui, komercinė licencija yra brangi, o tai gali būti didelis trūkumas startuoliams.
- **Mokymosi kreivė**: nors ir ne tokia stati kaip ECharts, Highcharts mokymosi kreivė vis tiek gali būti sudėtinga pradedantiesiems.

**Išvada**:  
Highcharts yra biblioteka, turtinga funkcijomis, tačiau dėl komercinio licencijavimo ji mažiau tinka atvirojo kodo, į išlaidas jautriems projektams. Jos išsamios grafikų parinktys yra pliusas, bet licencijavimo klausimas riboja jos patrauklumą šiam naudojimo atvejui.

---

### 6. **Carbon Charts**

**Apžvalga**:  
Carbon Charts yra IBM sukurta grafikų biblioteka, skirta vizualiai patraukliems ir labai pritaikomiems grafikams kurti.

**Stiprybės**:
- **Pritaikomumas**: Carbon Charts leidžia plačiai pritaikyti grafikų išvaizdą ir elgseną.
- **Atvirasis kodas**: ji nemokama ir atvirojo kodo, o tai atitinka projekto reikalavimą dėl biudžetui draugiškų sprendimų.
- **Įprastų grafikų palaikymas**: ji palaiko įprastus grafikų tipus, tokius kaip žiedinė, radaro ir ploto diagramos, nors jai trūksta pažangesnių tipų, tokių kaip geografiniai žemėlapiai ar žvakių diagramos, palaikymo.

**Silpnybės**:
- **Ribotos pažangios diagramos**: ji nepalaiko geografinių žemėlapių, klasterizavimo proceso diagramų ar žvakių diagramų, kurios yra būtinos projektui.
- **Mažesnė ekosistema**: Carbon Charts turi mažesnę bendruomenę ir ekosistemą, palyginti su didesnėmis grafikų bibliotekomis, tokiomis kaip ECharts ar Highcharts.

**Išvada**:  
Carbon Charts yra atvirojo kodo ir pritaikoma, bet jai trūksta sudėtingesnių grafikų tipų, reikalingų šiam projektui, palaikymo. Ji labiau tinka paprastesniems grafikų poreikiams.

---

### 7. **Layer Cake**

**Apžvalga**:  
Layer Cake yra duomenų vizualizacijos biblioteka, skirta lanksčioms, sluoksniuotoms vizualizacijoms kurti.

**Stiprybės**:
- **Pritaikomi sluoksniai**: ji suteikia galingas sluoksniavimo parinktis sudėtingoms vizualizacijoms.
- **Atvirasis kodas**: ji nemokama ir atvirojo kodo, todėl yra tinkamas pasirinkimas biudžetą taupantiems projektams.

**Silpnybės**:
- **Ribota dokumentacija**: Layer Cake trūksta plačios dokumentacijos ir bendruomenės paramos, todėl su ja dirbti sunkiau nei su labiau įsitvirtinusiomis bibliotekomis.
- **Nesukurta grafikams**: Layer Cake labiau tinka ne grafikų vizualizacijoms, todėl jos iškart paruoštos grafikų parinktys yra ribotos.

**Išvada**:  
Nors Layer Cake įdomi unikalioms vizualizacijoms, ji nėra idealus pasirinkimas tradiciniams grafikų reikalavimams, tokiems kaip žvakių ar radaro diagramos. Ji labiau tinka pasirinktinėms vizualizacijoms, nepatenkančioms į standartinių grafikų sritį.

---

### 8. **D3.js**

**Apžvalga**:  
D3.js yra galinga JavaScript biblioteka duomenimis grįstoms vizualizacijoms kurti per HTML, SVG ir CSS.

**Stiprybės**:
- **Neprilygstamas lankstumas**: D3.js leidžia sukurti praktiškai bet kokio tipo pasirinktinę vizualizaciją, todėl ji labai galinga pažangiems ir interaktyviems grafikams.
- **Plačios funkcijos**: ji palaiko visus reikalaujamus grafikų tipus, įskaitant geografinius žemėlapius, klasterizavimo diagramas ir kt.
- **Pritaikoma**: D3.js pritaikymo lygis yra neprilygstamas, leidžiantis programuotojams kurti labai pritaikytas vizualizacijas.

**Silpnybės**:
- **Stati mokymosi kreivė**: D3.js turi statią mokymosi kreivę ir yra sudėtingesnė integruoti, palyginti su kitomis bibliotekomis.
- **Atima daug laiko**: grafikų kūrimas D3.js gali atimti daug laiko, ypač įprastiems grafikams, tokiems kaip žvakių ar žiedinės diagramos.

**Išvada**:  
D3.js yra nepaprastai galinga pažangiems, pritaikytiems grafikams, bet dėl statios mokymosi kreivės ir kūrimo laiko yra per galinga daugeliui tipinių naudojimo atvejų. Ji geriausiai tinka situacijoms, kai kitos grafikų bibliotekos nesuteikia reikiamo pritaikymo lygio.

---

### Išvada

Įvertinę bibliotekas pagal projekto poreikius, nusprendėme, kad **Apache ECharts** išsiskiria kaip geriausias variantas. Ji palaiko visą reikalaujamų grafikų spektrą, įskaitant geografinius žemėlapius, žvakių diagramas ir klasterizavimo diagramas. Ji yra atvirojo kodo, turtinga funkcijomis ir labai interaktyvi, o tai puikiai atitinka projekto tikslus. Nors **D3.js** siūlo didžiausią lankstumą, jos sudėtingumas ir laiko investicijos daro ją mažiau idealią startuoliui, norinčiam greitai iteruoti. **ApexCharts** ir **Chart.js** yra geros alternatyvos paprastesniems projektams, tačiau joms trūksta pažangių grafikų tipų palaikymo.
