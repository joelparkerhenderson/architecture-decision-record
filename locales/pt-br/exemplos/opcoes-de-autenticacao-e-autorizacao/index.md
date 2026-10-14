# Registro de Decisão de Arquitetura: opções de autenticação e autorização

<!--

Prompt do ChatGPT:

Explique autenticação e autorização de aplicações web.

Descreva: OAuth, OpenID Connect, SAML, WS-Federation, LDAP, provedores de SSO social.

-->

Autenticação e autorização de aplicações web são dois conceitos cruciais para proteger o acesso a aplicações e serviços. Ambos lidam com a identidade dos usuários e com a forma como permissões são concedidas, mas se concentram em aspectos diferentes:

- **Autenticação** é o processo de verificar a identidade de um usuário ou sistema.
- **Autorização** é o processo de determinar quais recursos ou ações o usuário ou sistema autenticado pode acessar.

Agora, vamos nos aprofundar nos protocolos e tecnologias específicos que você mencionou, que são comumente usados em aplicações web modernas para gerenciar autenticação e autorização.

### 1. **OAuth (Open Authorization)**

**OAuth** é um padrão aberto para autorização. Ele permite que um usuário conceda a uma aplicação de terceiros acesso limitado aos seus recursos sem compartilhar suas credenciais. A ideia central é **acesso delegado**. OAuth é frequentemente usado em situações em que usuários podem entrar em um serviço de terceiros (por exemplo, entrar com Google) sem fornecer diretamente seu nome de usuário e senha ao terceiro.

- **Fluxo**: OAuth normalmente segue um fluxo **baseado em tokens**, no qual um servidor de autorização emite um token de acesso para a aplicação de terceiros. Esse token representa as permissões do usuário, e a aplicação o usa para acessar dados ou recursos do usuário a partir de uma API.
- **Exemplo**: Um usuário entra em um app de terceiros usando sua conta do Google. O Google verifica a identidade do usuário e então concede um token que permite que o app de terceiros acesse alguns dados do Google (por exemplo, Google Calendar).

OAuth **não** lida diretamente com autenticação; ele trata de conceder acesso. Para autenticação, OAuth é frequentemente combinado com outros protocolos, como **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** é uma camada de identidade construída sobre o **OAuth 2.0** que adiciona autenticação às capacidades de autorização do OAuth. Essencialmente, OpenID Connect estende OAuth para lidar com **autenticação de usuários** e fornece uma forma padronizada para aplicações verificarem a identidade de um usuário.

- **Fluxo**: Quando um usuário entra usando OpenID Connect, a aplicação de terceiros solicita um token de ID (além do token de acesso OAuth). O token de ID contém informações sobre o usuário (como nome de usuário, e-mail e outras declarações). Isso permite que a aplicação saiba quem é o usuário e se ele está autenticado.
- **Exemplo**: Entrar em um serviço como Slack usando sua conta do Google (sendo o Google o provedor OpenID Connect) envolve autenticação via OpenID Connect, enquanto OAuth gerencia o acesso aos seus recursos do Google.

OIDC facilita para apps de terceiros **autenticar usuários**, ao mesmo tempo em que ainda permite controle refinado sobre quais recursos esses apps podem acessar.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** é um padrão mais antigo, baseado em XML, usado para trocar dados de autenticação e autorização entre partes, especialmente em cenários de **Single Sign-On (SSO)**. Ele é usado principalmente em ambientes corporativos para permitir que usuários se autentiquem uma vez e acessem múltiplas aplicações sem inserir credenciais novamente.

- **Fluxo**: O usuário primeiro se autentica com um provedor de identidade (IdP). O IdP gera uma **asserção SAML** assinada que inclui a identidade do usuário e atributos relacionados. A asserção é enviada ao provedor de serviço (SP), que a usa para autorizar o acesso à aplicação.
- **Exemplo**: Um funcionário entra no portal corporativo (o IdP) e é automaticamente conectado a outros sistemas, como e-mail, CRM etc., sem inserir credenciais novamente. O processo de autenticação é baseado na asserção SAML enviada pelo IdP.

SAML é comumente usado em **soluções corporativas de SSO** e funciona bem para aplicações web em ambientes corporativos, mas é menos amigável para mobile em comparação com OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** é outro protocolo usado para **Single Sign-On (SSO)**, especialmente em ambientes corporativos baseados em Microsoft. Ele faz parte da família de especificações **WS-* (Web Services)** e permite federação de identidade entre diferentes domínios de segurança (como entre diferentes organizações ou entre diferentes serviços).

- **Fluxo**: WS-Federation permite que um **provedor de identidade confiável (IdP)** autentique usuários e emita tokens que o provedor de serviço pode usar para autorização. Ele é semelhante ao SAML, mas costuma ser usado em cenários que dependem fortemente de tecnologias Microsoft.
- **Exemplo**: Um usuário entra em uma aplicação corporativa hospedada pelo Microsoft Azure Active Directory (AD), e sua identidade pode ser usada para acessar outros serviços federados, incluindo aplicações hospedadas por fornecedores terceiros.

Embora WS-Federation tenha sido amplamente substituído por protocolos mais novos, como OAuth2.0 e OpenID Connect, em muitos ambientes web modernos, ele ainda é usado em sistemas legados, especialmente em empresas centradas em Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** é um protocolo usado para acessar e gerenciar serviços de diretório, comumente usado para **armazenar credenciais de usuários** e gerenciar controle de acesso em um diretório centralizado (frequentemente chamado de **Directory Service**). LDAP não é especificamente sobre autenticação ou autorização, mas é usado para armazenar e recuperar dados de identidade, que então são usados nesses processos.

- **Autenticação**: LDAP permite que uma aplicação autentique usuários consultando o serviço de diretório em busca de credenciais (como senhas).
- **Autorização**: Ele também gerencia papéis e permissões de usuários, ajudando a determinar se um usuário tem acesso a determinados recursos.
- **Exemplo**: Muitas empresas usam diretórios baseados em LDAP (por exemplo, **Active Directory**) para autenticação e autorização, especialmente em ambientes Windows.

LDAP é crucial para empresas gerenciarem acesso de usuários em sistemas internos, mas, em um contexto web moderno, LDAP costuma ser integrado a outros protocolos como SAML ou OAuth para gerenciamento de identidade mais completo.

### 6. **Provedores de SSO social**

Provedores de **Single Sign-On (SSO)** social, como **Facebook**, **Google**, **Twitter**, **GitHub** e outros, permitem que usuários se autentiquem em aplicações de terceiros usando suas credenciais de redes sociais. Esse é um tipo de **autenticação baseada em OAuth** em que o serviço de terceiros (por exemplo, Google) é o provedor de identidade.

- **Fluxo**: O usuário clica em "Entrar com Google" (por exemplo). O app redireciona para o Google, onde o usuário entra (se ainda não estiver conectado). O Google então fornece um token de acesso ou token de ID ao app de terceiros, que pode ser usado para autenticar o usuário e possivelmente acessar seus dados.
- **Exemplo**: Muitas aplicações permitem que você entre usando suas credenciais do Google ou Facebook. O app usará OAuth ou OpenID Connect nos bastidores para verificar sua identidade e, em alguns casos, acessar certos dados de redes sociais.

SSO social é um método conveniente e amplamente adotado para autenticação porque reduz atrito para usuários, que podem não querer criar mais um nome de usuário e senha.

---

### Resumo das diferenças:

- **OAuth**: Usado para autorização, permite que apps de terceiros acessem dados do usuário sem expor credenciais.
- **OpenID Connect**: Estende OAuth para fornecer autenticação, permitindo que apps verifiquem a identidade do usuário.
- **SAML**: Protocolo baseado em XML usado para SSO, frequentemente em ambientes corporativos.
- **WS-Federation**: Um protocolo específico da Microsoft para federação de identidade, usado em sistemas legados.
- **LDAP**: Um protocolo para consultar serviços de diretório a fim de autenticar usuários e gerenciar autorização.
- **Provedores de SSO social**: Sistemas baseados em OAuth (como Google, Facebook) que permitem que apps de terceiros autentiquem usuários usando suas credenciais de redes sociais.

Cada uma dessas tecnologias tem seus próprios pontos fortes e casos de uso, e em aplicações modernas você pode ver uma combinação delas sendo usada para diferentes aspectos de segurança (por exemplo, OAuth/OIDC para acesso a APIs, SAML para SSO corporativo).
