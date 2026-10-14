# Architekturális döntési feljegyzés (ADR)

Az architekturális döntési feljegyzés (ADR) egy olyan dokumentum, amely egy fontos architekturális döntést rögzít a hozzá tartozó háttérrel és következményekkel együtt.

> [!IMPORTANT]
> Végezze el a saját gondos felülvizsgálatát ezekről az erőforrásokról, mielőtt bármely kritikus rendszerben használná őket.

Tartalom:

- [Mi az architekturális döntési feljegyzés?](#mi-az-architekturális-döntési-feljegyzés)
- [Hogyan kezdjünk hozzá az ADR-ek használatához](#hogyan-kezdjünk-hozzá-az-adr-ek-használatához)
- [Hogyan kezdjünk hozzá az ADR-ek használatához eszközökkel](#hogyan-kezdjünk-hozzá-az-adr-ek-használatához-eszközökkel)
- [Hogyan kezdjünk hozzá az ADR-ek használatához gittel](#hogyan-kezdjünk-hozzá-az-adr-ek-használatához-gittel)
- [Claude Code képességek ADR-ekhez](#claude-code-képességek-adr-ekhez)
- [ADR-fájlnév-konvenciók](#adr-fájlnév-konvenciók)
- [Javaslatok jó ADR-ek íráshoz](#javaslatok-jó-adr-ek-íráshoz)
- [ADR-példasablonok](#adr-példasablonok)
- [Csapatmunka-tanácsok ADR-ekhez](#csapatmunka-tanácsok-adr-ekhez)
- [Csapatmunka-kérdések ADR-ekhez](#csapatmunka-kérdések-adr-ekhez)
- [Következő lépés koncepciók ADR-ekhez](#következő-lépés-koncepciók-adr-ekhez)
- [Architekturális diagramok, nézetek és nézőpontok](#architekturális-diagramok-nézetek-és-nézőpontok)
- [Alkalmassági függvények döntésekhez kódként](#alkalmassági-függvények-döntésekhez-kódként)
- [Döntési korlátok pull requestekhez](#döntési-korlátok-pull-requestekhez)
- [További információ](#további-információ)

Sablonok:

- [Döntési feljegyzés sablon – Jeff Tyree és Art Akerman](sablonok/dontesi-feljegyzes-sablon-jeff-tyree-es-art-akerman/)
- [Döntési feljegyzés sablon – Michael Nygard](sablonok/dontesi-feljegyzes-sablon-michael-nygard/)
- [Döntési feljegyzés sablon – EdgeX](sablonok/dontesi-feljegyzes-sablon-edgex/)
- [Döntési feljegyzés sablon – arc42](sablonok/dontesi-feljegyzes-sablon-arc42/)
- [Döntési feljegyzés sablon alexandriai mintához](sablonok/dontesi-feljegyzes-sablon-alexandriai-mintahoz/)
- [Döntési feljegyzés sablon üzleti esethez](sablonok/dontesi-feljegyzes-sablon-uzleti-esethez/)
- [Döntési feljegyzés sablon – a MADR projekt](sablonok/dontesi-feljegyzes-sablon-madr-projekt/)
- [Döntési feljegyzés sablon Planguage használatával](sablonok/dontesi-feljegyzes-sablon-planguage-szal/)
- [Döntési feljegyzés sablon – Paulo Merson](https://github.com/pmerson/ADR-template)
- [Döntési feljegyzés sablon – Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Döntési feljegyzés sablon – Gareth Morgan](sablonok/dontesi-feljegyzes-sablon-gareth-morgan/)
- [Döntési feljegyzés sablon – GIG Cymru NHS Wales](sablonok/dontesi-feljegyzes-sablon-gig-cymru-nhs-wales/)
- [Döntési feljegyzés sablon Fontos Technikai Döntésekhez (ITD) – Ignacio Larrañaga](sablonok/dontesi-feljegyzes-sablon-fontos-technikai-dontesekhez/)

Példák:

- [CSS keretrendszer](peldak/css-keretrendszer/)
- [Környezeti változók konfigurálása](peldak/kornyezeti-valtozok-konfiguralasa/)
- [Metrikák, monitorok, riasztások](peldak/metrikak-monitorok-riasztasok/)
- [Microsoft Azure DevOps](peldak/microsoft-azure-devops/)
- [Monorepo vagy multirepo](peldak/monorepo-vagy-multirepo/)
- [Programozási nyelvek](peldak/programozasi-nyelvek/)
- [Titkok tárolása](peldak/titkok-tarolasa/)
- [Időbélyeg-formátum](peldak/idobelyeg-formatum/)
- [Még sok más...](peldak/)

## Mi az architekturális döntési feljegyzés?

Az **architekturális döntési feljegyzés** (angolul architecture decision record, ADR) egy olyan dokumentum, amely egy fontos architekturális döntést rögzít a hozzá tartozó háttérrel és következményekkel együtt.

Az **architekturális döntés** (angolul architecture decision, AD) egy olyan szoftvertervezési választás, amely egy jelentős követelményre ad választ.

Az **architekturális döntési napló** (angolul architecture decision log, ADL) egy adott projekt (vagy szervezet) számára létrehozott és karbantartott összes ADR gyűjteménye.

Az **architekturálisan jelentős követelmény** (angolul architecturally-significant requirement, ASR) olyan követelmény, amely mérhető hatással van egy szoftverrendszer architektúrájára.

Mindez az **architekturális tudásmenedzsment** (angolul architecture knowledge management, AKM) témakörébe tartozik.

E dokumentum célja, hogy gyors áttekintést adjon az ADR-ekről, a létrehozásukról és arról, hol található további információ.

Rövidítések:

  * **AD**: architekturális döntés

  * **ADL**: architekturális döntési napló

  * **ADR**: architekturális döntési feljegyzés

  * **AKM**: architekturális tudásmenedzsment

  * **ASR**: architekturálisan jelentős követelmény

## Hogyan kezdjünk hozzá az ADR-ek használatához

Az ADR-ek használatának megkezdéséhez beszélgessen a csapattársaival az alábbi területekről.

A döntések azonosítása:

  * Mennyire sürgős és mennyire fontos az architekturális döntés?

  * Most kell meghozni, vagy várhat, amíg többet tudunk?

  * A személyes és a közös tapasztalat, valamint az elismert tervezési módszerek és gyakorlatok egyaránt segíthetnek a döntések azonosításában.

  * Ideális esetben vezessen döntési teendőlistát, amely kiegészíti a termék teendőlistáját.

A döntéshozatal:

  * Számos döntéshozatali technika létezik, általánosak és a szoftverarchitektúrára jellemzőek is, például a párbeszédtérképezés (dialogue mapping).

  * A csoportos döntéshozatal aktív kutatási téma.

A döntések életbe léptetése és érvényesítése:

  * Az architekturális döntéseket a szoftvertervezés használja; ezért közölni kell őket a rendszert finanszírozó, fejlesztő és üzemeltető érdekelt felekkel, és el kell fogadtatni velük.

  * Két kapcsolódó gyakorlat az architekturálisan érthető kódolási stílus, valamint az architekturális szempontokra és döntésekre összpontosító kódellenőrzés.

  * Az architekturális döntéseket a szoftverrendszer korszerűsítésekor, a szoftver fejlődése során is (újra) át kell gondolni.

A döntések megosztása (nem kötelező):

  * Sok architekturális döntés ismétlődik a projektek között.

  * Ezért a korábbi döntésekkel kapcsolatos tapasztalatok, jók és rosszak egyaránt, értékes újrahasznosítható eszközök lehetnek, ha kifejezett tudásmenedzsment-stratégiát alkalmazunk.

A döntések dokumentálása:

  * Számos sablon és eszköz létezik a döntések rögzítésére.

  * Lásd az agilis közösségeket, pl. M. Nygard ADR-jeit.

  * Lásd a hagyományos szoftverfejlesztési és architektúratervezési folyamatokat, pl. az IBM UMF és a CapitalOne-os Tyree és Akerman által javasolt táblázatos elrendezéseket.

További információ:

  * A fenti lépések a Wikipedia [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision) szócikkéből származnak

## Hogyan kezdjünk hozzá az ADR-ek használatához eszközökkel

- [MySpec](https://myspec.dev) — Automatizált specifikációs és architekturális döntési platform, amely a projekt alapelveit, a műszaki architektúrát és az ADR-eket tiszta Markdownba rendezi, és MCP-n keresztül szolgáltatja.

Az ADR-ek használatát eszközökkel bárhogyan elkezdheti.

Például:

  * Ha szereti a Google Drive-ot és az online szerkesztést, létrehozhat egy Google-dokumentumot vagy Google-táblázatot.

  * Ha szereti a forráskód verziókezelését, például a gitet, létrehozhat egy fájlt minden ADR-hez.

  * Ha szereti a projekttervező eszközöket, például az Atlassian Jirát, használhatja az eszköz tervezési követőjét.

  * Ha szereti a wikiket, például a MediaWikit, létrehozhat egy ADR-wikit.

## Hogyan kezdjünk hozzá az ADR-ek használatához gittel

Ha szereti a git verziókezelést, így szeretünk mi hozzáfogni az ADR-ek használatához gittel egy tipikus, forráskóddal rendelkező szoftverprojektben.

Hozzon létre egy könyvtárat az ADR-fájloknak:

```sh
$ mkdir adr
```

Minden ADR-hez hozzon létre egy szövegfájlt, például `choose-database.md`:

```sh
$ vi choose-database.md
```

Írjon az ADR-be bármit. Ötletekért nézze meg az ebben a tárolóban található sablonokat.

Commitolja az ADR-t a git tárolójába.

## Claude Code képességek ADR-ekhez

Ez a tároló két [Claude Code](https://claude.com/claude-code) képességet (skill) szállít a [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/) könyvtárban, hogy egy MI-programozási ügynök úgy tudjon ADR-eket írni és karbantartani, ahogyan ez a projekt javasolja:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — általános célú, bárkinek, aki bármely projektben ADR-t ír. Segít eldönteni, hogy egy döntés igényel-e ADR-t, létrehoz egy `adr/` vagy `decisions/` könyvtárat, elnevezi a fájlt, kiválaszt egy sablont a tizenegy mellékelt vázlat közül, és szilárd Háttér/Döntés/Következmények szakaszokat ír.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — kifejezetten e tároló karbantartóinak. Dokumentálja a tároló felépítését, a README/locales tükrözési konvenciót és az új sablon, példa vagy eszközhivatkozás hozzáadásának pontos lépéseit.

Egy képesség használatához másolja a mappáját annak a tárolónak a gyökerében lévő `.claude/skills/` könyvtárba, amelyben dolgozik (vagy a `~/.claude/skills/` könyvtárba, hogy minden projektben elérhető legyen), majd kérje meg a Claude Code-ot, hogy írjon vagy vizsgáljon felül egy ADR-t.

## ADR-fájlnév-konvenciók

Ha az ADR-eket hagyományos szövegfájlokban hozza létre, érdemes kialakítania a saját ADR-fájlnév-konvencióját.

Mi egy meghatározott formátumú fájlnév-konvenciót részesítünk előnyben.

Példák:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

A mi fájlnév-konvenciónk:

  * A név egy felszólító módú igei kifejezést tartalmaz (angolul jelen idő). Ez javítja az olvashatóságot, és illeszkedik a commitüzeneteink formátumához.

  * A név kisbetűket és kötőjeleket használ (mint ez a tároló). Ez egyensúly az olvashatóság és a rendszerben való használhatóság között.

  * A kiterjesztés markdown. Ez hasznos lehet az egyszerű formázáshoz.

## Javaslatok jó ADR-ek íráshoz

Egy jó ADR jellemzői:

* Indoklás: Magyarázza el az adott architekturális döntés meghozatalának okait. Ez magában foglalhatja a hátteret (lásd lent), a különböző lehetséges választások előnyeit és hátrányait, funkcióösszehasonlításokat, költség–haszon megbeszéléseket és egyebeket.

* Konkrét: Minden ADR egy architekturális döntésről szóljon, ne többről.

* Időbélyegek: Jelölje meg, mikor íródott az ADR egyes elemei. Ez különösen fontos azoknál a szempontoknál, amelyek idővel változhatnak, például költségek, ütemtervek, skálázás és hasonlók.

* Megváltoztathatatlan: Ne módosítsa az ADR meglévő információit. Ehelyett egészítse ki az ADR-t új információkkal, vagy váltsa le egy új ADR létrehozásával.

Egy jó „Háttér” szakasz jellemzői egy ADR-ben:

* Magyarázza el a szervezet helyzetét és az üzleti prioritásokat.

* Foglaljon bele a csapatai társas és készségbeli összetételén alapuló indoklást és szempontokat.

* Foglaljon bele releváns előnyöket és hátrányokat, és írja le őket az igényeivel és céljaival összhangban lévő módon.

Egy jó „Következmények” szakasz jellemzői egy ADR-ben:

* Magyarázza el, mi következik a döntés meghozatalából. Ez magában foglalhatja a hatásokat, eredményeket, kimeneteket, utókövetést és egyebeket.

* Foglaljon bele információt az esetleges későbbi ADR-ekről. Viszonylag gyakori, hogy egy ADR további ADR-ek szükségességét váltja ki, például amikor egy ADR nagy, átfogó választást tesz, ami viszont több kisebb döntés igényét hozza létre.

* Foglaljon bele minden utólagos értékelési folyamatot. Jellemző, hogy a csapatok egy hónappal később áttekintik az egyes ADR-eket, hogy összevessék az ADR információit a gyakorlatban történtekkel, hogy tanuljanak és fejlődjenek.

Egy új ADR átveheti egy korábbi ADR helyét:

* Amikor olyan architekturális döntés születik, amely felváltja vagy érvényteleníti egy korábbi ADR-t, új ADR-t kell létrehozni

## ADR-példasablonok

Az interneten gyűjtött ADR-példasablonok:

- [ADR-sablon – Michael Nygard](sablonok/dontesi-feljegyzes-sablon-michael-nygard/) (egyszerű és népszerű)

- [ADR-sablon – Jeff Tyree és Art Akerman](sablonok/dontesi-feljegyzes-sablon-jeff-tyree-es-art-akerman/) (kifinomultabb)

- [ADR-sablon alexandriai mintához](sablonok/dontesi-feljegyzes-sablon-alexandriai-mintahoz/) (egyszerű, háttérrészletekkel)

- [ADR-sablon üzleti esethez](sablonok/dontesi-feljegyzes-sablon-uzleti-esethez/) (MBA-orientáltabb, költségekkel, SWOT-tal és több véleménnyel)

- [A Markdown Any Decision Records (MADR) projekt ADR-sablonja](sablonok/dontesi-feljegyzes-sablon-madr-projekt/) (egyszerű és kidolgozott változat is; az utóbbi a lehetőségeket és azok előnyeit és hátrányait hangsúlyozza)

- [ADR-sablon Planguage használatával](sablonok/dontesi-feljegyzes-sablon-planguage-szal/) (minőségbiztosítás-orientáltabb)

- [Sablon Fontos Technikai Döntésekhez (ITD) – Ignacio Larrañaga](sablonok/dontesi-feljegyzes-sablon-fontos-technikai-dontesekhez/) (karcsú és döntés-központú, gyors vezetői átvizsgálásra optimalizált)

## Csapatmunka-tanácsok ADR-ekhez

Ha azt fontolgatja, hogy döntési feljegyzéseket használjon a csapatával, íme néhány tanács, amelyet sok csapattal dolgozva tanultunk.

Lehetősége van vezetni a csapattársait azzal, hogy együtt beszélnek a „miértről”, ahelyett hogy a „mit” előírnák. Például a döntési feljegyzések a csapatok számára az okosabb gondolkodás és a jobb kommunikáció eszközei; a döntési feljegyzéseknek nincs értékük, ha csak utólagos, kényszerű papírmunkává válnak.

Néhány csapat sokkal jobban szereti a „döntések” nevet az „ADR” rövidítésnél. Amikor egyes csapatok a „decisions” könyvtárnevet használják, mintha felgyulladna egy villanykörte, és a csapat több információt kezd tenni a könyvtárba, például beszállítói döntéseket, tervezési döntéseket, ütemezési döntéseket stb. Mindezek az információfajták használhatják ugyanazt a sablont. Feltételezésünk szerint az emberek gyorsabban tanulnak szavakkal („döntések”), mint rövidítésekkel („ADR”), nagyobb a motivációjuk a folyamatban lévő dokumentumok megírására, ha elhagyjuk a „feljegyzés” szót, és néhány fejlesztő és néhány vezető nem szereti az „architektúra” szót.

Elméletben a megváltoztathatatlanság az ideális. A gyakorlatban a csapatainknál a módosíthatóság vált be jobban. Az új információt beillesztjük a meglévő ADR-be, dátumbélyeggel és megjegyzéssel, hogy az információ a döntés után érkezett. Ez a megközelítés „élő dokumentumhoz” vezet, amelyet mindannyian frissíthetünk. Tipikus frissítések, amikor új csapattársaknak, új ajánlatoknak, a használatunk valós eredményeinek köszönhetően jutunk információhoz, vagy utólagos harmadik felek általi változások miatt, például szállítói képességek, árazási tervek, licencszerződések stb.

## Csapatmunka-kérdések ADR-ekhez

### Ki hozhat létre ADR-t?

Gondoljon olyan területekre, mint konkrét személyek, konkrét szerepkörök, konkrét csapatok vagy konkrét osztályok; vegye figyelembe azt is, hogy vannak-e olyan személyek, szerepkörök, csapatok vagy osztályok, amelyek megrendelhetnek egy ADR-t, vagyis kérhetik, hogy más írja meg. 

Példaválasz: Szervezetünk bármely tagja, aki elolvasta az architekturális döntési feljegyzés README oldalt, javasolhat ADR-t, vagyis elkezdheti megírni, és megoszthatja a csapattal.

### Mi indokolja egy ADR létrehozását?

Gondoljon olyan területekre, mint a szervezet csapatainak munkamódszerei, a szoftverrendszer szerkezete, a csapatok közötti koordináció, a hosszú távú karbantarthatóság, a külső felületek, kinek szeretne hasznot hajtani és hasonlók. 

Példaválasz: Akkor akarunk ADR-t létrehozni, amikor azt szeretnénk, hogy a jövőbeli fejlesztők megértsék a „miértet” abban, amit csinálunk.

### Mi indokolja, hogy ne hozzunk létre ADR-t?

Gondoljon olyan területekre, mint azok a döntések, amelyek nem az architektúráról szólnak, vagy aprók, például minimális kockázatúak, önállóak vagy egyetlen fejlesztő döntései, vagy már teljesen le vannak fedve máshol, például szabványokban, szabályzatokban vagy dokumentációban, vagy átmenetiek, például kerülőmegoldások, koncepcióigazolások vagy kísérletek. 

Példaválasz: Kihagyunk egy ADR-t, ha egy döntés hatóköre, ideje, kockázata és költsége korlátozott, vagy már le van fedve máshol.

### Mi egy ADR életciklusa?

Gondoljon olyan területekre, mint a létrehozási folyamat, a kutatási folyamat, a döntéshozatali folyamat, a megvalósítási folyamat és a kivezetési folyamat. Gondolja végig, hogyan követi nyomon az ADR életciklusát az idő múlásával, például hogyan viszi az ADR-t egyik állapotból a következőbe, és hogyan kommunikálja ezt az érdekelt feleknek. 

Példaválasz: Azt szeretnénk, hogy egy ADR-nek öt életciklus-szakasza legyen: Kezdeményezés → Kutatás → Értékelés → Megvalósítás → Karbantartás → Kivezetés.

### Mik az ADR életciklus-lépéseinek kritériumai?

Gondoljon olyan területekre, mint az ADR elfogadási kritériumai, vagyis honnan tudja, hogy elég jó ahhoz, hogy az egyik életciklus-lépésből a következőbe lépjen? Világosan megfogalmazott a probléma? Megvizsgálták az alternatívákat? Elég jól értik és dokumentálták a kompromisszumokat?
Megvan minden releváns háttér? Be vannak vonva az összes releváns érdekelt fél? Beépítették az összes visszajelzést? 

Példaválasz: Azt szeretnénk, hogy az érdekelt felek szavazzanak egy ADR-ről, amikor az aktív csapat 1) befejezte a kutatását, 2) befejezte az értékelését, 3) közzétette az ADR-javaslatot az érdekelt feleknek észrevételkéréssel és egyhetes határidővel, 4) minden érdekelt féli észrevételt beépítettek és kezeltek.

### Milyen szerepkörök és felelősségek kapcsolódnak egy ADR-hez?

Gondoljon olyan szerepkörökre, mint kezdeményező, kutató, értékelő, felülvizsgáló, jóváhagyó, karbantartó és hasonlók. Gondoljon olyan felelősségekre, mint az érdekelt felekkel való kommunikáció, az elvárások teljesülésének biztosítása, a weboldalon vagy intraneten való megosztás, valamint a munka időszakos felülvizsgálata, különösen releváns változások esetén.

Példaválasz: Azt szeretnénk, hogy minden ADR-nek mindig legyen elsődleges kapcsolattartója, másodlagos kapcsolattartója és felelős csapata; ezek felelnek a kommunikációért, a közzétételért, a karbantartásért, az évente legalább egyszeri időszakos felülvizsgálatért és szükség esetén a végső kivezetésért.

### Hogyan kapcsolódik az irányítás egy ADR-hez?

Gondoljon olyan területekre, mint a szervezet munkamódszerei, különleges megfelelőségi igények, például jogi vagy humánerőforrás-szempontok, és hogyan kíván bánni a konszenzussal, a konfliktussal és az eszkalációval. Vannak-e olyan területek, személyek vagy csapatok, amelyeknek nagyobb befolyásuk lehet egy ADR-re, például jóváhagyhatják, szavazhatnak róla vagy megvétózhatják?

Példaválasz: Az ADR irányítása ebben a prioritási sorrendben történik: vezérigazgató (CEO), technológiai igazgató (CTO), jogi igazgató (CLO), az ADR-t megvalósító csapat, a csapat azon szakértői, akik a legjobban ismerik az architekturális döntést. Senki másnak nincs irányítási joga, kivéve, ha az ADR leírja. 

### Milyen alapelvek kapcsolódnak egy ADR-hez?

Gondoljon olyan területekre, mint a szervezet munkamódszerei, amelyek magukban foglalják a gyors és a lassú haladást, a döntési konszenzust és a döntési konfliktust, a kockázati és a biztonsági preferenciákat, a nyilvános és a magánvitát és hasonlókat.

Példaválasz: A cselekvéshajlam, az egyet nem értés melletti elköteleződés (disagree-and-commit), a könnyen visszafordítható, könnyen elszigetelhető döntéseknél elegendő 70%-os becslések és a nyilvános munkamódszerek vezetési elveit alkalmazzuk, kivéve a szervezetünk titoktartási megállapodásában leírt bizalmas információkat.

## Következő lépés koncepciók ADR-ekhez

Az [Arc42](https://arc42.org/) pragmatikus módon válaszol két kérdésre, és az Ön konkrét igényeihez igazítható. Mit érdemes dokumentálnia/közölnie az architektúrájáról? Hogyan érdemes dokumentálnia/közölnie? Az Arc42 tartalmaz architekturális döntési feljegyzéseket, valamint útmutatást a célokról, megszorításokról, háttérről, minőségről, kockázatokról és egyebekről.

A [C4-modell](https://c4model.com/) könnyen tanulható, fejlesztőbarát megközelítés a szoftverarchitektúra diagramozásához. A C4 hierarchikus diagramok készlete a háttérhez, konténerekhez, komponensekhez, kódhoz, valamint kiegészítő diagramok a rendszertájképhez, a dinamikához és a telepítéshez.

## Architekturális diagramok, nézetek és nézőpontok

Az architekturális diagramot „architekturális nézetnek” nevezzük.

Az „architekturális nézet” egy „architekturális nézőpont” példánya.

Az „architekturális nézőpontnak” meghatározott közönsége van, meghatározott szempontokat szem előtt tartva.

Architekturális nézőpontok, nézetek és diagramok példái:

- Üzleti képességek

- Magas szintű üzleti folyamatok

- [Értékáramok](https://en.wikipedia.org/wiki/Value_stream)

- Alkalmazáskomponensekre leképezett szoftverfunkciók

- [C4-modell](https://en.wikipedia.org/wiki/C4_model) kontextusdiagram (TO-BE / AS-IS)

- [C4-modell](https://en.wikipedia.org/wiki/C4_model) konténerdiagram (TO-BE / AS-IS)

- [Egyed-kapcsolat diagram](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) az adategyedek alkalmazáskomponensekre való leképezéséhez

- [Szekvenciadiagramok](https://en.wikipedia.org/wiki/Sequence_diagram) a rendszereken belüli és integrációs funkcionális folyamatok leírásához

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagramok az alkalmazáskomponensek közötti adatfolyamok leírásához

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagramok az üzleti folyamatok / felhasználói forgatókönyvek leírásához

- [Identity and Access Management](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) diagramok

- [Role-Based Access Control](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) diagramok alkalmazáskomponensenkénti szerepkörökkel

- [Attribute-Based Access Control](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) diagramok alkalmazáskomponensenkénti attribútumokkal

- Adatvédelmi diagramok

Kapcsolódó diagramok:

- A használatieset-diagram a használati eseteket mutatja a vezetésnek/ügyfeleknek, ami megelőzi a követelményeket, amelyek megelőzik a szoftverarchitektúrát.

- A telepítési diagram azt a fizikai hardvert/számítógépeket mutatja, amelyekre a szoftverkomponenseket telepítik.
- Az adatfolyam-diagram azt mutatja, hogyan mozognak az adatok a rendszerben, és hogyan alakulnak át.
- A szekvenciadiagram annak bemutatására szolgál, hogyan működnek az olyan protokollok, mint a HTTP, időtengelyen.

- A tevékenységdiagram egy szoftverrendszer által végzett tevékenységek munkafolyamatát ábrázolja, például egy NPC MI-jét.

## Alkalmassági függvények döntésekhez kódként

Az alkalmassági függvények (fitness functions) objektív, automatizált ellenőrzések, programkóddal írva, amelyek igazolják, hogy a döntéseket betartják.

- Az alkalmassági függvények tesztelhetővé és biztosíthatóvá teszik a döntéseket.

- A döntésekhez tartozó alkalmassági függvények nagyban segíthetik a minőségbiztosítást, a szabályozási folyamatokat és az irányítási célokat.

### Hogyan kapcsolódnak az alkalmassági függvények a döntésekhez

A döntési feljegyzés dokumentálja a döntést, míg az alkalmassági függvény biztosítja azt.

- Példa döntés: Eseményforrást (event sourcing) használunk az auditkövetelmények miatt.

- Példa alkalmassági függvény: A folyamatos integrációs kiszolgálóval teszteljük, hogy minden állapotváltozásnak eseményeket kell létrehoznia.

### Miért segítenek az alkalmassági függvények a döntéseken

Objektív mérések: Az alkalmassági függvények sikeresek vagy sikertelenek, így a munka látható és világos.

Folyamatos használat: Az alkalmassági függvények az Ön élő szabályai, minden commitnál és buildnél lefutnak.

Magabiztosság az újraszervezésben: Az alkalmassági függvények automatikusan elkapják a döntési szabályok hibáit.

Skálázható irányítás: Az alkalmassági függvények szűk keresztmetszetek létrehozása nélkül biztosítják a szabványokat.

### Használhatnak-e az alkalmassági függvények mesterséges intelligenciát?

Az alkalmassági függvények kihasználhatják az MI nagy nyelvi modelljeit (LLM) a döntésekhez, kérdéseket téve fel a munkájáról,
például a terveiről, a kódjáról, a sémáiról, az API-iról és egyebekről:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Architektúra egységtesztelése

[ArchUnit](https://www.archunit.org/): Java-kód architekturális szabályainak ellenőrzése bármely egyszerű Java egységtesztelő keretrendszerrel.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): TypeScript- és JavaScript-kód architekturális szabályainak ellenőrzése Jest, Vitest, Jasmine stb. használatával.

## Döntési korlátok pull requestekhez

A [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
automatikusan felszínre hozza a megfelelő döntési feljegyzéseket a megfelelő pillanatban — amikor
egy fejlesztő aktívan módosítja azt a kódot, amelyet ezek a döntések lefednek. Ahelyett, hogy
abban bíznánk, hogy a fejlesztők elolvasnak egy dokumentációs mappát a beolvasztás előtt, a releváns háttér
közvetlenül a pull requesten jelenik meg.

Ez bármilyen típusú döntési feljegyzésnél működik: architekturális döntéseknél, adatdöntéseknél,
megfelelőségi döntéseknél, klinikai és orvosi döntéseknél, biztonsági döntéseknél és egyebeknél.

Bármely CI-rendszerrel (GitLab, Jenkins, CircleCI) és pre-commit hookként is működik.
Nyílt forráskódú. MIT licenc.

Az [ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) egy GitHub
Action, amely megbuktat egy pull requestet, ha a megfigyelt kódutak megváltoznak
anélkül, hogy architekturális döntési feljegyzést adnának hozzá vagy frissítenének. A mentességek
kifejezettek: egy `ADR-Exempt:` sor indoklással átengedi a kaput, és beíródik a feladat
összefoglalójába. Sablonfüggetlen, függőségek nélkül. Nyílt forráskódú. MIT licenc.

## További információ

Bevezetés:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Sablonok:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Elmélyülés:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - ingyenes havi szoftverarchitektúra-lecke

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Eszközök:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Cégspecifikus útmutatás:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Példák:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Videók:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcastok:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Könyvek:

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

Lásd még:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Szállítósemleges, géppel olvasható YAML/JSON formátum döntések kifejezett indoklással, feltevésekkel, kognitív állapottal és kompromisszumokkal való ábrázolására. Kiegészíti az ADR-eket azzal, hogy strukturált, validálható indoklást ad a döntésdokumentációhoz.
