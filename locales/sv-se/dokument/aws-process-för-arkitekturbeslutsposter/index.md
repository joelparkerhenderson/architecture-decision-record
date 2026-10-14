# AWS process för arkitekturbeslutsposter

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

En arkitekturbeslutspost (architectural decision record, ADR) är ett dokument som beskriver ett val som teamet gör om en betydande aspekt av den programvaruarkitektur de planerar att bygga. Varje ADR beskriver arkitekturbeslutet, dess sammanhang och dess konsekvenser. ADR:er har tillstånd och följer därför en livscykel. Ett exempel på en ADR finns i bilagan.

ADR-processen producerar en samling arkitekturbeslutsposter. Den här samlingen bildar beslutsloggen. Beslutsloggen ger projektets sammanhang samt detaljerad information om implementation och design. Projektmedlemmar skummar rubrikerna i varje ADR för att få en överblick över projektets sammanhang. De läser ADR:erna för att gå på djupet med projektets implementation och designval.

När teamet godkänner en ADR blir den oföränderlig. Om nya insikter kräver ett annat beslut föreslår teamet en ny ADR. När teamet godkänner den nya ADR:en ersätter den den tidigare ADR:en.

## ADR-processens omfattning

Projektmedlemmar bör skapa en ADR för varje arkitektoniskt betydelsefullt beslut som påverkar programvaruprojektet eller produkten, bland annat följande (Richards och Ford 2020):

* Struktur (till exempel mönster som mikrotjänster)

* Icke-funktionella krav (säkerhet, hög tillgänglighet och feltolerans)

* Beroenden (koppling mellan komponenter)

* Gränssnitt (API:er och publicerade kontrakt)

* Konstruktionstekniker (bibliotek, ramverk, verktyg och processer)

* Funktionella och icke-funktionella krav är de vanligaste indata till ADR-processen.


## ADR:ens innehåll

När teamet identifierar ett behov av en ADR börjar en teammedlem skriva ADR:en utifrån en projektövergripande mall. (Se ADR-organisationen på GitHub för exempelmallar.) Mallen förenklar skapandet av ADR:er och säkerställer att ADR:en fångar all relevant information. Som minimum bör varje ADR definiera beslutets sammanhang, själva beslutet och beslutets konsekvenser för projektet och dess leveranser. (Exempel på dessa avsnitt finns i bilagan.) En av de mest kraftfulla aspekterna av ADR-strukturen är att den fokuserar på skälet till beslutet snarare än på hur teamet genomförde det. Att förstå varför teamet fattade beslutet gör det lättare för andra teammedlemmar att anamma det och hindrar andra arkitekter som inte var delaktiga i beslutsprocessen från att åsidosätta beslutet i framtiden.


## Process för att införa ADR:er

Varje teammedlem kan skapa en ADR, men teamet bör fastställa en definition av ägarskap för en ADR. Varje författare som är ägare till en ADR bör aktivt underhålla och kommunicera ADR:ens innehåll. För att förtydliga detta ägarskap kallar den här guiden ADR-författare för ADR-ägare i följande avsnitt. Andra teammedlemmar kan alltid bidra till en ADR. Om innehållet i en ADR ändras innan teamet godkänner den bör ägaren godkänna ändringarna.

När teamet har identifierat ett arkitekturbeslut och dess ägare lämnar ADR-ägaren in ADR:en i tillståndet **Proposed** (Föreslagen) i början av processen. ADR:er i tillståndet Proposed är redo för granskning.

ADR-ägaren inleder sedan granskningsprocessen för ADR:en. Målet med ADR-granskningsprocessen är att avgöra om teamet godkänner ADR:en, kommer fram till att den behöver omarbetas eller avvisar ADR:en. Projektteamet, inklusive ägaren, granskar ADR:en. Granskningsmötet bör inledas med en avsatt tid för att läsa ADR:en. I genomsnitt bör 10 till 15 minuter räcka. Under den här tiden läser varje teammedlem dokumentet och lägger till kommentarer och frågor för att flagga oklara ämnen. Efter granskningsfasen läser ADR-ägaren upp och diskuterar varje kommentar med teamet.

Om teamet hittar åtgärdspunkter för att förbättra ADR:en förblir ADR:ens tillstånd **Proposed**. ADR-ägaren formulerar åtgärderna och tilldelar, i samarbete med teamet, en ansvarig till varje åtgärd. Varje teammedlem kan bidra till och lösa åtgärdspunkterna. Det är ADR-ägarens ansvar att boka om granskningsprocessen.

Teamet kan också besluta att avvisa ADR:en. I så fall lägger ADR-ägaren till ett skäl till avvisningen för att förhindra framtida diskussioner om samma ämne. Ägaren ändrar ADR:ens tillstånd till **Rejected** (Avvisad).

Om teamet godkänner ADR:en lägger ägaren till en tidsstämpel, en version och en lista över intressenter. Ägaren uppdaterar sedan tillståndet till **Accepted** (Godkänd).

ADR:er och den beslutslogg de skapar representerar beslut som teamet fattat och ger en historik över alla beslut. Teamet använder ADR:erna som referens vid kod- och arkitekturgranskningar där det är möjligt. Utöver kodgranskningar, designuppgifter och implementationsuppgifter bör teammedlemmar rådfråga ADR:er för strategiska beslut om produkten.

Som god praxis bör varje programvaruändring genomgå kollegagranskning och kräva minst ett godkännande. Under kodgranskningen kan en granskare hitta ändringar som strider mot en eller flera ADR:er. I så fall ber granskaren kodändringens författare att uppdatera koden och delar en länk till ADR:en. När författaren uppdaterar koden godkänns den av kollegagranskarna och slås samman med den huvudsakliga kodbasen.


## Process för granskning av ADR:er

Teamet bör behandla ADR:er som oföränderliga dokument efter att teamet godkänt eller avvisat dem. Ändringar i en befintlig ADR kräver att man skapar en ny ADR, upprättar en granskningsprocess för den nya ADR:en och godkänner ADR:en. Om teamet godkänner den nya ADR:en bör ägaren ändra den gamla ADR:ens tillstånd till **Superseded** (Ersatt). 
