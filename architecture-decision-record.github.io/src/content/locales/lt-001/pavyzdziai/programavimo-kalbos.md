# Programavimo kalbos

Turinys:

* [Santrauka](#santrauka)
  * [Problema](#problema)
  * [Sprendimas](#sprendimas)
  * [Būsena](#būsena)
* [Detalės](#detalės)
  * [Prielaidos](#prielaidos)
  * [Apribojimai](#apribojimai)
  * [Pozicijos](#pozicijos)
  * [Argumentas](#argumentas)
  * [Implikacijos](#implikacijos)
* [Susiję](#susiję)
  * [Susiję sprendimai](#susiję-sprendimai)
  * [Susiję reikalavimai](#susiję-reikalavimai)
  * [Susiję artefaktai](#susiję-artefaktai)
  * [Susiję principai](#susiję-principai)
* [Pastabos](#pastabos)


## Santrauka


### Problema

Turime pasirinkti programavimo kalbas savo programinei įrangai. Turime du pagrindinius poreikius: priekinės dalies programavimo kalbą, tinkamą interneto programoms, ir galinės dalies programavimo kalbą, tinkamą serverio programoms.


### Sprendimas

Priekinei daliai renkamės TypeScript.

Galinei daliai renkamės Rust.


### Būsena

Nuspręsta. Atviri naujoms alternatyvoms, kai jos atsiras.


## Detalės


### Prielaidos

Priekinės dalies programos yra tipinės:

  * Tipiniai naudotojai ir sąveikos

  * Tipinės naršyklės ir sistemos

  * Tipiniai kūrimai ir diegimai

Priekinės dalies programos greičiausiai greitai keisis:

  * Norime užtikrinti greitą ir lengvą kūrimą, diegimą, iteracijas ir pan.

  * Vertiname įrodomumą, pavyzdžiui, tipų saugumą, ir sutinkame padaryti šiek tiek daugiau darbo jam pasiekti.

  * Mums nereikia suderinamumo su paveldėtomis sistemomis.

Galinės dalies programos yra aukštesnės nei tipinės:

  * Aukštesni nei tipiniai kokybės tikslai, ypač įrodomumo, patikimumo, saugumo ir pan.

  * Aukštesni nei tipiniai beveik realaus laiko tikslai, t. y. nenorime pauzių dėl virtualiosios mašinos šiukšlių surinkimo.

  * Aukštesni nei tipiniai funkcinio programavimo tikslai, ypač lygiagretinimo, daugiabranduolio apdorojimo ir atminties saugumo požiūriu.

Sutinkame su mažesniu kompiliavimo laiko greičiu mainais už kompiliavimo laiko saugumą ir vykdymo laiko greitį.


### Apribojimai

Turime stiprų apribojimą kalboms, kurias galima naudoti su didžiųjų debesijos teikėjų funkcijų paslaugomis, pavyzdžiui, Amazon Lambda.


### Pozicijos

Svarstėme šias kalbas:

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



### Argumentas

Kiekvienos kalbos santrauka:

  * C: atmesta dėl mažo saugumo; Rust beveik viską gali padaryti geriau.

  * C++: atmesta, nes tai netvarka; Rust beveik viską gali padaryti geriau.

  * Clojure: puikus modeliavimas; geriausias Lisp aproksimavimas; puiki vykdymo aplinka JVM.
  
  * Elixir: puiki vykdymo aplinka, įskaitant diegiamumą ir lygiagretumą; puiki programuotojo patirtis; gana maža ekosistema.

  * Erlang: puiki vykdymo aplinka, įskaitant diegiamumą ir lygiagretumą; sudėtinga programuotojo patirtis; gana maža ekosistema.

  * Elm: atrodo labai perspektyvi; IBM skelbia svarbius atvejų tyrimus su gerais rezultatais; mažesnė ekosistema.

  * Flow: įdomus JavaScript patobulinimas; tačiau programuotojai nuo jo tolsta.

  * Go: puiki programuotojo patirtis; puikus lygiagretumas; tačiau blogų sprendimų istorija, kuri sužlugdo kalbą.

  * Haskell: geriausia funkcinė kalba; mažesnė programuotojų bendruomenė; nepasiekė pakankamai paskelbtų gamybinių sėkmių.

  * Java: puiki vykdymo aplinka; puiki ekosistema; prastesnė nei vidutinė programuotojo patirtis.

  * JavaScript: populiariausia kalba kada nors; plačiausiai paplitusi ekosistema.

  * Kotlin: ištaiso tiek daug Java trūkumų; puiki JetBrains parama; geri paskelbti perkėlimo iš Java į Kotlin atvejai.
  
  * Python: populiariausia sistemų administravimo kalba; puikūs analitikos įrankiai; geri interneto karkasai; tačiau Google ją paliko dėl Go.

  * Ruby: geriausia programuotojo patirtis kada nors; geriausi interneto karkasai; maloniausia bendruomenė; tačiau labai lėta; šiek tiek sunku supakuoti.

  * Rust: geriausia nauja kalba; pabrėžiamas nulinės abstrakcijos principas; pabrėžiamas lygiagretumas; tačiau gana maža ekosistema; ir turi sąmoningų tam tikrų kompiliatoriaus pagreitinimų apribojimų, pvz., tiesioginė prieiga prie atminties turi būti aiškiai nesaugi (unsafe).

  * TypeScript: prideda tipus prie JavaScript; puikus transpiliatorius; vis labiau programuotojai orientuojasi į perkėlimą iš JavaScript į TypeScript; stipri Microsoft parama.

Nusprendėme, kad VM turi kompromisų rinkinį, kurio šiuo metu mums nereikia, pavyzdžiui, papildomą sudėtingumą, suteikiantį vykdymo laiko galimybes.

Manome, kad mūsų pagrindinį sprendimą lemia du skersiniai rūpesčiai:

  * Greičiausiam vykdymo greičiui ir sandariausiai prieigai prie sistemos rinktumėmės JavaScript ir C.

  * Beveik greičiausiam vykdymo greičiui ir beveik sandariausiai prieigai prie sistemos renkamės TypeScript ir Rust.

Garbingai paminime VM kalbas ir interneto karkasus, kuriuos rinktumėmės, jei norėtume VM kalbos:

  * Clojure ir Luminus

  * Java ir Spring

  * Elixir ir Phoenix


### Implikacijos

Priekinės dalies programuotojams reikės išmokti TypeScript. Tai tikriausiai lengva mokymosi kreivė, jei programuotojo pagrindinė patirtis yra naudojant JavaScript.

Galinės dalies programuotojams reikės išmokti Rust. Tai tikriausiai vidutinė mokymosi kreivė, jei programuotojo pagrindinė patirtis yra naudojant C/C++, ir sunki mokymosi kreivė, jei programuotojo pagrindinė patirtis yra naudojant Java, Python, Ruby ar panašias atmintį valdomas kalbas. 

TypeScript ir Rust abi yra gana naujos. Tai reiškia, kad daugeliui įrankių dar nėra dokumentacijos šioms kalboms. Pavyzdžiui, devops konvejerį reikės nustatyti šioms kalboms, ir kol kas nė vienas iš mūsų vertinamų devops įrankių neturi numatytųjų pavyzdžių šioms kalboms.

TypeScript ir Rust kompiliavimo laikai yra gana lėti. Dalis to gali būti dėl kalbų naujumo. Galbūt norėsime išnagrinėti, kaip sušvelninti lėtus kompiliavimo laikus, pavyzdžiui, kompiliavimu pagal poreikį, kompiliavimo lygiagretumu ir pan.

IDE palaikymas šioms kalboms dar nėra visur ir dar nėra pirmos klasės. Pavyzdžiui, JetBrains parduoda PyCharm IDE su pirmos klasės Python palaikymu, bet neparduoda IDE su pirmos klasės Rust palaikymu; vietoj to JetBrains gali naudoti Rust papildinį, kuris suteikia galbūt 80 % Rust kalbos palaikymo, palyginti su Python kalbos palaikymu.


## Susiję


### Susiję sprendimai

Siekiame ekosistemos pasirinkimų, atitinkančių šias kalbas.

Pavyzdžiui, norime pasirinkti IDE, turintį geras šių kalbų galimybes.

Pavyzdžiui, savo priekinės dalies interneto karkasui labiau tikėtina, kad rinksimės karkasą, orientuotą į TypeScript (pvz., Vue), o ne karkasą, orientuotą į gryną JavaScript (pvz., React).


### Susiję reikalavimai

Visa mūsų įrankių grandinė turi palaikyti šias kalbas.


### Susiję artefaktai

Tikimės, kad kai kurias paslaptis galime eksportuoti į aplinkos kintamuosius.


### Susiję principai

Septynis kartus matuok, vieną kartą pjauk. Teikiame pirmenybę tam tikram saugumui, o ne tam tikram greičiui.

Vykdymo laikas vertingesnis už kompiliavimo laiką. Teikiame pirmenybę klientų naudojimui, o ne programuotojų naudojimui.


## Pastabos

Čia bet kokios pastabos.
