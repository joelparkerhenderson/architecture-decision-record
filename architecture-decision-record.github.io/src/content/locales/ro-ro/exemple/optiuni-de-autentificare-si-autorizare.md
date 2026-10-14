# Înregistrare a deciziei de arhitectură: opțiuni de autentificare și autorizare

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Autentificarea și autorizarea aplicațiilor web sunt două concepte esențiale în securizarea accesului la aplicații și servicii. Ambele se referă la identitatea utilizatorilor și la modul în care sunt acordate permisiunile, dar se concentrează pe aspecte diferite:

- **Autentificarea** (engl. authentication) este procesul de verificare a identității unui utilizator sau a unui sistem.
- **Autorizarea** (engl. authorization) este procesul de stabilire a resurselor sau a acțiunilor la care utilizatorul sau sistemul autentificat are acces.

Să aprofundăm acum protocoalele și tehnologiile specifice pe care le-ai menționat, folosite frecvent în aplicațiile web moderne pentru gestionarea autentificării și autorizării.

### 1. **OAuth (Open Authorization)**

**OAuth** este un standard deschis pentru autorizare. Permite unui utilizator să acorde unei aplicații terțe acces limitat la resursele sale, fără a-și partaja datele de autentificare. Ideea cheie este **accesul delegat**. OAuth este adesea folosit în situații în care utilizatorii se pot conecta la un serviciu terț (de exemplu, conectarea cu Google) fără a furniza direct numele de utilizator și parola terțului.

- **Flux**: OAuth urmează de obicei un flux **bazat pe token-uri**, în care un server de autorizare emite un token de acces către aplicația terță. Acest token reprezintă permisiunile utilizatorului, iar aplicația îl folosește pentru a accesa datele sau resursele utilizatorului dintr-un API.
- **Exemplu**: Un utilizator se conectează la o aplicație terță folosind contul său Google. Google verifică identitatea utilizatorului și apoi acordă un token care permite aplicației terțe să acceseze unele date Google (de exemplu, Google Calendar).

OAuth **nu** gestionează direct autentificarea; este vorba despre acordarea accesului. Pentru autentificare, OAuth este adesea asociat cu alte protocoale, precum **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** este un strat de identitate construit peste **OAuth 2.0**, care adaugă autentificare capabilităților de autorizare ale OAuth. În esență, OpenID Connect extinde OAuth pentru a gestiona **autentificarea utilizatorilor** și oferă aplicațiilor un mod standardizat de a verifica identitatea unui utilizator.

- **Flux**: Când un utilizator se conectează folosind OpenID Connect, aplicația terță solicită un token de identitate (în plus față de token-ul de acces OAuth). Token-ul de identitate conține informații despre utilizator (precum numele de utilizator, e-mailul și alte revendicări). Astfel, aplicația știe cine este utilizatorul și dacă este autentificat.
- **Exemplu**: Conectarea la un serviciu precum Slack folosind contul Google (Google fiind furnizorul OpenID Connect) implică autentificare prin OpenID Connect, în timp ce OAuth gestionează accesul la resursele tale Google.

OIDC face mai ușor pentru aplicațiile terțe să **autentifice utilizatorii**, permițând în același timp un control fin asupra resurselor la care au acces aceste aplicații.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** este un standard mai vechi, bazat pe XML, folosit pentru schimbul de date de autentificare și autorizare între părți, în special în scenarii de **autentificare unică (Single Sign-On, SSO)**. Este folosit în principal în medii enterprise pentru a le permite utilizatorilor să se autentifice o singură dată și să acceseze mai multe aplicații fără a reintroduce datele de autentificare.

- **Flux**: Utilizatorul se autentifică mai întâi la un furnizor de identitate (IdP). IdP-ul generează o **aserțiune SAML** semnată, care include identitatea utilizatorului și atributele conexe. Aserțiunea este trimisă furnizorului de servicii (SP), care o folosește pentru a autoriza accesul la aplicație.
- **Exemplu**: Un angajat se conectează la portalul corporativ (IdP) și este conectat automat la alte sisteme precum e-mail, CRM etc., fără a reintroduce datele de autentificare. Procesul de autentificare se bazează pe aserțiunea SAML trimisă de IdP.

SAML este folosit frecvent în **soluții SSO enterprise** și funcționează bine pentru aplicațiile web din medii corporative, dar este mai puțin prietenos cu dispozitivele mobile decât OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** este un alt protocol folosit pentru **autentificare unică (SSO)**, în special în mediile enterprise bazate pe Microsoft. Face parte din familia de specificații **WS-* (Web Services)** și permite federarea identităților între domenii de securitate diferite (de exemplu, între organizații diferite sau între servicii diferite).

- **Flux**: WS-Federation permite unui **furnizor de identitate (IdP) de încredere** să autentifice utilizatori și să emită token-uri pe care furnizorul de servicii le poate folosi pentru autorizare. Este similar cu SAML, dar este adesea folosit în scenarii care se bazează în mare măsură pe tehnologii Microsoft.
- **Exemplu**: Un utilizator se conectează la o aplicație enterprise găzduită de Microsoft Azure Active Directory (AD), iar identitatea sa poate fi folosită pentru a accesa alte servicii federate, inclusiv aplicații găzduite de furnizori terți.

Deși WS-Federation este în mare parte înlocuit de protocoale mai noi, precum OAuth 2.0 și OpenID Connect, în multe medii web moderne, este încă folosit în sisteme vechi, în special în întreprinderile centrate pe Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** este un protocol folosit pentru accesarea și gestionarea serviciilor de director, folosit frecvent pentru **stocarea datelor de autentificare ale utilizatorilor** și gestionarea controlului accesului într-un director centralizat (numit adesea **serviciu de director**). LDAP nu se referă în mod specific la autentificare sau autorizare, ci este folosit pentru a stoca și a prelua date de identitate, care sunt apoi folosite în aceste procese.

- **Autentificare**: LDAP permite unei aplicații să autentifice utilizatori interogând serviciul de director pentru datele de autentificare (precum parolele).
- **Autorizare**: Gestionează, de asemenea, rolurile și permisiunile utilizatorilor, ajutând la stabilirea dacă un utilizator are acces la anumite resurse.
- **Exemplu**: Multe întreprinderi folosesc directoare bazate pe LDAP (de exemplu, **Active Directory**) pentru autentificare și autorizare, în special în mediile Windows.

LDAP este esențial pentru întreprinderi pentru gestionarea accesului utilizatorilor la sistemele interne, dar într-un context web modern LDAP este adesea integrat cu alte protocoale precum SAML sau OAuth pentru o gestionare mai completă a identității.

### 6. **Furnizori SSO social**

Furnizorii de **autentificare unică (SSO)** socială, precum **Facebook**, **Google**, **Twitter**, **GitHub** și alții, le permit utilizatorilor să se autentifice în aplicații terțe folosind datele lor de autentificare din rețelele sociale. Este un tip de **autentificare bazată pe OAuth**, în care serviciul terț (de exemplu, Google) este furnizorul de identitate.

- **Flux**: Utilizatorul face clic pe „Conectare cu Google” (de exemplu). Aplicația redirecționează către Google, unde utilizatorul se autentifică (dacă nu este deja autentificat). Google furnizează apoi un token de acces sau un token de identitate aplicației terțe, care poate fi folosit pentru a autentifica utilizatorul și, eventual, pentru a-i accesa datele.
- **Exemplu**: Multe aplicații îți permit să te conectezi folosind datele tale Google sau Facebook. Aplicația va folosi OAuth sau OpenID Connect în fundal pentru a-ți verifica identitatea și, în unele cazuri, pentru a accesa anumite date din rețelele sociale.

SSO social este o metodă comodă și larg adoptată de autentificare, deoarece reduce fricțiunea pentru utilizatori, care poate nu vor să creeze încă un nume de utilizator și o parolă.

---

### Rezumatul diferențelor:

- **OAuth**: Folosit pentru autorizare, permite aplicațiilor terțe să acceseze datele utilizatorului fără a expune datele de autentificare.
- **OpenID Connect**: Extinde OAuth pentru a oferi autentificare, permițând aplicațiilor să verifice identitatea utilizatorului.
- **SAML**: Protocol bazat pe XML folosit pentru SSO, adesea în medii enterprise.
- **WS-Federation**: Un protocol specific Microsoft pentru federarea identităților, folosit în sisteme vechi.
- **LDAP**: Un protocol pentru interogarea serviciilor de director pentru autentificarea utilizatorilor și gestionarea autorizării.
- **Furnizori SSO social**: Sisteme bazate pe OAuth (precum Google, Facebook) care permit aplicațiilor terțe să autentifice utilizatori folosind datele lor din rețelele sociale.

Fiecare dintre aceste tehnologii are punctele sale forte și cazurile sale de utilizare, iar în aplicațiile moderne poți vedea o combinație a lor folosită pentru diferite aspecte ale securității (de exemplu, OAuth/OIDC pentru accesul la API, SAML pentru SSO enterprise).
