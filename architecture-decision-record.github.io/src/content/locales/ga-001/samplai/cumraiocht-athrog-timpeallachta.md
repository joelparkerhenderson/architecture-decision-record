# Cumraíocht athróg timpeallachta

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
  * [Impleachtaí ](#impleachtaí)
* [Gaolmhar](#gaolmhar)
  * [Cinntí gaolmhara](#cinntí-gaolmhara)
  * [Riachtanais ghaolmhara](#riachtanais-ghaolmhara)
  * [Déantáin ghaolmhara](#déantáin-ghaolmhara)
  * [Prionsabail ghaolmhara](#prionsabail-ghaolmhara)
* [Nótaí](#nótaí)


## Achoimre


### Saincheist

Ba mhaith linn go mbeadh ár bhfeidhmchláir inchumraithe thar déantáin/dénártha/foinse, ionas gur féidir le tógáil amháin iompar go difriúil ag brath ar a timpeallacht imlonnaithe.

  * Chun é seo a bhaint amach, ba mhaith linn cumraíocht athróg timpeallachta a úsáid.

  * Ba mhaith linn an chumraíocht a bhainistiú trí chomhaid a úsáid ar féidir linn rialú leaganacha a chur orthu.

  * Ba mhaith linn roinnt áise d'eispéireas forbróra a sholáthar, amhail a fhios cad is féidir a chumrú agus aon réamhshocruithe ábhartha.


### Cinneadh

Socraíodh ar chomhaid .env le comhad réamhshocruithe gaolmhar agus comhad scéime.


### Stádas

Socraithe. Oscailte do chumais nua a bhreithniú de réir mar a thagann siad chun cinn.


## Sonraí


### Toimhdeanna

Is fearr linn cód an fheidhmchláir agus cód na timpeallachta a scaradh. Glacaimid leis go gcaithfidh an aip oibriú go difriúil i dtimpeallachtaí difriúla, amhail i dtimpeallacht forbartha, timpeallacht tástála, timpeallacht taispeána, timpeallacht táirgthe, srl.

Is fearr linn cleachtas an tionscail “12 factor app” agus níos mó fós an cleachtas gaolmhar “15 factor app”.

Tá an coinbhinsiún comhad `.env` nó eolaire `.env` den chineál céanna úsáidte ag go leor dár dtionscadail roimhe seo. Is cleachtas tipiciúil é iad seo a choinneáil as rialú leaganacha, agus bealach éigin eile a úsáid chun iad a imlonnú, a leaganú, agus a bhainistiú.


### Srianta

Ba mhaith linn rúin a choinneáil as ár gcóras rialaithe leaganacha (VCS) bainistíochta foinse-chóid (SCM).

Ba mhaith linn díriú ar chomhoiriúnacht le creataí agus leabharlanna bogearraí coitianta. Mar shampla, tá modúl “dotenv” ag Node chun cumraíocht athróg timpeallachta a léamh.


### Seasaimh

Bhreithnigh muid cúpla cur chuige:

  * Cumraíocht a stóráil san aip, amhail i gcomhad `config.js`.

  * Cumraíocht a stóráil sa timpeallacht, amhail i gcomhad `.env`.

  * Cumraíocht a fháil ó shuíomh ar eolas, amhail freastalaí ceadúnais.


### Argóint

Roghnaigh muid an cur chuige comhad .env mar:

  * Tá sé coitianta, lena n-áirítear i measc saineolaithe.

  * Leanann sé patrún na gcomhad `.env` a d'úsáid ár bhfoirne go rathúil go minic ar go leor tionscadal.

  * Tá sé simplí. Go háirithe, táimid ceart go leor anois leis na cothromaíochtaí suntasacha a fheicimid, amhail easpa cumas iniúchta i gcomparáid le cur chuige freastalaí ceadúnais.


### Impleachtaí 

Ní mór dúinn bealach a aimsiú chun cumraíocht athróg timpeallachta atá poiblí a scaradh ó bhainistiú rúin ar bith.


## Gaolmhar


### Cinntí gaolmhara

Táimid ag súil go n-úsáidfidh ár bhfeidhmchláir go léir an cur chuige seo.

Beidh muid ag pleanáil aon cheann dár bhfeidhmchláir a úsáideann cur chuige níos lú cumais a uasghrádú, amhail códú crua i ndénártha nó i gcód foinse.

Fágfaimid mar atá aon cheann dár bhfeidhmchláir a úsáideann cur chuige níos cumasaí, amhail freastalaí ceadúnúcháin.


### Riachtanais ghaolmhara

Cuirfimid cumais devops leis na comhaid, lena n-áirítear crúcaí, tástálacha, agus lánpháirtiú leanúnach.

Ní mór dúinn oiliúint a chur ar gach comhghleacaí forbróra faoin gcinneadh seo.



### Déantáin ghaolmhara

Beidh a chomhad .env féin agus comhaid ghaolmhara ag teastáil ó gach limistéar ina n-imlonnaímid.


### Prionsabail ghaolmhara

Inaisiompaithe go héasca.


## Nótaí


Sampla comhad `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Sampla comhad `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Sampla comhad `.env.schema` leis na heochracha amháin:

```env
NAME
EMAIL
```
