## Architektūros sprendimo įrašas: naršyklės automatizavimo karkasas E2E testavimui (Playwright ar Selenium)

### 1. **Kontekstas**

Renkamės naršyklės automatizavimo karkasą savo visapusiško (angl. end-to-end, E2E) testavimo konvejeriui. Šis karkasas bus neatsiejama mūsų CI/CD procesų dalis ir vykdys testus, imituojančius realias naudotojų sąveikas mūsų platformoje. Konkrečiai, testai apims tokius scenarijus kaip naudotojo registracija / prisijungimas, failų įkėlimas, sąveika su skydeliais ir ataskaitų atsisiuntimas.

Kaip **startuolis**, dėmesį skiriame **lanksčiajam kūrimui**, todėl turime sparčiai iteruoti ir tobulėti. Mūsų komanda daugiausia dirba su **TypeScript** ir **Python**, todėl būtina galėti rašyti testus šiomis kalbomis. Be to, platformoje yra **interaktyvių diagramų ir skydelių**, todėl labai svarbu, kad automatizavimo įrankis gerai palaikytų turtingas, dinamiškas sąsajas.

Du kandidatai šiai užduočiai yra **Playwright** ir **Selenium**, kurių kiekvienas turi savo stipriąsias puses ir kompromisus. Šiuos karkasus turime įvertinti pagal toliau nurodytas funkcijas ir reikalavimus.

### 2. **Svarstyti variantai**

- **Playwright** (Microsoft)
- **Selenium** (Selenium Project)

### 3. **Sprendimo veiksniai**

Sprendimą lemiantys veiksniai yra šie:

1. **Lankstusis kūrimas**: pasirinktas įrankis turi leisti greitus, lanksčius kūrimo ciklus.
2. **Kalbų palaikymas**: mūsų komandai reikia tiek **TypeScript**, tiek **Python** palaikymo.
3. **Interaktyvios sąsajos testavimas**: būtina patikimai testuoti interaktyvias diagramas, skydelius ir dinamiškus elementus.
4. **Vykdymo greitis**: nors tai nėra pagrindinis rūpestis, našumas CI/CD konvejeriuose yra svarstytinas dalykas.
5. **Mastelio keitimas**: artimiausiu metu nesiruošiame labai didelio masto, bet norime užtikrinti, kad sprendimas atlaikytų būsimą augimą.
6. **Atgalinis suderinamumas**: paveldėtos sistemos ir suderinamumas su senesnėmis naršyklėmis šiuo metu mūsų projektui nėra kritiški.
7. **Mobilusis testavimas**: nors tai nėra neatidėliotinas dėmesio centras, karkasas turėtų galėti testuoti prisitaikančias mobiliąsias funkcijas arba būti išplečiamas tokiems naudojimo atvejams.
8. **Testavimas keliuose monitoriuose**: kelių monitorių konfigūracijų palaikymas yra antrinis reikalavimas, ypač jei kada nors pereisime prie sudėtingesnių naudotojų darbo eigų testavimo.
9. **Failų įkėlimo testavimas**: karkasas turi efektyviai tvarkyti failų įkėlimą, kuris yra pagrindinis mūsų testavimo poreikis.

### 4. **Vertinimo kriterijai**

- **Naudojimo paprastumas**: kaip lengva rašyti ir prižiūrėti testus?
- **Kalbų palaikymas**: ar karkasas palaiko TypeScript ir Python – dvi kalbas, kurias mūsų komanda naudoja dažniausiai?
- **Interaktyvios sąsajos testavimas**: kaip gerai karkasas tvarko sudėtingas, interaktyvias naudotojo sąsajas, tokias kaip diagramos, failų įkėlimai ir dinaminiai duomenys?
- **CI/CD integracija**: kaip gerai karkasas integruojasi su įprastais CI/CD įrankiais ir paslaugomis?
- **Palaikymas keliose naršyklėse**: kokios naršyklės palaikomos ir kaip gerai jos veikia?
- **Našumas ir greitis**: kaip greitai vykdomi testai, ypač CI/CD konvejeryje?
- **Mastelio keitimas**: kaip gerai karkasas keičia mastelį, jei pridedama daugiau testų ar sudėtingesnių scenarijų?
- **Bendruomenė ir ekosistema**: kiek aktyvi karkaso bendruomenė? Ar yra daug integracijų ir plėtinių?

### 5. **Svarstymai**

#### 5.1 **Playwright**

##### **Privalumai**:
1. **Išmanesnė API vietinių failų įkėlimui**: Playwright API sąveikai su vietiniais failais ir failų įkėlimui atlikti yra paprastesnė ir intuityvesnė. Tai palengvintų failų įkėlimo testavimo įgyvendinimą ir priežiūrą.
2. **Sintaksė ir kodo generavimas**: Playwright turi trumpesnę, glaustesnę sintaksę. Dėl to mažiau šabloninio kodo, o tai pagerina prižiūrimumą ir programuotojų efektyvumą. Be to, ši trumpesnė sintaksė pagerina OpenAI kodo generavimo kokybę, todėl lengviau automatiškai generuoti testų scenarijus.
3. **Interaktyvios sąsajos testavimas**: Playwright puikiai tinka dinaminėms, interaktyvioms interneto programoms testuoti, pavyzdžiui, turinčioms turtingas diagramas, sudėtingas naudotojų sąveikas ir realaus laiko atnaujinimus. Jis labai veiksmingai tvarko WebSockets, WebRTC, shadow DOM ir kitas modernias interneto technologijas.
4. **Palaikymas keliose naršyklėse**: Playwright palaiko **Chromium**, **WebKit** ir **Firefox**. Jis veikia nuosekliai šiose naršyklėse, o tai turėtų padengti daugumą mūsų testavimo poreikių.
5. **CI/CD integracija**: Playwright sklandžiai integruojasi su šiuolaikinėmis CI/CD platformomis (GitHub Actions, Jenkins ir kt.). Jis gali vykdyti testus lygiagrečiai skirtingose naršyklėse, optimizuodamas testų vykdymo laiką, todėl tinka spartiam kūrimui.
6. **Greitas ir patikimas**: Playwright apskritai yra greitesnis nei Selenium, ypač be grafinės sąsajos (headless) režimu, ir atsparesnis dirbant su asinchroniniais interneto elementais.

##### **Trūkumai**:
1. **Ribotas mobilusis testavimas**: nors Playwright palaiko mobiliųjų įrenginių emuliaciją naršyklėse, jam trūksta savitų mobiliojo testavimo galimybių, tokių kaip Selenium integracija su Appium tikram mobiliajam testavimui.
2. **Mažesnė ekosistema**: Playwright vis dar naujesnis ir mažiau įsitvirtinęs nei Selenium. Nors jis turi sparčiai augančią bendruomenę ir gerą dokumentaciją, jis gali dar neturėti tokios didžiulės papildinių ir integracijų ekosistemos kaip Selenium.
3. **Ribotas naršyklių palaikymas**: nors Playwright apima pagrindines modernias naršykles (Chrome, Safari, Firefox), jo paveldėtų naršyklių (pvz., Internet Explorer) palaikymas nėra toks tvirtas kaip Selenium.

#### 5.2 **Selenium**

##### **Privalumai**:
1. **Ilgesnė istorija ir branda**: Selenium egzistuoja jau seniai ir turi įrodytą patirtį. Jis plačiai naudojamas daugelyje komandų ir pramonės šakų, todėl susiformavo didžiulė papildinių, integracijų ir išteklių ekosistema.
2. **Palaikymas įvairiose naršyklėse ir platformose**: Selenium palaiko **labai įvairias naršykles** ir versijas, įskaitant **Internet Explorer**, ir taip pat gali būti integruotas su įvairiais įrankiais, tokiais kaip **Docker**, **Selenium Grid** ir **debesijos paslaugos** paskirstytam testavimui.
3. **Mobilusis testavimas**: Selenium per savo integraciją su **Appium** yra daug tvirtesnis mobiliajam testavimui, įskaitant ir Android, ir iOS programas. Todėl tai geresnis pasirinkimas projektams, orientuotiems pirmiausia į mobiliuosius ar daug dėmesio skiriantiems mobiliesiems.
4. **Testavimas keliuose monitoriuose**: Selenium geriau palaiko scenarijus, apimančius **kelis monitorius** ar sudėtingas kelių langų sąveikas.

##### **Trūkumai**:
1. **Sudėtingumas**: Selenium API yra daugiažodiškesnė ir aiškesnė. Nors kai kuriais atvejais tai gali būti privalumas, tai reiškia daugiau kodo rašyti ir prižiūrėti, o tai gali sumažinti programuotojų judrumą – o tai ypač svarbu startuolio aplinkoje.
2. **Našumas**: Selenium paprastai veikia lėčiau nei Playwright, ypač be grafinės sąsajos (headless) režimu. Tai gali paveikti CI/CD konvejerius, ypač augant testų skaičiui.
3. **Interaktyvios sąsajos testavimas**: Selenium nėra toks sklandus kaip Playwright testuojant modernias, interaktyvias interneto sąsajas, ypač su diagramomis ir realaus laiko duomenų atnaujinimais. Norint patikimai sąveikauti su dinaminiu turiniu, reikia daugiau sąrankos ir tvarkymo.

### 6. **Palyginimo santrauka**

| Savybė                           | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Naudojimo paprastumas**         | Trumpesnė sintaksė, intuityvesnė modernioms sąsajoms | Aiškesnė, reikia daugiau šabloninio kodo  |
| **Kalbų palaikymas**              | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Interaktyvios sąsajos testavimas** | Puikus dinaminėms, realaus laiko sąsajoms  | Tvarko paprastas sąsajas, bet daugiažodiškesnis ir sudėtingesnis turtingoms sąveikoms |
| **Failų įkėlimo testavimas**      | Išmanesnė API failų įkėlimui                  | Daugiažodiškesnė, mažiau intuityvi API    |
| **CI/CD integracija**             | Lengva integracija su GitHub Actions, Jenkins | Tvirta integracija su daugeliu CI įrankių |
| **Mobilusis testavimas**          | Ribotas, tik emuliacija                       | Visas palaikymas per Appium               |
| **Palaikymas keliose naršyklėse** | Chromium, WebKit, Firefox                     | Visas palaikymas pagrindinėse ir paveldėtose naršyklėse |
| **Našumas**                       | Greitas, optimizuotas testavimui be grafinės sąsajos | Lėtesnis, ypač be grafinės sąsajos (headless) režimu |
| **Testavimas keliuose monitoriuose** | Ribotas                                    | Geras kelių monitorių sąrankų palaikymas  |
| **Bendruomenė ir ekosistema**     | Auganti, gera dokumentacija                   | Didelė, brandi, plati ekosistema          |

### 7. **Sprendimas**

Apsvarsčius reikalavimus ir kompromisus, **Playwright** yra geresnis pasirinkimas mūsų dabartiniams poreikiams. Jo išmanesnė API vietinių failų įkėlimo testavimui, glausta sintaksė ir tvirtas interaktyvios sąsajos testavimo palaikymas daro jį idealiai tinkamą mūsų lanksčiojo kūrimo ciklui. Tai, kad jis palaiko ir **TypeScript**, ir **Python**, mūsų komandai yra labai svarbu, o šiuolaikinis karkaso požiūris į testavimą leis mums rašyti švarų, prižiūrimą kodą.

Nors **Selenium** išlieka puikiu įrankiu, ypač mobiliajam testavimui, paveldėtų naršyklių palaikymui ir kelių monitorių sąrankoms, jis mažiau tinka mūsų dabartiniams poreikiams. Dėl savo daugiažodiškumo, lėtesnio našumo ir sudėtingesnio dinaminių sąsajų, tokių kaip diagramos, tvarkymo jis yra mažiau optimalus mūsų naudojimo atvejui.

### 8. **Pasekmės**

- **Neatidėliotini veiksmai**: savo E2E testavimui priimsime **Playwright**, sutelkdami dėmesį į naudotojų eigų, apimančių registraciją, prisijungimą, failų įkėlimą, skydelius ir ataskaitų atsisiuntimą, testavimą.
- **Ilgalaikiai svarstymai**: stebėsime besivystančią Playwright ekosistemą. Jei mūsų poreikiai pasikeistų, ypač dėl mobiliojo testavimo ar paveldėtų naršyklių palaikymo, galime iš naujo svarstyti Selenium.
- **Mokymai ir dokumentacija**: kūrimo komandoms reikės susipažinti su Playwright API, ypač dėl dinaminių sąsajų ir failų įkėlimo tvarkymo.
- **Migracija**: esami Selenium testai (jei jų yra) bus palaipsniui perkelti į Playwright.

### 9. **Būsimi svarstymai**
