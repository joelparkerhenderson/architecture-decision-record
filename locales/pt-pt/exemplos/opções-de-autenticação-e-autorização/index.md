# Registro de decisão de arquitetura: opções de autenticação e autorização

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

A autenticação e a autorização de aplicações web são dois conceitos cruciais para proteger o acesso a aplicações e serviços. Ambos lidam com a identidade dos usuários e com a forma como as permissões são concedidas, mas se concentram em aspectos diferentes:

- **Autenticação** é o processo de verificar a identidade de um usuário ou sistema.
- **Autorização** é o processo de determinar a quais recursos ou ações o usuário ou sistema autenticado pode ter acesso.

Agora, vamos mergulhar nos protocolos e tecnologias específicos que você mencionou, que são comumente usados em aplicações web modernas para gerenciar autenticação e autorização.

### 1. **OAuth (Open Authorization)**

O **OAuth** é um padrão aberto para autorização. Ele permite que um usuário conceda a uma aplicação de terceiros acesso limitado aos seus recursos sem compartilhar suas credenciais. A ideia central é o **acesso delegado**. O OAuth é frequentemente usado em situações em que os usuários podem entrar em um serviço de terceiros (p. ex., entrar com o Google) sem fornecer diretamente seu nome de usuário e senha ao terceiro.

- **Fluxo**: o OAuth normalmente segue um fluxo **baseado em tokens**, em que um servidor de autorização emite um token de acesso para a aplicação de terceiros. Esse token representa as permissões do usuário, e a aplicação o usa para acessar os dados ou recursos do usuário a partir de uma API.
- **Exemplo**: um usuário entra em um app de terceiros usando sua conta do Google. O Google verifica a identidade do usuário e então concede um token que permite ao app de terceiros acessar alguns dados do Google (p. ex., o Google Calendar).

O OAuth **não** lida diretamente com autenticação; ele trata de conceder acesso. Para autenticação, o OAuth costuma ser combinado com outros protocolos, como o **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

O **OpenID Connect (OIDC)** é uma camada de identidade construída sobre o **OAuth 2.0** que adiciona autenticação às capacidades de autorização do OAuth. Essencialmente, o OpenID Connect estende o OAuth para lidar com a **autenticação de usuários** e fornece uma maneira padronizada de as aplicações verificarem a identidade de um usuário.

- **Fluxo**: quando um usuário faz login usando o OpenID Connect, a aplicação de terceiros solicita um token de ID (além do token de acesso do OAuth). O token de ID contém informações sobre o usuário (como nome de usuário, e-mail e outras declarações). Isso permite que a aplicação saiba quem é o usuário e se ele está autenticado.
- **Exemplo**: entrar em um serviço como o Slack usando sua conta do Google (sendo o Google o provedor OpenID Connect) envolve autenticação via OpenID Connect, enquanto o OAuth gerencia o acesso aos seus recursos do Google.

O OIDC facilita para as aplicações de terceiros **autenticar usuários**, ao mesmo tempo que permite controle refinado sobre quais recursos essas aplicações podem acessar.

### 3. **SAML (Security Assertion Markup Language)**

O **SAML** é um padrão mais antigo, baseado em XML, usado para trocar dados de autenticação e autorização entre partes, particularmente em cenários de **Single Sign-On (SSO)**. É usado principalmente em ambientes corporativos para permitir que os usuários se autentiquem uma vez e acessem várias aplicações sem reinserir credenciais.

- **Fluxo**: o usuário primeiro se autentica em um provedor de identidade (IdP). O IdP gera uma **asserção SAML** assinada que inclui a identidade do usuário e atributos relacionados. A asserção é enviada ao provedor de serviço (SP), que a usa para autorizar o acesso à aplicação.
- **Exemplo**: um funcionário entra no portal corporativo da empresa (o IdP) e é automaticamente conectado a outros sistemas, como e-mail, CRM etc., sem reinserir credenciais. O processo de autenticação baseia-se na asserção SAML enviada pelo IdP.

O SAML é comumente usado em **soluções de SSO corporativas** e funciona bem para aplicações web em ambientes corporativos, mas é menos adequado a dispositivos móveis em comparação com OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

O **WS-Federation** é outro protocolo usado para **Single Sign-On (SSO)**, especialmente em ambientes corporativos baseados na Microsoft. Faz parte da família de especificações **WS-* (Web Services)** e permite a federação de identidades entre diferentes domínios de segurança (como entre organizações diferentes ou entre serviços diferentes).

- **Fluxo**: o WS-Federation permite que um **provedor de identidade (IdP) confiável** autentique usuários e emita tokens que o provedor de serviço pode usar para autorização. É semelhante ao SAML, mas é frequentemente usado em cenários que dependem muito de tecnologias da Microsoft.
- **Exemplo**: um usuário entra em uma aplicação corporativa hospedada no Microsoft Azure Active Directory (AD), e sua identidade pode ser usada para acessar outros serviços federados, incluindo aplicações hospedadas por fornecedores terceiros.

Embora o WS-Federation tenha sido em grande parte substituído por protocolos mais novos, como o OAuth 2.0 e o OpenID Connect, em muitos ambientes web modernos, ele ainda é usado em sistemas legados, especialmente em empresas centradas na Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

O **LDAP** é um protocolo usado para acessar e gerenciar serviços de diretório, comumente usado para **armazenar credenciais de usuários** e gerenciar o controle de acesso em um diretório centralizado (frequentemente chamado de **Serviço de Diretório**). O LDAP não trata especificamente de autenticação ou autorização, mas é usado para armazenar e recuperar dados de identidade, que são então usados nesses processos.

- **Autenticação**: o LDAP permite que uma aplicação autentique usuários consultando o serviço de diretório em busca de credenciais (como senhas).
- **Autorização**: ele também gerencia funções e permissões de usuários, ajudando a determinar se um usuário tem acesso a determinados recursos.
- **Exemplo**: muitas empresas usam diretórios baseados em LDAP (p. ex., o **Active Directory**) para autenticação e autorização, especialmente em ambientes Windows.

O LDAP é crucial para as empresas gerenciarem o acesso de usuários em sistemas internos, mas, em um contexto web moderno, o LDAP é frequentemente integrado a outros protocolos, como SAML ou OAuth, para um gerenciamento de identidade mais completo.

### 6. **Provedores de SSO social**

Provedores de **Single Sign-On (SSO)** social como **Facebook**, **Google**, **Twitter**, **GitHub** e outros permitem que os usuários se autentiquem em aplicações de terceiros usando suas credenciais de mídia social. É um tipo de **autenticação baseada em OAuth** em que o serviço de terceiros (p. ex., o Google) é o provedor de identidade.

- **Fluxo**: o usuário clica em “Entrar com o Google” (por exemplo). O app redireciona para o Google, onde o usuário faz login (se ainda não estiver conectado). O Google então fornece um token de acesso ou token de ID à aplicação de terceiros, que pode ser usado para autenticar o usuário e possivelmente acessar seus dados.
- **Exemplo**: muitas aplicações permitem que você entre usando suas credenciais do Google ou do Facebook. O app usará OAuth ou OpenID Connect nos bastidores para verificar sua identidade e, em alguns casos, acessar certos dados de mídia social.

O SSO social é um método de autenticação conveniente e amplamente adotado porque reduz o atrito para usuários que podem não querer criar mais um nome de usuário e senha.

---

### Resumo das diferenças:

- **OAuth**: usado para autorização, permite que aplicações de terceiros acessem dados do usuário sem expor credenciais.
- **OpenID Connect**: estende o OAuth para fornecer autenticação, permitindo que as aplicações verifiquem a identidade do usuário.
- **SAML**: protocolo baseado em XML usado para SSO, frequentemente em ambientes corporativos.
- **WS-Federation**: um protocolo específico da Microsoft para federação de identidades, usado em sistemas legados.
- **LDAP**: um protocolo para consultar serviços de diretório a fim de autenticar usuários e gerenciar autorização.
- **Provedores de SSO social**: sistemas baseados em OAuth (como Google e Facebook) que permitem que aplicações de terceiros autentiquem usuários usando credenciais de mídia social.

Cada uma dessas tecnologias tem seus próprios pontos fortes e casos de uso e, em aplicações modernas, você pode ver uma combinação delas sendo usada para diferentes aspectos da segurança (p. ex., OAuth/OIDC para acesso a APIs, SAML para SSO corporativo).
