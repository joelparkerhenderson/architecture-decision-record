# Formato de carimbo de data e hora

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

Queremos poder acompanhar quando as coisas acontecem usando carimbos de data e hora e um formato de carimbo consistente que funcione bem em todos os nossos sistemas e em sistemas de terceiros.

Interagimos com sistemas que têm formatos de carimbo de data e hora diferentes:

* As mensagens JSON não têm um formato de carimbo de data e hora nativo, então precisamos escolher como converter um carimbo de data e hora em string e uma string em carimbo de data e hora, ou seja, como serializar/desserializar.

* Algumas aplicações são configuradas para usar a hora local, em vez da hora UTC. Isso pode ser conveniente para projetos que precisam se ajustar à hora local, como projetos que disparam eventos baseados na hora local.

* Alguns sistemas têm necessidades e capacidades de precisão de tempo diferentes, como usar resolução de tempo em segundos, milissegundos ou nanossegundos. Por exemplo, o comando `date` do sistema operacional Linux usa uma precisão de tempo padrão de segundos, enquanto a bolsa de valores Nasdaq quer uma precisão de tempo padrão de nanossegundos.


### Decisão

Escolhemos o formato padrão de carimbo de data e hora ISO 8601 com precisão de nanossegundos, especificamente "YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ".

O formato mostra o ano, mês, dia, hora, minuto, segundo, nanossegundos e o fuso horário Zulu, também conhecido como UTC, GMT.


### Estado

Decidido.


## Detalhes


### Premissas

Precisamos lidar com essas strings de texto de carimbo de data e hora, para converter de um carimbo para uma string (também conhecido como serializar) e converter de uma string para um carimbo (também conhecido como desserializar).

Queremos um formato que seja em geral fácil de usar, fácil de converter e fácil de ser lido por uma pessoa.

Queremos compatibilidade com uma ampla gama de sistemas externos que não controlamos, como sistemas de análise, sistemas de banco de dados e sistemas financeiros.


### Restrições

Alguns sistemas têm limitações de precisão de tempo. Por exemplo, o comando `date` do sistema operacional macOS pode imprimir a precisão de tempo em segundos, mas não em nanossegundos.


### Posições

Consideramos uma gama de opções:

* Época Unix (Unix epoch), ou seja, um número crescente.

* Formato de texto conciso "YYYYMMDDTHHMMSSNNNNNNNNN".

* Usar um fuso horário local versus o fuso horário UTC.


### Argumento

Para uso típico, valorizamos a facilidade de leitura/escrita por humanos mais do que a velocidade/tamanho brutos.

Para uso típico, queremos um formato que funcione bem em sistemas de máquina e também funcione bem manualmente, como ao escrever dados de exemplo, ler saída JSON, procurar com grep em um arquivo de log etc.

Para uso atípico, como computação de alto desempenho, esperamos que queiramos otimizar qualquer formato de texto que escolhermos, convertendo o texto em um formato mais rápido, como o tipo de objeto de data nativo de uma linguagem de programação. Assim, o formato de texto não importa muito para HPC.


### Implicações

Nossos vários sistemas de texto e sistemas de tempo convergirão para este formato.


## Relacionado


### Decisões relacionadas

Podemos querer uma forma rápida/fácil de também acompanhar deltas de tempo, também conhecidos como durações. Isso é fácil com carimbos de data e hora de época Unix.


### Requisitos relacionados

Podemos querer ajustar nossa decisão, p. ex., se tivermos um requisito relacionado a um tipo específico de carimbo de mensagem de log, como para Splunk, Sumo, ELK etc.


### Artefatos relacionados

Formatadores e analisadores de linguagens:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Exemplos do Rosetta Code:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Exemplos da SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Princípios relacionados

Facilmente reversível. Podemos mudar com bastante facilidade para um formato diferente, como a época Unix.

Adie a otimização prematura. Para uso típico, não nos importamos muito com um punhado de caracteres extras, como num formato que usa hifens e dois-pontos.


## Notas

Adicione notas aqui.
