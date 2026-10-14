# Formatul marcajului de timp

Cuprins:

* [Rezumat](#rezumat)
  * [Problemă](#problemă)
  * [Decizie](#decizie)
  * [Stare](#stare)
* [Detalii](#detalii)
  * [Ipoteze](#ipoteze)
  * [Constrângeri](#constrângeri)
  * [Poziții](#poziții)
  * [Argument](#argument)
  * [Implicații](#implicații)
* [Conexe](#conexe)
  * [Decizii conexe](#decizii-conexe)
  * [Cerințe conexe](#cerințe-conexe)
  * [Artefacte conexe](#artefacte-conexe)
  * [Principii conexe](#principii-conexe)
* [Note](#note)


## Rezumat


### Problemă

Vrem să putem urmări când se întâmplă lucrurile folosind marcaje de timp și un format consecvent al marcajului de timp, care funcționează bine în toate sistemele noastre și în sistemele terțe.

Interacționăm cu sisteme care au formate diferite de marcaj de timp:

* Mesajele JSON nu au un format nativ de marcaj de timp, deci trebuie să alegem cum convertim un marcaj de timp într-un șir și un șir într-un marcaj de timp, adică cum serializăm/deserializăm.

* Unele aplicații sunt setate să folosească ora locală, nu ora UTC. Aceasta poate fi comodă pentru proiectele care trebuie să se ajusteze la ora locală, precum proiectele care declanșează evenimente bazate pe ora locală.

* Unele sisteme au nevoi și capabilități diferite de precizie a timpului, precum o rezoluție de secunde față de milisecunde față de nanosecunde. De exemplu, comanda `date` a sistemului de operare Linux folosește implicit o precizie de secunde, în timp ce bursa Nasdaq vrea implicit o precizie de nanosecunde.


### Decizie

Alegem formatul standard de marcaj de timp ISO 8601 cu precizie de nanosecunde, mai exact „YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ”.

Formatul arată anul, luna, ziua, ora, minutul, secunda, nanosecundele și fusul orar Zulu, alias UTC, GMT.


### Stare

Decis.


## Detalii


### Ipoteze

Trebuie să gestionăm aceste șiruri de text ale marcajelor de timp, pentru a converti un marcaj de timp într-un șir (alias serializare) și un șir într-un marcaj de timp (alias deserializare).

Vrem un format care este în general ușor de folosit, ușor de convertit și ușor de citit de o persoană.

Vrem compatibilitate cu o gamă largă de sisteme externe pe care nu le putem controla, precum sisteme de analiză, sisteme de baze de date, sisteme financiare.


### Constrângeri

Unele sisteme au limitări de precizie a timpului. De exemplu, comanda `date` a sistemului de operare macOS poate afișa timpul cu precizie de secunde, dar nu de nanosecunde.


### Poziții

Am luat în considerare o gamă de opțiuni:

* Epoca Unix, adică un singur număr incremental.

* Format text concis „YYYYMMDDTHHMMSSNNNNNNNNN”.

* Folosirea unui fus orar local față de fusul orar UTC.


### Argument

Pentru utilizarea tipică, prețuim ușurința de citit/scris de către oameni mai mult decât viteza/dimensiunea brută.

Pentru utilizarea tipică, vrem un format care funcționează bine în sistemele automate și, de asemenea, bine manual, de exemplu la scrierea datelor de probă, citirea ieșirii JSON, căutarea cu grep într-un fișier de log etc.

Pentru utilizări atipice, precum calculul de înaltă performanță, ne așteptăm să dorim să optimizăm orice format text ales, convertind textul într-un format mai rapid, precum tipul de obiect dată integrat al unui limbaj de programare. Deci formatul text nu contează prea mult pentru HPC.


### Implicații

Diversele noastre sisteme text și sisteme de timp vor converge spre acest format.


## Conexe


### Decizii conexe

Am putea dori și o modalitate rapidă/ușoară de a urmări diferențele de timp, alias durate. Acestea sunt ușoare cu marcajele de timp din epoca Unix.


### Cerințe conexe

Am putea dori să ne ajustăm decizia, de exemplu dacă avem o cerință conexă pentru un anumit tip de marcaj al mesajelor de logare, precum pentru Splunk, Sumo, ELK etc.


### Artefacte conexe

Formatatoare și parsere pentru limbaje:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Exemple Rosetta Code:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Exemple SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Principii conexe

Ușor reversibil. Putem schimba destul de ușor la un alt format, precum epoca Unix.

Amână optimizarea prematură. Pentru utilizarea tipică nu ne pasă prea mult de o mână de caractere în plus, precum un format care folosește cratime și două puncte.


## Note

Adaugă note aici.
