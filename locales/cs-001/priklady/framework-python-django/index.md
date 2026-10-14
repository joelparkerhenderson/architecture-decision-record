# Záznam architektonického rozhodnutí pro framework Python Django

Datum rozhodnutí: 2021-07-15

Stav: Přijaté

## Kontext

Naše organizace plánuje vyvinout webovou aplikaci, která spravuje data zákazníků. Jako programovací jazyk jsme zvolili Python a jako webový framework pro vývoj aplikace zvažujeme Django.

## Rozhodnutí

Rozhodli jsme se pro vývoj webové aplikace použít webový framework Django. Django poskytuje robustní sadu nástrojů a funkcí pro rychlé a efektivní vytváření webových aplikací. 

## Faktory

Mezi faktory, které naše rozhodnutí ovlivnily, patří:

1. Objektově-relační mapování (ORM): Django má vestavěné ORM, které nám umožňuje pracovat s databází bez psaní SQL dotazů. Díky tomu je snazší aplikaci vyvíjet a dlouhodobě udržovat.

2. Framework MVC: Django se řídí architekturou Model-View-Controller (MVC), takže je snazší oddělit obchodní logiku a prezentační vrstvu aplikace.

3. Škálovatelnost: Django je známé svými schopnostmi škálování, což z něj činí vynikající volbu pro vývoj rozsáhlých aplikací.

4. Bezpečnost: Django má vestavěné bezpečnostní funkce, například ochranu proti běžným webovým útokům, jako je cross-site scripting (XSS) a SQL injection.

5. Podpora komunity: Django má velkou a aktivní komunitu, která poskytuje podporu a přispívá k vývoji frameworku.

## Zvažované alternativy

Zvažovali jsme další webové frameworky, například Flask a Pyramid. Zjistili jsme však, že Django je vyspělejší a zavedenější framework s robustní sadou funkcí.

Diskutovali jsme také o vývoji aplikace bez webového frameworku s použitím knihoven jako SQLAlchemy a Flask-RESTful. Zjistili jsme však, že Django nabízí širší funkcionalitu, takže je lepší volbou pro kompletní webovou aplikaci.

## Důsledky

Přijetí Djanga povede k následujícím důsledkům:

1. Snazší vývoj a údržba aplikace díky vestavěným nástrojům a funkcím Djanga.

2. Oddělení obchodní logiky a prezentační vrstvy, což vede k organizovanějšímu a snáze udržovatelnému kódu.

3. Škálovatelnost a robustnost aplikace.

4. Vestavěné bezpečnostní funkce, které pomáhají chránit aplikaci před běžnými webovými útoky.

5. Přístup k velké a aktivní komunitě pro podporu.

Chápeme, že Django má strmější křivku učení než jiné frameworky, ale považujeme ji za investici, která se pro dlouhodobé přínosy vyplatí.

## Závěr

Na základě zvažovaných faktorů jsme se rozhodli pro vývoj webové aplikace použít webový framework Django. Věříme, že funkce, podpora komunity a schopnosti škálování Djanga z něj činí nejlepší volbu pro vytvoření kompletní webové aplikace. Vývojáře proškolíme v používání Djanga, aby byl framework používán efektivně a účinně.