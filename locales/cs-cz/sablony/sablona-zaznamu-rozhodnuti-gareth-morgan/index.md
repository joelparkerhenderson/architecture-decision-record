# [000] Název
*Přidělte každému ADR číslo pro snadný odkaz a katalogizaci* \
*POZNÁMKA: Veškerý text psaný kurzívou poskytuje nápovědu a v produkční verzi by měl být odstraněn*

## Stav - KONCEPT (DRAFT) / AKTIVNÍ (ACTIVE) / ZASTARALÉ (DEPRECATED) podle [000] / NAHRAZUJE (SUPERSEDES) [000]

## Kontext
*Stručně popište problém(y), které má toto ADR řešit, a proč tyto problémy existují.*

## Zvolený přístup
*Podrobně popište architektonicky významné rozhodnutí, které bylo / bude učiněno, a popište, jak řeší problémy uvedené v sekci Kontext.*

## Důsledky
*Jaký dopad má toto rozhodnutí na architektonické charakteristiky a funkční požadavky systému?*

## Správa a řízení
*Jak budou sledovány výsledky tohoto rozhodnutí?* \
*Jak bude zajištěn soulad s tímto rozhodnutím?*

## Analýza možností
*Pokud je to relevantní, zahrňte nebo odkažte na jakoukoli analýzu kompromisů, která byla provedena, aby se dospělo k rozhodnutí učiněnému v tomto dokumentu.*

### Legenda
*Volitelné: Poskytněte zainteresovaným stranám vizuální pomůcky, které jim mohou pomoci rychle odhalit pozitivní a negativní kompromisy – například jednoduché zvýraznění ve stylu semaforu s kladnými nebo zápornými předponami.*

<span style="background-color:#4bce97; color:black;">Zelené</span> pozadí označuje dobré přizpůsobení, zhoršující se přes <span style="background-color:#f1c232; color:black;">jantarové</span>, přičemž <span style="background-color:#e06666; color:black;">červené</span> je nejhorší přizpůsobení. \
\+ označuje komentář s pozitivním dopadem \
\- označuje komentář s negativním dopadem

### Přehled na vysoké úrovni
*Jak dobře každá možnost na první pohled odpovídá kontextu problému?*

<table>
  <thead>
    <tr>
      <th>Shrnutí</th>
      <th>Možnost 1</th>
      <th>Možnost 2</th>
      <th>Možnost 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Snadnost implementace</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Velmi snadné
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Záludné
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Rozsáhlá implementace vyžadující odborné znalosti
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Časové rámce</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Velmi rychlé
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Poměrně pomalé
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Velmi pomalé
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Strategická hodnota</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Žádná strategická hodnota, čistě taktické
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Mírně zlepšuje zkušenost se zaváděním zákazníků
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ideální pro nadcházející fúzi
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Funkční požadavky
*Jak dobře každá potenciální možnost odpovídá požadovaným funkčním požadavkům?*

<table>
  <thead>
    <tr>
      <th>Scénář</th>
      <th><i>Možnost 1</i></th>
      <th><i>Možnost 2</i></th>
      <th><i>Možnost 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Scénář 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scénář 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scénář 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Volitelné: Přidejte řádky / další tabulku pro pokrytí známých budoucích scénářů.*

### Nefunkční požadavky
*Jak dobře každá potenciální možnost odpovídá požadovaným architektonickým charakteristikám?
Poznámka: „Architektonické charakteristiky“ by byl vhodnější název, ale přizpůsobte jej jazyku známému ve vaší obchodní doméně.*

<table>
  <thead>
    <tr>
      <th>Architektonická </br> charakteristika</th>
      <th><i>Možnost 1</i></th>
      <th><i>Možnost 2</i></th>
      <th><i>Možnost 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Škálovatelnost</i></td>
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
      <td><i>Dostupnost</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Volitelné: Přidejte nebo odkažte na definice architektonických charakteristik, jak se týkají vašeho podnikání / produktu.*
