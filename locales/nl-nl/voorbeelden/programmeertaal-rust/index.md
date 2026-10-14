# Architectuurbeslissingsdocument: programmeertaal Rust

Beslissingsnummer: AR-001

Titel van de beslissing: Invoering van de programmeertaal Rust

Datum: 1 december 2021

Status: Geaccepteerd

### Probleemstelling

Naarmate we softwareapplicaties blijven ontwikkelen, hebben we waargenomen dat het steeds uitdagender wordt potentiële beveiligingskwetsbaarheden te mitigeren en runtimefouten te voorkomen. Met de bestaande programmeertalen, zoals C en C++, blijven we problemen ervaren zoals bufferoverflows, geheugenlekken en ongedefinieerd gedrag dat tot crashes van applicaties leidt. We hebben een programmeertaal nodig die garanties voor geheugenveiligheid biedt en efficiënt genoeg is om prestatiekritieke applicaties te ondersteunen.

### Overwegingen

Verschillende programmeertalen zijn ontworpen om de bestaande problemen aan te pakken. Daaronder heeft de programmeertaal Rust vanwege zijn unieke ontwerpkenmerken aanzienlijke aandacht gekregen van de ontwikkelaarsgemeenschap. Overwegingen zijn onder meer;

1. Geheugenveiligheid en beveiliging

2. Prestaties en efficiëntie

3. Ondersteuning en adoptie door de gemeenschap

4. Leercurve

5. Tools en ecosysteem

6. Compatibiliteit met bestaande softwaresystemen.

### Beperkingen

Het invoeren van een nieuwe programmeertaal vereist het omscholen van ontwikkelaars, wat tijd en middelen kost. Het integreren van de taal in de bestaande ontwikkelwerkstroom kan een uitdaging zijn. We moeten compatibiliteit met de bestaande systemen waarborgen en brekende wijzigingen vermijden om continuïteit te behouden.

### Implementatie

1. Ons ontwikkelteam volgt training om de programmeertaal Rust te leren en zich eigen te maken.

2. We maken op proefbasis een nieuw project met Rust om de compatibiliteit en geschiktheid voor onze ontwikkeldoeleinden te evalueren.

3. We migreren bestaande systemen die in C en C++ zijn geschreven geleidelijk naar Rust.

4. We werken samen met de Rust-gemeenschap om de beschikbare tools en bibliotheken te verkennen die onze ontwikkelwerkstroom kunnen verbeteren.

5. We monitoren de prestaties van Rust en vergelijken die regelmatig met de prestaties van de bestaande programmeertalen.

6. We hanteren een langetermijnaanpak die de kosten van training en integratie afweegt tegen de mogelijke voordelen van het gebruik van Rust.

### Onderbouwing

We hebben Rust ingevoerd vanwege de unieke functies die zijn ontworpen om garanties voor geheugenveiligheid en beveiliging te bieden met behoud van prestaties en efficiëntie. Het robuuste typesysteem, de borrow checker en de concepten voor geheugenveiligheid van Rust maken het zeer geschikt voor het ontwikkelen van prestatiekritieke en veiligheidskritieke applicaties. Bovendien heeft Rust een aanzienlijke gemeenschap van ontwikkelaars, waardoor we toegang hebben tot een breed scala aan tools, bibliotheken en ecosysteem die onze ontwikkelwerkstroom ondersteunen. Hoewel Rust een leercurve heeft, geloven we dat de voordelen van het invoeren van Rust zwaarder wegen dan de kosten en een uitstekende kans bieden voor voortdurende groei en innovatie.

### Gevolgen

1. De invoering van Rust vereist een aanzienlijke investering in tijd en middelen om ontwikkelaars te trainen en de taal in de bestaande ontwikkelwerkstroom te integreren.

2. Het invoeren van Rust kan enige mate van compatibiliteitsproblemen met bestaande systemen veroorzaken, wat refactoring en aanpassingen vereist.

3. De invoering van Rust kan het aantal ontwikkelaars vergroten dat aan ons project kan bijdragen door Rust-ontwikkelaars aan te trekken die aan spannende projecten willen werken.

4. De invoering kan leiden tot betere prestaties, efficiëntie en veiligheid vergeleken met de bestaande talen.

5. Ten slotte biedt het invoeren van Rust het mogelijke voordeel dat beveiligingskwetsbaarheden in onze applicaties afnemen.
   
<h6>Bronvermelding: deze pagina is gegenereerd door ChatGPT en daarna bewerkt voor duidelijkheid en opmaak.</h6>
