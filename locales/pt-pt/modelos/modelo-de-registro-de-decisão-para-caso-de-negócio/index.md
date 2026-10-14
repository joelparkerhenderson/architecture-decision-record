# Modelo de registro de decisão para caso de negócio

Este modelo de ADR enfatiza a criação de um caso de negócio para uma decisão, incluindo critérios, candidatos e custos.


## Nível superior

* Título
* Estado
* Critérios de avaliação
* Candidatos a considerar
* Pesquisa e análise de cada candidato
  * Atende/não atende aos critérios e por quê
  * Análise de custos
  * Análise SWOT
  * Opiniões e feedback
* Recomendação


## Aprofundamento em nível baixo

**Título**:

  * Uma locução curta no imperativo do presente, com menos de 50 caracteres, como uma mensagem de commit do git.

**Estado**:

  * Um destes: proposed, accepted, rejected, deprecated, superseded etc.

**Critérios de avaliação**:

  * Resumo: explique brevemente o que buscamos descobrir e por quê.

  * Detalhes

**Candidatos a considerar**:

  * Resumo: explique brevemente como descobrimos os candidatos e chame a atenção para quaisquer pontos fora da curva.

  * Liste todos os candidatos e opções relacionadas; o que estamos avaliando como soluções potenciais?

  * Detalhes

**Pesquisa e análise de cada candidato**:

  * Resumo: explique brevemente os métodos de pesquisa e chame a atenção para padrões, agrupamentos e pontos fora da curva.

  * Atende/não atende aos critérios e por quê

    * Resumo

    * Detalhes

  * Análise de custos

    * Resumo

    * Exemplos

      * Licenciamento, como acordos contratuais e compromissos legais

      * Treinamento, como capacitação e gestão de mudanças

      * Operação, como suporte e manutenção

      * Medição, como uso de largura de banda e de CPU

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

      * Atributos de qualidade, também conhecidos como requisitos multifuncionais 

  * Opiniões e feedback externos

    * Resumo

    * Quem está fornecendo a opinião?

    * Quais outros candidatos você considerou?

    * O que você está criando? 

      * Exemplos

        * B2B ou B2C

        * voltado ao público externo ou apenas para funcionários

        * desktop ou móvel

        * piloto ou produção

        * monólito ou microsserviços

    * Como você avaliou os candidatos?

    * Por que você escolheu o vencedor?

    * O que está acontecendo desde então?

      * Exemplos

        * Como o vencedor está se saindo?

        * Que % do tráfego real de usuários em produção está passando pelo vencedor?

        * Que tipos de integrações estão envolvidos, como com pipelines de entrega contínua, sistemas de gestão de conteúdo, análises e métricas etc.?

        * Sabendo o que sabe agora, o que você aconselharia as pessoas a fazer de modo diferente?

  * Anedotas

**Recomendação**:

  * Resumo

  * Detalhes
