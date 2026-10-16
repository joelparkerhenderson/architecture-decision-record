# Format časovnega žiga

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
  * [Posledice](#posledice)
* [Povezano](#povezano)
  * [Povezane odločitve](#povezane-odločitve)
  * [Povezane zahteve](#povezane-zahteve)
  * [Povezani artefakti](#povezani-artefakti)
  * [Povezana načela](#povezana-načela)
* [Opombe](#opombe)


## Povzetek


### Vprašanje

Želimo lahko slediti, kdaj se stvari zgodijo, z uporabo časovnih žigov in z uporabo doslednega formata časovnega žiga, ki dobro deluje v vseh naših sistemih in sistemih tretjih oseb.

Komuniciramo s sistemi, ki imajo različne formate časovnih žigov:

* Sporočila JSON nimajo izvornega formata časovnega žiga, zato se moramo odločiti, kako pretvoriti časovni žig v niz in niz v časovni žig, tj. kako serializirati/deserializirati.

* Nekatere aplikacije so nastavljene na uporabo lokalnega časa namesto časa UTC. To je lahko priročno za projekte, ki se morajo prilagajati lokalnemu času, na primer projekte, ki sprožajo dogodke na podlagi lokalnega časa.

* Nekateri sistemi imajo različne potrebe in zmožnosti glede časovne natančnosti, na primer uporabo časovne ločljivosti sekund, milisekund ali nanosekund. Na primer, ukaz `date` v operacijskem sistemu Linux uporablja privzeto časovno natančnost sekund, medtem ko borza Nasdaq želi privzeto časovno natančnost nanosekund.


### Odločitev

Izbrali smo standardni format časovnega žiga ISO 8601 z natančnostjo nanosekund, natančneje »YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ«.

Format prikazuje leto, mesec, dan, uro, minuto, sekundo, nanosekunde in časovni pas Zulu, imenovan tudi UTC, GMT.


### Stanje

Odločeno.


## Podrobnosti


### Predpostavke

Obravnavati moramo te besedilne nize časovnih žigov, pretvarjati iz časovnega žiga v niz (imenovano tudi serializacija) in iz niza v časovni žig (imenovano tudi deserializacija).

Želimo format, ki je na splošno enostaven za uporabo, enostaven za pretvorbo in enostaven za branje človeku.

Želimo združljivost s širokim naborom zunanjih sistemov, ki jih ne moremo nadzorovati, kot so analitični sistemi, podatkovni sistemi, finančni sistemi.


### Omejitve

Nekateri sistemi imajo omejitve časovne natančnosti. Na primer, ukaz `date` v operacijskem sistemu macOS lahko izpiše časovno natančnost v sekundah, ne pa v nanosekundah.


### Stališča

Preučili smo vrsto možnosti:

* Unixova doba (epoch), tj. eno naraščajoče število.

* Jedrnat besedilni format »YYYYMMDDTHHMMSSNNNNNNNNN«.

* Uporaba lokalnega časovnega pasu v primerjavi s časovnim pasom UTC.


### Argument

Pri tipični uporabi cenimo enostavnost branja/pisanja za ljudi bolj kot surovo hitrost/velikost.

Pri tipični uporabi želimo format, ki dobro deluje v strojnih sistemih, pa tudi ročno, na primer pri pisanju vzorčnih podatkov, branju izpisa JSON, iskanju z grep po dnevniški datoteki itd.

Pri netipični uporabi, kot je visokozmogljivostno računalništvo, pričakujemo, da bomo želeli optimizirati vsak izbran besedilni format s pretvorbo besedila v hitrejši format, kot je vgrajeni tip objekta za datum programskega jezika. Zato besedilni format za HPC ni pomemben.


### Posledice

Naši različni besedilni sistemi in časovni sistemi bodo konvergirali k temu formatu.


## Povezano


### Povezane odločitve

Morda bomo želeli hiter/enostaven način za sledenje tudi časovnim razlikam, imenovanim tudi trajanja. Te so enostavne z časovnimi žigi Unixove dobe.


### Povezane zahteve

Morda bomo želeli prilagoditi svojo odločitev, npr. če imamo sorodno zahtevo za določeno vrsto žiga dnevniškega sporočila, kot je za Splunk, Sumo, ELK itd.


### Povezani artefakti

Oblikovalniki in razčlenjevalniki jezikov:

  * [date-fns: sodobna JavaScriptna knjižnica pripomočkov za datume](https://date-fns.org/)
  * [Crono: knjižnica za datum in čas za Rust](https://github.com/chronotope/chron)
  
Primeri Rosetta Code:

  * [Sistemski čas](https://www.rosettacode.org/wiki/System_time)
  * [Format datuma](https://www.rosettacode.org/wiki/Date_format)
  * [Prikaz dobe (epoch)](https://www.rosettacode.org/wiki/Show_the_epoch)

Primeri SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Povezana načela

Lahko povratljivo. Zelo zlahka lahko preidemo na drug format, na primer Unixovo dobo.

Odložite prezgodnjo optimizacijo. Pri tipični uporabi nam ni mar za peščico dodatnih znakov, kot je format, ki uporablja vezaje in dvopičja.


## Opombe

Tu dodajte opombe.
