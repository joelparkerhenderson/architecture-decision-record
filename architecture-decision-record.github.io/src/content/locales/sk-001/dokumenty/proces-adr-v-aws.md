# Proces záznamov architektonických rozhodnutí v AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Záznam architektonického rozhodnutia (ADR) je dokument, ktorý opisuje voľbu, ktorú tím urobí o významnom aspekte softvérovej architektúry, ktorú plánuje vybudovať. Každý ADR opisuje architektonické rozhodnutie, jeho kontext a jeho dôsledky. ADR majú stavy, a preto sledujú životný cyklus. Príklad ADR nájdete v prílohe.

Výstupom procesu ADR je zbierka záznamov architektonických rozhodnutí. Táto zbierka tvorí denník rozhodnutí. Denník rozhodnutí poskytuje kontext projektu, ako aj podrobné informácie o implementácii a návrhu. Členovia projektu preletia nadpisy každého ADR, aby získali prehľad o kontexte projektu. Čítajú ADR, aby sa hlboko ponorili do implementácií projektu a návrhových rozhodnutí.

Keď tím prijme ADR, stane sa nemenným. Ak nové poznatky vyžadujú iné rozhodnutie, tím navrhne nový ADR. Keď tím prijme nový ADR, nahradí predchádzajúci ADR.

## Rozsah procesu ADR

Členovia projektu by mali vytvoriť ADR pre každé architektonicky významné rozhodnutie, ktoré ovplyvňuje softvérový projekt alebo produkt, vrátane nasledujúcich (Richards and Ford 2020):

* Štruktúra (napríklad vzory ako mikroslužby)

* Nefunkčné požiadavky (bezpečnosť, vysoká dostupnosť a odolnosť voči chybám)

* Závislosti (väzba komponentov)

* Rozhrania (API a publikované zmluvy)

* Techniky budovania (knižnice, frameworky, nástroje a procesy)

* Funkčné a nefunkčné požiadavky sú najčastejšími vstupmi do procesu ADR.


## Obsah ADR

Keď tím identifikuje potrebu ADR, člen tímu začne písať ADR na základe šablóny platnej pre celý projekt. (Príklady šablón nájdete v organizácii ADR na GitHube.) Šablóna zjednodušuje tvorbu ADR a zaisťuje, že ADR zachytáva všetky relevantné informácie. Každý ADR by mal minimálne definovať kontext rozhodnutia, samotné rozhodnutie a dôsledky rozhodnutia pre projekt a jeho výstupy. (Príklady týchto sekcií nájdete v prílohe.) Jedným z najsilnejších aspektov štruktúry ADR je, že sa zameriava na dôvod rozhodnutia, nie na to, ako ho tím implementoval. Pochopenie, prečo tím rozhodnutie urobil, uľahčuje ostatným členom tímu jeho prijatie a bráni ďalším architektom, ktorí sa nezúčastnili na procese rozhodovania, aby toto rozhodnutie v budúcnosti zrušili.


## Proces prijímania ADR

Každý člen tímu môže vytvoriť ADR, ale tím by mal stanoviť definíciu vlastníctva ADR. Každý autor, ktorý je vlastníkom ADR, by mal aktívne udržiavať a komunikovať obsah ADR. Aby sa toto vlastníctvo objasnilo, táto príručka v nasledujúcich sekciách označuje autorov ADR ako vlastníkov ADR. Ostatní členovia tímu môžu k ADR vždy prispievať. Ak sa obsah ADR zmení predtým, ako ho tím prijme, vlastník by mal tieto zmeny schváliť.

Po tom, čo tím identifikuje architektonické rozhodnutie a jeho vlastníka, vlastník ADR na začiatku procesu poskytne ADR v stave **Navrhnuté**. ADR v stave Navrhnuté sú pripravené na revíziu.

Vlastník ADR potom iniciuje proces revízie ADR. Cieľom procesu revízie ADR je rozhodnúť, či tím ADR prijme, určí, že vyžaduje prepracovanie, alebo ADR zamietne. Projektový tím vrátane vlastníka ADR posúdi. Stretnutie k revízii by malo začať vyhradeným časovým úsekom na prečítanie ADR. V priemere by malo stačiť 10 až 15 minút. Počas tohto času každý člen tímu číta dokument a pridáva komentáre a otázky, aby označil nejasné témy. Po fáze revízie vlastník ADR prečíta nahlas a prediskutuje s tímom každý komentár.

Ak tím nájde akčné body na zlepšenie ADR, stav ADR zostane **Navrhnuté**. Vlastník ADR formuluje akcie a v spolupráci s tímom pridelí riešiteľa ku každej akcii. Každý člen tímu môže prispievať a riešiť akčné body. Zodpovednosťou vlastníka ADR je znovu naplánovať proces revízie.

Tím sa môže tiež rozhodnúť ADR zamietnuť. V takom prípade vlastník ADR pridá dôvod zamietnutia, aby sa predišlo budúcim diskusiám o rovnakej téme. Vlastník zmení stav ADR na **Zamietnuté**.

Ak tím ADR schváli, vlastník pridá časovú pečiatku, verziu a zoznam zainteresovaných strán. Vlastník potom aktualizuje stav na **Prijaté**.

ADR a denník rozhodnutí, ktorý vytvárajú, predstavujú rozhodnutia tímu a poskytujú históriu všetkých rozhodnutí. Tím používa ADR ako referenciu počas revízií kódu a architektúry, kde je to možné. Okrem vykonávania revízií kódu, návrhových úloh a implementačných úloh by sa členovia tímu mali s ADR radiť pri strategických rozhodnutiach o produkte.

Ako dobrá prax by mala každá softvérová zmena prejsť recenziami od kolegov a vyžadovať aspoň jedno schválenie. Počas revízie kódu môže recenzent nájsť zmeny, ktoré porušujú jeden alebo viac ADR. V takom prípade recenzent požiada autora zmeny kódu o aktualizáciu kódu a zdieľa odkaz na ADR. Keď autor kód aktualizuje, schvália ho recenzenti-kolegovia a zlúči sa do hlavnej kódovej základne.


## Proces revízie ADR

Tím by mal s ADR zaobchádzať ako s nemennými dokumentmi po tom, čo ich prijme alebo zamietne. Zmeny existujúceho ADR vyžadujú vytvorenie nového ADR, zavedenie procesu revízie pre nový ADR a schválenie ADR. Ak tím nový ADR schváli, vlastník by mal zmeniť stav starého ADR na **Nahradené**. 
