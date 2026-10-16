# Aplinkos kintamųjų konfigūracija

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
  * [Implikacijos ](#implikacijos)
* [Susiję](#susiję)
  * [Susiję sprendimai](#susiję-sprendimai)
  * [Susiję reikalavimai](#susiję-reikalavimai)
  * [Susiję artefaktai](#susiję-artefaktai)
  * [Susiję principai](#susiję-principai)
* [Pastabos](#pastabos)


## Santrauka


### Problema

Norime, kad mūsų programos būtų konfigūruojamos už artefaktų / dvejetainių failų / šaltinio ribų, kad vienas kūrinys (angl. build) galėtų elgtis skirtingai priklausomai nuo diegimo aplinkos.

  * Tam pasiekti norime naudoti aplinkos kintamųjų konfigūraciją.

  * Norime valdyti konfigūraciją naudodami failus, kuriuos galime versijuoti.

  * Norime suteikti šiek tiek programuotojo patirties patogumo, pavyzdžiui, žinoti, ką galima konfigūruoti, ir kokios yra svarbios numatytosios reikšmės.


### Sprendimas

Pasirinkti .env failai su susijusiu numatytųjų reikšmių failu ir schemos failu.


### Būsena

Nuspręsta. Atviri naujoms galimybėms, kai jos atsiras.


## Detalės


### Prielaidos

Teikiame pirmenybę programos kodo ir aplinkos kodo atskyrimui. Darome prielaidą, kad programa turi veikti skirtingai skirtingose aplinkose, pavyzdžiui, kūrimo aplinkoje, testavimo aplinkoje, demonstracinėje aplinkoje, gamybinėje aplinkoje ir t. t.

Teikiame pirmenybę pramonės praktikai „12 faktorių programa“ (angl. 12 factor app) ir dar labiau susijusiai praktikai „15 faktorių programa“.

Daugelis mūsų ankstesnių projektų naudojo `.env` failo arba panašaus `.env` katalogo konvenciją. Tipinė praktika – juos laikyti už versijų valdymo ribų, o juos diegti, versijuoti ir valdyti kitu būdu.


### Apribojimai

Norime laikyti paslaptis atokiau nuo mūsų šaltinio kodo valdymo (SCM) versijų valdymo sistemos (VCS).

Norime siekti suderinamumo su populiariais programinės įrangos karkasais ir bibliotekomis. Pavyzdžiui, Node turi modulį „dotenv“ aplinkos kintamųjų konfigūracijai skaityti.


### Pozicijos

Svarstėme kelis požiūrius:

  * Laikyti konfigūraciją programoje, pavyzdžiui, faile `config.js`.

  * Laikyti konfigūraciją aplinkoje, pavyzdžiui, faile `.env`.

  * Gauti konfigūraciją iš žinomos vietos, pavyzdžiui, licencijų serverio.


### Argumentas

Pasirinkome failo .env požiūrį, nes:

  * Jis populiarus, įskaitant ekspertų tarpe.

  * Jis atitinka `.env` failų šabloną, kurį mūsų komandos daug kartų sėkmingai naudojo daugelyje projektų.

  * Jis paprastas. Visų pirma, kol kas sutinkame su reikšmingais kompromisais, kuriuos matome, pavyzdžiui, audito galimybių trūkumu, palyginti su licencijų serverio požiūriu.


### Implikacijos 

Turime rasti būdą, kaip atskirti viešą aplinkos kintamųjų konfigūraciją nuo paslapčių valdymo.


## Susiję


### Susiję sprendimai

Tikimės, kad visos mūsų programos naudos šį požiūrį.

Planuosime atnaujinti visas savo programas, kurios naudoja mažiau galimybių turintį požiūrį, pavyzdžiui, įrašymą dvejetainiame faile ar šaltinio kode.

Paliksime nepakeistas visas savo programas, kurios naudoja daugiau galimybių turintį požiūrį, pavyzdžiui, licencijavimo serverį.


### Susiję reikalavimai

Pridėsime failų devops galimybes, įskaitant kabliukus, testus ir nuolatinę integraciją.

Turime apmokyti visus komandos programuotojus apie šį sprendimą.



### Susiję artefaktai

Kiekvienai sričiai, kurioje diegiame, reikės savo .env failo ir susijusių failų.


### Susiję principai

Lengvai atšaukiama.


## Pastabos


Pavyzdinis failas `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Pavyzdinis failas `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Pavyzdinis failas `.env.schema` tik su raktais:

```env
NAME
EMAIL
```
