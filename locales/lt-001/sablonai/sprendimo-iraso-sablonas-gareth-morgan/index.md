# [000] Pavadinimas
*Kiekvienam ADR priskirkite numerį, kad būtų lengva remtis ir kataloguoti* \
*PASTABA: visas kursyvu parašytas tekstas yra užuominos ir turi būti pašalintas galutinėje versijoje*

## Būsena – JUODRAŠTIS / AKTYVUS /  NEBENAUDOTINAS pagal [000] / PAKEIČIA [000]

## Kontekstas
*Trumpai aprašykite problemą (problemas), kurią šis ADR siekia spręsti, ir kodėl tos problemos egzistuoja.*

## Pasirinktas požiūris
*Išsamiai aprašykite architektūriškai reikšmingą sprendimą, kuris buvo / bus priimtas, ir apibūdinkite, kaip jis sprendžia skyriuje „Kontekstas“ nurodytas problemas.*

## Pasekmės
*Koks šio sprendimo poveikis sistemos architektūros charakteristikoms ir funkciniams reikalavimams?*

## Valdysena
*Kaip bus stebimi šio sprendimo rezultatai?* \
*Kaip bus užtikrinta šio sprendimo atitiktis?*

## Variantų analizė
*Jei taikoma, įtraukite arba pateikite nuorodą į bet kokią kompromisų analizę, atliktą siekiant priimti šiame dokumente aprašytą sprendimą.*

### Legenda
*Neprivaloma: suinteresuotiesiems asmenims pateikite vaizdines priemones, padedančias greitai pastebėti teigiamus ir neigiamus kompromisus – pavyzdžiui, paprastą šviesoforo paryškinimą su teigiamais ar neigiamais priešdėliais.*

<span style="background-color:#4bce97; color:black;">Žalias</span> fonas rodo gerą atitiktį, kuri blogėja per <span style="background-color:#f1c232; color:black;">gintarinį</span>, o <span style="background-color:#e06666; color:black;">raudonas</span> yra blogiausia atitiktis. \
\+ rodo teigiamą poveikį darantį komentarą \
\- rodo neigiamą poveikį darantį komentarą

### Aukšto lygio apžvalga
*Kaip gerai kiekvienas variantas iš pirmo žvilgsnio tinka problemos kontekstui?*

<table>
  <thead>
    <tr>
      <th>Santrauka</th>
      <th>1 variantas</th>
      <th>2 variantas</th>
      <th>3 variantas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Įgyvendinimo paprastumas</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Labai paprasta
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Sudėtinga
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Didelis įgyvendinimas, reikalaujantis ekspertinių žinių
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Terminai</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Labai greita
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Gana lėta
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Labai lėta
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Strateginė vertė</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Jokios strateginės vertės, grynai taktinis
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Šiek tiek pagerina klientų įvedimo patirtį
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Idealiai tinka artėjančiam susijungimui
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Funkciniai reikalavimai
*Kaip gerai kiekvienas galimas variantas atitinka pageidaujamus funkcinius reikalavimus?*

<table>
  <thead>
    <tr>
      <th>Scenarijus</th>
      <th><i>1 variantas</i></th>
      <th><i>2 variantas</i></th>
      <th><i>3 variantas</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>1 scenarijus</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>2 scenarijus</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>3 scenarijus</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Neprivaloma: pridėkite eilučių / dar vieną lentelę žinomiems būsimiems scenarijams aprėpti.*

### Nefunkciniai reikalavimai
*Kaip gerai kiekvienas galimas variantas atitinka pageidaujamas architektūros charakteristikas?
Pastaba: tinkamesnis pavadinimas būtų „Architektūros charakteristikos“, tačiau pritaikykite jį jūsų verslo srityje įprastai kalbai.*

<table>
  <thead>
    <tr>
      <th>Architektūros </br> charakteristika</th>
      <th><i>1 variantas</i></th>
      <th><i>2 variantas</i></th>
      <th><i>3 variantas</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Mastelio keitimas</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Našumas</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Prieinamumas</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Neprivaloma: pridėkite architektūros charakteristikų apibrėžimus, susijusius su jūsų verslu / produktu, arba nuorodas į juos.*