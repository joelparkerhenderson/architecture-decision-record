# Konfigurácia premenných prostredia

Obsah:

* [Zhrnutie](#zhrnutie)
  * [Problém](#problém)
  * [Rozhodnutie](#rozhodnutie)
  * [Stav](#stav)
* [Podrobnosti](#podrobnosti)
  * [Predpoklady](#predpoklady)
  * [Obmedzenia](#obmedzenia)
  * [Pozície](#pozície)
  * [Argument](#argument)
  * [Dôsledky ](#dôsledky)
* [Súvisiace](#súvisiace)
  * [Súvisiace rozhodnutia](#súvisiace-rozhodnutia)
  * [Súvisiace požiadavky](#súvisiace-požiadavky)
  * [Súvisiace artefakty](#súvisiace-artefakty)
  * [Súvisiace princípy](#súvisiace-princípy)
* [Poznámky](#poznámky)


## Zhrnutie


### Problém

Chceme, aby boli naše aplikácie konfigurovateľné mimo artefaktov/binárnych súborov/zdrojového kódu, tak aby sa jedno zostavenie mohlo správať odlišne v závislosti od prostredia nasadenia.

  * Aby sme to dosiahli, chceme použiť konfiguráciu pomocou premenných prostredia.

  * Chceme spravovať konfiguráciu pomocou súborov, ktoré môžeme verzovať.

  * Chceme poskytnúť určitú ergonómiu vývojárskeho zážitku, napríklad vedieť, čo sa dá konfigurovať a aké sú relevantné predvolené hodnoty.


### Rozhodnutie

Rozhodli sme sa pre súbory .env so súvisiacim súborom predvolených hodnôt a súborom schémy.


### Stav

Rozhodnuté. Sme otvorení zvažovaniu nových schopností, keď sa objavia.


## Podrobnosti


### Predpoklady

Uprednostňujeme oddelenie kódu aplikácie a kódu prostredia. Predpokladáme, že aplikácia musí fungovať odlišne v rôznych prostrediach, ako je vývojové prostredie, testovacie prostredie, demo prostredie, produkčné prostredie atď.

Uprednostňujeme odvetvovú prax „12 factor app“ a ešte viac súvisiacu prax „15 factor app“.

Mnohé z našich predchádzajúcich projektov používali konvenciu súboru `.env` alebo podobného adresára `.env`. Typickou praxou je udržiavať ich mimo verzovania a namiesto toho použiť iný spôsob na ich nasadenie, verzovanie a správu.


### Obmedzenia

Chceme udržať tajomstvá mimo nášho systému verzovania (VCS) správy zdrojového kódu (SCM).

Chceme sa usilovať o kompatibilitu s populárnymi softvérovými frameworkmi a knižnicami. Napríklad Node má modul „dotenv“ na čítanie konfigurácie z premenných prostredia.


### Pozície

Zvažovali sme niekoľko prístupov:

  * Ukladať konfiguráciu v aplikácii, napríklad v súbore `config.js`.

  * Ukladať konfiguráciu v prostredí, napríklad v súbore `.env`.

  * Získavať konfiguráciu zo známeho miesta, napríklad z licenčného servera.


### Argument

Zvolili sme prístup so súborom .env, pretože:

  * Je populárny, vrátane medzi odborníkmi.

  * Sleduje vzor súborov `.env`, ktoré naše tímy úspešne mnohokrát použili v mnohých projektoch.

  * Je jednoduchý. Najmä zatiaľ nám vyhovujú významné kompromisy, ktoré vidíme, ako je nedostatok auditných schopností v porovnaní s prístupom licenčného servera.


### Dôsledky 

Musíme vymyslieť spôsob, ako oddeliť konfiguráciu pomocou premenných prostredia, ktorá je verejná, od akejkoľvek správy tajomstiev.


## Súvisiace


### Súvisiace rozhodnutia

Očakávame, že všetky naše aplikácie budú používať tento prístup.

Budeme plánovať inováciu všetkých našich aplikácií, ktoré používajú menej schopný prístup, ako je tvrdé kódovanie v binárnom súbore alebo v zdrojovom kóde.

Ponecháme tak, ako sú, všetky naše aplikácie, ktoré používajú schopnejší prístup, ako je licenčný server.


### Súvisiace požiadavky

Pridáme devops schopnosti pre súbory vrátane hookov, testov a kontinuálnej integrácie.

Musíme vyškoliť všetkých členov vývojového tímu o tomto rozhodnutí.



### Súvisiace artefakty

Každá oblasť, v ktorej nasadzujeme, bude potrebovať vlastný súbor .env a súvisiace súbory.


### Súvisiace princípy

Ľahko vratné.


## Poznámky


Ukážkový súbor `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Ukážkový súbor `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Ukážkový súbor `.env.schema` iba s kľúčmi:

```env
NAME
EMAIL
```
