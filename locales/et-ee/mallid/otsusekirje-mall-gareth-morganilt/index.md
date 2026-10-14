# [000] Pealkiri
*Nummerda iga ADR hõlpsa viitamise ja kategoriseerimise jaoks* \
*Märkus: kogu kursiivtekst on vihjed ja tuleks tegelikul kasutamisel eemaldada*

## Olek - DRAFT / ACTIVE /  DEPRECATED by [000] / SUPERSEDES [000]

## Kontekst
*Kirjelda lühidalt probleemi, mida see ADR käsitleda soovib, ja miks see olemas on.*

## Valitud lähenemine
*Kirjelda üksikasjalikult arhitektuuriliselt olulisi otsuseid, mis on tehtud või tehakse, ja selgita, kuidas need lahendavad konteksti jaotises toodud probleemi.*

## Tagajärjed
*Kuidas see otsus mõjutab süsteemi arhitektuuriomadusi ja funktsionaalseid nõudeid?*

## Juhtimine
*Kuidas selle otsuse tagajärgi jälgitakse?* \
*Kuidas tagatakse selle otsuse järgimine?*

## Valikute analüüs
*Kui asjakohane, lisa või lingi kompromissianalüüs, mis tehti selles dokumendis toodud otsuseni jõudmiseks.*

### Legend
*Valikuline: paku visuaalset abivahendit, mis aitab huvirühmadel kiiresti näha positiivseid ja negatiivseid kompromisse, näiteks lihtne valgusfoori esiletõstmine positiivse või negatiivse prefiksiga.*

<span style="background-color:#4bce97; color:black;">Roheline</span> taust näitab head sobivust, halvenedes läbi <span style="background-color:#f1c232; color:black;">kollase</span> <span style="background-color:#e06666; color:black;">punaseni</span> kui halvima sobivuseni. \
\+ tähistab positiivse mõjuga kommentaari \
\- tähistab negatiivse mõjuga kommentaari

### Kõrgetasemeline ülevaade
*Näita ühe pilguga, kui hästi iga valik probleemi kontekstiga sobib.*

<table>
  <thead>
    <tr>
      <th>Kokkuvõte</th>
      <th>Valik 1</th>
      <th>Valik 2</th>
      <th>Valik 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Teostuse lihtsus</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Väga lihtne
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Keeruline
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Suur teostus, mis nõuab spetsialisti teadmisi
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Ajakava</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Väga kiire
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Üsna aeglane
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Väga aeglane
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Strateegiline väärtus</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Strateegiline väärtus puudub, puhtalt taktikaline
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Parandab veidi klientide kasutuselevõtukogemust
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ideaalne eelseisva ühinemise jaoks
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Funktsionaalsed nõuded
*Kui hästi sobib iga võimalik valik soovitud funktsionaalsete nõuetega?*

<table>
  <thead>
    <tr>
      <th>Stsenaarium</th>
      <th><i>Valik 1</i></th>
      <th><i>Valik 2</i></th>
      <th><i>Valik 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Stsenaarium 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Stsenaarium 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Stsenaarium 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Valikuline: lisa ridu või teine tabel teadaolevate tulevaste stsenaariumide katmiseks.*

### Mittefunktsionaalsed nõuded
*Kui hästi sobib iga võimalik valik soovitud arhitektuuriomadustega?
Märkus: 'Arhitektuuriomadused' on sobivam pealkiri, kuid kohanda ärivaldkonnas tuttavate terminitega.*

<table>
  <thead>
    <tr>
      <th>Arhitektuuri </br> omadus</th>
      <th><i>Valik 1</i></th>
      <th><i>Valik 2</i></th>
      <th><i>Valik 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Laiendatavus</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Jõudlus</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Käideldavus</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Valikuline: lisa või lingi äri/toote jaoks asjakohaste arhitektuuriomaduste määratlused.*
