# Záznam architektonického rozhodnutia: možnosti autentifikácie a autorizácie

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Autentifikácia a autorizácia webových aplikácií sú dva kľúčové koncepty pri zabezpečení prístupu k aplikáciám a službám. Obe sa zaoberajú identitou používateľov a spôsobom udeľovania oprávnení, ale zameriavajú sa na rôzne aspekty:

- **Autentifikácia** je proces overenia identity používateľa alebo systému.
- **Autorizácia** je proces určenia, ku ktorým zdrojom alebo akciám môže autentifikovaný používateľ alebo systém pristupovať.

Teraz sa ponorme do konkrétnych protokolov a technológií, ktoré ste spomenuli a ktoré sa bežne používajú v moderných webových aplikáciách na správu autentifikácie a autorizácie.

### 1. **OAuth (Open Authorization)**

**OAuth** je otvorený štandard pre autorizáciu. Umožňuje používateľovi udeliť aplikácii tretej strany obmedzený prístup k svojim zdrojom bez zdieľania svojich prihlasovacích údajov. Kľúčovou myšlienkou je **delegovaný prístup**. OAuth sa často používa v situáciách, keď sa používatelia môžu prihlásiť do služby tretej strany (napr. prihlásenie cez Google) bez priameho poskytnutia používateľského mena a hesla tretej strane.

- **Tok**: OAuth zvyčajne sleduje **tok založený na tokenoch**, pri ktorom autorizačný server vydá prístupový token aplikácii tretej strany. Tento token predstavuje oprávnenia používateľa a aplikácia ho používa na prístup k údajom alebo zdrojom používateľa z API.
- **Príklad**: Používateľ sa prihlási do aplikácie tretej strany svojím účtom Google. Google overí identitu používateľa a potom udelí token, ktorý aplikácii tretej strany umožňuje prístup k niektorým údajom Google (napr. Google Calendar).

OAuth **nerieši** autentifikáciu priamo; ide o udeľovanie prístupu. Na autentifikáciu sa OAuth často spája s inými protokolmi, ako je **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** je vrstva identity vybudovaná nad **OAuth 2.0**, ktorá pridáva autentifikáciu k autorizačným schopnostiam OAuth. V podstate OpenID Connect rozširuje OAuth o spracovanie **autentifikácie používateľa** a poskytuje štandardizovaný spôsob, ako aplikácie overujú identitu používateľa.

- **Tok**: Keď sa používateľ prihlasuje cez OpenID Connect, aplikácia tretej strany si vyžiada ID token (okrem prístupového tokenu OAuth). ID token obsahuje informácie o používateľovi (ako je jeho používateľské meno, e-mail a ďalšie tvrdenia). To aplikácii umožňuje vedieť, kto je používateľ a či je autentifikovaný.
- **Príklad**: Prihlásenie do služby ako Slack pomocou vášho účtu Google (Google je poskytovateľ OpenID Connect) zahŕňa autentifikáciu cez OpenID Connect, zatiaľ čo OAuth spravuje prístup k vašim zdrojom Google.

OIDC uľahčuje aplikáciám tretích strán **autentifikovať používateľov** a zároveň umožňuje jemné riadenie toho, ku ktorým zdrojom tieto aplikácie môžu pristupovať.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** je starší štandard založený na XML, ktorý sa používa na výmenu autentifikačných a autorizačných údajov medzi stranami, najmä v scenároch **jednotného prihlásenia (SSO)**. Používa sa predovšetkým v podnikových prostrediach, aby sa používatelia mohli autentifikovať raz a pristupovať k viacerým aplikáciám bez opätovného zadávania prihlasovacích údajov.

- **Tok**: Používateľ sa najprv autentifikuje u poskytovateľa identity (IdP). IdP vygeneruje podpísané **SAML tvrdenie**, ktoré zahŕňa identitu používateľa a súvisiace atribúty. Tvrdenie sa odošle poskytovateľovi služby (SP), ktorý ho použije na autorizáciu prístupu k aplikácii.
- **Príklad**: Zamestnanec sa prihlási do svojho firemného portálu (IdP) a automaticky je prihlásený do ďalších systémov ako e-mail, CRM atď. bez opätovného zadávania prihlasovacích údajov. Proces autentifikácie je založený na SAML tvrdení odoslanom IdP.

SAML sa bežne používa v **podnikových riešeniach SSO** a funguje dobre pre webové aplikácie vo firemných prostrediach, ale je menej vhodný pre mobilné zariadenia v porovnaní s OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** je ďalší protokol používaný pre **jednotné prihlásenie (SSO)**, najmä v podnikových prostrediach založených na Microsofte. Je súčasťou rodiny špecifikácií **WS-* (Web Services)** a umožňuje federáciu identít naprieč rôznymi bezpečnostnými doménami (napríklad medzi rôznymi organizáciami alebo medzi rôznymi službami).

- **Tok**: WS-Federation umožňuje **dôveryhodnému poskytovateľovi identity (IdP)** autentifikovať používateľov a vydávať tokeny, ktoré môže poskytovateľ služby použiť na autorizáciu. Je podobný SAML, ale často sa používa v scenároch, ktoré sa vo veľkej miere spoliehajú na technológie Microsoftu.
- **Príklad**: Používateľ sa prihlási do podnikovej aplikácie hostovanej v Microsoft Azure Active Directory (AD) a jeho identitu možno použiť na prístup k ďalším federovaným službám vrátane aplikácií hostovaných dodávateľmi tretích strán.

Hoci WS-Federation v mnohých moderných webových prostrediach z veľkej časti nahradili novšie protokoly ako OAuth2.0 a OpenID Connect, stále sa používa v starších systémoch, najmä v podnikoch zameraných na Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** je protokol používaný na prístup k adresárovým službám a ich správu, bežne používaný na **ukladanie prihlasovacích údajov používateľov** a správu riadenia prístupu v centralizovanom adresári (často nazývanom **Directory Service**). LDAP nie je konkrétne o autentifikácii ani autorizácii, ale používa sa na ukladanie a získavanie údajov o identite, ktoré sa potom používajú v týchto procesoch.

- **Autentifikácia**: LDAP umožňuje aplikácii autentifikovať používateľov dopytovaním adresárovej služby na prihlasovacie údaje (ako sú heslá).
- **Autorizácia**: Spravuje aj používateľské roly a oprávnenia, čo pomáha určiť, či má používateľ prístup k určitým zdrojom.
- **Príklad**: Mnoho podnikov používa adresáre založené na LDAP (napr. **Active Directory**) na autentifikáciu a autorizáciu, najmä v prostrediach Windows.

LDAP je pre podniky kľúčový pri správe prístupu používateľov k interným systémom, ale v modernom webovom kontexte sa LDAP často integruje s inými protokolmi, ako sú SAML alebo OAuth, pre úplnejšiu správu identít.

### 6. **Poskytovatelia sociálneho SSO**

Poskytovatelia sociálneho **jednotného prihlásenia (SSO)** ako **Facebook**, **Google**, **Twitter**, **GitHub** a ďalší umožňujú používateľom autentifikovať sa v aplikáciách tretích strán pomocou prihlasovacích údajov sociálnych sietí. Ide o druh **autentifikácie založenej na OAuth**, kde je poskytovateľom identity služba tretej strany (napr. Google).

- **Tok**: Používateľ klikne na „Prihlásiť sa cez Google“ (napríklad). Aplikácia presmeruje na Google, kde sa používateľ prihlási (ak ešte nie je prihlásený). Google potom poskytne aplikácii tretej strany prístupový token alebo ID token, ktorý možno použiť na autentifikáciu používateľa a prípadne na prístup k jeho údajom.
- **Príklad**: Mnohé aplikácie vám umožňujú prihlásiť sa pomocou vašich prihlasovacích údajov Google alebo Facebook. Aplikácia na pozadí použije OAuth alebo OpenID Connect na overenie vašej identity a v niektorých prípadoch na prístup k určitým údajom zo sociálnych sietí.

Sociálne SSO je pohodlná a široko prijatá metóda autentifikácie, pretože znižuje trenie pre používateľov, ktorí si možno nechcú vytvárať ďalšie používateľské meno a heslo.

---

### Zhrnutie rozdielov:

- **OAuth**: Používa sa na autorizáciu, umožňuje aplikáciám tretích strán pristupovať k údajom používateľov bez odhalenia prihlasovacích údajov.
- **OpenID Connect**: Rozširuje OAuth o poskytovanie autentifikácie, čím umožňuje aplikáciám overovať identitu používateľa.
- **SAML**: Protokol založený na XML používaný pre SSO, často v podnikových prostrediach.
- **WS-Federation**: Protokol špecifický pre Microsoft na federáciu identít, používaný v starších systémoch.
- **LDAP**: Protokol na dopytovanie adresárových služieb na autentifikáciu používateľov a správu autorizácie.
- **Poskytovatelia sociálneho SSO**: Systémy založené na OAuth (ako Google, Facebook), ktoré umožňujú aplikáciám tretích strán autentifikovať používateľov pomocou ich prihlasovacích údajov zo sociálnych sietí.

Každá z týchto technológií má svoje silné stránky a prípady použitia a v moderných aplikáciách môžete vidieť ich kombináciu používanú pre rôzne aspekty bezpečnosti (napr. OAuth/OIDC pre prístup k API, SAML pre podnikové SSO).