# Configuração por variáveis de ambiente

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
  * [Implicações ](#implicações)
* [Relacionado](#relacionado)
  * [Decisões relacionadas](#decisões-relacionadas)
  * [Requisitos relacionados](#requisitos-relacionados)
  * [Artefatos relacionados](#artefatos-relacionados)
  * [Princípios relacionados](#princípios-relacionados)
* [Notas](#notas)


## Resumo


### Questão

Queremos que nossas aplicações sejam configuráveis para além de artefatos/binários/código-fonte, de modo que um build possa se comportar de forma diferente dependendo de seu ambiente de implantação.

  * Para realizar isso, queremos usar configuração por variáveis de ambiente.

  * Queremos gerenciar a configuração usando arquivos que possamos controlar por versão.

  * Queremos fornecer alguma ergonomia de experiência do desenvolvedor, como saber o que pode ser configurado e quaisquer padrões relevantes.


### Decisão

Decidido por arquivos .env com arquivo de padrões e arquivo de esquema relacionados.


### Status

Decidido. Aberto a considerar novas capacidades conforme surgirem.


## Detalhes


### Premissas

Favorecemos separar o código da aplicação e o código de ambiente. Assumimos que o app precisa funcionar de modo diferente em diferentes ambientes, como em um ambiente de desenvolvimento, ambiente de teste, ambiente de demo, ambiente de produção etc.

Favorecemos a prática da indústria de "12 factor app" e ainda mais a prática relacionada de "15 factor app".

Muitos dos nossos projetos anteriores usaram a convenção de um arquivo `.env` ou diretório `.env` semelhante. Há uma prática típica de mantê-los fora do controle de versão e, em vez disso, usar alguma outra forma de implantá-los, versioná-los e gerenciá-los.


### Restrições

Queremos manter segredos fora do nosso sistema de gerenciamento de código-fonte (SCM) e sistema de controle de versão (VCS).

Queremos buscar compatibilidade com frameworks e bibliotecas de software populares. Por exemplo, Node tem um módulo "dotenv" para ler configuração por variáveis de ambiente.


### Posições

Consideramos algumas abordagens:

  * Armazenar configuração no app, como em um arquivo `config.js`.

  * Armazenar configuração no ambiente, como em um arquivo `.env`.

  * Buscar configuração de um local conhecido, como um servidor de licenças.


### Argumento

Selecionamos a abordagem de um arquivo .env porque:

  * Ela é popular, inclusive entre especialistas.

  * Ela segue o padrão de arquivos `.env`, que nossas equipes usaram com sucesso muitas vezes em muitos projetos.

  * Ela é simples. Notavelmente,  Por enquanto estamos bem com os trade-offs significativos que vemos, como a falta de capacidades de auditoria em comparação com uma abordagem de servidor de licenças.


### Implicações

Precisamos descobrir uma forma de separar configuração por variáveis de ambiente que é pública de qualquer gerenciamento de segredos.


## Relacionado


### Decisões relacionadas

Esperamos que todas as nossas aplicações usem esta abordagem.

Planejaremos atualizar quaisquer das nossas aplicações que usem uma abordagem menos capaz, como hardcoding em um binário ou em código-fonte.

Manteremos como estão quaisquer das nossas aplicações que usem uma abordagem mais capaz, como um servidor de licenciamento.


### Requisitos relacionados

Adicionaremos capacidades de devops para os arquivos, incluindo hooks, testes e integração contínua.

Precisamos treinar todos os colegas desenvolvedores nesta decisão.



### Artefatos relacionados

Cada área em que implantamos precisará de seu próprio arquivo .env e arquivos relacionados.


### Princípios relacionados

Facilmente reversível.


## Notas


Arquivo de exemplo `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Arquivo de exemplo `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Arquivo de exemplo `.env.schema` apenas com as chaves:

```env
NAME
EMAIL
```
