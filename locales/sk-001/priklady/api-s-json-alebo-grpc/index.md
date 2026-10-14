# Záznam architektonického rozhodnutia: API s JSON alebo gRPC

## Stav

Prijaté

## Kontext

Navrhujeme API pre novú službu, ktorú bude používať viacero klientov. Zvažovali sme dve možnosti implementácie API: použitie JSON cez HTTP alebo použitie gRPC.

JSON cez HTTP je široko používaný prístup k budovaniu API a podporuje ho mnoho programovacích jazykov a frameworkov. Tento prístup je jednoduchý, ľahký a ľahko pochopiteľný, vďaka čomu je dobrou voľbou pre mnohé projekty. Môže však byť menej efektívny ako iné možnosti, najmä pri spracovaní veľkého množstva dát.

gRPC je na druhej strane novšia technológia, ktorá ponúka efektívnejší spôsob budovania API. Na prenos dát používa binárnu serializáciu, ktorá môže byť rýchlejšia a kompaktnejšia než použitie JSON. gRPC podporuje aj obojsmerné streamovanie, vďaka čomu je dobrou voľbou pre aplikácie v reálnom čase.

## Rozhodnutie

Po zvážení výhod a nevýhod oboch možností sme sa rozhodli použiť gRPC pre naše API. Hoci je JSON cez HTTP jednoduchšou možnosťou, veríme, že gRPC poskytne efektívnejšie a škálovateľnejšie riešenie pre našu službu. Očakávame tiež, že naše API bude spracúvať veľké množstvo dát a binárna serializácia gRPC bude pre tento prípad použitia efektívnejšia.

Okrem toho veríme, že podpora obojsmerného streamovania v gRPC bude prínosná pre aplikácie v reálnom čase, ktoré by sme mohli v budúcnosti vyvíjať.

## Dôsledky

Výberom gRPC budeme musieť na vybudovanie nášho API použiť iný súbor nástrojov a knižníc než pri použití JSON cez HTTP. To môže vyžadovať dodatočný čas a úsilie na osvojenie a implementáciu týchto technológií. Okrem toho klienti, ktorí chcú naše API používať, budú musieť používať knižnice kompatibilné s gRPC, ktoré nemusia byť tak široko podporované ako knižnice pre JSON cez HTTP.

Veríme však, že prínosy používania gRPC prevažujú nad týmito potenciálnymi nevýhodami, a sme presvedčení, že toto rozhodnutie povedie k efektívnejšiemu a škálovateľnejšiemu API.