# Szablon rejestru decyzji autorstwa arc42

<https://arc42.org/overview>

## 1. Wprowadzenie i cele

Krótki opis wymagań, sił napędowych, wyciąg (lub streszczenie) wymagań. Trzy
(maksymalnie pięć) najważniejszych celów jakościowych architektury, które mają
najwyższy priorytet dla głównych interesariuszy. Tabela ważnych interesariuszy
wraz z ich oczekiwaniami wobec architektury.

## 1.1 Przegląd wymagań

### Zawartość

Krótki opis wymagań funkcjonalnych, sił napędowych, wyciąg (lub streszczenie)
wymagań. Odnośniki do (miejmy nadzieję istniejących) dokumentów wymagań wraz z
informacją, gdzie je znaleźć. 

### Motywacja

Z punktu widzenia użytkowników końcowych system jest tworzony lub modyfikowany,
aby lepiej wspierać działalność biznesową i/lub poprawić jakość. 

### Forma

Krótki opis tekstowy, prawdopodobnie w tabelarycznym formacie przypadków użycia.
Jeśli istnieją dokumenty wymagań, ten przegląd powinien się do nich odwoływać.

Utrzymuj te wyciągi tak krótkie, jak to możliwe. Zrównoważ czytelność tego
dokumentu z potencjalną redundancją względem dokumentów wymagań. 

## 1.2 Cele jakościowe

### Zawartość

Trzy (maksymalnie pięć) najważniejszych celów jakościowych architektury, których
spełnienie ma największe znaczenie dla głównych interesariuszy. Naprawdę mamy na
myśli cele jakościowe dla architektury. Nie myl ich z celami projektu. Nie
muszą być identyczne. Norma ISO 25010 zapewnia dobry przegląd potencjalnych
interesujących tematów.

### Motywacja

Powinieneś znać cele jakościowe swoich najważniejszych interesariuszy, ponieważ
wpłyną one na fundamentalne decyzje architektoniczne. Bądź bardzo konkretny
co do tych jakości, unikaj modnych haseł. Jeśli jako architekt nie wiesz, jak
będzie oceniana jakość Twojej pracy …

### Forma

Tabela z najważniejszymi celami jakościowymi i konkretnymi scenariuszami,
uporządkowana według priorytetów.

## 1.3 Interesariusze

### Zawartość

Jawny przegląd interesariuszy systemu, czyli wszystkich osób, ról lub
organizacji, które

- powinny znać architekturę

- trzeba przekonać do architektury

- muszą pracować z architekturą lub z kodem

- potrzebują dokumentacji architektury do swojej pracy

- muszą podejmować decyzje dotyczące systemu lub jego rozwoju

### Motywacja

Powinieneś znać wszystkie strony zaangażowane w rozwój systemu lub dotknięte
przez system. W przeciwnym razie możesz doświadczyć nieprzyjemnych niespodzianek
w dalszej części procesu rozwoju. Ci interesariusze decydują o zakresie i
poziomie szczegółowości Twojej pracy oraz jej wyników.

### Forma

Tabela z nazwami ról, imionami i nazwiskami osób oraz ich oczekiwaniami wobec
architektury i jej dokumentacji.

## 2. Ograniczenia

Wszystko, co ogranicza zespoły w decyzjach projektowych i implementacyjnych lub
w decyzjach o powiązanych procesach. Czasem mogą wykraczać poza pojedyncze
systemy i obowiązywać w całych organizacjach i firmach.

### Zawartość

Każde wymaganie, które ogranicza architektów oprogramowania w swobodzie decyzji
projektowych i implementacyjnych lub w decyzjach o procesie rozwoju. Te
ograniczenia czasem wykraczają poza pojedyncze systemy i obowiązują w całych
organizacjach i firmach.

### Motywacja

Architekci powinni dokładnie wiedzieć, gdzie mają swobodę w decyzjach
projektowych, a gdzie muszą przestrzegać ograniczeń. Z ograniczeniami zawsze
trzeba sobie radzić; mogą jednak podlegać negocjacjom.

### Forma

Proste tabele ograniczeń z wyjaśnieniami. W razie potrzeby możesz je podzielić
na ograniczenia techniczne, ograniczenia organizacyjne i polityczne oraz
konwencje (np. wytyczne dotyczące programowania lub wersjonowania, konwencje
dokumentacji lub nazewnictwa)

## 3. Kontekst i zakres

Wyznacza granicę między Twoim systemem a jego (zewnętrznymi) partnerami
komunikacji (systemami sąsiednimi i użytkownikami). Określa interfejsy
zewnętrzne. Przedstawiany z perspektywy biznesowej/dziedzinowej (zawsze) lub
technicznej (opcjonalnie)

### Zawartość

Zakres i kontekst systemu — jak sama nazwa wskazuje — wyznacza granicę między
Twoim systemem (czyli Twoim zakresem) a wszystkimi jego partnerami komunikacji
(systemami sąsiednimi i użytkownikami, czyli kontekstem Twojego systemu). W ten
sposób określa interfejsy zewnętrzne.

W razie potrzeby rozróżnij kontekst biznesowy (dane wejściowe i wyjściowe
właściwe dla dziedziny) od kontekstu technicznego (kanały, protokoły, sprzęt).

### Motywacja

Interfejsy dziedzinowe i techniczne do partnerów komunikacji należą do
najbardziej krytycznych aspektów Twojego systemu. Upewnij się, że w pełni je
rozumiesz.

### Forma

- Różne diagramy kontekstu

- Listy partnerów komunikacji i ich interfejsów.

## 3.1 Kontekst biznesowy

### Zawartość

Specyfikacja wszystkich partnerów komunikacji (użytkowników, systemów IT, …) z
wyjaśnieniami danych wejściowych i wyjściowych lub interfejsów właściwych dla
dziedziny. Opcjonalnie możesz dodać formaty właściwe dla dziedziny lub protokoły
komunikacyjne.

### Motywacja

Wszyscy interesariusze powinni rozumieć, jakie dane są wymieniane z otoczeniem
systemu.

### Forma

Wszelkiego rodzaju diagramy, które pokazują system jako czarną skrzynkę i
określają interfejsy dziedzinowe do partnerów komunikacji.

Alternatywnie (lub dodatkowo) możesz użyć tabeli. Tytułem tabeli jest nazwa
Twojego systemu, a trzy kolumny zawierają nazwę partnera komunikacji, dane
wejściowe i dane wyjściowe.

## 3.2 Kontekst techniczny

### Zawartość

Interfejsy techniczne (kanały i nośniki transmisji) łączące Twój system z jego
otoczeniem. Ponadto odwzorowanie danych wejściowych/wyjściowych właściwych dla
dziedziny na kanały, czyli wyjaśnienie, które wejście/wyjście używa którego
kanału.

### Motywacja

Wielu interesariuszy podejmuje decyzje architektoniczne na podstawie interfejsów
technicznych między systemem a jego kontekstem. W szczególności projektanci
infrastruktury lub sprzętu decydują o tych interfejsach technicznych.

### Forma

Np. diagram wdrożenia UML opisujący kanały do systemów sąsiednich wraz z tabelą
odwzorowań pokazującą zależności między kanałami a wejściem/wyjściem.

## 4. Strategia rozwiązania

Podsumowanie fundamentalnych decyzji i strategii rozwiązania, które kształtują
architekturę. Może obejmować technologię, dekompozycję najwyższego poziomu,
podejścia do osiągnięcia najważniejszych celów jakościowych oraz istotne decyzje
organizacyjne.

### Zawartość

Krótkie podsumowanie i wyjaśnienie fundamentalnych decyzji i strategii
rozwiązania, które kształtują architekturę systemu. Należą do nich

- decyzje technologiczne

- decyzje o dekompozycji systemu na najwyższym poziomie, np. użycie wzorca architektonicznego lub wzorca projektowego

- decyzje o tym, jak osiągnąć kluczowe cele jakościowe

- istotne decyzje organizacyjne, np. wybór procesu rozwoju lub powierzenie określonych zadań podmiotom trzecim.

### Motywacja

Te decyzje stanowią fundamenty Twojej architektury. Są podstawą dla wielu innych
szczegółowych decyzji lub reguł implementacji.

### Forma

Utrzymuj wyjaśnienie tych kluczowych decyzji krótkie.

Uzasadnij, co postanowiłeś i dlaczego tak postanowiłeś, w oparciu o opis
problemu, cele jakościowe i kluczowe ograniczenia. Odwołuj się do szczegółów w
kolejnych sekcjach (sekcja 5 dla szczegółów strukturalnych, sekcja 8 dla
koncepcji przekrojowych).

Możesz użyć listy podejść do rozwiązania lub tabeli.

## 5. Widok bloków budulcowych

Statyczna dekompozycja systemu, abstrakcje kodu źródłowego, przedstawione jako
hierarchia białych skrzynek (zawierających czarne skrzynki), do odpowiedniego
poziomu szczegółowości.

### Zawartość

Widok bloków budulcowych pokazuje statyczną dekompozycję systemu na bloki
budulcowe (moduły, komponenty, podsystemy, klasy, interfejsy, pakiety,
biblioteki, frameworki, warstwy, partycje, poziomy, funkcje, makra, operacje,
struktury danych, …) oraz ich zależności (relacje, powiązania, …)

Ten widok jest obowiązkowy w każdej dokumentacji architektury. Przez analogię do
domu jest to rzut piętra.

### Motywacja

Zachowaj przegląd swojego kodu źródłowego, czyniąc jego strukturę zrozumiałą
dzięki abstrakcji.

Pozwala to komunikować się z interesariuszami na poziomie abstrakcyjnym bez
ujawniania szczegółów implementacji.

### Forma

Widok bloków budulcowych to hierarchiczny zbiór czarnych i białych skrzynek
(patrz rysunek poniżej) oraz ich opisów.

## 5.1 Biała skrzynka — cały system

Tutaj opisujesz dekompozycję całego systemu, używając poniższego szablonu białej
skrzynki. Zawiera on

- diagram przeglądowy

- motywację dekompozycji

- opisy czarnych skrzynek zawartych bloków budulcowych. Dla nich oferujemy
  alternatywy:

  - użyj jednej tabeli do krótkiego i pragmatycznego przeglądu wszystkich zawartych bloków budulcowych i ich interfejsów

  - użyj listy opisów czarnych skrzynek bloków budulcowych według szablonu czarnej skrzynki (patrz niżej). W zależności od wybranego narzędzia ta lista może być podrozdziałami (w plikach tekstowych), podstronami (w wiki) lub zagnieżdżonymi elementami (w narzędziu do modelowania).

  - (opcjonalnie:) ważne interfejsy, które nie są wyjaśnione w szablonach czarnej skrzynki bloku budulcowego, ale są bardzo ważne dla zrozumienia białej skrzynki.

Ponieważ istnieje tak wiele sposobów określania interfejsów, nie dostarczamy dla
nich konkretnego szablonu.

W najlepszym przypadku wystarczą przykłady lub proste sygnatury.

## 5.2 Poziom 2

Tutaj możesz określić wewnętrzną strukturę (niektórych) bloków budulcowych z
poziomu 1 jako białe skrzynki.

Musisz zdecydować, które bloki budulcowe Twojego systemu są na tyle ważne, by
uzasadnić tak szczegółowy opis. Wybieraj istotność zamiast kompletności. Opisuj
bloki budulcowe ważne, zaskakujące, ryzykowne, złożone lub zmienne. Pomiń
normalne, proste, nudne lub znormalizowane części systemu

### 5.2.1 Biała skrzynka dla bloku budulcowego 1

Określa wewnętrzną strukturę bloku budulcowego 1.

Użyj szablonu białej skrzynki (patrz wyżej).

## 6. Widok czasu wykonania

Zachowanie bloków budulcowych w postaci scenariuszy obejmujących ważne
przypadki użycia lub funkcje, interakcje na krytycznych interfejsach
zewnętrznych, eksploatację i administrację oraz zachowanie w przypadku błędów i
wyjątków.

### Zawartość

Widok czasu wykonania opisuje konkretne zachowanie i interakcje bloków
budulcowych systemu w postaci scenariuszy z następujących obszarów:

- ważne przypadki użycia lub funkcje: jak bloki budulcowe je realizują?

- interakcje na krytycznych interfejsach zewnętrznych: jak bloki budulcowe współpracują z użytkownikami i systemami sąsiednimi?

- eksploatacja i administracja: uruchomienie, start, zatrzymanie

- scenariusze błędów i wyjątków

Uwaga: Głównym kryterium wyboru możliwych scenariuszy (sekwencji, przepływów pracy) jest ich istotność architektoniczna. Nie jest ważne opisanie dużej liczby scenariuszy. Lepiej udokumentować reprezentatywny wybór.

### Motywacja

Powinieneś rozumieć, jak (instancje) bloków budulcowych Twojego systemu wykonują swoją pracę i komunikują się w czasie wykonania. W dokumentacji będziesz głównie opisywać scenariusze, aby przekazać architekturę interesariuszom, którzy mniej chętnie lub mniej potrafią czytać i rozumieć modele statyczne (widok bloków budulcowych, widok wdrożenia).

### Forma

Istnieje wiele notacji do opisywania scenariuszy, np.


- numerowana lista kroków (w języku naturalnym)

- diagramy aktywności lub schematy blokowe

- diagramy sekwencji

- BPMN lub EPC (łańcuchy procesów zdarzeniowych)

- maszyny stanów

- itd.

## 6.n Scenariusz czasu wykonania n (1, 2, 3 itd.)

Wstaw diagram czasu wykonania lub tekstowy opis scenariusza.

Wstaw opis istotnych aspektów interakcji między instancjami bloków budulcowych przedstawionych na tym diagramie.

## 7. Widok wdrożenia

Infrastruktura techniczna ze środowiskami, komputerami, procesorami,
topologiami. Odwzorowanie (programowych) bloków budulcowych na elementy
infrastruktury.

### Zawartość

Widok wdrożenia opisuje:

- infrastrukturę techniczną użytą do uruchamiania Twojego systemu, z elementami
  infrastruktury takimi jak lokalizacje geograficzne, środowiska, komputery,
  procesory, kanały i topologie sieci oraz inne elementy infrastruktury, a także

- odwzorowanie (programowych) bloków budulcowych na te elementy infrastruktury.

Systemy są często uruchamiane w różnych środowiskach, np. środowisko
programistyczne, środowisko testowe, środowisko produkcyjne. W takich
przypadkach powinieneś udokumentować wszystkie istotne środowiska.

Szczególnie dokumentuj widok wdrożenia, gdy Twoje oprogramowanie działa jako
system rozproszony z więcej niż jednym komputerem, procesorem, serwerem lub
kontenerem albo gdy projektujesz i budujesz własne procesory sprzętowe i układy.

Z perspektywy oprogramowania wystarczy opisać te elementy infrastruktury, które
są potrzebne do pokazania wdrożenia Twoich bloków budulcowych. Architekci
sprzętu mogą pójść dalej i opisać infrastrukturę z dowolnym poziomem
szczegółowości, jakiego potrzebują. 

### Motywacja

Oprogramowanie nie działa bez sprzętu. Ta leżąca u podstaw infrastruktura może i
będzie wpływać na Twój system i/lub niektóre koncepcje przekrojowe. Dlatego
musisz znać infrastrukturę.

### Forma

Być może diagram wdrożenia najwyższego poziomu jest już zawarty w sekcji 3.2 jako kontekst techniczny, z Twoją własną infrastrukturą jako JEDNĄ czarną skrzynką. W tej sekcji przybliżysz tę czarną skrzynkę za pomocą dodatkowych diagramów wdrożenia.

- UML oferuje diagramy wdrożenia do wyrażenia tego widoku. Użyj go, prawdopodobnie z zagnieżdżonymi diagramami, gdy Twoja infrastruktura jest bardziej złożona.

- Gdy Twoi interesariusze (od sprzętu) wolą inne rodzaje diagramów niż diagram
  wdrożenia UML, pozwól im użyć dowolnego rodzaju, który potrafi pokazać węzły i
  kanały infrastruktury.

## 7.1 Infrastruktura — poziom 1

Opisz (zwykle w połączeniu diagramów, tabel i tekstu):

- rozmieszczenie Twojego systemu w wielu lokalizacjach, środowiskach, komputerach, procesorach, .. oraz fizyczne połączenia między nimi

- ważne uzasadnienie lub motywację dla tej struktury wdrożenia

- cechy jakościowe i/lub wydajnościowe infrastruktury

- odwzorowanie artefaktów programowych (bloków budulcowych) na elementy infrastruktury

W przypadku wielu środowisk lub alternatywnych wdrożeń skopiuj tę sekcję arc42 dla wszystkich istotnych środowisk. **

## 7.2 Infrastruktura — poziom 2

Tutaj możesz zamieścić wewnętrzną strukturę (niektórych) elementów infrastruktury z poziomu 1 infrastruktury.

Skopiuj strukturę z poziomu 1 dla każdego wybranego elementu.

## 8. Koncepcje przekrojowe

Ogólne, podstawowe regulacje i podejścia do rozwiązań istotne w wielu częściach
(→ przekrojowo) systemu. Koncepcje często dotyczą wielu bloków budulcowych.
Obejmują różne tematy, takie jak modele dziedzinowe, wzorce i style
architektoniczne, reguły użycia określonych technologii oraz reguły
implementacji.

### Zawartość

Ta sekcja opisuje koncepcje przekrojowe (praktyki, wzorce, regulacje lub pomysły
na rozwiązania). Takie koncepcje często dotyczą wielu bloków budulcowych. Mogą
obejmować wiele różnych tematów.

### Motywacja

Koncepcje stanowią podstawę spójności koncepcyjnej (zgodności, jednorodności)
architektury. Są zatem ważnym wkładem w osiągnięcie wewnętrznych jakości Twojego
systemu.

To jest miejsce w szablonie, które przewidzieliśmy na spójną specyfikację takich
koncepcji.

Wiele z tych koncepcji odnosi się do kilku Twoich bloków budulcowych lub na nie
wpływa.

### Forma

Forma może być różna:

- opracowania koncepcyjne o dowolnej strukturze

- przykładowe implementacje, zwłaszcza dla koncepcji technicznych

- przekrojowe wyciągi z modeli lub scenariusze w notacjach widoków architektury

### Struktura tej sekcji

Wybierz tylko najbardziej potrzebne tematy dla swojego systemu i przypisz każdemu nagłówek drugiego poziomu w tej sekcji (np. 8.1, 8.2 itd.).

- NIE PRÓBUJ obejmować wszystkich tematów z wyżej wspomnianego diagramu.

### Tło

Niektóre tematy w systemach często dotyczą wielu bloków budulcowych, elementów
sprzętu lub procesów rozwoju. Łatwiej może być przekazywać lub dokumentować
takie tematy przekrojowe w jednym centralnym miejscu, zamiast powtarzać je w
opisie dotyczących ich bloków budulcowych, elementów sprzętu lub procesów
rozwoju.

Niektóre koncepcje mogą dotyczyć wszystkich elementów systemu, inne mogą być
istotne tylko dla kilku.

## 9. Decyzje architektoniczne

Ważne, kosztowne, krytyczne, wielkoskalowe lub ryzykowne decyzje architektoniczne
wraz z uzasadnieniami.

### Zawartość

Ważne, kosztowne, wielkoskalowe lub ryzykowne decyzje architektoniczne wraz z
uzasadnieniami. Przez „decyzje” rozumiemy wybór jednej alternatywy na podstawie
danych kryteriów.

Oceń według własnego osądu, czy decyzja architektoniczna powinna być
udokumentowana tutaj, w tej centralnej sekcji, czy lepiej udokumentować ją
lokalnie (np. w szablonie białej skrzynki jednego bloku budulcowego). Unikaj
redundantnych tekstów. Odwołaj się do sekcji 4, w której już opisałeś
najważniejsze decyzje swojej architektury.

### Motywacja

Interesariusze Twojego systemu powinni móc zrozumieć i prześledzić Twoje
decyzje.

### Forma

- ADR (rejestr decyzji architektonicznych) dla każdej ważnej decyzji

- lista lub tabela, uporządkowana według ważności i konsekwencji, albo

- bardziej szczegółowo w postaci osobnych sekcji dla każdej decyzji

### Tło (dotyczące ADR)

Mniejsze fragmenty dokumentacji są łatwiejsze do czytania, tworzenia i
utrzymania. W przypadku decyzji architektonicznych zespoły programistyczne
często:

- znają decyzję, ponieważ jest widoczna np. w kodzie źródłowym, ale

- nie znają motywacji stojącej za tą decyzją (patrz Nygard 2011)

Dlatego powinieneś udokumentować kilka ważnych decyzji wraz z ich motywacją i
uzasadnieniem

### Nasza propozycja dotycząca decyzji

Prowadź zbiór decyzji istotnych dla architektury, czyli tych decyzji, które
wpływają na strukturę, cechy jakościowe, ważne (zwłaszcza zewnętrzne) zależności
i interfejsy lub techniki budowy (dzięki Michaelowi Nygardowi za tę propozycję).

## 10. Wymagania jakościowe

Wymagania jakościowe jako scenariusze, z drzewem jakości dającym przegląd na
wysokim poziomie. Najważniejsze cele jakościowe powinny być opisane w sekcji
1.2. (cele jakościowe).

### Zawartość

Ta sekcja zawiera wszystkie istotne wymagania jakościowe.

Najważniejsze z tych wymagań zostały już opisane w sekcji 1.2. (cele jakościowe),
dlatego należy tu tylko się do nich odwołać. W tej sekcji 10 powinieneś także
opisać wymagania jakościowe o mniejszym znaczeniu, które nie stwarzają dużego
ryzyka, gdy nie zostaną w pełni osiągnięte (ale mogą być mile widziane).

### Motywacja

Ponieważ wymagania jakościowe mają duży wpływ na decyzje architektoniczne,
powinieneś wiedzieć, jakie jakości są naprawdę ważne dla Twoich interesariuszy,
w sposób konkretny i mierzalny.

### Dalsze informacje

Zobacz obszerny model jakości Q42 na https://quality.arc42.org.

## 10.1 Przegląd wymagań jakościowych

### Zawartość

Przegląd lub podsumowanie wymagań jakościowych.

### Motywacja

Często spotykamy dziesiątki (a nawet setki) szczegółowych wymagań jakościowych.
W tej sekcji przeglądowej powinieneś spróbować je podsumować, np. opisując
kategorie lub tematy (jak sugerują ISO 25010:2023 lub Q42

Jeśli te opisy podsumowujące są już precyzyjne, wystarczająco konkretne i
mierzalne, możesz pominąć sekcję 10.2.

### Forma

Użyj prostej tabeli, w której każdy wiersz zawiera kategorię lub temat oraz
krótki opis wymagania jakościowego. Alternatywnie możesz użyć mapy myśli do
uporządkowania tych wymagań jakościowych.

W literaturze opisano także ideę drzewa atrybutów jakości, które stawia ogólny
termin „jakość” jako korzeń i używa drzewiastego uszczegóławiania terminu
„jakość”. [Bass+21] wprowadził w tym celu termin „Quality Attribute Utility
Tree”.

## 10.2 Scenariusze jakościowe

### Zawartość

Scenariusze jakościowe konkretyzują wymagania jakościowe i pozwalają zdecydować,
czy są spełnione (w rozumieniu kryteriów akceptacji). Zadbaj, aby Twoje
scenariusze były konkretne i mierzalne.

Dwa rodzaje scenariuszy są szczególnie użyteczne:

- Scenariusze użycia (zwane też scenariuszami aplikacji lub scenariuszami
  przypadków użycia) opisują reakcję systemu w czasie wykonania na określony
  bodziec. Obejmuje to również scenariusze opisujące efektywność lub wydajność
  systemu. Przykład: System reaguje na żądanie użytkownika w ciągu jednej sekundy.

- Scenariusze zmian opisują pożądany efekt modyfikacji lub rozszerzenia
  systemu albo jego bezpośredniego otoczenia. Przykład: Zostaje zaimplementowana
  dodatkowa funkcjonalność lub zmieniają się wymagania dotyczące atrybutu
  jakości, a nakład pracy lub czas trwania zmiany jest mierzony.

### Forma

Typowe informacje w szczegółowych scenariuszach obejmują:

W formie skróconej (preferowanej w modelu Q42):

- Kontekst/Tło: Jaki rodzaj systemu lub komponentu, jakie jest środowisko lub sytuacja?

- Źródło/Bodziec: Kto lub co inicjuje lub wywołuje zachowanie, reakcję lub działanie.

- Miara/Kryteria akceptacji: Odpowiedź zawierająca miarę lub metrykę

Forma rozszerzona scenariuszy (preferowana przez SEI i [Bass+21]) jest bardziej szczegółowa i zawiera następujące informacje:

- Identyfikator scenariusza: Unikalny identyfikator scenariusza.

- Nazwa scenariusza: Krótka, opisowa nazwa scenariusza.

- Źródło: Podmiot (użytkownik, system lub zdarzenie), który inicjuje scenariusz.

- Bodziec: Zdarzenie lub warunek wyzwalający, którym system musi się zająć.

- Środowisko: Kontekst operacyjny lub warunek, w którym system doświadcza bodźca.

- Artefakt: Bloki budulcowe lub inne elementy systemu, na które wpływa bodziec.

- Odpowiedź: Wynik lub zachowanie, jakie system wykazuje w reakcji na bodziec.

- Miara odpowiedzi: Kryteria lub metryka, według których oceniana jest odpowiedź systemu.

### Zobacz także

Od stycznia 2023 r. arc42 udostępnia pragmatyczny model jakości, który proponuje
oznaczanie wymagań jakościowych hashtagami lub etykietami, takimi jak #flexible,
#efficient, #usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Ryzyka i dług techniczny

Znane ryzyka techniczne lub dług techniczny. Jakie potencjalne problemy istnieją
w systemie lub wokół niego? Z czym zespół programistyczny czuje się źle?

### Zawartość

Lista zidentyfikowanych ryzyk technicznych lub długów technicznych,
uporządkowana według priorytetu

### Motywacja

„Zarządzanie ryzykiem to zarządzanie projektem dla dorosłych” (Tim Lister,
Atlantic Systems Guild.)

Powinno to być Twoje motto w systematycznym wykrywaniu i ocenie ryzyk i długów
technicznych w architekturze, które będą potrzebne interesariuszom z zarządzania
(np. kierownikom projektów, właścicielom produktów) w ramach ogólnej analizy
ryzyka i planowania działań.

### Forma

Lista ryzyk i/lub długów technicznych, prawdopodobnie wraz z sugerowanymi
środkami minimalizacji, łagodzenia lub unikania ryzyk albo redukcji długów
technicznych.
