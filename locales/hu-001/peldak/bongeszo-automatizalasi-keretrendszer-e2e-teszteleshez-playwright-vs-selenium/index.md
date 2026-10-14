## Architekturális döntési feljegyzés: böngészőautomatizálási keretrendszer E2E teszteléshez (Playwright vs Selenium)

### 1. **Háttér**

Böngészőautomatizálási keretrendszert választunk az end-to-end (E2E) tesztelési folyamatunkhoz. Ez a keretrendszer szerves része lesz a CI/CD-folyamatainknak, olyan teszteket futtatva, amelyek valós felhasználói interakciókat szimulálnak a platformunkon. Konkrétan a tesztek olyan forgatókönyveket fednek le, mint a felhasználói regisztráció/bejelentkezés, fájlfeltöltések, irányítópult-interakciók és jelentések letöltése.

**Startupként** az **agilis fejlesztésre** összpontosítunk, a gyors iteráció és fejlődés igényével. Csapatunk főként **TypeScripttel** és **Pythonnal** dolgozik, és elengedhetetlen, hogy ezeken a nyelveken lehessen teszteket írni. Ezenkívül a platform **interaktív diagramokat és irányítópultokat** tartalmaz, ezért kritikus, hogy az automatizálási eszköz jól támogassa a gazdag, dinamikus felhasználói felületeket.

A feladatra két jelölt van, a **Playwright** és a **Selenium**, mindkettőnek megvannak az erősségei és kompromisszumai. Ezeket a keretrendszereket az alább felvázolt funkciók és követelmények alapján kell értékelnünk.

### 2. **Megfontolt lehetőségek**

- **Playwright** (a Microsofttól)
- **Selenium** (a Selenium Projecttől)

### 3. **Döntési tényezők**

A döntésünket befolyásoló tényezők a következők:

1. **Agilis fejlesztés**: A választott eszköznek gyors, rugalmas fejlesztési ciklusokat kell lehetővé tennie.
2. **Nyelvtámogatás**: Csapatunknak mind a **TypeScript**, mind a **Python** támogatására szüksége van.
3. **Interaktív felület tesztelése**: Elengedhetetlen az interaktív diagramok, irányítópultok és dinamikus elemek megbízható tesztelésének képessége.
4. **Futási sebesség**: Bár nem elsődleges szempont, a teljesítmény a CI/CD-folyamatokban megfontolandó.
5. **Skálázhatóság**: A közeljövőben nem tervezünk masszív skálázást, de biztosítani akarjuk, hogy a megoldás kezelni tudja a jövőbeli növekedést.
6. **Visszamenőleges kompatibilitás**: A régi rendszerek és a régebbi böngészőkkel való kompatibilitás jelenleg nem kritikus a projektünk számára.
7. **Mobil tesztelés**: Bár nem azonnali fókusz, a keretrendszernek képesnek kell lennie mobilra reszponzív funkciók tesztelésére, vagy bővíthetőnek kell lennie ilyen felhasználási esetekre.
8. **Több monitoros tesztelés**: A több monitoros konfigurációk támogatása másodlagos követelmény, főleg ha valaha összetettebb felhasználói munkafolyamatok tesztelésére skálázunk.
9. **Fájlfeltöltés tesztelése**: A keretrendszernek hatékonyan kell kezelnie a fájlfeltöltéseket, ami a tesztelési igényeink alapkövetelménye.

### 4. **Értékelési kritériumok**

- **Használhatóság**: Mennyire egyszerű tesztek írása és karbantartása?
- **Nyelvtámogatás**: Támogatja-e a keretrendszer a TypeScriptet és a Pythont, azt a két nyelvet, amelyet csapatunk a leggyakrabban használ?
- **Interaktív felület tesztelése**: Mennyire jól kezeli a keretrendszer az összetett, interaktív felhasználói felületeket, mint a diagramok, fájlfeltöltések és dinamikus adatok?
- **CI/CD-integráció**: Mennyire jól integrálódik a keretrendszer a gyakori CI/CD-eszközökbe és -szolgáltatásokba?
- **Több böngésző támogatása**: Mely böngészők támogatottak, és mennyire jól teljesítenek?
- **Teljesítmény és sebesség**: Milyen gyorsan futnak a tesztek, különösen CI/CD-folyamatban?
- **Skálázhatóság**: Mennyire skálázható a keretrendszer, ha több tesztet vagy összetettebb forgatókönyveket adnak hozzá?
- **Közösség és ökoszisztéma**: Mennyire aktív a keretrendszer közössége? Rendelkezésre áll-e sok integráció és bővítmény?

### 5. **Megfontolások**

#### 5.1 **Playwright**

##### **Előnyök**:
1. **Okosabb API a helyi fájlfeltöltésekhez**: A Playwright API-ja a helyi fájlokkal való interakcióhoz és a fájlfeltöltések végrehajtásához egyszerűbb és intuitívabb. Ez megkönnyítené a fájlfeltöltés-tesztelés megvalósítását és karbantartását.
2. **Szintaxis és kódgenerálás**: A Playwright rövidebb, tömörebb szintaxissal rendelkezik. Ez kevesebb sablonkódot eredményez, ami javítja a karbantarthatóságot és a fejlesztői hatékonyságot. Ezenkívül ez a rövidebb szintaxis javítja az OpenAI kódgenerálás minőségét, megkönnyítve a tesztszkriptek automatikus előállítását.
3. **Interaktív felület tesztelése**: A Playwright kiválóan tesztel dinamikus, interaktív webalkalmazásokat, például gazdag diagramokkal, összetett felhasználói interakciókkal és valós idejű frissítésekkel rendelkezőket. Nagyon hatékonyan kezeli a WebSocketeket, a WebRTC-t, a shadow DOM-ot és más modern webes technológiákat.
4. **Több böngésző támogatása**: A Playwright támogatja a **Chromiumot**, a **WebKitet** és a **Firefoxot**. Következetes teljesítményt nyújt ezeken a böngészőkön, ami a legtöbb tesztelési igényünket le kell fedje.
5. **CI/CD-integráció**: A Playwright zökkenőmentesen integrálódik a modern CI/CD-platformokkal (GitHub Actions, Jenkins stb.). Párhuzamosan tud tesztet futtatni különböző böngészőkön, optimalizálva a tesztfutási időket és alkalmassá téve a gyors fejlesztésre.
6. **Gyors és megbízható**: A Playwright általában gyorsabb a Seleniumnál, különösen headless módban, és ellenállóbb az aszinkron webes elemek kezelésében.

##### **Hátrányok**:
1. **Korlátozott mobil tesztelés**: Bár a Playwright támogatja a mobil emulációt böngészőkhöz, hiányoznak belőle a natív mobil tesztelési képességek, mint a Selenium Appiummal való integrációja a valódi mobil teszteléshez.
2. **Kisebb ökoszisztéma**: A Playwright még újabb és kevésbé megalapozott, mint a Selenium. Bár gyorsan növekvő közössége és jó dokumentációja van, még nem biztos, hogy rendelkezik a Selenium által kínált hatalmas bővítmény- és integrációs ökoszisztémával.
3. **Korlátozott böngészőtámogatás**: Bár a Playwright lefedi a főbb modern böngészőket (Chrome, Safari, Firefox), a régi böngészők (pl. Internet Explorer) támogatása nem olyan erős, mint a Seleniumé.

#### 5.2 **Selenium**

##### **Előnyök**:
1. **Hosszabb történet és érettség**: A Selenium régóta létezik, és bizonyított eredménytörténete van. Széles körben használják sok csapatnál és iparágban, ami bővítmények, integrációk és források hatalmas ökoszisztémájához vezetett.
2. **Több böngésző és platform támogatása**: A Selenium **böngészők és verziók széles választékát** támogatja, beleértve az **Internet Explorert**, és integrálható különféle eszközökkel is, mint a **Docker**, a **Selenium Grid** és a **felhőszolgáltatások** az elosztott teszteléshez.
3. **Mobil tesztelés**: A Selenium az **Appiummal** való integrációja révén sokkal robusztusabb a mobil teszteléshez, beleértve az Android- és iOS-alkalmazásokat. Ez a jobb választás mobil-első vagy erősen mobilos fókuszú projektekhez.
4. **Több monitoros tesztelés**: A Selenium jobb támogatást nyújt a **több monitort** vagy összetett többablakos interakciókat érintő forgatókönyvekhez.

##### **Hátrányok**:
1. **Bonyolultság**: A Selenium API-ja bőbeszédűbb és explicitebb. Bár ez bizonyos esetekben előny lehet, több kódot jelent írni és karbantartani, ami csökkentheti a fejlesztői agilitást — ez különösen fontos startup környezetben.
2. **Teljesítmény**: A Selenium általában lassabban fut, mint a Playwright, különösen headless módban. Ez hatással lehet a CI/CD-folyamatokra, különösen a tesztek számának növekedésével.
3. **Interaktív felület tesztelése**: A Selenium nem olyan zökkenőmentes, mint a Playwright a modern, interaktív webes felületek tesztelésében, különösen diagramokkal és valós idejű adatfrissítésekkel. Több beállítást és kezelést igényel a dinamikus tartalommal való megbízható interakcióhoz.

### 6. **Összehasonlítás összefoglalója**

| Szempont                         | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Használhatóság**                | Rövidebb szintaxis, intuitívabb modern felületekhez | Explicitebb, több sablonkódot igényel  |
| **Nyelvtámogatás**                | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Interaktív felület tesztelése** | Kiváló dinamikus, valós idejű felületekhez    | Kezeli az alapvető felületeket, de bőbeszédűbb és bonyolultabb gazdag interakciókhoz |
| **Fájlfeltöltés tesztelése**      | Okosabb API a fájlfeltöltésekhez              | Bőbeszédűbb, kevésbé intuitív API         |
| **CI/CD-integráció**              | Egyszerű integráció a GitHub Actions-szel, Jenkinsszel | Erős integráció sok CI-eszközzel    |
| **Mobil tesztelés**               | Korlátozott, csak emuláció                    | Teljes támogatás Appiumon keresztül       |
| **Több böngésző támogatása**      | Chromium, WebKit, Firefox                     | Teljes támogatás a főbb és régi böngészőkre |
| **Teljesítmény**                  | Gyors, headless tesztelésre optimalizált      | Lassabb, különösen headless módban        |
| **Több monitoros tesztelés**      | Korlátozott                                   | Jó támogatás több monitoros beállításokhoz |
| **Közösség és ökoszisztéma**      | Növekvő, jó dokumentáció                      | Nagy, érett, kiterjedt ökoszisztéma       |

### 7. **Döntés**

A követelmények és kompromisszumok mérlegelése után a **Playwright** a jobb választás jelenlegi igényeinkhez. Okosabb API-ja a helyi fájlfeltöltés teszteléséhez, tömör szintaxisa és erős támogatása az interaktív felületek teszteléséhez ideálissá teszik agilis fejlesztési ciklusunkhoz. Az, hogy mind a **TypeScriptet**, mind a **Pythont** támogatja, kritikus csapatunk számára, és a keretrendszer modern megközelítése a teszteléshez lehetővé teszi, hogy tiszta, karbantartható kódot írjunk.

Bár a **Selenium** továbbra is kiváló eszköz, különösen a mobil teszteléshez, a régi böngészők támogatásához és a több monitoros beállításokhoz, kevésbé illik jelenlegi igényeinkhez. Bőbeszédűsége, lassabb teljesítménye és a dinamikus felületek, például diagramok bonyolultabb kezelése kevésbé optimálissá teszik felhasználási esetünkre.

### 8. **Következmények**

- **Azonnali lépés**: A **Playwrightot** vezetjük be az E2E teszteléshez, a regisztrációt, bejelentkezést, fájlfeltöltéseket, irányítópultokat és jelentésletöltéseket érintő felhasználói folyamatok tesztelésére összpontosítva.
- **Hosszú távú megfontolások**: Figyelemmel kísérjük a Playwright fejlődő ökoszisztémáját. Ha igényeink megváltoznak, különösen a mobil tesztelés vagy a régi böngészők támogatása terén, újra megfontolhatjuk a Seleniumot.
- **Képzés és dokumentáció**: A fejlesztőcsapatoknak meg kell ismerkedniük a Playwright API-jával, különösen a dinamikus felületek és fájlfeltöltések kezeléséhez.
- **Migráció**: A meglévő Selenium-teszteket (ha vannak) fokozatosan áttelepítjük a Playwrightra.

### 9. **Jövőbeli megfontolások**
