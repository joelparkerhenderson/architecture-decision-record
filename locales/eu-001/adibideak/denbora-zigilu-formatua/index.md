# Denbora-zigilu formatua

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

Gauzak noiz gertatzen diren jarraitzeko gai izan nahi dugu denbora-zigiluak erabiliz eta gure sistema guztietan eta hirugarrenen sistemetan ondo funtzionatzen duen denbora-zigilu formatu koherentea erabiliz.

Denbora-zigilu formatu desberdinak dituzten sistemekin elkarreragiten dugu:

* JSON mezuek ez dute jatorrizko denbora-zigilu formaturik, beraz aukeratu behar dugu denbora-zigilu bat kate bihurtzeko modua, eta kate bat denbora-zigilu bihurtzekoa, hau da, nola serializatu/deserializatu.

* Aplikazio batzuk tokiko ordua erabiltzeko ezarrita daude, UTC ordua erabili beharrean. Hori erosoa izan daiteke tokiko ordura egokitu behar duten proiektuetarako, hala nola tokiko orduan oinarritutako gertaerak abiarazten dituzten proiektuak.

* Sistema batzuek denbora-zehaztasun behar eta gaitasun desberdinak dituzte, hala nola segundoen vs. milisegundoen vs. nanosegundoen denbora-bereizmena erabiltzea. Adibidez, Linux sistema eragilearen `date` komandoak segundoen denbora-zehaztasun lehenetsia erabiltzen du, Nasdaq burtsak, berriz, nanosegundoen denbora-zehaztasun lehenetsia nahi du.


### Erabakia

ISO 8601 denbora-zigilu formatu estandarra aukeratzen dugu nanosegundoko zehaztasunarekin, zehazki "YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ".

Formatuak urtea, hilabetea, eguna, ordua, minutua, segundoa, nanosegundoak eta Zulu ordu-eremua, hau da, UTC, GMT, erakusten ditu.


### Egoera

Erabakia.


## Xehetasunak


### Hipotesiak

Denbora-zigilu testu-kate hauek kudeatu behar ditugu, denbora-zigilu batetik kate batera bihurtzeko (serializatu) eta kate batetik denbora-zigilu batera bihurtzeko (deserializatu).

Orokorrean erabiltzeko erraza, bihurtzeko erraza eta pertsona batek irakurtzeko erraza den formatu bat nahi dugu.

Kontrolatu ezin ditugun kanpoko sistemen sorta zabalarekin bateragarritasuna nahi dugu, hala nola analitika-sistemak, datu-base sistemak, finantza-sistemak.


### Murriztapenak

Sistema batzuek denbora-zehaztasun mugak dituzte. Adibidez, macOS sistema eragilearen `date` komandoak denbora-zehaztasuna segundotan inprima dezake, baina ez nanosegundotan.


### Jarrerak

Hainbat aukera aztertu ditugu:

* Unix epoch, hau da, zenbaki hazkor bakarra.

* Testu-formatu laburra "YYYYMMDDTHHMMSSNNNNNNNNN".

* Tokiko ordu-eremua vs. UTC ordu-eremua erabiltzea.


### Arrazoibidea

Erabilera tipikorako, pertsonek irakurtzeko/idazteko erraza dena baloratzen dugu, abiadura/tamaina gordina baino gehiago.

Erabilera tipikorako, makina-sistemetan ondo funtzionatzen duen eta eskuz ere ondo funtzionatzen duen formatu bat nahi dugu, hala nola lagin-datuak idaztea, JSON irteera irakurtzea, log-fitxategi bat grep egitea, eta abar.

Erabilera ez-tipikorako, hala nola errendimendu handiko konputazioa, espero dugu aukeratzen dugun edozein testu-formatu optimizatu nahiko dugula testua formatu azkarrago batera bihurtuz, hala nola programazio-lengoaia baten barne-data objektu motara. Beraz testu-formatuak ez du asko inporta HPC-rako.


### Ondorioak

Gure testu-sistemak eta ordu-sistemak formatu honetara konbergituko dute.


## Erlazionatuta


### Erlazionatutako erabakiak

Baliteke denbora-delta, hau da, iraupenak, jarraitzeko modu azkar/erraza ere nahi izatea. Hauek errazak dira Unix epoch denbora-zigiluekin.


### Erlazionatutako eskakizunak

Baliteke gure erabakia egokitu nahi izatea adib. log-mezu zigilu mota jakin baterako eskakizun lotua badugu, hala nola Splunk, Sumo, ELK eta abarrentzat.


### Erlazionatutako artefaktuak

Lengoaia formateatzaileak eta parseatzaileak:

  * [date-fns: JavaScript data-utilitate liburutegi modernoa](https://date-fns.org/)
  * [Crono: Rust-erako data eta ordu liburutegia](https://github.com/chronotope/chron)
  
Rosetta Code adibideak:

  * [Sistemaren ordua](https://www.rosettacode.org/wiki/System_time)
  * [Data formatua](https://www.rosettacode.org/wiki/Date_format)
  * [Erakutsi epoch-a](https://www.rosettacode.org/wiki/Show_the_epoch)

SixArm adibideak:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Erlazionatutako printzipioak

Erraz atzera egin daitekeena. Nahiko erraz alda dezakegu beste formatu batera, hala nola Unix epoch-era.

Atzeratu behar baino lehenagoko optimizazioa. Erabilera tipikorako ez zaigu asko axola karaktere gehigarri gutxi batzuk, hala nola gidoiak eta bi puntuak erabiltzen dituen formatua.


## Oharrak

Gehitu oharrak hemen.
