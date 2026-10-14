# [000] Titel
*Vergeben Sie für jeden ADR eine Nummer zur einfachen Referenzierung und Katalogisierung* \
*HINWEIS: Alle kursiven Texte sind Hinweise und sollten für die Produktivversion entfernt werden*

## Status - DRAFT / ACTIVE /  DEPRECATED by [000] / SUPERSEDES [000]

## Kontext
*Beschreiben Sie kurz das/die Problem(e), das/die dieser ADR adressieren soll, und warum die Probleme bestehen.*

## Beschlossener Ansatz
*Beschreiben Sie im Detail die architektonisch bedeutsame Entscheidung, die getroffen wurde/wird, und beschreiben Sie, wie sie die im Abschnitt „Kontext“ umrissenen Probleme angeht.*

## Konsequenzen
*Welche Auswirkungen hat diese Entscheidung auf die Architekturmerkmale und funktionalen Anforderungen des Systems?*

## Governance
*Wie werden die Ergebnisse dieser Entscheidung überwacht?* \
*Wie wird die Einhaltung dieser Entscheidung sichergestellt?*

## Optionsanalyse
*Falls zutreffend, fügen Sie jede Abwägungsanalyse bei oder verlinken Sie sie, die durchgeführt wurde, um zu der in diesem Dokument getroffenen Entscheidung zu gelangen.*

### Legende
*Optional: Stellen Sie den Stakeholdern visuelle Hilfen bereit, die helfen, die positiven und negativen Abwägungen schnell zu erkennen – zum Beispiel einfache Ampelhervorhebungen mit positiven oder negativen Präfixen.*

Ein <span style="background-color:#4bce97; color:black;">grüner</span> Hintergrund zeigt eine gute Passung an, die über <span style="background-color:#f1c232; color:black;">Gelb</span> schlechter wird, wobei <span style="background-color:#e06666; color:black;">Rot</span> die schlechteste Passung ist. \
\+ kennzeichnet einen Kommentar mit positiver Wirkung \
\- kennzeichnet einen Kommentar mit negativer Wirkung

### Überblick
*Wie gut passt jede Option auf den ersten Blick zum Problemkontext?*

<table>
  <thead>
    <tr>
      <th>Zusammenfassung</th>
      <th>Option 1</th>
      <th>Option 2</th>
      <th>Option 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Einfachheit der Umsetzung</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Supereinfach
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Knifflig
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Große Umsetzung, die Expertenwissen erfordert
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Zeitrahmen</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Sehr schnell
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Ziemlich langsam
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Sehr langsam
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Strategischer Wert</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Kein strategischer Wert, rein taktisch
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Verbessert das Onboarding-Erlebnis der Kunden leicht
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ideal für die bevorstehende Fusion
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Funktionale Anforderungen
*Wie gut passt jede mögliche Option zu den gewünschten funktionalen Anforderungen?*

<table>
  <thead>
    <tr>
      <th>Szenario</th>
      <th><i>Option 1</i></th>
      <th><i>Option 2</i></th>
      <th><i>Option 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Szenario 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Szenario 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Szenario 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Optional: Fügen Sie Zeilen / eine weitere Tabelle hinzu, um bekannte künftige Szenarien abzudecken.*

### Nichtfunktionale Anforderungen
*Wie gut passt jede mögliche Option zu den gewünschten Architekturmerkmalen?
Hinweis: ‚Architekturmerkmale‘ wäre ein passenderer Titel, passen Sie ihn aber an die Ihrem Geschäftsbereich vertraute Sprache an.*

<table>
  <thead>
    <tr>
      <th>Architektur- </br> merkmal</th>
      <th><i>Option 1</i></th>
      <th><i>Option 2</i></th>
      <th><i>Option 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Skalierbarkeit</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Leistung</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Verfügbarkeit</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Optional: Fügen Sie Definitionen der Architekturmerkmale hinzu oder verlinken Sie sie, soweit sie für Ihr Geschäft / Ihr Produkt relevant sind.*
