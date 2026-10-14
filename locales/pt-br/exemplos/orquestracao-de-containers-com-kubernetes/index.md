# Registro de Decisão de Arquitetura: orquestração de containers com Kubernetes

## Declaração do problema

Precisamos selecionar uma plataforma de orquestração de containers para nosso portfólio crescente de aplicações cloud-native. A implantação da nossa plataforma legada atual é lenta demais e não é ágil o suficiente para acompanhar nossas necessidades crescentes. Estamos procurando um sistema que nos permita escalar nossos serviços da forma mais eficiente possível sem comprometer a agilidade ou a facilidade de uso.

## Alternativas consideradas

1. Docker Swarm

2. Kubernetes

3. Apache Mesos

## Decisão tomada

Depois de conduzir uma análise completa de cada plataforma de orquestração de containers, decidimos adotar Kubernetes como a melhor opção para nossas necessidades corporativas. Nossas razões para escolher Kubernetes são as seguintes:

1. **Escalabilidade:**  O design único do Kubernetes é perfeito para escalar aplicações e, à medida que nossos requisitos de escalabilidade evoluírem com o tempo, Kubernetes tem a capacidade integrada de atender a essas mudanças sem problemas.

2. **Arquitetura descentralizada:**  A topologia master-worker do Kubernetes garante uma arquitetura descentralizada que assegura que não haja ponto único de falha.

3. **Suporte da comunidade:**  Kubernetes tem a maior e mais ativa comunidade open-source, o que significa que tem um grande número de contribuidores, desenvolvedores e fornecedores, tornando mais fácil para nós obter ajuda e encontrar recursos.

4. **Suporte do ecossistema:**  Kubernetes tem um ecossistema crescente com uma variedade de ferramentas de terceiros, integrações com registros de containers, pipelines de CI/CD, armazenamento de dados e mais.

Portanto, decidimos adotar Kubernetes como nossa plataforma de orquestração de containers para o presente e o futuro imediato.

<h6>Crédito: esta página é gerada pelo ChatGPT e depois editada para clareza e formato.</h6>
