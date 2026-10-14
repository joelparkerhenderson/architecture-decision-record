# Monorepo au multirepo

Yaliyomo:

* [Muhtasari](#muhtasari)
  * [Suala](#suala)
  * [Uamuzi](#uamuzi)
  * [Hali](#hali)
* [Undani](#undani)
  * [Dhana](#dhana)
  * [Vikwazo](#vikwazo)
  * [Misimamo](#misimamo)
  * [Hoja](#hoja)
  * [Athari](#athari)
* [Yanayohusiana](#yanayohusiana)
  * [Maamuzi yanayohusiana](#maamuzi-yanayohusiana)
  * [Mahitaji yanayohusiana](#mahitaji-yanayohusiana)
  * [Vielelezo vinavyohusiana](#vielelezo-vinavyohusiana)
  * [Kanuni zinazohusiana](#kanuni-zinazohusiana)
* [Maelezo ya ziada](#maelezo-ya-ziada)


## Muhtasari


### Suala

Mradi wetu unahusisha kuunda makundi makuu matatu ya programu:

  * GUI za sehemu ya mbele
  * Huduma za tabaka la kati
  * Seva za sehemu ya nyuma

Tunapounda, mfumo wetu wa udhibiti wa matoleo (VCS) wa usimamizi wa msimbo chanzi (SCM) ni git.

Tunahitaji kuchagua jinsi tutakavyotumia git kupanga msimbo wetu.

Chaguo la ngazi ya juu ni kupanga kama "monorepo" au "polyrepo" au "mseto":

  * Monorepo inamaanisha tunaweka vipande vyote kwenye hifadhi moja kubwa
  * Polyrepo inamaanisha tunaweka kila kipande kwenye hifadhi yake
  * Mseto inamaanisha mchanganyiko fulani wa monorepo na polyrepo

Kwa zaidi tafadhali tazama https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Uamuzi

Monorepo wakati shirika/timu/mradi ni mdogo kiasi, na uundaji wa awamu wa haraka una kipaumbele cha juu kuliko kudumisha uthabiti.

Polyrepo wakati shirika/timu/mradi ni mkubwa kiasi, na kudumisha uthabiti kuna kipaumbele cha juu kuliko uundaji wa awamu wa haraka.


### Hali

Imeamuliwa. Tuko wazi kuupitia upya ikiwa/wakati zana mpya zitakapopatikana za kusimamia monorepo na/au polyrepo.


## Undani


### Dhana

Msimbo wote tunaounda ni kwa bidhaa za shirika moja, na si kwa umma kwa ujumla. Yaani Wakala wa Dalali haulengi kuwa na kitu kama waundaji wa kujitolea wa umma kwa ujumla.


### Vikwazo

Vikwazo vimeandikwa vizuri katika https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Misimamo

Tulizingatia monorepo kwa mtindo wa Google, Facebook, n.k. Tunafikiri matatizo yoyote ya upanuzi wa monorepo yako mbali sana siku zijazo hivi kwamba tutaweza kutumia mazoea yaleyale ya Google na Facebook, wakati tutakapoyahitaji.

Tulizingatia polyrepo kwa mtindo wa miradi ya kawaida ya Git ya chanzo huria, kama Google Android, Facebook React, n.k. Tunafikiri hizi ndizo chaguo bora kwa ushiriki wa umma kwa ujumla (mf. yeyote duniani anaweza kufanya kazi kwenye msimbo) na upatikanaji wa mtu binafsi (mf. mradi unatumika peke yake, bila vipande vingine vyovyote).


### Hoja

Wakati shirika/timu/mradi ni mdogo kiasi, tunachagua monorepo, kwa sababu uundaji wa awamu wa haraka una kipaumbele cha juu zaidi kwa kiasi kikubwa kuliko kudumisha uthabiti

Wakati shirika/timu/mradi ni mkubwa kiasi, tunachagua polyrepo, kwa sababu kudumisha uthabiti kuna kipaumbele cha juu zaidi kwa kiasi kikubwa kuliko uundaji wa awamu wa haraka.


### Athari

Ikiwa kuna mfereji uliopo wa CI+CD, basi tunaweza kuhitaji kuurekebisha ili kujaribu miradi mingi ndani ya hifadhi moja.

CI+CD inaweza kuchukua muda zaidi kwa ujenzi kamili wa monorepo, kwa sababu CI+CD inaweza kujenga miradi yote katika monorepo.

Ikiwa shirika/timu/mradi unakua, basi monorepo itakuwa na matatizo ya upanuzi.

Matatizo ya upanuzi wa monorepo yanaweza kufanya iwe na thamani zaidi na zaidi kuhamia polyrepo.

Mpito kutoka monorepo kwenda polyrepo ni kazi kubwa ya devops, na itahitaji kupangwa, kusimamiwa, na kuprogramiwa.


## Yanayohusiana


### Maamuzi yanayohusiana

Tutaunda maamuzi kwa zana zinazohusiana za kusimamia monorepo (mf. Google Bazel) na polyrepo (mf. Lyft Refactorator).


### Mahitaji yanayohusiana

Tunahitaji kuunda mfereji wa CI+CD ufanye kazi vizuri na git.


### Vielelezo vinavyohusiana

Tunatarajia mpangilio wa hifadhi kuwa na vielelezo vinavyohusiana kwa utoaji, usimamizi wa usanidi, majaribio, na maeneo yanayofanana ya devops. 


### Kanuni zinazohusiana

Inayoweza kurudishwa kwa urahisi. Ikiwa monorepo haifanyi kazi kwa vitendo, au haitakiwi na uongozi, ni rahisi kubadilisha kwenda polyrepo.

Kuwa na wazimu wa mteja. Tunathamini kuweka mradi mikononi mwa wateja, na tunaamini monorepo inaweza kutufikisha huko kwa kasi zaidi kuliko polyrepo, na pia kutusaidia kurudia kwa kasi zaidi.

Fikiria kubwa. Google na Facebook ni watetezi wenye nguvu sana wa monorepo badala ya polyrepo, kwa sababu bidhaa zote kuu zinaweza kuundwa/kujaribiwa/kuwekwa kwa pamoja.


## Maelezo ya ziada

Ongeza maelezo yoyote hapa.
