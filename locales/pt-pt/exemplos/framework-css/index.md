# Registro de decisão de arquitetura: framework CSS

Sumário:

- [Resumo](#resumo)
  - [Questão](#questão)
  - [Decisão](#decisão)
  - [Estado](#estado)
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

  * Queremos aplicações responsivas, especialmente para telas menores, como em dispositivos móveis, telas maiores, como widescreens 4K, e telas dinâmicas, como monitores rotacionáveis.  


### Decisão

Decidido pelo Bulma.


### Estado

Decidido pelo Bulma. Abertos a novas escolhas de frameworks CSS à medida que surgirem.


## Detalhes


### Premissas

Queremos criar apps web modernos, rápidos, confiáveis, responsivos etc.

Os apps web modernos típicos estão reduzindo/eliminando o uso do jQuery por vários motivos: 

  * O JavaScript moderno está incorporando gradualmente muitas capacidades que o jQuery oferecia, então o jQuery é menos necessário, e há módulos melhores/mais rápidos/menores que fornecem implementações específicas

  * A abordagem ampla do jQuery é manipular o DOM diretamente, o que é um antipadrão para frameworks JavaScript modernos (p. ex., React, Vue, Svelte)

  * O jQuery interfere em si mesmo se for carregado duas vezes, etc.


### Restrições

Se escolhermos um framework CSS que usa jQuery, ficaremos presos a importar o jQuery. Por exemplo, o Semantic UI usa jQuery, e o Tachyons não.

Se escolhermos um framework CSS mínimo, abrimos mão de componentes do framework que podemos querer agora ou em breve. Por exemplo, o Semantic UI fornece um carrossel de imagens, e o Tachyons não.


### Posições

Consideramos não usar framework. Isso ainda parece viável, especialmente porque o CSS grid fornece grande parte do que precisamos para o nosso projeto.

Consideramos muitos frameworks CSS por meio de uma triagem rápida em lista curta: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons etc. Nossas duas seleções para uma revisão mais profunda são o Semantic UI (porque tem a abordagem mais semântica) e o Bulma (porque tem a abordagem mais leve que fornece os componentes que queremos agora).

Consideramos o Semantic UI. Ele fornece muitos componentes, incluindo os que queremos para o nosso projeto: abas, grades, botões etc. Fizemos um piloto com o Semantic UI de duas maneiras: usando arquivos CDN típicos e usando repositórios NPM. Tivemos sucesso com o Semantic UI em uma página HTML estática, mas não obtivemos sucesso dentro do nosso prazo para construir uma SPA em JavaScript (principalmente por problemas de carregamento do jQuery). Descobrimos que outros programadores vêm pedindo aos desenvolvedores do Semantic UI que criem uma versão sem jQuery, pelos mesmos motivos que nós. Outros programadores vêm pedindo uma versão sem jQuery há muitos anos, mas os desenvolvedores disseram não e declararam que qualquer versão sem jQuery seria difícil demais de escrever, p. ex. ~"o projeto Semantic UI tem mais de 22.000 pontos de contato que usam jQuery".

Exemplo com Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Consideramos o Bulma. O Bulma tem muitas capacidades semelhantes às do Semantic UI, embora não tantos componentes sofisticados. O Bulma é construído com técnicas modernas, como a ausência de jQuery. O Bulma tem alguns componentes de terceiros, dos quais podemos querer usar alguns.


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

Especificamente, o Semantic UI parece ter uma bandeira de cautela tanto em termos de tecnologia (ou seja, tantos pontos de contato com o jQuery) quanto em termos de liderança (ou seja, ficar sem jQuery foi um não categórico, em vez de tentar um roteiro, ou melhoria contínua, ou arrecadação de doações etc.).


### Implicações

Se encontrarmos um bom framework CSS sem jQuery, isso geralmente é útil e bom no geral.


## Relacionado


### Decisões relacionadas

O framework CSS que escolhermos pode afetar a testabilidade.


### Requisitos relacionados

Queremos lançar rapidamente um app puramente moderno. 

Não queremos gastar tempo trabalhando em frameworks mais antigos (esp. Semantic UI) que usam dependências mais antigas (esp. jQuery).


### Artefatos relacionados

Afeta todo o HTML típico que usará o CSS.


### Princípios relacionados

Facilmente reversível.

Necessidade de velocidade.


## Notas

Quaisquer notas aqui.
