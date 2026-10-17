# Arkitektura-erabakien erregistroa: CSS markoa

Edukia:

- [Laburpena](#laburpena)
  - [Arazoa](#arazoa)
  - [Erabakia](#erabakia)
  - [Egoera](#egoera)
- [Xehetasunak](#xehetasunak)
  - [Hipotesiak](#hipotesiak)
  - [Murriztapenak](#murriztapenak)
  - [Jarrerak](#jarrerak)
  - [Arrazoibidea](#arrazoibidea)
  - [Ondorioak](#ondorioak)
- [Erlazionatuta](#erlazionatuta)
  - [Erlazionatutako erabakiak](#erlazionatutako-erabakiak)
  - [Erlazionatutako eskakizunak](#erlazionatutako-eskakizunak)
  - [Erlazionatutako artefaktuak](#erlazionatutako-artefaktuak)
  - [Erlazionatutako printzipioak](#erlazionatutako-printzipioak)
- [Oharrak](#oharrak)


## Laburpena


### Arazoa

CSS marko bat erabili nahi dugu gure web aplikazioak sortzeko:

  * Erabiltzaile-esperientzia azkarra eta fidagarria nahi dugu, nabigatzaile eta pantaila-tamaina ezagun guztietan.

  * Diseinuan, antolaeran, UI/UX-an eta abarretan iterazio azkarra nahi dugu.

  * Aplikazio erantzunkorrak nahi ditugu, bereziki pantaila txikietarako, hala nola gailu mugikorretan, pantaila handietarako, hala nola 4K pantaila zabaletan, eta pantaila dinamikoetarako, hala nola biratu daitezkeen pantailetarako.  


### Erabakia

Bulma aukeratu da.


### Egoera

Bulma aukeratu da. CSS marko berrien aukerei irekia, iristen diren heinean.


## Xehetasunak


### Hipotesiak

Web aplikazio modernoak, azkarrak, fidagarriak, erantzunkorrak eta abar sortu nahi ditugu.

Web aplikazio moderno tipikoek jQuery-ren erabilera murrizten/ezabatzen ari dira arrazoi anitzengatik: 

  * JavaScript modernoak jQuery-k eskaini dituen gaitasun asko pixkanaka sartzen ari da, beraz jQuery gutxiago behar da, eta inplementazio espezifikoak eskaintzen dituzten modulu hobeak/azkarragoak/txikiagoak daude

  * jQuery-ren ikuspegi zabala DOM-aren zuzeneko manipulazioa da, eta hori anti-eredua da JavaScript esparru modernoentzat (adib. React, Vue, Svelte)

  * jQuery-k bere buruarekin interferitzen du birritan kargatzen bada, eta abar


### Murriztapenak

jQuery erabiltzen duen CSS marko bat aukeratzen badugu, jQuery inportatzera behartuta gaude. Adibidez, Semantic UI-k jQuery erabiltzen du, eta Tachyons-ek ez.

CSS marko minimo bat aukeratzen badugu, orain edo laster nahi ditzakegun marko-osagaiei uko egiten diegu. Adibidez, Semantic UI-k irudi-karrusela eskaintzen du, eta Tachyons-ek ez.


### Jarrerak

Markorik ez erabiltzea aztertu dugu. Hori bideragarria dirudi oraindik, bereziki CSS grid-ek gure proiektuak behar duen zati handi bat eskaintzen duelako..

CSS marko asko aztertu ditugu zerrenda labur azkar baten bidez: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons, eta abar. Sakonago berrikusteko gure bi aukerak Semantic UI (ikuspegirik semantikoena duelako) eta Bulma (orain nahi ditugun osagaiak eskaintzen dituen ikuspegirik arinena duelako) dira.

Semantic UI aztertu dugu. Osagai asko eskaintzen ditu, gure proiekturako nahi ditugunak barne: fitxak, sareak, botoiak eta abar. Semantic UI-rekin pilotu bat egin dugu bi modutan: CDN fitxategi tipikoak erabiliz, eta NPM biltegiak erabiliz. Arrakasta izan dugu Semantic UI-rekin HTML orri estatiko batean, baina ez dugu arrakastarik lortu JavaScript SPA bat eraikitzeko dugun denbora-mugan (batez ere jQuery karga-arazoengatik). Aurkitu dugu beste kodetzaile batzuek Semantic UI-ren garatzaileei jQuery gabeko bertsio bat sortzeko eskatzen ari direla, guk ditugun arrazoi berberengatik. Beste kodetzaile batzuek urte askotan eskatu dute jQuery gabeko bertsio bat, baina garatzaileek ezetz esan dute, eta jQuery gabeko edozein bertsio idazteko zailegia izango litzatekeela adierazi dute, adib. ~"Semantic UI proiektuak jQuery erabiltzen duten 22.000 ukipen-puntu baino gehiago ditu".

Semantic-ekin adibidea:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Bulma aztertu dugu. Bulma-k Semantic UI-ren antzeko gaitasun asko ditu, nahiz eta osagai sofistikatu horrenbeste ez eduki. Bulma teknika modernoekin eraikita dago, hala nola jQuery gabe. Bulma-k hirugarrenen osagai batzuk ditu, eta horietako batzuk erabili nahi izango ditugu.


Bulma-rekin adibidea:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Arrazoibidea

Goian bezala.

Zehazki, Semantic UI-k kontu-banderola bat duela dirudi, bai teknologiari dagokionez (hau da, jQuery ukipen-puntu horrenbeste), bai lidergoari dagokionez (hau da, jQuery gabekoa ezezko tinko bat izan zen, ibilbide-orri bat, etengabeko hobekuntza edo dirua biltzeko ekimenak eta abar saiatu beharrean).


### Ondorioak

jQuery gabeko CSS marko on bat aurkitzen badugu, orokorrean lagungarria eta ona da.


## Erlazionatuta


### Erlazionatutako erabakiak

Aukeratzen dugun CSS markoak probagarritasunean eragin dezake.


### Erlazionatutako eskakizunak

Aplikazio guztiz modernoa azkar bidali nahi dugu. 

Ez dugu denbora galdu nahi mendekotasun zaharrak (bereziki jQuery) erabiltzen dituzten marko zaharretan (bereziki Semantic UI) lanean.


### Erlazionatutako artefaktuak

CSS-a erabiliko duen HTML tipiko guztian eragiten du.


### Erlazionatutako printzipioak

Erraz atzera egin daitekeena.

Abiadura beharra.


## Oharrak

Edozein ohar hemen.
