# Az AWS architekturális döntési feljegyzési folyamata

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Az architekturális döntési feljegyzés (ADR) olyan dokumentum, amely egy választást ír le, amelyet a csapat az általa építeni tervezett szoftverarchitektúra egy jelentős szempontjáról hoz. Minden ADR leírja az architekturális döntést, annak hátterét és következményeit. Az ADR-eknek vannak állapotaik, ezért életciklust követnek. Egy ADR példáját lásd a függelékben.

Az ADR-folyamat eredménye architekturális döntési feljegyzések gyűjteménye. Ez a gyűjtemény alkotja a döntési naplót. A döntési napló biztosítja a projekt hátterét, valamint a részletes megvalósítási és tervezési információkat. A projekt tagjai átfutják az egyes ADR-ek címsorait, hogy áttekintést kapjanak a projekt hátteréről. Elolvassák az ADR-eket, hogy elmélyedjenek a projekt megvalósításaiban és tervezési választásaiban.

Amikor a csapat elfogad egy ADR-t, az megváltoztathatatlanná válik. Ha új felismerések más döntést igényelnek, a csapat új ADR-t javasol. Amikor a csapat elfogadja az új ADR-t, az felváltja az előzőt.

## Az ADR-folyamat hatóköre

A projekt tagjainak ADR-t kell létrehozniuk minden olyan architekturálisan jelentős döntésről, amely a szoftverprojektet vagy -terméket érinti, többek között a következőkről (Richards és Ford 2020):

* Szerkezet (például minták, mint a mikroszolgáltatások)

* Nem funkcionális követelmények (biztonság, magas rendelkezésre állás és hibatűrés)

* Függőségek (az összetevők csatolása)

* Felületek (API-k és közzétett szerződések)

* Építési technikák (könyvtárak, keretrendszerek, eszközök és folyamatok)

* A funkcionális és nem funkcionális követelmények az ADR-folyamat leggyakoribb bemenetei.


## Az ADR tartalma

Amikor a csapat ADR szükségességét azonosítja, egy csapattag az egész projektre érvényes sablon alapján elkezdi írni az ADR-t. (Példasablonokért lásd az ADR GitHub-szervezetet.) A sablon egyszerűsíti az ADR létrehozását, és biztosítja, hogy az ADR minden releváns információt rögzítsen. Minden ADR-nek legalább meg kell határoznia a döntés hátterét, magát a döntést, valamint a döntés következményeit a projektre és annak szállítandó elemeire nézve. (E szakaszok példáit lásd a függelékben.) Az ADR-szerkezet egyik legerősebb vonása, hogy a döntés okára összpontosít, nem arra, hogyan valósította meg a csapat. Ha megértik, miért hozta meg a csapat a döntést, azzal a többi csapattag könnyebben átveszi, és megakadályozza, hogy más, a döntéshozatali folyamatban részt nem vett építészek a jövőben felülbíráljak.


## Az ADR elfogadási folyamata

Bármely csapattag létrehozhat ADR-t, de a csapatnak meg kell határoznia az ADR tulajdonlásának fogalmát. Minden szerző, aki egy ADR tulajdonosa, aktívan karbantartja és kommunikálja az ADR tartalmát. A tulajdonlás tisztázása érdekében ez az útmutató a következő szakaszokban az ADR szerzőit ADR-tulajdonosoknak nevezi. A többi csapattag mindig hozzájárulhat egy ADR-hez. Ha egy ADR tartalma megváltozik, mielőtt a csapat elfogadná, a tulajdonosnak jóvá kell hagynia ezeket a változásokat.

Miután a csapat azonosít egy architekturális döntést és annak tulajdonosát, az ADR tulajdonosa a folyamat elején **Proposed** (Javasolt) állapotban nyújtja be az ADR-t. A Proposed állapotú ADR-ek készen állnak a felülvizsgálatra.

Ezután az ADR tulajdonosa elindítja az ADR felülvizsgálati folyamatát. Az ADR felülvizsgálati folyamatának célja eldönteni, hogy a csapat elfogadja-e az ADR-t, úgy ítéli-e, hogy át kell dolgozni, vagy elutasítja. A projektcsapat, a tulajdonossal együtt, felülvizsgálja az ADR-t. A felülvizsgálati megbeszélést egy külön időszakkal kell kezdeni az ADR elolvasására. Átlagosan 10–15 perc elegendő. Ez idő alatt minden csapattag elolvassa a dokumentumot, és megjegyzéseket és kérdéseket fűz hozzá a nem világos témák jelzésére. A felülvizsgálati fázis után az ADR tulajdonosa felolvassa és megbeszéli az egyes megjegyzéseket a csapattal.

Ha a csapat az ADR javítására vonatkozó teendőket talál, az ADR állapota **Proposed** marad. Az ADR tulajdonosa megfogalmazza a teendőket, és a csapattal együttműködve minden teendőhöz hozzárendel egy felelőst. Minden csapattag hozzájárulhat a teendők megoldásához. Az ADR tulajdonosának felelőssége, hogy újraütemezze a felülvizsgálati folyamatot.

A csapat dönthet az ADR elutasításáról is. Ebben az esetben az ADR tulajdonosa megadja az elutasítás okát, hogy megelőzze az ugyanarról a témáról folytatott későbbi vitákat. A tulajdonos az ADR állapotát **Rejected** (Elutasított) értékre változtatja.

Ha a csapat jóváhagyja az ADR-t, a tulajdonos hozzáad egy időbélyeget, egy verziót és az érdekelt felek listáját. Ezután a tulajdonos az állapotot **Accepted** (Elfogadott) értékre frissíti.

Az ADR-ek és az általuk létrehozott döntési napló a csapat által hozott döntéseket képviselik, és történetet adnak az összes döntésről. A csapat lehetőség szerint hivatkozási alapként használja az ADR-eket a kód- és architektúra-felülvizsgálatok során. A kódfelülvizsgálatok, tervezési feladatok és megvalósítási feladatok elvégzése mellett a csapattagoknak a termék stratégiai döntéseihez is konzultálniuk kell az ADR-ekkel.

Jó gyakorlatként minden szoftvermódosításnak át kell mennie a társak általi felülvizsgálaton, és legalább egy jóváhagyást igényel. A kódfelülvizsgálat során a felülvizsgáló találhat olyan módosításokat, amelyek megsértenek egy vagy több ADR-t. Ebben az esetben a felülvizsgáló megkéri a kódmódosítás szerzőjét a kód frissítésére, és megosztja az ADR hivatkozását. Amikor a szerző frissíti a kódot, azt a társ-felülvizsgálók jóváhagyják, és beolvasztják a fő kódbázisba.


## Az ADR felülvizsgálati folyamata

A csapatnak megváltoztathatatlan dokumentumként kell kezelnie az ADR-eket, miután elfogadta vagy elutasította őket. Egy meglévő ADR módosítása új ADR létrehozását, az új ADR felülvizsgálati folyamatának kialakítását és az ADR jóváhagyását igényli. Ha a csapat jóváhagyja az új ADR-t, a tulajdonosnak a régi ADR állapotát **Superseded** (Leváltott) értékre kell változtatnia. 
