# Päätöstietueen mallipohja: arc42

<https://arc42.org/overview>

## 1. Johdanto ja tavoitteet

Lyhyt kuvaus vaatimuksista, ajavista voimista ja vaatimusten tiivistelmä (tai
abstrakti). Arkkitehtuurin kolme (enintään viisi) tärkeintä laatutavoitetta, joilla on
korkein prioriteetti keskeisille sidosryhmille. Taulukko tärkeistä sidosryhmistä
ja heidän odotuksistaan arkkitehtuurin suhteen.

## 1.1 Vaatimusten yleiskatsaus

### Sisältö

Lyhyt kuvaus toiminnallisista vaatimuksista, ajavista voimista ja vaatimusten
tiivistelmä (tai abstrakti). Linkit (toivottavasti olemassa oleviin) vaatimusdokumentteihin,
sekä tieto siitä, mistä ne löytyvät. 

### Motivaatio

Loppukäyttäjien näkökulmasta järjestelmä luodaan tai sitä muutetaan
liiketoiminnan tukemiseksi paremmin ja/tai laadun parantamiseksi. 

### Muoto

Lyhyt tekstikuvaus, todennäköisesti taulukkomuotoisena käyttötapauskuvauksena. Jos vaatimusdokumentteja
on olemassa, tämän yleiskatsauksen tulisi viitata niihin.

Pidä nämä otteet mahdollisimman lyhyinä. Tasapainota tämän dokumentin luettavuus
vaatimusdokumentteihin nähden mahdollisen päällekkäisyyden kanssa. 

## 1.2 Laatutavoitteet

### Sisältö

Arkkitehtuurin kolme (enintään viisi) tärkeintä laatutavoitetta, joiden täyttyminen on
tärkeintä keskeisille sidosryhmille. Tarkoitamme todella arkkitehtuurin
laatutavoitteita. Älä sekoita niitä projektin tavoitteisiin. Ne eivät ole
välttämättä samoja. ISO 25010 -standardi antaa hyvän yleiskuvan
mahdollisista kiinnostavista aiheista.

### Motivaatio

Sinun tulisi tuntea tärkeimpien sidosryhmiesi laatutavoitteet, koska
ne vaikuttavat perustaviin arkkitehtuuripäätöksiin. Ole hyvin
konkreettinen näistä laatuominaisuuksista, vältä muotisanoja. Jos et arkkitehtina
tiedä, miten työsi laatua arvioidaan …

### Muoto

Taulukko tärkeimmistä laatutavoitteista ja konkreettisista skenaarioista, prioriteettijärjestyksessä.

## 1.3 Sidosryhmät

### Sisältö

Selkeä yleiskuva järjestelmän sidosryhmistä, eli kaikista henkilöistä, rooleista tai
organisaatioista, jotka

- tarvitsevat tietoa arkkitehtuurista

- täytyy vakuuttaa arkkitehtuurista

- joutuvat työskentelemään arkkitehtuurin tai koodin kanssa

- tarvitsevat arkkitehtuurin dokumentaatiota työssään

- joutuvat tekemään päätöksiä järjestelmästä tai sen kehityksestä

### Motivaatio

Sinun tulisi tuntea kaikki järjestelmän kehitykseen osallistuvat tai
järjestelmän vaikutuksen kohteena olevat osapuolet. Muuten saatat kohdata ikäviä yllätyksiä myöhemmin
kehitysprosessissa. Nämä sidosryhmät määrittävät työsi ja sen tulosten laajuuden ja
yksityiskohtaisuustason.

### Muoto

Taulukko, jossa on roolien nimet, henkilöiden nimet ja heidän odotuksensa
arkkitehtuurin ja sen dokumentaation suhteen.

## 2. Rajoitteet

Kaikki, mikä rajoittaa tiimejä suunnittelu- ja toteutuspäätöksissä tai
päätöksissä liittyvistä prosesseista. Voivat joskus ylittää yksittäisten järjestelmien rajat ja
olla voimassa kokonaisissa organisaatioissa ja yrityksissä.

### Sisältö

Kaikki vaatimukset, jotka rajoittavat ohjelmistoarkkitehtien suunnittelu- ja
toteutuspäätösten vapautta tai päätöksiä kehitysprosessista. Nämä
rajoitteet ylittävät joskus yksittäiset järjestelmät ja ovat voimassa kokonaisissa
organisaatioissa ja yrityksissä.

### Motivaatio

Arkkitehtien tulisi tietää tarkalleen, missä he ovat vapaita suunnittelupäätöksissään ja
missä heidän on noudatettava rajoitteita. Rajoitteet on aina käsiteltävä;
ne voivat kuitenkin olla neuvoteltavissa.

### Muoto

Yksinkertaiset rajoitetaulukot selityksineen. Tarvittaessa voit jakaa ne
teknisiin rajoitteisiin, organisatorisiin ja poliittisiin rajoitteisiin sekä käytäntöihin (esim. ohjelmointi- tai versiointiohjeet, dokumentaatio- tai nimeämiskäytännöt)

## 3. Konteksti ja rajaus

Rajaa järjestelmäsi sen (ulkoisista) kommunikointikumppaneista (naapurijärjestelmät ja
käyttäjät). Määrittelee ulkoiset rajapinnat. Esitetään liiketoiminta-/toimialanäkökulmasta (aina) tai
teknisestä näkökulmasta (valinnainen)

### Sisältö

Järjestelmän rajaus ja konteksti — kuten nimikin kertoo — rajaa järjestelmäsi (eli
laajuutesi) kaikista sen kommunikointikumppaneista (naapurijärjestelmät ja käyttäjät,
eli järjestelmäsi konteksti). Se määrittää siten ulkoiset rajapinnat.

Tarvittaessa erota liiketoimintakonteksti (toimialakohtaiset syötteet ja
tulosteet) tekniseksi kontekstiksi (kanavat, protokollat, laitteisto).

### Motivaatio

Toimialarajapinnat ja tekniset rajapinnat kommunikointikumppaneihin ovat
järjestelmäsi kriittisimpiä osa-alueita. Varmista, että ymmärrät ne täysin.

### Muoto

- Erilaisia kontekstikaavioita

- Luettelot kommunikointikumppaneista ja heidän rajapinnoistaan.

## 3.1 Liiketoimintakonteksti

### Sisältö

Kaikkien kommunikointikumppaneiden (käyttäjät, IT-järjestelmät, …) määrittely
selityksineen toimialakohtaisista syötteistä ja tulosteista tai rajapinnoista. Valinnaisesti voit
lisätä toimialakohtaisia formaatteja tai kommunikointiprotokollia.

### Motivaatio

Kaikkien sidosryhmien tulisi ymmärtää, mitä dataa vaihdetaan järjestelmän ympäristön
kanssa.

### Muoto

Kaikenlaisia kaavioita, jotka esittävät järjestelmän mustana laatikkona ja määrittelevät toimialarajapinnat
kommunikointikumppaneihin.

Vaihtoehtoisesti (tai lisäksi) voit käyttää taulukkoa. Taulukon otsikko on
järjestelmäsi nimi, ja kolme saraketta sisältävät kommunikointikumppanin nimen,
syötteet ja tulosteet.

## 3.2 Tekninen konteksti

### Sisältö

Tekniset rajapinnat (kanavat ja siirtovälineet), jotka yhdistävät järjestelmäsi
sen ympäristöön. Lisäksi toimialakohtaisen syötteen/tulosteen kuvaus
kanaviin, eli selitys siitä, mikä I/O käyttää mitäkin kanavaa.

### Motivaatio

Monet sidosryhmät tekevät arkkitehtuuripäätöksiä järjestelmän ja sen kontekstin
välisten teknisten rajapintojen perusteella. Erityisesti infrastruktuuri- tai laitteistosuunnittelijat päättävät nämä tekniset rajapinnat.

### Muoto

Esim. UML-käyttöönottokaavio, joka kuvaa kanavat naapurijärjestelmiin, yhdessä
kuvaustaulukon kanssa, joka näyttää kanavien ja
syötteen/tulosteen väliset suhteet.

## 4. Ratkaisustrategia

Yhteenveto perustavista päätöksistä ja ratkaisustrategioista, jotka muovaavat
arkkitehtuuria. Voi sisältää teknologian, ylimmän tason hajotuksen, lähestymistavat
tärkeimpien laatutavoitteiden saavuttamiseksi ja olennaiset organisatoriset päätökset.

### Sisältö

Lyhyt yhteenveto ja selitys perustavista päätöksistä ja ratkaisustrategioista, jotka muovaavat järjestelmän arkkitehtuuria. Näitä ovat

- teknologiapäätökset

- päätökset järjestelmän ylimmän tason hajotuksesta, esim. arkkitehtuurimallin tai suunnittelumallin käyttö

- päätökset siitä, miten keskeiset laatutavoitteet saavutetaan

- olennaiset organisatoriset päätökset, esim. kehitysprosessin valinta tai tiettyjen tehtävien delegointi kolmansille osapuolille.

### Motivaatio

Nämä päätökset muodostavat arkkitehtuurisi kulmakivet. Ne ovat perusta
monille muille yksityiskohtaisille päätöksille tai toteutussäännöille.

### Muoto

Pidä näiden avainpäätösten selitys lyhyenä.

Perustele, mitä olet päättänyt ja miksi päätit niin, ongelmanasettelusi,
laatutavoitteiden ja keskeisten rajoitteiden pohjalta. Viittaa yksityiskohtiin
seuraavissa osioissa (osio 5 rakenteellisiin yksityiskohtiin, osio 8
läpileikkaaviin käsitteisiin).

Voit käyttää luetteloa ratkaisulähestymistavoista tai taulukkoa.

## 5. Rakennuspalikkanäkymä

Järjestelmän staattinen hajotus, lähdekoodin abstraktiot, esitettynä
valkoisten laatikoiden hierarkiana (jotka sisältävät mustia laatikoita) sopivalle
yksityiskohtaisuustasolle asti.

### Sisältö

Rakennuspalikkanäkymä esittää järjestelmän staattisen hajotuksen
rakennuspalikoihin (moduulit, komponentit, alijärjestelmät, luokat, rajapinnat, paketit,
kirjastot, kehykset, kerrokset, osiot, tasot, funktiot, makrot, operaatiot,
tietorakenteet, …) sekä niiden riippuvuudet (suhteet, assosiaatiot,
…)

Tämä näkymä on pakollinen jokaisessa arkkitehtuuridokumentaatiossa. Talon
vertauskuvassa tämä on pohjapiirros.

### Motivaatio

Pidä yleiskuva lähdekoodistasi tekemällä sen rakenteesta ymmärrettävä
abstraktion avulla.

Näin voit kommunikoida sidosryhmäsi kanssa abstraktilla tasolla
paljastamatta toteutuksen yksityiskohtia.

### Muoto

Rakennuspalikkanäkymä on hierarkkinen kokoelma mustia laatikoita ja valkoisia
laatikoita (katso alla oleva kuva) ja niiden kuvauksia.

## 5.1 Koko järjestelmän valkoinen laatikko

Tässä kuvaat koko järjestelmän hajotuksen käyttäen seuraavaa valkoisen laatikon mallipohjaa. Se sisältää

- yleiskatsauskaavion

- perustelun hajotukselle

- mustan laatikon kuvaukset sisältyvistä rakennuspalikoista. Näille tarjoamme vaihtoehtoja:

  - käytä yhtä taulukkoa lyhyeen ja pragmaattiseen yleiskuvaan kaikista sisältyvistä rakennuspalikoista ja niiden rajapinnoista

  - käytä luetteloa rakennuspalikoiden mustan laatikon kuvauksista mustan laatikon mallipohjan mukaan (katso alla). Työkalun valinnasta riippuen tämä luettelo voi olla alalukuja (tekstitiedostoissa), alisivuja (wikissä) tai sisäkkäisiä elementtejä (mallinnustyökalussa).

  - (valinnainen:) tärkeät rajapinnat, joita ei ole selitetty rakennuspalikan mustan laatikon mallipohjissa, mutta jotka ovat hyvin tärkeitä valkoisen laatikon ymmärtämiselle.

Koska rajapintojen määrittelyyn on niin monia tapoja, emme tarjoa niille erityistä mallipohjaa.

Parhaassa tapauksessa selviät esimerkeillä tai yksinkertaisilla allekirjoituksilla.

## 5.2 Taso 2

Tässä voit määritellä (joidenkin) tason 1 rakennuspalikoiden sisäisen rakenteen
valkoisina laatikoina.

Sinun on päätettävä, mitkä järjestelmäsi rakennuspalikat ovat riittävän tärkeitä
oikeuttaakseen tällaisen yksityiskohtaisen kuvauksen. Suosi olennaisuutta täydellisyyden sijaan.
Määrittele tärkeät, yllättävät, riskialttiit, monimutkaiset tai muuttuvat rakennuspalikat. Jätä
pois järjestelmäsi tavalliset, yksinkertaiset, tylsät tai standardoidut osat

### 5.2.1 Rakennuspalikan 1 valkoinen laatikko

Määrittelee rakennuspalikan 1 sisäisen rakenteen.

Käytä valkoisen laatikon mallipohjaa (katso yllä).

## 6. Ajonaikainen näkymä

Rakennuspalikoiden käyttäytyminen skenaarioina, jotka kattavat tärkeät käyttötapaukset tai
ominaisuudet, vuorovaikutukset kriittisissä ulkoisissa rajapinnoissa, käytön ja
hallinnan sekä virhe- ja poikkeustilanteet.

### Sisältö

Ajonaikainen näkymä kuvaa järjestelmän rakennuspalikoiden konkreettista käyttäytymistä ja vuorovaikutuksia skenaarioina seuraavilta alueilta:

- tärkeät käyttötapaukset tai ominaisuudet: miten rakennuspalikat toteuttavat ne?

- vuorovaikutukset kriittisissä ulkoisissa rajapinnoissa: miten rakennuspalikat toimivat yhdessä käyttäjien ja naapurijärjestelmien kanssa?

- käyttö ja hallinta: käynnistys, käynnistyminen, pysäytys

- virhe- ja poikkeusskenaariot

Huomautus: Pääkriteeri mahdollisten skenaarioiden (sekvenssit, työnkulut) valinnalle on niiden arkkitehtuurinen olennaisuus. Ei ole tärkeää kuvata suurta määrää skenaarioita. Dokumentoi mieluummin edustava valikoima.

### Motivaatio

Sinun tulisi ymmärtää, miten järjestelmäsi rakennuspalikoiden (ilmentymät) suorittavat tehtävänsä ja kommunikoivat ajon aikana. Kirjaat dokumentaatioosi pääasiassa skenaarioita viestiäksesi arkkitehtuurisi sidosryhmille, jotka ovat vähemmän halukkaita tai kykeneviä lukemaan ja ymmärtämään staattisia malleja (rakennuspalikkanäkymä, käyttöönottonäkymä).

### Muoto

Skenaarioiden kuvaamiseen on monia notaatioita, esim.


- numeroitu luettelo vaiheista (luonnollisella kielellä)

- aktiviteettikaaviot tai vuokaaviot

- sekvenssikaaviot

- BPMN tai EPC:t (tapahtumaprosessiketjut)

- tilakoneet

- jne.

## 6.n Ajonaikainen skenaario n (1, 2, 3 jne.)

Lisää ajonaikainen kaavio tai skenaarion tekstikuvaus.

Lisää kuvaus tässä kaaviossa esitettyjen rakennuspalikoiden ilmentymien välisten vuorovaikutusten huomionarvoisista piirteistä.

## 7. Käyttöönottonäkymä

Tekninen infrastruktuuri ympäristöineen, tietokoneineen, suorittimineen, topologioineen.
(Ohjelmisto)rakennuspalikoiden kuvaus infrastruktuurielementteihin.

### Sisältö

Käyttöönottonäkymä kuvaa:

- teknisen infrastruktuurin, jolla järjestelmäsi suoritetaan, infrastruktuurielementteineen
  kuten maantieteelliset sijainnit, ympäristöt, tietokoneet, suorittimet,
  kanavat ja verkkotopologiat sekä muut infrastruktuurielementit, sekä

- (ohjelmisto)rakennuspalikoiden kuvauksen näihin infrastruktuurielementteihin.

Usein järjestelmiä ajetaan eri ympäristöissä, esim. kehitysympäristö,
testiympäristö, tuotantoympäristö. Tällaisissa tapauksissa sinun tulisi
dokumentoida kaikki olennaiset ympäristöt.

Dokumentoi käyttöönottonäkymä erityisesti silloin, kun ohjelmistosi ajetaan
hajautettuna järjestelmänä useammalla kuin yhdellä tietokoneella, suorittimella, palvelimella tai kontilla
tai kun suunnittelet ja rakennat omia laitteistosuorittimia ja siruja.

Ohjelmistonäkökulmasta riittää kirjata ne infrastruktuurin elementit,
joita tarvitaan rakennuspalikoidesi käyttöönoton esittämiseen.
Laitteistoarkkitehdit voivat mennä tätä pidemmälle ja kuvata infrastruktuurin millä tahansa
yksityiskohtaisuustasolla, jonka he tarvitsevat kirjatakseen. 

### Motivaatio

Ohjelmisto ei toimi ilman laitteistoa. Tämä taustalla oleva infrastruktuuri voi ja
tulee vaikuttamaan järjestelmääsi ja/tai joihinkin läpileikkaaviin käsitteisiin. Siksi
sinun on tunnettava infrastruktuuri.

### Muoto

Ylimmän tason käyttöönottokaavio voi jo sisältyä osioon 3.2. teknisenä kontekstina, jossa oma infrastruktuurisi on YKSI musta laatikko. Tässä osiossa zoomaat tähän mustaan laatikkoon lisäkäyttöönottokaavioiden avulla.

- UML tarjoaa käyttöönottokaavioita tämän näkymän ilmaisemiseen. Käytä sitä, mahdollisesti sisäkkäisillä kaavioilla, kun infrastruktuurisi on monimutkaisempi.

- Kun (laitteisto)sidosryhmäsi suosivat muita kaaviotyyppejä UML-käyttöönottokaavion sijaan, anna heidän käyttää mitä tahansa tyyppiä, joka pystyy näyttämään infrastruktuurin solmut ja
  kanavat.

## 7.1 Infrastruktuuri, taso 1

Kuvaile (yleensä kaavioiden, taulukoiden ja tekstin yhdistelmällä):

- järjestelmäsi jakautuminen useisiin sijainteihin, ympäristöihin, tietokoneisiin, suorittimiin, .. sekä niiden väliset fyysiset yhteydet

- tärkeä perustelu tai motivaatio tälle käyttöönottorakenteelle

- infrastruktuurin laatu- ja/tai suorituskykyominaisuudet

- ohjelmistoartefaktien (rakennuspalikoiden) kuvaus infrastruktuurin elementteihin

Useita ympäristöjä tai vaihtoehtoisia käyttöönottoja varten kopioi tämä arc42:n osio kaikille olennaisille ympäristöille.

## 7.2 Infrastruktuuri, taso 2

Tässä voit sisällyttää (joidenkin) infrastruktuurielementtien sisäisen rakenteen infrastruktuurin tasolta 1.

Kopioi rakenne tasolta 1 jokaista valittua elementtiä varten.

## 8. Läpileikkaavat käsitteet

Kokonaisuutena periaatteelliset säännöt ja ratkaisulähestymistavat, jotka ovat olennaisia useissa
järjestelmän osissa (→ läpileikkaavia). Käsitteet liittyvät usein useisiin
rakennuspalikoihin. Sisällytä erilaisia aiheita kuten toimialamallit, arkkitehtuurimallit
ja -tyylit, tietyn teknologian käyttösäännöt ja toteutussäännöt.

### Sisältö

Tämä osio kuvaa läpileikkaavia käsitteitä (käytännöt, mallit, säännöt
tai ratkaisuideat). Tällaiset käsitteet liittyvät usein useisiin rakennuspalikoihin.
Ne voivat sisältää monia erilaisia aiheita.

### Motivaatio

Käsitteet muodostavat perustan arkkitehtuurin käsitteelliselle eheydelle (johdonmukaisuus, yhtenäisyys). Siten ne ovat tärkeä
panos järjestelmäsi sisäisten laatuominaisuuksien saavuttamisessa.

Tämä on paikka mallipohjassa, jonka tarjosimme tällaisten käsitteiden
yhtenäiselle määrittelylle.

Monet näistä käsitteistä liittyvät useisiin rakennuspalikoihisi tai vaikuttavat niihin.

### Muoto

Muoto voi vaihdella:

- käsitepaperit minkä tahansa rakenteen kanssa

- esimerkkitoteutukset, erityisesti teknisille käsitteille

- läpileikkaavat mallien otteet tai skenaariot arkkitehtuurinäkymien notaatioita käyttäen

### Tämän osion rakenne

Valitse vain järjestelmällesi tarpeellisimmat aiheet ja anna kullekin tason 2 otsikko tässä osiossa (esim. 8.1, 8.2 jne.).

- ÄLÄ YRITÄ kattaa kaikkia edellä mainitun kaavion aiheita.

### Tausta

Jotkin järjestelmien sisäiset aiheet koskevat usein useita rakennuspalikoita, laitteistoelementtejä
tai kehitysprosesseja. Voi olla helpompaa viestiä tai dokumentoida
tällaiset läpileikkaavat aiheet keskitetysti sen sijaan, että niitä toistettaisiin
kyseisten rakennuspalikoiden, laitteistoelementtien tai
kehitysprosessien kuvauksissa.

Tietyt käsitteet voivat koskea kaikkia järjestelmän elementtejä, toiset voivat olla
olennaisia vain muutamille.

## 9. Arkkitehtuuripäätökset

Tärkeät, kalliit, kriittiset, laajamittaiset tai riskialttiit arkkitehtuuripäätökset
perusteluineen.

### Sisältö

Tärkeät, kalliit, laajamittaiset tai riskialttiit arkkitehtuuripäätökset perusteluineen.
"Päätöksillä" tarkoitamme yhden vaihtoehdon valitsemista annettujen
kriteerien perusteella.

Käytä harkintaasi päättääksesi, tulisiko arkkitehtuuripäätös
dokumentoida tässä keskitetyssä osiossa vai dokumentoida se paremmin
paikallisesti (esim. yhden rakennuspalikan valkoisen laatikon mallipohjassa). Vältä
päällekkäisiä tekstejä. Viittaa osioon 4, jossa kirjasit jo arkkitehtuurisi tärkeimmät
päätökset.

### Motivaatio

Järjestelmäsi sidosryhmien tulisi pystyä ymmärtämään ja jäljittämään
päätöksesi.

### Muoto

- ADR (arkkitehtuuripäätöstietue) jokaisesta tärkeästä päätöksestä

- luettelo tai taulukko, järjestettynä tärkeyden ja seurausten mukaan tai

- yksityiskohtaisemmin erillisinä osioina päätöstä kohti

### Tausta (ADR-tietueista)

Pienemmät dokumentaatiokokonaisuudet ovat helpompia lukea, luoda ja ylläpitää. Arkkitehtuuripäätösten
osalta kehitystiimit usein:

- tietävät päätöksestä, koska se näkyy esim. lähdekoodissa, mutta

- eivät tiedä päätöksen taustalla olevaa motivaatiota (katso Nygard 2011)

Siksi sinun tulisi dokumentoida muutama tärkeä päätös yhdessä niiden motivaation ja perustelujen kanssa

### Ehdotuksemme päätöksistä

Pidä kokoelma arkkitehtuurin kannalta merkittävistä päätöksistä, eli päätöksistä, jotka
vaikuttavat rakenteeseen, laatuominaisuuksiin, tärkeisiin (erityisesti ulkoisiin)
riippuvuuksiin ja rajapintoihin tai rakennustekniikoihin (kiitos Michael
Nygardille tästä ehdotuksesta).

## 10. Laatuvaatimukset

Laatuvaatimukset skenaarioina, laatupuun avulla korkean tason
yleiskuvaksi. Tärkeimmät laatutavoitteet tulisi olla kuvattu osiossa
1.2. (laatutavoitteet).

### Sisältö

Tämä osio sisältää kaikki olennaiset laatuvaatimukset.

Tärkeimmät näistä vaatimuksista on jo kuvattu osiossa
1.2. (laatutavoitteet), joten niihin tulisi tässä vain viitata. Tässä
osiossa 10 tulisi kirjata myös vähemmän tärkeät laatuvaatimukset,
jotka eivät aiheuta suuria riskejä, jos niitä ei saavuteta täysin (mutta jotka voisivat olla
mukavia lisiä).

### Motivaatio

Koska laatuvaatimukset vaikuttavat paljon arkkitehtuuripäätöksiin,
sinun tulisi tietää, mitkä laatuominaisuudet ovat todella tärkeitä
sidosryhmillesi, täsmällisellä ja mitattavalla tavalla.

### Lisätietoja

Katso laaja Q42-laatumalli osoitteessa https://quality.arc42.org.

## 10.1 Laatuvaatimusten yleiskatsaus

### Sisältö

Yleiskatsaus tai yhteenveto laatuvaatimuksista.

### Motivaatio

Usein kohtaamme kymmeniä (tai jopa satoja) yksityiskohtaisia laatuvaatimuksia.
Tässä yleiskatsausosiossa sinun tulisi yrittää tiivistää, esim. kuvaamalla
kategorioita tai aiheita (kuten ISO 25010:2023 tai Q42 ehdottavat

Jos nämä yhteenvetokuvaukset ovat jo riittävän tarkkoja, täsmällisiä ja
mitattavia, voit ohittaa osion 10.2.

### Muoto

Käytä yksinkertaista taulukkoa, jossa jokainen rivi sisältää kategorian tai aiheen ja lyhyen kuvauksen
laatuvaatimuksesta. Vaihtoehtoisesti voit käyttää miellekarttaa
näiden laatuvaatimusten jäsentämiseen.

Kirjallisuudessa on kuvattu myös laatuominaisuuspuun idea,
joka asettaa yleisen termin "laatu" juureksi ja käyttää puumaista
tarkennusta termistä "laatu". [Bass+21] otti tähän tarkoitukseen käyttöön termin "Quality
Attribute Utility Tree".

## 10.2 Laatuskenaariot

### Sisältö

Laatuskenaariot konkretisoivat laatuvaatimukset ja mahdollistavat sen päättämisen, täyttyvätkö
ne (hyväksymiskriteerien mielessä). Varmista, että skenaariosi
ovat täsmällisiä ja mitattavia.

Kaksi skenaariotyyppiä on erityisen hyödyllisiä:

- Käyttöskenaariot (kutsutaan myös sovellusskenaarioiksi tai käyttötapausskenaarioiksi)
  kuvaavat järjestelmän ajonaikaisen reaktion tiettyyn ärsykkeeseen. Tämä sisältää myös
  skenaariot, jotka kuvaavat järjestelmän tehokkuutta tai suorituskykyä.
  Esimerkki: Järjestelmä reagoi käyttäjän pyyntöön yhden sekunnin kuluessa.

- Muutosskenaariot kuvaavat halutun vaikutuksen järjestelmän tai sen välittömän ympäristön
  muokkauksesta tai laajennuksesta. Esimerkki: Lisätoiminnallisuus
  toteutetaan tai laatuominaisuuden vaatimukset muuttuvat, ja muutoksen työmäärä tai kesto
  mitataan.

### Muoto

Yksityiskohtaisten skenaarioiden tyypillinen tieto sisältää seuraavaa:

Lyhyessä muodossa (Q42-mallissa suosittu):

- Konteksti/Tausta: Millainen järjestelmä tai komponentti, mikä on ympäristö tai tilanne?

- Lähde/Ärsyke: Kuka tai mikä käynnistää tai laukaisee käyttäytymisen, reaktion tai toiminnon.

- Mittari/Hyväksymiskriteerit: Vaste, joka sisältää mittauksen tai mittarin

Skenaarioiden pitkä muoto (SEI:n ja [Bass+21]:n suosima) on yksityiskohtaisempi ja sisältää seuraavat tiedot:

- Skenaarion tunniste: Skenaarion yksilöllinen tunniste.

- Skenaarion nimi: Lyhyt, kuvaava nimi skenaariolle.

- Lähde: Entiteetti (käyttäjä, järjestelmä tai tapahtuma), joka käynnistää skenaarion.

- Ärsyke: Laukaiseva tapahtuma tai ehto, johon järjestelmän on vastattava.

- Ympäristö: Toiminnallinen konteksti tai ehto, jossa järjestelmä kokee ärsykkeen.

- Artefakti: Rakennuspalikat tai muut järjestelmän elementit, joihin ärsyke vaikuttaa.

- Vaste: Lopputulos tai käyttäytyminen, jonka järjestelmä osoittaa reaktiona ärsykkeeseen.

- Vastemitta: Kriteerit tai mittari, jolla järjestelmän vastetta arvioidaan.

### Katso myös

Tammikuusta 2023 lähtien arc42 tarjoaa pragmaattisen laatumallin, joka ehdottaa
laatuvaatimusten merkitsemistä hashtageilla tai tunnisteilla kuten #flexible, #efficient,
#usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Riskit ja tekninen velka

Tunnetut tekniset riskit tai tekninen velka. Mitä mahdollisia ongelmia on olemassa järjestelmässä tai
sen ympärillä? Mistä kehitystiimi tuntee olonsa kurjaksi?

### Sisältö

Luettelo tunnistetuista teknisistä riskeistä tai teknisestä velasta, prioriteettijärjestyksessä

### Motivaatio

"Riskienhallinta on projektinhallintaa aikuisille" (Tim Lister, Atlantic
Systems Guild.)

Tämän tulisi olla mottosi arkkitehtuurin riskien ja teknisen velan
systemaattiselle havaitsemiselle ja arvioinnille, jota johdon
sidosryhmät (esim. projektipäälliköt, tuoteomistajat) tarvitsevat osana kokonaisriskianalyysia ja
toimenpidesuunnittelua.

### Muoto

Luettelo riskeistä ja/tai teknisestä velasta, mahdollisesti sisältäen ehdotettuja toimenpiteitä
riskien minimoimiseksi, lieventämiseksi tai välttämiseksi tai teknisen velan vähentämiseksi.
