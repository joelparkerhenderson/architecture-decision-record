# Ukladanie tajomstiev

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
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Zhrnutie


### Problém

Potrebujeme ukladať tajomstvá, ako sú heslá, súkromné kľúče, autentifikačné tokeny atď.

Niektoré tajomstvá sú orientované na používateľa. Napríklad náš vývojár chce mať možnosť pomocou mobilného telefónu vyhľadať heslo k službe.

Niektoré tajomstvá sú orientované na systém. Napríklad naša pipeline kontinuálneho doručovania musí vedieť vyhľadať prihlasovacie údaje k nášmu cloudovému hostingu.


### Rozhodnutie

Bitwarden pre tajomstvá orientované na používateľa

Vault by HashiCorp pre tajomstvá orientované na systém.


### Stav

Rozhodnuté. Sme otvorení novým alternatívam, keď sa objavia.


## Podrobnosti


### Predpoklady

Na tento účel a pri našom súčasnom stave si ceníme pohodlie orientované na používateľa, ako sú použiteľné mobilné aplikácie.

  * Chceme zabezpečiť rýchly a jednoduchý prístup na cestách, napríklad pre vývojára, ktorý vykonáva pohotovostné inžinierstvo spoľahlivosti systémov.

  * Chceme mať možnosť zdieľať niektoré tajomstvá medzi vybranými ľuďmi, napríklad tímom.

Nesnažíme sa riešiť pre jediného poskytovateľa, napríklad ukladanie všetkých tajomstiev výlučne u Amazonu, Azure alebo Googlu.

Nechceme ad hoc prístupy, ako „zapamätaj si to“ alebo „napíš si to na papierik“ alebo „vymysli si vlastný spôsob ukladania“.

Náš bezpečnostný model na tento účel je v poriadku s používaním vysoko rešpektovaných komerčných hotových (COTS) dodávateľov, ako sú SaaS nástroje na správu hesiel.


### Obmedzenia

Práve teraz chceme niečo jednoduché, t. j. bez potreby písať kód, bez potreby inštalovať servery, bez potreby veľkého záväzku, bez potreby štandardizovať všetkých.


### Pozície

Zvažovali sme:

1. Hotové správcovské nástroje hesiel orientované na používateľa: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG atď.

2. Komerčné hotové správcovské nástroje hesiel orientované na systém: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Prístupy orientované na zdieľanie: použitie zdieľaného dokumentu Google, zdieľaného kanála Slack, zdieľaného sieťového priečinka atď.

4. Nízkotechnologické ad hoc prístupy, ako zapamätanie, napísanie poznámky alebo spoliehanie sa na to, že si každý používateľ vymyslí vlastný prístup.


### Argument

Bitwarden, LastPass, 1Password a Dashlane sú všetko komerčné hotové produkty.

  * Podobné druhy funkcií pre používateľov, tímy, organizácie atď.

  * Desktopové schopnosti pre Windows a Mac a mobilné schopnosti pre Android a iOS.

  * Rozšírenia prehliadačov pre Chrome a Firefox na automatické vypĺňanie formulárov atď.

Bitwarden má oproti ostatným dve výhody:

  * Bitwarden je open source, čo znamená, že bezpečnosť môže byť podrobená vzájomnej kontrole a spoločnosť je tiež široko oceňovaná vývojármi orientovanými na bezpečnosť.

  * Anekdoty softvérových pracovníkov opisujú výraznú preferenciu Bitwardenu pred ostatnými.

Typický dobrý článok: https://jcs.org/2017/11/17/bitwarden

Typická stránka s hlasovaním porovnávajúca nástroje vedľa seba: https://stackshare.io/stackups/bitwarden-vs-dashlane

KeyPass, pass, GPG atď. odkladáme, pretože prinášajú dodatočnú zložitosť. Všetky tieto vyzerajú ako skvelé riešenia pre technických používateľov. GPG vyzerá obzvlášť dobre pre technických používateľov, ktorí chcú príkazovo orientované schopnosti naprieč systémami.

KMS odkladáme, pretože má viazanosť na jediného poskytovateľa.

Pre potreby orientované na systém volíme Vault, pretože recenzie sú úžasne pozitívne a pretože HashiCorp má vynikajúcu históriu softvéru a podpory najvyššej kvality.

Vetujeme prístupy zdieľania, ako prostredníctvom zdieľaných dokumentov, zdieľaných kanálov, zdieľaných sieťových priečinkov atď. Tie neposkytujú bezpečnostné kvality, ktoré chceme.

Vetujeme ad hoc nízkotechnologické prístupy, pretože sa všetci zhodujeme, že to nie je dlhodobá cesta vpred.


### Dôsledky

Vývojári možno budú musieť sledovať tajomstvá na dvoch miestach: Bitwarden pre prístup orientovaný na používateľa a Vault pre prístup orientovaný na systém.


## Súvisiace


### Súvisiace rozhodnutia

Rozhodnutie o tom, ktorý CI/CD server použiť, musí zahŕňať dôkaz schopnosti pristupovať k tajomstvám.

Budeme sa musieť rozhodnúť, ako tajomstvá spravovať, pokiaľ ide o politiky, rotácie, organizácie atď.


### Súvisiace požiadavky

Tajomstvá budú mať súvisiace požiadavky na súlad, audit a nástup/odchod zamestnancov v HR.


### Súvisiace artefakty

Očakávame, že niektoré tajomstvá exportujeme do premenných prostredia.


### Súvisiace princípy

Ľahko vratné.

Ľahko paralelné, t. j. je ľahké používať rôzne správcovské nástroje hesiel.

Lacné na vyskúšanie, t. j. existuje bezplatná skúšobná verzia a žiadny záväzok.


## Poznámky

Poznámky k hodnoteniu tu. Všetky poznámky sú verejné komentáre na rôznych diskusných fórach o devops.


### Vault by HashiCorp

Vault je presne to, čo tu chcete. 

Nenasadzujte však Vault rovno do produkcie, najprv ho sprevádzkujte v testovacom prostredí, pretože dokumentácia HashiCorp môže byť dosť nedostatočná, aj keď sú ich produkty úžasné.

Veľmi strmá krivka učenia a nie je triviálne ho sprevádzkovať. 

Počiatočné nastavenie je trochu trápenie. Oplatí sa to však a komunita ho podporuje dosť na to, aby ste sa zaobišli.

Príšerná dokumentácia, ale online je veľa návodov od ľudí, ktorí ho nastavovali, a ak z nich zložíte niekoľko, budete mať funkčné nastavenie.

Počiatočné nastavenie vyžadovalo pohrať sa s ich helm chartmi (vault a consul). Hoci technicky môžete použiť mnoho ďalších backendov, naozaj, naozaj to neodporúčam. Backend/consul môže byť maličký, ak nemáte veľa dát na uloženie.

Určite si zvyknite na používanie CLI, pretože GUI je skôr proof-of-concept/reklamný portál pre ich enterprise edíciu.

Fakt, že ho nemôžete jednoducho „naplniť“, je trápenie. Napríklad ak máte 5 polí, musíte ručne pridať každé pole pre každú položku. Takže to nie je tak, že by ste vopred definovali polia pre konkrétnu kategóriu a vyplnili tieto polia pre všetky položky v kategórii, je to skôr „všetko generujete zakaždým znova“, čo je (podľa mňa) poriadna otrava.

Možno sa tiež pozrite na goldfish ako UI nad vaultom. Celkom uľahčuje získať tím na vašu stranu. Majú aj demo. 1. Nastavte consul. 2. Nastavte vault smerujúci na consul. 3. Nastavte goldfish smerujúci na vault. 3. Nastavte nejakú cron úlohu na spúšťanie consul snapshot pre zálohy.



### LastPass

LastPass Teams. Používame ho, má vlastné šablóny, ACL, podľa mňa nič nechýba.

Implementoval som LastPass vo svojej organizácii a dávam mu C+/B-. Najväčším problémom v poslednom čase je nedostatok spoľahlivosti. Za posledných 90 dní bolo niekoľko hodín, keď boli trezory nútene prepnuté do offline režimu. To nie je ideálne pre moju organizáciu, pretože máme doslova 4 000+ hesiel uložených v 20+ zdieľaných priečinkoch. Ako si viete predstaviť, pri takom množstve hesiel sa aspoň niekoľko denne aktualizuje alebo pridá. Máme plán DR pre prípad, že problémy trvajú dlhšie ako hodinu či dve: skript každú noc podpíše a zašifruje CSV výpis trezora, ktorý možno importovať do keepass.

LastPass mal nenahlásené výkyvy zhoršenej služby: prihlásenie „funguje“, ale nenačíta weby, náhodné funkcie v administrátorskom paneli sú pokazené a nezdieľajú sa správne kľúče pre nové zdieľané priečinky najvyššej úrovne. Mám špeciálneho používateľa pre „key push“/zálohovanie, ktorý je v každej skupine. Prihlásenie ako tento používateľ zvyčajne opraví akékoľvek problémy so zdieľaním kľúčov, ale nie keď je služba zhoršená, bez ohľadu na to, čo hovorí stavová stránka...

Pre integráciu to môže byť jednoduché, ak máte správne ACL s modelom najmenších oprávnení, napr. ak má používateľ pri položke alebo priečinku čítanie aj zápis a iba čítanie, dostane iba oprávnenia iba na čítanie. Bohužiaľ ACL v mojej organizácii nie sú najlepšie, takže som nakoniec použil JSON provisioning API a ~500 riadkov Pythonu, pretože závislá povaha našich stoviek ACL sa zle mapuje na model najmenších oprávnení. Nakoniec som získal všetky ACL, v ktorých používateľ bol, a urobil som akési prechádzanie závislostí.

Ak je vaša štruktúra ACL alebo skupín už vybudovaná s ohľadom na model najmenších oprávnení, nástroj na synchronizáciu AD/LDAP pre Windows bude fungovať dobre.

Obráťte sa na ich predajný tím a môžu vám zabezpečiť dlhšiu skúšobnú verziu Enterprise. Uistite sa, že plne rozumiete jej obmedzeniam, skôr než sa rozhodnete. Mali sme dosť rastových bolestí, ale okrem výpadkov alebo zhoršení na strane servera to bolo neuveriteľne plynulé.


### Bitwarden

Bitwarden má okolo seba pekné nástroje (WebUI, CLI, mobilné, desktopové). Dá sa hostovať samostatne a je pomerne ľahký na nastavenie. Pomerne dobrá dokumentácia a nástroj odporúčaný PrivacyTools.


### EnvKey

https://www.envkey.com/ je SaaS. Naozaj jednoduchý na implementáciu, integráciu a správu.

Funkcie:

  * Ochrana API kľúčov a prihlasovacích údajov.

  * Udržiavanie konfigurácie synchronizovanej všade.

  * Inteligentná, end-to-end šifrovaná správa konfigurácie a tajomstiev. 

  * Predchádzanie nezabezpečenému zdieľaniu a rozrastaniu konfigurácie. 

  * Integrácia za pár minút.

Schopnosti:

  * Správa konfigurácie a úrovní prístupu pre všetky vaše aplikácie, prostredia a tímy na jednom mieste.

  * Konfigurácia akéhokoľvek vývojového alebo serverového prostredia iba jednou premennou prostredia.

Klady:

  * Dobrá domovská stránka.

  * Jasná hodnotová ponuka.

  * Vizuálne vynikajúca webová aplikácia.

  * Špičkové ukážkové dáta, napr. Algolia, AWS, Datadog, GitHub, Stripe atď.

  * Hovoril som so zakladateľom 30 minút o spoločnosti, UI atď. Dane znie dobre informovane, úprimne o kladoch/zápornoch a ako životaschopný partner.

  * Spoločnosť je v podstate typická spoločnosť z Y Combinator s 1 zakladateľom. V januári 2018 získala 120 tisíc USD.

  * Dôraz je na dosiahnutí enterprise funkcií, najmä prechod z cloudového hostingu EnvKey buď na on-prem, alebo BYOC.

  * Potenciálna cesta vpred: začať s EnvKey pre jednoduchosť používania a neskôr (alebo paralelne) pridať Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant je open source služba na správu tajomstiev, ktorá poskytuje používateľsky prívetivé ukladanie tajomstiev a prístup k nim bezpečným spôsobom, od vývojárov v Lyfte.

Autentifikácia pomocou KMS: Confidant rieši problém sliepky a vajca pri autentifikácii použitím AWS KMS a IAM, aby IAM roly mohli generovať bezpečné autentifikačné tokeny, ktoré môže Confidant overiť. Confidant spravuje aj KMS granty pre vaše IAM roly, čo IAM rolám umožňuje generovať tokeny použiteľné na autentifikáciu medzi službami alebo na odovzdávanie šifrovaných správ medzi službami.

Šifrovanie verzovaných tajomstiev v pokoji: Confidant ukladá tajomstvá spôsobom iba na pridávanie do DynamoDB, pričom pre každú revíziu každého tajomstva generuje jedinečný KMS dátový kľúč pomocou symetrickej autentifikovanej kryptografie Fernet.

Používateľsky prívetivé webové rozhranie na správu tajomstiev: Confidant poskytuje webové rozhranie AngularJS, ktoré koncovým používateľom umožňuje jednoducho spravovať tajomstvá, priradenia tajomstiev k službám a históriu zmien.


### Devolutions Password Server

https://server.devolutions.net/

Zabezpečte, spravujte a monitorujte prístup k privilegovaným účtom a reláciám.

Komplexný, vysoko zabezpečený trezor hesiel, ktorý vám umožňuje kontrolovať prístup k vašim privilegovaným účtom a zároveň zlepšuje celkovú viditeľnosť siete pre správcov systémov a poskytuje bezproblémový zážitok koncovým používateľom.

Funkcie: centralizovaný organizačný trezor hesiel, súkromný trezor špecifický pre používateľa, správca hesiel, vkladanie prihlasovacích údajov,
integrácia s Active Directory, riadenie prístupu na základe rolí, dvojfaktorová autentifikácia, pripravenosť pre enterprise, obmedzenia podľa IP, možnosti správy, automatický generátor hesiel, prístup z mobilnej aplikácie, história hesiel, prístupové správy, e-mailové upozornenia.

  * podporuje šifrovanie dát

  * podporuje viaceré schémy autentifikácie vrátane LDAP, O365 a lokálnych používateľov S podporou MFA z viacerých zdrojov

  * viaceré repozitáre/trezory s jemne členenými kontrolami prístupu pre viaceré tímy

  * moderné webové UI

  * súkromné trezory prihlasovacích údajov a pripojení pre osobné prihlasovacie údaje/pripojenia

  * mobilné aplikácie pre iOS/Android

  * auditné záznamy pre každý záznam, kto/čo/kedy s voliteľnou výzvou, prečo pristupujú

  * prispôsobiteľné šablóny (hoci natívne podporujú stovky typov pripojení)

  * ešte mnoho ďalších funkcií a hrubý klient pre Windows/Mac (Remote Desktop Manager), s ktorým môžete synchronizovať a ktorý výrazne rozširuje možnosti... pripojenia jedným kliknutím

  * cena nie je až taká zlá - až 15 používateľov stojí 500 USD ročne za password server


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Funkcie on-premise verzie: 

  * Úplná kontrola nad vašimi end-to-end bezpečnostnými systémami a infraštruktúrou

  * Nasadenie softvéru vo vašom on-premise dátovom centre alebo vo vašej vlastnej inštancii virtuálneho súkromného cloudu

  * Splnenie zákonných a regulačných povinností, ktoré vyžadujú, aby všetky dáta a systémy sídlili on premise

Funkcie cloudovej verzie:

  * Model softvér ako služba vám umožňuje zaregistrovať sa a začať hneď

  * Elastická škálovateľnosť s vaším rastom

  * Kontroly a redundanciu zabezpečuje Azure so SLA dostupnosti 99,9 %

Spätná väzba používateľov:

  * Tento produkt sme predtým používali. Dal sa ľahko obísť a pravidlá fungujú len pre inteligentných ľudí. Leniví alebo hlúpi používatelia ho môžu v tímovej oblasti ľahko pokaziť. Ceny sú pri rokovaní s nimi vyjednateľné.

  * Môžete ho spustiť pomocou SQL express a stroja s Win 7. 

  * Lacný.
