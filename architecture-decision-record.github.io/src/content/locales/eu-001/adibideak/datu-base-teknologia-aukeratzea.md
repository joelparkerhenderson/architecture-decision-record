# Arkitektura-erabakien erregistroa: datu-base teknologia aukeratzea

## Egoera

Onartua

## Testuingurua

Datuak modu eskalagarri eta errendimendu onekoan gorde eta berreskuratu behar dituen aplikazio berri bat diseinatzen ari gara. Ohikoak diren hiru datu-base teknologia mota identifikatu ditugu: datu-base erlazionalak, dokumentu-datu-baseak eta gertaera-datu-baseak.

Datu-base erlazionalek datuak eskema finkoko taulatan gordetzen dituzte eta datuen osotasun-murrizketa zorrotzak aplikatzen dituzte. Datu-erlazio eta transakzio konplexuak behar dituzten aplikazioetarako egokiak dira. Adibideen artean MySQL, PostgreSQL eta Oracle daude.

Dokumentu-datu-baseek datuak JSON itxurako dokumentuetan gordetzen dituzte eta eskemarik gabekoak dira. Datu-eredu malguak eta horizontalki eskalatzea behar dituzten aplikazioetarako oso egokiak dira. Adibideen artean MongoDB, Couchbase eta Amazon DynamoDB daude.

Gertaera-datu-baseek datuak gertaera-serie gisa gordetzen dituzte, datuen aldaketa bakoitza jasoz. Ikuskaritza, event sourcing eta datuen prozesamendu konplexua behar dituzten aplikazioetarako egokiak dira. Adibideen artean Apache Kafka, Apache Pulsar eta AWS Kinesis daude.
Erabakia

Gure aplikazioaren eskakizunak eta murrizketak arretaz ebaluatu ondoren, dokumentu-datu-base bat erabiltzea erabaki dugu.

## Arrazoibidea

Dokumentu-datu-base bat aukeratu dugu zeren:

1. Gure aplikazioak denboran zehar eboluziona dezakeen datu-eredu malgu bat behar du. Dokumentu-datu-baseek datuak eskemarik gabeko formatuan gordetzeko aukera ematen digute, eta horrek esan nahi du eremu berriak gehitu edo lehendik dauden dokumentuen egitura alda dezakegula datu-basearen eskema aldatu beharrik gabe.

2. Gure aplikazioak horizontalki eskalatu behar du datu eta trafiko kopuru handiak kudeatzeko. Dokumentu-datu-baseek sharding-erako eta erreplikaziorako laguntza integratua eskaintzen dute, eta horrek datuak zerbitzari anitzen artean banatzeko eta irakurketa- eta idazketa-throughput handia kudeatzeko aukera ematen digu.

3. Gure aplikazioak datuak azkar eta eraginkortasunez berreskuratzea behar du. Dokumentu-datu-baseek indexazio- eta kontsulta-gaitasun indartsuak eskaintzen dituzte, datuak azkar eta eraginkortasunez berreskuratzeko aukera ematen dutenak.

4. Gure aplikazioak ez ditu transakzio edo datu-erlazio konplexuak behar. Datu-base erlazionalak bikainak diren arren datuen osotasun-murrizketak betearazten eta transakzio konplexuak kudeatzen, gure aplikazioak ez du halako eskakizunik. Dokumentu-datu-baseek gure erabilera-kasurako koherentzia eta iraunkortasun-berme nahikoak eman ditzakete.

## Ondorioak

Dokumentu-datu-base bat aukeratuz, erabiltzea erabaki dugun teknologia zehatza ikasi eta ulertzen inbertitu beharko dugu. Gainera, ziurtatu beharko dugu gure aplikazioaren datu-eredua dokumentu-datu-basearen datu-ereduarekin ondo egokitzen dela errendimendua eta eskalagarritasuna maximizatzeko.

Hala ere, uste dugu dokumentu-datu-base bat erabiltzearen onurak kostuak baino handiagoak direla, eta gure aplikazioaren eskakizun eta murrizketetarako aukera egokiena dela.
