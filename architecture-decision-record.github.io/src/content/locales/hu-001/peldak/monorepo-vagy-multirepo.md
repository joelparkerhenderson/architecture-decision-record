# Monorepo vagy multirepo

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

Projektünk a szoftver három fő kategóriájának fejlesztését foglalja magában:

  * Front-end grafikus felületek
  * Köztes (middleware) szolgáltatások
  * Back-end kiszolgálók

Fejlesztéskor a forráskódkezelő (SCM) verziókezelő rendszerünk (VCS) a git.

El kell döntenünk, hogyan használjuk a gitet a kódunk szervezéséhez.

A legfelső szintű választás a „monorepo”, „polyrepo” vagy „hibrid” szervezés:

  * A monorepo azt jelenti, hogy minden részt egy nagy tárolóba teszünk
  * A polyrepo azt jelenti, hogy minden részt a saját tárolójába teszünk
  * A hibrid a monorepo és a polyrepo valamilyen keverékét jelenti

További információért lásd https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Döntés

Monorepo, ha egy szervezet/csapat/projekt viszonylag kicsi, és a gyors iteráció magasabb prioritású, mint a stabilitás fenntartása.

Polyrepo, ha egy szervezet/csapat/projekt viszonylag nagy, és a stabilitás fenntartása magasabb prioritású, mint a gyors iteráció.


### Állapot

Eldöntve. Nyitottak vagyunk az újragondolásra, ha/amikor új eszközök válnak elérhetővé a monorepók és/vagy polyrepók kezelésére.


## Részletek


### Feltevések

Az általunk fejlesztett összes kód egy szervezet kínálatához készül, nem a nagyközönség számára. Vagyis a brókercég nem törekszik arra, hogy legyenek mondjuk nagyközönségből jövő önkéntes fejlesztői.


### Megszorítások

A megszorítások jól dokumentáltak a https://github.com/joelparkerhenderson/monorepo-vs-polyrepo oldalon


### Álláspontok

Fontolóra vettük a Google, a Facebook stb. stílusú monorepókat. Úgy véljük, hogy az esetleges monorepo-skálázási problémák olyan távol vannak a jövőben, hogy mire szükségünk lesz rájuk, ki tudjuk használni ugyanazokat a gyakorlatokat, mint a Google és a Facebook.

Fontolóra vettük a tipikus Git nyílt forráskódú projektek, például a Google Android, a Facebook React stb. stílusú polyrepóit. Úgy véljük, hogy ezek a legjobb választás a nagyközönség részvételéhez (pl. a világon bárki dolgozhat a kódon) és az egyéni elérhetőséghez (pl. a projektet önmagában használják, más részek nélkül).


### Érv

Amikor egy szervezet/csapat/projekt viszonylag kicsi, a monorepót választjuk, mert a gyors iteráció jelentősen magasabb prioritású, mint a stabilitás fenntartása

Amikor egy szervezet/csapat/projekt viszonylag nagy, a polyrepót választjuk, mert a stabilitás fenntartása jelentősen magasabb prioritású, mint a gyors iteráció.


### Következmények

Ha van meglévő CI+CD-folyamat, lehet, hogy módosítanunk kell több projekt egy tárolón belüli teszteléséhez.

A CI+CD több időt vehet igénybe a monorepo teljes buildjéhez, mert a CI+CD a monorepo összes projektjét építhetné.

Ha a szervezet/csapat/projekt nő, a monorepónak skálázási problémái lesznek.

A monorepo skálázási problémái egyre értékesebbé tehetik a polyrepóra való átállást.

A monorepóról polyrepóra való átállás jelentős devops-feladat, amelyet meg kell tervezni, kezelni és programozni.


## Kapcsolódó


### Kapcsolódó döntések

Döntéseket hozunk a monorepók (pl. Google Bazel) és a polyrepók (pl. Lyft Refactorator) kezelésére szolgáló kapcsolódó eszközökről.


### Kapcsolódó követelmények

A CI+CD-folyamatot úgy kell fejlesztenünk, hogy jól működjön a gittel.


### Kapcsolódó artefaktumok

Várjuk, hogy a tárolószervezésnek lesznek kapcsolódó artefaktumai a kiépítéshez, konfigurációkezeléshez, teszteléshez és hasonló devops-területekhez. 


### Kapcsolódó alapelvek

Könnyen visszafordítható. Ha a monorepo a gyakorlatban nem működik, vagy a vezetés nem kívánja, egyszerű polyrepóra váltani.

Ügyfélmánia. Nagyra értékeljük, hogy a projekt az ügyfelek kezébe kerüljön, és úgy véljük, hogy a monorepo gyorsabban elvezethet oda, mint a polyrepo, és gyorsabb iterációban is segíthet.

Gondolkodj nagyban. A Google és a Facebook nagyon erős támogatói a monorepóknak a polyrepókkal szemben, mert az összes alapkínálat együtt fejleszthető/tesztelhető/telepíthető.


## Megjegyzések

Ide adjon hozzá bármilyen megjegyzést.
