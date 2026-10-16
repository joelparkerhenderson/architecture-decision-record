# Arhitektūras lēmuma ieraksts: CSS ietvars

Saturs:

- [Kopsavilkums](#kopsavilkums)
  - [Jautājums](#jautājums)
  - [Lēmums](#lēmums)
  - [Statuss](#statuss)
- [Detaļas](#detaļas)
  - [Pieņēmumi](#pieņēmumi)
  - [Ierobežojumi](#ierobežojumi)
  - [Pozīcijas](#pozīcijas)
  - [Arguments](#arguments)
  - [Sekas](#sekas)
- [Saistītais](#saistītais)
  - [Saistītie lēmumi](#saistītie-lēmumi)
  - [Saistītās prasības](#saistītās-prasības)
  - [Saistītie artefakti](#saistītie-artefakti)
  - [Saistītie principi](#saistītie-principi)
- [Piezīmes](#piezīmes)


## Kopsavilkums


### Jautājums

Mēs vēlamies izmantot CSS ietvaru savu tīmekļa lietojumprogrammu izveidei:

  * Mēs vēlamies, lai lietotāja pieredze būtu ātra un uzticama visās populārajās pārlūkprogrammās un ekrāna izmēros.

  * Mēs vēlamies ātru dizaina, izkārtojuma, UI/UX utt. iterāciju.

  * Mēs vēlamies atsaucīgas lietojumprogrammas, īpaši mazākiem ekrāniem, piemēram, mobilajās ierīcēs, lielākiem ekrāniem, piemēram, 4K platekrāniem, un dinamiskiem ekrāniem, piemēram, rotējamiem displejiem.  


### Lēmums

Izvēlējāmies Bulma.


### Statuss

Izvēlējāmies Bulma. Esam atvērti jaunām CSS ietvaru izvēlēm, kad tās parādās.


## Detaļas


### Pieņēmumi

Mēs vēlamies izveidot tīmekļa lietotnes, kas ir modernas, ātras, uzticamas, atsaucīgas utt.

Tipiskas modernas tīmekļa lietotnes samazina/novērš jQuery izmantošanu vairāku iemeslu dēļ: 

  * Moderns JavaScript pakāpeniski ievieš daudzas iespējas, ko nodrošināja jQuery, tāpēc jQuery ir mazāk vajadzīgs, un ir labāki/ātrāki/mazāki moduļi, kas nodrošina konkrētus īstenojumus

  * jQuery plašā pieeja ir tieša DOM manipulācija, kas ir antimodelis modernajiem JavaScript ietvariem (piem., React, Vue, Svelte)

  * jQuery traucē pats sev, ja tas tiek ielādēts divreiz utt.


### Ierobežojumi

Ja mēs izvēlamies CSS ietvaru, kas izmanto jQuery, mēs esam spiesti importēt jQuery. Piemēram, Semantic UI izmanto jQuery, bet Tachyons neizmanto.

Ja mēs izvēlamies CSS ietvaru, kas ir minimāls, mēs atsakāmies no ietvara komponentēm, kuras varētu vēlēties tagad vai drīz. Piemēram, Semantic UI nodrošina attēlu karuseli, bet Tachyons nenodrošina.


### Pozīcijas

Mēs apsvērām iespēju neizmantot nekādu ietvaru. Tas joprojām šķiet dzīvotspējīgi, īpaši tāpēc, ka CSS grid nodrošina lielu daļu no tā, kas mums nepieciešams mūsu projektam..

Mēs apsvērām daudzus CSS ietvarus, izmantojot ātru īsā saraksta atlasi: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons utt. Mūsu divas izvēles padziļinātai pārskatīšanai ir Semantic UI (jo tam ir visvairāk semantiskā pieeja) un Bulma (jo tai ir vieglākā pieeja, kas nodrošina komponentes, kuras mēs vēlamies tagad).

Mēs apsvērām Semantic UI. Tas nodrošina daudzas komponentes, tostarp tās, kuras vēlamies savam projektam: cilnes, režģus, pogas utt. Mēs veicām pilotu ar Semantic UI divos veidos: izmantojot tipiskus CDN failus un izmantojot NPM repozitorijus. Mēs guvām panākumus ar Semantic UI statiskā HTML lapā, bet nepanācām panākumus savā laika logā, veidojot JavaScript SPA (galvenokārt jQuery ielādes problēmu dēļ). Mēs atklājām, ka citi programmētāji lūdz Semantic UI izstrādātājiem izveidot versiju bez jQuery tādu pašu iemeslu dēļ kā mēs. Citi programmētāji daudzus gadus ir pieprasījuši versiju bez jQuery, taču izstrādātāji ir atteikušies un norādījuši, ka jebkura versija bez jQuery būtu pārāk grūti uzrakstāma, piem. ~„Semantic UI projektam ir vairāk nekā 22 000 saskares punktu, kas izmanto jQuery”.

Piemērs ar Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Mēs apsvērām Bulma. Bulma ir daudzas līdzīgas iespējas kā Semantic UI, lai gan ne tik daudz sarežģītu komponenšu. Bulma ir veidota ar modernām metodēm, piemēram, bez jQuery. Bulma ir dažas trešo pušu komponentes, no kurām dažas mēs varētu vēlēties izmantot.


Piemērs ar Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Arguments

Kā iepriekš.

Konkrēti, Semantic UI šķiet brīdinājuma karogs gan tehnoloģijas ziņā (t. i., tik daudz jQuery saskares punktu), gan vadības ziņā (t. i., versija bez jQuery bija stingrs nē, nevis mēģinājums izveidot ceļvedi, nepārtrauktu uzlabošanu, ziedojumu vākšanu utt.).


### Sekas

Ja atrodam labu CSS ietvaru bez jQuery, tas kopumā ir noderīgi un labi.


## Saistītais


### Saistītie lēmumi

Mūsu izvēlētais CSS ietvars var ietekmēt testējamību.


### Saistītās prasības

Mēs vēlamies ātri piegādāt tīri modernu lietotni. 

Mēs nevēlamies tērēt laiku darbam ar vecākiem ietvariem (īpaši Semantic UI), kas izmanto vecākas atkarības (īpaši jQuery).


### Saistītie artefakti

Ietekmē visu tipisko HTML, kas izmantos CSS.


### Saistītie principi

Viegli atgriezenisks.

Nepieciešamība pēc ātruma.


## Piezīmes

Jebkādas piezīmes šeit.
