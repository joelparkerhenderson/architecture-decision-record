# Szablon rejestru decyzji architektonicznych (ADR) <!-- Replace with ADR title -->

To jest szablon ADR dla EdgeX Foundry.

Źródło: https://docs.edgexfoundry.org/2.3/design/adr/template/


### Zgłaszający

Wymień osoby zgłaszające ADR.

Format:

- Imię i nazwisko (Organizacja)


## Dziennik zmian

Wymień zmiany w dokumencie, w tym stan, datę i adres URL PR.

Stan to jeden z: oczekujący (pending), zatwierdzony (approved), zmieniony (amended), wycofany (deprecated).

Data to ciąg w formacie ISO 8601 (RRRR-MM-DD).

PR to pull request, który wprowadził zmianę, zawierający informacje takie jak różnice, współautorzy i recenzenci.

Format:

- \[Status ADR, np. approved, amended itd.\]\(URL pull requesta\) RRRR-MM-DD


## Przywołane przypadki użycia

Wymień wszystkie istotne dokumenty przypadków użycia / wymagań.

ADR wymaga co najmniej jednego istotnego, zatwierdzonego przypadku użycia.

Format:

- \[Nazwa przypadku użycia\]\(URL\)

Dodaj wyjaśnienia, jeśli ADR nie odpowiada na wszystkie wymagania przypadku użycia.


## Kontekst

Opisz:

- dlaczego projekt jest istotny dla architektury i uzasadnia ADR (zamiast prostego zgłoszenia i PR naprawiającego problem)

- ogólne podejście projektowe (szczegóły opisane w proponowanym projekcie poniżej)


## Proponowany projekt

Szczegóły projektu (w miarę możliwości bez wchodzenia w implementację).

Zarys:

- usługi/moduły, na które projekt wpłynie (zmiana)

- nowe usługi/moduły do dodania

- wpływ na model i DTO (zmiany/dodania/usunięcia)

- wpływ na API (zmiany/dodania/usunięcia)

- wpływ na ogólną konfigurację (utworzenie nowych sekcji, zmiany/dodania/usunięcia)

- wpływ na devops


## Rozważania

Opisz alternatywy, wątpliwości, kwestie poboczne lub powiązane oraz pytania, które pojawiły się w debacie nad ADR. 

Wskaż, czy i jak je rozstrzygnięto lub złagodzono.


## Decyzja

Opisz wszelkie uzgodnione ważne szczegóły implementacji, zastrzeżenia, kwestie na przyszłość oraz pozostałe lub odroczone problemy projektowe.

Opisz wszelkie części wymagań niespełnione przez proponowany projekt.


## Inne powiązane ADR

Wymień wszystkie istotne ADR — takie jak decyzja projektowa dla podkomponentu funkcji, projekt wycofany w wyniku tego projektu itd. 

Format:

- \[Tytuł ADR\]\(URL\) - Znaczenie


## Odniesienia

Wymień dodatkowe odniesienia.

Format:

- \[Tytuł\]\(URL\)

