# Időbélyeg-formátum

Tartalom:

* [Összefoglaló](#összefoglaló)
  * [Probléma](#probléma)
  * [Döntés](#döntés)
  * [Állapot](#állapot)
* [Részletek](#részletek)
  * [Feltevések](#feltevések)
  * [Megszorítások](#megszorítások)
  * [Álláspontok](#álláspontok)
  * [Érv](#érv)
  * [Következmények](#következmények)
* [Kapcsolódó](#kapcsolódó)
  * [Kapcsolódó döntések](#kapcsolódó-döntések)
  * [Kapcsolódó követelmények](#kapcsolódó-követelmények)
  * [Kapcsolódó artefaktumok](#kapcsolódó-artefaktumok)
  * [Kapcsolódó alapelvek](#kapcsolódó-alapelvek)
* [Megjegyzések](#megjegyzések)


## Összefoglaló


### Probléma

Szeretnénk nyomon követni, mikor történnek a dolgok, időbélyegek és egy következetes időbélyeg-formátum használatával, amely jól működik az összes rendszerünkben és a harmadik felek rendszereiben.

Olyan rendszerekkel lépünk kapcsolatba, amelyeknek különböző időbélyeg-formátumaik vannak:

* A JSON-üzeneteknek nincs natív időbélyeg-formátumuk, ezért el kell döntenünk, hogyan alakítsunk át egy időbélyeget karakterlánccá és egy karakterláncot időbélyeggé, azaz hogyan szerializáljunk/deszerializáljunk.

* Egyes alkalmazások helyi időt használnak UTC helyett. Ez kényelmes lehet azoknak a projekteknek, amelyeknek alkalmazkodniuk kell a helyi időhöz, például a helyi időn alapuló eseményeket kiváltó projekteknek.

* Egyes rendszereknek eltérő időpontossági igényeik és képességeik vannak, például másodperces, ezredmásodperces vagy nanoszekundumos időfelbontást használnak. Például a Linux operációs rendszer `date` parancsa alapértelmezetten másodperces időpontosságot használ, míg a Nasdaq tőzsde alapértelmezetten nanoszekundumos időpontosságot kér.


### Döntés

Az ISO 8601 szabványos időbélyeg-formátumot választjuk nanoszekundumos pontossággal, konkrétan az „YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ” formát.

A formátum megmutatja az évet, hónapot, napot, órát, percet, másodpercet, nanoszekundumokat és a Zulu időzónát, más néven UTC, GMT.


### Állapot

Eldöntve.


## Részletek


### Feltevések

Kezelnünk kell ezeket az időbélyeg-szöveges karakterláncokat, hogy időbélyegből karakterláncot (más néven szerializálás) és karakterláncból időbélyeget (más néven deszerializálás) alakítsunk.

Olyan formátumot szeretnénk, amely általában könnyen használható, könnyen átalakítható és ember számára könnyen olvasható.

Kompatibilitást szeretnénk a külső rendszerek széles körével, amelyeket nem tudunk irányítani, például elemző rendszerekkel, adatbázisrendszerekkel, pénzügyi rendszerekkel.


### Megszorítások

Egyes rendszereknek időpontossági korlátaik vannak. Például a macOS operációs rendszer `date` parancsa ki tudja írni az időt másodperces pontossággal, de nanoszekundumos pontossággal nem.


### Álláspontok

Egy sor lehetőséget megfontoltunk:

* Unix-epocha, azaz egy növekvő szám.

* Tömör szövegformátum „YYYYMMDDTHHMMSSNNNNNNNNN”.

* Helyi időzóna használata az UTC időzónával szemben.


### Érv

Tipikus használatnál az ember általi könnyű olvasást/írást többre értékeljük a nyers sebességnél/méretnél.

Tipikus használatnál olyan formátumot szeretnénk, amely jól működik gépi rendszerekben, és kézzel is jól működik, például mintaadatok írásakor, JSON-kimenet olvasásakor, naplófájlban grepelésnél stb.

Atipikus használatnál, például nagy teljesítményű számításnál, arra számítunk, hogy a választott szöveges formátumot optimalizálni szeretnénk a szöveg gyorsabb formátumba, például egy programozási nyelv beépített dátumobjektum-típusába való átalakításával. Így a szöveges formátum nem számít sokat a HPC-nél.


### Következmények

A különféle szöveges rendszereink és időrendszereink erre a formátumra fognak konvergálni.


## Kapcsolódó


### Kapcsolódó döntések

Szükségünk lehet gyors/könnyű módra az időkülönbségek, más néven időtartamok nyomon követésére is. Ezek könnyűek Unix-epocha időbélyegekkel.


### Kapcsolódó követelmények

Módosítani szeretnénk a döntésünket, pl. ha kapcsolódó követelményünk van egy adott típusú naplóüzenet-bélyegre, például Splunkhoz, Sumóhoz, ELK-hoz stb.


### Kapcsolódó artefaktumok

Nyelvi formázók és értelmezők:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Rosetta Code példák:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

SixArm példák:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Kapcsolódó alapelvek

Könnyen visszafordítható. Elég könnyen válthatunk másik formátumra, például a Unix-epochára.

A korai optimalizálás halasztása. Tipikus használatnál nem sokat törődünk egy marék további karakterrel, például egy olyan formátummal, amely kötőjeleket és kettőspontokat használ.


## Megjegyzések

Ide adjon hozzá megjegyzéseket.
