# Architectuurbeslissingsdocument: opties voor authenticatie en autorisatie

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Authenticatie en autorisatie van webapplicaties zijn twee cruciale concepten bij het beveiligen van toegang tot applicaties en diensten. Beide gaan over de identiteit van gebruikers en hoe rechten worden verleend, maar ze richten zich op verschillende aspecten:

- **Authenticatie** is het proces van het verifiëren van de identiteit van een gebruiker of systeem.
- **Autorisatie** is het proces van het bepalen tot welke bronnen of acties de geauthenticeerde gebruiker of het geauthenticeerde systeem toegang heeft.

Laten we nu dieper ingaan op de specifieke protocollen en technologieën die je noemde en die vaak worden gebruikt in moderne webapplicaties voor het beheren van authenticatie en autorisatie.

### 1. **OAuth (Open Authorization)**

**OAuth** is een open standaard voor autorisatie. Het stelt een gebruiker in staat een externe applicatie beperkte toegang tot zijn bronnen te verlenen zonder zijn inloggegevens te delen. Het kernidee is **gedelegeerde toegang**. OAuth wordt vaak gebruikt in situaties waarin gebruikers kunnen inloggen bij een externe dienst (bijvoorbeeld inloggen met Google) zonder hun gebruikersnaam en wachtwoord rechtstreeks aan de externe partij te geven.

- **Flow**: OAuth volgt doorgaans een **tokengebaseerde** flow, waarbij een autorisatieserver een toegangstoken uitgeeft aan de externe applicatie. Dit token vertegenwoordigt de rechten van de gebruiker en de applicatie gebruikt het om toegang te krijgen tot de data of bronnen van de gebruiker via een API.
- **Voorbeeld**: een gebruiker meldt zich aan bij een externe app met zijn Google-account. Google verifieert de identiteit van de gebruiker en verleent vervolgens een token waarmee de externe app toegang krijgt tot bepaalde Google-data (bijvoorbeeld Google Agenda).

OAuth handelt authenticatie **niet** rechtstreeks af; het gaat om het verlenen van toegang. Voor authenticatie wordt OAuth vaak gecombineerd met andere protocollen, zoals **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** is een identiteitslaag bovenop **OAuth 2.0** die authenticatie toevoegt aan de autorisatiemogelijkheden van OAuth. In essentie breidt OpenID Connect OAuth uit om **gebruikersauthenticatie** af te handelen en biedt het een gestandaardiseerde manier voor applicaties om de identiteit van een gebruiker te verifiëren.

- **Flow**: wanneer een gebruiker inlogt met OpenID Connect, vraagt de externe applicatie een ID-token aan (naast het OAuth-toegangstoken). Het ID-token bevat informatie over de gebruiker (zoals gebruikersnaam, e-mailadres en andere claims). Hierdoor weet de applicatie wie de gebruiker is en of die geauthenticeerd is.
- **Voorbeeld**: inloggen bij een dienst als Slack met je Google-account (Google is de OpenID Connect-provider) omvat authenticatie via OpenID Connect, terwijl OAuth de toegang tot je Google-bronnen beheert.

OIDC maakt het voor externe apps gemakkelijker om **gebruikers te authenticeren** en geeft toch fijnmazige controle over tot welke bronnen die apps toegang hebben.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** is een oudere, op XML gebaseerde standaard voor het uitwisselen van authenticatie- en autorisatiegegevens tussen partijen, met name in **Single Sign-On (SSO)**-scenario's. Het wordt voornamelijk gebruikt in bedrijfsomgevingen zodat gebruikers één keer kunnen authenticeren en toegang krijgen tot meerdere applicaties zonder opnieuw hun inloggegevens in te voeren.

- **Flow**: de gebruiker authenticeert eerst bij een identiteitsprovider (IdP). De IdP genereert een ondertekende **SAML-assertie** met de identiteit van de gebruiker en bijbehorende attributen. De assertie wordt naar de serviceprovider (SP) gestuurd, die deze gebruikt om toegang tot de applicatie te autoriseren.
- **Voorbeeld**: een medewerker logt in op zijn bedrijfsportaal (de IdP) en wordt automatisch ingelogd bij andere systemen zoals e-mail, CRM enz., zonder opnieuw inloggegevens in te voeren. Het authenticatieproces is gebaseerd op de SAML-assertie die de IdP verstuurt.

SAML wordt vaak gebruikt in **SSO-oplossingen voor bedrijven** en werkt goed voor webapplicaties in zakelijke omgevingen, maar is minder mobielvriendelijk dan OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** is een ander protocol voor **Single Sign-On (SSO)**, vooral in op Microsoft gebaseerde bedrijfsomgevingen. Het maakt deel uit van de **WS-* (Web Services)**-familie van specificaties en maakt identiteitsfederatie mogelijk over verschillende beveiligingsdomeinen heen (zoals tussen verschillende organisaties of tussen verschillende diensten).

- **Flow**: WS-Federation laat een **vertrouwde identiteitsprovider (IdP)** gebruikers authenticeren en tokens uitgeven die de serviceprovider kan gebruiken voor autorisatie. Het lijkt op SAML, maar wordt vaak gebruikt in scenario's die sterk op Microsoft-technologieën leunen.
- **Voorbeeld**: een gebruiker logt in op een bedrijfsapplicatie die wordt gehost door Microsoft Azure Active Directory (AD), en zijn identiteit kan worden gebruikt om toegang te krijgen tot andere gefedereerde diensten, waaronder applicaties die door externe leveranciers worden gehost.

Hoewel WS-Federation in veel moderne webomgevingen grotendeels is vervangen door nieuwere protocollen zoals OAuth2.0 en OpenID Connect, wordt het nog steeds gebruikt in legacysystemen, vooral in op Microsoft gerichte bedrijven.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** is een protocol voor het benaderen en beheren van directoryservices, vaak gebruikt voor het **opslaan van gebruikersreferenties** en het beheren van toegangscontrole in een gecentraliseerde directory (vaak een **Directory Service** genoemd). LDAP gaat niet specifiek over authenticatie of autorisatie, maar wordt gebruikt om identiteitsgegevens op te slaan en op te halen, die vervolgens in die processen worden gebruikt.

- **Authenticatie**: met LDAP kan een applicatie gebruikers authenticeren door de directoryservice te bevragen naar referenties (zoals wachtwoorden).
- **Autorisatie**: het beheert ook gebruikersrollen en machtigingen en helpt bepalen of een gebruiker toegang heeft tot bepaalde bronnen.
- **Voorbeeld**: veel bedrijven gebruiken op LDAP gebaseerde directory's (bijv. **Active Directory**) voor authenticatie en autorisatie, vooral binnen Windows-omgevingen.

LDAP is cruciaal voor bedrijven om gebruikerstoegang tot interne systemen te beheren, maar in een moderne webcontext wordt LDAP vaak geïntegreerd met andere protocollen zoals SAML of OAuth voor completer identiteitsbeheer.

### 6. **Sociale SSO-providers**

Sociale **Single Sign-On (SSO)**-providers zoals **Facebook**, **Google**, **Twitter**, **GitHub** en andere stellen gebruikers in staat zich bij externe applicaties te authenticeren met hun inloggegevens van sociale media. Dit is een soort **op OAuth gebaseerde authenticatie** waarbij de externe dienst (bijv. Google) de identiteitsprovider is.

- **Flow**: de gebruiker klikt op "Inloggen met Google" (bijvoorbeeld). De app stuurt door naar Google, waar de gebruiker inlogt (als die nog niet is ingelogd). Google levert vervolgens een toegangstoken of ID-token aan de externe app, dat kan worden gebruikt om de gebruiker te authenticeren en mogelijk toegang te krijgen tot zijn data.
- **Voorbeeld**: veel applicaties laten je inloggen met je Google- of Facebook-gegevens. De app gebruikt achter de schermen OAuth of OpenID Connect om je identiteit te verifiëren en in sommige gevallen toegang te krijgen tot bepaalde data van sociale media.

Sociale SSO is een handige en veelgebruikte authenticatiemethode omdat het de drempel voor gebruikers verlaagt, die misschien niet nog een gebruikersnaam en wachtwoord willen aanmaken.

---

### Samenvatting van de verschillen:

- **OAuth**: gebruikt voor autorisatie, laat externe apps toegang krijgen tot gebruikersdata zonder inloggegevens bloot te geven.
- **OpenID Connect**: breidt OAuth uit met authenticatie, zodat apps de identiteit van de gebruiker kunnen verifiëren.
- **SAML**: op XML gebaseerd protocol voor SSO, vaak in bedrijfsomgevingen.
- **WS-Federation**: een Microsoft-specifiek protocol voor identiteitsfederatie, gebruikt in legacysystemen.
- **LDAP**: een protocol voor het bevragen van directoryservices om gebruikers te authenticeren en autorisatie te beheren.
- **Sociale SSO-providers**: op OAuth gebaseerde systemen (zoals Google, Facebook) waarmee externe apps gebruikers kunnen authenticeren met hun inloggegevens van sociale media.

Elk van deze technologieën heeft zijn eigen sterke punten en gebruiksscenario's, en in moderne applicaties zie je mogelijk een combinatie ervan voor verschillende aspecten van beveiliging (bijv. OAuth/OIDC voor API-toegang, SAML voor SSO voor bedrijven).
