# Svelte osagaietarako arkitektura-erabakien erregistroa (ADR)

<!--

Prompt:

Architecture decision record for Svelte components.

Compare options: SVAR, Carbon, Flowbite, SkeletonUI, MeltUI, SvelteUI, shadcn-svelte

The goal is full features for table, charts, lists, grids, gantt, 

-->

## Testuingurua

Svelte UI osagai-liburutegi bat aukeratzen ari gara ezaugarri osoak eskaintzeko hauetarako:
- **Taulak**
- **Diagramak**
- **Zerrendak**
- **Sareak**
- **Gantt diagramak**

Helburua integrazio-erraztasuna, ezaugarri osoen euskarria, errendimendua eta epe luzerako mantentzeko gaitasuna orekatzen dituen liburutegi bat aukeratzea da. Aztertzen ari diren aukerak hauek dira:

1. **SVAR**
2. **Carbon**
3. **Flowbite**
4. **SkeletonUI**
5. **MeltUI**
6. **SvelteUI**
7. **shadcn-svelte**

## Aukeren analisia

### 1. **SVAR**
- **Ikuspegi orokorra**: SVAR Svelte-rako osagai-liburutegi modernoa eta ezaugarri-aberatsa da, diseinu-sistemetan eta enpresa-mailako osagaietan zentratua.
- **Alde onak**:
  - Osagai ezaugarri-oso, taulak, formularioak eta diagramak barne.
  - Pertsonalizazio-aukera handiak, gai-euskarri integratuarekin.
  - Irisgarritasunerako eta erantzuteko gaitasunerako euskarri integratua.
  - Ondo dokumentatua, komunitatearen ekarpenekin.
- **Alde txarrak**:
  - Beste liburutegi sinpleago batzuekin alderatuta astunagoa izan daiteke.
  - Euskarri mugatua Gantt diagramak eta sare aurreratuak bezalako osagai jakinetarako.
- **Egokiena**: Diseinu-sistema oso bat beharrezkoa den enpresa-mailako aplikazioak.
- **Taula/Diagrama euskarria**: Ertainetik onera.
- **Sare/Gantt euskarria**: Minimoa.

### 2. **Carbon**
- **Ikuspegi orokorra**: Carbon Design System IBM-en diseinu-sistema irekia da, UI osagai multzo sendoa eskaintzen duena.
- **Alde onak**:
  - Diseinu landua eta kalitate handikoa, dokumentazio zabalarekin.
  - Oso irisgarria eta erantzunkorra.
  - Osagai-liburutegi handia, sareak, taulak eta formulario-kontrolak barne.
- **Alde txarrak**:
  - Ez dago Svelte-n zentratua, beraz integrazioa neketsua izan daiteke.
  - Pertsonalizazio gehigarria behar izan dezake Svelte bateragarritasun osorako.
  - Kutxatik kanpoko euskarririk ez Gantt diagramak edo diagrama konplexuak bezalako osagai aurreratuetarako.
- **Egokiena**: Eskala handiko proiektuak UI koherente eta landu bat behar dutenak.
- **Taula/Diagrama euskarria**: Ona (diagrama-liburutegien integrazioekin).
- **Sare/Gantt euskarria**: Ona (sare-euskarria eskuragarri, baina Gantt diagramarik ez).

### 3. **Flowbite**
- **Ikuspegi orokorra**: Flowbite Tailwind CSS-ekin eraikitako osagai-liburutegia da, osagai eta UI elementu anitz eskaintzen dituena.
- **Alde onak**:
  - Tailwind CSS oinarritua, pertsonalizatzeko erraza dena.
  - Svelte-rekin integratzeko eta erabiltzeko erraza.
  - Osagai aberatsak eskaintzen ditu, hala nola taulak, diagramak eta UI kontrolak.
- **Alde txarrak**:
  - Ezaugarri aurreratuak falta ditu (adib. Gantt diagramak edo sare konplexuak).
  - Ez du diagrama-osagai natiborik; kanpoko liburutegien mende dago.
- **Egokiena**: Garapen azkarra behar duten proiektuak, Tailwind CSS integrazioan zentratuta.
- **Taula/Diagrama euskarria**: Ona (hirugarrenen diagrama-liburutegiekin integrazioa behar du).
- **Sare/Gantt euskarria**: Minimoa.

### 4. **SkeletonUI**
- **Ikuspegi orokorra**: SkeletonUI Svelte-rako osagai-liburutegi arina da, sinpletasunean eta minimalismoan zentratua.
- **Alde onak**:
  - Oso arina eta azkarra.
  - API sinplea eta intuitiboa.
  - Proiektu txikietarako edo errendimendua kritikoa den lekuetarako ona.
- **Alde txarrak**:
  - Osagai oso gutxi sartzen dira, beraz ez da ezaugarri-aberatsa.
  - Taula/sare/diagrama/Gantt osagai aurreratuak falta ditu.
  - Komunitate-laguntza mugatua eta dokumentazio ez hain osoa.
- **Egokiena**: Gastu minimoko osagai arinak behar dituzten proiektuak.
- **Taula/Diagrama euskarria**: Minimoa.
- **Sare/Gantt euskarria**: Minimoa.

### 5. **MeltUI**
- **Ikuspegi orokorra**: MeltUI Svelte-rako UI osagai irisgarrien bilduma da, sinpletasunean eta konposagarritasunean zentratua.
- **Alde onak**:
  - Arina eta guztiz pertsonalizagarria.
  - Irisgarritasun-ezaugarri onak kutxatik kanpo.
  - Diseinu modernoa eta minimalista.
- **Alde txarrak**:
  - Beste liburutegiekin alderatuta ezaugarri gutxiagokoa.
  - Sare eta taula aurreratuak falta ditu.
  - Ez du Gantt diagramarik edo diagrama-aukera konplexurik.
- **Egokiena**: Irisgarritasuna eta errendimendua lehenesten dituzten diseinu minimalistak.
- **Taula/Diagrama euskarria**: Minimoa.
- **Sare/Gantt euskarria**: Minimoa.

### 6. **SvelteUI**
- **Ikuspegi orokorra**: SvelteUI Svelte-rako UI osagai-liburutegi oso eta pertsonalizagarria da, UI dotorearekin web aplikazio modernoak eraikitzeko diseinatua.
- **Alde onak**:
  - Osagai multzo osoa, taulak, sareak, diagramak eta formularioak barne.
  - Modu argia eta iluna onartzen ditu.
  - Oso pertsonalizagarria eta hedatzeko erraza.
  - `chart.js` edo `d3.js` bezalako diagrama-liburutegientzako integrazio integratuak.
- **Alde txarrak**:
  - Osagai-liburutegi sinpleagoak baino astunagoa izan daiteke.
  - Konfigurazio batzuk behar ditu kanpoko liburutegiak integratzeko Gantt diagramak bezalako ezaugarri konplexuagoetarako.
- **Egokiena**: Osagai multzo oso eta pertsonalizagarria behar duten proiektuak.
- **Taula/Diagrama euskarria**: Bikaina (diagrama-liburutegiak onartzen dira).
- **Sare/Gantt euskarria**: Ona (sare-osagaiak eskuragarri; Gantt-ek kanpoko integrazioa behar du).

### 7. **shadcn-svelte**
- **Ikuspegi orokorra**: ShadCN-en Svelte bertsioa, utility-first diseinuan zentratzen dena eta osagai moderno eta estilatuak eskaintzen dituena.
- **Alde onak**:
  - Utility-first diseinua, Tailwind CSS-en gainean eraikia, pertsonalizatzeko erraza egiten duena.
  - Osagai multzo aberatsa eta kutxatik kanpo guztiz estilatua.
  - Beste liburutegiekin integratzeko erraza.
- **Alde txarrak**:
  - Ez da beste batzuk bezain ezaugarri-osoa UI elementu aurreratuen aldetik.
  - Taula, diagrama edo sareetarako euskarri integratua falta du.
  - Ez dago kutxatik kanpoko euskarririk Gantt diagrametarako.
- **Egokiena**: Utility-first, pertsonalizagarria den ikuspegia behar duten proiektu txiki-ertainak.
- **Taula/Diagrama euskarria**: Minimoa.
- **Sare/Gantt euskarria**: Minimoa.

## Erabakia

### Gomendatutako aukera: **SvelteUI**

- **Arrazoibidea**: SvelteUI-k osagai multzo orekatu eta oso bat eskaintzen du, taulen, diagramen, sareen eta formularioen beharra asetzen duena. Oso pertsonalizagarria da, kanpoko diagrama-liburutegiekin ondo integratzen da (`chart.js` eta `d3.js` bezalakoak), eta errendimendu arinaren eta ezaugarri-aberastasunaren arteko oreka ona du. Kutxatik kanpo Gantt diagrama euskarria ez eskaini arren, erraz hedatu daiteke hirugarrenen integrazioekin, eta horrek ezin hobea egiten du soluzio oso eta eskalagarri baterako.
  
  - **Alde onak**:
    - Taula eta diagrama euskarri bikaina.
    - Sare eta diseinu osagai osoak.
    - Pertsonalizagarria eta kanpoko diagrama-liburutegiekin ondo integratzen da.
    - Komunitate eta dokumentazio ona.
  
  - **Alde txarrak**:
    - Beste liburutegi minimalista batzuk baino astunagoa.
    - Kanpoko integrazioa behar du Gantt diagramak bezalako diagrama konplexuetarako.
  
### Alternatiba: **Flowbite** edo **Carbon** (enpresa-proiektu handiagoetarako)
- Diseinu-sistema landu, Tailwind-en oinarritutako edo koherenteago bat behar bada, **Flowbite** (Tailwind CSS-ekin) edo **Carbon** (enpresa-mailako soluzioetarako) alternatiba egokiak izan daitezke. Hala ere, ahalegin gehigarria behar izan dezakete diagrama eta osagai konplexuagoekin integratzeko.

## Ondorioa

Zure eskakizunetarako (taulen, diagramen, zerrenden, sareen, Gantt-en ezaugarri osoak) aukerarik egokiena **SvelteUI** da, jarraian **Flowbite** eta **Carbon** proiektuaren beharren eta diseinu-lehentasunen arabera.
