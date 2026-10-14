# Rekodi ya Uamuzi wa Usanifu: chaguo za uthibitishaji na uidhinishaji

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Uthibitishaji na uidhinishaji wa programu za wavuti ni dhana mbili muhimu katika kulinda ufikiaji wa programu na huduma. Zote mbili zinahusu utambulisho wa watumiaji na jinsi ruhusa zinavyotolewa, lakini zinazingatia vipengele tofauti:

- **Uthibitishaji** (authentication) ni mchakato wa kuthibitisha utambulisho wa mtumiaji au mfumo.
- **Uidhinishaji** (authorization) ni mchakato wa kubaini ni rasilimali au vitendo gani mtumiaji au mfumo uliothibitishwa unaweza kufikia.

Sasa hebu tuzame katika itifaki na teknolojia mahsusi ulizotaja, ambazo hutumika kwa kawaida katika programu za kisasa za wavuti kusimamia uthibitishaji na uidhinishaji.

### 1. **OAuth (Open Authorization)**

**OAuth** ni kiwango huria cha uidhinishaji. Kinamruhusu mtumiaji kumpa programu ya mhusika wa tatu ufikiaji mdogo wa rasilimali zake bila kushiriki vitambulisho vyake. Wazo kuu ni **ufikiaji uliokabidhiwa**. OAuth mara nyingi hutumika katika hali ambapo watumiaji wanaweza kuingia kwenye huduma ya mhusika wa tatu (mf., kuingia na Google) bila kutoa moja kwa moja jina la mtumiaji na nenosiri lao kwa mhusika wa tatu.

- **Mtiririko**: OAuth kwa kawaida hufuata mtiririko **unaotegemea tokeni**, ambapo seva ya uidhinishaji hutoa tokeni ya ufikiaji kwa programu ya mhusika wa tatu. Tokeni hii inawakilisha ruhusa za mtumiaji, na programu huitumia kufikia data au rasilimali za mtumiaji kutoka kwa API.
- **Mfano**: Mtumiaji anaingia kwenye programu ya mhusika wa tatu kwa kutumia akaunti yake ya Google. Google huthibitisha utambulisho wa mtumiaji kisha hutoa tokeni inayoruhusu programu ya mhusika wa tatu kufikia baadhi ya data ya Google (mf., Google Calendar).

OAuth **haishughulikii** uthibitishaji moja kwa moja; ni kuhusu kutoa ufikiaji. Kwa uthibitishaji, OAuth mara nyingi huunganishwa na itifaki nyingine, kama **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** ni tabaka la utambulisho lililojengwa juu ya **OAuth 2.0** linaloongeza uthibitishaji kwenye uwezo wa uidhinishaji wa OAuth. Kimsingi, OpenID Connect hupanua OAuth kushughulikia **uthibitishaji wa mtumiaji** na hutoa njia sanifu kwa programu kuthibitisha utambulisho wa mtumiaji.

- **Mtiririko**: Mtumiaji anapoingia kwa kutumia OpenID Connect, programu ya mhusika wa tatu huomba tokeni ya kitambulisho (ID token) (pamoja na tokeni ya ufikiaji ya OAuth). Tokeni ya kitambulisho ina taarifa kuhusu mtumiaji (kama jina lake la mtumiaji, barua pepe, na madai mengine). Hii inaruhusu programu kujua mtumiaji ni nani na kama amethibitishwa.
- **Mfano**: Kuingia kwenye huduma kama Slack kwa kutumia akaunti yako ya Google (Google ikiwa mtoa OpenID Connect) kunahusisha uthibitishaji kupitia OpenID Connect, huku OAuth ikisimamia ufikiaji wa rasilimali zako za Google.

OIDC hurahisisha programu za wahusika wa tatu **kuthibitisha watumiaji** huku bado ikiruhusu udhibiti mwembamba juu ya rasilimali gani programu hizo zinaweza kufikia.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** ni kiwango cha zamani zaidi, kinachotegemea XML, kinachotumika kubadilishana data ya uthibitishaji na uidhinishaji kati ya pande, hasa katika hali za **Kuingia Mara Moja (Single Sign-On, SSO)**. Hutumika hasa katika mazingira ya biashara kuwezesha watumiaji kujithibitisha mara moja na kufikia programu nyingi bila kuingiza tena vitambulisho.

- **Mtiririko**: Mtumiaji kwanza hujithibitisha kwa mtoa utambulisho (IdP). IdP huzalisha **kauli ya SAML** iliyotiwa saini inayojumuisha utambulisho wa mtumiaji na sifa zinazohusiana. Kauli hutumwa kwa mtoa huduma (SP), anayeitumia kuidhinisha ufikiaji wa programu.
- **Mfano**: Mfanyakazi anaingia kwenye lango la kampuni yake (IdP) na anaingizwa kiotomatiki kwenye mifumo mingine kama barua pepe, CRM, n.k., bila kuingiza tena vitambulisho. Mchakato wa uthibitishaji unategemea kauli ya SAML iliyotumwa na IdP.

SAML hutumika kwa kawaida katika **suluhisho za SSO za biashara** na hufanya kazi vizuri kwa programu za wavuti katika mazingira ya kampuni, lakini si rafiki kwa simu kama OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** ni itifaki nyingine inayotumika kwa **Kuingia Mara Moja (SSO)**, hasa katika mazingira ya biashara yanayotegemea Microsoft. Ni sehemu ya familia ya vipimo ya **WS-* (Web Services)** na inaruhusu muungano wa utambulisho katika vikoa tofauti vya usalama (kama kati ya mashirika tofauti au kati ya huduma tofauti).

- **Mtiririko**: WS-Federation huruhusu **mtoa utambulisho anayeaminika (IdP)** kuthibitisha watumiaji na kutoa tokeni ambazo mtoa huduma anaweza kutumia kwa uidhinishaji. Inafanana na SAML lakini mara nyingi hutumika katika hali zinazotegemea sana teknolojia za Microsoft.
- **Mfano**: Mtumiaji anaingia kwenye programu ya biashara iliyopangishwa na Microsoft Azure Active Directory (AD), na utambulisho wake unaweza kutumika kufikia huduma nyingine zilizounganishwa, ikiwa ni pamoja na programu zilizopangishwa na wauzaji wa wahusika wa tatu.

Ingawa WS-Federation kwa kiasi kikubwa imebadilishwa na itifaki mpya kama OAuth2.0 na OpenID Connect katika mazingira mengi ya kisasa ya wavuti, bado inatumika katika mifumo ya zamani, hasa katika biashara zinazozingatia Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** ni itifaki inayotumika kufikia na kusimamia huduma za saraka, ambayo hutumika kwa kawaida **kuhifadhi vitambulisho vya watumiaji** na kusimamia udhibiti wa ufikiaji katika saraka ya kati (mara nyingi huitwa **Huduma ya Saraka**). LDAP haihusu hasa uthibitishaji au uidhinishaji lakini hutumika kuhifadhi na kupata data ya utambulisho, ambayo kisha hutumika katika michakato hiyo.

- **Uthibitishaji**: LDAP huruhusu programu kuthibitisha watumiaji kwa kuuliza huduma ya saraka vitambulisho (kama nenosiri).
- **Uidhinishaji**: Pia husimamia majukumu na ruhusa za watumiaji, ikisaidia kubaini kama mtumiaji ana ufikiaji wa rasilimali fulani.
- **Mfano**: Biashara nyingi hutumia saraka zinazotegemea LDAP (mf., **Active Directory**) kwa uthibitishaji na uidhinishaji, hasa katika mazingira ya Windows.

LDAP ni muhimu kwa biashara kusimamia ufikiaji wa watumiaji katika mifumo ya ndani, lakini katika muktadha wa kisasa wa wavuti, LDAP mara nyingi huunganishwa na itifaki nyingine kama SAML au OAuth kwa usimamizi kamili zaidi wa utambulisho.

### 6. **Watoa SSO wa Kijamii (Social SSO)**

Watoa **Kuingia Mara Moja (SSO)** wa kijamii kama **Facebook**, **Google**, **Twitter**, **GitHub**, na wengine huruhusu watumiaji kujithibitisha kwenye programu za wahusika wa tatu kwa kutumia vitambulisho vyao vya mitandao ya kijamii. Hii ni aina ya **uthibitishaji unaotegemea OAuth** ambapo huduma ya mhusika wa tatu (mf., Google) ndiyo mtoa utambulisho.

- **Mtiririko**: Mtumiaji hubofya "Ingia na Google" (kwa mfano). Programu humwelekeza kwa Google, ambapo mtumiaji huingia (ikiwa hajaingia tayari). Kisha Google hutoa tokeni ya ufikiaji au tokeni ya kitambulisho kwa programu ya mhusika wa tatu, ambayo inaweza kutumika kuthibitisha mtumiaji na pengine kufikia data yake.
- **Mfano**: Programu nyingi hukuruhusu kuingia kwa kutumia vitambulisho vyako vya Google au Facebook. Programu itatumia OAuth au OpenID Connect nyuma ya pazia kuthibitisha utambulisho wako na, katika hali fulani, kufikia data fulani ya mitandao ya kijamii.

SSO ya kijamii ni njia rahisi na inayokubaliwa kwa upana ya uthibitishaji kwa sababu hupunguza msuguano kwa watumiaji, ambao huenda hawataki kuunda jina lingine la mtumiaji na nenosiri.

---

### Muhtasari wa Tofauti:

- **OAuth**: Hutumika kwa uidhinishaji, huruhusu programu za wahusika wa tatu kufikia data ya mtumiaji bila kufichua vitambulisho.
- **OpenID Connect**: Hupanua OAuth kutoa uthibitishaji, ikiwezesha programu kuthibitisha utambulisho wa mtumiaji.
- **SAML**: Itifaki inayotegemea XML inayotumika kwa SSO, mara nyingi katika mazingira ya biashara.
- **WS-Federation**: Itifaki mahsusi ya Microsoft ya muungano wa utambulisho, inayotumika katika mifumo ya zamani.
- **LDAP**: Itifaki ya kuuliza huduma za saraka kuthibitisha watumiaji na kusimamia uidhinishaji.
- **Watoa SSO wa Kijamii**: Mifumo inayotegemea OAuth (kama Google, Facebook) inayoruhusu programu za wahusika wa tatu kuthibitisha watumiaji kwa kutumia vitambulisho vyao vya mitandao ya kijamii.

Kila moja ya teknolojia hizi ina nguvu zake na visa vya matumizi, na katika programu za kisasa, unaweza kuona mchanganyiko wake ukitumika kwa vipengele tofauti vya usalama (mf., OAuth/OIDC kwa ufikiaji wa API, SAML kwa SSO ya biashara).
