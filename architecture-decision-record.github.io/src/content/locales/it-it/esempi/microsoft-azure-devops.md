# Microsoft Azure DevOps

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
  * [Microsoft Devops CI: un'avventura insoddisfacente](#microsoft-devops-ci-unavventura-insoddisfacente)
  * [Punti salienti della discussione su Hacker News](#punti-salienti-della-discussione-su-hacker-news)
  * [Windows Development MVP](#windows-development-mvp)
  * [Riepilogo di Edward Thomson (Azure PM)](#riepilogo-di-edward-thomson-azure-pm)


## Riepilogo


### Questione

Vogliamo usare il devops per costruire, integrare, distribuire e ospitare i nostri progetti. Stiamo considerando Microsoft Azure DevOps.

  * Vogliamo che l'esperienza dello sviluppatore sia veloce e affidabile, sia per la configurazione del devops, per esempio la configurazione, sia per l'uso continuo, per esempio tempi di build rapidi.
  
  * Vogliamo considerare l'uso di Microsoft Azure nel suo insieme, per ospitare le app del progetto, i database ecc.


### Decisione

Deciso contro Microsoft Azure DevOps.


### Stato

Deciso. Aperti a rivedere se/quando arriveranno nuove informazioni significative.


## Dettagli


### Ipotesi

Tutte le consuete ipotesi devops, come nel libro Accelerate.

  * Build veloci sono un aiuto significativo. Questo accelera i cicli di feedback.

  * Possiamo sostituire o togliere parti di fornitori alternativi, cioè potremmo voler portare i nostri server di build più veloci, usare il sistema di controllo di versione di nostra scelta o coordinarci con un server di integrazione continua self-hosted.
  
  * L'usabilità semplificata è un aiuto significativo per l'esperienza dello sviluppatore e, a sua volta, per aree sottili come coerenza, chiarezza, sicurezza e facilità della curva di apprendimento.

  * Quando qualcosa è rotto o problematico, vogliamo un modo efficace di segnalare il problema. Questo è particolarmente importante per i problemi legati alla sicurezza.


### Vincoli

Nessuno noto. Azure ha un impegno pubblicato a funzionare bene con strumenti esterni.


### Posizioni

Abbiamo considerato l'uso di Microsoft Azure Devops rispetto ad AWS, che è il fornitore attuale.

Abbiamo sperimentato Azure DevOps, Azure Pipelines, Azure Repo e l'avvio di un nuovo server in Azure tramite Terraform.

Abbiamo sperimentato l'ottenimento di supporto dai rappresentanti Microsoft.

Abbiamo raccolto informazioni da colleghi su blog e Hacker News.


### Argomento

Azure DevOps pubblicizza un eccellente insieme di offerte, ma non reggono, non funzionano bene insieme e il supporto è scarso.

La nostra esperienza diretta:

  * La configurazione di Azure è un pasticcio di interfacce, alcune delle quali si sovrappongono agli account Microsoft e altre no. Per esempio, c'è un accesso Azure, un accesso Microsoft.com, un accesso Live.com ecc. e tutti sono in gioco contemporaneamente.

  * Abbiamo incontrato un problema di sicurezza minore durante la configurazione e non abbiamo trovato alcuna soluzione. Abbiamo provato in molti modi a segnalarlo a molti rappresentanti Microsoft, senza successo. Lo abbiamo segnalato con successo alla sicurezza di Microsoft, che ha risposto che non verrà corretto (won't fix).

  * La documentazione è spesso sbagliata o obsoleta. Almeno una parte di ciò è dovuta al motore di ricerca scadente di Microsoft e una parte a una SEO mediocre.
  
  * La configurazione di Terraform è ben documentata e funziona. Tuttavia, il supporto di Terraform è debole rispetto ad AWS perché Microsoft sta costruendo relazioni commerciali con i fornitori per realizzare esempi di configurazione Terraform concatenati.

Le esperienze dei nostri colleghi:

  * Dopo aver fatto la nostra valutazione alla cieca, abbiamo cercato le esperienze dei colleghi. Ciò che abbiamo trovato ha confermato le nostre esperienze.

  * I colleghi hanno segnalato ulteriori problemi con i tempi di build e problemi con il server di build portato dall'utente. Questi problemi sono significativamente più gravi dei problemi di interfaccia, perché eseguire le build è lo scopo principale di una pipeline di build e prevediamo di eseguirne molte al giorno.

  * Abbiamo trovato un'eccellente partecipazione dei colleghi di Azure nelle aree di discussione. Complimenti a Microsoft per questo. Siamo particolarmente colpiti da Edward Thomson, Azure PM e programmatore, per la sua partecipazione, franchezza e spiegazioni tecniche.


### Implicazioni

Scegliere Microsoft Azure DevOps sembra probabilmente più costoso (~3x) in tempo e costi rispetto al non scegliere Azure.


## Correlato


### Decisioni correlate

Se scegliamo Azure DevOps, ci sono molte offerte correlate, tra cui Azure Repo, Azure Pipeline ecc. Crediamo che, se scegliamo Azure Devops, ciò possa rendere più facile usare più capacità di Azure o rendere più difficile usare le capacità di altri fornitori.

Crediamo che Microsoft stia facendo grandi passi avanti nell'esperienza dello sviluppatore e vediamo Microsoft fare grandi acquisizioni di strumenti per sviluppatori (per esempio GitHub) e di dipendenze (per esempio Citus).

Se scegliamo Azure DevOps, potremmo voler dare enfasi alla scelta delle offerte derivanti dalle acquisizioni Microsoft e potremmo anche voler affrontare le offerte acquisite con più cura/valutazione a causa di un potenziale rigetto, per esempio il rischio di turnover del personale.


### Requisiti correlati

Vogliamo che i tempi di build siano molto rapidi. Accettiamo di pagare un premio elevato per questo. Questo perché vogliamo iterare molto velocemente.

Vogliamo che l'affidabilità sia molto alta. Accettiamo di pagare un premio elevato per questo. Questo perché stiamo testando casi d'uso di alto valore, comprese transazioni finanziarie, transazioni riservate ecc.

I nostri primi 4 KPI devops includono il tempo medio di ripristino, il che richiede build veloci e alta affidabilità.


### Artefatti correlati

Vogliamo che il sistema di build produca artefatti adatti all'uso in altri sistemi, come Artifactory.


### Principi correlati

Facilmente reversibile. Possiamo valutare Azure DevOps in parallelo con il fornitore attuale AWS.


## Note


### Microsoft Devops CI: un'avventura insoddisfacente

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Post di blog.

"Come sviluppatore software, so per esperienza diretta quanto sia difficile costruire prodotti di qualità in modo rapido ed economico. È una forma d'arte che a volte riusciamo a fare bene, e altre volte degenera in qualcosa di simile al sito governativo sanitario dell'era Obama. Il nostro livello di controllo sul prodotto risultante varia, e la colpa del fallimento ricade spesso sulle persone sbagliate nella gerarchia decisionale. Azure DevOps di Microsoft (precedentemente noto come Visual Studio Team Services), nonostante intenzioni chiaramente buone, è una tempesta perfetta di cattive decisioni e scarsa esecuzione."


### Punti salienti della discussione su Hacker News

https://news.ycombinator.com/item?id=18983586

"Usiamo Azure DevOps in modo estensivo al mio lavoro e, dopo aver usato GitHub, Gitlab, soluzioni self-hosted, Jenkins, TeamCity... Azure DevOps si classifica ultimo."

"L'interfaccia è terribilmente goffa ovunque. Il peggio per me sono le pull request. Incredibilmente difficile lavorare con le persone su una pull request. Non posso nemmeno indicare un "singolo" problema particolare - per noi è rotto ovunque."

"Azure Devops è qualcosa che vorrei amare. L'interfaccia continua a cambiare, ma non risolve i bug sottostanti che esistono da secoli."

"Gli strumenti non sono ben integrati, l'interfaccia è davvero lenta, non c'è una vista dashboard delle pull request attive, build, release ecc. per i miei repository preferiti. I tempi di build/deployment sono incredibilmente lenti."

"Abbiamo provato a usare anche Azure Boards (Work Items, Boards, Backlogs ecc.). Ahi. È un completo pasticcio di interfaccia di idee sconnesse. Invece di implementare una cosa bene, ne hanno implementate due dozzine in modo terribile."


### Windows Development MVP

Windows Development MVP qui. Sento di dover sostenere parte della responsabilità per non aver parlato più forte di questi problemi. Ma devo dire che sono deluso nel sentire che siete "sorpresi" dai problemi di UX. Ho detto alla vostra gente che la UX è terribile (per esempio già prima del lancio) e continuavo a sentirmi rispondere "lo sappiamo, la stiamo sistemando". Inizierò a formalizzare il feedback e a farlo passare per i canali, restate sintonizzati. Sono anche locale (Bellevue) e mi piacerebbe venire a provare a far passare nella pipeline la nostra app open source .net/wpf/uwp relativamente semplice. Sospetto che sarà un'esperienza illuminante per entrambi.

Alcuni esempi:

* Non si può costruire una pipeline con un repo git che contiene sottomoduli

* Ho trovato impossibile modificare il PATH per alcuni strumenti personalizzati

* L'esperienza della nuova pipeline semplicemente non ha molto senso; i nuovi utenti che cliccano in giro finiranno alla fine nella documentazione sbagliata.


### Riepilogo di Edward Thomson (Azure PM)

Ho scritto il codice che unisce le tue pull request. Program Manager in Microsoft per Azure DevOps; in precedenza ingegnere software sugli strumenti di controllo di versione in GitHub, Microsoft, SourceGear.

https://www.edwardthomson.com/

Co-maintainer di libgit2. https://libgit2.github.io

Co-conduttore di All Things Git, il podcast su Git. https://www.allthingsgit.com/

Curatore di Developer Tools Weekly, una newsletter sugli strumenti di sviluppo. https://developertoolsweekly.com/
