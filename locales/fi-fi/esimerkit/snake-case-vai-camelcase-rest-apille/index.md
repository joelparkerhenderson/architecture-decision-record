# Arkkitehtuuripäätöstietue: snake_case vai camelCase REST-rajapinnalle?

Päätös: REST-rajapinnan päätepisteissä käytetään snake_case-nimeämiskäytäntöä

Tila: Hyväksytty

## Konteksti

REST-rajapintojen nimeämiskäytännöissä on kaksi suosittua muotoa: snake_case ja camelCase. Muodossa snake_case jokainen nimen sana erotetaan alaviivoilla, kun taas camelCasessa nimen ensimmäinen sana kirjoitetaan pienellä alkukirjaimella ja seuraavien sanojen ensimmäinen kirjain on iso. Tämä päätös määrittää, mitä nimeämiskäytäntöä REST-rajapinnassa tulisi käyttää.

## Päätöksen ajurit

- Yhdenmukaisuus projektin olemassa olevien nimeämiskäytäntöjen kanssa

- Luettavuus ja selkeys kaikille, jotka voivat työskennellä rajapinnan parissa

- Yhdenmukaisuus alan parhaiden käytäntöjen kanssa REST-rajapintojen nimeämiskäytännöissä

- Toteutuksen ja ylläpidon helppous

## Päätös

REST-rajapinnan päätepisteissä käytetään snake_case-nimeämiskäytäntöä. Tämän valinnan ajavat seuraavat tekijät:

1. **Yhdenmukaisuus**: Projekti käyttää jo snake_case-nimeämiskäytäntöä kaikissa päätepisteissä, ja olisi hyödyllistä säilyttää tämä käytäntö yhdenmukaisuuden varmistamiseksi koko projektissa.

2. **Luettavuus ja selkeys**: snake_case-käytäntö on luettavampi ja helpommin ymmärrettävä. Alaviivat tarjoavat selkeän erottelun sanojen välillä, mikä helpottaa nimen jäsentämistä ja merkityksen ymmärtämistä.

3. **Yhdenmukaisuus alan parhaiden käytäntöjen kanssa**: snake_case-käytäntöä käytetään laajasti alalla ja sitä pidetään parhaana käytäntönä REST-rajapinnoille, mikä tekee siitä hyvän valinnan projektille.

4. **Toteutuksen ja ylläpidon helppous**: Olemassa olevan nimeämiskäytännön noudattaminen on helpompi toteuttaa ja ylläpitää, koska kaikki olemassa oleva koodi ja dokumentaatio olisi päivitettävä, jos valittaisiin uusi käytäntö.

## Seuraukset

Tällä päätöksellä on mahdollisia seurauksia. 

* Jos projektiin liittyvät uudet tiimin jäsenet eivät tunne snake_case-nimeämiskäytäntöä, se voi johtaa sekaannukseen ja virheisiin kehityksessä. Koska snake_case on kuitenkin laajasti käytetty käytäntö, tällainen riski on vähäinen. 
  
* Jos projektissa käytetään muita työkaluja tai kehyksiä, jotka perustuvat vahvasti camelCase-käytäntöön, nimeämiskäytäntöjen välillä muuntaminen voi vaatia lisävaivaa. Se ei kuitenkaan ole merkittävä huolenaihe, koska projekti on vakiinnuttanut snake_case-käytännön. 
 
Kaiken kaikkiaan päätös käyttää snake_case-nimeämiskäytäntöä REST-rajapinnan päätepisteissä johtaa johdonmukaiseen, luettavaan ja alan standardin mukaiseen lähestymistapaan, joka on helppo toteuttaa ja ylläpitää.

<h6>Kunnianosoitus: tämän sivun on luonut ChatGPT, minkä jälkeen sitä on muokattu selkeyden ja muodon vuoksi.</h6>
