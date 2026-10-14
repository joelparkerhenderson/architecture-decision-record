# Processo de Registros de Decisão de Arquitetura da AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Um registro de decisão de arquitetura (ADR) é um documento que descreve uma escolha que a equipe faz sobre um aspecto significativo da arquitetura de software que está planejando construir. Cada ADR descreve a decisão de arquitetura, seu contexto e suas consequências. ADRs têm estados e, portanto, seguem um ciclo de vida. Para ver um exemplo de ADR, consulte o apêndice.

O processo de ADR gera uma coleção de registros de decisão de arquitetura. Essa coleção cria o log de decisões. O log de decisões fornece o contexto do projeto, bem como informações detalhadas de implementação e design. Membros do projeto passam os olhos pelos títulos de cada ADR para obter uma visão geral do contexto do projeto. Eles leem os ADRs para se aprofundar nas implementações do projeto e nas escolhas de design.

Quando a equipe aceita um ADR, ele se torna imutável. Se novos aprendizados exigirem uma decisão diferente, a equipe propõe um novo ADR. Quando a equipe aceita o novo ADR, ele substitui o ADR anterior.

## Escopo do processo de ADR

Membros do projeto devem criar um ADR para toda decisão arquiteturalmente significativa que afete o projeto ou produto de software, incluindo o seguinte (Richards e Ford 2020):

* Estrutura (por exemplo, padrões como microsserviços)

* Requisitos não funcionais (segurança, alta disponibilidade e tolerância a falhas)

* Dependências (acoplamento de componentes)

* Interfaces (APIs e contratos publicados)

* Técnicas de construção (bibliotecas, frameworks, ferramentas e processos)

* Requisitos funcionais e não funcionais são as entradas mais comuns para o processo de ADR.


## Conteúdo do ADR

Quando a equipe identifica a necessidade de um ADR, uma pessoa da equipe começa a escrever o ADR com base em um modelo comum ao projeto. (Consulte a organização ADR no GitHub para ver exemplos de modelos.) O modelo simplifica a criação de ADRs e garante que o ADR capture todas as informações relevantes. No mínimo, cada ADR deve definir o contexto da decisão, a decisão em si e as consequências da decisão para o projeto e seus entregáveis. (Para ver exemplos dessas seções, consulte o apêndice.) Um dos aspectos mais poderosos da estrutura de ADR é que ela se concentra no motivo da decisão, e não em como a equipe a implementou. Entender por que a equipe tomou a decisão facilita que outros membros da equipe adotem a decisão e impede que outros arquitetos que não participaram do processo de tomada de decisão a invalidem no futuro.


## Processo de adoção de ADR

Qualquer membro da equipe pode criar um ADR, mas a equipe deve estabelecer uma definição de responsabilidade por um ADR. Cada autor responsável por um ADR deve manter e comunicar ativamente o conteúdo do ADR. Para esclarecer essa responsabilidade, este guia se refere aos autores de ADRs como responsáveis pelos ADRs nas seções a seguir. Outros membros da equipe sempre podem contribuir para um ADR. Se o conteúdo de um ADR mudar antes de a equipe aceitá-lo, a pessoa responsável deve aprovar essas mudanças.

Depois que a equipe identifica uma decisão de arquitetura e sua pessoa responsável, essa pessoa disponibiliza o ADR no estado **Proposto** no início do processo. ADRs no estado Proposto estão prontos para revisão.

A pessoa responsável pelo ADR então inicia o processo de revisão do ADR. O objetivo do processo de revisão do ADR é decidir se a equipe aceita o ADR, determina que ele precisa de retrabalho ou o rejeita. A equipe do projeto, incluindo a pessoa responsável, revisa o ADR. A reunião de revisão deve começar com um intervalo de tempo dedicado para leitura do ADR. Em média, 10 a 15 minutos devem ser suficientes. Durante esse tempo, cada membro da equipe lê o documento e adiciona comentários e perguntas para sinalizar tópicos pouco claros. Depois da fase de revisão, a pessoa responsável pelo ADR lê em voz alta e discute cada comentário com a equipe.

Se a equipe encontrar pontos de ação para melhorar o ADR, o estado do ADR permanece **Proposto**. A pessoa responsável pelo ADR formula as ações e, em colaboração com a equipe, atribui uma pessoa a cada ação. Cada membro da equipe pode contribuir e resolver os pontos de ação. É responsabilidade da pessoa responsável pelo ADR reagendar o processo de revisão.

A equipe também pode decidir rejeitar o ADR. Nesse caso, a pessoa responsável pelo ADR adiciona um motivo para a rejeição a fim de evitar discussões futuras sobre o mesmo tópico. A pessoa responsável altera o estado do ADR para **Rejeitado**.

Se a equipe aprovar o ADR, a pessoa responsável adiciona um timestamp, uma versão e uma lista de partes interessadas. Em seguida, atualiza o estado para **Aceito**.

Os ADRs e o log de decisões que eles criam representam decisões tomadas pela equipe e fornecem um histórico de todas as decisões. A equipe usa os ADRs como referência durante revisões de código e de arquitetura sempre que possível. Além de realizar revisões de código, tarefas de design e tarefas de implementação, membros da equipe devem consultar ADRs para decisões estratégicas do produto.

Como boa prática, cada mudança de software deve passar por revisões por pares e exigir pelo menos uma aprovação. Durante a revisão de código, uma pessoa revisora pode encontrar mudanças que violam um ou mais ADRs. Nesse caso, a pessoa revisora pede à pessoa autora da mudança de código que atualize o código e compartilha um link para o ADR. Quando a pessoa autora atualiza o código, ele é aprovado por revisores por pares e incorporado à base principal de código.


## Processo de revisão de ADR

A equipe deve tratar ADRs como documentos imutáveis depois que a equipe os aceita ou rejeita. Mudanças em um ADR existente exigem a criação de um novo ADR, o estabelecimento de um processo de revisão para o novo ADR e a aprovação do ADR. Se a equipe aprovar o novo ADR, a pessoa responsável deve alterar o estado do ADR antigo para **Substituído**.
