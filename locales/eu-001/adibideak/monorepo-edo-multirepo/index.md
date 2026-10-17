# Monorepo edo multirepo

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


## Laburpena


### Arazoa

Gure proiektuak hiru software-kategoria nagusiren garapena dakar:

  * Front-end GUI-ak
  * Middleware zerbitzuak
  * Back-end zerbitzariak

Garatzean, gure iturburu-kodearen kudeaketako (SCM) bertsio-kontroleko sistema (VCS) git da.

Aukeratu behar dugu git nola erabili gure kodea antolatzeko.

Goi-mailako aukera "monorepo", "polyrepo" edo "hibridoa" gisa antolatzea da:

  * Monorepo-k esan nahi du pieza guztiak biltegi handi batean jartzen ditugula
  * Polyrepo-k esan nahi du pieza bakoitza bere biltegian jartzen dugula
  * Hibridoak monorepo eta polyrepo-ren nahaste bat esan nahi du

Informazio gehiagorako ikus https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Erabakia

Monorepo erakundea/taldea/proiektua nahiko txikia denean, eta iterazio azkarra egonkortasuna mantentzea baino lehentasun handiagokoa denean.

Polyrepo erakundea/taldea/proiektua nahiko handia denean, eta egonkortasuna mantentzea iterazio azkarra baino lehentasun handiagokoa denean.


### Egoera

Erabakia. Monorepo-ak eta/edo polyrepo-ak kudeatzeko tresna berriak eskuragarri egoten badira berriz aztertzeko irekia.


## Xehetasunak


### Hipotesiak

Garatzen ari garen kode guztia erakunde baten eskaintzetarako da, ez publiko orokorrarentzat. Hau da, Broker-Dealer-ak ez du publiko orokorreko boluntario garatzaileen antzeko ezer izatea helburu.


### Murriztapenak

Murriztapenak ondo dokumentatuta daude https://github.com/joelparkerhenderson/monorepo-vs-polyrepo helbidean


### Jarrerak

Monorepo-ak aztertu ditugu Google, Facebook eta abarren estiloan. Uste dugu monorepo-en edozein eskalatze-arazo etorkizunean hain urrun dagoela, non behar ditugunerako Google eta Facebook-en praktika berberak aprobetxa ahal izango ditugula.

Polyrepo-ak aztertu ditugu Git kode irekiko proiektu tipikoen estiloan, hala nola Google Android, Facebook React eta abar. Uste dugu hauek direla publiko orokorraren parte-hartzerako (adib. munduko edonork kodean lan egin dezake) eta norbanakoaren erabilgarritasunerako (adib. proiektua bere kabuz erabiltzen da, beste pieza batzuk gabe) aukerarik onenak.


### Arrazoibidea

Erakundea/taldea/proiektua nahiko txikia denean, monorepo-a aukeratzen dugu, iterazio azkarra egonkortasuna mantentzea baino nabarmen lehentasun handiagokoa delako

Erakundea/taldea/proiektua nahiko handia denean, polyrepo-a aukeratzen dugu, egonkortasuna mantentzea iterazio azkarra baino nabarmen lehentasun handiagokoa delako.


### Ondorioak

CI+CD-rako pipeline bat badago, baliteke bera egokitu behar izatea biltegi bakar baten barruan proiektu anitz probatzeko.

CI+CD-k denbora gehiago har dezake monorepo baten build oso baterako, CI+CD-k monorepo-ko proiektu guztiak eraiki ditzakeelako.

Erakundea/taldea/proiektua hazten bada, monorepo-ak eskalatze-arazoak izango ditu.

Monorepo-aren eskalatze-arazoek polyrepo-ra trantsizioa gero eta baliotsuagoa bihur dezakete.

Monorepo-tik polyrepo-rako trantsizioa devops-eko zeregin esanguratsua da, eta plangintza, kudeaketa eta programazioa beharko ditu.


## Erlazionatuta


### Erlazionatutako erabakiak

Monorepo-ak (adib. Google Bazel) eta polyrepo-ak (adib. Lyft Refactorator) kudeatzeko lotutako tresnetarako erabakiak sortuko ditugu.


### Erlazionatutako eskakizunak

CI+CD pipeline-a garatu behar dugu gitekin ondo funtzionatzeko.


### Erlazionatutako artefaktuak

Biltegi-antolaketak hornidurarako, konfigurazio-kudeaketarako, probetarako eta antzeko devops arloetarako artefaktu lotuak izatea espero dugu. 


### Erlazionatutako printzipioak

Erraz atzera egin daitekeena. Monorepo-ak praktikan funtzionatzen ez badu, edo zuzendaritzak nahi ez badu, sinplea da polyrepo-ra aldatzea.

Bezeroarekiko obsesioa. Proiektua bezeroen eskuetan jartzea baloratzen dugu, eta uste dugu monorepo-ak polyrepo-ak baino azkarrago eraman gaitzakeela hara, eta, gainera, iterazio azkarragoan lagundu.

Pentsatu handi. Google eta Facebook monorepo-en defendatzaile sutsuak dira polyrepo-en aurrean, eskaintza nagusi guztiak batera gara/proba/hedatu daitezkeelako.


## Oharrak

Gehitu edozein ohar hemen.
