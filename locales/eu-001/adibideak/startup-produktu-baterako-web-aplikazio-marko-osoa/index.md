# Arkitektura-erabakien erregistroa: web aplikazio markoa, dena barne, full stack, startup produktu baterako

<!-- 

ChatGPT prompt

Long software architecture decision record 
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports. 

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Helburu nagusia:**  
Ordaintzen duten bezeroek saioa hasteko, fitxategiak igotzeko, datuak prozesatzeko eta txostenak ikusteko web aplikazio bat eraikitzea, garapen arinean, full-stack funtzionalitatean eta AA/ML tresnekiko bateragarritasun sendoan, bereziki Project Jupyter koadernoetan, zentratuta.

### Testuingurua eta eskakizunak:

1. **Garapen arina (lehentasun handia)**: Startup gisa, iterazio azkarra eta malgutasuna behar ditugu. Praktika arinak, hala nola prototipatze azkarra, garapen iteratiboa eta aldaketetara egokitzeko gaitasuna, gure garapen-zikloaren gakoak dira.

2. **Full-stack marko (lehentasun handia)**: Gastu orokorrak minimizatu nahi ditugu back-end zein front-end eraginkortasunez kudea ditzakeen marko bat aukeratuz, front-end marko bereizien beharra murriztuz.

3. **AA/ML tresnekiko bateragarritasuna (lehentasun handia)**: Datu-analisiko tresnekin, hala nola Jupyter koadernoekin eta Python-en datu-zientziako ekosistemarekin (NumPy, Pandas, TensorFlow, eta abar), erraz integratzeko gaitasuna ezinbestekoa da. Horrek datuen prozesamendu eta txosten eraginkorrak errazten ditu.

4. **Lehentasun txikiko irizpideak**:
   - **Exekuzio-abiadura**: Errendimendua garrantzitsua den arren, ez da faktore kritikoena hasieran, garapen-abiadura eta ezaugarrien osotasuna gehiago kezkatzen gaituztelako.
   - **Eskalagarritasuna**: Hazkundea aurreikusten dugu, baina eskalagarritasun-kezkak geroago jorra daitezke, eta ez da oraingo lehen eskakizuna.
   - **Atzerako bateragarritasuna**: Oraingo teknologietan zentratzen gara eta ez gaude oso kezkatuta sistema zaharrekiko atzerako bateragarritasunarekin.

### Ebaluatutako markoak:

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Ikuspegi orokorra**:  
Django Python-erako goi-mailako web marko bat da, garapen azkarra eta diseinu garbi eta pragmatikoa sustatzen dituena. "batteries included" filosofiagatik ezaguna da, hau da, ezaugarri asko kutxatik kanpo sartzen dituela, hala nola autentikazioa, bideratzea, ORM-a eta formularioen kudeaketa.

**Indarrak**:  
- **Full-stack**: Django marko full-stack zabala da, back-end zein front-end beharrak kudea ditzakeena ezaugarri integratuekin (adib. txantiloi-motorra, admin interfazea).
- **Garapen arina**: Djangoren egitura eta konbentzio ongi definituek garapen azkarra eta egokitzeko gaitasuna ahalbidetzen dute, startup ingurunerako funtsezkoak. Markoak dokumentazio bikaina eta hirugarrenen pakete ekosistema aberatsa ditu, garapena bizkortzen dutenak.
- **AA/ML integrazioa**: Python-en ekosistema parekaezina da datu-zientziari eta ikaskuntza automatikoari dagokionez. Django, Python oinarritua izanik, Jupyter koadernoak, Pandas, NumPy, TensorFlow eta scikit-learn bezalako tresnekin oztoporik gabe integratzen da.
- **Komunitatea eta ekosistema**: Djangok komunitate zabala, dokumentazio sendoa eta plugin eta luzapen sorta zabala ditu, garapena eta arazoen konponketa nabarmen bizkortzen dutenak.
  
**Ahuleziak**:  
- **Exekuzio-abiadura**: Python Rust edo Elixir bezalako lengoaiak baino motelagoa izan ohi da. Hala ere, errendimendua kezka nagusia ez den erabilera-kasu honetarako, baliteke hau ez izatea erabakigarria.
- **Eskalagarritasuna**: Django oso eskalagarria den arren, baliteke erronkak egotea eskala oso handian optimizazio zainduik gabe (adib. eskaera konkurrente astunak kudeatzean). Hala ere, Django eraginkortasunez eskala daiteke karga-orekatze eta cache teknikak erabiliz.

**Epaia**:  
Django ondo egokitzen da garapen arinaren, full-stack euskarriaren eta AA/ML bateragarritasunaren eskakizunetara. Bere Python integrazioak aplikaziorako beharrezkoak diren datu-zientziako tresna eta liburutegietara oztoporik gabe sartzeko aukera ematen du.

---

### 2. **Ruby on Rails (Ruby)**

**Ikuspegi orokorra**:  
Ruby on Rails (RoR) web aplikazio marko full-stack helduan da, konfigurazioaren gaineko konbentzioaren ikuspegiagatik ezaguna, garapen azkarra errazten duena.

**Indarrak**:  
- **Full-stack**: RoR-ek back-end zein front-end garapenerako tresna integratuak ditu (adib. ikuspegiak, txantiloiak, scaffolding), eta bere gem liburutegi aberatsak hainbat ezaugarri azkar ezartzeko aukera ematen du.
- **Garapen arina**: Ruby on Rails bereziki ezaguna da bere iterazio-ziklo azkarrengatik, ezaugarrietan azkar iteratu nahi duten startup-entzat abantailatsua dena. RoR-ek proba-gidatutako garapena (TDD) onartzen du eta lan-fluxu arinetarako ekosistema finkatua du.
- **Komunitatea eta ekosistema**: RoR-ek komunitate sendo finkatua eta garapena bizkor dezaketen gem sorta zabala ditu.
- **Erabilera-erraztasuna**: Rails-ek garatzaile-lagunkoia den sintaxia du eta datu-base migrazioak, model-view-controller (MVC) arkitektura eta ibilbide-kudeaketa bezalako zereginak azkar eta sinple egiteagatik ezaguna da.

**Ahuleziak**:  
- **Errendimendua**: Ruby-k Python edo Elixir baino exekuzio-errendimendu motelagoa izan ohi du. RoR azpiegitura egokiarekin eskala daitekeen arren, Ruby-ren errendimendua botila-lepoa izan daiteke denbora errealeko prozesamendu astuna edo trafiko konkurrente handia behar duten aplikazioetan.
- **AA/ML integrazioa**: Ruby-k ikaskuntza automatikoko liburutegi batzuk dituen arren, ez da Python bezain zabal hartua AA/ML komunitatean. Jupyter koadernoak bezalako tresnekin integrazioa ez da hain leuna, eta horrek Python aukera sendoagoa egiten du datu-intentsiboko aplikazioetarako.
  
**Epaia**:  
Ruby on Rails garapen arinean eta prototipazio azkarrean bikaina den arren, Python-ekin (Django) alderatuta AA/ML bateragarritasunean motz geratzen da. Datu-analisiaren integrazio sakonaren gainetik iterazio azkarra lehenesten duten startup-entzat aukera bideragarria da.

---

### 3. **Phoenix (Elixir)**

**Ikuspegi orokorra**:  
Phoenix Elixir-ekin eraikitako web marko bat da, eskalagarritasunerako eta konkurrentziarako diseinatutako programazio-lengoaia funtzionala. Phoenix-ek Erlang VM-a aprobetxatzen du, konkurrentzia masiboa eta akats-tolerantea den sistemak kudeatzeagatik ezaguna dena.

**Indarrak**:  
- **Eskalagarritasuna eta errendimendua**: Phoenix distiratsua da eskalagarritasunean eta konkurrentzia handia kudeatzean. Erlang VM-an eraikita dago, milaka (edo milioika ere) konexio konkurrente onar ditzakeena, eta horrek hautagai sendoa bihurtzen du denbora errealeko datu-prozesamendua edo trafiko-bolumen handia behar duten aplikazioetarako.
- **Full-stack**: Phoenix-ek aplikazio baten back-end eta front-end eraikitzeko behar den guztia sartzen du. Live view-ak onartzen ditu UI eguneraketa interaktiboetarako eta txantiloi-motorra sartzen du.
- **Garapen arina**: Phoenix oso modularra da, ezaugarrien iterazio azkarra ahalbidetuz. Azkar mugitu behar duten startup-entzat oso egokia da.
- **AA/ML bateragarritasuna**: Elixir-ek ikaskuntza automatikoko liburutegi berriak dituen arren, ez da Python bezain zabal onartua AA/ML zereginetarako. Jupyter koadernoak bezalako tresnekin integratzeak konponbide-bideak beharko lituzke, Elixir-en datu-zientziako ekosistema ez baita Python-ena bezain helduan.

**Ahuleziak**:  
- **AA/ML ekosistema**: Elixir ez da datu-zientzian edo ikaskuntza automatikoan erabiltzen den lengoaia nagusia, eta ekosistema ez da Python-ena bezain helduan. Beraz, Jupyter koadernoak edo AA liburutegi ezagunak (TensorFlow, PyTorch) bezalako tresnekin integrazioa neketsua izango da.
- **Ikaskuntza-kurba**: Taldeak programazio funtzionala eta Elixir ezagutzen ez baditu, ikaskuntza-kurba aldapatsuagoa egon daiteke.

**Epaia**:  
Phoenix aukera bikaina da eskalagarritasuna eta konkurrentzia kezka nagusia direnean. Hala ere, AA/ML bateragarritasunaren lehentasuna kontuan hartuta, baliteke Phoenix ez izatea egokiena Elixir-en ekosistema mugatua dela eta arlo horretan.

---

### 4. **Loco (Rust)**

**Ikuspegi orokorra**:  
Loco Rust-ekin eraikitako web marko bat da, errendimenduagatik, memoria-segurtasunagatik eta konkurrentziagatik ezaguna den sistema-programazio lengoaia. Rust gero eta ezagunagoa da errendimendu handiko aplikazioak eraikitzeko.

**Indarrak**:  
- **Errendimendua**: Rust-en indar nagusia bere errendimendu handian eta memoria-segurtasunean datza, eta horrek aukera bikaina bihurtzen du behe-mailako kontrola edo oso errendimendu handia behar duten aplikazioetarako.
- **Konkurrentzia**: Rust-en jabetza-sistemak memoria-segurtasuna ziurtatzen du programazio konkurrente segurua ahalbidetzen duen bitartean, eta horrek ezin hobea egiten du eraginkortasunez eskalatu eta paralelismoa kudeatu behar duten sistemetarako.

**Ahuleziak**:  
- **Full-stack garapena**: Loco, itxaropentsua izan arren, ez da beste markoak bezain helduan full-stack soluzio osoa eskaintzeari dagokionez. Back-end garapenerako egokiagoa da, eta Rust-en inguruko front-end ekosistema oraindik sortzen ari da.
- **Garapen arina**: Rust-ekin garatzea motelagoa izan daiteke Python edo Ruby bezalako goi-mailako lengoaiekin alderatuta, bere izaera behe-mailakoagatik eta ikaskuntza-kurba aldapatsuagoagatik.
- **AA/ML ekosistema**: Rust-ek ez du Python-ek duen AA/ML ekosistema zabalik. Konputazio numerikorako Rust-en liburutegi hazkorrak daudenean ere, askoz ez dira Python-en eskaintzak bezain helduak, hala nola Jupyter koadernoak edo ikaskuntza automatikoko esparruak.
  
**Epaia**:  
Rust eta bere Loco markoak errendimendu apartekoa eskaintzen duten arren, full-stack euskarririk eza, garapen arinaren onurak eta AA/ML ekosistema ez dira ezin hobeak erabilera-kasu zehatz honetarako. Errendimendu-kritikoak diren aplikazioetarako egokiagoa da, datu-zientziako tresna integratuekin web garapen azkarrerako baino.

---

### Ondorioa

Proiektuaren eskakizunen arabera aukerak ebaluatu ondoren, **Django (Python)** da aukerarik egokiena. Abantaila hauek eskaintzen ditu:

- **Full-stack gaitasunak**: Django full-stack marko bat da, back-end eta front-end garapena integratzen duena.
- **Garapen arina**: Markoa ondo egokitzen da prototipatze eta iterazio azkarrerako, startup ingurunerako funtsezkoa dena.
- **AA/ML bateragarritasuna**: Python AA/ML-n lengoaia liderra da, eta Django-k Jupyter koadernoak bezalako liburutegiekin duen bateragarritasunak datu-analisi eta prozesamendurako integrazio leuna ziurtatzen du.
- **Komunitatea eta ekosistema**: Djangoren komunitate-laguntza sendoak eta liburutegi-ekosistema zabalak garapena bizkortzeko tresna ugari eskaintzen dituzte.

**Ruby on Rails** ere lehiakide sendoa den arren garapen arinerako, bere AA/ML euskarri mugatuak erabilera-kasu zehatz honetarako ez-egoki bihurtzen du. **Phoenix (Elixir)** eta **Loco (Rust)**, eskalagarritasunerako eta errendimendurako bikainak izan arren, AA/ML integrazioan eta full-stack garapenean motz geratzen dira. Beraz, Django da proiektu honetarako gomendatutako marko.
