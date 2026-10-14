# Arkkitehtuuripäätöstietue: ohjelmointikoodin editorit

## Konteksti

Ohjelmointikoodin editorit ovat kehittäjille olennainen työkalu koodin kirjoittamiseen ja muokkaamiseen. Saatavilla on lukuisia koodieditoreja, joilla kullakin on omat ominaisuutensa, etunsa ja haittansa. Tämän ADR-tietueen tarkoituksena on dokumentoida ohjelmointikoodin editoreille tehdyt arkkitehtuuripäätökset.

## Prioriteetit

Ohjelmointikoodin editorien arkkitehtuurin tulisi priorisoida seuraavia:

* **Modulaarisuus**: Koodieditori tulisi suunnitella modulaarisesti, jotta kehittäjät voivat mukauttaa ja laajentaa sitä tarpeen mukaan. Tämä mahdollistaa joustavan arkkitehtuurin, joka voi mukautua eri kehittäjien ja tiimien tarpeisiin.

* **Suorituskyky**: Koodieditorin tulisi olla suorituskykyinen ja reagoiva, jotta kehittäjät voivat työskennellä tehokkaasti käyttämänsä työkalun hidastamatta.

* **Käyttöliittymä**: Käyttöliittymän tulisi olla intuitiivinen ja helppokäyttöinen, jotta kehittäjät voivat keskittyä koodiinsa sen sijaan, että painiskelisivat editorin kanssa.

* **Laajennettavuus**: Koodieditori tulisi suunnitella niin, että sitä voidaan helposti laajentaa kolmansien osapuolten lisäosilla ja integraatioilla.

* **Yhteensopivuus**: Koodieditorin tulisi olla yhteensopiva laajan ohjelmointikielten ja teknologioiden kanssa, mikä tekee siitä hyödyllisen työkalun laajalle kehittäjäjoukolle.

## Päätös

Näiden prioriteettien perusteella ohjelmointikoodin editorien arkkitehtuuri tulisi suunnitella seuraavilla komponenteilla:

* **Ydin**: Tämä komponentti tarjoaa koodieditorin perustoiminnallisuuden, kuten syntaksin korostuksen, tekstin muokkauksen ja tiedostonhallinnan.

* **Käyttöliittymä**: Tämä komponentti tarjoaa koodieditorin käyttöliittymän, mukaan lukien valikot, työkalupalkit ja pikanäppäimet.

* **Lisäosat**: Tämä komponentti sallii kehittäjien laajentaa koodieditorin toiminnallisuutta asentamalla kolmansien osapuolten lisäosia. Lisäosat voivat tarjota lisäominaisuuksia, kuten koodin täydennys, linttaus tai virheenjäljitys.

* **Integraatiot**: Tämä komponentti sallii koodieditorin integroitua muihin työkaluihin ja teknologioihin, kuten versionhallintajärjestelmiin, koontijärjestelmiin tai virheenjäljitystyökaluihin.

## Perustelut

Koodieditorin modulaarisuus sallii kehittäjien mukauttaa ja laajentaa sitä tarpeen mukaan. Tämä on tärkeää, koska eri kehittäjillä ja tiimeillä on erilaiset tarpeet ja työnkulut, ja joustava arkkitehtuuri voi mukautua näihin eroihin.

* **Suorituskyky**: ratkaiseva, koska kehittäjien on voitava työskennellä tehokkaasti työkalujensa hidastamatta. Suorituskykyinen koodieditori on olennainen tuottavuudelle ja voi auttaa kehittäjiä säilyttämään keskittymisensä ja keskittymiskykynsä.

* **Käyttöliittymä**: tärkeä, koska se sallii kehittäjien keskittyä koodiinsa sen sijaan, että painiskelisivat editorin kanssa. Tämä voi johtaa parempaan tuottavuuteen ja vähempään turhautumiseen kehittäjille.

* **Laajennettavuus**: tehokas, koska se sallii koodieditorin mukauttamisen erilaisiin tarpeisiin ja työnkulkuihin. Kolmansien osapuolten lisäosat ja integraatiot voivat tarjota lisäominaisuuksia ja -kykyjä, joita ei ole sisällytetty ydineditoriin.

* **Yhteensopivuus**: arvokas, koska se sallii koodieditorin käytön laajan ohjelmointikielten ja teknologioiden kanssa. Tämä tekee editorista hyödyllisemmän työkalun laajalle kehittäjäjoukolle.

Ydin-, lisäosa-, integraatio- ja käyttöliittymäkomponentit tarjoavat selkeän vastuualueiden erottelun ja mahdollistavat modulaarisen arkkitehtuurin, jota voidaan helposti laajentaa ja mukauttaa. Tämä arkkitehtuuri on joustava, suorituskykyinen ja yhteensopiva laajan ohjelmointikielten ja teknologioiden kanssa, mikä tekee siitä hyödyllisen työkalun kehittäjille.
