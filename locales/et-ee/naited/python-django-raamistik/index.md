# Pythoni Django raamistiku arhitektuuriotsuse kirje

Otsuse kuupäev: 2021-07-15

Olek: Aktsepteeritud

## Kontekst

Meie organisatsioon plaanib arendada veebirakendust, mis haldab kliendiandmeid. Oleme valinud programmeerimiskeeleks Pythoni ja kaalume rakenduse arenduseks veebiraamistikuna Djangot.

## Otsus

Otsustasime kasutada veebirakenduse arenduseks Django veebiraamistikku. Django pakub töökindlat tööriistade ja funktsioonide komplekti veebirakenduste kiireks ja tõhusaks ehitamiseks. 

## Tegurid

Mõned tegurid, mis meie otsust mõjutasid, on:

1. Objekt-relatsiooniline kaardistus (ORM): Djangol on sisseehitatud ORM, mis võimaldab meil andmebaasiga suhelda SQL-päringuid kirjutamata. See teeb rakenduse arendamise ja pikaajalise hooldamise lihtsamaks.

2. MVC-raamistik: Django järgib Model-View-Controller (MVC) arhitektuuri, mis teeb rakenduse ärilogika ja esituskihtide eraldamise lihtsamaks.

3. Skaleeritavus: Django on tuntud oma skaleeritavuse poolest, mis teeb sellest suurepärase valiku suuremastaabiliste rakenduste arendamiseks.

4. Turvalisus: Djangol on sisseehitatud turvafunktsioonid, nagu kaitse tavaliste veebirünnakute vastu, nagu saidiülene skriptimine (XSS) ja SQL-i süstimine.

5. Kogukonna toetus: Djangol on suur ja aktiivne kogukond, mis pakub tuge ja aitab kaasa raamistiku arendamisele.

## Kaalutud alternatiivid

Kaalusime teisi veebiraamistikke nagu Flask ja Pyramid. Leidsime aga, et Django on küpsem ja paremini väljakujunenud raamistik töökindla funktsioonide komplektiga.

Arutasime ka rakenduse arendamist ilma veebiraamistikuta ja teekidega nagu SQLAlchemy ja Flask-RESTful. Leidsime aga, et Django pakub laiemat funktsionaalsust, mis teeb sellest parema valiku täieliku veebirakenduse jaoks.

## Tagajärjed

Django kasutuselevõtt toob kaasa järgmised tagajärjed:

1. Rakenduse arendamine ja hooldamine on lihtsam tänu Django sisseehitatud tööriistadele ja funktsioonidele.

2. Ärilogika ja esituskihi eraldamine, mis viib organiseeritumasse ja lihtsamini hooldatavasse koodi.

3. Rakenduse skaleeritavus ja töökindlus.

4. Sisseehitatud turvafunktsioonid, mis aitavad rakendust tavaliste veebirünnakute vastu kaitsta.

5. Juurdepääs suurele ja aktiivsele kogukonnale toe saamiseks.

Mõistame, et Djangol on teistest raamistikest järsem õppimiskõver, kuid leiame, et see on pikaajaliste eeliste tõttu investeeringut väärt.

## Kokkuvõte

Kaalutud tegurite põhjal otsustasime kasutada veebirakenduse arenduseks Django veebiraamistikku. Usume, et Django funktsioonid, kogukonna toetus ja skaleeritavus teevad sellest parima valiku täieliku veebirakenduse ehitamiseks. Koolitame oma arendajaid Djangot kasutama, et tagada raamistiku tõhus ja tulemuslik kasutamine.
