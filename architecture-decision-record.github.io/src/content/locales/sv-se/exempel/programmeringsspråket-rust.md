# Arkitekturbeslutspost: Programmeringsspråket Rust

Beslutsnummer: AR-001

Beslutstitel: Införande av programmeringsspråket Rust

Datum: 1 december 2021

Tillstånd: Godkänd

### Problemformulering

När vi fortsätter att utveckla programvaruapplikationer har vi observerat att det blir allt svårare att mildra potentiella säkerhetssårbarheter och förhindra körtidsfel. Med de befintliga programmeringsspråken, som C och C++, upplever vi fortsatt problem som buffertöverskridningar, minnesläckor och odefinierat beteende som leder till att applikationer kraschar. Vi behöver ett programmeringsspråk som ger garantier för minnessäkerhet och är tillräckligt effektivt för att stödja prestandakritiska applikationer.

### Överväganden

Flera programmeringsspråk är utformade för att åtgärda de befintliga problemen. Bland dem har programmeringsspråket Rust fått stor uppmärksamhet från utvecklargemenskapen på grund av sina unika designegenskaper. Överväganden inkluderar;

1. Minnessäkerhet och säkerhet

2. Prestanda och effektivitet

3. Communitystöd och spridning

4. Inlärningskurva

5. Verktyg och ekosystem

6. Kompatibilitet med befintliga programvarusystem.

### Begränsningar

Att anta ett nytt programmeringsspråk kräver omskolning av utvecklare, vilket tar tid och resurser. Att integrera språket i det befintliga utvecklingsarbetsflödet kan vara en utmaning. Vi måste säkerställa kompatibilitet med de befintliga systemen och undvika brytande ändringar för att upprätthålla kontinuitet.

### Implementation

1. Vårt utvecklingsteam kommer att genomgå utbildning för att lära sig och bekanta sig med programmeringsspråket Rust.

2. Vi kommer att skapa ett nytt projekt med Rust på prov för att utvärdera dess kompatibilitet och lämplighet för våra utvecklingsändamål.

3. Vi kommer gradvis att migrera befintliga system skrivna i C och C++ till Rust.

4. Vi kommer att samarbeta med Rust-gemenskapen för att utforska de tillgängliga verktygen och biblioteken som kan förbättra vårt utvecklingsarbetsflöde.

5. Vi kommer att övervaka Rusts prestanda och regelbundet jämföra den med de befintliga programmeringsspråkens prestanda.

6. Vi kommer att anta ett långsiktigt tillvägagångssätt som balanserar kostnaderna för utbildning och integration mot de potentiella fördelarna med att använda Rust.

### Motivering

Vi har antagit Rust på grund av dess unika funktioner som är utformade för att ge garantier för minnessäkerhet och säkerhet samtidigt som prestanda och effektivitet bibehålls. Rusts robusta typsystem, lånegranskare (borrow checker) och minnessäkerhetskoncept gör det mycket lämpligt för att utveckla prestandakritiska och säkerhetskritiska applikationer. Dessutom har Rust en betydande gemenskap av utvecklare, vilket ger oss tillgång till ett brett utbud av verktyg, bibliotek och ekosystem som stöder vårt utvecklingsarbetsflöde. Även om Rust har en inlärningskurva tror vi att fördelarna med att anta Rust överväger kostnaderna och ger en utmärkt möjlighet till fortsatt tillväxt och innovation.

### Konsekvenser

1. Införandet av Rust kommer att kräva en betydande investering i tid och resurser för att utbilda utvecklare och integrera språket i det befintliga utvecklingsarbetsflödet.

2. Att anta Rust kan orsaka en viss grad av kompatibilitetsproblem med befintliga system, vilket kräver omstrukturering och ändringar.

3. Införandet av Rust kan öka antalet utvecklare som kan bidra till vårt projekt genom att locka Rust-utvecklare som vill arbeta med spännande projekt.

4. Införandet kan leda till förbättrad prestanda, effektivitet och säkerhet jämfört med de befintliga språken.

5. Slutligen medför införandet av Rust den potentiella fördelen att minska säkerhetssårbarheter i våra applikationer.
   
<h6>Källhänvisning: Den här sidan är genererad av ChatGPT och därefter redigerad för tydlighet och format.</h6>
