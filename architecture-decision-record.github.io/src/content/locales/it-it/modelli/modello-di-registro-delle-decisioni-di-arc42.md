# Modello di registro delle decisioni di arc42

<https://arc42.org/overview>

## 1. Introduzione e obiettivi

Requisiti, breve descrizione dei fattori determinanti, estratto (o riepilogo) dei requisiti. I tre (al massimo cinque) principali obiettivi di qualità per l'architettura che hanno la priorità più alta per le parti interessate principali. Una panoramica delle parti interessate importanti con le loro aspettative sull'architettura.

## 1.1 Panoramica dei requisiti

### Contenuto

Breve descrizione dei requisiti funzionali, dei fattori determinanti, estratto (o
riepilogo) dei requisiti. Link ai documenti dei requisiti (che si spera esistano)
con informazioni su dove trovarli. 

### Motivazione

Dal punto di vista degli utenti finali, un sistema viene costruito o modificato per
migliorare il supporto alle attività aziendali o per migliorare la qualità. 

### Formato

Breve descrizione testuale, magari in forma tabellare di casi d'uso. Se
esistono documenti dei requisiti, questa panoramica dovrebbe fare riferimento a tali documenti.

Mantieni questo estratto il più breve possibile. Bilancia la leggibilità di questo documento con
la possibile ridondanza con i documenti dei requisiti. 

## 1.2 Obiettivi di qualità

### Contenuto

I tre (al massimo cinque) principali obiettivi di qualità per l'architettura il cui
soddisfacimento è più cruciale per le parti interessate principali. Intendiamo davvero obiettivi di qualità per l'architettura. Non confonderli
con gli obiettivi del progetto. Non sono necessariamente identici. Lo standard ISO 25010
offre un'ottima panoramica dei potenziali argomenti di interesse.

### Motivazione

Dovresti conoscere gli obiettivi di qualità delle parti interessate più importanti, perché
influenzano le decisioni architetturali fondamentali. Sii molto
concreto su queste qualità ed evita le parole di moda. Se, da architetto, non sai come verrà valutata la qualità del tuo lavoro …

### Formato

Una tabella con i principali obiettivi di qualità e scenari concreti, in ordine di priorità.

## 1.3 Parti interessate

### Contenuto

Panoramica esplicita delle parti interessate del sistema, cioè di tutte le persone, i ruoli o le organizzazioni che

- devono conoscere l'architettura

- devono essere convinte dell'architettura

- devono lavorare con l'architettura o con il codice

- hanno bisogno della documentazione dell'architettura per il proprio lavoro

- devono prendere decisioni sul sistema o sul suo sviluppo

### Motivazione

Dovresti conoscere tutte le parti coinvolte nello sviluppo del sistema o influenzate da esso.
Altrimenti, potresti avere spiacevoli sorprese più avanti nel processo di sviluppo. Queste parti interessate
determinano l'estensione e il livello di dettaglio del tuo lavoro e dei suoi risultati.

### Formato

Tabella con nomi dei ruoli, nomi delle persone e le loro aspettative sull'architettura e
sulla sua documentazione.

## 2. Vincoli

Qualsiasi cosa che limita il team nelle decisioni di progettazione e implementazione o nelle decisioni sul processo correlato.
A volte valgono per intere organizzazioni e aziende, al di là dei singoli sistemi.

### Contenuto

Tutti i requisiti che vincolano gli architetti software nella loro libertà rispetto alle
decisioni di progettazione, implementazione o di processo di sviluppo. Questi vincoli a volte valgono
per intere organizzazioni e aziende, al di là dei singoli sistemi.

### Motivazione

Gli architetti dovrebbero sapere esattamente dove sono liberi nelle loro decisioni di progettazione e
dove devono rispettare i vincoli. I vincoli devono sempre essere affrontati,
ma possono essere negoziabili.

### Formato

Semplici tabelle di vincoli con spiegazioni. Se necessario, puoi
suddividerli in vincoli tecnici, vincoli organizzativi e politici e
convenzioni (per esempio linee guida di programmazione o di controllo di versione, convenzioni di documentazione o di denominazione)

## 3. Contesto e ambito

Delimita il tuo sistema dai partner di comunicazione (esterni) (sistemi vicini e utenti). Specifica le interfacce
esterne. Mostralo dal punto di vista aziendale/di dominio (sempre) o dal punto di vista tecnico (facoltativo)

### Contenuto

L'ambito del sistema e il contesto, come dice il nome, delimitano il tuo sistema (cioè l'ambito) da tutti i
partner di comunicazione (sistemi vicini e utenti, cioè il contesto del sistema). In questo modo
specificano le interfacce esterne.

Se necessario, distingui il contesto aziendale (input e output specifici del dominio) dal contesto tecnico (canali, protocolli, hardware).

### Motivazione

Le interfacce di dominio e le interfacce tecniche verso i partner di comunicazione sono tra
gli aspetti più critici del tuo sistema. Assicurati di comprenderle appieno.

### Formato

Varie possibilità:

- Diversi diagrammi di contesto

- Elenchi di partner di comunicazione e delle loro interfacce.

## 3.1 Contesto aziendale

### Contenuto

Specifica di tutti i partner di comunicazione (utenti, sistemi IT, …) con spiegazioni di input
e output specifici del dominio o di interfacce. Facoltativamente puoi aggiungere formati specifici del dominio o protocolli di comunicazione.

### Motivazione

Tutte le parti interessate dovrebbero comprendere l'ambiente del sistema e quali dati
vengono scambiati.

### Formato

Qualsiasi tipo di diagramma che mostri il sistema come scatola nera e specifichi le interfacce di dominio
verso i partner di comunicazione.

Oppure (in aggiunta) una tabella. Il titolo della tabella è il nome del tuo sistema, le tre colonne contengono il nome del partner di comunicazione,
l'input e l'output.

## 3.2 Contesto tecnico

### Contenuto

Interfacce tecniche (canali e mezzi di trasmissione) che collegano il sistema al suo ambiente. In aggiunta,
una mappatura dell'input/output specifico del dominio sui canali, cioè una spiegazione di quale input e output usa quale canale.

### Motivazione

Molte parti interessate prendono decisioni architetturali in base alle interfacce tecniche tra il sistema e
il suo contesto. In particolare i progettisti di infrastruttura o hardware decidono queste interfacce tecniche.

### Formato

Per esempio un diagramma di deployment UML che descrive i canali verso i sistemi vicini,
insieme a una tabella di mappatura che mostra le relazioni tra canali e input/output.

## 4. Strategia della soluzione

Riepilogo delle decisioni fondamentali e delle strategie di soluzione che plasmano l'architettura. Può includere tecnologia, scomposizione di primo livello,
approcci per raggiungere i principali obiettivi di qualità e decisioni organizzative pertinenti.

### Contenuto

Un breve riepilogo e una spiegazione delle decisioni fondamentali e delle strategie di soluzione che
plasmano l'architettura del sistema. Questo include

- decisioni tecnologiche

- decisioni sulla scomposizione di primo livello del sistema, per esempio l'uso di pattern architetturali o pattern di progettazione

- decisioni su come raggiungere i principali obiettivi di qualità

- decisioni organizzative pertinenti, per esempio la selezione di un processo di sviluppo o la delega di determinati compiti a terze parti.

### Motivazione

Queste decisioni sono le pietre angolari della tua architettura. Sono il fondamento di molte altre decisioni
di dettaglio o regole di implementazione.

### Formato

Mantieni breve la spiegazione di queste decisioni chiave.

Motiva ciò che hai deciso e perché lo hai deciso, in base all'enunciato del problema, agli obiettivi di qualità e ai principali
vincoli. Fai riferimento alle sezioni seguenti per i dettagli (sezione 5 per i dettagli strutturali, sezione 8 per
le questioni trasversali).

Puoi usare un elenco o una tabella di approcci alla soluzione.

## 5. Vista a blocchi costruttivi

Scomposizione statica del sistema, astrazioni del codice sorgente, mostrata come gerarchia di
scatole bianche (contenenti scatole nere), fino a un livello di dettaglio appropriato.

### Contenuto

La vista a blocchi costruttivi mostra la scomposizione statica del sistema in blocchi costruttivi (moduli, componenti, sottosistemi, classi,
interfacce, pacchetti, librerie, framework, livelli, partizioni, tier, funzioni, macro, operazioni,
strutture dati, …) e le loro dipendenze (relazioni, associazioni, …)

Questa vista è obbligatoria per qualsiasi documentazione architetturale. Per analogia con una casa,
è la planimetria.

### Motivazione

Mantieni la panoramica del tuo codice sorgente rendendo comprensibile la struttura
attraverso l'astrazione.

Questo ti permette di comunicare con le parti interessate a livello astratto senza
rivelare i dettagli di implementazione.

### Formato

La vista a blocchi costruttivi è una raccolta gerarchica di scatole nere e scatole bianche
(vedi la figura sotto) e delle loro descrizioni.

## 5.1 Scatola bianca dell'intero sistema

Qui descrivi la scomposizione del sistema complessivo usando il seguente modello di scatola bianca. Contiene

- un diagramma di panoramica

- una motivazione per la scomposizione

- descrizioni a scatola nera dei blocchi costruttivi contenuti. Per questo sono offerte le seguenti alternative:

  - usa una tabella per una panoramica breve e pragmatica di tutti i blocchi costruttivi contenuti e delle loro interfacce

  - usa un elenco di descrizioni a scatola nera dei blocchi costruttivi secondo il modello di scatola nera (vedi sotto). A seconda del tuo strumento, questo elenco potrebbe essere composto da sottocapitoli (file di testo), sottopagine (wiki) o elementi annidati (strumenti di modellazione).

  - (facoltativo:) interfacce importanti che non sono descritte nel modello di scatola nera di un blocco costruttivo, ma che sono molto importanti per comprendere la scatola bianca.

Poiché ci sono tanti modi di specificare le interfacce, non forniamo un modello specifico per esse.

Nel migliore dei casi bastano esempi o semplici firme.

## 5.2 Livello 2

Qui puoi specificare la struttura interna di (alcuni) blocchi costruttivi del livello 1 come scatole bianche.

Devi decidere quali blocchi costruttivi del tuo sistema sono abbastanza importanti da giustificare una descrizione
così dettagliata. Preferisci la rilevanza alla completezza.
Specifica i blocchi costruttivi che sono importanti, sorprendenti, rischiosi, complessi o volatili.
Lascia fuori le parti ordinarie, semplici, noiose o standardizzate del tuo sistema

### 5.2.1 Scatola bianca del blocco costruttivo 1

...descrive la struttura interna del blocco costruttivo 1.

Usa il modello di scatola bianca (vedi sopra).

## 6. Vista a runtime

Comportamento dei blocchi costruttivi come scenari, che coprono importanti casi d'uso o funzionalità, interazioni
alle interfacce esterne critiche, esercizio e amministrazione, e comportamento in caso di errori ed eccezioni.

### Contenuto

La vista a runtime descrive il comportamento concreto e le interazioni dei blocchi costruttivi del sistema sotto forma di scenari delle seguenti aree:

- importanti casi d'uso o funzionalità: come li eseguono i blocchi costruttivi?

- interazioni alle interfacce esterne critiche: come collaborano i blocchi costruttivi con utenti e sistemi vicini?

- esercizio e amministrazione: avvio, partenza, arresto

- scenari di errore ed eccezione

Nota: il criterio principale per scegliere i possibili scenari (sequenze, flussi di lavoro) è la loro rilevanza architetturale. Non è importante descrivere un gran numero di scenari. Dovresti piuttosto documentare una selezione rappresentativa.

### Motivazione

Dovresti capire come (le istanze dei) blocchi costruttivi del tuo sistema svolgono il loro lavoro e comunicano a runtime. Includerai gli scenari nella documentazione soprattutto per comunicare la tua architettura alle parti interessate che sono meno attive o meno esperte nella lettura e comprensione dei modelli statici (vista a blocchi costruttivi, vista di deployment).

### Formato

Esistono molte notazioni per descrivere gli scenari, per esempio


- elenco numerato di passi (in linguaggio naturale)

- diagrammi di attività o diagrammi di flusso

- diagrammi di sequenza

- BPMN o EPC (catene di processi a eventi)

- macchine a stati

- ecc.

## 6.n Scenario di runtime n (1, 2, 3 ecc.)

Inserisci un diagramma di runtime o una descrizione testuale dello scenario.

Inserisci una spiegazione degli aspetti notevoli delle interazioni tra le istanze dei blocchi costruttivi raffigurate in questo diagramma.

## 7. Vista di deployment

Infrastruttura tecnica con ambienti, computer, processori e topologie.
Mappatura dei blocchi costruttivi (software) sugli elementi dell'infrastruttura.

### Contenuto

La vista di deployment descrive:

- l'infrastruttura tecnica usata per eseguire il tuo sistema, con elementi dell'infrastruttura come ubicazioni geografiche, ambienti, computer, processori,
  canali e topologie di rete, nonché altri elementi dell'infrastruttura, e

- la mappatura dei blocchi costruttivi (software) su tali elementi dell'infrastruttura.

Spesso i sistemi vengono eseguiti in ambienti diversi, per esempio ambiente di sviluppo, ambiente di test, ambiente di produzione. In tali casi dovresti
documentare tutti gli ambienti pertinenti.

Documenta la vista di deployment in particolare quando il tuo software viene eseguito come sistema distribuito con più di un computer, processore, server o container o quando progetti e costruisci i tuoi processori e chip hardware.

Dal punto di vista software, è sufficiente catturare gli elementi dell'infrastruttura necessari per mostrare il
deployment dei blocchi costruttivi.
Gli architetti hardware possono andare oltre e descrivere l'infrastruttura a qualsiasi
livello di dettaglio abbiano bisogno di catturare. 

### Motivazione

Il software non funziona senza hardware. Questa infrastruttura sottostante può e influenzerà il tuo sistema e/o alcuni
concetti trasversali. Pertanto devi conoscere l'infrastruttura.

### Formato

Il livello più alto dei diagrammi di deployment è già incluso nella sezione 3.2 come contesto tecnico con la tua
infrastruttura come un'unica scatola nera. In questa sezione ingrandisci quella scatola nera con diagrammi di deployment aggiuntivi.

- UML offre diagrammi di deployment per esprimere quella vista. Usali, magari con diagrammi annidati,
  quando la tua infrastruttura è più complessa.

- Quando le tue parti interessate (hardware) preferiscono un altro tipo di diagramma al diagramma di deployment UML,
  lascia che usino qualsiasi tipo che possa mostrare nodi e canali dell'infrastruttura.

## 7.1 Infrastruttura di livello 1

Descrivi (di solito in una combinazione di diagrammi, tabelle e testo):

- la distribuzione di un sistema su più ubicazioni, ambienti, computer, processori ecc., nonché le connessioni fisiche tra di essi

- importante giustificazione o motivazione di questa struttura di deployment

- caratteristiche di qualità e/o di prestazioni dell'infrastruttura

- mappatura degli artefatti software (blocchi costruttivi) sugli elementi dell'infrastruttura

Per più ambienti o deployment alternativi, copia quella sezione di arc42 per tutti gli ambienti pertinenti. **

## 7.2 Infrastruttura di livello 2

Può includere la struttura interna di (alcuni) elementi dell'infrastruttura del livello 1.

Copia la struttura del livello 1 per ogni elemento selezionato.

## 8. Concetti trasversali

Normative generali e di principio e approcci di soluzione rilevanti per più
parti (→ trasversali) del tuo sistema. I concetti sono spesso correlati a più
blocchi costruttivi. Includi argomenti diversi come modelli di dominio, pattern
e stili architetturali, regole per l'uso di una tecnologia specifica e regole di
implementazione.

### Contenuto

Questa sezione descrive concetti trasversali (pratiche, pattern, normative
o idee di soluzione). Tali concetti sono spesso correlati a più blocchi costruttivi.
Possono riguardare molti argomenti diversi.

### Motivazione

I concetti sono la base dell'integrità concettuale (coerenza, omogeneità) dell'architettura. Pertanto
sono un contributo importante alla qualità interna del tuo sistema.

Questo è il posto che abbiamo creato nel modello per una specifica coerente di tali concetti.

Molti di questi concetti sono correlati o influenzano più blocchi costruttivi.

### Formato

Il formato può variare:

- documenti di concetto con qualsiasi struttura

- implementazioni di esempio, in particolare per concetti tecnici

- estratti di modelli trasversali o scenari che usano le notazioni delle viste architetturali

### Struttura di questa sezione

Scegli solo gli argomenti più necessari per il tuo sistema e assegna a ciascuno un titolo di livello 2 in questa sezione (per esempio 8.1, 8.2 ecc.).

- Non cercare di coprire tutti gli argomenti del diagramma sopra menzionato.

### Contesto

Alcuni argomenti all'interno di un sistema sono spesso correlati a più blocchi costruttivi, elementi
hardware o processi di sviluppo. Può essere più facile comunicare o documentare tali argomenti trasversali in un unico
punto centrale invece di ripeterli nella descrizione dei blocchi costruttivi, degli elementi hardware o dei
processi di sviluppo correlati.

Certi concetti possono essere rilevanti per tutti gli elementi del sistema, altri solo per alcuni.

## 9. Decisioni architetturali

Decisioni architetturali importanti, costose, critiche, di ampia portata o rischiose, inclusi i fondamenti.

### Contenuto

Decisioni architetturali importanti, costose, di ampia portata o rischiose, inclusi i fondamenti.
Per "decisioni" intendiamo la scelta di un'alternativa in base a criteri dati.

Decidi a tua discrezione se documentare le decisioni architetturali in questa sezione centrale o se preferisci
documentarle a livello locale (per esempio all'interno del modello di scatola bianca di un blocco costruttivo). Evita testo ridondante. Fai riferimento alla sezione 4, che contiene già
le decisioni più importanti della tua architettura.

### Motivazione

Le parti interessate del tuo sistema dovrebbero essere in grado di comprendere e risalire
alle tue decisioni.

### Formato

- ADR (registri delle decisioni architetturali) per ogni decisione importante

- elenco o tabella, ordinati per importanza e conseguenze, oppure

- più dettagliato in sezioni separate per ogni decisione

### Contesto (sugli ADR)

I pezzi di documentazione più piccoli sono più facili da leggere, scrivere e mantenere. Riguardo alle decisioni architetturali,
i team di sviluppo spesso conoscono:

- la decisione, perché per esempio è visibile nel codice sorgente, ma

- mancano della motivazione dietro quella decisione (vedi Nygard 2011)

Pertanto dovresti documentare alcune decisioni importanti con la loro motivazione e il loro ragionamento

### La nostra proposta per le decisioni

Mantieni una raccolta di decisioni architetturalmente significative, cioè decisioni che influenzano struttura, caratteristiche di qualità, dipendenze
(in particolare esterne) e interfacce importanti o tecniche di costruzione (grazie a Michael
Nygard per questa proposta).

## 10. Requisiti di qualità

Requisiti di qualità come scenari, con un albero della qualità per fornire una panoramica di alto livello.
I più importanti obiettivi di qualità dovrebbero essere già descritti nella sezione
1.2 (obiettivi di qualità).

### Contenuto

Questa sezione contiene tutti i requisiti di qualità pertinenti.

I più importanti di questi requisiti sono già stati descritti nella sezione
1.2 (obiettivi di qualità), quindi dovresti solo fare riferimento a essi qui. In questa
sezione 10 dovresti includere anche requisiti di qualità meno importanti che non creano rischi elevati se
non vengono raggiunti pienamente (ma che sono utili da avere).

### Motivazione

Poiché i requisiti di qualità influenzano molto le decisioni architetturali, dovresti sapere quale qualità
è davvero importante per le parti interessate, in modo concreto e misurabile.

### Ulteriori informazioni

Vedi il completo modello di qualità Q42 su https://quality.arc42.org.

## 10.1 Panoramica dei requisiti di qualità

### Contenuto

Una panoramica o un riepilogo dei requisiti di qualità.

### Motivazione

Spesso ti trovi di fronte a decine (persino centinaia) di requisiti di qualità dettagliati.
In questa sezione di panoramica dovresti cercare di riassumerli, per esempio descrivendo categorie o argomenti (come suggerito da ISO 25010:2023 o Q42)

Se queste descrizioni riepilogative sono già accurate, sufficientemente specifiche
e misurabili, puoi saltare la sezione 10.2.

### Formato

Usa una semplice tabella con la categoria o l'argomento e una breve descrizione del requisito di qualità su ogni riga.
Oppure usa una mappa mentale per strutturare questi requisiti di qualità.

Nella letteratura è descritta anche l'idea degli alberi degli attributi di qualità, che hanno il termine generale "qualità" come radice e
raffinano il termine "qualità" in una struttura ad albero.
[Bass+21] ha introdotto a questo scopo il termine "Quality
Attribute Utility Tree".

## 10.2 Scenari di qualità

### Contenuto

Gli scenari di qualità concretizzano i requisiti di qualità e permettono di decidere se sono
(nel senso dei criteri di accettazione) soddisfatti. Assicurati che gli scenari siano
specifici e misurabili.

Due tipi di scenari sono particolarmente utili:

- Gli scenari d'uso (chiamati anche scenari applicativi o scenari di caso d'uso) descrivono la reazione a runtime del sistema a un
  determinato stimolo. Questo include anche scenari che descrivono l'efficienza o le
  prestazioni del sistema.
  Esempio: il sistema reagisce a una richiesta di un utente entro un secondo.

- Gli scenari di modifica descrivono l'effetto desiderato di una modifica o estensione del sistema o
  del suo ambiente immediato. Esempio: viene implementata una funzionalità aggiuntiva o cambiano i requisiti
  per un attributo di qualità, e si misura lo sforzo o la durata della modifica.

### Formato

Le informazioni tipiche negli scenari dettagliati includono:

Forma breve (preferita nel modello Q42):

- Contesto/sfondo: che tipo di sistema o componente e qual è l'ambiente o la situazione?

- Origine/stimolo: chi o che cosa avvia o innesca l'azione, la reazione o il comportamento.

- Metrica/criterio di accettazione: la risposta, inclusa la scala o la metrica

La forma lunga degli scenari (preferita dal SEI e da [Bass+21]) è più dettagliata e include le seguenti informazioni:

- ID dello scenario: un identificatore univoco per lo scenario.

- Nome dello scenario: un nome breve e descrittivo per lo scenario.

- Origine: l'entità (utente, sistema o evento) che avvia lo scenario.

- Stimolo: l'evento o la condizione scatenante a cui il sistema deve rispondere.

- Ambiente: il contesto operativo o le condizioni in cui il sistema sperimenta lo stimolo.

- Artefatto: il blocco costruttivo o altro elemento del sistema che è influenzato dallo stimolo.

- Risposta: il risultato o il comportamento che il sistema mostra in risposta allo stimolo.

- Misura della risposta: il criterio o la metrica con cui viene valutata la risposta del sistema.

### Vedi anche

Dal gennaio 2023 arc42 offre un modello di qualità pragmatico che suggerisce di etichettare i requisiti di qualità
con hashtag o etichette come
#flexible, #efficient, #usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Rischi e debito tecnico

Rischi tecnici noti o debito tecnico. Quali potenziali problemi ci sono nel sistema o intorno a esso?
Con che cosa ha difficoltà il team di sviluppo?

### Contenuto

Un elenco prioritizzato dei rischi tecnici o del debito tecnico individuati

### Motivazione

"La gestione del rischio è la gestione dei progetti per adulti" (Tim Lister, Atlantic
Systems Guild.)

Questo dovrebbe essere il tuo motto per una scoperta e una valutazione sistematiche dei rischi e del debito tecnico nell'architettura,
di cui le parti interessate della gestione (per esempio project manager, product owner) avranno bisogno come parte dell'analisi complessiva del rischio e della pianificazione delle misure.

### Formato

Elenco di rischi e/o debito tecnico, magari con misure proposte per
minimizzare, mitigare o evitare i rischi o ridurre il debito tecnico.

