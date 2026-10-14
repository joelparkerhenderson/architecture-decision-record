# Limbaje de programare

Cuprins:

* [Rezumat](#rezumat)
  * [Problemă](#problemă)
  * [Decizie](#decizie)
  * [Stare](#stare)
* [Detalii](#detalii)
  * [Ipoteze](#ipoteze)
  * [Constrângeri](#constrângeri)
  * [Poziții](#poziții)
  * [Argument](#argument)
  * [Implicații](#implicații)
* [Conexe](#conexe)
  * [Decizii conexe](#decizii-conexe)
  * [Cerințe conexe](#cerințe-conexe)
  * [Artefacte conexe](#artefacte-conexe)
  * [Principii conexe](#principii-conexe)
* [Note](#note)


## Rezumat


### Problemă

Trebuie să alegem limbaje de programare pentru software-ul nostru. Avem două nevoi majore: un limbaj de programare front-end potrivit pentru aplicații web și un limbaj de programare back-end potrivit pentru aplicații server.


### Decizie

Alegem TypeScript pentru front-end.

Alegem Rust pentru back-end.


### Stare

Decis. Suntem deschiși la alternative noi pe măsură ce apar.


## Detalii


### Ipoteze

Aplicațiile front-end sunt tipice:

  * Utilizatori și interacțiuni tipice

  * Browsere și sisteme tipice

  * Dezvoltări și implementări tipice

Aplicațiile front-end vor evolua probabil rapid:

  * Vrem să asigurăm dezvoltări, implementări, iterații etc. rapide și ușoare.

  * Prețuim demonstrabilitatea, precum siguranța tipurilor, și suntem de acord să facem ceva mai multă muncă pentru a o obține.

  * Nu avem nevoie de compatibilitate cu sisteme vechi.

Aplicațiile back-end sunt peste media tipică:

  * Obiective de calitate peste media tipică, în special demonstrabilitate, fiabilitate, securitate etc.

  * Obiective peste media tipică pentru apropierea de timpul real, adică nu vrem pauze din cauza colectării gunoiului de către mașina virtuală.

  * Obiective peste media tipică pentru programarea funcțională, în special pentru paralelizare, procesare multi-core și siguranța memoriei.

Acceptăm viteze mai mici la compilare în favoarea siguranței la compilare și a vitezelor la execuție.


### Constrângeri

Avem o constrângere puternică privind limbajele care pot fi folosite cu serviciile de funcții ale marilor furnizori de cloud, precum Amazon Lambda.


### Poziții

Am luat în considerare aceste limbaje:

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

Rezumat pentru fiecare limbaj:

  * C: respins din cauza siguranței scăzute; Rust poate face aproape totul mai bine.

  * C++: respins pentru că este un talmeș-balmeș; Rust poate face aproape totul mai bine.

  * Clojure: modelare excelentă; cea mai bună aproximare de Lisp; mediu de execuție excelent pe JVM.
  
  * Elixir: mediu de execuție excelent, inclusiv implementabilitate și concurență; experiență excelentă pentru dezvoltatori; ecosistem relativ mic.

  * Erlang: mediu de execuție excelent, inclusiv implementabilitate și concurență; experiență dificilă pentru dezvoltatori; ecosistem relativ mic.

  * Elm: pare foarte promițător; IBM publică studii de caz importante cu rezultate bune; ecosistem mai mic.

  * Flow: o îmbunătățire interesantă față de JavaScript; totuși, dezvoltatorii se îndepărtează de el.

  * Go: experiență excelentă pentru dezvoltatori; concurență excelentă; dar un istoric de decizii proaste care paralizează limbajul.

  * Haskell: cel mai bun limbaj funcțional; comunitate de dezvoltatori mai mică; nu a obținut suficiente succese publicate în producție.

  * Java: mediu de execuție excelent; ecosistem excelent; experiență mediocră pentru dezvoltatori.

  * JavaScript: cel mai popular limbaj din toate timpurile; cel mai răspândit ecosistem.

  * Kotlin: repară atât de multe din Java; sprijin excelent din partea JetBrains; cazuri publicate bune de portare de la Java la Kotlin.
  
  * Python: cel mai popular limbaj pentru administrarea sistemelor; instrumente de analiză excelente; framework-uri web bune; dar abandonat de Google în favoarea Go.

  * Ruby: cea mai bună experiență pentru dezvoltatori din toate timpurile; cele mai bune framework-uri web; cea mai plăcută comunitate; dar foarte lent; oarecum greu de împachetat.

  * Rust: cel mai bun limbaj nou; accent pe zero abstractizare; accent pe concurență; totuși ecosistem relativ mic; și are limite deliberate asupra unor tipuri de accelerări ale compilatorului, de exemplu accesul direct la memorie trebuie să fie explicit nesigur (unsafe).

  * TypeScript: adaugă tipuri la JavaScript; transpilator excelent; accent crescând al dezvoltatorilor pe portarea de la JavaScript la TypeScript; sprijin puternic din partea Microsoft.

Am decis că mașinile virtuale (VM) implică un set de compromisuri de care nu avem nevoie acum, precum complexitate suplimentară care oferă capabilități la execuție.

Credem că decizia noastră de bază este determinată de două aspecte transversale:

  * Pentru cea mai rapidă viteză de execuție și cel mai strâns acces la sistem, am alege JavaScript și C.

  * Pentru o viteză de execuție apropiată de cea mai rapidă și un acces la sistem apropiat de cel mai strâns, alegem TypeScript și Rust.

Mențiuni de onoare merg către limbajele VM și framework-urile web pe care le-am alege dacă am vrea un limbaj VM:

  * Clojure și Luminus

  * Java și Spring

  * Elixir și Phoenix


### Implicații

Dezvoltatorii front-end vor trebui să învețe TypeScript. Aceasta este probabil o curbă de învățare ușoară dacă experiența principală a dezvoltatorului este JavaScript.

Dezvoltatorii back-end vor trebui să învețe Rust. Aceasta este probabil o curbă de învățare moderată dacă experiența principală a dezvoltatorului este C/C++ și o curbă de învățare dificilă dacă experiența principală a dezvoltatorului este Java, Python, Ruby sau limbaje similare cu memorie gestionată. 

TypeScript și Rust sunt ambele relativ noi. Aceasta înseamnă că multe instrumente nu au încă documentație pentru aceste limbaje. De exemplu, fluxul devops va trebui configurat pentru aceste limbaje și, până acum, niciunul dintre instrumentele devops pe care le evaluăm nu are exemple implicite pentru aceste limbaje.

Timpii de compilare pentru TypeScript și Rust sunt destul de lenți. O parte din aceasta poate fi din cauza noutății limbajelor. Ar putea merita să vedem cum putem atenua timpii lungi de compilare, de exemplu prin compilare la cerere, concurență la compilare etc.

Suportul IDE pentru aceste limbaje nu este încă omniprezent și nu este încă de prim rang. De exemplu, JetBrains vinde IDE-ul PyCharm cu suport de prim rang pentru Python, dar nu vinde un IDE cu suport de prim rang pentru Rust; în schimb, JetBrains poate folosi un plugin Rust care oferă poate 80% din suportul limbajului Rust față de suportul limbajului Python.


## Conexe


### Decizii conexe

Vom tinde spre alegeri de ecosistem aliniate cu aceste limbaje.

De exemplu, vrem să alegem un IDE care are capabilități bune pentru aceste limbaje.

De exemplu, pentru framework-ul nostru web front-end, este mai probabil să alegem un framework care tinde spre TypeScript (de exemplu Vue) decât un framework care tinde spre JavaScript simplu (de exemplu React).


### Cerințe conexe

Întregul nostru lanț de instrumente trebuie să suporte aceste limbaje.


### Artefacte conexe

Ne așteptăm să putem exporta unele secrete în variabile de mediu.


### Principii conexe

Măsoară de două ori, construiește o dată. Prioritizăm o anumită siguranță în fața unei anumite viteze.

Timpul de execuție este mai valoros decât timpul de compilare. Prioritizăm utilizarea de către clienți în fața utilizării de către dezvoltatori.


## Note

Orice note aici.
