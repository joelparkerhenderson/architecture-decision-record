# Arkitekturbeslutspost: CSS-ramverk

Innehåll:

- [Sammanfattning](#sammanfattning)
  - [Problem](#problem)
  - [Beslut](#beslut)
  - [Status](#status)
- [Detaljer](#detaljer)
  - [Antaganden](#antaganden)
  - [Begränsningar](#begränsningar)
  - [Ståndpunkter](#ståndpunkter)
  - [Argument](#argument)
  - [Implikationer](#implikationer)
- [Relaterat](#relaterat)
  - [Relaterade beslut](#relaterade-beslut)
  - [Relaterade krav](#relaterade-krav)
  - [Relaterade artefakter](#relaterade-artefakter)
  - [Relaterade principer](#relaterade-principer)
- [Anteckningar](#anteckningar)


## Sammanfattning


### Problem

Vi vill använda ett CSS-ramverk för att skapa våra webbapplikationer:

  * Vi vill att användarupplevelsen ska vara snabb och pålitlig, i alla populära webbläsare och skärmstorlekar.

  * Vi vill ha snabb iteration av design, layout, UI/UX osv.

  * Vi vill ha responsiva applikationer, särskilt för mindre skärmar som på mobila enheter, större skärmar som 4K-bredbildsskärmar och dynamiska skärmar som roterbara displayer.  


### Beslut

Beslutade oss för Bulma.


### Status

Beslutade oss för Bulma. Öppna för nya val av CSS-ramverk när de dyker upp.


## Detaljer


### Antaganden

Vi vill skapa webbappar som är moderna, snabba, pålitliga, responsiva osv.

Typiska moderna webbappar minskar/eliminerar användningen av jQuery av flera skäl: 

  * Modern JavaScript fasar in många förmågor som jQuery har tillhandahållit, så jQuery behövs mindre, och det finns bättre/snabbare/mindre moduler som ger specifika implementationer

  * jQuerys breda ansats är att göra direkt DOM-manipulation, vilket är ett antimönster för moderna JavaScript-ramverk (t.ex. React, Vue, Svelte)

  * jQuery stör sig själv om det laddas två gånger osv.


### Begränsningar

Om vi väljer ett CSS-ramverk som använder jQuery är vi tvungna att importera jQuery. Till exempel använder Semantic UI jQuery, och Tachyons gör det inte.

Om vi väljer ett CSS-ramverk som är minimalt avstår vi från ramverkskomponenter som vi kanske vill ha nu eller snart. Till exempel tillhandahåller Semantic UI en bildkarusell, och Tachyons gör det inte.


### Ståndpunkter

Vi övervägde att inte använda något ramverk. Det verkar fortfarande genomförbart, särskilt eftersom CSS grid tillhandahåller mycket av det vi behöver för vårt projekt..

Vi övervägde många CSS-ramverk med en snabb gallring av en kortlista: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons osv. Våra två val för en djupare granskning är Semantic UI (eftersom det har den mest semantiska ansatsen) och Bulma (eftersom det har den mest lättviktiga ansatsen som tillhandahåller de komponenter vi vill ha nu).

Vi övervägde Semantic UI. Det tillhandahåller många komponenter, inklusive sådana vi vill ha för vårt projekt: flikar, rutnät, knappar osv. Vi gjorde en pilot med Semantic UI på två sätt: med typiska CDN-filer och med NPM-repon. Vi lyckades med Semantic UI på en statisk HTML-sida, men lyckades inte inom vår tidsram att bygga en JavaScript-SPA (främst på grund av problem med att ladda jQuery). Vi upptäckte att andra kodare har bett Semantic UI:s utvecklare att skapa en jQuery-fri version, av samma skäl som vi. Andra kodare har efterfrågat en jQuery-fri version i många år, men utvecklarna har sagt nej och uppgett att en jQuery-fri version skulle vara för svår att skriva, t.ex. ~”Semantic UI-projektet har mer än 22 000 beröringspunkter som använder jQuery”.

Exempel med Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Vi övervägde Bulma. Bulma har många liknande förmågor som Semantic UI, om än inte lika många sofistikerade komponenter. Bulma är byggt med moderna tekniker, till exempel utan jQuery. Bulma har vissa tredjepartskomponenter, av vilka vi kanske vill använda några.


Exempel med Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argument

Som ovan.

Specifikt verkar Semantic UI ha en varningsflagga både när det gäller teknik (dvs. så många jQuery-beröringspunkter) och ledarskap (dvs. jQuery-fri var ett hårt nej, i stället för att försöka med en färdplan, eller kontinuerlig förbättring, eller insamling av donationer osv.).


### Implikationer

Om vi hittar ett bra CSS-ramverk utan jQuery är det i allmänhet till hjälp och bra överlag.


## Relaterat


### Relaterade beslut

Det CSS-ramverk vi väljer kan påverka testbarheten.


### Relaterade krav

Vi vill snabbt leverera en rent modern app. 

Vi vill inte lägga tid på att arbeta med äldre ramverk (särskilt Semantic UI) som använder äldre beroenden (särskilt jQuery).


### Relaterade artefakter

Påverkar all typisk HTML som kommer att använda CSS:en.


### Relaterade principer

Lätt att ångra.

Behov av snabbhet.


## Anteckningar

Eventuella anteckningar här.
