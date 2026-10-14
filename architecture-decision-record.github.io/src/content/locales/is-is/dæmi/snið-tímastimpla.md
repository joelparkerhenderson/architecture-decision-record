# Snið tímastimpla

Efnisyfirlit:

* [Samantekt](#samantekt)
  * [Vandamál](#vandamál)
  * [Ákvörðun](#ákvörðun)
  * [Staða](#staða)
* [Nánar](#nánar)
  * [Forsendur](#forsendur)
  * [Takmarkanir](#takmarkanir)
  * [Afstöður](#afstöður)
  * [Röksemd](#röksemd)
  * [Afleiðingar](#afleiðingar)
* [Tengt](#tengt)
  * [Tengdar ákvarðanir](#tengdar-ákvarðanir)
  * [Tengdar kröfur](#tengdar-kröfur)
  * [Tengdar afurðir](#tengdar-afurðir)
  * [Tengdar meginreglur](#tengdar-meginreglur)
* [Athugasemdir](#athugasemdir)


## Samantekt


### Vandamál

Við viljum geta fylgst með hvenær hlutir gerast með því að nota tímastimpla og samræmt snið tímastimpla sem virkar vel í öllum kerfum okkar og kerfum þriðju aðila.

Við eigum í samskiptum við kerfi með ólík snið tímastimpla:

* JSON-skilaboð hafa ekki innbyggt snið tímastimpla, svo við þurfum að velja hvernig á að umbreyta tímastimpli í streng og streng í tímastimpil, þ.e. hvernig á að raðgera/afraðgera.

* Sum forrit eru stillt á staðartíma frekar en UTC-tíma. Þetta getur verið þægilegt fyrir verkefni sem þurfa að laga sig að staðartíma, svo sem verkefni sem kveikja atburði sem byggja á staðartíma.

* Sum kerfi hafa ólíkar þarfir og getu varðandi nákvæmni tíma, svo sem að nota tímaupplausn í sekúndum, millisekúndum eða nanósekúndum. Til dæmis notar Linux-stýrikerfisskipunin `date` sjálfgefna tímanákvæmni í sekúndum, en kauphöllin Nasdaq vill sjálfgefna tímanákvæmni í nanósekúndum.


### Ákvörðun

Við veljum staðlaða sniðið ISO 8601 tímastimpils með nanósekúndunákvæmni, nánar tiltekið „YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ“.

Sniðið sýnir ár, mánuð, dag, klukkustund, mínútu, sekúndu, nanósekúndur og Zulu-tímabeltið, öðru nafni UTC, GMT.


### Staða

Ákveðið.


## Nánar


### Forsendur

Við þurfum að meðhöndla þessa tímastimpilstexta, til að umbreyta úr tímastimpli í streng (öðru nafni raðgera) og úr streng í tímastimpil (öðru nafni afraðgera).

Við viljum snið sem er almennt auðvelt í notkun, auðvelt að umbreyta og auðvelt fyrir manneskju að lesa.

Við viljum samhæfni við fjölbreytt úrval ytri kerfa sem við getum ekki stjórnað, svo sem greiningarkerfi, gagnagrunnskerfi og fjármálakerfi.


### Takmarkanir

Sum kerfi hafa takmarkanir á tímanákvæmni. Til dæmis getur macOS-stýrikerfisskipunin `date` prentað tímanákvæmni í sekúndum en ekki í nanósekúndum.


### Afstöður

Við skoðuðum úrval valkosta:

* Unix-tímabil (epoch), þ.e. ein hækkandi tala.

* Stutt textasnið „YYYYMMDDTHHMMSSNNNNNNNNN“.

* Að nota staðartímabelti á móti UTC-tímabelti.


### Röksemd

Fyrir dæmigerða notkun metum við auðvelt að lesa/skrifa fyrir menn meira en hráan hraða/stærð.

Fyrir dæmigerða notkun viljum við snið sem virkar vel í vélakerfum og virkar einnig vel handvirkt, svo sem við að skrifa sýnigögn, lesa JSON-úttak, leita með grep í logskrá o.s.frv.

Fyrir óhefðbundna notkun, svo sem afkastamikla tölvuvinnslu, væntum við þess að við viljum fínstilla hvaða textasnið sem við veljum með því að umbreyta textanum í hraðara snið, svo sem innbyggða dagsetningarhlutagerð forritunarmáls. Textasniðið skiptir því litlu máli fyrir HPC.


### Afleiðingar

Ýmis textakerfi okkar og tímakerfi munu renna saman á þetta snið.


## Tengt


### Tengdar ákvarðanir

Við gætum viljað hraða/auðvelda leið til að rekja einnig tímamismun, öðru nafni tímalengdir. Þær eru auðveldar með Unix-tímastimplum.


### Tengdar kröfur

Við gætum viljað aðlaga ákvörðun okkar t.d. ef við höfum tengda kröfu um tiltekna tegund stimpils á skráningarskilaboðum, svo sem fyrir Splunk, Sumo, ELK o.s.frv.


### Tengdar afurðir

Sniðmótarar og þáttarar fyrir forritunarmál:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Dæmi af Rosetta Code:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Dæmi frá SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Tengdar meginreglur

Auðafturkræft. Við getum breytt nokkuð auðveldlega í annað snið, svo sem Unix-tímabil.

Fresta ótímabærri fínstillingu. Fyrir dæmigerða notkun skiptir okkur litlu máli um örfáa aukastafi eins og snið sem notar bandstrik og tvípunkta.


## Athugasemdir

Bættu við athugasemdum hér.
