# Sprendimo įrašo šablonas pagal Jeffą Tyree ir Artą Akermaną

Tai architektūros sprendimo aprašo šablonas, paskelbtas straipsnyje ["Architecture Decisions: Demystifying Architecture", autoriai Jeff Tyree ir Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Problema**: aprašykite architektūrinę projektavimo problemą, kurią sprendžiate, nepalikdami klausimų, kodėl ją sprendžiate būtent dabar. Laikydamiesi minimalistinio požiūrio, spręskite ir dokumentuokite tik tas problemas, kurias reikia spręsti įvairiais gyvavimo ciklo etapais.

* **Sprendimas**: aiškiai nurodykite architektūros kryptį, t. y. pasirinktą poziciją.

* **Būsena**: sprendimo būsena, pavyzdžiui, laukiamas, priimtas ar patvirtintas.

* **Grupė**: galite naudoti paprastą grupavimą, pavyzdžiui, integracija, pateikimas, duomenys ir pan., kad padėtumėte sutvarkyti sprendimų rinkinį. Taip pat galite naudoti sudėtingesnę architektūros ontologiją, pavyzdžiui, Johno Kyaruzi ir Jano van Katwijko, kurioje yra abstraktesnių kategorijų, tokių kaip įvykis, kalendorius ir vieta. Pavyzdžiui, naudodami šią ontologiją, sprendimus, susijusius su atvejais, kai sistemai reikia informacijos, grupuotumėte pagal įvykį.

* **Prielaidos**: aiškiai aprašykite pagrindines aplinkos, kurioje priimate sprendimą, prielaidas – kainą, tvarkaraštį, technologiją ir pan. Atkreipkite dėmesį, kad aplinkos apribojimai (pavyzdžiui, priimti technologijų standartai, įmonės architektūra, dažnai naudojami šablonai ir pan.) gali riboti alternatyvas, kurias svarstote.

* **Apribojimai**: užfiksuokite visus papildomus aplinkos apribojimus, kuriuos gali sukelti pasirinkta alternatyva (sprendimas).

* **Pozicijos**: išvardykite pozicijas (įgyvendinamus variantus ar alternatyvas), kurias svarstėte. Joms dažnai reikia ilgų paaiškinimų, kartais net modelių ir diagramų. Tai nėra išsamus sąrašas. Tačiau galutinės peržiūros metu nenorite girdėti klausimo „Ar pagalvojote apie...?“; tai lemia patikimumo praradimą ir kitų architektūrinių sprendimų abejojimą. Šis skyrius taip pat padeda įsitikinti, kad išgirdote kitų nuomones; aiškiai nurodžius kitas nuomones, jų šalininkus lengviau įtraukti į jūsų sprendimą.

* **Argumentas**: apibūdinkite, kodėl pasirinkote tam tikrą poziciją, įskaitant tokius dalykus kaip įgyvendinimo kaina, bendroji nuosavybės kaina, laikas iki rinkos ir reikiamų kūrimo išteklių prieinamumas. Tai tikriausiai tiek pat svarbu, kiek ir pats sprendimas.

* **Implikacijos**: sprendimas turi daug implikacijų, kaip nurodo REMAP metamodelis. Pavyzdžiui, sprendimas gali sukelti poreikį priimti kitus sprendimus, sukurti naujų reikalavimų arba pakeisti esamus; nustatyti papildomų aplinkos apribojimų; reikalauti iš naujo derėtis su klientais dėl apimties ar tvarkaraščio; arba reikalauti papildomų darbuotojų mokymų. Aiškiai suprasti ir nurodyti sprendimo implikacijas gali būti labai veiksminga siekiant pritarimo ir kuriant architektūros vykdymo žemėlapį.

* **Susiję sprendimai**: akivaizdu, kad daug sprendimų yra tarpusavyje susiję; juos galite išvardyti čia. Tačiau praktiškai pastebėjome, kad naudingesnė yra atsekamumo matrica, sprendimų medžiai ar metamodeliai. Metamodeliai naudingi sudėtingiems ryšiams rodyti diagramomis (pavyzdžiui, Rose modeliai).

* **Susiję reikalavimai**: sprendimai turėtų būti grindžiami verslu. Kad parodytumėte atskaitomybę, aiškiai susiekite savo sprendimus su tikslais ar reikalavimais. Šiuos susijusius reikalavimus galite išvardyti čia, tačiau pastebėjome, kad patogiau remtis atsekamumo matrica. Galite įvertinti, kokį indėlį kiekvienas architektūros sprendimas įneša į kiekvieno reikalavimo tenkinimą, o tada įvertinti, kiek gerai reikalavimas tenkinamas per visus sprendimus. Jei sprendimas neprisideda prie reikalavimo tenkinimo, nepriimkite to sprendimo.

* **Susiję artefaktai**: išvardykite susijusius architektūros, projektavimo ar apimties dokumentus, kuriuos šis sprendimas veikia.

* **Susiję principai**: jei įmonė turi sutartą principų rinkinį, įsitikinkite, kad sprendimas atitinka vieną ar kelis iš jų. Tai padeda užtikrinti suderinimą tarp sričių ar sistemų.

* **Pastabos**: kadangi sprendimų priėmimo procesas gali trukti savaites, pastebėjome, kad naudinga užfiksuoti pastabas ir klausimus, kuriuos komanda aptaria viešinimo proceso metu.
