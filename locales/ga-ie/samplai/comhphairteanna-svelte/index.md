# Taifead Cinnidh Ailtireachta (ADR) do Chomhpháirteanna Svelte

<!--

Prompt:

Architecture decision record for Svelte components.

Compare options: SVAR, Carbon, Flowbite, SkeletonUI, MeltUI, SvelteUI, shadcn-svelte

The goal is full features for table, charts, lists, grids, gantt, 

-->

## Comhthéacs

Táimid ag roghnú leabharlann comhpháirteanna UI Svelte chun gnéithe iomlána a sholáthar do:
- **Táblaí**
- **Cairteacha**
- **Liostaí**
- **Greillí**
- **Cairteacha Gantt**

Is é an sprioc leabharlann a roghnú a chothromaíonn éascaíocht comhtháthaithe, tacaíocht iomlán do ghnéithe, feidhmíocht, agus inchothabháilteacht fhadtéarmach. Is iad seo a leanas na roghanna atá á mbreithniú:

1. **SVAR**
2. **Carbon**
3. **Flowbite**
4. **SkeletonUI**
5. **MeltUI**
6. **SvelteUI**
7. **shadcn-svelte**

## Anailís Roghanna

### 1. **SVAR**
- **Forbhreathnú**: Is leabharlann comhpháirteanna nua-aimseartha, saibhir i ngnéithe é SVAR do Svelte, le fócas ar chórais dearaidh agus comhpháirteanna atá réidh don fhiontar.
- **Buntáistí**:
  - Comhpháirteanna lánghnéitheacha, lena n-áirítear táblaí, foirmeacha, agus cairteacha.
  - Roghanna ard-saincheaptha le tacaíocht téama ionsuite.
  - Tacaíocht ionsuite d'inrochtaineacht agus d'fhreagrúlacht.
  - Doiciméadaithe go maith le ranníocaíochtaí ón bpobal.
- **Míbhuntáistí**:
  - D'fhéadfadh sé a bheith níos troime i gcomparáid le leabharlanna níos simplí eile.
  - Tacaíocht theoranta do chomhpháirteanna ar leith cosúil le cairteacha Gantt agus greillí casta.
- **Is Fearr Do**: Feidhmchláir ar leibhéal fiontair ina bhfuil córas dearaidh lánghnéitheach riachtanach.
- **Tacaíocht Tábla/Cairt**: Measartha go maith.
- **Tacaíocht Greille/Gantt**: Íosta.

### 2. **Carbon**
- **Forbhreathnú**: Is córas dearaidh foinse oscailte ó IBM é Carbon Design System, a thairgeann tacar láidir comhpháirteanna UI.
- **Buntáistí**:
  - Dearadh ardchaighdeáin, snasta le doiciméadú fairsing.
  - An-inrochtana agus freagrúil.
  - Leabharlann mhór comhpháirteanna, lena n-áirítear greillí, táblaí, agus rialuithe foirme.
- **Míbhuntáistí**:
  - Níl fócas ar Svelte, mar sin d'fhéadfadh comhtháthú a bheith trom.
  - D'fhéadfadh saincheapadh breise a bheith ag teastáil le haghaidh comhoiriúnacht iomlán Svelte.
  - Gan tacaíocht ionsuite do chomhpháirteanna casta cosúil le cairteacha Gantt nó cairteacha casta.
- **Is Fearr Do**: Tionscadail mhórscála a éilíonn UI comhsheasmhach, snasta.
- **Tacaíocht Tábla/Cairt**: Go maith (le comhtháthaithe leabharlainne cairteacha).
- **Tacaíocht Greille/Gantt**: Go maith (tacaíocht greille ar fáil, ach gan cairteacha Gantt).

### 3. **Flowbite**
- **Forbhreathnú**: Is leabharlann comhpháirteanna í Flowbite atá tógtha le Tailwind CSS, a thairgeann comhpháirteanna agus eilimintí UI éagsúla.
- **Buntáistí**:
  - Bunaithe ar Tailwind CSS, rud a fhágann go bhfuil sé éasca a shaincheapadh.
  - Éasca a chomhtháthú agus a úsáid le Svelte.
  - Soláthraíonn comhpháirteanna saibhre cosúil le táblaí, cairteacha, agus rialuithe UI.
- **Míbhuntáistí**:
  - Easpa gnéithe casta (m.sh., cairteacha Gantt nó greillí casta).
  - Níl comhpháirteanna cairte dúchasacha aige; brath ar leabharlanna seachtracha.
- **Is Fearr Do**: Tionscadail a éilíonn forbairt thapa le fócas ar chomhtháthú Tailwind CSS.
- **Tacaíocht Tábla/Cairt**: Go maith (éilíonn comhtháthú le leabharlanna cairteacha tríú páirtí).
- **Tacaíocht Greille/Gantt**: Íosta.

### 4. **SkeletonUI**
- **Forbhreathnú**: Is leabharlann comhpháirteanna éadrom é SkeletonUI do Svelte, le fócas ar shimplíocht agus ar íostachas.
- **Buntáistí**:
  - Thar a bheith éadrom agus tapa.
  - API simplí agus intuigthe.
  - Go maith do thionscadail bheaga nó nuair atá feidhmíocht ríthábhachtach.
- **Míbhuntáistí**:
  - Tá an-bheagán comhpháirteanna san áireamh, mar sin níl sé saibhir i ngnéithe.
  - Easpa comhpháirteanna casta tábla/greille/cairte/Gantt.
  - Tacaíocht theoranta ón bpobal agus doiciméadú níos lú cuimsitheach.
- **Is Fearr Do**: Tionscadail a éilíonn comhpháirteanna éadroma le forchostais íosta.
- **Tacaíocht Tábla/Cairt**: Íosta.
- **Tacaíocht Greille/Gantt**: Íosta.

### 5. **MeltUI**
- **Forbhreathnú**: Is bailiúchán de chomhpháirteanna UI inrochtana é MeltUI do Svelte, le fócas ar shimplíocht agus ar infhoirmiúlacht.
- **Buntáistí**:
  - Éadrom agus go hiomlán inchustaimithe.
  - Gnéithe maithe inrochtaineachta amach as an mbosca.
  - Dearadh nua-aimseartha agus íostach.
- **Míbhuntáistí**:
  - Níos lú saibhir i ngnéithe i gcomparáid le leabharlanna eile.
  - Easpa comhpháirteanna casta greille agus tábla.
  - Gan cairteacha Gantt nó roghanna cairte casta.
- **Is Fearr Do**: Dearaí íostacha a thugann tosaíocht d'inrochtaineacht agus d'fheidhmíocht.
- **Tacaíocht Tábla/Cairt**: Íosta.
- **Tacaíocht Greille/Gantt**: Íosta.

### 6. **SvelteUI**
- **Forbhreathnú**: Is leabharlann comhpháirteanna UI cuimsitheach agus inchustaimithe é SvelteUI do Svelte, deartha chun aipeanna gréasáin nua-aimseartha a thógáil le UI galánta.
- **Buntáistí**:
  - Tacar cuimsitheach comhpháirteanna, lena n-áirítear táblaí, greillí, cairteacha, agus foirmeacha.
  - Soláthraíonn sé tacaíocht mód éadrom agus dorcha.
  - An-inchustaimithe agus éasca a leathnú.
  - Comhtháthaithe ionsuite do leabharlanna cairteacha cosúil le `chart.js` nó `d3.js`.
- **Míbhuntáistí**:
  - Féadann sé a bheith níos troime ná leabharlanna comhpháirteanna níos simplí.
  - Éilíonn roinnt socraithe chun leabharlanna seachtracha a chomhtháthú le haghaidh gnéithe níos casta cosúil le cairteacha Gantt.
- **Is Fearr Do**: Tionscadail a bhfuil tacar cuimsitheach, inchustaimithe comhpháirteanna ag teastáil uathu.
- **Tacaíocht Tábla/Cairt**: Sármhaith (tacaítear le leabharlanna cairteacha).
- **Tacaíocht Greille/Gantt**: Go maith (comhpháirteanna greille ar fáil; teastaíonn comhtháthú seachtrach ó Gantt).

### 7. **shadcn-svelte**
- **Forbhreathnú**: Leagan Svelte de ShadCN, a dhíríonn ar dhearadh utility-first agus a sholáthraíonn comhpháirteanna nua-aimseartha, stílithe.
- **Buntáistí**:
  - Dearadh utility-first, tógtha ar bharr Tailwind CSS, rud a fhágann go bhfuil sé éasca a shaincheapadh.
  - Tacar saibhir comhpháirteanna agus iad go hiomlán stílithe amach as an mbosca.
  - Éasca a chomhtháthú le leabharlanna eile.
- **Míbhuntáistí**:
  - Níl sé chomh lánghnéitheach le cinn eile maidir le heilimintí UI casta.
  - Easpa tacaíochta ionsuite do tháblaí, cairteacha, nó greillí.
  - Gan tacaíocht ionsuite do chairteacha Gantt.
- **Is Fearr Do**: Tionscadail bheaga go meánmhéide a éilíonn cur chuige utility-first, inchustaimithe.
- **Tacaíocht Tábla/Cairt**: Íosta.
- **Tacaíocht Greille/Gantt**: Íosta.

## Cinneadh

### An Rogha Mholta: **SvelteUI**

- **Réasúnaíocht**: Tairgeann SvelteUI sraith chuimsitheach, dea-chothromaithe comhpháirteanna a fhreastalaíonn ar an ngá le táblaí, cairteacha, greillí, agus foirmeacha. Tá sé an-inchustaimithe, comhtháthaíonn sé go maith le leabharlanna cairte eile (cosúil le `chart.js` agus `d3.js`), agus tá cothromaíocht mhaith aige idir feidhmíocht éadrom agus saibhreas gnéithe. Cé nach soláthróidh sé tacaíocht cairte Gantt amach as an mbosca, is féidir é a leathnú go héasca le comhtháthaithe tríú páirtí, rud a fhágann go bhfuil sé idéalach do réiteach lánghnéitheach, inscálaithe.
  
  - **Buntáistí**:
    - Tacaíocht den scoth do tháblaí agus do chairteacha.
    - Comhpháirteanna iomlána greille agus leagan amach.
    - Inchustaimithe agus comhtháthaíonn sé go maith le leabharlanna cairteacha seachtracha.
    - Pobal agus doiciméadú maith.
  
  - **Míbhuntáistí**:
    - Níos troime ná roinnt leabharlanna íostacha eile.
    - Teastaíonn comhtháthú seachtrach do chairteacha casta cosúil le cairteacha Gantt.
  
### Rogha eile: **Flowbite** nó **Carbon** (do thionscadail fiontair níos mó)
- Má theastaíonn córas dearaidh snasta, bunaithe ar Tailwind, nó níos comhsheasmhaí, d'fhéadfadh **Flowbite** (le Tailwind CSS) nó **Carbon** (do réitigh ar chaighdeán fiontair) a bheith ina roghanna eile oiriúnacha. Mar sin féin, d'fhéadfadh iarracht bhreise a bheith ag teastáil uathu le haghaidh comhtháthaithe le cairteacha agus comhpháirteanna níos casta.

## Conclúid

Is é **SvelteUI** an oiriúnú is fearr do do riachtanais (gnéithe iomlána do tháblaí, cairteacha, liostaí, greillí, Gantt), agus **Flowbite** agus **Carbon** ina dhiaidh, ag brath ar riachtanais an tionscadail agus ar roghanna dearaidh.