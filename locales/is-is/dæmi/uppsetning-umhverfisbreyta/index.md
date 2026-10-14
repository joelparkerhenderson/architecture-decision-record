# Uppsetning umhverfisbreyta

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
  * [Afleiðingar ](#afleiðingar)
* [Tengt](#tengt)
  * [Tengdar ákvarðanir](#tengdar-ákvarðanir)
  * [Tengdar kröfur](#tengdar-kröfur)
  * [Tengdar afurðir](#tengdar-afurðir)
  * [Tengdar meginreglur](#tengdar-meginreglur)
* [Athugasemdir](#athugasemdir)


## Samantekt


### Vandamál

Við viljum að forrit okkar séu stillanleg umfram afurðir/tvíundarskrár/frumkóða, svo ein smíði geti hegðað sér ólíkt eftir því umhverfi sem hún er sett upp í.

  * Til að ná þessu viljum við nota uppsetningu með umhverfisbreytum.

  * Við viljum stýra uppsetningunni með skrám sem við getum útgáfustýrt.

  * Við viljum veita þróunaraðilum þægindi, svo sem að vita hvað er hægt að stilla og hver sjálfgefin gildi eru.


### Ákvörðun

Ákveðið var að nota .env-skrár með tengdri sjálfgefinni skrá og skemaskrá.


### Staða

Ákveðið. Opið fyrir að íhuga nýja getu þegar hún kemur fram.


## Nánar


### Forsendur

Við kjósum að aðgreina forritskóða og umhverfiskóða. Við gerum ráð fyrir að forritið þurfi að virka ólíkt í ólíkum umhverfum, svo sem þróunarumhverfi, prófunarumhverfi, sýnisumhverfi, framleiðsluumhverfi o.s.frv.

Við kjósum starfsvenju greinarinnar „12 factor app“ og enn frekar tengda starfsvenju „15 factor app“.

Mörg fyrri verkefna okkar hafa notað venjuna um `.env`-skrá eða áþekka `.env`-möppu. Dæmigerð starfsvenja er að halda þessum utan útgáfustýringar og nota í staðinn einhverja aðra leið til að setja þær upp, útgáfustýra og stýra.


### Takmarkanir

Við viljum halda leyndarmálum utan útgáfustýringarkerfis (VCS) frumkóðastjórnunar (SCM).

Við viljum stefna að samhæfni við vinsæla hugbúnaðarramma og söfn. Til dæmis hefur Node einingu „dotenv“ til að lesa uppsetningu umhverfisbreyta.


### Afstöður

Við skoðuðum nokkrar nálganir:

  * Geyma uppsetningu í forritinu, svo sem í skránni `config.js`.

  * Geyma uppsetningu í umhverfinu, svo sem í skránni `.env`.

  * Sækja uppsetningu frá þekktum stað, svo sem leyfisþjóni.


### Röksemd

Við völdum nálgunina með skránni .env vegna þess að:

  * Hún er vinsæl, þar á meðal meðal sérfræðinga.

  * Hún fylgir mynstri `.env`-skráa sem teymi okkar hafa notað með góðum árangri oft í mörgum verkefnum.

  * Hún er einföld. Einkum sættum við okkur í bili við þær umtalsverðu málamiðlanir sem við sjáum, svo sem skort á endurskoðunargetu samanborið við nálgun með leyfisþjóni.


### Afleiðingar 

Við þurfum að finna leið til að aðgreina uppsetningu umhverfisbreyta sem er opinber frá hvers kyns leyndarmálastýringu.


## Tengt


### Tengdar ákvarðanir

Við væntum þess að öll forrit okkar noti þessa nálgun.

Við munum áætla að uppfæra öll forrit okkar sem nota minna færa nálgun, svo sem harðkóðun í tvíundarskrá eða frumkóða.

Við munum halda óbreyttum öllum forritum okkar sem nota færari nálgun, svo sem leyfisþjón.


### Tengdar kröfur

Við munum bæta við devops-getu fyrir skrárnar, þar á meðal króka, próf og samfellda samþættingu.

Við þurfum að þjálfa allt þróunarteymi í þessari ákvörðun.



### Tengdar afurðir

Hvert svæði þar sem við setjum upp þarf sína eigin .env-skrá og tengdar skrár.


### Tengdar meginreglur

Auðafturkræft.


## Athugasemdir


Dæmi um skrána `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Dæmi um skrána `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Dæmi um skrána `.env.schema` með aðeins lyklunum:

```env
NAME
EMAIL
```
