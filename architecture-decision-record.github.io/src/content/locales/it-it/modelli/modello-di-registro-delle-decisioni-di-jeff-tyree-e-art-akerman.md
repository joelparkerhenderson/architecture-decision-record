# Modello di registro delle decisioni di Jeff Tyree e Art Akerman

Questo è il modello per descrivere le decisioni architetturali tratto da ["Architecture Decisions: Demystifying Architecture", Jeff Tyree e Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Questione (Issue)**: Descrivi il problema di progettazione architetturale affrontato, in modo che non resti dubbio sul perché lo affronti ora. Secondo un approccio minimalista, affronta e documenta solo le questioni che richiedono attenzione in determinati punti del ciclo di vita.

* **Decisione (Decision)**: Indica chiaramente la direzione architetturale, cioè la posizione scelta.

* **Stato (Status)**: Lo stato della decisione, per esempio pending, decided, approved.

* **Gruppo (Group)**: Puoi usare semplici raggruppamenti, come integrazione, presentazione, dati ecc., per aiutare a organizzare un insieme di decisioni. Puoi anche usare un'ontologia architetturale più raffinata, come quella di John Kyaruzi e Jan van Katwijk, con categorie più astratte come eventi, calendari e luoghi. Con questa ontologia, per esempio, raggrupperesti sotto gli eventi le decisioni che affrontano situazioni in cui il sistema ha bisogno di informazioni.

* **Ipotesi (Assumptions)**: Descrivi chiaramente le ipotesi di fondo nell'ambiente in cui viene presa la decisione: costo, tempistica, tecnologia e così via. Tieni presente che i vincoli ambientali (come standard tecnologici accettati, architettura aziendale, pattern comunemente usati) possono limitare le alternative considerate.

* **Vincoli (Constraints)**: Registra eventuali vincoli aggiuntivi che l'alternativa scelta (la decisione) può imporre all'ambiente.

* **Posizioni (Positions)**: Elenca le posizioni considerate (opzioni fattibili o alternative). Questo richiede spesso una lunga spiegazione e a volte anche modelli e diagrammi. Questo non è necessariamente un elenco esaustivo. Tuttavia, non vuoi sentire la domanda "Hai pensato a ...?" alla revisione finale. Ciò porta a perdita di fiducia e a dubbi su altre decisioni architetturali. Questa sezione aiuta anche a confermare che hai ascoltato le opinioni altrui. Rendere esplicite le altre opinioni aiuta a portare i loro sostenitori dalla tua parte.

* **Argomento (Argument)**: Delinea perché hai scelto una posizione, con argomenti come costo di implementazione, costo totale di proprietà, tempo di arrivo sul mercato e disponibilità delle risorse di sviluppo necessarie. Questo è probabilmente importante quanto la decisione stessa.

* **Implicazioni (Implications)**: Una decisione ha molte implicazioni, come mostra il metamodello REMAP. Per esempio, una decisione può creare la necessità di prendere altre decisioni, creare nuovi requisiti o modificare quelli esistenti, imporre vincoli aggiuntivi all'ambiente, richiedere di rinegoziare con il cliente l'ambito o la tempistica o richiedere formazione aggiuntiva del personale. Comprendere e dichiarare con chiarezza le implicazioni di una decisione può essere molto efficace per ottenere consenso e creare una tabella di marcia per l'esecuzione dell'architettura.

* **Decisioni correlate**: È chiaro che molte decisioni sono correlate; puoi elencarle qui. In pratica, però, riteniamo più utile una matrice di tracciabilità, un albero decisionale o un metamodello. I metamodelli sono utili per mostrare relazioni complesse nei diagrammi (per esempio i modelli Rose).

* **Requisiti correlati**: Le decisioni dovrebbero essere guidate dal business. Per dimostrare responsabilità, collega esplicitamente le decisioni a obiettivi o requisiti. Puoi elencare qui questi requisiti correlati, ma riteniamo più comodo fare riferimento a una matrice di tracciabilità. Valuti il grado in cui ciascuna decisione architetturale contribuisce a soddisfare ciascun requisito, e poi quanto bene i requisiti sono soddisfatti nel complesso di tutte le decisioni. Se una decisione non contribuisce a soddisfare un requisito, non prendere quella decisione.

* **Artefatti correlati**: Elenca i documenti architetturali, di progettazione o di ambito pertinenti che questa decisione influenza.

* **Principi correlati**: Se l'azienda ha un insieme concordato di principi, assicurati che la decisione sia coerente con uno o più di essi. Questo aiuta a garantire l'allineamento tra domini o sistemi.

* **Note**: Poiché i processi decisionali possono durare settimane, riteniamo utile registrare le note e le questioni che il team discute durante la condivisione preliminare.

