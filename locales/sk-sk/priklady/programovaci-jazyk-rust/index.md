# Záznam architektonického rozhodnutia: programovací jazyk Rust

Číslo rozhodnutia: AR-001

Názov rozhodnutia: Prijatie programovacieho jazyka Rust

Dátum: 1. decembra 2021

Stav: Prijaté

### Opis problému

Ako pokračujeme vo vývoji softvérových aplikácií, pozorujeme, že je čoraz náročnejšie zmierňovať potenciálne bezpečnostné zraniteľnosti a predchádzať chybám za behu. Pri existujúcich programovacích jazykoch, ako sú C a C++, sa naďalej stretávame s problémami ako pretečenie bufferu, úniky pamäte a nedefinované správanie vedúce k pádom aplikácií. Potrebujeme programovací jazyk, ktorý poskytuje záruky bezpečnosti pamäte a je dostatočne efektívny na podporu aplikácií kritických z hľadiska výkonu.

### Úvahy

Niekoľko programovacích jazykov je navrhnutých tak, aby riešili existujúce problémy. Medzi nimi získal programovací jazyk Rust značnú pozornosť komunity vývojárov vďaka svojim jedinečným konštrukčným vlastnostiam. Úvahy zahŕňajú;

1. Bezpečnosť pamäte a zabezpečenie

2. Výkon a efektivita

3. Podpora komunity a miera prijatia

4. Krivka učenia

5. Nástroje a ekosystém

6. Kompatibilita s existujúcimi softvérovými systémami.

### Obmedzenia

Prijatie nového programovacieho jazyka vyžaduje preškolenie vývojárov, čo zaberie čas a zdroje. Integrácia jazyka do existujúceho vývojového pracovného postupu môže byť výzvou. Musíme zabezpečiť kompatibilitu s existujúcimi systémami a vyhnúť sa zásadným zmenám, aby sme zachovali kontinuitu.

### Implementácia

1. Náš vývojový tím absolvuje školenie, aby sa s programovacím jazykom Rust naučil a oboznámil.

2. Vytvoríme skúšobne nový projekt v Ruste, aby sme vyhodnotili jeho kompatibilitu a vhodnosť pre naše vývojové účely.

3. Postupne migrujeme existujúce systémy napísané v C a C++ do Rustu.

4. Budeme spolupracovať s komunitou Rustu na preskúmaní dostupných nástrojov a knižníc, ktoré môžu zlepšiť náš vývojový pracovný postup.

5. Budeme sledovať výkon Rustu a pravidelne ho porovnávať s výkonom existujúcich programovacích jazykov.

6. Prijmeme dlhodobý prístup, ktorý vyvažuje náklady na školenie, integráciu a potenciálne prínosy používania Rustu.

### Zdôvodnenie

Prijali sme Rust kvôli jeho jedinečným vlastnostiam navrhnutým tak, aby poskytovali záruky bezpečnosti pamäte a zabezpečenia pri zachovaní výkonu a efektivity. Robustný typový systém Rustu, borrow checker a koncepty bezpečnosti pamäte ho robia veľmi vhodným na vývoj aplikácií kritických z hľadiska výkonu a bezpečnosti. Rust má navyše významnú komunitu vývojárov, čo nám umožňuje prístup k širokej škále nástrojov, knižníc a ekosystému, ktoré podporujú náš vývojový pracovný postup. Hoci Rust prichádza s krivkou učenia, veríme, že prínosy prijatia Rustu prevažujú nad nákladmi a poskytujú výbornú príležitosť na ďalší rast a inovácie.

### Dôsledky

1. Prijatie Rustu bude vyžadovať významnú investíciu času a zdrojov do školenia vývojárov a integrácie jazyka do existujúceho vývojového pracovného postupu.

2. Prijatie Rustu môže spôsobiť určitý stupeň problémov s kompatibilitou s existujúcimi systémami, čo si vyžiada refaktoring a úpravy.

3. Prijatie Rustu môže zvýšiť počet vývojárov, ktorí môžu prispievať do nášho projektu, tým, že pritiahne vývojárov Rustu, ktorí chcú pracovať na zaujímavých projektoch.

4. Prijatie by mohlo viesť k zlepšenému výkonu, efektivite a bezpečnosti v porovnaní s existujúcimi jazykmi.

5. Napokon prijatie Rustu prináša potenciálny prínos v podobe zníženia bezpečnostných zraniteľností v našich aplikáciách.
   
<h6>Zdroj: túto stránku vygeneroval ChatGPT a potom bola upravená kvôli prehľadnosti a formátu.</h6>