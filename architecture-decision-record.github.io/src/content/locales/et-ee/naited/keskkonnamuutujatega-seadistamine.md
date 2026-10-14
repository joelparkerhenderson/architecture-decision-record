# Keskkonnamuutujatega seadistamine

Sisukord:

* [Kokkuvõte](#kokkuvõte)
  * [Küsimus](#küsimus)
  * [Otsus](#otsus)
  * [Olek](#olek)
* [Üksikasjad](#üksikasjad)
  * [Eeldused](#eeldused)
  * [Piirangud](#piirangud)
  * [Seisukohad](#seisukohad)
  * [Argument](#argument)
  * [Tagajärjed](#tagajärjed)
* [Seotud](#seotud)
  * [Seotud otsused](#seotud-otsused)
  * [Seotud nõuded](#seotud-nõuded)
  * [Seotud artefaktid](#seotud-artefaktid)
  * [Seotud põhimõtted](#seotud-põhimõtted)
* [Märkmed](#märkmed)


## Kokkuvõte


### Küsimus

Tahame, et meie rakendused oleksid seadistatavad väljaspool artefakte/binaarfaile/lähtekoodi, nii et üks ehitus võiks käituda erinevalt sõltuvalt oma kasutuselevõtukeskkonnast.

  * Selle saavutamiseks tahame kasutada keskkonnamuutujatega seadistamist.

  * Tahame seadistust hallata failidega, mida saame versioonihaldusse panna.

  * Tahame pakkuda mõningast arendajakogemuse ergonoomikat, näiteks teadmist, mida saab seadistada, ja asjakohaseid vaikeväärtusi.


### Otsus

Otsustasime .env-failide kasuks koos seotud vaikeväärtuste faili ja skeemifailiga.


### Olek

Otsustatud. Oleme avatud uute võimaluste kaalumisele, kui need ilmnevad.


## Üksikasjad


### Eeldused

Eelistame rakenduse koodi ja keskkonnakoodi eraldamist. Eeldame, et rakendus peab erinevates keskkondades töötama erinevalt, nagu arenduskeskkond, testimiskeskkond, demokeskkond, tootmiskeskkond jne.

Eelistame valdkonna tava "12 factor app" ja veelgi enam sellega seotud tava "15 factor app".

Paljud meie varasemad projektid on kasutanud `.env`-faili või sarnase `.env`-kausta konventsiooni. On tavaline hoida neid versioonihaldusest väljas ja kasutada nende kasutusele võtmiseks, versioonimiseks ja haldamiseks mõnda muud viisi.


### Piirangud

Tahame hoida saladused oma lähtekoodihalduse (SCM) versioonihaldussüsteemist (VCS) väljas.

Püüame ühilduda populaarsete tarkvararaamistike ja -teekidega. Näiteks Node'il on moodul "dotenv" keskkonnamuutujatega seadistuse lugemiseks.


### Seisukohad

Kaalusime mõningaid lähenemisi:

  * Salvestada seadistus rakenduses, näiteks failis `config.js`.

  * Salvestada seadistus keskkonnas, näiteks failis `.env`.

  * Tuua seadistus tuntud asukohast, näiteks litsentsiserverist.


### Argument

Valisime .env-faili lähenemise, sest:

  * See on populaarne, ka ekspertide seas.

  * See järgib `.env`-failide mustrit, mida meie meeskonnad on paljudes projektides edukalt palju kordi kasutanud.

  * See on lihtne. Eelkõige oleme praegu rahul oluliste kompromissidega, mida näeme, nagu auditivõimaluste puudumine võrreldes litsentsiserveri lähenemisega.


### Tagajärjed

Peame välja mõtlema viisi, kuidas eraldada avalik keskkonnamuutujatega seadistus saladuste haldusest.


## Seotud


### Seotud otsused

Eeldame, et kõik meie rakendused kasutavad seda lähenemist.

Plaanime uuendada kõik oma rakendused, mis kasutavad vähem võimekat lähenemist, näiteks kõvakodeerimist binaarfailis või lähtekoodis.

Jätame muutmata kõik oma rakendused, mis kasutavad võimekamat lähenemist, näiteks litsentsiserverit.


### Seotud nõuded

Lisame failide jaoks devopsi võimalused, sealhulgas konksud, testid ja pideva integratsiooni.

Peame koolitama kõiki arendajatest meeskonnakaaslasi selle otsuse osas.



### Seotud artefaktid

Iga ala, kuhu me kasutusele võtame, vajab oma .env-faili ja seotud faile.


### Seotud põhimõtted

Hõlpsasti tagasipööratav.


## Märkmed


Näidisfail `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Näidisfail `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Näidisfail `.env.schema` ainult võtmetega:

```env
NAME
EMAIL
```
