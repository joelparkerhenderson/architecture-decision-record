# Registro de Decisão de Arquitetura: framework CSS

Conteúdo:

- [Resumo](#resumo)
  - [Questão](#questão)
  - [Decisão](#decisão)
  - [Status](#status)
- [Detalhes](#detalhes)
  - [Premissas](#premissas)
  - [Restrições](#restrições)
  - [Posições](#posições)
  - [Argumento](#argumento)
  - [Implicações](#implicações)
- [Relacionado](#relacionado)
  - [Decisões relacionadas](#decisões-relacionadas)
  - [Requisitos relacionados](#requisitos-relacionados)
  - [Artefatos relacionados](#artefatos-relacionados)
  - [Princípios relacionados](#princípios-relacionados)
- [Notas](#notas)


## Resumo


### Questão

Queremos usar um framework CSS para criar nossas aplicações web:

  * Queremos que a experiência do usuário seja rápida e confiável, em todos os navegadores populares e tamanhos de tela.

  * Queremos iteração rápida em design, layout, UI/UX etc.

  * Queremos aplicações responsivas, especialmente para telas menores, como em dispositivos móveis, telas maiores, como widescreens 4K, e telas dinâmicas, como displays rotativos.


### Decisão

Decidido por Bulma.


### Status

Decidido por Bulma. Aberto a novas escolhas de framework CSS conforme surgirem.


## Detalhes


### Premissas

Queremos criar apps web modernos, rápidos, confiáveis, responsivos etc.

Apps web modernos típicos estão reduzindo/eliminando o uso de jQuery por múltiplos motivos:

  * JavaScript moderno está introduzindo muitas capacidades que jQuery forneceu, então jQuery é menos necessário, e há módulos melhores/mais rápidos/menores que fornecem implementações específicas

  * A abordagem ampla do jQuery é fazer manipulação direta do DOM, o que é um antipadrão para frameworks JavaScript modernos (por exemplo, React, Vue, Svelte)

  * jQuery interfere consigo mesmo se for carregado duas vezes etc.


### Restrições

Se escolhermos um framework CSS que usa jQuery, então ficamos presos a importar jQuery. Por exemplo, Semantic UI usa jQuery, e Tachyons não.

Se escolhermos um framework CSS mínimo, então abrimos mão de componentes de framework que podemos querer agora ou em breve. Por exemplo, Semantic UI fornece um carrossel de imagens, e Tachyons não.


### Posições

Consideramos não usar framework. Isso ainda parece viável, especialmente porque CSS grid fornece muito do que precisamos para nosso projeto..

Consideramos muitos frameworks CSS usando uma triagem rápida de shortlist: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons etc. Nossas duas seleções para revisão mais profunda são Semantic UI (porque tem a abordagem mais semântica) e Bulma (porque tem a abordagem mais leve que fornece os componentes que queremos agora).

Consideramos Semantic UI. Ele fornece muitos componentes, incluindo os que queremos para nosso projeto: abas, grids, botões etc. Fizemos um piloto com Semantic UI de duas formas: usando arquivos CDN típicos e usando repositórios NPM. Obtivemos sucesso com Semantic UI em uma página HTML estática, mas não obtivemos sucesso dentro do nosso timebox para construir uma SPA JavaScript (principalmente por causa de problemas de carregamento do jQuery). Descobrimos que outros coders vêm pedindo aos desenvolvedores do Semantic UI para criar uma versão sem jQuery, pelos mesmos motivos que temos. Outros coders vêm solicitando uma versão sem jQuery há muitos anos, mas os desenvolvedores disseram não e afirmaram que qualquer versão sem jQuery seria difícil demais de escrever, por exemplo, ~"the Semantic UI project has more than 22,000 touchpoints that use jQuery".

Exemplo com Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Consideramos Bulma. Bulma tem muitas capacidades semelhantes às do Semantic UI, embora não tantos componentes sofisticados. Bulma é construído com técnicas modernas, como ausência de jQuery. Bulma tem alguns componentes de terceiros, alguns dos quais talvez queiramos usar.


Exemplo com Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argumento

Como acima.

Especificamente, Semantic UI parece ter um sinal de cautela tanto em termos de tecnologia (ou seja, tantos pontos de contato com jQuery) quanto em termos de liderança (ou seja, sem jQuery foi um não firme, em vez de tentar um roadmap, ou melhoria contínua, ou captação de doações etc.).


### Implicações

Se encontrarmos um bom framework CSS sem jQuery, isso geralmente é útil e bom no geral.


## Relacionado


### Decisões relacionadas

O framework CSS que escolhermos pode afetar a testabilidade.


### Requisitos relacionados

Queremos entregar rapidamente um app puramente moderno.

Não queremos gastar tempo trabalhando em frameworks mais antigos (especialmente Semantic UI) usando dependências mais antigas (especialmente jQuery).


### Artefatos relacionados

Afeta todo o HTML típico que usará o CSS.


### Princípios relacionados

Facilmente reversível.

Necessidade de velocidade.


## Notas

Quaisquer notas aqui.
