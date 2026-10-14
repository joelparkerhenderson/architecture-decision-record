# {Sem vložte svoj názov}

!!! info

    **Stav**: { Navrhnuté | V revízii | Prijaté |  Zamietnuté | Nahradené | Zastarané }
    
    **Aktualizované**: {YYYY-MM-DD}

## Zhrnutie

{Toto je „manažérske zhrnutie“ alebo „výťahový pitch“ pre váš ADR. V niekoľkých
stručných vetách (zvyčajne 2-4) jasne uveďte základný problém, otázku alebo
príležitosť, ktorú tento ADR rieši. Zahrňte krátky náznak prijatého rozhodnutia alebo
oblasti zamerania. Cieľom je pomôcť čitateľom rýchlo pochopiť, o čom tento ADR je
a rozhodnúť sa, či je pre nich relevantný, bez potreby čítať celý
dokument. Predstavte si ho ako abstrakt technického článku alebo veľmi krátky
úvod do hlavnej témy.}

## Hnacie sily

{Táto sekcia vysvetľuje, **prečo** sa toto rozhodnutie robí **teraz**. Jasne
sformulujte primárne motivácie, potreby alebo problémy, ktoré toto
architektonické rozhodnutie vyžadujú. Zamyslite sa nad základnými dôvodmi a tlakmi.}

* {napr. Vyvíjame novú funkciu/schopnosť, ktorá potrebuje...}

* {napr. Potrebujeme zlepšiť výkon, prístupnosť, odstrániť dlh...}

* {napr. Spätná väzba od používateľov naznačuje...}

* {napr. Súčasný prístup ukladá tieto obmedzenia...}

## Možnosti

{Tu uvádzate rôzne možnosti, ktoré zvažujete. Držte sa
faktov a vyhnite sa názorom, ďalšia sekcia pokrýva analýzu. Zahrňte
stručný opis, odkazy na relevantnú dokumentáciu alebo príklady.

Zahrňte všetky významné alternatívy, ktoré ste preskúmali, aj keď boli nakoniec
nezvolené. Cieľom je poskytnúť čitateľom jasné, nestranné pochopenie každej
alternatívy predtým, ako sa ponoríte do hodnotenia.}

### {Názov možnosti 1}

{Opíšte možnosť, poskytnite zhrnutie, uveďte fakty, poskytnite odkazy atď.}

### {Názov možnosti n}

...

## Analýza možností

{Tu kriticky hodnotíte každú možnosť uvedenú v sekcii *Možnosti*.
Pre každú možnosť poskytnite vyvážený pohľad na jej výhody,
nevýhody a akékoľvek ďalšie relevantné úvahy alebo kompromisy. Buďte konkrétni
a ak je to možné, vzťahujte svoje body späť k *Hnacím silám*.

Zvážte aspekty ako:

* Náklady (vývoj, prevádzka, licencovanie)

* Zložitosť (implementácia, údržba, krivka učenia)

* Riziká (technické, prevádzkové, bezpečnostné)

* Súlad s architektonickými princípmi alebo existujúcimi štandardmi

* Vplyv na výkon, škálovateľnosť, použiteľnosť, udržiavateľnosť,
    bezpečnosť atď.

Zahrňte toľko tvrdení Výhoda/Nevýhoda/Iné, koľko je potrebné.
}

### {Hodnotenie možnosti 1}

* Výhoda: {Konkrétna výhoda alebo prínos tejto možnosti.}

* Nevýhoda: {Konkrétna nevýhoda, riziko alebo náklad spojený s touto možnosťou.}

* Iné: {Relevantný bod, ktorý nie je striktne výhodou ani nevýhodou.}

### {Hodnotenie možnosti n}

...

## Odporúčanie

{Tu jasne uvedte konečné rozhodnutie a explicitne pomenujte
zvolenú možnosť. Podrobne vysvetlite, **prečo** bola táto možnosť zvolená.
Mali by ste jasne sformulovať, ako zvolená možnosť najlepšie rieši *Hnacie sily*
a spĺňa kľúčové požiadavky alebo rieši uvedený problém.}

### Dôsledky

{Táto sekcia je **voliteľná**.}

{Teraz, keď bolo rozhodnutie prijaté, aké sú očakávané výsledky a dopady,
pozitívne aj negatívne? Aké známe obmedzenia, náklady alebo riziká sa
akceptujú prijatím tohto rozhodnutia? Ako toto rozhodnutie ovplyvní rôzne
zainteresované strany, iné systémy, vývojové postupy, prevádzkové postupy alebo
používateľský zážitok?}

* Výhoda: {Konkrétny pozitívny výsledok alebo prínos očakávaný z tohto rozhodnutia.}

* Nevýhoda: {Konkrétna akceptovaná nevýhoda, náklad alebo riziko vyplývajúce z tohto
    rozhodnutia. }

* Iné: {Dôsledok, ktorý nie je striktne výhodou ani nevýhodou.}

### Potvrdenie

{Táto sekcia je **voliteľná**.}

{Načrtnite, ako sa overí implementácia tohto rozhodnutia a ako sa
zabezpečí priebežný súlad. To pomáha preukázať, že rozhodnutie
nie je len teoretické, ale bude aktívne uplatňované a monitorované.

Ako skontrolujete, že rozhodnutie bolo správne implementované? (napr. revízie kódu,
konkrétne testy, demonštrácie, recenzia kolegov).

Ako sa bude dodržiavanie tohto rozhodnutia udržiavať v čase? (napr. automatizované
kontroly, pravidelné audity, aktualizácie usmernení tímu, školenia).

Existujú konkrétne metriky alebo ukazovatele, ktoré preukážu, že rozhodnutie
dosahuje zamýšľané pozitívne výsledky? (napr. referenčné hodnoty výkonu,
miery prijatia, zníženie konkrétnych chýb, skóre spätnej väzby používateľov).

Kto je zodpovedný za dohľad nad tým a čo sa stane, ak sa rozhodnutie
nedodržiava?}

## Ďalšie informácie

{Táto sekcia je **voliteľná**.}

{Použite túto sekciu na poskytnutie doplňujúcich informácií, ktoré podporujú
rozhodnutie, dopĺňajú kontext alebo usmerňujú budúce kroky. Môžu sa tu objaviť aj odkazy na iné rozhodnutia a
zdroje.

Môžete stručne uviesť, kto sa podieľal na procese rozhodovania a
či/ako sa dosiahol konsenzus. Môžete tiež navrhnúť časový rámec alebo
konkrétne udalosti, ktoré by mohli podnietiť prehodnotenie tohto rozhodnutia v
budúcnosti.}
