# Rejestr decyzji architektonicznych: edytory kodu

## Kontekst

Edytory kodu to podstawowe narzędzie programistów do pisania i edycji kodu. Dostępnych jest wiele edytorów kodu, z których każdy ma własny zestaw funkcji, zalet i wad. Celem tego ADR jest udokumentowanie decyzji architektonicznych podjętych dla edytorów kodu.

## Priorytety

Architektura edytorów kodu powinna uwzględniać następujące priorytety:

* **Modularność**: Edytor kodu powinien być zaprojektowany modułowo, aby programiści mogli go dostosowywać i rozszerzać w razie potrzeby. Pozwala to na elastyczną architekturę, która dostosowuje się do potrzeb różnych programistów i zespołów.

* **Wydajność**: Edytor kodu powinien być wydajny i responsywny, aby programiści mogli pracować efektywnie, bez spowalniania przez używane narzędzie.

* **Interfejs użytkownika**: Interfejs użytkownika powinien być intuicyjny i łatwy w użyciu, aby programiści mogli skupić się na kodzie, a nie zmagać się z edytorem.

* **Rozszerzalność**: Edytor kodu powinien być zaprojektowany tak, aby umożliwiał łatwe rozszerzanie za pomocą wtyczek i integracji firm trzecich.

* **Zgodność**: Edytor kodu powinien być zgodny z szeroką gamą języków programowania i technologii, co czyni go użytecznym narzędziem dla szerokiego grona programistów.

## Decyzja

Na podstawie tych priorytetów architektura edytorów kodu powinna być zaprojektowana z następującymi komponentami:

* **Rdzeń**: Ten komponent zapewnia podstawową funkcjonalność edytora kodu, taką jak podświetlanie składni, edycja tekstu i zarządzanie plikami.

* **UI**: Ten komponent zapewnia interfejs użytkownika edytora kodu, w tym menu, paski narzędzi i skróty klawiszowe.

* **Wtyczki**: Ten komponent pozwala programistom rozszerzać funkcjonalność edytora kodu przez instalowanie wtyczek firm trzecich. Wtyczki mogą zapewniać dodatkowe funkcje, takie jak uzupełnianie kodu, linting czy debugowanie.

* **Integracje**: Ten komponent pozwala edytorowi kodu integrować się z innymi narzędziami i technologiami, takimi jak systemy kontroli wersji, systemy budowania lub narzędzia do debugowania.

## Uzasadnienie

Modularność edytora kodu pozwala programistom dostosowywać go i rozszerzać w razie potrzeby. Jest to ważne, ponieważ różni programiści i zespoły mają różne potrzeby i przepływy pracy, a elastyczna architektura może te różnice uwzględnić.

* **Wydajność**: kluczowa, ponieważ programiści muszą móc pracować efektywnie, bez spowalniania przez swoje narzędzia. Wydajny edytor kodu jest niezbędny dla produktywności i może pomagać programistom utrzymać skupienie i koncentrację.

* **UI**: ważny, ponieważ pozwala programistom skupić się na kodzie, a nie zmagać się z edytorem. Może to prowadzić do lepszej produktywności i mniejszej frustracji programistów.

* **Rozszerzalność**: potężna, ponieważ pozwala dostosować edytor kodu do różnych potrzeb i przepływów pracy. Wtyczki i integracje firm trzecich mogą zapewniać dodatkowe funkcje i możliwości, których nie ma w podstawowym edytorze.

* **Zgodność**: cenna, ponieważ pozwala używać edytora kodu z szeroką gamą języków programowania i technologii. Czyni to edytor bardziej użytecznym narzędziem dla szerokiego grona programistów.

Komponenty rdzenia, wtyczek, integracji i UI zapewniają wyraźny podział odpowiedzialności i umożliwiają modułową architekturę, którą można łatwo rozszerzać i dostosowywać. Ta architektura jest elastyczna, wydajna i zgodna z szeroką gamą języków programowania i technologii, co czyni ją użytecznym narzędziem dla programistów.