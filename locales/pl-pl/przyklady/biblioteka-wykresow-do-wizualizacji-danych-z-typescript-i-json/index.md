# Rejestr decyzji architektonicznych: biblioteka wykresów do wizualizacji danych z TypeScript i JSON

<!--

ChatGPT prompt:

Long software architecture decision record 
chart library toolkit for data visualization using TypeScript and JSON

Evaluate Charts: Apache ECharts, Chart.js, ApexCharts, AG Charts, Highcharts, Carbon Charts, Layer Cake, D3.

Primary need: advanced interactive charts, especially for financial data, scientific data, and government data.

High importance: 1. Agile development because this is for a startup. 2. Doughnut Chart, Radar Chart, Clustering Process
Chart, Area Chart with Time Axis, Candlestick Chart, Nightingale Chart, Geo SVG Map. 3. Free open source.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Cel główny:**  
Wybór zaawansowanego zestawu narzędzi do wykresów, służącego do tworzenia interaktywnych wizualizacji, ze szczególnym uwzględnieniem danych finansowych, naukowych i rządowych, z użyciem TypeScript i JSON. Biblioteka powinna oferować solidne funkcje, elastyczność i być open source. 

### Kontekst i wymagania:

1. **Zwinny rozwój (wysoki priorytet)**: Jako startup potrzebujemy szybkiego iterowania, prototypowania i elastyczności w rozwoju. Biblioteka wykresów musi umożliwiać szybkie cykle rozwoju.
   
2. **Typy wykresów (wysoki priorytet)**:
   - **Wykres pierścieniowy**
   - **Wykres radarowy**
   - **Wykres procesu klasteryzacji**
   - **Wykres warstwowy z osią czasu**
   - **Wykres świecowy**
   - **Wykres Nightingale’a**
   - **Mapa geograficzna SVG**
   
   Te typy wykresów są szczególnie ważne do wizualizacji złożonych zbiorów danych, takich jak trendy finansowe, metryki naukowe i informacje geograficzne.

3. **Bezpłatna i open source (wysoki priorytet)**: Zestaw narzędzi powinien być open source, aby uniknąć kosztów licencji, zapewnić przejrzystość i elastyczność dostosowywania.

4. **Kryteria o niskim znaczeniu**:
   - **Szybkość działania**: Choć wydajność jest ważna, nie jest priorytetem w tej decyzji.
   - **Skalowalność**: Choć skalowalność jest ogólnie ważna, bezpośrednią potrzebą jest zbudowanie MVP, który może z czasem rosnąć. Kwestie skalowalności można rozwiązać później.
   - **Zgodność wsteczna**: Nie jest główną kwestią w początkowej budowie, o ile biblioteka jest nowoczesna i aktywnie utrzymywana.

### Oceniane biblioteki:

1. **Apache ECharts**
2. **Chart.js**
3. **ApexCharts**
4. **AG Charts**
5. **Highcharts**
6. **Carbon Charts**
7. **Layer Cake**
8. **D3.js**

---

### 1. **Apache ECharts**

**Przegląd**:  
Apache ECharts to potężna, elastyczna biblioteka wykresów do interaktywnych, konfigurowalnych wizualizacji. Obsługuje szeroką gamę wykresów i jest szczególnie mocna w złożonych, dynamicznych wizualizacjach.

**Mocne strony**:
- **Zaawansowana interaktywność**: ECharts doskonale zapewnia interaktywne wykresy, oferując funkcje takie jak powiększanie, przesuwanie i dynamiczne aktualizacje danych.
- **Pierścieniowy, radarowy, świecowy, mapy geograficzne SVG**: ECharts obsługuje wiele wymaganych typów wykresów, w tym wizualizacje pierścieniowe, radarowe, świecowe i mapy geograficzne.
- **Bezpłatna i open source**: ECharts to biblioteka open source, co pasuje do oszczędnego charakteru startupu i daje swobodę modyfikowania kodu.
- **Elastyczność i rozszerzalność**: Bardzo konfigurowalna, z rozbudowaną obsługą animacji, niestandardowych wizualizacji i zaawansowanych technik wykresów.
  
**Słabe strony**:
- **Krzywa uczenia się**: ECharts, choć potężna, może mieć bardziej stromą krzywą uczenia się ze względu na elastyczność i rozbudowane API.
- **Złożoność dokumentacji**: Dokumentacja jest obszerna, ale może przytłaczać programistów, którzy dopiero zaczynają z niej korzystać.

**Werdykt**:  
ECharts bardzo dobrze nadaje się do projektu dzięki obsłudze interaktywnych wykresów, w tym wszystkich wymaganych typów, takich jak wykresy świecowe, radarowe i mapy geograficzne. Jej charakter open source odpowiada potrzebie elastyczności i opłacalności w projekcie.

---

### 2. **Chart.js**

**Przegląd**:  
Chart.js to prosta, łatwa w użyciu biblioteka wykresów do budowania popularnych typów wykresów. Znana jest z prostoty i łatwej integracji.

**Mocne strony**:
- **Łatwość użycia**: Chart.js jest bardzo prosta w konfiguracji i użyciu, z minimalną krzywą uczenia się.
- **Open source**: Chart.js jest bezpłatna i open source, co jest kluczowe dla ograniczenia kosztów.
- **Popularne typy wykresów**: Obsługuje podstawowe wykresy, takie jak pierścieniowy, warstwowy, radarowy i liniowy, które pokrywają większość głównych potrzeb.

**Słabe strony**:
- **Ograniczone wykresy zaawansowane**: Chart.js nie obsługuje natywnie złożonych typów wykresów, takich jak wykresy świecowe, mapy geograficzne SVG czy wykresy procesu klasteryzacji. Choć te funkcje można dodać przez wtyczki lub dostosowanie, nie jest to tak proste jak w innych bibliotekach.
- **Interaktywność**: Choć Chart.js obsługuje podstawową interaktywność (np. etykiety narzędzi i efekty najechania), nie oferuje tak zaawansowanych funkcji jak ECharts czy D3.js.

**Werdykt**:  
Chart.js świetnie nadaje się do prostych, szybkich projektów, ale brak obsługi złożonych typów wykresów czyni ją nieodpowiednią dla aplikacji intensywnie korzystającej z danych, z zaawansowanymi potrzebami, takimi jak wykresy świecowe i mapy geograficzne. To dobry wybór do prototypowania, ale dla wymaganych typów wykresów zalecane są bardziej zaawansowane narzędzia.

---

### 3. **ApexCharts**

**Przegląd**:  
ApexCharts to nowoczesna biblioteka wykresów, która oferuje różne typy wykresów i skupia się na interaktywnych wizualizacjach z łatwym w użyciu API.

**Mocne strony**:
- **Funkcje interaktywne**: ApexCharts oferuje interaktywne wykresy z etykietami narzędzi, powiększaniem, przesuwaniem i aktualizacjami.
- **Obsługa wykresów finansowych i naukowych**: Obsługuje szeroką gamę typów wykresów, w tym wykresy świecowe, radarowe i warstwowe.
- **Łatwość użycia**: Ma proste API i łatwo ją zintegrować z projektem.
- **Bezpłatna i open source**: ApexCharts oferuje bezpłatną wersję open source, odpowiednią do wielu zastosowań.
  
**Słabe strony**:
- **Złożone dostosowywanie**: Choć oferuje wiele funkcji, opcje dostosowywania nie są tak elastyczne jak w ECharts czy D3.js w przypadku bardzo złożonych lub niestandardowych potrzeb wykresów.
- **Mapy geograficzne**: ApexCharts nie obsługuje natywnie map geograficznych ani wykresów procesu klasteryzacji, które są wymagane w tym projekcie.

**Werdykt**:  
ApexCharts to silny kandydat dzięki łatwości użycia i interaktywności, ale nie spełnia wymagań dla niektórych zaawansowanych typów wykresów, zwłaszcza map geograficznych i wykresów klasteryzacji. To dobra opcja dla prostszych wykresów, ale brakuje jej niektórych wymaganych funkcji.

---

### 4. **AG Charts**

**Przegląd**:  
AG Charts to biblioteka wykresów klasy komercyjnej, zaprojektowana z myślą o wydajności i precyzji. Bardzo dobrze nadaje się do tworzenia pulpitów finansowych, naukowych i biznesowych.

**Mocne strony**:
- **Zaawansowane typy wykresów**: AG Charts obsługuje wiele zaawansowanych typów wykresów, w tym świecowe, warstwowe, radarowe i inne. Oferuje też głęboką integrację z innymi produktami AG-Grid.
- **Wysoka wydajność**: Oferuje doskonałą wydajność, zwłaszcza przy dużych zbiorach danych.
- **Interaktywność**: AG Charts obsługuje różne funkcje interaktywne, takie jak powiększanie, etykiety narzędzi i dynamiczne aktualizacje.

**Słabe strony**:
- **Nie w pełni bezpłatna**: Choć AG Charts oferuje wersję bezpłatną, pełna wersja jest płatna, co może być barierą dla startupów chcących minimalizować koszty.
- **Złożoność**: Choć biblioteka jest bogata w funkcje, może być przesadą dla prostszych projektów i wymagać więcej konfiguracji niż inne opcje.

**Werdykt**:  
AG Charts jest potężna i bogata w funkcje, ale może nie być najlepszym wyborem ze względu na komercyjny charakter i strukturę kosztów. Jej przydatność zależy od tego, czy budżet pozwala na wersje płatne, czy preferowane są alternatywy open source.

---

### 5. **Highcharts**

**Przegląd**:  
Highcharts to popularna biblioteka wykresów, znana z szerokiej gamy typów wykresów i potężnych opcji dostosowywania.

**Mocne strony**:
- **Kompleksowe typy wykresów**: Highcharts obsługuje szeroką gamę wykresów, w tym świecowe, radarowe, warstwowe i mapy geograficzne.
- **Interaktywna i dynamiczna**: Highcharts oferuje bogate funkcje interaktywne, w tym drążenie w głąb (drill-down), powiększanie i przesuwanie.
- **Łatwość użycia**: Ma przyjazne API i dobrą dokumentację, co ułatwia start.

**Słabe strony**:
- **Licencja komercyjna**: Choć Highcharts oferuje wersję bezpłatną do użytku niekomercyjnego, licencja komercyjna jest droga, co może być istotną wadą dla startupów.
- **Krzywa uczenia się**: Choć nie tak stroma jak w ECharts, krzywa uczenia się Highcharts nadal może być wyzwaniem dla początkujących.

**Werdykt**:  
Highcharts to biblioteka bogata w funkcje, ale jej licencjonowanie komercyjne czyni ją mniej odpowiednią dla projektów open source wrażliwych na koszty. Kompleksowe opcje wykresów to plus, ale kwestia licencji ogranicza jej atrakcyjność w tym przypadku.

---

### 6. **Carbon Charts**

**Przegląd**:  
Carbon Charts to biblioteka wykresów opracowana przez IBM, zaprojektowana do tworzenia atrakcyjnych wizualnie i bardzo konfigurowalnych wykresów.

**Mocne strony**:
- **Konfigurowalność**: Carbon Charts pozwala na szerokie dostosowywanie wyglądu i zachowania wykresów.
- **Open source**: Jest bezpłatna i open source, co odpowiada wymaganiu projektu dotyczącemu rozwiązań przyjaznych dla budżetu.
- **Obsługa popularnych wykresów**: Obsługuje popularne typy wykresów, takie jak pierścieniowy, radarowy i warstwowy, choć brakuje jej obsługi bardziej zaawansowanych typów, takich jak mapy geograficzne czy wykresy świecowe.

**Słabe strony**:
- **Ograniczone zaawansowane typy wykresów**: Nie obsługuje map geograficznych, wykresów procesu klasteryzacji ani wykresów świecowych, które są niezbędne dla projektu.
- **Mniejszy ekosystem**: Carbon Charts ma mniejszą społeczność i ekosystem w porównaniu z większymi bibliotekami wykresów, takimi jak ECharts czy Highcharts.

**Werdykt**:  
Carbon Charts jest open source i konfigurowalna, ale brakuje jej obsługi bardziej złożonych typów wykresów potrzebnych w tym projekcie. Lepiej nadaje się do prostszych potrzeb wykresów.

---

### 7. **Layer Cake**

**Przegląd**:  
Layer Cake to biblioteka wizualizacji danych zaprojektowana do tworzenia elastycznych, warstwowych wizualizacji.

**Mocne strony**:
- **Konfigurowalne warstwy**: Oferuje potężne opcje warstwowania dla złożonych wizualizacji.
- **Open source**: Jest bezpłatna i open source, co czyni ją realną opcją dla projektów wrażliwych na budżet.

**Słabe strony**:
- **Ograniczona dokumentacja**: Layer Cake nie ma obszernej dokumentacji ani wsparcia społeczności, co utrudnia pracę w porównaniu z bardziej ugruntowanymi bibliotekami.
- **Nie jest zbudowana do wykresów**: Layer Cake lepiej nadaje się do wizualizacji innych niż wykresy, więc jej gotowe opcje wykresów są ograniczone.

**Werdykt**:  
Choć interesująca do unikalnych wizualizacji, Layer Cake nie jest idealna dla tradycyjnych wymagań wykresów, takich jak wykresy świecowe czy radarowe. Lepiej nadaje się do niestandardowych wizualizacji wykraczających poza zakres standardowych wykresów.

---

### 8. **D3.js**

**Przegląd**:  
D3.js to potężna biblioteka JavaScript do tworzenia wizualizacji opartych na danych za pomocą HTML, SVG i CSS.

**Mocne strony**:
- **Niezrównana elastyczność**: D3.js pozwala tworzyć praktycznie każdy rodzaj niestandardowej wizualizacji, co czyni ją bardzo potężną w zaawansowanych i interaktywnych wykresach.
- **Rozbudowane funkcje**: Obsługuje wszystkie wymagane typy wykresów, w tym mapy geograficzne, wykresy klasteryzacji i inne.
- **Konfigurowalność**: Poziom dostosowywania w D3.js jest niezrównany, co pozwala programistom budować w pełni dopasowane wizualizacje.

**Słabe strony**:
- **Stroma krzywa uczenia się**: D3.js ma stromą krzywą uczenia się i jest trudniejsza w integracji niż inne biblioteki.
- **Czasochłonność**: Budowanie wykresów w D3.js może być czasochłonne, zwłaszcza popularnych wykresów, takich jak świecowe czy pierścieniowe.

**Werdykt**:  
D3.js jest niezwykle potężna w zaawansowanych, dostosowanych wykresach, ale w wielu typowych zastosowaniach jest przesadą ze względu na stromą krzywą uczenia się i czas rozwoju. Najlepiej sprawdza się tam, gdzie inne biblioteki wykresów nie zapewniają wymaganego poziomu dostosowania.

---

### Podsumowanie

Po ocenie bibliotek pod kątem potrzeb projektu **Apache ECharts** wyróżnia się jako najlepsza opcja. Obsługuje pełen zakres wymaganych wykresów, w tym mapy geograficzne, wykresy świecowe i wykresy klasteryzacji. Jest open source, bogata w funkcje i wysoce interaktywna, co idealnie pasuje do celów projektu. Choć **D3.js** oferuje największą elastyczność, jej złożoność i nakład czasu czynią ją mniej idealną dla startupu, który chce szybko iterować. **ApexCharts** i **Chart.js** to dobre alternatywy dla prostszych projektów, ale brakuje im obsługi zaawansowanych typów wykresów.
