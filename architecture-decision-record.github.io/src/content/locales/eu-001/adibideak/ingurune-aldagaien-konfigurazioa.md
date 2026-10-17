# Ingurune-aldagaien konfigurazioa

Edukia:

* [Laburpena](#laburpena)
  * [Arazoa](#arazoa)
  * [Erabakia](#erabakia)
  * [Egoera](#egoera)
* [Xehetasunak](#xehetasunak)
  * [Hipotesiak](#hipotesiak)
  * [Murriztapenak](#murriztapenak)
  * [Jarrerak](#jarrerak)
  * [Arrazoibidea](#arrazoibidea)
  * [Ondorioak](#ondorioak)
* [Erlazionatuta](#erlazionatuta)
  * [Erlazionatutako erabakiak](#erlazionatutako-erabakiak)
  * [Erlazionatutako eskakizunak](#erlazionatutako-eskakizunak)
  * [Erlazionatutako artefaktuak](#erlazionatutako-artefaktuak)
  * [Erlazionatutako printzipioak](#erlazionatutako-printzipioak)
* [Oharrak](#oharrak)


## Laburpena


### Arazoa

Gure aplikazioak artefaktu/bitar/iturburutik harago konfiguragarriak izatea nahi dugu, build bakar batek bere hedapen-inguruneraren arabera portaera desberdina izan dezan.

  * Hori lortzeko, ingurune-aldagaien konfigurazioa erabili nahi dugu.

  * Konfigurazioa bertsio-kontrolatu ditzakegun fitxategien bidez kudeatu nahi dugu.

  * Garatzailearen esperientziaren ergonomia batzuk eskaini nahi ditugu, hala nola zer konfiguratu daitekeen eta lotutako lehenetsiak ezagutzea.


### Erabakia

.env fitxategiak aukeratu dira, lotutako fitxategi lehenetsi eta eskema-fitxategiarekin.


### Egoera

Erabakia. Gaitasun berriak sortzen diren heinean horiek aztertzeko irekia.


## Xehetasunak


### Hipotesiak

Aplikazioaren kodea eta ingurunearen kodea bereiztearen alde gaude. Aplikazioak ingurune desberdinetan era desberdinean funtzionatu behar duela suposatzen dugu, hala nola garapen-ingurunean, proba-ingurunean, demo-ingurunean, produkzio-ingurunean eta abar.

"12 factor app" industria-praktikaren alde gaude, eta are gehiago lotutako "15 factor app" praktikaren alde.

Gure aurreko proiektu askok `.env` fitxategiaren edo antzeko `.env` direktorioaren konbentzioa erabili dute. Horiek bertsio-kontroletik kanpo mantentzea ohiko praktika da, eta horiek hedatu, bertsionatu eta kudeatzeko beste modu bat erabiltzea.


### Murriztapenak

Sekretuak gure iturburu-kodearen kudeaketako (SCM) bertsio-kontroleko sistematik (VCS) kanpo mantendu nahi ditugu.

Software-esparru eta liburutegi ezagunekiko bateragarritasuna bilatu nahi dugu. Adibidez, Node-k "dotenv" modulua du ingurune-aldagaien konfigurazioa irakurtzeko.


### Jarrerak

Hainbat ikuspegi aztertu ditugu:

  * Konfigurazioa aplikazioan gordetzea, adib. `config.js` fitxategi batean.

  * Konfigurazioa ingurunean gordetzea, adib. `.env` fitxategi batean.

  * Konfigurazioa kokapen ezagun batetik eskuratzea, adib. lizentzia-zerbitzari batetik.


### Arrazoibidea

.env fitxategiaren ikuspegia aukeratu dugu zeren:

  * Ezaguna da, adituen artean barne.

  * Gure taldeek proiektu askotan aldi askotan arrakastaz erabili dituzten `.env` fitxategien eredua jarraitzen du.

  * Sinplea da. Bereziki, une honetan ados gaude ikusten ditugun konpentsazio handiekin, hala nola lizentzia-zerbitzariaren ikuspegiarekin alderatuta ikuskaritza-gaitasunik eza.


### Ondorioak 

Sekretuen kudeaketatik publikoa den ingurune-aldagaien konfigurazioa bereizteko modu bat asmatu behar dugu.


## Erlazionatuta


### Erlazionatutako erabakiak

Gure aplikazio guztiek ikuspegi hau erabiliko dutela espero dugu.

Ikuspegi gaitasun txikiagokoa erabiltzen duten gure aplikazioak, hala nola bitar edo iturburu-kodean hardkodetuak, eguneratzea planifikatuko dugu.

Ikuspegi gaitasun handiagokoa erabiltzen duten gure aplikazioak, hala nola lizentzia-zerbitzari bat, dauden bezala mantenduko ditugu.


### Erlazionatutako eskakizunak

Fitxategientzako devops gaitasunak gehituko ditugu, hook-ak, probak eta etengabeko integrazioa barne.

Garatzaile-kide guztiak erabaki honetan prestatu behar ditugu.



### Erlazionatutako artefaktuak

Hedatzen dugun eremu bakoitzak bere .env fitxategia eta lotutako fitxategiak beharko ditu.


### Erlazionatutako printzipioak

Erraz atzera egin daitekeena.


## Oharrak


`.env` fitxategiaren adibidea:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

`.env.defaults` fitxategiaren adibidea:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Gakoak bakarrik dituen `.env.schema` fitxategiaren adibidea:

```env
NAME
EMAIL
```
