# [000] Naslov
*Svakom ADR-u dodijelite broj radi lakšeg referenciranja i katalogiziranja* \
*NAPOMENA: Sav kurzivni tekst daje savjete i treba ga ukloniti u produkcijskoj verziji*

## Status - NACRT / AKTIVNO /  ZASTARJELO zbog [000] / ZAMJENJUJE [000]

## Kontekst
*Ukratko opišite problem(e) koje ovaj ADR namjerava riješiti i zašto problemi postoje.*

## Odabrani pristup
*Detaljno opišite arhitekturno značajnu odluku koja je donesena / bit će donesena i opišite kako ona rješava probleme navedene u odjeljku Kontekst.*

## Posljedice
*Kakav je učinak ove odluke na arhitekturne karakteristike i funkcionalne zahtjeve sustava?*

## Upravljanje
*Kako će se pratiti ishodi ove odluke?* \
*Kako će se osigurati usklađenost s ovom odlukom?*

## Analiza opcija
*Ako je primjenjivo, uključite ili povežite sve analize kompromisa provedene kako bi se došlo do odluke donesene u ovom dokumentu.*

### Legenda
*Neobavezno: Pružite dionicima vizualna pomagala koja mogu pomoći u brzom uočavanju pozitivnih i negativnih kompromisa – na primjer, jednostavno isticanje u boji semafora s pozitivnim ili negativnim prefiksima.*

<span style="background-color:#4bce97; color:black;">Zelena</span> pozadina označava dobro podudaranje, koje se pogoršava preko <span style="background-color:#f1c232; color:black;">jantarne</span>, a <span style="background-color:#e06666; color:black;">crvena</span> je najlošije podudaranje. \
\+ označava komentar s pozitivnim učinkom \
\- označava komentar s negativnim učinkom

### Pregled na visokoj razini
*Koliko se svaka opcija na prvi pogled uklapa u kontekst problema?*

<table>
  <thead>
    <tr>
      <th>Sažetak</th>
      <th>Opcija 1</th>
      <th>Opcija 2</th>
      <th>Opcija 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Jednostavnost implementacije</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Vrlo jednostavno
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Zahtjevno
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Velika implementacija koja zahtijeva stručno znanje
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Vremenski okviri</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Vrlo brzo
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Prilično sporo
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Vrlo sporo
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Strateška vrijednost</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Nema strateške vrijednosti, čisto taktički
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Blago poboljšava iskustvo uvođenja klijenata
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Idealno za nadolazeće spajanje
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Funkcionalni zahtjevi
*Koliko se svaka potencijalna opcija uklapa u željene funkcionalne zahtjeve?*

<table>
  <thead>
    <tr>
      <th>Scenarij</th>
      <th><i>Opcija 1</i></th>
      <th><i>Opcija 2</i></th>
      <th><i>Opcija 3</i></th>
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

*Neobavezno: Dodajte retke / još jednu tablicu kako biste pokrili poznate buduće scenarije.*

### Nefunkcionalni zahtjevi
*Koliko se svaka potencijalna opcija uklapa u željene arhitekturne karakteristike?
Napomena: „Arhitekturne karakteristike“ bio bi prikladniji naslov, ali prilagodite ga jeziku poznatom u vašoj poslovnoj domeni.*

<table>
  <thead>
    <tr>
      <th>Arhitekturna </br> karakteristika</th>
      <th><i>Opcija 1</i></th>
      <th><i>Opcija 2</i></th>
      <th><i>Opcija 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Skalabilnost</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Performanse</i></td>
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

*Neobavezno: Dodajte ili povežite definicije arhitekturnih karakteristika kako se odnose na vaše poslovanje / proizvod.*