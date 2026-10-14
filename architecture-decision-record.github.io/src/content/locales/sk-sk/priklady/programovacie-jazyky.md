# Programovacie jazyky

Obsah:

* [Zhrnutie](#zhrnutie)
  * [Problém](#problém)
  * [Rozhodnutie](#rozhodnutie)
  * [Stav](#stav)
* [Podrobnosti](#podrobnosti)
  * [Predpoklady](#predpoklady)
  * [Obmedzenia](#obmedzenia)
  * [Pozície](#pozície)
  * [Argument](#argument)
  * [Dôsledky](#dôsledky)
* [Súvisiace](#súvisiace)
  * [Súvisiace rozhodnutia](#súvisiace-rozhodnutia)
  * [Súvisiace požiadavky](#súvisiace-požiadavky)
  * [Súvisiace artefakty](#súvisiace-artefakty)
  * [Súvisiace princípy](#súvisiace-princípy)
* [Poznámky](#poznámky)


## Zhrnutie


### Problém

Musíme zvoliť programovacie jazyky pre náš softvér. Máme dve hlavné potreby: front-endový programovací jazyk vhodný pre webové aplikácie a back-endový programovací jazyk vhodný pre serverové aplikácie.


### Rozhodnutie

Pre front-end volíme TypeScript.

Pre back-end volíme Rust.


### Stav

Rozhodnuté. Sme otvorení novým alternatívam, keď sa objavia.


## Podrobnosti


### Predpoklady

Front-endové aplikácie sú typické:

  * Typickí používatelia a interakcie

  * Typické prehliadače a systémy

  * Typický vývoj a nasadenia

U front-endových aplikácií sa očakáva rýchly vývoj:

  * Chceme zabezpečiť rýchly a jednoduchý vývoj, nasadenia, iterácie atď.

  * Ceníme si dokázateľnosť, ako je typová bezpečnosť, a sme ochotní vynaložiť na jej dosiahnutie trochu viac práce.

  * Nepotrebujeme spätnú kompatibilitu.

Back-endové aplikácie sú nadštandardné:

  * Nadštandardné ciele kvality, najmä dokázateľnosť, spoľahlivosť, bezpečnosť atď.

  * Nadštandardné ciele takmer v reálnom čase, t. j. nechceme pauzy spôsobené garbage collectionom virtuálneho stroja.

  * Nadštandardné ciele funkcionálneho programovania, najmä pre paralelizáciu, viacjadrové spracovanie a bezpečnosť pamäte.

Akceptujeme nižšiu rýchlosť kompilácie v prospech bezpečnosti pri kompilácii a rýchlosti za behu.


### Obmedzenia

Máme silné obmedzenie na jazyky použiteľné so službami hlavných poskytovateľov cloudu pre funkcie, ako je Amazon Lambda.


### Pozície

Zvažovali sme tieto jazyky:

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

Zhrnutie podľa jazyka:

  * C: zamietnutý kvôli nízkej bezpečnosti; Rust dokáže takmer všetko lepšie.

  * C++: zamietnutý, pretože je to zmes; Rust dokáže takmer všetko lepšie.

  * Clojure: vynikajúce modelovanie; najlepšia aproximácia Lispu; skvelé runtime prostredie na JVM.
  
  * Elixir: vynikajúce runtime prostredie vrátane nasaditeľnosti a súbežnosti; vynikajúci zážitok vývojára; relatívne malý ekosystém.

  * Erlang: vynikajúce runtime prostredie vrátane nasaditeľnosti a súbežnosti; náročný zážitok vývojára; relatívne malý ekosystém.

  * Elm: vyzerá veľmi sľubne; IBM publikuje významné prípadové štúdie s dobrými výsledkami; menší ekosystém.

  * Flow: zaujímavé vylepšenie oproti JavaScriptu; vývojári sa od neho však odkláňajú.

  * Go: vynikajúci zážitok vývojára; vynikajúca súbežnosť; ale história zlých rozhodnutí, ktoré jazyk ochromujú.

  * Haskell: najlepší funkcionálny jazyk; menšia komunita vývojárov; nedosiahol dostatok publikovaných produkčných úspechov.

  * Java: vynikajúce runtime prostredie; vynikajúci ekosystém; podpriemerný zážitok vývojára.

  * JavaScript: najpopulárnejší jazyk vôbec; najrozšírenejší ekosystém.

  * Kotlin: opravuje toľko z Javy; vynikajúca podpora od JetBrains; dobré publikované prípady prenosu z Javy do Kotlinu.
  
  * Python: najpopulárnejší jazyk pre správu systémov; skvelé nástroje na analytiku; dobré webové frameworky; ale opustený Googlom v prospech Go.

  * Ruby: najlepší zážitok vývojára vôbec; najlepšie webové frameworky; najpríjemnejšia komunita; ale veľmi pomalý; trochu ťažko sa balí.

  * Rust: najlepší nový jazyk; dôraz na nulovú abstrakciu; dôraz na súbežnosť; má však relatívne malý ekosystém; a zámerné obmedzenia niektorých druhov zrýchlenia kompilátora, napr. priamy prístup do pamäte musí byť explicitne unsafe.

  * TypeScript: pridáva typy do JavaScriptu; skvelý transpilátor; rastúci dôraz vývojárov na prenos z JavaScriptu do TypeScriptu; silná podpora od Microsoftu.

Rozhodli sme sa, že virtuálne stroje majú súbor kompromisov, ktoré teraz nepotrebujeme, ako je dodatočná zložitosť, ktorá poskytuje schopnosti za behu.

Veríme, že naše základné rozhodnutie je poháňané dvoma prierezovými hľadiskami:

  * Pre najrýchlejšiu rýchlosť za behu a najtesnejší prístup k systému by sme zvolili JavaScript a C.

  * Pre takmer najrýchlejšiu rýchlosť za behu a takmer najtesnejší prístup k systému volíme TypeScript a Rust.

Čestné uznania patria jazykom s virtuálnym strojom a webovým frameworkom, ktoré by sme zvolili, keby sme chceli jazyk s virtuálnym strojom:

  * Clojure a Luminus

  * Java a Spring

  * Elixir a Phoenix


### Dôsledky

Front-endoví vývojári sa budú musieť naučiť TypeScript. Ide pravdepodobne o ľahkú krivku učenia, ak je primárna skúsenosť vývojára s JavaScriptom.

Back-endoví vývojári sa budú musieť naučiť Rust. Ide pravdepodobne o strednú krivku učenia, ak je primárna skúsenosť vývojára s C/C++, a o ťažkú krivku učenia, ak je primárna skúsenosť vývojára s Javou, Pythonom, Ruby alebo podobnými jazykmi so správou pamäte. 

TypeScript aj Rust sú relatívne nové. To znamená, že mnohé nástroje zatiaľ nemajú dokumentáciu pre tieto jazyky. Napríklad devops pipeline bude treba pre tieto jazyky nastaviť a zatiaľ žiadny z devops nástrojov, ktoré hodnotíme, nemá predvolené príklady pre tieto jazyky.

Časy kompilácie TypeScriptu a Rustu sú pomerne pomalé. Časť z toho môže byť spôsobená novosťou jazykov. Možno sa budeme chcieť pozrieť na to, ako zmierniť pomalé kompilácie, napríklad kompiláciou na požiadanie, súbežnou kompiláciou atď.

Podpora IDE pre tieto jazyky ešte nie je všadeprítomná a ešte nie je prvotriedna. Napríklad JetBrains predáva IDE PyCharm s prvotriednou podporou Pythonu, ale nepredáva IDE s prvotriednou podporou Rustu; namiesto toho môže JetBrains použiť zásuvný modul pre Rust, ktorý poskytuje možno 80 % podpory jazyka Rust v porovnaní s podporou jazyka Python.


## Súvisiace


### Súvisiace rozhodnutia

Budeme smerovať k voľbám ekosystému, ktoré zodpovedajú týmto jazykom.

Napríklad chceme zvoliť IDE, ktoré má dobré schopnosti pre tieto jazyky.

Napríklad pre náš front-endový webový framework sa skôr rozhodneme pre framework, ktorý smeruje k TypeScriptu (napr. Vue), než pre framework, ktorý smeruje k obyčajnému JavaScriptu (napr. React).


### Súvisiace požiadavky

Celý náš toolchain musí tieto jazyky podporovať.


### Súvisiace artefakty

Očakávame, že niektoré tajomstvá exportujeme do premenných prostredia.


### Súvisiace princípy

Dvakrát meraj, raz rež. Uprednostňujeme určitú bezpečnosť pred určitou rýchlosťou.

Runtime je cennejší než čas kompilácie. Uprednostňujeme používanie zákazníkmi pred používaním vývojármi.


## Poznámky

Akékoľvek poznámky tu.
