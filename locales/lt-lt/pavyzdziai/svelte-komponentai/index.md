# Architektūros sprendimo įrašas (ADR) dėl Svelte komponentų

<!--

Prompt:

Architecture decision record for Svelte components.

Compare options: SVAR, Carbon, Flowbite, SkeletonUI, MeltUI, SvelteUI, shadcn-svelte

The goal is full features for table, charts, lists, grids, gantt, 

-->

## Kontekstas

Renkamės Svelte UI komponentų biblioteką, kuri suteiktų visas funkcijas:
- **Lentelėms**
- **Diagramoms**
- **Sąrašams**
- **Tinkleliams**
- **Gantt diagramoms**

Tikslas – pasirinkti biblioteką, subalansuojančią integravimo paprastumą, visapusišką funkcijų palaikymą, našumą ir ilgalaikį prižiūrimumą. Svarstomi variantai:

1. **SVAR**
2. **Carbon**
3. **Flowbite**
4. **SkeletonUI**
5. **MeltUI**
6. **SvelteUI**
7. **shadcn-svelte**

## Variantų analizė

### 1. **SVAR**
- **Apžvalga**: SVAR yra moderni, daug funkcijų turinti Svelte komponentų biblioteka, orientuota į dizaino sistemas ir įmonėms paruoštus komponentus.
- **Privalumai**:
  - Visapusiški komponentai, įskaitant lenteles, formas ir diagramas.
  - Plačios pritaikymo galimybės su integruotu temų palaikymu.
  - Integruotas prieinamumo ir prisitaikymo palaikymas.
  - Gerai dokumentuota, su bendruomenės indėliu.
- **Trūkumai**:
  - Gali būti sunkesnė, palyginti su kitomis paprastesnėmis bibliotekomis.
  - Ribotas tam tikrų komponentų, pavyzdžiui, Gantt diagramų ir pažangių tinklelių, palaikymas.
- **Geriausiai tinka**: įmonių lygio programoms, kuriose reikalinga visapusiška dizaino sistema.
- **Lentelių / diagramų palaikymas**: vidutinis iki geras.
- **Tinklelių / Gantt palaikymas**: minimalus.

### 2. **Carbon**
- **Apžvalga**: Carbon Design System yra IBM atvirojo kodo dizaino sistema, siūlanti tvirtą UI komponentų rinkinį.
- **Privalumai**:
  - Aukštos kokybės, nušlifuotas dizainas su plačia dokumentacija.
  - Labai prieinama ir prisitaikanti.
  - Didelė komponentų biblioteka, įskaitant tinklelius, lenteles ir formų valdiklius.
- **Trūkumai**:
  - Nėra orientuota į Svelte, todėl integravimas gali būti nepatogus.
  - Gali reikėti papildomo pritaikymo visiškam suderinamumui su Svelte.
  - Nėra iškart paruošto palaikymo pažangiems komponentams, tokiems kaip Gantt diagramos ar sudėtingos diagramos.
- **Geriausiai tinka**: dideliems projektams, kuriems reikalinga nuosekli, nušlifuota sąsaja.
- **Lentelių / diagramų palaikymas**: geras (su diagramų bibliotekų integracijomis).
- **Tinklelių / Gantt palaikymas**: geras (tinklelių palaikymas yra, bet Gantt diagramų nėra).

### 3. **Flowbite**
- **Apžvalga**: Flowbite yra komponentų biblioteka, sukurta su Tailwind CSS, siūlanti įvairius komponentus ir UI elementus.
- **Privalumai**:
  - Pagrįsta Tailwind CSS, todėl lengva pritaikyti.
  - Lengva integruoti ir naudoti su Svelte.
  - Suteikia turtingus komponentus, tokius kaip lentelės, diagramos ir UI valdikliai.
- **Trūkumai**:
  - Trūksta pažangių funkcijų (pvz., Gantt diagramų ar sudėtingų tinklelių).
  - Neturi savitų diagramų komponentų; remiasi išorinėmis bibliotekomis.
- **Geriausiai tinka**: projektams, kuriems reikalingas greitas kūrimas su dėmesiu Tailwind CSS integracijai.
- **Lentelių / diagramų palaikymas**: geras (reikia integracijos su trečiųjų šalių diagramų bibliotekomis).
- **Tinklelių / Gantt palaikymas**: minimalus.

### 4. **SkeletonUI**
- **Apžvalga**: SkeletonUI yra lengva Svelte komponentų biblioteka, orientuota į paprastumą ir minimalizmą.
- **Privalumai**:
  - Itin lengva ir greita.
  - Paprasta ir intuityvi API.
  - Gera mažiems projektams arba kai našumas kritinis.
- **Trūkumai**:
  - Įtraukta labai mažai komponentų, todėl ji nėra turtinga funkcijomis.
  - Trūksta pažangių lentelių / tinklelių / diagramų / Gantt komponentų.
  - Ribota bendruomenės parama ir mažiau išsami dokumentacija.
- **Geriausiai tinka**: projektams, kuriems reikalingi lengvi komponentai su minimaliomis pridėtinėmis sąnaudomis.
- **Lentelių / diagramų palaikymas**: minimalus.
- **Tinklelių / Gantt palaikymas**: minimalus.

### 5. **MeltUI**
- **Apžvalga**: MeltUI yra prieinamų UI komponentų rinkinys Svelte, orientuotas į paprastumą ir komponuojamumą.
- **Privalumai**:
  - Lengva ir visiškai pritaikoma.
  - Geros iškart paruoštos prieinamumo funkcijos.
  - Moderni ir minimalistinė išvaizda.
- **Trūkumai**:
  - Mažiau turtinga funkcijomis, palyginti su kitomis bibliotekomis.
  - Trūksta pažangių tinklelių ir lentelių komponentų.
  - Nėra Gantt diagramų ar sudėtingų diagramų parinkčių.
- **Geriausiai tinka**: minimalistiniams dizainams, teikiantiems pirmenybę prieinamumui ir našumui.
- **Lentelių / diagramų palaikymas**: minimalus.
- **Tinklelių / Gantt palaikymas**: minimalus.

### 6. **SvelteUI**
- **Apžvalga**: SvelteUI yra išsami ir pritaikoma Svelte UI komponentų biblioteka, skirta modernioms interneto programoms su elegantiška sąsaja kurti.
- **Privalumai**:
  - Išsamus komponentų rinkinys, įskaitant lenteles, tinklelius, diagramas ir formas.
  - Palaiko ir šviesųjį, ir tamsųjį režimus.
  - Labai pritaikoma ir lengvai išplečiama.
  - Integruotos integracijos su diagramų bibliotekomis, tokiomis kaip `chart.js` ar `d3.js`.
- **Trūkumai**:
  - Gali būti sunkesnė nei paprastesnės komponentų bibliotekos.
  - Reikia šiek tiek sąrankos išorinėms bibliotekoms integruoti sudėtingesnėms funkcijoms, pavyzdžiui, Gantt diagramoms.
- **Geriausiai tinka**: projektams, kuriems reikalingas išsamus, pritaikomas komponentų rinkinys.
- **Lentelių / diagramų palaikymas**: puikus (palaikomos diagramų bibliotekos).
- **Tinklelių / Gantt palaikymas**: geras (tinklelių komponentai yra; Gantt reikia išorinės integracijos).

### 7. **shadcn-svelte**
- **Apžvalga**: Svelte ShadCN versija, orientuota į pirmiausia įrankių (utility-first) dizainą ir suteikianti modernius, stilizuotus komponentus.
- **Privalumai**:
  - Pirmiausia įrankių (utility-first) dizainas, sukurtas ant Tailwind CSS, todėl lengva pritaikyti.
  - Turtingas komponentų rinkinys ir iškart visiškai stilizuota.
  - Lengva integruoti su kitomis bibliotekomis.
- **Trūkumai**:
  - Ne tokia funkcijų požiūriu pilna kaip kai kurios kitos pažangių UI elementų atžvilgiu.
  - Trūksta integruoto lentelių, diagramų ar tinklelių palaikymo.
  - Nėra iškart paruošto Gantt diagramų palaikymo.
- **Geriausiai tinka**: mažiems ir vidutiniams projektams, kuriems reikalingas pirmiausia įrankių (utility-first), pritaikomas požiūris.
- **Lentelių / diagramų palaikymas**: minimalus.
- **Tinklelių / Gantt palaikymas**: minimalus.

## Sprendimas

### Rekomenduojamas variantas: **SvelteUI**

- **Pagrindimas**: SvelteUI siūlo visapusišką, išsamų komponentų rinkinį, atitinkantį lentelių, diagramų, tinklelių ir formų poreikį. Ji labai pritaikoma, gerai integruojasi su kitomis diagramų bibliotekomis (pvz., `chart.js` ir `d3.js`) ir turi gerą lengvo našumo bei funkcijų turtingumo pusiausvyrą. Nors ji gali nesuteikti iškart paruošto Gantt diagramų palaikymo, ją galima lengvai išplėsti trečiųjų šalių integracijomis, todėl ji idealiai tinka visapusiškam, keičiamo mastelio sprendimui.
  
  - **Privalumai**:
    - Puikus lentelių ir diagramų palaikymas.
    - Pilni tinklelių ir išdėstymo komponentai.
    - Pritaikoma ir gerai integruojasi su išorinėmis diagramų bibliotekomis.
    - Gera bendruomenė ir dokumentacija.
  
  - **Trūkumai**:
    - Sunkesnė nei kai kurios kitos minimalistinės bibliotekos.
    - Sudėtingoms diagramoms, tokioms kaip Gantt diagramos, reikia išorinės integracijos.
  
### Alternatyva: **Flowbite** arba **Carbon** (didesniems įmonių projektams)
- Jei reikalinga nušlifuota, Tailwind pagrįsta ar nuoseklesnė dizaino sistema, tinkamomis alternatyvomis gali būti **Flowbite** (su Tailwind CSS) arba **Carbon** (įmonių lygio sprendimams). Tačiau gali reikėti papildomų pastangų integracijoms su sudėtingesnėmis diagramomis ir komponentais.

## Išvada

Geriausiai jūsų reikalavimus (visos funkcijos lentelėms, diagramoms, sąrašams, tinkleliams, Gantt) atitinka **SvelteUI**, toliau seka **Flowbite** ir **Carbon**, priklausomai nuo projekto poreikių ir dizaino pageidavimų.