# Criteri di sostenibilità delle decisioni

<https://www.infoq.com/articles/sustainable-architectural-design-decisions/>

Per definire in modo concreto la sostenibilità delle decisioni, abbiamo ricavato cinque criteri fondamentali.

## Strategica

Chi esamina le conseguenze strategiche quando prende una decisione dovrebbe considerare gli effetti a lungo termine della decisione, come il futuro impegno operativo e di manutenzione.

## Misurabile e gestibile

Le conseguenze di una decisione possono essere misurate e valutate nel tempo in base a criteri oggettivi, idealmente numerici (come quelli degli scenari degli attributi di qualità e proposti nel Workshop 4). Poiché è impossibile catturare tutte le decisioni di dettaglio, gli architetti dovrebbero limitare la granularità delle decisioni a un certo livello di dettaglio (per esempio la creazione di classi di progettazione). Questo porta a un insieme di decisioni più sostenibile e a meno collegamenti di tracciabilità. Inoltre, limitare il numero di dipendenze tra le decisioni riduce l'effetto a catena delle modifiche.

## Raggiungibile e realistica

La motivazione per far corrispondere le soluzioni ai problemi dovrebbe essere scelta in modo pragmatico e resa esplicita. Un architetto può, per esempio, indicare che si è prestata attenzione a evitare un sovradimensionamento o un sottodimensionamento del progetto (cioè che si dovrebbe applicare un approccio "abbastanza buono").

## Radicata nei requisiti

Le decisioni dovrebbero basarsi sull'esperienza e sul contesto specifici del dominio nella progettazione architetturale. Oltre ai requisiti e ai vincoli del progetto, dovrebbe essere considerato anche l'ambiente aziendale, comprese le competenze attuali del team di sviluppo, il budget per la formazione e i processi.

## Senza tempo

Le decisioni dovrebbero basarsi su esperienza e conoscenze che non diventeranno presto obsolete. Un architetto può, per esempio, scegliere pattern o tattiche architetturali neutrali rispetto alla piattaforma.
