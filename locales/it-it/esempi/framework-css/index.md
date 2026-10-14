# Registro delle decisioni architetturali: framework CSS

Indice:

- [Riepilogo](#riepilogo)
  - [Questione](#questione)
  - [Decisione](#decisione)
  - [Stato](#stato)
- [Dettagli](#dettagli)
  - [Ipotesi](#ipotesi)
  - [Vincoli](#vincoli)
  - [Posizioni](#posizioni)
  - [Argomento](#argomento)
  - [Implicazioni](#implicazioni)
- [Correlato](#correlato)
  - [Decisioni correlate](#decisioni-correlate)
  - [Requisiti correlati](#requisiti-correlati)
  - [Artefatti correlati](#artefatti-correlati)
  - [Principi correlati](#principi-correlati)
- [Note](#note)


## Riepilogo


### Questione

Vogliamo usare un framework CSS per creare le nostre applicazioni web:

  * Vogliamo che l'esperienza utente sia veloce e affidabile, su tutti i browser e le dimensioni dello schermo più diffusi.

  * Vogliamo un'iterazione rapida su design, layout, UI/UX ecc.

  * Vogliamo applicazioni responsive, soprattutto per schermi più piccoli come quelli dei dispositivi mobili, schermi più grandi come i widescreen 4K e schermi dinamici come i display ruotabili.  


### Decisione

Scelto Bulma.


### Stato

Scelto Bulma. Aperti a nuove scelte di framework CSS man mano che arrivano.


## Dettagli


### Ipotesi

Vogliamo creare app web moderne, veloci, affidabili, responsive ecc.

Le tipiche app web moderne stanno riducendo o eliminando l'uso di jQuery per più motivi: 

  * Il JavaScript moderno sta introducendo gradualmente molte capacità che jQuery ha fornito, quindi jQuery è meno necessario e ci sono moduli migliori/più veloci/più piccoli che forniscono implementazioni specifiche

  * L'approccio ampio di jQuery è la manipolazione diretta del DOM, che è un anti-pattern per i framework JavaScript moderni (per esempio React, Vue, Svelte)

  * jQuery interferisce con se stesso se viene caricato due volte ecc.


### Vincoli

Se scegliamo un framework CSS che usa jQuery, siamo costretti a importare jQuery. Per esempio, Semantic UI usa jQuery e Tachyons no.

Se scegliamo un framework CSS minimale, rinunciamo ai componenti del framework che potremmo volere ora o presto. Per esempio, Semantic UI fornisce un carosello di immagini e Tachyons no.


### Posizioni

Abbiamo considerato di non usare alcun framework. Questo sembra ancora praticabile, soprattutto perché CSS grid fornisce gran parte di ciò che serve al nostro progetto.

Abbiamo considerato molti framework CSS con una rapida selezione per shortlist: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons ecc. Le nostre due selezioni per una revisione più approfondita sono Semantic UI (perché ha l'approccio più semantico) e Bulma (perché ha l'approccio più leggero che fornisce i componenti che vogliamo ora).

Abbiamo considerato Semantic UI. Fornisce molti componenti, compresi quelli che vogliamo per il nostro progetto: schede, griglie, pulsanti ecc. Abbiamo fatto un pilota con Semantic UI in due modi: usando tipici file CDN e usando repository NPM. Abbiamo ottenuto successo con Semantic UI in una pagina HTML statica, ma non nel nostro tempo massimo per costruire una SPA JavaScript (principalmente a causa di problemi di caricamento di jQuery). Abbiamo scoperto che altri programmatori hanno chiesto agli sviluppatori di Semantic UI di creare una versione senza jQuery, per gli stessi motivi per cui lo facciamo noi. Altri programmatori chiedono da molti anni una versione senza jQuery, ma gli sviluppatori hanno detto di no e hanno affermato che qualsiasi versione senza jQuery sarebbe troppo difficile da scrivere, per esempio ~"il progetto Semantic UI ha più di 22.000 punti di contatto che usano jQuery".

Esempio con Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Abbiamo considerato Bulma. Bulma ha molte capacità simili a Semantic UI, anche se non altrettanti componenti sofisticati. Bulma è costruito con tecniche moderne, come l'assenza di jQuery. Bulma ha alcuni componenti di terze parti, alcuni dei quali potremmo voler usare.


Esempio con Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argomento

Come sopra.

In particolare, Semantic UI sembra avere una bandierina di cautela sia in termini di tecnologia (cioè così tanti punti di contatto con jQuery) sia in termini di leadership (cioè la versione senza jQuery è stata un no netto, anziché tentare una roadmap, un miglioramento continuo, una raccolta fondi con donazioni ecc.).


### Implicazioni

Se troviamo un buon framework CSS senza jQuery, questo è in generale utile e positivo.


## Correlato


### Decisioni correlate

Il framework CSS che scegliamo può influire sulla testabilità.


### Requisiti correlati

Vogliamo consegnare rapidamente un'app puramente moderna. 

Non vogliamo spendere tempo a lavorare su framework più vecchi (in particolare Semantic UI) con dipendenze più vecchie (in particolare jQuery).


### Artefatti correlati

Influisce su tutto il tipico HTML che userà il CSS.


### Principi correlati

Facilmente reversibile.

Necessità di velocità.


## Note

Eventuali note qui.
