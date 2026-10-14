# Környezeti változók konfigurálása

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
  * [Következmények ](#következmények)
* [Kapcsolódó](#kapcsolódó)
  * [Kapcsolódó döntések](#kapcsolódó-döntések)
  * [Kapcsolódó követelmények](#kapcsolódó-követelmények)
  * [Kapcsolódó artefaktumok](#kapcsolódó-artefaktumok)
  * [Kapcsolódó alapelvek](#kapcsolódó-alapelvek)
* [Megjegyzések](#megjegyzések)


## Összefoglaló


### Probléma

Azt szeretnénk, hogy alkalmazásaink a műtermékeken/bináris fájlokon/forráskódon túl is konfigurálhatók legyenek, így egyetlen build a telepítési környezetétől függően eltérően viselkedhet.

  * Ennek eléréséhez környezeti változós konfigurációt szeretnénk használni.

  * A konfigurációt verziókezelhető fájlokkal szeretnénk kezelni.

  * Szeretnénk némi fejlesztői kényelmet biztosítani, például annak ismeretét, mi konfigurálható, és melyek a releváns alapértelmezések.


### Döntés

A .env fájlok mellett döntöttünk, kapcsolódó alapértelmezett fájllal és sémafájllal.


### Állapot

Eldöntve. Nyitottak vagyunk új lehetőségek megfontolására, ahogy felmerülnek.


## Részletek


### Feltevések

Előnyben részesítjük az alkalmazáskód és a környezeti kód szétválasztását. Feltételezzük, hogy az alkalmazásnak különböző környezetekben eltérően kell működnie, például fejlesztői környezetben, tesztkörnyezetben, bemutató környezetben, éles környezetben stb.

Előnyben részesítjük a „12 factor app” iparági gyakorlatot, és még inkább a kapcsolódó „15 factor app” gyakorlatot.

Korábbi projektjeink közül sok használta a `.env` fájl vagy hasonló `.env` könyvtár konvencióját. Tipikus gyakorlat ezeket a verziókezelésen kívül tartani, és más módot használni a telepítésükre, verziózásukra és kezelésükre.


### Megszorítások

A titkokat ki szeretnénk tartani a forráskódkezelő (SCM) verziókezelő rendszerből (VCS).

Törekedni szeretnénk a népszerű szoftveres keretrendszerekkel és könyvtárakkal való kompatibilitásra. Például a Node-nak van egy „dotenv” modulja a környezeti változós konfiguráció olvasásához.


### Álláspontok

Néhány megközelítést fontolóra vettünk:

  * A konfiguráció tárolása az alkalmazásban, például egy `config.js` fájlban.

  * A konfiguráció tárolása a környezetben, például egy `.env` fájlban.

  * A konfiguráció lekérése egy ismert helyről, például egy licenckiszolgálóról.


### Érv

A .env fájl megközelítését azért választottuk, mert:

  * Népszerű, a szakértők körében is.

  * Követi a `.env` fájlok mintáját, amelyet csapataink sokszor, sok projektben sikeresen használtak.

  * Egyszerű. Különösen egyelőre megbékélünk a jelentős kompromisszumokkal, amelyeket látunk, például az auditálási képességek hiányával a licenckiszolgálós megközelítéshez képest.


### Következmények 

Ki kell találnunk egy módot a nyilvános környezeti változós konfiguráció elválasztására a titkok kezelésétől.


## Kapcsolódó


### Kapcsolódó döntések

Elvárjuk, hogy minden alkalmazásunk ezt a megközelítést használja.

Tervezzük az olyan alkalmazásaink korszerűsítését, amelyek kevésbé képes megközelítést használnak, például a bináris fájlba vagy forráskódba való beégetést.

Változatlanul hagyjuk azokat az alkalmazásainkat, amelyek képesebb megközelítést használnak, például licenckiszolgálót.


### Kapcsolódó követelmények

DevOps-képességeket adunk a fájlokhoz, beleértve a hookokat, teszteket és folyamatos integrációt.

Minden fejlesztő kollégánkat ki kell képeznünk e döntésre.



### Kapcsolódó artefaktumok

Minden telepítési területnek szüksége lesz saját .env fájlra és kapcsolódó fájlokra.


### Kapcsolódó alapelvek

Könnyen visszafordítható.


## Megjegyzések


Példa `.env` fájl:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Példa `.env.defaults` fájl:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Példa `.env.schema` fájl csak a kulcsokkal:

```env
NAME
EMAIL
```
