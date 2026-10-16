# Funkcije ustreznosti za odločitve kot kodo

Funkcije ustreznosti (fitness functions) so objektivna samodejna preverjanja, napisana s programsko kodo, ki preverjajo, da se odločitve upoštevajo.

- Funkcije ustreznosti omogočajo testiranje in zagotavljanje odločitev.

- Funkcije ustreznosti za odločitve lahko močno pomagajo pri zagotavljanju kakovosti, regulativnih postopkih in ciljih upravljanja.

## Kako so funkcije ustreznosti povezane z odločitvami

Zapis odločitve dokumentira odločitev, funkcija ustreznosti pa odločitev zagotavlja.

- Primer odločitve: Za revizijske zahteve uporabljamo dogodkovno shranjevanje (event sourcing).

- Primer funkcije ustreznosti: S strežnikom za neprekinjeno integracijo preizkusimo, da morajo vse spremembe stanja ustvariti dogodke.

## Zakaj funkcije ustreznosti pomagajo odločitvam

Objektivne meritve: Funkcije ustreznosti uspejo ali padejo, zato je delo vidno in jasno.

Neprekinjena uporaba: Funkcije ustreznosti so vaša živa pravila, ki se izvajajo ob vsaki potrditvi in vsaki gradnji.

Zaupanje za preoblikovanje kode: Funkcije ustreznosti samodejno ujamejo napake v pravilih odločitev.

Razširljivo upravljanje: Funkcije ustreznosti zagotavljajo standarde, ne da bi ustvarjale ozka grla.

## Ali lahko funkcije ustreznosti uporabljajo umetno inteligenco?

Funkcije ustreznosti lahko pri odločitvah izkoristijo velike jezikovne modele (LLM) z umetno inteligenco, tako da postavljajo vprašanja o vašem delu,
na primer o načrtih, kodi, shemah, API-jih in drugem:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Testiranje arhitekturnih enot

[ArchUnit](https://www.archunit.org/): preverjajte arhitekturna pravila kode Java z uporabo katerega koli navadnega ogrodja za enotne teste Java.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): preverjajte arhitekturna pravila kode TypeScript in kode JavaScript z uporabo Jest, Vitest, Jasmine itd.
