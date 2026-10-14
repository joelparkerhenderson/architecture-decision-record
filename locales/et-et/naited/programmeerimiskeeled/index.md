# Programmeerimiskeeled

Sisukord:

* [Kokkuvõte](#kokkuvõte)
  * [Küsimus](#küsimus)
  * [Otsus](#otsus)
  * [Olek](#olek)
* [Üksikasjad](#üksikasjad)
  * [Eeldused](#eeldused)
  * [Piirangud](#piirangud)
  * [Seisukohad](#seisukohad)
  * [Argument](#argument)
  * [Tagajärjed](#tagajärjed)
* [Seotud](#seotud)
  * [Seotud otsused](#seotud-otsused)
  * [Seotud nõuded](#seotud-nõuded)
  * [Seotud artefaktid](#seotud-artefaktid)
  * [Seotud põhimõtted](#seotud-põhimõtted)
* [Märkmed](#märkmed)


## Kokkuvõte


### Küsimus

Peame valima oma tarkvara jaoks programmeerimiskeeled. Meil on kaks suurt vajadust: veebirakendustele sobiv kasutajaliidese programmeerimiskeel ja serverirakendustele sobiv taustasüsteemi programmeerimiskeel.


### Otsus

Valime kasutajaliidese jaoks TypeScripti.

Valime taustasüsteemi jaoks Rusti.


### Olek

Otsustatud. Oleme avatud uutele alternatiividele, kui need ilmnevad.


## Üksikasjad


### Eeldused

Kasutajaliidese rakendused on tüüpilised:

  * Tüüpilised kasutajad ja interaktsioonid

  * Tüüpilised brauserid ja süsteemid

  * Tüüpilised arendused ja kasutuselevõtud

Kasutajaliidese rakendused arenevad tõenäoliselt kiiresti:

  * Tahame tagada kiired lihtsad arendused, kasutuselevõtud, iteratsioonid jne.

  * Hindame tõestatavust, nagu tüübiohutus, ja oleme nõus selle saavutamiseks veidi rohkem tööd tegema.

  * Me ei vaja pärandühilduvust.

Taustasüsteemi rakendused on tüüpilisest kõrgemad:

  * Tüüpilisest kõrgemad eesmärgid kvaliteedile, eriti tõestatavusele, töökindlusele, turvalisusele jne.

  * Tüüpilisest kõrgemad eesmärgid peaaegu reaalajale, st me ei taha pause virtuaalmasina prügikoristuse tõttu.

  * Tüüpilisest kõrgemad eesmärgid funktsionaalsele programmeerimisele, eriti paralleelimiseks, mitmetuumaliseks töötluseks ja mäluohutuseks.

Aktsepteerime madalamat kompileerimiskiirust kompileerimisaja ohutuse ja käitusaja kiiruse kasuks.


### Piirangud

Meil on tugev piirang keeltele, mida saab kasutada suuremate pilveteenuse pakkujate funktsiooniteenustega, nagu Amazon Lambda.


### Seisukohad

Kaalusime neid keeli:

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



### Argument

Kokkuvõte keele kohta:

  * C: tagasi lükatud madala ohutuse tõttu; Rust suudab peaaegu kõike paremini.

  * C++: tagasi lükatud, sest see on segadus; Rust suudab peaaegu kõike paremini.

  * Clojure: suurepärane modelleerimine; parim Lispi lähendus; suurepärane käitusaeg JVM-is.
  
  * Elixir: suurepärane käitusaeg, sealhulgas kasutuselevõetavus ja samaaegsus; suurepärane arendajakogemus; suhteliselt väike ökosüsteem.

  * Erlang: suurepärane käitusaeg, sealhulgas kasutuselevõetavus ja samaaegsus; keeruline arendajakogemus; suhteliselt väike ökosüsteem.

  * Elm: näeb väga paljulubav välja; IBM avaldab suuri juhtumiuuringuid heade tulemustega; väiksem ökosüsteem.

  * Flow: huvitav täiustus JavaScripti suhtes; arendajad aga loobuvad sellest.

  * Go: suurepärane arendajakogemus; suurepärane samaaegsus; kuid halbade otsuste ajalugu, mis keelt halvab.

  * Haskell: parim funktsionaalne keel; väiksem arendajate kogukond; pole saavutanud piisavalt avaldatud tootmisedusi.

  * Java: suurepärane käitusaeg; suurepärane ökosüsteem; keskpärane arendajakogemus.

  * JavaScript: kõigi aegade populaarseim keel; kõige laialdasem ökosüsteem.

  * Kotlin: parandab nii palju Javat; suurepärane toetus JetBrainsilt; head avaldatud juhtumid Java-lt Kotlinile portimisest.
  
  * Python: populaarseim keel süsteemihalduseks; suurepärased analüüsitööriistad; head veebiraamistikud; kuid Google loobus sellest Go kasuks.

  * Ruby: kõigi aegade parim arendajakogemus; parimad veebiraamistikud; kõige toredam kogukond; kuid väga aeglane; mõnevõrra raske pakendada.

  * Rust: parim uus keel; rõhk nullabstraktsioonil; rõhk samaaegsusel; kuid suhteliselt väike ökosüsteem; ja sellel on tahtlikud piirangud mõnedele kompilaatori kiirendustele, nt otsene mälupöördus peab olema selgesõnaliselt unsafe.

  * TypeScript: lisab JavaScriptile tüübid; suurepärane transpilaator; kasvav arendajate rõhk JavaScriptist TypeScriptile portimisele; tugev toetus Microsoftilt.

Otsustasime, et VM-idel on kompromisside komplekt, mida me praegu ei vaja, näiteks täiendav keerukus, mis pakub käitusaja võimalusi.

Usume, et meie põhiotsust ajendavad kaks läbivat muret:

  * Kiireima käitusaja kiiruse ja tihedaima süsteemipöörduse jaoks valiksime JavaScripti ja C.

  * Peaaegu kiireima käitusaja kiiruse ja peaaegu tihedaima süsteemipöörduse jaoks valime TypeScripti ja Rusti.

Ausad mainimised lähevad VM-keeltele ja veebiraamistikele, mille valiksime, kui tahaksime VM-keelt:

  * Clojure ja Luminus

  * Java ja Spring

  * Elixir ja Phoenix


### Tagajärjed

Kasutajaliidese arendajad peavad õppima TypeScripti. See on tõenäoliselt lihtne õppimiskõver, kui arendaja peamine kogemus on JavaScripti kasutamine.

Taustasüsteemi arendajad peavad õppima Rusti. See on tõenäoliselt mõõdukas õppimiskõver, kui arendaja peamine kogemus on C/C++ kasutamine, ja raske õppimiskõver, kui arendaja peamine kogemus on Java, Python, Ruby või sarnaste mäluhaldusega keelte kasutamine. 

TypeScript ja Rust on mõlemad suhteliselt uued. See tähendab, et paljudel tööriistadel pole veel nende keelte jaoks dokumentatsiooni. Näiteks devopsi torujuhe tuleb nende keelte jaoks üles seada ja siiani pole ühelgi meie hinnatavatest devopsi tööriistadest nende keelte jaoks vaikenäiteid.

TypeScripti ja Rusti kompileerimisajad on üsna aeglased. Osa sellest võib tuleneda keelte uudsusest. Võime tahta vaadata, kuidas aeglaseid kompileerimisaegu leevendada, näiteks nõudmisel kompileerimise, kompileerimise samaaegsuse jne abil.

IDE tugi nendele keeltele ei ole veel kõikjal olemas ega esmaklassiline. Näiteks JetBrains müüb PyCharm IDE-d Pythoni esmaklassilise toe jaoks, kuid ei müü IDE-d Rusti esmaklassilise toega; selle asemel saab JetBrains kasutada Rusti pluginat, mis pakub võib-olla 80% Rusti keeletoest võrreldes Pythoni keeletoega.


## Seotud


### Seotud otsused

Püüame valida ökosüsteemivalikuid, mis on nende keeltega kooskõlas.

Näiteks tahame valida IDE, millel on nende keelte jaoks head võimalused.

Näiteks oma kasutajaliidese veebiraamistiku jaoks otsustame tõenäolisemalt raamistiku kasuks, mis kaldub TypeScripti poole (nt Vue), kui raamistiku kasuks, mis kaldub tavalise JavaScripti poole (nt React).


### Seotud nõuded

Kogu meie tööriistaahel peab neid keeli toetama.


### Seotud artefaktid

Eeldame, et võime mõned saladused keskkonnamuutujatesse eksportida.


### Seotud põhimõtted

Mõõda kaks korda, ehita üks kord. Seame mõningase ohutuse mõningase kiiruse ees esikohale.

Käitusaeg on väärtuslikum kui kompileerimisaeg. Seame klientide kasutuse arendajate kasutuse ees esikohale.


## Märkmed

Mis tahes märkmed siin.
