# Sopivuusfunktiot koodina ilmaistuille päätöksille

Sopivuusfunktiot (fitness functions) ovat objektiivisia automaattisia tarkistuksia, jotka on kirjoitettu ohjelmointikoodilla ja jotka varmistavat, että päätöksiä noudatetaan.

- Sopivuusfunktiot tekevät päätöksistä testattavia ja varmistettavia.

- Päätösten sopivuusfunktiot voivat auttaa suuresti laadunvarmistuksessa, sääntelyprosesseissa ja hallintotavoitteissa.

## Miten sopivuusfunktiot liittyvät päätöksiin

Päätöstietue dokumentoi päätöksen, kun taas sopivuusfunktio varmistaa päätöksen.

- Esimerkkipäätös: Käytämme tapahtumalähteistystä (event sourcing) auditointivaatimusten vuoksi.

- Esimerkkisopivuusfunktio: Käytämme jatkuvan integroinnin palvelinta testaamaan, että kaikkien tilamuutosten on tuotettava tapahtumia.

## Miksi sopivuusfunktiot auttavat päätöksiä

Objektiiviset mittaukset: Sopivuusfunktiot joko läpäisevät tai epäonnistuvat, joten työ on näkyvää ja selkeää.

Jatkuva käyttö: Sopivuusfunktiot ovat elävät sääntösi, jotka ajetaan jokaisella commitilla ja koonnilla.

Varmuus refaktorointiin: Sopivuusfunktiot havaitsevat päätössääntöjen virheet automaattisesti.

Skaalautuva hallinto: Sopivuusfunktiot varmistavat standardit luomatta pullonkauloja.

## Voivatko sopivuusfunktiot käyttää tekoälyä?

Sopivuusfunktiot voivat hyödyntää tekoälyn suuria kielimalleja (LLM) päätösten arvioinnissa esittämällä kysymyksiä työstäsi,
kuten suunnitelmistasi, koodistasi, skeemoistasi, rajapinnoistasi ja muusta:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Arkkitehtuurin yksikkötestaus

[ArchUnit](https://www.archunit.org/): tarkista Java-koodin arkkitehtuurisäännöt käyttämällä mitä tahansa tavallista Javan yksikkötestauskehystä.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): tarkista TypeScript-koodin ja JavaScript-koodin arkkitehtuurisäännöt käyttämällä Jestiä, Vitestiä, Jasminea jne.
