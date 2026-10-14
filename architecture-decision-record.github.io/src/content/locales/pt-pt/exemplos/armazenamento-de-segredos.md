# Armazenamento de segredos

Sumário:

* [Resumo](#resumo)
  * [Questão](#questão)
  * [Decisão](#decisão)
  * [Estado](#estado)
* [Detalhes](#detalhes)
  * [Premissas](#premissas)
  * [Restrições](#restrições)
  * [Posições](#posições)
  * [Argumento](#argumento)
  * [Implicações](#implicações)
* [Relacionado](#relacionado)
  * [Decisões relacionadas](#decisões-relacionadas)
  * [Requisitos relacionados](#requisitos-relacionados)
  * [Artefatos relacionados](#artefatos-relacionados)
  * [Princípios relacionados](#princípios-relacionados)
* [Notas](#notas)
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Resumo


### Questão

Precisamos armazenar segredos, como senhas, chaves privadas, tokens de autenticação etc.

Alguns dos segredos são orientados ao usuário. Por exemplo, nosso desenvolvedor quer poder usar o celular para consultar a senha de um serviço.

Alguns dos segredos são orientados ao sistema. Por exemplo, nosso pipeline de entrega contínua precisa poder consultar as credenciais da nossa hospedagem em nuvem.


### Decisão

Bitwarden para segredos orientados ao usuário

Vault by HashiCorp para segredos orientados ao sistema.


### Estado

Decidido. Estamos abertos a novas alternativas à medida que surgirem.


## Detalhes


### Premissas

Para este propósito, e no nosso estado atual, valorizamos a conveniência orientada ao usuário, como aplicativos móveis utilizáveis.

  * Queremos garantir acesso rápido e fácil em movimento, como para um desenvolvedor fazendo engenharia de confiabilidade de sistemas de plantão.

  * Queremos poder compartilhar alguns segredos entre pessoas selecionadas, como uma equipe.

Não estamos tentando resolver para um único provedor, como armazenar todos os segredos exclusivamente na Amazon, Azure ou Google.

Não queremos abordagens improvisadas como “decore”, “anote em um papel” ou “descubra sua própria forma de armazenar”.

Nosso modelo de segurança para este propósito aceita usar fornecedores COTS respeitados, como ferramentas SaaS de gerenciamento de senhas.


### Restrições

No momento queremos algo fácil, ou seja, sem necessidade de escrever código, sem necessidade de instalar servidores, sem necessidade de assumir um grande compromisso, sem necessidade de padronizar todo mundo.


### Posições

Consideramos:

1. Gerenciadores de senhas prontos orientados ao usuário: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG etc.

2. Gerenciadores de senhas COTS orientados ao sistema: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Abordagens orientadas ao compartilhamento: usar um documento compartilhado do Google, um canal compartilhado do Slack, uma pasta de rede compartilhada etc.

4. Abordagens improvisadas de baixa tecnologia, como decorar, escrever um bilhete ou depender de cada usuário para descobrir sua própria abordagem.


### Argumento

Bitwarden, LastPass, 1Password e Dashlane são todos produtos comerciais prontos para uso.

  * Tipos de recursos semelhantes para usuários, equipes, organizações etc.

  * Capacidade para desktop em Windows e Mac, e capacidade móvel para Android e iOS.

  * Extensões de navegador para Chrome e Firefox, para preenchimento automático de formulários etc.

O Bitwarden tem duas vantagens sobre os demais:

  * O Bitwarden é de código aberto, o que significa que a segurança pode ser revisada por pares e que a empresa é amplamente apreciada por desenvolvedores voltados à segurança.

  * Relatos de profissionais de software descrevem uma preferência significativa pelo Bitwarden em relação aos outros.

Um bom exemplo típico de artigo: https://jcs.org/2017/11/17/bitwarden

Um site típico de votação lado a lado: https://stackshare.io/stackups/bitwarden-vs-dashlane

Adiamos KeyPass, pass, GPG etc. porque há complexidade adicional. Todos parecem boas soluções para usuários técnicos. O GPG parece especialmente bom para usuários técnicos que querem capacidades multissistema orientadas a linha de comando.

Adiamos o KMS porque ele tem dependência de um único provedor.

Escolhemos o Vault para as necessidades orientadas ao sistema, porque as avaliações são surpreendentemente positivas e porque a HashiCorp tem um excelente histórico de software e suporte de alta qualidade.

Vetamos as abordagens de compartilhamento, como por documentos compartilhados, canais compartilhados, pastas de rede compartilhadas etc. Elas não fornecem as qualidades de segurança que queremos.

Vetamos as abordagens improvisadas de baixa tecnologia, porque todos concordamos que não é um caminho de longo prazo.


### Implicações

Os desenvolvedores podem precisar acompanhar segredos em dois lugares: no Bitwarden para acesso orientado ao usuário e no Vault para acesso orientado ao sistema.


## Relacionado


### Decisões relacionadas

A decisão sobre qual servidor de CI/CD usar deve incluir prova de capacidade de acesso a segredos.

Precisaremos decidir como gerenciar os segredos, em termos de políticas, rotações, organizações etc.


### Requisitos relacionados

Os segredos terão requisitos relacionados de conformidade, auditoria e integração/desligamento de RH.


### Artefatos relacionados

Esperamos que possamos exportar alguns segredos para variáveis de ambiente.


### Princípios relacionados

Facilmente reversível.

Facilmente paralelo, ou seja, é fácil usar uma variedade de gerenciadores de senhas.

Barato de experimentar, ou seja, há um teste gratuito e nenhum compromisso.


## Notas

Notas de avaliação aqui. As notas são todas comentários públicos em vários fóruns de devops.


### Vault by HashiCorp

O Vault é exatamente o que você quer aqui. 

Mas não jogue o Vault direto em produção; suba-o primeiro em um ambiente de teste, porque a documentação da HashiCorp pode ser bem deficiente, mesmo que os produtos deles sejam incríveis.

Curva de aprendizado muito íngreme e não é trivial de subir. 

A configuração inicial é um pouco trabalhosa. Vale totalmente a pena, porém, e a comunidade o apoiará o bastante para você se virar.

Documentação horrível, mas há muitos guias online de pessoas que o configuraram e, se você juntar alguns deles, terá uma configuração funcionando.

A configuração inicial exigiu mexer nos helm charts deles (vault e consul). Embora tecnicamente você possa usar muitos outros back-ends, eu realmente não recomendo. O back-end/consul pode ser minúsculo se você não tiver muitos dados para armazenar.

Definitivamente fique à vontade/familiarizado com o uso da CLI, porque a GUI é mais uma prova de conceito/portal de propaganda da edição enterprise deles.

O fato de você não conseguir simplesmente “enchê-lo” é uma dor. Por exemplo, se você tem 5 campos, precisa adicionar manualmente cada campo para cada item. Então não é como se você predefinisse campos para uma categoria específica e preenchesse esses campos para todos os itens dessa categoria; é mais como “você gera tudo toda vez”, o que (na minha opinião) é um saco.

Você também pode querer olhar o goldfish como uma UI sobre o vault. Torna bem agradável convencer sua equipe a adotá-lo. Eles também têm uma demo. 1. Configure o consul. 2. Configure o vault apontando para o consul. 3. Configure o goldfish apontando para o vault. 3. Configure algum cron job para executar o consul snapshot para backups.



### LastPass

LastPass Teams. Nós o usamos, tem modelos personalizados, ACL, nada faltando na minha opinião.

Implementei o LastPass na minha organização e dou nota C+/B-. O maior problema ultimamente é a falta de confiabilidade. Nos últimos 90 dias houve várias horas em que os cofres foram forçados ao modo offline. Isso não é o ideal para a minha organização porque temos, literalmente, mais de 4.000 senhas armazenadas em mais de 20 pastas compartilhadas. Como você pode imaginar, com tantas senhas, pelo menos algumas são atualizadas ou adicionadas diariamente. Temos um plano de recuperação de desastres se os problemas durarem mais de uma ou duas horas: um script assina e criptografa todas as noites um dump CSV do cofre que pode ser importado no keepass.

O LastPass teve lampejos não relatados de serviço degradado: o login “funciona”, mas não traz os sites, recursos aleatórios quebrados no painel de administração e chaves não compartilhadas corretamente para novas pastas compartilhadas de nível superior. Tenho um usuário específico de “key push”/backup que está em todos os grupos. Normalmente entrar como esse usuário resolve qualquer problema de compartilhamento de chaves, mas não quando o serviço está degradado, apesar do que diz a página de status...

Quanto à integração, pode ser fácil se você tiver ACLs adequadas com um modelo de privilégio mínimo, p. ex., se um usuário tem leitura e escrita e somente leitura em uma entrada ou pasta, ele recebe apenas permissões de somente leitura. Infelizmente, as ACLs da minha organização não são as melhores, então acabei usando a API de provisionamento JSON e ~500 linhas de python porque a natureza dependente das nossas centenas de ACLs não se mapeia bem no modelo de privilégio mínimo. Acabei obtendo todas as ACLs em que um usuário estava e fazendo uma espécie de percurso de dependências.

Se a estrutura de ACL ou de grupos já foi construída pensando em uma estrutura de privilégio mínimo, a ferramenta de sincronização AD/LDAP para Windows funcionará bem.

Entre em contato com a equipe de vendas deles e eles podem arranjar um teste Enterprise mais longo. Certifique-se de entender plenamente suas limitações antes de apertar o gatilho. Tivemos um bom número de dores de crescimento, mas, afora interrupções ou degradações do lado do servidor, tem sido incrivelmente tranquilo.


### Bitwarden

O Bitwarden tem boas ferramentas ao redor (WebUI, CLI, móvel, desktop). Auto-hospedado e razoavelmente fácil de configurar. Documentação razoavelmente boa e ferramenta recomendada pelo PrivacyTools.


### EnvKey

https://www.envkey.com/ é um saas. Muito fácil de implementar, integrar e gerenciar.

Recursos:

  * Proteger chaves de API e credenciais.

  * Manter a configuração sincronizada em todo lugar.

  * Gerenciamento inteligente de configuração e segredos com criptografia de ponta a ponta. 

  * Evitar compartilhamento inseguro e dispersão de configurações. 

  * Integrar em minutos.

Capacidades:

  * Gerenciar configuração e níveis de acesso para todos os seus apps, ambientes e equipes em um só lugar.

  * Configurar qualquer ambiente de desenvolvimento ou servidor com apenas uma única variável de ambiente.

Prós:

  * Boa página inicial.

  * Proposta de valor clara.

  * App web visualmente excelente.

  * Dados de exemplo superiores, p. ex., Algolia, AWS, Datadog, GitHub, Stripe etc.

  * Conversei com o fundador por 30 min sobre a empresa, a UI etc. O Dane parece bem informado, honesto sobre os prós e contras e um parceiro viável.

  * A empresa é essencialmente uma típica empresa da Y Combinator, com 1 fundador. Levantou US$ 120 mil em 2018-01.

  * O foco é chegar a recursos enterprise, esp. passar da hospedagem em nuvem do EnvKey para on-prem ou BYOC.

  * Possível caminho a seguir: começar com o EnvKey pela facilidade de uso e, depois (ou em paralelo), adicionar o Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

O Confidant é um serviço de gerenciamento de segredos de código aberto que fornece armazenamento fácil de usar e acesso a segredos de forma segura, dos desenvolvedores da Lyft.

Autenticação KMS: o Confidant resolve o problema do “ovo e da galinha” da autenticação usando o AWS KMS e o IAM para permitir que funções IAM gerem tokens de autenticação seguros que podem ser verificados pelo Confidant. O Confidant também gerencia as concessões do KMS para as suas funções IAM, o que permite que as funções IAM gerem tokens que podem ser usados para autenticação serviço a serviço ou para passar mensagens criptografadas entre serviços.

Criptografia em repouso de segredos versionados: o Confidant armazena segredos de forma somente de acréscimo no DynamoDB, gerando uma chave de dados KMS exclusiva para cada revisão de cada segredo, usando a criptografia autenticada simétrica Fernet.

Uma interface web amigável para gerenciar segredos: o Confidant fornece uma interface web em AngularJS que permite aos usuários finais gerenciar facilmente segredos, os mapeamentos de segredos para serviços e o histórico de mudanças.


### Devolutions Password Server

https://server.devolutions.net/

Proteja, gerencie e monitore o acesso a contas e sessões privilegiadas.

Um cofre de senhas abrangente e altamente seguro que permite controlar o acesso às suas contas privilegiadas, ao mesmo tempo que melhora a visibilidade geral da rede para administradores de sistemas e oferece uma experiência fluida aos usuários finais.

Recursos: cofre de senhas centralizado da organização, cofre privado específico do usuário, gerenciador de senhas, injeção de credenciais,
integração com o Active Directory, controle de acesso baseado em funções, autenticação de dois fatores, pronto para empresas, restrições de IP, capacidades de gerenciamento, gerador automático de senhas, acesso por aplicativo móvel, histórico de senhas, relatórios de acesso, alertas por e-mail.

  * dá suporte à criptografia de dados

  * dá suporte a vários esquemas de autenticação, incluindo LDAP, O365 e usuários locais, COM suporte a MFA de várias fontes

  * vários repositórios/cofres com controles de acesso refinados para várias equipes

  * UI web moderna

  * cofres privados de credenciais e conexões para credenciais/conexões pessoais

  * aplicativos móveis para iOS/Android

  * logs de auditoria para cada entrada, quem/o quê/quando, com um prompt opcional sobre o porquê do acesso

  * modelos personalizáveis (embora deem suporte nativo a centenas de tipos de conexão)

  * muitos outros recursos e um cliente pesado para Windows/Mac (Remote Desktop Manager) com o qual você pode sincronizar e que amplia muito as opções... conexões com um clique

  * o preço não é tão ruim — até 15 usuários custa US$ 500 por ano pelo servidor de senhas


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Recursos da versão on-premise: 

  * Controle total sobre seus sistemas de segurança e infraestrutura de ponta a ponta

  * Implante o software dentro do seu data center local ou da sua própria instância de nuvem privada virtual

  * Cumpra obrigações legais e regulatórias que exigem que todos os dados e sistemas residam no local

Recursos da versão em nuvem:

  * O modelo de software como serviço permite que você se cadastre e comece imediatamente

  * Escalabilidade elástica conforme você cresce

  * Controles e redundância fornecidos pelo Azure com SLA de 99,9% de tempo de atividade

Feedback dos usuários:

  * Costumávamos usar esse produto. Era tão fácil de contornar e as regras só funcionam para gente esperta. Usuários preguiçosos ou burros conseguem estragá-lo com facilidade em uma área de equipe. Os preços são negociáveis quando você fala com eles.

  * Você pode rodá-lo usando SQL express e uma máquina Win 7. 

  * Barato.
