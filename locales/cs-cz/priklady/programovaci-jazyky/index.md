# Programovací jazyky

Obsah:

* [Shrnutí](#shrnutí)
  * [Problém](#problém)
  * [Rozhodnutí](#rozhodnutí)
  * [Stav](#stav)
* [Podrobnosti](#podrobnosti)
  * [Předpoklady](#předpoklady)
  * [Omezení](#omezení)
  * [Stanoviska](#stanoviska)
  * [Argument](#argument)
  * [Důsledky](#důsledky)
* [Související](#související)
  * [Související rozhodnutí](#související-rozhodnutí)
  * [Související požadavky](#související-požadavky)
  * [Související artefakty](#související-artefakty)
  * [Související principy](#související-principy)
* [Poznámky](#poznámky)


## Shrnutí


### Problém

Musíme zvolit programovací jazyky pro náš software. Máme dvě hlavní potřeby: front-endový programovací jazyk vhodný pro webové aplikace a back-endový programovací jazyk vhodný pro serverové aplikace.


### Rozhodnutí

Pro front-end volíme TypeScript.

Pro back-end volíme Rust.


### Stav

Rozhodnuto. Jsme otevřeni novým alternativám, jakmile se objeví.


## Podrobnosti


### Předpoklady

Front-endové aplikace jsou typické:

  * Typičtí uživatelé a interakce

  * Typické prohlížeče a systémy

  * Typický vývoj a nasazení

U front-endových aplikací se očekává rychlý vývoj:

  * Chceme zajistit rychlý a snadný vývoj, nasazení, iterace atd.

  * Ceníme si prokazatelnosti, například typové bezpečnosti, a jsme ochotni udělat k jejímu dosažení trochu víc práce.

  * Nepotřebujeme zpětnou kompatibilitu.

Back-endové aplikace jsou nadprůměrné:

  * Nadprůměrné cíle kvality, zejména prokazatelnosti, spolehlivosti, bezpečnosti atd.

  * Nadprůměrné cíle blízké reálnému času, tj. nechceme pauzy způsobené garbage collection virtuálního stroje.

  * Nadprůměrné cíle funkcionálního programování, zejména pro paralelizaci, vícejádrové zpracování a bezpečnost paměti.

Přijímáme nižší rychlost kompilace ve prospěch bezpečnosti při kompilaci a rychlosti za běhu.


### Omezení

Máme silné omezení na jazyky použitelné se službami hlavních poskytovatelů cloudu pro funkce, například Amazon Lambda.


### Stanoviska

Zvažovali jsme tyto jazyky:

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

Shrnutí podle jazyka:

  * C: zamítnuto kvůli nízké bezpečnosti; Rust zvládne téměř vše lépe.

  * C++: zamítnuto, protože je to změť; Rust zvládne téměř vše lépe.

  * Clojure: vynikající modelování; nejlepší aproximace Lispu; skvělý runtime na JVM.
  
  * Elixir: vynikající runtime včetně nasaditelnosti a souběžnosti; vynikající zkušenost vývojáře; relativně malý ekosystém.

  * Erlang: vynikající runtime včetně nasaditelnosti a souběžnosti; náročná zkušenost vývojáře; relativně malý ekosystém.

  * Elm: vypadá velmi slibně; IBM zveřejňuje významné případové studie s dobrými výsledky; menší ekosystém.

  * Flow: zajímavé vylepšení oproti JavaScriptu; vývojáři se však od něj odklánějí.

  * Go: vynikající zkušenost vývojáře; vynikající souběžnost; ale historie špatných rozhodnutí, která jazyk ochromují.

  * Haskell: nejlepší funkcionální jazyk; menší komunita vývojářů; nedosáhl dostatečného počtu publikovaných produkčních úspěchů.

  * Java: vynikající runtime; vynikající ekosystém; podprůměrná zkušenost vývojáře.

  * JavaScript: nejpopulárnější jazyk všech dob; nejrozšířenější ekosystém.

  * Kotlin: opravuje tolik z Javy; vynikající podpora od JetBrains; dobré publikované případy portování z Javy do Kotlinu.
  
  * Python: nejpopulárnější jazyk pro správu systémů; skvělé nástroje pro analytiku; dobré webové frameworky; ale opuštěný Googlem ve prospěch Go.

  * Ruby: nejlepší zkušenost vývojáře vůbec; nejlepší webové frameworky; nejpříjemnější komunita; ale velmi pomalý; poněkud obtížně se balí.

  * Rust: nejlepší nový jazyk; důraz na nulovou abstrakci; důraz na souběžnost; má však relativně malý ekosystém; a záměrná omezení některých druhů zrychlení kompilátoru, např. přímý přístup do paměti musí být explicitně unsafe.

  * TypeScript: přidává typy do JavaScriptu; skvělý transpiler; rostoucí důraz vývojářů na portování z JavaScriptu do TypeScriptu; silná podpora od Microsoftu.

Rozhodli jsme se, že virtuální stroje mají soubor kompromisů, které nyní nepotřebujeme, například další složitost, která poskytuje schopnosti za běhu.

Věříme, že naše zásadní rozhodnutí je řízeno dvěma průřezovými hledisky:

  * Pro nejrychlejší rychlost za běhu a nejtěsnější přístup k systému bychom zvolili JavaScript a C.

  * Pro téměř nejrychlejší rychlost za běhu a téměř nejtěsnější přístup k systému volíme TypeScript a Rust.

Čestné zmínky patří jazykům s virtuálním strojem a webovým frameworkům, které bychom zvolili, kdybychom chtěli jazyk s virtuálním strojem:

  * Clojure a Luminus

  * Java a Spring

  * Elixir a Phoenix


### Důsledky

Front-endoví vývojáři se budou muset naučit TypeScript. Jde pravděpodobně o snadnou křivku učení, pokud má vývojář primární zkušenost s JavaScriptem.

Back-endoví vývojáři se budou muset naučit Rust. Jde pravděpodobně o střední křivku učení, pokud má vývojář primární zkušenost s C/C++, a o těžkou křivku učení, pokud má vývojář primární zkušenost s Javou, Pythonem, Ruby nebo podobnými jazyky se správou paměti. 

TypeScript i Rust jsou relativně nové. To znamená, že mnoho nástrojů zatím nemá pro tyto jazyky dokumentaci. Například devops pipeline bude třeba pro tyto jazyky nastavit a zatím žádný z devops nástrojů, které hodnotíme, nemá výchozí příklady pro tyto jazyky.

Doby kompilace TypeScriptu a Rustu jsou poměrně pomalé. Část z toho může být způsobena novostí jazyků. Možná se budeme chtít podívat, jak zmírnit pomalé kompilace, například kompilací na vyžádání, souběžnou kompilací atd.

Podpora IDE pro tyto jazyky zatím není všudypřítomná a zatím není prvotřídní. Například JetBrains prodává IDE PyCharm s prvotřídní podporou Pythonu, ale neprodává IDE s prvotřídní podporou Rustu; místo toho může JetBrains použít zásuvný modul pro Rust, který poskytuje snad 80 % podpory jazyka Rust ve srovnání s podporou jazyka Python.


## Související


### Související rozhodnutí

Budeme směřovat k volbám ekosystému, které odpovídají těmto jazykům.

Například chceme zvolit IDE, které má dobré schopnosti pro tyto jazyky.

Například pro náš front-endový webový framework se spíše rozhodneme pro framework, který míří na TypeScript (např. Vue), než pro framework, který míří na čistý JavaScript (např. React).


### Související požadavky

Celý náš toolchain musí tyto jazyky podporovat.


### Související artefakty

Očekáváme, že některá tajemství exportujeme do proměnných prostředí.


### Související principy

Dvakrát měř, jednou řež. Upřednostňujeme určitou bezpečnost před určitou rychlostí.

Runtime je cennější než čas kompilace. Upřednostňujeme používání zákazníky před používáním vývojáři.


## Poznámky

Jakékoli poznámky zde.
