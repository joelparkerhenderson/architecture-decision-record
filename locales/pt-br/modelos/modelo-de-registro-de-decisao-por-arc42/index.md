# Modelo de registro de decisão por arc42

<https://arc42.org/overview>

## 1. Introdução e objetivos

Breve descrição dos requisitos, forças direcionadoras, extrato (ou resumo) dos
requisitos. Os três principais (no máximo cinco) objetivos de qualidade da
arquitetura que têm maior prioridade para as principais partes interessadas.
Uma tabela de partes interessadas importantes com suas expectativas em relação
à arquitetura.

## 1.1 Visão geral dos requisitos

### Conteúdo

Breve descrição dos requisitos funcionais, forças direcionadoras, extrato (ou
resumo) dos requisitos. Links para os documentos de requisitos (espera-se que
existam), com informações sobre onde encontrá-los.

### Motivação

Do ponto de vista dos usuários finais, um sistema é criado ou modificado para
melhorar o suporte a uma atividade de negócio e/ou melhorar a qualidade.

### Forma

Breve descrição textual, provavelmente em formato tabular de caso de uso. Se
existirem documentos de requisitos, esta visão geral deve referenciá-los.

Mantenha estes extratos tão curtos quanto possível. Equilibre a legibilidade
deste documento com a possível redundância em relação aos documentos de
requisitos.

## 1.2 Objetivos de qualidade

### Conteúdo

Os três principais (no máximo cinco) objetivos de qualidade da arquitetura cujo
cumprimento é de maior importância para as principais partes interessadas.
Queremos dizer realmente objetivos de qualidade para a arquitetura. Não os
confunda com objetivos do projeto. Eles não são necessariamente idênticos. A
norma ISO 25010 fornece uma boa visão geral de possíveis tópicos de interesse.

### Motivação

Você deve conhecer os objetivos de qualidade das suas partes interessadas mais
importantes, pois eles influenciarão decisões fundamentais de arquitetura.
Certifique-se de ser muito concreto sobre estas qualidades e evite buzzwords.
Se você, como arquiteto, não sabe como a qualidade do seu trabalho será julgada
...

### Forma

Uma tabela com os objetivos de qualidade mais importantes e cenários concretos, ordenados por prioridades.

## 1.3 Parte interessada

### Conteúdo

Visão geral explícita das partes interessadas do sistema, isto é, todas as
pessoas, papéis ou organizações que

- devem conhecer a arquitetura

- precisam ser convencidas da arquitetura

- precisam trabalhar com a arquitetura ou com código

- precisam da documentação da arquitetura para seu trabalho

- precisam chegar a decisões sobre o sistema ou seu desenvolvimento

### Motivação

Você deve conhecer todas as partes envolvidas no desenvolvimento do sistema ou
afetadas pelo sistema. Caso contrário, poderá ter surpresas desagradáveis mais
tarde no processo de desenvolvimento. Estas partes interessadas determinam a
extensão e o nível de detalhe do seu trabalho e de seus resultados.

### Forma

Tabela com nomes de papéis, nomes de pessoas e suas expectativas em relação à
arquitetura e sua documentação.

## 2. Restrições

Qualquer coisa que restrinja as equipes em decisões de design e implementação
ou em decisões sobre processos relacionados. Às vezes pode ir além de sistemas
individuais e ser válida para organizações e empresas inteiras.

### Conteúdo

Qualquer requisito que restrinja arquitetos de software em sua liberdade de
decisões de design e implementação ou decisões sobre o processo de
desenvolvimento. Estas restrições às vezes vão além de sistemas individuais e
são válidas para organizações e empresas inteiras.

### Motivação

Arquitetos devem saber exatamente onde são livres em suas decisões de design e
onde precisam aderir a restrições. Restrições devem sempre ser tratadas; porém,
elas podem ser negociáveis.

### Forma

Tabelas simples de restrições com explicações. Se necessário, você pode
subdividi-las em restrições técnicas, restrições organizacionais e políticas e
convenções (por exemplo, diretrizes de programação ou versionamento,
convenções de documentação ou nomenclatura)

## 3. Contexto e escopo

Delimita seu sistema em relação a seus parceiros de comunicação (externos)
(sistemas vizinhos e usuários). Especifica as interfaces externas. Mostrado a
partir de uma perspectiva de negócio/domínio (sempre) ou de uma perspectiva
técnica (opcional)

### Conteúdo

Escopo e contexto do sistema - como o nome sugere - delimitam seu sistema (isto
é, seu escopo) em relação a todos os seus parceiros de comunicação (sistemas
vizinhos e usuários, isto é, o contexto do seu sistema). Assim, especificam as
interfaces externas.

Se necessário, diferencie o contexto de negócio (entradas e saídas específicas
do domínio) do contexto técnico (canais, protocolos, hardware).

### Motivação

As interfaces de domínio e interfaces técnicas para parceiros de comunicação
estão entre os aspectos mais críticos do seu sistema. Certifique-se de
compreendê-las completamente.

### Forma

- Vários diagramas de contexto

- Listas de parceiros de comunicação e suas interfaces.

## 3.1 Contexto de negócio

### Conteúdo

Especificação de todos os parceiros de comunicação (usuários, sistemas de TI,
...) com explicações de entradas e saídas ou interfaces específicas do domínio.
Opcionalmente, você pode adicionar formatos específicos do domínio ou
protocolos de comunicação.

### Motivação

Todas as partes interessadas devem entender quais dados são trocados com o
ambiente do sistema.

### Forma

Todos os tipos de diagramas que mostram o sistema como uma caixa preta e
especificam as interfaces de domínio para parceiros de comunicação.

Alternativamente (ou adicionalmente), você pode usar uma tabela. O título da
tabela é o nome do seu sistema; as três colunas contêm o nome do parceiro de
comunicação, as entradas e as saídas.

## 3.2 Contexto técnico

### Conteúdo

Interfaces técnicas (canais e meios de transmissão) que conectam seu sistema ao
seu ambiente. Além disso, um mapeamento de entrada/saída específica do domínio
para os canais, isto é, uma explicação de qual I/O usa qual canal.

### Motivação

Muitas partes interessadas tomam decisões de arquitetura com base nas
interfaces técnicas entre o sistema e seu contexto. Especialmente designers de
infraestrutura ou hardware decidem estas interfaces técnicas.

### Forma

Por exemplo, diagrama de implantação UML descrevendo canais para sistemas
vizinhos, junto com uma tabela de mapeamento que mostra os relacionamentos
entre canais e entrada/saída.

## 4. Estratégia de solução

Resumo das decisões fundamentais e estratégias de solução que moldam a
arquitetura. Pode incluir tecnologia, decomposição de alto nível, abordagens
para alcançar os principais objetivos de qualidade e decisões organizacionais
relevantes.

### Conteúdo

Um breve resumo e explicação das decisões fundamentais e estratégias de solução que moldam a arquitetura do sistema. Elas incluem

- decisões de tecnologia

- decisões sobre a decomposição de alto nível do sistema, por exemplo, uso de um padrão de arquitetura ou padrão de design

- decisões sobre como alcançar objetivos de qualidade principais

- decisões organizacionais relevantes, por exemplo, selecionar um processo de desenvolvimento ou delegar certas tarefas a terceiros.

### Motivação

Estas decisões formam os pilares da sua arquitetura. Elas são a base para
muitas outras decisões detalhadas ou regras de implementação.

### Forma

Mantenha curta a explicação destas decisões-chave.

Motive o que você decidiu e por que decidiu dessa forma, com base na sua
declaração do problema, nos objetivos de qualidade e nas principais restrições.
Consulte detalhes nas seções seguintes (seção 5 para detalhes estruturais,
seção 8 para conceitos transversais).

Você pode usar uma lista de abordagens de solução ou uma tabela.

## 5. Visão de blocos de construção

Decomposição estática do sistema, abstrações de código-fonte, mostradas como
hierarquia de caixas brancas (contendo caixas pretas), até o nível de detalhe
apropriado.

### Conteúdo

A visão de blocos de construção mostra a decomposição estática do sistema em
blocos de construção (módulos, componentes, subsistemas, classes, interfaces,
pacotes, bibliotecas, frameworks, camadas, partições, tiers, funções, macros,
operações, estruturas de dados, ...) bem como suas dependências
(relacionamentos, associações, ...)

Esta visão é obrigatória para toda documentação de arquitetura. Em analogia a
uma casa, este é o plano de planta.

### Motivação

Mantenha uma visão geral do seu código-fonte tornando sua estrutura
compreensível por meio de abstração.

Isso permite que você se comunique com suas partes interessadas em um nível
abstrato sem revelar detalhes de implementação.

### Forma

A visão de blocos de construção é uma coleção hierárquica de caixas pretas e
caixas brancas (veja a figura abaixo) e suas descrições.

## 5.1 Caixa branca do sistema geral

Aqui você descreve a decomposição do sistema geral usando o seguinte modelo de caixa branca. Ele contém

- um diagrama de visão geral

- uma motivação para a decomposição

- descrições de caixa preta dos blocos de construção contidos. Para elas, oferecemos alternativas:

  - use uma tabela para uma visão geral curta e pragmática de todos os blocos de construção contidos e suas interfaces

  - use uma lista de descrições de caixa preta dos blocos de construção de acordo com o modelo de caixa preta (veja abaixo). Dependendo da sua escolha de ferramenta, esta lista poderia ser subcapítulos (em arquivos de texto), subpáginas (em uma Wiki) ou elementos aninhados (em uma ferramenta de modelagem).

  - (opcional:) interfaces importantes que não são explicadas nos modelos de caixa preta de um bloco de construção, mas são muito importantes para entender a caixa branca.

Como há tantas formas de especificar interfaces, por que não fornecer um modelo específico para elas.

No melhor caso, você conseguirá se virar com exemplos ou assinaturas simples.

## 5.2 Nível 2

Aqui você pode especificar a estrutura interna de (alguns) blocos de construção
do nível 1 como caixas brancas.

Você precisa decidir quais blocos de construção do seu sistema são importantes
o suficiente para justificar uma descrição tão detalhada. Prefira relevância em
vez de completude. Especifique blocos de construção importantes,
surpreendentes, arriscados, complexos ou voláteis. Deixe de fora partes
normais, simples, entediantes ou padronizadas do seu sistema

### 5.2.1 Caixa branca para o bloco de construção 1

Especifica a estrutura interna do bloco de construção 1.

Use o modelo de caixa branca (veja acima).

## 6. Visão de tempo de execução

Comportamento de blocos de construção como cenários, cobrindo casos de uso ou
funcionalidades importantes, interações em interfaces externas críticas,
operação e administração, além de comportamento de erros e exceções.

### Conteúdo

A visão de tempo de execução descreve comportamento e interações concretos dos blocos de construção do sistema na forma de cenários das seguintes áreas:

- casos de uso ou funcionalidades importantes: como os blocos de construção os executam?

- interações em interfaces externas críticas: como os blocos de construção cooperam com usuários e sistemas vizinhos?

- operação e administração: lançamento, inicialização, parada

- cenários de erro e exceção

Observação: O principal critério para escolher cenários possíveis (sequências, workflows) é sua relevância arquitetural. Não é importante descrever um grande número de cenários. Em vez disso, você deve documentar uma seleção representativa.

### Motivação

Você deve entender como (instâncias de) blocos de construção do seu sistema realizam seu trabalho e se comunicam em tempo de execução. Você capturará cenários principalmente na sua documentação para comunicar sua arquitetura a partes interessadas que estão menos dispostas ou aptas a ler e entender os modelos estáticos (visão de blocos de construção, visão de implantação).

### Forma

Há muitas notações para descrever cenários, por exemplo:


- lista numerada de passos (em linguagem natural)

- diagramas de atividade ou fluxogramas

- diagramas de sequência

- BPMN ou EPCs (event process chains)

- máquinas de estado

- etc.

## 6.n Cenário de tempo de execução n (1, 2, 3 etc.)

Insira o diagrama de tempo de execução ou a descrição textual do cenário.

Insira a descrição dos aspectos notáveis das interações entre as instâncias de blocos de construção representadas neste diagrama.

## 7. Visão de implantação

Infraestrutura técnica com ambientes, computadores, processadores, topologias.
Mapeamento de blocos de construção (de software) para elementos de
infraestrutura.

### Conteúdo

A visão de implantação descreve:

- a infraestrutura técnica usada para executar seu sistema, com elementos de
  infraestrutura como localizações geográficas, ambientes, computadores,
  processadores, canais e topologias de rede, bem como outros elementos de
  infraestrutura e

- o mapeamento de blocos de construção (de software) para esses elementos de infraestrutura.

Frequentemente, sistemas são executados em diferentes ambientes, por exemplo,
ambiente de desenvolvimento, ambiente de teste, ambiente de produção. Nesses
casos, você deve documentar todos os ambientes relevantes.

Documente especialmente a visão de implantação quando seu software for
executado como sistema distribuído com mais de um computador, processador,
servidor ou container, ou quando você projetar e construir seus próprios
processadores e chips de hardware.

Da perspectiva de software, é suficiente capturar os elementos da infraestrutura
necessários para mostrar a implantação dos seus blocos de construção. Arquitetos
de hardware podem ir além disso e descrever a infraestrutura em qualquer nível
de detalhe de que precisem para capturá-la.

### Motivação

Software não roda sem hardware. Esta infraestrutura subjacente pode influenciar
e influenciará seu sistema e/ou alguns conceitos transversais. Portanto, você
precisa conhecer a infraestrutura.

### Forma

Talvez o diagrama de implantação de nível mais alto já esteja contido na seção 3.2. como contexto técnico, com sua própria infraestrutura como UMA caixa preta. Nesta seção, você dará zoom nesta caixa preta usando diagramas de implantação adicionais.

- UML oferece diagramas de implantação para expressar essa visão. Use-os, provavelmente com diagramas aninhados, quando sua infraestrutura for mais complexa.

- Quando suas partes interessadas (de hardware) preferirem outros tipos de diagramas em vez de
  diagrama de implantação UML, deixe-as usar qualquer tipo capaz de mostrar nós e
  canais da infraestrutura.

## 7.1 Infraestrutura nível 1

Descreva (normalmente em uma combinação de diagramas, tabelas e texto):

- a distribuição do seu sistema para múltiplas localizações, ambientes, computadores, processadores, .. bem como as conexões físicas entre eles

- justificativa ou motivação importante para esta estrutura de implantação

- características de qualidade e/ou desempenho da infraestrutura

- o mapeamento de artefatos de software (blocos de construção) para elementos da infraestrutura

Para múltiplos ambientes ou implantações alternativas, copie esta seção do arc42 para todos os ambientes relevantes. **

## 7.2 Infraestrutura nível 2

Aqui você pode incluir a estrutura interna de (alguns) elementos de infraestrutura do nível de infraestrutura 1.

Copie a estrutura do nível 1 para cada elemento selecionado.

## 8. Conceitos transversais

Regulamentos principais, gerais, e abordagens de solução relevantes em múltiplas
partes (→ transversais) do sistema. Conceitos frequentemente se relacionam a
múltiplos blocos de construção. Inclua diferentes tópicos como modelos de
domínio, padrões e estilos de arquitetura, regras para uso de tecnologia
específica e regras de implementação.

### Conteúdo

Esta seção descreve conceitos transversais (práticas, padrões, regulamentos ou
ideias de solução). Tais conceitos frequentemente se relacionam a múltiplos
blocos de construção. Eles podem incluir muitos tópicos diferentes.

### Motivação

Conceitos formam a base para a integridade conceitual (consistência,
homogeneidade) da arquitetura. Portanto, eles são uma contribuição importante
para alcançar qualidades internas do seu sistema.

Este é o lugar no modelo que fornecemos para uma especificação coesa desses
conceitos.

Muitos destes conceitos se relacionam a vários dos seus blocos de construção ou
os influenciam.

### Forma

A forma pode variar:

- documentos conceituais com qualquer tipo de estrutura

- implementações de exemplo, especialmente para conceitos técnicos

- excertos de modelos transversais ou cenários usando notações das visões de arquitetura

### Estrutura desta seção

Escolha apenas os tópicos mais necessários para seu sistema e atribua a cada um um heading de nível 2 nesta seção (por exemplo, 8.1, 8.2 etc).

- NÃO TENTE cobrir todos os tópicos do diagrama mencionado acima.

### Contexto adicional

Alguns tópicos dentro de sistemas frequentemente dizem respeito a múltiplos
blocos de construção, elementos de hardware ou processos de desenvolvimento.
Pode ser mais fácil comunicar ou documentar esses tópicos transversais em um
local central, em vez de repeti-los na descrição dos blocos de construção,
elementos de hardware ou processos de desenvolvimento envolvidos.

Certos conceitos podem dizer respeito a todos os elementos de um sistema,
outros podem ser relevantes apenas para alguns.

## 9. Decisões de arquitetura

Decisões de arquitetura importantes, caras, críticas, de grande escala ou
arriscadas, incluindo justificativas.

### Conteúdo

Decisões de arquitetura importantes, caras, de grande escala ou arriscadas,
incluindo justificativas. Com "decisões", queremos dizer selecionar uma
alternativa com base em determinados critérios.

Use seu julgamento para decidir se uma decisão de arquitetura deve ser
documentada aqui nesta seção central ou se é melhor documentá-la localmente
(por exemplo, dentro do modelo de caixa branca de um bloco de construção).
Evite textos redundantes. Consulte a seção 4, onde você já capturou as decisões
mais importantes da sua arquitetura.

### Motivação

As partes interessadas do seu sistema devem ser capazes de compreender e
rastrear suas decisões.

### Forma

- ADR (architecture decision record) para cada decisão importante

- lista ou tabela, ordenada por importância e consequências ou

- mais detalhado na forma de seções separadas por decisão

### Contexto adicional (sobre ADRs)

Pequenas partes de documentação são mais fáceis de ler, criar e manter. Quando
se trata de decisões de arquitetura, equipes de desenvolvimento frequentemente:

- sabem da decisão, pois ela está visível, por exemplo, no código-fonte, mas

- perdem a motivação por trás dessa decisão (veja Nygard 2011)

Portanto, você deve documentar algumas decisões importantes junto com sua
motivação e raciocínio

### Nossa proposta sobre decisões

Mantenha uma coleção de decisões arquiteturalmente significativas, aquelas
decisões que afetam a estrutura, características de qualidade, dependências e
interfaces importantes (especialmente externas), ou técnicas de construção
(agradecimentos a Michael Nygard por esta proposta).

## 10. Requisitos de qualidade

Requisitos de qualidade como cenários, com árvore de qualidade para fornecer
uma visão geral de alto nível. Os objetivos de qualidade mais importantes
devem ter sido descritos na seção 1.2. (objetivos de qualidade).

### Conteúdo

Esta seção contém todos os requisitos de qualidade relevantes.

Os mais importantes destes requisitos já foram descritos na seção 1.2.
(objetivos de qualidade), portanto eles devem ser apenas referenciados aqui.
Nesta seção 10, você também deve capturar requisitos de qualidade de menor
importância, que não criarão riscos altos se não forem plenamente alcançados
(mas podem ser desejáveis).

### Motivação

Como requisitos de qualidade terão muita influência sobre decisões de
arquitetura, você deve saber quais qualidades são realmente importantes para
suas partes interessadas, de uma forma específica e mensurável.

### Informações adicionais

Veja o extenso modelo de qualidade Q42 em https://quality.arc42.org.

## 10.1 Visão geral dos requisitos de qualidade

### Conteúdo

Uma visão geral ou resumo dos requisitos de qualidade.

### Motivação

Frequentemente encontramos dezenas (ou até centenas) de requisitos de qualidade
detalhados. Nesta seção de visão geral, você deve tentar resumir, por exemplo,
descrevendo categorias ou tópicos (como sugerido pela ISO 25010:2023 ou Q42

Se estas descrições resumidas já forem precisas, específicas o suficiente e
mensuráveis, você pode pular a seção 10.2.

### Forma

Use uma tabela simples em que cada linha contém uma categoria ou tópico e uma
breve descrição do requisito de qualidade. Alternativamente, você pode usar um
mapa mental para estruturar estes requisitos de qualidade.

Na literatura, a ideia de uma árvore de atributos de qualidade também foi
descrita, colocando o termo genérico "qualidade" como raiz e usando um
refinamento em forma de árvore do termo "qualidade". [Bass+21] introduziu o
termo "Quality Attribute Utility Tree" para esse propósito.

## 10.2 Cenários de qualidade

### Conteúdo

Cenários de qualidade tornam requisitos de qualidade concretos e permitem
decidir se eles são cumpridos (no sentido de critérios de aceite). Certifique-se
de que seus cenários sejam específicos e mensuráveis.

Dois tipos de cenários são especialmente úteis:

- Cenários de uso (também chamados de cenários de aplicação ou cenários de caso de uso)
  descrevem a reação do sistema em tempo de execução a um determinado estímulo. Isso também
  inclui cenários que descrevem a eficiência ou desempenho do sistema.
  Exemplo: O sistema reage à solicitação de um usuário em até um segundo.

- Cenários de mudança descrevem o efeito desejado de uma modificação ou extensão do
  sistema ou de seu ambiente imediato. Exemplo: Funcionalidade adicional
  é implementada ou requisitos de um atributo de qualidade mudam, e o esforço
  ou duração da mudança é medido.

### Forma

Informações típicas para cenários detalhados incluem o seguinte:

Na forma curta (favorecida no modelo Q42):

- Contexto/Histórico: Que tipo de sistema ou componente, qual é o ambiente ou situação?

- Fonte/Estímulo: Quem ou o que inicia ou dispara um comportamento, reação ou ação.

- Métrica/Critérios de aceite: Uma resposta incluindo uma medida ou métrica

A forma longa de cenários (favorecida pelo SEI e [Bass+21]) é mais detalhada e inclui as seguintes informações:

- ID do cenário: Um identificador único para o cenário.

- Nome do cenário: Um nome curto e descritivo para o cenário.

- Fonte: A entidade (usuário, sistema ou evento) que inicia o cenário.

- Estímulo: O evento ou condição disparadora que o sistema deve tratar.

- Ambiente: O contexto ou condição operacional sob o qual o sistema experimenta o estímulo.

- Artefato: Os blocos de construção ou outros elementos do sistema afetados pelo estímulo.

- Resposta: O resultado ou comportamento que o sistema exibe em reação ao estímulo.

- Medida de resposta: Os critérios ou métrica pelos quais a resposta do sistema é avaliada.

### Veja também

Desde janeiro de 2023, arc42 fornece um modelo pragmático de qualidade que
propõe rotular requisitos de qualidade com hashtags ou labels como #flexible,
#efficient, #usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Riscos e dívida técnica

Riscos técnicos conhecidos ou dívida técnica. Que problemas potenciais existem
dentro ou ao redor do sistema? O que faz a equipe de desenvolvimento se sentir
desconfortável?

### Conteúdo

Uma lista de riscos técnicos ou dívidas técnicas identificados, ordenada por prioridade

### Motivação

"Risk management is project management for grown-ups" (Tim Lister, Atlantic
Systems Guild.)

Este deve ser seu lema para detecção e avaliação sistemáticas de riscos e
dívidas técnicas na arquitetura, que serão necessárias para partes interessadas
de gestão (por exemplo, gerentes de projeto, product owners) como parte da
análise geral de riscos e do planejamento de medição.

### Forma

Lista de riscos e/ou dívidas técnicas, provavelmente incluindo medidas sugeridas
para minimizar, mitigar ou evitar riscos ou reduzir dívidas técnicas.
