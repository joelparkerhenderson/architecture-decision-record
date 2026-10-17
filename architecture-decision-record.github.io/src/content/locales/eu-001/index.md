# Arkitektura-erabakien erregistroa (ADR)

Arkitektura-erabakien erregistroa (ADR) hartutako arkitektura-erabaki garrantzitsu bat bere testuinguru eta ondorioekin batera jasotzen duen dokumentua da.

> [!IMPORTANT]
> Egin zeure ikerketa zorrotza baliabide hauekin, sistema kritikoetan erabili aurretik.

Edukia:

- [Zer da arkitektura-erabakien erregistroa?](#zer-da-arkitektura-erabakien-erregistroa)
- [ADR-ak erabiltzen hasteko modua](#adr-ak-erabiltzen-hasteko-modua)
- [ADR-ak tresnekin erabiltzen hasteko modua](#adr-ak-tresnekin-erabiltzen-hasteko-modua)
- [ADR-ak gitekin erabiltzen hasteko modua](#adr-ak-gitekin-erabiltzen-hasteko-modua)
- [ADR-etarako Claude Code skill-ak](#adr-etarako-claude-code-skill-ak)
- [ADR-etarako fitxategi-izenen konbentzioak](#adr-etarako-fitxategi-izenen-konbentzioak)
- [ADR onak idazteko iradokizunak](#adr-onak-idazteko-iradokizunak)
- [ADR adibide-txantiloiak](#adr-adibide-txantiloiak)
- [ADR-etarako talde-lanerako aholkuak](#adr-etarako-talde-lanerako-aholkuak)
- [ADR-etarako talde-lanerako galderak](#adr-etarako-talde-lanerako-galderak)
- [ADR-etarako hurrengo urratsaren kontzeptuak](#adr-etarako-hurrengo-urratsaren-kontzeptuak)
- [Arkitektura-diagramak, ikuspegiak eta ikuspuntuak](#arkitektura-diagramak-ikuspegiak-eta-ikuspuntuak)
- [Erabakietarako fitness funtzioak kode gisa](#erabakietarako-fitness-funtzioak-kode-gisa)
- [Pull request-etarako erabaki-babesak](#pull-request-etarako-erabaki-babesak)
- [Informazio gehiagorako](#informazio-gehiagorako)

Txantiloiak:

- [Jeff Tyree eta Art Akermanen erabaki-erregistroaren txantiloia](txantiloiak/jeff-tyree-eta-art-akermanen-erabaki-erregistroaren-txantiloia/)
- [Michael Nygarden erabaki-erregistroaren txantiloia](txantiloiak/michael-nygarden-erabaki-erregistroaren-txantiloia/)
- [EdgeX-en erabaki-erregistroaren txantiloia](txantiloiak/edgex-en-erabaki-erregistroaren-txantiloia/)
- [arc42-ren erabaki-erregistroaren txantiloia](txantiloiak/arc42-ren-erabaki-erregistroaren-txantiloia/)
- [Eredu alexandriarrerako erabaki-erregistroaren txantiloia](txantiloiak/eredu-alexandriarrerako-erabaki-erregistroaren-txantiloia/)
- [Negozio-kasurako erabaki-erregistroaren txantiloia](txantiloiak/negozio-kasurako-erabaki-erregistroaren-txantiloia/)
- [MADR proiektuaren erabaki-erregistroaren txantiloia](txantiloiak/madr-proiektuaren-erabaki-erregistroaren-txantiloia/)
- [Planguage erabiltzen duen erabaki-erregistroaren txantiloia](txantiloiak/planguage-erabiltzen-duen-erabaki-erregistroaren-txantiloia/)
- [Paulo Mersonen erabaki-erregistroaren txantiloia](https://github.com/pmerson/ADR-template)
- [Olaf Zimmermannen erabaki-erregistroaren txantiloia](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Gareth Morganen erabaki-erregistroaren txantiloia](txantiloiak/gareth-morganen-erabaki-erregistroaren-txantiloia/)
- [GIG Cymru NHS Walesen erabaki-erregistroaren txantiloia](txantiloiak/gig-cymru-nhs-wales-en-erabaki-erregistroaren-txantiloia/)
- [Erabaki tekniko garrantzitsuetarako (ITD) erabaki-erregistroaren txantiloia, Ignacio Larrañagarena](txantiloiak/erabaki-tekniko-garrantzitsuetarako-erabaki-erregistroaren-txantiloia/)

Adibideak:

- [CSS markoa](adibideak/css-markoa/)
- [Ingurune-aldagaien konfigurazioa](adibideak/ingurune-aldagaien-konfigurazioa/)
- [Metrikak, monitoreak, alertak](adibideak/metrikak-monitoreak-alertak/)
- [Microsoft Azure DevOps](adibideak/microsoft-azure-devops/)
- [Monorepo edo multirepo](adibideak/monorepo-edo-multirepo/)
- [Programazio-lengoaiak](adibideak/programazio-lengoaiak/)
- [Sekretuen biltegiratzea](adibideak/sekretuen-biltegiratzea/)
- [Denbora-zigilu formatua](adibideak/denbora-zigilu-formatua/)
- [Eta askoz gehiago...](adibideak/)

## Zer da arkitektura-erabakien erregistroa?

**Arkitektura-erabakien erregistroa** (ADR) hartutako arkitektura-erabaki garrantzitsu bat bere testuinguru eta ondorioekin batera jasotzen duen dokumentua da.

**Arkitektura-erabakia** (AD) eskakizun esanguratsu bati erantzuten dion softwarearen diseinu-aukera bat da.

**Arkitektura-erabakien egunkaria** (ADL) proiektu jakin baterako (edo erakunde baterako) sortu eta mantentzen diren ADR guztien bilduma da.

**Arkitekturaren ikuspegitik esanguratsua den eskakizuna** (ASR) software-sistema baten arkitekturan eragin neurgarria duen eskakizuna da.

Hori guztia **arkitektura-ezagutzaren kudeaketa** (AKM) gaiaren barruan sartzen da.

Dokumentu honen helburua ADR-en ikuspegi azkar bat ematea da: nola sortzen diren eta non bilatu informazio gehiago.

Laburdurak:

  * **AD**: arkitektura-erabakia

  * **ADL**: arkitektura-erabakien egunkaria

  * **ADR**: arkitektura-erabakien erregistroa

  * **AKM**: arkitektura-ezagutzaren kudeaketa

  * **ASR**: arkitekturaren ikuspegitik esanguratsua den eskakizuna

## ADR-ak erabiltzen hasteko modua

ADR-ak erabiltzen hasteko, hitz egin zure taldekideekin arlo hauei buruz.

Erabakien identifikazioa:

  * Zein premiazkoa eta zein garrantzitsua da AD?

  * Orain hartu behar al da, ala itxaron daiteke gehiago jakin arte?

  * Bai esperientzia pertsonalak eta kolektiboak, bai diseinu-metodo eta praktika aitortuek erabakiak identifikatzen lagun dezakete.

  * Egokiena erabaki-zeregin zerrenda bat mantentzea da, produktuaren zeregin zerrendaren osagarri gisa.

Erabakiak hartzea:

  * Erabakiak hartzeko hainbat teknika daude, orokorrak zein software-arkitekturari espezifikoak, esaterako elkarrizketa-mapak egitea.

  * Taldeko erabakiak hartzea ikerketa-gai aktiboa da.

Erabakiak ezartzea eta betearaztea:

  * AD-ak software-diseinuan erabiltzen dira; beraz, sistemaren interesdunei jakinarazi eta haiek onartu behar dituzte, sistema finantzatzen, garatzen eta erabiltzen dutenek.

  * Arkitekturaren aldetik agerikoak diren kodeketa-estiloak eta arkitektura-kezka eta -erabakietan zentratzen diren kode-berrikuspenak lotutako bi praktika dira.

  * AD-ak (berriz) aztertu behar dira software-sistema bat modernizatzean, software-bilakaeran.

Erabakiak partekatzea (aukerakoa):

  * AD asko errepikatzen dira proiektuetan.

  * Beraz, iraganeko erabakiei buruzko esperientziak, onak zein txarrak, aktibo berrerabilgarri baliotsuak izan daitezke, ezagutza-kudeaketako estrategia esplizitu bat erabiltzen denean.

Erabakien dokumentazioa:

  * Erabakiak jasotzeko txantiloi eta tresna asko daude.

  * Ikus komunitate arinak, adibidez M. Nygarden ADR-ak.

  * Ikus software-ingeniaritza eta arkitektura-diseinuko prozesu tradizionalak, adibidez IBM UMF-k eta CapitalOne-ko Tyree eta Akermanek iradokitako taula-diseinuak.

Informazio gehiagorako:

  * Goiko urratsak Wikipediako [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision) sarreratik hartu dira

## ADR-ak tresnekin erabiltzen hasteko modua

- [MySpec](https://myspec.dev) — Proiektuaren konstituzioa, arkitektura teknikoa eta ADR-ak Markdown garbian egituratzen dituen eta MCP bidez eskaintzen duen espezifikazio- eta arkitektura-erabaki automatizatuen plataforma.

ADR-ak tresnekin nahi duzun moduan has zaitezke erabiltzen.

Adibidez:

  * Google Drive eta lineako edizioa erabiltzea gustatzen bazaizu, Google Doc bat edo Google Sheet bat sor dezakezu.

  * Iturburu-kodearen bertsio-kontrola, adibidez git, erabiltzea gustatzen bazaizu, fitxategi bat sor dezakezu ADR bakoitzeko.

  * Proiektuak planifikatzeko tresnak, adibidez Atlassian Jira, erabiltzea gustatzen bazaizu, tresnaren plangintza-jarraipena erabil dezakezu.

  * Wikiak, adibidez MediaWiki, erabiltzea gustatzen bazaizu, ADR wiki bat sor dezakezu.

## ADR-ak gitekin erabiltzen hasteko modua

git bertsio-kontrola erabiltzea gustatzen bazaizu, hona hemen iturburu-kodea duen software-proiektu tipiko baterako ADR-ak gitekin erabiltzen hasteko dugun modua.

Sortu direktorio bat ADR fitxategientzat:

```sh
$ mkdir adr
```

ADR bakoitzeko, sortu testu-fitxategi bat, adibidez `choose-database.md`:

```sh
$ vi choose-database.md
```

Idatzi nahi duzun guztia ADR-an. Ikus biltegi honetako txantiloiak ideien bila.

Egin commit ADR-a zure git biltegian.

## ADR-etarako Claude Code skill-ak

Biltegi honek bi [Claude Code](https://claude.com/claude-code) skill eskaintzen ditu [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/) direktorioan, AA kodeketa-agente batek proiektu honek gomendatzen duen moduan ADR-ak idatzi eta mantendu ditzan:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — helburu orokorrekoa, edozein proiektutan ADR bat idazten duen edonorentzat. Erabaki batek ADR bat behar duen erabakitzen laguntzen du, `adr/` edo `decisions/` direktorio bat prestatzen du, fitxategiaren izena ematen du, barne dauden hamaika eskeletoen artean txantiloi bat hautatzen du, eta Testuinguru/Erabakia/Ondorioak atal sendoak idazten ditu.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — biltegi honen mantentzaileentzat bereziki. Biltegiaren antolaketa, README/locales ispilatze-konbentzioa eta txantiloi, adibide edo tresna-esteka berri bat gehitzeko urrats zehatzak dokumentatzen ditu.

Skill bat erabiltzeko, kopiatu bere karpeta lanean ari zaren biltegiaren erroko `.claude/skills/` direktorioan (edo `~/.claude/skills/` direktorioan proiektu guztietan eskuragarri egon dadin), eta eskatu Claude Code-ri ADR bat idazteko edo berrikusteko.

## ADR-etarako fitxategi-izenen konbentzioak

ADR-ak testu-fitxategi tipikoetan sortzea aukeratzen baduzu, baliteke zure ADR fitxategi-izenen konbentzio propioa asmatu nahi izatea.

Formatu zehatza duen fitxategi-izenen konbentzioa erabiltzea nahiago dugu.

Adibideak:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Gure fitxategi-izenen konbentzioa:

  * Izenak orainaldiko aditz-esapide inperatibo bat dauka. Horrek irakurgarritasuna errazten du eta gure commit-mezuen formatuarekin bat dator.

  * Izenak letra xehea eta gidoiak erabiltzen ditu (biltegi honen berdin). Irakurgarritasunaren eta sistemaren erabilgarritasunaren arteko oreka da.

  * Luzapena markdown da. Hori baliagarria izan daiteke formatua errazteko.

## ADR onak idazteko iradokizunak

ADR on baten ezaugarriak:

* Arrazoibidea: Azaldu zergatik hartu den AD jakin hori. Horrek testuingurua (ikus behean), aukera potentzial desberdinen alde onak eta txarrak, ezaugarrien alderaketak, kostu/onura eztabaidak eta gehiago izan ditzake.

* Espezifikoa: ADR bakoitzak AD bati buruzkoa izan behar du, ez hainbati.

* Denbora-zigiluak: Identifikatu ADR-ko elementu bakoitza noiz idatzi den. Hori bereziki garrantzitsua da denboran alda daitezkeen alderdietan, hala nola kostuetan, egutegietan, eskalatzean eta antzekoetan.

* Aldaezina: Ez aldatu ADR batean lehendik dagoen informazioa. Horren ordez, zuzendu ADR-a informazio berria gehituz, edo ordeztu ADR-a beste ADR berri bat sortuz.

ADR bateko "Testuinguru" atal on baten ezaugarriak:

* Azaldu zure erakundearen egoera eta negozio-lehentasunak.

* Sartu zure taldeen osaera sozialean eta trebetasunetan oinarritutako arrazoibideak eta kontuan hartzekoak.

* Sartu garrantzitsuak diren alde onak eta txarrak, eta deskribatu zure behar eta helburuekin bat datozen terminoetan.

ADR bateko "Ondorioak" atal on baten ezaugarriak:

* Azaldu erabakia hartzearen ondoren zer gertatzen den. Horrek ondorioak, emaitzak, irteerak, jarraipenak eta gehiago izan ditzake.

* Sartu ondorengo ADR-ei buruzko informazioa. Nahiko ohikoa da ADR batek ADR gehiagoren beharra eragitea, adibidez ADR batek aukera orokor handi bat egiten duenean eta horrek, aldi berean, erabaki txiki gehiagoren beharra sortzen duenean.

* Sartu ekintzaren osteko berrikuspen-prozesuak. Taldeek ADR bakoitza hilabete beranduago berrikustea ohikoa da, ADR-ko informazioa praktikan gertatutakoarekin alderatzeko, ikasi eta hazteko.

ADR berri batek aurreko ADR baten lekua har dezake:

* Aurreko ADR bat ordezkatzen edo baliogabetzen duen AD bat hartzen denean, ADR berri bat sortu behar da

## ADR adibide-txantiloiak

Sarean bildu ditugun ADR adibide-txantiloiak:

- [Michael Nygarden ADR txantiloia](txantiloiak/michael-nygarden-erabaki-erregistroaren-txantiloia/) (sinplea eta ezaguna)

- [Jeff Tyree eta Art Akermanen ADR txantiloia](txantiloiak/jeff-tyree-eta-art-akermanen-erabaki-erregistroaren-txantiloia/) (sofistikatuagoa)

- [Eredu alexandriarrerako ADR txantiloia](txantiloiak/eredu-alexandriarrerako-erabaki-erregistroaren-txantiloia/) (sinplea, testuinguruaren xehetasunekin)

- [Negozio-kasurako ADR txantiloia](txantiloiak/negozio-kasurako-erabaki-erregistroaren-txantiloia/) (MBA-orientatuagoa, kostuekin, SWOT-ekin eta iritzi gehiagorekin)

- [Markdown Any Decision Records (MADR) proiektuaren ADR txantiloia](txantiloiak/madr-proiektuaren-erabaki-erregistroaren-txantiloia/) (bertsio sinplea eta zabala; azken honek aukerak eta haien alde on eta txarrak azpimarratzen ditu)

- [Planguage erabiltzen duen ADR txantiloia](txantiloiak/planguage-erabiltzen-duen-erabaki-erregistroaren-txantiloia/) (kalitatearen bermean orientatuagoa)

- [Erabaki Tekniko Garrantzitsuetarako (ITD) txantiloia, Ignacio Larrañagarena](txantiloiak/erabaki-tekniko-garrantzitsuetarako-erabaki-erregistroaren-txantiloia/) (meheak eta erabakia-lehenengo, zuzendaritzaren berrikuspen azkarrerako optimizatua)

## ADR-etarako talde-lanerako aholkuak

Zure taldearekin erabaki-erregistroak erabiltzea pentsatzen ari bazara, hona hemen talde askorekin lan eginez ikasi ditugun aholku batzuk.

Zure taldekideak gidatzeko aukera duzu, "zer" derrigortu beharrean "zergatik"-ari buruz elkarrekin hitz eginez. Adibidez, erabaki-erregistroak taldeek adimentsuago pentsatzeko eta hobeto komunikatzeko modu bat dira; erabaki-erregistroek ez dute baliorik gertatu ondoren behartutako paperezko eskakizun bat baino ez badira.

Talde batzuek "erabakiak" izena nahiago dute "ADR-ak" laburdura baino. Talde batzuek "decisions" direktorio-izena erabiltzen dutenean, bonbilla piztu izan balitz bezala da, eta taldeak informazio gehiago sartzen hasten da direktorioan, esaterako hornitzaileen erabakiak, plangintza-erabakiak, programazio-erabakiak eta abar. Informazio mota horiek guztiek txantiloi bera erabil dezakete. Hipotesi gisa, jendeak azkarrago ikasten du hitzekin ("erabakiak") laburdurekin ("ADR-ak") baino, jendea gehiago motibatzen da lanean dauden dokumentuak idazteko "erregistro" hitza kentzen denean, eta, gainera, garatzaile eta kudeatzaile batzuek ez dute gustuko "arkitektura" hitza.

Teorian, aldaezintasuna ideala da. Praktikan, aldakortasunak hobeto funtzionatu du gure taldeentzat. Informazio berria lehendik dagoen ADR-an sartzen dugu, data-zigiluarekin eta informazioa erabakiaren ondoren iritsi zela dioen ohar batekin. Ikuspegi horrek guztiok eguneratu dezakegun "dokumentu bizia" sortzen du. Eguneraketa tipikoak gertatzen dira taldekide berrien, eskaintza berrien edo gure erabileren mundu errealeko emaitzen bidez informazioa jasotzen dugunean, edo hirugarrenen aldaketa geroztikoen ondorioz, esaterako hornitzaileen gaitasunak, prezio-planak, lizentzia-hitzarmenak eta abar.

## ADR-etarako talde-lanerako galderak

### Nork sor dezake ADR bat?

Pentsatu arlo hauetan: pertsona jakinak, rol jakinak, talde jakinak edo sail jakinak; pentsatu, halaber, ea ADR bat enkarga dezaketen pertsonarik, rolik, talderik edo sailik dagoen, hau da, beste norbaitek idatziko duen ADR bat eskatzea.

Adibide-erantzuna: Gure erakundeko edozein pertsonak, arkitektura-erabakien erregistroaren README orria irakurri badu, ADR bat proposa dezake, hau da, hura idazten hasi eta taldearekin parteka dezake.

### Zerk justifikatzen du ADR bat sortzea?

Pentsatu arlo hauetan: zure erakundearen taldeen lan-moduak, zure software-sistemaren egitura, taldeen arteko koordinazioa, epe luzeko mantentzeko gaitasuna, kanpoko interfazeak, nork atera nahi duzun onura, eta antzekoak.

Adibide-erantzuna: ADR bat sortu nahi dugu etorkizuneko garatzaileek egiten ari garenaren "zergatia" ulertzea nahi dugunean.

### Zerk justifikatzen du ADR bat ez sortzea?

Pentsatu arlo hauetan: arkitekturari buruzkoak ez diren erabakiak, edo txikiak direnak, hala nola arrisku minimokoak, bere kabuz osoak edo garatzaile bakarrekoak, edo beste nonbait guztiz estalita daudenak, adibidez estandarretan, politiketan edo dokumentazioan, edo behinekoak direnak, hala nola konponbide probisionalak, kontzeptu-frogak edo esperimentuak.

Adibide-erantzuna: ADR bat saltatu nahi dugu erabaki bat irismenean, denboran, arriskuan eta kostuan mugatua denean, edo beste nonbait estalita dagoenean.

### Zein da ADR baten bizi-zikloa?

Pentsatu arlo hauetan: sortze-prozesua, ikerketa-prozesua, erabakitze-prozesua, ezartze-prozesua eta erretiratze-prozesua. Pentsatu nola jarraitu ADR baten bizi-zikloari denboran zehar, adibidez nola eraman ADR bat egoera batetik hurrengora, eta nola jakinarazi hori interesdunei.

Adibide-erantzuna: ADR batek bost bizi-ziklo fase izatea nahi dugu: Hastea → Ikertzea → Ebaluatzea → Ezartzea → Mantentzea → Erretiratzea.

### Zein dira ADR baten bizi-zikloko urratsen irizpideak?

Pentsatu arlo hauetan: ADR baten onarpen-irizpideak, hau da, nola jakin bizi-zikloko urrats batetik hurrengora aurrera egiteko adina ona den? Arazoa argi azaldu al da? Alternatibak aztertu al dira? Konpentsazioak ondo ulertu eta dokumentatu al dira?
Testuinguru garrantzitsu guztia dago? Interesdun garrantzitsu guztiak sartu al dira? Iritzi guztiak jaso al dira?

Adibide-erantzuna: ADR bat interesdunek bozka dezaten nahi dugu talde aktiboak 1) ikerketa amaitu duenean, 2) ebaluazioa amaitu duenean, 3) ADR proposamena interesdunei argitaratu dienean iruzkinak eskatuz eta astebeteko epearekin, 4) interesdun guztien iruzkinak sartu eta erantzun direnean.

### Zein rol eta erantzukizunek elkarreragiten dute ADR batekin?

Pentsatu rol hauetan: proposatzailea, ikertzailea, ebaluatzailea, berrikuslea, onartzailea, mantentzailea eta antzekoak. Pentsatu erantzukizun hauetan: interesdunekin komunikatzea, itxaropenak betetzen direla ziurtatzea, webgunean edo intranetean partekatzea, eta lana aldian-aldian berrikustea, bereziki aldaketa garrantzitsuak gertatzen direnean.

Adibide-erantzuna: ADR bakoitzak beti kontaktu-pertsona nagusi bat, bigarren kontaktu-pertsona bat eta erantzukizuneko talde bat izatea nahi dugu; horiek arduratzen dira komunikazioez, argitalpenez, mantentzeaz, urtean behin gutxienez egiten den aldizkako berrikuspenaz eta, behar denean, azkenean erretiratzeaz.

### Nola elkarreragiten du gobernantzak ADR batekin?

Pentsatu arlo hauetan: zure erakundearen lan-moduak, adostasuna, gatazka eta eskalatzea nola kudeatu nahi duzun, eta betetze-behar bereziak, adibidez alderdi juridikoei edo giza baliabideei dagozkienak. Badago ADR bati dagokionez besteek baino eragin handiagoa izan dezaketen arlorik, pertsonarik edo talderik, hala nola onartzeko, bozkatzeko edo betoa jartzeko gai direnak?

Adibide-erantzuna: ADR baten gobernantza lehentasun-ordena honetan dago: CEO, CTO, CLO, ADR bat ezartzen duen taldea, taldeko AD-ari buruz ezagutza gehien duten adituak. Beste inork ez du gobernantzarik ADR-an deskribatzen ez bada.

### Zein printzipiok elkarreragiten dute ADR batekin?

Pentsatu arlo hauetan: zure erakundearen lan-moduak, azkar mugitzea vs. astiro mugitzea, erabaki-adostasuna vs. erabaki-gatazka, arrisku-lehentasunak vs. segurtasun-lehentasunak, eztabaida publikoa vs. eztabaida pribatua, eta antzekoak.

Adibide-erantzuna: Lidergo-printzipio hauek erabiltzen ditugu: ekintzarako joera, desadostasuna agertu eta konpromisoa hartzea, %70eko estimazioak nahikoak dira erraz atzera egin daitezkeen eta erraz isola daitezkeen erabakietarako, eta lan-modu publikoak, gure erakundearen konfidentzialtasun-hitzarmenean deskribatutako informazio konfidentzialaren salbuespenarekin.

## ADR-etarako hurrengo urratsaren kontzeptuak

[Arc42](https://arc42.org/)-k bi galdera erantzuten ditu modu pragmatikoan eta zure behar espezifikoetara egokitu daiteke. Zer dokumentatu/komunikatu beharko zenuke zure arkitekturari buruz? Nola dokumentatu/komunikatu beharko zenuke? Arc42-k arkitektura-erabakien erregistroak eta helburuei, murriztapenei, testuinguruei, kalitateari, arriskuei eta gehiagori buruzko orientazioa barne hartzen ditu.

[C4 eredua](https://c4model.com/) software-arkitekturaren diagramak egiteko ikasteko erraza eta garatzaile-lagunkoia den ikuspegia da. C4 testuinguru, ontzi, osagai eta kodearen diagrama hierarkikoen multzoa da, sistemaren paisaiarako, dinamikoetarako eta hedapenerako diagrama osagarriekin.

## Arkitektura-diagramak, ikuspegiak eta ikuspuntuak

Arkitektura-diagrama bati "arkitektura-ikuspegi" deitzen zaio.

"Arkitektura-ikuspegi" bat "arkitektura-ikuspuntu" baten instantzia da.

"Arkitektura-ikuspuntu" batek kezka zehatzak kontuan dituen audientzia zehatz bat du.

Arkitektura-ikuspuntuen adibideak, ikuspegien adibideak eta diagramen adibideak:

- Negozio-gaitasunak (Business Capabilities)

- Goi-mailako negozio-prozesuak

- [Balio-korronteak (Value Streams)](https://en.wikipedia.org/wiki/Value_stream)

- Aplikazio-osagaietan mapatutako software-funtzioak

- [C4 ereduaren](https://en.wikipedia.org/wiki/C4_model) testuinguru-diagrama (TO-BE / AS-IS)

- [C4 ereduaren](https://en.wikipedia.org/wiki/C4_model) ontzi-diagrama (TO-BE / AS-IS)

- Datu-entitateak aplikazio-osagaietan mapatzeko [Entitate-erlazio diagrama](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD)

- Sistemen barruko eta integrazioetarako fluxu funtzionalak deskribatzeko [sekuentzia-diagramak](https://en.wikipedia.org/wiki/Sequence_diagram)

- Aplikazio-osagaien arteko datu-fluxuak deskribatzeko [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagramak

- Negozio-prozesuak / erabiltzaile-eszenatokiak deskribatzeko [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagramak

- [Identitate eta Sarbide Kudeaketa (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) diagramak

- Aplikazio-osagai bakoitzeko rolekin [Rol-oinarritutako Sarbide Kontrola (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) diagramak

- Aplikazio-osagai bakoitzeko atributuekin [Atributu-oinarritutako Sarbide Kontrola (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) diagramak

- Pribatutasun-diagramak

Lotutako diagramak:

- Erabilera-kasuen diagramak (Use Case Diagram) erabilera-kasuak erakusten dizkie kudeaketari/bezeroei, eskakizunen aurretik datozenak, software-arkitekturaren aurretik datozenak.

- Hedapen-diagramak (Deployment Diagram) software-osagaiak hedatzen diren hardware/ordenagailu fisikoak erakusten ditu.
- Datu-fluxuaren diagramak (Data Flow Diagram) datuak sistematik nola mugitzen eta eraldatzen diren erakusten du.
- Sekuentzia-diagramak (Sequence Diagram) HTTP bezalako protokoloek denbora-ardatzean nola funtzionatzen duten erakusteko erabiltzen da.

- Jarduera-diagramak (Activity Diagram) software-sistema batek egiten duen jardueren lan-fluxua irudikatzen du, NPC AA bezala.

## Erabakietarako fitness funtzioak kode gisa

Fitness funtzioak programazio-kodez idatzitako egiaztapen automatizatu objektiboak dira, erabakiak mantentzen ari direla egiaztatzen dutenak.

- Fitness funtzioek erabakiak probagarri eta bermagarri egiten dituzte.

- Erabakietarako fitness funtzioek asko lagun dezakete kalitatearen bermean, arau-prozesuetan eta gobernantza-helburuetan.

### Nola lotzen diren fitness funtzioak erabakiekin

Erabaki-erregistro batek erabakia dokumentatzen du, eta fitness funtzio batek erabakia ziurtatzen du.

- Adibide-erabakia: Gertaeren iturburu-bilketa (event sourcing) erabiltzen dugu ikuskaritza-eskakizunetarako.

- Adibide-fitness funtzioa: Etengabeko integrazioko zerbitzaria erabiltzen dugu egoera-aldaketa guztiek gertaerak sortu behar dituztela probatzeko.

### Zergatik laguntzen dute fitness funtzioek erabakietan

Neurketa objektiboak: Fitness funtzioek gainditu edo huts egiten dute, beraz lana ikusgai eta argia da.

Etengabeko erabilera: Fitness funtzioak zure arau bizidunak dira, commit eta build bakoitzean exekutatzen direnak.

Berregituratzeko konfiantza: Fitness funtzioek erabaki-arauen erroreak automatikoki harrapatzen dituzte.

Eskalagarria den gobernantza: Fitness funtzioek estandarrak ziurtatzen dituzte oztoporik sortu gabe.

### Fitness funtzioek AA erabil dezakete?

Fitness funtzioek AA LLM-en abantaila har dezakete erabakietarako, zure lanari buruzko galderak eginez,
esaterako zure planei, kodeari, eskemei, API-ei eta gehiagori buruz:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Arkitektura-unitate probak

[ArchUnit](https://www.archunit.org/): egiaztatu Java kodearen arkitektura-arauak edozein Java unitate-proba esparru arrunt erabiliz.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): egiaztatu TypeScript eta JavaScript kodearen arkitektura-arauak Jest, Vitest, Jasmine eta abar erabiliz.

## Pull request-etarako erabaki-babesak

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)-ek
erabaki-erregistro egokiak une egokian azaleratzen ditu automatikoki — garatzaile
bat erabaki horiek estaltzen dituen kodea aldatzen ari denean. Garatzaileek
batu aurretik dokumentu-karpeta bat irakurriko dutelakoan egon beharrean, testuinguru
garrantzitsua zuzenean pull request-ean agertzen da.

Erabaki-erregistro mota guztietarako funtzionatzen du: arkitektura-erabakiak,
datu-erabakiak, betetze-erabakiak, erabaki kliniko eta medikoak, segurtasun-erabakiak
eta gehiago.

Edozein CI sistemarekin (GitLab, Jenkins, CircleCI) eta pre-commit hook gisa funtzionatzen du.
Kode irekia. MIT lizentzia.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) GitHub
Action bat da, zaintzapeko kode-bideak aldatzen direnean arkitektura-erabakien
erregistro bat gehitu edo eguneratu gabe pull request-ak huts egiten dituena. Salbuespenak esplizituak dira:
arrazoi batekin `ADR-Exempt:` lerro batek atea gainditzen du eta lanaren laburpenean idazten da.
Txantiloiarekiko neutroa, mendekotasunik gabe. Kode irekia. MIT lizentzia.

## Informazio gehiagorako

Sarrera:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Txantiloiak:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Sakonean:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - hileroko software-arkitekturako ikasgai librea

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Tresnak:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Enpresa-espezifikoko orientazioa:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Adibideak:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Bideoak:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcastak:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Liburuak:

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

Ikus gainera:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Erabakiak arrazoibide esplizituarekin, hipotesiekin, egoera kognitiboarekin eta konpentsazioekin irudikatzeko hornitzailearekiko neutroa den makinak irakur dezakeen YAML/JSON formatua. ADR-ak osatzen ditu erabakien dokumentazioari arrazoibide egituratua eta baliozkotu daitekeena gehituz.
