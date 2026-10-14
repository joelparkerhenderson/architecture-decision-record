# Architekturális döntési feljegyzés: Rust programozási nyelv

Döntés száma: AR-001

Döntés címe: A Rust programozási nyelv bevezetése

Dátum: 2021. december 1.

Állapot: Elfogadott

### Problémafelvetés

Ahogy folytatjuk a szoftveralkalmazások fejlesztését, azt észleltük, hogy egyre nehezebb enyhíteni a lehetséges biztonsági réseket és megelőzni a futásidejű hibákat. A meglévő programozási nyelvekkel, mint a C és a C++, továbbra is olyan problémákkal szembesülünk, mint a puffertúlcsordulások, memóriaszivárgások és az alkalmazások összeomlásához vezető meghatározatlan viselkedés. Olyan programozási nyelvre van szükségünk, amely memóriabiztonsági garanciákat nyújt, és elég hatékony a teljesítménykritikus alkalmazások támogatásához.

### Megfontolások

Több programozási nyelvet terveztek a meglévő problémák kezelésére. Ezek közül a Rust programozási nyelv jelentős figyelmet kapott a fejlesztői közösségtől egyedi tervezési jellemzői miatt. A megfontolások közé tartozik:

1. Memóriabiztonság és biztonság

2. Teljesítmény és hatékonyság

3. Közösségi támogatás és elterjedtség

4. Tanulási görbe

5. Eszközök és ökoszisztéma

6. Kompatibilitás a meglévő szoftverrendszerekkel.

### Megszorítások

Új programozási nyelv bevezetése a fejlesztők átképzését igényli, ami időt és erőforrásokat vesz igénybe. A nyelv beillesztése a meglévő fejlesztési munkafolyamatba kihívást jelenthet. Biztosítanunk kell a kompatibilitást a meglévő rendszerekkel, és el kell kerülnünk a törő változtatásokat a folytonosság fenntartása érdekében.

### Megvalósítás

1. Fejlesztőcsapatunk képzésen vesz részt, hogy megtanulja és megismerje a Rust programozási nyelvet.

2. Próbaképpen új projektet hozunk létre Rusttal, hogy értékeljük a kompatibilitását és alkalmasságát fejlesztési céljainkra.

3. Fokozatosan áttelepítjük a C-ben és C++-ban írt meglévő rendszereket Rustra.

4. Együttműködünk a Rust-közösséggel, hogy felfedezzük a rendelkezésre álló eszközöket és könyvtárakat, amelyek javíthatják fejlesztési munkafolyamatunkat.

5. Rendszeresen figyeljük a Rust teljesítményét, és összehasonlítjuk a meglévő programozási nyelvek teljesítményével.

6. Hosszú távú megközelítést alkalmazunk, amely egyensúlyba hozza a képzés, az integráció költségeit és a Rust használatának lehetséges előnyeit.

### Indoklás

A Rustot egyedi funkciói miatt vezettük be, amelyeket arra terveztek, hogy memóriabiztonsági és védelmi garanciákat nyújtsanak, miközben fenntartják a teljesítményt és a hatékonyságot. A Rust robusztus típusrendszere, borrow checkere és memóriabiztonsági koncepciói rendkívül alkalmassá teszik teljesítmény- és biztonságkritikus alkalmazások fejlesztésére. Ráadásul a Rustnak jelentős fejlesztői közössége van, ami hozzáférést biztosít számunkra eszközök, könyvtárak és ökoszisztéma széles köréhez, amelyek támogatják a fejlesztési munkafolyamatunkat. Bár a Rustnak tanulási görbéje van, úgy véljük, hogy a bevezetés előnyei meghaladják a költségeket, és kiváló lehetőséget nyújtanak a folyamatos növekedéshez és innovációhoz.

### Következmények

1. A Rust bevezetése jelentős idő- és erőforrás-befektetést igényel a fejlesztők képzéséhez és a nyelv beillesztéséhez a meglévő fejlesztési munkafolyamatba.

2. A Rust bevezetése bizonyos fokú kompatibilitási problémákat okozhat a meglévő rendszerekkel, ami átalakítást és módosításokat igényel.

3. A Rust bevezetése növelheti a projektünkhöz hozzájárulni képes fejlesztők számát azáltal, hogy vonzza azokat a Rust-fejlesztőket, akik izgalmas projekteken akarnak dolgozni.

4. A bevezetés a meglévő nyelvekhez képest jobb teljesítményhez, hatékonysághoz és biztonsághoz vezethet.

5. Végül a Rust bevezetése azzal a lehetséges előnnyel jár, hogy csökkenti az alkalmazásaink biztonsági réseit.
   
<h6>Forrás: ezt az oldalt a ChatGPT generálta, majd az érthetőség és a formázás érdekében szerkesztették.</h6>