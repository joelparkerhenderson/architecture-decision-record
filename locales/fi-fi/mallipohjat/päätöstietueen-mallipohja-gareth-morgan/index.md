# [000] Otsikko
*Anna jokaiselle ADR-tietueelle numero helppoa viittausta ja luettelointia varten* \
*HUOM: Kaikki kursivoitu teksti antaa vihjeitä ja tulee poistaa tuotantoversiosta*

## Tila - LUONNOS / AKTIIVINEN /  VANHENTUNUT: [000] / KORVAA [000]

## Konteksti
*Kuvaile lyhyesti ongelma/ongelmat, joihin tämä ADR pyrkii vastaamaan, ja miksi ongelmat ovat olemassa.*

## Päätetty lähestymistapa
*Kuvaile yksityiskohtaisesti arkkitehtuurisesti merkittävä päätös, joka on tehty / tullaan tekemään, ja kuvaile, miten se vastaa Konteksti-osiossa esitettyihin ongelmiin.*

## Seuraukset
*Mikä on tämän päätöksen vaikutus järjestelmän arkkitehtuuriominaisuuksiin ja toiminnallisiin vaatimuksiin?*

## Hallinto
*Miten tämän päätöksen tuloksia seurataan?* \
*Miten tämän päätöksen noudattaminen varmistetaan?*

## Vaihtoehtojen analyysi
*Tarvittaessa sisällytä mikä tahansa kompromissianalyysi, joka on tehty tässä dokumentissa tehtyyn päätökseen pääsemiseksi, tai linkitä siihen.*

### Selite
*Valinnainen: Tarjoa sidosryhmille visuaalisia apuvälineitä, jotka auttavat havaitsemaan nopeasti myönteiset ja kielteiset kompromissit — esimerkiksi yksinkertaiset liikennevalokorostukset myönteisillä tai kielteisillä etuliitteillä.*

<span style="background-color:#4bce97; color:black;">Vihreä</span> tausta osoittaa hyvää sopivuutta, heikentyen <span style="background-color:#f1c232; color:black;">keltaisen</span> kautta, ja <span style="background-color:#e06666; color:black;">punainen</span> on huonoin sopivuus. \
\+ osoittaa myönteisesti vaikuttavan kommentin \
\- osoittaa kielteisesti vaikuttavan kommentin

### Korkean tason yleiskatsaus
*Kuinka hyvin kukin vaihtoehto sopii ongelman kontekstiin yhdellä silmäyksellä?*

<table>
  <thead>
    <tr>
      <th>Yhteenveto</th>
      <th>Vaihtoehto 1</th>
      <th>Vaihtoehto 2</th>
      <th>Vaihtoehto 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Toteutuksen helppous</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Erittäin helppo
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Hankala
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Laaja toteutus, joka vaatii asiantuntemusta
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Aikataulut</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Erittäin nopea
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Melko hidas
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Erittäin hidas
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Strateginen arvo</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Ei strategista arvoa, puhtaasti taktinen
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Parantaa hieman asiakkaan perehdytyskokemusta
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ihanteellinen tulevaa yhdistymistä varten
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Toiminnalliset vaatimukset
*Kuinka hyvin kukin mahdollinen vaihtoehto sopii haluttuihin toiminnallisiin vaatimuksiin?*

<table>
  <thead>
    <tr>
      <th>Skenaario</th>
      <th><i>Vaihtoehto 1</i></th>
      <th><i>Vaihtoehto 2</i></th>
      <th><i>Vaihtoehto 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Skenaario 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Skenaario 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Skenaario 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Valinnainen: Lisää rivejä / toinen taulukko kattamaan tunnetut tulevaisuuden skenaariot.*

### Ei-toiminnalliset vaatimukset
*Kuinka hyvin kukin mahdollinen vaihtoehto sopii haluttuihin arkkitehtuuriominaisuuksiin?
Huom: 'Arkkitehtuuriominaisuudet' olisi sopivampi otsikko, mutta mukauta tämä liiketoiminta-alueellesi tuttuun kieleen.*

<table>
  <thead>
    <tr>
      <th>Arkkitehtuuri- <br> ominaisuus</th>
      <th><i>Vaihtoehto 1</i></th>
      <th><i>Vaihtoehto 2</i></th>
      <th><i>Vaihtoehto 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Skaalautuvuus</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Suorituskyky</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Käytettävyys (saatavuus)</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Valinnainen: Lisää tai linkitä arkkitehtuuriominaisuuksien määritelmät sellaisina kuin ne koskevat liiketoimintaasi / tuotettasi.*
