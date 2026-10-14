# Arkitektúrákvörðunarskrá: myndritasafn fyrir gagnasýn með TypeScript og JSON

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

**Meginmarkmið:**  
Að velja háþróað myndritasafn til að búa til gagnvirkar sjónrænar framsetningar, með áherslu á fjármálagögn, vísindagögn og opinber gögn með TypeScript og JSON. Safnið ætti að bjóða upp á öfluga eiginleika, sveigjanleika og vera opið.

### Samhengi og kröfur:

1. **Lipur þróun (mikill forgangur)**: Sem sprotafyrirtæki eru hröð þróun í áföngum, frumgerðasmíði og sveigjanleiki í þróun nauðsynleg. Myndritasafnið verður að leyfa hraðar þróunarlotur.
   
2. **Tegundir myndrita (mikill forgangur)**:
   - **Kleinuhringjarit (Doughnut)**
   - **Radarrit (Radar)**
   - **Þyrpingarferlisrit (Clustering Process Chart)**
   - **Svæðisrit með tímaás**
   - **Kertastjakarit (Candlestick)**
   - **Nightingale-rit**
   - **Geo SVG-kort**
   
   Þessar tegundir myndrita skipta sérstaklega máli til að sýna flókin gagnasöfn, svo sem fjármálaþróun, vísindamælikvarða og landfræðilegar upplýsingar.

3. **Ókeypis og opið (mikill forgangur)**: Safnið ætti að vera opið til að forðast leyfiskostnað, veita gagnsæi og bjóða upp á sveigjanleika til sérsníðunar.

4. **Viðmið með lítinn forgang**:
   - **Keyrsluhraði**: Þótt afköst skipti máli eru þau ekki forgangsatriði í þessari ákvörðun.
   - **Stigstærð**: Þótt stigstærð skipti almennt máli er brýnasta þörfin að smíða MVP sem getur vaxið með tímanum. Hægt er að taka á áhyggjum af stigstærð síðar.
   - **Afturábak samhæfni**: Ekki aðalatriði við upphaflega smíði, svo lengi sem safnið er nútímalegt og viðhaldið af virkni.

### Söfn sem voru metin:

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

**Yfirlit**:  
Apache ECharts er öflugt og sveigjanlegt myndritasafn fyrir gagnvirkar, sérsníðanlegar framsetningar. Það styður fjölbreytt úrval myndrita og er sérstaklega sterkt í flóknum, kvikum framsetningum.

**Styrkleikar**:
- **Háþróuð gagnvirkni**: ECharts skarar fram úr í gagnvirkum myndritum og býður upp á eiginleika eins og aðdrátt, færslu og kvikar gagnauppfærslur.
- **Kleinuhringjarit, radarrit, kertastjakarit, Geo SVG-kort**: ECharts styður margar nauðsynlegar tegundir myndrita, þar á meðal kleinuhringjarit, radarrit, kertastjakarit og landfræðileg kort.
- **Ókeypis og opið**: ECharts er opið safn, sem hentar fjárhagsvitund sprotafyrirtækis og veitir frelsi til að breyta kóðanum.
- **Sveigjanleiki og útvíkkanleiki**: Mjög sérsníðanlegt, með víðtækum stuðningi við hreyfimyndir, sérsniðnar framsetningar og háþróaða myndritatækni.
  
**Veikleikar**:
- **Námsferill**: ECharts getur, þótt öflugt sé, haft brattari námsferil vegna sveigjanleika síns og umfangsmikils API.
- **Flækjustig skjölunar**: Skjölunin er ítarleg en getur verið yfirþyrmandi fyrir þróunaraðila sem eru að byrja.

**Úrskurður**:  
ECharts hentar verkefninu mjög vel vegna stuðnings við gagnvirk myndrit, þar á meðal allar nauðsynlegar tegundir eins og kertastjakarit, radarrit og landfræðileg kort. Opinn eðli þess samræmist þörf verkefnisins fyrir sveigjanleika og hagkvæmni.

---

### 2. **Chart.js**

**Yfirlit**:  
Chart.js er einfalt og auðnotað myndritasafn til að smíða algengar tegundir myndrita. Það er þekkt fyrir einfaldleika og auðvelda samþættingu.

**Styrkleikar**:
- **Auðveld notkun**: Chart.js er mjög einfalt í uppsetningu og notkun, með lágmarks námsferil.
- **Opið**: Chart.js er ókeypis og opið, sem er mikilvægt til að draga úr kostnaði.
- **Algengar tegundir myndrita**: Það styður grunnmyndrit eins og kleinuhringjarit, svæðisrit, radarrit og línurit, sem ná yfir flestar aðalþarfir.

**Veikleikar**:
- **Takmörkuð háþróuð myndrit**: Chart.js styður ekki innbyggt flóknar tegundir myndrita eins og kertastjakarit, Geo SVG-kort eða þyrpingarferlisrit. Þótt hægt sé að bæta þessum eiginleikum við með viðbótum eða sérsníðun er það ekki jafn beinskeytt og með öðrum söfnum.
- **Gagnvirkni**: Þótt Chart.js styðji grunngagnvirkni (t.d. ábendingar og sveimáhrif) býður það ekki upp á jafn háþróaða eiginleika og ECharts eða D3.js.

**Úrskurður**:  
Chart.js er frábært fyrir einföld, hröð verkefni, en skortur þess á stuðningi við flóknar tegundir myndrita gerir það óhentugt fyrir gagnaþungt forrit með háþróaðar þarfir eins og kertastjakarit og landfræðileg kort. Það er góður kostur fyrir frumgerðasmíði, en fyrir nauðsynlegar tegundir myndrita er mælt með háþróaðri verkfærum.

---

### 3. **ApexCharts**

**Yfirlit**:  
ApexCharts er nútímalegt myndritasafn sem býður upp á fjölbreyttar tegundir myndrita og leggur áherslu á gagnvirkar framsetningar með auðnotuðu API.

**Styrkleikar**:
- **Gagnvirkir eiginleikar**: ApexCharts býður upp á gagnvirk myndrit með ábendingum, aðdrætti, færslu og uppfærslum.
- **Stuðningur við fjármála- og vísindamyndrit**: Það styður fjölbreyttar tegundir myndrita, þar á meðal kertastjakarit, radarrit og svæðisrit.
- **Auðveld notkun**: Það hefur beinskeytt API og er einfalt að samþætta í verkefni.
- **Ókeypis og opið**: ApexCharts býður upp á ókeypis opna útgáfu sem hentar í mörgum notkunartilvikum.
  
**Veikleikar**:
- **Flókin sérsníðun**: Þótt það bjóði upp á marga eiginleika eru sérsníðunarmöguleikarnir ekki jafn sveigjanlegir og í ECharts eða D3.js fyrir mjög flóknar eða sérsniðnar myndritaþarfir.
- **Landfræðileg kort**: ApexCharts styður ekki innbyggt landfræðileg kort eða þyrpingarferlisrit, sem verkefnið krefst.

**Úrskurður**:  
ApexCharts er sterkur keppinautur vegna auðveldrar notkunar og gagnvirkni, en fellur á prófinu hvað varðar tilteknar háþróaðar tegundir myndrita, einkum þörfina fyrir landfræðileg kort og þyrpingarrit. Það er góður kostur fyrir einfaldari myndrit en skortir sumar nauðsynlegar eiginleika.

---

### 4. **AG Charts**

**Yfirlit**:  
AG Charts er myndritasafn á viðskiptalegu stigi, hannað fyrir afköst og nákvæmni. Það hentar mjög vel til að búa til fjármála-, vísinda- og viðskiptamælaborð.

**Styrkleikar**:
- **Háþróaðar tegundir myndrita**: AG Charts styður margar háþróaðar tegundir myndrita, þar á meðal kertastjakarit, svæðisrit, radarrit og fleira. Það býður einnig upp á djúpa samþættingu við aðrar AG-Grid vörur.
- **Mikil afköst**: Það býður upp á framúrskarandi afköst, einkum við meðhöndlun stórra gagnasafna.
- **Gagnvirkni**: AG Charts styður ýmsa gagnvirka eiginleika eins og aðdrátt, ábendingar og kvikar uppfærslur.

**Veikleikar**:
- **Ekki alveg ókeypis**: Þótt AG Charts bjóði upp á ókeypis útgáfu er fullbúna útgáfan greidd, sem gæti verið hindrun fyrir sprotafyrirtæki sem vilja lágmarka kostnað.
- **Flækjustig**: Þótt safnið sé eiginleikaríkt gæti það verið ofvaxið einfaldari verkefnum og getur krafist meiri uppsetningar og stillinga en aðrir valkostir.

**Úrskurður**:  
AG Charts er öflugt og eiginleikaríkt en er hugsanlega ekki besta passunin vegna viðskiptalegs eðlis og kostnaðarskipanar. Hentugleiki þess veltur á því hvort fjárhagsáætlun rúmar greiddar útgáfur eða hvort opnir valkostir eru æskilegri.

---

### 5. **Highcharts**

**Yfirlit**:  
Highcharts er vinsælt myndritasafn, þekkt fyrir mikið úrval tegunda myndrita og öfluga sérsníðunarmöguleika.

**Styrkleikar**:
- **Alhliða tegundir myndrita**: Highcharts styður fjölbreytt úrval myndrita, þar á meðal kertastjakarit, radarrit, svæðisrit og landfræðileg kort.
- **Gagnvirkt og kvikt**: Highcharts býður upp á ríka gagnvirka eiginleika, þar á meðal niðurborun, aðdrátt og færslu.
- **Auðveld notkun**: Það hefur notendavænt API og góða skjölun, sem gerir auðvelt að byrja.

**Veikleikar**:
- **Viðskiptaleyfi**: Þótt Highcharts bjóði upp á ókeypis útgáfu fyrir notkun sem er ekki í viðskiptaskyni er viðskiptaleyfið dýrt, sem gæti verið verulegur ókostur fyrir sprotafyrirtæki.
- **Námsferill**: Þótt hann sé ekki jafn brattur og hjá ECharts getur námsferill Highcharts samt verið krefjandi fyrir byrjendur.

**Úrskurður**:  
Highcharts er eiginleikaríkt safn, en viðskiptaleyfi þess gerir það síður hentugt fyrir opin, kostnaðarnæm verkefni. Alhliða myndritamöguleikar þess eru kostur, en leyfismálið takmarkar aðdráttarafl þess fyrir þetta notkunartilvik.

---

### 6. **Carbon Charts**

**Yfirlit**:  
Carbon Charts er myndritasafn þróað af IBM, hannað til að búa til sjónrænt aðlaðandi og mjög sérsníðanleg myndrit.

**Styrkleikar**:
- **Sérsníðanleiki**: Carbon Charts leyfir víðtæka sérsníðun á útliti og hegðun myndrita.
- **Opið**: Það er ókeypis og opið, sem samræmist kröfu verkefnisins um fjárhagsvænar lausnir.
- **Stuðningur við algeng myndrit**: Það styður algengar tegundir myndrita eins og kleinuhringjarit, radarrit og svæðisrit, þótt það skorti stuðning við háþróaðri gerðir eins og landfræðileg kort eða kertastjakarit.

**Veikleikar**:
- **Takmarkaðar háþróaðar tegundir myndrita**: Það styður ekki landfræðileg kort, þyrpingarferlisrit eða kertastjakarit, sem eru nauðsynleg fyrir verkefnið.
- **Minna vistkerfi**: Carbon Charts hefur minna samfélag og vistkerfi en stærri myndritasöfn eins og ECharts eða Highcharts.

**Úrskurður**:  
Carbon Charts er opið og sérsníðanlegt en skortir stuðning við flóknari tegundir myndrita sem verkefnið þarf. Það hentar betur fyrir einfaldari myndritaþarfir.

---

### 7. **Layer Cake**

**Yfirlit**:  
Layer Cake er gagnasýnarsafn hannað til að búa til sveigjanlegar, lagskiptar framsetningar.

**Styrkleikar**:
- **Sérsníðanleg lög**: Það býður upp á öfluga lagskiptingarmöguleika fyrir flóknar framsetningar.
- **Opið**: Það er ókeypis og opið, sem gerir það að raunhæfum kosti fyrir fjárhagsvitund verkefni.

**Veikleikar**:
- **Takmörkuð skjölun**: Layer Cake skortir umfangsmikla skjölun og stuðning samfélags, sem gerir erfiðara að vinna með það samanborið við rótgrónari söfn.
- **Ekki smíðað fyrir myndrit**: Layer Cake hentar betur fyrir framsetningar sem eru ekki myndrit, svo innbyggðir myndritamöguleikar þess eru takmarkaðir.

**Úrskurður**:  
Þótt Layer Cake sé áhugavert fyrir einstakar framsetningar er það ekki tilvalið fyrir hefðbundnar myndritakröfur eins og kertastjakarit eða radarrit. Það hentar betur fyrir sérsniðnar framsetningar utan staðlaðra myndrita.

---

### 8. **D3.js**

**Yfirlit**:  
D3.js er öflugt JavaScript-safn til að búa til gagnadrifnar framsetningar með HTML, SVG og CSS.

**Styrkleikar**:
- **Óviðjafnanlegur sveigjanleiki**: D3.js leyfir að búa til nánast hvaða tegund sérsniðinnar framsetningar sem er, sem gerir það mjög öflugt fyrir háþróuð og gagnvirk myndrit.
- **Víðtækir eiginleikar**: Það styður allar nauðsynlegar tegundir myndrita, þar á meðal landfræðileg kort, þyrpingarrit og fleira.
- **Sérsníðanlegt**: Sérsníðunarstigið í D3.js á sér engan líka og gerir þróunaraðilum kleift að smíða mjög sérsniðnar framsetningar.

**Veikleikar**:
- **Brattur námsferill**: D3.js hefur brattan námsferil og er flóknara að samþætta en önnur söfn.
- **Tímafrekt**: Að smíða myndrit í D3.js getur verið tímafrekt, einkum fyrir algeng myndrit eins og kertastjaka- eða kleinuhringjarit.

**Úrskurður**:  
D3.js er ótrúlega öflugt fyrir háþróuð, sérsniðin myndrit en ofvaxið fyrir mörg dæmigerð notkunartilvik vegna bratts námsferils og þróunartíma. Það hentar best þegar önnur myndritasöfn veita ekki það sérsníðunarstig sem krafist er.

---

### Niðurstaða

Eftir að hafa metið söfnin út frá þörfum verkefnisins stendur **Apache ECharts** upp úr sem besti kosturinn. Það styður allt úrval nauðsynlegra myndrita, þar á meðal landfræðileg kort, kertastjakarit og þyrpingarrit. Það er opið, eiginleikaríkt og mjög gagnvirkt, sem samræmist fullkomlega markmiðum verkefnisins. Þótt **D3.js** bjóði upp á mestan sveigjanleika gera flækjustig þess og tímafjárfesting það síður tilvalið fyrir sprotafyrirtæki sem vill þróa hratt í áföngum. **ApexCharts** og **Chart.js** eru góðir valkostir fyrir einfaldari verkefni en skortir stuðning við háþróaðar tegundir myndrita.