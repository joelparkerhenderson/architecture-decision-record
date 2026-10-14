# Proces záznamů architektonických rozhodnutí v AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Záznam architektonického rozhodnutí (ADR) je dokument popisující volbu, kterou tým činí ohledně významného aspektu softwarové architektury, kterou plánuje vybudovat. Každé ADR popisuje architektonické rozhodnutí, jeho kontext a jeho důsledky. ADR mají stavy, a proto sledují životní cyklus. Příklad ADR najdete v příloze.

Výstupem procesu ADR je soubor záznamů architektonických rozhodnutí. Tento soubor vytváří protokol rozhodnutí. Protokol rozhodnutí poskytuje kontext projektu i podrobné informace o implementaci a návrhu. Členové projektu prolétnou nadpisy každého ADR, aby získali přehled o kontextu projektu. ADR čtou, aby se ponořili do implementací a návrhových voleb projektu.

Jakmile tým ADR přijme, stane se neměnným. Pokud nové poznatky vyžadují jiné rozhodnutí, tým navrhne nové ADR. Když tým nové ADR přijme, nahradí předchozí ADR.

## Rozsah procesu ADR

Členové projektu by měli vytvořit ADR pro každé architektonicky významné rozhodnutí, které ovlivňuje softwarový projekt nebo produkt, včetně následujících (Richards a Ford 2020):

* Struktura (například vzory jako mikroslužby)

* Nefunkční požadavky (bezpečnost, vysoká dostupnost a odolnost vůči chybám)

* Závislosti (vazba komponent)

* Rozhraní (API a publikované smlouvy)

* Techniky konstrukce (knihovny, frameworky, nástroje a procesy)

* Funkční a nefunkční požadavky jsou nejčastějšími vstupy procesu ADR.


## Obsah ADR

Když tým identifikuje potřebu ADR, člen týmu začne psát ADR na základě šablony platné pro celý projekt. (Příklady šablon najdete v organizaci ADR na GitHubu.) Šablona zjednodušuje vytváření ADR a zajišťuje, že ADR zachycuje všechny relevantní informace. Každé ADR by mělo alespoň definovat kontext rozhodnutí, samotné rozhodnutí a důsledky rozhodnutí pro projekt a jeho dodávky. (Příklady těchto sekcí najdete v příloze.) Jedním z nejsilnějších aspektů struktury ADR je, že se zaměřuje na důvod rozhodnutí, nikoli na to, jak ho tým implementoval. Pochopení toho, proč tým rozhodnutí učinil, usnadňuje ostatním členům týmu jeho přijetí a brání tomu, aby ho v budoucnu zrušili jiní architekti, kteří se na rozhodovacím procesu nepodíleli.


## Proces přijímání ADR

Každý člen týmu může ADR vytvořit, ale tým by měl stanovit definici vlastnictví ADR. Každý autor, který je vlastníkem ADR, by měl aktivně udržovat a komunikovat obsah ADR. Aby se toto vlastnictví upřesnilo, tento průvodce v následujících sekcích označuje autory ADR jako vlastníky ADR. Ostatní členové týmu mohou k ADR vždy přispívat. Pokud se obsah ADR změní dříve, než ho tým přijme, vlastník by měl tyto změny schválit.

Poté, co tým identifikuje architektonické rozhodnutí a jeho vlastníka, vlastník ADR na začátku procesu předloží ADR ve stavu **Proposed** (Navrhované). ADR ve stavu Proposed jsou připravena k revizi.

Poté vlastník ADR zahájí proces revize ADR. Cílem procesu revize ADR je rozhodnout, zda tým ADR přijme, určí, že vyžaduje přepracování, nebo ho zamítne. ADR přezkoumává projektový tým včetně vlastníka. Revizní schůzka by měla začít vyhrazeným časovým úsekem na přečtení ADR. V průměru by mělo stačit 10 až 15 minut. Během této doby každý člen týmu čte dokument a přidává komentáře a otázky, aby označil nejasná témata. Po fázi revize vlastník ADR přečte a probere každý komentář s týmem.

Pokud tým najde akční body ke zlepšení ADR, stav ADR zůstává **Proposed**. Vlastník ADR akce formuluje a ve spolupráci s týmem ke každé akci přidá řešitele. Každý člen týmu může přispět k akčním bodům a vyřešit je. Je odpovědností vlastníka ADR přeplánovat proces revize.

Tým se také může rozhodnout ADR zamítnout. V takovém případě vlastník ADR přidá důvod zamítnutí, aby předešel budoucím diskusím na stejné téma. Vlastník změní stav ADR na **Rejected** (Zamítnuté).

Pokud tým ADR schválí, vlastník přidá časové razítko, verzi a seznam zainteresovaných stran. Poté vlastník aktualizuje stav na **Accepted** (Přijaté).

ADR a protokol rozhodnutí, který vytvářejí, představují rozhodnutí učiněná týmem a poskytují historii všech rozhodnutí. Tým používá ADR jako referenci během revizí kódu a architektury, kdykoli je to možné. Kromě provádění revizí kódu, návrhových úkolů a implementačních úkolů by členové týmu měli konzultovat ADR pro strategická rozhodnutí o produktu.

Jako dobrá praxe by každá softwarová změna měla projít vzájemnou revizí a vyžadovat alespoň jedno schválení. Během revize kódu může recenzent najít změny, které porušují jedno nebo více ADR. V takovém případě recenzent požádá autora změny kódu o aktualizaci kódu a sdílí odkaz na ADR. Když autor kód aktualizuje, schválí ho kolegové recenzenti a sloučí se do hlavní kódové základny.


## Proces revize ADR

Tým by měl s ADR po jejich přijetí nebo zamítnutí zacházet jako s neměnnými dokumenty. Změna stávajícího ADR vyžaduje vytvoření nového ADR, zavedení procesu revize nového ADR a jeho schválení. Pokud tým nové ADR schválí, vlastník by měl změnit stav starého ADR na **Superseded** (Nahrazené). 
