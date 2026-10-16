# Konfiguracija okoljskih spremenljivk

Vsebina:

* [Povzetek](#povzetek)
  * [Vprašanje](#vprašanje)
  * [Odločitev](#odločitev)
  * [Stanje](#stanje)
* [Podrobnosti](#podrobnosti)
  * [Predpostavke](#predpostavke)
  * [Omejitve](#omejitve)
  * [Stališča](#stališča)
  * [Argument](#argument)
  * [Posledice ](#posledice)
* [Povezano](#povezano)
  * [Povezane odločitve](#povezane-odločitve)
  * [Povezane zahteve](#povezane-zahteve)
  * [Povezani artefakti](#povezani-artefakti)
  * [Povezana načela](#povezana-načela)
* [Opombe](#opombe)


## Povzetek


### Vprašanje

Želimo, da so naše aplikacije nastavljive onkraj artefaktov/binarnih datotek/izvorne kode, tako da se lahko ena gradnja obnaša drugače glede na okolje uvajanja.

  * Za dosego tega želimo uporabiti konfiguracijo z okoljskimi spremenljivkami.

  * Konfiguracijo želimo upravljati z datotekami, ki jih lahko vključimo v nadzor različic.

  * Želimo zagotoviti nekaj ergonomije za razvijalce, na primer vedenje, kaj je mogoče nastaviti, in vse ustrezne privzete vrednosti.


### Odločitev

Odločili smo se za datoteke .env s pripadajočo datoteko privzetih vrednosti in datoteko sheme.


### Stanje

Odločeno. Odprti smo za preučitev novih zmožnosti, ko se pojavijo.


## Podrobnosti


### Predpostavke

Dajemo prednost ločevanju kode aplikacije in kode okolja. Predpostavljamo, da mora aplikacija v različnih okoljih delovati drugače, na primer v razvojnem okolju, testnem okolju, predstavitvenem okolju, produkcijskem okolju itd.

Dajemo prednost panožni praksi »12 factor app« in še bolj sorodni praksi »15 factor app«.

Mnogi naši prejšnji projekti so uporabljali konvencijo datoteke `.env` ali podobnega imenika `.env`. Običajna praksa je, da se te datoteke ne hranijo v nadzoru različic, temveč se uvajajo, različicirajo in upravljajo na drug način.


### Omejitve

Skrivnosti želimo ohraniti zunaj našega sistema za upravljanje izvorne kode (SCM) oziroma sistema za nadzor različic (VCS).

Želimo si zagotoviti združljivost s priljubljenimi programskimi ogrodji in knjižnicami. Na primer, Node ima modul »dotenv« za branje konfiguracije okoljskih spremenljivk.


### Stališča

Preučili smo nekaj pristopov:

  * Konfiguracijo shraniti v aplikacijo, na primer v datoteko `config.js`.

  * Konfiguracijo shraniti v okolje, na primer v datoteko `.env`.

  * Konfiguracijo pridobiti z znane lokacije, kot je licenčni strežnik.


### Argument

Izbrali smo pristop z datoteko .env, ker:

  * Je priljubljen, tudi med strokovnjaki.

  * Sledi vzorcu datotek `.env`, ki so jih naše ekipe že mnogokrat uspešno uporabile pri mnogih projektih.

  * Je preprost. Zlasti se za zdaj strinjamo z občutnimi kompromisi, ki jih vidimo, kot je pomanjkanje zmožnosti revizije v primerjavi s pristopom licenčnega strežnika.


### Posledice 

Najti moramo način za ločevanje konfiguracije okoljskih spremenljivk, ki je javna, od upravljanja skrivnosti.


## Povezano


### Povezane odločitve

Pričakujemo, da bodo vse naše aplikacije uporabljale ta pristop.

Načrtujemo nadgradnjo vseh naših aplikacij, ki uporabljajo manj zmožen pristop, kot je trdo kodiranje v binarni datoteki ali izvorni kodi.

Vse naše aplikacije, ki uporabljajo bolj zmožen pristop, kot je licenčni strežnik, bomo pustili nespremenjene.


### Povezane zahteve

Za datoteke bomo dodali zmožnosti DevOps, vključno s kljukami, testi in neprekinjeno integracijo.

Vse razvijalske sodelavce moramo usposobiti glede te odločitve.



### Povezani artefakti

Vsako območje, kjer uvajamo, bo potrebovalo svojo datoteko .env in sorodne datoteke.


### Povezana načela

Lahko povratljivo.


## Opombe


Primer datoteke `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Primer datoteke `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Primer datoteke `.env.schema` samo s ključi:

```env
NAME
EMAIL
```
