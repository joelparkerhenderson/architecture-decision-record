# Métricas, monitores, alertas

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
  * [Mensagens de texto livre versus mensagens de eventos estruturados](#mensagens-de-texto-livre-versus-mensagens-de-eventos-estruturados)
  * [O Graylog é mais fácil](#o-graylog-é-mais-fácil)
  * [O Prometheus exige algum ajuste](#o-prometheus-exige-algum-ajuste)
  * [Os serviços da AWS são variados](#os-serviços-da-aws-são-variados)
  * [Kafka](#kafka)
  * [Loki](#loki)
  * [Prometheus + alertmanager + Rollbar + Graylog + Grafana](#prometheus--alertmanager--rollbar--graylog--grafana)
  * [Thanos](#thanos)
  * [Prometheus HA](#prometheus-ha)
  * [Datadog + PagerDuty + Threat Stack](#datadog--pagerduty--threat-stack)
  * [Zabbix](#zabbix)
  * [Outlyer](#outlyer)
  * [Nagios + Nagiosgraph](#nagios--nagiosgraph)
  * [Prometheus + Grafana + AlertManager](#prometheus--grafana--alertmanager)
  * [DataDog + Sentry + PagerDuty.](#datadog--sentry--pagerduty)
  * [Sensu + Graphite + ELK](#sensu--graphite--elk)
  * [Prometheus + Alertmanager](#prometheus--alertmanager)
  * [Sensu + Grafana + Graylog + Kibana + NewRelic.](#sensu--grafana--graylog--kibana--newrelic)
  * [Prometheus + Circonus](#prometheus--circonus)
  * [icinga2 + VictorOps + NewRelic + Sentry + Slack](#icinga2--victorops--newrelic--sentry--slack)
  * [AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver](#appdynamics--papertrail--pagerduty--healthchecksio--stackdriver)
  * [icinga2 + elasticsearch](#icinga2--elasticsearch)
  * [DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps](#datadog--new-relic--elk--efk--sentry--alertmanager--victorops)
  * [Wavefront + Scalyr + PagerDuty + Stackstorm + Slack](#wavefront--scalyr--pagerduty--stackstorm--slack)
  * [Telegraf + Prometheus + InfluxDB + Grafana](#telegraf--prometheus--influxdb--grafana)
  * [Sematext + Logagent + Experience](#sematext--logagent--experience)
  * [Azure Monitor/Analytics + OpsGenie](#azure-monitoranalytics--opsgenie)
  * [Prometheus + Alertmanager + Grafana + Splunk + PagerDuty](#prometheus--alertmanager--grafana--splunk--pagerduty)
  * [Telegraf + Prometheus + Grafana + Alertmanager](#telegraf--prometheus--grafana--alertmanager)
  * [Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch](#prometheus--grafana--cloudwatch--sentry--kibana--elasticsearch)
  * [PagerDuty + Monitis](#pagerduty--monitis)
  * [Prometheus + Grafana + Bosun](#prometheus--grafana--bosun)
  * [Azure Monitor/Analytics/Insights/Dashboards](#azure-monitoranalyticsinsightsdashboards)
  * [Grafana + Monitis + OpsGenie + Slack](#grafana--monitis--opsgenie--slack)
  * [Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail](#checkly--appoptics--cloudwatch--heroku--pagerduty--papertrail)
  * [Instana + Logz.io + slack](#instana--logzio--slack)
  * [SignalFX + Splunk + PagerDuty + Slack](#signalfx--splunk--pagerduty--slack)
  * [ELK + Prometheus + Grafana](#elk--prometheus--grafana)
  * [Datadog + Prometheus + Grafana](#datadog--prometheus--grafana)
  * [Nagios + ELK](#nagios--elk)
  * [Datadog versus Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack](#datadog-versus-site24x7--statuscake--pagerduty--sumologic--slack)
  * [Prometheus + AlertManager + Grafana + Stackdriver](#prometheus--alertmanager--grafana--stackdriver)
  * [Zabbix](#zabbix-1)


## Resumo


### Questão

Queremos usar métricas, monitores e alertas, porque queremos saber o quão bem nossas aplicações estão funcionando e saber quando há um problema.


### Decisão

Em andamento (WIP).


### Estado

Coletando informações. Estamos começando pelos extremos plausíveis do espectro: a ferramenta gratuita mais antiga e mais recomendada (Nagios) e a ferramenta paga mais nova e mais recomendada (New Relic).


## Detalhes


### Premissas

Queremos criar apps web modernos, rápidos, confiáveis, responsivos etc.

Queremos comprar em vez de construir.


### Restrições

Queremos ferramentas que funcionem bem com o nosso pipeline de devops e com as nossas nuvens de implantação.


### Posições

Estamos pesquisando posições agora.


  * AlertManager

  * AppDynamics

  * AppOptics

  * Azure Monitor/Analytics/Insights/Dashboards

  * Bosun

  * Checkly

  * Circonus

  * Cloudwatch

  * EFK

  * ELK

  * Grafana

  * Grafana

  * Graphite

  * Graylog

  * Healthchecks.io

  * Heroku

  * icinga2

  * InfluxDB

  * Instana

  * Kafka

  * Logagent

  * Logz.io

  * Loki

  * Monitis

  * Nagios

  * Nagios

  * Nagiosgraph

  * NewRelic

  * OpsGenie

  * Outlyer

  * PagerDuty

  * Pagerduty

  * PagerDuty

  * Papertrail

  * Prometheus

  * Rollbar

  * Scalyr

  * Sematext Metrics, Logs, Experience, Tracing

  * Sensu

  * SignalFX

  * Slack

  * Splunk

  * Stackdriver

  * Stackstorm

  * Telegraf

  * Telegraf

  * Thanos

  * VictorOps

  * Wavefront

  * Zabbix

  
### Argumento

Até agora, Nagios e New Relic são os extremos do espectro. O Nagios é a ferramenta mais antiga, mais simples, gratuita e viável. O New Relic é a ferramenta mais nova em recursos, mais completa, paga e viável. Começaremos com avaliações dessas duas. Conforme necessário, migraremos para o meio do espectro.  

Até agora, o Zabbix tem as melhores recomendações e também oferece as capacidades mais completas.

Até agora, o ELK tem a melhor popularidade de “construir em vez de comprar” em código aberto.

Até agora, Prometheus + Grafana têm a melhor popularidade.


### Implicações

A fazer (TODO).


## Relacionado


### Decisões relacionadas

As escolhas afetarão a testabilidade, a telemetria e provavelmente outros sistemas, como os de atendimento ao cliente, engenharia de confiabilidade de sites etc.


### Requisitos relacionados

A fazer (TODO).


### Artefatos relacionados

A fazer (TODO).


### Princípios relacionados

Facilmente reversível.

Necessidade de velocidade.


## Notas


Uma pilha de código aberto razoavelmente boa é:

* Prometheus para métricas e alertas baseados em métricas

* Grafana para exibir métricas

* Elasticsearch/Logstash/Kibana (ELK) para logs e eventos estruturados

* Pushover para notificações móveis


### Mensagens de texto livre versus mensagens de eventos estruturados

Mensagens de texto livre: por exemplo, o tipo de coisa aleatória que você encontraria em /var/log/messages, e algo gerado intencionalmente pela aplicação. As mensagens são úteis para identificar outras coisas que estão acontecendo na máquina, como falta de memória ou erros de hardware, mas têm muito lixo. 

Mensagens de eventos estruturados: geradas pela aplicação, com um conjunto fixo ou dinâmico de atributos, p. ex., um log de requisições HTTP, um log contábil, um login de usuário.

De modo geral, é bom registrar em log os detalhes de cada requisição de uma forma que permita detalhar com base em atributos. Assim, adicionar, p. ex., um userid ou sessionid a tudo permite rastrear. O rastreamento explícito também é bom, claro. Usar o ELK para isso é meio que um https://www.honeycomb.io/ de pobre.


### O Graylog é mais fácil

O Graylog é mais fácil de subir, na minha experiência.



### O Prometheus exige algum ajuste


Em geral estou satisfeito com o Prometheus para métricas. O alerta exige algum ajuste, mas é bem bom. Depende da sua aplicação. Acho melhor alertar sobre condições visíveis ao usuário final, não sobre causas subjacentes. Por exemplo, o tempo de carregamento da página é bom, o número de requisições por segundo não. Embora zero requisições por segundo indique que algo está errado.

A vantagem de um serviço é que ele oferece inteligência adicional pronta para uso. Em geral eu gosto do Datadog. Os serviços podem ser assustadoramente caros se você tem muitos dados, e às vezes têm modelos de preços que não são amigáveis à nuvem, p. ex., cobrar por instância quando as instâncias são dinâmicas. Também há uma diferença entre serviços em que toda requisição vem de um usuário pagante e os relacionados a publicidade, em que apenas uma pequena porcentagem das requisições gera dinheiro. Você pode acabar com muitos dados e pouco orçamento.

Trabalho em alguns serviços que recebem 1 bilhão de requisições por dia, então faz sentido hospedar nosso próprio monitoramento e registro em log. Se seus volumes forem menores, então os serviços hospedados são mais fáceis.


### Os serviços da AWS são variados

Minha experiência com os serviços da AWS tem sido variada. O serviço Elasticsearch deles foi instável, então executamos nossas próprias instâncias para isso. As métricas do CloudWatch são caras, então geralmente as usamos apenas para métricas de nível de “infraestrutura” em vez da aplicação, ou seja, métricas relacionadas à saúde em que a AWS pode saber melhor o que está acontecendo do que o software rodando na instância. O CloudWatch Logs pode demorar para atualizar e não tem tantos metadados. Executar o ELK ajuda com isso. Se eu realmente quiser dados em tempo real, usar o Kafka como transporte para os logs é melhor. Isso é muito bem suportado pelo Logstash. Gerenciar um cluster Kafka, porém, não é para os fracos de coração, há muita tubulação exposta.


### Kafka

Comentário: o Kafka pode ser super complicado às vezes, ou pode ser sólido como uma rocha, a ponto de você quase esquecer que ele está lá amarrando tudo.


Comentário: o Kafka tem sido sólido, mas foi uma quantidade surpreendente de trabalho colocá-lo para funcionar. Penso nele como um banco de dados relacional, mas em que você trabalha apenas na camada “física”, p. ex., tablespaces, arquivos e partições. Houve momentos no início em que faltavam utilitários de gerenciamento e tivemos de escrever programas para, p. ex., redefinir um grupo de consumidores. http://howfuckedismydatabase.com/nosql/

Comentário: usamos o Kafka como um “buffer” para mensagens de log e um lugar onde podemos fazer processamento de fluxo em tempo real de dados vindos de vários servidores. Se sofrermos um ataque DDOS, precisamos de uma forma de analisar dados entre várias instâncias. Se estivermos registrando diretamente dos servidores para o ELK, a carga pode estourar o cluster Elasticsearch.

Comentário: o Kafka é bom para nós porque, se sofrermos um ataque DDOS, precisamos de uma forma de analisar dados entre várias instâncias. Se estivermos registrando diretamente dos servidores para o ELK, a carga pode estourar o cluster Elasticsearch.


Comentário: o Kafka faz menos trabalho e é mais eficiente, então consegue lidar melhor com a carga. E colocamos o trabalho do Kafka em fila e tentamos de novo. E ter o Kafka sobrecarregado não afeta os usuários que estão tentando trabalhar de forma interativa com o Kibana, como afetaria se o Elasticsearch estivesse com dificuldades.

Comentário: o processamento de fluxo busca principalmente abuso, p. ex., tráfego excessivo de um único IP em todo o cluster, e então compartilha o bloqueio com todo o cluster.

Comentário: o plugin logstash-output-kafka é bem pouco confiável no momento, no entanto. Fui atingido por vários dos problemas na página de issues dele no GitHub, que parecem nunca ser corrigidos. Quero deixar de usá-lo e enviar diretamente de nossos apps para o Kafka.

Comentário: agora estamos enviando eventos estruturados diretamente do app para o Kafka. A motivação principal foi tocar os dados de log menos vezes e evitar ler e gravar o disco várias vezes. Em sistemas de alto volume, o registro em log pode dar mais trabalho do que a própria aplicação. Estou pensando em fazer o journald também enviar logs diretamente, a partir de um programa em C.


### Loki

Fique de olho no Loki. Ele ainda não está pronto, mas, quando estiver, espero que se encaixe melhor nesta pilha. O Loki é um agregador de logs criado pela grafana labs; usa uma sintaxe de coleta e de tags semelhante à do Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager para métricas. Adoro o Prometheus.

Rollbar/Graylog para registro em log/relato de erros (há alguma sobreposição aqui; um serviço pequeno provavelmente não precisa dos dois).

Atualmente, os alertas vão apenas para um dos poucos canais do Slack em que as partes interessadas ativaram as notificações. Se estivéssemos mais sérios sobre plantão, iriam para PagerDuty/VictorOps/etc.

Grafana para gráficos e painéis. Também aguardo ansiosamente para ver se os recursos de registro em log que eles terão em breve dispensarão o Graylog.


### Thanos

Usamos o Thanos como front-end para a nossa configuração de HA. Ele sabe desduplicar pares de HA.

Atualmente mantemos 6 meses de dados locais do Prometheus. Isso funciona razoavelmente bem para nós. Mas estou no meio da implantação de armazenamento em bucket na nossa configuração do Thanos para armazenamento de dados de longo prazo. Em teoria, o armazenamento do GCS será cerca de 30% mais barato do que o disco persistente padrão do GCE que usamos agora.

Não fazemos backup dos dados do Prometheus agora. Os dados simplesmente não são muito importantes para nós além de ter o suficiente para alertas. A implantação da nossa frota geral muda tanto de um ano para o outro que dados históricos com mais de alguns meses simplesmente não são tão interessantes. Pode ser interessante ter algumas estatísticas centrais ano a ano; posso configurar um conjunto de regras de gravação de estatísticas centrais e armazená-las com Federação ou simplesmente deixar o Thanos cuidar disso.

EDIT: uma pequena ressalva, sou desenvolvedor do Prometheus.


### Prometheus HA

O HA no Prometheus é feito por duplicação: você executa vários coletores, e há maneiras de consultar vários e desduplicar os dados.

A escala é feita decidindo a rede e fazendo diferentes Prometheus consultarem diferentes partes da rede.

O armazenamento de longo prazo não é o ponto forte do Prometheus, mas é transferido para algo como influx ou timescaledb (que tecnicamente também marca o item de HA). Artigo que li sobre isso: https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Ainda não experimentei a parte de longo prazo, pois ainda estou só experimentando e usando para gráficos de curto prazo, enquanto o librenms monitora minha rede no longo prazo.


###  Datadog + PagerDuty + Threat Stack

Usamos o Datadog (com PagerDuty) e o Threat Stack e não poderíamos estar mais felizes. Minha única queixa do DD é o custo relativamente alto do armazenamento de métricas.


### Zabbix

Zabbix com scripts personalizados para monitorar quase tudo. Funciona às mil maravilhas.


### Outlyer

Estou usando o Outlyer, mas preciso ressalvar que trabalho aqui, e usar o nosso próprio produto é obrigatório.

Ainda preciso de Graylog, Sentry e Statuscake para complementar.

Pode soar tendencioso, mas, depois de ter executado com gosto o Nagios e outros sistemas de monitoramento internamente, eu compraria uma solução hospedada em qualquer emprego novo e me livraria dessa dor.


### Nagios + Nagiosgraph

Executamos o Nagios para todo o monitoramento e alertas. Os alertas acontecem por e-mail (avisos e notificações críticas) e por notificações sonoras do app (para alertas críticos).

O Nagiosgraph é usado para visualizações.

Essa configuração tem sido muito eficaz em nos manter amplamente informados sobre o que está acontecendo em nosso ambiente. Executamos e monitoramos cerca de 110 servidores críticos para a missão e cerca de 760 pontos de dados, e temos esse sistema matinal em vigor há mais de sete anos.

Gostaria de também agregar logs com o Graylog ou o ELK em algum momento.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager por meio do incrível helm chart do Prometheus Operator. Os logs ainda vão para o plano birch do LogDNA, pois percebemos que o ELK é pesado demais para o nosso humilde cluster de mín. 3, máx. 5 nós no GKE.


### DataDog + Sentry + PagerDuty.

Eu costumava executar todas as minhas próprias soluções de monitoramento usando todo tipo de software, incluindo Nagios, Icinga, Zabbix, ELK, Greylog2, Influx e muitas outras ferramentas, mas a verdade é que há esforço demais envolvido em executar a própria infraestrutura de monitoramento, especialmente quando você pode pagar a outra pessoa tarifas tão baixas para que ela faça isso por você!

Pagar a outros para executar a infraestrutura de monitoramento libera meus clientes para se concentrarem em executar suas plataformas em vez de monitorar o monitoramento, o que significa que o valor que obtêm da estabilidade de sua plataforma supera em muito quaisquer custos de Monitoramento como Serviço.


### Sensu + Graphite + ELK

Minha empresa é muito adepta de coisas auto-hospedadas.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager para alertas; minha equipe acredita que monitoramento simples é bom monitoramento.

Outros sistemas, como registro em log e rastreamento, fornecerão contexto rico para diagnóstico quando o plantonista receber um alerta, mas nunca construímos alertas sobre eles.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Serviços instrumentados com Prometheus => análise e visualização no Circonus


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Estamos usando os seguintes serviços:

icinga2 para monitoramento e VictorOps para alertas

NewRelic para monitoramento detalhado do serviço

Sentry para rastreamento de erros no serviço

Slack/e-mail fazem parte dos alertas, disparados a partir do NewRelic ou do icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 com integração com o elasticsearch para análise e integração com graphite+grafana para gráficos.

graças à flexibilidade das regras de aplicação no icinga2, os desenvolvedores só veem os serviços para os quais recebem notificações.

e por meio do icinga2 director, os programadores podem definir facilmente suas próprias verificações (o que fazem, a cada poucos dias - saem 100 verificações, entram outras 100) em larga escala, sem nenhum transtorno.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

O que temos agora:

DataDog para métricas

New Relic para monitoramento de aplicações

ELK (Elastic Search + Logstash + Kibana) para os logs

Sentry (auto-hospedado) para registrar exceções

E-mails + Slack + VictorOps para alertas (com base na gravidade)

O que queremos ter:

Prometheus para métricas (Grafana para visualização)

New Relic (provavelmente Elastic Search APM) para o monitoramento de aplicações

EFK (elastic search + fluentd + kibana) para registro em log. Provavelmente, o Loki da Grafana estará pronto para produção até o momento em que chegarmos lá

Sentry para as exceções

Alertmanager + e-mail + VictorOps para os alertas


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (ressalva: trabalho na VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf para métricas de servidor, como CPU, disco, memória e rede. Também usamos o Telegraf para monitoramento SNMP de nossos dispositivos de rede.

Prometheus para métricas de aplicação. Codificamos verificações de saúde em nossa aplicação que o Prometheus coleta.

InfluxDB para armazenamento de séries temporais. É para onde os dados do Telegraf são enviados.

Grafana para painéis e alertas. O mecanismo de alertas não é super robusto, mas dá conta do recado. Também disparamos alertas no Slack.

O que não tenho agora é uma solução de registro em log centralizada. O ELK é poderoso, mas difícil de configurar e gerenciar, e não conheço alternativas gratuitas que se aproximem o bastante para investigar.


### Sematext + Logagent + Experience

Sematext para métricas, para logs, para traces e, em breve, também para monitoramento de usuários reais. Mais simples/mais barato do que usar N ferramentas/serviços diferentes, na minha humilde opinião.

Para o envio de logs, costumávamos usar o rsyslog e depois passamos para o Logagent.

Para o relato de falhas de front-end usamos o Sentry, mas em breve migraremos para o Experience.

Ressalva: sou um Sematextan.


### Azure Monitor/Analytics + OpsGenie

Gostaria que o Log Analytics tivesse uma interface melhor. Estamos nos afastando do splunk, que era muito mais fácil de navegar.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Você realmente não quer executar seu próprio sistema de notificação. Você pode substituir o Splunk pelo ELK, a menos que sua equipe de segurança prefira o Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf como coletor, Prometheus + Alertmanager para monitoramento e alertas, integrados a canais do slack e ao pagerduty para alertas críticos. Grafana para visualização de métricas dos hosts.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus para métricas + alertas

Grafana para painéis do Prometheus

Cloudwatch monitorando as instâncias do Prometheus

sentry para rastreamento de exceções

kibana + elasticsearch

graylog

prometheus Push Gateway para lotes/cronjobs

SOP https://github.com/rapidloop/sop para “enviar/encaminhar” métricas de uma instância do Prometheus para outra

os clientes usam os clientes do Prometheus. Tentamos usar o opencensus.io no lado do cliente


### PagerDuty + Monitis

PagerDuty + Monitis. Também algumas Azure Functions sob medida para testar a saúde de alguns serviços.

Procurando introduzir o Prometheus e o Grafana este ano


### Prometheus + Grafana + Bosun

Prometheus para armazenar os dados de séries temporais. Grafana para visualização. Bosun para gerenciamento de alertas.


### Azure Monitor/Analytics/Insights/Dashboards

Loja somente Azure: Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana para monitorar serviços de contêineres no Kubernetes via Prometheus

Monitis para monitoramento de serviços de ponta a ponta, principalmente para APIs web e aplicações web

OpsGenie para gerenciamento de alertas

Slack para receber informações de status dos nossos sistemas


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Engenheiro (dev)ops de longa data aqui. Cresci com o Nagios. Adoraria ter opiniões sobre o meu SaaS autofinanciado https://checklyhq.com. Fazemos monitoramento de APIs e monitoramento de transações de sites com alertas bem detalhados.

Comecei o Checkly porque o monitoramento ativo / sintético no espaço de APIs era um pouco limitado (e caro). O monitoramento baseado em navegador / com scripts é ainda mais proprietário e caro. Usamos o Puppeteer e mantemos os preços o mais baixo possível.

Nossa pilha de monitoramento:

Checkly (comendo a nossa própria comida...)

AppOptics (gráficos personalizados)

AWS Cloudwatch e SNS para mensagens SMS.

alertas integrados do Heroku.

Pagerduty

Papertrail


### Instana + Logz.io + slack

O Instana nos alerta no slack sobre problemas de infraestrutura ou degradação de desempenho, e configuramos o logz.io para alertar no slack sobre um certo volume de logs de nível de erro da camada de aplicação.


### SignalFX + Splunk + PagerDuty + Slack

Atualmente usando: SignalFX, Splunk, PagerDuty e Slack. Não sou grande fã do SignalFX, embora a equipe de suporte deles seja super amigável e responsiva. Gosto do Splunk (vale a pena se você puder pagar), do PagerDuty e do Slack.

Eu costumava usar a pilha TICK, em que o C era na verdade um G, ou seja, Grafana, embora eu tenha usado um pouco o Chronograf. Era incrível, mas era um sofrimento de gerenciar. O clássico dilema SaaS versus auto-hospedagem.

Usei DataDog, New Relic, Graylog, ELK e BugSnag. Gosto muito do DataDog e do New Relic, o Graylog é bem bom. Não sou grande fã do ELK. O BugSnag é legal; na verdade, sinto que rastrear erros/exceções é um bom substituto para o monitoramento completo de logs em muitos casos.


### ELK + Prometheus + Grafana

Assim como outros, usamos o ELK para logs e Prometheus+Grafana para todo o resto.

Manter essa configuração é fácil se você se der permissão para perder dados ocasionalmente. Por exemplo, se o nosso banco de dados ElasticSearch entrar numa pane (o que acontece a cada 2-3 meses para nós, infelizmente), não nos preocupamos com HA; em vez disso, descartamos os dados e seguimos com nossas vidas. Se você realmente precisa de HA ou retenção de longo prazo, boa sorte.


### Datadog + Prometheus + Grafana

Configurei o Datadog mês a mês porque, quando cheguei aqui, não havia monitoramento nem alertas. Apenas alguns de nossos sites eram monitorados a cada 5 min quanto à disponibilidade. O Datadog é, sem dúvida, o mais fácil de configurar. Quando eu terminar de resolver todos os outros problemas, mudarei para Prometheus+Grafana. Ainda não estou 100% decidido sobre o gerenciamento de logs.

### Nagios + ELK

Temos mais de 100 produtos que damos suporte.

Para on-prem, é principalmente Nagios e ELK. Para a nuvem, estamos migrando do DataDog para o NewRelic.


### Datadog versus Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Costumávamos usar o datadog, mas o achamos caro demais para as nossas necessidades. Não me entenda mal, ele é incrível, mas tem um custo enorme. Conseguimos configurar o site24x7.com com uma assinatura anual por cerca de 2-3 meses do custo do DD.

Nossa pilha de monitoramento:

Site24x7 - APM, monitoramento de URLs externas, monitoramento de fluxo de e-mail SMTP, expiração de ssl e monitoramento de processos.

StatusCake - para monitoramento e confirmação de URLs - é o nosso backup, caso o site24x7 deixe passar algo (não deixa), mas o SC é mais flexível para o monitoramento de portas e serviços externos para as nossas necessidades.

Ambas as ferramentas escalonam para o PagerDuty, e então recebemos nossos escalonamentos no slack.

SumoLogic - para monitoramento de logs (é uma ótima ferramenta, mas um pouco complicada para as nossas necessidades)

Do slack podemos reconhecer (ack) ou remediar o alerta.

Temos então muitas automações do site24x7 que se conectam ao commando.io para o que chamamos de ‘BedOps’ - em que, quando um alerta é disparado, executamos alguns scripts ou automações na tentativa de remediar a situação (em 99% das vezes a automação + nossos scripts nos mantêm fora de problemas).

Temos runbooks internos em nossa KB para quando as automações falham ou quando há algo fora do escopo que precisa ser corrigido.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana para métricas em nossos clusters GKE e VMs.

Google Stackdriver para logs (pois já está incluído e ativo por padrão e atualmente é suficiente para as nossas necessidades).


### Zabbix

Zabbix para tudo. Nenhum software adicional necessário.
