# Architectuurbeslissingsdocument (ADR) voor Svelte-componenten

<!--

Prompt:

Architecture decision record for Svelte components.

Compare options: SVAR, Carbon, Flowbite, SkeletonUI, MeltUI, SvelteUI, shadcn-svelte

The goal is full features for table, charts, lists, grids, gantt, 

-->

## Context

We selecteren een Svelte-UI-componentenbibliotheek die volledige functionaliteit biedt voor:
- **Tabellen**
- **Grafieken**
- **Lijsten**
- **Grids**
- **Gantt-diagrammen**

Het doel is een bibliotheek te kiezen die integratiegemak, volledige functieondersteuning, prestaties en onderhoudbaarheid op lange termijn in balans brengt. De opties die worden overwogen zijn:

1. **SVAR**
2. **Carbon**
3. **Flowbite**
4. **SkeletonUI**
5. **MeltUI**
6. **SvelteUI**
7. **shadcn-svelte**

## Analyse van opties

### 1. **SVAR**
- **Overzicht**: SVAR is een moderne, functierijke componentenbibliotheek voor Svelte, gericht op ontwerpsystemen en componenten voor bedrijfsgebruik.
- **Voordelen**:
  - Volledig uitgeruste componenten, waaronder tabellen, formulieren en grafieken.
  - Veel aanpassingsmogelijkheden met ingebouwde themaondersteuning.
  - Ingebouwde ondersteuning voor toegankelijkheid en responsiviteit.
  - Goed gedocumenteerd met bijdragen van de gemeenschap.
- **Nadelen**:
  - Kan zwaarder zijn dan andere eenvoudigere bibliotheken.
  - Beperkte ondersteuning voor specifieke componenten zoals Gantt-diagrammen en geavanceerde grids.
- **Het meest geschikt voor**: applicaties op ondernemingsniveau waar een volledig ontwerpsysteem nodig is.
- **Ondersteuning voor tabellen/grafieken**: matig tot goed.
- **Ondersteuning voor grids/Gantt**: minimaal.

### 2. **Carbon**
- **Overzicht**: Carbon Design System is een open-source ontwerpsysteem van IBM met een robuuste set UI-componenten.
- **Voordelen**:
  - Hoogwaardig, verzorgd ontwerp met uitgebreide documentatie.
  - Zeer toegankelijk en responsief.
  - Grote componentenbibliotheek, waaronder grids, tabellen en formulierbesturingselementen.
- **Nadelen**:
  - Niet gericht op Svelte, dus integratie kan omslachtig zijn.
  - Kan extra aanpassing vereisen voor volledige Svelte-compatibiliteit.
  - Geen kant-en-klare ondersteuning voor geavanceerde componenten zoals Gantt-diagrammen of complexe grafieken.
- **Het meest geschikt voor**: grootschalige projecten die een consistente, verzorgde UI vereisen.
- **Ondersteuning voor tabellen/grafieken**: goed (met integraties van grafiekbibliotheken).
- **Ondersteuning voor grids/Gantt**: goed (gridondersteuning beschikbaar, maar geen Gantt-diagrammen).

### 3. **Flowbite**
- **Overzicht**: Flowbite is een componentenbibliotheek die is gebouwd met Tailwind CSS en verschillende componenten en UI-elementen biedt.
- **Voordelen**:
  - Gebaseerd op Tailwind CSS, wat aanpassing eenvoudig maakt.
  - Gemakkelijk te integreren en te gebruiken met Svelte.
  - Biedt rijke componenten zoals tabellen, grafieken en UI-besturingselementen.
- **Nadelen**:
  - Mist geavanceerde functies (bijv. Gantt-diagrammen of complexe grids).
  - Heeft geen native grafiekcomponenten; leunt op externe bibliotheken.
- **Het meest geschikt voor**: projecten die snelle ontwikkeling vereisen met focus op integratie met Tailwind CSS.
- **Ondersteuning voor tabellen/grafieken**: goed (vereist integratie met grafiekbibliotheken van derden).
- **Ondersteuning voor grids/Gantt**: minimaal.

### 4. **SkeletonUI**
- **Overzicht**: SkeletonUI is een lichtgewicht componentenbibliotheek voor Svelte, gericht op eenvoud en minimalisme.
- **Voordelen**:
  - Extreem lichtgewicht en snel.
  - Eenvoudige en intuïtieve API.
  - Goed voor kleine projecten of waar prestaties kritiek zijn.
- **Nadelen**:
  - Er zijn zeer weinig componenten inbegrepen, dus het is niet functierijk.
  - Mist geavanceerde tabel-/grid-/grafiek-/Gantt-componenten.
  - Beperkte ondersteuning door de gemeenschap en minder uitgebreide documentatie.
- **Het meest geschikt voor**: projecten die lichtgewicht componenten met minimale overhead vereisen.
- **Ondersteuning voor tabellen/grafieken**: minimaal.
- **Ondersteuning voor grids/Gantt**: minimaal.

### 5. **MeltUI**
- **Overzicht**: MeltUI is een verzameling toegankelijke UI-componenten voor Svelte, gericht op eenvoud en samenstelbaarheid.
- **Voordelen**:
  - Lichtgewicht en volledig aanpasbaar.
  - Goede toegankelijkheidsfuncties kant-en-klaar.
  - Modern en minimalistisch ontwerp.
- **Nadelen**:
  - Minder functierijk dan andere bibliotheken.
  - Mist geavanceerde grid- en tabelcomponenten.
  - Geen Gantt-diagrammen of complexe grafiekopties.
- **Het meest geschikt voor**: minimalistische ontwerpen die toegankelijkheid en prestaties vooropstellen.
- **Ondersteuning voor tabellen/grafieken**: minimaal.
- **Ondersteuning voor grids/Gantt**: minimaal.

### 6. **SvelteUI**
- **Overzicht**: SvelteUI is een uitgebreide en aanpasbare UI-componentenbibliotheek voor Svelte, ontworpen voor het bouwen van moderne webapps met een elegante UI.
- **Voordelen**:
  - Uitgebreide set componenten, waaronder tabellen, grids, grafieken en formulieren.
  - Biedt ondersteuning voor zowel lichte als donkere modus.
  - Zeer aanpasbaar en gemakkelijk uit te breiden.
  - Ingebouwde integraties voor grafiekbibliotheken zoals `chart.js` of `d3.js`.
- **Nadelen**:
  - Kan zwaarder zijn dan eenvoudigere componentenbibliotheken.
  - Vereist enige configuratie om externe bibliotheken te integreren voor complexere functies zoals Gantt-diagrammen.
- **Het meest geschikt voor**: projecten die een uitgebreide, aanpasbare set componenten nodig hebben.
- **Ondersteuning voor tabellen/grafieken**: uitstekend (grafiekbibliotheken ondersteund).
- **Ondersteuning voor grids/Gantt**: goed (gridcomponenten beschikbaar; Gantt vereist externe integratie).

### 7. **shadcn-svelte**
- **Overzicht**: een Svelte-versie van ShadCN, dat zich richt op utility-first ontwerp en moderne, gestileerde componenten biedt.
- **Voordelen**:
  - Utility-first ontwerp, gebouwd bovenop Tailwind CSS, waardoor aanpassing eenvoudig is.
  - Rijke set componenten en kant-en-klaar volledig gestileerd.
  - Gemakkelijk te integreren met andere bibliotheken.
- **Nadelen**:
  - Niet zo functiecompleet als sommige andere wat betreft geavanceerde UI-elementen.
  - Mist ingebouwde ondersteuning voor tabellen, grafieken of grids.
  - Geen kant-en-klare ondersteuning voor Gantt-diagrammen.
- **Het meest geschikt voor**: kleine tot middelgrote projecten die een utility-first, aanpasbare aanpak vereisen.
- **Ondersteuning voor tabellen/grafieken**: minimaal.
- **Ondersteuning voor grids/Gantt**: minimaal.

## Beslissing

### Aanbevolen optie: **SvelteUI**

- **Onderbouwing**: SvelteUI biedt een evenwichtige, uitgebreide reeks componenten die tegemoetkomt aan de behoefte aan tabellen, grafieken, grids en formulieren. Het is zeer aanpasbaar, integreert goed met andere grafiekbibliotheken (zoals `chart.js` en `d3.js`) en heeft een goede balans tussen lichtgewicht prestaties en functierijkdom. Hoewel het mogelijk geen kant-en-klare ondersteuning voor Gantt-diagrammen biedt, kan het gemakkelijk worden uitgebreid met integraties van derden, waardoor het ideaal is voor een volledig uitgeruste, schaalbare oplossing.
  
  - **Voordelen**:
    - Uitstekende ondersteuning voor tabellen en grafieken.
    - Volledige grid- en lay-outcomponenten.
    - Aanpasbaar en integreert goed met externe grafiekbibliotheken.
    - Goede gemeenschap en documentatie.
  
  - **Nadelen**:
    - Zwaarder dan sommige andere minimalistische bibliotheken.
    - Heeft externe integratie nodig voor complexe grafieken zoals Gantt-diagrammen.
  
### Alternatief: **Flowbite** of **Carbon** (voor grotere bedrijfsprojecten)
- Als een verzorgd, op Tailwind gebaseerd of consistenter ontwerpsysteem vereist is, kunnen **Flowbite** (met Tailwind CSS) of **Carbon** (voor oplossingen op ondernemingsniveau) geschikte alternatieven zijn. Ze kunnen echter extra inspanning vergen voor integraties met complexere grafieken en componenten.

## Conclusie

De beste match voor je eisen (volledige functionaliteit voor tabellen, grafieken, lijsten, grids, Gantt) is **SvelteUI**, gevolgd door **Flowbite** en **Carbon**, afhankelijk van de projectbehoeften en ontwerpvoorkeuren.
