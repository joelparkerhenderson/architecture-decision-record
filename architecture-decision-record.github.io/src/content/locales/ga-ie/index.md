# Taifead cinnidh ailtireachta (ADR)

Is éard is taifead cinnidh ailtireachta (ADR) ann ná doiciméad a thaifeadann cinneadh tábhachtach ailtireachta a rinneadh mar aon lena chomhthéacs agus a iarmhairtí.

> [!IMPORTANT]
> Déan do dhícheall cuí féin ar na hacmhainní seo sula n-úsáideann tú iad in aon chórais chriticiúla.

Ábhar:

- [Cad is taifead cinneadh ailtireachta ann?](#cad-is-taifead-cinneadh-ailtireachta-ann)
- [Conas tosú ag úsáid ADR](#conas-tosú-ag-úsáid-adr)
- [Conas tosú ag úsáid ADR le huirlisí](#conas-tosú-ag-úsáid-adr-le-huirlisí)
- [Conas tosú ag úsáid ADR le git](#conas-tosú-ag-úsáid-adr-le-git)
- [Scileanna Claude Code do ADR](#scileanna-claude-code-do-adr)
- [Coinbhinsiúin ainmniúcháin comhad do ADR](#coinbhinsiúin-ainmniúcháin-comhad-do-adr)
- [Moltaí chun ADR maithe a scríobh](#moltaí-chun-adr-maithe-a-scríobh)
- [Samplaí de theimpléid ADR](#samplaí-de-theimpléid-adr)
- [Comhairle oibre foirne do ADR](#comhairle-oibre-foirne-do-adr)
- [Ceisteanna oibre foirne do ADR](#ceisteanna-oibre-foirne-do-adr)
- [Coincheapa céim eile do ADR](#coincheapa-céim-eile-do-adr)
- [Léaráidí ailtireachta & radhairc & dearcthaí](#léaráidí-ailtireachta--radhairc--dearcthaí)
- [Feidhmeanna oiriúnachta do chinntí mar chód](#feidhmeanna-oiriúnachta-do-chinntí-mar-chód)
- [Cosaintí cinntí d'iarratais tharraingthe](#cosaintí-cinntí-diarratais-tharraingthe)
- [Tuilleadh eolais](#tuilleadh-eolais)

Teimpléid:

- [Teimpléad taifid chinnidh le Jeff Tyree agus Art Akerman](teimpleid/teimplead-taifid-chinnidh-jeff-tyree-agus-art-akerman/)
- [Teimpléad taifid chinnidh le Michael Nygard](teimpleid/teimplead-taifid-chinnidh-michael-nygard/)
- [Teimpléad taifid chinnidh le EdgeX](teimpleid/teimplead-taifid-chinnidh-edgex/)
- [Teimpléad taifid chinnidh le arc42](teimpleid/teimplead-taifid-chinnidh-arc42/)
- [Teimpléad taifid chinnidh do phatrún Alexandrian](teimpleid/teimplead-taifid-chinnidh-do-phatrun-alexandrian/)
- [Teimpléad taifid chinnidh do chás gnó](teimpleid/teimplead-taifid-chinnidh-do-chas-gno/)
- [Teimpléad taifid chinnidh de chuid Thionscadal MADR](teimpleid/teimplead-taifid-chinnidh-de-chuid-thionscadal-madr/)
- [Teimpléad taifid chinnidh ag úsáid Planguage](teimpleid/teimplead-taifid-chinnidh-ag-usaid-planguage/)
- [Teimpléad taifid chinnidh le Paulo Merson](https://github.com/pmerson/ADR-template)
- [Teimpléad taifid chinnidh le Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Teimpléad taifid chinnidh le Gareth Morgan](teimpleid/teimplead-taifid-chinnidh-gareth-morgan/)
- [Teimpléad taifid chinnidh le GIG Cymru NHS Wales](teimpleid/teimplead-taifid-chinnidh-gig-cymru-nhs-wales/)
- [Teimpléad taifid chinnidh do Chinntí Teicniúla Tábhachtacha (ITDanna) le Ignacio Larrañaga](teimpleid/teimplead-taifid-chinnidh-do-chinnti-teicniula-tabhachtacha/)

Samplaí:

- [Creat CSS](samplai/creat-css/)
- [Cumraíocht athróg timpeallachta](samplai/cumraiocht-athrog-timpeallachta/)
- [Méadrachtaí, monatóirí, foláirimh](samplai/meadrachtai-monatoiri-folairimh/)
- [Microsoft Azure DevOps](samplai/microsoft-azure-devops/)
- [Monorepo nó multirepo](samplai/monorepo-no-multirepo/)
- [Teangacha ríomhchlárúcháin](samplai/teangacha-riomhchlaruchain/)
- [Stóráil rún](samplai/storail-ruin/)
- [Formáid stampa ama](samplai/formaid-stampa-ama/)
- [An-chuid eile...](samplai/)

## Cad is taifead cinneadh ailtireachta ann?

Is éard is **taifead cinneadh ailtireachta** (ADR) ann ná doiciméad a thaifeadann cinneadh tábhachtach ailtireachta a rinneadh, mar aon lena chomhthéacs agus a iarmhairtí.

Is éard is **cinneadh ailtireachta** (AD) ann ná rogha i ndearadh bogearraí a thugann aghaidh ar riachtanas suntasach.

Is éard is **logchomhad cinneadh ailtireachta** (ADL) ann ná bailiúchán de na ADR uile a cruthaíodh agus a chothaítear do thionscadal (nó d'eagraíocht) áirithe.

Is éard is **riachtanas suntasach ó thaobh na hailtireachta de** (ASR) ann ná riachtanas a bhfuil tionchar intomhaiste aige ar ailtireacht chórais bogearraí.

Baineann an méid seo ar fad le hábhar **bainistíocht eolais ailtireachta** (AKM).

Is é cuspóir an doiciméid seo forbhreathnú tapa a thabhairt ar ADR, conas iad a chruthú, agus cá háit a bhfaighfear tuilleadh eolais.

Giorrúcháin:

  * **AD**: cinneadh ailtireachta

  * **ADL**: logchomhad cinneadh ailtireachta

  * **ADR**: taifead cinneadh ailtireachta

  * **AKM**: bainistíocht eolais ailtireachta

  * **ASR**: riachtanas suntasach ó thaobh na hailtireachta de

## Conas tosú ag úsáid ADR

Chun tosú ag úsáid ADR, pléigh na réimsí seo le do chomhghleacaithe foirne.

Cinntí a aithint:

  * Cé chomh práinneach agus cé chomh tábhachtach is atá an AD?

  * An gcaithfear é a dhéanamh anois, nó an féidir fanacht go mbeidh níos mó ar eolas?

  * Is féidir le taithí phearsanta agus chomhchoiteann, chomh maith le modhanna agus cleachtais aitheanta dearaidh, cabhrú le cinntí a aithint.

  * Go hidéalach, coinnigh liosta de chinntí le déanamh a chomhlánaíonn liosta tascanna an táirge.

Cinntí a dhéanamh:

  * Tá roinnt teicnící cinnteoireachta ann, idir cinn ghinearálta agus cinn atá sainiúil don ailtireacht bogearraí, mar shampla, mapáil idirphlé (dialogue mapping).

  * Is ábhar taighde gníomhach é cinnteoireacht ghrúpa.

Cinntí a chur i bhfeidhm agus a fhorfheidhmiú:

  * Úsáidtear ADanna i ndearadh bogearraí; dá bhrí sin, ní mór iad a chur in iúl do gheallsealbhóirí an chórais a mhaoiníonn, a fhorbraíonn agus a oibríonn é, agus ní mór dóibh iad a ghlacadh.

  * Dhá chleachtas gaolmhara is ea stíleanna códaithe atá follasach ó thaobh na hailtireachta de agus athbhreithnithe cód a dhíríonn ar ábhair imní agus cinntí ailtireachta.

  * Ní mór ADanna a (ath)bhreithniú freisin nuair a dhéantar córas bogearraí a nuachóiriú i bhforbairt bogearraí.

Cinntí a roinnt (roghnach):

  * Tarlaíonn go leor ADanna arís agus arís eile ar fud tionscadal.

  * Dá bhrí sin, is féidir le taithí ar chinntí a rinneadh roimhe, idir mhaith agus dhona, a bheith ina sócmhainní luachmhara in-athúsáidte nuair a úsáidtear straitéis shoiléir bainistíochta eolais.

Cinntí a dhoiciméadú:

  * Tá go leor teimpléad agus uirlisí ann chun cinntí a ghabháil.

  * Féach pobail agile, m.sh. ADR de chuid M. Nygard.

  * Féach próisis thraidisiúnta innealtóireachta bogearraí agus dearadh ailtireachta, m.sh. leaganacha amach tábla a mholann IBM UMF agus Tyree agus Akerman ó CapitalOne.

Tuilleadh eolais:

  * Glacadh na céimeanna thuas ón iontráil Wikipedia ar [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Conas tosú ag úsáid ADR le huirlisí

- [MySpec](https://myspec.dev) — ardán uathoibrithe sonraíochtaí agus cinntí ailtireachta a struchtúrann bunreacht tionscadail, ailtireacht theicniúil, agus ADR i Markdown glan a sheirbheáiltear trí MCP.

Is féidir leat tosú ag úsáid ADR le huirlisí ar aon bhealach is mian leat.

Mar shampla:

  * Más maith leat Google Drive agus eagarthóireacht ar líne, is féidir leat Google Doc, nó Google Sheet, a chruthú.

  * Más maith leat rialú leaganacha foinse-chóid, amhail git, is féidir leat comhad a chruthú do gach ADR.

  * Más maith leat uirlisí pleanála tionscadail, amhail Atlassian Jira, is féidir leat rianaitheoir pleanála na huirlise a úsáid.

  * Más maith leat vicí, amhail MediaWiki, is féidir leat vicí ADR a chruthú.

## Conas tosú ag úsáid ADR le git

Más maith leat rialú leaganacha git, seo an chaoi a dtosaímid ag úsáid ADR le git do thionscadal bogearraí tipiciúil le cód foinse.

Cruthaigh eolaire do chomhaid ADR:

```sh
$ mkdir adr
```

Do gach ADR, cruthaigh comhad téacs, amhail `choose-database.md`:

```sh
$ vi choose-database.md
```

Scríobh aon rud is mian leat sa ADR. Féach ar na teimpléid sa taisclann seo le haghaidh smaointe.

Tiomnaigh an ADR do do thaisclann git.

## Scileanna Claude Code do ADR

Seolann an taisclann seo dhá scil [Claude Code](https://claude.com/claude-code) faoi [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), ionas gur féidir le gníomhaire códaithe AI ADR a scríobh agus a chothabháil mar a mholann an tionscadal seo:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — ginearálta, d'aon duine atá ag scríobh ADR in aon tionscadal. Cabhraíonn sé cinneadh a dhéanamh an teastaíonn ADR ó chinneadh, bunaíonn sé eolaire `adr/` nó `decisions/`, ainmníonn sé an comhad, roghnaíonn sé teimpléad as na haon chnámharlach déag atá comhthionscanta, agus scríobhann sé hailt Comhthéacs/Cinneadh/Iarmhairtí dhaingne.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — do chothabhálaithe na taisclainne seo go sonrach. Doiciméadaíonn sé leagan amach na taisclainne, an coinbhinsiún scátha README/logchaighdeán, agus na céimeanna cruinne chun teimpléad, sampla, nó nasc uirlise nua a chur leis.

Chun scil a úsáid, cóipeáil a fillteán isteach i `.claude/skills/` ag fréamh na taisclainne ina bhfuil tú ag obair (nó isteach i `~/.claude/skills/` chun é a chur ar fáil i ngach tionscadal), ansin iarr ar Claude Code ADR a scríobh nó a athbhreithniú.

## Coinbhinsiúin ainmniúcháin comhad do ADR

Má roghnaíonn tú do ADR a chruthú ag úsáid gnáthchomhad téacs, b'fhéidir gur mhaith leat coinbhinsiún ainmniúcháin comhad ADR a chruthú duit féin.

Is fearr linn coinbhinsiún ainmniúcháin comhad a bhfuil formáid shainiúil aige a úsáid.

Samplaí:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Ár gcoinbhinsiún ainmniúcháin comhad:

  * Tá frása briathartha sa mhodh ordaitheach san aimsir láithreach san ainm. Feabhsaíonn sé seo inléiteacht agus tá sé ag teacht lenár bhformáid teachtaireachtaí tiomanta.

  * Úsáideann an t-ainm litreacha beaga agus fleiscíní (mar an gcéanna leis an taisclann seo). Is cothromaíocht é seo idir inléiteacht agus inúsáidteacht an chórais.

  * Is markdown an iarmhír. Féadann sé seo a bheith úsáideach le haghaidh formáidithe éasca.

## Moltaí chun ADR maithe a scríobh

Tréithe ADR mhaith:

* Réasúnaíocht: Mínigh na cúiseanna le AD ar leith a dhéanamh. Féadfaidh sé seo an comhthéacs (féach thíos), buntáistí agus míbhuntáistí roghanna éagsúla féideartha, comparáidí gnéithe, plé costais/tairbhe, agus níos mó a áireamh.

* Sainiúil: Ba cheart go mbeadh gach ADR faoi AD amháin, ní faoi ADanna iomadúla.

* Stampaí ama: Sainaithin cén uair a scríobhadh gach mír sa ADR. Tá sé seo tábhachtach go háirithe do ghnéithe a d'fhéadfadh athrú le himeacht ama, amhail costais, sceidil, scálú, agus a leithéid.

* Do-athraithe: Ná hathraigh faisnéis atá sa ADR cheana. Ina ionad sin, leasaigh an ADR trí fhaisnéis nua a chur leis, nó cuir ADR nua ina ionad trí ADR nua a chruthú.

Tréithe sraith mhaith “Comhthéacs” i ADR:

* Mínigh cás d'eagraíochta agus tosaíochtaí gnó.

* Cuir réasúnaíocht agus breithnithe bunaithe ar chomhdhéanamh sóisialta agus scileanna do fhoirne san áireamh.

* Cuir buntáistí agus míbhuntáistí ábhartha san áireamh, agus déan cur síos orthu i dtéarmaí atá ag teacht le do riachtanais agus do spriocanna.

Tréithe sraith mhaith “Iarmhairtí” i ADR:

* Mínigh an méid a leanann as an gcinneadh a dhéanamh. Féadfaidh sé seo éifeachtaí, torthaí, aschuir, obair leantach, agus níos mó a áireamh.

* Cuir faisnéis faoi aon ADR ina dhiaidh sin san áireamh. Is minic go spreagann ADR amháin gá le tuilleadh ADR, mar shampla nuair a dhéanann ADR amháin rogha mhór fhoriomlán, a chruthaíonn riachtanais do chinntí níos lú.

* Cuir aon phróisis athbhreithnithe iarghníomhaíochta san áireamh. Is gnách d'fhoirne gach ADR a athbhreithniú mí ina dhiaidh sin, chun faisnéis an ADR a chur i gcomparáid leis an méid a tharla i ndáiríre, chun foghlaim agus fás.

Féadfaidh ADR nua teacht in ionad ADR roimhe:

* Nuair a dhéantar AD a thagann in ionad ADR roimhe nó a chuireann ar neamhní é, ba cheart ADR nua a chruthú

## Samplaí de theimpléid ADR

Samplaí de theimpléid ADR a bhailigh muid ar an ngréasán:

- [Teimpléad ADR le Michael Nygard](teimpleid/teimplead-taifid-chinnidh-michael-nygard/) (simplí agus coitianta)

- [Teimpléad ADR le Jeff Tyree agus Art Akerman](teimpleid/teimplead-taifid-chinnidh-jeff-tyree-agus-art-akerman/) (níos sofaisticiúla)

- [Teimpléad ADR do phatrún Alexandrian](teimpleid/teimplead-taifid-chinnidh-do-phatrun-alexandrian/) (simplí le sonraí comhthéacs)

- [Teimpléad ADR do chás gnó](teimpleid/teimplead-taifid-chinnidh-do-chas-gno/) (níos dírithe ar MBA, le costais, SWOT, agus tuilleadh tuairimí)

- [Teimpléad ADR de chuid thionscadal Markdown Any Decision Records (MADR)](teimpleid/teimplead-taifid-chinnidh-de-chuid-thionscadal-madr/) (leagan simplí agus leagan casta; cuireann an ceann deireanach béim ar roghanna agus a mbuntáistí agus a míbhuntáistí)

- [Teimpléad ADR ag úsáid Planguage](teimpleid/teimplead-taifid-chinnidh-ag-usaid-planguage/) (níos dírithe ar chinnteacht cháilíochta)

- [Teimpléad do Chinntí Teicniúla Tábhachtacha (ITDanna) le Ignacio Larrañaga](teimpleid/teimplead-taifid-chinnidh-do-chinnti-teicniula-tabhachtacha/) (caol agus cinneadh-ar-dtús, barrfheabhsaithe d'athbhreithniú tapa feidhmiúcháin)

## Comhairle oibre foirne do ADR

Má tá tú ag smaoineamh ar thaifid chinntí a úsáid le do fhoireann, seo roinnt comhairle a d'fhoghlaimíomar trí oibriú le go leor foirne.

Tá deis agat do chomhghleacaithe foirne a threorú, trí labhairt le chéile faoin “cén fáth”, seachas an “cad é” a ordú. Mar shampla, is bealach iad taifid chinntí chun go smaoineoidh foirne níos cliste agus go gcumarsáidfidh siad níos fearr; níl taifid chinntí luachmhar mura bhfuil iontu ach riachtanas páipéarachais éigeantach i ndiaidh an ama.

Is fearr le roinnt foirne go mór an t-ainm “cinntí” ná an giorrúchán “ADR”. Nuair a úsáideann roinnt foirne ainm an eolaire “decisions”, is amhail is go gcasann bolgán solais air, agus tosaíonn an fhoireann ag cur tuilleadh faisnéise isteach san eolaire, amhail cinntí díoltóra, cinntí pleanála, cinntí sceidealaithe, srl. Is féidir an teimpléad céanna a úsáid do na cineálacha faisnéise seo ar fad. Tá hipitéis againn go bhfoghlaimíonn daoine níos tapúla le focail (“cinntí”) seachas le giorrúcháin (“ADR”), go bhfuil daoine níos spreagtha chun doiciméid atá idir lámha a scríobh nuair a bhaintear an focal “taifead”, agus freisin nach dtaitníonn an focal “ailtireacht” le roinnt forbróirí agus le roinnt bainisteoirí.

I dteoiric, is idéalach é an do-athraitheacht. I gcleachtas, d'oibrigh an inathraitheacht níos fearr dár bhfoirne. Cuirimid an fhaisnéis nua isteach sa ADR atá ann cheana, le stampa dáta, agus nóta gur tháinig an fhaisnéis tar éis an chinnidh. Tugann cur chuige den sórt seo “doiciméad beo” dúinn is féidir linn go léir a nuashonrú. Is iondúil go dtarlaíonn nuashonruithe nuair a fhaighimid faisnéis a bhuí le comhghleacaithe foirne nua, nó le tairiscintí nua, nó le torthaí fíorshaoil ár n-úsáide, nó tar éis athruithe tríú páirtí i ndiaidh an ama amhail cumais díoltóra, pleananna praghsála, comhaontuithe ceadúnais, srl.

## Ceisteanna oibre foirne do ADR


### Cé a fhéadann ADR a chruthú?

Smaoinigh ar réimsí amhail daoine ar leith, róil ar leith, foirne ar leith, nó ranna ar leith; smaoinigh freisin an bhfuil daoine, róil, foirne, nó ranna ann is féidir leo ADR a choimisiúnú, rud a chiallaíonn go n-iarrann siad ceann a scríobhfaidh duine eile. 

Sampla freagra: Féadfaidh aon duine inár n-eagraíocht a léigh leathanach README an taifid chinnidh ailtireachta ADR a mholadh, rud a chiallaíonn gur féidir leis an duine tosú á scríobh, agus é a roinnt leis an bhfoireann.

### Cad a thugann údar le ADR a ardú?

Smaoinigh ar réimsí amhail bealaí oibre foirne d'eagraíochta, struchtúr do chórais bhogearraí, comhordú idir-fhoirne, inchothaitheacht fhadtéarmach, comhéadain sheachtracha, cé ba mhaith leat tairbhe a bhaint, agus a leithéid. 

Sampla freagra: Ba mhaith linn ADR a chruthú nuair is mian linn go dtuigfidh forbróirí sa todhchaí an “cén fáth” leis an méid atá á dhéanamh againn.

### Cad a thugann údar gan ADR a ardú?

Smaoinigh ar réimsí amhail cinntí nach bhfuil faoin ailtireacht, nó atá an-bheag amhail íosriosca nó féinchuimsitheach nó forbróir aonair, nó atá clúdaithe go hiomlán in áit eile cheana amhail ag caighdeáin nó polasaithe nó doiciméadú, nó atá sealadach amhail réitigh shealadacha nó cruthúnais choincheapa nó turgnaimh. 

Sampla freagra: Ba mhaith linn ADR a fhágáil ar lár nuair atá cinneadh teoranta ó thaobh scóipe agus ama agus riosca agus costais, nó nuair atá sé clúdaithe in áit eile cheana.

### Cad é saolré ADR?

Smaoinigh ar réimsí amhail an próiseas cruthaithe, próiseas taighde, próiseas cinnteoireachta, próiseas cur chun feidhme, agus próiseas deireadh seirbhíse. Smaoinigh ar an gcaoi ar féidir saolré an ADR a rianú le himeacht ama, amhail conas an ADR a bhogadh ó staid amháin go dtí an chéad staid eile, agus conas é seo a chur in iúl do gheallsealbhóirí. 

Sampla freagra: Ba mhaith linn go mbeadh cúig chéim saolré ag ADR: Tionscnamh → Taighde → Meastóireacht → Cur chun feidhme → Cothabháil → Deireadh seirbhíse.

### Cad iad na critéir do chéimeanna saolré ADR?

Smaoinigh ar réimsí amhail critéir ghlactha do ADR, rud a chiallaíonn conas a bhfuil a fhios agat go bhfuil sé maith go leor chun dul ar aghaidh ó chéim saolré amháin go dtí an chéad cheann eile? An bhfuil an fhadhb sainithe go soiléir? An bhfuil na roghanna eile breithnithe? An bhfuil cothromaíochtaí tuigthe agus doiciméadaithe go maith?
An bhfuil an comhthéacs ábhartha go léir i bhfeidhm? An bhfuil na geallsealbhóirí ábhartha go léir páirteach? An bhfuil an t-aiseolas go léir ionchorpraithe? 

Sampla freagra: Ba mhaith linn go vótálfaidh geallsealbhóirí ar ADR nuair atá an fhoireann ghníomhach 1) tar éis a gcuid taighde a chur i gcrích, 2) tar éis a meastóireacht a chur i gcrích, 3) tar éis togra ADR a fhoilsiú do na geallsealbhóirí le hiarratas ar thuairimí agus teorainn ama de sheachtain amháin, 4) go bhfuil gach tuairim geallsealbhóra ionchorpraithe agus freagartha.

### Cad iad na róil agus freagrachtaí a idirghníomhaíonn le ADR?

Smaoinigh ar róil amhail moltóir, taighdeoir, meastóir, athbhreithneoir, formheasóir, cothabhálaí, agus a leithéid. Smaoinigh ar fhreagrachtaí amhail cumarsáid le geallsealbhóirí, a chinntiú go gcomhlíontar ionchais, roinnt ar an suíomh gréasáin nó an intranet, agus athbhreithniú an tsaothair go tréimhsiúil agus go háirithe nuair a tharlaíonn athruithe ábhartha.

Sampla freagra: Ba mhaith linn go mbeadh príomhdhuine teagmhála, dara duine teagmhála, agus foireann chuntasach ag gach ADR i gcónaí; tá siad seo freagrach as cumarsáid, foilseacháin, cothabháil, athbhreithniú tréimhsiúil uair sa bhliain ar a laghad, agus deireadh seirbhíse deiridh de réir mar is gá.

### Conas a idirghníomhaíonn rialachas le ADR?

Smaoinigh ar réimsí amhail bealaí oibre d'eagraíochta, aon riachtanais chomhlíonta speisialta amhail do ghnéithe dlí nó gnéithe acmhainní daonna, conas ba mhaith leat comhdhearcadh a láimhseáil seachas coinbhleacht seachas ardú. An bhfuil réimsí nó daoine nó foirne ann a bhfuil níos mó tionchair acu ná cinn eile maidir le ADR, amhail a bheith in ann é a fhormheas, nó vótáil air, nó veto a chur air?

Sampla freagra: Is é seo ord tosaíochta rialachas ADR: an POF, an CTO, an CLO, an fhoireann a chuireann ADR i bhfeidhm, na saineolaithe ar an bhfoireann is eolaí ar an AD. Níl rialachas ag aon duine eile mura bhfuil sé léirithe sa ADR. 

### Cad iad na prionsabail a idirghníomhaíonn le ADR?

Smaoinigh ar réimsí amhail bealaí oibre d'eagraíochta lena n-áirítear bogadh go tapa seachas bogadh go mall, do chomhdhearcadh cinnidh seachas coinbhleacht chinnidh, agus do roghanna riosca seachas roghanna sábháilteachta, plé poiblí seachas plé príobháideach, agus a leithéid.

Sampla freagra: Úsáidimid na prionsabail cheannaireachta claonadh i dtreo gníomhaíochta (bias for action), easaontú-agus-tiomantas (disagree-and-commit), is leor meastacháin 70% do chinntí atá furasta a aisiompú agus furasta a leithlisiú, agus bealaí oibre poiblí ach amháin faisnéis rúnda mar a thuairiscítear inár gcomhaontú rúndachta eagraíochta.

## Coincheapa céim eile do ADR

Freagraíonn [Arc42](https://arc42.org/) dhá cheist ar bhealach pragmatach agus is féidir é a oiriúnú do do riachtanais shonracha. Cad ba cheart duit a dhoiciméadú/a chur in iúl faoi d'ailtireacht? Conas ba cheart duit doiciméadú/cumarsáid a dhéanamh? Áiríonn Arc42 taifid chinntí ailtireachta móide treoir ar spriocanna, srianta, comhthéacsanna, cáilíocht, rioscaí, agus níos mó.

Is cur chuige éasca le foghlaim, cairdiúil d'fhorbróirí é [Samhail C4](https://c4model.com/) chun léaráidí ailtireachta bogearraí a dhéanamh. Is tacar léaráidí ordlathacha é C4 do chomhthéacs, coimeádáin, comhpháirteanna, cód, móide léaráidí tacaíochta do thírdhreach córas, dinimic, agus imlonnú.

## Léaráidí ailtireachta & radhairc & dearcthaí

Tugtar “radharc ailtireachta” ar léaráid ailtireachta.

Is sampla de “dearcadh ailtireachta” é “radharc ailtireachta”.

Tá lucht féachana sonrach ag “dearcadh ailtireachta” le hábhair imní shonracha.

Samplaí de dhearcthaí ailtireachta, samplaí radhairc, agus samplaí léaráidí:

- Cumais Ghnó

- Próisis Ghnó Ardleibhéil

- [Sruthanna Luacha (Value Streams)](https://en.wikipedia.org/wiki/Value_stream)

- Feidhmeanna Bogearraí mapáilte ar chomhpháirteanna feidhmchláir

- Léaráid Chomhthéacs [Samhail C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- Léaráid Coimeádán [Samhail C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- [Léaráid Eintitis-Caidrimh (Entity-relationship Diagram)](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) chun eintitis sonraí a mhapáil ar chomhpháirteanna feidhmchláir

- [Léaráidí Seicheamh (Sequence Diagrams)](https://en.wikipedia.org/wiki/Sequence_diagram) chun sreafaí feidhmiúla laistigh de chórais agus le haghaidh comhtháthaithe a chur síos

- Léaráidí [Samhail agus Nodaireacht Próisis Ghnó (Business Process Model and Notation)](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) chun sreafaí sonraí a chur síos ar fud comhpháirteanna feidhmchláir

- Léaráidí [Samhail agus Nodaireacht Próisis Ghnó (Business Process Model and Notation)](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) chun próisis ghnó / cásanna úsáideora a chur síos

- Léaráidí [Bainistíocht Céannachta agus Rochtana (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM)

- Léaráidí [Rialú Rochtana Bunaithe ar Róil (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) le róil in aghaidh na comhpháirte feidhmchláir

- Léaráidí [Rialú Rochtana Bunaithe ar Thréithe (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) le tréithe in aghaidh na comhpháirte feidhmchláir

- Léaráidí príobháideachta

Léaráidí gaolmhara:

- Taispeánann Léaráid Cás Úsáide cásanna úsáide don bhainistíocht/do chustaiméirí, a thagann roimh riachtanais, a thagann roimh an ailtireacht bogearraí.

- Taispeánann Léaráid Imlonnaithe na crua-earraí/ríomhairí fisiciúla ar a n-imlonnaítear na comhpháirteanna bogearraí.
- Taispeánann Léaráid Sreabhadh Sonraí conas a ghluaiseann sonraí tríd an gcóras agus a aistrítear iad.
- Úsáidtear Léaráid Seicheamh chun a thaispeáint conas a oibríonn prótacail amhail HTTP ar ais ama.

- Léiríonn Léaráid Gníomhaíochta an sreabhadh oibre de ghníomhaíochtaí a ghlacann córas bogearraí, cosúil le NPC AI.

## Feidhmeanna oiriúnachta do chinntí mar chód

Seiceálacha uathoibrithe oibiachtúla is ea feidhmeanna oiriúnachta (fitness functions), scríofa le cód ríomhchlárúcháin, a fhíoraíonn go bhfuil cinntí á gcothabháil.

- Déanann feidhmeanna oiriúnachta cinntí inchoimeádta ó thaobh tástála agus cinnteachta de.

- Is féidir le feidhmeanna oiriúnachta do chinntí cabhrú go mór le cinnteacht cáilíochta, próisis rialála, agus spriocanna rialachais.

### Conas a bhaineann feidhmeanna oiriúnachta le cinntí

Doiciméadaíonn taifead cinnidh an cinneadh, agus cinntíonn feidhm oiriúnachta an cinneadh.

- Sampla cinnidh: Úsáidimid foinsiú teagmhas (event sourcing) do riachtanais iniúchta.

- Sampla feidhme oiriúnachta: Úsáidimid an freastalaí lánpháirtithe leanúnaigh chun a thástáil go gcaithfidh gach athrú staide teagmhais a tháirgeadh.

### Cén fáth a gcabhraíonn feidhmeanna oiriúnachta le cinntí

Tomhais oibiachtúla: Éiríonn nó teipeann ar fheidhmeanna oiriúnachta, mar sin tá an obair le feiceáil agus soiléir.

Úsáid leanúnach: Is iad feidhmeanna oiriúnachta do rialacha beo, a rithtear ar gach tiomantas (commit) agus tógáil.

Muinín chun athfhachtóiriú a dhéanamh: Gabhann feidhmeanna oiriúnachta earráidí rialacha cinnidh go huathoibríoch.

Rialachas inscálaithe: Cinntíonn feidhmeanna oiriúnachta caighdeáin gan constaicí a chruthú.

### An féidir le feidhmeanna oiriúnachta AI a úsáid?

Is féidir le feidhmeanna oiriúnachta samhlacha móra teanga (LLM) AI a úsáid do chinntí trí cheisteanna a chur faoi do chuid oibre,
amhail do phleananna, do chód, do scéimeanna, do APInna, agus níos mó:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Tástáil aonaid ailtireachta

[ArchUnit](https://www.archunit.org/): seiceáil rialacha ailtireachta cód Java trí aon chreat tástála aonaid Java simplí a úsáid.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): seiceáil rialacha ailtireachta cód TypeScript agus cód JavaScript trí Jest, Vitest, Jasmine, srl. a úsáid.

## Cosaintí cinntí d'iarratais tharraingthe

Tugann [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
na taifid chinntí cearta chun solais go huathoibríoch ag an nóiméad ceart — nuair a
bhíonn forbróir ag athrú gníomhach an chóid a chlúdaíonn na cinntí sin. In ionad
a bheith ag súil go léifidh forbróirí fillteán doiciméad sula gcumasc siad, tá an
comhthéacs ábhartha le feiceáil go díreach ar an iarratas tarraingthe (pull request).

Oibríonn sé seo d'aon chineál taifid chinnidh: cinntí ailtireachta, cinntí sonraí,
cinntí comhlíonta, cinntí cliniciúla agus míochaine, cinntí slándála, agus níos mó.

Oibríonn sé le haon chóras CI (GitLab, Jenkins, CircleCI) agus mar chrúca réamh-thiomanta
(pre-commit hook). Foinse oscailte. Ceadúnas MIT.

Is Gníomh GitHub é [ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates)
a theipeann ar iarratas tarraingthe nuair a athraíonn cosáin chóid faoi bhreathnóireacht
gan taifead cinnidh ailtireachta a chur leis nó a nuashonrú. Tá díolúintí sainráite: ligeann
líne `ADR-Exempt:` le cúis don gheata trí agus scríobhtar isteach in achoimre an phoist í.
Neodrach ó theimpléad, gan spleáchais. Foinse oscailte. Ceadúnas MIT.

## Tuilleadh eolais

Réamhrá:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Teimpléid:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Go domhain:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - ceacht míosúil saor in aisce ar ailtireacht bogearraí

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Uirlisí:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Treoir Shonrach do Chuideachtaí:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Samplaí:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Físeáin:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podchraoltaí:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Leabhair:

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

Féach freisin:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Formáid YAML/JSON neodrach ó dhíoltóirí, inléite ag meaisín chun cinntí a léiriú le réasúnaíocht shainráite, toimhdí, staid chognaíoch, agus cothromaíochtaí. Comhlánaíonn sé ADR trí réasúnaíocht struchtúrtha, inbhailíochta a chur le doiciméadú cinntí.
