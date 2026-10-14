# Lämplighetsfunktioner för beslut som kod

Lämplighetsfunktioner (fitness functions) är objektiva automatiserade kontroller, skrivna med programmeringskod, som verifierar att beslut upprätthålls.

- Lämplighetsfunktioner gör beslut testbara och säkerställbara.

- Lämplighetsfunktioner för beslut kan i hög grad hjälpa kvalitetssäkring, regelefterlevnadsprocesser och styrningsmål.

## Hur lämplighetsfunktioner hänger ihop med beslut

En beslutspost dokumenterar beslutet, medan en lämplighetsfunktion säkerställer beslutet.

- Exempel på beslut: Vi använder event sourcing för granskningskrav.

- Exempel på lämplighetsfunktion: Vi använder servern för kontinuerlig integration för att testa att alla tillståndsändringar måste ge upphov till händelser.

## Varför lämplighetsfunktioner hjälper beslut

Objektiva mätningar: Lämplighetsfunktioner godkänns eller underkänns, så arbetet blir synligt och tydligt.

Kontinuerlig användning: Lämplighetsfunktioner är dina levande regler och körs vid varje commit och bygge.

Förtroende att refaktorera: Lämplighetsfunktioner fångar automatiskt fel i beslutsregler.

Skalbar styrning: Lämplighetsfunktioner säkerställer standarder utan att skapa flaskhalsar.

## Kan lämplighetsfunktioner använda AI?

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

## Enhetstestning av arkitektur

[ArchUnit](https://www.archunit.org/): kontrollera arkitekturregler för Java-kod med valfritt enkelt ramverk för Java-enhetstester.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): kontrollera arkitekturregler för TypeScript-kod och JavaScript-kod med Jest, Vitest, Jasmine och så vidare.
