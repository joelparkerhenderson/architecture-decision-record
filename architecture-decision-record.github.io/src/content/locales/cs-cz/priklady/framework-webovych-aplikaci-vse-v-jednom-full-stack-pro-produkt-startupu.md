# Záznam architektonického rozhodnutí: webový aplikační framework, vše v jednom, full stack, pro produkt startupu

<!-- 

ChatGPT prompt

Long software architecture decision record 
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports. 

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Primární cíl:**  
Vytvořit webovou aplikaci, ve které se platící zákazníci mohou přihlásit, nahrávat soubory, zpracovávat data a prohlížet reporty, se zaměřením na agilní vývoj, full-stack funkcionalitu a silnou kompatibilitu s nástroji AI/ML, zejména s notebooky Project Jupyter.

### Kontext a požadavky:

1. **Agilní vývoj (vysoká priorita)**: Jako startup potřebujeme rychlé iterace a flexibilitu. Agilní postupy, jako je rychlé prototypování, iterativní vývoj a přizpůsobivost změnám, jsou klíčové pro náš vývojový cyklus.

2. **Full-stack framework (vysoká priorita)**: Snažíme se minimalizovat režii výběrem frameworku, který dokáže efektivně zvládnout back-end i front-end a snižuje potřebu samostatných front-endových frameworků.

3. **Kompatibilita s nástroji AI/ML (vysoká priorita)**: Schopnost snadné integrace s nástroji pro analýzu dat, jako jsou notebooky Jupyter, a s datově-vědeckým ekosystémem Pythonu (NumPy, Pandas, TensorFlow atd.) je nezbytná. To by usnadnilo efektivní zpracování dat a reporting.

4. **Kritéria s nízkou důležitostí**:
   - **Rychlost za běhu**: Ačkoli je výkon relevantní, na začátku není nejkritičtějším faktorem, protože nám více záleží na rychlosti vývoje a úplnosti funkcí.
   - **Škálovatelnost**: Očekáváme růst, ale otázky škálovatelnosti lze řešit později a není to nyní primární požadavek.
   - **Zpětná kompatibilita**: Zaměřujeme se na současné technologie a zpětná kompatibilita se staršími systémy nás příliš netrápí.

### Hodnocené frameworky:

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Přehled**:  
Django je vysokoúrovňový webový framework pro Python, který podporuje rychlý vývoj a čistý, pragmatický návrh. Je známý filozofií „vše v jednom“ (batteries included), což znamená, že hned po instalaci obsahuje mnoho funkcí, jako je autentizace, směrování, ORM a zpracování formulářů.

**Silné stránky**:  
- **Full-stack**: Django je komplexní full-stack framework, který zvládne potřeby back-endu i front-endu s integrovanými funkcemi (např. šablonovací engine, administrátorské rozhraní).
- **Agilní vývoj**: Dobře definovaná struktura a konvence Djanga umožňují rychlý vývoj a přizpůsobivost, což je pro prostředí startupu zásadní. Framework přichází s vynikající dokumentací a bohatým ekosystémem balíčků třetích stran, což vývoj urychluje.
- **Integrace AI/ML**: Ekosystém Pythonu je v oblasti datové vědy a strojového učení nepřekonatelný. Django, které je založeno na Pythonu, se bezproblémově integruje s nástroji jako notebooky Jupyter, Pandas, NumPy, TensorFlow a scikit-learn.
- **Komunita a ekosystém**: Django má rozsáhlou komunitu, robustní dokumentaci a širokou škálu zásuvných modulů a rozšíření, což výrazně urychluje vývoj a řešení problémů.
  
**Slabé stránky**:  
- **Rychlost za běhu**: Python bývá pomalejší ve srovnání s jazyky jako Rust nebo Elixir. Pro tento případ použití, kde výkon není primárním zájmem, to však nemusí být překážka.
- **Škálovatelnost**: Ačkoli je Django vysoce škálovatelné, při velmi vysokém měřítku mohou bez pečlivé optimalizace nastat problémy (např. při zpracování velkého množství souběžných požadavků). Django lze však stále efektivně škálovat pomocí vyvažování zátěže a technik cachování.

**Verdikt**:  
Django dobře odpovídá požadavkům na agilní vývoj, full-stack podporu a kompatibilitu s AI/ML. Jeho integrace s Pythonem nabízí bezproblémový přístup k nástrojům a knihovnám datové vědy, které aplikace potřebuje.

---

### 2. **Ruby on Rails (Ruby)**

**Přehled**:  
Ruby on Rails (RoR) je vyspělý full-stack webový aplikační framework známý přístupem konvence před konfigurací, který usnadňuje rychlý vývoj.

**Silné stránky**:  
- **Full-stack**: RoR přichází s vestavěnými nástroji pro vývoj back-endu i front-endu (např. pohledy, šablony, scaffolding) a jeho bohatá knihovna gemů umožňuje rychlou implementaci různých funkcí.
- **Agilní vývoj**: Ruby on Rails je zvláště známé rychlými iteračními cykly, což je výhodné pro startupy, které chtějí rychle iterovat funkce. RoR podporuje vývoj řízený testy (TDD) a má zavedený ekosystém pro agilní pracovní postupy.
- **Komunita a ekosystém**: RoR má dobře zavedenou, silnou komunitu a širokou nabídku gemů, které mohou vývoj urychlit.
- **Snadné použití**: Rails má velmi přívětivou syntaxi pro vývojáře a je známé tím, že úkoly jako databázové migrace, architektura model-view-controller (MVC) a zpracování tras jsou rychlé a jednoduché.

**Slabé stránky**:  
- **Výkon**: Ruby má obvykle pomalejší výkon za běhu ve srovnání s Pythonem nebo Elixirem. Ačkoli RoR lze škálovat se správnou infrastrukturou, výkon Ruby se může stát úzkým hrdlem u aplikací, které vyžadují náročné zpracování v reálném čase nebo vysoký souběžný provoz.
- **Integrace AI/ML**: Ačkoli má Ruby některé knihovny pro strojové učení, není v komunitě AI/ML tak široce přijímáno jako Python. Integrace s nástroji jako notebooky Jupyter není tak bezproblémová, takže Python je silnější volbou pro datově náročné aplikace.
  
**Verdikt**:  
Ačkoli Ruby on Rails vyniká v agilním vývoji a rychlém prototypování, ve srovnání s Pythonem (Django) zaostává v kompatibilitě s AI/ML. Je to životaschopná volba pro startupy, které upřednostňují rychlou iteraci před hlubokou integrací analýzy dat.

---

### 3. **Phoenix (Elixir)**

**Přehled**:  
Phoenix je webový framework vytvořený v Elixiru, funkcionálním programovacím jazyce navrženém pro škálovatelnost a souběžnost. Phoenix využívá virtuální stroj Erlang, který je známý zvládáním masivní souběžnosti a systémů odolných proti chybám.

**Silné stránky**:  
- **Škálovatelnost a výkon**: Phoenix září ve škálovatelnosti a zvládání vysoké souběžnosti. Je postaven na virtuálním stroji Erlang, který dokáže podporovat tisíce (nebo dokonce miliony) souběžných připojení, což z něj činí silného kandidáta pro aplikace vyžadující zpracování dat v reálném čase nebo vysoký objem provozu.
- **Full-stack**: Phoenix zahrnuje vše potřebné k vytvoření back-endu i front-endu aplikace. Podporuje live views pro interaktivní aktualizace UI a zahrnuje šablonovací engine.
- **Agilní vývoj**: Phoenix je vysoce modulární, což umožňuje rychlou iteraci funkcí. Je dobře vhodný pro startupy, které se potřebují rychle pohybovat.
- **Kompatibilita s AI/ML**: Ačkoli Elixir má vznikající knihovny pro strojové učení, není pro úlohy AI/ML podporován tak široce jako Python. Integrace s nástroji jako notebooky Jupyter by vyžadovala obcházení, protože ekosystém Elixiru pro datovou vědu není tak vyspělý jako ekosystém Pythonu.

**Slabé stránky**:  
- **Ekosystém AI/ML**: Elixir není hlavním jazykem používaným v datové vědě ani strojovém učení a ekosystém není tak vyspělý jako ekosystém Pythonu. Integrace s nástroji jako notebooky Jupyter nebo oblíbené knihovny AI (TensorFlow, PyTorch) tak bude těžkopádná.
- **Křivka učení**: Pokud tým nezná funkcionální programování a Elixir, může být křivka učení strmější.

**Verdikt**:  
Phoenix je vynikající volba, pokud je primárním zájmem škálovatelnost a souběžnost. Vzhledem k prioritě kompatibility s AI/ML však Phoenix nemusí být nejlepší volbou kvůli omezenému ekosystému Elixiru v této oblasti.

---

### 4. **Loco (Rust)**

**Přehled**:  
Loco je webový framework vytvořený v Rustu, systémovém programovacím jazyce známém výkonem, bezpečností paměti a souběžností. Rust je stále populárnější pro vytváření vysoce výkonných aplikací.

**Silné stránky**:  
- **Výkon**: Hlavní síla Rustu spočívá ve vysokém výkonu a bezpečnosti paměti, což z něj činí vynikající volbu pro aplikace vyžadující nízkoúrovňovou kontrolu nebo extrémně vysoký výkon.
- **Souběžnost**: Systém vlastnictví v Rustu zajišťuje bezpečnost paměti a zároveň umožňuje bezpečné souběžné programování, takže je ideální pro systémy, které se potřebují efektivně škálovat a zvládat paralelismus.

**Slabé stránky**:  
- **Full-stack vývoj**: Loco, ač slibné, není tak vyspělé jako ostatní frameworky, pokud jde o poskytnutí kompletního full-stack řešení. Je vhodnější pro vývoj back-endu a front-endový ekosystém kolem Rustu se teprve rodí.
- **Agilní vývoj**: Vývoj v Rustu může být pomalejší ve srovnání s vysokoúrovňovými jazyky jako Python nebo Ruby kvůli jeho nižší úrovni a strmější křivce učení.
- **Ekosystém AI/ML**: Rust nemá tak rozsáhlý ekosystém pro AI/ML jako Python. Ačkoli v Rustu vznikají knihovny pro numerické výpočty, jsou mnohem méně vyspělé než nabídka Pythonu, například notebooky Jupyter nebo frameworky strojového učení.
  
**Verdikt**:  
Ačkoli Rust a jeho framework Loco nabízejí výjimečný výkon, nedostatek full-stack podpory, výhod agilního vývoje a ekosystému AI/ML ho činí pro tento konkrétní případ použití méně ideálním. Je vhodnější pro aplikace kritické z hlediska výkonu než pro rychlý webový vývoj s integrovanými nástroji datové vědy.

---

### Závěr

Po vyhodnocení možností na základě požadavků projektu je **Django (Python)** nejvhodnější volbou. Nabízí následující výhody:

- **Full-stack schopnosti**: Django je full-stack framework, který integruje vývoj back-endu i front-endu.
- **Agilní vývoj**: Framework je dobře vhodný pro rychlé prototypování a iteraci, což je pro prostředí startupu nezbytné.
- **Kompatibilita s AI/ML**: Python je přední jazyk v AI/ML a kompatibilita Djanga s knihovnami jako notebooky Jupyter zajišťuje hladkou integraci pro analýzu a zpracování dat.
- **Komunita a ekosystém**: Silná podpora komunity Djanga a rozsáhlý ekosystém knihoven poskytují řadu nástrojů pro urychlení vývoje.

Ačkoli je **Ruby on Rails** také silným kandidátem pro agilní vývoj, jeho omezená podpora AI/ML ho činí pro tento konkrétní případ použití méně ideálním. **Phoenix (Elixir)** a **Loco (Rust)**, přestože jsou vynikající z hlediska škálovatelnosti a výkonu, zaostávají v integraci AI/ML a full-stack vývoji. Django je proto doporučeným frameworkem pro tento projekt.