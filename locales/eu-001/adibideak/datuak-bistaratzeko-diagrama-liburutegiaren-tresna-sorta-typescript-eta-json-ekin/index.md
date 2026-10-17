# Arkitektura-erabakien erregistroa: datuak bistaratzeko diagrama-liburutegiaren tresna-sorta TypeScript eta JSON erabiliz

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

**Helburu nagusia:**  
Bistaratze interaktiboak sortzeko diagrama-tresna-sorta aurreratu bat aukeratzea, finantza-datuetan, datu zientifikoetan eta gobernu-datuetan zentratuta, TypeScript eta JSON erabiliz. Liburutegiak ezaugarri sendoak, malgutasuna eskaini eta kode irekikoa izan behar du. 

### Testuingurua eta eskakizunak:

1. **Garapen arina (lehentasun handia)**: Startup gisa, iterazio azkarra, prototipatzea eta garapenean malgutasuna ezinbestekoak dira. Diagrama-liburutegiak garapen-ziklo azkarrak ahalbidetu behar ditu.
   
2. **Diagrama motak (lehentasun handia)**:
   - **Donut diagrama**
   - **Radar diagrama**
   - **Clustering prozesuaren diagrama**
   - **Denbora-ardatza duen area diagrama**
   - **Candlestick diagrama**
   - **Nightingale diagrama**
   - **Geo SVG mapa**
   
   Diagrama mota hauek bereziki garrantzitsuak dira datu-multzo konplexuak bistaratzeko, hala nola finantza-joerak, metrika zientifikoak eta informazio geografikoa.

3. **Doakoa eta kode irekikoa (lehentasun handia)**: Tresna-sorta kode irekikoa izan behar da lizentzia-kostuak saihesteko, gardentasuna eskaintzeko eta pertsonalizaziorako malgutasuna emateko.

4. **Lehentasun txikiko irizpideak**:
   - **Exekuzio-abiadura**: Errendimendua garrantzitsua den arren, ez da erabaki honetarako lehentasun gorena.
   - **Eskalagarritasuna**: Eskalagarritasuna orokorrean garrantzitsua den arren, berehalako beharra denboran zehar hazi daitekeen MVP bat eraikitzea da. Eskalagarritasun-kezkak geroago jorra daitezke.
   - **Atzerako bateragarritasuna**: Ez da kezka nagusia hasierako eraikuntzarako, liburutegia modernoa eta aktiboki mantendua den bitartean.

### Ebaluatutako liburutegiak:

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

**Ikuspegi orokorra**:  
Apache ECharts bistaratze interaktibo eta pertsonalizagarrietarako diagrama-liburutegi ahaltsu eta malgua da. Diagrama sorta zabala onartzen du eta bereziki sendoa da bistaratze konplexu eta dinamikoetan.

**Indarrak**:
- **Interaktibitate aurreratua**: ECharts bikaina da diagrama interaktiboak eskaintzen, zoom, panning eta datu dinamikoen eguneraketa bezalako ezaugarriak eskainiz.
- **Donut, radar, candlestick, Geo SVG mapak**: ECharts-ek behar diren diagrama mota asko onartzen ditu, donut, radar, candlestick eta mapa geografikoen bistaratzeak barne.
- **Doakoa eta kode irekikoa**: ECharts kode irekiko liburutegia da, startup baten aurrekontu-kontzientziarekin bat datorrena eta kodea aldatzeko askatasuna ematen duena.
- **Malgutasuna eta hedagarritasuna**: Oso pertsonalizagarria, animazioetarako, bistaratze pertsonalizatuetarako eta diagramatze-teknika aurreratuetarako euskarri zabalarekin.
  
**Ahuleziak**:
- **Ikaskuntza-kurba**: ECharts, ahaltsua izan arren, ikaskuntza-kurba aldapatsuagoa izan dezake bere malgutasunagatik eta API zabalagatik.
- **Dokumentazioaren konplexutasuna**: Dokumentazioa zabala da baina gainezka egin dezake hasi berri diren garatzaileentzat.

**Epaia**:  
ECharts oso egokia da proiekturako diagrama interaktiboak onartzen dituelako, behar diren mota guztiak barne, hala nola candlestick diagramak, radar diagramak eta geo mapak. Bere kode irekiko izaera proiektuaren malgutasun- eta kostu-eraginkortasun beharrarekin bat dator.

---

### 2. **Chart.js**

**Ikuspegi orokorra**:  
Chart.js diagrama mota arruntak eraikitzeko diagrama-liburutegi sinple eta erraz erabilgarria da. Sinpletasunagatik eta integratzeko erraztasunagatik ezaguna da.

**Indarrak**:
- **Erabilera-erraztasuna**: Chart.js oso erraza da konfiguratzeko eta erabiltzeko, ikaskuntza-kurba minimoarekin.
- **Kode irekia**: Chart.js doakoa eta kode irekikoa da, kostuak murrizteko kritikoa dena.
- **Diagrama mota arruntak**: Donut, area, radar eta lerro diagrama bezalako oinarrizko diagramak onartzen ditu, behar nagusi gehienak estaltzen dituztenak.

**Ahuleziak**:
- **Diagrama aurreratu mugatuak**: Chart.js-ek ez ditu natiboki onartzen candlestick diagrama, geo SVG mapa edo clustering prozesuaren diagrama bezalako diagrama mota konplexuak. Ezaugarri horiek pluginen edo pertsonalizazioaren bidez gehi badaitezke ere, ez da beste liburutegiekin bezain zuzena.
- **Interaktibitatea**: Chart.js-ek oinarrizko interaktibitatea (adib. tooltip-ak eta hover efektuak) onartzen duen arren, ez du ECharts edo D3.js bezain ezaugarri aurreraturik eskaintzen.

**Epaia**:  
Chart.js bikaina da proiektu sinple eta azkarretarako, baina diagrama mota konplexuen euskarri faltak ez-egoki bihurtzen du candlestick diagramak eta geo mapak bezalako behar aurreratuak dituen datu-intentsiboko aplikazio baterako. Prototipatzeko aukera ona da, baina behar diren diagrama motetarako tresna aurreratuagoak gomendatzen dira.

---

### 3. **ApexCharts**

**Ikuspegi orokorra**:  
ApexCharts diagrama-liburutegi modernoa da, diagrama mota anitz eskaintzen dituena eta bistaratze interaktiboetan zentratzen dena, API erraz erabilgarri batekin.

**Indarrak**:
- **Ezaugarri interaktiboak**: ApexCharts-ek diagrama interaktiboak eskaintzen ditu tooltip-ekin, zoom-ekin, panning-ekin eta eguneraketekin.
- **Finantza- eta diagrama zientifikoetarako euskarria**: Diagrama mota sorta zabala onartzen du, candlestick diagramak, radar diagramak eta area diagramak barne.
- **Erabilera-erraztasuna**: API zuzena du eta proiektu batean integratzeko sinplea da.
- **Doakoa eta kode irekikoa**: ApexCharts-ek erabilera-kasu askotarako egokia den kode irekiko bertsio doakoa eskaintzen du.
  
**Ahuleziak**:
- **Pertsonalizazio konplexua**: Ezaugarri ugari eskaintzen dituen arren, pertsonalizazio-aukerak ez dira ECharts edo D3.js bezain malguak diagramatze-behar oso konplexu edo pertsonalizatuetarako.
- **Geo mapak**: ApexCharts-ek ez ditu natiboki onartzen geo mapak edo clustering prozesuaren diagramak, proiektu honetarako beharrezkoak direnak.

**Epaia**:  
ApexCharts lehiakide sendoa da bere erabilera-erraztasunagatik eta interaktibitateagatik, baina diagrama mota aurreratu jakin batzuetan hutsegiten du, bereziki geo mapen eta clustering diagramen beharrean. Diagrama sinpleagoetarako aukera ona da, baina beharrezko ezaugarri batzuk falta ditu.

---

### 4. **AG Charts**

**Ikuspegi orokorra**:  
AG Charts errendimendurako eta zehaztasunerako diseinatutako maila komertzialeko diagrama-liburutegia da. Oso egokia da finantza-, zientzia- eta negozio-paneleak sortzeko.

**Indarrak**:
- **Diagrama mota aurreratuak**: AG Charts-ek diagrama mota aurreratu asko onartzen ditu, candlestick diagramak, area diagramak, radar diagramak eta gehiago barne. AG-Grid produktuekin integrazio sakona ere eskaintzen du.
- **Errendimendu handia**: Errendimendu bikaina eskaintzen du, bereziki datu-multzo handiak kudeatzean.
- **Interaktibitatea**: AG Charts-ek ezaugarri interaktibo ugari onartzen ditu, hala nola zoom-a, tooltip-ak eta eguneraketa dinamikoak.

**Ahuleziak**:
- **Ez erabat doakoa**: AG Charts-ek bertsio doakoa eskaintzen duen arren, ezaugarri guztiak dituen bertsioa ordainpekoa da, eta horrek oztopo izan daiteke kostuak minimizatu nahi dituzten startup-entzat.
- **Konplexutasuna**: Liburutegia ezaugarri-aberatsa den arren, proiektu sinpleagoetarako gehiegizkoa izan daiteke eta beste aukerekin alderatuta konfigurazio eta ezarpen gehiago behar ditzake.

**Epaia**:  
AG Charts ahaltsua eta ezaugarri-aberatsa da baina baliteke aukerarik egokiena ez izatea bere izaera komertzialagatik eta kostu-egituragatik. Bere egokitasuna aurrekontuak ordainpeko bertsioak hartu ditzakeen ala kode irekiko alternatibak nahiago diren araberakoa da.

---

### 5. **Highcharts**

**Ikuspegi orokorra**:  
Highcharts diagrama mota sorta zabalagatik eta pertsonalizazio-aukera indartsuengatik ezaguna den diagrama-liburutegi ezaguna da.

**Indarrak**:
- **Diagrama mota zabalak**: Highcharts-ek diagrama sorta zabala onartzen du, candlestick, radar, area eta geo mapak barne.
- **Interaktiboa eta dinamikoa**: Highcharts-ek ezaugarri interaktibo aberatsak eskaintzen ditu, drill-down, zoom eta panning barne.
- **Erabilera-erraztasuna**: Erabiltzaile-lagunkoia den API-a eta dokumentazio ona ditu, hasteko erraza dena.

**Ahuleziak**:
- **Lizentzia komertziala**: Highcharts-ek erabilera ez-komertzialerako bertsio doakoa eskaintzen duen arren, lizentzia komertziala garestia da, eta horrek eragozpen garrantzitsua izan daiteke startup-entzat.
- **Ikaskuntza-kurba**: ECharts bezain aldapatsua ez den arren, Highcharts-en ikaskuntza-kurba oraindik ere erronka izan daiteke hasiberrientzat.

**Epaia**:  
Highcharts ezaugarri-aberatsa den liburutegia da, baina bere lizentzia komertzialak ez egoki bihurtzen du kode irekiko, kostuarekiko sentikorrak diren proiektuetarako. Bere diagramatze-aukera zabalak plus bat dira, baina lizentzia-arazoak erabilera-kasu honetarako bere erakargarritasuna mugatzen du.

---

### 6. **Carbon Charts**

**Ikuspegi orokorra**:  
Carbon Charts IBM-k garatutako diagrama-liburutegia da, bistaratze erakargarriak eta oso pertsonalizagarriak diren diagramak sortzeko diseinatua.

**Indarrak**:
- **Pertsonalizagarritasuna**: Carbon Charts-ek diagramen itxura eta portaeraren pertsonalizazio zabala ahalbidetzen du.
- **Kode irekia**: Doakoa eta kode irekikoa da, proiektuaren aurrekontu-lagunkoia den soluzioen eskakizunarekin bat datorrena.
- **Diagrama arruntetarako euskarria**: Donut, radar eta area diagrama bezalako diagrama mota arruntak onartzen ditu, nahiz eta geo mapak edo candlestick diagramak bezalako mota aurreratuagoetarako euskarririk ez duen.

**Ahuleziak**:
- **Diagrama mota aurreratu mugatuak**: Ez ditu onartzen geo mapak, clustering prozesuaren diagramak edo candlestick diagramak, proiekturako ezinbestekoak direnak.
- **Ekosistema txikiagoa**: Carbon Charts-ek ECharts edo Highcharts bezalako diagrama-liburutegi handiagoek baino komunitate eta ekosistema txikiagoa du.

**Epaia**:  
Carbon Charts kode irekikoa eta pertsonalizagarria da, baina proiektu honetarako behar diren diagrama mota konplexuagoen euskarririk ez du. Diagramatze-behar sinpleagoetarako egokiagoa da.

---

### 7. **Layer Cake**

**Ikuspegi orokorra**:  
Layer Cake bistaratze malguak eta geruzatuak sortzeko diseinatutako datu-bistaratze liburutegia da.

**Indarrak**:
- **Geruza pertsonalizagarriak**: Bistaratze konplexuetarako geruzatze-aukera indartsuak eskaintzen ditu.
- **Kode irekia**: Doakoa eta kode irekikoa da, aurrekontu-kontzienteak diren proiektuetarako aukera bideragarria bihurtuz.

**Ahuleziak**:
- **Dokumentazio mugatua**: Layer Cake-k dokumentazio zabala eta komunitate-euskarria falta ditu, liburutegi finkatuagoekin alderatuta lan egitea zailagoa eginez.
- **Ez dago diagramentzat eraikia**: Layer Cake diagrama ez diren bistaratzeetarako egokiagoa da, beraz bere diagramatze-aukera berehalakoak mugatuak dira.

**Epaia**:  
Bistaratze bereziak egiteko interesgarria den arren, Layer Cake ez da egokia candlestick diagramak edo radar diagramak bezalako diagramatze-eskakizun tradizionalak betetzeko. Diagrama estandarren eremutik kanpoko bistaratze pertsonalizatuetarako egokiagoa da.

---

### 8. **D3.js**

**Ikuspegi orokorra**:  
D3.js datuek gidatutako bistaratzeak HTML, SVG eta CSS bidez sortzeko JavaScript liburutegi ahaltsua da.

**Indarrak**:
- **Malgutasun parekaezina**: D3.js-ek ia edozein bistaratze pertsonalizatu mota sortzea ahalbidetzen du, eta horrek oso ahaltsua egiten du diagrama aurreratu eta interaktiboetarako.
- **Ezaugarri zabalak**: Behar diren diagrama mota guztiak onartzen ditu, geo mapak, clustering diagramak eta gehiago barne.
- **Pertsonalizagarria**: D3.js-en pertsonalizazio-maila parekaezina da, garatzaileei bistaratze oso neurrira egindakoak eraikitzeko aukera emanez.

**Ahuleziak**:
- **Ikaskuntza-kurba aldapatsua**: D3.js-ek ikaskuntza-kurba aldapatsua du eta beste liburutegiak baino konplexuagoa da integratzeko.
- **Denbora asko eskatzen du**: D3.js-en diagramak eraikitzeak denbora asko eskatu dezake, bereziki candlestick edo donut diagrama bezalako diagrama arruntetarako.

**Epaia**:  
D3.js izugarri ahaltsua da diagrama aurreratu eta pertsonalizatuetarako, baina erabilera-kasu tipiko askotarako gehiegizkoa da bere ikaskuntza-kurba aldapatsua eta garapen-denborarengatik. Egokiena beste diagrama-liburutegiek behar den pertsonalizazio-maila eskaintzen ez duten egoeretarako.

---

### Ondorioa

Proiektuaren beharretan oinarrituta liburutegiak ebaluatu ondoren, **Apache ECharts** aukerarik onena da. Behar diren diagrama sorta osoa onartzen du, geo mapak, candlestick diagramak eta clustering diagramak barne. Kode irekikoa, ezaugarri-aberatsa eta oso interaktiboa da, eta proiektuaren helburuekin perfektuki bat dator. **D3.js**-ek malgutasun gehien eskaintzen duen arren, bere konplexutasuna eta denbora-inbertsioa ez-ideal bihurtzen dute azkar iteratu nahi duen startup batentzat. **ApexCharts** eta **Chart.js** alternatiba onak dira proiektu sinpleagoetarako, baina diagrama mota aurreratuen euskarririk ez dute.
