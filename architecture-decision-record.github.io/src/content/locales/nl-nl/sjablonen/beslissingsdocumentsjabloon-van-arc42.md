# Beslissingsdocumentsjabloon van arc42

<https://arc42.org/overview>

## 1. Inleiding en doelen

Eisen, korte beschrijving van de drijfveren, uittreksel (of samenvatting) van de eisen. De top drie (maximaal vijf) kwaliteitsdoelen voor de architectuur met de hoogste prioriteit voor de belangrijkste belanghebbenden. Een overzicht van belangrijke belanghebbenden met hun verwachtingen van de architectuur.

## 1.1 Overzicht van de eisen

### Inhoud

Korte beschrijving van de functionele eisen, drijfveren, uittreksel (of
samenvatting) van de eisen. Links naar (hopelijk bestaande) eisendocumenten
met informatie over waar ze te vinden zijn. 

### Motivatie

Vanuit het perspectief van de eindgebruikers wordt een systeem gebouwd of gewijzigd om
de ondersteuning van bedrijfsactiviteiten te verbeteren of om de kwaliteit te verhogen. 

### Vorm

Korte tekstuele beschrijving, eventueel in tabelvorm van gebruiksscenario's. Als
eisendocumenten bestaan, moet dit overzicht naar die documenten verwijzen.

Houd dit uittreksel zo kort mogelijk. Weeg de leesbaarheid van dit document af tegen
mogelijke redundantie met eisendocumenten. 

## 1.2 Kwaliteitsdoelen

### Inhoud

De top drie (maximaal vijf) kwaliteitsdoelen voor de architectuur waarvan de
vervulling het belangrijkst is voor de belangrijkste belanghebbenden. We bedoelen echt kwaliteitsdoelen voor de architectuur. Verwar ze
niet met projectdoelen. Ze zijn niet noodzakelijk identiek. De ISO 25010-standaard
biedt een goed overzicht van potentiële onderwerpen van belang.

### Motivatie

Je moet de kwaliteitsdoelen van de belangrijkste belanghebbenden kennen, omdat ze
fundamentele architectuurbeslissingen beïnvloeden. Wees zeer
concreet over deze kwaliteiten en vermijd modewoorden. Als je als architect niet weet hoe de kwaliteit van je werk
zal worden beoordeeld …

### Vorm

Een tabel met de belangrijkste kwaliteitsdoelen en concrete scenario's, op volgorde van prioriteit.

## 1.3 Belanghebbenden

### Inhoud

Expliciet overzicht van de belanghebbenden van het systeem, dat wil zeggen alle personen, rollen of organisaties die

- de architectuur moeten kennen

- van de architectuur moeten worden overtuigd

- met de architectuur of de code moeten werken

- de architectuurdocumentatie nodig hebben voor hun werk

- beslissingen moeten nemen over het systeem of de ontwikkeling ervan

### Motivatie

Je moet alle partijen kennen die betrokken zijn bij de ontwikkeling van het systeem of erdoor worden beïnvloed.
Anders kun je later in het ontwikkelproces onaangename verrassingen tegenkomen. Deze belanghebbenden
bepalen de omvang en het detailniveau van je werk en de resultaten.

### Vorm

Tabel met rolnamen, persoonsnamen en hun verwachtingen ten aanzien van de architectuur en de
documentatie ervan.

## 2. Beperkingen

Alles wat het team beperkt in ontwerp- en implementatiebeslissingen of beslissingen over het gerelateerde proces.
Soms gelden ze voor hele organisaties en bedrijven, buiten individuele systemen om.

### Inhoud

Alle eisen die softwarearchitecten beperken in hun vrijheid met betrekking tot
ontwerp-, implementatie- of ontwikkelprocesbeslissingen. Deze beperkingen gelden soms
voor hele organisaties en bedrijven, buiten individuele systemen om.

### Motivatie

Architecten moeten precies weten waar ze vrij zijn in hun ontwerpbeslissingen en
waar ze beperkingen moeten respecteren. Beperkingen moeten altijd worden behandeld,
maar zijn mogelijk onderhandelbaar.

### Vorm

Eenvoudige tabellen met beperkingen en uitleg. Indien nodig kun je ze
onderverdelen in technische beperkingen, organisatorische en politieke beperkingen en
conventies (bijvoorbeeld programmeer- of versiebeheerrichtlijnen, documentatie- of naamgevingsconventies)

## 3. Context en reikwijdte

Scheidt je systeem af van (externe) communicatiepartners (aangrenzende systemen en gebruikers). Specificeert de externe
interfaces. Toon het vanuit zakelijk/domeinperspectief (altijd) of technisch perspectief (optioneel)

### Inhoud

Systeemreikwijdte en context scheiden, zoals de naam al zegt, je systeem (dat wil zeggen de reikwijdte) van alle
communicatiepartners (aangrenzende systemen en gebruikers, dat wil zeggen de context van het systeem). Zo
specificeer je de externe interfaces.

Indien nodig, onderscheid de zakelijke context (domeinspecifieke invoer en uitvoer) van de technische context (kanalen, protocollen, hardware).

### Motivatie

De domeininterfaces en technische interfaces naar communicatiepartners behoren tot
de meest kritieke aspecten van je systeem. Zorg ervoor dat je ze volledig begrijpt.

### Vorm

Verschillende mogelijkheden:

- Diverse contextdiagrammen

- Lijsten van communicatiepartners en hun interfaces.

## 3.1 Zakelijke context

### Inhoud

Specificatie van alle communicatiepartners (gebruikers, IT-systemen, …) met uitleg van domeinspecifieke
invoer en uitvoer of interfaces. Optioneel kun je domeinspecifieke formaten of communicatieprotocollen toevoegen.

### Motivatie

Alle belanghebbenden moeten de omgeving van het systeem begrijpen en welke data
worden uitgewisseld.

### Vorm

Alle soorten diagrammen die het systeem als blackbox tonen en de domeininterfaces
naar communicatiepartners specificeren.

Of (aanvullend) een tabel. De titel van de tabel is de naam van je systeem, de drie kolommen bevatten de naam van de communicatiepartner,
de invoer en de uitvoer.

## 3.2 Technische context

### Inhoud

Technische interfaces (kanalen en transmissiemedia) die het systeem met zijn omgeving verbinden. Daarnaast
een mapping van de domeinspecifieke invoer/uitvoer naar de kanalen, dat wil zeggen een uitleg welke invoer en uitvoer welk kanaal gebruikt.

### Motivatie

Veel belanghebbenden nemen architectuurbeslissingen op basis van de technische interfaces tussen het systeem en
zijn context. Met name infrastructuur- of hardwareontwerpers beslissen over deze technische interfaces.

### Vorm

Bijvoorbeeld een UML-deploymentdiagram dat de kanalen naar aangrenzende systemen beschrijft,
samen met een mappingtabel die de relaties tussen kanalen en invoer/uitvoer toont.

## 4. Oplossingsstrategie

Samenvatting van de fundamentele beslissingen en oplossingsstrategieën die de architectuur vormgeven. Kan technologie, ontbinding op het hoogste niveau,
aanpak om de belangrijkste kwaliteitsdoelen te bereiken en relevante organisatorische beslissingen omvatten.

### Inhoud

Een korte samenvatting en uitleg van de fundamentele beslissingen en oplossingsstrategieën die
de systeemarchitectuur vormgeven. Dit omvat

- technologiebeslissingen

- beslissingen over de ontbinding van het systeem op het hoogste niveau, bijvoorbeeld gebruik van architectuurpatronen of ontwerppatronen

- beslissingen over hoe de belangrijkste kwaliteitsdoelen worden bereikt

- relevante organisatorische beslissingen, bijvoorbeeld het kiezen van een ontwikkelproces of het delegeren van bepaalde taken aan derden.

### Motivatie

Deze beslissingen vormen de hoekstenen van je architectuur. Ze zijn de basis voor veel andere gedetailleerde
beslissingen of implementatieregels.

### Vorm

Houd de uitleg van deze kernbeslissingen kort.

Motiveer wat je hebt besloten en waarom je zo hebt besloten op basis van de probleemstelling, de kwaliteitsdoelen en de belangrijkste
beperkingen. Verwijs voor details naar de volgende secties (sectie 5 voor structurele details, sectie 8 voor
transversale aspecten).

Je kunt een lijst of tabel met oplossingsbenaderingen gebruiken.

## 5. Bouwsteenweergave

Statische ontbinding van het systeem, abstracties van broncode, getoond als hiërarchie van
whiteboxen (met daarin blackboxen), tot een passend detailniveau.

### Inhoud

De bouwsteenweergave toont de statische ontbinding van het systeem in bouwstenen (modules, componenten, subsystemen, klassen,
interfaces, pakketten, bibliotheken, frameworks, lagen, partities, tiers, functies, macro's, operaties,
datastructuren, …) en hun afhankelijkheden (relaties, associaties, …)

Deze weergave is verplicht voor elke architectuurdocumentatie. In analogie met een huis
is dit de plattegrond.

### Motivatie

Houd overzicht over je broncode door de structuur begrijpelijk te maken door
middel van abstractie.

Zo kun je op een abstract niveau met je belanghebbenden communiceren zonder
implementatiedetails bloot te leggen.

### Vorm

De bouwsteenweergave is een hiërarchische verzameling blackboxen en whiteboxen
(zie de figuur hieronder) en hun beschrijvingen.

## 5.1 Whitebox van het hele systeem

Hier beschrijf je de ontbinding van het totale systeem met behulp van het volgende whiteboxsjabloon. Het bevat

- een overzichtsdiagram

- een motivatie voor de ontbinding

- blackboxbeschrijvingen van de bevatte bouwstenen. Hiervoor zijn de volgende alternatieven beschikbaar:

  - gebruik één tabel voor een kort en pragmatisch overzicht van alle bevatte bouwstenen en hun interfaces

  - gebruik een lijst van blackboxbeschrijvingen van de bouwstenen volgens het blackboxsjabloon (zie hieronder). Afhankelijk van je tool kan deze lijst bestaan uit subhoofdstukken (tekstbestanden), subpagina's (wiki) of geneste elementen (modelleertools).

  - (optioneel:) belangrijke interfaces die niet in het blackboxsjabloon van een bouwsteen worden beschreven, maar die erg belangrijk zijn om de whitebox te begrijpen.

Omdat er zoveel manieren zijn om interfaces te specificeren, bieden we geen specifiek sjabloon daarvoor.

In het beste geval volstaan voorbeelden of eenvoudige signaturen.

## 5.2 Niveau 2

Hier kun je de binnenstructuur van (sommige) bouwstenen van niveau 1 als whitebox specificeren.

Je moet beslissen welke bouwstenen van je systeem belangrijk genoeg zijn om zo'n gedetailleerde
beschrijving te rechtvaardigen. Geef de voorkeur aan relevantie boven volledigheid.
Specificeer bouwstenen die belangrijk, verrassend, riskant, complex of volatiel zijn.
Laat de gewone, eenvoudige, saaie of gestandaardiseerde delen van je systeem weg

### 5.2.1 Whitebox van bouwsteen 1

...beschrijft de binnenstructuur van bouwsteen 1.

Gebruik het whiteboxsjabloon (zie hierboven).

## 6. Runtimeweergave

Gedrag van bouwstenen als scenario's, die belangrijke gebruiksscenario's of functies, interacties
aan kritieke externe interfaces, operatie en beheer, en fout- en uitzonderingsgedrag omvatten.

### Inhoud

De runtimeweergave beschrijft concreet gedrag en interacties van de bouwstenen van het systeem in de vorm van scenario's uit de volgende gebieden:

- belangrijke gebruiksscenario's of functies: hoe voeren bouwstenen deze uit?

- interacties aan kritieke externe interfaces: hoe werken bouwstenen samen met gebruikers en aangrenzende systemen?

- operatie en beheer: opstarten, starten, stoppen

- fout- en uitzonderingsscenario's

Opmerking: het belangrijkste criterium voor het kiezen van mogelijke scenario's (reeksen, werkstromen) is hun architectonische relevantie. Het is niet belangrijk om een groot aantal scenario's te beschrijven. Je moet eerder een representatieve selectie documenteren.

### Motivatie

Je moet begrijpen hoe (instanties van) bouwstenen van je systeem hun werk doen en communiceren tijdens runtime. Je zult scenario's in de documentatie opnemen, vooral om je architectuur te communiceren aan belanghebbenden die minder actief of minder bedreven zijn in het lezen en begrijpen van de statische modellen (bouwsteenweergave, deploymentweergave).

### Vorm

Er zijn veel notaties voor het beschrijven van scenario's, bijvoorbeeld


- genummerde stappenlijst (in natuurlijke taal)

- activiteitendiagrammen of stroomschema's

- sequentiediagrammen

- BPMN of EPK's (gebeurtenisprocesketens)

- toestandsmachines

- enz.

## 6.n Runtimescenario n (1, 2, 3 enz.)

Voeg een runtimediagram of een tekstuele beschrijving van het scenario in.

Voeg een uitleg in van opmerkelijke aspecten van de interacties tussen de bouwsteeninstanties die in dit diagram worden afgebeeld.

## 7. Deploymentweergave

Technische infrastructuur met omgevingen, computers, processors en topologieën.
Mapping van (software-)bouwstenen naar infrastructuurelementen.

### Inhoud

De deploymentweergave beschrijft:

- de technische infrastructuur die wordt gebruikt om je systeem uit te voeren, met infrastructuurelementen zoals geografische locaties, omgevingen, computers, processors,
  kanalen en netwerktopologieën, evenals andere infrastructuurelementen, en

- de mapping van (software-)bouwstenen naar die infrastructuurelementen.

Vaak draaien systemen in verschillende omgevingen, bijvoorbeeld ontwikkelomgeving, testomgeving, productieomgeving. In dergelijke gevallen moet je alle relevante omgevingen
documenteren.

Documenteer de deploymentweergave met name wanneer je software draait als een gedistribueerd systeem met meer dan één computer, processor, server of container of wanneer je je eigen hardwareprocessors en chips ontwerpt en bouwt.

Vanuit een softwareperspectief volstaat het om de infrastructuurelementen vast te leggen die nodig zijn om de
deployment van bouwstenen te tonen.
Hardwarearchitecten kunnen verder gaan en de infrastructuur beschrijven op elk
detailniveau dat ze nodig vinden. 

### Motivatie

Software draait niet zonder hardware. Deze onderliggende infrastructuur kan en zal van invloed zijn op je systeem en/of sommige
transversale concepten. Daarom moet je de infrastructuur kennen.

### Vorm

Het hoogste niveau van deploymentdiagrammen is al opgenomen in sectie 3.2 als technische context met je eigen
infrastructuur als één enkele blackbox. In deze sectie zoom je in op die blackbox met aanvullende deploymentdiagrammen.

- UML biedt deploymentdiagrammen om die weergave uit te drukken. Gebruik ze, mogelijk met geneste diagrammen,
  wanneer je infrastructuur complexer is.

- Als je (hardware-)belanghebbenden een ander soort diagram verkiezen boven het UML-deploymentdiagram,
  laat hen dan elk soort gebruiken dat nodes en kanalen van de infrastructuur kan tonen.

## 7.1 Infrastructuur niveau 1

Beschrijf (meestal in een combinatie van diagrammen, tabellen en tekst):

- de distributie van een systeem over meerdere locaties, omgevingen, computers, processors enz., evenals de fysieke verbindingen daartussen

- belangrijke rechtvaardiging of motivatie voor deze deploymentstructuur

- kwaliteits- en/of prestatiekenmerken van de infrastructuur

- mapping van softwareartefacten (bouwstenen) naar elementen van de infrastructuur

Voor meerdere omgevingen of alternatieve deployments kopieer je die sectie van arc42 voor alle relevante omgevingen. **

## 7.2 Infrastructuur niveau 2

Dit kan de binnenstructuur van (sommige) infrastructuurelementen van niveau 1 omvatten.

Kopieer de structuur van niveau 1 voor elk geselecteerd element.

## 8. Transversale concepten

Algemene, principiële regelgeving en oplossingsbenaderingen die relevant zijn voor meerdere
delen (→ transversaal) van je systeem. Concepten zijn vaak gerelateerd aan meerdere
bouwstenen. Neem diverse onderwerpen op, zoals domeinmodellen, architectuurpatronen
en -stijlen, regels voor het gebruik van specifieke technologie en implementatieregels.

### Inhoud

Deze sectie beschrijft transversale concepten (praktijken, patronen, regelgeving
of oplossingsideeën). Dergelijke concepten zijn vaak gerelateerd aan meerdere bouwstenen.
Ze kunnen veel verschillende onderwerpen omvatten.

### Motivatie

Concepten vormen de basis voor de conceptuele integriteit (consistentie, homogeniteit) van de architectuur. Daarom zijn
ze een belangrijke bijdrage aan de interne kwaliteit van je systeem.

Dit is de plek die we in het sjabloon hebben gemaakt voor een samenhangende specificatie van dergelijke concepten.

Veel van deze concepten zijn gerelateerd aan of beïnvloeden meerdere bouwstenen.

### Vorm

Het formaat kan variëren:

- conceptpapers met elke structuur

- voorbeeldimplementaties, vooral voor technische concepten

- transversale modeluittreksels of scenario's met de notaties van de architectuurweergaven

### Structuur van deze sectie

Kies alleen de onderwerpen die het meest nodig zijn voor je systeem en geef elk daarvan in deze sectie een kop van niveau 2 (bijvoorbeeld 8.1, 8.2 enz.).

- Probeer niet alle onderwerpen uit het bovengenoemde diagram te behandelen.

### Achtergrond

Sommige onderwerpen binnen een systeem zijn vaak gerelateerd aan meerdere bouwstenen, hardware-
elementen of ontwikkelprocessen. Het kan gemakkelijker zijn om dergelijke transversale onderwerpen op één centrale
plaats te communiceren of te documenteren in plaats van ze te herhalen in de beschrijving van de gerelateerde bouwstenen, hardwareelementen of
ontwikkelprocessen.

Bepaalde concepten kunnen relevant zijn voor alle elementen van het systeem, andere voor slechts enkele.

## 9. Architectuurbeslissingen

Belangrijke, dure, kritieke, grootschalige of risicovolle architectuurbeslissingen, inclusief onderbouwing.

### Inhoud

Belangrijke, dure, grootschalige of risicovolle architectuurbeslissingen, inclusief onderbouwing.
Met "beslissingen" bedoelen we het kiezen van één alternatief op basis van gegeven criteria.

Beslis naar eigen inzicht of je architectuurbeslissingen in deze centrale sectie wilt documenteren of dat je ze liever
lokaal documenteert (bijvoorbeeld binnen het whiteboxsjabloon van een bouwsteen). Vermijd redundante tekst. Raadpleeg sectie 4, die al
de belangrijkste beslissingen van je architectuur bevat.

### Motivatie

Belanghebbenden van je systeem moeten je beslissingen kunnen begrijpen en
herleiden.

### Vorm

- ADR's (architectuurbeslissingsdocumenten) voor elke belangrijke beslissing

- lijst of tabel, geordend op belang en gevolgen, of

- meer gedetailleerd in aparte secties per beslissing

### Achtergrond (over ADR's)

Kleinere stukken documentatie zijn gemakkelijker te lezen, te schrijven en te onderhouden. Over architectuurbeslissingen
kennen ontwikkelteams vaak:

- de beslissing, omdat die bijvoorbeeld in de broncode zichtbaar is, maar

- missen ze de motivatie achter die beslissing (zie Nygard 2011)

Daarom moet je een aantal belangrijke beslissingen met hun motivatie en redenering documenteren

### Ons voorstel voor beslissingen

Houd een verzameling bij van architectonisch significante beslissingen, dat wil zeggen beslissingen die van invloed zijn op de structuur, kwaliteitskenmerken, belangrijke
(vooral externe) afhankelijkheden en interfaces, of constructietechnieken (met dank aan Michael
Nygard voor dit voorstel).

## 10. Kwaliteitseisen

Kwaliteitseisen als scenario's, met een kwaliteitsboom voor een overzicht op hoog niveau.
De belangrijkste kwaliteitsdoelen moeten al zijn beschreven in sectie
1.2 (kwaliteitsdoelen).

### Inhoud

Deze sectie bevat alle relevante kwaliteitseisen.

De belangrijkste daarvan zijn al beschreven in sectie
1.2 (kwaliteitsdoelen), dus je moet er hier alleen naar verwijzen. In deze
sectie 10 moet je ook minder belangrijke kwaliteitseisen opnemen die geen hoge risico's creëren als ze
niet volledig worden bereikt (maar wel leuk zijn om te hebben).

### Motivatie

Omdat kwaliteitseisen veel invloed hebben op architectuurbeslissingen, moet je weten welke kwaliteit
echt belangrijk is voor belanghebbenden, op een concrete en meetbare manier.

### Verdere informatie

Zie het uitgebreide Q42-kwaliteitsmodel op https://quality.arc42.org.

## 10.1 Overzicht van kwaliteitseisen

### Inhoud

Een overzicht of samenvatting van de kwaliteitseisen.

### Motivatie

Vaak heb je te maken met tientallen (zelfs honderden) gedetailleerde kwaliteitseisen.
In deze overzichtssectie moet je proberen ze samen te vatten, bijvoorbeeld door categorieën of onderwerpen te beschrijven (zoals voorgesteld door ISO 25010:2023 of Q42)

Als deze samenvattende beschrijvingen al nauwkeurig, voldoende specifiek
en meetbaar zijn, kun je sectie 10.2 overslaan.

### Vorm

Gebruik een eenvoudige tabel met op elke regel de categorie of het onderwerp en een korte beschrijving van de kwaliteitseis.
Of gebruik een mindmap om deze kwaliteitseisen te structureren.

In de literatuur wordt ook het idee van kwaliteitsattribuutbomen beschreven, die de algemene term "kwaliteit" als wortel hebben en
de term "kwaliteit" in een boomvormige structuur verfijnen.
[Bass+21] introduceerde hiervoor de term "Quality
Attribute Utility Tree".

## 10.2 Kwaliteitsscenario's

### Inhoud

Kwaliteitsscenario's concretiseren kwaliteitseisen en maken het mogelijk te beslissen of ze
(in de zin van acceptatiecriteria) zijn vervuld. Zorg ervoor dat scenario's
specifiek en meetbaar zijn.

Twee soorten scenario's zijn bijzonder nuttig:

- Gebruiksscenario's (ook wel toepassingsscenario's of gebruiksscenario's genoemd) beschrijven de runtimereactie van het systeem op een
  bepaalde stimulus. Dit omvat ook scenario's die de efficiëntie of
  prestaties van het systeem beschrijven.
  Voorbeeld: het systeem reageert binnen één seconde op een verzoek van een gebruiker.

- Wijzigingsscenario's beschrijven het gewenste effect van een wijziging of uitbreiding van het systeem of
  zijn directe omgeving. Voorbeeld: er wordt een extra functie geïmplementeerd of de eisen
  voor een kwaliteitsattribuut veranderen, en de inspanning of duur van de wijziging wordt gemeten.

### Vorm

Typische informatie in gedetailleerde scenario's omvat:

Korte vorm (de voorkeur in het Q42-model):

- Context/achtergrond: wat voor soort systeem of component, en wat is de omgeving of situatie?

- Bron/stimulus: wie of wat start of triggert de actie, reactie of het gedrag.

- Statistiek/acceptatiecriterium: de respons, inclusief schaal of statistiek

De lange vorm van scenario's (de voorkeur van het SEI en [Bass+21]) is gedetailleerder en omvat de volgende informatie:

- Scenario-ID: een unieke identificatie voor het scenario.

- Scenarionaam: een korte, beschrijvende naam voor het scenario.

- Bron: de entiteit (gebruiker, systeem of gebeurtenis) die het scenario initieert.

- Stimulus: de triggerende gebeurtenis of voorwaarde waarop het systeem moet reageren.

- Omgeving: de operationele context of omstandigheden waarin het systeem de stimulus ervaart.

- Artefact: de bouwsteen of het andere element van het systeem dat door de stimulus wordt getroffen.

- Respons: het resultaat of gedrag dat het systeem vertoont als reactie op de stimulus.

- Responsmaat: het criterium of de statistiek waarmee de respons van het systeem wordt beoordeeld.

### Zie ook

Sinds januari 2023 biedt arc42 een pragmatisch kwaliteitsmodel dat voorstelt om kwaliteitseisen te taggen
met hashtags of labels zoals
#flexible, #efficient, #usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Risico's en technische schuld

Bekende technische risico's of technische schuld. Welke potentiële problemen zijn er in of rond het systeem?
Waar heeft het ontwikkelteam last van?

### Inhoud

Een op prioriteit gesorteerde lijst van geïdentificeerde technische risico's of technische schuld

### Motivatie

"Risicomanagement is projectmanagement voor volwassenen" (Tim Lister, Atlantic
Systems Guild.)

Dit moet je motto zijn voor een systematische ontdekking en beoordeling van risico's en technische schuld in de architectuur,
wat managementbelanghebbenden (bijv. projectmanagers, product owners) nodig hebben als onderdeel van de algehele risicoanalyse en maatregelenplanning.

### Vorm

Lijst van risico's en/of technische schuld, eventueel met voorgestelde maatregelen om
de risico's te minimaliseren, te mitigeren of te vermijden of de technische schuld te verminderen.

