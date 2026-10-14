# Arkitekturbeslutspost: API med JSON eller gRPC

## Tillstånd

Godkänd

## Sammanhang

Vi utformar ett API för en ny tjänst som ska användas av flera klienter. Vi har övervägt två alternativ för att implementera API:et: att använda JSON över HTTP eller att använda gRPC.

JSON över HTTP är ett allmänt använt tillvägagångssätt för att bygga API:er och stöds av många programmeringsspråk och ramverk. Det här tillvägagångssättet är enkelt, lättviktigt och lätt att förstå, vilket gör det till ett bra val för många projekt. Det kan dock vara mindre effektivt än andra alternativ, särskilt när det gäller att hantera stora datamängder.

gRPC, å andra sidan, är en nyare teknik som erbjuder ett effektivare sätt att bygga API:er. Den använder binär serialisering för att överföra data, vilket kan vara snabbare och mer kompakt än att använda JSON. gRPC stöder också dubbelriktad strömning, vilket gör det till ett bra val för realtidsapplikationer.

## Beslut

Efter att ha övervägt för- och nackdelarna med båda alternativen har vi beslutat att använda gRPC för vårt API. Även om JSON över HTTP är det enklare alternativet tror vi att gRPC ger en effektivare och mer skalbar lösning för vår tjänst. Vi räknar också med att vårt API kommer att hantera en stor mängd data, och gRPC:s binära serialisering blir effektivare för det här användningsfallet.

Dessutom tror vi att gRPC:s stöd för dubbelriktad strömning kommer att vara fördelaktigt för realtidsapplikationer som vi kan utveckla i framtiden.

## Konsekvenser

Genom att välja gRPC kommer vi att behöva använda en annan uppsättning verktyg och bibliotek för att bygga vårt API jämfört med att använda JSON över HTTP. Det kan kräva extra tid och ansträngning för att lära sig och implementera dessa tekniker. Dessutom kommer klienter som vill använda vårt API att behöva använda gRPC-kompatibla bibliotek, som kanske inte stöds lika brett som bibliotek för JSON över HTTP.

Vi tror dock att fördelarna med att använda gRPC överväger dessa potentiella nackdelar, och vi är säkra på att det här beslutet kommer att resultera i ett effektivare och mer skalbart API.
