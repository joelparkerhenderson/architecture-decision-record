
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
