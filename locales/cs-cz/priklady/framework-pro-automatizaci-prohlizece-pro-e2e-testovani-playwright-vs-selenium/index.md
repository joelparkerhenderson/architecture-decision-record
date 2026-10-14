## Záznam architektonického rozhodnutí: framework pro automatizaci prohlížeče pro E2E testování (Playwright vs Selenium)

### 1. **Kontext**

Vybíráme framework pro automatizaci prohlížeče pro náš kontinuální proces end-to-end (E2E) testování. Tento framework bude nedílnou součástí našich procesů CI/CD a bude spouštět testy simulující skutečné interakce uživatelů s naší platformou. Konkrétně testy pokryjí scénáře jako registrace/přihlášení uživatele, nahrávání souborů, interakce s dashboardy a stahování reportů.

Jako **startup** se zaměřujeme na **agilní vývoj** s potřebou rychle iterovat a vyvíjet se. Náš tým pracuje převážně s **TypeScriptem** a **Pythonem** a schopnost psát testy v těchto jazycích je nezbytná. Platforma navíc obsahuje **interaktivní grafy a dashboardy**, takže je kritické, aby nástroj pro automatizaci dobře podporoval bohaté, dynamické uživatelské rozhraní.

Dva kandidáti na tento úkol jsou **Playwright** a **Selenium**, každý se svými silnými stránkami a kompromisy. Tyto frameworky musíme vyhodnotit na základě funkcí a požadavků uvedených níže.

### 2. **Zvažované možnosti**

- **Playwright** (od Microsoftu)
- **Selenium** (od projektu Selenium)

### 3. **Rozhodovací faktory**

Faktory ovlivňující naše rozhodnutí jsou následující:

1. **Agilní vývoj**: Zvolený nástroj musí umožňovat rychlé, flexibilní vývojové cykly.
2. **Podpora jazyků**: Náš tým vyžaduje podporu jak pro **TypeScript**, tak pro **Python**.
3. **Testování interaktivního UI**: Schopnost spolehlivě testovat interaktivní grafy, dashboardy a dynamické prvky je nezbytná.
4. **Rychlost běhu**: Ačkoli to není hlavní priorita, výkon v pipeline CI/CD je třeba zvážit.
5. **Škálovatelnost**: V nejbližší době neplánujeme masivní škálování, ale chceme zajistit, aby řešení zvládlo budoucí růst.
6. **Zpětná kompatibilita**: Starší systémy a kompatibilita se staršími prohlížeči nejsou pro náš projekt v tuto chvíli kritické.
7. **Mobilní testování**: Přestože to není okamžité zaměření, framework by měl umět testovat funkce přizpůsobené mobilům nebo být pro takové případy rozšiřitelný.
8. **Testování na více monitorech**: Podpora konfigurací s více monitory je sekundární požadavek, zejména pokud někdy budeme škálovat na testování složitějších uživatelských pracovních postupů.
9. **Testování nahrávání souborů**: Framework musí efektivně zvládat nahrávání souborů, což je základní požadavek našich testů.

### 4. **Hodnoticí kritéria**

- **Snadnost použití**: Jak snadné je psát a udržovat testy?
- **Podpora jazyků**: Podporuje framework TypeScript a Python, dva jazyky, které náš tým používá nejčastěji?
- **Testování interaktivního UI**: Jak dobře framework zvládá složitá, interaktivní uživatelská rozhraní, jako jsou grafy, nahrávání souborů a dynamická data?
- **Integrace CI/CD**: Jak dobře se framework integruje do běžných nástrojů a služeb CI/CD?
- **Podpora více prohlížečů**: Které prohlížeče jsou podporovány a jak dobře fungují?
- **Výkon a rychlost**: Jak rychle testy běží, zejména v pipeline CI/CD?
- **Škálovatelnost**: Jak dobře se framework škáluje, pokud se přidá více testů nebo složitějších scénářů?
- **Komunita a ekosystém**: Jak aktivní je komunita frameworku? Je k dispozici mnoho integrací a rozšíření?

### 5. **Úvahy**

#### 5.1 **Playwright**

##### **Výhody**:
1. **Chytřejší API pro nahrávání lokálních souborů**: API Playwrightu pro práci s lokálními soubory a provádění nahrávání souborů je jednodušší a intuitivnější. To by usnadnilo implementaci a údržbu testů nahrávání souborů.
2. **Syntaxe a generování kódu**: Playwright má kratší, stručnější syntaxi. To vede k menšímu množství šablonového kódu, což zlepšuje udržovatelnost a efektivitu vývojářů. Tato kratší syntaxe navíc zlepšuje kvalitu generování kódu pomocí OpenAI, takže je snazší automaticky generovat testovací skripty.
3. **Testování interaktivního UI**: Playwright vyniká při testování dynamických, interaktivních webových aplikací, například těch s bohatými grafy, složitými uživatelskými interakcemi a aktualizacemi v reálném čase. Velmi efektivně zvládá WebSockets, WebRTC, shadow DOM a další moderní webové technologie.
4. **Podpora více prohlížečů**: Playwright podporuje **Chromium**, **WebKit** a **Firefox**. Má konzistentní výkon napříč těmito prohlížeči, což by mělo pokrýt většinu našich testovacích potřeb.
5. **Integrace CI/CD**: Playwright se bez problémů integruje s moderními platformami CI/CD (GitHub Actions, Jenkins atd.). Může spouštět testy paralelně v různých prohlížečích, optimalizovat doby běhu testů a je vhodný pro rychlý vývoj.
6. **Rychlý a spolehlivý**: Playwright je obecně rychlejší než Selenium, zejména v režimu headless, a odolnější při práci s asynchronními webovými prvky.

##### **Nevýhody**:
1. **Omezené mobilní testování**: Ačkoli Playwright podporuje emulaci mobilních zařízení pro prohlížeče, chybí mu nativní schopnosti mobilního testování, jako je integrace Selenium s Appium pro skutečné mobilní testování.
2. **Menší ekosystém**: Playwright je stále novější a méně zavedený než Selenium. Přestože má rychle rostoucí komunitu a dobrou dokumentaci, nemusí mít ještě rozsáhlý ekosystém zásuvných modulů a integrací, který nabízí Selenium.
3. **Omezená podpora prohlížečů**: Přestože Playwright pokrývá hlavní moderní prohlížeče (Chrome, Safari, Firefox), jeho podpora starších prohlížečů (např. Internet Explorer) není tak robustní jako u Selenium.

#### 5.2 **Selenium**

##### **Výhody**:
1. **Delší historie a vyspělost**: Selenium existuje dlouho a má osvědčenou historii. Je široce používáno v mnoha týmech a odvětvích, což vedlo k rozsáhlému ekosystému zásuvných modulů, integrací a zdrojů.
2. **Podpora více prohlížečů a platforem**: Selenium podporuje **širokou škálu prohlížečů** a verzí, včetně **Internet Exploreru**, a lze jej integrovat i s různými nástroji, jako jsou **Docker**, **Selenium Grid** a **cloudové služby** pro distribuované testování.
3. **Mobilní testování**: Selenium je díky integraci s **Appium** mnohem robustnější pro mobilní testování, včetně aplikací pro Android a iOS. To z něj činí lepší volbu pro projekty zaměřené na mobily.
4. **Testování na více monitorech**: Selenium poskytuje lepší podporu scénářů zahrnujících **více monitorů** nebo složité interakce s více okny.

##### **Nevýhody**:
1. **Složitost**: API Selenium je rozvláčnější a explicitnější. Ačkoli to může být v některých případech výhoda, znamená to více kódu k napsání a údržbě, což může snížit agilitu vývojářů — zvlášť důležitou v prostředí startupu.
2. **Výkon**: Selenium obecně běží pomaleji než Playwright, zejména v režimu headless. To by mohlo ovlivnit pipeline CI/CD, zejména s rostoucím počtem testů.
3. **Testování interaktivního UI**: Selenium není tak plynulé jako Playwright při testování moderních, interaktivních webových rozhraní, zejména s grafy a aktualizacemi dat v reálném čase. Vyžaduje více nastavení a obsluhy pro spolehlivou interakci s dynamickým obsahem.

### 6. **Shrnutí srovnání**

| Vlastnost                        | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Snadnost použití**              | Kratší syntaxe, intuitivnější pro moderní UI  | Explicitnější, vyžaduje více šablonového kódu  |
| **Podpora jazyků**                | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Testování interaktivního UI**   | Vynikající pro dynamická UI v reálném čase    | Zvládá základní UI, ale rozvláčnější a složitější pro bohaté interakce |
| **Testování nahrávání souborů**   | Chytřejší API pro nahrávání souborů           | Rozvláčnější, méně intuitivní API         |
| **Integrace CI/CD**               | Snadná integrace s GitHub Actions, Jenkins    | Silná integrace s mnoha nástroji CI       |
| **Mobilní testování**             | Omezené, jen emulace                          | Plná podpora přes Appium                  |
| **Podpora více prohlížečů**       | Chromium, WebKit, Firefox                     | Plná podpora hlavních i starších prohlížečů |
| **Výkon**                         | Rychlý, optimalizovaný pro testování headless | Pomalejší, zejména v režimu headless      |
| **Testování na více monitorech**  | Omezené                                       | Dobrá podpora nastavení s více monitory   |
| **Komunita a ekosystém**          | Rostoucí, dobrá dokumentace                   | Velká, vyspělá, rozsáhlý ekosystém        |

### 7. **Rozhodnutí**

Po zvážení požadavků a kompromisů je **Playwright** lepší volbou pro naše současné potřeby. Jeho chytřejší API pro testování nahrávání lokálních souborů, stručná syntaxe a silná podpora testování interaktivního UI z něj činí ideální volbu pro náš agilní vývojový cyklus. Skutečnost, že podporuje jak **TypeScript**, tak **Python**, je pro náš tým kritická a moderní přístup frameworku k testování nám umožní psát čistý, udržovatelný kód.

Ačkoli **Selenium** zůstává skvělým nástrojem, zejména pro mobilní testování, podporu starších prohlížečů a nastavení s více monitory, je pro naše současné potřeby méně vhodné. Jeho rozvláčnost, pomalejší výkon a složitější zpracování dynamických UI, jako jsou grafy, ho činí pro náš případ použití méně optimálním.

### 8. **Důsledky**

- **Okamžitá akce**: Pro naše E2E testování přijmeme **Playwright** se zaměřením na testování uživatelských toků zahrnujících registraci, přihlášení, nahrávání souborů, dashboardy a stahování reportů.
- **Dlouhodobé úvahy**: Budeme sledovat vyvíjející se ekosystém Playwrightu. Pokud se naše potřeby změní, zejména v oblasti mobilního testování nebo podpory starších prohlížečů, můžeme se k Selenium vrátit.
- **Školení a dokumentace**: Vývojové týmy se budou muset seznámit s API Playwrightu, zejména pro zpracování dynamických UI a nahrávání souborů.
- **Migrace**: Stávající testy Selenium (pokud existují) budou postupně migrovány na Playwright.

### 9. **Budoucí úvahy**
