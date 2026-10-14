# Otsuste sobivusfunktsioonid koodina

Sobivusfunktsioon (fitness function) on objektiivne, automatiseeritud kontroll, mis on kirjutatud programmeerimiskoodina ja mis kontrollib, et otsust järgitakse.

- Sobivusfunktsioonid muudavad otsused testitavaks ja tagatavaks.

- Otsuste sobivusfunktsioonid võivad suuresti aidata kvaliteeditagamisel, regulatiivsetes protsessides ja juhtimiseesmärkides.

## Kuidas sobivusfunktsioonid ja otsused seostuvad

Otsusekirje dokumenteerib otsuse; sobivusfunktsioon jõustab selle otsuse.

- Näide otsusest: kasuta auditinõuete jaoks sündmuste allikat (event sourcing).

- Näide sobivusfunktsioonist: kasuta pidevintegratsiooni serverit, et testida, et iga olekumuudatus peab genereerima sündmuse.

## Miks sobivusfunktsioonid otsuseid aitavad

Objektiivne mõõtmine: sobivusfunktsioon kas läbib või ebaõnnestub, seega on töö nähtav ja selge.

Pidev kasutus: sobivusfunktsioon on elav reegel ja jookseb igal commitil ja ehitusel.

Kindlus refaktoreerimisel: sobivusfunktsioon tabab otsusereeglite vastu eksimisi automaatselt.

Skaleeritav juhtimine: sobivusfunktsioon jõustab standardeid kitsaskohti tekitamata.

## Kas sobivusfunktsioonid saavad kasutada tehisintellekti?

Sobivusfunktsioon võib otsuste jaoks kasutada tehisintellekti LLM-i, esitades küsimusi
meie töö kohta, näiteks plaanid, kood, skeemid, API-d ja nii edasi:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Arhitektuuri ühikutestid

[ArchUnit](https://www.archunit.org/): kontrolli Java koodi arhitektuurireegleid tavalise Java ühikutestide raamistikuga.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): kontrolli TypeScripti koodi ja JavaScripti koodi arhitektuurireegleid Jesti, Vitesti, Jasmine'i ja teistega.
