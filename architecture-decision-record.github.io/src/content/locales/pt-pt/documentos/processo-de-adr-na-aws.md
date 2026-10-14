# Processo de registros de decisão de arquitetura na AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Um registro de decisão de arquitetura (ADR) é um documento que descreve uma escolha feita pela equipe sobre um aspecto significativo da arquitetura de software que ela está planejando construir. Cada ADR descreve a decisão de arquitetura, seu contexto e suas consequências. Os ADRs têm estados e, portanto, seguem um ciclo de vida. Para ver um exemplo de ADR, consulte o apêndice.

O processo de ADR produz uma coleção de registros de decisão de arquitetura. Essa coleção cria o registro de decisões. O registro de decisões fornece o contexto do projeto, bem como informações detalhadas de implementação e design. Os membros do projeto percorrem os títulos de cada ADR para ter uma visão geral do contexto do projeto. Eles leem os ADRs para se aprofundar nas implementações e nas escolhas de design do projeto.

Quando a equipe aceita um ADR, ele se torna imutável. Se novos conhecimentos exigirem uma decisão diferente, a equipe propõe um novo ADR. Quando a equipe aceita o novo ADR, ele substitui o ADR anterior.

## Escopo do processo de ADR

Os membros do projeto devem criar um ADR para toda decisão arquiteturalmente significativa que afete o projeto ou produto de software, incluindo as seguintes (Richards and Ford 2020):

* Estrutura (por exemplo, padrões como microsserviços)

* Requisitos não funcionais (segurança, alta disponibilidade e tolerância a falhas)

* Dependências (acoplamento de componentes)

* Interfaces (APIs e contratos publicados)

* Técnicas de construção (bibliotecas, frameworks, ferramentas e processos)

* Requisitos funcionais e não funcionais são as entradas mais comuns do processo de ADR.


## Conteúdo do ADR

Quando a equipe identifica a necessidade de um ADR, um membro da equipe começa a escrevê-lo com base em um modelo válido para todo o projeto. (Consulte a organização ADR no GitHub para ver exemplos de modelos.) O modelo simplifica a criação do ADR e garante que ele capture todas as informações relevantes. No mínimo, cada ADR deve definir o contexto da decisão, a própria decisão e as consequências da decisão para o projeto e seus produtos entregáveis. (Para ver exemplos dessas seções, consulte o apêndice.) Um dos aspectos mais poderosos da estrutura do ADR é que ela se concentra na razão da decisão, e não em como a equipe a implementou. Entender por que a equipe tomou a decisão facilita a adoção por outros membros da equipe e impede que outros arquitetos que não participaram do processo de tomada de decisão revoguem essa decisão no futuro.


## Processo de adoção do ADR

Todo membro da equipe pode criar um ADR, mas a equipe deve estabelecer uma definição de propriedade para um ADR. Cada autor que é o proprietário de um ADR deve manter e comunicar ativamente o conteúdo do ADR. Para esclarecer essa propriedade, este guia se refere aos autores de ADR como proprietários de ADR nas seções a seguir. Outros membros da equipe sempre podem contribuir para um ADR. Se o conteúdo de um ADR mudar antes de a equipe aceitá-lo, o proprietário deve aprovar essas mudanças.

Depois que a equipe identifica uma decisão de arquitetura e seu proprietário, o proprietário do ADR fornece o ADR no estado **Proposed** (proposto) no início do processo. Os ADRs no estado Proposed estão prontos para revisão.

Em seguida, o proprietário do ADR inicia o processo de revisão do ADR. O objetivo do processo de revisão do ADR é decidir se a equipe aceita o ADR, determina que ele precisa de retrabalho ou o rejeita. A equipe do projeto, incluindo o proprietário, revisa o ADR. A reunião de revisão deve começar com um intervalo de tempo dedicado à leitura do ADR. Em média, de 10 a 15 minutos devem ser suficientes. Durante esse tempo, cada membro da equipe lê o documento e adiciona comentários e perguntas para sinalizar tópicos pouco claros. Após a fase de revisão, o proprietário do ADR lê e discute cada comentário com a equipe.

Se a equipe encontrar itens de ação para melhorar o ADR, o estado do ADR permanece **Proposed**. O proprietário do ADR formula as ações e, em colaboração com a equipe, atribui um responsável a cada ação. Cada membro da equipe pode contribuir e resolver os itens de ação. É responsabilidade do proprietário do ADR reagendar o processo de revisão.

A equipe também pode decidir rejeitar o ADR. Nesse caso, o proprietário do ADR adiciona um motivo para a rejeição, a fim de evitar discussões futuras sobre o mesmo tópico. O proprietário altera o estado do ADR para **Rejected** (rejeitado).

Se a equipe aprovar o ADR, o proprietário adiciona um carimbo de data e hora, uma versão e uma lista de partes interessadas. Em seguida, o proprietário atualiza o estado para **Accepted** (aceito).

Os ADRs e o registro de decisões que eles criam representam decisões tomadas pela equipe e fornecem um histórico de todas as decisões. Sempre que possível, a equipe usa os ADRs como referência durante as revisões de código e de arquitetura. Além de realizar revisões de código, tarefas de design e tarefas de implementação, os membros da equipe devem consultar os ADRs para conhecer as decisões estratégicas do produto.

Como boa prática, cada mudança de software deve passar por revisão por pares e exigir pelo menos uma aprovação. Durante a revisão de código, um revisor pode encontrar mudanças que violem um ou mais ADRs. Nesse caso, o revisor pede ao autor da mudança de código que atualize o código e compartilha um link para o ADR. Quando o autor atualiza o código, ele é aprovado pelos revisores e integrado à base de código principal.


## Processo de revisão do ADR

A equipe deve tratar os ADRs como documentos imutáveis depois de aceitá-los ou rejeitá-los. Alterar um ADR existente exige criar um novo ADR, estabelecer um processo de revisão para o novo ADR e aprová-lo. Se a equipe aprovar o novo ADR, o proprietário deve alterar o estado do ADR antigo para **Superseded** (substituído). 
