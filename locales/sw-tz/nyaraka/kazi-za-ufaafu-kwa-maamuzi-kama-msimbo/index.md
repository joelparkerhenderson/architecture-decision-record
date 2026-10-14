# Kazi za ufaafu kwa maamuzi kama msimbo

Kazi za ufaafu (fitness functions) ni ukaguzi wa kiotomatiki wa kiobjektivu, ulioandikwa kwa msimbo wa programu, unaothibitisha kwamba maamuzi yanadumishwa.

- Kazi za ufaafu hufanya maamuzi yaweze kujaribiwa na kuhakikishwa.

- Kazi za ufaafu kwa maamuzi zinaweza kusaidia sana uhakikisho wa ubora, michakato ya udhibiti, na malengo ya usimamizi.

## Jinsi kazi za ufaafu zinavyohusiana na maamuzi

Rekodi ya uamuzi huandika uamuzi, huku kazi ya ufaafu ikihakikisha uamuzi.

- Mfano wa uamuzi: Tunatumia event sourcing kwa mahitaji ya ukaguzi.

- Mfano wa kazi ya ufaafu: Tunatumia seva ya ujumuishaji endelevu kujaribu kwamba mabadiliko yote ya hali lazima yazalishe matukio.

## Kwa nini kazi za ufaafu husaidia maamuzi

Vipimo vya kiobjektivu: Kazi za ufaafu hufaulu au hushindwa, kwa hivyo kazi huonekana na iko wazi.

Matumizi endelevu: Kazi za ufaafu ni kanuni zako hai, zinazoendeshwa kwa kila commit na ujenzi.

Kujiamini kurekebisha msimbo: Kazi za ufaafu hunasa kiotomatiki makosa ya kanuni za maamuzi.

Usimamizi unaoweza kupanuka: Kazi za ufaafu huhakikisha viwango bila kuunda vikwazo.

## Je, kazi za ufaafu zinaweza kutumia akili bandia?

Kazi za ufaafu zinaweza kutumia modeli kubwa za lugha za akili bandia (LLM) kwa maamuzi kwa kuuliza maswali kuhusu kazi yako,
kama vile mipango yako, msimbo, skima, API, na zaidi:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Majaribio ya kitengo ya usanifu

[ArchUnit](https://www.archunit.org/): kagua kanuni za usanifu za msimbo wa Java kwa kutumia mfumo wowote wa kawaida wa majaribio ya kitengo wa Java.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): kagua kanuni za usanifu za msimbo wa TypeScript na msimbo wa JavaScript kwa kutumia Jest, Vitest, Jasmine, n.k.
