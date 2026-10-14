# Linguaggi di programmazione

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

Dobbiamo scegliere i linguaggi di programmazione per il nostro software. Abbiamo due grandi esigenze: un linguaggio di programmazione front-end adatto alle applicazioni web e un linguaggio di programmazione back-end adatto alle applicazioni server.


### Decisione

Scegliamo TypeScript per il front-end.

Scegliamo Rust per il back-end.


### Stato

Deciso. Siamo aperti a nuove alternative man mano che emergono.


## Dettagli


### Ipotesi

Le applicazioni front-end sono tipiche:

  * Utenti e interazioni tipici

  * Browser e sistemi tipici

  * Sviluppi e deployment tipici

È probabile che le applicazioni front-end evolvano rapidamente:

  * Vogliamo garantire sviluppi, deployment, iterazioni ecc. rapidi e semplici.

  * Diamo valore alla dimostrabilità, come la sicurezza dei tipi, e siamo disposti a fare un po' più di lavoro per ottenerla.

  * Non ci serve la compatibilità con il legacy.

Le applicazioni back-end sono superiori al tipico:

  * Obiettivi superiori al tipico per la qualità, in particolare dimostrabilità, affidabilità, sicurezza ecc.

  * Obiettivi superiori al tipico per il quasi tempo reale, cioè non vogliamo pause dovute alla garbage collection della macchina virtuale.

  * Obiettivi superiori al tipico per la programmazione funzionale, in particolare per la parallelizzazione, l'elaborazione multicore e la sicurezza della memoria.

Accettiamo velocità di compilazione inferiori a favore della sicurezza in fase di compilazione e delle velocità di runtime.


### Vincoli

Abbiamo un forte vincolo sui linguaggi utilizzabili con i servizi per funzioni dei principali fornitori cloud, come Amazon Lambda.


### Posizioni

Abbiamo considerato questi linguaggi:

  * C

  * C++

  * Clojure
  
  * Elixir
  
  * Erlang
  
  * Elm
  
  * Flow
  
  * Go
  
  * Haskell
  
  * Java
  
  * JavaScript
  
  * Kotlin
  
  * Python
  
  * Ruby
  
  * Rust
  
  * TypeScript



### Argomento

Riepilogo per linguaggio:

  * C: scartato per la bassa sicurezza; Rust può fare quasi tutto meglio.

  * C++: scartato perché è un pasticcio; Rust può fare quasi tutto meglio.

  * Clojure: modellazione eccellente; la migliore approssimazione di Lisp; ottimo runtime sulla JVM.
  
  * Elixir: runtime eccellente inclusa la distribuibilità e la concorrenza; esperienza di sviluppo eccellente; ecosistema relativamente piccolo.

  * Erlang: runtime eccellente inclusa la distribuibilità e la concorrenza; esperienza di sviluppo impegnativa; ecosistema relativamente piccolo.

  * Elm: sembra molto promettente; IBM sta pubblicando importanti casi di studio con buoni risultati; ecosistema più piccolo.

  * Flow: interessante miglioramento rispetto a JavaScript; tuttavia gli sviluppatori se ne stanno allontanando.

  * Go: esperienza di sviluppo eccellente; concorrenza eccellente; ma una storia di decisioni sbagliate che paralizzano il linguaggio.

  * Haskell: il miglior linguaggio funzionale; comunità di sviluppatori più piccola; non ha ottenuto abbastanza successi di produzione pubblicati.

  * Java: runtime eccellente; ecosistema eccellente; esperienza di sviluppo mediocre.

  * JavaScript: il linguaggio più popolare di sempre; l'ecosistema più diffuso.

  * Kotlin: corregge tanta parte di Java; eccellente sostegno di JetBrains; buoni casi pubblicati di porting da Java a Kotlin.
  
  * Python: linguaggio più popolare per l'amministrazione di sistema; ottimi strumenti di analisi; buoni framework web; ma abbandonato da Google a favore di Go.

  * Ruby: la migliore esperienza di sviluppo di sempre; i migliori framework web; la comunità più simpatica; ma molto lento; piuttosto difficile da impacchettare.

  * Rust: il miglior nuovo linguaggio; enfasi sulla zero-abstraction; enfasi sulla concorrenza; tuttavia ecosistema relativamente piccolo; e ha limiti deliberati su alcuni tipi di accelerazioni del compilatore, per esempio l'accesso diretto alla memoria deve essere esplicitamente unsafe.

  * TypeScript: aggiunge tipi a JavaScript; ottimo transpiler; crescente enfasi degli sviluppatori sul porting da JavaScript a TypeScript; forte sostegno di Microsoft.

Abbiamo deciso che le VM hanno un insieme di compromessi di cui non abbiamo bisogno in questo momento, come la complessità aggiuntiva che fornisce capacità di runtime.

Crediamo che la nostra decisione di fondo sia guidata da due preoccupazioni trasversali:

  * Per la massima velocità di runtime e l'accesso più stretto al sistema, sceglieremmo JavaScript e C.

  * Per una velocità di runtime quasi massima e un accesso al sistema quasi più stretto, scegliamo TypeScript e Rust.

Menzioni d'onore vanno ai linguaggi VM e ai framework web che sceglieremmo se volessimo un linguaggio VM:

  * Clojure e Luminus

  * Java e Spring

  * Elixir e Phoenix


### Implicazioni

Gli sviluppatori front-end dovranno imparare TypeScript. Questa è probabilmente una curva di apprendimento facile se l'esperienza principale dello sviluppatore è l'uso di JavaScript.

Gli sviluppatori back-end dovranno imparare Rust. Questa è probabilmente una curva di apprendimento moderata se l'esperienza principale dello sviluppatore è l'uso di C/C++, e una curva di apprendimento difficile se l'esperienza principale è l'uso di Java, Python, Ruby o linguaggi simili con gestione automatica della memoria. 

TypeScript e Rust sono entrambi relativamente nuovi. Ciò significa che molti strumenti non hanno ancora documentazione per questi linguaggi. Per esempio, la pipeline devops dovrà essere configurata per questi linguaggi e finora nessuno degli strumenti devops che stiamo valutando ha esempi predefiniti per questi linguaggi.

I tempi di compilazione di TypeScript e Rust sono piuttosto lenti. Parte di ciò può essere dovuta alla novità dei linguaggi. Potremmo voler vedere come mitigare i tempi di compilazione lenti, per esempio con la compilazione su richiesta, la concorrenza della compilazione ecc.

Il supporto IDE per questi linguaggi non è ancora ubiquo e non ancora di prima classe. Per esempio, JetBrains vende l'IDE PyCharm per il supporto di prima classe a Python, ma non vende un IDE con supporto di prima classe per Rust; invece, JetBrains può usare un plugin Rust che fornisce forse l'80% del supporto al linguaggio Rust rispetto al supporto al linguaggio Python.


## Correlato


### Decisioni correlate

Punteremo a scelte di ecosistema allineate con questi linguaggi.

Per esempio, vogliamo scegliere un IDE con buone capacità per questi linguaggi.

Per esempio, per il nostro framework web front-end, è più probabile che decideremo per un framework che tende a puntare a TypeScript (per esempio Vue) che per un framework che tende a puntare a JavaScript semplice (per esempio React).


### Requisiti correlati

L'intera nostra toolchain deve supportare questi linguaggi.


### Artefatti correlati

Ci aspettiamo di poter esportare alcuni segreti in variabili d'ambiente.


### Principi correlati

Misura due volte, costruisci una volta. Stiamo dando priorità a un po' di sicurezza rispetto a un po' di velocità.

Il runtime è più prezioso del tempo di compilazione. Stiamo dando priorità all'uso da parte dei clienti rispetto all'uso da parte degli sviluppatori.


## Note

Eventuali note qui.
