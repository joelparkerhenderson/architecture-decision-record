# Beslissingsdocumentsjabloon voor belangrijke technische beslissingen (ITD)

Dit is het sjabloon voor belangrijke technische beslissingen (Important Technical Decisions, ITD) zoals beschreven in
[ITDs: a lean ADR for executive technical decision-making at scale - Ignacio Larrañaga](https://ignaciolarranaga.medium.com/itds-a-lean-adr-for-executive-technical-decision-making-at-scale-e18bb3f6a563).

Een ITD is een gerichte evolutie van de ADR, geoptimaliseerd voor snelheid, duidelijkheid en
validatie door het management. Waar een ADR documenteert wat is besloten, is een ITD een lean,
beslissing-eerst artefact dat de beslissing zelf beoordeelbaar maakt, zodat belanghebbenden het snel kunnen
doorlezen en gemakkelijk kunnen betwisten. ITD's zijn geschikt voor technische beslissingen die niet strikt
over architectuur gaan, zoals het kiezen van een model, een bibliotheek of een CI/CD-strategie.

In elk ITD-bestand schrijf je deze secties:

# Titel

Formuleer de beslissing zelf, niet een beschrijving van het onderwerp.
Bijvoorbeeld "Gebruik Qwen2.5 1.5B Instruct voor vertaling op het apparaat".

## Probleem

Eén zin die beschrijft wat we proberen op te lossen.

## Overwogen opties

De alternatieven die zijn beoordeeld, met de gekozen optie in **vet**.

## Onderbouwing

Alleen de doorslaggevende factoren die tot de keuze hebben geleid, geen
uitputtende lijst van alle voor- en nadelen.

## Opmerkingen

Optioneel. Aanvullende context die het vastleggen waard is, zoals beperkingen, aannames of links.
