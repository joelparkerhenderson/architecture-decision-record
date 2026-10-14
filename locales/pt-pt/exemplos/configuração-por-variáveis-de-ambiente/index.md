# Configuração por variáveis de ambiente

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

Queremos que nossas aplicações sejam configuráveis além de artefatos/binários/código-fonte, de modo que um mesmo build possa se comportar de maneira diferente dependendo do ambiente de implantação.

  * Para isso, queremos usar a configuração por variáveis de ambiente.

  * Queremos gerenciar a configuração usando arquivos que possamos versionar.

  * Queremos oferecer alguma ergonomia de experiência do desenvolvedor, como saber o que pode ser configurado e quais são os padrões relevantes.


### Decisão

Decidido por arquivos .env com arquivo de padrões e arquivo de esquema relacionados.


### Estado

Decidido. Abertos a considerar novas capacidades à medida que surgirem.


## Detalhes


### Premissas

Preferimos separar o código da aplicação e o código do ambiente. Presumimos que o app precisa funcionar de maneira diferente em ambientes diferentes, como ambiente de desenvolvimento, ambiente de teste, ambiente de demonstração, ambiente de produção etc.

Preferimos a prática do setor “12 factor app” e ainda mais a prática relacionada “15 factor app”.

Muitos de nossos projetos anteriores usaram a convenção de um arquivo `.env` ou de um diretório `.env` similar. Há uma prática típica de manter esses arquivos fora do controle de versão e, em vez disso, usar alguma outra forma de implantá-los, versioná-los e gerenciá-los.


### Restrições

Queremos manter segredos fora do nosso sistema de controle de versão (VCS) de gerenciamento de código-fonte (SCM).

Queremos buscar compatibilidade com frameworks e bibliotecas de software populares. Por exemplo, o Node tem um módulo “dotenv” para ler a configuração por variáveis de ambiente.


### Posições

Consideramos algumas abordagens:

  * Armazenar a configuração no app, como em um arquivo `config.js`.

  * Armazenar a configuração no ambiente, como em um arquivo `.env`.

  * Buscar a configuração em um local conhecido, como um servidor de licenças.


### Argumento

Selecionamos a abordagem do arquivo .env porque:

  * É popular, inclusive entre especialistas.

  * Segue o padrão de arquivos `.env` que nossas equipes usaram com sucesso muitas vezes em muitos projetos.

  * É simples. Notavelmente, por ora aceitamos bem os trade-offs significativos que vemos, como a falta de capacidades de auditoria em comparação com a abordagem de um servidor de licenças.


### Implicações

Precisamos descobrir uma forma de separar a configuração por variáveis de ambiente que é pública do gerenciamento de segredos.


## Relacionado


### Decisões relacionadas

Esperamos que todas as nossas aplicações usem essa abordagem.

Planejaremos atualizar quaisquer de nossas aplicações que usem uma abordagem menos capaz, como valores fixos em um binário ou no código-fonte.

Manteremos como estão quaisquer de nossas aplicações que usem uma abordagem mais capaz, como um servidor de licenciamento.


### Requisitos relacionados

Adicionaremos capacidades de devops para os arquivos, incluindo hooks, testes e integração contínua.

Precisamos treinar todos os colegas desenvolvedores nesta decisão.



### Artefatos relacionados

Cada área em que implantamos precisará de seu próprio arquivo .env e arquivos relacionados.


### Princípios relacionados

Facilmente reversível.


## Notas


Exemplo de arquivo `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Exemplo de arquivo `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Exemplo de arquivo `.env.schema` somente com as chaves:

```env
NAME
EMAIL
```
