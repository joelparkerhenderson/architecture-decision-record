# Arkkitehtuuripäätöstietue: tietokantateknologian valinta

## Tila

Hyväksytty

## Konteksti

Suunnittelemme uutta sovellusta, joka vaatii tietojen tallentamista ja hakemista skaalautuvalla ja suorituskykyisellä tavalla. Olemme tunnistaneet kolme yleisesti käytettyä tietokantateknologiatyyppiä: relaatiotietokannat, dokumenttitietokannat ja tapahtumatietokannat.

Relaatiotietokannat tallentavat tietoa taulukoihin, joilla on kiinteät skeemat, ja valvovat tiukkoja tietojen eheyden rajoitteita. Ne sopivat sovelluksiin, jotka vaativat monimutkaisia tietosuhteita ja transaktioita. Esimerkkejä ovat MySQL, PostgreSQL ja Oracle.

Dokumenttitietokannat tallentavat tietoa JSON-tyyppisiin dokumentteihin, eikä niissä ole skeemaa. Ne sopivat hyvin sovelluksiin, jotka vaativat joustavia tietomalleja ja vaakasuuntaista skaalausta. Esimerkkejä ovat MongoDB, Couchbase ja Amazon DynamoDB.

Tapahtumatietokannat tallentavat tietoa tapahtumien sarjana, tallentaen jokaisen tietojen muutoksen. Ne sopivat sovelluksiin, jotka vaativat auditointia, tapahtumalähteistystä (event sourcing) ja monimutkaista tietojenkäsittelyä. Esimerkkejä ovat Apache Kafka, Apache Pulsar ja AWS Kinesis.
Päätös

Sovelluksemme vaatimusten ja rajoitteiden huolellisen arvioinnin jälkeen olemme päättäneet käyttää dokumenttitietokantaa.

## Perustelut

Olemme valinneet dokumenttitietokannan, koska:

1. Sovelluksemme vaatii joustavaa tietomallia, joka voi kehittyä ajan myötä. Dokumenttitietokannat sallivat meidän tallentaa tietoa skeemattomassa muodossa, mikä tarkoittaa, että voimme lisätä uusia kenttiä tai muuttaa olemassa olevien dokumenttien rakennetta muuttamatta tietokannan skeemaa.

2. Sovelluksemme täytyy skaalautua vaakasuunnassa käsitelläkseen suuria tietomääriä ja liikennettä. Dokumenttitietokannat tarjoavat sisäänrakennetun tuen jaolle (sharding) ja replikoinnille, mikä mahdollistaa tietojen jakamisen usealle palvelimelle ja korkean luku- ja kirjoituskapasiteetin käsittelyn.

3. Sovelluksemme vaatii nopeaa ja tehokasta tiedon hakua. Dokumenttitietokannat tarjoavat tehokkaat indeksointi- ja kyselyominaisuudet, joiden avulla voimme hakea tietoa nopeasti ja tehokkaasti.

4. Sovelluksemme ei vaadi monimutkaisia transaktioita tai tietosuhteita. Vaikka relaatiotietokannat ovat erinomaisia tietojen eheyden rajoitteiden valvonnassa ja monimutkaisten transaktioiden käsittelyssä, sovelluksellamme ei ole tällaisia vaatimuksia. Dokumenttitietokannat voivat tarjota riittävät johdonmukaisuuden ja pysyvyyden takeet käyttötapaukseemme.

## Seuraukset

Valitsemalla dokumenttitietokannan meidän on investoitava valitsemamme tietyn teknologian oppimiseen ja ymmärtämiseen. Lisäksi meidän on varmistettava, että sovelluksemme tietomalli sopii hyvin dokumenttitietokannan tietomalliin suorituskyvyn ja skaalautuvuuden maksimoimiseksi.

Uskomme kuitenkin, että dokumenttitietokannan käytön hyödyt ovat kustannuksia suuremmat ja että se sopii parhaiten sovelluksemme vaatimuksiin ja rajoitteisiin.
