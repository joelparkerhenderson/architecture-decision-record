# મેટ્રિક્સ, મોનિટર, ચેતવણીઓ

સામગ્રી:

* [સારાંશ](#સારાંશ)
  * [સમસ્યા](#સમસ્યા)
  * [નિર્ણય](#નિર્ણય)
  * [સ્થિતિ](#સ્થિતિ)
* [વિગતો](#વિગતો)
  * [ધારણાઓ](#ધારણાઓ)
  * [મર્યાદાઓ](#મર્યાદાઓ)
  * [વલણો](#વલણો)
  * [દલીલ](#દલીલ)
  * [અસરો](#અસરો)
* [સંબંધિત](#સંબંધિત)
  * [સંબંધિત નિર્ણયો](#સંબંધિત-નિર્ણયો)
  * [સંબંધિત જરૂરિયાતો](#સંબંધિત-જરૂરિયાતો)
  * [સંબંધિત આર્ટિફેક્ટ્સ](#સંબંધિત-આર્ટિફેક્ટ્સ)
  * [સંબંધિત સિદ્ધાંતો](#સંબંધિત-સિદ્ધાંતો)
* [નોંધો](#નોંધો)
  * [મુક્ત લખાણ સંદેશા વિરુદ્ધ સંરચિત ઇવેન્ટ સંદેશા](#મુક્ત-લખાણ-સંદેશા-વિરુદ્ધ-સંરચિત-ઇવેન્ટ-સંદેશા)
  * [Graylog સરળ છે](#graylog-સરળ-છે)
  * [Prometheus ને થોડું ટ્યૂનિંગ જોઈએ](#prometheus-ને-થોડું-ટ્યૂનિંગ-જોઈએ)
  * [AWS સેવાઓ મિશ્ર છે](#aws-સેવાઓ-મિશ્ર-છે)
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


## સારાંશ


### સમસ્યા

અમે મેટ્રિક્સ, મોનિટર અને ચેતવણીઓ વાપરવા માગીએ છીએ, કારણ કે અમે જાણવા માગીએ છીએ કે અમારી એપ્લિકેશનો કેટલી સારી રીતે કામ કરી રહી છે, અને ક્યારે સમસ્યા છે.


### નિર્ણય

WIP.


### સ્થિતિ

માહિતી એકત્રિત કરી રહ્યા છીએ. અમે સ્પેક્ટ્રમના સંભવિત છેડાઓથી શરૂ કરી રહ્યા છીએ: સૌથી વધુ ભલામણ કરાયેલું જૂનું મફત સાધન (Nagios) અને સૌથી વધુ ભલામણ કરાયેલું નવું ચૂકવણીવાળું સાધન (New Relic).


## વિગતો


### ધારણાઓ

અમે આધુનિક, ઝડપી, વિશ્વસનીય, પ્રતિભાવશીલ, વગેરે વેબ એપ્લિકેશનો બનાવવા માગીએ છીએ.

અમે બનાવવાને બદલે ખરીદવા માગીએ છીએ.


### મર્યાદાઓ

અમે એવા સાધનો ઇચ્છીએ છીએ જે અમારી devops પાઇપલાઇન અને અમારા ડિપ્લોયમેન્ટ ક્લાઉડ સાથે સારી રીતે કામ કરે.


### વલણો

અમે હાલમાં વલણો પર સંશોધન કરી રહ્યા છીએ.


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

  

  
### દલીલ

અત્યાર સુધી, Nagios અને New Relic સ્પેક્ટ્રમના છેડા છે. Nagios સૌથી જૂનું, સૌથી સરળ, મફત, શક્ય સાધન છે. New Relic સૌથી નવી સુવિધાઓવાળું, સૌથી સંપૂર્ણ, ચૂકવણીવાળું, શક્ય સાધન છે. અમે આનાથી મૂલ્યાંકન શરૂ કરીશું. જરૂર પડ્યે, અમે સ્પેક્ટ્રમની અંદર જઈશું.  

અત્યાર સુધી, Zabbix પાસે શ્રેષ્ઠ ભલામણો છે, અને સૌથી સંપૂર્ણ ક્ષમતાઓ પણ આપે છે.

અત્યાર સુધી, ELK પાસે શ્રેષ્ઠ ઓપન-સોર્સ બનાવવા-પર-ખરીદવાની લોકપ્રિયતા છે.

અત્યાર સુધી, Prometheus + Graphana પાસે શ્રેષ્ઠ લોકપ્રિયતા છે.


### અસરો

TODO.


## સંબંધિત


### સંબંધિત નિર્ણયો

પસંદગીઓ પરીક્ષણક્ષમતા, ટેલિમેટ્રી, અને સંભવતઃ ગ્રાહક સેવા, સાઇટ વિશ્વસનીયતા એન્જિનિયરિંગ, વગેરે જેવી અન્ય સિસ્ટમોને અસર કરશે.


### સંબંધિત જરૂરિયાતો

TODO.


### સંબંધિત આર્ટિફેક્ટ્સ

TODO.


### સંબંધિત સિદ્ધાંતો

સરળતાથી પલટાવી શકાય તેવું.

ઝડપની જરૂરિયાત.


## નોંધો

એક ઘણો સારો ઓપન સોર્સ સ્ટેક આ છે:

* મેટ્રિક્સ અને મેટ્રિક્સ પર આધારિત ચેતવણીઓ માટે Prometheus

* મેટ્રિક્સ દર્શાવવા માટે Grafana

* લોગ અને સંરચિત ઇવેન્ટ્સ માટે Elasticsearch/Logstash/Kibana (ELK)

* મોબાઇલ સૂચનાઓ માટે Pushover


### મુક્ત લખાણ સંદેશા વિરુદ્ધ સંરચિત ઇવેન્ટ સંદેશા

મુક્ત લખાણ સંદેશા: ઉદાહરણ તરીકે, /var/log/messages માં તમને મળતી એવી રેન્ડમ સામગ્રી, અને એપ્લિકેશન દ્વારા ઇરાદાપૂર્વક ઉત્પન્ન થયેલું. આ સંદેશા બોક્સ પર થઈ રહેલી અન્ય બાબતો, જેમ કે મેમરી ખૂટવી કે હાર્ડવેર ભૂલો, ઓળખવા માટે ઉપયોગી છે, પરંતુ તેમાં ઘણો કચરો હોય છે. 

સંરચિત ઇવેન્ટ સંદેશા: એપ્લિકેશન દ્વારા ઉત્પન્ન, લક્ષણોના નિશ્ચિત કે ગતિશીલ સમૂહ સાથે, દા.ત. HTTP વિનંતી લોગ, હિસાબી લોગ, વપરાશકર્તા લૉગિન.

સામાન્ય રીતે કહીએ તો, દરેક વિનંતીની વિગતો એવી રીતે લોગ કરવી સરસ છે કે તમે લક્ષણોના આધારે ઊંડા ઉતરી શકો. તેથી દરેક વસ્તુમાં દા.ત. userid કે sessionid ઉમેરવાથી તમે ટ્રેસ કરી શકો. સ્પષ્ટ ટ્રેસિંગ પણ સારું છે, અલબત્ત. આ માટે ELK વાપરવું એ https://www.honeycomb.io/ ના ગરીબ માણસના સંસ્કરણ જેવું છે


### Graylog સરળ છે

મારા અનુભવમાં Graylog ચાલુ કરવું વધુ સરળ છે.


### Prometheus ને થોડું ટ્યૂનિંગ જોઈએ

હું સામાન્ય રીતે મેટ્રિક્સ માટે Prometheus થી ખુશ છું. ચેતવણીને થોડું ટ્યૂનિંગ જોઈએ, પરંતુ તે ઘણું સારું છે. તે તમારી એપ્લિકેશન પર આધાર રાખે છે. મને લાગે છે કે અંતર્ગત કારણો પર નહીં પણ અંતિમ-વપરાશકર્તાને દેખાતી પરિસ્થિતિઓ પર ચેતવણી આપવી શ્રેષ્ઠ છે. ઉદાહરણ તરીકે, પેજ લોડ સમય સારો છે, પ્રતિ સેકન્ડ વિનંતીઓની સંખ્યા નથી. જોકે પ્રતિ સેકન્ડ શૂન્ય વિનંતીઓ સૂચવે છે કે કંઈક ખોટું છે.

સેવાનો ફાયદો એ છે કે તેઓ બોક્સ-બહાર વધારાની બુદ્ધિમત્તા આપે છે. મને સામાન્ય રીતે Datadog ગમે છે. જો તમારી પાસે ઘણો ડેટા હોય તો સેવાઓ ડરામણી રીતે મોંઘી હોઈ શકે, અને ક્યારેક એવા કિંમત મોડેલ હોય છે જે ક્લાઉડ-અનુકૂળ નથી, દા.ત. પ્રતિ ઇન્સ્ટન્સ ચાર્જ કરવું, જ્યારે ઇન્સ્ટન્સ ગતિશીલ હોય. જ્યાં દરેક વિનંતી ચૂકવણી કરનાર વપરાશકર્તાની હોય તેવી સેવાઓ અને જાહેરાત-સંબંધિત હોય તેવી સેવાઓ વચ્ચે પણ તફાવત છે, તેથી વિનંતીઓની ફક્ત નાની ટકાવારી તમને કમાણી કરાવે છે. તમારી પાસે ઘણો ડેટા અને બજેટ ઓછું હોઈ શકે.

હું કેટલીક સેવાઓ પર કામ કરું છું જે દિવસમાં 1B વિનંતીઓ મેળવે છે, તેથી અમારું પોતાનું નિરીક્ષણ અને લોગિંગ હોસ્ટ કરવું સમજદારીભર્યું છે. જો તમારી માત્રા ઓછી હોય તો, હોસ્ટેડ સેવાઓ સરળ છે.


### AWS સેવાઓ મિશ્ર છે

AWS સેવાઓ સાથેનો મારો અનુભવ મિશ્ર રહ્યો છે. તેમની Elasticsearch સેવા અસ્થિર રહી છે, તેથી અમે તેના માટે અમારા પોતાના ઇન્સ્ટન્સ ચલાવીએ છીએ. CloudWatch મેટ્રિક્સ મોંઘા છે, તેથી અમે સામાન્ય રીતે તેમને એપ્લિકેશન માટે નહીં પણ "ઇન્ફ્રાસ્ટ્રક્ચર" સ્તરના મેટ્રિક્સ માટે જ વાપરીએ છીએ, એટલે કે આરોગ્ય-સંબંધિત મેટ્રિક્સ જ્યાં AWS ઇન્સ્ટન્સ પર ચાલતા સોફ્ટવેર કરતાં વધુ સારી રીતે જાણી શકે કે શું ચાલી રહ્યું છે. CloudWatch Logs અપડેટ થવામાં ધીમા હોઈ શકે અને તેમાં એટલો મેટાડેટા નથી. ELK ચલાવવું તેમાં મદદ કરે છે. જો મને ખરેખર રીઅલ ટાઇમ ડેટા જોઈએ, તો લોગ માટે પરિવહન તરીકે Kafka વાપરવું વધુ સારું છે. તેને Logstash દ્વારા ઠીકઠીક સપોર્ટ છે. Kafka ક્લસ્ટરનું સંચાલન કમજોર દિલવાળા માટે નથી, જોકે, ઘણી ખુલ્લી પ્લમ્બિંગ છે.


### Kafka

ટિપ્પણી: Kafka ક્યારેક અત્યંત અટપટું હોઈ શકે, અથવા Kafka ખડક જેવું મજબૂત હોઈ શકે અને તમે લગભગ ભૂલી જાવ કે તે ત્યાં બધું જોડીને બેઠું છે.


ટિપ્પણી: Kafka મજબૂત રહ્યું છે, પરંતુ તેને ચાલુ કરવામાં આશ્ચર્યજનક રીતે ઘણું કામ લાગ્યું. હું તેને રિલેશનલ ડેટાબેઝ જેવું ગણું છું પણ તમે ફક્ત "ભૌતિક" સ્તરે કામ કરી રહ્યા છો, દા.ત. ટેબલસ્પેસ, ફાઇલો અને પાર્ટિશન. શરૂઆતમાં કેટલાક સમય એવા હતા જ્યારે વ્યવસ્થાપન ઉપયોગિતાઓ ઓછી હતી, અને અમારે દા.ત. કન્ઝ્યુમર ગ્રુપ રીસેટ કરવા પ્રોગ્રામ લખવા પડ્યા. http://howfuckedismydatabase.com/nosql/

ટિપ્પણી: અમે Kafka ને લોગ સંદેશા માટે "બફર" તરીકે અને એવા સ્થાન તરીકે વાપરીએ છીએ જ્યાં અમે અનેક સર્વર્સમાંથી આવતા ડેટા પર રીઅલ ટાઇમ સ્ટ્રીમ પ્રોસેસિંગ કરી શકીએ. જો અમને DDOS હુમલો થાય, તો અમને અનેક ઇન્સ્ટન્સમાં ડેટાનું વિશ્લેષણ કરવાની રીત જોઈએ. જો અમે સર્વર્સમાંથી સીધા ELK માં લોગ કરીએ, તો ભાર Elasticsearch ક્લસ્ટરને ઉડાડી શકે.

ટિપ્પણી: Kafka અમારા માટે સારું છે કારણ કે જો અમને DDOS હુમલો થાય, તો અમને અનેક ઇન્સ્ટન્સમાં ડેટાનું વિશ્લેષણ કરવાની રીત જોઈએ. જો અમે સર્વર્સમાંથી સીધા ELK માં લોગ કરીએ, તો ભાર Elasticsearch ક્લસ્ટરને ઉડાડી શકે.


ટિપ્પણી: Kafka ઓછું કામ કરે છે અને વધુ કાર્યક્ષમ છે, તેથી તે ભારને વધુ સારી રીતે સંભાળી શકે. અને અમે Kafka નું કામ કતારમાં મૂકીએ છીએ અને ફરી પ્રયત્ન કરીએ છીએ. અને Kafka પર ભાર હોવાથી Kibana સાથે ઇન્ટરેક્ટિવ કામ કરવાનો પ્રયત્ન કરતા વપરાશકર્તાઓ પર અસર થતી નથી, જેમ Elasticsearch સંઘર્ષ કરતું હોય ત્યારે થાય.

ટિપ્પણી:  સ્ટ્રીમ પ્રોસેસિંગ મુખ્યત્વે દુરુપયોગ શોધે છે, દા.ત. સમગ્ર ક્લસ્ટરમાં એક IP તરફથી વધુ પડતો ટ્રાફિક, અને પછી બ્લોકને સમગ્ર ક્લસ્ટરમાં વહેંચે છે.

ટિપ્પણી: logstash-output-kafka પ્લગઇન હાલમાં ઘણું અવિશ્વસનીય છે. મને તેના GitHub issues પાના પરની ઘણી સમસ્યાઓએ ડંખ્યો છે, જે ક્યારેય ઠીક થતી લાગતી નથી. હું તેનો ઉપયોગ છોડીને અમારી એપ્સમાંથી સીધું Kafka પર મોકલવા માગું છું.

ટિપ્પણી: અમે હવે સંરચિત ઇવેન્ટ્સ એપ્લિકેશનમાંથી સીધી Kafka ને મોકલી રહ્યા છીએ. મુખ્ય પ્રેરણા લોગ ડેટાને ઓછી વાર સ્પર્શવાની અને ડિસ્કને ઘણી વાર વાંચવા-લખવાથી બચવાની હતી. ઉચ્ચ-માત્રાની સિસ્ટમોમાં, લોગિંગ એપ્લિકેશન પોતે કરતાં વધુ કામ લઈ શકે. હું journald પણ સીધા લોગ મોકલે એવું બનાવવાનું વિચારી રહ્યો છું, C પ્રોગ્રામમાંથી.


### Loki

Loki પર નજીકથી નજર રાખો. તે હજુ તૈયાર નથી પણ જ્યારે થશે ત્યારે હું અપેક્ષા રાખું છું કે તે આ સ્ટેકમાં વધુ સારી રીતે બંધબેસશે. Loki એ grafana labs દ્વારા બનાવાયેલ લોગ એગ્રીગેટર છે, તે Prometheus જેવા જ સ્ક્રેપિંગ અને ટેગ વાક્યરચના વાપરે છે.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

મેટ્રિક્સ માટે Prometheus + alertmanager. <3 Prometheus.

લોગિંગ/ભૂલ રિપોર્ટિંગ માટે Rollbar/Graylog (અહીં થોડો ઓવરલેપ છે; નાની સેવાને કદાચ બંનેની જરૂર નથી).

હાલમાં, ચેતવણીઓ રસ ધરાવતા પક્ષોએ સૂચનાઓ ચાલુ કરેલી હોય તેવી થોડી Slack ચેનલમાંની એકમાં જ જાય છે. જો અમે ઓન-કોલ વિશે વધુ ગંભીર હોત તો તે PagerDuty/VictorOps/વગેરેમાં જશે.

ગ્રાફ અને ડેશબોર્ડિંગ માટે Grafana. તેમની આવનારી લોગિંગ સુવિધાઓ Graylog ની જરૂર દૂર કરશે કે નહીં તે જોવા પણ આતુરતાથી રાહ જોઉં છું.


### Thanos

અમે Thanos ને અમારા HA સેટઅપના ફ્રન્ટ-એન્ડ તરીકે વાપરીએ છીએ. તે HA જોડીઓને ડી-ડુપ્લિકેટ કરવાનું જાણે છે.

અમે હાલમાં 6 મહિનાનો સ્થાનિક Prometheus ડેટા રાખીએ છીએ. આ અમારા માટે ઠીકઠીક સારું કામ કરે છે. પરંતુ હું હમણાં લાંબા ગાળાના ડેટા સંગ્રહ માટે અમારા Thanos સેટઅપમાં બકેટ સ્ટોરેજ લાગુ કરવાની વચ્ચે છું. સૈદ્ધાંતિક રીતે, GCS સ્ટોરેજ અમે હાલમાં વાપરીએ છીએ તે GCE માનક પર્સિસ્ટન્ટ ડિસ્ક કરતાં લગભગ 30% સસ્તું હશે.

અમે હાલમાં Prometheus ડેટાનું બેકઅપ લેતા નથી. ડેટા અમારા માટે ચેતવણી માટે પૂરતો હોય તેનાથી આગળ ખરેખર મહત્વનો નથી. અમારી સંપૂર્ણ ફ્લીટ ડિપ્લોયમેન્ટ વર્ષે વર્ષે એટલી બદલાય છે કે થોડા મહિનાથી જૂનો ઐતિહાસિક ડેટા ખરેખર રસપ્રદ નથી. વર્ષ-દર-વર્ષ થોડા મુખ્ય આંકડા હોવા રસપ્રદ હોઈ શકે, હું મુખ્ય-આંકડાના રેકોર્ડિંગ નિયમોનો સમૂહ સેટ કરી શકું અને તેમને Federation સાથે સંગ્રહું અથવા ફક્ત Thanos ને તેનું ધ્યાન રાખવા દઉં.

EDIT: નાની જાહેરાત, હું Prometheus ડેવલપર છું.


### Prometheus HA

Prometheus માં HA દોહરાવણી દ્વારા થાય છે, તમે અનેક પોપર ચલાવો છો અને અનેકને પોલ કરવાની અને ડેટાને ડી-ડુપ્લિકેટ કરવાની રીતો છે

માપવાનું નેટવર્ક નક્કી કરીને અને જુદા જુદા Prometheus ને નેટવર્કના જુદા જુદા ભાગો પોલ કરાવીને થાય છે

લાંબા ગાળાનો સંગ્રહ Prom નો મજબૂત મુદ્દો નથી પરંતુ તેને influx કે timescaledb જેવા કશા પર ઉતારવામાં આવે છે (જે તકનીકી રીતે HA ના ખાનાને પણ ટિક કરે છે) મેં વાંચેલો લેખ https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

લાંબા ગાળાની વસ્તુ હજુ અજમાવી નથી કારણ કે હું હજુ ફક્ત પ્રયોગ કરી રહ્યો છું અને તેનો ઉપયોગ ટૂંકા ગાળાના ગ્રાફ માટે કરી રહ્યો છું જ્યારે librenms લાંબા ગાળા માટે મારા નેટવર્કની દેખરેખ રાખે છે


### Datadog + PagerDuty + Threat Stack

અમે Datadog (PagerDuty સાથે) અને Threat Stack વાપરીએ છીએ અને વધુ ખુશ ન હોઈ શકીએ. DD સાથે મારી એકમાત્ર ફરિયાદ મેટ્રિક સંગ્રહનો પ્રમાણમાં ઊંચો ખર્ચ છે.


### Zabbix

લગભગ બધું નિરીક્ષણ કરવા માટે કસ્ટમ સ્ક્રિપ્ટ સાથે Zabbix. જાદુની જેમ કામ કરે છે.


### Outlyer

હું Outlyer વાપરી રહ્યો છું, પણ મારે જાહેર કરવું પડશે કે હું અહીં કામ કરું છું, અને પોતાનું ખાવાનું જાતે ચાખવું ફરજિયાત છે.

વધારવા માટે હજુ Graylog, Sentry અને Statuscake ની જરૂર છે.

પક્ષપાતી લાગે છે, પરંતુ Nagios અને અન્ય નિરીક્ષણ સિસ્ટમો આંતરિક રીતે ખુશીથી ચલાવ્યા પછી, હું કોઈપણ નવા કામમાં હોસ્ટેડ ઉકેલ ખરીદીશ અને તે પીડા સોંપી દઈશ.


### Nagios + Nagiosgraph

અમે બધા નિરીક્ષણ અને ચેતવણી માટે Nagios ચલાવીએ છીએ. ચેતવણીઓ ઇમેઇલ (ચેતવણી અને ગંભીર સૂચનાઓ) અને સંભળાય તેવી એપ સૂચનાઓ (ગંભીર ચેતવણીઓ માટે) દ્વારા થાય છે.

Nagiosgraph નો ઉપયોગ દૃશ્યો માટે થાય છે.

આ સેટઅપ અમારા પર્યાવરણમાં શું થઈ રહ્યું છે તે વિશે અમને વ્યાપક રીતે માહિતગાર રાખવામાં ખૂબ અસરકારક રહ્યું છે. અમે લગભગ 110 મિશન-ક્રિટિકલ સર્વર્સ અને લગભગ 760 ડેટા પોઇન્ટ્સ ચલાવીએ છીએ અને નિરીક્ષણ કરીએ છીએ, અને સાત વર્ષથી વધુ સમયથી આ સવારની સિસ્ટમ છે.

હું કોઈક તબક્કે Graylog કે ELk સાથે લોગ એકત્રિત પણ કરવા માગું છું.


### Prometheus + Grafana + AlertManager

અદ્ભુત Prometheus Operator helm chart દ્વારા Prometheus + Grafana + AlertManager. લોગ હજુ LogDNA birch યોજનામાં જાય છે કારણ કે અમે નોંધ્યું કે ELK અમારા સાધારણ min 3 max 5 નોડ GKE માટે ખૂબ ભારે છે.


### DataDog + Sentry + PagerDuty.

હું મારા બધા નિરીક્ષણ ઉકેલો જાતે ચલાવતો હતો, Nagios, Icinga, Zabbix, ELK, Greylog2, Influx અને અન્ય ઘણા સાધનો સહિત દરેક પ્રકારના સોફ્ટવેર વાપરીને, પણ સત્ય એ છે કે તમારું પોતાનું નિરીક્ષણ ઇન્ફ્રાસ્ટ્રક્ચર ચલાવવામાં ખૂબ વધુ પ્રયત્ન લાગે છે, ખાસ કરીને જ્યારે તમે એ જ કામ બીજા પાસે કરાવવા માટે એટલા ઓછા દરે ચૂકવણી કરી શકો!

નિરીક્ષણ ઇન્ફ્રા ચલાવવા માટે બીજાઓને ચૂકવણી કરવાથી મારા ગ્રાહકો નિરીક્ષણનું નિરીક્ષણ કરવાને બદલે તેમના પ્લેટફોર્મ ચલાવવા પર ધ્યાન આપી શકે છે, એટલે કે તેમના પ્લેટફોર્મની સ્થિરતામાંથી તેમને મળતું મૂલ્ય Monitoring as a Service ના કોઈપણ ખર્ચ કરતાં ઘણું વધુ છે.


### Sensu + Graphite + ELK

મારી કંપની સ્વ-હોસ્ટેડ બાબતો પર ખૂબ ભાર મૂકે છે.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

ચેતવણી માટે Prometheus + Alertmanager, મારી ટીમ માને છે કે સરળ નિરીક્ષણ સારું નિરીક્ષણ છે.

લોગિંગ અને ટ્રેસિંગ જેવી અન્ય સિસ્ટમો ઓન-કોલને ચેતવણી મળે ત્યારે નિદાન માટે સમૃદ્ધ સંદર્ભ પૂરો પાડશે, પરંતુ અમે ક્યારેય તેમના પર ચેતવણી બનાવતા નથી.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Prometheus-ઇન્સ્ટ્રુમેન્ટેડ સેવાઓ => Circonus એનાલિટિક્સ અને વિઝ્યુલાઇઝેશન


### icinga2 + VictorOps + NewRelic + Sentry + Slack

અમે નીચેની સેવાઓ વાપરી રહ્યા છીએ:

નિરીક્ષણ માટે icinga2 અને ચેતવણી માટે VictorOps

સેવાના વિગતવાર નિરીક્ષણ માટે NewRelic

સેવામાં ભૂલ ટ્રેકિંગ માટે Sentry

Slack/Email ચેતવણીનો ભાગ છે જે NewRelic કે icinga2 માંથી ટ્રિગર થાય છે


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

વિશ્લેષણ માટે elasticsearch ઇન્ટિગ્રેશન અને ગ્રાફ માટે graphite+grafana ઇન્ટિગ્રેશન સાથે icinga2.

icinga2 માં apply નિયમોની લવચીકતાને કારણે, ડેવલપર્સ ફક્ત તે જ સેવાઓ જોઈ શકે છે જેની સૂચનાઓ તેમને મળે છે.

અને icinga2 director દ્વારા, પ્રોગ્રામર્સ સરળતાથી પોતાની તપાસ મોટા પાયે શૂન્ય ઝંઝટ સાથે વ્યાખ્યાયિત કરી શકે છે (જે તેઓ દર થોડા દિવસે કરે છે - 100 તપાસ બહાર જાય છે, 100 અન્ય તપાસ અંદર આવે છે).


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

હાલમાં અમારી પાસે શું છે:

મેટ્રિક્સ માટે DataDog

એપ્લિકેશન નિરીક્ષણ માટે New Relic

લોગ માટે ELK (Elastic Search + Logstash + Kibana)

અપવાદ લોગ કરવા માટે Sentry (સ્વ-હોસ્ટેડ)

ચેતવણી માટે ઇમેઇલ + Slack + VictorOps (ગંભીરતાના આધારે)

અમારે શું જોઈએ છે:

મેટ્રિક્સ માટે Prometheus (વિઝ્યુલાઇઝેશન માટે Grafana)

એપ્લિકેશન નિરીક્ષણ માટે New Relic (કદાચ Elastic Search APM)

લોગિંગ માટે EFK (elastic search + fluentd + kibana). કદાચ, અમે ત્યાં પહોંચીએ ત્યાં સુધીમાં Grafana નું Loki પ્રોડ-તૈયાર થઈ જશે

અપવાદ માટે Sentry

ચેતવણીઓ માટે Alertmanager + ઇમેઇલ + VictorOps


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (જાહેરાત: VMware માં કામ કરે છે)


### Telegraf + Prometheus + InfluxDB + Grafana

CPU, ડિસ્ક, મેમરી અને નેટવર્ક જેવા સર્વર મેટ્રિક્સ માટે Telegraf. અમે અમારા નેટવર્ક ઉપકરણોના SNMP નિરીક્ષણ માટે પણ Telegraf વાપરીએ છીએ.

એપ્લિકેશન મેટ્રિક્સ માટે Prometheus. અમે અમારી એપ્લિકેશનમાં આરોગ્ય તપાસ લખીએ છીએ જેને Prometheus સ્ક્રેપ કરે છે.

સમય-શ્રેણી સંગ્રહ માટે InfluxDB. અહીં અમારો Telegraf ડેટા મોકલાય છે.

ડેશબોર્ડ અને ચેતવણી માટે Grafana. ચેતવણી એન્જિન બહુ મજબૂત નથી, પણ કામ ચલાવે છે. અમે ચેતવણીઓ Slack માં પણ મોકલીએ છીએ.

હાલમાં મારી પાસે જે નથી તે કેન્દ્રિત લોગિંગ ઉકેલ છે. ELK શક્તિશાળી છે પણ સેટ અપ અને સંચાલન કરવું મુશ્કેલ છે, અને મને એવો કોઈ મફત વિકલ્પ ખબર નથી જે જોવા લાયક પૂરતો નજીક હોય.


### Sematext + Logagent + Experience

મેટ્રિક્સ, લોગ, ટ્રેસ માટે Sematext, જલ્દી રિયલ યુઝર મોનિટરિંગ માટે પણ. મારા મતે N જુદા જુદા સાધનો/સેવાઓ વાપરવા કરતાં સરળ/સસ્તું.

લોગ મોકલવા માટે અમે rsyslog વાપરતા હતા અને પછી Logagent પર ગયા.

ફ્રન્ટએન્ડ ક્રેશ રિપોર્ટિંગ માટે અમે Sentry વાપરીએ છીએ, પણ અમે જલ્દી Experience પર જઈશું.

જાહેરાત: હું Sematext નો કર્મચારી છું.


### Azure Monitor/Analytics + OpsGenie

કાશ Log Analytics નું ઇન્ટરફેસ વધુ સારું હોત. અમે splunk થી દૂર જઈ રહ્યા છીએ, જેમાં ફરવું ઘણું સરળ હતું.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

તમે ખરેખર તમારી પોતાની સૂચના સિસ્ટમ ચલાવવા માગતા નથી. જ્યાં સુધી તમારી સુરક્ષા ટીમ Splunk પસંદ ન કરે ત્યાં સુધી તમે Splunk ને ELK થી બદલી શકો.


### Telegraf + Prometheus + Grafana + Alertmanager

કલેક્ટર તરીકે Telegraf, નિરીક્ષણ અને ચેતવણી માટે Prometheus + Alertmanager, slack ચેનલ અને ગંભીર ચેતવણીઓ માટે pagerduty સાથે ઇન્ટિગ્રેટેડ. હોસ્ટ મેટ્રિક્સના વિઝ્યુલાઇઝેશન માટે Grafana.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

મેટ્રિક્સ + ચેતવણીઓ માટે Prometheus

Prometheus ડેશબોર્ડ માટે Grafana

Prometheus ઇન્સ્ટન્સનું નિરીક્ષણ કરતું Cloudwatch

અપવાદ ટ્રેકિંગ માટે sentry

kibana + elasticsearch

graylog

batch/cronjob માટે prometheus Push Gateway

એક Prometheus ઇન્સ્ટન્સમાંથી બીજામાં મેટ્રિક્સ „push/forward“ કરવા SOP https://github.com/rapidloop/sop

ક્લાયન્ટ્સ કાં તો Prometheus ક્લાયન્ટ્સ વાપરે છે. અમે ક્લાયન્ટ બાજુએ opencensus.io વાપરવાનો પ્રયાસ કરીએ છીએ


### PagerDuty + Monitis

PagerDuty + Monitis. ઉપરાંત કેટલીક સેવાઓના આરોગ્યની ચકાસણી માટે કેટલાક કસ્ટમ Azure Functions.

આ વર્ષે Prometheus અને Grafana લાવવાનું વિચારી રહ્યા છીએ


### Prometheus + Grafana + Bosun

સમય-શ્રેણી ડેટા સંગ્રહવા માટે Prometheus. વિઝ્યુલાઇઝેશન માટે Grafana. ચેતવણી વ્યવસ્થાપન માટે Bosun.


### Azure Monitor/Analytics/Insights/Dashboards

માત્ર Azure ની દુકાન, Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Prometheus દ્વારા Kubernetes માં કન્ટેનર સેવાઓના નિરીક્ષણ માટે Grafana

મુખ્યત્વે વેબ API અને વેબ એપ્લિકેશનો માટે એન્ડ-ટુ-એન્ડ સેવા નિરીક્ષણ માટે Monitis

ચેતવણી વ્યવસ્થાપન માટે OpsGenie

અમારી સિસ્ટમોમાંથી સ્થિતિ માહિતી મેળવવા માટે Slack


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

અહીં લાંબા સમયનો (dev)ops એન્જિનિયર. Nagios પર મોટો થયો. મારા બૂટસ્ટ્રેપ્ડ SaaS https://checklyhq.com પર અભિપ્રાયો મેળવવા ગમશે. અમે ઠીકઠીક ઊંડી ચેતવણી સાથે API નિરીક્ષણ અને સાઇટ ટ્રાન્ઝેક્શન નિરીક્ષણ કરીએ છીએ.

મેં Checkly શરૂ કર્યું કારણ કે API ક્ષેત્રમાં સક્રિય / સિન્થેટિક નિરીક્ષણ થોડું મર્યાદિત (અને મોંઘું) હતું. બ્રાઉઝર-આધારિત / સ્ક્રિપ્ટેડ નિરીક્ષણ તો વધુ માલિકીનું અને મોંઘું છે. અમે Puppeteer વાપરીએ છીએ અને કિંમતો શક્ય તેટલી ઓછી રાખીએ છીએ.

અમારો નિરીક્ષણ સ્ટેક:

Checkly (પોતાનું ખાવાનું જાતે ચાખવું...)

AppOptics (કસ્ટમ ગ્રાફિંગ)

SMS સંદેશા માટે AWS Cloudwatch & SNS.

બિલ્ટ-ઇન Heroku ચેતવણી.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana અમને ઇન્ફ્રાસ્ટ્રક્ચર સમસ્યાઓ કે કામગીરી ઘટાડા વિશે slack માં ચેતવે છે, અને અમે logz.io ને એપ્લિકેશન સ્તરના ભૂલ-સ્તરના લોગની ચોક્કસ માત્રા પર slack માં ચેતવણી આપવા રૂપરેખાંકિત કર્યું છે.


### SignalFX + Splunk + PagerDuty + Slack

હાલમાં વાપરી રહ્યા છીએ: SignalFX, Splunk, PagerDuty અને Slack. હું SignalFX નો મોટો ચાહક નથી જોકે તેમની સહાય ટીમ ખૂબ મિત્રતાપૂર્ણ અને પ્રતિભાવશીલ છે. મને Splunk (જો પોસાય તો યોગ્ય), PagerDuty અને Slack ગમે છે.

હું TICK સ્ટેક વાપરતો હતો જ્યાં મોટાભાગે C ખરેખર G હતો, એટલે કે Grafana જોકે મેં Chronograf થોડું વાપર્યું. તે અદ્ભુત હતું પણ સંચાલન મુશ્કેલ હતું. SaaS વિરુદ્ધ સ્વ-હોસ્ટિંગની ક્લાસિક દુવિધા.

મેં DataDog, New Relic, Graylog, ELK અને BugSnag વાપર્યા છે. મને DataDog અને New Relic ખૂબ ગમે છે, Graylog ઠીકઠીક સારું છે. હું ELK નો મોટો ચાહક નથી. BugSnag સરસ છે, મને ખરેખર લાગે છે કે ભૂલો/અપવાદો ટ્રેક કરવા એ ઘણા કિસ્સામાં સંપૂર્ણ લોગ નિરીક્ષણનો ઠીકઠીક વિકલ્પ છે.


### ELK + Prometheus + Grafana

બીજાઓની જેમ જ, અમે લોગ માટે ELK અને બાકી બધા માટે Prometheus+Grafana વાપરીએ છીએ.

આ સેટઅપ જાળવવું સરળ છે જો તમે તમારી જાતને ક્યારેક ડેટા ગુમાવવાની પરવાનગી આપો. ઉદાહરણ તરીકે, જો અમારો ElasticSearch ડેટાબેઝ ગરબડમાં આવે (જે દુર્ભાગ્યે અમારા માટે દર 2-3 મહિને થાય છે) તો અમે HA ની ઝંઝટમાં પડતા નથી અને તેના બદલે ડેટા ફેંકી દઈને જીવન આગળ ચલાવીએ છીએ. જો તમારે ચોક્કસપણે HA કે લાંબા ગાળાની જાળવણી જોઈએ, તો શુભેચ્છા.


### Datadog + Prometheus + Grafana

મેં Datadog મહિને-મહિને સેટ કર્યું કારણ કે જ્યારે હું અહીં આવ્યો ત્યારે કોઈ નિરીક્ષણ અને કોઈ ચેતવણી નહોતી. ફક્ત અમારી થોડી સાઇટ્સ અપટાઇમ માટે દર 5 મિનિટે મોનિટર થતી હતી. Datadog નિઃશંકપણે સેટ કરવા માટે સૌથી સરળ છે. જ્યારે હું અન્ય બધી સમસ્યાઓ ઉકેલી લઈશ, ત્યારે હું Prometheus+Grafana પર જઈશ. લોગ વ્યવસ્થાપન પર હજુ 100% નક્કી નથી.


### Nagios + ELK

અમારી પાસે 100+ થી વધુ ઉત્પાદનો છે જેને અમે ટેકો આપીએ છીએ.

ઓન-પ્રિમ માટે, મોટાભાગે Nagios અને ELK. ક્લાઉડ માટે, અમે DataDog થી NewRelic પર સ્થળાંતર કરી રહ્યા છીએ.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

અમે datadog વાપરતા હતા પરંતુ જણાયું કે તે અમારી જરૂરિયાતો માટે ખૂબ મોંઘું છે. ખોટું ન સમજશો તે અદ્ભુત છે, પણ તેનો મોટો ખર્ચ છે. અમે DD ના ખર્ચના લગભગ 2-3 મહિના જેટલા વાર્ષિક સબ્સ્ક્રિપ્શન સાથે site24x7.com સેટ કરી શક્યા.

અમારો નિરીક્ષણ સ્ટેક:

Site24x7 - APM, બાહ્ય URL નિરીક્ષણ, SMTP મેઇલફ્લો નિરીક્ષણ, ssl સમાપ્તિઓ અને પ્રક્રિયા નિરીક્ષણ.

StatusCake - URL નિરીક્ષણ અને પુષ્ટિ માટે - જો site24x7 કંઈક ચૂકી જાય તો તે અમારું બેકઅપ છે (તે ચૂકતું નથી) પરંતુ SC અમારી જરૂરિયાતો માટે બાહ્ય પોર્ટ અને સેવા નિરીક્ષણ માટે વધુ લવચીક છે.

બંને સાધનો PagerDuty પર વધારે છે, અને પછી અમને slack માં અમારા વધારા મળે છે.

SumoLogic - લોગ નિરીક્ષણ માટે (તે મહાન સાધન છે પણ અમારી જરૂરિયાતો માટે થોડું જટિલ)

slack માંથી અમે ચેતવણી ack કે નિવારણ કરી શકીએ છીએ.

પછી અમારી પાસે ઘણા site24x7 સ્વચાલનો છે જે 'BedOps' માટે commando.io સાથે જોડાય છે જેને અમે એમ કહીએ છીએ - જ્યાં ચેતવણી ટ્રિગર થાય છે, અમે પરિસ્થિતિ સુધારવાના પ્રયાસ તરીકે થોડી સ્ક્રિપ્ટ કે સ્વચાલનો શરૂ કરીએ છીએ (99% સમય સ્વચાલન + અમારી સ્ક્રિપ્ટ અમને મુશ્કેલીથી દૂર રાખે છે)

જ્યારે સ્વચાલન નિષ્ફળ જાય અથવા કંઈક વ્યાપની બહારનું હોય જે ઠીક કરવાનું હોય ત્યારે માટે અમારી પાસે અમારા KB માં આંતરિક runbook છે.


### Prometheus + AlertManager + Grafana + Stackdriver

અમારા GKE ક્લસ્ટર્સ અને VM માં મેટ્રિક્સ માટે Prometheus (Operator) / AlertManager / Grafana.

લોગ માટે Google Stackdriver (કારણ કે તે સમાવિષ્ટ અને ડિફોલ્ટ રૂપે સક્રિય છે અને હાલમાં અમારી જરૂરિયાતો માટે પૂરતું છે).


### Zabbix

બધા માટે Zabbix. કોઈ વધારાના સોફ્ટવેરની જરૂર નથી.
