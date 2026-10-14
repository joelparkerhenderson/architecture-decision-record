# Format znacznika czasu

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

Chcemy móc śledzić, kiedy coś się dzieje, za pomocą znaczników czasu i spójnego formatu znacznika czasu, który dobrze działa we wszystkich naszych systemach i systemach firm trzecich.

Współpracujemy z systemami, które mają różne formaty znaczników czasu:

* Komunikaty JSON nie mają natywnego formatu znacznika czasu, więc musimy wybrać, jak przekształcić znacznik czasu w ciąg znaków i ciąg znaków w znacznik czasu, tzn. jak serializować/deserializować.

* Niektóre aplikacje są ustawione na czas lokalny, a nie UTC. Może to być wygodne dla projektów, które muszą dostosowywać się do czasu lokalnego, takich jak projekty wyzwalające zdarzenia oparte na czasie lokalnym.

* Niektóre systemy mają różne potrzeby i możliwości dotyczące precyzji czasu, takie jak rozdzielczość w sekundach, milisekundach lub nanosekundach. Na przykład polecenie `date` systemu operacyjnego Linux domyślnie używa precyzji w sekundach, podczas gdy giełda Nasdaq wymaga domyślnie precyzji w nanosekundach.


### Decyzja

Wybieramy standardowy format znacznika czasu ISO 8601 z precyzją nanosekund, a konkretnie „YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ”.

Format pokazuje rok, miesiąc, dzień, godzinę, minutę, sekundę, nanosekundy oraz strefę czasową Zulu, czyli UTC, GMT.


### Status

Zdecydowano.


## Szczegóły


### Założenia

Musimy obsługiwać te ciągi tekstowe znaczników czasu, aby przekształcać znacznik czasu w ciąg znaków (czyli serializować) i ciąg znaków w znacznik czasu (czyli deserializować).

Chcemy formatu, który jest ogólnie łatwy w użyciu, łatwy do konwersji i łatwy do odczytania przez człowieka.

Chcemy zgodności z szeroką gamą systemów zewnętrznych, nad którymi nie mamy kontroli, takich jak systemy analityczne, systemy baz danych i systemy finansowe.


### Ograniczenia

Niektóre systemy mają ograniczenia precyzji czasu. Na przykład polecenie `date` systemu operacyjnego macOS może wypisywać czas z precyzją sekund, ale nie nanosekund.


### Stanowiska

Rozważaliśmy szereg opcji:

* Epoka uniksowa, czyli jedna rosnąca liczba.

* Zwięzły format tekstowy „YYYYMMDDTHHMMSSNNNNNNNNN”.

* Użycie lokalnej strefy czasowej a strefy czasowej UTC.


### Argument

W typowym użyciu cenimy łatwość odczytu/zapisu przez ludzi bardziej niż surową szybkość/rozmiar.

W typowym użyciu chcemy formatu, który dobrze działa w systemach maszynowych, a także dobrze sprawdza się ręcznie, np. przy pisaniu danych przykładowych, czytaniu wyjścia JSON, przeszukiwaniu pliku logu za pomocą grep itd.

W nietypowym użyciu, takim jak obliczenia wysokiej wydajności, spodziewamy się, że będziemy chcieli zoptymalizować dowolny wybrany format tekstowy, konwertując tekst na szybszy format, taki jak wbudowany typ obiektu daty w języku programowania. Format tekstowy nie ma więc większego znaczenia dla HPC.


### Implikacje

Nasze różne systemy tekstowe i systemy czasu zbiegną się w tym formacie.


## Powiązane


### Powiązane decyzje

Możemy chcieć mieć szybki/łatwy sposób śledzenia również różnic czasu, czyli czasów trwania. Są one łatwe z użyciem znaczników czasu epoki uniksowej.


### Powiązane wymagania

Możemy chcieć dostosować naszą decyzję, np. jeśli pojawi się powiązane wymaganie dotyczące określonego rodzaju znacznika komunikatów logowania, na przykład dla Splunk, Sumo, ELK itd.


### Powiązane artefakty

Formatery i parsery dla języków:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Przykłady Rosetta Code:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Przykłady SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Powiązane zasady

Łatwo odwracalne. Możemy dość łatwo zmienić na inny format, taki jak epoka uniksowa.

Odkładaj przedwczesną optymalizację. W typowym użyciu nie zależy nam zbytnio na garści dodatkowych znaków, takich jak format używający myślników i dwukropków.


## Notatki

Tu dodaj notatki.
