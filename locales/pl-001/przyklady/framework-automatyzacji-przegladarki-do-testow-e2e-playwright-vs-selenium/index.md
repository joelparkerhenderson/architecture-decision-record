## Rejestr decyzji architektonicznych: framework automatyzacji przeglądarki do testów E2E (Playwright vs Selenium)

### 1. **Kontekst**

Wybieramy framework automatyzacji przeglądarki do naszego potoku testów end-to-end (E2E). Ten framework będzie integralną częścią naszych procesów CI/CD i będzie uruchamiał testy symulujące rzeczywiste interakcje użytkowników z naszą platformą. W szczególności testy obejmą scenariusze takie jak rejestracja/logowanie użytkownika, przesyłanie plików, interakcje z pulpitami i pobieranie raportów.

Jako **startup** skupiamy się na **zwinnym rozwoju**, z potrzebą szybkiego iterowania i ewoluowania. Nasz zespół pracuje głównie z **TypeScript** i **Python**, a możliwość pisania testów w tych językach jest niezbędna. Ponadto platforma zawiera **interaktywne wykresy i pulpity**, więc kluczowe jest, aby narzędzie do automatyzacji dobrze obsługiwało bogate, dynamiczne interfejsy użytkownika.

Dwaj kandydaci do tego zadania to **Playwright** i **Selenium**, z których każdy ma swoje mocne strony i kompromisy. Musimy ocenić te frameworki na podstawie funkcji i wymagań opisanych poniżej.

### 2. **Rozważane opcje**

- **Playwright** (firmy Microsoft)
- **Selenium** (projektu Selenium)

### 3. **Czynniki decyzji**

Czynniki wpływające na naszą decyzję są następujące:

1. **Zwinny rozwój**: Wybrane narzędzie musi umożliwiać szybkie, elastyczne cykle rozwoju.
2. **Obsługa języków**: Nasz zespół wymaga obsługi zarówno **TypeScript**, jak i **Python**.
3. **Testowanie interaktywnego UI**: Niezbędna jest możliwość niezawodnego testowania interaktywnych wykresów, pulpitów i dynamicznych elementów.
4. **Szybkość działania**: Choć nie jest to główna kwestia, wydajność w potokach CI/CD ma znaczenie.
5. **Skalowalność**: Nie planujemy masowego skalowania w najbliższej przyszłości, ale chcemy mieć pewność, że rozwiązanie poradzi sobie z przyszłym wzrostem.
6. **Zgodność wsteczna**: Systemy starszego typu i zgodność ze starszymi przeglądarkami nie są obecnie krytyczne dla naszego projektu.
7. **Testowanie mobilne**: Choć nie jest to bezpośredni priorytet, framework powinien umożliwiać testowanie funkcji dostosowanych do urządzeń mobilnych lub być rozszerzalny na takie przypadki.
8. **Testowanie na wielu monitorach**: Obsługa konfiguracji z wieloma monitorami jest wymaganiem drugorzędnym, zwłaszcza gdyby kiedyś trzeba było testować bardziej złożone przepływy pracy użytkowników.
9. **Testowanie przesyłania plików**: Framework musi efektywnie obsługiwać przesyłanie plików, co jest podstawowym wymaganiem naszych testów.

### 4. **Kryteria oceny**

- **Łatwość użycia**: Jak łatwo pisać i utrzymywać testy?
- **Obsługa języków**: Czy framework obsługuje TypeScript i Python, dwa języki, których nasz zespół używa najczęściej?
- **Testowanie interaktywnego UI**: Jak dobrze framework radzi sobie ze złożonymi, interaktywnymi interfejsami użytkownika, takimi jak wykresy, przesyłanie plików i dane dynamiczne?
- **Integracja z CI/CD**: Jak dobrze framework integruje się z popularnymi narzędziami i usługami CI/CD?
- **Obsługa wielu przeglądarek**: Jakie przeglądarki są obsługiwane i jak dobrze działają?
- **Wydajność i szybkość**: Jak szybko działają testy, zwłaszcza w potoku CI/CD?
- **Skalowalność**: Jak dobrze framework skaluje się, gdy dodajemy więcej testów lub bardziej złożone scenariusze?
- **Społeczność i ekosystem**: Jak aktywna jest społeczność frameworka? Czy dostępnych jest wiele integracji i rozszerzeń?

### 5. **Rozważania**

#### 5.1 **Playwright**

##### **Zalety**:
1. **Sprytniejsze API do przesyłania plików lokalnych**: API Playwright do pracy z plikami lokalnymi i przesyłania plików jest prostsze i bardziej intuicyjne. Ułatwiłoby to wdrożenie i utrzymanie testów przesyłania plików.
2. **Składnia i generowanie kodu**: Playwright ma krótszą, bardziej zwięzłą składnię. Skutkuje to mniejszą ilością kodu szablonowego, co poprawia utrzymywalność i efektywność programistów. Ponadto ta krótsza składnia poprawia jakość kodu generowanego przez OpenAI, co ułatwia automatyczne generowanie skryptów testowych.
3. **Testowanie interaktywnego UI**: Playwright doskonale testuje dynamiczne, interaktywne aplikacje internetowe, takie jak te z bogatymi wykresami, złożonymi interakcjami użytkownika i aktualizacjami w czasie rzeczywistym. Bardzo skutecznie obsługuje WebSockets, WebRTC, shadow DOM i inne nowoczesne technologie internetowe.
4. **Obsługa wielu przeglądarek**: Playwright obsługuje **Chromium**, **WebKit** i **Firefox**. Działa spójnie w tych przeglądarkach, co powinno pokryć większość naszych potrzeb testowych.
5. **Integracja z CI/CD**: Playwright integruje się bezproblemowo z nowoczesnymi platformami CI/CD (GitHub Actions, Jenkins itd.). Może uruchamiać testy równolegle w różnych przeglądarkach, optymalizując czas uruchomienia testów i nadając się do szybkiego rozwoju.
6. **Szybkość i niezawodność**: Playwright jest ogólnie szybszy niż Selenium, zwłaszcza w trybie headless, i bardziej odporny przy obsłudze asynchronicznych elementów stron.

##### **Wady**:
1. **Ograniczone testowanie mobilne**: Choć Playwright obsługuje emulację urządzeń mobilnych w przeglądarkach, brakuje mu natywnych możliwości testowania mobilnego, takich jak integracja Selenium z Appium do prawdziwego testowania mobilnego.
2. **Mniejszy ekosystem**: Playwright jest nadal nowszy i mniej ugruntowany niż Selenium. Choć ma szybko rosnącą społeczność i dobrą dokumentację, może jeszcze nie mieć tak ogromnego ekosystemu wtyczek i integracji jak Selenium.
3. **Ograniczona obsługa przeglądarek**: Choć Playwright obejmuje główne nowoczesne przeglądarki (Chrome, Safari, Firefox), jego obsługa starszych przeglądarek (np. Internet Explorer) nie jest tak solidna jak w Selenium.

#### 5.2 **Selenium**

##### **Zalety**:
1. **Dłuższa historia i dojrzałość**: Selenium istnieje od dawna i ma sprawdzone osiągnięcia. Jest szeroko stosowany w wielu zespołach i branżach, co doprowadziło do powstania ogromnego ekosystemu wtyczek, integracji i zasobów.
2. **Obsługa wielu przeglądarek i platform**: Selenium obsługuje **szeroką gamę przeglądarek** i wersji, w tym **Internet Explorer**, i może być też zintegrowany z różnymi narzędziami, takimi jak **Docker**, **Selenium Grid** i **usługi chmurowe** do testowania rozproszonego.
3. **Testowanie mobilne**: Selenium, dzięki integracji z **Appium**, jest znacznie solidniejszy w testowaniu mobilnym, w tym aplikacji na Androida i iOS. Czyni go to lepszym wyborem dla projektów nastawionych na mobile lub w dużej mierze mobilnych.
4. **Testowanie na wielu monitorach**: Selenium zapewnia lepszą obsługę scenariuszy z **wieloma monitorami** lub złożonych interakcji z wieloma oknami.

##### **Wady**:
1. **Złożoność**: API Selenium jest bardziej rozwlekłe i jawne. Choć w niektórych przypadkach może to być zaletą, oznacza więcej kodu do napisania i utrzymania, co może zmniejszać zwinność programistów — co jest szczególnie ważne w środowisku startupu.
2. **Wydajność**: Selenium zwykle działa wolniej niż Playwright, zwłaszcza w trybie headless. Może to wpływać na potoki CI/CD, szczególnie wraz ze wzrostem liczby testów.
3. **Testowanie interaktywnego UI**: Selenium nie radzi sobie tak płynnie jak Playwright z testowaniem nowoczesnych, interaktywnych interfejsów internetowych, zwłaszcza z wykresami i aktualizacjami danych w czasie rzeczywistym. Wymaga więcej konfiguracji i obsługi, aby niezawodnie współpracować z treścią dynamiczną.

### 6. **Podsumowanie porównania**

| Cecha                            | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Łatwość użycia**                | Krótsza składnia, bardziej intuicyjny dla nowoczesnych UI | Bardziej jawny, wymaga więcej kodu szablonowego  |
| **Obsługa języków**               | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Testowanie interaktywnego UI**  | Doskonały dla dynamicznych UI czasu rzeczywistego | Obsługuje podstawowe UI, ale bardziej rozwlekły i złożony przy bogatych interakcjach |
| **Testowanie przesyłania plików** | Sprytniejsze API do przesyłania plików        | Bardziej rozwlekłe, mniej intuicyjne API         |
| **Integracja z CI/CD**            | Łatwa integracja z GitHub Actions, Jenkins    | Silna integracja z wieloma narzędziami CI    |
| **Testowanie mobilne**            | Ograniczone, tylko emulacja                   | Pełna obsługa przez Appium               |
| **Obsługa wielu przeglądarek**    | Chromium, WebKit, Firefox                     | Pełna obsługa głównych i starszych przeglądarek |
| **Wydajność**                     | Szybki, zoptymalizowany pod testy headless    | Wolniejszy, zwłaszcza w trybie headless       |
| **Testowanie na wielu monitorach**| Ograniczone                                   | Dobra obsługa konfiguracji z wieloma monitorami    |
| **Społeczność i ekosystem**       | Rosnąca, dobra dokumentacja                   | Duża, dojrzała, rozległy ekosystem       |

### 7. **Decyzja**

Po rozważeniu wymagań i kompromisów **Playwright** jest lepszym wyborem dla naszych obecnych potrzeb. Jego sprytniejsze API do testowania przesyłania plików lokalnych, zwięzła składnia i silna obsługa testowania interaktywnego UI sprawiają, że idealnie pasuje do naszego zwinnego cyklu rozwoju. Fakt, że obsługuje zarówno **TypeScript**, jak i **Python**, jest krytyczny dla naszego zespołu, a nowoczesne podejście frameworka do testowania pozwoli nam pisać czysty, łatwy w utrzymaniu kod.

Choć **Selenium** pozostaje świetnym narzędziem, zwłaszcza do testowania mobilnego, obsługi starszych przeglądarek i konfiguracji z wieloma monitorami, jest mniej dopasowany do naszych obecnych potrzeb. Jego rozwlekłość, wolniejsze działanie i bardziej złożona obsługa dynamicznych UI, takich jak wykresy, czynią go mniej optymalnym w naszym przypadku.

### 8. **Konsekwencje**

- **Działanie natychmiastowe**: Przyjmiemy **Playwright** do naszych testów E2E, skupiając się na testowaniu przepływów użytkownika obejmujących rejestrację, logowanie, przesyłanie plików, pulpity i pobieranie raportów.
- **Kwestie długoterminowe**: Będziemy obserwować rozwój ekosystemu Playwright. Jeśli nasze potrzeby się zmienią, zwłaszcza w zakresie testowania mobilnego lub obsługi starszych przeglądarek, możemy wrócić do Selenium.
- **Szkolenia i dokumentacja**: Zespoły programistyczne będą musiały poznać API Playwright, zwłaszcza w zakresie obsługi dynamicznych UI i przesyłania plików.
- **Migracja**: Istniejące testy Selenium (jeśli są) będą stopniowo migrowane do Playwright.

### 9. **Kwestie na przyszłość**
