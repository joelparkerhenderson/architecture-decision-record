# Monorepo vs multirepo

Conteúdo:

* [Resumo](#resumo)
  * [Questão](#questão)
  * [Decisão](#decisão)
  * [Status](#status)
* [Detalhes](#detalhes)
  * [Premissas](#premissas)
  * [Restrições](#restrições)
  * [Posições](#posições)
  * [Argumento](#argumento)
  * [Implicações](#implicações)
* [Relacionado](#relacionado)
  * [Decisões relacionadas](#decisões-relacionadas)
  * [Requisitos relacionados](#requisitos-relacionados)
  * [Artefatos relacionados](#artefatos-relacionados)
  * [Princípios relacionados](#princípios-relacionados)
* [Notas](#notas)


## Resumo


### Questão

Nosso projeto envolve desenvolver três grandes categorias de software:

  * GUIs front-end
  * Serviços de middleware
  * Servidores back-end

Quando desenvolvemos, nosso sistema de controle de versão (VCS) para gerenciamento de código-fonte (SCM) é o git.

Precisamos escolher como usamos o git para organizar nosso código.

A escolha de alto nível é organizar como "monorepo", "polyrepo" ou "híbrido":

  * Monorepo significa colocar todas as partes em um grande repo
  * Polyrepo significa colocar cada parte em seu próprio repo
  * Híbrido significa alguma mistura de monorepo e polyrepo

Para mais informações, veja https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Decisão

Monorepo quando uma organização/equipe/projeto é relativamente pequena, e iteração rápida tem prioridade maior do que sustentar estabilidade.

Polyrepo quando uma organização/equipe/projeto é relativamente grande, e sustentar estabilidade tem prioridade maior do que iteração rápida.


### Status

Decidido. Aberto a revisitar se/quando novas ferramentas ficarem disponíveis para gerenciar monorepos e/ou polyrepos.


## Detalhes


### Premissas

Todo o código que estamos desenvolvendo é para as ofertas de uma organização, e não para o público em geral. Ou seja, a Broker-Dealer não pretende ter algo como desenvolvedores voluntários do público em geral.


### Restrições

As restrições estão bem documentadas em https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Posições

Consideramos monorepos no estilo de Google, Facebook etc. Achamos que quaisquer problemas de escala de monorepo estão tão distantes no futuro que poderemos aproveitar as mesmas práticas de Google e Facebook quando precisarmos delas.

Consideramos polyrepos no estilo de projetos open source típicos em Git, como Google Android, Facebook React etc. Achamos que esses são a melhor escolha para participação do público em geral (por exemplo, qualquer pessoa no mundo pode trabalhar no código) e disponibilidade individual (por exemplo, o projeto é usado por conta própria, sem nenhuma outra parte).


### Argumento

Quando uma organização/equipe/projeto é relativamente pequena, escolhemos monorepo, porque a iteração rápida é significativamente mais prioritária do que sustentar estabilidade.

Quando uma organização/equipe/projeto é relativamente grande, escolhemos polyrepo, porque sustentar estabilidade é significativamente mais prioritário do que iteração rápida.


### Implicações

Se houver um pipeline existente de CI+CD, talvez precisemos ajustá-lo para testar múltiplos projetos dentro de um repo.

CI+CD poderia levar mais tempo para uma build completa de um monorepo, porque CI+CD poderia construir todos os projetos no monorepo.

Se uma organização/equipe/projeto crescer, então um monorepo terá problemas de escala.

Problemas de escala de monorepo podem tornar cada vez mais valiosa uma transição para polyrepo.

A transição de monorepo para polyrepo é uma tarefa significativa de devops, e precisará ser planejada, gerenciada e programada.


## Relacionado


### Decisões relacionadas

Criaremos decisões para ferramentas relacionadas para gerenciar monorepos (por exemplo, Google Bazel) e polyrepos (por exemplo, Lyft Refactorator).


### Requisitos relacionados

Precisamos desenvolver o pipeline de CI+CD para funcionar bem com git.


### Artefatos relacionados

Esperamos que a organização do repo tenha artefatos relacionados para provisionamento, gerenciamento de configuração, testes e áreas semelhantes de devops.


### Princípios relacionados

Facilmente reversível. Se o monorepo não funcionar na prática, ou não for desejado pela liderança, é simples mudar para polyrepo.

Customer Obsession. Valorizamos colocar o projeto nas mãos dos clientes, e acreditamos que um monorepo pode nos levar até lá mais rapidamente do que um polyrepo, além de nos ajudar a iterar mais rápido.

Think big. Google e Facebook defendem fortemente monorepos em vez de polyrepos, porque todas as ofertas principais podem ser desenvolvidas/testadas/implantadas em conjunto.


## Notas

Adicione quaisquer notas aqui.
