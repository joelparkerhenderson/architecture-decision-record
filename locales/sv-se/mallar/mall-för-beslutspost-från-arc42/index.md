# Mall för beslutspost från arc42

<https://arc42.org/overview>

## 1. Introduktion och mål

Kort beskrivning av kraven, drivkrafterna, utdrag (eller sammandrag) av
kraven. De tre (högst fem) främsta kvalitetsmålen för arkitekturen som har
högst prioritet för de viktigaste intressenterna. En tabell över viktiga intressenter med
deras förväntningar på arkitekturen.

## 1.1 Kravöversikt

### Innehåll

Kort beskrivning av de funktionella kraven, drivkrafterna, utdrag (eller
sammandrag) av kraven. Länkar till de (förhoppningsvis befintliga) kravdokumenten, med information om var de finns. 

### Motivering

Ur slutanvändarnas perspektiv skapas eller ändras ett system för att
förbättra stödet för en affärsverksamhet och/eller förbättra kvaliteten. 

### Form

Kort textbeskrivning, förmodligen i tabellformat för användningsfall. Om kravdokument
finns bör den här översikten hänvisa till dessa dokument.

Håll dessa utdrag så korta som möjligt. Balansera det här dokumentets läsbarhet
mot potentiell redundans i förhållande till kravdokumenten. 

## 1.2 Kvalitetsmål

### Innehåll

De tre (högst fem) främsta kvalitetsmålen för arkitekturen vars uppfyllelse är av
högsta vikt för de viktigaste intressenterna. Vi menar verkligen kvalitetsmål
för arkitekturen. Blanda inte ihop dem med projektmål. De är inte
nödvändigtvis identiska. Standarden ISO 25010 ger en bra översikt över
potentiella ämnen av intresse.

### Motivering

Du bör känna till dina viktigaste intressenters kvalitetsmål, eftersom
de kommer att påverka grundläggande arkitekturbeslut. Var mycket
konkret om dessa kvaliteter och undvik modeord. Om du som arkitekt inte
vet hur kvaliteten på ditt arbete kommer att bedömas …

### Form

En tabell med de viktigaste kvalitetsmålen och konkreta scenarier, sorterad efter prioritet.

## 1.3 Intressenter

### Innehåll

Explicit översikt över systemets intressenter, det vill säga alla personer, roller eller
organisationer som

- bör känna till arkitekturen

- måste övertygas om arkitekturen

- måste arbeta med arkitekturen eller med koden

- behöver arkitekturdokumentationen för sitt arbete

- måste fatta beslut om systemet eller dess utveckling

### Motivering

Du bör känna till alla parter som är involverade i utvecklingen av systemet eller berörs av
systemet. Annars kan du få obehagliga överraskningar senare i
utvecklingsprocessen. Dessa intressenter avgör omfattningen och detaljnivån på ditt
arbete och dess resultat.

### Form

Tabell med rollnamn, personnamn och deras förväntningar på
arkitekturen och dess dokumentation.

## 2. Begränsningar

Allt som begränsar team i design- och implementationsbeslut eller beslut om
relaterade processer. Kan ibland gå utöver enskilda system och
gälla för hela organisationer och företag.

### Innehåll

Alla krav som begränsar programvaruarkitekters frihet i design- och
implementationsbeslut eller beslut om utvecklingsprocessen. Dessa
begränsningar går ibland utöver enskilda system och gäller för hela
organisationer och företag.

### Motivering

Arkitekter bör veta exakt var de är fria i sina designbeslut och
var de måste följa begränsningar. Begränsningar måste alltid hanteras;
de kan dock vara förhandlingsbara.

### Form

Enkla tabeller över begränsningar med förklaringar. Vid behov kan du dela upp dem
i tekniska begränsningar, organisatoriska och politiska begränsningar och
konventioner (t.ex. programmerings- eller versionshanteringsriktlinjer, dokumentations- eller namnkonventioner)

## 3. Kontext och avgränsning

Avgränsar ditt system från dess (externa) kommunikationspartner (angränsande
system och användare). Specificerar de externa gränssnitten. Visas ur ett
affärs-/domänperspektiv (alltid) eller ett tekniskt perspektiv (valfritt)

### Innehåll

Systemets avgränsning och kontext – som namnet antyder – avgränsar ditt system (dvs.
din avgränsning) från alla dess kommunikationspartner (angränsande system och användare,
dvs. ditt systems kontext). Den specificerar därmed de externa gränssnitten.

Om det behövs, skilj affärskontexten (domänspecifika indata och
utdata) från den tekniska kontexten (kanaler, protokoll, hårdvara).

### Motivering

Domängränssnitten och de tekniska gränssnitten till kommunikationspartner hör
till ditt systems mest kritiska aspekter. Se till att du förstår dem
fullständigt.

### Form

- Olika kontextdiagram

- Listor över kommunikationspartner och deras gränssnitt.

## 3.1 Affärskontext

### Innehåll

Specifikation av alla kommunikationspartner (användare, IT-system, …) med
förklaringar av domänspecifika indata och utdata eller gränssnitt. Valfritt kan du
lägga till domänspecifika format eller kommunikationsprotokoll.

### Motivering

Alla intressenter bör förstå vilka data som utbyts med systemets
omgivning.

### Form

Alla slags diagram som visar systemet som en svart låda och specificerar domän-
gränssnitten till kommunikationspartner.

Alternativt (eller dessutom) kan du använda en tabell. Tabellens titel är
ditt systems namn, de tre kolumnerna innehåller kommunikations-
partnerns namn, indata och utdata.

## 3.2 Teknisk kontext

### Innehåll

Tekniska gränssnitt (kanaler och överföringsmedier) som länkar ditt system till
dess omgivning. Dessutom en mappning av domänspecifika indata/utdata till
kanalerna, dvs. en förklaring av vilken indata/utdata som använder vilken kanal.

### Motivering

Många intressenter fattar arkitekturbeslut utifrån de tekniska gränssnitten
mellan systemet och dess kontext. Särskilt infrastruktur- eller hårdvaru-
designers bestämmer dessa tekniska gränssnitt.

### Form

T.ex. UML-distributionsdiagram som beskriver kanaler till angränsande system, tillsammans
med en mappningstabell som visar sambanden mellan kanaler och
indata/utdata.

## 4. Lösningsstrategi

Sammanfattning av de grundläggande besluten och lösningsstrategierna som formar
arkitekturen. Kan omfatta teknik, nedbrytning på toppnivå, tillvägagångssätt för att
uppnå de främsta kvalitetsmålen och relevanta organisatoriska beslut.

### Innehåll

En kort sammanfattning och förklaring av de grundläggande besluten och lösningsstrategierna som formar systemets arkitektur. Dessa omfattar

- tekniska beslut

- beslut om systemets nedbrytning på toppnivå, t.ex. användning av ett arkitekturmönster eller designmönster

- beslut om hur nyckelkvalitetsmål ska uppnås

- relevanta organisatoriska beslut, t.ex. val av utvecklingsprocess eller delegering av vissa uppgifter till tredje part.

### Motivering

Dessa beslut utgör hörnstenarna i din arkitektur. De är grunden
för många andra detaljerade beslut eller implementationsregler.

### Form

Håll förklaringen av dessa nyckelbeslut kort.

Motivera vad du har beslutat och varför du beslutade så, utifrån din
problemformulering, kvalitetsmålen och de viktigaste begränsningarna. Hänvisa till detaljer i
följande avsnitt (avsnitt 5 för strukturella detaljer, avsnitt 8 för
tvärgående koncept).

Du kan använda en lista över lösningsansatser eller en tabell.

## 5. Byggstensvy

Statisk nedbrytning av systemet, abstraktioner av källkoden, visad som
en hierarki av vita lådor (som innehåller svarta lådor), upp till lämplig detaljnivå.

### Innehåll

Byggstensvyn visar den statiska nedbrytningen av systemet i
byggstenar (moduler, komponenter, delsystem, klasser, gränssnitt, paket,
bibliotek, ramverk, lager, partitioner, nivåer, funktioner, makron, operationer,
datastrukturer, …) samt deras beroenden (relationer, associationer,
…)

Den här vyn är obligatorisk för all arkitekturdokumentation. I analogi med ett
hus är detta planritningen.

### Motivering

Behåll överblicken över din källkod genom att göra dess struktur begriplig
genom abstraktion.

Det gör att du kan kommunicera med dina intressenter på en abstrakt nivå
utan att avslöja implementationsdetaljer.

### Form

Byggstensvyn är en hierarkisk samling av svarta lådor och vita
lådor (se figuren nedan) och deras beskrivningar.

## 5.1 Vit låda för hela systemet

Här beskriver du nedbrytningen av hela systemet med hjälp av följande mall för vit låda. Den innehåller

- ett översiktsdiagram

- en motivering för nedbrytningen

- beskrivningar av svarta lådor för de ingående byggstenarna. För dessa erbjuder vi alternativ:

  - använd en tabell för en kort och pragmatisk översikt över alla ingående byggstenar och deras gränssnitt

  - använd en lista med beskrivningar av svarta lådor för byggstenarna enligt mallen för svart låda (se nedan). Beroende på ditt val av verktyg kan den här listan vara underkapitel (i textfiler), undersidor (i en wiki) eller kapslade element (i ett modelleringsverktyg).

  - (valfritt:) viktiga gränssnitt som inte förklaras i en byggstens mallar för svart låda, men som är mycket viktiga för att förstå den vita lådan.

Eftersom det finns så många sätt att specificera gränssnitt tillhandahåller vi ingen specifik mall för dem.

I bästa fall klarar du dig med exempel eller enkla signaturer.

## 5.2 Nivå 2

Här kan du specificera den inre strukturen hos (några) byggstenar från nivå 1
som vita lådor.

Du måste avgöra vilka byggstenar i ditt system som är tillräckligt viktiga för att
motivera en så detaljerad beskrivning. Föredra relevans framför fullständighet.
Specificera viktiga, överraskande, riskfyllda, komplexa eller föränderliga byggstenar. Utelämna
normala, enkla, tråkiga eller standardiserade delar av ditt system

### 5.2.1 Vit låda för byggsten 1

Specificerar den interna strukturen hos byggsten 1.

Använd mallen för vit låda (se ovan).

## 6. Körtidsvy

Byggstenarnas beteende som scenarier, som täcker viktiga användningsfall eller
funktioner, interaktioner vid kritiska externa gränssnitt, drift och
administration samt fel- och undantagsbeteende.

### Innehåll

Körtidsvyn beskriver konkret beteende och interaktioner hos systemets byggstenar i form av scenarier från följande områden:

- viktiga användningsfall eller funktioner: hur utför byggstenarna dem?

- interaktioner vid kritiska externa gränssnitt: hur samverkar byggstenarna med användare och angränsande system?

- drift och administration: start, uppstart, stopp

- fel- och undantagsscenarier

Anmärkning: Huvudkriteriet för valet av möjliga scenarier (sekvenser, arbetsflöden) är deras arkitektoniska relevans. Det är inte viktigt att beskriva ett stort antal scenarier. Dokumentera hellre ett representativt urval.

### Motivering

Du bör förstå hur (instanser av) byggstenar i ditt system utför sitt jobb och kommunicerar vid körning. Du kommer huvudsakligen att fånga scenarier i din dokumentation för att kommunicera din arkitektur till intressenter som är mindre villiga eller kapabla att läsa och förstå de statiska modellerna (byggstensvyn, distributionsvyn).

### Form

Det finns många notationer för att beskriva scenarier, t.ex.


- numrerad lista med steg (på naturligt språk)

- aktivitetsdiagram eller flödesscheman

- sekvensdiagram

- BPMN eller EPC:er (händelsestyrda processkedjor)

- tillståndsmaskiner

- osv.

## 6.n Körtidsscenario n (1, 2, 3 osv.)

Infoga körtidsdiagram eller textbeskrivning av scenariot.

Infoga beskrivning av de anmärkningsvärda aspekterna av interaktionerna mellan de byggstensinstanser som visas i det här diagrammet.

## 7. Distributionsvy

Teknisk infrastruktur med miljöer, datorer, processorer, topologier.
Mappning av (programvaru)byggstenar till infrastrukturelement.

### Innehåll

Distributionsvyn beskriver:

- den tekniska infrastrukturen som används för att köra ditt system, med infrastruktur-
  element som geografiska platser, miljöer, datorer, processorer,
  kanaler och nättopologier samt andra infrastrukturelement och

- mappningen av (programvaru)byggstenar till dessa infrastrukturelement.

Ofta körs system i olika miljöer, t.ex. utvecklings-
miljö, testmiljö, produktionsmiljö. I sådana fall bör du
dokumentera alla relevanta miljöer.

Dokumentera särskilt distributionsvyn när din programvara körs som
distribuerat system med mer än en dator, processor, server eller container
eller när du designar och konstruerar egna hårdvaruprocessorer och chip.

Ur ett programvaruperspektiv räcker det att fånga de element i
infrastrukturen som behövs för att visa distributionen av dina byggstenar.
Hårdvaruarkitekter kan gå längre och beskriva infrastrukturen till vilken
detaljnivå de än behöver fånga. 

### Motivering

Programvara körs inte utan hårdvara. Den här underliggande infrastrukturen kan och
kommer att påverka ditt system och/eller vissa tvärgående koncept. Därför
måste du känna till infrastrukturen.

### Form

Kanske finns distributionsdiagrammet på högsta nivå redan i avsnitt 3.2 som teknisk kontext med din egen infrastruktur som EN svart låda. I det här avsnittet zoomar du in på den svarta lådan med hjälp av ytterligare distributionsdiagram.

- UML erbjuder distributionsdiagram för att uttrycka den vyn. Använd det, kanske med kapslade diagram, när din infrastruktur är mer komplex.

- När dina (hårdvaru)intressenter föredrar andra typer av diagram framför
  UML-distributionsdiagram, låt dem använda vilken typ som helst som kan visa noder och
  kanaler i infrastrukturen.

## 7.1 Infrastruktur nivå 1

Beskriv (vanligtvis i en kombination av diagram, tabeller och text):

- distributionen av ditt system till flera platser, miljöer, datorer, processorer, .. samt de fysiska anslutningarna mellan dem

- viktig motivering eller bakgrund till den här distributionsstrukturen

- kvalitets- och/eller prestandaegenskaper hos infrastrukturen

- mappningen av programvaruartefakter (byggstenar) till infrastrukturens element

För flera miljöer eller alternativa distributioner, kopiera det avsnittet i arc42 för alla relevanta miljöer. **

## 7.2 Infrastruktur nivå 2

Här kan du inkludera den inre strukturen hos (några) infrastrukturelement från infrastruktur nivå 1.

Kopiera strukturen från nivå 1 för varje valt element.

## 8. Tvärgående koncept

Övergripande, principiella regleringar och lösningsansatser som är relevanta i flera
delar (→ tvärgående) av systemet. Koncept hänger ofta samman med flera
byggstenar. Inkludera olika ämnen som domänmodeller, arkitektur-
mönster och -stilar, regler för att använda specifik teknik och implementations-
regler.

### Innehåll

Det här avsnittet beskriver tvärgående koncept (metoder, mönster, regleringar
eller lösningsidéer). Sådana koncept hänger ofta samman med flera byggstenar.
De kan omfatta många olika ämnen.

### Motivering

Koncept utgör grunden för arkitekturens konceptuella integritet (konsekvens, homogenitet). De är
alltså ett viktigt bidrag för att uppnå systemets inre
kvaliteter.

Det här är platsen i mallen som vi har avsatt för en sammanhängande specifikation
av sådana koncept.

Många av dessa koncept hänger samman med eller påverkar flera av dina byggstenar.

### Form

Formen kan variera:

- konceptpapper med valfri struktur

- exempelimplementationer, särskilt för tekniska koncept

- tvärgående modellutdrag eller scenarier med notation från arkitekturvyerna

### Det här avsnittets struktur

Välj bara de ämnen som behövs mest för ditt system och tilldela var och en en nivå 2-rubrik i det här avsnittet (t.ex. 8.1, 8.2 osv).

- FÖRSÖK INTE täcka alla ämnen i det ovan nämnda diagrammet.

### Bakgrund

Vissa ämnen inom system rör ofta flera byggstenar, hårdvaru-
element eller utvecklingsprocesser. Det kan vara enklare att kommunicera eller dokumentera
sådana tvärgående ämnen på en central plats, i stället för att upprepa dem i
beskrivningen av de berörda byggstenarna, hårdvaruelementen eller
utvecklingsprocesserna.

Vissa koncept kan beröra alla element i ett system, andra kan bara vara
relevanta för några få.

## 9. Arkitekturbeslut

Viktiga, dyra, kritiska, storskaliga eller riskfyllda arkitekturbeslut
inklusive motiveringar.

### Innehåll

Viktiga, dyra, storskaliga eller riskfyllda arkitekturbeslut inklusive
motiveringar. Med ”beslut” menar vi att välja ett alternativ utifrån givna
kriterier.

Använd ditt omdöme för att avgöra om ett arkitekturbeslut bör
dokumenteras här i det här centrala avsnittet eller om du hellre dokumenterar det
lokalt (t.ex. inom mallen för vit låda för en byggsten). Undvik
redundanta texter. Hänvisa till avsnitt 4, där du redan fångat de viktigaste
besluten i din arkitektur.

### Motivering

Intressenter i ditt system bör kunna förstå och spåra dina
beslut.

### Form

- ADR (arkitekturbeslutspost) för varje viktigt beslut

- lista eller tabell, ordnad efter vikt och konsekvenser eller

- mer detaljerat i form av separata avsnitt per beslut

### Bakgrund (om ADR:er)

Mindre dokumentationsbitar är lättare att läsa, skapa och underhålla. När det
gäller arkitekturbeslut kommer utvecklingsteam ofta att:

- känna till beslutet, eftersom det syns t.ex. i källkoden, men

- sakna motiveringen bakom det beslutet (se Nygard 2011)

Därför bör du dokumentera några viktiga beslut tillsammans med deras
motivering och resonemang

### Vårt förslag gällande beslut

För en samling arkitektoniskt betydelsefulla beslut, dvs. beslut som
påverkar struktur, kvalitetsegenskaper, viktiga (särskilt externa)
beroenden och gränssnitt eller konstruktionstekniker (tack till Michael
Nygard för det här förslaget).

## 10. Kvalitetskrav

Kvalitetskrav som scenarier, med ett kvalitetsträd för att ge en överblick
på hög nivå. De viktigaste kvalitetsmålen borde ha beskrivits i avsnitt
1.2. (kvalitetsmål).

### Innehåll

Det här avsnittet innehåller alla relevanta kvalitetskrav.

De viktigaste av dessa krav har redan beskrivits i avsnitt
1.2. (kvalitetsmål), därför bör de bara hänvisas till här. I det här
avsnitt 10 bör du också fånga kvalitetskrav av mindre vikt,
som inte skapar höga risker om de inte uppnås fullt ut (men som kanske
är trevliga att ha).

### Motivering

Eftersom kvalitetskrav kommer att ha stort inflytande på arkitektur-
beslut bör du veta vilka kvaliteter som verkligen är viktiga för
dina intressenter, på ett specifikt och mätbart sätt.

### Mer information

Se den omfattande kvalitetsmodellen Q42 på https://quality.arc42.org.

## 10.1 Översikt över kvalitetskrav

### Innehåll

En översikt eller sammanfattning av kvalitetskrav.

### Motivering

Ofta möter vi dussintals (eller till och med hundratals) detaljerade kvalitetskrav.
I det här översiktsavsnittet bör du försöka sammanfatta, t.ex. genom att beskriva
kategorier eller ämnen (som föreslås av ISO 25010:2023 eller Q42

Om dessa sammanfattande beskrivningar redan är precisa, tillräckligt specifika och
mätbara kan du hoppa över avsnitt 10.2.

### Form

Använd en enkel tabell där varje rad innehåller en kategori eller ett ämne och en kort
beskrivning av kvalitetskravet. Alternativt kan du använda en tankekarta för att
strukturera dessa kvalitetskrav.

I litteraturen har även idén om ett kvalitetsattributträd beskrivits,
som sätter den generiska termen ”kvalitet” som rot och använder en trädliknande
förfining av termen ”kvalitet”. [Bass+21] introducerade termen ”Quality
Attribute Utility Tree” för detta ändamål.

## 10.2 Kvalitetsscenarier

### Innehåll

Kvalitetsscenarier gör kvalitetskrav konkreta och gör det möjligt att avgöra om
de är uppfyllda (i betydelsen godkännandekriterier). Se till att dina
scenarier är specifika och mätbara.

Två typer av scenarier är särskilt användbara:

- Användningsscenarier (även kallade tillämpningsscenarier eller användningsfallsscenarier)
  beskriver systemets körtidsreaktion på en viss stimulans. Detta
  omfattar även scenarier som beskriver systemets effektivitet eller prestanda.
  Exempel: Systemet reagerar på en användares begäran inom en sekund.

- Ändringsscenarier beskriver den önskade effekten av en modifiering eller utvidgning av
  systemet eller dess närmaste omgivning. Exempel: Ytterligare funktionalitet
  implementeras eller krav på ett kvalitetsattribut ändras, och insatsen eller
  varaktigheten för ändringen mäts.

### Form

Typisk information för detaljerade scenarier omfattar följande:

I kortform (föredras i Q42-modellen):

- Kontext/Bakgrund: Vilken typ av system eller komponent, vad är miljön eller situationen?

- Källa/Stimulans: Vem eller vad som initierar eller utlöser ett beteende, en reaktion eller en handling.

- Mått/Godkännandekriterium: Ett svar inklusive ett mått eller en metrik

Den långa formen av scenarier (föredras av SEI och [Bass+21]) är mer detaljerad och omfattar följande information:

- Scenario-ID: En unik identifierare för scenariot.

- Scenarionamn: Ett kort, beskrivande namn för scenariot.

- Källa: Entiteten (användare, system eller händelse) som initierar scenariot.

- Stimulans: Den utlösande händelsen eller det tillstånd som systemet måste hantera.

- Miljö: Det operativa sammanhang eller tillstånd under vilket systemet upplever stimulansen.

- Artefakt: Byggstenarna eller andra element i systemet som påverkas av stimulansen.

- Svar: Det utfall eller beteende som systemet uppvisar som reaktion på stimulansen.

- Svarsmått: Kriteriet eller metriken som systemets svar utvärderas efter.

### Se även

Sedan januari 2023 tillhandahåller arc42 en pragmatisk kvalitetsmodell som föreslår att
kvalitetskrav märks med hashtaggar eller etiketter som #flexible, #efficient,
#usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Risker och teknisk skuld

Kända tekniska risker eller teknisk skuld. Vilka potentiella problem finns inom eller
kring systemet? Vad känner utvecklingsteamet sig olyckligt över?

### Innehåll

En lista över identifierade tekniska risker eller tekniska skulder, ordnad efter prioritet

### Motivering

”Riskhantering är projektledning för vuxna” (Tim Lister, Atlantic
Systems Guild.)

Det här bör vara ditt motto för systematisk upptäckt och utvärdering av risker och
tekniska skulder i arkitekturen, vilket kommer att behövas av ledningens
intressenter (t.ex. projektledare, produktägare) som en del av den övergripande risk-
analysen och åtgärdsplaneringen.

### Form

Lista över risker och/eller tekniska skulder, troligen med föreslagna åtgärder för att
minimera, mildra eller undvika risker eller minska tekniska skulder.

