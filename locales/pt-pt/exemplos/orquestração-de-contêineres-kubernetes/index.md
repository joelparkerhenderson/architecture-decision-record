# Registro de decisão de arquitetura: orquestração de contêineres Kubernetes

## Declaração do problema 

Precisamos selecionar uma plataforma de orquestração de contêineres para o nosso crescente portfólio de aplicações nativas da nuvem. A implantação da nossa atual plataforma legada é lenta demais e não é ágil o bastante para acompanhar nossas necessidades crescentes. Procuramos um sistema que nos permita escalar nossos serviços da maneira mais eficiente possível, sem comprometer a agilidade ou a facilidade de uso.

## Alternativas consideradas

1. Docker Swarm

2. Kubernetes

3. Apache Mesos

## Decisão tomada

Após realizar uma análise minuciosa de cada plataforma de orquestração de contêineres, decidimos adotar o Kubernetes como a melhor opção para as nossas necessidades corporativas. Nossos motivos para escolher o Kubernetes são os seguintes:

1. **Escalabilidade:**  o design único do Kubernetes é perfeito para escalar aplicações e, à medida que nossos requisitos de escalabilidade evoluem ao longo do tempo, o Kubernetes tem a capacidade integrada de atender a essas mudanças sem problemas.

2. **Arquitetura descentralizada:**  a topologia mestre-trabalhador do Kubernetes garante uma arquitetura descentralizada, o que assegura que não haja um ponto único de falha.

3. **Apoio da comunidade:**  o Kubernetes tem a maior e mais ativa comunidade de código aberto, o que significa que tem um grande número de colaboradores, desenvolvedores e fornecedores, facilitando para nós obter ajuda e encontrar recursos.

4. **Apoio do ecossistema:**  o Kubernetes tem um ecossistema em crescimento, com uma variedade de ferramentas de terceiros, integrações com registros de contêineres, pipelines de CI/CD, armazenamento de dados e mais.

Portanto, decidimos adotar o Kubernetes como nossa plataforma de orquestração de contêineres para o presente e o futuro imediato.

<h6>Crédito: esta página foi gerada pelo ChatGPT e depois editada quanto à clareza e ao formato.</h6>
