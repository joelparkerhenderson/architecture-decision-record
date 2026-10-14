# Döntési feljegyzés sablon – arc42

<https://arc42.org/overview>

## 1. Bevezetés és célok

A követelmények, a mozgatóerők rövid leírása, a követelmények kivonata (vagy
összefoglalója). Az architektúra három (legfeljebb öt) legfontosabb minőségi célja,
amelyek a legnagyobb prioritást élvezik a fő érdekelt felek számára. Fontos
érdekelt felek táblázata az architektúrával kapcsolatos elvárásaikkal.

## 1.1 Követelmények áttekintése

### Tartalom

A funkcionális követelmények, a mozgatóerők rövid leírása, a követelmények
kivonata (vagy összefoglalója). Hivatkozások a (remélhetőleg létező) követelmény-
dokumentumokra, azzal az információval, hol találhatók. 

### Motiváció

A végfelhasználók szempontjából egy rendszert azért hoznak létre vagy módosítanak,
hogy jobban támogasson egy üzleti tevékenységet és/vagy javítsa a minőséget. 

### Forma

Rövid szöveges leírás, valószínűleg táblázatos használati eset formátumban. Ha
léteznek követelménydokumentumok, ennek az áttekintésnek hivatkoznia kell rájuk.

Tartsa ezeket a kivonatokat a lehető legrövidebbek. Egyensúlyozza ennek a
dokumentumnak az olvashatóságát a követelménydokumentumokhoz képest esetleges
redundanciával. 

## 1.2 Minőségi célok

### Tartalom

Az architektúra három (legfeljebb öt) legfontosabb minőségi célja, amelyek
teljesülése a legnagyobb jelentőségű a fő érdekelt felek számára. Valóban az
architektúra minőségi céljaira gondolunk. Ne tévessze össze őket a projektcélokkal.
Nem feltétlenül azonosak. Az ISO 25010 szabvány szép áttekintést ad a potenciálisan
érdekes témákról.

### Motiváció

Ismernie kell a legfontosabb érdekelt feleinek minőségi céljait, mert ezek
befolyásolják az alapvető architekturális döntéseket. Legyen nagyon konkrét ezekről
a minőségekről, kerülje a divatszavakat. Ha Ön mint építész nem tudja, hogyan fogják
megítélni a munkája minőségét …

### Forma

Táblázat a legfontosabb minőségi célokkal és konkrét forgatókönyvekkel, prioritás
szerint rendezve.

## 1.3 Érdekelt felek

### Tartalom

A rendszer érdekelt feleinek kifejezett áttekintése, azaz minden olyan személy,
szerepkör vagy szervezet, amely

- ismernie kell az architektúrát

- meg kell győzni az architektúráról

- az architektúrával vagy a kóddal kell dolgoznia

- munkájához szüksége van az architektúra dokumentációjára

- döntéseket kell hoznia a rendszerről vagy a fejlesztéséről

### Motiváció

Ismernie kell a rendszer fejlesztésében részt vevő vagy a rendszer által érintett
összes felet. Ellenkező esetben kellemetlen meglepetések érhetik a fejlesztési
folyamat későbbi szakaszában. Ezek az érdekelt felek határozzák meg a munkája és
eredményei terjedelmét és részletességét.

### Forma

Táblázat szerepkörnevekkel, személynevekkel és az architektúrával és annak
dokumentációjával kapcsolatos elvárásaikkal.

## 2. Megszorítások

Minden, ami korlátozza a csapatokat a tervezési és megvalósítási döntésekben vagy a
kapcsolódó folyamatokra vonatkozó döntésekben. Néha túlmehetnek az egyes
rendszereken, és egész szervezetekre és vállalatokra érvényesek.

### Tartalom

Minden olyan követelmény, amely korlátozza a szoftverépítészeket a tervezési
szabadságukban és a megvalósítási döntéseikben vagy a fejlesztési folyamatra
vonatkozó döntésben. Ezek a megszorítások néha túlmennek az egyes rendszereken,
és egész szervezetekre és vállalatokra érvényesek.

### Motiváció

Az építészeknek pontosan tudniuk kell, hol szabadok a tervezési döntéseikben, és hol
kell betartaniuk megszorításokat. A megszorításokkal mindig foglalkozni kell;
azonban tárgyalhatók lehetnek.

### Forma

Egyszerű megszorítás-táblázatok magyarázatokkal. Ha szükséges, felosztható őket
műszaki megszorításokra, szervezeti és politikai megszorításokra és konvenciókra
(pl. programozási vagy verziókezelési irányelvek, dokumentációs vagy elnevezési
konvenciók)

## 3. Háttér és hatókör

Elhatárolja a rendszert annak (külső) kommunikációs partnereitől (szomszédos
rendszerek és felhasználók). Meghatározza a külső felületeket. Üzleti/tartományi
nézőpontból (mindig) vagy műszaki nézőpontból (nem kötelező) bemutatva

### Tartalom

A rendszer hatóköre és háttere – ahogy a név is sugallja – elhatárolja a rendszert
(vagyis a hatókörét) az összes kommunikációs partnerétől (szomszédos rendszerek és
felhasználók, vagyis a rendszer háttere). Ezáltal meghatározza a külső felületeket.

Ha szükséges, különböztesse meg az üzleti hátteret (tartományspecifikus bemenetek
és kimenetek) a műszaki háttértől (csatornák, protokollok, hardver).

### Motiváció

A kommunikációs partnerekhez fűződő tartományi felületek és műszaki felületek a
rendszer legkritikusabb szempontjai közé tartoznak. Győződjön meg arról, hogy
teljesen megérti őket.

### Forma

- Különféle kontextusdiagramok

- A kommunikációs partnerek és felületeik listái.

## 3.1 Üzleti háttér

### Tartalom

Az összes kommunikációs partner (felhasználók, informatikai rendszerek, …)
specifikációja a tartományspecifikus bemenetek és kimenetek vagy felületek
magyarázatával. Opcionálisan hozzáadhat tartományspecifikus formátumokat vagy
kommunikációs protokollokat.

### Motiváció

Minden érdekelt félnek meg kell értenie, milyen adatokat cserélnek a rendszer
környezetével.

### Forma

Mindenféle diagram, amely a rendszert fekete dobozként mutatja, és meghatározza a
tartományi felületeket a kommunikációs partnerek felé.

Alternatívaként (vagy kiegészítésként) használhat táblázatot. A táblázat címe a
rendszer neve, a három oszlop a kommunikációs partner nevét, a bemeneteket és a
kimeneteket tartalmazza.

## 3.2 Műszaki háttér

### Tartalom

A műszaki felületek (csatornák és átviteli közegek), amelyek a rendszert a
környezetéhez kapcsolják. Ezen felül a tartományspecifikus bemenet/kimenet leképezése
a csatornákra, vagyis annak magyarázata, hogy melyik I/O melyik csatornát használja.

### Motiváció

Sok érdekelt fél hoz architekturális döntést a rendszer és háttere közötti műszaki
felületek alapján. Különösen az infrastruktúra- vagy hardvertervezők döntenek ezekről
a műszaki felületekről.

### Forma

Pl. UML telepítési diagram, amely a szomszédos rendszerekhez vezető csatornákat írja
le, egy leképezési táblázattal együtt, amely a csatornák és a bemenet/kimenet közötti
kapcsolatokat mutatja.

## 4. Megoldási stratégia

Az architektúrát alakító alapvető döntések és megoldási stratégiák összefoglalója.
Tartalmazhat technológiát, a legfelső szintű bontást, a legfontosabb minőségi célok
eléréséhez vezető megközelítéseket és releváns szervezeti döntéseket.

### Tartalom

A rendszer architektúráját alakító alapvető döntések és megoldási stratégiák rövid
összefoglalója és magyarázata. Ezek közé tartoznak

- technológiai döntések

- a rendszer legfelső szintű bontásáról szóló döntések, pl. architekturális minta vagy tervezési minta használata

- döntések arról, hogyan érjük el a kulcsfontosságú minőségi célokat

- releváns szervezeti döntések, pl. fejlesztési folyamat kiválasztása vagy egyes feladatok harmadik félre bízása.

### Motiváció

Ezek a döntések az architektúra sarokkövei. Ezek képezik az alapját sok más részletes
döntésnek vagy megvalósítási szabálynak.

### Forma

Tartsa rövidre e kulcsdöntések magyarázatát.

Indokolja meg, mit döntött és miért döntött úgy, a problémafelvetés, a minőségi
célok és a kulcsfontosságú megszorítások alapján. Hivatkozzon a részletekre a
következő szakaszokban (az 5. szakasz a szerkezeti részletekhez, a 8. szakasz a
keresztmetszeti koncepciókhoz).

Használhat megoldási megközelítések listáját vagy táblázatot.

## 5. Építőelem-nézet

A rendszer statikus bontása, a forráskód absztrakciói, fehér dobozok (fekete
dobozokat tartalmazó) hierarchiájaként bemutatva, a megfelelő részletességi szintig.

### Tartalom

Az építőelem-nézet a rendszer építőelemekre (modulok, összetevők, alrendszerek,
osztályok, felületek, csomagok, könyvtárak, keretrendszerek, rétegek, partíciók,
szintek, függvények, makrók, műveletek, adatszerkezetek, …) való statikus bontását
mutatja, valamint azok függőségeit (kapcsolatok, asszociációk, …)

Ez a nézet kötelező minden architektúra-dokumentációhoz. Egy házhoz hasonlítva ez
az alaprajz.

### Motiváció

Tartson áttekintést a forráskódjáról azáltal, hogy a szerkezetét az absztrakció révén
érthetővé teszi.

Ez lehetővé teszi, hogy az érdekelt felekkel absztrakt szinten kommunikáljon a
megvalósítási részletek felfedése nélkül.

### Forma

Az építőelem-nézet fekete és fehér dobozok hierarchikus gyűjteménye (lásd az alábbi
ábrát) és azok leírásai.

## 5.1 Fehér doboz – a teljes rendszer

Itt írja le a teljes rendszer bontását az alábbi fehérdoboz-sablon használatával.
Tartalmaz

- egy áttekintő diagramot

- a bontás indoklását

- a tartalmazott építőelemek feketedoboz-leírásait. Ezekhez alternatívákat kínálunk:

  - használjon egy táblázatot az összes tartalmazott építőelem és felületeik rövid és pragmatikus áttekintéséhez

  - használja az építőelemek feketedoboz-leírásainak listáját a feketedoboz-sablon szerint (lásd lent). Az eszközválasztástól függően ez a lista lehet alfejezetek (szövegfájlokban), aloldalak (Wikiben) vagy beágyazott elemek (modellezőeszközben).

  - (nem kötelező:) fontos felületek, amelyeket egy építőelem feketedoboz-sablonjai nem magyaráznak, de nagyon fontosak a fehér doboz megértéséhez.

Mivel a felületek meghatározásának annyi módja van, nem adunk rájuk konkrét sablont.

A legjobb esetben megúszhatja példákkal vagy egyszerű szignatúrákkal.

## 5.2 2. szint

Itt megadhatja az 1. szint (egyes) építőelemeinek belső szerkezetét fehér dobozként.

El kell döntenie, hogy a rendszer mely építőelemei elég fontosak ahhoz, hogy
indokolják az ilyen részletes leírást. Részesítse előnyben a relevanciát a
teljességgel szemben. Adja meg a fontos, meglepő, kockázatos, összetett vagy
változékony építőelemeket. Hagyja ki a rendszer normális, egyszerű, unalmas vagy
szabványosított részeit

### 5.2.1 Fehér doboz az 1. építőelemhez

Meghatározza az 1. építőelem belső szerkezetét.

Használja a fehérdoboz-sablont (lásd fent).

## 6. Futásidejű nézet

Az építőelemek viselkedése forgatókönyvekként, amelyek fontos használati eseteket
vagy funkciókat, kritikus külső felületeknél történő interakciókat, üzemeltetést és
adminisztrációt, valamint hiba- és kivételviselkedést fednek le.

### Tartalom

A futásidejű nézet a rendszer építőelemeinek konkrét viselkedését és interakcióit
írja le forgatókönyvek formájában a következő területekről:

- fontos használati esetek vagy funkciók: hogyan hajtják végre az építőelemek?

- interakciók kritikus külső felületeknél: hogyan működnek együtt az építőelemek a felhasználókkal és a szomszédos rendszerekkel?

- üzemeltetés és adminisztráció: indítás, felfutás, leállítás

- hiba- és kivételforgatókönyvek

Megjegyzés: A lehetséges forgatókönyvek (sorozatok, munkafolyamatok) kiválasztásának fő szempontja az architekturális relevanciájuk. Nem fontos nagy számú forgatókönyvet leírni. Inkább egy reprezentatív válogatást dokumentáljon.

### Motiváció

Meg kell értenie, hogyan végzik a munkájukat és kommunikálnak futásidőben a rendszer építőelemeinek (példányai). A dokumentációban főként forgatókönyveket fog rögzíteni, hogy az architektúráját olyan érdekelt feleknek közvetítse, akik kevésbé hajlandók vagy képesek elolvasni és megérteni a statikus modelleket (építőelem-nézet, telepítési nézet).

### Forma

A forgatókönyvek leírására számos jelölésmód létezik, pl.


- számozott lépéslista (természetes nyelven)

- tevékenységdiagramok vagy folyamatábrák

- szekvenciadiagramok

- BPMN vagy EPC-k (eseményvezérelt folyamatláncok)

- állapotgépek

- stb.

## 6.n n. futásidejű forgatókönyv (1, 2, 3 stb.)

Szúrjon be futásidejű diagramot vagy a forgatókönyv szöveges leírását.

Szúrjon be leírást a diagramon ábrázolt építőelem-példányok közötti interakciók figyelemre méltó szempontjairól.

## 7. Telepítési nézet

Műszaki infrastruktúra környezetekkel, számítógépekkel, processzorokkal,
topológiákkal. A (szoftver) építőelemek leképezése infrastruktúra-elemekre.

### Tartalom

A telepítési nézet leírja:

- a rendszer futtatásához használt műszaki infrastruktúrát, olyan infrastruktúra-
  elemekkel, mint földrajzi helyek, környezetek, számítógépek, processzorok,
  csatornák és hálózati topológiák, valamint más infrastruktúra-elemek, és

- a (szoftver) építőelemek leképezését ezekre az infrastruktúra-elemekre.

A rendszereket gyakran különböző környezetekben futtatják, pl. fejlesztői
környezet, tesztkörnyezet, éles környezet. Ilyen esetekben az összes releváns
környezetet dokumentálnia kell.

Különösen akkor dokumentálja a telepítési nézetet, ha a szoftvere elosztott
rendszerként fut, egynél több számítógéppel, processzorral, kiszolgálóval vagy
konténerrel, vagy ha saját hardverprocesszorokat és chipeket tervez és épít.

Szoftveres szempontból elegendő az infrastruktúrának azokat az elemeit rögzíteni,
amelyek az építőelemek telepítésének bemutatásához szükségesek. A hardverépítészek
ezen túl mehetnek, és az infrastruktúrát bármilyen szükséges részletességgel
leírhatják. 

### Motiváció

A szoftver hardver nélkül nem fut. Ez az alapul szolgáló infrastruktúra
befolyásolhatja és befolyásolni fogja a rendszert és/vagy egyes keresztmetszeti
koncepciókat. Ezért ismernie kell az infrastruktúrát.

### Forma

Talán a legfelső szintű telepítési diagram már szerepel a 3.2. szakaszban műszaki háttérként, a saját infrastruktúrájával EGY fekete dobozként. Ebben a szakaszban további telepítési diagramokkal ráközelít erre a fekete dobozra.

- Az UML telepítési diagramokat kínál e nézet kifejezésére. Használja, valószínűleg beágyazott diagramokkal, ha az infrastruktúra összetettebb.

- Ha a (hardveres) érdekelt felek az UML telepítési diagram helyett más típusú
  diagramokat részesítenek előnyben, engedje meg nekik, hogy bármilyen olyan típust
  használjanak, amely az infrastruktúra csomópontjait és csatornáit meg tudja mutatni.

## 7.1 Infrastruktúra 1. szint

Írja le (általában diagramok, táblázatok és szöveg kombinációjával):

- a rendszer elosztását több helyre, környezetbe, számítógépre, processzorra, .. valamint a köztük lévő fizikai kapcsolatokat

- a telepítési szerkezet fontos indoklását vagy motivációját

- az infrastruktúra minőségi és/vagy teljesítményjellemzőit

- a szoftverartefaktumok (építőelemek) leképezését az infrastruktúra elemeire

Több környezet vagy alternatív telepítés esetén másolja ki az arc42 e szakaszát az összes releváns környezetre. **

## 7.2 Infrastruktúra 2. szint

Itt belefoglalhatja az infrastruktúra 1. szintjének (egyes) infrastruktúra-elemeinek belső szerkezetét.

Másolja át az 1. szint szerkezetét minden kiválasztott elemhez.

## 8. Keresztmetszeti koncepciók

Általános, alapvető szabályozások és megoldási megközelítések, amelyek a rendszer
több részén (→ keresztmetszetben) relevánsak. A koncepciók gyakran több
építőelemhez kapcsolódnak. Különböző témákat foglalnak magukban, mint a
tartományi modellek, architekturális minták és stílusok, egyes technológiák
használatának szabályai és megvalósítási szabályok.

### Tartalom

Ez a szakasz keresztmetszeti koncepciókat (gyakorlatok, minták, szabályozások vagy
megoldási ötletek) ír le. Az ilyen koncepciók gyakran több építőelemhez kapcsolódnak.
Sokféle témát foglalhatnak magukban.

### Motiváció

A koncepciók képezik az architektúra fogalmi integritásának (következetesség,
homogenitás) alapját. Így fontos hozzájárulást jelentenek a rendszer belső
minőségeinek eléréséhez.

Ez az a hely a sablonban, amelyet az ilyen koncepciók összefüggő specifikációjához
biztosítottunk.

E koncepciók közül sok több építőelemhez kapcsolódik vagy befolyásolja azokat.

### Forma

A forma változatos lehet:

- tetszőleges szerkezetű koncepciódokumentumok

- példamegvalósítások, különösen műszaki koncepciókhoz

- keresztmetszeti modellkivonatok vagy forgatókönyvek az architektúranézetek jelöléseivel

### E szakasz szerkezete

Válassza ki csak a rendszeréhez legszükségesebb témákat, és rendeljen mindegyikhez egy 2. szintű címsort ebben a szakaszban (pl. 8.1, 8.2 stb.).

- NE PRÓBÁLJA lefedni a fent említett diagram összes témáját.

### Háttér

A rendszerek egyes témái gyakran több építőelemet, hardverelemet vagy
fejlesztési folyamatot érintenek. Könnyebb lehet az ilyen keresztmetszeti témákat
egy központi helyen közölni vagy dokumentálni, ahelyett hogy az érintett
építőelemek, hardverelemek vagy fejlesztési folyamatok leírásában ismételnénk őket.

Egyes koncepciók a rendszer minden elemét érinthetik, mások csak néhányat.

## 9. Architekturális döntések

Fontos, költséges, kritikus, nagyléptékű vagy kockázatos architekturális döntések
indoklással együtt.

### Tartalom

Fontos, költséges, nagyléptékű vagy kockázatos architekturális döntések indoklással
együtt. A „döntések” alatt azt értjük, hogy adott kritériumok alapján kiválasztunk
egy alternatívát.

Saját megítélése szerint döntse el, hogy egy architekturális döntést itt, ebben a
központi szakaszban érdemes dokumentálni, vagy jobb helyben dokumentálni (pl. egy
építőelem fehérdoboz-sablonján belül). Kerülje a felesleges szövegeket. Hivatkozzon
a 4. szakaszra, ahol már rögzítette az architektúra legfontosabb döntéseit.

### Motiváció

A rendszer érdekelt feleinek képesnek kell lenniük a döntései megértésére és
nyomon követésére.

### Forma

- ADR (architekturális döntési feljegyzés) minden fontos döntéshez

- lista vagy táblázat, fontosság és következmények szerint rendezve, vagy

- részletesebben, döntésenkénti külön szakaszok formájában

### Háttér (az ADR-ekről)

A kisebb dokumentációdarabokat könnyebb olvasni, létrehozni és karbantartani. Az
architekturális döntéseknél a fejlesztőcsapatok gyakran:

- ismerik a döntést, mert az látható pl. a forráskódban, de

- nem ismerik a döntés mögötti motivációt (lásd Nygard 2011)

Ezért érdemes néhány fontos döntést a motivációjukkal és érvelésükkel együtt
dokumentálnia

### Javaslatunk a döntésekre

Vezessen gyűjteményt az architekturálisan jelentős döntésekről, azokról a
döntésekről, amelyek befolyásolják a szerkezetet, a minőségi jellemzőket, a fontos
(különösen külső) függőségeket és felületeket, vagy az építési technikákat (köszönet
Michael Nygardnak e javaslatért).

## 10. Minőségi követelmények

Minőségi követelmények forgatókönyvekként, minőségfával, amely magas szintű
áttekintést ad. A legfontosabb minőségi célokat az 1.2. szakaszban (minőségi célok)
kellett volna leírni.

### Tartalom

Ez a szakasz tartalmazza az összes releváns minőségi követelményt.

E követelmények közül a legfontosabbakat már leírták az 1.2. szakaszban (minőségi
célok), ezért itt csak hivatkozni kell rájuk. E 10. szakaszban a kisebb jelentőségű
minőségi követelményeket is rögzítenie kell, amelyek nem okoznak nagy kockázatot, ha
nem teljesülnek teljesen (de lehet, hogy kívánatosak).

### Motiváció

Mivel a minőségi követelmények nagy hatással lesznek az architekturális döntésekre,
tudnia kell, hogy mely minőségek valóban fontosak az érdekelt feleinek, konkrét és
mérhető módon.

### További információ

Lásd a kiterjedt Q42 minőségi modellt a https://quality.arc42.org oldalon.

## 10.1 Minőségi követelmények áttekintése

### Tartalom

A minőségi követelmények áttekintése vagy összefoglalója.

### Motiváció

Gyakran találkozunk tucatnyi (vagy akár százas nagyságrendű) részletes minőségi
követelménnyel. Ebben az áttekintő szakaszban érdemes összefoglalnia, pl.
kategóriák vagy témák leírásával (ahogy az ISO 25010:2023 vagy a Q42 javasolja

Ha ezek az összefoglaló leírások már pontosak, elég konkrétak és mérhetők,
kihagyhatja a 10.2. szakaszt.

### Forma

Használjon egy egyszerű táblázatot, amelyben minden sor egy kategóriát vagy témát és
a minőségi követelmény rövid leírását tartalmazza. Alternatívaként használhat
gondolattérképet e minőségi követelmények strukturálásához.

Az irodalomban a minőségi attribútumfa gondolata is megjelent, amely a „minőség”
általános fogalmát teszi gyökérré, és a „minőség” fogalmának fa-szerű finomítását
használja. A [Bass+21] erre a célra vezette be a „Quality Attribute Utility Tree”
kifejezést.

## 10.2 Minőségi forgatókönyvek

### Tartalom

A minőségi forgatókönyvek konkretizálják a minőségi követelményeket, és lehetővé
teszik annak eldöntését, hogy teljesülnek-e (az elfogadási kritériumok értelmében).
Gondoskodjon arról, hogy a forgatókönyvei konkrétak és mérhetők legyenek.

Két típusú forgatókönyv különösen hasznos:

- A használati forgatókönyvek (alkalmazási forgatókönyveknek vagy használatiesetes
  forgatókönyveknek is nevezik) a rendszer futásidejű reakcióját írják le egy
  bizonyos ingerre. Ide tartoznak a rendszer hatékonyságát vagy teljesítményét leíró
  forgatókönyvek is. Példa: A rendszer egy másodpercen belül reagál a felhasználó kérésére.

- A változásforgatókönyvek a rendszer vagy közvetlen környezete módosításának vagy
  bővítésének kívánt hatását írják le. Példa: További funkcionalitást valósítanak
  meg, vagy egy minőségi attribútum követelményei változnak, és mérik a változás
  erőfeszítését vagy időtartamát.

### Forma

A részletes forgatókönyvek tipikus információi a következők:

Rövid formában (a Q42 modellben előnyben részesítve):

- Háttér: Milyen rendszer vagy összetevő, mi a környezet vagy helyzet?

- Forrás/Inger: Ki vagy mi kezdeményez vagy vált ki viselkedést, reakciót vagy cselekvést.

- Mérőszám/Elfogadási kritériumok: Mérőszámot vagy metrikát tartalmazó válasz

A forgatókönyvek hosszú formája (az SEI és a [Bass+21] által előnyben részesített) részletesebb, és a következő információkat tartalmazza:

- Forgatókönyv-azonosító: A forgatókönyv egyedi azonosítója.

- Forgatókönyv neve: A forgatókönyv rövid, leíró neve.

- Forrás: Az entitás (felhasználó, rendszer vagy esemény), amely elindítja a forgatókönyvet.

- Inger: Az indító esemény vagy feltétel, amelyet a rendszernek kezelnie kell.

- Környezet: Az üzemi háttér vagy feltétel, amelyben a rendszer az ingert tapasztalja.

- Artefaktum: A rendszer építőelemei vagy más elemei, amelyeket az inger érint.

- Válasz: Az eredmény vagy viselkedés, amelyet a rendszer az ingerre reagálva mutat.

- Válaszmérték: A kritériumok vagy metrika, amely alapján a rendszer válaszát értékelik.

### Lásd még

2023 januárja óta az arc42 pragmatikus minőségi modellt kínál, amely azt javasolja,
hogy a minőségi követelményeket hashtagekkel vagy címkékkel jelöljék, mint
#flexible, #efficient, #usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Kockázatok és műszaki adósság

Ismert műszaki kockázatok vagy műszaki adósság. Milyen potenciális problémák léteznek
a rendszerben vagy körülötte? Mivel nincs megelégedve a fejlesztőcsapat?

### Tartalom

Az azonosított műszaki kockázatok vagy műszaki adósságok listája, prioritás szerint rendezve

### Motiváció

„A kockázatkezelés felnőtteknek szóló projektmenedzsment” (Tim Lister, Atlantic
Systems Guild.)

Ez legyen a jelmondata az architektúra kockázatainak és műszaki adósságainak
szisztematikus felderítéséhez és értékeléséhez, amelyre a vezetői érdekelt feleknek
(pl. projektmenedzserek, terméktulajdonosok) szükségük lesz az átfogó
kockázatelemzés és intézkedéstervezés részeként.

### Forma

Kockázatok és/vagy műszaki adósságok listája, valószínűleg a kockázatok
minimalizálására, enyhítésére vagy elkerülésére, illetve a műszaki adósságok
csökkentésére javasolt intézkedésekkel.
