# Métricas, monitores, alertas

Contenido:

* [Resumen](#resumen)
  * [Asunto](#asunto)
  * [Decisión](#decisión)
  * [Estado](#estado)
* [Detalles](#detalles)
  * [Supuestos](#supuestos)
  * [Restricciones](#restricciones)
  * [Posiciones](#posiciones)
  * [Argumento](#argumento)
  * [Implicaciones](#implicaciones)
* [Relacionado](#relacionado)
  * [Decisiones relacionadas](#decisiones-relacionadas)
  * [Requisitos relacionados](#requisitos-relacionados)
  * [Artefactos relacionados](#artefactos-relacionados)
  * [Principios relacionados](#principios-relacionados)
* [Notas](#notas)
  * [Mensajes de texto libre frente a mensajes de eventos estructurados](#mensajes-de-texto-libre-frente-a-mensajes-de-eventos-estructurados)
  * [Graylog is easier](#graylog-is-easier)
  * [Prometheus take some tuning](#prometheus-take-some-tuning)
  * [AWS services are mixed](#aws-services-are-mixed)
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


## Resumen


### Asunto

Queremos usar métricas, monitores y alertas, porque queremos saber qué tan bien funcionan nuestras aplicaciones y saber cuándo hay un problema.


### Decisión

En curso (WIP).


### Estado

Reuniendo información. Empezamos con los extremos plausibles del espectro: la herramienta gratuita más antigua y más recomendada (Nagios) y la herramienta de pago más reciente y más recomendada (New Relic).


## Detalles


### Supuestos

Queremos crear aplicaciones web modernas, rápidas, fiables, adaptables, etc.

Queremos comprar en lugar de construir.


### Restricciones

Queremos herramientas que funcionen bien con nuestra canalización de devops y con las nubes en las que desplegamos.


### Posiciones

Ahora estamos investigando posiciones.


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

Hasta ahora, Nagios y New Relic son los extremos del espectro. Nagios es la herramienta viable más antigua, más simple y gratuita. New Relic es la herramienta viable más reciente en funciones, más completa y de pago. Empezaremos con evaluaciones de estas. Según sea necesario, nos desplazaremos hacia el interior del espectro.  

Hasta ahora, Zabbix tiene las mejores recomendaciones y además ofrece las capacidades más completas.

Hasta ahora, ELK tiene la mejor popularidad en la opción de código abierto de construir en lugar de comprar.

Hasta ahora, Prometheus + Graphana tienen la mejor popularidad.


### Implicaciones

Pendiente (TODO).


## Relacionado


### Decisiones relacionadas

Las elecciones afectarán a la capacidad de prueba, a la telemetría y probablemente a otros sistemas, como los de atención al cliente, ingeniería de fiabilidad de sitios, etc.


### Requisitos relacionados

Pendiente (TODO).


### Artefactos relacionados

Pendiente (TODO).


### Principios relacionados

Fácilmente reversible.

Necesidad de velocidad.


## Notas


Una pila de código abierto bastante buena es:

* Prometheus para métricas y alertas basadas en métricas

* Grafana para mostrar métricas

* Elasticsearch/Logstash/Kibana (ELK) para registros y eventos estructurados

* Pushover para notificaciones móviles


### Mensajes de texto libre frente a mensajes de eventos estructurados

Mensajes de texto libre: por ejemplo, el tipo de cosas al azar que se encuentran en /var/log/messages, y algo generado intencionalmente por la aplicación. Los mensajes son útiles para identificar otras cosas que ocurren en la máquina, como falta de memoria o errores de hardware, pero tienen mucha basura. 

Mensajes de eventos estructurados: generados por la aplicación, con un conjunto fijo o dinámico de atributos, p. ej., un registro de solicitudes HTTP, un registro contable, un inicio de sesión de usuario.

En términos generales, es bueno registrar los detalles de cada solicitud de una forma que permita profundizar según los atributos. Así que añadir, p. ej., un userid o un sessionid a todo permite hacer trazas. El seguimiento explícito (tracing) también es bueno, por supuesto. Usar ELK para esto es una especie de https://www.honeycomb.io/ para pobres


### Graylog is easier

Graylog es más fácil de poner en marcha según mi experiencia.



### Prometheus take some tuning


En general estoy contento con Prometheus para las métricas. Las alertas requieren algo de ajuste, pero son bastante buenas. Depende de tu aplicación. Creo que lo mejor es alertar sobre condiciones visibles para el usuario final, no sobre las causas subyacentes. Por ejemplo, el tiempo de carga de la página es bueno, el número de solicitudes por segundo no. Aunque cero solicitudes por segundo indica que algo va mal.

La ventaja de un servicio es que ofrece inteligencia adicional lista para usar. En general me gusta Datadog. Los servicios pueden ser aterradoramente caros si tienes muchos datos, y a veces tienen modelos de precios que no son amigables con la nube, p. ej., cobrar por instancia cuando las instancias son dinámicas. También hay una diferencia entre los servicios en los que cada solicitud proviene de un usuario de pago y los relacionados con publicidad, donde solo un pequeño porcentaje de las solicitudes te da dinero. Puedes acabar con muchos datos y no tanto presupuesto.

Trabajo en algunos servicios que reciben 1000 millones de solicitudes al día, así que tiene sentido alojar nuestra propia monitorización y registro. Si tus volúmenes son menores, los servicios alojados son más fáciles.


### AWS services are mixed

Mi experiencia con los servicios de AWS ha sido desigual. Su servicio de Elasticsearch ha sido inestable, así que ejecutamos nuestras propias instancias para eso. Las métricas de CloudWatch son caras, así que por lo general solo las usamos para métricas de nivel de «infraestructura» en lugar de la aplicación, es decir, métricas relacionadas con la salud donde AWS puede saber mejor qué ocurre que el software que se ejecuta en la instancia. Los registros de CloudWatch pueden tardar en actualizarse y no tienen tantos metadatos. Ejecutar ELK ayuda con eso. Si realmente quiero datos en tiempo real, entonces usar Kafka como transporte de los registros es mejor. Logstash lo admite bastante bien. Sin embargo, gestionar un clúster de Kafka no es para los débiles de corazón, hay mucha fontanería expuesta.


### Kafka

Comentario: Kafka puede ser súper complicado a veces, o Kafka puede ser sólido como una roca y casi te olvidas de que está ahí atando todo. 


Comentario: Kafka ha sido sólido, pero poner en marcha todo costó una cantidad sorprendente de trabajo. Lo veo como una base de datos relacional en la que solo trabajas en la capa «física», p. ej., espacios de tablas, archivos y particiones. Hubo momentos al principio en que faltaban utilidades de gestión, y tuvimos que escribir programas para, p. ej., restablecer un grupo de consumidores. http://howfuckedismydatabase.com/nosql/

Comentario: Usamos Kafka como «búfer» de los mensajes de registro y como lugar donde podemos hacer procesamiento de flujos en tiempo real sobre los datos que llegan de varios servidores. Si recibimos un ataque DDOS, necesitamos una forma de analizar datos de varias instancias. Si registramos directamente desde los servidores a ELK, la carga puede hacer reventar el clúster de Elasticsearch.

Comentario: Kafka es bueno para nosotros porque, si recibimos un ataque DDOS, necesitamos una forma de analizar datos de varias instancias. Si registramos directamente desde los servidores a ELK, la carga puede hacer reventar el clúster de Elasticsearch.


Comentario: Kafka hace menos trabajo y es más eficiente, por lo que puede manejar mejor la carga. Y ponemos en cola el trabajo de Kafka y reintentamos. Y que Kafka esté sobrecargado no afecta a los usuarios que intentan hacer trabajo interactivo con Kibana, como ocurriría si Elasticsearch estuviera en apuros.

Comentario: El procesamiento de flujos consiste sobre todo en buscar abusos, p. ej., demasiado tráfico desde una sola IP en todo el clúster, y luego compartir el bloqueo en todo el clúster.

Comentario: El plugin logstash-output-kafka es bastante poco fiable por ahora. Me han afectado varios de los problemas de su página de incidencias de GitHub, que parece que nunca se resuelven. Quiero dejar de usarlo y enviar directamente desde nuestras aplicaciones a Kafka.

Comentario: Ahora estamos enviando eventos estructurados directamente desde la aplicación a Kafka. La motivación principal fue tocar menos veces los datos de registro y evitar leer y escribir en disco varias veces. En sistemas de alto volumen, registrar puede requerir más trabajo que la propia aplicación. Estoy pensando en hacer que journald también envíe los registros directamente, desde un programa en C.


### Loki

Sigue de cerca Loki. Todavía no está listo, pero cuando lo esté espero que encaje mejor en esta pila. Loki es un agregador de registros creado por grafana labs, y usa un raspado y una sintaxis de etiquetas similares a los de Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager para métricas. Me encanta Prometheus.

Rollbar/Graylog para registro/informes de errores (hay cierta superposición; un servicio pequeño probablemente no necesita ambos).

Actualmente, las alertas simplemente van a uno de unos pocos canales de Slack que las partes interesadas tienen activados para notificaciones. Si nos tomáramos más en serio las guardias, irían a PagerDuty/VictorOps/etc.

Grafana para gráficos y paneles. También espero con interés ver si sus próximas funciones de registro harán innecesario Graylog.


### Thanos

Usamos Thanos como front end de nuestra configuración de alta disponibilidad (HA). Sabe cómo deduplicar pares de HA.

Actualmente conservamos 6 meses de datos locales de Prometheus. Esto nos funciona razonablemente bien. Pero estoy en pleno despliegue del almacenamiento en buckets en nuestra configuración de Thanos para el almacenamiento de datos a largo plazo. En teoría, el almacenamiento en GCS será aproximadamente un 30 % más barato que el disco persistente estándar de GCE que usamos ahora.

Ahora mismo no hacemos copia de seguridad de los datos de Prometheus. Los datos realmente no son importantes para nosotros más allá de tener suficientes para las alertas. Nuestro despliegue general de flota cambia tanto de un año a otro que los datos históricos de más de unos meses simplemente no resultan interesantes. Podría ser interesante tener unas pocas estadísticas básicas año tras año; podría configurar un conjunto de reglas de registro de estadísticas básicas y almacenarlas con Federation o dejar que Thanos se encargue.

EDICIÓN: pequeño descargo, soy desarrollador de Prometheus.


### Prometheus HA

La HA en Prometheus se hace por duplicación: se ejecutan varios recolectores, y hay formas de sondear varios y deduplicar los datos.

El escalado se hace decidiendo la red y haciendo que distintos Prometheus sondeen distintas partes de la red.

El almacenamiento a largo plazo no es el punto fuerte de Prom, sino que se delega en algo como influx o timescaledb (que técnicamente también cumple el requisito de HA); artículo que leí al respecto https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Todavía no he probado lo de largo plazo, ya que solo estoy experimentando y lo uso para gráficos a corto plazo mientras librenms monitoriza mi red a largo plazo.


###  Datadog + PagerDuty + Threat Stack

Usamos Datadog (con PagerDuty) y Threat Stack y no podríamos estar más contentos. Mi única queja sobre DD es el costo relativamente alto del almacenamiento de métricas.


### Zabbix

Zabbix con scripts personalizados para monitorizar casi todo. Funciona de maravilla.


### Outlyer

Uso Outlyer, pero debo avisar de que trabajo aquí, y usar nuestro propio producto es obligatorio.

Todavía necesito Graylog, Sentry y Statuscake para complementar.

Suena parcial, pero, después de haber ejecutado felizmente Nagios y otros sistemas de monitorización internamente, contrataría una solución alojada en cualquier trabajo nuevo y me quitaría ese dolor de encima.


### Nagios + Nagiosgraph

Ejecutamos Nagios para toda la monitorización y las alertas. Las alertas se envían por correo electrónico (advertencias y notificaciones críticas) y por notificaciones audibles de la aplicación (para alertas críticas).

Nagiosgraph se usa para las visualizaciones.

Esta configuración ha sido muy eficaz para mantenernos informados de manera exhaustiva sobre lo que ocurre en nuestro entorno. Ejecutamos y monitorizamos unos 110 servidores críticos y unos 760 puntos de datos, y llevamos más de siete años con este sistema matutino.

También me gustaría agregar registros con Graylog o ELK en algún momento.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager mediante el estupendo helm chart de Prometheus Operator. Los registros siguen yendo al plan birch de LogDNA porque notamos que ELK es demasiado pesado para nuestros humildes mínimo de 3 y máximo de 5 nodos en GKE.


### DataDog + Sentry + PagerDuty.

Antes ejecutaba todas mis propias soluciones de monitorización con todo tipo de software, incluidos Nagios, Icinga, Zabbix, ELK, Greylog2, Influx y muchas otras herramientas, pero la verdad es que ejecutar tu propia infraestructura de monitorización implica demasiado esfuerzo, ¡sobre todo cuando puedes pagar tan poco a otra persona para que lo haga por ti!

Pagar a otros por ejecutar la infraestructura de monitorización libera a mis clientes para centrarse en operar sus plataformas en lugar de monitorizar la monitorización, lo que significa que el valor que obtienen de la estabilidad de su plataforma supera con creces cualquier costo de la monitorización como servicio.


### Sensu + Graphite + ELK

Mi empresa es muy partidaria de lo autoalojado.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager para las alertas; mi equipo cree que una monitorización simple es una buena monitorización.

Otros sistemas, como el registro y el seguimiento, aportarán un contexto rico para el diagnóstico cuando la persona de guardia reciba una alerta, pero nunca construimos alertas sobre ellos.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Servicios instrumentados con Prometheus => analítica y visualización con Circonus


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Estamos usando los servicios siguientes:

icinga2 para la monitorización y VictorOps para las alertas

NewRelic para la monitorización detallada del servicio

Sentry para el seguimiento de errores en el servicio

Slack/correo electrónico forman parte de las alertas que se activan desde NewRelic o icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 con integración con elasticsearch para el análisis y con integración con graphite+grafana para los gráficos.

gracias a la flexibilidad de las reglas apply de icinga2, los desarrolladores solo ven los servicios de los que reciben notificaciones.

y mediante icinga2 director, los programadores pueden definir fácilmente sus propias comprobaciones (cosa que hacen cada pocos días: salen 100 comprobaciones y entran otras 100) a gran escala y sin ninguna complicación.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Lo que tenemos ahora:

DataDog para métricas

New Relic para la monitorización de aplicaciones

ELK (Elastic Search + Logstash + Kibana) para los registros

Sentry (autoalojado) para registrar excepciones

Correos electrónicos + Slack + VictorOps para las alertas (según la gravedad)

Lo que queremos tener:

Prometheus para métricas (Grafana para visualización)

New Relic (probablemente Elastic Search APM) para la monitorización de aplicaciones

EFK (elastic search + fluentd + kibana) para el registro. Probablemente Loki de Grafana ya estará listo para producción para cuando lleguemos a ese punto

Sentry para las excepciones

Alertmanager + correo electrónico + VictorOps para las alertas


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Descargo: trabajo en VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf para métricas de servidor como CPU, disco, memoria y red. También usamos Telegraf para la monitorización SNMP de nuestros dispositivos de red.

Prometheus para métricas de aplicación. Programamos comprobaciones de estado en nuestra aplicación que Prometheus recopila.

InfluxDB para el almacenamiento de series temporales. Aquí es adonde se envían nuestros datos de Telegraf.

Grafana para paneles y alertas. El motor de alertas no es súper robusto, pero cumple. También enviamos alertas a Slack.

Lo que no tengo ahora mismo es una solución de registro centralizado. ELK es potente pero difícil de configurar y gestionar, y no conozco ninguna alternativa gratuita lo bastante parecida como para investigarla.


### Sematext + Logagent + Experience

Sematext para métricas, para registros, para trazas y pronto también para la monitorización de usuarios reales. Más simple y más barato que usar N herramientas o servicios diferentes, en mi humilde opinión.

Para el envío de registros solíamos usar rsyslog y luego cambiamos a Logagent.

Para los informes de fallos del front end usamos Sentry, pero pronto cambiaremos a Experience.

Descargo: soy un Sematextan.


### Azure Monitor/Analytics + OpsGenie

Ojalá Log Analytics tuviera una mejor interfaz. Nos estamos alejando de splunk, que era mucho más fácil de navegar.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Realmente no quieres ejecutar tu propio sistema de notificaciones. Puedes reemplazar Splunk por ELK a menos que tu equipo de seguridad prefiera Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf como recolector, Prometheus + Alertmanager para la monitorización y las alertas, integrados con canales de slack y con pagerduty para las alertas críticas. Grafana para la visualización de métricas de hosts.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus para métricas + alertas

Grafana para los paneles de Prometheus

Cloudwatch monitorizando las instancias de Prometheus

sentry para el seguimiento de excepciones

kibana + elasticsearch

graylog

prometheus Push Gateway para trabajos por lotes o cronjobs

SOP https://github.com/rapidloop/sop para «empujar/reenviar» métricas de una instancia de Prometheus a otra

los clientes usan los clientes de Prometheus. Intentamos usar opencensus.io en el lado del cliente


### PagerDuty + Monitis

PagerDuty + Monitis. También algunas Azure Functions a medida para probar la salud de algunos servicios.

Con ganas de introducir Prometheus y Grafana este año


### Prometheus + Grafana + Bosun

Prometheus para almacenar los datos de series temporales. Grafana para la visualización. Bosun para la gestión de alertas.


### Azure Monitor/Analytics/Insights/Dashboards

Empresa solo Azure: Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana para monitorizar servicios en contenedores en Kubernetes mediante Prometheus

Monitis para la monitorización de servicios de extremo a extremo, principalmente para API web y aplicaciones web

OpsGenie para la gestión de alertas

Slack para recibir información de estado de nuestros sistemas


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Ingeniero de (dev)ops desde hace mucho tiempo. Crecí con Nagios. Me encantaría recibir opiniones sobre mi SaaS autofinanciado https://checklyhq.com. Hacemos monitorización de API y monitorización de transacciones del sitio con alertas bastante detalladas.

Empecé Checkly porque la monitorización activa/sintética en el espacio de las API era algo limitada (y cara). La monitorización basada en navegador o con guiones es aún más propietaria y cara. Usamos Puppeteer y mantenemos los precios lo más bajos posible.

Nuestra pila de monitorización:

Checkly (comiendo nuestra propia comida...)

AppOptics (gráficos personalizados)

AWS Cloudwatch y SNS para mensajes SMS.

alertas integradas de Heroku.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana nos alerta en slack sobre problemas de infraestructura o degradación del rendimiento, y hemos configurado logz.io para alertar en slack cuando hay cierto volumen de registros de nivel de error de la capa de aplicación.


### SignalFX + Splunk + PagerDuty + Slack

Actualmente usamos: SignalFX, Splunk, PagerDuty y Slack. No soy un gran fan de SignalFX, aunque su equipo de soporte es súper amable y receptivo. Me gustan Splunk (merece la pena si puedes pagarlo), PagerDuty y Slack.

Antes usaba la pila TICK, donde la mayor parte de la C era en realidad una G, es decir, Grafana, aunque sí usé un poco Chronograf. Era genial, pero era un fastidio de gestionar. El clásico dilema de SaaS frente a autoalojamiento.

He usado DataDog, New Relic, Graylog, ELK y BugSnag. Me gustan mucho DataDog y New Relic, Graylog es bastante bueno. No soy un gran fan de ELK. BugSnag está bien; de hecho creo que hacer seguimiento de errores y excepciones es un sustituto bastante bueno de la monitorización completa de registros, en muchos casos.


### ELK + Prometheus + Grafana

Como otros, usamos ELK para los registros y Prometheus+Grafana para todo lo demás.

Mantener esta configuración es fácil si te das permiso para perder datos de vez en cuando. Por ejemplo, si nuestra base de datos de ElasticSearch entra en un bache (lo que desgraciadamente nos ocurre cada 2-3 meses), no nos molestamos con la HA, sino que volcamos los datos y seguimos con nuestras vidas. Si de verdad necesitas HA o retención a largo plazo, buena suerte.


### Datadog + Prometheus + Grafana

Configuré Datadog mes a mes porque cuando llegué aquí no había ni monitorización ni alertas. Solo un par de nuestros sitios se monitorizaban cada 5 minutos para comprobar su disponibilidad. Datadog es, sin lugar a dudas, el más fácil de configurar. Cuando termine de atender todos los demás problemas, cambiaré a Prometheus+Grafana. Todavía no estoy 100 % decidido sobre la gestión de registros.

### Nagios + ELK

Damos soporte a más de 100 productos.

Para on-prem, sobre todo Nagios y ELK. Para la nube, estamos migrando de DataDog a NewRelic.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Antes usábamos datadog, pero lo encontramos demasiado caro para nuestras necesidades. No me malinterpretes, es increíble, pero tiene un costo enorme. Pudimos configurar site24x7.com con una suscripción anual por aproximadamente 2-3 meses del costo de DD.

Nuestra pila de monitorización:

Site24x7 - APM, monitorización de URL externas, monitorización del flujo de correo SMTP, vencimientos de ssl y monitorización de procesos.

StatusCake - para la monitorización y confirmación de URL: es nuestro respaldo por si site24x7 se pierde algo (no lo hace), pero SC es más flexible para la monitorización de puertos y servicios externos para nuestras necesidades.

Ambas herramientas escalan a PagerDuty, y luego recibimos nuestras escalaciones en slack.

SumoLogic - para la monitorización de registros (es una gran herramienta pero algo complicada para nuestras necesidades)

Desde slack podemos confirmar (ack) o remediar la alerta.

Luego tenemos muchas automatizaciones de site24x7 que se conectan a commando.io para lo que llamamos «BedOps»: cuando se activa una alerta, lanzamos algunos scripts o automatizaciones como intento de remediar la situación (el 99 % de las veces la automatización más nuestros scripts nos mantienen fuera de problemas).

Tenemos guías operativas internas en nuestra base de conocimiento para cuando las automatizaciones fallan o hay algo fuera de alcance que necesita arreglarse.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana para las métricas en nuestros clústeres de GKE y VM.

Google Stackdriver para los registros (ya que está incluido, activo por defecto y actualmente es suficiente para nuestras necesidades).


### Zabbix

Zabbix para todo. No se necesita software adicional.
