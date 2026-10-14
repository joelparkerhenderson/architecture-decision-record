# Architekturális döntési feljegyzés: diagramkönyvtár adatvizualizációhoz TypeScripttel és JSON-nal

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

**Elsődleges cél:**  
Fejlett diagrameszköztár kiválasztása interaktív vizualizációk készítéséhez, pénzügyi, tudományos és kormányzati adatokra összpontosítva, TypeScript és JSON használatával. A könyvtárnak robusztus funkciókat és rugalmasságot kell nyújtania, és nyílt forráskódúnak kell lennie. 

### Háttér és követelmények:

1. **Agilis fejlesztés (magas prioritás)**: Startupként elengedhetetlen a gyors iteráció, a prototípus-készítés és a fejlesztési rugalmasság. A diagramkönyvtárnak gyors fejlesztési ciklusokat kell lehetővé tennie.
   
2. **Diagramtípusok (magas prioritás)**:
   - **Fánkdiagram (doughnut)**
   - **Radardiagram**
   - **Klaszterezési folyamat diagramja**
   - **Területdiagram időtengellyel**
   - **Gyertyadiagram (candlestick)**
   - **Nightingale-diagram**
   - **Földrajzi SVG-térkép**
   
   Ezek a diagramtípusok különösen fontosak összetett adatkészletek vizualizálásához, mint a pénzügyi trendek, tudományos mutatók és földrajzi információk.

3. **Ingyenes és nyílt forráskódú (magas prioritás)**: Az eszköztárnak nyílt forráskódúnak kell lennie a licenckiadások elkerülése, az átláthatóság és a testreszabási rugalmasság érdekében.

4. **Alacsony fontosságú kritériumok**:
   - **Futási sebesség**: Bár a teljesítmény fontos, nem kiemelt prioritás ennél a döntésnél.
   - **Skálázhatóság**: Bár a skálázhatóság általában fontos, a közvetlen igény egy olyan MVP építése, amely idővel nőhet. A skálázhatósági kérdések később kezelhetők.
   - **Visszamenőleges kompatibilitás**: A kezdeti építésnél nem elsődleges szempont, amíg a könyvtár modern és aktívan karbantartott.

### Értékelt könyvtárak:

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

**Áttekintés**:  
Az Apache ECharts egy erőteljes, rugalmas diagramkönyvtár interaktív, testreszabható vizualizációkhoz. Sokféle diagramot támogat, és különösen erős összetett, dinamikus vizualizációkban.

**Erősségek**:
- **Fejlett interaktivitás**: Az ECharts kiválóan nyújt interaktív diagramokat, olyan funkciókkal, mint a nagyítás, a görgetés és a dinamikus adatfrissítések.
- **Fánk-, radar-, gyertya-, földrajzi SVG-térképek**: Az ECharts a szükséges diagramtípusok közül sokat támogat, köztük a fánk-, radar-, gyertya- és földrajzi térképes vizualizációkat.
- **Ingyenes és nyílt forráskódú**: Az ECharts nyílt forráskódú könyvtár, ami illik a startup költségtudatos jellegéhez, és szabadságot ad a kód módosítására.
- **Rugalmasság és bővíthetőség**: Erősen testreszabható, kiterjedt támogatással animációkhoz, egyéni vizualizációkhoz és fejlett diagramkészítési technikákhoz.
  
**Gyengeségek**:
- **Tanulási görbe**: Az ECharts, bár erőteljes, rugalmassága és kiterjedt API-ja miatt meredekebb tanulási görbével rendelkezhet.
- **Dokumentáció bonyolultsága**: A dokumentáció átfogó, de nyomasztó lehet az éppen csak kezdő fejlesztőknek.

**Ítélet**:  
Az ECharts nagyon alkalmas a projekthez az interaktív diagramok támogatása miatt, beleértve az összes szükséges típust, mint a gyertyadiagramok, radardiagramok és földrajzi térképek. Nyílt forráskódú jellege összhangban van a projekt rugalmasság- és költséghatékonyság-igényével.

---

### 2. **Chart.js**

**Áttekintés**:  
A Chart.js egy egyszerű, könnyen használható diagramkönyvtár gyakori diagramtípusok építéséhez. Egyszerűségéről és könnyű integrálhatóságáról ismert.

**Erősségek**:
- **Használhatóság**: A Chart.js nagyon egyszerűen beállítható és használható, minimális tanulási görbével.
- **Nyílt forráskód**: A Chart.js ingyenes és nyílt forráskódú, ami kulcsfontosságú a költségek csökkentéséhez.
- **Gyakori diagramtípusok**: Alap diagramokat támogat, mint a fánk-, terület-, radar- és vonaldiagram, amelyek lefedik az elsődleges igények többségét.

**Gyengeségek**:
- **Korlátozott fejlett diagramok**: A Chart.js natívan nem támogat összetett diagramtípusokat, mint a gyertyadiagramok, a földrajzi SVG-térképek vagy a klaszterezési folyamat diagramjai. Bár ezek a funkciók hozzáadhatók bővítményekkel vagy testreszabással, ez nem olyan egyszerű, mint más könyvtáraknál.
- **Interaktivitás**: Bár a Chart.js támogat alapvető interaktivitást (pl. eszköztippek és rámutatási hatások), nem kínál olyan fejlett funkciókat, mint az ECharts vagy a D3.js.

**Ítélet**:  
A Chart.js remek egyszerű, gyors projektekhez, de az összetett diagramtípusok támogatásának hiánya alkalmatlanná teszi egy adatigényes alkalmazáshoz, fejlett igényekkel, mint a gyertyadiagramok és földrajzi térképek. Jó választás prototípus-készítéshez, de a szükséges diagramtípusokhoz fejlettebb eszközök ajánlottak.

---

### 3. **ApexCharts**

**Áttekintés**:  
Az ApexCharts egy modern diagramkönyvtár, amely sokféle diagramtípust nyújt, és az interaktív vizualizációkra összpontosít, könnyen használható API-val.

**Erősségek**:
- **Interaktív funkciók**: Az ApexCharts interaktív diagramokat kínál eszköztippekkel, nagyítással, görgetéssel és frissítésekkel.
- **Pénzügyi és tudományos diagramok támogatása**: Sokféle diagramtípust támogat, köztük gyertya-, radar- és területdiagramokat.
- **Használhatóság**: Egyszerű API-ja van, és könnyű integrálni egy projektbe.
- **Ingyenes és nyílt forráskódú**: Az ApexCharts ingyenes nyílt forráskódú verziót kínál, amely sok felhasználási esetre alkalmas.
  
**Gyengeségek**:
- **Bonyolult testreszabás**: Bár sok funkciót nyújt, a testreszabási lehetőségek nem olyan rugalmasak, mint az ECharts vagy a D3.js esetében nagyon összetett vagy egyedi diagramigényeknél.
- **Földrajzi térképek**: Az ApexCharts natívan nem támogat földrajzi térképeket vagy klaszterezési folyamat diagramokat, amelyekre ebben a projektben szükség van.

**Ítélet**:  
Az ApexCharts erős jelölt a használhatósága és interaktivitása miatt, de egyes fejlett diagramtípusoknál, különösen a földrajzi térképek és klaszterezési diagramok igényénél elmarad. Jó lehetőség egyszerűbb diagramokhoz, de hiányzik belőle néhány szükséges funkció.

---

### 4. **AG Charts**

**Áttekintés**:  
Az AG Charts kereskedelmi szintű diagramkönyvtár, teljesítményre és pontosságra tervezve. Nagyon alkalmas pénzügyi, tudományos és üzleti irányítópultok létrehozására.

**Erősségek**:
- **Fejlett diagramtípusok**: Az AG Charts sok fejlett diagramtípust támogat, köztük gyertya-, terület-, radardiagramokat és mást. Mély integrációt kínál más AG-Grid termékekkel is.
- **Magas teljesítmény**: Kiváló teljesítményt nyújt, különösen nagy adatkészletek kezelésekor.
- **Interaktivitás**: Az AG Charts különféle interaktív funkciókat támogat, mint a nagyítás, eszköztippek és dinamikus frissítések.

**Gyengeségek**:
- **Nem teljesen ingyenes**: Bár az AG Charts kínál ingyenes verziót, a teljes funkcionalitású verzió fizetős, ami akadály lehet a költségeket minimalizálni kívánó startupoknak.
- **Bonyolultság**: Bár a könyvtár funkciógazdag, túlzás lehet egyszerűbb projektekhez, és több beállítást és konfigurálást igényelhet, mint más lehetőségek.

**Ítélet**:  
Az AG Charts erőteljes és funkciógazdag, de kereskedelmi jellege és költségstruktúrája miatt nem biztos, hogy a legjobb választás. Alkalmassága attól függ, hogy a költségvetés elbírja-e a fizetős verziókat, vagy a nyílt forráskódú alternatívákat részesítik előnyben.

---

### 5. **Highcharts**

**Áttekintés**:  
A Highcharts népszerű diagramkönyvtár, amely a diagramtípusok széles skálájáról és az erőteljes testreszabási lehetőségekről ismert.

**Erősségek**:
- **Átfogó diagramtípusok**: A Highcharts sokféle diagramot támogat, köztük gyertya-, radar-, terület- és földrajzi térképeket.
- **Interaktív és dinamikus**: A Highcharts gazdag interaktív funkciókat nyújt, köztük lefúrást (drill-down), nagyítást és görgetést.
- **Használhatóság**: Felhasználóbarát API-val és jó dokumentációval rendelkezik, ami megkönnyíti a kezdést.

**Gyengeségek**:
- **Kereskedelmi licenc**: Bár a Highcharts ingyenes verziót kínál nem kereskedelmi használatra, a kereskedelmi licenc drága, ami jelentős hátrány lehet a startupoknak.
- **Tanulási görbe**: Bár nem olyan meredek, mint az EChartsé, a Highcharts tanulási görbéje még mindig kihívást jelenthet a kezdőknek.

**Ítélet**:  
A Highcharts funkciógazdag könyvtár, de kereskedelmi licencelése kevésbé alkalmassá teszi nyílt forráskódú, költségérzékeny projektekhez. Az átfogó diagramlehetőségek plusz, de a licencelési kérdés korlátozza vonzerejét ebben a felhasználási esetben.

---

### 6. **Carbon Charts**

**Áttekintés**:  
A Carbon Charts az IBM által fejlesztett diagramkönyvtár, vizuálisan vonzó és erősen testreszabható diagramok létrehozására tervezve.

**Erősségek**:
- **Testreszabhatóság**: A Carbon Charts lehetővé teszi a diagramok megjelenésének és viselkedésének kiterjedt testreszabását.
- **Nyílt forráskód**: Ingyenes és nyílt forráskódú, ami összhangban van a projekt költségbarát megoldások iránti követelményével.
- **Gyakori diagramok támogatása**: Támogatja a gyakori diagramtípusokat, mint a fánk-, radar- és területdiagram, bár hiányzik a fejlettebb típusok, mint a földrajzi térképek vagy gyertyadiagramok támogatása.

**Gyengeségek**:
- **Korlátozott fejlett diagramtípusok**: Nem támogat földrajzi térképeket, klaszterezési folyamat diagramokat vagy gyertyadiagramokat, amelyek elengedhetetlenek a projekthez.
- **Kisebb ökoszisztéma**: A Carbon Charts kisebb közösséggel és ökoszisztémával rendelkezik a nagyobb diagramkönyvtárakhoz, mint az ECharts vagy a Highcharts, képest.

**Ítélet**:  
A Carbon Charts nyílt forráskódú és testreszabható, de hiányzik belőle az ebben a projektben szükséges összetettebb diagramtípusok támogatása. Egyszerűbb diagramigényekhez alkalmasabb.

---

### 7. **Layer Cake**

**Áttekintés**:  
A Layer Cake egy adatvizualizációs könyvtár, rugalmas, rétegzett vizualizációk létrehozására tervezve.

**Erősségek**:
- **Testreszabható rétegek**: Erőteljes rétegezési lehetőségeket nyújt összetett vizualizációkhoz.
- **Nyílt forráskód**: Ingyenes és nyílt forráskódú, ami életképes lehetőséggé teszi költségvetés-érzékeny projektekhez.

**Gyengeségek**:
- **Korlátozott dokumentáció**: A Layer Cake-nek nincs kiterjedt dokumentációja és közösségi támogatása, ami nehezebbé teszi a vele való munkát az ismertebb könyvtárakhoz képest.
- **Nem diagramokhoz épült**: A Layer Cake alkalmasabb nem diagram jellegű vizualizációkhoz, ezért a készen kapható diagramlehetőségei korlátozottak.

**Ítélet**:  
Bár egyedi vizualizációkhoz érdekes, a Layer Cake nem ideális hagyományos diagramkövetelményekhez, mint a gyertyadiagramok vagy radardiagramok. Alkalmasabb a szabványos diagramok körén kívüli egyedi vizualizációkhoz.

---

### 8. **D3.js**

**Áttekintés**:  
A D3.js erőteljes JavaScript-könyvtár adatvezérelt vizualizációk létrehozására HTML, SVG és CSS segítségével.

**Erősségek**:
- **Páratlan rugalmasság**: A D3.js gyakorlatilag bármilyen egyedi vizualizáció létrehozását lehetővé teszi, ami nagyon erőssé teszi fejlett és interaktív diagramokhoz.
- **Kiterjedt funkciók**: Az összes szükséges diagramtípust támogatja, köztük a földrajzi térképeket, klaszterezési diagramokat és mást.
- **Testreszabhatóság**: A D3.js testreszabási szintje páratlan, lehetővé téve a fejlesztőknek, hogy erősen testre szabott vizualizációkat építsenek.

**Gyengeségek**:
- **Meredek tanulási görbe**: A D3.js tanulási görbéje meredek, és bonyolultabb integrálni, mint más könyvtárakat.
- **Időigényes**: A diagramok építése D3.js-ben időigényes lehet, különösen olyan gyakori diagramoknál, mint a gyertya- vagy fánkdiagramok.

**Ítélet**:  
A D3.js hihetetlenül erőteljes fejlett, egyedi diagramokhoz, de meredek tanulási görbéje és fejlesztési ideje miatt sok tipikus felhasználási esethez túlzás. Akkor a legjobb, ha a többi diagramkönyvtár nem nyújtja a szükséges testreszabási szintet.

---

### Összegzés

A könyvtárak projektigények szerinti értékelése után az **Apache ECharts** a legjobb lehetőségként emelkedik ki. Támogatja a szükséges diagramok teljes körét, beleértve a földrajzi térképeket, gyertyadiagramokat és klaszterezési diagramokat. Nyílt forráskódú, funkciógazdag és erősen interaktív, ami tökéletesen összhangban van a projekt céljaival. Bár a **D3.js** kínálja a legnagyobb rugalmasságot, összetettsége és időbefektetése kevésbé ideálissá teszi egy gyorsan iterálni kívánó startup számára. Az **ApexCharts** és a **Chart.js** jó alternatívák egyszerűbb projektekhez, de hiányzik belőlük a fejlett diagramtípusok támogatása.
