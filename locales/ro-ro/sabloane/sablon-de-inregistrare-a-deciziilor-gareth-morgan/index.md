# [000] Titlu
*Alocă fiecărui ADR un număr pentru referință și catalogare ușoare* \
*NOTĂ: Tot textul scris cu cursive oferă indicii și trebuie eliminat în versiunea de producție*

## Stare - CIORNĂ (DRAFT) / ACTIV (ACTIVE) / DEPĂȘIT (DEPRECATED) de [000] / ÎNLOCUIEȘTE (SUPERSEDES) [000]

## Context
*Descrie pe scurt problema (problemele) pe care acest ADR intenționează să le abordeze și de ce există aceste probleme.*

## Abordarea decisă
*Detaliază decizia semnificativă din punct de vedere arhitectural care a fost / va fi luată și descrie modul în care abordează problemele prezentate în secțiunea Context.*

## Consecințe
*Care este impactul acestei decizii asupra caracteristicilor de arhitectură și asupra cerințelor funcționale ale sistemului?*

## Guvernanță
*Cum vor fi monitorizate rezultatele acestei decizii?* \
*Cum va fi asigurată conformitatea cu această decizie?*

## Analiza opțiunilor
*Dacă este cazul, include sau trimite la orice analiză de compromisuri care a fost efectuată pentru a ajunge la decizia luată în acest document.*

### Legendă
*Opțional: Oferă părților interesate ajutoare vizuale care îi pot ajuta să observe rapid compromisurile pozitive și negative - de exemplu simple evidențieri de tip semafor cu prefixe pozitive sau negative.*

Un fundal <span style="background-color:#4bce97; color:black;">verde</span> indică o potrivire bună, înrăutățindu-se prin <span style="background-color:#f1c232; color:black;">chihlimbariu</span>, <span style="background-color:#e06666; color:black;">roșu</span> fiind cea mai slabă potrivire. \
\+ indică un comentariu cu impact pozitiv \
\- indică un comentariu cu impact negativ

### Prezentare generală
*Cât de bine se potrivește fiecare opțiune cu contextul problemei, dintr-o privire?*

<table>
  <thead>
    <tr>
      <th>Rezumat</th>
      <th>Opțiunea 1</th>
      <th>Opțiunea 2</th>
      <th>Opțiunea 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Ușurința implementării</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Foarte ușor
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Dificil
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Implementare amplă care necesită cunoștințe de specialitate
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Termene</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Foarte rapid
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Destul de lent
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Foarte lent
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Valoare strategică</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Fără valoare strategică, pur tactic
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Îmbunătățește ușor experiența de integrare a clienților
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ideal pentru fuziunea viitoare
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Cerințe funcționale
*Cât de bine se potrivește fiecare opțiune potențială cu cerințele funcționale dorite?*

<table>
  <thead>
    <tr>
      <th>Scenariu</th>
      <th><i>Opțiunea 1</i></th>
      <th><i>Opțiunea 2</i></th>
      <th><i>Opțiunea 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Scenariul 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scenariul 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scenariul 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Opțional: Adaugă rânduri / un alt tabel pentru a acoperi scenarii viitoare cunoscute.*

### Cerințe non-funcționale
*Cât de bine se potrivește fiecare opțiune potențială cu caracteristicile de arhitectură dorite?
Notă: „Caracteristicile arhitecturii” ar fi un titlu mai potrivit, dar adaptează-l la limbajul familiar domeniului tău de business.*

<table>
  <thead>
    <tr>
      <th>Caracteristica </br> arhitecturii</th>
      <th><i>Opțiunea 1</i></th>
      <th><i>Opțiunea 2</i></th>
      <th><i>Opțiunea 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Scalabilitate</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Performanță</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Disponibilitate</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Opțional: Adaugă sau trimite la definițiile caracteristicilor de arhitectură în raport cu afacerea / produsul tău.*
