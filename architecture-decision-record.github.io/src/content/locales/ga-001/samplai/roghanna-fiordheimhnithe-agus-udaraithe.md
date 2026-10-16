# Taifead Cinnidh Ailtireachta: roghanna fíordheimhnithe agus údaraithe

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Is dhá choincheap ríthábhachtacha iad fíordheimhniú agus údarú feidhmchlár gréasáin chun rochtain ar fheidhmchláir agus ar sheirbhísí a dhaingniú. Baineann an dá cheann le céannacht úsáideoirí agus leis an gcaoi a gcuirtear ceadanna ar fáil, ach díríonn siad ar ghnéithe difriúla:

- Is é **Fíordheimhniú** an próiseas chun céannacht úsáideora nó córais a fhíorú.
- Is é **Údarú** an próiseas chun a chinneadh cad iad na hacmhainní nó na gníomhartha ar féidir leis an úsáideoir nó leis an gcóras fíordheimhnithe rochtain a fháil orthu.

Anois, déanaimis tumadh isteach sna prótacail agus sna teicneolaíochtaí ar leith a luaigh tú, a úsáidtear go coitianta i bhfeidhmchláir ghréasáin nua-aimseartha chun fíordheimhniú agus údarú a bhainistiú.

### 1. **OAuth (Open Authorization)**

Is caighdeán oscailte le haghaidh údaraithe é **OAuth**. Ceadaíonn sé d'úsáideoir rochtain theoranta a thabhairt d'fheidhmchlár tríú páirtí ar a gcuid acmhainní gan a gcuid dintiúir a roinnt. Is é an príomhsmaoineamh ná **rochtain tarmligthe**. Úsáidtear OAuth go minic i gcásanna ina bhféadfaidh úsáideoirí logáil isteach i seirbhís tríú páirtí (m.sh., síniú isteach le Google) gan a n-ainm úsáideora agus a bhfocal faire a sholáthar go díreach don tríú páirtí.

- **Sreabhadh**: Leanann OAuth sreabhadh **bunaithe ar chomharthaí** de ghnáth, áit a eisíonn freastalaí údaraithe comhartha rochtana chuig an bhfeidhmchlár tríú páirtí. Léiríonn an comhartha seo ceadanna an úsáideora, agus úsáideann an feidhmchlár é chun rochtain a fháil ar shonraí nó ar acmhainní an úsáideora ó API.
- **Sampla**: Síníonn úsáideoir isteach i bhfeidhmchlár tríú páirtí ag úsáid a gcuntais Google. Fíoraíonn Google céannacht an úsáideora agus ansin deonaíonn sé comhartha a cheadaíonn don fheidhmchlár tríú páirtí rochtain a fháil ar roinnt sonraí Google (m.sh., Google Calendar).

**Ní** láimhseálann OAuth fíordheimhniú go díreach; baineann sé le rochtain a dheonú. Le haghaidh fíordheimhnithe, is minic a phéireáiltear OAuth le prótacail eile, amhail **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

Is sraith céannachta é **OpenID Connect (OIDC)** atá tógtha ar **OAuth 2.0** a chuireann fíordheimhniú le cumais údaraithe OAuth. Go bunúsach, leathnaíonn OpenID Connect OAuth chun **fíordheimhniú úsáideora** a láimhseáil agus soláthraíonn sé bealach caighdeánaithe do fheidhmchláir chun céannacht úsáideora a fhíorú.

- **Sreabhadh**: Nuair a logálann úsáideoir isteach ag úsáid OpenID Connect, iarrann an feidhmchlár tríú páirtí comhartha ID (chomh maith leis an gcomhartha rochtana OAuth). Tá faisnéis faoin úsáideoir sa chomhartha ID (amhail a n-ainm úsáideora, ríomhphost, agus éilimh eile). Ceadaíonn sé seo don fheidhmchlár a fhios a bheith aige cé hé an t-úsáideoir agus an bhfuil sé fíordheimhnithe.
- **Sampla**: Is éard atá i gceist le logáil isteach i seirbhís amhail Slack ag úsáid do chuntais Google (is é Google an soláthraí OpenID Connect) ná fíordheimhniú trí OpenID Connect, agus bainistíonn OAuth an rochtain ar d'acmhainní Google.

Éascaíonn OIDC d'fheidhmchláir tríú páirtí **úsáideoirí a fhíordheimhniú** agus smacht mionchruinn a choinneáil ar na hacmhainní ar féidir leis na feidhmchláir sin rochtain a fháil orthu.

### 3. **SAML (Security Assertion Markup Language)**

Is caighdeán níos sine bunaithe ar XML é **SAML** a úsáidtear chun sonraí fíordheimhnithe agus údaraithe a mhalartú idir páirtithe, go háirithe i gcásanna **Single Sign-On (SSO)**. Úsáidtear go príomha i dtimpeallachtaí fiontair é chun cur ar chumas úsáideoirí fíordheimhniú uair amháin agus rochtain a fháil ar fheidhmchláir iomadúla gan dintiúir a athiontráil.

- **Sreabhadh**: Fíordheimhníonn an t-úsáideoir ar dtús le soláthraí céannachta (IdP). Gineann an IdP **dearbhú SAML** sínithe a chuimsíonn céannacht an úsáideora agus tréithe gaolmhara. Seoltar an dearbhú chuig an soláthraí seirbhíse (SP), a úsáideann é chun rochtain ar an bhfeidhmchlár a údarú.
- **Sampla**: Logálann fostaí isteach ar a gclár corparáideach (an IdP) agus logáiltear isteach go huathoibríoch iad i gcórais eile amhail ríomhphost, CRM, srl., gan dintiúir a athiontráil. Tá an próiseas fíordheimhnithe bunaithe ar an dearbhú SAML a sheolann an IdP.

Úsáidtear SAML go coitianta i **réitigh SSO fiontair** agus oibríonn sé go maith d'fheidhmchláir ghréasáin i dtimpeallachtaí corparáideacha, ach tá sé níos lú cairdiúil don ghluaiseacht i gcomparáid le OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

Prótacal eile é **WS-Federation** a úsáidtear le haghaidh **Single Sign-On (SSO)**, go háirithe i dtimpeallachtaí fiontair bunaithe ar Microsoft. Tá sé mar chuid de theaghlach sonraíochtaí **WS-* (Web Services)** agus ceadaíonn sé cónaidhm céannachta ar fud fearainn slándála éagsúla (amhail idir eagraíochtaí éagsúla nó idir seirbhísí éagsúla).

- **Sreabhadh**: Ceadaíonn WS-Federation do **sholáthraí céannachta iontaofa (IdP)** úsáideoirí a fhíordheimhniú agus comharthaí a eisiúint ar féidir leis an soláthraí seirbhíse a úsáid le haghaidh údaraithe. Tá sé cosúil le SAML ach úsáidtear go minic é i gcásanna a bhfuil siad ag brath go mór ar theicneolaíochtaí Microsoft.
- **Sampla**: Logálann úsáideoir isteach i bhfeidhmchlár fiontair arna óstáil ag Microsoft Azure Active Directory (AD), agus is féidir a gcéannacht a úsáid chun rochtain a fháil ar sheirbhísí cónaidhmithe eile, lena n-áirítear feidhmchláir arna n-óstáil ag díoltóirí tríú páirtí.

Cé go bhfuil WS-Federation cuimsithe den chuid is mó ag prótacail níos nuaí amhail OAuth2.0 agus OpenID Connect i go leor timpeallachtaí gréasáin nua-aimseartha, úsáidtear fós é i gcórais oidhreachta, go háirithe i bhfiontair atá dírithe ar Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

Is prótacal é **LDAP** a úsáidtear chun rochtain a fháil ar sheirbhísí eolaire agus iad a bhainistiú, a úsáidtear go coitianta chun **dintiúir úsáideora a stóráil** agus rialú rochtana a bhainistiú in eolaire láraithe (ar a dtugtar **Seirbhís Eolaire** go minic). Ní bhaineann LDAP go sonrach le fíordheimhniú nó údarú ach úsáidtear é chun sonraí céannachta a stóráil agus a aisghabháil, a úsáidtear ansin sna próisis sin.

- **Fíordheimhniú**: Ceadaíonn LDAP d'fheidhmchlár úsáideoirí a fhíordheimhniú trí iarratas a dhéanamh ar an tseirbhís eolaire le haghaidh dintiúir (amhail focail faire).
- **Údarú**: Bainistíonn sé róil agus ceadanna úsáideoirí freisin, ag cabhrú le cinneadh an bhfuil rochtain ag úsáideoir ar acmhainní áirithe.
- **Sampla**: Úsáideann go leor fiontar eolairí bunaithe ar LDAP (m.sh., **Active Directory**) le haghaidh fíordheimhnithe agus údaraithe, go háirithe laistigh de thimpeallachtaí Windows.

Tá LDAP ríthábhachtach d'fhiontair chun rochtain úsáideoirí a bhainistiú ar fud córas inmheánach, ach i gcomhthéacs gréasáin nua-aimseartha, is minic a chomhtháthaítear LDAP le prótacail eile amhail SAML nó OAuth le haghaidh bainistíocht céannachta níos iomláine.

### 6. **Soláthraithe SSO Sóisialta**

Ceadaíonn soláthraithe **Single Sign-On (SSO)** sóisialta amhail **Facebook**, **Google**, **Twitter**, **GitHub**, agus eile d'úsáideoirí fíordheimhniú isteach i bhfeidhmchláir tríú páirtí ag úsáid a ndintiúir meáin shóisialta. Cineál **fíordheimhnithe bunaithe ar OAuth** é seo ina bhfuil an tseirbhís tríú páirtí (m.sh., Google) mar an soláthraí céannachta.

- **Sreabhadh**: Cliceálann an t-úsáideoir “Log isteach le Google” (mar shampla). Atreoraíonn an feidhmchlár chuig Google, áit a logálann an t-úsáideoir isteach (mura bhfuil sé logáilte isteach cheana). Soláthraíonn Google ansin comhartha rochtana nó comhartha ID don fheidhmchlár tríú páirtí, ar féidir é a úsáid chun an t-úsáideoir a fhíordheimhniú agus b'fhéidir rochtain a fháil ar a gcuid sonraí.
- **Sampla**: Ceadaíonn go leor feidhmchlár duit logáil isteach ag úsáid do dhintiúir Google nó Facebook. Úsáidfidh an feidhmchlár OAuth nó OpenID Connect ar chúl an scéil chun do chéannacht a fhíorú agus, i gcásanna áirithe, rochtain a fháil ar shonraí meáin shóisialta áirithe.

Is modh áisiúil agus forleathan glactha é SSO sóisialta le haghaidh fíordheimhnithe toisc go laghdaíonn sé frithchuimilt d'úsáideoirí, nach mbeadh fonn orthu ainm úsáideora agus focal faire eile a chruthú.

---

### Achoimre ar Dhifríochtaí:

- **OAuth**: Úsáidtear le haghaidh údaraithe, ceadaíonn sé d'fheidhmchláir tríú páirtí rochtain a fháil ar shonraí úsáideora gan dintiúir a nochtadh.
- **OpenID Connect**: Leathnaíonn sé OAuth chun fíordheimhniú a sholáthar, ag cur ar chumas feidhmchlár céannacht úsáideora a fhíorú.
- **SAML**: Prótacal bunaithe ar XML a úsáidtear le haghaidh SSO, go minic i dtimpeallachtaí fiontair.
- **WS-Federation**: Prótacal sonrach do Microsoft le haghaidh cónaidhm céannachta, a úsáidtear i gcórais oidhreachta.
- **LDAP**: Prótacal chun seirbhísí eolaire a cheistiú chun úsáideoirí a fhíordheimhniú agus údarú a bhainistiú.
- **Soláthraithe SSO Sóisialta**: Córais bunaithe ar OAuth (amhail Google, Facebook) a cheadaíonn d'fheidhmchláir tríú páirtí úsáideoirí a fhíordheimhniú ag úsáid a ndintiúir meáin shóisialta.

Tá a láidreachtaí agus a gcásanna úsáide féin ag gach ceann de na teicneolaíochtaí seo, agus i bhfeidhmchláir nua-aimseartha, is féidir meascán díobh a fheiceáil á úsáid do ghnéithe éagsúla slándála (m.sh., OAuth/OIDC le haghaidh rochtain API, SAML le haghaidh SSO fiontair).
