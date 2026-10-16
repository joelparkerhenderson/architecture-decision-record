# Programski jeziki

Vsebina:

* [Povzetek](#povzetek)
  * [Vprašanje](#vprašanje)
  * [Odločitev](#odločitev)
  * [Stanje](#stanje)
* [Podrobnosti](#podrobnosti)
  * [Predpostavke](#predpostavke)
  * [Omejitve](#omejitve)
  * [Stališča](#stališča)
  * [Argument](#argument)
  * [Posledice](#posledice)
* [Povezano](#povezano)
  * [Povezane odločitve](#povezane-odločitve)
  * [Povezane zahteve](#povezane-zahteve)
  * [Povezani artefakti](#povezani-artefakti)
  * [Povezana načela](#povezana-načela)
* [Opombe](#opombe)


## Povzetek


### Vprašanje

Za svojo programsko opremo moramo izbrati programske jezike. Imamo dve glavni potrebi: programski jezik za uporabniški del, primeren za spletne aplikacije, in programski jezik za zaledje, primeren za strežniške aplikacije.


### Odločitev

Za uporabniški del izbiramo TypeScript.

Za zaledje izbiramo Rust.


### Stanje

Odločeno. Odprti smo za nove alternative, ko se pojavijo.


## Podrobnosti


### Predpostavke

Aplikacije uporabniškega dela so tipične:

  * Tipični uporabniki in interakcije

  * Tipični brskalniki in sistemi

  * Tipični razvoji in uvajanja

Aplikacije uporabniškega dela se bodo verjetno hitro razvijale:

  * Želimo zagotoviti hitre in preproste razvoje, uvajanja, iteracije itd.

  * Cenimo dokazljivost, kot je varnost tipov, in smo pripravljeni opraviti nekoliko več dela, da jo dosežemo.

  * Ne potrebujemo združljivosti s starejšimi sistemi.

Aplikacije zaledja so zahtevnejše od tipičnih:

  * Višji od tipičnih cilji glede kakovosti, zlasti dokazljivosti, zanesljivosti, varnosti itd.

  * Višji od tipičnih cilji glede skoraj realnega časa, tj. ne želimo premorov zaradi čiščenja pomnilnika (garbage collection) virtualnega stroja.

  * Višji od tipičnih cilji glede funkcijskega programiranja, zlasti za paralelizacijo, večjedrno obdelavo in varnost pomnilnika.

Sprejemamo daljše čase prevajanja v korist varnosti ob prevajanju in hitrosti ob izvajanju.


### Omejitve

Imamo močno omejitev glede jezikov, ki so uporabni z glavnimi storitvami ponudnikov oblaka za funkcije, kot je Amazon Lambda.


### Stališča

Preučili smo te jezike:

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

Povzetek po jezikih:

  * C: zavrnjen zaradi nizke varnosti; Rust zmore skoraj vse bolje.

  * C++: zavrnjen, ker je zmeda; Rust zmore skoraj vse bolje.

  * Clojure: odlično modeliranje; najboljši približek jezika Lisp; odlično izvajalno okolje na JVM.
  
  * Elixir: odlično izvajalno okolje, vključno z uvedljivostjo in sočasnostjo; odlična izkušnja razvijalcev; razmeroma majhen ekosistem.

  * Erlang: odlično izvajalno okolje, vključno z uvedljivostjo in sočasnostjo; zahtevna izkušnja razvijalcev; razmeroma majhen ekosistem.

  * Elm: videti je zelo obetavno; IBM objavlja pomembne študije primerov z dobrimi rezultati; manjši ekosistem.

  * Flow: zanimiva izboljšava JavaScripta; vendar se razvijalci od njega odmikajo.

  * Go: odlična izkušnja razvijalcev; odlična sočasnost; vendar zgodovina slabih odločitev, ki jezik pohabljajo.

  * Haskell: najboljši funkcijski jezik; manjša razvijalska skupnost; ni dosegel dovolj objavljenih produkcijskih uspehov.

  * Java: odlično izvajalno okolje; odličen ekosistem; podpovprečna izkušnja razvijalcev.

  * JavaScript: najbolj priljubljen jezik doslej; najbolj razširjen ekosistem.

  * Kotlin: odpravlja toliko pomanjkljivosti Jave; odlična podpora JetBrains; dobri objavljeni primeri prenosa iz Jave v Kotlin.
  
  * Python: najbolj priljubljen jezik za sistemsko administracijo; odlična orodja za analitiko; dobra spletna ogrodja; vendar ga je Google opustil v korist jezika Go.

  * Ruby: najboljša izkušnja razvijalcev doslej; najboljša spletna ogrodja; najprijetnejša skupnost; vendar zelo počasen; nekoliko težko pakiranje.

  * Rust: najboljši nov jezik; poudarek na ničelni abstrakciji; poudarek na sočasnosti; vendar razmeroma majhen ekosistem; in ima namerne omejitve pri nekaterih vrstah pospeševanja prevajalnika, npr. neposreden dostop do pomnilnika mora biti izrecno nevaren (unsafe).

  * TypeScript: JavaScriptu doda tipe; odličen transpiler; vse večji poudarek razvijalcev na prenosu iz JavaScripta v TypeScript; močna podpora Microsofta.

Odločili smo se, da imajo navidezni stroji (VM) nabor kompromisov, ki jih zdaj ne potrebujemo, na primer dodatno kompleksnost, ki zagotavlja zmožnosti izvajalnega okolja.

Verjamemo, da našo temeljno odločitev vodita dve prečni skrbi:

  * Za najhitrejšo hitrost izvajanja in najtesnejši dostop do sistema bi izbrali JavaScript in C.

  * Za skoraj najhitrejšo hitrost izvajanja in skoraj najtesnejši dostop do sistema izbiramo TypeScript in Rust.

Častne omembe gredo jezikom VM in spletnim ogrodjem, ki bi jih izbrali, če bi želeli jezik VM:

  * Clojure in Luminus

  * Java in Spring

  * Elixir in Phoenix


### Posledice

Razvijalci uporabniškega dela se bodo morali naučiti TypeScript. To je verjetno lahka krivulja učenja, če so primarne izkušnje razvijalca z uporabo JavaScripta.

Razvijalci zaledja se bodo morali naučiti Rust. To je verjetno zmerna krivulja učenja, če so primarne izkušnje razvijalca z uporabo C/C++, in težka krivulja učenja, če so primarne izkušnje razvijalca z uporabo Jave, Pythona, Rubyja ali podobnih jezikov z upravljanim pomnilnikom. 

TypeScript in Rust sta razmeroma nova. To pomeni, da veliko orodij za te jezike še nima dokumentacije. Na primer, cevovod DevOps bo treba postaviti za te jezike, in doslej nobeno od orodij DevOps, ki jih vrednotimo, nima privzetih primerov za te jezike.

Časi prevajanja za TypeScript in Rust so precej počasni. Nekaj tega je morda posledica novosti jezikov. Morda bomo želeli preučiti, kako omiliti počasne čase prevajanja, na primer s prevajanjem na zahtevo, sočasnim prevajanjem itd.

Podpora IDE za te jezike še ni vseprisotna in še ni prvovrstna. Na primer, JetBrains prodaja IDE PyCharm za prvovrstno podporo Pythonu, ne prodaja pa IDE s prvovrstno podporo za Rust; namesto tega lahko JetBrains uporablja vtičnik za Rust, ki zagotavlja morda 80 % podpore jeziku Rust v primerjavi s podporo jeziku Python.


## Povezano


### Povezane odločitve

Stremeli bomo k izbiram ekosistema, ki so usklajene s temi jeziki.

Na primer, želimo izbrati IDE, ki ima dobre zmožnosti za te jezike.

Na primer, pri spletnem ogrodju za uporabniški del se bomo verjetneje odločili za ogrodje, ki je običajno usmerjeno v TypeScript (npr. Vue), kot za ogrodje, ki je običajno usmerjeno v navaden JavaScript (npr. React).


### Povezane zahteve

Celotna naša veriga orodij mora podpirati te jezike.


### Povezani artefakti

Pričakujemo, da bomo nekatere skrivnosti morda izvozili v okoljske spremenljivke.


### Povezana načela

Dvakrat meri, enkrat zgradi. Nekoliko višjo prednost dajemo varnosti kot hitrosti.

Čas izvajanja je dragocenejši od časa prevajanja. Prednost dajemo uporabi s strani strank pred uporabo s strani razvijalcev.


## Opombe

Tu so vse opombe.
