## Záznam architektonického rozhodnutia: framework na automatizáciu prehliadača pre E2E testovanie (Playwright alebo Selenium)

### 1. **Kontext**

Sme v procese výberu frameworku na automatizáciu prehliadača pre našu pipeline kompletného (end-to-end, E2E) testovania. Tento framework bude súčasťou našich CI/CD procesov a bude spúšťať testy, ktoré simulujú skutočné interakcie používateľov s našou platformou. Testy budú konkrétne pokrývať scenáre ako registrácia/prihlásenie používateľa, nahrávanie súborov, interakcie s dashboardom a sťahovanie reportov.

Ako **startup** sa zameriavame na **agilný vývoj** s potrebou rýchlo iterovať a vyvíjať sa. Náš tím pracuje prevažne s **TypeScriptom** a **Pythonom** a možnosť písať testy v týchto jazykoch je nevyhnutná. Platforma navyše obsahuje **interaktívne grafy a dashboardy**, preto je kľúčové, aby nástroj na automatizáciu dobre podporoval bohaté, dynamické používateľské rozhrania.

Dvaja kandidáti na túto úlohu sú **Playwright** a **Selenium**, každý so svojimi silnými stránkami a kompromismi. Musíme tieto frameworky vyhodnotiť na základe funkcií a požiadaviek uvedených nižšie.

### 2. **Zvažované možnosti**

- **Playwright** (od Microsoftu)
- **Selenium** (od projektu Selenium)

### 3. **Hnacie sily rozhodnutia**

Faktory ovplyvňujúce naše rozhodnutie sú tieto:

1. **Agilný vývoj**: Zvolený nástroj musí umožňovať rýchle, flexibilné vývojové cykly.
2. **Podpora jazykov**: Náš tím vyžaduje podporu **TypeScriptu** aj **Pythonu**.
3. **Testovanie interaktívneho UI**: Schopnosť spoľahlivo testovať interaktívne grafy, dashboardy a dynamické prvky je nevyhnutná.
4. **Rýchlosť behu**: Hoci nejde o primárnu starosť, výkon v CI/CD pipeline je zváženie.
5. **Škálovateľnosť**: V najbližšej dobe neplánujeme masívne škálovanie, ale chceme zabezpečiť, aby riešenie zvládlo budúci rast.
6. **Spätná kompatibilita**: Staršie systémy a kompatibilita so staršími prehliadačmi nie sú pre náš projekt momentálne kritické.
7. **Testovanie na mobilných zariadeniach**: Hoci to nie je bezprostredné zameranie, framework by mal byť schopný testovať mobilne responzívne funkcie alebo byť pre takéto prípady použitia rozšíriteľný.
8. **Testovanie s viacerými monitormi**: Podpora konfigurácií s viacerými monitormi je sekundárna požiadavka, najmä ak niekedy budeme škálovať na testovanie zložitejších používateľských pracovných postupov.
9. **Testovanie nahrávania súborov**: Framework musí efektívne zvládať nahrávanie súborov, čo je základná požiadavka našich potrieb testovania.

### 4. **Kritériá hodnotenia**

- **Jednoduchosť používania**: Aké ľahké je písať a udržiavať testy?
- **Podpora jazykov**: Podporuje framework TypeScript a Python, dva jazyky, ktoré náš tím používa najčastejšie?
- **Testovanie interaktívneho UI**: Ako dobre framework zvláda zložité, interaktívne používateľské rozhrania ako grafy, nahrávanie súborov a dynamické dáta?
- **Integrácia s CI/CD**: Ako dobre sa framework integruje do bežných CI/CD nástrojov a služieb?
- **Podpora viacerých prehliadačov**: Ktoré prehliadače sú podporované a ako dobre fungujú?
- **Výkon a rýchlosť**: Ako rýchlo sa testy vykonávajú, najmä v CI/CD pipeline?
- **Škálovateľnosť**: Ako dobre sa framework dokáže škálovať, ak sa pridá viac testov alebo zložitejšie scenáre?
- **Komunita a ekosystém**: Aká aktívna je komunita frameworku? Je k dispozícii veľa integrácií a rozšírení?

### 5. **Úvahy**

#### 5.1 **Playwright**

##### **Výhody**:
1. **Šikovnejšie API pre nahrávanie lokálnych súborov**: API Playwrightu na prácu s lokálnymi súbormi a nahrávanie súborov je jednoduchšie a intuitívnejšie. To by uľahčilo implementáciu a udržiavanie testov nahrávania súborov.
2. **Syntax a generovanie kódu**: Playwright má kratšiu, stručnejšiu syntax. To vedie k menšiemu množstvu boilerplate kódu, čo zlepšuje udržiavateľnosť a efektivitu vývojárov. Táto kratšia syntax navyše zlepšuje kvalitu generovania kódu pomocou OpenAI, čím uľahčuje automatické generovanie testovacích skriptov.
3. **Testovanie interaktívneho UI**: Playwright vyniká v testovaní dynamických, interaktívnych webových aplikácií, napríklad s bohatými grafmi, zložitými používateľskými interakciami a aktualizáciami v reálnom čase. Veľmi efektívne zvláda WebSockets, WebRTC, shadow DOM a ďalšie moderné webové technológie.
4. **Podpora viacerých prehliadačov**: Playwright podporuje **Chromium**, **WebKit** a **Firefox**. Má konzistentný výkon naprieč týmito prehliadačmi, čo by malo pokryť väčšinu našich potrieb testovania.
5. **Integrácia s CI/CD**: Playwright sa bezproblémovo integruje s modernými CI/CD platformami (GitHub Actions, Jenkins atď.). Dokáže spúšťať testy paralelne naprieč rôznymi prehliadačmi, čím optimalizuje časy behu testov a je vhodný pre rýchly vývoj.
6. **Rýchly a spoľahlivý**: Playwright je vo všeobecnosti rýchlejší než Selenium, najmä v headless režime, a odolnejší pri práci s asynchrónnymi webovými prvkami.

##### **Nevýhody**:
1. **Obmedzené testovanie na mobilných zariadeniach**: Hoci Playwright podporuje mobilnú emuláciu pre prehliadače, chýbajú mu natívne schopnosti mobilného testovania, ako je integrácia Selenia s Appiumom pre skutočné mobilné testovanie.
2. **Menší ekosystém**: Playwright je stále novší a menej etablovaný než Selenium. Hoci má rýchlo rastúcu komunitu a dobrú dokumentáciu, nemusí mať ešte rozsiahly ekosystém doplnkov a integrácií, ktorý ponúka Selenium.
3. **Obmedzená podpora prehliadačov**: Hoci Playwright pokrýva hlavné moderné prehliadače (Chrome, Safari, Firefox), jeho podpora starších prehliadačov (napr. Internet Explorer) nie je taká robustná ako podpora Selenia.

#### 5.2 **Selenium**

##### **Výhody**:
1. **Dlhšia história a zrelosť**: Selenium existuje dlho a má preukázané výsledky. Široko ho používajú mnohé tímy a odvetvia, čo viedlo k rozsiahlemu ekosystému doplnkov, integrácií a zdrojov.
2. **Podpora viacerých prehliadačov a platforiem**: Selenium podporuje **širokú škálu prehliadačov** a verzií vrátane **Internet Explorer** a dá sa integrovať aj s rôznymi nástrojmi ako **Docker**, **Selenium Grid** a **cloudové služby** pre distribuované testovanie.
3. **Testovanie na mobilných zariadeniach**: Selenium je vďaka integrácii s **Appium** oveľa robustnejšie pre mobilné testovanie vrátane aplikácií pre Android aj iOS. To z neho robí lepšiu voľbu pre projekty s mobilnou prioritou alebo silným mobilným zameraním.
4. **Testovanie s viacerými monitormi**: Selenium poskytuje lepšiu podporu pre scenáre zahŕňajúce **viacero monitorov** alebo zložité interakcie s viacerými oknami.

##### **Nevýhody**:
1. **Zložitosť**: API Selenia je podrobnejšie a explicitnejšie. Hoci to môže byť v niektorých prípadoch výhoda, znamená to viac kódu na písanie a udržiavanie, čo môže znížiť agilitu vývojárov — obzvlášť dôležitú v prostredí startupu.
2. **Výkon**: Selenium sa vo všeobecnosti vykonáva pomalšie než Playwright, najmä v headless režime. To by mohlo ovplyvniť CI/CD pipeline, najmä s rastúcim počtom testov.
3. **Testovanie interaktívneho UI**: Selenium nie je také plynulé ako Playwright pri testovaní moderných, interaktívnych webových UI, najmä s grafmi a aktualizáciami dát v reálnom čase. Vyžaduje viac nastavovania a spracovania na spoľahlivú interakciu s dynamickým obsahom.

### 6. **Zhrnutie porovnania**

| Funkcia                          | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Jednoduchosť používania**                   | Kratšia syntax, intuitívnejší pre moderné UI | Explicitnejšie, vyžaduje viac boilerplate kódu  |
| **Podpora jazykov**              | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Testovanie interaktívneho UI**        | Vynikajúci pre dynamické UI v reálnom čase          | Zvláda základné UI, ale podrobnejší a zložitejší pre bohaté interakcie |
| **Testovanie nahrávania súborov**           | Šikovnejšie API pre nahrávanie súborov                  | Podrobnejšie, menej intuitívne API         |
| **Integrácia s CI/CD**             | Jednoduchá integrácia s GitHub Actions, Jenkins | Silná integrácia s mnohými CI nástrojmi    |
| **Testovanie na mobilných zariadeniach**                | Obmedzené, iba emulácia                       | Plná podpora cez Appium               |
| **Podpora viacerých prehliadačov**         | Chromium, WebKit, Firefox                     | Plná podpora naprieč hlavnými aj staršími prehliadačmi |
| **Výkon**                   | Rýchly, optimalizovaný pre headless testovanie          | Pomalší, najmä v headless režime       |
| **Testovanie s viacerými monitormi**         | Obmedzené                                       | Dobrá podpora pre nastavenia s viacerými monitormi    |
| **Komunita a ekosystém**       | Rastúca, dobrá dokumentácia                   | Veľká, zrelá, rozsiahly ekosystém       |

### 7. **Rozhodnutie**

Po zvážení požiadaviek a kompromisov je **Playwright** lepšou voľbou pre naše súčasné potreby. Jeho šikovnejšie API na testovanie nahrávania lokálnych súborov, stručná syntax a silná podpora testovania interaktívneho UI z neho robia ideálnu voľbu pre náš cyklus agilného vývoja. Skutočnosť, že podporuje **TypeScript** aj **Python**, je pre náš tím kľúčová a moderný prístup frameworku k testovaniu nám umožní písať čistý, udržiavateľný kód.

Hoci **Selenium** zostáva skvelým nástrojom, najmä pre mobilné testovanie, podporu starších prehliadačov a nastavenia s viacerými monitormi, je pre naše súčasné potreby menej vhodný. Jeho rozvláčnosť, pomalší výkon a zložitejšie zaobchádzanie s dynamickými UI ako grafy ho robia pre náš prípad použitia menej optimálnym.

### 8. **Dôsledky**

- **Okamžitá akcia**: Prijmeme **Playwright** pre naše E2E testovanie so zameraním na testovanie používateľských tokov zahŕňajúcich registráciu, prihlásenie, nahrávanie súborov, dashboardy a sťahovanie reportov.
- **Dlhodobé úvahy**: Budeme sledovať vyvíjajúci sa ekosystém Playwrightu. Ak sa naše potreby zmenia, najmä v oblasti mobilného testovania alebo podpory starších prehliadačov, môžeme Selenium znovu zvážiť.
- **Školenie a dokumentácia**: Vývojové tímy sa budú musieť oboznámiť s API Playwrightu, najmä pre prácu s dynamickými UI a nahrávaním súborov.
- **Migrácia**: Existujúce testy Selenia (ak nejaké sú) budú postupne migrované na Playwright.

### 9. **Budúce úvahy**

