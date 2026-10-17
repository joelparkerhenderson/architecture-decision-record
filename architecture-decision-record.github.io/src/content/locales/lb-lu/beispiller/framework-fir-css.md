# Architektur-Decisiounsopzeechnung: Framework fir CSS

Inhalt:

- [Zesummefaassung](#zesummefaassung)
  - [Problem](#problem)
  - [Decisioun](#decisioun)
  - [Zoustand](#zoustand)
- [Detailer](#detailer)
  - [Viraussetzungen](#viraussetzungen)
  - [Restriktiounen](#restriktiounen)
  - [Positiounen](#positiounen)
  - [Argument](#argument)
  - [Implikatiounen](#implikatiounen)
- [Verwandt](#verwandt)
  - [Verwandt Decisiounen](#verwandt-decisiounen)
  - [Verwandt Ufuerderungen](#verwandt-ufuerderungen)
  - [Verwandt Artefakten](#verwandt-artefakten)
  - [Verwandt Prinzipien](#verwandt-prinzipien)
- [Notizen](#notizen)


## Zesummefaassung


### Problem

Mir wëllen e CSS-Framework benotzen, fir eis Webapplikatiounen ze erstellen:

  * Mir wëllen, datt d'Benotzererfahrung séier an zouverlässeg ass, op alle gängege Browser a Bildschirmgréissten.

  * Mir wëllen séier Iteratioun beim Design, Layout, UI/UX, asw.

  * Mir wëllen responsiv Applikatiounen, besonnesch fir méi kleng Bildschirmer wéi op mobilen Apparater, méi grouss Bildschirmer wéi op 4K-Widescreens, an dynamesch Bildschirmer wéi dréibar Affichagen.  


### Decisioun

Mir hunn eis fir Bulma decidéiert.


### Zoustand

Fir Bulma decidéiert. Oppen fir nei Choixe vu CSS-Frameworks, soubal se opdauchen.


## Detailer


### Viraussetzungen

Mir wëllen Web-Apps erstellen, déi modern, séier, zouverlässeg, responsiv, asw. sinn.

Typesch modern Web-Apps reduzéieren/eliminéiere d'Notzung vu jQuery aus verschiddene Grënn: 

  * Modernt JavaScript féiert vill Fäegkeeten, déi jQuery bruecht huet, no an no an, sou datt jQuery manner néideg ass, an et besser/méi séier/méi kleng Moduler gëtt, déi spezifesch Ëmsetzunge bidden

  * Dem jQuery säin allgemenge Usaz ass et, den DOM direkt ze manipuléieren, wat en Anti-Pattern fir modern JavaScript-Frameworks ass (z.B. React, Vue, Svelte)

  * jQuery stéiert sech selwer, wann et zweemol gelueden gëtt, asw.


### Restriktiounen

Wa mir e CSS-Framework wielen, dat jQuery benotzt, da sinn et mir gezwongen, jQuery z'importéieren. Zum Beispill benotzt Semantic UI jQuery, an Tachyons net.

Wa mir e CSS-Framework wielen, dat minimal ass, da verzichte mir op Framework-Komponenten, déi mir elo oder geschwënn eventuell wëllen. Zum Beispill bitt Semantic UI e Bild-Carousel, an Tachyons net.


### Positiounen

Mir hu iwwerluecht, kee Framework ze benotzen. Dat schéngt nach ëmmer machbar, besonnesch well CSS Grid vill vun deem bitt, wat mir fir eise Projet brauchen..

Mir hu vill CSS-Frameworks mat engem séiere Shortlist-Triage iwwerluecht: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons, asw. Eis zwou Auswiele fir déifer Iwwerpréiwung sinn Semantic UI (well et den semantesche Usaz huet) a Bulma (well et den liichtsten Usaz huet, dee d'Komponente bitt, déi mir elo wëllen).

Mir hu Semantic UI iwwerluecht. Dat bitt vill Komponenten, dorënner déi, déi mir fir eise Projet wëllen: Tabs, Grids, Buttons, asw. Mir hunn en Pilot mat Semantic UI op zwou Weeër gemaach: mat typesche CDN-Dateien, a mat NPM-Repos. Mir hu Succès mat Semantic UI an enger statescher HTML-Säit gehat, awer net bannent eiser Zäitbegrenzung, fir eng JavaScript-SPA ze bauen (haaptsächlech wéinst jQuery-Ladeproblemer). Mir hunn entdeckt, datt aner Programméierer d'Semantic-UI-Entwéckler gefrot hunn, eng jQuery-fräi Versioun ze erstellen, aus deene selwechte Grënn wéi mir. Aner Programméierer froen zënter villen Joer no enger jQuery-fräier Versioun, awer d'Entwéckler hunn Nee gesot an erkläert, datt all jQuery-fräi Versioun ze schwéier ze schreiwe wier, z.B. ~"de Semantic-UI-Projet huet méi wéi 22.000 Touchpoints, déi jQuery benotzen".

Beispill mat Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Mir hu Bulma iwwerluecht. Bulma huet vill ähnlech Fäegkeeten wéi Semantic UI, awer net sou vill raffinéiert Komponenten. Bulma ass mat modernen Techniken gebaut, wéi kee jQuery. Bulma huet e puer Drëtt-Komponenten, vun deenen mir e puer eventuell benotze wëllen.


Beispill mat Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argument

Wéi uewen.

Speziell schéngt Semantic UI eng Warnflag ze hunn, souwuel technologesch (dat heescht, sou vill jQuery-Touchpoints) wéi och bei der Féierung (dat heescht, jQuery-fräi war en haart Nee, amplaz eng Roadmap, oder kontinuéierlech Verbesserung, oder Spendesammlung, asw. ze probéieren).


### Implikatiounen

Wa mir e gutt Net-jQuery-CSS-Framework fannen, ass dat allgemeng hëllefräich a gutt am Ganzen.


## Verwandt


### Verwandt Decisiounen

D'CSS-Framework, dat mir wielen, kann d'Testbarkeet beaflossen.


### Verwandt Ufuerderungen

Mir wëllen eng rein modern App séier ausliwweren. 

Mir wëllen keng Zäit domat verbréngen, un eelere Frameworks (besonnesch Semantic UI) mat eelere Ofhängegkeeten (besonnesch jQuery) ze schaffen.


### Verwandt Artefakten

Betrëfft de ganzen typeschen HTML, dee dat CSS benotze wäert.


### Verwandt Prinzipien

Einfach réckgängeg ze maachen.

Besoin u Vitess.


## Notizen

All Notizen hei.
