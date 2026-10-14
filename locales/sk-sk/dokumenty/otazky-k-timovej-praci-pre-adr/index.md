
### Kto môže vytvoriť ADR?

Zvážte oblasti ako konkrétni ľudia, konkrétne roly, konkrétne tímy alebo konkrétne oddelenia; zvážte aj to, či existujú ľudia, roly, tímy alebo oddelenia, ktoré môžu ADR objednať, teda požiadať o ADR, ktorý napíše niekto iný. 

Príklad odpovede: Ktorákoľvek osoba v našej organizácii, ktorá si prečítala stránku README o zázname architektonického rozhodnutia, môže navrhnúť ADR, čo znamená, že ho môže začať písať a zdieľať s tímom.

### Čo odôvodňuje vznik ADR?

Zvážte oblasti ako spôsoby práce tímu vo vašej organizácii, štruktúra vášho softvérového systému, koordinácia medzi tímami, dlhodobá udržiavateľnosť, externé rozhrania, kto má mať prospech a podobne. 

Príklad odpovede: Chceme vytvoriť ADR, keď chceme, aby budúci vývojári pochopili „prečo“ toho, čo robíme.

### Čo odôvodňuje nevytvorenie ADR?

Zvážte oblasti ako rozhodnutia, ktoré nie sú o architektúre alebo sú drobné, napríklad s minimálnym rizikom, samostatné alebo pre jedného vývojára, alebo sú už úplne pokryté inde, napríklad štandardmi, politikami alebo dokumentáciou, alebo sú dočasné, napríklad obchádzky, dôkazy konceptu alebo experimenty. 

Príklad odpovede: Chceme preskočiť ADR, keď je rozhodnutie obmedzené rozsahom, časom, rizikom a nákladmi alebo je už pokryté inde.

### Aký je životný cyklus ADR?

Zvážte oblasti ako proces tvorby, proces výskumu, proces rozhodovania, proces implementácie a proces ukončenia. Zvážte, ako sledovať životný cyklus ADR v čase, napríklad ako presunúť ADR z jedného stavu do ďalšieho a tiež ako to komunikovať zainteresovaným stranám. 

Príklad odpovede: Chceme, aby mal ADR päť fáz životného cyklu: Iniciovanie → Skúmanie → Vyhodnocovanie → Implementácia → Udržiavanie → Ukončenie.

### Aké sú kritériá pre kroky životného cyklu ADR?

Zvážte oblasti ako akceptačné kritériá pre ADR, teda ako viete, že je dosť dobrý na to, aby postúpil z jedného kroku životného cyklu do ďalšieho? Je problém jasne sformulovaný? Boli zvážené alternatívy? Sú kompromisy dostatočne pochopené a zdokumentované?
Je k dispozícii všetok relevantný kontext? Sú zapojené všetky relevantné zainteresované strany? Bola zapracovaná všetka spätná väzba? 

Príklad odpovede: Chceme, aby o ADR hlasovali zainteresované strany, keď aktívny tím 1) dokončil svoj výskum, 2) dokončil svoje vyhodnotenie, 3) zverejnil návrh ADR zainteresovaným stranám s výzvou na pripomienky a lehotou jedného týždňa, 4) všetky pripomienky zainteresovaných strán boli zapracované a vyriešené.

### Aké roly a zodpovednosti interagujú s ADR?

Zvážte roly ako navrhovateľ, výskumník, hodnotiteľ, recenzent, schvaľovateľ, správca a podobne. Zvážte zodpovednosti ako komunikácia so zainteresovanými stranami, zabezpečenie splnenia očakávaní, zdieľanie na webovej lokalite alebo intranete a pravidelná revízia práce, najmä keď nastanú relevantné zmeny.

Príklad odpovede: Chceme, aby mal každý ADR vždy primárnu kontaktnú osobu, sekundárnu kontaktnú osobu a zodpovedný tím; tí sú zodpovední za komunikáciu, publikácie, údržbu, pravidelnú revíziu aspoň raz ročne a prípadné ukončenie podľa potreby.

### Ako riadenie (governance) interaguje s ADR?

Zvážte oblasti ako spôsoby práce vašej organizácie, akékoľvek osobitné potreby zhody, napríklad pre právne aspekty alebo aspekty ľudských zdrojov, ako chcete zaobchádzať s konsenzom oproti konfliktu oproti eskalácii. Existujú oblasti, osoby alebo tímy, ktoré môžu mať väčší vplyv než iné, pokiaľ ide o ADR, napríklad ho môžu schváliť, hlasovať o ňom alebo naň uvaliť veto?

Príklad odpovede: Riadenie ADR je v tomto poradí priority: generálny riaditeľ, technický riaditeľ, právny riaditeľ, tím, ktorý ADR implementuje, odborníci v tíme, ktorí najlepšie poznajú AD. Nikto iný nemá právomoc riadenia, pokiaľ nie je opísaná v ADR. 

### Aké princípy interagujú s ADR?

Zvážte oblasti ako spôsoby práce vašej organizácie, ktoré zahŕňajú rýchle pohyb oproti pomalému pohybu, konsenzus pri rozhodnutiach oproti konfliktu pri rozhodnutiach, preferencie rizika oproti preferenciám bezpečnosti, verejná diskusia oproti súkromnej diskusii a podobne.

Príklad odpovede: Používame vodcovské princípy sklonu ku konaniu, nesúhlasu a záväzku (disagree-and-commit), 70 % odhady sú dosť dobré pre ľahko vratné, ľahko izolovateľné rozhodnutia a verejné spôsoby práce s výnimkou dôverných informácií, ako je opísané v dohode o dôvernosti našej organizácie.
