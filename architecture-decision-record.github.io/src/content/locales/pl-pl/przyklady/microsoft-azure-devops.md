# Microsoft Azure DevOps

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
  * [Microsoft Devops CI: An Unsatisfying Adventure](#microsoft-devops-ci-an-unsatisfying-adventure)
  * [Najważniejsze fragmenty dyskusji na Hacker News](#najważniejsze-fragmenty-dyskusji-na-hacker-news)
  * [Windows Development MVP](#windows-development-mvp)
  * [Podsumowanie Edwarda Thomsona (Azure PM)](#podsumowanie-edwarda-thomsona-azure-pm)


## Podsumowanie


### Problem

Chcemy używać devops do budowania, integrowania, wdrażania i hostowania naszych projektów. Rozważamy Microsoft Azure DevOps.

  * Chcemy, aby doświadczenie programisty było szybkie i niezawodne, zarówno przy konfiguracji devops, np. ustawianiu, jak i w bieżącym użyciu, np. szybkie czasy budowania.
  
  * Chcemy rozważyć użycie Microsoft Azure jako całości, do hostowania aplikacji projektów, baz danych itd.


### Decyzja

Zdecydowano przeciwko Microsoft Azure DevOps.


### Status

Zdecydowano. Jesteśmy otwarci na ponowne rozważenie, jeśli/gdy pojawią się nowe istotne informacje.


## Szczegóły


### Założenia

Wszystkie zwykłe założenia devops, takie jak w książce Accelerate.

  * Szybkie buildy bardzo pomagają. Przyspiesza to pętle sprzężenia zwrotnego.

  * Możemy wymieniać elementy na elementy od innych dostawców, tzn. możemy chcieć użyć własnych, szybszych serwerów budowania, wybrać własny system kontroli wersji lub współpracować z samodzielnie hostowanym serwerem ciągłej integracji.
  
  * Uproszczona użyteczność bardzo pomaga w doświadczeniu programisty, a w konsekwencji w subtelnych obszarach, takich jak spójność, jasność, bezpieczeństwo i łatwość krzywej uczenia się.

  * Gdy coś jest zepsute lub problematyczne, chcemy skutecznego sposobu zgłoszenia problemu. Jest to szczególnie ważne w przypadku problemów związanych z bezpieczeństwem.


### Ograniczenia

Nie znamy żadnych. Azure ma opublikowane zobowiązanie do dobrej współpracy z narzędziami zewnętrznymi.


### Stanowiska

Rozważaliśmy użycie Microsoft Azure Devops w porównaniu z AWS, który jest obecnym rozwiązaniem.

Eksperymentowaliśmy z Azure DevOps, Azure Pipelines, Azure Repo i uruchamianiem nowego serwera Azure przez Terraform.

Eksperymentowaliśmy z uzyskiwaniem wsparcia od przedstawicieli Microsoftu.

Zbieraliśmy informacje od kolegów z branży na blogach i w Hacker News.


### Argument

Azure DevOps reklamuje doskonały zestaw ofert, ale nie spełniają one oczekiwań, nie współpracują dobrze ze sobą, a wsparcie jest słabe.

Nasze własne doświadczenie:

  * Konfiguracja Azure to bałagan interfejsów, z których część nakłada się na konta Microsoft, a część nie. Np. jest logowanie do Azure, logowanie do Microsoft.com, logowanie do Live.com itd. i wszystkie są jednocześnie w grze.

  * Podczas konfiguracji napotkaliśmy drobny problem z bezpieczeństwem i nie znaleźliśmy rozwiązania. Próbowaliśmy zgłosić go na wiele sposobów, wielu przedstawicielom Microsoftu, bez powodzenia. Zgłosiliśmy go skutecznie do zespołu bezpieczeństwa Microsoftu, który odpowiedział, że nie naprawi.

  * Dokumentacja jest często błędna lub przestarzała. Przynajmniej część wynika ze słabej wyszukiwarki Microsoftu, a część z przeciętnego SEO.
  
  * Konfiguracja Terraform jest dobrze udokumentowana i działa. Jednak wsparcie Terraform jest słabe w porównaniu z AWS, ponieważ Microsoft buduje relacje biznesowe z dostawcami, aby tworzyć łańcuchowe przykłady konfiguracji Terraform.

Doświadczenia kolegów z branży:

  * Po własnej, ślepej ocenie szukaliśmy doświadczeń innych. To, co znaleźliśmy, potwierdziło nasze doświadczenia.

  * Koledzy zgłaszali dodatkowe problemy z czasami budowania i problemy z serwerem budowania dostarczanym przez użytkownika. Te problemy są znacznie poważniejsze niż problemy z interfejsem, ponieważ wykonywanie buildów jest podstawowym celem potoku budowania, a spodziewamy się wielu dziennie.

  * Znaleźliśmy doskonały udział pracowników Azure w obszarach dyskusji. Brawa dla Microsoftu za to. Szczególne wrażenie robi na nas Edward Thomson, PM i programista Azure, ze względu na jego zaangażowanie, bezpośredniość i techniczne wyjaśnienia.


### Implikacje

Wybór Microsoft Azure DevOps wydaje się prawdopodobnie droższy (~3x) pod względem czasu i kosztu niż niewybieranie Azure.


## Powiązane


### Powiązane decyzje

Jeśli wybierzemy Azure DevOps, istnieje wiele powiązanych ofert, w tym Azure Repo, Azure Pipeline itd. Uważamy, że jeśli wybierzemy Azure Devops, może to ułatwić korzystanie z większej liczby możliwości Azure lub utrudnić korzystanie z możliwości innych dostawców.

Uważamy, że Microsoft robi wielkie postępy w doświadczeniu programisty i widzimy, jak Microsoft dokonuje dużych przejęć narzędzi dla programistów (np. GitHub) i zależności (np. Citus).

Jeśli wybierzemy Azure DevOps, możemy chcieć kłaść nacisk na wybór ofert z przejęć Microsoftu, a także podchodzić do ofert z przejęć z większą ostrożnością/oceną z powodu potencjalnego odrzucenia tkanki, np. ryzyka rotacji pracowników.


### Powiązane wymagania

Chcemy, aby czasy budowania były bardzo szybkie. Akceptujemy zapłacenie za to wysokiej premii. Dlatego że chcemy iterować bardzo szybko.

Chcemy bardzo wysokiej niezawodności. Akceptujemy zapłacenie za to wysokiej premii. Dlatego że testujemy przypadki użycia o wysokiej wartości, w tym transakcje finansowe, transakcje poufne itd.

Nasze 4 najważniejsze KPI devops obejmują średni czas przywracania sprawności, co wymaga szybkich buildów i wysokiej niezawodności.


### Powiązane artefakty

Chcemy, aby system budowania generował artefakty nadające się do użycia w innych systemach, takich jak Artifactory.


### Powiązane zasady

Łatwo odwracalne. Możemy oceniać Azure DevOps równolegle z obecnym AWS.


## Notatki


### Microsoft Devops CI: An Unsatisfying Adventure

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Wpis na blogu.

„Jako programista z pierwszej ręki wiem, jak trudno jest szybko i tanio budować produkty wysokiej jakości. To sztuka, którą czasem opanowujemy, a czasem sprowadza się to do czegoś w rodzaju rządowej strony o opiece zdrowotnej z czasów Obamy. Nasz poziom kontroli nad powstałym produktem bywa różny, a winę za porażkę często ponoszą niewłaściwe osoby w hierarchii decyzyjnej. Azure DevOps firmy Microsoft (dawniej znany jako Visual Studio Team Services), mimo wyraźnie dobrych intencji, to idealna burza złych decyzji i słabego wykonania.”


### Najważniejsze fragmenty dyskusji na Hacker News

https://news.ycombinator.com/item?id=18983586

„W mojej pracy intensywnie używamy Azure DevOps i po używaniu GitHuba, Gitlaba, rozwiązań hostowanych samodzielnie, Jenkinsa, TeamCity... Azure DevOps plasuje się na ostatnim miejscu.”

„Interfejs jest wszędzie strasznie niezgrabny. Najgorsze dla mnie są pull requesty. Niesamowicie trudno współpracować z ludźmi nad pull requestem. Nie mogę nawet wskazać „jednego” konkretnego problemu — u nas jest zepsute wszędzie.”

„Azure Devops to coś, co chcę pokochać. Interfejs ciągle się zmienia, ale nie naprawia błędów leżących u podstaw, które istnieją od wieków.”

„Narzędzia nie są dobrze zintegrowane, interfejs jest naprawdę wolny, nie ma widoku pulpitu aktywnych pull requestów, buildów, wydań itd. dla moich ulubionych repozytoriów. Czasy build/deploy są szalenie wolne.”

„Próbowaliśmy też użyć Azure Boards (Work Items, Boards, Backlogs itd.). Ała. To kompletny bałagan w interfejsie, złożony z niepowiązanych pomysłów. Zamiast zaimplementować jedną rzecz dobrze, zaimplementowali dwa tuziny rzeczy fatalnie.”


### Windows Development MVP

Jestem tu jako Windows Development MVP. Czuję, że muszę wziąć na siebie część odpowiedzialności za to, że nie mówiłem głośniej o tych problemach. Muszę jednak powiedzieć, że jestem rozczarowany, słysząc, że jesteście „zaskoczeni” problemami z UX. Mówiłem Waszym ludziom, że UX jest straszny (np. jeszcze przed premierą) i słyszałem w odpowiedzi „wiemy, naprawiamy”. Zacznę formalizować opinie i przepchnę je przez rury, bądźcie czujni. Jestem też lokalnie (Bellevue), chętnie bym przyszedł i spróbował przepuścić przez pipeline naszą stosunkowo prostą aplikację oss .net/wpf/uwp. Podejrzewam, że będzie to dla obu stron otwarcie oczu.

Niektóre przykłady:

* Nie można zbudować pipeline’u z repozytorium git, które zawiera podmoduły

* Edycja PATH dla niektórych własnych narzędzi okazała się niemożliwa

* Doświadczenie New Pipeline po prostu nie ma sensu, nowi użytkownicy klikając dookoła, w końcu trafią do niewłaściwej dokumentacji.


### Podsumowanie Edwarda Thomsona (Azure PM)

Napisałem kod, który scala Wasze pull requesty. Program Manager w Microsoft dla Azure DevOps; wcześniej inżynier oprogramowania w narzędziach kontroli wersji w GitHub, Microsoft, SourceGear.

https://www.edwardthomson.com/

Współopiekun libgit2. https://libgit2.github.io

Współprowadzący All Things Git, podcastu o Gicie. https://www.allthingsgit.com/

Kurator Developer Tools Weekly, newslettera o narzędziach programistycznych. https://developertoolsweekly.com/
