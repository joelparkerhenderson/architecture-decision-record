# Architektur-Decisiounsopzeechnung: Optioune fir Authentifikatioun an Autorisatioun

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Authentifikatioun an Autorisatioun vu Webapplikatioune si zwee wesentlech Konzepter, fir den Zougang zu Applikatiounen a Servicer ze sécheren. Béid beschäftege sech mat der Identitéit vun de Benotzer a domat, wéi Rechter erteelt ginn, awer si konzentréiere sech op ënnerschiddlech Aspekter:

- **Authentifikatioun** ass de Prozess, d'Identitéit vun engem Benotzer oder System ze verifizéieren.
- **Autorisatioun** ass de Prozess, ze bestëmmen, op wéi eng Ressourcen oder Aktiounen de authentifizéierte Benotzer oder System zougräifen däerf.

Elo gi mir an déi spezifesch Protokoller an Technologien, déi Dir genannt hutt, a déi gemeinsam a modernen Webapplikatioune benotzt, fir Authentifikatioun an Autorisatioun ze verwalten.

### 1. **OAuth (Open Authorization)**

**OAuth** ass en oppene Standard fir Autorisatioun. Hie erlaabt engem Benotzer, enger Drëtt-Applikatioun limitéierten Zougang zu senge Ressourcen ze ginn, ouni seng Umeldedaten ze deelen. D'Haaptiddi ass **delegéierten Zougang**. OAuth gëtt dacks a Situatioune benotzt, wou Benotzer sech bei engem Drëtt-Service umelde kënnen (z.B. mat Google umellen), ouni direkt hire Benotzernumm a Passwuert un den Drëtte weiderzeginn.

- **Flow**: OAuth follegt typesch engem **token-baséierte** Flow, wou en Autorisatiounsserver en Access-Token un d'Drëtt-Applikatioun ausgëtt. Dëse Token representéiert d'Rechter vum Benotzer, an d'Applikatioun benotzt en, fir op d'Daten oder Ressourcen vum Benotzer vun enger API zouzegräifen.
- **Beispill**: E Benotzer mellt sech mat sengem Google-Kont an enger Drëtt-App un. Google verifizéiert d'Identitéit vum Benotzer a gëtt dann en Token, deen der Drëtt-App erlaabt, op e puer Google-Daten (z.B. Google Calendar) zouzegräifen.

OAuth behandelt Authentifikatioun **net** direkt; et geet ëm d'Erteele vum Zougang. Fir d'Authentifikatioun gëtt OAuth dacks mat anere Protokoller kombinéiert, wéi **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** ass eng Identitéitsschicht, déi op **OAuth 2.0** opbaut a Authentifikatioun zu den Autorisatiounsfäegkeete vun OAuth derbäifügt. Am Wesentlechen erweidert OpenID Connect OAuth, fir **Benotzerauthentifikatioun** ze behandelen, a bitt Applikatiounen eng standardiséiert Manéier, d'Identitéit vun engem Benotzer ze verifizéieren.

- **Flow**: Wann e Benotzer sech mat OpenID Connect umellt, freet d'Drëtt-Applikatioun en ID-Token un (zousätzlech zum OAuth-Access-Token). Den ID-Token enthält Informatiounen iwwer de Benotzer (wéi säi Benotzernumm, seng E-Mail an aner Claims). Dat erlaabt der Applikatioun ze wëssen, wien de Benotzer ass a ob en authentifizéiert ass.
- **Beispill**: D'Umellung bei engem Service wéi Slack mat Ärem Google-Kont (Google ass den OpenID-Connect-Provider) implizéiert Authentifikatioun iwwer OpenID Connect, während OAuth den Zougang zu Ären Google-Ressourcen verwalt.

OIDC mécht et fir Drëtt-Apps méi einfach, **Benotzer ze authentifizéieren**, an erlaabt weiderhin eng fein Kontroll doriwwer, op wéi eng Ressourcen dës Apps zougräife kënnen.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** ass e méi alen, XML-baséierte Standard, deen benotzt gëtt, fir Authentifikatiouns- an Autorisatiounsdaten tëscht Parteien auszetauschen, besonnesch a **Single-Sign-On-(SSO)**-Szenarien. Hie gëtt haaptsächlech an Enterprise-Ëmfelder benotzt, fir Benotzer z'erméiglechen, sech eemol ze authentifizéieren an op verschidden Applikatiounen zouzegräifen, ouni d'Umeldedaten nei anzeginn.

- **Flow**: De Benotzer authentifizéiert sech als éischt bei engem Identity Provider (IdP). Den IdP generéiert eng ënnerschriwwen **SAML-Assertion**, déi d'Identitéit vum Benotzer an zougehéiereg Attributer enthält. D'Assertion gëtt un de Service Provider (SP) geschéckt, deen se benotzt, fir den Zougang zur Applikatioun ze autoriséieren.
- **Beispill**: E Mataarbechter mellt sech bäi sengem Firmeportal (dem IdP) un a gëtt automatesch an aner Systemer wéi E-Mail, CRM, asw. ageloggt, ouni d'Umeldedaten nei anzeginn. De Authentifikatiounsprozess baséiert op der SAML-Assertion, déi vum IdP geschéckt gëtt.

SAML gëtt dacks a **Enterprise-SSO-Léisungen** benotzt a funktionéiert gutt fir Webapplikatiounen a Firmeëmfelder, ass awer manner mobilfrëndlech am Verglach zu OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** ass en anert Protokoll, dat fir **Single Sign-On (SSO)** benotzt gëtt, besonnesch a Microsoft-baséierten Enterprise-Ëmfelder. Et ass Deel vun der **WS-* (Web Services)**-Famill vu Spezifikatiounen an erlaabt Identitéitsfederatioun iwwer verschidde Sécherheetsdomäne (wéi tëscht verschiddenen Organisatiounen oder tëscht verschiddene Servicer).

- **Flow**: WS-Federation erlaabt engem **vertrauenswürdegen Identity Provider (IdP)**, Benotzer ze authentifizéieren an Tokens auszestellen, déi de Service Provider fir d'Autorisatioun benotze kann. Et ass ähnlech wéi SAML, gëtt awer dacks a Szenarien benotzt, déi staark op Microsoft-Technologien ugewise sinn.
- **Beispill**: E Benotzer mellt sech an eng Enterprise-Applikatioun un, déi vu Microsoft Azure Active Directory (AD) gehost gëtt, a seng Identitéit ka benotzt ginn, fir op aner federéiert Servicer zouzegräifen, dorënner Applikatiounen, déi vun Drëttanbieter gehost ginn.

Och wann WS-Federation a ville modernen Webëmfelder gréisstendeels duerch méi nei Protokoller wéi OAuth2.0 an OpenID Connect ersat gouf, gëtt et nach ëmmer a Legacy-Systemer benotzt, besonnesch a Microsoft-zentréierten Entreprisen.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** ass e Protokoll, dat benotzt gëtt, fir op Verzeechnesservicer zouzegräifen an se ze verwalten, a gëtt dacks fir **d'Späichere vu Benotzerumeldedaten** an d'Verwaltung vun der Zougangskontroll an engem zentrale Verzeechnes (dacks **Directory Service** genannt) benotzt. LDAP geet net speziell ëm Authentifikatioun oder Autorisatioun, mee gëtt benotzt, fir Identitéitsdaten ze späicheren an ofzefroen, déi dann an dëse Prozesser benotzt ginn.

- **Authentifikatioun**: LDAP erlaabt eng Applikatioun, Benotzer ze authentifizéieren, andeems de Verzeechnesservice no Umeldedaten (wéi Passwierder) ofgefrot gëtt.
- **Autorisatioun**: Et verwalt och Benotzerrollen a -rechter, wat hëlleft ze bestëmmen, ob e Benotzer Zougang zu bestëmmte Ressourcen huet.
- **Beispill**: Vill Entreprise benotze LDAP-baséiert Verzeechnesser (z.B. **Active Directory**) fir Authentifikatioun an Autorisatioun, besonnesch a Windows-Ëmfelder.

LDAP ass fir Entreprisen entscheedend, fir den Zougang vu Benotzer iwwer intern Systemer ze verwalten, awer an engem modernen Webkontext gëtt LDAP dacks mat anere Protokoller wéi SAML oder OAuth fir eng méi komplett Identitéitsverwaltung integréiert.

### 6. **Social-SSO-Provider**

Sozial **Single-Sign-On-(SSO)**-Provider wéi **Facebook**, **Google**, **Twitter**, **GitHub** an anerer erlaben de Benotzer, sech mat hiren Social-Media-Umeldedaten an Drëtt-Applikatiounen z'authentifizéieren. Dëst ass eng Zort **OAuth-baséiert Authentifikatioun**, wou den Drëtt-Service (z.B. Google) den Identity Provider ass.

- **Flow**: De Benotzer klickt op "Log in with Google" (zum Beispill). D'App leet op Google ëm, wou de Benotzer sech umellt (wann en net scho ageloggt ass). Google gëtt dann en Access-Token oder ID-Token un d'Drëtt-App, deen benotzt ka ginn, fir de Benotzer ze authentifizéieren a méiglecherweis op seng Daten zouzegräifen.
- **Beispill**: Vill Applikatiounen erlaben Iech, Iech mat Ären Google- oder Facebook-Umeldedaten unzemellen. D'App benotzt hannert de Kulissen OAuth oder OpenID Connect, fir Är Identitéit ze verifizéieren an a verschiddene Fäll op bestëmmt Social-Media-Daten zouzegräifen.

Social SSO ass eng praktesch a wäit verbreet Method fir d'Authentifikatioun, well se d'Reibung fir Benotzer reduzéiert, déi vläicht net nach e Benotzernumm a Passwuert erstelle wëllen.

---

### Zesummefaassung vun den Ënnerscheeder:

- **OAuth**: Gëtt fir d'Autorisatioun benotzt, erlaabt Drëtt-Apps, op Benotzerdaten zouzegräifen, ouni Umeldedaten opzedecken.
- **OpenID Connect**: Erweidert OAuth ëm Authentifikatioun, erlaabt Apps, d'Identitéit vum Benotzer ze verifizéieren.
- **SAML**: XML-baséiert Protokoll fir SSO, dacks an Enterprise-Ëmfelder.
- **WS-Federation**: E Microsoft-spezifescht Protokoll fir Identitéitsfederatioun, benotzt a Legacy-Systemer.
- **LDAP**: E Protokoll, fir Verzeechnesservicer ofzefroen, fir Benotzer ze authentifizéieren an d'Autorisatioun ze verwalten.
- **Social-SSO-Provider**: OAuth-baséiert Systemer (wéi Google, Facebook), déi Drëtt-Apps erlaben, Benotzer mat hire Social-Media-Umeldedaten ze authentifizéieren.

Jidd vun dësen Technologien huet seng eege Stäerkten an Notzungsfäll, an a modernen Applikatioune kann eng Kombinatioun dovun fir verschidden Aspekter vun der Sécherheet benotzt ginn (z.B. OAuth/OIDC fir API-Zougang, SAML fir Enterprise-SSO).
