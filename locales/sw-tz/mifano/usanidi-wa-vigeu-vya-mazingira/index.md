# Usanidi wa vigeu vya mazingira

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
  * [Athari ](#athari)
* [Yanayohusiana](#yanayohusiana)
  * [Maamuzi yanayohusiana](#maamuzi-yanayohusiana)
  * [Mahitaji yanayohusiana](#mahitaji-yanayohusiana)
  * [Vielelezo vinavyohusiana](#vielelezo-vinavyohusiana)
  * [Kanuni zinazohusiana](#kanuni-zinazohusiana)
* [Maelezo ya ziada](#maelezo-ya-ziada)


## Muhtasari


### Suala

Tunataka programu zetu ziweze kusanidiwa zaidi ya vielelezo/mafaili ya kibinari/msimbo chanzi, ili ujenzi mmoja uweze kutenda tofauti kulingana na mazingira yake ya uwekaji.

  * Ili kufanikisha hili, tunataka kutumia usanidi wa vigeu vya mazingira.

  * Tunataka kusimamia usanidi kwa kutumia faili tunazoweza kudhibiti matoleo yake.

  * Tunataka kutoa urahisi fulani wa uzoefu wa waundaji, kama kujua kinachoweza kusanidiwa na thamani chaguomsingi zozote husika.


### Uamuzi

Tuliamua kutumia faili za .env pamoja na faili chaguomsingi inayohusiana na faili ya skima.


### Hali

Imeamuliwa. Tuko wazi kuzingatia uwezo mpya unapojitokeza.


## Undani


### Dhana

Tunapendelea kutenganisha msimbo wa programu na msimbo wa mazingira. Tunadhani programu inahitaji kufanya kazi tofauti katika mazingira tofauti, kama mazingira ya uundaji, mazingira ya majaribio, mazingira ya maonyesho, mazingira ya uzalishaji, n.k.

Tunapendelea mazoea ya sekta ya "12 factor app" na hata zaidi mazoea yanayohusiana ya "15 factor app".

Miradi yetu mingi ya awali imetumia kanuni ya faili ya `.env` au saraka kama hiyo ya `.env`. Kuna mazoea ya kawaida ya kuziweka nje ya udhibiti wa matoleo, na badala yake kutumia njia nyingine ya kuziweka, kudhibiti matoleo yake, na kuzisimamia.


### Vikwazo

Tunataka kuweka siri nje ya mfumo wetu wa udhibiti wa matoleo (VCS) wa usimamizi wa msimbo chanzi (SCM).

Tunataka kulenga upatanifu na mifumo na maktaba maarufu za programu. Kwa mfano, Node ina moduli "dotenv" ya kusoma usanidi wa vigeu vya mazingira.


### Misimamo

Tulizingatia mbinu chache:

  * Kuhifadhi usanidi ndani ya programu kama katika faili `config.js`.

  * Kuhifadhi usanidi katika mazingira kama katika faili `.env`.

  * Kuleta usanidi kutoka mahali panapojulikana kama seva ya leseni.


### Hoja

Tulichagua mbinu ya faili ya .env kwa sababu:

  * Ni maarufu ikiwa ni pamoja na miongoni mwa wataalamu.

  * Inafuata mtindo wa faili za `.env` ambazo timu zetu zimetumia kwa mafanikio mara nyingi kwenye miradi mingi.

  * Ni rahisi. Hasa, kwa sasa tunakubali mabadilishano makubwa tunayoyaona, kama ukosefu wa uwezo wa ukaguzi ikilinganishwa na mbinu ya seva ya leseni.


### Athari 

Tunahitaji kubaini njia ya kutenganisha usanidi wa vigeu vya mazingira ulio wa umma na usimamizi wowote wa siri.


## Yanayohusiana


### Maamuzi yanayohusiana

Tunatarajia programu zetu zote kutumia mbinu hii.

Tutapanga kusasisha programu zetu zozote zinazotumia mbinu yenye uwezo mdogo, kama kuweka moja kwa moja kwenye faili ya kibinari au kwenye msimbo chanzi.

Tutaacha kama zilivyo programu zetu zozote zinazotumia mbinu yenye uwezo zaidi, kama seva ya leseni.


### Mahitaji yanayohusiana

Tutaongeza uwezo wa devops kwa faili hizo, ikiwa ni pamoja na ndoano, majaribio, na ujumuishaji endelevu.

Tunahitaji kuwafunza wenzetu wote wa uundaji kuhusu uamuzi huu.



### Vielelezo vinavyohusiana

Kila eneo tunaloweka kitahitaji faili yake ya .env na faili zinazohusiana.


### Kanuni zinazohusiana

Inayoweza kurudishwa kwa urahisi.


## Maelezo ya ziada


Mfano wa faili `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Mfano wa faili `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Mfano wa faili `.env.schema` yenye funguo pekee:

```env
NAME
EMAIL
```
