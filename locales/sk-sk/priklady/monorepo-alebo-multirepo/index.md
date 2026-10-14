# Monorepo alebo multirepo

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

Náš projekt zahŕňa vývoj troch hlavných kategórií softvéru:

  * Front-endové GUI
  * Middlewarové služby
  * Back-endové servery

Pri vývoji je naším systémom správy zdrojového kódu (SCM) a verzovania (VCS) git.

Musíme zvoliť, ako použijeme git na organizáciu nášho kódu.

Základnou voľbou je organizovať ako „monorepo“, „polyrepo“ alebo „hybrid“:

  * Monorepo znamená, že všetky časti dáme do jedného veľkého repozitára
  * Polyrepo znamená, že každú časť dáme do vlastného repozitára
  * Hybrid znamená nejakú zmes monorepa a polyrepa

Viac nájdete na https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Rozhodnutie

Monorepo, keď je organizácia/tím/projekt relatívne malý a rýchla iterácia má vyššiu prioritu než udržiavanie stability.

Polyrepo, keď je organizácia/tím/projekt relatívne veľký a udržiavanie stability má vyššiu prioritu než rýchla iterácia.


### Stav

Rozhodnuté. Sme otvorení opätovnému posúdeniu, ak/keď budú dostupné nové nástroje na správu monorepozitárov a/alebo polyrepozitárov.


## Podrobnosti


### Predpoklady

Všetok kód, ktorý vyvíjame, je určený pre ponuky jednej organizácie a nie pre širokú verejnosť. T. j. Broker-Dealer nemá v úmysle mať nič ako dobrovoľných vývojárov z radov širokej verejnosti.


### Obmedzenia

Obmedzenia sú dobre zdokumentované na https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Pozície

Zvažovali sme monorepá v štýle Googlu, Facebooku atď. Myslíme si, že akékoľvek problémy so škálovaním monorepa sú tak ďaleko v budúcnosti, že kým ich budeme potrebovať, budeme môcť využiť rovnaké postupy ako Google a Facebook.

Zvažovali sme polyrepá v štýle typických open source projektov v Gite, ako Google Android, Facebook React atď. Myslíme si, že sú najlepšou voľbou pre účasť širokej verejnosti (napr. ktokoľvek na svete môže pracovať na kóde) a individuálnu dostupnosť (napr. projekt sa používa samostatne, bez akýchkoľvek ďalších častí).


### Argument

Keď je organizácia/tím/projekt relatívne malý, zvolíme monorepo, pretože rýchla iterácia má výrazne vyššiu prioritu než udržiavanie stability

Keď je organizácia/tím/projekt relatívne veľký, zvolíme polyrepo, pretože udržiavanie stability má výrazne vyššiu prioritu než rýchla iterácia.


### Dôsledky

Ak existuje pipeline pre CI+CD, možno ju bude potrebné upraviť na testovanie viacerých projektov v jednom repozitári.

CI+CD môže trvať dlhšie pri úplnom zostavení monorepa, pretože CI+CD môže zostavovať všetky projekty v monorepe.

Ak organizácia/tím/projekt rastie, monorepo bude mať problémy so škálovaním.

Problémy so škálovaním monorepa môžu robiť prechod na polyrepo čoraz hodnotnejším.

Prechod z monorepa na polyrepo je významná devops úloha a bude ju treba naplánovať, riadiť a naprogramovať.


## Súvisiace


### Súvisiace rozhodnutia

Vytvoríme rozhodnutia pre súvisiace nástroje na správu monorepozitárov (napr. Google Bazel) a polyrepozitárov (napr. Lyft Refactorator).


### Súvisiace požiadavky

Musíme vyvinúť pipeline CI+CD tak, aby dobre fungovala s gitom.


### Súvisiace artefakty

Očakávame, že organizácia repozitárov bude mať súvisiace artefakty pre provisioning, správu konfigurácie, testovanie a podobné devops oblasti. 


### Súvisiace princípy

Ľahko vratné. Ak monorepo v praxi nefunguje alebo ho vedenie nechce, je jednoduché prejsť na polyrepo.

Posadnutosť zákazníkom. Ceníme si doručenie projektu do rúk zákazníkov a veríme, že monorepo nás tam môže dostať rýchlejšie než polyrepo a tiež nám pomôcť rýchlejšie iterovať.

Mysli vo veľkom. Google a Facebook sú veľmi silní zástancovia monorepozitárov pred polyrepozitármi, pretože všetky základné ponuky možno vyvíjať/testovať/nasadzovať súhrnne.


## Poznámky

Sem pridajte poznámky.
