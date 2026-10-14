# Arkkitehtuuripäätöstietue: tunnistautumisen ja valtuutuksen vaihtoehdot

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Verkkosovellusten tunnistautuminen ja valtuutus ovat kaksi ratkaisevaa käsitettä sovellusten ja palvelujen käytön suojaamisessa. Molemmat käsittelevät käyttäjien identiteettiä ja sitä, miten oikeuksia myönnetään, mutta ne keskittyvät eri näkökohtiin:

- **Tunnistautuminen** on prosessi, jossa varmennetaan käyttäjän tai järjestelmän identiteetti.
- **Valtuutus** on prosessi, jossa määritetään, mihin resursseihin tai toimintoihin tunnistautunut käyttäjä tai järjestelmä pääsee käsiksi.

Perehdytään nyt mainitsemiisi erityisiin protokolliin ja teknologioihin, joita käytetään yleisesti nykyaikaisissa verkkosovelluksissa tunnistautumisen ja valtuutuksen hallintaan.

### 1. **OAuth (Open Authorization)**

**OAuth** on avoin valtuutusstandardi. Se sallii käyttäjän antaa kolmannen osapuolen sovellukselle rajoitetun pääsyn omiin resursseihinsa jakamatta tunnistetietojaan. Keskeinen ajatus on **delegoitu pääsy**. OAuthia käytetään usein tilanteissa, joissa käyttäjät voivat kirjautua kolmannen osapuolen palveluun (esim. kirjautuminen Googlella) antamatta käyttäjätunnustaan ja salasanaansa suoraan kolmannelle osapuolelle.

- **Kulku**: OAuth noudattaa tyypillisesti **tunnisteisiin (token) perustuvaa** kulkua, jossa valtuutuspalvelin myöntää kolmannen osapuolen sovellukselle käyttöoikeustunnisteen. Tämä tunniste edustaa käyttäjän oikeuksia, ja sovellus käyttää sitä käyttäjän tietojen tai resurssien hakemiseen rajapinnasta.
- **Esimerkki**: Käyttäjä kirjautuu kolmannen osapuolen sovellukseen Google-tilillään. Google varmentaa käyttäjän identiteetin ja myöntää sitten tunnisteen, jonka avulla kolmannen osapuolen sovellus pääsee käsiksi joihinkin Google-tietoihin (esim. Google Kalenteriin).

OAuth **ei** käsittele tunnistautumista suoraan; se koskee pääsyn myöntämistä. Tunnistautumiseen OAuth yhdistetään usein muihin protokolliin, kuten **OpenID Connectiin**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** on **OAuth 2.0:n** päälle rakennettu identiteettikerros, joka lisää tunnistautumisen OAuthin valtuutusominaisuuksiin. Pohjimmiltaan OpenID Connect laajentaa OAuthia käsittelemään **käyttäjän tunnistautumista** ja tarjoaa standardoidun tavan sovelluksille varmentaa käyttäjän identiteetti.

- **Kulku**: Kun käyttäjä kirjautuu OpenID Connectilla, kolmannen osapuolen sovellus pyytää ID-tunnisteen (OAuthin käyttöoikeustunnisteen lisäksi). ID-tunniste sisältää tietoja käyttäjästä (kuten käyttäjätunnus, sähköposti ja muut väitteet). Näin sovellus tietää, kuka käyttäjä on ja onko hän tunnistautunut.
- **Esimerkki**: Palveluun, kuten Slackiin, kirjautuminen Google-tililläsi (Google on OpenID Connect -tarjoaja) tarkoittaa tunnistautumista OpenID Connectin kautta, kun taas OAuth hallitsee pääsyä Google-resursseihisi.

OIDC helpottaa kolmannen osapuolen sovellusten **käyttäjien tunnistamista** ja sallii samalla tarkan hallinnan siitä, mihin resursseihin nämä sovellukset pääsevät käsiksi.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** on vanhempi, XML-pohjainen standardi, jota käytetään tunnistautumis- ja valtuutustietojen vaihtoon osapuolten välillä, erityisesti **kertakirjautumisen (SSO)** tilanteissa. Sitä käytetään ensisijaisesti yritysympäristöissä, jotta käyttäjät voivat tunnistautua kerran ja käyttää useita sovelluksia syöttämättä tunnistetietoja uudelleen.

- **Kulku**: Käyttäjä tunnistautuu ensin identiteetintarjoajalle (IdP). IdP luo allekirjoitetun **SAML-väitteen**, joka sisältää käyttäjän identiteetin ja siihen liittyvät attribuutit. Väite lähetetään palveluntarjoajalle (SP), joka käyttää sitä sovellukseen pääsyn valtuuttamiseen.
- **Esimerkki**: Työntekijä kirjautuu yrityksensä portaaliin (IdP) ja kirjataan automaattisesti sisään muihin järjestelmiin, kuten sähköpostiin, CRM:ään jne., syöttämättä tunnistetietoja uudelleen. Tunnistautumisprosessi perustuu IdP:n lähettämään SAML-väitteeseen.

SAMLia käytetään yleisesti **yritysten SSO-ratkaisuissa**, ja se toimii hyvin yritysympäristöjen verkkosovelluksissa, mutta se on OAuthiin/OIDC:hen verrattuna vähemmän mobiiliystävällinen.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** on toinen **kertakirjautumiseen (SSO)** käytetty protokolla, erityisesti Microsoft-pohjaisissa yritysympäristöissä. Se kuuluu **WS-* (Web Services)** -määrittelyperheeseen ja mahdollistaa identiteetin federoinnin eri turvallisuusalueiden välillä (kuten eri organisaatioiden tai eri palvelujen välillä).

- **Kulku**: WS-Federation sallii **luotetun identiteetintarjoajan (IdP)** tunnistaa käyttäjät ja myöntää tunnisteita, joita palveluntarjoaja voi käyttää valtuutukseen. Se on samankaltainen kuin SAML, mutta sitä käytetään usein tilanteissa, jotka nojaavat vahvasti Microsoft-teknologioihin.
- **Esimerkki**: Käyttäjä kirjautuu Microsoft Azure Active Directoryn (AD) isännöimään yrityssovellukseen, ja hänen identiteettiään voidaan käyttää muihin federoituihin palveluihin pääsyyn, mukaan lukien kolmansien osapuolten toimittajien isännöimät sovellukset.

Vaikka uudemmat protokollat, kuten OAuth2.0 ja OpenID Connect, ovat suurelta osin korvanneet WS-Federationin monissa nykyaikaisissa verkkoympäristöissä, sitä käytetään edelleen vanhoissa järjestelmissä, erityisesti Microsoft-keskeisissä yrityksissä.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** on protokolla, jota käytetään hakemistopalvelujen käyttöön ja hallintaan, ja jota käytetään yleisesti **käyttäjien tunnistetietojen tallentamiseen** ja pääsynhallinnan hallintaan keskitetyssä hakemistossa (jota kutsutaan usein **hakemistopalveluksi**). LDAP ei varsinaisesti koske tunnistautumista tai valtuutusta, vaan sitä käytetään identiteettitietojen tallentamiseen ja hakemiseen, joita sitten käytetään näissä prosesseissa.

- **Tunnistautuminen**: LDAP sallii sovelluksen tunnistaa käyttäjät kyselemällä hakemistopalvelusta tunnistetietoja (kuten salasanoja).
- **Valtuutus**: Se hallitsee myös käyttäjien rooleja ja oikeuksia auttaen määrittämään, onko käyttäjällä pääsy tiettyihin resursseihin.
- **Esimerkki**: Monet yritykset käyttävät LDAP-pohjaisia hakemistoja (esim. **Active Directory**) tunnistautumiseen ja valtuutukseen, erityisesti Windows-ympäristöissä.

LDAP on ratkaisevan tärkeä yrityksille käyttäjien pääsyn hallinnassa sisäisissä järjestelmissä, mutta nykyaikaisessa verkkokontekstissa LDAP integroidaan usein muihin protokolliin, kuten SAMLiin tai OAuthiin, kattavamman identiteetinhallinnan saavuttamiseksi.

### 6. **Sosiaalisen median SSO-tarjoajat**

Sosiaalisen median **kertakirjautumisen (SSO)** tarjoajat, kuten **Facebook**, **Google**, **Twitter**, **GitHub** ja muut, sallivat käyttäjien tunnistautua kolmannen osapuolen sovelluksiin sosiaalisen median tunnuksillaan. Tämä on **OAuth-pohjaisen tunnistautumisen** tyyppi, jossa kolmannen osapuolen palvelu (esim. Google) on identiteetintarjoaja.

- **Kulku**: Käyttäjä napsauttaa "Kirjaudu Googlella" (esimerkiksi). Sovellus ohjaa Googleen, jossa käyttäjä kirjautuu (jos hän ei ole jo kirjautunut). Google antaa sitten kolmannen osapuolen sovellukselle käyttöoikeustunnisteen tai ID-tunnisteen, jota voidaan käyttää käyttäjän tunnistamiseen ja mahdollisesti hänen tietojensa käyttöön.
- **Esimerkki**: Monet sovellukset sallivat kirjautumisen Google- tai Facebook-tunnuksillasi. Sovellus käyttää OAuthia tai OpenID Connectia taustalla identiteettisi varmentamiseen ja joissakin tapauksissa tiettyjen sosiaalisen median tietojen käyttämiseen.

Sosiaalinen SSO on kätevä ja laajasti omaksuttu tunnistautumismenetelmä, koska se vähentää kitkaa käyttäjille, jotka eivät välttämättä halua luoda taas yhtä käyttäjätunnusta ja salasanaa.

---

### Erojen yhteenveto:

- **OAuth**: Käytetään valtuutukseen, sallii kolmannen osapuolen sovellusten käyttää käyttäjän tietoja paljastamatta tunnistetietoja.
- **OpenID Connect**: Laajentaa OAuthia tarjoamaan tunnistautumisen, jolloin sovellukset voivat varmentaa käyttäjän identiteetin.
- **SAML**: XML-pohjainen protokolla, jota käytetään SSO:hon, usein yritysympäristöissä.
- **WS-Federation**: Microsoft-kohtainen protokolla identiteetin federointiin, käytössä vanhoissa järjestelmissä.
- **LDAP**: Protokolla hakemistopalvelujen kyselyyn käyttäjien tunnistamiseksi ja valtuutuksen hallitsemiseksi.
- **Sosiaalisen median SSO-tarjoajat**: OAuth-pohjaiset järjestelmät (kuten Google, Facebook), jotka sallivat kolmannen osapuolen sovellusten tunnistaa käyttäjät heidän sosiaalisen median tunnuksillaan.

Jokaisella näistä teknologioista on omat vahvuutensa ja käyttötapauksensa, ja nykyaikaisissa sovelluksissa saatat nähdä niiden yhdistelmän käytössä turvallisuuden eri näkökohtiin (esim. OAuth/OIDC rajapintapääsyyn, SAML yritysten SSO:hon).
