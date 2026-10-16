# Architektūros sprendimo įrašas: CSS karkasas

Turinys:

- [Santrauka](#santrauka)
  - [Problema](#problema)
  - [Sprendimas](#sprendimas)
  - [Būsena](#būsena)
- [Detalės](#detalės)
  - [Prielaidos](#prielaidos)
  - [Apribojimai](#apribojimai)
  - [Pozicijos](#pozicijos)
  - [Argumentas](#argumentas)
  - [Implikacijos](#implikacijos)
- [Susiję](#susiję)
  - [Susiję sprendimai](#susiję-sprendimai)
  - [Susiję reikalavimai](#susiję-reikalavimai)
  - [Susiję artefaktai](#susiję-artefaktai)
  - [Susiję principai](#susiję-principai)
- [Pastabos](#pastabos)


## Santrauka


### Problema

Norime naudoti CSS karkasą savo interneto programoms kurti:

  * Norime, kad naudotojo patirtis būtų greita ir patikima visose populiariose naršyklėse ir ekrano dydžiuose.

  * Norime greitai iteruoti dizainą, išdėstymą, UI/UX ir pan.

  * Norime prisitaikančių programų, ypač mažesniems ekranams, pavyzdžiui, mobiliuosiuose įrenginiuose, didesniems ekranams, pavyzdžiui, 4K plačiaekraniams, ir dinaminiams ekranams, pavyzdžiui, pasukamiems ekranams.  


### Sprendimas

Pasirinkta Bulma.


### Būsena

Pasirinkta Bulma. Atviri naujiems CSS karkasų pasirinkimams, kai jie atsiras.


## Detalės


### Prielaidos

Norime kurti šiuolaikines, greitas, patikimas, prisitaikančias ir pan. interneto programas.

Tipinės šiuolaikinės interneto programos mažina arba atsisako jQuery naudojimo dėl kelių priežasčių: 

  * Šiuolaikinis JavaScript palaipsniui perima daugelį jQuery teikiamų galimybių, todėl jQuery reikia mažiau, o konkrečioms realizacijoms yra geresnių / greitesnių / mažesnių modulių

  * jQuery bendras požiūris yra tiesioginis DOM manipuliavimas, o tai yra antišablonas šiuolaikiniams JavaScript karkasams (pvz., React, Vue, Svelte)

  * jQuery trukdo pats sau, jei įkeliamas du kartus ir pan.


### Apribojimai

Jei pasirinksime CSS karkasą, naudojantį jQuery, būsime priversti importuoti jQuery. Pavyzdžiui, Semantic UI naudoja jQuery, o Tachyons – ne.

Jei pasirinksime minimalų CSS karkasą, atsisakysime karkaso komponentų, kurių galime norėti dabar ar netrukus. Pavyzdžiui, Semantic UI turi paveikslėlių karuselę, o Tachyons – ne.


### Pozicijos

Svarstėme galimybę nenaudoti jokio karkaso. Tai vis dar atrodo įgyvendinama, ypač todėl, kad CSS tinklelis (angl. grid) suteikia didžiąją dalį to, ko reikia mūsų projektui..

Svarstėme daug CSS karkasų naudodami greitą trumpojo sąrašo atranką: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons ir kt. Du mūsų pasirinkimai išsamesnei peržiūrai yra Semantic UI (nes jis turi semantiškiausią požiūrį) ir Bulma (nes jis turi lengviausią požiūrį, suteikiantį komponentus, kurių norime dabar).

Svarstėme Semantic UI. Jis turi daug komponentų, įskaitant tuos, kurių norime savo projektui: korteles (angl. tabs), tinklelius, mygtukus ir kt. Atlikome Semantic UI bandomąjį projektą dviem būdais: naudojant įprastus CDN failus ir naudojant NPM saugyklas. Pasiekėme sėkmės su Semantic UI statiniame HTML puslapyje, bet per skirtą laiką nepavyko sukurti JavaScript SPA (daugiausia dėl jQuery įkėlimo problemų). Išsiaiškinome, kad kiti programuotojai prašo Semantic UI kūrėjų sukurti versiją be jQuery dėl tų pačių priežasčių kaip ir mes. Kiti programuotojai versijos be jQuery prašo jau daugelį metų, tačiau kūrėjai atsakė ne ir pareiškė, kad bet kuri versija be jQuery būtų per sunki, pvz., ~„Semantic UI projekte yra daugiau nei 22 000 sąlyčio taškų, naudojančių jQuery“.

Pavyzdys su Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Svarstėme Bulma. Bulma turi daug panašių galimybių kaip Semantic UI, nors ir ne tiek daug sudėtingų komponentų. Bulma sukurta naudojant šiuolaikinius metodus, pavyzdžiui, be jQuery. Bulma turi keletą trečiųjų šalių komponentų, kai kuriuos iš jų galime norėti naudoti.


Pavyzdys su Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argumentas

Kaip aukščiau.

Konkrečiai, Semantic UI atrodo turi įspėjamąjį ženklą tiek technologijos požiūriu (t. y. tiek daug jQuery sąlyčio taškų), tiek lyderystės požiūriu (t. y. versija be jQuery buvo kategoriškas ne, užuot bandžius sudaryti veiksmų planą, nuolat tobulinti ar rinkti paramos lėšas ir pan.).


### Implikacijos

Jei rasime gerą CSS karkasą be jQuery, tai apskritai naudinga ir gerai.


## Susiję


### Susiję sprendimai

Mūsų pasirinktas CSS karkasas gali paveikti testuojamumą.


### Susiję reikalavimai

Norime greitai pristatyti grynai šiuolaikišką programą. 

Nenorime leisti laiko dirbdami su senesniais karkasais (ypač Semantic UI), naudojančiais senesnes priklausomybes (ypač jQuery).


### Susiję artefaktai

Veikia visą tipinį HTML, kuris naudos šį CSS.


### Susiję principai

Lengvai atšaukiama.

Greičio poreikis.


## Pastabos

Čia bet kokios pastabos.
