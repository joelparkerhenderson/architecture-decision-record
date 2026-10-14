# Registro delle decisioni architetturali: API con JSON o gRPC

## Stato

Accettato

## Contesto

Stiamo progettando un'API per un nuovo servizio che sarà usato da più client. Abbiamo considerato due opzioni per implementare l'API: JSON su HTTP o gRPC.

JSON su HTTP è un approccio ampiamente usato per costruire API ed è supportato da molti linguaggi di programmazione e framework. Questo approccio è semplice, leggero e facile da capire, il che lo rende una buona scelta per molti progetti. Tuttavia, può essere meno efficiente di altre opzioni, soprattutto quando si tratta di gestire grandi quantità di dati.

gRPC, d'altra parte, è una tecnologia più recente che offre un modo più efficiente di costruire API. Usa la serializzazione binaria per trasferire i dati, che può essere più veloce e più compatta rispetto all'uso di JSON. gRPC supporta anche lo streaming bidirezionale, il che lo rende una buona scelta per le applicazioni in tempo reale.

## Decisione

Dopo aver considerato pro e contro di entrambe le opzioni, abbiamo deciso di usare gRPC per la nostra API. Sebbene JSON su HTTP sia un'opzione più semplice, crediamo che gRPC fornirà una soluzione più efficiente e scalabile per il nostro servizio. Prevediamo anche che la nostra API gestirà una grande quantità di dati e la serializzazione binaria di gRPC sarà più efficiente per questo caso d'uso.

Inoltre, crediamo che il supporto di gRPC allo streaming bidirezionale sarà utile per le applicazioni in tempo reale che potremmo sviluppare in futuro.

## Conseguenze

Scegliendo gRPC, dovremo usare un insieme diverso di strumenti e librerie per costruire la nostra API rispetto all'uso di JSON su HTTP. Ciò può richiedere tempo e impegno aggiuntivi per imparare e implementare queste tecnologie. Inoltre, i client che vogliono usare la nostra API dovranno usare librerie compatibili con gRPC, che potrebbero non essere così ampiamente supportate come le librerie JSON su HTTP.

Tuttavia, crediamo che i vantaggi dell'uso di gRPC superino questi potenziali svantaggi e siamo fiduciosi che questa decisione porterà a un'API più efficiente e scalabile.
