# [000] Naslov
*Vsakemu ADR dodelite številko za preprosto sklicevanje in katalogiziranje* \
*OPOMBA: Vse poševno besedilo podaja namige in ga je treba za produkcijsko rabo odstraniti*

## Status - DRAFT / ACTIVE /  DEPRECATED by [000] / SUPERSEDES [000]

## Kontekst
*Na kratko opišite problem(e), ki jih ta ADR namerava obravnavati, in zakaj problemi obstajajo.*

## Izbrani pristop
*Podrobno opišite arhitekturno pomembno odločitev, ki je bila / bo sprejeta, in opišite, kako obravnava probleme, navedene v razdelku Kontekst.*

## Posledice
*Kakšen je vpliv te odločitve na arhitekturne lastnosti in funkcionalne zahteve sistema?*

## Upravljanje
*Kako se bodo spremljali izidi te odločitve?* \
*Kako bo zagotovljena skladnost s to odločitvijo?*

## Analiza možnosti
*Če je primerno, vključite ali povežite vse analize kompromisov, ki so bile opravljene za sprejem odločitve v tem dokumentu.*

### Legenda
*Neobvezno: Deležnikom zagotovite vizualne pripomočke, ki pomagajo hitro opaziti pozitivne in negativne kompromise – na primer preprosta semaforska poudarjanja s pozitivnimi ali negativnimi predponami.*

<span style="background-color:#4bce97; color:black;">Zelena</span> podlaga označuje dobro ujemanje, ki se slabša prek <span style="background-color:#f1c232; color:black;">rumene</span>, pri čemer je <span style="background-color:#e06666; color:black;">rdeča</span> najslabše ujemanje. \
\+ označuje komentar s pozitivnim vplivom \
\- označuje komentar z negativnim vplivom

### Pregled na visoki ravni
*Kako dobro se posamezna možnost na prvi pogled ujema s kontekstom problema?*

<table>
  <thead>
    <tr>
      <th>Povzetek</th>
      <th>Možnost 1</th>
      <th>Možnost 2</th>
      <th>Možnost 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Enostavnost izvedbe</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Zelo preprosto
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Zahtevno
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Obsežna izvedba, ki zahteva strokovno znanje
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Časovni okvirji</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Zelo hitro
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Precej počasi
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Zelo počasi
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Strateška vrednost</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Brez strateške vrednosti, povsem taktično
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Rahlo izboljša izkušnjo uvajanja strank
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Idealno za prihajajočo združitev
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Funkcionalne zahteve
*Kako dobro se posamezna možnost ujema z želenimi funkcionalnimi zahtevami?*

<table>
  <thead>
    <tr>
      <th>Scenarij</th>
      <th><i>Možnost 1</i></th>
      <th><i>Možnost 2</i></th>
      <th><i>Možnost 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Scenarij 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scenarij 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scenarij 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Neobvezno: Dodajte vrstice / drugo tabelo, ki zajema znane prihodnje scenarije.*

### Nefunkcionalne zahteve
*Kako dobro se posamezna možnost ujema z želenimi arhitekturnimi lastnostmi?
Opomba: »Arhitekturne lastnosti« bi bil ustreznejši naslov, vendar ga prilagodite jeziku, ki je znan na vašem poslovnem področju.*

<table>
  <thead>
    <tr>
      <th>Arhitekturna </br> lastnost</th>
      <th><i>Možnost 1</i></th>
      <th><i>Možnost 2</i></th>
      <th><i>Možnost 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Razširljivost</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Zmogljivost</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Razpoložljivost</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Neobvezno: Dodajte ali povežite opredelitve arhitekturnih lastnosti, kot se nanašajo na vaše poslovanje / izdelek.*
