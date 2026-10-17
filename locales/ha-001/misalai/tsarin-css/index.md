# Rikodin shawarar gine-gine: tsarin CSS

Abubuwan da ke ciki:

- [Taƙaitawa](#taƙaitawa)
  - [Matsala](#matsala)
  - [Shawara](#shawara)
  - [Matsayi](#matsayi)
- [Cikakkun bayanai](#cikakkun-bayanai)
  - [Zato](#zato)
  - [Ƙuntatawa](#ƙuntatawa)
  - [Ra’ayoyi](#raayoyi)
  - [Hujja](#hujja)
  - [Tasiri](#tasiri)
- [Mai alaƙa](#mai-alaƙa)
  - [Shawarwari masu alaƙa](#shawarwari-masu-alaƙa)
  - [Buƙatu masu alaƙa](#buƙatu-masu-alaƙa)
  - [Kayayyakin da aka samar masu alaƙa](#kayayyakin-da-aka-samar-masu-alaƙa)
  - [Ƙa’idoji masu alaƙa](#ƙaidoji-masu-alaƙa)
- [Bayanan kula](#bayanan-kula)


## Taƙaitawa


### Matsala

Muna son amfani da tsarin CSS don ƙirƙirar aikace-aikacen yanar gizonmu:

  * Muna son ƙwarewar mai amfani ta kasance mai sauri da aminci, a dukkan shahararrun burauza da girman allo.

  * Muna son saurin maimaitawa a zane, tsari, UI/UX, da sauransu.

  * Muna son aikace-aikace masu amsawa, musamman ga ƙananan allo kamar na na’urorin hannu, manyan allo kamar na 4K masu faɗi, da allo masu motsi kamar na’urorin nuni masu juyawa.  


### Shawara

An yanke shawara kan Bulma.


### Matsayi

An yanke shawara kan Bulma. A buɗe ga sababbin zaɓuɓɓukan tsarin CSS idan suka zo.


## Cikakkun bayanai


### Zato

Muna son ƙirƙirar aikace-aikacen yanar gizo na zamani, masu sauri, masu aminci, masu amsawa, da sauransu.

Aikace-aikacen yanar gizo na zamani na yau da kullum suna rage/kawar da amfani da jQuery saboda dalilai da yawa: 

  * JavaScript na zamani yana shigo da iyawa da yawa waɗanda jQuery ya bayar, don haka jQuery ba a buƙatarsa sosai, kuma akwai ɓangarori mafi kyau/sauri/ƙanana waɗanda ke ba da takamaiman aiwatarwa

  * Hanyar jQuery mai faɗi ita ce yin sarrafa DOM kai tsaye, wanda ya saɓa wa tsarin tsarukan JavaScript na zamani (misali React, Vue, Svelte)

  * jQuery yana kawo cikas ga kansa idan an ɗora shi sau biyu, da sauransu.


### Ƙuntatawa

Idan muka zaɓi tsarin CSS da ke amfani da jQuery, to mun makale da shigo da jQuery. Misali, Semantic UI yana amfani da jQuery, Tachyons kuma ba ya yi.

Idan muka zaɓi tsarin CSS mai ƙaranci, to mun bar ɓangarorin tsarin da za mu so a yanzu ko nan ba da jimawa ba. Misali, Semantic UI yana ba da carousel na hotuna, Tachyons kuma ba ya yi.


### Ra’ayoyi

Mun yi la’akari da rashin amfani da kowane tsari. Wannan har yanzu yana da yiwuwa, musamman domin CSS grid yana ba da yawancin abin da muke bukata don aikinmu..

Mun yi la’akari da tsarukan CSS da yawa ta amfani da gajeren jerin tantancewa cikin sauri: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons, da sauransu. Zaɓuɓɓukanmu biyu don bita mai zurfi su ne Semantic UI (domin yana da hanya mafi ma’ana) da Bulma (domin yana da hanya mafi sauƙin nauyi wadda ke ba da ɓangarorin da muke so a yanzu).

Mun yi la’akari da Semantic UI. Wannan yana ba da ɓangarori da yawa, ciki har da waɗanda muke so don aikinmu: tabs, grids, buttons, da sauransu. Mun yi gwaji da Semantic UI ta hanyoyi biyu: ta amfani da fayilolin CDN na yau da kullum, da ta amfani da ma’ajiyar NPM. Mun sami nasara da Semantic UI a shafin HTML mai tsayawa, amma ba mu sami nasara ba cikin iyakar lokacinmu na gina SPA na JavaScript (galibi saboda matsalolin ɗora jQuery). Mun gano cewa wasu masu rubuta lamba sun kasance suna roƙon masu haɓaka Semantic UI su ƙirƙiri sigar da ba ta da jQuery, saboda dalilai iri ɗaya da namu. Wasu masu rubuta lamba sun kasance suna neman sigar da ba ta da jQuery tsawon shekaru da yawa, amma masu haɓakawa sun ce a’a, kuma sun bayyana cewa duk wata sigar da ba ta da jQuery za ta yi wahalar rubutawa misali ~“aikin Semantic UI yana da fiye da wuraren taɓawa 22,000 da ke amfani da jQuery”.

Misali da Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Mun yi la’akari da Bulma. Bulma yana da iyawa da yawa iri ɗaya da Semantic UI, ko da yake ba ɓangarori masu ci-gaba sosai kamar yawansu ba. An gina Bulma da dabaru na zamani, kamar rashin jQuery. Bulma yana da wasu ɓangarori na wasu kamfanoni, wasu daga cikinsu za mu so mu yi amfani da su.


Misali da Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Hujja

Kamar yadda ke sama.

Musamman, Semantic UI yana da alamar taka tsantsan duka a fannin fasaha (wato wuraren taɓawa na jQuery da yawa) da kuma a fannin shugabanci (wato rashin jQuery ya sami “a’a” mai tsauri, maimakon ƙoƙarin taswirar hanya, ko ci gaba mai dorewa, ko tara gudummawa, da sauransu).


### Tasiri

Idan muka sami tsarin CSS mai kyau wanda ba na jQuery ba, wannan gabaɗaya yana da amfani da kyau.


## Mai alaƙa


### Shawarwari masu alaƙa

Tsarin CSS da muka zaɓa na iya shafar sauƙin gwaji.


### Buƙatu masu alaƙa

Muna son jigilar aikace-aikace na zamani tsantsa cikin sauri. 

Ba ma son kashe lokaci muna aiki a kan tsofaffin tsarukan (musamman Semantic UI) masu amfani da tsofaffin dogaro (musamman jQuery).


### Kayayyakin da aka samar masu alaƙa

Yana shafar dukkan HTML na yau da kullum da zai yi amfani da CSS.


### Ƙa’idoji masu alaƙa

Mai sauƙin sakewa.

Buƙatar sauri.


## Bayanan kula

Kowane bayanin kula a nan.
