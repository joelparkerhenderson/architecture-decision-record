# Arhitektūras lēmuma ieraksts (ADR)

Arhitektūras lēmuma ieraksts (ADR) ir dokuments, kurā fiksēts svarīgs pieņemts arhitektūras lēmums kopā ar tā kontekstu un sekām.

> [!IMPORTANT]
> Pirms šo resursu izmantošanas jebkurā kritiskā sistēmā veiciet savu rūpīgo pārbaudi.

Saturs:

- [Kas ir arhitektūras lēmuma ieraksts?](#kas-ir-arhitektūras-lēmuma-ieraksts)
- [Kā sākt lietot ADR](#kā-sākt-lietot-adr)
- [Kā sākt lietot ADR ar instrumentiem](#kā-sākt-lietot-adr-ar-instrumentiem)
- [Kā sākt lietot ADR ar git](#kā-sākt-lietot-adr-ar-git)
- [Claude Code prasmes ADR](#claude-code-prasmes-adr)
- [ADR failu nosaukumu konvencijas](#adr-failu-nosaukumu-konvencijas)
- [Ieteikumi labu ADR rakstīšanai](#ieteikumi-labu-adr-rakstīšanai)
- [ADR veidņu piemēri](#adr-veidņu-piemēri)
- [Komandas darba padomi ADR lietošanai](#komandas-darba-padomi-adr-lietošanai)
- [Komandas darba jautājumi ADR](#komandas-darba-jautājumi-adr)
- [Nākamo soļu koncepti ADR](#nākamo-soļu-koncepti-adr)
- [Arhitektūras diagrammas, skati un skatpunkti](#arhitektūras-diagrammas-skati-un-skatpunkti)
- [Piemērotības funkcijas lēmumiem kā kodam](#piemērotības-funkcijas-lēmumiem-kā-kodam)
- [Lēmumu aizsargmehānismi izmaiņu pieprasījumiem](#lēmumu-aizsargmehānismi-izmaiņu-pieprasījumiem)
- [Papildu informācija](#papildu-informācija)

Veidnes:

- [Jeff Tyree un Art Akerman lēmuma ieraksta veidne](veidnes/lemuma-ieraksta-veidne-jeff-tyree-un-art-akerman/)
- [Michael Nygard lēmuma ieraksta veidne](veidnes/lemuma-ieraksta-veidne-michael-nygard/)
- [EdgeX lēmuma ieraksta veidne](veidnes/lemuma-ieraksta-veidne-edgex/)
- [arc42 lēmuma ieraksta veidne](veidnes/lemuma-ieraksta-veidne-arc42/)
- [Lēmuma ieraksta veidne Aleksandrijas modelim](veidnes/lemuma-ieraksta-veidne-aleksandrijas-modelim/)
- [Lēmuma ieraksta veidne biznesa pamatojumam](veidnes/lemuma-ieraksta-veidne-biznesa-pamatojumam/)
- [MADR projekta lēmuma ieraksta veidne](veidnes/lemuma-ieraksta-veidne-madr-projekta/)
- [Lēmuma ieraksta veidne ar Planguage](veidnes/lemuma-ieraksta-veidne-ar-planguage/)
- [Paulo Merson lēmuma ieraksta veidne](https://github.com/pmerson/ADR-template)
- [Olaf Zimmermann lēmuma ieraksta veidne](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Gareth Morgan lēmuma ieraksta veidne](veidnes/lemuma-ieraksta-veidne-gareth-morgan/)
- [GIG Cymru NHS Wales lēmuma ieraksta veidne](veidnes/lemuma-ieraksta-veidne-gig-cymru-nhs-wales/)
- [Lēmuma ieraksta veidne svarīgiem tehniskiem lēmumiem (ITD), autors Ignacio Larrañaga](veidnes/lemuma-ieraksta-veidne-svarigiem-tehniskiem-lemumiem/)

Piemēri:

- [CSS ietvars](piemeri/css-ietvars/)
- [Vides mainīgo konfigurācija](piemeri/vides-mainigo-konfiguracija/)
- [Metrikas, uzraudzība, brīdinājumi](piemeri/metrikas-uzraudziba-bridinajumi/)
- [Microsoft Azure DevOps](piemeri/microsoft-azure-devops/)
- [Monorepo vai multirepo](piemeri/monorepo-vai-multirepo/)
- [Programmēšanas valodas](piemeri/programmesanas-valodas/)
- [Noslēpumu glabāšana](piemeri/noslepumu-glabasana/)
- [Laika zīmoga formāts](piemeri/laika-zimoga-formats/)
- [Vēl daudz vairāk ...](piemeri/)

## Kas ir arhitektūras lēmuma ieraksts?

**Arhitektūras lēmuma ieraksts** (ADR) ir dokuments, kurā fiksēts svarīgs pieņemts arhitektūras lēmums kopā ar tā kontekstu un sekām.

**Arhitektūras lēmums** (AD) ir programmatūras projektēšanas izvēle, kas risina būtisku prasību.

**Arhitektūras lēmumu žurnāls** (ADL) ir visu konkrētam projektam (vai organizācijai) izveidoto un uzturēto ADR kopums.

**Arhitektūriski nozīmīga prasība** (ASR) ir prasība, kurai ir izmērāma ietekme uz programmatūras sistēmas arhitektūru.

Tas viss ietilpst **arhitektūras zināšanu pārvaldības** (AKM) tēmā.

Šī dokumenta mērķis ir sniegt ātru ADR pārskatu, parādīt, kā tos izveidot, un norādīt, kur meklēt papildu informāciju.

Saīsinājumi:

  * **AD**: arhitektūras lēmums

  * **ADL**: arhitektūras lēmumu žurnāls

  * **ADR**: arhitektūras lēmuma ieraksts

  * **AKM**: arhitektūras zināšanu pārvaldība

  * **ASR**: arhitektūriski nozīmīga prasība

## Kā sākt lietot ADR

Lai sāktu lietot ADR, pārrunājiet ar komandas biedriem šīs jomas.

Lēmumu apzināšana:

  * Cik steidzams un cik svarīgs ir AD?

  * Vai tas jāpieņem tagad, vai arī var pagaidīt, līdz kļūs zināms vairāk?

  * Lēmumu apzināšanā var palīdzēt gan personīgā un kolektīvā pieredze, gan atzītas projektēšanas metodes un prakses.

  * Ideālā gadījumā uzturiet lēmumu uzdevumu sarakstu, kas papildina produkta uzdevumu sarakstu.

Lēmumu pieņemšana:

  * Pastāv vairākas lēmumu pieņemšanas metodes, gan vispārīgas, gan specifiskas programmatūras arhitektūrai, piemēram, dialoga kartēšana (dialogue mapping).

  * Grupas lēmumu pieņemšana ir aktīva pētniecības tēma.

Lēmumu īstenošana un nodrošināšana:

  * AD tiek izmantoti programmatūras projektēšanā; tāpēc tie ir jāpaziņo sistēmas ieinteresētajām pusēm, kas to finansē, izstrādā un ekspluatē, un šīm pusēm tie ir jāapstiprina.

  * Divas saistītas prakses ir arhitektūriski izteiksmīgi kodēšanas stili un koda pārskati, kas koncentrējas uz arhitektūras jautājumiem un lēmumiem.

  * AD ir (atkārtoti) jāapsver arī tad, kad programmatūras sistēma tiek modernizēta programmatūras evolūcijas gaitā.

Lēmumu kopīgošana (pēc izvēles):

  * Daudzi AD atkārtojas dažādos projektos.

  * Tāpēc pieredze ar iepriekšējiem lēmumiem, gan labiem, gan sliktiem, var būt vērtīgs atkārtoti izmantojams resurss, ja tiek piemērota skaidra zināšanu pārvaldības stratēģija.

Lēmumu dokumentēšana:

  * Pastāv daudz veidņu un rīku lēmumu fiksēšanai.

  * Skatiet aģilās kopienas, piemēram, M. Nygard ADR.

  * Skatiet tradicionālos programmatūras inženierijas un arhitektūras projektēšanas procesus, piemēram, tabulu izkārtojumus, ko iesaka IBM UMF un Tyree un Akerman no CapitalOne.

Papildu informācija:

  * Iepriekšminētie soļi ir pārņemti no Vikipēdijas ieraksta [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Kā sākt lietot ADR ar instrumentiem

- [MySpec](https://myspec.dev) — automatizēta specifikāciju un arhitektūras lēmumu platforma, kas strukturē projekta konstitūciju, tehnisko arhitektūru un ADR tīrā Markdown formātā, kuru nodrošina caur MCP.

ADR ar instrumentiem varat sākt lietot jebkurā veidā.

Piemēram:

  * Ja jums patīk Google Drive un tiešsaistes rediģēšana, varat izveidot Google Doc vai Google Sheet.

  * Ja jums patīk pirmkoda versiju kontrole, piemēram, git, varat katram ADR izveidot failu.

  * Ja jums patīk projektu plānošanas rīki, piemēram, Atlassian Jira, varat izmantot rīka plānošanas izsekotāju.

  * Ja jums patīk viki, piemēram, MediaWiki, varat izveidot ADR vikiju.

## Kā sākt lietot ADR ar git

Ja jums patīk git versiju kontrole, lūk, kā mēs mēdzam sākt lietot ADR ar git tipiskā programmatūras projektā ar pirmkodu.

Izveidojiet direktoriju ADR failiem:

```sh
$ mkdir adr
```

Katram ADR izveidojiet teksta failu, piemēram, `choose-database.md`:

```sh
$ vi choose-database.md
```

ADR rakstiet jebko, ko vēlaties. Idejām skatiet šajā repozitorijā esošās veidnes.

Iekomitējiet ADR savā git repozitorijā.

## Claude Code prasmes ADR

Šajā repozitorijā ir divas [Claude Code](https://claude.com/claude-code) prasmes (angl. skills) direktorijā [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), lai MI programmēšanas aģents varētu rakstīt un uzturēt ADR tā, kā iesaka šis projekts:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — vispārēja lietojuma, ikvienam, kas raksta ADR jebkurā projektā. Palīdz izlemt, vai lēmumam vajadzīgs ADR, izveido direktoriju `adr/` vai `decisions/`, nosauc failu, izvēlas veidni no vienpadsmit komplektētajiem karkasiem un uzraksta stabilas sadaļas Konteksts/Lēmums/Sekas.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — īpaši šī repozitorija uzturētājiem. Dokumentē repozitorija struktūru, README/lokalizāciju atspoguļošanas konvenciju un precīzus soļus jaunas veidnes, piemēra vai saites uz rīku pievienošanai.

Lai izmantotu prasmi, nokopējiet tās mapi uz `.claude/skills/` repozitorija saknē, kurā strādājat (vai uz `~/.claude/skills/`, lai tā būtu pieejama katrā projektā), pēc tam lūdziet Claude Code uzrakstīt vai pārskatīt ADR.

## ADR failu nosaukumu konvencijas

Ja nolemjat veidot ADR, izmantojot parastus teksta failus, iespējams, vēlēsities izveidot savu ADR failu nosaukumu konvenciju.

Mēs dodam priekšroku failu nosaukumu konvencijai ar noteiktu formātu.

Piemēri:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Mūsu failu nosaukumu konvencija:

  * Nosaukumā ir tagadnes pavēles izteiksmes darbības vārda frāze. Tas uzlabo lasāmību un atbilst mūsu komita ziņojumu formātam.

  * Nosaukumā izmanto mazos burtus un domuzīmes (tāpat kā šajā repozitorijā). Tas ir līdzsvars starp lasāmību un sistēmas izmantojamību.

  * Paplašinājums ir markdown. Tas var noderēt vienkāršai formatēšanai.

## Ieteikumi labu ADR rakstīšanai

Laba ADR raksturojums:

* Pamatojums: paskaidrojiet iemeslus konkrētā AD īstenošanai. Tas var ietvert kontekstu (skatiet tālāk), dažādu iespējamo izvēļu priekšrocības un trūkumus, funkciju salīdzinājumus, izmaksu un ieguvumu apspriešanu un citu.

* Konkrētība: katram ADR jābūt par vienu AD, nevis vairākiem AD.

* Laika zīmogi: norādiet, kad katrs ADR elements ir uzrakstīts. Tas ir īpaši svarīgi aspektiem, kas laika gaitā var mainīties, piemēram, izmaksām, grafikiem, mērogošanai un tamlīdzīgi.

* Nemainīgums: nemainiet ADR esošo informāciju. Tā vietā papildiniet ADR, pievienojot jaunu informāciju, vai aizstājiet ADR, izveidojot jaunu ADR.

Laba ADR sadaļas „Konteksts” raksturojums:

* Paskaidrojiet savas organizācijas situāciju un biznesa prioritātes.

* Iekļaujiet pamatojumu un apsvērumus, kas balstīti uz jūsu komandu sociālo sastāvu un prasmēm.

* Iekļaujiet atbilstošas priekšrocības un trūkumus un aprakstiet tos izteiksmēs, kas atbilst jūsu vajadzībām un mērķiem.

Laba ADR sadaļas „Sekas” raksturojums:

* Paskaidrojiet, kas izriet no lēmuma pieņemšanas. Tas var ietvert ietekmi, iznākumus, rezultātus, turpmākās darbības un citu.

* Iekļaujiet informāciju par jebkuriem turpmākiem ADR. Ir samērā ierasti, ka viens ADR izraisa vajadzību pēc papildu ADR, piemēram, kad viens ADR pieņem lielu pārsvarā esošu izvēli, kas savukārt rada vajadzību pēc vairākiem mazākiem lēmumiem.

* Iekļaujiet jebkurus pēcdarbības pārskata procesus. Komandām ir tipiski pārskatīt katru ADR vienu mēnesi vēlāk, lai salīdzinātu ADR informāciju ar to, kas noticis praksē, un tā mācītos un attīstītos.

Jauns ADR var aizstāt iepriekšējo ADR:

* Kad tiek pieņemts AD, kas aizstāj vai anulē iepriekšējo ADR, jāizveido jauns ADR

## ADR veidņu piemēri

ADR veidņu piemēri, ko esam apkopojuši internetā:

- [Michael Nygard ADR veidne](veidnes/lemuma-ieraksta-veidne-michael-nygard/) (vienkārša un populāra)

- [Jeff Tyree un Art Akerman ADR veidne](veidnes/lemuma-ieraksta-veidne-jeff-tyree-un-art-akerman/) (sarežģītāka)

- [ADR veidne Aleksandrijas modelim](veidnes/lemuma-ieraksta-veidne-aleksandrijas-modelim/) (vienkārša ar konteksta specifiku)

- [ADR veidne biznesa pamatojumam](veidnes/lemuma-ieraksta-veidne-biznesa-pamatojumam/) (vairāk MBA orientēta, ar izmaksām, SWOT un vairāk viedokļiem)

- [Projekta Markdown Any Decision Records (MADR) ADR veidne](veidnes/lemuma-ieraksta-veidne-madr-projekta/) (gan vienkārša, gan izvērsta versija; pēdējā uzsver iespējas un to priekšrocības un trūkumus)

- [ADR veidne ar Planguage](veidnes/lemuma-ieraksta-veidne-ar-planguage/) (vairāk orientēta uz kvalitātes nodrošināšanu)

- [Veidne svarīgiem tehniskiem lēmumiem (ITD), autors Ignacio Larrañaga](veidnes/lemuma-ieraksta-veidne-svarigiem-tehniskiem-lemumiem/) (viegla un ar lēmumu pirmajā vietā, optimizēta ātram vadības pārskatam)

## Komandas darba padomi ADR lietošanai

Ja apsverat lēmumu ierakstu lietošanu savā komandā, lūk, daži padomi, ko esam apguvuši, strādājot ar daudzām komandām.

Jums ir iespēja vadīt komandas biedrus, kopīgi runājot par „kāpēc”, nevis uzspiežot „ko”. Piemēram, lēmumu ieraksti ir veids, kā komandas var gudrāk domāt un labāk komunicēt; lēmumu ieraksti nav vērtīgi, ja tie ir tikai pēc fakta uzspiesta papīru kārtošana.

Dažas komandas daudz vairāk dod priekšroku nosaukumam „lēmumi” nekā saīsinājumam „ADR”. Kad dažas komandas izmanto direktorijas nosaukumu „decisions”, tas ir kā ieslēgta spuldze, un komanda sāk šajā direktorijā ievietot vairāk informācijas, piemēram, piegādātāju lēmumus, plānošanas lēmumus, grafiku lēmumus utt. Visiem šiem informācijas veidiem var izmantot vienu un to pašu veidni. Mēs izvirzām hipotēzi, ka cilvēki mācās ātrāk ar vārdiem („lēmumi”) nekā ar saīsinājumiem („ADR”), ka cilvēki ir motivētāki rakstīt nepabeigtus dokumentus, kad vārds „ieraksts” ir izņemts, kā arī to, ka dažiem izstrādātājiem un dažiem vadītājiem nepatīk vārds „arhitektūra”.

Teorētiski nemainīgums ir ideāls. Praksē mūsu komandām labāk darbojusies mainīgums. Jauno informāciju mēs ievietojam esošajā ADR ar datuma zīmogu un piezīmi, ka informācija ir saņemta pēc lēmuma. Šāda pieeja noved pie „dzīva dokumenta”, ko varam atjaunināt mēs visi. Tipiski atjauninājumi notiek, kad mēs saņemam informāciju pateicoties jauniem komandas biedriem vai jauniem piedāvājumiem, mūsu lietojuma reālās pasaules rezultātiem vai pēc fakta notikušām trešo pušu izmaiņām, piemēram, piegādātāju iespējām, cenu plāniem, licences līgumiem utt.

## Komandas darba jautājumi ADR


### Kas var izveidot ADR?

Apsveriet jomas, piemēram, konkrētas personas, konkrētas lomas, konkrētas komandas vai konkrētas nodaļas; apsveriet arī to, vai ir personas, lomas, komandas vai nodaļas, kas var pasūtīt ADR, proti, pieprasīt tādu, ko uzrakstīs kāds cits. 

Atbildes piemērs: jebkura mūsu organizācijas persona, kas ir izlasījusi arhitektūras lēmuma ieraksta README lapu, var ierosināt ADR, proti, persona var sākt to rakstīt un kopīgot ar komandu.

### Kas attaisno ADR izveidi?

Apsveriet jomas, piemēram, jūsu organizācijas komandu darba veidus, jūsu programmatūras sistēmas struktūru, starpkomandu koordināciju, ilgtermiņa uzturamību, ārējās saskarnes, kam vēlaties nest labumu un tamlīdzīgi. 

Atbildes piemērs: mēs vēlamies izveidot ADR, kad vēlamies, lai nākotnes izstrādātāji saprastu „kāpēc” mūsu darbībām.

### Kas attaisno ADR neizveidi?

Apsveriet jomas, piemēram, lēmumi, kas nav par arhitektūru vai ir sīki, piemēram, ar minimālu risku, patstāvīgi vai viena izstrādātāja lēmumi, vai ir jau pilnībā aptverti citur, piemēram, ar standartiem, politikām vai dokumentāciju, vai ir pagaidu, piemēram, apvedceļi, koncepcijas pierādījumi vai eksperimenti. 

Atbildes piemērs: mēs vēlamies izlaist ADR, kad lēmums ir ierobežots pēc apjoma, laika, riska un izmaksām vai ir jau aptverts citur.

### Kāds ir ADR dzīves cikls?

Apsveriet jomas, piemēram, izveides process, izpētes process, lēmuma pieņemšanas process, īstenošanas process un izbeigšanas process. Apsveriet, kā izsekot ADR dzīves ciklam laika gaitā, piemēram, kā pārvietot ADR no viena stāvokļa uz nākamo un kā to paziņot ieinteresētajām pusēm. 

Atbildes piemērs: mēs vēlamies, lai ADR ir pieci dzīves cikla posmi: uzsākšana → izpēte → izvērtēšana → īstenošana → uzturēšana → izbeigšana.

### Kādi ir ADR dzīves cikla soļu kritēriji?

Apsveriet jomas, piemēram, ADR pieņemšanas kritēriji, proti, kā zināt, ka tas ir pietiekami labs, lai pārietu no viena dzīves cikla soļa uz nākamo? Vai problēma ir skaidri formulēta? Vai alternatīvas ir apsvērtas? Vai kompromisi ir pietiekami labi izprasti un dokumentēti?
Vai viss attiecīgais konteksts ir sagatavots? Vai visas attiecīgās ieinteresētās puses ir iesaistītas? Vai visa atgriezeniskā saite ir iekļauta? 

Atbildes piemērs: mēs vēlamies, lai par ADR balso ieinteresētās puses, kad aktīvā komanda ir 1) pabeigusi izpēti, 2) pabeigusi izvērtēšanu, 3) publicējusi ADR priekšlikumu ieinteresētajām pusēm ar komentāru pieprasījumu un viena nedēļas laika logu, 4) visi ieinteresēto pušu komentāri ir iekļauti un izskatīti.

### Kādas lomas un pienākumi mijiedarbojas ar ADR?

Apsveriet tādas lomas kā ierosinātājs, pētnieks, izvērtētājs, pārskatītājs, apstiprinātājs, uzturētājs un tamlīdzīgi. Apsveriet tādus pienākumus kā saziņa ar ieinteresētajām pusēm, gaidu izpildes nodrošināšana, kopīgošana tīmekļa vietnē vai intranetā un darba periodiska pārskatīšana, īpaši tad, kad notiek būtiskas izmaiņas.

Atbildes piemērs: mēs vēlamies, lai katram ADR vienmēr ir primārā kontaktpersona, sekundārā kontaktpersona un atbildīgā komanda; šie ir atbildīgi par saziņu, publikācijām, uzturēšanu, periodisku pārskatīšanu vismaz reizi gadā un galīgo izbeigšanu pēc vajadzības.

### Kā pārvaldība (governance) mijiedarbojas ar ADR?

Apsveriet jomas, piemēram, jūsu organizācijas darba veidus, jebkādas īpašas atbilstības vajadzības, piemēram, juridiskos vai cilvēkresursu aspektus, kā vēlaties rīkoties ar vienprātību, konfliktiem un eskalāciju. Vai ir jomas, personas vai komandas, kurām var būt lielāka ietekme nekā citām attiecībā uz ADR, piemēram, spēja to apstiprināt, par to balsot vai uz to noteikt vetu?

Atbildes piemērs: ADR pārvaldība notiek šādā prioritārā secībā: izpilddirektors (CEO), tehniskais direktors (CTO), juridiskais direktors (CLO), komanda, kas īsteno ADR, eksperti komandā, kas vislabāk pārzina AD. Nevienam citam nav pārvaldības tiesību, ja vien tas nav aprakstīts ADR. 

### Kādi principi mijiedarbojas ar ADR?

Apsveriet jomas, piemēram, jūsu organizācijas darba veidus, kas ietver ātru vai lēnu rīcību, lēmumu vienprātību vai lēmumu konfliktu, riska vai drošības preferences, publisku vai privātu diskusiju un tamlīdzīgi.

Atbildes piemērs: mēs izmantojam vadības principus: tieksme uz rīcību (bias for action), nepiekrišana un apņemšanās (disagree-and-commit), 70 % aplēses ir pietiekami labas viegli atgriezeniskiem un viegli izolējamiem lēmumiem, un publiski darba veidi, izņemot konfidenciālu informāciju, kā aprakstīts mūsu organizācijas konfidencialitātes līgumā.

## Nākamo soļu koncepti ADR

[Arc42](https://arc42.org/) pragmatiski atbild uz diviem jautājumiem, un to var pielāgot jūsu īpašajām vajadzībām. Ko jums vajadzētu dokumentēt/paziņot par savu arhitektūru? Kā jums vajadzētu dokumentēt/paziņot? Arc42 ietver arhitektūras lēmumu ierakstus, kā arī norādījumus par mērķiem, ierobežojumiem, kontekstiem, kvalitāti, riskiem un citu.

[C4 modelis](https://c4model.com/) ir viegli apgūstama, izstrādātājiem draudzīga pieeja programmatūras arhitektūras diagrammu veidošanai. C4 ir hierarhisku diagrammu kopa kontekstam, konteineriem, komponentēm un kodam, kā arī atbalsta diagrammas sistēmu ainavai, dinamikai un izvietošanai.

## Arhitektūras diagrammas, skati un skatpunkti

Arhitektūras diagramma tiek saukta par „arhitektūras skatu”.

„Arhitektūras skats” ir „arhitektūras skatpunkta” eksemplārs.

„Arhitektūras skatpunktam” ir noteikta auditorija ar konkrētām interesēm.

Arhitektūras skatpunktu, skatu un diagrammu piemēri:

- Biznesa spējas

- Augsta līmeņa biznesa procesi

- [Vērtības plūsmas (Value Streams)](https://en.wikipedia.org/wiki/Value_stream)

- Programmatūras funkcijas, kas kartētas uz lietojumprogrammu komponentēm

- [C4 modeļa](https://en.wikipedia.org/wiki/C4_model) konteksta diagramma (TO-BE / AS-IS)

- [C4 modeļa](https://en.wikipedia.org/wiki/C4_model) konteineru diagramma (TO-BE / AS-IS)

- [Entītiju attiecību diagramma (Entity-relationship Diagram)](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) datu entītiju kartēšanai uz lietojumprogrammu komponentēm

- [Secību diagrammas (Sequence Diagrams)](https://en.wikipedia.org/wiki/Sequence_diagram) funkcionālo plūsmu aprakstīšanai sistēmās un integrācijām

- [Biznesa procesu modeļa un notācijas (Business Process Model and Notation)](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagrammas datu plūsmu aprakstīšanai starp lietojumprogrammu komponentēm

- [Biznesa procesu modeļa un notācijas (Business Process Model and Notation)](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagrammas biznesa procesu / lietotāju scenāriju aprakstīšanai

- [Identitātes un piekļuves pārvaldības (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) diagrammas

- [Uz lomām balstītas piekļuves kontroles (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) diagrammas ar lomām katrai lietojumprogrammas komponentei

- [Uz atribūtiem balstītas piekļuves kontroles (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) diagrammas ar atribūtiem katrai lietojumprogrammas komponentei

- Privātuma diagrammas

Saistītās diagrammas:

- Lietošanas gadījumu diagramma parāda lietošanas gadījumus vadībai/klientiem; tā ir pirms prasībām, kuras ir pirms programmatūras arhitektūras.

- Izvietošanas diagramma parāda fizisko aparatūru/datorus, uz kuriem tiek izvietotas programmatūras komponentes.
- Datu plūsmas diagramma parāda, kā dati pārvietojas pa sistēmu un tiek pārveidoti.
- Secību diagramma tiek izmantota, lai parādītu, kā protokoli, piemēram, HTTP, darbojas uz laika ass.

- Aktivitāšu diagramma attēlo darbību plūsmu, ko veic programmatūras sistēma, piemēram, kā NPC MI.

## Piemērotības funkcijas lēmumiem kā kodam

Piemērotības funkcijas (fitness functions) ir objektīvas automatizētas pārbaudes, kas uzrakstītas ar programmēšanas kodu un pārbauda, vai lēmumi tiek ievēroti.

- Piemērotības funkcijas padara lēmumus testējamus un nodrošināmus.

- Piemērotības funkcijas lēmumiem var ievērojami palīdzēt kvalitātes nodrošināšanā, regulatīvajos procesos un pārvaldības mērķos.

### Kā piemērotības funkcijas ir saistītas ar lēmumiem

Lēmuma ieraksts dokumentē lēmumu, savukārt piemērotības funkcija nodrošina lēmumu.

- Lēmuma piemērs: revīzijas prasībām mēs izmantojam notikumu avotu izmantošanu (event sourcing).

- Piemērotības funkcijas piemērs: mēs ar nepārtrauktās integrācijas serveri pārbaudām, ka visām stāvokļa izmaiņām jāveido notikumi.

### Kāpēc piemērotības funkcijas palīdz lēmumiem

Objektīvi mērījumi: piemērotības funkcijas izturēs vai neizturēs, tāpēc darbs ir redzams un skaidrs.

Nepārtraukta lietošana: piemērotības funkcijas ir jūsu dzīvie noteikumi, kas tiek izpildīti katrā komitā un būvējumā.

Pārliecība pārveidot kodu: piemērotības funkcijas automātiski uztver lēmumu noteikumu kļūdas.

Mērogojama pārvaldība: piemērotības funkcijas nodrošina standartus, neradot sastrēgumus.

### Vai piemērotības funkcijas var izmantot mākslīgo intelektu?

Piemērotības funkcijas lēmumiem var izmantot mākslīgā intelekta lielos valodas modeļus (LLM), uzdodot jautājumus par jūsu darbu,
piemēram, par jūsu plāniem, kodu, shēmām, API un citu:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Arhitektūras vienībtestēšana

[ArchUnit](https://www.archunit.org/): pārbaudiet Java koda arhitektūras noteikumus, izmantojot jebkuru parasto Java vienībtestu ietvaru.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): pārbaudiet TypeScript koda un JavaScript koda arhitektūras noteikumus, izmantojot Jest, Vitest, Jasmine utt.

## Lēmumu aizsargmehānismi izmaiņu pieprasījumiem

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
automātiski parāda pareizos lēmumu ierakstus pareizajā brīdī – kad
izstrādātājs aktīvi maina kodu, ko šie lēmumi aptver. Tā vietā, lai cerētu,
ka izstrādātāji pirms sapludināšanas izlasīs dokumentu mapi, attiecīgais
konteksts parādās tieši izmaiņu pieprasījumā (pull request).

Tas darbojas ar jebkāda veida lēmumu ierakstiem: arhitektūras lēmumiem, datu
lēmumiem, atbilstības lēmumiem, klīniskiem un medicīniskiem lēmumiem, drošības
lēmumiem un citiem.

Darbojas ar jebkuru CI sistēmu (GitLab, Jenkins, CircleCI) un kā pirms-komita
kāsis (pre-commit hook). Atvērtais pirmkods. MIT licence.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) ir GitHub
Action, kas noraida izmaiņu pieprasījumu, kad novērotie koda ceļi mainās,
nepievienojot vai neatjauninot arhitektūras lēmuma ierakstu. Atbrīvojumi ir
skaidri: rinda `ADR-Exempt:` ar iemeslu izlaiž vārtus un tiek ierakstīta
darba kopsavilkumā. Neatkarīga no veidnes, bez atkarībām. Atvērtais pirmkods. MIT licence.

## Papildu informācija

Ievads:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Veidnes:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Padziļināti:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - bezmaksas ikmēneša programmatūras arhitektūras nodarbība

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Rīki:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Konkrētu uzņēmumu norādījumi:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Piemēri:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Video:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Aplādes:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Grāmatas:

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

Skatiet arī:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - No piegādātāja neatkarīgs, mašīnlasāms YAML/JSON formāts lēmumu attēlošanai ar skaidru pamatojumu, pieņēmumiem, kognitīvo stāvokli un kompromisiem. Papildina ADR, pievienojot strukturētu, validējamu pamatojumu lēmumu dokumentācijai.
