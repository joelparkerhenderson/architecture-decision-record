# Rikodin shawarar gine-gine (ADR) don ɓangarorin Svelte

<!--

Prompt:

Architecture decision record for Svelte components.

Compare options: SVAR, Carbon, Flowbite, SkeletonUI, MeltUI, SvelteUI, shadcn-svelte

The goal is full features for table, charts, lists, grids, gantt, 

-->

## Mahalli

Muna zaɓar laburaren ɓangarorin UI na Svelte don samar da cikakkun siffofi na:
- **Teburori**
- **Zane-zane (charts)**
- **Jeri**
- **Grids**
- **Zane-zanen Gantt**

Manufar ita ce a zaɓi laburare da ke daidaita sauƙin haɗewa, cikakken goyon bayan siffofi, aiki, da dorewar kulawa na dogon lokaci. Zaɓuɓɓukan da ake la’akari da su su ne:

1. **SVAR**
2. **Carbon**
3. **Flowbite**
4. **SkeletonUI**
5. **MeltUI**
6. **SvelteUI**
7. **shadcn-svelte**

## Nazarin Zaɓuɓɓuka

### 1. **SVAR**
- **Bayyani**: SVAR laburaren ɓangarori ne na zamani, mai wadatattun siffofi na Svelte, wanda ya mai da hankali kan tsarukan zane da ɓangarori da suka shirya ga kamfanoni.
- **Fa’idodi**:
  - Cikakkun ɓangarori masu siffofi, ciki har da teburori, fom, da zane-zane.
  - Zaɓuɓɓukan keɓancewa masu yawa tare da goyon bayan jigo na ciki.
  - Goyon baya na ciki ga samun dama da amsawa.
  - An rubuta shi da kyau tare da gudummawar al’umma.
- **Rashin fa’idodi**:
  - Yana iya zama mai nauyi idan aka kwatanta da sauran laburare masu sauƙi.
  - Iyakantaccen goyon baya ga takamaiman ɓangarori kamar zane-zanen Gantt da ci-gaban grids.
- **Mafi dacewa da**: Aikace-aikacen matakin kamfani inda cikakken tsarin zane mai siffofi yake da muhimmanci.
- **Goyon bayan Tebur/Zane**: Matsakaici zuwa mai kyau.
- **Goyon bayan Grid/Gantt**: Kaɗan.

### 2. **Carbon**
- **Bayyani**: Carbon Design System tsarin zane ne na buɗaɗɗen tushe daga IBM, wanda ke ba da ƙaƙƙarfan jerin ɓangarorin UI.
- **Fa’idodi**:
  - Zane mai inganci, mai kyau tare da cikakkun takardu.
  - Mai sauƙin samun dama da amsawa sosai.
  - Babban laburaren ɓangarori, ciki har da grids, teburori, da sarrafa fom.
- **Rashin fa’idodi**:
  - Bai mai da hankali kan Svelte ba, don haka haɗewa na iya zama mai wahala.
  - Zai iya buƙatar ƙarin keɓancewa don cikakken dacewa da Svelte.
  - Babu goyon baya na asali ga ci-gaban ɓangarori kamar zane-zanen Gantt ko sarƙaƙƙun zane-zane.
- **Mafi dacewa da**: Manyan ayyuka da ke buƙatar UI mai daidaito da kyau.
- **Goyon bayan Tebur/Zane**: Mai kyau (tare da haɗewar laburaren zane).
- **Goyon bayan Grid/Gantt**: Mai kyau (akwai goyon bayan Grid, amma babu zane-zanen Gantt).

### 3. **Flowbite**
- **Bayyani**: Flowbite laburaren ɓangarori ne da aka gina da Tailwind CSS, yana ba da ɓangarori da abubuwan UI daban-daban.
- **Fa’idodi**:
  - Na tushen Tailwind CSS, wanda ke sauƙaƙa keɓancewa.
  - Mai sauƙin haɗewa da amfani da Svelte.
  - Yana ba da wadatattun ɓangarori kamar teburori, zane-zane, da sarrafa UI.
- **Rashin fa’idodi**:
  - Ba shi da ci-gaban siffofi (misali zane-zanen Gantt ko sarƙaƙƙun grids).
  - Ba shi da ɓangarorin zane na asali; yana dogara da laburare na waje.
- **Mafi dacewa da**: Ayyukan da ke buƙatar ci gaba cikin sauri tare da mai da hankali kan haɗewar Tailwind CSS.
- **Goyon bayan Tebur/Zane**: Mai kyau (yana buƙatar haɗewa da laburaren zane na wasu kamfanoni).
- **Goyon bayan Grid/Gantt**: Kaɗan.

### 4. **SkeletonUI**
- **Bayyani**: SkeletonUI laburaren ɓangarori ne mai nauyi ƙanƙani na Svelte, wanda ya mai da hankali kan sauƙi da ƙaranci.
- **Fa’idodi**:
  - Mai nauyi ƙanƙani sosai kuma mai sauri.
  - API mai sauƙi kuma mai fahimta.
  - Mai kyau ga ƙananan ayyuka ko inda aiki yake da muhimmanci.
- **Rashin fa’idodi**:
  - Ɓangarori kaɗan ne kawai aka haɗa, don haka bai da wadatattun siffofi ba.
  - Ba shi da ci-gaban ɓangarorin tebur/grid/zane/Gantt.
  - Iyakantaccen tallafin al’umma da takardu marasa cikawa.
- **Mafi dacewa da**: Ayyukan da ke buƙatar ɓangarori masu nauyi ƙanƙani da ƙaramin nauyin ƙari.
- **Goyon bayan Tebur/Zane**: Kaɗan.
- **Goyon bayan Grid/Gantt**: Kaɗan.

### 5. **MeltUI**
- **Bayyani**: MeltUI tarin ɓangarorin UI ne masu sauƙin samun dama na Svelte, wanda ya mai da hankali kan sauƙi da iya haɗawa.
- **Fa’idodi**:
  - Mai nauyi ƙanƙani kuma gabaɗaya mai keɓancewa.
  - Kyawawan siffofin samun dama daga cikin akwatin.
  - Zane na zamani da ƙaranci.
- **Rashin fa’idodi**:
  - Ba shi da wadatattun siffofi idan aka kwatanta da sauran laburare.
  - Ba shi da ci-gaban ɓangarorin grid da tebur.
  - Babu zane-zanen Gantt ko sarƙaƙƙun zaɓuɓɓukan zane.
- **Mafi dacewa da**: Zane-zane masu ƙaranci waɗanda ke fifita samun dama da aiki.
- **Goyon bayan Tebur/Zane**: Kaɗan.
- **Goyon bayan Grid/Gantt**: Kaɗan.

### 6. **SvelteUI**
- **Bayyani**: SvelteUI cikakken laburaren ɓangarorin UI ne mai keɓancewa na Svelte, wanda aka ƙirƙira don gina aikace-aikacen yanar gizo na zamani da UI mai kyau.
- **Fa’idodi**:
  - Cikakken tarin ɓangarori, ciki har da teburori, grids, zane-zane, da fom.
  - Yana ba da goyon baya ga yanayin haske da duhu duka.
  - Mai keɓancewa sosai kuma mai sauƙin faɗaɗawa.
  - Haɗewa ta ciki da laburaren zane kamar `chart.js` ko `d3.js`.
- **Rashin fa’idodi**:
  - Zai iya zama mai nauyi fiye da laburaren ɓangarori masu sauƙi.
  - Yana buƙatar wani saiti don haɗa laburare na waje don siffofi masu sarƙaƙiya kamar zane-zanen Gantt.
- **Mafi dacewa da**: Ayyukan da ke buƙatar cikakken tarin ɓangarori mai keɓancewa.
- **Goyon bayan Tebur/Zane**: Mafi kyau (ana goyon bayan laburaren zane).
- **Goyon bayan Grid/Gantt**: Mai kyau (akwai ɓangarorin Grid; Gantt yana buƙatar haɗewa ta waje).

### 7. **shadcn-svelte**
- **Bayyani**: Sigar Svelte ta ShadCN, wacce ta mai da hankali kan zane na fifita kayan amfani kuma tana ba da ɓangarori na zamani masu salo.
- **Fa’idodi**:
  - Zane na fifita kayan amfani, wanda aka gina a kan Tailwind CSS, yana sauƙaƙa keɓancewa.
  - Wadatattun ɓangarori masu salo gabaɗaya daga cikin akwatin.
  - Mai sauƙin haɗewa da sauran laburare.
- **Rashin fa’idodi**:
  - Bai cika siffofi kamar wasu ba ta fuskar ci-gaban abubuwan UI.
  - Ba shi da goyon baya na ciki ga teburori, zane-zane, ko grids.
  - Babu goyon baya na asali ga zane-zanen Gantt.
- **Mafi dacewa da**: Ƙanana zuwa matsakaitan ayyuka da ke buƙatar hanyar fifita kayan amfani mai keɓancewa.
- **Goyon bayan Tebur/Zane**: Kaɗan.
- **Goyon bayan Grid/Gantt**: Kaɗan.

## Shawara

### Zaɓin da Aka Ba da Shawara: **SvelteUI**

- **Dalili**: SvelteUI yana ba da cikakken tarin ɓangarori mai daidaito wanda ke biyan buƙatar teburori, zane-zane, grids, da fom. Yana da keɓancewa sosai, yana haɗewa da kyau da sauran laburaren zane (kamar `chart.js` da `d3.js`), kuma yana da kyakkyawan daidaito tsakanin aiki mai nauyi ƙanƙani da wadatar siffofi. Ko da yake bazai iya ba da goyon bayan zane-zanen Gantt na asali ba, ana iya faɗaɗa shi cikin sauƙi da haɗewar wasu kamfanoni, wanda ya sa ya dace da cikakkiyar mafita mai iya faɗaɗuwa.
  
  - **Fa’idodi**:
    - Kyakkyawan goyon bayan tebur da zane.
    - Cikakkun ɓangarorin grid da tsari.
    - Mai keɓancewa kuma yana haɗewa da kyau da laburaren zane na waje.
    - Kyakkyawar al’umma da takardu.
  
  - **Rashin fa’idodi**:
    - Ya fi nauyi fiye da wasu laburare masu ƙaranci.
    - Yana buƙatar haɗewa ta waje don sarƙaƙƙun zane-zane kamar zane-zanen Gantt.
  
### Madadin: **Flowbite** ko **Carbon** (don manyan ayyukan kamfanoni)
- Idan ana buƙatar tsarin zane mai kyau, na tushen Tailwind, ko mafi daidaito, **Flowbite** (da Tailwind CSS) ko **Carbon** (don mafita na matakin kamfani) na iya zama madadin da suka dace. Duk da haka, suna iya buƙatar ƙarin ƙoƙari don haɗewa da sarƙaƙƙun zane-zane da ɓangarori.

## Kammalawa

Mafi dacewa da buƙatunku (cikakkun siffofi na teburori, zane-zane, jeri, grids, Gantt) shi ne **SvelteUI**, sai **Flowbite** da **Carbon** bisa buƙatun aiki da fifikon zane.
