# 메트릭, 모니터, 알림

목차:

* [요약](#요약)
  * [이슈](#이슈)
  * [결정](#결정)
  * [상태](#상태)
* [세부 사항](#세부-사항)
  * [가정](#가정)
  * [제약](#제약)
  * [입장](#입장)
  * [논거](#논거)
  * [영향](#영향)
* [관련 항목](#관련-항목)
  * [관련 결정](#관련-결정)
  * [관련 요구사항](#관련-요구사항)
  * [관련 산출물](#관련-산출물)
  * [관련 원칙](#관련-원칙)
* [메모](#메모)
  * [자유 형식 메시지 대 구조화된 이벤트 메시지](#자유-형식-메시지-대-구조화된-이벤트-메시지)
  * [Graylog가 더 쉽다](#graylog가-더-쉽다)
  * [Prometheus는 약간의 튜닝이 필요하다](#prometheus는-약간의-튜닝이-필요하다)
  * [AWS 서비스는 엇갈린다](#aws-서비스는-엇갈린다)
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
  * [Datadog 대 Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack](#datadog-대-site24x7--statuscake--pagerduty--sumologic--slack)
  * [Prometheus + AlertManager + Grafana + Stackdriver](#prometheus--alertmanager--grafana--stackdriver)
  * [Zabbix](#zabbix-1)


## 요약


### 이슈

우리는 애플리케이션이 얼마나 잘 작동하는지 알고 문제가 있을 때 알 수 있도록 메트릭, 모니터, 알림을 사용하고자 합니다.


### 결정

작업 중(WIP).


### 상태

정보를 수집하는 중입니다. 스펙트럼의 합리적인 양 극단에서 시작합니다. 가장 많이 추천되는 오래된 무료 도구(Nagios)와 가장 많이 추천되는 더 새로운 유료 도구(New Relic)입니다.


## 세부 사항


### 가정

우리는 현대적이고, 빠르고, 신뢰할 수 있고, 반응형인 웹 앱을 만들고자 합니다.

우리는 만드는 것보다 사는 것을 선호합니다.


### 제약

우리는 데브옵스 파이프라인 및 배포 클라우드와 잘 작동하는 도구를 원합니다.


### 입장

우리는 현재 입장을 조사하고 있습니다.


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

  
### 논거

지금까지 Nagios와 New Relic이 스펙트럼의 양 극단입니다. Nagios는 가장 오래되고, 가장 단순하고, 무료이며, 실행 가능한 도구입니다. New Relic은 가장 새로운 기능을 갖추고, 가장 완전하며, 유료이고, 실행 가능한 도구입니다. 이 둘에 대한 평가로 시작합니다. 필요에 따라 스펙트럼 안쪽으로 이동합니다.  

지금까지 Zabbix가 가장 좋은 추천을 받았으며 가장 완전한 기능도 제공합니다.

지금까지 ELK가 오픈 소스, 직접 구축(사기보다 만들기) 방식 중 가장 좋은 인기를 얻고 있습니다.

지금까지 Prometheus + Graphana가 가장 좋은 인기를 얻고 있습니다.


### 영향

해야 할 일(TODO).


## 관련 항목


### 관련 결정

이 선택은 테스트 용이성, 텔레메트리, 그리고 고객 지원, 사이트 신뢰성 엔지니어링 등을 위한 시스템 같은 다른 시스템에도 영향을 미칠 가능성이 높습니다.


### 관련 요구사항

해야 할 일(TODO).


### 관련 산출물

해야 할 일(TODO).


### 관련 원칙

쉽게 되돌릴 수 있음.

속도에 대한 필요.


## 메모


꽤 좋은 오픈 소스 스택은 다음과 같습니다:

* 메트릭과 메트릭 기반 알림을 위한 Prometheus

* 메트릭을 표시하기 위한 Grafana

* 로그와 구조화된 이벤트를 위한 Elasticsearch/Logstash/Kibana (ELK)

* 모바일 알림을 위한 Pushover


### 자유 형식 메시지 대 구조화된 이벤트 메시지

자유 형식 메시지: 예를 들어 /var/log/messages에서 볼 수 있는 임의의 것들과, 애플리케이션이 의도적으로 생성하는 것. 이 메시지는 메모리 부족이나 하드웨어 오류 같은 머신에서 일어나는 다른 일을 식별하는 데 유용하지만 쓰레기가 많습니다. 

구조화된 이벤트 메시지: 애플리케이션이 생성하며 고정 또는 동적 속성 집합을 가집니다. 예: HTTP 요청 로그, 회계 로그, 사용자 로그인.

일반적으로 속성별로 드릴다운할 수 있는 방식으로 각 요청에 대한 세부 정보를 기록하는 것이 좋습니다. 그래서 모든 것에 예를 들어 userid나 sessionid를 추가하면 추적할 수 있습니다. 명시적 추적도 물론 좋습니다. 이를 위해 ELK를 사용하는 것은 일종의 가난한 사람의 https://www.honeycomb.io/ 입니다.


### Graylog가 더 쉽다

제 경험으로는 Graylog가 설정하기 더 쉽습니다.



### Prometheus는 약간의 튜닝이 필요하다


저는 메트릭에 대해서는 대체로 Prometheus에 만족합니다. 알림은 약간의 튜닝이 필요하지만 꽤 좋습니다. 애플리케이션에 따라 다릅니다. 저는 근본 원인이 아니라 최종 사용자에게 보이는 상태에 대해 알림을 보내는 것이 가장 좋다고 생각합니다. 예를 들어 페이지 로드 시간은 좋지만 초당 요청 수는 그렇지 않습니다. 물론 초당 요청이 0이라면 뭔가 잘못된 것이지만요.

서비스의 이점은 바로 쓸 수 있는 추가적인 지능을 제공한다는 것입니다. 저는 대체로 Datadog를 좋아합니다. 데이터가 많으면 서비스는 무섭도록 비쌀 수 있고, 때로는 인스턴스가 동적인데 인스턴스당 과금하는 것처럼 클라우드 친화적이지 않은 가격 모델을 가집니다. 또한 모든 요청이 유료 사용자에게서 오는 서비스와 광고 관련이어서 요청의 작은 비율만 돈이 되는 서비스 사이에는 차이가 있습니다. 데이터는 많은데 예산은 별로 없는 상황이 될 수 있습니다.

저는 하루 10억 건의 요청을 받는 몇몇 서비스에서 일하는데, 그래서 자체 모니터링과 로깅을 호스팅하는 것이 합리적입니다. 규모가 더 작다면 호스팅 서비스가 더 쉽습니다.


### AWS 서비스는 엇갈린다

AWS 서비스에 대한 제 경험은 엇갈렸습니다. 그들의 Elasticsearch 서비스는 불안정해서 우리는 자체 인스턴스를 운영합니다. CloudWatch 메트릭은 비싸서, 일반적으로 애플리케이션이 아니라 “인프라 수준” 메트릭, 즉 인스턴스에서 실행되는 소프트웨어보다 AWS가 무슨 일이 일어나는지 더 잘 알 수 있는 상태 관련 메트릭에만 사용합니다. CloudWatch Logs는 갱신이 느릴 수 있고 메타데이터가 많지 않습니다. ELK를 운영하면 도움이 됩니다. 정말 실시간 데이터를 원한다면 로그의 전송 수단으로 Kafka를 사용하는 것이 좋습니다. Logstash가 꽤 잘 지원합니다. 다만 Kafka 클러스터를 관리하는 것은 심약한 사람을 위한 일이 아니며, 날것 그대로의 배관 작업이 많습니다.


### Kafka

댓글: Kafka는 때로는 엄청나게 어려울 수 있고, 또는 있다는 사실을 거의 잊을 만큼 바위처럼 안정적이어서 모든 것을 이어 주기도 합니다. 


댓글: Kafka는 안정적이었지만 동작시키는 데 놀랄 만큼 많은 작업이 필요했습니다. 저는 이를 관계형 데이터베이스처럼 생각하지만 테이블스페이스, 파일, 파티션 같은 “물리적” 계층에서만 작업하는 것입니다. 초기에는 관리 도구가 부족한 때가 있어서, 예를 들어 컨슈머 그룹을 재설정하려면 프로그램을 작성해야 했습니다. http://howfuckedismydatabase.com/nosql/

댓글: 우리는 Kafka를 로그 메시지의 “버퍼”로, 그리고 여러 서버에서 오는 데이터에 대해 실시간 스트림 처리를 할 수 있는 곳으로 사용합니다. DDOS 공격을 받으면 여러 인스턴스에 걸쳐 데이터를 분석할 방법이 필요합니다. 서버에서 ELK로 직접 로깅하면 부하가 Elasticsearch 클러스터를 터뜨릴 수 있습니다.

댓글: Kafka는 우리에게 좋은데, DDOS 공격을 받으면 여러 인스턴스에 걸쳐 데이터를 분석할 방법이 필요하기 때문입니다. 서버에서 ELK로 직접 로깅하면 부하가 Elasticsearch 클러스터를 터뜨릴 수 있습니다.


댓글: Kafka는 더 적은 일을 하고 더 효율적이므로 부하를 더 잘 처리할 수 있습니다. 그리고 우리는 Kafka 작업을 큐에 넣고 재시도합니다. 또한 Kafka가 과부하 상태여도 Elasticsearch가 힘들어할 때처럼 Kibana로 대화형 작업을 하려는 사용자에게는 영향이 없습니다.

댓글: 스트림 처리는 주로 남용, 예를 들어 클러스터 전체에서 단일 IP의 과도한 트래픽을 찾고, 그 차단을 클러스터 전체에 공유합니다.

댓글: 하지만 logstash-output-kafka 플러그인은 지금 꽤 신뢰할 수 없습니다. GitHub 이슈 페이지에 있는 여러 문제를 겪었는데 해결되는 것 같지 않습니다. 저는 이를 쓰지 않고 우리 앱에서 Kafka로 직접 보내는 쪽으로 옮겨 가고 싶습니다.

댓글: 이제 우리는 구조화된 이벤트를 앱에서 Kafka로 직접 보냅니다. 주된 동기는 로그 데이터를 만지는 횟수를 줄이고 디스크를 여러 번 읽고 쓰는 것을 피하는 것이었습니다. 대용량 시스템에서는 로깅이 앱 자체보다 더 많은 작업을 할 수 있습니다. journald가 C 프로그램에서 로그를 직접 보내게 하는 것도 생각 중입니다.


### Loki

Loki를 지켜보십시오. 아직 준비되지 않았지만 준비되면 이 스택에 더 잘 맞을 것으로 기대합니다. Loki는 grafana labs가 만든 로그 수집기로, Prometheus와 비슷한 스크레이핑 및 태그 문법을 사용합니다.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 메트릭에는 Prometheus + alertmanager. Prometheus를 정말 좋아합니다.

로깅/오류 보고에는 Rollbar/Graylog (여기에는 약간의 중복이 있으며, 작은 서비스에는 아마 둘 다 필요하지 않을 것입니다).

현재 알림은 관심 있는 사람들이 알림을 켜 둔 몇 개의 Slack 채널 중 하나로만 갑니다. 당직에 더 진지하다면 PagerDuty/VictorOps 등으로 갈 것입니다.

그래프와 대시보드에는 Grafana. 곧 나올 로깅 기능이 Graylog를 불필요하게 만들지도 기대하고 있습니다.


### Thanos

우리는 HA 설정의 프런트엔드로 Thanos를 사용합니다. HA 쌍의 중복을 제거할 줄 압니다.

현재 로컬 Prometheus 데이터를 6개월 보관합니다. 우리에게는 꽤 잘 작동합니다. 하지만 장기 데이터 보관을 위해 Thanos 설정에 버킷 스토리지를 도입하는 중입니다. 이론적으로 GCS 스토리지는 현재 사용 중인 GCE 표준 영구 디스크보다 약 30% 저렴할 것입니다.

현재 Prometheus 데이터는 백업하지 않습니다. 데이터는 알림에 충분한 정도를 넘어서는 우리에게 그다지 중요하지 않습니다. 우리의 전체 플릿 배포는 해마다 많이 변하므로 몇 달보다 오래된 과거 데이터는 그다지 흥미롭지 않습니다. 연도별 핵심 통계 몇 가지를 갖는 것은 흥미로울 수 있으니, 핵심 통계에 대한 기록 규칙 집합을 설정하고 Federation으로 저장하거나 Thanos가 처리하게 할 수도 있습니다.

수정: 약간의 설명을 덧붙이면, 저는 Prometheus 개발자입니다.


### Prometheus HA

Prometheus의 HA는 복제로 이루어집니다. 여러 수집기를 실행하며, 여러 개를 조회하고 데이터의 중복을 제거하는 방법이 있습니다.

확장은 네트워크를 정하고 서로 다른 Prometheus가 네트워크의 서로 다른 부분을 조회하게 함으로써 이루어집니다.

장기 저장은 Prometheus의 강점이 아니므로 influx나 timescaledb(기술적으로 HA도 충족) 같은 것에 맡깁니다. 이에 대해 읽은 글: https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

아직은 실험만 하고 단기 그래프에 사용하며 librenms가 장기적으로 네트워크를 모니터링하고 있어서 장기 부분은 아직 시도하지 않았습니다


###  Datadog + PagerDuty + Threat Stack

우리는 Datadog(PagerDuty와 함께)와 Threat Stack을 사용하며 이보다 더 만족스러울 수 없습니다. DD에 대한 제 유일한 불만은 메트릭 저장 비용이 상대적으로 높다는 것입니다.


### Zabbix

거의 모든 것을 모니터링하기 위한 사용자 정의 스크립트와 함께 Zabbix. 꿈처럼 작동합니다.


### Outlyer

저는 Outlyer를 사용하지만 여기서 일한다는 것을 밝혀야 하며, 자사 제품을 직접 써 보는 것(dogfooding)은 필수입니다.

개선을 위해 여전히 Graylog, Sentry, Statuscake가 필요합니다.

편향되게 들리지만, 내부적으로 Nagios와 다른 모니터링 시스템을 즐겁게 운영해 본 후에는 새 직장마다 호스팅 솔루션을 사서 그 고통을 덜어 줄 것입니다.


### Nagios + Nagiosgraph

우리는 모든 모니터링과 알림에 Nagios를 운영합니다. 알림은 이메일(경고 및 치명적 알림)과 소리가 나는 앱 알림(치명적 알림)을 통해 이루어집니다.

시각화에는 Nagiosgraph를 사용합니다.

이 설정은 우리 환경에서 무슨 일이 일어나는지 포괄적으로 알려 주는 데 매우 효과적이었습니다. 우리는 약 110대의 업무상 중요한 서버와 약 760개의 데이터 포인트를 운영하고 모니터링하며, 이 아침 시스템을 7년 넘게 사용해 왔습니다.

언젠가는 Graylog나 ELk로 로그도 집계하고 싶습니다.


### Prometheus + Grafana + AlertManager

멋진 helm 차트 Prometheus Operator를 통한 Prometheus + Grafana + AlertManager. 로그는 여전히 LogDNA birch 플랜으로 가는데, 최소 3개 최대 5개 노드의 GKE에 있는 우리의 소박한 클러스터에는 ELK가 너무 무겁다는 것을 알게 되었기 때문입니다.


### DataDog + Sentry + PagerDuty.

저는 Nagios, Icinga, Zabbix, ELK, Greylog2, Influx 등 온갖 종류의 소프트웨어로 직접 모든 모니터링 솔루션을 운영하곤 했지만, 사실 자체 모니터링 인프라를 운영하는 것은 너무나 많은 일이며, 특히 다른 누군가에게 그렇게 낮은 가격으로 대신 맡길 수 있을 때는 더욱 그렇습니다!

다른 사람에게 비용을 지불하고 모니터링 인프라를 운영하게 하면 고객들이 모니터링을 모니터링하는 대신 플랫폼 운영에 집중할 수 있으며, 이는 플랫폼 안정성에서 얻는 가치가 서비스형 모니터링의 어떤 비용보다 훨씬 크다는 뜻입니다.


### Sensu + Graphite + ELK

제 회사는 자체 호스팅을 매우 선호합니다.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

알림에는 Prometheus + Alertmanager, 우리 팀은 단순한 모니터링이 좋은 모니터링이라고 생각합니다.

로깅과 추적 같은 다른 시스템은 당직자가 알림을 받았을 때 진단을 위한 풍부한 맥락을 제공하지만, 우리는 그것들을 기반으로 알림을 만들지는 않습니다.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Prometheus로 계측된 서비스 => Circonus 분석과 시각화


### icinga2 + VictorOps + NewRelic + Sentry + Slack

우리는 다음 서비스를 사용합니다:

모니터링에는 icinga2, 알림에는 VictorOps

서비스의 상세한 모니터링에는 NewRelic

서비스의 오류 추적에는 Sentry

Slack/이메일은 NewRelic이나 icinga2에서 발동되는 알림의 일부입니다


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

분석을 위한 elasticsearch 통합과 그래프를 위한 graphite+grafana 통합이 있는 icinga2.

icinga2의 apply 규칙의 유연성 덕분에 개발자는 자신이 알림을 받는 서비스만 볼 수 있습니다.

그리고 icinga2 director를 통해 프로그래머는 번거로움 없이 대규모로 자신의 검사를 쉽게 정의할 수 있습니다(실제로 며칠마다 100개의 검사가 나가고 다른 100개의 검사가 들어옵니다).


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

지금 가진 것:

메트릭에는 DataDog

애플리케이션 모니터링에는 New Relic

로그에는 ELK(Elastic Search + Logstash + Kibana)

예외 로깅에는 Sentry(자체 호스팅)

알림에는 이메일 + Slack + VictorOps(심각도에 따라)

원하는 것:

메트릭에는 Prometheus(시각화에는 Grafana)

애플리케이션 모니터링에는 New Relic(아마 Elastic Search APM)

로깅에는 EFK(elastic search + fluentd + kibana). 그때쯤이면 Grafana의 Loki가 운영 준비가 될 수도 있음

예외에는 Sentry

알림에는 Alertmanager + 이메일 + VictorOps


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (설명: VMware에서 일합니다)


### Telegraf + Prometheus + InfluxDB + Grafana

CPU, 디스크, 메모리, 네트워크 같은 서버 메트릭에는 Telegraf. 네트워크 장치의 SNMP 모니터링에도 Telegraf를 사용합니다.

애플리케이션 메트릭에는 Prometheus. 우리는 애플리케이션에 Prometheus가 스크레이핑하는 상태 검사를 코딩합니다.

시계열 저장에는 InfluxDB. Telegraf 데이터가 여기로 갑니다.

대시보드와 알림에는 Grafana. 알림 엔진은 아주 탄탄하지는 않지만 제 역할은 합니다. 알림은 Slack으로도 보냅니다.

지금 없는 것은 중앙화된 로깅 솔루션입니다. ELK는 강력하지만 설정하고 관리하기 어렵고, 살펴볼 만큼 충분히 비슷한 무료 대안은 모릅니다.


### Sematext + Logagent + Experience

메트릭, 로그, 추적, 그리고 곧 실제 사용자 모니터링까지 Sematext. 제 소견으로는 N개의 서로 다른 도구/서비스를 사용하는 것보다 더 쉽고/저렴합니다.

로그 전송에는 rsyslog를 사용하다가 Logagent로 바꿨습니다.

프런트엔드 충돌 보고에는 Sentry를 사용하지만 곧 Experience로 바꿀 것입니다.

설명: 저는 Sematext 직원입니다.


### Azure Monitor/Analytics + OpsGenie

Log Analytics에 더 나은 인터페이스가 있으면 좋겠습니다. 탐색하기가 훨씬 쉬웠던 splunk에서 벗어나는 중입니다.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

자체 알림 시스템을 운영하고 싶지는 않을 것입니다. 보안팀이 Splunk를 선호하지 않는다면 Splunk를 ELK로 대체할 수 있습니다.


### Telegraf + Prometheus + Grafana + Alertmanager

수집기로 Telegraf, 모니터링과 알림에 Prometheus + Alertmanager, slack 채널과 치명적 알림용 pagerduty와 통합. 호스트 메트릭 시각화에는 Grafana.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

메트릭 + 알림에 Prometheus

Prometheus 대시보드에 Grafana

Cloudwatch가 Prometheus 인스턴스를 모니터링

예외 추적에 sentry

kibana + elasticsearch

graylog

배치/cronjob용 prometheus Push Gateway

메트릭을 Prometheus 인스턴스 1에서 다른 인스턴스로 “푸시/전달”하기 위한 SOP https://github.com/rapidloop/sop

클라이언트는 Prometheus 클라이언트를 사용합니다. 클라이언트 측에서는 opencensus.io를 사용하려고 합니다


### PagerDuty + Monitis

PagerDuty + Monitis. 일부 서비스의 상태를 테스트하기 위한 맞춤형 Azure Functions도 있습니다.

올해 Prometheus와 Grafana를 도입하기를 희망합니다


### Prometheus + Grafana + Bosun

시계열 데이터를 저장하는 Prometheus. 시각화에는 Grafana. 알림 관리에는 Bosun.


### Azure Monitor/Analytics/Insights/Dashboards

Azure 전용: Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Prometheus를 통해 Kubernetes의 컨테이너 서비스를 모니터링하는 Grafana

주로 웹 API와 웹 애플리케이션에 대한 서비스의 종단 간 모니터링을 위한 Monitis

알림 관리를 위한 OpsGenie

시스템의 상태 정보를 받기 위한 Slack


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

오랜 경력의 (dev)ops 엔지니어입니다. Nagios와 함께 자랐습니다. 제가 자체 자금으로 만든 SaaS https://checklyhq.com 에 대한 의견을 기꺼이 듣고 싶습니다. 우리는 API 모니터링과 웹사이트 트랜잭션 모니터링을 꽤 깊이 있는 알림과 함께 제공합니다.

저는 API 영역의 능동적/합성 모니터링이 다소 제한적이고(비싸기도 했기에) Checkly를 시작했습니다. 브라우저 기반/스크립트 기반 모니터링은 훨씬 더 독점적이고 비쌉니다. 우리는 Puppeteer를 사용하고 가격을 가능한 한 낮게 유지합니다.

우리의 모니터링 스택:

Checkly (dogfooding...)

AppOptics (사용자 정의 그래프)

SMS 알림을 위한 AWS Cloudwatch & SNS.

내장 Heroku 알림.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana는 인프라 문제나 성능 저하가 있으면 slack으로 알려 주고, 우리는 애플리케이션 계층에서 오류 수준 로그가 일정 볼륨에 이르면 slack에 알리도록 logz.io를 구성했습니다.


### SignalFX + Splunk + PagerDuty + Slack

현재 사용 중: SignalFX, Splunk, PagerDuty, Slack. 지원팀은 매우 친절하고 반응이 빠르지만 저는 SignalFX의 큰 팬은 아닙니다. Splunk(비용을 감당할 수 있다면 그만한 가치가 있음), PagerDuty, Slack은 좋아합니다.

TICK 스택을 사용하곤 했는데, 그 C의 대부분은 사실 G, 즉 Grafana였습니다(Chronograf도 조금 썼지만). 훌륭했지만 관리하기가 고통이었습니다. SaaS 대 자체 호스팅이라는 고전적인 딜레마입니다.

DataDog, New Relic, Graylog, ELK, BugSnag를 사용해 봤습니다. DataDog와 New Relic은 매우 좋아하고 Graylog는 꽤 좋습니다. ELK의 큰 팬은 아닙니다. BugSnag는 좋으며, 사실 많은 경우 오류/예외 추적이 전체 로그 모니터링의 꽤 좋은 대체재라고 느낍니다.


### ELK + Prometheus + Grafana

다른 사람들처럼 우리는 로그에 ELK를, 그 외 모든 것에 Prometheus+Grafana를 사용합니다.

이 설정은 가끔 데이터를 잃는 것을 스스로 허용한다면 유지보수가 쉽습니다. 예를 들어 우리의 ElasticSearch 데이터베이스가 침체에 빠지면(안타깝게도 2~3개월마다 일어납니다) HA에 신경 쓰지 않고 데이터를 버리고 우리 삶을 계속합니다. 반드시 HA나 장기 저장이 필요하다면 행운을 빕니다.


### Datadog + Prometheus + Grafana

저는 월 단위로 Datadog를 설정했는데, 제가 여기 왔을 때는 모니터링도 알림도 없었기 때문입니다. 사이트 몇 개만 가동 시간을 위해 5분마다 모니터링되고 있었습니다. Datadog는 단연코 설정하기 가장 쉽습니다. 다른 모든 문제를 처리하고 나면 Prometheus+Grafana로 전환할 것입니다. 로그 관리에 대해서는 아직 100% 정하지 못했습니다.

### Nagios + ELK

우리는 100개 이상의 제품을 지원합니다.

온프레미스는 대부분 Nagios와 ELK입니다. 클라우드는 DataDog에서 NewRelic으로 마이그레이션 중입니다.


### Datadog 대 Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

우리는 datadog를 사용하곤 했지만 우리 요구에 비해 너무 비싸다는 것을 알았습니다. 오해하지 마세요, 훌륭하지만 비용이 엄청납니다. 우리는 DD 비용의 약 2~3개월 치로 site24x7.com의 연간 구독을 설정할 수 있었습니다.

우리의 모니터링 스택:

Site24x7 - APM, 외부 URL 모니터링, SMTP 메일 흐름 모니터링, ssl 만료일, 프로세스 모니터링.

StatusCake - URL 모니터링과 확인용 - site24x7이 무언가를 놓칠 경우를 위한 우리의 예비(놓치지는 않지만)이며, SC는 우리 요구에 맞는 외부 포트와 서비스 모니터링에 더 유연합니다.

두 도구 모두 PagerDuty로 에스컬레이션하고, 그다음 slack에서 에스컬레이션을 받습니다.

SumoLogic - 로그 모니터링용(훌륭한 도구이지만 우리 요구에는 약간 복잡함)

slack에서 알림을 확인(ack)하거나 해결할 수 있습니다.

그리고 우리가 ’BedOps’라고 부르는 것을 위해 commando.io에 연결되는 site24x7 자동화가 많이 있습니다. 알림이 발동하면 상황을 해결하려는 시도로 일부 스크립트나 자동화를 시작합니다(99%의 경우 자동화와 우리 스크립트가 우리를 곤경에서 구해 줍니다).

자동화가 실패하거나 해결이 필요한 범위 밖의 일이 있을 때를 위한 내부 런북이 우리 KB에 있습니다.


### Prometheus + AlertManager + Grafana + Stackdriver

우리 GKE 클러스터와 VM의 메트릭에는 Prometheus(Operator) / AlertManager / Grafana.

로그에는 Google Stackdriver(기본으로 포함되어 활성화되어 있고 현재로서는 우리 요구에 충분하기 때문에).


### Zabbix

모든 것에 Zabbix. 추가 소프트웨어가 필요 없습니다.
