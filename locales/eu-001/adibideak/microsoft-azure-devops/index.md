# Microsoft Azure DevOps

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
  * [Microsoft Devops CI: abentura asegarria ez dena](#microsoft-devops-ci-abentura-asegarria-ez-dena)
  * [Hacker News eztabaidaren nabarmenak](#hacker-news-eztabaidaren-nabarmenak)
  * [Windows Development MVP](#windows-development-mvp)
  * [Edward Thomson-en (Azure PM) laburpena](#edward-thomson-en-azure-pm-laburpena)


## Laburpena


### Arazoa

Devops erabili nahi dugu gure proiektuak eraiki, integratu, hedatu eta ostatatzeko. Microsoft Azure DevOps aztertzen ari gara.

  * Garatzailearen esperientzia azkarra eta fidagarria izatea nahi dugu, bai devops-aren konfigurazioan, adib. konfiguratzean, bai etengabeko erabileran, adib. build denbora azkarrak.
  
  * Microsoft Azure osotasunean erabiltzea aztertu nahi dugu, proiektuko aplikazioak, datu-baseak eta abar ostatatzeko.


### Erabakia

Microsoft Azure DevOps-en aurka erabaki da.


### Egoera

Erabakia. Informazio esanguratsu berria iristen bada berriz aztertzeko irekia.


## Xehetasunak


### Hipotesiak

Devops-eko ohiko hipotesi guztiak, Accelerate liburuan bezala.

  * Build azkarrak laguntza handia dira. Horrek feedback-begiztak bizkortzen ditu.

  * Beste hornitzaile batzuen piezak sartu/atera ditzakegu, hau da, gure abiadura handiagoko build zerbitzariak ekarri nahi izan ditzakegu, edo gure aukerako bertsio-kontroleko sistema erabili, edo norberak ostatatutako etengabeko integrazio-zerbitzari batekin koordinatu.
  
  * Erabilgarritasun arindua laguntza handia da, garatzailearen esperientziarako, eta, aldi berean, koherentzia, argitasuna, segurtasuna eta ikaskuntza-kurbaren erraztasun bezalako alderdi sotiletarako.

  * Zerbait hautsita edo arazotsua dagoenean, arazoa jakinarazteko modu eraginkorra nahi dugu. Hau bereziki garrantzitsua da segurtasunarekin lotutako arazoetarako.


### Murriztapenak

Ezagunik ez. Azure-k kanpoko tresnekin ondo funtzionatzeko konpromiso argitaratua du.


### Jarrerak

Microsoft Azure DevOps vs. AWS aztertu dugu, azken hau lehendik zegoen eta.

Azure DevOps, Azure Pipelines, Azure Repo eta zerbitzari berrien Azure-n Terraform bidez abiaraztea frogatu ditugu.

Microsoft ordezkariengandik laguntza lortzea frogatu dugu.

Informazioa bildu dugu kideengandik blogetan eta Hacker News-en.


### Arrazoibidea

Azure DevOps-ek eskaintza-sorta bikaina iragartzen du, baina ez dira iraunkorrak, ez dute ondo elkarrekin funtzionatzen, eta laguntza eskasa da.

Gure lehen eskuko esperientzia:

  * Azure-ren konfigurazioa UI nahaspila bat da, batzuk Microsoft kontuekin gainjartzen direnak, beste batzuk ez. Adib. Azure saio-hasiera dago, Microsoft.com saio-hasiera, Live.com saio-hasiera, eta abar, eta guztiak aldi berean erabiltzen dira.

  * Segurtasun-arazo txiki bat aurkitu genuen konfigurazioan, eta ez genuen konponbiderik aurkitu. Modu askotan saiatu ginen jakinarazten, Microsoft ordezkari askorekin, arrakastarik gabe. Microsoft-en segurtasun-sailari jakinaraztea lortu genuen, eta ez zela konponduko erantzun zuen.

  * Dokumentazioa sarritan okerra edo zaharkitua da. Honen zati bat, gutxienez, Microsoft-en bilatzaile eskasagatik da, eta beste zati bat SEO eskasagatik.
  
  * Terraform-en konfigurazioa ondo dokumentatuta dago, eta funtzionatzen du. Hala ere, Terraform-en laguntza AWS-rekin alderatuta ahula da, Microsoft hornitzaileekin negozio-harremanak eraikitzen ari delako Terraform konfigurazio-adibide kateatuak egiteko.

Gure kideen esperientziak:

  * Gure kasuan itsu-itsuan ebaluazioa egin ondoren, kideen esperientziak bilatu genituen. Aurkitutakoak gure esperientziak baieztatu zituen.

  * Kideek build denborei buruzko arazo gehigarriak eta zerbitzari propioa ekartzeari buruzko arazoak jakinarazi zituzten. Arazo hauek UI arazoak baino nabarmen larriagoak dira, build-ak egitea build hodi baten helburu nagusia delako, eta egunean asko egitea espero dugulako.

  * Azure-ko taldekideen parte-hartze bikaina aurkitu genuen eztabaida-guneetan. Zorionak Microsoft-i horregatik. Bereziki Edward Thomson, Azure PM eta kodetzailea, miresten dugu bere parte-hartzeagatik, zuzentasunagatik eta azalpen teknikoengatik.


### Ondorioak

Microsoft Azure DevOps aukeratzea garestiagoa izango dela dirudi (~3x) denboran eta kostuan Azure ez aukeratzea baino.


## Erlazionatuta


### Erlazionatutako erabakiak

Azure DevOps aukeratzen badugu, lotutako eskaintza asko daude, Azure Repo, Azure Pipeline eta abar barne. Uste dugu Azure Devops aukeratzen badugu, horrek Azure gaitasun gehiago erabiltzea errazago bihur dezakeela, edo beste hornitzaile batzuen gaitasunak erabiltzea zailago.

Uste dugu Microsoft urrats handiak ematen ari dela garatzailearen esperientzian, eta Microsoft garapen-tresna (adib. GitHub) eta mendekotasun (adib. Citus) erosketa handiak egiten ikusten dugu.

Azure DevOps aukeratzen badugu, Microsoft-en erosketa-eskaintzak aukeratzea azpimarratu nahi izan dezakegu, eta erosketa-eskaintzetara arreta/ebaluazio handiagoz hurbildu nahi izan dezakegu ehun-baztertze potentzialagatik, adib. langileen errotazio-arriskua.


### Erlazionatutako eskakizunak

Build denborak oso azkarrak izatea nahi dugu. Horregatik prima handia ordaintzea onartzen dugu. Hau da oso azkar iteratu nahi dugulako.

Fidagarritasuna oso handia izatea nahi dugu. Horregatik prima handia ordaintzea onartzen dugu. Hau da balio handiko erabilera-kasuak probatzen ari garelako, finantza-transakzioak, transakzio konfidentzialak eta abar barne.

Gure devops KPI nagusi 4en artean berreskuratze-denbora ertaina dago, eta horrek build azkarrak eta fidagarritasun handia behar ditu.


### Erlazionatutako artefaktuak

Build sistemak beste sistemetan, esaterako Artifactory-n, erabiltzeko egokiak diren artefaktuak ematea nahi dugu.


### Erlazionatutako printzipioak

Erraz atzera egin daitekeena. Azure DevOps ebalua dezakegu lehendik dagoen AWS-ren paraleloan.


## Oharrak


### Microsoft Devops CI: abentura asegarria ez dena

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Blog sarrera.

"Software-garatzaile gisa, lehen eskutik dakit zein zaila den kalitatezko produktuak azkar eta merke eraikitzea. Batzuetan ondo egiten dugun arte bat da, eta beste batzuetan Obama aroko osasun-arreta gobernu-gunearen antzeko zerbait bihurtzen da. Lortutako produktuaren gaineko gure kontrol-maila aldatu egiten da, eta porrotaren errua sarritan erabaki-hierarkiako gaizkileei egozten zaie. Microsoft-en Azure DevOps (lehen Visual Studio Team Services bezala ezaguna), asmo on argiak izan arren, erabaki txarren eta exekuzio eskasaren ekaitz perfektua da."


### Hacker News eztabaidaren nabarmenak

https://news.ycombinator.com/item?id=18983586

"Azure DevOps asko erabiltzen dugu lanean eta, GitHub, Gitlab, norberak ostatatutako soluzioak, Jenkins, TeamCity erabili ondoren... Azure DevOps azkenengoa da."

"UI-a izugarri traketsa da leku guztietan. Niretzat txarrena pull request-ak dira. Izugarri zaila da jendearekin lan egitea pull request batean. Ezin dut "arazo" jakin bat seinalatu - guretzat leku guztietan hautsita dago."

"Azure Devops maitatu nahi dudan zerbait da. UI-a aldatzen jarraitzen du, baina ez ditu urteak dituzten oinarrizko akatsak konpontzen."

"Tresnak ez daude ondo integratuta, UI-a oso motela da, ez dago nire biltegi gogokoenetako pull request, build, release aktiboen panel-ikuspegirik. Build/Deploy denborak zoragarriro motelak dira."

"Azure Boards (Work Items, Boards, Backlogs, eta abar) ere erabiltzen saiatu ginen. Aupa. Elkarrekin lotu gabeko ideien UI nahaspila osoa da. Gauza bat ondo ezarri beharrean, dozena bat gauza txarto ezarri zituzten."


### Windows Development MVP

Windows Development MVP naiz hemen. Uste dut ardura batzuk hartu behar ditudala arazo hauei buruz ozenago ez egoteagatik. Baina esan behar dut, etsita nago "harrituta" zaudetela UX arazoekin. UX-a ikaragarria dela esaten ari nintzen zure jendeari (adib. martxan jarri aurretik ere) eta "badakigu, konpontzen ari gara" entzuten jarraitzen nuen. Feedbacka formalizatzen hasiko naiz eta hodietatik bultzatuko dut, egon adi. Lokala ere banaiz (Bellevue), etorri eta gure oss .net/wpf/uwp aplikazio nahiko sinplearen hodia egiten saiatu nahi nuke. Susmoa dut begiak irekiko dizkigula biontzat.

Adibide batzuk:

* Ezin duzu pipeline bat eraiki azpimodulu dituen git biltegi batekin

* Ezinezkoa iruditu zitzaidan PATH aldatzea tresna pertsonalizatu batzuetarako

* Pipeline Berriaren esperientziak ez du zentzu handirik, erabiltzaile berriak klik eginez gaizki dagoen Docs-era iristen dira azkenean.


### Edward Thomson-en (Azure PM) laburpena

Zure pull request-ak batzen dituen kodea idatzi dut nik. Microsoft-eko Azure DevOps-eko Program Manager-a; lehen GitHub, Microsoft, SourceGear-en bertsio-kontroleko tresnen software-ingeniaria.

https://www.edwardthomson.com/

libgit2-ren kide-mantentzailea. https://libgit2.github.io

All Things Git-en kide-aurkezlea, Git-i buruzko podcasta. https://www.allthingsgit.com/

Developer Tools Weekly-ren kurator, garapen-tresnei buruzko buletina. https://developertoolsweekly.com/
