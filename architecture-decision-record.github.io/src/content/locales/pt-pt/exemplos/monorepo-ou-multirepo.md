# Monorepo ou multirepo

Sumário:

* [Resumo](#resumo)
  * [Questão](#questão)
  * [Decisão](#decisão)
  * [Estado](#estado)
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

Nosso projeto envolve o desenvolvimento de três grandes categorias de software:

  * GUIs de front-end
  * Serviços de middleware
  * Servidores de back-end

Quando desenvolvemos, nosso sistema de controle de versão (VCS) de gerenciamento de código-fonte (SCM) é o git.

Precisamos escolher como usamos o git para organizar nosso código.

A escolha de nível superior é organizar como “monorepo”, “polirepo” ou “híbrido”:

  * Monorepo significa que colocamos todas as partes em um grande repositório
  * Polirepo significa que colocamos cada parte em seu próprio repositório
  * Híbrido significa alguma mistura de monorepo e polirepo

Para saber mais, veja https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Decisão

Monorepo quando uma organização/equipe/projeto é relativamente pequena e a iteração rápida tem maior prioridade do que sustentar a estabilidade.

Polirepo quando uma organização/equipe/projeto é relativamente grande e sustentar a estabilidade tem maior prioridade do que a iteração rápida.


### Estado

Decidido. Abertos a revisitar se/quando surgirem novas ferramentas para gerenciar monorepos e/ou polirepos.


## Detalhes


### Premissas

Todo o código que estamos desenvolvendo é para as ofertas de uma organização, e não para o público em geral. Ou seja, o Broker-Dealer não pretende ter nada parecido com desenvolvedores voluntários do público em geral.


### Restrições

As restrições estão bem documentadas em https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Posições

Consideramos monorepos no estilo do Google, do Facebook etc. Achamos que quaisquer problemas de escalabilidade do monorepo estão tão distantes no futuro que, quando precisarmos delas, poderemos aproveitar as mesmas práticas do Google e do Facebook.

Consideramos polirepos no estilo dos projetos open source típicos do Git, como Google Android, Facebook React etc. Achamos que são a melhor escolha para a participação do público em geral (p. ex., qualquer pessoa no mundo pode trabalhar no código) e para a disponibilidade individual (p. ex., o projeto é usado por si só, sem nenhuma outra parte).


### Argumento

Quando uma organização/equipe/projeto é relativamente pequena, escolhemos monorepo, porque a iteração rápida tem prioridade significativamente maior do que sustentar a estabilidade

Quando uma organização/equipe/projeto é relativamente grande, escolhemos polirepo, porque sustentar a estabilidade tem prioridade significativamente maior do que a iteração rápida.


### Implicações

Se houver um pipeline de CI+CD existente, talvez precisemos ajustá-lo para testar vários projetos dentro de um repositório.

O CI+CD pode levar mais tempo para um build completo de um monorepo, porque o CI+CD pode fazer o build de todos os projetos do monorepo.

Se uma organização/equipe/projeto crescer, o monorepo terá problemas de escalabilidade.

Os problemas de escalabilidade do monorepo podem tornar cada vez mais valiosa a transição para um polirepo.

A transição de monorepo para polirepo é uma tarefa significativa de devops e precisará ser planejada, gerenciada e programada.


## Relacionado


### Decisões relacionadas

Criaremos decisões para as ferramentas relacionadas ao gerenciamento de monorepos (p. ex., Google Bazel) e polirepos (p. ex., Lyft Refactorator).


### Requisitos relacionados

Precisamos desenvolver o pipeline de CI+CD para funcionar bem com o git.


### Artefatos relacionados

Esperamos que a organização dos repositórios tenha artefatos relacionados para provisionamento, gerenciamento de configuração, testes e áreas de devops semelhantes. 


### Princípios relacionados

Facilmente reversível. Se o monorepo não funcionar na prática ou não for desejado pela liderança, é simples mudar para polirepo.

Obsessão pelo cliente. Valorizamos colocar o projeto nas mãos dos clientes e acreditamos que um monorepo pode nos levar até lá mais rápido do que um polirepo, além de ajudar a iterar mais rápido.

Pense grande. O Google e o Facebook são defensores muito fortes de monorepos em vez de polirepos, porque todas as ofertas principais podem ser desenvolvidas/testadas/implantadas em conjunto.


## Notas

Adicione quaisquer notas aqui.
