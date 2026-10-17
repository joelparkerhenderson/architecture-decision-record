# ఆర్కిటెక్చర్ నిర్ణయ రికార్డు (ADR)

ఆర్కిటెక్చర్ నిర్ణయ రికార్డు (ADR) అనేది తీసుకున్న ఒక ముఖ్యమైన ఆర్కిటెక్చర్ నిర్ణయాన్ని దాని సందర్భం, పర్యవసానాలతో సహా నమోదు చేసే పత్రం.

> [!IMPORTANT]
> ఈ వనరులను ఏ కీలక వ్యవస్థలోనైనా వాడే ముందు మీ స్వంత తగిన పరిశీలన చేయండి.

విషయసూచిక:

- [ఆర్కిటెక్చర్ నిర్ణయ రికార్డు అంటే ఏమిటి?](#ఆర్కిటెక్చర్-నిర్ణయ-రికార్డు-అంటే-ఏమిటి)
- [ADRల వాడకం ఎలా ప్రారంభించాలి](#adrల-వాడకం-ఎలా-ప్రారంభించాలి)
- [సాధనాలతో ADRల వాడకం ఎలా ప్రారంభించాలి](#సాధనాలతో-adrల-వాడకం-ఎలా-ప్రారంభించాలి)
- [gitతో ADRల వాడకం ఎలా ప్రారంభించాలి](#gitతో-adrల-వాడకం-ఎలా-ప్రారంభించాలి)
- [ADRల కోసం Claude Code నైపుణ్యాలు](#adrల-కోసం-claude-code-నైపుణ్యాలు)
- [ADRల ఫైల్ పేరు సంప్రదాయాలు](#adrల-ఫైల్-పేరు-సంప్రదాయాలు)
- [మంచి ADRలు రాయడానికి సూచనలు](#మంచి-adrలు-రాయడానికి-సూచనలు)
- [ADR ఉదాహరణ మూసలు](#adr-ఉదాహరణ-మూసలు)
- [ADRల కోసం బృందకృషి సలహా](#adrల-కోసం-బృందకృషి-సలహా)
- [ADRల కోసం బృందకృషి ప్రశ్నలు](#adrల-కోసం-బృందకృషి-ప్రశ్నలు)
- [ADRల కోసం తదుపరి దశ భావనలు](#adrల-కోసం-తదుపరి-దశ-భావనలు)
- [ఆర్కిటెక్చర్ రేఖాచిత్రాలు, వీక్షణలు, దృక్కోణాలు](#ఆర్కిటెక్చర్-రేఖాచిత్రాలు-వీక్షణలు-దృక్కోణాలు)
- [కోడ్ రూపంలో నిర్ణయాలకు ఫిట్నెస్ ఫంక్షన్లు](#కోడ్-రూపంలో-నిర్ణయాలకు-ఫిట్నెస్-ఫంక్షన్లు)
- [పుల్ రిక్వెస్ట్ల కోసం నిర్ణయ రక్షణలు](#పుల్-రిక్వెస్ట్ల-కోసం-నిర్ణయ-రక్షణలు)
- [మరింత సమాచారం కోసం](#మరింత-సమాచారం-కోసం)

మూసలు:

- [Jeff Tyree, Art Akerman నిర్ణయ రికార్డు మూస](మూసలు/jeff-tyree-art-akerman-నిర్ణయ-రికార్డు-మూస/)
- [Michael Nygard నిర్ణయ రికార్డు మూస](మూసలు/michael-nygard-నిర్ణయ-రికార్డు-మూస/)
- [EdgeX నిర్ణయ రికార్డు మూస](మూసలు/edgex-నిర్ణయ-రికార్డు-మూస/)
- [arc42 నిర్ణయ రికార్డు మూస](మూసలు/arc42-నిర్ణయ-రికార్డు-మూస/)
- [అలెగ్జాండ్రియన్ నమూనా నిర్ణయ రికార్డు మూస](మూసలు/అలెగ్జాండ్రియన్-నమూనా-నిర్ణయ-రికార్డు-మూస/)
- [వ్యాపార ప్రతిపాదన నిర్ణయ రికార్డు మూస](మూసలు/వ్యాపార-ప్రతిపాదన-నిర్ణయ-రికార్డు-మూస/)
- [MADR ప్రాజెక్ట్ నిర్ణయ రికార్డు మూస](మూసలు/madr-ప్రాజెక్ట్-నిర్ణయ-రికార్డు-మూస/)
- [Planguage వాడే నిర్ణయ రికార్డు మూస](మూసలు/planguage-నిర్ణయ-రికార్డు-మూస/)
- [Paulo Merson నిర్ణయ రికార్డు మూస](https://github.com/pmerson/ADR-template)
- [Olaf Zimmermann నిర్ణయ రికార్డు మూస](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Gareth Morgan నిర్ణయ రికార్డు మూస](మూసలు/gareth-morgan-నిర్ణయ-రికార్డు-మూస/)
- [GIG Cymru NHS Wales నిర్ణయ రికార్డు మూస](మూసలు/gig-cymru-nhs-wales-నిర్ణయ-రికార్డు-మూస/)
- [Ignacio Larrañaga రూపొందించిన ముఖ్యమైన సాంకేతిక నిర్ణయాల (ITD) నిర్ణయ రికార్డు మూస](మూసలు/ముఖ్యమైన-సాంకేతిక-నిర్ణయాల-నిర్ణయ-రికార్డు-మూస/)

ఉదాహరణలు:

- [CSS ఫ్రేమ్వర్క్](ఉదాహరణలు/css-ఫ్రేమ్వర్క్/)
- [ఎన్విరాన్మెంట్ వేరియబుల్ కాన్ఫిగరేషన్](ఉదాహరణలు/ఎన్విరాన్మెంట్-వేరియబుల్-కాన్ఫిగరేషన్/)
- [మెట్రిక్స్, మానిటర్లు, హెచ్చరికలు](ఉదాహరణలు/మెట్రిక్స్-మానిటర్లు-అలర్ట్లు/)
- [Microsoft Azure DevOps](ఉదాహరణలు/microsoft-azure-devops/)
- [మోనోరెపో వర్సెస్ మల్టీరెపో](ఉదాహరణలు/మోనోరెపో-వర్సెస్-మల్టీరెపో/)
- [ప్రోగ్రామింగ్ భాషలు](ఉదాహరణలు/ప్రోగ్రామింగ్-భాషలు/)
- [రహస్యాల నిల్వ](ఉదాహరణలు/రహస్యాల-నిల్వ/)
- [టైమ్స్టాంప్ ఫార్మాట్](ఉదాహరణలు/టైమ్స్టాంప్-ఫార్మాట్/)
- [మరెన్నో...](ఉదాహరణలు/)

## ఆర్కిటెక్చర్ నిర్ణయ రికార్డు అంటే ఏమిటి?

**ఆర్కిటెక్చర్ నిర్ణయ రికార్డు** (ADR) అనేది తీసుకున్న ఒక ముఖ్యమైన ఆర్కిటెక్చర్ నిర్ణయాన్ని, దాని సందర్భం, పర్యవసానాలతో సహా నమోదు చేసే పత్రం.

**ఆర్కిటెక్చర్ నిర్ణయం** (AD) అనేది ఒక ముఖ్యమైన అవసరాన్ని తీర్చే సాఫ్ట్వేర్ డిజైన్ ఎంపిక.

**ఆర్కిటెక్చర్ నిర్ణయ లాగ్** (ADL) అనేది ఒక నిర్దిష్ట ప్రాజెక్ట్ (లేదా సంస్థ) కోసం సృష్టించి, నిర్వహించే అన్ని ADRల సముదాయం.

**ఆర్కిటెక్చర్ పరంగా ముఖ్యమైన అవసరం** (ASR) అనేది సాఫ్ట్వేర్ వ్యవస్థ ఆర్కిటెక్చర్పై కొలవదగిన ప్రభావం చూపే అవసరం.

ఇవన్నీ **ఆర్కిటెక్చర్ జ్ఞాన నిర్వహణ** (AKM) అనే అంశం పరిధిలోకి వస్తాయి.

ADRల గురించి త్వరిత అవలోకనం ఇవ్వడం, వాటిని ఎలా సృష్టించాలో చెప్పడం, మరింత సమాచారం కోసం ఎక్కడ చూడాలో సూచించడం ఈ పత్రం లక్ష్యం.

సంక్షిప్త రూపాలు:

  * **AD**: ఆర్కిటెక్చర్ నిర్ణయం

  * **ADL**: ఆర్కిటెక్చర్ నిర్ణయ లాగ్

  * **ADR**: ఆర్కిటెక్చర్ నిర్ణయ రికార్డు

  * **AKM**: ఆర్కిటెక్చర్ జ్ఞాన నిర్వహణ

  * **ASR**: ఆర్కిటెక్చర్ పరంగా ముఖ్యమైన అవసరం

## ADRల వాడకం ఎలా ప్రారంభించాలి

ADRలను వాడటం ప్రారంభించడానికి, ఈ అంశాల గురించి మీ సహచరులతో మాట్లాడండి.

నిర్ణయాన్ని గుర్తించడం:

  * ఆ AD ఎంత అత్యవసరం, ఎంత ముఖ్యం?

  * దాన్ని ఇప్పుడే తీసుకోవాలా, లేక మరింత సమాచారం తెలిసే వరకు వేచి ఉండవచ్చా?

  * వ్యక్తిగత, సామూహిక అనుభవం, అలాగే గుర్తింపు పొందిన డిజైన్ పద్ధతులు, ఆచరణలు నిర్ణయాన్ని గుర్తించడంలో తోడ్పడతాయి.

  * ఆదర్శంగా, ఉత్పత్తి చేయవలసిన పనుల జాబితాకు తోడుగా నిర్ణయాల చేయవలసిన పనుల జాబితాను నిర్వహించండి.

నిర్ణయం తీసుకోవడం:

  * సాధారణమైనవి, సాఫ్ట్వేర్ ఆర్కిటెక్చర్కు ప్రత్యేకమైనవి (ఉదాహరణకు, డైలాగ్ మ్యాపింగ్) అనేక నిర్ణయ సాంకేతికతలు ఉన్నాయి.

  * సమూహ నిర్ణయ ప్రక్రియ ఒక చురుకైన పరిశోధనా అంశం.

నిర్ణయాన్ని అమలు చేయడం, పాటింపజేయడం:

  * ADలను సాఫ్ట్వేర్ డిజైన్లో ఉపయోగిస్తారు; అందువల్ల వ్యవస్థకు నిధులు సమకూర్చే, దాన్ని అభివృద్ధి చేసే, నడిపే భాగస్వాములకు వాటిని తెలియజేయాలి, వారు వాటిని ఆమోదించాలి.

  * ఆర్కిటెక్చర్ స్పష్టంగా కనిపించే కోడింగ్ శైలులు, ఆర్కిటెక్చర్ సంబంధిత అంశాలు, నిర్ణయాలపై దృష్టి పెట్టే కోడ్ సమీక్షలు రెండు సంబంధిత ఆచరణలు.

  * సాఫ్ట్వేర్ పరిణామంలో సాఫ్ట్వేర్ వ్యవస్థను ఆధునీకరించేటప్పుడు కూడా ADలను (తిరిగి) పరిశీలించాలి.

నిర్ణయ భాగస్వామ్యం (ఐచ్ఛికం):

  * అనేక ADలు ప్రాజెక్టుల మధ్య పునరావృతమవుతాయి.

  * అందువల్ల, స్పష్టమైన జ్ఞాన నిర్వహణ వ్యూహాన్ని అనుసరించేటప్పుడు, గత నిర్ణయాలతో కలిగిన మంచి, చెడు అనుభవాలు పునర్వినియోగించదగిన విలువైన ఆస్తులు కాగలవు.

నిర్ణయ డాక్యుమెంటేషన్:

  * నిర్ణయాలను నమోదు చేయడానికి అనేక మూసలు, సాధనాలు ఉన్నాయి.

  * చురుకైన సముదాయాలను చూడండి, ఉదా. M. Nygard యొక్క ADRలు.

  * సంప్రదాయ సాఫ్ట్వేర్ ఇంజనీరింగ్, ఆర్కిటెక్చర్ డిజైన్ ప్రక్రియలను చూడండి, ఉదా. IBM UMF, CapitalOne కు చెందిన Tyree, Akerman సూచించిన పట్టిక రూపకల్పనలు.

మరిన్ని వివరాలకు:

  * పై దశలను Wikipedia లోని [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision) పేజీ నుండి తీసుకున్నాం

## సాధనాలతో ADRల వాడకం ఎలా ప్రారంభించాలి

- [MySpec](https://myspec.dev) — ప్రాజెక్ట్ రాజ్యాంగం, సాంకేతిక ఆర్కిటెక్చర్, ADRలను MCP ద్వారా అందించే శుభ్రమైన Markdown గా నిర్మించే స్వయంచాలక స్పెసిఫికేషన్, ఆర్కిటెక్చర్ నిర్ణయ వేదిక.

మీకు నచ్చిన ఏ విధంగానైనా సాధనాలతో ADRల వాడకాన్ని ప్రారంభించవచ్చు.

ఉదాహరణకు:

  * మీరు Google Drive, ఆన్లైన్ ఎడిటింగ్ వాడటం ఇష్టపడితే, Google Doc లేదా Google Sheet సృష్టించవచ్చు.

  * మీరు git వంటి సోర్స్ కోడ్ వెర్షన్ నియంత్రణ వాడటం ఇష్టపడితే, ప్రతి ADR కోసం ఒక ఫైల్ సృష్టించవచ్చు.

  * మీరు Atlassian Jira వంటి ప్రాజెక్ట్ ప్రణాళిక సాధనాలు వాడటం ఇష్టపడితే, ఆ సాధనపు ప్రణాళిక ట్రాకర్ను వాడవచ్చు.

  * మీరు MediaWiki వంటి వికీలు వాడటం ఇష్టపడితే, ADR వికీని సృష్టించవచ్చు.

## gitతో ADRల వాడకం ఎలా ప్రారంభించాలి

మీరు git వెర్షన్ నియంత్రణ వాడటం ఇష్టపడితే, సోర్స్ కోడ్ ఉన్న సాధారణ సాఫ్ట్వేర్ ప్రాజెక్ట్ కోసం gitతో ADRలను వాడటం మేము ఎలా ప్రారంభిస్తామో ఇక్కడ ఉంది.

ADR ఫైళ్ల కోసం ఒక డైరెక్టరీ సృష్టించండి:

```sh
$ mkdir adr
```

ప్రతి ADR కోసం, `choose-database.md` వంటి ఒక టెక్స్ట్ ఫైల్ సృష్టించండి:

```sh
$ vi choose-database.md
```

ADRలో మీకు కావలసినది ఏదైనా రాయండి. ఆలోచనల కోసం ఈ రిపాజిటరీలోని మూసలను చూడండి.

ADRని మీ git రిపోకు కమిట్ చేయండి.

## ADRల కోసం Claude Code నైపుణ్యాలు

ఈ రిపాజిటరీ [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/) కింద రెండు [Claude Code](https://claude.com/claude-code) నైపుణ్యాలను అందిస్తుంది, తద్వారా AI కోడింగ్ ఏజెంట్ ఈ ప్రాజెక్ట్ సిఫార్సు చేసే విధంగా ADRలను రాయగలదు, నిర్వహించగలదు:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — సాధారణ ప్రయోజనం కోసం, ఏ ప్రాజెక్ట్లోనైనా ADR రాసే ఎవరికైనా. ఒక నిర్ణయానికి ADR అవసరమా అని నిర్ణయించడంలో సహాయపడుతుంది, `adr/` లేదా `decisions/` డైరెక్టరీని ఏర్పాటు చేస్తుంది, ఫైల్కు పేరు పెడుతుంది, చేర్చిన పదకొండు అస్థిపంజరాల నుండి ఒక మూసను ఎంచుకుంటుంది, దృఢమైన సందర్భం/నిర్ణయం/పర్యవసానాల విభాగాలను రాస్తుంది.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — ప్రత్యేకంగా ఈ రిపాజిటరీ నిర్వాహకుల కోసం. ఇది రిపాజిటరీ లేఅవుట్ను, README/locales ప్రతిబింబ సంప్రదాయాన్ని, కొత్త మూస, ఉదాహరణ లేదా సాధన లింక్ను జోడించడానికి కచ్చితమైన దశలను డాక్యుమెంట్ చేస్తుంది.

నైపుణ్యాన్ని వాడటానికి, దాని ఫోల్డర్ను మీరు పని చేస్తున్న రిపాజిటరీ మూలంలోని `.claude/skills/`లోకి (లేదా ప్రతి ప్రాజెక్ట్లో అందుబాటులో ఉండేలా `~/.claude/skills/`లోకి) కాపీ చేసి, ఆపై ADR రాయమని లేదా సమీక్షించమని Claude Codeను అడగండి.

## ADRల ఫైల్ పేరు సంప్రదాయాలు

మీరు సాధారణ టెక్స్ట్ ఫైళ్లతో ADRలను సృష్టించాలని ఎంచుకుంటే, మీ స్వంత ADR ఫైల్ పేరు సంప్రదాయాన్ని రూపొందించుకోవాలనుకోవచ్చు.

మేము ఒక నిర్దిష్ట ఫార్మాట్ ఉన్న ఫైల్ పేరు సంప్రదాయాన్ని వాడటానికి ఇష్టపడతాం.

ఉదాహరణలు:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

మా ఫైల్ పేరు సంప్రదాయం:

  * పేరులో వర్తమాన కాలపు ఆజ్ఞార్థక క్రియా పదబంధం ఉంటుంది. ఇది చదవడానికి సులభంగా ఉండి, మా కమిట్ సందేశ ఫార్మాట్కు సరిపోతుంది.

  * పేరులో చిన్న అక్షరాలు, డాష్లు వాడతారు (ఈ రిపో లాగే). ఇది చదవడానికి సులభత, వ్యవస్థ వినియోగ సౌలభ్యం మధ్య సమతుల్యత.

  * పొడిగింపు markdown. ఇది సులభంగా ఫార్మాట్ చేయడానికి ఉపయోగపడుతుంది.

## మంచి ADRలు రాయడానికి సూచనలు

మంచి ADR లక్షణాలు:

* హేతువు: ఆ నిర్దిష్ట ADని ఎందుకు చేశారో కారణాలను వివరించండి. ఇందులో సందర్భం (క్రింద చూడండి), వివిధ సాధ్యమైన ఎంపికల లాభనష్టాలు, ఫీచర్ల పోలికలు, ఖర్చు/ప్రయోజన చర్చలు మరిన్ని ఉండవచ్చు.

* నిర్దిష్టత: ప్రతి ADR ఒకే AD గురించి ఉండాలి, అనేక ADల గురించి కాదు.

* టైమ్స్టాంప్లు: ADRలోని ప్రతి అంశాన్ని ఎప్పుడు రాశారో తెలపండి. ఖర్చులు, షెడ్యూళ్లు, స్కేలింగ్ వంటి కాలక్రమేణా మారగల అంశాలకు ఇది ప్రత్యేకంగా ముఖ్యం.

* మార్పులేనిది: ADRలోని ఉన్న సమాచారాన్ని మార్చకండి. బదులుగా కొత్త సమాచారం చేర్చి ADRని సవరించండి, లేదా కొత్త ADRని సృష్టించి ఆ ADRని భర్తీ చేయండి.

ADRలో మంచి "సందర్భం" విభాగం లక్షణాలు:

* మీ సంస్థ పరిస్థితిని, వ్యాపార ప్రాధాన్యతలను వివరించండి.

* మీ బృందాల సామాజిక, నైపుణ్య నిర్మాణాల ఆధారంగా హేతువు, పరిగణనలను చేర్చండి.

* సంబంధితమైన లాభనష్టాలను చేర్చి, వాటిని మీ అవసరాలకు, లక్ష్యాలకు అనుగుణంగా వివరించండి.

ADRలో మంచి "పర్యవసానాలు" విభాగం లక్షణాలు:

* నిర్ణయం తీసుకోవడం వల్ల ఏమి జరుగుతుందో వివరించండి. ఇందులో ప్రభావాలు, ఫలితాలు, అవుట్పుట్లు, తదుపరి చర్యలు మరిన్ని ఉండవచ్చు.

* తదుపరి ADRల గురించి సమాచారం చేర్చండి. ఒక ADR మరిన్ని ADRల అవసరాన్ని కలిగించడం చాలా సాధారణం, ఉదాహరణకు ఒక ADR పెద్ద, విస్తృతమైన ఎంపిక చేసినప్పుడు, అది మరిన్ని చిన్న నిర్ణయాల అవసరాన్ని సృష్టిస్తుంది.

* ఏవైనా చర్యానంతర సమీక్ష ప్రక్రియలను చేర్చండి. బృందాలు ప్రతి ADRని ఒక నెల తర్వాత సమీక్షించి, ADR సమాచారాన్ని వాస్తవ ఆచరణలో జరిగిన దానితో పోల్చి, నేర్చుకుని ఎదగడం సాధారణం.

కొత్త ADR మునుపటి ADR స్థానాన్ని భర్తీ చేయవచ్చు:

* మునుపటి ADRని భర్తీ చేసే లేదా చెల్లకుండా చేసే AD తీసుకున్నప్పుడు, కొత్త ADRని సృష్టించాలి

## ADR ఉదాహరణ మూసలు

మేము ఇంటర్నెట్లో సేకరించిన ADR ఉదాహరణ మూసలు:

- [Michael Nygard ADR మూస](మూసలు/michael-nygard-నిర్ణయ-రికార్డు-మూస/) (సరళమైనది, ప్రజాదరణ పొందినది)

- [Jeff Tyree, Art Akerman ADR మూస](మూసలు/jeff-tyree-art-akerman-నిర్ణయ-రికార్డు-మూస/) (మరింత అధునాతనమైనది)

- [అలెగ్జాండ్రియన్ నమూనా ADR మూస](మూసలు/అలెగ్జాండ్రియన్-నమూనా-నిర్ణయ-రికార్డు-మూస/) (సందర్భ ప్రత్యేకతలతో సరళమైనది)

- [వ్యాపార ప్రతిపాదన ADR మూస](మూసలు/వ్యాపార-ప్రతిపాదన-నిర్ణయ-రికార్డు-మూస/) (మరింత MBA-ఆధారితం, ఖర్చులు, SWOT, మరిన్ని అభిప్రాయాలతో)

- [Markdown Any Decision Records (MADR) ప్రాజెక్ట్ ADR మూస](మూసలు/madr-ప్రాజెక్ట్-నిర్ణయ-రికార్డు-మూస/) (సరళమైన, విపులమైన రెండు వెర్షన్లు; రెండోది ఎంపికలను, వాటి లాభనష్టాలను నొక్కి చెబుతుంది)

- [Planguage వాడే ADR మూస](మూసలు/planguage-నిర్ణయ-రికార్డు-మూస/) (మరింత నాణ్యతా హామీ ఆధారితం)

- [Ignacio Larrañaga రూపొందించిన ముఖ్యమైన సాంకేతిక నిర్ణయాల (ITDs) మూస](మూసలు/ముఖ్యమైన-సాంకేతిక-నిర్ణయాల-నిర్ణయ-రికార్డు-మూస/) (సన్నని, నిర్ణయం-మొదటి, వేగవంతమైన కార్యనిర్వాహక సమీక్షకు ఆప్టిమైజ్ చేయబడింది)

## ADRల కోసం బృందకృషి సలహా

మీ బృందంతో నిర్ణయ రికార్డులను వాడాలని ఆలోచిస్తుంటే, అనేక బృందాలతో పనిచేస్తూ మేము నేర్చుకున్న కొన్ని సలహాలు ఇక్కడ ఉన్నాయి.

"ఏమి చేయాలి" అని ఆదేశించడం కంటే "ఎందుకు" అనే దాని గురించి కలిసి మాట్లాడటం ద్వారా మీ సహచరులకు నాయకత్వం వహించే అవకాశం మీకు ఉంది. ఉదాహరణకు, నిర్ణయ రికార్డులు బృందాలు తెలివిగా ఆలోచించడానికి, మెరుగ్గా సంభాషించడానికి ఒక మార్గం; అవి కేవలం పని అయిపోయిన తర్వాత బలవంతంగా చేసే కాగితపు పని అవసరమైతే వాటికి విలువ ఉండదు.

కొన్ని బృందాలు "ADRలు" అనే సంక్షిప్త రూపం కంటే "నిర్ణయాలు" అనే పేరును ఎంతో ఇష్టపడతాయి. కొన్ని బృందాలు "decisions" అనే డైరెక్టరీ పేరు వాడినప్పుడు, ఒక బల్బు వెలిగినట్లు అవుతుంది, ఆ బృందం డైరెక్టరీలో విక్రేత నిర్ణయాలు, ప్రణాళిక నిర్ణయాలు, షెడ్యూల్ నిర్ణయాలు వంటి మరింత సమాచారాన్ని ఉంచడం ప్రారంభిస్తుంది. ఈ రకాల సమాచారమంతటికీ ఒకే మూసను వాడవచ్చు. మా ఊహ ఏమిటంటే, సంక్షిప్త రూపాల ("ADRలు") కంటే పదాల ("నిర్ణయాలు") ద్వారా ప్రజలు వేగంగా నేర్చుకుంటారు, "రికార్డు" అనే పదం తొలగించినప్పుడు పురోగతిలో ఉన్న పత్రాలు రాయడానికి ప్రజలు ఎక్కువ ప్రేరణ పొందుతారు, అలాగే కొందరు డెవలపర్లకు, కొందరు మేనేజర్లకు "ఆర్కిటెక్చర్" అనే పదం నచ్చదు.

సిద్ధాంతపరంగా, మార్పులేనితనం ఆదర్శం. ఆచరణలో, మార్చగలిగే విధానం మా బృందాలకు బాగా పనిచేసింది. ఉన్న ADRలో కొత్త సమాచారాన్ని తేదీ ముద్రతో, ఆ సమాచారం నిర్ణయం తర్వాత వచ్చిందనే గమనికతో చేరుస్తాం. ఈ రకమైన విధానం మనమంతా నవీకరించగల "సజీవ పత్రం"కు దారి తీస్తుంది. కొత్త సహచరుల వల్ల, కొత్త ఆఫర్ల వల్ల, మా వాడకాల వాస్తవ ఫలితాల వల్ల సమాచారం అందినప్పుడు, లేదా విక్రేత సామర్థ్యాలు, ధరల ప్రణాళికలు, లైసెన్స్ ఒప్పందాలు వంటి నిర్ణయం తర్వాత మూడవ పక్షాల మార్పుల వల్ల సాధారణంగా నవీకరణలు జరుగుతాయి.

## ADRల కోసం బృందకృషి ప్రశ్నలు

### ADR ఎవరు సృష్టించవచ్చు?

నిర్దిష్ట వ్యక్తులు, నిర్దిష్ట పాత్రలు, నిర్దిష్ట బృందాలు లేదా నిర్దిష్ట విభాగాల వంటి అంశాలను పరిగణించండి; అలాగే ADRను కమిషన్ చేయగల, అంటే మరొకరు రాసే ADRను అభ్యర్థించగల వ్యక్తులు, పాత్రలు, బృందాలు లేదా విభాగాలు ఉన్నాయో లేదో కూడా పరిగణించండి.

ఉదాహరణ సమాధానం: ఆర్కిటెక్చర్ నిర్ణయ రికార్డు README పేజీని చదివిన మా సంస్థలోని ఎవరైనా ADRను ప్రతిపాదించవచ్చు, అంటే ఆ వ్యక్తి దాన్ని రాయడం ప్రారంభించి, బృందంతో పంచుకోవచ్చు.

### ADR లేవనెత్తడాన్ని ఏది సమర్థిస్తుంది?

మీ సంస్థ బృందాల పని విధానాలు, మీ సాఫ్ట్వేర్ వ్యవస్థ నిర్మాణం, బృందాల మధ్య సమన్వయం, దీర్ఘకాలిక నిర్వహణ సౌలభ్యం, బాహ్య ఇంటర్ఫేస్లు, ఎవరికి ప్రయోజనం కలగాలని మీరు కోరుకుంటున్నారు వంటి అంశాలను పరిగణించండి.

ఉదాహరణ సమాధానం: భవిష్యత్తు డెవలపర్లు మేము చేస్తున్న దాని వెనుక ఉన్న "ఎందుకు"ను అర్థం చేసుకోవాలని కోరుకున్నప్పుడు మేము ADR సృష్టించాలనుకుంటాం.

### ADR లేవనెత్తకపోవడాన్ని ఏది సమర్థిస్తుంది?

ఆర్కిటెక్చర్కు సంబంధం లేని నిర్ణయాలు; కనీస ప్రమాదం ఉన్నవి, స్వయం-పూర్తి అయినవి లేదా ఒకే డెవలపర్కు సంబంధించినవి వంటి చిన్న నిర్ణయాలు; ప్రమాణాలు, విధానాలు లేదా డాక్యుమెంటేషన్ ద్వారా ఇప్పటికే పూర్తిగా వేరే చోట కవర్ అయిన నిర్ణయాలు; తాత్కాలిక పరిష్కారాలు, భావనా నిరూపణలు లేదా ప్రయోగాలు వంటి తాత్కాలికమైనవి వంటి అంశాలను పరిగణించండి.

ఉదాహరణ సమాధానం: ఒక నిర్ణయం పరిధి, సమయం, ప్రమాదం, ఖర్చు పరంగా పరిమితమైనప్పుడు, లేదా ఇప్పటికే వేరే చోట కవర్ అయినప్పుడు మేము ADRను వదిలివేయాలనుకుంటాం.

### ADR జీవనచక్రం ఏమిటి?

సృష్టి ప్రక్రియ, పరిశోధన ప్రక్రియ, నిర్ణయ ప్రక్రియ, అమలు ప్రక్రియ, ముగింపు ప్రక్రియ వంటి అంశాలను పరిగణించండి. కాలక్రమేణా ADR జీవనచక్రాన్ని ఎలా ట్రాక్ చేయాలో, అంటే ADRని ఒక స్థితి నుండి తదుపరి స్థితికి ఎలా తరలించాలో, దీన్ని భాగస్వాములకు ఎలా తెలియజేయాలో పరిగణించండి.

ఉదాహరణ సమాధానం: ADRకు ఐదు జీవనచక్ర దశలు ఉండాలని మేము కోరుకుంటాం: ప్రారంభించడం → పరిశోధించడం → మూల్యాంకనం చేయడం → అమలు చేయడం → నిర్వహించడం → ముగించడం.

### ADR జీవనచక్ర దశలకు ప్రమాణాలు ఏమిటి?

ADRకు అంగీకార ప్రమాణాలు వంటి అంశాలను పరిగణించండి, అంటే ఒక జీవనచక్ర దశ నుండి తదుపరి దశకు వెళ్లడానికి అది తగినంత మంచిదని మీకు ఎలా తెలుస్తుంది? సమస్య స్పష్టంగా వివరించబడిందా? ప్రత్యామ్నాయాలను పరిగణించారా? రాజీలను తగినంతగా అర్థం చేసుకుని నమోదు చేశారా?
సంబంధిత సందర్భమంతా ఉందా? సంబంధిత భాగస్వాములందరూ పాల్గొన్నారా? అభిప్రాయమంతా చేర్చారా?

ఉదాహరణ సమాధానం: క్రియాశీల బృందం 1) తమ పరిశోధనను పూర్తి చేసినప్పుడు, 2) తమ మూల్యాంకనాన్ని పూర్తి చేసినప్పుడు, 3) వ్యాఖ్యల అభ్యర్థనతో, ఒక వారం గడువుతో ADR ప్రతిపాదనను భాగస్వాములకు ప్రచురించినప్పుడు, 4) భాగస్వాముల వ్యాఖ్యలన్నీ చేర్చి, పరిష్కరించినప్పుడు ADRపై భాగస్వాములు ఓటు వేయాలని మేము కోరుకుంటాం.

### ADRతో ఏ పాత్రలు, బాధ్యతలు సంబంధం కలిగి ఉంటాయి?

ప్రతిపాదకుడు, పరిశోధకుడు, మూల్యాంకనకర్త, సమీక్షకుడు, ఆమోదకుడు, నిర్వాహకుడు వంటి పాత్రలను పరిగణించండి. భాగస్వాములతో సంభాషణ, అంచనాలు నెరవేరేలా చూడటం, వెబ్సైట్ లేదా ఇంట్రానెట్లో పంచుకోవడం, పనిని కాలానుగుణంగా, ముఖ్యంగా సంబంధిత మార్పులు జరిగినప్పుడు సమీక్షించడం వంటి బాధ్యతలను పరిగణించండి.

ఉదాహరణ సమాధానం: ప్రతి ADRకు ఎల్లప్పుడూ ఒక ప్రాథమిక సంప్రదింపు వ్యక్తి, ఒక ద్వితీయ సంప్రదింపు వ్యక్తి, ఒక జవాబుదారీ బృందం ఉండాలని మేము కోరుకుంటాం; వీరు సంభాషణలు, ప్రచురణలు, నిర్వహణ, కనీసం సంవత్సరానికి ఒకసారి కాలానుగుణ సమీక్ష, అవసరమైనప్పుడు చివరికి ముగింపు బాధ్యత వహిస్తారు.

### పాలన ADRతో ఎలా సంబంధం కలిగి ఉంటుంది?

మీ సంస్థ పని విధానాలు, చట్టపరమైన లేదా మానవ వనరుల అంశాలకు సంబంధించిన ప్రత్యేక వర్తింపు అవసరాలు, ఏకాభిప్రాయం, సంఘర్షణ, ఉన్నతస్థాయికి తీసుకెళ్లడం (ఎస్కలేషన్) అనే వాటిని మీరు ఎలా నిర్వహించాలనుకుంటున్నారు వంటి అంశాలను పరిగణించండి. ADR విషయంలో ఇతరుల కంటే ఎక్కువ ప్రభావం చూపగల, ఉదాహరణకు దాన్ని ఆమోదించగల, దానిపై ఓటు వేయగల లేదా వీటో చేయగల రంగాలు, వ్యక్తులు లేదా బృందాలు ఉన్నాయా?

ఉదాహరణ సమాధానం: ADR పాలన ఈ ప్రాధాన్యతా క్రమంలో ఉంటుంది: CEO, CTO, CLO, ADRను అమలు చేసే బృందం, ఆ ADకి సంబంధించి అత్యంత పరిజ్ఞానం ఉన్న బృంద నిపుణులు. ADRలో వివరించకపోతే మరెవరికీ పాలన అధికారం ఉండదు.

### ఏ సూత్రాలు ADRతో సంబంధం కలిగి ఉంటాయి?

వేగంగా కదలడం, నెమ్మదిగా కదలడం; నిర్ణయ ఏకాభిప్రాయం, నిర్ణయ సంఘర్షణ; ప్రమాద ప్రాధాన్యతలు, భద్రత ప్రాధాన్యతలు; బహిరంగ చర్చ, ప్రైవేట్ చర్చ వంటివి కలిగిన మీ సంస్థ పని విధానాల వంటి అంశాలను పరిగణించండి.

ఉదాహరణ సమాధానం: మేము చర్యకు ప్రాధాన్యం, విభేదించి కట్టుబడి ఉండటం, సులభంగా వెనక్కి తీసుకోగల, సులభంగా వేరు చేయగల నిర్ణయాలకు 70% అంచనాలు సరిపోతాయి అనే నాయకత్వ సూత్రాలను, మా సంస్థ గోప్యతా ఒప్పందంలో వివరించిన రహస్య సమాచారం మినహా బహిరంగ పని విధానాలను అనుసరిస్తాం.

## ADRల కోసం తదుపరి దశ భావనలు

[Arc42](https://arc42.org/) రెండు ప్రశ్నలకు ఆచరణాత్మక పద్ధతిలో సమాధానం ఇస్తుంది, మీ నిర్దిష్ట అవసరాలకు అనుగుణంగా మార్చుకోవచ్చు. మీ ఆర్కిటెక్చర్ గురించి మీరు ఏమి డాక్యుమెంట్ చేయాలి/తెలియజేయాలి? ఎలా డాక్యుమెంట్ చేయాలి/తెలియజేయాలి? Arc42లో ఆర్కిటెక్చర్ నిర్ణయ రికార్డులతో పాటు లక్ష్యాలు, పరిమితులు, సందర్భాలు, నాణ్యత, ప్రమాదాలు, మరిన్నింటిపై మార్గదర్శకత్వం ఉంటుంది.

[C4 మోడల్](https://c4model.com/) అనేది సాఫ్ట్వేర్ ఆర్కిటెక్చర్ రేఖాచిత్రణకు నేర్చుకోవడానికి సులభమైన, డెవలపర్-స్నేహపూర్వక విధానం. C4 అనేది సందర్భం, కంటైనర్లు, కాంపోనెంట్లు, కోడ్ కోసం క్రమానుగత రేఖాచిత్రాల సమితి, అలాగే సిస్టమ్ ల్యాండ్స్కేప్, డైనమిక్, డిప్లాయ్మెంట్ కోసం సహాయక రేఖాచిత్రాలు.

## ఆర్కిటెక్చర్ రేఖాచిత్రాలు, వీక్షణలు, దృక్కోణాలు

ఆర్కిటెక్చర్ రేఖాచిత్రాన్ని "ఆర్కిటెక్చర్ వీక్షణ" అంటారు.

"ఆర్కిటెక్చర్ వీక్షణ" అనేది "ఆర్కిటెక్చర్ దృక్కోణం"కు ఒక ఉదాహరణ.

"ఆర్కిటెక్చర్ దృక్కోణం"కు నిర్దిష్ట ఆందోళనలను దృష్టిలో ఉంచుకున్న నిర్దిష్ట ప్రేక్షకులు ఉంటారు.

ఆర్కిటెక్చర్ దృక్కోణ ఉదాహరణలు, వీక్షణ ఉదాహరణలు, రేఖాచిత్ర ఉదాహరణలు:

- వ్యాపార సామర్థ్యాలు (Business Capabilities)

- ఉన్నత-స్థాయి వ్యాపార ప్రక్రియలు

- [విలువ ప్రవాహాలు (Value Streams)](https://en.wikipedia.org/wiki/Value_stream)

- అప్లికేషన్ కాంపోనెంట్లకు మ్యాప్ చేసిన సాఫ్ట్వేర్ ఫంక్షన్లు

- [C4 మోడల్](https://en.wikipedia.org/wiki/C4_model) సందర్భ రేఖాచిత్రం (TO-BE / AS-IS)

- [C4 మోడల్](https://en.wikipedia.org/wiki/C4_model) కంటైనర్ రేఖాచిత్రం (TO-BE / AS-IS)

- డేటా ఎంటిటీలను అప్లికేషన్ కాంపోనెంట్లకు మ్యాప్ చేసే [ఎంటిటీ-రిలేషన్షిప్ రేఖాచిత్రం](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD)

- వ్యవస్థలలోపల, ఇంటిగ్రేషన్ల కోసం ఫంక్షనల్ ప్రవాహాలను వివరించే [సీక్వెన్స్ రేఖాచిత్రాలు](https://en.wikipedia.org/wiki/Sequence_diagram)

- అప్లికేషన్ కాంపోనెంట్ల అంతటా డేటా ప్రవాహాలను వివరించే [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) రేఖాచిత్రాలు

- వ్యాపార ప్రక్రియలు / వినియోగదారు దృశ్యాలను వివరించే [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) రేఖాచిత్రాలు

- [గుర్తింపు, ప్రాప్యత నిర్వహణ (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) రేఖాచిత్రాలు

- ప్రతి అప్లికేషన్ కాంపోనెంట్కు పాత్రలతో కూడిన [పాత్ర-ఆధారిత ప్రాప్యత నియంత్రణ (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) రేఖాచిత్రాలు

- ప్రతి అప్లికేషన్ కాంపోనెంట్కు లక్షణాలతో కూడిన [లక్షణ-ఆధారిత ప్రాప్యత నియంత్రణ (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) రేఖాచిత్రాలు

- గోప్యతా రేఖాచిత్రాలు

సంబంధిత రేఖాచిత్రాలు:

- వినియోగ సందర్భ రేఖాచిత్రం (Use Case Diagram) నిర్వహణ/కస్టమర్లకు వినియోగ సందర్భాలను చూపుతుంది, ఇది అవసరాలకు ముందు వస్తుంది, అవి సాఫ్ట్వేర్ ఆర్కిటెక్చర్కు ముందు వస్తాయి.

- డిప్లాయ్మెంట్ రేఖాచిత్రం (Deployment Diagram) సాఫ్ట్వేర్ కాంపోనెంట్లు డిప్లాయ్ చేయబడే భౌతిక హార్డ్వేర్/కంప్యూటర్లను చూపుతుంది.
- డేటా ఫ్లో రేఖాచిత్రం (Data Flow Diagram) డేటా వ్యవస్థ ద్వారా ఎలా కదులుతుందో, ఎలా రూపాంతరం చెందుతుందో చూపుతుంది.
- సీక్వెన్స్ రేఖాచిత్రం (Sequence Diagram) HTTP వంటి ప్రోటోకాల్లు సమయ అక్షంపై ఎలా పనిచేస్తాయో చూపడానికి వాడతారు.

- కార్యకలాప రేఖాచిత్రం (Activity Diagram) NPC AI వంటి సాఫ్ట్వేర్ వ్యవస్థ చేపట్టే కార్యకలాపాల వర్క్ఫ్లోను వర్ణిస్తుంది.

## కోడ్ రూపంలో నిర్ణయాలకు ఫిట్నెస్ ఫంక్షన్లు

ఫిట్నెస్ ఫంక్షన్లు అనేవి నిర్ణయాలు కొనసాగుతున్నాయని ధృవీకరించే, ప్రోగ్రామింగ్ కోడ్తో రాసిన, లక్ష్యాత్మక స్వయంచాలక తనిఖీలు.

- ఫిట్నెస్ ఫంక్షన్లు నిర్ణయాలను పరీక్షించదగినవిగా, హామీ ఇవ్వదగినవిగా చేస్తాయి.

- నిర్ణయాలకు ఫిట్నెస్ ఫంక్షన్లు నాణ్యతా హామీకి, నియంత్రణ ప్రక్రియలకు, పాలన లక్ష్యాలకు ఎంతగానో సహాయపడతాయి.

### ఫిట్నెస్ ఫంక్షన్లు నిర్ణయాలతో ఎలా అనుసంధానమవుతాయి

నిర్ణయ రికార్డు నిర్ణయాన్ని నమోదు చేస్తుంది, ఫిట్నెస్ ఫంక్షన్ ఆ నిర్ణయానికి హామీ ఇస్తుంది.

- ఉదాహరణ నిర్ణయం: ఆడిట్ అవసరాల కోసం మేము ఈవెంట్ సోర్సింగ్ను వాడతాం.

- ఉదాహరణ ఫిట్నెస్ ఫంక్షన్: అన్ని స్థితి మార్పులు తప్పనిసరిగా ఈవెంట్లను ఉత్పత్తి చేయాలని పరీక్షించడానికి మేము నిరంతర ఇంటిగ్రేషన్ సర్వర్ను వాడతాం.

### ఫిట్నెస్ ఫంక్షన్లు నిర్ణయాలకు ఎందుకు సహాయపడతాయి

లక్ష్యాత్మక కొలతలు: ఫిట్నెస్ ఫంక్షన్లు పాస్ లేదా ఫెయిల్ అవుతాయి, కాబట్టి పని కనిపిస్తూ, స్పష్టంగా ఉంటుంది.

నిరంతర వాడకం: ఫిట్నెస్ ఫంక్షన్లు మీ సజీవ నియమాలు, ప్రతి కమిట్, బిల్డ్లో నడుస్తాయి.

రీఫ్యాక్టర్ చేసే విశ్వాసం: ఫిట్నెస్ ఫంక్షన్లు నిర్ణయ నియమ దోషాలను స్వయంచాలకంగా పట్టుకుంటాయి.

విస్తరించదగిన పాలన: ఫిట్నెస్ ఫంక్షన్లు అడ్డంకులు సృష్టించకుండా ప్రమాణాలకు హామీ ఇస్తాయి.

### ఫిట్నెస్ ఫంక్షన్లు AIని వాడగలవా?

ఫిట్నెస్ ఫంక్షన్లు మీ ప్రణాళికలు, కోడ్, స్కీమాలు, APIలు మరిన్ని వంటి మీ పని గురించి ప్రశ్నలు అడగడం ద్వారా నిర్ణయాల కోసం AI LLMలను ఉపయోగించుకోగలవు:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### ఆర్కిటెక్చర్ యూనిట్ టెస్టింగ్

[ArchUnit](https://www.archunit.org/): ఏదైనా సాధారణ Java యూనిట్ టెస్ట్ ఫ్రేమ్వర్క్ను వాడి Java కోడ్ ఆర్కిటెక్చర్ నియమాలను తనిఖీ చేయండి.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): Jest, Vitest, Jasmine మొదలైన వాటిని వాడి TypeScript కోడ్, JavaScript కోడ్ ఆర్కిటెక్చర్ నియమాలను తనిఖీ చేయండి.

## పుల్ రిక్వెస్ట్ల కోసం నిర్ణయ రక్షణలు

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
ఒక డెవలపర్ ఆ నిర్ణయాలు కవర్ చేసే కోడ్ను చురుకుగా మార్చేటప్పుడు, సరైన క్షణంలో
సరైన నిర్ణయ రికార్డులను ఆటోమేటిక్గా ముందుకు తెస్తుంది. విలీనం చేయడానికి ముందు
డెవలపర్లు డాక్స్ ఫోల్డర్ను చదువుతారని ఆశించే బదులు, సంబంధిత సందర్భం నేరుగా
పుల్ రిక్వెస్ట్లో కనిపిస్తుంది.

ఇది ప్రతి రకమైన నిర్ణయ రికార్డుకూ పనిచేస్తుంది: ఆర్కిటెక్చర్ నిర్ణయాలు, డేటా
నిర్ణయాలు, వర్తింపు నిర్ణయాలు, క్లినికల్, వైద్య నిర్ణయాలు, భద్రతా నిర్ణయాలు, మరిన్ని.

ఏ CI వ్యవస్థతోనైనా (GitLab, Jenkins, CircleCI), pre-commit హుక్గా కూడా పనిచేస్తుంది.
ఓపెన్ సోర్స్. MIT లైసెన్స్.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) అనేది ఒక GitHub
Action, ఇది ఆర్కిటెక్చర్ నిర్ణయ రికార్డును జోడించకుండా లేదా నవీకరించకుండా పర్యవేక్షిస్తున్న కోడ్ మార్గాలు మారినప్పుడు
పుల్ రిక్వెస్ట్ను విఫలం చేస్తుంది. మినహాయింపులు స్పష్టంగా ఉంటాయి:
కారణంతో కూడిన `ADR-Exempt:` పంక్తి గేట్ను దాటిస్తుంది, జాబ్ సారాంశంలో నమోదు చేయబడుతుంది.
మూస-నిరపేక్షం, ఆధారితాలు లేవు. ఓపెన్ సోర్స్. MIT లైసెన్స్.

## మరింత సమాచారం కోసం

పరిచయం:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

మూసలు:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

లోతుగా:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - ఉచిత నెలవారీ సాఫ్ట్వేర్ ఆర్కిటెక్చర్ పాఠం

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

సాధనాలు:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

కంపెనీ-నిర్దిష్ట మార్గదర్శకత్వం:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

ఉదాహరణలు:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

వీడియోలు:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

పాడ్కాస్ట్లు:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

పుస్తకాలు:

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

ఇవి కూడా చూడండి:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - స్పష్టమైన తర్కం, ఊహలు, జ్ఞానాత్మక స్థితి, రాజీలతో నిర్ణయాలను సూచించడానికి విక్రేత-తటస్థ, యంత్రం చదవగల YAML/JSON ఫార్మాట్. నిర్ణయ డాక్యుమెంటేషన్కు నిర్మాణాత్మక, ధృవీకరించదగిన తర్కాన్ని జోడించడం ద్వారా ADRలకు తోడ్పడుతుంది.
