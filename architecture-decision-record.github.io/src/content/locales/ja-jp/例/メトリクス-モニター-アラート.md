# メトリクス、モニター、アラート

目次:

* [概要](#概要)
  * [課題](#課題)
  * [決定](#決定)
  * [状態](#状態)
* [詳細](#詳細)
  * [前提](#前提)
  * [制約](#制約)
  * [ポジション](#ポジション)
  * [論拠](#論拠)
  * [影響](#影響)
* [関連](#関連)
  * [関連する決定](#関連する決定)
  * [関連する要件](#関連する要件)
  * [関連する成果物](#関連する成果物)
  * [関連する原則](#関連する原則)
* [メモ](#メモ)
  * [自由形式のテキストメッセージ対構造化イベントメッセージ](#自由形式のテキストメッセージ対構造化イベントメッセージ)
  * [Graylog の方が簡単](#graylog-の方が簡単)
  * [Prometheus には多少のチューニングが必要](#prometheus-には多少のチューニングが必要)
  * [AWS のサービスは玉石混交](#aws-のサービスは玉石混交)
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
  * [Datadog 対 Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack](#datadog-対-site24x7--statuscake--pagerduty--sumologic--slack)
  * [Prometheus + AlertManager + Grafana + Stackdriver](#prometheus--alertmanager--grafana--stackdriver)
  * [Zabbix](#zabbix-1)


## 概要


### 課題

アプリケーションがどれだけうまく動作しているか、そして問題が発生したときにそれを知りたいため、メトリクス、モニター、アラートを使用したい。


### 決定

WIP。


### 状態

情報を収集中。可能性のあるスペクトルの両端から始めています: 最も推奨されている古い無料ツール(Nagios)と、最も推奨されている新しい有料ツール(New Relic)です。


## 詳細


### 前提

モダンで、高速で、信頼でき、レスポンシブな Web アプリなどを作成したい。

構築するよりも購入したい。


### 制約

私たちの devops パイプラインおよびデプロイ先のクラウドとうまく連携するツールが欲しい。


### ポジション

現在、ポジションを調査しています。


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

  
### 論拠

これまでのところ、Nagios と New Relic がスペクトルの両端です。Nagios は最も古く、最もシンプルで、無料の、実行可能なツールです。New Relic は最も新しい機能を備え、最も完全で、有料の、実行可能なツールです。まずこれらの評価から始めます。必要に応じて、スペクトルの中間へ移っていきます。  

これまでのところ、Zabbix が最良の推奨を得ており、また最も完全な機能を提供しています。

これまでのところ、ELK は、オープンソースを購入ではなく自前で構築するという点で最高の人気を得ています。

これまでのところ、Prometheus + Graphana が最高の人気を得ています。


### 影響

TODO。


## 関連


### 関連する決定

この選択は、テスト容易性、テレメトリ、およびおそらくカスタマーサービスやサイト信頼性エンジニアリングなどの他のシステムに影響を与えます。


### 関連する要件

TODO。


### 関連する成果物

TODO。


### 関連する原則

容易に元に戻せる。

スピードの必要性。


## メモ


かなり良いオープンソーススタックは次のとおりです:

* メトリクスと、メトリクスに基づくアラートのための Prometheus

* メトリクスを表示するための Grafana

* ログと構造化イベントのための Elasticsearch/Logstash/Kibana(ELK)

* モバイル通知のための Pushover


### 自由形式のテキストメッセージ対構造化イベントメッセージ

自由形式のテキストメッセージ: たとえば、/var/log/messages にあるようなランダムなもの、およびアプリケーションが意図的に生成するもの。このメッセージは、メモリ不足やハードウェアエラーなど、そのマシンで起きている他のことを特定するのに役立ちますが、ゴミがたくさんあります。 

構造化イベントメッセージ: アプリケーションによって生成され、固定または動的な属性のセットを持ちます。たとえば、HTTP リクエストログ、会計ログ、ユーザーログイン。

一般に、属性に基づいて掘り下げられる方法で、すべてのリクエストの詳細をログに記録するのが望ましいです。したがって、たとえば userid や sessionid をすべてに追加すると、追跡できます。もちろん、明示的なトレースも良いです。これに ELK を使用するのは、https://www.honeycomb.io/ の貧乏人版のようなものです


### Graylog の方が簡単

私の経験では、Graylog の方が立ち上げが簡単です。



### Prometheus には多少のチューニングが必要


私は一般にメトリクスには Prometheus に満足しています。アラートには多少のチューニングが必要ですが、かなり良いです。アプリケーション次第です。根本的な原因ではなく、エンドユーザーから見える状態に対してアラートを出すのが最善だと思います。たとえば、ページの読み込み時間は良いですが、1 秒あたりのリクエスト数は良くありません。ただし、1 秒あたりのリクエストがゼロの場合は、何かがおかしいことを示します。

サービスの利点は、追加のインテリジェンスをすぐに提供してくれることです。私は一般に Datadog が好きです。データが大量にある場合、サービスは恐ろしく高価になる可能性があり、インスタンスが動的なのにインスタンスごとに課金するなど、クラウドに優しくない価格モデルを持つこともあります。また、すべてのリクエストが有料ユーザーからのサービスと、広告関連のサービスの間にも違いがあります。後者では、リクエストのごく一部の割合しかお金になりません。大量のデータがあるのに、予算はそれほどない、という状態になりかねません。

私は 1 日に 10 億件のリクエストを受けるいくつかのサービスに取り組んでおり、自前でモニタリングとロギングをホストするのが理にかなっています。ボリュームが少ないなら、ホスト型サービスの方が簡単です。


### AWS のサービスは玉石混交

AWS のサービスに関する私の経験は玉石混交です。彼らの Elasticsearch サービスは不安定だったため、それについては自前のインスタンスを実行しています。CloudWatch のメトリクスは高価なので、一般にアプリケーションではなく「インフラストラクチャ」レベルのメトリクス、つまり AWS の方がインスタンス上で動作するソフトウェアよりも何が起きているかをよく把握できる、健全性に関連するメトリクスにのみ使用しています。CloudWatch Logs は更新が遅いことがあり、メタデータもそれほど多くありません。ELK を実行するとそれが改善されます。本当にリアルタイムのデータが欲しいなら、ログのトランスポートとして Kafka を使う方が良いです。それは Logstash でかなりよくサポートされています。ただし、Kafka クラスターの管理は気の弱い人向けではなく、むき出しの配管がたくさんあります。


### Kafka

コメント: Kafka は時に非常に厄介になることもあれば、非常に堅牢で、すべてをつなぎ合わせてそこにあることをほとんど忘れてしまうこともあります。 


コメント: Kafka は堅牢でしたが、動かすまでに驚くほどの作業量がありました。リレーショナルデータベースのようなものだと考えていますが、テーブルスペース、ファイル、パーティションなどの「物理」層でのみ作業している感じです。初期の頃は管理ユーティリティが不足している時期があり、たとえばコンシューマーグループをリセットするためのプログラムを書かなければなりませんでした。http://howfuckedismydatabase.com/nosql/

コメント: 私たちは Kafka を、ログメッセージの「バッファ」として、また複数のサーバーから来るデータに対してリアルタイムのストリーム処理を行える場所として使用しています。DDOS 攻撃を受けた場合、複数のインスタンスにわたってデータを分析する方法が必要です。サーバーから直接 ELK にログを記録していると、その負荷が Elasticsearch クラスターを吹き飛ばす可能性があります。

コメント: Kafka は私たちにとって良いものです。DDOS 攻撃を受けた場合、複数のインスタンスにわたってデータを分析する方法が必要だからです。サーバーから直接 ELK にログを記録していると、その負荷が Elasticsearch クラスターを吹き飛ばす可能性があります。


コメント: Kafka はより少ない仕事で、より効率的なので、負荷をよりうまく処理できます。また、私たちは Kafka の作業をキューに入れて再試行します。そして、Kafka が過負荷になっても、Elasticsearch が苦戦している場合のように、Kibana でインタラクティブな作業をしようとしているユーザーには影響しません。

コメント: ストリーム処理は主に不正利用、たとえばクラスター全体で単一の IP からのトラフィックが多すぎることなどを探し、そのブロックをクラスター全体で共有します。

コメント: ただし、logstash-output-kafka プラグインは現時点ではかなり信頼性が低いです。GitHub の issues ページにある、決して修正されないように見える複数の問題に悩まされてきました。これの使用をやめて、アプリから直接 Kafka に送信する方向に移りたいと考えています。

コメント: 現在、アプリから直接 Kafka に構造化イベントを送信しています。主な動機は、ログデータに触れる回数を減らし、ディスクの読み書きを何度も行うことを避けることでした。大量のボリュームのシステムでは、ロギングがアプリ自体より多くの仕事を必要とすることがあります。journald にも、C プログラムから直接ログを送信させることを検討しています。


### Loki

Loki に注目してください。まだ準備ができていませんが、準備ができたときには、このスタックにより適合するものになると期待しています。Loki は grafana labs が作成したログアグリゲーターで、Prometheus と同様のスクレイピングとタグの構文を使用します。


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 メトリクスには Prometheus + alertmanager。Prometheus が大好きです。

ロギング/エラー報告には Rollbar/Graylog(ここには重複があります。小規模なサービスなら、おそらく両方は必要ありません)。

現在、アラートは、関係者が通知をオンにしているいくつかの Slack チャンネルのいずれかに送られるだけです。オンコールにもっと真剣に取り組むなら、PagerDuty/VictorOps などに送られるでしょう。

グラフとダッシュボードには Grafana。また、彼らの近日公開予定のロギング機能が Graylog を不要にするかどうかを見るのも、楽しみにしています。


### Thanos

HA セットアップのフロントエンドとして Thanos を使用しています。HA ペアの重複を排除する方法を知っています。

現在、ローカルの Prometheus データを 6 か月分保持しています。これは私たちにとってそれなりにうまく機能しています。しかし、長期データストレージのために、Thanos セットアップにバケットストレージを導入している最中です。理論上、GCS ストレージは、現在使用している GCE 標準永続ディスクより約 30% 安くなります。

現時点では Prometheus のデータをバックアップしていません。アラートに十分な量があるという以上には、データは私たちにとってあまり重要ではないからです。私たちのフリート全体のデプロイメントは年々大きく変わるため、数か月より古い履歴データはそれほど興味深くありません。いくつかのコア統計を前年比で持つのは興味深いかもしれません。コア統計のレコーディングルールのセットを設定して、それらを Federation で保存するか、単に Thanos に任せてしまうかもしれません。

編集: 軽い開示ですが、私は Prometheus の開発者です。


### Prometheus HA

Prometheus での HA は、複製によって行われます。複数のコレクターを実行し、複数からポーリングしてデータの重複を排除する方法があります。

スケーリングは、ネットワークを決定し、異なる Prometheus にネットワークの異なる部分をポーリングさせることによって行われます。

長期ストレージは Prometheus の強みではなく、influx や timescaledb のようなものにオフロードされます(これは技術的には HA のチェックも満たします)。それについて読んだ記事 https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

まだ実験中で、短期のグラフに使っているだけで、長期のためには librenms がネットワークを監視しているため、長期の部分はまだ試していません


###  Datadog + PagerDuty + Threat Stack

私たちは Datadog(PagerDuty と併用)と Threat Stack を使っており、これ以上ないほど満足しています。DD に対する唯一の不満は、メトリクスストレージの比較的高いコストです。


### Zabbix

ほぼすべてを監視するカスタムスクリプトを備えた Zabbix。魔法のように機能します。


### Outlyer

私は Outlyer を使っていますが、ここで働いていることを明示しなければなりません。ドッグフーディングは必須です。

強化のために、まだ Graylog、Sentry、Statuscake が必要です。

偏っているように聞こえるかもしれませんが、Nagios やその他のモニタリングシステムを社内で喜んで運用してきた経験から、新しい職場では、ホスト型ソリューションを買って、その苦労を肩代わりしてもらうでしょう。


### Nagios + Nagiosgraph

すべてのモニタリングとアラートに Nagios を実行しています。アラートは、メール(警告と重大な通知)と、聞こえるアプリ通知(重大なアラート用)を通じて行われます。

可視化には Nagiosgraph が使用されます。

このセットアップは、環境で何が起きているかを包括的に把握し続けるのに非常に効果的でした。約 110 台のミッションクリティカルなサーバーと約 760 のデータポイントを実行・監視しており、この朝のシステムは 7 年以上稼働しています。

いつかは Graylog や ELk でログも集約したいと思っています。


### Prometheus + Grafana + AlertManager

素晴らしい Prometheus Operator の helm チャートによる Prometheus + Grafana + AlertManager。ログは、GKE 上の私たちのささやかな最小 3 最大 5 ノードには ELK が重すぎることに気づいたため、LogDNA の birch プランに送られています。


### DataDog + Sentry + PagerDuty.

以前は、Nagios、Icinga、Zabbix、ELK、Greylog2、Influx、その他多くのツールを含む、あらゆる種類のソフトウェアを使って、自分でモニタリングソリューションをすべて運用していましたが、実際のところ、自前のモニタリングインフラストラクチャを運用するのは、特に他の誰かにこれほど低い料金でやってもらえる場合には、あまりに多くの労力がかかります!

モニタリングインフラストラクチャの運用に他者に支払うことで、クライアントは、モニタリングをモニタリングする代わりに、プラットフォームの運用に集中できるようになります。つまり、プラットフォームの安定性から得られる価値は、サービスとしてのモニタリングのどんなコストよりもはるかに大きいのです。


### Sensu + Graphite + ELK

私の会社はセルフホストのものを大いに好んでいます。

Sensu -> PagerDuty

Graphite/Grafana

ELK(Elasticsearch、Logstash、Kibana)


### Prometheus + Alertmanager

アラートには Prometheus + Alertmanager。私のチームは、シンプルなモニタリングが良いモニタリングだと信じています。

ロギングやトレーシングなどの他のシステムは、オンコールの担当者がアラートを受け取ったときの診断に豊富なコンテキストを提供しますが、それらに基づくアラートは決して構築しません。


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu、grafana、graylog、kibana、newrelic。


### Prometheus + Circonus

Prometheus で計装されたサービス => Circonus の分析と可視化


### icinga2 + VictorOps + NewRelic + Sentry + Slack

次のサービスを使用しています:

モニタリングには icinga2、アラートには VictorOps

サービスの詳細なモニタリングには NewRelic

サービスのエラー追跡には Sentry

Slack/メールは、NewRelic または icinga2 からトリガーされるアラートの一部


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

分析のための elasticsearch 統合と、グラフのための graphite+grafana 統合を備えた icinga2。

icinga2 の apply ルールの柔軟性のおかげで、開発者は自分が通知を受け取るサービスだけを見ることができます。

また icinga2 director を通じて、プログラマーは自分のチェックを(数日おきに行っています。100 のチェックが出て、他の 100 のチェックが入ってきます)大規模に、手間なく簡単に定義できます。


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

現在持っているもの:

メトリクスには DataDog

アプリケーションモニタリングには New Relic

ログには ELK(Elastic Search + Logstash + Kibana)

例外のログ記録には Sentry(セルフホスト)

アラートにはメール + Slack + VictorOps(重大度に基づく)

持ちたいもの:

メトリクスには Prometheus(可視化には Grafana)

アプリケーションモニタリングには New Relic(おそらく Elastic Search APM)

ロギングには EFK(elastic search + fluentd + kibana)。おそらく、そこに到達する頃には Grafana の Loki が本番対応になっているでしょう

例外には Sentry

アラートには Alertmanager + メール + VictorOps


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack(開示: VMware 勤務)


### Telegraf + Prometheus + InfluxDB + Grafana

CPU、ディスク、メモリ、ネットワークなどのサーバーメトリクスには Telegraf。ネットワークデバイスの SNMP モニタリングにも Telegraf を使用しています。

アプリケーションメトリクスには Prometheus。Prometheus がスクレイプするヘルスチェックを、アプリケーションにコーディングしています。

時系列ストレージには InfluxDB。Telegraf のデータはここに送られます。

ダッシュボードとアラートには Grafana。アラートエンジンはそれほど堅牢ではありませんが、仕事はこなします。アラートは Slack にも送っています。

今のところ持っていないのは、一元化されたロギングソリューションです。ELK は強力ですが、セットアップと管理が難しく、調べてみるのに十分近い無料の代替品は知りません。


### Sematext + Logagent + Experience

メトリクス、ログ、トレース、そして近いうちにリアルユーザーモニタリングにも Sematext。N 個の異なるツール/サービスを使うよりもシンプル/安価だと私は思います。

ログの転送には以前 rsyslog を使っていましたが、その後 Logagent に切り替えました。

フロントエンドのクラッシュ報告には Sentry を使っていますが、まもなく Experience に切り替えます。

開示: 私は Sematext の社員です。


### Azure Monitor/Analytics + OpsGenie

Log Analytics のインターフェースがもっと良ければと思います。はるかにナビゲートしやすかった splunk から移行しているところです。


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus、Alertmanager、Grafana、Splunk、PagerDuty

自前の通知システムを運用したいとは本当に思わないはずです。セキュリティチームが Splunk を好まない限り、Splunk を ELK に置き換えることもできます。


### Telegraf + Prometheus + Grafana + Alertmanager

コレクターとして Telegraf、モニタリングとアラートに Prometheus + Alertmanager、重大なアラートには slack チャンネルと pagerduty と統合。ホストメトリクスの可視化には Grafana。


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

メトリクス + アラートには Prometheus

Prometheus のダッシュボードには Grafana

Prometheus インスタンスを監視する Cloudwatch

例外追跡には sentry

kibana + elasticsearch

graylog

バッチ/cronjob には prometheus Push Gateway

1 つの Prometheus インスタンスから別のインスタンスへメトリクスを「プッシュ/転送」するための SOP https://github.com/rapidloop/sop

クライアントは Prometheus クライアントを使用します。クライアント側では opencensus.io を使うようにしています


### PagerDuty + Monitis

PagerDuty + Monitis。また、一部のサービスの健全性をテストするための、いくつかのオーダーメイドの Azure Functions。

今年、Prometheus と Grafana の導入を期待しています


### Prometheus + Grafana + Bosun

時系列データを保存するための Prometheus。可視化のための Grafana。アラート管理のための Bosun。


### Azure Monitor/Analytics/Insights/Dashboards

Azure のみの店。Azure Monitor、Log Analytics、App Insights、Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Prometheus を介して Kubernetes のコンテナサービスを監視するための Grafana

主に Web API と Web アプリケーションのエンドツーエンドのサービス監視のための Monitis

アラート管理のための OpsGenie

システムからステータス情報を得るための Slack


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

長年の(dev)ops エンジニアです。Nagios で育ちました。自力で立ち上げた SaaS https://checklyhq.com について、ご意見をいただけると嬉しいです。私たちは、かなり詳細なアラートを備えた API モニタリングとサイトトランザクションモニタリングを行っています。

Checkly を始めたのは、API 分野でのアクティブ/合成モニタリングが少し限られていて(そして高価)だったからです。ブラウザベース/スクリプト化されたモニタリングは、さらに独自仕様で高価です。私たちは Puppeteer を使用し、価格をできるだけ低く保っています。

私たちのモニタリングスタック:

Checkly(ドッグフーディング...)

AppOptics(カスタムグラフ作成)

SMS メッセージのための AWS Cloudwatch と SNS。

組み込みの Heroku アラート。

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana はインフラストラクチャの問題やパフォーマンスの低下について slack でアラートを出してくれます。また、アプリケーション層からのエラーレベルのログが一定量に達したときに slack でアラートを出すよう、logz.io を設定しています。


### SignalFX + Splunk + PagerDuty + Slack

現在使用中: SignalFX、Splunk、PagerDuty、Slack。SignalFX のサポートチームは非常にフレンドリーで迅速に対応してくれますが、私は SignalFX の大ファンではありません。Splunk(支払えるなら価値あり)、PagerDuty、Slack は好きです。

以前は TICK スタックを使っていました。その C は実際には G、つまり Grafana でしたが、Chronograf も少し使いました。素晴らしかったですが、管理は面倒でした。典型的な SaaS 対セルフホスティングのジレンマです。

DataDog、New Relic、Graylog、ELK、BugSnag を使ってきました。DataDog と New Relic は大好きで、Graylog もかなり良いです。ELK は大ファンではありません。BugSnag は良く、多くの場合、エラー/例外の追跡は完全なログモニタリングのかなり良い代用になると実際に感じています。


### ELK + Prometheus + Grafana

他の人と同じく、ログには ELK、それ以外のすべてには Prometheus+Grafana を使用しています。

このセットアップの保守は、たまにデータを失うことを許容すれば簡単です。たとえば、ElasticSearch データベースが不調になった場合(残念ながら私たちは 2〜3 か月ごとに起きます)、HA に煩わされず、代わりにデータを捨てて人生を先に進めます。どうしても HA や長期保存が必要なら、幸運を祈ります。


### Datadog + Prometheus + Grafana

ここに来たときモニタリングもアラートもなかったため、Datadog を月単位で設定しました。サイトの数件だけが、5 分ごとの稼働時間監視を受けていました。Datadog は間違いなく最もセットアップが簡単です。他のすべての問題に対処し終えたら、Prometheus+Grafana に切り替えます。ログ管理についてはまだ 100% 決めていません。

### Nagios + ELK

私たちは 100 以上の製品をサポートしています。

オンプレミスでは、ほとんどが Nagios と ELK です。クラウドでは、DataDog から NewRelic へ移行中です。


### Datadog 対 Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

以前は datadog を使っていましたが、私たちのニーズにはあまりにも高価だと分かりました。誤解しないでください。素晴らしいのですが、莫大なコストがかかります。DD の 2〜3 か月分のコストで、年間サブスクリプションの site24x7.com をセットアップできました。

私たちのモニタリングスタック:

Site24x7 - APM、外部 URL モニタリング、SMTP メールフローモニタリング、ssl の有効期限、プロセスモニタリング。

StatusCake - URL モニタリングと確認用 - site24x7 が何かを見逃した場合の備え(見逃しませんが)ですが、SC は私たちのニーズにおいて外部ポートやサービスのモニタリングにより柔軟です。

どちらのツールも PagerDuty にエスカレーションし、その後エスカレーションを slack で受け取ります。

SumoLogic - ログモニタリング用(素晴らしいツールですが、私たちのニーズには少し複雑です)

slack から、アラートを確認(ack)したり、修復したりできます。

その後、私たちが「BedOps」と呼ぶもののために commando.io に接続する、多くの site24x7 の自動化があります。アラートがトリガーされると、状況を修復する試みとしていくつかのスクリプトや自動化を起動します(99% の場合、自動化 + 私たちのスクリプトが私たちを問題から遠ざけてくれます)。

自動化が失敗した場合や、範囲外で修正が必要なものがある場合のために、KB に社内ランブックがあります。


### Prometheus + AlertManager + Grafana + Stackdriver

GKE クラスターと VM のメトリクスには Prometheus(Operator)/ AlertManager / Grafana。

ログには Google Stackdriver(含まれていてデフォルトで有効であり、現在のところ私たちのニーズに十分だからです)。


### Zabbix

すべてに Zabbix。追加のソフトウェアは不要です。
