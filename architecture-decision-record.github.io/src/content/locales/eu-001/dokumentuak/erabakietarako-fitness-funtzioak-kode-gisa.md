# Erabakietarako fitness funtzioak kode gisa

Fitness funtzioak programazio-kodez idatzitako egiaztapen automatizatu objektiboak dira, erabakiak mantentzen ari direla egiaztatzen dutenak.

- Fitness funtzioek erabakiak probagarri eta bermagarri egiten dituzte.

- Erabakietarako fitness funtzioek asko lagun dezakete kalitatearen bermean, arau-prozesuetan eta gobernantza-helburuetan.

## Nola lotzen diren fitness funtzioak erabakiekin

Erabaki-erregistro batek erabakia dokumentatzen du, eta fitness funtzio batek erabakia ziurtatzen du.

- Adibide-erabakia: Gertaeren iturburu-bilketa (event sourcing) erabiltzen dugu ikuskaritza-eskakizunetarako.

- Adibide-fitness funtzioa: Etengabeko integrazioko zerbitzaria erabiltzen dugu egoera-aldaketa guztiek gertaerak sortu behar dituztela probatzeko.

## Zergatik laguntzen dute fitness funtzioek erabakietan

Neurketa objektiboak: Fitness funtzioek gainditu edo huts egiten dute, beraz lana ikusgai eta argia da.

Etengabeko erabilera: Fitness funtzioak zure arau bizidunak dira, commit eta build bakoitzean exekutatzen direnak.

Berregituratzeko konfiantza: Fitness funtzioek erabaki-arauen erroreak automatikoki harrapatzen dituzte.

Eskalagarria den gobernantza: Fitness funtzioek estandarrak ziurtatzen dituzte oztoporik sortu gabe.

## Fitness funtzioek AA erabil dezakete?

Fitness funtzioek AA LLM-en abantaila har dezakete erabakietarako, zure lanari buruzko galderak eginez,
esaterako zure planei, kodeari, eskemei, API-ei eta gehiagori buruz:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Arkitektura-unitate probak

[ArchUnit](https://www.archunit.org/): egiaztatu Java kodearen arkitektura-arauak edozein Java unitate-proba esparru arrunt erabiliz.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): egiaztatu TypeScript eta JavaScript kodearen arkitektura-arauak Jest, Vitest, Jasmine eta abar erabiliz.
