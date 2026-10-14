# Google Cloud Platformi arhitektuuriotsuse kirje

## Kontekst

Google Cloud Platform (GCP) on silmapaistev pilvearvutuse platvorm, mis pakub mitmesuguseid pilveteenuseid, sealhulgas arvutus-, salvestus- ja võrgulahendusi. Selle ADR-i eesmärk on dokumenteerida arhitektuuriotsused, mis on tehtud meie organisatsiooni GCP-põhise taristu arendamiseks ja teostamiseks.

## Otsus

Meie organisatsioon on otsustanud kasutada oma rakenduse pilvetaristuna Google Cloud Platformi. Selle otsuse peamised kaalutlused on:

   - Kulutõhusus

   - Skaleeritavus

   - Töökindlus

   - Paindlikkus

## Valikud

Meie nõuete täitmiseks on valitud GCP järgmised teenused:

   - Compute Engine virtuaalmasinate ja arvutusressursside jaoks

   - Cloud Storage objektisalvestuse ja failihostimise jaoks

   - Cloud SQL hallatud andmebaasiteenuse jaoks

   - Firebase rakenduste arenduse ja hostimise jaoks

## Põhjendus

   - Kulutõhusus: Google Cloud Platform on võrreldes teiste pilveplatvormidega väga kulutõhus, muutes selle atraktiivseks valikuks eelarvepiirangutega organisatsioonidele.

   - Skaleeritavus: GCP hõlpsasti skaleeritav taristu võimaldab käsitleda mis tahes liiklusmahtu reaalajas.

   - Töökindlus: GCP hallatud teenused pakuvad kõrget töökindlust automaatsete varukoopiate ja katastroofitaaste võimalustega, mis tagavad ressursside ja andmete kõrge käideldavuse.

   - Paindlikkus: platvorm pakub erinevaid tööriistu ja teenuseid erinevates valdkondades nagu tehisintellekt, andmeanalüüs ja IoT, muutes selle väga mitmekülgseks.

## Tagajärjed

Üleminek Google Cloud Platformile nõuab meie meeskondade koolitamist GCP teenuste osas, rakenduse ümberarhitektuurimist, et see ühilduks valitud teenustega, ning taristukoodi uuendamist GCP teenuste toetamiseks. Eeldatakse aga, et kui migratsioon on lõpetatud, on meil väga skaleeritav, töökindel ja kulutõhus taristu oma rakenduse hostimiseks. Samuti peame haldama ressursside varustamise jooksvaid kulusid GCP-s.

## Kokkuvõte

Google Cloud Platform on meie pilvetaristu jaoks suurepärane valik oma kulutõhususe, skaleeritavuse, töökindluse ja paindlikkuse tõttu. Valitud teenuseid kasutades saame pakkuda oma rakendusele väga käideldavat ja töökindlat taristut.
