# Arhitektūras lēmuma ieraksts: diagrammu bibliotēka datu vizualizācijai ar TypeScript un JSON

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

**Galvenais mērķis:**  
Izvēlēties uzlabotu diagrammu rīkkopu interaktīvu vizualizāciju veidošanai, koncentrējoties uz finanšu datiem, zinātniskajiem datiem un valdības datiem, izmantojot TypeScript un JSON. Bibliotēkai jānodrošina robustas funkcijas, elastība un jābūt atvērtā pirmkoda. 

### Konteksts un prasības:

1. **Aģila izstrāde (augsta prioritāte)**: kā jaunuzņēmumam ātra iterācija, prototipēšana un elastība izstrādē ir būtiska. Diagrammu bibliotēkai jāļauj veikt ātrus izstrādes ciklus.
   
2. **Diagrammu veidi (augsta prioritāte)**:
   - **Gredzena diagramma (doughnut)**
   - **Radara diagramma**
   - **Klasterizācijas procesa diagramma**
   - **Laukuma diagramma ar laika asi**
   - **Svečturu diagramma (candlestick)**
   - **Naitingeilas diagramma**
   - **Ģeogrāfiskā SVG karte**
   
   Šie diagrammu veidi ir īpaši svarīgi sarežģītu datu kopu vizualizēšanai, piemēram, finanšu tendencēm, zinātniskajām metrikām un ģeogrāfiskajai informācijai.

3. **Bezmaksas un atvērtā pirmkoda (augsta prioritāte)**: rīkkopai jābūt atvērtā pirmkoda, lai izvairītos no licencēšanas izmaksām, nodrošinātu pārredzamību un piedāvātu elastību pielāgošanai.

4. **Zemas svarīguma kritēriji**:
   - **Izpildlaika ātrums**: lai gan veiktspēja ir svarīga, tā nav galvenā prioritāte šim lēmumam.
   - **Mērogojamība**: lai gan mērogojamība parasti ir svarīga, tūlītējā vajadzība ir izveidot MVP, kas laika gaitā var augt. Mērogojamības jautājumus var risināt vēlāk.
   - **Atpakaļsaderība**: nav galvenā bažas sākotnējai būvēšanai, kamēr vien bibliotēka ir moderna un aktīvi uzturēta.

### Izvērtētās bibliotēkas:

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

**Pārskats**:  
Apache ECharts ir jaudīga, elastīga diagrammu bibliotēka interaktīvām, pielāgojamām vizualizācijām. Tā atbalsta plašu diagrammu klāstu un ir īpaši spēcīga sarežģītās, dinamiskās vizualizācijās.

**Stiprās puses**:
- **Uzlabota interaktivitāte**: ECharts izceļas interaktīvu diagrammu nodrošināšanā, piedāvājot tādas funkcijas kā tālummaiņa, pārvietošana un dinamiski datu atjauninājumi.
- **Gredzena, radara, svečturu, ģeogrāfiskās SVG kartes**: ECharts atbalsta daudzus no nepieciešamajiem diagrammu veidiem, tostarp gredzena, radara, svečturu un ģeogrāfisko karšu vizualizācijas.
- **Bezmaksas un atvērtā pirmkoda**: ECharts ir atvērtā pirmkoda bibliotēka, kas atbilst jaunuzņēmuma budžetu apzinīgajam raksturam un nodrošina brīvību modificēt kodu.
- **Elastība un paplašināmība**: ļoti pielāgojama, ar plašu atbalstu animācijām, pielāgotām vizualizācijām un uzlabotām diagrammu veidošanas metodēm.
  
**Vājās puses**:
- **Mācīšanās līkne**: ECharts, lai gan jaudīgs, savas elastības un plašā API dēļ var būt stāvāka mācīšanās līkne.
- **Dokumentācijas sarežģītība**: dokumentācija ir visaptveroša, bet izstrādātājiem, kuri tikai sāk, var būt pārāk apjomīga.

**Spriedums**:  
ECharts ir ļoti piemērots projektam, pateicoties tā atbalstam interaktīvām diagrammām, tostarp visiem nepieciešamajiem veidiem, piemēram, svečturu diagrammām, radara diagrammām un ģeogrāfiskajām kartēm. Tā atvērtā pirmkoda raksturs atbilst projekta vajadzībai pēc elastības un rentabilitātes.

---

### 2. **Chart.js**

**Pārskats**:  
Chart.js ir vienkārša, viegli lietojama diagrammu bibliotēka bieži sastopamu diagrammu veidu izveidei. Tā ir pazīstama ar savu vienkāršību un viegli veicamo integrāciju.

**Stiprās puses**:
- **Lietošanas vienkāršība**: Chart.js ir ļoti vienkārši iestatāms un lietojams, ar minimālu mācīšanās līkni.
- **Atvērtā pirmkoda**: Chart.js ir bezmaksas un atvērtā pirmkoda, kas ir kritiski svarīgi izmaksu samazināšanai.
- **Bieži sastopami diagrammu veidi**: tā atbalsta pamata diagrammas, piemēram, gredzena, laukuma, radara un līniju diagrammas, kas aptver lielāko daļu galveno vajadzību.

**Vājās puses**:
- **Ierobežotas uzlabotās diagrammas**: Chart.js dabiski neatbalsta sarežģītus diagrammu veidus, piemēram, svečturu diagrammas, ģeogrāfiskās SVG kartes vai klasterizācijas procesa diagrammas. Lai gan šīs funkcijas var pievienot ar spraudņiem vai pielāgojumiem, tas nav tik vienkārši kā ar citām bibliotēkām.
- **Interaktivitāte**: lai gan Chart.js atbalsta pamata interaktivitāti (piem., rīkjoslu padomus un uzlidināšanas efektus), tā nepiedāvā tik uzlabotas funkcijas kā ECharts vai D3.js.

**Spriedums**:  
Chart.js ir lielisks vienkāršiem, ātriem projektiem, taču atbalsta trūkums sarežģītiem diagrammu veidiem padara to nepiemērotu datu ietilpīgai lietojumprogrammai ar uzlabotām vajadzībām, piemēram, svečturu diagrammām un ģeogrāfiskajām kartēm. Tā ir laba izvēle prototipēšanai, bet nepieciešamajiem diagrammu veidiem ieteicami uzlabotāki rīki.

---

### 3. **ApexCharts**

**Pārskats**:  
ApexCharts ir moderna diagrammu bibliotēka, kas nodrošina dažādus diagrammu veidus un koncentrējas uz interaktīvām vizualizācijām ar viegli lietojamu API.

**Stiprās puses**:
- **Interaktīvās funkcijas**: ApexCharts piedāvā interaktīvas diagrammas ar rīkjoslu padomiem, tālummaiņu, pārvietošanu un atjauninājumiem.
- **Atbalsts finanšu un zinātniskajām diagrammām**: tā atbalsta plašu diagrammu veidu klāstu, tostarp svečturu diagrammas, radara diagrammas un laukuma diagrammas.
- **Lietošanas vienkāršība**: tai ir tiešs API, un to ir viegli integrēt projektā.
- **Bezmaksas un atvērtā pirmkoda**: ApexCharts piedāvā bezmaksas atvērtā pirmkoda versiju, kas ir piemērota daudziem lietošanas gadījumiem.
  
**Vājās puses**:
- **Sarežģīta pielāgošana**: lai gan tā nodrošina daudzas funkcijas, pielāgošanas iespējas nav tik elastīgas kā ECharts vai D3.js ļoti sarežģītām vai pielāgotām diagrammu vajadzībām.
- **Ģeogrāfiskās kartes**: ApexCharts dabiski neatbalsta ģeogrāfiskās kartes vai klasterizācijas procesa diagrammas, kas šim projektam ir nepieciešamas.

**Spriedums**:  
ApexCharts ir spēcīgs pretendents tā lietošanas vienkāršības un interaktivitātes dēļ, taču tā atpaliek attiecībā uz dažiem uzlabotiem diagrammu veidiem, īpaši vajadzībā pēc ģeogrāfiskām kartēm un klasterizācijas diagrammām. Tā ir laba iespēja vienkāršākām diagrammām, bet trūkst dažu nepieciešamo funkciju.

---

### 4. **AG Charts**

**Pārskats**:  
AG Charts ir komerciālas kvalitātes diagrammu bibliotēka, kas paredzēta veiktspējai un precizitātei. Tā ir ļoti piemērota finanšu, zinātnisko un biznesa informācijas paneļu izveidei.

**Stiprās puses**:
- **Uzlaboti diagrammu veidi**: AG Charts atbalsta daudzus uzlabotus diagrammu veidus, tostarp svečturu diagrammas, laukuma diagrammas, radara diagrammas un citus. Tā piedāvā arī dziļu integrāciju ar citiem AG-Grid produktiem.
- **Augsta veiktspēja**: tā piedāvā teicamu veiktspēju, īpaši strādājot ar lielām datu kopām.
- **Interaktivitāte**: AG Charts atbalsta dažādas interaktīvas funkcijas, piemēram, tālummaiņu, rīkjoslu padomus un dinamiskus atjauninājumus.

**Vājās puses**:
- **Nav pilnībā bezmaksas**: lai gan AG Charts piedāvā bezmaksas versiju, pilnu funkciju versija ir maksas, kas var būt šķērslis jaunuzņēmumiem, kuri vēlas samazināt izmaksas.
- **Sarežģītība**: lai gan bibliotēka ir funkcijām bagāta, tā var būt pārmērīga vienkāršākiem projektiem un var prasīt vairāk iestatīšanas un konfigurēšanas salīdzinājumā ar citām iespējām.

**Spriedums**:  
AG Charts ir jaudīga un funkcijām bagāta, bet, iespējams, nav labākā izvēle sava komerciālā rakstura un izmaksu struktūras dēļ. Tās piemērotība ir atkarīga no tā, vai budžets pieļauj maksas versijas vai arī priekšroka tiek dota atvērtā pirmkoda alternatīvām.

---

### 5. **Highcharts**

**Pārskats**:  
Highcharts ir populāra diagrammu bibliotēka, kas pazīstama ar plašo diagrammu veidu klāstu un jaudīgām pielāgošanas iespējām.

**Stiprās puses**:
- **Visaptveroši diagrammu veidi**: Highcharts atbalsta plašu diagrammu klāstu, tostarp svečturu, radara, laukuma un ģeogrāfiskās kartes.
- **Interaktīvs un dinamisks**: Highcharts nodrošina bagātas interaktīvas funkcijas, tostarp detalizāciju (drill-down), tālummaiņu un pārvietošanu.
- **Lietošanas vienkāršība**: tai ir lietotājam draudzīgs API un laba dokumentācija, kas atvieglo darba sākšanu.

**Vājās puses**:
- **Komerciālā licence**: lai gan Highcharts piedāvā bezmaksas versiju nekomerciālai lietošanai, komerciālā licence ir dārga, kas var būt ievērojams trūkums jaunuzņēmumiem.
- **Mācīšanās līkne**: lai gan tā nav tik stāva kā ECharts, Highcharts mācīšanās līkne iesācējiem joprojām var būt sarežģīta.

**Spriedums**:  
Highcharts ir funkcijām bagāta bibliotēka, bet tās komerciālā licencēšana padara to mazāk piemērotu atvērtā pirmkoda, izmaksu ziņā jutīgiem projektiem. Tās visaptverošās diagrammu iespējas ir pluss, taču licencēšanas jautājums ierobežo tās pievilcību šim lietošanas gadījumam.

---

### 6. **Carbon Charts**

**Pārskats**:  
Carbon Charts ir IBM izstrādāta diagrammu bibliotēka, kas paredzēta vizuāli pievilcīgu un ļoti pielāgojamu diagrammu veidošanai.

**Stiprās puses**:
- **Pielāgojamība**: Carbon Charts ļauj plaši pielāgot diagrammu izskatu un uzvedību.
- **Atvērtā pirmkoda**: tā ir bezmaksas un atvērtā pirmkoda, kas atbilst projekta prasībai pēc budžetam draudzīgiem risinājumiem.
- **Atbalsts bieži sastopamām diagrammām**: tā atbalsta bieži sastopamus diagrammu veidus, piemēram, gredzena, radara un laukuma diagrammas, lai gan tai trūkst atbalsta uzlabotākiem veidiem, piemēram, ģeogrāfiskām kartēm vai svečturu diagrammām.

**Vājās puses**:
- **Ierobežoti uzlaboti diagrammu veidi**: tā neatbalsta ģeogrāfiskās kartes, klasterizācijas procesa diagrammas vai svečturu diagrammas, kas projektam ir būtiskas.
- **Mazāka ekosistēma**: Carbon Charts ir mazāka kopiena un ekosistēma salīdzinājumā ar lielākām diagrammu bibliotēkām, piemēram, ECharts vai Highcharts.

**Spriedums**:  
Carbon Charts ir atvērtā pirmkoda un pielāgojama, bet tai trūkst atbalsta sarežģītākiem diagrammu veidiem, kas nepieciešami šim projektam. Tā ir piemērotāka vienkāršākām diagrammu vajadzībām.

---

### 7. **Layer Cake**

**Pārskats**:  
Layer Cake ir datu vizualizācijas bibliotēka, kas paredzēta elastīgu, slāņainu vizualizāciju izveidei.

**Stiprās puses**:
- **Pielāgojami slāņi**: tā nodrošina jaudīgas slāņošanas iespējas sarežģītām vizualizācijām.
- **Atvērtā pirmkoda**: tā ir bezmaksas un atvērtā pirmkoda, padarot to par dzīvotspējīgu iespēju budžetu apzinīgiem projektiem.

**Vājās puses**:
- **Ierobežota dokumentācija**: Layer Cake trūkst plašas dokumentācijas un kopienas atbalsta, padarot darbu ar to grūtāku salīdzinājumā ar iedibinātākām bibliotēkām.
- **Nav veidota diagrammām**: Layer Cake ir labāk piemērota vizualizācijām, kas nav diagrammas, tāpēc tās tūlītējās diagrammu iespējas ir ierobežotas.

**Spriedums**:  
Lai gan Layer Cake ir interesanta unikālām vizualizācijām, tā nav ideāla tradicionālajām diagrammu prasībām, piemēram, svečturu vai radara diagrammām. Tā ir piemērotāka pielāgotām vizualizācijām ārpus standarta diagrammu jomas.

---

### 8. **D3.js**

**Pārskats**:  
D3.js ir jaudīga JavaScript bibliotēka datu vadītu vizualizāciju veidošanai ar HTML, SVG un CSS.

**Stiprās puses**:
- **Nepārspējama elastība**: D3.js ļauj izveidot praktiski jebkura veida pielāgotu vizualizāciju, padarot to ļoti jaudīgu uzlabotām un interaktīvām diagrammām.
- **Plašas funkcijas**: tā atbalsta visus nepieciešamos diagrammu veidus, tostarp ģeogrāfiskās kartes, klasterizācijas diagrammas un citus.
- **Pielāgojama**: pielāgošanas līmenis D3.js ir nepārspējams, ļaujot izstrādātājiem veidot ļoti pielāgotas vizualizācijas.

**Vājās puses**:
- **Stāva mācīšanās līkne**: D3.js ir stāva mācīšanās līkne, un to ir sarežģītāk integrēt salīdzinājumā ar citām bibliotēkām.
- **Laikietilpīga**: diagrammu veidošana D3.js var būt laikietilpīga, īpaši bieži sastopamām diagrammām, piemēram, svečturu vai gredzena diagrammām.

**Spriedums**:  
D3.js ir neticami jaudīga uzlabotām, pielāgotām diagrammām, taču daudziem tipiskiem lietošanas gadījumiem tā ir pārmērīga savas stāvās mācīšanās līknes un izstrādes laika dēļ. Tā ir vislabākā situācijās, kad citas diagrammu bibliotēkas nenodrošina nepieciešamo pielāgošanas līmeni.

---

### Secinājums

Pēc bibliotēku izvērtēšanas pēc projekta vajadzībām par labāko iespēju izvirzās **Apache ECharts**. Tā atbalsta pilnu nepieciešamo diagrammu klāstu, tostarp ģeogrāfiskās kartes, svečturu diagrammas un klasterizācijas diagrammas. Tā ir atvērtā pirmkoda, funkcijām bagāta un ļoti interaktīva, kas ideāli atbilst projekta mērķiem. Lai gan **D3.js** piedāvā vislielāko elastību, tās sarežģītība un laika ieguldījums padara to mazāk ideālu jaunuzņēmumam, kas vēlas ātri iterēt. **ApexCharts** un **Chart.js** ir labas alternatīvas vienkāršākiem projektiem, taču tām trūkst atbalsta uzlabotiem diagrammu veidiem.
