# Arkitekturbeslutspost: Kodredigerare för programmering

## Sammanhang

Kodredigerare för programmering är ett väsentligt verktyg för utvecklare att skriva och redigera kod. Det finns många kodredigerare tillgängliga, var och en med sin egen uppsättning funktioner, fördelar och nackdelar. Syftet med den här ADR:en är att dokumentera de arkitekturbeslut som fattats för kodredigerare för programmering.

## Prioriteringar

Arkitekturen för kodredigerare för programmering bör prioritera följande:

* **Modularitet**: Kodredigeraren bör utformas på ett modulärt sätt så att utvecklare kan anpassa och utöka den efter behov. Det möjliggör en flexibel arkitektur som kan anpassas till olika utvecklares och teams behov.

* **Prestanda**: Kodredigeraren bör vara högpresterande och responsiv, så att utvecklare kan arbeta effektivt utan att bromsas av verktyget de använder.

* **Användargränssnitt**: Användargränssnittet bör vara intuitivt och lätt att använda, så att utvecklare kan fokusera på sin kod i stället för att kämpa med redigeraren.

* **Utökningsbarhet**: Kodredigeraren bör utformas för att möjliggöra enkel utökning med tredjepartsinsticksmoduler och integrationer.

* **Kompatibilitet**: Kodredigeraren bör vara kompatibel med ett brett utbud av programmeringsspråk och tekniker, vilket gör den till ett användbart verktyg för ett brett spektrum av utvecklare.

## Beslut

Baserat på dessa prioriteringar bör arkitekturen för kodredigerare för programmering utformas med följande komponenter:

* **Kärna**: Den här komponenten tillhandahåller kodredigerarens grundläggande funktionalitet, som syntaxmarkering, textredigering och filhantering.

* **UI**: Den här komponenten tillhandahåller användargränssnittet för kodredigeraren, inklusive menyer, verktygsfält och kortkommandon.

* **Insticksmoduler**: Den här komponenten låter utvecklare utöka kodredigerarens funktionalitet genom att installera tredjepartsinsticksmoduler. Insticksmoduler kan tillhandahålla ytterligare funktioner, som kodkomplettering, linting eller felsökning.

* **Integrationer**: Den här komponenten gör att kodredigeraren kan integreras med andra verktyg och tekniker, som versionshanteringssystem, byggsystem eller felsökningsverktyg.

## Motivering

Kodredigerarens modularitet gör det möjligt för utvecklare att anpassa och utöka den efter behov. Det här är viktigt eftersom olika utvecklare och team har olika behov och arbetsflöden, och en flexibel arkitektur kan tillgodose dessa skillnader.

* **Prestanda**: avgörande eftersom utvecklare behöver kunna arbeta effektivt utan att bromsas av sina verktyg. En högpresterande kodredigerare är nödvändig för produktivitet och kan hjälpa utvecklare att behålla sitt fokus och sin koncentration.

* **UI**: viktigt eftersom det gör att utvecklare kan fokusera på sin kod i stället för att kämpa med redigeraren. Det kan leda till bättre produktivitet och mindre frustration för utvecklare.

* **Utökningsbarhet**: kraftfullt eftersom det gör att kodredigeraren kan anpassas till olika behov och arbetsflöden. Tredjepartsinsticksmoduler och integrationer kan tillhandahålla ytterligare funktioner och förmågor som inte ingår i kärnredigeraren.

* **Kompatibilitet**: värdefullt eftersom det gör att kodredigeraren kan användas med ett brett utbud av programmeringsspråk och tekniker. Det gör redigeraren till ett mer användbart verktyg för ett brett spektrum av utvecklare.

Komponenterna kärna, insticksmoduler, integrationer och UI ger en tydlig åtskillnad av ansvarsområden och möjliggör en modulär arkitektur som enkelt kan utökas och anpassas. Den här arkitekturen är flexibel, högpresterande och kompatibel med ett brett utbud av programmeringsspråk och tekniker, vilket gör den till ett användbart verktyg för utvecklare.
