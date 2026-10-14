# [000] Titel
*Nummerér hver ADR for nem reference og kategorisering* \
*Bemærk: al kursiv tekst er hints og bør fjernes ved faktisk brug*

## Status - DRAFT / ACTIVE /  DEPRECATED by [000] / SUPERSEDES [000]

## Kontekst
*Beskriv kort det problem, som denne ADR sigter mod at løse, og hvorfor det findes.*

## Valgt tilgang
*Beskriv i detaljer den eller de arkitektonisk væsentlige beslutninger, der er eller vil blive truffet, og forklar, hvordan de løser problemet beskrevet i afsnittet Kontekst.*

## Konsekvenser
*Hvordan påvirker denne beslutning systemets arkitekturkarakteristika og funktionelle krav?*

## Governance
*Hvordan overvåges konsekvenserne af denne beslutning?* \
*Hvordan sikres overholdelse af denne beslutning?*

## Analyse af muligheder
*Hvis relevant, medtag eller link til den afvejningsanalyse, der blev udført for at nå frem til beslutningen i dette dokument.*

### Signaturforklaring
*Valgfrit: giv et visuelt hjælpemiddel, der hjælper interessenter med hurtigt at se positive og negative afvejninger, for eksempel enkel trafiklysmarkering med et positivt eller negativt præfiks.*

<span style="background-color:#4bce97; color:black;">Grøn</span> baggrund angiver et godt match, forværres via <span style="background-color:#f1c232; color:black;">gul</span> til <span style="background-color:#e06666; color:black;">rød</span> som det dårligste match. \
\+ angiver en kommentar med positiv indflydelse \
\- angiver en kommentar med negativ indflydelse

### Overordnet oversigt
*Vis med et blik, hvor godt hver mulighed passer til problemkonteksten.*

<table>
  <thead>
    <tr>
      <th>Oversigt</th>
      <th>Mulighed 1</th>
      <th>Mulighed 2</th>
      <th>Mulighed 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Nem implementering</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Meget nem
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Vanskelig
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Stor implementering, der kræver specialistviden
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Tidslinje</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Meget hurtig
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Ret langsom
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Meget langsom
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Strategisk værdi</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Ingen strategisk værdi, rent taktisk
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Forbedrer kunders onboarding-oplevelse en smule
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ideel til en kommende fusion
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Funktionelle krav
*Hvor godt passer hver mulig mulighed til de ønskede funktionelle krav?*

<table>
  <thead>
    <tr>
      <th>Scenarie</th>
      <th><i>Mulighed 1</i></th>
      <th><i>Mulighed 2</i></th>
      <th><i>Mulighed 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Scenarie 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scenarie 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scenarie 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Valgfrit: tilføj rækker eller en anden tabel for at dække kendte fremtidige scenarier.*

### Ikke-funktionelle krav
*Hvor godt passer hver mulig mulighed til de ønskede arkitekturkarakteristika?
Bemærk: 'Arkitekturkarakteristika' er en mere passende titel, men tilpas til termer, der er kendt i forretningsdomænet.*

<table>
  <thead>
    <tr>
      <th>Arkitektur </br> karakteristik</th>
      <th><i>Mulighed 1</i></th>
      <th><i>Mulighed 2</i></th>
      <th><i>Mulighed 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Udvidelsesmuligheder</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Ydeevne</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Tilgængelighed</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Valgfrit: tilføj eller link til definitioner af arkitekturkarakteristika, der er relevante for forretningen/produktet.*
