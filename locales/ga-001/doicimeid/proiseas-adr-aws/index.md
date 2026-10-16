# Próiseas Taifead Cinntí Ailtireachta AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Is éard is taifead cinnidh ailtireachta (ADR) ann ná doiciméad a dhéanann cur síos ar rogha a dhéanann an fhoireann faoi ghné shuntasach den ailtireacht bogearraí atá beartaithe acu a thógáil. Déanann gach ADR cur síos ar an gcinneadh ailtireachta, a chomhthéacs, agus a iarmhairtí. Tá staideanna ag ADR agus mar sin leanann siad saolré. Chun sampla de ADR a fheiceáil, féach ar an aguisín.

Táirgeann an próiseas ADR bailiúchán de thaifid chinntí ailtireachta. Cruthaíonn an bailiúchán seo an logchomhad cinntí. Soláthraíonn an logchomhad cinntí comhthéacs an tionscadail chomh maith le faisnéis mhionsonraithe cur chun feidhme agus dearaidh. Féachann baill an tionscadail ar chinnirí gach ADR chun forbhreathnú ar chomhthéacs an tionscadail a fháil. Léann siad na ADR chun dul go doimhin isteach i gcur chun feidhme agus roghanna dearaidh an tionscadail.

Nuair a ghlacann an fhoireann ADR, éiríonn sé do-athraithe. Má éilíonn léargais nua cinneadh difriúil, molann an fhoireann ADR nua. Nuair a ghlacann an fhoireann leis an ADR nua, tagann sé in ionad an ADR roimhe sin.

## Scóip an phróisis ADR

Ba cheart do bhaill an tionscadail ADR a chruthú do gach cinneadh suntasach ó thaobh na hailtireachta de a théann i bhfeidhm ar an tionscadal nó ar an táirge bogearraí, lena n-áirítear an méid seo a leanas (Richards agus Ford 2020):

* Struchtúr (mar shampla, patrúin amhail micreaseirbhísí)

* Riachtanais neamhfheidhmiúla (slándáil, ardinfhaighteacht, agus lamháltas lochtanna)

* Spleáchais (cúpláil comhpháirteanna)

* Comhéadain (APInna agus conarthaí foilsithe)

* Teicnící tógála (leabharlanna, creataí, uirlisí, agus próisis)

* Is iad riachtanais fheidhmiúla agus neamhfheidhmiúla na ngnáthionchuir don phróiseas ADR.


## Ábhar ADR

Nuair a aithníonn an fhoireann gá le ADR, tosaíonn ball foirne ag scríobh an ADR bunaithe ar theimpléad tionscadail-leathan. (Féach eagraíocht ADR GitHub le haghaidh teimpléad samplacha.) Simplíonn an teimpléad cruthú ADR agus cinntíonn sé go ngabhann an ADR gach faisnéis ábhartha. Ar a laghad, ba cheart do gach ADR comhthéacs an chinnidh, an cinneadh féin, agus iarmhairtí an chinnidh don tionscadal agus dá thorthaí a shainiú. (Chun samplaí de na hailt seo a fheiceáil, féach an t-aguisín.) Ceann de na gnéithe is cumhachtaí de struchtúr an ADR is ea go ndíríonn sé ar chúis an chinnidh seachas ar an gcaoi ar chuir an fhoireann i bhfeidhm é. Éascaíonn tuiscint ar cén fáth ar ghlac an fhoireann an cinneadh do bhaill foirne eile an cinneadh a ghlacadh, agus coscann sé ailtirí eile nach raibh páirteach sa phróiseas cinnteoireachta ón gcinneadh sin a chur ar neamhní amach anseo.


## Próiseas glactha ADR

Is féidir le gach ball foirne ADR a chruthú, ach ba cheart don fhoireann sainmhíniú úinéireachta a bhunú do ADR. Ba cheart do gach údar atá ina úinéir ar ADR ábhar an ADR a chothabháil agus a chur in iúl go gníomhach. Chun an úinéireacht seo a shoiléiriú, tagraíonn an treoir seo d'údair ADR mar úinéirí ADR sna hailt seo a leanas. Is féidir le baill foirne eile cur le ADR i gcónaí. Má athraíonn ábhar ADR sula nglacann an fhoireann leis an ADR, ba cheart don úinéir na hathruithe seo a fhormheas.

Tar éis don fhoireann cinneadh ailtireachta agus a úinéir a aithint, soláthraíonn úinéir an ADR an ADR sa staid **Molta** (Proposed) ag tús an phróisis. Tá ADR sa staid Molta réidh le haghaidh athbhreithnithe.

Ansin tionscnaíonn úinéir an ADR an próiseas athbhreithnithe don ADR. Is é cuspóir phróiseas athbhreithnithe an ADR cinneadh a dhéanamh an nglacann an fhoireann leis an ADR, an gcinneann sí go bhfuil gá athoibre leis, nó an diúltaíonn sí don ADR. Athbhreithníonn foireann an tionscadail, an t-úinéir san áireamh, an ADR. Ba cheart tús a chur leis an gcruinniú athbhreithnithe le sliotán ama tiomanta chun an ADR a léamh. Ar an meán, ba cheart go mbeadh 10 go 15 nóiméad go leor. Le linn an ama seo, léann gach ball foirne an doiciméad agus cuireann sé tuairimí agus ceisteanna leis chun topaicí neamhshoiléire a bhratú. Tar éis an chéim athbhreithnithe, léann úinéir an ADR amach agus pléann sé gach tuairim leis an bhfoireann.

Má aimsíonn an fhoireann pointí gníomhaíochta chun an ADR a fheabhsú, fanann staid an ADR **Molta**. Cumasaíonn úinéir an ADR na gníomhartha, agus, i gcomhar leis an bhfoireann, cuireann sé sannaí le gach gníomh. Is féidir le gach ball foirne cur leis na pointí gníomhaíochta agus iad a réiteach. Tá sé de fhreagracht ar úinéir an ADR an próiseas athbhreithnithe a athsceidealú.

Is féidir leis an bhfoireann cinneadh a dhéanamh diúltú don ADR freisin. Sa chás seo, cuireann úinéir an ADR cúis an diúltaithe leis chun plé amach anseo ar an ábhar céanna a sheachaint. Athraíonn an t-úinéir staid an ADR go **Diúltaithe** (Rejected).

Má fhormheasann an fhoireann an ADR, cuireann an t-úinéir stampa ama, leagan, agus liosta geallsealbhóirí leis. Ansin nuashonraíonn an t-úinéir an staid go **Glactha** (Accepted).

Léiríonn ADR agus an logchomhad cinntí a chruthaíonn siad cinntí a rinne an fhoireann agus soláthraíonn siad stair na gcinntí uile. Úsáideann an fhoireann na ADR mar thagairt le linn athbhreithnithe cód agus ailtireachta nuair is féidir. Chomh maith le hathbhreithnithe cód, tascanna dearaidh, agus tascanna cur chun feidhme a dhéanamh, ba cheart do bhaill foirne dul i gcomhairle le ADR do chinntí straitéiseacha don táirge.

Mar dhea-chleachtas, ba cheart go rachadh gach athrú bogearraí trí athbhreithnithe piaraí agus go n-éileodh sé formheas amháin ar a laghad. Le linn an athbhreithnithe cód, d'fhéadfadh athbhreithneoir cód athruithe a aimsiú a sháraíonn ADR amháin nó níos mó. Sa chás seo, iarrann an t-athbhreithneoir ar údar an athraithe cód an cód a nuashonrú, agus roinneann sé nasc leis an ADR. Nuair a nuashonraíonn an t-údar an cód, formheasann athbhreithneoirí piaraí é agus cumasctar isteach sa phríomhbhonn cód é.


## Próiseas athbhreithnithe ADR

Ba cheart don fhoireann ADR a láimhseáil mar dhoiciméid do-athraithe tar éis di glacadh leo nó diúltú dóibh. Chun athruithe ar ADR atá ann cheana a dhéanamh, ní mór ADR nua a chruthú, próiseas athbhreithnithe a bhunú don ADR nua, agus an ADR a fhormheas. Má fhormheasann an fhoireann an ADR nua, ba cheart don úinéir staid an tsean-ADR a athrú go **Curtha ina ionad** (Superseded).
