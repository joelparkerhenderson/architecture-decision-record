# Métricas, monitores, alertas

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
  * [Mensagens de texto livre vs mensagens de evento estruturadas](#mensagens-de-texto-livre-vs-mensagens-de-evento-estruturadas)
  * [Graylog é mais fácil](#graylog-é-mais-fácil)
  * [Prometheus exige algum ajuste](#prometheus-exige-algum-ajuste)
  * [Serviços AWS são mistos](#serviços-aws-são-mistos)
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
  * [Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack](#datadog-vs-site24x7--statuscake--pagerduty--sumologic--slack)
  * [Prometheus + AlertManager + Grafana + Stackdriver](#prometheus--alertmanager--grafana--stackdriver)
  * [Zabbix](#zabbix)


## Resumo


### Questão

Queremos usar métricas, monitores e alertas, porque queremos saber quão bem nossas aplicações estão funcionando e saber quando há um problema.


### Decisão

WIP.


### Status

Coletando informações. Estamos começando pelas extremidades plausíveis do espectro: a ferramenta gratuita antiga mais recomendada (Nagios) e a ferramenta paga mais nova mais recomendada (New Relic).


## Detalhes


### Premissas

Queremos criar apps web modernos, rápidos, confiáveis, responsivos etc.

Queremos comprar em vez de construir.


### Restrições

Queremos ferramental que funcione bem com nosso pipeline de devops e com nossas clouds de implantação.


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

Até agora, Nagios e New Relic são as extremidades do espectro. Nagios é a ferramenta viável mais antiga, mais simples e gratuita. New Relic é a ferramenta viável paga, mais completa e com recursos mais novos. Começaremos com avaliações dessas. Conforme necessário, migraremos para dentro do espectro.

Até agora, Zabbix tem as melhores recomendações e também oferece as capacidades mais completas.

Até agora, ELK tem a melhor popularidade open-source de construir em vez de comprar.

Até agora, Prometheus + Graphana têm a melhor popularidade.


### Implicações

TODO.


## Relacionado


### Decisões relacionadas

As escolhas afetarão testabilidade, telemetria e provavelmente outros sistemas, como atendimento ao cliente, engenharia de confiabilidade de sites etc.


### Requisitos relacionados

TODO.


### Artefatos relacionados

TODO.


### Princípios relacionados

Facilmente reversível.

Necessidade de velocidade.


## Notas


Uma stack open source muito boa é:

* Prometheus para métricas e alertas baseados em métricas

* Grafana para exibir métricas

* Elasticsearch/Logstash/Kibana (ELK) para logs e eventos estruturados

* Pushover para notificações mobile


### Mensagens de texto livre vs mensagens de evento estruturadas

Mensagens de texto livre: por exemplo, o tipo de coisa aleatória que você encontraria em /var/log/messages e algo gerado intencionalmente pela aplicação. As mensagens são úteis para identificar outras coisas que estão acontecendo na máquina, como falta de memória ou erros de hardware, mas têm muito lixo.

Mensagens de evento estruturadas: geradas pela aplicação, com um conjunto fixo ou dinâmico de atributos, por exemplo, um log de requisição HTTP, um log contábil, um login de usuário.

De modo geral, é bom registrar detalhes sobre cada requisição de uma forma que permita fazer drill down com base em atributos. Então adicionar, por exemplo, um userid ou sessionid a tudo permite rastrear. Rastreamento explícito também é bom, claro. Usar ELK para isso é uma espécie de https://www.honeycomb.io/ de pobre.


### Graylog é mais fácil

Graylog é mais fácil de subir pela minha experiência.



### Prometheus exige algum ajuste


Em geral estou feliz com Prometheus para métricas. O alerting exige algum ajuste, mas é muito bom. Depende da sua aplicação. Acho melhor alertar sobre condições visíveis ao usuário final, não sobre causas subjacentes. Por exemplo, tempo de carregamento de página é bom, número de requisições por segundo não é. Embora zero requisições por segundo indique que algo está errado.

A vantagem de um serviço é que eles oferecem inteligência adicional pronta para uso. Em geral gosto do Datadog. Os serviços podem ser assustadoramente caros se você tem muitos dados, e às vezes têm modelos de preço que não são cloud friendly, por exemplo cobrar por instância, quando instâncias são dinâmicas. Também há uma diferença entre serviços em que cada requisição vem de um usuário pago e aqueles relacionados a publicidade, em que apenas uma pequena porcentagem das requisições gera dinheiro. Você pode acabar com muitos dados e não tanto orçamento.

Trabalho em alguns serviços que recebem 1B de requisições por dia, então faz sentido hospedar nosso próprio monitoramento e logging. Se seus volumes são menores, então serviços hospedados são mais fáceis.


### Serviços AWS são mistos

Minha experiência com serviços AWS tem sido mista. O serviço Elasticsearch deles tem sido instável, então executamos nossas próprias instâncias para isso. Métricas do CloudWatch são caras, então geralmente só as usamos para métricas de nível "infraestrutura" em vez da aplicação, isto é, métricas relacionadas a saúde em que a AWS pode saber melhor o que está acontecendo do que software executando na instância. CloudWatch Logs pode demorar para atualizar e não tem tantos metadados. Executar ELK ajuda com isso. Se eu realmente quero dados em tempo real, então usar Kafka como transporte para logs é melhor. Isso é bem suportado pelo Logstash. Gerenciar um cluster Kafka não é para os fracos, porém, há muito encanamento exposto.


### Kafka

Comentário: Kafka pode ser super complicado às vezes, ou Kafka pode ser sólido como uma rocha e você quase esquece que ele está ali amarrando tudo junto.


Comentário: Kafka tem sido sólido, mas foi uma quantidade surpreendente de trabalho fazê-lo funcionar. Penso nele como um banco de dados relacional, mas você está trabalhando apenas na camada "física", por exemplo, tablespaces, arquivos e partições. Houve algumas vezes no início em que os utilitários de gerenciamento eram insuficientes, e tivemos que escrever programas para, por exemplo, resetar um consumer group. http://howfuckedismydatabase.com/nosql/

Comentário: Usamos Kafka como um "buffer" para mensagens de log e um lugar onde podemos fazer processamento de stream em tempo real sobre dados que vêm de múltiplos servidores. Se sofrermos um ataque DDOS, então precisamos de uma forma de analisar dados entre múltiplas instâncias. Se estivermos enviando logs diretamente dos servidores para ELK, a carga pode explodir o cluster Elasticsearch.

Comentário: Kafka é bom para nós porque, se sofrermos um ataque DDOS, então precisamos de uma forma de analisar dados entre múltiplas instâncias. Se estivermos enviando logs diretamente dos servidores para ELK, a carga pode explodir o cluster Elasticsearch.


Comentário: Kafka faz menos trabalho e é mais eficiente, então consegue lidar melhor com a carga. E colocamos o trabalho do Kafka em fila e tentamos novamente. E Kafka estar sobrecarregado não afeta usuários que estão tentando fazer trabalho interativo com Kibana, do jeito que afetaria se Elasticsearch estivesse sofrendo.

Comentário:  Processamento de stream é principalmente procurar abuso, por exemplo, tráfego demais de um único IP em todo o cluster, e então compartilhar o bloqueio por todo o cluster.

Comentário: O plugin logstash-output-kafka é bastante não confiável no momento, porém. Fui afetado por vários dos problemas na página de issues dele no GitHub, que nunca parecem ser corrigidos. Quero me afastar de usá-lo, para enviar diretamente dos nossos apps para Kafka.

Comentário: Agora estamos enviando eventos estruturados diretamente do app para Kafka. A principal motivação foi tocar os dados de log menos vezes e evitar ler e escrever no disco múltiplas vezes. Em sistemas de alto volume, logging pode dar mais trabalho do que o próprio app. Estou pensando em fazer journald enviar logs diretamente também, a partir de um programa em C.


### Loki

Fique de olho no Loki. Ele ainda não está pronto, mas, quando estiver, eu esperaria que fosse um ajuste melhor nesta stack. Loki é um agregador de logs criado pela grafana labs; ele usa sintaxe de scraping e tags semelhante à do Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager para métricas. <3 Prometheus.

Rollbar/Graylog para logging/relato de erros (há alguma sobreposição aqui; um serviço pequeno provavelmente não precisa de ambos).

Atualmente, alertas apenas vão para um de alguns canais Slack nos quais partes interessadas ativaram notificações. Se fôssemos mais sérios sobre on-call, eles iriam para PagerDuty/VictorOps/etc.

Grafana para gráficos e dashboards. Também aguardando ansiosamente para ver se os próximos recursos de logging deles tornarão Graylog desnecessário.


### Thanos

Usamos Thanos como front-end para nossa configuração HA. Ele sabe como deduplicar pares HA.

Atualmente mantemos 6 meses de dados locais do Prometheus. Isso funciona razoavelmente bem para nós. Mas estou bem no meio de lançar bucket storage para nossa configuração Thanos para armazenamento de dados de longo prazo. Em teoria, armazenamento GCS será cerca de 30% mais barato do que o disco persistente padrão GCE que usamos agora.

Não fazemos backup dos dados do Prometheus agora. Os dados simplesmente não são realmente importantes para nós além de ter o suficiente para alerting. Nossa implantação geral de frota muda tanto de ano para ano que dados históricos com mais de alguns meses simplesmente não são tão interessantes. Talvez seja interessante ter algumas estatísticas centrais ano a ano; posso configurar um conjunto core-stats de recording rules e armazená-las com Federation ou apenas deixar Thanos cuidar disso.

EDIT: Pequeno aviso, sou desenvolvedor do Prometheus.


### Prometheus HA

HA em Prometheus é feita por duplicação: você executa múltiplos poppers, há formas de consultar múltiplos e deduplicar os dados

A escalabilidade é feita decidindo a rede e fazendo diferentes Prometheus consultarem diferentes partes da rede

Armazenamento de longo prazo não é o ponto forte do proms, mas é descarregado para algo como influxes ou timescaledb (que tecnicamente também marca o check de HA) artigo que li sobre isso https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Ainda não experimentei as coisas de longo prazo, pois ainda estou apenas experimentando e usando-o para gráficos de curto prazo enquanto librenms monitora minha rede para longo prazo


###  Datadog + PagerDuty + Threat Stack

Usamos Datadog (com PagerDuty) e Threat Stack e não poderíamos estar mais felizes. Minha única queixa com DD é o custo relativamente alto do armazenamento de métricas.


### Zabbix

Zabbix com scripts customizados para monitorar quase tudo. Funciona como um encanto.


### Outlyer

Estou usando Outlyer, mas então preciso declarar que trabalho aqui, e dogfooding é obrigatório.

Ainda precisa de Graylog, Sentry e Statuscake para aprimorar.

Parece enviesado, mas, tendo executado Nagios e outros sistemas de monitoramento internamente com satisfação, eu compraria uma solução hospedada em qualquer novo trabalho e descarregaria essa dor.


### Nagios + Nagiosgraph

Executamos Nagios para todo monitoramento e alerting. Alertas acontecem por e-mail (avisos e notificações críticas) e notificações audíveis de app (para alertas críticos).

Nagiosgraph é usado para visualizações.

Essa configuração tem sido muito efetiva para nos manter amplamente informados sobre o que está acontecendo em nosso ambiente. Executamos e monitoramos cerca de 110 servidores críticos para a missão e cerca de 760 pontos de dados, e temos esse sistema de monitoramento em vigor há mais de sete anos.

Eu também gostaria de agregar logs com Graylog ou ELk em algum momento.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager via o incrível chart helm Prometheus Operator. Log ainda vai para o plano birch do LogDNA, pois percebemos que ELK é pesado demais para nossos humildes mínimo de 3 máximo de 5 nós no GKE.


### DataDog + Sentry + PagerDuty.

Eu costumava executar todas as minhas próprias soluções de monitoramento usando todo tipo de software, incluindo Nagios, Icinga, Zabbix, ELK, Greylog2, Influx e muitas outras ferramentas, mas a verdade é que há esforço demais envolvido em executar sua própria infraestrutura de monitoramento, especialmente quando você pode pagar taxas tão baixas para outra pessoa fazer isso por você!

Pagar outros para executar a infra de monitoramento libera meus clientes para focar em executar suas plataformas em vez de monitorar o monitoramento, o que significa que o valor que eles obtêm da estabilidade da plataforma supera em muito quaisquer custos de Monitoring as a Service.


### Sensu + Graphite + ELK

Minha empresa gosta muito de coisas auto-hospedadas.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager para alerting; minha equipe acredita que monitoramento simples é bom monitoramento.

Outros sistemas como logging e tracing fornecerão contexto rico para diagnosticar quando o on-call receber um alerta, mas nunca construímos alerting sobre estes.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Serviços instrumentados com Prometheus => analytics e visualização Circonus


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Estamos usando os serviços abaixo:

icinga2 para monitoramento e VictorOps para alerting

NewRelic para monitoramento detalhado do serviço

Sentry para rastreamento de erros no serviço

Slack/Email faz parte do alerting que dispara a partir de NewRelic ou icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 com integração elasticsearch para análise e integração graphite+grafana para gráficos.

graças à flexibilidade de apply rules no icinga2, os desenvolvedores só conseguem ver serviços para os quais recebem notificações.

e por meio do icinga2 director, programadores podem definir facilmente seus próprios checks (o que fazem a cada poucos dias - 100 checks saem, 100 outros checks entram) em grande escala com zero incômodo.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

O que temos agora:

DataDog para métricas

New Relic para monitoramento de aplicações

ELK (Elastic Search + Logstash + Kibana) para os logs

Sentry (auto-hospedado) para logging de exceções

Emails + Slack + VictorOps para alerting (com base na severidade)

O que queremos ter:

Prometheus para métricas (Grafana para visualização)

New Relic (provavelmente Elastic Search APM) para o monitoramento da aplicação

EFK (elastic search + fluentd + kibana) para logging. Provavelmente, Loki by Grafana estaria pronto para prod quando chegarmos aqui

Sentry para as exceções

Alertmanager + email + VictorOps para os alertas


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Aviso: trabalha na VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf para métricas de servidor como CPU, Disco, Memória e Rede. Também usamos Telegraf para monitoramento SNMP dos nossos dispositivos de rede.

Prometheus para métricas de aplicação. Codificamos health checks em nossa aplicação que Prometheus coleta.

InfluxDB para armazenamento de séries temporais. É para lá que nossos dados do Telegraf são enviados.

Grafana para dashboards e alertas. O mecanismo de alerting não é super robusto, mas faz o trabalho. Também disparamos alertas para Slack.

O que não tenho agora é uma solução centralizada de logging. ELK é poderoso, mas difícil de configurar e gerenciar, e não conheço alternativas gratuitas próximas o suficiente para investigar.


### Sematext + Logagent + Experience

Sematext para métricas, para logs, para traces, em breve para real user monitoring também. Mais simples/barato do que usar N ferramentas/serviços diferentes, IMHO.

Para envio de logs, costumávamos usar rsyslog e depois mudamos para Logagent.

Para frontend crash reporting usamos Sentry, mas mudaremos para Experience em breve.

Aviso: sou um Sematextan.


### Azure Monitor/Analytics + OpsGenie

Gostaria que Log Analytics tivesse uma interface melhor. Estamos nos afastando do splunk, que era muito mais fácil de navegar.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Você realmente não quer executar seu próprio sistema de notificações. Você pode substituir Splunk por ELK, a menos que sua equipe de Security prefira Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf como coletor, Prometheus + Alertmanager para monitoramento e alerting, integrado a canais slack e pagerduty para alertas críticos. Grafana para visualização de métricas de host.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus para métricas + alertas

Grafana para dashboards Prometheus

Cloudwatch monitorando instâncias Prometheus

sentry para rastreamento de exceções

kibana + elasticsearch

graylog

prometheus Push Gateway para batch/cronjobs

SOP https://github.com/rapidloop/sop para “push/forward” métricas de 1 instância Prometheus para outra

clientes usam os clientes Prometheus . Tentamos usar opencensus.io no lado do cliente


### PagerDuty + Monitis

PagerDuty + Monitis. Também algumas Azure Functions sob medida para testar a saúde de alguns serviços.

Procurando introduzir Prometheus e Grafana este ano


### Prometheus + Grafana + Bosun

Prometheus para armazenar os dados de séries temporais. Grafana para visualização. Bosun para gerenciamento de alertas.


### Azure Monitor/Analytics/Insights/Dashboards

Loja somente Azure, Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana para monitorar serviços de container no Kubernetes via Prometheus

Monitis para monitoramento de serviço end-to-end, principalmente para APIs web e aplicações web

OpsGenie para gerenciamento de alertas

Slack para obter informações de status dos nossos sistemas


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Engenheiro (dev)ops de longa data aqui. Cresci com Nagios. Adoraria receber opiniões sobre meu SaaS bootstrapped https://checklyhq.com. Fazemos monitoramento de API e monitoramento de transações de site com alerting bem aprofundado.

Comecei Checkly porque monitoramento ativo / sintético no espaço de APIs era um pouco limitado (e caro). Monitoramento baseado em navegador / com scripts é ainda mais proprietário e caro. Usamos Puppeteer e mantemos preços o mais baixos possível.

Nossa stack de monitoramento:

Checkly (dogfooding...)

AppOptics (gráficos customizados)

AWS Cloudwatch & SNS para mensagens SMS.

alerting integrado do Heroku.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana nos alerta no slack sobre problemas de infraestrutura ou degradação de performance, e configuramos logz.io para alertar no slack sobre certo volume de logs de nível de erro da camada da aplicação.


### SignalFX + Splunk + PagerDuty + Slack

Usando atualmente: SignalFX, Splunk, PagerDuty e Slack. Não sou um grande fã de SignalFX, embora a equipe de suporte deles seja super amigável e responsiva. Gosto de Splunk (vale a pena se você puder pagar), PagerDuty e Slack.

Eu costumava usar a stack TICK, em que a maior parte do C era na verdade um G, isto é, Grafana, embora eu tenha usado Chronograf um pouco. Aquilo era incrível, mas era uma dor para gerenciar. O dilema clássico SaaS vs auto-hospedagem.

Usei DataDog, New Relic, Graylog, ELK e BugSnag. Gosto muito de DataDog e New Relic; Graylog é muito bom. Mas não sou um grande fã de ELK. BugSnag é legal; na verdade sinto que rastrear erros/exceções é um substituto muito bom para monitoramento completo de logs em muitos casos.


### ELK + Prometheus + Grafana

Assim como outros, usamos ELK para logs e Prometheus+Grafana para todo o resto.

Manter essa configuração é fácil se você se der permissão para ocasionalmente perder dados. Por exemplo, se nosso banco de dados ElasticSearch entrar em pane (o que infelizmente acontece a cada 2-3 meses para nós), não nos preocupamos com HA e em vez disso descartamos os dados e seguimos com a vida. Se você absolutamente precisa ter HA ou retenção de longo prazo, boa sorte.


### Datadog + Prometheus + Grafana

Configurei Datadog mês a mês porque, quando cheguei aqui, não havia monitoramento nem alerting. Apenas alguns dos nossos sites estavam sendo monitorados a cada 5m para uptime. Datadog é de longe o mais fácil de configurar. Quando eu terminar de tratar todos os outros problemas, mudarei para Prometheus+Grafana. Ainda não 100% decidido sobre gerenciamento de logs.

### Nagios + ELK

Temos mais de 100+ produtos que suportamos.

Para on-prem, é principalmente Nagios e ELK. Para cloud, estamos migrando de DataDog para NewRelic.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Costumávamos usar datadog, mas achamos caro demais para nossas necessidades. Não me entenda mal, é incrível, mas tem um custo enorme. Conseguimos configurar site24x7.com com uma assinatura anual por cerca de 2-3 meses de custo da DD.

Nossa stack de monitoramento:

Site24x7 - APM, monitoramento de URL externa, monitoramento de mailflow SMTP, expiração de ssl e monitoramento de processos.

StatusCake - para monitoramento de URL e confirmação - É nosso backup caso site24x7 perca alguma coisa (não perde), mas SC é mais flexível para monitoramento externo de portas e serviços para nossas necessidades.

Ambas as ferramentas escalam para PagerDuty, e então recebemos nossas escalações no slack.

SumoLogic - para monitoramento de logs (é uma ótima ferramenta, mas um pouco complicada para nossas necessidades)

A partir do slack podemos ack ou remediar o alerta.

Então temos muitas automações site24x7 que se conectam a commando.io para 'BedOps', como chamamos - onde um alerta é disparado, iniciamos alguns scripts ou automações como tentativa de remediar a situação (99% do tempo a automação + nossos scripts nos mantêm fora de problemas)

Temos runbooks internos em nossa KB para quando as automações falham ou se há algo fora do escopo que precisa ser corrigido.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana para métricas em nossos clusters GKE e VMs.

Google Stackdriver para Logs (pois está incluído e ativo por padrão e atualmente é suficiente para nossas necessidades).


### Zabbix

Zabbix para tudo. Nenhum software adicional necessário.
