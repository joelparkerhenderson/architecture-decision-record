# Záznam architektonického rozhodnutí: CSS framework

Obsah:

- [Shrnutí](#shrnutí)
  - [Problém](#problém)
  - [Rozhodnutí](#rozhodnutí)
  - [Stav](#stav)
- [Podrobnosti](#podrobnosti)
  - [Předpoklady](#předpoklady)
  - [Omezení](#omezení)
  - [Stanoviska](#stanoviska)
  - [Argument](#argument)
  - [Důsledky](#důsledky)
- [Související](#související)
  - [Související rozhodnutí](#související-rozhodnutí)
  - [Související požadavky](#související-požadavky)
  - [Související artefakty](#související-artefakty)
  - [Související principy](#související-principy)
- [Poznámky](#poznámky)


## Shrnutí


### Problém

Chceme použít CSS framework k vytváření našich webových aplikací:

  * Chceme, aby uživatelský zážitek byl rychlý a spolehlivý, ve všech oblíbených prohlížečích a velikostech obrazovky.

  * Chceme rychlou iteraci designu, rozvržení, UI/UX atd.

  * Chceme responzivní aplikace, zejména pro menší obrazovky, například na mobilních zařízeních, větší obrazovky, například na širokoúhlých 4K, a dynamické obrazovky, například otočné displeje.  


### Rozhodnutí

Rozhodnuto pro Bulma.


### Stav

Rozhodnuto pro Bulma. Jsme otevřeni novým volbám CSS frameworku, jakmile se objeví.


## Podrobnosti


### Předpoklady

Chceme vytvářet webové aplikace, které jsou moderní, rychlé, spolehlivé, responzivní atd.

Typické moderní webové aplikace omezují/vylučují používání jQuery z několika důvodů: 

  * Moderní JavaScript postupně zavádí mnoho schopností, které poskytovalo jQuery, takže jQuery je méně potřeba, a existují lepší/rychlejší/menší moduly, které poskytují konkrétní implementace

  * Široký přístup jQuery je přímá manipulace s DOM, což je anti-vzor pro moderní JavaScriptové frameworky (např. React, Vue, Svelte)

  * jQuery si překáží samo, pokud se načte dvakrát atd.


### Omezení

Pokud zvolíme CSS framework, který používá jQuery, jsme nuceni importovat jQuery. Například Semantic UI jQuery používá a Tachyons ne.

Pokud zvolíme CSS framework, který je minimální, vzdáváme se komponent frameworku, které můžeme chtít nyní nebo brzy. Například Semantic UI poskytuje karusel obrázků a Tachyons ne.


### Stanoviska

Zvažovali jsme nepoužít žádný framework. To se stále jeví jako schůdné, zejména proto, že CSS grid poskytuje velkou část toho, co pro svůj projekt potřebujeme..

Zvažovali jsme mnoho CSS frameworků rychlým tříděním na krátký seznam: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons atd. Naše dvě volby pro hlubší přezkoumání jsou Semantic UI (protože má nejsémantičtější přístup) a Bulma (protože má nejlehčí přístup, který poskytuje komponenty, které nyní chceme).

Zvažovali jsme Semantic UI. Poskytuje mnoho komponent, včetně těch, které pro svůj projekt chceme: karty, mřížky, tlačítka atd. Provedli jsme pilotní ověření se Semantic UI dvěma způsoby: pomocí typických souborů z CDN a pomocí repozitářů NPM. Dosáhli jsme úspěchu se Semantic UI na statické stránce HTML, ale nedosáhli jsme úspěchu v rámci našeho časového limitu při budování JavaScriptového SPA (hlavně kvůli problémům s načítáním jQuery). Zjistili jsme, že jiní programátoři žádají vývojáře Semantic UI, aby vytvořili verzi bez jQuery, ze stejných důvodů jako my. Jiní programátoři žádají verzi bez jQuery mnoho let, ale vývojáři řekli ne a uvedli, že jakákoli verze bez jQuery by byla příliš těžká na napsání, např. ~„projekt Semantic UI má více než 22 000 styčných bodů, které používají jQuery“.

Příklad se Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Zvažovali jsme Bulma. Bulma má mnoho podobných schopností jako Semantic UI, i když ne tolik sofistikovaných komponent. Bulma je postavena moderními technikami, například bez jQuery. Bulma má některé komponenty třetích stran, z nichž některé můžeme chtít použít.


Příklad s Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argument

Jak výše.

Konkrétně Semantic UI se jeví jako varovný signál jak z hlediska technologie (tedy tolik styčných bodů s jQuery), tak z hlediska vedení (tedy bezjQuerová verze byla tvrdé ne, místo pokusu o plán, průběžné zlepšování, sbírání darů atd.).


### Důsledky

Pokud najdeme dobrý CSS framework bez jQuery, je to obecně užitečné a dobré.


## Související


### Související rozhodnutí

Zvolený CSS framework může ovlivnit testovatelnost.


### Související požadavky

Chceme rychle dodat čistě moderní aplikaci. 

Nechceme trávit čas prací se staršími frameworky (zejména Semantic UI) používajícími starší závislosti (zejména jQuery).


### Související artefakty

Ovlivňuje veškerý typický HTML, který bude toto CSS používat.


### Související principy

Snadno vratné.

Potřeba rychlosti.


## Poznámky

Zde jakékoli poznámky.
