# Tidsstämpelformat

Innehåll:

* [Sammanfattning](#sammanfattning)
  * [Problem](#problem)
  * [Beslut](#beslut)
  * [Status](#status)
* [Detaljer](#detaljer)
  * [Antaganden](#antaganden)
  * [Begränsningar](#begränsningar)
  * [Ståndpunkter](#ståndpunkter)
  * [Argument](#argument)
  * [Implikationer](#implikationer)
* [Relaterat](#relaterat)
  * [Relaterade beslut](#relaterade-beslut)
  * [Relaterade krav](#relaterade-krav)
  * [Relaterade artefakter](#relaterade-artefakter)
  * [Relaterade principer](#relaterade-principer)
* [Anteckningar](#anteckningar)


## Sammanfattning


### Problem

Vi vill kunna spåra när saker händer genom att använda tidsstämplar och genom att använda ett konsekvent tidsstämpelformat som fungerar väl över alla våra system och tredjepartssystem.

Vi interagerar med system som har olika tidsstämpelformat:

* JSON-meddelanden har inget inbyggt tidsstämpelformat, så vi behöver välja hur en tidsstämpel konverteras till en sträng och en sträng konverteras till en tidsstämpel, dvs. hur man serialiserar/deserialiserar.

* Vissa applikationer är inställda på att använda lokal tid i stället för UTC-tid. Det kan vara praktiskt för projekt som måste anpassa sig till lokal tid, till exempel projekt som utlöser händelser baserade på lokal tid.

* Vissa system har olika behov och förmågor när det gäller tidsprecision, till exempel att använda en tidsupplösning på sekunder kontra millisekunder kontra nanosekunder. Till exempel använder kommandot `date` i operativsystemet Linux som standard en tidsprecision på sekunder, medan Nasdaq-börsen vill ha en tidsprecision på nanosekunder som standard.


### Beslut

Vi väljer standardtidsstämpelformatet ISO 8601 med nanosekundsprecision, specifikt ”YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ”.

Formatet visar år, månad, dag, timme, minut, sekund, nanosekunder och zulu-tidszonen, alias UTC, GMT.


### Status

Beslutat.


## Detaljer


### Antaganden

Vi behöver hantera dessa textsträngar för tidsstämplar, för att konvertera från en tidsstämpel till en sträng (alias serialisera) och konvertera från en sträng till en tidsstämpel (alias deserialisera).

Vi vill ha ett format som i allmänhet är lätt att använda, lätt att konvertera och lätt för en person att läsa.

Vi vill ha kompatibilitet med ett brett utbud av externa system som vi inte kan kontrollera, till exempel analyssystem, databassystem och finansiella system.


### Begränsningar

Vissa system har begränsningar i tidsprecision. Till exempel kan kommandot `date` i operativsystemet macOS skriva ut tidsprecision i sekunder, men inte i nanosekunder.


### Ståndpunkter

Vi övervägde en rad alternativ:

* Unix-epok, dvs. ett enda stegande tal.

* Kortfattat textformat ”YYYYMMDDTHHMMSSNNNNNNNNN”.

* Att använda en lokal tidszon kontra tidszonen UTC.


### Argument

För typisk användning värdesätter vi lätt att läsa/skriva för människor mer än rå hastighet/storlek.

För typisk användning vill vi ha ett format som fungerar bra i maskinsystem, och även fungerar bra manuellt, till exempel vid skrivande av exempeldata, läsning av JSON-utdata, grep i en loggfil osv.

För atypisk användning, till exempel högpresterande beräkning, förväntar vi oss att vi vill optimera vilket textformat vi än väljer genom att konvertera texten till ett snabbare format, till exempel ett programmeringsspråks inbyggda datumobjekttyp. Så textformatet spelar inte så stor roll för HPC.


### Implikationer

Våra olika textsystem och tidssystem kommer att konvergera mot det här formatet.


## Relaterat


### Relaterade beslut

Vi kanske också vill ha ett snabbt/enkelt sätt att spåra tidsdeltan, alias varaktigheter. Dessa är enkla med Unix-epok-tidsstämplar.


### Relaterade krav

Vi kan vilja justera vårt beslut t.ex. om vi har ett relaterat krav på en specifik typ av loggmeddelandestämpel, till exempel för Splunk, Sumo, ELK osv.


### Relaterade artefakter

Formaterare och tolkare för språk:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Rosetta Code-exempel:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

SixArm-exempel:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Relaterade principer

Lätt att ångra. Vi kan ganska lätt byta till ett annat format, till exempel Unix-epok.

Skjut upp förtida optimering. För typisk användning bryr vi oss inte så mycket om en handfull extra tecken, till exempel ett format som använder bindestreck och kolon.


## Anteckningar

Lägg till anteckningar här.
