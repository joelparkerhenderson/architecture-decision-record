# Ympäristömuuttujien konfigurointi

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

Haluamme sovellustemme olevan konfiguroitavissa artefaktien/binäärien/lähdekoodin ulkopuolella, jotta yksi koonti voi toimia eri tavoin käyttöönottoympäristöstä riippuen.

  * Tämän saavuttamiseksi haluamme käyttää ympäristömuuttujakonfigurointia.

  * Haluamme hallita konfigurointia tiedostoilla, joita voimme versionhallita.

  * Haluamme tarjota jonkin verran kehittäjäkokemuksen ergonomiaa, kuten tiedon siitä, mitä voidaan konfiguroida, ja olennaiset oletusarvot.


### Päätös

Päätettiin .env-tiedostoista, joihin liittyy oletustiedosto ja skeematiedosto.


### Tila

Päätetty. Olemme avoimia uusien ominaisuuksien harkinnalle niiden ilmaantuessa.


## Yksityiskohdat


### Oletukset

Suosimme sovelluskoodin ja ympäristökoodin erottamista. Oletamme, että sovelluksen on toimittava eri tavoin eri ympäristöissä, kuten kehitysympäristössä, testiympäristössä, demoympäristössä, tuotantoympäristössä jne.

Suosimme alan käytäntöä "12 factor app" ja vielä enemmän siihen liittyvää käytäntöä "15 factor app".

Monet aiemmista projekteistamme ovat käyttäneet `.env`-tiedoston tai vastaavan `.env`-hakemiston käytäntöä. On tyypillistä pitää nämä pois versionhallinnasta ja käyttää sen sijaan jotakin muuta tapaa niiden käyttöönottoon, versiointiin ja hallintaan.


### Rajoitteet

Haluamme pitää salaisuudet poissa lähdekoodinhallinta- (SCM) versionhallintajärjestelmästämme (VCS).

Haluamme pyrkiä yhteensopivuuteen suosittujen ohjelmistokehysten ja kirjastojen kanssa. Esimerkiksi Nodessa on moduuli "dotenv" ympäristömuuttujakonfiguroinnin lukemiseen.


### Kannat

Harkitsimme muutamaa lähestymistapaa:

  * Tallenna konfiguraatio sovellukseen, esimerkiksi tiedostoon `config.js`.

  * Tallenna konfiguraatio ympäristöön, esimerkiksi tiedostoon `.env`.

  * Hae konfiguraatio tunnetusta sijainnista, kuten lisenssipalvelimelta.


### Perustelu

Valitsimme .env-tiedoston lähestymistavan, koska:

  * Se on suosittu, myös asiantuntijoiden keskuudessa.

  * Se noudattaa `.env`-tiedostojen mallia, jota tiimimme ovat käyttäneet menestyksekkäästi monta kertaa monissa projekteissa.

  * Se on yksinkertainen. Erityisesti olemme toistaiseksi sinut näkemiemme merkittävien kompromissien kanssa, kuten auditointiominaisuuksien puute verrattuna lisenssipalvelimen lähestymistapaan.


### Seuraukset

Meidän on keksittävä tapa erottaa julkinen ympäristömuuttujakonfigurointi salaisuuksien hallinnasta.


## Liittyvät


### Liittyvät päätökset

Odotamme kaikkien sovellustemme käyttävän tätä lähestymistapaa.

Suunnittelemme päivittävämme kaikki sovelluksemme, jotka käyttävät kykenemättömämpää lähestymistapaa, kuten kovakoodausta binääriin tai lähdekoodiin.

Pidämme sellaisenaan kaikki sovelluksemme, jotka käyttävät kyvykkäämpää lähestymistapaa, kuten lisensointipalvelinta.


### Liittyvät vaatimukset

Lisäämme tiedostoille devops-ominaisuuksia, mukaan lukien koukut, testit ja jatkuvan integroinnin.

Meidän on koulutettava kaikki kehittäjätiimikaverit tähän päätökseen.



### Liittyvät artefaktit

Jokainen alue, johon otamme käyttöön, tarvitsee oman .env-tiedostonsa ja siihen liittyvät tiedostot.


### Liittyvät periaatteet

Helposti peruttavissa.


## Huomiot


Esimerkkitiedosto `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Esimerkkitiedosto `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Esimerkkitiedosto `.env.schema`, jossa vain avaimet:

```env
NAME
EMAIL
```
