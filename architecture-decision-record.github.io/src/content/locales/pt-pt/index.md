# Registro de decisão de arquitetura (ADR)

Um registro de decisão de arquitetura (ADR) é um documento que registra uma decisão de arquitetura importante, junto com seu contexto e suas consequências.

> [!IMPORTANT]
> Faça sua própria diligência prévia sobre estes recursos antes de usá-los em quaisquer sistemas críticos.

Conteúdo:

- [O que é um registro de decisão de arquitetura?](#o-que-é-um-registro-de-decisão-de-arquitetura)
- [Como começar a usar ADRs](#como-começar-a-usar-adrs)
- [Como começar a usar ADRs com ferramentas](#como-começar-a-usar-adrs-com-ferramentas)
- [Como começar a usar ADRs com git](#como-começar-a-usar-adrs-com-git)
- [Skills do Claude Code para ADRs](#skills-do-claude-code-para-adrs)
- [Convenções de nomes de arquivo](#convenções-de-nomes-de-arquivo)
- [Sugestões para escrever bons ADRs](#sugestões-para-escrever-bons-adrs)
- [Modelos de exemplo de ADR](#modelos-de-exemplo-de-adr)
- [Conselhos de trabalho em equipe para ADRs](#conselhos-de-trabalho-em-equipe-para-adrs)
- [Perguntas de trabalho em equipe para ADRs](#perguntas-de-trabalho-em-equipe-para-adrs)
- [Conceitos do próximo passo para ADRs](#conceitos-do-próximo-passo-para-adrs)
- [Diagramas, visões e pontos de vista de arquitetura](#diagramas-visões-e-pontos-de-vista-de-arquitetura)
- [Funções de aptidão para decisões como código](#funções-de-aptidão-para-decisões-como-código)
- [Proteções de decisão para pull requests](#proteções-de-decisão-para-pull-requests)
- [Para mais informações](#para-mais-informações)

Modelos:

- [Modelo de registro de decisão de Jeff Tyree e Art Akerman](modelos/modelo-de-registro-de-decisão-de-jeff-tyree-e-art-akerman/)
- [Modelo de registro de decisão de Michael Nygard](modelos/modelo-de-registro-de-decisão-de-michael-nygard/)
- [Modelo de registro de decisão do EdgeX](modelos/modelo-de-registro-de-decisão-do-edgex/)
- [Modelo de registro de decisão do arc42](modelos/modelo-de-registro-de-decisão-do-arc42/)
- [Modelo de registro de decisão para padrão alexandrino](modelos/modelo-de-registro-de-decisão-para-padrão-alexandrino/)
- [Modelo de registro de decisão para caso de negócio](modelos/modelo-de-registro-de-decisão-para-caso-de-negócio/)
- [Modelo de registro de decisão do projeto MADR](modelos/modelo-de-registro-de-decisão-do-projeto-madr/)
- [Modelo de registro de decisão usando Planguage](modelos/modelo-de-registro-de-decisão-usando-planguage/)
- [Modelo de registro de decisão de Paulo Merson](https://github.com/pmerson/ADR-template)
- [Modelo de registro de decisão de Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Modelo de registro de decisão de Gareth Morgan](modelos/modelo-de-registro-de-decisão-de-gareth-morgan/)
- [Modelo de registro de decisão do GIG Cymru NHS Wales](modelos/modelo-de-registro-de-decisão-do-gig-cymru-nhs-wales/)
- [Modelo de registro de decisão para decisões técnicas importantes (ITDs), de Ignacio Larrañaga](modelos/modelo-de-registro-de-decisão-para-decisões-técnicas-importantes/)

Exemplos:

- [Framework CSS](exemplos/framework-css/)
- [Configuração por variáveis de ambiente](exemplos/configuração-por-variáveis-de-ambiente/)
- [Métricas, monitores, alertas](exemplos/métricas-monitores-alertas/)
- [Microsoft Azure DevOps](exemplos/microsoft-azure-devops/)
- [Monorepo ou multirepo](exemplos/monorepo-ou-multirepo/)
- [Linguagens de programação](exemplos/linguagens-de-programação/)
- [Armazenamento de segredos](exemplos/armazenamento-de-segredos/)
- [Formato de carimbo de data e hora](exemplos/formato-de-carimbo-de-data-e-hora/)
- [Muitos mais...](exemplos/)

## O que é um registro de decisão de arquitetura?

Um **registro de decisão de arquitetura** (ADR) é um documento que captura uma decisão arquitetural importante tomada, juntamente com seu contexto e suas consequências.

Uma **decisão de arquitetura** (AD) é uma escolha de design de software que atende a um requisito significativo.

Um **registro de decisões de arquitetura** (ADL) é a coleção de todos os ADRs criados e mantidos para um projeto (ou organização) específico.

Um **requisito arquiteturalmente significativo** (ASR) é um requisito que tem um efeito mensurável na arquitetura de um sistema de software.

Tudo isso está dentro do tópico da **gestão do conhecimento de arquitetura** (AKM).

O objetivo deste documento é fornecer uma visão geral rápida dos ADRs, de como criá-los e de onde procurar mais informações.

Abreviações:

  * **AD**: decisão de arquitetura

  * **ADL**: registro de decisões de arquitetura

  * **ADR**: registro de decisão de arquitetura

  * **AKM**: gestão do conhecimento de arquitetura

  * **ASR**: requisito arquiteturalmente significativo

## Como começar a usar ADRs

Para começar a usar ADRs, converse com seus colegas de equipe sobre estas áreas.

Identificação da decisão:

  * Quão urgente e quão importante é o AD?

  * Ele precisa ser tomado agora ou pode esperar até que se saiba mais?

  * Tanto a experiência pessoal e coletiva quanto métodos e práticas de design reconhecidos podem ajudar na identificação de decisões.

  * Idealmente, mantenha uma lista de decisões a tomar que complemente a lista de tarefas do produto.

Tomada de decisão:

  * Existem várias técnicas de tomada de decisão, tanto gerais quanto específicas de arquitetura de software, por exemplo, o mapeamento de diálogo.

  * A tomada de decisão em grupo é um tópico de pesquisa ativo.

Promulgação e aplicação da decisão:

  * Os ADs são usados no design de software; portanto, precisam ser comunicados e aceitos pelas partes interessadas do sistema que o financiam, desenvolvem e operam.

  * Estilos de codificação arquiteturalmente evidentes e revisões de código que se concentram em preocupações e decisões arquiteturais são duas práticas relacionadas.

  * Os ADs também precisam ser (re)considerados ao modernizar um sistema de software na evolução do software.

Compartilhamento da decisão (opcional):

  * Muitos ADs se repetem entre projetos.

  * Portanto, as experiências com decisões passadas, boas e ruins, podem ser ativos reutilizáveis valiosos ao empregar uma estratégia explícita de gestão do conhecimento.

Documentação da decisão:

  * Existem muitos modelos e ferramentas para captura de decisões.

  * Veja as comunidades ágeis, por exemplo, os ADRs de M. Nygard.

  * Veja os processos tradicionais de engenharia de software e design de arquitetura, por exemplo, os layouts de tabela sugeridos pela IBM UMF e por Tyree e Akerman, da CapitalOne.

Para saber mais:

  * Os passos acima foram adotados do verbete da Wikipédia [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Como começar a usar ADRs com ferramentas

- [MySpec](https://myspec.dev) — Plataforma automatizada de especificação e decisão de arquitetura que estrutura a constituição do projeto, a arquitetura técnica e os ADRs em Markdown limpo servido via MCP.

Você pode começar a usar ADRs com ferramentas da maneira que quiser.

Por exemplo:

  * Se você gosta de usar o Google Drive e a edição online, pode criar um Google Doc ou uma Google Sheet.

  * Se você gosta de usar controle de versão de código-fonte, como o git, pode criar um arquivo para cada ADR.

  * Se você gosta de usar ferramentas de planejamento de projetos, como o Atlassian Jira, pode usar o rastreador de planejamento da ferramenta.

  * Se você gosta de usar wikis, como o MediaWiki, pode criar uma wiki de ADRs.

## Como começar a usar ADRs com git

Se você gosta de usar o controle de versão git, veja como gostamos de começar a usar ADRs com git em um projeto de software típico com código-fonte.

Crie um diretório para os arquivos de ADR:

```sh
$ mkdir adr
```

Para cada ADR, crie um arquivo de texto, como `database.txt`:

```sh
$ vi database.txt
```

Escreva o que quiser no ADR. Veja os modelos neste repositório para ter ideias.

Faça commit do ADR no seu repositório git.

## Skills do Claude Code para ADRs

Este repositório inclui duas skills do [Claude Code](https://claude.com/claude-code) em [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), para que um agente de programação com IA possa escrever e manter ADRs do jeito que este projeto recomenda:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — de uso geral, para qualquer pessoa que escreva um ADR em qualquer projeto. Ajuda a decidir se uma decisão precisa de um ADR, cria um diretório `adr/` ou `decisions/`, nomeia o arquivo, escolhe um modelo entre os onze esqueletos incluídos e escreve seções sólidas de contexto, decisão e consequências.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — específica para quem mantém este repositório. Documenta a estrutura do repositório, a convenção de espelhar README e locales e os passos exatos para adicionar um novo modelo, exemplo ou link de ferramenta.

Para usar uma skill, copie a pasta dela para `.claude/skills/` na raiz do repositório em que você está trabalhando (ou para `~/.claude/skills/` para deixá-la disponível em todos os projetos) e peça ao Claude Code que escreva ou revise um ADR.

## Convenções de nomes de arquivo

Se você optar por criar seus ADRs usando arquivos de texto comuns, talvez queira definir sua própria convenção de nomes de arquivo de ADR.

Preferimos usar uma convenção de nomes de arquivo que tenha um formato específico.

Exemplos:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Nossa convenção de nomes de arquivo:

  * O nome tem uma locução verbal no imperativo do presente. Isso ajuda a legibilidade e combina com o formato das nossas mensagens de commit.

  * O nome usa letras minúsculas e hifens (igual a este repositório). É um equilíbrio entre legibilidade e usabilidade do sistema.

  * A extensão é markdown. Isso pode ser útil para formatar facilmente.

## Sugestões para escrever bons ADRs

Características de um bom ADR:

* Justificativa: explique os motivos para tomar o AD em questão. Isso pode incluir o contexto (veja abaixo), prós e contras de várias escolhas potenciais, comparações de recursos, discussões de custo/benefício e mais.

* Específico: cada ADR deve tratar de um AD, não de vários ADs.

* Carimbos de data e hora: identifique quando cada item do ADR foi escrito. Isso é especialmente importante para aspectos que podem mudar com o tempo, como custos, cronogramas, escalabilidade e similares.

* Imutável: não altere informações existentes em um ADR. Em vez disso, emende o ADR adicionando novas informações ou substitua o ADR criando um novo ADR.

Características de uma boa seção “Contexto” em um ADR:

* Explique a situação da sua organização e as prioridades de negócio.

* Inclua justificativas e considerações baseadas na composição social e de habilidades das suas equipes.

* Inclua prós e contras relevantes e descreva-os em termos alinhados às suas necessidades e objetivos.

Características de uma boa seção “Consequências” em um ADR:

* Explique o que decorre de tomar a decisão. Isso pode incluir efeitos, resultados, saídas, desdobramentos e mais.

* Inclua informações sobre quaisquer ADRs subsequentes. É relativamente comum um ADR desencadear a necessidade de mais ADRs, como quando um ADR faz uma grande escolha abrangente, o que por sua vez cria necessidade de mais decisões menores.

* Inclua quaisquer processos de revisão pós-ação. É típico as equipes revisarem cada ADR um mês depois, para comparar as informações do ADR com o que aconteceu na prática, a fim de aprender e crescer.

Um novo ADR pode tomar o lugar de um ADR anterior:

* Quando um AD é tomado e substitui ou invalida um ADR anterior, deve-se criar um novo ADR

## Modelos de exemplo de ADR

Modelos de exemplo de ADR que coletamos na rede:

- [Modelo de ADR de Michael Nygard](modelos/modelo-de-registro-de-decisão-de-michael-nygard/) (simples e popular)

- [Modelo de ADR de Jeff Tyree e Art Akerman](modelos/modelo-de-registro-de-decisão-de-jeff-tyree-e-art-akerman/) (mais sofisticado)

- [Modelo de ADR para o padrão Alexandrian](modelos/modelo-de-registro-de-decisão-para-padrão-alexandrino/) (simples, com detalhes de contexto)

- [Modelo de ADR para estudo de viabilidade](modelos/modelo-de-registro-de-decisão-para-caso-de-negócio/) (mais voltado a MBA, com custos, SWOT e mais opiniões)

- [Modelo de ADR do projeto Markdown Any Decision Records (MADR)](modelos/modelo-de-registro-de-decisão-do-projeto-madr/) (versão simples e versão elaborada; esta última enfatiza as opções e seus prós e contras)

- [Modelo de ADR usando Planguage](modelos/modelo-de-registro-de-decisão-usando-planguage/) (mais voltado à garantia de qualidade)

- [Modelo para Decisões Técnicas Importantes (ITDs) de Ignacio Larrañaga](modelos/modelo-de-registro-de-decisão-para-decisões-técnicas-importantes/) (enxuto e com a decisão em primeiro lugar, otimizado para revisão executiva rápida)

## Conselhos de trabalho em equipe para ADRs

Se você está pensando em usar registros de decisão com sua equipe, aqui estão alguns conselhos que aprendemos trabalhando com muitas equipes.

Você tem a oportunidade de liderar seus colegas conversando juntos sobre o “porquê”, em vez de impor o “quê”. Por exemplo, registros de decisão são uma forma de as equipes pensarem de modo mais inteligente e se comunicarem melhor; registros de decisão não têm valor se forem apenas uma exigência burocrática imposta após o fato.

Algumas equipes preferem muito mais o nome “decisões” (decisions) à abreviação “ADRs”. Quando algumas equipes usam o nome de diretório “decisions”, é como se uma lâmpada se acendesse, e a equipe começa a colocar mais informações no diretório, como decisões de fornecedores, decisões de planejamento, decisões de cronograma etc. Todos esses tipos de informação podem usar o mesmo modelo. Nossa hipótese é que as pessoas aprendem mais rápido com palavras (“decisões”) do que com abreviações (“ADRs”), que as pessoas ficam mais motivadas a escrever documentos em andamento quando a palavra “registro” é removida e que alguns desenvolvedores e alguns gerentes não gostam da palavra “arquitetura”.

Em teoria, a imutabilidade é ideal. Na prática, a mutabilidade funcionou melhor para as nossas equipes. Inserimos a nova informação no ADR existente, com um carimbo de data e uma nota de que a informação chegou depois da decisão. Esse tipo de abordagem leva a um “documento vivo” que todos nós podemos atualizar. Atualizações típicas ocorrem quando recebemos informações graças a novos colegas, novas ofertas, resultados reais dos nossos usos ou mudanças de terceiros posteriores à decisão, como capacidades de fornecedores, planos de preços, contratos de licença etc.

## Perguntas de trabalho em equipe para ADRs

### Quem pode criar um ADR?

Considere áreas como pessoas específicas, papéis específicos, equipes específicas ou departamentos específicos; considere também se há pessoas, papéis, equipes ou departamentos que podem encomendar um ADR, ou seja, solicitar um que outra pessoa irá redigir. 

Exemplo de resposta: qualquer pessoa da nossa organização que tenha lido a página README sobre registros de decisão de arquitetura pode propor um ADR, ou seja, pode começar a escrevê-lo e compartilhá-lo com a equipe.

### O que justifica abrir um ADR?

Considere áreas como as formas de trabalho das equipes da sua organização, a estrutura do seu sistema de software, a coordenação entre equipes, a manutenibilidade de longo prazo, as interfaces externas, quem você quer beneficiar e similares. 

Exemplo de resposta: queremos criar um ADR quando queremos que desenvolvedores futuros entendam o “porquê” do que estamos fazendo.

### O que justifica não abrir um ADR?

Considere áreas como decisões que não são sobre arquitetura, ou são minúsculas, por exemplo de risco mínimo, autocontidas ou de um único desenvolvedor, ou já estão totalmente cobertas em outro lugar, como em padrões, políticas ou documentação, ou são temporárias, como soluções paliativas, provas de conceito ou experimentos. 

Exemplo de resposta: queremos dispensar um ADR quando uma decisão é limitada em escopo, tempo, risco e custo, ou já está coberta em outro lugar.

### Qual é o ciclo de vida de um ADR?

Considere áreas como o processo de criação, o processo de pesquisa, o processo de decisão, o processo de implementação e o processo de desativação. Considere como acompanhar o ciclo de vida do ADR ao longo do tempo, como mover o ADR de um estado para o próximo e também como comunicar isso às partes interessadas. 

Exemplo de resposta: queremos que um ADR tenha cinco estágios de ciclo de vida: Iniciando → Pesquisando → Avaliando → Implementando → Mantendo → Desativando.

### Quais são os critérios para as etapas do ciclo de vida de um ADR?

Considere áreas como os critérios de aceitação de um ADR, ou seja, como você sabe que ele está bom o suficiente para avançar de uma etapa do ciclo de vida para a seguinte? O problema está claramente articulado? As alternativas foram consideradas? Os trade-offs estão bem compreendidos e documentados?
Todo o contexto relevante está presente? Todas as partes interessadas relevantes estão envolvidas? Todo o feedback foi incorporado? 

Exemplo de resposta: queremos que um ADR seja votado pelas partes interessadas quando a equipe ativa tiver 1) concluído sua pesquisa, 2) concluído sua avaliação, 3) publicado a proposta de ADR para as partes interessadas com um pedido de comentários e um prazo de uma semana, 4) incorporado e tratado todos os comentários das partes interessadas.

### Quais papéis e responsabilidades interagem com um ADR?

Considere papéis como proponente, pesquisador, avaliador, revisor, aprovador, mantenedor e similares. Considere responsabilidades como comunicação com as partes interessadas, garantia de que as expectativas sejam atendidas, compartilhamento no site ou na intranet e revisão periódica do trabalho, especialmente quando ocorrerem mudanças relevantes.

Exemplo de resposta: queremos que cada ADR sempre tenha uma pessoa de contato principal, uma pessoa de contato secundária e uma equipe responsável; elas são responsáveis por comunicações, publicações, manutenção, revisão periódica pelo menos uma vez por ano e eventual desativação, conforme necessário.

### Como a governança interage com um ADR?

Considere áreas como as formas de trabalho da sua organização, quaisquer necessidades especiais de conformidade, por exemplo em aspectos jurídicos ou de recursos humanos, e como você quer lidar com consenso versus conflito versus escalonamento. Existem áreas, pessoas ou equipes que podem ter mais influência que outras sobre um ADR, como poder aprová-lo, votar nele ou vetá-lo?

Exemplo de resposta: a governança de um ADR obedece a esta ordem de prioridade: o CEO, o CTO, o CLO, a equipe que implementa um ADR, os especialistas da equipe mais conhecedores do ADD. Ninguém mais tem governança, a menos que descrito no ADR. 

### Quais princípios interagem com um ADR?

Considere áreas como as formas de trabalho da sua organização, que incluem agir rápido versus agir devagar, consenso de decisão versus conflito de decisão, preferências de risco versus preferências de segurança, discussão pública versus discussão privada e similares.

Exemplo de resposta: usamos os princípios de liderança de viés para a ação, discordar e comprometer-se, estimativas de 70% são boas o suficiente para decisões facilmente reversíveis e facilmente isoláveis, e formas de trabalho públicas, com exceção de informações confidenciais conforme descrito no acordo de confidencialidade da nossa organização.

## Conceitos do próximo passo para ADRs

O [Arc42](https://arc42.org/) responde a duas perguntas de forma pragmática e pode ser adaptado às suas necessidades. O que você deve documentar/comunicar sobre a sua arquitetura? Como deve documentar/comunicar? O Arc42 inclui registros de decisão de arquitetura e orientações sobre metas, restrições, contextos, qualidade, riscos e mais.

[O modelo C4](https://c4model.com/) é uma abordagem fácil de aprender e amigável para desenvolvedores de diagramar a arquitetura de software. O C4 é um conjunto de diagramas hierárquicos de contexto, contêineres, componentes e código, além de diagramas de apoio para panorama de sistemas, dinâmica e implantação.

## Diagramas, visões e pontos de vista de arquitetura

Um diagrama de arquitetura é chamado de "visão de arquitetura".

Uma "visão de arquitetura" é uma instância de um "ponto de vista de arquitetura".

Um "ponto de vista de arquitetura" considera um público específico com preocupações específicas.

Exemplos de pontos de vista, visões e diagramas de arquitetura:

- Capacidades de negócio

- Processos de negócio de alto nível

- [Fluxos de valor](https://en.wikipedia.org/wiki/Value_stream)

- Funções de software mapeadas para componentes de aplicação

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Diagrama de contexto (TO-BE / AS-IS)

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Diagrama de contêineres (TO-BE / AS-IS)

- [Diagrama entidade-relacionamento](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) para mapear entidades de dados para componentes de aplicação

- [Diagramas de sequência](https://en.wikipedia.org/wiki/Sequence_diagram) para descrever fluxos funcionais dentro dos sistemas e nas integrações

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagramas para descrever fluxos de dados entre componentes de aplicação

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagramas para descrever processos de negócio / cenários de usuário

- [Gerenciamento de Identidade e Acesso](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) diagramas

- [Controle de Acesso Baseado em Papéis](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) diagramas com papéis por componente de aplicação

- [Controle de Acesso Baseado em Atributos](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) diagramas com atributos por componente de aplicação

- Diagramas de privacidade

Diagramas relacionados:

- Um diagrama de casos de uso mostra casos de uso à gerência/aos clientes, o que precede os requisitos, que precedem a arquitetura de software.

- Um diagrama de implantação mostra o hardware/os computadores físicos nos quais os componentes de software são implantados.
- Um diagrama de fluxo de dados mostra como os dados se movem pelo sistema e são transformados.
- Um diagrama de sequência é usado para mostrar como protocolos como HTTP funcionam em um eixo de tempo.

- Um diagrama de atividades retrata o fluxo de trabalho das atividades que um sistema de software executa, como uma IA de NPC.

## Funções de aptidão para decisões como código

Funções de aptidão (fitness functions) são verificações automatizadas e objetivas, escritas com código de programação, que verificam se as decisões estão sendo mantidas.

- As funções de aptidão tornam as decisões testáveis e asseguráveis.

- As funções de aptidão para decisões podem ajudar muito a garantia de qualidade, os processos regulatórios e os objetivos de governança.

### Como as funções de aptidão se conectam às decisões

Um registro de decisão documenta a decisão, enquanto uma função de aptidão a assegura.

- Exemplo de decisão: usamos event sourcing para requisitos de auditoria.

- Exemplo de função de aptidão: usamos o servidor de integração contínua para testar que toda mudança de estado deve produzir eventos.

### Por que as funções de aptidão ajudam as decisões

Medições objetivas: as funções de aptidão passam ou falham, então o trabalho fica visível e claro.

Uso contínuo: as funções de aptidão são suas regras vivas, executadas a cada commit e build.

Confiança para refatorar: as funções de aptidão detectam automaticamente erros nas regras de decisão.

Governança escalável: as funções de aptidão asseguram padrões sem criar gargalos.

### As funções de aptidão podem usar IA?

As funções de aptidão podem aproveitar LLMs de IA para decisões, fazendo perguntas sobre o seu trabalho,
como seus planos, código, esquemas, APIs e mais:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Teste unitário de arquitetura

[ArchUnit](https://www.archunit.org/): verifique regras de arquitetura de código Java usando qualquer framework de teste unitário Java comum.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): verifique regras de arquitetura de código TypeScript e JavaScript usando Jest, Vitest, Jasmine etc.

## Proteções de decisão para pull requests

O [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
mostra automaticamente os registros de decisão certos no momento certo, ou seja, quando um
desenvolvedor está modificando o código que essas decisões cobrem. Em vez de esperar que os desenvolvedores
leiam uma pasta de documentos antes de mesclar, o contexto relevante aparece diretamente no pull request.

Isso funciona para qualquer tipo de registro de decisão: decisões de arquitetura, de dados, de conformidade, clínicas e médicas, de segurança e mais.

Funciona com qualquer sistema de CI (GitLab, Jenkins, CircleCI) e como hook de pre-commit.
Código aberto. Licença MIT.

O [ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) é uma GitHub
Action que reprova um pull request quando caminhos de código monitorados mudam sem que um
registro de decisão de arquitetura seja adicionado ou atualizado. As isenções são explícitas: uma linha
`ADR-Exempt:` com um motivo passa pelo portão e é escrita no resumo do job. Independe de modelo, sem dependências. Código aberto. Licença MIT.

## Para mais informações

Introdução:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Modelos:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Aprofundamento:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - aula mensal gratuita de arquitetura de software

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Ferramentas:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Orientações específicas de empresas:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Exemplos:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Vídeos:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcasts:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Livros:

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

Veja também:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Um formato YAML/JSON neutro quanto a fornecedores e legível por máquina para representar decisões com raciocínio explícito, premissas, estado cognitivo e trade-offs. Complementa os ADRs ao adicionar raciocínio estruturado e validável à documentação de decisões.
