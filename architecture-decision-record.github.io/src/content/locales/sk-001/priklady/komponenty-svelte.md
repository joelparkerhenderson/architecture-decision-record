# Záznam architektonického rozhodnutia (ADR) pre komponenty Svelte

<!--

Prompt:

Architecture decision record for Svelte components.

Compare options: SVAR, Carbon, Flowbite, SkeletonUI, MeltUI, SvelteUI, shadcn-svelte

The goal is full features for table, charts, lists, grids, gantt, 

-->

## Kontext

Vyberáme knižnicu UI komponentov pre Svelte, ktorá poskytne plné funkcie pre:
- **Tabuľky**
- **Grafy**
- **Zoznamy**
- **Mriežky**
- **Ganttove diagramy**

Cieľom je zvoliť knižnicu, ktorá vyvažuje jednoduchosť integrácie, plnú podporu funkcií, výkon a dlhodobú udržiavateľnosť. Zvažované možnosti sú:

1. **SVAR**
2. **Carbon**
3. **Flowbite**
4. **SkeletonUI**
5. **MeltUI**
6. **SvelteUI**
7. **shadcn-svelte**

## Analýza možností

### 1. **SVAR**
- **Prehľad**: SVAR je moderná, funkciami bohatá knižnica komponentov pre Svelte so zameraním na dizajnové systémy a komponenty pripravené pre enterprise.
- **Výhody**:
  - Plnohodnotné komponenty vrátane tabuliek, formulárov a grafov.
  - Vysoké možnosti prispôsobenia so vstavanou podporou tém.
  - Vstavaná podpora prístupnosti a responzívnosti.
  - Dobre zdokumentované s príspevkami komunity.
- **Nevýhody**:
  - Môže byť ťažšia v porovnaní s inými jednoduchšími knižnicami.
  - Obmedzená podpora konkrétnych komponentov, ako sú Ganttove diagramy a pokročilé mriežky.
- **Najvhodnejšia pre**: Aplikácie na úrovni enterprise, kde je potrebný plnohodnotný dizajnový systém.
- **Podpora tabuliek/grafov**: Stredná až dobrá.
- **Podpora mriežok/Ganttu**: Minimálna.

### 2. **Carbon**
- **Prehľad**: Carbon Design System je open source dizajnový systém od IBM, ktorý ponúka robustný súbor UI komponentov.
- **Výhody**:
  - Vysokokvalitný, vypilovaný dizajn s rozsiahlou dokumentáciou.
  - Veľmi prístupná a responzívna.
  - Veľká knižnica komponentov vrátane mriežok, tabuliek a ovládacích prvkov formulárov.
- **Nevýhody**:
  - Nie je zameraná na Svelte, takže integrácia môže byť ťažkopádna.
  - Môže vyžadovať dodatočné prispôsobenie pre plnú kompatibilitu so Svelte.
  - Žiadna podpora pokročilých komponentov ako Ganttove diagramy alebo zložité grafy hneď po inštalácii.
- **Najvhodnejšia pre**: Rozsiahle projekty vyžadujúce konzistentné, vypilované UI.
- **Podpora tabuliek/grafov**: Dobrá (s integráciami knižníc grafov).
- **Podpora mriežok/Ganttu**: Dobrá (podpora mriežok je k dispozícii, ale žiadne Ganttove diagramy).

### 3. **Flowbite**
- **Prehľad**: Flowbite je knižnica komponentov postavená na Tailwind CSS, ktorá ponúka rôzne komponenty a UI prvky.
- **Výhody**:
  - Založená na Tailwind CSS, čo uľahčuje prispôsobenie.
  - Jednoduchá integrácia a používanie so Svelte.
  - Poskytuje bohaté komponenty ako tabuľky, grafy a UI ovládacie prvky.
- **Nevýhody**:
  - Chýbajú pokročilé funkcie (napr. Ganttove diagramy alebo zložité mriežky).
  - Nemá natívne komponenty pre grafy; spolieha sa na externé knižnice.
- **Najvhodnejšia pre**: Projekty vyžadujúce rýchly vývoj so zameraním na integráciu Tailwind CSS.
- **Podpora tabuliek/grafov**: Dobrá (vyžaduje integráciu s knižnicami grafov tretích strán).
- **Podpora mriežok/Ganttu**: Minimálna.

### 4. **SkeletonUI**
- **Prehľad**: SkeletonUI je ľahká knižnica komponentov pre Svelte zameraná na jednoduchosť a minimalizmus.
- **Výhody**:
  - Extrémne ľahká a rýchla.
  - Jednoduché a intuitívne API.
  - Dobrá pre malé projekty alebo tam, kde je kritický výkon.
- **Nevýhody**:
  - Obsahuje veľmi málo komponentov, takže nie je bohatá na funkcie.
  - Chýbajú pokročilé komponenty pre tabuľky/mriežky/grafy/Gantt.
  - Obmedzená podpora komunity a menej obsiahla dokumentácia.
- **Najvhodnejšia pre**: Projekty, ktoré vyžadujú ľahké komponenty s minimálnou réžiou.
- **Podpora tabuliek/grafov**: Minimálna.
- **Podpora mriežok/Ganttu**: Minimálna.

### 5. **MeltUI**
- **Prehľad**: MeltUI je zbierka prístupných UI komponentov pre Svelte zameraných na jednoduchosť a skladateľnosť.
- **Výhody**:
  - Ľahká a plne prispôsobiteľná.
  - Dobré funkcie prístupnosti hneď po inštalácii.
  - Moderný a minimalistický dizajn.
- **Nevýhody**:
  - Menej bohatá na funkcie v porovnaní s inými knižnicami.
  - Chýbajú pokročilé komponenty mriežok a tabuliek.
  - Žiadne Ganttove diagramy ani zložité možnosti grafov.
- **Najvhodnejšia pre**: Minimalistické dizajny, ktoré uprednostňujú prístupnosť a výkon.
- **Podpora tabuliek/grafov**: Minimálna.
- **Podpora mriežok/Ganttu**: Minimálna.

### 6. **SvelteUI**
- **Prehľad**: SvelteUI je komplexná a prispôsobiteľná knižnica UI komponentov pre Svelte navrhnutá na budovanie moderných webových aplikácií s elegantným UI.
- **Výhody**:
  - Komplexný súbor komponentov vrátane tabuliek, mriežok, grafov a formulárov.
  - Poskytuje podporu svetlého aj tmavého režimu.
  - Vysoko prispôsobiteľná a ľahko rozšíriteľná.
  - Vstavané integrácie pre knižnice grafov ako `chart.js` alebo `d3.js`.
- **Nevýhody**:
  - Môže byť ťažšia než jednoduchšie knižnice komponentov.
  - Vyžaduje určité nastavenie na integráciu externých knižníc pre zložitejšie funkcie ako Ganttove diagramy.
- **Najvhodnejšia pre**: Projekty, ktoré potrebujú komplexný, prispôsobiteľný súbor komponentov.
- **Podpora tabuliek/grafov**: Výborná (podporované knižnice grafov).
- **Podpora mriežok/Ganttu**: Dobrá (komponenty mriežok sú k dispozícii; Gantt potrebuje externú integráciu).

### 7. **shadcn-svelte**
- **Prehľad**: Verzia ShadCN pre Svelte, ktorá sa zameriava na utility-first dizajn a poskytuje moderné, ostylované komponenty.
- **Výhody**:
  - Utility-first dizajn postavený na Tailwind CSS, čo uľahčuje prispôsobenie.
  - Bohatý súbor komponentov a plne ostylované hneď po inštalácii.
  - Jednoduchá integrácia s inými knižnicami.
- **Nevýhody**:
  - Nie je taká funkčne kompletná ako niektoré iné, pokiaľ ide o pokročilé UI prvky.
  - Chýba vstavaná podpora tabuliek, grafov alebo mriežok.
  - Žiadna podpora Ganttových diagramov hneď po inštalácii.
- **Najvhodnejšia pre**: Malé až stredné projekty vyžadujúce utility-first, prispôsobiteľný prístup.
- **Podpora tabuliek/grafov**: Minimálna.
- **Podpora mriežok/Ganttu**: Minimálna.

## Rozhodnutie

### Odporúčaná možnosť: **SvelteUI**

- **Zdôvodnenie**: SvelteUI ponúka vyvážený, komplexný súbor komponentov, ktorý pokrýva potrebu tabuliek, grafov, mriežok a formulárov. Je vysoko prispôsobiteľná, dobre sa integruje s ďalšími knižnicami grafov (ako `chart.js` a `d3.js`) a má dobrú rovnováhu ľahkého výkonu a bohatstva funkcií. Hoci nemusí poskytovať natívnu podporu Ganttových diagramov, dá sa ľahko rozšíriť integráciami tretích strán, vďaka čomu je ideálna pre plnohodnotné, škálovateľné riešenie.
  
  - **Výhody**:
    - Výborná podpora tabuliek a grafov.
    - Plné komponenty mriežok a rozloženia.
    - Prispôsobiteľná a dobre sa integruje s externými knižnicami grafov.
    - Dobrá komunita a dokumentácia.
  
  - **Nevýhody**:
    - Ťažšia než niektoré iné minimalistické knižnice.
    - Pre zložité grafy ako Ganttove diagramy vyžaduje externú integráciu.
  
### Alternatíva: **Flowbite** alebo **Carbon** (pre väčšie enterprise projekty)
- Ak je potrebný vypilovaný dizajnový systém založený na Tailwinde alebo konzistentnejší, vhodnými alternatívami môžu byť **Flowbite** (s Tailwind CSS) alebo **Carbon** (pre riešenia na úrovni enterprise). Môžu však vyžadovať dodatočné úsilie na integráciu so zložitejšími grafmi a komponentmi.

## Záver

Najvhodnejšou voľbou pre vaše požiadavky (plné funkcie pre tabuľky, grafy, zoznamy, mriežky, Gantt) je **SvelteUI**, nasledovaná **Flowbite** a **Carbon** v závislosti od potrieb projektu a dizajnových preferencií.