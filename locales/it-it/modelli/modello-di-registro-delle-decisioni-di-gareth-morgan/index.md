# [000] Titolo
*Numera ogni ADR per facilitare il riferimento e la categorizzazione* \
*Nota: tutto il testo in corsivo è un suggerimento e dovrebbe essere rimosso nell'uso effettivo*

## Stato - DRAFT / ACTIVE /  DEPRECATED by [000] / SUPERSEDES [000]

## Contesto
*Descrivi brevemente il problema che questo ADR intende affrontare e perché esiste.*

## Approccio scelto
*Descrivi in dettaglio la o le decisioni architetturalmente significative che sono state o saranno prese e spiega come risolvono il problema delineato nella sezione Contesto.*

## Conseguenze
*Qual è l'effetto di questa decisione sulle caratteristiche architetturali e sui requisiti funzionali del sistema?*

## Governance
*Come vengono monitorate le conseguenze di questa decisione?* \
*Come viene garantito il rispetto di questa decisione?*

## Analisi delle opzioni
*Se pertinente, includi o collega l'analisi dei compromessi svolta per arrivare alla decisione presente in questo documento.*

### Legenda
*Facoltativo: fornisci un aiuto visivo che aiuti le parti interessate a vedere rapidamente i compromessi positivi e negativi, per esempio una semplice evidenziazione a semaforo con un prefisso positivo o negativo.*

Lo sfondo <span style="background-color:#4bce97; color:black;">verde</span> indica una buona corrispondenza, che peggiora passando per il <span style="background-color:#f1c232; color:black;">giallo</span> fino al <span style="background-color:#e06666; color:black;">rosso</span> come peggiore corrispondenza. \
\+ indica un commento con influenza positiva \
\- indica un commento con influenza negativa

### Panoramica di alto livello
*Mostra a colpo d'occhio quanto ciascuna opzione si adatta al contesto del problema.*

<table>
  <thead>
    <tr>
      <th>Riepilogo</th>
      <th>Opzione 1</th>
      <th>Opzione 2</th>
      <th>Opzione 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Facilità di implementazione</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Molto facile
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Difficile
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Grande implementazione che richiede conoscenze specialistiche
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Tempistica</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Molto veloce
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Piuttosto lenta
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Molto lenta
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Valore strategico</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Nessun valore strategico, puramente tattico
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Migliora leggermente l'esperienza di onboarding dei clienti
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ideale per una fusione imminente
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Requisiti funzionali
*Quanto ciascuna opzione possibile si adatta ai requisiti funzionali desiderati?*

<table>
  <thead>
    <tr>
      <th>Scenario</th>
      <th><i>Opzione 1</i></th>
      <th><i>Opzione 2</i></th>
      <th><i>Opzione 3</i></th>
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

*Facoltativo: aggiungi righe o un'altra tabella per coprire scenari futuri noti.*

### Requisiti non funzionali
*Quanto ciascuna opzione possibile si adatta alle caratteristiche architetturali desiderate?
Nota: 'Caratteristiche architetturali' è un titolo più appropriato, ma adattalo ai termini familiari al dominio aziendale.*

<table>
  <thead>
    <tr>
      <th>Caratteristica </br> architetturale</th>
      <th><i>Opzione 1</i></th>
      <th><i>Opzione 2</i></th>
      <th><i>Opzione 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Estensibilità</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Prestazioni</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Disponibilità</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Facoltativo: aggiungi o collega definizioni delle caratteristiche architetturali rilevanti per l'azienda/il prodotto.*
