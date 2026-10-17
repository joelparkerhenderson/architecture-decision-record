# متریک، مانیتور، هشدار

فهرست مطالب:

* [خلاصه](#خلاصه)
  * [مسئله](#مسئله)
  * [تصمیم](#تصمیم)
  * [وضعیت](#وضعیت)
* [جزئیات](#جزئیات)
  * [مفروضات](#مفروضات)
  * [قیود](#قیود)
  * [مواضع](#مواضع)
  * [استدلال](#استدلال)
  * [پیامدها](#پیامدها)
* [مرتبط](#مرتبط)
  * [تصمیمات مرتبط](#تصمیمات-مرتبط)
  * [الزامات مرتبط](#الزامات-مرتبط)
  * [مصنوعات مرتبط](#مصنوعات-مرتبط)
  * [اصول مرتبط](#اصول-مرتبط)
* [توضیحات](#توضیحات)
  * [پیام‌های متنی آزاد در برابر پیام‌های رویداد ساختاریافته](#پیامهای-متنی-آزاد-در-برابر-پیامهای-رویداد-ساختاریافته)
  * [Graylog آسان‌تر است](#graylog-آسانتر-است)
  * [Prometheus کمی تنظیم می‌خواهد](#prometheus-کمی-تنظیم-میخواهد)
  * [سرویس‌های AWS ترکیبی هستند](#سرویسهای-aws-ترکیبی-هستند)
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


## خلاصه


### مسئله

می‌خواهیم از سنجه‌ها، پایشگرها و هشدارها استفاده کنیم، زیرا می‌خواهیم بدانیم برنامه‌های ما چقدر خوب کار می‌کنند و بدانیم چه زمانی مشکلی وجود دارد.


### تصمیم

WIP (در دست انجام).


### وضعیت

در حال جمع‌آوری اطلاعات. از دو سر محتمل طیف شروع می‌کنیم: پرتوصیه‌ترین ابزار رایگان قدیمی‌تر (Nagios) و پرتوصیه‌ترین ابزار پولی جدیدتر (New Relic).


## جزئیات


### مفروضات

می‌خواهیم برنامه‌های وبی بسازیم که مدرن، سریع، قابل‌اعتماد، واکنش‌گرا و غیره باشند.

می‌خواهیم به‌جای ساختن، بخریم.


### قیود

ابزارهایی می‌خواهیم که با خط‌لولهٔ devops و ابرهای استقرار ما خوب کار کنند.


### مواضع

اکنون در حال پژوهش دربارهٔ مواضع هستیم.


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

  

  
### استدلال

تاکنون Nagios و New Relic دو سر طیف هستند. Nagios قدیمی‌ترین، ساده‌ترین، رایگان و ابزار عملی است. New Relic جدیدترین ویژگی‌ها، کامل‌ترین، پولی و ابزار عملی است. با ارزیابی این‌ها شروع می‌کنیم. در صورت نیاز، به درون طیف حرکت می‌کنیم.  

تاکنون Zabbix بهترین توصیه‌ها را دارد و همچنین کامل‌ترین قابلیت‌ها را ارائه می‌دهد.

تاکنون ELK بهترین محبوبیت متن‌باز در مسیر ساختن به‌جای خریدن را دارد.

تاکنون Prometheus + Graphana بهترین محبوبیت را دارند.


### پیامدها

TODO (باید انجام شود).


## مرتبط


### تصمیمات مرتبط

این انتخاب‌ها بر قابلیت آزمون، تله‌متری و احتمالاً سیستم‌های دیگر مانند خدمات مشتری، مهندسی قابلیت اطمینان سایت و غیره تأثیر خواهند گذاشت.


### الزامات مرتبط

TODO (باید انجام شود).


### مصنوعات مرتبط

TODO (باید انجام شود).


### اصول مرتبط

به‌آسانی برگشت‌پذیر.

نیاز به سرعت.


## توضیحات

یک پشتهٔ متن‌باز نسبتاً خوب این است:

* Prometheus برای سنجه‌ها و هشداردهی بر پایهٔ سنجه‌ها

* Grafana برای نمایش سنجه‌ها

* Elasticsearch/Logstash/Kibana (ELK) برای لاگ‌ها و رویدادهای ساختاریافته

* Pushover برای اعلان‌های موبایل


### پیام‌های متنی آزاد در برابر پیام‌های رویداد ساختاریافته

پیام‌های متنی آزاد: برای مثال، همان چیزهای تصادفی‌ای که در /var/log/messages پیدا می‌کنید، و چیزی که برنامه عمداً تولید می‌کند. این پیام‌ها برای شناسایی چیزهای دیگری که روی دستگاه رخ می‌دهند، مانند کمبود حافظه یا خطاهای سخت‌افزاری، مفیدند، اما آشغال زیادی دارند. 

پیام‌های رویداد ساختاریافته: تولیدشده توسط برنامه، با مجموعه‌ای ثابت یا پویا از ویژگی‌ها، مثلاً لاگ درخواست HTTP، لاگ حسابداری، ورود کاربر.

به‌طور کلی، خوب است جزئیات هر درخواست را به شکلی لاگ کنید که بتوانید بر پایهٔ ویژگی‌ها عمیق‌تر شوید. بنابراین افزودن مثلاً userid یا sessionid به همه‌چیز امکان ردیابی می‌دهد. البته ردیابی صریح نیز خوب است. استفاده از ELK برای این کار نوعی نسخهٔ فقیرانهٔ https://www.honeycomb.io/ است


### Graylog آسان‌تر است

بر پایهٔ تجربهٔ من، راه‌اندازی Graylog آسان‌تر است.


### Prometheus کمی تنظیم می‌خواهد

من به‌طور کلی از Prometheus برای سنجه‌ها راضی‌ام. هشداردهی کمی تنظیم می‌خواهد، اما کاملاً خوب است. به برنامهٔ شما بستگی دارد. فکر می‌کنم بهتر است روی شرایط قابل‌مشاهده برای کاربر نهایی هشدار داده شود، نه علل زیربنایی. برای مثال، زمان بارگذاری صفحه خوب است، تعداد درخواست در ثانیه نه. هرچند صفر درخواست در ثانیه نشان می‌دهد چیزی اشتباه است.

مزیت یک سرویس این است که هوشمندی اضافی را به‌صورت آماده ارائه می‌دهد. من عموماً Datadog را دوست دارم. اگر داده‌های زیادی دارید، سرویس‌ها می‌توانند به‌طرز ترسناکی گران باشند، و گاهی مدل‌های قیمت‌گذاری دارند که با ابر سازگار نیستند، مثلاً دریافت هزینه به‌ازای هر نمونه (instance) در حالی که نمونه‌ها پویا هستند. همچنین تفاوتی هست میان سرویس‌هایی که هر درخواست از یک کاربر پرداخت‌کننده است و آن‌هایی که به تبلیغات مربوط‌اند و فقط درصد کمی از درخواست‌ها برای شما درآمد دارند. ممکن است داده‌های زیادی داشته باشید و بودجهٔ چندانی نه.

من روی سرویس‌هایی کار می‌کنم که روزانه 1 میلیارد درخواست می‌گیرند، بنابراین میزبانی پایش و لاگ‌گیری خودمان منطقی است. اگر حجم شما کمتر است، سرویس‌های میزبانی‌شده آسان‌ترند.


### سرویس‌های AWS ترکیبی هستند

تجربهٔ من از سرویس‌های AWS ترکیبی بوده است. سرویس Elasticsearch آن‌ها ناپایدار بوده، بنابراین برای آن نمونه‌های خودمان را اجرا می‌کنیم. سنجه‌های CloudWatch گران‌اند، بنابراین عموماً فقط برای سنجه‌های سطح «زیرساخت» از آن‌ها استفاده می‌کنیم، نه برای برنامه، یعنی سنجه‌های مرتبط با سلامت که در آن‌ها AWS بهتر از نرم‌افزار در حال اجرا روی نمونه می‌تواند بداند چه خبر است. CloudWatch Logs می‌تواند در به‌روزرسانی کند باشد و فراداده چندانی ندارد. اجرای ELK به این کمک می‌کند. اگر واقعاً داده بی‌درنگ بخواهم، استفاده از Kafka به‌عنوان وسیلهٔ انتقال لاگ‌ها بهتر است. این را Logstash نسبتاً خوب پشتیبانی می‌کند. با این حال، مدیریت یک خوشهٔ Kafka کار آدم‌های ضعیف‌دل نیست، لوله‌کشی آشکار زیادی دارد.


### Kafka

نظر: Kafka گاهی می‌تواند فوق‌العاده دردسرساز باشد، یا Kafka می‌تواند محکم مثل صخره باشد و تقریباً فراموش می‌کنید که آنجاست و همه‌چیز را به هم گره می‌زند. 


نظر: Kafka محکم بوده است، اما راه انداختنش شگفت‌انگیز زحمت داشت. آن را مثل یک پایگاه داده رابطه‌ای می‌بینم اما جایی که فقط در لایهٔ «فیزیکی» کار می‌کنید، مثلاً tablespaceها، فایل‌ها و پارتیشن‌ها. اوایل زمان‌هایی بود که ابزارهای مدیریتی کم بودند و مجبور شدیم برنامه‌هایی بنویسیم تا مثلاً یک consumer group را بازنشانی کنیم. http://howfuckedismydatabase.com/nosql/

نظر: ما از Kafka به‌عنوان «بافر» برای پیام‌های لاگ و جایی استفاده می‌کنیم که بتوانیم پردازش جریان بی‌درنگ را روی داده‌هایی که از چندین سرور می‌آیند انجام دهیم. اگر حملهٔ DDOS بخوریم، راهی برای تحلیل داده در چندین نمونه لازم داریم. اگر مستقیماً از سرورها به ELK لاگ کنیم، بار می‌تواند خوشهٔ Elasticsearch را منفجر کند.

نظر: Kafka برای ما خوب است چون اگر حملهٔ DDOS بخوریم، راهی برای تحلیل داده در چندین نمونه لازم داریم. اگر مستقیماً از سرورها به ELK لاگ کنیم، بار می‌تواند خوشهٔ Elasticsearch را منفجر کند.


نظر: Kafka کار کمتری انجام می‌دهد و کارآمدتر است، بنابراین می‌تواند بار را بهتر تحمل کند. و ما کار Kafka را در صف می‌گذاریم و دوباره تلاش می‌کنیم. و سربار بیش‌ازحد Kafka بر کاربرانی که می‌خواهند با Kibana کار تعاملی انجام دهند تأثیر نمی‌گذارد، برخلاف وقتی که Elasticsearch به زحمت افتاده باشد.

نظر:  پردازش جریان بیشتر به دنبال سوءاستفاده است، مثلاً ترافیک بیش‌ازحد از یک IP واحد در کل خوشه، و سپس به اشتراک گذاشتن مسدودسازی در کل خوشه.

نظر: افزونهٔ logstash-output-kafka فعلاً کاملاً غیرقابل‌اعتماد است. چند مشکل از صفحهٔ issueهای GitHub آن مرا گزیده که به نظر می‌رسد هرگز رفع نمی‌شوند. می‌خواهم از استفاده از آن دور شوم و مستقیماً از برنامه‌هایمان به Kafka بفرستم.

نظر: اکنون رویدادهای ساختاریافته را مستقیماً از برنامه به Kafka می‌فرستیم. انگیزهٔ اصلی کمتر دست زدن به داده‌های لاگ و پرهیز از چندبار خواندن و نوشتن روی دیسک بود. در سیستم‌های با حجم بالا، لاگ‌گیری می‌تواند از خود برنامه کار بیشتری ببرد. به این فکر می‌کنم که journald را هم وادار کنم مستقیماً از یک برنامهٔ C لاگ بفرستد.


### Loki

Loki را از نزدیک زیر نظر داشته باشید. هنوز آماده نیست اما وقتی آماده شود انتظار دارم در این پشته تناسب بهتری باشد. Loki یک جمع‌آورندهٔ لاگ است که grafana labs ساخته و از نحو scraping و تگ مشابه Prometheus استفاده می‌کند.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

Prometheus + alertmanager برای سنجه‌ها. <3 Prometheus.

Rollbar/Graylog برای لاگ‌گیری/گزارش خطا (کمی همپوشانی هست؛ یک سرویس کوچک احتمالاً به هر دو نیاز ندارد).

فعلاً هشدارها فقط به یکی از چند کانال Slack می‌روند که طرف‌های علاقه‌مند اعلان‌هایشان را روشن کرده‌اند. اگر دربارهٔ on-call جدی‌تر بودیم، به PagerDuty/VictorOps/و غیره می‌رفتند.

Grafana برای نمودارها و داشبورد. همچنین مشتاقانه منتظرم ببینم آیا امکانات لاگ‌گیری آیندهٔ آن‌ها نیاز به Graylog را از بین می‌برد.


### Thanos

ما از Thanos به‌عنوان فرانت‌اند برای راه‌اندازی HA خود استفاده می‌کنیم. می‌داند چگونه جفت‌های HA را حذف تکرار کند.

فعلاً 6 ماه داده محلی Prometheus را نگه می‌داریم. این برای ما به‌طور معقولی خوب کار می‌کند. اما همین الان وسط پیاده‌سازی ذخیره‌سازی bucket برای راه‌اندازی Thanos خود برای ذخیرهٔ بلندمدت داده هستم. در تئوری، ذخیره‌سازی GCS حدود 30% ارزان‌تر از دیسک پایدار استاندارد GCE است که اکنون استفاده می‌کنیم.

فعلاً از داده‌های Prometheus پشتیبان نمی‌گیریم. داده‌ها فراتر از داشتن به‌اندازهٔ کافی برای هشداردهی واقعاً برای ما مهم نیستند. استقرار کلی ناوگان ما سال به سال آن‌قدر تغییر می‌کند که داده‌های تاریخی قدیمی‌تر از چند ماه واقعاً جالب نیست. شاید داشتن چند آمار هسته سال به سال جالب باشد، ممکن است مجموعه‌ای از قوانین ضبط آمار هسته راه بیندازم و آن‌ها را با Federation ذخیره کنم یا بگذارم Thanos مراقبش باشد.

ویرایش: سلب مسئولیت کوچک، من توسعه‌دهندهٔ Prometheus هستم.


### Prometheus HA

HA در Prometheus با تکرار انجام می‌شود، چند poppers اجرا می‌کنید، راه‌هایی برای poll کردن چندتا و حذف تکرار داده هست

مقیاس‌دهی با تصمیم‌گیری دربارهٔ شبکه و داشتن Prometheusهای مختلف برای poll کردن بخش‌های مختلف شبکه است

ذخیرهٔ بلندمدت نقطهٔ قوت prom نیست اما به چیزی مثل influx یا timescaledb (که از نظر فنی تیک HA را هم می‌زند) واگذار می‌شود، مقاله‌ای که دربارهٔ آن خواندم https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

بخش بلندمدت را هنوز امتحان نکرده‌ام چون هنوز فقط آزمایش می‌کنم و از آن برای نمودارهای کوتاه‌مدت استفاده می‌کنم، در حالی که librenms برای بلندمدت شبکهٔ من را پایش می‌کند


### Datadog + PagerDuty + Threat Stack

ما از Datadog (همراه PagerDuty) و Threat Stack استفاده می‌کنیم و نمی‌توانستیم خوشحال‌تر باشیم. تنها گلایهٔ من از DD هزینهٔ نسبتاً بالای ذخیره‌سازی سنجه است.


### Zabbix

Zabbix با اسکریپت‌های سفارشی برای پایش تقریباً همه‌چیز. مثل جادو کار می‌کند.


### Outlyer

من از Outlyer استفاده می‌کنم، اما باید اعلام کنم که اینجا کار می‌کنم و استفاده از محصول خودمان واجب است.

هنوز Graylog، Sentry و Statuscake برای تکمیل لازم است.

جانبدارانه به نظر می‌رسد، اما پس از اجرای خوشحال‌کنندهٔ Nagios و سایر سیستم‌های پایش به‌صورت درون‌سازمانی، در هر کار جدیدی راه‌حل میزبانی‌شده می‌خرم و آن درد را واگذار می‌کنم.


### Nagios + Nagiosgraph

ما Nagios را برای همهٔ پایش و هشداردهی اجرا می‌کنیم. هشدارها از طریق ایمیل (هشدارها و اعلان‌های بحرانی) و اعلان‌های شنیداری برنامه (برای هشدارهای بحرانی) رخ می‌دهند.

Nagiosgraph برای مصورسازی استفاده می‌شود.

این راه‌اندازی در آگاه نگه داشتن جامع ما از آنچه در محیطمان رخ می‌دهد بسیار مؤثر بوده است. حدود 110 سرور حیاتی و حدود 760 نقطه داده را اجرا و پایش می‌کنیم و بیش از هفت سال است که این سیستم صبحگاهی برقرار است.

دوست دارم گاهی لاگ‌ها را هم با Graylog یا ELk جمع کنم.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager از طریق helm chart فوق‌العادهٔ Prometheus Operator. لاگ همچنان به طرح birch در LogDNA می‌رود چون متوجه شدیم ELK برای خوشهٔ فروتن 3 تا 5 گرهٔ ما روی GKE بیش‌ازحد سنگین است.


### DataDog + Sentry + PagerDuty.

من همهٔ راه‌حل‌های پایش خودم را اجرا می‌کردم، با استفاده از انواع نرم‌افزارها از جمله Nagios، Icinga، Zabbix، ELK، Greylog2، Influx و بسیاری ابزار دیگر، اما حقیقت این است که اجرای زیرساخت پایش خودتان تلاش زیادی می‌طلبد، به‌ویژه وقتی می‌توانید با نرخ‌های بسیار پایین به کس دیگری پول بدهید تا برایتان انجامش دهد!

پرداخت به دیگران برای اجرای زیرساخت پایش مشتریان من را آزاد می‌کند تا به‌جای پایشِ پایش روی اجرای پلتفرم‌هایشان تمرکز کنند، یعنی ارزشی که از پایداری پلتفرمشان به دست می‌آورند بسیار فراتر از هر هزینهٔ پایش به‌عنوان سرویس است.


### Sensu + Graphite + ELK

شرکت من واقعاً به چیزهای خودمیزبان علاقه‌مند است.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager برای هشداردهی، تیم من باور دارد پایش ساده پایش خوب است.

سیستم‌های دیگر مانند لاگ‌گیری و ردیابی وقتی فرد on-call هشداری دریافت می‌کند زمینهٔ غنی برای تشخیص فراهم می‌کنند، اما ما هرگز هشداردهی را روی این‌ها نمی‌سازیم.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

سرویس‌های ابزارگذاری‌شده با Prometheus => تحلیل و مصورسازی Circonus


### icinga2 + VictorOps + NewRelic + Sentry + Slack

از سرویس‌های زیر استفاده می‌کنیم:

icinga2 برای پایش و VictorOps برای هشداردهی

NewRelic برای پایش تفصیلی سرویس

Sentry برای ردیابی خطا در سرویس

Slack/ایمیل بخشی از هشداردهی است که از NewRelic یا icinga2 فعال می‌شود


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 با ادغام elasticsearch برای تحلیل و ادغام graphite+grafana برای نمودارها.

به لطف انعطاف قوانین apply در icinga2، توسعه‌دهندگان فقط سرویس‌هایی را می‌بینند که اعلان‌هایش را دریافت می‌کنند.

و از طریق icinga2 director، برنامه‌نویسان به‌آسانی می‌توانند بررسی‌های خودشان را در مقیاس بزرگ و بدون دردسر تعریف کنند (که هر چند روز یک‌بار انجام می‌دهند - 100 بررسی بیرون می‌رود، 100 بررسی دیگر داخل می‌آید).


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

اکنون چه داریم:

DataDog برای سنجه‌ها

New Relic برای پایش برنامه

ELK (Elastic Search + Logstash + Kibana) برای لاگ‌ها

Sentry (خودمیزبان) برای ثبت استثناها

ایمیل + Slack + VictorOps برای هشداردهی (بر پایهٔ شدت)

چه می‌خواهیم داشته باشیم:

Prometheus برای سنجه‌ها (Grafana برای مصورسازی)

New Relic (احتمالاً Elastic Search APM) برای پایش برنامه

EFK (elastic search + fluentd + kibana) برای لاگ‌گیری. شاید تا زمانی که به آنجا برسیم Loki از Grafana آمادهٔ تولید باشد

Sentry برای استثناها

Alertmanager + ایمیل + VictorOps برای هشدارها


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (سلب مسئولیت: در VMware کار می‌کنم)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf برای سنجه‌های سرور مانند CPU، دیسک، حافظه و شبکه. از Telegraf برای پایش SNMP دستگاه‌های شبکهٔ خود هم استفاده می‌کنیم.

Prometheus برای سنجه‌های برنامه. بررسی‌های سلامت را در برنامهٔ خود کد می‌کنیم که Prometheus آن‌ها را scrape می‌کند.

InfluxDB برای ذخیرهٔ سری‌زمانی. داده‌های Telegraf ما به اینجا فرستاده می‌شود.

Grafana برای داشبوردها و هشدارها. موتور هشداردهی فوق‌العاده مقاوم نیست، اما کار را راه می‌اندازد. هشدارها را به Slack هم می‌فرستیم.

چیزی که اکنون ندارم راه‌حل لاگ‌گیری متمرکز است. ELK قدرتمند است اما راه‌اندازی و مدیریتش دشوار است و جایگزین رایگانی که آن‌قدر نزدیک باشد که ارزش بررسی داشته باشد نمی‌شناسم.


### Sematext + Logagent + Experience

Sematext برای سنجه‌ها، برای لاگ‌ها، برای ردها، به‌زودی برای پایش کاربر واقعی هم. به نظر من ساده‌تر/ارزان‌تر از استفاده از N ابزار/سرویس مختلف.

برای ارسال لاگ قبلاً از rsyslog استفاده می‌کردیم و بعد به Logagent رفتیم.

برای گزارش کرش فرانت‌اند از Sentry استفاده می‌کنیم، اما به‌زودی به Experience می‌رویم.

سلب مسئولیت: من یک Sematextan هستم.


### Azure Monitor/Analytics + OpsGenie

کاش Log Analytics رابط بهتری داشت. از splunk دور می‌شویم که گشت‌وگذار در آن بسیار آسان‌تر بود.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

واقعاً نمی‌خواهید سیستم اعلان خودتان را اجرا کنید. می‌توانید Splunk را با ELK جایگزین کنید مگر اینکه تیم امنیت شما Splunk را ترجیح دهد.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf به‌عنوان جمع‌آورنده، Prometheus + Alertmanager برای پایش و هشداردهی، یکپارچه با کانال‌های slack و pagerduty برای هشدارهای بحرانی. Grafana برای مصورسازی سنجه‌های میزبان.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus برای سنجه‌ها + هشدارها

Grafana برای داشبوردهای Prometheus

Cloudwatch که نمونه‌های Prometheus را پایش می‌کند

sentry برای ردیابی استثنا

kibana + elasticsearch

graylog

prometheus Push Gateway برای batch/cronjobها

SOP https://github.com/rapidloop/sop برای «فشار دادن/ارسال» سنجه‌ها از یک نمونهٔ Prometheus به دیگری

کلاینت‌ها یا از کلاینت‌های Prometheus استفاده می‌کنند. سعی می‌کنیم در سمت کلاینت از opencensus.io استفاده کنیم


### PagerDuty + Monitis

PagerDuty + Monitis. همچنین چند Azure Function سفارشی برای آزمودن سلامت برخی سرویس‌ها.

امسال دنبال معرفی Prometheus و Grafana هستم


### Prometheus + Grafana + Bosun

Prometheus برای ذخیرهٔ داده‌های سری‌زمانی. Grafana برای مصورسازی. Bosun برای مدیریت هشدار.


### Azure Monitor/Analytics/Insights/Dashboards

شرکتی فقط-Azure، Azure Monitor، Log Analytics، App Insights، Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana برای پایش سرویس‌های کانتینری در Kubernetes از طریق Prometheus

Monitis برای پایش سرویس سرتاسری عمدتاً برای API‌های وب و برنامه‌های وب

OpsGenie برای مدیریت هشدار

Slack برای دریافت اطلاعات وضعیت از سیستم‌هایمان


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

اینجا مهندس باسابقهٔ (dev)ops هستم. با Nagios بزرگ شدم. دوست دارم دربارهٔ SaaS خودساختهٔ من https://checklyhq.com نظر بشنوم. ما پایش API و پایش تراکنش سایت را با هشداردهی نسبتاً عمیق انجام می‌دهیم.

Checkly را شروع کردم چون پایش فعال / مصنوعی در حوزهٔ API کمی محدود (و گران) بود. پایش مبتنی بر مرورگر / اسکریپتی حتی انحصاری‌تر و گران‌تر است. ما از Puppeteer استفاده می‌کنیم و قیمت را تا حد امکان پایین نگه می‌داریم.

پشتهٔ پایش ما:

Checkly (استفاده از محصول خودمان...)

AppOptics (نمودارسازی سفارشی)

AWS Cloudwatch و SNS برای پیام‌های SMS.

هشداردهی داخلی Heroku.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana ما را از مشکلات زیرساخت یا افت کارایی در slack آگاه می‌کند، و logz.io را پیکربندی کرده‌ایم که روی حجم مشخصی از لاگ‌های سطح خطا از لایهٔ برنامه در slack هشدار دهد.


### SignalFX + Splunk + PagerDuty + Slack

فعلاً استفاده می‌کنم: SignalFX، Splunk، PagerDuty و Slack. طرفدار بزرگ SignalFX نیستم هرچند تیم پشتیبانی‌شان فوق‌العاده دوستانه و پاسخگو است. Splunk را دوست دارم (اگر بتوانید هزینه‌اش را بپردازید می‌ارزد)، PagerDuty و Slack را هم.

قبلاً از پشتهٔ TICK استفاده می‌کردم که در آن بیشتر C در واقع G بود، یعنی Grafana، هرچند کمی هم Chronograf استفاده کردم. عالی بود اما مدیریتش دردسر داشت. معضل کلاسیک SaaS در برابر میزبانی شخصی.

DataDog، New Relic، Graylog، ELK و BugSnag را استفاده کرده‌ام. DataDog و New Relic را خیلی دوست دارم، Graylog کاملاً خوب است. طرفدار بزرگ ELK نیستم. BugSnag خوب است، در واقع احساس می‌کنم ردیابی خطاها/استثناها در بسیاری موارد جایگزین کاملاً خوبی برای پایش کامل لاگ است.


### ELK + Prometheus + Grafana

مثل بقیه، ما از ELK برای لاگ‌ها و از Prometheus+Grafana برای هر چیز دیگر استفاده می‌کنیم.

اگر به خودتان اجازه بدهید گاهی داده از دست بدهید، نگهداری این راه‌اندازی آسان است. برای مثال، اگر پایگاه داده ElasticSearch ما به وضعیت بد بیفتد (که متأسفانه هر 2 تا 3 ماه برای ما رخ می‌دهد) سراغ HA نمی‌رویم و در عوض داده را دور می‌ریزیم و به زندگی‌مان ادامه می‌دهیم. اگر مطلقاً HA یا نگهداشت بلندمدت لازم دارید، موفق باشید.


### Datadog + Prometheus + Grafana

Datadog را ماه‌به‌ماه راه انداختم چون وقتی به اینجا آمدم هیچ پایش و هیچ هشداردهی‌ای نبود. فقط چند سایت از سایت‌های ما هر 5 دقیقه برای آپ‌تایم پایش می‌شدند. Datadog بی‌هیچ تردید آسان‌ترین برای راه‌اندازی است. وقتی رسیدگی به همهٔ مسائل دیگر را تمام کنم، به Prometheus+Grafana تغییر می‌دهم. دربارهٔ مدیریت لاگ هنوز 100% تصمیم نگرفته‌ام.


### Nagios + ELK

بیش از 100 محصول داریم که پشتیبانی می‌کنیم.

برای درون‌سازمانی بیشتر Nagios و ELK است. برای ابر، از DataDog به NewRelic مهاجرت می‌کنیم.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

قبلاً datadog استفاده می‌کردیم اما دیدیم برای نیازهای ما بیش‌ازحد گران است. اشتباه نفهمید، شگفت‌انگیز است اما هزینهٔ عظیمی دارد. توانستیم site24x7.com را با اشتراک سالانه به قیمت حدود 2 تا 3 ماه هزینهٔ DD راه بیندازیم.

پشتهٔ پایش ما:

Site24x7 - APM، پایش URL بیرونی، پایش جریان نامهٔ SMTP، انقضای ssl و پایش فرایند.

StatusCake - برای پایش و تأیید URL - پشتیبان ماست اگر site24x7 چیزی را از قلم بیندازد (نمی‌اندازد) اما SC برای نیازهای ما در پایش پورت و سرویس بیرونی انعطاف‌پذیرتر است.

هر دو ابزار به PagerDuty ارجاع می‌دهند، و سپس ارجاع‌های خود را در slack می‌گیریم.

SumoLogic - برای پایش لاگ (ابزار عالی‌ای است اما برای نیازهای ما کمی پیچیده)

از slack می‌توانیم هشدار را ack کنیم یا رفع کنیم.

سپس خودکارسازی‌های site24x7 بسیاری داریم که به commando.io برای آنچه خودمان «BedOps» می‌نامیم وصل می‌شوند - جایی که هشداری فعال می‌شود، چند اسکریپت یا خودکارسازی را برای تلاش در رفع وضعیت اجرا می‌کنیم (99% مواقع خودکارسازی + اسکریپت‌هایمان ما را از دردسر دور نگه می‌دارند).

برای زمانی که خودکارسازی‌ها شکست بخورند یا چیزی خارج از دامنه باشد که باید رفع شود، runbookهای داخلی در KB خود داریم.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana برای سنجه‌ها در خوشه‌های GKE و VMهای ما.

Google Stackdriver برای لاگ‌ها (چون شامل و به‌طور پیش‌فرض فعال است و فعلاً برای نیازهای ما کافی است).


### Zabbix

Zabbix برای همه‌چیز. نیازی به نرم‌افزار اضافی نیست.
