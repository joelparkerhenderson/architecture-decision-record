# [000] Nosaukums
*Piešķiriet katram ADR numuru vieglai atsaucei un kataloģizēšanai* \
*PIEZĪME: viss slīpraksta teksts sniedz mājienus, un to ražošanas versijā jānoņem*

## Statuss - DRAFT / ACTIVE /  DEPRECATED by [000] / SUPERSEDES [000]

## Konteksts
*Īsi aprakstiet problēmu(-as), kuras šis ADR paredz risināt, un kāpēc problēmas pastāv.*

## Izvēlētā pieeja
*Detalizēti aprakstiet arhitektūriski nozīmīgo lēmumu, kas ir pieņemts / tiks pieņemts, un aprakstiet, kā tas risina sadaļā Konteksts izklāstītās problēmas.*

## Sekas
*Kāda ir šī lēmuma ietekme uz sistēmas arhitektūras raksturlielumiem un funkcionālajām prasībām?*

## Pārvaldība
*Kā tiks uzraudzīti šī lēmuma iznākumi?* \
*Kā tiks nodrošināta atbilstība šim lēmumam?*

## Iespēju analīze
*Ja piemērojams, iekļaujiet vai norādiet saiti uz jebkuru kompromisu analīzi, kas veikta, lai nonāktu pie šajā dokumentā pieņemtā lēmuma.*

### Apzīmējumi
*Pēc izvēles: nodrošiniet ieinteresētajām pusēm vizuālus palīglīdzekļus, kas palīdz ātri pamanīt pozitīvos un negatīvos kompromisus – piemēram, vienkāršus luksofora izcēlumus ar pozitīviem vai negatīviem prefiksiem.*

<span style="background-color:#4bce97; color:black;">Zaļš</span> fons norāda uz labu atbilstību, pasliktinoties caur <span style="background-color:#f1c232; color:black;">dzintara</span>, un <span style="background-color:#e06666; color:black;">sarkans</span> ir sliktākā atbilstība. \
\+ norāda uz komentāru ar pozitīvu ietekmi \
\- norāda uz komentāru ar negatīvu ietekmi

### Augsta līmeņa pārskats
*Cik labi katra iespēja uz pirmo acu uzmetienu atbilst problēmas kontekstam?*

<table>
  <thead>
    <tr>
      <th>Kopsavilkums</th>
      <th>1. iespēja</th>
      <th>2. iespēja</th>
      <th>3. iespēja</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Īstenošanas vienkāršība</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Ļoti viegli
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Sarežģīti
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Liela īstenošana, kas prasa ekspertu zināšanas
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Laika grafiki</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ļoti ātri
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Diezgan lēni
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Ļoti lēni
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Stratēģiskā vērtība</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Nav stratēģiskas vērtības, tīri taktisks
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Nedaudz uzlabo klientu ievadīšanas pieredzi
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ideāli piemērots gaidāmajai apvienošanai
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Funkcionālās prasības
*Cik labi katra potenciālā iespēja atbilst vēlamajām funkcionālajām prasībām?*

<table>
  <thead>
    <tr>
      <th>Scenārijs</th>
      <th><i>1. iespēja</i></th>
      <th><i>2. iespēja</i></th>
      <th><i>3. iespēja</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>1. scenārijs</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>2. scenārijs</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>3. scenārijs</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Pēc izvēles: pievienojiet rindas / citu tabulu, lai aptvertu zināmus nākotnes scenārijus.*

### Nefunkcionālās prasības
*Cik labi katra potenciālā iespēja atbilst vēlamajiem arhitektūras raksturlielumiem?
Piezīme: „Arhitektūras raksturlielumi” būtu piemērotāks nosaukums, taču pielāgojiet to valodai, kas pazīstama jūsu biznesa jomā.*

<table>
  <thead>
    <tr>
      <th>Arhitektūras </br> raksturlielums</th>
      <th><i>1. iespēja</i></th>
      <th><i>2. iespēja</i></th>
      <th><i>3. iespēja</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Mērogojamība</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Veiktspēja</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Pieejamība</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Pēc izvēles: pievienojiet vai norādiet saiti uz arhitektūras raksturlielumu definīcijām, kā tās attiecas uz jūsu biznesu / produktu.*
