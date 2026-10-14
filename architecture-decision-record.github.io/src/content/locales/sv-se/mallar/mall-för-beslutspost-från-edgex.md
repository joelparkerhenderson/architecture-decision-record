# Mall för arkitekturbeslutspost (ADR) <!-- Replace with ADR title -->

Det här är en mall för ADR:er i EdgeX Foundry.

Källa: https://docs.edgexfoundry.org/2.3/design/adr/template/


### Inlämnare

Lista ADR:ens inlämnare.

Format:

- Namn (Organisation)


## Ändringslogg

Lista ändringarna i dokumentet, inklusive tillstånd, datum och PR-URL.

Tillståndet är något av: pending, approved, amended, deprecated.

Datumet är en ISO 8601-sträng (YYYY-MM-DD).

PR är den pull request som lämnade in ändringen, med information som diff, bidragsgivare och granskare.

Format:

- \[ADR:ens tillstånd, t.ex. approved, amended osv.\]\(URL till pull request\) YYYY-MM-DD


## Refererade användningsfall

Lista alla relevanta dokument om användningsfall / krav.

En ADR kräver minst ett relevant, godkänt användningsfall.

Format:

- \[Användningsfallets namn\]\(URL\)

Lägg till förklaringar om ADR:en inte adresserar alla krav i ett användningsfall.


## Sammanhang

Beskriv:

- hur designen är arkitektoniskt betydelsefull – vilket motiverar en ADR (i stället för ett enkelt ärende och en PR för att åtgärda ett problem)

- den övergripande designansatsen (detaljer beskrivs i den föreslagna designen nedan)


## Föreslagen design

Detaljer om designen (utan att gå in på implementation där det är möjligt).

Disposition:

- tjänster/moduler som påverkas (ändras)

- nya tjänster/moduler som ska läggas till

- påverkan på modell och DTO (ändringar/tillägg/borttagningar)

- påverkan på API (ändringar/tillägg/borttagningar)

- påverkan på allmän konfiguration (inrättande av nya avsnitt, ändringar/tillägg/borttagningar)

- påverkan på devops


## Överväganden

Dokumentera alternativ, farhågor, sidoärenden eller relaterade frågor och frågor som uppstod i debatten om ADR:en. 

Ange om/hur de löstes eller mildrades.


## Beslut

Dokumentera eventuella överenskomna viktiga implementationsdetaljer, förbehåll, framtida överväganden, kvarvarande eller uppskjutna designfrågor.

Dokumentera alla delar av kraven som inte uppfylls av den föreslagna designen.


## Andra relaterade ADR:er

Lista alla relevanta ADR:er – till exempel ett designbeslut för en delkomponent i en funktion, en design som föråldrats till följd av den här designen osv.. 

Format:

- \[ADR-titel\]\(URL\) - Relevans


## Referenser

Lista ytterligare referenser.

Format:

- \[Titel\]\(URL\)

