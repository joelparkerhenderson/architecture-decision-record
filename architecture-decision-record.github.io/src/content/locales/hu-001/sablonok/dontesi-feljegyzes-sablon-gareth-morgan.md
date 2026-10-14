# [000] Cím
*Rendeljen minden ADR-hez egy számot a könnyű hivatkozás és katalogizálás érdekében* \
*MEGJEGYZÉS: Minden dőlt szöveg tippeket ad, és az éles változatból el kell távolítani*

## Állapot - VÁZLAT (DRAFT) / AKTÍV (ACTIVE) / ELAVULT (DEPRECATED) a [000] által / LEVÁLTJA (SUPERSEDES) a [000]-t

## Háttér
*Röviden írja le azt a problémát (problémákat), amelyet ez az ADR kezelni szándékozik, és hogy miért állnak fenn a problémák.*

## Elfogadott megközelítés
*Részletezze az architekturálisan jelentős döntést, amelyet meghoztak / meg fognak hozni, és írja le, hogyan kezeli a Háttér szakaszban vázolt problémákat.*

## Következmények
*Mi a döntés hatása a rendszer architekturális jellemzőire és funkcionális követelményeire?*

## Irányítás
*Hogyan fogják nyomon követni e döntés eredményeit?* \
*Hogyan biztosítják az e döntésnek való megfelelést?*

## Lehetőségek elemzése
*Ha alkalmazható, foglalja bele vagy hivatkozza azt a kompromisszum-elemzést, amelyet az ebben a dokumentumban hozott döntéshez végeztek.*

### Jelmagyarázat
*Nem kötelező: Adjon az érdekelt feleknek vizuális segédeszközöket, amelyek segítségével gyorsan észrevehetik a pozitív és negatív kompromisszumokat – például egyszerű közlekedési lámpa-szerű kiemeléseket pozitív vagy negatív előtagokkal.*

A <span style="background-color:#4bce97; color:black;">zöld</span> háttér jó illeszkedést jelez, amely a <span style="background-color:#f1c232; color:black;">borostyánsárgán</span> át romlik, a <span style="background-color:#e06666; color:black;">piros</span> a legrosszabb illeszkedés. \
\+ pozitív hatású megjegyzést jelez \
\- negatív hatású megjegyzést jelez

### Magas szintű áttekintés
*Mennyire illeszkedik az egyes lehetőség a probléma hátteréhez első ránézésre?*

<table>
  <thead>
    <tr>
      <th>Összefoglaló</th>
      <th>1. lehetőség</th>
      <th>2. lehetőség</th>
      <th>3. lehetőség</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Megvalósítás könnyűsége</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Nagyon egyszerű
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Trükkös
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Nagy, szakértelmet igénylő megvalósítás
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Határidők</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Nagyon gyors
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Meglehetősen lassú
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Nagyon lassú
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Stratégiai érték</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Nincs stratégiai érték, tisztán taktikai
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Kissé javítja az ügyfélbevezetési élményt
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ideális a közelgő egyesüléshez
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Funkcionális követelmények
*Mennyire illeszkedik az egyes lehetséges lehetőség a kívánt funkcionális követelményekhez?*

<table>
  <thead>
    <tr>
      <th>Forgatókönyv</th>
      <th><i>1. lehetőség</i></th>
      <th><i>2. lehetőség</i></th>
      <th><i>3. lehetőség</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>1. forgatókönyv</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>2. forgatókönyv</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>3. forgatókönyv</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Nem kötelező: Adjon hozzá sorokat / egy másik táblázatot az ismert jövőbeli forgatókönyvek lefedésére.*

### Nem funkcionális követelmények
*Mennyire illeszkedik az egyes lehetséges lehetőség a kívánt architekturális jellemzőkhöz?
Megjegyzés: Az „Architekturális jellemzők” megfelelőbb cím lenne, de igazítsa az üzleti területén ismert nyelvhez.*

<table>
  <thead>
    <tr>
      <th>Architekturális </br> jellemző</th>
      <th><i>1. lehetőség</i></th>
      <th><i>2. lehetőség</i></th>
      <th><i>3. lehetőség</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Skálázhatóság</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Teljesítmény</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Rendelkezésre állás</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Nem kötelező: Adja hozzá vagy hivatkozza az architekturális jellemzők definícióit, ahogyan azok az Ön üzletére / termékére vonatkoznak.*
