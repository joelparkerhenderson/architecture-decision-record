# Înregistrare a deciziei de arhitectură: framework CSS

Cuprins:

- [Rezumat](#rezumat)
  - [Problemă](#problemă)
  - [Decizie](#decizie)
  - [Stare](#stare)
- [Detalii](#detalii)
  - [Ipoteze](#ipoteze)
  - [Constrângeri](#constrângeri)
  - [Poziții](#poziții)
  - [Argument](#argument)
  - [Implicații](#implicații)
- [Conexe](#conexe)
  - [Decizii conexe](#decizii-conexe)
  - [Cerințe conexe](#cerințe-conexe)
  - [Artefacte conexe](#artefacte-conexe)
  - [Principii conexe](#principii-conexe)
- [Note](#note)


## Rezumat


### Problemă

Vrem să folosim un framework CSS pentru a crea aplicațiile noastre web:

  * Vrem ca experiența utilizatorului să fie rapidă și fiabilă, pe toate browserele populare și dimensiunile de ecran.

  * Vrem iterare rapidă asupra designului, aspectului, UI/UX etc.

  * Vrem aplicații responsive, în special pentru ecrane mai mici, precum cele ale dispozitivelor mobile, ecrane mai mari, precum cele panoramice 4K, și ecrane dinamice, precum afișajele rotative.  


### Decizie

S-a decis Bulma.


### Stare

S-a decis Bulma. Suntem deschiși la noi alegeri de framework CSS pe măsură ce apar.


## Detalii


### Ipoteze

Vrem să creăm aplicații web moderne, rapide, fiabile, responsive etc.

Aplicațiile web moderne tipice reduc/elimină utilizarea jQuery din mai multe motive: 

  * JavaScript modern introduce treptat multe capabilități pe care le oferea jQuery, deci jQuery este mai puțin necesar, iar există module mai bune/mai rapide/mai mici care oferă implementări specifice

  * Abordarea largă a jQuery este manipularea directă a DOM, ceea ce este un anti-tipar pentru framework-urile JavaScript moderne (de exemplu React, Vue, Svelte)

  * jQuery interferează cu el însuși dacă este încărcat de două ori etc.


### Constrângeri

Dacă alegem un framework CSS care folosește jQuery, atunci suntem obligați să importăm jQuery. De exemplu, Semantic UI folosește jQuery, iar Tachyons nu.

Dacă alegem un framework CSS minimal, renunțăm la componente ale framework-ului pe care le-am putea dori acum sau în curând. De exemplu, Semantic UI oferă un carusel de imagini, iar Tachyons nu.


### Poziții

Am luat în considerare renunțarea la orice framework. Aceasta pare încă viabilă, mai ales că CSS grid oferă mare parte din ce ne trebuie pentru proiectul nostru..

Am luat în considerare multe framework-uri CSS printr-o triere rapidă pe o listă scurtă: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons etc. Cele două alegeri ale noastre pentru o analiză mai aprofundată sunt Semantic UI (pentru că are abordarea cea mai semantică) și Bulma (pentru că are abordarea cea mai ușoară, care oferă componentele pe care le dorim acum).

Am luat în considerare Semantic UI. Acesta oferă multe componente, inclusiv cele pe care le dorim pentru proiectul nostru: file, grile, butoane etc. Am făcut un pilot cu Semantic UI în două moduri: folosind fișiere CDN obișnuite și folosind depozite NPM. Am reușit cu Semantic UI într-o pagină HTML statică, dar nu am reușit în intervalul de timp alocat construirii unui SPA JavaScript (în principal din cauza problemelor de încărcare jQuery). Am descoperit că alți programatori le-au cerut dezvoltatorilor Semantic UI să creeze o versiune fără jQuery, din aceleași motive ca ale noastre. Alți programatori cer de mulți ani o versiune fără jQuery, dar dezvoltatorii au spus nu și au afirmat că orice versiune fără jQuery ar fi prea greu de scris, de exemplu ~„proiectul Semantic UI are peste 22.000 de puncte de contact care folosesc jQuery”.

Exemplu cu Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Am luat în considerare Bulma. Bulma are multe capabilități similare cu Semantic UI, deși nu atât de multe componente sofisticate. Bulma este construit cu tehnici moderne, de exemplu fără jQuery. Bulma are unele componente terțe, dintre care unele am putea dori să le folosim.


Exemplu cu Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argument

Ca mai sus.

Mai exact, Semantic UI pare să aibă un semnal de avertizare atât din punct de vedere tehnologic (adică atâtea puncte de contact cu jQuery), cât și din punctul de vedere al conducerii (adică versiunea fără jQuery a primit un refuz categoric, în loc de încercarea unei foi de parcurs, a unei îmbunătățiri continue, a strângerii de donații etc.).


### Implicații

Dacă găsim un framework CSS bun, fără jQuery, aceasta este în general util și bun.


## Conexe


### Decizii conexe

Framework-ul CSS pe care îl alegem poate afecta testabilitatea.


### Cerințe conexe

Vrem să livrăm rapid o aplicație pur modernă. 

Nu vrem să pierdem timp lucrând cu framework-uri mai vechi (în special Semantic UI) care folosesc dependențe mai vechi (în special jQuery).


### Artefacte conexe

Afectează tot HTML-ul tipic care va folosi acest CSS.


### Principii conexe

Ușor reversibil.

Nevoia de viteză.


## Note

Orice note aici.
