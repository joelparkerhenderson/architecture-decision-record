# Monorepo nó multirepo

Ábhar:

* [Achoimre](#achoimre)
  * [Saincheist](#saincheist)
  * [Cinneadh](#cinneadh)
  * [Stádas](#stádas)
* [Sonraí](#sonraí)
  * [Toimhdeanna](#toimhdeanna)
  * [Srianta](#srianta)
  * [Seasaimh](#seasaimh)
  * [Argóint](#argóint)
  * [Impleachtaí](#impleachtaí)
* [Gaolmhar](#gaolmhar)
  * [Cinntí gaolmhara](#cinntí-gaolmhara)
  * [Riachtanais ghaolmhara](#riachtanais-ghaolmhara)
  * [Déantáin ghaolmhara](#déantáin-ghaolmhara)
  * [Prionsabail ghaolmhara](#prionsabail-ghaolmhara)
* [Nótaí](#nótaí)


## Achoimre


### Saincheist

Tá forbairt trí phríomhchatagóir bogearraí i gceist lenár dtionscadal:

  * GUInna taobh tosaigh
  * Seirbhísí meánbhogearraí
  * Freastalaithe taobh cúil

Nuair a dhéanaimid forbairt, is é git ár gcóras rialaithe leaganacha (VCS) bainistíochta foinse-chóid (SCM).

Ní mór dúinn a roghnú conas git a úsáid chun ár gcód a eagrú.

Is é an rogha barrleibhéil eagrú mar “monorepo” nó “polyrepo” nó “hibrid”:

  * Ciallaíonn monorepo go gcuirimid na codanna go léir i dtaisclann mhór amháin
  * Ciallaíonn polyrepo go gcuirimid gach cuid ina taisclann féin
  * Ciallaíonn hibrid meascán éigin de monorepo agus polyrepo

Le haghaidh tuilleadh féach https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Cinneadh

Monorepo nuair atá eagraíocht/foireann/tionscadal measartha beag, agus atá atriall tapa ina thosaíocht níos airde ná cobhsaíocht a chothabháil.

Polyrepo nuair atá eagraíocht/foireann/tionscadal measartha mór, agus atá cobhsaíocht a chothabháil ina thosaíocht níos airde ná atriall tapa.


### Stádas

Socraithe. Oscailte d'athbhreithniú dá mbeidh uirlisí nua ar fáil chun monorepos agus/nó polyrepos a bhainistiú.


## Sonraí


### Toimhdeanna

Tá an cód go léir atá á fhorbairt againn le haghaidh tairiscintí eagraíochta amháin, agus ní don phobal i gcoitinne. I.e. níl sé mar aidhm ag an Bróicéir-Déileálaí aon rud cosúil le forbróirí deonacha ón bpobal i gcoitinne a bheith aige.


### Srianta

Tá srianta doiciméadaithe go maith ag https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Seasaimh

Bhreithnigh muid monorepos i stíl Google, Facebook, srl. Síleann muid go bhfuil aon saincheisteanna scálaithe monorepo chomh fada sa todhchaí go mbeimid in ann leas a bhaint as na cleachtais chéanna le Google agus Facebook, faoin am a mbeidh siad ag teastáil uainn.

Bhreithnigh muid polyrepos i stíl tionscadal foinse oscailte tipiciúla Git, amhail Google Android, Facebook React, srl. Síleann muid gurb iad seo an rogha is fearr do rannpháirtíocht an phobail i gcoitinne (m.sh. is féidir le duine ar bith ar domhan oibriú ar an gcód) agus infhaighteacht aonair (m.sh. úsáidtear an tionscadal ar a shon féin, gan aon phíosaí eile).


### Argóint

Nuair atá eagraíocht/foireann/tionscadal measartha beag, roghnaímid monorepo, toisc go bhfuil atriall tapa i bhfad níos tábhachtaí ná cobhsaíocht a chothabháil

Nuair atá eagraíocht/foireann/tionscadal measartha mór, roghnaímid polyrepo, toisc go bhfuil cobhsaíocht a chothabháil i bhfad níos tábhachtaí ná atriall tapa.


### Impleachtaí

Má tá píblíne ann cheana do CI+CD, b'fhéidir go mbeidh orainn é a choigeartú chun tionscadail iomadúla laistigh de thaisclann amháin a thástáil.

D'fhéadfadh CI+CD níos mó ama a thógáil le haghaidh tógála iomláine do monorepo, mar go bhféadfadh CI+CD na tionscadail go léir sa monorepo a thógáil.

Má fhásann eagraíocht/foireann/tionscadal, beidh saincheisteanna scálaithe ag monorepo.

D'fhéadfadh saincheisteanna scálaithe monorepo ardú luacha a chur ar aistriú go polyrepo.

Is tasc devops suntasach é aistriú ó monorepo go polyrepo, agus beidh gá é a phleanáil, a bhainistiú, agus a ríomhchlárú.


## Gaolmhar


### Cinntí gaolmhara

Cruthóimid cinntí d'uirlisí gaolmhara chun monorepos (m.sh. Google Bazel) agus polyrepos (m.sh. Lyft Refactorator) a bhainistiú.


### Riachtanais ghaolmhara

Ní mór dúinn an phíblíne CI+CD a fhorbairt chun oibriú go maith le git.


### Déantáin ghaolmhara

Táimid ag súil go mbeidh déantáin ghaolmhara ag eagrú na taisclainne do sholáthar, bainistiú cumraíochta, tástáil, agus réimsí devops den chineál céanna. 


### Prionsabail ghaolmhara

Inaisiompaithe go héasca. Mura n-oibríonn an monorepo i gcleachtas, nó mura dteastaíonn sé ón gceannaireacht, tá sé simplí athrú go polyrepo.

Seilbh Chustaiméirí. Cuirimid luach ar an tionscadal a chur i lámha custaiméirí, agus creidimid go bhféadfadh monorepo muid a thabhairt ann níos tapúla ná polyrepo, agus cabhrú linn atriall níos tapúla a dhéanamh freisin.

Smaoinigh mór. Tá Google agus Facebook ina n-abhcóidí an-láidre ar monorepos thar polyrepos, toisc gur féidir na príomhthairiscintí go léir a fhorbairt/a thástáil/a imlonnú i gcomhar.


## Nótaí

Cuir aon nótaí anseo.
