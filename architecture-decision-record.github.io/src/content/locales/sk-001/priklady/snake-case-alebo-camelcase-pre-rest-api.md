# Záznam architektonického rozhodnutia: snake_case alebo camelCase pre REST API?

Rozhodnutie: Pre koncové body REST API sa bude používať konvencia pomenovania snake_case

Stav: Prijaté

## Kontext

V konvenciách pomenovania pre REST API existujú dva populárne formáty: snake_case a camelCase. Formát snake_case je taký, kde je každé slovo v názve oddelené podčiarkovníkmi, zatiaľ čo camelCase je taký, kde je prvé slovo názvu písané malými písmenami a ďalšie slová majú prvé písmeno veľké. Toto rozhodnutie určí, ktorá konvencia pomenovania sa má pre REST API použiť.

## Hnacie sily rozhodnutia

- Konzistentnosť s existujúcimi konvenciami pomenovania v projekte

- Čitateľnosť a prehľadnosť pre každého, kto môže na API pracovať

- Súlad s osvedčenými odvetvovými postupmi pre konvencie pomenovania REST API

- Jednoduchosť implementácie a údržby

## Rozhodnutie

Pre koncové body REST API sa bude používať konvencia pomenovania snake_case. Túto voľbu určujú nasledujúce faktory:

1. **Konzistentnosť**: Projekt už používa konvenciu pomenovania snake_case pre všetky koncové body a bolo by prínosné túto konvenciu zachovať, aby sa zabezpečila konzistentnosť v celom projekte.

2. **Čitateľnosť a prehľadnosť**: Konvencia snake_case je čitateľnejšia a ľahšie pochopiteľná. Podčiarkovníky poskytujú jasné oddelenie slov, čo uľahčuje analýzu a pochopenie významu názvu.

3. **Súlad s osvedčenými odvetvovými postupmi**: Konvencia snake_case sa v odvetví široko používa a považuje sa za osvedčený postup pre REST API, vďaka čomu je dobrou voľbou pre projekt.

4. **Jednoduchosť implementácie a údržby**: Zachovanie existujúcej konvencie pomenovania je jednoduchšie na implementáciu a údržbu, pretože pri zvolení novej konvencie by sa musel aktualizovať všetok existujúci kód a dokumentácia.

## Dôsledky

Toto rozhodnutie má možné dôsledky. 

* Ak noví členovia tímu, ktorí sa k projektu pripoja, nepoznajú konvenciu pomenovania snake_case, môže to viesť k zmätku a chybám vo vývoji. Keďže však snake_case je široko používaná konvencia, takéto riziko je minimálne. 
  
* Ak sa v projekte používajú iné nástroje alebo frameworky silno založené na konvencii camelCase, môže byť potrebné vynaložiť dodatočné úsilie na prevod medzi konvenciami pomenovania. Nie je to však významná obava, keďže projekt je štandardizovaný na konvencii snake_case. 
 
Celkovo rozhodnutie použiť pre koncové body REST API konvenciu pomenovania snake_case vedie ku konzistentnému, čitateľnému a odvetvovo štandardnému prístupu, ktorý je zároveň jednoduchý na implementáciu a údržbu.

<h6>Zdroj: túto stránku vygeneroval ChatGPT a potom bola upravená kvôli prehľadnosti a formátu.</h6>