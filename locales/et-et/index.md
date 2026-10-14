# Arhitektuuriotsuse kirje (ADR)

Arhitektuuriotsuse kirje (ADR) on dokument, mis jäädvustab olulise arhitektuuriotsuse koos selle konteksti ja tagajärgedega.

> [!IMPORTANT]
> Tee nende ressursside suhtes oma hoolsuskontroll enne, kui kasutad neid kriitilistes süsteemides.

Sisukord:

- [Mis on arhitektuuriotsuse kirje?](#mis-on-arhitektuuriotsuse-kirje)
- [Kuidas ADR-e kasutama hakata](#kuidas-adr-e-kasutama-hakata)
- [Kuidas ADR-e kasutama hakata tööriistadega](#kuidas-adr-e-kasutama-hakata-tööriistadega)
- [Kuidas ADR-e kasutama hakata gitiga](#kuidas-adr-e-kasutama-hakata-gitiga)
- [Claude Code'i oskused ADR-ide jaoks](#claude-codei-oskused-adr-ide-jaoks)
- [Failinimede konventsioonid](#failinimede-konventsioonid)
- [Soovitused heade ADR-ide kirjutamiseks](#soovitused-heade-adr-ide-kirjutamiseks)
- [ADR-i näidismallid](#adr-i-näidismallid)
- [Meeskonnatöö nõuanded ADR-idele](#meeskonnatöö-nõuanded-adr-idele)
- [Meeskonnatöö küsimused ADR-ide jaoks](#meeskonnatöö-küsimused-adr-ide-jaoks)
- [ADR-ide järgmise sammu kontseptsioonid](#adr-ide-järgmise-sammu-kontseptsioonid)
- [Arhitektuuridiagrammid, vaated ja vaatepunktid](#arhitektuuridiagrammid-vaated-ja-vaatepunktid)
- [Otsuste sobivusfunktsioonid koodina](#otsuste-sobivusfunktsioonid-koodina)
- [Otsuste kaitsepiirded tõmbepäringute jaoks](#otsuste-kaitsepiirded-tõmbepäringute-jaoks)
- [Lisateave](#lisateave)

Mallid:

- [Jeff Tyree'lt ja Art Akermanilt pärit otsusekirje mall](mallid/otsusekirje-mall-jeff-tyreelt-ja-art-akermanilt/)
- [Michael Nygardi otsusekirje mall](mallid/otsusekirje-mall-michael-nygardilt/)
- [EdgeX-i otsusekirje mall](mallid/otsusekirje-mall-edgex-ilt/)
- [arc42-lt pärit otsusekirje mall](mallid/otsusekirje-mall-arc42-lt/)
- [Otsusekirje mall aleksandria mustri jaoks](mallid/otsusekirje-mall-aleksandria-mustri-jaoks/)
- [Otsusekirje mall ärijuhtumi jaoks](mallid/otsusekirje-mall-aarijuhtumi-jaoks/)
- [MADR-i projekti otsusekirje mall](mallid/otsusekirje-mall-madr-projektilt/)
- [Otsusekirje mall Planguage'iga](mallid/otsusekirje-mall-planguage-iga/)
- [Paulo Merson otsusekirje mall](https://github.com/pmerson/ADR-template)
- [Olaf Zimmermanni otsusekirje mall](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Gareth Morgani otsusekirje mall](mallid/otsusekirje-mall-gareth-morganilt/)
- [GIG Cymru NHS Walesi otsusekirje mall](mallid/otsusekirje-mall-gig-cymru-nhs-walesilt/)
- [Ignacio Larrañaga otsusekirje mall oluliste tehniliste otsuste jaoks](mallid/otsusekirje-mall-oluliste-tehniliste-otsuste-jaoks/)

Näited:

- [CSS-raamistik](naited/css-raamistik/)
- [Keskkonnamuutujatega seadistamine](naited/keskkonnamuutujatega-seadistamine/)
- [Mõõdikud, seire, hoiatused](naited/maotikud-seire-hoiatused/)
- [Microsoft Azure DevOps](naited/microsoft-azure-devops/)
- [Monorepo või multirepo](naited/monorepo-voi-multirepo/)
- [Programmeerimiskeeled](naited/programmeerimiskeeled/)
- [Saladuste salvestamine](naited/saladuste-salvestamine/)
- [Ajatempli vorming](naited/ajatempli-vorming/)
- [Palju rohkem...](naited/)

## Mis on arhitektuuriotsuse kirje?

**Arhitektuuriotsuse kirje** (ADR) on dokument, mis jäädvustab tehtud olulise arhitektuuriotsuse koos selle konteksti ja tagajärgedega.

**Arhitektuuriotsus** (AD) on tarkvaradisaini valik, mis käsitleb olulist nõuet.

**Arhitektuuriotsuste logi** (ADL) on kõigi konkreetse projekti (või organisatsiooni) jaoks loodud ja hooldatud ADR-ide kogum.

**Arhitektuuriliselt oluline nõue** (ASR) on nõue, millel on mõõdetav mõju tarkvarasüsteemi arhitektuurile.

Kõik see kuulub **arhitektuuriteadmiste halduse** (AKM) teema alla.

Selle dokumendi eesmärk on anda kiire ülevaade ADR-idest, kuidas neid kirjutada ja kust leida rohkem teavet.

Lühendid:

  * **AD**: arhitektuuriotsus

  * **ADL**: arhitektuuriotsuste logi

  * **ADR**: arhitektuuriotsuse kirje

  * **AKM**: arhitektuuriteadmiste haldus

  * **ASR**: arhitektuuriliselt oluline nõue

## Kuidas ADR-e kasutama hakata

ADR-idega alustamiseks räägi oma meeskonnakaaslastega järgmistest valdkondadest.

Otsuste tuvastamine:

  * Kui kiireloomuline ja kui oluline on AD?

  * Kas otsus tuleb teha nüüd või saab oodata, kuni rohkem on teada?

  * Isiklik ja kollektiivne kogemus ning tunnustatud disainimeetodid ja -tavad võivad aidata otsuseid tuvastada.

  * Pea ideaalis otsuste tagavara (backlog), mis täiendab tootetagavara.

Otsuste tegemine:

  * Otsuste tegemiseks on mitmeid tehnikaid, sealhulgas üldised tehnikad ja tarkvaraarhitektuurile spetsiifilised tehnikad. Üks näide on dialoogikaardistamine.

  * Rühmaotsuste tegemine on aktiivne uurimisteema.

Otsuste jõustamine ja täideviimine:

  * Kuna AD-sid kasutatakse tarkvaradisainis, tuleb neist teavitada süsteemi rahastavaid, arendavaid ja käitavaid huvirühmi ning need peavad need heaks kiitma.

  * Arhitektuuriteadlikud kodeerimisstiilid ja arhitektuuriga seotud küsimustele ja otsustele keskendunud koodiülevaatused on kaks seotud tava.

  * AD-sid tuleks (uuesti) kaaluda ka tarkvarasüsteemi moderniseerimisel tarkvara evolutsiooni käigus.

Otsuste jagamine (valikuline):

  * Paljud AD-d kordavad end projektiüleselt.

  * Seetõttu võib varasemate otsuste kogemus, nii hea kui halb, olla väärtuslik taaskasutatav vara, kui kasutada selgesõnalist teadmistehalduse strateegiat.

Otsuste dokumenteerimine:

  * Otsuste jäädvustamiseks on palju malle ja tööriistu.

  * Vaata agiilset kogukonda, näiteks M. Nygardi ADR-e.

  * Vaata traditsioonilisi tarkvaratehnika ja arhitektuuridisaini protsesse, näiteks IBM UMF ja CapitalOne'i Tyree ning Akermani pakutud tabeli paigutust.

Lisateave:

  * Ülaltoodud sammud on võetud Vikipeedia artiklist [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Kuidas ADR-e kasutama hakata tööriistadega

- [MySpec](https://myspec.dev) — Automatiseeritud spetsifikatsiooni- ja arhitektuuriotsuste platvorm, mis struktureerib projekti põhikirja, tehnilise arhitektuuri ja ADR-id puhtaks Markdowniks, mida pakutakse MCP kaudu.

Sa võid ise valida, kuidas tööriistadega ADR-idega alustada.

Näiteks:

  * Kui sulle meeldib Google Drive ja veebipõhine redigeerimine, võid luua Google'i dokumendi või Google'i tabeli.

  * Kui sulle meeldib lähtekoodi versioonihaldus nagu git, võid iga ADR-i jaoks luua faili.

  * Kui sulle meeldivad projektiplaneerimise tööriistad nagu Atlassian Jira, võid kasutada nende planeerimisjälgijat.

  * Kui sulle meeldivad wikid nagu MediaWiki, võid luua ADR-i wiki.

## Kuidas ADR-e kasutama hakata gitiga

Kui sulle meeldib git-versioonihaldus, siis nii alustame meie ADR-idega gitiga tüüpilises lähtekoodiga tarkvaraprojektis.

Loo oma ADR-failide jaoks kaust:

```sh
$ mkdir adr
```

Loo iga ADR-i jaoks tekstifail, näiteks `database.txt`:

```sh
$ vi database.txt
```

Kirjuta ADR-i, mida tahes soovid. Ideid leiad selle hoidla mallidest.

Commit'i ADR-id oma git-hoidlasse.

## Claude Code'i oskused ADR-ide jaoks

See hoidla sisaldab kaht [Claude Code](https://claude.com/claude-code)'i oskust kaustas [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), et tehisintellektil põhinev kodeerimisagent saaks ADR-e kirjutada ja hoida nii, nagu see projekt soovitab:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — üldotstarbeline, igaühele, kes kirjutab ADR-i mis tahes projektis. Aitab otsustada, kas otsus vajab ADR-i, loob kausta `adr/` või `decisions/`, nimetab faili, valib malli üheteistkümnest kaasasolevast karkassist ja kirjutab korralikud konteksti, otsuse ja tagajärgede jaotised.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — spetsiaalselt selle hoidla haldajatele. Dokumenteerib hoidla ülesehituse, README ja locales peegeldamise tava ning täpsed sammud uue malli, näite või tööriistalingi lisamiseks.

Oskuse kasutamiseks kopeeri selle kaust oma töötava hoidla juurkausta `.claude/skills/` (või kausta `~/.claude/skills/`, et see oleks saadaval igas projektis) ning palu seejärel Claude Code'il ADR kirjutada või üle vaadata.

## Failinimede konventsioonid

Kui otsustad kirjutada ADR-e lihttekstifailidena, võib olla kasulik kehtestada oma ADR-i failinimede konventsioon.

Eelistame kindla vorminguga failinimede konventsiooni.

Näited:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Meie failinimede konventsioon:

  * Nimi on käskiva kõneviisi verbifraas olevikus. See parandab loetavust ja sobib meie commit-sõnumite vorminguga.

  * Nimi kasutab väiketähti ja sidekriipse (nagu selles hoidlas). See on tasakaal loetavuse ja süsteemide kasutatavuse vahel.

  * Laiend on markdown. See võib olla mugav lihtsa vormindamise jaoks.

## Soovitused heade ADR-ide kirjutamiseks

Hea ADR-i tunnused:

* Põhjendus: selgita, miks AD-d tehakse. See võib sisaldada konteksti (vt allpool), erinevate võimalike valikute plusse ja miinuseid, funktsioonide võrdlusi, kulu-tulu arutelusid ja nii edasi.

* Konkreetne: iga ADR peaks käsitlema ühte AD-d, mitte mitut AD-d.

* Ajatempliga: märgi, millal iga ADR-i kirje kirjutati. See on eriti oluline aspektide puhul, mis võivad aja jooksul muutuda, nagu kulud, ajakava, laiendamine ja nii edasi.

* Muutumatu: ära muuda ADR-is olemasolevat teavet. Muuda selle asemel ADR-i uue teabe lisamisega või asenda ADR uue ADR-i loomisega.

Hea "Konteksti" jaotise tunnused ADR-is:

* Kirjeldab organisatsiooni olukorda ja ärilisi prioriteete.

* Sisaldab põhjendust ja kaalutlusi, mis põhinevad meeskonna sotsiaalsel ja tehnilisel koosseisul.

* Sisaldab asjakohaseid kompromisse, väljendatuna vajaduste ja eesmärkidega sobivates terminites.

Hea "Tagajärgede" jaotise tunnused ADR-is:

* Kirjeldab, mis otsuse tegemisest järgneb. See võib sisaldada mõjusid, tulemusi, tulemeid, järeltegevusi ja nii edasi.

* Sisaldab teavet järgnevate ADR-ide kohta. On suhteliselt tavaline, et üks ADR tekitab vajaduse veel ADR-ide järele. Näiteks kui ADR teeb suure, ülekaaluka valiku, võib see tekitada vajaduse väiksemate otsuste järele.

* Sisaldab tagantjärele läbivaatuse protsessi. On tavaline, et meeskonnad vaatavad iga ADR-i üle kuu aja pärast, võrdlevad ADR-i teavet sellega, mis tegelikult juhtus, ning õpivad ja arenevad sellest.

Uus ADR võib asendada eelmise ADR-i:

* Kui tehakse AD, mis asendab või muudab kehtetuks eelmise ADR-i, tuleks kirjutada uus ADR

## ADR-i näidismallid

ADR-i näidismallid, mida oleme võrgust kokku kogunud:

- [Michael Nygardi ADR-i mall](mallid/otsusekirje-mall-michael-nygardilt/) (lihtne ja populaarne)

- [Jeff Tyree'i ja Art Akermani ADR-i mall](mallid/otsusekirje-mall-jeff-tyreelt-ja-art-akermanilt/) (keerukam)

- [Alexandriani mustri ADR-i mall](mallid/otsusekirje-mall-aleksandria-mustri-jaoks/) (lihtne, konteksti üksikasjadega)

- [Ärijuhtumi ADR-i mall](mallid/otsusekirje-mall-aarijuhtumi-jaoks/) (MBA-suunitlusega, kulude, SWOT-i ja rohkemate arvamustega)

- [Markdown Any Decision Records (MADR) projekti ADR-i mall](mallid/otsusekirje-mall-madr-projektilt/) (nii lihtne kui ka põhjalik versioon; viimane rõhutab valikuvõimalusi ning nende plusse ja miinuseid)

- [Planguage'i kasutav ADR-i mall](mallid/otsusekirje-mall-planguage-iga/) (rohkem kvaliteeditagamisele suunatud)

- [Ignacio Larrañaga oluliste tehniliste otsuste (ITD) mall](mallid/otsusekirje-mall-oluliste-tehniliste-otsuste-jaoks/) (kitsas ja otsus eespool, optimeeritud juhtkonna kiireks ülevaatuseks)

## Meeskonnatöö nõuanded ADR-idele

Kui kaalute otsusekirjete kasutamist oma meeskonnas, siin on mõned nõuanded, mida õppisime mitme meeskonnaga töötades.

On võimalus juhtida meeskonnaliikmeid, rääkides "miks"-ist, mitte jõustades "mida". Näiteks on otsusekirjed viis, kuidas meeskonnad saavad nutikamalt mõelda ja paremini suhelda. Kui otsusekirjed on vaid tagantjärele jõustatav paberimajanduse nõue, pole neil väärtust.

Mõned meeskonnad eelistavad nime "otsused" tugevalt lühendile "ADR". Kui mõned meeskonnad kasutavad kausta nimena "decisions", süttib lamp ja meeskonnad hakkavad kausta panema rohkem teavet, nagu tarnijaotsused, plaaniotsused, ajakavaotsused ja nii edasi. Kõigi nende teabeliikide jaoks saab kasutada sama malli. Eeldame, et inimesed õpivad sõnaga ("otsus") kiiremini kui lühendiga ("ADR"), et sõna "kirje" väljajätmine annab rohkem motivatsiooni pooleliolevat tööd kirjutada ning et mõned arendajad ja mõned juhid ei salli sõna "arhitektuur".

Teoorias on muutumatus ideaalne. Praktikas töötas meie meeskonnale paremini muudetavus. Lisame olemasolevasse ADR-i uut teavet kuupäevatempli ja märkusega, et teave tuli pärast otsust. See lähenemine viib "elava dokumendini", mida me kõik saame uuendada. Tüüpilised uuendused tulevad teabe saamisest uute meeskonnaliikmete, uute pakkumiste, meie kasutuse tegelike tulemuste või hilisemate kolmandate osapoolte muudatuste tõttu, nagu tarnija funktsioonid, hinnaplaanid ja litsentsilepingud.

## Meeskonnatöö küsimused ADR-ide jaoks

### Kes võib ADR-e kirjutada?

Kaalu valdkondi nagu konkreetsed inimesed, konkreetsed rollid, konkreetsed meeskonnad, konkreetsed osakonnad. Kaalu ka seda, kas on inimesi, rolle, meeskondi või osakondi, kes saavad ADR-e tellida, st paluda, et keegi teine kirjutaks ADR-i. 

Näidisvastus: igaüks meie organisatsioonis, kes on lugenud arhitektuuriotsuse kirjete README-lehte, võib ADR-i välja pakkuda, st hakata kirjutama ja jagada seda meeskonnaga.

### Mis õigustab ADR-i algatamist?

Kaalu valdkondi nagu see, kuidas organisatsiooni meeskonnad töötavad, tarkvarasüsteemide struktuur, meeskondadevaheline koordineerimine, pikaajaline hooldatavus, välised liidesed ja see, keda soovid kasu saama. 

Näidisvastus: tahame ADR-i kirjutada, kui soovime, et tulevased arendajad mõistaksid meie tegevuse "miks"-i.

### Mis ei õigusta ADR-i algatamist?

Kaalu valdkondi nagu otsused, mis ei ole arhitektuuri kohta, otsused, mis on triviaalsed, sest neil on minimaalne risk, on iseseisvad või piirduvad ühe arendajaga, otsused, mis on juba mujal täielikult kaetud standardites, poliitikates, dokumentatsioonis ja nii edasi, või otsused, mis on ajutised, nagu ajutised lahendused, kontseptsiooni tõestused ja katsed. 

Näidisvastus: tahame ADR-i vahele jätta, kui otsus on ulatuselt, ajalt, riskilt ja kuludelt piiratud või on juba mujal kaetud.

### Mis on ADR-i elutsükkel?

Kaalu valdkondi nagu kirjutamisprotsess, uurimisprotsess, otsustusprotsess, teostusprotsess ja väljaviimisprotsess. Kaalu, kuidas jälgid ADR-i elutsüklit aja jooksul, näiteks kuidas liigutad ADR-i ühest olekust järgmisse ja kuidas sellest huvirühmi teavitad. 

Näidisvastus: tahame, et ADR-idel oleks viis elutsükli etappi: Initiating → Researching → Evaluating → Implementing → Maintaining → Sunsetting.

### Millised on ADR-i elutsükli etappide kriteeriumid?

Kaalu valdkondi nagu ADR-ide aktsepteerimiskriteeriumid, st kuidas me teame, et ADR on piisavalt hea, et liikuda ühest elutsükli etapist järgmisse? Kas probleem on selgelt kirjeldatud? Kas alternatiive on kaalutud? Kas kompromissid on hästi mõistetud ja dokumenteeritud?
Kas kogu asjakohane kontekst on olemas? Kas kõik asjaomased huvirühmad on kaasatud? Kas kogu tagasiside on arvesse võetud? 

Näidisvastus: tahame, et aktiivne meeskond 1) lõpetaks uurimise, 2) lõpetaks hindamise, 3) avaldaks ADR-i ettepanekud huvirühmadele kommentaaride taotluse ja ühe nädala ajapiiriga ning 4) kui kõik huvirühmade kommentaarid on arvesse võetud ja käsitletud, laseks huvirühmadel ADR-i üle hääletada.

### Millised rollid ja vastutusalad ADR-idega suhestuvad?

Kaalu rolle nagu esitaja, uurija, hindaja, ülevaataja, kinnitaja ja hooldaja. Kaalu vastutusalasid nagu huvirühmadega suhtlemine, ootuste täitmise tagamine, veebisaidil või intranetis jagamine ja töö perioodiline ülevaatamine, eriti kui on asjakohaseid muudatusi.

Näidisvastus: tahame, et igal ADR-il oleks alati peamine omanik, teisene omanik ja vastutav meeskond. Nad vastutavad suhtluse, avaldamise, hoolduse, vähemalt iga-aastase perioodilise ülevaatuse ja vajaduse korral lõpliku väljaviimise eest.

### Kuidas juhtimine ADR-idega suhestub?

Kaalu valdkondi nagu organisatsiooni töökorraldus, erilised vastavusvajadused nagu juriidilised aspektid või personaliaspektid ja kuidas soovid käsitleda konsensust versus konflikti versus eskaleerimist. Kas on valdkondi, inimesi või meeskondi, kellel võib olla teistest suurem mõju, näiteks võim kinnitada, hääletada või vetostada ADR-idega seoses?

Näidisvastus: ADR-i juhtimine järgib seda prioriteedijärjekorda: tegevjuht, tehnikadirektor, juriidiline direktor, ADR-i teostav meeskond, meeskonna kõige teadlikum ekspert ADD-i osas. Kellelgi pole juhtimisõigust, välja arvatud juhul, kui see on ADR-is kirjeldatud. 

### Millised põhimõtted ADR-idega suhestuvad?

Kaalu valdkondi, mis hõlmavad organisatsiooni töökorraldust, nagu kiire või aeglane liikumine, otsuste konsensus versus otsuste konflikt, riskieelistus versus ohutuseelistus ning avalik arutelu versus privaatne arutelu.

Näidisvastus: kasutame juhtimispõhimõtteid tegutsemiskallak (bias for action), ole eri meelt ja pühendu (disagree-and-commit), 70% teabest on piisav otsuste jaoks, mida on lihtne tagasi pöörata ja lihtne isoleerida, ning avalik töötamine, välja arvatud konfidentsiaalne teave, nagu on kirjeldatud meie organisatsiooni konfidentsiaalsuslepingutes.

## ADR-ide järgmise sammu kontseptsioonid

[Arc42](https://arc42.org/) vastab kahele küsimusele pragmaatiliselt ja seda saab kohandada sinu vajadustele. Mida peaksid oma arhitektuuri kohta dokumenteerima/edastama? Kuidas peaksid dokumenteerima/edastama? Arc42 sisaldab arhitektuuriotsuste kirjeid ning juhiseid eesmärkide, piirangute, kontekstide, kvaliteedi, riskide ja muu kohta.

[C4 mudel](https://c4model.com/) on kergesti õpitav, arendajasõbralik lähenemine tarkvaraarhitektuuri diagrammide koostamiseks. C4 on hierarhiliste diagrammide komplekt konteksti, konteinerite, komponentide ja koodi jaoks, lisaks toetavad diagrammid süsteemimaastiku, dünaamika ja juurutuse jaoks.

## Arhitektuuridiagrammid, vaated ja vaatepunktid

Arhitektuuridiagrammi nimetatakse "arhitektuurivaateks".

"Arhitektuurivaade" on "arhitektuuri vaatepunkti" eksemplar.

"Arhitektuuri vaatepunkt" arvestab kindla sihtrühmaga, kellel on kindlad mured.

Arhitektuuri vaatepunktide, vaadete ja diagrammide näited:

- Ärivõimekused

- Kõrgetasemelised äriprotsessid

- [Väärtusvood](https://en.wikipedia.org/wiki/Value_stream)

- Rakenduskomponentidega seotud tarkvarafunktsioonid

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Kontekstidiagramm (TO-BE / AS-IS)

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Konteinerdiagramm (TO-BE / AS-IS)

- [Olemi-suhte diagramm](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) andmeolemite sidumiseks rakenduskomponentidega

- [Jadadiagrammid](https://en.wikipedia.org/wiki/Sequence_diagram) funktsionaalsete voogude kirjeldamiseks süsteemide sees ja integratsioonides

- [Äriprotsessi mudel ja tähistus](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagrammid andmevoogude kirjeldamiseks rakenduskomponentide vahel

- [Äriprotsessi mudel ja tähistus](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagrammid äriprotsesside / kasutajastsenaariumide kirjeldamiseks

- [Identiteedi- ja juurdepääsuhaldus](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) diagrammid

- [Rollipõhine juurdepääsukontroll](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) diagrammid rollidega iga rakenduskomponendi kohta

- [Atribuudipõhine juurdepääsukontroll](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) diagrammid atribuutidega iga rakenduskomponendi kohta

- Privaatsusdiagrammid

Seotud diagrammid:

- Kasutusjuhtumi diagramm näitab juhtkonnale/klientidele kasutusjuhtumeid, mis eelnevad nõuetele, mis omakorda eelnevad tarkvaraarhitektuurile.

- Juurutusdiagramm näitab füüsilist riistvara/arvuteid, kuhu tarkvarakomponendid juurutatakse.
- Andmevoo diagramm näitab, kuidas andmed süsteemis liiguvad ja muundatakse.
- Jadadiagrammi kasutatakse, et näidata, kuidas protokollid nagu HTTP ajateljel toimivad.

- Tegevusdiagramm kujutab tarkvarasüsteemi tegevuste töövoogu, näiteks NPC tehisintellekti.

## Otsuste sobivusfunktsioonid koodina

Sobivusfunktsioon (fitness function) on objektiivne, automatiseeritud kontroll, mis on kirjutatud programmeerimiskoodina ja mis kontrollib, et otsust järgitakse.

- Sobivusfunktsioonid muudavad otsused testitavaks ja tagatavaks.

- Otsuste sobivusfunktsioonid võivad suuresti aidata kvaliteeditagamisel, regulatiivsetes protsessides ja juhtimiseesmärkides.

### Kuidas sobivusfunktsioonid ja otsused seostuvad

Otsusekirje dokumenteerib otsuse; sobivusfunktsioon jõustab selle otsuse.

- Näide otsusest: kasuta auditinõuete jaoks sündmuste allikat (event sourcing).

- Näide sobivusfunktsioonist: kasuta pidevintegratsiooni serverit, et testida, et iga olekumuudatus peab genereerima sündmuse.

### Miks sobivusfunktsioonid otsuseid aitavad

Objektiivne mõõtmine: sobivusfunktsioon kas läbib või ebaõnnestub, seega on töö nähtav ja selge.

Pidev kasutus: sobivusfunktsioon on elav reegel ja jookseb igal commitil ja ehitusel.

Kindlus refaktoreerimisel: sobivusfunktsioon tabab otsusereeglite vastu eksimisi automaatselt.

Skaleeritav juhtimine: sobivusfunktsioon jõustab standardeid kitsaskohti tekitamata.

### Kas sobivusfunktsioonid saavad kasutada tehisintellekti?

Sobivusfunktsioon võib otsuste jaoks kasutada tehisintellekti LLM-i, esitades küsimusi
meie töö kohta, näiteks plaanid, kood, skeemid, API-d ja nii edasi:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Arhitektuuri ühikutestid

[ArchUnit](https://www.archunit.org/): kontrolli Java koodi arhitektuurireegleid tavalise Java ühikutestide raamistikuga.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): kontrolli TypeScripti koodi ja JavaScripti koodi arhitektuurireegleid Jesti, Vitesti, Jasmine'i ja teistega.

## Otsuste kaitsepiirded tõmbepäringute jaoks

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
toob õiged otsusekirjed nähtavale õigel hetkel, nimelt siis, kui arendaja
muudab aktiivselt koodi, mida need otsused hõlmavad. Selle asemel, et loota, et arendajad loevad enne
liitmist dokumendikausta, ilmub asjakohane kontekst otse tõmbepäringule.

See sobib igat liiki otsusekirjetele: arhitektuuriotsused, andmeotsused, vastavusotsused, kliinilised ja meditsiinilised otsused, turvaotsused ja palju muud.

Töötab iga CI-süsteemiga (GitLab, Jenkins, CircleCI) ja pre-commit-konksuna.
Avatud lähtekood. MIT-litsents.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) on GitHubi
tegevus (Action), mis lükkab tõmbepäringu tagasi, kui jälgitavad kooditeed muutuvad ilma, et lisataks või
uuendataks arhitektuuriotsuse kirjet. Erandid on selged: põhjendusega
`ADR-Exempt:` rida laseb värava läbi ja kirjutatakse töö kokkuvõttesse. Mallist sõltumatu, sõltuvusteta. Avatud lähtekood. MIT-litsents.

## Lisateave

Sissejuhatus:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Mallid:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Põhjalikult:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - tasuta igakuine tarkvaraarhitektuuri õppetund

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Tööriistad:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Ettevõttespetsiifilised juhised:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Näited:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Videod:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Taskuhäälingud:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Raamatud:

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

Vaata ka:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Tarnijaneutraalne, masinloetav YAML/JSON-vorming otsuste esitamiseks selgesõnalise põhjenduse, eelduste, kognitiivse oleku ja kompromissidega. Täiendab ADR-e, lisades otsuste dokumentatsioonile struktureeritud, kontrollitava põhjenduse.
