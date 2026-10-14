# Formát časovej pečiatky

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
  * [Dôsledky](#dôsledky)
* [Súvisiace](#súvisiace)
  * [Súvisiace rozhodnutia](#súvisiace-rozhodnutia)
  * [Súvisiace požiadavky](#súvisiace-požiadavky)
  * [Súvisiace artefakty](#súvisiace-artefakty)
  * [Súvisiace princípy](#súvisiace-princípy)
* [Poznámky](#poznámky)


## Zhrnutie


### Problém

Chceme byť schopní sledovať, kedy sa veci dejú, pomocou časových pečiatok a konzistentného formátu časových pečiatok, ktorý dobre funguje naprieč všetkými našimi systémami a systémami tretích strán.

Komunikujeme so systémami, ktoré majú rôzne formáty časových pečiatok:

* Správy JSON nemajú natívny formát časovej pečiatky, takže musíme zvoliť, ako previesť časovú pečiatku na reťazec a reťazec na časovú pečiatku, t. j. ako serializovať/deserializovať.

* Niektoré aplikácie sú nastavené na používanie miestneho času namiesto času UTC. To môže byť pohodlné pre projekty, ktoré sa musia prispôsobiť miestnemu času, ako sú projekty spúšťajúce udalosti na základe miestneho času.

* Niektoré systémy majú rôzne potreby a schopnosti časovej presnosti, ako je použitie časového rozlíšenia sekúnd oproti milisekundám oproti nanosekundám. Napríklad príkaz `date` operačného systému Linux používa predvolenú časovú presnosť sekúnd, zatiaľ čo burza Nasdaq chce predvolenú časovú presnosť nanosekúnd.


### Rozhodnutie

Volíme štandardný formát časovej pečiatky ISO 8601 s presnosťou na nanosekundy, konkrétne „YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ“.

Formát zobrazuje rok, mesiac, deň, hodinu, minútu, sekundu, nanosekundy a časovú zónu Zulu, t. j. UTC, GMT.


### Stav

Rozhodnuté.


## Podrobnosti


### Predpoklady

Musíme spracúvať tieto textové reťazce časových pečiatok, prevádzať z časovej pečiatky na reťazec (t. j. serializovať) a z reťazca na časovú pečiatku (t. j. deserializovať).

Chceme formát, ktorý sa vo všeobecnosti ľahko používa, ľahko prevádza a ľahko číta človekom.

Chceme kompatibilitu so širokou škálou externých systémov, ktoré nemôžeme ovládať, ako sú analytické systémy, databázové systémy, finančné systémy.


### Obmedzenia

Niektoré systémy majú obmedzenia časovej presnosti. Napríklad príkaz `date` operačného systému macOS môže vypísať časovú presnosť v sekundách, ale nie v nanosekundách.


### Pozície

Zvažovali sme celý rad možností:

* Unix epocha, t. j. jedno rastúce číslo.

* Stručný textový formát „YYYYMMDDTHHMMSSNNNNNNNNN“.

* Použitie miestnej časovej zóny oproti časovej zóne UTC.


### Argument

Pre typické použitie si ceníme jednoduché čítanie/písanie ľuďmi viac než čistú rýchlosť/veľkosť.

Pre typické použitie chceme formát, ktorý dobre funguje v strojových systémoch a tiež dobre funguje ručne, napríklad pri písaní ukážkových dát, čítaní výstupu JSON, prehľadávaní log súboru pomocou grep atď.

Pre netypické použitie, ako sú vysokovýkonné výpočty, očakávame, že budeme chcieť optimalizovať akýkoľvek zvolený textový formát prevodom textu na rýchlejší formát, napríklad vstavaný typ objektu dátumu programovacieho jazyka. Textový formát teda pre HPC nemá veľký význam.


### Dôsledky

Naše rôzne textové systémy a časové systémy sa zbližia na tomto formáte.


## Súvisiace


### Súvisiace rozhodnutia

Možno budeme chcieť rýchly/jednoduchý spôsob, ako sledovať aj časové rozdiely, t. j. trvania. Tie sú jednoduché s časovými pečiatkami Unix epochy.


### Súvisiace požiadavky

Možno budeme chcieť upraviť svoje rozhodnutie, napr. ak budeme mať súvisiacu požiadavku na konkrétny druh pečiatky logovacej správy, napríklad pre Splunk, Sumo, ELK atď.


### Súvisiace artefakty

Formátovače a parsery pre jazyky:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Príklady z Rosetta Code:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Príklady od SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Súvisiace princípy

Ľahko vratné. Môžeme pomerne ľahko prejsť na iný formát, ako je Unix epocha.

Odložte predčasnú optimalizáciu. Pri typickom použití nám nezáleží veľmi na hŕstke znakov navyše, ako je formát, ktorý používa pomlčky a dvojbodky.


## Poznámky

Sem pridajte poznámky.
