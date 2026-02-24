# 架構決策記錄：驗證與授權選項

<!--

ChatGPT prompt:

Explain web application authentication authorization.

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Web 應用程式的驗證（Authentication）與授權（Authorization）是確保應用程式和服務存取安全的兩個關鍵概念。兩者都涉及使用者身分以及權限的授予方式，但各自關注不同的面向：

- **驗證（Authentication）**是驗證使用者或系統身分的過程。
- **授權（Authorization）**是確定已驗證的使用者或系統可以存取哪些資源或執行哪些操作的過程。

接下來，讓我們深入了解您所提到的特定協定和技術，這些是現代 Web 應用程式中常用於管理驗證與授權的方案。

### 1. **OAuth（開放授權，Open Authorization）**

**OAuth** 是一種開放的授權標準。它允許使用者在不分享其憑證的情況下，授予第三方應用程式對其資源的有限存取權。核心概念是**委託存取（Delegated Access）**。OAuth 通常用於使用者可以登入第三方服務的場景（例如使用 Google 帳號登入），而無需直接向第三方提供其帳號密碼。

- **流程**：OAuth 通常遵循**基於權杖（Token-based）**的流程，由授權伺服器向第三方應用程式發放存取權杖（Access Token）。此權杖代表使用者的權限，應用程式使用它來從 API 存取使用者的資料或資源。
- **範例**：使用者使用其 Google 帳號登入第三方應用程式。Google 驗證使用者身分後，授予一個權杖，允許第三方應用程式存取部分 Google 資料（例如 Google 日曆）。

OAuth **不**直接處理驗證；它專注於授予存取權。對於驗證，OAuth 通常與其他協定搭配使用，例如 **OpenID Connect**。

### 2. **OpenID Connect（OIDC）**

**OpenID Connect（OIDC）**是建立在 **OAuth 2.0** 之上的身分層，為 OAuth 的授權功能加入了驗證能力。本質上，OpenID Connect 擴展了 OAuth 以處理**使用者驗證**，並提供了標準化的方式讓應用程式驗證使用者的身分。

- **流程**：當使用者使用 OpenID Connect 登入時，第三方應用程式會請求一個 ID 權杖（ID Token）（除了 OAuth 存取權杖之外）。ID 權杖包含使用者的相關資訊（例如使用者名稱、電子郵件及其他宣告）。這使應用程式能夠知道使用者是誰，以及他們是否已通過驗證。
- **範例**：使用 Google 帳號登入 Slack 等服務（Google 作為 OpenID Connect 提供者）涉及透過 OpenID Connect 進行驗證，而 OAuth 負責管理對 Google 資源的存取。

OIDC 使第三方應用程式能更容易地**驗證使用者身分**，同時仍允許對這些應用程式可存取的資源進行細粒度控制。

### 3. **SAML（安全性聲明標記語言，Security Assertion Markup Language）**

**SAML** 是一種較舊的、基於 XML 的標準，用於在各方之間交換驗證和授權資料，特別是在**單一登入（Single Sign-On, SSO）**場景中。它主要用於企業環境，使使用者只需驗證一次即可存取多個應用程式，無需重新輸入憑證。

- **流程**：使用者首先向身分提供者（Identity Provider, IdP）進行驗證。IdP 產生一個已簽署的 **SAML 斷言（Assertion）**，包含使用者的身分及相關屬性。此斷言被傳送至服務提供者（Service Provider, SP），SP 使用它來授權對應用程式的存取。
- **範例**：員工登入其企業入口網站（IdP），然後自動登入其他系統如電子郵件、CRM 等，無需重新輸入憑證。驗證過程基於 IdP 傳送的 SAML 斷言。

SAML 常用於**企業 SSO 解決方案**，在企業環境的 Web 應用程式中表現良好，但相較於 OAuth/OIDC，對行動裝置的支援較差。

### 4. **WS-Federation（Web 服務聯邦）**

**WS-Federation** 是另一種用於**單一登入（SSO）**的協定，尤其在以 Microsoft 為基礎的企業環境中使用。它是 **WS-*（Web Services）**規範系列的一部分，允許在不同安全域（例如不同組織之間或不同服務之間）進行身分聯邦。

- **流程**：WS-Federation 允許**受信任的身分提供者（IdP）**驗證使用者身分並發放權杖，服務提供者可以使用這些權杖進行授權。它類似於 SAML，但通常用於高度依賴 Microsoft 技術的場景。
- **範例**：使用者登入由 Microsoft Azure Active Directory（AD）託管的企業應用程式，其身分可用於存取其他聯邦服務，包括第三方供應商託管的應用程式。

雖然 WS-Federation 在許多現代 Web 環境中已被 OAuth 2.0 和 OpenID Connect 等較新的協定所取代，但在舊有系統中仍被使用，尤其是在以 Microsoft 為核心的企業中。

### 5. **LDAP（輕量級目錄存取協定，Lightweight Directory Access Protocol）**

**LDAP** 是一種用於存取和管理目錄服務的協定，常用於在集中式目錄（通常稱為**目錄服務，Directory Service**）中**儲存使用者憑證**和管理存取控制。LDAP 本身並非專門處理驗證或授權，而是用於儲存和擷取身分資料，這些資料隨後在驗證和授權過程中被使用。

- **驗證**：LDAP 允許應用程式透過查詢目錄服務中的憑證（如密碼）來驗證使用者身分。
- **授權**：它還管理使用者角色和權限，協助確定使用者是否有權存取特定資源。
- **範例**：許多企業使用基於 LDAP 的目錄（例如 **Active Directory**）進行驗證和授權，尤其是在 Windows 環境中。

LDAP 對於企業管理內部系統的使用者存取至關重要，但在現代 Web 環境中，LDAP 通常與 SAML 或 OAuth 等其他協定整合，以實現更完整的身分管理。

### 6. **社群 SSO 提供者（Social SSO Providers）**

社群**單一登入（SSO）**提供者如 **Facebook**、**Google**、**Twitter**、**GitHub** 等，允許使用者使用其社群媒體憑證登入第三方應用程式。這是一種**基於 OAuth 的驗證**方式，其中第三方服務（例如 Google）作為身分提供者。

- **流程**：使用者點擊「使用 Google 登入」（舉例）。應用程式重新導向至 Google，使用者在此登入（如尚未登入）。然後 Google 向第三方應用程式提供存取權杖或 ID 權杖，可用於驗證使用者身分，並可能存取其資料。
- **範例**：許多應用程式允許您使用 Google 或 Facebook 憑證登入。應用程式在幕後使用 OAuth 或 OpenID Connect 來驗證您的身分，並在某些情況下存取特定的社群媒體資料。

社群 SSO 是一種便利且廣泛採用的驗證方法，因為它減少了使用者的摩擦——使用者可能不想再建立一組帳號密碼。

---

### 差異摘要：

- **OAuth**：用於授權，允許第三方應用程式在不暴露憑證的情況下存取使用者資料。
- **OpenID Connect**：擴展 OAuth 以提供驗證功能，使應用程式能驗證使用者身分。
- **SAML**：基於 XML 的協定，用於 SSO，常見於企業環境。
- **WS-Federation**：Microsoft 專屬的身分聯邦協定，用於舊有系統。
- **LDAP**：用於查詢目錄服務以驗證使用者身分和管理授權的協定。
- **社群 SSO 提供者**：基於 OAuth 的系統（如 Google、Facebook），允許第三方應用程式使用社群媒體憑證驗證使用者身分。

每種技術都有其自身的優勢和使用情境，在現代應用程式中，您可能會看到它們的組合被用於安全性的不同面向（例如 OAuth/OIDC 用於 API 存取，SAML 用於企業 SSO）。
