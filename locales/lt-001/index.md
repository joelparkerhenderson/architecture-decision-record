# Architektūros sprendimo įrašas (ADR)

Architektūros sprendimo įrašas (ADR) yra dokumentas, kuriame užfiksuotas svarbus priimtas architektūrinis sprendimas kartu su jo kontekstu ir pasekmėmis.

> [!IMPORTANT]
> Prieš naudodami šiuos išteklius bet kurioje kritinėje sistemoje, atlikite savo kruopštų patikrinimą.

Turinys:

- [Kas yra architektūros sprendimo įrašas?](#kas-yra-architektūros-sprendimo-įrašas)
- [Kaip pradėti naudoti ADR](#kaip-pradėti-naudoti-adr)
- [Kaip pradėti naudoti ADR su įrankiais](#kaip-pradėti-naudoti-adr-su-įrankiais)
- [Kaip pradėti naudoti ADR su git](#kaip-pradėti-naudoti-adr-su-git)
- [Claude Code įgūdžiai ADR](#claude-code-įgūdžiai-adr)
- [ADR failų pavadinimų konvencijos](#adr-failų-pavadinimų-konvencijos)
- [Patarimai, kaip rašyti gerus ADR](#patarimai-kaip-rašyti-gerus-adr)
- [ADR sprendimo įrašų šablonų pavyzdžiai](#adr-sprendimo-įrašų-šablonų-pavyzdžiai)
- [Komandinio darbo patarimai dėl ADR](#komandinio-darbo-patarimai-dėl-adr)
- [Komandinio darbo klausimai dėl ADR](#komandinio-darbo-klausimai-dėl-adr)
- [Tolesnių žingsnių konceptai ADR](#tolesnių-žingsnių-konceptai-adr)
- [Architektūros diagramos, vaizdai ir požiūriai](#architektūros-diagramos-vaizdai-ir-požiūriai)
- [Tinkamumo funkcijos sprendimams kaip kodui](#tinkamumo-funkcijos-sprendimams-kaip-kodui)
- [Sprendimų apsauginės priemonės pull request'ams](#sprendimų-apsauginės-priemonės-pull-requestams)
- [Daugiau informacijos](#daugiau-informacijos)

Šablonai:

- [Sprendimo įrašo šablonas pagal Jeffą Tyree ir Artą Akermaną](sablonai/sprendimo-iraso-sablonas-jeff-tyree-ir-art-akerman/)
- [Sprendimo įrašo šablonas pagal Michaelą Nygardą](sablonai/sprendimo-iraso-sablonas-michael-nygard/)
- [Sprendimo įrašo šablonas pagal EdgeX](sablonai/sprendimo-iraso-sablonas-edgex/)
- [Sprendimo įrašo šablonas pagal arc42](sablonai/sprendimo-iraso-sablonas-arc42/)
- [Sprendimo įrašo šablonas Aleksandrijos šablonui](sablonai/sprendimo-iraso-sablonas-aleksandrijos-sablonui/)
- [Sprendimo įrašo šablonas verslo pagrindimui](sablonai/sprendimo-iraso-sablonas-verslo-pagrindimui/)
- [Sprendimo įrašo šablonas pagal MADR projektą](sablonai/sprendimo-iraso-sablonas-madr-projekto/)
- [Sprendimo įrašo šablonas su Planguage](sablonai/sprendimo-iraso-sablonas-su-planguage/)
- [Sprendimo įrašo šablonas pagal Paulo Mersoną](https://github.com/pmerson/ADR-template)
- [Sprendimo įrašo šablonas pagal Olafą Zimmermanną](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Sprendimo įrašo šablonas pagal Garethą Morganą](sablonai/sprendimo-iraso-sablonas-gareth-morgan/)
- [Sprendimo įrašo šablonas pagal GIG Cymru NHS Wales](sablonai/sprendimo-iraso-sablonas-gig-cymru-nhs-wales/)
- [Sprendimo įrašo šablonas svarbiems techniniams sprendimams (ITD) pagal Ignacio Larrañaga](sablonai/sprendimo-iraso-sablonas-svarbiems-techniniams-sprendimams/)

Pavyzdžiai:

- [CSS karkasas](pavyzdziai/css-karkasas/)
- [Aplinkos kintamųjų konfigūracija](pavyzdziai/aplinkos-kintamuju-konfiguracija/)
- [Metrikos, monitoriai, įspėjimai](pavyzdziai/metrikos-monitoriai-ispejimai/)
- [Microsoft Azure DevOps](pavyzdziai/microsoft-azure-devops/)
- [Monorepo ar multirepo](pavyzdziai/monorepo-ar-multirepo/)
- [Programavimo kalbos](pavyzdziai/programavimo-kalbos/)
- [Paslapčių saugojimas](pavyzdziai/paslapciu-saugojimas/)
- [Laiko žymės formatas](pavyzdziai/laiko-zymes-formatas/)
- [Daugiau...](pavyzdziai/)

## Kas yra architektūros sprendimo įrašas?

**Architektūros sprendimo įrašas** (ADR) yra dokumentas, kuriame užfiksuotas svarbus priimtas architektūrinis sprendimas kartu su jo kontekstu ir pasekmėmis.

**Architektūros sprendimas** (AD) yra programinės įrangos projektavimo pasirinkimas, kuriuo sprendžiamas reikšmingas reikalavimas.

**Architektūros sprendimų žurnalas** (ADL) yra visų konkrečiam projektui (ar organizacijai) sukurtų ir prižiūrimų ADR rinkinys.

**Architektūriškai reikšmingas reikalavimas** (ASR) yra reikalavimas, kuris turi išmatuojamą poveikį programinės įrangos sistemos architektūrai.

Visa tai priklauso **architektūros žinių valdymo** (AKM) temai.

Šio dokumento tikslas – greitai apžvelgti ADR, parodyti, kaip juos kurti, ir nurodyti, kur ieškoti daugiau informacijos.

Santrumpos:

  * **AD**: architektūros sprendimas

  * **ADL**: architektūros sprendimų žurnalas

  * **ADR**: architektūros sprendimo įrašas

  * **AKM**: architektūros žinių valdymas

  * **ASR**: architektūriškai reikšmingas reikalavimas

## Kaip pradėti naudoti ADR

Norėdami pradėti naudoti ADR, pasikalbėkite su komandos nariais apie šias sritis.

Sprendimų nustatymas:

  * Kiek skubus ir kiek svarbus yra AD?

  * Ar jį reikia priimti dabar, ar galima palaukti, kol paaiškės daugiau?

  * Sprendimams nustatyti gali padėti tiek asmeninė, tiek kolektyvinė patirtis, taip pat pripažinti projektavimo metodai ir praktikos.

  * Idealiu atveju palaikykite sprendimų užduočių sąrašą, papildantį produkto užduočių sąrašą.

Sprendimų priėmimas:

  * Yra daug sprendimų priėmimo būdų – tiek bendrųjų, tiek būdingų programinės įrangos architektūrai, pavyzdžiui, dialogų žemėlapiai.

  * Grupinis sprendimų priėmimas yra aktyvi tyrimų tema.

Sprendimų įgyvendinimas ir užtikrinimas:

  * AD naudojami programinės įrangos projektavime, todėl apie juos reikia informuoti sistemos suinteresuotuosius asmenis, kurie ją finansuoja, kuria ir eksploatuoja, ir jie turi juos pritarti.

  * Dvi susijusios praktikos – architektūriškai aiškus kodavimo stilius ir kodo peržiūros, kuriose daugiausia dėmesio skiriama architektūriniams rūpesčiams ir sprendimams.

  * AD taip pat reikia (iš naujo) apsvarstyti modernizuojant programinės įrangos sistemą jos evoliucijos metu.

Sprendimų dalijimasis (neprivaloma):

  * Daugelis AD kartojasi įvairiuose projektuose.

  * Todėl patirtis, susijusi su ankstesniais sprendimais, tiek gerais, tiek blogais, gali būti vertingas pakartotinai naudojamas turtas, kai taikoma aiški žinių valdymo strategija.

Sprendimų dokumentavimas:

  * Yra daug sprendimų fiksavimo šablonų ir įrankių.

  * Žr. lanksčiąsias bendruomenes, pvz., M. Nygardo ADR.

  * Žr. tradicinius programinės įrangos inžinerijos ir architektūros projektavimo procesus, pvz., lentelių išdėstymus, kuriuos siūlo IBM UMF ir „CapitalOne“ atstovai Tyree ir Akermanas.

Daugiau:

  * Pirmiau pateikti veiksmai perimti iš Vikipedijos straipsnio [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Kaip pradėti naudoti ADR su įrankiais

- [MySpec](https://myspec.dev) — automatizuota specifikacijų ir architektūrinių sprendimų platforma, kuri projekto konstituciją, techninę architektūrą ir ADR sutvarko į aiškų Markdown, pateikiamą per MCP.

ADR su įrankiais galite pradėti naudoti bet kokiu jums patinkančiu būdu.

Pavyzdžiui:

  * Jei mėgstate naudoti „Google Drive“ ir redagavimą internete, galite sukurti „Google“ dokumentą arba „Google“ skaičiuoklę.

  * Jei mėgstate naudoti šaltinio kodo versijų valdymą, pavyzdžiui, git, galite sukurti failą kiekvienam ADR.

  * Jei mėgstate naudoti projektų planavimo įrankius, pavyzdžiui, „Atlassian Jira“, galite naudoti įrankio planavimo sekiklį.

  * Jei mėgstate viki svetaines, pavyzdžiui, „MediaWiki“, galite sukurti ADR viki.

## Kaip pradėti naudoti ADR su git

Jei mėgstate git versijų valdymą, štai kaip mes mėgstame pradėti naudoti ADR su git tipiniame programinės įrangos projekte su šaltinio kodu.

Sukurkite katalogą ADR failams:

```sh
$ mkdir adr
```

Kiekvienam ADR sukurkite tekstinį failą, pavyzdžiui, `choose-database.md`:

```sh
$ vi choose-database.md
```

ADR rašykite bet ką norite. Idėjų ieškokite šiame saugykloje esančiuose šablonuose.

Įkelkite ADR į savo git saugyklą (angl. commit).

## Claude Code įgūdžiai ADR

Šioje saugykloje yra du [Claude Code](https://claude.com/claude-code) įgūdžiai (angl. skills) kataloge [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), kad DI programavimo agentas galėtų rašyti ir prižiūrėti ADR taip, kaip rekomenduoja šis projektas:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — bendrosios paskirties, skirtas visiems, rašantiems ADR bet kuriame projekte. Padeda nuspręsti, ar sprendimui reikia ADR, sukuria katalogą `adr/` arba `decisions/`, parenka failo pavadinimą, pasirenka šabloną iš vienuolikos pateiktų karkasų ir parašo tvirtus skyrius „Kontekstas“ / „Sprendimas“ / „Pasekmės“.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — skirtas būtent šios saugyklos prižiūrėtojams. Aprašo saugyklos struktūrą, README / lokalių atspindėjimo konvenciją ir tikslius veiksmus, kaip pridėti naują šabloną, pavyzdį ar nuorodą į įrankį.

Norėdami naudoti įgūdį, nukopijuokite jo aplanką į `.claude/skills/` savo saugyklos, kurioje dirbate, šakniniame kataloge (arba į `~/.claude/skills/`, kad jis būtų prieinamas kiekviename projekte), tada paprašykite Claude Code parašyti ar peržiūrėti ADR.

## ADR failų pavadinimų konvencijos

Jei nusprendėte kurti ADR naudodami įprastus tekstinius failus, galbūt norėsite susikurti savo ADR failų pavadinimų konvenciją.

Mes teikiame pirmenybę failų pavadinimų konvencijai, turinčiai konkretų formatą.

Pavyzdžiai:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Mūsų failų pavadinimų konvencija:

  * Pavadinime yra tiesioginės nuosakos veiksmažodžio frazė esamuoju laiku. Tai gerina skaitomumą ir atitinka mūsų įkėlimo pranešimų (angl. commit message) formatą.

  * Pavadinime naudojamos mažosios raidės ir brūkšneliai (kaip ir šioje saugykloje). Tai skaitomumo ir sistemos patogumo pusiausvyra.

  * Plėtinys yra markdown. Tai gali būti naudinga, kad formatuoti būtų lengva.

## Patarimai, kaip rašyti gerus ADR

Gero ADR savybės:

* Pagrindimas: paaiškinkite konkretaus AD priėmimo priežastis. Tai gali apimti kontekstą (žr. toliau), įvairių galimų pasirinkimų privalumus ir trūkumus, savybių palyginimus, sąnaudų ir naudos aptarimus ir kita.

* Konkretumas: kiekvienas ADR turi būti apie vieną AD, o ne apie kelis.

* Laiko žymos: nurodykite, kada parašytas kiekvienas ADR elementas. Tai ypač svarbu aspektams, kurie laikui bėgant gali keistis, pavyzdžiui, sąnaudoms, tvarkaraščiams, mastelio keitimui ir panašiems dalykams.

* Nekeičiamumas: nekeiskite esamos ADR informacijos. Vietoj to papildykite ADR nauja informacija arba pakeiskite ADR sukurdami naują ADR.

Gero ADR skyriaus „Kontekstas“ savybės:

* Paaiškinkite savo organizacijos situaciją ir verslo prioritetus.

* Pateikite pagrindimą ir svarstymus, grindžiamus jūsų komandų socialine sudėtimi ir įgūdžiais.

* Nurodykite tinkamus privalumus ir trūkumus ir aprašykite juos taip, kad jie atitiktų jūsų poreikius ir tikslus.

Gero ADR skyriaus „Pasekmės“ savybės:

* Paaiškinkite, kas seka iš sprendimo priėmimo. Tai gali apimti poveikį, rezultatus, išvestis, tolesnius veiksmus ir kita.

* Pateikite informaciją apie visus vėlesnius ADR. Gana įprasta, kad vienas ADR sukelia poreikį kurti daugiau ADR, pavyzdžiui, kai vienu ADR daromas didelis bendras pasirinkimas, o tai savo ruožtu sukuria poreikį priimti daugiau mažesnių sprendimų.

* Nurodykite visus poveikio peržiūros procesus. Įprasta, kad komandos kiekvieną ADR peržiūri po mėnesio, palygindamos ADR informaciją su tuo, kas įvyko praktikoje, kad mokytųsi ir tobulėtų.

Naujas ADR gali pakeisti ankstesnį ADR:

* Kai priimamas AD, kuris pakeičia ar panaikina ankstesnį ADR, reikėtų sukurti naują ADR

## ADR sprendimo įrašų šablonų pavyzdžiai

ADR šablonų pavyzdžiai, kuriuos surinkome internete:

- [ADR šablonas pagal Michaelą Nygardą](sablonai/sprendimo-iraso-sablonas-michael-nygard/) (paprastas ir populiarus)

- [ADR šablonas pagal Jeffą Tyree ir Artą Akermaną](sablonai/sprendimo-iraso-sablonas-jeff-tyree-ir-art-akerman/) (sudėtingesnis)

- [ADR šablonas Aleksandrijos šablonui](sablonai/sprendimo-iraso-sablonas-aleksandrijos-sablonui/) (paprastas, su konteksto detalėmis)

- [ADR šablonas verslo pagrindimui](sablonai/sprendimo-iraso-sablonas-verslo-pagrindimui/) (labiau orientuotas į MBA, su sąnaudomis, SSGG analize ir daugiau nuomonių)

- [ADR šablonas pagal Markdown Any Decision Records (MADR) projektą](sablonai/sprendimo-iraso-sablonas-madr-projekto/) (paprasta ir išplėstinė versija; pastaroji pabrėžia variantus ir jų privalumus bei trūkumus)

- [ADR šablonas su Planguage](sablonai/sprendimo-iraso-sablonas-su-planguage/) (labiau orientuotas į kokybės užtikrinimą)

- [Šablonas svarbiems techniniams sprendimams (ITD) pagal Ignacio Larrañaga](sablonai/sprendimo-iraso-sablonas-svarbiems-techniniams-sprendimams/) (liesas, pirmiausia pateikiantis sprendimą, optimizuotas greitai vadovų peržiūrai)

## Komandinio darbo patarimai dėl ADR

Jei svarstote su savo komanda naudoti sprendimų įrašus, štai keletas patarimų, kuriuos išmokome dirbdami su daugeliu komandų.

Turite galimybę vesti komandos narius pirmyn kartu kalbėdami apie „kodėl“, o ne primesdami „ką“. Pavyzdžiui, sprendimų įrašai yra būdas komandoms protingiau mąstyti ir geriau bendrauti; sprendimų įrašai neturi vertės, jei tai tik po fakto primesti popieriai.

Kai kurios komandos daug labiau mėgsta pavadinimą „sprendimai“ nei santrumpą „ADR“. Kai kai kurios komandos naudoja katalogo pavadinimą „decisions“, tarsi įsijungia lemputė, ir komanda pradeda į katalogą dėti daugiau informacijos, pavyzdžiui, tiekėjų sprendimus, planavimo sprendimus, tvarkaraščių sprendimus ir pan. Visiems šiems informacijos tipams galima naudoti tą patį šabloną. Spėjame, kad žmonės greičiau mokosi iš žodžių („sprendimai“) nei iš santrumpų („ADR“), kad žmones labiau motyvuoja rašyti nebaigtus dokumentus, kai žodis „įrašas“ pašalinamas, o kai kurie programuotojai ir vadovai taip pat nemėgsta žodžio „architektūra“.

Teoriškai nekeičiamumas yra idealus. Praktiškai mūsų komandoms geriau pasiteisino keičiamumas. Naują informaciją įterpiame į esamą ADR su datos žyma ir pastaba, kad informacija atsirado po sprendimo. Toks požiūris veda prie „gyvo dokumento“, kurį visi galime atnaujinti. Tipiniai atnaujinimai atsiranda, kai informaciją gauname dėl naujų komandos narių, naujų pasiūlymų, realių mūsų naudojimo rezultatų arba po fakto įvykusių trečiųjų šalių pokyčių, pavyzdžiui, tiekėjų galimybių, kainodaros planų, licencijų sutarčių ir pan.

## Komandinio darbo klausimai dėl ADR

### Kas gali sukurti ADR?

Apsvarstykite tokias sritis kaip konkretūs žmonės, konkrečios pareigos, konkrečios komandos ar konkretūs skyriai; taip pat apsvarstykite, ar yra žmonių, pareigų, komandų ar skyrių, kurie gali užsakyti ADR, t. y. paprašyti, kad jį parašytų kas nors kitas.

Atsakymo pavyzdys: bet kuris mūsų organizacijos asmuo, perskaitęs architektūros sprendimo įrašo README puslapį, gali pasiūlyti ADR, t. y. gali pradėti jį rašyti ir pasidalyti juo su komanda.

### Kas pateisina ADR kūrimą?

Apsvarstykite tokias sritis kaip jūsų organizacijos komandų darbo būdai, programinės įrangos sistemos struktūra, tarpkomandinis koordinavimas, ilgalaikis prižiūrimumas, išorinės sąsajos, kam norite duoti naudos ir panašiai.

Atsakymo pavyzdys: ADR norime kurti, kai norime, kad būsimi programuotojai suprastų, „kodėl“ darome tai, ką darome.

### Kas pateisina ADR nekūrimą?

Apsvarstykite tokias sritis kaip sprendimai, kurie nėra susiję su architektūra arba yra smulkūs, pavyzdžiui, mažos rizikos, savarankiški ar vieno programuotojo sprendimai, arba jau visiškai aprėpti kitur, pavyzdžiui, standartuose, politikose ar dokumentacijoje, arba yra laikini, pavyzdžiui, apėjimo būdai, koncepcijos įrodymai ar eksperimentai.

Atsakymo pavyzdys: ADR norime praleisti, kai sprendimo apimtis, trukmė, rizika ir kaina yra ribotos arba jis jau aprėptas kitur.

### Koks yra ADR gyvavimo ciklas?

Apsvarstykite tokias sritis kaip kūrimo procesas, tyrimo procesas, sprendimo priėmimo procesas, įgyvendinimo procesas ir nutraukimo procesas. Apsvarstykite, kaip sekti ADR gyvavimo ciklą laikui bėgant, pavyzdžiui, kaip perkelti ADR iš vienos būsenos į kitą ir kaip apie tai informuoti suinteresuotuosius asmenis.

Atsakymo pavyzdys: norime, kad ADR turėtų penkis gyvavimo ciklo etapus: inicijavimas → tyrimas → vertinimas → įgyvendinimas → priežiūra → nutraukimas.

### Kokie yra ADR gyvavimo ciklo žingsnių kriterijai?

Apsvarstykite tokias sritis kaip ADR priėmimo kriterijai, t. y. kaip žinoti, kad jis pakankamai geras, kad pereitų iš vieno gyvavimo ciklo žingsnio į kitą? Ar problema aiškiai suformuluota? Ar apsvarstytos alternatyvos? Ar kompromisai pakankamai gerai suprasti ir dokumentuoti?
Ar visas svarbus kontekstas pateiktas? Ar įtraukti visi svarbūs suinteresuotieji asmenys? Ar atsižvelgta į visas atsiliepimus?

Atsakymo pavyzdys: norime, kad suinteresuotieji asmenys dėl ADR balsuotų, kai aktyvi komanda: 1) baigė tyrimą, 2) baigė vertinimą, 3) paskelbė ADR pasiūlymą suinteresuotiesiems asmenims prašydama komentarų su vienos savaitės laiko riba, 4) į visus suinteresuotųjų asmenų komentarus atsižvelgta ir jie išspręsti.

### Kokios pareigos ir atsakomybės sąveikauja su ADR?

Apsvarstykite tokias pareigas kaip pasiūlytojas, tyrėjas, vertintojas, peržiūrėtojas, tvirtintojas, prižiūrėtojas ir panašiai. Apsvarstykite tokias atsakomybes kaip bendravimas su suinteresuotaisiais asmenimis, lūkesčių išpildymo užtikrinimas, dalijimasis svetainėje ar intranete ir darbo periodinė peržiūra, ypač kai įvyksta svarbių pokyčių.

Atsakymo pavyzdys: norime, kad kiekvienas ADR visada turėtų pagrindinį kontaktinį asmenį, antrinį kontaktinį asmenį ir atsakingą komandą; jie atsakingi už komunikaciją, publikavimą, priežiūrą, periodinę peržiūrą bent kartą per metus ir galimą nutraukimą, kai reikia.

### Kaip valdysena sąveikauja su ADR?

Apsvarstykite tokias sritis kaip jūsų organizacijos darbo būdai, ypatingi atitikties poreikiai, pavyzdžiui, teisiniai ar žmogiškųjų išteklių aspektai, kaip norite spręsti konsensuso, konflikto ir eskalavimo klausimus. Ar yra sričių, žmonių ar komandų, kurie dėl ADR gali turėti daugiau įtakos nei kiti, pavyzdžiui, galėti jį patvirtinti, dėl jo balsuoti ar uždėti veto?

Atsakymo pavyzdys: ADR valdysena eina šia prioriteto tvarka: generalinis direktorius (CEO), technologijų direktorius (CTO), teisės direktorius (CLO), komanda, įgyvendinanti ADR, komandos ekspertai, geriausiai išmanantys AD. Niekas kitas neturi valdysenos teisių, nebent tai aprašyta ADR.

### Kokie principai sąveikauja su ADR?

Apsvarstykite tokias sritis kaip jūsų organizacijos darbo būdai, apimantys greitą ar lėtą judėjimą, sprendimų konsensusą ar sprendimų konfliktą, rizikos ar saugumo pirmenybes, viešą ar privačią diskusiją ir panašiai.

Atsakymo pavyzdys: naudojame šiuos lyderystės principus: polinkis veikti, nesutikti ir įsipareigoti, 70 % įvertinimų pakanka lengvai atšaukiamiems ir lengvai izoliuojamiems sprendimams, ir viešas darbo būdas, išskyrus konfidencialią informaciją, kaip aprašyta mūsų organizacijos konfidencialumo sutartyje.

## Tolesnių žingsnių konceptai ADR

[Arc42](https://arc42.org/) pragmatiškai atsako į du klausimus ir gali būti pritaikytas jūsų konkretiems poreikiams. Ką turėtumėte dokumentuoti / perteikti apie savo architektūrą? Kaip turėtumėte dokumentuoti / perteikti? Arc42 apima architektūros sprendimo įrašus ir nurodymus dėl tikslų, apribojimų, kontekstų, kokybės, rizikų ir kt.

[C4 modelis](https://c4model.com/) yra lengvai išmokstamas, programuotojams draugiškas programinės įrangos architektūros diagramų kūrimo požiūris. C4 yra hierarchinių diagramų rinkinys kontekstui, konteineriams, komponentams, kodui, taip pat pagalbinės diagramos sistemų kraštovaizdžiui, dinamikai ir diegimui.

## Architektūros diagramos, vaizdai ir požiūriai

Architektūros diagrama vadinama „architektūros vaizdu“.

„Architektūros vaizdas“ yra „architektūros požiūrio“ egzempliorius.

„Architektūros požiūris“ turi konkrečią auditoriją su konkrečiais rūpesčiais.

Architektūros požiūrių, vaizdų ir diagramų pavyzdžiai:

- Verslo gebėjimai

- Aukšto lygio verslo procesai

- [Vertės srautai (Value Streams)](https://en.wikipedia.org/wiki/Value_stream)

- Programinės įrangos funkcijos, susietos su programų komponentais

- [C4 modelio](https://en.wikipedia.org/wiki/C4_model) konteksto diagrama (TO-BE / AS-IS)

- [C4 modelio](https://en.wikipedia.org/wiki/C4_model) konteinerių diagrama (TO-BE / AS-IS)

- [Esybių ryšių diagrama (Entity-relationship Diagram)](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD), skirta duomenų esybėms susieti su programų komponentais

- [Sekų diagramos (Sequence Diagrams)](https://en.wikipedia.org/wiki/Sequence_diagram) funkcinėms eigoms sistemose ir integracijoms aprašyti

- [Verslo procesų modelio ir notacijos (Business Process Model and Notation)](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagramos duomenų srautams tarp programų komponentų aprašyti

- [Verslo procesų modelio ir notacijos (Business Process Model and Notation)](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagramos verslo procesams / naudotojų scenarijams aprašyti

- [Tapatybės ir prieigos valdymo (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) diagramos

- [Vaidmenimis grįstos prieigos kontrolės (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) diagramos su vaidmenimis kiekvienam programos komponentui

- [Atributais grįstos prieigos kontrolės (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) diagramos su atributais kiekvienam programos komponentui

- Privatumo diagramos

Susijusios diagramos:

- Naudojimo atvejų diagrama rodo naudojimo atvejus vadovybei / klientams; ji eina prieš reikalavimus, o šie – prieš programinės įrangos architektūrą.

- Diegimo diagrama rodo fizinę aparatinę įrangą / kompiuterius, kuriuose diegiami programinės įrangos komponentai.
- Duomenų srautų diagrama rodo, kaip duomenys juda per sistemą ir yra transformuojami.
- Sekų diagrama naudojama parodyti, kaip protokolai, tokie kaip HTTP, veikia laiko ašyje.

- Veiklos diagrama vaizduoja veiklų, kurias atlieka programinės įrangos sistema, darbo eigą, pavyzdžiui, kaip NPC DI.

## Tinkamumo funkcijos sprendimams kaip kodui

Tinkamumo funkcijos (angl. fitness functions) yra objektyvūs automatizuoti patikrinimai, parašyti programavimo kodu, kurie tikrina, ar sprendimų laikomasi.

- Tinkamumo funkcijos leidžia sprendimus išbandyti ir užtikrinti.

- Sprendimų tinkamumo funkcijos gali labai padėti kokybės užtikrinimui, reguliaciniams procesams ir valdysenos tikslams.

### Kaip tinkamumo funkcijos susijusios su sprendimais

Sprendimo įrašas dokumentuoja sprendimą, o tinkamumo funkcija sprendimą užtikrina.

- Sprendimo pavyzdys: audito reikalavimams naudojame įvykių šaltinių modelį (angl. event sourcing).

- Tinkamumo funkcijos pavyzdys: nuolatinės integracijos serveriu tikriname, ar visi būsenos pakeitimai privalo sukurti įvykius.

### Kodėl tinkamumo funkcijos padeda sprendimams

Objektyvūs matavimai: tinkamumo funkcijos arba praeina, arba nepraeina, todėl darbas matomas ir aiškus.

Nuolatinis naudojimas: tinkamumo funkcijos yra jūsų gyvos taisyklės, vykdomos su kiekvienu įkėlimu (angl. commit) ir kūrimu.

Pasitikėjimas pertvarkant kodą: tinkamumo funkcijos automatiškai pagauna sprendimų taisyklių klaidas.

Mastelio keitimą atlaikanti valdysena: tinkamumo funkcijos užtikrina standartus nesukurdamos kliūčių.

### Ar tinkamumo funkcijos gali naudoti dirbtinį intelektą?

Tinkamumo funkcijos sprendimams gali pasitelkti DI didžiuosius kalbos modelius (LLM), užduodamos klausimus apie jūsų darbą,
pavyzdžiui, apie planus, kodą, schemas, API ir kita:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Architektūros vienetų testavimas

[ArchUnit](https://www.archunit.org/): tikrinkite Java kodo architektūros taisykles naudodami bet kurią paprastą Java vienetų testų sistemą.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): tikrinkite TypeScript ir JavaScript kodo architektūros taisykles naudodami Jest, Vitest, Jasmine ir kt.

## Sprendimų apsauginės priemonės pull request'ams

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
automatiškai parodo tinkamus sprendimų įrašus tinkamu momentu – kai
programuotojas aktyviai keičia kodą, kurį tie sprendimai apima. Užuot
tikėjęsi, kad programuotojai prieš sujungdami perskaitys dokumentų aplanką,
svarbus kontekstas pasirodo tiesiogiai pull request.

Tai veikia su bet kokio tipo sprendimų įrašais: architektūros sprendimais,
duomenų sprendimais, atitikties sprendimais, klinikiniais ir medicininiais
sprendimais, saugumo sprendimais ir kt.

Veikia su bet kuria CI sistema (GitLab, Jenkins, CircleCI) ir kaip pre-commit
kabliukas. Atvirasis kodas. MIT licencija.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) yra GitHub
Action, kuris nepraleidžia pull request, kai stebimi kodo keliai pasikeičia
nepridėjus ar neatnaujinus architektūros sprendimo įrašo. Atleidimai aiškūs:
eilutė `ADR-Exempt:` su priežastimi praleidžia vartus ir įrašoma į užduoties
santrauką. Nepriklauso nuo šablono, be priklausomybių. Atvirasis kodas. MIT licencija.

## Daugiau informacijos

Įvadas:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Šablonai:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Išsamiau:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - nemokama mėnesinė programinės įrangos architektūros pamoka

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Įrankiai:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Konkrečių įmonių rekomendacijos:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Pavyzdžiai:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Vaizdo įrašai:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Tinklalaidės:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Knygos:

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

Taip pat žr.:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Nuo tiekėjo nepriklausomas, mašininiu būdu skaitomas YAML/JSON formatas sprendimams vaizduoti su aiškia argumentacija, prielaidomis, kognityvine būsena ir kompromisais. Papildo ADR pridėdamas struktūrizuotą, patikrinamą argumentaciją prie sprendimų dokumentacijos.
