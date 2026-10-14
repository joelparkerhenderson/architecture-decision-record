# Rejestr decyzji architektonicznych: opcje uwierzytelniania i autoryzacji

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Uwierzytelnianie i autoryzacja aplikacji internetowych to dwa kluczowe pojęcia w zabezpieczaniu dostępu do aplikacji i usług. Oba dotyczą tożsamości użytkowników i sposobu nadawania uprawnień, ale skupiają się na różnych aspektach:

- **Uwierzytelnianie** (ang. authentication) to proces weryfikacji tożsamości użytkownika lub systemu.
- **Autoryzacja** (ang. authorization) to proces ustalania, do jakich zasobów lub działań uwierzytelniony użytkownik lub system ma dostęp.

Przyjrzyjmy się teraz konkretnym protokołom i technologiom, o których wspomniałeś i które są powszechnie używane we współczesnych aplikacjach internetowych do zarządzania uwierzytelnianiem i autoryzacją.

### 1. **OAuth (Open Authorization)**

**OAuth** to otwarty standard autoryzacji. Pozwala użytkownikowi przyznać aplikacji zewnętrznej ograniczony dostęp do swoich zasobów bez udostępniania poświadczeń. Kluczowa idea to **delegowany dostęp**. OAuth jest często używany w sytuacjach, gdy użytkownicy mogą logować się do usługi zewnętrznej (np. logowanie przez Google) bez bezpośredniego podawania nazwy użytkownika i hasła podmiotowi trzeciemu.

- **Przepływ**: OAuth zwykle opiera się na przepływie **opartym na tokenach**, w którym serwer autoryzacji wydaje token dostępu aplikacji zewnętrznej. Ten token reprezentuje uprawnienia użytkownika, a aplikacja używa go do uzyskania dostępu do danych lub zasobów użytkownika z API.
- **Przykład**: Użytkownik loguje się do aplikacji zewnętrznej za pomocą konta Google. Google weryfikuje tożsamość użytkownika, a następnie wydaje token, który pozwala aplikacji zewnętrznej uzyskać dostęp do niektórych danych Google (np. Kalendarza Google).

OAuth **nie** obsługuje bezpośrednio uwierzytelniania; chodzi w nim o przyznawanie dostępu. Do uwierzytelniania OAuth jest często łączony z innymi protokołami, takimi jak **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** to warstwa tożsamości zbudowana na **OAuth 2.0**, która dodaje uwierzytelnianie do możliwości autoryzacyjnych OAuth. Zasadniczo OpenID Connect rozszerza OAuth o obsługę **uwierzytelniania użytkowników** i zapewnia ustandaryzowany sposób weryfikacji tożsamości użytkownika przez aplikacje.

- **Przepływ**: Gdy użytkownik loguje się przez OpenID Connect, aplikacja zewnętrzna żąda tokenu ID (oprócz tokenu dostępu OAuth). Token ID zawiera informacje o użytkowniku (takie jak nazwa użytkownika, e-mail i inne roszczenia). Dzięki temu aplikacja wie, kim jest użytkownik i czy jest uwierzytelniony.
- **Przykład**: Logowanie do usługi takiej jak Slack za pomocą konta Google (Google jako dostawca OpenID Connect) wiąże się z uwierzytelnieniem przez OpenID Connect, podczas gdy OAuth zarządza dostępem do Twoich zasobów Google.

OIDC ułatwia aplikacjom zewnętrznym **uwierzytelnianie użytkowników**, a jednocześnie pozwala na szczegółową kontrolę nad tym, do jakich zasobów te aplikacje mają dostęp.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** to starszy standard oparty na XML, używany do wymiany danych uwierzytelniania i autoryzacji między stronami, szczególnie w scenariuszach **jednokrotnego logowania (Single Sign-On, SSO)**. Jest używany głównie w środowiskach korporacyjnych, aby użytkownicy mogli uwierzytelnić się raz i uzyskać dostęp do wielu aplikacji bez ponownego wpisywania poświadczeń.

- **Przepływ**: Użytkownik najpierw uwierzytelnia się u dostawcy tożsamości (IdP). IdP generuje podpisaną **asercję SAML**, zawierającą tożsamość użytkownika i powiązane atrybuty. Asercja jest wysyłana do dostawcy usługi (SP), który używa jej do autoryzacji dostępu do aplikacji.
- **Przykład**: Pracownik loguje się do firmowego portalu (IdP) i jest automatycznie logowany do innych systemów, takich jak poczta e-mail, CRM itd., bez ponownego wpisywania poświadczeń. Proces uwierzytelniania opiera się na asercji SAML wysłanej przez IdP.

SAML jest powszechnie używany w **korporacyjnych rozwiązaniach SSO** i dobrze sprawdza się w aplikacjach internetowych w środowiskach firmowych, ale jest mniej przyjazny dla urządzeń mobilnych niż OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** to kolejny protokół używany do **jednokrotnego logowania (SSO)**, zwłaszcza w środowiskach korporacyjnych opartych na produktach Microsoft. Jest częścią rodziny specyfikacji **WS-* (Web Services)** i umożliwia federację tożsamości między różnymi domenami bezpieczeństwa (na przykład między różnymi organizacjami lub różnymi usługami).

- **Przepływ**: WS-Federation pozwala **zaufanemu dostawcy tożsamości (IdP)** uwierzytelniać użytkowników i wydawać tokeny, których dostawca usługi może użyć do autoryzacji. Jest podobny do SAML, ale często używany w scenariuszach silnie opartych na technologiach Microsoft.
- **Przykład**: Użytkownik loguje się do aplikacji korporacyjnej hostowanej w Microsoft Azure Active Directory (AD), a jego tożsamość może być użyta do uzyskania dostępu do innych sfederowanych usług, w tym aplikacji hostowanych przez zewnętrznych dostawców.

Choć WS-Federation jest w wielu nowoczesnych środowiskach internetowych w dużej mierze zastępowany nowszymi protokołami, takimi jak OAuth 2.0 i OpenID Connect, nadal jest używany w systemach starszego typu, zwłaszcza w przedsiębiorstwach opartych na produktach Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** to protokół używany do dostępu do usług katalogowych i zarządzania nimi, powszechnie stosowany do **przechowywania poświadczeń użytkowników** i zarządzania kontrolą dostępu w scentralizowanym katalogu (często nazywanym **usługą katalogową**). LDAP nie dotyczy konkretnie uwierzytelniania ani autoryzacji, ale służy do przechowywania i pobierania danych tożsamości, które są następnie używane w tych procesach.

- **Uwierzytelnianie**: LDAP pozwala aplikacji uwierzytelniać użytkowników przez zapytanie usługi katalogowej o poświadczenia (takie jak hasła).
- **Autoryzacja**: Zarządza też rolami i uprawnieniami użytkowników, pomagając ustalić, czy użytkownik ma dostęp do określonych zasobów.
- **Przykład**: Wiele przedsiębiorstw używa katalogów opartych na LDAP (np. **Active Directory**) do uwierzytelniania i autoryzacji, zwłaszcza w środowiskach Windows.

LDAP ma kluczowe znaczenie dla przedsiębiorstw w zarządzaniu dostępem użytkowników do systemów wewnętrznych, ale we współczesnym kontekście internetowym LDAP jest często integrowany z innymi protokołami, takimi jak SAML lub OAuth, aby uzyskać pełniejsze zarządzanie tożsamością.

### 6. **Dostawcy społecznościowego SSO**

Dostawcy społecznościowego **jednokrotnego logowania (SSO)**, tacy jak **Facebook**, **Google**, **Twitter**, **GitHub** i inni, pozwalają użytkownikom uwierzytelniać się w aplikacjach zewnętrznych za pomocą poświadczeń z mediów społecznościowych. Jest to rodzaj **uwierzytelniania opartego na OAuth**, w którym usługa zewnętrzna (np. Google) jest dostawcą tożsamości.

- **Przepływ**: Użytkownik klika „Zaloguj się przez Google” (na przykład). Aplikacja przekierowuje do Google, gdzie użytkownik się loguje (jeśli nie jest jeszcze zalogowany). Następnie Google przekazuje aplikacji zewnętrznej token dostępu lub token ID, który może posłużyć do uwierzytelnienia użytkownika i ewentualnie uzyskania dostępu do jego danych.
- **Przykład**: Wiele aplikacji pozwala zalogować się za pomocą poświadczeń Google lub Facebooka. Aplikacja używa OAuth lub OpenID Connect w tle, aby zweryfikować Twoją tożsamość i w niektórych przypadkach uzyskać dostęp do określonych danych z mediów społecznościowych.

Społecznościowe SSO to wygodna i szeroko przyjęta metoda uwierzytelniania, ponieważ zmniejsza tarcie dla użytkowników, którzy mogą nie chcieć tworzyć kolejnej nazwy użytkownika i hasła.

---

### Podsumowanie różnic:

- **OAuth**: Używany do autoryzacji, pozwala aplikacjom zewnętrznym uzyskać dostęp do danych użytkownika bez ujawniania poświadczeń.
- **OpenID Connect**: Rozszerza OAuth o uwierzytelnianie, umożliwiając aplikacjom weryfikację tożsamości użytkownika.
- **SAML**: Protokół oparty na XML używany do SSO, często w środowiskach korporacyjnych.
- **WS-Federation**: Protokół firmy Microsoft do federacji tożsamości, używany w systemach starszego typu.
- **LDAP**: Protokół do odpytywania usług katalogowych w celu uwierzytelniania użytkowników i zarządzania autoryzacją.
- **Dostawcy społecznościowego SSO**: Systemy oparte na OAuth (jak Google, Facebook), które pozwalają aplikacjom zewnętrznym uwierzytelniać użytkowników za pomocą poświadczeń z mediów społecznościowych.

Każda z tych technologii ma swoje mocne strony i zastosowania, a we współczesnych aplikacjach można spotkać ich kombinację stosowaną do różnych aspektów bezpieczeństwa (np. OAuth/OIDC do dostępu do API, SAML do korporacyjnego SSO).
