# Arhitektuuriotsuse kirje: diagrammiteek andmete visualiseerimiseks TypeScripti ja JSON-iga

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

**Peamine eesmärk:**  
Valida täiustatud diagrammitööriistakomplekt interaktiivsete visualiseerimiste loomiseks, keskendudes finantsandmetele, teadusandmetele ja valitsuse andmetele TypeScripti ja JSON-iga. Teek peaks pakkuma töökindlaid funktsioone ja paindlikkust ning olema avatud lähtekoodiga. 

### Kontekst ja nõuded:

1. **Agiilne arendus (kõrge prioriteet)**: idufirmana on kiire iteratsioon, prototüüpimine ja paindlikkus arenduses ülioluline. Diagrammiteek peab võimaldama kiireid arendustsükleid.
   
2. **Diagrammitüübid (kõrge prioriteet)**:
   - **Sõõrikdiagramm (Doughnut Chart)**
   - **Radardiagramm (Radar Chart)**
   - **Klasterdamisprotsessi diagramm (Clustering Process Chart)**
   - **Alaga diagramm ajateljega (Area Chart with Time Axis)**
   - **Küünlajalgdiagramm (Candlestick Chart)**
   - **Nightingale'i diagramm (Nightingale Chart)**
   - **Geo SVG kaart (Geo SVG Map)**
   
   Need diagrammitüübid on eriti olulised keerukate andmekogumite, nagu finantstrendid, teaduslikud mõõdikud ja geograafiline teave, visualiseerimiseks.

3. **Tasuta ja avatud lähtekoodiga (kõrge prioriteet)**: tööriist peaks olema avatud lähtekoodiga, et vältida litsentsikulusid, pakkuda läbipaistvust ja anda paindlikkust kohandamiseks.

4. **Madala prioriteediga kriteeriumid**:
   - **Käitusaja kiirus**: kuigi jõudlus on oluline, ei ole see selle otsuse kõrgeim prioriteet.
   - **Skaleeritavus**: kuigi skaleeritavus on üldiselt oluline, on vahetu vajadus ehitada MVP, mis saab aja jooksul kasvada. Skaleeritavuse küsimusi saab käsitleda hiljem.
   - **Tagasiulatuv ühilduvus**: pole esialgse ehituse jaoks peamine mure, kui teek on kaasaegne ja seda hooldatakse aktiivselt.

### Hinnatud teegid:

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

**Ülevaade**:  
Apache ECharts on võimas, paindlik diagrammiteek interaktiivsete, kohandatavate visualiseerimiste jaoks. See toetab laia valikut diagramme ja on eriti tugev keerukate, dünaamiliste visualiseerimiste puhul.

**Tugevused**:
- **Täiustatud interaktiivsus**: ECharts paistab silma interaktiivsete diagrammide pakkumisel ning pakub funktsioone nagu suumimine, panoraamimine ja dünaamilised andmeuuendused.
- **Sõõrik-, radar-, küünlajalgdiagrammid, Geo SVG kaardid**: ECharts toetab paljusid vajalikke diagrammitüüpe, sealhulgas sõõrik-, radar-, küünlajalgdiagrammide ja geograafiliste kaartide visualiseerimisi.
- **Tasuta ja avatud lähtekoodiga**: ECharts on avatud lähtekoodiga teek, mis sobib idufirma eelarveteadliku olemusega ja annab vabaduse koodi muuta.
- **Paindlikkus ja laiendatavus**: väga kohandatav, ulatusliku toega animatsioonidele, kohandatud visualiseerimistele ja täiustatud diagrammitehnikatele.
  
**Nõrkused**:
- **Õppimiskõver**: ECharts võib, kuigi võimas, omada järsemat õppimiskõverat oma paindlikkuse ja ulatusliku API tõttu.
- **Dokumentatsiooni keerukus**: dokumentatsioon on põhjalik, kuid võib olla algajatele arendajatele ülekaalukas.

**Hinnang**:  
ECharts sobib projektile väga hästi tänu oma toele interaktiivsetele diagrammidele, sealhulgas kõigile vajalikele tüüpidele nagu küünlajalgdiagrammid, radardiagrammid ja geokaardid. Selle avatud lähtekoodiga olemus on kooskõlas projekti vajadusega paindlikkuse ja kulutõhususe järele.

---

### 2. **Chart.js**

**Ülevaade**:  
Chart.js on lihtne, kasutajasõbralik diagrammiteek tavaliste diagrammitüüpide ehitamiseks. See on tuntud oma lihtsuse ja hõlpsa integreerimise poolest.

**Tugevused**:
- **Kasutuslihtsus**: Chart.js on väga lihtne seadistada ja kasutada minimaalse õppimiskõveraga.
- **Avatud lähtekood**: Chart.js on tasuta ja avatud lähtekoodiga, mis on kulude vähendamiseks ülioluline.
- **Tavalised diagrammitüübid**: see toetab põhidiagramme nagu sõõrik-, ala-, radar- ja joondiagrammid, mis katavad enamiku peamistest vajadustest.

**Nõrkused**:
- **Piiratud täiustatud diagrammid**: Chart.js ei toeta natiivselt keerukaid diagrammitüüpe nagu küünlajalgdiagrammid, Geo SVG kaardid või klasterdamisprotsessi diagrammid. Kuigi neid funktsioone saab lisada pluginate või kohandamise kaudu, ei ole see nii lihtne kui teiste teekidega.
- **Interaktiivsus**: kuigi Chart.js toetab põhilist interaktiivsust (nt vihjed ja hõljumise efektid), ei paku see nii täiustatud funktsioone kui ECharts või D3.js.

**Hinnang**:  
Chart.js on suurepärane lihtsate, kiirete projektide jaoks, kuid keerukate diagrammitüüpide toe puudumine teeb selle sobimatuks andmemahukale rakendusele, millel on täiustatud vajadused nagu küünlajalgdiagrammid ja geokaardid. See on hea valik prototüüpimiseks, kuid vajalike diagrammitüüpide jaoks soovitatakse täiustatumaid tööriistu.

---

### 3. **ApexCharts**

**Ülevaade**:  
ApexCharts on kaasaegne diagrammiteek, mis pakub mitmeid diagrammitüüpe ja keskendub interaktiivsetele visualiseerimistele hõlpsasti kasutatava API-ga.

**Tugevused**:
- **Interaktiivsed funktsioonid**: ApexCharts pakub interaktiivseid diagramme vihjete, suumimise, panoraamimise ja uuendustega.
- **Finants- ja teaduslike diagrammide tugi**: see toetab laia valikut diagrammitüüpe, sealhulgas küünlajalgdiagramme, radardiagramme ja alaga diagramme.
- **Kasutuslihtsus**: sellel on lihtne API ja see on projekti hõlpsasti integreeritav.
- **Tasuta ja avatud lähtekoodiga**: ApexCharts pakub tasuta avatud lähtekoodiga versiooni, mis sobib paljudeks kasutusjuhtudeks.
  
**Nõrkused**:
- **Keeruline kohandamine**: kuigi see pakub palju funktsioone, ei ole kohandamisvõimalused nii paindlikud kui ECharts või D3.js väga keerukate või kohandatud diagrammivajaduste jaoks.
- **Geokaardid**: ApexCharts ei toeta natiivselt geokaarte ega klasterdamisprotsessi diagramme, mida selle projekti jaoks nõutakse.

**Hinnang**:  
ApexCharts on tugev kandidaat oma kasutuslihtsuse ja interaktiivsuse tõttu, kuid jääb alla mõne täiustatud diagrammitüübi osas, eriti vajadus geokaartide ja klasterdamisdiagrammide järele. See on hea alternatiiv lihtsamatele diagrammidele, kuid sellel puuduvad mõned vajalikud funktsioonid.

---

### 4. **AG Charts**

**Ülevaade**:  
AG Charts on kommertskvaliteediga diagrammiteek, mis on loodud jõudluse ja täpsuse jaoks. See sobib väga hästi finants-, teadus- ja ärilaudade loomiseks.

**Tugevused**:
- **Täiustatud diagrammitüübid**: AG Charts toetab paljusid täiustatud diagrammitüüpe, sealhulgas küünlajalgdiagramme, alaga diagramme, radardiagramme ja muud. See pakub ka sügavat integratsiooni teiste AG-Grid toodetega.
- **Kõrge jõudlus**: see pakub suurepärast jõudlust, eriti suurte andmekogumite käsitlemisel.
- **Interaktiivsus**: AG Charts toetab rida interaktiivseid funktsioone nagu suumimine, vihjed ja dünaamilised uuendused.

**Nõrkused**:
- **Mitte täiesti tasuta**: kuigi AG Charts pakub tasuta versiooni, on täisfunktsionaalne versioon tasuline, mis võib olla takistuseks idufirmadele, kes tahavad kulusid minimeerida.
- **Keerukus**: kuigi teek on funktsioonirikas, võib see olla lihtsamate projektide jaoks üledimensioneeritud ja nõuda teiste valikutega võrreldes rohkem konfiguratsiooni ja seadistust.

**Hinnang**:  
AG Charts on võimas ja funktsioonirikas, kuid ei pruugi olla parim sobivus oma kommertslikkuse ja kulustruktuuri tõttu. Selle sobivus sõltub sellest, kas eelarve mahutab tasulisi versioone või eelistatakse avatud lähtekoodiga alternatiive.

---

### 5. **Highcharts**

**Ülevaade**:  
Highcharts on populaarne diagrammiteek, mis on tuntud oma laia diagrammitüüpide valiku ja võimsate kohandamisvõimaluste poolest.

**Tugevused**:
- **Põhjalikud diagrammitüübid**: Highcharts toetab laia valikut diagramme, sealhulgas küünlajalg-, radar-, alaga diagramme ja geokaarte.
- **Interaktiivne ja dünaamiline**: Highcharts pakub rikkalikke interaktiivseid funktsioone, sealhulgas drill-down'e, suumimist ja panoraamimist.
- **Kasutuslihtsus**: sellel on kasutajasõbralik API ja hea dokumentatsioon, mis teeb alustamise lihtsaks.

**Nõrkused**:
- **Kommertslitsents**: kuigi Highcharts pakub tasuta versiooni mitteärilisel kasutamiseks, on kommertslitsents kallis, mis võib olla idufirmadele märkimisväärne puudus.
- **Õppimiskõver**: kuigi see pole nii järsk kui ECharts'il, võib Highchartsi õppimiskõver olla algajatele endiselt keeruline.

**Hinnang**:  
Highcharts on funktsioonirikas teek, kuid selle kommertslitsentsimine teeb selle vähem sobivaks kulutundlikele avatud lähtekoodiga projektidele. Selle põhjalikud diagrammivalikud on pluss, kuid litsentsiküsimus piirab selle atraktiivsust selle kasutusjuhu jaoks.

---

### 6. **Carbon Charts**

**Ülevaade**:  
Carbon Charts on IBM-i arendatud diagrammiteek, mis on loodud visuaalselt atraktiivsete ja väga kohandatavate diagrammide loomiseks.

**Tugevused**:
- **Kohandatavus**: Carbon Charts võimaldab diagrammide välimuse ja käitumise ulatuslikku kohandamist.
- **Avatud lähtekood**: see on tasuta ja avatud lähtekoodiga, mis on kooskõlas projekti nõudega eelarvesõbralike lahenduste järele.
- **Tavaliste diagrammide tugi**: see toetab tavalisi diagrammitüüpe nagu sõõrik-, radar- ja alaga diagrammid, kuid sellel puudub tugi täiustatumatele tüüpidele nagu geokaardid või küünlajalgdiagrammid.

**Nõrkused**:
- **Piiratud täiustatud diagrammitüübid**: see ei toeta geokaarte, klasterdamisprotsessi diagramme ega küünlajalgdiagramme, mis on projekti jaoks vajalikud.
- **Väiksem ökosüsteem**: Carbon Chartsil on väiksem kogukond ja ökosüsteem võrreldes suuremate diagrammiteekidega nagu ECharts või Highcharts.

**Hinnang**:  
Carbon Charts on avatud lähtekoodiga ja kohandatav, kuid sellel puudub tugi keerukamatele diagrammitüüpidele, mida selle projekti jaoks vaja on. See sobib paremini lihtsamate diagrammivajaduste jaoks.

---

### 7. **Layer Cake**

**Ülevaade**:  
Layer Cake on andmete visualiseerimise teek, mis on loodud paindlike, kihiliste visualiseerimiste loomiseks.

**Tugevused**:
- **Kohandatavad kihid**: see pakub võimsaid kihistamisvõimalusi keerukate visualiseerimiste jaoks.
- **Avatud lähtekood**: see on tasuta ja avatud lähtekoodiga, mis teeb sellest teostatava valiku eelarveteadlikele projektidele.

**Nõrkused**:
- **Piiratud dokumentatsioon**: Layer Cake'il puudub põhjalik dokumentatsioon ja kogukonna toetus, mis teeb sellega töötamise raskemaks võrreldes väljakujunenumate teekidega.
- **Pole diagrammide jaoks ehitatud**: Layer Cake sobib paremini visualiseerimisteks, mis ei ole diagrammid, seega on selle karbist välja diagrammivalikud piiratud.

**Hinnang**:  
Kuigi Layer Cake on huvitav ainulaadsete visualiseerimiste jaoks, ei ole see ideaalne traditsiooniliste diagramminõuete, nagu küünlajalgdiagrammid või radardiagrammid, jaoks. See sobib paremini kohandatud visualiseerimisteks väljaspool standarddiagrammide ulatust.

---

### 8. **D3.js**

**Ülevaade**:  
D3.js on võimas JavaScripti teek andmepõhiste visualiseerimiste loomiseks HTML-i, SVG ja CSS-i kaudu.

**Tugevused**:
- **Võrratu paindlikkus**: D3.js võimaldab luua praktiliselt igat tüüpi kohandatud visualiseerimist, muutes selle väga võimsaks täiustatud ja interaktiivsete diagrammide jaoks.
- **Põhjalikud funktsioonid**: see toetab kõiki vajalikke diagrammitüüpe, sealhulgas geokaarte, klasterdamisdiagramme ja muud.
- **Kohandatav**: D3.js kohandamise tase on võrratu, võimaldades arendajatel ehitada väga kohandatud visualiseerimisi.

**Nõrkused**:
- **Järsk õppimiskõver**: D3.js-il on järsk õppimiskõver ja seda on teiste teekidega võrreldes keerulisem integreerida.
- **Aeganõudev**: diagrammide ehitamine D3.js-is võib olla aeganõudev, eriti tavaliste diagrammide nagu küünlajalg- või sõõrikdiagrammide puhul.

**Hinnang**:  
D3.js on uskumatult võimas täiustatud, kohandatud diagrammide jaoks, kuid paljude tüüpiliste kasutusjuhtude jaoks üledimensioneeritud oma järsu õppimiskõvera ja arendusaja tõttu. See on parim olukordades, kus teised diagrammiteegid ei paku vajalikku kohandamise taset.

---

### Kokkuvõte

Pärast teekide hindamist projekti vajaduste alusel ilmneb **Apache ECharts** parima valikuna. See toetab kogu vajalike diagrammide spektrit, sealhulgas geokaarte, küünlajalgdiagramme ja klasterdamisdiagramme. See on avatud lähtekoodiga, funktsioonirikas ja väga interaktiivne, mis on projekti eesmärkidega ideaalselt kooskõlas. Kuigi **D3.js** pakub suurimat paindlikkust, teevad selle keerukus ja ajainvesteering selle vähem ideaalseks idufirma jaoks, kes tahab kiiresti iteratsioone teha. **ApexCharts** ja **Chart.js** on head alternatiivid lihtsamatele projektidele, kuid neil puudub tugi täiustatud diagrammitüüpidele.
