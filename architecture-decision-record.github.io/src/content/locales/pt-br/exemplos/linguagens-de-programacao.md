# Linguagens de programação

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

Precisamos escolher linguagens de programação para nosso software. Temos duas necessidades principais: uma linguagem de programação front-end adequada para aplicações web e uma linguagem de programação back-end adequada para aplicações de servidor.


### Decisão

Estamos escolhendo TypeScript para o front-end.

Estamos escolhendo Rust para o back-end.


### Status

Decidido. Estamos abertos a novas alternativas conforme elas surgirem.


## Detalhes


### Premissas

As aplicações front-end são típicas:

  * Usuários e interações típicos

  * Navegadores e sistemas típicos

  * Desenvolvimentos e implantações típicos

As aplicações front-end provavelmente evoluirão rapidamente:

  * Queremos garantir desenvolvimentos, implantações, iterações etc. rápidos e fáceis.

  * Valorizamos comprovabilidade, como segurança de tipos, e estamos confortáveis fazendo um pouco mais de trabalho para alcançá-la.

  * Não precisamos de compatibilidade legada.

As aplicações back-end são acima do típico:

  * Objetivos acima do típico para qualidade, especialmente comprovabilidade, confiabilidade, segurança etc.

  * Objetivos acima do típico para quase tempo real, ou seja, não queremos pausas devido à coleta de lixo de máquinas virtuais.

  * Objetivos acima do típico para programação funcional, especialmente para paralelização, processamento multi-core e segurança de memória.

Aceitamos velocidades menores de tempo de compilação em favor de segurança em tempo de compilação e velocidades em runtime.


### Restrições

Temos uma restrição forte quanto a linguagens que sejam utilizáveis com serviços dos principais provedores de cloud para funções, como Amazon Lambda.


### Posições

Consideramos estas linguagens:

  * C

  * C++

  * Clojure

  * Elixir

  * Erlang

  * Elm

  * Flow

  * Go

  * Haskell

  * Java

  * JavaScript

  * Kotlin

  * Python

  * Ruby

  * Rust

  * TypeScript



### Argumento

Resumo por linguagem:

  * C: rejeitada por baixa segurança; Rust consegue fazer quase tudo melhor.

  * C++: rejeitada porque é uma bagunça; Rust consegue fazer quase tudo melhor.

  * Clojure: excelente modelagem; melhor aproximação de Lisp; ótimo runtime na JVM.

  * Elixir: excelente runtime, incluindo implantabilidade e concorrência; excelente experiência de desenvolvimento; ecossistema relativamente pequeno.

  * Erlang: excelente runtime, incluindo implantabilidade e concorrência; experiência de desenvolvimento desafiadora; ecossistema relativamente pequeno.

  * Elm: parece muito promissora; a IBM está publicando grandes estudos de caso com bons resultados; ecossistema menor.

  * Flow: melhoria interessante sobre JavaScript; entretanto, desenvolvedores estão se afastando dela.

  * Go: excelente experiência de desenvolvimento; excelente concorrência; mas um histórico de decisões ruins que limitam a linguagem.

  * Haskell: melhor linguagem funcional; comunidade de desenvolvedores menor; não alcançou sucessos publicados de produção em quantidade suficiente.

  * Java: excelente runtime; excelente ecossistema; experiência de desenvolvimento abaixo da média.

  * JavaScript: linguagem mais popular de todos os tempos; ecossistema mais difundido.

  * Kotlin: corrige muita coisa do Java; excelente apoio da JetBrains; bons casos publicados de migração de Java para Kotlin.

  * Python: linguagem mais popular para administração de sistemas; ótimas ferramentas de analytics; bons frameworks web; mas abandonada pelo Google em favor de Go.

  * Ruby: melhor experiência de desenvolvimento de todas; melhores frameworks web; comunidade mais agradável; mas muito lenta; um pouco difícil de empacotar.

  * Rust: melhor nova linguagem; ênfase em abstração zero; ênfase em concorrência; entretanto, ecossistema relativamente pequeno; e tem limites deliberados para alguns tipos de aceleração do compilador, por exemplo acesso direto à memória precisa ser explicitamente unsafe.

  * TypeScript: adiciona tipos ao JavaScript; ótimo transpilador; ênfase crescente de desenvolvedores em migrar de JavaScript para TypeScript; forte apoio da Microsoft.

Decidimos que VMs têm um conjunto de trade-offs de que não precisamos agora, como complexidade adicional que fornece capacidades de runtime.

Acreditamos que nossa decisão central é direcionada por duas preocupações transversais:

  * Para a maior velocidade de runtime e o acesso mais direto ao sistema, escolheríamos JavaScript e C.

  * Para velocidade de runtime próxima da maior e acesso ao sistema próximo do mais direto, escolhemos TypeScript e Rust.

Menções honrosas vão para as linguagens de VM e frameworks web que escolheríamos se quiséssemos uma linguagem de VM:

  * Clojure e Luminus

  * Java e Spring

  * Elixir e Phoenix


### Implicações

Desenvolvedores front-end precisarão aprender TypeScript. Esta provavelmente é uma curva de aprendizado fácil se a experiência principal do desenvolvedor for usar JavaScript.

Desenvolvedores back-end precisarão aprender Rust. Esta provavelmente é uma curva de aprendizado moderada se a experiência principal do desenvolvedor for usar C/C++, e uma curva de aprendizado difícil se a experiência principal do desenvolvedor for usar Java, Python, Ruby ou linguagens semelhantes com gerenciamento de memória.

TypeScript e Rust são ambas relativamente novas. Isso significa que muitas ferramentas ainda não têm documentação para essas linguagens. Por exemplo, o pipeline de devops precisará ser configurado para essas linguagens, e até agora nenhuma das ferramentas de devops que estamos avaliando tem exemplos padrão para essas linguagens.

Tempos de compilação para TypeScript e Rust são bastante lentos. Parte disso pode decorrer da novidade das linguagens. Talvez queiramos analisar como mitigar tempos de compilação lentos, como por compile-on-demand, concorrência de compilação etc.

Suporte de IDE para essas linguagens ainda não é ubíquo nem de primeira classe. Por exemplo, a JetBrains vende a IDE PyCharm para suporte de primeira classe a Python, mas não vende uma IDE com suporte de primeira classe a Rust; em vez disso, a JetBrains pode usar um plug-in de Rust que fornece talvez 80% do suporte à linguagem Rust em comparação com o suporte à linguagem Python.


## Relacionado


### Decisões relacionadas

Miraremos escolhas de ecossistema que se alinhem a essas linguagens.

Por exemplo, queremos escolher uma IDE que tenha boas capacidades para essas linguagens.

Por exemplo, para nosso framework web front-end, é mais provável decidirmos por um framework que tenda a mirar TypeScript (por exemplo, Vue) do que por um framework que tenda a mirar JavaScript puro (por exemplo, React).


### Requisitos relacionados

Toda a nossa toolchain deve dar suporte a essas linguagens.


### Artefatos relacionados

Esperamos talvez exportar alguns segredos para variáveis de ambiente.


### Princípios relacionados

Meça duas vezes, construa uma vez. Estamos priorizando alguma segurança sobre alguma velocidade.

Runtime é mais valioso que tempo de compilação. Estamos priorizando o uso pelo cliente sobre o uso pelo desenvolvedor.


## Notas

Quaisquer notas aqui.
