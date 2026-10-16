# Arhitektūras lēmuma ieraksts (ADR) par Svelte komponentēm

<!--

Prompt:

Architecture decision record for Svelte components.

Compare options: SVAR, Carbon, Flowbite, SkeletonUI, MeltUI, SvelteUI, shadcn-svelte

The goal is full features for table, charts, lists, grids, gantt, 

-->

## Konteksts

Mēs izvēlamies Svelte UI komponenšu bibliotēku, kas nodrošinātu pilnas funkcijas šādiem elementiem:
- **Tabulas**
- **Diagrammas**
- **Saraksti**
- **Režģi**
- **Ganta diagrammas**

Mērķis ir izvēlēties bibliotēku, kas līdzsvaro integrācijas vieglumu, pilnu funkciju atbalstu, veiktspēju un ilgtermiņa uzturamību. Apsvērtās iespējas ir:

1. **SVAR**
2. **Carbon**
3. **Flowbite**
4. **SkeletonUI**
5. **MeltUI**
6. **SvelteUI**
7. **shadcn-svelte**

## Iespēju analīze

### 1. **SVAR**
- **Pārskats**: SVAR ir moderna, funkcijām bagāta komponenšu bibliotēka Svelte, kas koncentrējas uz dizaina sistēmām un uzņēmumiem gatavām komponentēm.
- **Priekšrocības**:
  - Pilnu funkciju komponentes, tostarp tabulas, veidlapas un diagrammas.
  - Plašas pielāgošanas iespējas ar iebūvētu motīvu atbalstu.
  - Iebūvēts pieejamības un atsaucības atbalsts.
  - Labi dokumentēta ar kopienas ieguldījumiem.
- **Trūkumi**:
  - Tā var būt smagāka salīdzinājumā ar citām vienkāršākām bibliotēkām.
  - Ierobežots atbalsts konkrētām komponentēm, piemēram, Ganta diagrammām un uzlabotiem režģiem.
- **Vislabāk piemērota**: uzņēmuma līmeņa lietojumprogrammām, kurās nepieciešama pilnu funkciju dizaina sistēma.
- **Tabulu/diagrammu atbalsts**: mērens līdz labs.
- **Režģu/Ganta atbalsts**: minimāls.

### 2. **Carbon**
- **Pārskats**: Carbon Design System ir IBM atvērtā pirmkoda dizaina sistēma, kas piedāvā robustu UI komponenšu kopumu.
- **Priekšrocības**:
  - Augstas kvalitātes, izsmalcināts dizains ar plašu dokumentāciju.
  - Ļoti pieejama un atsaucīga.
  - Liela komponenšu bibliotēka, tostarp režģi, tabulas un veidlapu vadīklas.
- **Trūkumi**:
  - Nav koncentrēta uz Svelte, tāpēc integrācija var būt apgrūtinoša.
  - Pilnai Svelte saderībai var būt nepieciešama papildu pielāgošana.
  - Nav tiešā atbalsta uzlabotām komponentēm, piemēram, Ganta diagrammām vai sarežģītām diagrammām.
- **Vislabāk piemērota**: liela mēroga projektiem, kuriem nepieciešama konsekventa, izsmalcināta lietotāja saskarne.
- **Tabulu/diagrammu atbalsts**: labs (ar diagrammu bibliotēku integrācijām).
- **Režģu/Ganta atbalsts**: labs (režģu atbalsts ir pieejams, bet nav Ganta diagrammu).

### 3. **Flowbite**
- **Pārskats**: Flowbite ir komponenšu bibliotēka, kas veidota ar Tailwind CSS un piedāvā dažādas komponentes un UI elementus.
- **Priekšrocības**:
  - Balstīta uz Tailwind CSS, kas ļauj to viegli pielāgot.
  - Viegli integrējama un lietojama ar Svelte.
  - Nodrošina bagātas komponentes, piemēram, tabulas, diagrammas un UI vadīklas.
- **Trūkumi**:
  - Trūkst uzlabotu funkciju (piem., Ganta diagrammas vai sarežģīti režģi).
  - Nav dabisko diagrammu komponenšu; paļaujas uz ārējām bibliotēkām.
- **Vislabāk piemērota**: projektiem, kuriem nepieciešama ātra izstrāde ar uzsvaru uz integrāciju ar Tailwind CSS.
- **Tabulu/diagrammu atbalsts**: labs (nepieciešama integrācija ar trešo pušu diagrammu bibliotēkām).
- **Režģu/Ganta atbalsts**: minimāls.

### 4. **SkeletonUI**
- **Pārskats**: SkeletonUI ir viegla komponenšu bibliotēka Svelte, kas koncentrējas uz vienkāršību un minimālismu.
- **Priekšrocības**:
  - Ārkārtīgi viegla un ātra.
  - Vienkāršs un intuitīvs API.
  - Laba maziem projektiem vai tur, kur veiktspēja ir kritiska.
- **Trūkumi**:
  - Iekļauts ļoti maz komponenšu, tāpēc tā nav funkcijām bagāta.
  - Trūkst uzlabotu tabulu/režģu/diagrammu/Ganta komponenšu.
  - Ierobežots kopienas atbalsts un mazāk visaptveroša dokumentācija.
- **Vislabāk piemērota**: projektiem, kuriem nepieciešamas vieglas komponentes ar minimālām izmaksām.
- **Tabulu/diagrammu atbalsts**: minimāls.
- **Režģu/Ganta atbalsts**: minimāls.

### 5. **MeltUI**
- **Pārskats**: MeltUI ir pieejamu UI komponenšu kolekcija Svelte, kas koncentrējas uz vienkāršību un komponējamību.
- **Priekšrocības**:
  - Viegla un pilnībā pielāgojama.
  - Labas pieejamības funkcijas uzreiz.
  - Moderns un minimālistisks dizains.
- **Trūkumi**:
  - Mazāk funkcijām bagāta salīdzinājumā ar citām bibliotēkām.
  - Trūkst uzlabotu režģu un tabulu komponenšu.
  - Nav Ganta diagrammu vai sarežģītu diagrammu iespēju.
- **Vislabāk piemērota**: minimālistiskiem dizainiem, kas prioritizē pieejamību un veiktspēju.
- **Tabulu/diagrammu atbalsts**: minimāls.
- **Režģu/Ganta atbalsts**: minimāls.

### 6. **SvelteUI**
- **Pārskats**: SvelteUI ir visaptveroša un pielāgojama UI komponenšu bibliotēka Svelte, kas paredzēta moderno tīmekļa lietotņu veidošanai ar elegantu lietotāja saskarni.
- **Priekšrocības**:
  - Visaptverošs komponenšu kopums, tostarp tabulas, režģi, diagrammas un veidlapas.
  - Nodrošina gaišā un tumšā režīma atbalstu.
  - Ļoti pielāgojama un viegli paplašināma.
  - Iebūvētas integrācijas diagrammu bibliotēkām, piemēram, `chart.js` vai `d3.js`.
- **Trūkumi**:
  - Var būt smagāka par vienkāršākām komponenšu bibliotēkām.
  - Nepieciešama zināma iestatīšana, lai integrētu ārējās bibliotēkas sarežģītākām funkcijām, piemēram, Ganta diagrammām.
- **Vislabāk piemērota**: projektiem, kuriem nepieciešams visaptverošs, pielāgojams komponenšu kopums.
- **Tabulu/diagrammu atbalsts**: teicams (atbalstītas diagrammu bibliotēkas).
- **Režģu/Ganta atbalsts**: labs (režģu komponentes ir pieejamas; Gantam nepieciešama ārēja integrācija).

### 7. **shadcn-svelte**
- **Pārskats**: ShadCN Svelte versija, kas koncentrējas uz utilītu pirmo dizainu (utility-first) un nodrošina modernas, noformētas komponentes.
- **Priekšrocības**:
  - Utilītu pirmais dizains, veidots uz Tailwind CSS, padarot to viegli pielāgojamu.
  - Bagāts komponenšu kopums, pilnībā noformēts uzreiz.
  - Viegli integrējama ar citām bibliotēkām.
- **Trūkumi**:
  - Nav tik funkcionāli pilnīga kā dažas citas attiecībā uz uzlabotiem UI elementiem.
  - Trūkst iebūvēta atbalsta tabulām, diagrammām vai režģiem.
  - Nav tiešā atbalsta Ganta diagrammām.
- **Vislabāk piemērota**: maziem līdz vidējiem projektiem, kuriem nepieciešama utilītu pirmā, pielāgojama pieeja.
- **Tabulu/diagrammu atbalsts**: minimāls.
- **Režģu/Ganta atbalsts**: minimāls.

## Lēmums

### Ieteicamā iespēja: **SvelteUI**

- **Pamatojums**: SvelteUI piedāvā līdzsvarotu, visaptverošu komponenšu komplektu, kas apmierina vajadzību pēc tabulām, diagrammām, režģiem un veidlapām. Tā ir ļoti pielāgojama, labi integrējas ar citām diagrammu bibliotēkām (piemēram, `chart.js` un `d3.js`) un tai ir labs līdzsvars starp vieglu veiktspēju un funkciju bagātību. Lai gan tā var nenodrošināt tiešu Ganta diagrammu atbalstu, to var viegli paplašināt ar trešo pušu integrācijām, padarot to ideālu pilnu funkciju mērogojamam risinājumam.
  
  - **Priekšrocības**:
    - Teicams tabulu un diagrammu atbalsts.
    - Pilnas režģu un izkārtojuma komponentes.
    - Pielāgojama un labi integrējas ar ārējām diagrammu bibliotēkām.
    - Laba kopiena un dokumentācija.
  
  - **Trūkumi**:
    - Smagāka nekā dažas citas minimālistiskas bibliotēkas.
    - Sarežģītām diagrammām, piemēram, Ganta diagrammām, nepieciešama ārēja integrācija.
  
### Alternatīva: **Flowbite** vai **Carbon** (lielākiem uzņēmumu projektiem)
- Ja nepieciešama izsmalcināta, uz Tailwind balstīta vai konsekventāka dizaina sistēma, piemērotas alternatīvas var būt **Flowbite** (ar Tailwind CSS) vai **Carbon** (uzņēmuma līmeņa risinājumiem). Tomēr tām var būt nepieciešamas papildu pūles integrācijām ar sarežģītākām diagrammām un komponentēm.

## Secinājums

Vislabākā izvēle jūsu prasībām (pilnas funkcijas tabulām, diagrammām, sarakstiem, režģiem, Gantam) ir **SvelteUI**, kam seko **Flowbite** un **Carbon**, atkarībā no projekta vajadzībām un dizaina preferencēm.