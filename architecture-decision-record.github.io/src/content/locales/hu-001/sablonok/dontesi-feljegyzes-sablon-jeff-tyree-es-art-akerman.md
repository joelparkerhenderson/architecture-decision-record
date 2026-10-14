# Döntési feljegyzés sablon – Jeff Tyree és Art Akerman

Ez az architekturális döntésleíró sablon, amelyet a ["Architecture Decisions: Demystifying Architecture", Jeff Tyree és Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf) tett közzé.

* **Probléma (Issue)**: Írja le a megoldandó architekturális tervezési problémát úgy, hogy ne maradjon kérdés arról, miért foglalkozik vele éppen most. Minimalista megközelítést követve csak azokat a problémákat kezelje és dokumentálja, amelyeket az életciklus különböző pontjain kezelni kell.

* **Döntés (Decision)**: Fogalmazza meg világosan az architektúra irányát — vagyis a választott álláspontot.

* **Állapot (Status)**: A döntés állapota, például függőben, meghozott vagy jóváhagyott.

* **Csoport (Group)**: Használhat egyszerű csoportosítást — például integráció, megjelenítés, adat stb. — a döntések halmazának rendszerezéséhez. Használhat kifinomultabb architektúra-ontológiát is, például John Kyaruzi és Jan van Katwijk ontológiáját, amely elvontabb kategóriákat tartalmaz, mint az esemény, a naptár és a hely. Például ezzel az ontológiával az olyan előfordulásokkal foglalkozó döntéseket, amelyekhez a rendszernek információra van szüksége, az esemény alá csoportosítaná.

* **Feltevések (Assumptions)**: Írja le világosan a környezet mögöttes feltevéseit, amelyben a döntést meghozza — költség, ütemterv, technológia stb. Vegye figyelembe, hogy a környezeti korlátok (például elfogadott technológiai szabványok, vállalati architektúra, általánosan alkalmazott minták stb.) korlátozhatják a megfontolt alternatívákat.

* **Megszorítások (Constraints)**: Rögzítse a környezetre vonatkozó további megszorításokat, amelyeket a választott alternatíva (a döntés) támaszthat.

* **Álláspontok (Positions)**: Sorolja fel a megfontolt álláspontokat (járható lehetőségeket vagy alternatívákat). Ezek gyakran hosszú magyarázatot, néha modelleket és diagramokat is igényelnek. Ez nem kimerítő lista. Mégsem szeretné a végső felülvizsgálaton hallani a „Gondoltak arra, hogy...?” kérdést; ez a hitelesség elvesztéséhez és más architekturális döntések megkérdőjelezéséhez vezet. Ez a szakasz abban is segít, hogy biztosan meghallgassa mások véleményét; más vélemények kifejezett kimondása segít megnyerni szószólóikat a döntéséhez.

* **Érv (Argument)**: Vázolja, miért választott egy álláspontot, beleértve olyan tételeket, mint a megvalósítási költség, a teljes birtoklási költség, a piacra jutás ideje és a szükséges fejlesztési erőforrások rendelkezésre állása. Ez valószínűleg ugyanolyan fontos, mint maga a döntés.

* **Következmények (Implications)**: Egy döntésnek sok következménye van, ahogy a REMAP metamodell jelzi. Például egy döntés bevezetheti más döntések meghozatalának szükségességét, új követelményeket hozhat létre vagy meglévőket módosíthat, további megszorításokat támaszthat a környezettel szemben, megkövetelheti a hatókör vagy az ütemterv újratárgyalását az ügyfelekkel, vagy további személyzeti képzést igényelhet. A döntés következményeinek világos megértése és kimondása nagyon hatékony lehet a támogatás megszerzésében és az architektúra végrehajtásának ütemtervéhez.

* **Kapcsolódó döntések (Related decisions)**: Nyilvánvaló, hogy sok döntés összefügg; itt felsorolhatja őket. Tapasztalatunk szerint azonban a gyakorlatban egy nyomonkövethetőségi mátrix, döntési fák vagy metamodellek hasznosabbak. A metamodellek hasznosak összetett kapcsolatok diagramszerű bemutatására (például Rose-modellek).

* **Kapcsolódó követelmények (Related requirements)**: A döntéseknek üzletvezéreltnek kell lenniük. A számonkérhetőség bemutatásához rendelje hozzá kifejezetten a döntéseit a célokhoz vagy követelményekhez. Itt felsorolhatja ezeket a kapcsolódó követelményeket, de tapasztalatunk szerint kényelmesebb egy nyomonkövethetőségi mátrixra hivatkozni. Értékelheti az egyes architekturális döntések hozzájárulását az egyes követelmények teljesítéséhez, majd azt, hogy a követelmény mennyire teljesül az összes döntés mentén. Ha egy döntés nem járul hozzá egy követelmény teljesítéséhez, ne hozza meg azt a döntést.

* **Kapcsolódó artefaktumok (Related artifacts)**: Sorolja fel a kapcsolódó architektúra-, tervezési vagy hatókördokumentumokat, amelyeket e döntés érint.

* **Kapcsolódó alapelvek (Related principles)**: Ha a vállalatnak van egy elfogadott alapelv-készlete, győződjön meg arról, hogy a döntés összhangban van egy vagy több közülük. Ez segít az összhang biztosításában a területek vagy rendszerek mentén.

* **Megjegyzések (Notes)**: Mivel a döntéshozatali folyamat hetekig is eltarthat, hasznosnak találtuk a csapat által a megismertetési folyamat során megvitatott jegyzetek és problémák rögzítését.

