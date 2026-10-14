# Modello di registro delle decisioni per decisioni tecniche importanti (ITD)

Questo è il modello per le decisioni tecniche importanti (Important Technical Decisions, ITD) descritto in
[ITDs: a lean ADR for executive technical decision-making at scale - Ignacio Larrañaga](https://ignaciolarranaga.medium.com/itds-a-lean-adr-for-executive-technical-decision-making-at-scale-e18bb3f6a563).

Un ITD è un'evoluzione mirata dell'ADR, ottimizzata per velocità, chiarezza e
validazione da parte della dirigenza. Mentre un ADR documenta ciò che è stato deciso, un ITD è un
artefatto lean, che mette la decisione al primo posto, che rende la decisione stessa rivedibile, così che le parti interessate possano
scorrerla rapidamente e contestarla facilmente. Gli ITD sono adatti a decisioni tecniche che non
riguardano strettamente l'architettura, come la scelta di un modello, di una libreria o di una strategia CI/CD.

In ogni file ITD scrivi queste sezioni:

# Titolo

Enuncia la decisione stessa, non una descrizione dell'argomento.
Per esempio "Usa Qwen2.5 1.5B Instruct per la traduzione sul dispositivo".

## Problema

Una frase che descrive ciò che stiamo cercando di risolvere.

## Opzioni considerate

Le alternative valutate, con l'opzione scelta in **grassetto**.

## Motivazione

Solo i fattori decisivi che hanno portato alla scelta, non un
elenco esaustivo di tutti i pro e i contro.

## Note

Facoltativo. Contesto aggiuntivo che vale la pena registrare, come vincoli, ipotesi o link.
