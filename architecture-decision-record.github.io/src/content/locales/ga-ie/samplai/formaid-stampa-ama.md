# Formáid stampa ama

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

Ba mhaith linn a bheith in ann rianú a dhéanamh ar cathain a tharlaíonn rudaí trí stampaí ama a úsáid agus trí fhormáid stampa ama chomhsheasmhach a úsáid a oibríonn go maith ar fud ár gcórais uile agus córais tríú páirtí.

Idirghníomhaímid le córais a bhfuil formáidí stampa ama difriúla acu:

* Níl formáid stampa ama dhúchasach ag teachtaireachtaí JSON, mar sin ní mór dúinn a roghnú conas stampa ama a thiontú go teaghrán, agus teaghrán a thiontú go stampa ama, i.e. conas sraitheoireacht/dí-sraitheoireacht a dhéanamh.

* Tá roinnt feidhmchlár socraithe chun am áitiúil a úsáid, seachas am UTC. Féadann sé seo a bheith áisiúil do thionscadail a gcaithfidh siad oiriúnú d'am áitiúil, amhail tionscadail a spreagann teagmhais atá bunaithe ar am áitiúil.

* Tá riachtanais agus cumais chruinnis ama dhifriúla ag roinnt córas, amhail taifeach ama soicindí vs. milleasoicindí vs. nanashoicindí a úsáid. Mar shampla, úsáideann ordú `date` an chórais oibriúcháin Linux cruinneas ama réamhshocraithe soicindí, ach ba mhaith le malartán stoc Nasdaq cruinneas ama réamhshocraithe nanashoicindí.


### Cinneadh

Roghnaímid an fhormáid chaighdeánach stampa ama ISO 8601 le cruinneas nanashoicind, go sonrach “YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ”.

Taispeánann an fhormáid an bhliain, an mhí, an lá, an uair, an nóiméad, an dara, nanashoicindí, agus crios ama Zulu ar a dtugtar UTC, GMT freisin.


### Stádas

Socraithe.


## Sonraí


### Toimhdeanna

Ní mór dúinn na teaghráin téacs stampa ama seo a láimhseáil, chun tiontú ó stampa ama go teaghrán (ar a dtugtar sraitheoireacht freisin) agus tiontú ó theaghrán go stampa ama (ar a dtugtar dí-sraitheoireacht freisin).

Ba mhaith linn formáid atá éasca le húsáid go ginearálta, éasca le tiontú, agus éasca do dhuine a léamh.

Ba mhaith linn comhoiriúnacht le raon leathan córas seachtrach nach féidir linn a rialú, amhail córais anailísíochta, córais bunachar sonraí, córais airgeadais.


### Srianta

Tá teorainneacha cruinnis ama ag roinnt córas. Mar shampla, is féidir le hordú `date` an chórais oibriúcháin macOS cruinneas ama a phriontáil i soicindí, ach ní i nanashoicindí.


### Seasaimh

Bhreithnigh muid raon roghanna:

* Epoch Unix i.e. uimhir amháin ag méadú.

* Formáid téacs gharbh “YYYYMMDDTHHMMSSNNNNNNNNN”.

* Crios ama áitiúil a úsáid vs. crios ama UTC.


### Argóint

Le haghaidh gnáthúsáide, cuirimid luach ar éascaíocht léite/scríofa ag daoine, níos mó ná ar luas/méid amh.

Le haghaidh gnáthúsáide, ba mhaith linn formáid a oibríonn go maith i gcórais mheaisín, agus a oibríonn go maith de láimh freisin, amhail sonraí samplacha a scríobh, aschur JSON a léamh, comhad logála a ghrep, srl.

Le haghaidh úsáide neamhghnách, amhail ríomhaireacht ardfheidhmíochta, táimid ag súil go mbeidh fonn orainn aon fhormáid téacs a roghnaíonn muid a bharrfheabhsú trí thiontú an téacs go formáid níos tapúla, amhail cineál réada dáta ionsuite teanga ríomhchlárúcháin. Mar sin ní tábhachtach an fhormáid téacs do HPC.


### Impleachtaí

Cuirfidh ár gcórais téacs éagsúla agus ár gcórais ama le chéile ar an bhformáid seo.


## Gaolmhar


### Cinntí gaolmhara

B'fhéidir go mbeadh bealach tapa/éasca uainn chun fad ama a rianú freisin. Tá siad seo éasca le stampaí ama epoch Unix.


### Riachtanais ghaolmhara

B'fhéidir gur mhaith linn ár gcinneadh a choigeartú m.sh. má tá riachtanas gaolmhar againn do chineál áirithe stampa teachtaireachta logála, amhail do Splunk, Sumo, ELK, srl.


### Déantáin ghaolmhara

Formáidithe agus parsálaithe teanga:

  * [date-fns: leabharlann uirlisí dáta JavaScript nua-aimseartha](https://date-fns.org/)
  * [Crono: leabharlann dáta agus ama do Rust](https://github.com/chronotope/chron)
  
Samplaí Rosetta Code:

  * [Am córais](https://www.rosettacode.org/wiki/System_time)
  * [Formáid dáta](https://www.rosettacode.org/wiki/Date_format)
  * [Taispeáin an epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Samplaí SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Prionsabail ghaolmhara

Inaisiompaithe go héasca. Is féidir linn athrú go héasca go formáid dhifriúil, amhail epoch Unix.

Cuir siar barrfheabhsú anabaí. Le haghaidh gnáthúsáide is cuma linn faoi cúpla carachtar breise amhail formáid a úsáideann fleiscíní agus idirstadanna.


## Nótaí

Cuir nótaí anseo.
