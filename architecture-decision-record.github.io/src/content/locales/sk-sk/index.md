# Záznam architektonického rozhodnutia (ADR)

Záznam architektonického rozhodnutia (ADR) je dokument, ktorý zachytáva dôležité architektonické rozhodnutie spolu s jeho kontextom a dôsledkami.

> [!IMPORTANT]
> Pred použitím týchto zdrojov v akýchkoľvek kritických systémoch vykonajte vlastnú náležitú kontrolu.

Obsah:

- [Čo je záznam architektonického rozhodnutia?](#čo-je-záznam-architektonického-rozhodnutia)
- [Ako začať používať ADR](#ako-začať-používať-adr)
- [Ako začať používať ADR s nástrojmi](#ako-začať-používať-adr-s-nástrojmi)
- [Ako začať používať ADR s gitom](#ako-začať-používať-adr-s-gitom)
- [Zručnosti Claude Code pre ADR](#zručnosti-claude-code-pre-adr)
- [Konvencie pomenovania súborov ADR](#konvencie-pomenovania-súborov-adr)
- [Tipy na písanie dobrých ADR](#tipy-na-písanie-dobrých-adr)
- [Príklady šablón ADR](#príklady-šablón-adr)
- [Rady k tímovej práci pre ADR](#rady-k-tímovej-práci-pre-adr)
- [Otázky k tímovej práci pre ADR](#otázky-k-tímovej-práci-pre-adr)
- [Koncepty ďalšieho kroku pre ADR](#koncepty-ďalšieho-kroku-pre-adr)
- [Architektonické diagramy, pohľady a hľadiská](#architektonické-diagramy-pohľady-a-hľadiská)
- [Fitness funkcie pre rozhodnutia ako kód](#fitness-funkcie-pre-rozhodnutia-ako-kód)
- [Ochranné pravidlá rozhodnutí pre pull requesty](#ochranné-pravidlá-rozhodnutí-pre-pull-requesty)
- [Ďalšie informácie](#ďalšie-informácie)

Šablóny:

- [Šablóna záznamu rozhodnutia od Jeffa Tyreeho a Arta Akermana](sablony/sablona-zaznamu-rozhodnutia-jeff-tyree-a-art-akerman/)
- [Šablóna záznamu rozhodnutia od Michaela Nygarda](sablony/sablona-zaznamu-rozhodnutia-michael-nygard/)
- [Šablóna záznamu rozhodnutia od EdgeX](sablony/sablona-zaznamu-rozhodnutia-edgex/)
- [Šablóna záznamu rozhodnutia od arc42](sablony/sablona-zaznamu-rozhodnutia-arc42/)
- [Šablóna záznamu rozhodnutia pre alexandrijský vzor](sablony/sablona-zaznamu-rozhodnutia-alexandrijsky-vzor/)
- [Šablóna záznamu rozhodnutia pre obchodný prípad](sablony/sablona-zaznamu-rozhodnutia-obchodny-pripad/)
- [Šablóna záznamu rozhodnutia projektu MADR](sablony/sablona-zaznamu-rozhodnutia-projekt-madr/)
- [Šablóna záznamu rozhodnutia s Planguage](sablony/sablona-zaznamu-rozhodnutia-s-planguage/)
- [Šablóna záznamu rozhodnutia od Paula Mersona](https://github.com/pmerson/ADR-template)
- [Šablóna záznamu rozhodnutia od Olafa Zimmermanna](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Šablóna záznamu rozhodnutia od Garetha Morgana](sablony/sablona-zaznamu-rozhodnutia-gareth-morgan/)
- [Šablóna záznamu rozhodnutia od GIG Cymru NHS Wales](sablony/sablona-zaznamu-rozhodnutia-gig-cymru-nhs-wales/)
- [Šablóna záznamu rozhodnutia pre dôležité technické rozhodnutia (ITD) od Ignacia Larrañagu](sablony/sablona-zaznamu-rozhodnutia-dolezite-technicke-rozhodnutia/)

Príklady:

- [CSS framework](priklady/framework-css/)
- [Konfigurácia premenných prostredia](priklady/konfiguracia-premennych-prostredia/)
- [Metriky, monitory, upozornenia](priklady/metriky-monitory-upozornenia/)
- [Microsoft Azure DevOps](priklady/microsoft-azure-devops/)
- [Monorepo alebo multirepo](priklady/monorepo-alebo-multirepo/)
- [Programovacie jazyky](priklady/programovacie-jazyky/)
- [Ukladanie tajomstiev](priklady/ukladanie-tajomstiev/)
- [Formát časovej pečiatky](priklady/format-casovej-peciatky/)
- [A mnoho ďalších...](priklady/)

## Čo je záznam architektonického rozhodnutia?

**Záznam architektonického rozhodnutia** (ADR) je dokument, ktorý zachytáva dôležité architektonické rozhodnutie spolu s jeho kontextom a dôsledkami.

**Architektonické rozhodnutie** (AD) je voľba pri návrhu softvéru, ktorá rieši významnú požiadavku.

**Denník architektonických rozhodnutí** (ADL) je súbor všetkých ADR vytvorených a udržiavaných pre konkrétny projekt (alebo organizáciu).

**Architektonicky významná požiadavka** (ASR) je požiadavka, ktorá má merateľný vplyv na architektúru softvérového systému.

To všetko patrí do témy **správy architektonických znalostí** (AKM).

Cieľom tohto dokumentu je poskytnúť rýchly prehľad o ADR, o tom, ako ich vytvárať, a kde hľadať ďalšie informácie.

Skratky:

  * **AD**: architektonické rozhodnutie

  * **ADL**: denník architektonických rozhodnutí

  * **ADR**: záznam architektonického rozhodnutia

  * **AKM**: správa architektonických znalostí

  * **ASR**: architektonicky významná požiadavka

## Ako začať používať ADR

Ak chcete začať používať ADR, porozprávajte sa so spolupracovníkmi o týchto oblastiach.

Identifikácia rozhodnutí:

  * Ako naliehavé a ako dôležité je AD?

  * Musí sa urobiť teraz, alebo môže počkať, kým sa nezistí viac?

  * Pri identifikácii rozhodnutí môžu pomôcť osobné aj kolektívne skúsenosti, ako aj uznávané metódy a postupy návrhu.

  * V ideálnom prípade udržiavajte zoznam rozhodnutí, ktoré treba urobiť, ktorý dopĺňa zoznam úloh produktu.

Rozhodovanie:

  * Existuje množstvo techník rozhodovania, všeobecných aj špecifických pre softvérovú architektúru, napríklad mapovanie dialógu.

  * Skupinové rozhodovanie je aktívnou výskumnou témou.

Presadzovanie a vynucovanie rozhodnutí:

  * AD sa používajú pri návrhu softvéru; preto musia byť komunikované zainteresovaným stranám systému, ktoré ho financujú, vyvíjajú a prevádzkujú, a tými prijaté.

  * Architektonicky zjavné štýly kódovania a revízie kódu zamerané na architektonické záležitosti a rozhodnutia sú dve súvisiace praktiky.

  * AD je tiež potrebné (znovu) zvážiť pri modernizácii softvérového systému v rámci softvérovej evolúcie.

Zdieľanie rozhodnutí (voliteľné):

  * Mnohé AD sa opakujú naprieč projektmi.

  * Skúsenosti s minulými rozhodnutiami, dobré aj zlé, preto môžu byť cenným opakovane použiteľným aktívom pri uplatňovaní explicitnej stratégie správy znalostí.

Dokumentovanie rozhodnutí:

  * Existuje mnoho šablón a nástrojov na zachytávanie rozhodnutí.

  * Pozrite si agilné komunity, napr. ADR od M. Nygarda.

  * Pozrite si tradičné procesy softvérového inžinierstva a architektonického návrhu, napr. tabuľkové rozloženia navrhnuté IBM UMF a Tyreem a Akermanom z CapitalOne.

Viac informácií:

  * Vyššie uvedené kroky sú prevzaté z hesla na Wikipédii o [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Ako začať používať ADR s nástrojmi

- [MySpec](https://myspec.dev) — Platforma na automatizované špecifikácie a architektonické rozhodnutia, ktorá štruktúruje ústavu projektu, technickú architektúru a ADR do čistého Markdownu sprístupneného cez MCP.

ADR môžete začať používať s nástrojmi akýmkoľvek spôsobom, aký chcete.

Napríklad:

  * Ak radi používate Google Drive a online úpravy, môžete vytvoriť Google Doc alebo Google Sheet.

  * Ak radi používate verzovanie zdrojového kódu, napríklad git, môžete pre každý ADR vytvoriť súbor.

  * Ak radi používate nástroje na plánovanie projektov, napríklad Atlassian Jira, môžete použiť sledovač plánovania nástroja.

  * Ak radi používate wiki, napríklad MediaWiki, môžete vytvoriť wiki pre ADR.

## Ako začať používať ADR s gitom

Ak radi používate verzovanie git, takto radi začíname používať ADR s gitom pri typickom softvérovom projekte so zdrojovým kódom.

Vytvorte adresár pre súbory ADR:

```sh
$ mkdir adr
```

Pre každý ADR vytvorte textový súbor, napríklad `choose-database.md`:

```sh
$ vi choose-database.md
```

Do ADR napíšte čokoľvek chcete. Nápady nájdete v šablónach v tomto úložisku.

Commitnite ADR do svojho git úložiska.

## Zručnosti Claude Code pre ADR

Toto úložisko obsahuje dve zručnosti (skills) pre [Claude Code](https://claude.com/claude-code) v adresári [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), aby AI programovací agent mohol písať a udržiavať ADR spôsobom, ktorý tento projekt odporúča:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — všeobecného určenia, pre každého, kto píše ADR v ľubovoľnom projekte. Pomáha rozhodnúť, či rozhodnutie potrebuje ADR, vytvorí adresár `adr/` alebo `decisions/`, pomenuje súbor, vyberie šablónu z jedenástich priložených návrhov a napíše pevné sekcie Kontext/Rozhodnutie/Dôsledky.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — osobitne pre správcov tohto úložiska. Dokumentuje usporiadanie úložiska, konvenciu zrkadlenia README/locales a presné kroky na pridanie novej šablóny, príkladu alebo odkazu na nástroj.

Ak chcete zručnosť použiť, skopírujte jej priečinok do `.claude/skills/` v koreni úložiska, v ktorom pracujete (alebo do `~/.claude/skills/`, aby bola dostupná vo všetkých projektoch), a potom požiadajte Claude Code, aby napísal alebo skontroloval ADR.

## Konvencie pomenovania súborov ADR

Ak sa rozhodnete vytvárať svoje ADR pomocou typických textových súborov, možno si budete chcieť vymyslieť vlastnú konvenciu pomenovania súborov ADR.

Uprednostňujeme konvenciu pomenovania súborov so špecifickým formátom.

Príklady:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Naša konvencia pomenovania súborov:

  * Názov obsahuje slovesnú frázu v rozkazovacom spôsobe v prítomnom čase. To pomáha čitateľnosti a zodpovedá to nášmu formátu správ commitov.

  * Názov používa malé písmená a pomlčky (rovnako ako toto úložisko). Je to rovnováha medzi čitateľnosťou a použiteľnosťou systému.

  * Prípona je markdown. To môže byť užitočné pre jednoduché formátovanie.

## Tipy na písanie dobrých ADR

Charakteristiky dobrého ADR:

* Zdôvodnenie: Vysvetlite dôvody konkrétneho AD. To môže zahŕňať kontext (pozri nižšie), výhody a nevýhody rôznych možných volieb, porovnania funkcií, diskusie o nákladoch a prínosoch a ďalšie.

* Konkrétnosť: Každý ADR by mal byť o jednom AD, nie o viacerých AD.

* Časové pečiatky: Uveďte, kedy bola každá položka v ADR napísaná. To je obzvlášť dôležité pre aspekty, ktoré sa môžu v čase meniť, ako sú náklady, harmonogramy, škálovanie a podobne.

* Nemennosť: Neupravujte existujúce informácie v ADR. Namiesto toho ADR doplňte pridaním nových informácií alebo ADR nahraďte vytvorením nového ADR.

Charakteristiky dobrej sekcie „Kontext“ v ADR:

* Vysvetlite situáciu vašej organizácie a obchodné priority.

* Zahrňte zdôvodnenie a úvahy založené na sociálnom a zručnostnom zložení vašich tímov.

* Zahrňte relevantné výhody a nevýhody a opíšte ich výrazmi, ktoré zodpovedajú vašim potrebám a cieľom.

Charakteristiky dobrej sekcie „Dôsledky“ v ADR:

* Vysvetlite, čo vyplýva z prijatia rozhodnutia. To môže zahŕňať účinky, výsledky, výstupy, nadväzujúce kroky a ďalšie.

* Zahrňte informácie o všetkých následných ADR. Je pomerne bežné, že jeden ADR vyvolá potrebu ďalších ADR, napríklad keď jeden ADR urobí veľkú zastrešujúcu voľbu, ktorá zasa vytvorí potrebu viacerých menších rozhodnutí.

* Zahrňte všetky procesy revízie po akcii. Je typické, že tímy preskúmajú každý ADR o mesiac neskôr, aby porovnali informácie v ADR s tým, čo sa stalo v skutočnej praxi, aby sa učili a rástli.

Nový ADR môže nahradiť predchádzajúci ADR:

* Keď sa urobí AD, ktoré nahrádza alebo zneplatňuje predchádzajúci ADR, mal by sa vytvoriť nový ADR

## Príklady šablón ADR

Príklady šablón ADR zozbierané z internetu:

- [Šablóna ADR od Michaela Nygarda](sablony/sablona-zaznamu-rozhodnutia-michael-nygard/) (jednoduchá a populárna)

- [Šablóna ADR od Jeffa Tyreeho a Arta Akermana](sablony/sablona-zaznamu-rozhodnutia-jeff-tyree-a-art-akerman/) (prepracovanejšia)

- [Šablóna ADR pre alexandrijský vzor](sablony/sablona-zaznamu-rozhodnutia-alexandrijsky-vzor/) (jednoduchá, s podrobnosťami o kontexte)

- [Šablóna ADR pre obchodný prípad](sablony/sablona-zaznamu-rozhodnutia-obchodny-pripad/) (viac orientovaná na MBA, s nákladmi, SWOT a viacerými názormi)

- [Šablóna ADR projektu Markdown Any Decision Records (MADR)](sablony/sablona-zaznamu-rozhodnutia-projekt-madr/) (jednoduchá aj rozpracovaná verzia; tá druhá zdôrazňuje možnosti a ich výhody a nevýhody)

- [Šablóna ADR s Planguage](sablony/sablona-zaznamu-rozhodnutia-s-planguage/) (viac orientovaná na zabezpečenie kvality)

- [Šablóna pre dôležité technické rozhodnutia (ITD) od Ignacia Larrañagu](sablony/sablona-zaznamu-rozhodnutia-dolezite-technicke-rozhodnutia/) (štíhla a zameraná na rozhodnutie, optimalizovaná na rýchlu revíziu vedením)

## Rady k tímovej práci pre ADR

Ak uvažujete o používaní záznamov rozhodnutí vo svojom tíme, tu je niekoľko rád, ktoré sme sa naučili pri práci s mnohými tímami.

Máte príležitosť viesť svojich spolupracovníkov tým, že sa spolu budete rozprávať o tom „prečo“, namiesto nariaďovania toho „čo“. Napríklad záznamy rozhodnutí sú spôsob, ako môžu tímy múdrejšie rozmýšľať a lepšie komunikovať; záznamy rozhodnutí nemajú hodnotu, ak sú len dodatočne vynútenou papierovou požiadavkou.

Niektoré tímy oveľa viac uprednostňujú názov „rozhodnutia“ pred skratkou „ADR“. Keď niektoré tímy použijú názov adresára „decisions“, je to, ako keby sa rozsvietila žiarovka a tím začne do adresára dávať viac informácií, napríklad rozhodnutia o dodávateľoch, rozhodnutia o plánovaní, rozhodnutia o harmonogramoch atď. Všetky tieto druhy informácií môžu používať rovnakú šablónu. Predpokladáme, že sa ľudia učia rýchlejšie so slovami („rozhodnutia“) než so skratkami („ADR“), že ľudia sú motivovanejší písať dokumenty o rozpracovanej práci, keď sa slovo „záznam“ odstráni, a tiež že niektorým vývojárom a niektorým manažérom sa slovo „architektúra“ nepáči.

Teoreticky je nemennosť ideálna. V praxi sa našim tímom lepšie osvedčila meniteľnosť. Nové informácie vkladáme do existujúceho ADR s dátumovou pečiatkou a poznámkou, že informácie prišli po rozhodnutí. Tento druh prístupu vedie k „živému dokumentu“, ktorý môžeme všetci aktualizovať. Typické aktualizácie nastávajú, keď získame informácie vďaka novým spolupracovníkom, novým ponukám alebo skutočným výsledkom nášho používania, alebo po dodatočných zmenách tretích strán, ako sú schopnosti dodávateľov, cenové plány, licenčné zmluvy atď.

## Otázky k tímovej práci pre ADR

### Kto môže vytvoriť ADR?

Zvážte oblasti ako konkrétni ľudia, konkrétne roly, konkrétne tímy alebo konkrétne oddelenia; zvážte aj to, či existujú ľudia, roly, tímy alebo oddelenia, ktoré môžu ADR objednať, teda požiadať o ADR, ktorý napíše niekto iný. 

Príklad odpovede: Ktorákoľvek osoba v našej organizácii, ktorá si prečítala stránku README o zázname architektonického rozhodnutia, môže navrhnúť ADR, čo znamená, že ho môže začať písať a zdieľať s tímom.

### Čo odôvodňuje vznik ADR?

Zvážte oblasti ako spôsoby práce tímu vo vašej organizácii, štruktúra vášho softvérového systému, koordinácia medzi tímami, dlhodobá udržiavateľnosť, externé rozhrania, kto má mať prospech a podobne. 

Príklad odpovede: Chceme vytvoriť ADR, keď chceme, aby budúci vývojári pochopili „prečo“ toho, čo robíme.

### Čo odôvodňuje nevytvorenie ADR?

Zvážte oblasti ako rozhodnutia, ktoré nie sú o architektúre alebo sú drobné, napríklad s minimálnym rizikom, samostatné alebo pre jedného vývojára, alebo sú už úplne pokryté inde, napríklad štandardmi, politikami alebo dokumentáciou, alebo sú dočasné, napríklad obchádzky, dôkazy konceptu alebo experimenty. 

Príklad odpovede: Chceme preskočiť ADR, keď je rozhodnutie obmedzené rozsahom, časom, rizikom a nákladmi alebo je už pokryté inde.

### Aký je životný cyklus ADR?

Zvážte oblasti ako proces tvorby, proces výskumu, proces rozhodovania, proces implementácie a proces ukončenia. Zvážte, ako sledovať životný cyklus ADR v čase, napríklad ako presunúť ADR z jedného stavu do ďalšieho a tiež ako to komunikovať zainteresovaným stranám. 

Príklad odpovede: Chceme, aby mal ADR päť fáz životného cyklu: Iniciovanie → Skúmanie → Vyhodnocovanie → Implementácia → Udržiavanie → Ukončenie.

### Aké sú kritériá pre kroky životného cyklu ADR?

Zvážte oblasti ako akceptačné kritériá pre ADR, teda ako viete, že je dosť dobrý na to, aby postúpil z jedného kroku životného cyklu do ďalšieho? Je problém jasne sformulovaný? Boli zvážené alternatívy? Sú kompromisy dostatočne pochopené a zdokumentované?
Je k dispozícii všetok relevantný kontext? Sú zapojené všetky relevantné zainteresované strany? Bola zapracovaná všetka spätná väzba? 

Príklad odpovede: Chceme, aby o ADR hlasovali zainteresované strany, keď aktívny tím 1) dokončil svoj výskum, 2) dokončil svoje vyhodnotenie, 3) zverejnil návrh ADR zainteresovaným stranám s výzvou na pripomienky a lehotou jedného týždňa, 4) všetky pripomienky zainteresovaných strán boli zapracované a vyriešené.

### Aké roly a zodpovednosti interagujú s ADR?

Zvážte roly ako navrhovateľ, výskumník, hodnotiteľ, recenzent, schvaľovateľ, správca a podobne. Zvážte zodpovednosti ako komunikácia so zainteresovanými stranami, zabezpečenie splnenia očakávaní, zdieľanie na webovej lokalite alebo intranete a pravidelná revízia práce, najmä keď nastanú relevantné zmeny.

Príklad odpovede: Chceme, aby mal každý ADR vždy primárnu kontaktnú osobu, sekundárnu kontaktnú osobu a zodpovedný tím; tí sú zodpovední za komunikáciu, publikácie, údržbu, pravidelnú revíziu aspoň raz ročne a prípadné ukončenie podľa potreby.

### Ako riadenie (governance) interaguje s ADR?

Zvážte oblasti ako spôsoby práce vašej organizácie, akékoľvek osobitné potreby zhody, napríklad pre právne aspekty alebo aspekty ľudských zdrojov, ako chcete zaobchádzať s konsenzom oproti konfliktu oproti eskalácii. Existujú oblasti, osoby alebo tímy, ktoré môžu mať väčší vplyv než iné, pokiaľ ide o ADR, napríklad ho môžu schváliť, hlasovať o ňom alebo naň uvaliť veto?

Príklad odpovede: Riadenie ADR je v tomto poradí priority: generálny riaditeľ, technický riaditeľ, právny riaditeľ, tím, ktorý ADR implementuje, odborníci v tíme, ktorí najlepšie poznajú AD. Nikto iný nemá právomoc riadenia, pokiaľ nie je opísaná v ADR. 

### Aké princípy interagujú s ADR?

Zvážte oblasti ako spôsoby práce vašej organizácie, ktoré zahŕňajú rýchle pohyb oproti pomalému pohybu, konsenzus pri rozhodnutiach oproti konfliktu pri rozhodnutiach, preferencie rizika oproti preferenciám bezpečnosti, verejná diskusia oproti súkromnej diskusii a podobne.

Príklad odpovede: Používame vodcovské princípy sklonu ku konaniu, nesúhlasu a záväzku (disagree-and-commit), 70 % odhady sú dosť dobré pre ľahko vratné, ľahko izolovateľné rozhodnutia a verejné spôsoby práce s výnimkou dôverných informácií, ako je opísané v dohode o dôvernosti našej organizácie.

## Koncepty ďalšieho kroku pre ADR

[Arc42](https://arc42.org/) pragmaticky odpovedá na dve otázky a dá sa prispôsobiť vašim konkrétnym potrebám. Čo stojí za to dokumentovať/komunikovať o vašej architektúre? Ako to stojí za to dokumentovať/komunikovať? Arc42 zahŕňa záznamy architektonických rozhodnutí, ako aj usmernenia k cieľom, obmedzeniam, kontextu, kvalite, rizikám a ďalším témam.

[Model C4](https://c4model.com/) je ľahko naučiteľný prístup k diagramovaniu softvérovej architektúry, prívetivý pre vývojárov. C4 je hierarchická sada diagramov pre kontext, kontajnery, komponenty, kód a doplnkové diagramy pre krajinu systémov, dynamiku a nasadenie.

## Architektonické diagramy, pohľady a hľadiská

Architektonický diagram sa nazýva „architektonický pohľad“.

„Architektonický pohľad“ je inštanciou „architektonického hľadiska“.

„Architektonické hľadisko“ má konkrétne publikum s konkrétnymi záujmami.

Príklady architektonických hľadísk, pohľadov a diagramov:

- Obchodné schopnosti

- Obchodné procesy na vysokej úrovni

- [Toky hodnoty](https://en.wikipedia.org/wiki/Value_stream)

- Softvérové funkcie namapované na komponenty aplikácie

- Kontextový diagram [modelu C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- Diagram kontajnerov [modelu C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- [Diagram entít a vzťahov](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) na mapovanie dátových entít na komponenty aplikácie

- [Sekvenčné diagramy](https://en.wikipedia.org/wiki/Sequence_diagram) opisujúce funkčné toky v systémoch a integračné toky

- Diagramy [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) opisujúce dátové toky medzi komponentmi aplikácie

- Diagramy [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) opisujúce obchodné procesy / používateľské scenáre

- Diagramy [Identity and Access Management](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM)

- Diagramy [Role-Based Access Control](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) s rolami podľa komponentov aplikácie

- Diagramy [Attribute-Based Access Control](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) s atribútmi podľa komponentov aplikácie

- Diagramy ochrany osobných údajov

Súvisiace diagramy:

- Diagram prípadov použitia zobrazuje prípady použitia vedeniu/zákazníkom, čo predchádza požiadavkám, ktoré predchádzajú softvérovej architektúre.

- Diagram nasadenia zobrazuje fyzický hardvér/počítače, na ktorých sú nasadené softvérové komponenty.
- Diagram dátových tokov zobrazuje, ako sa dáta v systéme pohybujú a ako sa transformujú.
- Sekvenčný diagram slúži na zobrazenie toho, ako fungujú protokoly, napríklad HTTP, na časovej osi.

- Diagram aktivít zobrazuje pracovný tok aktivít vykonávaných softvérovým systémom, napríklad AI NPC.

## Fitness funkcie pre rozhodnutia ako kód

Fitness funkcie sú objektívne automatizované kontroly, napísané programovým kódom, ktoré overujú, že sa rozhodnutia dodržiavajú.

- Fitness funkcie robia rozhodnutia testovateľnými a zaručiteľnými.

- Fitness funkcie pre rozhodnutia môžu výrazne pomôcť zabezpečeniu kvality, regulačným procesom a cieľom riadenia.

### Ako sa fitness funkcie spájajú s rozhodnutiami

Záznam rozhodnutia dokumentuje rozhodnutie, zatiaľ čo fitness funkcia ho zaručuje.

- Príklad rozhodnutia: Používame event sourcing kvôli požiadavkám na audit.

- Príklad fitness funkcie: Používame server na kontinuálnu integráciu na testovanie, že všetky zmeny stavu musia produkovať udalosti.

### Prečo fitness funkcie pomáhajú rozhodnutiam

Objektívne merania: Fitness funkcie prejdú alebo zlyhajú, takže práca je viditeľná a jasná.

Nepretržité používanie: Fitness funkcie sú vaše živé pravidlá, spúšťané pri každom commite a builde.

Istota pri refaktorovaní: Fitness funkcie automaticky zachytia chyby v pravidlách rozhodnutí.

Škálovateľné riadenie: Fitness funkcie zaručujú štandardy bez vytvárania úzkych miest.

### Môžu fitness funkcie používať AI?

Fitness funkcie môžu využívať AI LLM pre rozhodnutia kladením otázok o vašej práci,
napríklad o vašich plánoch, kóde, schémach, API a ďalšom:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Jednotkové testovanie architektúry

[ArchUnit](https://www.archunit.org/): kontroluje architektonické pravidlá Java kódu pomocou ľubovoľného bežného frameworku na jednotkové testovanie v Jave.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): kontroluje architektonické pravidlá TypeScript kódu a JavaScript kódu pomocou Jest, Vitest, Jasmine a ďalších.

## Ochranné pravidlá rozhodnutí pre pull requesty

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
automaticky vyvolá správne záznamy rozhodnutí vo správnom okamihu — keď
vývojár aktívne mení kód, ktorý tieto rozhodnutia pokrývajú. Namiesto spoliehania sa na to,
že vývojári pred zlúčením preštudujú priečinok s dokumentáciou, sa relevantný kontext
objaví priamo v pull requeste.

Funguje s akýmkoľvek typom záznamu rozhodnutia: architektonické rozhodnutia, dátové rozhodnutia,
rozhodnutia o súlade s predpismi, klinické a lekárske rozhodnutia, bezpečnostné rozhodnutia a ďalšie.

Funguje aj s akýmkoľvek systémom CI (GitLab, Jenkins, CircleCI) a ako pre-commit hook.
Open source. Licencia MIT.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) je GitHub
Action, ktorá neprepustí pull request, ak sa sledované cesty kódu zmenia
bez pridania alebo aktualizácie záznamu architektonického rozhodnutia. Výnimky
sú explicitné: riadok `ADR-Exempt:` s odôvodnením prepustí bránu a zapíše sa do súhrnu
úlohy. Nezávislé od šablóny, bez závislostí. Open source. Licencia MIT.

## Ďalšie informácie

Úvod:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Šablóny:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Do hĺbky:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - bezplatná mesačná lekcia softvérovej architektúry

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Nástroje:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Usmernenia špecifické pre spoločnosti:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Príklady:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Videá:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcasty:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Knihy:

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

Pozri aj:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Dodávateľsky neutrálny, strojovo čitateľný formát YAML/JSON na reprezentáciu rozhodnutí s explicitným zdôvodnením, predpokladmi, kognitívnym stavom a kompromismi. Dopĺňa ADR pridaním štruktúrovaného, validovateľného zdôvodnenia do dokumentácie rozhodnutí.
