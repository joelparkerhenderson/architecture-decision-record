# Muundo wa muhuri wa muda

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

Tunataka kuweza kufuatilia mambo yanapotokea kwa kutumia mihuri ya muda na kwa kutumia muundo thabiti wa muhuri wa muda unaofanya kazi vizuri katika mifumo yetu yote na mifumo ya wahusika wa tatu.

Tunaingiliana na mifumo yenye miundo tofauti ya mihuri ya muda:

* Ujumbe wa JSON hauna muundo asilia wa muhuri wa muda, kwa hivyo tunahitaji kuchagua jinsi ya kubadilisha muhuri wa muda kuwa mfuatano wa herufi, na kubadilisha mfuatano wa herufi kuwa muhuri wa muda, yaani jinsi ya kuserialisha/kuondoa userialishaji.

* Baadhi ya programu zimewekwa kutumia saa ya mahali, badala ya saa ya UTC. Hii inaweza kuwa rahisi kwa miradi inayopaswa kurekebisha kulingana na saa ya mahali, kama miradi inayoanzisha matukio yanayotegemea saa ya mahali.

* Baadhi ya mifumo ina mahitaji na uwezo tofauti wa usahihi wa muda, kama kutumia azimio la muda la sekunde dhidi ya milisekunde dhidi ya nanosekunde. Kwa mfano, amri ya `date` ya mfumo wa uendeshaji wa Linux hutumia usahihi wa muda chaguomsingi wa sekunde, ilhali soko la hisa la Nasdaq linataka usahihi wa muda chaguomsingi wa nanosekunde.


### Uamuzi

Tunachagua muundo sanifu wa muhuri wa muda ISO 8601 wenye usahihi wa nanosekunde, hasa "YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ".

Muundo unaonyesha mwaka, mwezi, siku, saa, dakika, sekunde, nanosekunde, na ukanda wa saa wa Zulu a.k.a. UTC, GMT.


### Hali

Imeamuliwa.


## Undani


### Dhana

Tunahitaji kushughulikia mifuatano hii ya maandishi ya mihuri ya muda, kubadilisha kutoka muhuri wa muda kuwa mfuatano wa herufi (a.k.a. kuserialisha) na kubadilisha kutoka mfuatano wa herufi kuwa muhuri wa muda (a.k.a. kuondoa userialishaji).

Tunataka muundo ambao kwa ujumla ni rahisi kutumia, rahisi kubadilisha, na rahisi kwa mtu kusoma.

Tunataka upatanifu na anuwai pana ya mifumo ya nje ambayo hatuwezi kuidhibiti, kama mifumo ya uchanganuzi, mifumo ya hifadhidata, mifumo ya kifedha.


### Vikwazo

Baadhi ya mifumo ina mapungufu ya usahihi wa muda. Kwa mfano, amri ya `date` ya mfumo wa uendeshaji wa macOS inaweza kuchapisha usahihi wa muda kwa sekunde, lakini si kwa nanosekunde.


### Misimamo

Tulizingatia anuwai ya chaguo:

* Unix epoch yaani nambari moja inayoongezeka.

* Muundo mfupi wa maandishi "YYYYMMDDTHHMMSSNNNNNNNNN".

* Kutumia ukanda wa saa wa mahali dhidi ya ukanda wa saa wa UTC.


### Hoja

Kwa matumizi ya kawaida, tunathamini urahisi wa kusoma/kuandika kwa binadamu, zaidi ya kasi/ukubwa ghafi.

Kwa matumizi ya kawaida, tunataka muundo unaofanya kazi vizuri katika mifumo ya mashine, na pia unafanya kazi vizuri kwa mkono, kama kuandika data ya sampuli, kusoma pato la JSON, kutafuta kwa grep kwenye faili ya kumbukumbu, n.k.

Kwa matumizi yasiyo ya kawaida, kama kompyuta ya utendaji wa juu, tunatarajia tutataka kuboresha muundo wowote wa maandishi tunaochagua kwa kubadilisha maandishi kuwa muundo wa haraka zaidi, kama aina ya kitu cha tarehe iliyojengewa ndani ya lugha ya programu. Kwa hivyo muundo wa maandishi hauna umuhimu mkubwa kwa HPC.


### Athari

Mifumo yetu mbalimbali ya maandishi na mifumo ya muda itakusanyika kwenye muundo huu.


## Yanayohusiana


### Maamuzi yanayohusiana

Tunaweza kutaka njia ya haraka/rahisi pia ya kufuatilia tofauti za muda a.k.a. vipindi. Hivi ni rahisi kwa mihuri ya muda ya Unix epoch.


### Mahitaji yanayohusiana

Tunaweza kutaka kurekebisha uamuzi wetu mf. ikiwa tuna hitaji linalohusiana la aina mahsusi ya muhuri wa ujumbe wa kumbukumbu, kama kwa Splunk, Sumo, ELK, n.k.


### Vielelezo vinavyohusiana

Wapangaji muundo na wachanganuzi wa lugha:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Mifano ya Rosetta Code:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Mifano ya SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Kanuni zinazohusiana

Inayoweza kurudishwa kwa urahisi. Tunaweza kubadilisha kwa urahisi kabisa kwenda muundo tofauti, kama Unix epoch.

Ahirisha uboreshaji wa mapema. Kwa matumizi ya kawaida hatujali sana herufi chache za ziada kama muundo unaotumia vistari na nukta mbili.


## Maelezo ya ziada

Ongeza maelezo hapa.
