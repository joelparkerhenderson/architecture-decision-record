# AWS:n arkkitehtuuripäätöstietueiden prosessi

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Arkkitehtuuripäätöstietue (ADR) on dokumentti, joka kuvaa valinnan, jonka tiimi tekee jostakin merkittävästä rakentamansa ohjelmistoarkkitehtuurin osa-alueesta. Jokainen ADR-tietue kuvaa arkkitehtuuripäätöksen, sen kontekstin ja sen seuraukset. ADR-tietueilla on tiloja, ja siksi ne noudattavat elinkaarta. Esimerkki ADR-tietueesta löytyy liitteestä.

ADR-prosessin tuloksena syntyy kokoelma arkkitehtuuripäätöstietueita. Tämä kokoelma muodostaa päätöslokin. Päätösloki tarjoaa projektin kontekstin sekä yksityiskohtaista tietoa toteutuksesta ja suunnittelusta. Projektin jäsenet silmäilevät kunkin ADR-tietueen otsikoita saadakseen yleiskuvan projektin kontekstista. He lukevat ADR-tietueet perehtyäkseen syvällisesti projektin toteutuksiin ja suunnitteluvalintoihin.

Kun tiimi hyväksyy ADR-tietueen, siitä tulee muuttumaton. Jos uudet oivallukset edellyttävät toista päätöstä, tiimi ehdottaa uutta ADR-tietuetta. Kun tiimi hyväksyy uuden ADR-tietueen, se korvaa edellisen ADR-tietueen.

## ADR-prosessin laajuus

Projektin jäsenten tulisi luoda ADR-tietue jokaisesta arkkitehtuurin kannalta merkittävästä päätöksestä, joka vaikuttaa ohjelmistoprojektiin tai -tuotteeseen, mukaan lukien seuraavat (Richards ja Ford 2020):

* Rakenne (esimerkiksi mallit kuten mikropalvelut)

* Ei-toiminnalliset vaatimukset (tietoturva, korkea käytettävyys ja vikasietoisuus)

* Riippuvuudet (komponenttien kytkentä)

* Rajapinnat (rajapinnat ja julkaistut sopimukset)

* Rakennustekniikat (kirjastot, kehykset, työkalut ja prosessit)

* Toiminnalliset ja ei-toiminnalliset vaatimukset ovat ADR-prosessin yleisimmät syötteet.


## ADR-tietueen sisältö

Kun tiimi tunnistaa ADR-tietueen tarpeen, tiimin jäsen alkaa kirjoittaa ADR-tietuetta koko projektia koskevan mallipohjan pohjalta. (Katso ADR GitHub -organisaatiosta esimerkkimallipohjia.) Mallipohja yksinkertaistaa ADR-tietueen luomista ja varmistaa, että ADR-tietue kirjaa kaiken olennaisen tiedon. ADR-tietueen tulisi vähintään määritellä päätöksen konteksti, itse päätös sekä päätöksen seuraukset projektille ja sen tuotoksille. (Esimerkkejä näistä osioista on liitteessä.) Yksi ADR-rakenteen tehokkaimmista piirteistä on, että se keskittyy päätöksen syyhyn sen sijaan, miten tiimi toteutti sen. Sen ymmärtäminen, miksi tiimi teki päätöksen, helpottaa muiden tiimin jäsenten päätöksen omaksumista ja estää muita arkkitehteja, jotka eivät olleet mukana päätöksentekoprosessissa, kumoamasta kyseistä päätöstä tulevaisuudessa.


## ADR-tietueen käyttöönottoprosessi

Jokainen tiimin jäsen voi luoda ADR-tietueen, mutta tiimin tulisi määritellä ADR-tietueen omistajuus. Jokaisen ADR-tietueen omistajana olevan kirjoittajan tulisi aktiivisesti ylläpitää ja viestiä ADR-tietueen sisältöä. Tämän omistajuuden selventämiseksi tässä oppaassa viitataan ADR-tietueiden kirjoittajiin seuraavissa osioissa ADR-tietueen omistajina. Muut tiimin jäsenet voivat aina osallistua ADR-tietueeseen. Jos ADR-tietueen sisältö muuttuu ennen kuin tiimi hyväksyy sen, omistajan tulisi hyväksyä nämä muutokset.

Kun tiimi on tunnistanut arkkitehtuuripäätöksen ja sen omistajan, ADR-tietueen omistaja tuo ADR-tietueen prosessin alussa tilaan **Ehdotettu**. Ehdotettu-tilassa olevat ADR-tietueet ovat valmiita katselmoitavaksi.

Tämän jälkeen ADR-tietueen omistaja käynnistää ADR-tietueen katselmointiprosessin. ADR-katselmoinnin tavoitteena on päättää, hyväksyykö tiimi ADR-tietueen, päättääkö se, että se tarvitsee uudelleentyöstöä, vai hylkääkö se ADR-tietueen. Projektitiimi, omistaja mukaan lukien, katselmoi ADR-tietueen. Katselmointikokouksen tulisi alkaa varatulla aikajaksolla ADR-tietueen lukemiseen. Keskimäärin 10–15 minuuttia pitäisi riittää. Tänä aikana jokainen tiimin jäsen lukee dokumentin ja lisää kommentteja ja kysymyksiä merkitäkseen epäselvät aiheet. Katselmointivaiheen jälkeen ADR-tietueen omistaja lukee ääneen ja keskustelee jokaisesta kommentista tiimin kanssa.

Jos tiimi löytää toimenpiteitä ADR-tietueen parantamiseksi, ADR-tietueen tila pysyy **Ehdotettu**. ADR-tietueen omistaja muotoilee toimenpiteet ja lisää yhteistyössä tiimin kanssa kullekin toimenpiteelle vastuuhenkilön. Jokainen tiimin jäsen voi osallistua toimenpiteisiin ja ratkaista ne. ADR-tietueen omistajan vastuulla on ajoittaa katselmointiprosessi uudelleen.

Tiimi voi myös päättää hylätä ADR-tietueen. Tässä tapauksessa ADR-tietueen omistaja lisää hylkäämiselle syyn estääkseen saman aiheen tulevat keskustelut. Omistaja muuttaa ADR-tietueen tilaksi **Hylätty**.

Jos tiimi hyväksyy ADR-tietueen, omistaja lisää siihen aikaleiman, version ja sidosryhmien luettelon. Sen jälkeen omistaja päivittää tilaksi **Hyväksytty**.

ADR-tietueet ja niiden muodostama päätösloki edustavat tiimin tekemiä päätöksiä ja tarjoavat historian kaikista päätöksistä. Tiimi käyttää ADR-tietueita viitteenä koodi- ja arkkitehtuurikatselmoinneissa, kun se on mahdollista. Koodikatselmointien, suunnittelutehtävien ja toteutustehtävien suorittamisen lisäksi tiimin jäsenten tulisi tutustua ADR-tietueisiin tuotteen strategisten päätösten osalta.

Hyvänä käytäntönä jokaisen ohjelmistomuutoksen tulisi käydä läpi vertaiskatselmointi ja vaatia vähintään yksi hyväksyntä. Koodikatselmoinnin aikana koodikatselmoija saattaa löytää muutoksia, jotka rikkovat yhtä tai useampaa ADR-tietuetta. Tässä tapauksessa katselmoija pyytää koodimuutoksen tekijää päivittämään koodin ja jakaa linkin ADR-tietueeseen. Kun tekijä päivittää koodin, vertaiskatselmoijat hyväksyvät sen ja se yhdistetään pääasialliseen koodikantaan.


## ADR-tietueen katselmointiprosessi

Tiimin tulisi käsitellä ADR-tietueita muuttumattomina dokumentteina sen jälkeen, kun tiimi on hyväksynyt tai hylännyt ne. Olemassa olevan ADR-tietueen muutokset edellyttävät uuden ADR-tietueen luomista, uuden ADR-tietueen katselmointiprosessin järjestämistä ja ADR-tietueen hyväksymistä. Jos tiimi hyväksyy uuden ADR-tietueen, omistajan tulisi muuttaa vanhan ADR-tietueen tilaksi **Korvattu**.
