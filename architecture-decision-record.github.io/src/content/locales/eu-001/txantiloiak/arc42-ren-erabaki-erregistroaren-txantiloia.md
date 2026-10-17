# arc42-ren erabaki-erregistroaren txantiloia

<https://arc42.org/overview>

## 1. Sarrera eta helburuak

Eskakizunen, bultzatzaileen eta eskakizunen laburpenaren (edo abstraktuaren) deskribapen laburra. Arkitekturarako kalitate-helburu nagusi hiru (gehienez bost), interesdun nagusientzat lehentasun handiena dutenak. Interesdun garrantzitsuen taula, arkitekturari buruzko beren itxaropenekin.

## 1.1 Eskakizunen ikuspegi orokorra

### Edukia

Eskakizun funtzionalen, bultzatzaileen eta eskakizunen laburpenaren (edo
abstraktuaren) deskribapen laburra. (Espero dugu) lehendik dauden eskakizun-dokumentuetarako estekak, non aurkitu daitezkeen jakinarazita. 

### Motibazioa

Azken erabiltzaileen ikuspegitik, sistema bat sortzen edo aldatzen da
negozio-jarduera baten laguntza hobetzeko eta/edo kalitatea hobetzeko. 

### Forma

Testu-deskribapen laburra, ziurrenik erabilera-kasuen taula formatuan. Eskakizun-dokumentuak
badaude, ikuspegi orokor honek dokumentu horiei erreferentzia egin behar die.

Mantendu atal hauek ahalik eta laburren. Orekatu dokumentu honen irakurgarritasuna
eskakizun-dokumentuekiko errepikapen potentzialarekin. 

## 1.2 Kalitate-helburuak

### Edukia

Arkitekturarako hiru (gehienez bost) kalitate-helburu nagusi, beren betetzea
interesdun nagusientzat garrantzi handiena duena. Benetan arkitekturarako kalitate-helburuez ari gara. Ez nahastu proiektuaren helburuekin. Ez dira
nahitaez berdinak. ISO 25010 estandarrak interes potentziala duten gaien ikuspegi orokor ona ematen du.

### Motibazioa

Zure interesdun garrantzitsuenen kalitate-helburuak ezagutu behar dituzu, funtsezko
arkitektura-erabakietan eragingo dutelako. Izan oso zehatza kalitate horiei buruz, saihestu hitz hutsalak. Arkitekto gisa zure lanaren kalitatea
nola epaituko den ez badakizu …

### Forma

Kalitate-helburu garrantzitsuenak eta eszenatoki konkretuak dituen taula, lehentasun-ordenan.

## 1.3 Interesdunak

### Edukia

Sistemaren interesdunen ikuspegi orokor esplizitua, hau da, pertsona, rol edo
erakunde guztiak, zeinek

- arkitektura ezagutu behar duten

- arkitekturaz konbentzitu behar diren

- arkitekturarekin edo kodearekin lan egin behar duten

- beren lanerako arkitekturaren dokumentazioa behar duten

- sistemari edo bere garapenari buruzko erabakiak hartu behar dituzten

### Motibazioa

Sistemaren garapenean parte hartzen duten edo sistemak eragiten dien alde guztiak ezagutu behar dituzu. Bestela, sorpresa desatseginak izan ditzakezu geroago garapen-prozesuan. Interesdun hauek zure
lanaren eta bere emaitzen irismena eta xehetasun-maila zehazten dute.

### Forma

Rol-izenak, pertsona-izenak eta arkitekturari eta bere dokumentazioari buruzko beren itxaropenak dituen taula.

## 2. Murriztapenak

Taldeak diseinu- eta ezarpen-erabakietan edo lotutako prozesuei buruzko erabakietan mugatzen duen edozer. Batzuetan sistema indibidualetatik harago joan daiteke eta
erakunde eta enpresa osoentzat baliozkoa da.

### Edukia

Software-arkitektoak diseinu- eta ezarpen-erabakietan edo garapen-prozesuari buruzko erabakietan duten askatasuna mugatzen duen edozein eskakizun. Murriztapen hauek
batzuetan sistema indibidualetatik harago doaz eta erakunde eta enpresa
osoentzat baliozkoak dira.

### Motibazioa

Arkitektoek zehazki jakin behar dute diseinu-erabakietan non diren askeak eta
non bete behar dituzten murriztapenak. Murriztapenei beti aurre egin behar zaie;
negoziagarriak izan daitezke, ordea.

### Forma

Murriztapenen taula sinpleak azalpenekin. Behar izanez gero, banatu ditzakezu
murriztapen teknikoetan, murriztapen antolakuntzako eta politikoetan, eta konbentzioetan (adib. programazio- edo bertsio-jarraibideak, dokumentazio- edo izendapen-konbentzioak)

## 3. Testuingurua eta irismena

Zure sistema bere (kanpoko) komunikazio-kideetatik (inguruko sistemak
eta erabiltzaileak) mugatzen du. Kanpoko interfazeak zehazten ditu. Negozio/domeinu ikuspegitik (beti) edo ikuspegi teknikotik (aukerakoa) erakutsia

### Edukia

Sistemaren irismena eta testuingurua —izenak dioen bezala— zure sistema (hau da,
zure irismena) bere komunikazio-kide guztietatik (inguruko sistemak eta erabiltzaileak,
hau da, zure sistemaren testuingurua) mugatzen du. Horrela kanpoko interfazeak zehazten ditu.

Beharrezkoa bada, bereizi negozio-testuingurua (domeinu-espezifikoko sarrerak eta
irteerak) testuinguru teknikotik (kanalak, protokoloak, hardwarea).

### Motibazioa

Komunikazio-kideekiko domeinu-interfazeak eta interfaze teknikoak
zure sistemaren alderdirik kritikoenen artean daude. Ziurtatu erabat
ulertzen dituzula.

### Forma

- Testuinguru-diagrama desberdinak

- Komunikazio-kideen eta haien interfazeen zerrendak.

## 3.1 Negozio-testuingurua

### Edukia

Komunikazio-kide guztien (erabiltzaileak, IT sistemak, …) zehaztapena,
domeinu-espezifikoko sarreren eta irteeren edo interfazeen azalpenekin. Aukeran
domeinu-espezifikoko formatuak edo komunikazio-protokoloak gehi ditzakezu.

### Motibazioa

Interesdun guztiek ulertu behar dute zer datu trukatzen diren sistemaren
inguruneare­kin.

### Forma

Sistema kutxa beltz gisa erakusten duten eta komunikazio-kideekiko domeinu-interfazeak
zehazten dituzten diagrama mota guztiak.

Edo (edo gainera) taula bat erabil dezakezu. Taularen izenburua zure sistemaren izena da, hiru zutabek komunikazio-kidearen izena,
sarrerak eta irteerak dituzte.

## 3.2 Testuinguru teknikoa

### Edukia

Zure sistema bere ingurunearekin lotzen duten interfaze teknikoak (kanalak eta transmisio-bideak). Gainera, domeinu-espezifikoko sarrera/irteeren kanalekiko mapaketa,
hau da, I/O zeinek zein kanal erabiltzen duen azalpena.

### Motibazioa

Interesdun askok arkitektura-erabakiak hartzen dituzte sistemaren eta bere testuinguruaren arteko interfaze teknikoetan oinarrituta.
Bereziki azpiegitura- edo hardware-diseinatzaileek erabakitzen dituzte interfaze tekniko hauek.

### Forma

Adib. inguruko sistemetarako kanalak deskribatzen dituen UML hedapen-diagrama, kanalen eta
sarrera/irteeren arteko erlazioak erakusten dituen mapaketa-taula batekin batera.

## 4. Soluzio-estrategia

Arkitekturari forma ematen dioten funtsezko erabakien eta soluzio-estrategien laburpena. Teknologia, goi-mailako deskonposizioa, kalitate-helburu nagusiak
lortzeko ikuspegiak eta antolakuntzako erabaki garrantzitsuak sar ditzake.

### Edukia

Sistemaren arkitekturari forma ematen dioten funtsezko erabakien eta soluzio-estrategien laburpen eta azalpen laburra. Hauek sartzen dira

- teknologia-erabakiak

- sistemaren goi-mailako deskonposizioari buruzko erabakiak, adib. arkitektura-eredu edo diseinu-eredu baten erabilera

- funtsezko kalitate-helburuak nola lortu erabakiak

- antolakuntzako erabaki garrantzitsuak, adib. garapen-prozesu bat aukeratzea edo zeregin batzuk hirugarrenei eskuordetzea.

### Motibazioa

Erabaki hauek zure arkitekturaren oinarrizko harriak dira. Beste erabaki
xehatu edo ezarpen-arau askoren oinarria dira.

### Forma

Mantendu funtsezko erabaki hauen azalpena laburra.

Arrazoitu zer erabaki duzun eta zergatik erabaki duzun horrela, zure
arazo-adierazpenean, kalitate-helburuetan eta funtsezko murriztapenetan oinarrituta. Erreferentzia egin hurrengo ataletako xehetasunei
(5. atala egitura-xehetasunetarako, 8. atala
zeharkako kontzeptuetarako).

Soluzio-ikuspegien zerrenda edo taula erabil dezakezu.

## 5. Eraikuntza-blokeen ikuspegia

Sistemaren deskonposizio estatikoa, iturburu-kodearen abstrakzioak, kutxa zurien
(kutxa beltzak dituztenak) hierarkia gisa erakutsita, xehetasun-maila egokira arte.

### Edukia

Eraikuntza-blokeen ikuspegiak sistemaren deskonposizio estatikoa erakusten du
eraikuntza-blokeetan (moduluak, osagaiak, azpisistemak, klaseak, interfazeak, paketeak,
liburutegiak, esparruak, geruzak, partizioak, mailak, funtzioak, makroak, eragiketak,
datu-egiturak, …) eta haien mendekotasunak (erlazioak, asoziazioak,
…)

Ikuspegi hau derrigorrezkoa da arkitektura-dokumentazio guztietan. Etxe baten
antzera, oin-planoa da.

### Motibazioa

Mantendu zure iturburu-kodearen ikuspegi orokorra bere egitura abstrakzioaren bidez
ulergarri eginez.

Horrek zure interesdunekin maila abstraktuan komunikatzeko aukera ematen du,
ezarpen-xehetasunak ikertu gabe.

### Forma

Eraikuntza-blokeen ikuspegia kutxa beltzen eta kutxa zurien bilduma hierarkikoa da
(ikus beheko irudia) eta haien deskribapenak.

## 5.1 Sistema osoaren kutxa zuria

Hemen sistema osoaren deskonposizioa deskribatzen duzu beheko kutxa zuriaren txantiloia erabiliz. Honako hauek ditu

- ikuspegi orokorreko diagrama bat

- deskonposizioaren motibazioa

- sartutako eraikuntza-blokeen kutxa beltzaren deskribapenak. Horretarako alternatibak eskaintzen ditugu:

  - erabili taula bat sartutako eraikuntza-bloke guztien eta haien interfazeen ikuspegi labur eta pragmatiko baterako

  - erabili eraikuntza-blokeen kutxa beltzaren deskribapenen zerrenda kutxa beltzaren txantiloiaren arabera (ikus behean). Zure tresna-aukeraren arabera zerrenda hau azpikapituluak (testu-fitxategietan), azpiorriak (Wiki batean) edo elementu habiaratuak (modelatze-tresna batean) izan daitezke.

  - (aukerakoa:) eraikuntza-bloke baten kutxa beltzaren txantiloietan azaltzen ez diren, baina kutxa zuria ulertzeko oso garrantzitsuak diren interfaze garrantzitsuak.

Interfazeak zehazteko modu asko daudenez, ez dugu horientzako txantiloi espezifikorik ematen.

Kasurik onenean adibideekin edo sinadura sinpleekin moldatuko zara.

## 5.2 2. maila

Hemen 1. mailako (batzuen) eraikuntza-blokeen barne-egitura kutxa zuri gisa zehaztu dezakezu.

Erabaki behar duzu zure sistemako zein eraikuntza-bloke diren nahikoa garrantzitsuak
horrelako deskribapen xehatua justifikatzeko. Mesedez, lehenetsi garrantzia osotasunaren aurrean.
Zehaztu eraikuntza-bloke garrantzitsuak, harrigarriak, arriskutsuak, konplexuak edo aldakorrak. Utzi kanpoan
zure sistemaren zati normalak, sinpleak, aspergarriak edo estandarizatuak

### 5.2.1 1. eraikuntza-blokearen kutxa zuria

1. eraikuntza-blokearen barne-egitura zehazten du.

Erabili kutxa zuriaren txantiloia (ikus goian).

## 6. Exekuzio-ikuspegia

Eraikuntza-blokeen portaera eszenatoki gisa, erabilera-kasu edo
ezaugarri garrantzitsuak, kanpoko interfaze kritikoetako interakzioak, operazioa eta
administrazioa eta errore- eta salbuespen-portaera estaliz.

### Edukia

Exekuzio-ikuspegiak sistemaren eraikuntza-blokeen portaera eta interakzio konkretuak deskribatzen ditu hurrengo arloetako eszenatoki gisa:

- erabilera-kasu edo ezaugarri garrantzitsuak: nola exekutatzen dituzte eraikuntza-blokeek?

- kanpoko interfaze kritikoetako interakzioak: nola kooperatzen dute eraikuntza-blokeek erabiltzaileekin eta inguruko sistemekin?

- operazioa eta administrazioa: abiarazpena, hasiera, geldiketa

- errore- eta salbuespen-eszenatokiak

Oharra: Eszenatoki posibleak (sekuentziak, lan-fluxuak) aukeratzeko irizpide nagusia haien arkitektura-garrantzia da. Ez da garrantzitsua eszenatoki asko deskribatzea. Hobe da hautaketa adierazgarri bat dokumentatzea.

### Motibazioa

Ulertu behar duzu zure sistemako eraikuntza-blokeek (instantziek) nola egiten duten beren lana eta nola komunikatzen diren exekuzio-garaian. Batez ere eszenatokiak jasoko dituzu zure dokumentazioan zure arkitektura eredu estatikoak (eraikuntza-blokeen ikuspegia, hedapen-ikuspegia) irakurri eta ulertzeko hain prest edo gai ez diren interesdunei komunikatzeko.

### Forma

Eszenatokiak deskribatzeko notazio asko daude, adib.


- urratsen zerrenda zenbakitua (hizkuntza naturalean)

- jarduera-diagramak edo fluxu-diagramak

- sekuentzia-diagramak

- BPMN edo EPC-ak (gertaera-prozesu kateak)

- egoera-makinak

- eta abar.

## 6.n Exekuzio-eszenatokia n (1, 2, 3, eta abar)

Txertatu eszenatokiaren exekuzio-diagrama edo testu-deskribapena.

Txertatu diagrama honetan irudikatutako eraikuntza-bloke instantzien arteko interakzioen alderdi nabarmenen deskribapena.

## 7. Hedapen-ikuspegia

Ingurune, ordenagailu, prozesadore eta topologiak dituen azpiegitura teknikoa.
(Software) eraikuntza-blokeen azpiegitura-elementuekiko mapaketa.

### Edukia

Hedapen-ikuspegiak deskribatzen du:

- zure sistema exekutatzeko erabilitako azpiegitura teknikoa, azpiegitura-elementuekin
  hala nola kokapen geografikoak, inguruneak, ordenagailuak, prozesadoreak,
  kanalak eta sare-topologiak, baita beste azpiegitura-elementu batzuk ere eta

- (software) eraikuntza-blokeen azpiegitura-elementu horiekiko mapaketa.

Sarritan sistemak ingurune desberdinetan exekutatzen dira, adib. garapen-ingurunea,
proba-ingurunea, produkzio-ingurunea. Kasu horietan ingurune garrantzitsu guztiak
dokumentatu behar dituzu.

Dokumentatu bereziki hedapen-ikuspegia zure softwarea sistema banatu gisa exekutatzen denean, ordenagailu, prozesadore, zerbitzari edo ontzi bat baino gehiagorekin
edo zure hardware-prozesadore eta txipak diseinatzen eta eraikitzen dituzunean.

Software-ikuspegitik, nahikoa da zure eraikuntza-blokeen hedapena erakusteko behar diren azpiegitura-elementuak jasotzea.
Hardware-arkitektoek harago joan daitezke eta azpiegitura nahi duten xehetasun-mailara arte deskriba dezakete. 

### Motibazioa

Softwarea ez da hardwarerik gabe exekutatzen. Azpiko azpiegitura honek zure sisteman eta/edo zeharkako kontzeptu batzuetan eragin dezake eta eragingo du. Beraz,
azpiegitura ezagutu behar duzu.

### Forma

Agian goi-mailako hedapen-diagrama 3.2. atalean dago jada testuinguru tekniko gisa, zure azpiegitura KUTXA BELTZ BAT gisa duela. Atal honetan kutxa beltz hori handituko duzu hedapen-diagrama gehigarriak erabiliz.

- UMLk hedapen-diagramak eskaintzen ditu ikuspegi hori adierazteko. Erabili, agian diagrama habiaratuekin, zure azpiegitura konplexuagoa denean.

- Zure (hardware) interesdunek UML hedapen-diagrama baino diagrama mota
  desberdinak nahiago dituztenean, utzi azpiegituraren nodoak eta
  kanalak erakusteko gai den edozein mota erabiltzen.

## 7.1 1. mailako azpiegitura

Deskribatu (normalean diagramen, taulen eta testuaren konbinazioan):

- zure sistemaren banaketa hainbat kokapen, ingurune, ordenagailu, prozesadoretan, .. baita haien arteko lotura fisikoak ere

- hedapen-egitura honen justifikazio edo motibazio garrantzitsua

- azpiegituraren kalitate- eta/edo errendimendu-ezaugarriak

- software-artefaktuen (eraikuntza-blokeen) azpiegitura-elementuekiko mapaketa

Ingurune anitz edo hedapen alternatiboetarako, mesedez kopiatu arc42-ren atal hori ingurune garrantzitsu guztientzat. **

## 7.2 2. mailako azpiegitura

Hemen 1. mailako azpiegituraren (batzuen) azpiegitura-elementuen barne-egitura sar dezakezu.

Mesedez, kopiatu 1. mailako egitura hautatutako elementu bakoitzerako.

## 8. Zeharkako kontzeptuak

Orokorrean, sistemaren hainbat zatitan (→ zeharkako) garrantzitsuak diren arau nagusiak eta soluzio-ikuspegiak. Kontzeptuak askotan hainbat
eraikuntza-blokerekin lotuta daude. Sartu gai desberdinak, hala nola domeinu-ereduak, arkitektura-
ereduak eta -estiloak, teknologia espezifikoak erabiltzeko arauak eta ezarpen-
arauak.

### Edukia

Atal honek zeharkako kontzeptuak (praktikak, ereduak, arauak
edo soluzio-ideiak) deskribatzen ditu. Halako kontzeptuak sarritan hainbat eraikuntza-blokerekin lotuta daude.
Gai desberdin asko sar ditzakete.

### Motibazioa

Kontzeptuek arkitekturaren osotasun kontzeptualaren (koherentzia, homogeneotasuna) oinarria osatzen dute.
Beraz, ekarpen garrantzitsua dira zure sistemaren barne-kalitateak lortzeko.

Hau da txantiloian halako kontzeptuen zehaztapen kohesionatu baterako eman dugun lekua.

Kontzeptu hauetako asko zure eraikuntza-bloke batzuekin lotuta daude edo eragiten diete.

### Forma

Forma aldakorra izan daiteke:

- edozein egiturako kontzeptu-paperak

- adibide-ezarpenak, bereziki kontzeptu teknikoetarako

- zeharkako eredu-zatiak edo eszenatokiak arkitektura-ikuspegien notazioak erabiliz

### Atal honen egitura

Aukeratu zure sistemarako gehien behar diren gaiak soilik eta eman 2. mailako goiburu bat atal honetan (adib. 8.1, 8.2 eta abar).

- EZ SAIATU goiko diagramako gai guztiak estaltzen.

### Atzeko planoa

Sistemetako gai batzuek askotan hainbat eraikuntza-bloke, hardware-elementu
edo garapen-prozesu ukitzen dituzte. Errazagoa izan daiteke halako zeharkako gaiak
leku zentral batean komunikatzea edo dokumentatzea, kezkatutako eraikuntza-bloke, hardware-elementu edo
garapen-prozesuen deskribapenean errepikatu beharrean.

Kontzeptu batzuek sistemaren elementu guztiak ukitu ditzakete, beste batzuek
gutxi batzuentzat soilik dute garrantzia.

## 9. Arkitektura-erabakiak

Arkitektura-erabaki garrantzitsuak, garestiak, kritikoak, eskala handikoak edo arriskutsuak
arrazoiak barne.

### Edukia

Arkitektura-erabaki garrantzitsuak, garestiak, eskala handikoak edo arriskutsuak
arrazoiak barne. "Erabakiak" esatean, emandako irizpideetan oinarrituta alternatiba bat
aukeratzea esan nahi dugu.

Mesedez, erabili zure iritzia erabakitzeko arkitektura-erabaki bat atal zentral honetan
dokumentatu behar den ala hobe den lokalki dokumentatzea
(adib. eraikuntza-bloke baten kutxa zuriaren txantiloian). Saihestu testu
errepikatua. Erreferentzia egin 4. atalari, non zure arkitekturaren erabaki
garrantzitsuenak jaso dituzun jada.

### Motibazioa

Zure sistemaren interesdunek zure erabakiak ulertu eta berriz bide-gurutzatzeko gai izan behar dute.

### Forma

- ADR (arkitektura-erabakien erregistroa) erabaki garrantzitsu bakoitzerako

- garrantziaren eta ondorioen arabera ordenatutako zerrenda edo taula edo

- erabaki bakoitzeko atal bereizien forman xehetasun handiagoz

### Atzeko planoa (ADR-ei buruz)

Dokumentazio zati txikiagoak errazagoak dira irakurtzeko, sortzeko eta mantentzeko. Arkitektura-erabakien kasuan, garapen-taldeek askotan:

- erabakiaz jakitea, ikusgai dagoelako adib. iturburu-kodean, baina

- erabaki horren atzean dagoen motibazioa galtzea (ikus Nygard 2011)

Beraz, erabaki garrantzitsu batzuk dokumentatu behar dituzu beren motibazioarekin, arrazoibidearekin

### Erabakiei buruzko gure proposamena

Mantendu arkitekturaren ikuspegitik esanguratsuak diren erabakien bilduma bat, hau da, egituran, kalitate-ezaugarrietan, mendekotasun (bereziki kanpoko) eta interfaze garrantzitsuetan,
edo eraikuntza-teknikan eragiten duten erabakiak (eskerrik asko Michael
Nygard-i proposamen honengatik).

## 10. Kalitate-eskakizunak

Kalitate-eskakizunak eszenatoki gisa, goi-mailako ikuspegi orokorra emateko kalitate-zuhaitzarekin. Kalitate-helburu garrantzitsuenak 1.2. atalean
(kalitate-helburuak) deskribatuta egon beharko lirateke.

### Edukia

Atal honek kalitate-eskakizun garrantzitsu guztiak ditu.

Eskakizun hauetako garrantzitsuenak 1.2. atalean
(kalitate-helburuak) deskribatu dira jada, beraz hemen erreferentzia soilik egin behar zaie. 10. atal honetan
garrantzi txikiagoko kalitate-eskakizunak ere jaso behar dituzu,
erabat lortzen ez direnean arrisku handirik sortuko ez dutenak (baina baliteke atsegin izatea).

### Motibazioa

Kalitate-eskakizunek eragin handia izango dutenez arkitektura-erabakietan, jakin behar duzu zein kalitate diren benetan garrantzitsuak
zure interesdunentzat, modu zehatz eta neurgarrian.

### Informazio gehiago

Ikus Q42 kalitate-eredu zabala https://quality.arc42.org helbidean.

## 10.1 Kalitate-eskakizunen ikuspegi orokorra

### Edukia

Kalitate-eskakizunen ikuspegi orokorra edo laburpena.

### Motibazioa

Askotan hamarnaka (edo ehunka ere) kalitate-eskakizun xehatu aurkitzen ditugu.
Ikuspegi orokor atal honetan laburtzen saiatu beharko zenuke, adib. kategoriak
edo gaiak deskribatuz (ISO 25010:2023-k edo Q42-k iradokitzen duten bezala

Laburpen-deskribapen hauek zehatzak, nahikoa espezifikoak eta
neurgarriak badira, 10.2 atala saltatu dezakezu.

### Forma

Erabili taula sinple bat, non lerro bakoitzak kategoria edo gai bat eta kalitate-eskakizunaren deskribapen
laburra duen. Edo, mapa mentala erabil dezakezu kalitate-eskakizun hauek
egituratzeko.

Literaturan, kalitate-atributuen zuhaitzaren ideia ere deskribatu da,
"kalitate" termino orokorra erro gisa jartzen duena eta "kalitate" terminoaren
zuhaitz-itxurako fintzea erabiltzen duena. [Bass+21]-k "Quality
Attribute Utility Tree" terminoa sartu zuen helburu horretarako.

## 10.2 Kalitate-eszenatokiak

### Edukia

Kalitate-eszenatokiek kalitate-eskakizunak konkretu egiten dituzte eta betetzen diren erabakitzeko aukera ematen dute
(onarpen-irizpideen zentzuan). Ziurtatu zure
eszenatokiak espezifikoak eta neurgarriak direla.

Bi eszenatoki mota bereziki erabilgarriak dira:

- Erabilera-eszenatokiek (aplikazio-eszenatoki edo erabilera-kasu eszenatoki ere deituak)
  sistemaren exekuzio-erreakzioa deskribatzen dute estimulu jakin baten aurrean. Honek
  sistemaren eraginkortasuna edo errendimendua deskribatzen duten eszenatokiak ere barne hartzen ditu.
  Adibidea: Sistemak erabiltzailearen eskaerari segundo batean erantzuten dio.

- Aldaketa-eszenatokiek sistemaren edo bere berehalako inguruneko aldaketa edo zabalkundearen
  nahi den eragina deskribatzen dute. Adibidea: Funtzionalitate gehigarria
  ezartzen da edo kalitate-atributu baten eskakizunak aldatzen dira, eta
  aldaketaren ahalegina edo iraupena neurtzen da.

### Forma

Eszenatoki xehatuetarako informazio tipikoak honakoak dira:

Forma laburrean (Q42 ereduan nahiago dena):

- Testuingurua/Atzeko planoa: Zein sistema edo osagai mota, zein da ingurunea edo egoera?

- Iturria/Estimulua: Nork edo zerk hasten edo abiarazten duen portaera, erreakzioa edo ekintza.

- Metrika/Onarpen-irizpideak: Neurri edo metrika bat barne hartzen duen erantzuna

Eszenatokien forma luzea (SEI-k eta [Bass+21]-k nahiago dutena) xehatuagoa da eta informazio hau barne hartzen du:

- Eszenatoki IDa: Eszenatokiaren identifikatzaile bakarra.

- Eszenatokiaren izena: Eszenatokiaren izen labur eta deskribatzailea.

- Iturria: Eszenatokia hasten duen entitatea (erabiltzailea, sistema edo gertaera).

- Estimulua: Sistemak jorratu behar duen abiarazpen-gertaera edo -baldintza.

- Ingurunea: Sistemak estimulua jasaten duen eragiketa-testuingurua edo -baldintza.

- Artefaktua: Estimuluak eragindako eraikuntza-blokeak edo sistemaren beste elementuak.

- Erantzuna: Sistemak estimuluaren aurrean erakusten duen emaitza edo portaera.

- Erantzunaren neurria: Sistemaren erantzuna ebaluatzeko irizpidea edo metrika.

### Ikus gainera

2023ko urtarriletik, arc42-k kalitate-eredu pragmatiko bat eskaintzen du, kalitate-eskakizunak
hashtag edo etiketekin etiketatzea proposatzen duena, hala nola #flexible, #efficient,
#usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Arriskuak eta zor teknikoa

Arrisku tekniko edo zor tekniko ezagunak. Zer arazo potentzial daude sistemaren barruan edo
inguruan? Zerk sentiarazten du garapen-taldea gaizki?

### Edukia

Identifikatutako arrisku tekniko edo zor teknikoen zerrenda, lehentasunaren arabera ordenatua

### Motibazioa

"Arriskuen kudeaketa helduentzako proiektuen kudeaketa da" (Tim Lister, Atlantic
Systems Guild.)

Hau izan beharko litzateke zure leloa arkitekturan arriskuen eta zor teknikoen detektatze eta ebaluazio sistematikorako, kudeaketako interesdunek (adib. proiektu-kudeatzaileak, produktu-jabeak) arrisku-analisi eta neurketa-plangintza orokorraren zati gisa beharko dutena.

### Forma

Arriskuen eta/edo zor teknikoen zerrenda, agian arriskuak minimizatzeko, arintzeko edo saihesteko edo zor teknikoa murrizteko neurri iradokiak barne.
