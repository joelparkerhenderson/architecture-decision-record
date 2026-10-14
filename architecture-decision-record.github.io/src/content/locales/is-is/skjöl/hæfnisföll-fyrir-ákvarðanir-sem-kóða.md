# Hæfnisföll fyrir ákvarðanir sem kóða

Hæfnisföll eru hlutlægar sjálfvirkar athuganir, skrifaðar með forritunarkóða, sem sannreyna að ákvörðunum sé fylgt.

- Hæfnisföll gera ákvarðanir prófanlegar og tryggjanlegar.

- Hæfnisföll fyrir ákvarðanir geta stórlega hjálpað gæðatryggingu, regluverksferlum og stjórnarháttamarkmiðum.

## Hvernig hæfnisföll tengjast ákvörðunum

Ákvörðunarskrá skjalfestir ákvörðunina, en hæfnisfall tryggir hana.

- Dæmi um ákvörðun: Við notum atburðaupprunann (event sourcing) vegna kröfu um endurskoðunarslóð.

- Dæmi um hæfnisfall: Við notum þjón fyrir samfellda samþættingu til að prófa að allar stöðubreytingar verði að búa til atburði.

## Hvers vegna hæfnisföll hjálpa ákvörðunum

Hlutlægar mælingar: Hæfnisföll standast eða falla, svo vinnan er sýnileg og skýr.

Stöðug notkun: Hæfnisföll eru lifandi reglur þínar, keyrðar við hverja skráningu (commit) og smíði.

Öryggi til að endurskipuleggja kóða: Hæfnisföll grípa sjálfkrafa villur í ákvörðunarreglum.

Stigstærð stjórnarhættir: Hæfnisföll tryggja staðla án þess að skapa flöskuhálsa.

## Geta hæfnisföll notað gervigreind?

Hæfnisföll geta nýtt gervigreindar-tungumálalíkön (LLM) fyrir ákvarðanir með því að spyrja spurninga um vinnuna þína,
svo sem áætlanir, kóða, skema, API og fleira:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Einingaprófanir á arkitektúr

[ArchUnit](https://www.archunit.org/): athugaðu arkitektúrreglur Java-kóða með hvaða venjulega Java-einingaprófunarramma sem er.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): athugaðu arkitektúrreglur TypeScript-kóða og JavaScript-kóða með Jest, Vitest, Jasmine o.fl.
