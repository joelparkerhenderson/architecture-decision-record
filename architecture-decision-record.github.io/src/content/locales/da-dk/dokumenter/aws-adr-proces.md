# AWS-processen for arkitekturbeslutningsposter

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

En arkitekturbeslutningspost (architectural decision record, ADR) er et dokument, der beskriver de valg, et team træffer om et vigtigt aspekt af den softwarearkitektur, det planlægger at bygge. Hver ADR beskriver arkitekturbeslutningen, dens kontekst og dens konsekvenser. ADR'er har en status og følger derfor en livscyklus. Se bilaget for eksempler på ADR'er.

ADR-processen frembringer en samling af arkitekturbeslutningsposter. Den samling udgør beslutningsloggen. Beslutningsloggen giver detaljerede implementerings- og designoplysninger ud over projektkonteksten. Projektmedlemmer gennemser titlen på hver ADR for at få et overblik over projektkonteksten. Derefter læser de ADR'erne for at få en dyb forståelse af projektets implementerings- og designvalg.

Når teamet accepterer en ADR, bliver den uforanderlig. Hvis nye indsigter kræver en anden beslutning, foreslår teamet en ny ADR. Når teamet accepterer den nye ADR, erstatter den den tidligere ADR.

## ADR-procesens omfang

Projektmedlemmer bør skrive en ADR for enhver arkitektonisk væsentlig beslutning, der påvirker softwareprojektet eller produktet, herunder (Richards og Ford 2020):

* Struktur (for eksempel mønstre som mikroservices)

* Ikke-funktionelle krav (sikkerhed, høj tilgængelighed, fejltolerance)

* Afhængigheder (kobling af komponenter)

* Grænseflader (API'er og offentliggjorte kontrakter)

* Konstruktionsteknikker (biblioteker, frameworks, værktøjer, processer)

* Funktionelle og ikke-funktionelle krav er de mest almindelige input til ADR-processen.


## Indholdet af en ADR

Når teamet identificerer behovet for en ADR, begynder teammedlemmer at skrive ADR'en på baggrund af en projektdækkende skabelon. (Se ADR-organisationen på GitHub for eksempler på skabeloner.) Skabelonen forenkler skrivningen af ADR'en og sikrer, at ADR'en indeholder alle relevante oplysninger. Som minimum bør hver ADR definere beslutningens kontekst, selve beslutningen og beslutningens konsekvenser for projektet og dets leverancer. (Se bilaget for eksempler på disse afsnit.) Et af de mest kraftfulde aspekter ved ADR-strukturen er fokus på årsagen til beslutningen frem for på, hvordan teamet implementerede den. Når du forstår, hvorfor teamet traf beslutningen, bliver det lettere for andre teammedlemmer at acceptere den, og du forhindrer, at andre arkitekter, der ikke deltog i beslutningsprocessen, omgør beslutningen senere.


## Processen for indførelse af ADR'er

Selv om ethvert teammedlem kan skrive en ADR, bør teamet fastlægge en definition af ejerskab for ADR'er. Hver forfatter, som er ADR'ens ejer, bør aktivt vedligeholde og kommunikere ADR'ens indhold. For at tydeliggøre dette ejerskab kalder denne vejledning i senere afsnit ADR-forfattere for ADR-ejere. Andre teammedlemmer kan til enhver tid bidrage til ADR'en. Hvis ADR'ens indhold ændres, før teamet accepterer ADR'en, skal ejeren godkende disse ændringer.

Når teamet har identificeret arkitekturbeslutningen og dens ejer, fremlægger ADR-ejeren tidligt i processen en ADR med status **Proposed** (foreslået). En ADR med status Proposed er klar til gennemgang.

Derefter starter ADR-ejeren gennemgangsprocessen for den ADR. Målet med ADR-gennemgangsprocessen er, at teamet beslutter, om det vil acceptere ADR'en, afgøre, at den kræver omarbejdning, eller afvise ADR'en. Projektteamet, inklusive ejeren, gennemgår ADR'en. Gennemgangsmødet bør starte med afsat tid til at læse ADR'en. I gennemsnit er 10–15 minutter tilstrækkeligt. I løbet af denne tid tilføjer hvert teammedlem kommentarer og spørgsmål for at markere uklare emner. Ved afslutningen af gennemgangsfasen læser ADR-ejeren hver kommentar og drøfter dem med teamet.

Når teamet finder handlingspunkter til at forbedre ADR'en, forbliver ADR'ens status **Proposed**. ADR-ejeren samler handlingerne og arbejder sammen med teamet om at tildele hver handling en ansvarlig. Ethvert teammedlem kan bidrage til handlingspunkterne og løse dem. Det er ADR-ejerens ansvar at omlægge gennemgangsprocessen.

Teamet kan også beslutte at afvise ADR'en. I så fald tilføjer ADR-ejeren årsagen til afvisningen for at forhindre fremtidige diskussioner om samme emne. Ejeren ændrer ADR'ens status til **Rejected** (afvist).

Når teamet godkender ADR'en, tilføjer ejeren et tidsstempel, en version og en liste over interessenter. Derefter opdaterer ejeren statussen til **Accepted** (accepteret).

ADR'en og den beslutningslog, den bidrager til, repræsenterer teamets beslutninger og giver en historik over alle beslutninger. Hvor det er muligt, bruger teamet ADR'er som reference under kode- og arkitekturgennemgange. Ud over at udføre kodegennemgange, designarbejde og implementeringsarbejde bør teammedlemmer konsultere ADR'er ved strategiske beslutninger om produktet.

Som god praksis bør alle softwareændringer gennemgå peer review og kræve mindst én godkendelse. Under kodegennemgangen kan en gennemgående finde en ændring, der overtræder en eller flere ADR'er. I så fald beder gennemgangeren forfatteren af kodeændringen om at rette koden og deler linket til ADR'en/ADR'erne. Når forfatteren har rettet koden, får vedkommende godkendelse fra en peer-gennemgående, og koden flettes ind i den primære kodebase.


## ADR-gennemgangsprocessen

Når teamet har accepteret eller afvist en ADR, bør det behandle den som et uforanderligt dokument. For at ændre en eksisterende ADR skal teamet skrive en ny ADR, fastlægge gennemgangsprocessen for den nye ADR og godkende ADR'en. Når teamet godkender den nye ADR, skal ejeren ændre den gamle ADR's status til **Superseded** (erstattet). 
