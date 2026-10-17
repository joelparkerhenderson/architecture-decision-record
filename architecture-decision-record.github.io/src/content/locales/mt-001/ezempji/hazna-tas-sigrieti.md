# Ħażna tas-sigrieti

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
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Sommarju


### Kwistjoni

Neħtieġu naħżnu s-sigrieti, bħal passwords, ċwievet privati, tokens ta' awtentikazzjoni, eċċ.

Xi whud mis-sigrieti huma orjentati lejn l-utent. Pereżempju, l-iżviluppatur tagħna jrid ikun jista' juża t-telefon mobile tiegħu biex ifittex password ta' servizz.

Xi whud mis-sigrieti huma orjentati lejn is-sistema. Pereżempju, il-pipeline tagħna tal-kunsinna kontinwa jeħtieġ ikun jista' jfittex il-kredenzjali għall-hosting tagħna fil-cloud.


### Deċiżjoni

Bitwarden għal sigrieti orjentati lejn l-utent

Vault minn HashiCorp għal sigrieti orjentati lejn is-sistema.


### Stat

Deċiż. Aħna miftuħin għal alternattivi ġodda hekk kif jinqalgħu.


## Dettalji


### Suppożizzjonijiet

Għal dan l-iskop, u l-istat attwali tagħna, napprezzaw il-konvenjenza orjentata lejn l-utent, bħal apps mobile użabbli.

  * Irridu niżguraw aċċess faċli u mgħaġġel waqt il-mixi, bħal għal iżviluppatur li jagħmel inġinerija tal-affidabbiltà tas-sistema on-call.

  * Irridu nkunu nistgħu naqsmu xi sigrieti fost persuni magħżula, bħal tim.

Mhux qed nippruvaw insolvu għal fornitur uniku, bħal li naħżnu s-sigrieti kollha esklussivament fuq Amazon jew Azure jew Google.

Ma rridux approċċi ad-hoc bħal "ftakar fih" jew "ikteb fuq nota" jew "sib il-mod tiegħek stess kif taħżnu".

Il-mudell tas-sigurtà tagħna għal dan l-iskop huwa tajjeb bl-użu ta' fornituri COTS rispettati sew, bħal għodod SaaS tal-ġestjoni tal-passwords.


### Restrizzjonijiet

Bħalissa rridu xi ħaġa li hija faċli jiġifieri m'hemmx bżonn li niktbu kodiċi, m'hemmx bżonn li ninstallaw servers, m'hemmx bżonn ta' impenn kbir, m'hemmx bżonn li kulħadd jiġi standardizzat.


### Pożizzjonijiet

Ikkunsidrajna:

1. Maniġers tal-passwords lesti għall-użu orjentati lejn l-utent: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG, eċċ.

2. Maniġers COTS tal-passwords orjentati lejn is-sistema: AWS KMS, Vault minn HashiCorp, EnvKy, Secret Server minn Thycotic, Devolutions Password Server, Confidant minn Lyft.

3. Approċċi orjentati lejn il-qsim: l-użu ta' dokument kondiviż ta' Google, jew kanal kondiviż ta' Slack, jew folder kondiviż tan-netwerk, eċċ.

4. Approċċi ad-hoc b'teknoloġija baxxa, bħal li wieħed jiftakar, jikteb nota, jew jiddependi fuq kull utent biex isib l-approċċ tiegħu stess.


### Argument

Bitwarden, LastPass, 1Password, u Dashlane huma kollha prodotti kummerċjali lesti għall-użu.

  * Tipi simili ta' karatteristiċi għall-utenti, it-timijiet, l-organizzazzjonijiet, eċċ.

  * Kapaċità desktop għal Windows u Mac, u kapaċità mobile għal Android u iOS.

  * Estensjonijiet tal-browser għal Chrome u Firefox, għall-mili awtomatiku tal-forms, eċċ.

Bitwarden għandu żewġ vantaġġi fuq l-oħrajn:

  * Bitwarden huwa open source, li jfisser li s-sigurtà tista' tiġi riveduta mill-pari u wkoll il-kumpanija hija apprezzata b'mod wiesa' mill-iżviluppaturi orjentati lejn is-sigurtà.

  * L-aneddoti minn ħaddiema tas-software jiddeskrivu preferenza sinifikanti għal Bitwarden fuq l-oħrajn.

Eżempju tipiku ta' artiklu tajjeb: https://jcs.org/2017/11/17/bitwarden

Sit tipiku tal-votazzjoni side-by-side: https://stackshare.io/stackups/bitwarden-vs-dashlane

Qed inpostponu KeyPass, pass, GPG, eċċ. għax hemm kumplessità addizzjonali. Dawn kollha jidhru soluzzjonijiet tajbin għall-utenti tekniċi. GPG jidher speċjalment tajjeb għal utenti tekniċi li jridu kapaċitajiet orjentati lejn il-kmandi bejn sistemi differenti.

Qed inpostponu KMS għax għandu lock-in ma' fornitur uniku.

Nagħżlu Vault għall-bżonnijiet orjentati lejn is-sistema, għax ir-reviżjonijiet huma pożittivi b'mod sorprendenti, u għax HashiCorp għandha rekord eċċellenti ta' software u appoġġ tal-ogħla kwalità.

Nivvetaw l-approċċi ta' qsim bħal permezz ta' dokumenti kondiviżi, kanali kondiviżi, folders kondiviżi tan-netwerk, eċċ. Dawn ma jipprovdux il-kwalitajiet ta' sigurtà li rridu.

Nivvetaw l-approċċi ad-hoc b'teknoloġija baxxa, għax kulħadd jaqbel li mhuwiex triq 'il quddiem fit-tul.


### Implikazzjonijiet

L-iżviluppaturi jistgħu jkollhom bżonn jittraċċaw is-sigrieti f'żewġ postijiet: Bitwarden għal aċċess orjentat lejn l-utent, u Vault għal aċċess orjentat lejn is-sistema.


## Relatati


### Deċiżjonijiet relatati

Id-deċiżjoni dwar liema server CI/CD trid tinkludi prova ta' kapaċità għall-aċċess tas-sigrieti.

Se neħtieġu niddeċiedu kif nimmaniġġjaw is-sigrieti, f'termini ta' politiki, rotazzjonijiet, organizzazzjonijiet, eċċ.


### Rekwiżiti relatati

Is-sigrieti se jkollhom rekwiżiti relatati għall-konformità, l-awditjar, u l-onboarding/offboarding tar-riżorsi umani.


### Artefatti relatati

Nistennew li jista' jkun li neżportaw xi sigrieti għal varjabbli tal-ambjent.


### Prinċipji relatati

Faċilment riversibbli.

Faċilment parallel jiġifieri huwa faċli li tuża varjetà ta' maniġers tal-passwords.

Rħis biex tipprova jiġifieri hemm prova b'xejn u l-ebda impenn.


## Noti

In-noti tal-evalwazzjoni hawn. In-noti huma kollha kummenti pubbliċi fuq diversi bordijiet ta' diskussjoni devops.


### Vault by HashiCorp

Vault huwa eżattament dak li trid hawn. 

Tarmix Vault biss fil-produzzjoni, madankollu, waqqfu l-ewwel f'ambjent tat-test, għax id-dokumentazzjoni ta' HashiCorp tista' tkun pjuttost nieqsa anke jekk il-prodotti tagħhom huma tal-għaġeb.

Kurva tat-tagħlim wieqfa ħafna u mhuwiex trivjali biex jitwaqqaf. 

Is-setup inizjali huwa kemmxejn uġigħ. Jiswa l-ħsieb madankollu, u l-komunità se tappoġġah biżżejjed biex tgħaddi.

Dokumenti orribbli imma hemm ħafna gwidi online ta' nies li waqqfuh u jekk tpoġġi ftit minnhom flimkien ikollok setup li jaħdem.

Is-setup inizjali ħa xi tbaħbiħ bil-helm charts tagħhom (vault u consul). Għalkemm teknikament tista' tuża ħafna back-ends oħra, verament verament ma nirrakkomandax. Il-back-end/consul jista' jkun żgħir ħafna jekk m'għandekx ħafna data x'taħżen.

Żgur kun komdu/familjari bl-użu tas-CLI, għax il-GUI hija aktar bħal portal ta' proof-of-concept/reklamar għall-edizzjoni enterprise tagħhom.

Il-fatt li ma tistax sempliċement "timlieh" huwa uġigħ. Pereżempju jekk għandek 5 oqsma trid iżżid manwalment kull qasam għal kull element. Allura mhuwiex bħal li tiddefinixxi oqsma minn qabel għal kategorija speċifika, u timla dawk l-oqsma għall-elementi kollha f'dik il-kategorija, huwa aktar bħal "tiġġenera kollox kull darba", li (fil-fehma tiegħi) huwa uġigħ fil-qadd.

Jista' jkun li trid tħares lejn goldfish bħala UI fuq Vault. Jagħmilha pjuttost sabiħa biex iġġib lit-tim tiegħek a bord miegħu. Għandhom ukoll demo. 1. Waqqaf consul. 2. Waqqaf vault li jindika lejn consul. 3. Waqqaf goldfish li jindika lejn vault. 3. Waqqaf xi cron job biex iħaddem consul snapshot għal backups.



### LastPass

LastPass Teams. Nużawh, għandu templates personalizzati, ACL, ma jonqos xejn fl-opinjoni tiegħi.

Implimentajt LastPass fl-organizzazzjoni tiegħi u nagħtih C+/B-. L-akbar kwistjoni dan l-aħħar hija nuqqas ta' affidabbiltà. Fl-aħħar 90 jum kien hemm sigħat multipli fejn il-vaults ġew imġiegħla f'modalità offline. Dan mhuwiex ideali għall-organizzazzjoni tiegħi minħabba li għandi, litteralment, 4,000+ password maħżuna f'20+ folder kondiviż. Kif tista' timmaġina b'daqshekk passwords mill-inqas ftit jiġu aġġornati jew miżjuda kuljum. Għandna pjan DR jekk il-kwistjonijiet idumu aktar minn siegħa jew tnejn: script jiffirma u jikkripta dump CSV tal-vault kull lejl li jista' jiġi importat f'keepass.

LastPass kellu blips mhux irrappurtati ta' servizz degradat: il-login 'jaħdem' imma ma jiġbidx is-siti, karatteristiċi każwali maqsuma fil-pannell tal-amministratur, u ma jaqsamx iċ-ċwievet kif suppost għal folders kondiviżi ġodda tal-ogħla livell. Għandi utent speċifiku ta' 'key push'/backup li hu f'kull grupp. Normalment id-dħul bħala dak l-utent jirranġa kwalunkwe kwistjoni ta' qsim taċ-ċwievet imma mhux meta s-servizz ikun degradat minkejja dak li tgħid il-paġna tal-istatus...

Għall-integrazzjoni tista' tkun faċli jekk għandek ACLs xierqa b'mudell tal-inqas privileġġ eż. jekk utent għandu read & write u read only fuq entrata jew folder jingħata biss permessi read only. Sfortunatament l-ACLs tal-organizzazzjoni tiegħi mhumiex l-aħjar għalhekk spiċċajt bl-użu tal-API tal-provvediment JSON u ~500 linja ta' python minħabba n-natura dipendenti tal-mijiet ta' ACLs tagħna li ma jimmappjawx tajjeb mal-mudell tal-inqas privileġġ. Spiċċajt niġbor l-ACLs kollha li kien fihom utent u nagħmel mixja ta' dipendenzi ta' xorta.

Jekk l-istruttura tal-ACL jew tal-gruppi tiegħek diġà nbniet bi struttura tal-inqas privileġġ f'moħħha l-għodda tas-sinkronizzazzjoni AD/LDAP għal Windows se taħdem tajjeb.

Kellem it-tim tal-bejgħ tagħhom u jistgħu jagħtuk prova Enterprise itwal. Kun żgur li tifhem bis-sħiħ il-limitazzjonijiet tagħha qabel ma tieħu l-pass. Kellna numru tajjeb ta' uġigħ tat-tkabbir imma minbarra waqfiet jew indeboliment min-naħa tas-server kien inkredibbilment bla xkiel.


### Bitwarden

Bitwarden għandu għodod sbieħ madwaru (WebUI, CLI, Mobile, Desktop). Self-hosted u pjuttost faċli biex jiġi ssettjat. Dokumentazzjoni pjuttost tajba u għodda rakkomandata minn PrivacyTools.


### EnvKey

https://www.envkey.com/ Huwa saas. Verament faċli biex jiġi implimentat, integrat u mmaniġġjat.

Karatteristiċi:

  * Jipproteġi ċwievet API u kredenzjali.

  * Iżomm il-konfigurazzjoni sinkronizzata kullimkien.

  * Ġestjoni intelliġenti tal-konfigurazzjoni u tas-sigrieti ikkriptata end-to-end. 

  * Jevita qsim mhux sigur u firxa tal-konfigurazzjoni. 

  * Jintegra fi ftit minuti.

Kapaċitajiet:

  * Immaniġġja l-konfigurazzjoni u l-livelli ta' aċċess għall-apps, l-ambjenti, u t-timijiet kollha tiegħek f'post wieħed.

  * Ikkonfigura kwalunkwe ambjent ta' żvilupp jew server b'varjabbli waħda tal-ambjent.

Vantaġġi:

  * Paġna ewlenija tajba.

  * Proposta ta' valur ċara.

  * Web app eċċellenti viżwalment.

  * Data ta' eżempju superjuri eż. Algolia, AWS, Datadog, GitHub, Stripe, eċċ.

  * Tkellimt mal-fundatur għal 30 minuta dwar il-kumpanija, l-UI, eċċ. Dane jinstema' infurmat tajjeb, onest dwar il-vantaġġi/żvantaġġi, u sieħeb vijabbli.

  * Il-kumpanija hija essenzjalment kumpanija tipika ta' Y Combinator, b'fundatur wieħed. Qajmet K f'2018-01.

  * Il-fokus huwa fuq il-wasla għal karatteristiċi enterprise, speċjalment li tgħaddi minn EnvKey cloud-hosting għal jew on-prem jew BYOC.

  * Triq potenzjali 'l quddiem li tibda b'EnvKey għall-faċilità tal-użu, imbagħad aktar tard (jew b'mod parallel) iżżid Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant huwa servizz open source tal-ġestjoni tas-sigrieti li jipprovdi ħażna u aċċess faċli għall-utent għas-sigrieti b'mod sigur, mill-iżviluppaturi f'Lyft.

Awtentikazzjoni KMS: Confidant isolvi l-problema tal-awtentikazzjoni tal-"bajda u d-denb" billi juża AWS KMS u IAM biex jippermetti lir-rwoli IAM jiġġeneraw tokens sikuri ta' awtentikazzjoni li jistgħu jiġu vverifikati minn Confidant. Confidant jimmaniġġja wkoll KMS grants għar-rwoli IAM tiegħek, li jippermettu lir-rwoli IAM jiġġeneraw tokens li jistgħu jintużaw għall-awtentikazzjoni bejn servizzi, jew biex jgħaddu messaġġi kkriptati bejn servizzi.

Kriptaġġ at-rest ta' sigrieti vverżjonati: Confidant jaħżen is-sigrieti b'mod append-only f'DynamoDB, u jiġġenera ċavetta tad-data unika ta' KMS għal kull reviżjoni ta' kull sigriet, bl-użu ta' kriptografija awtentikata simetrika Fernet.

Interface tal-web faċli għall-utent għall-ġestjoni tas-sigrieti: Confidant jipprovdi interface tal-web AngularJS li tippermetti lill-utenti aħħarin jimmaniġġjaw faċilment is-sigrieti, il-mapping tas-sigrieti għas-servizzi u l-istorja tal-bidliet.


### Devolutions Password Server

https://server.devolutions.net/

Issigura, immaniġġja, u immonitorja l-aċċess għal kontijiet u sessjonijiet privileġġjati.

Vault tal-passwords komprensiv u sigur ħafna li jippermettilek tikkontrolla l-aċċess għall-kontijiet privileġġjati tiegħek, filwaqt li jtejjeb ukoll il-viżibbiltà ġenerali tan-netwerk għas-sysadmins u jipprovdi esperjenza bla xkiel għall-utenti aħħarin.

Karatteristiċi: vault ċentralizzat tal-passwords tal-organizzazzjoni, vault privat speċifiku għall-utent, maniġer tal-passwords, injezzjoni tal-kredenzjali,
integrazzjoni ma' Active Directory, kontroll tal-aċċess ibbażat fuq ir-rwoli, awtentikazzjoni b'żewġ fatturi, lest għall-intrapriża, restrizzjonijiet tal-IP, kapaċitajiet ta' ġestjoni, ġeneratur awtomatizzat tal-passwords, aċċess permezz ta' app mobile, storja tal-passwords, rapporti tal-aċċess, twissijiet bl-email.

  * jappoġġa kriptaġġ tad-data

  * jappoġġa skemi multipli ta' awtentikazzjoni inklużi LDAP, O365, u utenti Lokali B'appoġġ għal MFA minn sorsi multipli

  * repożitorji/vaults multipli b'kontrolli tal-aċċess dettaljati għal timijiet multipli

  * UI moderna tal-web

  * vaults privati ta' kredenzjali u konnessjonijiet għal kredenzjali/konnessjonijiet personali

  * apps mobile għal IOS/Android

  * logs tal-awditjar għal kull entrata, min/x'/meta b'prompt fakultattiv għal għaliex qed jaċċessaw

  * templates personalizzabbli (għalkemm jappoġġaw mijiet ta' tipi ta' konnessjoni nattivament)

  * ħafna aktar karatteristiċi u klijent thick għal Windows/Mac (Remote Desktop Manager) li tista' tissinkronizza miegħu li jespandi ħafna l-għażliet...konnessjonijiet b'klikk wieħed

  * il-prezzijiet mhumiex ħżiena kemm hekk - sa 15-il utent huwa  fis-sena għas-password server


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Karatteristiċi tal-verżjoni on-premise: 

  * Kontroll totali fuq is-sistemi u l-infrastruttura tas-sigurtà end-to-end tiegħek

  * Iddeploja s-software fid-data center on-premise tiegħek jew fl-istanza tiegħek stess ta' virtual private cloud

  * Issodisfa obbligi legali u regolatorji li jeħtieġu li d-data u s-sistemi kollha jibqgħu on-premise

Karatteristiċi tal-verżjoni tal-cloud:

  * Mudell software-as-a-service li jippermettilek tirreġistra u tibda minnufih

  * Skalabbiltà elastika hekk kif tikber

  * Kontrolli u ridondanza mogħtija minn Azure b'SLA ta' 99.9% uptime

Feedback tal-utenti:

  * Konna nużaw dak il-prodott. Kien evitat faċilment u r-regoli jaħdmu biss għal nies intelliġenti. Utenti għażżenin jew boloh jistgħu faċilment jarmawh fiż-żona tat-tim. Il-prezzijiet huma negozjabbli meta titkellem magħhom.

  * Tista' tħaddmu bl-użu ta' SQL express u kaxxa Win 7. 

  * Rħis.
