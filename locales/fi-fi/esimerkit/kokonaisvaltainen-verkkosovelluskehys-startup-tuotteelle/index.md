# Arkkitehtuuripäätöstietue: verkkosovelluskehys, kaikki mukana (batteries included), full stack, startup-tuotteelle

<!-- 

ChatGPT prompt

Long software architecture decision record 
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports. 

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Ensisijainen tavoite:**  
Rakentaa verkkosovellus maksaville asiakkaille kirjautumista, tiedostojen lataamista, datan käsittelyä ja raporttien katselua varten, keskittyen ketterään kehitykseen, full stack -toiminnallisuuteen ja vahvaan yhteensopivuuteen tekoäly-/koneoppimistyökalujen, erityisesti Project Jupyter -muistikirjojen, kanssa.

### Konteksti ja vaatimukset:

1. **Ketterä kehitys (korkea prioriteetti)**: Startupina tarvitsemme nopeaa iterointia ja joustavuutta. Ketterät käytännöt, kuten nopea prototyyppien teko, iteratiivinen kehitys ja muutoksiin mukautuvuus, ovat avainasemassa kehityssyklissämme.

2. **Full stack -kehys (korkea prioriteetti)**: Pyrimme minimoimaan kuormituksen valitsemalla kehyksen, joka pystyy käsittelemään tehokkaasti sekä taustajärjestelmän että käyttöliittymän, vähentäen erillisten käyttöliittymäkehysten tarvetta.

3. **Yhteensopivuus tekoäly-/koneoppimistyökalujen kanssa (korkea prioriteetti)**: Kyky integroitua helposti data-analyysityökaluihin, kuten Jupyter-muistikirjoihin, ja Pythonin datatieteen ekosysteemiin (NumPy, Pandas, TensorFlow jne.) on välttämätön. Tämä helpottaisi tehokasta datan käsittelyä ja raportointia.

4. **Matalan tärkeyden kriteerit**:
   - **Ajonaikainen nopeus**: Vaikka suorituskyky on olennaista, se ei ole alussa kriittisin tekijä, koska olemme huolissamme enemmän kehitysnopeudesta ja ominaisuuksien kattavuudesta.
   - **Skaalautuvuus**: Odotamme kasvua, mutta skaalautuvuushuolet voidaan käsitellä myöhemmin, eikä tämä ole nyt ensisijainen vaatimus.
   - **Taaksepäin yhteensopivuus**: Keskitymme nykyisiin teknologioihin emmekä ole kovin huolissamme taaksepäin yhteensopivuudesta vanhojen järjestelmien kanssa.

### Arvioidut kehykset:

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Yleiskuva**:  
Django on korkean tason verkkokehys Pythonille, joka edistää nopeaa kehitystä sekä puhdasta ja pragmaattista suunnittelua. Se tunnetaan "batteries included" -filosofiastaan, mikä tarkoittaa, että se sisältää monia ominaisuuksia, kuten tunnistautumisen, reitityksen, ORM:n ja lomakkeiden käsittelyn suoraan laatikosta.

**Vahvuudet**:  
- **Full stack**: Django on kattava full stack -kehys, joka pystyy käsittelemään sekä taustajärjestelmän että käyttöliittymän tarpeet integroiduilla ominaisuuksilla (esim. mallipohjamoottori, hallintakäyttöliittymä).
- **Ketterä kehitys**: Djangon hyvin määritelty rakenne ja käytännöt mahdollistavat nopean kehityksen ja mukautuvuuden, mikä on ratkaisevaa startup-ympäristössä. Kehys tulee erinomaisen dokumentaation ja rikkaan kolmannen osapuolen pakettien ekosysteemin kanssa, mikä nopeuttaa kehitystä.
- **Tekoäly-/koneoppimisintegraatio**: Pythonin ekosysteemi on vertaansa vailla datatieteen ja koneoppimisen osalta. Django, joka on Python-pohjainen, integroituu saumattomasti työkaluihin kuten Jupyter-muistikirjat, Pandas, NumPy, TensorFlow ja scikit-learn.
- **Yhteisö ja ekosysteemi**: Djangolla on laaja yhteisö, vankka dokumentaatio ja laaja valikoima liitännäisiä ja laajennuksia, mikä nopeuttaa merkittävästi kehitystä ja vianetsintää.
  
**Heikkoudet**:  
- **Ajonaikainen nopeus**: Python on yleensä hitaampi verrattuna kieliin kuten Rust tai Elixir. Tässä käyttötapauksessa, jossa suorituskyky ei ole ensisijainen huolenaihe, tämä ei välttämättä ole ratkaiseva este.
- **Skaalautuvuus**: Vaikka Django on erittäin skaalautuva, erittäin suurilla kuormilla voi olla haasteita ilman huolellista optimointia (esim. käsiteltäessä raskaita samanaikaisia pyyntöjä). Djangoa voidaan kuitenkin edelleen skaalata tehokkaasti kuormantasaus- ja välimuistitekniikoilla.

**Tuomio**:  
Django sopii hyvin yhteen ketterän kehityksen, full stack -tuen ja tekoäly-/koneoppimisyhteensopivuuden vaatimusten kanssa. Sen Python-integraatio tarjoaa saumattoman pääsyn sovellukselle tarpeellisiin datatieteen työkaluihin ja kirjastoihin.

---

### 2. **Ruby on Rails (Ruby)**

**Yleiskuva**:  
Ruby on Rails (RoR) on kypsä full stack -verkkosovelluskehys, joka tunnetaan konventio-ennen-konfigurointia-lähestymistavastaan, joka helpottaa nopeaa kehitystä.

**Vahvuudet**:  
- **Full stack**: RoR sisältää sisäänrakennetut työkalut sekä taustajärjestelmän että käyttöliittymän kehitykseen (esim. näkymät, mallipohjat, runkogenerointi), ja sen rikas gem-kirjasto mahdollistaa erilaisten ominaisuuksien nopean toteuttamisen.
- **Ketterä kehitys**: Ruby on Rails tunnetaan erityisesti nopeista iterointisykleistään, mikä on edullista startupeille, jotka haluavat iteroida ominaisuuksia nopeasti. RoR tukee testilähtöistä kehitystä (TDD) ja sillä on vakiintunut ekosysteemi ketterille työnkuluille.
- **Yhteisö ja ekosysteemi**: RoR:llä on vakiintunut, vahva yhteisö ja laaja valikoima gemejä, jotka voivat nopeuttaa kehitystä.
- **Käytön helppous**: Railsilla on erittäin kehittäjäystävällinen syntaksi, ja se tunnetaan siitä, että se tekee tehtävistä kuten tietokantasiirroista, model-view-controller (MVC) -arkkitehtuurista ja reittien käsittelystä nopeita ja yksinkertaisia.

**Heikkoudet**:  
- **Suorituskyky**: Rubyn ajonaikainen suorituskyky on yleensä hitaampi verrattuna Pythoniin tai Elixiriin. Vaikka RoR voi skaalautua oikealla infrastruktuurilla, Rubyn suorituskyky voi muodostua pullonkaulaksi sovelluksille, jotka vaativat raskasta reaaliaikaista käsittelyä tai korkeaa samanaikaista liikennettä.
- **Tekoäly-/koneoppimisintegraatio**: Vaikka Rubylla on joitakin koneoppimiskirjastoja, sitä ei ole omaksuttu yhtä laajasti tekoäly-/koneoppimisyhteisössä kuin Pythonia. Integrointi työkaluihin kuten Jupyter-muistikirjat ei ole yhtä saumatonta, mikä tekee Pythonista vahvemman valinnan dataraskaille sovelluksille.
  
**Tuomio**:  
Vaikka Ruby on Rails on erinomainen ketterässä kehityksessä ja nopeassa prototyyppien teossa, se jää jälkeen tekoäly-/koneoppimisyhteensopivuudessa verrattuna Pythoniin (Django). Se on toteuttamiskelpoinen valinta startupeille, jotka priorisoivat nopean iteroinnin syvän data-analyysin integraation edelle.

---

### 3. **Phoenix (Elixir)**

**Yleiskuva**:  
Phoenix on Elixirillä rakennettu verkkokehys. Elixir on funktionaalinen ohjelmointikieli, joka on suunniteltu skaalautuvuutta ja rinnakkaisuutta varten. Phoenix hyödyntää Erlang-virtuaalikonetta, joka tunnetaan massiivisen rinnakkaisuuden ja vikasietoisten järjestelmien käsittelystä.

**Vahvuudet**:  
- **Skaalautuvuus ja suorituskyky**: Phoenix loistaa skaalautuvuudessa ja korkean rinnakkaisuuden käsittelyssä. Se on rakennettu Erlang-virtuaalikoneen päälle, joka voi tukea tuhansia (tai jopa miljoonia) samanaikaisia yhteyksiä, mikä tekee siitä vahvan ehdokkaan sovelluksille, jotka vaativat reaaliaikaista tietojenkäsittelyä tai suuren volyymin liikennettä.
- **Full stack**: Phoenix sisältää kaiken tarvittavan sekä sovelluksen taustajärjestelmän että käyttöliittymän rakentamiseen. Se tukee live-näkymiä (live views) interaktiivisiin käyttöliittymäpäivityksiin ja sisältää mallipohjamoottorin.
- **Ketterä kehitys**: Phoenix on erittäin modulaarinen, mikä mahdollistaa ominaisuuksien nopean iteroinnin. Se sopii hyvin startupeille, joiden täytyy edetä nopeasti.
- **Tekoäly-/koneoppimisyhteensopivuus**: Vaikka Elixirillä on kehittyviä koneoppimiskirjastoja, sitä ei tueta yhtä laajasti tekoäly-/koneoppimistehtävissä kuin Pythonia. Integrointi työkaluihin kuten Jupyter-muistikirjat vaatisi kiertoteitä, koska Elixirin datatieteen ekosysteemi ei ole yhtä kypsä kuin Pythonin.

**Heikkoudet**:  
- **Tekoäly-/koneoppimisekosysteemi**: Elixir ei ole datatieteessä tai koneoppimisessa ensisijaisesti käytetty kieli, eikä ekosysteemi ole yhtä kypsä kuin Pythonin. Siten integrointi työkaluihin kuten Jupyter-muistikirjat tai suosittuihin tekoälykirjastoihin (TensorFlow, PyTorch) on hankalaa.
- **Oppimiskäyrä**: Jos tiimi ei tunne funktionaalista ohjelmointia ja Elixiriä, oppimiskäyrä voi olla jyrkempi.

**Tuomio**:  
Phoenix on erinomainen valinta, jos skaalautuvuus ja rinnakkaisuus ovat ensisijaisia huolenaiheita. Kun otetaan huomioon tekoäly-/koneoppimisyhteensopivuuden prioriteetti, Phoenix ei välttämättä ole paras valinta Elixirin rajallisen ekosysteemin vuoksi tällä alueella.

---

### 4. **Loco (Rust)**

**Yleiskuva**:  
Loco on Rustilla rakennettu verkkokehys. Rust on järjestelmäohjelmointikieli, joka tunnetaan suorituskyvystään, muistiturvallisuudestaan ja rinnakkaisuudestaan. Rust on yhä suositumpi korkean suorituskyvyn sovellusten rakentamisessa.

**Vahvuudet**:  
- **Suorituskyky**: Rustin tärkein vahvuus on sen korkea suorituskyky ja muistiturvallisuus, mikä tekee siitä erinomaisen valinnan sovelluksille, jotka vaativat matalan tason hallintaa tai äärimmäisen korkeaa suorituskykyä.
- **Rinnakkaisuus**: Rustin omistajuusjärjestelmä takaa muistiturvallisuuden samalla kun se sallii turvallisen rinnakkaisen ohjelmoinnin, mikä tekee siitä ihanteellisen järjestelmille, joiden on skaalauduttava tehokkaasti ja käsiteltävä rinnakkaisuutta.

**Heikkoudet**:  
- **Full stack -kehitys**: Loco, vaikka lupaava, ei ole yhtä kypsä kuin muut kehykset täydellisen full stack -ratkaisun tarjoamisessa. Se sopii paremmin taustajärjestelmäkehitykseen, ja Rustin ympärillä oleva käyttöliittymäekosysteemi on vielä kehittymässä.
- **Ketterä kehitys**: Kehitys Rustilla voi olla hitaampaa verrattuna korkeamman tason kieliin kuten Python tai Ruby sen matalamman tason luonteen ja jyrkemmän oppimiskäyrän vuoksi.
- **Tekoäly-/koneoppimisekosysteemi**: Rustilla ei ole yhtä laajaa ekosysteemiä tekoälylle/koneoppimiselle kuin Pythonilla. Vaikka Rustille on kasvavia kirjastoja numeeriseen laskentaan, ne ovat paljon vähemmän kypsiä kuin Pythonin tarjonta, kuten Jupyter-muistikirjat tai koneoppimiskehykset.
  
**Tuomio**:  
Vaikka Rust ja sen kehys Loco tarjoavat poikkeuksellisen suorituskyvyn, full stack -tuen, ketterän kehityksen etujen ja tekoäly-/koneoppimisekosysteemin puute tekevät siitä vähemmän ihanteellisen tähän nimenomaiseen käyttötapaukseen. Se sopii paremmin suorituskykykriittisiin sovelluksiin kuin nopeaan verkkokehitykseen integroiduilla datatieteen työkaluilla.

---

### Johtopäätös

Vaihtoehtojen arvioinnin jälkeen projektin vaatimusten perusteella **Django (Python)** on sopivin valinta. Se tarjoaa seuraavat edut:

- **Full stack -ominaisuudet**: Django on full stack -kehys, joka integroi sekä taustajärjestelmän että käyttöliittymän kehityksen.
- **Ketterä kehitys**: Kehys sopii hyvin nopeaan prototyyppien tekoon ja iterointiin, mikä on olennaista startup-ympäristössä.
- **Tekoäly-/koneoppimisyhteensopivuus**: Python on tekoälyn/koneoppimisen johtava kieli, ja Djangon yhteensopivuus kirjastojen, kuten Jupyter-muistikirjojen, kanssa varmistaa sujuvan integroinnin data-analyysiin ja -käsittelyyn.
- **Yhteisö ja ekosysteemi**: Djangon vahva yhteisön tuki ja laaja kirjastoekosysteemi tarjoavat lukuisia työkaluja kehityksen nopeuttamiseen.

Vaikka **Ruby on Rails** on myös vahva ehdokas ketterään kehitykseen, sen rajallinen tekoäly-/koneoppimistuki tekee siitä vähemmän ihanteellisen tähän nimenomaiseen käyttötapaukseen. **Phoenix (Elixir)** ja **Loco (Rust)**, vaikka erinomaisia skaalautuvuudessa ja suorituskyvyssä, jäävät jälkeen tekoäly-/koneoppimisintegraatiossa ja full stack -kehityksessä. Siksi Django on tälle projektille suositeltu kehys.
