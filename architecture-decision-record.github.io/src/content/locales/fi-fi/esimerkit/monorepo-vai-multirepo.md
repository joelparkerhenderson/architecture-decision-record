# Monorepo vai multirepo

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

Projektimme sisältää kolmen pääkategorian ohjelmiston kehittämisen:

  * Käyttöliittymät (front-end GUI)
  * Välikerroksen palvelut (middleware)
  * Taustapalvelimet (back-end)

Kehittäessämme lähdekoodinhallinta- (SCM) versionhallintajärjestelmämme (VCS) on git.

Meidän on valittava, miten käytämme gitiä koodimme järjestämiseen.

Ylimmän tason valinta on järjestää "monorepoksi" tai "polyrepoksi" tai "hybridiksi":

  * Monorepo tarkoittaa, että laitamme kaikki osat yhteen suureen tietovarastoon
  * Polyrepo tarkoittaa, että laitamme jokaisen osan omaan tietovarastoonsa
  * Hybridi tarkoittaa jonkinlaista sekoitusta monorepoa ja polyrepoa

Lisätietoja varten katso https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Päätös

Monorepo, kun organisaatio/tiimi/projekti on suhteellisen pieni ja nopea iterointi on tärkeämpää kuin vakauden ylläpito.

Polyrepo, kun organisaatio/tiimi/projekti on suhteellisen suuri ja vakauden ylläpito on tärkeämpää kuin nopea iterointi.


### Tila

Päätetty. Olemme avoimia uudelleenarvioinnille, jos/kun monorepojen ja/tai polyrepojen hallintaan tulee uusia työkaluja.


## Yksityiskohdat


### Oletukset

Kaikki kehittämämme koodi on yhden organisaation tuotteita varten, ei suurelle yleisölle. Eli Välittäjä-Kauppiaan tavoitteena ei ole saada mitään yleisön vapaaehtoisten kehittäjien kaltaista.


### Rajoitteet

Rajoitteet on dokumentoitu hyvin osoitteessa https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Kannat

Harkitsimme monorepoja Googlen, Facebookin jne. tyyliin. Uskomme, että mahdolliset monorepon skaalausongelmat ovat niin kaukana tulevaisuudessa, että pystymme hyödyntämään samoja käytäntöjä kuin Google ja Facebook siihen mennessä, kun tarvitsemme niitä.

Harkitsimme polyrepoja tyypillisten Git-avoimen lähdekoodin projektien tyyliin, kuten Google Android, Facebook React jne. Uskomme, että nämä ovat paras valinta yleisön osallistumiseen (esim. kuka tahansa maailmassa voi työskennellä koodin parissa) ja yksittäiseen saatavuuteen (esim. projektia käytetään sellaisenaan ilman muita osia).


### Perustelu

Kun organisaatio/tiimi/projekti on suhteellisen pieni, valitsemme monorepon, koska nopea iterointi on merkittävästi tärkeämpää kuin vakauden ylläpito

Kun organisaatio/tiimi/projekti on suhteellisen suuri, valitsemme polyrepon, koska vakauden ylläpito on merkittävästi tärkeämpää kuin nopea iterointi.


### Seuraukset

Jos CI+CD-putki on jo olemassa, meidän on ehkä mukautettava sitä usean projektin testaamiseksi yhdessä tietovarastossa.

CI+CD voi kestää kauemmin monorepon täydellä koonnilla, koska CI+CD voi koota kaikki monorepon projektit.

Jos organisaatio/tiimi/projekti kasvaa, monorepolla on skaalausongelmia.

Monorepon skaalausongelmat voivat tehdä siirtymisestä polyrepoon yhä arvokkaampaa.

Siirtyminen monorepoista polyrepoon on merkittävä devops-tehtävä, ja se on suunniteltava, hallittava ja ohjelmoitava.


## Liittyvät


### Liittyvät päätökset

Teemme päätöksiä liittyvistä työkaluista monorepojen (esim. Google Bazel) ja polyrepojen (esim. Lyft Refactorator) hallintaan.


### Liittyvät vaatimukset

Meidän on kehitettävä CI+CD-putki toimimaan hyvin gitin kanssa.


### Liittyvät artefaktit

Odotamme, että tietovarastojen organisointiin liittyy artefakteja provisiointia, konfiguraationhallintaa, testausta ja vastaavia devops-alueita varten. 


### Liittyvät periaatteet

Helposti peruttavissa. Jos monorepo ei toimi käytännössä tai johto ei halua sitä, on helppo vaihtaa polyrepoon.

Asiakaspakkomielle. Arvostamme projektin saamista asiakkaiden käsiin, ja uskomme, että monorepo voi viedä meidät sinne nopeammin kuin polyrepo ja auttaa meitä myös iteroimaan nopeammin.

Ajattele isosti. Google ja Facebook ovat erittäin vahvoja monorepojen kannattajia polyrepojen sijaan, koska kaikkia ydintuotteita voidaan kehittää/testata/ottaa käyttöön yhdessä.


## Huomiot

Lisää huomiot tähän.
