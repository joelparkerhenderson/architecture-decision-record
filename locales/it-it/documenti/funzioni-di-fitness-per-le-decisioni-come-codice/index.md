# Funzioni di fitness per le decisioni come codice

Una funzione di fitness è un controllo oggettivo e automatizzato, scritto come codice di programmazione, che verifica che una decisione sia rispettata.

- Le funzioni di fitness rendono le decisioni verificabili e garantibili.

- Le funzioni di fitness per le decisioni possono aiutare molto la garanzia della qualità, i processi normativi e gli obiettivi di governance.

## Come si collegano funzioni di fitness e decisioni

Un registro delle decisioni documenta una decisione; una funzione di fitness la fa rispettare.

- Decisione di esempio: usare l'event sourcing per i requisiti di audit.

- Funzione di fitness di esempio: usare un server di integrazione continua per verificare che ogni cambiamento di stato debba generare un evento.

## Perché le funzioni di fitness aiutano le decisioni

Misurazione oggettiva: una funzione di fitness passa o fallisce, quindi il lavoro è visibile e chiaro.

Uso continuo: una funzione di fitness è una regola viva e viene eseguita a ogni commit e a ogni build.

Fiducia nel refactoring: una funzione di fitness rileva automaticamente gli errori rispetto alle regole di decisione.

Governance scalabile: una funzione di fitness fa rispettare gli standard senza creare colli di bottiglia.

## Le funzioni di fitness possono usare l'IA?

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

## Test unitari dell'architettura

[ArchUnit](https://www.archunit.org/): verifica le regole architetturali del codice Java con un comune framework di test unitari Java.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): verifica le regole architetturali del codice TypeScript e del codice JavaScript con Jest, Vitest, Jasmine e altri.
