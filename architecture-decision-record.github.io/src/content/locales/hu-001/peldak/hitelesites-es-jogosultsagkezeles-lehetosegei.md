# Architekturális döntési feljegyzés: hitelesítés és jogosultságkezelés lehetőségei

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

A webalkalmazások hitelesítése és jogosultságkezelése két kulcsfontosságú fogalom az alkalmazásokhoz és szolgáltatásokhoz való hozzáférés biztosításában. Mindkettő a felhasználók identitásával és a jogosultságok megadásának módjával foglalkozik, de különböző szempontokra összpontosít:

- A **hitelesítés** (authentication) egy felhasználó vagy rendszer identitásának ellenőrzése.
- A **jogosultságkezelés** (authorization) annak megállapítása, hogy a hitelesített felhasználó vagy rendszer mely erőforrásokhoz vagy műveletekhez fér hozzá.

Merüljünk most el az Ön által említett konkrét protokollokban és technológiákban, amelyeket gyakran használnak modern webalkalmazásokban a hitelesítés és jogosultságkezelés kezelésére.

### 1. **OAuth (Open Authorization)**

Az **OAuth** a jogosultságkezelés nyílt szabványa. Lehetővé teszi, hogy egy felhasználó korlátozott hozzáférést adjon egy harmadik fél alkalmazásának az erőforrásaihoz a hitelesítő adatai megosztása nélkül. A kulcsgondolat a **delegált hozzáférés**. Az OAuth-ot gyakran használják olyan helyzetekben, ahol a felhasználók bejelentkezhetnek egy harmadik fél szolgáltatásába (pl. bejelentkezés Google-lal) anélkül, hogy közvetlenül megadnák felhasználónevüket és jelszavukat a harmadik félnek.

- **Folyamat**: Az OAuth általában **tokenalapú** folyamatot követ, amelyben egy jogosultságkezelő kiszolgáló hozzáférési tokent ad ki a harmadik fél alkalmazásának. Ez a token a felhasználó jogosultságait képviseli, és az alkalmazás ezzel fér hozzá a felhasználó adataihoz vagy erőforrásaihoz egy API-ból.
- **Példa**: Egy felhasználó bejelentkezik egy harmadik fél alkalmazásába a Google-fiókjával. A Google ellenőrzi a felhasználó identitását, majd kiad egy tokent, amely lehetővé teszi a harmadik fél alkalmazásának, hogy hozzáférjen néhány Google-adathoz (pl. Google Naptár).

Az OAuth **nem** kezeli közvetlenül a hitelesítést; a hozzáférés megadásáról szól. Hitelesítéshez az OAuth-ot gyakran más protokollokkal párosítják, például az **OpenID Connecttel**.

### 2. **OpenID Connect (OIDC)**

Az **OpenID Connect (OIDC)** az **OAuth 2.0** tetejére épített identitásréteg, amely hitelesítéssel egészíti ki az OAuth jogosultságkezelési képességeit. Lényegében az OpenID Connect kiterjeszti az OAuth-ot a **felhasználói hitelesítés** kezelésére, és szabványos módot nyújt az alkalmazásoknak a felhasználó identitásának ellenőrzésére.

- **Folyamat**: Amikor egy felhasználó OpenID Connecttel jelentkezik be, a harmadik fél alkalmazása azonosító tokent (ID token) kér (az OAuth hozzáférési tokenen felül). Az azonosító token információkat tartalmaz a felhasználóról (például felhasználónév, e-mail és egyéb állítások). Ez lehetővé teszi, hogy az alkalmazás tudja, ki a felhasználó, és hitelesített-e.
- **Példa**: Egy olyan szolgáltatásba, mint a Slack, a Google-fiókkal való bejelentkezés (a Google az OpenID Connect szolgáltatója) OpenID Connecten keresztüli hitelesítést jelent, míg az OAuth kezeli a Google-erőforrásokhoz való hozzáférést.

Az OIDC megkönnyíti a harmadik felek alkalmazásainak a **felhasználók hitelesítését**, miközben továbbra is finom szemcsézettségű ellenőrzést tesz lehetővé afelett, hogy ezek az alkalmazások mely erőforrásokhoz férhetnek hozzá.

### 3. **SAML (Security Assertion Markup Language)**

A **SAML** egy régebbi, XML-alapú szabvány, amelyet hitelesítési és jogosultsági adatok cseréjére használnak felek között, különösen **egyszeri bejelentkezési (Single Sign-On, SSO)** forgatókönyvekben. Elsősorban vállalati környezetben használják, hogy a felhasználók egyszer hitelesítsék magukat, és több alkalmazáshoz férjenek hozzá a hitelesítő adatok újbóli megadása nélkül.

- **Folyamat**: A felhasználó először egy identitásszolgáltatónál (IdP) hitelesíti magát. Az IdP aláírt **SAML-állítást (assertion)** hoz létre, amely tartalmazza a felhasználó identitását és kapcsolódó attribútumait. Az állítást elküldik a szolgáltatónak (SP), amely ezt használja az alkalmazáshoz való hozzáférés engedélyezésére.
- **Példa**: Egy alkalmazott bejelentkezik a vállalati portálra (IdP), és automatikusan bejelentkezik más rendszerekbe, mint az e-mail, CRM stb., a hitelesítő adatok újbóli megadása nélkül. A hitelesítési folyamat az IdP által küldött SAML-állításon alapul.

A SAML-t gyakran használják **vállalati SSO-megoldásokban**, és jól működik vállalati környezetek webalkalmazásaihoz, de kevésbé mobilbarát, mint az OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

A **WS-Federation** egy másik protokoll az **egyszeri bejelentkezéshez (SSO)**, különösen Microsoft-alapú vállalati környezetekben. A **WS-* (Web Services)** specifikációcsalád része, és lehetővé teszi az identitások föderálását különböző biztonsági tartományok között (például különböző szervezetek vagy különböző szolgáltatások között).

- **Folyamat**: A WS-Federation lehetővé teszi, hogy egy **megbízható identitásszolgáltató (IdP)** hitelesítse a felhasználókat, és tokeneket adjon ki, amelyeket a szolgáltató jogosultságkezelésre használhat. Hasonló a SAML-hez, de gyakran használják olyan forgatókönyvekben, amelyek erősen támaszkodnak a Microsoft technológiáira.
- **Példa**: Egy felhasználó bejelentkezik egy Microsoft Azure Active Directory (AD) által üzemeltetett vállalati alkalmazásba, és az identitása felhasználható más föderált szolgáltatások, köztük harmadik fél szállítók által üzemeltetett alkalmazások eléréséhez.

Bár a WS-Federationt sok modern webes környezetben nagyrészt felváltották újabb protokollok, mint az OAuth 2.0 és az OpenID Connect, még mindig használják régi rendszerekben, különösen Microsoft-központú vállalatoknál.

### 5. **LDAP (Lightweight Directory Access Protocol)**

Az **LDAP** egy protokoll, amelyet címtárszolgáltatások elérésére és kezelésére használnak, általában **felhasználói hitelesítő adatok tárolására** és a hozzáférés-vezérlés kezelésére egy központosított címtárban (amelyet gyakran **címtárszolgáltatásnak** neveznek). Az LDAP nem kifejezetten a hitelesítésről vagy a jogosultságkezelésről szól, hanem identitásadatok tárolására és lekérdezésére szolgál, amelyeket aztán ezekben a folyamatokban használnak.

- **Hitelesítés**: Az LDAP lehetővé teszi, hogy egy alkalmazás hitelesítse a felhasználókat azáltal, hogy lekérdezi a címtárszolgáltatást a hitelesítő adatokról (például jelszavakról).
- **Jogosultságkezelés**: Kezeli a felhasználói szerepköröket és engedélyeket is, segítve annak megállapítását, hogy egy felhasználó hozzáfér-e bizonyos erőforrásokhoz.
- **Példa**: Sok vállalat használ LDAP-alapú címtárakat (pl. **Active Directory**) hitelesítésre és jogosultságkezelésre, különösen Windows-környezetekben.

Az LDAP létfontosságú a vállalatok számára a felhasználói hozzáférés kezeléséhez a belső rendszerekben, de modern webes kontextusban az LDAP-t gyakran integrálják más protokollokkal, például a SAML-lel vagy az OAuth-tal a teljesebb identitáskezelés érdekében.

### 6. **Közösségi SSO-szolgáltatók**

A közösségi **egyszeri bejelentkezési (SSO)** szolgáltatók, mint a **Facebook**, a **Google**, a **Twitter**, a **GitHub** és mások lehetővé teszik a felhasználóknak, hogy közösségi média hitelesítő adataikkal hitelesítsék magukat harmadik fél alkalmazásaiban. Ez az **OAuth-alapú hitelesítés** egy típusa, ahol a harmadik fél szolgáltatása (pl. a Google) az identitásszolgáltató.

- **Folyamat**: A felhasználó rákattint a „Bejelentkezés Google-lal” gombra (például). Az alkalmazás átirányít a Google-hoz, ahol a felhasználó bejelentkezik (ha még nincs bejelentkezve). A Google ezután hozzáférési tokent vagy azonosító tokent ad a harmadik fél alkalmazásának, amely felhasználható a felhasználó hitelesítésére és esetleg az adataihoz való hozzáférésre.
- **Példa**: Sok alkalmazás lehetővé teszi, hogy Google- vagy Facebook-hitelesítő adataival jelentkezzen be. Az alkalmazás a háttérben OAuth-ot vagy OpenID Connectet használ az identitása ellenőrzésére, és bizonyos esetekben bizonyos közösségimédia-adatokhoz való hozzáférésre.

A közösségi SSO kényelmes és széles körben elterjedt hitelesítési módszer, mert csökkenti a súrlódást a felhasználók számára, akik esetleg nem akarnak újabb felhasználónevet és jelszót létrehozni.

---

### A különbségek összefoglalója:

- **OAuth**: Jogosultságkezelésre használják, lehetővé teszi harmadik fél alkalmazásainak, hogy hozzáférjenek a felhasználó adataihoz a hitelesítő adatok felfedése nélkül.
- **OpenID Connect**: Kiterjeszti az OAuth-ot hitelesítés biztosítására, lehetővé téve az alkalmazásoknak a felhasználó identitásának ellenőrzését.
- **SAML**: XML-alapú protokoll SSO-hoz, gyakran vállalati környezetben.
- **WS-Federation**: Microsoft-specifikus protokoll identitásföderációhoz, régi rendszerekben használják.
- **LDAP**: Protokoll címtárszolgáltatások lekérdezésére a felhasználók hitelesítéséhez és a jogosultságkezelés kezeléséhez.
- **Közösségi SSO-szolgáltatók**: OAuth-alapú rendszerek (mint a Google, Facebook), amelyek lehetővé teszik harmadik fél alkalmazásainak a felhasználók hitelesítését közösségi média hitelesítő adataikkal.

Ezeknek a technológiáknak mindegyike megvan a maga erőssége és felhasználási esete, és a modern alkalmazásokban a biztonság különböző szempontjaihoz ezek kombinációját láthatja (pl. OAuth/OIDC az API-hozzáféréshez, SAML a vállalati SSO-hoz).
