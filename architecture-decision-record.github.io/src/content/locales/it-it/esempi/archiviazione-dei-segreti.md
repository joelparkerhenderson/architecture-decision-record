# Archiviazione dei segreti

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
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Riepilogo


### Questione

Dobbiamo archiviare segreti, come password, chiavi private, token di autenticazione ecc.

Alcuni dei segreti sono orientati all'utente. Per esempio, il nostro sviluppatore vuole poter usare il suo telefono cellulare per cercare la password di un servizio.

Alcuni dei segreti sono orientati al sistema. Per esempio, la nostra pipeline di consegna continua deve poter cercare le credenziali di accesso per il nostro hosting cloud.


### Decisione

Bitwarden per i segreti orientati all'utente.

Vault by HashiCorp per i segreti orientati al sistema.


### Stato

Deciso. Siamo aperti a nuove opzioni man mano che emergono.


## Dettagli


### Ipotesi

Per questo scopo e per la nostra situazione attuale, diamo valore alla comodità orientata all'utente, come app mobili utili.

  * Vogliamo garantire un accesso rapido e semplice in mobilità, per esempio per uno sviluppatore che svolge servizio di reperibilità per l'ingegneria dell'affidabilità.

  * Vogliamo poter condividere alcuni segreti tra persone selezionate, per esempio un team.

Non cerchiamo di risolvere per un singolo fornitore, per esempio archiviare tutti i segreti esclusivamente presso Amazon o Azure o Google.

Non vogliamo approcci ad hoc come "ricordalo" o "scrivilo su un foglietto" o "trova il tuo modo per archiviarlo".

Il nostro modello di sicurezza per questo scopo è soddisfatto dell'uso di fornitori COTS ben considerati, per esempio strumenti SaaS di gestione delle password.


### Vincoli

In questo momento vogliamo qualcosa di semplice, cioè nessuna necessità di scrivere codice, nessuna necessità di installare server, nessuna necessità di assumere un grande impegno, nessuna necessità di standardizzare tutti.


### Posizioni

Abbiamo considerato:

1. Gestori di password già pronti orientati all'utente: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG ecc.

2. Gestori di password COTS orientati al sistema: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Approcci orientati alla condivisione: usare un documento Google condiviso, un canale Slack condiviso, una cartella di rete condivisa ecc.

4. Approcci ad hoc a bassa tecnologia, come ricordare, scrivere un foglietto o contare sul fatto che ogni utente trovi il proprio modo di archiviare.


### Argomento

Bitwarden, LastPass, 1Password e Dashlane sono tutti prodotti commerciali già pronti.

  * Tipi simili di funzionalità per utenti, team, organizzazioni ecc.

  * Capacità desktop per Windows e Mac e capacità mobile per Android e iOS.

  * Estensioni del browser per Chrome e Firefox, per la compilazione automatica dei moduli ecc.

Bitwarden ha due vantaggi rispetto agli altri:

  * Bitwarden è open source, il che significa che la sicurezza può essere esaminata dai colleghi e che l'azienda è anche generalmente apprezzata dagli sviluppatori attenti alla sicurezza.

  * Aneddoti di persone del software descrivono una preferenza significativa per Bitwarden rispetto agli altri.

Un tipico buon articolo: https://jcs.org/2017/11/17/bitwarden

Un tipico sito di voto con confronto affiancato: https://stackshare.io/stackups/bitwarden-vs-dashlane

Rimandiamo KeyPass, pass, GPG ecc. perché c'è ulteriore complessità. Tutti sembrano ottime soluzioni per utenti tecnici. GPG sembra particolarmente buono per utenti tecnici che vogliono capacità orientate ai comandi tra i sistemi.

Rimandiamo KMS perché ha il vincolo di un singolo fornitore.

Scegliamo Vault per le esigenze orientate al sistema, perché le recensioni sono sorprendentemente positive e perché HashiCorp ha un eccellente curriculum in software e supporto di prim'ordine.

Poniamo il veto sugli approcci di condivisione, per esempio tramite documenti condivisi, canali condivisi, cartelle di rete condivise ecc. Questi non forniscono le qualità di sicurezza che vogliamo.

Poniamo il veto sugli approcci ad hoc a bassa tecnologia, perché siamo tutti d'accordo che non è una via a lungo termine.


### Implicazioni

Gli sviluppatori potrebbero dover tenere traccia dei segreti in due posti: Bitwarden per l'accesso orientato all'utente e Vault per l'accesso orientato al sistema.


## Correlato


### Decisioni correlate

La decisione su quale server CI/CD scegliere deve includere la prova della capacità di accedere ai segreti.

Dovremo decidere come gestire i segreti, in termini di politiche, rotazioni, organizzazioni ecc.


### Requisiti correlati

I segreti avranno requisiti correlati per conformità, audit e onboarding/offboarding delle risorse umane.


### Artefatti correlati

Ci aspettiamo di poter esportare alcuni segreti in variabili d'ambiente.


### Principi correlati

Facilmente reversibile.

Facile da eseguire in parallelo, cioè è semplice usare una varietà di gestori di password.

Economico da provare, cioè c'è una prova gratuita e nessun impegno.


## Note

Note di valutazione qui. Le note sono tutte commenti pubblici su vari forum di discussione devops.


### Vault by HashiCorp

Vault è esattamente ciò che vuoi qui. 

Ma non buttare semplicemente Vault in produzione, configuralo prima in un ambiente di test, perché la documentazione di HashiCorp può essere piuttosto carente anche se i loro prodotti sono fantastici.

Curva di apprendimento molto ripida e non è banale da configurare. 

La configurazione iniziale è un po' una seccatura. Ne vale assolutamente la pena e la comunità lo supporterà abbastanza bene da farti cavare d'impaccio.

Documentazione terribile, ma ci sono molte guide online di persone che l'hanno configurato e se ne combini alcune avrai una configurazione funzionante.

La configurazione iniziale ha richiesto di smanettare con i loro helm chart (vault e consul). Tecnicamente puoi usare molti altri backend, ma davvero, davvero non lo raccomando. Il backend/consul può essere minuscolo se non hai molti dati da archiviare.

Familiarizza decisamente con l'uso della CLI, perché la GUI è più una prova di concetto/portale pubblicitario per la loro edizione enterprise.

Il fatto che non puoi semplicemente "riempirlo" è una seccatura. Se per esempio hai 5 campi, devi aggiungere manualmente ogni campo per ogni elemento. Quindi non è che predefinisci i campi per una categoria specifica e compili quei campi per tutti gli elementi di quella categoria, ma è più "generi tutto ogni volta", il che (secondo me) è una seccatura.

Potresti anche guardare goldfish come UI sopra vault. Rende abbastanza piacevole coinvolgere il tuo team. Hanno anche una demo. 1. Configura consul. 2. Configura vault che punta a consul. 3. Configura goldfish che punta a vault. 3. Configura un cron job che esegue consul snapshot per i backup.



### LastPass

LastPass Teams. Lo usiamo, abbiamo modelli personalizzati, ACL e secondo me non manca nulla.

Ho implementato LastPass nella mia organizzazione e gli do un C+/B-. Il problema più grande ultimamente è la mancanza di affidabilità. Negli ultimi 90 giorni ci sono state diverse ore in cui le casseforti sono state forzate in modalità offline. Questo non è l'ideale per la mia organizzazione perché abbiamo letteralmente più di 4.000 password archiviate in più di 20 cartelle condivise. Come puoi immaginare con così tante password, almeno alcune vengono aggiornate o aggiunte ogni giorno. Abbiamo un piano di DR se i problemi durano più di un'ora o due: uno script firma e cifra ogni notte un dump CSV della cassaforte che può essere importato in keepass.

LastPass ha avuto momenti non segnalati di servizio degradato: l'accesso "funziona" ma non recupera alcun sito, funzioni casuali del pannello di amministrazione sono rotte e le chiavi non vengono condivise correttamente per le nuove cartelle condivise di primo livello. Ho un utente speciale "key push"/di backup che è in ogni gruppo. Di solito accedere come quell'utente risolve tutti i problemi di condivisione delle chiavi, ma non quando il servizio è degradato indipendentemente da ciò che dice la pagina di stato...

Per l'integrazione può essere semplice se hai ACL adeguate con un modello di minimo privilegio, per esempio se un utente ha sia permessi di lettura e scrittura sia di sola lettura su un elemento o una cartella, ottiene solo permessi di lettura. Purtroppo le ACL della mia organizzazione non sono le migliori, quindi ho finito per usare l'API di provisioning JSON e ~500 righe di python perché la dipendenza nelle nostre centinaia di ACL non si mappava bene sul modello di minimo privilegio. Alla fine ho recuperato tutte le ACL in cui un utente si trovava e ho fatto una specie di percorso delle dipendenze.

Se la struttura delle tue ACL o dei tuoi gruppi è già costruita con una struttura di minimo privilegio in mente, lo strumento di sincronizzazione AD/LDAP per Windows funziona bene.

Contatta il loro team commerciale e possono organizzare una prova Enterprise più lunga. Assicurati di comprenderne appieno i limiti prima di premere il grilletto. Abbiamo avuto parecchi problemi di crescita ma, a parte interruzioni o degradi lato server, è stato incredibilmente fluido.


### Bitwarden

Bitwarden ha buoni strumenti intorno (WebUI, CLI, mobile, desktop). Può essere self-hosted ed è abbastanza semplice da configurare. Documentazione abbastanza buona e uno strumento raccomandato da PrivacyTools.


### EnvKey

https://www.envkey.com/ è un saas. Davvero facile da implementare, integrare e gestire.

Funzionalità:

  * Proteggi chiavi API e credenziali di accesso.

  * Mantieni la configurazione sincronizzata ovunque.

  * Gestione intelligente e cifrata end-to-end di configurazione e segreti. 

  * Previeni la condivisione non sicura e la dispersione della configurazione. 

  * Integra in pochi minuti.

Capacità:

  * Gestisci configurazione e livelli di accesso per tutte le tue app, ambienti e team in un unico posto.

  * Configura qualsiasi ambiente di sviluppo o server con una sola variabile d'ambiente.

Vantaggi:

  * Ottima pagina di destinazione.

  * Proposta di valore chiara.

  * Web app visivamente eccellente.

  * Dati di esempio superiori, per esempio Algolia, AWS, Datadog, GitHub, Stripe ecc.

  * Ho parlato con il fondatore per 30 minuti dell'azienda, della UI ecc. Dane sembra ben informato, onesto su pro e contro e un partner praticabile.

  * L'azienda è fondamentalmente una tipica azienda Y Combinator con 1 fondatore. Ha raccolto $120K nel 2018-01.

  * Il focus è sul raggiungimento delle funzionalità enterprise, in particolare sul passaggio dall'hosting cloud EnvKey a on-prem o BYOC.

  * Possibile via da seguire: iniziare con EnvKey per semplicità e poi in seguito (o in parallelo) aggiungere Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant è un servizio di gestione dei segreti open source che offre archiviazione e accesso ai segreti facili da usare e sicuri, degli sviluppatori di Lyft.

Autenticazione KMS: Confidant risolve il problema dell'"uovo e gallina" dell'autenticazione usando AWS KMS e IAM per consentire ai ruoli IAM di generare token di autenticazione sicuri che possono essere verificati da Confidant. Confidant gestisce anche i grant KMS per i tuoi ruoli IAM, il che consente ai ruoli IAM di generare token che possono essere usati per l'autenticazione tra servizi o per inviare messaggi cifrati tra servizi.

Cifratura a riposo di segreti versionati: Confidant archivia i segreti in modo append-only in DynamoDB e genera una chiave dati KMS univoca per ogni revisione di ogni segreto, usando la crittografia autenticata simmetrica Fernet.

Un'interfaccia web facile da usare per gestire i segreti: Confidant fornisce un'interfaccia web AngularJS che consente agli utenti finali di gestire facilmente i segreti, le mappature dei segreti ai servizi e la cronologia delle modifiche.


### Devolutions Password Server

https://server.devolutions.net/

Proteggi, gestisci e monitora l'accesso ad account e sessioni privilegiati.

Una cassaforte di password completa e ad alta sicurezza che ti permette di controllare l'accesso ai tuoi account privilegiati, migliorando al contempo la visibilità complessiva della rete per gli amministratori di sistema e fornendo un'esperienza fluida agli utenti finali.

Funzionalità: cassaforte di password centralizzata dell'organizzazione, cassaforte privata specifica dell'utente, gestore di password, iniezione di credenziali,
integrazione con Active Directory, controllo degli accessi basato sui ruoli, autenticazione a due fattori, pronto per l'enterprise, restrizioni IP, capacità di gestione, generatore automatico di password, accesso tramite app mobile, cronologia delle password, report di accesso, avvisi email.

  * supporta la cifratura dei dati

  * supporta più schemi di autenticazione inclusi LDAP, O365 e utenti locali CON supporto MFA da più fonti

  * più repo/casseforti con controlli di accesso granulari per più team

  * UI web moderna

  * casseforti private per credenziali e connessioni per credenziali/connessioni personali

  * app mobili per iOS/Android

  * log di audit per ogni voce, chi/cosa/quando con una domanda facoltativa sul perché vi accedono

  * modelli personalizzabili (anche se supportano nativamente centinaia di tipi di connessione)

  * molte altre funzionalità e un client pesante per Windows/Mac (Remote Desktop Manager) con cui puoi sincronizzarti e che estende molto le opzioni... connessioni con un clic

  * il prezzo non è male - fino a 15 utenti il server delle password costa $500 all'anno


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Funzionalità della versione on-premises: 

  * Controllo totale sui tuoi sistemi di sicurezza end-to-end e sulla tua infrastruttura

  * Distribuisci il software nel tuo data center on-premises o nella tua istanza di un cloud privato virtuale

  * Soddisfa gli obblighi legali e normativi che richiedono che tutti i dati e i sistemi siano on-premises

Funzionalità della versione cloud:

  * Il modello software-as-a-service ti permette di registrarti e iniziare subito

  * Scalabilità elastica man mano che cresci

  * Controlli e ridondanza forniti da Azure con SLA di uptime del 99,9%

Feedback degli utenti:

  * Abbiamo usato quel prodotto in passato. Era così facile da aggirare e le regole funzionano solo per persone intelligenti. Utenti pigri o stupidi possono facilmente rovinarlo in un'area di team. I prezzi sono negoziabili quando parli con loro.

  * Puoi eseguirlo con SQL express e un computer Win 7. 

  * Economico.
