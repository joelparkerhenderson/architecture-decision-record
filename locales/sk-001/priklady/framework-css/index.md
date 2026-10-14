# Záznam architektonického rozhodnutia: CSS framework

Obsah:

- [Zhrnutie](#zhrnutie)
  - [Problém](#problém)
  - [Rozhodnutie](#rozhodnutie)
  - [Stav](#stav)
- [Podrobnosti](#podrobnosti)
  - [Predpoklady](#predpoklady)
  - [Obmedzenia](#obmedzenia)
  - [Pozície](#pozície)
  - [Argument](#argument)
  - [Dôsledky](#dôsledky)
- [Súvisiace](#súvisiace)
  - [Súvisiace rozhodnutia](#súvisiace-rozhodnutia)
  - [Súvisiace požiadavky](#súvisiace-požiadavky)
  - [Súvisiace artefakty](#súvisiace-artefakty)
  - [Súvisiace princípy](#súvisiace-princípy)
- [Poznámky](#poznámky)


## Zhrnutie


### Problém

Chceme na tvorbu našich webových aplikácií používať CSS framework:

  * Chceme, aby bol používateľský zážitok rýchly a spoľahlivý vo všetkých populárnych prehliadačoch a veľkostiach obrazovky.

  * Chceme rýchlu iteráciu dizajnu, rozloženia, UI/UX atď.

  * Chceme responzívne aplikácie, najmä pre menšie obrazovky, ako sú mobilné zariadenia, väčšie obrazovky, ako sú 4K širokouhlé, a dynamické obrazovky, ako sú otočné displeje.  


### Rozhodnutie

Rozhodli sme sa pre Bulmu.


### Stav

Rozhodnuté pre Bulmu. Sme otvorení novým voľbám CSS frameworkov, keď sa objavia.


## Podrobnosti


### Predpoklady

Chceme vytvárať webové aplikácie, ktoré sú moderné, rýchle, spoľahlivé, responzívne atď.

Typické moderné webové aplikácie obmedzujú/eliminujú používanie jQuery z viacerých dôvodov: 

  * Moderný JavaScript postupne zavádza mnohé schopnosti, ktoré poskytoval jQuery, takže jQuery je menej potrebný a existujú lepšie/rýchlejšie/menšie moduly, ktoré poskytujú konkrétne implementácie

  * Široký prístup jQuery spočíva v priamej manipulácii s DOM, čo je anti-vzor pre moderné JavaScriptové frameworky (napr. React, Vue, Svelte)

  * jQuery sám sebe prekáža, ak sa načíta dvakrát atď.


### Obmedzenia

Ak zvolíme CSS framework, ktorý používa jQuery, sme nútení importovať jQuery. Napríklad Semantic UI používa jQuery a Tachyons nie.

Ak zvolíme CSS framework, ktorý je minimálny, vzdávame sa komponentov frameworku, ktoré možno chceme teraz alebo čoskoro. Napríklad Semantic UI poskytuje karusel obrázkov a Tachyons nie.


### Pozície

Zvažovali sme použitie žiadneho frameworku. To sa stále zdá byť životaschopné, najmä preto, že CSS grid poskytuje veľkú časť toho, čo pre náš projekt potrebujeme..

Zvažovali sme mnohé CSS frameworky rýchlym triedením do užšieho výberu: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons atď. Naše dva výbery na hlbšie preskúmanie sú Semantic UI (pretože má najsémantickejší prístup) a Bulma (pretože má najľahší prístup, ktorý poskytuje komponenty, ktoré chceme teraz).

Zvažovali sme Semantic UI. Ten poskytuje mnoho komponentov vrátane tých, ktoré pre náš projekt chceme: karty, mriežky, tlačidlá atď. Urobili sme pilot so Semantic UI dvoma spôsobmi: pomocou typických súborov CDN a pomocou repozitárov NPM. Dosiahli sme úspech so Semantic UI v statickej HTML stránke, ale v rámci nášho časového limitu sme nedosiahli úspech pri budovaní JavaScriptového SPA (primárne kvôli problémom s načítaním jQuery). Zistili sme, že iní programátori žiadajú vývojárov Semantic UI o vytvorenie verzie bez jQuery z rovnakých dôvodov ako my. Iní programátori žiadajú verziu bez jQuery už mnoho rokov, no vývojári to odmietli a uviedli, že akákoľvek verzia bez jQuery by bola príliš ťažká na napísanie, napr. ~„projekt Semantic UI má viac ako 22 000 dotykových bodov, ktoré používajú jQuery“.

Príklad so Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Zvažovali sme Bulmu. Bulma má mnohé podobné schopnosti ako Semantic UI, hoci nie toľko sofistikovaných komponentov. Bulma je vybudovaná modernými technikami, napríklad bez jQuery. Bulma má niektoré komponenty tretích strán, z ktorých niektoré by sme mohli chcieť použiť.


Príklad s Bulmou:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argument

Ako vyššie.

Konkrétne, Semantic UI sa zdá mať varovný príznak tak z hľadiska technológie (t. j. toľko dotykových bodov s jQuery), ako aj z hľadiska vedenia (t. j. verzia bez jQuery bola tvrdé nie, namiesto pokusu o plán vývoja, nepretržité zlepšovanie, zbieranie darov atď.).


### Dôsledky

Ak nájdeme dobrý CSS framework bez jQuery, je to vo všeobecnosti užitočné a dobré.


## Súvisiace


### Súvisiace rozhodnutia

CSS framework, ktorý zvolíme, môže ovplyvniť testovateľnosť.


### Súvisiace požiadavky

Chceme rýchlo dodať čisto modernú aplikáciu. 

Nechceme tráviť čas prácou so staršími frameworkmi (najmä Semantic UI), ktoré používajú staršie závislosti (najmä jQuery).


### Súvisiace artefakty

Ovplyvňuje všetok typický HTML, ktorý bude CSS používať.


### Súvisiace princípy

Ľahko vratné.

Potreba rýchlosti.


## Poznámky

Akékoľvek poznámky tu.
