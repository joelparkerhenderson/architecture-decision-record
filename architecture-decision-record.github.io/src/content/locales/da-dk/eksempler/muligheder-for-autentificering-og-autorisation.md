# Arkitekturbeslutningspost: muligheder for autentificering og autorisation

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Autentificering og autorisation i webapplikationer er to afgørende begreber i sikring af adgang til applikationer og tjenester. Begge handler om brugeres identitet og om, hvordan tilladelser gives, men de fokuserer på forskellige aspekter:

- **Autentificering** er processen med at verificere en brugers eller et systems identitet.
- **Autorisation** er processen med at afgøre, hvilke ressourcer eller handlinger den autentificerede bruger eller det autentificerede system har adgang til.

Lad os nu dykke ned i de specifikke protokoller og teknologier, du nævnte, som ofte bruges i moderne webapplikationer til at håndtere autentificering og autorisation.

### 1. **OAuth (Open Authorization)**

**OAuth** er en åben standard for autorisation. Den giver en bruger mulighed for at give en tredjepartsapplikation begrænset adgang til sine ressourcer uden at dele sine legitimationsoplysninger. Nøgleidéen er **delegeret adgang**. OAuth bruges ofte i situationer, hvor brugere kan logge ind på en tredjepartstjeneste (f.eks. logge ind med Google) uden direkte at give deres brugernavn og adgangskode til tredjeparten.

- **Flow**: OAuth følger typisk et **tokenbaseret** flow, hvor en autorisationsserver udsteder et adgangstoken til tredjepartsapplikationen. Dette token repræsenterer brugerens tilladelser, og applikationen bruger det til at få adgang til brugerens data eller ressourcer fra et API.
- **Eksempel**: en bruger logger ind på en tredjepartsapp med sin Google-konto. Google verificerer brugerens identitet og giver derefter et token, der gør det muligt for tredjepartsappen at få adgang til nogle Google-data (f.eks. Google Kalender).

OAuth håndterer **ikke** autentificering direkte; det handler om at give adgang. Til autentificering kombineres OAuth ofte med andre protokoller, som **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** er et identitetslag bygget oven på **OAuth 2.0**, der tilføjer autentificering til OAuths autorisationsfunktioner. Grundlæggende udvider OpenID Connect OAuth til at håndtere **brugerautentificering** og giver en standardiseret måde for applikationer at verificere en brugers identitet.

- **Flow**: når en bruger logger ind med OpenID Connect, anmoder tredjepartsapplikationen om et ID-token (ud over OAuth-adgangstokenet). ID-tokenet indeholder oplysninger om brugeren (såsom brugernavn, e-mail og andre claims). Det gør det muligt for applikationen at vide, hvem brugeren er, og om vedkommende er autentificeret.
- **Eksempel**: at logge ind på en tjeneste som Slack med din Google-konto (Google er OpenID Connect-udbyderen) indebærer autentificering via OpenID Connect, mens OAuth styrer adgangen til dine Google-ressourcer.

OIDC gør det lettere for tredjepartsapps at **autentificere brugere** og giver stadig finkornet kontrol over, hvilke ressourcer disse apps kan få adgang til.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** er en ældre, XML-baseret standard til udveksling af autentificerings- og autorisationsdata mellem parter, især i **Single Sign-On (SSO)**-scenarier. Den bruges primært i virksomhedsmiljøer, så brugere kan autentificere én gang og få adgang til flere applikationer uden at indtaste legitimationsoplysninger igen.

- **Flow**: brugeren autentificerer først hos en identitetsudbyder (IdP). IdP'en genererer en signeret **SAML-assertion**, der indeholder brugerens identitet og relaterede attributter. Assertionen sendes til tjenesteudbyderen (SP), som bruger den til at autorisere adgang til applikationen.
- **Eksempel**: en medarbejder logger ind på sin virksomhedsportal (IdP'en) og bliver automatisk logget ind på andre systemer som e-mail, CRM osv. uden at indtaste legitimationsoplysninger igen. Autentificeringsprocessen er baseret på den SAML-assertion, IdP'en sender.

SAML bruges almindeligvis i **SSO-løsninger til virksomheder** og fungerer godt til webapplikationer i virksomhedsmiljøer, men er mindre mobilvenlig end OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** er en anden protokol til **Single Sign-On (SSO)**, især i Microsoft-baserede virksomhedsmiljøer. Den er en del af **WS-* (Web Services)**-familien af specifikationer og muliggør identitetsfederation på tværs af forskellige sikkerhedsdomæner (f.eks. mellem forskellige organisationer eller mellem forskellige tjenester).

- **Flow**: WS-Federation lader en **betroet identitetsudbyder (IdP)** autentificere brugere og udstede tokens, som tjenesteudbyderen kan bruge til autorisation. Den ligner SAML, men bruges ofte i scenarier, der i høj grad bygger på Microsoft-teknologier.
- **Eksempel**: en bruger logger ind på en virksomhedsapplikation hostet af Microsoft Azure Active Directory (AD), og vedkommendes identitet kan bruges til at få adgang til andre fødererede tjenester, herunder applikationer hostet af tredjepartsleverandører.

Selv om WS-Federation i vidt omfang er erstattet af nyere protokoller som OAuth2.0 og OpenID Connect i mange moderne webmiljøer, bruges den stadig i ældre systemer, især i Microsoft-centrerede virksomheder.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** er en protokol, der bruges til at få adgang til og administrere katalogtjenester, almindeligvis brugt til at **gemme brugeroplysninger** og styre adgangskontrol i et centralt katalog (ofte kaldet en **Directory Service**). LDAP handler ikke specifikt om autentificering eller autorisation, men bruges til at gemme og hente identitetsdata, som derefter bruges i disse processer.

- **Autentificering**: LDAP giver en applikation mulighed for at autentificere brugere ved at forespørge katalogtjenesten om legitimationsoplysninger (som adgangskoder).
- **Autorisation**: den administrerer også brugerroller og tilladelser og hjælper med at afgøre, om en bruger har adgang til visse ressourcer.
- **Eksempel**: mange virksomheder bruger LDAP-baserede kataloger (f.eks. **Active Directory**) til autentificering og autorisation, især i Windows-miljøer.

LDAP er afgørende for virksomheder til at administrere brugeradgang på tværs af interne systemer, men i en moderne webkontekst integreres LDAP ofte med andre protokoller som SAML eller OAuth for mere komplet identitetsstyring.

### 6. **Sociale SSO-udbydere**

Sociale **Single Sign-On (SSO)**-udbydere som **Facebook**, **Google**, **Twitter**, **GitHub** og andre giver brugere mulighed for at autentificere sig i tredjepartsapplikationer med deres legitimationsoplysninger fra sociale medier. Det er en slags **OAuth-baseret autentificering**, hvor tredjepartstjenesten (f.eks. Google) er identitetsudbyderen.

- **Flow**: brugeren klikker på "Log ind med Google" (for eksempel). Appen omdirigerer til Google, hvor brugeren logger ind (hvis vedkommende ikke allerede er logget ind). Google giver derefter et adgangstoken eller ID-token til tredjepartsappen, som kan bruges til at autentificere brugeren og muligvis få adgang til vedkommendes data.
- **Eksempel**: mange applikationer lader dig logge ind med dine Google- eller Facebook-oplysninger. Appen bruger OAuth eller OpenID Connect bag kulisserne til at verificere din identitet og i nogle tilfælde få adgang til visse data fra sociale medier.

Social SSO er en praktisk og udbredt autentificeringsmetode, fordi den reducerer gnidning for brugere, som måske ikke vil oprette endnu et brugernavn og en adgangskode.

---

### Oversigt over forskellene:

- **OAuth**: bruges til autorisation, lader tredjepartsapps få adgang til brugerdata uden at afsløre legitimationsoplysninger.
- **OpenID Connect**: udvider OAuth med autentificering, så apps kan verificere brugerens identitet.
- **SAML**: XML-baseret protokol til SSO, ofte i virksomhedsmiljøer.
- **WS-Federation**: en Microsoft-specifik protokol til identitetsfederation, brugt i ældre systemer.
- **LDAP**: en protokol til at forespørge katalogtjenester for at autentificere brugere og administrere autorisation.
- **Sociale SSO-udbydere**: OAuth-baserede systemer (som Google, Facebook), der lader tredjepartsapps autentificere brugere med deres legitimationsoplysninger fra sociale medier.

Hver af disse teknologier har sine egne styrker og anvendelsestilfælde, og i moderne applikationer kan du se en kombination af dem bruges til forskellige aspekter af sikkerhed (f.eks. OAuth/OIDC til API-adgang, SAML til virksomheds-SSO).
