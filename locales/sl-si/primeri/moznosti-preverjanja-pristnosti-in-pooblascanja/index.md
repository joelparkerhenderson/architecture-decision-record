# Zapis arhitekturne odločitve: možnosti preverjanja pristnosti in pooblaščanja

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Preverjanje pristnosti (authentication) in pooblaščanje (authorization) v spletnih aplikacijah sta dva ključna koncepta pri zavarovanju dostopa do aplikacij in storitev. Oba se nanašata na identiteto uporabnikov in na to, kako se dodeljujejo dovoljenja, vendar se osredotočata na različne vidike:

- **Preverjanje pristnosti** je postopek preverjanja identitete uporabnika ali sistema.
- **Pooblaščanje** je postopek ugotavljanja, do katerih virov ali dejanj lahko preverjeni uporabnik ali sistem dostopa.

Zdaj se poglobimo v posamezne protokole in tehnologije, ki ste jih omenili in ki se pogosto uporabljajo v sodobnih spletnih aplikacijah za upravljanje preverjanja pristnosti in pooblaščanja.

### 1. **OAuth (Open Authorization)**

**OAuth** je odprt standard za pooblaščanje. Uporabniku omogoča, da aplikaciji tretje osebe odobri omejen dostop do svojih virov, ne da bi delil svojih poverilnic. Ključna zamisel je **delegiran dostop**. OAuth se pogosto uporablja v primerih, ko se uporabniki lahko prijavijo v storitev tretje osebe (npr. prijava z Googlom), ne da bi tretji osebi neposredno posredovali uporabniško ime in geslo.

- **Potek**: OAuth običajno sledi poteku, **temelječem na žetonih**, kjer strežnik za pooblaščanje izda dostopni žeton aplikaciji tretje osebe. Ta žeton predstavlja uporabnikova dovoljenja, aplikacija pa ga uporabi za dostop do uporabnikovih podatkov ali virov prek API.
- **Primer**: Uporabnik se v aplikacijo tretje osebe prijavi s svojim računom Google. Google preveri uporabnikovo identiteto in nato odobri žeton, ki aplikaciji tretje osebe omogoča dostop do nekaterih podatkov Googla (npr. Google Koledarja).

OAuth **ne** obravnava preverjanja pristnosti neposredno; gre za dodeljevanje dostopa. Za preverjanje pristnosti se OAuth pogosto združuje z drugimi protokoli, kot je **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** je identitetna plast, zgrajena na **OAuth 2.0**, ki k zmožnostim pooblaščanja OAuth dodaja preverjanje pristnosti. V bistvu OpenID Connect razširja OAuth, da obravnava **preverjanje pristnosti uporabnikov**, in aplikacijam zagotavlja standardiziran način za preverjanje identitete uporabnika.

- **Potek**: Ko se uporabnik prijavi z OpenID Connect, aplikacija tretje osebe (poleg dostopnega žetona OAuth) zahteva žeton ID. Žeton ID vsebuje informacije o uporabniku (kot so uporabniško ime, e-pošta in druge trditve). To aplikaciji omogoča, da ve, kdo je uporabnik in ali je preverjen.
- **Primer**: Prijava v storitev, kot je Slack, z računom Google (Google je ponudnik OpenID Connect) vključuje preverjanje pristnosti prek OpenID Connect, medtem ko OAuth upravlja dostop do vaših virov Google.

OIDC aplikacijam tretjih oseb olajša **preverjanje pristnosti uporabnikov**, hkrati pa še vedno omogoča natančen nadzor nad tem, do katerih virov lahko te aplikacije dostopajo.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** je starejši standard, ki temelji na XML in se uporablja za izmenjavo podatkov o preverjanju pristnosti in pooblaščanju med stranmi, zlasti v scenarijih **enotne prijave (Single Sign-On, SSO)**. Uporablja se predvsem v podjetniških okoljih, da se lahko uporabniki preverijo enkrat in dostopajo do več aplikacij, ne da bi znova vnašali poverilnice.

- **Potek**: Uporabnik se najprej preveri pri ponudniku identitete (IdP). IdP ustvari podpisano **trditev SAML**, ki vključuje uporabnikovo identiteto in sorodne atribute. Trditev se pošlje ponudniku storitve (SP), ki jo uporabi za pooblastitev dostopa do aplikacije.
- **Primer**: Zaposleni se prijavi v svoj podjetniški portal (IdP) in je samodejno prijavljen v druge sisteme, kot so e-pošta, CRM itd., ne da bi znova vnašal poverilnice. Postopek preverjanja pristnosti temelji na trditvi SAML, ki jo pošlje IdP.

SAML se pogosto uporablja v **podjetniških rešitvah SSO** in dobro deluje za spletne aplikacije v podjetniških okoljih, vendar je v primerjavi z OAuth/OIDC manj prijazen do mobilnih naprav.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** je še en protokol, ki se uporablja za **enotno prijavo (SSO)**, zlasti v podjetniških okoljih, ki temeljijo na Microsoftu. Je del družine specifikacij **WS-* (Web Services)** in omogoča federacijo identitet med različnimi varnostnimi domenami (na primer med različnimi organizacijami ali med različnimi storitvami).

- **Potek**: WS-Federation omogoča **zaupanja vrednemu ponudniku identitete (IdP)**, da preveri uporabnike in izda žetone, ki jih ponudnik storitve lahko uporabi za pooblaščanje. Je podoben SAML, vendar se pogosto uporablja v scenarijih, ki se močno zanašajo na tehnologije Microsoft.
- **Primer**: Uporabnik se prijavi v podjetniško aplikacijo, ki jo gosti Microsoft Azure Active Directory (AD), njegova identiteta pa se lahko uporabi za dostop do drugih federiranih storitev, vključno z aplikacijami, ki jih gostijo zunanji ponudniki.

Čeprav so WS-Federation v mnogih sodobnih spletnih okoljih večinoma nadomestili novejši protokoli, kot sta OAuth2.0 in OpenID Connect, se še vedno uporablja v podedovanih sistemih, zlasti v podjetjih, osredotočenih na Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** je protokol, ki se uporablja za dostop do imeniških storitev in njihovo upravljanje; pogosto se uporablja za **shranjevanje poverilnic uporabnikov** in upravljanje nadzora dostopa v osrednjem imeniku (pogosto imenovanem **imeniška storitev**). LDAP se ne nanaša posebej na preverjanje pristnosti ali pooblaščanje, temveč se uporablja za shranjevanje in pridobivanje podatkov o identiteti, ki se nato uporabijo v teh postopkih.

- **Preverjanje pristnosti**: LDAP aplikaciji omogoča preverjanje pristnosti uporabnikov s poizvedovanjem imeniške storitve za poverilnice (kot so gesla).
- **Pooblaščanje**: Upravlja tudi uporabniške vloge in dovoljenja ter pomaga ugotoviti, ali ima uporabnik dostop do določenih virov.
- **Primer**: Mnoga podjetja uporabljajo imenike, ki temeljijo na LDAP (npr. **Active Directory**), za preverjanje pristnosti in pooblaščanje, zlasti v okoljih Windows.

LDAP je za podjetja ključen pri upravljanju uporabniškega dostopa v notranjih sistemih, vendar je v sodobnem spletnem kontekstu LDAP pogosto integriran z drugimi protokoli, kot sta SAML ali OAuth, za popolnejše upravljanje identitet.

### 6. **Ponudniki družabne SSO**

Ponudniki družabne **enotne prijave (SSO)**, kot so **Facebook**, **Google**, **Twitter**, **GitHub** in drugi, uporabnikom omogočajo preverjanje pristnosti v aplikacijah tretjih oseb z njihovimi poverilnicami družabnih omrežij. To je vrsta **preverjanja pristnosti, ki temelji na OAuth**, kjer je storitev tretje osebe (npr. Google) ponudnik identitete.

- **Potek**: Uporabnik klikne »Prijava z Googlom« (na primer). Aplikacija preusmeri na Google, kjer se uporabnik prijavi (če še ni prijavljen). Google nato aplikaciji tretje osebe zagotovi dostopni žeton ali žeton ID, ki ga je mogoče uporabiti za preverjanje pristnosti uporabnika in morda dostop do njegovih podatkov.
- **Primer**: Mnoge aplikacije omogočajo prijavo s poverilnicami Google ali Facebook. Aplikacija v ozadju uporabi OAuth ali OpenID Connect za preverjanje vaše identitete in v nekaterih primerih za dostop do določenih podatkov družabnih omrežij.

Družabna SSO je priročen in široko sprejet način preverjanja pristnosti, ker zmanjšuje trenje za uporabnike, ki morda ne želijo ustvariti še enega uporabniškega imena in gesla.

---

### Povzetek razlik:

- **OAuth**: Uporablja se za pooblaščanje, aplikacijam tretjih oseb omogoča dostop do uporabniških podatkov brez razkritja poverilnic.
- **OpenID Connect**: Razširja OAuth, da zagotavlja preverjanje pristnosti in aplikacijam omogoča preverjanje identitete uporabnika.
- **SAML**: Protokol, ki temelji na XML in se uporablja za SSO, pogosto v podjetniških okoljih.
- **WS-Federation**: Protokol, specifičen za Microsoft, za federacijo identitet, uporabljen v podedovanih sistemih.
- **LDAP**: Protokol za poizvedovanje po imeniških storitvah za preverjanje pristnosti uporabnikov in upravljanje pooblaščanja.
- **Ponudniki družabne SSO**: Sistemi, ki temeljijo na OAuth (kot sta Google, Facebook) in aplikacijam tretjih oseb omogočajo preverjanje pristnosti uporabnikov z njihovimi poverilnicami družabnih omrežij.

Vsaka od teh tehnologij ima svoje prednosti in primere uporabe, v sodobnih aplikacijah pa lahko opazite njihovo kombinacijo za različne vidike varnosti (npr. OAuth/OIDC za dostop do API, SAML za podjetniški SSO).
