# Proċess tar-Rekords ta' Deċiżjoni Arkitettonika ta' AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Rekord ta' deċiżjoni arkitettonika (ADR) huwa dokument li jiddeskrivi għażla li t-tim jagħmel dwar aspett sinifikanti tal-arkitettura tas-software li qed jippjana jibni. Kull ADR jiddeskrivi d-deċiżjoni arkitettonika, il-kuntest tagħha, u l-konsegwenzi tagħha. L-ADR għandhom stati u għalhekk isegwu ċiklu tal-ħajja. Għal eżempju ta' ADR, ara l-appendiċi.

Il-proċess tal-ADR jipproduċi ġabra ta' rekords ta' deċiżjoni arkitettonika. Din il-ġabra toħloq ir-reġistru tad-deċiżjonijiet. Ir-reġistru tad-deċiżjonijiet jipprovdi l-kuntest tal-proġett kif ukoll informazzjoni dettaljata dwar l-implimentazzjoni u d-disinn. Il-membri tal-proġett jaqraw malajr l-intestaturi ta' kull ADR biex jaqbdu ħarsa ġenerali lejn il-kuntest tal-proġett. Jaqraw l-ADR biex jidħlu fil-fond fl-implimentazzjonijiet tal-proġett u fl-għażliet tad-disinn.

Meta t-tim jaċċetta ADR, dan isir immutabbli. Jekk għarfien ġdid jirrikjedi deċiżjoni differenti, it-tim jipproponi ADR ġdid. Meta t-tim jaċċetta l-ADR il-ġdid, dan jieħu post l-ADR preċedenti.

## Ambitu tal-proċess tal-ADR

Il-membri tal-proġett għandhom joħolqu ADR għal kull deċiżjoni sinifikanti mil-lat arkitettoniku li taffettwa l-proġett jew il-prodott tas-software, inklużi dawn li ġejjin (Richards u Ford 2020):

* Struttura (pereżempju, xejriet bħall-microservices)

* Rekwiżiti mhux funzjonali (sigurtà, disponibbiltà għolja, u tolleranza għall-ħsarat)

* Dipendenzi (akkoppjar tal-komponenti)

* Interfaces (API u kuntratti ppubblikati)

* Tekniki ta' kostruzzjoni (librerijiet, frameworks, għodod, u proċessi)

* Ir-rekwiżiti funzjonali u mhux funzjonali huma l-aktar inputs komuni tal-proċess tal-ADR.


## Kontenut tal-ADR

Meta t-tim jidentifika ħtieġa għal ADR, membru tat-tim jibda jikteb l-ADR abbażi ta' mudell għall-proġett kollu. (Ara l-organizzazzjoni ADR fuq GitHub għal mudelli bħala eżempju.) Il-mudell jissimplifika l-ħolqien tal-ADR u jiżgura li l-ADR jiġbor l-informazzjoni rilevanti kollha. Bħala minimu, kull ADR għandu jiddefinixxi l-kuntest tad-deċiżjoni, id-deċiżjoni nnifisha, u l-konsegwenzi tad-deċiżjoni għall-proġett u għar-riżultati konsenjabbli tiegħu. (Għal eżempji ta' dawn is-sezzjonijiet, ara l-appendiċi.) Wieħed mill-aktar aspetti b'saħħithom tal-istruttura tal-ADR huwa li tiffoka fuq ir-raġuni tad-deċiżjoni aktar milli fuq kif it-tim implimentaha. Il-fehim tar-raġuni għaliex it-tim ħa d-deċiżjoni jagħmilha eħfef għall-membri l-oħra tat-tim biex jadottaw id-deċiżjoni, u jipprevjeni lil arkitetti oħra li ma kinux involuti fil-proċess tat-teħid tad-deċiżjoni milli jwaqqgħu dik id-deċiżjoni fil-futur.


## Proċess ta' adozzjoni tal-ADR

Kull membru tat-tim jista' joħloq ADR, iżda t-tim għandu jistabbilixxi definizzjoni ta' sjieda għal ADR. Kull awtur li huwa s-sid ta' ADR għandu jżomm u jikkomunika b'mod attiv il-kontenut tal-ADR. Biex tkun ċara din is-sjieda, din il-gwida tirreferi għall-awturi tal-ADR bħala s-sidien tal-ADR fit-taqsimiet li ġejjin. Membri oħra tat-tim jistgħu dejjem jikkontribwixxu għal ADR. Jekk il-kontenut ta' ADR jinbidel qabel ma t-tim jaċċettah, is-sid għandu japprova dawn il-bidliet.

Wara li t-tim jidentifika deċiżjoni arkitettonika u s-sid tagħha, is-sid tal-ADR jipprovdi l-ADR fl-istat **Proposed** (Proposta) fil-bidu tal-proċess. L-ADR fl-istat Proposed ikunu lesti għar-reviżjoni.

Is-sid tal-ADR imbagħad jibda l-proċess tar-reviżjoni għall-ADR. L-għan tal-proċess tar-reviżjoni tal-ADR huwa li jiġi deċiż jekk it-tim jaċċettax l-ADR, jiddeterminax li jeħtieġ aktar xogħol, jew jirrifjutax l-ADR. It-tim tal-proġett, inkluż is-sid, jirrevedi l-ADR. Il-laqgħa tar-reviżjoni għandha tibda b'perjodu ddedikat biex jinqara l-ADR. Bħala medja, 10 sa 15-il minuta għandhom ikunu biżżejjed. Matul dan iż-żmien, kull membru tat-tim jaqra d-dokument u jżid kummenti u mistoqsijiet biex jimmarka suġġetti mhux ċari. Wara l-fażi tar-reviżjoni, is-sid tal-ADR jaqra u jiddiskuti kull kumment mat-tim.

Jekk it-tim isib punti ta' azzjoni biex itejjeb l-ADR, l-istat tal-ADR jibqa' **Proposed**. Is-sid tal-ADR jifformula l-azzjonijiet, u, f'kollaborazzjoni mat-tim, iżid inkarigat għal kull azzjoni. Kull membru tat-tim jista' jikkontribwixxi u jirrisolvi l-punti ta' azzjoni. Hija r-responsabbiltà tas-sid tal-ADR li jerġa' jiskeda l-proċess tar-reviżjoni.

It-tim jista' jiddeċiedi wkoll li jirrifjuta l-ADR. F'dan il-każ, is-sid tal-ADR iżid raġuni għar-rifjut biex jiġu evitati diskussjonijiet futuri dwar l-istess suġġett. Is-sid ibiddel l-istat tal-ADR għal **Rejected** (Rifjutat).

Jekk it-tim japprova l-ADR, is-sid iżid timbru taż-żmien, verżjoni, u lista tal-partijiet interessati. Is-sid imbagħad jaġġorna l-istat għal **Accepted** (Aċċettat).

L-ADR u r-reġistru tad-deċiżjonijiet li joħolqu jirrappreżentaw deċiżjonijiet li ħa t-tim u jipprovdu storja tad-deċiżjonijiet kollha. It-tim juża l-ADR bħala referenza matul ir-reviżjonijiet tal-kodiċi u tal-arkitettura kull fejn ikun possibbli. Minbarra l-eżekuzzjoni ta' reviżjonijiet tal-kodiċi, kompiti ta' disinn, u kompiti ta' implimentazzjoni, il-membri tat-tim għandhom jikkonsultaw l-ADR għal deċiżjonijiet strateġiċi għall-prodott.

Bħala prattika tajba, kull bidla fis-software għandha tgħaddi minn reviżjonijiet bejn il-pari u tirrikjedi mill-inqas approvazzjoni waħda. Matul ir-reviżjoni tal-kodiċi, reviżur tal-kodiċi jista' jsib bidliet li jiksru ADR wieħed jew aktar. F'dan il-każ, ir-reviżur jitlob lill-awtur tal-bidla fil-kodiċi biex jaġġorna l-kodiċi, u jaqsam rabta mal-ADR. Meta l-awtur jaġġorna l-kodiċi, dan jiġi approvat mir-reviżuri pari u jiġi magħqud mal-kodiċi bażi ewlenija.


## Proċess ta' reviżjoni tal-ADR

It-tim għandu jittratta l-ADR bħala dokumenti immutabbli wara li t-tim jaċċettahom jew jirrifjutahom. Il-bidliet f'ADR eżistenti jirrikjedu l-ħolqien ta' ADR ġdid, it-twaqqif ta' proċess ta' reviżjoni għall-ADR il-ġdid, u l-approvazzjoni tal-ADR. Jekk it-tim japprova l-ADR il-ġdid, is-sid għandu jbiddel l-istat tal-ADR il-qadim għal **Superseded** (Mibdul).
