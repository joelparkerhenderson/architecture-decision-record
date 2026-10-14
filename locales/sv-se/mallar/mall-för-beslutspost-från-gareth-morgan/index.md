# [000] Titel
*Tilldela varje ADR ett nummer för enkel referens och katalogisering* \
*OBS: All kursiv text är tips och bör tas bort i produktionsversionen*

## Tillstånd - DRAFT / ACTIVE /  DEPRECATED by [000] / SUPERSEDES [000]

## Sammanhang
*Beskriv kortfattat det/de problem som den här ADR:en är avsedd att åtgärda och varför problemen finns.*

## Beslutat tillvägagångssätt
*Beskriv i detalj det arkitektoniskt betydelsefulla beslut som har fattats / kommer att fattas och beskriv hur det åtgärdar de problem som beskrivs i avsnittet Sammanhang.*

## Konsekvenser
*Vilken inverkan har det här beslutet på systemets arkitekturegenskaper och funktionella krav?*

## Styrning
*Hur kommer utfallet av det här beslutet att följas upp?* \
*Hur säkerställs efterlevnaden av det här beslutet?*

## Alternativanalys
*Om tillämpligt, ta med eller länka till eventuell avvägningsanalys som gjorts för att komma fram till beslutet i det här dokumentet.*

### Teckenförklaring
*Valfritt: Ge intressenterna visuella hjälpmedel som kan hjälpa dem att snabbt upptäcka positiva och negativa avvägningar – till exempel enkla trafikljusmarkeringar med positiva eller negativa prefix.*

En <span style="background-color:#4bce97; color:black;">grön</span> bakgrund anger god passform, som försämras via <span style="background-color:#f1c232; color:black;">bärnsten</span>, där <span style="background-color:#e06666; color:black;">rött</span> är sämst passform. \
\+ anger en kommentar med positiv inverkan \
\- anger en kommentar med negativ inverkan

### Översikt på hög nivå
*Hur väl passar varje alternativ problemets sammanhang vid en hastig anblick?*

<table>
  <thead>
    <tr>
      <th>Sammanfattning</th>
      <th>Alternativ 1</th>
      <th>Alternativ 2</th>
      <th>Alternativ 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Enkelhet att genomföra</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Superenkelt
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Knepigt
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Stor implementation som kräver expertkunskap
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Tidsramar</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Mycket snabbt
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Ganska långsamt
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Mycket långsamt
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Strategiskt värde</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Inget strategiskt värde, rent taktiskt
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Förbättrar kundintroduktionen något
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Idealiskt för den kommande fusionen
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Funktionella krav
*Hur väl passar varje möjligt alternativ de önskade funktionella kraven?*

<table>
  <thead>
    <tr>
      <th>Scenario</th>
      <th><i>Alternativ 1</i></th>
      <th><i>Alternativ 2</i></th>
      <th><i>Alternativ 3</i></th>
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

*Valfritt: Lägg till rader / en annan tabell för att täcka kända framtida scenarier.*

### Icke-funktionella krav
*Hur väl passar varje möjligt alternativ de önskade arkitekturegenskaperna?
Obs: ’Arkitekturegenskaper’ vore en mer lämplig rubrik, men anpassa den till språkbruk som är välkänt inom din affärsdomän.*

<table>
  <thead>
    <tr>
      <th>Arkitektur- </br> egenskap</th>
      <th><i>Alternativ 1</i></th>
      <th><i>Alternativ 2</i></th>
      <th><i>Alternativ 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Skalbarhet</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Prestanda</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Tillgänglighet</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Valfritt: Lägg till eller länka till definitioner av arkitekturegenskaperna så som de avser din verksamhet / produkt.*
