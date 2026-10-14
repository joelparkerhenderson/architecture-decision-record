# Przechowywanie sekretów

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
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Podsumowanie


### Problem

Musimy przechowywać sekrety, takie jak hasła, klucze prywatne, tokeny uwierzytelniania itd.

Niektóre sekrety są zorientowane na użytkownika. Na przykład nasz programista chce móc użyć telefonu komórkowego, aby sprawdzić hasło do usługi.

Niektóre sekrety są zorientowane na system. Na przykład nasz potok ciągłego dostarczania musi móc sprawdzić poświadczenia do naszego hostingu w chmurze.


### Decyzja

Bitwarden dla sekretów zorientowanych na użytkownika

Vault by HashiCorp dla sekretów zorientowanych na system.


### Status

Zdecydowano. Jesteśmy otwarci na nowe alternatywy, gdy się pojawią.


## Szczegóły


### Założenia

Do tego celu i w naszym obecnym stanie cenimy wygodę zorientowaną na użytkownika, taką jak użyteczne aplikacje mobilne.

  * Chcemy zapewnić szybki, łatwy dostęp w ruchu, na przykład dla programisty pełniącego dyżur z zakresu inżynierii niezawodności systemów.

  * Chcemy móc udostępniać niektóre sekrety wybranym osobom, na przykład zespołowi.

Nie próbujemy rozwiązać problemu dla jednego dostawcy, takiego jak przechowywanie wszystkich sekretów wyłącznie w Amazon, Azure czy Google.

Nie chcemy podejść doraźnych, takich jak „zapamiętaj to”, „zapisz na karteczce” lub „wymyśl własny sposób przechowywania”.

Nasz model bezpieczeństwa do tego celu akceptuje korzystanie z cenionych dostawców COTS, takich jak narzędzia SaaS do zarządzania hasłami.


### Ograniczenia

Teraz chcemy czegoś, co jest łatwe, tzn. bez potrzeby pisania kodu, instalowania serwerów, podejmowania poważnych zobowiązań i ujednolicania wszystkich.


### Stanowiska

Rozważaliśmy:

1. Gotowe menedżery haseł zorientowane na użytkownika: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG itd.

2. Menedżery haseł COTS zorientowane na system: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Podejścia zorientowane na współdzielenie: użycie wspólnego dokumentu Google, wspólnego kanału Slack, wspólnego folderu sieciowego itd.

4. Doraźne podejścia niskich technologii, takie jak zapamiętywanie, zapisanie notatki lub poleganie na tym, że każdy użytkownik sam wymyśli swój sposób.


### Argument

Bitwarden, LastPass, 1Password i Dashlane to wszystkie gotowe produkty komercyjne.

  * Podobne rodzaje funkcji dla użytkowników, zespołów, organizacji itd.

  * Wersja na komputery dla Windows i Mac oraz wersja mobilna dla Androida i iOS.

  * Rozszerzenia przeglądarek dla Chrome i Firefox, do automatycznego wypełniania formularzy itd.

Bitwarden ma dwie przewagi nad pozostałymi:

  * Bitwarden jest open source, co oznacza, że bezpieczeństwo może być recenzowane przez społeczność, a firma jest szeroko ceniona przez programistów zajmujących się bezpieczeństwem.

  * Anegdoty pracowników branży oprogramowania opisują wyraźną preferencję Bitwardena względem innych.

Typowy dobry opis: https://jcs.org/2017/11/17/bitwarden

Typowa strona z głosowaniem porównawczym: https://stackshare.io/stackups/bitwarden-vs-dashlane

Odkładamy KeyPass, pass, GPG itd., ponieważ wiążą się z dodatkową złożonością. Wszystkie wyglądają na dobre rozwiązania dla użytkowników technicznych. GPG wygląda szczególnie dobrze dla użytkowników technicznych, którzy chcą możliwości międzysystemowych opartych na poleceniach.

Odkładamy KMS, ponieważ wiąże z jednym dostawcą.

Dla potrzeb zorientowanych na system wybieramy Vault, ponieważ opinie są zdumiewająco pozytywne, a HashiCorp ma doskonałe osiągi w oprogramowaniu i wsparciu najwyższej jakości.

Wetujemy podejścia oparte na współdzieleniu, takie jak wspólne dokumenty, wspólne kanały, wspólne foldery sieciowe itd. Nie zapewniają one cech bezpieczeństwa, których chcemy.

Wetujemy doraźne podejścia niskich technologii, ponieważ wszyscy zgadzamy się, że to nie jest droga na dłuższą metę.


### Implikacje

Programiści mogą musieć śledzić sekrety w dwóch miejscach: w Bitwarden dla dostępu zorientowanego na użytkownika i w Vault dla dostępu zorientowanego na system.


## Powiązane


### Powiązane decyzje

Decyzja o wyborze serwera CI/CD musi zawierać dowód możliwości dostępu do sekretów.

Będziemy musieli zdecydować, jak zarządzać sekretami pod względem polityk, rotacji, organizacji itd.


### Powiązane wymagania

Sekrety będą miały powiązane wymagania dotyczące zgodności, audytu oraz wdrażania/wyłączania pracowników w HR.


### Powiązane artefakty

Spodziewamy się, że możemy eksportować niektóre sekrety do zmiennych środowiskowych.


### Powiązane zasady

Łatwo odwracalne.

Łatwo równoległe, tzn. łatwo używać różnych menedżerów haseł.

Tanie w wypróbowaniu, tzn. jest bezpłatna wersja próbna i brak zobowiązań.


## Notatki

Tu notatki z oceny. Wszystkie notatki to publiczne komentarze z różnych forów dyskusyjnych o devops.


### Vault by HashiCorp

Vault to dokładnie to, czego tu potrzebujesz. 

Nie wrzucaj jednak Vaulta od razu na produkcję, najpierw uruchom go w środowisku testowym, ponieważ dokumentacja HashiCorp bywa dość uboga, nawet jeśli ich produkty są wspaniałe.

Bardzo stroma krzywa uczenia się i uruchomienie nie jest trywialne. 

Początkowa konfiguracja jest nieco uciążliwa. Warto jednak, a społeczność wesprze go na tyle, że sobie poradzisz.

Okropna dokumentacja, ale w sieci jest wiele przewodników ludzi, którzy go konfigurowali, i jeśli połączysz kilka z nich, będziesz mieć działającą konfigurację.

Początkowa konfiguracja wymagała majsterkowania z ich wykresami helm (vault i consul). Choć technicznie można użyć wielu innych back-endów, naprawdę nie polecam. Back-end/consul może być maleńki, jeśli nie masz dużo danych do przechowywania.

Zdecydowanie oswój się z CLI, ponieważ GUI jest bardziej proof-of-concept / portalem reklamowym ich wersji enterprise.

Fakt, że nie można go po prostu „wypełnić”, jest uciążliwy. Na przykład jeśli masz 5 pól, musisz ręcznie dodawać każde pole dla każdego elementu. Nie jest więc tak, że wstępnie definiujesz pola dla danej kategorii i wypełniasz je dla wszystkich elementów w tej kategorii; jest raczej tak, że „generujesz wszystko za każdym razem”, co (moim zdaniem) jest upierdliwe.

Możesz też przyjrzeć się goldfish jako UI nad vaultem. Dzięki temu całkiem łatwo przekonać zespół. Mają też demo. 1. Skonfiguruj consul. 2. Skonfiguruj vault wskazujący na consul. 3. Skonfiguruj goldfish wskazujący na vault. 3. Skonfiguruj zadanie cron uruchamiające consul snapshot do kopii zapasowych.



### LastPass

LastPass Teams. Używamy go, ma własne szablony, ACL, niczego moim zdaniem nie brakuje.

Wdrożyłem LastPass w mojej organizacji i oceniam go na C+/B-. Największym problemem ostatnio jest brak niezawodności. W ciągu ostatnich 90 dni było wiele godzin, gdy sejfy były wymuszane w tryb offline. To nieidealne dla mojej organizacji, bo mamy dosłownie ponad 4000 haseł w ponad 20 współdzielonych folderach. Jak można sobie wyobrazić, przy takiej liczbie haseł przynajmniej kilka jest aktualizowanych lub dodawanych codziennie. Mamy plan DR na wypadek, gdyby problemy trwały dłużej niż godzinę lub dwie: skrypt co noc podpisuje i szyfruje zrzut CSV sejfu, który można zaimportować do keepass.

LastPass miał niezgłoszone chwile obniżonej jakości usługi: logowanie „działa”, ale nie pobiera witryn, losowe funkcje w panelu administracyjnym nie działają, a klucze nie są prawidłowo udostępniane dla nowych współdzielonych folderów najwyższego poziomu. Mam specjalnego użytkownika „key push”/backup, który jest w każdej grupie. Zwykle zalogowanie się jako ten użytkownik naprawia problemy z udostępnianiem kluczy, ale nie wtedy, gdy usługa jest obniżona, mimo tego co mówi strona statusu...

Integracja może być łatwa, jeśli masz poprawne ACL w modelu najmniejszych uprawnień, np. jeśli użytkownik ma odczyt i zapis oraz tylko odczyt do wpisu lub folderu, dostaje tylko uprawnienia do odczytu. Niestety ACL w mojej organizacji nie są najlepsze, więc skończyłem na użyciu API provisioningu JSON i ~500 liniach Pythona, ponieważ zależny charakter naszych setek ACL nie odwzorowuje się dobrze na model najmniejszych uprawnień. Skończyło się na pobraniu wszystkich ACL, w których jest użytkownik, i przejściu po zależnościach.

Jeśli Twoja struktura ACL lub grup jest już zbudowana z myślą o najmniejszych uprawnieniach, narzędzie synchronizacji AD/LDAP dla Windows będzie działać dobrze.

Skontaktuj się z ich działem sprzedaży, a załatwią Ci dłuższą wersję próbną Enterprise. Upewnij się, że w pełni rozumiesz jego ograniczenia, zanim zdecydujesz się na zakup. Mieliśmy sporo problemów wzrostu, ale poza awariami lub pogorszeniem po stronie serwera działa niesamowicie płynnie.


### Bitwarden

Bitwarden ma ładne narzędzia wokół siebie (WebUI, CLI, mobilne, desktopowe). Hostowany samodzielnie i dość łatwy w konfiguracji. Dość dobra dokumentacja i narzędzie polecane przez PrivacyTools.


### EnvKey

https://www.envkey.com/ To SaaS. Naprawdę łatwy we wdrożeniu, integracji i zarządzaniu.

Funkcje:

  * Chroni klucze API i poświadczenia.

  * Utrzymuje konfigurację zsynchronizowaną wszędzie.

  * Inteligentne, szyfrowane end-to-end zarządzanie konfiguracją i sekretami. 

  * Zapobiega niebezpiecznemu udostępnianiu i rozrostowi konfiguracji. 

  * Integracja w kilka minut.

Możliwości:

  * Zarządzanie konfiguracją i poziomami dostępu dla wszystkich aplikacji, środowisk i zespołów w jednym miejscu.

  * Konfigurowanie dowolnego środowiska programistycznego lub serwerowego za pomocą jednej zmiennej środowiskowej.

Zalety:

  * Dobra strona główna.

  * Jasna propozycja wartości.

  * Wizualnie doskonała aplikacja internetowa.

  * Wyśmienite dane przykładowe, np. Algolia, AWS, Datadog, GitHub, Stripe itd.

  * Rozmawiałem z założycielem przez 30 minut o firmie, UI itd. Dane brzmi na dobrze poinformowanego, szczerego co do zalet/wad i realnego partnera.

  * Firma to w zasadzie typowa firma Y Combinator z 1 założycielem. W 2018-01 pozyskała 120 tys. USD.

  * Skupienie na dojściu do funkcji enterprise, zwłaszcza przejściu z hostingu EnvKey w chmurze do on-prem lub BYOC.

  * Potencjalna ścieżka: zacząć od EnvKey dla łatwości użycia, a później (lub równolegle) dodać Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant to usługa zarządzania sekretami open source, która zapewnia przyjazne dla użytkownika przechowywanie sekretów i dostęp do nich w bezpieczny sposób, od programistów z Lyft.

Uwierzytelnianie KMS: Confidant rozwiązuje problem kury i jajka w uwierzytelnianiu, używając AWS KMS i IAM, aby role IAM mogły generować bezpieczne tokeny uwierzytelniania, które Confidant może zweryfikować. Confidant zarządza też uprawnieniami KMS dla Twoich ról IAM, co pozwala rolom IAM generować tokeny, które mogą służyć do uwierzytelniania między usługami lub przekazywania zaszyfrowanych wiadomości między usługami.

Szyfrowanie wersjonowanych sekretów w spoczynku: Confidant przechowuje sekrety w trybie tylko dopisywania w DynamoDB, generując unikalny klucz danych KMS dla każdej rewizji każdego sekretu, z użyciem symetrycznej kryptografii uwierzytelnionej Fernet.

Przyjazny dla użytkownika interfejs internetowy do zarządzania sekretami: Confidant udostępnia interfejs internetowy AngularJS, który pozwala użytkownikom końcowym łatwo zarządzać sekretami, odwzorowaniami sekretów na usługi i historią zmian.


### Devolutions Password Server

https://server.devolutions.net/

Zabezpieczaj, zarządzaj i monitoruj dostęp do kont uprzywilejowanych i sesji.

Kompleksowy, wysoce zabezpieczony sejf haseł, który pozwala kontrolować dostęp do kont uprzywilejowanych, a jednocześnie poprawia ogólną widoczność sieci dla administratorów systemów i zapewnia płynne doświadczenie użytkownikom końcowym.

Funkcje: scentralizowany sejf haseł organizacji, prywatny sejf użytkownika, menedżer haseł, wstrzykiwanie poświadczeń,
integracja z Active Directory, kontrola dostępu oparta na rolach, uwierzytelnianie dwuskładnikowe, gotowość dla przedsiębiorstw, ograniczenia IP, możliwości zarządzania, zautomatyzowany generator haseł, dostęp z aplikacji mobilnej, historia haseł, raporty dostępu, alerty e-mail.

  * obsługuje szyfrowanie danych

  * obsługuje wiele schematów uwierzytelniania, w tym LDAP, O365 i użytkowników lokalnych Z obsługą MFA z wielu źródeł

  * wiele repozytoriów/sejfów z precyzyjną kontrolą dostępu dla wielu zespołów

  * nowoczesny interfejs internetowy

  * prywatne sejfy poświadczeń i połączeń dla osobistych poświadczeń/połączeń

  * aplikacje mobilne na iOS/Androida

  * logi audytu dla każdego wpisu: kto/co/kiedy z opcjonalnym pytaniem, dlaczego uzyskuje dostęp

  * konfigurowalne szablony (choć natywnie obsługują setki typów połączeń)

  * mnóstwo kolejnych funkcji oraz klient desktopowy dla Windows/Mac (Remote Desktop Manager), z którym można się synchronizować i który znacznie rozszerza opcje... połączenia jednym kliknięciem

  * ceny nie są takie złe - do 15 użytkowników kosztuje 500 USD rocznie za serwer haseł


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Funkcje wersji lokalnej (on-premise): 

  * Pełna kontrola nad Twoimi systemami i infrastrukturą bezpieczeństwa end-to-end

  * Wdrożenie oprogramowania w lokalnym centrum danych lub we własnej instancji wirtualnej chmury prywatnej

  * Spełnienie wymogów prawnych i regulacyjnych, które wymagają, aby wszystkie dane i systemy znajdowały się lokalnie

Funkcje wersji chmurowej:

  * Model oprogramowania jako usługi pozwala zarejestrować się i zacząć od razu

  * Elastyczna skalowalność w miarę rozwoju

  * Kontrola i redundancja zapewniane przez Azure z umową SLA 99,9% dostępności

Opinie użytkowników:

  * Kiedyś używaliśmy tego produktu. Tak łatwo go było obejść, a reguły działają tylko dla mądrych ludzi. Leniwi lub głupi użytkownicy mogą go łatwo zepsuć w obszarze zespołu. Ceny są negocjowalne, gdy z nimi porozmawiasz.

  * Można go uruchomić na SQL Express i maszynie z Win 7. 

  * Tani.
