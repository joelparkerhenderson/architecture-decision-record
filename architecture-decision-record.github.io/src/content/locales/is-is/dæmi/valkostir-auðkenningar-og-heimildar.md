# Arkitektúrákvörðunarskrá: valkostir auðkenningar og heimildar

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Auðkenning og heimild í vefforritum eru tvö lykilhugtök við að tryggja aðgang að forritum og þjónustum. Bæði snúast um auðkenni notenda og hvernig heimildir eru veittar, en þau beinast að ólíkum þáttum:

- **Auðkenning** (authentication) er ferlið við að sannreyna auðkenni notanda eða kerfis.
- **Heimild** (authorization) er ferlið við að ákvarða hvaða auðlindum eða aðgerðum auðkenndur notandi eða kerfi hefur aðgang að.

Nú skulum við kafa í tilteknu samskiptareglurnar og tæknina sem þú nefndir, og eru algengar í nútíma vefforritum til að stýra auðkenningu og heimild.

### 1. **OAuth (Open Authorization)**

**OAuth** er opinn staðall fyrir heimild. Hann gerir notanda kleift að veita forriti þriðja aðila takmarkaðan aðgang að auðlindum sínum án þess að deila skilríkjum sínum. Lykilhugmyndin er **framseldur aðgangur**. OAuth er oft notað þar sem notendur geta skráð sig inn hjá þjónustu þriðja aðila (t.d. innskráning með Google) án þess að gefa þriðja aðilanum beint upp notandanafn sitt og lykilorð.

- **Flæði**: OAuth fylgir yfirleitt **tákn-byggðu** flæði, þar sem heimildarþjónn gefur út aðgangstákn til forrits þriðja aðila. Þetta tákn táknar heimildir notandans og forritið notar það til að nálgast gögn eða auðlindir notandans úr API.
- **Dæmi**: Notandi skráir sig inn í forrit þriðja aðila með Google-reikningi sínum. Google sannreynir auðkenni notandans og veitir síðan tákn sem leyfir forriti þriðja aðila að nálgast einhver Google-gögn (t.d. Google Calendar).

OAuth sér **ekki** um auðkenningu beint; það snýst um að veita aðgang. Fyrir auðkenningu er OAuth oft parað við aðrar samskiptareglur, eins og **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** er auðkennislag byggt ofan á **OAuth 2.0** sem bætir auðkenningu við heimildargetu OAuth. Í meginatriðum víkkar OpenID Connect OAuth út til að sjá um **auðkenningu notenda** og veitir stöðluð leið fyrir forrit til að sannreyna auðkenni notanda.

- **Flæði**: Þegar notandi skráir sig inn með OpenID Connect biður forrit þriðja aðila um auðkennistákn (ID token) til viðbótar við OAuth-aðgangstáknið. Auðkennistáknið inniheldur upplýsingar um notandann (svo sem notandanafn, netfang og aðrar fullyrðingar). Þetta gerir forritinu kleift að vita hver notandinn er og hvort hann er auðkenndur.
- **Dæmi**: Innskráning í þjónustu eins og Slack með Google-reikningi (Google er OpenID Connect veitan) felur í sér auðkenningu með OpenID Connect, en OAuth stýrir aðgangi að Google-auðlindum þínum.

OIDC auðveldar forritum þriðja aðila að **auðkenna notendur** en leyfir samt nákvæma stjórn á því hvaða auðlindum þessi forrit hafa aðgang að.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** er eldri, XML-byggður staðall sem notaður er til að skiptast á auðkenningar- og heimildargögnum milli aðila, einkum í **einskiptisinnskráningar** (Single Sign-On, SSO) sviðsmyndum. Hann er aðallega notaður í fyrirtækjaumhverfi til að gera notendum kleift að auðkenna sig einu sinni og fá aðgang að mörgum forritum án þess að slá inn skilríki aftur.

- **Flæði**: Notandinn auðkennir sig fyrst hjá auðkennisveitu (IdP). IdP býr til undirritaða **SAML-fullyrðingu** sem inniheldur auðkenni notandans og tengd eigindi. Fullyrðingin er send til þjónustuveitunnar (SP), sem notar hana til að heimila aðgang að forritinu.
- **Dæmi**: Starfsmaður skráir sig inn á fyrirtækjagátt sína (IdP) og er sjálfkrafa skráður inn í önnur kerfi eins og tölvupóst, CRM o.fl., án þess að slá inn skilríki aftur. Auðkenningarferlið byggir á SAML-fullyrðingunni sem IdP sendir.

SAML er algengt í **SSO-lausnum fyrir fyrirtæki** og hentar vel fyrir vefforrit í fyrirtækjaumhverfi, en er síður farsímavænt en OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** er önnur samskiptaregla sem notuð er fyrir **einskiptisinnskráningu (SSO)**, einkum í fyrirtækjaumhverfi byggðu á Microsoft. Hún er hluti af **WS-* (Web Services)** fjölskyldu forskrifta og leyfir auðkennissamband milli ólíkra öryggissviða (svo sem milli ólíkra stofnana eða milli ólíkra þjónusta).

- **Flæði**: WS-Federation leyfir **traustum auðkennisveitum (IdP)** að auðkenna notendur og gefa út tákn sem þjónustuveitan getur notað til heimildar. Hún er svipuð SAML en er oft notuð í sviðsmyndum sem reiða sig mikið á Microsoft-tækni.
- **Dæmi**: Notandi skráir sig inn í fyrirtækjaforrit hýst á Microsoft Azure Active Directory (AD), og auðkenni hans má nota til að nálgast aðra sambandsþjónustu, þar á meðal forrit hýst hjá söluaðilum þriðja aðila.

Þótt WS-Federation hafi að mestu verið leyst af hólmi af nýrri samskiptareglum eins og OAuth2.0 og OpenID Connect í mörgu nútíma vefumhverfi er hún enn notuð í eldri kerfum, einkum í fyrirtækjum sem snúast um Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** er samskiptaregla notuð til að nálgast og stýra möppuþjónustu, algeng til að **geyma skilríki notenda** og stýra aðgangsstýringu í miðlægri möppu (oft kölluð **möppuþjónusta**, Directory Service). LDAP snýst ekki sérstaklega um auðkenningu eða heimild heldur er notað til að geyma og sækja auðkennisgögn, sem eru síðan notuð í þeim ferlum.

- **Auðkenning**: LDAP leyfir forriti að auðkenna notendur með því að fyrirspyrja möppuþjónustuna um skilríki (eins og lykilorð).
- **Heimild**: Það stýrir einnig hlutverkum og heimildum notenda og hjálpar til við að ákvarða hvort notandi hafi aðgang að tilteknum auðlindum.
- **Dæmi**: Mörg fyrirtæki nota LDAP-byggðar möppur (t.d. **Active Directory**) fyrir auðkenningu og heimild, einkum í Windows-umhverfi.

LDAP er mikilvægt fyrir fyrirtæki til að stýra aðgangi notenda að innri kerfum, en í nútíma vefsamhengi er LDAP oft samþætt öðrum samskiptareglum eins og SAML eða OAuth fyrir fyllri auðkennisstjórnun.

### 6. **Veitur félagslegrar einskiptisinnskráningar (Social SSO)**

Veitur félagslegrar **einskiptisinnskráningar (SSO)** eins og **Facebook**, **Google**, **Twitter**, **GitHub** og aðrar leyfa notendum að auðkenna sig í forritum þriðja aðila með skilríkjum sínum af samfélagsmiðlum. Þetta er tegund **OAuth-byggðrar auðkenningar** þar sem þjónusta þriðja aðila (t.d. Google) er auðkennisveitan.

- **Flæði**: Notandinn smellir á „Skrá inn með Google“ (til dæmis). Forritið vísar yfir til Google, þar sem notandinn skráir sig inn (ef hann er ekki þegar innskráður). Google veitir síðan aðgangstákn eða auðkennistákn til forrits þriðja aðila, sem hægt er að nota til að auðkenna notandann og mögulega nálgast gögn hans.
- **Dæmi**: Mörg forrit leyfa þér að skrá þig inn með Google- eða Facebook-skilríkjum. Forritið mun nota OAuth eða OpenID Connect á bak við tjöldin til að sannreyna auðkenni þitt og í sumum tilvikum nálgast tiltekin gögn af samfélagsmiðlum.

Félagsleg SSO er þægileg og víða tekin upp aðferð við auðkenningu því hún dregur úr núningi hjá notendum, sem vilja kannski ekki búa til enn eitt notandanafn og lykilorð.

---

### Samantekt á mismun:

- **OAuth**: Notað fyrir heimild, leyfir forritum þriðja aðila að nálgast gögn notenda án þess að afhjúpa skilríki.
- **OpenID Connect**: Víkkar OAuth út til að veita auðkenningu, sem gerir forritum kleift að sannreyna auðkenni notanda.
- **SAML**: XML-byggð samskiptaregla notuð fyrir SSO, oft í fyrirtækjaumhverfi.
- **WS-Federation**: Samskiptaregla sértæk fyrir Microsoft um auðkennissamband, notuð í eldri kerfum.
- **LDAP**: Samskiptaregla til að fyrirspyrja möppuþjónustu til að auðkenna notendur og stýra heimildum.
- **Veitur félagslegrar SSO**: OAuth-byggð kerfi (eins og Google, Facebook) sem leyfa forritum þriðja aðila að auðkenna notendur með skilríkjum þeirra af samfélagsmiðlum.

Hver þessara tækni hefur sína styrkleika og notkunartilvik, og í nútímaforritum gætirðu séð blöndu þeirra notaða fyrir ólíka þætti öryggis (t.d. OAuth/OIDC fyrir API-aðgang, SAML fyrir SSO í fyrirtækjum).
