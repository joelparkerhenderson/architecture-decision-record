# Programazio-lengoaiak

Edukia:

* [Laburpena](#laburpena)
  * [Arazoa](#arazoa)
  * [Erabakia](#erabakia)
  * [Egoera](#egoera)
* [Xehetasunak](#xehetasunak)
  * [Hipotesiak](#hipotesiak)
  * [Murriztapenak](#murriztapenak)
  * [Jarrerak](#jarrerak)
  * [Arrazoibidea](#arrazoibidea)
  * [Ondorioak](#ondorioak)
* [Erlazionatuta](#erlazionatuta)
  * [Erlazionatutako erabakiak](#erlazionatutako-erabakiak)
  * [Erlazionatutako eskakizunak](#erlazionatutako-eskakizunak)
  * [Erlazionatutako artefaktuak](#erlazionatutako-artefaktuak)
  * [Erlazionatutako printzipioak](#erlazionatutako-printzipioak)
* [Oharrak](#oharrak)


## Laburpena


### Arazoa

Programazio-lengoaiak aukeratu behar ditugu gure softwarerako. Bi behar nagusi ditugu: web aplikazioetarako egokia den front-end programazio-lengoaia bat, eta zerbitzari-aplikazioetarako egokia den back-end programazio-lengoaia bat.


### Erabakia

TypeScript aukeratzen ari gara front-end-erako.

Rust aukeratzen ari gara back-end-erako.


### Egoera

Erabakia. Alternatiba berrietara irekiak gaude sortzen diren heinean.


## Xehetasunak


### Hipotesiak

Front-end aplikazioak tipikoak dira:

  * Erabiltzaile eta interakzio tipikoak

  * Nabigatzaile eta sistema tipikoak

  * Garapen eta hedapen tipikoak

Front-end aplikazioak azkar eboluzionatzeko aukera handia dago:

  * Garapen, hedapen, iterazio eta abar azkar eta errazak ziurtatu nahi ditugu.

  * Frogagarritasuna, hala nola tipo-segurtasuna, baloratzen dugu, eta lan pixka bat gehiago egitearekin ados gaude hori lortzeko.

  * Ez dugu atzerako bateragarritasunik behar.

Back-end aplikazioak ohikoa baino altuagoak dira:

  * Kalitaterako ohikoa baino helburu altuagoak, bereziki frogagarritasuna, fidagarritasuna, segurtasuna eta abar.

  * Ia denbora errealerako ohikoa baino helburu altuagoak, hau da, ez ditugu nahi makina birtualaren zabor-bilketa dela eta etenak.

  * Programazio funtzionalerako ohikoa baino helburu altuagoak, bereziki paralelizaziorako, nukleo anitzeko prozesamendurako eta memoria-segurtasunerako.

Konpilazio-denborako abiadura txikiagoak onartzen ditugu konpilazio-denborako segurtasunaren eta exekuzio-denborako abiaduraren alde.


### Murriztapenak

Murriztapen sendoa dugu hodei-hornitzaile nagusien funtzioetarako zerbitzuekin erabilgarriak diren lengoaiei dagokienez, hala nola Amazon Lambda.


### Jarrerak

Lengoaia hauek aztertu ditugu:

  * C

  * C++

  * Clojure
  
  * Elixir
  
  * Erlang
  
  * Elm
  
  * Flow
  
  * Go
  
  * Haskell
  
  * Java
  
  * JavaScript
  
  * Kotlin
  
  * Python
  
  * Ruby
  
  * Rust
  
  * TypeScript



### Arrazoibidea

Lengoaia bakoitzaren laburpena:

  * C: baztertua segurtasun txikiagatik; Rust-ek ia dena hobeto egin dezake.

  * C++: baztertua nahaspila delako; Rust-ek ia dena hobeto egin dezake.

  * Clojure: modelatze bikaina; Lisp hurbilketa onena; exekuzio-denbora bikaina JVM-an.
  
  * Elixir: exekuzio-denbora bikaina, hedagarritasuna eta konkurrentzia barne; garatzaile-esperientzia bikaina; ekosistema nahiko txikia.

  * Erlang: exekuzio-denbora bikaina, hedagarritasuna eta konkurrentzia barne; garatzaile-esperientzia erronkatsua; ekosistema nahiko txikia.

  * Elm: oso itxaropentsua dirudi; IBM kasu-azterketa garrantzitsuak argitaratzen ari da emaitza onekin; ekosistema txikiagoa.

  * Flow: JavaScript-en hobekuntza interesgarria; hala ere, garatzaileak urruntzen ari dira.

  * Go: garatzaile-esperientzia bikaina; konkurrentzia bikaina; baina lengoaia mugatzen duten erabaki txarren ibilbidea.

  * Haskell: lengoaia funtzional onena; garatzaile-komunitate txikiagoa; ez du nahikoa produkzio-arrakasta argitaratu lortu.

  * Java: exekuzio-denbora bikaina; ekosistema bikaina; garatzaile-esperientzia kaskarra.

  * JavaScript: inoizko lengoaia ezagunena; ekosistema hedatuena.

  * Kotlin: Javaren asko konpontzen du; JetBrains-en euskarri bikaina; Javatik Kotlinera eramateko argitaratutako kasu onak.
  
  * Python: sistemen administraziorako lengoaia ezagunena; analisirako tresna bikainak; web esparru onak; baina Google-k Go-ren alde utzi zuen.

  * Ruby: inoizko garatzaile-esperientzia onena; web esparru onenak; komunitate atseginena; baina oso motela; paketatzeko nahiko zaila.

  * Rust: lengoaia berri onena; zero-abstrakzioaren azpimarra; konkurrentziaren azpimarra; hala ere ekosistema nahiko txikia; eta konpilatzaile-azelerazio mota batzuei buruzko muga nahita ditu, adib. memoriarako sarbide zuzenak esplizituki unsafe izan behar du.

  * TypeScript: tipoak gehitzen dizkio JavaScript-i; transpiler bikaina; garatzaileen arreta hazkorra JavaScript-etik TypeScript-era eramatean; Microsoft-en euskarri sendoa.

Erabaki dugu VM-ek orain behar ez dugun konpentsazio-multzo bat dutela, hala nola exekuzio-gaitasunak ematen dituen konplexutasun gehigarria.

Uste dugu gure oinarrizko erabakia zeharkako bi kezkak gidatzen dutela:

  * Exekuzio-abiadura azkarrenerako eta sistemarako sarbide estuenerako, JavaScript eta C aukeratuko genituzke.

  * Ia exekuzio-abiadura azkarrenerako eta ia sistemarako sarbide estuenerako, TypeScript eta Rust aukeratzen ditugu.

Aipamen berezia VM lengoaiei eta web esparruei, VM lengoaia bat nahi bagenu aukeratuko genituzkeenak:

  * Clojure eta Luminus

  * Java eta Spring

  * Elixir eta Phoenix


### Ondorioak

Front-end garatzaileek TypeScript ikasi beharko dute. Hau ziurrenik ikaskuntza-kurba erraza da garatzailearen lehen esperientzia JavaScript erabiltzea bada.

Back-end garatzaileek Rust ikasi beharko dute. Hau ziurrenik ikaskuntza-kurba ertaina da garatzailearen lehen esperientzia C/C++ erabiltzea bada, eta ikaskuntza-kurba zaila Java, Python, Ruby edo antzeko memoria kudeatuko lengoaiak erabiltzea bada. 

TypeScript eta Rust biak nahiko berriak dira. Horrek esan nahi du tresna askok oraindik ez dutela lengoaia hauetarako dokumentaziorik. Adibidez, devops hodia lengoaia hauetarako konfiguratu beharko da, eta orain arte, ebaluatzen ari garen devops tresnetako batek ere ez du lengoaia hauetarako adibide lehenetsirik.

TypeScript eta Rust-en konpilazio-denborak nahiko motelak dira. Honen zati bat lengoaien berritasunagatik izan daiteke. Konpilazio-denbora motelak arintzeko moduak aztertu nahi izan ditzakegu, hala nola eskaeraren araberako konpilazioa, konpilazio-konkurrentzia eta abar.

Lengoaia hauetarako IDE euskarria ez dago oraindik nonahi eta ez da oraindik lehen mailakoa. Adibidez, JetBrains-ek PyCharm IDE saltzen du Python-erako lehen mailako euskarriarekin, baina ez du Rust-erako lehen mailako euskarria duen IDE-rik saltzen; horren ordez, JetBrains-ek Rust plug-in bat erabil dezake, Python lengoaiaren euskarriarekin alderatuta Rust lengoaiaren euskarriaren %80 inguru ematen duena.


## Erlazionatuta


### Erlazionatutako erabakiak

Lengoaia hauekin bat datozen ekosistema-aukeretara zuzenduko gara.

Adibidez, lengoaia hauetarako gaitasun onak dituen IDE bat aukeratu nahi dugu.

Adibidez, gure front-end web esparrurako, TypeScript-era zuzentzen den esparru bat (adib. Vue) erabakitzeko aukera handiagoa dugu JavaScript hutsera zuzentzen den esparru bat (adib. React) baino.


### Erlazionatutako eskakizunak

Gure tresna-kate osoak lengoaia hauek onartu behar ditu.


### Erlazionatutako artefaktuak

Espero dugu sekretu batzuk ingurune-aldagaietara esportatu behar izatea.


### Erlazionatutako printzipioak

Bi aldiz neurtu, behin eraiki. Segurtasun pixka bat abiadura pixka baten aurretik lehenesten ari gara.

Exekuzio-denbora konpilazio-denbora baino baliotsuagoa da. Bezeroen erabilera garatzaileen erabileraren aurretik lehenesten ari gara.


## Oharrak

Edozein ohar hemen.
