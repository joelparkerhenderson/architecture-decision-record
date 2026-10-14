# Formato de timestamp

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

Queremos conseguir rastrear quando as coisas acontecem usando timestamps e usando um formato de timestamp consistente que funcione bem em todos os nossos sistemas e sistemas de terceiros.

Interagimos com sistemas que têm formatos de timestamp diferentes:

* Mensagens JSON não têm um formato nativo de timestamp, então precisamos escolher como converter um timestamp em string e converter uma string em timestamp, ou seja, como serializar/desserializar.

* Algumas aplicações estão configuradas para usar horário local em vez de horário UTC. Isso pode ser conveniente para projetos que precisam se ajustar ao horário local, como projetos que disparam eventos baseados no horário local.

* Alguns sistemas têm diferentes necessidades e capacidades de precisão de tempo, como usar resolução de tempo de segundos vs. milissegundos vs. nanossegundos. Por exemplo, o comando `date` do sistema operacional Linux usa uma precisão padrão de segundos, enquanto a bolsa Nasdaq quer uma precisão padrão de nanossegundos.


### Decisão

Escolhemos o formato padrão de timestamp ISO 8601 com precisão de nanossegundos, especificamente "YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ".

O formato mostra ano, mês, dia, hora, minuto, segundo, nanossegundos e fuso horário Zulu, também conhecido como UTC, GMT.


### Status

Decidido.


## Detalhes


### Premissas

Precisamos lidar com estas strings de texto de timestamp, para converter de um timestamp para uma string (também conhecido como serializar) e converter de uma string para um timestamp (também conhecido como desserializar).

Queremos um formato que seja geralmente fácil de usar, fácil de converter e fácil para uma pessoa ler.

Queremos compatibilidade com uma ampla variedade de sistemas externos que não controlamos, como sistemas de analytics, sistemas de banco de dados e sistemas financeiros.


### Restrições

Alguns sistemas têm limitações de precisão de tempo. Por exemplo, o comando `date` do sistema operacional macOS consegue imprimir precisão de tempo em segundos, mas não em nanossegundos.


### Posições

Consideramos uma variedade de opções:

* Unix epoch, ou seja, um número incremental.

* Formato textual sucinto "YYYYMMDDTHHMMSSNNNNNNNNN".

* Usar um fuso horário local vs. o fuso horário UTC.


### Argumento

Para uso típico, valorizamos facilidade de leitura/escrita por humanos mais do que velocidade/tamanho brutos.

Para uso típico, queremos um formato que funcione bem em sistemas de máquina e também funcione bem manualmente, como escrever dados de exemplo, ler saída JSON, usar grep em um arquivo de log etc.

Para uso atípico, como computação de alta performance, esperamos querer otimizar qualquer formato textual escolhido convertendo o texto para um formato mais rápido, como o tipo de objeto de data embutido de uma linguagem de programação. Portanto, o formato textual não importa muito para HPC.


### Implicações

Nossos vários sistemas de texto e sistemas de tempo convergirão para este formato.


## Relacionado


### Decisões relacionadas

Talvez queiramos uma forma rápida/fácil de também rastrear deltas de tempo, também conhecidos como durações. Isso é fácil com timestamps Unix epoch.


### Requisitos relacionados

Talvez queiramos ajustar nossa decisão, por exemplo, se tivermos um requisito relacionado para um tipo específico de carimbo de mensagem de logging, como para Splunk, Sumo, ELK etc.


### Artefatos relacionados

Formatadores e parsers de linguagens:

  * [date-fns: biblioteca moderna utilitária de data para JavaScript](https://date-fns.org/)
  * [Crono: biblioteca de data e hora para Rust](https://github.com/chronotope/chron)

Exemplos da Rosetta Code:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Exemplos SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Princípios relacionados

Facilmente reversível. Podemos mudar com bastante facilidade para um formato diferente, como Unix epoch.

Adie otimização prematura. Para uso típico, não nos importamos muito com alguns caracteres extras, como um formato que usa hifens e dois-pontos.


## Notas

Adicione notas aqui.
