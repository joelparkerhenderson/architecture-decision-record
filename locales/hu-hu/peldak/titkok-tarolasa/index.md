# Titkok tárolása

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
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Összefoglaló


### Probléma

Titkokat kell tárolnunk, például jelszavakat, privát kulcsokat, hitelesítési tokeneket stb.

Néhány titok felhasználóorientált. Például a fejlesztőnk szeretné a mobiltelefonját használni, hogy megnézze egy szolgáltatás jelszavát.

Néhány titok rendszerorientált. Például a folyamatos szállítási csővezetékünknek tudnia kell megkeresni a felhőhosztingunk hitelesítő adatait.


### Döntés

Bitwarden a felhasználóorientált titkokhoz

Vault by HashiCorp a rendszerorientált titkokhoz.


### Állapot

Eldöntve. Nyitottak vagyunk az új alternatívákra, ahogy felmerülnek.


## Részletek


### Feltevések

Erre a célra és jelenlegi állapotunkban értékeljük a felhasználóorientált kényelmet, például a használható mobilalkalmazásokat.

  * Gyors, egyszerű mozgás közbeni hozzáférést szeretnénk biztosítani, például egy ügyeletes rendszermegbízhatósági mérnököt végző fejlesztő számára.

  * Szeretnénk bizonyos titkokat megosztani kiválasztott személyek, például egy csapat között.

Nem egyetlen szolgáltatóra próbálunk megoldást adni, például az összes titok kizárólag az Amazonon, az Azure-on vagy a Google-nél való tárolására.

Nem akarunk ad hoc megközelítéseket, mint a „jegyezd meg” vagy a „írd fel egy cetlire” vagy a „találd ki a saját módod a tárolásra”.

Biztonsági modellünk erre a célra rendben van jól tekintett COTS-szállítók, például SaaS jelszókezelő eszközök használatával.


### Megszorítások

Most valami egyszerűt szeretnénk, vagyis nincs szükség kód írására, kiszolgálók telepítésére, komoly elköteleződésre, mindenki szabványosítására.


### Álláspontok

Megfontoltuk:

1. Kész, felhasználóorientált jelszókezelők: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG stb.

2. Rendszerorientált COTS jelszókezelők: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Megosztásorientált megközelítések: megosztott Google-dokumentum, megosztott Slack-csatorna, megosztott hálózati mappa stb. használata.

4. Alacsony technológiájú ad hoc megközelítések, mint a megjegyzés, a cédulaírás vagy az, hogy minden felhasználó maga találja ki a saját módszerét.


### Érv

A Bitwarden, a LastPass, az 1Password és a Dashlane mind kereskedelmi kész termékek.

  * Hasonló típusú funkciók felhasználóknak, csapatoknak, szervezeteknek stb.

  * Asztali képesség Windowshoz és Machez, és mobil képesség Androidhoz és iOS-hez.

  * Böngészőbővítmények Chrome-hoz és Firefoxhoz, automatikus űrlapkitöltéshez stb.

A Bitwardennek két előnye van a többivel szemben:

  * A Bitwarden nyílt forráskódú, ami azt jelenti, hogy a biztonság társak által felülvizsgálható, és a céget a biztonságorientált fejlesztők széles körben nagyra értékelik.

  * A szoftveres dolgozók anekdotái jelentős preferenciát írnak le a Bitwarden iránt a többivel szemben.

Egy tipikus jó cikk: https://jcs.org/2017/11/17/bitwarden

Egy tipikus egymás melletti szavazóoldal: https://stackshare.io/stackups/bitwarden-vs-dashlane

A KeyPasst, passt, GPG-t stb. elhalasztjuk, mert további bonyolultság van bennük. Mindegyik jó megoldásnak tűnik műszaki felhasználók számára. A GPG különösen jónak tűnik azoknak a műszaki felhasználóknak, akik rendszerek közötti, parancsorientált képességeket akarnak.

A KMS-t elhalasztjuk, mert egyetlen szolgáltatóhoz köt.

A Vaultot választjuk a rendszerorientált igényekhez, mert az értékelések elképesztően pozitívak, és mert a HashiCorpnak kiváló eredménytörténete van csúcsminőségű szoftverek és támogatás terén.

Megvétózzuk a megosztási megközelítéseket, például megosztott dokumentumokon, megosztott csatornákon, megosztott hálózati mappákon stb. keresztül. Ezek nem nyújtják azokat a biztonsági minőségeket, amelyeket szeretnénk.

Megvétózzuk az alacsony technológiájú ad hoc megközelítéseket, mert mindannyian egyetértünk abban, hogy ez nem hosszú távú járható út.


### Következmények

A fejlesztőknek esetleg két helyen kell nyomon követniük a titkokat: Bitwarden a felhasználóorientált hozzáféréshez és Vault a rendszerorientált hozzáféréshez.


## Kapcsolódó


### Kapcsolódó döntések

A CI/CD-kiszolgálóról szóló döntésnek tartalmaznia kell a titkokhoz való hozzáférési képesség bizonyítékát.

Dönteni kell majd arról, hogyan kezeljük a titkokat, szabályzatok, rotációk, szervezetek stb. tekintetében.


### Kapcsolódó követelmények

A titkokhoz kapcsolódó követelmények lesznek a megfelelőségre, az auditálásra és a HR-es belépésre/kilépésre.


### Kapcsolódó artefaktumok

Várjuk, hogy egyes titkokat környezeti változókba exportálhatunk.


### Kapcsolódó alapelvek

Könnyen visszafordítható.

Könnyen párhuzamos, azaz könnyű különféle jelszókezelőket használni.

Olcsó kipróbálni, azaz van ingyenes próba és nincs elköteleződés.


## Megjegyzések

Értékelési jegyzetek itt. A jegyzetek mind nyilvános megjegyzések különféle devops-vitafórumokról.


### Vault by HashiCorp

A Vault pontosan az, amire itt szükség van. 

Ne dobd azonban egyből élesbe a Vaultot, előbb állítsd fel tesztkörnyezetben, mert a HashiCorp dokumentációja elég hiányos lehet, még ha a termékeik csodálatosak is.

Nagyon meredek tanulási görbe, és nem triviális felállítani. 

A kezdeti beállítás kissé szívás. Bőven megéri, és a közösség eléggé támogatja ahhoz, hogy boldogulj.

Borzalmas dokumentáció, de sok útmutató van online olyanoktól, akik beállították, és ha párat összerakol, működő beállításod lesz.

A kezdeti beállítás a helm chartjaik (vault és consul) piszkálását igényelte. Bár technikailag sok más backendet használhatsz, tényleg nem javaslom. A backend/consul pici lehet, ha nincs sok tárolandó adatod.

Mindenképpen ismerkedj meg a CLI használatával, mert a GUI inkább proof-of-concept/reklámportál az enterprise kiadásukhoz.

Az, hogy nem tudod egyszerűen „feltölteni”, szívás. Például ha 5 meződ van, minden elemhez kézzel kell hozzáadnod minden mezőt. Tehát nem úgy van, hogy előre definiálsz mezőket egy adott kategóriához, és kitöltöd őket a kategória összes eleméhez, hanem inkább „mindent mindig újra előállítasz”, ami (szerintem) fájdalom a fenekemben.

Érdemes lehet a goldfisht is megnézni a vault fölötti felületként. Elég kellemessé teszi a csapat meggyőzését. Van demójuk is. 1. Állítsd be a consult. 2. Állítsd be a vaultot a consulra mutatva. 3. Állítsd be a goldfisht a vaultra mutatva. 3. Állíts be egy cron-feladatot, amely consul snapshotot futtat biztonsági mentésekhez.



### LastPass

LastPass Teams. Használjuk, vannak egyedi sablonjai, ACL-je, szerintem nem hiányzik semmi.

Bevezettem a LastPasst a szervezetemben, és C+/B- értékelést adok neki. A legnagyobb probléma mostanában a megbízhatóság hiánya. Az elmúlt 90 napban több órán át a széfeket kényszerítették offline módba. Ez nem ideális a szervezetemnek, mert szó szerint több mint 4000 jelszó van tárolva több mint 20 megosztott mappában. Ahogy el tudod képzelni, ennyi jelszónál naponta legalább néhányat frissítenek vagy adnak hozzá. Van DR-tervünk arra az esetre, ha a problémák egy-két óránál tovább tartanak: egy szkript minden éjjel aláír és titkosít egy CSV-exportot a széfről, amely importálható a keepassba.

A LastPassnak voltak be nem jelentett pillanatai romlott szolgáltatással: a bejelentkezés „működik”, de nem húzza le az oldalakat, véletlenszerű funkciók hibásak az adminisztrációs panelen, és nem osztja meg helyesen a kulcsokat az új legfelső szintű megosztott mappákhoz. Van egy speciális „key push”/mentési felhasználóm, aki minden csoportban benne van. Általában az ezzel a felhasználóval való bejelentkezés megjavítja a kulcsmegosztási problémákat, de nem akkor, ha a szolgáltatás romlott, bármit mond is az állapotoldal...

Az integráció egyszerű lehet, ha megfelelő ACL-ek vannak a legkisebb jogosultság modelljével, pl. ha egy felhasználónak olvasási és írási, valamint csak olvasási jogosultsága is van egy bejegyzésen vagy mappán, csak olvasási jogot kap. Sajnos a szervezetem ACL-jei nem a legjobbak, ezért a JSON provisioning API-t és ~500 sor Pythont használtam, mert több száz ACL-ünk függő jellege nem illeszkedik jól a legkisebb jogosultság modelljéhez. Végül lekértem az összes ACL-t, amelyben egy felhasználó benne van, és egyfajta függőségi bejárást végeztem.

Ha az ACL- vagy csoportszerkezeted már a legkisebb jogosultság szem előtt tartásával épült, az AD/LDAP-szinkronizációs eszköz Windowshoz jól fog működni.

Vedd fel a kapcsolatot az értékesítési csapatukkal, és szereznek egy hosszabb Enterprise próbaverziót. Győződj meg róla, hogy teljesen megérted a korlátait, mielőtt meghúzod a ravaszt. Elég sok növekedési fájdalmunk volt, de a kiszolgálóoldali kimaradásokat vagy romlásokat leszámítva hihetetlenül zökkenőmentes volt.


### Bitwarden

A Bitwarden körül szép eszközök vannak (WebUI, CLI, mobil, asztali). Saját üzemeltetésű és elég könnyen beállítható. Elég jó dokumentáció, és a PrivacyTools által ajánlott eszköz.


### EnvKey

https://www.envkey.com/ SaaS. Nagyon könnyű megvalósítani, integrálni és kezelni.

Funkciók:

  * Védi az API-kulcsokat és hitelesítő adatokat.

  * Mindenhol szinkronban tartja a konfigurációt.

  * Okos, végpontok közötti titkosítású konfigurációs és titokkezelés. 

  * Megakadályozza a nem biztonságos megosztást és a konfiguráció burjánzását. 

  * Percek alatt integrálható.

Képességek:

  * Egy helyen kezeli a konfigurációt és a hozzáférési szinteket az összes alkalmazásodhoz, környezetedhez és csapatodhoz.

  * Bármely fejlesztési vagy kiszolgálói környezetet konfigurál egyetlen környezeti változóval.

Előnyök:

  * Jó főoldal.

  * Világos értékajánlat.

  * Vizuálisan kiváló webalkalmazás.

  * Kiváló példaadatok, pl. Algolia, AWS, Datadog, GitHub, Stripe stb.

  * Beszéltem az alapítóval 30 percet a cégről, a felületről stb. Dane tájékozottnak, a pro/kontra kérdésekben őszintének és életképes partnernek hangzik.

  * A cég lényegében egy tipikus Y Combinator-cég, 1 alapítóval. 2018-01-ben 120 000 dollárt gyűjtött.

  * A fókusz az enterprise funkciók elérésén van, főleg az EnvKey felhőhosztingról on-premre vagy BYOC-re való átlépésen.

  * Lehetséges út: kezdés az EnvKey-jel a használhatóság kedvéért, majd később (vagy párhuzamosan) a Vault hozzáadása. 


### Confidant by Lyft

https://lyft.github.io/confidant/

A Confidant nyílt forráskódú titokkezelő szolgáltatás, amely felhasználóbarát tárolást és biztonságos hozzáférést nyújt a titkokhoz, a Lyft fejlesztőitől.

KMS-hitelesítés: A Confidant megoldja a hitelesítési tyúk-tojás problémát az AWS KMS és az IAM használatával, hogy az IAM-szerepkörök biztonságos hitelesítési tokeneket generálhassanak, amelyeket a Confidant ellenőrizni tud. A Confidant az IAM-szerepköreid KMS-engedélyeit is kezeli, ami lehetővé teszi az IAM-szerepköröknek, hogy olyan tokeneket generáljanak, amelyek szolgáltatás-szolgáltatás hitelesítéshez vagy titkosított üzenetek szolgáltatások közötti átadásához használhatók.

Verziózott titkok nyugalmi állapotú titkosítása: A Confidant a titkokat csak hozzáfűzéses módon tárolja a DynamoDB-ben, minden titok minden revíziójához egyedi KMS-adatkulcsot generálva, Fernet szimmetrikus hitelesített kriptográfiával.

Felhasználóbarát webes felület a titkok kezeléséhez: A Confidant AngularJS webes felületet nyújt, amely lehetővé teszi a végfelhasználóknak, hogy könnyen kezeljék a titkokat, a titkok szolgáltatásokhoz rendelését és a változások előzményeit.


### Devolutions Password Server

https://server.devolutions.net/

Biztosítsd, kezeld és figyeld a privilegizált fiókokhoz és munkamenetekhez való hozzáférést.

Átfogó, erősen védett jelszószéf, amely lehetővé teszi, hogy ellenőrizd a privilegizált fiókjaidhoz való hozzáférést, miközben javítja a rendszergazdák számára a hálózat általános láthatóságát, és zökkenőmentes élményt nyújt a végfelhasználóknak.

Funkciók: központosított szervezeti jelszószéf, felhasználóspecifikus privát széf, jelszókezelő, hitelesítő adatok beinjektálása,
Active Directory-integráció, szerepköralapú hozzáférés-vezérlés, kétfaktoros hitelesítés, enterprise-ra kész, IP-korlátozások, kezelési képességek, automatizált jelszógenerátor, mobilalkalmazás-hozzáférés, jelszóelőzmények, hozzáférési jelentések, e-mail riasztások.

  * támogatja az adattitkosítást

  * támogat több hitelesítési sémát, köztük LDAP-ot, O365-öt és helyi felhasználókat TÖBB FORRÁSBÓL ÉRKEZŐ MFA-támogatással

  * több tároló/széf finom szemcsézettségű hozzáférés-vezérléssel több csapat számára

  * modern webes felület

  * privát hitelesítőadat- és kapcsolatszéfek személyes hitelesítő adatokhoz/kapcsolatokhoz

  * mobilalkalmazások iOS-hez/Androidhoz

  * auditnaplók minden bejegyzéshez, ki/mi/mikor, opcionális kérdéssel arról, miért fér hozzá

  * testreszabható sablonok (bár natívan több száz kapcsolattípust támogatnak)

  * rengeteg további funkció és egy Windows/Mac vastag kliens (Remote Desktop Manager), amellyel szinkronizálhatsz, és ami nagyban bővíti a lehetőségeket... egykattintásos kapcsolatok

  * az árazás nem is olyan rossz - 15 felhasználóig évi 500 dollár a jelszókiszolgálóért


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

A helyi (on-premise) verzió funkciói: 

  * Teljes kontroll a végpontok közötti biztonsági rendszereid és infrastruktúrád felett

  * A szoftver telepítése a helyi adatközpontodban vagy a saját virtuális magánfelhő-példányodban

  * Olyan jogi és szabályozási kötelezettségek teljesítése, amelyek megkövetelik, hogy minden adat és rendszer helyben legyen

A felhőverzió funkciói:

  * A szoftver mint szolgáltatás modell lehetővé teszi, hogy regisztrálj és azonnal elkezdj

  * Rugalmas skálázhatóság, ahogy nősz

  * Az Azure által nyújtott ellenőrzések és redundancia 99,9%-os rendelkezésre állási SLA-val

Felhasználói visszajelzés:

  * Használtuk ezt a terméket. Annyira könnyen megkerülhető volt, és a szabályok csak okos embereknek működnek. A lusta vagy buta felhasználók könnyen elronthatják egy csapatterületen. Az árak tárgyalhatók, ha beszélsz velük.

  * Futtathatod SQL Express és egy Win 7 gép használatával. 

  * Olcsó.
