# Záznam architektonického rozhodnutí: snake_case nebo camelCase pro REST API?

Rozhodnutí: Pro koncové body REST API se bude používat konvence pojmenování snake_case

Stav: Přijaté

## Kontext

V konvencích pojmenování pro REST API existují dva oblíbené formáty: snake_case a camelCase. Formát snake_case je takový, kde je každé slovo v názvu odděleno podtržítky, zatímco camelCase je takový, kde je první slovo názvu psáno malými písmeny a další slova mají první písmeno velké. Toto rozhodnutí určí, která konvence pojmenování se má pro REST API použít.

## Hnací síly rozhodnutí

- Konzistence se stávajícími konvencemi pojmenování v projektu

- Čitelnost a srozumitelnost pro každého, kdo může na API pracovat

- Soulad s osvědčenými postupy v odvětví pro konvence pojmenování REST API

- Snadnost implementace a údržby

## Rozhodnutí

Pro koncové body REST API se bude používat konvence pojmenování snake_case. Tato volba je řízena následujícími faktory:

1. **Konzistence**: Projekt již používá konvenci pojmenování snake_case pro všechny koncové body a bylo by přínosné tuto konvenci zachovat, aby byla zajištěna konzistence v celém projektu.

2. **Čitelnost a srozumitelnost**: Konvence snake_case je čitelnější a snáze pochopitelná. Podtržítka poskytují jasné oddělení slov, takže je snazší název analyzovat a porozumět jeho významu.

3. **Soulad s osvědčenými postupy v odvětví**: Konvence snake_case se v odvětví široce používá a je považována za osvědčený postup pro REST API, takže je pro projekt dobrou volbou.

4. **Snadnost implementace a údržby**: Zachování stávající konvence pojmenování je snazší na implementaci a údržbu, protože při zvolení nové konvence by bylo nutné aktualizovat veškerý stávající kód a dokumentaci.

## Důsledky

Toto rozhodnutí má možné důsledky. 

* Pokud noví členové týmu, kteří se k projektu připojí, neznají konvenci pojmenování snake_case, může to vést k nejasnostem a chybám ve vývoji. Protože je však snake_case široce používaná konvence, je takové riziko minimální. 
  
* Pokud se v projektu používají jiné nástroje nebo frameworky silně založené na konvenci camelCase, může být nutné vynaložit další úsilí na převod mezi konvencemi pojmenování. Není to však významný problém, protože projekt je standardizován na konvenci snake_case. 
 
Celkově rozhodnutí použít pro koncové body REST API konvenci pojmenování snake_case vede ke konzistentnímu, čitelnému a oborově standardnímu přístupu, který je zároveň snadno implementovatelný a udržovatelný.

<h6>Zdroj: tuto stránku vygeneroval ChatGPT a poté byla upravena pro přehlednost a formát.</h6>