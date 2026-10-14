# Arhitektuuriotsuse kirje: andmebaasitehnoloogia valimine

## Olek

Aktsepteeritud

## Kontekst

Kujundame uut rakendust, mis peab andmeid salvestama ja hankima skaleeritaval ja jõudlusel viisil. Oleme tuvastanud kolm tavaliselt kasutatavat andmebaasitehnoloogia tüüpi: relatsioonilised andmebaasid, dokumendiandmebaasid ja sündmusandmebaasid.

Relatsioonilised andmebaasid salvestavad andmeid fikseeritud skeemidega tabelites ja jõustavad ranged andmete terviklikkuse piirangud. Need sobivad rakendustele, mis vajavad keerulisi andmesuhteid ja tehinguid. Näited on MySQL, PostgreSQL ja Oracle.

Dokumendiandmebaasid salvestavad andmeid JSON-i sarnastes dokumentides ja on skeemivabad. Need sobivad hästi rakendustele, mis vajavad paindlikke andmemudeleid ja horisontaalset skaleerimist. Näited on MongoDB, Couchbase ja Amazon DynamoDB.

Sündmusandmebaasid salvestavad andmeid sündmuste jadana, jäädvustades iga andmete muudatuse. Need sobivad rakendustele, mis vajavad auditeerimist, sündmuste allikat (event sourcing) ja keerulist andmetöötlust. Näited on Apache Kafka, Apache Pulsar ja AWS Kinesis.
Otsus

Pärast meie rakenduse nõuete ja piirangute hoolikat hindamist otsustasime kasutada dokumendiandmebaasi.

## Põhjendus

Valisime dokumendiandmebaasi, sest:

1. Meie rakendus vajab paindlikku andmemudelit, mis võib aja jooksul areneda. Dokumendiandmebaasid lubavad meil andmeid salvestada skeemivabas vormingus, mis tähendab, et saame lisada uusi välju või muuta olemasolevate dokumentide struktuuri andmebaasi skeemi muutmata.

2. Meie rakendus peab suurte andmemahtude ja liikluse käsitlemiseks horisontaalselt skaleeruma. Dokumendiandmebaasidel on sisseehitatud tugi sharding'ule ja replikatsioonile, mis võimaldab meil andmeid mitme serveri vahel jaotada ning käsitleda suurt lugemis- ja kirjutamisläbilaset.

3. Meie rakendus vajab kiiret ja tõhusat andmete hankimist. Dokumendiandmebaasid pakuvad võimsaid indekseerimis- ja päringuvõimalusi, mis võimaldavad andmeid kiiresti ja tõhusalt hankida.

4. Meie rakendus ei vaja keerulisi tehinguid ega andmesuhteid. Kui relatsioonilised andmebaasid on andmete terviklikkuse piirangute jõustamises ja keeruliste tehingute käsitlemises silmapaistvad, siis meie rakendusel selliseid nõudeid ei ole. Dokumendiandmebaasid võivad meie kasutusjuhu jaoks pakkuda piisavat järjepidevuse ja vastupidavuse garantiid.

## Tagajärjed

Dokumendiandmebaasi valimisega peame investeerima valitud konkreetse tehnoloogia õppimisse ja mõistmisse. Lisaks peame tagama, et meie rakenduse andmemudel sobib hästi dokumendiandmebaasi andmemudeliga, et jõudlust ja skaleeritavust maksimeerida.

Usume aga, et dokumendiandmebaasi kasutamise eelised kaaluvad kulud üles ja see on meie rakenduse nõuete ja piirangutega parim sobivus.
