# Konfiguracija varijabli okruženja

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
  * [Implikacije ](#implikacije)
* [Povezano](#povezano)
  * [Povezane odluke](#povezane-odluke)
  * [Povezani zahtjevi](#povezani-zahtjevi)
  * [Povezani artefakti](#povezani-artefakti)
  * [Povezana načela](#povezana-načela)
* [Bilješke](#bilješke)


## Sažetak


### Problem

Želimo da naše aplikacije budu konfigurabilne izvan artefakata/binarnih datoteka/izvornog koda, tako da se jedna izgradnja može ponašati drukčije ovisno o okruženju implementacije.

  * Da bismo to postigli, želimo koristiti konfiguraciju varijablama okruženja.

  * Želimo upravljati konfiguracijom pomoću datoteka koje možemo staviti pod kontrolu verzija.

  * Želimo pružiti određenu ergonomiju razvojnog iskustva, poput znanja što se može konfigurirati i koje su relevantne zadane vrijednosti.


### Odluka

Odlučili smo se za .env datoteke s povezanom datotekom zadanih vrijednosti i datotekom sheme.


### Status

Odlučeno. Otvoreni smo za razmatranje novih mogućnosti kad se pojave.


## Pojedinosti


### Pretpostavke

Preferiramo odvajanje koda aplikacije i koda okruženja. Pretpostavljamo da aplikacija treba raditi drukčije u različitim okruženjima, poput razvojnog okruženja, testnog okruženja, demo okruženja, produkcijskog okruženja itd.

Preferiramo industrijsku praksu „12 factor app“, a još više povezanu praksu „15 factor app“.

Mnogi naši prethodni projekti koristili su konvenciju datoteke `.env` ili sličnog direktorija `.env`. Tipična je praksa držati ih izvan kontrole verzija i umjesto toga koristiti neki drugi način za njihovu implementaciju, verzioniranje i upravljanje.


### Ograničenja

Želimo držati tajne izvan našeg sustava kontrole verzija (VCS) za upravljanje izvornim kodom (SCM).

Želimo ciljati na kompatibilnost s popularnim softverskim okvirima i bibliotekama. Na primjer, Node ima modul „dotenv“ za čitanje konfiguracije varijablama okruženja.


### Pozicije

Razmatrali smo nekoliko pristupa:

  * Pohrana konfiguracije u aplikaciji, primjerice u datoteci `config.js`.

  * Pohrana konfiguracije u okruženju, primjerice u datoteci `.env`.

  * Dohvat konfiguracije s poznate lokacije, primjerice s licencnog poslužitelja.


### Argument

Odabrali smo pristup datoteke .env jer:

  * Popularan je, uključujući među stručnjacima.

  * Slijedi obrazac `.env` datoteka koje su naši timovi uspješno koristili mnogo puta na mnogim projektima.

  * Jednostavan je. Osobito, za sada smo zadovoljni značajnim kompromisima koje vidimo, poput nedostatka mogućnosti revizije u usporedbi s pristupom licencnog poslužitelja.


### Implikacije 

Moramo smisliti način za odvajanje konfiguracije varijablama okruženja koja je javna od svakog upravljanja tajnama.


## Povezano


### Povezane odluke

Očekujemo da će sve naše aplikacije koristiti ovaj pristup.

Planirat ćemo nadogradnju svih naših aplikacija koje koriste manje sposoban pristup, poput tvrdog kodiranja u binarnoj datoteci ili izvornom kodu.

Zadržat ćemo nepromijenjene sve naše aplikacije koje koriste sposobniji pristup, poput licencnog poslužitelja.


### Povezani zahtjevi

Dodat ćemo devops mogućnosti za datoteke, uključujući hookove, testove i kontinuiranu integraciju.

Moramo obučiti sve članove razvojnog tima o ovoj odluci.



### Povezani artefakti

Svako područje u kojem implementiramo trebat će vlastitu .env datoteku i povezane datoteke.


### Povezana načela

Lako reverzibilno.


## Bilješke


Primjer datoteke `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Primjer datoteke `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Primjer datoteke `.env.schema` samo s ključevima:

```env
NAME
EMAIL
```
