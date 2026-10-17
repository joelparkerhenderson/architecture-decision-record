# Rekord ta' deċiżjoni arkitettonika: qafas CSS

Werrej:

- [Sommarju](#sommarju)
  - [Kwistjoni](#kwistjoni)
  - [Deċiżjoni](#deċiżjoni)
  - [Stat](#stat)
- [Dettalji](#dettalji)
  - [Suppożizzjonijiet](#suppożizzjonijiet)
  - [Restrizzjonijiet](#restrizzjonijiet)
  - [Pożizzjonijiet](#pożizzjonijiet)
  - [Argument](#argument)
  - [Implikazzjonijiet](#implikazzjonijiet)
- [Relatati](#relatati)
  - [Deċiżjonijiet relatati](#deċiżjonijiet-relatati)
  - [Rekwiżiti relatati](#rekwiżiti-relatati)
  - [Artefatti relatati](#artefatti-relatati)
  - [Prinċipji relatati](#prinċipji-relatati)
- [Noti](#noti)


## Sommarju


### Kwistjoni

Irridu nużaw qafas CSS biex noħolqu l-applikazzjonijiet tal-web tagħna:

  * Irridu li l-esperjenza tal-utent tkun mgħaġġla u affidabbli, fuq il-browsers popolari kollha u d-daqsijiet kollha tal-iskrin.

  * Irridu iterazzjoni mgħaġġla fuq id-disinn, il-layout, l-UI/UX, eċċ.

  * Irridu applikazzjonijiet responsivi, speċjalment għal skrins iżgħar bħal fuq apparati mobile, skrins akbar bħal fuq widescreens 4K, u skrins dinamiċi bħal displays li jduru.  


### Deċiżjoni

Iddeċidejna fuq Bulma.


### Stat

Iddeċidejna fuq Bulma. Miftuħin għal għażliet ġodda ta' qafas CSS hekk kif jaslu.


## Dettalji


### Suppożizzjonijiet

Irridu noħolqu web apps li huma moderni, mgħaġġla, affidabbli, responsivi, eċċ.

Web apps moderni tipiċi qed inaqqsu/jeliminaw l-użu ta' jQuery għal diversi raġunijiet: 

  * JavaScript modern qed iżid gradwalment ħafna kapaċitajiet li jQuery kien jipprovdi, għalhekk jQuery huwa inqas meħtieġ, u hemm moduli aħjar/aktar mgħaġġla/iżgħar li jipprovdu implimentazzjonijiet speċifiċi

  * L-approċċ wiesa' ta' jQuery huwa li jimmanipula direttament id-DOM, li huwa anti-pattern għal frameworks moderni ta' JavaScript (eż. React, Vue, Svelte)

  * jQuery jinterferixxi miegħu nnifsu jekk jiġi mgħobbi darbtejn, eċċ.


### Restrizzjonijiet

Jekk nagħżlu qafas CSS li juża jQuery, allura nkunu mġiegħla nimportaw jQuery. Pereżempju, Semantic UI juża jQuery, u Tachyons le.

Jekk nagħżlu qafas CSS li huwa minimu, allura nirrinunzjaw għal komponenti tal-qafas li nistgħu rridu issa jew dalwaqt. Pereżempju, Semantic UI jipprovdi carousel tal-immaġini, u Tachyons le.


### Pożizzjonijiet

Ikkunsidrajna li ma nużawx qafas. Dan xorta jidher vijabbli, speċjalment għax is-CSS grid jipprovdi ħafna minn dak li neħtieġu għall-proġett tagħna..

Ikkunsidrajna ħafna framework CSS billi użajna triage mgħaġġel b'lista qasira: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons, eċċ. It-tnejn li għażilna għal reviżjoni aktar fil-fond huma Semantic UI (għax għandu l-aktar approċċ semantiku) u Bulma (għax għandu l-aktar approċċ ħafif li jipprovdi l-komponenti li rridu issa).

Ikkunsidrajna Semantic UI. Dan jipprovdi ħafna komponenti, inklużi dawk li rridu għall-proġett tagħna: tabs, grids, buttons, eċċ. Għamilna pilota b'Semantic UI b'żewġ modi: bl-użu ta' fajls CDN tipiċi, u bl-użu ta' repos NPM. Kellna suċċess b'Semantic UI f'paġna HTML statika, iżda ma kellniex suċċess fil-limitu taż-żmien tagħna biex nibnu SPA ta' JavaScript (primarjament minħabba kwistjonijiet ta' tagħbija ta' jQuery). Skoprejna li programmaturi oħra kienu qed jitolbu lill-iżviluppaturi ta' Semantic UI joħolqu verżjoni mingħajr jQuery, għall-istess raġunijiet li għandna aħna. Programmaturi oħra kienu qed jitolbu verżjoni mingħajr jQuery għal ħafna snin, iżda l-iżviluppaturi qalu le, u ddikjaraw li kwalunkwe verżjoni mingħajr jQuery tkun diffiċli wisq biex tinkiteb eż. ~"il-proġett Semantic UI għandu aktar minn 22,000 punt ta' kuntatt li jużaw jQuery".

Eżempju b'Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Ikkunsidrajna Bulma. Bulma għandha ħafna kapaċitajiet simili għal Semantic UI, għalkemm mhux daqstant komponenti sofistikati. Bulma hija mibnija b'tekniki moderni, bħal li ma tużax jQuery. Bulma għandha xi komponenti ta' partijiet terzi, li wħud minnhom nistgħu rridu nużaw.


Eżempju b'Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argument

Kif hawn fuq.

B'mod speċifiku, Semantic UI jidher li għandu bandiera ta' twissija kemm f'termini ta' teknoloġija (jiġifieri tant punti ta' kuntatt ma' jQuery) kif ukoll f'termini ta' tmexxija (jiġifieri li verżjoni mingħajr jQuery kienet le sod, minflok ma ppruvaw ippjanaw roadmap, jew titjib kontinwu, jew ġbir ta' donazzjonijiet, eċċ.).


### Implikazzjonijiet

Jekk insibu qafas CSS tajjeb mingħajr jQuery, dan ġeneralment huwa ta' għajnuna u tajjeb b'mod ġenerali.


## Relatati


### Deċiżjonijiet relatati

Il-qafas CSS li nagħżlu jista' jaffettwa l-ittestjabbiltà.


### Rekwiżiti relatati

Irridu nwasslu app purament moderna malajr. 

Ma rridux nonfqu ħin naħdmu fuq frameworks eqdem (speċjalment Semantic UI) li jużaw dipendenzi eqdem (speċjalment jQuery).


### Artefatti relatati

Taffettwa l-HTML tipiku kollu li se juża s-CSS.


### Prinċipji relatati

Faċilment riversibbli.

Il-ħtieġa tal-veloċità.


## Noti

Kwalunkwe noti hawn.
