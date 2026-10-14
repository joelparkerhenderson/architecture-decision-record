# Monorepo o multirepo

Indice:

* [Riepilogo](#riepilogo)
  * [Questione](#questione)
  * [Decisione](#decisione)
  * [Stato](#stato)
* [Dettagli](#dettagli)
  * [Ipotesi](#ipotesi)
  * [Vincoli](#vincoli)
  * [Posizioni](#posizioni)
  * [Argomento](#argomento)
  * [Implicazioni](#implicazioni)
* [Correlato](#correlato)
  * [Decisioni correlate](#decisioni-correlate)
  * [Requisiti correlati](#requisiti-correlati)
  * [Artefatti correlati](#artefatti-correlati)
  * [Principi correlati](#principi-correlati)
* [Note](#note)


## Riepilogo


### Questione

Il nostro progetto comporta lo sviluppo di tre categorie principali di software:

  * GUI front-end
  * Servizi middleware
  * Server back-end

Quando sviluppiamo, il nostro sistema di controllo di versione (VCS) per la gestione del codice sorgente (SCM) è git.

Dobbiamo scegliere come usare git per organizzare il nostro codice.

La scelta di primo livello è organizzare come "monorepo", "polyrepo" o "ibrido":

  * Monorepo significa che mettiamo tutte le parti in un unico grande repository
  * Polyrepo significa che mettiamo ogni parte nel proprio repository
  * Ibrido significa un misto di monorepo e polyrepo

Per saperne di più vedi https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Decisione

Monorepo quando un'organizzazione/team/progetto è relativamente piccolo e l'iterazione rapida ha priorità più alta del mantenimento della stabilità.

Polyrepo quando un'organizzazione/team/progetto è relativamente grande e il mantenimento della stabilità ha priorità più alta dell'iterazione rapida.


### Stato

Deciso. Aperti a rivedere se/quando saranno disponibili nuovi strumenti per gestire monorepo e/o polyrepo.


## Dettagli


### Ipotesi

Tutto il codice che sviluppiamo è per le offerte di un'organizzazione e non per il grande pubblico. Cioè il broker-dealer non punta ad avere qualcosa come sviluppatori volontari del grande pubblico.


### Vincoli

I vincoli sono ben documentati su https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Posizioni

Abbiamo considerato i monorepo nello stile di Google, Facebook ecc. Pensiamo che eventuali problemi di scalabilità dei monorepo siano così lontani nel futuro che, quando ne avremo bisogno, saremo in grado di sfruttare le stesse pratiche di Google e Facebook.

Abbiamo considerato i polyrepo nello stile dei tipici progetti open source Git, come Google Android, Facebook React ecc. Pensiamo che siano la scelta migliore per la partecipazione del grande pubblico (per esempio chiunque al mondo può lavorare sul codice) e per la disponibilità individuale (per esempio il progetto è usato da solo, senza altre parti).


### Argomento

Quando un'organizzazione/team/progetto è relativamente piccolo, scegliamo il monorepo, perché l'iterazione rapida ha una priorità significativamente più alta del mantenimento della stabilità

Quando un'organizzazione/team/progetto è relativamente grande, scegliamo il polyrepo, perché il mantenimento della stabilità ha una priorità significativamente più alta dell'iterazione rapida.


### Implicazioni

Se esiste già una pipeline per CI+CD, potremmo doverla adattare per testare più progetti all'interno di un repository.

CI+CD potrebbe richiedere più tempo per una build completa di un monorepo, perché CI+CD potrebbe costruire tutti i progetti nel monorepo.

Se un'organizzazione/team/progetto cresce, il monorepo avrà problemi di scalabilità.

I problemi di scalabilità del monorepo possono rendere sempre più utile la transizione a un polyrepo.

La transizione da monorepo a polyrepo è un compito devops significativo e dovrà essere pianificata, gestita e programmata.


## Correlato


### Decisioni correlate

Creeremo decisioni per gli strumenti correlati per gestire monorepo (per esempio Google Bazel) e polyrepo (per esempio Lyft Refactorator).


### Requisiti correlati

Dobbiamo sviluppare la pipeline CI+CD perché funzioni bene con git.


### Artefatti correlati

Ci aspettiamo che l'organizzazione del repository abbia artefatti correlati per provisioning, gestione della configurazione, test e aree devops simili. 


### Principi correlati

Facilmente reversibile. Se il monorepo non funziona nella pratica o non è voluto dalla leadership, è semplice passare al polyrepo.

Ossessione per il cliente. Diamo valore al mettere il progetto nelle mani dei clienti e crediamo che un monorepo possa portarci lì più velocemente di un polyrepo e anche aiutarci a iterare più velocemente.

Pensare in grande. Google e Facebook sono sostenitori molto forti dei monorepo rispetto ai polyrepo, perché tutte le offerte principali possono essere sviluppate/testate/distribuite di concerto.


## Note

Aggiungi qui eventuali note.
