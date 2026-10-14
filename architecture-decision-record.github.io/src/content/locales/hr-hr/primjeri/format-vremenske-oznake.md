# Format vremenske oznake

Sadržaj:

* [Sažetak](#sažetak)
  * [Problem](#problem)
  * [Odluka](#odluka)
  * [Status](#status)
* [Pojedinosti](#pojedinosti)
  * [Pretpostavke](#pretpostavke)
  * [Ograničenja](#ograničenja)
  * [Pozicije](#pozicije)
  * [Argument](#argument)
  * [Implikacije](#implikacije)
* [Povezano](#povezano)
  * [Povezane odluke](#povezane-odluke)
  * [Povezani zahtjevi](#povezani-zahtjevi)
  * [Povezani artefakti](#povezani-artefakti)
  * [Povezana načela](#povezana-načela)
* [Bilješke](#bilješke)


## Sažetak


### Problem

Želimo moći pratiti kada se stvari događaju pomoću vremenskih oznaka i dosljednog formata vremenske oznake koji dobro radi u svim našim sustavima i sustavima trećih strana.

Komuniciramo sa sustavima koji imaju različite formate vremenskih oznaka:

* JSON poruke nemaju izvorni format vremenske oznake, pa moramo odabrati kako pretvoriti vremensku oznaku u niz i niz u vremensku oznaku, tj. kako serijalizirati/deserijalizirati.

* Neke su aplikacije postavljene da koriste lokalno vrijeme, a ne UTC vrijeme. To može biti prikladno za projekte koji se moraju prilagoditi lokalnom vremenu, poput projekata koji pokreću događaje temeljene na lokalnom vremenu.

* Neki sustavi imaju različite potrebe i mogućnosti vremenske preciznosti, poput korištenja vremenske razlučivosti sekundi naspram milisekundi naspram nanosekundi. Na primjer, naredba `date` operacijskog sustava Linux koristi zadanu vremensku preciznost od sekundi, dok burza Nasdaq želi zadanu vremensku preciznost od nanosekundi.


### Odluka

Biramo standardni format vremenske oznake ISO 8601 s preciznošću do nanosekunde, konkretno „YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ“.

Format prikazuje godinu, mjesec, dan, sat, minutu, sekundu, nanosekunde i vremensku zonu Zulu, tj. UTC, GMT.


### Status

Odlučeno.


## Pojedinosti


### Pretpostavke

Moramo obrađivati te tekstualne nizove vremenskih oznaka, pretvarati iz vremenske oznake u niz (tj. serijalizirati) i pretvarati iz niza u vremensku oznaku (tj. deserijalizirati).

Želimo format koji je općenito jednostavan za uporabu, lak za pretvorbu i lak za čitanje čovjeku.

Želimo kompatibilnost sa širokim rasponom vanjskih sustava koje ne možemo kontrolirati, poput analitičkih sustava, sustava baza podataka, financijskih sustava.


### Ograničenja

Neki sustavi imaju ograničenja vremenske preciznosti. Na primjer, naredba `date` operacijskog sustava macOS može ispisati vremensku preciznost u sekundama, ali ne u nanosekundama.


### Pozicije

Razmatrali smo niz opcija:

* Unix epoha, tj. jedan rastući broj.

* Sažet tekstualni format „YYYYMMDDTHHMMSSNNNNNNNNN“.

* Korištenje lokalne vremenske zone naspram vremenske zone UTC.


### Argument

Za tipičnu uporabu cijenimo lako čitanje/pisanje od strane ljudi više od sirove brzine/veličine.

Za tipičnu uporabu želimo format koji dobro radi u strojnim sustavima, a također dobro radi ručno, primjerice pri pisanju primjera podataka, čitanju JSON izlaza, grepanju log datoteke itd.

Za netipičnu uporabu, poput računalstva visokih performansi, očekujemo da ćemo htjeti optimizirati svaki odabrani tekstualni format pretvaranjem teksta u brži format, poput ugrađene vrste objekta datuma programskog jezika. Dakle, tekstualni format nije mnogo važan za HPC.


### Implikacije

Naši različiti tekstualni sustavi i vremenski sustavi konvergirat će na ovaj format.


## Povezano


### Povezane odluke

Možda ćemo htjeti brz/jednostavan način da pratimo i vremenske razlike, tj. trajanja. One su jednostavne s vremenskim oznakama Unix epohe.


### Povezani zahtjevi

Možda ćemo htjeti prilagoditi svoju odluku, npr. ako imamo povezani zahtjev za određenu vrstu oznake log poruke, primjerice za Splunk, Sumo, ELK itd.


### Povezani artefakti

Formateri i parseri za jezike:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Primjeri s Rosetta Codea:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Primjeri tvrtke SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Povezana načela

Lako reverzibilno. Možemo prilično lako prijeći na drukčiji format, poput Unix epohe.

Odgodite preranu optimizaciju. Za tipičnu uporabu nije nam bitna šačica dodatnih znakova, poput formata koji koristi crtice i dvotočke.


## Bilješke

Ovdje dodajte bilješke.
