# Rekodi ya Uamuzi wa Usanifu: mfumo wa programu za wavuti, kila kitu ndani, safu kamili, kwa bidhaa ya kampuni changa

<!-- 

ChatGPT prompt

Long software architecture decision record 
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports. 

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Lengo Kuu:**  
Kujenga programu ya wavuti kwa wateja wanaolipa kuingia, kupakia faili, kuchakata data, na kutazama ripoti, kwa kuzingatia uundaji wenye wepesi, utendaji wa safu kamili, na upatanifu imara na zana za AI/ML, hasa Project Jupyter notebooks.

### Muktadha na Mahitaji:

1. **Uundaji wenye Wepesi (Kipaumbele cha Juu)**: Kama kampuni changa, tunahitaji kurudia kwa haraka na unyumbufu. Mazoea ya wepesi, kama kutengeneza mifano ya awali kwa haraka, uundaji wa awamu, na kubadilika kulingana na mabadiliko, ni muhimu kwa mzunguko wetu wa uundaji.

2. **Mfumo wa Safu Kamili (Kipaumbele cha Juu)**: Tunalenga kupunguza mzigo wa ziada kwa kuchagua mfumo unaoweza kushughulikia sehemu ya nyuma na ya mbele kwa ufanisi, ukipunguza haja ya mifumo tofauti ya sehemu ya mbele.

3. **Upatanifu na Zana za AI/ML (Kipaumbele cha Juu)**: Uwezo wa kuunganishwa kwa urahisi na zana za uchanganuzi wa data kama Jupyter notebooks na mfumo ikolojia wa sayansi ya data wa Python (NumPy, Pandas, TensorFlow, n.k.) ni muhimu. Hii ingewezesha usindikaji na utoaji wa ripoti wa data kwa ufanisi.

4. **Vigezo vya Umuhimu wa Chini**:
   - **Kasi ya Utekelezaji**: Ingawa utendaji ni muhimu, si jambo muhimu zaidi mwanzoni kwa kuwa tunajali zaidi kasi ya uundaji na ukamilifu wa vipengele.
   - **Uwezo wa Kupanuka**: Tunatarajia ukuaji, lakini masuala ya uwezo wa kupanuka yanaweza kushughulikiwa baadaye, na hili si hitaji kuu sasa.
   - **Upatanifu wa Nyuma**: Tunazingatia teknolojia za sasa na hatujali sana upatanifu wa nyuma na mifumo ya zamani.

### Mifumo Iliyotathminiwa:

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Muhtasari**:  
Django ni mfumo wa wavuti wa kiwango cha juu kwa Python unaokuza uundaji wa haraka na muundo safi, wa vitendo. Unajulikana kwa falsafa yake ya "kila kitu ndani", ikimaanisha unajumuisha vipengele vingi kama uthibitishaji, upitishaji, ORM, na ushughulikiaji wa fomu moja kwa moja.

**Nguvu**:  
- **Safu Kamili**: Django ni mfumo kamili wa safu kamili unaoweza kushughulikia mahitaji ya sehemu ya nyuma na ya mbele kwa vipengele vilivyounganishwa (mf., injini ya violezo, kiolesura cha usimamizi).
- **Uundaji wenye Wepesi**: Muundo na kanuni zilizofafanuliwa vizuri za Django huruhusu uundaji wa haraka na kubadilika, jambo muhimu kwa mazingira ya kampuni changa. Mfumo unakuja na nyaraka bora na mfumo ikolojia tajiri wa vifurushi vya wahusika wa tatu, vinavyoharakisha uundaji.
- **Ujumuishaji wa AI/ML**: Mfumo ikolojia wa Python hauna kifani linapokuja suala la sayansi ya data na ujifunzaji wa mashine. Django, ikiwa inategemea Python, huunganishwa bila mshono na zana kama Jupyter notebooks, Pandas, NumPy, TensorFlow, na scikit-learn.
- **Jamii na Mfumo Ikolojia**: Django ina jamii kubwa, nyaraka thabiti, na anuwai pana ya programu-jalizi na viendelezi, vinavyoharakisha kwa kiasi kikubwa uundaji na utatuzi wa matatizo.
  
**Udhaifu**:  
- **Kasi ya Utekelezaji**: Python huelekea kuwa polepole ikilinganishwa na lugha kama Rust au Elixir. Hata hivyo, kwa kisa hiki cha matumizi, ambapo utendaji si jambo kuu, hili huenda lisiwe kikwazo.
- **Uwezo wa Kupanuka**: Ingawa Django inaweza kupanuka sana, kunaweza kuwa na changamoto katika kiwango cha juu sana bila uboreshaji makini (mf., wakati wa kushughulikia maombi mazito ya wakati mmoja). Hata hivyo, Django bado inaweza kupanuliwa kwa ufanisi kwa kutumia ugawaji wa mzigo na mbinu za uhifadhi wa muda.

**Hukumu**:  
Django inaendana vizuri na mahitaji ya uundaji wenye wepesi, usaidizi wa safu kamili, na upatanifu wa AI/ML. Ujumuishaji wake wa Python hutoa ufikiaji usio na mshono wa zana na maktaba za sayansi ya data zinazohitajika kwa programu.

---

### 2. **Ruby on Rails (Ruby)**

**Muhtasari**:  
Ruby on Rails (RoR) ni mfumo uliokomaa wa programu za wavuti wa safu kamili, unaojulikana kwa mbinu yake ya kanuni-kuliko-usanidi, inayowezesha uundaji wa haraka.

**Nguvu**:  
- **Safu Kamili**: RoR inakuja na zana zilizojengewa ndani kwa uundaji wa sehemu ya nyuma na ya mbele (mf., mionekano, violezo, scaffolding), na maktaba yake tajiri ya gems inaruhusu utekelezaji wa haraka wa vipengele mbalimbali.
- **Uundaji wenye Wepesi**: Ruby on Rails inajulikana hasa kwa mizunguko yake ya haraka ya marudio, jambo lenye faida kwa kampuni changa zinazotaka kurudia vipengele kwa haraka. RoR inaunga mkono uundaji unaoendeshwa na majaribio (TDD) na ina mfumo ikolojia ulioimarika kwa mtiririko wa kazi wa wepesi.
- **Jamii na Mfumo Ikolojia**: RoR ina jamii iliyoimarika, imara na anuwai pana ya gems zinazoweza kuharakisha uundaji.
- **Urahisi wa Matumizi**: Rails ina sintaksia rafiki sana kwa waundaji na inajulikana kwa kufanya kazi kama uhamishaji wa hifadhidata, usanifu wa model-view-controller (MVC), na ushughulikiaji wa njia kuwa wa haraka na rahisi.

**Udhaifu**:  
- **Utendaji**: Ruby huelekea kuwa na utendaji wa polepole wa wakati wa utekelezaji ikilinganishwa na Python au Elixir. Ingawa RoR inaweza kupanuka kwa miundombinu sahihi, utendaji wa Ruby unaweza kuwa kikwazo kwa programu zinazohitaji usindikaji mzito wa wakati halisi au trafiki kubwa ya wakati mmoja.
- **Ujumuishaji wa AI/ML**: Ingawa Ruby ina maktaba kadhaa za ujifunzaji wa mashine, haikubaliwi kwa upana katika jamii ya AI/ML kama Python. Ujumuishaji na zana kama Jupyter notebooks si laini, na kufanya Python kuwa chaguo imara zaidi kwa programu zinazotegemea sana data.
  
**Hukumu**:  
Ingawa Ruby on Rails inafanya vizuri katika uundaji wenye wepesi na utengenezaji wa haraka wa mifano ya awali, inapungukiwa katika upatanifu wa AI/ML ikilinganishwa na Python (Django). Ni chaguo linalowezekana kwa kampuni changa zinazoweka kipaumbele marudio ya haraka kuliko ujumuishaji wa kina wa uchanganuzi wa data.

---

### 3. **Phoenix (Elixir)**

**Muhtasari**:  
Phoenix ni mfumo wa wavuti uliojengwa kwa Elixir, lugha ya kiutendaji ya programu iliyobuniwa kwa uwezo wa kupanuka na uendeshaji sambamba. Phoenix hutumia Erlang VM, inayojulikana kwa kushughulikia uendeshaji sambamba mkubwa na mifumo inayostahimili hitilafu.

**Nguvu**:  
- **Uwezo wa Kupanuka na Utendaji**: Phoenix inang'aa katika uwezo wa kupanuka na kushughulikia uendeshaji sambamba wa juu. Imejengwa juu ya Erlang VM, inayoweza kuunga mkono maelfu (au hata mamilioni) ya miunganisho ya wakati mmoja, na kuifanya mgombea imara kwa programu zinazohitaji usindikaji wa data wa wakati halisi au trafiki ya kiasi kikubwa.
- **Safu Kamili**: Phoenix inajumuisha kila kitu kinachohitajika kujenga sehemu ya nyuma na ya mbele ya programu. Inasaidia mionekano hai (live views) kwa masasisho yenye mwingiliano ya UI na inajumuisha injini ya violezo.
- **Uundaji wenye Wepesi**: Phoenix ni ya kimoduli sana, ikiruhusu marudio ya haraka ya vipengele. Inafaa vizuri kwa kampuni changa zinazohitaji kusonga haraka.
- **Upatanifu wa AI/ML**: Ingawa Elixir ina maktaba zinazoibuka za ujifunzaji wa mashine, haisaidiwi kwa upana kwa kazi za AI/ML kama Python. Kuunganisha na zana kama Jupyter notebooks kungehitaji suluhisho mbadala, kwa kuwa mfumo ikolojia wa Elixir wa sayansi ya data haujakomaa kama wa Python.

**Udhaifu**:  
- **Mfumo Ikolojia wa AI/ML**: Elixir si lugha kuu inayotumika katika sayansi ya data au ujifunzaji wa mashine, na mfumo ikolojia haujakomaa kama wa Python. Hivyo, ujumuishaji na zana kama Jupyter notebooks au maktaba maarufu za AI (TensorFlow, PyTorch) utakuwa mgumu.
- **Mkondo wa Kujifunza**: Ikiwa timu haifahamu upangaji wa kiutendaji na Elixir, kunaweza kuwa na mkondo mkali zaidi wa kujifunza.

**Hukumu**:  
Phoenix ni chaguo bora ikiwa uwezo wa kupanuka na uendeshaji sambamba ni jambo kuu. Hata hivyo, kwa kuzingatia kipaumbele cha upatanifu wa AI/ML, Phoenix huenda isiwe inayofaa zaidi kutokana na mfumo ikolojia mdogo wa Elixir katika eneo hili.

---

### 4. **Loco (Rust)**

**Muhtasari**:  
Loco ni mfumo wa wavuti uliojengwa kwa Rust, lugha ya upangaji wa mifumo inayojulikana kwa utendaji, usalama wa kumbukumbu, na uendeshaji sambamba. Rust inazidi kuwa maarufu kwa kujenga programu zenye utendaji wa juu.

**Nguvu**:  
- **Utendaji**: Nguvu kuu ya Rust iko katika utendaji wake wa juu na usalama wa kumbukumbu, na kuifanya chaguo bora kwa programu zinazohitaji udhibiti wa kiwango cha chini au utendaji wa juu sana.
- **Uendeshaji Sambamba**: Mfumo wa umiliki wa Rust unahakikisha usalama wa kumbukumbu huku ukiruhusu upangaji salama wa uendeshaji sambamba, na kuufanya kuwa bora kwa mifumo inayohitaji kupanuka kwa ufanisi na kushughulikia ulinganifu.

**Udhaifu**:  
- **Uundaji wa Safu Kamili**: Loco, ingawa inatia matumaini, haijakomaa kama mifumo mingine kwa upande wa kutoa suluhisho kamili la safu kamili. Inafaa zaidi kwa uundaji wa sehemu ya nyuma, na mfumo ikolojia wa sehemu ya mbele kuzunguka Rust bado unaibuka.
- **Uundaji wenye Wepesi**: Kuunda kwa Rust kunaweza kuwa polepole ikilinganishwa na lugha za kiwango cha juu zaidi kama Python au Ruby kutokana na asili yake ya kiwango cha chini na mkondo mkali wa kujifunza.
- **Mfumo Ikolojia wa AI/ML**: Rust haina mfumo ikolojia mpana kama huo wa AI/ML kama Python. Ingawa kuna maktaba zinazokua katika Rust kwa kompyuta ya nambari, hazijakomaa kabisa kuliko matoleo ya Python, kama Jupyter notebooks au mifumo ya ujifunzaji wa mashine.
  
**Hukumu**:  
Ingawa Rust na mfumo wake Loco hutoa utendaji wa kipekee, ukosefu wa usaidizi wa safu kamili, faida za uundaji wenye wepesi, na mfumo ikolojia wa AI/ML huufanya usiwe bora kwa kisa hiki mahsusi cha matumizi. Unafaa zaidi kwa programu zinazotegemea utendaji badala ya uundaji wa haraka wa wavuti wenye zana jumuishi za sayansi ya data.

---

### Hitimisho

Baada ya kutathmini chaguo kulingana na mahitaji ya mradi, **Django (Python)** ndilo chaguo linalofaa zaidi. Linatoa faida zifuatazo:

- **Uwezo wa Safu Kamili**: Django ni mfumo wa safu kamili unaounganisha uundaji wa sehemu ya nyuma na ya mbele.
- **Uundaji wenye Wepesi**: Mfumo unafaa vizuri kwa utengenezaji wa haraka wa mifano ya awali na marudio, jambo muhimu kwa mazingira ya kampuni changa.
- **Upatanifu wa AI/ML**: Python ndiyo lugha inayoongoza katika AI/ML, na upatanifu wa Django na maktaba kama Jupyter notebooks unahakikisha ujumuishaji laini kwa uchanganuzi na usindikaji wa data.
- **Jamii na Mfumo Ikolojia**: Usaidizi imara wa jamii ya Django na mfumo ikolojia mpana wa maktaba hutoa zana nyingi za kuharakisha uundaji.

Ingawa **Ruby on Rails** pia ni mshindani mwenye nguvu kwa uundaji wenye wepesi, usaidizi wake mdogo wa AI/ML huufanya usiwe bora kwa kisa hiki mahsusi cha matumizi. **Phoenix (Elixir)** na **Loco (Rust)**, ingawa ni bora kwa uwezo wa kupanuka na utendaji, zinapungukiwa katika ujumuishaji wa AI/ML na uundaji wa safu kamili. Kwa hivyo, Django ndio mfumo unaopendekezwa kwa mradi huu.
