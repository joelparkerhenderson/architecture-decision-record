# Enregistrement de décision d’architecture : options d’authentification et d’autorisation

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

L’authentification et l’autorisation des applications web sont deux concepts essentiels pour sécuriser l’accès aux applications et aux services. Tous deux portent sur l’identité des utilisateurs et sur la manière dont les permissions sont accordées, mais ils se concentrent sur des aspects différents :

- **L’authentification** est le processus de vérification de l’identité d’un utilisateur ou d’un système.
- **L’autorisation** est le processus qui détermine à quelles ressources ou actions l’utilisateur ou le système authentifié peut accéder.

Passons maintenant aux protocoles et technologies spécifiques que vous avez mentionnés, couramment utilisés dans les applications web modernes pour gérer l’authentification et l’autorisation.

### 1. **OAuth (Open Authorization)**

**OAuth** est une norme ouverte d’autorisation. Il permet à un utilisateur d’accorder à une application tierce un accès limité à ses ressources sans partager ses identifiants. L’idée clé est l’**accès délégué**. OAuth est souvent utilisé lorsque les utilisateurs peuvent se connecter à un service tiers (p. ex. en se connectant avec Google) sans fournir directement leur nom d’utilisateur et leur mot de passe au tiers.

- **Flux** : OAuth suit généralement un flux **à base de jetons**, dans lequel un serveur d’autorisation émet un jeton d’accès à l’application tierce. Ce jeton représente les permissions de l’utilisateur, et l’application l’utilise pour accéder aux données ou ressources de l’utilisateur depuis une API.
- **Exemple** : un utilisateur se connecte à une application tierce avec son compte Google. Google vérifie l’identité de l’utilisateur puis accorde un jeton qui permet à l’application tierce d’accéder à certaines données Google (p. ex. Google Agenda).

OAuth ne gère **pas** directement l’authentification ; il s’agit d’accorder un accès. Pour l’authentification, OAuth est souvent associé à d’autres protocoles, comme **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** est une couche d’identité construite au-dessus d’**OAuth 2.0** qui ajoute l’authentification aux capacités d’autorisation d’OAuth. En substance, OpenID Connect étend OAuth pour gérer l’**authentification des utilisateurs** et offre aux applications un moyen normalisé de vérifier l’identité d’un utilisateur.

- **Flux** : lorsqu’un utilisateur se connecte avec OpenID Connect, l’application tierce demande un jeton d’identité (en plus du jeton d’accès OAuth). Le jeton d’identité contient des informations sur l’utilisateur (comme son nom d’utilisateur, son courriel et d’autres revendications). Cela permet à l’application de savoir qui est l’utilisateur et s’il est authentifié.
- **Exemple** : se connecter à un service comme Slack avec votre compte Google (Google étant le fournisseur OpenID Connect) implique une authentification via OpenID Connect, tandis qu’OAuth gère l’accès à vos ressources Google.

OIDC permet aux applications tierces d’**authentifier plus facilement les utilisateurs** tout en autorisant un contrôle fin des ressources auxquelles ces applications peuvent accéder.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** est une norme plus ancienne, fondée sur XML, utilisée pour échanger des données d’authentification et d’autorisation entre les parties, en particulier dans les scénarios d’**authentification unique (SSO)**. Il est principalement utilisé dans les environnements d’entreprise pour permettre aux utilisateurs de s’authentifier une seule fois et d’accéder à plusieurs applications sans ressaisir leurs identifiants.

- **Flux** : l’utilisateur s’authentifie d’abord auprès d’un fournisseur d’identité (IdP). L’IdP génère une **assertion SAML** signée qui comprend l’identité de l’utilisateur et les attributs associés. L’assertion est envoyée au fournisseur de services (SP), qui l’utilise pour autoriser l’accès à l’application.
- **Exemple** : un employé se connecte au portail de son entreprise (l’IdP) et est automatiquement connecté à d’autres systèmes comme la messagerie, le CRM, etc., sans ressaisir ses identifiants. Le processus d’authentification repose sur l’assertion SAML envoyée par l’IdP.

SAML est couramment utilisé dans les **solutions SSO d’entreprise** et convient bien aux applications web des environnements d’entreprise, mais il est moins adapté au mobile qu’OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** est un autre protocole utilisé pour l’**authentification unique (SSO)**, en particulier dans les environnements d’entreprise fondés sur Microsoft. Il fait partie de la famille de spécifications **WS-* (Web Services)** et permet la fédération d’identités entre différents domaines de sécurité (par exemple entre différentes organisations ou entre différents services).

- **Flux** : WS-Federation permet à un **fournisseur d’identité (IdP) de confiance** d’authentifier les utilisateurs et d’émettre des jetons que le fournisseur de services peut utiliser pour l’autorisation. Il est similaire à SAML mais est souvent utilisé dans des scénarios qui reposent fortement sur les technologies Microsoft.
- **Exemple** : un utilisateur se connecte à une application d’entreprise hébergée par Microsoft Azure Active Directory (AD), et son identité peut servir à accéder à d’autres services fédérés, y compris des applications hébergées par des fournisseurs tiers.

Bien que WS-Federation ait été en grande partie remplacé par des protocoles plus récents comme OAuth 2.0 et OpenID Connect dans de nombreux environnements web modernes, il reste utilisé dans les systèmes hérités, en particulier dans les entreprises centrées sur Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** est un protocole utilisé pour accéder à des services d’annuaire et les gérer, couramment employé pour **stocker les identifiants des utilisateurs** et gérer le contrôle d’accès dans un annuaire centralisé (souvent appelé **service d’annuaire**). LDAP ne concerne pas spécifiquement l’authentification ou l’autorisation, mais sert à stocker et récupérer des données d’identité, qui sont ensuite utilisées dans ces processus.

- **Authentification** : LDAP permet à une application d’authentifier des utilisateurs en interrogeant le service d’annuaire pour obtenir leurs identifiants (comme les mots de passe).
- **Autorisation** : il gère aussi les rôles et permissions des utilisateurs, ce qui aide à déterminer si un utilisateur a accès à certaines ressources.
- **Exemple** : de nombreuses entreprises utilisent des annuaires fondés sur LDAP (p. ex. **Active Directory**) pour l’authentification et l’autorisation, surtout dans les environnements Windows.

LDAP est essentiel pour que les entreprises gèrent l’accès des utilisateurs aux systèmes internes, mais dans un contexte web moderne, LDAP est souvent intégré à d’autres protocoles comme SAML ou OAuth pour une gestion des identités plus complète.

### 6. **Fournisseurs de SSO social**

Les fournisseurs d’**authentification unique (SSO)** sociale comme **Facebook**, **Google**, **Twitter**, **GitHub** et d’autres permettent aux utilisateurs de s’authentifier auprès d’applications tierces avec leurs identifiants de réseaux sociaux. C’est un type d’**authentification fondée sur OAuth** où le service tiers (p. ex. Google) est le fournisseur d’identité.

- **Flux** : l’utilisateur clique sur « Se connecter avec Google » (par exemple). L’application redirige vers Google, où l’utilisateur se connecte (s’il ne l’est pas déjà). Google fournit alors un jeton d’accès ou un jeton d’identité à l’application tierce, qui peut servir à authentifier l’utilisateur et éventuellement à accéder à ses données.
- **Exemple** : de nombreuses applications vous permettent de vous connecter avec vos identifiants Google ou Facebook. L’application utilisera OAuth ou OpenID Connect en coulisses pour vérifier votre identité et, dans certains cas, accéder à certaines données de réseaux sociaux.

Le SSO social est une méthode d’authentification pratique et largement adoptée parce qu’elle réduit les frictions pour les utilisateurs, qui ne souhaitent peut-être pas créer encore un autre nom d’utilisateur et un autre mot de passe.

---

### Résumé des différences :

- **OAuth** : utilisé pour l’autorisation, permet à des applications tierces d’accéder aux données de l’utilisateur sans exposer ses identifiants.
- **OpenID Connect** : étend OAuth pour fournir l’authentification, ce qui permet aux applications de vérifier l’identité de l’utilisateur.
- **SAML** : protocole fondé sur XML utilisé pour le SSO, souvent dans les environnements d’entreprise.
- **WS-Federation** : protocole propre à Microsoft pour la fédération d’identités, utilisé dans les systèmes hérités.
- **LDAP** : protocole d’interrogation de services d’annuaire pour authentifier les utilisateurs et gérer l’autorisation.
- **Fournisseurs de SSO social** : systèmes fondés sur OAuth (comme Google, Facebook) qui permettent aux applications tierces d’authentifier les utilisateurs avec leurs identifiants de réseaux sociaux.

Chacune de ces technologies a ses propres forces et cas d’usage, et dans les applications modernes vous pouvez voir une combinaison d’entre elles utilisée pour différents aspects de la sécurité (p. ex. OAuth/OIDC pour l’accès aux API, SAML pour le SSO d’entreprise).
