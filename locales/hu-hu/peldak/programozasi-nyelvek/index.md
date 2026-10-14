# Programozási nyelvek

Tartalom:

* [Összefoglaló](#összefoglaló)
  * [Probléma](#probléma)
  * [Döntés](#döntés)
  * [Állapot](#állapot)
* [Részletek](#részletek)
  * [Feltevések](#feltevések)
  * [Megszorítások](#megszorítások)
  * [Álláspontok](#álláspontok)
  * [Érv](#érv)
  * [Következmények](#következmények)
* [Kapcsolódó](#kapcsolódó)
  * [Kapcsolódó döntések](#kapcsolódó-döntések)
  * [Kapcsolódó követelmények](#kapcsolódó-követelmények)
  * [Kapcsolódó artefaktumok](#kapcsolódó-artefaktumok)
  * [Kapcsolódó alapelvek](#kapcsolódó-alapelvek)
* [Megjegyzések](#megjegyzések)


## Összefoglaló


### Probléma

Programozási nyelveket kell választanunk a szoftverünkhöz. Két fő igényünk van: webalkalmazásokhoz alkalmas front-end programozási nyelv és kiszolgálóalkalmazásokhoz alkalmas back-end programozási nyelv.


### Döntés

A TypeScriptet választjuk a front-endhez.

A Rustot választjuk a back-endhez.


### Állapot

Eldöntve. Nyitottak vagyunk az új alternatívákra, ahogy felmerülnek.


## Részletek


### Feltevések

A front-end alkalmazások tipikusak:

  * Tipikus felhasználók és interakciók

  * Tipikus böngészők és rendszerek

  * Tipikus fejlesztések és telepítések

A front-end alkalmazások valószínűleg gyorsan fejlődnek:

  * Gyors, egyszerű fejlesztéseket, telepítéseket, iterációkat stb. szeretnénk biztosítani.

  * Értékeljük a bizonyíthatóságot, például a típusbiztonságot, és hajlandóak vagyunk egy kicsit több munkát végezni az eléréséért.

  * Nincs szükségünk régi rendszerekkel való kompatibilitásra.

A back-end alkalmazások a tipikusnál magasabb igényűek:

  * A tipikusnál magasabb minőségi célok, különösen a bizonyíthatóság, megbízhatóság, biztonság stb. terén.

  * A tipikusnál magasabb célok a közel valós idejűség terén, azaz nem akarunk szüneteket a virtuális gép szemétgyűjtése miatt.

  * A tipikusnál magasabb célok a funkcionális programozás terén, különösen a párhuzamosítás, a többmagos feldolgozás és a memóriabiztonság terén.

Elfogadjuk az alacsonyabb fordítási sebességet a fordítási idejű biztonság és a futási sebességek javára.


### Megszorítások

Erős megszorításunk van a nagy felhőszolgáltatók függvényszolgáltatásaival, mint az Amazon Lambda, használható nyelvekre.


### Álláspontok

Ezeket a nyelveket fontoltuk meg:

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



### Érv

Összefoglaló nyelvenként:

  * C: elutasítva az alacsony biztonság miatt; a Rust szinte mindent jobban tud.

  * C++: elutasítva, mert egy zűrzavar; a Rust szinte mindent jobban tud.

  * Clojure: kiváló modellezés; a legjobb Lisp-közelítés; nagyszerű futtatókörnyezet a JVM-en.
  
  * Elixir: kiváló futtatókörnyezet, beleértve a telepíthetőséget és a párhuzamosságot; kiváló fejlesztői élmény; viszonylag kis ökoszisztéma.

  * Erlang: kiváló futtatókörnyezet, beleértve a telepíthetőséget és a párhuzamosságot; kihívást jelentő fejlesztői élmény; viszonylag kis ökoszisztéma.

  * Elm: nagyon ígéretesnek tűnik; az IBM jelentős esettanulmányokat tesz közzé jó eredményekkel; kisebb ökoszisztéma.

  * Flow: érdekes fejlesztés a JavaScripthez képest; azonban a fejlesztők elfordulnak tőle.

  * Go: kiváló fejlesztői élmény; kiváló párhuzamosság; de a nyelvet megbénító rossz döntések története.

  * Haskell: a legjobb funkcionális nyelv; kisebb fejlesztői közösség; nem ért el elég publikált éles sikert.

  * Java: kiváló futtatókörnyezet; kiváló ökoszisztéma; átlag alatti fejlesztői élmény.

  * JavaScript: minden idők legnépszerűbb nyelve; a legelterjedtebb ökoszisztéma.

  * Kotlin: a Java oly sok hibáját javítja; kiváló támogatás a JetBrains részéről; jó publikált esetek a Javáról Kotlinra portolásra.
  
  * Python: a rendszeradminisztráció legnépszerűbb nyelve; nagyszerű elemzőeszközök; jó webes keretrendszerek; de a Google a Go javára elhagyta.

  * Ruby: minden idők legjobb fejlesztői élménye; a legjobb webes keretrendszerek; a legkedvesebb közösség; de nagyon lassú; némileg nehezen csomagolható.

  * Rust: a legjobb új nyelv; a zéró absztrakció hangsúlya; a párhuzamosság hangsúlya; azonban viszonylag kis ökoszisztéma; és szándékos korlátai vannak egyes fordítógyorsításoknak, pl. a közvetlen memóriahozzáférésnek kifejezetten nem biztonságosnak (unsafe) kell lennie.

  * TypeScript: típusokat ad a JavaScripthez; nagyszerű transpiler; a fejlesztők növekvő hangsúlya a JavaScriptről TypeScriptre portoláson; erős támogatás a Microsofttól.

Úgy döntöttünk, hogy a virtuális gépeknek (VM) vannak olyan kompromisszumai, amelyekre most nincs szükségünk, például további bonyolultság, amely futásidejű képességeket nyújt.

Úgy véljük, hogy alapdöntésünket két keresztmetszeti szempont vezérli:

  * A leggyorsabb futási sebességhez és a legszorosabb rendszerhozzáféréshez JavaScriptet és C-t választanánk.

  * A közel leggyorsabb futási sebességhez és közel legszorosabb rendszerhozzáféréshez TypeScriptet és Rustot választunk.

Megtisztelő említést kapnak azok a VM-nyelvek és webes keretrendszerek, amelyeket választanánk, ha VM-nyelvet akarnánk:

  * Clojure és Luminus

  * Java és Spring

  * Elixir és Phoenix


### Következmények

A front-end fejlesztőknek meg kell tanulniuk a TypeScriptet. Ez valószínűleg könnyű tanulási görbe, ha a fejlesztő fő tapasztalata a JavaScript.

A back-end fejlesztőknek meg kell tanulniuk a Rustot. Ez valószínűleg mérsékelt tanulási görbe, ha a fejlesztő fő tapasztalata a C/C++, és nehéz tanulási görbe, ha a fejlesztő fő tapasztalata a Java, Python, Ruby vagy hasonló memóriakezelt nyelvek. 

A TypeScript és a Rust is viszonylag új. Ez azt jelenti, hogy sok eszköznek még nincs dokumentációja ezekhez a nyelvekhez. Például a devops-folyamatot be kell állítani ezekhez a nyelvekhez, és eddig az általunk értékelt devops-eszközök egyikének sincsenek alapértelmezett példái ezekhez a nyelvekhez.

A TypeScript és a Rust fordítási ideje elég lassú. Ennek egy része a nyelvek újdonságának tudható be. Érdemes megnézni, hogyan mérsékelhetjük a lassú fordítási időket, például igény szerinti fordítással, fordítási párhuzamossággal stb.

Az IDE-támogatás ezekhez a nyelvekhez még nem mindenütt jelen lévő, és még nem elsőrangú. Például a JetBrains árulja a PyCharm IDE-t a Python elsőrangú támogatásával, de nem árul olyan IDE-t, amely a Rust elsőrangú támogatását nyújtja; ehelyett a JetBrains használhat egy Rust-bővítményt, amely talán a Rust nyelv támogatásának 80%-át nyújtja a Python nyelv támogatásához képest.


## Kapcsolódó


### Kapcsolódó döntések

Olyan ökoszisztéma-választásokra fogunk törekedni, amelyek összhangban vannak ezekkel a nyelvekkel.

Például olyan IDE-t szeretnénk választani, amely jó képességekkel rendelkezik ezekhez a nyelvekhez.

Például a front-end webes keretrendszerünkhöz nagyobb valószínűséggel döntünk a TypeScript felé hajló keretrendszer (pl. Vue) mellett, mint a sima JavaScript felé hajló keretrendszer (pl. React) mellett.


### Kapcsolódó követelmények

A teljes eszközláncunknak támogatnia kell ezeket a nyelveket.


### Kapcsolódó artefaktumok

Várjuk, hogy egyes titkokat környezeti változókba exportálhatunk.


### Kapcsolódó alapelvek

Kétszer mérj, egyszer építs. Némi biztonságot előnyben részesítünk némi sebességgel szemben.

A futásidő értékesebb, mint a fordítási idő. Az ügyfelek általi használatot előnyben részesítjük a fejlesztők általi használattal szemben.


## Megjegyzések

Bármilyen megjegyzés ide.
