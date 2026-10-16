# Arhitektūras lēmuma ieraksts: autentifikācijas un autorizācijas iespējas

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Tīmekļa lietojumprogrammu autentifikācija un autorizācija ir divi svarīgi jēdzieni piekļuves nodrošināšanā lietojumprogrammām un pakalpojumiem. Abi attiecas uz lietotāju identitāti un to, kā tiek piešķirtas atļaujas, taču tie koncentrējas uz dažādiem aspektiem:

- **Autentifikācija** ir lietotāja vai sistēmas identitātes pārbaudes process.
- **Autorizācija** ir process, kurā nosaka, kuriem resursiem vai darbībām autentificētais lietotājs vai sistēma var piekļūt.

Tagad iedziļināsimies konkrētajos protokolos un tehnoloģijās, ko minējāt un kuras parasti izmanto mūsdienu tīmekļa lietojumprogrammās autentifikācijas un autorizācijas pārvaldībai.

### 1. **OAuth (Open Authorization)**

**OAuth** ir atvērts autorizācijas standarts. Tas ļauj lietotājam piešķirt trešās puses lietojumprogrammai ierobežotu piekļuvi saviem resursiem, nekopīgojot savus akreditācijas datus. Galvenā ideja ir **deleģēta piekļuve**. OAuth bieži izmanto situācijās, kad lietotāji var pieteikties trešās puses pakalpojumā (piemēram, pieteikšanās ar Google), tieši nesniedzot trešajai pusei savu lietotājvārdu un paroli.

- **Plūsma**: OAuth parasti seko uz **marķieriem** balstītai plūsmai, kurā autorizācijas serveris izsniedz piekļuves marķieri trešās puses lietojumprogrammai. Šis marķieris atspoguļo lietotāja atļaujas, un lietojumprogramma to izmanto, lai piekļūtu lietotāja datiem vai resursiem no API.
- **Piemērs**: lietotājs piesakās trešās puses lietotnē ar savu Google kontu. Google pārbauda lietotāja identitāti un pēc tam piešķir marķieri, kas ļauj trešās puses lietotnei piekļūt dažiem Google datiem (piemēram, Google kalendāram).

OAuth **neapstrādā** autentifikāciju tieši; tas ir par piekļuves piešķiršanu. Autentifikācijai OAuth bieži tiek savienots ar citiem protokoliem, piemēram, **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** ir identitātes slānis, kas veidots virs **OAuth 2.0** un pievieno autentifikāciju OAuth autorizācijas iespējām. Būtībā OpenID Connect paplašina OAuth, lai apstrādātu **lietotāju autentifikāciju**, un nodrošina standartizētu veidu, kā lietojumprogrammas var pārbaudīt lietotāja identitāti.

- **Plūsma**: kad lietotājs piesakās, izmantojot OpenID Connect, trešās puses lietojumprogramma pieprasa ID marķieri (papildus OAuth piekļuves marķierim). ID marķieris satur informāciju par lietotāju (piemēram, lietotājvārdu, e-pastu un citus apgalvojumus). Tas ļauj lietojumprogrammai zināt, kas ir lietotājs un vai viņš ir autentificēts.
- **Piemērs**: pieteikšanās tādā pakalpojumā kā Slack ar jūsu Google kontu (Google ir OpenID Connect nodrošinātājs) ietver autentifikāciju, izmantojot OpenID Connect, savukārt OAuth pārvalda piekļuvi jūsu Google resursiem.

OIDC trešo pušu lietotnēm atvieglo **lietotāju autentifikāciju**, vienlaikus saglabājot precīzu kontroli pār to, kuriem resursiem šīs lietotnes var piekļūt.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** ir vecāks, uz XML balstīts standarts, ko izmanto autentifikācijas un autorizācijas datu apmaiņai starp pusēm, īpaši **vienotās pieteikšanās (Single Sign-On, SSO)** scenārijos. To galvenokārt izmanto uzņēmumu vidēs, lai lietotāji varētu autentificēties vienreiz un piekļūt vairākām lietojumprogrammām, atkārtoti neievadot akreditācijas datus.

- **Plūsma**: lietotājs vispirms autentificējas pie identitātes nodrošinātāja (IdP). IdP ģenerē parakstītu **SAML apgalvojumu**, kas ietver lietotāja identitāti un saistītos atribūtus. Apgalvojums tiek nosūtīts pakalpojuma nodrošinātājam (SP), kas to izmanto, lai autorizētu piekļuvi lietojumprogrammai.
- **Piemērs**: darbinieks piesakās savā korporatīvajā portālā (IdP) un tiek automātiski pieteikts citās sistēmās, piemēram, e-pastā, CRM utt., atkārtoti neievadot akreditācijas datus. Autentifikācijas process balstās uz SAML apgalvojumu, ko nosūta IdP.

SAML parasti izmanto **uzņēmumu SSO risinājumos**, un tas labi darbojas tīmekļa lietojumprogrammām korporatīvajās vidēs, taču tas ir mazāk piemērots mobilajām ierīcēm salīdzinājumā ar OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** ir vēl viens protokols, ko izmanto **vienotajai pieteikšanai (SSO)**, īpaši uz Microsoft balstītās uzņēmumu vidēs. Tas ir daļa no **WS-* (Web Services)** specifikāciju saimes un ļauj veikt identitāšu federāciju starp dažādiem drošības domēniem (piemēram, starp dažādām organizācijām vai dažādiem pakalpojumiem).

- **Plūsma**: WS-Federation ļauj **uzticamam identitātes nodrošinātājam (IdP)** autentificēt lietotājus un izsniegt marķierus, ko pakalpojuma nodrošinātājs var izmantot autorizācijai. Tas ir līdzīgs SAML, taču bieži tiek izmantots scenārijos, kas lielā mērā balstās uz Microsoft tehnoloģijām.
- **Piemērs**: lietotājs piesakās uzņēmuma lietojumprogrammā, ko mitina Microsoft Azure Active Directory (AD), un viņa identitāti var izmantot, lai piekļūtu citiem federētiem pakalpojumiem, tostarp lietojumprogrammām, ko mitina trešo pušu piegādātāji.

Lai gan daudzās mūsdienu tīmekļa vidēs WS-Federation lielā mērā ir aizstājuši jaunāki protokoli, piemēram, OAuth2.0 un OpenID Connect, to joprojām izmanto mantotajās sistēmās, īpaši uz Microsoft orientētos uzņēmumos.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** ir protokols, ko izmanto, lai piekļūtu direktoriju pakalpojumiem un tos pārvaldītu, parasti **lietotāju akreditācijas datu glabāšanai** un piekļuves kontroles pārvaldībai centralizētā direktorijā (bieži saukta par **direktoriju pakalpojumu**). LDAP nav īpaši par autentifikāciju vai autorizāciju, bet tiek izmantots identitātes datu glabāšanai un izgūšanai, ko pēc tam izmanto šajos procesos.

- **Autentifikācija**: LDAP ļauj lietojumprogrammai autentificēt lietotājus, vaicājot direktoriju pakalpojumam pēc akreditācijas datiem (piemēram, parolēm).
- **Autorizācija**: tas pārvalda arī lietotāju lomas un atļaujas, palīdzot noteikt, vai lietotājam ir piekļuve noteiktiem resursiem.
- **Piemērs**: daudzi uzņēmumi izmanto uz LDAP balstītus direktorijus (piemēram, **Active Directory**) autentifikācijai un autorizācijai, īpaši Windows vidēs.

LDAP ir būtisks uzņēmumiem, lai pārvaldītu lietotāju piekļuvi iekšējām sistēmām, taču mūsdienu tīmekļa kontekstā LDAP bieži tiek integrēts ar citiem protokoliem, piemēram, SAML vai OAuth, pilnīgākai identitātes pārvaldībai.

### 6. **Sociālo tīklu SSO nodrošinātāji**

Sociālo tīklu **vienotās pieteikšanās (SSO)** nodrošinātāji, piemēram, **Facebook**, **Google**, **Twitter**, **GitHub** un citi, ļauj lietotājiem autentificēties trešo pušu lietojumprogrammās, izmantojot savus sociālo mediju akreditācijas datus. Šis ir **uz OAuth balstītas autentifikācijas** veids, kurā trešās puses pakalpojums (piemēram, Google) ir identitātes nodrošinātājs.

- **Plūsma**: lietotājs noklikšķina uz „Pieteikties ar Google” (piemēram). Lietotne novirza uz Google, kur lietotājs piesakās (ja vēl nav pieteicies). Pēc tam Google nodrošina piekļuves marķieri vai ID marķieri trešās puses lietotnei, ko var izmantot lietotāja autentificēšanai un, iespējams, piekļuvei viņa datiem.
- **Piemērs**: daudzas lietotnes ļauj pieteikties, izmantojot jūsu Google vai Facebook akreditācijas datus. Lietotne fonā izmantos OAuth vai OpenID Connect, lai pārbaudītu jūsu identitāti un dažos gadījumos piekļūtu noteiktiem sociālo mediju datiem.

Sociālo tīklu SSO ir ērta un plaši pieņemta autentifikācijas metode, jo tā samazina berzi lietotājiem, kuri, iespējams, nevēlas veidot vēl vienu lietotājvārdu un paroli.

---

### Atšķirību kopsavilkums:

- **OAuth**: izmanto autorizācijai, ļauj trešo pušu lietotnēm piekļūt lietotāja datiem, neatklājot akreditācijas datus.
- **OpenID Connect**: paplašina OAuth, lai nodrošinātu autentifikāciju, ļaujot lietotnēm pārbaudīt lietotāja identitāti.
- **SAML**: uz XML balstīts protokols, ko izmanto SSO, bieži uzņēmumu vidēs.
- **WS-Federation**: Microsoft specifisks protokols identitāšu federācijai, ko izmanto mantotajās sistēmās.
- **LDAP**: protokols direktoriju pakalpojumu vaicāšanai, lai autentificētu lietotājus un pārvaldītu autorizāciju.
- **Sociālo tīklu SSO nodrošinātāji**: uz OAuth balstītas sistēmas (piemēram, Google, Facebook), kas ļauj trešo pušu lietotnēm autentificēt lietotājus, izmantojot viņu sociālo mediju akreditācijas datus.

Katrai no šīm tehnoloģijām ir savas stiprās puses un lietošanas gadījumi, un mūsdienu lietojumprogrammās var redzēt to kombināciju dažādiem drošības aspektiem (piemēram, OAuth/OIDC API piekļuvei, SAML uzņēmuma SSO).
