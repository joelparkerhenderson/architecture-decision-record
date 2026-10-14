# Architectuurbeslissingsdocument: CSS-framework

Inhoud:

- [Samenvatting](#samenvatting)
  - [Kwestie](#kwestie)
  - [Beslissing](#beslissing)
  - [Status](#status)
- [Details](#details)
  - [Aannames](#aannames)
  - [Beperkingen](#beperkingen)
  - [Standpunten](#standpunten)
  - [Argument](#argument)
  - [Implicaties](#implicaties)
- [Gerelateerd](#gerelateerd)
  - [Gerelateerde beslissingen](#gerelateerde-beslissingen)
  - [Gerelateerde eisen](#gerelateerde-eisen)
  - [Gerelateerde artefacten](#gerelateerde-artefacten)
  - [Gerelateerde principes](#gerelateerde-principes)
- [Notities](#notities)


## Samenvatting


### Kwestie

We willen een CSS-framework gebruiken om onze webapplicaties te maken:

  * We willen dat de gebruikerservaring snel en betrouwbaar is, in alle populaire browsers en schermformaten.

  * We willen snelle iteratie op ontwerp, lay-out, UI/UX enz.

  * We willen responsieve applicaties, vooral voor kleinere schermen zoals op mobiele apparaten, grotere schermen zoals 4K-breedbeeldschermen en dynamische schermen zoals draaibare displays.  


### Beslissing

Gekozen voor Bulma.


### Status

Gekozen voor Bulma. Open voor nieuwe keuzes van CSS-frameworks zodra ze verschijnen.


## Details


### Aannames

We willen webapps maken die modern, snel, betrouwbaar, responsief enz. zijn.

Typische moderne webapps verminderen of elimineren het gebruik van jQuery om meerdere redenen: 

  * Modern JavaScript voert veel mogelijkheden in die jQuery bood, dus jQuery is minder nodig, en er zijn betere/snellere/kleinere modules die specifieke implementaties bieden

  * De brede aanpak van jQuery is directe DOM-manipulatie, wat een anti-patroon is voor moderne JavaScript-frameworks (bijv. React, Vue, Svelte)

  * jQuery stoort zichzelf als het twee keer wordt geladen enz.


### Beperkingen

Als we een CSS-framework kiezen dat jQuery gebruikt, zijn we gedwongen jQuery te importeren. Semantic UI gebruikt bijvoorbeeld jQuery en Tachyons niet.

Als we een minimaal CSS-framework kiezen, laten we frameworkcomponenten schieten die we nu of binnenkort misschien willen. Semantic UI biedt bijvoorbeeld een afbeeldingencarrousel en Tachyons niet.


### Standpunten

We hebben overwogen geen framework te gebruiken. Dit lijkt nog steeds haalbaar, vooral omdat CSS grid veel biedt van wat we voor ons project nodig hebben.

We hebben veel CSS-frameworks overwogen met een snelle shortlistselectie: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons enz. Onze twee selecties voor een diepere beoordeling zijn Semantic UI (omdat het de meest semantische aanpak heeft) en Bulma (omdat het de lichtgewicht aanpak heeft die de componenten biedt die we nu willen).

We hebben Semantic UI overwogen. Dit biedt veel componenten, waaronder componenten die we voor ons project willen: tabbladen, grids, knoppen enz. We hebben een pilot gedaan met Semantic UI op twee manieren: met typische CDN-bestanden en met NPM-repository's. We hadden succes met Semantic UI in een statische HTML-pagina, maar niet binnen onze timebox om een JavaScript-SPA te bouwen (voornamelijk door problemen bij het laden van jQuery). We ontdekten dat andere programmeurs de ontwikkelaars van Semantic UI vragen een jQuery-vrije versie te maken, om dezelfde redenen als wij. Andere programmeurs vragen al jarenlang om een jQuery-vrije versie, maar de ontwikkelaars hebben nee gezegd en gesteld dat elke jQuery-vrije versie te moeilijk te schrijven zou zijn, bijv. ~"het Semantic UI-project heeft meer dan 22.000 aanknopingspunten die jQuery gebruiken".

Voorbeeld met Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

We hebben Bulma overwogen. Bulma heeft veel vergelijkbare mogelijkheden als Semantic UI, hoewel niet zoveel geavanceerde componenten. Bulma is gebouwd met moderne technieken, zoals geen jQuery. Bulma heeft enkele componenten van derden, waarvan we er een aantal misschien willen gebruiken.


Voorbeeld met Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argument

Zoals hierboven.

Specifiek lijkt Semantic UI een waarschuwingsvlag te hebben, zowel qua technologie (namelijk zoveel jQuery-aanknopingspunten) als qua leiderschap (namelijk jQuery-vrij was een harde nee, in plaats van een roadmap, continue verbetering, donatiewerving enz. te proberen).


### Implicaties

Als we een goed niet-jQuery CSS-framework vinden, is dat over het algemeen nuttig en goed.


## Gerelateerd


### Gerelateerde beslissingen

Het CSS-framework dat we kiezen kan de testbaarheid beïnvloeden.


### Gerelateerde eisen

We willen snel een puur moderne app opleveren. 

We willen geen tijd besteden aan het werken met oudere frameworks (vooral Semantic UI) met oudere afhankelijkheden (vooral jQuery).


### Gerelateerde artefacten

Beïnvloedt alle typische HTML die de CSS zal gebruiken.


### Gerelateerde principes

Gemakkelijk omkeerbaar.

Behoefte aan snelheid.


## Notities

Eventuele notities hier.
