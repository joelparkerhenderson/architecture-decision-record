# Rekord ta' deċiżjoni arkitettonika: għażliet ta' awtentikazzjoni u awtorizzazzjoni

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

L-awtentikazzjoni u l-awtorizzazzjoni ta' applikazzjonijiet tal-web huma żewġ kunċetti kruċjali biex jiġi żgurat l-aċċess għall-applikazzjonijiet u s-servizzi. It-tnejn jittrattaw l-identità tal-utenti u kif jingħataw il-permessi, iżda jiffukaw fuq aspetti differenti:

- **L-awtentikazzjoni** hija l-proċess li permezz tiegħu tiġi vverifikata l-identità ta' utent jew sistema.
- **L-awtorizzazzjoni** hija l-proċess li permezz tiegħu jiġi ddeterminat liema riżorsi jew azzjonijiet jista' jaċċessa l-utent jew is-sistema awtentikati.

Issa, ejja nidħlu fil-fond fil-protokolli u t-teknoloġiji speċifiċi li semmejt, li jintużaw komunement f'applikazzjonijiet moderni tal-web għall-ġestjoni tal-awtentikazzjoni u tal-awtorizzazzjoni.

### 1. **OAuth (Open Authorization)**

**OAuth** huwa standard miftuħ għall-awtorizzazzjoni. Jippermetti lil utent jagħti aċċess limitat lil applikazzjoni ta' parti terza għar-riżorsi tiegħu mingħajr ma jaqsam il-kredenzjali tiegħu. L-idea ewlenija hija l-**aċċess iddelegat**. OAuth spiss jintuża f'sitwazzjonijiet fejn l-utenti jistgħu jidħlu f'servizz ta' parti terza (eż., billi jidħlu b'Google) mingħajr ma jagħtu direttament l-isem tal-utent u l-password tagħhom lill-parti terza.

- **Fluss**: OAuth tipikament isegwi fluss **ibbażat fuq tokens**, fejn server tal-awtorizzazzjoni joħroġ token ta' aċċess lill-applikazzjoni tal-parti terza. Dan it-token jirrappreżenta l-permessi tal-utent, u l-applikazzjoni tużah biex taċċessa d-data jew ir-riżorsi tal-utent minn API.
- **Eżempju**: Utent jidħol f'app ta' parti terza bl-użu tal-kont Google tiegħu. Google tivverifika l-identità tal-utent u mbagħad tagħti token li jippermetti lill-app tal-parti terza taċċessa xi data ta' Google (eż., Google Calendar).

OAuth **ma jittrattax** direttament l-awtentikazzjoni; huwa dwar l-għoti ta' aċċess. Għall-awtentikazzjoni, OAuth spiss jiġi akkoppjat ma' protokolli oħra, bħal **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** huwa saff ta' identità mibni fuq **OAuth 2.0** li jżid l-awtentikazzjoni mal-kapaċitajiet ta' awtorizzazzjoni ta' OAuth. Essenzjalment, OpenID Connect jestendi OAuth biex jittratta l-**awtentikazzjoni tal-utent** u jipprovdi mod standardizzat biex l-applikazzjonijiet jivverifikaw l-identità ta' utent.

- **Fluss**: Meta utent jidħol bl-użu ta' OpenID Connect, l-applikazzjoni tal-parti terza titlob token tal-ID (flimkien mat-token ta' aċċess ta' OAuth). It-token tal-ID fih informazzjoni dwar l-utent (bħall-isem tal-utent, l-email, u claims oħra). Dan jippermetti lill-applikazzjoni tkun taf min hu l-utent u jekk huwiex awtentikat.
- **Eżempju**: Id-dħul f'servizz bħal Slack bl-użu tal-kont Google tiegħek (Google tkun il-fornitur ta' OpenID Connect) jinvolvi awtentikazzjoni permezz ta' OpenID Connect, filwaqt li OAuth jimmaniġġja l-aċċess għar-riżorsi tiegħek ta' Google.

OIDC jagħmilha eħfef għall-apps ta' partijiet terzi biex **jawtentikaw l-utenti** filwaqt li xorta jippermettu kontroll dettaljat fuq liema riżorsi dawk l-apps jistgħu jaċċessaw.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** huwa standard eqdem, ibbażat fuq XML, użat biex tiġi skambjata data ta' awtentikazzjoni u awtorizzazzjoni bejn partijiet, partikolarment fi xenarji ta' **Single Sign-On (SSO)**. Jintuża primarjament f'ambjenti tal-intrapriża biex l-utenti jkunu jistgħu jawtentikaw darba waħda u jaċċessaw applikazzjonijiet multipli mingħajr ma jerġgħu jdaħħlu l-kredenzjali.

- **Fluss**: L-utent l-ewwel jawtentika ma' fornitur tal-identità (IdP). L-IdP jiġġenera **assertion SAML** iffirmata li tinkludi l-identità tal-utent u attributi relatati. L-assertion tintbagħat lill-fornitur tas-servizz (SP), li jużaha biex jawtorizza l-aċċess għall-applikazzjoni.
- **Eżempju**: Impjegat jidħol fil-portal korporattiv tiegħu (l-IdP) u jidħol awtomatikament f'sistemi oħra bħall-email, is-CRM, eċċ., mingħajr ma jerġa' jdaħħal il-kredenzjali. Il-proċess tal-awtentikazzjoni huwa bbażat fuq l-assertion SAML mibgħuta mill-IdP.

SAML jintuża komunement f'**soluzzjonijiet SSO tal-intrapriża** u jaħdem tajjeb għal applikazzjonijiet tal-web f'ambjenti korporattivi, iżda huwa inqas faċli għall-mobile meta mqabbel ma' OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** huwa protokoll ieħor użat għal **Single Sign-On (SSO)**, speċjalment f'ambjenti tal-intrapriża bbażati fuq Microsoft. Huwa parti mill-familja ta' speċifikazzjonijiet **WS-* (Web Services)** u jippermetti federazzjoni tal-identità fuq dominji ta' sigurtà differenti (bħal bejn organizzazzjonijiet differenti jew bejn servizzi differenti).

- **Fluss**: WS-Federation jippermetti li **fornitur tal-identità fdat (IdP)** jawtentika l-utenti u joħroġ tokens li l-fornitur tas-servizz jista' juża għall-awtorizzazzjoni. Huwa simili għal SAML iżda spiss jintuża f'xenarji li jiddependu ħafna fuq teknoloġiji ta' Microsoft.
- **Eżempju**: Utent jidħol f'applikazzjoni tal-intrapriża ospitata minn Microsoft Azure Active Directory (AD), u l-identità tiegħu tista' tintuża biex jaċċessa servizzi federati oħra, inklużi applikazzjonijiet ospitati minn fornituri ta' partijiet terzi.

Għalkemm WS-Federation fil-biċċa l-kbira ġie mibdul minn protokolli ġodda bħal OAuth2.0 u OpenID Connect f'ħafna ambjenti moderni tal-web, xorta jintuża f'sistemi legacy, speċjalment f'intrapriżi ċċentrati fuq Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** huwa protokoll użat biex jaċċessa u jimmaniġġja servizzi tad-direttorju, użat komunement għall-**ħażna tal-kredenzjali tal-utenti** u l-ġestjoni tal-kontroll tal-aċċess f'direttorju ċentralizzat (spiss imsejjaħ **Servizz tad-Direttorju**). LDAP mhuwiex speċifikament dwar l-awtentikazzjoni jew l-awtorizzazzjoni iżda jintuża biex jaħżen u jirkupra data dwar l-identità, li mbagħad tintuża f'dawk il-proċessi.

- **Awtentikazzjoni**: LDAP jippermetti lil applikazzjoni tawtentika l-utenti billi tistaqsi s-servizz tad-direttorju għall-kredenzjali (bħall-passwords).
- **Awtorizzazzjoni**: Jimmaniġġja wkoll ir-rwoli u l-permessi tal-utenti, u jgħin jiġi ddeterminat jekk utent għandux aċċess għal ċerti riżorsi.
- **Eżempju**: Ħafna intrapriżi jużaw direttorji bbażati fuq LDAP (eż., **Active Directory**) għall-awtentikazzjoni u l-awtorizzazzjoni, speċjalment f'ambjenti Windows.

LDAP huwa kruċjali għall-intrapriżi biex jimmaniġġjaw l-aċċess tal-utenti fuq sistemi interni, iżda f'kuntest modern tal-web, LDAP spiss jiġi integrat ma' protokolli oħra bħal SAML jew OAuth għal ġestjoni aktar kompleta tal-identità.

### 6. **Fornituri ta' Social SSO**

Il-fornituri ta' **Single Sign-On (SSO)** soċjali bħal **Facebook**, **Google**, **Twitter**, **GitHub**, u oħrajn jippermettu lill-utenti jawtentikaw f'applikazzjonijiet ta' partijiet terzi bl-użu tal-kredenzjali tal-midja soċjali tagħhom. Dan huwa tip ta' **awtentikazzjoni bbażata fuq OAuth** fejn is-servizz ta' parti terza (eż., Google) huwa l-fornitur tal-identità.

- **Fluss**: L-utent jikklikkja "Log in with Google" (pereżempju). L-app tirredirezzjona lejn Google, fejn l-utent jidħol (jekk mhux diġà dieħel). Google mbagħad tipprovdi token ta' aċċess jew token tal-ID lill-app tal-parti terza, li jista' jintuża biex jawtentika l-utent u possibbilment jaċċessa d-data tiegħu.
- **Eżempju**: Ħafna applikazzjonijiet jippermettulek tidħol bl-użu tal-kredenzjali tiegħek ta' Google jew Facebook. L-app tuża OAuth jew OpenID Connect fl-isfond biex tivverifika l-identità tiegħek u, f'xi każijiet, taċċessa ċerta data tal-midja soċjali.

Il-Social SSO huwa metodu konvenjenti u adottat b'mod wiesa' għall-awtentikazzjoni għax inaqqas l-frizzjoni għall-utenti, li jistgħu ma jkunux irridu joħolqu isem tal-utent u password oħra.

---

### Sommarju tad-differenzi:

- **OAuth**: Użat għall-awtorizzazzjoni, jippermetti lill-apps ta' partijiet terzi jaċċessaw id-data tal-utent mingħajr ma jesponu l-kredenzjali.
- **OpenID Connect**: Jestendi OAuth biex jipprovdi awtentikazzjoni, u jippermetti lill-apps jivverifikaw l-identità tal-utent.
- **SAML**: Protokoll ibbażat fuq XML użat għal SSO, spiss f'ambjenti tal-intrapriża.
- **WS-Federation**: Protokoll speċifiku għal Microsoft għall-federazzjoni tal-identità, użat f'sistemi legacy.
- **LDAP**: Protokoll biex jiġu mistoqsija servizzi tad-direttorju sabiex jiġu awtentikati l-utenti u jiġi ġestit l-awtorizzazzjoni.
- **Fornituri ta' Social SSO**: Sistemi bbażati fuq OAuth (bħal Google, Facebook) li jippermettu lill-apps ta' partijiet terzi jawtentikaw l-utenti bl-użu tal-kredenzjali tal-midja soċjali tagħhom.

Kull waħda minn dawn it-teknoloġiji għandha s-saħħiet u l-każijiet ta' użu tagħha, u f'applikazzjonijiet moderni, tista' tara taħlita tagħhom użata għal aspetti differenti tas-sigurtà (eż., OAuth/OIDC għall-aċċess għall-API, SAML għal SSO tal-intrapriża).
