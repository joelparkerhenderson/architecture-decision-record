# Modelo de registro de decisão do arc42

<https://arc42.org/overview>

## 1. Introdução e objetivos

Breve descrição dos requisitos, das forças motrizes, extrato (ou resumo) dos requisitos. Os três (no máximo cinco) principais objetivos de qualidade para a arquitetura que têm a mais alta prioridade para as principais partes interessadas. Uma tabela das partes interessadas importantes com suas expectativas em relação à arquitetura.

## 1.1 Visão geral dos requisitos

### Conteúdo

Breve descrição dos requisitos funcionais, das forças motrizes, extrato (ou
resumo) dos requisitos. Links para os documentos de requisitos (esperamos que existentes),
com informações sobre onde encontrá-los. 

### Motivação

Do ponto de vista dos usuários finais, um sistema é criado ou modificado para
melhorar o suporte a uma atividade de negócio e/ou melhorar a qualidade. 

### Forma

Breve descrição textual, provavelmente em formato tabular de casos de uso. Se
existirem documentos de requisitos, esta visão geral deve referir-se a eles.

Mantenha esses extratos o mais curtos possível. Equilibre a legibilidade deste documento
com a potencial redundância em relação aos documentos de requisitos. 

## 1.2 Objetivos de qualidade

### Conteúdo

Os três (no máximo cinco) principais objetivos de qualidade para a arquitetura cujo cumprimento é
da mais alta importância para as principais partes interessadas. Queremos dizer realmente objetivos de qualidade
para a arquitetura. Não os confunda com objetivos do projeto. Eles não são
necessariamente idênticos. A norma ISO 25010 fornece uma boa visão geral de
possíveis tópicos de interesse.

### Motivação

Você deve conhecer os objetivos de qualidade das suas partes interessadas mais importantes, pois
eles influenciarão decisões arquiteturais fundamentais. Seja bem
concreto sobre essas qualidades, evite jargões. Se você, como arquiteto, não
sabe como a qualidade do seu trabalho será julgada …

### Forma

Uma tabela com os objetivos de qualidade mais importantes e cenários concretos, ordenados por prioridade.

## 1.3 Partes interessadas

### Conteúdo

Visão geral explícita das partes interessadas do sistema, ou seja, todas as pessoas, papéis ou
organizações que

- devem conhecer a arquitetura

- precisam ser convencidas da arquitetura

- precisam trabalhar com a arquitetura ou com o código

- precisam da documentação da arquitetura para o seu trabalho

- precisam tomar decisões sobre o sistema ou seu desenvolvimento

### Motivação

Você deve conhecer todas as partes envolvidas no desenvolvimento do sistema ou afetadas
pelo sistema. Caso contrário, poderá ter surpresas desagradáveis mais tarde no processo
de desenvolvimento. Essas partes interessadas determinam a extensão e o nível de detalhe do seu
trabalho e de seus resultados.

### Forma

Tabela com nomes de papéis, nomes de pessoas e suas expectativas em relação à
arquitetura e à sua documentação.

## 2. Restrições

Tudo o que restringe as equipes em decisões de design e implementação ou
decisões sobre processos relacionados. Às vezes podem ir além de sistemas individuais e
valer para organizações e empresas inteiras.

### Conteúdo

Qualquer requisito que restrinja os arquitetos de software em sua liberdade de decisões de design
e implementação ou decisão sobre o processo de desenvolvimento. Essas
restrições às vezes vão além de sistemas individuais e valem para
organizações e empresas inteiras.

### Motivação

Os arquitetos devem saber exatamente onde são livres em suas decisões de design e
onde devem aderir a restrições. As restrições sempre precisam ser tratadas;
elas podem, porém, ser negociáveis.

### Forma

Tabelas simples de restrições com explicações. Se necessário, você pode subdividi-las
em restrições técnicas, restrições organizacionais e políticas e
convenções (p. ex., diretrizes de programação ou de versionamento, convenções de documentação ou de nomenclatura)

## 3. Contexto e escopo

Delimita o seu sistema de seus parceiros de comunicação (externos) (sistemas
vizinhos e usuários). Especifica as interfaces externas. Mostrado da
perspectiva de negócio/domínio (sempre) ou de uma perspectiva técnica (opcional)

### Conteúdo

O escopo e o contexto do sistema — como o nome sugere — delimitam o seu sistema (ou seja,
o seu escopo) de todos os seus parceiros de comunicação (sistemas vizinhos e usuários,
ou seja, o contexto do seu sistema). Assim, especificam as interfaces externas.

Se necessário, diferencie o contexto de negócio (entradas e saídas específicas do domínio)
do contexto técnico (canais, protocolos, hardware).

### Motivação

As interfaces de domínio e as interfaces técnicas com parceiros de comunicação estão
entre os aspectos mais críticos do seu sistema. Certifique-se de que você as
compreende completamente.

### Forma

- Vários diagramas de contexto

- Listas de parceiros de comunicação e suas interfaces.

## 3.1 Contexto de negócio

### Conteúdo

Especificação de todos os parceiros de comunicação (usuários, sistemas de TI, …) com
explicações das entradas e saídas ou interfaces específicas do domínio. Opcionalmente,
você pode adicionar formatos ou protocolos de comunicação específicos do domínio.

### Motivação

Todas as partes interessadas devem entender quais dados são trocados com o ambiente
do sistema.

### Forma

Todos os tipos de diagramas que mostram o sistema como uma caixa-preta e especificam as
interfaces de domínio com os parceiros de comunicação.

Alternativamente (ou adicionalmente), você pode usar uma tabela. O título da tabela é
o nome do seu sistema, as três colunas contêm o nome do parceiro de comunicação,
as entradas e as saídas.

## 3.2 Contexto técnico

### Conteúdo

Interfaces técnicas (canais e meios de transmissão) que ligam o seu sistema ao
seu ambiente. Além disso, um mapeamento das entradas/saídas específicas do domínio para os
canais, ou seja, uma explicação de qual E/S usa qual canal.

### Motivação

Muitas partes interessadas tomam decisões arquiteturais com base nas interfaces técnicas
entre o sistema e seu contexto. Especialmente projetistas de infraestrutura ou de hardware
decidem essas interfaces técnicas.

### Forma

P. ex., diagrama de implantação UML descrevendo canais para sistemas vizinhos, junto
com uma tabela de mapeamento mostrando as relações entre canais e
entrada/saída.

## 4. Estratégia de solução

Resumo das decisões fundamentais e das estratégias de solução que moldam a
arquitetura. Pode incluir tecnologia, decomposição de nível superior, abordagens para
alcançar os principais objetivos de qualidade e decisões organizacionais relevantes.

### Conteúdo

Um breve resumo e explicação das decisões fundamentais e das estratégias de solução que moldam a arquitetura do sistema. Elas incluem

- decisões de tecnologia

- decisões sobre a decomposição de nível superior do sistema, p. ex., uso de um padrão de arquitetura ou padrão de projeto

- decisões sobre como alcançar os principais objetivos de qualidade

- decisões organizacionais relevantes, p. ex., selecionar um processo de desenvolvimento ou delegar certas tarefas a terceiros.

### Motivação

Essas decisões formam as pedras angulares da sua arquitetura. São a base
para muitas outras decisões detalhadas ou regras de implementação.

### Forma

Mantenha curta a explicação dessas decisões-chave.

Motive o que você decidiu e por que decidiu dessa forma, com base na sua
declaração do problema, nos objetivos de qualidade e nas principais restrições. Remeta aos detalhes nas
seções seguintes (seção 5 para detalhes estruturais, seção 8 para
conceitos transversais).

Você pode usar uma lista de abordagens de solução ou uma tabela.

## 5. Visão de blocos de construção

Decomposição estática do sistema, abstrações do código-fonte, mostradas como
hierarquia de caixas-brancas (contendo caixas-pretas), até o nível de
detalhe apropriado.

### Conteúdo

A visão de blocos de construção mostra a decomposição estática do sistema em
blocos de construção (módulos, componentes, subsistemas, classes, interfaces, pacotes,
bibliotecas, frameworks, camadas, partições, tiers, funções, macros, operações,
estruturas de dados, …), bem como suas dependências (relações, associações,
…)

Essa visão é obrigatória para toda documentação de arquitetura. Em analogia
com uma casa, esta é a planta baixa.

### Motivação

Mantenha uma visão geral do seu código-fonte tornando sua estrutura compreensível
por meio da abstração.

Isso permite que você se comunique com suas partes interessadas em um nível abstrato
sem revelar detalhes de implementação.

### Forma

A visão de blocos de construção é uma coleção hierárquica de caixas-pretas e caixas-brancas
(veja a figura abaixo) e suas descrições.

## 5.1 Caixa-branca: sistema geral

Aqui você descreve a decomposição do sistema geral usando o modelo de caixa-branca a seguir. Ele contém

- um diagrama de visão geral

- uma motivação para a decomposição

- descrições de caixa-preta dos blocos de construção contidos. Para elas, oferecemos alternativas:

  - use uma tabela para uma visão geral curta e pragmática de todos os blocos de construção contidos e suas interfaces

  - use uma lista de descrições de caixa-preta dos blocos de construção de acordo com o modelo de caixa-preta (veja abaixo). Dependendo da sua escolha de ferramenta, essa lista pode ser subcapítulos (em arquivos de texto), subpáginas (em uma wiki) ou elementos aninhados (em uma ferramenta de modelagem).

  - (opcional:) interfaces importantes, que não são explicadas nos modelos de caixa-preta de um bloco de construção, mas são muito importantes para entender a caixa-branca.

Como há tantas maneiras de especificar interfaces, não fornecemos um modelo específico para elas.

No melhor caso, você se virará com exemplos ou assinaturas simples.

## 5.2 Nível 2

Aqui você pode especificar a estrutura interna de (alguns) blocos de construção do nível 1
como caixas-brancas.

Você precisa decidir quais blocos de construção do seu sistema são importantes o suficiente para
justificar uma descrição tão detalhada. Prefira a relevância à completude.
Especifique blocos de construção importantes, surpreendentes, arriscados, complexos ou voláteis. Deixe de fora
as partes normais, simples, enfadonhas ou padronizadas do seu sistema

### 5.2.1 Caixa-branca para o bloco de construção 1

Especifica a estrutura interna do bloco de construção 1.

Use o modelo de caixa-branca (veja acima).

## 6. Visão de tempo de execução

Comportamento dos blocos de construção como cenários, cobrindo casos de uso ou
recursos importantes, interações em interfaces externas críticas, operação e
administração, além do comportamento em erros e exceções.

### Conteúdo

A visão de tempo de execução descreve o comportamento concreto e as interações dos blocos de construção do sistema na forma de cenários das seguintes áreas:

- casos de uso ou recursos importantes: como os blocos de construção os executam?

- interações em interfaces externas críticas: como os blocos de construção cooperam com usuários e sistemas vizinhos?

- operação e administração: lançamento, inicialização, parada

- cenários de erro e exceção

Observação: o principal critério para a escolha dos cenários possíveis (sequências, fluxos de trabalho) é a sua relevância arquitetural. Não é importante descrever um grande número de cenários. Você deve preferir documentar uma seleção representativa.

### Motivação

Você deve entender como (instâncias de) blocos de construção do seu sistema desempenham seu trabalho e se comunicam em tempo de execução. Você capturará principalmente cenários em sua documentação para comunicar sua arquitetura a partes interessadas menos dispostas ou capazes de ler e entender os modelos estáticos (visão de blocos de construção, visão de implantação).

### Forma

Há muitas notações para descrever cenários, p. ex.


- lista numerada de passos (em linguagem natural)

- diagramas de atividades ou fluxogramas

- diagramas de sequência

- BPMN ou EPCs (cadeias de processos orientadas a eventos)

- máquinas de estados

- etc.

## 6.n Cenário de tempo de execução n (1, 2, 3 etc.)

Insira o diagrama de tempo de execução ou a descrição textual do cenário.

Insira a descrição dos aspectos notáveis das interações entre as instâncias de blocos de construção representadas neste diagrama.

## 7. Visão de implantação

Infraestrutura técnica com ambientes, computadores, processadores, topologias.
Mapeamento dos blocos de construção (de software) para os elementos da infraestrutura.

### Conteúdo

A visão de implantação descreve:

- a infraestrutura técnica usada para executar o seu sistema, com elementos de infraestrutura
  como localizações geográficas, ambientes, computadores, processadores,
  canais e topologias de rede, bem como outros elementos de infraestrutura, e

- o mapeamento dos blocos de construção (de software) para esses elementos de infraestrutura.

Com frequência, os sistemas são executados em ambientes diferentes, p. ex., ambiente de desenvolvimento,
ambiente de teste, ambiente de produção. Nesses casos, você deve
documentar todos os ambientes relevantes.

Documente especialmente a visão de implantação quando o seu software for executado como
sistema distribuído com mais de um computador, processador, servidor ou contêiner
ou quando você projetar e construir seus próprios processadores e chips de hardware.

Do ponto de vista de software, é suficiente capturar os elementos da
infraestrutura necessários para mostrar a implantação dos seus blocos de construção.
Arquitetos de hardware podem ir além e descrever a infraestrutura em qualquer
nível de detalhe de que precisem. 

### Motivação

O software não funciona sem hardware. Essa infraestrutura subjacente pode e
vai influenciar o seu sistema e/ou alguns conceitos transversais. Portanto, você
precisa conhecer a infraestrutura.

### Forma

Talvez o diagrama de implantação de nível mais alto já esteja contido na seção 3.2 como contexto técnico, com a sua própria infraestrutura como UMA caixa-preta. Nesta seção você dará zoom nessa caixa-preta usando diagramas de implantação adicionais.

- A UML oferece diagramas de implantação para expressar essa visão. Use-os, provavelmente com diagramas aninhados, quando a sua infraestrutura for mais complexa.

- Quando as suas partes interessadas (de hardware) preferirem outros tipos de diagramas em vez
  do diagrama de implantação UML, deixe que usem qualquer tipo capaz de mostrar nós e
  canais da infraestrutura.

## 7.1 Infraestrutura nível 1

Descreva (geralmente em uma combinação de diagramas, tabelas e texto):

- a distribuição do seu sistema por múltiplas localizações, ambientes, computadores, processadores, .. bem como as conexões físicas entre eles

- justificativa ou motivação importante para essa estrutura de implantação

- recursos de qualidade e/ou desempenho da infraestrutura

- o mapeamento de artefatos de software (blocos de construção) para elementos da infraestrutura

Para múltiplos ambientes ou implantações alternativas, copie essa seção do arc42 para todos os ambientes relevantes. **

## 7.2 Infraestrutura nível 2

Aqui você pode incluir a estrutura interna de (alguns) elementos de infraestrutura do nível 1 da infraestrutura.

Copie a estrutura do nível 1 para cada elemento selecionado.

## 8. Conceitos transversais

Regulamentações gerais e principais e abordagens de solução relevantes em várias
partes (→ transversais) do sistema. Os conceitos costumam estar relacionados a vários
blocos de construção. Inclua tópicos diferentes, como modelos de domínio, padrões
e estilos de arquitetura, regras para o uso de tecnologias específicas e regras
de implementação.

### Conteúdo

Esta seção descreve conceitos transversais (práticas, padrões, regulamentações
ou ideias de solução). Esses conceitos costumam estar relacionados a vários blocos de construção.
Eles podem incluir muitos tópicos diferentes.

### Motivação

Os conceitos formam a base da integridade conceitual (consistência, homogeneidade)
da arquitetura. Assim, são uma contribuição importante para alcançar as qualidades
internas do seu sistema.

Este é o lugar no modelo que fornecemos para uma especificação coesa
desses conceitos.

Muitos desses conceitos se relacionam com vários dos seus blocos de construção ou os influenciam.

### Forma

A forma pode variar:

- documentos conceituais com qualquer tipo de estrutura

- implementações de exemplo, especialmente para conceitos técnicos

- trechos de modelos transversais ou cenários usando notações das visões de arquitetura

### Estrutura desta seção

Escolha apenas os tópicos mais necessários para o seu sistema e atribua a cada um um título de nível 2 nesta seção (p. ex., 8.1, 8.2 etc.).

- NÃO TENTE cobrir todos os tópicos do diagrama mencionado anteriormente.

### Contexto

Alguns tópicos dentro dos sistemas frequentemente dizem respeito a vários blocos de construção, elementos de hardware ou processos de
desenvolvimento. Pode ser mais fácil comunicar ou documentar
esses tópicos transversais em um local central, em vez de repeti-los na
descrição dos blocos de construção, elementos de hardware ou processos de
desenvolvimento envolvidos.

Certos conceitos podem dizer respeito a todos os elementos de um sistema; outros podem ser
relevantes apenas para alguns.

## 9. Decisões de arquitetura

Decisões de arquitetura importantes, caras, críticas, de grande escala ou arriscadas,
incluindo justificativas.

### Conteúdo

Decisões de arquitetura importantes, caras, de grande escala ou arriscadas, incluindo
justificativas. Por “decisões” entendemos selecionar uma alternativa com base em critérios
dados.

Use seu julgamento para decidir se uma decisão de arquitetura deve ser
documentada aqui, nesta seção central, ou se é melhor documentá-la
localmente (p. ex., dentro do modelo de caixa-branca de um bloco de construção). Evite
textos redundantes. Remeta à seção 4, onde você já capturou as decisões mais importantes
da sua arquitetura.

### Motivação

As partes interessadas do seu sistema devem poder compreender e refazer o percurso das suas
decisões.

### Forma

- ADR (registro de decisão de arquitetura) para cada decisão importante

- lista ou tabela, ordenada por importância e consequências, ou

- de forma mais detalhada, em seções separadas por decisão

### Contexto (sobre ADRs)

Peças menores de documentação são mais fáceis de ler, criar e manter. Quando se trata
de decisões de arquitetura, as equipes de desenvolvimento frequentemente:

- conhecem a decisão, pois ela é visível, p. ex., no código-fonte, mas

- desconhecem a motivação por trás dessa decisão (veja Nygard 2011)

Portanto, você deve documentar algumas decisões importantes junto com sua
motivação e raciocínio

### Nossa proposta sobre decisões

Mantenha uma coleção de decisões arquiteturalmente significativas, aquelas decisões que
afetam a estrutura, as características de qualidade, dependências (especialmente externas)
e interfaces importantes ou técnicas de construção (obrigado a Michael
Nygard por esta proposta).

## 10. Requisitos de qualidade

Requisitos de qualidade como cenários, com árvore de qualidade para fornecer uma visão
geral de alto nível. Os objetivos de qualidade mais importantes devem ter sido descritos na seção
1.2 (objetivos de qualidade).

### Conteúdo

Esta seção contém todos os requisitos de qualidade relevantes.

Os mais importantes desses requisitos já foram descritos na seção
1.2 (objetivos de qualidade); portanto, aqui eles só devem ser referenciados. Nesta
seção 10 você também deve capturar requisitos de qualidade de menor importância,
que não criarão riscos altos se não forem totalmente alcançados (mas podem ser
desejáveis).

### Motivação

Como os requisitos de qualidade terão muita influência nas decisões
arquiteturais, você deve saber quais qualidades são realmente importantes para as suas
partes interessadas, de maneira específica e mensurável.

### Mais informações

Veja o extenso modelo de qualidade Q42 em https://quality.arc42.org.

## 10.1 Visão geral dos requisitos de qualidade

### Conteúdo

Uma visão geral ou resumo dos requisitos de qualidade.

### Motivação

Frequentemente nos deparamos com dezenas (ou até centenas) de requisitos de qualidade detalhados.
Nesta seção de visão geral, você deve tentar resumir, p. ex., descrevendo
categorias ou tópicos (como sugerem a ISO 25010:2023 ou o Q42

Se essas descrições resumidas já forem precisas, específicas o bastante e
mensuráveis, você pode pular a seção 10.2.

### Forma

Use uma tabela simples em que cada linha contenha uma categoria ou tópico e uma breve
descrição do requisito de qualidade. Alternativamente, você pode usar um mapa mental para estruturar esses requisitos de qualidade.

Na literatura, também foi descrita a ideia de uma árvore de atributos de qualidade,
que coloca o termo genérico “qualidade” como raiz e usa um refinamento em forma de árvore
do termo “qualidade”. [Bass+21] introduziu o termo “Quality
Attribute Utility Tree” para esse fim.

## 10.2 Cenários de qualidade

### Conteúdo

Os cenários de qualidade tornam os requisitos de qualidade concretos e permitem decidir se
eles foram cumpridos (no sentido de critérios de aceitação). Garanta que os seus
cenários sejam específicos e mensuráveis.

Dois tipos de cenários são especialmente úteis:

- Cenários de uso (também chamados de cenários de aplicação ou cenários de caso de uso)
  descrevem a reação em tempo de execução do sistema a um determinado estímulo. Isso também
  inclui cenários que descrevem a eficiência ou o desempenho do sistema.
  Exemplo: o sistema reage à solicitação de um usuário em até um segundo.

- Cenários de mudança descrevem o efeito desejado de uma modificação ou extensão do
  sistema ou de seu ambiente imediato. Exemplo: uma funcionalidade adicional
  é implementada ou os requisitos de um atributo de qualidade mudam, e o esforço ou
  a duração da mudança é medido.

### Forma

Informações típicas para cenários detalhados incluem as seguintes:

Em forma curta (preferida no modelo Q42):

- Contexto/Antecedentes: que tipo de sistema ou componente, qual é o ambiente ou a situação?

- Fonte/Estímulo: quem ou o que inicia ou aciona um comportamento, reação ou ação.

- Métrica/Critérios de aceitação: uma resposta que inclui uma medida ou métrica

A forma longa dos cenários (preferida pelo SEI e por [Bass+21]) é mais detalhada e inclui as seguintes informações:

- ID do cenário: um identificador único para o cenário.

- Nome do cenário: um nome curto e descritivo para o cenário.

- Fonte: a entidade (usuário, sistema ou evento) que inicia o cenário.

- Estímulo: o evento ou condição desencadeante que o sistema deve tratar.

- Ambiente: o contexto operacional ou a condição sob a qual o sistema experimenta o estímulo.

- Artefato: os blocos de construção ou outros elementos do sistema afetados pelo estímulo.

- Resposta: o resultado ou comportamento que o sistema exibe em reação ao estímulo.

- Medida da resposta: os critérios ou a métrica pelos quais a resposta do sistema é avaliada.

### Veja também

Desde janeiro de 2023, o arc42 fornece um modelo de qualidade pragmático, que propõe
rotular os requisitos de qualidade com hashtags ou rótulos como #flexible, #efficient,
#usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Riscos e dívida técnica

Riscos técnicos ou dívida técnica conhecidos. Que problemas potenciais existem dentro do sistema ou
ao redor dele? Com o que a equipe de desenvolvimento se sente péssima?

### Conteúdo

Uma lista de riscos técnicos ou dívidas técnicas identificados, ordenada por prioridade

### Motivação

“Gestão de riscos é gestão de projetos para adultos” (Tim Lister, Atlantic
Systems Guild.)

Este deve ser o seu lema para a detecção e avaliação sistemáticas de riscos e
dívidas técnicas na arquitetura, que serão necessárias para as partes interessadas da gestão (p. ex., gerentes de projeto, product owners) como parte da análise
de riscos geral e do planejamento de medidas.

### Forma

Lista de riscos e/ou dívidas técnicas, provavelmente incluindo medidas sugeridas para
minimizar, mitigar ou evitar riscos ou reduzir dívidas técnicas.
