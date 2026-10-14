# Záznam architektonického rozhodnutia pre framework Python Django

Dátum rozhodnutia: 2021-07-15

Stav: Prijaté

## Kontext

Naša organizácia plánuje vyvinúť webovú aplikáciu, ktorá spravuje dáta zákazníkov. Ako programovací jazyk sme zvolili Python a ako webový framework na vývoj aplikácie zvažujeme Django.

## Rozhodnutie

Rozhodli sme sa na vývoj webovej aplikácie použiť webový framework Django. Django poskytuje robustný súbor nástrojov a funkcií na rýchle a efektívne budovanie webových aplikácií. 

## Faktory

Medzi faktory, ktoré ovplyvnili naše rozhodnutie, patria:

1. Objektovo-relačné mapovanie (ORM): Django má vstavané ORM, ktoré nám umožňuje pracovať s databázou bez písania SQL dopytov. To uľahčuje vývoj aplikácie a jej dlhodobú údržbu.

2. Framework MVC: Django sleduje architektúru Model-View-Controller (MVC), čo uľahčuje oddelenie obchodnej logiky a prezentačnej vrstvy aplikácie.

3. Škálovateľnosť: Django je známe svojimi schopnosťami škálovania, vďaka čomu je výbornou voľbou na vývoj rozsiahlych aplikácií.

4. Bezpečnosť: Django má vstavané bezpečnostné funkcie, ako je ochrana pred bežnými webovými útokmi, ako je cross-site scripting (XSS) a SQL injection.

5. Podpora komunity: Django má veľkú a aktívnu komunitu, ktorá poskytuje podporu a prispieva k vývoju frameworku.

## Zvažované alternatívy

Zvažovali sme iné webové frameworky ako Flask a Pyramid. Zistili sme však, že Django je zrelší a etablovanejší framework s robustným súborom funkcií.

Diskutovali sme tiež o vývoji aplikácie bez webového frameworku s použitím knižníc ako SQLAlchemy a Flask-RESTful. Zistili sme však, že Django ponúka širšiu funkcionalitu, vďaka čomu je lepšou voľbou pre kompletnú webovú aplikáciu.

## Dôsledky

Prijatie Djanga povedie k týmto dôsledkom:

1. Jednoduchší vývoj a údržba aplikácie vďaka vstavaným nástrojom a funkciám Djanga.

2. Oddelenie obchodnej logiky a prezentačnej vrstvy, čo vedie k organizovanejšiemu a ľahšie udržiavateľnému kódu.

3. Škálovateľnosť a robustnosť aplikácie.

4. Vstavané bezpečnostné funkcie, ktoré pomáhajú chrániť aplikáciu pred bežnými webovými útokmi.

5. Prístup k veľkej a aktívnej komunite pre podporu.

Chápeme, že Django má strmšiu krivku učenia než iné frameworky, ale považujeme ju za investíciu, ktorá sa vyplatí vďaka dlhodobým prínosom, ktoré poskytuje.

## Záver

Na základe zvažovaných faktorov sme sa rozhodli na vývoj webovej aplikácie použiť webový framework Django. Veríme, že funkcie, podpora komunity a schopnosti škálovania Djanga z neho robia najlepšiu voľbu na vybudovanie kompletnej webovej aplikácie. Našich vývojárov vyškolíme v používaní Djanga, aby sme zabezpečili, že sa framework používa efektívne a účinne.