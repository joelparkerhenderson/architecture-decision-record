## Arkitekturbeslutningspost: framework til browserautomatisering ved E2E-test (Playwright eller Selenium)

### 1. **Kontekst**

Vi er i gang med at vælge et framework til browserautomatisering til vores pipeline for end-to-end (E2E)-test. Dette framework vil være en integreret del af vores CI/CD-processer og køre tests, der simulerer reelle brugerinteraktioner på vores platform. Testene vil især dække scenarier som brugeroprettelse/login, filuploads, dashboardinteraktioner og download af rapporter.

Som **startup** er vores fokus på **agil udvikling**, med behov for hurtigt at iterere og udvikle os. Vores team arbejder hovedsageligt med **TypeScript** og **Python**, og evnen til at skrive tests i disse sprog er afgørende. Derudover indeholder platformen **interaktive diagrammer og dashboards**, hvilket gør det kritisk, at automatiseringsværktøjet understøtter rige, dynamiske UI'er godt.

De to kandidater til denne opgave er **Playwright** og **Selenium**, hver med sine styrker og afvejninger. Vi skal evaluere disse frameworks ud fra de funktioner og krav, der er beskrevet nedenfor.

### 2. **Overvejede muligheder**

- **Playwright** (fra Microsoft)
- **Selenium** (fra Selenium Project)

### 3. **Beslutningsdrivkræfter**

De faktorer, der påvirker vores beslutning, er følgende:

1. **Agil udvikling**: det valgte værktøj skal muliggøre hurtige, fleksible udviklingscyklusser.
2. **Sprogunderstøttelse**: vores team kræver understøttelse af både **TypeScript** og **Python**.
3. **Test af interaktive UI'er**: evnen til pålideligt at teste interaktive diagrammer, dashboards og dynamiske elementer er afgørende.
4. **Kørselshastighed**: selv om det ikke er en primær bekymring, er ydeevne i CI/CD-pipelines en overvejelse.
5. **Skalerbarhed**: vi planlægger ikke massiv skalering i den nærmeste fremtid, men vi vil sikre, at løsningen kan håndtere fremtidig vækst.
6. **Bagudkompatibilitet**: ældre systemer og kompatibilitet med ældre browsere er ikke kritiske for vores projekt lige nu.
7. **Mobiltest**: selv om det ikke er et umiddelbart fokus, bør frameworket kunne teste mobilresponsive funktioner eller kunne udvides til sådanne anvendelsestilfælde.
8. **Test med flere skærme**: understøttelse af opsætninger med flere skærme er et sekundært krav, især hvis vi senere skalerer op til at teste mere komplekse brugerarbejdsgange.
9. **Test af filupload**: frameworket skal effektivt kunne håndtere filuploads, et kernekrav i vores testbehov.

### 4. **Evalueringskriterier**

- **Brugervenlighed**: hvor nemt er det at skrive og vedligeholde tests?
- **Sprogunderstøttelse**: understøtter frameworket TypeScript og Python, de to sprog, vores team bruger mest?
- **Test af interaktive UI'er**: hvor godt håndterer frameworket komplekse, interaktive brugergrænseflader som diagrammer, filuploads og dynamiske data?
- **CI/CD-integration**: hvor godt integrerer frameworket med almindelige CI/CD-værktøjer og -tjenester?
- **Understøttelse af flere browsere**: hvilke browsere understøttes, og hvor godt fungerer de?
- **Ydeevne og hastighed**: hvor hurtigt kører testene, især i en CI/CD-pipeline?
- **Skalerbarhed**: hvor godt kan frameworket skalere, hvis der tilføjes flere tests eller mere komplekse scenarier?
- **Fællesskab og økosystem**: hvor aktivt er frameworkets fællesskab? Er der rigeligt med integrationer og plugins?

### 5. **Overvejelser**

#### 5.1 **Playwright**

##### **Fordele**:
1. **Smartere API til upload af lokale filer**: Playwrights API til interaktion med lokale filer og udførelse af filuploads er enklere og mere intuitivt. Det gør test af filupload lettere at implementere og vedligeholde.
2. **Syntaks og kodegenerering**: Playwright har en kortere, mere koncis syntaks. Det giver mindre boilerplate, hvilket forbedrer vedligeholdeligheden og udviklernes effektivitet. Desuden forbedrer den kortere syntaks kvaliteten af OpenAI's kodegenerering, hvilket gør det lettere automatisk at generere testscripts.
3. **Test af interaktive UI'er**: Playwright udmærker sig ved at teste dynamiske, interaktive webapplikationer, f.eks. dem med rige diagrammer, komplekse brugerinteraktioner og realtidsopdateringer. Det håndterer WebSockets, WebRTC, shadow DOM og andre moderne webteknologier meget effektivt.
4. **Understøttelse af flere browsere**: Playwright understøtter **Chromium**, **WebKit** og **Firefox**. Det har ensartet ydeevne på tværs af disse browsere, hvilket bør dække de fleste af vores testbehov.
5. **CI/CD-integration**: Playwright integrerer problemfrit med moderne CI/CD-platforme (GitHub Actions, Jenkins osv.). Det kan køre tests parallelt på tværs af forskellige browsere, hvilket optimerer testkørselstiderne og gør det egnet til hurtig udvikling.
6. **Hurtigt og pålideligt**: Playwright er generelt hurtigere end Selenium, især i headless-tilstand, og mere robust over for asynkrone webelementer.

##### **Ulemper**:
1. **Begrænset mobiltest**: selv om Playwright understøtter mobilemulering for browsere, mangler det indbyggede mobiltestfunktioner som Seleniums integration med Appium til ægte mobiltest.
2. **Mindre økosystem**: Playwright er stadig nyere og mindre etableret end Selenium. Selv om det har et hurtigt voksende fællesskab og god dokumentation, har det måske endnu ikke det store økosystem af plugins og integrationer, som Selenium tilbyder.
3. **Begrænset browserunderstøttelse**: selv om Playwright dækker de store moderne browsere (Chrome, Safari, Firefox), er understøttelsen af ældre browsere (f.eks. Internet Explorer) ikke så robust som Seleniums.

#### 5.2 **Selenium**

##### **Fordele**:
1. **Længere historik og modenhed**: Selenium har eksisteret længe og har en dokumenteret meritliste. Det bruges bredt af mange teams og brancher, hvilket har ført til et stort økosystem af plugins, integrationer og ressourcer.
2. **Understøttelse af flere browsere og platforme**: Selenium understøtter et **bredt udvalg af browsere** og versioner, herunder **Internet Explorer**, og kan også integreres med forskellige værktøjer som **Docker**, **Selenium Grid** og **cloudtjenester** til distribueret test.
3. **Mobiltest**: Selenium er, gennem sin integration med **Appium**, meget mere robust til mobiltest, herunder både Android- og iOS-applikationer. Det gør det til det bedre valg til projekter med mobile-first eller tungt mobilt fokus.
4. **Test med flere skærme**: Selenium giver bedre understøttelse af scenarier med **flere skærme** eller komplekse interaktioner med flere vinduer.

##### **Ulemper**:
1. **Kompleksitet**: Seleniums API er mere ordrigt og eksplicit. Selv om det i nogle tilfælde kan være en fordel, betyder det mere kode at skrive og vedligeholde, hvilket kan reducere udvikleres smidighed – især vigtigt i et startupmiljø.
2. **Ydeevne**: Selenium kører generelt langsommere end Playwright, især i headless-tilstand. Det kan påvirke CI/CD-pipelines, især når antallet af tests vokser.
3. **Test af interaktive UI'er**: Selenium er ikke så smidigt som Playwright, når det gælder test af moderne, interaktive web-UI'er, især med diagrammer og realtidsdataopdateringer. Det kræver mere konfiguration og håndtering for pålideligt at interagere med dynamisk indhold.

### 6. **Sammenligningsoversigt**

| Funktion                          | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Brugervenlighed**               | Kortere syntaks, mere intuitivt til moderne UI'er | Mere eksplicit, kræver mere boilerplate |
| **Sprogunderstøttelse**           | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Test af interaktive UI'er**     | Fremragende til dynamiske realtids-UI'er      | Håndterer grundlæggende UI'er, men mere ordrigt og komplekst til rige interaktioner |
| **Test af filupload**             | Smartere API til filuploads                   | Mere ordrigt, mindre intuitivt API        |
| **CI/CD-integration**             | Nem integration med GitHub Actions, Jenkins   | Stærk integration med mange CI-værktøjer  |
| **Mobiltest**                     | Begrænset, kun emulering                      | Fuld understøttelse via Appium            |
| **Understøttelse af flere browsere** | Chromium, WebKit, Firefox                  | Fuld understøttelse af store og ældre browsere |
| **Ydeevne**                       | Hurtigt, optimeret til headless-test          | Langsommere, især i headless-tilstand     |
| **Test med flere skærme**         | Begrænset                                     | God understøttelse af opsætninger med flere skærme |
| **Fællesskab og økosystem**       | Voksende, god dokumentation                   | Stort, modent, omfattende økosystem       |

### 7. **Beslutning**

Efter at have overvejet kravene og afvejningerne er **Playwright** det bedre valg til vores nuværende behov. Dets smartere API til test af upload af lokale filer, koncise syntaks og stærke understøttelse af test af interaktive UI'er gør det til et ideelt match til vores agile udviklingscyklus. Det faktum, at det understøtter både **TypeScript** og **Python**, er afgørende for vores team, og frameworkets moderne tilgang til test gør, at vi kan skrive ren, vedligeholdelig kode.

Selv om **Selenium** forbliver et fremragende værktøj, især til mobiltest, understøttelse af ældre browsere og opsætninger med flere skærme, er det mindre egnet til vores nuværende behov. Dets ordrighed, langsommere ydeevne og mere komplekse håndtering af dynamiske UI'er som diagrammer gør det mindre optimalt til vores anvendelsestilfælde.

### 8. **Konsekvenser**

- **Umiddelbar handling**: vi indfører **Playwright** til vores E2E-test med fokus på at teste brugerflows, der involverer oprettelse, login, filuploads, dashboards og download af rapporter.
- **Langsigtede overvejelser**: vi holder øje med Playwrights udviklende økosystem. Hvis vores behov ændrer sig, især omkring mobiltest eller understøttelse af ældre browsere, kan vi genoverveje Selenium.
- **Uddannelse og dokumentation**: udviklingsteamene skal blive fortrolige med Playwrights API, især til håndtering af dynamiske UI'er og filuploads.
- **Migrering**: eksisterende Selenium-tests (hvis nogen) migreres gradvist til Playwright.

### 9. **Fremtidige overvejelser**
