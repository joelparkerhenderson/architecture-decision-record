# Tidsstempelformat

Indhold:

* [Resumé](#resumé)
  * [Problemstilling](#problemstilling)
  * [Beslutning](#beslutning)
  * [Status](#status)
* [Detaljer](#detaljer)
  * [Antagelser](#antagelser)
  * [Begrænsninger](#begrænsninger)
  * [Standpunkter](#standpunkter)
  * [Argument](#argument)
  * [Implikationer](#implikationer)
* [Relateret](#relateret)
  * [Relaterede beslutninger](#relaterede-beslutninger)
  * [Relaterede krav](#relaterede-krav)
  * [Relaterede artefakter](#relaterede-artefakter)
  * [Relaterede principper](#relaterede-principper)
* [Noter](#noter)


## Resumé


### Problemstilling

Vi vil kunne spore, hvornår ting sker, ved hjælp af tidsstempler og et konsistent tidsstempelformat, der fungerer godt på tværs af alle vores systemer og tredjepartssystemer.

Vi interagerer med systemer, der har forskellige tidsstempelformater:

* JSON-beskeder har intet native tidsstempelformat, så vi skal vælge, hvordan et tidsstempel konverteres til en streng, og en streng konverteres til et tidsstempel, dvs. hvordan der serialiseres/deserialiseres.

* Nogle applikationer er indstillet til at bruge lokal tid frem for UTC-tid. Det kan være praktisk for projekter, der skal tilpasse sig lokal tid, såsom projekter, der udløser hændelser baseret på lokal tid.

* Nogle systemer har forskellige behov og muligheder for tidspræcision, såsom en tidsopløsning på sekunder versus millisekunder versus nanosekunder. For eksempel bruger kommandoen `date` i operativsystemet Linux som standard en tidspræcision på sekunder, mens Nasdaq-børsen som standard ønsker en tidspræcision på nanosekunder.


### Beslutning

Vi vælger tidsstempelstandardformatet ISO 8601 med nanosekundpræcision, specifikt "YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ".

Formatet viser år, måned, dag, time, minut, sekund, nanosekunder og Zulu-tidszonen, også kaldet UTC, GMT.


### Status

Besluttet.


## Detaljer


### Antagelser

Vi skal håndtere disse tidsstempeltekststrenge, for at konvertere fra et tidsstempel til en streng (også kaldet serialisere) og konvertere fra en streng til et tidsstempel (også kaldet deserialisere).

Vi vil have et format, der generelt er nemt at bruge, nemt at konvertere og nemt for et menneske at læse.

Vi ønsker kompatibilitet med et bredt udvalg af eksterne systemer, som vi ikke kan kontrollere, såsom analysesystemer, databasesystemer og finansielle systemer.


### Begrænsninger

Nogle systemer har begrænsninger i tidspræcision. For eksempel kan kommandoen `date` i operativsystemet macOS udskrive tidspræcision i sekunder, men ikke i nanosekunder.


### Standpunkter

Vi overvejede en række muligheder:

* Unix-epoke, dvs. ét stigende tal.

* Kortfattet tekstformat "YYYYMMDDTHHMMSSNNNNNNNNN".

* Brug af en lokal tidszone versus UTC-tidszonen.


### Argument

Til typisk brug sætter vi mere pris på let at læse/skrive for mennesker end på rå hastighed/størrelse.

Til typisk brug vil vi have et format, der fungerer fint i maskinsystemer og også fungerer godt manuelt, såsom ved skrivning af eksempeldata, læsning af JSON-output, grep i en logfil osv.

Til atypisk brug, såsom højtydende databehandling, forventer vi, at vi vil optimere ethvert tekstformat, vi vælger, ved at konvertere teksten til et hurtigere format, såsom et programmeringssprogs indbyggede datoobjekttype. Så tekstformatet er ikke så vigtigt for HPC.


### Implikationer

Vores forskellige tekstsystemer og tidssystemer vil konvergere mod dette format.


## Relateret


### Relaterede beslutninger

Vi vil måske også have en hurtig/nem måde at spore tidsforskelle, også kaldet varigheder. De er nemme med Unix-epoke-tidsstempler.


### Relaterede krav

Vi vil måske justere vores beslutning, f.eks. hvis vi har et relateret krav om en bestemt slags logbeskedstempel, såsom til Splunk, Sumo, ELK osv.


### Relaterede artefakter

Sprogformattere og -parsere:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Rosetta Code-eksempler:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

SixArm-eksempler:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Relaterede principper

Let at gøre om. Vi kan ret nemt skifte til et andet format, såsom Unix-epoke.

Udskyd for tidlig optimering. Til typisk brug er vi ikke meget optaget af en håndfuld ekstra tegn såsom et format, der bruger bindestreger og kolon.


## Noter

Tilføj noter her.
