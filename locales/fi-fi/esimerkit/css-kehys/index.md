# Arkkitehtuuripäätöstietue: CSS-kehys

Sisällys:

- [Yhteenveto](#yhteenveto)
  - [Ongelma](#ongelma)
  - [Päätös](#päätös)
  - [Tila](#tila)
- [Yksityiskohdat](#yksityiskohdat)
  - [Oletukset](#oletukset)
  - [Rajoitteet](#rajoitteet)
  - [Kannat](#kannat)
  - [Perustelu](#perustelu)
  - [Seuraukset](#seuraukset)
- [Liittyvät](#liittyvät)
  - [Liittyvät päätökset](#liittyvät-päätökset)
  - [Liittyvät vaatimukset](#liittyvät-vaatimukset)
  - [Liittyvät artefaktit](#liittyvät-artefaktit)
  - [Liittyvät periaatteet](#liittyvät-periaatteet)
- [Huomiot](#huomiot)


## Yhteenveto


### Ongelma

Haluamme käyttää CSS-kehystä verkkosovellustemme luomiseen:

  * Haluamme käyttökokemuksen olevan nopea ja luotettava kaikilla suosituilla selaimilla ja näyttökokoilla.

  * Haluamme nopean iteroinnin suunnittelussa, asettelussa, UI/UX:ssä jne.

  * Haluamme responsiivisia sovelluksia, erityisesti pienemmille näytöille kuten mobiililaitteille, suuremmille näytöille kuten 4K-laajakuvanäytöille ja dynaamisille näytöille kuten kierrettäville näytöille.  


### Päätös

Päätettiin Bulmasta.


### Tila

Päätettiin Bulmasta. Olemme avoimia uusille CSS-kehysvalinnoille niiden ilmaantuessa.


## Yksityiskohdat


### Oletukset

Haluamme luoda verkkosovelluksia, jotka ovat nykyaikaisia, nopeita, luotettavia, responsiivisia jne.

Tyypilliset nykyaikaiset verkkosovellukset vähentävät/poistavat jQueryn käyttöä useista syistä: 

  * Nykyaikainen JavaScript tuo vähitellen monia ominaisuuksia, joita jQuery on tarjonnut, joten jQueryä tarvitaan vähemmän, ja on parempia/nopeampia/pienempiä moduuleja, jotka tarjoavat tiettyjä toteutuksia

  * jQueryn laaja lähestymistapa on suora DOM-manipulointi, mikä on antimalli nykyaikaisille JavaScript-kehyksille (esim. React, Vue, Svelte)

  * jQuery häiritsee itseään, jos se ladataan kahdesti jne.


### Rajoitteet

Jos valitsemme CSS-kehyksen, joka käyttää jQueryä, olemme jumissa jQueryn tuomisessa. Esimerkiksi Semantic UI käyttää jQueryä, ja Tachyons ei.

Jos valitsemme minimaalisen CSS-kehyksen, luovumme kehyskomponenteista, joita saatamme haluta nyt tai pian. Esimerkiksi Semantic UI tarjoaa kuvakarusellin, ja Tachyons ei.


### Kannat

Harkitsimme kehyksen käyttämättä jättämistä. Tämä näyttää edelleen toteuttamiskelpoiselta, erityisesti koska CSS grid tarjoaa suuren osan siitä, mitä projektimme tarvitsee..

Harkitsimme monia CSS-kehyksiä nopealla lyhyen listan seulonnalla: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons jne. Kaksi valintaamme syvempään tarkasteluun ovat Semantic UI (koska siinä on semanttisin lähestymistapa) ja Bulma (koska siinä on kevyin lähestymistapa, joka tarjoaa haluamamme komponentit nyt).

Harkitsimme Semantic UI:ta. Se tarjoaa monia komponentteja, mukaan lukien sellaisia, joita haluamme projektiimme: välilehdet, ruudukot, painikkeet jne. Teimme pilotin Semantic UI:lla kahdella tavalla: käyttäen tyypillisiä CDN-tiedostoja ja käyttäen NPM-tietovarastoja. Onnistuimme Semantic UI:n kanssa staattisella HTML-sivulla, mutta emme onnistuneet aikarajamme puitteissa rakentamaan JavaScript-SPA:ta (pääasiassa jQueryn latausongelmien vuoksi). Havaitsimme, että muut koodaajat ovat pyytäneet Semantic UI:n kehittäjiä luomaan jQuery-vapaan version samoista syistä kuin me. Muut koodaajat ovat pyytäneet jQuery-vapaata versiota monien vuosien ajan, mutta kehittäjät ovat sanoneet ei ja todenneet, että mikä tahansa jQuery-vapaa versio olisi liian vaikea kirjoittaa esim. ~"Semantic UI -projektissa on yli 22 000 kosketuspistettä, jotka käyttävät jQueryä".

Esimerkki Semanticilla:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Harkitsimme Bulmaa. Bulmassa on monia samoja ominaisuuksia kuin Semantic UI:ssa, vaikkakaan ei yhtä paljon hienostuneita komponentteja. Bulma on rakennettu nykyaikaisilla tekniikoilla, kuten ilman jQueryä. Bulmalle on joitakin kolmansien osapuolten komponentteja, joista osaa saatamme haluta käyttää.


Esimerkki Bulmalla:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Perustelu

Kuten edellä.

Erityisesti Semantic UI:ssa näyttää olevan varoitusmerkki sekä teknologian (eli niin monet jQuery-kosketuspisteet) että johtajuuden osalta (eli jQuery-vapaa oli jyrkkä ei, sen sijaan että olisi yritetty tiekarttaa, jatkuvaa parantamista, lahjoituskeräystä jne.).


### Seuraukset

Jos löydämme hyvän jQuery-vapaan CSS-kehyksen, tämä on yleisesti hyödyllistä ja hyvää kokonaisuudessaan.


## Liittyvät


### Liittyvät päätökset

Valitsemamme CSS-kehys voi vaikuttaa testattavuuteen.


### Liittyvät vaatimukset

Haluamme toimittaa täysin nykyaikaisen sovelluksen nopeasti. 

Emme halua käyttää aikaa vanhempien kehysten (erityisesti Semantic UI) parissa, jotka käyttävät vanhempia riippuvuuksia (erityisesti jQuery).


### Liittyvät artefaktit

Vaikuttaa kaikkeen tyypilliseen HTML:ään, joka käyttää CSS:ää.


### Liittyvät periaatteet

Helposti peruttavissa.

Tarve nopeuteen.


## Huomiot

Mahdolliset huomiot tähän.
