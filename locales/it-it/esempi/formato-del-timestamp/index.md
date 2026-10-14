# Formato del timestamp

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

Vogliamo poter tracciare quando avvengono le cose usando i timestamp e un formato di timestamp coerente che funzioni bene in tutti i nostri sistemi e nei sistemi di terze parti.

Interagiamo con sistemi che hanno formati di timestamp diversi:

* I messaggi JSON non hanno un formato di timestamp nativo, quindi dobbiamo scegliere come convertire un timestamp in una stringa e una stringa in un timestamp, cioè come serializzare/deserializzare.

* Alcune applicazioni sono impostate per usare l'ora locale anziché l'ora UTC. Ciò può essere comodo per i progetti che devono adattarsi all'ora locale, come i progetti che attivano eventi basati sull'ora locale.

* Alcuni sistemi hanno esigenze e capacità di precisione temporale diverse, come usare una risoluzione temporale di secondi rispetto a millisecondi rispetto a nanosecondi. Per esempio, il comando `date` del sistema operativo Linux usa per impostazione predefinita una precisione temporale di secondi, mentre la borsa Nasdaq vuole per impostazione predefinita una precisione temporale di nanosecondi.


### Decisione

Scegliamo il formato standard di timestamp ISO 8601 con precisione al nanosecondo, in particolare "YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ".

Il formato mostra anno, mese, giorno, ora, minuto, secondo, nanosecondi e fuso orario Zulu, detto anche UTC, GMT.


### Stato

Deciso.


## Dettagli


### Ipotesi

Dobbiamo gestire queste stringhe di testo di timestamp, per convertire da timestamp a stringa (detto anche serializzare) e convertire da stringa a timestamp (detto anche deserializzare).

Vogliamo un formato che sia in generale facile da usare, facile da convertire e facile da leggere per una persona.

Vogliamo compatibilità con un'ampia gamma di sistemi esterni che non possiamo controllare, come sistemi di analisi, sistemi di database, sistemi finanziari.


### Vincoli

Alcuni sistemi hanno limitazioni di precisione temporale. Per esempio, il comando `date` del sistema operativo macOS può stampare la precisione temporale in secondi, ma non in nanosecondi.


### Posizioni

Abbiamo considerato una serie di opzioni:

* Epoca Unix, cioè un unico numero crescente.

* Formato di testo conciso "YYYYMMDDTHHMMSSNNNNNNNNN".

* Uso di un fuso orario locale rispetto al fuso orario UTC.


### Argomento

Per l'uso tipico, diamo più valore alla facilità di lettura/scrittura da parte degli esseri umani che alla pura velocità/dimensione.

Per l'uso tipico, vogliamo un formato che funzioni bene nei sistemi macchina e funzioni bene anche manualmente, come scrivere dati di esempio, leggere l'output JSON, fare grep di un file di log ecc.

Per l'uso atipico, come il calcolo ad alte prestazioni, ci aspettiamo di voler ottimizzare qualsiasi formato di testo scegliamo convertendo il testo in un formato più veloce, come il tipo di oggetto data integrato di un linguaggio di programmazione. Quindi il formato di testo non ha molta importanza per l'HPC.


### Implicazioni

I nostri vari sistemi di testo e sistemi temporali convergeranno su questo formato.


## Correlato


### Decisioni correlate

Potremmo volere anche un modo rapido/facile per tracciare le differenze di tempo, dette anche durate. Sono facili con i timestamp dell'epoca Unix.


### Requisiti correlati

Potremmo voler modificare la nostra decisione, per esempio se abbiamo un requisito correlato per un tipo specifico di marcatura dei messaggi di log, come per Splunk, Sumo, ELK ecc.


### Artefatti correlati

Formattatori e parser per linguaggio:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Esempi di Rosetta Code:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Esempi di SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Principi correlati

Facilmente reversibile. Possiamo passare abbastanza facilmente a un formato diverso, come l'epoca Unix.

Rimandare l'ottimizzazione prematura. Per l'uso tipico non ci importa molto di una manciata di caratteri in più, come un formato che usa trattini e due punti.


## Note

Aggiungi qui le note.
