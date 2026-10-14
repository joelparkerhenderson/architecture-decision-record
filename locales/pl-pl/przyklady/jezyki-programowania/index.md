# Języki programowania

Spis treści:

* [Podsumowanie](#podsumowanie)
  * [Problem](#problem)
  * [Decyzja](#decyzja)
  * [Status](#status)
* [Szczegóły](#szczegóły)
  * [Założenia](#założenia)
  * [Ograniczenia](#ograniczenia)
  * [Stanowiska](#stanowiska)
  * [Argument](#argument)
  * [Implikacje](#implikacje)
* [Powiązane](#powiązane)
  * [Powiązane decyzje](#powiązane-decyzje)
  * [Powiązane wymagania](#powiązane-wymagania)
  * [Powiązane artefakty](#powiązane-artefakty)
  * [Powiązane zasady](#powiązane-zasady)
* [Notatki](#notatki)


## Podsumowanie


### Problem

Musimy wybrać języki programowania dla naszego oprogramowania. Mamy dwie główne potrzeby: język programowania front-endu odpowiedni dla aplikacji internetowych oraz język programowania back-endu odpowiedni dla aplikacji serwerowych.


### Decyzja

Wybieramy TypeScript dla front-endu.

Wybieramy Rust dla back-endu.


### Status

Zdecydowano. Jesteśmy otwarci na nowe alternatywy, gdy się pojawią.


## Szczegóły


### Założenia

Aplikacje front-endu są typowe:

  * Typowi użytkownicy i interakcje

  * Typowe przeglądarki i systemy

  * Typowe rozwijanie i wdrażanie

Aplikacje front-endu prawdopodobnie będą szybko ewoluować:

  * Chcemy zapewnić szybkie, łatwe tworzenie, wdrażanie, iteracje itd.

  * Cenimy dowodliwość, taką jak bezpieczeństwo typów, i godzimy się na nieco więcej pracy, by ją osiągnąć.

  * Nie potrzebujemy zgodności ze starszymi systemami.

Aplikacje back-endu mają wyższe niż typowe wymagania:

  * Wyższe niż typowe cele jakościowe, zwłaszcza dowodliwość, niezawodność, bezpieczeństwo itd.

  * Wyższe niż typowe cele dotyczące zbliżania się do czasu rzeczywistego, tzn. nie chcemy pauz z powodu odśmiecania pamięci maszyny wirtualnej.

  * Wyższe niż typowe cele dotyczące programowania funkcyjnego, zwłaszcza dla paralelizacji, przetwarzania wielordzeniowego i bezpieczeństwa pamięci.

Akceptujemy dłuższy czas kompilacji na rzecz bezpieczeństwa w czasie kompilacji i szybkości w czasie wykonania.


### Ograniczenia

Mamy silne ograniczenie dotyczące języków, które można używać z usługami funkcji głównych dostawców chmury, takimi jak Amazon Lambda.


### Stanowiska

Rozważaliśmy te języki:

  * C

  * C++

  * Clojure
  
  * Elixir
  
  * Erlang
  
  * Elm
  
  * Flow
  
  * Go
  
  * Haskell
  
  * Java
  
  * JavaScript
  
  * Kotlin
  
  * Python
  
  * Ruby
  
  * Rust
  
  * TypeScript



### Argument

Podsumowanie dla każdego języka:

  * C: odrzucony z powodu niskiego bezpieczeństwa; Rust potrafi niemal wszystko robić lepiej.

  * C++: odrzucony, bo to bałagan; Rust potrafi niemal wszystko robić lepiej.

  * Clojure: doskonałe modelowanie; najlepsze przybliżenie Lispa; świetne środowisko uruchomieniowe na JVM.
  
  * Elixir: doskonałe środowisko uruchomieniowe, w tym wdrażalność i współbieżność; doskonałe doświadczenie programisty; stosunkowo mały ekosystem.

  * Erlang: doskonałe środowisko uruchomieniowe, w tym wdrażalność i współbieżność; wymagające doświadczenie programisty; stosunkowo mały ekosystem.

  * Elm: wygląda bardzo obiecująco; IBM publikuje duże studia przypadków z dobrymi wynikami; mniejszy ekosystem.

  * Flow: ciekawe ulepszenie JavaScriptu; jednak programiści od niego odchodzą.

  * Go: doskonałe doświadczenie programisty; doskonała współbieżność; ale historia złych decyzji, które okaleczają język.

  * Haskell: najlepszy język funkcyjny; mniejsza społeczność programistów; nie osiągnął wystarczająco wielu opublikowanych sukcesów produkcyjnych.

  * Java: doskonałe środowisko uruchomieniowe; doskonały ekosystem; przeciętne doświadczenie programisty.

  * JavaScript: najpopularniejszy język w historii; najbardziej rozpowszechniony ekosystem.

  * Kotlin: naprawia tak wiele w Javie; doskonałe wsparcie JetBrains; dobre opublikowane przypadki portowania z Javy na Kotlin.
  
  * Python: najpopularniejszy język do administracji systemami; świetne narzędzia analityczne; dobre frameworki internetowe; ale porzucony przez Google na rzecz Go.

  * Ruby: najlepsze doświadczenie programisty w historii; najlepsze frameworki internetowe; najmilsza społeczność; ale bardzo wolny; nieco trudny do pakowania.

  * Rust: najlepszy nowy język; nacisk na zerowy koszt abstrakcji; nacisk na współbieżność; jednak stosunkowo mały ekosystem; i ma celowe ograniczenia w niektórych rodzajach przyspieszeń kompilatora, np. bezpośredni dostęp do pamięci musi być jawnie niebezpieczny (unsafe).

  * TypeScript: dodaje typy do JavaScriptu; świetny transpiler; rosnący nacisk programistów na portowanie z JavaScriptu na TypeScript; silne wsparcie Microsoftu.

Zdecydowaliśmy, że maszyny wirtualne wiążą się z kompromisami, których teraz nie potrzebujemy, takimi jak dodatkowa złożoność zapewniająca możliwości w czasie wykonania.

Uważamy, że nasza podstawowa decyzja wynika z dwóch przekrojowych kwestii:

  * Dla najszybszej szybkości wykonania i najściślejszego dostępu do systemu wybralibyśmy JavaScript i C.

  * Dla niemal najszybszej szybkości wykonania i niemal najściślejszego dostępu do systemu wybieramy TypeScript i Rust.

Wyróżnienia otrzymują języki VM i frameworki internetowe, które wybralibyśmy, gdybyśmy chcieli języka VM:

  * Clojure i Luminus

  * Java i Spring

  * Elixir i Phoenix


### Implikacje

Programiści front-endu będą musieli nauczyć się TypeScriptu. Jest to prawdopodobnie łatwa krzywa uczenia się, jeśli głównym doświadczeniem programisty jest JavaScript.

Programiści back-endu będą musieli nauczyć się Rusta. Jest to prawdopodobnie umiarkowana krzywa uczenia się, jeśli głównym doświadczeniem programisty jest C/C++, i trudna krzywa uczenia się, jeśli głównym doświadczeniem programisty jest Java, Python, Ruby lub podobne języki z zarządzaną pamięcią. 

TypeScript i Rust są stosunkowo nowe. Oznacza to, że wiele narzędzi nie ma jeszcze dokumentacji dla tych języków. Na przykład potok devops będzie trzeba skonfigurować dla tych języków, a jak dotąd żadne z narzędzi devops, które oceniamy, nie ma domyślnych przykładów dla tych języków.

Czasy kompilacji TypeScriptu i Rusta są dość długie. Część tego może wynikać z nowości języków. Warto przyjrzeć się sposobom łagodzenia długich czasów kompilacji, takim jak kompilacja na żądanie, współbieżność kompilacji itd.

Wsparcie IDE dla tych języków nie jest jeszcze wszechobecne ani pierwszorzędne. Na przykład JetBrains sprzedaje IDE PyCharm z pierwszorzędnym wsparciem dla Pythona, ale nie sprzedaje IDE z pierwszorzędnym wsparciem dla Rusta; zamiast tego JetBrains może użyć wtyczki Rust, która zapewnia być może 80% wsparcia języka Rust w porównaniu ze wsparciem języka Python.


## Powiązane


### Powiązane decyzje

Będziemy dążyć do wyborów ekosystemowych zgodnych z tymi językami.

Na przykład chcemy wybrać IDE, które ma dobre możliwości dla tych języków.

Na przykład dla naszego frameworka internetowego front-endu bardziej prawdopodobne jest, że wybierzemy framework nastawiony na TypeScript (np. Vue) niż framework nastawiony na czysty JavaScript (np. React).


### Powiązane wymagania

Cały nasz łańcuch narzędzi musi obsługiwać te języki.


### Powiązane artefakty

Spodziewamy się, że możemy eksportować niektóre sekrety do zmiennych środowiskowych.


### Powiązane zasady

Dwa razy mierz, raz buduj. Przedkładamy pewne bezpieczeństwo nad pewną szybkość.

Czas wykonania jest cenniejszy niż czas kompilacji. Przedkładamy użytkowanie przez klientów nad użytkowanie przez programistów.


## Notatki

Tu wszelkie notatki.
