# Mchakato wa Rekodi za Maamuzi ya Usanifu wa AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Rekodi ya uamuzi wa usanifu (ADR) ni hati inayoeleza chaguo ambalo timu hufanya kuhusu kipengele muhimu cha usanifu wa programu wanayopanga kujenga. Kila ADR inaeleza uamuzi wa usanifu, muktadha wake, na matokeo yake. ADR zina hali na kwa hivyo hufuata mzunguko wa maisha. Kwa mfano wa ADR, tazama kiambatisho.

Mchakato wa ADR hutoa mkusanyiko wa rekodi za maamuzi ya usanifu. Mkusanyiko huu huunda kumbukumbu ya maamuzi. Kumbukumbu ya maamuzi hutoa muktadha wa mradi pamoja na maelezo ya kina ya utekelezaji na usanifu. Wanachama wa mradi hupitia vichwa vya habari vya kila ADR ili kupata muhtasari wa muktadha wa mradi. Husoma ADR ili kuzama kwa kina katika utekelezaji na chaguo za usanifu wa mradi.

Timu inapokubali ADR, inakuwa isiyobadilika. Ikiwa maarifa mapya yanahitaji uamuzi tofauti, timu hupendekeza ADR mpya. Timu inapokubali ADR mpya, inachukua nafasi ya ADR ya awali.

## Wigo wa mchakato wa ADR

Wanachama wa mradi wanapaswa kuunda ADR kwa kila uamuzi muhimu kiusanifu unaoathiri mradi au bidhaa ya programu, ikiwa ni pamoja na yafuatayo (Richards na Ford 2020):

* Muundo (kwa mfano, mifumo kama huduma ndogo)

* Mahitaji yasiyo ya kiutendaji (usalama, upatikanaji wa juu, na uvumilivu wa hitilafu)

* Utegemezi (uunganishaji wa vipengele)

* Violesura (API na mikataba iliyochapishwa)

* Mbinu za ujenzi (maktaba, mifumo, zana, na michakato)

* Mahitaji ya kiutendaji na yasiyo ya kiutendaji ndiyo pembejeo za kawaida zaidi za mchakato wa ADR.


## Maudhui ya ADR

Timu inapotambua hitaji la ADR, mwanachama wa timu huanza kuandika ADR kulingana na kiolezo cha mradi mzima. (Tazama shirika la ADR kwenye GitHub kwa mifano ya violezo.) Kiolezo hurahisisha uundaji wa ADR na kuhakikisha ADR inanasa taarifa zote husika. Kwa kiwango cha chini, kila ADR inapaswa kufafanua muktadha wa uamuzi, uamuzi wenyewe, na matokeo ya uamuzi kwa mradi na bidhaa zake. (Kwa mifano ya sehemu hizi, tazama kiambatisho.) Mojawapo ya vipengele vyenye nguvu zaidi vya muundo wa ADR ni kwamba unazingatia sababu ya uamuzi badala ya jinsi timu ilivyoutekeleza. Kuelewa kwa nini timu ilifanya uamuzi huo hurahisisha wanachama wengine wa timu kuukubali, na huzuia wasanifu wengine ambao hawakuhusika katika mchakato wa kufanya uamuzi kuupindua uamuzi huo siku zijazo.


## Mchakato wa kupitisha ADR

Kila mwanachama wa timu anaweza kuunda ADR, lakini timu inapaswa kuweka fasili ya umiliki wa ADR. Kila mwandishi ambaye ni mmiliki wa ADR anapaswa kudumisha na kuwasilisha maudhui ya ADR kwa bidii. Ili kufafanua umiliki huu, mwongozo huu unarejelea waandishi wa ADR kama wamiliki wa ADR katika sehemu zinazofuata. Wanachama wengine wa timu wanaweza daima kuchangia ADR. Ikiwa maudhui ya ADR yatabadilika kabla timu haijaikubali ADR, mmiliki anapaswa kuidhinisha mabadiliko haya.

Baada ya timu kutambua uamuzi wa usanifu na mmiliki wake, mmiliki wa ADR huwasilisha ADR katika hali ya **Proposed** (Imependekezwa) mwanzoni mwa mchakato. ADR zilizo katika hali ya Imependekezwa ziko tayari kwa mapitio.

Kisha mmiliki wa ADR huanzisha mchakato wa mapitio ya ADR. Lengo la mchakato wa mapitio ya ADR ni kuamua kama timu inakubali ADR, inabaini kwamba inahitaji marekebisho, au inakataa ADR. Timu ya mradi, ikiwa ni pamoja na mmiliki, hupitia ADR. Mkutano wa mapitio unapaswa kuanza kwa muda maalum wa kusoma ADR. Kwa wastani, dakika 10 hadi 15 zinapaswa kutosha. Katika muda huu, kila mwanachama wa timu husoma hati na kuongeza maoni na maswali kuashiria mada zisizo wazi. Baada ya awamu ya mapitio, mmiliki wa ADR husoma kwa sauti na kujadili kila maoni na timu.

Ikiwa timu itapata vitendo vya kuboresha ADR, hali ya ADR inabaki **Proposed** (Imependekezwa). Mmiliki wa ADR hutunga vitendo hivyo na, kwa ushirikiano na timu, huongeza mtu wa kuwajibika kwa kila kitendo. Kila mwanachama wa timu anaweza kuchangia na kutatua vitendo hivyo. Ni jukumu la mmiliki wa ADR kupanga upya mchakato wa mapitio.

Timu pia inaweza kuamua kukataa ADR. Katika hali hii, mmiliki wa ADR huongeza sababu ya kukataa ili kuzuia mijadala ya baadaye kuhusu mada hiyo hiyo. Mmiliki hubadilisha hali ya ADR kuwa **Rejected** (Imekataliwa).

Ikiwa timu itaidhinisha ADR, mmiliki huongeza muhuri wa muda, toleo, na orodha ya wadau. Kisha mmiliki husasisha hali kuwa **Accepted** (Imekubaliwa).

ADR na kumbukumbu ya maamuzi wanayounda huwakilisha maamuzi yaliyofanywa na timu na kutoa historia ya maamuzi yote. Timu hutumia ADR kama rejeleo wakati wa mapitio ya msimbo na usanifu inapowezekana. Mbali na kufanya mapitio ya msimbo, kazi za usanifu, na kazi za utekelezaji, wanachama wa timu wanapaswa kushauriana na ADR kwa maamuzi ya kimkakati ya bidhaa.

Kama mazoea mazuri, kila badiliko la programu linapaswa kupitia mapitio ya wenzao na kuhitaji angalau idhini moja. Wakati wa mapitio ya msimbo, mkaguzi anaweza kupata mabadiliko yanayokiuka ADR moja au zaidi. Katika hali hii, mkaguzi anamwomba mwandishi wa badiliko la msimbo kusasisha msimbo, na kushiriki kiungo cha ADR. Mwandishi anaposasisha msimbo, huidhinishwa na wakaguzi wenzake na kuunganishwa kwenye msingi mkuu wa msimbo.


## Mchakato wa mapitio ya ADR

Timu inapaswa kuchukulia ADR kama hati zisizobadilika baada ya timu kuzikubali au kuzikataa. Mabadiliko kwa ADR iliyopo yanahitaji kuunda ADR mpya, kuweka mchakato wa mapitio kwa ADR mpya, na kuidhinisha ADR hiyo. Ikiwa timu itaidhinisha ADR mpya, mmiliki anapaswa kubadilisha hali ya ADR ya zamani kuwa **Superseded** (Imechukuliwa nafasi).
