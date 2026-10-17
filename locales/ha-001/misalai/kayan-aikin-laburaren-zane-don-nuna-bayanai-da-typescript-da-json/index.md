# Rikodin shawarar gine-gine: kayan aikin laburaren zane don nuna bayanai da TypeScript da JSON

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

**Babban Manufa:**  
Zaɓar ci-gaban kayan aikin zane don ƙirƙirar nuni masu mu’amala, mai mai da hankali kan bayanan kuɗi, bayanan kimiyya, da bayanan gwamnati ta amfani da TypeScript da JSON. Ya kamata laburaren ya samar da ƙaƙƙarfan siffofi, sassauci, kuma ya kasance buɗaɗɗen tushe. 

### Mahalli da Buƙatu:

1. **Ci Gaba Mai Sassauci (Fifiko Mai Girma)**: A matsayin sabuwar kamfani, saurin maimaitawa, yin samfurin gwaji, da sassauci a ci gaba suna da muhimmanci. Dole ne laburaren zane ya ba da damar zagayen ci gaba masu sauri.
   
2. **Nau’ikan Zane (Fifiko Mai Girma)**:
   - **Zanen Doughnut**
   - **Zanen Radar**
   - **Zanen Tsarin Taruwa (Clustering Process Chart)**
   - **Zanen Area mai Axis na Lokaci**
   - **Zanen Candlestick**
   - **Zanen Nightingale**
   - **Taswirar Geo SVG**
   
   Waɗannan nau’ikan zane suna da muhimmanci musamman wajen nuna sarƙaƙƙun tarin bayanai, kamar yanayin kuɗi, ma’aunin kimiyya, da bayanan ƙasa.

3. **Kyauta Kuma Buɗaɗɗen Tushe (Fifiko Mai Girma)**: Ya kamata kayan aikin ya zama buɗaɗɗen tushe don guje wa kuɗin lasisi, samar da bayyana, kuma ya ba da sassauci don keɓancewa.

4. **Ma’aunin Ƙaramin Muhimmanci**:
   - **Gudun Lokacin Aiki**: Ko da yake aiki yana da dacewa, ba shi ne babban fifiko ga wannan shawara ba.
   - **Iya Faɗaɗuwa**: Ko da yake iya faɗaɗuwa gabaɗaya yana da muhimmanci, buƙatar yanzu ita ce gina MVP wanda zai iya girma a kan lokaci. Ana iya magance damuwar iya faɗaɗuwa daga baya.
   - **Dacewa da Baya**: Ba babban damuwa ba ne ga ginin farko, matuƙar laburaren na zamani ne kuma ana kula da shi sosai.

### Laburaren da Aka Kimanta:

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

**Bayyani**:  
Apache ECharts ƙaƙƙarfan laburaren zane ne mai sassauci don nuni masu mu’amala, masu keɓancewa. Yana ba da goyon baya ga nau’ikan zane iri-iri kuma yana da ƙarfi musamman a cikin sarƙaƙƙun nuni masu motsi.

**Ƙarfi**:
- **Ci-gaban Mu’amala**: ECharts ya yi fice wajen samar da zane-zane masu mu’amala, yana ba da siffofi kamar zuƙowa, ja, da sabuntawar bayanai masu motsi.
- **Doughnut, Radar, Candlestick, Taswirar Geo SVG**: ECharts yana goyon bayan yawancin nau’ikan zanen da ake buƙata, ciki har da doughnut, radar, candlestick, da nuni na taswirar ƙasa.
- **Kyauta Kuma Buɗaɗɗen Tushe**: ECharts laburare ne na buɗaɗɗen tushe, wanda ya dace da yanayin sabuwar kamfani mai kula da kasafi kuma yana ba da ’yancin gyara lamba.
- **Sassauci da Iya Faɗaɗuwa**: Mai keɓancewa sosai, tare da goyon baya mai yawa ga motsin hoto, nuni na musamman, da ci-gaban dabarun zane.
  
**Rauni**:
- **Lokacin Koyo**: ECharts, ko da yake yana da ƙarfi, na iya samun lokacin koyo mai tsayi saboda sassaucinsa da API mai yawa.
- **Sarƙaƙiyar Takardu**: Takardun cikakku ne amma na iya zama masu nauyi ga masu haɓakawa da suka fara amfani da shi.

**Hukunci**:  
ECharts ya dace sosai da aikin saboda goyon bayansa ga zane-zane masu mu’amala, ciki har da dukkan nau’ikan da ake buƙata kamar zanen candlestick, zanen radar, da taswirar geo. Yanayinsa na buɗaɗɗen tushe ya dace da buƙatar aikin ta sassauci da rashin tsada.

---

### 2. **Chart.js**

**Bayyani**:  
Chart.js laburaren zane ne mai sauƙi, mai sauƙin amfani don gina nau’ikan zane na yau da kullum. An san shi da sauƙinsa da sauƙin haɗewa.

**Ƙarfi**:
- **Sauƙin Amfani**: Chart.js yana da sauƙin kafawa da amfani sosai, tare da ƙaramin lokacin koyo.
- **Buɗaɗɗen Tushe**: Chart.js kyauta ne kuma buɗaɗɗen tushe, wanda yake da muhimmanci wajen rage kuɗi.
- **Nau’ikan Zane na Yau da Kullum**: Yana goyon bayan zane na asali kamar doughnut, area, radar, da layi, waɗanda ke rufe mafi yawan manyan buƙatu.

**Rauni**:
- **Iyakantattun Ci-gaban Zane**: Chart.js ba ya goyon bayan sarƙaƙƙun nau’ikan zane kamar candlestick, taswirar geo SVG, ko zanen tsarin taruwa a asali. Ko da yake ana iya ƙara waɗannan siffofi ta plugins ko keɓancewa, ba shi da sauƙi kamar a sauran laburare.
- **Mu’amala**: Ko da yake Chart.js yana goyon bayan mu’amala ta asali (misali, tooltips da tasirin hover), ba ya ba da ci-gaban siffofi kamar ECharts ko D3.js.

**Hukunci**:  
Chart.js yana da kyau ga ayyuka masu sauƙi, masu sauri, amma rashin goyon bayansa ga sarƙaƙƙun nau’ikan zane ya sa bai dace da aikace-aikace masu yawan bayanai da ke da ci-gaban buƙatu kamar zanen candlestick da taswirar geo ba. Zaɓi ne mai kyau don yin samfurin gwaji, amma ga nau’ikan zanen da ake buƙata, ana ba da shawarar ƙarin ci-gaban kayan aiki.

---

### 3. **ApexCharts**

**Bayyani**:  
ApexCharts laburaren zane ne na zamani wanda ke ba da nau’ikan zane iri-iri kuma ya mai da hankali kan nuni masu mu’amala tare da API mai sauƙin amfani.

**Ƙarfi**:
- **Siffofin Mu’amala**: ApexCharts yana ba da zane-zane masu mu’amala tare da tooltips, zuƙowa, ja, da sabuntawa.
- **Goyon Baya Ga Zane na Kuɗi da Kimiyya**: Yana goyon bayan nau’ikan zane iri-iri, ciki har da zanen candlestick, zanen radar, da zanen area.
- **Sauƙin Amfani**: Yana da API mai sauƙi kuma mai sauƙin haɗawa cikin aiki.
- **Kyauta Kuma Buɗaɗɗen Tushe**: ApexCharts yana ba da sigar buɗaɗɗen tushe kyauta da ta dace da amfani da yawa.
  
**Rauni**:
- **Sarƙaƙƙen Keɓancewa**: Ko da yake yana ba da siffofi da yawa, zaɓuɓɓukan keɓancewa ba su da sassauci kamar ECharts ko D3.js don buƙatun zane masu sarƙaƙiya ko na musamman.
- **Taswirar Geo**: ApexCharts ba ya goyon bayan taswirar geo ko zanen tsarin taruwa a asali, waɗanda ake buƙata don wannan aiki.

**Hukunci**:  
ApexCharts mai takara ne mai ƙarfi saboda sauƙin amfaninsa da mu’amalarsa, amma ya gaza a wasu ci-gaban nau’ikan zane, musamman buƙatar taswirar geo da zanen taruwa. Zaɓi ne mai kyau ga zane masu sauƙi amma ba shi da wasu siffofin da ake buƙata.

---

### 4. **AG Charts**

**Bayyani**:  
AG Charts laburaren zane ne na matakin kasuwanci wanda aka ƙirƙira don aiki da daidaito. Ya dace sosai don ƙirƙirar dashboards na kuɗi, kimiyya, da kasuwanci.

**Ƙarfi**:
- **Ci-gaban Nau’ikan Zane**: AG Charts yana goyon bayan ci-gaban nau’ikan zane da yawa, ciki har da zanen candlestick, zanen area, zanen radar, da ƙari. Yana kuma ba da haɗewa mai zurfi da sauran kayayyakin AG-Grid.
- **Babban Aiki**: Yana ba da kyakkyawan aiki, musamman wajen mu’amala da manyan tarin bayanai.
- **Mu’amala**: AG Charts yana goyon bayan siffofin mu’amala iri-iri kamar zuƙowa, tooltips, da sabuntawa masu motsi.

**Rauni**:
- **Ba Kyauta Gabaɗaya Ba**: Ko da yake AG Charts yana ba da sigar kyauta, cikakkiyar sigar ta kuɗi ce, wanda zai iya zama cikas ga sabbin kamfanoni da ke son rage kuɗi.
- **Sarƙaƙiya**: Ko da yake laburaren yana da wadatattun siffofi, yana iya zama fiye da buƙata ga ayyuka masu sauƙi kuma yana iya buƙatar ƙarin saiti da tsari idan aka kwatanta da sauran zaɓuɓɓuka.

**Hukunci**:  
AG Charts yana da ƙarfi kuma yana da wadatattun siffofi amma bai iya zama mafi dacewa ba saboda yanayinsa na kasuwanci da tsarin kuɗinsa. Dacewarsa tana dogara ne kan ko kasafi zai iya ɗaukar sigogin kuɗi ko ana fifita madadin buɗaɗɗen tushe.

---

### 5. **Highcharts**

**Bayyani**:  
Highcharts shahararren laburaren zane ne da aka san shi da faffadan nau’ikan zane da ƙarfafan zaɓuɓɓukan keɓancewa.

**Ƙarfi**:
- **Cikakkun Nau’ikan Zane**: Highcharts yana goyon bayan zane iri-iri, ciki har da candlestick, radar, area, da taswirar geo.
- **Mai Mu’amala Kuma Mai Motsi**: Highcharts yana ba da wadatattun siffofin mu’amala, ciki har da drill-downs, zuƙowa, da ja.
- **Sauƙin Amfani**: Yana da API mai sauƙin amfani da kyawawan takardu, wanda ke sauƙaƙa farawa.

**Rauni**:
- **Lasisin Kasuwanci**: Ko da yake Highcharts yana ba da sigar kyauta don amfani marar kasuwanci, lasisin kasuwanci yana da tsada, wanda zai iya zama babban koma baya ga sabbin kamfanoni.
- **Lokacin Koyo**: Ko da yake bai kai ECharts tsayi ba, lokacin koyo na Highcharts na iya zama ƙalubale ga masu farawa.

**Hukunci**:  
Highcharts laburare ne mai wadatattun siffofi, amma lasisinsa na kasuwanci ya sa bai dace sosai da ayyukan buɗaɗɗen tushe masu kula da kuɗi ba. Cikakkun zaɓuɓɓukan zanensa fa’ida ne, amma matsalar lasisi tana iyakance jan hankalinsa ga wannan amfani.

---

### 6. **Carbon Charts**

**Bayyani**:  
Carbon Charts laburaren zane ne da IBM ya haɓaka, wanda aka ƙirƙira don ƙirƙirar zane masu kyan gani da keɓancewa sosai.

**Ƙarfi**:
- **Keɓancewa**: Carbon Charts yana ba da damar keɓance siffar zane da halayensa sosai.
- **Buɗaɗɗen Tushe**: Kyauta ne kuma buɗaɗɗen tushe, wanda ya dace da buƙatar aikin ta mafita masu dacewa da kasafi.
- **Goyon Baya Ga Zane na Yau da Kullum**: Yana goyon bayan nau’ikan zane na yau da kullum kamar doughnut, radar, da area, ko da yake ba shi da goyon baya ga ƙarin ci-gaban nau’ikan kamar taswirar geo ko zanen candlestick.

**Rauni**:
- **Iyakantattun Ci-gaban Nau’ikan Zane**: Ba ya goyon bayan taswirar geo, zanen tsarin taruwa, ko zanen candlestick, waɗanda suke da muhimmanci ga aikin.
- **Ƙaramin Tsarin Muhalli**: Carbon Charts yana da ƙaramar al’umma da tsarin muhalli idan aka kwatanta da manyan laburaren zane kamar ECharts ko Highcharts.

**Hukunci**:  
Carbon Charts buɗaɗɗen tushe ne kuma mai keɓancewa amma ba shi da goyon baya ga sarƙaƙƙun nau’ikan zanen da ake buƙata don wannan aiki. Ya fi dacewa da buƙatun zane masu sauƙi.

---

### 7. **Layer Cake**

**Bayyani**:  
Layer Cake laburaren nuna bayanai ne da aka ƙirƙira don ƙirƙirar nuni masu sassauci, masu yadudduka.

**Ƙarfi**:
- **Yadudduka Masu Keɓancewa**: Yana ba da ƙarfafan zaɓuɓɓukan yadudduka don sarƙaƙƙun nuni.
- **Buɗaɗɗen Tushe**: Kyauta ne kuma buɗaɗɗen tushe, yana sa ya zama zaɓi mai yiwuwa ga ayyuka masu kula da kasafi.

**Rauni**:
- **Iyakantattun Takardu**: Layer Cake ba shi da cikakkun takardu da tallafin al’umma, wanda ke sa ya fi wahalar aiki da shi idan aka kwatanta da laburare da suka fi kafuwa.
- **Ba a Gina Shi Don Zane Ba**: Layer Cake ya fi dacewa da nuni marasa zane, don haka zaɓuɓɓukan zanensa daga cikin akwatin iyakantattu ne.

**Hukunci**:  
Ko da yake yana da ban sha’awa ga nuni na musamman, Layer Cake bai dace da buƙatun zane na gargajiya kamar zanen candlestick ko zanen radar ba. Ya fi dacewa da nuni na musamman a wajen fannin zane na ma’auni.

---

### 8. **D3.js**

**Bayyani**:  
D3.js ƙaƙƙarfan laburaren JavaScript ne don ƙirƙirar nuni masu tuƙin bayanai ta hanyar HTML, SVG, da CSS.

**Ƙarfi**:
- **Sassauci Mara Misaltuwa**: D3.js yana ba da damar ƙirƙirar kusan kowane nau’in nuni na musamman, wanda ya sa yake da ƙarfi sosai don ci-gaban zane masu mu’amala.
- **Faffadan Siffofi**: Yana goyon bayan dukkan nau’ikan zanen da ake buƙata, ciki har da taswirar geo, zanen taruwa, da ƙari.
- **Mai Keɓancewa**: Matakin keɓancewa a D3.js ba shi da kamarsa, yana ba masu haɓakawa damar gina nuni na musamman sosai.

**Rauni**:
- **Lokacin Koyo Mai Tsayi**: D3.js yana da lokacin koyo mai tsayi kuma ya fi sarƙaƙiya a haɗa idan aka kwatanta da sauran laburare.
- **Mai Cin Lokaci**: Gina zane a D3.js na iya ɗaukar lokaci, musamman ga zane na yau da kullum kamar zanen candlestick ko doughnut.

**Hukunci**:  
D3.js yana da ƙarfi sosai ga ci-gaban zane na musamman amma ya fi buƙata ga amfani da yawa na yau da kullum saboda lokacin koyonsa mai tsayi da lokacin ci gaba. Ya fi dacewa a yanayin da sauran laburaren zane ba sa ba da matakin keɓancewar da ake buƙata.

---

### Kammalawa

Bayan kimanta laburaren bisa buƙatun aikin, **Apache ECharts** ya fito a matsayin mafi kyawun zaɓi. Yana goyon bayan cikakken jerin zanen da ake buƙata, ciki har da taswirar geo, zanen candlestick, da zanen taruwa. Buɗaɗɗen tushe ne, mai wadatattun siffofi, kuma mai mu’amala sosai, wanda ya dace daidai da manufofin aikin. Ko da yake **D3.js** yana ba da mafi yawan sassauci, sarƙaƙiyarsa da lokacin da yake ɗauka sun sa bai dace sosai da sabuwar kamfani da ke son maimaitawa cikin sauri ba. **ApexCharts** da **Chart.js** madadin da suka dace ne ga ayyuka masu sauƙi amma ba su da goyon baya ga ci-gaban nau’ikan zane.
