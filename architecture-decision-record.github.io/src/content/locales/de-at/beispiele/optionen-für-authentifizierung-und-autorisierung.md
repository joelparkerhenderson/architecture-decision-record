# Architecture Decision Record: Optionen für Authentifizierung und Autorisierung

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Authentifizierung und Autorisierung von Webanwendungen sind zwei entscheidende Konzepte zum Schutz des Zugriffs auf Anwendungen und Dienste. Beide befassen sich mit der Identität von Benutzern und damit, wie Berechtigungen erteilt werden, konzentrieren sich aber auf unterschiedliche Aspekte:

- **Authentifizierung** ist der Vorgang, die Identität eines Benutzers oder Systems zu überprüfen.
- **Autorisierung** ist der Vorgang, zu bestimmen, auf welche Ressourcen oder Aktionen der authentifizierte Benutzer oder das authentifizierte System zugreifen darf.

Nun wollen wir uns die konkreten Protokolle und Technologien ansehen, die Sie genannt haben und die häufig in modernen Webanwendungen zur Verwaltung von Authentifizierung und Autorisierung verwendet werden.

### 1. **OAuth (Open Authorization)**

**OAuth** ist ein offener Standard für die Autorisierung. Er ermöglicht es einem Benutzer, einer Drittanbieteranwendung eingeschränkten Zugriff auf seine Ressourcen zu gewähren, ohne seine Zugangsdaten preiszugeben. Die Kernidee ist der **delegierte Zugriff**. OAuth wird häufig in Situationen eingesetzt, in denen Benutzer sich bei einem Drittanbieterdienst anmelden können (z. B. Anmeldung mit Google), ohne dem Drittanbieter direkt ihren Benutzernamen und ihr Passwort zu geben.

- **Ablauf**: OAuth folgt typischerweise einem **tokenbasierten** Ablauf, bei dem ein Autorisierungsserver der Drittanbieteranwendung ein Zugriffstoken ausstellt. Dieses Token repräsentiert die Berechtigungen des Benutzers, und die Anwendung nutzt es, um über eine API auf die Daten oder Ressourcen des Benutzers zuzugreifen.
- **Beispiel**: Ein Benutzer meldet sich mit seinem Google-Konto bei einer Drittanbieter-App an. Google überprüft die Identität des Benutzers und stellt dann ein Token aus, das der Drittanbieter-App den Zugriff auf einige Google-Daten (z. B. Google Kalender) erlaubt.

OAuth übernimmt die Authentifizierung **nicht** direkt; es geht um das Gewähren von Zugriff. Für die Authentifizierung wird OAuth oft mit anderen Protokollen wie **OpenID Connect** kombiniert.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** ist eine Identitätsschicht, die auf **OAuth 2.0** aufbaut und den Autorisierungsfähigkeiten von OAuth eine Authentifizierung hinzufügt. Im Wesentlichen erweitert OpenID Connect OAuth um die **Benutzerauthentifizierung** und bietet Anwendungen eine standardisierte Möglichkeit, die Identität eines Benutzers zu überprüfen.

- **Ablauf**: Wenn sich ein Benutzer mit OpenID Connect anmeldet, fordert die Drittanbieteranwendung (zusätzlich zum OAuth-Zugriffstoken) ein ID-Token an. Das ID-Token enthält Informationen über den Benutzer (etwa Benutzername, E-Mail-Adresse und andere Claims). So kann die Anwendung wissen, wer der Benutzer ist und ob er authentifiziert ist.
- **Beispiel**: Die Anmeldung bei einem Dienst wie Slack mit Ihrem Google-Konto (Google ist der OpenID-Connect-Anbieter) erfolgt per Authentifizierung über OpenID Connect, während OAuth den Zugriff auf Ihre Google-Ressourcen verwaltet.

OIDC macht es Drittanbieter-Apps leichter, **Benutzer zu authentifizieren**, und erlaubt gleichzeitig eine fein abgestufte Kontrolle darüber, auf welche Ressourcen diese Apps zugreifen dürfen.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** ist ein älterer, XML-basierter Standard zum Austausch von Authentifizierungs- und Autorisierungsdaten zwischen Parteien, insbesondere in **Single-Sign-On-(SSO)**-Szenarien. Er wird vor allem in Unternehmensumgebungen verwendet, damit Benutzer sich einmal authentifizieren und auf mehrere Anwendungen zugreifen können, ohne ihre Zugangsdaten erneut einzugeben.

- **Ablauf**: Der Benutzer authentifiziert sich zunächst bei einem Identitätsanbieter (IdP). Der IdP erzeugt eine signierte **SAML-Assertion**, die die Identität des Benutzers und zugehörige Attribute enthält. Die Assertion wird an den Dienstanbieter (SP) gesendet, der sie nutzt, um den Zugriff auf die Anwendung zu autorisieren.
- **Beispiel**: Ein Mitarbeiter meldet sich in seinem Unternehmensportal (dem IdP) an und wird automatisch bei anderen Systemen wie E-Mail, CRM usw. angemeldet, ohne seine Zugangsdaten erneut einzugeben. Der Authentifizierungsprozess beruht auf der vom IdP gesendeten SAML-Assertion.

SAML wird häufig in **Unternehmens-SSO-Lösungen** verwendet und funktioniert gut für Webanwendungen in Unternehmensumgebungen, ist aber im Vergleich zu OAuth/OIDC weniger mobilfreundlich.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** ist ein weiteres Protokoll für **Single Sign-On (SSO)**, insbesondere in Microsoft-basierten Unternehmensumgebungen. Es ist Teil der **WS-* (Web Services)**-Spezifikationsfamilie und ermöglicht Identitätsföderation über verschiedene Sicherheitsdomänen hinweg (etwa zwischen verschiedenen Organisationen oder zwischen verschiedenen Diensten).

- **Ablauf**: WS-Federation erlaubt einem **vertrauenswürdigen Identitätsanbieter (IdP)**, Benutzer zu authentifizieren und Token auszustellen, die der Dienstanbieter zur Autorisierung nutzen kann. Es ähnelt SAML, wird aber oft in Szenarien verwendet, die stark auf Microsoft-Technologien setzen.
- **Beispiel**: Ein Benutzer meldet sich bei einer Unternehmensanwendung an, die von Microsoft Azure Active Directory (AD) gehostet wird, und seine Identität kann für den Zugriff auf andere föderierte Dienste genutzt werden, einschließlich Anwendungen, die von Drittanbietern gehostet werden.

Obwohl WS-Federation in vielen modernen Webumgebungen weitgehend durch neuere Protokolle wie OAuth 2.0 und OpenID Connect ersetzt wurde, wird es in Altsystemen weiterhin verwendet, besonders in Microsoft-zentrierten Unternehmen.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** ist ein Protokoll für den Zugriff auf und die Verwaltung von Verzeichnisdiensten, das häufig zum **Speichern von Benutzerzugangsdaten** und zur Verwaltung der Zugriffskontrolle in einem zentralen Verzeichnis (oft **Verzeichnisdienst** genannt) verwendet wird. LDAP befasst sich nicht speziell mit Authentifizierung oder Autorisierung, sondern dient zum Speichern und Abrufen von Identitätsdaten, die dann in diesen Prozessen genutzt werden.

- **Authentifizierung**: LDAP erlaubt einer Anwendung, Benutzer zu authentifizieren, indem sie den Verzeichnisdienst nach Zugangsdaten (etwa Passwörtern) abfragt.
- **Autorisierung**: Es verwaltet außerdem Benutzerrollen und Berechtigungen und hilft zu bestimmen, ob ein Benutzer Zugriff auf bestimmte Ressourcen hat.
- **Beispiel**: Viele Unternehmen nutzen LDAP-basierte Verzeichnisse (z. B. **Active Directory**) für Authentifizierung und Autorisierung, besonders in Windows-Umgebungen.

LDAP ist für Unternehmen entscheidend, um den Benutzerzugriff über interne Systeme hinweg zu verwalten, aber im modernen Webkontext wird LDAP oft mit anderen Protokollen wie SAML oder OAuth für ein vollständigeres Identitätsmanagement integriert.

### 6. **Social-SSO-Anbieter**

Social-**Single-Sign-On-(SSO)**-Anbieter wie **Facebook**, **Google**, **Twitter**, **GitHub** und andere ermöglichen es Benutzern, sich mit ihren Social-Media-Zugangsdaten bei Drittanbieteranwendungen zu authentifizieren. Dies ist eine Art **OAuth-basierter Authentifizierung**, bei der der Drittanbieterdienst (z. B. Google) der Identitätsanbieter ist.

- **Ablauf**: Der Benutzer klickt (zum Beispiel) auf „Mit Google anmelden“. Die App leitet zu Google weiter, wo sich der Benutzer anmeldet (falls noch nicht angemeldet). Google stellt dann ein Zugriffstoken oder ID-Token für die Drittanbieter-App bereit, das zur Authentifizierung des Benutzers und möglicherweise für den Zugriff auf seine Daten verwendet werden kann.
- **Beispiel**: Viele Anwendungen erlauben die Anmeldung mit Ihren Google- oder Facebook-Zugangsdaten. Die App nutzt im Hintergrund OAuth oder OpenID Connect, um Ihre Identität zu überprüfen und in einigen Fällen auf bestimmte Social-Media-Daten zuzugreifen.

Social SSO ist eine bequeme und weit verbreitete Authentifizierungsmethode, weil sie die Hürden für Benutzer verringert, die nicht noch einen weiteren Benutzernamen und ein weiteres Passwort anlegen möchten.

---

### Zusammenfassung der Unterschiede:

- **OAuth**: Wird für die Autorisierung verwendet und erlaubt Drittanbieter-Apps den Zugriff auf Benutzerdaten, ohne Zugangsdaten preiszugeben.
- **OpenID Connect**: Erweitert OAuth um Authentifizierung und ermöglicht Apps, die Identität von Benutzern zu überprüfen.
- **SAML**: XML-basiertes Protokoll für SSO, häufig in Unternehmensumgebungen.
- **WS-Federation**: Ein Microsoft-spezifisches Protokoll für Identitätsföderation, das in Altsystemen verwendet wird.
- **LDAP**: Ein Protokoll zur Abfrage von Verzeichnisdiensten, um Benutzer zu authentifizieren und die Autorisierung zu verwalten.
- **Social-SSO-Anbieter**: OAuth-basierte Systeme (wie Google, Facebook), die Drittanbieter-Apps erlauben, Benutzer mit ihren Social-Media-Zugangsdaten zu authentifizieren.

Jede dieser Technologien hat ihre eigenen Stärken und Anwendungsfälle, und in modernen Anwendungen sehen Sie möglicherweise eine Kombination davon, die für verschiedene Sicherheitsaspekte eingesetzt wird (z. B. OAuth/OIDC für den API-Zugriff, SAML für Unternehmens-SSO).
