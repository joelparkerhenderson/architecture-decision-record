# Programski jezici

Sadržaj:

* [Sažetak](#sažetak)
  * [Problem](#problem)
  * [Odluka](#odluka)
  * [Status](#status)
* [Pojedinosti](#pojedinosti)
  * [Pretpostavke](#pretpostavke)
  * [Ograničenja](#ograničenja)
  * [Pozicije](#pozicije)
  * [Argument](#argument)
  * [Implikacije](#implikacije)
* [Povezano](#povezano)
  * [Povezane odluke](#povezane-odluke)
  * [Povezani zahtjevi](#povezani-zahtjevi)
  * [Povezani artefakti](#povezani-artefakti)
  * [Povezana načela](#povezana-načela)
* [Bilješke](#bilješke)


## Sažetak


### Problem

Moramo odabrati programske jezike za naš softver. Imamo dvije glavne potrebe: front-end programski jezik prikladan za web aplikacije i back-end programski jezik prikladan za poslužiteljske aplikacije.


### Odluka

Za front-end biramo TypeScript.

Za back-end biramo Rust.


### Status

Odlučeno. Otvoreni smo za nove alternative kako se pojave.


## Pojedinosti


### Pretpostavke

Front-end aplikacije su tipične:

  * Tipični korisnici i interakcije

  * Tipični preglednici i sustavi

  * Tipični razvoj i implementacije

Front-end aplikacije vjerojatno će se brzo razvijati:

  * Želimo osigurati brz i jednostavan razvoj, implementacije, iteracije itd.

  * Cijenimo dokazivost, poput sigurnosti tipova, i spremni smo uložiti nešto više rada da je postignemo.

  * Ne trebamo kompatibilnost s naslijeđenim sustavima.

Back-end aplikacije iznad su tipičnog:

  * Iznadprosječni ciljevi kvalitete, osobito dokazivosti, pouzdanosti, sigurnosti itd.

  * Iznadprosječni ciljevi bliski stvarnom vremenu, tj. ne želimo pauze zbog garbage collectiona virtualnog stroja.

  * Iznadprosječni ciljevi funkcijskog programiranja, osobito za paralelizaciju, višejezgrenu obradu i sigurnost memorije.

Prihvaćamo manju brzinu kompajliranja u korist sigurnosti pri kompajliranju i brzine izvođenja.


### Ograničenja

Imamo snažno ograničenje na jezike koji se mogu koristiti s uslugama glavnih pružatelja clouda za funkcije, poput Amazon Lambde.


### Pozicije

Razmatrali smo ove jezike:

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

Sažetak po jeziku:

  * C: odbijen zbog niske sigurnosti; Rust može gotovo sve učiniti bolje.

  * C++: odbijen jer je zbrka; Rust može gotovo sve učiniti bolje.

  * Clojure: izvrsno modeliranje; najbolja aproksimacija Lispa; sjajno izvršno okruženje na JVM-u.
  
  * Elixir: izvrsno izvršno okruženje, uključujući mogućnost implementacije i istodobnost; izvrsno iskustvo programera; relativno malen ekosustav.

  * Erlang: izvrsno izvršno okruženje, uključujući mogućnost implementacije i istodobnost; zahtjevno iskustvo programera; relativno malen ekosustav.

  * Elm: izgleda vrlo obećavajuće; IBM objavljuje značajne studije slučaja s dobrim rezultatima; manji ekosustav.

  * Flow: zanimljivo poboljšanje JavaScripta; međutim, programeri se udaljavaju od njega.

  * Go: izvrsno iskustvo programera; izvrsna istodobnost; ali povijest loših odluka koje sakate jezik.

  * Haskell: najbolji funkcijski jezik; manja zajednica programera; nije postigao dovoljno objavljenih produkcijskih uspjeha.

  * Java: izvrsno izvršno okruženje; izvrsan ekosustav; ispodprosječno iskustvo programera.

  * JavaScript: najpopularniji jezik ikad; najraširenji ekosustav.

  * Kotlin: popravlja toliko toga u Javi; izvrsna podrška JetBrainsa; dobri objavljeni slučajevi prelaska s Jave na Kotlin.
  
  * Python: najpopularniji jezik za administraciju sustava; sjajni alati za analitiku; dobri web okviri; ali Google ga je napustio u korist Goa.

  * Ruby: najbolje iskustvo programera ikad; najbolji web okviri; najljepša zajednica; ali vrlo spor; donekle težak za pakiranje.

  * Rust: najbolji novi jezik; naglasak na nultoj apstrakciji; naglasak na istodobnosti; međutim, relativno malen ekosustav; i namjerna ograničenja nekih vrsta ubrzanja kompajlera, npr. izravan pristup memoriji mora biti eksplicitno unsafe.

  * TypeScript: dodaje tipove u JavaScript; sjajan transpiler; sve veći naglasak programera na prelasku s JavaScripta na TypeScript; snažna podrška Microsofta.

Odlučili smo da virtualni strojevi imaju skup kompromisa koji nam sada nisu potrebni, poput dodatne složenosti koja pruža mogućnosti pri izvođenju.

Vjerujemo da našu temeljnu odluku pokreću dva međusektorska pitanja:

  * Za najbržu brzinu izvođenja i najuži pristup sustavu odabrali bismo JavaScript i C.

  * Za gotovo najbržu brzinu izvođenja i gotovo najuži pristup sustavu biramo TypeScript i Rust.

Počasna spominjanja idu jezicima s virtualnim strojem i web okvirima koje bismo odabrali da želimo jezik s virtualnim strojem:

  * Clojure i Luminus

  * Java i Spring

  * Elixir i Phoenix


### Implikacije

Front-end programeri morat će naučiti TypeScript. To je vjerojatno laka krivulja učenja ako je primarno iskustvo programera JavaScript.

Back-end programeri morat će naučiti Rust. To je vjerojatno umjerena krivulja učenja ako je primarno iskustvo programera C/C++, a teška krivulja učenja ako je primarno iskustvo programera Java, Python, Ruby ili slični jezici s upravljanom memorijom. 

TypeScript i Rust relativno su novi. To znači da mnogi alati još nemaju dokumentaciju za te jezike. Na primjer, devops cjevovod morat će se postaviti za te jezike, a za sada nijedan od devops alata koje vrednujemo nema zadane primjere za te jezike.

Vremena kompajliranja za TypeScript i Rust prilično su spora. Dio toga može biti zbog novosti jezika. Možda ćemo htjeti razmotriti kako ublažiti spora kompajliranja, primjerice kompajliranjem na zahtjev, istodobnim kompajliranjem itd.

Podrška IDE-a za te jezike još nije sveprisutna i još nije prvorazredna. Na primjer, JetBrains prodaje IDE PyCharm za prvorazrednu podršku za Python, ali ne prodaje IDE s prvorazrednom podrškom za Rust; umjesto toga JetBrains može koristiti dodatak za Rust koji pruža možda 80 % podrške za jezik Rust u odnosu na podršku za jezik Python.


## Povezano


### Povezane odluke

Težit ćemo izborima ekosustava koji su usklađeni s tim jezicima.

Na primjer, želimo odabrati IDE koji ima dobre mogućnosti za te jezike.

Na primjer, za naš front-end web okvir vjerojatnije ćemo se odlučiti za okvir koji teži TypeScriptu (npr. Vue) nego za okvir koji teži običnom JavaScriptu (npr. React).


### Povezani zahtjevi

Cijeli naš lanac alata mora podržavati te jezike.


### Povezani artefakti

Očekujemo da bismo mogli izvesti neke tajne u varijable okruženja.


### Povezana načela

Dvaput mjeri, jednom reži. Dajemo prednost određenoj sigurnosti pred određenom brzinom.

Vrijeme izvođenja vrjednije je od vremena kompajliranja. Dajemo prednost korištenju od strane kupaca pred korištenjem od strane programera.


## Bilješke

Sve bilješke ovdje.
