# Záznam architektonického rozhodnutia: výber databázovej technológie

## Stav

Prijaté

## Kontext

Navrhujeme novú aplikáciu, ktorá vyžaduje ukladanie a získavanie dát škálovateľným a výkonným spôsobom. Identifikovali sme tri typy databázových technológií, ktoré sa bežne používajú: relačné databázy, dokumentové databázy a databázy udalostí.

Relačné databázy ukladajú dáta v tabuľkách s pevnými schémami a presadzujú prísne obmedzenia integrity dát. Sú vhodné pre aplikácie, ktoré vyžadujú zložité vzťahy medzi dátami a transakcie. Príklady zahŕňajú MySQL, PostgreSQL a Oracle.

Dokumentové databázy ukladajú dáta v dokumentoch podobných JSON a sú bez schémy. Sú vhodné pre aplikácie, ktoré vyžadujú flexibilné dátové modely a horizontálne škálovanie. Príklady zahŕňajú MongoDB, Couchbase a Amazon DynamoDB.

Databázy udalostí ukladajú dáta ako sériu udalostí a zachytávajú každú zmenu dát. Sú vhodné pre aplikácie, ktoré vyžadujú audit, event sourcing a zložité spracovanie dát. Príklady zahŕňajú Apache Kafka, Apache Pulsar a AWS Kinesis.
Rozhodnutie

Po starostlivom vyhodnotení požiadaviek a obmedzení našej aplikácie sme sa rozhodli použiť dokumentovú databázu.

## Zdôvodnenie

Vybrali sme dokumentovú databázu, pretože:

1. Naša aplikácia vyžaduje flexibilný dátový model, ktorý sa môže časom vyvíjať. Dokumentové databázy nám umožňujú ukladať dáta vo formáte bez schémy, čo znamená, že môžeme pridávať nové polia alebo meniť štruktúru existujúcich dokumentov bez nutnosti upravovať schému databázy.

2. Naša aplikácia sa musí horizontálne škálovať, aby zvládla veľké objemy dát a prevádzky. Dokumentové databázy poskytujú vstavanú podporu shardingu a replikácie, čo nám umožňuje distribuovať dáta medzi viacero serverov a zvládať vysokú priepustnosť čítania a zápisu.

3. Naša aplikácia vyžaduje rýchle a efektívne získavanie dát. Dokumentové databázy poskytujú výkonné možnosti indexovania a dopytovania, ktoré nám umožňujú získavať dáta rýchlo a efektívne.

4. Naša aplikácia nevyžaduje zložité transakcie ani vzťahy medzi dátami. Hoci relačné databázy vynikajú v presadzovaní obmedzení integrity dát a spracovaní zložitých transakcií, naša aplikácia také požiadavky nemá. Dokumentové databázy môžu poskytnúť dostatočné záruky konzistencie a trvanlivosti pre náš prípad použitia.

## Dôsledky

Výberom dokumentovej databázy budeme musieť investovať do učenia a pochopenia konkrétnej technológie, ktorú sa rozhodneme použiť. Okrem toho sa budeme musieť uistiť, že dátový model našej aplikácie dobre zapadá do dátového modelu dokumentovej databázy, aby sme maximalizovali výkon a škálovateľnosť.

Veríme však, že prínosy používania dokumentovej databázy prevažujú nad nákladmi a že je to najlepšia voľba pre požiadavky a obmedzenia našej aplikácie.
