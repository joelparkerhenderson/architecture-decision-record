# Programméiersproochen

Inhalt:

* [Zesummefaassung](#zesummefaassung)
  * [Problem](#problem)
  * [Decisioun](#decisioun)
  * [Zoustand](#zoustand)
* [Detailer](#detailer)
  * [Viraussetzungen](#viraussetzungen)
  * [Restriktiounen](#restriktiounen)
  * [Positiounen](#positiounen)
  * [Argument](#argument)
  * [Implikatiounen](#implikatiounen)
* [Verwandt](#verwandt)
  * [Verwandt Decisiounen](#verwandt-decisiounen)
  * [Verwandt Ufuerderungen](#verwandt-ufuerderungen)
  * [Verwandt Artefakten](#verwandt-artefakten)
  * [Verwandt Prinzipien](#verwandt-prinzipien)
* [Notizen](#notizen)


## Zesummefaassung


### Problem

Mir mussen Programméiersprooche fir eis Software wielen. Mir hunn zwee Haaptbedierfnisser: eng Front-End-Programméiersprooch, déi fir Webapplikatioune gëeegent ass, an eng Back-End-Programméiersprooch, déi fir Serverapplikatioune gëeegent ass.


### Decisioun

Mir wielen TypeScript fir de Front-End.

Mir wielen Rust fir de Back-End.


### Zoustand

Decidéiert. Mir si fir nei Alternativen op, soubal se opkommen.


## Detailer


### Viraussetzungen

D'Front-End-Applikatioune sinn typesch:

  * Typesch Benotzer an Interaktiounen

  * Typesch Browser a Systemer

  * Typesch Entwécklungen an Deployments

D'Front-End-Applikatioune wäerte sech wahrscheinlech séier entwéckelen:

  * Mir wëllen séier einfach Entwécklungen, Deployments, Iteratiounen, asw. suergen.

  * Mir schätzen Beweisbarkeet, wéi Typesécherheet, a mir hu kee Problem, e bëssen méi Aarbecht ze maachen, fir se ze erreechen.

  * Mir brauchen keng Legacy-Kompatibilitéit.

D'Back-End-Applikatioune si méi héich wéi typesch:

  * Méi héich wéi typesch Ziler fir d'Qualitéit, besonnesch Beweisbarkeet, Zouverlässegkeet, Sécherheet, asw.

  * Méi héich wéi typesch Ziler fir Quasi-Echtzäit, dat heescht, mir wëllen keng Paus wéinst der Garbage Collection vun der virtueller Maschinn.

  * Méi héich wéi typesch Ziler fir funktionell Programméierung, besonnesch fir Parallelisatioun, Multi-Core-Veraarbechtung a Memory-Sécherheet.

Mir akzeptéieren méi niddreg Kompiléierzäiten zugonschte vun der Kompiléierzäit-Sécherheet a vun der Laufzäit-Vitess.


### Restriktiounen

Mir hunn eng staark Restriktioun op Sproochen, déi mat de Funktiounsservicer vu groussen Cloud-Providere benotzbar sinn, wéi Amazon Lambda.


### Positiounen

Mir hunn dës Sprooche berécksiichtegt:

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

Zesummefaassung pro Sprooch:

  * C: ofgeleent wéinst niddreger Sécherheet; Rust kann bal alles besser.

  * C++: ofgeleent, well et e Chaos ass; Rust kann bal alles besser.

  * Clojure: exzellent Modelléierung; bescht Lisp-Annäherung; super Runtime op der JVM.
  
  * Elixir: exzellent Runtime, dorënner Deploybarkeet a Concurrency; exzellent Entwécklererfahrung; relativ klenge Ökosystem.

  * Erlang: exzellent Runtime, dorënner Deploybarkeet a Concurrency; erausfuerdernd Entwécklererfahrung; relativ klenge Ökosystem.

  * Elm: gesäit ganz villverspriechend aus; IBM publizéiert grouss Fallstudien mat gudde Resultater; méi klenge Ökosystem.

  * Flow: interessant Verbesserung vu JavaScript; awer; Entwéckler gi vun deem ewech.

  * Go: exzellent Entwécklererfahrung; exzellent Concurrency; awer eng Geschicht vu schlechten Decisiounen, déi d'Sprooch lähmen.

  * Haskell: bescht funktionell Sprooch; méi kleng Entwécklercommunautéit; huet nach net genuch publizéiert Produktiounserfolleger erreecht.

  * Java: exzellent Runtime; exzellent Ökosystem; ënnerduerchschnëttlech Entwécklererfahrung.

  * JavaScript: populärste Sprooch ëmmer; am wäitste verbreete Ökosystem.

  * Kotlin: fixt sou vill vu Java; exzellent Ënnerstëtzung vu JetBrains; gutt publizéiert Fäll vum Portéiere vu Java op Kotlin.
  
  * Python: populärste Sprooch fir Systemadministratioun; super Analytik-Tooling; gutt Web-Frameworks; awer vu Google zugonschte vu Go opginn.

  * Ruby: bescht Entwécklererfahrung ëmmer; bescht Web-Frameworks; schéinsten Communautéit; awer ganz lues; e bëssen schwéier ze packen.

  * Rust: bescht nei Sprooch; Fokus op Null-Abstraktioun; Fokus op Concurrency; awer relativ klenge Ökosystem; an huet bewosst Limitten bei e puer Aarte vu Kompiler-Beschleunigungen, z.B. direkten Memory-Zougang muss explizit unsafe sinn.

  * TypeScript: füügt Typen zu JavaScript derbäi; super Transpiler; wuessenden Entwécklerfokus op de Portéiere vu JavaScript op TypeScript; staark Ënnerstëtzung vu Microsoft.

Mir hunn decidéiert, datt VMs e Set u Kompromësser hunn, déi mir momentan net brauchen, wéi zousätzlech Komplexitéit, déi Laufzäitfäegkeeten bitt.

Mir gleewen, datt eis Kärdecisioun vun zwee funktiounsiwwergräifende Bedenken gedriwwe gëtt:

  * Fir déi séierst Laufzäit-Vitess an den ënnerschten Systemzougang wieele mir JavaScript a C.

  * Fir bal déi séierst Laufzäit-Vitess an bal den ënnerschten Systemzougang wieele mir TypeScript a Rust.

Éierend Erwähnunge ginn un d'VM-Sproochen a Web-Frameworks, déi mir géifen auswielen, wa mir eng VM-Sprooch wollten:

  * Clojure a Luminus

  * Java a Spring

  * Elixir a Phoenix


### Implikatiounen

Front-End-Entwéckler mussen TypeScript léieren. Dat ass wahrscheinlech eng einfach Léierkurve, wann d'Haapterfahrung vum Entwéckler d'Notzung vu JavaScript ass.

Back-End-Entwéckler mussen Rust léieren. Dat ass wahrscheinlech eng moderat Léierkurve, wann d'Haapterfahrung vum Entwéckler d'Notzung vu C/C++ ass, an eng schwéier Léierkurve, wann d'Haapterfahrung vum Entwéckler d'Notzung vu Java, Python, Ruby oder ähnleche Sprooche mat verwaltetem Memory ass. 

TypeScript a Rust si béid relativ nei. Dat bedeit, datt vill Tools nach keng Dokumentatioun fir dës Sproochen hunn. Zum Beispill muss d'Devops-Pipeline fir dës Sprooche opgesat ginn, an bis elo huet keen vun den Devops-Tools, déi mir evaluéieren, Standardbeispiller fir dës Sproochen.

D'Kompiléierzäite fir TypeScript a Rust sinn zimlech lues. En Deel dovun kann un der Newheet vun de Sproochen leien. Mir wëllen eventuell kucken, wéi mir lues Kompiléierzäite mildere kënnen, z.B. duerch Compile-on-Demand, Compile-Concurrency, asw.

D'IDE-Ënnerstëtzung fir dës Sproochen ass nach net iwwerall verbreet an nach net éischtklassesch. Zum Beispill verkeeft JetBrains d'PyCharm-IDE fir éischtklasseg Ënnerstëtzung fir Python, verkeeft awer keng IDE mat éischtklasseger Ënnerstëtzung fir Rust; amplaz kann JetBrains e Rust-Plug-in benotzen, dee vläicht 80% vun der Rust-Sproochënnerstëtzung par rapport zur Python-Sproochënnerstëtzung bitt.


## Verwandt


### Verwandt Decisiounen

Mir striewen Ökosystem-Choixe un, déi zu dëse Sprooche passen.

Zum Beispill wëlle mir eng IDE wielen, déi gutt Fäegkeeten fir dës Sprooche huet.

Zum Beispill, fir eist Front-End-Web-Framework, wäerte mir eis méi wahrscheinlech fir e Framework entscheeden, dat dozou tendéiert, TypeScript unzepeilen (z.B. Vue), wéi fir e Framework, dat dozou tendéiert, einfacht JavaScript unzepeilen (z.B. React).


### Verwandt Ufuerderungen

Eis ganz Toolchain muss dës Sprooche ënnerstëtzen.


### Verwandt Artefakten

Mir erwaarden, datt mir eventuell e puer Geheimnisser an Emgebungsvariabele exportéieren.


### Verwandt Prinzipien

Zweemol moossen, eemol bauen. Mir prioritiséieren e bëssen Sécherheet iwwer e bëssen Vitess.

D'Laufzäit ass méi wäertvoll wéi d'Kompiléierzäit. Mir prioritiséieren d'Notzung duerch Clienten iwwer d'Notzung duerch Entwéckler.


## Notizen

All Notizen hei.
