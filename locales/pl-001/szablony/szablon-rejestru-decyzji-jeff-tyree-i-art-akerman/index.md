# Szablon rejestru decyzji autorstwa Jeffa Tyree’a i Arta Akermana

To jest szablon opisu decyzji architektonicznej opublikowany w ["Architecture Decisions: Demystifying Architecture" autorstwa Jeffa Tyree’a i Arta Akermana, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Problem (Issue)**: Opisz problem projektowy architektury, którym się zajmujesz, nie pozostawiając wątpliwości, dlaczego zajmujesz się nim teraz. Stosując podejście minimalistyczne, rozwiązuj i dokumentuj tylko te problemy, którymi trzeba się zająć w poszczególnych momentach cyklu życia.

* **Decyzja (Decision)**: Jasno określ kierunek architektury, czyli wybrane stanowisko.

* **Status**: Status decyzji, na przykład oczekująca, podjęta lub zatwierdzona.

* **Grupa (Group)**: Możesz użyć prostego grupowania — na przykład integracja, prezentacja, dane itd. — aby uporządkować zbiór decyzji. Możesz też użyć bardziej zaawansowanej ontologii architektury, takiej jak ontologia Johna Kyaruzi i Jana van Katwijka, która zawiera bardziej abstrakcyjne kategorie, takie jak zdarzenie, kalendarz i lokalizacja. Na przykład według tej ontologii decyzje dotyczące zdarzeń, w których system wymaga informacji, grupowałbyś pod kategorią zdarzenie.

* **Założenia (Assumptions)**: Jasno opisz założenia dotyczące środowiska, w którym podejmujesz decyzję — koszt, harmonogram, technologia itd. Zwróć uwagę, że ograniczenia środowiska (takie jak przyjęte standardy technologiczne, architektura korporacyjna, powszechnie stosowane wzorce itd.) mogą ograniczać rozważane przez Ciebie alternatywy.

* **Ograniczenia (Constraints)**: Opisz wszelkie dodatkowe ograniczenia dla środowiska, które może narzucić wybrana alternatywa (decyzja).

* **Stanowiska (Positions)**: Wymień stanowiska (realne opcje lub alternatywy), które rozważałeś. Często wymagają one długich wyjaśnień, czasem nawet modeli i diagramów. Nie jest to lista wyczerpująca. Jednak nie chcesz usłyszeć podczas końcowego przeglądu pytania „Czy myślałeś o...?”; prowadzi to do utraty wiarygodności i podważania innych decyzji architektonicznych. Ta sekcja pomaga też upewnić się, że wysłuchałeś opinii innych; wyraźne przedstawienie innych opinii pomaga pozyskać ich zwolenników dla Twojej decyzji.

* **Argument**: Przedstaw, dlaczego wybrałeś dane stanowisko, uwzględniając takie kwestie jak koszt wdrożenia, całkowity koszt posiadania, czas wprowadzenia na rynek i dostępność wymaganych zasobów programistycznych. Jest to prawdopodobnie równie ważne jak sama decyzja.

* **Implikacje (Implications)**: Decyzja niesie wiele implikacji, jak wskazuje metamodel REMAP. Na przykład decyzja może wprowadzić potrzebę podjęcia innych decyzji, utworzyć nowe wymagania lub zmienić istniejące, narzucić dodatkowe ograniczenia dla środowiska, wymagać renegocjacji zakresu lub harmonogramu z klientami albo wymagać dodatkowych szkoleń personelu. Jasne zrozumienie i przedstawienie implikacji decyzji może być bardzo skuteczne w zdobywaniu poparcia i tworzeniu mapy drogowej realizacji architektury.

* **Powiązane decyzje (Related decisions)**: Oczywiste jest, że wiele decyzji jest ze sobą powiązanych; możesz je tutaj wymienić. Jednak w praktyce okazało się, że bardziej przydatne są macierz identyfikowalności, drzewa decyzyjne lub metamodele. Metamodele są użyteczne do diagramowego pokazywania złożonych relacji (na przykład modele Rose).

* **Powiązane wymagania (Related requirements)**: Decyzje powinny wynikać z potrzeb biznesu. Aby pokazać rozliczalność, jawnie odwzoruj swoje decyzje na cele lub wymagania. Możesz tu wymienić te powiązane wymagania, ale wygodniej jest odwoływać się do macierzy identyfikowalności. Możesz ocenić wkład każdej decyzji architektonicznej w spełnienie każdego wymagania, a następnie ocenić, jak dobrze wymaganie jest spełnione przez wszystkie decyzje. Jeśli decyzja nie przyczynia się do spełnienia żadnego wymagania, nie podejmuj tej decyzji.

* **Powiązane artefakty (Related artifacts)**: Wymień powiązane dokumenty architektury, projektu lub zakresu, na które ta decyzja wpływa.

* **Powiązane zasady (Related principles)**: Jeśli przedsiębiorstwo ma uzgodniony zbiór zasad, upewnij się, że decyzja jest zgodna z jedną lub kilkoma z nich. Pomaga to zapewnić spójność w poszczególnych dziedzinach lub systemach.

* **Notatki (Notes)**: Ponieważ proces podejmowania decyzji może trwać tygodniami, przydatne okazało się zapisywanie notatek i problemów, które zespół omawia w trakcie upowszechniania decyzji.

