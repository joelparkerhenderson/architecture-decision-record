# Zapis arhitekturne odločitve (ADR)

Zapis arhitekturne odločitve (ADR) je dokument, ki zajema pomembno sprejeto arhitekturno odločitev skupaj z njenim kontekstom in posledicami.

> [!IMPORTANT]
> Pred uporabo teh virov v katerem koli kritičnem sistemu opravite lastno skrbno preverjanje.

Vsebina:

- [Kaj je zapis arhitekturne odločitve?](#kaj-je-zapis-arhitekturne-odločitve)
- [Kako začeti uporabljati ADR](#kako-začeti-uporabljati-adr)
- [Kako začeti uporabljati ADR z orodji](#kako-začeti-uporabljati-adr-z-orodji)
- [Kako začeti uporabljati ADR z gitom](#kako-začeti-uporabljati-adr-z-gitom)
- [Veščine Claude Code za ADR](#veščine-claude-code-za-adr)
- [Konvencije poimenovanja datotek za ADR](#konvencije-poimenovanja-datotek-za-adr)
- [Predlogi za pisanje dobrih ADR](#predlogi-za-pisanje-dobrih-adr)
- [Primeri predlog ADR](#primeri-predlog-adr)
- [Nasveti za timsko delo pri ADR](#nasveti-za-timsko-delo-pri-adr)
- [Vprašanja za timsko delo pri ADR](#vprašanja-za-timsko-delo-pri-adr)
- [Koncepti naslednjih korakov za ADR](#koncepti-naslednjih-korakov-za-adr)
- [Arhitekturni diagrami, pogledi in zorni koti](#arhitekturni-diagrami-pogledi-in-zorni-koti)
- [Funkcije ustreznosti za odločitve kot kodo](#funkcije-ustreznosti-za-odločitve-kot-kodo)
- [Varovala odločitev za zahteve za združitev](#varovala-odločitev-za-zahteve-za-združitev)
- [Več informacij](#več-informacij)

Predloge:

- [Predloga zapisa odločitve Jeffa Tyreeja in Arta Akermana](predloge/predloga-zapisa-odlocitve-jeff-tyree-in-art-akerman/)
- [Predloga zapisa odločitve Michaela Nygarda](predloge/predloga-zapisa-odlocitve-michael-nygard/)
- [Predloga zapisa odločitve EdgeX](predloge/predloga-zapisa-odlocitve-edgex/)
- [Predloga zapisa odločitve arc42](predloge/predloga-zapisa-odlocitve-arc42/)
- [Predloga zapisa odločitve za aleksandrijski vzorec](predloge/predloga-zapisa-odlocitve-za-aleksandrijski-vzorec/)
- [Predloga zapisa odločitve za poslovni primer](predloge/predloga-zapisa-odlocitve-za-poslovni-primer/)
- [Predloga zapisa odločitve projekta MADR](predloge/predloga-zapisa-odlocitve-projekta-madr/)
- [Predloga zapisa odločitve s Planguage](predloge/predloga-zapisa-odlocitve-s-planguage/)
- [Predloga zapisa odločitve Paula Mersona](https://github.com/pmerson/ADR-template)
- [Predloga zapisa odločitve Olafa Zimmermanna](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Predloga zapisa odločitve Garetha Morgana](predloge/predloga-zapisa-odlocitve-gareth-morgan/)
- [Predloga zapisa odločitve GIG Cymru NHS Wales](predloge/predloga-zapisa-odlocitve-gig-cymru-nhs-wales/)
- [Predloga zapisa odločitve za pomembne tehnične odločitve (ITD) Ignacia Larrañage](predloge/predloga-zapisa-odlocitve-za-pomembne-tehnicne-odlocitve/)

Primeri:

- [Ogrodje CSS](primeri/ogrodje-css/)
- [Konfiguracija okoljskih spremenljivk](primeri/konfiguracija-okoljskih-spremenljivk/)
- [Metrike, nadzor, opozorila](primeri/metrike-nadzor-opozorila/)
- [Microsoft Azure DevOps](primeri/microsoft-azure-devops/)
- [Monorepo ali multirepo](primeri/monorepo-ali-multirepo/)
- [Programski jeziki](primeri/programski-jeziki/)
- [Shranjevanje skrivnosti](primeri/shranjevanje-skrivnosti/)
- [Format časovnega žiga](primeri/format-casovnega-ziga/)
- [Še veliko več ...](primeri/)

## Kaj je zapis arhitekturne odločitve?

**Zapis arhitekturne odločitve** (ADR) je dokument, ki zajema pomembno sprejeto arhitekturno odločitev skupaj z njenim kontekstom in posledicami.

**Arhitekturna odločitev** (AD) je izbira pri oblikovanju programske opreme, ki obravnava pomembno zahtevo.

**Dnevnik arhitekturnih odločitev** (ADL) je zbirka vseh ADR, ustvarjenih in vzdrževanih za določen projekt (ali organizacijo).

**Arhitekturno pomembna zahteva** (ASR) je zahteva, ki ima merljiv vpliv na arhitekturo programskega sistema.

Vse našteto spada na področje **upravljanja arhitekturnega znanja** (AKM).

Namen tega dokumenta je zagotoviti hiter pregled ADR, kako jih ustvariti in kje poiskati več informacij.

Kratice:

  * **AD**: arhitekturna odločitev

  * **ADL**: dnevnik arhitekturnih odločitev

  * **ADR**: zapis arhitekturne odločitve

  * **AKM**: upravljanje arhitekturnega znanja

  * **ASR**: arhitekturno pomembna zahteva

## Kako začeti uporabljati ADR

Če želite začeti uporabljati ADR, se s sodelavci pogovorite o naslednjih področjih.

Prepoznavanje odločitev:

  * Kako nujna in kako pomembna je AD?

  * Ali jo je treba sprejeti zdaj ali lahko počaka, dokler ne bo znanega več?

  * Pri prepoznavanju odločitev lahko pomagajo osebne in skupne izkušnje ter priznane metode in prakse oblikovanja.

  * Idealno je vzdrževati seznam odločitev, ki jih je treba sprejeti, kot dopolnilo seznama opravil izdelka.

Sprejemanje odločitev:

  * Obstaja več tehnik odločanja, tako splošnih kot posebnih za programsko arhitekturo, na primer kartiranje dialoga (dialogue mapping).

  * Skupinsko odločanje je dejavno raziskovalno področje.

Uveljavitev in izvrševanje odločitev:

  * AD se uporabljajo pri oblikovanju programske opreme; zato jih je treba sporočiti deležnikom sistema, ki ga financirajo, razvijajo in upravljajo, in jih ti morajo sprejeti.

  * Dva sorodna pristopa sta arhitekturno razvidni slogi kodiranja ter pregledi kode, osredotočeni na arhitekturna vprašanja in odločitve.

  * AD je treba pri posodabljanju programskega sistema v okviru evolucije programske opreme tudi (ponovno) obravnavati.

Deljenje odločitev (neobvezno):

  * Številne AD se ponavljajo v različnih projektih.

  * Zato so lahko izkušnje s preteklimi odločitvami, dobrimi in slabimi, dragoceno ponovno uporabno sredstvo, če uporabljate izrecno strategijo upravljanja znanja.

Dokumentiranje odločitev:

  * Obstaja veliko predlog in orodij za zajemanje odločitev.

  * Oglejte si agilne skupnosti, na primer ADR Michaela Nygarda.

  * Oglejte si tradicionalne procese programskega inženirstva in oblikovanja arhitekture, na primer postavitve tabel, ki jih predlagata IBM UMF ter Tyree in Akerman iz CapitalOne.

Več informacij:

  * Zgornji koraki so povzeti po Wikipedijinem gesu [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Kako začeti uporabljati ADR z orodji

- [MySpec](https://myspec.dev) — platforma za samodejne specifikacije in arhitekturne odločitve, ki strukturira projektno ustavo, tehnično arhitekturo in ADR v čist Markdown, objavljen prek MCP.

ADR lahko začnete uporabljati z orodji na kateri koli način.

Na primer:

  * Če radi uporabljate Google Drive in spletno urejanje, lahko ustvarite Google Doc ali Google Sheet.

  * Če radi uporabljate nadzor različic izvorne kode, na primer git, lahko za vsak ADR ustvarite datoteko.

  * Če radi uporabljate orodja za načrtovanje projektov, na primer Atlassian Jira, lahko uporabite sledilnik načrtovanja v orodju.

  * Če radi uporabljate wikije, na primer MediaWiki, lahko ustvarite wiki za ADR.

## Kako začeti uporabljati ADR z gitom

Če radi uporabljate nadzor različic git, vam tukaj pokažemo, kako radi začnemo uporabljati ADR z gitom pri tipičnem programskem projektu z izvorno kodo.

Ustvarite imenik za datoteke ADR:

```sh
$ mkdir adr
```

Za vsak ADR ustvarite besedilno datoteko, na primer `choose-database.md`:

```sh
$ vi choose-database.md
```

V ADR napišite, karkoli želite. Za zamisli si oglejte predloge v tem repozitoriju.

Potrdite ADR v svoj repozitorij git.

## Veščine Claude Code za ADR

Ta repozitorij vsebuje dve veščini (angl. skills) za [Claude Code](https://claude.com/claude-code) v imeniku [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), tako da lahko programerski agent z umetno inteligenco piše in vzdržuje ADR, kot priporoča ta projekt:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — splošnonamenska, za vsakogar, ki piše ADR v katerem koli projektu. Pomaga se odločiti, ali odločitev potrebuje ADR, vzpostavi imenik `adr/` ali `decisions/`, poimenuje datoteko, izbere predlogo izmed enajstih priloženih ogrodij in napiše trdne razdelke Kontekst/Odločitev/Posledice.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — posebej za vzdrževalce tega repozitorija. Dokumentira postavitev repozitorija, konvencijo zrcaljenja README/jezikovnih različic in natančne korake za dodajanje nove predloge, primera ali povezave na orodje.

Za uporabo veščine kopirajte njeno mapo v `.claude/skills/` v korenu repozitorija, v katerem delate (ali v `~/.claude/skills/`, da bo na voljo v vsakem projektu), nato Claude Code prosite, naj napiše ali pregleda ADR.

## Konvencije poimenovanja datotek za ADR

Če se odločite ustvarjati ADR s tipičnimi besedilnimi datotekami, si boste morda želeli izdelati lastno konvencijo poimenovanja datotek ADR.

Mi dajemo prednost konvenciji poimenovanja datotek z določeno obliko.

Primeri:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Naša konvencija poimenovanja datotek:

  * Ime vsebuje glagolsko zvezo v velelniku sedanjika. To izboljša berljivost in se ujema z obliko naših sporočil ob potrditvah.

  * Ime uporablja male črke in vezaje (enako kot ta repozitorij). To je ravnovesje med berljivostjo in uporabnostjo sistema.

  * Pripona je markdown. To je lahko koristno za preprosto oblikovanje.

## Predlogi za pisanje dobrih ADR

Značilnosti dobrega ADR:

* Utemeljitev: Pojasnite razloge za določeno AD. To lahko vključuje kontekst (glejte spodaj), prednosti in slabosti različnih možnih izbir, primerjave funkcij, razprave o stroških in koristih ter drugo.

* Natančnost: Vsak ADR naj govori o eni AD, ne o več AD.

* Časovni žigi: Navedite, kdaj je bil napisan posamezni element v ADR. To je še posebej pomembno za vidike, ki se lahko sčasoma spremenijo, na primer stroške, urnike, skaliranje in podobno.

* Nespremenljivost: Ne spreminjajte obstoječih informacij v ADR. Namesto tega ADR dopolnite z dodajanjem novih informacij ali ga nadomestite z ustvarjanjem novega ADR.

Značilnosti dobrega razdelka »Kontekst« v ADR:

* Pojasnite položaj svoje organizacije in poslovne prednostne naloge.

* Vključite utemeljitve in premisleke, ki temeljijo na družbeni sestavi in veščinah vaših ekip.

* Vključite prednosti in slabosti, ki so pomembne, ter jih opišite z izrazi, ki se skladajo z vašimi potrebami in cilji.

Značilnosti dobrega razdelka »Posledice« v ADR:

* Pojasnite, kaj izhaja iz sprejetja odločitve. To lahko vključuje učinke, izide, izdelke, nadaljnje ukrepe in drugo.

* Vključite informacije o morebitnih naslednjih ADR. Relativno pogosto en ADR sproži potrebo po dodatnih ADR, na primer ko en ADR sprejme veliko krovno izbiro, ta pa ustvari potrebe po več manjših odločitvah.

* Vključite morebitne postopke pregleda po ukrepu. Običajno ekipe vsak ADR pregledajo en mesec pozneje, da primerjajo informacije v ADR s tem, kar se je zgodilo v praksi, in se tako učijo ter rastejo.

Nov ADR lahko nadomesti prejšnji ADR:

* Ko je sprejeta AD, ki nadomesti ali razveljavi prejšnji ADR, je treba ustvariti nov ADR

## Primeri predlog ADR

Primeri predlog ADR, ki smo jih zbrali na spletu:

- [Predloga ADR Michaela Nygarda](predloge/predloga-zapisa-odlocitve-michael-nygard/) (preprosta in priljubljena)

- [Predloga ADR Jeffa Tyreeja in Arta Akermana](predloge/predloga-zapisa-odlocitve-jeff-tyree-in-art-akerman/) (bolj dovršena)

- [Predloga ADR za aleksandrijski vzorec](predloge/predloga-zapisa-odlocitve-za-aleksandrijski-vzorec/) (preprosta, s podrobnostmi konteksta)

- [Predloga ADR za poslovni primer](predloge/predloga-zapisa-odlocitve-za-poslovni-primer/) (bolj usmerjena v MBA, s stroški, analizo SWOT in več mnenji)

- [Predloga ADR projekta Markdown Any Decision Records (MADR)](predloge/predloga-zapisa-odlocitve-projekta-madr/) (preprosta in obsežna različica; slednja poudarja možnosti ter njihove prednosti in slabosti)

- [Predloga ADR s Planguage](predloge/predloga-zapisa-odlocitve-s-planguage/) (bolj usmerjena v zagotavljanje kakovosti)

- [Predloga za pomembne tehnične odločitve (ITD) Ignacia Larrañage](predloge/predloga-zapisa-odlocitve-za-pomembne-tehnicne-odlocitve/) (vitka in z odločitvijo na prvem mestu, optimizirana za hiter pregled vodstva)

## Nasveti za timsko delo pri ADR

Če razmišljate o uporabi zapisov odločitev v svoji ekipi, vam tukaj ponujamo nekaj nasvetov, ki smo se jih naučili pri delu z mnogimi ekipami.

Imate priložnost voditi sodelavce tako, da se skupaj pogovarjate o tem, »zakaj«, namesto da bi ukazovali, »kaj«. Zapisi odločitev so na primer način, s katerim ekipe pametneje razmišljajo in bolje komunicirajo; zapisi odločitev niso dragoceni, če so le naknadno vsiljena papirologija.

Nekatere ekipe veliko raje uporabljajo ime »odločitve« kot kratico »ADR«. Ko nekatere ekipe uporabijo ime imenika »decisions«, se kot da prižge žarnica in ekipa začne v imenik dajati več informacij, na primer odločitve o dobaviteljih, odločitve o načrtovanju, odločitve o terminih itd. Vse te vrste informacij lahko uporabljajo isto predlogo. Domnevamo, da se ljudje hitreje učijo z besedami (»odločitve«) kot s kraticami (»ADR«), da so ljudje bolj motivirani za pisanje dokumentov v nastajanju, ko se odstrani beseda »zapis«, ter da nekaterim razvijalcem in nekaterim vodjem beseda »arhitektura« ni všeč.

Teoretično je nespremenljivost idealna. V praksi se je spremenljivost za naše ekipe bolje obnesla. Nove informacije vstavimo v obstoječi ADR z datumom in opombo, da so informacije prispele po odločitvi. Takšen pristop vodi do »živega dokumenta«, ki ga lahko posodabljamo vsi. Tipične posodobitve nastanejo, ko dobimo informacije zaradi novih članov ekipe ali novih ponudb, zaradi resničnih rezultatov naše uporabe ali po naknadnih spremembah tretjih strani, na primer zmožnosti dobaviteljev, cenovnih načrtov, licenčnih pogodb itd.

## Vprašanja za timsko delo pri ADR


### Kdo lahko ustvari ADR?

Upoštevajte področja, kot so določene osebe, določene vloge, določene ekipe ali določeni oddelki; upoštevajte tudi, ali obstajajo osebe, vloge, ekipe ali oddelki, ki lahko naročijo ADR, kar pomeni, da zahtevajo ADR, ki ga bo napisal nekdo drug. 

Primer odgovora: Vsaka oseba v naši organizaciji, ki je prebrala stran README o zapisu arhitekturne odločitve, lahko predlaga ADR, kar pomeni, da ga lahko začne pisati in ga deli z ekipo.

### Kaj upravičuje pripravo ADR?

Upoštevajte področja, kot so načini dela ekip v vaši organizaciji, struktura vašega programskega sistema, usklajevanje med ekipami, dolgoročna vzdržljivost, zunanji vmesniki, kdo naj ima korist in podobno. 

Primer odgovora: ADR želimo ustvariti, kadar želimo, da bi prihodnji razvijalci razumeli »zakaj« tega, kar počnemo.

### Kaj upravičuje opustitev priprave ADR?

Upoštevajte področja, kot so odločitve, ki niso arhitekturne ali so drobne, na primer z minimalnim tveganjem, samostojne ali ki jih sprejme en sam razvijalec, ali so že v celoti pokrite drugje, na primer s standardi, politikami ali dokumentacijo, ali so začasne, na primer obvodi, dokazi o izvedljivosti ali poskusi. 

Primer odgovora: ADR želimo preskočiti, kadar je odločitev omejena po obsegu, času, tveganju in stroških ali je že pokrita drugje.

### Kakšen je življenjski cikel ADR?

Upoštevajte področja, kot so postopek ustvarjanja, postopek raziskovanja, postopek odločanja, postopek izvajanja in postopek opustitve. Razmislite, kako spremljati življenjski cikel ADR skozi čas, na primer kako ADR premakniti iz enega stanja v naslednje in kako to sporočiti deležnikom. 

Primer odgovora: Želimo, da ima ADR pet stopenj življenjskega cikla: Uvedba → Raziskovanje → Vrednotenje → Izvajanje → Vzdrževanje → Opustitev.

### Kakšna so merila za korake življenjskega cikla ADR?

Upoštevajte področja, kot so merila sprejemljivosti za ADR, kar pomeni, kako veste, da je dovolj dober za prehod iz enega koraka življenjskega cikla v naslednjega? Ali je problem jasno opredeljen? Ali so bile upoštevane alternative? Ali so kompromisi dovolj dobro razumljeni in dokumentirani?
Ali je ves ustrezen kontekst na mestu? Ali so vključeni vsi ustrezni deležniki? Ali so bile vse povratne informacije upoštevane? 

Primer odgovora: Želimo, da o ADR glasujejo deležniki, ko je dejavna ekipa 1) zaključila raziskavo, 2) zaključila vrednotenje, 3) deležnikom objavila predlog ADR z zahtevo za komentarje in časovnim oknom enega tedna, 4) so bili vsi komentarji deležnikov upoštevani in obravnavani.

### Katere vloge in odgovornosti sodelujejo pri ADR?

Upoštevajte vloge, kot so predlagatelj, raziskovalec, ocenjevalec, pregledovalec, odobritelj, vzdrževalec in podobno. Upoštevajte odgovornosti, kot so komunikacija z deležniki, zagotavljanje izpolnitve pričakovanj, deljenje na spletnem mestu ali intranetu ter redno pregledovanje dela, še posebej ob pomembnih spremembah.

Primer odgovora: Želimo, da ima vsak ADR vedno primarno kontaktno osebo, sekundarno kontaktno osebo in odgovorno ekipo; te so odgovorne za komunikacijo, objave, vzdrževanje, redni pregled vsaj enkrat na leto in morebitno opustitev po potrebi.

### Kako upravljanje (governance) vpliva na ADR?

Upoštevajte področja, kot so načini dela v vaši organizaciji, posebne potrebe po skladnosti, na primer pravni vidiki ali vidiki kadrovskih virov, ter kako želite ravnati s soglasjem, konflikti in stopnjevanjem. Ali obstajajo področja, osebe ali ekipe, ki imajo lahko glede ADR večji vpliv kot druge, na primer da ga lahko odobrijo, o njem glasujejo ali nanj vložijo veto?

Primer odgovora: Upravljanje ADR poteka v tem vrstnem redu prednosti: generalni direktor (CEO), tehnični direktor (CTO), pravni direktor (CLO), ekipa, ki izvaja ADR, strokovnjaki v ekipi, ki najbolje poznajo AD. Nihče drug nima pristojnosti upravljanja, razen če je to opisano v ADR. 

### Katera načela vplivajo na ADR?

Upoštevajte področja, kot so načini dela v vaši organizaciji, ki vključujejo hitro ali počasno ukrepanje, soglasje ali nesoglasje pri odločitvah, prednost tveganja ali prednost varnosti, javno ali zasebno razpravo in podobno.

Primer odgovora: Uporabljamo vodstvena načela nagnjenosti k ukrepanju (bias for action), nestrinjanja z zavezanostjo (disagree-and-commit), 70-odstotne ocene zadoščajo za lahko povratljive in lahko izolirane odločitve ter javne načine dela, razen pri zaupnih informacijah, kot je opisano v dogovoru o zaupnosti naše organizacije.

## Koncepti naslednjih korakov za ADR

[Arc42](https://arc42.org/) pragmatično odgovarja na dve vprašanji in ga je mogoče prilagoditi vašim posebnim potrebam. Kaj naj dokumentirate/sporočate o svoji arhitekturi? Kako naj dokumentirate/sporočate? Arc42 vključuje zapise arhitekturnih odločitev ter smernice o ciljih, omejitvah, kontekstih, kakovosti, tveganjih in drugem.

[Model C4](https://c4model.com/) je lahko naučljiv, razvijalcem prijazen pristop k izdelavi diagramov programske arhitekture. C4 je nabor hierarhičnih diagramov za kontekst, vsebnike, komponente in kodo ter podpornih diagramov za krajino sistemov, dinamiko in uvajanje.

## Arhitekturni diagrami, pogledi in zorni koti

Arhitekturni diagram se imenuje »arhitekturni pogled«.

»Arhitekturni pogled« je primerek »arhitekturnega zornega kota«.

»Arhitekturni zorni kot« ima določeno občinstvo z določenimi skrbmi.

Primeri arhitekturnih zornih kotov, pogledov in diagramov:

- Poslovne zmožnosti

- Poslovni procesi na visoki ravni

- [Tokovi vrednosti (Value Streams)](https://en.wikipedia.org/wiki/Value_stream)

- Programske funkcije, preslikane na komponente aplikacij

- [Model C4](https://en.wikipedia.org/wiki/C4_model): kontekstni diagram (TO-BE / AS-IS)

- [Model C4](https://en.wikipedia.org/wiki/C4_model): diagram vsebnikov (TO-BE / AS-IS)

- [Diagram entitet in razmerij (Entity-relationship Diagram)](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) za preslikavo podatkovnih entitet na komponente aplikacij

- [Sekvenčni diagrami (Sequence Diagrams)](https://en.wikipedia.org/wiki/Sequence_diagram) za opis funkcijskih tokov znotraj sistemov in za integracije

- Diagrami [modela in notacije poslovnih procesov (Business Process Model and Notation)](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) za opis tokov podatkov med komponentami aplikacij

- Diagrami [modela in notacije poslovnih procesov (Business Process Model and Notation)](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) za opis poslovnih procesov / uporabniških scenarijev

- Diagrami [upravljanja identitet in dostopa (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM)

- Diagrami [nadzora dostopa na podlagi vlog (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) z vlogami za vsako komponento aplikacije

- Diagrami [nadzora dostopa na podlagi atributov (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) z atributi za vsako komponento aplikacije

- Diagrami zasebnosti

Sorodni diagrami:

- Diagram primerov uporabe prikazuje primere uporabe vodstvu/strankam; ta je pred zahtevami, te pa pred programsko arhitekturo.

- Diagram uvajanja prikazuje fizično strojno opremo/računalnike, na katere se uvajajo programske komponente.
- Diagram pretoka podatkov prikazuje, kako se podatki gibljejo skozi sistem in se preoblikujejo.
- Sekvenčni diagram se uporablja za prikaz delovanja protokolov, kot je HTTP, na časovni osi.

- Diagram dejavnosti prikazuje potek dejavnosti, ki jih izvaja programski sistem, na primer kot umetna inteligenca NPC.

## Funkcije ustreznosti za odločitve kot kodo

Funkcije ustreznosti (fitness functions) so objektivna samodejna preverjanja, napisana s programsko kodo, ki preverjajo, da se odločitve upoštevajo.

- Funkcije ustreznosti omogočajo testiranje in zagotavljanje odločitev.

- Funkcije ustreznosti za odločitve lahko močno pomagajo pri zagotavljanju kakovosti, regulativnih postopkih in ciljih upravljanja.

### Kako so funkcije ustreznosti povezane z odločitvami

Zapis odločitve dokumentira odločitev, funkcija ustreznosti pa odločitev zagotavlja.

- Primer odločitve: Za revizijske zahteve uporabljamo dogodkovno shranjevanje (event sourcing).

- Primer funkcije ustreznosti: S strežnikom za neprekinjeno integracijo preizkusimo, da morajo vse spremembe stanja ustvariti dogodke.

### Zakaj funkcije ustreznosti pomagajo odločitvam

Objektivne meritve: Funkcije ustreznosti uspejo ali padejo, zato je delo vidno in jasno.

Neprekinjena uporaba: Funkcije ustreznosti so vaša živa pravila, ki se izvajajo ob vsaki potrditvi in vsaki gradnji.

Zaupanje za preoblikovanje kode: Funkcije ustreznosti samodejno ujamejo napake v pravilih odločitev.

Razširljivo upravljanje: Funkcije ustreznosti zagotavljajo standarde, ne da bi ustvarjale ozka grla.

### Ali lahko funkcije ustreznosti uporabljajo umetno inteligenco?

Funkcije ustreznosti lahko pri odločitvah izkoristijo velike jezikovne modele (LLM) z umetno inteligenco, tako da postavljajo vprašanja o vašem delu,
na primer o načrtih, kodi, shemah, API-jih in drugem:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Testiranje arhitekturnih enot

[ArchUnit](https://www.archunit.org/): preverjajte arhitekturna pravila kode Java z uporabo katerega koli navadnega ogrodja za enotne teste Java.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): preverjajte arhitekturna pravila kode TypeScript in kode JavaScript z uporabo Jest, Vitest, Jasmine itd.

## Varovala odločitev za zahteve za združitev

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
samodejno prikaže prave zapise odločitev v pravem trenutku – ko razvijalec
dejavno spreminja kodo, ki jo te odločitve zajemajo. Namesto da bi upali, da
razvijalci pred združitvijo preberejo mapo z dokumenti, se ustrezni kontekst
pojavi neposredno na zahtevi za združitev (pull request).

To deluje za vse vrste zapisov odločitev: arhitekturne odločitve, podatkovne
odločitve, odločitve o skladnosti, klinične in medicinske odločitve, varnostne
odločitve in druge.

Deluje s katerim koli sistemom CI (GitLab, Jenkins, CircleCI) in kot kljuka
pred potrditvijo (pre-commit hook). Odprta koda. Licenca MIT.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) je akcija
GitHub, ki zavrne zahtevo za združitev, ko se spremljane poti kode spremenijo,
ne da bi bil dodan ali posodobljen zapis arhitekturne odločitve. Izjeme so
izrecne: vrstica `ADR-Exempt:` z razlogom prepusti vrata in se zapiše v
povzetek opravila. Neodvisna od predloge, brez odvisnosti. Odprta koda. Licenca MIT.

## Več informacij

Uvod:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Predloge:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Poglobljeno:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - brezplačna mesečna lekcija o programski arhitekturi

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Orodja:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Smernice posameznih podjetij:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Primeri:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Videoposnetki:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podkasti:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Knjige:

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

Glejte tudi:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Od dobavitelja neodvisen, strojno berljiv format YAML/JSON za predstavitev odločitev z izrecno utemeljitvijo, predpostavkami, kognitivnim stanjem in kompromisi. Dopolnjuje ADR z dodajanjem strukturirane, preverljive utemeljitve k dokumentaciji odločitev.
