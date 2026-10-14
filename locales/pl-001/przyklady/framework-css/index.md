# Rejestr decyzji architektonicznych: framework CSS

Spis treści:

- [Podsumowanie](#podsumowanie)
  - [Problem](#problem)
  - [Decyzja](#decyzja)
  - [Status](#status)
- [Szczegóły](#szczegóły)
  - [Założenia](#założenia)
  - [Ograniczenia](#ograniczenia)
  - [Stanowiska](#stanowiska)
  - [Argument](#argument)
  - [Implikacje](#implikacje)
- [Powiązane](#powiązane)
  - [Powiązane decyzje](#powiązane-decyzje)
  - [Powiązane wymagania](#powiązane-wymagania)
  - [Powiązane artefakty](#powiązane-artefakty)
  - [Powiązane zasady](#powiązane-zasady)
- [Notatki](#notatki)


## Podsumowanie


### Problem

Chcemy użyć frameworka CSS do tworzenia naszych aplikacji internetowych:

  * Chcemy, aby doświadczenie użytkownika było szybkie i niezawodne we wszystkich popularnych przeglądarkach i rozmiarach ekranu.

  * Chcemy szybkiej iteracji nad projektem, układem, UI/UX itd.

  * Chcemy aplikacji responsywnych, zwłaszcza dla mniejszych ekranów, takich jak urządzenia mobilne, większych ekranów, takich jak panoramiczne 4K, oraz ekranów dynamicznych, takich jak obracane wyświetlacze.  


### Decyzja

Zdecydowano się na Bulma.


### Status

Zdecydowano się na Bulma. Jesteśmy otwarci na nowe wybory frameworków CSS, gdy się pojawią.


## Szczegóły


### Założenia

Chcemy tworzyć aplikacje internetowe, które są nowoczesne, szybkie, niezawodne, responsywne itd.

Typowe nowoczesne aplikacje internetowe ograniczają lub eliminują użycie jQuery z kilku powodów: 

  * Nowoczesny JavaScript stopniowo wprowadza wiele możliwości, które zapewniało jQuery, więc jQuery jest mniej potrzebne, a istnieją lepsze/szybsze/mniejsze moduły zapewniające konkretne implementacje

  * Szerokie podejście jQuery polega na bezpośredniej manipulacji DOM, co jest antywzorcem dla nowoczesnych frameworków JavaScript (np. React, Vue, Svelte)

  * jQuery przeszkadza samo sobie, jeśli zostanie załadowane dwukrotnie itd.


### Ograniczenia

Jeśli wybierzemy framework CSS, który używa jQuery, będziemy musieli importować jQuery. Na przykład Semantic UI używa jQuery, a Tachyons nie.

Jeśli wybierzemy framework CSS, który jest minimalny, zrezygnujemy z komponentów frameworka, które możemy chcieć teraz lub wkrótce. Na przykład Semantic UI zapewnia karuzelę obrazów, a Tachyons nie.


### Stanowiska

Rozważaliśmy użycie braku frameworka. Nadal wydaje się to realne, zwłaszcza że CSS grid zapewnia wiele z tego, czego potrzebujemy w naszym projekcie..

Rozważaliśmy wiele frameworków CSS, używając szybkiej selekcji krótkiej listy: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons itd. Nasze dwa wybory do głębszej oceny to Semantic UI (ponieważ ma najbardziej semantyczne podejście) i Bulma (ponieważ ma najlżejsze podejście, które zapewnia komponenty, jakich teraz chcemy).

Rozważaliśmy Semantic UI. Zapewnia on wiele komponentów, w tym te, których chcemy w naszym projekcie: karty, siatki, przyciski itd. Przeprowadziliśmy pilotaż z Semantic UI na dwa sposoby: używając typowych plików z CDN i używając repozytoriów NPM. Osiągnęliśmy sukces z Semantic UI na statycznej stronie HTML, ale nie osiągnęliśmy sukcesu w ramach naszego limitu czasu przy budowie SPA w JavaScript (głównie z powodu problemów z ładowaniem jQuery). Odkryliśmy, że inni programiści proszą twórców Semantic UI o stworzenie wersji bez jQuery z tych samych powodów, co my. Inni programiści proszą o wersję bez jQuery od wielu lat, ale twórcy odmawiają i twierdzą, że każda wersja bez jQuery byłaby zbyt trudna do napisania, np. ~„projekt Semantic UI ma ponad 22 000 punktów styku, które używają jQuery”.

Przykład z Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Rozważaliśmy Bulma. Bulma ma wiele podobnych możliwości jak Semantic UI, choć nie tak wiele zaawansowanych komponentów. Bulma jest zbudowana nowoczesnymi technikami, np. bez jQuery. Bulma ma pewne komponenty od podmiotów trzecich, z których niektóre możemy chcieć użyć.


Przykład z Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argument

Jak wyżej.

W szczególności Semantic UI wydaje się mieć flagę ostrzegawczą zarówno pod względem technologii (czyli tak wiele punktów styku z jQuery), jak i przywództwa (czyli wersja bez jQuery spotkała się ze stanowczym „nie”, zamiast próby opracowania mapy drogowej, ciągłego ulepszania, zbiórki darowizn itd.).


### Implikacje

Jeśli znajdziemy dobry framework CSS bez jQuery, jest to ogólnie pomocne i korzystne.


## Powiązane


### Powiązane decyzje

Wybrany przez nas framework CSS może wpłynąć na testowalność.


### Powiązane wymagania

Chcemy szybko wydać czysto nowoczesną aplikację. 

Nie chcemy tracić czasu na pracę ze starszymi frameworkami (zwłaszcza Semantic UI) używającymi starszych zależności (zwłaszcza jQuery).


### Powiązane artefakty

Wpływa na cały typowy HTML, który będzie używał tego CSS.


### Powiązane zasady

Łatwo odwracalne.

Potrzeba szybkości.


## Notatki

Tu wszelkie notatki.
