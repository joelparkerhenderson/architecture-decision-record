# Registro delle decisioni architetturali: scelta di una tecnologia di database

## Stato

Accettato

## Contesto

Stiamo progettando una nuova applicazione che richiede di archiviare e recuperare dati in modo scalabile e performante. Abbiamo individuato tre tipi di tecnologie di database comunemente usate: database relazionali, database documentali e database di eventi.

I database relazionali archiviano i dati in tabelle con schemi fissi e impongono rigidi vincoli di integrità dei dati. Sono adatti ad applicazioni che richiedono relazioni complesse tra i dati e transazioni. Esempi sono MySQL, PostgreSQL e Oracle.

I database documentali archiviano i dati in documenti simili a JSON e sono privi di schema. Sono adatti ad applicazioni che richiedono modelli di dati flessibili e scalabilità orizzontale. Esempi sono MongoDB, Couchbase e Amazon DynamoDB.

I database di eventi archiviano i dati come una serie di eventi, catturando ogni modifica ai dati. Sono adatti ad applicazioni che richiedono audit, event sourcing e elaborazione complessa dei dati. Esempi sono Apache Kafka, Apache Pulsar e AWS Kinesis.
Decisione

Dopo aver valutato attentamente i requisiti e i vincoli della nostra applicazione, abbiamo deciso di usare un database documentale.

## Motivazione

Abbiamo scelto un database documentale perché:

1. La nostra applicazione richiede un modello di dati flessibile che possa evolvere nel tempo. I database documentali ci permettono di archiviare i dati in un formato privo di schema, il che significa che possiamo aggiungere nuovi campi o cambiare la struttura dei documenti esistenti senza modificare lo schema del database.

2. La nostra applicazione deve scalare orizzontalmente per gestire grandi volumi di dati e di traffico. I database documentali offrono supporto integrato per sharding e replica, che ci permette di distribuire i dati su più server e gestire un'elevata velocità di lettura e scrittura.

3. La nostra applicazione richiede un recupero dei dati rapido ed efficiente. I database documentali offrono potenti capacità di indicizzazione e interrogazione che ci permettono di recuperare i dati in modo rapido ed efficiente.

4. La nostra applicazione non richiede transazioni o relazioni complesse tra i dati. Mentre i database relazionali eccellono nell'imporre vincoli di integrità dei dati e nella gestione di transazioni complesse, la nostra applicazione non ha tali requisiti. I database documentali possono fornire garanzie sufficienti di coerenza e durabilità per il nostro caso d'uso.

## Conseguenze

Scegliendo un database documentale, dovremo investire nell'apprendere e comprendere la specifica tecnologia che sceglieremo di usare. Inoltre, dovremo assicurarci che il modello di dati della nostra applicazione si adatti bene al modello di dati del database documentale per massimizzare prestazioni e scalabilità.

Tuttavia, crediamo che i vantaggi dell'uso di un database documentale superino i costi e che sia la soluzione più adatta ai requisiti e ai vincoli della nostra applicazione.
