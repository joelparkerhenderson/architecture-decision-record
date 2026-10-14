# Arhitektuuriotsuse kirje: veebirakenduse raamistik, kõik kaasas (batteries included), full stack, idutoote jaoks

<!-- 

ChatGPT prompt

Long software architecture decision record 
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports. 

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Peamine eesmärk:**  
Ehitada veebirakendus, kus maksvad kliendid saavad sisse logida, faile üles laadida, andmeid töödelda ja aruandeid vaadata, keskendudes agiilsele arendusele, full stack funktsionaalsusele ja tugevale ühilduvusele tehisintellekti/masinõppe tööriistadega, eriti Project Jupyteri märkmikega.

### Kontekst ja nõuded:

1. **Agiilne arendus (kõrge prioriteet)**: idufirmana vajame kiiret iteratsiooni ja paindlikkust. Agiilsed meetodid, nagu kiire prototüüpimine, iteratiivne arendus ja kohanemisvõime muutustega, on meie arendustsükli võti.

2. **Full stack raamistik (kõrge prioriteet)**: püüame minimeerida lisakoormust, valides raamistiku, mis suudab tõhusalt käsitleda nii taustasüsteemi kui ka kasutajaliidest, vähendades vajadust eraldi kasutajaliidese raamistike järele.

3. **Ühilduvus tehisintellekti/masinõppe tööriistadega (kõrge prioriteet)**: võime hõlpsasti integreeruda andmeanalüüsi tööriistadega nagu Jupyteri märkmikud ja Pythoni andmeteaduse ökosüsteem (NumPy, Pandas, TensorFlow jne) on ülioluline. See hõlbustaks tõhusat andmetöötlust ja aruandlust.

4. **Madala prioriteediga kriteeriumid**:
   - **Käitusaja kiirus**: kuigi jõudlus on oluline, ei ole see alguses kõige kriitilisem tegur, kuna oleme rohkem mures arenduskiiruse ja funktsioonide valmimise pärast.
   - **Skaleeritavus**: ootame kasvu, kuid skaleeritavuse küsimusi saab käsitleda hiljem ja see ei ole praegu peamine nõue.
   - **Tagasiulatuv ühilduvus**: keskendume praegustele tehnoloogiatele ega ole eriti mures tagasiulatuva ühilduvuse pärast vanemate süsteemidega.

### Hinnatud raamistikud:

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Ülevaade**:  
Django on Pythoni kõrgetasemeline veebiraamistik, mis soodustab kiiret arendust ning puhast, pragmaatilist disaini. See on tuntud oma "batteries included" filosoofia poolest, mis tähendab, et see sisaldab karbist välja paljusid funktsioone nagu autentimine, marsruutimine, ORM ja vormitöötlus.

**Tugevused**:  
- **Full stack**: Django on põhjalik full stack raamistik, mis suudab käsitleda nii taustasüsteemi kui ka kasutajaliidese vajadusi integreeritud funktsioonidega (nt mallimootor, haldusliides).
- **Agiilne arendus**: Django hästi määratletud struktuur ja konventsioonid võimaldavad kiiret arendust ja kohanemisvõimet, mis on idufirma keskkonnas hädavajalik. Raamistik tuleb suurepärase dokumentatsiooni ja kolmandate osapoolte pakettide rikkaliku ökosüsteemiga, mis kiirendab arendust.
- **Tehisintellekti/masinõppe integratsioon**: Pythoni ökosüsteem on andmeteaduses ja masinõppes vaieldamatu. Python-põhine Django integreerub sujuvalt tööriistadega nagu Jupyteri märkmikud, Pandas, NumPy, TensorFlow ja scikit-learn.
- **Kogukond ja ökosüsteem**: Djangol on ulatuslik kogukond, töökindel dokumentatsioon ja lai valik pluginaid ja laiendusi, mis kiirendavad oluliselt arendust ja silumist.
  
**Nõrkused**:  
- **Käitusaja kiirus**: Python kipub olema aeglasem võrreldes keeltega nagu Rust või Elixir. Selle kasutusjuhu jaoks, kus jõudlus ei ole peamine mure, ei pruugi see olla otsustav.
- **Skaleeritavus**: kuigi Django on väga skaleeritav, võib väga suure mahu korral ilma hoolika optimeerimiseta olla väljakutseid (nt raskete samaaegsete päringute käsitlemisel). Django saab siiski tõhusalt skaleeruda koormuse jaotamise ja vahemällu salvestamise tehnikatega.

**Hinnang**:  
Django sobib hästi agiilse arenduse, full stack toe ja tehisintellekti/masinõppe ühilduvuse nõuetega. Selle Pythoni integratsioon pakub sujuvat juurdepääsu rakenduse jaoks vajalikele andmeteaduse tööriistadele ja teekidele.

---

### 2. **Ruby on Rails (Ruby)**

**Ülevaade**:  
Ruby on Rails (RoR) on küps full stack veebirakenduste raamistik, mis on tuntud oma "konventsioon konfiguratsiooni ees" lähenemise poolest, mis hõlbustab kiiret arendust.

**Tugevused**:  
- **Full stack**: RoR tuleb sisseehitatud tööriistadega nii taustasüsteemi kui ka kasutajaliidese arenduseks (nt vaated, mallid, scaffolding) ja selle rikkalik gem'ide teek võimaldab erinevaid funktsioone kiiresti teostada.
- **Agiilne arendus**: Ruby on Rails on eriti tuntud oma kiirete iteratsioonitsüklite poolest, mis on kasulik idufirmadele, kes tahavad funktsioonidel kiiresti iteratsioone teha. RoR toetab testipõhist arendust (TDD) ja sellel on väljakujunenud ökosüsteem agiilsete töövoogude jaoks.
- **Kogukond ja ökosüsteem**: RoR-il on väljakujunenud, tugev kogukond ja lai valik gem'e, mis võivad arendust kiirendada.
- **Kasutuslihtsus**: Railsil on väga arendajasõbralik süntaks ja see on tuntud selle poolest, et teeb ülesanded nagu andmebaasimigratsioonid, Model-View-Controller (MVC) arhitektuur ja marsruudihaldus kiireks ja lihtsaks.

**Nõrkused**:  
- **Jõudlus**: Rubyl kipub olema aeglasem käitusaja jõudlus võrreldes Pythoni või Elixiriga. Kuigi RoR saab õige taristuga skaleeruda, võib Ruby jõudlus saada kitsaskohaks rakendustele, mis nõuavad rasket reaalajatöötlust või suurt samaaegset liiklust.
- **Tehisintellekti/masinõppe integratsioon**: kuigi Rubyl on mõned masinõppe teegid, ei ole see tehisintellekti/masinõppe kogukonnas nii laialdaselt kasutusele võetud kui Python. Integratsioon tööriistadega nagu Jupyteri märkmikud ei ole nii sujuv, mis teeb Pythonist tugevama valiku andmemahukate rakenduste jaoks.
  
**Hinnang**:  
Kuigi Ruby on Rails paistab silma agiilses arenduses ja kiires prototüüpimises, jääb see tehisintellekti/masinõppe ühilduvuses Pythoni (Django) ees alla. See on teostatav valik idufirmadele, kes seavad kiire iteratsiooni andmeanalüüsi sügava integratsiooni ette.

---

### 3. **Phoenix (Elixir)**

**Ülevaade**:  
Phoenix on Elixiriga ehitatud veebiraamistik, mis on funktsionaalne programmeerimiskeel, mis on loodud skaleeritavuse ja samaaegsuse jaoks. Phoenix kasutab Erlang VM-i, mis on tuntud massiivse samaaegsuse ja veataluvate süsteemide käsitlemise poolest.

**Tugevused**:  
- **Skaleeritavus ja jõudlus**: Phoenix särab skaleeritavuses ja kõrge samaaegsuse käsitlemises. See on ehitatud Erlang VM-ile, mis suudab toetada tuhandeid (või isegi miljoneid) samaaegseid ühendusi, muutes selle tugevaks kandidaadiks rakendustele, mis nõuavad reaalajas andmetöötlust või suure mahuga liiklust.
- **Full stack**: Phoenix sisaldab kõike, mis on vajalik rakenduse nii taustasüsteemi kui ka kasutajaliidese ehitamiseks. See toetab live view'e interaktiivsete UI uuenduste jaoks ja sisaldab mallimootorit.
- **Agiilne arendus**: Phoenix on väga modulaarne, mis võimaldab funktsioonidel kiiret iteratsiooni. See sobib hästi idufirmadele, kes peavad kiiresti liikuma.
- **Tehisintellekti/masinõppe ühilduvus**: kuigi Elixiril on tärkavad masinõppe teegid, ei toetata seda tehisintellekti/masinõppe ülesannete jaoks nii laialdaselt kui Pythonit. Integratsioon tööriistadega nagu Jupyteri märkmikud nõuaks ümbersõite, kuna Elixiri andmeteaduse ökosüsteem ei ole nii küps kui Pythonil.

**Nõrkused**:  
- **Tehisintellekti/masinõppe ökosüsteem**: Elixir ei ole andmeteaduses ega masinõppes peamiselt kasutatav keel ning ökosüsteem ei ole nii küps kui Pythonil. Seetõttu muutub integratsioon tööriistadega nagu Jupyteri märkmikud või populaarsed tehisintellekti teegid (TensorFlow, PyTorch) tülikaks.
- **Õppimiskõver**: kui meeskond ei ole funktsionaalse programmeerimise ja Elixiriga tuttav, võib olla järsem õppimiskõver.

**Hinnang**:  
Phoenix on suurepärane valik, kui skaleeritavus ja samaaegsus on peamine mure. Arvestades tehisintellekti/masinõppe ühilduvuse prioriteeti, ei pruugi Phoenix aga olla parim sobivus Elixiri piiratud ökosüsteemi tõttu selles valdkonnas.

---

### 4. **Loco (Rust)**

**Ülevaade**:  
Loco on Rustiga ehitatud veebiraamistik, mis on süsteemiprogrammeerimiskeel, mis on tuntud jõudluse, mäluohutuse ja samaaegsuse poolest. Rust muutub üha populaarsemaks kõrge jõudlusega rakenduste ehitamisel.

**Tugevused**:  
- **Jõudlus**: Rusti peamine tugevus seisneb selle kõrges jõudluses ja mäluohutuses, mis teeb sellest suurepärase valiku rakendustele, mis nõuavad madala taseme kontrolli või äärmiselt kõrget jõudlust.
- **Samaaegsus**: Rusti omandisüsteem (ownership) tagab mäluohutuse, lubades samal ajal ohutut samaaegset programmeerimist, mis teeb selle ideaalseks süsteemide jaoks, mis peavad tõhusalt skaleeruma ja paralleelsust käsitlema.

**Nõrkused**:  
- **Full stack arendus**: Loco ei ole, kuigi paljulubav, nii küps kui teised raamistikud täieliku full stack lahenduse pakkumisel. See sobib paremini taustasüsteemi arenduseks ja Rusti ümber olev kasutajaliidese ökosüsteem alles tekib.
- **Agiilne arendus**: arendus Rustiga võib olla aeglasem võrreldes kõrgetasemeliste keeltega nagu Python või Ruby selle madalama taseme ja järsema õppimiskõvera tõttu.
- **Tehisintellekti/masinõppe ökosüsteem**: Rustil ei ole sama ulatuslikku tehisintellekti/masinõppe ökosüsteemi kui Pythonil. Kuigi Rustis on kasvavaid teeke numbriliseks arvutuseks, on need palju vähem küpsed kui Pythoni pakkumised, nagu Jupyteri märkmikud või masinõppe raamistikud.
  
**Hinnang**:  
Kuigi Rust ja selle raamistik Loco pakuvad erakordset jõudlust, muudavad full stack toe, agiilse arenduse eeliste ja tehisintellekti/masinõppe ökosüsteemi puudumine selle selle konkreetse kasutusjuhu jaoks vähem ideaalseks. See sobib paremini jõudluskriitilistele rakendustele kui kiireks veebiarenduseks integreeritud andmeteaduse tööriistadega.

---

### Kokkuvõte

Pärast võimaluste hindamist projekti nõuete alusel on **Django (Python)** kõige sobivam valik. See pakub järgmisi eeliseid:

- **Full stack võimalused**: Django on full stack raamistik, mis integreerib taustasüsteemi ja kasutajaliidese arenduse.
- **Agiilne arendus**: raamistik sobib hästi kiireks prototüüpimiseks ja iteratsiooniks, mis on idufirma keskkonnas ülioluline.
- **Tehisintellekti/masinõppe ühilduvus**: Python on tehisintellekti/masinõppe juhtiv keel ja Django ühilduvus teekidega nagu Jupyteri märkmikud tagab sujuva integratsiooni andmeanalüüsiks ja andmetöötluseks.
- **Kogukond ja ökosüsteem**: Django tugev kogukonna toetus ja ulatuslik teekide ökosüsteem pakuvad arvukalt tööriistu arenduse kiirendamiseks.

Kuigi **Ruby on Rails** on samuti tugev kandidaat agiilseks arenduseks, teeb selle piiratud tehisintellekti/masinõppe tugi selle selle konkreetse kasutusjuhu jaoks vähem ideaalseks. **Phoenix (Elixir)** ja **Loco (Rust)**, mis paistavad silma skaleeritavuse ja jõudlusega, jäävad tehisintellekti/masinõppe integratsioonis ja full stack arenduses alla. Seetõttu on Django selle projekti jaoks soovitatav raamistik.
