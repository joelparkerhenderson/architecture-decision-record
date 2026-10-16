## Zapis arhitekturne odločitve: ogrodje za avtomatizacijo brskalnika za testiranje E2E (Playwright ali Selenium)

### 1. **Kontekst**

Izbiramo ogrodje za avtomatizacijo brskalnika za naš cevovod za celostno (end-to-end, E2E) testiranje. To ogrodje bo sestavni del naših procesov CI/CD in bo izvajalo teste, ki simulirajo resnične interakcije uporabnikov na naši platformi. Testi bodo zajemali zlasti scenarije, kot so registracija/prijava uporabnika, nalaganje datotek, interakcije z nadzorno ploščo in prenosi poročil.

Kot **zagonsko podjetje** se osredotočamo na **agilen razvoj** s potrebo po hitri iteraciji in razvoju. Naša ekipa večinoma dela s **TypeScriptom** in **Pythonom**, zato je bistvena možnost pisanja testov v teh jezikih. Poleg tega platforma vsebuje **interaktivne grafikone in nadzorne plošče**, zato je ključno, da orodje za avtomatizacijo dobro podpira bogate, dinamične uporabniške vmesnike.

Dva kandidata za to nalogo sta **Playwright** in **Selenium**, vsak s svojimi prednostmi in kompromisi. Ogrodji moramo ovrednotiti na podlagi spodaj navedenih funkcij in zahtev.

### 2. **Preučene možnosti**

- **Playwright** (Microsoft)
- **Selenium** (projekt Selenium)

### 3. **Gonilniki odločitve**

Dejavniki, ki vplivajo na našo odločitev, so naslednji:

1. **Agilen razvoj**: Izbrano orodje mora omogočati hitre, prilagodljive razvojne cikle.
2. **Podpora jezikom**: Naša ekipa zahteva podporo za **TypeScript** in **Python**.
3. **Testiranje interaktivnega uporabniškega vmesnika**: Bistvena je zmožnost zanesljivega testiranja interaktivnih grafikonov, nadzornih plošč in dinamičnih elementov.
4. **Hitrost izvajanja**: Čeprav ni primarna skrb, je zmogljivost v cevovodih CI/CD premislek.
5. **Razširljivost**: V neposredni prihodnosti ne načrtujemo množičnega skaliranja, vendar želimo zagotoviti, da rešitev zmore prihodnjo rast.
6. **Združljivost za nazaj**: Podedovani sistemi in združljivost s starejšimi brskalniki za naš projekt trenutno niso kritični.
7. **Testiranje mobilnih naprav**: Čeprav ni takojšnji fokus, bi moralo biti ogrodje zmožno testirati mobilno odzivne funkcije ali pa razširljivo za takšne primere uporabe.
8. **Testiranje z več monitorji**: Podpora za konfiguracije z več monitorji je sekundarna zahteva, zlasti če bomo kdaj skalirali na testiranje bolj zapletenih uporabniških potekov dela.
9. **Testiranje nalaganja datotek**: Ogrodje mora učinkovito obravnavati nalaganje datotek, ki je osrednja zahteva naših potreb po testiranju.

### 4. **Merila vrednotenja**

- **Enostavnost uporabe**: Kako enostavno je pisati in vzdrževati teste?
- **Podpora jezikom**: Ali ogrodje podpira TypeScript in Python, jezika, ki ju naša ekipa uporablja najpogosteje?
- **Testiranje interaktivnega uporabniškega vmesnika**: Kako dobro ogrodje obravnava zapletene, interaktivne uporabniške vmesnike, kot so grafikoni, nalaganje datotek in dinamični podatki?
- **Integracija CI/CD**: Kako dobro se ogrodje integrira v običajna orodja in storitve CI/CD?
- **Podpora več brskalnikom**: Kateri brskalniki so podprti in kako dobro delujejo?
- **Zmogljivost in hitrost**: Kako hitro se izvajajo testi, zlasti v cevovodu CI/CD?
- **Razširljivost**: Kako dobro se ogrodje lahko skalira, če se dodajo novi testi ali zapletenejši scenariji?
- **Skupnost in ekosistem**: Kako dejavna je skupnost ogrodja? Ali je na voljo veliko integracij in razširitev?

### 5. **Premisleki**

#### 5.1 **Playwright**

##### **Prednosti**:
1. **Pametnejši API za nalaganje lokalnih datotek**: API Playwrighta za interakcijo z lokalnimi datotekami in nalaganje datotek je preprostejši in intuitivnejši. To bi olajšalo izvedbo in vzdrževanje testiranja nalaganja datotek.
2. **Sintaksa in generiranje kode**: Playwright ima krajšo, jedrnatejšo sintakso. To pomeni manj ponavljajoče se kode, kar izboljša vzdržljivost in učinkovitost razvijalcev. Poleg tega krajša sintaksa izboljša kakovost generiranja kode z OpenAI, kar olajša samodejno generiranje testnih skriptov.
3. **Testiranje interaktivnega uporabniškega vmesnika**: Playwright je odličen pri testiranju dinamičnih, interaktivnih spletnih aplikacij, kot so tiste z bogatimi grafikoni, zapletenimi interakcijami uporabnikov in posodobitvami v realnem času. Zelo učinkovito obravnava WebSockets, WebRTC, senčne DOM-e (shadow DOM) in druge sodobne spletne tehnologije.
4. **Podpora več brskalnikom**: Playwright podpira **Chromium**, **WebKit** in **Firefox**. Ima dosledno zmogljivost v teh brskalnikih, kar bi moralo pokriti večino naših potreb po testiranju.
5. **Integracija CI/CD**: Playwright se brezhibno integrira s sodobnimi platformami CI/CD (GitHub Actions, Jenkins itd.). Teste lahko izvaja vzporedno v različnih brskalnikih, kar optimizira čase izvajanja testov in ga naredi primernega za hiter razvoj.
6. **Hiter in zanesljiv**: Playwright je na splošno hitrejši od Seleniuma, zlasti v načinu brez glave (headless), in odpornejši pri delu z asinhronimi spletnimi elementi.

##### **Slabosti**:
1. **Omejeno testiranje mobilnih naprav**: Čeprav Playwright podpira mobilno emulacijo za brskalnike, nima izvornih zmožnosti testiranja mobilnih naprav, kot je integracija Seleniuma z Appium za pravo testiranje mobilnih naprav.
2. **Manjši ekosistem**: Playwright je še vedno novejši in manj uveljavljen kot Selenium. Čeprav ima hitro rastočo skupnost in dobro dokumentacijo, morda še nima obsežnega ekosistema vtičnikov in integracij, ki jih ponuja Selenium.
3. **Omejena podpora brskalnikom**: Čeprav Playwright pokriva glavne sodobne brskalnike (Chrome, Safari, Firefox), njegova podpora za starejše brskalnike (npr. Internet Explorer) ni tako robustna kot pri Seleniumu.

#### 5.2 **Selenium**

##### **Prednosti**:
1. **Daljša zgodovina in zrelost**: Selenium obstaja že dolgo in ima dokazano zgodovino. Široko se uporablja v številnih ekipah in panogah, kar je privedlo do obsežnega ekosistema vtičnikov, integracij in virov.
2. **Podpora več brskalnikom in platformam**: Selenium podpira **široko paleto brskalnikov** in različic, vključno z **Internet Explorerjem**, ter ga je mogoče integrirati tudi z različnimi orodji, kot so **Docker**, **Selenium Grid** in **oblačne storitve** za porazdeljeno testiranje.
3. **Testiranje mobilnih naprav**: Selenium je prek integracije z **Appium** veliko robustnejši za testiranje mobilnih naprav, vključno z aplikacijami za Android in iOS. To ga naredi boljšo izbiro za projekte z mobilnim poudarkom (mobile-first) ali velikim deležem mobilnega.
4. **Testiranje z več monitorji**: Selenium zagotavlja boljšo podporo za scenarije z **več monitorji** ali zapletenimi interakcijami z več okni.

##### **Slabosti**:
1. **Kompleksnost**: API Seleniuma je bolj dolgovezen in izrecen. Čeprav je to v nekaterih primerih lahko prednost, pomeni več kode za pisanje in vzdrževanje, kar lahko zmanjša agilnost razvijalcev – kar je še posebej pomembno v zagonskem okolju.
2. **Zmogljivost**: Selenium na splošno deluje počasneje kot Playwright, zlasti v načinu brez glave. To bi lahko vplivalo na cevovode CI/CD, zlasti ko se število testov povečuje.
3. **Testiranje interaktivnega uporabniškega vmesnika**: Selenium ni tako gladek kot Playwright pri testiranju sodobnih, interaktivnih spletnih uporabniških vmesnikov, zlasti z grafikoni in podatki v realnem času. Za zanesljivo interakcijo z dinamično vsebino zahteva več nastavitev in obravnave.

### 6. **Povzetek primerjave**

| Funkcija                          | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Enostavnost uporabe**           | Krajša sintaksa, intuitivnejši za sodobne uporabniške vmesnike | Bolj izrecen, zahteva več ponavljajoče se kode |
| **Podpora jezikom**               | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Testiranje interaktivnega uporabniškega vmesnika** | Odlično za dinamične uporabniške vmesnike v realnem času | Obravnava osnovne uporabniške vmesnike, a bolj dolgovezno in zapleteno pri bogatih interakcijah |
| **Testiranje nalaganja datotek**  | Pametnejši API za nalaganje datotek           | Bolj dolgovezen, manj intuitiven API         |
| **Integracija CI/CD**             | Enostavna integracija z GitHub Actions, Jenkins | Močna integracija z mnogimi orodji CI    |
| **Testiranje mobilnih naprav**    | Omejeno, samo emulacija                       | Polna podpora prek Appium                 |
| **Podpora več brskalnikom**       | Chromium, WebKit, Firefox                     | Polna podpora v glavnih in starejših brskalnikih |
| **Zmogljivost**                   | Hiter, optimiziran za testiranje brez glave   | Počasnejši, zlasti v načinu brez glave    |
| **Testiranje z več monitorji**    | Omejeno                                       | Dobra podpora za nastavitve z več monitorji |
| **Skupnost in ekosistem**         | Rastoča, dobra dokumentacija                  | Velik, zrel, obsežen ekosistem           |

### 7. **Odločitev**

Po preučitvi zahtev in kompromisov je **Playwright** boljša izbira za naše trenutne potrebe. Njegov pametnejši API za testiranje nalaganja lokalnih datotek, jedrnata sintaksa in močna podpora za testiranje interaktivnega uporabniškega vmesnika ga delajo idealnega za naš agilni razvojni cikel. Dejstvo, da podpira **TypeScript** in **Python**, je za našo ekipo ključno, sodoben pristop ogrodja k testiranju pa nam bo omogočil pisanje čiste, vzdržljive kode.

Čeprav **Selenium** ostaja odlično orodje, zlasti za testiranje mobilnih naprav, podporo starejšim brskalnikom in nastavitve z več monitorji, je manj primeren za naše trenutne potrebe. Njegova dolgovezenost, počasnejša zmogljivost in zahtevnejša obravnava dinamičnih uporabniških vmesnikov, kot so grafikoni, ga delajo manj optimalnega za naš primer uporabe.

### 8. **Posledice**

- **Takojšnji ukrep**: Za testiranje E2E bomo uvedli **Playwright**, s poudarkom na testiranju uporabniških tokov, ki vključujejo registracijo, prijavo, nalaganje datotek, nadzorne plošče in prenose poročil.
- **Dolgoročni premisleki**: Spremljali bomo razvoj ekosistema Playwright. Če se bodo naše potrebe spremenile, zlasti glede testiranja mobilnih naprav ali podpore starejšim brskalnikom, bomo morda ponovno preučili Selenium.
- **Usposabljanje in dokumentacija**: Razvojne ekipe se bodo morale seznaniti z API Playwrighta, zlasti za obravnavo dinamičnih uporabniških vmesnikov in nalaganja datotek.
- **Selitev**: Obstoječi testi Selenium (če obstajajo) bodo postopoma preseljeni v Playwright.

### 9. **Prihodnji premisleki**
