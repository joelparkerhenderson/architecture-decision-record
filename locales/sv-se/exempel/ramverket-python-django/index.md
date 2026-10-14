# Arkitekturbeslutspost för ramverket Python Django

Beslutsdatum: 2021-07-15

Tillstånd: Godkänd

## Sammanhang

Vår organisation planerar att utveckla en webbapplikation som hanterar kunddata. Vi har valt Python som programmeringsspråk och överväger Django som webbramverk för utveckling av applikationen.

## Beslut

Vi har beslutat att använda webbramverket Django för utveckling av webbapplikationen. Django tillhandahåller en robust uppsättning verktyg och funktioner för att bygga webbapplikationer snabbt och effektivt. 

## Faktorer

Några av de faktorer som påverkade vårt beslut inkluderar:

1. Objektrelationell mappning (ORM): Django har en inbyggd ORM som låter oss interagera med databasen utan att skriva SQL-frågor. Det gör det enklare att utveckla applikationen och underhålla den på lång sikt.

2. MVC-ramverk: Django följer en Model-View-Controller-arkitektur (MVC), vilket gör det enklare att separera applikationens affärslogik och presentationslager.

3. Skalbarhet: Django är känt för sin skalbarhet, vilket gör det till ett utmärkt val för att utveckla storskaliga applikationer.

4. Säkerhet: Django har inbyggda säkerhetsfunktioner, som skydd mot vanliga webbattacker som cross-site scripting (XSS) och SQL-injektion.

5. Communitystöd: Django har en stor och aktiv gemenskap som ger stöd och bidrar till ramverkets utveckling.

## Övervägda alternativ

Vi övervägde andra webbramverk som Flask och Pyramid. Vi fann dock att Django är ett mognare och mer etablerat ramverk med en robust uppsättning funktioner.

Vi diskuterade också att utveckla applikationen utan ett webbramverk och använda bibliotek som SQLAlchemy och Flask-RESTful. Vi fann dock att Django erbjuder bredare funktionalitet, vilket gör det till ett bättre val för en komplett webbapplikation.

## Konsekvenser

Införandet av Django kommer att leda till följande konsekvenser:

1. Enklare att utveckla och underhålla applikationen tack vare Djangos inbyggda verktyg och funktioner.

2. Separation av affärslogik och presentationslager, vilket leder till mer organiserad och lättare underhållen kod.

3. Skalbarhet och robusthet hos applikationen.

4. Inbyggda säkerhetsfunktioner som hjälper till att skydda applikationen mot vanliga webbattacker.

5. Tillgång till en stor och aktiv gemenskap för stöd.

Vi förstår att Django har en brantare inlärningskurva än andra ramverk, men vi anser att det är värt investeringen för de långsiktiga fördelar det ger.

## Slutsats

Baserat på de faktorer som beaktats har vi beslutat att använda webbramverket Django för utveckling av webbapplikationen. Vi tror att Djangos funktioner, communitystöd och skalbarhet gör det till det bästa valet för att bygga en komplett webbapplikation. Vi kommer att utbilda våra utvecklare i att använda Django för att säkerställa att ramverket används effektivt och ändamålsenligt.
