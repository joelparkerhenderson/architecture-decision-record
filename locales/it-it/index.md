# Registro delle decisioni architetturali (ADR)

Un registro delle decisioni architetturali (ADR) è un documento che registra una decisione architetturale importante insieme al suo contesto e alle sue conseguenze.

> [!IMPORTANT]
> Esegui la tua due diligence su queste risorse prima di usarle in qualsiasi sistema critico.

Indice:

- [Che cos'è un registro delle decisioni architetturali?](#che-cosè-un-registro-delle-decisioni-architetturali)
- [Come iniziare a usare gli ADR](#come-iniziare-a-usare-gli-adr)
- [Come iniziare a usare gli ADR con strumenti](#come-iniziare-a-usare-gli-adr-con-strumenti)
- [Come iniziare a usare gli ADR con git](#come-iniziare-a-usare-gli-adr-con-git)
- [Skill di Claude Code per gli ADR](#skill-di-claude-code-per-gli-adr)
- [Convenzioni per i nomi dei file](#convenzioni-per-i-nomi-dei-file)
- [Suggerimenti per scrivere buoni ADR](#suggerimenti-per-scrivere-buoni-adr)
- [Modelli di esempio di ADR](#modelli-di-esempio-di-adr)
- [Consigli di lavoro di squadra per gli ADR](#consigli-di-lavoro-di-squadra-per-gli-adr)
- [Domande sul lavoro di squadra per gli ADR](#domande-sul-lavoro-di-squadra-per-gli-adr)
- [Concetti per il passo successivo sugli ADR](#concetti-per-il-passo-successivo-sugli-adr)
- [Diagrammi, viste e punti di vista architetturali](#diagrammi-viste-e-punti-di-vista-architetturali)
- [Funzioni di fitness per le decisioni come codice](#funzioni-di-fitness-per-le-decisioni-come-codice)
- [Guardrail decisionali per le pull request](#guardrail-decisionali-per-le-pull-request)
- [Per ulteriori informazioni](#per-ulteriori-informazioni)

Modelli:

- [Modello di registro delle decisioni di Jeff Tyree e Art Akerman](modelli/modello-di-registro-delle-decisioni-di-jeff-tyree-e-art-akerman/)
- [Modello di registro delle decisioni di Michael Nygard](modelli/modello-di-registro-delle-decisioni-di-michael-nygard/)
- [Modello di registro delle decisioni di EdgeX](modelli/modello-di-registro-delle-decisioni-di-edgex/)
- [Modello di registro delle decisioni di arc42](modelli/modello-di-registro-delle-decisioni-di-arc42/)
- [Modello di registro delle decisioni per il pattern alessandrino](modelli/modello-di-registro-delle-decisioni-per-il-pattern-alessandrino/)
- [Modello di registro delle decisioni per il business case](modelli/modello-di-registro-delle-decisioni-per-il-business-case/)
- [Modello di registro delle decisioni del progetto MADR](modelli/modello-di-registro-delle-decisioni-del-progetto-madr/)
- [Modello di registro delle decisioni con Planguage](modelli/modello-di-registro-delle-decisioni-con-planguage/)
- [Modello di registro delle decisioni di Paulo Merson](https://github.com/pmerson/ADR-template)
- [Modello di registro delle decisioni di Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Modello di registro delle decisioni di Gareth Morgan](modelli/modello-di-registro-delle-decisioni-di-gareth-morgan/)
- [Modello di registro delle decisioni di GIG Cymru NHS Wales](modelli/modello-di-registro-delle-decisioni-di-gig-cymru-nhs-wales/)
- [Modello di registro delle decisioni per decisioni tecniche importanti di Ignacio Larrañaga](modelli/modello-di-registro-delle-decisioni-per-decisioni-tecniche-importanti/)

Esempi:

- [Framework CSS](esempi/framework-css/)
- [Configurazione con variabili d'ambiente](esempi/configurazione-con-variabili-d-ambiente/)
- [Metriche, monitoraggio, avvisi](esempi/metriche-monitoraggio-avvisi/)
- [Microsoft Azure DevOps](esempi/microsoft-azure-devops/)
- [Monorepo o multirepo](esempi/monorepo-o-multirepo/)
- [Linguaggi di programmazione](esempi/linguaggi-di-programmazione/)
- [Archiviazione dei segreti](esempi/archiviazione-dei-segreti/)
- [Formato del timestamp](esempi/formato-del-timestamp/)
- [Molti altri...](esempi/)

## Che cos'è un registro delle decisioni architetturali?

Un **registro delle decisioni architetturali** (ADR) è un documento che registra una decisione architetturale importante presa, insieme al suo contesto e alle sue conseguenze.

Una **decisione architetturale** (AD) è una scelta di progettazione software che risponde a un requisito significativo.

Un **log delle decisioni architetturali** (ADL) è la raccolta di tutti gli ADR creati e mantenuti per un particolare progetto (o organizzazione).

Un **requisito architetturalmente significativo** (ASR) è un requisito che ha un effetto misurabile sull'architettura di un sistema software.

Tutto questo ricade nell'argomento della **gestione della conoscenza architetturale** (AKM).

L'obiettivo di questo documento è fornire una rapida panoramica degli ADR, di come scriverli e di dove trovare maggiori informazioni.

Abbreviazioni:

  * **AD**: decisione architetturale

  * **ADL**: log delle decisioni architetturali

  * **ADR**: registro delle decisioni architetturali

  * **AKM**: gestione della conoscenza architetturale

  * **ASR**: requisito architetturalmente significativo

## Come iniziare a usare gli ADR

Per iniziare con gli ADR, parla con i tuoi compagni di squadra delle seguenti aree.

Individuazione delle decisioni:

  * Quanto è urgente e quanto è importante la AD?

  * La decisione va presa ora o può aspettare finché non si sa di più?

  * L'esperienza personale e collettiva, così come i metodi e le pratiche di progettazione riconosciuti, possono aiutare a individuare le decisioni.

  * Idealmente, mantieni un backlog delle decisioni che integri il backlog del prodotto.

Presa delle decisioni:

  * Esistono diverse tecniche per la presa di decisioni, comprese tecniche generali e tecniche specifiche dell'architettura software. Un esempio è il dialogue mapping.

  * La presa di decisioni di gruppo è un argomento di ricerca attivo.

Applicazione e attuazione delle decisioni:

  * Poiché le AD sono usate nella progettazione del software, devono essere comunicate e accettate dalle parti interessate che finanziano, sviluppano e gestiscono il sistema.

  * Gli stili di codifica attenti all'architettura e le revisioni del codice incentrate su questioni e decisioni architetturali sono due pratiche correlate.

  * Le AD dovrebbero anche essere (ri)considerate quando si modernizza un sistema software durante l'evoluzione del software.

Condivisione delle decisioni (facoltativa):

  * Molte AD si ripetono tra i progetti.

  * Pertanto, l'esperienza delle decisioni passate, buone e cattive, può essere una risorsa riutilizzabile di valore quando si usa una strategia esplicita di gestione della conoscenza.

Documentazione delle decisioni:

  * Esistono molti modelli e strumenti per registrare le decisioni.

  * Consulta la comunità agile, per esempio gli ADR di M. Nygard.

  * Consulta i processi tradizionali di ingegneria del software e di progettazione architetturale, per esempio IBM UMF e il layout a tabella proposto da Tyree e Akerman di CapitalOne.

Per saperne di più:

  * I passi precedenti sono tratti dalla voce di Wikipedia [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Come iniziare a usare gli ADR con strumenti

- [MySpec](https://myspec.dev) — Piattaforma automatizzata di specifiche e decisioni architetturali che struttura la costituzione del progetto, l'architettura tecnica e gli ADR in Markdown pulito servito tramite MCP.

Puoi scegliere come iniziare a usare gli ADR con gli strumenti.

Per esempio:

  * Se ti piacciono Google Drive e la modifica online, puoi creare un documento Google o un foglio Google.

  * Se ti piace il controllo di versione del codice sorgente come git, puoi creare un file per ogni ADR.

  * Se ti piacciono gli strumenti di pianificazione dei progetti come Atlassian Jira, puoi usare il loro tracker di pianificazione.

  * Se ti piacciono i wiki come MediaWiki, puoi creare un wiki degli ADR.

## Come iniziare a usare gli ADR con git

Se ti piace il controllo di versione git, ecco come iniziamo con gli ADR usando git in un tipico progetto software con codice sorgente.

Crea una directory per i tuoi file ADR:

```sh
$ mkdir adr
```

Per ogni ADR crea un file di testo, come `database.txt`:

```sh
$ vi database.txt
```

Scrivi nell'ADR ciò che vuoi. Per idee, vedi i modelli in questo repository.

Fai il commit degli ADR nel tuo repository git.

## Skill di Claude Code per gli ADR

Questo repository include due skill di [Claude Code](https://claude.com/claude-code) in [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), così che un agente di programmazione con IA possa scrivere e mantenere gli ADR come raccomanda questo progetto:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — di uso generale, per chiunque scriva un ADR in qualsiasi progetto. Aiuta a decidere se una decisione richiede un ADR, crea una directory `adr/` o `decisions/`, assegna il nome al file, sceglie un modello tra gli undici scheletri inclusi e scrive solide sezioni di contesto, decisione e conseguenze.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — specifica per chi mantiene questo repository. Documenta la struttura del repository, la convenzione di rispecchiare README e locales e i passaggi esatti per aggiungere un nuovo modello, esempio o link a uno strumento.

Per usare una skill, copia la sua cartella in `.claude/skills/` nella radice del repository su cui lavori (o in `~/.claude/skills/` per averla in ogni progetto), poi chiedi a Claude Code di scrivere o rivedere un ADR.

## Convenzioni per i nomi dei file

Se scegli di scrivere gli ADR come file di testo semplice, può essere utile stabilire una tua convenzione per i nomi dei file degli ADR.

Preferiamo una convenzione per i nomi dei file con un formato specifico.

Esempi:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

La nostra convenzione per i nomi dei file:

  * Il nome è una frase verbale all'imperativo presente. Questo migliora la leggibilità e corrisponde al nostro formato dei messaggi di commit.

  * Il nome usa lettere minuscole e trattini (come in questo repository). È un equilibrio tra leggibilità e usabilità nei sistemi.

  * L'estensione è markdown. Può essere utile per una formattazione semplice.

## Suggerimenti per scrivere buoni ADR

Caratteristiche di un buon ADR:

* Motivazione: spiega perché si sta eseguendo la AD. Può includere il contesto (vedi sotto), pro e contro di diverse opzioni possibili, confronti di funzionalità, discussioni su costi e benefici e così via.

* Specifico: ogni ADR dovrebbe riguardare una AD, non più AD.

* Con timestamp: indica quando è stata scritta ogni voce dell'ADR. Questo è particolarmente importante per gli aspetti che possono cambiare nel tempo, come costi, tempistiche, espansione e così via.

* Immutabile: non modificare le informazioni esistenti in un ADR. Modifica invece l'ADR aggiungendo nuove informazioni, oppure sostituisci l'ADR creando un nuovo ADR.

Caratteristiche di una buona sezione "Contesto" in un ADR:

* Descrive la situazione dell'organizzazione e le priorità aziendali.

* Include la motivazione e le considerazioni basate sulla composizione sociale e tecnica del team.

* Include compromessi pertinenti, espressi in termini che corrispondono a esigenze e obiettivi.

Caratteristiche di una buona sezione "Conseguenze" in un ADR:

* Descrive ciò che deriva dalla presa della decisione. Possono essere effetti, risultati, consegne, azioni successive e così via.

* Include informazioni sugli ADR successivi. È relativamente comune che un ADR faccia sorgere la necessità di altri ADR. Per esempio, se un ADR compie una scelta ampia e generale, questa può far nascere la necessità di decisioni più piccole.

* Include un processo di revisione a posteriori. È comune che i team rivedano ogni ADR dopo un mese, confrontino le informazioni dell'ADR con ciò che è realmente accaduto e imparino e crescano da questo.

Un nuovo ADR può sostituire un ADR precedente:

* Quando viene presa una AD che sostituisce o invalida un ADR precedente, dovrebbe essere scritto un nuovo ADR

## Modelli di esempio di ADR

Modelli di esempio di ADR che abbiamo raccolto in rete:

- [Modello di ADR di Michael Nygard](modelli/modello-di-registro-delle-decisioni-di-michael-nygard/) (semplice e popolare)

- [Modello di ADR di Jeff Tyree e Art Akerman](modelli/modello-di-registro-delle-decisioni-di-jeff-tyree-e-art-akerman/) (più sofisticato)

- [Modello di ADR per il pattern Alexandrian](modelli/modello-di-registro-delle-decisioni-per-il-pattern-alessandrino/) (semplice, con dettagli sul contesto)

- [Modello di ADR per un business case](modelli/modello-di-registro-delle-decisioni-per-il-business-case/) (più orientato all'MBA, con costi, SWOT e più opinioni)

- [Modello di ADR del progetto Markdown Any Decision Records (MADR)](modelli/modello-di-registro-delle-decisioni-del-progetto-madr/) (sia versione semplice sia elaborata; quest'ultima enfatizza le opzioni e i loro pro e contro)

- [Modello di ADR con Planguage](modelli/modello-di-registro-delle-decisioni-con-planguage/) (più orientato all'assicurazione della qualità)

- [Modello per le decisioni tecniche importanti (ITD) di Ignacio Larrañaga](modelli/modello-di-registro-delle-decisioni-per-decisioni-tecniche-importanti/) (snello e con la decisione al primo posto, ottimizzato per una rapida revisione dirigenziale)

## Consigli di lavoro di squadra per gli ADR

Se stai pensando di usare i registri delle decisioni nel tuo team, ecco alcuni consigli che abbiamo imparato lavorando con più team.

C'è l'opportunità di guidare i membri del team parlando del "perché" anziché imporre il "cosa". Per esempio, i registri delle decisioni sono un modo per i team di pensare in modo più intelligente e comunicare meglio. Se i registri delle decisioni sono solo un requisito burocratico imposto a posteriori, non hanno valore.

Alcuni team preferiscono molto il nome "decisioni" all'abbreviazione "ADR". Quando alcuni team usano "decisions" come nome della directory, si accende una lampadina e i team iniziano a inserire più informazioni nella directory, come decisioni sui fornitori, decisioni di pianificazione, decisioni sui calendari e così via. Puoi usare lo stesso modello per tutti questi tipi di informazioni. Ipotizziamo che le persone imparino più in fretta con la parola ("decisione") che con l'abbreviazione ("ADR"), che l'omissione della parola "registro" dia più motivazione a scrivere il lavoro in corso, e che ad alcuni sviluppatori e ad alcuni manager non piaccia la parola "architettura".

In teoria l'immutabilità è ideale. In pratica, per il nostro team ha funzionato meglio la mutabilità. Inseriamo nuove informazioni in un ADR esistente con un timestamp con la data e una nota che indica che l'informazione è arrivata dopo la decisione. Questo approccio porta a un "documento vivo" che tutti possiamo aggiornare. Gli aggiornamenti tipici derivano dall'acquisizione di informazioni grazie a nuovi membri del team, nuove offerte, risultati effettivi del nostro utilizzo, o dopo modifiche successive di terze parti come funzionalità dei fornitori, piani tariffari e contratti di licenza.

## Domande sul lavoro di squadra per gli ADR

### Chi può scrivere gli ADR?

Considera aree come persone specifiche, ruoli specifici, team specifici, reparti specifici. Considera anche se ci sono persone, ruoli, team o reparti che possono commissionare ADR, cioè possono chiedere a qualcun altro di scrivere un ADR. 

Risposta di esempio: chiunque nella nostra organizzazione abbia letto la pagina README sui registri delle decisioni architetturali può proporre un ADR, cioè iniziare a scrivere e condividerlo con il team.

### Che cosa giustifica l'apertura di un ADR?

Considera aree come il modo in cui lavorano i team dell'organizzazione, la struttura dei sistemi software, il coordinamento tra i team, la manutenibilità a lungo termine, le interfacce esterne e chi vuoi che ne tragga beneficio. 

Risposta di esempio: vogliamo scrivere un ADR quando desideriamo che gli sviluppatori futuri comprendano il "perché" di ciò che facciamo.

### Che cosa non giustifica l'apertura di un ADR?

Considera aree come decisioni che non riguardano l'architettura, decisioni banali perché hanno rischio minimo, sono autonome o limitate a uno sviluppatore, decisioni già pienamente trattate altrove in standard, politiche, documentazione e così via, o decisioni temporanee come soluzioni provvisorie, proof of concept ed esperimenti. 

Risposta di esempio: vogliamo saltare un ADR quando la decisione è limitata per ambito, tempo, rischio e costo, o è già trattata altrove.

### Qual è il ciclo di vita di un ADR?

Considera aree come il processo di scrittura, il processo di ricerca, il processo decisionale, il processo di implementazione e il processo di dismissione. Considera come tieni traccia del ciclo di vita dell'ADR nel tempo, per esempio come sposti un ADR da uno stato al successivo e come lo comunichi alle parti interessate. 

Risposta di esempio: vogliamo che gli ADR abbiano cinque fasi del ciclo di vita: Initiating → Researching → Evaluating → Implementing → Maintaining → Sunsetting.

### Quali sono i criteri per le fasi del ciclo di vita di un ADR?

Considera aree come i criteri di accettazione degli ADR, cioè come sappiamo che un ADR è abbastanza buono per passare da una fase del ciclo di vita alla successiva? Il problema è descritto con chiarezza? Sono state considerate le alternative? I compromessi sono ben compresi e documentati?
Tutto il contesto pertinente è presente? Tutte le parti interessate rilevanti sono coinvolte? Tutto il feedback è stato recepito? 

Risposta di esempio: vogliamo che il team attivo 1) completi la ricerca, 2) completi la valutazione, 3) pubblichi le proposte di ADR alle parti interessate con una richiesta di commenti e un limite di tempo di una settimana, e 4) quando tutti i commenti delle parti interessate sono stati recepiti e affrontati, faccia votare le parti interessate sull'ADR.

### Quali ruoli e responsabilità interagiscono con gli ADR?

Considera ruoli come proponente, ricercatore, valutatore, revisore, approvatore e manutentore. Considera responsabilità come comunicare con le parti interessate, assicurare che le aspettative siano soddisfatte, condividere sul sito web o sull'intranet e rivedere periodicamente il lavoro, specialmente quando ci sono modifiche rilevanti.

Risposta di esempio: vogliamo che ogni ADR abbia sempre un proprietario primario, un proprietario secondario e un team responsabile. Sono responsabili di comunicazione, pubblicazione, manutenzione, revisione periodica almeno annuale e dismissione finale quando necessario.

### In che modo la governance interagisce con gli ADR?

Considera aree come il modo in cui lavora l'organizzazione, esigenze speciali di conformità come aspetti legali o aspetti delle risorse umane e come vuoi gestire consenso rispetto a conflitto rispetto a escalation. Ci sono aree, persone o team che possono avere più influenza di altri, come il potere di approvare, votare o porre il veto in relazione agli ADR?

Risposta di esempio: la governance di un ADR segue questo ordine di priorità: CEO, CTO, CLO, il team che implementa l'ADR, l'esperto più competente nel team sull'ADD. Nessuno ha governance a meno che non sia descritta nell'ADR. 

### Quali principi interagiscono con gli ADR?

Considera aree che riguardano il modo in cui lavora l'organizzazione, come muoversi in fretta o lentamente, consenso decisionale rispetto a conflitto decisionale, preferenza per il rischio rispetto a preferenza per la sicurezza e discussione pubblica rispetto a discussione privata.

Risposta di esempio: usiamo i principi di leadership propensione all'azione (bias for action), dissentire e impegnarsi (disagree-and-commit), il 70% delle informazioni è sufficiente per decisioni facilmente reversibili e facilmente isolabili e lavoro aperto, tranne che per le informazioni riservate descritte negli accordi di riservatezza della nostra organizzazione.

## Concetti per il passo successivo sugli ADR

[Arc42](https://arc42.org/) risponde a due domande in modo pragmatico e può essere adattato alle tue esigenze. Cosa dovresti documentare/comunicare sulla tua architettura? Come dovresti documentarlo/comunicarlo? Arc42 include registri delle decisioni architetturali e indicazioni su obiettivi, vincoli, contesti, qualità, rischi e altro.

[Il modello C4](https://c4model.com/) è un approccio facile da imparare e adatto agli sviluppatori per diagrammare l'architettura software. C4 è un insieme di diagrammi gerarchici per contesto, container, componenti e codice, più diagrammi di supporto per il panorama dei sistemi, la dinamica e il deployment.

## Diagrammi, viste e punti di vista architetturali

Un diagramma architetturale si chiama "vista architetturale".

Una "vista architetturale" è un'istanza di un "punto di vista architetturale".

Un "punto di vista architetturale" ha in mente un pubblico specifico con preoccupazioni specifiche.

Esempi di punti di vista, viste e diagrammi architetturali:

- Capacità di business

- Processi di business di alto livello

- [Flussi di valore](https://en.wikipedia.org/wiki/Value_stream)

- Funzioni software associate ai componenti applicativi

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Diagramma di contesto (TO-BE / AS-IS)

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Diagramma dei container (TO-BE / AS-IS)

- [Diagramma entità-relazione](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) per associare le entità di dati ai componenti applicativi

- [Diagrammi di sequenza](https://en.wikipedia.org/wiki/Sequence_diagram) per descrivere i flussi funzionali all'interno dei sistemi e per le integrazioni

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagrammi per descrivere i flussi di dati tra i componenti applicativi

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagrammi per descrivere i processi di business / gli scenari utente

- [Identity and Access Management](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) diagrammi

- [Controllo degli accessi basato sui ruoli](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) diagrammi con i ruoli per componente applicativo

- [Controllo degli accessi basato sugli attributi](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) diagrammi con gli attributi per componente applicativo

- Diagrammi sulla privacy

Diagrammi correlati:

- Un diagramma dei casi d'uso mostra i casi d'uso a dirigenti/clienti, e precede i requisiti, che precedono l'architettura software.

- Un diagramma di deployment mostra l'hardware/i computer fisici su cui sono distribuiti i componenti software.
- Un diagramma di flusso dei dati mostra come i dati si muovono nel sistema e vengono trasformati.
- Un diagramma di sequenza serve a mostrare come funzionano protocolli come HTTP su un asse temporale.

- Un diagramma di attività descrive il flusso di lavoro delle attività svolte da un sistema software, come un'IA di un NPC.

## Funzioni di fitness per le decisioni come codice

Una funzione di fitness è un controllo oggettivo e automatizzato, scritto come codice di programmazione, che verifica che una decisione sia rispettata.

- Le funzioni di fitness rendono le decisioni verificabili e garantibili.

- Le funzioni di fitness per le decisioni possono aiutare molto la garanzia della qualità, i processi normativi e gli obiettivi di governance.

### Come si collegano funzioni di fitness e decisioni

Un registro delle decisioni documenta una decisione; una funzione di fitness la fa rispettare.

- Decisione di esempio: usare l'event sourcing per i requisiti di audit.

- Funzione di fitness di esempio: usare un server di integrazione continua per verificare che ogni cambiamento di stato debba generare un evento.

### Perché le funzioni di fitness aiutano le decisioni

Misurazione oggettiva: una funzione di fitness passa o fallisce, quindi il lavoro è visibile e chiaro.

Uso continuo: una funzione di fitness è una regola viva e viene eseguita a ogni commit e a ogni build.

Fiducia nel refactoring: una funzione di fitness rileva automaticamente gli errori rispetto alle regole di decisione.

Governance scalabile: una funzione di fitness fa rispettare gli standard senza creare colli di bottiglia.

### Le funzioni di fitness possono usare l'IA?

Una funzione di fitness può usare un LLM di IA per le decisioni ponendo domande
sul nostro lavoro, come piani, codice, schemi, API e così via:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Test unitari dell'architettura

[ArchUnit](https://www.archunit.org/): verifica le regole architetturali del codice Java con un comune framework di test unitari Java.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): verifica le regole architetturali del codice TypeScript e del codice JavaScript con Jest, Vitest, Jasmine e altri.

## Guardrail decisionali per le pull request

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
fa emergere automaticamente i registri delle decisioni giusti al momento giusto, cioè quando uno
sviluppatore sta modificando il codice coperto da quelle decisioni. Invece di sperare che gli sviluppatori
leggano una cartella di documenti prima del merge, il contesto rilevante appare direttamente nella pull request.

Funziona per qualsiasi tipo di registro delle decisioni: decisioni architetturali, sui dati, di conformità, cliniche e mediche, di sicurezza e altro.

Funziona con qualsiasi sistema CI (GitLab, Jenkins, CircleCI) e come hook di pre-commit.
Open source. Licenza MIT.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) è una GitHub
Action che fa fallire una pull request quando i percorsi di codice monitorati cambiano senza che un
registro delle decisioni architetturali sia aggiunto o aggiornato. Le deroghe sono esplicite: una riga
`ADR-Exempt:` con una motivazione supera il controllo e viene scritta nel riepilogo del job. Indipendente dal modello, senza dipendenze. Open source. Licenza MIT.

## Per ulteriori informazioni

Introduzione:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Modelli:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Approfondimenti:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - lezione mensile gratuita di architettura software

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Strumenti:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Indicazioni specifiche di aziende:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Esempi:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Video:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcast:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Libri:

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

Vedi anche:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Un formato YAML/JSON neutrale rispetto ai fornitori e leggibile dalle macchine per rappresentare le decisioni con ragionamento esplicito, ipotesi, stato cognitivo e compromessi. Integra gli ADR aggiungendo alla documentazione delle decisioni un ragionamento strutturato e verificabile.
