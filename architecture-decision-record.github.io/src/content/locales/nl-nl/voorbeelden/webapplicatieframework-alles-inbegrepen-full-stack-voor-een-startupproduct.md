# Architectuurbeslissingsdocument: webapplicatieframework, alles inbegrepen (batteries included), full stack, voor een startupproduct

<!-- 

ChatGPT prompt

Long software architecture decision record 
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports. 

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Primair doel:**  
Een webapplicatie bouwen waarmee betalende klanten kunnen inloggen, bestanden kunnen uploaden, data kunnen verwerken en rapporten kunnen bekijken, met focus op agile ontwikkeling, full-stackfunctionaliteit en sterke compatibiliteit met AI/ML-tools, met name Project Jupyter-notebooks.

### Context en eisen:

1. **Agile ontwikkeling (hoge prioriteit)**: als startup hebben we snelle iteratie en flexibiliteit nodig. Agile methoden, zoals snelle prototyping, iteratieve ontwikkeling en aanpasbaarheid aan verandering, zijn essentieel voor onze ontwikkelcyclus.

2. **Full-stackframework (hoge prioriteit)**: we willen de overhead minimaliseren door een framework te kiezen dat zowel backend als frontend effectief kan afhandelen, waardoor de behoefte aan afzonderlijke frontend-frameworks afneemt.

3. **Compatibiliteit met AI/ML-tools (hoge prioriteit)**: het kunnen eenvoudig integreren met data-analysetools zoals Jupyter-notebooks en het datawetenschapsecosysteem van Python (NumPy, Pandas, TensorFlow enz.) is cruciaal. Dit zou efficiënte dataverwerking en rapportage vergemakkelijken.

4. **Criteria met lage prioriteit**:
   - **Runtimesnelheid**: hoewel prestaties relevant zijn, is het in het begin niet de meest kritieke factor, omdat we ons meer zorgen maken over ontwikkelsnelheid en het afronden van functies.
   - **Schaalbaarheid**: we verwachten groei, maar schaalbaarheidskwesties kunnen later worden aangepakt en zijn nu geen primaire eis.
   - **Achterwaartse compatibiliteit**: we richten ons op huidige technologieën en maken ons niet bijzonder zorgen over achterwaartse compatibiliteit met oudere systemen.

### Geëvalueerde frameworks:

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Overzicht**:  
Django is een webframework op hoog niveau voor Python dat snelle ontwikkeling en een schoon, pragmatisch ontwerp bevordert. Het staat bekend om zijn filosofie van "batteries included", wat betekent dat het veel functies zoals authenticatie, routing, ORM en formulierverwerking standaard bevat.

**Sterke punten**:  
- **Full stack**: Django is een uitgebreid full-stackframework dat zowel backend- als frontendbehoeften kan afhandelen met geïntegreerde functies (bijv. templating-engine, beheerinterface).
- **Agile ontwikkeling**: de goed gedefinieerde structuur en conventies van Django maken snelle ontwikkeling en aanpasbaarheid mogelijk, essentieel voor een startupomgeving. Het framework wordt geleverd met uitstekende documentatie en een rijk ecosysteem van pakketten van derden, wat de ontwikkeling versnelt.
- **AI/ML-integratie**: het ecosysteem van Python is ongeëvenaard voor datawetenschap en machine learning. Django, dat op Python is gebaseerd, integreert naadloos met tools als Jupyter-notebooks, Pandas, NumPy, TensorFlow en scikit-learn.
- **Gemeenschap en ecosysteem**: Django heeft een uitgebreide gemeenschap, robuuste documentatie en een breed scala aan plug-ins en extensies, wat ontwikkeling en debugging aanzienlijk versnelt.
  
**Zwakke punten**:  
- **Runtimesnelheid**: Python is doorgaans langzamer dan talen als Rust of Elixir. Voor dit gebruiksscenario, waar prestaties niet de primaire zorg zijn, hoeft dat echter niet doorslaggevend te zijn.
- **Schaalbaarheid**: hoewel Django zeer schaalbaar is, kunnen er bij zeer hoge schaal zonder zorgvuldige optimalisatie uitdagingen zijn (bijv. bij het verwerken van zware gelijktijdige verzoeken). Django kan echter nog steeds effectief schalen met load balancing en cachingtechnieken.

**Oordeel**:  
Django sluit goed aan bij de eisen voor agile ontwikkeling, full-stackondersteuning en AI/ML-compatibiliteit. De Python-integratie biedt naadloze toegang tot de datawetenschapstools en -bibliotheken die nodig zijn voor de applicatie.

---

### 2. **Ruby on Rails (Ruby)**

**Overzicht**:  
Ruby on Rails (RoR) is een volwassen full-stackframework voor webapplicaties, bekend om zijn aanpak van "conventie boven configuratie", wat snelle ontwikkeling vergemakkelijkt.

**Sterke punten**:  
- **Full stack**: RoR wordt geleverd met ingebouwde tools voor zowel backend- als frontendontwikkeling (bijv. views, templates, scaffolding), en de rijke bibliotheek van gems maakt het mogelijk snel verschillende functies te implementeren.
- **Agile ontwikkeling**: Ruby on Rails staat vooral bekend om zijn snelle iteratiecycli, wat gunstig is voor startups die snel op functies willen itereren. RoR ondersteunt test-driven development (TDD) en heeft een gevestigd ecosysteem voor agile werkstromen.
- **Gemeenschap en ecosysteem**: RoR heeft een gevestigde, sterke gemeenschap en een breed scala aan gems die de ontwikkeling kunnen versnellen.
- **Gebruiksgemak**: Rails heeft een zeer ontwikkelaarsvriendelijke syntaxis en staat bekend om het snel en eenvoudig maken van taken zoals databasemigraties, de Model-View-Controller (MVC)-architectuur en routebeheer.

**Zwakke punten**:  
- **Prestaties**: Ruby heeft doorgaans tragere runtimeprestaties dan Python of Elixir. Hoewel RoR met de juiste infrastructuur kan schalen, kunnen de prestaties van Ruby een knelpunt worden voor applicaties die zware realtimeverwerking of hoog gelijktijdig verkeer vereisen.
- **AI/ML-integratie**: hoewel Ruby enkele bibliotheken voor machine learning heeft, wordt het in de AI/ML-gemeenschap niet zo breed toegepast als Python. Integratie met tools als Jupyter-notebooks is minder naadloos, waardoor Python een sterkere keuze is voor datazware applicaties.
  
**Oordeel**:  
Hoewel Ruby on Rails uitblinkt in agile ontwikkeling en snelle prototyping, schiet het tekort op AI/ML-compatibiliteit vergeleken met Python (Django). Het is een haalbare keuze voor startups die snelle iteratie boven diepe integratie van data-analyse stellen.

---

### 3. **Phoenix (Elixir)**

**Overzicht**:  
Phoenix is een webframework gebouwd met Elixir, een functionele programmeertaal ontworpen voor schaalbaarheid en concurrency. Phoenix maakt gebruik van de Erlang VM, die bekendstaat om het verwerken van enorme concurrency en fouttolerante systemen.

**Sterke punten**:  
- **Schaalbaarheid en prestaties**: Phoenix schittert in schaalbaarheid en het verwerken van hoge concurrency. Het is gebouwd op de Erlang VM, die duizenden (of zelfs miljoenen) gelijktijdige verbindingen kan ondersteunen, waardoor het een sterke kandidaat is voor applicaties die realtimedataverwerking of verkeer met hoog volume vereisen.
- **Full stack**: Phoenix bevat alles wat nodig is om zowel backend als frontend van een applicatie te bouwen. Het ondersteunt live views voor interactieve UI-updates en bevat een templating-engine.
- **Agile ontwikkeling**: Phoenix is zeer modulair, wat snelle iteratie op functies mogelijk maakt. Het past goed bij startups die snel moeten bewegen.
- **AI/ML-compatibiliteit**: hoewel Elixir opkomende bibliotheken voor machine learning heeft, wordt het niet zo breed ondersteund voor AI/ML-taken als Python. Integratie met tools als Jupyter-notebooks zou omwegen vereisen, omdat het datawetenschapsecosysteem van Elixir niet zo volwassen is als dat van Python.

**Zwakke punten**:  
- **AI/ML-ecosysteem**: Elixir is niet de primaire taal voor datawetenschap of machine learning en het ecosysteem is niet zo volwassen als dat van Python. Daardoor wordt integratie met tools als Jupyter-notebooks of populaire AI-bibliotheken (TensorFlow, PyTorch) lastig.
- **Leercurve**: als het team niet bekend is met functioneel programmeren en Elixir, kan er een steilere leercurve zijn.

**Oordeel**:  
Phoenix is een uitstekende keuze als schaalbaarheid en concurrency een primaire zorg zijn. Gezien de prioriteit van AI/ML-compatibiliteit is Phoenix echter mogelijk niet de beste match vanwege het beperkte ecosysteem van Elixir op dit gebied.

---

### 4. **Loco (Rust)**

**Overzicht**:  
Loco is een webframework gebouwd met Rust, een systeemprogrammeertaal die bekendstaat om prestaties, geheugenveiligheid en concurrency. Rust wordt steeds populairder voor het bouwen van hoogpresterende applicaties.

**Sterke punten**:  
- **Prestaties**: de belangrijkste kracht van Rust ligt in zijn hoge prestaties en geheugenveiligheid, wat het een uitstekende keuze maakt voor applicaties die controle op laag niveau of extreem hoge prestaties vereisen.
- **Concurrency**: het eigendomssysteem (ownership) van Rust garandeert geheugenveiligheid en staat veilig gelijktijdig programmeren toe, wat het ideaal maakt voor systemen die efficiënt moeten schalen en parallellisme moeten verwerken.

**Zwakke punten**:  
- **Full-stackontwikkeling**: Loco is, hoewel veelbelovend, niet zo volwassen als de andere frameworks wat betreft het bieden van een complete full-stackoplossing. Het is beter geschikt voor backendontwikkeling, en het frontend-ecosysteem rond Rust is nog in opkomst.
- **Agile ontwikkeling**: ontwikkeling met Rust kan langzamer zijn dan met talen op hoog niveau zoals Python of Ruby vanwege het lagere niveau en de steilere leercurve.
- **AI/ML-ecosysteem**: Rust heeft niet hetzelfde uitgebreide AI/ML-ecosysteem als Python. Hoewel er groeiende bibliotheken in Rust zijn voor numeriek rekenen, zijn deze veel minder volwassen dan het aanbod van Python, zoals Jupyter-notebooks of machine-learningframeworks.
  
**Oordeel**:  
Hoewel Rust en het framework Loco uitzonderlijke prestaties bieden, maken het gebrek aan full-stackondersteuning, voordelen voor agile ontwikkeling en AI/ML-ecosysteem het minder ideaal voor dit specifieke gebruiksscenario. Het is beter geschikt voor prestatiekritieke applicaties dan voor snelle webontwikkeling met geïntegreerde datawetenschapstools.

---

### Conclusie

Na het evalueren van de opties op basis van de projecteisen is **Django (Python)** de meest geschikte keuze. Het biedt de volgende voordelen:

- **Full-stackmogelijkheden**: Django is een full-stackframework dat backend- en frontendontwikkeling integreert.
- **Agile ontwikkeling**: het framework is zeer geschikt voor snelle prototyping en iteratie, wat cruciaal is in een startupomgeving.
- **AI/ML-compatibiliteit**: Python is de toonaangevende taal voor AI/ML, en de compatibiliteit van Django met bibliotheken als Jupyter-notebooks zorgt voor soepele integratie voor data-analyse en dataverwerking.
- **Gemeenschap en ecosysteem**: de sterke ondersteuning door de gemeenschap en het uitgebreide ecosysteem van bibliotheken van Django bieden talloze tools om de ontwikkeling te versnellen.

Hoewel **Ruby on Rails** ook een sterke kandidaat is voor agile ontwikkeling, maakt de beperkte AI/ML-ondersteuning het minder ideaal voor dit specifieke gebruiksscenario. **Phoenix (Elixir)** en **Loco (Rust)**, die uitblinken in schaalbaarheid en prestaties, schieten tekort op AI/ML-integratie en full-stackontwikkeling. Daarom is Django het aanbevolen framework voor dit project.
