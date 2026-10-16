# Architektūros sprendimo įrašas: duomenų bazės technologijos pasirinkimas

## Būsena

Priimtas

## Kontekstas

Projektuojame naują programą, kuriai reikia duomenis saugoti ir gauti keičiamo mastelio ir našiu būdu. Nustatėme tris dažniausiai naudojamų duomenų bazių technologijų tipus: reliacines duomenų bazes, dokumentų duomenų bazes ir įvykių duomenų bazes.

Reliacinės duomenų bazės saugo duomenis lentelėse su fiksuotomis schemomis ir taiko griežtus duomenų vientisumo apribojimus. Jos tinka programoms, kurioms reikia sudėtingų duomenų ryšių ir transakcijų. Pavyzdžiai: MySQL, PostgreSQL ir Oracle.

Dokumentų duomenų bazės saugo duomenis į JSON panašiuose dokumentuose ir neturi schemos. Jos gerai tinka programoms, kurioms reikia lanksčių duomenų modelių ir horizontalaus mastelio keitimo. Pavyzdžiai: MongoDB, Couchbase ir Amazon DynamoDB.

Įvykių duomenų bazės saugo duomenis kaip įvykių seką, fiksuodamos kiekvieną duomenų pakeitimą. Jos tinka programoms, kurioms reikia audito, įvykių šaltinių modelio (angl. event sourcing) ir sudėtingo duomenų apdorojimo. Pavyzdžiai: Apache Kafka, Apache Pulsar ir AWS Kinesis.
Sprendimas

Kruopščiai įvertinę savo programos reikalavimus ir apribojimus, nusprendėme naudoti dokumentų duomenų bazę.

## Pagrindimas

Pasirinkome dokumentų duomenų bazę, nes:

1. Mūsų programai reikia lankstaus duomenų modelio, kuris laikui bėgant gali keistis. Dokumentų duomenų bazės leidžia saugoti duomenis be schemos formatu, o tai reiškia, kad galime pridėti naujų laukų ar keisti esamų dokumentų struktūrą nekeisdami duomenų bazės schemos.

2. Mūsų programa turi keisti mastelį horizontaliai, kad apdorotų didelius duomenų ir srauto kiekius. Dokumentų duomenų bazės turi integruotą šardų ir replikacijos palaikymą, kuris leidžia paskirstyti duomenis keliuose serveriuose ir apdoroti didelį skaitymo bei rašymo pralaidumą.

3. Mūsų programai reikia greito ir efektyvaus duomenų gavimo. Dokumentų duomenų bazės turi galingas indeksavimo ir užklausų galimybes, leidžiančias greitai ir efektyviai gauti duomenis.

4. Mūsų programai nereikia sudėtingų transakcijų ar duomenų ryšių. Nors reliacinės duomenų bazės puikiai užtikrina duomenų vientisumo apribojimus ir tvarko sudėtingas transakcijas, mūsų programa tokių reikalavimų neturi. Dokumentų duomenų bazės gali užtikrinti pakankamas nuoseklumo ir patvarumo garantijas mūsų naudojimo atvejui.

## Pasekmės

Pasirinkę dokumentų duomenų bazę, turėsime investuoti į konkrečios pasirinktos technologijos mokymąsi ir supratimą. Be to, turėsime užtikrinti, kad mūsų programos duomenų modelis gerai tiktų dokumentų duomenų bazės duomenų modeliui, kad našumas ir mastelio keitimas būtų maksimalūs.

Tačiau manome, kad dokumentų duomenų bazės naudojimo privalumai nusveria išlaidas ir kad ji geriausiai atitinka mūsų programos reikalavimus ir apribojimus.
