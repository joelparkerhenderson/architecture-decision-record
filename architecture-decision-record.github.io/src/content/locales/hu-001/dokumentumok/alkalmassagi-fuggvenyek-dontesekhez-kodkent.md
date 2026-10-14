# Alkalmassági függvények döntésekhez kódként

Az alkalmassági függvények (fitness functions) objektív, automatizált ellenőrzések, programkóddal írva, amelyek igazolják, hogy a döntéseket betartják.

- Az alkalmassági függvények tesztelhetővé és biztosíthatóvá teszik a döntéseket.

- A döntésekhez tartozó alkalmassági függvények nagyban segíthetik a minőségbiztosítást, a szabályozási folyamatokat és az irányítási célokat.

## Hogyan kapcsolódnak az alkalmassági függvények a döntésekhez

A döntési feljegyzés dokumentálja a döntést, míg az alkalmassági függvény biztosítja azt.

- Példa döntés: Eseményforrást (event sourcing) használunk az auditkövetelmények miatt.

- Példa alkalmassági függvény: A folyamatos integrációs kiszolgálóval teszteljük, hogy minden állapotváltozásnak eseményeket kell létrehoznia.

## Miért segítenek az alkalmassági függvények a döntéseken

Objektív mérések: Az alkalmassági függvények sikeresek vagy sikertelenek, így a munka látható és világos.

Folyamatos használat: Az alkalmassági függvények az Ön élő szabályai, minden commitnál és buildnél lefutnak.

Magabiztosság az újraszervezésben: Az alkalmassági függvények automatikusan elkapják a döntési szabályok hibáit.

Skálázható irányítás: Az alkalmassági függvények szűk keresztmetszetek létrehozása nélkül biztosítják a szabványokat.

## Használhatnak-e az alkalmassági függvények mesterséges intelligenciát?

Az alkalmassági függvények kihasználhatják az MI nagy nyelvi modelljeit (LLM) a döntésekhez, kérdéseket téve fel a munkájáról,
például a terveiről, a kódjáról, a sémáiról, az API-iról és egyebekről:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Architektúra egységtesztelése

[ArchUnit](https://www.archunit.org/): Java-kód architekturális szabályainak ellenőrzése bármely egyszerű Java egységtesztelő keretrendszerrel.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): TypeScript- és JavaScript-kód architekturális szabályainak ellenőrzése Jest, Vitest, Jasmine stb. használatával.
