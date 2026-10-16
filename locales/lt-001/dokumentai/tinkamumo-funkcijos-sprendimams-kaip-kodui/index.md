# Tinkamumo funkcijos sprendimams kaip kodui

Tinkamumo funkcijos (angl. fitness functions) yra objektyvūs automatizuoti patikrinimai, parašyti programavimo kodu, kurie tikrina, ar sprendimų laikomasi.

- Tinkamumo funkcijos leidžia sprendimus išbandyti ir užtikrinti.

- Sprendimų tinkamumo funkcijos gali labai padėti kokybės užtikrinimui, reguliaciniams procesams ir valdysenos tikslams.

## Kaip tinkamumo funkcijos susijusios su sprendimais

Sprendimo įrašas dokumentuoja sprendimą, o tinkamumo funkcija sprendimą užtikrina.

- Sprendimo pavyzdys: audito reikalavimams naudojame įvykių šaltinių modelį (angl. event sourcing).

- Tinkamumo funkcijos pavyzdys: nuolatinės integracijos serveriu tikriname, ar visi būsenos pakeitimai privalo sukurti įvykius.

## Kodėl tinkamumo funkcijos padeda sprendimams

Objektyvūs matavimai: tinkamumo funkcijos arba praeina, arba nepraeina, todėl darbas matomas ir aiškus.

Nuolatinis naudojimas: tinkamumo funkcijos yra jūsų gyvos taisyklės, vykdomos su kiekvienu įkėlimu (angl. commit) ir kūrimu.

Pasitikėjimas pertvarkant kodą: tinkamumo funkcijos automatiškai pagauna sprendimų taisyklių klaidas.

Mastelio keitimą atlaikanti valdysena: tinkamumo funkcijos užtikrina standartus nesukurdamos kliūčių.

## Ar tinkamumo funkcijos gali naudoti dirbtinį intelektą?

Tinkamumo funkcijos sprendimams gali pasitelkti DI didžiuosius kalbos modelius (LLM), užduodamos klausimus apie jūsų darbą,
pavyzdžiui, apie planus, kodą, schemas, API ir kita:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Architektūros vienetų testavimas

[ArchUnit](https://www.archunit.org/): tikrinkite Java kodo architektūros taisykles naudodami bet kurią paprastą Java vienetų testų sistemą.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): tikrinkite TypeScript ir JavaScript kodo architektūros taisykles naudodami Jest, Vitest, Jasmine ir kt.
