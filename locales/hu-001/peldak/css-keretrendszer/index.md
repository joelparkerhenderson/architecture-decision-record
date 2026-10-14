# Architekturális döntési feljegyzés: CSS keretrendszer

Tartalom:

- [Összefoglaló](#összefoglaló)
  - [Probléma](#probléma)
  - [Döntés](#döntés)
  - [Állapot](#állapot)
- [Részletek](#részletek)
  - [Feltevések](#feltevések)
  - [Megszorítások](#megszorítások)
  - [Álláspontok](#álláspontok)
  - [Érv](#érv)
  - [Következmények](#következmények)
- [Kapcsolódó](#kapcsolódó)
  - [Kapcsolódó döntések](#kapcsolódó-döntések)
  - [Kapcsolódó követelmények](#kapcsolódó-követelmények)
  - [Kapcsolódó artefaktumok](#kapcsolódó-artefaktumok)
  - [Kapcsolódó alapelvek](#kapcsolódó-alapelvek)
- [Megjegyzések](#megjegyzések)


## Összefoglaló


### Probléma

CSS keretrendszert szeretnénk használni a webalkalmazásaink létrehozásához:

  * Azt szeretnénk, hogy a felhasználói élmény gyors és megbízható legyen az összes népszerű böngészőn és képernyőméreten.

  * Gyors iterációt szeretnénk a dizájnban, elrendezésben, UI/UX-ben stb.

  * Reszponzív alkalmazásokat szeretnénk, különösen kisebb képernyőkre, például mobileszközökön, nagyobb képernyőkre, például 4K szélesvásznakon, és dinamikus képernyőkre, például forgatható kijelzőkre.  


### Döntés

A Bulma mellett döntöttünk.


### Állapot

A Bulma mellett döntöttünk. Nyitottak vagyunk az új CSS keretrendszer-választásokra, ahogy megjelennek.


## Részletek


### Feltevések

Modern, gyors, megbízható, reszponzív stb. webalkalmazásokat szeretnénk létrehozni.

A tipikus modern webalkalmazások csökkentik/megszüntetik a jQuery használatát több okból: 

  * A modern JavaScript fokozatosan bevezeti a jQuery által nyújtott számos képességet, ezért a jQuery kevésbé szükséges, és vannak jobb/gyorsabb/kisebb modulok, amelyek konkrét megvalósításokat nyújtanak

  * A jQuery széles megközelítése a közvetlen DOM-manipuláció, ami ellenminta a modern JavaScript keretrendszerek (pl. React, Vue, Svelte) számára

  * A jQuery zavarja önmagát, ha kétszer töltik be stb.


### Megszorítások

Ha olyan CSS keretrendszert választunk, amely jQuery-t használ, akkor kénytelenek vagyunk importálni a jQuery-t. Például a Semantic UI jQuery-t használ, a Tachyons nem.

Ha minimális CSS keretrendszert választunk, lemondunk olyan keretrendszer-komponensekről, amelyekre most vagy hamarosan szükségünk lehet. Például a Semantic UI képkaruzelt nyújt, a Tachyons nem.


### Álláspontok

Fontolóra vettük, hogy nem használunk keretrendszert. Ez továbbra is járhatónak tűnik, különösen mert a CSS grid sok mindent megad, amire a projektünkhöz szükségünk van..

Sok CSS keretrendszert fontolóra vettünk gyors, rövid listás válogatással: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons stb. A mélyebb áttekintésre kiválasztott két jelölt a Semantic UI (mert ez a legszemantikusabb megközelítés) és a Bulma (mert ez a legkönnyebb megközelítés, amely megadja a most kívánt komponenseket).

Fontolóra vettük a Semantic UI-t. Ez sok komponenst nyújt, köztük olyanokat, amelyeket a projektünkhöz szeretnénk: füleket, rácsokat, gombokat stb. Kétféleképpen végeztünk kísérletet a Semantic UI-jal: hagyományos CDN-fájlokkal és NPM-tárolók használatával. Sikerrel jártunk a Semantic UI-jal egy statikus HTML-oldalon, de nem értünk el sikert az időkeretünkön belül egy JavaScript SPA építésében (elsősorban a jQuery betöltési problémái miatt). Felfedeztük, hogy más programozók kérik a Semantic UI fejlesztőit, hogy készítsenek jQuery-mentes verziót, ugyanazokból az okokból, mint mi. Más programozók sok éve kérnek jQuery-mentes verziót, a fejlesztők azonban nemet mondtak, és kijelentették, hogy bármilyen jQuery-mentes verziót túl nehéz lenne megírni, pl. ~„a Semantic UI projektnek több mint 22 000 érintkezési pontja van, amely jQuery-t használ”.

Példa a Semantic-kal:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Fontolóra vettük a Bulmát. A Bulma sok hasonló képességgel rendelkezik, mint a Semantic UI, bár nem olyan sok kifinomult komponenssel. A Bulma modern technikákkal készült, például jQuery nélkül. A Bulmának vannak harmadik féltől származó komponensei, amelyek közül néhányat esetleg használni szeretnénk.


Példa a Bulmával:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Érv

Mint fent.

Konkrétan a Semantic UI-nál figyelmeztető jelzés látszik mind technológiai szempontból (azaz annyi jQuery-érintkezési pont), mind vezetési szempontból (azaz a jQuery-mentesség kemény nemet kapott, ahelyett hogy útitervet, folyamatos fejlesztést, adománygyűjtést stb. kíséreltek volna meg).


### Következmények

Ha találunk egy jó jQuery-mentes CSS keretrendszert, az általában hasznos és jó.


## Kapcsolódó


### Kapcsolódó döntések

A választott CSS keretrendszer befolyásolhatja a tesztelhetőséget.


### Kapcsolódó követelmények

Gyorsan szeretnénk kiadni egy tisztán modern alkalmazást. 

Nem akarunk időt tölteni régebbi keretrendszerekkel (főleg a Semantic UI-jal) való munkával, amelyek régebbi függőségeket (főleg a jQuery-t) használnak.


### Kapcsolódó artefaktumok

Érinti az összes tipikus HTML-t, amely ezt a CSS-t használja.


### Kapcsolódó alapelvek

Könnyen visszafordítható.

A sebesség szükségessége.


## Megjegyzések

Bármilyen megjegyzés ide.
