# [000] Titel
*Nummer elke ADR voor eenvoudige verwijzing en categorisering* \
*Let op: alle cursieve tekst zijn hints en moeten bij daadwerkelijk gebruik worden verwijderd*

## Status - DRAFT / ACTIVE /  DEPRECATED by [000] / SUPERSEDES [000]

## Context
*Beschrijf kort het probleem dat deze ADR wil aanpakken en waarom het bestaat.*

## Gekozen aanpak
*Beschrijf in detail de architectonisch significante beslissing(en) die zijn of worden genomen en leg uit hoe zij het probleem oplossen dat in de sectie Context is geschetst.*

## Gevolgen
*Wat is het effect van deze beslissing op de architectuurkenmerken en functionele eisen van het systeem?*

## Governance
*Hoe worden de gevolgen van deze beslissing gemonitord?* \
*Hoe wordt naleving van deze beslissing gewaarborgd?*

## Analyse van opties
*Voeg, indien van toepassing, de afwegingsanalyse op die is uitgevoerd om tot de beslissing in dit document te komen, of verwijs ernaar.*

### Legenda
*Optioneel: bied een visueel hulpmiddel waarmee belanghebbenden snel positieve en negatieve afwegingen kunnen zien, bijvoorbeeld eenvoudige verkeerslichtmarkeringen met een positief of negatief voorvoegsel.*

<span style="background-color:#4bce97; color:black;">Groene</span> achtergrond geeft een goede pasvorm aan, via <span style="background-color:#f1c232; color:black;">geel</span> verslechterend tot <span style="background-color:#e06666; color:black;">rood</span> als de slechtste pasvorm. \
\+ geeft een opmerking aan met een positieve invloed \
\- geeft een opmerking aan met een negatieve invloed

### Overzicht op hoog niveau
*Toon in één oogopslag hoe goed elke optie past bij de probleemcontext.*

<table>
  <thead>
    <tr>
      <th>Samenvatting</th>
      <th>Optie 1</th>
      <th>Optie 2</th>
      <th>Optie 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Implementatiegemak</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Zeer eenvoudig
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Lastig
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Grote implementatie die specialistische kennis vereist
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Tijdlijn</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Zeer snel
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Vrij traag
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Zeer traag
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Strategische waarde</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Geen strategische waarde, puur tactisch
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Verbetert de onboardingervaring van klanten enigszins
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ideaal voor een aanstaande fusie
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Functionele eisen
*Hoe goed past elke mogelijke optie bij de gewenste functionele eisen?*

<table>
  <thead>
    <tr>
      <th>Scenario</th>
      <th><i>Optie 1</i></th>
      <th><i>Optie 2</i></th>
      <th><i>Optie 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Scenario 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scenario 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scenario 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Optioneel: voeg rijen toe of een andere tabel om bekende toekomstige scenario's te dekken.*

### Niet-functionele eisen
*Hoe goed past elke mogelijke optie bij de gewenste architectuurkenmerken?
Let op: 'Architectuurkenmerken' is een geschiktere titel, maar pas aan naar termen die bekend zijn bij het bedrijfsdomein.*

<table>
  <thead>
    <tr>
      <th>Architectuur </br> kenmerk</th>
      <th><i>Optie 1</i></th>
      <th><i>Optie 2</i></th>
      <th><i>Optie 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Uitbreidbaarheid</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Prestaties</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Beschikbaarheid</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Optioneel: voeg definities toe van, of verwijs naar, architectuurkenmerken die relevant zijn voor het bedrijf/product.*
