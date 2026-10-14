# Armazenamento de segredos

Conteúdo:

* [Resumo](#resumo)
  * [Questão](#questão)
  * [Decisão](#decisão)
  * [Status](#status)
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

Alguns dos segredos são orientados a usuários. Por exemplo, nosso desenvolvedor quer poder usar seu celular para consultar uma senha de um serviço.

Alguns dos segredos são orientados a sistemas. Por exemplo, nosso pipeline de entrega contínua precisa conseguir consultar as credenciais da nossa hospedagem em cloud.


### Decisão

Bitwarden para segredos orientados a usuários.

Vault by HashiCorp para segredos orientados a sistemas.


### Status

Decidido. Estamos abertos a novas alternativas conforme elas surgirem.


## Detalhes


### Premissas

Para este propósito, e em nosso estado atual, valorizamos conveniência orientada a usuários, como aplicativos móveis usáveis.

  * Queremos garantir acesso rápido e fácil em movimento, como para um desenvolvedor fazendo engenharia de confiabilidade de sistemas on-call.

  * Queremos poder compartilhar alguns segredos entre pessoas selecionadas, como uma equipe.

Não estamos tentando resolver para um único provedor, como armazenar todos os segredos exclusivamente na Amazon, Azure ou Google.

Não queremos abordagens ad hoc como "memorize", "escreva em uma anotação" ou "descubra seu próprio jeito de armazenar".

Nosso modelo de segurança para este propósito está confortável com o uso de fornecedores COTS respeitados, como ferramentas SaaS de gerenciamento de senhas.


### Restrições

Agora queremos algo que seja fácil, ou seja, sem necessidade de escrever código, instalar servidores, assumir um grande compromisso ou padronizar todo mundo.


### Posições

Consideramos:

1. Gerenciadores de senhas prontos de prateleira orientados a usuários: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG etc.

2. Gerenciadores de senhas COTS orientados a sistemas: AWS KMS, Vault by HashiCorp, EnvKy, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Abordagens orientadas a compartilhamento: usar um documento Google compartilhado, um canal Slack compartilhado, uma pasta de rede compartilhada etc.

4. Abordagens ad hoc de baixa tecnologia, como memorizar, escrever uma anotação ou confiar que cada usuário descubra sua própria abordagem.


### Argumento

Bitwarden, LastPass, 1Password e Dashlane são todos produtos comerciais prontos de prateleira.

  * Tipos semelhantes de recursos para usuários, equipes, organizações etc.

  * Capacidade desktop para Windows e Mac, e capacidade móvel para Android e iOS.

  * Extensões de navegador para Chrome e Firefox, para preenchimento automático de formulários etc.

Bitwarden tem duas vantagens sobre os outros:

  * Bitwarden é open source, o que significa que a segurança pode ser revisada por pares e também que a empresa é amplamente apreciada por desenvolvedores orientados a segurança.

  * Relatos de trabalhadores de software descrevem uma preferência significativa por Bitwarden em relação aos outros.

Um exemplo típico de bom texto: https://jcs.org/2017/11/17/bitwarden

Um site típico de votação lado a lado: https://stackshare.io/stackups/bitwarden-vs-dashlane

Adiamos KeyPass, pass, GPG etc. porque há complexidade adicional. Todas essas parecem soluções boas para usuários técnicos. GPG parece especialmente bom para usuários técnicos que querem capacidades orientadas a comandos entre sistemas.

Adiamos KMS porque tem lock-in de provedor único.

Escolhemos Vault para necessidades orientadas a sistemas, porque as avaliações são incrivelmente positivas e porque a HashiCorp tem um excelente histórico de software e suporte de alta qualidade.

Vetamos as abordagens de compartilhamento, como via documentos compartilhados, canais compartilhados, pastas de rede compartilhadas etc. Elas não fornecem as qualidades de segurança que queremos.

Vetamos as abordagens ad hoc de baixa tecnologia, porque todos concordamos que não são um caminho sustentável de longo prazo.


### Implicações

Desenvolvedores talvez precisem rastrear segredos em dois lugares: Bitwarden para acesso orientado a usuários e Vault para acesso orientado a sistemas.


## Relacionado


### Decisões relacionadas

A decisão de qual servidor de CI/CD deve incluir prova de capacidade para acessar segredos.

Precisaremos decidir como gerenciar os segredos, em termos de políticas, rotações, organizações etc.


### Requisitos relacionados

Os segredos terão requisitos relacionados para conformidade, auditoria e onboarding/offboarding de RH.


### Artefatos relacionados

Esperamos talvez exportar alguns segredos para variáveis de ambiente.


### Princípios relacionados

Facilmente reversível.

Facilmente paralelo, ou seja, é fácil usar uma variedade de gerenciadores de senha.

Barato de experimentar, ou seja, há um teste gratuito e nenhum compromisso.


## Notas

Notas de avaliação aqui. As notas são todas comentários públicos em vários fóruns de discussão de devops.


### Vault by HashiCorp

Vault é exatamente o que você quer aqui.

Mas não coloque Vault direto em produção; coloque-o primeiro em um ambiente de teste, porque a documentação da HashiCorp pode ser bem deficiente, mesmo que os produtos deles sejam incríveis.

Curva de aprendizado muito íngreme e não é trivial colocá-lo de pé.

A configuração inicial é um pouco trabalhosa. Mas vale muito a pena, e a comunidade dará suporte suficiente para você seguir em frente.

Documentação horrível, mas há muitos guias online de pessoas configurando a ferramenta; se você juntar alguns deles, terá uma configuração funcionando.

A configuração inicial exigiu mexer nos helm charts deles (vault e consul). Embora tecnicamente você possa usar muitos outros back-ends, eu realmente não recomendo. O back-end/consul pode ser minúsculo se você não tiver muitos dados para armazenar.

Definitivamente fique confortável/familiarizado com o uso da CLI, porque a GUI é mais como uma prova de conceito/portal de propaganda para a edição enterprise deles.

O fato de você não poder simplesmente "preencher tudo" é incômodo. Por exemplo, se você tem 5 campos, precisa adicionar manualmente cada campo para cada item. Então não é como se você pré-definisse campos para uma categoria específica e preenchesse esses campos para todos os itens daquela categoria; é mais como "você gera tudo toda vez", o que (na minha opinião) é uma chateação.

Talvez você também queira olhar o goldfish como uma UI em cima do vault. Torna bem agradável trazer sua equipe para ele. Eles também têm uma demo. 1. Configure consul. 2. Configure vault apontando para consul. 3. Configure goldfish apontando para vault. 3. Configure algum cron job para executar snapshot do consul para backups.



### LastPass

LastPass Teams. Nós usamos, tem templates customizados, ACL, nada faltando IMO.

Implementei LastPass na minha organização e dou uma nota C+/B-. O maior problema ultimamente é falta de confiabilidade. Nos últimos 90 dias houve várias horas em que vaults foram forçados para modo offline. Isso não é ideal para minha organização por termos, literalmente, mais de 4.000 senhas armazenadas em mais de 20 pastas compartilhadas. Como você pode imaginar, com tantas senhas pelo menos algumas são atualizadas ou adicionadas diariamente. Temos um plano de DR se os problemas durarem mais de uma ou duas horas: um script assina e criptografa todas as noites um dump CSV do vault que pode ser importado no keepass.

LastPass teve falhas não reportadas de serviço degradado: login "funciona", mas não puxa sites, recursos aleatórios quebram no painel de administração e chaves não são compartilhadas corretamente para novas pastas compartilhadas de nível superior. Tenho um usuário específico de "key push"/backup que está em todos os grupos. Normalmente fazer login como esse usuário corrige quaisquer problemas de compartilhamento de chaves, mas não quando o serviço está degradado, apesar do que a página de status diz...

Para integração, pode ser fácil se você tiver ACLs adequadas com um modelo de menor privilégio, por exemplo, se um usuário tiver leitura e escrita e somente leitura em uma entrada ou pasta, ele recebe apenas permissões de somente leitura. Infelizmente, as ACLs da minha organização não são as melhores, então acabei usando a API de provisionamento JSON e ~500 linhas de python devido à natureza dependente das nossas centenas de ACLs, que não mapeiam bem para o modelo de menor privilégio. Acabei pegando todas as ACLs em que um usuário estava e fazendo uma espécie de caminhada de dependências.

Se sua estrutura de ACL ou grupos já estiver construída com uma estrutura de menor privilégio em mente, a ferramenta de sincronização AD/LDAP para Windows funcionará bem.

Fale com a equipe de vendas deles e eles podem conseguir um trial Enterprise mais longo. Certifique-se de entender completamente suas limitações antes de tomar a decisão. Tivemos um bom número de dores de crescimento, mas, além de indisponibilidades ou prejuízos do lado do servidor, tem sido incrivelmente tranquilo.


### Bitwarden

Bitwarden tem boas ferramentas em torno dele (WebUI, CLI, Mobile, Desktop). Self-hosted e bastante fácil de configurar. Documentação razoavelmente boa e ferramenta recomendada pela PrivacyTools.


### EnvKey

https://www.envkey.com/ É um SaaS. Muito fácil de implementar, integrar e gerenciar.

Recursos:

  * Proteja chaves de API e credenciais.

  * Mantenha a configuração sincronizada em todos os lugares.

  * Gerenciamento inteligente de configuração e segredos com criptografia end-to-end.

  * Previna compartilhamento inseguro e dispersão de configuração.

  * Integre em minutos.

Capacidades:

  * Gerencie configuração e níveis de acesso para todos os seus apps, ambientes e equipes em um só lugar.

  * Configure qualquer ambiente de desenvolvimento ou servidor com apenas uma variável de ambiente.

Prós:

  * Boa página inicial.

  * Proposta de valor clara.

  * Web app visualmente excelente.

  * Dados de exemplo superiores, por exemplo Algolia, AWS, Datadog, GitHub, Stripe etc.

  * Conversei com o fundador por 30 min sobre a empresa, UI etc. Dane parece bem informado, honesto sobre prós/contras e um parceiro viável.

  * A empresa é essencialmente uma típica empresa Y Combinator, com 1 fundador. Levantou US$120K em 2018-01.

  * Foco em chegar a recursos enterprise, especialmente migrando de hospedagem em cloud da EnvKey para on-prem ou BYOC.

  * Caminho potencial adiante começando com EnvKey pela facilidade de uso, depois adicionando Vault mais tarde (ou em paralelo).


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant é um serviço open source de gerenciamento de segredos que fornece armazenamento e acesso a segredos de maneira segura e amigável para usuários, vindo dos desenvolvedores da Lyft.

Autenticação KMS: Confidant resolve o problema de ovo e galinha da autenticação usando AWS KMS e IAM para permitir que roles IAM gerem tokens de autenticação seguros que podem ser verificados pelo Confidant. Confidant também gerencia grants KMS para suas roles IAM, o que permite que as roles IAM gerem tokens que podem ser usados para autenticação serviço-a-serviço ou para passar mensagens criptografadas entre serviços.

Criptografia em repouso de segredos versionados: Confidant armazena segredos de forma append-only no DynamoDB, gerando uma chave de dados KMS única para cada revisão de cada segredo, usando criptografia autenticada simétrica Fernet.

Uma interface web amigável para gerenciar segredos: Confidant fornece uma interface web AngularJS que permite que usuários finais gerenciem facilmente segredos, os mapeamentos de segredos para serviços e o histórico de mudanças.


### Devolutions Password Server

https://server.devolutions.net/

Acesso seguro, gerenciado e monitorado a contas e sessões privilegiadas.

Um vault de senhas abrangente e altamente seguro que permite controlar o acesso às suas contas privilegiadas, ao mesmo tempo em que melhora a visibilidade geral da rede para sysadmins e fornece uma experiência fluida para usuários finais.

Recursos: vault centralizado de senhas da organização, vault privado específico por usuário, gerenciador de senhas, injeção de credenciais,
integração com Active Directory, controle de acesso baseado em roles, autenticação de dois fatores, pronto para enterprise, restrições de IP, capacidades de gerenciamento, gerador de senhas automatizado, acesso por aplicativo móvel, histórico de senhas, relatórios de acesso, alertas por e-mail.

  * suporta criptografia de dados

  * suporta múltiplos esquemas de autenticação, incluindo LDAP, O365 e usuários locais COM suporte a MFA de múltiplas fontes

  * múltiplos repositórios/vaults com controles de acesso granulares para múltiplas equipes

  * Web UI moderna

  * vaults privados de credenciais e conexões para creds/conexões pessoais

  * apps móveis para IOS/Android

  * logs de auditoria para cada entrada, quem/o quê/quando, com um prompt opcional para por que estão acessando

  * templates customizáveis (embora suportem nativamente centenas de tipos de conexão)

  * toneladas de outros recursos e um cliente Windows/Mac robusto (Remote Desktop Manager) com o qual você pode sincronizar e que amplia muito as opções... conexões com um clique

  * preço não é tão ruim: até 15 usuários custa US$500 por ano para o password server


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Recursos da versão on-premise:

  * Controle total sobre seus sistemas e infraestrutura de segurança end-to-end

  * Implante software dentro do seu data center on-premise ou em sua própria instância de cloud privada virtual

  * Atenda a obrigações legais e regulatórias que exigem que todos os dados e sistemas residam on-premise

Recursos da versão cloud:

  * O modelo software-as-a-service permite que você se cadastre e comece imediatamente

  * Escalabilidade elástica conforme você cresce

  * Controles e redundância entregues pela Azure com SLA de 99,9% de uptime

Feedback de usuários:

  * Usávamos esse produto. Ele era muito facilmente contornado, e as regras só funcionam para pessoas espertas. Usuários preguiçosos ou burros podem estragar tudo facilmente em uma área de equipe. Os preços são negociáveis quando você fala com eles.

  * Você pode rodá-lo usando SQL Express e uma máquina Win 7.

  * Barato.
