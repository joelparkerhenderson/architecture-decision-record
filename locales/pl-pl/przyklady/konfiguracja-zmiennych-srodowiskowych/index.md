# Konfiguracja zmiennych środowiskowych

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
  * [Implikacje ](#implikacje)
* [Powiązane](#powiązane)
  * [Powiązane decyzje](#powiązane-decyzje)
  * [Powiązane wymagania](#powiązane-wymagania)
  * [Powiązane artefakty](#powiązane-artefakty)
  * [Powiązane zasady](#powiązane-zasady)
* [Notatki](#notatki)


## Podsumowanie


### Problem

Chcemy, aby nasze aplikacje były konfigurowalne poza artefaktami/plikami binarnymi/kodem źródłowym, tak aby jeden build mógł zachowywać się inaczej w zależności od środowiska wdrożenia.

  * Aby to osiągnąć, chcemy użyć konfiguracji przez zmienne środowiskowe.

  * Chcemy zarządzać konfiguracją za pomocą plików, które możemy wersjonować.

  * Chcemy zapewnić programistom pewne udogodnienia, takie jak wiedza o tym, co można konfigurować, i o odpowiednich wartościach domyślnych.


### Decyzja

Zdecydowano się na pliki .env z powiązanym plikiem wartości domyślnych i plikiem schematu.


### Status

Zdecydowano. Jesteśmy otwarci na rozważenie nowych możliwości, gdy się pojawią.


## Szczegóły


### Założenia

Preferujemy oddzielenie kodu aplikacji od kodu środowiska. Zakładamy, że aplikacja musi działać inaczej w różnych środowiskach, takich jak środowisko programistyczne, testowe, demonstracyjne, produkcyjne itd.

Preferujemy praktykę branżową „12 factor app”, a jeszcze bardziej pokrewną praktykę „15 factor app”.

Wiele naszych poprzednich projektów stosowało konwencję pliku `.env` lub podobnego katalogu `.env`. Typową praktyką jest trzymanie ich poza kontrolą wersji i wdrażanie, wersjonowanie oraz zarządzanie nimi w inny sposób.


### Ograniczenia

Chcemy trzymać sekrety poza naszym systemem zarządzania kodem źródłowym (SCM) i systemem kontroli wersji (VCS).

Chcemy dążyć do zgodności z popularnymi frameworkami i bibliotekami oprogramowania. Na przykład Node ma moduł „dotenv” do odczytu konfiguracji ze zmiennych środowiskowych.


### Stanowiska

Rozważaliśmy kilka podejść:

  * Przechowywanie konfiguracji w aplikacji, na przykład w pliku `config.js`.

  * Przechowywanie konfiguracji w środowisku, na przykład w pliku `.env`.

  * Pobieranie konfiguracji ze znanej lokalizacji, takiej jak serwer licencji.


### Argument

Wybraliśmy podejście z plikiem .env, ponieważ:

  * Jest popularne, także wśród ekspertów.

  * Jest zgodne ze wzorcem plików `.env`, który nasze zespoły z powodzeniem stosowały wiele razy w wielu projektach.

  * Jest proste. W szczególności na razie akceptujemy istotne kompromisy, które widzimy, takie jak brak możliwości audytu w porównaniu z podejściem opartym na serwerze licencji.


### Implikacje 

Musimy wymyślić sposób oddzielenia publicznej konfiguracji zmiennych środowiskowych od zarządzania sekretami.


## Powiązane


### Powiązane decyzje

Oczekujemy, że wszystkie nasze aplikacje będą stosować to podejście.

Zaplanujemy aktualizację wszystkich naszych aplikacji, które używają mniej zaawansowanego podejścia, takiego jak wpisanie na stałe w pliku binarnym lub w kodzie źródłowym.

Pozostawimy bez zmian wszystkie nasze aplikacje, które używają bardziej zaawansowanego podejścia, takiego jak serwer licencji.


### Powiązane wymagania

Dodamy możliwości devops dla tych plików, w tym hooki, testy i ciągłą integrację.

Musimy przeszkolić wszystkich współpracujących programistów w zakresie tej decyzji.



### Powiązane artefakty

Każdy obszar, w którym wdrażamy, będzie potrzebował własnego pliku .env i powiązanych plików.


### Powiązane zasady

Łatwo odwracalne.


## Notatki


Przykładowy plik `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Przykładowy plik `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Przykładowy plik `.env.schema` tylko z kluczami:

```env
NAME
EMAIL
```
