# Modello di registro delle decisioni per il business case

Questo modello di ADR sottolinea la redazione di un business case per una decisione, inclusi criteri, candidati e costi.


## Livello più alto

* Titolo
* Stato
* Criteri di valutazione
* Candidati da considerare
* Ricerca e analisi di ciascun candidato
  * Soddisfa/non soddisfa i criteri e perché
  * Analisi dei costi
  * Analisi SWOT
  * Opinioni e feedback
* Raccomandazione


## Livello più approfondito

**Titolo**:

  * Breve frase all'imperativo presente, meno di 50 caratteri, come un messaggio di commit git.

**Stato**:

  * Uno tra: proposed, accepted, rejected, deprecated, superseded ecc.

**Criteri di valutazione**:

  * Riepilogo: descrivi brevemente che cosa stai cercando di scoprire e perché.

  * Dettagli

**Candidati da considerare**:

  * Riepilogo: descrivi brevemente come hai trovato i candidati e richiama l'attenzione sui valori anomali.

  * Elenca tutti i candidati e le opzioni pertinenti. Che cosa stai valutando come soluzioni potenziali?

  * Dettagli

**Ricerca e analisi di ciascun candidato**:

  * Riepilogo: descrivi brevemente come hai svolto la ricerca e richiama l'attenzione su pattern, cluster e valori anomali.

  * Soddisfa/non soddisfa i criteri e perché

    * Riepilogo

    * Dettagli

  * Analisi dei costi

    * Riepilogo

    * Esempi

      * Licenze. Per esempio accordi contrattuali e impegni legali

      * Formazione. Per esempio sviluppo delle capacità e gestione del cambiamento

      * Esercizio. Per esempio supporto e manutenzione

      * Misurazione dell'uso. Per esempio larghezza di banda e uso della CPU

  * Analisi SWOT

    * Riepilogo

    * Punti di forza (Strengths)

    * Punti di debolezza (Weaknesses)

    * Opportunità (Opportunities)

    * Minacce (Threats)

  * Opinioni e feedback interni

    * Riepilogo

    * Esempi

      * Dal team, idealmente scritti dalle parti effettive

      * Da altre parti interessate

      * Attributi di qualità, noti anche come requisiti trasversali 

  * Opinioni e feedback esterni

    * Riepilogo

    * Chi sta fornendo l'opinione?

    * Quali altri candidati hanno considerato?

    * Che cosa stanno costruendo? 

      * Esempi

        * B2B o B2C

        * Rivolto all'esterno o solo ai dipendenti

        * Desktop o mobile

        * Pilota o produzione

        * Monolite o microservizi

    * Come hanno valutato i candidati?

    * Perché hanno scelto il vincitore?

    * Che cosa è successo da allora?

      * Esempi

        * Come si comporta il vincitore?

        * Quale percentuale del traffico utente di produzione reale passa attraverso il vincitore?

        * Che tipo di integrazione è coinvolta, come l'integrazione con pipeline di consegna continua, sistemi di gestione dei contenuti, analisi e metriche ecc.?

        * In base a ciò che sanno ora, che cosa consiglierebbero di fare diversamente?

  * Aneddoti

**Raccomandazione**:

  * Riepilogo

  * Dettagli

