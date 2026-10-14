# Záznam architektonického rozhodnutí (ADR) pro komponenty Svelte

<!--

Prompt:

Architecture decision record for Svelte components.

Compare options: SVAR, Carbon, Flowbite, SkeletonUI, MeltUI, SvelteUI, shadcn-svelte

The goal is full features for table, charts, lists, grids, gantt, 

-->

## Kontext

Vybíráme knihovnu UI komponent pro Svelte, která poskytne plné funkce pro:
- **Tabulky**
- **Grafy**
- **Seznamy**
- **Mřížky**
- **Ganttovy diagramy**

Cílem je zvolit knihovnu, která vyvažuje snadnost integrace, plnou podporu funkcí, výkon a dlouhodobou udržovatelnost. Zvažované možnosti jsou:

1. **SVAR**
2. **Carbon**
3. **Flowbite**
4. **SkeletonUI**
5. **MeltUI**
6. **SvelteUI**
7. **shadcn-svelte**

## Analýza možností

### 1. **SVAR**
- **Přehled**: SVAR je moderní, funkčně bohatá knihovna komponent pro Svelte se zaměřením na designové systémy a komponenty připravené pro enterprise.
- **Klady**:
  - Plnohodnotné komponenty, včetně tabulek, formulářů a grafů.
  - Vysoké možnosti přizpůsobení s vestavěnou podporou témat.
  - Vestavěná podpora přístupnosti a responzivity.
  - Dobře zdokumentováno s příspěvky komunity.
- **Zápory**:
  - Může být těžší ve srovnání s jinými jednoduššími knihovnami.
  - Omezená podpora konkrétních komponent, jako jsou Ganttovy diagramy a pokročilé mřížky.
- **Nejlepší pro**: Aplikace na úrovni enterprise, kde je nutný plnohodnotný designový systém.
- **Podpora tabulek/grafů**: Střední až dobrá.
- **Podpora mřížek/Ganttu**: Minimální.

### 2. **Carbon**
- **Přehled**: Carbon Design System je open source designový systém od IBM nabízející robustní sadu komponent UI.
- **Klady**:
  - Vysoce kvalitní, vypilovaný design s rozsáhlou dokumentací.
  - Velmi přístupný a responzivní.
  - Velká knihovna komponent, včetně mřížek, tabulek a ovládacích prvků formulářů.
- **Zápory**:
  - Není zaměřen na Svelte, takže integrace může být těžkopádná.
  - Může vyžadovat další přizpůsobení pro plnou kompatibilitu se Svelte.
  - Žádná podpora pokročilých komponent, jako jsou Ganttovy diagramy nebo složité grafy, hned po instalaci.
- **Nejlepší pro**: Rozsáhlé projekty vyžadující konzistentní, vypilované UI.
- **Podpora tabulek/grafů**: Dobrá (s integrací knihoven pro grafy).
- **Podpora mřížek/Ganttu**: Dobrá (podpora mřížek je k dispozici, ale žádné Ganttovy diagramy).

### 3. **Flowbite**
- **Přehled**: Flowbite je knihovna komponent postavená na Tailwind CSS, nabízející různé komponenty a prvky UI.
- **Klady**:
  - Založeno na Tailwind CSS, což usnadňuje přizpůsobení.
  - Snadno se integruje a používá se Svelte.
  - Poskytuje bohaté komponenty, jako jsou tabulky, grafy a ovládací prvky UI.
- **Zápory**:
  - Chybí pokročilé funkce (např. Ganttovy diagramy nebo složité mřížky).
  - Nemá nativní komponenty pro grafy; spoléhá na externí knihovny.
- **Nejlepší pro**: Projekty vyžadující rychlý vývoj se zaměřením na integraci Tailwind CSS.
- **Podpora tabulek/grafů**: Dobrá (vyžaduje integraci s knihovnami grafů třetích stran).
- **Podpora mřížek/Ganttu**: Minimální.

### 4. **SkeletonUI**
- **Přehled**: SkeletonUI je lehká knihovna komponent pro Svelte se zaměřením na jednoduchost a minimalismus.
- **Klady**:
  - Extrémně lehká a rychlá.
  - Jednoduché a intuitivní API.
  - Dobrá pro malé projekty nebo tam, kde je kritický výkon.
- **Zápory**:
  - Zahrnuje velmi málo komponent, takže není funkčně bohatá.
  - Chybí pokročilé komponenty pro tabulky/mřížky/grafy/Gantt.
  - Omezená podpora komunity a méně obsáhlá dokumentace.
- **Nejlepší pro**: Projekty, které vyžadují lehké komponenty s minimální režií.
- **Podpora tabulek/grafů**: Minimální.
- **Podpora mřížek/Ganttu**: Minimální.

### 5. **MeltUI**
- **Přehled**: MeltUI je sbírka přístupných komponent UI pro Svelte se zaměřením na jednoduchost a skládatelnost.
- **Klady**:
  - Lehká a plně přizpůsobitelná.
  - Dobré funkce přístupnosti hned po instalaci.
  - Moderní a minimalistický design.
- **Zápory**:
  - Méně funkčně bohatá ve srovnání s jinými knihovnami.
  - Chybí pokročilé komponenty mřížek a tabulek.
  - Žádné Ganttovy diagramy ani složité možnosti grafů.
- **Nejlepší pro**: Minimalistické designy, které upřednostňují přístupnost a výkon.
- **Podpora tabulek/grafů**: Minimální.
- **Podpora mřížek/Ganttu**: Minimální.

### 6. **SvelteUI**
- **Přehled**: SvelteUI je komplexní a přizpůsobitelná knihovna komponent UI pro Svelte, navržená pro tvorbu moderních webových aplikací s elegantním UI.
- **Klady**:
  - Komplexní sada komponent, včetně tabulek, mřížek, grafů a formulářů.
  - Poskytuje podporu světlého i tmavého režimu.
  - Vysoce přizpůsobitelná a snadno rozšiřitelná.
  - Vestavěné integrace pro knihovny grafů, jako jsou `chart.js` nebo `d3.js`.
- **Zápory**:
  - Může být těžší než jednodušší knihovny komponent.
  - Vyžaduje určité nastavení pro integraci externích knihoven pro složitější funkce, jako jsou Ganttovy diagramy.
- **Nejlepší pro**: Projekty, které potřebují komplexní, přizpůsobitelnou sadu komponent.
- **Podpora tabulek/grafů**: Výborná (podporovány knihovny grafů).
- **Podpora mřížek/Ganttu**: Dobrá (komponenty mřížek jsou k dispozici; Gantt potřebuje externí integraci).

### 7. **shadcn-svelte**
- **Přehled**: Verze ShadCN pro Svelte, která se zaměřuje na utility-first design a poskytuje moderní, nastylované komponenty.
- **Klady**:
  - Utility-first design, postavený na Tailwind CSS, což usnadňuje přizpůsobení.
  - Bohatá sada komponent a plně nastylovaná hned po instalaci.
  - Snadno se integruje s jinými knihovnami.
- **Zápory**:
  - Není tak funkčně úplná jako některé jiné, pokud jde o pokročilé prvky UI.
  - Chybí vestavěná podpora tabulek, grafů nebo mřížek.
  - Žádná podpora Ganttových diagramů hned po instalaci.
- **Nejlepší pro**: Malé až střední projekty vyžadující utility-first, přizpůsobitelný přístup.
- **Podpora tabulek/grafů**: Minimální.
- **Podpora mřížek/Ganttu**: Minimální.

## Rozhodnutí

### Doporučená možnost: **SvelteUI**

- **Zdůvodnění**: SvelteUI nabízí vyváženou, komplexní sadu komponent, která pokrývá potřebu tabulek, grafů, mřížek a formulářů. Je vysoce přizpůsobitelné, dobře se integruje s dalšími knihovnami grafů (jako `chart.js` a `d3.js`) a má dobrou rovnováhu lehkého výkonu a funkční bohatosti. Ačkoli nemusí poskytovat podporu Ganttových diagramů hned po instalaci, lze ho snadno rozšířit integracemi třetích stran, takže je ideální pro plnohodnotné, škálovatelné řešení.
  
  - **Klady**:
    - Výborná podpora tabulek a grafů.
    - Plné komponenty mřížek a rozvržení.
    - Přizpůsobitelné a dobře se integruje s externími knihovnami grafů.
    - Dobrá komunita a dokumentace.
  
  - **Zápory**:
    - Těžší než některé jiné minimalistické knihovny.
    - Pro složité grafy, jako jsou Ganttovy diagramy, vyžaduje externí integraci.
  
### Alternativa: **Flowbite** nebo **Carbon** (pro větší enterprise projekty)
- Pokud je vyžadován vypilovaný designový systém založený na Tailwindu nebo konzistentnější, mohou být vhodnými alternativami **Flowbite** (s Tailwind CSS) nebo **Carbon** (pro řešení na úrovni enterprise). Mohou však vyžadovat další úsilí pro integraci se složitějšími grafy a komponentami.

## Závěr

Nejlepší volbou pro vaše požadavky (plné funkce pro tabulky, grafy, seznamy, mřížky, Gantt) je **SvelteUI**, následované **Flowbite** a **Carbon** v závislosti na potřebách projektu a designových preferencích.