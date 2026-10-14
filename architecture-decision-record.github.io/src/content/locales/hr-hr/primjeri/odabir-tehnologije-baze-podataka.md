# Zapis arhitekturne odluke: odabir tehnologije baze podataka

## Status

Prihvaćeno

## Kontekst

Dizajniramo novu aplikaciju koja zahtijeva pohranu i dohvat podataka na skalabilan i performantan način. Utvrdili smo tri vrste tehnologija baza podataka koje se uobičajeno koriste: relacijske baze podataka, dokumentne baze podataka i baze podataka događaja.

Relacijske baze podataka pohranjuju podatke u tablice s fiksnim shemama i nameću stroga ograničenja integriteta podataka. Prikladne su za aplikacije koje zahtijevaju složene odnose podataka i transakcije. Primjeri uključuju MySQL, PostgreSQL i Oracle.

Dokumentne baze podataka pohranjuju podatke u dokumentima sličnima JSON-u i nemaju shemu. Prikladne su za aplikacije koje zahtijevaju fleksibilne modele podataka i horizontalno skaliranje. Primjeri uključuju MongoDB, Couchbase i Amazon DynamoDB.

Baze podataka događaja pohranjuju podatke kao niz događaja, bilježeći svaku promjenu podataka. Prikladne su za aplikacije koje zahtijevaju reviziju, event sourcing i složenu obradu podataka. Primjeri uključuju Apache Kafka, Apache Pulsar i AWS Kinesis.
Odluka

Nakon pažljivog vrednovanja zahtjeva i ograničenja naše aplikacije odlučili smo koristiti dokumentnu bazu podataka.

## Obrazloženje

Odabrali smo dokumentnu bazu podataka jer:

1. Naša aplikacija zahtijeva fleksibilan model podataka koji se može razvijati tijekom vremena. Dokumentne baze podataka omogućuju nam pohranu podataka u formatu bez sheme, što znači da možemo dodavati nova polja ili mijenjati strukturu postojećih dokumenata bez izmjene sheme baze podataka.

2. Naša aplikacija mora se horizontalno skalirati kako bi obradila velike količine podataka i prometa. Dokumentne baze podataka pružaju ugrađenu podršku za sharding i replikaciju, što nam omogućuje distribuciju podataka na više poslužitelja i obradu visoke propusnosti čitanja i pisanja.

3. Naša aplikacija zahtijeva brz i učinkovit dohvat podataka. Dokumentne baze podataka pružaju moćne mogućnosti indeksiranja i upita koje nam omogućuju brz i učinkovit dohvat podataka.

4. Naša aplikacija ne zahtijeva složene transakcije ni odnose među podacima. Iako relacijske baze podataka ističu se u nametanju ograničenja integriteta podataka i obradi složenih transakcija, naša aplikacija nema takve zahtjeve. Dokumentne baze podataka mogu pružiti dovoljna jamstva dosljednosti i trajnosti za naš slučaj uporabe.

## Posljedice

Odabirom dokumentne baze podataka morat ćemo uložiti u učenje i razumijevanje specifične tehnologije koju odaberemo. Osim toga, morat ćemo osigurati da se model podataka naše aplikacije dobro uklapa u model podataka dokumentne baze podataka kako bismo maksimizirali performanse i skalabilnost.

Međutim, vjerujemo da koristi od uporabe dokumentne baze podataka nadmašuju troškove i da je ona najbolje rješenje za zahtjeve i ograničenja naše aplikacije.
