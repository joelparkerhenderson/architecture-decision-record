# Záznam architektonického rozhodnutí: možnosti autentizace a autorizace

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Autentizace a autorizace webových aplikací jsou dva klíčové pojmy při zabezpečení přístupu k aplikacím a službám. Oba se týkají identity uživatelů a způsobu udělování oprávnění, ale zaměřují se na různé aspekty:

- **Autentizace** (authentication) je proces ověření identity uživatele nebo systému.
- **Autorizace** (authorization) je proces určení, ke kterým zdrojům nebo akcím má autentizovaný uživatel nebo systém přístup.

Pojďme se nyní ponořit do konkrétních protokolů a technologií, které jste zmínili a které se běžně používají v moderních webových aplikacích ke správě autentizace a autorizace.

### 1. **OAuth (Open Authorization)**

**OAuth** je otevřený standard pro autorizaci. Umožňuje uživateli udělit aplikaci třetí strany omezený přístup ke svým zdrojům, aniž by sdílel své přihlašovací údaje. Klíčovou myšlenkou je **delegovaný přístup**. OAuth se často používá v situacích, kdy se uživatelé mohou přihlásit ke službě třetí strany (např. přihlášení přes Google), aniž by třetí straně přímo poskytli své uživatelské jméno a heslo.

- **Tok**: OAuth obvykle následuje tok **založený na tokenech**, kdy autorizační server vydá přístupový token aplikaci třetí strany. Tento token představuje oprávnění uživatele a aplikace jej používá k přístupu k datům nebo zdrojům uživatele z API.
- **Příklad**: Uživatel se přihlásí do aplikace třetí strany pomocí svého účtu Google. Google ověří identitu uživatele a poté vydá token, který aplikaci třetí strany umožní přístup k některým datům Google (např. Kalendář Google).

OAuth **neřeší** přímo autentizaci; jde o udělování přístupu. Pro autentizaci se OAuth často kombinuje s jinými protokoly, jako je **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** je vrstva identity postavená na **OAuth 2.0**, která k autorizačním schopnostem OAuth přidává autentizaci. OpenID Connect v podstatě rozšiřuje OAuth o řešení **autentizace uživatelů** a poskytuje standardizovaný způsob, jak mohou aplikace ověřit identitu uživatele.

- **Tok**: Když se uživatel přihlásí pomocí OpenID Connect, aplikace třetí strany požádá o token identity (ID token) (navíc k přístupovému tokenu OAuth). Token identity obsahuje informace o uživateli (například jeho uživatelské jméno, e-mail a další tvrzení). Díky tomu aplikace ví, kdo uživatel je a zda je autentizovaný.
- **Příklad**: Přihlášení ke službě, jako je Slack, pomocí vašeho účtu Google (Google je poskytovatelem OpenID Connect) zahrnuje autentizaci přes OpenID Connect, zatímco OAuth spravuje přístup k vašim zdrojům Google.

OIDC usnadňuje aplikacím třetích stran **autentizovat uživatele** a zároveň umožňuje jemně odstupňovanou kontrolu nad tím, ke kterým zdrojům tyto aplikace mohou přistupovat.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** je starší standard založený na XML, používaný k výměně autentizačních a autorizačních dat mezi stranami, zejména ve scénářích **jednotného přihlášení (Single Sign-On, SSO)**. Používá se především v podnikových prostředích, aby se uživatelé mohli autentizovat jednou a přistupovat k více aplikacím bez opětovného zadávání přihlašovacích údajů.

- **Tok**: Uživatel se nejprve autentizuje u poskytovatele identity (IdP). IdP vygeneruje podepsané **tvrzení SAML (assertion)**, které obsahuje identitu uživatele a související atributy. Tvrzení se odešle poskytovateli služby (SP), který jej použije k autorizaci přístupu k aplikaci.
- **Příklad**: Zaměstnanec se přihlásí do firemního portálu (IdP) a je automaticky přihlášen do dalších systémů, jako je e-mail, CRM atd., bez opětovného zadávání přihlašovacích údajů. Proces autentizace je založen na tvrzení SAML odeslaném IdP.

SAML se běžně používá v **podnikových řešeních SSO** a dobře funguje pro webové aplikace ve firemních prostředích, ale je méně vhodný pro mobilní zařízení než OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** je další protokol používaný pro **jednotné přihlášení (SSO)**, zejména v podnikových prostředích založených na produktech Microsoft. Je součástí rodiny specifikací **WS-* (Web Services)** a umožňuje federaci identit napříč různými bezpečnostními doménami (například mezi různými organizacemi nebo mezi různými službami).

- **Tok**: WS-Federation umožňuje **důvěryhodnému poskytovateli identity (IdP)** autentizovat uživatele a vydávat tokeny, které poskytovatel služby může použít k autorizaci. Je podobný SAML, ale často se používá ve scénářích silně závislých na technologiích Microsoft.
- **Příklad**: Uživatel se přihlásí do podnikové aplikace hostované v Microsoft Azure Active Directory (AD) a jeho identitu lze použít k přístupu k dalším federovaným službám, včetně aplikací hostovaných dodavateli třetích stran.

Přestože WS-Federation byl v mnoha moderních webových prostředích z velké části nahrazen novějšími protokoly, jako jsou OAuth 2.0 a OpenID Connect, stále se používá ve starších systémech, zejména v podnicích zaměřených na Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** je protokol používaný pro přístup k adresářovým službám a jejich správu, běžně používaný pro **ukládání přihlašovacích údajů uživatelů** a správu řízení přístupu v centralizovaném adresáři (často nazývaném **adresářová služba**). LDAP se konkrétně netýká autentizace ani autorizace, ale slouží k ukládání a načítání dat identity, která se pak v těchto procesech používají.

- **Autentizace**: LDAP umožňuje aplikaci autentizovat uživatele dotazem na adresářovou službu na přihlašovací údaje (jako jsou hesla).
- **Autorizace**: Spravuje také role a oprávnění uživatelů a pomáhá určit, zda má uživatel přístup k určitým zdrojům.
- **Příklad**: Mnoho podniků používá adresáře založené na LDAP (např. **Active Directory**) pro autentizaci a autorizaci, zejména v prostředích Windows.

LDAP je pro podniky zásadní při správě přístupu uživatelů k interním systémům, ale v moderním webovém kontextu je LDAP často integrován s jinými protokoly, jako je SAML nebo OAuth, pro úplnější správu identit.

### 6. **Poskytovatelé sociálního SSO**

Poskytovatelé sociálního **jednotného přihlášení (SSO)**, jako jsou **Facebook**, **Google**, **Twitter**, **GitHub** a další, umožňují uživatelům autentizovat se v aplikacích třetích stran pomocí přihlašovacích údajů ze sociálních sítí. Jde o typ **autentizace založené na OAuth**, kde je poskytovatelem identity služba třetí strany (např. Google).

- **Tok**: Uživatel klikne na „Přihlásit se přes Google“ (například). Aplikace přesměruje na Google, kde se uživatel přihlásí (pokud ještě není přihlášen). Google poté poskytne aplikaci třetí strany přístupový token nebo token identity, který lze použít k autentizaci uživatele a případně k přístupu k jeho datům.
- **Příklad**: Mnoho aplikací umožňuje přihlásit se pomocí přihlašovacích údajů Google nebo Facebook. Aplikace na pozadí použije OAuth nebo OpenID Connect k ověření vaší identity a v některých případech k přístupu k určitým datům ze sociálních médií.

Sociální SSO je pohodlná a široce přijímaná metoda autentizace, protože snižuje tření pro uživatele, kteří možná nechtějí vytvářet další uživatelské jméno a heslo.

---

### Shrnutí rozdílů:

- **OAuth**: Používá se pro autorizaci, umožňuje aplikacím třetích stran přistupovat k datům uživatele bez odhalení přihlašovacích údajů.
- **OpenID Connect**: Rozšiřuje OAuth o autentizaci a umožňuje aplikacím ověřovat identitu uživatele.
- **SAML**: Protokol založený na XML používaný pro SSO, často v podnikových prostředích.
- **WS-Federation**: Protokol specifický pro Microsoft pro federaci identit, používaný ve starších systémech.
- **LDAP**: Protokol pro dotazování adresářových služeb za účelem autentizace uživatelů a správy autorizace.
- **Poskytovatelé sociálního SSO**: Systémy založené na OAuth (jako Google, Facebook), které umožňují aplikacím třetích stran autentizovat uživatele pomocí jejich přihlašovacích údajů ze sociálních médií.

Každá z těchto technologií má své silné stránky a případy použití a v moderních aplikacích můžete vidět jejich kombinaci pro různé aspekty zabezpečení (např. OAuth/OIDC pro přístup k API, SAML pro podnikové SSO).
