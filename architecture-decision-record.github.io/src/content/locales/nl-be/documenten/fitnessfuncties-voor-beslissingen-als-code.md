# Fitnessfuncties voor beslissingen als code

Een fitnessfunctie is een objectieve, geautomatiseerde controle, geschreven als programmeercode, die verifieert dat een beslissing wordt nagekomen.

- Fitnessfuncties maken beslissingen testbaar en controleerbaar.

- Fitnessfuncties voor beslissingen kunnen enorm helpen bij kwaliteitsborging, regelgevingsprocessen en governancedoelen.

## Hoe fitnessfuncties en beslissingen samenhangen

Een beslissingsdocument legt een beslissing vast; een fitnessfunctie handhaaft die beslissing.

- Voorbeeldbeslissing: gebruik event sourcing voor auditvereisten.

- Voorbeeld van een fitnessfunctie: gebruik een continue-integratieserver om te testen dat elke statuswijziging een gebeurtenis moet genereren.

## Waarom fitnessfuncties beslissingen helpen

Objectieve meting: een fitnessfunctie slaagt of faalt, dus het werk is zichtbaar en duidelijk.

Doorlopend gebruik: een fitnessfunctie is een levende regel en draait bij elke commit en build.

Vertrouwen bij refactoring: een fitnessfunctie vangt fouten tegen de beslissingsregels automatisch op.

Schaalbare governance: een fitnessfunctie handhaaft standaarden zonder knelpunten te creëren.

## Kunnen fitnessfuncties AI gebruiken?

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

## Architectuureenheidstests

[ArchUnit](https://www.archunit.org/): controleer architectuurregels voor Java-code met een gangbaar Java-unittestframework.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): controleer architectuurregels voor TypeScript-code en JavaScript-code met Jest, Vitest, Jasmine en andere.
