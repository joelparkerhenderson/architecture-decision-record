# Záznam architektonického rozhodnutia: editory programového kódu

## Kontext

Editory programového kódu sú pre vývojárov nevyhnutným nástrojom na písanie a úpravu kódu. K dispozícii je mnoho editorov kódu, každý s vlastným súborom funkcií, výhod a nevýhod. Účelom tohto ADR je zdokumentovať architektonické rozhodnutia prijaté pre editory programového kódu.

## Priority

Architektúra editorov programového kódu by mala uprednostňovať nasledujúce:

* **Modularita**: Editor kódu by mal byť navrhnutý modulárne, aby ho vývojári mohli podľa potreby prispôsobovať a rozširovať. To umožňuje flexibilnú architektúru, ktorá sa dokáže prispôsobiť potrebám rôznych vývojárov a tímov.

* **Výkon**: Editor kódu by mal byť výkonný a rýchlo reagovať, aby vývojári mohli pracovať efektívne a nebol ich spomaľovaný nástroj, ktorý používajú.

* **Používateľské rozhranie**: Používateľské rozhranie by malo byť intuitívne a ľahko použiteľné, aby sa vývojári mohli sústrediť na svoj kód a nemuseli zápasiť s editorom.

* **Rozšíriteľnosť**: Editor kódu by mal byť navrhnutý tak, aby umožňoval jednoduché rozšírenie pomocou zásuvných modulov a integrácií tretích strán.

* **Kompatibilita**: Editor kódu by mal byť kompatibilný so širokou škálou programovacích jazykov a technológií, aby bol užitočným nástrojom pre široký okruh vývojárov.

## Rozhodnutie

Na základe týchto priorít by mala byť architektúra editorov programového kódu navrhnutá s nasledujúcimi komponentmi:

* **Jadro**: Tento komponent poskytuje základnú funkcionalitu editora kódu, ako je zvýrazňovanie syntaxe, úprava textu a správa súborov.

* **UI**: Tento komponent poskytuje používateľské rozhranie editora kódu vrátane ponúk, panelov nástrojov a klávesových skratiek.

* **Zásuvné moduly**: Tento komponent umožňuje vývojárom rozšíriť funkcionalitu editora kódu inštaláciou zásuvných modulov tretích strán. Zásuvné moduly môžu poskytovať ďalšie funkcie, ako je dopĺňanie kódu, linting alebo ladenie.

* **Integrácie**: Tento komponent umožňuje editoru kódu integrovať sa s inými nástrojmi a technológiami, ako sú systémy správy verzií, build systémy alebo nástroje na ladenie.

## Zdôvodnenie

Modularita editora kódu umožňuje vývojárom prispôsobiť a rozšíriť ho podľa potreby. To je dôležité, pretože rôzni vývojári a tímy majú rôzne potreby a pracovné postupy a flexibilná architektúra môže tieto rozdiely pojať.

* **Výkon**: kľúčový, pretože vývojári musia byť schopní pracovať efektívne bez toho, aby ich nástroje spomaľovali. Výkonný editor kódu je nevyhnutný pre produktivitu a môže vývojárom pomôcť udržať si sústredenie a koncentráciu.

* **UI**: dôležité, pretože umožňuje vývojárom sústrediť sa na svoj kód a nezápasiť s editorom. To môže viesť k lepšej produktivite a menšej frustrácii vývojárov.

* **Rozšíriteľnosť**: silná, pretože umožňuje prispôsobiť editor kódu rôznym potrebám a pracovným postupom. Zásuvné moduly a integrácie tretích strán môžu poskytovať ďalšie funkcie a schopnosti, ktoré nie sú súčasťou základného editora.

* **Kompatibilita**: cenná, pretože umožňuje používať editor kódu so širokou škálou programovacích jazykov a technológií. To z editora robí užitočnejší nástroj pre široký okruh vývojárov.

Komponenty jadra, zásuvných modulov, integrácií a UI poskytujú jasné oddelenie zodpovedností a umožňujú modulárnu architektúru, ktorú možno ľahko rozširovať a prispôsobovať. Táto architektúra je flexibilná, výkonná a kompatibilná so širokou škálou programovacích jazykov a technológií, vďaka čomu je užitočným nástrojom pre vývojárov.