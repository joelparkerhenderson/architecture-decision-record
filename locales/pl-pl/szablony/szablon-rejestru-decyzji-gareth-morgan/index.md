# [000] Tytuł
*Nadaj każdemu ADR numer, aby łatwo się do niego odwoływać i go katalogować* \
*UWAGA: Cały tekst pisany kursywą to podpowiedzi i należy go usunąć w wersji produkcyjnej*

## Status - SZKIC (DRAFT) / AKTYWNY (ACTIVE) / WYCOFANY (DEPRECATED) przez [000] / ZASTĘPUJE (SUPERSEDES) [000]

## Kontekst
*Krótko opisz problem(y), które ten ADR ma rozwiązać, i dlaczego te problemy istnieją.*

## Przyjęte podejście
*Opisz szczegółowo decyzję istotną dla architektury, która została lub zostanie podjęta, i wyjaśnij, jak rozwiązuje problemy opisane w sekcji Kontekst.*

## Konsekwencje
*Jaki wpływ ma ta decyzja na charakterystyki architektury i wymagania funkcjonalne systemu?*

## Zarządzanie
*Jak będą monitorowane skutki tej decyzji?* \
*Jak zostanie zapewniona zgodność z tą decyzją?*

## Analiza opcji
*Jeśli ma zastosowanie, dołącz lub podaj odnośnik do analizy kompromisów, którą przeprowadzono, aby dojść do decyzji opisanej w tym dokumencie.*

### Legenda
*Opcjonalnie: Zapewnij interesariuszom pomoce wizualne, które pomagają szybko dostrzec pozytywne i negatywne kompromisy — na przykład proste podświetlenia w stylu świateł drogowych z przedrostkami pozytywnymi lub negatywnymi.*

<span style="background-color:#4bce97; color:black;">Zielone</span> tło oznacza dobre dopasowanie, pogarszające się przez <span style="background-color:#f1c232; color:black;">bursztynowe</span>, a <span style="background-color:#e06666; color:black;">czerwone</span> oznacza najgorsze dopasowanie. \
\+ oznacza komentarz o pozytywnym wpływie \
\- oznacza komentarz o negatywnym wpływie

### Przegląd ogólny
*Jak dobrze każda opcja pasuje do kontekstu problemu na pierwszy rzut oka?*

<table>
  <thead>
    <tr>
      <th>Podsumowanie</th>
      <th>Opcja 1</th>
      <th>Opcja 2</th>
      <th>Opcja 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Łatwość wdrożenia</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Bardzo łatwe
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Podchwytliwe
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Duże wdrożenie wymagające specjalistycznej wiedzy
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Terminy</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Bardzo szybko
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Dość wolno
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Bardzo wolno
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Wartość strategiczna</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Brak wartości strategicznej, czysto taktyczne
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Nieznacznie poprawia wdrażanie nowych klientów
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Idealne na potrzeby zbliżającej się fuzji
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Wymagania funkcjonalne
*Jak dobrze każda potencjalna opcja pasuje do oczekiwanych wymagań funkcjonalnych?*

<table>
  <thead>
    <tr>
      <th>Scenariusz</th>
      <th><i>Opcja 1</i></th>
      <th><i>Opcja 2</i></th>
      <th><i>Opcja 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Scenariusz 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scenariusz 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scenariusz 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Opcjonalnie: Dodaj wiersze / kolejną tabelę, aby objąć znane przyszłe scenariusze.*

### Wymagania niefunkcjonalne
*Jak dobrze każda potencjalna opcja pasuje do oczekiwanych charakterystyk architektury?
Uwaga: „Charakterystyki architektury” byłyby bardziej odpowiednim tytułem, ale dostosuj go do języka znanego w Twojej dziedzinie biznesowej.*

<table>
  <thead>
    <tr>
      <th>Charakterystyka </br> architektury</th>
      <th><i>Opcja 1</i></th>
      <th><i>Opcja 2</i></th>
      <th><i>Opcja 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Skalowalność</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Wydajność</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Dostępność</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Opcjonalnie: Dodaj lub podaj odnośnik do definicji charakterystyk architektury w odniesieniu do Twojej firmy / produktu.*
