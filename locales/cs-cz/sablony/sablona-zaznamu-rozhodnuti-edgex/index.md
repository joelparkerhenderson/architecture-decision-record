# Šablona záznamu architektonického rozhodnutí (ADR) <!-- Replace with ADR title -->

Toto je šablona pro ADR EdgeX Foundry.

Zdroj: https://docs.edgexfoundry.org/2.3/design/adr/template/


### Předkladatelé

Uveďte předkladatele ADR.

Formát:

- Jméno (Organizace)


## Protokol změn

Uveďte změny dokumentu, včetně stavu, data a URL PR.

Stav je jeden z: pending (nevyřízené), approved (schválené), amended (změněné), deprecated (zastaralé).

Datum je řetězec ISO 8601 (RRRR-MM-DD).

PR je pull request, který změnu předložil, včetně informací jako rozdíly, přispěvatelé a recenzenti.

Formát:

- \[Stav ADR, např. approved, amended atd.\]\(URL pull requestu\) RRRR-MM-DD


## Odkazované případy užití

Uveďte všechny relevantní dokumenty případů užití / požadavků.

ADR vyžaduje alespoň jeden relevantní, schválený případ užití.

Formát:

- \[Název případu užití\]\(URL\)

Přidejte vysvětlení, pokud ADR neřeší všechny požadavky případu užití.


## Kontext

Popište:

- v čem je návrh architektonicky významný — ospravedlňující ADR (oproti prostému problému a PR, který problém opravuje)

- přístup k návrhu na vysoké úrovni (podrobnosti jsou popsány v navrhovaném návrhu níže)


## Navrhovaný návrh

Podrobnosti návrhu (pokud možno bez zacházení do implementace).

Osnova:

- služby/moduly, které budou dotčeny (změněny)

- nové služby/moduly k přidání

- dopad na model a DTO (změny/přidání/odstranění)

- dopad na API (změny/přidání/odstranění)

- dopad na obecnou konfiguraci (zavedení nových sekcí, změny/přidání/odstranění)

- dopad na devops


## Úvahy

Zdokumentujte alternativy, obavy, vedlejší nebo související otázky a dotazy, které vznikly v diskusi o ADR. 

Uveďte, zda/jak byly vyřešeny nebo zmírněny.


## Rozhodnutí

Zdokumentujte jakýkoli dohodnutý důležitý implementační detail, výhrady, budoucí úvahy a zbývající nebo odložené návrhové otázky.

Zdokumentujte jakoukoli část požadavků, kterou navrhovaný návrh nesplňuje.


## Další související ADR

Uveďte jakákoli relevantní ADR — například návrhové rozhodnutí pro dílčí komponentu funkce, návrh zastaralý v důsledku tohoto návrhu atd. 

Formát:

- \[Název ADR\]\(URL\) - Relevance


## Reference

Uveďte další reference.

Formát:

- \[Název\]\(URL\)

