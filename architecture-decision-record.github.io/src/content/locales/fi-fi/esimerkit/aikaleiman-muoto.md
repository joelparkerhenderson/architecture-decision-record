# Aikaleiman muoto

Sisällys:

* [Yhteenveto](#yhteenveto)
  * [Ongelma](#ongelma)
  * [Päätös](#päätös)
  * [Tila](#tila)
* [Yksityiskohdat](#yksityiskohdat)
  * [Oletukset](#oletukset)
  * [Rajoitteet](#rajoitteet)
  * [Kannat](#kannat)
  * [Perustelu](#perustelu)
  * [Seuraukset](#seuraukset)
* [Liittyvät](#liittyvät)
  * [Liittyvät päätökset](#liittyvät-päätökset)
  * [Liittyvät vaatimukset](#liittyvät-vaatimukset)
  * [Liittyvät artefaktit](#liittyvät-artefaktit)
  * [Liittyvät periaatteet](#liittyvät-periaatteet)
* [Huomiot](#huomiot)


## Yhteenveto


### Ongelma

Haluamme pystyä seuraamaan, milloin asiat tapahtuvat, käyttämällä aikaleimoja ja johdonmukaista aikaleimamuotoa, joka toimii hyvin kaikissa järjestelmissämme ja kolmansien osapuolten järjestelmissä.

Olemme vuorovaikutuksessa järjestelmien kanssa, joilla on erilaiset aikaleimamuodot:

* JSON-viesteillä ei ole natiivia aikaleimamuotoa, joten meidän on valittava, miten aikaleima muunnetaan merkkijonoksi ja merkkijono aikaleimaksi, eli miten serialisoidaan/deserialisoidaan.

* Jotkin sovellukset on asetettu käyttämään paikallista aikaa UTC-ajan sijaan. Tämä voi olla kätevää projekteille, joiden on mukauduttava paikalliseen aikaan, kuten projekteille, jotka laukaisevat paikalliseen aikaan perustuvia tapahtumia.

* Joillakin järjestelmillä on erilaiset aikatarkkuustarpeet ja -kyvyt, kuten sekuntien, millisekuntien tai nanosekuntien aikaresoluutio. Esimerkiksi Linux-käyttöjärjestelmän `date`-komento käyttää oletuksena sekuntien aikatarkkuutta, kun taas Nasdaq-pörssi haluaa oletuksena nanosekuntien aikatarkkuuden.


### Päätös

Valitsemme aikaleiman vakiomuodoksi ISO 8601:n nanosekunnin tarkkuudella, erityisesti "YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ".

Muoto näyttää vuoden, kuukauden, päivän, tunnin, minuutin, sekunnin, nanosekunnit ja Zulu-aikavyöhykkeen eli UTC:n, GMT:n.


### Tila

Päätetty.


## Yksityiskohdat


### Oletukset

Meidän on käsiteltävä nämä aikaleiman merkkijonot, muunnettava aikaleimasta merkkijonoksi (eli serialisoitava) ja merkkijonosta aikaleimaksi (eli deserialisoitava).

Haluamme muodon, joka on yleisesti helppo käyttää, helppo muuntaa ja helppo ihmisen lukea.

Haluamme yhteensopivuuden laajan ulkoisten järjestelmien joukon kanssa, joita emme voi hallita, kuten analytiikkajärjestelmät, tietokantajärjestelmät, rahoitusjärjestelmät.


### Rajoitteet

Joillakin järjestelmillä on aikatarkkuusrajoituksia. Esimerkiksi macOS-käyttöjärjestelmän `date`-komento voi tulostaa aikatarkkuuden sekunteina, mutta ei nanosekunteina.


### Kannat

Harkitsimme useita vaihtoehtoja:

* Unix-epookki eli yksi kasvava luku.

* Tiivis tekstimuoto "YYYYMMDDTHHMMSSNNNNNNNNN".

* Paikallisen aikavyöhykkeen käyttö vs. UTC-aikavyöhyke.


### Perustelu

Tyypillisessä käytössä arvostamme ihmisen helppoa luettavuutta/kirjoitettavuutta enemmän kuin raakaa nopeutta/kokoa.

Tyypillisessä käytössä haluamme muodon, joka toimii hyvin konejärjestelmissä ja myös manuaalisesti, kuten esimerkkidatan kirjoittamisessa, JSON-tulosteen lukemisessa, lokitiedoston grepaamisessa jne.

Epätyypillisessä käytössä, kuten korkean suorituskyvyn laskennassa, odotamme haluavamme optimoida valitsemamme tekstimuodon muuntamalla tekstin nopeampaan muotoon, kuten ohjelmointikielen sisäänrakennettuun päivämääräobjektityyppiin. Siten tekstimuoto ei ole kovin tärkeä HPC:lle.


### Seuraukset

Eri tekstijärjestelmämme ja aikajärjestelmämme lähentyvät tähän muotoon.


## Liittyvät


### Liittyvät päätökset

Voimme haluta nopean/helpon tavan seurata myös aikaeroja eli kestoja. Nämä ovat helppoja Unix-epookin aikaleimoilla.


### Liittyvät vaatimukset

Saatamme haluta muuttaa päätöstämme esim. jos meillä on liittyvä vaatimus tietynlaiselle lokiviestin leimalle, kuten Splunkille, Sumolle, ELK:lle jne.


### Liittyvät artefaktit

Kielikohtaiset muotoilijat ja jäsentimet:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Rosetta Code -esimerkit:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

SixArm-esimerkit:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Liittyvät periaatteet

Helposti peruttavissa. Voimme melko helposti vaihtaa toiseen muotoon, kuten Unix-epookkiin.

Lykkää ennenaikaista optimointia. Tyypillisessä käytössä emme välitä paljon muutamasta ylimääräisestä merkistä, kuten muodosta, joka käyttää tavuviivoja ja kaksoispisteitä.


## Huomiot

Lisää huomiot tähän.
