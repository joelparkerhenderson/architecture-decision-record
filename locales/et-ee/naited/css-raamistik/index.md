# Arhitektuuriotsuse kirje: CSS-raamistik

Sisukord:

- [Kokkuvõte](#kokkuvõte)
  - [Küsimus](#küsimus)
  - [Otsus](#otsus)
  - [Olek](#olek)
- [Üksikasjad](#üksikasjad)
  - [Eeldused](#eeldused)
  - [Piirangud](#piirangud)
  - [Seisukohad](#seisukohad)
  - [Argument](#argument)
  - [Tagajärjed](#tagajärjed)
- [Seotud](#seotud)
  - [Seotud otsused](#seotud-otsused)
  - [Seotud nõuded](#seotud-nõuded)
  - [Seotud artefaktid](#seotud-artefaktid)
  - [Seotud põhimõtted](#seotud-põhimõtted)
- [Märkmed](#märkmed)


## Kokkuvõte


### Küsimus

Tahame kasutada oma veebirakenduste loomiseks CSS-raamistikku:

  * Tahame, et kasutajakogemus oleks kiire ja töökindel kõigis populaarsetes brauserites ja ekraanisuurustes.

  * Tahame kiiret iteratsiooni disaini, paigutuse, UI/UX jne üle.

  * Tahame responsiivseid rakendusi, eriti väiksematele ekraanidele nagu mobiilseadmed, suurematele ekraanidele nagu 4K-laiekraanid ja dünaamilistele ekraanidele nagu pööratavad ekraanid.  


### Otsus

Otsustasime Bulma kasuks.


### Olek

Otsustasime Bulma kasuks. Oleme avatud uutele CSS-raamistiku valikutele, kui need ilmuvad.


## Üksikasjad


### Eeldused

Tahame luua veebirakendusi, mis on kaasaegsed, kiired, töökindlad, responsiivsed jne.

Tüüpilised kaasaegsed veebirakendused vähendavad või kaotavad jQuery kasutamise mitmel põhjusel: 

  * Kaasaegne JavaScript võtab järk-järgult kasutusele paljud jQuery pakutud võimalused, seega on jQuery'd vähem vaja ja on olemas paremaid/kiiremaid/väiksemaid mooduleid, mis pakuvad konkreetseid teostusi

  * jQuery lai lähenemine on otsene DOM-i manipuleerimine, mis on kaasaegsete JavaScripti raamistike (nt React, Vue, Svelte) jaoks antimuster

  * jQuery segab iseennast, kui see laaditakse kaks korda jne.


### Piirangud

Kui valime CSS-raamistiku, mis kasutab jQuery'd, oleme sunnitud jQuery'd importima. Näiteks Semantic UI kasutab jQuery'd ja Tachyons mitte.

Kui valime minimaalse CSS-raamistiku, loobume raamistiku komponentidest, mida võime praegu või peagi tahta. Näiteks Semantic UI pakub pildikarusselli ja Tachyons mitte.


### Seisukohad

Kaalusime ka raamistiku mitte kasutamist. See tundub endiselt teostatav, eriti kuna CSS grid pakub suure osa sellest, mida meie projekt vajab.

Kaalusime paljusid CSS-raamistikke kiire lühinimekirja sõelumisega: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons jne. Meie kaks valikut sügavamaks ülevaatuseks on Semantic UI (sest sellel on kõige semantilisem lähenemine) ja Bulma (sest sellel on kõige kergem lähenemine, mis pakub komponente, mida me praegu tahame).

Kaalusime Semantic UI-d. See pakub palju komponente, sealhulgas neid, mida me oma projekti jaoks tahame: vahekaardid, ruudustikud, nupud jne. Tegime Semantic UI-ga pilootprojekti kahel viisil: tüüpiliste CDN-failide ja NPM-hoidlate abil. Saavutasime Semantic UI-ga edu staatilisel HTML-lehel, kuid mitte oma ajapiiri sees JavaScripti SPA ehitamisel (peamiselt jQuery laadimisprobleemide tõttu). Avastasime, et teised programmeerijad on palunud Semantic UI arendajatel luua jQuery-vaba versiooni samadel põhjustel kui meie. Teised programmeerijad on paljude aastate jooksul jQuery-vaba versiooni küsinud, kuid arendajad on öelnud ei ja märkinud, et iga jQuery-vaba versioon oleks liiga raske kirjutada, nt ~"Semantic UI projektil on rohkem kui 22 000 jQuery'd kasutavat puutepunkti".

Näide Semanticuga:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Kaalusime Bulmat. Bulmal on palju sarnaseid võimalusi nagu Semantic UI-l, kuigi mitte nii palju keerukaid komponente. Bulma on ehitatud kaasaegsete tehnikatega, näiteks ilma jQuery'ta. Bulmal on mõned kolmandate osapoolte komponendid, millest mõnda võime tahta kasutada.


Näide Bulmaga:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argument

Nagu eespool.

Täpsemalt tundub Semantic UI-l olevat hoiatusmärk nii tehnoloogia mõttes (st nii palju jQuery puutepunkte) kui ka juhtimise mõttes (st jQuery-vaba oli kõva ei, selle asemel et proovida teekaarti, pidevat täiustamist, annetuste kogumist jne).


### Tagajärjed

Kui leiame hea mitte-jQuery CSS-raamistiku, on see üldiselt kasulik ja hea.


## Seotud


### Seotud otsused

Meie valitud CSS-raamistik võib mõjutada testitavust.


### Seotud nõuded

Tahame kiiresti tarnida puhtalt kaasaegse rakenduse. 

Me ei taha kulutada aega vanemate raamistike (eriti Semantic UI) vanemate sõltuvustega (eriti jQuery) töötamisele.


### Seotud artefaktid

Mõjutab kogu tüüpilist HTML-i, mis CSS-i kasutab.


### Seotud põhimõtted

Hõlpsasti tagasipööratav.

Vajadus kiiruse järele.


## Märkmed

Mis tahes märkmed siin.
