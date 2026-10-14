# Arkitektúrákvörðunarskrá: CSS-rammi

Efnisyfirlit:

- [Samantekt](#samantekt)
  - [Vandamál](#vandamál)
  - [Ákvörðun](#ákvörðun)
  - [Staða](#staða)
- [Nánar](#nánar)
  - [Forsendur](#forsendur)
  - [Takmarkanir](#takmarkanir)
  - [Afstöður](#afstöður)
  - [Röksemd](#röksemd)
  - [Afleiðingar](#afleiðingar)
- [Tengt](#tengt)
  - [Tengdar ákvarðanir](#tengdar-ákvarðanir)
  - [Tengdar kröfur](#tengdar-kröfur)
  - [Tengdar afurðir](#tengdar-afurðir)
  - [Tengdar meginreglur](#tengdar-meginreglur)
- [Athugasemdir](#athugasemdir)


## Samantekt


### Vandamál

Við viljum nota CSS-ramma til að búa til vefforrit okkar:

  * Við viljum að notendaupplifun sé hröð og áreiðanleg, í öllum vinsælum vöfrum og skjástærðum.

  * Við viljum hraða þróun í áföngum á hönnun, útliti, UI/UX o.s.frv.

  * Við viljum svörunarfús forrit, einkum fyrir minni skjái eins og í farsímum, stærri skjái eins og 4K-breiðskjái og kvika skjái eins og snúanlega skjái.  


### Ákvörðun

Ákveðið var að nota Bulma.


### Staða

Ákveðið var að nota Bulma. Opið fyrir nýjum valkostum CSS-ramma þegar þeir koma fram.


## Nánar


### Forsendur

Við viljum búa til vefforrit sem eru nútímaleg, hröð, áreiðanleg, svörunarfús o.s.frv.

Dæmigerð nútíma vefforrit eru að draga úr/útrýma notkun jQuery af mörgum ástæðum: 

  * Nútíma JavaScript er smám saman að taka upp marga eiginleika sem jQuery hefur veitt, svo jQuery er síður þörf, og til eru betri/hraðari/minni einingar sem veita sérstakar útfærslur

  * Almenn nálgun jQuery er að eiga beint við DOM, sem er andmynstur fyrir nútíma JavaScript-ramma (t.d. React, Vue, Svelte)

  * jQuery truflar sjálft sig ef það er hlaðið tvisvar o.s.frv.


### Takmarkanir

Ef við veljum CSS-ramma sem notar jQuery sitjum við föst í að flytja inn jQuery. Til dæmis notar Semantic UI jQuery en Tachyons ekki.

Ef við veljum CSS-ramma sem er lágmarks förum við á mis við rammaíhluti sem við gætum viljað nú eða fljótlega. Til dæmis býður Semantic UI upp á myndaröð (carousel) en Tachyons ekki.


### Afstöður

Við skoðuðum að nota engan ramma. Það virðist enn raunhæft, einkum vegna þess að CSS grid veitir mikið af því sem við þurfum fyrir verkefnið okkar..

Við skoðuðum marga CSS-ramma með hraðri flokkun á stuttlista: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons o.fl. Tveir valkostir okkar til dýpri rýni eru Semantic UI (því hann hefur merkingarfræðilegustu nálgunina) og Bulma (því hann hefur léttustu nálgunina sem veitir íhlutina sem við viljum nú).

Við skoðuðum Semantic UI. Hann veitir marga íhluti, þar á meðal þá sem við viljum fyrir verkefnið okkar: flipa, ristar, hnappa o.s.frv. Við gerðum tilraunaverkefni með Semantic UI á tvo vegu: með venjulegum CDN-skrám og með NPM-söfnum. Við náðum árangri með Semantic UI á kyrrstæðri HTML-síðu, en náðum ekki árangri innan tímaramma okkar við að smíða JavaScript SPA (aðallega vegna vandamála við hleðslu jQuery). Við komumst að því að aðrir forritarar hafa beðið þróunaraðila Semantic UI um að búa til útgáfu án jQuery, af sömu ástæðum og við. Aðrir forritarar hafa beðið um útgáfu án jQuery í mörg ár, en þróunaraðilarnir hafa sagt nei og sagt að hvaða útgáfa án jQuery sem er yrði of erfið í ritun, t.d. ~„Semantic UI verkefnið hefur yfir 22.000 snertipunkta sem nota jQuery“.

Dæmi með Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Við skoðuðum Bulma. Bulma hefur marga áþekka eiginleika og Semantic UI, þó ekki jafn marga flókna íhluti. Bulma er smíðað með nútímatækni, svo sem án jQuery. Bulma hefur nokkra íhluti frá þriðju aðilum, sem sumir gætu hentað okkur.


Dæmi með Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Röksemd

Eins og að ofan.

Sérstaklega virðist Semantic UI hafa varúðarflagg bæði hvað varðar tækni (þ.e. svo marga snertipunkta jQuery) og forystu (þ.e. útgáfa án jQuery var harðneitun, frekar en tilraun til vegvísis, stöðugra umbóta eða fjáröflunar með framlögum o.s.frv.).


### Afleiðingar

Ef við finnum góðan CSS-ramma án jQuery er það almennt gagnlegt og gott í heildina.


## Tengt


### Tengdar ákvarðanir

CSS-ramminn sem við veljum getur haft áhrif á prófanleika.


### Tengdar kröfur

Við viljum afhenda eingöngu nútímalegt forrit hratt. 

Við viljum ekki eyða tíma í að vinna með eldri ramma (einkum Semantic UI) sem nota eldri ávirkni (einkum jQuery).


### Tengdar afurðir

Hefur áhrif á allt dæmigert HTML sem mun nota CSS-ið.


### Tengdar meginreglur

Auðafturkræft.

Þörf fyrir hraða.


## Athugasemdir

Allar athugasemdir hér.
