# Architekturális döntési feljegyzés (ADR) sablon <!-- Replace with ADR title -->

Ez egy sablon az EdgeX Foundry ADR-jeihez.

Forrás: https://docs.edgexfoundry.org/2.3/design/adr/template/


### Beterjesztők

Sorolja fel az ADR beterjesztőit.

Formátum:

- Név (Szervezet)


## Változásnapló

Sorolja fel a dokumentum változásait, beleértve az állapotot, a dátumot és a PR URL-jét.

Az állapot a következők egyike: pending (függőben), approved (jóváhagyott), amended (módosított), deprecated (elavult).

A dátum ISO 8601 (ÉÉÉÉ-HH-NN) karakterlánc.

A PR az a pull request, amely beterjesztette a változást, olyan információkkal, mint a különbségek, a közreműködők és a felülvizsgálók.

Formátum:

- \[Az ADR állapota, pl. approved, amended stb.\]\(a pull request URL-je\) ÉÉÉÉ-HH-NN


## Hivatkozott használati esetek

Sorolja fel az összes releváns használati eset / követelmény dokumentumot.

Az ADR legalább egy releváns, jóváhagyott használati esetet igényel.

Formátum:

- \[Használati eset neve\]\(URL\)

Adjon magyarázatot, ha az ADR nem fedi le egy használati eset összes követelményét.


## Háttér

Írja le:

- miért architekturálisan jelentős a terv — igazolva az ADR-t (szemben egy egyszerű hibajegyzékkel és egy problémát javító PR-rel)

- a magas szintű tervezési megközelítést (a részleteket az alábbi javasolt terv ismerteti)


## Javasolt terv

A terv részletei (lehetőség szerint a megvalósításba való belemenés nélkül).

Vázlat:

- érintett (módosított) szolgáltatások/modulok

- hozzáadandó új szolgáltatások/modulok

- modell- és DTO-hatás (módosítások/kiegészítések/eltávolítások)

- API-hatás (módosítások/kiegészítések/eltávolítások)

- általános konfigurációs hatás (új szakaszok létrehozása, módosítások/kiegészítések/eltávolítások)

- devops-hatás


## Megfontolások

Dokumentálja az ADR vitájában felmerült alternatívákat, aggályokat, járulékos vagy kapcsolódó kérdéseket és kérdéseket. 

Jelezze, ha/hogyan oldották meg vagy enyhítették őket.


## Döntés

Dokumentáljon minden megegyezett fontos megvalósítási részletet, fenntartást, jövőbeli megfontolást, valamint megmaradt vagy elhalasztott tervezési kérdést.

Dokumentálja a követelmények azon részeit, amelyeket a javasolt terv nem elégít ki.


## Egyéb kapcsolódó ADR-ek

Sorolja fel az esetleges releváns ADR-eket — például egy funkció alkomponensére vonatkozó tervezési döntést, egy e terv következtében elavulttá váló tervet stb. 

Formátum:

- \[ADR címe\]\(URL\) - Relevancia


## Hivatkozások

Sorolja fel a további hivatkozásokat.

Formátum:

- \[Cím\]\(URL\)

