# Programmēšanas valodas

Saturs:

* [Kopsavilkums](#kopsavilkums)
  * [Jautājums](#jautājums)
  * [Lēmums](#lēmums)
  * [Statuss](#statuss)
* [Detaļas](#detaļas)
  * [Pieņēmumi](#pieņēmumi)
  * [Ierobežojumi](#ierobežojumi)
  * [Pozīcijas](#pozīcijas)
  * [Arguments](#arguments)
  * [Sekas](#sekas)
* [Saistītais](#saistītais)
  * [Saistītie lēmumi](#saistītie-lēmumi)
  * [Saistītās prasības](#saistītās-prasības)
  * [Saistītie artefakti](#saistītie-artefakti)
  * [Saistītie principi](#saistītie-principi)
* [Piezīmes](#piezīmes)


## Kopsavilkums


### Jautājums

Mums jāizvēlas programmēšanas valodas savai programmatūrai. Mums ir divas galvenās vajadzības: priekšpuses programmēšanas valoda, kas piemērota tīmekļa lietojumprogrammām, un aizmugures programmēšanas valoda, kas piemērota serveru lietojumprogrammām.


### Lēmums

Priekšpusei izvēlamies TypeScript.

Aizmugurei izvēlamies Rust.


### Statuss

Izlemts. Esam atvērti jaunām alternatīvām, kad tās parādās.


## Detaļas


### Pieņēmumi

Priekšpuses lietojumprogrammas ir tipiskas:

  * Tipiski lietotāji un mijiedarbības

  * Tipiskas pārlūkprogrammas un sistēmas

  * Tipiskas izstrādes un izvietošanas

Priekšpuses lietojumprogrammas, visticamāk, strauji attīstīsies:

  * Mēs vēlamies nodrošināt ātras vieglas izstrādes, izvietošanas, iterācijas utt.

  * Mēs vērtējam pierādāmību, piemēram, tipu drošību, un esam gatavi veikt nedaudz vairāk darba, lai to sasniegtu.

  * Mums nav vajadzīga atpakaļsaderība ar mantotām sistēmām.

Aizmugures lietojumprogrammas ir augstākas par tipiskām:

  * Augstāki nekā tipiski mērķi attiecībā uz kvalitāti, īpaši pierādāmību, uzticamību, drošību utt.

  * Augstāki nekā tipiski mērķi attiecībā uz gandrīz reāllaiku, t. i., mēs nevēlamies pauzes virtuālās mašīnas atkritumu savākšanas (garbage collection) dēļ.

  * Augstāki nekā tipiski mērķi attiecībā uz funkcionālo programmēšanu, īpaši paralelizācijai, daudzkodolu apstrādei un atmiņas drošībai.

Mēs pieņemam zemāku kompilēšanas laika ātrumu par labu kompilēšanas laika drošībai un izpildlaika ātrumam.


### Ierobežojumi

Mums ir stingrs ierobežojums attiecībā uz valodām, kuras ir izmantojamas ar lielāko mākoņpakalpojumu sniedzēju funkciju pakalpojumiem, piemēram, Amazon Lambda.


### Pozīcijas

Mēs apsvērām šīs valodas:

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



### Arguments

Kopsavilkums pa valodām:

  * C: noraidīts zemās drošības dēļ; Rust var gandrīz visu izdarīt labāk.

  * C++: noraidīts, jo tas ir juceklis; Rust var gandrīz visu izdarīt labāk.

  * Clojure: izcila modelēšana; labākais Lisp tuvinājums; lieliska izpildvide uz JVM.
  
  * Elixir: izcila izpildvide, tostarp izvietojamība un vienlaicība; izcila izstrādātāja pieredze; samērā maza ekosistēma.

  * Erlang: izcila izpildvide, tostarp izvietojamība un vienlaicība; sarežģīta izstrādātāja pieredze; samērā maza ekosistēma.

  * Elm: izskatās ļoti daudzsološi; IBM publicē nozīmīgus gadījumu pētījumus ar labiem rezultātiem; mazāka ekosistēma.

  * Flow: interesants uzlabojums salīdzinājumā ar JavaScript; tomēr izstrādātāji no tā attālinās.

  * Go: izcila izstrādātāja pieredze; izcila vienlaicība; bet sliktu lēmumu vēsture, kas kropļo valodu.

  * Haskell: labākā funkcionālā valoda; mazāka izstrādātāju kopiena; nav sasniegusi pietiekami daudz publicētu ražošanas panākumu.

  * Java: izcila izpildvide; izcila ekosistēma; zem vidējā izstrādātāja pieredze.

  * JavaScript: populārākā valoda jebkad; visizplatītākā ekosistēma.

  * Kotlin: izlabo tik daudz no Java; lielisks JetBrains atbalsts; labi publicēti gadījumi par pāreju no Java uz Kotlin.
  
  * Python: populārākā valoda sistēmu administrēšanai; lieliski analītikas rīki; labi tīmekļa ietvari; bet Google to pameta par labu Go.

  * Ruby: labākā izstrādātāja pieredze jebkad; labākie tīmekļa ietvari; patīkamākā kopiena; bet ļoti lēna; nedaudz grūti pakotnēt.

  * Rust: labākā jaunā valoda; uzsvars uz nulles abstrakciju; uzsvars uz vienlaicību; tomēr samērā maza ekosistēma; un tai ir apzināti ierobežojumi dažiem kompilatora paātrinājumu veidiem, piem., tiešai piekļuvei atmiņai jābūt skaidri nedrošai (unsafe).

  * TypeScript: pievieno JavaScript tipus; lielisks transpilētājs; pieaugošs izstrādātāju uzsvars uz pāreju no JavaScript uz TypeScript; spēcīgs Microsoft atbalsts.

Mēs nolēmām, ka VM ir kompromisu kopums, kas mums tagad nav vajadzīgs, piemēram, papildu sarežģītība, kas nodrošina izpildlaika iespējas.

Mēs uzskatām, ka mūsu galveno lēmumu virza divi šķērsgriezuma apsvērumi:

  * Ātrākajam izpildlaika ātrumam un visciešākajai piekļuvei sistēmai mēs izvēlētos JavaScript un C.

  * Gandrīz ātrākajam izpildlaika ātrumam un gandrīz visciešākajai piekļuvei sistēmai mēs izvēlamies TypeScript un Rust.

Goda pieminēšana tiek VM valodām un tīmekļa ietvariem, ko mēs izvēlētos, ja vēlētos VM valodu:

  * Clojure un Luminus

  * Java un Spring

  * Elixir un Phoenix


### Sekas

Priekšpuses izstrādātājiem būs jāapgūst TypeScript. Tā, visticamāk, ir viegla mācīšanās līkne, ja izstrādātāja galvenā pieredze ir darbs ar JavaScript.

Aizmugures izstrādātājiem būs jāapgūst Rust. Tā, visticamāk, ir mērena mācīšanās līkne, ja izstrādātāja galvenā pieredze ir darbs ar C/C++, un grūta mācīšanās līkne, ja izstrādātāja galvenā pieredze ir darbs ar Java, Python, Ruby vai līdzīgām atmiņas pārvaldītām valodām. 

TypeScript un Rust abi ir samērā jauni. Tas nozīmē, ka daudziem rīkiem vēl nav dokumentācijas šīm valodām. Piemēram, DevOps cauruļvads būs jāiestata šīm valodām, un līdz šim neviens no DevOps rīkiem, ko mēs izvērtējam, nav ar noklusējuma piemēriem šīm valodām.

TypeScript un Rust kompilēšanas laiki ir diezgan lēni. Daļēji tas var būt valodu jaunuma dēļ. Mēs varētu vēlēties apskatīt, kā mazināt lēnos kompilēšanas laikus, piemēram, kompilēšana pēc pieprasījuma, kompilēšanas vienlaicība utt.

IDE atbalsts šīm valodām vēl nav visuresošs un vēl nav pirmšķirīgs. Piemēram, JetBrains pārdod PyCharm IDE ar pirmšķirīgu atbalstu Python, bet nepārdod IDE ar pirmšķirīgu atbalstu Rust; tā vietā JetBrains var izmantot Rust spraudni, kas nodrošina varbūt 80 % no Rust valodas atbalsta salīdzinājumā ar Python valodas atbalstu.


## Saistītais


### Saistītie lēmumi

Mēs censīsimies izvēlēties ekosistēmas, kas atbilst šīm valodām.

Piemēram, mēs vēlamies izvēlēties IDE, kam ir labas iespējas šīm valodām.

Piemēram, mūsu priekšpuses tīmekļa ietvaram mēs, visticamāk, izlemsim par ietvaru, kas parasti vērsts uz TypeScript (piem., Vue), nevis ietvaru, kas parasti vērsts uz tīru JavaScript (piem., React).


### Saistītās prasības

Visai mūsu rīku ķēdei jāatbalsta šīs valodas.


### Saistītie artefakti

Mēs sagaidām, ka varētu eksportēt dažus noslēpumus uz vides mainīgajiem.


### Saistītie principi

Septiņreiz nomēri, vienreiz izgriez. Mēs prioritizējam zināmu drošību pār zināmu ātrumu.

Izpildlaiks ir vērtīgāks par kompilēšanas laiku. Mēs prioritizējam klientu lietošanu pār izstrādātāju lietošanu.


## Piezīmes

Jebkādas piezīmes šeit.
