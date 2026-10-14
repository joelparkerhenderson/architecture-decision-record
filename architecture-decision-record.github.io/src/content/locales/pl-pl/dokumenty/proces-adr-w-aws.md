# Proces rejestrów decyzji architektonicznych w AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Rejestr decyzji architektonicznych (ADR) to dokument opisujący wybór, którego zespół dokonuje w istotnej kwestii architektury oprogramowania, które planuje zbudować. Każdy ADR opisuje decyzję architektoniczną, jej kontekst i konsekwencje. ADR mają stany, a zatem podlegają cyklowi życia. Przykład ADR znajdziesz w dodatku.

Wynikiem procesu ADR jest zbiór rejestrów decyzji architektonicznych. Ten zbiór tworzy dziennik decyzji. Dziennik decyzji zapewnia kontekst projektu oraz szczegółowe informacje o wdrożeniu i projekcie. Członkowie projektu przeglądają nagłówki każdego ADR, aby zorientować się w kontekście projektu. Czytają ADR, aby zagłębić się w wybory dotyczące implementacji i projektu.

Gdy zespół zaakceptuje ADR, staje się on niezmienny. Jeśli nowe spostrzeżenia wymagają innej decyzji, zespół proponuje nowy ADR. Gdy zespół zaakceptuje nowy ADR, zastępuje on poprzedni ADR.

## Zakres procesu ADR

Członkowie projektu powinni utworzyć ADR dla każdej decyzji istotnej dla architektury, która wpływa na projekt lub produkt programistyczny, w tym dla następujących (Richards i Ford 2020):

* Struktura (na przykład wzorce, takie jak mikrousługi)

* Wymagania niefunkcjonalne (bezpieczeństwo, wysoka dostępność i odporność na awarie)

* Zależności (sprzężenie komponentów)

* Interfejsy (API i opublikowane kontrakty)

* Techniki budowy (biblioteki, frameworki, narzędzia i procesy)

* Wymagania funkcjonalne i niefunkcjonalne są najczęstszymi danymi wejściowymi procesu ADR.


## Zawartość ADR

Gdy zespół stwierdzi potrzebę ADR, członek zespołu zaczyna pisać ADR na podstawie szablonu obowiązującego w całym projekcie. (Przykładowe szablony znajdziesz w organizacji ADR na GitHubie.) Szablon upraszcza tworzenie ADR i zapewnia, że ADR zawiera wszystkie istotne informacje. Każdy ADR powinien co najmniej określać kontekst decyzji, samą decyzję oraz konsekwencje decyzji dla projektu i jego rezultatów. (Przykłady tych sekcji znajdziesz w dodatku.) Jedną z najmocniejszych stron struktury ADR jest to, że skupia się na powodzie decyzji, a nie na tym, jak zespół ją wdrożył. Zrozumienie, dlaczego zespół podjął decyzję, ułatwia pozostałym członkom zespołu jej przyjęcie i chroni przed tym, by inni architekci, którzy nie uczestniczyli w procesie decyzyjnym, unieważnili ją w przyszłości.


## Proces przyjmowania ADR

Każdy członek zespołu może utworzyć ADR, ale zespół powinien ustalić definicję własności ADR. Każdy autor będący właścicielem ADR powinien aktywnie utrzymywać treść ADR i o niej informować. Aby doprecyzować tę własność, w dalszych sekcjach tego przewodnika autorów ADR nazywamy właścicielami ADR. Pozostali członkowie zespołu zawsze mogą współtworzyć ADR. Jeśli treść ADR zmieni się, zanim zespół go zaakceptuje, właściciel powinien zatwierdzić te zmiany.

Gdy zespół zidentyfikuje decyzję architektoniczną i jej właściciela, właściciel ADR przedstawia na początku procesu ADR w stanie **Proposed** (Zaproponowany). ADR w stanie Proposed są gotowe do przeglądu.

Następnie właściciel ADR rozpoczyna proces przeglądu ADR. Celem procesu przeglądu ADR jest rozstrzygnięcie, czy zespół akceptuje ADR, uznaje, że wymaga on poprawek, czy go odrzuca. ADR przegląda zespół projektowy, w tym właściciel. Spotkanie przeglądowe powinno zacząć się od wydzielonego czasu na przeczytanie ADR. Średnio wystarczy 10 do 15 minut. W tym czasie każdy członek zespołu czyta dokument i dodaje komentarze oraz pytania, by oznaczyć niejasne kwestie. Po fazie przeglądu właściciel ADR odczytuje każdy komentarz i omawia go z zespołem.

Jeśli zespół znajdzie punkty do poprawy ADR, stan ADR pozostaje **Proposed**. Właściciel ADR formułuje działania i we współpracy z zespołem przypisuje do każdego z nich wykonawcę. Każdy członek zespołu może wnosić wkład i zamykać punkty działań. Za ponowne zaplanowanie procesu przeglądu odpowiada właściciel ADR.

Zespół może też zdecydować o odrzuceniu ADR. W takim przypadku właściciel ADR dodaje powód odrzucenia, aby zapobiec przyszłym dyskusjom na ten sam temat. Właściciel zmienia stan ADR na **Rejected** (Odrzucony).

Jeśli zespół zatwierdzi ADR, właściciel dodaje znacznik czasu, wersję i listę interesariuszy. Następnie właściciel zmienia stan na **Accepted** (Zaakceptowany).

ADR i tworzony przez nie dziennik decyzji przedstawiają decyzje podjęte przez zespół i zapewniają historię wszystkich decyzji. Zespół w miarę możliwości korzysta z ADR jako punktu odniesienia podczas przeglądów kodu i architektury. Oprócz przeglądów kodu, zadań projektowych i zadań implementacyjnych członkowie zespołu powinni sięgać do ADR przy strategicznych decyzjach dotyczących produktu.

Dobrą praktyką jest, aby każda zmiana w oprogramowaniu przechodziła przegląd koleżeński i wymagała co najmniej jednej akceptacji. Podczas przeglądu kodu recenzent może znaleźć zmiany naruszające jeden lub więcej ADR. W takim przypadku recenzent prosi autora zmiany w kodzie o jego aktualizację i udostępnia link do ADR. Gdy autor zaktualizuje kod, jest on zatwierdzany przez recenzentów i włączany do głównej bazy kodu.


## Proces przeglądu ADR

Zespół powinien traktować ADR jako dokumenty niezmienne po ich zaakceptowaniu lub odrzuceniu. Zmiana istniejącego ADR wymaga utworzenia nowego ADR, ustalenia procesu przeglądu nowego ADR i jego zatwierdzenia. Jeśli zespół zatwierdzi nowy ADR, właściciel powinien zmienić stan starego ADR na **Superseded** (Zastąpiony). 
