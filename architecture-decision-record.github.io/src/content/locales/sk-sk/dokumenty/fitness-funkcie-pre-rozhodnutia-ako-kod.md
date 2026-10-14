# Fitness funkcie pre rozhodnutia ako kód

Fitness funkcie sú objektívne automatizované kontroly, napísané programovým kódom, ktoré overujú, že sa rozhodnutia dodržiavajú.

- Fitness funkcie robia rozhodnutia testovateľnými a zaručiteľnými.

- Fitness funkcie pre rozhodnutia môžu výrazne pomôcť zabezpečeniu kvality, regulačným procesom a cieľom riadenia.

## Ako sa fitness funkcie spájajú s rozhodnutiami

Záznam rozhodnutia dokumentuje rozhodnutie, zatiaľ čo fitness funkcia ho zaručuje.

- Príklad rozhodnutia: Používame event sourcing kvôli požiadavkám na audit.

- Príklad fitness funkcie: Používame server na kontinuálnu integráciu na testovanie, že všetky zmeny stavu musia produkovať udalosti.

## Prečo fitness funkcie pomáhajú rozhodnutiam

Objektívne merania: Fitness funkcie prejdú alebo zlyhajú, takže práca je viditeľná a jasná.

Nepretržité používanie: Fitness funkcie sú vaše živé pravidlá, spúšťané pri každom commite a builde.

Istota pri refaktorovaní: Fitness funkcie automaticky zachytia chyby v pravidlách rozhodnutí.

Škálovateľné riadenie: Fitness funkcie zaručujú štandardy bez vytvárania úzkych miest.

## Môžu fitness funkcie používať AI?

Fitness funkcie môžu využívať AI LLM pre rozhodnutia kladením otázok o vašej práci,
napríklad o vašich plánoch, kóde, schémach, API a ďalšom:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Jednotkové testovanie architektúry

[ArchUnit](https://www.archunit.org/): kontroluje architektonické pravidlá Java kódu pomocou ľubovoľného bežného frameworku na jednotkové testovanie v Jave.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): kontroluje architektonické pravidlá TypeScript kódu a JavaScript kódu pomocou Jest, Vitest, Jasmine a ďalších.
