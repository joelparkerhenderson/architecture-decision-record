# Piemērotības funkcijas lēmumiem kā kodam

Piemērotības funkcijas (fitness functions) ir objektīvas automatizētas pārbaudes, kas uzrakstītas ar programmēšanas kodu un pārbauda, vai lēmumi tiek ievēroti.

- Piemērotības funkcijas padara lēmumus testējamus un nodrošināmus.

- Piemērotības funkcijas lēmumiem var ievērojami palīdzēt kvalitātes nodrošināšanā, regulatīvajos procesos un pārvaldības mērķos.

## Kā piemērotības funkcijas ir saistītas ar lēmumiem

Lēmuma ieraksts dokumentē lēmumu, savukārt piemērotības funkcija nodrošina lēmumu.

- Lēmuma piemērs: revīzijas prasībām mēs izmantojam notikumu avotu izmantošanu (event sourcing).

- Piemērotības funkcijas piemērs: mēs ar nepārtrauktās integrācijas serveri pārbaudām, ka visām stāvokļa izmaiņām jāveido notikumi.

## Kāpēc piemērotības funkcijas palīdz lēmumiem

Objektīvi mērījumi: piemērotības funkcijas izturēs vai neizturēs, tāpēc darbs ir redzams un skaidrs.

Nepārtraukta lietošana: piemērotības funkcijas ir jūsu dzīvie noteikumi, kas tiek izpildīti katrā komitā un būvējumā.

Pārliecība pārveidot kodu: piemērotības funkcijas automātiski uztver lēmumu noteikumu kļūdas.

Mērogojama pārvaldība: piemērotības funkcijas nodrošina standartus, neradot sastrēgumus.

## Vai piemērotības funkcijas var izmantot mākslīgo intelektu?

Piemērotības funkcijas lēmumiem var izmantot mākslīgā intelekta lielos valodas modeļus (LLM), uzdodot jautājumus par jūsu darbu,
piemēram, par jūsu plāniem, kodu, shēmām, API un citu:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Arhitektūras vienībtestēšana

[ArchUnit](https://www.archunit.org/): pārbaudiet Java koda arhitektūras noteikumus, izmantojot jebkuru parasto Java vienībtestu ietvaru.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): pārbaudiet TypeScript koda un JavaScript koda arhitektūras noteikumus, izmantojot Jest, Vitest, Jasmine utt.
