# Funcții de adecvare pentru decizii ca cod

Funcțiile de adecvare (engl. fitness functions) sunt verificări automate obiective, scrise în cod de programare, care confirmă că deciziile sunt respectate.

- Funcțiile de adecvare fac deciziile testabile și asigurabile.

- Funcțiile de adecvare pentru decizii pot ajuta foarte mult la asigurarea calității, la procesele de reglementare și la obiectivele de guvernanță.

## Cum se leagă funcțiile de adecvare de decizii

O înregistrare a deciziei documentează decizia, în timp ce o funcție de adecvare o asigură.

- Exemplu de decizie: Folosim event sourcing pentru cerințele de audit.

- Exemplu de funcție de adecvare: Folosim serverul de integrare continuă pentru a testa că orice schimbare de stare trebuie să producă evenimente.

## De ce ajută funcțiile de adecvare deciziile

Măsurători obiective: Funcțiile de adecvare trec sau eșuează, deci munca este vizibilă și clară.

Utilizare continuă: Funcțiile de adecvare sunt regulile tale vii, rulate la fiecare commit și build.

Încredere în refactorizare: Funcțiile de adecvare prind automat erorile din regulile deciziilor.

Guvernanță scalabilă: Funcțiile de adecvare asigură standardele fără a crea blocaje.

## Pot funcțiile de adecvare să folosească AI?

Funcțiile de adecvare pot folosi modele lingvistice mari (LLM) AI pentru decizii, adresând întrebări despre munca ta,
cum ar fi planurile, codul, schemele, API-urile și altele:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Testarea unitară a arhitecturii

[ArchUnit](https://www.archunit.org/): verifică regulile de arhitectură ale codului Java folosind orice framework simplu de teste unitare Java.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): verifică regulile de arhitectură ale codului TypeScript și JavaScript folosind Jest, Vitest, Jasmine etc.
