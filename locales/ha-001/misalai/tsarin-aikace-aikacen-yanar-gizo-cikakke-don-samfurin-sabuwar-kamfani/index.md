# Rikodin shawarar gine-gine: tsarin aikace-aikacen yanar gizo, cikakke, full stack, don samfurin sabuwar kamfani

<!-- 

ChatGPT prompt

Long software architecture decision record 
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports. 

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Babban Manufa:**  
Gina aikace-aikacen yanar gizo don abokan ciniki masu biyan kuɗi su shiga, ɗora fayiloli, sarrafa bayanai, da duba rahotanni, mai mai da hankali kan ci gaba mai sassauci, aiki na full-stack, da ƙarfi dacewa da kayan aikin AI/ML, musamman litattafan rubutu na Project Jupyter.

### Mahalli da Buƙatu:

1. **Ci Gaba Mai Sassauci (Fifiko Mai Girma)**: A matsayin sabuwar kamfani, muna buƙatar saurin maimaitawa da sassauci. Ayyukan sassauci, kamar yin samfurin gwaji cikin sauri, ci gaba mai maimaitawa, da daidaitawa ga canji, su ne mabuɗin zagayen ci gabanmu.

2. **Tsarin Full-Stack (Fifiko Mai Girma)**: Muna nufin rage nauyin aiki ta zaɓar tsarin da zai iya sarrafa na baya da na gaba duka yadda ya kamata, yana rage buƙatar tsarukan gaba daban.

3. **Dacewa da Kayan Aikin AI/ML (Fifiko Mai Girma)**: Iya haɗewa cikin sauƙi da kayan aikin nazarin bayanai kamar litattafan rubutu na Jupyter da tsarin muhallin kimiyyar bayanai na Python (NumPy, Pandas, TensorFlow, da sauransu) yana da muhimmanci. Wannan zai sauƙaƙa sarrafa bayanai da rahotanni yadda ya kamata.

4. **Ma’aunin Ƙaramin Muhimmanci**:
   - **Gudun Lokacin Aiki**: Ko da yake aiki yana da dacewa, ba shi ne mafi muhimmanci a farko ba domin muna damuwa da saurin ci gaba da cikar siffofi.
   - **Iya Faɗaɗuwa**: Muna hasashen girma, amma ana iya magance damuwar iya faɗaɗuwa daga baya, kuma ba babban buƙata ba ne yanzu.
   - **Dacewa da Baya**: Muna mai da hankali kan fasahohin yanzu kuma ba mu damu sosai da dacewa da baya da tsoffin tsarukan ba.

### Tsarukan da Aka Kimanta:

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Bayyani**:  
Django tsarin yanar gizo ne na matakin sama na Python wanda ke haɓaka ci gaba cikin sauri da ƙira mai tsabta, mai amfani. An san shi da falsafar “cikakke” (“batteries included”), ma’ana ya haɗa da siffofi da yawa kamar tantancewa, hanyoyi, ORM, da sarrafa fom daga cikin akwatin.

**Ƙarfi**:  
- **Full-Stack**: Django cikakken tsari ne na full-stack wanda zai iya sarrafa buƙatun na baya da na gaba da siffofi da aka haɗa (misali, injin samfurin rubutu, mu’amalar admin).
- **Ci Gaba Mai Sassauci**: Tsari da ƙa’idojin Django da aka ayyana da kyau suna ba da damar ci gaba da sauri da daidaitawa, wanda yake da muhimmanci a muhallin sabuwar kamfani. Tsarin yana zuwa da kyawawan takardu da wadataccen tsarin muhalli na fakiti na wasu kamfanoni, wanda ke hanzarta ci gaba.
- **Haɗewa da AI/ML**: Tsarin muhallin Python ba shi da kamarsa idan ana maganar kimiyyar bayanai da koyon na’ura. Django, da yake na tushen Python ne, yana haɗewa cikin sauƙi da kayan aiki kamar litattafan rubutu na Jupyter, Pandas, NumPy, TensorFlow, da scikit-learn.
- **Al’umma da Tsarin Muhalli**: Django yana da babbar al’umma, ƙaƙƙarfan takardu, da faffadan plugins da kari, wanda ke hanzarta ci gaba da warware matsaloli sosai.
  
**Rauni**:  
- **Gudun Lokacin Aiki**: Python yakan zama a hankali idan aka kwatanta da harsuna kamar Rust ko Elixir. Duk da haka, ga wannan amfani, inda aiki ba shi ne babban damuwa ba, wannan bazai zama mai hana yarjejeniya ba.
- **Iya Faɗaɗuwa**: Ko da yake Django yana iya faɗaɗuwa sosai, ana iya samun ƙalubale a babban matakin ba tare da inganta a hankali ba (misali, lokacin sarrafa buƙatu masu yawa a lokaci ɗaya). Duk da haka, ana iya faɗaɗa Django yadda ya kamata ta amfani da daidaita nauyi da dabarun ajiyar wucin gadi.

**Hukunci**:  
Django ya dace da buƙatun ci gaba mai sassauci, goyon bayan full-stack, da dacewa da AI/ML. Haɗewarsa da Python tana ba da damar shiga cikin sauƙi ga kayan aikin kimiyyar bayanai da laburare da ake buƙata don aikace-aikacen.

---

### 2. **Ruby on Rails (Ruby)**

**Bayyani**:  
Ruby on Rails (RoR) balagagge ne, cikakken tsarin aikace-aikacen yanar gizo na full-stack da aka san shi da hanyar ƙa’ida-fiye-da-saiti, wadda ke sauƙaƙa ci gaba cikin sauri.

**Ƙarfi**:  
- **Full-Stack**: RoR yana zuwa da kayan aiki na ciki don ci gaban na baya da na gaba duka (misali, views, samfuran rubutu, scaffolding), kuma wadataccen laburarensa na gems yana ba da damar aiwatar da siffofi daban-daban da sauri.
- **Ci Gaba Mai Sassauci**: Ruby on Rails an san shi musamman da zagayen maimaitawa masu sauri, wanda yake da fa’ida ga sabbin kamfanoni da ke son maimaita siffofi cikin sauri. RoR yana goyon bayan ci gaba mai jagorantar gwaji (TDD) kuma yana da kafaffen tsarin muhalli don tsarin aiki masu sassauci.
- **Al’umma da Tsarin Muhalli**: RoR yana da kafaffiyar al’umma mai ƙarfi da faffadan gems waɗanda zasu iya hanzarta ci gaba.
- **Sauƙin Amfani**: Rails yana da tsarin rubutu mai sauƙi ga masu haɓakawa kuma an san shi da sa ayyuka kamar komawar rumbun bayanai, gine-ginen model-view-controller (MVC), da sarrafa hanyoyi su zama masu sauri da sauƙi.

**Rauni**:  
- **Aiki**: Ruby yakan samu jinkirin aikin lokacin aiki idan aka kwatanta da Python ko Elixir. Ko da yake RoR na iya faɗaɗuwa da kayayyakin more rayuwa da suka dace, aikin Ruby na iya zama cikas ga aikace-aikacen da ke buƙatar sarrafa lokaci-na-gaske mai nauyi ko zirga-zirga mai yawa a lokaci ɗaya.
- **Haɗewa da AI/ML**: Ko da yake Ruby yana da wasu laburaren koyon na’ura, ba a karɓe shi sosai a al’ummar AI/ML kamar Python ba. Haɗewa da kayan aiki kamar litattafan rubutu na Jupyter ba ta da santsi, wanda ya sa Python ya zama zaɓi mafi ƙarfi ga aikace-aikace masu yawan bayanai.
  
**Hukunci**:  
Ko da yake Ruby on Rails ya yi fice a ci gaba mai sassauci da yin samfurin gwaji cikin sauri, ya gaza a dacewa da AI/ML idan aka kwatanta da Python (Django). Zaɓi ne mai yiwuwa ga sabbin kamfanoni da ke fifita maimaitawa cikin sauri fiye da haɗewa mai zurfi ta nazarin bayanai.

---

### 3. **Phoenix (Elixir)**

**Bayyani**:  
Phoenix tsarin yanar gizo ne da aka gina da Elixir, harshen shirye-shirye mai aiki (functional) da aka ƙirƙira don iya faɗaɗuwa da aiki a lokaci ɗaya. Phoenix yana amfani da Erlang VM, wanda aka san shi da sarrafa manyan ayyuka a lokaci ɗaya da tsarukan masu jure kuskure.

**Ƙarfi**:  
- **Iya Faɗaɗuwa da Aiki**: Phoenix yana haskakawa a iya faɗaɗuwa da sarrafa aiki mai yawa a lokaci ɗaya. An gina shi a kan Erlang VM, wanda zai iya tallafawa dubbai (ko ma miliyoyi) na haɗi a lokaci ɗaya, wanda ya sa shi ɗan takara mai ƙarfi ga aikace-aikacen da ke buƙatar sarrafa bayanai a lokaci-na-gaske ko zirga-zirga mai yawa.
- **Full-Stack**: Phoenix ya haɗa da duk abin da ake buƙata don gina na baya da na gaba na aikace-aikace. Yana goyon bayan live views don sabuntawar UI mai mu’amala kuma ya haɗa da injin samfurin rubutu.
- **Ci Gaba Mai Sassauci**: Phoenix yana da ɓangarori da yawa, yana ba da damar maimaita siffofi cikin sauri. Ya dace sosai da sabbin kamfanoni da ke buƙatar motsawa da sauri.
- **Dacewa da AI/ML**: Ko da yake Elixir yana da laburaren koyon na’ura masu tasowa, ba a goyon bayansa sosai ga ayyukan AI/ML kamar Python ba. Haɗewa da kayan aiki kamar litattafan rubutu na Jupyter zai buƙaci mafita na gefe, domin tsarin muhallin Elixir na kimiyyar bayanai bai balaga kamar na Python ba.

**Rauni**:  
- **Tsarin Muhallin AI/ML**: Elixir ba shi ne babban harshen da ake amfani da shi a kimiyyar bayanai ko koyon na’ura ba, kuma tsarin muhallin bai balaga kamar na Python ba. Don haka, haɗewa da kayan aiki kamar litattafan rubutu na Jupyter ko shahararrun laburaren AI (TensorFlow, PyTorch) zai zama mai wahala.
- **Lokacin Koyo**: Idan tawagar ba ta saba da shirye-shirye masu aiki (functional) da Elixir ba, ana iya samun lokacin koyo mai tsayi.

**Hukunci**:  
Phoenix zaɓi ne mai kyau idan iya faɗaɗuwa da aiki a lokaci ɗaya su ne babban damuwa. Duk da haka, idan aka yi la’akari da fifikon dacewa da AI/ML, Phoenix bazai zama mafi dacewa ba saboda iyakantaccen tsarin muhallin Elixir a wannan fanni.

---

### 4. **Loco (Rust)**

**Bayyani**:  
Loco tsarin yanar gizo ne da aka gina da Rust, harshen shirye-shiryen tsarukan da aka san shi da aiki, amincin ƙwaƙwalwa, da aiki a lokaci ɗaya. Rust yana ƙara shahara wajen gina aikace-aikace masu babban aiki.

**Ƙarfi**:  
- **Aiki**: Babban ƙarfin Rust yana cikin babban aikinsa da amincin ƙwaƙwalwa, wanda ya sa shi zaɓi mai kyau ga aikace-aikacen da ke buƙatar ikon ƙaramin matakin ko babban aiki na ban mamaki.
- **Aiki a Lokaci Ɗaya**: Tsarin mallaka na Rust yana tabbatar da amincin ƙwaƙwalwa yayin da yake ba da damar shirye-shirye masu aiki a lokaci ɗaya cikin aminci, wanda ya sa ya dace da tsarukan da ke buƙatar faɗaɗuwa yadda ya kamata da sarrafa daidaita aiki.

**Rauni**:  
- **Ci Gaban Full-Stack**: Loco, ko da yake yana da alƙawari, bai balaga kamar sauran tsarukan ba wajen samar da cikakkiyar mafitar full-stack. Ya fi dacewa da ci gaban na baya, kuma tsarin muhallin na gaba da ke kewaye da Rust har yanzu yana tasowa.
- **Ci Gaba Mai Sassauci**: Ci gaba da Rust na iya zama a hankali idan aka kwatanta da harsunan matakin sama kamar Python ko Ruby saboda yanayinsa na ƙaramin matakin da lokacin koyo mai tsayi.
- **Tsarin Muhallin AI/ML**: Rust ba shi da faffadan tsarin muhalli na AI/ML kamar Python. Ko da yake akwai laburare masu girma a Rust don lissafin lambobi, sun fi rashin balaga sosai fiye da abin da Python ke bayarwa, kamar litattafan rubutu na Jupyter ko tsarukan koyon na’ura.
  
**Hukunci**:  
Ko da yake Rust da tsarinsa Loco suna ba da aiki na musamman, rashin goyon bayan full-stack, fa’idodin ci gaba mai sassauci, da tsarin muhallin AI/ML ya sa bai dace sosai da wannan takamaiman amfani ba. Ya fi dacewa da aikace-aikace masu muhimmancin aiki fiye da saurin ci gaban yanar gizo tare da kayan aikin kimiyyar bayanai da aka haɗa.

---

### Kammalawa

Bayan kimanta zaɓuɓɓukan bisa buƙatun aikin, **Django (Python)** shi ne zaɓi mafi dacewa. Yana ba da fa’idodi masu zuwa:

- **Iyawar Full-Stack**: Django tsarin full-stack ne wanda ke haɗa ci gaban na baya da na gaba.
- **Ci Gaba Mai Sassauci**: Tsarin ya dace sosai da yin samfurin gwaji da maimaitawa cikin sauri, wanda yake da muhimmanci a muhallin sabuwar kamfani.
- **Dacewa da AI/ML**: Python shi ne babban harshe a AI/ML, kuma dacewar Django da laburare kamar litattafan rubutu na Jupyter tana tabbatar da haɗewa mai santsi don nazari da sarrafa bayanai.
- **Al’umma da Tsarin Muhalli**: Ƙarfin tallafin al’ummar Django da faffadan tsarin muhallin laburare suna ba da kayan aiki da yawa don hanzarta ci gaba.

Ko da yake **Ruby on Rails** ma mai takara ne mai ƙarfi ga ci gaba mai sassauci, iyakantaccen goyon bayan AI/ML ɗinsa ya sa bai dace sosai da wannan takamaiman amfani ba. **Phoenix (Elixir)** da **Loco (Rust)**, ko da yake sun yi kyau don iya faɗaɗuwa da aiki, sun gaza a haɗewar AI/ML da ci gaban full-stack. Saboda haka, Django shi ne tsarin da aka ba da shawara ga wannan aiki.
