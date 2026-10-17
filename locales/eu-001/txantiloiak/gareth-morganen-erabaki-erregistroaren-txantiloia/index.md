# [000] Izenburua
*Esleitu zenbaki bat ADR bakoitzari erraz erreferentziatzeko eta katalogatzeko* \
*OHARRA: Letra etzanezko testu guztiek aholkuak ematen dituzte eta produkziorako kendu behar dira*

## Egoera - ZIRRIBORROA / AKTIBOA /  [000]-K ZAHARKITUA / [000] ORDEZTEN DU

## Testuingurua
*Deskribatu laburki ADR honek jorratu nahi dituen arazoak, eta zergatik dauden arazo horiek.*

## Erabakitako ikuspegia
*Zehaztu hartu den / hartuko den arkitekturaren ikuspegitik esanguratsua den erabakia eta deskribatu nola jorratzen dituen Testuingurua atalean azaldutako arazoak.*

## Ondorioak
*Zein da erabaki honek sistemaren arkitektura-ezaugarrietan eta eskakizun funtzionaletan duen eragina?*

## Gobernantza
*Nola jarraituko zaie erabaki honen emaitzei?* \
*Nola ziurtatuko da erabaki honekiko betetzea?*

## Aukeren analisia
*Aplikagarria bada, sartu edo estekatu dokumentu honetan hartutako erabakira iristeko egin den konpentsazio-analisia.*

### Gakoa
*Aukerakoa: Eman interesdunei laguntza bisualak konpentsazio positiboak eta negatiboak azkar identifikatzen laguntzen dutenak - adibidez, semaforo-nabarmentze sinpleak aurrizki positibo edo negatiboekin.*

Atzeko plano <span style="background-color:#4bce97; color:black;">berdeak</span> egokitzapen ona adierazten du, <span style="background-color:#f1c232; color:black;">anbarra</span> aldera okertuz, eta <span style="background-color:#e06666; color:black;">gorria</span> egokitzapen txarrena izanik. \
\+ eragin positiboa duen iruzkina adierazten du \
\- eragin negatiboa duen iruzkina adierazten du

### Goi-mailako ikuspegi orokorra
*Zenbat egokitzen da aukera bakoitza arazoaren testuinguruari begirada batean?*

<table>
  <thead>
    <tr>
      <th>Laburpena</th>
      <th>Aukera 1</th>
      <th>Aukera 2</th>
      <th>Aukera 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Ezartzeko erraztasuna</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Oso erraza
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Zaila
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Ezarpen handia, ezagutza espezializatua behar duena
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Epeak</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Oso azkarra
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Nahiko motela
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Oso motela
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Balio estrategikoa</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Balio estrategikorik ez, taktikoa soilik
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Bezeroen harrera-esperientzia apur bat hobetzen du
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ezin hobea datorren bategiterako
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Eskakizun funtzionalak
*Zenbat egokitzen da aukera potentzial bakoitza nahi diren eskakizun funtzionalei?*

<table>
  <thead>
    <tr>
      <th>Eszenatokia</th>
      <th><i>Aukera 1</i></th>
      <th><i>Aukera 2</i></th>
      <th><i>Aukera 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Eszenatokia 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Eszenatokia 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Eszenatokia 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Aukerakoa: Gehitu errenkadak / beste taula bat ezagutzen diren etorkizuneko eszenatokiak estaltzeko.*

### Eskakizun ez-funtzionalak
*Zenbat egokitzen da aukera potentzial bakoitza nahi diren arkitektura-ezaugarriei?
Oharra: 'Arkitektura-ezaugarriak' izenburu egokiagoa litzateke, baina egokitu zure negozio-domeinuko hizkera ezagunera.*

<table>
  <thead>
    <tr>
      <th>Arkitektura- </br> ezaugarria</th>
      <th><i>Aukera 1</i></th>
      <th><i>Aukera 2</i></th>
      <th><i>Aukera 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Eskalagarritasuna</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Errendimendua</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Erabilgarritasuna</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Aukerakoa: Gehitu arkitektura-ezaugarrien definizioak edo estekatu, zure negozioari / produktuari dagozkienez.*
