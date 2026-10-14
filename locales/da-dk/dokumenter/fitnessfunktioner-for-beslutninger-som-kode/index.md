# Fitnessfunktioner for beslutninger som kode

En fitnessfunktion er en objektiv, automatiseret kontrol, skrevet som programkode, der verificerer, at en beslutning overholdes.

- Fitnessfunktioner gør beslutninger testbare og kontrollerbare.

- Fitnessfunktioner for beslutninger kan være en stor hjælp til kvalitetssikring, regulatoriske processer og governance-mål.

## Sådan hænger fitnessfunktioner og beslutninger sammen

En beslutningspost dokumenterer en beslutning; en fitnessfunktion håndhæver den beslutning.

- Eksempel på beslutning: brug event sourcing til revisionskrav.

- Eksempel på fitnessfunktion: brug en kontinuerlig integrationsserver til at teste, at enhver tilstandsændring skal generere en hændelse.

## Hvorfor fitnessfunktioner hjælper beslutninger

Objektiv måling: en fitnessfunktion består eller fejler, så arbejdet er synligt og tydeligt.

Løbende brug: en fitnessfunktion er en levende regel og kører ved hver commit og build.

Tillid ved refaktorering: en fitnessfunktion fanger automatisk fejl i forhold til beslutningsreglerne.

Skalerbar governance: en fitnessfunktion håndhæver standarder uden at skabe flaskehalse.

## Kan fitnessfunktioner bruge AI?

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

## Arkitekturenhedstests

[ArchUnit](https://www.archunit.org/): kontrollér arkitekturregler for Java-kode med et almindeligt Java-enhedstestframework.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): kontrollér arkitekturregler for TypeScript-kode og JavaScript-kode med Jest, Vitest, Jasmine og andre.
