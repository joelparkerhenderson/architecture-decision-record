# {Otsikkosi tähän}

!!! info

    **Tila**: { Ehdotettu | Katselmoinnissa | Hyväksytty |  Hylätty | Korvattu | Vanhentunut }
    
    **Päivitetty**: {VVVV-KK-PP}

## Yhteenveto

{Tämä on ADR-tietueesi "johdon yhteenveto" tai "hissipuhe". Muutamalla
ytimekkäällä lauseella (tyypillisesti 2–4) ilmaise selkeästi ydinongelma, kysymys tai
mahdollisuus, johon tämä ADR vastaa. Sisällytä lyhyt vihje tehdystä päätöksestä tai
painopistealueesta. Tavoitteena on auttaa lukijoita ymmärtämään nopeasti, mistä tässä ADR-tietueessa
on kyse, ja päättämään, onko se heille olennainen, ilman että heidän tarvitsee lukea koko
dokumenttia. Ajattele sitä teknisen artikkelin tiivistelmänä tai hyvin lyhyenä
johdantona pääaiheeseen.}

## Ajurit

{Tämä osio selittää, **miksi** tämä päätös tehdään **nyt**. Ilmaise selkeästi
ensisijaiset motiivit, tarpeet tai ongelmat, jotka tekevät tästä arkkitehtuuripäätöksestä
välttämättömän. Ajattele taustalla olevia syitä ja paineita.}

* {esim. Kehitämme uutta ominaisuutta/kyvykkyyttä, joka tarvitsee...}

* {esim. Meidän täytyy parantaa suorituskykyä, saavutettavuutta, poistaa velkaa...}

* {esim. Käyttäjäpalaute viittaa siihen, että...}

* {esim. Nykyinen lähestymistapa asettaa nämä rajoitukset...}

## Vaihtoehdot

{Tässä luettelet eri vaihtoehdot, joita harkitset. Pysy tosiasioissa ja vältä
mielipiteitä, seuraava osio käsittelee analyysin. Sisällytä ytimekäs kuvaus,
linkit olennaiseen dokumentaatioon tai esimerkkeihin.

Sisällytä kaikki merkittävät tutkimasi vaihtoehdot, vaikka niitä ei lopulta
valittaisikaan. Tavoitteena on antaa lukijoille selkeä, puolueeton ymmärrys jokaisesta
vaihtoehdosta ennen kuin sukellat arviointiin.}

### {Vaihtoehto 1: otsikko}

{Kuvaile vaihtoehto, anna yhteenveto, luettele tosiasiat, anna linkkejä jne.}

### {Vaihtoehto n: otsikko}

...

## Vaihtoehtojen analyysi

{Tässä arvioit kriittisesti jokaisen *Vaihtoehdot*-osiossa esitetyn vaihtoehdon.
Anna kustakin vaihtoehdosta tasapainoinen kuva sen eduista,
haitoista ja muista olennaisista huomioista tai kompromisseista. Ole täsmällinen ja,
mahdollisuuksien mukaan, yhdistä kohtasi takaisin *Ajureihin*.

Harkitse näkökohtia kuten:

* Kustannus (kehitys, käyttö, lisensointi)

* Monimutkaisuus (toteutus, ylläpito, oppimiskäyrä)

* Riskit (tekniset, operatiiviset, tietoturva)

* Yhdenmukaisuus arkkitehtuuriperiaatteiden tai olemassa olevien standardien kanssa

* Vaikutus suorituskykyyn, skaalautuvuuteen, käytettävyyteen, ylläpidettävyyteen,
    tietoturvaan jne.

Sisällytä niin monta Hyvä/Huono/Muu-lausuntoa kuin tarvitaan.
}

### {Vaihtoehto 1: arviointi}

* Hyvä: {Tämän vaihtoehdon tietty etu tai hyöty.}

* Huono: {Tähän vaihtoehtoon liittyvä tietty haitta, riski tai kustannus.}

* Muu: {Olennainen seikka, joka ei ole tiukasti hyvä eikä huono.}

### {Vaihtoehto n: arviointi}

...

## Suositus

{Tässä ilmaiset selkeästi lopullisen päätöksen ja nimeät nimenomaisesti
valitun vaihtoehdon. Selitä yksityiskohtaisesti, **miksi** tämä vaihtoehto valittiin.
Ilmaise selkeästi, miten valittu vaihtoehto vastaa parhaiten *Ajureihin*
ja täyttää keskeiset vaatimukset tai ratkaisee esitetyn ongelman.}

### Seuraukset

{Tämä osio on **valinnainen**.}

{Nyt kun päätös on tehty, mitkä ovat odotetut tulokset ja vaikutukset,
sekä myönteiset että kielteiset? Mitä tunnettuja rajoituksia, kustannuksia tai riskejä
hyväksytään tekemällä tämä päätös? Miten tämä päätös vaikuttaa eri
sidosryhmiin, muihin järjestelmiin, kehityskäytäntöihin, toimintamenettelyihin tai
käyttökokemukseen?}

* Hyvä: {Tietty myönteinen tulos tai hyöty, jota tältä päätökseltä odotetaan.}

* Huono: {Tietty hyväksytty haitta, kustannus tai riski, joka seuraa tästä
    päätöksestä. }

* Muu: {Seuraus, joka ei ole tiukasti hyvä eikä huono.}

### Vahvistus

{Tämä osio on **valinnainen**.}

{Hahmottele, miten tämän päätöksen toteutus todennetaan ja miten jatkuva
vaatimustenmukaisuus varmistetaan. Tämä auttaa osoittamaan, että päätös
ei ole vain teoreettinen vaan se pannaan aktiivisesti täytäntöön ja sitä seurataan.

Miten tarkistat, että päätös on toteutettu oikein? (esim. koodikatselmoinnit,
erityiset testit, demonstraatiot, vertaiskatselmointi).

Miten päätöksen noudattamista ylläpidetään ajan myötä? (esim. automaattiset
tarkistukset, määräaikaiset auditoinnit, tiimin ohjeiden päivitykset, koulutus).

Onko olemassa erityisiä mittareita tai indikaattoreita, jotka osoittavat päätöksen
saavuttavan aiotut myönteiset tulokset? (esim. suorituskykyvertailut,
käyttöönottoasteet, tiettyjen virheiden väheneminen, käyttäjäpalautepisteet).

Kuka vastaa tämän valvonnasta, ja mitä tapahtuu, jos päätöstä ei noudateta?}

## Lisätietoja

{Tämä osio on **valinnainen**.}

{Käytä tätä osiota antaaksesi täydentävää tietoa, joka tukee
päätöstä, lisää kontekstia tai ohjaa tulevia toimia. Linkit muihin päätöksiin
ja resursseihin voivat ilmestyä myös tänne.

Voit lyhyesti mainita, ketkä osallistuivat päätöksentekoprosessiin ja
saavutettiinko konsensus ja miten. Voit myös ehdottaa aikajännettä tai
erityisiä tapahtumia, jotka voisivat johtaa tämän päätöksen uudelleenarviointiin
tulevaisuudessa.}
