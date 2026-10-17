# Microsoft Azure DevOps

Inhalt:

* [Zesummefaassung](#zesummefaassung)
  * [Problem](#problem)
  * [Decisioun](#decisioun)
  * [Zoustand](#zoustand)
* [Detailer](#detailer)
  * [Viraussetzungen](#viraussetzungen)
  * [Restriktiounen](#restriktiounen)
  * [Positiounen](#positiounen)
  * [Argument](#argument)
  * [Implikatiounen](#implikatiounen)
* [Verwandt](#verwandt)
  * [Verwandt Decisiounen](#verwandt-decisiounen)
  * [Verwandt Ufuerderungen](#verwandt-ufuerderungen)
  * [Verwandt Artefakten](#verwandt-artefakten)
  * [Verwandt Prinzipien](#verwandt-prinzipien)
* [Notizen](#notizen)
  * [Microsoft Devops CI: An Unsatisfying Adventure](#microsoft-devops-ci-an-unsatisfying-adventure)
  * [Highlights aus der Hacker-News-Diskussioun](#highlights-aus-der-hacker-news-diskussioun)
  * [Windows Development MVP](#windows-development-mvp)
  * [Zesummefaassung vum Edward Thomson (Azure PM)](#zesummefaassung-vum-edward-thomson-azure-pm)


## Zesummefaassung


### Problem

Mir wëllen Devops benotzen, fir eis Projeten ze bauen, ze integréieren, ze deployen an ze hosten. Mir iwwerleeë Microsoft Azure DevOps.

  * Mir wëllen, datt d'Entwécklererfahrung séier an zouverlässeg ass, fir den Opbau vun den Devops, z.B. d'Konfiguréieren, wéi och fir déi lafend Notzung, z.B. séier Build-Zäiten.
  
  * Mir wëllen iwwerleeën, Microsoft Azure als Ganzt ze benotzen, fir d'Hosting vun de Projet-Apps, Datebanken, asw.


### Decisioun

Géint Microsoft Azure DevOps decidéiert.


### Zoustand

Decidéiert. Oppe fir eng nei Iwwerleeung, wann/wa nei bedeitend Informatioun ukënnt.


## Detailer


### Viraussetzungen

All déi üblech Devops-Viraussetzungen, wéi am Buch Accelerate.

  * Séier Builds sinn eng bedeitend Hëllef. Dat beschleunegt d'Feedback-Schleifen.

  * Mir kënnen Deeler vun alternative Vendoren eran-/erausschalten, dat heescht, mir wëllen eventuell eis eege méi séier Build-Server matbréngen, oder eist eegent Versiounskontrollsystem benotzen, oder mat engem selbst gehostene Continuous-Integration-Server koordinéieren.
  
  * Eng strukturéiert Benotzbarkeet ass eng bedeitend Hëllef, fir d'Entwécklererfahrung, a och fir subtil Beräicher wéi Konsistenz, Kloerheet, Sécherheet an eng einfach Léierkurve.

  * Wann eppes futti oder problematesch ass, wëlle mir e wierksame Wee, de Problem ze mellen. Dat ass besonnesch wichteg fir all sécherheetsbezunne Problemer.


### Restriktiounen

Keng bekannt. Azure huet eng publizéiert Verpflichtung, gutt mat externen Tools zesummenzeschaffen.


### Positiounen

Mir hunn iwwerluecht, Microsoft Azure Devops vs. AWS ze benotzen, deen den Amtsinhaber ass.

Mir hunn mat Azure DevOps, Azure Pipelines, Azure Repo an dem Opsetze vun engem neie Server vun Azure iwwer Terraform experimentéiert.

Mir hunn experimentéiert, Ënnerstëtzung vu Microsoft-Vertrieder ze kréien.

Mir hunn Informatioune vu Kollegen op Blogs an Hacker News gesammelt.


### Argument

Azure DevOps annoncéiert e exzellent Set u Offeren, awer si halen net, si funktionéieren net gutt zesummen, an den Support ass schlecht.

Eis direkt Erfahrung:

  * Den Azure-Setup ass e Chaos vu UIen, vun deenen e puer sech mat Microsoft-Konten iwwerlappen, an anerer net. Z.B. gëtt et eng Azure-Umeldung, eng Microsoft.com-Umeldung, eng Live.com-Umeldung, asw., a si sinn all gläichzäiteg am Spill.

  * Mir si wärend dem Setup op e klenge Sécherheetsproblem gestouss a hu keng Léisung fonnt. Mir hunn op villen Weeër probéiert, en u vill Microsoft-Vertrieder ze mellen, ouni Succès. Mir hunn en erfollegräich der Microsoft-Sécherheet gemellt, déi geäntwert huet, et gëtt net gefixt.

  * D'Dokumentatioun ass dacks entweder falsch oder verallt. Op d'mannst en Deel dovun ass der schlechter Sichmotor vu Microsoft ze verdanken, an en Deel schlechter SEO.
  
  * Den Terraform-Setup ass gutt dokumentéiert an funktionéiert. Awer d'Terraform-Ënnerstëtzung ass am Verglach zu AWS schwaach, well Microsoft Geschäftsbezéiunge mat Vendoren opbaut, fir Beispiller vun Terraform-Setups ze maachen, déi ageketst sinn.

Eis Peer-Erfahrungen:

  * Nodeems mir eis eege blann Evaluatioun gemaach hunn, hu mir no Peer-Erfahrunge gesicht. Wat mir fonnt hunn, huet eis Erfahrunge bestätegt.

  * Peers hu zousätzlech Problemer mat de Build-Zäiten gemellt, a Problemer mam Bring-your-own-Build-Server. Dës Problemer si bedeitend méi schwéier wéi UI-Problemer, well Builds ze maachen den Haaptzweck vun enger Build-Pipeline ass, an mir erwaarden, vill pro Dag ze maachen.

  * Mir hunn eng exzellent Participatioun vun Azure-Teamkollegen an den Diskussiounsberäicher fonnt. Kudos u Microsoft dofir. Mir si besonnesch beandrockt vum Edward Thomson, Azure PM a Coder, wéinst senger Participatioun, Direktheet an technesche Erklärungen.


### Implikatiounen

D'Wiel vu Microsoft Azure DevOps gesäit no u Zäit a Käschte wahrscheinlech méi deier (~3x) aus wéi Azure net ze wielen.


## Verwandt


### Verwandt Decisiounen

Wa mir Azure DevOps wielen, gëtt et vill verwandt Offeren, dorënner Azure Repo, Azure Pipeline, asw. Mir gleewen, datt, wa mir Azure Devops wielen, dat et méi einfach kann maachen, méi Azure-Fäegkeeten ze benotzen, oder et méi schwéier kann maachen, d'Fäegkeeten vun aneren Vendoren ze benotzen.

Mir gleewen, datt Microsoft grouss Fortschrëtter an der Entwécklererfahrung mécht, a mir gesinn, datt Microsoft grouss Acquisitioune vun Entwécklertools (z.B. GitHub) an Ofhängegkeeten (z.B. Citus) mécht.

Wa mir Azure DevOps wielen, da wëlle mir eventuell d'Wiel vun de Microsoft-Acquisitiounsoffere betounen, a mir wëllen eventuell d'Acquisitiounsoffere mat méi Suergfalt/Bewäertung ugoen, wéinst potenzieller Gewebsofstoussung, z.B. dem Risiko vu Mataarbechterfluktuatioun.


### Verwandt Ufuerderungen

Mir wëllen, datt d'Build-Zäite ganz séier sinn. Mir akzeptéieren, dofir eng héich Prämie ze bezuelen. Dat, well mir ganz séier iteréiere wëllen.

Mir wëllen, datt d'Zouverlässegkeet ganz héich ass. Mir akzeptéieren, dofir eng héich Prämie ze bezuelen. Dat, well mir High-Value-Use-Cases testen, dorënner Finanztransaktiounen, vertraulech Transaktiounen, asw.

Eis Top-4-Devops-KPIen enthalen déi mëttel Zäit bis zur Erhuelung, wat séier Builds an héich Zouverlässegkeet néideg mécht.


### Verwandt Artefakten

Mir wëllen, datt de Build-System Artefakten erausgëtt, déi gëeegent sinn, fir an anere Systemer benotzt ze ginn, wéi Artifactory.


### Verwandt Prinzipien

Einfach réckgängeg ze maachen. Mir kënnen Azure DevOps parallel zum AWS-Amtsinhaber evaluéieren.


## Notizen


### Microsoft Devops CI: An Unsatisfying Adventure

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Blogbäitrag.

"Als Softwareentwéckler weess ech aus éischter Hand, wéi schwéier et ass, Qualitéitsprodukter séier a bëlleg ze bauen. Et ass eng Konscht, déi mir heiansdo richteg hunn, an anerer Kéieren zu eppes degeneréiert, wat dem Gesondheetssite vun der Obama-Zäit vun der Regierung ähnelt. Eise Kontrollniveau iwwer dat entstanend Produkt variéiert, an d'Schold fir de Mësserfolleg fält dacks op déi falsch Leit an der Decisiounshierarchie. Dem Microsoft säin Azure DevOps (fréier als Visual Studio Team Services bekannt), trotz kloer gudden Absichten, ass e perfekte Stuerm vu schlechten Decisiounen a schlechter Ausféierung."


### Highlights aus der Hacker-News-Diskussioun

https://news.ycombinator.com/item?id=18983586

"Mir benotzen Azure DevOps ausgiebeg bei mir op der Aarbecht a, nodeems ech GitHub, Gitlab, selbst gehostene Léisungen, Jenkins, TeamCity benotzt hunn... rangéiert Azure DevOps ganz um Schluss."

"D'UI ass iwwerall schrecklech klobig. Am schlëmmste fir mech sinn Pull Requests. Onheemlech schwéier, mat Leit un engem Pull Request ze schaffen. Ech kann Iech net emol op "ee" bestëmmte Problem weisen - fir eis ass et iwwerall futti."

"Azure Devops ass eppes, wat ech gär hunn wëll. D'UI ännert sech ëmmer erëm, behieft awer keng zougrondeliegend Bugs, déi scho laang do sinn."

"D'Tools sinn net gutt integréiert, d'UI ass wierklech lues, et gëtt keng Dashboard-Siicht vun aktive Pull Requests, Builds, Releases, asw. fir meng Lieblingsrepos. D'Build-/Deploy-Zäite si wahnsinneg lues."

"Mir hunn och probéiert, Azure Boards (Work Items, Boards, Backlogs, asw.) ze benotzen. Aua. Et ass e komplette UI-Chaos vun onzesummenhängenden Iddien. Amplaz eng Saach gutt ëmzesetzen, hunn se zwielef Saachen schrecklech ëmgesat."


### Windows Development MVP

Windows Development MVP hei. Ech hunn d'Gefill, datt ech en Deel vun der Verantwortung hei muss droen, well ech net méi haart iwwer dës Problemer geschwat hunn. Awer ech muss soen, ech sinn enttäuscht ze héieren, datt Dir "iwwerrascht" iwwer d'UX-Problemer sidd. Ech soen Ären Leit scho laang, datt d'UX schrecklech ass (z.B. schonn virum Launch) an hunn ëmmer erëm héieren "mir wëssen, mir fixen et". Ech fänken un, d'Feedback ze formaliséieren an duerch d'Päifen ze drécken, bleift drun. Ech sinn och lokal (Bellevue), ech wier gär erakomm, fir ze probéieren, eis relativ einfach OSS-.net/wpf/uwp-App ze pipelinen. Ech vermuden, et wäert fir eis béid eng Aenöffnung sinn.

E puer Beispiller:

* Dir kënnt keng Pipeline mat engem Git-Repo bauen, dee Submodules enthält

* Ech hunn et onméiglech fonnt, de PATH fir e puer eege Tools z'änneren

* D'Erfahrung vun der Neier Pipeline mécht einfach net vill Sënn, nei Benotzer, déi erëmklicken, landen eventuell an de falschen Docs.


### Zesummefaassung vum Edward Thomson (Azure PM)

Ech hunn de Code geschriwwen, dee Är Pull Requests mergt. Program Manager bei Microsoft fir Azure DevOps; fréier Softwareingenieur fir Versiounskontroll-Tools bei GitHub, Microsoft, SourceGear.

https://www.edwardthomson.com/

Co-Maintainer vu libgit2. https://libgit2.github.io

Co-Host vun All Things Git, dem Podcast iwwer Git. https://www.allthingsgit.com/

Kurator vun Developer Tools Weekly, engem Newsletter iwwer Entwécklungstools. https://developertoolsweekly.com/
