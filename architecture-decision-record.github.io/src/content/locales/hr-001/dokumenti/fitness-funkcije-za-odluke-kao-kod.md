# Fitness funkcije za odluke kao kod

Fitness funkcije su objektivne automatizirane provjere, napisane programskim kodom, koje potvrđuju da se odluke održavaju.

- Fitness funkcije čine odluke provjerljivima i osiguranima.

- Fitness funkcije za odluke mogu uvelike pomoći osiguranju kvalitete, regulatornim procesima i ciljevima upravljanja.

## Kako se fitness funkcije povezuju s odlukama

Zapis odluke dokumentira odluku, dok fitness funkcija osigurava odluku.

- Primjer odluke: Koristimo event sourcing zbog zahtjeva revizije.

- Primjer fitness funkcije: Koristimo poslužitelj za kontinuiranu integraciju kako bismo testirali da sve promjene stanja moraju proizvoditi događaje.

## Zašto fitness funkcije pomažu odlukama

Objektivna mjerenja: Fitness funkcije prolaze ili padaju, pa je rad vidljiv i jasan.

Kontinuirana upotreba: Fitness funkcije su vaša živa pravila, pokreću se pri svakom commitu i buildu.

Povjerenje za refaktoriranje: Fitness funkcije automatski hvataju pogreške u pravilima odluka.

Skalabilno upravljanje: Fitness funkcije osiguravaju standarde bez stvaranja uskih grla.

## Mogu li fitness funkcije koristiti umjetnu inteligenciju?

Fitness funkcije mogu koristiti AI LLM-ove za odluke postavljanjem pitanja o vašem radu,
poput vaših planova, koda, shema, API-ja i drugog:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Jedinično testiranje arhitekture

[ArchUnit](https://www.archunit.org/): provjerava arhitekturna pravila Java koda pomoću bilo kojeg običnog okvira za jedinično testiranje u Javi.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): provjerava arhitekturna pravila TypeScript koda i JavaScript koda pomoću Jesta, Vitesta, Jasmine i drugih.
