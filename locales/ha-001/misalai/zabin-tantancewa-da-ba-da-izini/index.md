# Rikodin shawarar gine-gine: zaɓuɓɓukan tantancewa da ba da izini

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Tantance aikace-aikacen yanar gizo (authentication) da ba da izini (authorization) ra’ayoyi ne guda biyu masu muhimmanci wajen tabbatar da samun damar aikace-aikace da ayyuka. Dukansu suna magana ne kan ainihin masu amfani da yadda ake ba da izini, amma suna mai da hankali kan fannoni daban-daban:

- **Tantancewa** shi ne tsarin tabbatar da ainihin mai amfani ko tsari.
- **Ba da izini** shi ne tsarin tantance waɗanne albarkatu ko ayyuka mai amfani ko tsarin da aka tantance zai iya samun dama.

Yanzu, bari mu nutse cikin takamaiman ƙa’idodin sadarwa da fasahohin da kuka ambata, waɗanda ake amfani da su sosai a aikace-aikacen yanar gizo na zamani don sarrafa tantancewa da ba da izini.

### 1. **OAuth (Open Authorization)**

**OAuth** ma’auni ne na buɗe don ba da izini. Yana ba mai amfani damar ba aikace-aikacen wani kamfani iyakantaccen damar shiga albarkatunsa ba tare da raba bayanan shigarsa ba. Babban ra’ayin shi ne **samun damar wakilci**. Ana amfani da OAuth sau da yawa a yanayi da masu amfani za su iya shiga sabis na wani kamfani (misali, shiga da Google) ba tare da ba wannan kamfani sunan mai amfani da kalmar sirrinsu kai tsaye ba.

- **Kwarara**: OAuth yawanci yana bin kwarara ta **tushen token**, inda sabar ba da izini ke bayar da token na samun dama ga aikace-aikacen wani kamfani. Wannan token yana wakiltar izinin mai amfani, kuma aikace-aikacen yana amfani da shi don samun bayanan mai amfani ko albarkatunsa daga API.
- **Misali**: Mai amfani yana shiga aikace-aikacen wani kamfani da asusunsa na Google. Google yana tabbatar da ainihin mai amfani sannan ya ba da token wanda ke ba aikace-aikacen wani kamfani damar samun wasu bayanan Google (misali, Google Calendar).

OAuth **ba ya** sarrafa tantancewa kai tsaye; yana game da ba da damar shiga ne. Don tantancewa, ana haɗa OAuth sau da yawa da wasu ƙa’idodin sadarwa, kamar **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** yadin ainihi ne da aka gina a kan **OAuth 2.0** wanda ke ƙara tantancewa ga iyawar ba da izini ta OAuth. A taƙaice, OpenID Connect yana faɗaɗa OAuth don sarrafa **tantance mai amfani** kuma yana ba da hanyar ma’auni ga aikace-aikace don tabbatar da ainihin mai amfani.

- **Kwarara**: Lokacin da mai amfani ke shiga ta amfani da OpenID Connect, aikace-aikacen wani kamfani yana neman token na ID (ban da token na samun dama na OAuth). Token na ID yana ɗauke da bayani game da mai amfani (kamar sunan mai amfani, imel, da sauran da’awa). Wannan yana ba aikace-aikacen damar sanin wanene mai amfani da ko an tantance shi.
- **Misali**: Shiga sabis kamar Slack ta amfani da asusun Google (Google shi ne mai samar da OpenID Connect) ya ƙunshi tantancewa ta OpenID Connect, yayin da OAuth ke sarrafa damar shiga albarkatun Google ɗinku.

OIDC yana sauƙaƙa wa aikace-aikacen wasu kamfanoni **tantance masu amfani** yayin da yake ci gaba da ba da damar sarrafa dalla-dalla kan waɗanne albarkatu waɗannan aikace-aikacen za su iya samun dama.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** tsoho ne, ma’auni na tushen XML da ake amfani da shi don musayar bayanan tantancewa da ba da izini tsakanin ɓangarori, musamman a yanayin **Single Sign-On (SSO)**. Ana amfani da shi galibi a muhallin kamfanoni don ba masu amfani damar tantancewa sau ɗaya su sami damar shiga aikace-aikace da yawa ba tare da sake shigar da bayanai ba.

- **Kwarara**: Mai amfani yana tantancewa da farko tare da mai samar da ainihi (IdP). IdP yana samar da **SAML assertion** mai sa hannu wanda ya haɗa da ainihin mai amfani da halayen da suka shafe shi. Ana aika assertion zuwa mai samar da sabis (SP), wanda ke amfani da shi don ba da izinin shiga aikace-aikacen.
- **Misali**: Ma’aikaci yana shiga tashar kamfaninsa (IdP) kuma ana shigar da shi ta atomatik cikin sauran tsarukan kamar imel, CRM, da sauransu, ba tare da sake shigar da bayanai ba. Tsarin tantancewa yana dogara ne kan assertion na SAML da IdP ya aika.

Ana amfani da SAML sosai a **mafitar SSO ta kamfanoni** kuma yana aiki da kyau ga aikace-aikacen yanar gizo a muhallin kamfanoni, amma ba shi da sauƙin amfani a wayar hannu idan aka kwatanta da OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** wata ƙa’idar sadarwa ce da ake amfani da ita don **Single Sign-On (SSO)**, musamman a muhallin kamfanoni na tushen Microsoft. Yana cikin iyalin ƙayyadaddun bayanai na **WS-* (Web Services)** kuma yana ba da damar haɗakar ainihi tsakanin yankunan tsaro daban-daban (kamar tsakanin ƙungiyoyi daban-daban ko tsakanin sabis daban-daban).

- **Kwarara**: WS-Federation yana ba **mai samar da ainihi amintacce (IdP)** damar tantance masu amfani da bayar da tokens waɗanda mai samar da sabis zai iya amfani da su don ba da izini. Yana kama da SAML amma ana amfani da shi sau da yawa a yanayin da ke dogara sosai kan fasahohin Microsoft.
- **Misali**: Mai amfani yana shiga aikace-aikacen kamfani da ake ɗauka a Microsoft Azure Active Directory (AD), kuma ana iya amfani da ainihinsa don samun damar shiga wasu sabis da aka haɗa, ciki har da aikace-aikacen da masu sayarwa na wasu kamfanoni ke ɗauka.

Ko da yake sababbin ƙa’idodin sadarwa kamar OAuth2.0 da OpenID Connect sun maye gurbin WS-Federation a muhallin yanar gizo na zamani da yawa, har yanzu ana amfani da shi a tsoffin tsarukan, musamman a kamfanonin da suka mai da hankali kan Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** ƙa’idar sadarwa ce da ake amfani da ita don samun dama da sarrafa sabis na kundin adireshi, wadda ake amfani da ita sosai don **adana bayanan shigar masu amfani** da sarrafa ikon shiga a kundin adireshi na tsakiya (wanda ake kira **Sabis na Kundin Adireshi** sau da yawa). LDAP ba musamman game da tantancewa ko ba da izini ba ne amma ana amfani da shi don adanawa da dawo da bayanan ainihi, waɗanda ake amfani da su a waɗannan tsare-tsare.

- **Tantancewa**: LDAP yana ba aikace-aikace damar tantance masu amfani ta hanyar tambayar sabis na kundin adireshi don bayanan shigarsu (kamar kalmomin sirri).
- **Ba da izini**: Yana kuma sarrafa matsayi da izinin masu amfani, yana taimakawa wajen tantance ko mai amfani yana da damar shiga wasu albarkatu.
- **Misali**: Kamfanoni da yawa suna amfani da kundin adireshi na tushen LDAP (misali, **Active Directory**) don tantancewa da ba da izini, musamman a muhallin Windows.

LDAP yana da muhimmanci ga kamfanoni wajen sarrafa damar masu amfani a tsarukan cikin gida, amma a yanayin yanar gizo na zamani, ana haɗa LDAP sau da yawa da wasu ƙa’idodin sadarwa kamar SAML ko OAuth don cikakken sarrafa ainihi.

### 6. **Masu Samar da Social SSO**

Masu samar da **Single Sign-On (SSO)** na zamantakewa kamar **Facebook**, **Google**, **Twitter**, **GitHub**, da sauransu suna ba masu amfani damar tantancewa a aikace-aikacen wasu kamfanoni ta amfani da bayanan shigar kafafen sada zumunta. Wannan wani nau’in **tantancewa ne na tushen OAuth** inda sabis na wani kamfani (misali, Google) shi ne mai samar da ainihi.

- **Kwarara**: Mai amfani yana danna “Shiga da Google” (misali). Aikace-aikacen yana tura zuwa Google, inda mai amfani ke shiga (idan bai riga ya shiga ba). Daga nan Google yana ba da token na samun dama ko token na ID ga aikace-aikacen wani kamfani, wanda za a iya amfani da shi don tantance mai amfani kuma wataƙila a sami bayanansa.
- **Misali**: Aikace-aikace da yawa suna ba ku damar shiga ta amfani da bayanan shigar Google ko Facebook. Aikace-aikacen zai yi amfani da OAuth ko OpenID Connect a bayan fage don tabbatar da ainihinku kuma, a wasu lokuta, ya sami damar shiga wasu bayanan kafafen sada zumunta.

Social SSO hanya ce mai sauƙi kuma wadda aka karɓa sosai don tantancewa domin tana rage cikas ga masu amfani, waɗanda wataƙila ba sa son ƙirƙirar wani sunan mai amfani da kalmar sirri.

---

### Taƙaitaccen Bambance-bambance:

- **OAuth**: Ana amfani da shi don ba da izini, yana ba aikace-aikacen wasu kamfanoni damar samun bayanan mai amfani ba tare da bayyana bayanan shiga ba.
- **OpenID Connect**: Yana faɗaɗa OAuth don ba da tantancewa, yana ba aikace-aikace damar tabbatar da ainihin mai amfani.
- **SAML**: Ƙa’idar sadarwa ta tushen XML da ake amfani da ita don SSO, sau da yawa a muhallin kamfanoni.
- **WS-Federation**: Ƙa’idar sadarwa ta musamman ta Microsoft don haɗakar ainihi, ana amfani da ita a tsoffin tsarukan.
- **LDAP**: Ƙa’idar sadarwa don tambayar sabis na kundin adireshi don tantance masu amfani da sarrafa ba da izini.
- **Masu Samar da Social SSO**: Tsarukan tushen OAuth (kamar Google, Facebook) waɗanda ke ba aikace-aikacen wasu kamfanoni damar tantance masu amfani ta amfani da bayanan shigar kafafen sada zumuntarsu.

Kowanne daga cikin waɗannan fasahohi yana da ƙarfinsa da yanayin amfaninsa, kuma a aikace-aikacen zamani, kuna iya ganin haɗin su ana amfani da shi don fannoni daban-daban na tsaro (misali, OAuth/OIDC don samun damar API, SAML don SSO na kamfanoni).
