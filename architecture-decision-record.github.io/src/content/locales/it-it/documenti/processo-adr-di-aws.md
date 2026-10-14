# Processo AWS per i registri delle decisioni architetturali

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Un registro delle decisioni architetturali (architectural decision record, ADR) è un documento che descrive le scelte che un team compie su un aspetto importante dell'architettura software che intende costruire. Ogni ADR descrive la decisione architetturale, il suo contesto e le sue conseguenze. Gli ADR hanno uno stato e quindi seguono un ciclo di vita. Per esempi di ADR, consulta l'appendice.

Il processo ADR produce una raccolta di registri delle decisioni architetturali. Quella raccolta costituisce il registro delle decisioni. Il registro delle decisioni fornisce informazioni dettagliate di implementazione e di progettazione, oltre al contesto del progetto. I membri del progetto scorrono il titolo di ogni ADR per avere una panoramica del contesto del progetto. Poi leggono gli ADR per comprendere a fondo le scelte di implementazione e progettazione del progetto.

Quando il team accetta un ADR, questo diventa immutabile. Se nuove intuizioni richiedono una decisione diversa, il team propone un nuovo ADR. Quando il team accetta il nuovo ADR, questo sostituisce l'ADR precedente.

## Ambito del processo ADR

I membri del progetto dovrebbero scrivere un ADR per ogni decisione architetturalmente significativa che influisce sul progetto software o sul prodotto, tra cui (Richards e Ford 2020):

* Struttura (per esempio pattern come i microservizi)

* Requisiti non funzionali (sicurezza, alta disponibilità, tolleranza ai guasti)

* Dipendenze (accoppiamento dei componenti)

* Interfacce (API e contratti pubblicati)

* Tecniche di costruzione (librerie, framework, strumenti, processi)

* I requisiti funzionali e non funzionali sono gli input più comuni del processo ADR.


## Contenuto di un ADR

Quando il team individua la necessità di un ADR, i membri del team iniziano a scrivere l'ADR a partire da un modello valido per l'intero progetto. (Per esempi di modelli, consulta l'organizzazione ADR su GitHub.) Il modello semplifica la scrittura dell'ADR e garantisce che l'ADR contenga tutte le informazioni pertinenti. Come minimo, ogni ADR dovrebbe definire il contesto della decisione, la decisione stessa e le conseguenze della decisione per il progetto e i suoi prodotti. (Per esempi di queste sezioni, consulta l'appendice.) Uno degli aspetti più potenti della struttura dell'ADR è l'attenzione al motivo della decisione anziché a come il team l'ha implementata. Quando comprendi perché il team ha preso la decisione, per gli altri membri del team è più facile accettarla e si evita che altri architetti che non hanno partecipato al processo decisionale la revochino in seguito.


## Il processo di adozione degli ADR

Anche se qualsiasi membro del team può scrivere un ADR, il team dovrebbe stabilire una definizione di proprietà per gli ADR. Ogni autore, che è il proprietario dell'ADR, dovrebbe mantenere e comunicare attivamente il contenuto dell'ADR. Per chiarire questa proprietà, questa guida chiama gli autori degli ADR proprietari dell'ADR nelle sezioni successive. Altri membri del team possono contribuire all'ADR in qualsiasi momento. Se il contenuto dell'ADR cambia prima che il team accetti l'ADR, il proprietario deve approvare tali modifiche.

Dopo che il team ha individuato la decisione architetturale e il suo proprietario, il proprietario dell'ADR presenta all'inizio del processo un ADR con stato **Proposed** (proposto). Un ADR con stato Proposed è pronto per la revisione.

Poi il proprietario dell'ADR avvia il processo di revisione per quell'ADR. L'obiettivo del processo di revisione dell'ADR è che il team decida se accettare l'ADR, stabilire che richiede un rifacimento o rifiutare l'ADR. Il team di progetto, incluso il proprietario, rivede l'ADR. La riunione di revisione dovrebbe iniziare con un tempo dedicato alla lettura dell'ADR. In media sono sufficienti 10–15 minuti. Durante questo tempo, ogni membro del team aggiunge commenti e domande per segnalare gli argomenti poco chiari. Al termine della fase di revisione, il proprietario dell'ADR legge ogni commento e ne discute con il team.

Quando il team trova azioni da compiere per migliorare l'ADR, lo stato dell'ADR resta **Proposed**. Il proprietario dell'ADR raccoglie le azioni e collabora con il team per assegnare un responsabile a ciascuna azione. Ogni membro del team può contribuire alle azioni e risolverle. È responsabilità del proprietario dell'ADR riprogrammare il processo di revisione.

Il team può anche decidere di rifiutare l'ADR. In tal caso, il proprietario dell'ADR aggiunge il motivo del rifiuto per evitare future discussioni sullo stesso argomento. Il proprietario cambia lo stato dell'ADR in **Rejected** (rifiutato).

Quando il team approva l'ADR, il proprietario aggiunge un timestamp, una versione e un elenco di parti interessate. Poi il proprietario aggiorna lo stato in **Accepted** (accettato).

L'ADR e il registro delle decisioni che ne deriva rappresentano le decisioni del team e forniscono una cronologia di tutte le decisioni. Quando possibile, il team usa gli ADR come riferimento durante le revisioni del codice e dell'architettura. Oltre a svolgere revisioni del codice, lavoro di progettazione e lavoro di implementazione, i membri del team dovrebbero consultare gli ADR per le decisioni strategiche sul prodotto.

Come buona pratica, tutte le modifiche al software dovrebbero essere sottoposte a revisione tra pari e richiedere almeno un'approvazione. Durante la revisione del codice, un revisore può trovare una modifica che viola uno o più ADR. In questo caso, il revisore chiede all'autore della modifica del codice di correggere il codice e condivide il link all'ADR o agli ADR. Una volta che l'autore corregge il codice, ottiene l'approvazione di un revisore pari e il codice viene unito nella base di codice principale.


## Il processo di revisione dell'ADR

Dopo che il team ha accettato o rifiutato un ADR, dovrebbe trattarlo come un documento immutabile. Per modificare un ADR esistente, il team deve scrivere un nuovo ADR, stabilire il processo di revisione per il nuovo ADR e approvare l'ADR. Quando il team approva il nuovo ADR, il proprietario deve cambiare lo stato del vecchio ADR in **Superseded** (sostituito). 
