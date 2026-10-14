# Architekturális döntési feljegyzés: API JSON-nal vagy gRPC-vel

## Állapot

Elfogadott

## Háttér

Egy új szolgáltatáshoz tervezünk API-t, amelyet több kliens fog használni. Két lehetőséget fontolgattunk az API megvalósítására: JSON HTTP felett vagy gRPC.

A JSON HTTP felett széles körben használt megközelítés API-k építésére, és számos programozási nyelv és keretrendszer támogatja. Ez a megközelítés egyszerű, könnyű és könnyen érthető, ami sok projekt számára jó választássá teszi. Azonban kevésbé hatékony lehet más lehetőségeknél, különösen nagy adatmennyiségek kezelésekor.

A gRPC ezzel szemben újabb technológia, amely hatékonyabb módot kínál API-k építésére. Bináris szerializációt használ az adatok átviteléhez, ami gyorsabb és tömörebb lehet a JSON-nál. A gRPC támogatja a kétirányú adatfolyamot (streaming) is, ami jó választássá teszi valós idejű alkalmazásokhoz.

## Döntés

Mindkét lehetőség előnyeinek és hátrányainak mérlegelése után úgy döntöttünk, hogy gRPC-t használunk az API-nkhoz. Bár a JSON HTTP felett egyszerűbb lehetőség, úgy véljük, hogy a gRPC hatékonyabb és skálázhatóbb megoldást nyújt a szolgáltatásunkhoz. Azt is előre látjuk, hogy az API-nk nagy mennyiségű adatot fog kezelni, és a gRPC bináris szerializációja hatékonyabb lesz erre a felhasználási esetre.

Ezenkívül úgy véljük, hogy a gRPC kétirányú adatfolyam-támogatása hasznos lesz azokhoz a valós idejű alkalmazásokhoz, amelyeket a jövőben fejleszthetünk.

## Következmények

A gRPC választásával más eszközkészletet és könyvtárakat kell majd használnunk az API építéséhez, mint a JSON HTTP felett esetén. Ez további időt és erőfeszítést igényelhet e technológiák megtanulásához és megvalósításához. Ráadásul az API-nkat használni kívánó klienseknek gRPC-kompatibilis könyvtárakat kell használniuk, amelyeket esetleg nem támogatnak olyan széles körben, mint a JSON HTTP felett könyvtárakat.

Úgy véljük azonban, hogy a gRPC használatának előnyei meghaladják ezeket a lehetséges hátrányokat, és bízunk benne, hogy ez a döntés hatékonyabb és skálázhatóbb API-t eredményez.
