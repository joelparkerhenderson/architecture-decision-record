# Architektur-Decisiounsopzeechnung (ADR)

Eng Architektur-Decisiounsopzeechnung (ADR) ass en Dokument, dat eng wichteg Architekturdecisioun zesumme mat hirem Kontext a séng Konsequenzen festhält.

> [!IMPORTANT]
> Maacht Är eege Due Diligence fir dës Ressourcen, ier Dir se a kriteschen Systemer benotzt.

Inhalt:

- [Wat ass eng Architektur-Decisiounsopzeechnung?](#wat-ass-eng-architektur-decisiounsopzeechnung)
- [Wéi een mat ADR ufänkt](#wéi-een-mat-adr-ufänkt)
- [Wéi een mat ADR a Verbindung mat Toole ufänkt](#wéi-een-mat-adr-a-verbindung-mat-toole-ufänkt)
- [Wéi een mat ADR a Verbindung mat Git ufänkt](#wéi-een-mat-adr-a-verbindung-mat-git-ufänkt)
- [Claude-Code-Skills fir ADR](#claude-code-skills-fir-adr)
- [Konventioune fir Dateinimm vun ADR](#konventioune-fir-dateinimm-vun-adr)
- [Virschléi fir gutt ADR ze schreiwen](#virschléi-fir-gutt-adr-ze-schreiwen)
- [ADR-Beispillvirlagen](#adr-beispillvirlagen)
- [Rotschléi fir d'Teamaarbecht bei ADR](#rotschléi-fir-dteamaarbecht-bei-adr)
- [Froen zur Teamaarbecht bei ADR](#froen-zur-teamaarbecht-bei-adr)
- [Next-Step-Konzepter fir ADR](#next-step-konzepter-fir-adr)
- [Architekturdiagrammer & Siichten & Perspektiven](#architekturdiagrammer--siichten--perspektiven)
- [Fitness-Funktioune fir Decisiounen als Code](#fitness-funktioune-fir-decisiounen-als-code)
- [Decisiounsleitplanken fir Pull Requests](#decisiounsleitplanken-fir-pull-requests)
- [Fir méi Informatiounen](#fir-méi-informatiounen)

Virlagen:

- [Virlag fir Decisiounsopzeechnung vum Jeff Tyree an Art Akerman](virlagen/virlag-fir-decisiounsopzeechnung-vum-jeff-tyree-an-art-akerman/)
- [Virlag fir Decisiounsopzeechnung vum Michael Nygard](virlagen/virlag-fir-decisiounsopzeechnung-vum-michael-nygard/)
- [Virlag fir Decisiounsopzeechnung vun EdgeX](virlagen/virlag-fir-decisiounsopzeechnung-vun-edgex/)
- [Virlag fir Decisiounsopzeechnung vun arc42](virlagen/virlag-fir-decisiounsopzeechnung-vun-arc42/)
- [Virlag fir Decisiounsopzeechnung fir Alexandrian-Muster](virlagen/virlag-fir-decisiounsopzeechnung-fir-alexandrian-muster/)
- [Virlag fir Decisiounsopzeechnung fir e Business Case](virlagen/virlag-fir-decisiounsopzeechnung-fir-en-business-case/)
- [Virlag fir Decisiounsopzeechnung vum MADR-Projet](virlagen/virlag-fir-decisiounsopzeechnung-vum-madr-projet/)
- [Virlag fir Decisiounsopzeechnung mat Planguage](virlagen/virlag-fir-decisiounsopzeechnung-mat-planguage/)
- [Virlag fir Decisiounsopzeechnung vum Paulo Merson](https://github.com/pmerson/ADR-template)
- [Virlag fir Decisiounsopzeechnung vum Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Virlag fir Decisiounsopzeechnung vum Gareth Morgan](virlagen/virlag-fir-decisiounsopzeechnung-vum-gareth-morgan/)
- [Virlag fir Decisiounsopzeechnung vu GIG Cymru NHS Wales](virlagen/virlag-fir-decisiounsopzeechnung-vu-gig-cymru-nhs-wales/)
- [Virlag fir Decisiounsopzeechnung fir Wichteg Technesch Decisiounen (ITDs) vum Ignacio Larrañaga](virlagen/virlag-fir-decisiounsopzeechnung-fir-wichteg-technesch-decisiounen/)

Beispiller:

- [Framework fir CSS](beispiller/framework-fir-css/)
- [Konfiguratioun vun Emgebungsvariabelen](beispiller/konfiguratioun-vun-emgebungsvariabelen/)
- [Metriken, Monitoren, Alarmer](beispiller/metriken-monitoren-alarmer/)
- [Microsoft Azure DevOps](beispiller/microsoft-azure-devops/)
- [Monorepo oder Multirepo](beispiller/monorepo-oder-multirepo/)
- [Programméiersproochen](beispiller/programmeiersproochen/)
- [Späicherung vu Geheimnisser](beispiller/speicherung-vu-geheimnisser/)
- [Zäitstempel-Format](beispiller/zaitstempel-format/)
- [Vill méi...](beispiller/)

## Wat ass eng Architektur-Decisiounsopzeechnung?

Eng **Architektur-Decisiounsopzeechnung** (ADR) ass en Dokument, dat eng wichteg Architekturdecisioun zesumme mat hirem Kontext a séng Konsequenzen festhält.

Eng **Architekturdecisioun** (AD) ass eng Entscheedung am Softwaredesign, déi eng wesentlech Ufuerderung adresséiert.

E **Architekturdecisiounsprotokoll** (ADL) ass d'Sammlung vun alle ADR, déi fir e bestëmmte Projet (oder eng Organisatioun) erstallt a gepflegt ginn.

Eng **architekturrelevant Ufuerderung** (ASR) ass eng Ufuerderung, déi e messbaren Effekt op d'Architektur vun engem Softwaresystem huet.

Dat alles gehéiert zum Thema **Architekturwëssensmanagement** (AKM).

D'Zil vun dësem Dokument ass et, e séieren Iwwerbléck iwwer ADR ze ginn, wéi een se erstellt, a wou een méi Informatioune fënnt.

Ofkierzungen:

  * **AD**: Architekturdecisioun

  * **ADL**: Architekturdecisiounsprotokoll

  * **ADR**: Architektur-Decisiounsopzeechnung

  * **AKM**: Architekturwëssensmanagement

  * **ASR**: architekturrelevant Ufuerderung

## Wéi een mat ADR ufänkt

Fir mat ADR unzefänken, schwätzt mat Ären Teamkollegen iwwer dës Beräicher.

Decisiounsidentifikatioun:

  * Wéi dringend a wéi wichteg ass d'AD?

  * Muss si elo geholl ginn, oder kann se waarden, bis méi bekannt ass?

  * Souwuel perséinlech a kollektiv Erfahrung wéi och unerkannt Designmethoden a -praktike kënnen d'Identifikatioun vun Decisioune ënnerstëtzen.

  * Am Idealfall féiert een eng Decisiounslëscht, déi d'Produktlëscht ergänzt.

Decisiounsfannung:

  * Et gëtt eng Rei Techniken zur Decisiounsfannung, souwuel allgemeng wéi och speziell fir Softwarearchitektur, zum Beispill Dialogue Mapping.

  * D'Decisiounsfannung a Gruppen ass en aktivt Fuerschungsthema.

Duerchsetzung an Ëmsetzung vun Decisiounen:

  * AD ginn am Softwaredesign benotzt; dofir musse si de Stakeholder vum System, déi et finanzéieren, entwéckelen an bedreiwen, matgedeelt a vun hinnen akzeptéiert ginn.

  * Architektonesch evident Coding-Stiler a Code-Reviews, déi sech op Architekturthemen an -decisiounen konzentréieren, sinn zwou verwandte Praktiken.

  * AD musse bei der Moderniséierung vun engem Softwaresystem an der Softwareevolutioun och nei ënnersicht ginn.

Decisiounen deelen (optional):

  * Vill AD widderhuele sech a Projeten.

  * Dofir kënnen Erfahrungen mat fréieren Decisiounen, gutt wéi schlecht, wäertvoll wiederverwendbar Ressource sinn, wann ee mat enger explizitter Wëssensmanagement-Strategie schafft.

Decisiounsdokumentatioun:

  * Et gëtt vill Virlagen an Tools fir Decisiounen z'erfaassen.

  * Kuckt déi agil Gemeinschaften, z.B. d'ADR vum M. Nygard.

  * Kuckt traditionell Prozesser vun der Softwareentwécklung a vum Architekturdesign, z.B. Tabelleformater, déi vum IBM UMF a vum Tyree an Akerman vu CapitalOne virgeschloe ginn.

Fir méi:

  * Dës Schrëtt sinn aus dem Wikipedia-Artikel iwwer [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision) iwwerholl

## Wéi een mat ADR a Verbindung mat Toole ufänkt

- [MySpec](https://myspec.dev) — Automatiséiert Spezifikatiouns- an Architekturdecisiounsplattform, déi d'Projetskonstitutioun, déi technesch Architektur an d'ADR a proppert Markdown strukturéiert, dat iwwer MCP zur Verfügung gestallt gëtt.

Dir kënnt ADR mat Toole sou benotzen, wéi et Iech gefält.

Zum Beispill:

  * Wann Dir gär Google Drive an Online-Editéiere benotzt, kënnt Dir en Google Doc oder e Google Sheet erstellen.

  * Wann Dir gär Quellcode-Versiounskontroll benotzt, wéi Git, kënnt Dir fir all ADR eng Datei erstellen.

  * Wann Dir gär Projetsplanungstools benotzt, wéi Atlassian Jira, kënnt Dir den Planungs-Tracker vum Tool benotzen.

  * Wann Dir gär Wikien benotzt, wéi MediaWiki, kënnt Dir e Wiki fir ADR erstellen.

## Wéi een mat ADR a Verbindung mat Git ufänkt

Wann Dir gär Git-Versiounskontroll benotzt, hei ass, wéi mir gär mat ADR a Verbindung mat Git fir en typesche Softwareprojet mat Quellcode ufänken.

Erstellt en Verzeechnes fir d'ADR-Dateien:

```sh
$ mkdir adr
```

Erstellt fir all ADR eng Textdatei, zum Beispill `choose-database.md`:

```sh
$ vi choose-database.md
```

Schreift an den ADR alles, wat Dir wëllt. Kuckt d'Virlagen an dësem Repository fir Iddien.

Committed den ADR an Äre Git-Repo.

## Claude-Code-Skills fir ADR

Dëse Repository liwwert zwee [Claude Code](https://claude.com/claude-code)-Skills ënner [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), sou datt en AI-Coding-Agent ADR esou schreiwe an erhale kann, wéi dëse Projet et recommandéiert:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — allgemeng, fir jiddereen, deen en ADR a irgendengem Projet schreift. Hëlleft ze entscheeden, ob eng Decisioun en ADR brauch, riicht e Verzeechnes `adr/` oder `decisions/` an, benennt d'Datei, wielt e Virlag aus den eelef matgelifferte Skeletter a schreift solid Kontext-/Decisioun-/Konsequenzen-Rubriken.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — speziell fir d'Maintainer vun dësem Repository. Dokumentéiert d'Layout vum Repository, d'Konventioun fir d'Spigelung vu README/Locales an déi exakt Schrëtt, fir en neie Virlag, e Beispill oder en Tool-Link derbäizesetzen.

Fir e Skill ze benotzen, kopéiert säin Dossier an `.claude/skills/` an der Wuerzel vum Repository, an deem Dir schafft (oder an `~/.claude/skills/`, fir en a jidde Projet verfügbar ze maachen), a freet dann Claude Code, en ADR ze schreiwen oder ze iwwerpréiwen.

## Konventioune fir Dateinimm vun ADR

Wann Dir Är ADR mat typeschen Textdateie wëllt erstellen, wëllt Dir vläicht Är eege Konventioun fir d'Dateinimm vun ADR festleeën.

Mir bevirzugen eng Konventioun fir Dateinimm, déi e spezifescht Format huet.

Beispiller:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Eis Konventioun fir Dateinimm:

  * Den Numm huet e Verbausdrock am Imperativ am Präsens. Dat hëlleft der Liesbarkeet a passt zu eisem Format fir Commit-Messagen.

  * Den Numm benotzt Klengbuschtawen a Bindestrécher (wéi an dësem Repo). Dat ass e Gläichgewiicht tëscht Liesbarkeet a Benotzbarkeet vum System.

  * D'Extensioun ass Markdown. Dat kann nëtzlech si fir einfach Formatéierung.

## Virschléi fir gutt ADR ze schreiwen

Charakteristike vun engem gudden ADR:

* Begrënnung: Erkläert d'Grënn, firwat déi bestëmmten AD geholl gëtt. Dat kann de Kontext (kuckt ënnen), Virdeeler an Nodeeler vu verschiddene méigleche Choixen, Featurevergläicher, Käschten-/Notze-Diskussiounen a méi enthalen.

* Spezifesch: All ADR soll iwwer eng AD goen, net iwwer méi AD.

* Zäitstempel: Haalt fest, wéini all Element am ADR geschriwwe gouf. Dat ass besonnesch wichteg fir Aspekter, déi sech mat der Zäit kënne änneren, wéi Käschten, Zäitplang, Skaléierung an Ähnleches.

* Onverännerbar: Ännert keng bestoend Informatioun an engem ADR. Amplaz ergänzt den ADR mat neier Informatioun, oder léist den ADR duerch en neien ADR of.

Charakteristike vun enger gudder "Kontext"-Rubrik an engem ADR:

* Erkläert d'Situatioun vun Ärer Organisatioun an d'Geschäftsprioritéiten.

* Bezitt Begrënnungen an Iwwerleeungen mat an, déi op der sozialer a kompetenzbaséierter Zesummesetzung vun Ären Teams baséieren.

* Bezitt Pro- a Kontra-Argumenter mat an, déi relevant sinn, a beschreift se esou, datt se zu Äre Bedürfnisser an Zieler passen.

Charakteristike vun enger gudder "Konsequenzen"-Rubrik an engem ADR:

* Erkläert, wat aus der Decisioun follegt. Dat kann d'Effekter, d'Resultater, d'Outputs, d'Follow-ups a méi enthalen.

* Bezitt Informatioune iwwer all nofollgend ADR mat an. Et ass relativ üblech, datt een ADR de Besoin u weidere ADR ausléist, zum Beispill wann een ADR eng grouss iwwergräifend Wiel mécht, déi dann de Besoin u méi klenge Decisiounen erstellt.

* Bezitt all Review-Prozesser nom Handelen mat an. Et ass typesch, datt Teams all ADR een Mount méi spéit nokucken, fir d'ADR-Informatioun mat deem ze vergläichen, wat an der Praxis geschitt ass, fir ze léieren an ze wuessen.

E neien ADR ka vun engem fréiere ADR iwwerholl:

* Wann eng AD geholl gëtt, déi e fréiere ADR ersetzt oder ongëlteg mécht, da soll en neien ADR erstallt ginn

## ADR-Beispillvirlagen

ADR-Beispillvirlagen, déi mir am Netz gesammelt hunn:

- [ADR-Virlag vum Michael Nygard](virlagen/virlag-fir-decisiounsopzeechnung-vum-michael-nygard/) (einfach a populär)

- [ADR-Virlag vum Jeff Tyree an Art Akerman](virlagen/virlag-fir-decisiounsopzeechnung-vum-jeff-tyree-an-art-akerman/) (méi raffinéiert)

- [ADR-Virlag fir Alexandrian-Muster](virlagen/virlag-fir-decisiounsopzeechnung-fir-alexandrian-muster/) (einfach mat Kontextspezifika)

- [ADR-Virlag fir e Business Case](virlagen/virlag-fir-decisiounsopzeechnung-fir-en-business-case/) (méi MBA-orientéiert, mat Käschten, SWOT a méi Meenungen)

- [ADR-Virlag vum Markdown-Any-Decision-Records-(MADR)-Projet](virlagen/virlag-fir-decisiounsopzeechnung-vum-madr-projet/) (souwuel einfach wéi och ausgeschafte Versioun; déi lescht betount Optiounen an hir Pros a Cons)

- [ADR-Virlag mat Planguage](virlagen/virlag-fir-decisiounsopzeechnung-mat-planguage/) (méi Qualitéitssécherungs-orientéiert)

- [Virlag fir Wichteg Technesch Decisiounen (ITDs) vum Ignacio Larrañaga](virlagen/virlag-fir-decisiounsopzeechnung-fir-wichteg-technesch-decisiounen/) (schlank an decisiounsorientéiert, optiméiert fir séier Review duerch d'Geschäftsleedung)

## Rotschléi fir d'Teamaarbecht bei ADR

Wann Dir iwwerleet, Decisiounsopzeechnungen an Ärem Team ze benotzen, hei sinn e puer Rotschléi, déi mir duerch d'Zesummenaarbecht mat ville Teams geléiert hunn.

Dir hutt d'Chance, Är Teamkollegen ze féieren, andeems Dir zesummen iwwer d'"Firwat" schwätzt, amplaz d'"Wat" virzeschreiwen. Zum Beispill sinn Decisiounsopzeechnungen e Wee fir Teams, intelligenter ze denken a besser ze kommunizéieren; Decisiounsopzeechnunge si wäertlos, wann se just eng nodréiglech erzwongen Pabeierfuerderung sinn.

E puer Teams bevirzugen den Numm "Decisiounen" däitlech virun der Ofkierzung "ADR". Wann e puer Teams de Verzeechnesnumm "decisions" benotzen, ass et wéi wann e Luucht usgeet, an d'Team fänkt un, méi Informatioun an d'Verzeechnes ze setzen, wéi Decisioune vu Lieferanten, Planungsdecisiounen, Terminplanungsdecisiounen, asw. All dës Zorte vun Informatioun kënnen dee selwechte Virlag benotzen. Mir stellen d'Hypothees op, datt d'Leit méi séier mat Wierder ("Decisiounen") léieren wéi mat Ofkierzungen ("ADR"), datt d'Leit méi motivéiert sinn, Dokumenter iwwer Aarbecht am Gaang ze schreiwen, wann d'Wuert "Opzeechnung" ewechfält, an datt e puer Entwéckler an e puer Manager d'Wuert "Architektur" net gär hunn.

An der Theorie ass Onverännerbarkeet ideal. An der Praxis huet Verännerbarkeet fir eis Teams besser geschafft. Mir setzen déi nei Informatioun an den bestoenden ADR an, mat engem Datumsstempel an enger Notiz, datt d'Informatioun no der Decisioun ukomm ass. Sou en Usaz féiert zu engem "liewegen Dokument", dat mir all aktualiséiere kënnen. Typesch Aktualiséierunge geschéien, wa mir Informatioun duerch nei Teamkollegen, nei Offeren, reell Resultater aus eiser Notzung, oder nodréiglech Ännerunge vun Drëttpartnere kréien, wéi Fäegkeete vu Lieferanten, Präispläng, Lizenzvereinbarungen, asw.

## Froen zur Teamaarbecht bei ADR


### Wien kann en ADR erstellen?

Berécksiichtegt Beräicher wéi spezifesch Persounen, spezifesch Rollen, spezifesch Teams oder spezifesch Departementer; berécksiichtegt och, ob et Persounen, Rollen, Teams oder Departementer gëtt, déi en ADR a Optrag ginn kënnen, dat heescht, si froen een un, deen een anere schreift. 

Beispillantwert: All Persoun an eiser Organisatioun, déi d'README-Säit vun der Architektur-Decisiounsopzeechnung gelies huet, kann en ADR virschloen, dat heescht, d'Persoun ka mat der Schreiwen ufänken an en dem Team matdeelen.

### Wat rechtfäerdegt et, en ADR unzeleeën?

Berécksiichtegt Beräicher wéi d'Aarbechtsweisen vun Ärer Organisatioun an Teams, d'Struktur vun Ärem Softwaresystem, d'Koordinatioun tëscht Teams, laangfristeg Wartbarkeet, extern Schnëttstellen, wiem Dir wëllt notzen, an Ähnleches. 

Beispillantwert: Mir wëllen en ADR erstellen, wa mir wëllen, datt zukünfteg Entwéckler d'"Firwat" vun deem verstoen, wat mir maachen.

### Wat rechtfäerdegt et, keen ADR unzeleeën?

Berécksiichtegt Beräicher wéi Decisiounen, déi net d'Architektur betreffen, oder winzeg sinn, zum Beispill mat minimalem Risiko oder selbststänneg oder fir en eenzegen Entwéckler, oder schonn anzwuesch voll ofgedeckt sinn, zum Beispill duerch Standarden oder Politiken oder Dokumentatioun, oder temporär sinn, zum Beispill Workarounds oder Proofs of Concept oder Experimenter. 

Beispillantwert: Mir wëllen en ADR iwwersprangen, wann eng Decisioun a Géigewier vun Ëmfang, Zäit, Risiko a Käschte limitéiert ass, oder schonn anzwuesch ofgedeckt ass.

### Wat ass de Lifecycle vun engem ADR?

Berécksiichtegt Beräicher wéi de Prozess vun der Erstellung, d'Recherche, de Prozess vun der Decisiounsfannung, d'Ëmsetzung an d'Ausleeë vun engem ADR. Berécksiichtegt, wéi de Lifecycle vum ADR mat der Zäit verfollegt gëtt, zum Beispill wéi de ADR vun engem Zoustand an deen nächsten bewegt gëtt, an och wéi dat de Stakeholder matgedeelt gëtt. 

Beispillantwert: Mir wëllen, datt en ADR fënnef Lifecycle-Stadie huet: Initiéieren → Recherchéieren → Evaluéieren → Ëmsetzen → Erhalen → Ausleeën.

### Wat sinn d'Critèrë fir d'Lifecycle-Schrëtt vun engem ADR?

Berécksiichtegt Beräicher wéi Akzeptanzcritèrë fir en ADR, dat heescht, wéi weess een, datt en gutt genuch ass, fir vun engem Lifecycle-Schrëtt an deen nächsten ze goen? Ass de Problem kloer formuléiert? Goufen d'Alternative berécksiichtegt? Sinn d'Kompromësser gutt genuch verstanen an dokumentéiert?
Ass de ganze relevante Kontext do? Sinn all relevant Stakeholder involvéiert? Gouf all Feedback agebaut? 

Beispillantwert: Mir wëllen, datt iwwer en ADR vun de Stakeholder ofgestëmmt gëtt, wann dat aktivt Team 1) seng Recherche ofgeschloss huet, 2) seng Evaluatioun ofgeschloss huet, 3) de Virschlag fir den ADR de Stakeholder mat enger Ufro fir Kommentare an enger Zäitbegrenzung vun enger Woch publizéiert huet, 4) all Kommentare vun de Stakeholder agebaut an adresséiert goufen.

### Wéi eng Rolle a Verantwortlechkeeten interagéieren mat engem ADR?

Berécksiichtegt Rolle wéi Virschloender, Recherchéierer, Evaluator, Reviewer, Genehmegen, Maintainer an Ähnleches. Berécksiichtegt Verantwortlechkeeten wéi d'Kommunikatioun mat de Stakeholder, d'Gewährleeschtung, datt Erwaardunge erfëllt ginn, d'Deele vum Dokument um Site oder Intranet, an d'periodesch Iwwerpréiwung vun der Aarbecht, besonnesch wann relevant Ännerunge geschéien.

Beispillantwert: Mir wëllen, datt all ADR ëmmer eng primär Kontaktpersoun, eng sekundär Kontaktpersoun an en responsabelt Team huet; dës sinn zoustänneg fir Kommunikatiounen, Publikatiounen, Erhalung, periodesch Iwwerpréiwung op d'mannst eemol d'Joer, an eventuell Ausleeë wéi néideg.

### Wéi interagéiert d'Governance mat engem ADR?

Berécksiichtegt Beräicher wéi d'Aarbechtsweise vun Ärer Organisatioun, speziell Compliance-Besoinen, zum Beispill fir juristesch Aspekter oder Personalaspekter, wéi Dir mat Konsens versus Konflikt versus Eskalatioun wëllt ëmgoen. Gëtt et Beräicher oder Persoune oder Teams, déi méi Afloss wéi anerer op en ADR kënne hunn, zum Beispill en genehmege kënnen, doriwwer ofstëmme kënnen oder en Veto asetze kënnen?

Beispillantwert: D'Governance vun engem ADR ass an dëser Prioritéitsuerdnung: de CEO, de CTO, de CLO, d'Team, dat en ADR ëmsetzt, d'Expert am Team, déi sech am beschten mat der AD auskennen. Keen anere huet Governance, ausser et ass am ADR beschriwwen. 

### Wéi eng Prinzipie interagéieren mat engem ADR?

Berécksiichtegt Beräicher wéi d'Aarbechtsweise vun Ärer Organisatioun, déi schnell Beweegung versus lues Beweegung enthalen, fir Decisiounskonsens versus Decisiounskonflikt, a fir Risikopräferenzen versus Sécherheetspräferenzen, ëffentlech Diskussioun versus privat Diskussioun an Ähnleches.

Beispillantwert: Mir benotzen d'Leadership-Prinzipie vum Bias for Action, Disagree-and-Commit, 70%-Schätzunge si gutt genuch fir einfach réckgängeg ze maachen an einfach isoléierbar Decisiounen, an ëffentlech Aarbechtsweisen mat der Ausnam vu vertraulecher Informatioun, wéi se an der Vertraulechkeetsvereinbarung vun eiser Organisatioun beschriwwen ass.

## Next-Step-Konzepter fir ADR

[Arc42](https://arc42.org/) beäntwert zwou Froen op pragmatesch Aart a Weis a kann un Är spezifesch Bedierfnisser ugepasst ginn. Wat soll een iwwer seng Architektur dokumentéieren/kommunizéieren? Wéi soll een dokumentéieren/kommunizéieren? Arc42 enthält Architektur-Decisiounsopzeechnungen plus Guidance zu Zieler, Restriktiounen, Kontexter, Qualitéit, Risiken a méi.

[D'C4-Modell](https://c4model.com/) ass en einfach ze léiere, entwécklerfrëndlechen Usaz fir Diagrammer vun der Softwarearchitektur. C4 ass e Set vun hierarchesche Diagrammer fir Kontext, Container, Komponenten, Code, plus ënnerstëtzend Diagrammer fir Systemlandschaft, Dynamik an Deployment.

## Architekturdiagrammer & Siichten & Perspektiven

Eng Architekturdiagramm gëtt "Architektursiicht" genannt.

Eng "Architektursiicht" ass eng Instanz vun enger "Architekturperspektiv".

Eng "Architekturperspektiv" huet e spezifescht Publikum mat spezifesche Bedenken am A.

Beispiller fir Architekturperspektiven, Siichten an Diagrammer:

- Geschäftsfäegkeeten (Business Capabilities)

- Héichniveau-Geschäftsprozesser

- [Value Streams](https://en.wikipedia.org/wiki/Value_stream)

- Softwarefunktiounen, op Applikatiounskomponenten gemappt

- [C4-Modell](https://en.wikipedia.org/wiki/C4_model)-Kontextdiagramm (TO-BE / AS-IS)

- [C4-Modell](https://en.wikipedia.org/wiki/C4_model)-Containerdiagramm (TO-BE / AS-IS)

- [Entity-Relationship-Diagramm](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD), fir Datenentitéiten op Applikatiounskomponenten ze mappen

- [Sequenzdiagrammer](https://en.wikipedia.org/wiki/Sequence_diagram), fir funktionell Flëss bannent Systemer a fir Integratiounen ze beschreiwen

- [Business-Process-Model-and-Notation-(BPMN)](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation)-Diagrammer, fir Datenflëss iwwer Applikatiounskomponenten ze beschreiwen

- [Business-Process-Model-and-Notation-(BPMN)](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation)-Diagrammer, fir Geschäftsprozesser / Benotzerszenarien ze beschreiwen

- [Identity-and-Access-Management-(IAM)](https://en.wikipedia.org/wiki/Identity_and_access_management)-Diagrammer

- [Role-Based-Access-Control-(RBAC)](https://en.wikipedia.org/wiki/Role-based_access_control)-Diagrammer mat Rollen pro Applikatiounskomponent

- [Attribute-Based-Access-Control-(ABAC)](https://en.wikipedia.org/wiki/Attribute-based_access_control)-Diagrammer mat Attributer pro Applikatiounskomponent

- Dateschutzdiagrammer

Verwandt Diagrammer:

- E Use-Case-Diagramm weist Use Cases fir d'Management/d'Clienten, wat virun den Ufuerderungen kënnt, déi virun der Softwarearchitektur kommen.

- E Deployment-Diagramm weist déi physesch Hardware/Computeren, op déi d'Softwarekomponente deployt ginn.
- E Datefluss-Diagramm weist, wéi Daten duerch de System beweegt a transforméiert ginn.
- E Sequenzdiagramm gëtt benotzt, fir ze weisen, wéi Protokoller wéi HTTP op enger Zäitachs funktionéieren.

- Eng Aktivitéitsdiagramm weist de Workflow vun Aktivitéiten, déi e Softwaresystem ënnerhëlt, wéi eng NPC-AI.

## Fitness-Funktioune fir Decisiounen als Code

Fitness-Funktioune si objektiv automatiséiert Kontrollen, mat Programméiercode geschriwwen, déi verifizéieren, datt Decisiounen agehale ginn.

- Fitness-Funktioune maachen Decisiounen testbar a sécherstellbar.

- Fitness-Funktioune fir Decisioune kënnen d'Qualitéitssécherung, regulatoresch Prozesser a Governance-Zieler staark ënnerstëtzen.

### Wéi Fitness-Funktioune mat Decisiounen zesummenhänken

Eng Decisiounsopzeechnung dokumentéiert d'Decisioun, während eng Fitness-Funktioun d'Decisioun sécherstellt.

- Beispilldecisioun: Mir benotzen Event Sourcing fir Audit-Ufuerderungen.

- Beispill fir eng Fitness-Funktioun: Mir benotzen de Continuous-Integration-Server, fir ze testen, datt all Zoustandsännerung Evenementer muss produzéieren.

### Firwat Fitness-Funktioune Decisioune hëllefen

Objektiv Miessungen: Fitness-Funktioune bestinn oder falen duerch, sou datt d'Aarbecht sichtbar a kloer ass.

Kontinuéierlech Notzung: Fitness-Funktioune sinn Är liewege Reegelen, déi bei all Commit a Build lafen.

Vertrauen fir Refactoring: Fitness-Funktioune fänken automatesch Feeler géint Decisiounsreegele op.

Skaléierbar Governance: Fitness-Funktioune sécheren Standarden of, ouni Flaschenhälser ze schafen.

### Kënnen Fitness-Funktioune AI benotzen?

Fitness-Funktioune kënnen AI-LLMs fir Decisiounen notzen, andeems si Froe fir Är Aarbecht stellen,
zum Beispill fir Är Pläng, Code, Schemaen, APIen a méi:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Unit-Testen vun der Architektur

[ArchUnit](https://www.archunit.org/): Architekturreegele vu Java-Code mat all ganz normalem Java-Unit-Test-Framework iwwerpréiwen.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): Architekturreegele vun TypeScript-Code a JavaScript-Code mat Jest, Vitest, Jasmine, asw. iwwerpréiwen.

## Decisiounsleitplanken fir Pull Requests

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
bréngt automatesch déi richteg Decisiounsopzeechnungen zum richtege Moment un d'Uewerfläch — wann
en Entwéckler aktiv de Code ännert, dee vun dësen Decisioune betraff ass. Amplaz
drop ze hoffen, datt Entwéckler en Dokumenteverzeechnes liesen, ier si mergen, erscheint de relevante
Kontext direkt um Pull Request.

Dat funktionéiert fir all Zort vun Decisiounsopzeechnung: Architekturdecisiounen, Datendecisiounen,
Compliance-Decisiounen, klinesch a medizinesch Decisiounen, Sécherheetsdecisiounen
a méi.

Funktionéiert mat all CI-System (GitLab, Jenkins, CircleCI) an als Pre-Commit-Hook.
Open Source. MIT-Lizenz.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) ass eng GitHub
Action, déi e Pull Request feelen léisst, wann iwwerwaacht Code-Pfaden änneren, ouni
datt eng Architektur-Decisiounsopzeechnung derbäigesat oder aktualiséiert gëtt. Ausnamen sinn explizit: eng
`ADR-Exempt:`-Zeil mat engem Grond léisst d'Gate passéieren a gëtt an d'Job-Zesummefaassung geschriwwen.
Template-agnostesch, keng Ofhängegkeeten. Open Source. MIT-Lizenz.

## Fir méi Informatiounen

Aféierung:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Virlagen:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Déiploteg:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - gratis monatlech Lektioun iwwer Softwarearchitektur

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Tools:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Firmespezifesch Guidance:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Beispiller:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Videoen:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcasts:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Bicher:

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

Kuckt och:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - E vendor-neutrale, maschinnenliesbart YAML-/JSON-Format, fir Decisiounen mat explizitter Begrënnung, Viraussetzungen, kognitivem Zoustand a Kompromësser duerzestellen. Ergänzt ADR, andeems et strukturéiert, validéierbar Begrënnung bei der Decisiounsdokumentatioun derbäisetzt.
