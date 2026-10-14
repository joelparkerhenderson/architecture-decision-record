# Rejestr decyzji architektonicznych: framework aplikacji internetowych, z gotowym zestawem, full stack, dla produktu startupu

<!-- 

ChatGPT prompt

Long software architecture decision record 
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports. 

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Cel główny:**  
Zbudowanie aplikacji internetowej, w której płacący klienci mogą się logować, przesyłać pliki, przetwarzać dane i przeglądać raporty, ze szczególnym uwzględnieniem zwinnego rozwoju, funkcjonalności full stack i silnej zgodności z narzędziami AI/ML, zwłaszcza notebookami Project Jupyter.

### Kontekst i wymagania:

1. **Zwinny rozwój (wysoki priorytet)**: Jako startup potrzebujemy szybkiej iteracji i elastyczności. Praktyki zwinne, takie jak szybkie prototypowanie, rozwój iteracyjny i zdolność dostosowywania się do zmian, są kluczowe dla naszego cyklu rozwoju.

2. **Framework full stack (wysoki priorytet)**: Chcemy zminimalizować narzut, wybierając framework, który efektywnie obsłuży zarówno back-end, jak i front-end, zmniejszając potrzebę osobnych frameworków front-endu.

3. **Zgodność z narzędziami AI/ML (wysoki priorytet)**: Niezbędna jest możliwość łatwej integracji z narzędziami do analizy danych, takimi jak notebooki Jupyter, oraz z ekosystemem data science w Pythonie (NumPy, Pandas, TensorFlow itd.). Ułatwi to efektywne przetwarzanie danych i raportowanie.

4. **Kryteria o niskim znaczeniu**:
   - **Szybkość działania**: Choć wydajność jest istotna, nie jest najważniejszym czynnikiem na starcie, ponieważ bardziej zależy nam na szybkości rozwoju i kompletności funkcji.
   - **Skalowalność**: Przewidujemy wzrost, ale kwestie skalowalności można rozwiązać później i nie jest to obecnie główne wymaganie.
   - **Zgodność wsteczna**: Skupiamy się na obecnych technologiach i nie zależy nam mocno na zgodności wstecznej z systemami starszego typu.

### Oceniane frameworki:

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Przegląd**:  
Django to wysokopoziomowy framework internetowy dla Pythona, który sprzyja szybkiemu rozwojowi i czystemu, pragmatycznemu projektowi. Jest znany z filozofii „batteries included”, co oznacza, że od razu zawiera wiele funkcji, takich jak uwierzytelnianie, routing, ORM i obsługa formularzy.

**Mocne strony**:  
- **Full stack**: Django to kompleksowy framework full stack, który z zintegrowanymi funkcjami (np. silnik szablonów, interfejs administracyjny) obsłuży potrzeby zarówno back-endu, jak i front-endu.
- **Zwinny rozwój**: Dobrze zdefiniowana struktura i konwencje Django umożliwiają szybki rozwój i zdolność dostosowywania się, kluczowe w środowisku startupu. Framework ma doskonałą dokumentację i bogaty ekosystem pakietów firm trzecich, co przyspiesza rozwój.
- **Integracja z AI/ML**: Ekosystem Pythona jest niezrównany w data science i uczeniu maszynowym. Django, oparte na Pythonie, integruje się bezproblemowo z narzędziami takimi jak notebooki Jupyter, Pandas, NumPy, TensorFlow i scikit-learn.
- **Społeczność i ekosystem**: Django ma rozległą społeczność, solidną dokumentację i szeroką gamę wtyczek i rozszerzeń, co znacznie przyspiesza rozwój i rozwiązywanie problemów.
  
**Słabe strony**:  
- **Szybkość działania**: Python bywa wolniejszy w porównaniu z językami takimi jak Rust czy Elixir. Jednak w tym przypadku, gdzie wydajność nie jest główną kwestią, może to nie być przeszkodą.
- **Skalowalność**: Choć Django jest wysoce skalowalne, przy bardzo dużej skali mogą pojawić się wyzwania bez starannej optymalizacji (np. przy obsłudze dużej liczby współbieżnych żądań). Django można jednak nadal skutecznie skalować technikami równoważenia obciążenia i buforowania.

**Werdykt**:  
Django dobrze spełnia wymagania dotyczące zwinnego rozwoju, wsparcia full stack i zgodności z AI/ML. Integracja z Pythonem zapewnia bezproblemowy dostęp do narzędzi i bibliotek data science niezbędnych dla aplikacji.

---

### 2. **Ruby on Rails (Ruby)**

**Przegląd**:  
Ruby on Rails (RoR) to dojrzały framework aplikacji internetowych full stack, znany z podejścia „konwencja zamiast konfiguracji”, które ułatwia szybki rozwój.

**Mocne strony**:  
- **Full stack**: RoR ma wbudowane narzędzia zarówno do rozwoju back-endu, jak i front-endu (np. widoki, szablony, scaffolding), a bogata biblioteka gemów pozwala szybko wdrażać różne funkcje.
- **Zwinny rozwój**: Ruby on Rails jest szczególnie znany z szybkich cykli iteracji, co jest zaletą dla startupów chcących szybko iterować funkcje. RoR wspiera programowanie sterowane testami (TDD) i ma ugruntowany ekosystem dla zwinnych przepływów pracy.
- **Społeczność i ekosystem**: RoR ma dobrze ugruntowaną, silną społeczność i szeroką gamę gemów, które mogą przyspieszyć rozwój.
- **Łatwość użycia**: Rails ma bardzo przyjazną dla programistów składnię i jest znany z tego, że zadania takie jak migracje bazy danych, architektura model-widok-kontroler (MVC) i obsługa tras są szybkie i proste.

**Słabe strony**:  
- **Wydajność**: Ruby ma zwykle wolniejszą wydajność w czasie wykonania niż Python czy Elixir. Choć RoR może się skalować przy odpowiedniej infrastrukturze, wydajność Ruby może stać się wąskim gardłem w aplikacjach wymagających intensywnego przetwarzania w czasie rzeczywistym lub dużego ruchu współbieżnego.
- **Integracja z AI/ML**: Choć Ruby ma pewne biblioteki uczenia maszynowego, nie jest tak szeroko przyjęty w społeczności AI/ML jak Python. Integracja z narzędziami takimi jak notebooki Jupyter nie jest tak płynna, co czyni Pythona mocniejszym wyborem dla aplikacji intensywnie korzystających z danych.
  
**Werdykt**:  
Choć Ruby on Rails doskonale sprawdza się w zwinnym rozwoju i szybkim prototypowaniu, ustępuje pod względem zgodności z AI/ML Pythonowi (Django). To realny wybór dla startupów, które przedkładają szybką iterację nad głęboką integrację analizy danych.

---

### 3. **Phoenix (Elixir)**

**Przegląd**:  
Phoenix to framework internetowy zbudowany w Elixirze, funkcyjnym języku programowania zaprojektowanym z myślą o skalowalności i współbieżności. Phoenix wykorzystuje maszynę wirtualną Erlanga, znaną z obsługi ogromnej współbieżności i systemów odpornych na awarie.

**Mocne strony**:  
- **Skalowalność i wydajność**: Phoenix błyszczy w skalowalności i obsłudze wysokiej współbieżności. Jest zbudowany na maszynie wirtualnej Erlanga, która może obsługiwać tysiące (a nawet miliony) współbieżnych połączeń, co czyni go silnym kandydatem dla aplikacji wymagających przetwarzania danych w czasie rzeczywistym lub dużego ruchu.
- **Full stack**: Phoenix zawiera wszystko, czego potrzeba do zbudowania zarówno back-endu, jak i front-endu aplikacji. Obsługuje widoki na żywo (live views) do interaktywnych aktualizacji UI i zawiera silnik szablonów.
- **Zwinny rozwój**: Phoenix jest wysoce modułowy, co pozwala na szybką iterację funkcji. Dobrze nadaje się dla startupów, które muszą działać szybko.
- **Zgodność z AI/ML**: Choć Elixir ma wschodzące biblioteki uczenia maszynowego, nie jest tak szeroko wspierany w zadaniach AI/ML jak Python. Integracja z narzędziami takimi jak notebooki Jupyter wymagałaby obejść, ponieważ ekosystem Elixira dla data science nie jest tak dojrzały jak Pythona.

**Słabe strony**:  
- **Ekosystem AI/ML**: Elixir nie jest głównym językiem używanym w data science ani uczeniu maszynowym, a jego ekosystem nie jest tak dojrzały jak Pythona. Dlatego integracja z narzędziami takimi jak notebooki Jupyter lub popularne biblioteki AI (TensorFlow, PyTorch) będzie kłopotliwa.
- **Krzywa uczenia się**: Jeśli zespół nie zna programowania funkcyjnego i Elixira, krzywa uczenia się może być bardziej stroma.

**Werdykt**:  
Phoenix to doskonały wybór, jeśli główną kwestią jest skalowalność i współbieżność. Jednak biorąc pod uwagę priorytet zgodności z AI/ML, Phoenix może nie być najlepszym dopasowaniem ze względu na ograniczony ekosystem Elixira w tej dziedzinie.

---

### 4. **Loco (Rust)**

**Przegląd**:  
Loco to framework internetowy zbudowany w Ruście, systemowym języku programowania znanym z wydajności, bezpieczeństwa pamięci i współbieżności. Rust jest coraz popularniejszy w budowaniu aplikacji o wysokiej wydajności.

**Mocne strony**:  
- **Wydajność**: Główną siłą Rusta jest wysoka wydajność i bezpieczeństwo pamięci, co czyni go doskonałym wyborem dla aplikacji wymagających kontroli niskiego poziomu lub niezwykle wysokiej wydajności.
- **Współbieżność**: System własności Rusta zapewnia bezpieczeństwo pamięci, a jednocześnie umożliwia bezpieczne programowanie współbieżne, co czyni go idealnym dla systemów, które muszą skalować się efektywnie i obsługiwać równoległość.

**Słabe strony**:  
- **Rozwój full stack**: Loco, choć obiecujące, nie jest tak dojrzałe jak inne frameworki pod względem zapewnienia kompletnego rozwiązania full stack. Lepiej nadaje się do rozwoju back-endu, a ekosystem front-endu wokół Rusta dopiero się kształtuje.
- **Zwinny rozwój**: Tworzenie w Ruście może być wolniejsze niż w językach wyższego poziomu, takich jak Python czy Ruby, ze względu na jego niższy poziom i bardziej stromą krzywą uczenia się.
- **Ekosystem AI/ML**: Rust nie ma tak rozległego ekosystemu AI/ML jak Python. Choć powstają biblioteki Rusta do obliczeń numerycznych, są znacznie mniej dojrzałe niż oferta Pythona, taka jak notebooki Jupyter czy frameworki uczenia maszynowego.
  
**Werdykt**:  
Choć Rust i jego framework Loco oferują wyjątkową wydajność, brak wsparcia full stack, korzyści zwinnego rozwoju i ekosystemu AI/ML czyni go mniej idealnym dla tego konkretnego przypadku. Lepiej nadaje się do aplikacji krytycznych pod względem wydajności niż do szybkiego tworzenia aplikacji internetowych ze zintegrowanymi narzędziami data science.

---

### Podsumowanie

Po ocenie opcji pod kątem wymagań projektu **Django (Python)** jest najodpowiedniejszym wyborem. Oferuje następujące zalety:

- **Możliwości full stack**: Django to framework full stack, który integruje rozwój back-endu i front-endu.
- **Zwinny rozwój**: Framework dobrze nadaje się do szybkiego prototypowania i iteracji, co jest niezbędne w środowisku startupu.
- **Zgodność z AI/ML**: Python jest wiodącym językiem w AI/ML, a zgodność Django z bibliotekami takimi jak notebooki Jupyter zapewnia płynną integrację na potrzeby analizy i przetwarzania danych.
- **Społeczność i ekosystem**: Silne wsparcie społeczności Django i rozległy ekosystem bibliotek dostarczają wielu narzędzi przyspieszających rozwój.

Choć **Ruby on Rails** jest również silnym kandydatem do zwinnego rozwoju, jego ograniczone wsparcie AI/ML czyni go mniej idealnym dla tego konkretnego przypadku. **Phoenix (Elixir)** i **Loco (Rust)**, choć doskonałe pod względem skalowalności i wydajności, ustępują w integracji z AI/ML i rozwoju full stack. Dlatego Django jest zalecanym frameworkiem dla tego projektu.