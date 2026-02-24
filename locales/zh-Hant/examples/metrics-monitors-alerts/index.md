# 指標、監控、警報（Metrics, Monitors, Alerts）

目錄：

* [摘要](#摘要)
  * [議題](#議題)
  * [決策](#決策)
  * [狀態](#狀態)
* [細節](#細節)
  * [假設](#假設)
  * [限制條件](#限制條件)
  * [立場](#立場)
  * [論點](#論點)
  * [影響](#影響)
* [相關資訊](#相關資訊)
  * [相關決策](#相關決策)
  * [相關需求](#相關需求)
  * [相關產出物](#相關產出物)
  * [相關原則](#相關原則)
* [備註](#備註)
  * [自由格式文字訊息 vs 結構化事件訊息](#自由格式文字訊息-vs-結構化事件訊息)
  * [Graylog 更容易使用](#graylog-更容易使用)
  * [Prometheus 需要一些調校](#prometheus-需要一些調校)
  * [AWS 服務好壞參半](#aws-服務好壞參半)
  * [Kafka](#kafka)
  * [Loki](#loki)
  * [Prometheus + alertmanager + Rollbar + Graylog + Grafana](#prometheus-alertmanager-rollbar-graylog-grafana)
  * [Thanos](#thanos)
  * [Prometheus HA](#prometheus-ha)
  * [Datadog + PagerDuty + Threat Stack](#datadog-pagerduty-threat-stack)
  * [Zabbix](#zabbix)
  * [Outlyer](#outlyer)
  * [Nagios + Nagiosgraph](#nagios-nagiosgraph)
  * [Prometheus + Grafana + AlertManager](#prometheus-grafana-alertmanager)
  * [DataDog + Sentry + PagerDuty](#datadog-sentry-pagerduty)
  * [Sensu + Graphite + ELK](#sensu-graphite-elk)
  * [Prometheus + Alertmanager](#prometheus-alertmanager)
  * [Sensu + Grafana + Graylog + Kibana + NewRelic](#sensu-grafana-graylog-kibana-newrelic)
  * [Prometheus + Circonus](#prometheus-circonus)
  * [icinga2 + VictorOps + NewRelic + Sentry + Slack](#icinga2-victorops-newrelic-sentry-slack)
  * [AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver](#appdynamics-papertrail-pagerduty-healthchecks-io-stackdriver)
  * [icinga2 + elasticsearch](#icinga2-elasticsearch)
  * [DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps](#datadog-new-relic-elk-efk-sentry-alertmanager-victorops)
  * [Wavefront + Scalyr + PagerDuty + Stackstorm + Slack](#wavefront-scalyr-pagerduty-stackstorm-slack)
  * [Telegraf + Prometheus + InfluxDB + Grafana](#telegraf-prometheus-influxdb-grafana)
  * [Sematext + Logagent + Experience](#sematext-logagent-experience)
  * [Azure Monitor/Analytics + OpsGenie](#azure-monitor-analytics-opsgenie)
  * [Prometheus + Alertmanager + Grafana + Splunk + PagerDuty](#prometheus-alertmanager-grafana-splunk-pagerduty)
  * [Telegraf + Prometheus + Grafana + Alertmanager](#telegraf-prometheus-grafana-alertmanager)
  * [Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch](#prometheus-grafana-cloudwatch-sentry-kibana-elasticsearch)
  * [PagerDuty + Monitis](#pagerduty-monitis)
  * [Prometheus + Grafana + Bosun](#prometheus-grafana-bosun)
  * [Azure Monitor/Analytics/Insights/Dashboards](#azure-monitor-analytics-insights-dashboards)
  * [Grafana + Monitis + OpsGenie + Slack](#grafana-monitis-opsgenie-slack)
  * [Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail](#checkly-appoptics-cloudwatch-heroku-pagerduty-papertrail)
  * [Instana + Logz.io + slack](#instana-logz-io-slack)
  * [SignalFX + Splunk + PagerDuty + Slack](#signalfx-splunk-pagerduty-slack)
  * [ELK + Prometheus + Grafana](#elk-prometheus-grafana)
  * [Datadog + Prometheus + Grafana](#datadog-prometheus-grafana)
  * [Nagios + ELK](#nagios-elk)
  * [Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack](#datadog-vs-site24x7-statuscake-pagerduty-sumologic-slack)
  * [Prometheus + AlertManager + Grafana + Stackdriver](#prometheus-alertmanager-grafana-stackdriver)
  * [Zabbix](#zabbix)


## 摘要


### 議題

我們希望使用指標（Metrics）、監控（Monitors）和警報（Alerts），因為我們想知道應用程式運作的狀況，以及何時出現問題。


### 決策

進行中（WIP）。


### 狀態

正在蒐集資訊。我們從光譜的兩端開始：最受推薦的較舊免費工具（Nagios）和最受推薦的較新付費工具（New Relic）。


## 細節


### 假設

我們希望建構現代、快速、可靠、響應式等特性的網頁應用程式。

我們傾向購買而非自建。


### 限制條件

我們希望工具能夠與我們的 DevOps 管線和部署雲端良好配合。


### 立場

我們目前正在研究各方立場。


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


### 論點

目前，Nagios 和 New Relic 是光譜的兩端。Nagios 是最古老、最簡單、免費且可行的工具。New Relic 是功能最新、最完整、付費且可行的工具。我們將從這兩者的評估開始。如有需要，我們將向光譜中間探索。

目前，Zabbix 擁有最好的推薦，同時也提供最完整的功能。

目前，ELK 在開源的自建方案中擁有最高的人氣。

目前，Prometheus + Grafana 擁有最高的人氣。


### 影響

待定（TODO）。


## 相關資訊


### 相關決策

選擇將影響可測試性（Testability）、遙測（Telemetry），以及其他系統，例如客戶服務、網站可靠性工程（Site Reliability Engineering）等。


### 相關需求

待定（TODO）。


### 相關產出物

待定（TODO）。


### 相關原則

容易復原（Easily Reversible）。

追求速度（Need for Speed）。


## 備註


一個相當不錯的開源技術堆疊（Stack）是：

* Prometheus 用於指標和基於指標的警報

* Grafana 用於顯示指標

* Elasticsearch/Logstash/Kibana（ELK）用於日誌和結構化事件

* Pushover 用於行動裝置通知


### 自由格式文字訊息 vs 結構化事件訊息

自由格式文字訊息：例如，你在 /var/log/messages 中會找到的那種隨機內容，以及應用程式刻意產生的訊息。這些訊息對於識別主機上發生的其他事情（如記憶體不足或硬體錯誤）很有用，但包含很多雜訊。

結構化事件訊息：由應用程式產生，具有固定或動態的屬性集合，例如 HTTP 請求日誌、會計日誌、使用者登入紀錄。

一般來說，以可根據屬性向下鑽取的方式記錄每個請求的詳細資訊是很好的做法。例如，在所有紀錄中加入使用者 ID 或會話 ID（Session ID）讓你能夠追蹤。明確的追蹤（Tracing）當然也很好。使用 ELK 來做這件事可以算是簡易版的 https://www.honeycomb.io/


### Graylog 更容易使用

根據我的經驗，Graylog 更容易啟動運行。



### Prometheus 需要一些調校


對於指標方面，我對 Prometheus 大致滿意。警報需要一些調校，但效果相當好。這取決於你的應用程式。我認為最好針對終端使用者可見的狀況進行警報，而不是底層原因。例如，頁面載入時間是好的指標，每秒請求數則不是。不過每秒零請求確實表示有問題。

服務的優勢在於它們開箱即提供額外的智慧分析。我大致上喜歡 Datadog。如果你有大量資料，這些服務的費用可能高得嚇人，有時定價模式不太適合雲端，例如按實例收費，而實例是動態的。此外，來自付費使用者的每個請求的服務與廣告相關的服務之間也有差異，後者只有一小部分請求能為你帶來收入。你可能會有大量資料但預算不多。

我負責的一些服務每天接收 10 億個請求，所以自行託管監控和日誌是合理的。如果你的量較低，託管服務會更容易。


### AWS 服務好壞參半

我使用 AWS 服務的經驗好壞參半。他們的 Elasticsearch 服務不太穩定，所以我們自行運行實例。CloudWatch 指標很貴，所以我們通常只將它們用於「基礎設施」層級的指標，而不是應用程式層級，即 AWS 比在實例上運行的軟體更能了解狀況的健康相關指標。CloudWatch Logs 更新可能很慢，且中繼資料不多。運行 ELK 有助於解決這個問題。如果我真的需要即時資料，使用 Kafka 作為日誌傳輸層更好。Logstash 對此有很好的支援。不過管理 Kafka 叢集不是件容易的事，有很多需要處理的管線細節。


### Kafka

評論：Kafka 有時可能超級棘手，或者 Kafka 可以非常穩固，讓你幾乎忘記它在那裡把所有東西串在一起。


評論：Kafka 一直很穩固，但讓它運行起來花了驚人的工作量。我把它想成是關聯式資料庫，但你只在「實體」層操作，例如表空間、檔案和分割區。早期有些時候管理工具不足，我們不得不自己寫程式來重設消費者群組（Consumer Group）。http://howfuckedismydatabase.com/nosql/

評論：我們使用 Kafka 作為日誌訊息的「緩衝區」，以及一個可以對來自多台伺服器的資料進行即時串流處理的地方。如果遭受 DDoS 攻擊，我們需要一種跨多個實例分析資料的方法。如果直接從伺服器記錄到 ELK，負載可能會壓垮 Elasticsearch 叢集。

評論：Kafka 對我們很有用，因為如果遭受 DDoS 攻擊，我們需要一種跨多個實例分析資料的方法。如果直接從伺服器記錄到 ELK，負載可能會壓垮 Elasticsearch 叢集。


評論：Kafka 做的事情更少且更有效率，所以能更好地處理負載。我們將 Kafka 的工作排入佇列並重試。而且 Kafka 過載不會影響嘗試使用 Kibana 進行互動查詢的使用者，但如果 Elasticsearch 在掙扎就會有影響。

評論：串流處理主要是尋找濫用行為，例如整個叢集中來自單一 IP 的過多流量，然後在整個叢集中共享封鎖。

評論：目前 logstash-output-kafka 外掛相當不穩定。我遇到了其 GitHub Issues 頁面上的好幾個問題，而且似乎一直沒有修復。我想停止使用它，改為從應用程式直接發送到 Kafka。

評論：我們現在從應用程式直接將結構化事件發送到 Kafka。主要動機是減少接觸日誌資料的次數，避免多次讀寫磁碟。在高流量系統中，日誌記錄可能比應用程式本身需要更多的工作量。我正在考慮讓 journald 也直接發送日誌，透過一個 C 程式。


### Loki

密切關注 Loki。它還沒準備好，但當它準備好時，我預期它會更適合這個技術堆疊。Loki 是 Grafana Labs 建立的日誌聚合器，使用與 Prometheus 類似的抓取和標籤語法。


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

Prometheus + alertmanager 用於指標。超愛 Prometheus。

Rollbar/Graylog 用於日誌/錯誤報告（這裡有些重疊；小型服務可能不需要兩者都用）。

目前，警報只發送到幾個 Slack 頻道，相關人員已開啟通知。如果我們更認真地看待值班（On-Call），它們會發送到 PagerDuty/VictorOps 等。

Grafana 用於圖表和儀表板。也熱切期待看看他們即將推出的日誌功能是否能取代 Graylog。


### Thanos

我們使用 Thanos 作為 HA 設置的前端。它知道如何對 HA 配對進行去重複化。

我們目前保留 6 個月的本地 Prometheus 資料。這對我們來說運作得相當好。但我正在為 Thanos 設置部署物件儲存（Bucket Storage）以用於長期資料儲存。理論上，GCS 儲存將比我們目前使用的 GCE 標準持久磁碟便宜約 30%。

我們目前不備份 Prometheus 資料。這些資料對我們來說除了用於警報之外並不那麼重要。我們的整體機群部署每年變化很大，超過幾個月的歷史資料就不太有趣了。保留幾個核心統計資料的年度對比可能會有趣，我可能會設置一組核心統計記錄規則（Recording Rules），並透過聯邦（Federation）儲存，或者就讓 Thanos 處理。

編輯：小聲明，我是 Prometheus 開發者。


### Prometheus HA

Prometheus 的 HA 透過複製來實現——你運行多個 Prometheus 實例，有方法可以輪詢多個並去重複化資料。

擴展是透過劃分網路，讓不同的 Prometheus 輪詢網路的不同部分。

長期儲存不是 Prometheus 的強項，但可以卸載到 InfluxDB 或 TimescaleDB（技術上也能滿足 HA 的要求）。我讀到的一篇文章：https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

我還沒嘗試長期儲存的部分，因為我仍在實驗中，使用 LibreNMS 監控我的網路用於長期圖表。


### Datadog + PagerDuty + Threat Stack

我們使用 Datadog（搭配 PagerDuty）和 Threat Stack，非常滿意。我對 DD 唯一的抱怨是指標儲存的成本相對較高。


### Zabbix

使用 Zabbix 搭配自訂腳本來監控幾乎所有東西。運作得非常好。


### Outlyer

我在用 Outlyer，但我必須聲明我在這裡工作，吃自己的狗糧（Dog Fooding）是必須的。

仍然需要 Graylog、Sentry 和 Statuscake 來增強功能。

聽起來有偏見，但在內部愉快地運行 Nagios 和其他監控系統之後，在任何新工作中我都會購買託管解決方案來卸除那些痛苦。


### Nagios + Nagiosgraph

我們使用 Nagios 進行所有監控和警報。警報透過電子郵件（警告和嚴重通知）和有聲應用程式通知（嚴重警報）發送。

Nagiosgraph 用於視覺化。

這個設置在讓我們全面了解環境中發生的事情方面非常有效。我們運行並監控大約 110 台關鍵任務伺服器和大約 760 個資料點，這個監控系統已經運作超過七年。

我想在某個時候也用 Graylog 或 ELK 來聚合日誌。


### Prometheus + Grafana + AlertManager

透過出色的 Prometheus Operator Helm Chart 使用 Prometheus + Grafana + AlertManager。日誌仍然傳送到 LogDNA birch 方案，因為我們注意到 ELK 對於我們在 GKE 上最少 3 個最多 5 個節點的規模來說太重了。


### DataDog + Sentry + PagerDuty

我過去曾使用各種軟體運行自己所有的監控解決方案，包括 Nagios、Icinga、Zabbix、ELK、Greylog2、InfluxDB 和許多其他工具，但事實是，運行自己的監控基礎設施需要太多精力，特別是當你可以用如此低的費率付費讓別人來做的時候！

付費讓別人運行監控基礎設施，能讓我的客戶專注於運行他們的平台，而不是監控監控系統，這意味著他們從平台穩定性中獲得的價值遠超過監控即服務（Monitoring as a Service）的任何成本。


### Sensu + Graphite + ELK

我的公司非常重視自行託管的方案。

Sensu -> PagerDuty

Graphite/Grafana

ELK（Elasticsearch、Logstash、Kibana）


### Prometheus + Alertmanager

Prometheus + Alertmanager 用於警報，我的團隊相信簡單的監控就是好的監控。

其他系統如日誌和追蹤會在值班人員收到警報時提供豐富的診斷上下文，但我們從不基於這些系統建立警報。


### Sensu + Grafana + Graylog + Kibana + NewRelic

Sensu、Grafana、Graylog、Kibana、NewRelic。


### Prometheus + Circonus

Prometheus 探測服務 => Circonus 分析和視覺化


### icinga2 + VictorOps + NewRelic + Sentry + Slack

我們使用以下服務：

icinga2 用於監控，VictorOps 用於警報

NewRelic 用於服務的詳細監控

Sentry 用於服務中的錯誤追蹤

Slack/Email 是警報的一部分，由 NewRelic 或 icinga2 觸發


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 搭配 elasticsearch 整合用於分析，以及 graphite+grafana 整合用於圖表。

感謝 icinga2 中靈活的套用規則（Apply Rules），開發者只能看到他們收到通知的服務。

透過 icinga2 director，程式設計師可以輕鬆地大規模定義自己的檢查（他們確實這樣做，每隔幾天就有 100 個檢查退出、100 個新檢查加入），完全沒有麻煩。


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

我們目前有什麼：

DataDog 用於指標

New Relic 用於應用程式監控

ELK（Elasticsearch + Logstash + Kibana）用於日誌

Sentry（自行託管）用於記錄例外

Emails + Slack + VictorOps 用於警報（根據嚴重程度）

我們想要什麼：

Prometheus 用於指標（Grafana 用於視覺化）

New Relic（可能是 Elasticsearch APM）用於應用程式監控

EFK（Elasticsearch + Fluentd + Kibana）用於日誌。可能等我們到這步時，Grafana 的 Loki 就已經能用於正式環境了

Sentry 用於例外

Alertmanager + email + VictorOps 用於警報


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack（聲明：在 VMware 工作）


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf 用於伺服器指標，如 CPU、磁碟、記憶體和網路。我們也使用 Telegraf 進行網路設備的 SNMP 監控。

Prometheus 用於應用程式指標。我們在應用程式中編寫健康檢查，由 Prometheus 抓取。

InfluxDB 用於時間序列儲存。這是我們的 Telegraf 資料傳送的目的地。

Grafana 用於儀表板和警報。警報引擎不是特別強大，但能完成工作。我們也將警報發送到 Slack。

我目前沒有的是集中式日誌解決方案。ELK 功能強大但難以設置和管理，我不知道有哪些免費替代方案足夠接近值得研究。


### Sematext + Logagent + Experience

Sematext 用於指標、日誌、追蹤，很快也會用於真實使用者監控（Real User Monitoring）。比使用 N 種不同的工具/服務更簡單/更便宜，這是我的看法。

日誌傳送方面，我們過去使用 rsyslog，後來切換到 Logagent。

前端崩潰報告方面，我們使用 Sentry，但很快會切換到 Experience。

聲明：我是 Sematext 的成員。


### Azure Monitor/Analytics + OpsGenie

我希望 Log Analytics 有更好的介面。我們正在從 Splunk 遷移，Splunk 的導航要容易得多。


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus、Alertmanager、Grafana、Splunk、PagerDuty

你真的不想自己運行通知系統。你可以用 ELK 替換 Splunk，除非你的資安團隊偏好 Splunk。


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf 作為收集器，Prometheus + Alertmanager 用於監控和警報，與 Slack 頻道和 PagerDuty 整合用於嚴重警報。Grafana 用於主機指標視覺化。


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus 用於指標 + 警報

Grafana 用於 Prometheus 儀表板

Cloudwatch 監控 Prometheus 實例

Sentry 用於例外追蹤

Kibana + Elasticsearch

Graylog

Prometheus Push Gateway 用於批次/排程任務（Cronjob）

SOP https://github.com/rapidloop/sop 用於在不同 Prometheus 實例之間「推送/轉發」指標

客戶端使用 Prometheus 客戶端。我們嘗試在客戶端使用 opencensus.io


### PagerDuty + Monitis

PagerDuty + Monitis。另外還有一些自訂的 Azure Functions 用於測試某些服務的健康狀態。

計畫今年引入 Prometheus 和 Grafana


### Prometheus + Grafana + Bosun

Prometheus 用於儲存時間序列資料。Grafana 用於視覺化。Bosun 用於警報管理。


### Azure Monitor/Analytics/Insights/Dashboards

純 Azure 商店，Azure Monitor、Log Analytics、App Insights、Azure Dashboards + PagerDuty


### Grafana + Monitis + OpsGenie + Slack

Grafana 用於透過 Prometheus 監控 Kubernetes 中的容器服務

Monitis 用於端對端服務監控，主要針對 Web API 和 Web 應用程式

OpsGenie 用於警報管理

Slack 用於從我們的系統取得狀態資訊


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

資深的（Dev）Ops 工程師在此。從 Nagios 時代成長過來。很想聽聽大家對我的 SaaS https://checklyhq.com 的看法。我們做 API 監控和網站交易監控，有相當深入的警報功能。

我創立 Checkly 是因為 API 領域的主動/合成監控（Active / Synthetic Monitoring）有點受限（而且很貴）。基於瀏覽器的/腳本化的監控更是專有且昂貴。我們使用 Puppeteer 並盡可能壓低價格。

我們的監控堆疊：

Checkly（吃自己的狗糧...）

AppOptics（自訂圖表）

AWS Cloudwatch & SNS 用於簡訊。

內建 Heroku 警報。

PagerDuty

Papertrail


### Instana + Logz.io + slack

Instana 在 Slack 中提醒我們基礎設施問題或效能下降，我們也設定了 logz.io 在應用程式層出現一定量的錯誤級別日誌時在 Slack 中發出警報。


### SignalFX + Splunk + PagerDuty + Slack

目前使用：SignalFX、Splunk、PagerDuty 和 Slack。我不是 SignalFX 的超級粉絲，雖然他們的支援團隊非常友善且反應迅速。我喜歡 Splunk（如果你付得起的話值得）、PagerDuty 和 Slack。

我過去使用 TICK 堆疊，其中大部分的 C 實際上是 G（即 Grafana），雖然我也用了一點 Chronograf。那很棒，但管理起來很痛苦。經典的 SaaS vs 自行託管困境。

我用過 DataDog、New Relic、Graylog、ELK 和 BugSnag。我非常喜歡 DataDog 和 New Relic，Graylog 相當不錯。我不是 ELK 的忠實粉絲。BugSnag 很好，我實際上覺得在很多情況下，追蹤錯誤/例外是全面日誌監控的一個相當好的替代方案。


### ELK + Prometheus + Grafana

和其他人一樣，我們使用 ELK 處理日誌，使用 Prometheus+Grafana 處理其他一切。

如果你允許自己偶爾丟失資料，維護這個設置是很容易的。例如，如果我們的 Elasticsearch 資料庫出問題了（不幸的是每 2-3 個月就會發生），我們不費心做 HA，而是清除資料然後繼續過日子。如果你絕對必須要有 HA 或長期保留，祝你好運。


### Datadog + Prometheus + Grafana

我按月設置了 Datadog，因為我到這裡的時候，沒有監控也沒有警報。我們只有幾個網站每 5 分鐘監控一次正常運行時間。Datadog 毫無疑問是最容易設置的。當我解決完所有其他問題後，我會切換到 Prometheus+Grafana。日誌管理方面還沒有 100% 決定。

### Nagios + ELK

我們支援超過 100 多個產品。

對於地端（On-Prem），主要是 Nagios 和 ELK。對於雲端，我們正在從 DataDog 遷移到 NewRelic。


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

我們過去使用 Datadog，但發現對我們的需求來說太貴了。別誤會，它很棒，但確實成本很高。我們用大約 DD 2-3 個月的費用就設置好了 site24x7.com 的年度訂閱。

我們的監控堆疊：

Site24x7 - APM、外部 URL 監控、SMTP 郵件流監控、SSL 到期和程序監控。

StatusCake - 用於 URL 監控和確認——它是我們的備份，以防 site24x7 遺漏什麼（實際上不會），但 SC 在外部埠和服務監控方面對我們的需求更靈活。

兩個工具都升級到 PagerDuty，然後我們在 Slack 中收到升級通知。

SumoLogic - 用於日誌監控（它是個很好的工具，但對我們的需求來說有點複雜）

從 Slack 中我們可以確認（Ack）或修復警報。

然後我們有很多 site24x7 自動化，連接到 commando.io 做我們稱之為 'BedOps' 的工作——當警報觸發時，我們啟動一些腳本或自動化嘗試修復狀況（99% 的時間自動化加上我們的腳本讓我們免於麻煩）

我們的知識庫中有內部 Runbook，用於自動化失敗或有超出範圍需要修復的情況。


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus（Operator）/ AlertManager / Grafana 用於我們 GKE 叢集和 VM 中的指標。

Google Stackdriver 用於日誌（因為它預設就已包含且啟用，目前足夠我們的需求）。


### Zabbix

Zabbix 用於所有事情。不需要額外的軟體。
