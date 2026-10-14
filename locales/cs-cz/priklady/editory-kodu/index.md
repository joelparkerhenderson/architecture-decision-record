# Záznam architektonického rozhodnutí: editory programového kódu

## Kontext

Editory programového kódu jsou pro vývojáře nezbytným nástrojem k psaní a úpravám kódu. K dispozici je mnoho editorů kódu, každý s vlastní sadou funkcí, výhod a nevýhod. Účelem tohoto ADR je zdokumentovat architektonická rozhodnutí učiněná pro editory programového kódu.

## Priority

Architektura editorů programového kódu by měla upřednostňovat následující:

* **Modularita**: Editor kódu by měl být navržen modulárně, aby ho vývojáři mohli podle potřeby přizpůsobit a rozšířit. To umožňuje flexibilní architekturu, která se dokáže přizpůsobit potřebám různých vývojářů a týmů.

* **Výkon**: Editor kódu by měl být výkonný a pohotový, aby vývojáři mohli pracovat efektivně a nebyli zpomalováni nástrojem, který používají.

* **Uživatelské rozhraní**: Uživatelské rozhraní by mělo být intuitivní a snadno použitelné, aby se vývojáři mohli soustředit na svůj kód a nemuseli bojovat s editorem.

* **Rozšiřitelnost**: Editor kódu by měl být navržen tak, aby umožňoval snadné rozšíření pomocí zásuvných modulů a integrací třetích stran.

* **Kompatibilita**: Editor kódu by měl být kompatibilní se širokou škálou programovacích jazyků a technologií, aby byl užitečným nástrojem pro široký okruh vývojářů.

## Rozhodnutí

Na základě těchto priorit by měla být architektura editorů programového kódu navržena s následujícími komponentami:

* **Jádro**: Tato komponenta poskytuje základní funkce editoru kódu, jako je zvýraznění syntaxe, úprava textu a správa souborů.

* **UI**: Tato komponenta poskytuje uživatelské rozhraní editoru kódu, včetně nabídek, panelů nástrojů a klávesových zkratek.

* **Zásuvné moduly**: Tato komponenta umožňuje vývojářům rozšířit funkčnost editoru kódu instalací zásuvných modulů třetích stran. Zásuvné moduly mohou poskytovat další funkce, například doplňování kódu, linting nebo ladění.

* **Integrace**: Tato komponenta umožňuje editoru kódu integrovat se s dalšími nástroji a technologiemi, například se systémy správy verzí, systémy sestavení nebo nástroji pro ladění.

## Zdůvodnění

Modularita editoru kódu umožňuje vývojářům přizpůsobit a rozšířit ho podle potřeby. To je důležité, protože různí vývojáři a týmy mají různé potřeby a pracovní postupy a flexibilní architektura může tyto rozdíly pojmout.

* **Výkon**: zásadní, protože vývojáři musí být schopni pracovat efektivně a nebýt zpomalováni svými nástroji. Výkonný editor kódu je nezbytný pro produktivitu a může vývojářům pomoci udržet soustředění a koncentraci.

* **UI**: důležité, protože umožňuje vývojářům soustředit se na svůj kód a nebojovat s editorem. To může vést k vyšší produktivitě a menší frustraci vývojářů.

* **Rozšiřitelnost**: silná, protože umožňuje přizpůsobit editor kódu různým potřebám a pracovním postupům. Zásuvné moduly a integrace třetích stran mohou poskytovat další funkce a schopnosti, které nejsou součástí základního editoru.

* **Kompatibilita**: cenná, protože umožňuje používat editor kódu se širokou škálou programovacích jazyků a technologií. Díky tomu je editor užitečnějším nástrojem pro široký okruh vývojářů.

Komponenty jádra, zásuvných modulů, integrací a UI poskytují jasné oddělení odpovědností a umožňují modulární architekturu, kterou lze snadno rozšiřovat a přizpůsobovat. Tato architektura je flexibilní, výkonná a kompatibilní se širokou škálou programovacích jazyků a technologií, takže je užitečným nástrojem pro vývojáře.