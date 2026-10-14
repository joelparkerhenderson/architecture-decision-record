# Rejestr decyzji architektonicznych (ADR)

Rejestr decyzji architektonicznych (ADR) to dokument, który opisuje ważną decyzję architektoniczną wraz z jej kontekstem i konsekwencjami.

> [!IMPORTANT]
> Dokładnie sprawdź te zasoby na własną odpowiedzialność, zanim użyjesz ich w jakichkolwiek systemach krytycznych.

Spis treści:

- [Czym jest rejestr decyzji architektonicznych?](#czym-jest-rejestr-decyzji-architektonicznych)
- [Jak zacząć korzystać z ADR](#jak-zacząć-korzystać-z-adr)
- [Jak zacząć korzystać z ADR z narzędziami](#jak-zacząć-korzystać-z-adr-z-narzędziami)
- [Jak zacząć korzystać z ADR z git](#jak-zacząć-korzystać-z-adr-z-git)
- [Umiejętności Claude Code dla ADR](#umiejętności-claude-code-dla-adr)
- [Konwencje nazw plików ADR](#konwencje-nazw-plików-adr)
- [Wskazówki, jak pisać dobre ADR](#wskazówki-jak-pisać-dobre-adr)
- [Przykładowe szablony ADR](#przykładowe-szablony-adr)
- [Porady o pracy zespołowej nad ADR](#porady-o-pracy-zespołowej-nad-adr)
- [Pytania o pracę zespołową nad ADR](#pytania-o-pracę-zespołową-nad-adr)
- [Koncepcje kolejnych kroków dla ADR](#koncepcje-kolejnych-kroków-dla-adr)
- [Diagramy architektury, widoki i punkty widzenia](#diagramy-architektury-widoki-i-punkty-widzenia)
- [Funkcje dopasowania dla decyzji jako kod](#funkcje-dopasowania-dla-decyzji-jako-kod)
- [Zabezpieczenia decyzji w pull requestach](#zabezpieczenia-decyzji-w-pull-requestach)
- [Więcej informacji](#więcej-informacji)

Szablony:

- [Szablon rejestru decyzji autorstwa Jeffa Tyree’a i Arta Akermana](szablony/szablon-rejestru-decyzji-jeff-tyree-i-art-akerman/)
- [Szablon rejestru decyzji autorstwa Michaela Nygarda](szablony/szablon-rejestru-decyzji-michael-nygard/)
- [Szablon rejestru decyzji autorstwa EdgeX](szablony/szablon-rejestru-decyzji-edgex/)
- [Szablon rejestru decyzji autorstwa arc42](szablony/szablon-rejestru-decyzji-arc42/)
- [Szablon rejestru decyzji dla wzorca aleksandryjskiego](szablony/szablon-rejestru-decyzji-wzorzec-aleksandryjski/)
- [Szablon rejestru decyzji dla uzasadnienia biznesowego](szablony/szablon-rejestru-decyzji-uzasadnienie-biznesowe/)
- [Szablon rejestru decyzji projektu MADR](szablony/szablon-rejestru-decyzji-projektu-madr/)
- [Szablon rejestru decyzji z użyciem Planguage](szablony/szablon-rejestru-decyzji-z-planguage/)
- [Szablon rejestru decyzji autorstwa Paulo Mersona](https://github.com/pmerson/ADR-template)
- [Szablon rejestru decyzji autorstwa Olafa Zimmermanna](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Szablon rejestru decyzji autorstwa Gareth Morgan](szablony/szablon-rejestru-decyzji-gareth-morgan/)
- [Szablon rejestru decyzji autorstwa GIG Cymru NHS Wales](szablony/szablon-rejestru-decyzji-gig-cymru-nhs-wales/)
- [Szablon rejestru decyzji dla Ważnych Decyzji Technicznych (ITD) autorstwa Ignacio Larrañagi](szablony/szablon-rejestru-decyzji-wazne-decyzje-techniczne/)

Przykłady:

- [Framework CSS](przyklady/framework-css/)
- [Konfiguracja zmiennych środowiskowych](przyklady/konfiguracja-zmiennych-srodowiskowych/)
- [Metryki, monitory, alerty](przyklady/metryki-monitory-alerty/)
- [Microsoft Azure DevOps](przyklady/microsoft-azure-devops/)
- [Monorepo czy multirepo](przyklady/monorepo-czy-multirepo/)
- [Języki programowania](przyklady/jezyki-programowania/)
- [Przechowywanie sekretów](przyklady/przechowywanie-sekretow/)
- [Format znacznika czasu](przyklady/format-znacznika-czasu/)
- [Wiele więcej...](przyklady/)

## Czym jest rejestr decyzji architektonicznych?

**Rejestr decyzji architektonicznych** (ang. architecture decision record, ADR) to dokument, który opisuje ważną decyzję architektoniczną wraz z jej kontekstem i konsekwencjami.

**Decyzja architektoniczna** (ang. architecture decision, AD) to wybór dotyczący projektu oprogramowania, który odpowiada na istotne wymaganie.

**Dziennik decyzji architektonicznych** (ang. architecture decision log, ADL) to zbiór wszystkich rejestrów ADR tworzonych i utrzymywanych dla danego projektu (lub organizacji).

**Wymaganie istotne dla architektury** (ang. architecturally-significant requirement, ASR) to wymaganie, które ma mierzalny wpływ na architekturę systemu oprogramowania.

Wszystkie te pojęcia należą do tematu **zarządzania wiedzą architektoniczną** (ang. architecture knowledge management, AKM).

Celem tego dokumentu jest szybki przegląd rejestrów ADR, sposobu ich tworzenia oraz miejsc, w których można znaleźć więcej informacji.

Skróty:

  * **AD**: decyzja architektoniczna

  * **ADL**: dziennik decyzji architektonicznych

  * **ADR**: rejestr decyzji architektonicznych

  * **AKM**: zarządzanie wiedzą architektoniczną

  * **ASR**: wymaganie istotne dla architektury

## Jak zacząć korzystać z ADR

Aby zacząć korzystać z rejestrów ADR, porozmawiaj ze współpracownikami o poniższych obszarach.

Identyfikacja decyzji:

  * Jak pilna i jak ważna jest decyzja architektoniczna?

  * Czy trzeba ją podjąć teraz, czy może poczekać, aż będzie wiadomo więcej?

  * W identyfikacji decyzji pomagają zarówno doświadczenia osobiste i zespołowe, jak i uznane metody oraz praktyki projektowania.

  * Najlepiej prowadzić listę decyzji do podjęcia, która uzupełnia listę zadań produktu.

Podejmowanie decyzji:

  * Istnieje wiele technik podejmowania decyzji, zarówno ogólnych, jak i właściwych dla architektury oprogramowania, na przykład mapowanie dialogu (ang. dialogue mapping).

  * Grupowe podejmowanie decyzji jest aktywnym tematem badań.

Wdrażanie i egzekwowanie decyzji:

  * Decyzje architektoniczne są stosowane w projektowaniu oprogramowania, dlatego trzeba je przekazać interesariuszom systemu, którzy go finansują, tworzą i obsługują, i uzyskać ich akceptację.

  * Dwie pokrewne praktyki to style kodowania, w których architektura jest widoczna w kodzie, oraz przeglądy kodu skupiające się na kwestiach i decyzjach architektonicznych.

  * Decyzje architektoniczne trzeba też (ponownie) rozważać podczas modernizacji systemu oprogramowania w ramach jego ewolucji.

Dzielenie się decyzjami (opcjonalnie):

  * Wiele decyzji architektonicznych powtarza się w różnych projektach.

  * Dlatego doświadczenia z podjętymi decyzjami, zarówno dobre, jak i złe, mogą być cennymi zasobami do ponownego wykorzystania, gdy stosuje się jawną strategię zarządzania wiedzą.

Dokumentowanie decyzji:

  * Istnieje wiele szablonów i narzędzi do zapisywania decyzji.

  * Zobacz społeczności zwinne, na przykład rejestry ADR M. Nygarda.

  * Zobacz tradycyjne procesy inżynierii oprogramowania i projektowania architektury, na przykład układy tabel zaproponowane przez IBM UMF oraz przez Tyree’a i Akermana z CapitalOne.

Więcej informacji:

  * Powyższe kroki zaczerpnięto z hasła w Wikipedii [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Jak zacząć korzystać z ADR z narzędziami

- [MySpec](https://myspec.dev) — Zautomatyzowana platforma specyfikacji i decyzji architektonicznych, która porządkuje konstytucję projektu, architekturę techniczną i rejestry ADR w czytelny Markdown udostępniany przez MCP.

Z rejestrów ADR możesz zacząć korzystać z narzędziami w dowolny sposób.

Na przykład:

  * Jeśli lubisz Dysk Google i edycję online, możesz utworzyć dokument Google lub arkusz Google.

  * Jeśli lubisz system kontroli wersji kodu źródłowego, taki jak git, możesz utworzyć plik dla każdego rejestru ADR.

  * Jeśli lubisz narzędzia do planowania projektów, takie jak Atlassian Jira, możesz skorzystać z modułu planowania tego narzędzia.

  * Jeśli lubisz wiki, takie jak MediaWiki, możesz utworzyć wiki z rejestrami ADR.

## Jak zacząć korzystać z ADR z git

Jeśli lubisz system kontroli wersji git, oto jak zwykle zaczynamy korzystać z rejestrów ADR z git w typowym projekcie oprogramowania z kodem źródłowym.

Utwórz katalog na pliki ADR:

```sh
$ mkdir adr
```

Dla każdego rejestru ADR utwórz plik tekstowy, na przykład `choose-database.md`:

```sh
$ vi choose-database.md
```

Napisz w rejestrze ADR, co chcesz. Pomysły znajdziesz w szablonach w tym repozytorium.

Zatwierdź rejestr ADR w repozytorium git (commit).

## Umiejętności Claude Code dla ADR

To repozytorium zawiera dwie umiejętności dla [Claude Code](https://claude.com/claude-code) w katalogu [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), aby agent programistyczny AI mógł pisać i utrzymywać ADR w sposób zalecany przez ten projekt:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — ogólnego przeznaczenia, dla każdego, kto pisze ADR w dowolnym projekcie. Pomaga zdecydować, czy decyzja wymaga ADR, tworzy katalog `adr/` lub `decisions/`, nadaje nazwę plikowi, wybiera szablon spośród jedenastu dołączonych szkieletów i pisze solidne sekcje Kontekst/Decyzja/Konsekwencje.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — specjalnie dla opiekunów tego repozytorium. Opisuje układ repozytorium, konwencję odzwierciedlania README/locales oraz dokładne kroki dodawania nowego szablonu, przykładu lub odnośnika do narzędzia.

Aby użyć umiejętności, skopiuj jej folder do `.claude/skills/` w katalogu głównym repozytorium, w którym pracujesz (lub do `~/.claude/skills/`, aby była dostępna w każdym projekcie), a następnie poproś Claude Code o napisanie lub przegląd ADR.

## Konwencje nazw plików ADR

Jeśli rejestry ADR tworzysz w zwykłych plikach tekstowych, warto opracować własną konwencję nazw plików ADR.

My wolimy konwencję nazw plików o określonym formacie.

Przykłady:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Nasza konwencja nazw plików:

  * Nazwa zawiera wyrażenie czasownikowe w trybie rozkazującym (angielski czas teraźniejszy). Poprawia to czytelność i odpowiada formatowi naszych komunikatów commitów.

  * Nazwa używa małych liter i myślników (tak samo jak to repozytorium). To kompromis między czytelnością a wygodą użycia w systemie.

  * Rozszerzenie to markdown. Ułatwia to formatowanie.

## Wskazówki, jak pisać dobre ADR

Cechy dobrego ADR:

* Uzasadnienie: Wyjaśnij powody podjęcia danej decyzji architektonicznej. Może to obejmować kontekst (patrz niżej), zalety i wady różnych możliwych wyborów, porównania funkcji, dyskusje o kosztach i korzyściach i inne.

* Konkretność: Każdy ADR powinien dotyczyć jednej decyzji architektonicznej, a nie kilku.

* Znaczniki czasu: Zaznacz, kiedy powstał każdy element ADR. Jest to szczególnie ważne w przypadku aspektów, które mogą się z czasem zmieniać, takich jak koszty, harmonogramy, skalowanie i tym podobne.

* Niezmienność: Nie zmieniaj istniejących informacji w ADR. Zamiast tego uzupełnij ADR o nowe informacje albo zastąp go, tworząc nowy ADR.

Cechy dobrej sekcji „Kontekst” w ADR:

* Wyjaśnij sytuację swojej organizacji i priorytety biznesowe.

* Uwzględnij uzasadnienia i względy wynikające ze struktury społecznej i umiejętności w Twoich zespołach.

* Uwzględnij istotne zalety i wady oraz opisz je w kategoriach zgodnych z Twoimi potrzebami i celami.

Cechy dobrej sekcji „Konsekwencje” w ADR:

* Wyjaśnij, co wynika z podjęcia decyzji. Mogą to być skutki, wyniki, rezultaty, działania następcze i inne.

* Uwzględnij informacje o kolejnych ADR. Dość często jeden ADR rodzi potrzebę kolejnych, na przykład gdy jeden ADR zawiera duży, nadrzędny wybór, który z kolei wymaga wielu mniejszych decyzji.

* Uwzględnij procesy przeglądu po wdrożeniu. Zespoły zwykle przeglądają każdy ADR po miesiącu, porównując jego treść z tym, co wydarzyło się w praktyce, aby się uczyć i rozwijać.

Nowy ADR może zastąpić poprzedni ADR:

* Gdy zostaje podjęta decyzja architektoniczna, która zastępuje lub unieważnia poprzedni ADR, należy utworzyć nowy ADR

## Przykładowe szablony ADR

Przykładowe szablony ADR, które zebraliśmy w sieci:

- [Szablon ADR autorstwa Michaela Nygarda](szablony/szablon-rejestru-decyzji-michael-nygard/) (prosty i popularny)

- [Szablon ADR autorstwa Jeffa Tyree’a i Arta Akermana](szablony/szablon-rejestru-decyzji-jeff-tyree-i-art-akerman/) (bardziej rozbudowany)

- [Szablon ADR dla wzorca aleksandryjskiego](szablony/szablon-rejestru-decyzji-wzorzec-aleksandryjski/) (prosty, ze szczegółami kontekstu)

- [Szablon ADR dla uzasadnienia biznesowego](szablony/szablon-rejestru-decyzji-uzasadnienie-biznesowe/) (bardziej zorientowany na MBA, z kosztami, analizą SWOT i większą liczbą opinii)

- [Szablon ADR projektu Markdown Any Decision Records (MADR)](szablony/szablon-rejestru-decyzji-projektu-madr/) (wersja prosta i rozbudowana; ta druga kładzie nacisk na opcje oraz ich zalety i wady)

- [Szablon ADR z użyciem Planguage](szablony/szablon-rejestru-decyzji-z-planguage/) (bardziej zorientowany na zapewnianie jakości)

- [Szablon dla Ważnych Decyzji Technicznych (ITD) autorstwa Ignacio Larrañagi](szablony/szablon-rejestru-decyzji-wazne-decyzje-techniczne/) (szczupły, z decyzją na pierwszym miejscu, zoptymalizowany pod szybki przegląd przez kierownictwo)

## Porady o pracy zespołowej nad ADR

Jeśli zastanawiasz się nad używaniem rejestrów decyzji w swoim zespole, oto kilka porad, których nauczyliśmy się, pracując z wieloma zespołami.

Masz okazję poprowadzić współpracowników, rozmawiając wspólnie o tym „dlaczego”, zamiast narzucać „co”. Na przykład rejestry decyzji to sposób, by zespoły myślały mądrzej i lepiej się komunikowały; nie mają wartości, jeśli są tylko wymuszonym papierkowym obowiązkiem wypełnianym po fakcie.

Niektóre zespoły zdecydowanie wolą nazwę „decyzje” od skrótu „ADR”. Gdy zespół używa nazwy katalogu „decisions”, to jakby zapalała się żarówka i zespół zaczyna umieszczać w katalogu więcej informacji, takich jak decyzje dotyczące dostawców, planowania, harmonogramów itd. Wszystkie te rodzaje informacji mogą korzystać z tego samego szablonu. Zakładamy, że ludzie uczą się szybciej ze słowami („decyzje”) niż ze skrótami („ADR”), że chętniej piszą dokumenty robocze, gdy usunie się słowo „rejestr”, a także że niektórzy programiści i niektórzy menedżerowie nie lubią słowa „architektura”.

W teorii niezmienność jest ideałem. W praktyce w naszych zespołach lepiej sprawdziła się zmienność. Wstawiamy nowe informacje do istniejącego ADR, z datą i adnotacją, że informacja pojawiła się po podjęciu decyzji. Takie podejście prowadzi do „żywego dokumentu”, który wszyscy możemy aktualizować. Typowe aktualizacje to informacje, które pojawiają się dzięki nowym członkom zespołu, nowym ofertom, rzeczywistym wynikom naszego korzystania lub zmianom po fakcie po stronie podmiotów trzecich, takim jak możliwości dostawców, plany cenowe, umowy licencyjne itp.

## Pytania o pracę zespołową nad ADR

### Kto może utworzyć ADR?

Rozważ obszary takie jak konkretne osoby, konkretne role, konkretne zespoły lub konkretne działy; rozważ też, czy są osoby, role, zespoły lub działy, które mogą zlecić ADR, czyli zażądać takiego, który napisze ktoś inny. 

Przykładowa odpowiedź: Każda osoba w naszej organizacji, która przeczytała stronę README o rejestrach decyzji architektonicznych, może zaproponować ADR, czyli zacząć go pisać i podzielić się nim z zespołem.

### Co uzasadnia utworzenie ADR?

Rozważ obszary takie jak sposoby pracy zespołów w Twojej organizacji, struktura systemu oprogramowania, koordynacja między zespołami, długoterminowa utrzymywalność, interfejsy zewnętrzne, komu chcesz przynieść korzyść i tym podobne. 

Przykładowa odpowiedź: Chcemy utworzyć ADR, gdy chcemy, aby przyszli programiści rozumieli „dlaczego” robimy to, co robimy.

### Co uzasadnia niepisanie ADR?

Rozważ obszary takie jak decyzje, które nie dotyczą architektury, są drobne (na przykład o minimalnym ryzyku, samodzielne lub podejmowane przez jednego programistę), są już w pełni opisane gdzie indziej (na przykład w standardach, politykach lub dokumentacji) albo są tymczasowe (na przykład obejścia, prototypy lub eksperymenty). 

Przykładowa odpowiedź: Pomijamy ADR, gdy decyzja jest ograniczona pod względem zakresu, czasu, ryzyka i kosztu albo jest już opisana gdzie indziej.

### Jaki jest cykl życia ADR?

Rozważ obszary takie jak proces tworzenia, proces badania, proces podejmowania decyzji, proces wdrażania i proces wycofywania. Zastanów się, jak śledzić cykl życia ADR w czasie, na przykład jak przenosić ADR z jednego stanu do następnego i jak informować o tym interesariuszy. 

Przykładowa odpowiedź: Chcemy, aby ADR miał pięć etapów cyklu życia: Inicjowanie → Badanie → Ocena → Wdrażanie → Utrzymanie → Wycofanie.

### Jakie są kryteria przechodzenia między etapami cyklu życia ADR?

Rozważ obszary takie jak kryteria akceptacji ADR, czyli skąd wiadomo, że jest wystarczająco dobry, by przejść z jednego etapu cyklu życia do następnego? Czy problem jest jasno sformułowany? Czy rozważono alternatywy? Czy kompromisy są dostatecznie dobrze zrozumiane i udokumentowane?
Czy cały istotny kontekst jest na miejscu? Czy zaangażowani są wszyscy istotni interesariusze? Czy uwzględniono wszystkie uwagi? 

Przykładowa odpowiedź: Chcemy, aby interesariusze głosowali nad ADR, gdy aktywny zespół 1) zakończył badania, 2) zakończył ocenę, 3) opublikował propozycję ADR dla interesariuszy wraz z prośbą o komentarze i terminem jednego tygodnia, 4) wszystkie komentarze interesariuszy zostały uwzględnione i rozpatrzone.

### Jakie role i odpowiedzialności wiążą się z ADR?

Rozważ role takie jak autor propozycji, badacz, oceniający, recenzent, zatwierdzający, opiekun i tym podobne. Rozważ odpowiedzialności takie jak komunikacja z interesariuszami, dbanie o spełnienie oczekiwań, udostępnianie na stronie internetowej lub w intranecie oraz okresowy przegląd pracy, zwłaszcza gdy zachodzą istotne zmiany.

Przykładowa odpowiedź: Chcemy, aby każdy ADR miał zawsze główną osobę kontaktową, dodatkową osobę kontaktową i odpowiedzialny zespół; odpowiadają one za komunikację, publikacje, utrzymanie, okresowy przegląd co najmniej raz w roku oraz ewentualne wycofanie w razie potrzeby.

### Jak ADR współgra z zarządzaniem (ang. governance)?

Rozważ obszary takie jak sposoby pracy Twojej organizacji, szczególne wymagania zgodności, na przykład prawne lub kadrowe, oraz to, jak chcesz postępować z konsensusem, konfliktem i eskalacją. Czy są obszary, osoby lub zespoły, które mogą mieć większy wpływ na ADR niż inne, na przykład mogą go zatwierdzić, głosować nad nim lub go zawetować?

Przykładowa odpowiedź: Zarządzanie ADR odbywa się w następującej kolejności priorytetów: dyrektor generalny (CEO), dyrektor techniczny (CTO), dyrektor prawny (CLO), zespół wdrażający ADR, eksperci w zespole najlepiej znający daną decyzję architektoniczną. Nikt inny nie ma uprawnień zarządczych, chyba że opisano je w ADR. 

### Jakie zasady współgrają z ADR?

Rozważ obszary takie jak sposoby pracy Twojej organizacji, w tym działanie szybkie albo powolne, konsensus albo konflikt przy decyzjach, preferencje wobec ryzyka albo bezpieczeństwa, dyskusja publiczna albo prywatna i tym podobne.

Przykładowa odpowiedź: Stosujemy zasady przywództwa: nastawienie na działanie, sprzeciw i zaangażowanie (disagree-and-commit), oszacowania na poziomie 70% są wystarczające dla decyzji łatwych do odwrócenia i wyizolowania oraz publiczny sposób pracy, z wyjątkiem informacji poufnych, jak opisano w umowie o zachowaniu poufności naszej organizacji.

## Koncepcje kolejnych kroków dla ADR

[Arc42](https://arc42.org/) w pragmatyczny sposób odpowiada na dwa pytania i można go dostosować do Twoich konkretnych potrzeb. Co powinieneś dokumentować/komunikować o swojej architekturze? Jak powinieneś to dokumentować/komunikować? Arc42 zawiera rejestry decyzji architektonicznych oraz wskazówki dotyczące celów, ograniczeń, kontekstów, jakości, ryzyk i innych kwestii.

[Model C4](https://c4model.com/) to łatwe do nauczenia, przyjazne programistom podejście do diagramowania architektury oprogramowania. C4 to zestaw hierarchicznych diagramów kontekstu, kontenerów, komponentów i kodu, a także diagramów pomocniczych dla krajobrazu systemów, dynamiki i wdrożenia.

## Diagramy architektury, widoki i punkty widzenia

Diagram architektury nazywa się „widokiem architektury”.

„Widok architektury” jest instancją „punktu widzenia architektury”.

„Punkt widzenia architektury” ma określonych odbiorców i określone kwestie, które mają na uwadze.

Przykłady punktów widzenia architektury, przykłady widoków i przykłady diagramów:

- Zdolności biznesowe

- Procesy biznesowe wysokiego poziomu

- [Strumienie wartości](https://en.wikipedia.org/wiki/Value_stream)

- Funkcje oprogramowania odwzorowane na komponenty aplikacji

- Diagram kontekstu [modelu C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- Diagram kontenerów [modelu C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- [Diagram związków encji](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) do odwzorowania encji danych na komponenty aplikacji

- [Diagramy sekwencji](https://en.wikipedia.org/wiki/Sequence_diagram) do opisu przepływów funkcjonalnych w systemach i integracjach

- Diagramy [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) do opisu przepływów danych między komponentami aplikacji

- Diagramy [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) do opisu procesów biznesowych / scenariuszy użytkownika

- Diagramy [zarządzania tożsamością i dostępem](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM)

- Diagramy [kontroli dostępu opartej na rolach](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) z rolami dla każdego komponentu aplikacji

- Diagramy [kontroli dostępu opartej na atrybutach](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) z atrybutami dla każdego komponentu aplikacji

- Diagramy prywatności

Powiązane diagramy:

- Diagram przypadków użycia pokazuje przypadki użycia kierownictwu/klientom, co poprzedza wymagania, które poprzedzają architekturę oprogramowania.

- Diagram wdrożenia pokazuje fizyczny sprzęt/komputery, na których wdrażane są komponenty oprogramowania.
- Diagram przepływu danych pokazuje, jak dane przemieszczają się przez system i jak są przekształcane.
- Diagram sekwencji służy do pokazania, jak protokoły takie jak HTTP działają na osi czasu.

- Diagram aktywności przedstawia przepływ pracy działań, które wykonuje system oprogramowania, na przykład jak AI postaci niezależnej (NPC).

## Funkcje dopasowania dla decyzji jako kod

Funkcje dopasowania (ang. fitness functions) to obiektywne, zautomatyzowane kontrole, napisane w kodzie programu, które sprawdzają, czy decyzje są przestrzegane.

- Funkcje dopasowania sprawiają, że decyzje można testować i zapewniać.

- Funkcje dopasowania dla decyzji mogą znacznie pomóc w zapewnianiu jakości, procesach regulacyjnych i celach zarządzania (governance).

### Jak funkcje dopasowania łączą się z decyzjami

Rejestr decyzji dokumentuje decyzję, a funkcja dopasowania ją zapewnia.

- Przykładowa decyzja: Używamy event sourcingu ze względu na wymagania audytowe.

- Przykładowa funkcja dopasowania: Używamy serwera ciągłej integracji, aby testować, że każda zmiana stanu musi generować zdarzenia.

### Dlaczego funkcje dopasowania pomagają decyzjom

Obiektywne pomiary: Funkcje dopasowania kończą się powodzeniem albo niepowodzeniem, więc praca jest widoczna i jasna.

Ciągłe użycie: Funkcje dopasowania to Twoje żywe reguły, uruchamiane przy każdym commicie i buildzie.

Pewność przy refaktoryzacji: Funkcje dopasowania automatycznie wychwytują błędy w regułach decyzji.

Skalowalne zarządzanie: Funkcje dopasowania zapewniają standardy bez tworzenia wąskich gardeł.

### Czy funkcje dopasowania mogą korzystać z AI?

Funkcje dopasowania mogą wykorzystywać duże modele językowe (LLM) AI do oceny decyzji, zadając pytania o Twoją pracę,
na przykład plany, kod, schematy, API i inne:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Testy jednostkowe architektury

[ArchUnit](https://www.archunit.org/): sprawdza reguły architektury kodu Java za pomocą dowolnego zwykłego frameworka testów jednostkowych Java.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): sprawdza reguły architektury kodu TypeScript i JavaScript za pomocą Jest, Vitest, Jasmine itd.

## Zabezpieczenia decyzji w pull requestach

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
automatycznie wyświetla właściwe rejestry decyzji we właściwym momencie — gdy
programista aktywnie modyfikuje kod, którego te decyzje dotyczą. Zamiast liczyć
na to, że programiści przeczytają folder z dokumentacją przed scaleniem, istotny
kontekst pojawia się bezpośrednio w pull requeście.

Działa to dla każdego rodzaju rejestru decyzji: decyzji architektonicznych,
decyzji dotyczących danych, decyzji dotyczących zgodności, decyzji klinicznych i
medycznych, decyzji dotyczących bezpieczeństwa i innych.

Działa z dowolnym systemem CI (GitLab, Jenkins, CircleCI) oraz jako hook
pre-commit. Open source. Licencja MIT.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) to GitHub
Action, która odrzuca pull request, gdy obserwowane ścieżki kodu zmieniają się
bez dodania lub zaktualizowania rejestru decyzji architektonicznych. Zwolnienia
są jawne: wiersz `ADR-Exempt:` z podanym powodem przepuszcza bramkę i jest
zapisywany w podsumowaniu zadania. Niezależny od szablonu, bez zależności. Open
source. Licencja MIT.

## Więcej informacji

Wprowadzenie:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Szablony:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Dla pogłębienia wiedzy:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - bezpłatna miesięczna lekcja o architekturze oprogramowania

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Narzędzia:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Wskazówki specyficzne dla firm:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Przykłady:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Filmy:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcasty:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Książki:

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

Zobacz także:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Niezależny od dostawcy, czytelny maszynowo format YAML/JSON do przedstawiania decyzji z jawnym rozumowaniem, założeniami, stanem poznawczym i kompromisami. Uzupełnia ADR, dodając ustrukturyzowane, walidowalne rozumowanie do dokumentacji decyzji.
