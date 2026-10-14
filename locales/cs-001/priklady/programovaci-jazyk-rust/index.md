# Záznam architektonického rozhodnutí: programovací jazyk Rust

Číslo rozhodnutí: AR-001

Název rozhodnutí: Přijetí programovacího jazyka Rust

Datum: 1. prosince 2021

Stav: Přijaté

### Popis problému

Jak dále vyvíjíme softwarové aplikace, pozorujeme, že je stále obtížnější zmírňovat potenciální bezpečnostní zranitelnosti a předcházet chybám za běhu. U stávajících programovacích jazyků, jako jsou C a C++, se stále setkáváme s problémy, jako jsou přetečení bufferu, úniky paměti a nedefinované chování vedoucí k pádům aplikací. Potřebujeme programovací jazyk, který poskytuje záruky bezpečnosti paměti a je dostatečně efektivní pro podporu aplikací kritických z hlediska výkonu.

### Úvahy

Několik programovacích jazyků je navrženo tak, aby řešily stávající problémy. Mezi nimi získal programovací jazyk Rust značnou pozornost vývojářské komunity díky svým jedinečným konstrukčním vlastnostem. Úvahy zahrnují;

1. Bezpečnost paměti a zabezpečení

2. Výkon a efektivita

3. Podpora komunity a míra přijetí

4. Křivka učení

5. Nástroje a ekosystém

6. Kompatibilita se stávajícími softwarovými systémy.

### Omezení

Přijetí nového programovacího jazyka vyžaduje přeškolení vývojářů, což zabere čas a zdroje. Integrace jazyka do stávajícího vývojového pracovního postupu může být výzvou. Musíme zajistit kompatibilitu se stávajícími systémy a vyhnout se zásadním změnám, abychom zachovali kontinuitu.

### Implementace

1. Náš vývojový tým projde školením, aby se s programovacím jazykem Rust naučil a seznámil.

2. Vytvoříme zkušebně nový projekt v Rustu, abychom vyhodnotili jeho kompatibilitu a vhodnost pro naše vývojové účely.

3. Postupně migrujeme stávající systémy napsané v C a C++ do Rustu.

4. Budeme spolupracovat s komunitou Rustu na prozkoumání dostupných nástrojů a knihoven, které mohou zlepšit náš vývojový pracovní postup.

5. Budeme sledovat výkon Rustu a pravidelně ho porovnávat s výkonem stávajících programovacích jazyků.

6. Přijmeme dlouhodobý přístup, který vyvažuje náklady na školení, integraci a možné přínosy používání Rustu.

### Zdůvodnění

Přijali jsme Rust kvůli jeho jedinečným vlastnostem navrženým tak, aby poskytovaly záruky bezpečnosti paměti a zabezpečení při zachování výkonu a efektivity. Robustní typový systém Rustu, borrow checker a koncepty bezpečnosti paměti ho činí vysoce vhodným pro vývoj aplikací kritických z hlediska výkonu a bezpečnosti. Rust má navíc významnou komunitu vývojářů, což nám umožňuje přístup k široké škále nástrojů, knihoven a ekosystému, které podporují náš vývojový pracovní postup. Přestože Rust přichází s křivkou učení, věříme, že přínosy přijetí Rustu převažují nad náklady a poskytují vynikající příležitost pro další růst a inovace.

### Důsledky

1. Přijetí Rustu bude vyžadovat významnou investici času a zdrojů do školení vývojářů a integrace jazyka do stávajícího vývojového pracovního postupu.

2. Přijetí Rustu může způsobit určitou míru problémů s kompatibilitou se stávajícími systémy, což bude vyžadovat refaktoring a úpravy.

3. Přijetí Rustu může zvýšit počet vývojářů, kteří mohou přispívat do našeho projektu, tím, že přiláká vývojáře Rustu, kteří chtějí pracovat na zajímavých projektech.

4. Přijetí by mohlo vést ke zlepšení výkonu, efektivity a bezpečnosti ve srovnání se stávajícími jazyky.

5. Přijetí Rustu konečně přináší potenciální přínos v podobě snížení bezpečnostních zranitelností v našich aplikacích.
   
<h6>Zdroj: tuto stránku vygeneroval ChatGPT a poté byla upravena pro přehlednost a formát.</h6>