# Taifead Cinnidh Ailtireachta: leabharlann cairteanna do léirshamhlú sonraí ag úsáid TypeScript agus JSON

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

**Príomhchuspóir:**  
Tacar uirlisí cairteanna casta a roghnú chun léirshamhluithe idirghníomhacha a chruthú, ag díriú ar shonraí airgeadais, sonraí eolaíochta, agus sonraí rialtais ag úsáid TypeScript agus JSON. Ba cheart go soláthródh an leabharlann gnéithe láidre, solúbthacht, agus go mbeadh sí foinse oscailte. 

### Comhthéacs agus Riachtanais:

1. **Forbairt Agile (Tosaíocht Ard)**: Mar thionscnamh nua, tá atriall tapa, prótaipeáil, agus solúbthacht san fhorbairt riachtanach. Ní mór don leabharlann cairteanna timthriallta forbartha tapa a cheadú.
   
2. **Cineálacha Cairteanna (Tosaíocht Ard)**:
   - **Cairt Fháinne (Doughnut)**
   - **Cairt Radair**
   - **Cairt Phróisis Braisleacháin**
   - **Cairt Limistéir le Ais Ama**
   - **Cairt Coinnle (Candlestick)**
   - **Cairt Nightingale**
   - **Léarscáil SVG Gheografach**
   
   Tá na cineálacha cairteanna seo tábhachtach go háirithe chun tacair sonraí chasta a léirshamhlú, amhail treochtaí airgeadais, méadrachtaí eolaíochta, agus faisnéis gheografach.

3. **Saor in Aisce agus Foinse Oscailte (Tosaíocht Ard)**: Ba cheart go mbeadh an tacar uirlisí foinse oscailte chun costais cheadúnais a sheachaint, trédhearcacht a sholáthar, agus solúbthacht a thairiscint le haghaidh saincheaptha.

4. **Critéir Thábhachta Íseal**:
   - **Luas Ama Rite**: Cé go bhfuil feidhmíocht tábhachtach, ní tosaíocht is airde é don chinneadh seo.
   - **Inscálaitheacht**: Cé go bhfuil inscálaitheacht tábhachtach go ginearálta, is é an gá láithreach MVP a thógáil a fhéadfaidh fás le himeacht ama. Is féidir imní inscálaitheachta a láimhseáil níos déanaí.
   - **Comhoiriúnacht Chúlghabhálach**: Ní príomhimní é don tógáil tosaigh, fad is atá an leabharlann nua-aimseartha agus á cothabháil go gníomhach.

### Leabharlanna a Measadh:

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

**Forbhreathnú**:  
Is leabharlann cairteanna chumhachtach, solúbtha é Apache ECharts le haghaidh léirshamhluithe idirghníomhacha, inchustaimithe. Tacaíonn sé le raon leathan cairteanna agus tá sé láidir go háirithe i léirshamhluithe casta, dinimiciúla.

**Láidreachtaí**:
- **Idirghníomhaíocht Chasta**: Is fearr le ECharts cairteanna idirghníomhacha a sholáthar, ag tairiscint gnéithe amhail súmáil, panáil, agus nuashonruithe dinimiciúla sonraí.
- **Fáinne, Radar, Coinnle, Léarscáileanna SVG Geografacha**: Tacaíonn ECharts le go leor de na cineálacha cairteanna riachtanacha, lena n-áirítear léirshamhluithe fáinne, radair, coinnle, agus léarscáileanna geografacha.
- **Saor in Aisce agus Foinse Oscailte**: Is leabharlann foinse oscailte é ECharts, a oireann do nádúr buiséadach tionscnaimh nua agus a thugann saoirse chun an cód a mhodhnú.
- **Solúbthacht agus Inleathnaitheacht**: An-inchustaimithe, le tacaíocht fhairsing d'ainmníochtaí, léirshamhluithe saincheaptha, agus teicnící casta cairteanna.
  
**Laigí**:
- **Cuar Foghlama**: D'fhéadfadh cuar foghlama níos géire a bheith ag ECharts, cé go bhfuil sé cumhachtach, mar gheall ar a sholúbthacht agus a API fairsing.
- **Castacht Doiciméadaithe**: Tá an doiciméadú cuimsitheach ach d'fhéadfadh sé a bheith róthrom d'fhorbróirí atá díreach ag tosú leis.

**Breithiúnas**:  
Tá ECharts an-oiriúnach don tionscadal mar gheall ar a thacaíocht do chairteacha idirghníomhacha, lena n-áirítear na cineálacha riachtanacha go léir amhail cairteacha coinnle, cairteacha radair, agus léarscáileanna geografacha. Tá a nádúr foinse oscailte ag teacht le riachtanas an tionscadail do sholúbthacht agus costéifeachtúlacht.

---

### 2. **Chart.js**

**Forbhreathnú**:  
Is leabharlann cairteanna simplí, éasca le húsáid é Chart.js chun gnáthchineálacha cairteanna a thógáil. Tá cáil air as a shimplíocht agus éascaíocht comhtháthaithe.

**Láidreachtaí**:
- **Éascaíocht Úsáide**: Tá Chart.js an-simplí le socrú agus le húsáid, le cuar foghlama íosta.
- **Foinse Oscailte**: Tá Chart.js saor in aisce agus foinse oscailte, rud atá ríthábhachtach chun costais a laghdú.
- **Gnáthchineálacha Cairteanna**: Tacaíonn sé le cairteanna bunúsacha amhail cairteanna fáinne, limistéir, radair, agus líne, a chlúdaíonn formhór na bpríomhriachtanas.

**Laigí**:
- **Cairteanna Casta Teoranta**: Ní thacaíonn Chart.js go dúchasach le cineálacha cairteanna casta amhail cairteacha coinnle, léarscáileanna SVG geografacha, nó cairteacha próisis braisleacháin. Cé gur féidir na gnéithe seo a chur leis trí bhreiseáin nó saincheapadh, níl sé chomh simplí agus atá le leabharlanna eile.
- **Idirghníomhaíocht**: Cé go dtacaíonn Chart.js le hidirghníomhaíocht bhunúsach (m.sh., leideanna uirlisí agus éifeachtaí scaoilte), ní thairgeann sé gnéithe chomh casta le ECharts nó D3.js.

**Breithiúnas**:  
Tá Chart.js iontach do thionscadail shimplí, thapa, ach fágann an easpa tacaíochta do chineálacha cairteanna casta nach bhfuil sé oiriúnach d'fheidhmchlár sonraí-throm le riachtanais chasta amhail cairteacha coinnle agus léarscáileanna geografacha. Is rogha mhaith é le haghaidh prótaipeála, ach do na cineálacha cairteanna riachtanacha, moltar uirlisí níos casta.

---

### 3. **ApexCharts**

**Forbhreathnú**:  
Is leabharlann cairteanna nua-aimseartha é ApexCharts a sholáthraíonn cineálacha cairteanna éagsúla agus a dhíríonn ar léirshamhluithe idirghníomhacha le API éasca le húsáid.

**Láidreachtaí**:
- **Gnéithe Idirghníomhacha**: Tairgeann ApexCharts cairteanna idirghníomhacha le leideanna uirlisí, súmáil, panáil, agus nuashonruithe.
- **Tacaíocht do Chairteacha Airgeadais agus Eolaíochta**: Tacaíonn sé le raon leathan cineálacha cairteanna, lena n-áirítear cairteacha coinnle, cairteacha radair, agus cairteacha limistéir.
- **Éascaíocht Úsáide**: Tá API díreach aige agus tá sé simplí a chomhtháthú i dtionscadal.
- **Saor in Aisce agus Foinse Oscailte**: Tairgeann ApexCharts leagan foinse oscailte saor in aisce atá oiriúnach do go leor cásanna úsáide.
  
**Laigí**:
- **Saincheapadh Casta**: Cé go soláthraíonn sé go leor gnéithe, níl na roghanna saincheaptha chomh solúbtha le ECharts nó D3.js d'ardriachtanais chasta nó shaincheaptha cairteanna.
- **Léarscáileanna Geografacha**: Ní thacaíonn ApexCharts go dúchasach le léarscáileanna geografacha ná cairteacha próisis braisleacháin, atá riachtanach don tionscadal seo.

**Breithiúnas**:  
Is iomaitheoir láidir é ApexCharts mar gheall ar a éascaíocht úsáide agus idirghníomhaíochta, ach tá sé gearr ar roinnt cineálacha cairteanna casta, go háirithe an gá le léarscáileanna geografacha agus cairteacha braisleacháin. Is rogha mhaith é do chairteanna níos simplí ach tá roinnt gnéithe riachtanacha in easnamh air.

---

### 4. **AG Charts**

**Forbhreathnú**:  
Is leabharlann cairteanna ar chaighdeán tráchtála é AG Charts atá deartha le haghaidh feidhmíochta agus cruinneas. Tá sé an-oiriúnach chun painéil airgeadais, eolaíochta, agus ghnó a chruthú.

**Láidreachtaí**:
- **Cineálacha Cairteanna Casta**: Tacaíonn AG Charts le go leor cineálacha cairteanna casta, lena n-áirítear cairteacha coinnle, cairteacha limistéir, cairteacha radair, agus níos mó. Tairgeann sé comhtháthú domhain le táirgí eile AG-Grid freisin.
- **Ardfheidhmíocht**: Tairgeann sé feidhmíocht den scoth, go háirithe agus tacair mhóra sonraí á láimhseáil.
- **Idirghníomhaíocht**: Tacaíonn AG Charts le gnéithe idirghníomhacha éagsúla amhail súmáil, leideanna uirlisí, agus nuashonruithe dinimiciúla.

**Laigí**:
- **Níl sé Saor in Aisce go hIomlán**: Cé go dtairgeann AG Charts leagan saor in aisce, tá an leagan lánghnéitheach íoctha, rud a d'fhéadfadh a bheith ina bhac ar thionscnaimh nua atá ag iarraidh costais a íoslaghdú.
- **Castacht**: Cé go bhfuil an leabharlann saibhir i ngnéithe, d'fhéadfadh sé a bheith iomarcach do thionscadail níos simplí agus d'fhéadfadh níos mó socraithe agus cumraíochta a bheith ag teastáil i gcomparáid le roghanna eile.

**Breithiúnas**:  
Tá AG Charts cumhachtach agus saibhir i ngnéithe ach b'fhéidir nach é an oiriúnú is fearr é mar gheall ar a nádúr tráchtála agus a struchtúr costais. Braitheann a oiriúnacht ar an bhféadfaidh an buiséad leaganacha íoctha a chur san áireamh nó an fearr roghanna foinse oscailte.

---

### 5. **Highcharts**

**Forbhreathnú**:  
Is leabharlann cairteanna choitianta é Highcharts a bhfuil cáil air as a raon leathan cineálacha cairteanna agus roghanna cumhachtacha saincheaptha.

**Láidreachtaí**:
- **Cineálacha Cairteanna Cuimsitheacha**: Tacaíonn Highcharts le héagsúlacht leathan cairteanna, lena n-áirítear coinnle, radar, limistéar, agus léarscáileanna geografacha.
- **Idirghníomhach agus Dinimiciúil**: Soláthraíonn Highcharts gnéithe saibhre idirghníomhacha, lena n-áirítear drill-downs, súmáil, agus panáil.
- **Éascaíocht Úsáide**: Tá API cairdiúil úsáideora agus doiciméadú maith aige, rud a fhágann go bhfuil sé éasca tosú.

**Laigí**:
- **Ceadúnas Tráchtála**: Cé go dtairgeann Highcharts leagan saor in aisce d'úsáid neamhthráchtála, tá an ceadúnas tráchtála daor, rud a d'fhéadfadh a bheith ina mhíbhuntáiste suntasach do thionscnaimh nua.
- **Cuar Foghlama**: Cé nach bhfuil sé chomh géar le ECharts, d'fhéadfadh an cuar foghlama do Highcharts a bheith dúshlánach do thosaitheoirí fós.

**Breithiúnas**:  
Is leabharlann saibhir i ngnéithe é Highcharts, ach fágann a cheadúnú tráchtála go bhfuil sé níos lú oiriúnach do thionscadail foinse oscailte, íogaire do chostais. Is buntáiste iad a roghanna cuimsitheacha cairteanna, ach cuireann an cheist cheadúnaithe teorainn lena mhealladh don chás úsáide seo.

---

### 6. **Carbon Charts**

**Forbhreathnú**:  
Is leabharlann cairteanna é Carbon Charts a d'fhorbair IBM, deartha chun cairteanna tarraingteacha ó thaobh amhairc agus an-inchustaimithe a chruthú.

**Láidreachtaí**:
- **Inchustaimitheacht**: Ceadaíonn Carbon Charts saincheapadh fairsing ar chuma agus iompar na gcairteanna.
- **Foinse Oscailte**: Tá sé saor in aisce agus foinse oscailte, rud a ailíníonn le riachtanas an tionscadail do réitigh atá cairdiúil don bhuiséad.
- **Tacaíocht do Ghnáthchairteanna**: Tacaíonn sé le gnáthchineálacha cairteanna amhail cairteacha fáinne, radair, agus limistéir, cé nach dtacaíonn sé le cineálacha níos casta amhail léarscáileanna geografacha nó cairteacha coinnle.

**Laigí**:
- **Cineálacha Cairteanna Casta Teoranta**: Ní thacaíonn sé le léarscáileanna geografacha, cairteacha próisis braisleacháin, ná cairteacha coinnle, atá riachtanach don tionscadal.
- **Éiceachóras Níos Lú**: Tá pobal agus éiceachóras níos lú ag Carbon Charts i gcomparáid le leabharlanna cairteanna níos mó cosúil le ECharts nó Highcharts.

**Breithiúnas**:  
Tá Carbon Charts foinse oscailte agus inchustaimithe ach níl tacaíocht aige do na cineálacha cairteanna níos casta atá ag teastáil don tionscadal seo. Tá sé níos oiriúnaí do riachtanais chairteanna níos simplí.

---

### 7. **Layer Cake**

**Forbhreathnú**:  
Is leabharlann léirshamhlaithe sonraí é Layer Cake atá deartha chun léirshamhluithe solúbtha, sraithe a chruthú.

**Láidreachtaí**:
- **Sraitheanna Inchustaimithe**: Soláthraíonn sé roghanna cumhachtacha sraithithe do léirshamhluithe casta.
- **Foinse Oscailte**: Tá sé saor in aisce agus foinse oscailte, rud a fhágann gur rogha inmharthana é do thionscadail atá aireach ar an mbuiséad.

**Laigí**:
- **Doiciméadú Teoranta**: Níl doiciméadú fairsing ná tacaíocht phobail ag Layer Cake, rud a fhágann go bhfuil sé níos deacra oibriú leis i gcomparáid le leabharlanna níos bunaithe.
- **Gan a Bheith Tógtha do Chairteanna**: Tá Layer Cake níos oiriúnaí do léirshamhluithe nach cairteanna iad, mar sin tá a roghanna cairteanna amach as an mbosca teoranta.

**Breithiúnas**:  
Cé go bhfuil sé suimiúil do léirshamhluithe uathúla, níl Layer Cake idéalach do ghnáthriachtanais chairteanna amhail cairteacha coinnle nó cairteacha radair. Tá sé níos oiriúnaí do léirshamhluithe saincheaptha lasmuigh de scóip gnáthchairteanna.

---

### 8. **D3.js**

**Forbhreathnú**:  
Is leabharlann JavaScript chumhachtach é D3.js chun léirshamhluithe tiomáinte ag sonraí a chruthú trí HTML, SVG, agus CSS.

**Láidreachtaí**:
- **Solúbthacht Gan Sárú**: Ceadaíonn D3.js beagnach aon chineál léirshamhlaithe saincheaptha a chruthú, rud a fhágann go bhfuil sé an-chumhachtach do chairteanna casta agus idirghníomhacha.
- **Gnéithe Fairsinge**: Tacaíonn sé leis na cineálacha cairteanna riachtanacha go léir, lena n-áirítear léarscáileanna geografacha, cairteacha braisleacháin, agus níos mó.
- **Inchustaimithe**: Tá leibhéal an tsaincheaptha i D3.js gan sárú, rud a ligeann d'fhorbróirí léirshamhluithe an-oiriúnaithe a thógáil.

**Laigí**:
- **Cuar Foghlama Géar**: Tá cuar foghlama géar ag D3.js agus tá sé níos casta a chomhtháthú i gcomparáid le leabharlanna eile.
- **Tógann sé Am**: Is féidir cairteacha a thógáil i D3.js a bheith am-tomhaiseach, go háirithe do ghnáthchairteanna amhail cairteacha coinnle nó fáinne.

**Breithiúnas**:  
Tá D3.js thar a bheith cumhachtach do chairteanna casta, saincheaptha ach tá sé iomarcach do go leor gnáthchásanna úsáide mar gheall ar a chuar foghlama géar agus a am forbartha. Is fearr é i gcásanna nach soláthraíonn leabharlanna cairteanna eile an leibhéal riachtanach saincheaptha.

---

### Conclúid

Tar éis na leabharlanna a mheas bunaithe ar riachtanais an tionscadail, seasann **Apache ECharts** amach mar an rogha is fearr. Tacaíonn sé leis an raon iomlán cairteanna riachtanacha, lena n-áirítear léarscáileanna geografacha, cairteacha coinnle, agus cairteacha braisleacháin. Tá sé foinse oscailte, saibhir i ngnéithe, agus an-idirghníomhach, rud a ailíníonn go foirfe le spriocanna an tionscadail. Cé go dtairgeann **D3.js** an tsolúbthacht is mó, fágann a chastacht agus an t-am a theastaíonn é níos lú idéalach do thionscnamh nua atá ag iarraidh atriall a dhéanamh go tapa. Is roghanna eile maithe iad **ApexCharts** agus **Chart.js** do thionscadail níos simplí ach níl tacaíocht acu do chineálacha cairteanna casta.
