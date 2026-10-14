# Architectuurbeslissingsdocument (ADR)

Een architectuurbeslissingsdocument (ADR) is een document dat een belangrijke architectuurbeslissing vastlegt, samen met de context en de gevolgen ervan.

> [!IMPORTANT]
> Voer zelf uw eigen zorgvuldigheidsonderzoek uit naar deze bronnen voordat u ze in kritieke systemen gebruikt.

Inhoud:

- [Wat is een architectuurbeslissingsdocument?](#wat-is-een-architectuurbeslissingsdocument)
- [Hoe begin je met ADR's](#hoe-begin-je-met-adrs)
- [Hoe begin je met ADR's met tools](#hoe-begin-je-met-adrs-met-tools)
- [Hoe begin je met ADR's met git](#hoe-begin-je-met-adrs-met-git)
- [Claude Code-vaardigheden voor ADR's](#claude-code-vaardigheden-voor-adrs)
- [Conventies voor bestandsnamen](#conventies-voor-bestandsnamen)
- [Suggesties voor het schrijven van goede ADR's](#suggesties-voor-het-schrijven-van-goede-adrs)
- [ADR-voorbeeldsjablonen](#adr-voorbeeldsjablonen)
- [Teamwerkadvies voor ADR's](#teamwerkadvies-voor-adrs)
- [Teamwerkvragen voor ADR's](#teamwerkvragen-voor-adrs)
- [Concepten voor de volgende stap bij ADR's](#concepten-voor-de-volgende-stap-bij-adrs)
- [Architectuurdiagrammen, weergaven en gezichtspunten](#architectuurdiagrammen-weergaven-en-gezichtspunten)
- [Fitnessfuncties voor beslissingen als code](#fitnessfuncties-voor-beslissingen-als-code)
- [Beslissingsvangrails voor pull requests](#beslissingsvangrails-voor-pull-requests)
- [Meer informatie](#meer-informatie)

Sjablonen:

- [Beslissingsdocumentsjabloon van Jeff Tyree en Art Akerman](sjablonen/beslissingsdocumentsjabloon-van-jeff-tyree-en-art-akerman/)
- [Beslissingsdocumentsjabloon van Michael Nygard](sjablonen/beslissingsdocumentsjabloon-van-michael-nygard/)
- [Beslissingsdocumentsjabloon van EdgeX](sjablonen/beslissingsdocumentsjabloon-van-edgex/)
- [Beslissingsdocumentsjabloon van arc42](sjablonen/beslissingsdocumentsjabloon-van-arc42/)
- [Beslissingsdocumentsjabloon voor alexandrijns patroon](sjablonen/beslissingsdocumentsjabloon-voor-alexandrijns-patroon/)
- [Beslissingsdocumentsjabloon voor businesscase](sjablonen/beslissingsdocumentsjabloon-voor-businesscase/)
- [Beslissingsdocumentsjabloon van het MADR-project](sjablonen/beslissingsdocumentsjabloon-van-het-madr-project/)
- [Beslissingsdocumentsjabloon met Planguage](sjablonen/beslissingsdocumentsjabloon-met-planguage/)
- [Beslissingsdocumentsjabloon van Paulo Merson](https://github.com/pmerson/ADR-template)
- [Beslissingsdocumentsjabloon van Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Beslissingsdocumentsjabloon van Gareth Morgan](sjablonen/beslissingsdocumentsjabloon-van-gareth-morgan/)
- [Beslissingsdocumentsjabloon van GIG Cymru NHS Wales](sjablonen/beslissingsdocumentsjabloon-van-gig-cymru-nhs-wales/)
- [Beslissingsdocumentsjabloon voor belangrijke technische beslissingen van Ignacio Larrañaga](sjablonen/beslissingsdocumentsjabloon-voor-belangrijke-technische-beslissingen/)

Voorbeelden:

- [CSS-framework](voorbeelden/css-framework/)
- [Configuratie met omgevingsvariabelen](voorbeelden/configuratie-met-omgevingsvariabelen/)
- [Statistieken, monitoring, waarschuwingen](voorbeelden/statistieken-monitoring-waarschuwingen/)
- [Microsoft Azure DevOps](voorbeelden/microsoft-azure-devops/)
- [Monorepo of multirepo](voorbeelden/monorepo-of-multirepo/)
- [Programmeertalen](voorbeelden/programmeertalen/)
- [Opslag van geheimen](voorbeelden/opslag-van-geheimen/)
- [Tijdstempelformaat](voorbeelden/tijdstempelformaat/)
- [Nog veel meer...](voorbeelden/)

## Wat is een architectuurbeslissingsdocument?

Een **architectuurbeslissingsdocument** (ADR) is een document dat een belangrijke architectuurbeslissing vastlegt, samen met de context en de gevolgen ervan.

Een **architectuurbeslissing** (AD) is een softwareontwerpkeuze die inspeelt op een significante eis.

Een **architectuurbeslissingslogboek** (ADL) is de verzameling van alle ADR's die voor een bepaald project (of een bepaalde organisatie) zijn gemaakt en bijgehouden.

Een **architectonisch significante eis** (ASR) is een eis die een meetbaar effect heeft op de architectuur van een softwaresysteem.

Dit alles valt onder het onderwerp **architectuurkennisbeheer** (AKM).

Het doel van dit document is een snel overzicht te geven van ADR's, hoe je ze schrijft en waar je meer informatie vindt.

Afkortingen:

  * **AD**: architectuurbeslissing

  * **ADL**: architectuurbeslissingslogboek

  * **ADR**: architectuurbeslissingsdocument

  * **AKM**: architectuurkennisbeheer

  * **ASR**: architectonisch significante eis

## Hoe begin je met ADR's

Om met ADR's te beginnen, praat je met je teamgenoten over de volgende gebieden.

Beslissingen identificeren:

  * Hoe dringend en hoe belangrijk is de AD?

  * Moet de beslissing nu worden genomen, of kan ze wachten tot er meer bekend is?

  * Persoonlijke en collectieve ervaring, evenals erkende ontwerpmethoden en -praktijken, kunnen helpen bij het identificeren van beslissingen.

  * Houd idealiter een beslissingenbacklog bij die de productbacklog aanvult.

Beslissingen nemen:

  * Er bestaan verschillende technieken voor besluitvorming, waaronder algemene technieken en technieken die specifiek zijn voor softwarearchitectuur. Een voorbeeld is dialoogmapping.

  * Groepsbesluitvorming is een actief onderzoeksonderwerp.

Beslissingen afdwingen en handhaven:

  * Omdat AD's worden gebruikt bij softwareontwerp, moeten ze worden gecommuniceerd naar en geaccepteerd door de belanghebbenden die het systeem financieren, ontwikkelen en exploiteren.

  * Architectuurbewuste codeerstijlen en codebeoordelingen die zich richten op architectuurgerelateerde zaken en beslissingen zijn twee verwante praktijken.

  * AD's moeten ook worden (her)overwogen bij het moderniseren van een softwaresysteem tijdens software-evolutie.

Beslissingen delen (optioneel):

  * Veel AD's worden herhaald in verschillende projecten.

  * Daarom kan ervaring met eerdere beslissingen, zowel goede als slechte, een waardevol herbruikbaar bezit zijn bij gebruik van een expliciete kennisbeheerstrategie.

Beslissingen documenteren:

  * Er zijn veel sjablonen en tools voor het vastleggen van beslissingen.

  * Raadpleeg de agile gemeenschap, bijvoorbeeld de ADR's van M. Nygard.

  * Raadpleeg traditionele softwaretechniek en architectuurontwerpprocessen, bijvoorbeeld IBM UMF en de tabelindeling voorgesteld door Tyree en Akerman van CapitalOne.

Meer informatie:

  * De bovenstaande stappen komen uit het Wikipedia-artikel [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Hoe begin je met ADR's met tools

- [MySpec](https://myspec.dev) — Geautomatiseerd platform voor specificaties en architectuurbeslissingen dat de projectconstitutie, technische architectuur en ADR's structureert in overzichtelijke Markdown die via MCP wordt aangeboden.

Je kunt zelf kiezen hoe je met ADR's begint met tools.

Bijvoorbeeld:

  * Als je van Google Drive en online bewerken houdt, kun je een Google-document of Google-spreadsheet maken.

  * Als je van broncodeversiebeheer zoals git houdt, kun je voor elke ADR een bestand maken.

  * Als je van projectplanningstools zoals Atlassian Jira houdt, kun je de planningstracker daarvan gebruiken.

  * Als je van wiki's zoals MediaWiki houdt, kun je een ADR-wiki maken.

## Hoe begin je met ADR's met git

Als je van git-versiebeheer houdt, zo beginnen wij met ADR's met git in een typisch softwareproject met broncode.

Maak een map voor je ADR-bestanden:

```sh
$ mkdir adr
```

Maak voor elke ADR een tekstbestand, zoals `database.txt`:

```sh
$ vi database.txt
```

Schrijf in de ADR wat je maar wilt. Voor ideeën zie je de sjablonen in deze repository.

Commit de ADR's naar je git-repository.

## Claude Code-vaardigheden voor ADR's

Deze repository bevat twee [Claude Code](https://claude.com/claude-code)-vaardigheden (skills) onder [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), zodat een AI-codeeragent ADR's kan schrijven en onderhouden zoals dit project aanbeveelt:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — voor algemeen gebruik, voor iedereen die in een willekeurig project een ADR schrijft. Helpt beslissen of een beslissing een ADR nodig heeft, maakt een map `adr/` of `decisions/` aan, geeft het bestand een naam, kiest een sjabloon uit de elf meegeleverde skeletten en schrijft solide secties over context, beslissing en gevolgen.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — speciaal voor de beheerders van deze repository. Documenteert de opzet van de repository, de afspraak om README en locales te spiegelen en de exacte stappen om een nieuw sjabloon, voorbeeld of toollink toe te voegen.

Om een vaardigheid te gebruiken, kopieert u de map naar `.claude/skills/` in de hoofdmap van de repository waarin u werkt (of naar `~/.claude/skills/` om hem in elk project beschikbaar te maken) en vraagt u Claude Code vervolgens een ADR te schrijven of te beoordelen.

## Conventies voor bestandsnamen

Als je ervoor kiest ADR's als platte tekstbestanden te schrijven, kan het nuttig zijn een eigen conventie voor ADR-bestandsnamen vast te stellen.

Wij geven de voorkeur aan een conventie voor bestandsnamen met een specifiek formaat.

Voorbeelden:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Onze conventie voor bestandsnamen:

  * De naam is een gebiedende wijs in de tegenwoordige tijd. Dit verbetert de leesbaarheid en komt overeen met ons formaat voor commitberichten.

  * De naam gebruikt kleine letters en streepjes (hetzelfde als in deze repository). Dit is een balans tussen leesbaarheid en bruikbaarheid in systemen.

  * De extensie is markdown. Dit kan handig zijn voor eenvoudige opmaak.

## Suggesties voor het schrijven van goede ADR's

Kenmerken van een goede ADR:

* Onderbouwing: leg uit waarom de AD wordt uitgevoerd. Dit kan context omvatten (zie hieronder), voor- en nadelen van verschillende mogelijke opties, functievergelijkingen, kosten-batenanalyses enzovoort.

* Specifiek: elke ADR moet over één AD gaan, niet over meerdere AD's.

* Tijdgestempeld: geef aan wanneer elk item in de ADR is geschreven. Dit is vooral belangrijk voor aspecten die in de loop van de tijd kunnen veranderen, zoals kosten, planning, uitbreiding enzovoort.

* Onveranderlijk: wijzig bestaande informatie in een ADR niet. Wijzig de ADR in plaats daarvan door nieuwe informatie toe te voegen, of vervang de ADR door een nieuwe ADR te maken.

Kenmerken van een goede sectie "Context" in een ADR:

* Beschrijft de situatie van de organisatie en de zakelijke prioriteiten.

* Bevat de onderbouwing en overwegingen op basis van de sociale en technische samenstelling van het team.

* Bevat relevante afwegingen, uitgedrukt in termen die passen bij de behoeften en doelen.

Kenmerken van een goede sectie "Gevolgen" in een ADR:

* Beschrijft wat er volgt uit het nemen van de beslissing. Dit kunnen effecten, resultaten, opleverbare producten, vervolgacties enzovoort zijn.

* Bevat informatie over vervolg-ADR's. Het komt relatief vaak voor dat één ADR de behoefte aan meer ADR's oproept. Als een ADR bijvoorbeeld een grote, overkoepelende keuze maakt, kan dat de behoefte aan kleinere beslissingen oproepen.

* Bevat een nabeschouwingsproces. Het is gebruikelijk dat teams elke ADR na een maand bekijken, de ADR-informatie vergelijken met wat er daadwerkelijk is gebeurd en daarvan leren en groeien.

Een nieuwe ADR kan een eerdere ADR vervangen:

* Wanneer een AD wordt genomen die een eerdere ADR vervangt of ongeldig maakt, moet een nieuwe ADR worden geschreven

## ADR-voorbeeldsjablonen

ADR-voorbeeldsjablonen die we op het web hebben verzameld:

- [ADR-sjabloon van Michael Nygard](sjablonen/beslissingsdocumentsjabloon-van-michael-nygard/) (eenvoudig en populair)

- [ADR-sjabloon van Jeff Tyree en Art Akerman](sjablonen/beslissingsdocumentsjabloon-van-jeff-tyree-en-art-akerman/) (verfijnder)

- [ADR-sjabloon voor het Alexandrian-patroon](sjablonen/beslissingsdocumentsjabloon-voor-alexandrijns-patroon/) (eenvoudig met contextdetails)

- [ADR-sjabloon voor een businesscase](sjablonen/beslissingsdocumentsjabloon-voor-businesscase/) (meer MBA-gericht, met kosten, SWOT en meer meningen)

- [ADR-sjabloon van het project Markdown Any Decision Records (MADR)](sjablonen/beslissingsdocumentsjabloon-van-het-madr-project/) (zowel een eenvoudige als een uitgebreide versie; de laatste legt de nadruk op opties en hun voor- en nadelen)

- [ADR-sjabloon met Planguage](sjablonen/beslissingsdocumentsjabloon-met-planguage/) (meer op kwaliteitsborging gericht)

- [Sjabloon voor Important Technical Decisions (ITD's) van Ignacio Larrañaga](sjablonen/beslissingsdocumentsjabloon-voor-belangrijke-technische-beslissingen/) (slank en beslissing-eerst, geoptimaliseerd voor snelle beoordeling door leidinggevenden)

## Teamwerkadvies voor ADR's

Als je overweegt beslissingsdocumenten in je team te gebruiken, volgt hier wat advies dat we hebben geleerd bij het werken met meerdere teams.

Er is een kans om teamleden te leiden door te praten over het "waarom" in plaats van het "wat" af te dwingen. Beslissingsdocumenten zijn bijvoorbeeld een manier voor teams om slimmer na te denken en beter te communiceren. Als beslissingsdocumenten slechts een papierwerkvereiste zijn die achteraf wordt afgedwongen, hebben ze geen waarde.

Sommige teams geven de voorkeur aan de naam "beslissingen" boven de afkorting "ADR". Wanneer sommige teams "decisions" als mapnaam gebruiken, gaat er een lampje branden en beginnen teams meer informatie in de map te zetten, zoals leveranciersbeslissingen, planningsbeslissingen, roosterbeslissingen enzovoort. Je kunt hetzelfde sjabloon voor al deze soorten informatie gebruiken. We gaan ervan uit dat mensen sneller leren met het woord ("beslissing") dan met de afkorting ("ADR"), dat het weglaten van het woord "document" meer motivatie geeft om lopend werk te schrijven, en dat sommige ontwikkelaars en sommige managers een hekel hebben aan het woord "architectuur".

In theorie is onveranderlijkheid ideaal. In de praktijk werkte veranderlijkheid beter voor ons team. We voegen nieuwe informatie toe aan een bestaande ADR, met een datumstempel en een opmerking dat de informatie na de beslissing is binnengekomen. Deze aanpak leidt tot een "levend document" dat we allemaal kunnen bijwerken. Typische updates komen van het opdoen van informatie dankzij nieuwe teamleden, nieuwe aanbod, werkelijke resultaten van ons gebruik, of na wijzigingen door derden achteraf zoals functies van leveranciers, prijsplannen en licentieovereenkomsten.

## Teamwerkvragen voor ADR's

### Wie kan ADR's schrijven?

Overweeg gebieden zoals specifieke personen, specifieke rollen, specifieke teams, specifieke afdelingen. Overweeg ook of er personen, rollen, teams of afdelingen zijn die ADR's kunnen laten maken, dat wil zeggen kunnen vragen dat iemand anders een ADR schrijft. 

Voorbeeldantwoord: iedereen in onze organisatie die de README-pagina over architectuurbeslissingsdocumenten heeft gelezen, kan een ADR voorstellen, dat wil zeggen beginnen met schrijven en delen met het team.

### Wat rechtvaardigt het indienen van een ADR?

Overweeg gebieden zoals hoe teams in de organisatie werken, de structuur van softwaresystemen, coördinatie tussen teams, onderhoudbaarheid op lange termijn, externe interfaces en wie je wilt laten profiteren. 

Voorbeeldantwoord: we willen een ADR schrijven wanneer we willen dat toekomstige ontwikkelaars het "waarom" achter wat we doen begrijpen.

### Wat rechtvaardigt het niet indienen van een ADR?

Overweeg gebieden zoals beslissingen die niet over architectuur gaan, beslissingen die triviaal zijn omdat ze minimaal risico hebben, op zichzelf staan of beperkt zijn tot één ontwikkelaar, beslissingen die al elders volledig worden behandeld in standaarden, beleid, documentatie enzovoort, of beslissingen die tijdelijk zijn, zoals noodoplossingen, proofs of concept en experimenten. 

Voorbeeldantwoord: we willen een ADR overslaan wanneer de beslissing beperkt is in reikwijdte, tijd, risico en kosten, of al elders wordt behandeld.

### Wat is de levenscyclus van een ADR?

Overweeg gebieden zoals het schrijfproces, het onderzoeksproces, het beslissingsproces, het implementatieproces en het uitfaseringsproces. Overweeg hoe je de levenscyclus van de ADR in de loop van de tijd volgt, bijvoorbeeld hoe je een ADR van de ene status naar de volgende verplaatst en hoe je dit aan belanghebbenden communiceert. 

Voorbeeldantwoord: we willen dat ADR's vijf levenscyclusfasen hebben: Initiating → Researching → Evaluating → Implementing → Maintaining → Sunsetting.

### Wat zijn de criteria voor de levenscyclusfasen van een ADR?

Overweeg gebieden zoals de acceptatiecriteria voor ADR's, dat wil zeggen hoe weten we dat een ADR goed genoeg is om van de ene levenscyclusfase naar de volgende te gaan? Is het probleem duidelijk beschreven? Zijn alternatieven overwogen? Zijn de afwegingen goed begrepen en gedocumenteerd?
Is alle relevante context aanwezig? Zijn alle relevante belanghebbenden betrokken? Is alle feedback verwerkt? 

Voorbeeldantwoord: we willen dat het actieve team 1) onderzoek afrondt, 2) evaluatie afrondt, 3) de ADR-voorstellen publiceert voor belanghebbenden met een verzoek om opmerkingen en een tijdslimiet van een week, en 4) wanneer alle opmerkingen van belanghebbenden zijn verwerkt en afgehandeld, laat belanghebbenden over de ADR stemmen.

### Welke rollen en verantwoordelijkheden werken samen met ADR's?

Overweeg rollen zoals indiener, onderzoeker, evaluator, beoordelaar, goedkeurder en onderhouder. Overweeg verantwoordelijkheden zoals communiceren met belanghebbenden, ervoor zorgen dat verwachtingen worden waargemaakt, delen op de website of het intranet, en het periodiek herzien van het werk, vooral wanneer er relevante wijzigingen zijn.

Voorbeeldantwoord: we willen dat elke ADR altijd een primaire eigenaar, een secundaire eigenaar en een verantwoordelijk team heeft. Zij zijn verantwoordelijk voor communicatie, publicatie, onderhoud, periodieke herziening minstens jaarlijks en uiteindelijke uitfasering indien nodig.

### Hoe werkt governance samen met ADR's?

Overweeg gebieden zoals hoe de organisatie werkt, speciale nalevingsbehoeften zoals juridische aspecten of HR-aspecten, en hoe je consensus versus conflict versus escalatie wilt behandelen. Zijn er gebieden, personen of teams die meer invloed kunnen hebben dan anderen, zoals de macht om goed te keuren, te stemmen of een veto uit te spreken in verband met ADR's?

Voorbeeldantwoord: de governance van een ADR volgt deze prioriteitsvolgorde: CEO, CTO, CLO, het team dat de ADR implementeert, de meest deskundige expert binnen het team over de ADD. Niemand heeft governance tenzij beschreven in de ADR. 

### Welke principes werken samen met ADR's?

Overweeg gebieden die te maken hebben met hoe de organisatie werkt, zoals snel of langzaam bewegen, beslissingsconsensus versus beslissingsconflict, risicovoorkeur versus veiligheidsvoorkeur, en openbare discussie versus privédiscussie.

Voorbeeldantwoord: we gebruiken de leiderschapsprincipes voorkeur voor actie (bias for action), het oneens zijn maar je committeren (disagree-and-commit), 70% van de informatie is genoeg voor beslissingen die gemakkelijk omkeerbaar en gemakkelijk te isoleren zijn, en openbaar werken, behalve voor vertrouwelijke informatie zoals beschreven in de geheimhoudingsovereenkomsten van onze organisatie.

## Concepten voor de volgende stap bij ADR's

[Arc42](https://arc42.org/) beantwoordt twee vragen op pragmatische wijze en kan op uw behoeften worden afgestemd. Wat moet u over uw architectuur documenteren/communiceren? Hoe moet u dat documenteren/communiceren? Arc42 omvat architectuurbeslissingsdocumenten plus richtlijnen over doelen, beperkingen, contexten, kwaliteit, risico's en meer.

[Het C4-model](https://c4model.com/) is een gemakkelijk te leren, ontwikkelaarsvriendelijke aanpak voor het tekenen van softwarearchitectuurdiagrammen. C4 is een reeks hiërarchische diagrammen voor context, containers, componenten en code, plus ondersteunende diagrammen voor systeemlandschap, dynamiek en uitrol.

## Architectuurdiagrammen, weergaven en gezichtspunten

Een architectuurdiagram heet een "architectuurweergave".

Een "architectuurweergave" is een instantie van een "architectuurgezichtspunt".

Een "architectuurgezichtspunt" richt zich op een specifiek publiek met specifieke zorgen.

Voorbeelden van architectuurgezichtspunten, weergaven en diagrammen:

- Bedrijfsvermogens

- Bedrijfsprocessen op hoog niveau

- [Waardestromen](https://en.wikipedia.org/wiki/Value_stream)

- Softwarefuncties gekoppeld aan toepassingscomponenten

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Contextdiagram (TO-BE / AS-IS)

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Containerdiagram (TO-BE / AS-IS)

- [Entiteit-relatiediagram](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) om gegevensentiteiten aan toepassingscomponenten te koppelen

- [Sequentiediagrammen](https://en.wikipedia.org/wiki/Sequence_diagram) om functionele stromen binnen systemen en bij integraties te beschrijven

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagrammen om gegevensstromen tussen toepassingscomponenten te beschrijven

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagrammen om bedrijfsprocessen / gebruikersscenario's te beschrijven

- [Identity and Access Management](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) diagrammen

- [Rolgebaseerde toegangscontrole](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) diagrammen met rollen per toepassingscomponent

- [Attribuutgebaseerde toegangscontrole](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) diagrammen met attributen per toepassingscomponent

- Privacydiagrammen

Gerelateerde diagrammen:

- Een use-casediagram toont use cases aan management/klanten; dit gaat vooraf aan de requirements, die voorafgaan aan de softwarearchitectuur.

- Een deploymentdiagram toont de fysieke hardware/computers waarop de softwarecomponenten worden uitgerold.
- Een gegevensstroomdiagram toont hoe gegevens door het systeem bewegen en worden getransformeerd.
- Een sequentiediagram wordt gebruikt om te laten zien hoe protocollen zoals HTTP op een tijdas werken.

- Een activiteitendiagram toont de workflow van de activiteiten die een softwaresysteem uitvoert, zoals een NPC-AI.

## Fitnessfuncties voor beslissingen als code

Een fitnessfunctie is een objectieve, geautomatiseerde controle, geschreven als programmeercode, die verifieert dat een beslissing wordt nagekomen.

- Fitnessfuncties maken beslissingen testbaar en controleerbaar.

- Fitnessfuncties voor beslissingen kunnen enorm helpen bij kwaliteitsborging, regelgevingsprocessen en governancedoelen.

### Hoe fitnessfuncties en beslissingen samenhangen

Een beslissingsdocument legt een beslissing vast; een fitnessfunctie handhaaft die beslissing.

- Voorbeeldbeslissing: gebruik event sourcing voor auditvereisten.

- Voorbeeld van een fitnessfunctie: gebruik een continue-integratieserver om te testen dat elke statuswijziging een gebeurtenis moet genereren.

### Waarom fitnessfuncties beslissingen helpen

Objectieve meting: een fitnessfunctie slaagt of faalt, dus het werk is zichtbaar en duidelijk.

Doorlopend gebruik: een fitnessfunctie is een levende regel en draait bij elke commit en build.

Vertrouwen bij refactoring: een fitnessfunctie vangt fouten tegen de beslissingsregels automatisch op.

Schaalbare governance: een fitnessfunctie handhaaft standaarden zonder knelpunten te creëren.

### Kunnen fitnessfuncties AI gebruiken?

Een fitnessfunctie kan een AI-LLM voor beslissingen gebruiken door vragen te stellen
over ons werk, zoals plannen, code, schema's, API's enzovoort:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Architectuureenheidstests

[ArchUnit](https://www.archunit.org/): controleer architectuurregels voor Java-code met een gangbaar Java-unittestframework.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): controleer architectuurregels voor TypeScript-code en JavaScript-code met Jest, Vitest, Jasmine en andere.

## Beslissingsvangrails voor pull requests

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
brengt automatisch de juiste beslissingsdocumenten naar voren op het juiste moment, namelijk wanneer een
ontwikkelaar actief de code wijzigt waar die beslissingen betrekking op hebben. In plaats van te hopen dat ontwikkelaars
een documentenmap lezen voordat ze mergen, verschijnt de relevante context direct in de pull request.

Dit werkt voor elk soort beslissingsdocument: architectuurbeslissingen, databeslissingen, compliancebeslissingen, klinische en medische beslissingen, beveiligingsbeslissingen en meer.

Werkt met elk CI-systeem (GitLab, Jenkins, CircleCI) en als pre-commit-hook.
Open source. MIT-licentie.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) is een GitHub
Action die een pull request laat mislukken wanneer bewaakte codepaden veranderen zonder dat een
architectuurbeslissingsdocument wordt toegevoegd of bijgewerkt. Vrijstellingen zijn expliciet: een
`ADR-Exempt:`-regel met een reden laat de poort passeren en wordt in de jobsamenvatting vermeld. Sjabloononafhankelijk, geen afhankelijkheden. Open source. MIT-licentie.

## Meer informatie

Inleiding:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Sjablonen:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Diepgaand:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - gratis maandelijkse les over softwarearchitectuur

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Hulpmiddelen:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Bedrijfsspecifieke richtlijnen:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Voorbeelden:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Video's:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcasts:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Boeken:

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

Zie ook:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Een leveranciersneutraal, machineleesbaar YAML/JSON-formaat om beslissingen weer te geven met expliciete redenering, aannames, cognitieve toestand en afwegingen. Vult ADR's aan door gestructureerde, valideerbare redenering aan beslissingsdocumentatie toe te voegen.
