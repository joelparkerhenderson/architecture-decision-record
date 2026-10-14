# Monorepo nebo multirepo

Obsah:

* [Shrnutí](#shrnutí)
  * [Problém](#problém)
  * [Rozhodnutí](#rozhodnutí)
  * [Stav](#stav)
* [Podrobnosti](#podrobnosti)
  * [Předpoklady](#předpoklady)
  * [Omezení](#omezení)
  * [Stanoviska](#stanoviska)
  * [Argument](#argument)
  * [Důsledky](#důsledky)
* [Související](#související)
  * [Související rozhodnutí](#související-rozhodnutí)
  * [Související požadavky](#související-požadavky)
  * [Související artefakty](#související-artefakty)
  * [Související principy](#související-principy)
* [Poznámky](#poznámky)


## Shrnutí


### Problém

Náš projekt zahrnuje vývoj tří hlavních kategorií softwaru:

  * Front-endová GUI
  * Middlewarové služby
  * Back-endové servery

Při vývoji je naším systémem správy zdrojového kódu (SCM) a správy verzí (VCS) git.

Musíme zvolit, jak použijeme git k organizaci našeho kódu.

Zásadní volbou je organizovat jako „monorepo“, „polyrepo“ nebo „hybrid“:

  * Monorepo znamená, že všechny části dáme do jednoho velkého repozitáře
  * Polyrepo znamená, že každou část dáme do vlastního repozitáře
  * Hybrid znamená určitou kombinaci monorepa a polyrepa

Více viz https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Rozhodnutí

Monorepo, když je organizace/tým/projekt relativně malý a rychlá iterace má vyšší prioritu než udržení stability.

Polyrepo, když je organizace/tým/projekt relativně velký a udržení stability má vyšší prioritu než rychlá iterace.


### Stav

Rozhodnuto. Jsme otevřeni k přehodnocení, pokud a když budou k dispozici nové nástroje pro správu monorepozitářů a/nebo polyrepozitářů.


## Podrobnosti


### Předpoklady

Veškerý kód, který vyvíjíme, je určen pro nabídky jedné organizace, nikoli pro širokou veřejnost. Tj. Broker-Dealer nemá v úmyslu mít nic jako dobrovolné vývojáře z široké veřejnosti.


### Omezení

Omezení jsou dobře zdokumentována na https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Stanoviska

Zvažovali jsme monorepa ve stylu Googlu, Facebooku atd. Domníváme se, že jakékoli problémy se škálováním monorepa jsou tak vzdálené v budoucnosti, že než je budeme potřebovat, budeme moci využít stejné postupy jako Google a Facebook.

Zvažovali jsme polyrepa ve stylu typických open source projektů v Gitu, jako Google Android, Facebook React atd. Domníváme se, že jsou nejlepší volbou pro účast široké veřejnosti (např. kdokoli na světě může pracovat na kódu) a individuální dostupnost (např. projekt se používá samostatně, bez jakýchkoli dalších částí).


### Argument

Když je organizace/tým/projekt relativně malý, volíme monorepo, protože rychlá iterace má výrazně vyšší prioritu než udržení stability

Když je organizace/tým/projekt relativně velký, volíme polyrepo, protože udržení stability má výrazně vyšší prioritu než rychlá iterace.


### Důsledky

Pokud existuje stávající pipeline pro CI+CD, možná ji bude nutné upravit pro testování více projektů v jednom repozitáři.

CI+CD může trvat déle při úplném sestavení monorepa, protože CI+CD může sestavovat všechny projekty v monorepu.

Pokud organizace/tým/projekt roste, monorepo bude mít problémy se škálováním.

Problémy se škálováním monorepa mohou činit přechod na polyrepo stále cennějším.

Přechod z monorepa na polyrepo je významný devops úkol a bude třeba ho naplánovat, řídit a naprogramovat.


## Související


### Související rozhodnutí

Vytvoříme rozhodnutí pro související nástroje pro správu monorepozitářů (např. Google Bazel) a polyrepozitářů (např. Lyft Refactorator).


### Související požadavky

Potřebujeme vyvinout pipeline CI+CD tak, aby dobře fungovala s gitem.


### Související artefakty

Očekáváme, že organizace repozitářů bude mít související artefakty pro provisioning, správu konfigurace, testování a podobné devops oblasti. 


### Související principy

Snadno vratné. Pokud monorepo v praxi nefunguje nebo ho vedení nechce, je jednoduché přejít na polyrepo.

Posedlost zákazníkem. Ceníme si toho, že projekt dostaneme do rukou zákazníků, a věříme, že monorepo nás tam dostane rychleji než polyrepo a také nám pomůže rychleji iterovat.

Myslete ve velkém. Google a Facebook jsou velmi silnými zastánci monorepozitářů před polyrepozitáři, protože všechny základní nabídky lze vyvíjet/testovat/nasazovat společně.


## Poznámky

Sem přidejte jakékoli poznámky.
