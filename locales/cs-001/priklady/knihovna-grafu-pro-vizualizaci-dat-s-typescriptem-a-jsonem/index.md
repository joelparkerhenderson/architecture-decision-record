# Záznam architektonického rozhodnutí: knihovna grafů pro vizualizaci dat s TypeScriptem a JSONem

<!--

ChatGPT prompt:

Long software architecture decision record 
chart library toolkit for data visualization using TypeScript and JSON

Evaluate Charts: Apache ECharts, Chart.js, ApexCharts, AG Charts, Highcharts, Carbon Charts, Layer Cake, D3.

Primary need: advanced interactive charts, especially for financial data, scientific data, and government data.

High importance: 1. Agile development because this is for a startup. 2. Doughnut Chart, Radar Chart, Clustering Process
Chart, Area Chart with Time Axis, Candlestick Chart, Nightingale Chart, Geo SVG Map. 3. Free open source.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Primární cíl:**  
Vybrat pokročilou sadu nástrojů pro grafy pro tvorbu interaktivních vizualizací se zaměřením na finanční data, vědecká data a vládní data s použitím TypeScriptu a JSONu. Knihovna by měla poskytovat robustní funkce, flexibilitu a být open source. 

### Kontext a požadavky:

1. **Agilní vývoj (vysoká priorita)**: Jako startup potřebujeme rychlou iteraci, prototypování a flexibilitu ve vývoji. Knihovna grafů musí umožňovat rychlé vývojové cykly.
   
2. **Typy grafů (vysoká priorita)**:
   - **Prstencový graf (doughnut)**
   - **Radarový graf**
   - **Graf procesu shlukování**
   - **Plošný graf s časovou osou**
   - **Svíčkový graf (candlestick)**
   - **Nightingaleův graf**
   - **Geografická SVG mapa**
   
   Tyto typy grafů jsou zvlášť důležité pro vizualizaci složitých datových sad, jako jsou finanční trendy, vědecké metriky a geografické informace.

3. **Zdarma a open source (vysoká priorita)**: Sada nástrojů by měla být open source, aby se předešlo licenčním nákladům, zajistila transparentnost a nabídla flexibilita pro přizpůsobení.

4. **Kritéria nízké důležitosti**:
   - **Rychlost běhu**: Ačkoli je výkon důležitý, pro toto rozhodnutí není hlavní prioritou.
   - **Škálovatelnost**: Ačkoli je škálovatelnost obecně důležitá, okamžitou potřebou je vybudovat MVP, které může časem růst. Otázky škálovatelnosti lze řešit později.
   - **Zpětná kompatibilita**: Pro počáteční sestavení to není hlavní starost, pokud je knihovna moderní a aktivně udržovaná.

### Hodnocené knihovny:

1. **Apache ECharts**
2. **Chart.js**
3. **ApexCharts**
4. **AG Charts**
5. **Highcharts**
6. **Carbon Charts**
7. **Layer Cake**
8. **D3.js**

---

### 1. **Apache ECharts**

**Přehled**:  
Apache ECharts je výkonná, flexibilní knihovna grafů pro interaktivní, přizpůsobitelné vizualizace. Podporuje širokou škálu grafů a je zvlášť silná ve složitých, dynamických vizualizacích.

**Silné stránky**:
- **Pokročilá interaktivita**: ECharts vyniká v poskytování interaktivních grafů s funkcemi jako přibližování, posouvání a dynamické aktualizace dat.
- **Prstencové, radarové, svíčkové grafy, geografické SVG mapy**: ECharts podporuje mnoho požadovaných typů grafů, včetně prstencových, radarových, svíčkových a geografických mapových vizualizací.
- **Zdarma a open source**: ECharts je open source knihovna, což odpovídá úspornému charakteru startupu a poskytuje svobodu upravovat kód.
- **Flexibilita a rozšiřitelnost**: Vysoce přizpůsobitelná, s rozsáhlou podporou animací, vlastních vizualizací a pokročilých technik grafů.
  
**Slabé stránky**:
- **Křivka učení**: ECharts, ačkoli je výkonná, může mít strmější křivku učení kvůli své flexibilitě a rozsáhlému API.
- **Složitost dokumentace**: Dokumentace je obsáhlá, ale může být ohromující pro vývojáře, kteří s ní teprve začínají.

**Verdikt**:  
ECharts je pro projekt velmi vhodná díky podpoře interaktivních grafů, včetně všech požadovaných typů, jako jsou svíčkové grafy, radarové grafy a geografické mapy. Její open source povaha odpovídá potřebě projektu flexibility a nákladové efektivity.

---

### 2. **Chart.js**

**Přehled**:  
Chart.js je jednoduchá, snadno použitelná knihovna grafů pro vytváření běžných typů grafů. Je známá svou jednoduchostí a snadnou integrací.

**Silné stránky**:
- **Snadnost použití**: Chart.js se velmi snadno nastavuje a používá, s minimální křivkou učení.
- **Open source**: Chart.js je zdarma a open source, což je klíčové pro snížení nákladů.
- **Běžné typy grafů**: Podporuje základní grafy jako prstencové, plošné, radarové a spojnicové, které pokrývají většinu hlavních potřeb.

**Slabé stránky**:
- **Omezené pokročilé grafy**: Chart.js nativně nepodporuje složité typy grafů, jako jsou svíčkové grafy, geografické SVG mapy nebo grafy procesu shlukování. Ačkoli lze tyto funkce přidat pomocí zásuvných modulů nebo přizpůsobení, není to tak přímočaré jako u jiných knihoven.
- **Interaktivita**: Ačkoli Chart.js podporuje základní interaktivitu (např. popisky a efekty při najetí), nenabízí tak pokročilé funkce jako ECharts nebo D3.js.

**Verdikt**:  
Chart.js je skvělá pro jednoduché, rychlé projekty, ale nedostatek podpory složitých typů grafů ji činí nevhodnou pro datově náročnou aplikaci s pokročilými potřebami, jako jsou svíčkové grafy a geografické mapy. Je to dobrá volba pro prototypování, ale pro požadované typy grafů se doporučují pokročilejší nástroje.

---

### 3. **ApexCharts**

**Přehled**:  
ApexCharts je moderní knihovna grafů, která poskytuje řadu typů grafů a zaměřuje se na interaktivní vizualizace se snadno použitelným API.

**Silné stránky**:
- **Interaktivní funkce**: ApexCharts nabízí interaktivní grafy s popisky, přibližováním, posouváním a aktualizacemi.
- **Podpora finančních a vědeckých grafů**: Podporuje širokou škálu typů grafů, včetně svíčkových, radarových a plošných grafů.
- **Snadnost použití**: Má přímočaré API a snadno se integruje do projektu.
- **Zdarma a open source**: ApexCharts nabízí bezplatnou open source verzi vhodnou pro mnoho případů použití.
  
**Slabé stránky**:
- **Složité přizpůsobení**: Ačkoli poskytuje mnoho funkcí, možnosti přizpůsobení nejsou tak flexibilní jako u ECharts nebo D3.js pro velmi složité nebo vlastní potřeby grafů.
- **Geografické mapy**: ApexCharts nativně nepodporuje geografické mapy ani grafy procesu shlukování, které jsou pro tento projekt požadovány.

**Verdikt**:  
ApexCharts je silný kandidát díky snadnému použití a interaktivitě, ale u některých pokročilých typů grafů, zejména u potřeby geografických map a shlukovacích grafů, zaostává. Je to dobrá možnost pro jednodušší grafy, ale chybí jí některé požadované funkce.

---

### 4. **AG Charts**

**Přehled**:  
AG Charts je knihovna grafů komerční třídy navržená pro výkon a přesnost. Je velmi vhodná pro tvorbu finančních, vědeckých a podnikových dashboardů.

**Silné stránky**:
- **Pokročilé typy grafů**: AG Charts podporuje mnoho pokročilých typů grafů, včetně svíčkových, plošných, radarových a dalších. Nabízí také hlubokou integraci s dalšími produkty AG-Grid.
- **Vysoký výkon**: Nabízí vynikající výkon, zejména při práci s velkými datovými sadami.
- **Interaktivita**: AG Charts podporuje různé interaktivní funkce, jako je přibližování, popisky a dynamické aktualizace.

**Slabé stránky**:
- **Není plně zdarma**: Ačkoli AG Charts nabízí bezplatnou verzi, plnohodnotná verze je placená, což může být překážkou pro startupy, které chtějí minimalizovat náklady.
- **Složitost**: Ačkoli je knihovna bohatá na funkce, může být pro jednodušší projekty přehnaná a může vyžadovat více nastavení a konfigurace než jiné možnosti.

**Verdikt**:  
AG Charts je výkonná a bohatá na funkce, ale kvůli své komerční povaze a struktuře nákladů nemusí být nejlepší volbou. Její vhodnost závisí na tom, zda rozpočet umožňuje placené verze, nebo se dává přednost open source alternativám.

---

### 5. **Highcharts**

**Přehled**:  
Highcharts je oblíbená knihovna grafů, známá širokou škálou typů grafů a výkonnými možnostmi přizpůsobení.

**Silné stránky**:
- **Komplexní typy grafů**: Highcharts podporuje širokou škálu grafů, včetně svíčkových, radarových, plošných a geografických map.
- **Interaktivní a dynamický**: Highcharts poskytuje bohaté interaktivní funkce, včetně drill-down, přibližování a posouvání.
- **Snadnost použití**: Má uživatelsky přívětivé API a dobrou dokumentaci, takže je snadné začít.

**Slabé stránky**:
- **Komerční licence**: Ačkoli Highcharts nabízí bezplatnou verzi pro nekomerční použití, komerční licence je drahá, což může být pro startupy významnou nevýhodou.
- **Křivka učení**: Ačkoli není tak strmá jako u ECharts, křivka učení Highcharts může být pro začátečníky stále náročná.

**Verdikt**:  
Highcharts je knihovna bohatá na funkce, ale její komerční licencování ji činí méně vhodnou pro open source projekty citlivé na náklady. Komplexní možnosti grafů jsou plus, ale problém s licencováním omezuje její přitažlivost pro tento případ použití.

---

### 6. **Carbon Charts**

**Přehled**:  
Carbon Charts je knihovna grafů vyvinutá společností IBM, navržená pro tvorbu vizuálně přitažlivých a vysoce přizpůsobitelných grafů.

**Silné stránky**:
- **Přizpůsobitelnost**: Carbon Charts umožňuje rozsáhlé přizpůsobení vzhledu a chování grafů.
- **Open source**: Je zdarma a open source, což odpovídá požadavku projektu na řešení šetrná k rozpočtu.
- **Podpora běžných grafů**: Podporuje běžné typy grafů jako prstencové, radarové a plošné, ačkoli jí chybí podpora pokročilejších typů, jako jsou geografické mapy nebo svíčkové grafy.

**Slabé stránky**:
- **Omezené pokročilé typy grafů**: Nepodporuje geografické mapy, grafy procesu shlukování ani svíčkové grafy, které jsou pro projekt zásadní.
- **Menší ekosystém**: Carbon Charts má menší komunitu a ekosystém ve srovnání s většími knihovnami grafů, jako jsou ECharts nebo Highcharts.

**Verdikt**:  
Carbon Charts je open source a přizpůsobitelná, ale chybí jí podpora složitějších typů grafů potřebných pro tento projekt. Je vhodnější pro jednodušší potřeby grafů.

---

### 7. **Layer Cake**

**Přehled**:  
Layer Cake je knihovna pro vizualizaci dat navržená pro tvorbu flexibilních, vrstvených vizualizací.

**Silné stránky**:
- **Přizpůsobitelné vrstvy**: Poskytuje výkonné možnosti vrstvení pro složité vizualizace.
- **Open source**: Je zdarma a open source, takže je životaschopnou možností pro projekty citlivé na rozpočet.

**Slabé stránky**:
- **Omezená dokumentace**: Layer Cake nemá rozsáhlou dokumentaci a podporu komunity, takže se s ní hůře pracuje ve srovnání s zavedenějšími knihovnami.
- **Není postavena pro grafy**: Layer Cake se lépe hodí pro vizualizace, které nejsou grafy, takže její hotové možnosti grafů jsou omezené.

**Verdikt**:  
Ačkoli je zajímavá pro jedinečné vizualizace, Layer Cake není ideální pro tradiční požadavky na grafy, jako jsou svíčkové nebo radarové grafy. Hodí se spíše pro vlastní vizualizace mimo rozsah standardních grafů.

---

### 8. **D3.js**

**Přehled**:  
D3.js je výkonná knihovna JavaScriptu pro tvorbu vizualizací řízených daty pomocí HTML, SVG a CSS.

**Silné stránky**:
- **Nepřekonatelná flexibilita**: D3.js umožňuje vytvořit prakticky jakýkoli typ vlastní vizualizace, takže je velmi výkonná pro pokročilé a interaktivní grafy.
- **Rozsáhlé funkce**: Podporuje všechny požadované typy grafů, včetně geografických map, shlukovacích grafů a dalších.
- **Přizpůsobitelnost**: Úroveň přizpůsobení v D3.js je bezkonkurenční a umožňuje vývojářům vytvářet vysoce na míru šité vizualizace.

**Slabé stránky**:
- **Strmá křivka učení**: D3.js má strmou křivku učení a je složitější na integraci ve srovnání s jinými knihovnami.
- **Časově náročná**: Tvorba grafů v D3.js může být časově náročná, zejména u běžných grafů, jako jsou svíčkové nebo prstencové.

**Verdikt**:  
D3.js je neuvěřitelně výkonná pro pokročilé, vlastní grafy, ale pro mnoho typických případů použití je přehnaná kvůli strmé křivce učení a době vývoje. Nejlepší je v situacích, kdy ostatní knihovny grafů neposkytují požadovanou úroveň přizpůsobení.

---

### Závěr

Po vyhodnocení knihoven podle potřeb projektu se jako nejlepší možnost vyčleňuje **Apache ECharts**. Podporuje celou škálu požadovaných grafů, včetně geografických map, svíčkových grafů a shlukovacích grafů. Je open source, bohatá na funkce a vysoce interaktivní, což dokonale odpovídá cílům projektu. Ačkoli **D3.js** nabízí největší flexibilitu, její složitost a časová investice ji činí méně ideální pro startup, který chce rychle iterovat. **ApexCharts** a **Chart.js** jsou dobré alternativy pro jednodušší projekty, ale chybí jim podpora pokročilých typů grafů.
