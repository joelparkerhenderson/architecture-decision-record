# Rekord ta' deċiżjoni arkitettonika (ADR)

Rekord ta' deċiżjoni arkitettonika (ADR) huwa dokument li jiġbor deċiżjoni arkitettonika importanti li saret flimkien mal-kuntest u mal-konsegwenzi tagħha.

> [!IMPORTANT]
> Agħmel id-diliġenza dovuta tiegħek stess fuq dawn ir-riżorsi qabel ma tużahom f'kwalunkwe sistema kritika.

Werrej:

- [X'inhu rekord ta' deċiżjoni arkitettonika?](#xinhu-rekord-ta-deċiżjoni-arkitettonika)
- [Kif tibda tuża l-ADR](#kif-tibda-tuża-l-adr)
- [Kif tibda tuża l-ADR bl-għodod](#kif-tibda-tuża-l-adr-bl-għodod)
- [Kif tibda tuża l-ADR mal-git](#kif-tibda-tuża-l-adr-mal-git)
- [Skills ta' Claude Code għall-ADR](#skills-ta-claude-code-għall-adr)
- [Konvenzjonijiet tal-ismijiet tal-fajls għall-ADR](#konvenzjonijiet-tal-ismijiet-tal-fajls-għall-adr)
- [Suġġerimenti biex tikteb ADR tajbin](#suġġerimenti-biex-tikteb-adr-tajbin)
- [Mudelli ta' eżempju tal-ADR](#mudelli-ta-eżempju-tal-adr)
- [Pariri dwar ix-xogħol fi tim għall-ADR](#pariri-dwar-ix-xogħol-fi-tim-għall-adr)
- [Mistoqsijiet dwar ix-xogħol fi tim għall-ADR](#mistoqsijiet-dwar-ix-xogħol-fi-tim-għall-adr)
- [Kunċetti tal-pass li jmiss għall-ADR](#kunċetti-tal-pass-li-jmiss-għall-adr)
- [Dijagrammi & vedute & perspettivi tal-arkitettura](#dijagrammi--vedute--perspettivi-tal-arkitettura)
- [Funzjonijiet ta' idoneità għad-deċiżjonijiet bħala kodiċi](#funzjonijiet-ta-idoneità-għad-deċiżjonijiet-bħala-kodiċi)
- [Guardrails tad-deċiżjonijiet għall-pull requests](#guardrails-tad-deċiżjonijiet-għall-pull-requests)
- [Aktar informazzjoni](#aktar-informazzjoni)

Mudelli:

- [Mudell ta' rekord ta' deċiżjoni minn Jeff Tyree u Art Akerman](mudelli/mudell-ta-rekord-ta-decizjoni-minn-jeff-tyree-u-art-akerman/)
- [Mudell ta' rekord ta' deċiżjoni minn Michael Nygard](mudelli/mudell-ta-rekord-ta-decizjoni-minn-michael-nygard/)
- [Mudell ta' rekord ta' deċiżjoni minn EdgeX](mudelli/mudell-ta-rekord-ta-decizjoni-minn-edgex/)
- [Mudell ta' rekord ta' deċiżjoni minn arc42](mudelli/mudell-ta-rekord-ta-decizjoni-minn-arc42/)
- [Mudell ta' rekord ta' deċiżjoni għax-xejra Alexandrian](mudelli/mudell-ta-rekord-ta-decizjoni-ghax-xejra-alexandrian/)
- [Mudell ta' rekord ta' deċiżjoni għal każ kummerċjali](mudelli/mudell-ta-rekord-ta-decizjoni-ghal-kaz-kummercjali/)
- [Mudell ta' rekord ta' deċiżjoni tal-Proġett MADR](mudelli/mudell-ta-rekord-ta-decizjoni-tal-progett-madr/)
- [Mudell ta' rekord ta' deċiżjoni bl-użu ta' Planguage](mudelli/mudell-ta-rekord-ta-decizjoni-bl-uzu-ta-planguage/)
- [Mudell ta' rekord ta' deċiżjoni minn Paulo Merson](https://github.com/pmerson/ADR-template)
- [Mudell ta' rekord ta' deċiżjoni minn Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Mudell ta' rekord ta' deċiżjoni minn Gareth Morgan](mudelli/mudell-ta-rekord-ta-decizjoni-minn-gareth-morgan/)
- [Mudell ta' rekord ta' deċiżjoni minn GIG Cymru NHS Wales](mudelli/mudell-ta-rekord-ta-decizjoni-minn-gig-cymru-nhs-wales/)
- [Mudell ta' rekord ta' deċiżjoni għal Deċiżjonijiet Tekniċi Importanti (ITDs) minn Ignacio Larrañaga](mudelli/mudell-ta-rekord-ta-decizjoni-ghal-decizjonijiet-tekniki-importanti/)

Eżempji:

- [Qafas CSS](ezempji/qafas-css/)
- [Konfigurazzjoni tal-varjabbli tal-ambjent](ezempji/konfigurazzjoni-tal-varjabbli-tal-ambjent/)
- [Metriċi, monitors, twissijiet](ezempji/metrici-monitors-twissijiet/)
- [Microsoft Azure DevOps](ezempji/microsoft-azure-devops/)
- [Monorepo jew multirepo](ezempji/monorepo-jew-multirepo/)
- [Lingwi tal-programmazzjoni](ezempji/lingwi-ta-programmazzjoni/)
- [Ħażna tas-sigrieti](ezempji/hazna-tas-sigrieti/)
- [Format tat-timestamp](ezempji/format-tat-timestamp/)
- [Ħafna aktar...](ezempji/)

## X'inhu rekord ta' deċiżjoni arkitettonika?

**Rekord ta' deċiżjoni arkitettonika** (ADR) huwa dokument li jiġbor deċiżjoni arkitettonika importanti li saret flimkien mal-kuntest u mal-konsegwenzi tagħha.

**Deċiżjoni arkitettonika** (AD) hija għażla fid-disinn tas-software li tindirizza rekwiżit sinifikanti.

**Reġistru tad-deċiżjonijiet arkitettoniċi** (ADL) huwa l-ġabra tal-ADR kollha maħluqa u miżmuma għal proġett (jew organizzazzjoni) partikolari.

**Rekwiżit sinifikanti mil-lat arkitettoniku** (ASR) huwa rekwiżit li għandu effett li jista' jitkejjel fuq l-arkitettura ta' sistema tas-software.

Dan kollu jidħol fis-suġġett tal-**ġestjoni tal-għarfien arkitettoniku** (AKM).

L-għan ta' dan id-dokument huwa li jagħti ħarsa ġenerali mgħaġġla lejn l-ADR, kif jinħolqu, u fejn wieħed jista' jara aktar informazzjoni.

Abbrevjazzjonijiet:

  * **AD**: deċiżjoni arkitettonika

  * **ADL**: reġistru tad-deċiżjonijiet arkitettoniċi

  * **ADR**: rekord ta' deċiżjoni arkitettonika

  * **AKM**: ġestjoni tal-għarfien arkitettoniku

  * **ASR**: rekwiżit sinifikanti mil-lat arkitettoniku

## Kif tibda tuża l-ADR

Biex tibda tuża l-ADR, kellem lil sħabek tat-tim dwar dawn l-oqsma.

Identifikazzjoni tad-deċiżjoni:

  * Kemm hi urġenti u kemm hi importanti l-AD?

  * Trid issir issa, jew tistax tistenna sakemm jinkiseb aktar għarfien?

  * Kemm l-esperjenza personali u kollettiva, kif ukoll metodi u prattiki ta' disinn rikonoxxuti, jistgħu jgħinu fl-identifikazzjoni tad-deċiżjonijiet.

  * Idealment żomm lista ta' deċiżjonijiet li jridu jsiru li tikkumplimenta l-lista ta' affarijiet li jridu jsiru tal-prodott.

It-teħid tad-deċiżjonijiet:

  * Teżisti numru ta' tekniki għat-teħid tad-deċiżjonijiet, kemm ġenerali kif ukoll speċifiċi għall-arkitettura tas-software, pereżempju d-dialogue mapping.

  * It-teħid ta' deċiżjonijiet fi grupp huwa suġġett ta' riċerka attiva.

Il-promulgazzjoni u l-infurzar tad-deċiżjonijiet:

  * L-AD jintużaw fid-disinn tas-software; għalhekk iridu jiġu kkomunikati lill-partijiet interessati tas-sistema li jiffinanzjawha, jiżviluppawha u jħaddmuha, u jridu jiġu aċċettati minnhom.

  * Stili ta' kodiċi arkitettonikament evidenti u reviżjonijiet tal-kodiċi li jiffukaw fuq tħassib u deċiżjonijiet arkitettoniċi huma żewġ prattiki relatati.

  * L-AD iridu jerġgħu jiġu kkunsidrati wkoll meta sistema tas-software tiġi mmodernizzata fl-evoluzzjoni tas-software.

Qsim tad-deċiżjonijiet (fakultattiv):

  * Ħafna AD jirrikorru bejn proġetti differenti.

  * Għalhekk, l-esperjenzi b'deċiżjonijiet tal-passat, tajbin u ħżiena, jistgħu jkunu assi riutilizzabbli prezzjużi meta jintuża approċċ espliċitu ta' ġestjoni tal-għarfien.

Dokumentazzjoni tad-deċiżjonijiet:

  * Jeżistu ħafna mudelli u għodod biex jinġabru d-deċiżjonijiet.

  * Ara l-komunitajiet agile, pereżempju l-ADR ta' M. Nygard.

  * Ara l-proċessi tradizzjonali tal-inġinerija tas-software u tad-disinn tal-arkitettura, pereżempju t-tabelli suġġeriti minn IBM UMF u minn Tyree u Akerman ta' CapitalOne.

Għal aktar:

  * Il-passi ta' hawn fuq huma meħuda mill-voce ta' Wikipedia dwar l-[Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Kif tibda tuża l-ADR bl-għodod

- [MySpec](https://myspec.dev) — Pjattaforma awtomatizzata ta' speċifikazzjoni u deċiżjonijiet arkitettoniċi li tistruttura l-kostituzzjoni tal-proġett, l-arkitettura teknika u l-ADR f'Markdown nadif servut permezz ta' MCP.

Tista' tibda tuża l-ADR bl-għodod bil-mod li tixtieq.

Pereżempju:

  * Jekk tħobb tuża Google Drive u l-editjar online, tista' toħloq Google Doc jew Google Sheet.

  * Jekk tħobb tuża kontroll tal-verżjonijiet tal-kodiċi sors, bħal git, tista' toħloq fajl għal kull ADR.

  * Jekk tħobb tuża għodod tal-ippjanar tal-proġetti, bħal Atlassian Jira, tista' tuża t-tracker tal-ippjanar tal-għodda.

  * Jekk tħobb tuża wikis, bħal MediaWiki, tista' toħloq wiki tal-ADR.

## Kif tibda tuża l-ADR mal-git

Jekk tħobb tuża l-kontroll tal-verżjonijiet git, hawn kif nieħdu pjaċir nibdew nużaw l-ADR mal-git għal proġett tipiku tas-software b'kodiċi sors.

Oħloq direttorju għall-fajls tal-ADR:

```sh
$ mkdir adr
```

Għal kull ADR, oħloq fajl tat-test, bħal `choose-database.md`:

```sh
$ vi choose-database.md
```

Ikteb fl-ADR dak kollu li trid. Ara l-mudelli f'dan ir-repożitorju għal ideat.

Ikkommetti l-ADR fir-repo git tiegħek.

## Skills ta' Claude Code għall-ADR

Dan ir-repożitorju jipprovdi żewġ skills ta' [Claude Code](https://claude.com/claude-code) taħt [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), sabiex aġent tal-kodiċi tal-AI jkun jista' jikteb u jżomm l-ADR bil-mod li jirrakkomanda dan il-proġett:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — ta' użu ġenerali, għal kull min jikteb ADR f'kwalunkwe proġett. Jgħin jiġi deċiż jekk deċiżjoni teħtieġx ADR, jistabbilixxi direttorju `adr/` jew `decisions/`, jagħti isem lill-fajl, jagħżel mudell mill-ħdax-il skeletru inklużi, u jikteb sezzjonijiet solidi ta' Kuntest/Deċiżjoni/Konsegwenzi.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — speċifikament għall-maniġers ta' dan ir-repożitorju. Jiddokumenta l-layout tar-repożitorju, il-konvenzjoni tar-rispekkjar ta' README/locales, u l-passi eżatti biex jiżdied mudell, eżempju, jew rabta ta' għodda ġodda.

Biex tuża skill, ikkopja l-folder tagħha fi `.claude/skills/` fl-għerq tar-repożitorju li qed taħdem fih (jew fi `~/.claude/skills/` biex issir disponibbli f'kull proġett), imbagħad itlob lil Claude Code jikteb jew jirrevedi ADR.

## Konvenzjonijiet tal-ismijiet tal-fajls għall-ADR

Jekk tagħżel li toħloq l-ADR tiegħek bi fajls tat-test tipiċi, forsi tixtieq tfassal il-konvenzjoni tiegħek għall-ismijiet tal-fajls tal-ADR.

Aħna nippreferu nużaw konvenzjoni għall-ismijiet tal-fajls li għandha format speċifiku.

Eżempji:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Il-konvenzjoni tagħna għall-ismijiet tal-fajls:

  * L-isem fih frażi verbali imperattiva fil-preżent. Dan jgħin il-qari u jaqbel mal-format tal-messaġġi tal-kommit tagħna.

  * L-isem juża ittri żgħar u trattini (bħal f'dan ir-repo). Dan huwa bilanċ bejn il-qari faċli u l-użabbiltà tas-sistema.

  * L-estensjoni hija markdown. Dan jista' jkun utli għal formattjar faċli.

## Suġġerimenti biex tikteb ADR tajbin

Karatteristiċi ta' ADR tajjeb:

* Raġunament: Spjega r-raġunijiet għaliex tittieħed l-AD partikolari. Dan jista' jinkludi l-kuntest (ara hawn taħt), il-vantaġġi u l-iżvantaġġi ta' għażliet potenzjali differenti, tqabbil tal-karatteristiċi, diskussjonijiet dwar l-ispiża u l-benefiċċju, u aktar.

* Speċifiku: Kull ADR għandu jkun dwar AD waħda, mhux dwar ħafna AD.

* Timestamps: Identifika meta nkiteb kull element tal-ADR. Dan huwa importanti speċjalment għal aspetti li jistgħu jinbidlu maż-żmien, bħall-ispejjeż, l-iskedi, l-iskalar, u affarijiet simili.

* Immutabbli: Tbiddilx l-informazzjoni eżistenti f'ADR. Minflok, immodifika l-ADR billi żżid informazzjoni ġdida, jew ibdel l-ADR b'ADR ġdid.

Karatteristiċi ta' sezzjoni "Kuntest" tajba f'ADR:

* Spjega s-sitwazzjoni tal-organizzazzjoni tiegħek u l-prijoritajiet tan-negozju.

* Inkludi r-raġunament u l-konsiderazzjonijiet ibbażati fuq il-kompożizzjoni soċjali u tal-ħiliet tat-timijiet tiegħek.

* Inkludi l-vantaġġi u l-iżvantaġġi rilevanti, u ddeskrivihom b'termini li jaqblu mal-bżonnijiet u l-għanijiet tiegħek.

Karatteristiċi ta' sezzjoni "Konsegwenzi" tajba f'ADR:

* Spjega dak li jirriżulta mit-teħid tad-deċiżjoni. Dan jista' jinkludi l-effetti, ir-riżultati, l-outputs, is-segwiti, u aktar.

* Inkludi informazzjoni dwar kwalunkwe ADR sussegwenti. Huwa relattivament komuni li ADR wieħed iqajjem il-ħtieġa għal aktar ADR, bħal meta ADR wieħed jieħu għażla kbira u ġenerali li min-naħa tagħha toħloq bżonn ta' aktar deċiżjonijiet iżgħar.

* Inkludi kwalunkwe proċess ta' reviżjoni wara l-azzjoni. Huwa tipiku li t-timijiet jirrevedu kull ADR xahar wara, biex iqabblu l-informazzjoni tal-ADR ma' dak li ġara fil-prattika, sabiex jitgħallmu u jikbru.

ADR ġdid jista' jieħu post ADR preċedenti:

* Meta tittieħed AD li tieħu post jew tinvalida ADR preċedenti, għandu jinħoloq ADR ġdid

## Mudelli ta' eżempju tal-ADR

Mudelli ta' eżempju tal-ADR li ġbarna fuq in-net:

- [Mudell tal-ADR minn Michael Nygard](mudelli/mudell-ta-rekord-ta-decizjoni-minn-michael-nygard/) (sempliċi u popolari)

- [Mudell tal-ADR minn Jeff Tyree u Art Akerman](mudelli/mudell-ta-rekord-ta-decizjoni-minn-jeff-tyree-u-art-akerman/) (aktar sofistikat)

- [Mudell tal-ADR għax-xejra Alexandrian](mudelli/mudell-ta-rekord-ta-decizjoni-ghax-xejra-alexandrian/) (sempliċi b'speċifiċi tal-kuntest)

- [Mudell tal-ADR għal każ kummerċjali](mudelli/mudell-ta-rekord-ta-decizjoni-ghal-kaz-kummercjali/) (aktar orjentat lejn l-MBA, bi spejjeż, SWOT, u aktar opinjonijiet)

- [Mudell tal-ADR tal-proġett Markdown Any Decision Records (MADR)](mudelli/mudell-ta-rekord-ta-decizjoni-tal-progett-madr/) (verżjoni sempliċi u verżjoni elaborata; din tal-aħħar tenfasizza l-għażliet u l-vantaġġi u l-iżvantaġġi tagħhom)

- [Mudell tal-ADR bl-użu ta' Planguage](mudelli/mudell-ta-rekord-ta-decizjoni-bl-uzu-ta-planguage/) (aktar orjentat lejn l-assigurazzjoni tal-kwalità)

- [Mudell għal Deċiżjonijiet Tekniċi Importanti (ITDs) minn Ignacio Larrañaga](mudelli/mudell-ta-rekord-ta-decizjoni-ghal-decizjonijiet-tekniki-importanti/) (lean u jibda mid-deċiżjoni, ottimizzat għal reviżjoni eżekuttiva mgħaġġla)

## Pariri dwar ix-xogħol fi tim għall-ADR

Jekk qed taħseb li tuża rekords ta' deċiżjoni mat-tim tiegħek, hawn xi pariri li tgħallimna bix-xogħol ma' ħafna timijiet.

Għandek opportunità li tmexxi lil sħabek tat-tim, billi tiddiskutu flimkien il-"għaliex", minflok timponi l-"x'għandu jsir". Pereżempju, ir-rekords ta' deċiżjoni huma mod kif it-timijiet jaħsbu aħjar u jikkomunikaw aħjar; ir-rekords ta' deċiżjoni mhumiex ta' valur jekk ikunu biss rekwiżit ta' karti mġiegħel wara li jkun sar kollox.

Xi timijiet jippreferu ħafna l-isem "deċiżjonijiet" milli l-abbrevjazzjoni "ADR". Meta xi timijiet jużaw l-isem tad-direttorju "decisions", ikun qisu tqabbad bozza tad-dawl, u t-tim jibda jpoġġi aktar informazzjoni fid-direttorju, bħal deċiżjonijiet dwar fornituri, deċiżjonijiet dwar l-ippjanar, deċiżjonijiet dwar l-iskedar, eċċ. Dawn it-tipi kollha ta' informazzjoni jistgħu jużaw l-istess mudell. Aħna nissuppożu li n-nies jitgħallmu aktar malajr bil-kliem ("deċiżjonijiet") milli bl-abbrevjazzjonijiet ("ADR"), li n-nies huma aktar motivati jiktbu dokumenti ta' xogħol li għadu għaddej meta titneħħa l-kelma "rekord", u li wkoll xi żviluppaturi u xi maniġers ma jħobbux il-kelma "arkitettura".

Fit-teorija, l-immutabbiltà hija ideali. Fil-prattika, il-mutabbiltà ħadmet aħjar għat-timijiet tagħna. Aħna ndaħħlu l-informazzjoni l-ġdida fl-ADR eżistenti, b'timbru tad-data, u nota li l-informazzjoni waslet wara d-deċiżjoni. Dan it-tip ta' approċċ iwassal għal "dokument ħaj" li lkoll nistgħu nġeddu. L-aġġornamenti tipiċi jsiru meta nkunu rċevejna informazzjoni grazzi għal membri ġodda tat-tim, jew offerti ġodda, jew riżultati fid-dinja reali mill-użu tagħna, jew wara bidliet minn partijiet terzi, bħal kapaċitajiet tal-fornituri, pjanijiet tal-prezzijiet, ftehimiet tal-liċenzja, eċċ.

## Mistoqsijiet dwar ix-xogħol fi tim għall-ADR


### Min jista' joħloq ADR?

Ikkunsidra oqsma bħal persuni speċifiċi, jew rwoli speċifiċi, jew timijiet speċifiċi, jew dipartimenti speċifiċi; ikkunsidra wkoll jekk hemmx persuni, jew rwoli, jew timijiet, jew dipartiment li jistgħu jikkummissjonaw ADR, jiġifieri jitolbu wieħed li xi ħadd ieħor jikteb. 

Eżempju ta' tweġiba: Kwalunkwe persuna fl-organizzazzjoni tagħna li qrat il-paġna README tar-rekord ta' deċiżjoni arkitettonika tista' tipproponi ADR, jiġifieri tista' tibda tikteb wieħed, u taqsmu mat-tim.

### X'jiġġustifika l-ħolqien ta' ADR?

Ikkunsidra oqsma bħall-modi ta' ħidma tat-timijiet tal-organizzazzjoni tiegħek, l-istruttura tas-sistema tas-software tiegħek, il-koordinazzjoni bejn it-timijiet, il-manutenibbiltà fit-tul, l-interfaces esterni, min trid li jibbenefika, u affarijiet simili. 

Eżempju ta' tweġiba: Irridu noħolqu ADR meta rridu li l-iżviluppaturi futuri jifhmu l-"għaliex" ta' dak li qed nagħmlu.

### X'jiġġustifika li ma jinħolqx ADR?

Ikkunsidra oqsma bħal deċiżjonijiet li mhumiex dwar l-arkitettura, jew li huma ċkejkna bħal riskju minimu jew awtonomi jew ta' żviluppatur wieħed, jew li diġà huma koperti bis-sħiħ x'imkien ieħor bħal fi standards jew politiki jew dokumentazzjoni, jew li huma temporanji bħal soluzzjonijiet alternattivi jew provi tal-kunċett jew esperimenti. 

Eżempju ta' tweġiba: Irridu naqbżu ADR meta deċiżjoni hija limitata fl-ambitu u fiż-żmien u fir-riskju u fl-ispiża, jew diġà hija koperta x'imkien ieħor.

### X'inhu ċ-ċiklu tal-ħajja ta' ADR?

Ikkunsidra oqsma bħall-proċess tal-ħolqien, il-proċess tar-riċerka, il-proċess tat-teħid tad-deċiżjoni, il-proċess tal-implimentazzjoni, u l-proċess tat-tmiem. Ikkunsidra kif tittraċċa ċ-ċiklu tal-ħajja tal-ADR maż-żmien, bħal kif tmexxi l-ADR minn stat għall-ieħor, u wkoll kif tikkomunika dan lill-partijiet interessati. 

Eżempju ta' tweġiba: Irridu li ADR ikollu ħames stadji taċ-ċiklu tal-ħajja: Bidu → Riċerka → Evalwazzjoni → Implimentazzjoni → Manutenzjoni → Tmiem.

### X'inhuma l-kriterji għall-passi taċ-ċiklu tal-ħajja ta' ADR?

Ikkunsidra oqsma bħal kriterji ta' aċċettazzjoni għal ADR, jiġifieri kif taf li huwa tajjeb biżżejjed biex jipprogressa minn pass taċ-ċiklu tal-ħajja għall-ieħor? Il-problema hija spjegata b'mod ċar? Intlaqgħu l-alternattivi? Il-kompromessi huma mifhuma u dokumentati biżżejjed?
Il-kuntest rilevanti kollu qiegħed f'postu? Il-partijiet interessati rilevanti kollha huma involuti? Il-feedback kollu ġie inkorporat? 

Eżempju ta' tweġiba: Irridu li ADR jitpoġġa għall-vot mill-partijiet interessati meta t-tim attiv ikun 1) lesta r-riċerka tiegħu, 2) lesta l-evalwazzjoni tiegħu, 3) ippubblika l-proposta tal-ADR lill-partijiet interessati b'talba għal kummenti u b'limitu ta' ġimgħa, 4) il-kummenti kollha tal-partijiet interessati jkunu ġew inkorporati u indirizzati.

### X'rwoli u responsabbiltajiet jinteraġixxu ma' ADR?

Ikkunsidra rwoli bħal min jipproponi, ir-riċerkatur, l-evalwatur, ir-reviżur, l-approvatur, il-persuna li żżomm, u affarijiet simili. Ikkunsidra responsabbiltajiet bħall-komunikazzjoni mal-partijiet interessati, l-assigurazzjoni li l-aspettattivi jintlaħqu, il-qsim fuq il-websajt jew l-intranet, u r-reviżjoni tax-xogħol perjodikament u speċjalment meta jseħħu bidliet rilevanti.

Eżempju ta' tweġiba: Irridu li kull ADR dejjem ikollu persuna ta' kuntatt primarja, persuna ta' kuntatt sekondarja, u tim responsabbli; dawn huma responsabbli għall-komunikazzjonijiet, il-pubblikazzjonijiet, il-manutenzjoni, ir-reviżjoni perjodika mill-inqas darba fis-sena, u t-tmiem eventwali kif meħtieġ.

### Kif tinteraġixxi l-governanza ma' ADR?

Ikkunsidra oqsma bħall-modi ta' ħidma tal-organizzazzjoni tiegħek, kwalunkwe ħtieġa speċjali ta' konformità bħal għal aspetti legali jew aspetti tar-riżorsi umani, kif tixtieq timmaniġġja l-kunsens kontra l-kunflitt kontra l-eskalazzjoni. Hemm oqsma jew persuni jew timijiet li jistgħu jkollhom aktar influwenza minn oħrajn dwar ADR, bħal li jkunu jistgħu japprovawh, jew jivvutaw fuqu, jew jipponu veto fuqu?

Eżempju ta' tweġiba: Il-governanza ta' ADR hija f'dan l-ordni ta' prijorità: is-CEO, is-CTO, is-CLO, it-tim li jimplimenta ADR, l-esperti fit-tim li huma l-aktar kapaċi dwar l-AD. Ħadd ieħor ma għandu governanza sakemm ma jkunx deskritt fl-ADR. 

### X'prinċipji jinteraġixxu ma' ADR?

Ikkunsidra oqsma bħall-modi ta' ħidma tal-organizzazzjoni tiegħek li jinkludu li tiċċaqlaq malajr kontra li tiċċaqlaq bil-mod, għal kunsens fid-deċiżjonijiet kontra kunflitt fid-deċiżjonijiet, u għal preferenzi dwar ir-riskju kontra preferenzi dwar is-sikurezza, diskussjoni pubblika kontra diskussjoni privata, u affarijiet simili.

Eżempju ta' tweġiba: Nużaw il-prinċipji tat-tmexxija ta' preferenza għall-azzjoni, nkunu ma' qbiela u nikkommettu (disagree-and-commit), stimi ta' 70% huma tajbin biżżejjed għal deċiżjonijiet faċilment riversibbli u faċilment iżolabbli, u modi ta' ħidma pubbliċi bl-eċċezzjoni ta' informazzjoni kunfidenzjali kif deskritt fil-ftehim ta' kunfidenzjalità tal-organizzazzjoni tagħna.

## Kunċetti tal-pass li jmiss għall-ADR

[Arc42](https://arc42.org/) iwieġeb żewġ mistoqsijiet b'mod pragmatiku u jista' jiġi adattat għall-bżonnijiet speċifiċi tiegħek. X'għandek tiddokumenta/tikkomunika dwar l-arkitettura tiegħek? Kif għandek tiddokumenta/tikkomunika? Arc42 jinkludi rekords ta' deċiżjoni arkitettonika flimkien ma' gwida dwar għanijiet, restrizzjonijiet, kuntesti, kwalità, riskji, u aktar.

[Il-mudell C4](https://c4model.com/) huwa approċċ faċli biex titgħallmu, favorevoli għall-iżviluppaturi, għat-tpinġija ta' dijagrammi tal-arkitettura tas-software. C4 huwa sett ta' dijagrammi ġerarkiċi għall-kuntest, il-kontenituri, il-komponenti, il-kodiċi, flimkien ma' dijagrammi ta' appoġġ għall-pajsaġġ tas-sistema, id-dinamika, u d-deployment.

## Dijagrammi & vedute & perspettivi tal-arkitettura

Dijagramma tal-arkitettura tissejjaħ "veduta tal-arkitettura".

"Veduta tal-arkitettura" hija istanza ta' "perspettiva tal-arkitettura".

"Perspettiva tal-arkitettura" għandha udjenza speċifika b'tħassib speċifiku f'moħħha.

Eżempji ta' perspettivi tal-arkitettura, eżempji ta' vedute, u eżempji ta' dijagrammi:

- Kapaċitajiet tan-Negozju

- Proċessi tan-Negozju ta' Livell Għoli

- [Value Streams](https://en.wikipedia.org/wiki/Value_stream)

- Funzjonijiet tas-Software mappati fuq komponenti tal-applikazzjoni

- Dijagramma tal-Kuntest tal-[Mudell C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- Dijagramma tal-Kontenituri tal-[Mudell C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- [Dijagramma Entità-Relazzjoni](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) biex jiġu mappati entitajiet tad-data fuq komponenti tal-applikazzjoni

- [Dijagrammi tas-Sekwenza](https://en.wikipedia.org/wiki/Sequence_diagram) biex jiddeskrivu flussi funzjonali fi ħdan sistemi u għal integrazzjonijiet

- Dijagrammi [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) biex jiddeskrivu flussi tad-data fuq komponenti tal-applikazzjoni

- Dijagrammi [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) biex jiddeskrivu proċessi tan-negozju / xenarji tal-utenti

- Dijagrammi [Identity and Access Management](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM)

- Dijagrammi [Role-Based Access Control](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) b'rwoli għal kull komponent tal-applikazzjoni

- Dijagrammi [Attribute-Based Access Control](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) b'attributi għal kull komponent tal-applikazzjoni

- Dijagrammi tal-privatezza

Dijagrammi relatati:

- Dijagramma tal-Każijiet ta' Użu turi każijiet ta' użu lill-maniġment/lill-klijenti, li jiġi qabel ir-rekwiżiti, li jiġu qabel l-arkitettura tas-software.

- Dijagramma tad-Deployment turi l-hardware/il-kompjuters fiżiċi li lejhom jiġu mqiegħda l-komponenti tas-software.
- Dijagramma tal-Fluss tad-Data turi kif id-data tiċċaqlaq mis-sistema u tiġi trasformata.
- Dijagramma tas-Sekwenza tintuża biex turi kif protokolli bħal HTTP jaħdmu fuq assi taż-żmien.

- Dijagramma tal-Attività tpinġi l-workflow ta' attivitajiet li tieħu sistema tas-software, bħal NPC AI.

## Funzjonijiet ta' idoneità għad-deċiżjonijiet bħala kodiċi

Il-funzjonijiet ta' idoneità (fitness functions) huma kontrolli awtomatizzati oġġettivi, miktuba bil-kodiċi tal-programmazzjoni, li jivverifikaw li d-deċiżjonijiet qed jinżammu.

- Il-funzjonijiet ta' idoneità jagħmlu d-deċiżjonijiet ittestjabbli u assigurabbli.

- Il-funzjonijiet ta' idoneità għad-deċiżjonijiet jistgħu jgħinu ħafna fl-assigurazzjoni tal-kwalità, fil-proċessi regolatorji, u fl-għanijiet tal-governanza.

### Kif il-funzjonijiet ta' idoneità jieħdu sehem mad-deċiżjonijiet

Rekord ta' deċiżjoni jiddokumenta d-deċiżjoni, filwaqt li funzjoni ta' idoneità tassigura d-deċiżjoni.

- Deċiżjoni b'eżempju: Nużaw l-event sourcing għar-rekwiżiti tal-awditjar.

- Funzjoni ta' idoneità b'eżempju: Nużaw is-server tal-integrazzjoni kontinwa biex nittestjaw li kull bidla fl-istat trid tipproduċi avvenimenti.

### Għaliex il-funzjonijiet ta' idoneità jgħinu d-deċiżjonijiet

Kejl oġġettiv: Il-funzjonijiet ta' idoneità jgħaddu jew jonqsu, għalhekk ix-xogħol jidher u jkun ċar.

Użu kontinwu: Il-funzjonijiet ta' idoneità huma r-regoli ħajjin tiegħek, li jitħaddmu f'kull kommit u build.

Fiduċja biex tagħmel refactoring: Il-funzjonijiet ta' idoneità jaqbdu awtomatikament l-iżbalji fir-regoli tad-deċiżjonijiet.

Governanza skalabbli: Il-funzjonijiet ta' idoneità jassiguraw l-istandards mingħajr ma joħolqu konġestjonijiet.

### Il-funzjonijiet ta' idoneità jistgħu jużaw l-AI?

Il-funzjonijiet ta' idoneità jistgħu jisfruttaw l-LLMs tal-AI għad-deċiżjonijiet billi jistaqsu mistoqsijiet dwar ix-xogħol tiegħek,
bħall-pjanijiet, il-kodiċi, l-iskemi, l-API, u aktar:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Ittestjar tal-unitajiet tal-arkitettura

[ArchUnit](https://www.archunit.org/): iċċekkja r-regoli tal-arkitettura tal-kodiċi Java billi tuża kwalunkwe framework tal-unit test tal-Java sempliċi.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): iċċekkja r-regoli tal-arkitettura tal-kodiċi TypeScript u tal-kodiċi JavaScript billi tuża Jest, Vitest, Jasmine, eċċ.

## Guardrails tad-deċiżjonijiet għall-pull requests

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
jippreżenta awtomatikament ir-rekords ta' deċiżjoni t-tajba fil-mument it-tajjeb — meta
żviluppatur ikun qed jimmodifika b'mod attiv il-kodiċi li dawk id-deċiżjonijiet ikopru. Minflok
ma nittamaw li l-iżviluppaturi jaqraw folder tad-dokumenti qabel jgħaqqdu, il-kuntest rilevanti
jidher direttament fuq il-pull request.

Dan jaħdem għal kull tip ta' rekord ta' deċiżjoni: deċiżjonijiet arkitettoniċi, deċiżjonijiet
dwar id-data, deċiżjonijiet ta' konformità, deċiżjonijiet kliniċi u mediċi, deċiżjonijiet ta'
sigurtà, u aktar.

Jaħdem ma' kwalunkwe sistema CI (GitLab, Jenkins, CircleCI) u bħala pre-commit hook.
Open source. Liċenzja MIT.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) huwa GitHub
Action li jfalli pull request meta jinbidlu perkorsi tal-kodiċi taħt osservazzjoni mingħajr
ma jiżdied jew jiġi aġġornat rekord ta' deċiżjoni arkitettonika. Id-dispensi huma espliċiti: linja
`ADR-Exempt:` b'raġuni tgħaddi l-gate u tinkiteb fis-sommarju tal-ħidma. Newtrali għall-mudelli, bla
dipendenzi. Open source. Liċenzja MIT.

## Aktar informazzjoni

Introduzzjoni:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Mudelli:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Fil-fond:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - lezzjoni xahrija b'xejn dwar l-arkitettura tas-software

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Għodod:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Gwida Speċifika għall-Kumpaniji:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Eżempji:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Vidjows:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcasts:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Kotba:

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

Ara wkoll:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Format YAML/JSON newtrali għall-fornituri, li jinqara mill-magni, biex jirrappreżenta deċiżjonijiet b'raġunament espliċitu, suppożizzjonijiet, stat konjittiv, u kompromessi. Jikkumplimenta l-ADR billi jżid raġunament strutturat u validabbli mad-dokumentazzjoni tad-deċiżjonijiet.
