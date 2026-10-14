# AWS-proces voor architectuurbeslissingsdocumenten

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Een architectuurbeslissingsdocument (architectural decision record, ADR) is een document waarin de keuzes worden beschreven die een team maakt over een belangrijk aspect van de softwarearchitectuur die het van plan is te bouwen. Elke ADR beschrijft de architectuurbeslissing, de context en de gevolgen. ADR's hebben een status en volgen daardoor een levenscyclus. Zie de bijlage voor voorbeelden van ADR's.

Het ADR-proces levert een verzameling architectuurbeslissingsdocumenten op. Die verzameling vormt het beslissingslogboek. Het beslissingslogboek biedt gedetailleerde implementatie- en ontwerpinformatie, naast de projectcontext. Projectleden doorlopen de titel van elke ADR om een overzicht van de projectcontext te krijgen. Vervolgens lezen ze de ADR's om diepgaand inzicht te krijgen in de implementatie- en ontwerpkeuzes van het project.

Wanneer het team een ADR accepteert, wordt die onveranderlijk. Als nieuwe inzichten een andere beslissing vereisen, stelt het team een nieuwe ADR voor. Wanneer het team de nieuwe ADR accepteert, vervangt die de vorige ADR.

## Reikwijdte van het ADR-proces

Projectleden moeten een ADR schrijven voor elke architectonisch significante beslissing die van invloed is op het softwareproject of product, waaronder (Richards en Ford 2020):

* Structuur (bijvoorbeeld patronen zoals microservices)

* Niet-functionele eisen (beveiliging, hoge beschikbaarheid, fouttolerantie)

* Afhankelijkheden (koppeling van componenten)

* Interfaces (API's en gepubliceerde contracten)

* Constructietechnieken (bibliotheken, frameworks, tools, processen)

* Functionele en niet-functionele eisen zijn de meest voorkomende invoer voor het ADR-proces.


## Inhoud van een ADR

Wanneer het team de behoefte aan een ADR vaststelt, beginnen teamleden met het schrijven van de ADR op basis van een projectbreed sjabloon. (Zie de ADR-organisatie op GitHub voor voorbeelden van sjablonen.) Het sjabloon vereenvoudigt het schrijven van de ADR en zorgt ervoor dat de ADR alle relevante informatie bevat. Elke ADR moet minimaal de context van de beslissing, de beslissing zelf en de gevolgen van de beslissing voor het project en de opgeleverde producten definiëren. (Zie de bijlage voor voorbeelden van deze secties.) Een van de krachtigste aspecten van de ADR-structuur is de focus op de reden achter de beslissing in plaats van op hoe het team die heeft geïmplementeerd. Als je begrijpt waarom het team de beslissing heeft genomen, is het voor andere teamleden gemakkelijker om de beslissing te accepteren en voorkom je dat andere architecten die niet aan het beslissingsproces hebben deelgenomen de beslissing later terugdraaien.


## Het ADR-adoptieproces

Hoewel elk teamlid een ADR kan schrijven, moet het team een definitie van eigenaarschap voor ADR's vaststellen. Elke auteur, de eigenaar van de ADR, moet de inhoud van de ADR actief bijhouden en communiceren. Om dit eigenaarschap te verduidelijken noemt deze gids ADR-auteurs in latere secties ADR-eigenaren. Andere teamleden kunnen op elk moment aan de ADR bijdragen. Als de inhoud van de ADR verandert voordat het team de ADR accepteert, moet de eigenaar deze wijzigingen goedkeuren.

Nadat het team de architectuurbeslissing en de eigenaar ervan heeft vastgesteld, presenteert de ADR-eigenaar vroeg in het proces een ADR met de status **Proposed** (voorgesteld). Een ADR met de status Proposed is klaar voor beoordeling.

Vervolgens start de ADR-eigenaar het beoordelingsproces voor die ADR. Het doel van het ADR-beoordelingsproces is dat het team besluit of het de ADR accepteert, vaststelt dat herwerking nodig is, of de ADR afwijst. Het projectteam, inclusief de eigenaar, beoordeelt de ADR. De beoordelingsvergadering moet beginnen met een gereserveerd moment om de ADR te lezen. Gemiddeld is 10–15 minuten voldoende. Tijdens deze tijd voegt elk teamlid opmerkingen en vragen toe om onduidelijke onderwerpen te markeren. Aan het einde van de beoordelingsfase leest de ADR-eigenaar elke opmerking en bespreekt die met het team.

Wanneer het team actiepunten vindt om de ADR te verbeteren, blijft de status van de ADR **Proposed**. De ADR-eigenaar verzamelt de acties en werkt samen met het team om aan elke actie een verantwoordelijke toe te wijzen. Elk teamlid kan aan de actiepunten bijdragen en ze oplossen. Het is de verantwoordelijkheid van de ADR-eigenaar om het beoordelingsproces opnieuw in te plannen.

Het team kan ook besluiten de ADR af te wijzen. In dat geval voegt de ADR-eigenaar de reden voor afwijzing toe om toekomstige discussies over hetzelfde onderwerp te voorkomen. De eigenaar wijzigt de status van de ADR in **Rejected** (afgewezen).

Wanneer het team de ADR goedkeurt, voegt de eigenaar een tijdstempel, een versie en een lijst van belanghebbenden toe. Daarna werkt de eigenaar de status bij naar **Accepted** (geaccepteerd).

De ADR en het beslissingslogboek dat daaruit ontstaat, vertegenwoordigen de beslissingen van het team en bieden een geschiedenis van alle beslissingen. Waar mogelijk gebruikt het team ADR's als referentie tijdens code- en architectuurbeoordelingen. Naast het uitvoeren van codebeoordelingen, ontwerpwerk en implementatiewerk moeten teamleden ADR's raadplegen voor strategische beslissingen over het product.

Als goede praktijk moeten alle softwarewijzigingen een collegiale beoordeling ondergaan en minimaal één goedkeuring vereisen. Tijdens de codebeoordeling kan een beoordelaar een wijziging aantreffen die een of meer ADR's schendt. In dat geval vraagt de beoordelaar de auteur van de codewijziging om de code te corrigeren en deelt de link naar de ADR('s). Zodra de auteur de code corrigeert, krijgt die de goedkeuring van een collega-beoordelaar en wordt de code samengevoegd in de hoofdcodebase.


## Het ADR-beoordelingsproces

Nadat het team een ADR heeft geaccepteerd of afgewezen, moet het deze behandelen als een onveranderlijk document. Om een bestaande ADR te wijzigen, moet het team een nieuwe ADR schrijven, het beoordelingsproces voor de nieuwe ADR vaststellen en de ADR goedkeuren. Wanneer het team de nieuwe ADR goedkeurt, moet de eigenaar de status van de oude ADR wijzigen in **Superseded** (vervangen). 
