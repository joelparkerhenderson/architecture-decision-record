# Rejestr decyzji architektonicznych: język programowania Rust

Numer decyzji: AR-001

Tytuł decyzji: Przyjęcie języka programowania Rust

Data: 1 grudnia 2021

Status: Zaakceptowany

### Opis problemu

W miarę rozwijania aplikacji zauważamy, że coraz trudniej łagodzić potencjalne luki w zabezpieczeniach i zapobiegać błędom w czasie wykonania. W istniejących językach programowania, takich jak C i C++, wciąż mamy problemy takie jak przepełnienia bufora, wycieki pamięci i niezdefiniowane zachowanie prowadzące do awarii aplikacji. Potrzebujemy języka programowania, który zapewnia gwarancje bezpieczeństwa pamięci i jest wystarczająco wydajny, by wspierać aplikacje krytyczne pod względem wydajności.

### Rozważania

Kilka języków programowania zaprojektowano, by rozwiązywać istniejące problemy. Wśród nich język programowania Rust zyskał znaczną uwagę społeczności programistów dzięki swoim unikalnym cechom projektowym. Rozważania obejmują:

1. Bezpieczeństwo pamięci i ochrona

2. Wydajność i efektywność

3. Wsparcie społeczności i przyjęcie

4. Krzywa uczenia się

5. Narzędzia i ekosystem

6. Zgodność z istniejącymi systemami oprogramowania.

### Ograniczenia

Przyjęcie nowego języka programowania wymaga przeszkolenia programistów, co zajmuje czas i zasoby. Zintegrowanie języka z istniejącym przepływem pracy może być wyzwaniem. Musimy zapewnić zgodność z istniejącymi systemami i unikać zmian łamiących zgodność, aby zachować ciągłość.

### Wdrożenie

1. Nasz zespół programistyczny przejdzie szkolenie, aby poznać język programowania Rust i się z nim zaznajomić.

2. Utworzymy nowy projekt w Ruście na próbę, aby ocenić jego zgodność i przydatność do naszych celów rozwojowych.

3. Będziemy stopniowo migrować istniejące systemy napisane w C i C++ do Rusta.

4. Będziemy współpracować ze społecznością Rusta, aby poznać dostępne narzędzia i biblioteki, które mogą usprawnić nasz przepływ pracy.

5. Będziemy regularnie monitorować wydajność Rusta i porównywać ją z wydajnością istniejących języków programowania.

6. Przyjmiemy podejście długoterminowe, które równoważy koszty szkolenia, integracji i potencjalne korzyści z używania Rusta.

### Uzasadnienie

Przyjęliśmy Rusta ze względu na jego unikalne cechy, zaprojektowane tak, by zapewniać gwarancje bezpieczeństwa pamięci i ochrony przy zachowaniu wydajności i efektywności. Solidny system typów Rusta, borrow checker i koncepcje bezpieczeństwa pamięci czynią go bardzo odpowiednim do tworzenia aplikacji krytycznych pod względem wydajności i bezpieczeństwa. Ponadto Rust ma znaczną społeczność programistów, co daje nam dostęp do szerokiej gamy narzędzi, bibliotek i ekosystemu wspierającego nasz przepływ pracy. Choć Rust wiąże się z krzywą uczenia się, wierzymy, że korzyści z jego przyjęcia przewyższają koszty i dają doskonałą okazję do dalszego rozwoju i innowacji.

### Konsekwencje

1. Przyjęcie Rusta będzie wymagało znacznej inwestycji czasu i zasobów w szkolenie programistów i integrację języka z istniejącym przepływem pracy.

2. Przyjęcie Rusta może powodować pewne problemy ze zgodnością z istniejącymi systemami, wymagające refaktoryzacji i modyfikacji.

3. Przyjęcie Rusta może zwiększyć liczbę programistów, którzy mogą wnosić wkład w nasz projekt, przyciągając programistów Rusta, którzy chcą pracować nad ciekawymi projektami.

4. Przyjęcie może prowadzić do poprawy wydajności, efektywności i bezpieczeństwa w porównaniu z istniejącymi językami.

5. Wreszcie przyjęcie Rusta niesie potencjalną korzyść w postaci zmniejszenia liczby luk w zabezpieczeniach w naszych aplikacjach.
   
<h6>Źródło: ta strona została wygenerowana przez ChatGPT, a następnie zredagowana pod kątem jasności i formatu.</h6>