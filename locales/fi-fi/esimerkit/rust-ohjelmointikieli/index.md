# Arkkitehtuuripäätöstietue: Rust-ohjelmointikieli

Päätöksen numero: AR-001

Päätöksen otsikko: Rust-ohjelmointikielen käyttöönotto

Päivämäärä: 1. joulukuuta 2021

Tila: Hyväksytty

### Ongelmanasettelu

Kehittäessämme ohjelmistosovelluksia olemme havainneet, että mahdollisten tietoturva-aukkojen lieventäminen ja ajonaikaisten virheiden ehkäiseminen on yhä haastavampaa. Nykyisillä ohjelmointikielillä, kuten C:llä ja C++:lla, kohtaamme edelleen ongelmia kuten puskurin ylivuodot, muistivuodot ja määrittelemätön käyttäytyminen, jotka johtavat sovellusten kaatumisiin. Tarvitsemme ohjelmointikielen, joka tarjoaa muistiturvallisuuden takeet ja on riittävän tehokas tukemaan suorituskykykriittisiä sovelluksia.

### Huomioon otettavat seikat

Useita ohjelmointikieliä on suunniteltu vastaamaan olemassa oleviin ongelmiin. Niiden joukossa Rust-ohjelmointikieli on saanut merkittävää huomiota kehittäjäyhteisöltä ainutlaatuisten suunnitteluominaisuuksiensa vuoksi. Huomioon otettavia seikkoja ovat;

1. Muistiturvallisuus ja tietoturva

2. Suorituskyky ja tehokkuus

3. Yhteisön tuki ja käyttöönotto

4. Oppimiskäyrä

5. Työkalut ja ekosysteemi

6. Yhteensopivuus olemassa olevien ohjelmistojärjestelmien kanssa.

### Rajoitteet

Uuden ohjelmointikielen käyttöönotto vaatii kehittäjien uudelleenkoulutusta, mikä vie aikaa ja resursseja. Kielen integrointi olemassa olevaan kehitystyönkulkuun voi olla haaste. Meidän on varmistettava yhteensopivuus olemassa olevien järjestelmien kanssa ja vältettävä rikkovia muutoksia jatkuvuuden säilyttämiseksi.

### Toteutus

1. Kehitystiimimme käy koulutuksen oppiakseen ja tutustuakseen Rust-ohjelmointikieleen.

2. Luomme uuden projektin Rustilla kokeilumielessä arvioidaksemme sen yhteensopivuutta ja soveltuvuutta kehitystarkoituksiimme.

3. Siirrämme olemassa olevat C:llä ja C++:lla kirjoitetut järjestelmät vähitellen Rustiin.

4. Teemme yhteistyötä Rust-yhteisön kanssa tutkiaksemme saatavilla olevia työkaluja ja kirjastoja, jotka voivat parantaa kehitystyönkulkuamme.

5. Seuraamme Rustin suorituskykyä ja vertaamme sitä säännöllisesti olemassa olevien ohjelmointikielten suorituskykyyn.

6. Omaksumme pitkän aikavälin lähestymistavan, joka tasapainottaa koulutuksen, integroinnin kustannukset ja Rustin käytön mahdolliset hyödyt.

### Perustelut

Olemme ottaneet Rustin käyttöön sen ainutlaatuisten ominaisuuksien vuoksi, jotka on suunniteltu tarjoamaan muistiturvallisuuden ja tietoturvan takeet suorituskykyä ja tehokkuutta säilyttäen. Rustin vankka tyyppijärjestelmä, lainantarkastin (borrow checker) ja muistiturvallisuuskonseptit tekevät siitä erittäin sopivan suorituskykykriittisten ja turvallisuuskriittisten sovellusten kehittämiseen. Lisäksi Rustilla on merkittävä kehittäjäyhteisö, joka antaa meille pääsyn laajaan työkalujen, kirjastojen ja ekosysteemin valikoimaan, joka tukee kehitystyönkulkuamme. Vaikka Rustin mukana tulee oppimiskäyrä, uskomme Rustin käyttöönoton hyötyjen olevan kustannuksia suuremmat ja tarjoavan erinomaisen mahdollisuuden jatkuvaan kasvuun ja innovaatioon.

### Seuraukset

1. Rustin käyttöönotto vaatii merkittävän investoinnin aikaan ja resursseihin kehittäjien kouluttamiseksi ja kielen integroimiseksi olemassa olevaan kehitystyönkulkuun.

2. Rustin käyttöönotto voi aiheuttaa jonkin verran yhteensopivuusongelmia olemassa olevien järjestelmien kanssa, mikä vaatii refaktorointia ja muutoksia.

3. Rustin käyttöönotto voi lisätä projektiimme osallistuvien kehittäjien määrää houkuttelemalla Rust-kehittäjiä, jotka haluavat työskennellä jännittävissä projekteissa.

4. Käyttöönotto voi johtaa parempaan suorituskykyyn, tehokkuuteen ja turvallisuuteen verrattuna olemassa oleviin kieliin.

5. Lopuksi Rustin käyttöönottoon liittyy mahdollinen hyöty tietoturva-aukkojen vähentämisessä sovelluksissamme.
   
<h6>Kunnianosoitus: tämän sivun on luonut ChatGPT, minkä jälkeen sitä on muokattu selkeyden ja muodon vuoksi.</h6>
