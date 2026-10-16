# Microsoft Azure DevOps

Saturs:

* [Kopsavilkums](#kopsavilkums)
  * [Jautājums](#jautājums)
  * [Lēmums](#lēmums)
  * [Statuss](#statuss)
* [Detaļas](#detaļas)
  * [Pieņēmumi](#pieņēmumi)
  * [Ierobežojumi](#ierobežojumi)
  * [Pozīcijas](#pozīcijas)
  * [Arguments](#arguments)
  * [Sekas](#sekas)
* [Saistītais](#saistītais)
  * [Saistītie lēmumi](#saistītie-lēmumi)
  * [Saistītās prasības](#saistītās-prasības)
  * [Saistītie artefakti](#saistītie-artefakti)
  * [Saistītie principi](#saistītie-principi)
* [Piezīmes](#piezīmes)
  * [Microsoft Devops CI: neapmierinošs piedzīvojums](#microsoft-devops-ci-neapmierinošs-piedzīvojums)
  * [Hacker News diskusijas akcenti](#hacker-news-diskusijas-akcenti)
  * [Windows Development MVP](#windows-development-mvp)
  * [Edward Thomson (Azure PM) kopsavilkums](#edward-thomson-azure-pm-kopsavilkums)


## Kopsavilkums


### Jautājums

Mēs vēlamies izmantot DevOps, lai būvētu, integrētu, izvietotu un mitinātu savus projektus. Mēs apsveram Microsoft Azure DevOps.

  * Mēs vēlamies, lai izstrādātāja pieredze būtu ātra un uzticama gan DevOps iestatīšanai, piemēram, konfigurēšanai, gan pastāvīgai lietošanai, piemēram, ātriem būvēšanas laikiem.
  
  * Mēs vēlamies apsvērt Microsoft Azure izmantošanu kopumā projekta lietotņu, datubāzu utt. mitināšanai.


### Lēmums

Nolēmām pret Microsoft Azure DevOps.


### Statuss

Izlemts. Atvērti pārskatīšanai, ja un kad pienāks jauna nozīmīga informācija.


## Detaļas


### Pieņēmumi

Visi parastie DevOps pieņēmumi, piemēram, grāmatā Accelerate.

  * Ātras būvēšanas ir ievērojams palīgs. Tas paātrina atgriezeniskās saites cilpas.

  * Mēs varam apmainīt daļas ar alternatīvu piegādātāju daļām, t. i., mēs varētu vēlēties ienest savus ātrākos būvēšanas serverus vai izmantot savu izvēlēto versiju kontroles sistēmu, vai saskaņot ar pašmitinātu nepārtrauktās integrācijas serveri.
  
  * Racionalizēta lietojamība ir ievērojams palīgs izstrādātāja pieredzei un savukārt smalkām jomām, piemēram, konsekvencei, skaidrībai, drošībai un mācīšanās līknes vieglumam.

  * Kad kaut kas ir bojāts vai problemātisks, mēs vēlamies efektīvu veidu, kā ziņot par problēmu. Tas ir īpaši svarīgi jebkurām ar drošību saistītām problēmām.


### Ierobežojumi

Nav zināmu. Azure ir publicējis apņemšanos labi sadarboties ar ārējiem rīkiem.


### Pozīcijas

Mēs apsvērām Microsoft Azure Devops izmantošanu salīdzinājumā ar AWS, kas ir pašreizējais risinājums.

Mēs eksperimentējām ar Azure DevOps, Azure Pipelines, Azure Repo un jauna servera palaišanu Azure ar Terraform.

Mēs eksperimentējām ar atbalsta saņemšanu no Microsoft pārstāvjiem.

Mēs vāktām informāciju no kolēģiem blogos un Hacker News.


### Arguments

Azure DevOps reklamē teicamu piedāvājumu kopumu, taču tie neiztur pārbaudi, tie nedarbojas labi kopā, un atbalsts ir slikts.

Mūsu tiešā pieredze:

  * Azure iestatīšana ir lietotāja saskarņu juceklis, no kurām dažas pārklājas ar Microsoft kontiem, dažas ne. Piem., ir Azure pieteikšanās, Microsoft.com pieteikšanās, Live.com pieteikšanās utt., un visas ir vienlaikus spēlē.

  * Iestatīšanas laikā mēs saskārāmies ar nelielu drošības problēmu un neatradām risinājumu. Mēs mēģinājām par to ziņot daudzos veidos daudziem Microsoft pārstāvjiem, bez panākumiem. Mēs veiksmīgi ziņojām par to Microsoft drošības dienestam, kas atbildēja ar „won't fix” (netiks labots).

  * Dokumentācija bieži ir vai nu nepareiza, vai novecojusi. Vismaz daļēji tas ir Microsoft sliktās meklētājprogrammas dēļ, un daļēji nepietiekamas SEO dēļ.
  
  * Terraform iestatīšana ir labi dokumentēta un darbojas. Tomēr Terraform atbalsts ir vājš salīdzinājumā ar AWS, jo Microsoft veido biznesa attiecības ar piegādātājiem, lai veidotu ķēdētus Terraform iestatīšanas piemērus.

Mūsu kolēģu pieredze:

  * Pēc mūsu pašu aklā novērtējuma mēs meklējām kolēģu pieredzi. Atrastais apstiprināja mūsu pieredzi.

  * Kolēģi ziņoja par papildu problēmām ar būvēšanas laikiem un problēmām ar savu būvēšanas serveru izmantošanu. Šīs problēmas ir ievērojami nopietnākas nekā UI problēmas, jo būvēšanas veikšana ir būvēšanas cauruļvada galvenais mērķis, un mēs paredzam veikt daudzas dienā.

  * Mēs atradām teicamu Azure komandas biedru līdzdalību diskusiju vietās. Pateicība Microsoft par to. Mūs īpaši pārsteidza Edward Thomson, Azure PM un programmētājs, par viņa līdzdalību, tiešumu un tehniskajiem paskaidrojumiem.


### Sekas

Microsoft Azure DevOps izvēle, visticamāk, būs dārgāka (~3 reizes) laikā un izmaksās nekā Azure neizvēle.


## Saistītais


### Saistītie lēmumi

Ja izvēlamies Azure DevOps, ir daudz saistītu piedāvājumu, tostarp Azure Repo, Azure Pipeline utt. Mēs uzskatām, ka, ja izvēlēsimies Azure Devops, tas var atvieglot vairāk Azure iespēju izmantošanu vai apgrūtināt citu piegādātāju iespēju izmantošanu.

Mēs uzskatām, ka Microsoft dara lielus soļus izstrādātāja pieredzē, un redzam, ka Microsoft veic lielus izstrādātāju rīku (piem., GitHub) un atkarību (piem., Citus) iegādes.

Ja izvēlamies Azure DevOps, mēs varētu vēlēties uzsvērt Microsoft iegūto piedāvājumu izvēli, kā arī mēs varētu vēlēties pieiet iegūtajiem piedāvājumiem ar lielāku piesardzību/novērtēšanu iespējamās audu noraidīšanas (tissue-rejection) dēļ, piem., personāla mainības riska dēļ.


### Saistītās prasības

Mēs vēlamies, lai būvēšanas laiki būtu ļoti ātri. Mēs piekrītam maksāt augstu piemaksu par to. Tas ir tāpēc, ka mēs vēlamies ļoti ātri iterēt.

Mēs vēlamies, lai uzticamība būtu ļoti augsta. Mēs piekrītam maksāt augstu piemaksu par to. Tas ir tāpēc, ka mēs testējam augstvērtīgus lietošanas gadījumus, tostarp finanšu darījumus, konfidenciālus darījumus utt.

Mūsu četri svarīgākie DevOps KPI ietver vidējo atgūšanās laiku, kas prasa ātras būvēšanas un augstu uzticamību.


### Saistītie artefakti

Mēs vēlamies, lai būvēšanas sistēma izvadītu artefaktus, kas piemēroti izmantošanai citās sistēmās, piemēram, Artifactory.


### Saistītie principi

Viegli atgriezenisks. Mēs varam novērtēt Azure DevOps paralēli ar pašreizējo AWS.


## Piezīmes


### Microsoft Devops CI: neapmierinošs piedzīvojums

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Bloga ieraksts.

„Kā programmatūras izstrādātājs es no pirmavota zinu, cik grūti ir ātri un lēti izveidot kvalitatīvus produktus. Tā ir mākslas forma, kas mums dažreiz izdodas, bet citreiz pārvēršas par kaut ko līdzīgu Obamas laikmeta valdības veselības aprūpes vietnei. Mūsu kontroles līmenis pār gala produktu ir atšķirīgs, un vaina par neveiksmi bieži krīt uz nepareizajiem cilvēkiem lēmumu pieņemšanas hierarhijā. Microsoft Azure DevOps (agrāk pazīstams kā Visual Studio Team Services), neskatoties uz acīmredzami labiem nodomiem, ir ideāla sliktu lēmumu un vāja izpildījuma vētra.”


### Hacker News diskusijas akcenti

https://news.ycombinator.com/item?id=18983586

„Mēs savā darbā plaši izmantojam Azure DevOps, un, izmantojot GitHub, Gitlab, pašmitinātus risinājumus, Jenkins, TeamCity... Azure DevOps ir pēdējā vietā.”

„UI ir briesmīgi neveikls visur. Man vissliktākais ir izmaiņu pieprasījumi (pull requests). Neticami grūti strādāt ar cilvēkiem pie izmaiņu pieprasījuma. Es pat nevaru norādīt uz „vienu” konkrētu problēmu – mums tas ir bojāts visur.”

„Azure Devops ir kaut kas, ko es vēlos mīlēt. UI pastāvīgi mainās, bet neatrisina pamatā esošās kļūdas, kas pastāv jau sen.”

„Rīki nav labi integrēti, UI ir ļoti lēns, nav panelī skata ar aktīvajiem izmaiņu pieprasījumiem, būvējumiem, izlaidumiem utt. manām iecienītākajām repozitorijām. Būvēšanas/izvietošanas laiki ir neprātīgi lēni.”

„Mēs mēģinājām izmantot arī Azure Boards (darba vienības, dēļi, atlikumi utt.). Au. Tas ir pilnīgs UI juceklis ar nesaistītām idejām. Tā vietā, lai labi īstenotu vienu lietu, viņi briesmīgi īstenoja divdesmit četras lietas.”


### Windows Development MVP

Šeit Windows Development MVP. Man šķiet, ka man jāuzņemas daļa atbildības par to, ka neesmu bijis skaļāks par šīm problēmām. Bet jāsaka, esmu vīlies, dzirdot, ka jūs esat „pārsteigti” par UX problēmām. Es jūsu cilvēkiem esmu teicis, ka UX ir briesmīgs (piem., jau pirms palaišanas), un turpināju dzirdēt „mēs zinām, mēs to labojam”. Es sākšu formalizēt atsauksmes un virzīt tās cauri caurulēm, sekojiet līdzi. Esmu arī vietējais (Bellevue), labprāt nāktu un mēģinātu izveidot cauruļvadu mūsu salīdzinoši vienkāršajai atvērtā pirmkoda .net/wpf/uwp lietotnei. Man šķiet, ka tas atvērs acis mums abiem.

Daži piemēri:

* Nevar izveidot cauruļvadu ar git repozitoriju, kas satur apakšmoduļus

* Neizdevās rediģēt PATH dažiem pielāgotiem rīkiem

* Jaunā cauruļvada pieredzei vienkārši nav jēgas, jaunie lietotāji, klikšķinot apkārt, galu galā nonāks nepareizā dokumentācijā.


### Edward Thomson (Azure PM) kopsavilkums

Es uzrakstīju kodu, kas sapludina jūsu izmaiņu pieprasījumus. Programmu vadītājs (Program Manager) Microsoft Azure DevOps; agrāk programmatūras inženieris versiju kontroles rīkiem GitHub, Microsoft, SourceGear.

https://www.edwardthomson.com/

libgit2 līdzuzturētājs. https://libgit2.github.io

All Things Git, aplādes par Git, līdzvadītājs. https://www.allthingsgit.com/

Developer Tools Weekly, ziņojumlapas par izstrādes rīkiem, kurators. https://developertoolsweekly.com/
