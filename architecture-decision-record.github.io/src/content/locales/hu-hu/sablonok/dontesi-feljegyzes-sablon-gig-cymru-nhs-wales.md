# {Ide írja a címet}

!!! info

    **Állapot**: { Javasolt | Felülvizsgálat alatt | Elfogadott |  Elutasított | Leváltott | Elavult }
    
    **Frissítve**: {ÉÉÉÉ-HH-NN}

## Összefoglaló

{Ez az ADR „vezetői összefoglalója” vagy „lifttel utazós bemutatkozása”. Néhány
tömör mondatban (jellemzően 2–4) fogalmazza meg világosan azt az alapproblémát,
kérdést vagy lehetőséget, amellyel ez az ADR foglalkozik. Adjon egy rövid utalást a
meghozott döntésre vagy a fókuszterületre. A cél, hogy segítse az olvasókat gyorsan
megérteni, miről szól ez az ADR, és eldönteni, releváns-e számukra, anélkül hogy az
egész dokumentumot el kellene olvasniuk. Gondoljon rá úgy, mint egy műszaki
tanulmány kivonatára vagy a fő témába vezető nagyon rövid bevezetésre.}

## Tényezők

{Ez a szakasz elmagyarázza, **miért** hozzák meg **most** ezt a döntést. Világosan
fogalmazza meg az elsődleges indítékokat, igényeket vagy problémákat, amelyek ezt az
architekturális döntést szükségessé teszik. Gondoljon a mögöttes okokra és nyomásokra.}

* {pl. Új funkciót/képességet fejlesztünk, amelynek szüksége van...}

* {pl. Javítanunk kell a teljesítményt, a hozzáférhetőséget, meg kell szüntetnünk az adósságot...}

* {pl. A felhasználói visszajelzések azt sugallják, hogy...}

* {pl. A jelenlegi megközelítés ezeket a korlátozásokat ró ki...}

## Lehetőségek

{Itt sorolja fel a megfontolt különböző lehetőségeket. Maradjon a tényeknél, és
kerülje a véleményeket, a következő szakasz az elemzéssel foglalkozik. Adjon tömör
leírást, hivatkozásokat a releváns dokumentációra vagy példákra.

Foglaljon bele minden jelentős alternatívát, amelyet megvizsgált, még ha végül nem is
választották őket. A cél, hogy az olvasók világos, elfogulatlan képet kapjanak az
egyes alternatívákról, mielőtt az értékelésbe mélyedne.}

### {1. lehetőség címe}

{Írja le a lehetőséget, adjon összefoglalót, sorolja fel a tényeket, adjon hivatkozásokat stb.}

### {n. lehetőség címe}

...

## Lehetőségek elemzése

{Itt kritikusan értékeli a *Lehetőségek* szakaszban bemutatott minden lehetőséget.
Minden lehetőséghez adjon kiegyensúlyozott képet az előnyeiről, hátrányairól és
egyéb releváns szempontjairól vagy kompromisszumairól. Legyen konkrét, és ahol
lehetséges, kösse vissza a megállapításait a *Tényezőkhöz*.

Vegye figyelembe az olyan szempontokat, mint:

* Költség (fejlesztés, üzemeltetés, licencelés)

* Bonyolultság (megvalósítás, karbantartás, tanulási görbe)

* Kockázatok (műszaki, működési, biztonsági)

* Összhang az architekturális alapelvekkel vagy a meglévő szabványokkal

* Hatás a teljesítményre, skálázhatóságra, használhatóságra, karbantarthatóságra,
    biztonságra stb.

Annyi Előny/Hátrány/Egyéb állítást foglaljon bele, amennyi szükséges.
}

### {1. lehetőség értékelése}

* Előny: {Ennek a lehetőségnek egy konkrét előnye vagy haszna.}

* Hátrány: {Egy konkrét hátrány, kockázat vagy költség, amely ehhez a lehetőséghez kapcsolódik.}

* Egyéb: {Egy releváns pont, amely nem szigorúan előny vagy hátrány.}

### {n. lehetőség értékelése}

...

## Ajánlás

{Itt világosan kimondja a végső döntést, és kifejezetten megnevezi a kiválasztott
lehetőséget. Részletesen magyarázza el, **miért** ezt a lehetőséget választották.
Világosan ki kell fejtenie, hogyan felel meg a választott lehetőség legjobban a
*Tényezőknek*, és hogyan teljesíti a kulcsfontosságú követelményeket vagy oldja meg
a megfogalmazott problémát.}

### Következmények

{Ez a szakasz **nem kötelező**.}

{Most, hogy a döntés megszületett, melyek a várt eredmények és hatások, pozitívak és
negatívak egyaránt? Milyen ismert korlátozásokat, költségeket vagy kockázatokat
fogadnak el e döntés meghozatalával? Hogyan érinti ez a döntés a különböző érdekelt
feleket, más rendszereket, fejlesztési gyakorlatokat, működési eljárásokat vagy
a felhasználói élményt?}

* Előny: {Egy konkrét pozitív eredmény vagy haszon, amely e döntéstől várható.}

* Hátrány: {Egy konkrét elfogadott hátrány, költség vagy kockázat, amely e döntésből
    adódik. }

* Egyéb: {Olyan következmény, amely nem szigorúan előny vagy hátrány.}

### Megerősítés

{Ez a szakasz **nem kötelező**.}

{Vázolja, hogyan ellenőrzik e döntés megvalósítását, és hogyan biztosítják a
folyamatos megfelelést. Ez segít bemutatni, hogy a döntés nem csupán elméleti,
hanem aktívan a gyakorlatba ültetik és nyomon követik.

Hogyan ellenőrzi, hogy a döntést helyesen valósították meg? (pl. kódfelülvizsgálatok,
konkrét tesztek, bemutatók, társak általi felülvizsgálat).

Hogyan tartják fenn a döntés betartását idővel? (pl. automatizált ellenőrzések,
időszakos auditok, a csapat irányelveinek frissítése, képzés).

Vannak-e konkrét metrikák vagy mutatók, amelyek megmutatják, hogy a döntés eléri a
kívánt pozitív eredményeket? (pl. teljesítmény-referenciaértékek, bevezetési arányok,
konkrét hibák csökkenése, felhasználói visszajelzési pontszámok).

Ki felelős ennek felügyeletéért, és mi történik, ha a döntést nem tartják be?}

## További információ

{Ez a szakasz **nem kötelező**.}

{Használja ezt a szakaszt bármilyen kiegészítő információ megadására, amely
támogatja a döntést, hátteret ad vagy irányítja a jövőbeli lépéseket. Itt más
döntésekre és forrásokra mutató hivatkozások is megjelenhetnek.

Röviden megjegyezheti, ki vett részt a döntéshozatali folyamatban, és
ha/hogyan jött létre konszenzus. Javasolhat időkeretet vagy konkrét eseményeket is,
amelyek a jövőben e döntés újraértékelését válthatják ki.}
