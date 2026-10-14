# Microsoft Azure DevOps

Tartalom:

* [Összefoglaló](#összefoglaló)
  * [Probléma](#probléma)
  * [Döntés](#döntés)
  * [Állapot](#állapot)
* [Részletek](#részletek)
  * [Feltevések](#feltevések)
  * [Megszorítások](#megszorítások)
  * [Álláspontok](#álláspontok)
  * [Érv](#érv)
  * [Következmények](#következmények)
* [Kapcsolódó](#kapcsolódó)
  * [Kapcsolódó döntések](#kapcsolódó-döntések)
  * [Kapcsolódó követelmények](#kapcsolódó-követelmények)
  * [Kapcsolódó artefaktumok](#kapcsolódó-artefaktumok)
  * [Kapcsolódó alapelvek](#kapcsolódó-alapelvek)
* [Megjegyzések](#megjegyzések)
  * [Microsoft Devops CI: An Unsatisfying Adventure](#microsoft-devops-ci-an-unsatisfying-adventure)
  * [A Hacker News-beszélgetés kiemelései](#a-hacker-news-beszélgetés-kiemelései)
  * [Windows Development MVP](#windows-development-mvp)
  * [Edward Thomson (Azure PM) összefoglalója](#edward-thomson-azure-pm-összefoglalója)


## Összefoglaló


### Probléma

Devopst szeretnénk használni a projektjeink építéséhez, integrálásához, telepítéséhez és üzemeltetéséhez. A Microsoft Azure DevOpsot fontolgatjuk.

  * Azt szeretnénk, hogy a fejlesztői élmény gyors és megbízható legyen, mind a devops beállításánál, pl. a konfigurálásnál, mind a folyamatos használatnál, pl. gyors build-idők.
  
  * Fontolóra szeretnénk venni a Microsoft Azure egészként való használatát a projektalkalmazások, adatbázisok stb. üzemeltetéséhez.


### Döntés

A Microsoft Azure DevOps ellen döntöttünk.


### Állapot

Eldöntve. Nyitottak vagyunk az újragondolásra, ha/amikor új jelentős információ érkezik.


## Részletek


### Feltevések

Az összes szokásos devops-feltevés, mint az Accelerate című könyvben.

  * A gyors buildek jelentősen segítenek. Ez felgyorsítja a visszajelzési hurkokat.

  * Elemeket cserélhetünk be/ki más szállítóktól, azaz lehet, hogy hozni akarjuk a saját gyorsabb build-kiszolgálóinkat, vagy a saját verziókezelő rendszerünket használni, vagy egy saját üzemeltetésű folyamatos integrációs kiszolgálóval koordinálni.
  
  * Az egyszerűsített használhatóság jelentősen segít a fejlesztői élményben, és ezáltal olyan finom területeken, mint a következetesség, az érthetőség, a biztonság és a tanulási görbe könnyűsége.

  * Amikor valami elromlott vagy problémás, hatékony módot szeretnénk a probléma jelentésére. Ez különösen fontos a biztonsággal kapcsolatos problémáknál.


### Megszorítások

Nincs ismert. Az Azure-nak közzétett elköteleződése van, hogy jól együttműködik külső eszközökkel.


### Álláspontok

Megfontoltuk a Microsoft Azure Devopsot az AWS-szel szemben, amely a jelenlegi megoldás.

Kísérleteztünk az Azure DevOpsszal, az Azure Pipelinesszal, az Azure Repóval és új kiszolgáló Azure-ban való felállításával Terraformon keresztül.

Kísérleteztünk a Microsoft képviselőitől való támogatás kérésével.

Információkat gyűjtöttünk társaktól blogokon és a Hacker Newson.


### Érv

Az Azure DevOps kiváló ajánlatkészletet hirdet, de azok nem állják ki a próbát, nem működnek jól együtt, és a támogatás gyenge.

A saját első kézből szerzett tapasztalatunk:

  * Az Azure beállítása felületek zűrzavara, amelyek egy része átfedésben van a Microsoft-fiókokkal, egy része nem. Pl. van Azure-bejelentkezés, Microsoft.com-bejelentkezés, Live.com-bejelentkezés stb., és mind egyszerre játékban van.

  * Kisebb biztonsági problémába ütköztünk a beállítás során, és nem találtunk megoldást. Sokféleképpen próbáltuk jelenteni, sok Microsoft-képviselőnek, sikertelenül. Sikeresen jelentettük a Microsoft biztonságának, amely azt válaszolta, hogy nem javítja.

  * A dokumentáció gyakran vagy téves, vagy elavult. Ennek legalább egy része a Microsoft gyenge keresőmotorjának tudható be, egy része az átlag alatti SEO-nak.
  
  * A Terraform-beállítás jól dokumentált, és működik. A Terraform-támogatás azonban gyenge az AWS-hez képest, mert a Microsoft üzleti kapcsolatokat épít a szállítókkal, hogy láncolt Terraform-beállítási példákat készítsenek.

A társak tapasztalatai:

  * Miután elvégeztük a saját vak értékelésünket, társak tapasztalatait kerestük. Amit találtunk, megerősítette a tapasztalatainkat.

  * A társak további problémákat jeleztek a build-időkkel és a saját build-kiszolgáló hozásával. Ezek a problémák jelentősen súlyosabbak, mint a felületi problémák, mert a buildek készítése a build-csővezeték fő célja, és sokat várunk naponta.

  * Kiváló részvételt találtunk az Azure-csapattársak részéről a vitaterületeken. Dicséret a Microsoftnak ezért. Különösen lenyűgöz minket Edward Thomson, az Azure PM-je és programozója, a részvétele, egyenessége és műszaki magyarázatai miatt.


### Következmények

A Microsoft Azure DevOps választása valószínűleg drágább (~3x) időben és költségben, mint az Azure nem választása.


## Kapcsolódó


### Kapcsolódó döntések

Ha az Azure DevOpsot választjuk, számos kapcsolódó ajánlat van, köztük az Azure Repo, az Azure Pipeline stb. Úgy véljük, hogy ha az Azure Devopsot választjuk, ez megkönnyítheti több Azure-képesség használatát, vagy megnehezítheti más szállítók képességeinek használatát.

Úgy véljük, hogy a Microsoft nagy lépéseket tesz a fejlesztői élmény terén, és látjuk, hogy a Microsoft nagy fejlesztői eszköz- (pl. GitHub) és függőségvásárlásokat (pl. Citus) hajt végre.

Ha az Azure DevOpsot választjuk, érdemes lehet hangsúlyt helyezni a Microsoft-felvásárlások ajánlatainak választására, és a felvásárlási ajánlatokhoz is nagyobb gonddal/értékeléssel közelíthetünk a lehetséges szövetkilökődés miatt, pl. a munkaerő-fluktuáció kockázata.


### Kapcsolódó követelmények

Azt szeretnénk, hogy a build-idők nagyon gyorsak legyenek. Elfogadjuk, hogy ezért magas felárat fizetünk. Ez azért, mert nagyon gyorsan akarunk iterálni.

Azt szeretnénk, hogy a megbízhatóság nagyon magas legyen. Elfogadjuk, hogy ezért magas felárat fizetünk. Ez azért, mert nagy értékű felhasználási eseteket tesztelünk, beleértve pénzügyi tranzakciókat, bizalmas tranzakciókat stb.

A legfontosabb 4 devops-KPI-nk közé tartozik az átlagos helyreállítási idő, amely gyors buildeket és magas megbízhatóságot igényel.


### Kapcsolódó artefaktumok

Azt szeretnénk, hogy a buildrendszer olyan artefaktumokat állítson elő, amelyek alkalmasak más rendszerekben való használatra, mint az Artifactory.


### Kapcsolódó alapelvek

Könnyen visszafordítható. Az Azure DevOpsot párhuzamosan értékelhetjük a jelenlegi AWS-szel.


## Megjegyzések


### Microsoft Devops CI: An Unsatisfying Adventure

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Blogbejegyzés.

„Szoftverfejlesztőként első kézből tudom, mennyire nehéz gyorsan és olcsón minőségi termékeket építeni. Ez egy olyan művészet, amelyet néha jól csinálunk, máskor az Obama-korszak egészségügyi kormányzati oldalához hasonlóvá fajul. Az eredményül kapott termék feletti kontrollunk szintje változó, és a kudarc felelőssége gyakran rossz embereket terhel a döntéshozatali hierarchiában. A Microsoft Azure DevOps (korábban Visual Studio Team Services), a nyilvánvalóan jó szándék ellenére, a rossz döntések és a gyenge kivitelezés tökéletes vihara.”


### A Hacker News-beszélgetés kiemelései

https://news.ycombinator.com/item?id=18983586

„Kiterjedten használjuk az Azure DevOpsot a munkahelyemen, és miután használtam GitHubot, Gitlabot, saját üzemeltetésű megoldásokat, Jenkinst, TeamCityt... az Azure DevOps az utolsó helyen áll.”

„A felület mindenhol szörnyen darabos. A legrosszabb nekem a pull requestek. Hihetetlenül nehéz emberekkel együtt dolgozni egy pull requesten. Még azt sem tudom megmutatni, hogy „egy” konkrét probléma — nálunk mindenhol elromlott.”

„Az Azure Devops valami, amit szeretnék szeretni. A felület folyton változik, de nem javítja a régóta fennálló mögöttes hibákat.”

„Az eszközök nincsenek jól integrálva, a felület nagyon lassú, nincs irányítópult-nézet az aktív pull requestekről, buildekről, kiadásokról stb. a kedvenc tárolóimhoz. A Build/Deploy idők őrülten lassúak.”

„Megpróbáltuk az Azure Boardsot (Work Items, Boards, Backlogs stb.) is használni. Au. Ez teljes UI-zűrzavar, széteső ötletekből. Ahelyett, hogy egy dolgot jól valósítottak volna meg, két tucat dolgot valósítottak meg borzalmasan.”


### Windows Development MVP

Windows Development MVP itt. Úgy érzem, nekem is vállalnom kell valamennyi felelősséget, amiért nem beszéltem hangosabban ezekről a problémákról. De mondanom kell, csalódott vagyok, hogy „meglepődnek” az UX-problémákon. Mondtam az embereiteknek, hogy az UX borzalmas (pl. már a bevezetés előtt), és folyton azt hallottam: „tudjuk, javítjuk”. Elkezdem formalizálni a visszajelzést, és átnyomni a csöveken, maradjatok velünk. Helyi vagyok (Bellevue), szívesen bemennék, és megpróbálnám pipeline-ba tenni a viszonylag egyszerű oss .net/wpf/uwp alkalmazásunkat. Gyanítom, hogy mindkettőnknek szemnyitogató lesz.

Néhány példa:

* Nem lehet pipeline-t építeni olyan git-tárolóval, amely almodulokat tartalmaz

* Lehetetlennek találtam a PATH szerkesztését néhány egyedi eszközhöz

* A New Pipeline élménynek egyszerűen nincs sok értelme, az újonnan kattintgató felhasználók végül a rossz dokumentációhoz jutnak.


### Edward Thomson (Azure PM) összefoglalója

Én írtam azt a kódot, amely beolvasztja a pull requesteket. Program Manager a Microsoftnál az Azure DevOpshoz; korábban szoftvermérnök verziókezelő eszközökön a GitHubnál, a Microsoftnál, a SourceGearnél.

https://www.edwardthomson.com/

A libgit2 társ-karbantartója. https://libgit2.github.io

Az All Things Git, a Gitről szóló podcast társ-műsorvezetője. https://www.allthingsgit.com/

A Developer Tools Weekly, a fejlesztői eszközökről szóló hírlevél gondozója. https://developertoolsweekly.com/
