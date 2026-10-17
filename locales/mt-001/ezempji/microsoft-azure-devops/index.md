# Microsoft Azure DevOps

Werrej:

* [Sommarju](#sommarju)
  * [Kwistjoni](#kwistjoni)
  * [Deċiżjoni](#deċiżjoni)
  * [Stat](#stat)
* [Dettalji](#dettalji)
  * [Suppożizzjonijiet](#suppożizzjonijiet)
  * [Restrizzjonijiet](#restrizzjonijiet)
  * [Pożizzjonijiet](#pożizzjonijiet)
  * [Argument](#argument)
  * [Implikazzjonijiet](#implikazzjonijiet)
* [Relatati](#relatati)
  * [Deċiżjonijiet relatati](#deċiżjonijiet-relatati)
  * [Rekwiżiti relatati](#rekwiżiti-relatati)
  * [Artefatti relatati](#artefatti-relatati)
  * [Prinċipji relatati](#prinċipji-relatati)
* [Noti](#noti)
  * [Microsoft Devops CI: An Unsatisfying Adventure](#microsoft-devops-ci-an-unsatisfying-adventure)
  * [Twiddijiet ewlenin mid-diskussjoni fuq Hacker News](#twiddijiet-ewlenin-mid-diskussjoni-fuq-hacker-news)
  * [MVP tal-Iżvilupp ta' Windows](#mvp-tal-iżvilupp-ta-windows)
  * [Sommarju minn Edward Thomson (Azure PM)](#sommarju-minn-edward-thomson-azure-pm)


## Sommarju


### Kwistjoni

Irridu nużaw devops biex nibnu, nintegraw, nagħmlu deployment, u nospitaw il-proġetti tagħna. Qed nikkunsidraw Microsoft Azure DevOps.

  * Irridu li l-esperjenza tal-iżviluppatur tkun mgħaġġla u affidabbli, għas-setup tad-devops eż. il-konfigurazzjoni kif ukoll għall-użu kontinwu eż. ħinijiet mgħaġġla tal-bini.
  
  * Irridu nikkunsidraw l-użu ta' Microsoft Azure kollu kemm hu, biex nospitaw l-apps tal-proġett, id-databases, eċċ.


### Deċiżjoni

Iddeċidejna kontra Microsoft Azure DevOps.


### Stat

Deċiż. Miftuħin biex nerġgħu nirrevedu jekk/meta tasal informazzjoni ġdida sinifikanti.


## Dettalji


### Suppożizzjonijiet

Is-suppożizzjonijiet tad-devops l-ordinarji kollha, bħal fil-ktieb Accelerate.

  * Bini mgħaġġel huwa għajnuna sinifikanti. Dan iħaffef iċ-ċikli tal-feedback.

  * Nistgħu nbiddlu biċċiet minn fornituri alternattivi jiġifieri jista' jkun li rridu nġibu servers tal-bini tagħna b'veloċità ogħla, jew nużaw is-sistema tagħna stess tal-kontroll tal-verżjonijiet, jew niskoordinaw ma' server tal-integrazzjoni kontinwa self-hosted.
  
  * Użabbiltà sempliċi hija għajnuna sinifikanti, għall-esperjenza tal-iżviluppatur, u min-naħa tagħha għal oqsma sottili bħall-konsistenza, iċ-ċarezza, is-sigurtà, u l-faċilità tal-kurva tat-tagħlim.

  * Meta xi ħaġa tkun maqsuma jew problematika, irridu mod effettiv biex nirrappurtaw il-kwistjoni. Dan huwa partikolarment importanti għal kwalunkwe kwistjoni relatata mas-sigurtà.


### Restrizzjonijiet

L-ebda waħda magħrufa. Azure għandu impenn ippubblikat li jaħdem tajjeb ma' għodod esterni.


### Pożizzjonijiet

Ikkunsidrajna l-użu ta' Microsoft Azure Devops vs. AWS li huwa l-inkumbent.

Esperimentajna b'Azure DevOps, Azure Pipelines, Azure Repo, u t-twaqqif minn Azure ta' server ġdid permezz ta' Terraform.

Esperimentajna biex niksbu appoġġ minn rappreżentanti ta' Microsoft.

Ġbarna informazzjoni minn kollegi fuq blogs u Hacker News.


### Argument

Azure DevOps jirreklama sett eċċellenti ta' offerti, iżda ma jissodisfawx, ma jaħdmux tajjeb flimkien, u l-appoġġ huwa fqir.

L-esperjenza diretta tagħna:

  * Is-setup ta' Azure huwa taħlita mħawda ta' UIs, li wħud minnhom jingħaqdu ma' kontijiet ta' Microsoft, u oħrajn le. Eż. hemm sign in ta' Azure, sign in ta' Microsoft.com, sign in ta' Live.com, eċċ. u kollha huma fil-logħob fl-istess ħin.

  * Ltqajna ma' kwistjoni żgħira ta' sigurtà waqt is-setup, u ma sibna l-ebda soluzzjoni. Ippruvajna ħafna modi biex nirrappurtawha, lil ħafna rappreżentanti ta' Microsoft, mingħajr suċċess. Irrappurtajnieha b'suċċess lis-sigurtà ta' Microsoft, li wieġbet li mhux se tirranġaha.

  * Id-dokumentazzjoni ħafna drabi hija jew żbaljata jew skaduta. Mill-inqas parti minn dan hija minħabba l-magna tat-tfittxija fqira ta' Microsoft, u parti minnu minħabba SEO inferjuri.
  
  * Is-setup ta' Terraform huwa dokumentat tajjeb, u jaħdem. Madankollu, l-appoġġ ta' Terraform huwa dgħajjef meta mqabbel ma' AWS għax Microsoft qed tibni relazzjonijiet tan-negozju ma' fornituri biex jagħmlu eżempji ta' setup ta' Terraform b'katina.

L-esperjenzi tal-kollegi tagħna:

  * Wara li għamilna l-valutazzjoni tagħna stess mingħajr preġudizzji, fittixna esperjenzi ta' kollegi. Dak li sibna kkonferma l-esperjenzi tagħna.

  * Il-kollegi rrappurtaw problemi addizzjonali bil-ħinijiet tal-bini, u problemi bis-server tal-bini tiegħek stess (bring-your-own-build server). Dawn il-problemi huma ferm aktar severi minn problemi tal-UI, għax it-twettiq tal-bini huwa l-għan ewlieni ta' pipeline tal-bini, u nistennew li nagħmlu ħafna kuljum.

  * Sibna parteċipazzjoni eċċellenti minn kollegi ta' Azure fl-oqsma tad-diskussjoni. Kudos lil Microsoft għal dan. Aħna impressjonati speċjalment minn Edward Thomson, PM u kodifikatur ta' Azure, minħabba l-parteċipazzjoni, id-direttezza, u l-ispjegazzjonijiet tekniċi tiegħu.


### Implikazzjonijiet

L-għażla ta' Microsoft Azure DevOps tidher li x'aktarx tkun aktar għalja (~3x) fil-ħin u fl-ispiża milli ma ngħażlux Azure.


## Relatati


### Deċiżjonijiet relatati

Jekk nagħżlu Azure DevOps, hemm ħafna offerti relatati, inklużi Azure Repo, Azure Pipeline, eċċ. Aħna nemmnu li jekk nagħżlu Azure Devops, dan jista' jagħmilha eħfef biex nużaw aktar kapaċitajiet ta' Azure, jew jista' jagħmilha aktar diffiċli biex nużaw kapaċitajiet ta' fornituri oħra.

Aħna nemmnu li Microsoft qed tagħmel passi kbar fl-esperjenza tal-iżviluppatur, u naraw lil Microsoft tagħmel akkwisti kbar ta' għodod tal-iżviluppaturi (eż. GitHub) u dipendenzi (eż. Citus).

Jekk nagħżlu Azure DevOps, allura jista' jkun li rridu nenfasizzaw l-għażla tal-offerti akkwistati minn Microsoft, u jista' jkun ukoll li rridu nersqu lejn l-offerti akkwistati b'aktar kawtela/valutazzjoni minħabba riġett potenzjali tat-tessut eż. riskju ta' tibdil tal-persunal.


### Rekwiżiti relatati

Irridu ħinijiet tal-bini mgħaġġla ħafna. Aħna nirrikonoxxu li nħallsu primjum għoli għal dan. Dan għax irridu nirripetu malajr ħafna.

Irridu affidabbiltà għolja ħafna. Aħna nirrikonoxxu li nħallsu primjum għoli għal dan. Dan għax qed nittestjaw każijiet ta' użu ta' valur għoli, inklużi tranżazzjonijiet finanzjarji, tranżazzjonijiet kunfidenzjali, eċċ.

L-aqwa 4 KPIs tagħna tad-devops jinkludu l-ħin medju ta' rkupru, li jirrikjedi bini mgħaġġel u affidabbiltà għolja.


### Artefatti relatati

Irridu li s-sistema tal-bini toħroġ artefatti adattati biex jintużaw f'sistemi oħra, bħal Artifactory.


### Prinċipji relatati

Faċilment riversibbli. Nistgħu nevalwaw Azure DevOps b'mod parallel ma' AWS l-inkumbent.


## Noti


### Microsoft Devops CI: An Unsatisfying Adventure

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Post tal-blog.

"Bħala żviluppatur tas-software, naf minn tajjeb kemm huwa diffiċli li jinbnew prodotti ta' kwalità malajr u bi prezz baxx. Hija forma ta' arti li xi drabi nirnexxu fiha, u drabi oħra tiddegenera f'xi ħaġa simili għas-sit tal-gvern tal-kura tas-saħħa tal-era ta' Obama. Il-livell ta' kontroll tagħna fuq il-prodott li jirriżulta jvarja, u t-tort għall-falliment spiss jaqa' fuq in-nies ħżiena fil-ġerarkija tat-teħid tad-deċiżjonijiet. Azure DevOps ta' Microsoft (magħruf qabel bħala Visual Studio Team Services), minkejja intenzjonijiet ċari tajbin, huwa maltempata perfetta ta' deċiżjonijiet ħżiena u eżekuzzjoni fqira."


### Twiddijiet ewlenin mid-diskussjoni fuq Hacker News

https://news.ycombinator.com/item?id=18983586

"Nużaw Azure DevOps b'mod estensiv fix-xogħol tiegħi u, wara li użajt GitHub, Gitlab, soluzzjonijiet self-hosted, Jenkins, TeamCity... Azure DevOps jiġi l-aħħar nett."

"L-UI hija terribbilment goffa kullimkien. L-agħar għalija huma l-pull requests. Inkredibbilment diffiċli li taħdem man-nies fuq pull request. Ma nistax anke nurik problema partikolari waħda - għalina huwa maqsum kullimkien."

"Azure Devops huwa xi ħaġa li rrid inħobb. L-UI tibqa' tinbidel, imma ma tirranġax il-bugs sottostanti li ilhom hemm għal żmien twil."

"L-għodod mhumiex integrati tajjeb, l-UI hija tassew bil-mod, m'hemm l-ebda veduta tad-dashboard ta' pull requests attivi, bini, releases, eċċ għar-repos favoriti tiegħi. Il-ħinijiet tal-Bini/Deployment huma bil-mod b'mod insan."

"Ippruvajna nużaw ukoll Azure Boards (Work Items, Boards, Backlogs, eċċ). Ouch. Hija taħlita kompleta ta' UI ta' ideat diżgħaqdin. Minflok ma implimentaw ħaġa waħda sew, implimentaw tużżana affarijiet b'mod terribbli."


### MVP tal-Iżvilupp ta' Windows

Windows Development MVP hawnhekk. Inħoss li għandi nerfa' parti mir-responsabbiltà hawnhekk talli ma kontx aktar għoli dwar dawn il-kwistjonijiet. Imma għandi ngħid, huwa diżappuntanti li nisma' li int "sorpriż" bil-kwistjonijiet tal-UX. Ilni ngħid lin-nies tiegħek li l-UX hija tal-biża' (eż. sa mill-qabel it-tnedija) u kont nibqa' nisma' lura "nafu, qed nirranġawha". Se nibda nifformalizza l-feedback u nibgħatu permezz tal-pipes, żomm għajnejk miftuħa. Jien lokali wkoll (Bellevue), nixtieq nidħol u nipprova nagħmel pipeline tal-app tagħna oss .net/wpf/uwp relattivament sempliċi. Nissuspetta li se tkun ħaġa li tiftħilna għajnejna t-tnejn.

Xi eżempji:

* Ma tistax tibni pipeline b'git repo li fih submodules

* Sibt impossibbli li nbiddel il-PATH għal xi għodod personalizzati

* L-esperjenza tal-Pipeline Ġdida sempliċement ma tagħmilx wisq sens, l-utenti ġodda li jikklikkjaw madwar eventwalment jispiċċaw fid-Docs ħżiena.


### Sommarju minn Edward Thomson (Azure PM)

Jien kitibt il-kodiċi li jgħaqqad il-pull requests tiegħek. Program Manager f'Microsoft għal Azure DevOps; qabel inġinier tas-software fuq għodod tal-kontroll tal-verżjonijiet f'GitHub, Microsoft, SourceGear.

https://www.edwardthomson.com/

Ko-manutentur ta' libgit2. https://libgit2.github.io

Ko-ospitant ta' All Things Git, il-Podcast dwar Git. https://www.allthingsgit.com/

Kurator ta' Developer Tools Weekly, newsletter dwar għodod tal-iżvilupp. https://developertoolsweekly.com/
