# Sekretuen biltegiratzea

Edukia:

* [Laburpena](#laburpena)
  * [Arazoa](#arazoa)
  * [Erabakia](#erabakia)
  * [Egoera](#egoera)
* [Xehetasunak](#xehetasunak)
  * [Hipotesiak](#hipotesiak)
  * [Murriztapenak](#murriztapenak)
  * [Jarrerak](#jarrerak)
  * [Arrazoibidea](#arrazoibidea)
  * [Ondorioak](#ondorioak)
* [Erlazionatuta](#erlazionatuta)
  * [Erlazionatutako erabakiak](#erlazionatutako-erabakiak)
  * [Erlazionatutako eskakizunak](#erlazionatutako-eskakizunak)
  * [Erlazionatutako artefaktuak](#erlazionatutako-artefaktuak)
  * [Erlazionatutako printzipioak](#erlazionatutako-printzipioak)
* [Oharrak](#oharrak)
  * [HashiCorp-en Vault](#hashicorp-en-vault)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Lyft-en Confidant](#lyft-en-confidant)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Thycotic-en Secret Server](#thycotic-en-secret-server)


## Laburpena


### Arazoa

Sekretuak gorde behar ditugu, hala nola pasahitzak, gako pribatuak, autentikazio-tokenak eta abar.

Sekretu batzuk erabiltzaileei zuzenduak dira. Adibidez, gure garatzaileak bere telefono mugikorra erabili nahi du zerbitzu baten pasahitza bilatzeko.

Sekretu batzuk sistemei zuzenduak dira. Adibidez, gure etengabeko entrega-hodiak gure hodei-ostatatzearen kredentzialak bilatu behar ditu.


### Erabakia

Bitwarden erabiltzaileei zuzendutako sekretuetarako

HashiCorp-en Vault sistemei zuzendutako sekretuetarako.


### Egoera

Erabakia. Alternatiba berrietara irekiak gaude sortzen diren heinean.


## Xehetasunak


### Hipotesiak

Helburu honetarako, eta gure oraingo egoeran, erabiltzailearentzako erosotasuna baloratzen dugu, hala nola aplikazio mugikor erabilgarriak.

  * Joan-etorrian sarbide azkar eta erraza ziurtatu nahi dugu, adib. dei-zerbitzuko sistemen fidagarritasun-ingeniaritza egiten duen garatzaile baterako.

  * Sekretu batzuk pertsona hautatuen artean, adib. talde baten artean, partekatzeko gai izan nahi dugu.

Ez gabiltza hornitzaile bakar baterako konponbidea bilatzen, hala nola sekretu guztiak Amazon-en, Azure-n edo Google-n soilik gordetzea.

Ez ditugu nahi ad hoc ikuspegiak, hala nola "buruz ikasi" edo "ohar batean idatzi" edo "bilatu zeure gordetzeko modua".

Helburu honetarako gure segurtasun-ereduarekin ados gaude COTS hornitzaile errespetatuak erabiltzearekin, hala nola SaaS pasahitz-kudeaketako tresnak.


### Murriztapenak

Orain erraza den zerbait nahi dugu, hau da, ez dago koderik idatzi beharrik, ez dago zerbitzaririk instalatu beharrik, ez dago konpromiso handirik hartu beharrik, ez dago guztiak estandarizatu beharrik.


### Jarrerak

Hauek aztertu ditugu:

1. Erabiltzailearentzako pasahitz-kudeatzaile prest-egindakoak: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG, eta abar.

2. Sistemetarako COTS pasahitz-kudeatzaileak: AWS KMS, HashiCorp-en Vault, EnvKey, Thycotic-en Secret Server, Devolutions Password Server, Lyft-en Confidant.

3. Partekatzera zuzendutako ikuspegiak: Google dokumentu partekatua, edo Slack kanal partekatua, edo sareko karpeta partekatua, eta abar erabiltzea.

4. Teknologia txikiko ad hoc ikuspegiak, hala nola buruz ikastea, ohar bat idaztea, edo erabiltzaile bakoitzak bere ikuspegia asmatzea.


### Arrazoibidea

Bitwarden, LastPass, 1Password eta Dashlane denak produktu komertzial prest-egindakoak dira.

  * Erabiltzaileentzako, taldeentzako, erakundeentzako eta abarretarako ezaugarri antzekoak.

  * Windows eta Mac-erako mahaigaineko gaitasuna, eta Android eta iOS-erako gaitasun mugikorra.

  * Chrome eta Firefox-erako nabigatzaile-hedapenak, formularioak automatikoki betetzeko eta abar.

Bitwarden-ek bi abantaila ditu besteen aldean:

  * Bitwarden kode irekikoa da, hau da, segurtasuna kideek berrikus dezakete eta enpresa segurtasunera zuzendutako garatzaileek zabal estimatzen dute.

  * Software-langileen anekdotek Bitwarden-en aldeko lehentasun nabarmena deskribatzen dute besteen aldean.

Idazlan on tipikoaren adibidea: https://jcs.org/2017/11/17/bitwarden

Boto-gune tipikoaren alderaketa-gunea: https://stackshare.io/stackups/bitwarden-vs-dashlane

KeyPass, pass, GPG eta abar atzeratu egiten ditugu konplexutasun gehigarria dagoelako. Horiek guztiak irtenbide onak dirudite erabiltzaile teknikoentzat. GPG bereziki ona dirudi sistemen arteko komando-orientatutako gaitasunak nahi dituzten erabiltzaile teknikoentzat.

KMS atzeratu egiten dugu hornitzaile bakarrarekiko lock-in-a duelako.

Vault aukeratzen dugu sistemetarako behar horietarako, berrikuspenak harrigarriro positiboak direlako, eta HashiCorp-ek kalitate handiko software eta laguntzaren ibilbide bikaina duelako.

Partekatze-ikuspegiak, hala nola dokumentu partekatuen, kanal partekatuen, sareko karpeta partekatuen eta abarren bidezkoak, betoa jartzen diegu. Horiek ez dute nahi dugun segurtasun-kalitaterik ematen.

Ad hoc teknologia txikiko ikuspegiei betoa jartzen diegu, guztiok ados gaudelako ez dela epe luzerako bide bat.


### Ondorioak

Garatzaileek sekretuak bi lekutan jarraitu beharko dituzte agian: Bitwarden erabiltzaileentzako sarbiderako, eta Vault sistemetarako sarbiderako.


## Erlazionatuta


### Erlazionatutako erabakiak

Zein CI/CD zerbitzari erabakitzeak sekretuetara sartzeko gaitasunaren froga sartu behar du.

Sekretuak nola kudeatu erabaki beharko dugu, politika, errotazio, erakunde eta abarren aldetik.


### Erlazionatutako eskakizunak

Sekretuek betetze, ikuskaritza eta giza baliabideen (HR) onboarding/offboarding-erako eskakizun lotuak izango dituzte.


### Erlazionatutako artefaktuak

Espero dugu sekretu batzuk ingurune-aldagaietara esportatu behar izatea.


### Erlazionatutako printzipioak

Erraz atzera egin daitekeena.

Erraz paraleloa, hau da, pasahitz-kudeatzaile aniztasuna erabiltzea erraza da.

Probatzeko merkea, hau da, doako proba dago eta konpromisorik ez.


## Oharrak

Ebaluazio-oharrak hemen. Oharrak devops eztabaida-foroetako iruzkin publikoak dira denak.


### HashiCorp-en Vault

Vault da zehazki hemen nahi duzuna. 

Baina ez bota Vault produkzioan zuzenean, ezarri proba-ingurune batean lehenik, HashiCorp-en dokumentazioa nahiko urria izan baitaiteke produktuak liluragarriak izan arren.

Ikaskuntza-kurba oso aldapatsua du eta ez da hutsala ezartzea. 

Hasierako konfigurazioa nahigabe bat da. Hala ere, merezi du, eta komunitateak nahikoa ondo lagunduko du aurrera egiteko.

Dokumentazio ikaragarria baina lineako gida asko daude jendeak konfiguratzen dutenak eta horietako batzuk elkartzen badituzu konfigurazio funtzionala izango duzu.

Hasierako konfigurazioak haien helm chart-ekin (vault eta consul) jolastea eskatu zuen. Teknikoki beste back-end asko erabil ditzakezun arren, benetan ez dut gomendatzen. Back-end/consul oso txikia izan daiteke gordetzeko datu asko ez badituzu.

Ziur egin CLI erabiltzearekin eroso/ohituta egotea, GUI-a bere enpresa-edizioaren kontzeptu-froga/iragarki-atari bat baita gehiago.

Ezin duzula "betetzea" arazo bat da. Adibidez 5 eremu badituzu eskuz gehitu behar duzu eremu bakoitza elementu bakoitzerako. Beraz ez da kategoria jakin baterako eremuak aldez aurretik definitu eta kategoria horretako elementu guztietarako eremu horiek betetzen dituzun moduko zerbait, "dena aldi bakoitzean sortzen duzu" modukoa baizik, eta hori (nire ustez) hondamendia da.

Agian goldfish ere aztertu nahiko duzu vault-aren gaineko UI gisa. Zure taldea honekin sartzea nahiko ona egiten du. Demo bat ere badute. 1. Konfiguratu consul. 2. Konfiguratu vault consul-i seinalatuz. 3. Konfiguratu goldfish vault-i seinalatuz. 3. Konfiguratu cron job bat consul snapshot exekutatzeko babeskopietarako.



### LastPass

LastPass Teams. Erabiltzen dugu, txantiloi pertsonalizatuak ditu, ACL-ak, nire ustez ez dago ezer falta.

LastPass ezarri nuen nire erakundean eta C+/B- nota ematen diot. Azkenaldiko arazo handiena fidagarritasun eza da. Azken 90 egunetan hainbat ordutan vault-ak ez-konektatu moduan behartu dira. Hau ez da ideala nire erakunderako literalki 4.000+ pasahitz gordeta dauzkagulako 20+ karpeta partekatutan. Imajinatu dezakezun bezala hainbeste pasahitzekin gutxienez batzuk eguneratzen edo gehitzen dira egunero. Hondamendi-berreskuratze plan bat dugu arazoak ordu bat edo bi baino gehiago irauten badu: script batek gauero vault-aren CSV iraulketa bat sinatu eta enkriptatzen du, keepass-en inporta daitekeena.

LastPass-ek zerbitzu degradatuaren gorabehera jakinarazi gabeak izan ditu: saio-hasiera 'funtzionatzen' du baina ez ditu guneak ekartzen, ausazko ezaugarriak hautsita daude administrazio-panelean, eta ez ditu gakoak behar bezala partekatzen goi-mailako karpeta partekatu berrietarako. 'Key push'/babeskopia erabiltzaile espezifiko bat dut talde guztietan dagoena. Normalean erabiltzaile horrekin saioa hasteak gako-partekatze arazoak konponduko ditu baina ez zerbitzua degradatuta dagoenean egoera-orriak esaten duena esaten duela ere...

Integraziorako erraza izan daiteke pribilegio minimoko eredua duten ACL egokiak badituzu, adib. erabiltzaile batek sarrera edo karpeta batean irakurri eta idatzi eta irakurri soilik baditu irakurri soilik baimenak lortzen ditu. Zoritxarrez nire erakundearen ACL-ak ez dira onenak, beraz JSON hornidura API-a eta ~500 lerro python erabili nituen gure ehunka ACL-en izaera mendekoak pribilegio minimoko ereduari ongi mapatzen ez zaiolako. Erabiltzaile bat ACL guztiak lortu eta mendekotasun-ibilbide moduko bat egin nuen.

Zure ACL edo talde-egitura pribilegio minimoko egitura buruan duela eraiki bada jada, Windows-erako AD/LDAP sinkronizazio tresnak ondo funtzionatuko du.

Jarri harremanetan haien salmenta-taldearekin eta Enterprise proba luzeago batekin konektatu zaitzakete. Ziurtatu mugak erabat ulertzen dituzula abiatu aurretik. Hazkunde-mina nahikoa izan genuen baina zerbitzari aldeko etenaldiak edo narriadurak ez badira, izugarri leuna izan da.


### Bitwarden

Bitwarden-ek tresneria polita du inguruan (WebUI, CLI, Mugikorra, Mahaigaina). Norberak ostata dezake eta nahiko erraza da ezartzeko. Dokumentazio nahiko ona eta PrivacyTools-ek gomendatutako tresna.


### EnvKey

https://www.envkey.com/ saas bat da. Oso erraza ezartzeko, integratzeko eta kudeatzeko.

Ezaugarriak:

  * Babestu API gakoak eta kredentzialak.

  * Mantendu konfigurazioa sinkronizatuta leku guztietan.

  * Konfigurazio eta sekretuen kudeaketa adimenduna eta muturretik muturrera enkriptatua. 

  * Saihestu partekatze ez-segurua eta konfigurazio-barreiatzea. 

  * Integratu minututan.

Gaitasunak:

  * Kudeatu zure aplikazio, ingurune eta talde guztien konfigurazioa eta sarbide-mailak leku bakar batean.

  * Konfiguratu edozein garapen- edo zerbitzari-ingurune ingurune-aldagai bakar batekin.

Alde onak:

  * Hasierako orri ona.

  * Balio-proposamen argia.

  * Web aplikazio bisualki bikaina.

  * Adibide-datu bikainak, adib. Algolia, AWS, Datadog, GitHub, Stripe, eta abar.

  * Sortzailearekin 30 minutu hitz egin nuen enpresari, UI-ari eta abarri buruz. Dane informatua dirudi, alde on/txarrei buruz zintzoa, eta bazkide bideragarria.

  * Enpresa funtsean Y Combinator enpresa tipiko bat da, sortzaile 1ekin. 2018-01ean $120K bildu zituen.

  * Fokua enpresa-ezaugarrietara iristean dago, bereziki EnvKey hodei-ostatatzetik on-prem edo BYOC-ra mugitzea.

  * Aurrera egiteko bide potentziala EnvKey-rekin hastea erabilera-erraztasunagatik, eta gero (edo paraleloan) Vault gehitzea. 


### Lyft-en Confidant

https://lyft.github.io/confidant/

Confidant kode irekiko sekretu-kudeaketa zerbitzua da, sekretuetarako biltegiratze eta sarbide erabiltzaile-lagunkoia modu seguruan eskaintzen duena, Lyft-eko garatzaileengandik.

KMS autentikazioa: Confidant-ek autentikazioaren oiloa-eta-arrautza arazoa konpontzen du AWS KMS eta IAM erabiliz IAM rolek Confidant-ek egiaztatu ditzakeen autentikazio-token seguruak sor ditzaten. Confidant-ek zure IAM roletarako KMS emakidak ere kudeatzen ditu, IAM roleei zerbitzutik-zerbitzura autentikaziorako erabil daitezkeen tokenak sortzeko aukera ematen diena, edo zerbitzuen artean mezu enkriptatuak pasatzeko.

Bertsionatutako sekretuen enkriptazioa atseden-egoeran: Confidant-ek sekretuak gehitze-soilik moduan gordetzen ditu DynamoDB-n, sekretu bakoitzaren berrikuspen bakoitzerako KMS datu-gako bakar bat sortuz, Fernet kriptografia simetriko autentikatua erabiliz.

Sekretuak kudeatzeko web interfaze erabiltzaile-lagunkoia: Confidant-ek AngularJS web interfaze bat eskaintzen du azken erabiltzaileek sekretuak, sekretuen zerbitzuekiko mapaketak eta aldaketen historia erraz kudeatzeko.


### Devolutions Password Server

https://server.devolutions.net/

Babestu, kudeatu eta monitorizatu pribilegiatutako kontu eta saioetarako sarbidea.

Pasahitz-biltegi osoa eta oso-segurua, zure kontu pribilegiatuetarako sarbidea kontrolatzeko aukera ematen dizuna, eta, aldi berean, sysadmin-entzako sarearen ikusgarritasun orokorra hobetzen eta azken erabiltzaileentzako esperientzia ezin hobea eskaintzen duena.

Ezaugarriak: erakundearen pasahitz-biltegi zentralizatua, erabiltzaile-espezifikoko biltegi pribatua, pasahitz-kudeatzailea, kredentzialen injekzioa,
Active Directory integrazioa, rol-oinarritutako sarbide-kontrola, bi faktoreko autentikazioa, enpresa-prest, IP murrizketak, kudeaketa-gaitasunak, pasahitz-sorgailu automatikoa, aplikazio mugikorreko sarbidea, pasahitz-historia, sarbide-txostenak, posta elektronikoko alertak.

  * datuen enkriptazioa onartzen du

  * autentikazio-eskema anitz onartzen ditu LDAP, O365 eta tokiko erabiltzaileak barne, iturri anitzetako MFA onarpenarekin

  * biltegi/vault anitz sarbide-kontrol finarekin talde anitzentzat

  * web UI modernoa

  * kredentzial eta konexio pribatuetarako kredentzial eta konexio vault pribatuak

  * iOS/Android-erako aplikazio mugikorrak

  * sarrera bakoitzerako ikuskaritza-erregistroak, nork/zer/noiz zergatik sartzen ari den galdera aukerakoarekin

  * txantiloi pertsonalizagarriak (ehunka konexio mota natiboki onartzen dituzten arren)

  * eginbide ugari gehiago eta Windows/Mac bezero lodi bat (Remote Desktop Manager) sinkroniza dezakezuna aukerak asko zabaltzen dituena...klik bakarreko konexioak

  * prezioa ez da hain txarra - 15 erabiltzaile arte $500 urtean pasahitz-zerbitzariarentzat


### Thycotic-en Secret Server

https://thycotic.com/products/secret-server/

Ekipamendu-barneko (on-premise) bertsioaren ezaugarriak: 

  * Zure muturretik muturrerako segurtasun-sistemen eta azpiegituraren kontrol osoa

  * Hedatu softwarea zure ekipamendu-barneko datu-zentroan edo zure hodei pribatu birtualaren instantzian

  * Bete datu eta sistema guztiak ekipamendu-barnean egotea eskatzen duten betebehar legal eta arauzkoak

Hodei bertsioaren ezaugarriak:

  * Zerbitzu gisa softwarea ereduak izena eman eta berehala hastea ahalbidetzen du

  * Eskalagarritasun elastikoa hazten zaren heinean

  * Azure-k emandako kontrolak eta erredundantzia %99,9ko uptime SLA-rekin

Erabiltzaileen feedbacka:

  * Produktu hori erabiltzen genuen. Hain erraz saihesten zen eta arauak jende argiarentzat soilik funtzionatzen dute. Erabiltzaile alferrek edo ergelek erraz hondatu dezakete talde-eremuan. Prezioak negoziagarriak dira haiekin hitz egitean.

  * SQL express eta Win 7 kutxa batekin exekuta dezakezu. 

  * Merkea.
