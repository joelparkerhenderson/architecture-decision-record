# Šablóna záznamu rozhodnutia od Jeffa Tyreeho a Arta Akermana

Toto je šablóna opisu architektonického rozhodnutia publikovaná v ["Architecture Decisions: Demystifying Architecture" od Jeffa Tyreeho a Arta Akermana, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Problém**: Opíšte problém architektonického návrhu, ktorý riešite, a nenechajte žiadne otázky o tom, prečo ho riešite práve teraz. Podľa minimalistického prístupu riešte a dokumentujte iba problémy, ktoré treba riešiť v rôznych bodoch životného cyklu.

* **Rozhodnutie**: Jasne uveďte smerovanie architektúry – teda pozíciu, ktorú ste zvolili.

* **Stav**: Stav rozhodnutia, napríklad čakajúce, rozhodnuté alebo schválené.

* **Skupina**: Na usporiadanie súboru rozhodnutí môžete použiť jednoduché zoskupenie – napríklad integrácia, prezentácia, dáta a pod. Môžete použiť aj sofistikovanejšiu architektonickú ontológiu, ako je ontológia Johna Kyaruziho a Jana van Katwijka, ktorá zahŕňa abstraktnejšie kategórie ako udalosť, kalendár a miesto. Napríklad pri tejto ontológii by ste rozhodnutia, ktoré sa zaoberajú výskytmi, kde systém vyžaduje informácie, zoskupili pod udalosť.

* **Predpoklady**: Jasne opíšte základné predpoklady v prostredí, v ktorom rozhodnutie robíte – náklady, harmonogram, technológia a pod. Všimnite si, že obmedzenia prostredia (ako akceptované technologické štandardy, podniková architektúra, bežne používané vzory a pod.) môžu obmedziť alternatívy, ktoré zvažujete.

* **Obmedzenia**: Zachyťte všetky dodatočné obmedzenia prostredia, ktoré môže zvolená alternatíva (rozhodnutie) priniesť.

* **Pozície**: Uveďte pozície (životaschopné možnosti alebo alternatívy), ktoré ste zvažovali. Tie si často vyžadujú dlhé vysvetlenia, niekedy dokonca modely a diagramy. Nejde o vyčerpávajúci zoznam. Nechcete však počuť otázku „Premýšľali ste o...?“ počas záverečnej revízie; to vedie k strate dôveryhodnosti a spochybňovaniu iných architektonických rozhodnutí. Táto sekcia tiež pomáha zabezpečiť, že ste si vypočuli názory ostatných; explicitné uvedenie iných názorov pomáha získať ich zástancov pre vaše rozhodnutie.

* **Argument**: Načrtnite, prečo ste zvolili pozíciu, vrátane položiek ako náklady na implementáciu, celkové náklady vlastníctva, čas uvedenia na trh a dostupnosť potrebných vývojových zdrojov. Toto je pravdepodobne rovnako dôležité ako samotné rozhodnutie.

* **Implikácie**: Rozhodnutie prináša mnoho implikácií, ako naznačuje metamodel REMAP. Rozhodnutie môže napríklad vyvolať potrebu urobiť ďalšie rozhodnutia, vytvoriť nové požiadavky alebo zmeniť existujúce požiadavky; priniesť dodatočné obmedzenia prostredia; vyžadovať opätovné vyjednávanie rozsahu alebo harmonogramu so zákazníkmi; alebo vyžadovať dodatočné školenie personálu. Jasné pochopenie a uvedenie implikácií vášho rozhodnutia môže byť veľmi účinné pri získavaní podpory a vytváraní plánu realizácie architektúry.

* **Súvisiace rozhodnutia**: Je zrejmé, že mnohé rozhodnutia spolu súvisia; môžete ich tu uviesť. Zistili sme však, že v praxi sú užitočnejšie matica sledovateľnosti, rozhodovacie stromy alebo metamodely. Metamodely sú užitočné na diagramové zobrazenie zložitých vzťahov (ako sú modely Rose).

* **Súvisiace požiadavky**: Rozhodnutia by mali byť riadené podnikaním. Aby ste preukázali zodpovednosť, explicitne priraďte svoje rozhodnutia k cieľom alebo požiadavkám. Tieto súvisiace požiadavky môžete vymenovať tu, ale zistili sme, že je pohodlnejšie odkazovať na maticu sledovateľnosti. Môžete posúdiť prínos každého architektonického rozhodnutia k splneniu každej požiadavky a potom posúdiť, ako dobre je požiadavka splnená naprieč všetkými rozhodnutiami. Ak rozhodnutie neprispieva k splneniu požiadavky, nerobte toto rozhodnutie.

* **Súvisiace artefakty**: Uveďte súvisiace architektonické dokumenty, dokumenty návrhu alebo rozsahu, ktoré toto rozhodnutie ovplyvňuje.

* **Súvisiace princípy**: Ak má podnik dohodnutý súbor princípov, uistite sa, že rozhodnutie je v súlade s jedným alebo viacerými z nich. To pomáha zabezpečiť zosúladenie naprieč doménami alebo systémami.

* **Poznámky**: Keďže proces rozhodovania môže trvať týždne, zistili sme, že je užitočné zachytávať poznámky a problémy, o ktorých tím diskutuje počas procesu socializácie.
