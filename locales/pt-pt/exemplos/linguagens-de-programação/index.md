# Linguagens de programação

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

Precisamos escolher linguagens de programação para o nosso software. Temos duas grandes necessidades: uma linguagem de programação de front-end adequada para aplicações web e uma linguagem de programação de back-end adequada para aplicações de servidor.


### Decisão

Estamos escolhendo TypeScript para o front-end.

Estamos escolhendo Rust para o back-end.


### Estado

Decidido. Estamos abertos a novas alternativas à medida que surgirem.


## Detalhes


### Premissas

As aplicações de front-end são típicas:

  * Usuários e interações típicos

  * Navegadores e sistemas típicos

  * Desenvolvimentos e implantações típicos

É provável que as aplicações de front-end evoluam rapidamente:

  * Queremos garantir desenvolvimentos, implantações, iterações etc. rápidos e fáceis.

  * Valorizamos a comprovabilidade, como a segurança de tipos, e aceitamos fazer um pouco mais de trabalho para alcançá-la.

  * Não precisamos de compatibilidade com sistemas legados.

As aplicações de back-end estão acima do típico:

  * Metas de qualidade acima do típico, especialmente comprovabilidade, confiabilidade, segurança etc.

  * Metas de quase tempo real acima do típico, ou seja, não queremos pausas devido à coleta de lixo da máquina virtual.

  * Metas de programação funcional acima do típico, especialmente para paralelização, processamento multinúcleo e segurança de memória.

Aceitamos velocidades de compilação menores em favor da segurança em tempo de compilação e das velocidades de execução.


### Restrições

Temos uma forte restrição quanto às linguagens que são utilizáveis com os serviços de funções dos principais provedores de nuvem, como o Amazon Lambda.


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

  * C: rejeitada por causa da baixa segurança; o Rust consegue fazer quase tudo melhor.

  * C++: rejeitada porque é uma bagunça; o Rust consegue fazer quase tudo melhor.

  * Clojure: excelente modelagem; melhor aproximação de Lisp; ótimo ambiente de execução na JVM.
  
  * Elixir: excelente ambiente de execução, incluindo capacidade de implantação e concorrência; excelente experiência do desenvolvedor; ecossistema relativamente pequeno.

  * Erlang: excelente ambiente de execução, incluindo capacidade de implantação e concorrência; experiência do desenvolvedor desafiadora; ecossistema relativamente pequeno.

  * Elm: parece muito promissora; a IBM está publicando grandes estudos de caso com bons resultados; ecossistema menor.

  * Flow: melhoria interessante em relação ao JavaScript; no entanto, os desenvolvedores estão se afastando dela.

  * Go: excelente experiência do desenvolvedor; excelente concorrência; mas com um histórico de más decisões que prejudicam a linguagem.

  * Haskell: melhor linguagem funcional; comunidade de desenvolvedores menor; não alcançou sucessos de produção publicados suficientes.

  * Java: excelente ambiente de execução; excelente ecossistema; experiência do desenvolvedor abaixo da média.

  * JavaScript: a linguagem mais popular de todos os tempos; ecossistema mais difundido.

  * Kotlin: corrige muita coisa do Java; excelente apoio da JetBrains; bons casos publicados de migração do Java para o Kotlin.
  
  * Python: linguagem mais popular para administração de sistemas; ótimas ferramentas de análise; bons frameworks web; mas abandonada pelo Google em favor do Go.

  * Ruby: melhor experiência do desenvolvedor de todos os tempos; melhores frameworks web; comunidade mais simpática; mas muito lenta; um tanto difícil de empacotar.

  * Rust: melhor linguagem nova; ênfase em abstração zero; ênfase em concorrência; no entanto, ecossistema relativamente pequeno; e tem limites deliberados em alguns tipos de aceleração do compilador, p. ex., o acesso direto à memória precisa ser explicitamente inseguro (unsafe).

  * TypeScript: adiciona tipos ao JavaScript; ótimo transpilador; ênfase crescente dos desenvolvedores na migração do JavaScript para o TypeScript; forte apoio da Microsoft.

Decidimos que as VMs têm um conjunto de trade-offs de que não precisamos agora, como a complexidade adicional que fornece capacidades em tempo de execução.

Acreditamos que nossa decisão central é impulsionada por duas preocupações transversais:

  * Para a maior velocidade de execução e o acesso mais estreito ao sistema, escolheríamos JavaScript e C.

  * Para uma velocidade de execução próxima da maior e um acesso ao sistema próximo do mais estreito, escolhemos TypeScript e Rust.

Menções honrosas vão para as linguagens de VM e os frameworks web que escolheríamos se quiséssemos uma linguagem de VM:

  * Clojure e Luminus

  * Java e Spring

  * Elixir e Phoenix


### Implicações

Os desenvolvedores de front-end precisarão aprender TypeScript. Essa provavelmente é uma curva de aprendizado fácil se a experiência principal do desenvolvedor for com JavaScript.

Os desenvolvedores de back-end precisarão aprender Rust. Essa provavelmente é uma curva de aprendizado moderada se a experiência principal do desenvolvedor for com C/C++, e uma curva de aprendizado difícil se a experiência principal do desenvolvedor for com Java, Python, Ruby ou linguagens semelhantes com gerenciamento automático de memória. 

TypeScript e Rust são ambas relativamente novas. Isso significa que muitas ferramentas ainda não têm documentação para essas linguagens. Por exemplo, o pipeline de devops precisará ser configurado para essas linguagens e, até agora, nenhuma das ferramentas de devops que estamos avaliando tem exemplos padrão para elas.

Os tempos de compilação de TypeScript e Rust são bastante lentos. Parte disso pode se dever à novidade das linguagens. Podemos querer examinar como atenuar tempos de compilação lentos, como por compilação sob demanda, concorrência de compilação etc.

O suporte de IDE para essas linguagens ainda não é onipresente nem de primeira classe. Por exemplo, a JetBrains vende a IDE PyCharm com suporte de primeira classe ao Python, mas não vende uma IDE com suporte de primeira classe ao Rust; em vez disso, a JetBrains pode usar um plugin de Rust que fornece talvez 80% do suporte à linguagem Rust em relação ao suporte à linguagem Python.


## Relacionado


### Decisões relacionadas

Buscaremos escolhas de ecossistema que se alinhem a essas linguagens.

Por exemplo, queremos escolher uma IDE que tenha boas capacidades para essas linguagens.

Por exemplo, para o nosso framework web de front-end, é mais provável que decidamos por um framework que tende a mirar o TypeScript (p. ex., Vue) do que por um que tende a mirar o JavaScript puro (p. ex., React).


### Requisitos relacionados

Toda a nossa cadeia de ferramentas deve dar suporte a essas linguagens.


### Artefatos relacionados

Esperamos que possamos exportar alguns segredos para variáveis de ambiente.


### Princípios relacionados

Meça duas vezes, construa uma. Estamos priorizando alguma segurança em detrimento de alguma velocidade.

O tempo de execução é mais valioso do que o tempo de compilação. Estamos priorizando o uso pelo cliente em detrimento do uso pelo desenvolvedor.


## Notas

Quaisquer notas aqui.
