# Registro delle decisioni architetturali: opzioni di autenticazione e autorizzazione

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

Autenticazione e autorizzazione delle applicazioni web sono due concetti cruciali per proteggere l'accesso ad applicazioni e servizi. Entrambi riguardano l'identità degli utenti e il modo in cui vengono concessi i permessi, ma si concentrano su aspetti diversi:

- L'**autenticazione** è il processo di verifica dell'identità di un utente o di un sistema.
- L'**autorizzazione** è il processo che determina a quali risorse o azioni può accedere l'utente o il sistema autenticato.

Ora approfondiamo i protocolli e le tecnologie specifici che hai citato, comunemente usati nelle moderne applicazioni web per gestire autenticazione e autorizzazione.

### 1. **OAuth (Open Authorization)**

**OAuth** è uno standard aperto per l'autorizzazione. Consente a un utente di concedere a un'applicazione di terze parti un accesso limitato alle proprie risorse senza condividere le proprie credenziali. L'idea chiave è l'**accesso delegato**. OAuth è spesso usato in situazioni in cui gli utenti possono accedere a un servizio di terze parti (per esempio accedere con Google) senza fornire direttamente nome utente e password alla terza parte.

- **Flusso**: OAuth segue tipicamente un flusso **basato su token**, in cui un server di autorizzazione emette un token di accesso all'applicazione di terze parti. Questo token rappresenta i permessi dell'utente e l'applicazione lo usa per accedere ai dati o alle risorse dell'utente da un'API.
- **Esempio**: un utente accede a un'app di terze parti con il suo account Google. Google verifica l'identità dell'utente e poi concede un token che consente all'app di terze parti di accedere ad alcuni dati Google (per esempio Google Calendar).

OAuth **non** gestisce direttamente l'autenticazione; si occupa di concedere l'accesso. Per l'autenticazione, OAuth è spesso abbinato ad altri protocolli, come **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** è un livello di identità costruito sopra **OAuth 2.0** che aggiunge l'autenticazione alle capacità di autorizzazione di OAuth. In sostanza, OpenID Connect estende OAuth per gestire l'**autenticazione degli utenti** e fornisce un modo standardizzato per le applicazioni di verificare l'identità di un utente.

- **Flusso**: quando un utente accede usando OpenID Connect, l'applicazione di terze parti richiede un token ID (oltre al token di accesso OAuth). Il token ID contiene informazioni sull'utente (come nome utente, email e altri claim). Questo permette all'applicazione di sapere chi è l'utente e se è autenticato.
- **Esempio**: accedere a un servizio come Slack con il tuo account Google (Google è il provider OpenID Connect) comporta l'autenticazione tramite OpenID Connect, mentre OAuth gestisce l'accesso alle tue risorse Google.

OIDC rende più semplice per le app di terze parti **autenticare gli utenti** consentendo comunque un controllo fine su quali risorse tali app possono accedere.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** è uno standard più vecchio, basato su XML, usato per scambiare dati di autenticazione e autorizzazione tra le parti, in particolare negli scenari di **Single Sign-On (SSO)**. È usato principalmente in ambienti aziendali per permettere agli utenti di autenticarsi una volta e accedere a più applicazioni senza reinserire le credenziali.

- **Flusso**: l'utente si autentica prima presso un provider di identità (IdP). L'IdP genera un'**asserzione SAML** firmata che include l'identità dell'utente e gli attributi correlati. L'asserzione viene inviata al fornitore di servizi (SP), che la usa per autorizzare l'accesso all'applicazione.
- **Esempio**: un dipendente accede al portale aziendale (l'IdP) e viene automaticamente connesso ad altri sistemi come email, CRM ecc., senza reinserire le credenziali. Il processo di autenticazione si basa sull'asserzione SAML inviata dall'IdP.

SAML è comunemente usato nelle **soluzioni SSO aziendali** e funziona bene per le applicazioni web negli ambienti aziendali, ma è meno adatto al mobile rispetto a OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** è un altro protocollo usato per il **Single Sign-On (SSO)**, soprattutto negli ambienti aziendali basati su Microsoft. Fa parte della famiglia di specifiche **WS-* (Web Services)** e consente la federazione delle identità tra diversi domini di sicurezza (per esempio tra organizzazioni diverse o tra servizi diversi).

- **Flusso**: WS-Federation consente a un **provider di identità (IdP) fidato** di autenticare gli utenti ed emettere token che il fornitore di servizi può usare per l'autorizzazione. È simile a SAML ma è spesso usato in scenari che si basano molto sulle tecnologie Microsoft.
- **Esempio**: un utente accede a un'applicazione aziendale ospitata da Microsoft Azure Active Directory (AD) e la sua identità può essere usata per accedere ad altri servizi federati, comprese applicazioni ospitate da fornitori terzi.

Sebbene WS-Federation sia in gran parte sostituito da protocolli più recenti come OAuth2.0 e OpenID Connect in molti ambienti web moderni, è ancora usato nei sistemi legacy, soprattutto nelle aziende incentrate su Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** è un protocollo usato per accedere e gestire servizi di directory, comunemente usato per **memorizzare le credenziali degli utenti** e gestire il controllo degli accessi in una directory centralizzata (spesso chiamata **Directory Service**). LDAP non riguarda specificamente l'autenticazione o l'autorizzazione, ma è usato per memorizzare e recuperare dati di identità, che vengono poi usati in questi processi.

- **Autenticazione**: LDAP consente a un'applicazione di autenticare gli utenti interrogando il servizio di directory per le credenziali (come le password).
- **Autorizzazione**: gestisce anche ruoli e permessi degli utenti, aiutando a determinare se un utente ha accesso a determinate risorse.
- **Esempio**: molte aziende usano directory basate su LDAP (per esempio **Active Directory**) per l'autenticazione e l'autorizzazione, soprattutto negli ambienti Windows.

LDAP è fondamentale per le aziende per gestire l'accesso degli utenti ai sistemi interni, ma in un contesto web moderno LDAP viene spesso integrato con altri protocolli come SAML o OAuth per una gestione delle identità più completa.

### 6. **Provider SSO social**

I provider **Single Sign-On (SSO)** social come **Facebook**, **Google**, **Twitter**, **GitHub** e altri consentono agli utenti di autenticarsi in applicazioni di terze parti usando le credenziali dei loro social media. Si tratta di un tipo di **autenticazione basata su OAuth** in cui il servizio di terze parti (per esempio Google) è il provider di identità.

- **Flusso**: l'utente fa clic su "Accedi con Google" (per esempio). L'app reindirizza a Google, dove l'utente effettua l'accesso (se non l'ha già fatto). Google fornisce poi un token di accesso o un token ID all'app di terze parti, che può essere usato per autenticare l'utente e possibilmente accedere ai suoi dati.
- **Esempio**: molte applicazioni permettono di accedere usando le credenziali Google o Facebook. L'app usa OAuth o OpenID Connect dietro le quinte per verificare la tua identità e, in alcuni casi, accedere a certi dati dei social media.

L'SSO social è un metodo di autenticazione comodo e ampiamente adottato perché riduce l'attrito per gli utenti, che potrebbero non voler creare un altro nome utente e un'altra password.

---

### Riepilogo delle differenze:

- **OAuth**: usato per l'autorizzazione, consente alle app di terze parti di accedere ai dati dell'utente senza esporre le credenziali.
- **OpenID Connect**: estende OAuth per fornire l'autenticazione, consentendo alle app di verificare l'identità dell'utente.
- **SAML**: protocollo basato su XML usato per l'SSO, spesso in ambienti aziendali.
- **WS-Federation**: un protocollo specifico di Microsoft per la federazione delle identità, usato nei sistemi legacy.
- **LDAP**: un protocollo per interrogare i servizi di directory per autenticare gli utenti e gestire l'autorizzazione.
- **Provider SSO social**: sistemi basati su OAuth (come Google, Facebook) che consentono alle app di terze parti di autenticare gli utenti usando le credenziali dei loro social media.

Ognuna di queste tecnologie ha i propri punti di forza e casi d'uso, e nelle applicazioni moderne potresti vedere una combinazione di esse usata per diversi aspetti della sicurezza (per esempio OAuth/OIDC per l'accesso alle API, SAML per l'SSO aziendale).
