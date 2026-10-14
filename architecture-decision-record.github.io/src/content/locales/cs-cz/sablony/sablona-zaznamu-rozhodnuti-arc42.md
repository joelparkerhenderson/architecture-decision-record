# Šablona záznamu rozhodnutí od arc42

<https://arc42.org/overview>

## 1. Úvod a cíle

Stručný popis požadavků, hnacích sil, výtah (nebo shrnutí) požadavků. Tři (nejvýše
pět) nejdůležitějších cílů kvality architektury, které mají nejvyšší prioritu pro
hlavní zainteresované strany. Tabulka důležitých zainteresovaných stran s jejich
očekáváními ohledně architektury.

## 1.1 Přehled požadavků

### Obsah

Stručný popis funkčních požadavků, hnacích sil, výtah (nebo shrnutí) požadavků.
Odkazy na (doufejme existující) dokumenty požadavků s informací, kde je najít. 

### Motivace

Z pohledu koncových uživatelů se systém vytváří nebo upravuje, aby lépe podporoval
podnikovou činnost a/nebo zlepšil kvalitu. 

### Forma

Krátký textový popis, pravděpodobně v tabulkovém formátu případů užití. Pokud
existují dokumenty požadavků, měl by tento přehled na tyto dokumenty odkazovat.

Tyto výtahy udržujte co nejkratší. Vyvažte čitelnost tohoto dokumentu s potenciální
redundancí vůči dokumentům požadavků. 

## 1.2 Cíle kvality

### Obsah

Tři (nejvýše pět) nejdůležitějších cílů kvality architektury, jejichž naplnění je
pro hlavní zainteresované strany nejdůležitější. Opravdu máme na mysli cíle kvality
pro architekturu. Nepleťte si je s cíli projektu. Nemusejí být totožné. Norma
ISO 25010 poskytuje pěkný přehled potenciálně zajímavých témat.

### Motivace

Měli byste znát cíle kvality svých nejdůležitějších zainteresovaných stran, protože
ovlivní zásadní architektonická rozhodnutí. Buďte u těchto kvalit velmi konkrétní,
vyhýbejte se módním slovům. Pokud vy jako architekt nevíte, jak bude kvalita vaší
práce posuzována …

### Forma

Tabulka s nejdůležitějšími cíli kvality a konkrétními scénáři, seřazená podle priorit.

## 1.3 Zainteresované strany

### Obsah

Výslovný přehled zainteresovaných stran systému, tedy všech osob, rolí nebo
organizací, které

- by měly znát architekturu

- je třeba přesvědčit o architektuře

- musí pracovat s architekturou nebo s kódem

- potřebují dokumentaci architektury pro svou práci

- musí činit rozhodnutí o systému nebo jeho vývoji

### Motivace

Měli byste znát všechny strany zapojené do vývoje systému nebo dotčené systémem.
Jinak vás mohou později ve vývojovém procesu čekat nepříjemná překvapení. Tyto
zainteresované strany určují rozsah a úroveň detailu vaší práce a jejích výsledků.

### Forma

Tabulka s názvy rolí, jmény osob a jejich očekáváními ve vztahu k architektuře
a její dokumentaci.

## 2. Omezení

Cokoli, co omezuje týmy v rozhodnutích o návrhu a implementaci nebo v rozhodnutích
o souvisejících procesech. Někdy mohou přesahovat jednotlivé systémy a platit pro
celé organizace a společnosti.

### Obsah

Jakýkoli požadavek, který omezuje softwarové architekty ve svobodě návrhu
a implementačních rozhodnutí nebo v rozhodnutí o vývojovém procesu. Tato omezení
někdy přesahují jednotlivé systémy a platí pro celé organizace a společnosti.

### Motivace

Architekti by měli přesně vědět, kde jsou při svých návrhových rozhodnutích
svobodní a kde musí dodržovat omezení. S omezeními je třeba se vždy vypořádat;
mohou být však vyjednatelná.

### Forma

Jednoduché tabulky omezení s vysvětleními. V případě potřeby je můžete rozdělit
na technická omezení, organizační a politická omezení a konvence (např. pokyny
pro programování nebo verzování, konvence dokumentace nebo pojmenování)

## 3. Kontext a rozsah

Vymezuje váš systém od jeho (vnějších) komunikačních partnerů (sousední systémy
a uživatelé). Specifikuje vnější rozhraní. Zobrazeno z obchodní/doménové perspektivy
(vždy) nebo technické perspektivy (volitelné)

### Obsah

Rozsah a kontext systému — jak název napovídá — vymezuje váš systém (tedy váš
rozsah) od všech jeho komunikačních partnerů (sousední systémy a uživatelé, tedy
kontext vašeho systému). Tím specifikuje vnější rozhraní.

V případě potřeby odlište obchodní kontext (vstupy a výstupy specifické pro doménu)
od technického kontextu (kanály, protokoly, hardware).

### Motivace

Doménová a technická rozhraní ke komunikačním partnerům patří k nejkritičtějším
aspektům vašeho systému. Ujistěte se, že jim plně rozumíte.

### Forma

- Různé kontextové diagramy

- Seznamy komunikačních partnerů a jejich rozhraní.

## 3.1 Obchodní kontext

### Obsah

Specifikace všech komunikačních partnerů (uživatelé, IT systémy, …) s vysvětlením
vstupů a výstupů nebo rozhraní specifických pro doménu. Volitelně můžete přidat
formáty specifické pro doménu nebo komunikační protokoly.

### Motivace

Všechny zainteresované strany by měly rozumět tomu, jaká data se vyměňují
s prostředím systému.

### Forma

Všechny druhy diagramů, které ukazují systém jako černou skříňku a specifikují
doménová rozhraní ke komunikačním partnerům.

Alternativně (nebo dodatečně) můžete použít tabulku. Titulek tabulky je název
vašeho systému, tři sloupce obsahují název komunikačního partnera, vstupy a výstupy.

## 3.2 Technický kontext

### Obsah

Technická rozhraní (kanály a přenosová média) propojující váš systém s jeho
prostředím. Navíc mapování doménově specifických vstupů/výstupů na kanály, tedy
vysvětlení, který vstup/výstup používá který kanál.

### Motivace

Mnoho zainteresovaných stran činí architektonická rozhodnutí na základě technických
rozhraní mezi systémem a jeho kontextem. Zejména návrháři infrastruktury nebo
hardwaru o těchto technických rozhraních rozhodují.

### Forma

Např. diagram nasazení UML popisující kanály k sousedním systémům spolu
s mapovací tabulkou ukazující vztahy mezi kanály a vstupem/výstupem.

## 4. Strategie řešení

Shrnutí zásadních rozhodnutí a strategií řešení, které utvářejí architekturu.
Může zahrnovat technologii, dekompozici nejvyšší úrovně, přístupy k dosažení
nejdůležitějších cílů kvality a relevantní organizační rozhodnutí.

### Obsah

Stručné shrnutí a vysvětlení zásadních rozhodnutí a strategií řešení, které utvářejí
architekturu systému. Patří sem

- technologická rozhodnutí

- rozhodnutí o dekompozici systému nejvyšší úrovně, např. použití architektonického vzoru nebo návrhového vzoru

- rozhodnutí o tom, jak dosáhnout klíčových cílů kvality

- relevantní organizační rozhodnutí, např. výběr vývojového procesu nebo delegování určitých úkolů na třetí strany.

### Motivace

Tato rozhodnutí tvoří základní kameny vaší architektury. Jsou základem pro mnoho
dalších podrobných rozhodnutí nebo implementačních pravidel.

### Forma

Vysvětlení těchto klíčových rozhodnutí udržujte krátké.

Zdůvodněte, co jste rozhodli a proč jste se tak rozhodli, na základě svého popisu
problému, cílů kvality a klíčových omezení. Odkazujte na podrobnosti v následujících
sekcích (sekce 5 pro strukturální podrobnosti, sekce 8 pro průřezové koncepty).

Můžete použít seznam přístupů k řešení nebo tabulku.

## 5. Pohled stavebních bloků

Statická dekompozice systému, abstrakce zdrojového kódu, zobrazená jako hierarchie
bílých skříněk (obsahujících černé skříňky), až do vhodné úrovně detailu.

### Obsah

Pohled stavebních bloků ukazuje statickou dekompozici systému na stavební bloky
(moduly, komponenty, podsystémy, třídy, rozhraní, balíčky, knihovny, frameworky,
vrstvy, oddíly, úrovně, funkce, makra, operace, datové struktury, …) a jejich
závislosti (vztahy, asociace, …)

Tento pohled je povinný pro každou dokumentaci architektury. Analogicky k domu je
to půdorys.

### Motivace

Udržujte přehled o svém zdrojovém kódu tím, že jeho strukturu učiníte srozumitelnou
pomocí abstrakce.

To vám umožní komunikovat se zainteresovanými stranami na abstraktní úrovni
bez odhalování implementačních podrobností.

### Forma

Pohled stavebních bloků je hierarchická sbírka černých a bílých skříněk (viz
obrázek níže) a jejich popisů.

## 5.1 Bílá skříňka — celý systém

Zde popisujete dekompozici celého systému pomocí následující šablony bílé skříňky.
Obsahuje

- přehledový diagram

- motivaci dekompozice

- popisy černých skříněk obsažených stavebních bloků. K tomu nabízíme alternativy:

  - použijte jednu tabulku pro stručný a pragmatický přehled všech obsažených stavebních bloků a jejich rozhraní

  - použijte seznam popisů černých skříněk stavebních bloků podle šablony černé skříňky (viz níže). V závislosti na zvoleném nástroji může být tento seznam tvořen podkapitolami (v textových souborech), podstránkami (ve Wiki) nebo vnořenými prvky (v modelovacím nástroji).

  - (volitelně:) důležitá rozhraní, která nejsou vysvětlena v šablonách černé skříňky stavebního bloku, ale jsou velmi důležitá pro pochopení bílé skříňky.

Protože existuje tolik způsobů specifikace rozhraní, neposkytujeme pro ně
konkrétní šablonu.

V nejlepším případě vystačíte s příklady nebo jednoduchými signaturami.

## 5.2 Úroveň 2

Zde můžete specifikovat vnitřní strukturu (některých) stavebních bloků z úrovně 1
jako bílé skříňky.

Musíte rozhodnout, které stavební bloky vašeho systému jsou dostatečně důležité,
aby ospravedlnily tak podrobný popis. Preferujte relevanci před úplností.
Specifikujte důležité, překvapivé, rizikové, složité nebo nestálé stavební bloky.
Vynechte normální, jednoduché, nudné nebo standardizované části vašeho systému

### 5.2.1 Bílá skříňka pro stavební blok 1

Specifikuje vnitřní strukturu stavebního bloku 1.

Použijte šablonu bílé skříňky (viz výše).

## 6. Pohled běhu

Chování stavebních bloků jako scénáře pokrývající důležité případy užití nebo
funkce, interakce na kritických vnějších rozhraních, provoz a správu plus chování
při chybách a výjimkách.

### Obsah

Pohled běhu popisuje konkrétní chování a interakce stavebních bloků systému
formou scénářů z následujících oblastí:

- důležité případy užití nebo funkce: jak je stavební bloky provádějí?

- interakce na kritických vnějších rozhraních: jak stavební bloky spolupracují s uživateli a sousedními systémy?

- provoz a správa: spuštění, start, zastavení

- chybové a výjimečné scénáře

Poznámka: Hlavním kritériem pro výběr možných scénářů (sekvencí, pracovních postupů) je jejich architektonická relevance. Není důležité popisovat velký počet scénářů. Spíše zdokumentujte reprezentativní výběr.

### Motivace

Měli byste rozumět tomu, jak (instance) stavebních bloků vašeho systému plní svou práci a komunikují za běhu. Ve své dokumentaci budete scénáře zachycovat hlavně proto, abyste sdělili svou architekturu zainteresovaným stranám, které jsou méně ochotny nebo schopny číst a chápat statické modely (pohled stavebních bloků, pohled nasazení).

### Forma

Existuje mnoho notací pro popis scénářů, např.


- číslovaný seznam kroků (v přirozeném jazyce)

- diagramy aktivit nebo vývojové diagramy

- sekvenční diagramy

- BPMN nebo EPC (událostmi řízené procesní řetězce)

- stavové automaty

- atd.

## 6.n Scénář běhu n (1, 2, 3 atd.)

Vložte diagram běhu nebo textový popis scénáře.

Vložte popis pozoruhodných aspektů interakcí mezi instancemi stavebních bloků znázorněnými v tomto diagramu.

## 7. Pohled nasazení

Technická infrastruktura s prostředími, počítači, procesory, topologiemi.
Mapování (softwarových) stavebních bloků na prvky infrastruktury.

### Obsah

Pohled nasazení popisuje:

- technickou infrastrukturu používanou ke spouštění vašeho systému, s prvky
  infrastruktury jako zeměpisné polohy, prostředí, počítače, procesory,
  kanály a síťové topologie a další prvky infrastruktury, a

- mapování (softwarových) stavebních bloků na tyto prvky infrastruktury.

Systémy se často spouštějí v různých prostředích, např. vývojové prostředí,
testovací prostředí, produkční prostředí. V takových případech byste měli
zdokumentovat všechna relevantní prostředí.

Pohled nasazení dokumentujte zejména tehdy, když váš software běží jako
distribuovaný systém s více než jedním počítačem, procesorem, serverem nebo
kontejnerem nebo když navrhujete a konstruujete vlastní hardwarové procesory
a čipy.

Z pohledu softwaru stačí zachytit ty prvky infrastruktury, které jsou potřeba
k ukázání nasazení vašich stavebních bloků. Hardwaroví architekti mohou jít dál
a popsat infrastrukturu do jakékoli úrovně detailu, kterou potřebují zachytit. 

### Motivace

Software bez hardwaru neběží. Tato základní infrastruktura může a bude ovlivňovat
váš systém a/nebo některé průřezové koncepty. Proto potřebujete infrastrukturu znát.

### Forma

Možná je diagram nasazení nejvyšší úrovně již obsažen v sekci 3.2 jako technický kontext s vaší vlastní infrastrukturou jako JEDNOU černou skříňkou. V této sekci tuto černou skříňku přiblížíte pomocí dalších diagramů nasazení.

- UML nabízí diagramy nasazení k vyjádření tohoto pohledu. Použijte ho, pravděpodobně s vnořenými diagramy, když je vaše infrastruktura složitější.

- Když vaše (hardwarové) zainteresované strany preferují jiné druhy diagramů
  než diagram nasazení UML, nechte je použít jakýkoli druh, který dokáže ukázat
  uzly a kanály infrastruktury.

## 7.1 Infrastruktura úroveň 1

Popište (obvykle kombinací diagramů, tabulek a textu):

- rozložení vašeho systému do více lokalit, prostředí, počítačů, procesorů, .. a také fyzická spojení mezi nimi

- důležité zdůvodnění nebo motivaci pro tuto strukturu nasazení

- vlastnosti kvality a/nebo výkonu infrastruktury

- mapování softwarových artefaktů (stavebních bloků) na prvky infrastruktury

Pro více prostředí nebo alternativních nasazení zkopírujte tuto sekci arc42 pro všechna relevantní prostředí. **

## 7.2 Infrastruktura úroveň 2

Zde můžete zahrnout vnitřní strukturu (některých) prvků infrastruktury z úrovně 1 infrastruktury.

Zkopírujte strukturu z úrovně 1 pro každý vybraný prvek.

## 8. Průřezové koncepty

Celkové, základní předpisy a přístupy k řešení relevantní ve více částech
(→ průřezově) systému. Koncepty se často vztahují k více stavebním blokům.
Zahrnují různá témata jako doménové modely, architektonické vzory a styly,
pravidla pro používání konkrétní technologie a implementační pravidla.

### Obsah

Tato sekce popisuje průřezové koncepty (praktiky, vzory, předpisy nebo nápady
na řešení). Takové koncepty se často vztahují k více stavebním blokům.
Mohou zahrnovat mnoho různých témat.

### Motivace

Koncepty tvoří základ koncepční integrity (konzistence, homogenity)
architektury. Jsou tedy důležitým příspěvkem k dosažení vnitřních kvalit vašeho
systému.

Toto je místo v šabloně, které jsme poskytli pro ucelenou specifikaci takových
konceptů.

Mnoho z těchto konceptů se vztahuje k několika vašim stavebním blokům nebo je ovlivňuje.

### Forma

Forma může být různá:

- koncepční dokumenty s jakoukoli strukturou

- ukázkové implementace, zejména pro technické koncepty

- průřezové výtahy z modelů nebo scénáře využívající notace architektonických pohledů

### Struktura této sekce

Vyberte jen témata nejpotřebnější pro váš systém a každému přiřaďte nadpis úrovně 2 v této sekci (např. 8.1, 8.2 atd.).

- NEPOKOUŠEJTE SE pokrýt všechna témata výše zmíněného diagramu.

### Pozadí

Některá témata v systémech se často týkají více stavebních bloků, hardwarových
prvků nebo vývojových procesů. Může být snazší sdělit nebo zdokumentovat taková
průřezová témata na centrálním místě, místo abyste je opakovali v popisu
dotčených stavebních bloků, hardwarových prvků nebo vývojových procesů.

Některé koncepty se mohou týkat všech prvků systému, jiné mohou být relevantní
jen pro několik.

## 9. Architektonická rozhodnutí

Důležitá, nákladná, kritická, rozsáhlá nebo riziková architektonická rozhodnutí
včetně zdůvodnění.

### Obsah

Důležitá, nákladná, rozsáhlá nebo riziková architektonická rozhodnutí včetně
zdůvodnění. Pod „rozhodnutími“ rozumíme výběr jedné alternativy na základě daných
kritérií.

Použijte svůj úsudek k rozhodnutí, zda by architektonické rozhodnutí mělo být
zdokumentováno zde, v této centrální sekci, nebo je lepší ho zdokumentovat
lokálně (např. v šabloně bílé skříňky jednoho stavebního bloku). Vyhněte se
redundantním textům. Odkažte na sekci 4, kde jste již zachytili nejdůležitější
rozhodnutí své architektury.

### Motivace

Zainteresované strany vašeho systému by měly být schopny vaše rozhodnutí pochopit
a zpětně sledovat.

### Forma

- ADR (záznam architektonického rozhodnutí) pro každé důležité rozhodnutí

- seznam nebo tabulka seřazená podle důležitosti a důsledků nebo

- podrobněji formou samostatných sekcí pro každé rozhodnutí

### Pozadí (k ADR)

Menší kusy dokumentace se snáze čtou, vytvářejí a udržují. U architektonických
rozhodnutí vývojové týmy často:

- o rozhodnutí vědí, protože je viditelné např. ve zdrojovém kódu, ale

- chybí jim motivace za tímto rozhodnutím (viz Nygard 2011)

Proto byste měli zdokumentovat několik důležitých rozhodnutí spolu s jejich
motivací a zdůvodněním

### Náš návrh týkající se rozhodnutí

Veďte sbírku architektonicky významných rozhodnutí, tedy těch rozhodnutí, která
ovlivňují strukturu, vlastnosti kvality, důležité (zejména vnější) závislosti
a rozhraní nebo techniky konstrukce (díky Michaelu Nygardovi za tento návrh).

## 10. Požadavky na kvalitu

Požadavky na kvalitu jako scénáře, se stromem kvality poskytujícím přehled
na vysoké úrovni. Nejdůležitější cíle kvality měly být popsány v sekci
1.2. (cíle kvality).

### Obsah

Tato sekce obsahuje všechny relevantní požadavky na kvalitu.

Nejdůležitější z těchto požadavků již byly popsány v sekci 1.2. (cíle kvality),
proto by se zde na ně mělo pouze odkazovat. V této sekci 10 byste měli zachytit
také požadavky na kvalitu menší důležitosti, které nevytvoří velká rizika, pokud
nebudou plně dosaženy (ale mohou být žádoucí).

### Motivace

Protože požadavky na kvalitu budou mít velký vliv na architektonická rozhodnutí,
měli byste vědět, jaké kvality jsou pro vaše zainteresované strany skutečně
důležité, konkrétním a měřitelným způsobem.

### Další informace

Viz rozsáhlý model kvality Q42 na https://quality.arc42.org.

## 10.1 Přehled požadavků na kvalitu

### Obsah

Přehled nebo shrnutí požadavků na kvalitu.

### Motivace

Často se setkáváme s desítkami (nebo dokonce stovkami) podrobných požadavků na
kvalitu. V této přehledové sekci byste se je měli pokusit shrnout, např.
popisem kategorií nebo témat (jak navrhuje ISO 25010:2023 nebo Q42

Pokud jsou tyto souhrnné popisy již dostatečně přesné, konkrétní a měřitelné,
můžete sekci 10.2 vynechat.

### Forma

Použijte jednoduchou tabulku, ve které každý řádek obsahuje kategorii nebo téma
a krátký popis požadavku na kvalitu. Alternativně můžete k uspořádání těchto
požadavků na kvalitu použít myšlenkovou mapu.

V literatuře byla také popsána myšlenka stromu atributů kvality, který staví
obecný pojem „kvalita“ do role kořene a používá stromové zjemňování pojmu
„kvalita“. [Bass+21] pro tento účel zavedl pojem „Quality Attribute Utility
Tree“.

## 10.2 Scénáře kvality

### Obsah

Scénáře kvality konkretizují požadavky na kvalitu a umožňují rozhodnout, zda jsou
splněny (ve smyslu akceptačních kritérií). Zajistěte, aby vaše scénáře byly
konkrétní a měřitelné.

Zvlášť užitečné jsou dva druhy scénářů:

- Scénáře užití (nazývané také aplikační scénáře nebo scénáře případů užití)
  popisují reakci systému za běhu na určitý podnět. Zahrnují i scénáře popisující
  efektivitu nebo výkon systému. Příklad: Systém reaguje na požadavek uživatele
  do jedné sekundy.

- Scénáře změn popisují požadovaný efekt úpravy nebo rozšíření systému nebo jeho
  bezprostředního okolí. Příklad: Implementuje se další funkcionalita nebo se
  změní požadavky na atribut kvality a měří se úsilí nebo doba trvání změny.

### Forma

Typické informace pro podrobné scénáře zahrnují následující:

V krátké formě (preferované v modelu Q42):

- Kontext/Pozadí: Jaký druh systému nebo komponenty, jaké je prostředí nebo situace?

- Zdroj/Podnět: Kdo nebo co iniciuje nebo spouští chování, reakci nebo akci.

- Metrika/Akceptační kritéria: Odpověď včetně míry nebo metriky

Dlouhá forma scénářů (preferovaná SEI a [Bass+21]) je podrobnější a zahrnuje následující informace:

- ID scénáře: Jedinečný identifikátor scénáře.

- Název scénáře: Krátký popisný název scénáře.

- Zdroj: Entita (uživatel, systém nebo událost), která scénář iniciuje.

- Podnět: Spouštěcí událost nebo podmínka, kterou musí systém řešit.

- Prostředí: Provozní kontext nebo podmínka, za které systém podnět zažívá.

- Artefakt: Stavební bloky nebo jiné prvky systému ovlivněné podnětem.

- Odpověď: Výsledek nebo chování, které systém projevuje v reakci na podnět.

- Míra odpovědi: Kritéria nebo metrika, podle které se hodnotí odpověď systému.

### Viz také

Od ledna 2023 poskytuje arc42 pragmatický model kvality, který navrhuje
označovat požadavky na kvalitu hashtagy nebo štítky jako #flexible, #efficient,
#usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Rizika a technický dluh

Známá technická rizika nebo technický dluh. Jaké potenciální problémy existují
v systému nebo kolem něj? S čím se vývojový tým necítí dobře?

### Obsah

Seznam identifikovaných technických rizik nebo technických dluhů seřazený podle
priority

### Motivace

„Řízení rizik je projektové řízení pro dospělé“ (Tim Lister, Atlantic
Systems Guild.)

Toto by mělo být vaše motto pro systematické odhalování a hodnocení rizik
a technických dluhů v architektuře, které budou potřebovat manažerské
zainteresované strany (např. projektoví manažeři, vlastníci produktu) jako součást
celkové analýzy rizik a plánování opatření.

### Forma

Seznam rizik a/nebo technických dluhů, pravděpodobně včetně navrhovaných opatření
k minimalizaci, zmírnění nebo vyhnutí se rizikům nebo ke snížení technických dluhů.
