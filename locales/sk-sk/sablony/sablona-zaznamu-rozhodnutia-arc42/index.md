# Šablóna záznamu rozhodnutia od arc42

<https://arc42.org/overview>

## 1. Úvod a ciele

Stručný opis požiadaviek, hnacích síl, výťah (alebo abstrakt) požiadaviek.
Tri (maximálne päť) cieľov kvality architektúry, ktoré majú
najvyššiu prioritu pre hlavné zainteresované strany. Tabuľka dôležitých zainteresovaných strán
s ich očakávaniami voči architektúre.

## 1.1 Prehľad požiadaviek

### Obsah

Stručný opis funkčných požiadaviek, hnacích síl, výťah (alebo
abstrakt) požiadaviek. Odkazy na (dúfajme existujúce) dokumenty
požiadaviek s informáciou, kde ich nájsť. 

### Motivácia

Z pohľadu koncových používateľov sa systém vytvára alebo mení, aby
zlepšil podporu obchodnej činnosti a/alebo zlepšil kvalitu. 

### Forma

Stručný textový opis, pravdepodobne vo forme tabuľky prípadov použitia. Ak dokumenty
požiadaviek existujú, tento prehľad by sa mal na ne odvolávať.

Tieto výňatky držte čo najkratšie. Vyvážte čitateľnosť tohto dokumentu
s potenciálnou redundanciou voči dokumentom požiadaviek. 

## 1.2 Ciele kvality

### Obsah

Tri (maximálne päť) cieľov kvality architektúry, ktorých splnenie je
najdôležitejšie pre hlavné zainteresované strany. Skutočne máme na mysli ciele kvality
architektúry. Nemýľte si ich s cieľmi projektu. Nie sú
nevyhnutne totožné. Norma ISO 25010 poskytuje pekný prehľad
potenciálnych tém záujmu.

### Motivácia

Mali by ste poznať ciele kvality svojich najdôležitejších zainteresovaných strán, pretože
ovplyvnia základné architektonické rozhodnutia. Buďte veľmi
konkrétni, pokiaľ ide o tieto kvality, vyhýbajte sa módnym slovám. Ak vy ako architekt neviete,
ako bude kvalita vašej práce posudzovaná …

### Forma

Tabuľka s najdôležitejšími cieľmi kvality a konkrétnymi scenármi, zoradená podľa priorít.

## 1.3 Zainteresované strany

### Obsah

Explicitný prehľad zainteresovaných strán systému, t. j. všetkých osôb, rolí alebo
organizácií, ktoré

- by mali poznať architektúru

- musia byť o architektúre presvedčené

- musia pracovať s architektúrou alebo s kódom

- potrebujú dokumentáciu architektúry pre svoju prácu

- musia prísť s rozhodnutiami o systéme alebo jeho vývoji

### Motivácia

Mali by ste poznať všetky strany zapojené do vývoja systému alebo ovplyvnené
systémom. Inak môžete neskôr v procese vývoja zažiť nepríjemné prekvapenia.
Tieto zainteresované strany určujú rozsah a úroveň detailu vašej
práce a jej výsledkov.

### Forma

Tabuľka s názvami rolí, menami osôb a ich očakávaniami voči
architektúre a jej dokumentácii.

## 2. Obmedzenia

Čokoľvek, čo obmedzuje tímy pri rozhodnutiach o návrhu a implementácii alebo rozhodnutiach
o súvisiacich procesoch. Môžu niekedy presahovať jednotlivé systémy a
platiť pre celé organizácie a spoločnosti.

### Obsah

Každá požiadavka, ktorá obmedzuje softvérových architektov v ich slobode rozhodovania o návrhu
a implementácii alebo rozhodnutiach o vývojovom procese. Tieto
obmedzenia niekedy presahujú jednotlivé systémy a platia pre celé
organizácie a spoločnosti.

### Motivácia

Architekti by mali presne vedieť, kde sú vo svojich návrhových rozhodnutiach slobodní
a kde sa musia držať obmedzení. S obmedzeniami sa treba vždy vysporiadať;
môžu však byť predmetom rokovania.

### Forma

Jednoduché tabuľky obmedzení s vysvetleniami. Ak je to potrebné, môžete ich rozdeliť
na technické obmedzenia, organizačné a politické obmedzenia a
konvencie (napr. smernice pre programovanie alebo verzovanie, konvencie dokumentácie alebo pomenovania)

## 3. Kontext a rozsah

Vymedzuje váš systém voči jeho (externým) komunikačným partnerom (susedné
systémy a používatelia). Určuje externé rozhrania. Zobrazuje sa z
obchodnej/doménovej perspektívy (vždy) alebo technickej perspektívy (voliteľne)

### Obsah

Rozsah a kontext systému – ako názov napovedá – vymedzuje váš systém (t. j.
váš rozsah) voči všetkým jeho komunikačným partnerom (susedné systémy a používatelia,
t. j. kontext vášho systému). Tým určuje externé rozhrania.

V prípade potreby rozlíšte obchodný kontext (doménovo špecifické vstupy a
výstupy) od technického kontextu (kanály, protokoly, hardvér).

### Motivácia

Doménové rozhrania a technické rozhrania ku komunikačným partnerom patria
medzi najkritickejšie aspekty vášho systému. Uistite sa, že im úplne
rozumiete.

### Forma

- Rôzne kontextové diagramy

- Zoznamy komunikačných partnerov a ich rozhraní.

## 3.1 Obchodný kontext

### Obsah

Špecifikácia všetkých komunikačných partnerov (používatelia, IT systémy, …) s
vysvetleniami doménovo špecifických vstupov a výstupov alebo rozhraní. Voliteľne môžete
pridať doménovo špecifické formáty alebo komunikačné protokoly.

### Motivácia

Všetky zainteresované strany by mali rozumieť, aké dáta sa vymieňajú s prostredím
systému.

### Forma

Všetky druhy diagramov, ktoré zobrazujú systém ako čiernu skrinku a určujú doménové
rozhrania ku komunikačným partnerom.

Alternatívne (alebo dodatočne) môžete použiť tabuľku. Názov tabuľky je
názov vášho systému, tri stĺpce obsahujú názov komunikačného
partnera, vstupy a výstupy.

## 3.2 Technický kontext

### Obsah

Technické rozhrania (kanály a prenosové médiá) spájajúce váš systém s
jeho prostredím. Navyše mapovanie doménovo špecifických vstupov/výstupov na
kanály, t. j. vysvetlenie, ktorý I/O používa ktorý kanál.

### Motivácia

Mnohé zainteresované strany robia architektonické rozhodnutia na základe technických rozhraní
medzi systémom a jeho kontextom. Najmä návrhári infraštruktúry alebo hardvéru rozhodujú o týchto technických rozhraniach.

### Forma

Napr. UML diagram nasadenia opisujúci kanály k susedným systémom spolu
s mapovacou tabuľkou zobrazujúcou vzťahy medzi kanálmi a
vstupom/výstupom.

## 4. Stratégia riešenia

Zhrnutie základných rozhodnutí a stratégií riešenia, ktoré formujú
architektúru. Môže zahŕňať technológiu, dekompozíciu na najvyššej úrovni, prístupy
na dosiahnutie najdôležitejších cieľov kvality a relevantné organizačné rozhodnutia.

### Obsah

Stručné zhrnutie a vysvetlenie základných rozhodnutí a stratégií riešenia, ktoré formujú architektúru systému. Patria sem

- technologické rozhodnutia

- rozhodnutia o dekompozícii systému na najvyššej úrovni, napr. použitie architektonického vzoru alebo návrhového vzoru

- rozhodnutia o tom, ako dosiahnuť kľúčové ciele kvality

- relevantné organizačné rozhodnutia, napr. výber vývojového procesu alebo delegovanie určitých úloh tretím stranám.

### Motivácia

Tieto rozhodnutia tvoria základné kamene vašej architektúry. Sú základom
pre mnohé ďalšie podrobné rozhodnutia alebo implementačné pravidlá.

### Forma

Vysvetlenie týchto kľúčových rozhodnutí nech je stručné.

Zdôvodnite, čo ste rozhodli a prečo ste rozhodli takto, na základe
opisu problému, cieľov kvality a kľúčových obmedzení. Odkážte na podrobnosti v
nasledujúcich sekciách (sekcia 5 pre štrukturálne podrobnosti, sekcia 8 pre
prierezové koncepty).

Môžete použiť zoznam prístupov k riešeniu alebo tabuľku.

## 5. Pohľad stavebných blokov

Statická dekompozícia systému, abstrakcie zdrojového kódu, zobrazené ako
hierarchia bielych skriniek (obsahujúcich čierne skrinky) až po vhodnú úroveň
detailu.

### Obsah

Pohľad stavebných blokov zobrazuje statickú dekompozíciu systému na
stavebné bloky (moduly, komponenty, podsystémy, triedy, rozhrania, balíky,
knižnice, frameworky, vrstvy, oddiely, úrovne, funkcie, makrá, operácie,
dátové štruktúry, …) ako aj ich závislosti (vzťahy, asociácie,
…)

Tento pohľad je povinný pre každú architektonickú dokumentáciu. Analogicky
k domu je to pôdorys.

### Motivácia

Udržujte si prehľad o svojom zdrojovom kóde tým, že jeho štruktúru urobíte zrozumiteľnou
prostredníctvom abstrakcie.

To vám umožňuje komunikovať so zainteresovanými stranami na abstraktnej úrovni
bez odhaľovania implementačných detailov.

### Forma

Pohľad stavebných blokov je hierarchická zbierka čiernych skriniek a bielych
skriniek (pozri obrázok nižšie) a ich opisov.

## 5.1 Biela skrinka celého systému

Tu opíšete dekompozíciu celého systému pomocou nasledujúcej šablóny bielej skrinky. Obsahuje

- prehľadový diagram

- motiváciu pre dekompozíciu

- opisy obsiahnutých stavebných blokov ako čiernych skriniek. Pre ne ponúkame alternatívy:

  - použite jednu tabuľku na stručný a pragmatický prehľad všetkých obsiahnutých stavebných blokov a ich rozhraní

  - použite zoznam opisov stavebných blokov ako čiernych skriniek podľa šablóny čiernej skrinky (pozri nižšie). V závislosti od vášho výberu nástroja môže byť tento zoznam podkapitolami (v textových súboroch), podstránkami (vo wiki) alebo vnorenými prvkami (v modelovacom nástroji).

  - (voliteľne:) dôležité rozhrania, ktoré nie sú vysvetlené v šablónach čiernej skrinky stavebného bloku, ale sú veľmi dôležité pre pochopenie bielej skrinky.

Keďže existuje toľko spôsobov, ako špecifikovať rozhrania, neposkytujeme pre ne konkrétnu šablónu.

V najlepšom prípade si vystačíte s príkladmi alebo jednoduchými signatúrami.

## 5.2 Úroveň 2

Tu môžete špecifikovať vnútornú štruktúru (niektorých) stavebných blokov z úrovne 1
ako biele skrinky.

Musíte sa rozhodnúť, ktoré stavebné bloky vášho systému sú dostatočne dôležité na
to, aby odôvodnili taký podrobný opis. Uprednostnite relevantnosť pred úplnosťou.
Špecifikujte dôležité, prekvapivé, rizikové, zložité alebo premenlivé stavebné bloky. Vynechajte
normálne, jednoduché, nudné alebo štandardizované časti vášho systému

### 5.2.1 Biela skrinka pre stavebný blok 1

Špecifikuje vnútornú štruktúru stavebného bloku 1.

Použite šablónu bielej skrinky (pozri vyššie).

## 6. Pohľad za behu

Správanie stavebných blokov ako scenáre pokrývajúce dôležité prípady použitia alebo
funkcie, interakcie na kritických externých rozhraniach, prevádzku a
administráciu plus správanie pri chybách a výnimkách.

### Obsah

Pohľad za behu opisuje konkrétne správanie a interakcie stavebných blokov systému vo forme scenárov z nasledujúcich oblastí:

- dôležité prípady použitia alebo funkcie: ako ich stavebné bloky vykonávajú?

- interakcie na kritických externých rozhraniach: ako stavebné bloky spolupracujú s používateľmi a susednými systémami?

- prevádzka a administrácia: spustenie, štart, zastavenie

- scenáre chýb a výnimiek

Poznámka: Hlavným kritériom pre výber možných scenárov (sekvencií, pracovných postupov) je ich architektonická relevantnosť. Nie je dôležité opísať veľký počet scenárov. Skôr by ste mali zdokumentovať reprezentatívny výber.

### Motivácia

Mali by ste rozumieť tomu, ako (inštancie) stavebných blokov vášho systému vykonávajú svoju prácu a komunikujú za behu. Scenáre budete v dokumentácii zachytávať hlavne na to, aby ste architektúru komunikovali zainteresovaným stranám, ktoré sú menej ochotné alebo schopné čítať a chápať statické modely (pohľad stavebných blokov, pohľad nasadenia).

### Forma

Existuje mnoho notácií na opis scenárov, napr.


- číslovaný zoznam krokov (v prirodzenom jazyku)

- diagramy aktivít alebo vývojové diagramy

- sekvenčné diagramy

- BPMN alebo EPC (reťazce udalostných procesov)

- stavové automaty

- atď.

## 6.n Scenár za behu n (1, 2, 3 atď.)

Vložte diagram behu alebo textový opis scenára.

Vložte opis pozoruhodných aspektov interakcií medzi inštanciami stavebných blokov zobrazenými na tomto diagrame.

## 7. Pohľad nasadenia

Technická infraštruktúra s prostrediami, počítačmi, procesormi, topológiami.
Mapovanie (softvérových) stavebných blokov na prvky infraštruktúry.

### Obsah

Pohľad nasadenia opisuje:

- technickú infraštruktúru použitú na spúšťanie vášho systému s prvkami infraštruktúry
  ako geografické lokality, prostredia, počítače, procesory,
  kanály a sieťové topológie, ako aj ďalšie prvky infraštruktúry a

- mapovanie (softvérových) stavebných blokov na tieto prvky infraštruktúry.

Systémy sa často spúšťajú v rôznych prostrediach, napr. vývojové
prostredie, testovacie prostredie, produkčné prostredie. V takých prípadoch by ste mali
zdokumentovať všetky relevantné prostredia.

Pohľad nasadenia zdokumentujte najmä vtedy, keď sa váš softvér spúšťa ako
distribuovaný systém s viac ako jedným počítačom, procesorom, serverom alebo kontajnerom
alebo keď navrhujete a konštruujete vlastné hardvérové procesory a čipy.

Z pohľadu softvéru stačí zachytiť tie prvky
infraštruktúry, ktoré sú potrebné na zobrazenie nasadenia vašich stavebných blokov.
Hardvéroví architekti môžu ísť ďalej a opísať infraštruktúru do akejkoľvek úrovne
detailu, ktorú potrebujú zachytiť. 

### Motivácia

Softvér nebeží bez hardvéru. Táto základná infraštruktúra môže a
bude ovplyvňovať váš systém a/alebo niektoré prierezové koncepty. Preto
potrebujete poznať infraštruktúru.

### Forma

Možno je diagram nasadenia najvyššej úrovne už obsiahnutý v sekcii 3.2. ako technický kontext s vašou vlastnou infraštruktúrou ako JEDNOU čiernou skrinkou. V tejto sekcii túto čiernu skrinku priblížite pomocou ďalších diagramov nasadenia.

- UML ponúka diagramy nasadenia na vyjadrenie tohto pohľadu. Použite ich, pravdepodobne s vnorenými diagramami, keď je vaša infraštruktúra zložitejšia.

- Keď vaše (hardvérové) zainteresované strany uprednostňujú iné druhy diagramov namiesto
  UML diagramu nasadenia, nechajte ich použiť akýkoľvek druh, ktorý dokáže zobraziť uzly a
  kanály infraštruktúry.

## 7.1 Infraštruktúra úroveň 1

Opíšte (zvyčajne kombináciou diagramov, tabuliek a textu):

- distribúciu vášho systému do viacerých lokalít, prostredí, počítačov, procesorov, .. ako aj fyzické spojenia medzi nimi

- dôležité zdôvodnenie alebo motiváciu pre túto štruktúru nasadenia

- kvalitatívne a/alebo výkonnostné vlastnosti infraštruktúry

- mapovanie softvérových artefaktov (stavebných blokov) na prvky infraštruktúry

Pre viaceré prostredia alebo alternatívne nasadenia skopírujte túto sekciu arc42 pre všetky relevantné prostredia. **

## 7.2 Infraštruktúra úroveň 2

Tu môžete zahrnúť vnútornú štruktúru (niektorých) prvkov infraštruktúry z infraštruktúry úrovne 1.

Skopírujte štruktúru z úrovne 1 pre každý vybraný prvok.

## 8. Prierezové koncepty

Celkové, základné predpisy a prístupy k riešeniu relevantné vo viacerých
častiach (→ prierezovo) systému. Koncepty sú často spojené s viacerými
stavebnými blokmi. Zahrňte rôzne témy ako doménové modely, architektonické
vzory a štýly, pravidlá používania konkrétnej technológie a implementačné pravidlá.

### Obsah

Táto sekcia opisuje prierezové koncepty (praktiky, vzory, predpisy
alebo nápady riešení). Takéto koncepty sú často spojené s viacerými stavebnými blokmi.
Môžu zahŕňať mnoho rôznych tém.

### Motivácia

Koncepty tvoria základ konceptuálnej integrity (konzistentnosti, homogénnosti)
architektúry. Sú teda dôležitým príspevkom k dosiahnutiu vnútorných
kvalít vášho systému.

Toto je miesto v šablóne, ktoré sme poskytli pre súdržnú špecifikáciu
takýchto konceptov.

Mnohé z týchto konceptov súvisia s niekoľkými vašimi stavebnými blokmi alebo ich ovplyvňujú.

### Forma

Forma môže byť rôzna:

- koncepčné dokumenty s akoukoľvek štruktúrou

- ukážkové implementácie, najmä pre technické koncepty

- prierezové výňatky z modelov alebo scenáre využívajúce notácie architektonických pohľadov

### Štruktúra tejto sekcie

Vyberte len tie najpotrebnejšie témy pre váš systém a každej priraďte nadpis úrovne 2 v tejto sekcii (napr. 8.1, 8.2 atď.).

- NESNAŽTE SA pokryť všetky témy z vyššie spomenutého diagramu.

### Pozadie

Niektoré témy v rámci systémov sa často týkajú viacerých stavebných blokov, hardvérových
prvkov alebo vývojových procesov. Môže byť jednoduchšie komunikovať alebo dokumentovať
takéto prierezové témy na centrálnom mieste, namiesto ich opakovania v
opise dotknutých stavebných blokov, hardvérových prvkov alebo
vývojových procesov.

Určité koncepty sa môžu týkať všetkých prvkov systému, iné môžu byť
relevantné len pre niekoľko.

## 9. Architektonické rozhodnutia

Dôležité, nákladné, kritické, rozsiahle alebo rizikové architektonické rozhodnutia
vrátane zdôvodnení.

### Obsah

Dôležité, nákladné, rozsiahle alebo rizikové architektonické rozhodnutia vrátane
zdôvodnení. Pod „rozhodnutiami“ rozumieme výber jednej alternatívy na základe daných
kritérií.

Použite svoj úsudok na rozhodnutie, či by sa architektonické rozhodnutie malo
zdokumentovať tu v tejto centrálnej sekcii, alebo je lepšie ho zdokumentovať
lokálne (napr. v šablóne bielej skrinky jedného stavebného bloku). Vyhnite sa
redundantným textom. Odkážte na sekciu 4, kde ste už zachytili najdôležitejšie
rozhodnutia svojej architektúry.

### Motivácia

Zainteresované strany vášho systému by mali byť schopné pochopiť a spätne vystopovať vaše
rozhodnutia.

### Forma

- ADR (záznam architektonického rozhodnutia) pre každé dôležité rozhodnutie

- zoznam alebo tabuľka, zoradené podľa dôležitosti a dôsledkov alebo

- podrobnejšie vo forme samostatných sekcií pre každé rozhodnutie

### Pozadie (k ADR)

Menšie kúsky dokumentácie sa ľahšie čítajú, tvoria a udržiavajú. Pokiaľ ide
o architektonické rozhodnutia, vývojové tímy často:

- vedia o rozhodnutí, pretože je viditeľné napr. v zdrojovom kóde, ale

- chýba im motivácia za týmto rozhodnutím (pozri Nygard 2011)

Preto by ste mali zdokumentovať niekoľko dôležitých rozhodnutí spolu s ich
motiváciou, uvažovaním

### Náš návrh týkajúci sa rozhodnutí

Udržujte zbierku architektonicky významných rozhodnutí, tých rozhodnutí, ktoré
ovplyvňujú štruktúru, kvalitatívne charakteristiky, dôležité (najmä externé)
závislosti a rozhrania alebo techniky budovania (vďaka Michaelovi
Nygardovi za tento návrh).

## 10. Požiadavky na kvalitu

Požiadavky na kvalitu ako scenáre so stromom kvality, ktorý poskytuje prehľad na vysokej úrovni.
Najdôležitejšie ciele kvality mali byť opísané v sekcii
1.2. (ciele kvality).

### Obsah

Táto sekcia obsahuje všetky relevantné požiadavky na kvalitu.

Najdôležitejšie z týchto požiadaviek už boli opísané v sekcii
1.2. (ciele kvality), preto by sa tu mali len odkazovať. V tejto
sekcii 10 by ste mali zachytiť aj požiadavky na kvalitu s menšou dôležitosťou,
ktoré nevytvoria vysoké riziká, ak nebudú úplne dosiahnuté (ale môžu byť
príjemným doplnkom).

### Motivácia

Keďže požiadavky na kvalitu budú mať veľký vplyv na architektonické
rozhodnutia, mali by ste vedieť, aké kvality sú pre vaše zainteresované strany skutočne
dôležité, konkrétnym a merateľným spôsobom.

### Ďalšie informácie

Pozri rozsiahly model kvality Q42 na https://quality.arc42.org.

## 10.1 Prehľad požiadaviek na kvalitu

### Obsah

Prehľad alebo zhrnutie požiadaviek na kvalitu.

### Motivácia

Často sa stretávame s desiatkami (alebo dokonca stovkami) podrobných požiadaviek na kvalitu.
V tejto prehľadovej sekcii by ste sa mali pokúsiť zhrnúť, napr. opisom
kategórií alebo tém (ako navrhuje ISO 25010:2023 alebo Q42

Ak sú tieto súhrnné opisy už presné, dostatočne konkrétne a
merateľné, môžete sekciu 10.2 preskočiť.

### Forma

Použite jednoduchú tabuľku, v ktorej každý riadok obsahuje kategóriu alebo tému a stručný
opis požiadavky na kvalitu. Alternatívne môžete použiť myšlienkovú mapu
na štruktúrovanie týchto požiadaviek na kvalitu.

V literatúre bola opísaná aj myšlienka stromu kvalitatívnych atribútov,
ktorý dáva všeobecný pojem „kvalita“ ako koreň a používa stromové
spresňovanie pojmu „kvalita“. [Bass+21] zaviedol na tento účel pojem „Quality
Attribute Utility Tree“.

## 10.2 Scenáre kvality

### Obsah

Scenáre kvality robia požiadavky na kvalitu konkrétnymi a umožňujú rozhodnúť, či
sú splnené (v zmysle akceptačných kritérií). Uistite sa, že vaše
scenáre sú konkrétne a merateľné.

Dva druhy scenárov sú obzvlášť užitočné:

- Scenáre použitia (nazývané aj aplikačné scenáre alebo scenáre prípadov použitia)
  opisujú reakciu systému za behu na určitý podnet. To tiež
  zahŕňa scenáre, ktoré opisujú efektívnosť alebo výkon systému.
  Príklad: Systém reaguje na požiadavku používateľa do jednej sekundy.

- Scenáre zmeny opisujú požadovaný účinok úpravy alebo rozšírenia
  systému alebo jeho bezprostredného prostredia. Príklad: Implementuje sa dodatočná funkcionalita
  alebo sa menia požiadavky na kvalitatívny atribút a meria sa úsilie
  alebo trvanie zmeny.

### Forma

Typické informácie pre podrobné scenáre zahŕňajú nasledujúce:

V krátkej forme (uprednostňovanej v modeli Q42):

- Kontext/Pozadie: Aký druh systému alebo komponentu, aké je prostredie alebo situácia?

- Zdroj/Podnet: Kto alebo čo iniciuje alebo spúšťa správanie, reakciu alebo akciu.

- Metrika/Akceptačné kritérium: Odpoveď vrátane miery alebo metriky

Dlhá forma scenárov (uprednostňovaná SEI a [Bass+21]) je podrobnejšia a zahŕňa nasledujúce informácie:

- ID scenára: Jedinečný identifikátor scenára.

- Názov scenára: Krátky, opisný názov scenára.

- Zdroj: Entita (používateľ, systém alebo udalosť), ktorá scenár iniciuje.

- Podnet: Spúšťacia udalosť alebo podmienka, ktorú musí systém riešiť.

- Prostredie: Prevádzkový kontext alebo podmienka, za ktorej systém podnet zažíva.

- Artefakt: Stavebné bloky alebo iné prvky systému ovplyvnené podnetom.

- Odpoveď: Výsledok alebo správanie, ktoré systém prejavuje v reakcii na podnet.

- Miera odpovede: Kritérium alebo metrika, podľa ktorej sa odpoveď systému hodnotí.

### Pozri tiež

Od januára 2023 arc42 poskytuje pragmatický model kvality, ktorý navrhuje
označovať požiadavky na kvalitu hashtagmi alebo štítkami ako #flexible, #efficient,
#usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Riziká a technický dlh

Známe technické riziká alebo technický dlh. Aké potenciálne problémy existujú v systéme alebo
okolo neho? S čím je vývojový tím nešťastný?

### Obsah

Zoznam identifikovaných technických rizík alebo technických dlhov, zoradený podľa priority

### Motivácia

„Riadenie rizík je projektový manažment pre dospelých“ (Tim Lister, Atlantic
Systems Guild.)

Toto by malo byť vaše motto pre systematické zisťovanie a vyhodnocovanie rizík a
technických dlhov v architektúre, ktoré budú potrebné pre manažérske
zainteresované strany (napr. projektových manažérov, vlastníkov produktov) ako súčasť celkovej
analýzy rizík a plánovania opatrení.

### Forma

Zoznam rizík a/alebo technických dlhov, pravdepodobne vrátane navrhovaných opatrení na
minimalizáciu, zmiernenie alebo vyhnutie sa rizikám alebo zníženie technických dlhov.
