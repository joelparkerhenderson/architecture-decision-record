# Modello di registro delle decisioni architetturali (ADR) <!-- Replace with ADR title -->

Questo è un modello per gli ADR di EdgeX Foundry.

Fonte: https://docs.edgexfoundry.org/2.3/design/adr/template/


### Proponenti

Elenca i proponenti dell'ADR.

Formato:

- Nome (organizzazione)


## Registro delle modifiche

Elenca le modifiche al documento, inclusi stato, data e URL della pull request.

Lo stato è uno tra: pending, approved, amended, deprecated.

La data è una stringa ISO 8601 (YYYY-MM-DD).

La PR è la pull request che ha presentato la modifica e include informazioni come diff, contributori e revisori.

Formato:

- \[stato dell'ADR, per esempio approved, amended ecc.\]\(URL della pull request\) YYYY-MM-DD


## Casi d'uso di riferimento

Elenca tutti i documenti di casi d'uso / requisiti pertinenti.

Un ADR richiede almeno un caso d'uso pertinente e approvato.

Formato:

- \[Nome del caso d'uso\]\(URL\)

Aggiungi una spiegazione se l'ADR non copre tutti i requisiti del caso d'uso.


## Contesto

Descrivi:

- Perché il progetto è architetturalmente significativo - perché serve un ADR (invece di una semplice issue e PR per risolvere il problema)

- L'approccio progettuale di alto livello (i dettagli vanno nella progettazione proposta qui sotto)


## Progettazione proposta

I dettagli della progettazione (se possibile senza scendere nell'implementazione).

Panoramica di:

- I servizi/moduli interessati (modificati)

- I nuovi servizi/moduli aggiunti

- Impatto su modelli e DTO (modificare/aggiungere/rimuovere)

- Impatto sulle API (modificare/aggiungere/rimuovere)

- Impatto sulla configurazione comune (nuova sezione, modificare/aggiungere/rimuovere)

- Impatto sul devops


## Considerazioni

Documenta alternative, preoccupazioni, questioni collaterali o correlate e domande sollevate durante la discussione dell'ADR. 

Indica se e come sono state risolte o mitigate.


## Decisione

Documenta importanti dettagli di implementazione concordati, avvertenze, considerazioni future e questioni di progettazione residue o rinviate.

Documenta le parti dei requisiti che non sono soddisfatte dalla progettazione proposta.


## Altri ADR correlati

Elenca gli ADR correlati, per esempio decisioni di progettazione per sottocomponenti della funzionalità, progetti resi obsoleti da questo progetto ecc.. 

Formato:

- \[Titolo dell'ADR\]\(URL\) - rilevanza


## Riferimenti

Elenca eventuali riferimenti aggiuntivi.

Formato:

- \[Titolo\]\(URL\)

