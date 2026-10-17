# Arkitektura-erabakien erregistroa: autentikazio eta baimenen aukerak

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Web aplikazioen autentikazioa eta baimena aplikazio eta zerbitzuetarako sarbidea babesteko bi kontzeptu funtsezkoak dira. Biak erabiltzaileen identitatearekin eta baimenak nola ematen diren lotuta daude, baina alderdi desberdinetan zentratzen dira:

- **Autentikazioa** erabiltzaile edo sistema baten identitatea egiaztatzeko prozesua da.
- **Baimena** autentikatutako erabiltzaileak edo sistemak zein baliabide edo ekintzatara sar daitekeen zehazteko prozesua da.

Orain, sartu gaitezen aipatu dituzun protokolo eta teknologia espezifikoetan, web aplikazio modernoetan autentikazioa eta baimena kudeatzeko ohikoak direnak.

### 1. **OAuth (Open Authorization)**

**OAuth** baimenerako estandar irekia da. Erabiltzaile batek hirugarren aplikazio bati bere baliabideetarako sarbide mugatua emateko aukera ematen du, bere kredentzialak partekatu gabe. Ideia nagusia **sarbide delegatua** da. OAuth sarritan erabiltzen da erabiltzaileak hirugarren zerbitzu batean saioa has dezakeen egoeretan (adib. Google-rekin saioa hastea), hirugarrenari zuzenean bere erabiltzaile-izena eta pasahitza eman gabe.

- **Fluxua**: OAuth-ek normalean **token-oinarritutako** fluxu bat jarraitzen du, non baimen-zerbitzari batek sarbide-token bat jaulkitzen dion hirugarren aplikazioari. Token horrek erabiltzailearen baimenak adierazten ditu, eta aplikazioak erabiltzen du erabiltzailearen datuetara edo baliabideetara API batetik sartzeko.
- **Adibidea**: Erabiltzaile batek hirugarren aplikazio batean saioa hasten du bere Google kontuarekin. Google-k erabiltzailearen identitatea egiaztatzen du eta ondoren hirugarren aplikazioari Google-ren datu batzuetara (adib. Google Calendar) sartzeko aukera ematen dion token bat ematen dio.

OAuth-ek **ez du** autentikazioa zuzenean kudeatzen; sarbidea ematearen ingurukoa da. Autentikaziorako, OAuth sarritan beste protokolo batzuekin parekatzen da, hala nola **OpenID Connect**-ekin.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** **OAuth 2.0**-ren gainean eraikitako identitate-geruza bat da, OAuth-en baimen-gaitasunei autentikazioa gehitzen diona. Funtsean, OpenID Connect-ek OAuth zabaltzen du **erabiltzaileen autentikazioa** kudeatzeko, eta aplikazioei erabiltzaile baten identitatea egiaztatzeko modu estandarizatua eskaintzen die.

- **Fluxua**: Erabiltzaile batek OpenID Connect erabiliz saioa hasten duenean, hirugarren aplikazioak ID token bat eskatzen du (OAuth sarbide-tokenaz gain). ID tokenak erabiltzaileari buruzko informazioa dauka (adib. bere erabiltzaile-izena, posta elektronikoa eta beste erreklamazio batzuk). Horrek aplikazioari erabiltzailea nor den eta autentikatuta dagoen jakiteko aukera ematen dio.
- **Adibidea**: Slack bezalako zerbitzu batean zure Google kontuarekin saioa hasteak (Google OpenID Connect hornitzailea izanik) OpenID Connect bidezko autentikazioa dakar, OAuth-ek zure Google baliabideetarako sarbidea kudeatzen duen bitartean.

OIDC-k errazten du hirugarren aplikazioek **erabiltzaileak autentikatzea**, aplikazio horiek zein baliabidetara sar daitezkeen kontrol zehatza mantenduz.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** XML oinarritutako estandar zaharragoa da, alderdien artean autentikazio- eta baimen-datuak trukatzeko erabiltzen dena, bereziki **Single Sign-On (SSO)** eszenatokietan. Batez ere enpresa-inguruneetan erabiltzen da, erabiltzaileek behin autentikatu eta aplikazio anitzetara sartu ahal izateko kredentzialak berriz sartu gabe.

- **Fluxua**: Erabiltzaileak lehenik identitate-hornitzaile (IdP) batekin autentikatzen da. IdP-k **SAML baieztapen** sinatu bat sortzen du, erabiltzailearen identitatea eta lotutako atributuak dituena. Baieztapena zerbitzu-hornitzaileari (SP) bidaltzen zaio, eta honek aplikaziorako sarbidea baimentzeko erabiltzen du.
- **Adibidea**: Langile batek bere korporazio-atarian (IdP) saioa hasten du eta automatikoki hasten du saioa beste sistemetan, hala nola posta elektronikoan, CRM-an eta abarretan, kredentzialak berriz sartu gabe. Autentikazio-prozesua IdP-k bidalitako SAML baieztapenean oinarritzen da.

SAML **enpresa SSO soluzioetan** ohikoa da eta ongi funtzionatzen du korporazio-inguruneetako web aplikazioetan, baina OAuth/OIDC baino mugikorrekiko lagunkoiagoa ez da.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** **Single Sign-On (SSO)** egiteko erabiltzen den beste protokolo bat da, bereziki Microsoft oinarritutako enpresa-inguruneetan. **WS-* (Web Services)** zehaztapen-familiaren parte da eta segurtasun-domeinu desberdinen artean (adib. erakunde desberdinen artean edo zerbitzu desberdinen artean) identitate-federazioa ahalbidetzen du.

- **Fluxua**: WS-Federation-ek **identitate-hornitzaile (IdP) fidagarri** bati erabiltzaileak autentikatzea eta zerbitzu-hornitzaileak baimenerako erabil ditzakeen tokenak jaulkitzea ahalbidetzen dio. SAML-en antzekoa da, baina sarritan Microsoft teknologian asko oinarritzen diren eszenatokietan erabiltzen da.
- **Adibidea**: Erabiltzaile batek Microsoft Azure Active Directory (AD)-k ostatatutako enpresa-aplikazio batean saioa hasten du, eta bere identitatea beste zerbitzu federatuetara sartzeko erabil daiteke, hirugarren hornitzaileek ostatatutako aplikazioak barne.

WS-Federation OAuth2.0 eta OpenID Connect bezalako protokolo berriagoek ordezkatu dute web ingurune moderno askotan, baina oraindik ere sistema zaharretan erabiltzen da, bereziki Microsoft-en inguruko enpresetan.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** direktorio-zerbitzuetara sartzeko eta horiek kudeatzeko erabiltzen den protokoloa da, ohikoa **erabiltzaileen kredentzialak gordetzeko** eta sarbide-kontrola direktorio zentralizatu batean (sarritan **Directory Service** deitua) kudeatzeko. LDAP ez da zehazki autentikazioari edo baimenari buruzkoa, baina identitate-datuak gorde eta berreskuratzeko erabiltzen da, gero prozesu horietan erabiltzen direnak.

- **Autentikazioa**: LDAP-ek aplikazio bati erabiltzaileak autentikatzeko aukera ematen dio, direktorio-zerbitzuari kredentzialak (pasahitzak adib.) kontsultatuz.
- **Baimena**: Erabiltzaileen rolak eta baimenak ere kudeatzen ditu, erabiltzaile batek baliabide jakin batzuetara sartzeko eskubidea duen zehazten lagunduz.
- **Adibidea**: Enpresa askok LDAP oinarritutako direktorioak (adib. **Active Directory**) erabiltzen dituzte autentikaziorako eta baimenerako, bereziki Windows inguruneetan.

LDAP funtsezkoa da enpresentzat barne-sistemetan erabiltzaileen sarbidea kudeatzeko, baina web testuinguru modernoan, LDAP sarritan beste protokolo batzuekin integratzen da, hala nola SAML edo OAuth-ekin, identitate-kudeaketa osoagoa lortzeko.

### 6. **SSO hornitzaile sozialak**

**Facebook**, **Google**, **Twitter**, **GitHub** eta beste batzuk bezalako **Single Sign-On (SSO)** hornitzaile sozialek erabiltzaileei hirugarren aplikazioetan autentikatzeko aukera ematen diete beren sare sozialetako kredentzialak erabiliz. **OAuth oinarritutako autentikazio** mota bat da, non hirugarren zerbitzua (adib. Google) identitate-hornitzailea den.

- **Fluxua**: Erabiltzaileak "Hasi saioa Google-rekin" botoian klik egiten du (adibidez). Aplikazioak Google-ra birbideratzen du, eta han erabiltzaileak saioa hasten du (oraindik hasi ez badu). Google-k sarbide-token bat edo ID token bat ematen dio orduan hirugarren aplikazioari, erabiltzailea autentikatzeko eta, agian, bere datuetara sartzeko erabil daitekeena.
- **Adibidea**: Aplikazio askok zure Google edo Facebook kredentzialekin saioa hasten uzten dizute. Aplikazioak OAuth edo OpenID Connect erabiliko du hondoan zure identitatea egiaztatzeko eta, kasu batzuetan, sare sozialetako datu batzuetara sartzeko.

SSO soziala autentikaziorako metodo erosoa eta oso hartua da, erabiltzaileentzat marruskadura murrizten duelako, erabiltzaile-izen eta pasahitz berri bat sortu nahi ez dutenentzat.

---

### Desberdintasunen laburpena:

- **OAuth**: Baimenerako erabiltzen da, hirugarren aplikazioei erabiltzaileen datuetara sartzeko aukera ematen die kredentzialak azaleratu gabe.
- **OpenID Connect**: OAuth zabaltzen du autentikazioa eskaintzeko, aplikazioei erabiltzailearen identitatea egiaztatzeko aukera emanez.
- **SAML**: SSO-rako erabiltzen den XML oinarritutako protokoloa, sarritan enpresa-inguruneetan.
- **WS-Federation**: Identitate-federaziorako Microsoft-en protokolo espezifikoa, sistema zaharretan erabilia.
- **LDAP**: Erabiltzaileak autentikatzeko eta baimena kudeatzeko direktorio-zerbitzuak kontsultatzeko protokoloa.
- **SSO hornitzaile sozialak**: OAuth oinarritutako sistemak (adib. Google, Facebook) hirugarren aplikazioei erabiltzaileak beren sare sozialetako kredentzialekin autentikatzeko aukera ematen dietenak.

Teknologia hauetako bakoitzak bere indarrak eta erabilera-kasuak ditu, eta aplikazio modernoetan, segurtasunaren alderdi desberdinetarako (adib. OAuth/OIDC API sarbiderako, SAML enpresa SSO-rako) horien konbinazioa erabiltzen ikus dezakezu.
