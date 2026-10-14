
### Kdo může vytvořit ADR?

Zvažte oblasti jako konkrétní osoby, konkrétní role, konkrétní týmy nebo konkrétní oddělení; zvažte také, zda existují osoby, role, týmy nebo oddělení, které mohou ADR zadat, tedy požádat o ADR, které napíše někdo jiný. 

Příklad odpovědi: Každá osoba v naší organizaci, která si přečetla stránku README o záznamech architektonických rozhodnutí, může navrhnout ADR, tedy začít ho psát a sdílet ho s týmem.

### Co ospravedlňuje zahájení ADR?

Zvažte oblasti jako způsoby práce týmů vaší organizace, strukturu vašeho softwarového systému, koordinaci mezi týmy, dlouhodobou udržovatelnost, externí rozhraní, komu chcete prospět a podobně. 

Příklad odpovědi: Chceme vytvořit ADR, když chceme, aby budoucí vývojáři pochopili „proč“ děláme to, co děláme.

### Co ospravedlňuje nezahájení ADR?

Zvažte oblasti jako rozhodnutí, která nejsou o architektuře nebo jsou drobná, například s minimálním rizikem, samostatná nebo týkající se jednoho vývojáře, nebo jsou již plně pokryta jinde, například standardy, zásadami nebo dokumentací, nebo jsou dočasná, například náhradní řešení, ověření konceptu nebo experimenty. 

Příklad odpovědi: ADR vynecháme, když je rozhodnutí omezené rozsahem, časem, rizikem i náklady nebo je již pokryto jinde.

### Jaký je životní cyklus ADR?

Zvažte oblasti jako proces vytváření, proces zkoumání, proces rozhodování, proces implementace a proces vyřazování. Zvažte, jak sledovat životní cyklus ADR v čase, například jak přesunout ADR z jednoho stavu do dalšího a jak to sdělit zainteresovaným stranám. 

Příklad odpovědi: Chceme, aby ADR mělo pět fází životního cyklu: Zahájení → Zkoumání → Hodnocení → Implementace → Údržba → Vyřazení.

### Jaká jsou kritéria pro kroky životního cyklu ADR?

Zvažte oblasti jako kritéria přijetí ADR, tedy jak poznáte, že je dost dobré, aby postoupilo z jednoho kroku životního cyklu do dalšího? Je problém jasně formulován? Byly zváženy alternativy? Jsou kompromisy dostatečně pochopeny a zdokumentovány?
Je k dispozici veškerý relevantní kontext? Jsou zapojeny všechny relevantní zainteresované strany? Byla zapracována veškerá zpětná vazba? 

Příklad odpovědi: Chceme, aby o ADR hlasovaly zainteresované strany, když aktivní tým 1) dokončil svůj výzkum, 2) dokončil své hodnocení, 3) zveřejnil návrh ADR zainteresovaným stranám s žádostí o připomínky a lhůtou jednoho týdne, 4) všechny připomínky zainteresovaných stran byly zapracovány a vyřešeny.

### Jaké role a odpovědnosti souvisejí s ADR?

Zvažte role jako navrhovatel, výzkumník, hodnotitel, recenzent, schvalovatel, správce a podobně. Zvažte odpovědnosti jako komunikace se zainteresovanými stranami, zajištění splnění očekávání, sdílení na webu nebo intranetu a pravidelná revize práce, zejména když nastanou relevantní změny.

Příklad odpovědi: Chceme, aby každé ADR mělo vždy primární kontaktní osobu, sekundární kontaktní osobu a odpovědný tým; ti odpovídají za komunikaci, publikace, údržbu, pravidelnou revizi alespoň jednou ročně a případné vyřazení podle potřeby.

### Jak souvisí správa a řízení (governance) s ADR?

Zvažte oblasti jako způsoby práce vaší organizace, případné zvláštní potřeby souladu, například právní aspekty nebo aspekty lidských zdrojů, a jak chcete zacházet s konsensem, konfliktem a eskalací. Existují oblasti, osoby nebo týmy, které mohou mít na ADR větší vliv než ostatní, například ho mohou schválit, hlasovat o něm nebo ho vetovat?

Příklad odpovědi: Řízení ADR probíhá v tomto pořadí priority: generální ředitel (CEO), technický ředitel (CTO), právní ředitel (CLO), tým, který ADR implementuje, odborníci v týmu, kteří o architektonickém rozhodnutí vědí nejvíce. Nikdo jiný řízení nemá, pokud to není popsáno v ADR. 

### Jaké principy souvisejí s ADR?

Zvažte oblasti jako způsoby práce vaší organizace, které zahrnují rychlý versus pomalý postup, konsensus versus konflikt při rozhodování, preference rizika versus preference bezpečí, veřejná diskuse versus soukromá diskuse a podobně.

Příklad odpovědi: Používáme principy vedení: sklon k akci, nesouhlas a závazek (disagree-and-commit), odhady na 70 % jsou dost dobré pro snadno vratná a snadno izolovatelná rozhodnutí a veřejné způsoby práce s výjimkou důvěrných informací popsaných v dohodě o mlčenlivosti naší organizace.
