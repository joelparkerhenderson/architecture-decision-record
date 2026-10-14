# Rekodi ya Uamuzi wa Usanifu: Mfumo wa CSS

Yaliyomo:

- [Muhtasari](#muhtasari)
  - [Suala](#suala)
  - [Uamuzi](#uamuzi)
  - [Hali](#hali)
- [Undani](#undani)
  - [Dhana](#dhana)
  - [Vikwazo](#vikwazo)
  - [Misimamo](#misimamo)
  - [Hoja](#hoja)
  - [Athari](#athari)
- [Yanayohusiana](#yanayohusiana)
  - [Maamuzi yanayohusiana](#maamuzi-yanayohusiana)
  - [Mahitaji yanayohusiana](#mahitaji-yanayohusiana)
  - [Vielelezo vinavyohusiana](#vielelezo-vinavyohusiana)
  - [Kanuni zinazohusiana](#kanuni-zinazohusiana)
- [Maelezo ya ziada](#maelezo-ya-ziada)


## Muhtasari


### Suala

Tunataka kutumia mfumo wa CSS kuunda programu zetu za wavuti:

  * Tunataka uzoefu wa mtumiaji uwe wa haraka na wa kuaminika, kwenye vivinjari vyote maarufu na ukubwa wa skrini.

  * Tunataka uundaji wa awamu wa haraka wa muundo, mpangilio, UI/UX, n.k.

  * Tunataka programu zinazojibu haraka (responsive), hasa kwa skrini ndogo kama kwenye vifaa vya simu, skrini kubwa kama skrini pana za 4K, na skrini zenye mabadiliko kama maonyesho yanayozunguka.  


### Uamuzi

Tuliamua Bulma.


### Hali

Tuliamua Bulma. Tuko wazi kwa chaguo mpya za mifumo ya CSS zitakapofika.


## Undani


### Dhana

Tunataka kuunda programu za wavuti ambazo ni za kisasa, za haraka, za kuaminika, zinazojibu haraka, n.k.

Programu za kawaida za kisasa za wavuti zinapunguza/zinaondoa matumizi ya jQuery kwa sababu nyingi: 

  * JavaScript ya kisasa inaingiza polepole uwezo mwingi ambao jQuery imetoa, kwa hivyo jQuery inahitajika kidogo, na kuna moduli bora/za haraka/ndogo zinazotoa utekelezaji mahsusi

  * Mbinu pana ya jQuery ni kufanya upotoshaji wa moja kwa moja wa DOM, ambao ni kinyume cha mifumo ya kisasa ya JavaScript (mf. React, Vue, Svelte)

  * jQuery inajiingilia yenyewe ikipakiwa mara mbili, n.k.


### Vikwazo

Tukichagua mfumo wa CSS unaotumia jQuery, basi tumekwama kuingiza jQuery. Kwa mfano, Semantic UI inatumia jQuery, na Tachyons haitumii.

Tukichagua mfumo wa CSS ulio mdogo kabisa, basi tunaachana na vipengele vya mfumo ambavyo tunaweza kuvitaka sasa au hivi karibuni. Kwa mfano, Semantic UI hutoa karoseli ya picha, na Tachyons haitoi.


### Misimamo

Tulizingatia kutotumia mfumo wowote. Hii bado inaonekana inawezekana, hasa kwa sababu CSS grid hutoa mengi ya tunayohitaji kwa mradi wetu..

Tulizingatia mifumo mingi ya CSS kwa kutumia upangaji wa haraka wa orodha fupi: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons, n.k. Chaguo zetu mbili za mapitio ya kina zaidi ni Semantic UI (kwa sababu ina mbinu yenye maana zaidi) na Bulma (kwa sababu ina mbinu nyepesi zaidi inayotoa vipengele tunavyovitaka sasa).

Tulizingatia Semantic UI. Hii hutoa vipengele vingi, ikiwa ni pamoja na vile tunavyovitaka kwa mradi wetu: vichupo, gridi, vitufe, n.k. Tulifanya majaribio ya awali na Semantic UI kwa njia mbili: kwa kutumia faili za kawaida za CDN, na kwa kutumia hifadhi za NPM. Tulifanikiwa na Semantic UI katika ukurasa tuli wa HTML, lakini hatukufanikiwa ndani ya kikomo chetu cha muda kujenga SPA ya JavaScript (hasa kwa sababu ya matatizo ya upakiaji wa jQuery). Tuligundua kwamba waandishi wengine wa msimbo wamekuwa wakiwaomba waundaji wa Semantic UI kuunda toleo lisilo na jQuery, kwa sababu zilezile tulizonazo. Waandishi wengine wa msimbo wamekuwa wakiomba toleo lisilo na jQuery kwa miaka mingi, lakini waundaji wamesema hapana, na wakasema toleo lolote lisilo na jQuery lingekuwa gumu mno kuandika mf. ~"mradi wa Semantic UI una zaidi ya vituo 22,000 vya kugusa vinavyotumia jQuery".

Mfano na Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Tulizingatia Bulma. Bulma ina uwezo mwingi unaofanana na Semantic UI, ingawa si vipengele vingi vya hali ya juu. Bulma imejengwa kwa mbinu za kisasa, kama kutokuwa na jQuery. Bulma ina vipengele vichache vya wahusika wa tatu, ambavyo baadhi yake tunaweza kutaka kuvitumia.


Mfano na Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Hoja

Kama ilivyo hapo juu.

Hasa, Semantic UI inaonekana kuwa na bendera ya tahadhari kwa upande wa teknolojia (yaani vituo vingi vya kugusa vya jQuery) na pia kwa upande wa uongozi (yaani kutokuwa na jQuery lilikuwa kataa kali, badala ya kujaribu ramani ya njia, au maboresho endelevu, au kuchangisha michango, n.k.).


### Athari

Ikiwa tutapata mfumo mzuri wa CSS usio na jQuery, hii kwa ujumla ni ya msaada na nzuri kwa ujumla.


## Yanayohusiana


### Maamuzi yanayohusiana

Mfumo wa CSS tunaochagua unaweza kuathiri uwezo wa kujaribiwa.


### Mahitaji yanayohusiana

Tunataka kusafirisha programu ya kisasa kabisa kwa haraka. 

Hatutaki kutumia muda kufanya kazi na mifumo ya zamani (hasa Semantic UI) inayotumia utegemezi wa zamani (hasa jQuery).


### Vielelezo vinavyohusiana

Huathiri HTML yote ya kawaida itakayotumia CSS.


### Kanuni zinazohusiana

Inayoweza kurudishwa kwa urahisi.

Haja ya kasi.


## Maelezo ya ziada

Maelezo yoyote hapa.
