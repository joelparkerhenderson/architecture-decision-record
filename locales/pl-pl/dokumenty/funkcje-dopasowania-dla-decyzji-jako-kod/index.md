# Funkcje dopasowania dla decyzji jako kod

Funkcje dopasowania (ang. fitness functions) to obiektywne, zautomatyzowane kontrole, napisane w kodzie programu, które sprawdzają, czy decyzje są przestrzegane.

- Funkcje dopasowania sprawiają, że decyzje można testować i zapewniać.

- Funkcje dopasowania dla decyzji mogą znacznie pomóc w zapewnianiu jakości, procesach regulacyjnych i celach zarządzania (governance).

## Jak funkcje dopasowania łączą się z decyzjami

Rejestr decyzji dokumentuje decyzję, a funkcja dopasowania ją zapewnia.

- Przykładowa decyzja: Używamy event sourcingu ze względu na wymagania audytowe.

- Przykładowa funkcja dopasowania: Używamy serwera ciągłej integracji, aby testować, że każda zmiana stanu musi generować zdarzenia.

## Dlaczego funkcje dopasowania pomagają decyzjom

Obiektywne pomiary: Funkcje dopasowania kończą się powodzeniem albo niepowodzeniem, więc praca jest widoczna i jasna.

Ciągłe użycie: Funkcje dopasowania to Twoje żywe reguły, uruchamiane przy każdym commicie i buildzie.

Pewność przy refaktoryzacji: Funkcje dopasowania automatycznie wychwytują błędy w regułach decyzji.

Skalowalne zarządzanie: Funkcje dopasowania zapewniają standardy bez tworzenia wąskich gardeł.

## Czy funkcje dopasowania mogą korzystać z AI?

Funkcje dopasowania mogą wykorzystywać duże modele językowe (LLM) AI do oceny decyzji, zadając pytania o Twoją pracę,
na przykład plany, kod, schematy, API i inne:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Testy jednostkowe architektury

[ArchUnit](https://www.archunit.org/): sprawdza reguły architektury kodu Java za pomocą dowolnego zwykłego frameworka testów jednostkowych Java.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): sprawdza reguły architektury kodu TypeScript i JavaScript za pomocą Jest, Vitest, Jasmine itd.
