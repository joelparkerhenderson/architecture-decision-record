# Arkitekturbeslutningspost (ADR)

En arkitekturbeslutningspost (ADR) er et dokument, der fastholder en vigtig arkitekturbeslutning sammen med dens sammenhæng og konsekvenser.

> [!IMPORTANT]
> Gør din egen rettidige omhu med disse ressourcer, før du bruger dem i kritiske systemer.

Indhold:

- [Hvad er en arkitekturbeslutningspost?](#hvad-er-en-arkitekturbeslutningspost)
- [Sådan kommer du i gang med ADR'er](#sådan-kommer-du-i-gang-med-adrer)
- [Sådan kommer du i gang med ADR'er med værktøjer](#sådan-kommer-du-i-gang-med-adrer-med-værktøjer)
- [Sådan kommer du i gang med ADR'er med git](#sådan-kommer-du-i-gang-med-adrer-med-git)
- [Claude Code-færdigheder til ADR'er](#claude-code-færdigheder-til-adrer)
- [Konventioner for filnavne](#konventioner-for-filnavne)
- [Forslag til at skrive gode ADR'er](#forslag-til-at-skrive-gode-adrer)
- [ADR-eksempelskabeloner](#adr-eksempelskabeloner)
- [Teamarbejdsråd til ADR'er](#teamarbejdsråd-til-adrer)
- [Teamwork-spørgsmål til ADR'er](#teamwork-spørgsmål-til-adrer)
- [Næste-skridt-begreber til ADR'er](#næste-skridt-begreber-til-adrer)
- [Arkitekturdiagrammer, visninger og synsvinkler](#arkitekturdiagrammer-visninger-og-synsvinkler)
- [Fitnessfunktioner for beslutninger som kode](#fitnessfunktioner-for-beslutninger-som-kode)
- [Beslutningsautoværn til pull requests](#beslutningsautoværn-til-pull-requests)
- [Mere information](#mere-information)

Skabeloner:

- [Skabelon til beslutningspost fra Jeff Tyree og Art Akerman](skabeloner/skabelon-til-beslutningspost-fra-jeff-tyree-og-art-akerman/)
- [Skabelon til beslutningspost fra Michael Nygard](skabeloner/skabelon-til-beslutningspost-fra-michael-nygard/)
- [Skabelon til beslutningspost fra EdgeX](skabeloner/skabelon-til-beslutningspost-fra-edgex/)
- [Skabelon til beslutningspost fra arc42](skabeloner/skabelon-til-beslutningspost-fra-arc42/)
- [Skabelon til beslutningspost for alexandrinsk mønster](skabeloner/skabelon-til-beslutningspost-for-alexandrinsk-moenster/)
- [Skabelon til beslutningspost for businesscase](skabeloner/skabelon-til-beslutningspost-for-businesscase/)
- [Skabelon til beslutningspost fra MADR-projektet](skabeloner/skabelon-til-beslutningspost-fra-madr-projektet/)
- [Skabelon til beslutningspost med Planguage](skabeloner/skabelon-til-beslutningspost-med-planguage/)
- [Skabelon til beslutningspost af Paulo Merson](https://github.com/pmerson/ADR-template)
- [Skabelon til beslutningspost af Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Skabelon til beslutningspost fra Gareth Morgan](skabeloner/skabelon-til-beslutningspost-fra-gareth-morgan/)
- [Skabelon til beslutningspost fra GIG Cymru NHS Wales](skabeloner/skabelon-til-beslutningspost-fra-gig-cymru-nhs-wales/)
- [Skabelon til beslutningspost for vigtige tekniske beslutninger af Ignacio Larrañaga](skabeloner/skabelon-til-beslutningspost-for-vigtige-tekniske-beslutninger/)

Eksempler:

- [CSS-framework](eksempler/css-framework/)
- [Konfiguration med miljøvariabler](eksempler/konfiguration-med-miljovariabler/)
- [Metrikker, overvågning, alarmer](eksempler/metrikker-overvaagning-alarmer/)
- [Microsoft Azure DevOps](eksempler/microsoft-azure-devops/)
- [Monorepo eller multirepo](eksempler/monorepo-eller-multirepo/)
- [Programmeringssprog](eksempler/programmeringssprog/)
- [Opbevaring af hemmeligheder](eksempler/opbevaring-af-hemmeligheder/)
- [Tidsstempelformat](eksempler/tidsstempelformat/)
- [Mange flere...](eksempler/)

## Hvad er en arkitekturbeslutningspost?

En **arkitekturbeslutningspost** (ADR) er et dokument, der registrerer en vigtig arkitekturbeslutning, der er truffet, sammen med dens kontekst og konsekvenser.

En **arkitekturbeslutning** (AD) er et softwaredesignvalg, der adresserer et væsentligt krav.

En **arkitekturbeslutningslog** (ADL) er samlingen af alle ADR'er, der er oprettet og vedligeholdt for et bestemt projekt (eller en bestemt organisation).

Et **arkitektonisk væsentligt krav** (ASR) er et krav, der har en målbar effekt på arkitekturen i et softwaresystem.

Alt dette hører under emnet **arkitekturvidensstyring** (AKM).

Formålet med dette dokument er at give et hurtigt overblik over ADR'er, hvordan man skriver dem, og hvor man finder flere oplysninger.

Forkortelser:

  * **AD**: arkitekturbeslutning

  * **ADL**: arkitekturbeslutningslog

  * **ADR**: arkitekturbeslutningspost

  * **AKM**: arkitekturvidensstyring

  * **ASR**: arkitektonisk væsentligt krav

## Sådan kommer du i gang med ADR'er

For at komme i gang med ADR'er kan du tale med dine teamkolleger om følgende områder.

Identificering af beslutninger:

  * Hvor presserende og hvor vigtig er AD'en?

  * Skal beslutningen træffes nu, eller kan den vente, til mere er kendt?

  * Personlig og kollektiv erfaring samt anerkendte designmetoder og -praksisser kan hjælpe med at identificere beslutninger.

  * Hold ideelt set en beslutningsbacklog, der supplerer produktbackloggen.

Beslutningstagning:

  * Der findes flere teknikker til beslutningstagning, både generelle teknikker og teknikker, der er specifikke for softwarearkitektur. Et eksempel er dialogkortlægning.

  * Gruppebeslutningstagning er et aktivt forskningsemne.

Håndhævelse og gennemførelse af beslutninger:

  * Da AD'er bruges i softwaredesign, skal de kommunikeres til og accepteres af de interessenter, der finansierer, udvikler og driver systemet.

  * Arkitekturbevidste kodestile og kodegennemgange med fokus på arkitekturrelaterede forhold og beslutninger er to beslægtede praksisser.

  * AD'er bør også (gen)overvejes, når et softwaresystem moderniseres under softwareudviklingens forløb.

Deling af beslutninger (valgfrit):

  * Mange AD'er gentages på tværs af projekter.

  * Derfor kan erfaring med tidligere beslutninger, både gode og dårlige, være et værdifuldt genanvendeligt aktiv, når man bruger en eksplicit strategi for videnstyring.

Dokumentation af beslutninger:

  * Der findes mange skabeloner og værktøjer til at registrere beslutninger.

  * Se det agile miljø, for eksempel M. Nygards ADR'er.

  * Se traditionelle softwareudviklings- og arkitekturdesignprocesser, for eksempel IBM UMF og tabellayoutet foreslået af Tyree og Akerman fra CapitalOne.

Læs mere:

  * Ovenstående trin er hentet fra Wikipedia-artiklen [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Sådan kommer du i gang med ADR'er med værktøjer

- [MySpec](https://myspec.dev) — Automatiseret specifikations- og arkitekturbeslutningsplatform, der strukturerer projektets forfatning, teknisk arkitektur og ADR'er i ren Markdown leveret via MCP.

Du kan selv vælge, hvordan du kommer i gang med ADR'er med værktøjer.

For eksempel:

  * Hvis du kan lide Google Drev og onlineredigering, kan du oprette et Google-dokument eller et Google-regneark.

  * Hvis du kan lide kildekodeversionsstyring som git, kan du oprette en fil for hver ADR.

  * Hvis du kan lide projektplanlægningsværktøjer som Atlassian Jira, kan du bruge deres planlægningstracker.

  * Hvis du kan lide wikier som MediaWiki, kan du oprette en ADR-wiki.

## Sådan kommer du i gang med ADR'er med git

Hvis du kan lide git-versionsstyring, er her, hvordan vi kommer i gang med ADR'er med git i et typisk softwareprojekt med kildekode.

Opret en mappe til dine ADR-filer:

```sh
$ mkdir adr
```

Opret en tekstfil for hver ADR, for eksempel `database.txt`:

```sh
$ vi database.txt
```

Skriv hvad du vil i ADR'en. For idéer kan du se skabelonerne i dette repository.

Commit ADR'erne til dit git-repository.

## Claude Code-færdigheder til ADR'er

Dette lager indeholder to [Claude Code](https://claude.com/claude-code)-færdigheder (skills) under [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), så en AI-kodeagent kan skrive og vedligeholde ADR'er på den måde, dette projekt anbefaler:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — til generelt brug, for alle der skriver en ADR i et hvilket som helst projekt. Hjælper med at afgøre, om en beslutning kræver en ADR, opretter en `adr/`- eller `decisions/`-mappe, navngiver filen, vælger en skabelon blandt de elleve medfølgende skelet og skriver solide afsnit om sammenhæng/beslutning/konsekvenser.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — specifikt til vedligeholdere af dette lager. Dokumenterer lagerets opbygning, konventionen om at spejle README/locales og de præcise trin til at tilføje en ny skabelon, et nyt eksempel eller et nyt værktøjslink.

For at bruge en færdighed skal du kopiere dens mappe til `.claude/skills/` i roden af det lager, du arbejder i (eller til `~/.claude/skills/` for at gøre den tilgængelig i alle projekter) og derefter bede Claude Code om at skrive eller gennemgå en ADR.

## Konventioner for filnavne

Hvis du vælger at skrive ADR'er som almindelige tekstfiler, kan det være nyttigt at fastlægge din egen konvention for ADR-filnavne.

Vi foretrækker en konvention for filnavne med et bestemt format.

Eksempler:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Vores konvention for filnavne:

  * Navnet er en bydemåde i nutid. Det forbedrer læsbarheden og passer til vores format for commit-beskeder.

  * Navnet bruger små bogstaver og bindestreger (ligesom i dette repository). Det er en balance mellem læsbarhed og brugbarhed på tværs af systemer.

  * Filendelsen er markdown. Det kan være praktisk til enkel formatering.

## Forslag til at skrive gode ADR'er

Kendetegn ved en god ADR:

* Begrundelse: forklar, hvorfor AD'en udføres. Det kan omfatte kontekst (se nedenfor), fordele og ulemper ved forskellige mulige valg, funktionssammenligninger, cost-benefit-diskussioner og så videre.

* Specifik: hver ADR bør handle om én AD, ikke flere AD'er.

* Tidsstemplet: angiv, hvornår hvert element i ADR'en blev skrevet. Det er især vigtigt for aspekter, der kan ændre sig over tid, såsom omkostninger, tidsplan, udvidelse og så videre.

* Uforanderlig: ændr ikke eksisterende oplysninger i en ADR. Ændr i stedet ADR'en ved at tilføje nye oplysninger, eller erstat ADR'en ved at oprette en ny ADR.

Kendetegn ved et godt afsnit om "Kontekst" i en ADR:

* Beskriver organisationens situation og forretningsmæssige prioriteter.

* Indeholder begrundelsen og overvejelserne baseret på teamets sociale og tekniske sammensætning.

* Indeholder relevante afvejninger, udtrykt i termer der passer til behov og mål.

Kendetegn ved et godt afsnit om "Konsekvenser" i en ADR:

* Beskriver, hvad der følger af at træffe beslutningen. Det kan omfatte effekter, resultater, leverancer, opfølgende handlinger og så videre.

* Indeholder oplysninger om opfølgende ADR'er. Det er relativt almindeligt, at én ADR udløser behovet for flere ADR'er. For eksempel kan en ADR, der træffer et stort, overordnet valg, udløse behov for mindre beslutninger.

* Indeholder en efterbehandlingsproces. Det er almindeligt, at teams gennemgår hver ADR efter en måned, sammenligner ADR-oplysningerne med det, der rent faktisk skete, og lærer og vokser heraf.

En ny ADR kan erstatte en tidligere ADR:

* Når der træffes en AD, der erstatter eller ugyldiggør en tidligere ADR, bør der skrives en ny ADR

## ADR-eksempelskabeloner

ADR-eksempelskabeloner, som vi har samlet fra nettet:

- [ADR-skabelon af Michael Nygard](skabeloner/skabelon-til-beslutningspost-fra-michael-nygard/) (enkel og populær)

- [ADR-skabelon af Jeff Tyree og Art Akerman](skabeloner/skabelon-til-beslutningspost-fra-jeff-tyree-og-art-akerman/) (mere sofistikeret)

- [ADR-skabelon til Alexandrian-mønster](skabeloner/skabelon-til-beslutningspost-for-alexandrinsk-moenster/) (enkel med detaljer om sammenhængen)

- [ADR-skabelon til business case](skabeloner/skabelon-til-beslutningspost-for-businesscase/) (mere MBA-orienteret, med omkostninger, SWOT og flere holdninger)

- [ADR-skabelon fra projektet Markdown Any Decision Records (MADR)](skabeloner/skabelon-til-beslutningspost-fra-madr-projektet/) (både en enkel og en udførlig version; den sidste fremhæver muligheder og deres fordele og ulemper)

- [ADR-skabelon med Planguage](skabeloner/skabelon-til-beslutningspost-med-planguage/) (mere kvalitetssikringsorienteret)

- [Skabelon til Important Technical Decisions (ITD'er) af Ignacio Larrañaga](skabeloner/skabelon-til-beslutningspost-for-vigtige-tekniske-beslutninger/) (slank og beslutningen først, optimeret til hurtig ledelsesgennemgang)

## Teamarbejdsråd til ADR'er

Hvis du overvejer at bruge beslutningsposter i dit team, er her nogle råd, vi har lært ved at arbejde med flere teams.

Der er mulighed for at lede teammedlemmer ved at tale om "hvorfor" frem for at gennemtvinge "hvad". Beslutningsposter er for eksempel en måde for teams at tænke klogere og kommunikere bedre. Hvis beslutningsposter blot er et papirarbejdskrav, der gennemtvinges bagefter, har de ingen værdi.

Nogle teams foretrækker i høj grad navnet "beslutninger" frem for forkortelsen "ADR". Når nogle teams bruger "decisions" som mappenavn, går der et lys op, og teams begynder at lægge flere oplysninger i mappen, såsom leverandørbeslutninger, planbeslutninger, tidsplanbeslutninger og så videre. Du kan bruge den samme skabelon til alle disse slags oplysninger. Vi antager, at folk lærer hurtigere med ordet ("beslutning") end med forkortelsen ("ADR"), at udeladelsen af ordet "post" giver mere motivation til at skrive igangværende arbejde, og at nogle udviklere og nogle ledere ikke bryder sig om ordet "arkitektur".

I teorien er uforanderlighed ideel. I praksis fungerede foranderlighed bedre for vores team. Vi indsætter nye oplysninger i en eksisterende ADR med et datostempel og en note om, at oplysningerne kom ind efter beslutningen. Denne tilgang fører til et "levende dokument", som vi alle kan opdatere. Typiske opdateringer kommer fra at få oplysninger takket være nye teammedlemmer, nye tilbud, faktiske resultater af vores brug eller efter efterfølgende ændringer fra tredjepart såsom leverandørers funktioner, prisplaner og licensaftaler.

## Teamwork-spørgsmål til ADR'er

### Hvem kan skrive ADR'er?

Overvej områder som bestemte personer, bestemte roller, bestemte teams, bestemte afdelinger. Overvej også, om der er personer, roller, teams eller afdelinger, der kan bestille ADR'er, dvs. kan anmode om, at en anden skriver en ADR. 

Eksempel på svar: enhver i vores organisation, der har læst README-siden om arkitekturbeslutningsposter, kan foreslå en ADR, dvs. begynde at skrive og dele den med teamet.

### Hvad retfærdiggør at rejse en ADR?

Overvej områder som hvordan teams i organisationen arbejder, softwaresystemers struktur, koordinering mellem teams, langsigtet vedligeholdelighed, eksterne grænseflader og hvem du vil have til at drage fordel. 

Eksempel på svar: vi vil gerne skrive en ADR, når vi ønsker, at fremtidige udviklere skal forstå "hvorfor" bag det, vi gør.

### Hvad retfærdiggør ikke at rejse en ADR?

Overvej områder som beslutninger, der ikke handler om arkitektur, beslutninger, der er trivielle, fordi de har minimal risiko, er selvstændige eller begrænset til én udvikler, beslutninger, der allerede er fuldt dækket andetsteds i standarder, politikker, dokumentation og så videre, eller beslutninger, der er midlertidige, såsom nødløsninger, proofs of concept og eksperimenter. 

Eksempel på svar: vi vil gerne springe en ADR over, når beslutningen er begrænset i omfang, tid, risiko og omkostninger eller allerede er dækket andetsteds.

### Hvad er en ADR's livscyklus?

Overvej områder som skriveprocessen, undersøgelsesprocessen, beslutningsprocessen, implementeringsprocessen og udfasningsprocessen. Overvej, hvordan du sporer ADR'ens livscyklus over tid, for eksempel hvordan du flytter en ADR fra én status til den næste, og hvordan du kommunikerer det til interessenter. 

Eksempel på svar: vi vil gerne have, at ADR'er har fem livscyklusfaser: Initiating → Researching → Evaluating → Implementing → Maintaining → Sunsetting.

### Hvad er kriterierne for en ADR's livscyklusfaser?

Overvej områder som acceptkriterier for ADR'er, dvs. hvordan ved vi, at en ADR er god nok til at gå fra én livscyklusfase til den næste? Er problemet klart beskrevet? Er alternativer overvejet? Er afvejningerne godt forstået og dokumenteret?
Er al relevant kontekst til stede? Er alle relevante interessenter involveret? Er al feedback blevet indarbejdet? 

Eksempel på svar: vi vil gerne have, at det aktive team 1) afslutter undersøgelsen, 2) afslutter evalueringen, 3) offentliggør ADR-forslagene for interessenter med en anmodning om kommentarer og en tidsfrist på en uge, og 4) når alle interessentkommentarer er indarbejdet og behandlet, lader interessenterne stemme om ADR'en.

### Hvilke roller og ansvarsområder samspiller med ADR'er?

Overvej roller som indsender, undersøger, evaluator, gennemgående, godkender og vedligeholder. Overvej ansvarsområder som at kommunikere med interessenter, sikre at forventninger indfris, dele på webstedet eller intranettet og periodisk gennemgå arbejdet, især når der er relevante ændringer.

Eksempel på svar: vi vil gerne have, at hver ADR altid har en primær ejer, en sekundær ejer og et ansvarligt team. De er ansvarlige for kommunikation, offentliggørelse, vedligeholdelse, periodisk gennemgang mindst årligt og endelig udfasning efter behov.

### Hvordan samspiller governance med ADR'er?

Overvej områder som hvordan organisationen arbejder, særlige compliancebehov såsom juridiske aspekter eller HR-aspekter, og hvordan du vil håndtere konsensus versus konflikt versus eskalering. Er der områder, personer eller teams, der kan have mere indflydelse end andre, såsom magten til at godkende, stemme eller nedlægge veto i forbindelse med ADR'er?

Eksempel på svar: governance for en ADR følger denne prioritetsrækkefølge: CEO, CTO, CLO, teamet der implementerer ADR'en, den mest vidende ekspert i teamet om ADD'en. Ingen har governance, medmindre det er beskrevet i ADR'en. 

### Hvilke principper samspiller med ADR'er?

Overvej områder, der involverer, hvordan organisationen arbejder, såsom at bevæge sig hurtigt eller langsomt, beslutningskonsensus versus beslutningskonflikt, risikopræference versus sikkerhedspræference og offentlig diskussion versus privat diskussion.

Eksempel på svar: vi bruger lederskabsprincipperne handlingsorientering (bias for action), uenighed og forpligtelse (disagree-and-commit), 70 % af oplysningerne er nok til beslutninger, der er lette at gøre om og lette at isolere, og åbent arbejde bortset fra fortrolige oplysninger som beskrevet i vores organisations fortrolighedsaftaler.

## Næste-skridt-begreber til ADR'er

[Arc42](https://arc42.org/) besvarer to spørgsmål pragmatisk og kan tilpasses dine konkrete behov. Hvad bør du dokumentere/kommunikere om din arkitektur? Hvordan bør du dokumentere/kommunikere? Arc42 omfatter arkitekturbeslutningsposter samt vejledning om mål, begrænsninger, kontekster, kvalitet, risici med mere.

[C4-modellen](https://c4model.com/) er en let at lære, udviklervenlig tilgang til at tegne softwarearkitekturdiagrammer. C4 er et sæt hierarkiske diagrammer for kontekst, containere, komponenter og kode samt understøttende diagrammer for systemlandskab, dynamik og udrulning.

## Arkitekturdiagrammer, visninger og synsvinkler

Et arkitekturdiagram kaldes en "arkitekturvisning".

En "arkitekturvisning" er en forekomst af et "arkitektursynspunkt".

Et "arkitektursynspunkt" har en bestemt målgruppe med bestemte bekymringer for øje.

Eksempler på arkitektursynspunkter, visninger og diagrammer:

- Forretningsevner

- Forretningsprocesser på højt niveau

- [Værdistrømme](https://en.wikipedia.org/wiki/Value_stream)

- Softwarefunktioner knyttet til applikationskomponenter

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Kontekstdiagram (TO-BE / AS-IS)

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Containerdiagram (TO-BE / AS-IS)

- [Entitet-relation-diagram](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) til at knytte dataentiteter til applikationskomponenter

- [Sekvensdiagrammer](https://en.wikipedia.org/wiki/Sequence_diagram) til at beskrive funktionelle flows i systemer og ved integrationer

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagrammer til at beskrive dataflow på tværs af applikationskomponenter

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagrammer til at beskrive forretningsprocesser / brugerscenarier

- [Identity and Access Management](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) diagrammer

- [Rollebaseret adgangskontrol](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) diagrammer med roller pr. applikationskomponent

- [Attributbaseret adgangskontrol](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) diagrammer med attributter pr. applikationskomponent

- Privatlivsdiagrammer

Relaterede diagrammer:

- Et use case-diagram viser use cases for ledelsen/kunderne, hvilket går forud for kravene, som går forud for softwarearkitekturen.

- Et udrulningsdiagram viser den fysiske hardware/de fysiske computere, som softwarekomponenterne udrulles til.
- Et dataflowdiagram viser, hvordan data bevæger sig gennem systemet og transformeres.
- Et sekvensdiagram bruges til at vise, hvordan protokoller som HTTP fungerer på en tidsakse.

- Et aktivitetsdiagram afbilder arbejdsgangen for de aktiviteter, et softwaresystem udfører, som en NPC-AI.

## Fitnessfunktioner for beslutninger som kode

En fitnessfunktion er en objektiv, automatiseret kontrol, skrevet som programkode, der verificerer, at en beslutning overholdes.

- Fitnessfunktioner gør beslutninger testbare og kontrollerbare.

- Fitnessfunktioner for beslutninger kan være en stor hjælp til kvalitetssikring, regulatoriske processer og governance-mål.

### Sådan hænger fitnessfunktioner og beslutninger sammen

En beslutningspost dokumenterer en beslutning; en fitnessfunktion håndhæver den beslutning.

- Eksempel på beslutning: brug event sourcing til revisionskrav.

- Eksempel på fitnessfunktion: brug en kontinuerlig integrationsserver til at teste, at enhver tilstandsændring skal generere en hændelse.

### Hvorfor fitnessfunktioner hjælper beslutninger

Objektiv måling: en fitnessfunktion består eller fejler, så arbejdet er synligt og tydeligt.

Løbende brug: en fitnessfunktion er en levende regel og kører ved hver commit og build.

Tillid ved refaktorering: en fitnessfunktion fanger automatisk fejl i forhold til beslutningsreglerne.

Skalerbar governance: en fitnessfunktion håndhæver standarder uden at skabe flaskehalse.

### Kan fitnessfunktioner bruge AI?

En fitnessfunktion kan bruge en AI-LLM til beslutninger ved at stille spørgsmål
om vores arbejde, såsom planer, kode, skemaer, API'er og så videre:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Arkitekturenhedstests

[ArchUnit](https://www.archunit.org/): kontrollér arkitekturregler for Java-kode med et almindeligt Java-enhedstestframework.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): kontrollér arkitekturregler for TypeScript-kode og JavaScript-kode med Jest, Vitest, Jasmine og andre.

## Beslutningsautoværn til pull requests

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
fremhæver automatisk de rette beslutningsposter på det rette tidspunkt, nemlig når en
udvikler aktivt ændrer den kode, som disse beslutninger dækker. I stedet for at håbe på, at udviklere
læser en dokumentmappe før en sammenfletning, vises den relevante sammenhæng direkte på pull requesten.

Det fungerer for alle slags beslutningsposter: arkitekturbeslutninger, databeslutninger, compliancebeslutninger, kliniske og medicinske beslutninger, sikkerhedsbeslutninger og flere.

Fungerer med ethvert CI-system (GitLab, Jenkins, CircleCI) og som en pre-commit-hook.
Open source. MIT-licens.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) er en GitHub
Action, der afviser en pull request, når overvågede kodestier ændres uden at en
arkitekturbeslutningspost tilføjes eller opdateres. Undtagelser er eksplicitte: en
`ADR-Exempt:`-linje med en begrundelse lader porten passere og skrives i jobbets
opsummering. Skabelonuafhængig, ingen afhængigheder. Open source. MIT-licens.

## Mere information

Introduktion:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Skabeloner:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Dybdegående:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - gratis månedlig lektion i softwarearkitektur

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Værktøjer:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Virksomhedsspecifik vejledning:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Eksempler:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Videoer:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcasts:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Bøger:

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

Se også:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Et leverandørneutralt, maskinlæsbart YAML/JSON-format til at repræsentere beslutninger med eksplicit ræsonnement, antagelser, kognitiv tilstand og afvejninger. Supplerer ADR'er ved at tilføje struktureret, validerbart ræsonnement til beslutningsdokumentation.
