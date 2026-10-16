# Taifead Cinnidh Ailtireachta: creat CSS

Ábhar:

- [Achoimre](#achoimre)
  - [Saincheist](#saincheist)
  - [Cinneadh](#cinneadh)
  - [Stádas](#stádas)
- [Sonraí](#sonraí)
  - [Toimhdeanna](#toimhdeanna)
  - [Srianta](#srianta)
  - [Seasaimh](#seasaimh)
  - [Argóint](#argóint)
  - [Impleachtaí](#impleachtaí)
- [Gaolmhar](#gaolmhar)
  - [Cinntí gaolmhara](#cinntí-gaolmhara)
  - [Riachtanais ghaolmhara](#riachtanais-ghaolmhara)
  - [Déantáin ghaolmhara](#déantáin-ghaolmhara)
  - [Prionsabail ghaolmhara](#prionsabail-ghaolmhara)
- [Nótaí](#nótaí)


## Achoimre


### Saincheist

Ba mhaith linn creat CSS a úsáid chun ár bhfeidhmchláir ghréasáin a chruthú:

  * Ba mhaith linn go mbeadh an taithí úsáideora tapa agus iontaofa, ar gach brabhsálaí agus méid scáileáin coitianta.

  * Ba mhaith linn atriall tapa ar dhearadh, leagan amach, UI/UX, srl.

  * Ba mhaith linn feidhmchláir fhreagrúla, go háirithe do scáileáin níos lú amhail ar ghléasanna gluaiste, scáileáin níos mó amhail ar leathscáileáin 4K, agus scáileáin dinimiciúla amhail taispeántais inrothlaithe.  


### Cinneadh

Socraíodh ar Bulma.


### Stádas

Socraíodh ar Bulma. Oscailte do roghanna nua creata CSS de réir mar a thagann siad.


## Sonraí


### Toimhdeanna

Ba mhaith linn feidhmchláir ghréasáin a chruthú atá nua-aimseartha, tapa, iontaofa, freagrúil, srl.

Tá feidhmchláir ghréasáin nua-aimseartha tipiciúla ag laghdú/ag cur deireadh le húsáid jQuery ar chúiseanna iomadúla: 

  * Tá JavaScript nua-aimseartha ag tabhairt isteach go céimiúil go leor cumas a sholáthair jQuery, mar sin tá níos lú gá le jQuery, agus tá modúil níos fearr/níos tapúla/níos lú ann a sholáthraíonn cur chun feidhme sonracha

  * Is é cur chuige leathan jQuery ná ionramháil dhíreach DOM a dhéanamh, rud atá ina frithphatrún do chreataí JavaScript nua-aimseartha (m.sh. React, Vue, Svelte)

  * Cuireann jQuery isteach air féin má luchtaítear faoi dhó é, srl.


### Srianta

Má roghnaímid creat CSS a úsáideann jQuery, tá orainn jQuery a iompórtáil. Mar shampla, úsáideann Semantic UI jQuery, agus ní úsáideann Tachyons.

Má roghnaímid creat CSS atá íosta, déanaimid dínit ar chomhpháirteanna creata a d'fhéadfadh a bheith uainn anois nó go luath. Mar shampla, soláthraíonn Semantic UI carasal íomhánna, agus ní sholáthraíonn Tachyons.


### Seasaimh

Bhreithnigh muid gan aon chreat a úsáid. Is cosúil go bhfuil sé seo inmharthana fós, go háirithe toisc go soláthraíonn CSS grid cuid mhór den mhéid atá uainn dár dtionscadal..

Bhreithnigh muid go leor creataí CSS ag baint úsáide as triaráil tapa ar ghearrliosta: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons, srl. Is iad ár ndá rogha le haghaidh athbhreithnithe níos doimhne ná Semantic UI (toisc go bhfuil an cur chuige is séimeantaí aige) agus Bulma (toisc go bhfuil an cur chuige is éadroime aige a sholáthraíonn na comhpháirteanna atá uainn anois).

Bhreithnigh muid Semantic UI. Soláthraíonn sé seo go leor comhpháirteanna, lena n-áirítear cinn atá uainn dár dtionscadal: cluaisíní, greillí, cnaipí, srl. Rinne muid píolótú le Semantic UI ar dhá bhealach: ag baint úsáide as comhaid CDN tipiciúla, agus ag baint úsáide as taisclanna NPM. D'éirigh linn le Semantic UI i leathanach HTML statach, ach níor éirigh linn laistigh dár bhfuinneog ama SPA JavaScript a thógáil (go príomha mar gheall ar shaincheisteanna luchtaithe jQuery). Fuair muid amach go bhfuil códóirí eile ag iarraidh ar fhorbróirí Semantic UI leagan saor ó jQuery a chruthú, ar na cúiseanna céanna atá againne. Tá códóirí eile ag iarraidh leagan saor ó jQuery le blianta fada, ach dúirt na forbróirí níl, agus luaigh siad go mbeadh aon leagan saor ó jQuery rófhuascailte a scríobh m.sh. ~“tá níos mó ná 22,000 pointe teagmhála ag tionscadal Semantic UI a úsáideann jQuery”.

Sampla le Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Bhreithnigh muid Bulma. Tá go leor cumas cosúil le Semantic UI ag Bulma, cé nach bhfuil an oiread sin comhpháirteanna sofaisticiúla aige. Tá Bulma tógtha le teicnící nua-aimseartha, amhail gan jQuery. Tá roinnt comhpháirteanna tríú páirtí ag Bulma, agus b'fhéidir gur mhaith linn cuid acu a úsáid.


Sampla le Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argóint

Mar atá thuas.

Go sonrach, is cosúil go bhfuil bratach rabhaidh ag Semantic UI ó thaobh teicneolaíochta de (i.e. an oiread sin pointí teagmhála jQuery) agus ó thaobh ceannaireachta de (i.e. ba dhiúltú crua é saor ó jQuery, seachas iarracht a dhéanamh ar mhapa bóthair, nó feabhsú leanúnach, nó tiomsú airgid trí bhronntanais, srl.).


### Impleachtaí

Má aimsímid creat maith CSS nach n-úsáideann jQuery, is rud úsáideach agus maith é seo go ginearálta.


## Gaolmhar


### Cinntí gaolmhara

D'fhéadfadh tionchar a bheith ag an gcreat CSS a roghnaímid ar inthástálacht.


### Riachtanais ghaolmhara

Ba mhaith linn feidhmchlár nua-aimseartha go hiomlán a sheoladh go tapa. 

Níl muid ag iarraidh am a chaitheamh ag obair ar chreataí níos sine (go háirithe Semantic UI) ag baint úsáide as spleáchais níos sine (go háirithe jQuery).


### Déantáin ghaolmhara

Téann sé i bhfeidhm ar an HTML tipiciúil go léir a úsáidfidh an CSS.


### Prionsabail ghaolmhara

Inaisiompaithe go héasca.

Gá le luas.


## Nótaí

Aon nótaí anseo.
