
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
