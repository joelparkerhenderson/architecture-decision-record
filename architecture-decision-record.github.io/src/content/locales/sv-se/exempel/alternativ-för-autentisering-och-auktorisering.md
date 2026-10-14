# Arkitekturbeslutspost: alternativ för autentisering och auktorisering

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Autentisering och auktorisering i webbapplikationer är två avgörande begrepp för att skydda åtkomsten till applikationer och tjänster. Båda handlar om användarnas identitet och hur behörigheter beviljas, men de fokuserar på olika aspekter:

- **Autentisering** är processen att verifiera en användares eller ett systems identitet.
- **Auktorisering** är processen att avgöra vilka resurser eller åtgärder den autentiserade användaren eller det autentiserade systemet får komma åt.

Nu går vi in på de specifika protokoll och tekniker du nämnt, som ofta används i moderna webbapplikationer för att hantera autentisering och auktorisering.

### 1. **OAuth (Open Authorization)**

**OAuth** är en öppen standard för auktorisering. Den låter en användare ge en tredjepartsapplikation begränsad åtkomst till sina resurser utan att dela sina inloggningsuppgifter. Grundtanken är **delegerad åtkomst**. OAuth används ofta i situationer där användare kan logga in hos en tredjepartstjänst (t.ex. logga in med Google) utan att direkt ange sitt användarnamn och lösenord till tredjeparten.

- **Flöde**: OAuth följer vanligtvis ett **tokenbaserat** flöde, där en auktoriseringsserver utfärdar en åtkomsttoken till tredjepartsapplikationen. Den här token representerar användarens behörigheter, och applikationen använder den för att komma åt användarens data eller resurser från ett API.
- **Exempel**: En användare loggar in i en tredjepartsapp med sitt Google-konto. Google verifierar användarens identitet och beviljar sedan en token som låter tredjepartsappen komma åt vissa Google-data (t.ex. Google Kalender).

OAuth hanterar **inte** autentisering direkt; det handlar om att bevilja åtkomst. För autentisering kombineras OAuth ofta med andra protokoll, som **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** är ett identitetslager byggt ovanpå **OAuth 2.0** som lägger till autentisering till OAuths auktoriseringsfunktioner. I grunden utökar OpenID Connect OAuth för att hantera **användarautentisering** och ger applikationer ett standardiserat sätt att verifiera en användares identitet.

- **Flöde**: När en användare loggar in med OpenID Connect begär tredjepartsapplikationen en ID-token (utöver OAuth-åtkomsttoken). ID-token innehåller information om användaren (som användarnamn, e-post och andra anspråk). Det låter applikationen veta vem användaren är och om den är autentiserad.
- **Exempel**: Att logga in i en tjänst som Slack med ditt Google-konto (där Google är OpenID Connect-leverantören) innebär autentisering via OpenID Connect, medan OAuth hanterar åtkomsten till dina Google-resurser.

OIDC gör det enklare för tredjepartsappar att **autentisera användare** samtidigt som det fortfarande tillåter detaljerad kontroll över vilka resurser dessa appar kan komma åt.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** är en äldre, XML-baserad standard som används för att utbyta autentiserings- och auktoriseringsdata mellan parter, särskilt i scenarier med **enkel inloggning (SSO)**. Den används främst i företagsmiljöer för att låta användare autentisera sig en gång och komma åt flera applikationer utan att ange inloggningsuppgifterna på nytt.

- **Flöde**: Användaren autentiserar sig först hos en identitetsleverantör (IdP). IdP:n genererar ett signerat **SAML-påstående** som innehåller användarens identitet och tillhörande attribut. Påståendet skickas till tjänsteleverantören (SP), som använder det för att auktorisera åtkomst till applikationen.
- **Exempel**: En anställd loggar in på sitt företagsportal (IdP:n) och loggas automatiskt in i andra system som e-post, CRM osv. utan att ange inloggningsuppgifterna på nytt. Autentiseringsprocessen bygger på det SAML-påstående som IdP:n skickar.

SAML används ofta i **SSO-lösningar för företag** och fungerar bra för webbapplikationer i företagsmiljöer, men är mindre mobilvänligt jämfört med OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** är ytterligare ett protokoll som används för **enkel inloggning (SSO)**, särskilt i Microsoft-baserade företagsmiljöer. Det ingår i specifikationsfamiljen **WS-* (Web Services)** och möjliggör identitetsfederation över olika säkerhetsdomäner (till exempel mellan olika organisationer eller mellan olika tjänster).

- **Flöde**: WS-Federation låter en **betrodd identitetsleverantör (IdP)** autentisera användare och utfärda token som tjänsteleverantören kan använda för auktorisering. Det liknar SAML men används ofta i scenarier som i hög grad förlitar sig på Microsoft-teknik.
- **Exempel**: En användare loggar in i ett företagsprogram som hostas av Microsoft Azure Active Directory (AD), och dennes identitet kan användas för att komma åt andra federerade tjänster, inklusive applikationer som hostas av tredjepartsleverantörer.

Även om WS-Federation i stor utsträckning har ersatts av nyare protokoll som OAuth 2.0 och OpenID Connect i många moderna webbmiljöer används det fortfarande i äldre system, särskilt i Microsoft-centrerade företag.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** är ett protokoll som används för att komma åt och hantera katalogtjänster, vanligen för att **lagra användaruppgifter** och hantera åtkomstkontroll i en central katalog (ofta kallad **katalogtjänst**). LDAP handlar inte specifikt om autentisering eller auktorisering utan används för att lagra och hämta identitetsdata, som sedan används i dessa processer.

- **Autentisering**: LDAP låter en applikation autentisera användare genom att fråga katalogtjänsten om inloggningsuppgifter (som lösenord).
- **Auktorisering**: Det hanterar också användarroller och behörigheter, vilket hjälper till att avgöra om en användare har åtkomst till vissa resurser.
- **Exempel**: Många företag använder LDAP-baserade kataloger (t.ex. **Active Directory**) för autentisering och auktorisering, särskilt i Windows-miljöer.

LDAP är avgörande för företag för att hantera användaråtkomst över interna system, men i en modern webbkontext integreras LDAP ofta med andra protokoll som SAML eller OAuth för mer fullständig identitetshantering.

### 6. **Leverantörer av social SSO**

Leverantörer av social **enkel inloggning (SSO)** som **Facebook**, **Google**, **Twitter**, **GitHub** och andra låter användare autentisera sig i tredjepartsapplikationer med sina inloggningsuppgifter från sociala medier. Detta är en typ av **OAuth-baserad autentisering** där tredjepartstjänsten (t.ex. Google) är identitetsleverantören.

- **Flöde**: Användaren klickar på ”Logga in med Google” (till exempel). Appen omdirigerar till Google, där användaren loggar in (om den inte redan är inloggad). Google tillhandahåller sedan en åtkomsttoken eller ID-token till tredjepartsappen, som kan användas för att autentisera användaren och eventuellt komma åt dennes data.
- **Exempel**: Många applikationer låter dig logga in med dina Google- eller Facebook-uppgifter. Appen använder OAuth eller OpenID Connect bakom kulisserna för att verifiera din identitet och, i vissa fall, komma åt viss data från sociala medier.

Social SSO är en bekväm och allmänt använd autentiseringsmetod eftersom den minskar friktionen för användare som kanske inte vill skapa ännu ett användarnamn och lösenord.

---

### Sammanfattning av skillnaderna:

- **OAuth**: Används för auktorisering, låter tredjepartsappar komma åt användardata utan att avslöja inloggningsuppgifter.
- **OpenID Connect**: Utökar OAuth för att tillhandahålla autentisering, så att appar kan verifiera användarens identitet.
- **SAML**: XML-baserat protokoll som används för SSO, ofta i företagsmiljöer.
- **WS-Federation**: Ett Microsoft-specifikt protokoll för identitetsfederation, som används i äldre system.
- **LDAP**: Ett protokoll för att fråga katalogtjänster för att autentisera användare och hantera auktorisering.
- **Leverantörer av social SSO**: OAuth-baserade system (som Google, Facebook) som låter tredjepartsappar autentisera användare med deras inloggningsuppgifter från sociala medier.

Var och en av dessa tekniker har sina egna styrkor och användningsfall, och i moderna applikationer kan du se en kombination av dem användas för olika säkerhetsaspekter (t.ex. OAuth/OIDC för API-åtkomst, SAML för SSO i företag).
