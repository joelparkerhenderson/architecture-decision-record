# मेट्रिक, मॉनिटर, अलर्ट

सामग्री:

* [सारांश](#सारांश)
  * [समस्या](#समस्या)
  * [फैसला](#फैसला)
  * [स्थिति](#स्थिति)
* [ब्योरा](#ब्योरा)
  * [मान्यता](#मान्यता)
  * [बंदिश](#बंदिश)
  * [रुख](#रुख)
  * [तर्क](#तर्क)
  * [असर](#असर)
* [संबंधित](#संबंधित)
  * [संबंधित फैसला](#संबंधित-फैसला)
  * [संबंधित जरूरत](#संबंधित-जरूरत)
  * [संबंधित आर्टिफैक्ट](#संबंधित-आर्टिफैक्ट)
  * [संबंधित सिद्धांत](#संबंधित-सिद्धांत)
* [टिप्पणी](#टिप्पणी)
  * [मुक्त पाठ संदेश बनाम संरचित इवेंट संदेश](#मुक्त-पाठ-संदेश-बनाम-संरचित-इवेंट-संदेश)
  * [Graylog जादा आसान बा](#graylog-जादा-आसान-बा)
  * [Prometheus के कुछ ट्यूनिंग चाहीं](#prometheus-के-कुछ-ट्यूनिंग-चाहीं)
  * [AWS सेवा मिश्रित बाड़ी](#aws-सेवा-मिश्रित-बाड़ी)
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
  * [Zabbix](#zabbix-1)


## सारांश


### समस्या

हमनी मेट्रिक, मॉनिटर, आ अलर्ट इस्तेमाल करे चाहत बानी, काहेकि हमनी जानल चाहत बानी कि हमनी के एप्लिकेशन केतना नीमन काम कर रहल बा, आ कब कवनो समस्या बा।


### फैसला

WIP।


### स्थिति

जानकारी जुटावल जा रहल बा। हमनी स्पेक्ट्रम के संभावित छोर से शुरू कर रहल बानी: सबसे जादा सिफारिश कइल गइल पुरान मुफ्त औजार (Nagios) आ सबसे जादा सिफारिश कइल गइल नया भुगतान वाला औजार (New Relic)।


## ब्योरा


### मान्यता

हमनी आधुनिक, तेज, भरोसेमंद, प्रतिक्रियाशील, वगैरह वेब एप्लिकेशन बनावे चाहत बानी।

हमनी बनावे के बजाय खरीदे चाहत बानी।


### बंदिश

हमनी अइसन औजार चाहत बानी जे हमनी के devops पाइपलाइन आ हमनी के डिप्लॉयमेंट क्लाउड संगे नीमन से काम करेला।


### रुख

हमनी अबहिन रुख पर शोध कर रहल बानी।


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

  

  
### तर्क

अब तक, Nagios आ New Relic स्पेक्ट्रम के छोर बा। Nagios सबसे पुरान, सबसे सादा, मुफ्त, व्यावहारिक औजार ह। New Relic सबसे नया फीचर वाला, सबसे पूरा, भुगतान वाला, व्यावहारिक औजार ह। हमनी एकरा के मूल्यांकन से शुरू करब। जरूरत पड़ला पर, हमनी स्पेक्ट्रम के भीतर जाइब।  

अब तक, Zabbix लग सबसे नीमन सिफारिश बा, आ सबसे पूरा क्षमता भी देला।

अब तक, ELK लग सबसे नीमन ओपन-सोर्स बनाम-खरीद लोकप्रियता बा।

अब तक, Prometheus + Graphana लग सबसे नीमन लोकप्रियता बा।


### असर

TODO।


## संबंधित


### संबंधित फैसला

ई चुनाव जाँचे-लायकता, टेलीमेट्री, आ संभव बा आउर प्रणाली जइसे ग्राहक सेवा, साइट भरोसेमंदी इंजीनियरिंग, वगैरह पर असर डाली।


### संबंधित जरूरत

TODO।


### संबंधित आर्टिफैक्ट

TODO।


### संबंधित सिद्धांत

आसानी से पलटे-लायक।

तेजी के जरूरत।


## टिप्पणी

एगो काफी नीमन ओपन सोर्स स्टैक ई बा:

* मेट्रिक आ मेट्रिक पर आधारित अलर्टिंग खातिर Prometheus

* मेट्रिक देखावे खातिर Grafana

* लॉग आ संरचित इवेंट खातिर Elasticsearch/Logstash/Kibana (ELK)

* मोबाइल सूचना खातिर Pushover


### मुक्त पाठ संदेश बनाम संरचित इवेंट संदेश

मुक्त पाठ संदेश: उदाहरण खातिर, ऊ बेतरतीब चीज जे रउआ /var/log/messages में पाइब, आ एप्लिकेशन द्वारा जानबूझ के बनावल चीज। ई संदेश बक्सा पर होखे वाली आउर चीज, जइसे मेमोरी खतम भइल चाहे हार्डवेयर गलती, के पहचाने खातिर उपयोगी बा, लेकिन एमे बहुत कचरा बा। 

संरचित इवेंट संदेश: एप्लिकेशन द्वारा बनावल, गुण के तय चाहे गतिशील सेट संगे, जइसे HTTP अनुरोध लॉग, लेखा लॉग, उपयोगकर्ता लॉगिन।

आम तौर पर कहल जाय त, हर अनुरोध के ब्योरा अइसन तरी से लॉग कइल बढ़िया बा कि रउआ गुण के आधार पर गहराई में जा सकीले। एहसे हर चीज में जइसे userid चाहे sessionid जोड़ला से रउआ ट्रेस कर सकीले। साफ ट्रेसिंग भी बढ़िया बा, जरूर। एकरा खातिर ELK इस्तेमाल करल https://www.honeycomb.io/ के गरीब आदमी के संस्करण जइसन बा


### Graylog जादा आसान बा

हमरा अनुभव में Graylog चालू करे में जादा आसान बा।


### Prometheus के कुछ ट्यूनिंग चाहीं

हम आम तौर पर मेट्रिक खातिर Prometheus से खुश बानी। अलर्टिंग के कुछ ट्यूनिंग चाहीं, लेकिन काफी नीमन बा। ई रउआ एप्लिकेशन पर निर्भर करेला। हमरा खयाल में अंतर्निहित कारन के बजाय अंतिम-उपयोगकर्ता के दिखे वाली स्थिति पर अलर्ट करल सबसे नीमन बा। उदाहरण खातिर, पन्ना लोड समय बढ़िया बा, प्रति सेकंड अनुरोध के संख्या ना। हालांकि प्रति सेकंड शून्य अनुरोध बतावेला कि कुछ गलत बा।

सेवा के फायदा ई बा कि ऊ बाक्स से बाहर अतिरिक्त बुद्धिमत्ता देवेली। हमके आम तौर पर Datadog पसंद बा। अगर रउआ लग बहुत डेटा बा त सेवा डरावना रूप से महंगा हो सकेली, आ कबो-कबो अइसन कीमत मॉडल होला जे क्लाउड-अनुकूल नइखे, जइसे प्रति इंस्टेंस पइसा लेवल, जबकि इंस्टेंस गतिशील होला। ओह सेवा के बीच भी अंतर बा जहाँ हर अनुरोध भुगतान करे वाला उपयोगकर्ता से बा आ ओह सेवा के बीच जे विज्ञापन-संबंधी बा, जेमें अनुरोध के बस कुछ छोट प्रतिशत से रउआ कमाई होला। रउआ पास बहुत डेटा हो सकेला लेकिन बजट ओतना ना।

हम कुछ सेवा पर काम करेनी जे रोज 1B अनुरोध पावेली, एहसे अपना निगरानी आ लॉगिंग खुद होस्ट करल समझदारी बा। अगर रउआ मात्रा कम बा त होस्ट कइल सेवा जादा आसान बा।


### AWS सेवा मिश्रित बाड़ी

AWS सेवा के साथ हमार अनुभव मिश्रित रहल बा। उनकर Elasticsearch सेवा अस्थिर रहल, एहसे हमनी ओकरा खातिर अपना इंस्टेंस चलावेनी। CloudWatch मेट्रिक महंगा बा, एहसे हमनी आम तौर पर एकरा के एप्लिकेशन के बजाय "इन्फ्रास्ट्रक्चर" स्तर के मेट्रिक खातिर इस्तेमाल करेनी, यानी स्वास्थ्य-संबंधी मेट्रिक जहाँ AWS इंस्टेंस पर चल रहल सॉफ्टवेयर से बेहतर जान सकेला कि का हो रहल बा। CloudWatch लॉग अपडेट होखे में धीमा हो सकेला आ ओकरा लग ओतना मेटाडेटा नइखे। ELK चलावल एमे मदद करेला। अगर हम सचमुच वास्तविक समय डेटा चाहीं, त लॉग खातिर परिवहन के रूप में Kafka इस्तेमाल करल बेहतर ह। ई Logstash द्वारा काफी नीमन से समर्थित बा। Kafka क्लस्टर संभालल कमजोर दिल वाला खातिर नइखे, हालांकि, बहुत सारा खुल्ला पाइपिंग बा।


### Kafka

टिप्पणी: Kafka कबो-कबो बहुत पेचीदा हो सकेला, चाहे Kafka चट्टान जइसन ठोस हो सकेला आ रउआ लगभग भुला जालीं कि ऊ सब कुछ बाँध के राखत बा।


टिप्पणी: Kafka ठोस रहल बा, लेकिन एकरा के चालू करे में आश्चर्यजनक मात्रा में काम लागल। हम एकरा के रिलेशनल डेटाबेस जइसन सोचेनी लेकिन रउआ बस "भौतिक" परत पर काम करत बानी, जइसे टेबलस्पेस, फाइल आ पार्टीशन। शुरू में कुछ समय अइसन रहे जब प्रबंधन उपयोगिता के कमी रहे, आ हमनी के जइसे कंज्यूमर ग्रुप रीसेट करे खातिर प्रोग्राम लिखे के पड़ल। http://howfuckedismydatabase.com/nosql/

टिप्पणी: हमनी Kafka के लॉग संदेश खातिर "बफर" के रूप में आ अइसन जगह के रूप में इस्तेमाल करेनी जहाँ हमनी कई सर्वर से आवे वाला डेटा पर वास्तविक समय स्ट्रीम प्रसंस्करण कर सकीले। अगर हमनी पर DDOS हमला होला, त हमनी के कई इंस्टेंस में डेटा के विश्लेषण करे के तरीका चाहीं। अगर हमनी सर्वर से सीधा ELK में लॉग करेनी, त भार Elasticsearch क्लस्टर के उड़ा सकेला।

टिप्पणी: Kafka हमनी खातिर नीमन बा काहेकि अगर हमनी पर DDOS हमला होला, त हमनी के कई इंस्टेंस में डेटा के विश्लेषण करे के तरीका चाहीं। अगर हमनी सर्वर से सीधा ELK में लॉग करेनी, त भार Elasticsearch क्लस्टर के उड़ा सकेला।


टिप्पणी: Kafka कम काम करेला आ जादा कुशल बा, एहसे ई भार के नीमन से संभाल सकेला। आ हमनी Kafka के काम के कतार में लगावेनी आ फेर से कोशिश करेनी। आ Kafka के जादा भार से ओह उपयोगकर्ता पर असर ना पड़ेला जे Kibana संगे इंटरैक्टिव काम करे के कोशिश कर रहल बाड़ें, जइसे अगर Elasticsearch संघर्ष कर रहल होखित त पड़ित।

टिप्पणी:  स्ट्रीम प्रसंस्करण मुख्य रूप से दुरुपयोग खोजेला, जइसे पूरा क्लस्टर में एगो IP से बहुत जादा ट्रैफिक, आ फेर ब्लॉक के पूरा क्लस्टर में साझा करेला।

टिप्पणी: logstash-output-kafka प्लगइन अबहिन काफी अविश्वसनीय बा। हम एकर GitHub मुद्दा पन्ना पर कई समस्या से कटल बानी, जे कबो ठीक होत ना लागेला। हम एकरा के इस्तेमाल से हट के, अपना ऐप से सीधा Kafka में भेजल चाहत बानी।

टिप्पणी: हमनी अब संरचित इवेंट के ऐप से सीधा Kafka में भेज रहल बानी। मुख्य प्रेरणा लॉग डेटा के कम बेर छूवल आ डिस्क के कई बेर पढ़े-लिखे से बचल रहे। उच्च मात्रा वाला सिस्टम में, लॉगिंग में एप्लिकेशन खुद से जादा काम लाग सकेला। हम सोच रहल बानी कि journald के भी सीधा लॉग भेजे लायक बनावल जाय, एगो C प्रोग्राम से।


### Loki

Loki पर कड़ी नजर राखीं। ई अबहिन तैयार नइखे लेकिन जब हो जाई त हम उम्मीद करब कि ई एह स्टैक में बेहतर फिट होई। Loki grafana labs द्वारा बनावल एगो लॉग एग्रीगेटर ह, ई Prometheus जइसन स्क्रैपिंग आ टैग वाक्य-विन्यास इस्तेमाल करेला।


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

मेट्रिक खातिर Prometheus + alertmanager। <3 Prometheus।

लॉगिंग/गलती रिपोर्टिंग खातिर Rollbar/Graylog (एमे कुछ ओवरलैप बा; छोट सेवा के शायद दूनो के जरूरत नइखे)।

अबहिन, अलर्ट बस कुछ Slack चैनल में से एक में जाला जेकरा खातिर इच्छुक पक्ष सूचना चालू कइले बाड़ें। अगर हमनी ऑन-कॉल के बारे में जादा गंभीर होखीं त ऊ PagerDuty/VictorOps/वगैरह में जाई।

ग्राफ आ डैशबोर्डिंग खातिर Grafana। उनके आवे वाली लॉगिंग सुविधा Graylog के जरूरत खतम कर दी कि ना ई देखे के भी बेसब्री से इंतजार बा।


### Thanos

हमनी Thanos के अपना HA सेटअप के फ्रंट-एंड के रूप में इस्तेमाल करेनी। ई जानेला कि HA जोड़ी के डी-डुप्लिकेट कइसे कइल जाला।

हमनी अबहिन 6 महीना के स्थानीय Prometheus डेटा राखत बानी। ई हमनी खातिर ठीक-ठाक काम करेला। लेकिन हम अबहिन लमहर समय के डेटा भंडारन खातिर अपना Thanos सेटअप में बकेट भंडारन लागू करे के बीच में बानी। सिद्धांत में, GCS भंडारन उ GCE मानक स्थायी डिस्क से लगभग 30% सस्ता होई जे हमनी अबहिन इस्तेमाल करेनी।

हमनी अबहिन Prometheus डेटा के बैकअप नइखीं लेत। डेटा हमनी खातिर अलर्टिंग लायक पर्याप्त होखे से आगे सचमुच जरूरी नइखे। हमनी के कुल बेड़ा डिप्लॉयमेंट साल-दर-साल एतना बदलेला कि कुछ महीना से पुरान ऐतिहासिक डेटा सचमुच दिलचस्प नइखे। साल-दर-साल कुछ मुख्य आंकड़ा होखल दिलचस्प हो सकेला, हम एगो मुख्य-आंकड़ा रिकॉर्डिंग नियम के सेट बना सकीले आ ओकरा के Federation से जमा कर सकीले चाहे बस Thanos के संभाले दीं।

EDIT: छोट अस्वीकरण, हम एगो Prometheus डेवलपर बानी।


### Prometheus HA

Prometheus में HA दोहराव से कइल जाला, रउआ कई पॉपर चलावेनी आ कई के पोल करे आ डेटा के डी-डुप्लिकेट करे के तरीका बा

पैमाना नेटवर्क तय करके आ नेटवर्क के अलग-अलग हिस्सा के अलग Prometheus से पोल करा के बढ़ावल जाला

लमहर समय के भंडारन Prometheus के मजबूत पक्ष नइखे लेकिन ओकरा के influx चाहे timescaledb जइसन कुछ पर उतार दिहल जाला (जे तकनीकी रूप से HA के निशान भी लगावेला) एकरा बारे में हम पढ़ल लेख https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

लमहर समय के चीज अबहिन आजमवले नइखीं काहेकि हम अबहिन बस प्रयोग कर रहल बानी आ ओकरा के छोट समय के ग्राफ खातिर इस्तेमाल कर रहल बानी जबकि librenms लमहर समय खातिर हमरा नेटवर्क के निगरानी करेला


### Datadog + PagerDuty + Threat Stack

हमनी Datadog (PagerDuty संगे) आ Threat Stack इस्तेमाल करेनी आ एकरा से जादा खुश ना हो सकीले। DD के साथ हमार बस एके शिकायत मेट्रिक भंडारन के अपेक्षाकृत ऊँच लागत बा।


### Zabbix

लगभग सब कुछ के निगरानी खातिर अनुकूलित स्क्रिप्ट संगे Zabbix। जादू जइसन काम करेला।


### Outlyer

हम Outlyer इस्तेमाल कर रहल बानी, लेकिन हमके अस्वीकरण देवे के पड़ी कि हम इहाँ काम करेनी, आ अपना खाना के खुद चखल जरूरी बा।

बढ़ावे खातिर अबहियों Graylog, Sentry आ Statuscake के जरूरत बा।

पक्षपाती सुनाई देला, लेकिन Nagios आ आउर निगरानी प्रणाली के आंतरिक रूप से खुशी से चलावे के बाद, हम कवनो नया काम में होस्ट कइल समाधान खरीद लेब आ ऊ दर्द सौंप देब।


### Nagios + Nagiosgraph

हमनी सब निगरानी आ अलर्टिंग खातिर Nagios चलावेनी। अलर्ट ईमेल (चेतावनी आ गंभीर सूचना) आ सुने-लायक ऐप सूचना (गंभीर अलर्ट खातिर) के जरिए होला।

Nagiosgraph के इस्तेमाल दृश्य खातिर कइल जाला।

ई सेटअप हमनी के माहौल में का हो रहल बा एकरा बारे में हमनी के व्यापक रूप से सूचित राखे में बहुत प्रभावी रहल बा। हमनी लगभग 110 मिशन-नाजुक सर्वर आ लगभग 760 डेटा बिंदु चलावेनी आ निगरानी करेनी, आ सात बरिस से जादा समय से ई सुबह के प्रणाली बा।

हम कवनो समय Graylog चाहे ELk संगे लॉग के एकत्र भी करे चाहब।


### Prometheus + Grafana + AlertManager

शानदार Prometheus Operator helm chart के जरिए Prometheus + Grafana + AlertManager। लॉग अबहियों LogDNA birch योजना में जाला काहेकि हमनी देखनी कि ELK हमनी के साधारण min 3 max 5 नोड GKE खातिर बहुत भारी बा।


### DataDog + Sentry + PagerDuty.

हम अपना सब निगरानी समाधान खुद चलावत रहनी, कई तरह के सॉफ्टवेयर इस्तेमाल करके जेमें Nagios, Icinga, Zabbix, ELK, Greylog2, Influx, आ कई आउर औजार शामिल रहल, लेकिन सच्चाई ई बा कि अपना निगरानी इन्फ्रास्ट्रक्चर के चलावे में बहुत जादा मेहनत लागेला, खास कर जब रउआ वोही काम खातिर दोसरा के एतना कम दर पर पइसा दे सकीले!

निगरानी इन्फ्रा चलावे खातिर दोसरा के पइसा देला से हमार ग्राहक अपना प्लेटफॉर्म चलावे पर ध्यान दे सकेलें, निगरानी के निगरानी करे के बजाय, मतलब उनकर प्लेटफॉर्म के स्थिरता से मिले वाला मूल्य निगरानी-के-रूप-में-सेवा के कवनो लागत से बहुत जादा होला।


### Sensu + Graphite + ELK

हमार कंपनी खुद-होस्ट कइल चीज पर बहुत जोर देला।

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

अलर्टिंग खातिर Prometheus + Alertmanager, हमार टीम मानेला कि सादा निगरानी नीमन निगरानी ह।

लॉगिंग आ ट्रेसिंग जइसन आउर प्रणाली तब निदान खातिर समृद्ध संदर्भ देवेली जब ऑन-कॉल अलर्ट पावेला, लेकिन हमनी कबो ओकरा पर अलर्टिंग ना बनावेनी।


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic।


### Prometheus + Circonus

Prometheus-इंस्ट्रूमेंटेड सेवा => Circonus विश्लेषण आ दृश्य


### icinga2 + VictorOps + NewRelic + Sentry + Slack

हमनी नीचे के सेवा इस्तेमाल कर रहल बानी:

निगरानी खातिर icinga2 आ अलर्टिंग खातिर VictorOps

सेवा के ब्योरेवार निगरानी खातिर NewRelic

सेवा में गलती ट्रैकिंग खातिर Sentry

Slack/Email अलर्टिंग के हिस्सा ह जे NewRelic चाहे icinga2 से ट्रिगर होला


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

विश्लेषण खातिर elasticsearch इंटीग्रेशन आ ग्राफ खातिर graphite+grafana इंटीग्रेशन संगे icinga2।

icinga2 में apply नियम के लचीलापन के चलते, डेवलपर बस ओकरा सेवा के देखेलें जेकरा खातिर उनके सूचना मिलेला।

आ icinga2 director के जरिए, प्रोग्रामर लोग आसानी से बड़ पैमाना पर बिना कवनो झंझट के आपन जाँच तय कर सकेलें (जे ऊ लोग हर कुछ दिन करेलें - 100 जाँच बाहर जाला, 100 आउर जाँच भीतर आवेला)।


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

अबहिन हमनी लग का बा:

मेट्रिक खातिर DataDog

एप्लिकेशन निगरानी खातिर New Relic

लॉग खातिर ELK (Elastic Search + Logstash + Kibana)

अपवाद लॉग करे खातिर Sentry (खुद-होस्ट कइल)

अलर्टिंग खातिर ईमेल + Slack + VictorOps (गंभीरता के आधार पर)

हमनी का चाहे चाहत बानी:

मेट्रिक खातिर Prometheus (दृश्य खातिर Grafana)

एप्लिकेशन निगरानी खातिर New Relic (शायद Elastic Search APM)

लॉगिंग खातिर EFK (elastic search + fluentd + kibana)। शायद, जबले हमनी ओहिजा पहुँचब Grafana के Loki प्रोडक्शन खातिर तैयार हो जाई

अपवाद खातिर Sentry

अलर्ट खातिर Alertmanager + ईमेल + VictorOps


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (अस्वीकरण: VMware में काम करेनी)


### Telegraf + Prometheus + InfluxDB + Grafana

CPU, डिस्क, मेमोरी आ नेटवर्क जइसन सर्वर मेट्रिक खातिर Telegraf। हमनी अपना नेटवर्क उपकरण के SNMP निगरानी खातिर भी Telegraf इस्तेमाल करेनी।

एप्लिकेशन मेट्रिक खातिर Prometheus। हमनी अपना एप्लिकेशन में स्वास्थ्य जाँच लिखेनी जेकरा के Prometheus स्क्रैप करेला।

समय-श्रृंखला भंडारन खातिर InfluxDB। इहाँ हमनी के Telegraf डेटा भेजल जाला।

डैशबोर्ड आ अलर्ट खातिर Grafana। अलर्टिंग इंजन बहुत मजबूत नइखे, लेकिन काम चला देला। हमनी अलर्ट Slack में भी भेजेनी।

अबहिन हमरा लग जवन नइखे ऊ केंद्रीकृत लॉगिंग समाधान बा। ELK ताकतवर बा लेकिन चालू करे आ संभाले में कठिन बा, आ हमके कवनो मुफ्त विकल्प के जानकारी नइखे जे देखे लायक काफी नजदीक होखे।


### Sematext + Logagent + Experience

मेट्रिक, लॉग, ट्रेस खातिर Sematext, जल्दिए असली उपयोगकर्ता निगरानी खातिर भी। हमरा राय में N अलग-अलग औजार/सेवा के इस्तेमाल से सादा/सस्ता।

लॉग भेजे खातिर हमनी पहिले rsyslog इस्तेमाल करत रहनी आ फेर Logagent पर चल गइनी।

फ्रंटएंड क्रैश रिपोर्टिंग खातिर हमनी Sentry इस्तेमाल करेनी, लेकिन हमनी जल्दिए Experience पर चल जाइब।

अस्वीकरण: हम एगो Sematextan बानी।


### Azure Monitor/Analytics + OpsGenie

काश Log Analytics के बेहतर इंटरफेस होखित। हमनी splunk से हट रहल बानी, जवना में रास्ता खोजल बहुत आसान रहे।


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

रउआ सचमुच आपन सूचना प्रणाली खुद चलावल ना चाहब। रउआ Splunk के जगह ELK ले सकीले जबले कि रउआ सुरक्षा टीम Splunk के पसंद ना करेला।


### Telegraf + Prometheus + Grafana + Alertmanager

कलेक्टर के रूप में Telegraf, निगरानी आ अलर्टिंग खातिर Prometheus + Alertmanager, slack चैनल आ गंभीर अलर्ट खातिर pagerduty संगे इंटीग्रेटेड। होस्ट मेट्रिक के दृश्य खातिर Grafana।


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

मेट्रिक + अलर्ट खातिर Prometheus

Prometheus डैशबोर्ड खातिर Grafana

Prometheus इंस्टेंस के निगरानी करे वाला Cloudwatch

अपवाद ट्रैकिंग खातिर sentry

kibana + elasticsearch

graylog

बैच/cronjob खातिर prometheus Push Gateway

मेट्रिक के एक Prometheus इंस्टेंस से दोसरा में „push/forward“ करे खातिर SOP https://github.com/rapidloop/sop

क्लाइंट या त Prometheus क्लाइंट इस्तेमाल करेलें। हमनी क्लाइंट पक्ष पर opencensus.io इस्तेमाल करे के कोशिश करेनी


### PagerDuty + Monitis

PagerDuty + Monitis। कुछ सेवा के स्वास्थ्य जाँचे खातिर कुछ खास बनावल Azure Functions भी।

एह साल Prometheus आ Grafana लावे पर विचार कर रहल बानी


### Prometheus + Grafana + Bosun

समय-श्रृंखला डेटा जमा करे खातिर Prometheus। दृश्य खातिर Grafana। अलर्ट प्रबंधन खातिर Bosun।


### Azure Monitor/Analytics/Insights/Dashboards

बस Azure वाली दुकान, Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Prometheus के जरिए Kubernetes में कंटेनर सेवा के निगरानी खातिर Grafana

मुख्य रूप से वेब API आ वेब एप्लिकेशन खातिर एंड-टू-एंड सेवा निगरानी खातिर Monitis

अलर्ट प्रबंधन खातिर OpsGenie

हमनी के प्रणाली से स्थिति जानकारी पावे खातिर Slack


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

इहाँ लमहर समय के (dev)ops इंजीनियर बानी। Nagios पर बढ़नी। अपना बूटस्ट्रैप कइल SaaS https://checklyhq.com पर राय पावल चाहेब। हमनी बहुत गहरा अलर्टिंग संगे API निगरानी आ साइट लेन-देन निगरानी करेनी।

हम Checkly शुरू कइनी काहेकि API क्षेत्र में सक्रिय / सिंथेटिक निगरानी तनी सीमित (आ महंगा) रहे। ब्राउजर-आधारित / स्क्रिप्ट वाली निगरानी आउर जादा मालिकाना आ महंगा बा। हमनी Puppeteer इस्तेमाल करेनी आ कीमत जेतना हो सके कम राखेनी।

हमनी के निगरानी स्टैक:

Checkly (अपना खाना खुद चखल...)

AppOptics (अनुकूलित ग्राफिंग)

SMS संदेश खातिर AWS Cloudwatch & SNS।

अंतर्निहित Heroku अलर्टिंग।

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana हमनी के इन्फ्रास्ट्रक्चर समस्या चाहे प्रदर्शन गिरावट के बारे में slack में अलर्ट करेला, आ हमनी logz.io के एप्लिकेशन परत से गलती-स्तर लॉग के एक खास मात्रा पर slack में अलर्ट करे खातिर कॉन्फिगर कइले बानी।


### SignalFX + Splunk + PagerDuty + Slack

अबहिन इस्तेमाल कर रहल बानी: SignalFX, Splunk, PagerDuty आ Slack। हम SignalFX के बड़ प्रशंसक नइखीं भले उनकर सहायता टीम बहुत मिलनसार आ प्रतिक्रियाशील बा। हमके Splunk (अगर रउआ पइसा दे सकीले त सार्थक), PagerDuty आ Slack पसंद बा।

हम TICK स्टैक इस्तेमाल करत रहनी जेमें C के अधिकतर हिस्सा सचमुच G रहे, यानी Grafana भले हम Chronograf तनी इस्तेमाल कइले रहनी। ई बहुत बढ़िया रहे लेकिन संभालल झंझट रहे। SaaS बनाम खुद-होस्टिंग के क्लासिक दुविधा।

हम DataDog, New Relic, Graylog, ELK आ BugSnag इस्तेमाल कइले बानी। हमके DataDog आ New Relic बहुत पसंद बा, Graylog काफी नीमन बा। हम ELK के बड़ प्रशंसक नइखीं। BugSnag नीमन बा, हमके सचमुच लागेला कि गलती/अपवाद ट्रैक कइल कई मामला में पूरा लॉग निगरानी के नीमन विकल्प बा।


### ELK + Prometheus + Grafana

आउर लोग के जइसे, हमनी लॉग खातिर ELK आ बाकी सब खातिर Prometheus+Grafana इस्तेमाल करेनी।

ई सेटअप बनवले राखल आसान बा अगर रउआ अपना के कबो-कबो डेटा खोवे के अनुमति देवेनी। उदाहरण खातिर, अगर हमनी के ElasticSearch डेटाबेस गड़बड़ हो जाला (जे हमनी खातिर दुर्भाग्य से हर 2-3 महीना में होला) त हमनी HA के चक्कर में ना पड़ीं आ बदले में डेटा फेंक के आगे बढ़ जालीं। अगर रउआ के सचमुच HA चाहे लमहर समय के प्रतिधारण चाहीं, त शुभकामना।


### Datadog + Prometheus + Grafana

हम Datadog महीना-दर-महीना सेट कइनी काहेकि जब हम इहाँ अइनी, कवनो निगरानी आ कवनो अलर्टिंग ना रहे। हमनी के बस कुछ साइट अपटाइम खातिर हर 5 मिनट पर निगरानी में रहे। Datadog बिना शक सेट करे में सबसे आसान ह। जब हम बाकी सब मुद्दा निपटा लेब, हम Prometheus+Grafana पर चल जाइब। लॉग प्रबंधन पर अबहिन 100% तय नइखे।


### Nagios + ELK

हमनी लग 100+ उत्पाद बा जेकरा के हमनी समर्थन देवेनी।

ऑन-प्रिम खातिर, अधिकतर Nagios आ ELK। क्लाउड खातिर, हमनी DataDog से NewRelic में माइग्रेट कर रहल बानी।


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

हमनी datadog इस्तेमाल करत रहनी लेकिन पवनी कि ई हमनी के जरूरत खातिर बहुत जादा महंगा बा। गलत मत समझीं ई अद्भुत बा पर एकर विशाल लागत बा। हमनी सालाना सदस्यता से site24x7.com सेट कर पवनी जेकर लागत DD के लगभग 2-3 महीना के बराबर रहे।

हमनी के निगरानी स्टैक:

Site24x7 - APM, बाहरी URL निगरानी, SMTP मेलफ्लो निगरानी, ssl समाप्ति आ प्रक्रिया निगरानी।

StatusCake - URL निगरानी आ पुष्टि खातिर - ई हमनी के बैकअप ह अगर site24x7 कुछ चूक जाए (ऊ ना चूकेला) लेकिन SC हमनी के जरूरत खातिर बाहरी पोर्ट आ सेवा निगरानी खातिर जादा लचीला ह।

दूनो औजार PagerDuty पर बढ़ावेला, आ फेर हमनी के slack में बढ़ावल सूचना मिलेला।

SumoLogic - लॉग निगरानी खातिर (ई बढ़िया औजार बा लेकिन हमनी के जरूरत खातिर तनी जटिल)

slack से हमनी ack कर सकीले, चाहे अलर्ट के निदान कर सकीले।

हमनी लग फेर बहुत सारा site24x7 स्वचालन बा जे 'BedOps' खातिर commando.io से जुड़ेला जइसन हमनी कहेनी - जहाँ अलर्ट ट्रिगर होला, हमनी स्थिति के निदान करे के कोशिश में कुछ स्क्रिप्ट चाहे स्वचालन शुरू करेनी (99% समय स्वचालन + हमनी के स्क्रिप्ट हमनी के मुसीबत से बाहर राखेला)

हमनी लग अपना KB में आंतरिक runbook बा जब स्वचालन विफल हो जाला चाहे जब कुछ अइसन होला जे दायरा से बाहर बा आ ठीक करे के बा।


### Prometheus + AlertManager + Grafana + Stackdriver

हमनी के GKE क्लस्टर आ VM में मेट्रिक खातिर Prometheus (Operator) / AlertManager / Grafana।

लॉग खातिर Google Stackdriver (काहेकि ई शामिल बा आ डिफॉल्ट रूप से सक्रिय बा आ अबहिन हमनी के जरूरत खातिर काफी बा)।


### Zabbix

सब कुछ खातिर Zabbix। कवनो अतिरिक्त सॉफ्टवेयर के जरूरत नइखे।
