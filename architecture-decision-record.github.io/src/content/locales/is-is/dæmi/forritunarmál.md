# Forritunarmál

Efnisyfirlit:

* [Samantekt](#samantekt)
  * [Vandamál](#vandamál)
  * [Ákvörðun](#ákvörðun)
  * [Staða](#staða)
* [Nánar](#nánar)
  * [Forsendur](#forsendur)
  * [Takmarkanir](#takmarkanir)
  * [Afstöður](#afstöður)
  * [Röksemd](#röksemd)
  * [Afleiðingar](#afleiðingar)
* [Tengt](#tengt)
  * [Tengdar ákvarðanir](#tengdar-ákvarðanir)
  * [Tengdar kröfur](#tengdar-kröfur)
  * [Tengdar afurðir](#tengdar-afurðir)
  * [Tengdar meginreglur](#tengdar-meginreglur)
* [Athugasemdir](#athugasemdir)


## Samantekt


### Vandamál

Við þurfum að velja forritunarmál fyrir hugbúnað okkar. Við höfum tvær meginþarfir: forritunarmál fyrir framenda sem hentar vefforritum og forritunarmál fyrir bakenda sem hentar þjónaforritum.


### Ákvörðun

Við veljum TypeScript fyrir framenda.

Við veljum Rust fyrir bakenda.


### Staða

Ákveðið. Við erum opin fyrir nýjum valkostum þegar þeir koma fram.


## Nánar


### Forsendur

Forrit á framenda eru dæmigerð:

  * Dæmigerðir notendur og samskipti

  * Dæmigerðir vafrar og kerfi

  * Dæmigerð þróun og uppsetning

Forrit á framenda munu líklega þróast hratt:

  * Við viljum tryggja hraða og auðvelda þróun, uppsetningu, endurtekningar o.s.frv.

  * Við metum sannanleika, svo sem tegundaöryggi, og erum sátt við að gera aðeins meira til að ná honum.

  * Við þurfum ekki eldri samhæfni.

Forrit á bakenda eru kröfuharðari en venjulega:

  * Kröfuharðari markmið en venjulega um gæði, einkum sannanleika, áreiðanleika, öryggi o.s.frv.

  * Kröfuharðari markmið en venjulega um nær-rauntíma, þ.e. við viljum ekki hlé vegna sorphirðu sýndarvéla.

  * Kröfuharðari markmið en venjulega um fallaforritun, einkum fyrir samhliðun, fjölkjarnavinnslu og minnisöryggi.

Við samþykkjum lægri þýðingarhraða í þágu öryggis við þýðingu og keyrsluhraða.


### Takmarkanir

Við höfum sterka takmörkun á málum sem hægt er að nota með þjónustu stórra skýjaveitna fyrir föll, svo sem Amazon Lambda.


### Afstöður

Við skoðuðum þessi mál:

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



### Röksemd

Samantekt fyrir hvert mál:

  * C: hafnað vegna lítils öryggis; Rust getur gert nánast allt betur.

  * C++: hafnað því það er óreiða; Rust getur gert nánast allt betur.

  * Clojure: framúrskarandi líkanagerð; besta nálgun á Lisp; frábært keyrsluumhverfi á JVM.
  
  * Elixir: framúrskarandi keyrsluumhverfi, þar á meðal uppsetning og samhliðun; framúrskarandi upplifun þróunaraðila; tiltölulega lítið vistkerfi.

  * Erlang: framúrskarandi keyrsluumhverfi, þar á meðal uppsetning og samhliðun; krefjandi upplifun þróunaraðila; tiltölulega lítið vistkerfi.

  * Elm: lítur mjög vel út; IBM birtir stórar tilviksrannsóknir með góðum árangri; minna vistkerfi.

  * Flow: áhugaverð framför miðað við JavaScript; hins vegar eru þróunaraðilar að færa sig frá því.

  * Go: framúrskarandi upplifun þróunaraðila; framúrskarandi samhliðun; en saga slæmra ákvarðana sem lama málið.

  * Haskell: besta fallamálið; minna þróunarsamfélag; hefur ekki náð nægum útgefnum árangri í framleiðslu.

  * Java: framúrskarandi keyrsluumhverfi; framúrskarandi vistkerfi; undir meðallagi upplifun þróunaraðila.

  * JavaScript: vinsælasta mál sem til hefur verið; útbreiddasta vistkerfið.

  * Kotlin: lagar svo margt í Java; framúrskarandi stuðningur frá JetBrains; góð útgefin dæmi um flutning frá Java í Kotlin.
  
  * Python: vinsælasta málið fyrir kerfisstjórn; frábær greiningarverkfæri; góðir veframmar; en yfirgefið af Google í þágu Go.

  * Ruby: besta upplifun þróunaraðila sem til hefur verið; bestu veframmarnir; vinalegasta samfélagið; en mjög hægt; nokkuð erfitt að pakka.

  * Rust: besta nýja málið; áhersla á núll-óhlutgervingu; áhersla á samhliðun; hins vegar tiltölulega lítið vistkerfi; og hefur viljandi takmörk á sumum tegundum þýðandahraðana, t.d. bein minnisaðgangur þarf að vera skýrt óöruggur.

  * TypeScript: bætir tegundum við JavaScript; frábær umþýðandi; vaxandi áhersla þróunaraðila á flutning frá JavaScript í TypeScript; sterkur stuðningur frá Microsoft.

Við ákváðum að sýndarvélar hafi safn málamiðlana sem við þurfum ekki núna, svo sem aukið flækjustig sem veitir keyrslugetu.

Við teljum að kjarnaákvörðun okkar sé knúin af tveimur þverlægum sjónarmiðum:

  * Fyrir mestan keyrsluhraða og þéttasta kerfisaðgang myndum við velja JavaScript og C.

  * Fyrir næstum mestan keyrsluhraða og næstum þéttasta kerfisaðgang veljum við TypeScript og Rust.

Heiðursviðurkenningar fá mál sýndarvéla og veframmar sem við myndum velja ef við vildum mál fyrir sýndarvél:

  * Clojure og Luminus

  * Java og Spring

  * Elixir og Phoenix


### Afleiðingar

Þróunaraðilar á framenda þurfa að læra TypeScript. Þetta er líklega auðveldur námsferill ef aðalreynsla þróunaraðilans er af JavaScript.

Þróunaraðilar á bakenda þurfa að læra Rust. Þetta er líklega miðlungs námsferill ef aðalreynsla þróunaraðilans er af C/C++ og erfiður námsferill ef aðalreynsla hans er af Java, Python, Ruby eða áþekkum málum með minnisstjórnun. 

TypeScript og Rust eru bæði tiltölulega ný. Þetta þýðir að mörg verkfæri hafa enn ekki skjölun fyrir þessi mál. Til dæmis þarf að setja upp devops-leiðsluna fyrir þessi mál, og hingað til hefur ekkert devops-verkfæranna sem við metum sjálfgefin dæmi fyrir þessi mál.

Þýðingartími fyrir TypeScript og Rust er nokkuð hægur. Hluti af þessu kann að stafa af nýjung málanna. Við gætum viljað skoða hvernig draga megi úr hægum þýðingartíma, svo sem með þýðingu eftir þörfum, samhliða þýðingu o.s.frv.

IDE-stuðningur fyrir þessi mál er enn ekki alls staðar og enn ekki fyrsta flokks. Til dæmis selur JetBrains PyCharm IDE með fyrsta flokks stuðningi við Python, en selur ekki IDE með fyrsta flokks stuðningi við Rust; í staðinn getur JetBrains notað Rust-viðbót sem veitir kannski 80% af stuðningi við Rust-málið miðað við stuðning við Python-málið.


## Tengt


### Tengdar ákvarðanir

Við munum stefna að vali á vistkerfi sem samræmist þessum málum.

Til dæmis viljum við velja IDE sem hefur góða getu fyrir þessi mál.

Til dæmis munum við fyrir veframma okkar á framenda frekar velja ramma sem hneigist til TypeScript (t.d. Vue) en ramma sem hneigist til hreins JavaScript (t.d. React).


### Tengdar kröfur

Öll verkfærakeðja okkar verður að styðja þessi mál.


### Tengdar afurðir

Við væntum þess að við gætum flutt út einhver leyndarmál í umhverfisbreytur.


### Tengdar meginreglur

Mældu tvisvar, smíðaðu einu sinni. Við setjum nokkurt öryggi í forgang umfram nokkurn hraða.

Keyrslutími er verðmætari en þýðingartími. Við setjum notkun viðskiptavina í forgang umfram notkun þróunaraðila.


## Athugasemdir

Allar athugasemdir hér.
