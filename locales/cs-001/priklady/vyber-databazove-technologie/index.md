# Záznam architektonického rozhodnutí: výběr databázové technologie

## Stav

Přijaté

## Kontext

Navrhujeme novou aplikaci, která vyžaduje ukládání a načítání dat škálovatelným a výkonným způsobem. Identifikovali jsme tři typy databázových technologií, které se běžně používají: relační databáze, dokumentové databáze a databáze událostí.

Relační databáze ukládají data do tabulek s pevnými schématy a vynucují přísná omezení integrity dat. Hodí se pro aplikace, které vyžadují složité vztahy mezi daty a transakce. Příklady jsou MySQL, PostgreSQL a Oracle.

Dokumentové databáze ukládají data do dokumentů podobných JSON a jsou bez schématu. Hodí se pro aplikace, které vyžadují flexibilní datové modely a horizontální škálování. Příklady jsou MongoDB, Couchbase a Amazon DynamoDB.

Databáze událostí ukládají data jako řadu událostí a zachycují každou změnu dat. Hodí se pro aplikace, které vyžadují auditování, event sourcing a složité zpracování dat. Příklady jsou Apache Kafka, Apache Pulsar a AWS Kinesis.

## Rozhodnutí

Po pečlivém vyhodnocení požadavků a omezení naší aplikace jsme se rozhodli použít dokumentovou databázi.

## Odůvodnění

Dokumentovou databázi jsme zvolili, protože:

1. Naše aplikace vyžaduje flexibilní datový model, který se může v čase vyvíjet. Dokumentové databáze nám umožňují ukládat data ve formátu bez schématu, což znamená, že můžeme přidávat nová pole nebo měnit strukturu stávajících dokumentů, aniž bychom museli upravovat schéma databáze.

2. Naše aplikace se musí horizontálně škálovat, aby zvládla velké objemy dat a provozu. Dokumentové databáze poskytují vestavěnou podporu pro sharding a replikaci, což nám umožňuje rozdělit data mezi více serverů a zvládnout vysokou propustnost čtení a zápisu.

3. Naše aplikace vyžaduje rychlé a efektivní načítání dat. Dokumentové databáze poskytují výkonné možnosti indexování a dotazování, které nám umožňují načítat data rychle a efektivně.

4. Naše aplikace nevyžaduje složité transakce ani vztahy mezi daty. Přestože relační databáze vynikají ve vynucování omezení integrity dat a zpracování složitých transakcí, naše aplikace takové požadavky nemá. Dokumentové databáze mohou pro náš případ použití poskytnout dostatečné záruky konzistence a trvanlivosti.

## Důsledky

Volbou dokumentové databáze budeme muset investovat do učení a pochopení konkrétní technologie, kterou zvolíme. Kromě toho budeme muset zajistit, aby datový model naší aplikace dobře odpovídal datovému modelu dokumentové databáze, abychom maximalizovali výkon a škálovatelnost.

Věříme však, že přínosy používání dokumentové databáze převažují nad náklady a že je to nejlepší shoda s požadavky a omezeními naší aplikace.
