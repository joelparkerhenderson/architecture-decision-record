# {Din titel här}

!!! info

    **Tillstånd**: { Proposed | Under Review | Accepted |  Rejected | Superseded | Deprecated }
    
    **Uppdaterad**: {YYYY-MM-DD}

## Sammanfattning

{Det här är den ”ledningssammanfattning” eller ”hisspresentation” som hör till din ADR. Ange i några
koncisa meningar (vanligen 2–4) tydligt det centrala problemet, frågan eller möjligheten som den
här ADR:en behandlar. Inkludera en kort antydan om beslutet som fattats eller fokusområdet. Målet
är att hjälpa läsare att snabbt förstå vad den här ADR:en handlar om och avgöra om den är relevant
för dem, utan att behöva läsa hela dokumentet. Tänk på det som sammandraget av en teknisk artikel
eller en mycket kort introduktion till huvudämnet.}

## Drivkrafter

{Det här avsnittet förklarar **varför** beslutet fattas **nu**. Formulera tydligt de primära
motiven, behoven eller problemen som gör det här arkitekturbeslutet nödvändigt. Tänk på de
underliggande skälen och trycket.}

* {t.ex. Vi utvecklar en ny funktion/förmåga som behöver...}

* {t.ex. Vi behöver förbättra prestanda, tillgänglighet, avveckla skuld...}

* {t.ex. Återkoppling från användare tyder på att...}

* {t.ex. Det nuvarande tillvägagångssättet innebär följande begränsningar...}

## Alternativ

{Här listar du de olika alternativ du överväger. Håll dig till fakta och undvik åsikter, nästa
avsnitt behandlar analysen. Inkludera en kortfattad beskrivning, länkar till relevant dokumentation
eller exempel.

Inkludera alla betydande alternativ du utforskade, även om de till slut inte valdes. Målet är att ge
läsarna en tydlig, opartisk förståelse av varje alternativ innan du går in på utvärderingen.}

### {Alternativ 1:s titel}

{Beskriv alternativet, ge en sammanfattning, lista fakta, ange länkar osv.}

### {Alternativ n:s titel}

...

## Alternativanalys

{Här utvärderar du kritiskt varje alternativ som presenterades i avsnittet *Alternativ*. För varje
alternativ, ge en balanserad bild av dess fördelar, nackdelar och eventuella andra relevanta
överväganden eller avvägningar. Var specifik och, där det är möjligt, knyt dina punkter tillbaka
till *Drivkrafterna*.

Överväg aspekter som:

* Kostnad (utveckling, drift, licensiering)

* Komplexitet (implementation, underhåll, inlärningskurva)

* Risker (tekniska, operativa, säkerhet)

* Överensstämmelse med arkitekturprinciper eller befintliga standarder

* Påverkan på prestanda, skalbarhet, användbarhet, underhållbarhet,
    säkerhet osv.

Ta med så många Fördel/Nackdel/Övrigt-påståenden som behövs.
}

### {Bedömning av alternativ 1}

* Fördel: {En specifik fördel eller nytta med det här alternativet.}

* Nackdel: {En specifik nackdel, risk eller kostnad som hör till det här alternativet.}

* Övrigt: {En relevant punkt som inte strikt är en fördel eller nackdel.}

### {Bedömning av alternativ n}

...

## Rekommendation

{Här anger du tydligt det slutliga beslutet och namnger uttryckligen det alternativ som har valts.
Förklara i detalj **varför** det här alternativet valdes. Du bör tydligt redogöra för hur det valda
alternativet bäst adresserar *Drivkrafterna* och uppfyller de viktigaste kraven eller löser det
angivna problemet.}

### Konsekvenser

{Det här avsnittet är **valfritt**.}

{Nu när ett beslut har fattats, vilka är de förväntade utfallen och effekterna, både positiva och
negativa? Vilka kända begränsningar, kostnader eller risker accepteras genom att fatta det här
beslutet? Hur kommer beslutet att påverka olika intressenter, andra system, utvecklingsmetoder,
driftsrutiner eller användarupplevelsen?}

* Fördel: {Ett specifikt positivt utfall eller en nytta som förväntas av det här beslutet.}

* Nackdel: {En specifik accepterad nackdel, kostnad eller risk till följd av det här
    beslutet. }

* Övrigt: {En konsekvens som inte strikt är en fördel eller nackdel.}

### Bekräftelse

{Det här avsnittet är **valfritt**.}

{Beskriv hur genomförandet av det här beslutet kommer att verifieras och hur fortlöpande efterlevnad
kommer att säkerställas. Det hjälper till att visa att beslutet inte bara är teoretiskt utan
aktivt kommer att omsättas i praktiken och följas upp.

Hur kontrollerar du att beslutet har genomförts korrekt? (t.ex. kodgranskningar, specifika tester,
demonstrationer, kollegagranskning).

Hur upprätthålls efterlevnaden av beslutet över tid? (t.ex. automatiserade kontroller, periodiska
revisioner, uppdateringar av teamets riktlinjer, utbildning).

Finns det specifika mått eller indikatorer som visar att beslutet uppnår sina avsedda positiva
utfall? (t.ex. prestandajämförelser, användningsgrad, minskning av specifika fel, betyg på
användarfeedback).

Vem ansvarar för att övervaka detta, och vad händer om beslutet inte följs?}

## Mer information

{Det här avsnittet är **valfritt**.}

{Använd det här avsnittet för att ge kompletterande information som stöder beslutet, tillför
sammanhang eller vägleder framtida åtgärder. Länkar till andra beslut och resurser kan också
förekomma här.

Du kan kort notera vilka som var delaktiga i beslutsprocessen och om/hur samsyn uppnåddes. Du kan
också föreslå en tidsram eller specifika händelser som kan föranleda en omprövning av det här
beslutet i framtiden.}
