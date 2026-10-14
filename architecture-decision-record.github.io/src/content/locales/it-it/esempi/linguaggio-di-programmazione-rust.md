# Registro delle decisioni architetturali: linguaggio di programmazione Rust

Numero della decisione: AR-001

Titolo della decisione: adozione del linguaggio di programmazione Rust

Data: 1 dicembre 2021

Stato: Accettato

### Enunciato del problema

Mentre continuiamo a sviluppare applicazioni software, abbiamo osservato che è sempre più difficile mitigare le potenziali vulnerabilità di sicurezza e prevenire errori di runtime. Con i linguaggi di programmazione esistenti, come C e C++, continuiamo a incontrare problemi come buffer overflow, memory leak e comportamento indefinito che portano ad arresti anomali delle applicazioni. Abbiamo bisogno di un linguaggio di programmazione che fornisca garanzie di sicurezza della memoria e sia abbastanza efficiente da supportare applicazioni critiche per le prestazioni.

### Considerazioni

Diversi linguaggi di programmazione sono progettati per affrontare i problemi esistenti. Tra questi, il linguaggio di programmazione Rust ha ottenuto una notevole attenzione dalla comunità degli sviluppatori grazie alle sue caratteristiche di progettazione uniche. Le considerazioni includono;

1. Sicurezza della memoria e sicurezza

2. Prestazioni ed efficienza

3. Supporto e adozione da parte della comunità

4. Curva di apprendimento

5. Strumenti ed ecosistema

6. Compatibilità con i sistemi software esistenti.

### Vincoli

Adottare un nuovo linguaggio di programmazione richiede di riqualificare gli sviluppatori, il che richiede tempo e risorse. Integrare il linguaggio nel flusso di lavoro di sviluppo esistente può essere una sfida. Dobbiamo garantire la compatibilità con i sistemi esistenti ed evitare modifiche che interrompano il funzionamento per mantenere la continuità.

### Implementazione

1. Il nostro team di sviluppo seguirà una formazione per imparare e familiarizzare con il linguaggio di programmazione Rust.

2. Creeremo un nuovo progetto usando Rust in via sperimentale per valutarne la compatibilità e l'idoneità ai nostri scopi di sviluppo.

3. Migreremo gradualmente i sistemi esistenti scritti in C e C++ a Rust.

4. Collaboreremo con la comunità Rust per esplorare gli strumenti e le librerie disponibili che possono migliorare il nostro flusso di lavoro di sviluppo.

5. Monitoreremo le prestazioni di Rust e le confronteremo regolarmente con le prestazioni dei linguaggi di programmazione esistenti.

6. Adotteremo un approccio a lungo termine che bilanci i costi di formazione e integrazione con i potenziali benefici dell'uso di Rust.

### Motivazione

Abbiamo adottato Rust per le sue caratteristiche uniche progettate per fornire garanzie di sicurezza della memoria e di sicurezza mantenendo prestazioni ed efficienza. Il solido sistema di tipi di Rust, il borrow checker e i concetti di sicurezza della memoria lo rendono molto adatto allo sviluppo di applicazioni critiche per le prestazioni e per la sicurezza. Inoltre, Rust ha una comunità significativa di sviluppatori, che ci permette di accedere a un'ampia gamma di strumenti, librerie ed ecosistema che supportano il nostro flusso di lavoro di sviluppo. Sebbene Rust abbia una curva di apprendimento, crediamo che i vantaggi dell'adozione di Rust superino i costi e offrano un'eccellente opportunità di crescita e innovazione continue.

### Conseguenze

1. L'adozione di Rust richiederà un investimento significativo di tempo e risorse per formare gli sviluppatori e integrare il linguaggio nel flusso di lavoro di sviluppo esistente.

2. L'adozione di Rust può causare un certo grado di problemi di compatibilità con i sistemi esistenti, richiedendo refactoring e modifiche.

3. L'adozione di Rust può aumentare il numero di sviluppatori che possono contribuire al nostro progetto attirando sviluppatori Rust che vogliono lavorare su progetti entusiasmanti.

4. L'adozione potrebbe portare a prestazioni, efficienza e sicurezza migliorate rispetto ai linguaggi esistenti.

5. Infine, l'adozione di Rust comporta il potenziale vantaggio di ridurre le vulnerabilità di sicurezza nelle nostre applicazioni.
   
<h6>Attribuzione: questa pagina è stata generata da ChatGPT e poi modificata per chiarezza e formato.</h6>
