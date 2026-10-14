# Monorepo eða multirepo

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

Verkefni okkar felur í sér þróun þriggja meginflokka hugbúnaðar:

  * Myndræn notendaviðmót á framenda
  * Millilagsþjónustur
  * Þjónar á bakenda

Þegar við þróum er útgáfustýringarkerfi (VCS) frumkóðastjórnunar (SCM) okkar git.

Við þurfum að velja hvernig við notum git til að skipuleggja kóðann okkar.

Æðsta valið er að skipuleggja sem „monorepo“, „polyrepo“ eða „blendingur“:

  * Monorepo þýðir að við setjum alla hluta í eitt stórt safn
  * Polyrepo þýðir að við setjum hvern hluta í sitt eigið safn
  * Blendingur þýðir einhver blanda af monorepo og polyrepo

Fyrir frekari upplýsingar, sjá https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Ákvörðun

Monorepo þegar stofnun/teymi/verkefni er tiltölulega lítið og hröð þróun í áföngum hefur meiri forgang en viðvarandi stöðugleiki.

Polyrepo þegar stofnun/teymi/verkefni er tiltölulega stórt og viðvarandi stöðugleiki hefur meiri forgang en hröð þróun í áföngum.


### Staða

Ákveðið. Opið fyrir endurskoðun ef/þegar ný verkfæri verða tiltæk til að stýra monorepo og/eða polyrepo.


## Nánar


### Forsendur

Allur kóðinn sem við þróum er fyrir framboð einnar stofnunar en ekki fyrir almenning. Þ.e. verðbréfamiðlarinn stefnir ekki að neinu í líkingu við sjálfboðaliða úr röðum almennings sem þróunaraðila.


### Takmarkanir

Takmarkanir eru vel skjalfestar á https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Afstöður

Við skoðuðum monorepo í stíl Google, Facebook o.s.frv. Við teljum að hvers kyns stigstærðarvandamál monorepo séu svo langt inni í framtíðinni að við munum geta nýtt sömu starfsvenjur og Google og Facebook þegar við þurfum á þeim að halda.

Við skoðuðum polyrepo í stíl dæmigerðra opinna Git-verkefna, svo sem Google Android, Facebook React o.s.frv. Við teljum að þetta sé besti kosturinn fyrir þátttöku almennings (t.d. hver sem er í heiminum getur unnið að kóðanum) og sjálfstætt framboð (t.d. verkefnið er notað eitt og sér, án nokkurra annarra hluta).


### Röksemd

Þegar stofnun/teymi/verkefni er tiltölulega lítið veljum við monorepo, því hröð þróun í áföngum hefur verulega meiri forgang en viðvarandi stöðugleiki

Þegar stofnun/teymi/verkefni er tiltölulega stórt veljum við polyrepo, því viðvarandi stöðugleiki hefur verulega meiri forgang en hröð þróun í áföngum.


### Afleiðingar

Ef fyrir er CI+CD-leiðsla gætum við þurft að laga hana til að prófa mörg verkefni innan eins safns.

CI+CD gæti tekið meiri tíma fyrir fulla smíði á monorepo, því CI+CD gæti smíðað öll verkefni í monorepo.

Ef stofnun/teymi/verkefni stækkar mun monorepo lenda í stigstærðarvandamálum.

Stigstærðarvandamál monorepo gætu gert það sífellt verðmætara að færa sig yfir í polyrepo.

Umskipti úr monorepo í polyrepo eru umtalsvert devops-verkefni og þarf að skipuleggja, stýra og forrita.


## Tengt


### Tengdar ákvarðanir

Við munum búa til ákvarðanir um tengd verkfæri til að stýra monorepo (t.d. Google Bazel) og polyrepo (t.d. Lyft Refactorator).


### Tengdar kröfur

Við þurfum að þróa CI+CD-leiðsluna þannig að hún virki vel með git.


### Tengdar afurðir

Við væntum þess að skipulag safnsins hafi tengdar afurðir fyrir útvegun, uppsetningarstýringu, prófanir og áþekk devops-svið.


### Tengdar meginreglur

Auðafturkræft. Ef monorepo virkar ekki í reynd, eða er ekki óskað af forystunni, er einfalt að breyta í polyrepo.

Þráhyggja um viðskiptavininn. Við metum mikils að koma verkefninu í hendur viðskiptavina og við teljum að monorepo geti komið okkur þangað hraðar en polyrepo, og einnig hjálpað okkur að þróa hraðar í áföngum.

Hugsaðu stórt. Google og Facebook eru mjög sterkir talsmenn monorepo fram yfir polyrepo, því hægt er að þróa/prófa/setja upp allar kjarnaafurðir í sameiningu.


## Athugasemdir

Bættu við athugasemdum hér.
