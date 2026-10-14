# Microsoft Azure DevOps

Obsah:

* [Zhrnutie](#zhrnutie)
  * [Problém](#problém)
  * [Rozhodnutie](#rozhodnutie)
  * [Stav](#stav)
* [Podrobnosti](#podrobnosti)
  * [Predpoklady](#predpoklady)
  * [Obmedzenia](#obmedzenia)
  * [Pozície](#pozície)
  * [Argument](#argument)
  * [Dôsledky](#dôsledky)
* [Súvisiace](#súvisiace)
  * [Súvisiace rozhodnutia](#súvisiace-rozhodnutia)
  * [Súvisiace požiadavky](#súvisiace-požiadavky)
  * [Súvisiace artefakty](#súvisiace-artefakty)
  * [Súvisiace princípy](#súvisiace-princípy)
* [Poznámky](#poznámky)
  * [Microsoft Devops CI: neuspokojivé dobrodružstvo](#microsoft-devops-ci-neuspokojivé-dobrodružstvo)
  * [Kľúčové momenty z diskusie na Hacker News](#kľúčové-momenty-z-diskusie-na-hacker-news)
  * [Windows Development MVP](#windows-development-mvp)
  * [Zhrnutie Edwarda Thomsona (Azure PM)](#zhrnutie-edwarda-thomsona-azure-pm)


## Zhrnutie


### Problém

Chceme používať devops na budovanie, integráciu, nasadzovanie a hosting našich projektov. Zvažujeme Microsoft Azure DevOps.

  * Chceme, aby bol zážitok vývojára rýchly a spoľahlivý, a to pri nastavení devops, napr. konfigurácii, aj pri priebežnom používaní, napr. rýchle časy zostavenia.
  
  * Chceme zvážiť používanie Microsoft Azure ako celku na hosting aplikácií projektu, databáz atď.


### Rozhodnutie

Rozhodli sme sa proti Microsoft Azure DevOps.


### Stav

Rozhodnuté. Sme otvorení prehodnoteniu, ak/keď prídu nové významné informácie.


## Podrobnosti


### Predpoklady

Všetky obvyklé devops predpoklady, ako v knihe Accelerate.

  * Rýchle zostavenia sú významná pomoc. Zrýchľujú spätnoväzbové slučky.

  * Môžeme vymieňať časti od alternatívnych dodávateľov, t. j. možno budeme chcieť priniesť vlastné rýchlejšie build servery alebo použiť vlastnú voľbu systému správy verzií alebo koordinovať s vlastným hostovaným serverom kontinuálnej integrácie.
  
  * Zjednodušená použiteľnosť je významná pomoc pre zážitok vývojára a následne aj pre jemné oblasti, ako je konzistentnosť, jasnosť, bezpečnosť a jednoduchosť krivky učenia.

  * Keď je čokoľvek pokazené alebo problematické, chceme účinný spôsob, ako problém nahlásiť. To je obzvlášť dôležité pri akýchkoľvek problémoch súvisiacich s bezpečnosťou.


### Obmedzenia

Žiadne známe. Azure má zverejnený záväzok dobre spolupracovať s externými nástrojmi.


### Pozície

Zvažovali sme použitie Microsoft Azure Devops oproti AWS, ktoré je zavedeným riešením.

Experimentovali sme s Azure DevOps, Azure Pipelines, Azure Repo a spustením nového servera v Azure cez Terraform.

Experimentovali sme so získaním podpory od zástupcov Microsoftu.

Informácie sme zbierali od kolegov na blogoch a Hacker News.


### Argument

Azure DevOps inzeruje vynikajúci súbor ponúk, ale tie neobstoja, nefungujú dobre spolu a podpora je slabá.

Naša priama skúsenosť:

  * Nastavenie Azure je zmes používateľských rozhraní, z ktorých sa niektoré prekrývajú s účtami Microsoft a niektoré nie. Napr. existuje prihlásenie do Azure, prihlásenie na Microsoft.com, prihlásenie na Live.com atď. a všetky sú súčasne v hre.

  * Pri nastavovaní sme narazili na menší bezpečnostný problém a nenašli sme riešenie. Skúšali sme ho nahlásiť mnohými spôsobmi mnohým zástupcom Microsoftu, bez úspechu. Úspešne sme ho nahlásili bezpečnostnému tímu Microsoftu, ktorý odpovedal, že to opravovať nebude.

  * Dokumentácia je často buď nesprávna, alebo zastaraná. Aspoň časť z toho je spôsobená slabým vyhľadávačom Microsoftu a časť podpriemerným SEO.
  
  * Nastavenie Terraformu je dobre zdokumentované a funguje. Podpora Terraformu je však v porovnaní s AWS slabá, pretože Microsoft buduje obchodné vzťahy s dodávateľmi, aby vytvárali príklady nastavenia cez Terraform v celom reťazci.

Skúsenosti kolegov:

  * Potom, čo sme urobili vlastné slepé hodnotenie, hľadali sme skúsenosti kolegov. To, čo sme našli, potvrdilo naše skúsenosti.

  * Kolegovia uvádzali ďalšie problémy s časmi zostavenia a problémy so serverom na zostavenie, ktorý si prinesiete sami (bring-your-own). Tieto problémy sú výrazne závažnejšie než problémy s UI, pretože vykonávanie zostavení je hlavným účelom pipeline na zostavenie a očakávame, že ich budeme robiť veľa denne.

  * Našli sme vynikajúcu účasť kolegov z Azure v diskusných oblastiach. Za to patrí Microsoftu uznanie. Obzvlášť nás zaujal Edward Thomson, PM a programátor Azure, kvôli svojej účasti, priamosti a technickým vysvetleniam.


### Dôsledky

Voľba Microsoft Azure DevOps sa javí ako pravdepodobne drahšia (~3x) v čase a nákladoch než nevoľba Azure.


## Súvisiace


### Súvisiace rozhodnutia

Ak zvolíme Azure DevOps, existuje mnoho súvisiacich ponúk vrátane Azure Repo, Azure Pipeline atď. Domnievame sa, že ak zvolíme Azure Devops, môže nám to uľahčiť používanie ďalších schopností Azure alebo sťažiť používanie schopností iných dodávateľov.

Domnievame sa, že Microsoft robí veľké pokroky v zážitku vývojárov, a vidíme, že Microsoft robí veľké akvizície vývojárskych nástrojov (napr. GitHub) a závislostí (napr. Citus).

Ak zvolíme Azure DevOps, možno budeme chcieť zdôrazniť voľbu ponúk z akvizícií Microsoftu a tiež sa možno budeme chcieť k akvizičným ponukám postaviť s väčšou starostlivosťou/hodnotením kvôli potenciálnemu odmietnutiu tkaniva, napr. riziku fluktuácie zamestnancov.


### Súvisiace požiadavky

Chceme, aby boli časy zostavenia veľmi rýchle. Sme ochotní za to zaplatiť vysokú prirážku. Je to preto, že chceme iterovať veľmi rýchlo.

Chceme veľmi vysokú spoľahlivosť. Sme ochotní za to zaplatiť vysokú prirážku. Je to preto, že testujeme prípady použitia s vysokou hodnotou vrátane finančných transakcií, dôverných transakcií atď.

Naše 4 najdôležitejšie devops KPI zahŕňajú strednú dobu obnovy, čo vyžaduje rýchle zostavenia a vysokú spoľahlivosť.


### Súvisiace artefakty

Chceme, aby build systém vydával artefakty vhodné na použitie v iných systémoch, ako je Artifactory.


### Súvisiace princípy

Ľahko vratné. Azure DevOps môžeme hodnotiť paralelne s existujúcim AWS.


## Poznámky


### Microsoft Devops CI: neuspokojivé dobrodružstvo

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Príspevok na blogu.

„Ako softvérový vývojár viem z prvej ruky, aké ťažké je vytvárať kvalitné produkty rýchlo a lacno. Je to umelecká forma, ktorú sa nám niekedy darí, a inokedy sa zvrhne na niečo podobné vládnej zdravotníckej webovej stránke z éry Obamu. Naša miera kontroly nad výsledným produktom sa líši a vina za neúspech často padá na nesprávnych ľudí v rozhodovacej hierarchii. Microsoft Azure DevOps (predtým známy ako Visual Studio Team Services) je napriek zjavne dobrým úmyslom dokonalou búrkou zlých rozhodnutí a slabého vykonania.“


### Kľúčové momenty z diskusie na Hacker News

https://news.ycombinator.com/item?id=18983586

„V práci Azure DevOps intenzívne používame a potom, čo som používal GitHub, Gitlab, vlastné hostované riešenia, Jenkins, TeamCity... Azure DevOps sa umiestňuje úplne posledný.“

„UI je všade strašne ťažkopádne. Najhoršie sú pre mňa pull requesty. Neuveriteľne ťažko sa pracuje s ľuďmi na pull requeste. Ani vám nedokážem ukázať „jeden“ konkrétny problém – u nás je to pokazené všade.“

„Azure Devops je niečo, čo chcem milovať. UI sa neustále mení, ale neopravuje základné chyby, ktoré existujú veky.“

„Nástroje nie sú dobre integrované, UI je naozaj pomalé, neexistuje pohľad na dashboard aktívnych pull requestov, zostavení, vydaní atď. pre moje obľúbené repozitáre. Časy zostavenia/nasadenia sú šialene pomalé.“

„Skúšali sme používať aj Azure Boards (Work Items, Boards, Backlogs atď.). Au. Je to úplná zmes UI nesúvisiacich nápadov. Namiesto toho, aby dobre implementovali jednu vec, implementovali dve desiatky vecí hrozne.“


### Windows Development MVP

Som Windows Development MVP. Cítim, že musím niesť časť zodpovednosti za to, že som o týchto problémoch nehovoril hlasnejšie. Ale musím povedať, že som sklamaný, keď počujem, že ste „prekvapení“ problémami s UX. Hovorím vašim ľuďom, že UX je hrozné (napr. ešte pred spustením) a neustále som počul „vieme, opravujeme to“. Začnem formalizovať spätnú väzbu a pretlačím ju kanálmi, zostaňte naladení. Som aj miestny (Bellevue), rád by som prišiel a skúsil vybudovať pipeline pre našu pomerne jednoduchú oss aplikáciu .net/wpf/uwp. Tuším, že to bude pre nás oboch otvorenie očí.

Niektoré príklady:

* Nemôžete vybudovať pipeline s git repozitárom, ktorý obsahuje submoduly

* Zistil som, že je nemožné upraviť PATH pre niektoré vlastné nástroje

* Nový zážitok z pipeline jednoducho nedáva veľký zmysel, noví používatelia, ktorí klikajú okolo, nakoniec skončia pri nesprávnej dokumentácii.


### Zhrnutie Edwarda Thomsona (Azure PM)

Napísal som kód, ktorý zlučuje vaše pull requesty. Program Manager v Microsofte pre Azure DevOps; predtým softvérový inžinier na nástrojoch správy verzií v GitHube, Microsofte, SourceGear.

https://www.edwardthomson.com/

Spoluudržiavateľ libgit2. https://libgit2.github.io

Spoluhostiteľ All Things Git, podcastu o Gite. https://www.allthingsgit.com/

Kurátor Developer Tools Weekly, newslettera o vývojárskych nástrojoch. https://developertoolsweekly.com/
