# Zapis arhitekturne odluke: mogućnosti autentifikacije i autorizacije

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Autentifikacija i autorizacija web aplikacija dva su ključna koncepta u zaštiti pristupa aplikacijama i uslugama. Oba se bave identitetom korisnika i načinom na koji se dodjeljuju dopuštenja, ali usredotočena su na različite aspekte:

- **Autentifikacija** je postupak provjere identiteta korisnika ili sustava.
- **Autorizacija** je postupak određivanja kojim resursima ili radnjama autentificirani korisnik ili sustav može pristupiti.

Sada zaronimo u specifične protokole i tehnologije koje ste spomenuli, a koje se uobičajeno koriste u modernim web aplikacijama za upravljanje autentifikacijom i autorizacijom.

### 1. **OAuth (Open Authorization)**

**OAuth** je otvoreni standard za autorizaciju. Omogućuje korisniku da aplikaciji treće strane dodijeli ograničen pristup svojim resursima bez dijeljenja svojih vjerodajnica. Ključna ideja je **delegirani pristup**. OAuth se često koristi u situacijama u kojima se korisnici mogu prijaviti u uslugu treće strane (npr. prijava putem Googlea) bez izravnog davanja korisničkog imena i lozinke trećoj strani.

- **Tijek**: OAuth obično slijedi **tijek temeljen na tokenima**, u kojem autorizacijski poslužitelj izdaje pristupni token aplikaciji treće strane. Taj token predstavlja korisnikova dopuštenja, a aplikacija ga koristi za pristup korisnikovim podacima ili resursima putem API-ja.
- **Primjer**: Korisnik se prijavljuje u aplikaciju treće strane svojim Google računom. Google provjerava identitet korisnika, a zatim dodjeljuje token koji aplikaciji treće strane omogućuje pristup nekim Googleovim podacima (npr. Google Calendar).

OAuth **ne** obrađuje izravno autentifikaciju; riječ je o dodjeli pristupa. Za autentifikaciju se OAuth često kombinira s drugim protokolima, poput **OpenID Connecta**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** je sloj identiteta izgrađen na vrhu **OAuth 2.0** koji dodaje autentifikaciju autorizacijskim mogućnostima OAutha. U biti, OpenID Connect proširuje OAuth kako bi obrađivao **autentifikaciju korisnika** i pruža standardiziran način na koji aplikacije provjeravaju identitet korisnika.

- **Tijek**: Kada se korisnik prijavljuje putem OpenID Connecta, aplikacija treće strane zahtijeva ID token (uz OAuth pristupni token). ID token sadrži informacije o korisniku (poput korisničkog imena, e-pošte i drugih tvrdnji). To aplikaciji omogućuje da zna tko je korisnik i je li autentificiran.
- **Primjer**: Prijava u uslugu poput Slacka vašim Google računom (Google je pružatelj OpenID Connecta) uključuje autentifikaciju putem OpenID Connecta, dok OAuth upravlja pristupom vašim Google resursima.

OIDC olakšava aplikacijama trećih strana da **autentificiraju korisnike**, a pritom i dalje omogućuje precizno upravljanje time kojim resursima te aplikacije mogu pristupiti.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** je stariji standard temeljen na XML-u koji se koristi za razmjenu podataka o autentifikaciji i autorizaciji među stranama, osobito u scenarijima **jedinstvene prijave (SSO)**. Primarno se koristi u poslovnim okruženjima kako bi se korisnicima omogućilo da se autentificiraju jednom i pristupe višestrukim aplikacijama bez ponovnog unosa vjerodajnica.

- **Tijek**: Korisnik se prvo autentificira kod pružatelja identiteta (IdP). IdP generira potpisanu **SAML tvrdnju** koja uključuje identitet korisnika i povezane atribute. Tvrdnja se šalje pružatelju usluge (SP), koji je koristi za odobravanje pristupa aplikaciji.
- **Primjer**: Zaposlenik se prijavljuje u svoj korporativni portal (IdP) i automatski je prijavljen u druge sustave poput e-pošte, CRM-a itd., bez ponovnog unosa vjerodajnica. Postupak autentifikacije temelji se na SAML tvrdnji koju šalje IdP.

SAML se obično koristi u **poslovnim SSO rješenjima** i dobro radi za web aplikacije u korporativnim okruženjima, ali je manje prilagođen mobilnim uređajima u usporedbi s OAuthom/OIDC-om.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** je još jedan protokol koji se koristi za **jedinstvenu prijavu (SSO)**, osobito u poslovnim okruženjima temeljenima na Microsoftu. Dio je obitelji specifikacija **WS-* (Web Services)** i omogućuje federaciju identiteta među različitim sigurnosnim domenama (primjerice između različitih organizacija ili različitih usluga).

- **Tijek**: WS-Federation omogućuje **pouzdanom pružatelju identiteta (IdP)** da autentificira korisnike i izdaje tokene koje pružatelj usluge može koristiti za autorizaciju. Sličan je SAML-u, ali se često koristi u scenarijima koji se uvelike oslanjaju na Microsoftove tehnologije.
- **Primjer**: Korisnik se prijavljuje u poslovnu aplikaciju hostiranu na Microsoft Azure Active Directoryju (AD), a njegov se identitet može koristiti za pristup drugim federiranim uslugama, uključujući aplikacije koje hostiraju dobavljači trećih strana.

Iako su WS-Federation u mnogim modernim web okruženjima uglavnom zamijenili noviji protokoli poput OAuth2.0 i OpenID Connecta, još se koristi u naslijeđenim sustavima, osobito u poduzećima usmjerenima na Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** je protokol koji se koristi za pristup direktorijskim uslugama i upravljanje njima, uobičajeno za **pohranu korisničkih vjerodajnica** i upravljanje kontrolom pristupa u centraliziranom direktoriju (često zvanom **Directory Service**). LDAP nije posebno o autentifikaciji ili autorizaciji, ali se koristi za pohranu i dohvat podataka o identitetu, koji se zatim koriste u tim procesima.

- **Autentifikacija**: LDAP aplikaciji omogućuje autentifikaciju korisnika upitom direktorijske usluge za vjerodajnice (poput lozinki).
- **Autorizacija**: Također upravlja korisničkim ulogama i dopuštenjima, pomažući odrediti ima li korisnik pristup određenim resursima.
- **Primjer**: Mnoga poduzeća koriste direktorije temeljene na LDAP-u (npr. **Active Directory**) za autentifikaciju i autorizaciju, osobito unutar Windows okruženja.

LDAP je ključan za poduzeća u upravljanju korisničkim pristupom internim sustavima, ali se u modernom web kontekstu LDAP često integrira s drugim protokolima poput SAML-a ili OAutha radi cjelovitijeg upravljanja identitetom.

### 6. **Pružatelji društvenog SSO-a**

Pružatelji društvene **jedinstvene prijave (SSO)** poput **Facebooka**, **Googlea**, **Twittera**, **GitHuba** i drugih omogućuju korisnicima autentifikaciju u aplikacijama trećih strana pomoću vjerodajnica društvenih mreža. To je vrsta **autentifikacije temeljene na OAuthu** u kojoj je usluga treće strane (npr. Google) pružatelj identiteta.

- **Tijek**: Korisnik klikne „Prijava putem Googlea“ (na primjer). Aplikacija preusmjerava na Google, gdje se korisnik prijavljuje (ako već nije prijavljen). Google zatim aplikaciji treće strane daje pristupni token ili ID token, koji se može koristiti za autentifikaciju korisnika i eventualni pristup njegovim podacima.
- **Primjer**: Mnoge aplikacije omogućuju prijavu vjerodajnicama za Google ili Facebook. Aplikacija iza kulisa koristi OAuth ili OpenID Connect za provjeru vašeg identiteta i, u nekim slučajevima, pristup određenim podacima društvenih mreža.

Društveni SSO prikladna je i široko prihvaćena metoda autentifikacije jer smanjuje trenje za korisnike, koji možda ne žele stvarati još jedno korisničko ime i lozinku.

---

### Sažetak razlika:

- **OAuth**: Koristi se za autorizaciju, omogućuje aplikacijama trećih strana pristup korisničkim podacima bez otkrivanja vjerodajnica.
- **OpenID Connect**: Proširuje OAuth radi pružanja autentifikacije, omogućujući aplikacijama provjeru identiteta korisnika.
- **SAML**: Protokol temeljen na XML-u koji se koristi za SSO, često u poslovnim okruženjima.
- **WS-Federation**: Protokol specifičan za Microsoft za federaciju identiteta, koji se koristi u naslijeđenim sustavima.
- **LDAP**: Protokol za upite direktorijskim uslugama radi autentifikacije korisnika i upravljanja autorizacijom.
- **Pružatelji društvenog SSO-a**: Sustavi temeljeni na OAuthu (poput Googlea, Facebooka) koji omogućuju aplikacijama trećih strana autentifikaciju korisnika pomoću vjerodajnica društvenih mreža.

Svaka od ovih tehnologija ima svoje prednosti i slučajeve uporabe, a u modernim aplikacijama možete vidjeti kombinaciju njih koja se koristi za različite aspekte sigurnosti (npr. OAuth/OIDC za pristup API-ju, SAML za poslovni SSO).