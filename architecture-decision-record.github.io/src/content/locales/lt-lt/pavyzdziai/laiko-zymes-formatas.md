# Laiko žymės formatas

Turinys:

* [Santrauka](#santrauka)
  * [Problema](#problema)
  * [Sprendimas](#sprendimas)
  * [Būsena](#būsena)
* [Detalės](#detalės)
  * [Prielaidos](#prielaidos)
  * [Apribojimai](#apribojimai)
  * [Pozicijos](#pozicijos)
  * [Argumentas](#argumentas)
  * [Implikacijos](#implikacijos)
* [Susiję](#susiję)
  * [Susiję sprendimai](#susiję-sprendimai)
  * [Susiję reikalavimai](#susiję-reikalavimai)
  * [Susiję artefaktai](#susiję-artefaktai)
  * [Susiję principai](#susiję-principai)
* [Pastabos](#pastabos)


## Santrauka


### Problema

Norime galėti sekti, kada kas nors įvyksta, naudodami laiko žymes ir nuoseklų laiko žymės formatą, kuris gerai veikia visose mūsų ir trečiųjų šalių sistemose.

Sąveikaujame su sistemomis, turinčiomis skirtingus laiko žymių formatus:

* JSON pranešimai neturi savito laiko žymės formato, todėl turime pasirinkti, kaip laiko žymę konvertuoti į eilutę ir eilutę konvertuoti į laiko žymę, t. y. kaip serializuoti / deserializuoti.

* Kai kurios programos nustatytos naudoti vietinį laiką, o ne UTC laiką. Tai gali būti patogu projektams, kurie turi prisitaikyti prie vietinio laiko, pavyzdžiui, projektams, kurie aktyvuoja įvykius pagal vietinį laiką.

* Kai kurios sistemos turi skirtingus laiko tikslumo poreikius ir galimybes, pavyzdžiui, naudoja sekundžių, milisekundžių ar nanosekundžių laiko skiriamąją gebą. Pavyzdžiui, Linux operacinės sistemos komanda `date` numatytai naudoja sekundžių laiko tikslumą, o Nasdaq vertybinių popierių birža numatytai nori nanosekundžių laiko tikslumo.


### Sprendimas

Pasirenkame laiko žymės standartinį formatą ISO 8601 su nanosekundžių tikslumu, konkrečiai „YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ“.

Formatas rodo metus, mėnesį, dieną, valandą, minutę, sekundę, nanosekundes ir Zulu laiko juostą, dar vadinamą UTC, GMT.


### Būsena

Nuspręsta.


## Detalės


### Prielaidos

Turime tvarkyti šias laiko žymių teksto eilutes, konvertuoti iš laiko žymės į eilutę (dar vadinama serializavimu) ir konvertuoti iš eilutės į laiko žymę (dar vadinama deserializavimu).

Norime formato, kurį apskritai lengva naudoti, lengva konvertuoti ir kurį žmogui lengva skaityti.

Norime suderinamumo su plačiu išorinių sistemų, kurių negalime kontroliuoti, spektru, pavyzdžiui, analitikos sistemomis, duomenų bazių sistemomis, finansinėmis sistemomis.


### Apribojimai

Kai kurios sistemos turi laiko tikslumo apribojimų. Pavyzdžiui, macOS operacinės sistemos komanda `date` gali spausdinti laiką sekundžių tikslumu, bet ne nanosekundžių.


### Pozicijos

Svarstėme įvairias galimybes:

* Unix epocha, t. y. vienas didėjantis skaičius.

* Glaustas teksto formatas „YYYYMMDDTHHMMSSNNNNNNNNN“.

* Vietinės laiko juostos naudojimas, palyginti su UTC laiko juosta.


### Argumentas

Tipiniam naudojimui vertiname lengvą žmonių skaitymą / rašymą labiau nei neapdorotą greitį / dydį.

Tipiniam naudojimui norime formato, kuris gerai veikia mašinų sistemose ir taip pat gerai veikia rankiniu būdu, pavyzdžiui, rašant pavyzdinius duomenis, skaitant JSON išvestį, ieškant žurnalo faile su grep ir pan.

Netipiniam naudojimui, pavyzdžiui, didelio našumo skaičiavimams, tikimės, kad norėsime optimizuoti bet kurį pasirinktą teksto formatą konvertuodami tekstą į greitesnį formatą, pavyzdžiui, programavimo kalbos integruotą datos objekto tipą. Todėl teksto formatas didelio našumo skaičiavimams nėra labai svarbus.


### Implikacijos

Mūsų įvairios teksto sistemos ir laiko sistemos konverguos į šį formatą.


## Susiję


### Susiję sprendimai

Galbūt norėsime greito / paprasto būdo taip pat sekti laiko skirtumus, dar vadinamus trukmėmis. Jie paprasti su Unix epochos laiko žymėmis.


### Susiję reikalavimai

Galbūt norėsime pakeisti savo sprendimą, pvz., jei turėsime susijusį reikalavimą tam tikram žurnalo pranešimo žymos tipui, pavyzdžiui, Splunk, Sumo, ELK ir pan.


### Susiję artefaktai

Kalbų formatuokliai ir analizatoriai:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Rosetta Code pavyzdžiai:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

SixArm pavyzdžiai:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Susiję principai

Lengvai atšaukiama. Gana lengvai galime pereiti prie kito formato, pavyzdžiui, Unix epochos.

Atidėkite ankstyvą optimizavimą. Tipiniam naudojimui mums nelabai rūpi saujelė papildomų simbolių, pavyzdžiui, formato, naudojančio brūkšnelius ir dvitaškius.


## Pastabos

Čia pridėkite pastabas.
