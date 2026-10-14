# Registros de decisão de arquitetura (ADRs)

Um registro de decisão de arquitetura (ADR) documenta uma decisão arquitetural importante, incluindo seu contexto e suas consequências.

> [!IMPORTANT]
> Avalie estas referências de forma independente antes de utilizá-las em sistemas críticos.

Conteúdo:

- [O que é um registro de decisão de arquitetura?](#o-que-é-um-registro-de-decisão-de-arquitetura)
- [Como começar a usar ADRs](#como-começar-a-usar-adrs)
- [Como começar a usar ADRs com ferramentas](#como-começar-a-usar-adrs-com-ferramentas)
- [Como começar a usar ADRs com Git](#como-começar-a-usar-adrs-com-git)
- [Skills do Claude Code para ADRs](#skills-do-claude-code-para-adrs)
- [Convenções de nomes de arquivos para ADRs](#convenções-de-nomes-de-arquivos-para-adrs)
- [Sugestões para escrever bons ADRs](#sugestões-para-escrever-bons-adrs)
- [Exemplos de modelos de ADR](#exemplos-de-modelos-de-adr)
- [Conselhos de trabalho em equipe para ADRs](#conselhos-de-trabalho-em-equipe-para-adrs)
- [Perguntas de trabalho em equipe para ADRs](#perguntas-de-trabalho-em-equipe-para-adrs)
- [Próximos conceitos para explorar](#próximos-conceitos-para-explorar)
- [Diagramas, visões e pontos de vista de arquitetura](#diagramas-visões-e-pontos-de-vista-de-arquitetura)
- [Funções de aptidão para decisões como código](#funções-de-aptidão-para-decisões-como-código)
- [Proteções de decisões em pull requests](#proteções-de-decisões-em-pull-requests)
- [Para saber mais](#para-saber-mais)

Modelos:

- [Modelo de registro de decisão por Jeff Tyree e Art Akerman](modelos/modelo-de-registro-de-decisao-por-jeff-tyree-e-art-akerman/)
- [Modelo de registro de decisão por Michael Nygard](modelos/modelo-de-registro-de-decisao-por-michael-nygard/)
- [Modelo de registro de decisão por EdgeX](modelos/modelo-de-registro-de-decisao-por-edgex/)
- [Modelo de registro de decisão por arc42](modelos/modelo-de-registro-de-decisao-por-arc42/)
- [Modelo de registro de decisão para padrão Alexandrino](modelos/modelo-de-registro-de-decisao-para-padrao-alexandrino/)
- [Modelo de registro de decisão para caso de negócio](modelos/modelo-de-registro-de-decisao-para-caso-de-negocio/)
- [Modelo de registro de decisão do Projeto MADR](modelos/modelo-de-registro-de-decisao-do-projeto-madr/)
- [Modelo de registro de decisão usando Planguage](modelos/modelo-de-registro-de-decisao-usando-planguage/)
- [Modelo de Paulo Merson](https://github.com/pmerson/ADR-template)
- [Modelo Y-Statements de Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Modelo de registro de decisão por Gareth Morgan](modelos/modelo-de-registro-de-decisao-por-gareth-morgan/)
- [Modelo de registro de decisão por GIG Cymru NHS Wales](modelos/modelo-de-registro-de-decisao-por-gig-cymru-nhs-wales/)
- [Modelo de registro de decisão para Decisões Técnicas Importantes (ITDs) por Ignacio Larrañaga](modelos/modelo-de-registro-de-decisao-para-decisoes-tecnicas-importantes/)

Exemplos:

- [Semana de trabalho de 4 dias](exemplos/semana-de-trabalho-de-4-dias/)
- [Desenvolvimento ágil de software](exemplos/desenvolvimento-agil-de-software/)
- [Amazon Web Services](exemplos/amazon-web-services/)
- [API usando JSON vs. gRPC](exemplos/api-usando-json-vs-grpc/)
- [Opções de autenticação e autorização](exemplos/opcoes-de-autenticacao-e-autorizacao/)
- [Framework de automação de navegador para testes E2E: Playwright vs Selenium](exemplos/framework-de-automacao-de-navegador-para-testes-e2e-playwright-vs-selenium/)
- [Biblioteca de gráficos para visualização de dados usando TypeScript e JSON](exemplos/biblioteca-de-graficos-para-visualizacao-de-dados-usando-typescript-e-json/)
- [Escolha de uma tecnologia de banco de dados](exemplos/escolha-de-tecnologia-de-banco-de-dados/)
- [Veja mais exemplos](exemplos/)

## O que é um registro de decisão de arquitetura?

Um **registro de decisão de arquitetura** (ADR) é um documento que captura uma decisão de arquitetura importante tomada junto com seu contexto e suas consequências.

Uma **decisão de arquitetura** (AD) é uma escolha de design de software que trata de um requisito significativo.

Um **log de decisões de arquitetura** (ADL) é a coleção de todas as ADRs criadas e mantidas para um projeto (ou organização) específico.

Um **requisito arquiteturalmente significativo** (ASR) é um requisito que tem efeito mensurável na arquitetura de um sistema de software.

Todos esses conceitos estão dentro do tema de **gestão do conhecimento de arquitetura** (AKM).

O objetivo deste documento é fornecer uma visão geral rápida de ADRs, como criá-los e onde procurar mais informações.

Abreviações:

  * **AD**: decisão de arquitetura

  * **ADL**: log de decisões de arquitetura

  * **ADR**: registro de decisão de arquitetura

  * **AKM**: gestão do conhecimento de arquitetura

  * **ASR**: requisito arquiteturalmente significativo

## Como começar a usar ADRs

Para começar a usar ADRs, converse com seus colegas de equipe sobre estas áreas.

Identificação da decisão:

  * Quão urgente e importante é a AD?

  * Ela precisa ser tomada agora ou pode esperar até que se saiba mais?

  * Tanto a experiência pessoal quanto a coletiva, bem como métodos e práticas de design reconhecidos, podem ajudar na identificação da decisão.

  * Idealmente, mantenha uma lista de tarefas de decisões que complemente a lista de tarefas do produto.

Tomada de decisão:

  * Existem várias técnicas de tomada de decisão, tanto gerais quanto específicas de arquitetura de software, por exemplo, dialogue mapping.

  * A tomada de decisão em grupo é um tema ativo de pesquisa.

Implementação e aplicação da decisão:

  * ADs são usadas em design de software; portanto, precisam ser comunicadas e aceitas pelas partes interessadas do sistema que o financiam, desenvolvem e operam.

  * Estilos de codificação arquiteturalmente evidentes e revisões de código focadas em preocupações e decisões de arquitetura são duas práticas relacionadas.

  * ADs também precisam ser (re)consideradas ao modernizar um sistema de software no contexto da evolução de software.

Compartilhamento de decisões (opcional):

  * Muitas ADs se repetem entre projetos.

  * Portanto, experiências com decisões passadas, tanto boas quanto ruins, podem ser ativos reutilizáveis valiosos ao empregar uma estratégia explícita de gestão do conhecimento.

Documentação da decisão:

  * Existem muitos modelos e ferramentas para captura de decisões.

  * Consulte comunidades ágeis, por exemplo, ADRs de M. Nygard.

  * Consulte processos tradicionais de engenharia de software e design de arquitetura, por exemplo, layouts de tabela sugeridos pela IBM UMF e por Tyree e Akerman da CapitalOne.

Para saber mais:

  * As etapas acima são adotadas da entrada da Wikipedia sobre [decisão de arquitetura](https://en.wikipedia.org/wiki/Architectural_decision)

## Como começar a usar ADRs com ferramentas

Você pode começar a usar ADRs com ferramentas da maneira que quiser.

Por exemplo:

  * Se você gosta de usar Google Drive e edição online, então pode criar um Google Doc ou uma Google Sheet.

  * Se você gosta de usar controle de versão de código-fonte, como git, então pode criar um arquivo para cada ADR.

  * Se você gosta de usar ferramentas de planejamento de projetos, como Atlassian Jira, então pode usar o rastreador de planejamento da ferramenta.

  * Se você gosta de usar wikis, como MediaWiki, então pode criar uma wiki de ADRs.

## Como começar a usar ADRs com Git

Se você gosta de usar controle de versão com git, então veja como gostamos de começar a usar ADRs com git em um projeto de software típico com código-fonte.

Crie um diretório para arquivos de ADR:

```sh
$ mkdir adr
```

Para cada ADR, crie um arquivo de texto, como `database.txt`:

```sh
$ vi database.txt
```

Escreva o que quiser na ADR. Veja os modelos neste repositório para ter ideias.

Faça commit da ADR no seu repositório git.

## Skills do Claude Code para ADRs

Este repositório oferece duas [skills do Claude Code](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/) para apoiar a criação e a manutenção de ADRs:

- [architecture-decision-record-skill](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — ajuda a decidir quando registrar uma decisão, escolher modelos e documentar contexto, decisão e consequências.
- [architecture-decision-record-maintainer-skill](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — orienta os mantenedores sobre como adicionar modelos, exemplos e conteúdo traduzido.

Para utilizar uma skill, copie sua pasta para `.claude/skills/` no repositório de trabalho, ou para `~/.claude/skills/` para disponibilizá-la globalmente. Em seguida, peça ao Claude Code para escrever ou revisar uma ADR.

## Convenções de nomes de arquivos para ADRs

Se você optar por criar seus ADRs usando arquivos de texto típicos, talvez queira definir sua própria convenção de nomes de arquivos de ADR.

Preferimos usar uma convenção de nomes de arquivos que tenha um formato específico.

Exemplos:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Nossa convenção de nomes de arquivos:

  * O nome tem uma frase verbal imperativa no presente. Isso ajuda na legibilidade e corresponde ao nosso formato de mensagem de commit.

  * O nome usa letras minúsculas e hífens (igual a este repositório). Esse é um equilíbrio entre legibilidade e usabilidade do sistema.

  * A extensão é markdown. Isso pode ser útil para facilitar a formatação.

## Sugestões para escrever bons ADRs

Características de uma boa ADR:

* Justificativa: explique os motivos para tomar uma AD específica. Isso pode incluir o contexto (veja abaixo), prós e contras de várias escolhas potenciais, comparações de funcionalidades, discussões de custo/benefício e mais.

* Específica: cada ADR deve tratar de uma AD, não de várias ADs.

* Timestamps: identifique quando cada item na ADR foi escrito. Isso é especialmente importante para aspectos que podem mudar ao longo do tempo, como custos, cronogramas, escalabilidade e afins.

* Imutável: não altere informações existentes em uma ADR. Em vez disso, complemente a ADR adicionando novas informações ou substitua a ADR criando uma nova ADR.

Características de uma boa seção "Contexto" em uma ADR:

* Explique a situação e as prioridades de negócio da sua organização.

* Inclua justificativa e considerações baseadas na composição social e de habilidades das suas equipes.

* Inclua prós e contras relevantes e descreva-os em termos alinhados às suas necessidades e metas.

Características de uma boa seção "Consequências" em uma ADR:

* Explique o que decorre da tomada da decisão. Isso pode incluir efeitos, resultados, entregas, ações de acompanhamento e mais.

* Inclua informações sobre quaisquer ADRs subsequentes. É relativamente comum que uma ADR acione a necessidade de mais ADRs, como quando uma ADR faz uma grande escolha abrangente, que por sua vez cria necessidades de decisões menores.

* Inclua quaisquer processos de revisão pós-ação. É típico que as equipes revisem cada ADR um mês depois, para comparar as informações da ADR com o que aconteceu na prática real, a fim de aprender e evoluir.

Uma nova ADR pode tomar o lugar de uma ADR anterior:

* Quando uma AD é tomada e substitui ou invalida uma ADR anterior, então uma nova ADR deve ser criada

## Exemplos de modelos de ADR

Os modelos de ADR atendem a diferentes necessidades e níveis de detalhamento:

- [Michael Nygard](modelos/modelo-de-registro-de-decisao-por-michael-nygard/) — simples e bastante utilizado.
- [Jeff Tyree e Art Akerman](modelos/modelo-de-registro-de-decisao-por-jeff-tyree-e-art-akerman/) — mais abrangente.
- [Padrão Alexandrino](modelos/modelo-de-registro-de-decisao-para-padrao-alexandrino/) — valoriza o contexto.
- [Caso de negócio](modelos/modelo-de-registro-de-decisao-para-caso-de-negocio/) — considera custos e alternativas.
- [MADR](modelos/modelo-de-registro-de-decisao-do-projeto-madr/) — evidencia opções e consequências.
- [Planguage](modelos/modelo-de-registro-de-decisao-usando-planguage/) — orientado a qualidade.
- [Decisões Técnicas Importantes](modelos/modelo-de-registro-de-decisao-para-decisoes-tecnicas-importantes/) — documentação concisa para revisão técnica.

## Conselhos de trabalho em equipe para ADRs

Se você está considerando usar registros de decisão com sua equipe, então aqui estão alguns conselhos que aprendemos trabalhando com muitas equipes.

Você tem uma oportunidade de liderar seus colegas de equipe conversando juntos sobre o "porquê", em vez de impor o "o quê". Por exemplo, registros de decisão são uma forma de as equipes pensarem melhor e se comunicarem melhor; registros de decisão não têm valor se forem apenas uma exigência forçada de documentação após o fato.

Algumas equipes preferem muito mais o nome "decisões" à abreviação "ADRs". Quando algumas equipes usam o nome de diretório "decisions", é como se uma lâmpada se acendesse, e a equipe começasse a colocar mais informações no diretório, como decisões sobre fornecedores, decisões de planejamento, decisões de cronograma etc. Todos esses tipos de informação podem usar o mesmo modelo. Nossa hipótese é que as pessoas aprendem mais rápido com palavras ("decisões") do que com abreviações ("ADRs"), e que as pessoas ficam mais motivadas a escrever documentos em andamento quando a palavra "registro" é removida, e também que alguns desenvolvedores e alguns gerentes não gostam da palavra "arquitetura".

Em teoria, a imutabilidade é ideal. Na prática, a mutabilidade funcionou melhor para nossas equipes. Inserimos as novas informações na ADR existente, com um carimbo de data, e uma observação de que as informações chegaram depois da decisão. Esse tipo de abordagem leva a um "documento vivo" que todos nós podemos atualizar. Atualizações típicas acontecem quando obtemos informações graças a novos colegas de equipe, novas ofertas, resultados reais de nossos usos, ou mudanças de terceiros após o fato, como capacidades de fornecedores, planos de preços, contratos de licença etc.

## Perguntas de trabalho em equipe para ADRs

### Quem pode criar uma ADR?

Considere áreas como pessoas específicas, papéis específicos, equipes específicas ou departamentos específicos; considere também se há pessoas, papéis, equipes ou departamentos que podem encomendar uma ADR, ou seja, solicitar uma que outra pessoa irá redigir.

Exemplo de resposta: qualquer pessoa em nossa organização que tenha lido a página README sobre registros de decisão de arquitetura pode propor uma ADR, ou seja, a pessoa pode começar a escrevê-la e compartilhá-la com a equipe.

### O que justifica abrir uma ADR?

Considere áreas como as formas de trabalho em equipe da sua organização, a estrutura do seu sistema de software, coordenação entre equipes, manutenibilidade de longo prazo, interfaces externas, quem você quer beneficiar e afins.

Exemplo de resposta: queremos criar uma ADR quando queremos que desenvolvedores futuros entendam o "porquê" do que estamos fazendo.

### O que justifica não abrir uma ADR?

Considere áreas como decisões que não são sobre arquitetura, ou são pequenas, como de risco mínimo, autocontidas ou de um único desenvolvedor, ou já estão totalmente cobertas em outro lugar, como por padrões, políticas ou documentação, ou são temporárias, como soluções de contorno, provas de conceito ou experimentos.

Exemplo de resposta: queremos dispensar uma ADR quando uma decisão é limitada em escopo, tempo, risco e custo, ou já está coberta em outro lugar.

### Qual é o ciclo de vida de uma ADR?

Considere áreas como o processo de criação, o processo de pesquisa, o processo de decisão, o processo de implementação e o processo de encerramento. Considere como acompanhar o ciclo de vida da ADR ao longo do tempo, como mover a ADR de um status para o próximo, e também como comunicar isso às partes interessadas.

Exemplo de resposta: queremos que uma ADR tenha seis estágios de ciclo de vida: Iniciando -> Pesquisando -> Avaliando -> Implementando -> Mantendo -> Encerrando.

### Quais são os critérios para as etapas do ciclo de vida de uma ADR?

Considere áreas como critérios de aceitação para uma ADR, ou seja, como você sabe que ela é boa o suficiente para avançar de uma etapa do ciclo de vida para a próxima? O problema está claramente articulado? As alternativas foram consideradas? Os trade-offs estão suficientemente bem compreendidos e documentados?
Todo o contexto relevante está disponível? Todas as partes interessadas relevantes estão envolvidas? Todo o feedback foi incorporado?

Exemplo de resposta: queremos que uma ADR seja votada pelas partes interessadas quando a equipe ativa tiver 1) concluído sua pesquisa, 2) concluído sua avaliação, 3) publicado a proposta de ADR para as partes interessadas com uma solicitação de comentários e um timebox de uma semana, 4) todos os comentários das partes interessadas tiverem sido incorporados e tratados.

### Quais papéis e responsabilidades interagem com uma ADR?

Considere papéis como proponente, pesquisador, avaliador, revisor, aprovador, mantenedor e afins. Considere responsabilidades como comunicação com partes interessadas, garantia de que expectativas sejam atendidas, compartilhamento no site ou na intranet, e revisão periódica do trabalho, especialmente quando mudanças relevantes acontecerem.

Exemplo de resposta: queremos que cada ADR sempre tenha uma pessoa de contato principal, uma pessoa de contato secundária e uma equipe responsável; elas são responsáveis por comunicações, publicações, manutenção, revisão periódica pelo menos uma vez por ano, e eventual encerramento conforme necessário.

### Como a governança interage com uma ADR?

Considere áreas como as formas de trabalho da sua organização, quaisquer necessidades especiais de conformidade, como aspectos legais ou de recursos humanos, e como você quer lidar com consenso versus conflito versus escalonamento. Há áreas, pessoas ou equipes que podem ter mais influência que outras em relação a uma ADR, como poder aprová-la, votar nela ou vetá-la?

Exemplo de resposta: a governança de uma ADR está nesta ordem de prioridade: o CEO, o CTO, o CLO, a equipe que implementa uma ADR, os especialistas da equipe que têm mais conhecimento sobre a decisão de arquitetura. Ninguém mais tem governança, a menos que isso esteja descrito na ADR.

### Quais princípios interagem com uma ADR?

Considere áreas como as formas de trabalho da sua organização que incluem mover-se rapidamente versus mover-se lentamente, consenso de decisão versus conflito de decisão, preferências de risco versus preferências de segurança, discussão pública versus discussão privada e afins.

Exemplo de resposta: usamos os princípios de liderança de viés para ação, discordar e se comprometer, estimativas de 70% são boas o suficiente para decisões facilmente reversíveis e facilmente isoláveis, e formas de trabalho públicas, com exceção de informações confidenciais conforme descrito no acordo de confidencialidade da nossa organização.

## Próximos conceitos para explorar

O [arc42](https://arc42.org/) oferece orientação para documentar objetivos, restrições, contexto, qualidade, riscos e decisões arquiteturais.

O [modelo C4](https://c4model.com/) apresenta diagramas hierárquicos de contexto, contêineres, componentes e código, além de diagramas dinâmicos e de implantação. Ambas as abordagens complementam a documentação de ADRs.

## Diagramas, visões e pontos de vista de arquitetura

Um **diagrama de arquitetura** é uma representação de uma visão arquitetural. A **visão** corresponde a um ponto de vista, definido de acordo com o público-alvo e suas preocupações.

Exemplos de diagramas e visões:

- Capacidades de negócio e processos de alto nível.
- [Fluxos de valor](https://en.wikipedia.org/wiki/Value_stream).
- Funcionalidades associadas aos componentes da aplicação.
- [Modelo C4](https://en.wikipedia.org/wiki/C4_model): contexto e contêineres (AS-IS e TO-BE).
- [Diagramas de entidade-relacionamento](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) para entidades e dados.
- [Diagramas de sequência](https://en.wikipedia.org/wiki/Sequence_diagram) para fluxos e integrações.
- [BPMN](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) para processos de negócio.
- Diagramas de identidade, autorização, segurança, infraestrutura e implantação.

Selecione o ponto de vista que melhor explica a decisão às partes interessadas.

## Funções de aptidão para decisões como código

Funções de aptidão são verificações automatizadas objetivas, escritas com código de programação, que verificam se as decisões estão sendo mantidas.

- Funções de aptidão tornam as decisões testáveis e asseguráveis.

- Funções de aptidão para decisões podem ajudar muito a garantia de qualidade, processos regulatórios e objetivos de governança.

### Como funções de aptidão se conectam às decisões

Um registro de decisão documenta a decisão, enquanto uma função de aptidão assegura a decisão.

- Exemplo de decisão: usamos event sourcing para requisitos de auditoria.

- Exemplo de função de aptidão: usamos o servidor de integração contínua para testar que todas as mudanças de estado devem produzir eventos.

### Por que funções de aptidão ajudam decisões

Medições objetivas: funções de aptidão passam ou falham, portanto o trabalho é visível e claro.

Uso contínuo: funções de aptidão são suas regras vivas, executadas em cada commit e build.

Confiança para refatorar: funções de aptidão capturam automaticamente erros em regras de decisão.

Governança escalável: funções de aptidão asseguram padrões sem criar gargalos.

### Funções de aptidão podem usar IA?

Funções de aptidão podem aproveitar LLMs de IA para decisões fazendo perguntas sobre seu trabalho,
como seus planos, código, schemas, APIs e mais:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Testes unitários de arquitetura

[ArchUnit](https://www.archunit.org/): verifica regras de arquitetura de código Java usando qualquer framework simples de testes unitários em Java.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): verifica regras de arquitetura de código TypeScript e código JavaScript usando Jest, Vitest, Jasmine etc.

## Proteções de decisões em pull requests

O [Decision Guardian](https://github.com/DecispherHQ/decision-guardian) apresenta automaticamente as decisões relacionadas aos arquivos alterados durante a revisão de código, trazendo o contexto arquitetural ao pull request.

O [ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) é uma GitHub Action que exige um ADR quando caminhos monitorados são alterados; exceções precisam ser justificadas, por exemplo, utilizando `ADR-Exempt:`. Ambos oferecem mecanismos de governança integrados ao processo de desenvolvimento.

## Para saber mais

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

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - free monthly software architecture lesson

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

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - A vendor-neutral, machine-readable YAML/JSON format for representing decisions with explicit reasoning, assumptions, cognitive state, and trade-offs. Complements ADRs by adding structured, validatable reasoning to decision documentation.

