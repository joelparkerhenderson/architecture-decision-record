# Architekturális döntési feljegyzés: Go programozási nyelv

Cím: A Go programozási nyelv bevezetése

Állapot: Elfogadott

## Háttér

Szervezetünk főként a Java programozási nyelvet használta webalkalmazások építéséhez. A Java bőbeszédűsége és egyes keretrendszerek bonyolultsága miatt azonban nehézségekkel szembesülünk. Csapatunk emellett érdeklődést mutatott a modern programozási nyelvek felfedezése iránt a hatékonyabb és robusztusabb fejlesztés érdekében. A kutatás után a Go-t azonosítottuk a Javával kapcsolatos problémáink lehetséges megoldásaként.

## Döntés

Mostantól a Go programozási nyelvet fogjuk használni webalkalmazások építéséhez.

## Indoklás

1. **Egyszerűség és olvashatóság:** A Go az egyszerűségéről és tömör szintaxisáról ismert. Ez könnyűvé teszi a kód olvasását és írását, csökkentve a fejlesztési folyamatunk bonyolultságát.

2. **Magas teljesítmény és skálázhatóság:** A Go gépi kódra fordítódik, amely natívan fut a kiszolgálón. Ez gyorsabb végrehajtási időket és jobb teljesítményt eredményez az értelmezett nyelvekhez, például a Javához képest. Ráadásul a Go párhuzamossági modellje egyszerre több kérést kezel, ami erősen skálázhatóvá teszi.

3. **Erős közösségi támogatás:** A Go-nak élénk fejlesztői közössége van, amely az évek során hozzájárult a növekedéséhez. Ez azt jelenti, hogy rengeteg forrás, könyvtár és keretrendszer áll rendelkezésre, amelyek segítenek elindulni és robusztus alkalmazásokat építeni.

4. **Rugalmasság:** A Go használható mind front-end, mind back-end fejlesztéshez. Ez azt jelenti, hogy mindkét területen kihasználhatjuk az előnyeit fejlesztési projektjeinkhez.

## Következmények

1. **Képzés:** Fejlesztőinknek képzésen kell részt venniük, hogy megtanulják a Go programozási nyelvet és annak árnyalatait.

2. **Tapasztalat:**  Kihívásokkal szembesülhetünk a Javáról Go-ra való átállás során. Eltarthat egy ideig, mire fejlesztőink jártasak lesznek az új nyelvben.

3. **Eszközök:**  Új, a Go-ra specifikus eszközöket és keretrendszereket kell majd bevezetnünk. A meglévő infrastruktúránkat azonban kihasználhatjuk, hogy minimalizáljuk e változás hatását.

4. **Beszállítófüggés:**  A Go nyílt forráskódú programozási nyelv, és nem leszünk kötve egyetlen szállítóhoz vagy szolgáltatóhoz sem.

## Összegzés

A Go programozási nyelv bevezetése segít javítani fejlesztési folyamatunkat és robusztus alkalmazásokat építeni. Erőforrásokat kell majd fektetnünk a képzésbe és az eszközökbe az átállás támogatására, de úgy véljük, hogy e döntés előnyei meghaladják a költségeket.

<h6>Forrás: ezt az oldalt a ChatGPT generálta, majd az érthetőség és a formázás érdekében szerkesztették.</h6>