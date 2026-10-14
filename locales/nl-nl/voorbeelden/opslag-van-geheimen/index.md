# Opslag van geheimen

Inhoud:

* [Samenvatting](#samenvatting)
  * [Kwestie](#kwestie)
  * [Beslissing](#beslissing)
  * [Status](#status)
* [Details](#details)
  * [Aannames](#aannames)
  * [Beperkingen](#beperkingen)
  * [Standpunten](#standpunten)
  * [Argument](#argument)
  * [Implicaties](#implicaties)
* [Gerelateerd](#gerelateerd)
  * [Gerelateerde beslissingen](#gerelateerde-beslissingen)
  * [Gerelateerde eisen](#gerelateerde-eisen)
  * [Gerelateerde artefacten](#gerelateerde-artefacten)
  * [Gerelateerde principes](#gerelateerde-principes)
* [Notities](#notities)
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Samenvatting


### Kwestie

We moeten geheimen opslaan, zoals wachtwoorden, privésleutels, authenticatietokens enz.

Sommige geheimen zijn gebruikersgericht. Onze ontwikkelaar wil bijvoorbeeld zijn mobiele telefoon kunnen gebruiken om een wachtwoord voor een dienst op te zoeken.

Sommige geheimen zijn systeemgericht. Onze pijplijn voor continue levering moet bijvoorbeeld de inloggegevens voor onze cloudhosting kunnen opzoeken.


### Beslissing

Bitwarden voor gebruikersgerichte geheimen.

Vault by HashiCorp voor systeemgerichte geheimen.


### Status

Besloten. We staan open voor nieuwe opties zodra ze zich aandienen.


## Details


### Aannames

Voor dit doel en onze huidige situatie hechten we waarde aan gebruikersgericht gemak, zoals nuttige mobiele apps.

  * We willen snelle, eenvoudige toegang onderweg waarborgen, bijvoorbeeld voor een ontwikkelaar die storingsdienst draait voor betrouwbaarheidstechniek.

  * We willen sommige geheimen kunnen delen tussen geselecteerde personen, zoals een team.

We proberen niet te oplossen voor één enkele leverancier, bijvoorbeeld alle geheimen uitsluitend bij Amazon of Azure of Google opslaan.

We willen geen ad-hocaanpakken zoals "onthoud het" of "schrijf het op een briefje" of "zoek zelf maar uit hoe je het opslaat".

Ons beveiligingsmodel voor dit doel is tevreden met het gebruik van gerenommeerde COTS-leveranciers, bijvoorbeeld SaaS-tools voor wachtwoordbeheer.


### Beperkingen

Op dit moment willen we iets eenvoudigs, dat wil zeggen geen code schrijven, geen servers installeren, geen grote verplichting aangaan en niet iedereen standaardiseren.


### Standpunten

We hebben overwogen:

1. Gebruikersgerichte kant-en-klare wachtwoordmanagers: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG enz.

2. Systeemgerichte COTS-wachtwoordmanagers: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Op delen gerichte aanpakken: een gedeeld Google-document, een gedeeld Slack-kanaal, een gedeelde netwerkmap enz. gebruiken.

4. Laagtechnologische ad-hocaanpakken, zoals onthouden, een briefje schrijven of erop vertrouwen dat elke gebruiker zelf een manier bedenkt.


### Argument

Bitwarden, LastPass, 1Password en Dashlane zijn allemaal commerciële kant-en-klare producten.

  * Vergelijkbare soorten functies voor gebruikers, teams, organisaties enz.

  * Desktopmogelijkheden voor Windows en Mac, en mobiele mogelijkheden voor Android en iOS.

  * Browserextensies voor Chrome en Firefox, voor automatisch invullen van formulieren enz.

Bitwarden heeft twee voordelen ten opzichte van de andere:

  * Bitwarden is open source, wat betekent dat de beveiliging door vakgenoten kan worden beoordeeld en dat het bedrijf ook algemeen wordt gewaardeerd door beveiligingsbewuste ontwikkelaars.

  * Anekdotes van softwaremensen beschrijven een aanzienlijke voorkeur voor Bitwarden boven de andere.

Een typisch goed verslag: https://jcs.org/2017/11/17/bitwarden

Een typische stemsite met vergelijking naast elkaar: https://stackshare.io/stackups/bitwarden-vs-dashlane

We stellen KeyPass, pass, GPG enz. uit omdat er extra complexiteit is. Ze lijken allemaal goede oplossingen voor technische gebruikers. GPG lijkt vooral goed voor technische gebruikers die opdrachtgerichte mogelijkheden over systemen heen willen.

We stellen KMS uit omdat het vendor lock-in heeft bij één enkele leverancier.

We kiezen Vault voor systeemgerichte behoeften, omdat de beoordelingen verrassend positief zijn en omdat HashiCorp een uitstekende staat van dienst heeft op het gebied van software en ondersteuning van topkwaliteit.

We spreken een veto uit over de aanpakken met delen, bijvoorbeeld via gedeelde documenten, gedeelde kanalen, gedeelde netwerkmappen enz. Deze bieden niet de beveiligingskwaliteiten die we willen.

We spreken een veto uit over de laagtechnologische ad-hocaanpakken, omdat we het er allemaal over eens zijn dat dat geen weg vooruit is op de lange termijn.


### Implicaties

Ontwikkelaars moeten mogelijk geheimen op twee plaatsen bijhouden: Bitwarden voor gebruikersgerichte toegang en Vault voor systeemgerichte toegang.


## Gerelateerd


### Gerelateerde beslissingen

De beslissing over welke CI/CD-server we kiezen, moet bewijs bevatten van het vermogen om toegang te krijgen tot geheimen.

We moeten beslissen hoe de geheimen worden beheerd, wat betreft beleid, rotaties, organisaties enz.


### Gerelateerde eisen

De geheimen krijgen gerelateerde eisen voor naleving, auditing en HR-onboarding/offboarding.


### Gerelateerde artefacten

We verwachten dat we sommige geheimen naar omgevingsvariabelen kunnen exporteren.


### Gerelateerde principes

Gemakkelijk omkeerbaar.

Gemakkelijk parallel te draaien, dat wil zeggen dat het eenvoudig is een verscheidenheid aan wachtwoordmanagers te gebruiken.

Goedkoop om uit te proberen, dat wil zeggen dat er een gratis proefperiode is en geen verplichting.


## Notities

Evaluatienotities hier. De notities zijn allemaal openbare opmerkingen op verschillende devops-discussieforums.


### Vault by HashiCorp

Vault is precies wat je hier wilt. 

Maar gooi Vault niet zomaar in productie, zet het eerst op in een testomgeving, want de documentatie van HashiCorp kan nogal gebrekkig zijn, ook al zijn hun producten fantastisch.

Zeer steile leercurve en het is niet triviaal om op te zetten. 

De eerste inrichting is een beetje een gedoe. Het is absoluut de moeite waard, en de gemeenschap ondersteunt het goed genoeg om je erdoorheen te slepen.

Vreselijke documentatie, maar er zijn tal van gidsen online van mensen die het hebben opgezet en als je er een paar combineert, heb je een werkende opstelling.

De eerste inrichting vereiste gerommel met hun helm-charts (vault en consul). Technisch gezien kun je veel andere backends gebruiken, maar ik raad dat echt, echt niet aan. De backend/consul kan piepklein zijn als je niet veel data hoeft op te slaan.

Maak je zeker vertrouwd met het gebruik van de CLI, want de GUI is meer een proof-of-concept/reclameportaal voor hun enterprise-editie.

Het feit dat je het niet zomaar kunt "vullen" is een gedoe. Als je bijvoorbeeld 5 velden hebt, moet je voor elk item handmatig elk veld toevoegen. Het is dus niet zo dat je velden voor een specifieke categorie vooraf definieert en die velden invult voor alle items in die categorie, maar eerder dat "je elke keer alles genereert", wat (naar mijn mening) een gedoe is.

Je kunt ook kijken naar goldfish als UI bovenop vault. Het maakt het vrij aangenaam om je team mee te krijgen. Ze hebben ook een demo. 1. Zet consul op. 2. Zet vault op dat naar consul wijst. 3. Zet goldfish op dat naar vault wijst. 3. Zet een cron-job op die consul snapshot draait voor back-ups.



### LastPass

LastPass Teams. We gebruiken het, hebben aangepaste sjablonen, ACL's, en naar mijn mening ontbreekt er niets.

Ik heb LastPass in mijn organisatie geïmplementeerd en geef het een C+/B-. Het grootste probleem de laatste tijd is een gebrek aan betrouwbaarheid. In de afgelopen 90 dagen waren er meerdere uren waarin kluizen gedwongen in offlinemodus werden gezet. Dit is niet ideaal voor mijn organisatie, omdat we letterlijk 4.000+ wachtwoorden hebben opgeslagen in 20+ gedeelde mappen. Zoals je je kunt voorstellen worden er bij zoveel wachtwoorden elke dag minstens een paar bijgewerkt of toegevoegd. We hebben een DR-plan als problemen langer dan een uur of twee duren: een script ondertekent en versleutelt elke nacht een CSV-dump van de kluis die kan worden geïmporteerd in keepass.

LastPass heeft onopgemerkte momenten van verminderde dienstverlening gehad: inloggen "werkt" maar haalt geen sites op, willekeurige functies in het beheerderspaneel zijn kapot en sleutels worden niet goed gedeeld voor nieuwe gedeelde mappen op het hoogste niveau. Ik heb een speciale "key push"-/back-upgebruiker die in elke groep zit. Meestal lost inloggen als die gebruiker alle problemen met sleuteldeling op, maar niet wanneer de dienst verminderd is, wat de statuspagina ook zegt...

Voor integratie kan het eenvoudig zijn als je goede ACL's hebt met een model van minimale rechten, bijvoorbeeld als een gebruiker zowel lees- en schrijf- als leesrechten heeft op een item of map, krijgt hij alleen leesrechten. Helaas zijn de ACL's van mijn organisatie niet de beste, dus uiteindelijk gebruikte ik de JSON-provisioning-API en ~500 regels python, omdat de afhankelijkheid in onze honderden ACL's niet goed op het model van minimale rechten aansloot. Uiteindelijk haalde ik alle ACL's op waarin een gebruiker zat en deed een soort afhankelijkheidswandeling.

Als je ACL- of groepsstructuur al is opgebouwd met een structuur van minimale rechten in gedachten, werkt de AD/LDAP-synchronisatietool voor Windows prima.

Neem contact op met hun verkoopteam, zij kunnen een langere Enterprise-proefperiode regelen. Zorg ervoor dat je de beperkingen volledig begrijpt voordat je de trekker overhaalt. We hadden nogal wat kinderziektes, maar afgezien van storingen of verminderde dienstverlening aan de serverkant is het ongelooflijk soepel verlopen.


### Bitwarden

Bitwarden heeft goede tools eromheen (WebUI, CLI, mobiel, desktop). Kan zelf worden gehost en is vrij eenvoudig op te zetten. Vrij goede documentatie en een tool die wordt aanbevolen door PrivacyTools.


### EnvKey

https://www.envkey.com/ is een saas. Echt eenvoudig te implementeren, te integreren en te beheren.

Functies:

  * Bescherm API-sleutels en inloggegevens.

  * Houd de configuratie overal gesynchroniseerd.

  * Slim, end-to-end versleuteld beheer van configuratie en geheimen. 

  * Voorkom onveilig delen en wildgroei aan configuratie. 

  * Integreer in enkele minuten.

Mogelijkheden:

  * Beheer configuratie en toegangsniveaus voor al je apps, omgevingen en teams op één plek.

  * Configureer elke ontwikkel- of serveromgeving met slechts één omgevingsvariabele.

Voordelen:

  * Geweldige landingspagina.

  * Duidelijke waardepropositie.

  * Visueel uitstekende web-app.

  * Superieure voorbeelddata, bijv. Algolia, AWS, Datadog, GitHub, Stripe enz.

  * 30 minuten met de oprichter gesproken over het bedrijf, de UI enz. Dane klinkt goed geïnformeerd, eerlijk over de voor- en nadelen en als een haalbare partner.

  * Het bedrijf is in feite een typisch Y Combinator-bedrijf met 1 oprichter. Haalde $120K op in 2018-01.

  * De focus ligt op het bereiken van bedrijfsfuncties, met name de overstap van EnvKey-cloudhosting naar on-prem of BYOC.

  * Mogelijke weg vooruit: begin met EnvKey voor de eenvoud en voeg later (of parallel) Vault toe. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant is een open-source dienst voor geheimenbeheer die gebruiksvriendelijke, veilige opslag van en toegang tot geheimen biedt, van de ontwikkelaars bij Lyft.

KMS-authenticatie: Confidant lost het "kip-en-ei"-probleem van authenticatie op door AWS KMS en IAM te gebruiken om IAM-rollen veilige authenticatietokens te laten genereren die door Confidant kunnen worden geverifieerd. Confidant beheert ook KMS-grants voor je IAM-rollen, waardoor de IAM-rollen tokens kunnen genereren die kunnen worden gebruikt voor authenticatie tussen services, of voor het verzenden van versleutelde berichten tussen services.

Versleuteling in rust van geversioneerde geheimen: Confidant slaat geheimen op in DynamoDB op een alleen-toevoegen-manier en genereert een unieke KMS-datasleutel voor elke revisie van elk geheim, met behulp van de symmetrische geauthenticeerde cryptografie Fernet.

Een gebruiksvriendelijke webinterface voor het beheren van geheimen: Confidant biedt een AngularJS-webinterface waarmee eindgebruikers gemakkelijk geheimen, toewijzingen van geheimen aan services en de wijzigingsgeschiedenis kunnen beheren.


### Devolutions Password Server

https://server.devolutions.net/

Beveilig, beheer en bewaak toegang tot bevoorrechte accounts en sessies.

Een uitgebreide, zeer veilige wachtwoordkluis waarmee je de toegang tot je bevoorrechte accounts kunt beheersen, terwijl de algehele netwerkzichtbaarheid voor systeembeheerders wordt verbeterd en eindgebruikers een naadloze ervaring krijgen.

Functies: gecentraliseerde organisatiewachtwoordkluis, gebruikersspecifieke privékluis, wachtwoordmanager, injectie van inloggegevens,
Active Directory-integratie, rolgebaseerde toegangscontrole, tweefactorauthenticatie, bedrijfsklaar, IP-beperkingen, beheermogelijkheden, automatische wachtwoordgenerator, toegang via mobiele app, wachtwoordgeschiedenis, toegangsrapporten, e-mailwaarschuwingen.

  * ondersteunt gegevensversleuteling

  * ondersteunt meerdere authenticatieschema's, waaronder LDAP, O365 en lokale gebruikers MET MFA-ondersteuning uit meerdere bronnen

  * meerdere repo's/kluizen met gedetailleerde toegangscontroles voor meerdere teams

  * moderne web-UI

  * privékluizen voor inloggegevens en verbindingen voor persoonlijke inloggegevens/verbindingen

  * mobiele apps voor iOS/Android

  * auditlogs voor elk item, wie/wat/wanneer met een optionele vraag waarom ze het openen

  * aanpasbare sjablonen (hoewel ze honderden verbindingstypen native ondersteunen)

  * veel meer functies en een dikke client voor Windows/Mac (Remote Desktop Manager) waarmee je kunt synchroniseren en die de opties sterk uitbreidt... verbindingen met één klik

  * de prijs is niet slecht - tot 15 gebruikers kost de wachtwoordserver $500 per jaar


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Functies van de on-premises-versie: 

  * Volledige controle over je end-to-end-beveiligingssystemen en infrastructuur

  * Deploy de software in je eigen on-premises datacenter of je eigen instantie van een virtueel privécloud

  * Voldoe aan wettelijke en regelgevende verplichtingen die vereisen dat alle data en systemen on-premises staan

Functies van de cloudversie:

  * Het software-as-a-service-model laat je je direct aanmelden en beginnen

  * Elastische schaalbaarheid naarmate je groeit

  * Controles en redundantie geleverd door Azure met 99,9% uptime-SLA

Gebruikersfeedback:

  * We gebruikten dat product vroeger. Het was zo gemakkelijk te omzeilen en de regels werken alleen voor slimme mensen. Luie of domme gebruikers kunnen het gemakkelijk verpesten in een teamomgeving. De prijzen zijn onderhandelbaar als je met hen praat.

  * Je kunt het draaien met SQL express en een Win 7-computer. 

  * Goedkoop.
