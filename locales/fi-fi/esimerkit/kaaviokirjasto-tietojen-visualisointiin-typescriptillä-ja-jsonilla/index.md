# Arkkitehtuuripäätöstietue: kaaviokirjastotyökalupaketti tietojen visualisointiin TypeScriptillä ja JSON:lla

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

**Ensisijainen tavoite:**  
Valita edistynyt kaaviotyökalupaketti interaktiivisten visualisointien luomiseen, keskittyen talousdataan, tieteelliseen dataan ja julkishallinnon dataan TypeScriptillä ja JSON:lla. Kirjaston tulisi tarjota vankat ominaisuudet ja joustavuus, ja sen tulisi olla avointa lähdekoodia. 

### Konteksti ja vaatimukset:

1. **Ketterä kehitys (korkea prioriteetti)**: Startupina nopea iterointi, prototyyppien tekeminen ja kehityksen joustavuus ovat olennaisia. Kaaviokirjaston on sallittava nopeat kehityssyklit.
   
2. **Kaaviotyypit (korkea prioriteetti)**:
   - **Donitsikaavio (Doughnut Chart)**
   - **Tutkakaavio (Radar Chart)**
   - **Klusterointiprosessikaavio**
   - **Aluekaavio aika-akselilla**
   - **Kynttiläkaavio (Candlestick Chart)**
   - **Nightingale-kaavio**
   - **Geo SVG -kartta**
   
   Nämä kaaviotyypit ovat erityisen tärkeitä monimutkaisten tietojoukkojen, kuten taloudellisten trendien, tieteellisten mittarien ja maantieteellisen tiedon, visualisoinnissa.

3. **Ilmainen ja avoin lähdekoodi (korkea prioriteetti)**: Työkalupaketin tulisi olla avointa lähdekoodia lisenssikustannusten välttämiseksi, läpinäkyvyyden tarjoamiseksi ja mukauttamisen joustavuuden takaamiseksi.

4. **Matalan tärkeyden kriteerit**:
   - **Ajonaikainen nopeus**: Vaikka suorituskyky on tärkeää, se ei ole tämän päätöksen ensisijainen prioriteetti.
   - **Skaalautuvuus**: Vaikka skaalautuvuus on yleisesti tärkeää, välitön tarve on rakentaa MVP, joka voi kasvaa ajan myötä. Skaalautuvuushuolet voidaan käsitellä myöhemmin.
   - **Taaksepäin yhteensopivuus**: Ei ensisijainen huolenaihe ensimmäisessä rakennuksessa, kunhan kirjasto on moderni ja aktiivisesti ylläpidetty.

### Arvioidut kirjastot:

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

**Yleiskuva**:  
Apache ECharts on tehokas, joustava kaaviokirjasto interaktiivisille, mukautettaville visualisoinneille. Se tukee laajaa kaaviovalikoimaa ja on erityisen vahva monimutkaisissa, dynaamisissa visualisoinneissa.

**Vahvuudet**:
- **Edistynyt interaktiivisuus**: ECharts on erinomainen interaktiivisten kaavioiden tarjoamisessa, ja siinä on ominaisuuksia kuten zoomaus, panorointi ja dynaamiset tietopäivitykset.
- **Donitsi, tutka, kynttilä, Geo SVG -kartat**: ECharts tukee monia vaadittuja kaaviotyyppejä, mukaan lukien donitsi-, tutka-, kynttilä- ja maantieteelliset karttavisualisoinnit.
- **Ilmainen ja avoin lähdekoodi**: ECharts on avoimen lähdekoodin kirjasto, mikä sopii startupin budjettitietoiseen luonteeseen ja antaa vapauden muokata koodia.
- **Joustavuus ja laajennettavuus**: Erittäin mukautettavissa, ja siinä on laaja tuki animaatioille, mukautetuille visualisoinneille ja edistyneille kaaviotekniikoille.
  
**Heikkoudet**:
- **Oppimiskäyrä**: ECharts, vaikka tehokas, voi olla jyrkemmän oppimiskäyrän takana joustavuutensa ja laajan rajapintansa vuoksi.
- **Dokumentaation monimutkaisuus**: Dokumentaatio on kattava, mutta se voi tuntua musertavalta kehittäjille, jotka vasta aloittavat sen käytön.

**Tuomio**:  
ECharts sopii erittäin hyvin projektiin interaktiivisten kaavioiden tuen vuoksi, mukaan lukien kaikki vaaditut tyypit kuten kynttilä-, tutka- ja karttakaaviot. Sen avoin lähdekoodi sopii projektin joustavuuden ja kustannustehokkuuden tarpeeseen.

---

### 2. **Chart.js**

**Yleiskuva**:  
Chart.js on yksinkertainen, helppokäyttöinen kaaviokirjasto yleisten kaaviotyyppien rakentamiseen. Se tunnetaan yksinkertaisuudestaan ja helposta integroinnistaan.

**Vahvuudet**:
- **Käytön helppous**: Chart.js on erittäin helppo asentaa ja käyttää, ja sen oppimiskäyrä on minimaalinen.
- **Avoin lähdekoodi**: Chart.js on ilmainen ja avoimen lähdekoodin, mikä on kriittistä kustannusten vähentämiseksi.
- **Yleiset kaaviotyypit**: Se tukee perusdiagrammeja kuten donitsi-, alue-, tutka- ja viivakaaviot, jotka kattavat suurimman osan ensisijaisista tarpeista.

**Heikkoudet**:
- **Rajalliset edistyneet kaaviot**: Chart.js ei tue natiivisti monimutkaisia kaaviotyyppejä, kuten kynttilädiagrammeja, geo SVG -karttoja tai klusterointiprosessikaavioita. Vaikka nämä ominaisuudet voidaan lisätä lisäosilla tai mukauttamalla, se ei ole yhtä suoraviivaista kuin muilla kirjastoilla.
- **Interaktiivisuus**: Vaikka Chart.js tukee perusinteraktiivisuutta (esim. työkaluvihjeet ja kohdistustehosteet), se ei tarjoa yhtä edistyneitä ominaisuuksia kuin ECharts tai D3.js.

**Tuomio**:  
Chart.js sopii erinomaisesti yksinkertaisiin, nopeisiin projekteihin, mutta sen monimutkaisten kaaviotyyppien tuen puute tekee siitä sopimattoman tietoraskaaseen sovellukseen, jolla on edistyneitä tarpeita, kuten kynttilädiagrammit ja geokartat. Se on hyvä valinta prototyyppien tekoon, mutta vaadittuihin kaaviotyyppeihin suositellaan edistyneempiä työkaluja.

---

### 3. **ApexCharts**

**Yleiskuva**:  
ApexCharts on moderni kaaviokirjasto, joka tarjoaa erilaisia kaaviotyyppejä ja keskittyy interaktiivisiin visualisointeihin helppokäyttöisellä rajapinnalla.

**Vahvuudet**:
- **Interaktiiviset ominaisuudet**: ApexCharts tarjoaa interaktiivisia kaavioita työkaluvihjeillä, zoomauksella, panoroinnilla ja päivityksillä.
- **Tuki talous- ja tiedekaavioille**: Se tukee laajaa kaaviotyyppien valikoimaa, mukaan lukien kynttilä-, tutka- ja aluekaaviot.
- **Käytön helppous**: Sillä on suoraviivainen rajapinta, ja se on helppo integroida projektiin.
- **Ilmainen ja avoin lähdekoodi**: ApexCharts tarjoaa ilmaisen avoimen lähdekoodin version, joka sopii moniin käyttötapauksiin.
  
**Heikkoudet**:
- **Monimutkainen mukauttaminen**: Vaikka se tarjoaa monia ominaisuuksia, mukautusvaihtoehdot eivät ole yhtä joustavia kuin ECharts tai D3.js erittäin monimutkaisiin tai mukautettuihin kaaviotarpeisiin.
- **Geokartat**: ApexCharts ei tue natiivisti geokarttoja tai klusterointiprosessikaavioita, joita tämä projekti vaatii.

**Tuomio**:  
ApexCharts on vahva ehdokas helppokäyttöisyytensä ja interaktiivisuutensa vuoksi, mutta se jää vajaaksi tiettyjen edistyneiden kaaviotyyppien osalta, erityisesti geokarttojen ja klusterointikaavioiden tarpeen suhteen. Se on hyvä vaihtoehto yksinkertaisemmille kaavioille, mutta siitä puuttuu joitakin vaadittuja ominaisuuksia.

---

### 4. **AG Charts**

**Yleiskuva**:  
AG Charts on kaupallisen tason kaaviokirjasto, joka on suunniteltu suorituskykyä ja tarkkuutta varten. Se sopii erittäin hyvin talous-, tiede- ja liiketoimintakojelautojen luomiseen.

**Vahvuudet**:
- **Edistyneet kaaviotyypit**: AG Charts tukee monia edistyneitä kaaviotyyppejä, mukaan lukien kynttiläkaaviot, aluekaaviot, tutkakaaviot ja muita. Se tarjoaa myös syvän integraation muiden AG-Grid-tuotteiden kanssa.
- **Korkea suorituskyky**: Se tarjoaa erinomaisen suorituskyvyn, erityisesti suurten tietojoukkojen käsittelyssä.
- **Interaktiivisuus**: AG Charts tukee erilaisia interaktiivisia ominaisuuksia kuten zoomaus, työkaluvihjeet ja dynaamiset päivitykset.

**Heikkoudet**:
- **Ei täysin ilmainen**: Vaikka AG Charts tarjoaa ilmaisen version, täysiominaisuuksinen versio on maksullinen, mikä voi olla este startupeille, jotka pyrkivät minimoimaan kustannukset.
- **Monimutkaisuus**: Vaikka kirjasto on ominaisuuksiltaan rikas, se voi olla liioittelua yksinkertaisemmille projekteille ja saattaa vaatia enemmän asetuksia ja konfigurointia verrattuna muihin vaihtoehtoihin.

**Tuomio**:  
AG Charts on tehokas ja ominaisuuksiltaan rikas, mutta se ei välttämättä ole paras valinta kaupallisen luonteensa ja kustannusrakenteensa vuoksi. Sen soveltuvuus riippuu siitä, voiko budjetti kattaa maksulliset versiot vai suositaanko avoimen lähdekoodin vaihtoehtoja.

---

### 5. **Highcharts**

**Yleiskuva**:  
Highcharts on suosittu kaaviokirjasto, joka tunnetaan laajasta kaaviotyyppien valikoimastaan ja tehokkaista mukautusvaihtoehdoistaan.

**Vahvuudet**:
- **Kattavat kaaviotyypit**: Highcharts tukee laajaa kaaviovalikoimaa, mukaan lukien kynttilä-, tutka-, alue- ja geokartat.
- **Interaktiivinen ja dynaaminen**: Highcharts tarjoaa rikkaita interaktiivisia ominaisuuksia, mukaan lukien porautuminen (drill-down), zoomaus ja panorointi.
- **Käytön helppous**: Sillä on käyttäjäystävällinen rajapinta ja hyvä dokumentaatio, mikä helpottaa alkuun pääsyä.

**Heikkoudet**:
- **Kaupallinen lisenssi**: Vaikka Highcharts tarjoaa ilmaisen version ei-kaupalliseen käyttöön, kaupallinen lisenssi on kallis, mikä voi olla merkittävä haitta startupeille.
- **Oppimiskäyrä**: Vaikka se ei ole yhtä jyrkkä kuin ECharts, Highchartsin oppimiskäyrä voi silti olla haastava aloittelijoille.

**Tuomio**:  
Highcharts on ominaisuuksiltaan rikas kirjasto, mutta sen kaupallinen lisensointi tekee siitä vähemmän sopivan avoimen lähdekoodin, kustannusherkille projekteille. Sen kattavat kaaviovaihtoehdot ovat plussaa, mutta lisenssiongelma rajoittaa sen vetovoimaa tässä käyttötapauksessa.

---

### 6. **Carbon Charts**

**Yleiskuva**:  
Carbon Charts on IBM:n kehittämä kaaviokirjasto, joka on suunniteltu visuaalisesti miellyttävien ja erittäin mukautettavien kaavioiden luomiseen.

**Vahvuudet**:
- **Mukautettavuus**: Carbon Charts sallii kaavioiden ulkonäön ja käyttäytymisen laajan mukauttamisen.
- **Avoin lähdekoodi**: Se on ilmainen ja avointa lähdekoodia, mikä sopii projektin vaatimukseen budjettiystävällisistä ratkaisuista.
- **Tuki yleisille kaavioille**: Se tukee yleisiä kaaviotyyppejä kuten donitsi-, tutka- ja aluekaaviot, vaikka siitä puuttuu tuki edistyneemmille tyypeille, kuten geokartoille tai kynttiläkaavioille.

**Heikkoudet**:
- **Rajalliset edistyneet kaaviotyypit**: Se ei tue geokarttoja, klusterointiprosessikaavioita tai kynttiläkaavioita, jotka ovat projektille olennaisia.
- **Pienempi ekosysteemi**: Carbon Chartsilla on pienempi yhteisö ja ekosysteemi verrattuna suurempiin kaaviokirjastoihin kuten ECharts tai Highcharts.

**Tuomio**:  
Carbon Charts on avoimen lähdekoodin ja mukautettavissa, mutta siitä puuttuu tuki monimutkaisemmille kaaviotyypeille, joita tämä projekti tarvitsee. Se sopii paremmin yksinkertaisempiin kaaviotarpeisiin.

---

### 7. **Layer Cake**

**Yleiskuva**:  
Layer Cake on tietojen visualisointikirjasto, joka on suunniteltu joustavien, kerrostettujen visualisointien luomiseen.

**Vahvuudet**:
- **Mukautettavat kerrokset**: Se tarjoaa tehokkaita kerrostusvaihtoehtoja monimutkaisille visualisoinneille.
- **Avoin lähdekoodi**: Se on ilmainen ja avointa lähdekoodia, mikä tekee siitä toteuttamiskelpoisen vaihtoehdon budjettitietoisille projekteille.

**Heikkoudet**:
- **Rajallinen dokumentaatio**: Layer Cakesta puuttuu laaja dokumentaatio ja yhteisön tuki, mikä tekee siitä vaikeamman käyttää verrattuna vakiintuneempiin kirjastoihin.
- **Ei rakennettu kaavioille**: Layer Cake sopii paremmin ei-kaaviomaisiin visualisointeihin, joten sen valmiit kaaviovaihtoehdot ovat rajalliset.

**Tuomio**:  
Vaikka Layer Cake on kiinnostava ainutlaatuisiin visualisointeihin, se ei ole ihanteellinen perinteisiin kaaviovaatimuksiin kuten kynttiläkaavioihin tai tutkakaavioihin. Se sopii paremmin mukautettuihin visualisointeihin tavallisten kaavioiden ulkopuolella.

---

### 8. **D3.js**

**Yleiskuva**:  
D3.js on tehokas JavaScript-kirjasto dataohjattujen visualisointien luomiseen HTML:n, SVG:n ja CSS:n kautta.

**Vahvuudet**:
- **Vertaansa vailla oleva joustavuus**: D3.js mahdollistaa lähes minkä tahansa mukautetun visualisoinnin luomisen, mikä tekee siitä erittäin tehokkaan edistyneille ja interaktiivisille kaavioille.
- **Laajat ominaisuudet**: Se tukee kaikkia vaadittuja kaaviotyyppejä, mukaan lukien geokartat, klusterointikaaviot ja muita.
- **Mukautettavissa**: D3.js:n mukautuksen taso on vertaansa vailla, ja se sallii kehittäjien rakentaa erittäin räätälöityjä visualisointeja.

**Heikkoudet**:
- **Jyrkkä oppimiskäyrä**: D3.js:llä on jyrkkä oppimiskäyrä, ja se on monimutkaisempi integroida verrattuna muihin kirjastoihin.
- **Aikaa vievä**: Kaavioiden rakentaminen D3.js:llä voi olla aikaa vievää, erityisesti yleisille kaavioille kuten kynttilä- tai donitsikaaviot.

**Tuomio**:  
D3.js on uskomattoman tehokas edistyneille, mukautetuille kaavioille, mutta on liioittelua monissa tyypillisissä käyttötapauksissa jyrkän oppimiskäyränsä ja kehitysaikansa vuoksi. Se on paras tilanteissa, joissa muut kaaviokirjastot eivät tarjoa vaadittua mukautuksen tasoa.

---

### Johtopäätös

Kirjastojen arvioinnin jälkeen projektin tarpeiden perusteella **Apache ECharts** nousee parhaaksi vaihtoehdoksi. Se tukee vaadittujen kaavioiden koko kirjoa, mukaan lukien geokartat, kynttiläkaaviot ja klusterointikaaviot. Se on avointa lähdekoodia, ominaisuuksiltaan rikas ja erittäin interaktiivinen, mikä sopii täydellisesti projektin tavoitteisiin. Vaikka **D3.js** tarjoaa eniten joustavuutta, sen monimutkaisuus ja aikainvestointi tekevät siitä vähemmän ihanteellisen startupille, joka haluaa iteroida nopeasti. **ApexCharts** ja **Chart.js** ovat hyviä vaihtoehtoja yksinkertaisemmille projekteille, mutta niistä puuttuu tuki edistyneille kaaviotyypeille.
