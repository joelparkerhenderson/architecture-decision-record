# Architekturális döntési feljegyzés: programozási kódszerkesztők

## Háttér

A programozási kódszerkesztők a fejlesztők elengedhetetlen eszközei a kód írásához és szerkesztéséhez. Számos kódszerkesztő létezik, mindegyiknek megvan a maga funkciókészlete, előnyei és hátrányai. Ennek az ADR-nek a célja a programozási kódszerkesztőkhöz hozott architekturális döntések dokumentálása.

## Prioritások

A programozási kódszerkesztők architektúrájának a következőket kell előnyben részesítenie:

* **Modularitás**: A kódszerkesztőt moduláris módon kell megtervezni, lehetővé téve a fejlesztőknek, hogy szükség szerint testre szabják és bővítsék. Ez rugalmas architektúrát tesz lehetővé, amely alkalmazkodhat a különböző fejlesztők és csapatok igényeihez.

* **Teljesítmény**: A kódszerkesztőnek teljesítőképesnek és reszponzívnak kell lennie, lehetővé téve a fejlesztőknek, hogy hatékonyan dolgozzanak anélkül, hogy az általuk használt eszköz lassítaná őket.

* **Felhasználói felület**: A felhasználói felületnek intuitívnak és könnyen használhatónak kell lennie, lehetővé téve a fejlesztőknek, hogy a kódjukra összpontosítsanak ahelyett, hogy a szerkesztővel küzdenének.

* **Bővíthetőség**: A kódszerkesztőt úgy kell megtervezni, hogy lehetővé tegye az egyszerű bővítést harmadik felek bővítményeivel és integrációival.

* **Kompatibilitás**: A kódszerkesztőnek kompatibilisnek kell lennie programozási nyelvek és technológiák széles körével, hasznos eszközzé téve fejlesztők széles köre számára.

## Döntés

Ezen prioritások alapján a programozási kódszerkesztők architektúráját a következő összetevőkkel kell megtervezni:

* **Mag**: Ez az összetevő a kódszerkesztő alapfunkcióit nyújtja, mint a szintaxiskiemelés, a szövegszerkesztés és a fájlkezelés.

* **UI**: Ez az összetevő a kódszerkesztő felhasználói felületét nyújtja, beleértve a menüket, eszköztárakat és billentyűparancsokat.

* **Bővítmények**: Ez az összetevő lehetővé teszi a fejlesztőknek, hogy harmadik felek bővítményeinek telepítésével bővítsék a kódszerkesztő funkcionalitását. A bővítmények további funkciókat nyújthatnak, mint a kódkiegészítés, a linting vagy a hibakeresés.

* **Integrációk**: Ez az összetevő lehetővé teszi, hogy a kódszerkesztő más eszközökkel és technológiákkal integrálódjon, mint a verziókezelő rendszerek, buildrendszerek vagy hibakereső eszközök.

## Indoklás

A kódszerkesztő modularitása lehetővé teszi a fejlesztőknek, hogy szükség szerint testre szabják és bővítsék. Ez azért fontos, mert a különböző fejlesztőknek és csapatoknak különböző igényeik és munkafolyamataik vannak, és a rugalmas architektúra befogadhatja ezeket a különbségeket.

* **Teljesítmény**: döntő, mert a fejlesztőknek hatékonyan kell tudniuk dolgozni anélkül, hogy az eszközeik lassítanák őket. A teljesítőképes kódszerkesztő elengedhetetlen a termelékenységhez, és segíthet a fejlesztőknek megtartani a figyelmüket és koncentrációjukat.

* **UI**: fontos, mert lehetővé teszi a fejlesztőknek, hogy a kódjukra összpontosítsanak ahelyett, hogy a szerkesztővel küzdenének. Ez jobb termelékenységhez és kevesebb frusztrációhoz vezethet a fejlesztők számára.

* **Bővíthetőség**: erőteljes, mert lehetővé teszi a kódszerkesztő különböző igényekhez és munkafolyamatokhoz való igazítását. A harmadik felek bővítményei és integrációi további funkciókat és képességeket nyújthatnak, amelyek nincsenek benne az alapszerkesztőben.

* **Kompatibilitás**: értékes, mert lehetővé teszi a kódszerkesztő használatát programozási nyelvek és technológiák széles körével. Ez a szerkesztőt hasznosabb eszközzé teszi fejlesztők széles köre számára.

A mag, a bővítmények, az integrációk és az UI összetevői világos felelősségszétválasztást nyújtanak, és lehetővé teszik a moduláris architektúrát, amely könnyen bővíthető és testre szabható. Ez az architektúra rugalmas, teljesítőképes, és kompatibilis programozási nyelvek és technológiák széles körével, ami hasznos eszközzé teszi a fejlesztők számára.