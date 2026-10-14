## Architectuurbeslissingsdocument: framework voor browserautomatisering bij E2E-testen (Playwright of Selenium)

### 1. **Context**

We zijn bezig een framework voor browserautomatisering te selecteren voor onze pijplijn voor end-to-end (E2E) testen. Dit framework wordt een integraal onderdeel van onze CI/CD-processen en voert tests uit die echte gebruikersinteracties op ons platform simuleren. De tests dekken met name scenario's zoals gebruikersregistratie/inloggen, bestandsuploads, dashboardinteracties en het downloaden van rapporten.

Als **startup** ligt onze focus op **agile ontwikkeling**, met de behoefte om snel te itereren en te evolueren. Ons team werkt voornamelijk met **TypeScript** en **Python**, en het kunnen schrijven van tests in deze talen is essentieel. Bovendien bevat het platform **interactieve grafieken en dashboards**, waardoor het cruciaal is dat de automatiseringstool rijke, dynamische UI's goed ondersteunt.

De twee kandidaten voor deze taak zijn **Playwright** en **Selenium**, elk met zijn sterke punten en afwegingen. We moeten deze frameworks evalueren op basis van de onderstaande functies en eisen.

### 2. **Overwogen opties**

- **Playwright** (door Microsoft)
- **Selenium** (door het Selenium Project)

### 3. **Beslissingsdrijfveren**

De factoren die onze beslissing beïnvloeden zijn de volgende:

1. **Agile ontwikkeling**: de gekozen tool moet snelle, flexibele ontwikkelcycli mogelijk maken.
2. **Taalondersteuning**: ons team heeft ondersteuning nodig voor zowel **TypeScript** als **Python**.
3. **Testen van interactieve UI's**: het betrouwbaar kunnen testen van interactieve grafieken, dashboards en dynamische elementen is essentieel.
4. **Runtimesnelheid**: hoewel geen primaire zorg, is prestatie in CI/CD-pijplijnen een overweging.
5. **Schaalbaarheid**: we plannen op korte termijn geen enorme schaalvergroting, maar we willen ervoor zorgen dat de oplossing toekomstige groei aankan.
6. **Achterwaartse compatibiliteit**: legacysystemen en compatibiliteit met oudere browsers zijn op dit moment niet kritiek voor ons project.
7. **Mobiel testen**: hoewel geen onmiddellijke focus, moet het framework mobiel responsieve functies kunnen testen of uitbreidbaar zijn voor dergelijke gebruiksscenario's.
8. **Testen met meerdere schermen**: ondersteuning voor opstellingen met meerdere schermen is een secundaire eis, vooral als we later opschalen naar het testen van complexere gebruikerswerkstromen.
9. **Testen van bestandsuploads**: het framework moet bestandsuploads, een kernvereiste van onze testbehoeften, efficiënt kunnen afhandelen.

### 4. **Evaluatiecriteria**

- **Gebruiksgemak**: hoe gemakkelijk is het tests te schrijven en te onderhouden?
- **Taalondersteuning**: ondersteunt het framework TypeScript en Python, de twee talen die ons team het meest gebruikt?
- **Testen van interactieve UI's**: hoe goed gaat het framework om met complexe, interactieve gebruikersinterfaces zoals grafieken, bestandsuploads en dynamische data?
- **CI/CD-integratie**: hoe goed integreert het framework met gangbare CI/CD-tools en -diensten?
- **Ondersteuning voor meerdere browsers**: welke browsers worden ondersteund en hoe goed presteren ze?
- **Prestaties en snelheid**: hoe snel draaien de tests, vooral in een CI/CD-pijplijn?
- **Schaalbaarheid**: hoe goed kan het framework schalen als er meer tests of complexere scenario's worden toegevoegd?
- **Gemeenschap en ecosysteem**: hoe actief is de gemeenschap van het framework? Zijn er volop integraties en plug-ins?

### 5. **Overwegingen**

#### 5.1 **Playwright**

##### **Voordelen**:
1. **Slimmere API voor het uploaden van lokale bestanden**: de API van Playwright voor interactie met lokale bestanden en het uitvoeren van bestandsuploads is eenvoudiger en intuïtiever. Dat maakt tests van bestandsuploads gemakkelijker te implementeren en te onderhouden.
2. **Syntaxis en codegeneratie**: Playwright heeft een kortere, beknoptere syntaxis. Dat geeft minder boilerplate, wat de onderhoudbaarheid en efficiëntie van ontwikkelaars verbetert. Bovendien verbetert de kortere syntaxis de kwaliteit van OpenAI-codegeneratie, waardoor het gemakkelijker wordt testscripts automatisch te genereren.
3. **Testen van interactieve UI's**: Playwright blinkt uit in het testen van dynamische, interactieve webapplicaties, bijvoorbeeld met rijke grafieken, complexe gebruikersinteracties en realtime-updates. Het verwerkt WebSockets, WebRTC, shadow DOM en andere moderne webtechnologieën zeer effectief.
4. **Ondersteuning voor meerdere browsers**: Playwright ondersteunt **Chromium**, **WebKit** en **Firefox**. Het heeft consistente prestaties over deze browsers, wat de meeste van onze testbehoeften zou moeten dekken.
5. **CI/CD-integratie**: Playwright integreert naadloos met moderne CI/CD-platforms (GitHub Actions, Jenkins enz.). Het kan tests parallel uitvoeren over verschillende browsers, wat de testuitvoeringstijden optimaliseert en het geschikt maakt voor snelle ontwikkeling.
6. **Snel en betrouwbaar**: Playwright is over het algemeen sneller dan Selenium, vooral in headless-modus, en veerkrachtiger bij asynchrone webelementen.

##### **Nadelen**:
1. **Beperkt mobiel testen**: hoewel Playwright mobiele emulatie voor browsers ondersteunt, mist het ingebouwde mobiele testmogelijkheden zoals de integratie van Selenium met Appium voor echt mobiel testen.
2. **Kleiner ecosysteem**: Playwright is nog nieuwer en minder gevestigd dan Selenium. Hoewel het een snelgroeiende gemeenschap en goede documentatie heeft, heeft het misschien nog niet het grote ecosysteem van plug-ins en integraties dat Selenium biedt.
3. **Beperkte browserondersteuning**: hoewel Playwright de grote moderne browsers dekt (Chrome, Safari, Firefox), is de ondersteuning voor oudere browsers (bijv. Internet Explorer) niet zo robuust als die van Selenium.

#### 5.2 **Selenium**

##### **Voordelen**:
1. **Langere geschiedenis en volwassenheid**: Selenium bestaat al lang en heeft een bewezen staat van dienst. Het wordt breed gebruikt door veel teams en branches, wat heeft geleid tot een groot ecosysteem van plug-ins, integraties en middelen.
2. **Ondersteuning voor meerdere browsers en platforms**: Selenium ondersteunt een **breed scala aan browsers** en versies, waaronder **Internet Explorer**, en kan ook worden geïntegreerd met verschillende tools zoals **Docker**, **Selenium Grid** en **clouddiensten** voor gedistribueerd testen.
3. **Mobiel testen**: Selenium is, via de integratie met **Appium**, veel robuuster voor mobiel testen, inclusief zowel Android- als iOS-applicaties. Dat maakt het de betere keuze voor projecten met een mobile-first of sterk mobiele focus.
4. **Testen met meerdere schermen**: Selenium biedt betere ondersteuning voor scenario's met **meerdere schermen** of complexe interacties met meerdere vensters.

##### **Nadelen**:
1. **Complexiteit**: de API van Selenium is uitgebreider en explicieter. Hoewel dat in sommige gevallen een voordeel kan zijn, betekent het meer code om te schrijven en te onderhouden, wat de wendbaarheid van ontwikkelaars kan verminderen, vooral belangrijk in een startupomgeving.
2. **Prestaties**: Selenium draait over het algemeen langzamer dan Playwright, vooral in headless-modus. Dat kan CI/CD-pijplijnen beïnvloeden, zeker naarmate het aantal tests groeit.
3. **Testen van interactieve UI's**: Selenium is minder soepel dan Playwright bij het testen van moderne, interactieve web-UI's, vooral met grafieken en realtime data-updates. Het vereist meer configuratie en afhandeling om betrouwbaar met dynamische inhoud te communiceren.

### 6. **Samenvatting van de vergelijking**

| Functie                           | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Gebruiksgemak**                 | Kortere syntaxis, intuïtiever voor moderne UI's | Explicieter, vereist meer boilerplate  |
| **Taalondersteuning**             | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Testen van interactieve UI's**  | Uitstekend voor dynamische realtime-UI's      | Verwerkt basis-UI's, maar uitgebreider en complexer voor rijke interacties |
| **Testen van bestandsuploads**    | Slimmere API voor bestandsuploads             | Uitgebreidere, minder intuïtieve API      |
| **CI/CD-integratie**              | Eenvoudige integratie met GitHub Actions, Jenkins | Sterke integratie met veel CI-tools   |
| **Mobiel testen**                 | Beperkt, alleen emulatie                      | Volledige ondersteuning via Appium        |
| **Ondersteuning voor meerdere browsers** | Chromium, WebKit, Firefox              | Volledige ondersteuning voor grote en oudere browsers |
| **Prestaties**                    | Snel, geoptimaliseerd voor headless testen    | Langzamer, vooral in headless-modus       |
| **Testen met meerdere schermen**  | Beperkt                                       | Goede ondersteuning voor opstellingen met meerdere schermen |
| **Gemeenschap en ecosysteem**     | Groeiend, goede documentatie                  | Groot, volwassen, uitgebreid ecosysteem   |

### 7. **Beslissing**

Na het afwegen van de eisen en afwegingen is **Playwright** de betere keuze voor onze huidige behoeften. De slimmere API voor het testen van uploads van lokale bestanden, de beknopte syntaxis en de sterke ondersteuning voor het testen van interactieve UI's maken het een ideale match voor onze agile ontwikkelcyclus. Het feit dat het zowel **TypeScript** als **Python** ondersteunt, is cruciaal voor ons team, en de moderne aanpak van het framework voor testen stelt ons in staat schone, onderhoudbare code te schrijven.

Hoewel **Selenium** een uitstekende tool blijft, vooral voor mobiel testen, ondersteuning van oudere browsers en opstellingen met meerdere schermen, is het minder geschikt voor onze huidige behoeften. De omslachtigheid, langzamere prestaties en complexere omgang met dynamische UI's zoals grafieken maken het minder optimaal voor ons gebruiksscenario.

### 8. **Gevolgen**

- **Onmiddellijke actie**: we voeren **Playwright** in voor onze E2E-tests, met focus op het testen van gebruikersstromen rond registratie, inloggen, bestandsuploads, dashboards en het downloaden van rapporten.
- **Overwegingen op lange termijn**: we blijven het zich ontwikkelende ecosysteem van Playwright in de gaten houden. Als onze behoeften veranderen, vooral rond mobiel testen of ondersteuning van oudere browsers, kunnen we Selenium heroverwegen.
- **Training en documentatie**: de ontwikkelteams moeten vertrouwd raken met de API van Playwright, vooral voor het afhandelen van dynamische UI's en bestandsuploads.
- **Migratie**: bestaande Selenium-tests (indien aanwezig) worden geleidelijk gemigreerd naar Playwright.

### 9. **Toekomstige overwegingen**
