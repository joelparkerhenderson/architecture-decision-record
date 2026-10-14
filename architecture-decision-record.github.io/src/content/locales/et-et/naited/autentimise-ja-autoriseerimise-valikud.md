# Arhitektuuriotsuse kirje: autentimise ja autoriseerimise valikud

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Veebirakenduste autentimine ja autoriseerimine on kaks olulist mõistet rakendustele ja teenustele juurdepääsu kaitsmisel. Mõlemad käsitlevad kasutajate identiteeti ja seda, kuidas õigusi antakse, kuid keskenduvad erinevatele aspektidele:

- **Autentimine** on kasutaja või süsteemi identiteedi kontrollimise protsess.
- **Autoriseerimine** on protsess, mis määrab, millistele ressurssidele või tegevustele autenditud kasutajal või süsteemil on juurdepääs.

Süveneme nüüd konkreetsetesse protokollidesse ja tehnoloogiatesse, mida mainisid ja mida kasutatakse tänapäevastes veebirakendustes sageli autentimise ja autoriseerimise haldamiseks.

### 1. **OAuth (Open Authorization)**

**OAuth** on autoriseerimise avatud standard. See võimaldab kasutajal anda kolmanda osapoole rakendusele piiratud juurdepääsu oma ressurssidele ilma oma volitusi jagamata. Põhiidee on **delegeeritud juurdepääs**. OAuth-i kasutatakse sageli olukordades, kus kasutajad saavad sisse logida kolmanda osapoole teenusesse (nt Google'iga sisselogimine), andmata oma kasutajanime ja parooli otse kolmandale osapoolele.

- **Voog**: OAuth järgib tavaliselt **tokenipõhist** voogu, kus autoriseerimisserver väljastab kolmanda osapoole rakendusele juurdepääsutokeni. See token esindab kasutaja õigusi ja rakendus kasutab seda kasutaja andmetele või ressurssidele juurdepääsuks API kaudu.
- **Näide**: kasutaja logib kolmanda osapoole rakendusse sisse oma Google'i kontoga. Google kontrollib kasutaja identiteeti ja annab seejärel tokeni, mis võimaldab kolmanda osapoole rakendusel pääseda ligi mõnele Google'i andmele (nt Google'i kalender).

OAuth **ei** tegele autentimisega otse; see käsitleb juurdepääsu andmist. Autentimiseks seotakse OAuth sageli teiste protokollidega, nagu **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** on **OAuth 2.0** peale ehitatud identiteedikiht, mis lisab OAuth-i autoriseerimisvõimalustele autentimise. Sisuliselt laiendab OpenID Connect OAuth-i **kasutaja autentimise** käsitlemiseks ja pakub rakendustele standardiseeritud viisi kasutaja identiteedi kontrollimiseks.

- **Voog**: kui kasutaja logib sisse OpenID Connectiga, taotleb kolmanda osapoole rakendus ID-tokenit (lisaks OAuth-i juurdepääsutokenile). ID-token sisaldab teavet kasutaja kohta (nagu kasutajanimi, e-post ja muud väited). See võimaldab rakendusel teada, kes kasutaja on ja kas ta on autenditud.
- **Näide**: teenusesse nagu Slack sisselogimine oma Google'i kontoga (Google on OpenID Connecti pakkuja) hõlmab autentimist OpenID Connecti kaudu, samal ajal kui OAuth haldab juurdepääsu sinu Google'i ressurssidele.

OIDC teeb kolmanda osapoole rakendustel **kasutajate autentimise** lihtsamaks, võimaldades samas täpset kontrolli selle üle, millistele ressurssidele need rakendused ligi pääsevad.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** on vanem XML-põhine standard autentimis- ja autoriseerimisandmete vahetamiseks osapoolte vahel, eriti **ühekordse sisselogimise (SSO)** stsenaariumides. Seda kasutatakse peamiselt ettevõttekeskkondades, et kasutajad saaksid autentida üks kord ja pääseda ligi mitmele rakendusele ilma volitusi uuesti sisestamata.

- **Voog**: kasutaja autendib kõigepealt identiteedipakkuja (IdP) juures. IdP genereerib allkirjastatud **SAML-i väite**, mis sisaldab kasutaja identiteeti ja seotud atribuute. Väide saadetakse teenusepakkujale (SP), kes kasutab seda rakendusele juurdepääsu autoriseerimiseks.
- **Näide**: töötaja logib sisse oma ettevõtte portaali (IdP) ja logitakse automaatselt sisse teistesse süsteemidesse nagu e-post, CRM jne, ilma volitusi uuesti sisestamata. Autentimisprotsess põhineb IdP saadetud SAML-i väitel.

SAML-i kasutatakse tavaliselt **ettevõtte SSO lahendustes** ja see töötab hästi veebirakenduste jaoks ettevõttekeskkondades, kuid on OAuth/OIDC-ga võrreldes vähem mobiilisõbralik.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** on veel üks **ühekordse sisselogimise (SSO)** protokoll, eriti Microsofti-põhistes ettevõttekeskkondades. See kuulub **WS-* (Web Services)** spetsifikatsioonide perekonda ja võimaldab identiteedi föderatsiooni erinevate turvadomeenide vahel (nt erinevate organisatsioonide või erinevate teenuste vahel).

- **Voog**: WS-Federation lubab **usaldusväärsel identiteedipakkujal (IdP)** kasutajaid autentida ja väljastada tokeneid, mida teenusepakkuja saab autoriseerimiseks kasutada. See sarnaneb SAML-iga, kuid seda kasutatakse sageli stsenaariumides, mis toetuvad tugevalt Microsofti tehnoloogiatele.
- **Näide**: kasutaja logib sisse Microsoft Azure Active Directory (AD) hostitud ettevõtterakendusse ja tema identiteeti saab kasutada teistele föderatiivsetele teenustele juurdepääsuks, sealhulgas kolmandate osapoolte tarnijate hostitud rakendustele.

Kuigi WS-Federation on paljudes kaasaegsetes veebikeskkondades suuresti asendatud uuemate protokollidega nagu OAuth2.0 ja OpenID Connect, kasutatakse seda endiselt pärandsüsteemides, eriti Microsoftile keskendunud ettevõtetes.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** on protokoll kataloogiteenustele juurdepääsuks ja nende haldamiseks, mida kasutatakse tavaliselt **kasutajavolituste salvestamiseks** ja juurdepääsukontrolli haldamiseks tsentraliseeritud kataloogis (sageli nimetatud **Directory Service**). LDAP ei ole spetsiifiliselt autentimise ega autoriseerimise kohta, vaid seda kasutatakse identiteediandmete salvestamiseks ja kättesaamiseks, mida seejärel nendes protsessides kasutatakse.

- **Autentimine**: LDAP võimaldab rakendusel kasutajaid autentida, päringuga kataloogiteenusele volituste (nagu paroolid) järele.
- **Autoriseerimine**: see haldab ka kasutajarolle ja õigusi, aidates kindlaks teha, kas kasutajal on juurdepääs teatud ressurssidele.
- **Näide**: paljud ettevõtted kasutavad autentimiseks ja autoriseerimiseks LDAP-põhiseid katalooge (nt **Active Directory**), eriti Windowsi keskkondades.

LDAP on ettevõtetele sisesüsteemide kasutajate juurdepääsu haldamiseks ülioluline, kuid kaasaegses veebikontekstis integreeritakse LDAP sageli teiste protokollidega nagu SAML või OAuth täielikumaks identiteedihalduseks.

### 6. **Sotsiaalse SSO pakkujad**

Sotsiaalse **ühekordse sisselogimise (SSO)** pakkujad nagu **Facebook**, **Google**, **Twitter**, **GitHub** ja teised võimaldavad kasutajatel end kolmanda osapoole rakendustes autentida oma sotsiaalmeedia volitustega. See on omamoodi **OAuth-põhine autentimine**, kus kolmanda osapoole teenus (nt Google) on identiteedipakkuja.

- **Voog**: kasutaja klõpsab (näiteks) "Logi sisse Google'iga". Rakendus suunab Google'isse, kus kasutaja logib sisse (kui ta pole veel sisse logitud). Google annab seejärel kolmanda osapoole rakendusele juurdepääsutokeni või ID-tokeni, mida saab kasutada kasutaja autentimiseks ja võib-olla tema andmetele juurdepääsuks.
- **Näide**: paljud rakendused lasevad sul sisse logida oma Google'i või Facebooki volitustega. Rakendus kasutab kulisside taga OAuth-i või OpenID Connecti sinu identiteedi kontrollimiseks ja mõnel juhul teatud sotsiaalmeedia andmetele juurdepääsuks.

Sotsiaalne SSO on mugav ja laialt omaks võetud autentimismeetod, kuna see vähendab hõõrdumist kasutajate jaoks, kes ei pruugi tahta luua veel ühte kasutajanime ja parooli.

---

### Erinevuste kokkuvõte:

- **OAuth**: kasutatakse autoriseerimiseks, võimaldab kolmanda osapoole rakendustel pääseda ligi kasutaja andmetele volitusi paljastamata.
- **OpenID Connect**: laiendab OAuth-i autentimisega, võimaldades rakendustel kasutaja identiteeti kontrollida.
- **SAML**: XML-põhine protokoll SSO jaoks, sageli ettevõttekeskkondades.
- **WS-Federation**: Microsoftile spetsiifiline protokoll identiteedi föderatsiooniks, kasutatakse pärandsüsteemides.
- **LDAP**: protokoll kataloogiteenuste päringuteks kasutajate autentimiseks ja autoriseerimise haldamiseks.
- **Sotsiaalse SSO pakkujad**: OAuth-põhised süsteemid (nagu Google, Facebook), mis võimaldavad kolmanda osapoole rakendustel kasutajaid autentida nende sotsiaalmeedia volitustega.

Igal neist tehnoloogiatest on oma tugevused ja kasutusjuhud ning kaasaegsetes rakendustes võib näha nende kombinatsiooni kasutamist turvalisuse erinevate aspektide jaoks (nt OAuth/OIDC API juurdepääsuks, SAML ettevõtte SSO jaoks).
