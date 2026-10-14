# Arkitekturbeslutspost (ADR)

En arkitekturbeslutspost (ADR) är ett dokument som fångar ett viktigt arkitekturbeslut tillsammans med dess sammanhang och konsekvenser.

> [!IMPORTANT]
> Gör din egen noggranna granskning av dessa resurser innan du använder dem i några kritiska system.

Innehåll:

- [Vad är en arkitekturbeslutspost?](#vad-är-en-arkitekturbeslutspost)
- [Så kommer du igång med ADR:er](#så-kommer-du-igång-med-adrer)
- [Så kommer du igång med ADR:er och verktyg](#så-kommer-du-igång-med-adrer-och-verktyg)
- [Så kommer du igång med ADR:er och git](#så-kommer-du-igång-med-adrer-och-git)
- [Claude Code-färdigheter för ADR:er](#claude-code-färdigheter-för-adrer)
- [Filnamnskonventioner](#filnamnskonventioner)
- [Tips för att skriva bra ADR:er](#tips-för-att-skriva-bra-adrer)
- [ADR-exempelmallar](#adr-exempelmallar)
- [Råd om teamarbete för ADR:er](#råd-om-teamarbete-för-adrer)
- [Teamarbetsfrågor för ADR:er](#teamarbetsfrågor-för-adrer)
- [Nästa-steg-koncept för ADR:er](#nästa-steg-koncept-för-adrer)
- [Arkitekturdiagram, vyer och synvinklar](#arkitekturdiagram-vyer-och-synvinklar)
- [Lämplighetsfunktioner för beslut som kod](#lämplighetsfunktioner-för-beslut-som-kod)
- [Beslutsräcken för pull requests](#beslutsräcken-för-pull-requests)
- [Mer information](#mer-information)

Mallar:

- [Mall för beslutspost från Jeff Tyree och Art Akerman](mallar/mall-för-beslutspost-från-jeff-tyree-och-art-akerman/)
- [Mall för beslutspost från Michael Nygard](mallar/mall-för-beslutspost-från-michael-nygard/)
- [Mall för beslutspost från EdgeX](mallar/mall-för-beslutspost-från-edgex/)
- [Mall för beslutspost från arc42](mallar/mall-för-beslutspost-från-arc42/)
- [Mall för beslutspost för alexandriskt mönster](mallar/mall-för-beslutspost-för-alexandriskt-mönster/)
- [Mall för beslutspost för affärscase](mallar/mall-för-beslutspost-för-affärscase/)
- [Mall för beslutspost från MADR-projektet](mallar/mall-för-beslutspost-från-madr-projektet/)
- [Mall för beslutspost med Planguage](mallar/mall-för-beslutspost-med-planguage/)
- [Mall för beslutspost av Paulo Merson](https://github.com/pmerson/ADR-template)
- [Mall för beslutspost av Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Mall för beslutspost från Gareth Morgan](mallar/mall-för-beslutspost-från-gareth-morgan/)
- [Mall för beslutspost från GIG Cymru NHS Wales](mallar/mall-för-beslutspost-från-gig-cymru-nhs-wales/)
- [Mall för beslutspost för Viktiga Tekniska Beslut (ITD) av Ignacio Larrañaga](mallar/mall-för-beslutspost-för-viktiga-tekniska-beslut/)

Exempel:

- [CSS-ramverk](exempel/css-ramverk/)
- [Konfiguration med miljövariabler](exempel/konfiguration-med-miljövariabler/)
- [Mätvärden, övervakning, larm](exempel/mätvärden-övervakning-larm/)
- [Microsoft Azure DevOps](exempel/microsoft-azure-devops/)
- [Monorepo eller multirepo](exempel/monorepo-eller-multirepo/)
- [Programmeringsspråk](exempel/programmeringsspråk/)
- [Lagring av hemligheter](exempel/lagring-av-hemligheter/)
- [Tidsstämpelformat](exempel/tidsstämpelformat/)
- [Många fler...](exempel/)

## Vad är en arkitekturbeslutspost?

En **arkitekturbeslutspost** (architecture decision record, ADR) är ett dokument som fångar ett viktigt arkitekturbeslut som fattats tillsammans med dess sammanhang och konsekvenser.

Ett **arkitekturbeslut** (architecture decision, AD) är ett programvarudesignval som adresserar ett betydande krav.

En **arkitekturbeslutslogg** (architecture decision log, ADL) är samlingen av alla ADR:er som skapats och underhålls för ett visst projekt (eller en organisation).

Ett **arkitektoniskt betydelsefullt krav** (architecturally-significant requirement, ASR) är ett krav som har en mätbar effekt på ett programvarusystems arkitektur.

Allt detta ryms inom ämnet **arkitekturkunskapshantering** (architecture knowledge management, AKM).

Målet med det här dokumentet är att ge en snabb översikt över ADR:er, hur man skapar dem och var man hittar mer information.

Förkortningar:

  * **AD**: arkitekturbeslut

  * **ADL**: arkitekturbeslutslogg

  * **ADR**: arkitekturbeslutspost

  * **AKM**: arkitekturkunskapshantering

  * **ASR**: arkitektoniskt betydelsefullt krav

## Så kommer du igång med ADR:er

För att komma igång med ADR:er, prata med dina teamkamrater om följande områden.

Identifiering av beslut:

  * Hur brådskande och hur viktigt är AD:t?

  * Måste det fattas nu, eller kan det vänta tills mer är känt?

  * Både personlig och kollektiv erfarenhet, samt erkända designmetoder och praxis, kan hjälpa till vid identifiering av beslut.

  * Underhåll helst en att-göra-lista för beslut som kompletterar produktens att-göra-lista.

Beslutsfattande:

  * Det finns ett antal beslutstekniker, både generella och sådana som är specifika för programvaruarkitektur, till exempel dialogue mapping.

  * Gruppbeslut är ett aktivt forskningsämne.

Genomförande och upprätthållande av beslut:

  * AD:n används i programvarudesign; därför måste de kommuniceras till, och accepteras av, systemets intressenter som finansierar, utvecklar och driver det.

  * Arkitektoniskt tydliga kodstilar och kodgranskningar som fokuserar på arkitektoniska frågor och beslut är två relaterade metoder.

  * AD:n måste också (om)prövas när ett programvarusystem moderniseras i programvaruevolutionen.

Delning av beslut (valfritt):

  * Många AD:n återkommer i olika projekt.

  * Därför kan erfarenheter av tidigare beslut, både goda och dåliga, vara värdefulla återanvändbara tillgångar när man använder en explicit kunskapshanteringsstrategi.

Dokumentation av beslut:

  * Det finns många mallar och verktyg för att fånga beslut.

  * Se agila gemenskaper, till exempel M. Nygards ADR:er.

  * Se traditionella programvaruutvecklings- och arkitekturdesignprocesser, till exempel de tabelllayouter som föreslagits av IBM UMF och av Tyree och Akerman på CapitalOne.

För mer:

  * Stegen ovan är hämtade från Wikipedia-artikeln om [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Så kommer du igång med ADR:er och verktyg

- [MySpec](https://myspec.dev) — Automatiserad plattform för specifikationer och arkitekturbeslut som strukturerar projektets konstitution, teknisk arkitektur och ADR:er i ren Markdown som levereras via MCP.

Du kan börja använda ADR:er med verktyg på vilket sätt du vill.

Till exempel:

  * Om du gillar att använda Google Drive och redigering online kan du skapa ett Google-dokument eller ett Google-kalkylblad.

  * Om du gillar versionshantering av källkod, till exempel git, kan du skapa en fil för varje ADR.

  * Om du gillar att använda projektplaneringsverktyg, till exempel Atlassian Jira, kan du använda verktygets planeringshanterare.

  * Om du gillar wikis, till exempel MediaWiki, kan du skapa en ADR-wiki.

## Så kommer du igång med ADR:er och git

Om du gillar versionshantering med git, så här börjar vi gärna använda ADR:er med git för ett typiskt programvaruprojekt med källkod.

Skapa en katalog för ADR-filer:

```sh
$ mkdir adr
```

Skapa en textfil för varje ADR, till exempel `database.txt`:

```sh
$ vi database.txt
```

Skriv vad du vill i ADR:en. Se mallarna i det här repot för idéer.

Checka in ADR:en i ditt git-repo.

## Claude Code-färdigheter för ADR:er

Det här arkivet innehåller två [Claude Code](https://claude.com/claude-code)-färdigheter (skills) under [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), så att en AI-kodningsagent kan skriva och underhålla ADR:er på det sätt som det här projektet rekommenderar:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — för allmänt bruk, för alla som skriver en ADR i vilket projekt som helst. Hjälper till att avgöra om ett beslut behöver en ADR, skapar en katalog `adr/` eller `decisions/`, namnger filen, väljer en mall bland de elva medföljande skeletten och skriver solida avsnitt om sammanhang, beslut och konsekvenser.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — särskilt för dem som underhåller det här arkivet. Dokumenterar arkivets uppbyggnad, konventionen att spegla README och locales och de exakta stegen för att lägga till en ny mall, ett nytt exempel eller en ny verktygslänk.

För att använda en färdighet kopierar du dess mapp till `.claude/skills/` i roten av det arkiv du arbetar i (eller till `~/.claude/skills/` för att göra den tillgänglig i alla projekt) och ber sedan Claude Code skriva eller granska en ADR.

## Filnamnskonventioner

Om du väljer att skapa dina ADR:er med vanliga textfiler kanske du vill ta fram en egen filnamnskonvention för ADR-filer.

Vi föredrar att använda en filnamnskonvention med ett specifikt format.

Exempel:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Vår filnamnskonvention:

  * Namnet har en verbfras i imperativ presens. Det underlättar läsbarheten och matchar vårt format för commit-meddelanden.

  * Namnet använder gemener och bindestreck (samma som detta repo). Det är en balans mellan läsbarhet och systemets användbarhet.

  * Filändelsen är markdown. Det kan vara användbart för enkel formatering.

## Tips för att skriva bra ADR:er

Kännetecken för en bra ADR:

* Motivering: Förklara skälen till att fatta det specifika AD:t. Det kan omfatta sammanhanget (se nedan), för- och nackdelar med olika möjliga val, funktionsjämförelser, diskussioner om kostnad/nytta och mer.

* Specifik: Varje ADR bör handla om ett AD, inte flera AD:n.

* Tidsstämplar: Ange när varje punkt i ADR:en skrevs. Detta är särskilt viktigt för aspekter som kan förändras över tid, såsom kostnader, scheman, skalning och liknande.

* Oföränderlig: Ändra inte befintlig information i en ADR. Komplettera i stället ADR:en genom att lägga till ny information, eller ersätt ADR:en genom att skapa en ny ADR.

Kännetecken för ett bra avsnitt ”Sammanhang” i en ADR:

* Förklara din organisations situation och affärsprioriteringar.

* Ta med motiveringar och överväganden som bygger på dina teams sociala sammansättning och kompetenser.

* Ta med relevanta för- och nackdelar och beskriv dem i termer som stämmer överens med dina behov och mål.

Kännetecken för ett bra avsnitt ”Konsekvenser” i en ADR:

* Förklara vad som följer av beslutet. Det kan omfatta effekter, utfall, resultat, uppföljning och mer.

* Ta med information om eventuella efterföljande ADR:er. Det är relativt vanligt att en ADR utlöser behov av fler ADR:er, till exempel när en ADR gör ett stort övergripande val som i sin tur skapar behov av fler mindre beslut.

* Ta med eventuella processer för efterhandsutvärdering. Det är vanligt att team granskar varje ADR en månad senare för att jämföra ADR-informationen med vad som hänt i praktiken, för att lära och växa.

En ny ADR kan ersätta en tidigare ADR:

* När ett AD fattas som ersätter eller upphäver en tidigare ADR bör en ny ADR skapas

## ADR-exempelmallar

ADR-exempelmallar som vi har samlat in på nätet:

- [ADR-mall av Michael Nygard](mallar/mall-för-beslutspost-från-michael-nygard/) (enkel och populär)

- [ADR-mall av Jeff Tyree och Art Akerman](mallar/mall-för-beslutspost-från-jeff-tyree-och-art-akerman/) (mer sofistikerad)

- [ADR-mall för Alexandrian-mönstret](mallar/mall-för-beslutspost-för-alexandriskt-mönster/) (enkel, med detaljer om sammanhanget)

- [ADR-mall för business case](mallar/mall-för-beslutspost-för-affärscase/) (mer MBA-inriktad, med kostnader, SWOT och fler åsikter)

- [ADR-mall från projektet Markdown Any Decision Records (MADR)](mallar/mall-för-beslutspost-från-madr-projektet/) (både enkel och utförlig version; den senare betonar alternativ och deras för- och nackdelar)

- [ADR-mall som använder Planguage](mallar/mall-för-beslutspost-med-planguage/) (mer kvalitetssäkringsinriktad)

- [Mall för Important Technical Decisions (ITD:er) av Ignacio Larrañaga](mallar/mall-för-beslutspost-för-viktiga-tekniska-beslut/) (slimmad och beslutet först, optimerad för snabb granskning av ledningen)

## Råd om teamarbete för ADR:er

Om du överväger att använda beslutsposter i ditt team finns här några råd som vi har lärt oss genom att arbeta med många team.

Du har en möjlighet att leda dina teamkamrater genom att tillsammans prata om ”varför”, i stället för att kräva ”vad”. Beslutsposter är till exempel ett sätt för team att tänka smartare och kommunicera bättre; beslutsposter är inte värdefulla om de bara är ett påtvingat pappersarbete i efterhand.

Vissa team föredrar namnet ”beslut” (decisions) långt före förkortningen ”ADR:er”. När vissa team använder katalognamnet ”decisions” är det som om en glödlampa tänds, och teamet börjar lägga mer information i katalogen, till exempel leverantörsbeslut, planeringsbeslut, schemaläggningsbeslut och så vidare. Alla dessa typer av information kan använda samma mall. Vi antar att människor lär sig snabbare med ord (”beslut”) än med förkortningar (”ADR:er”), och att människor är mer motiverade att skriva dokument för pågående arbete när ordet ”post” (record) tas bort, och dessutom att vissa utvecklare och vissa chefer ogillar ordet ”arkitektur”.

I teorin är oföränderlighet idealiskt. I praktiken har föränderlighet fungerat bättre för våra team. Vi infogar den nya informationen i den befintliga ADR:en, med en datumstämpel och en anteckning om att informationen kom efter beslutet. Ett sådant tillvägagångssätt leder till ett ”levande dokument” som vi alla kan uppdatera. Typiska uppdateringar sker när vi får information tack vare nya teamkamrater, eller nya erbjudanden, eller verkliga resultat av vår användning, eller efterhandsändringar från tredje part, såsom leverantörers kapacitet, prisplaner, licensavtal och så vidare.

## Teamarbetsfrågor för ADR:er

### Vem kan skapa en ADR?

Tänk på områden som specifika personer, specifika roller, specifika team eller specifika avdelningar; överväg också om det finns personer, roller, team eller avdelningar som kan beställa en ADR, det vill säga begära en som någon annan kommer att skriva. 

Exempelsvar: Vem som helst i vår organisation som har läst README-sidan om arkitekturbeslutsposter kan föreslå en ADR, vilket innebär att personen kan börja skriva den och dela den med teamet.

### Vad motiverar att man tar upp en ADR?

Tänk på områden som din organisations teams arbetssätt, ditt programvarusystems struktur, samordning mellan team, långsiktig underhållbarhet, externa gränssnitt, vem du vill ska dra nytta, och liknande. 

Exempelsvar: Vi vill skapa en ADR när vi vill att framtida utvecklare ska förstå ”varför” bakom det vi gör.

### Vad motiverar att man inte tar upp en ADR?

Tänk på områden som beslut som inte handlar om arkitektur, eller är små, till exempel minimal risk eller fristående eller för en enda utvecklare, eller redan helt täcks någon annanstans, till exempel av standarder, policyer eller dokumentation, eller är tillfälliga, till exempel tillfälliga lösningar, koncepttest eller experiment. 

Exempelsvar: Vi vill hoppa över en ADR när ett beslut är begränsat i omfattning, tid, risk och kostnad, eller redan täcks någon annanstans.

### Vad är en ADR:s livscykel?

Tänk på områden som skapandeprocess, undersökningsprocess, beslutsprocess, genomförandeprocess och avvecklingsprocess. Överväg hur man spårar ADR:ens livscykel över tid, till exempel hur man flyttar ADR:en från ett tillstånd till nästa, och även hur man kommunicerar detta till intressenterna. 

Exempelsvar: Vi vill att en ADR ska ha fem livscykelsteg: Inleda (Initiating) → Undersöka (Researching) → Utvärdera (Evaluating) → Genomföra (Implementing) → Underhålla (Maintaining) → Avveckla (Sunsetting).

### Vilka är kriterierna för en ADR:s livscykelsteg?

Tänk på områden som godkännandekriterier för en ADR, det vill säga hur vet du att den är tillräckligt bra för att gå från ett livscykelsteg till nästa? Är problemet tydligt formulerat? Har alternativen övervägts? Är avvägningarna tillräckligt väl förstådda och dokumenterade?
Finns allt relevant sammanhang på plats? Är alla relevanta intressenter involverade? Har all återkoppling arbetats in? 

Exempelsvar: Vi vill att en ADR röstas om av intressenter när det aktiva teamet har 1) slutfört sin undersökning, 2) slutfört sin utvärdering, 3) publicerat ADR-förslaget för intressenterna med en begäran om kommentarer och en tidsram på en vecka, 4) alla kommentarer från intressenterna har arbetats in och åtgärdats.

### Vilka roller och ansvar samverkar med en ADR?

Tänk på roller som förslagsställare, undersökare, utvärderare, granskare, godkännare, underhållare och liknande. Tänk på ansvar som kommunikation med intressenter, att säkerställa att förväntningar uppfylls, delning på webbplatsen eller intranätet och periodisk granskning av arbetet, särskilt när relevanta förändringar sker.

Exempelsvar: Vi vill att varje ADR alltid ska ha en primär kontaktperson, en sekundär kontaktperson och ett ansvarigt team; dessa ansvarar för kommunikation, publicering, underhåll, periodisk granskning minst en gång per år och eventuell avveckling vid behov.

### Hur samverkar styrning med en ADR?

Tänk på områden som din organisations arbetssätt, eventuella särskilda efterlevnadsbehov, till exempel gällande juridiska aspekter eller personalaspekter, hur du vill hantera samsyn kontra konflikt kontra eskalering. Finns det områden eller personer eller team som kan ha större inflytande än andra när det gäller en ADR, till exempel genom att kunna godkänna den, rösta om den eller lägga in veto mot den?

Exempelsvar: Styrningen av en ADR sker i denna prioritetsordning: vd:n, teknikchefen, juridikchefen, teamet som genomför en ADR, experterna i teamet som har mest kunskap om ADD:n. Ingen annan har styrning om det inte beskrivs i ADR:en. 

### Vilka principer samverkar med en ADR?

Tänk på områden som din organisations arbetssätt, som omfattar att röra sig snabbt kontra att röra sig långsamt, beslutssamsyn kontra beslutskonflikt, och riskpreferenser kontra säkerhetspreferenser, offentlig diskussion kontra privat diskussion, och liknande.

Exempelsvar: Vi använder ledarskapsprinciperna handlingsbenägenhet (bias for action), oenighet-och-åtagande (disagree-and-commit), 70 % uppskattningar är tillräckligt bra för lätt reversibla, lätt isolerbara beslut, och offentliga arbetssätt med undantag för konfidentiell information såsom beskrivs i vår organisations sekretessavtal.

## Nästa-steg-koncept för ADR:er

[Arc42](https://arc42.org/) besvarar två frågor pragmatiskt och kan anpassas efter dina behov. Vad bör du dokumentera/kommunicera om din arkitektur? Hur bör du dokumentera/kommunicera? Arc42 omfattar arkitekturbeslutsposter samt vägledning om mål, begränsningar, sammanhang, kvalitet, risker och mer.

[C4-modellen](https://c4model.com/) är ett lättlärt, utvecklarvänligt sätt att rita diagram över programvaruarkitektur. C4 är en uppsättning hierarkiska diagram för kontext, containrar, komponenter och kod, plus stödjande diagram för systemlandskap, dynamik och driftsättning.

## Arkitekturdiagram, vyer och synvinklar

Ett arkitekturdiagram kallas en "arkitekturvy".

En "arkitekturvy" är en instans av en "arkitektursynvinkel".

En "arkitektursynvinkel" har en specifik målgrupp med specifika angelägenheter i åtanke.

Exempel på arkitektursynvinklar, vyer och diagram:

- Affärsförmågor

- Affärsprocesser på hög nivå

- [Värdeflöden](https://en.wikipedia.org/wiki/Value_stream)

- Programvarufunktioner kopplade till applikationskomponenter

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Kontextdiagram (TO-BE / AS-IS)

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Containerdiagram (TO-BE / AS-IS)

- [Entitet-relationsdiagram](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) för att koppla dataentiteter till applikationskomponenter

- [Sekvensdiagram](https://en.wikipedia.org/wiki/Sequence_diagram) för att beskriva funktionella flöden inom system och vid integrationer

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagram för att beskriva dataflöden mellan applikationskomponenter

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagram för att beskriva affärsprocesser / användarscenarier

- [Identitets- och åtkomsthantering](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) diagram

- [Rollbaserad åtkomstkontroll](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) diagram med roller per applikationskomponent

- [Attributbaserad åtkomstkontroll](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) diagram med attribut per applikationskomponent

- Integritetsdiagram

Relaterade diagram:

- Ett användningsfallsdiagram visar användningsfall för ledning/kunder, vilket föregår kraven, som föregår programvaruarkitekturen.

- Ett driftsättningsdiagram visar den fysiska hårdvaran/de datorer som programvarukomponenterna driftsätts på.
- Ett dataflödesdiagram visar hur data rör sig genom systemet och omvandlas.
- Ett sekvensdiagram används för att visa hur protokoll som HTTP fungerar på en tidsaxel.

- Ett aktivitetsdiagram skildrar arbetsflödet för de aktiviteter ett programvarusystem utför, som en NPC-AI.

## Lämplighetsfunktioner för beslut som kod

Lämplighetsfunktioner (fitness functions) är objektiva automatiserade kontroller, skrivna med programmeringskod, som verifierar att beslut upprätthålls.

- Lämplighetsfunktioner gör beslut testbara och säkerställbara.

- Lämplighetsfunktioner för beslut kan i hög grad hjälpa kvalitetssäkring, regelefterlevnadsprocesser och styrningsmål.

### Hur lämplighetsfunktioner hänger ihop med beslut

En beslutspost dokumenterar beslutet, medan en lämplighetsfunktion säkerställer beslutet.

- Exempel på beslut: Vi använder event sourcing för granskningskrav.

- Exempel på lämplighetsfunktion: Vi använder servern för kontinuerlig integration för att testa att alla tillståndsändringar måste ge upphov till händelser.

### Varför lämplighetsfunktioner hjälper beslut

Objektiva mätningar: Lämplighetsfunktioner godkänns eller underkänns, så arbetet blir synligt och tydligt.

Kontinuerlig användning: Lämplighetsfunktioner är dina levande regler och körs vid varje commit och bygge.

Förtroende att refaktorera: Lämplighetsfunktioner fångar automatiskt fel i beslutsregler.

Skalbar styrning: Lämplighetsfunktioner säkerställer standarder utan att skapa flaskhalsar.

### Kan lämplighetsfunktioner använda AI?

Lämplighetsfunktioner kan utnyttja AI-LLM:er för beslut genom att ställa frågor om ditt arbete,
till exempel dina planer, kod, scheman, API:er och mer:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Enhetstestning av arkitektur

[ArchUnit](https://www.archunit.org/): kontrollera arkitekturregler för Java-kod med valfritt enkelt ramverk för Java-enhetstester.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): kontrollera arkitekturregler för TypeScript-kod och JavaScript-kod med Jest, Vitest, Jasmine och så vidare.

## Beslutsräcken för pull requests

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
visar automatiskt rätt beslutsposter i rätt ögonblick, nämligen när en
utvecklare aktivt ändrar den kod som besluten täcker. I stället för att hoppas att utvecklare
läser en dokumentmapp innan de slår ihop, dyker rätt sammanhang upp direkt i pull requesten.

Det här fungerar för alla slags beslutsposter: arkitekturbeslut, databeslut, efterlevnadsbeslut, kliniska och medicinska beslut, säkerhetsbeslut och mer.

Fungerar med alla CI-system (GitLab, Jenkins, CircleCI) och som pre-commit-hook.
Öppen källkod. MIT-licens.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) är en GitHub
Action som får en pull request att misslyckas när bevakade kodsökvägar ändras utan att en
arkitekturbeslutspost läggs till eller uppdateras. Undantag är uttryckliga: en
`ADR-Exempt:`-rad med en orsak släpper igenom grinden och skrivs in i jobbets sammanfattning. Mallagnostisk, inga beroenden. Öppen källkod. MIT-licens.

## Mer information

Introduktion:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Mallar:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Fördjupning:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - gratis månatlig lektion i programvaruarkitektur

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Verktyg:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Företagsspecifik vägledning:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Exempel:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Videor:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Poddar:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Böcker:

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

Se även:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Ett leverantörsneutralt, maskinläsbart YAML/JSON-format för att representera beslut med uttryckligt resonemang, antaganden, kognitivt tillstånd och avvägningar. Kompletterar ADR:er genom att lägga till strukturerat, validerbart resonemang i beslutsdokumentationen.
