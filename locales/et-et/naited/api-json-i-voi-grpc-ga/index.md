# Arhitektuuriotsuse kirje: API JSON-i või gRPC-ga

## Olek

Aktsepteeritud

## Kontekst

Kujundame API-d uue teenuse jaoks, mida kasutavad mitmed kliendid. Oleme kaalunud kahte võimalust API teostamiseks: JSON üle HTTP-i või gRPC.

JSON üle HTTP-i on laialt kasutatav lähenemine API-de ehitamiseks ning seda toetavad paljud programmeerimiskeeled ja raamistikud. See lähenemine on lihtne, kerge ja hõlpsasti mõistetav, mistõttu on see paljude projektide jaoks hea valik. See võib aga olla teistest võimalustest vähem tõhus, eriti suurte andmemahtude käsitlemisel.

gRPC on seevastu uuem tehnoloogia, mis pakub API-de ehitamiseks tõhusamat viisi. See kasutab andmete edastamiseks binaarset serialiseerimist, mis võib olla kiirem ja kompaktsem kui JSON. gRPC toetab ka kahesuunalist voogedastust, mis teeb sellest hea valiku reaalajarakenduste jaoks.

## Otsus

Pärast mõlema võimaluse plusside ja miinuste kaalumist otsustasime kasutada oma API jaoks gRPC-d. Kuigi JSON üle HTTP-i on lihtsam võimalus, usume, et gRPC pakub meie teenusele tõhusamat ja skaleeritavamat lahendust. Eeldame ka, et meie API töötleb suurt hulka andmeid ja gRPC binaarne serialiseerimine on selle kasutusjuhu jaoks tõhusam.

Lisaks usume, et gRPC toetus kahesuunalisele voogedastusele on kasulik reaalajarakenduste jaoks, mida me tulevikus arendada võime.

## Tagajärjed

gRPC valimisega peame oma API ehitamiseks kasutama teistsugust tööriistade ja teekide komplekti kui JSON üle HTTP-i puhul. See võib nõuda lisaaega ja -vaeva nende tehnoloogiate õppimiseks ja teostamiseks. Lisaks peavad kliendid, kes tahavad meie API-d kasutada, kasutama gRPC-ga ühilduvaid teeke, mida ei pruugita toetada nii laialt kui JSON üle HTTP-i teeke.

Usume aga, et gRPC eelised kaaluvad need potentsiaalsed puudused üles, ning oleme kindlad, et see otsus viib tõhusama ja skaleeritavama API-ni.
