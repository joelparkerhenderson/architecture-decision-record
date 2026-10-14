# Záznam architektonického rozhodnutia: framework webových aplikácií, všetko v jednom, full stack, pre produkt startupu

<!-- 

ChatGPT prompt

Long software architecture decision record 
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports. 

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Primárny cieľ:**  
Vybudovať webovú aplikáciu, v ktorej sa platiaci zákazníci môžu prihlásiť, nahrávať súbory, spracúvať dáta a prezerať reporty, so zameraním na agilný vývoj, full-stack funkcionalitu a silnú kompatibilitu s nástrojmi AI/ML, najmä s notebookmi Project Jupyter.

### Kontext a požiadavky:

1. **Agilný vývoj (vysoká priorita)**: Ako startup potrebujeme rýchlu iteráciu a flexibilitu. Agilné postupy, ako je rýchle prototypovanie, iteratívny vývoj a prispôsobivosť zmenám, sú kľúčové pre náš vývojový cyklus.

2. **Full-stack framework (vysoká priorita)**: Snažíme sa minimalizovať réžiu výberom frameworku, ktorý dokáže efektívne zvládať back-end aj front-end, čím sa znižuje potreba samostatných front-endových frameworkov.

3. **Kompatibilita s nástrojmi AI/ML (vysoká priorita)**: Schopnosť jednoduchej integrácie s nástrojmi na analýzu dát, ako sú notebooky Jupyter, a s dátovo-vedeckým ekosystémom Pythonu (NumPy, Pandas, TensorFlow atď.) je nevyhnutná. To by uľahčilo efektívne spracovanie dát a reportovanie.

4. **Kritériá nízkej dôležitosti**:
   - **Rýchlosť behu**: Hoci je výkon relevantný, na začiatku nie je najkritickejším faktorom, pretože nám viac záleží na rýchlosti vývoja a úplnosti funkcií.
   - **Škálovateľnosť**: Očakávame rast, ale otázky škálovateľnosti možno riešiť neskôr a momentálne to nie je primárna požiadavka.
   - **Spätná kompatibilita**: Zameriavame sa na súčasné technológie a spätná kompatibilita so staršími systémami nás príliš netrápi.

### Hodnotené frameworky:

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Prehľad**:  
Django je webový framework vysokej úrovne pre Python, ktorý podporuje rýchly vývoj a čistý, pragmatický dizajn. Je známy filozofiou „všetko v jednom“ (batteries included), čo znamená, že hneď po inštalácii obsahuje mnoho funkcií, ako je autentifikácia, smerovanie, ORM a spracovanie formulárov.

**Silné stránky**:  
- **Full-stack**: Django je komplexný full-stack framework, ktorý zvládne potreby back-endu aj front-endu s integrovanými funkciami (napr. šablónovací engine, administrátorské rozhranie).
- **Agilný vývoj**: Dobre definovaná štruktúra a konvencie Djanga umožňujú rýchly vývoj a prispôsobivosť, čo je pre prostredie startupu kľúčové. Framework prichádza s vynikajúcou dokumentáciou a bohatým ekosystémom balíkov tretích strán, čo vývoj urýchľuje.
- **Integrácia AI/ML**: Ekosystém Pythonu je v oblasti dátovej vedy a strojového učenia nepremožiteľný. Django, ktoré je založené na Pythone, sa bezproblémovo integruje s nástrojmi ako notebooky Jupyter, Pandas, NumPy, TensorFlow a scikit-learn.
- **Komunita a ekosystém**: Django má rozsiahlu komunitu, robustnú dokumentáciu a širokú škálu zásuvných modulov a rozšírení, čo výrazne urýchľuje vývoj a riešenie problémov.
  
**Slabé stránky**:  
- **Rýchlosť behu**: Python býva pomalší v porovnaní s jazykmi ako Rust alebo Elixir. Pre tento prípad použitia, kde výkon nie je primárnou starosťou, to však nemusí byť prekážkou.
- **Škálovateľnosť**: Hoci je Django vysoko škálovateľné, pri veľmi vysokej škále môžu bez starostlivej optimalizácie nastať problémy (napr. pri spracovaní veľkého množstva súbežných požiadaviek). Django však možno stále účinne škálovať pomocou vyvažovania záťaže a techník cachovania.

**Verdikt**:  
Django dobre zodpovedá požiadavkám na agilný vývoj, full-stack podporu a kompatibilitu s AI/ML. Jeho integrácia s Pythonom ponúka bezproblémový prístup k nástrojom a knižniciam dátovej vedy potrebným pre aplikáciu.

---

### 2. **Ruby on Rails (Ruby)**

**Prehľad**:  
Ruby on Rails (RoR) je zrelý full-stack framework pre webové aplikácie známy prístupom „konvencia pred konfiguráciou“, ktorý uľahčuje rýchly vývoj.

**Silné stránky**:  
- **Full-stack**: RoR prichádza so vstavanými nástrojmi pre vývoj back-endu aj front-endu (napr. pohľady, šablóny, scaffolding) a jeho bohatá knižnica gemov umožňuje rýchlu implementáciu rôznych funkcií.
- **Agilný vývoj**: Ruby on Rails je obzvlášť známe rýchlymi iteračnými cyklami, čo je výhodné pre startupy, ktoré chcú rýchlo iterovať funkcie. RoR podporuje vývoj riadený testami (TDD) a má zavedený ekosystém pre agilné pracovné postupy.
- **Komunita a ekosystém**: RoR má dobre zavedenú, silnú komunitu a širokú ponuku gemov, ktoré môžu vývoj urýchliť.
- **Jednoduchosť používania**: Rails má veľmi prívetivú syntax pre vývojárov a je známe tým, že úlohy ako databázové migrácie, architektúra model-view-controller (MVC) a spracovanie trás sú rýchle a jednoduché.

**Slabé stránky**:  
- **Výkon**: Ruby má zvyčajne pomalší výkon za behu v porovnaní s Pythonom alebo Elixirom. Hoci RoR možno škálovať so správnou infraštruktúrou, výkon Ruby sa môže stať úzkym miestom pre aplikácie, ktoré vyžadujú náročné spracovanie v reálnom čase alebo vysokú súbežnú prevádzku.
- **Integrácia AI/ML**: Hoci má Ruby niektoré knižnice pre strojové učenie, nie je v komunite AI/ML tak široko prijaté ako Python. Integrácia s nástrojmi ako notebooky Jupyter nie je taká bezproblémová, čo robí z Pythonu silnejšiu voľbu pre aplikácie s veľkým množstvom dát.
  
**Verdikt**:  
Hoci Ruby on Rails vyniká v agilnom vývoji a rýchlom prototypovaní, v porovnaní s Pythonom (Django) zaostáva v kompatibilite s AI/ML. Je to životaschopná voľba pre startupy, ktoré uprednostňujú rýchlu iteráciu pred hlbokou integráciou analýzy dát.

---

### 3. **Phoenix (Elixir)**

**Prehľad**:  
Phoenix je webový framework postavený na Elixire, funkcionálnom programovacom jazyku navrhnutom pre škálovateľnosť a súbežnosť. Phoenix využíva virtuálny stroj Erlang, ktorý je známy zvládaním masívnej súbežnosti a systémov odolných voči chybám.

**Silné stránky**:  
- **Škálovateľnosť a výkon**: Phoenix žiari v škálovateľnosti a zvládaní vysokej súbežnosti. Je postavený na virtuálnom stroji Erlang, ktorý dokáže podporovať tisíce (alebo dokonca milióny) súbežných pripojení, čo z neho robí silného kandidáta pre aplikácie vyžadujúce spracovanie dát v reálnom čase alebo vysoký objem prevádzky.
- **Full-stack**: Phoenix zahŕňa všetko potrebné na vybudovanie back-endu aj front-endu aplikácie. Podporuje live views pre interaktívne aktualizácie UI a zahŕňa šablónovací engine.
- **Agilný vývoj**: Phoenix je vysoko modulárny, čo umožňuje rýchlu iteráciu funkcií. Je dobre vhodný pre startupy, ktoré sa potrebujú rýchlo pohybovať.
- **Kompatibilita s AI/ML**: Hoci má Elixir vznikajúce knižnice pre strojové učenie, nie je pre úlohy AI/ML podporovaný tak široko ako Python. Integrácia s nástrojmi ako notebooky Jupyter by vyžadovala obchádzky, keďže ekosystém Elixiru pre dátovú vedu nie je taký zrelý ako ekosystém Pythonu.

**Slabé stránky**:  
- **Ekosystém AI/ML**: Elixir nie je primárnym jazykom používaným v dátovej vede alebo strojovom učení a ekosystém nie je taký zrelý ako ekosystém Pythonu. Integrácia s nástrojmi ako notebooky Jupyter alebo populárne knižnice AI (TensorFlow, PyTorch) tak bude ťažkopádna.
- **Krivka učenia**: Ak tím nepozná funkcionálne programovanie a Elixir, môže byť krivka učenia strmšia.

**Verdikt**:  
Phoenix je výborná voľba, ak sú primárnou starosťou škálovateľnosť a súbežnosť. Vzhľadom na prioritu kompatibility s AI/ML však Phoenix nemusí byť najlepšou voľbou kvôli obmedzenému ekosystému Elixiru v tejto oblasti.

---

### 4. **Loco (Rust)**

**Prehľad**:  
Loco je webový framework postavený na Ruste, systémovom programovacom jazyku známom výkonom, bezpečnosťou pamäte a súbežnosťou. Rust je čoraz populárnejší na budovanie vysokovýkonných aplikácií.

**Silné stránky**:  
- **Výkon**: Hlavná sila Rustu spočíva vo vysokom výkone a bezpečnosti pamäte, čo z neho robí vynikajúcu voľbu pre aplikácie vyžadujúce nízkoúrovňovú kontrolu alebo mimoriadne vysoký výkon.
- **Súbežnosť**: Systém vlastníctva v Ruste zaisťuje bezpečnosť pamäte a zároveň umožňuje bezpečné súbežné programovanie, vďaka čomu je ideálny pre systémy, ktoré sa potrebujú efektívne škálovať a zvládať paralelizmus.

**Slabé stránky**:  
- **Full-stack vývoj**: Loco, hoci je sľubné, nie je také zrelé ako ostatné frameworky, pokiaľ ide o poskytnutie kompletného full-stack riešenia. Je vhodnejšie pre vývoj back-endu a front-endový ekosystém okolo Rustu sa ešte len formuje.
- **Agilný vývoj**: Vývoj v Ruste môže byť pomalší v porovnaní s jazykmi vyššej úrovne ako Python alebo Ruby kvôli jeho nižšej úrovni a strmšej krivke učenia.
- **Ekosystém AI/ML**: Rust nemá taký rozsiahly ekosystém pre AI/ML ako Python. Hoci v Ruste vznikajú rastúce knižnice pre numerické výpočty, sú oveľa menej zrelé než ponuka Pythonu, ako sú notebooky Jupyter alebo frameworky strojového učenia.
  
**Verdikt**:  
Hoci Rust a jeho framework Loco ponúkajú výnimočný výkon, nedostatok full-stack podpory, výhod agilného vývoja a ekosystému AI/ML ich robí pre tento konkrétny prípad použitia menej ideálnymi. Sú vhodnejšie pre aplikácie kritické z hľadiska výkonu než pre rýchly webový vývoj s integrovanými nástrojmi dátovej vedy.

---

### Záver

Po vyhodnotení možností na základe požiadaviek projektu je **Django (Python)** najvhodnejšou voľbou. Ponúka tieto výhody:

- **Full-stack schopnosti**: Django je full-stack framework, ktorý integruje vývoj back-endu aj front-endu.
- **Agilný vývoj**: Framework je dobre vhodný na rýchle prototypovanie a iteráciu, čo je pre prostredie startupu nevyhnutné.
- **Kompatibilita s AI/ML**: Python je popredný jazyk v AI/ML a kompatibilita Djanga s knižnicami ako notebooky Jupyter zaisťuje hladkú integráciu pre analýzu a spracovanie dát.
- **Komunita a ekosystém**: Silná podpora komunity Djanga a rozsiahly ekosystém knižníc poskytujú množstvo nástrojov na urýchlenie vývoja.

Hoci je **Ruby on Rails** tiež silným kandidátom pre agilný vývoj, jeho obmedzená podpora AI/ML ho robí pre tento konkrétny prípad použitia menej ideálnym. **Phoenix (Elixir)** a **Loco (Rust)**, hoci sú vynikajúce z hľadiska škálovateľnosti a výkonu, zaostávajú v integrácii AI/ML a full-stack vývoji. Django je preto odporúčaným frameworkom pre tento projekt.