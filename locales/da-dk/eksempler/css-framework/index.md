# Arkitekturbeslutningspost: CSS-framework

Indhold:

- [Resumé](#resumé)
  - [Problemstilling](#problemstilling)
  - [Beslutning](#beslutning)
  - [Status](#status)
- [Detaljer](#detaljer)
  - [Antagelser](#antagelser)
  - [Begrænsninger](#begrænsninger)
  - [Standpunkter](#standpunkter)
  - [Argument](#argument)
  - [Implikationer](#implikationer)
- [Relateret](#relateret)
  - [Relaterede beslutninger](#relaterede-beslutninger)
  - [Relaterede krav](#relaterede-krav)
  - [Relaterede artefakter](#relaterede-artefakter)
  - [Relaterede principper](#relaterede-principper)
- [Noter](#noter)


## Resumé


### Problemstilling

Vi vil bruge et CSS-framework til at skabe vores webapplikationer:

  * Vi ønsker, at brugeroplevelsen er hurtig og pålidelig i alle populære browsere og skærmstørrelser.

  * Vi ønsker hurtig iteration af design, layout, UI/UX osv.

  * Vi ønsker responsive applikationer, især til mindre skærme som mobilenheder, større skærme som 4K-widescreens og dynamiske skærme som drejelige displays.  


### Beslutning

Besluttet: Bulma.


### Status

Besluttet: Bulma. Åben for nye valg af CSS-frameworks, efterhånden som de dukker op.


## Detaljer


### Antagelser

Vi vil skabe webapps, der er moderne, hurtige, pålidelige, responsive osv.

Typiske moderne webapps reducerer eller eliminerer brugen af jQuery af flere grunde: 

  * Moderne JavaScript indfører efterhånden mange af de funktioner, jQuery har leveret, så jQuery er mindre nødvendigt, og der findes bedre/hurtigere/mindre moduler, der giver specifikke implementeringer

  * jQuerys brede tilgang er direkte DOM-manipulation, hvilket er et antimønster for moderne JavaScript-frameworks (f.eks. React, Vue, Svelte)

  * jQuery forstyrrer sig selv, hvis det indlæses to gange osv.


### Begrænsninger

Hvis vi vælger et CSS-framework, der bruger jQuery, er vi nødt til at importere jQuery. For eksempel bruger Semantic UI jQuery, og Tachyons gør ikke.

Hvis vi vælger et minimalt CSS-framework, går vi glip af frameworkkomponenter, som vi måske vil have nu eller snart. For eksempel tilbyder Semantic UI en billedkarrusel, og Tachyons gør ikke.


### Standpunkter

Vi overvejede at bruge intet framework. Det virker stadig muligt, især fordi CSS grid leverer meget af det, vi har brug for til vores projekt.

Vi overvejede mange CSS-frameworks ved hjælp af en hurtig kortlistesortering: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons osv. Vores to valg til dybere gennemgang er Semantic UI (fordi det har den mest semantiske tilgang) og Bulma (fordi det har den letteste tilgang, der leverer de komponenter, vi vil have nu).

Vi overvejede Semantic UI. Det leverer mange komponenter, herunder nogle vi vil have til vores projekt: faner, grids, knapper osv. Vi lavede et pilotforsøg med Semantic UI på to måder: ved hjælp af typiske CDN-filer og ved hjælp af NPM-repositories. Vi opnåede succes med Semantic UI på en statisk HTML-side, men ikke inden for vores tidsramme til at bygge en JavaScript-SPA (primært på grund af problemer med indlæsning af jQuery). Vi opdagede, at andre programmører har bedt Semantic UI-udviklerne om at lave en jQuery-fri version af samme grunde som os. Andre programmører har i mange år bedt om en jQuery-fri version, men udviklerne har sagt nej og udtalt, at enhver jQuery-fri version ville være for svær at skrive, f.eks. ~"Semantic UI-projektet har mere end 22.000 berøringspunkter, der bruger jQuery".

Eksempel med Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Vi overvejede Bulma. Bulma har mange lignende funktioner som Semantic UI, selv om ikke lige så mange avancerede komponenter. Bulma er bygget med moderne teknikker, såsom ingen jQuery. Bulma har nogle tredjepartskomponenter, hvoraf nogle vi måske vil bruge.


Eksempel med Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argument

Som ovenfor.

Specifikt ser Semantic UI ud til at have et advarselsflag både med hensyn til teknologi (dvs. så mange jQuery-berøringspunkter) og med hensyn til lederskab (dvs. jQuery-fri var et hårdt nej, frem for at forsøge en køreplan, løbende forbedring, indsamling af donationer osv.).


### Implikationer

Hvis vi finder et godt non-jQuery CSS-framework, er det generelt nyttigt og godt.


## Relateret


### Relaterede beslutninger

Det CSS-framework, vi vælger, kan påvirke testbarheden.


### Relaterede krav

Vi vil hurtigt levere en rent moderne app. 

Vi vil ikke bruge tid på at arbejde med ældre frameworks (især Semantic UI) med ældre afhængigheder (især jQuery).


### Relaterede artefakter

Påvirker al den typiske HTML, der vil bruge CSS'en.


### Relaterede principper

Let at gøre om.

Behov for hastighed.


## Noter

Eventuelle noter her.
