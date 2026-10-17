# Funzjonijiet ta' idoneità għad-deċiżjonijiet bħala kodiċi

Il-funzjonijiet ta' idoneità (fitness functions) huma kontrolli awtomatizzati oġġettivi, miktuba bil-kodiċi tal-programmazzjoni, li jivverifikaw li d-deċiżjonijiet qed jinżammu.

- Il-funzjonijiet ta' idoneità jagħmlu d-deċiżjonijiet ittestjabbli u assigurabbli.

- Il-funzjonijiet ta' idoneità għad-deċiżjonijiet jistgħu jgħinu ħafna fl-assigurazzjoni tal-kwalità, fil-proċessi regolatorji, u fl-għanijiet tal-governanza.

## Kif il-funzjonijiet ta' idoneità jieħdu sehem mad-deċiżjonijiet

Rekord ta' deċiżjoni jiddokumenta d-deċiżjoni, filwaqt li funzjoni ta' idoneità tassigura d-deċiżjoni.

- Deċiżjoni b'eżempju: Nużaw l-event sourcing għar-rekwiżiti tal-awditjar.

- Funzjoni ta' idoneità b'eżempju: Nużaw is-server tal-integrazzjoni kontinwa biex nittestjaw li kull bidla fl-istat trid tipproduċi avvenimenti.

## Għaliex il-funzjonijiet ta' idoneità jgħinu d-deċiżjonijiet

Kejl oġġettiv: Il-funzjonijiet ta' idoneità jgħaddu jew jonqsu, għalhekk ix-xogħol jidher u jkun ċar.

Użu kontinwu: Il-funzjonijiet ta' idoneità huma r-regoli ħajjin tiegħek, li jitħaddmu f'kull kommit u build.

Fiduċja biex tagħmel refactoring: Il-funzjonijiet ta' idoneità jaqbdu awtomatikament l-iżbalji fir-regoli tad-deċiżjonijiet.

Governanza skalabbli: Il-funzjonijiet ta' idoneità jassiguraw l-istandards mingħajr ma joħolqu konġestjonijiet.

## Il-funzjonijiet ta' idoneità jistgħu jużaw l-AI?

Il-funzjonijiet ta' idoneità jistgħu jisfruttaw l-LLMs tal-AI għad-deċiżjonijiet billi jistaqsu mistoqsijiet dwar ix-xogħol tiegħek,
bħall-pjanijiet, il-kodiċi, l-iskemi, l-API, u aktar:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Ittestjar tal-unitajiet tal-arkitettura

[ArchUnit](https://www.archunit.org/): iċċekkja r-regoli tal-arkitettura tal-kodiċi Java billi tuża kwalunkwe framework tal-unit test tal-Java sempliċi.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): iċċekkja r-regoli tal-arkitettura tal-kodiċi TypeScript u tal-kodiċi JavaScript billi tuża Jest, Vitest, Jasmine, eċċ.
