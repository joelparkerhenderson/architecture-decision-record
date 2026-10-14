# Fitness funkce pro rozhodnutí jako kód

Fitness funkce (fitness functions) jsou objektivní automatizované kontroly napsané programovým kódem, které ověřují, že se rozhodnutí dodržují.

- Fitness funkce činí rozhodnutí testovatelnými a zajistitelnými.

- Fitness funkce pro rozhodnutí mohou výrazně pomoci při zajištění kvality, regulačních procesech a cílech správy a řízení.

## Jak fitness funkce souvisejí s rozhodnutími

Záznam rozhodnutí dokumentuje rozhodnutí, zatímco fitness funkce ho zajišťuje.

- Příklad rozhodnutí: Pro požadavky na audit používáme event sourcing.

- Příklad fitness funkce: Server kontinuální integrace používáme k testování, že každá změna stavu musí vytvářet události.

## Proč fitness funkce rozhodnutím pomáhají

Objektivní měření: Fitness funkce uspějí nebo selžou, takže práce je viditelná a jasná.

Nepřetržité používání: Fitness funkce jsou vaše živá pravidla, spouštěná při každém commitu a buildu.

Jistota při refaktorování: Fitness funkce automaticky zachytí chyby v pravidlech rozhodnutí.

Škálovatelná správa: Fitness funkce zajišťují standardy bez vytváření úzkých míst.

## Mohou fitness funkce využívat AI?

Fitness funkce mohou pro rozhodnutí využívat velké jazykové modely (LLM) AI tím, že kladou otázky k vaší práci,
například k vašim plánům, kódu, schématům, API a dalším:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Jednotkové testování architektury

[ArchUnit](https://www.archunit.org/): kontrola architektonických pravidel kódu v Javě pomocí libovolného běžného frameworku jednotkových testů pro Javu.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): kontrola architektonických pravidel kódu v TypeScriptu a JavaScriptu pomocí Jest, Vitest, Jasmine atd.
