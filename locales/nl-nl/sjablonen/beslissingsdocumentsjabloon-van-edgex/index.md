# Sjabloon voor architectuurbeslissingsdocument (ADR) <!-- Replace with ADR title -->

Dit is een sjabloon voor EdgeX Foundry ADR's.

Bron: https://docs.edgexfoundry.org/2.3/design/adr/template/


### Indieners

Vermeld de indieners van de ADR.

Formaat:

- Naam (organisatie)


## Wijzigingslogboek

Vermeld wijzigingen in het document, inclusief status, datum en pull-request-URL.

De status is een van: pending, approved, amended, deprecated.

De datum is een ISO 8601-tekenreeks (YYYY-MM-DD).

De PR is de pull request die de wijziging indiende en bevat informatie zoals diffs, bijdragers en beoordelaars.

Formaat:

- \[status van de ADR, bijv. approved, amended enz.\]\(URL van de pull request\) YYYY-MM-DD


## Gerefereerde gebruiksscenario's

Vermeld alle relevante documenten met gebruiksscenario's / eisen.

Een ADR heeft minimaal één relevant en goedgekeurd gebruiksscenario nodig.

Formaat:

- \[Naam van het gebruiksscenario\]\(URL\)

Voeg een uitleg toe als de ADR niet alle eisen van het gebruiksscenario dekt.


## Context

Beschrijf:

- Waarom het ontwerp architectonisch significant is - waarom een ADR nodig is (in plaats van alleen een issue en PR om het probleem op te lossen)

- De hoogwaardige ontwerpaanpak (details komen in het voorgestelde ontwerp hieronder)


## Voorgesteld ontwerp

De details van het ontwerp (zo mogelijk zonder in te gaan op de implementatie).

Overzicht van:

- De services/modules die worden beïnvloed (gewijzigd)

- De nieuwe services/modules die worden toegevoegd

- Impact op modellen en DTO's (wijzigen/toevoegen/verwijderen)

- Impact op API's (wijzigen/toevoegen/verwijderen)

- Impact op algemene configuratie (nieuwe sectie, wijzigen/toevoegen/verwijderen)

- Impact op devops


## Overwegingen

Documenteer alternatieven, zorgen, bijkomende of gerelateerde problemen en vragen die tijdens de ADR-discussie zijn opgeworpen. 

Geef aan of en hoe ze zijn opgelost of gemitigeerd.


## Beslissing

Documenteer belangrijke implementatiedetails waarover overeenstemming is bereikt, kanttekeningen, toekomstige overwegingen en resterende of uitgestelde ontwerpkwesties.

Documenteer de delen van de eisen die niet door het voorgestelde ontwerp worden vervuld.


## Andere gerelateerde ADR's

Vermeld gerelateerde ADR's, bijvoorbeeld ontwerpbeslissingen voor subcomponenten van de functie, ontwerpen die door dit ontwerp zijn komen te vervallen, enz.. 

Formaat:

- \[Titel van de ADR\]\(URL\) - relevantie


## Referenties

Vermeld eventuele aanvullende referenties.

Formaat:

- \[Titel\]\(URL\)

