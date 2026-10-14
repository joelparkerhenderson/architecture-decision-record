# Päätöstietueen mallipohja: Jeff Tyree ja Art Akerman

Tämä on arkkitehtuuripäätöksen kuvausmallipohja, joka on julkaistu artikkelissa ["Architecture Decisions: Demystifying Architecture", kirjoittajat Jeff Tyree ja Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Ongelma (Issue)**: Kuvaile arkkitehtuurisuunnitteluongelma, johon puutut, jättämättä epäselväksi, miksi puutut tähän ongelmaan juuri nyt. Noudattaen minimalistista lähestymistapaa käsittele ja dokumentoi vain ne ongelmat, jotka vaativat huomiota elinkaaren eri vaiheissa.

* **Päätös (Decision)**: Ilmaise selkeästi arkkitehtuurin suunta — eli valitsemasi kanta.

* **Tila (Status)**: Päätöksen tila, kuten odottaa, päätetty tai hyväksytty.

* **Ryhmä (Group)**: Voit käyttää yksinkertaista ryhmittelyä — kuten integraatio, esitys, data jne. — päätösjoukon jäsentämiseksi. Voit myös käyttää hienostuneempaa arkkitehtuuriontologiaa, kuten John Kyaruzin ja Jan van Katwijkin ontologiaa, joka sisältää abstraktimpia kategorioita kuten tapahtuma, kalenteri ja sijainti. Esimerkiksi tätä ontologiaa käyttäen ryhmittelisit tapahtumiin, joissa järjestelmä tarvitsee tietoa, liittyvät päätökset kategoriaan tapahtuma.

* **Oletukset (Assumptions)**: Kuvaile selkeästi ympäristön taustaoletukset, joissa teet päätöksen — kustannus, aikataulu, teknologia jne. Huomaa, että ympäristön rajoitteet (kuten hyväksytyt teknologiastandardit, yritysarkkitehtuuri, yleisesti käytetyt mallit jne.) voivat rajoittaa harkitsemiasi vaihtoehtoja.

* **Rajoitteet (Constraints)**: Kirjaa kaikki lisärajoitteet ympäristölle, joita valittu vaihtoehto (päätös) saattaa aiheuttaa.

* **Kannat (Positions)**: Luettele harkitsemasi kannat (toteuttamiskelpoiset vaihtoehdot). Nämä vaativat usein pitkiä selityksiä, joskus jopa malleja ja kaavioita. Tämä ei ole tyhjentävä luettelo. Et kuitenkaan halua kuulla kysymystä "Oletko ajatellut...?" loppukatselmoinnissa; tämä johtaa uskottavuuden menetykseen ja muiden arkkitehtuuripäätösten kyseenalaistamiseen. Tämä osio auttaa myös varmistamaan, että kuulit muiden mielipiteet; muiden mielipiteiden selkeä esittäminen auttaa saamaan heidän kannattajansa mukaan päätökseesi.

* **Argumentti (Argument)**: Hahmottele, miksi valitsit kannan, mukaan lukien seikat kuten toteutuskustannus, kokonaisomistuskustannus, markkinoille tuloaika ja tarvittavien kehitysresurssien saatavuus. Tämä on todennäköisesti yhtä tärkeää kuin itse päätös.

* **Seuraukset (Implications)**: Päätöksellä on monia seurauksia, kuten REMAP-metamalli osoittaa. Esimerkiksi päätös voi luoda tarpeen tehdä muita päätöksiä, luoda uusia vaatimuksia tai muuttaa olemassa olevia vaatimuksia; asettaa ympäristölle lisärajoitteita; vaatia laajuuden tai aikataulun uudelleenneuvottelua asiakkaiden kanssa; tai vaatia henkilöstön lisäkoulutusta. Päätöksesi seurausten selkeä ymmärtäminen ja ilmaiseminen voi olla erittäin tehokasta tuen saamisessa ja arkkitehtuurin toteutuksen tiekartan luomisessa.

* **Liittyvät päätökset (Related decisions)**: On ilmeistä, että monet päätökset liittyvät toisiinsa; voit luetella ne tähän. Olemme kuitenkin havainneet, että käytännössä jäljitettävyysmatriisi, päätöspuut tai metamallit ovat hyödyllisempiä. Metamallit ovat hyödyllisiä monimutkaisten suhteiden esittämiseen kaaviona (kuten Rose-mallit).

* **Liittyvät vaatimukset (Related requirements)**: Päätösten tulisi olla liiketoimintalähtöisiä. Osoittaaksesi vastuullisuuden yhdistä päätöksesi selkeästi tavoitteisiin tai vaatimuksiin. Voit luetella nämä liittyvät vaatimukset tähän, mutta olemme havainneet käytännöllisemmäksi viitata jäljitettävyysmatriisiin. Voit arvioida kunkin arkkitehtuuripäätöksen panoksen kunkin vaatimuksen täyttämisessä ja sitten arvioida, kuinka hyvin vaatimus täyttyy kaikkien päätösten yhteisvaikutuksesta. Jos päätös ei edistä vaatimuksen täyttämistä, älä tee kyseistä päätöstä.

* **Liittyvät artefaktit (Related artifacts)**: Luettele liittyvät arkkitehtuuri-, suunnittelu- tai laajuusdokumentit, joihin tämä päätös vaikuttaa.

* **Liittyvät periaatteet (Related principles)**: Jos yrityksellä on sovittu periaatejoukko, varmista, että päätös on johdonmukainen yhden tai useamman niistä kanssa. Tämä auttaa varmistamaan linjauksen toimialueiden tai järjestelmien välillä.

* **Huomiot (Notes)**: Koska päätöksentekoprosessi voi kestää viikkoja, olemme havainneet hyödylliseksi kirjata muistiin huomiot ja ongelmat, joita tiimi käsittelee sosialisointiprosessin aikana.
