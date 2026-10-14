# [000] Názov
*Priraďte každému ADR číslo pre jednoduché odkazovanie a katalogizáciu* \
*POZNÁMKA: Všetok kurzívou písaný text poskytuje rady a v produkčnej verzii by sa mal odstrániť*

## Stav - NÁVRH / AKTÍVNE /  ZASTARANÉ [000] / NAHRADZUJE [000]

## Kontext
*Stručne opíšte problém(y), ktoré sa tento ADR snaží riešiť, a prečo problémy existujú.*

## Zvolený prístup
*Podrobne opíšte architektonicky významné rozhodnutie, ktoré bolo / bude prijaté, a opíšte, ako rieši problémy uvedené v sekcii Kontext.*

## Dôsledky
*Aký je vplyv tohto rozhodnutia na architektonické charakteristiky a funkčné požiadavky systému?*

## Riadenie
*Ako sa budú monitorovať výsledky tohto rozhodnutia?* \
*Ako sa zabezpečí súlad s týmto rozhodnutím?*

## Analýza možností
*Ak je to relevantné, zahrňte alebo odkážte na akúkoľvek analýzu kompromisov, ktorá bola vykonaná na dosiahnutie rozhodnutia prijatého v tomto dokumente.*

### Legenda
*Voliteľné: Poskytnite zainteresovaným stranám vizuálne pomôcky, ktoré môžu pomôcť rýchlo odhaliť pozitívne a negatívne kompromisy - napríklad jednoduché zvýraznenie semaforom s pozitívnymi alebo negatívnymi predponami.*

<span style="background-color:#4bce97; color:black;">Zelené</span> pozadie označuje dobrú zhodu, zhoršujúcu sa cez <span style="background-color:#f1c232; color:black;">jantárové</span>, pričom <span style="background-color:#e06666; color:black;">červené</span> je najhoršia zhoda. \
\+ označuje komentár s pozitívnym vplyvom \
\- označuje komentár s negatívnym vplyvom

### Prehľad na vysokej úrovni
*Ako dobre sa každá možnosť na prvý pohľad hodí do kontextu problému?*

<table>
  <thead>
    <tr>
      <th>Zhrnutie</th>
      <th>Možnosť 1</th>
      <th>Možnosť 2</th>
      <th>Možnosť 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Jednoduchosť implementácie</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Veľmi jednoduché
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Zložité
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Rozsiahla implementácia vyžadujúca odborné znalosti
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Časový rámec</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Veľmi rýchle
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Pomerne pomalé
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Veľmi pomalé
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Strategická hodnota</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Žiadna strategická hodnota, čisto taktické
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Mierne zlepšuje zážitok z uvedenia zákazníkov
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ideálne pre nadchádzajúce zlúčenie
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Funkčné požiadavky
*Ako dobre sa každá potenciálna možnosť hodí k požadovaným funkčným požiadavkám?*

<table>
  <thead>
    <tr>
      <th>Scenár</th>
      <th><i>Možnosť 1</i></th>
      <th><i>Možnosť 2</i></th>
      <th><i>Možnosť 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Scenár 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scenár 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scenár 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Voliteľné: Pridajte riadky / ďalšiu tabuľku na pokrytie známych budúcich scenárov.*

### Nefunkčné požiadavky
*Ako dobre sa každá potenciálna možnosť hodí k požadovaným architektonickým charakteristikám?
Poznámka: „Architektonické charakteristiky“ by bol vhodnejší názov, ale prispôsobte ho jazyku, ktorý je známy vo vašej obchodnej doméne.*

<table>
  <thead>
    <tr>
      <th>Architektonická </br> charakteristika</th>
      <th><i>Možnosť 1</i></th>
      <th><i>Možnosť 2</i></th>
      <th><i>Možnosť 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Škálovateľnosť</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Výkon</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Dostupnosť</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Voliteľné: Pridajte alebo odkážte na definície architektonických charakteristík, pokiaľ sa týkajú vášho podnikania / produktu.*