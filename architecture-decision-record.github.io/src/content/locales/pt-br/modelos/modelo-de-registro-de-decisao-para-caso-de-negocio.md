# Modelo de registro de decisão para caso de negócio

Este modelo de ADR enfatiza a criação de um caso de negócio para uma decisão, incluindo critérios, candidatos e custos.


## Nível superior

* Título
* Status
* Critérios de avaliação
* Candidatos a considerar
* Pesquisa e análise de cada candidato
  * Atende/não atende aos critérios e por quê
  * Análise de custos
  * Análise SWOT
  * Opiniões e feedback
* Recomendação


## Detalhamento de baixo nível

**Título**:

  * Uma frase imperativa curta no presente, com menos de 50 caracteres, como uma mensagem de commit git.

**Status**:

  * Um de proposto, aceito, rejeitado, obsoleto, substituído etc.

**Critérios de avaliação**:

  * Resumo: explique brevemente o que buscamos descobrir e por quê.

  * Detalhes

**Candidatos a considerar**:

  * Resumo: explique brevemente como descobrimos os candidatos e chame atenção para quaisquer outliers.

  * Liste todos os candidatos e opções relacionadas; o que estamos avaliando como soluções potenciais?

  * Detalhes

**Pesquisa e análise de cada candidato**:

  * Resumo: explique brevemente os métodos de pesquisa e chame atenção para padrões, agrupamentos e outliers.

  * Atende/não atende aos critérios e por quê

    * Resumo

    * Detalhes

  * Análise de custos

    * Resumo

    * Exemplos

      * Licenciamento, como acordos contratuais e compromissos legais

      * Treinamento, como capacitação e gestão de mudanças

      * Operação, como suporte e manutenção

      * Medição, como largura de banda e uso de CPU

  * Análise SWOT

    * Resumo

    * Forças

    * Fraquezas

    * Oportunidades

    * Ameaças

  * Opiniões e feedback internos

    * Resumo

    * Exemplos

      * Pela equipe, idealmente escritos pela própria pessoa

      * De outras partes interessadas

      * Atributos de qualidade, também conhecidos como requisitos transversais

  * Opiniões e feedback externos

    * Resumo

    * Quem está dando a opinião?

    * Quais são os outros candidatos que você considerou?

    * O que você está criando?

      * Exemplos

        * B2B ou B2C

        * voltado externamente ou somente para funcionários

        * desktop ou mobile

        * piloto ou produção

        * monólito ou microsserviços

    * Como você avaliou os candidatos?

    * Por que você escolheu o vencedor?

    * O que aconteceu desde então?

      * Exemplos

        * Como o vencedor está se saindo?

        * Que % do tráfego de usuários reais em produção está passando pelo vencedor?

        * Que tipos de integrações estão envolvidas, como com pipelines de entrega contínua, sistemas de gestão de conteúdo, analytics e métricas etc.?

        * Sabendo o que você sabe agora, o que aconselharia as pessoas a fazer de modo diferente?

  * Anedotas

**Recomendação**:

  * Resumo

  * Detalhes
