# Monorepo czy multirepo

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

Nasz projekt obejmuje tworzenie trzech głównych kategorii oprogramowania:

  * Graficzne interfejsy front-endu
  * Usługi warstwy pośredniej (middleware)
  * Serwery back-endu

Podczas pracy naszym systemem zarządzania kodem źródłowym (SCM) i kontroli wersji (VCS) jest git.

Musimy wybrać, jak używamy gita do organizacji naszego kodu.

Wybór na najwyższym poziomie to organizacja jako „monorepo”, „polyrepo” lub „hybryda”:

  * Monorepo oznacza, że wszystkie elementy trafiają do jednego dużego repozytorium
  * Polyrepo oznacza, że każdy element ma własne repozytorium
  * Hybryda oznacza pewne połączenie monorepo i polyrepo

Więcej informacji: https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Decyzja

Monorepo, gdy organizacja/zespół/projekt jest stosunkowo mały, a szybka iteracja ma wyższy priorytet niż utrzymanie stabilności.

Polyrepo, gdy organizacja/zespół/projekt jest stosunkowo duży, a utrzymanie stabilności ma wyższy priorytet niż szybka iteracja.


### Status

Zdecydowano. Jesteśmy otwarci na ponowne rozważenie, jeśli/gdy pojawią się nowe narzędzia do zarządzania monorepo i/lub polyrepo.


## Szczegóły


### Założenia

Cały kod, który tworzymy, jest przeznaczony dla oferty jednej organizacji, a nie dla ogółu społeczeństwa. Tzn. dom maklerski nie zamierza mieć niczego w rodzaju ogólnodostępnych programistów-wolontariuszy.


### Ograniczenia

Ograniczenia są dobrze udokumentowane pod adresem https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Stanowiska

Rozważaliśmy monorepo w stylu Google, Facebooka itd. Uważamy, że ewentualne problemy ze skalowaniem monorepo są na tyle odległe w przyszłości, że do czasu, gdy będziemy ich potrzebować, będziemy mogli wykorzystać te same praktyki co Google i Facebook.

Rozważaliśmy polyrepo w stylu typowych projektów open source w Git, takich jak Google Android, Facebook React itd. Uważamy, że są one najlepszym wyborem dla udziału ogółu społeczeństwa (np. każdy na świecie może pracować nad kodem) i dostępności indywidualnej (np. projekt jest używany samodzielnie, bez żadnych innych elementów).


### Argument

Gdy organizacja/zespół/projekt jest stosunkowo mały, wybieramy monorepo, ponieważ szybka iteracja ma znacznie wyższy priorytet niż utrzymanie stabilności

Gdy organizacja/zespół/projekt jest stosunkowo duży, wybieramy polyrepo, ponieważ utrzymanie stabilności ma znacznie wyższy priorytet niż szybka iteracja.


### Implikacje

Jeśli istnieje już potok CI+CD, być może trzeba go dostosować do testowania wielu projektów w jednym repozytorium.

CI+CD może zajmować więcej czasu przy pełnym buildzie monorepo, ponieważ CI+CD może budować wszystkie projekty w monorepo.

Jeśli organizacja/zespół/projekt rośnie, monorepo będzie miało problemy ze skalowaniem.

Problemy ze skalowaniem monorepo mogą sprawić, że przejście na polyrepo stanie się coraz bardziej wartościowe.

Przejście z monorepo na polyrepo to istotne zadanie devops, które trzeba zaplanować, zarządzać nim i zaprogramować.


## Powiązane


### Powiązane decyzje

Utworzymy decyzje dotyczące powiązanych narzędzi do zarządzania monorepo (np. Google Bazel) i polyrepo (np. Lyft Refactorator).


### Powiązane wymagania

Musimy opracować potok CI+CD tak, aby dobrze współpracował z gitem.


### Powiązane artefakty

Spodziewamy się, że organizacja repozytoriów będzie mieć powiązane artefakty dla udostępniania zasobów, zarządzania konfiguracją, testowania i podobnych obszarów devops. 


### Powiązane zasady

Łatwo odwracalne. Jeśli monorepo nie sprawdzi się w praktyce lub nie będzie chciane przez kierownictwo, łatwo zmienić na polyrepo.

Obsesja na punkcie klienta. Cenimy dostarczenie projektu w ręce klientów i wierzymy, że monorepo może nas tam doprowadzić szybciej niż polyrepo, a także pomóc szybciej iterować.

Myśl z rozmachem. Google i Facebook są bardzo silnymi zwolennikami monorepo nad polyrepo, ponieważ wszystkie podstawowe oferty można rozwijać/testować/wdrażać wspólnie.


## Notatki

Tu dodaj wszelkie notatki.
