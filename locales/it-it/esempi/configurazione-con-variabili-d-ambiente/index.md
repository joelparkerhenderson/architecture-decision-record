# Configurazione con variabili d'ambiente

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

Vogliamo che le nostre applicazioni siano configurabili al di là di artefatti/binari/sorgenti, in modo che una singola build possa comportarsi in modo diverso a seconda dell'ambiente di deployment.

  * Per ottenere questo, vogliamo usare la configurazione con variabili d'ambiente.

  * Vogliamo gestire la configurazione usando file che possiamo mettere sotto controllo di versione.

  * Vogliamo offrire un po' di ergonomia nell'esperienza dello sviluppatore, come sapere che cosa si può configurare e quali sono i relativi valori predefiniti.


### Decisione

Scelti file .env con relativo file dei valori predefiniti e file di schema.


### Stato

Deciso. Aperti a considerare nuove capacità man mano che emergono.


## Dettagli


### Ipotesi

Preferiamo separare il codice dell'applicazione e il codice dell'ambiente. Ipotizziamo che l'app debba funzionare in modo diverso in ambienti diversi, come un ambiente di sviluppo, un ambiente di test, un ambiente demo, un ambiente di produzione ecc.

Preferiamo la pratica di settore "12 factor app" e ancora di più la pratica correlata "15 factor app".

Molti dei nostri progetti precedenti hanno usato la convenzione di un file `.env` o di una directory `.env` simile. Esiste una pratica tipica di tenere questi file fuori dal controllo di versione e di usare invece un altro modo per distribuirli, versionarli e gestirli.


### Vincoli

Vogliamo tenere i segreti fuori dal nostro sistema di controllo di versione (VCS) per la gestione del codice sorgente (SCM).

Vogliamo puntare alla compatibilità con framework e librerie software popolari. Per esempio, Node ha un modulo "dotenv" per leggere la configurazione con variabili d'ambiente.


### Posizioni

Abbiamo considerato alcuni approcci:

  * Archiviare la configurazione nell'app, per esempio in un file `config.js`.

  * Archiviare la configurazione nell'ambiente, per esempio in un file `.env`.

  * Recuperare la configurazione da una posizione nota, come un server delle licenze.


### Argomento

Abbiamo scelto l'approccio del file .env perché:

  * È popolare, anche tra gli esperti.

  * Segue il pattern dei file `.env` che i nostri team hanno usato con successo molte volte in molti progetti.

  * È semplice. In particolare, per ora ci stanno bene i compromessi significativi che vediamo, come la mancanza di capacità di audit rispetto a un approccio con un server delle licenze.


### Implicazioni

Dobbiamo trovare un modo per separare la configurazione con variabili d'ambiente che è pubblica dalla gestione dei segreti.


## Correlato


### Decisioni correlate

Ci aspettiamo che tutte le nostre applicazioni usino questo approccio.

Pianificheremo di aggiornare tutte le nostre applicazioni che usano un approccio meno capace, come l'hardcoding in un binario o nel codice sorgente.

Lasceremo invariate tutte le nostre applicazioni che usano un approccio più capace, come un server delle licenze.


### Requisiti correlati

Aggiungeremo capacità devops per i file, inclusi hook, test e integrazione continua.

Dobbiamo formare tutti i colleghi sviluppatori su questa decisione.



### Artefatti correlati

Ogni area in cui distribuiamo avrà bisogno del proprio file .env e dei relativi file.


### Principi correlati

Facilmente reversibile.


## Note


File di esempio `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

File di esempio `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

File di esempio `.env.schema` con solo le chiavi:

```env
NAME
EMAIL
```
