# Métriques, moniteurs, alertes

Sommaire :

* [Résumé](#résumé)
  * [Question](#question)
  * [Décision](#décision)
  * [État](#état)
* [Détails](#détails)
  * [Hypothèses](#hypothèses)
  * [Contraintes](#contraintes)
  * [Positions](#positions)
  * [Argument](#argument)
  * [Implications](#implications)
* [Connexe](#connexe)
  * [Décisions connexes](#décisions-connexes)
  * [Exigences connexes](#exigences-connexes)
  * [Artefacts connexes](#artefacts-connexes)
  * [Principes connexes](#principes-connexes)
* [Notes](#notes)
  * [Messages texte libres ou messages d’événements structurés](#messages-texte-libres-ou-messages-dévénements-structurés)
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


## Résumé


### Question

Nous voulons utiliser des métriques, des moniteurs et des alertes, parce que nous voulons savoir dans quelle mesure nos applications fonctionnent bien, et savoir quand il y a un problème.


### Décision

En cours (WIP).


### État

Collecte d’informations. Nous commençons par les extrémités plausibles du spectre : l’outil gratuit plus ancien le plus recommandé (Nagios) et l’outil payant plus récent le plus recommandé (New Relic).


## Détails


### Hypothèses

Nous voulons créer des applications web modernes, rapides, fiables, adaptatives, etc.

Nous voulons acheter plutôt que construire.


### Contraintes

Nous voulons des outils qui fonctionnent bien avec notre chaîne devops et avec nos clouds de déploiement.


### Positions

Nous recherchons actuellement des positions.


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

  
### Argument

Jusqu’ici, Nagios et New Relic sont les extrémités du spectre. Nagios est l’outil viable le plus ancien, le plus simple et gratuit. New Relic est l’outil viable le plus récent en fonctionnalités, le plus complet et payant. Nous commencerons par des évaluations de ces deux outils. Au besoin, nous nous déplacerons dans le spectre.  

Jusqu’ici, Zabbix a les meilleures recommandations, et offre aussi les capacités les plus complètes.

Jusqu’ici, ELK a la meilleure popularité parmi les solutions open source à construire plutôt qu’à acheter.

Jusqu’ici, Prometheus + Graphana ont la meilleure popularité.


### Implications

À FAIRE (TODO).


## Connexe


### Décisions connexes

Les choix affecteront la testabilité, la télémétrie et probablement d’autres systèmes comme ceux du service client, de l’ingénierie de fiabilité des sites, etc.


### Exigences connexes

À FAIRE (TODO).


### Artefacts connexes

À FAIRE (TODO).


### Principes connexes

Facilement réversible.

Besoin de vitesse.


## Notes


Une pile open source plutôt bonne est :

* Prometheus pour les métriques et les alertes fondées sur les métriques

* Grafana pour afficher les métriques

* Elasticsearch/Logstash/Kibana (ELK) pour les journaux et les événements structurés

* Pushover pour les notifications mobiles


### Messages texte libres ou messages d’événements structurés

Messages texte libres : par exemple, le genre de choses aléatoires que vous trouveriez dans /var/log/messages, et quelque chose généré intentionnellement par l’application. Les messages sont utiles pour identifier d’autres événements sur la machine, comme un manque de mémoire ou des erreurs matérielles, mais comportent beaucoup de bruit. 

Messages d’événements structurés : générés par l’application, avec un ensemble fixe ou dynamique d’attributs, p. ex. un journal de requêtes HTTP, un journal comptable, une connexion d’utilisateur.

De façon générale, il est bon de consigner les détails de chaque requête de manière à pouvoir explorer en profondeur selon les attributs. Ajouter p. ex. un userid ou un sessionid à tout permet donc de tracer. Le traçage explicite est aussi bon, bien sûr. Utiliser ELK pour cela est une sorte de https://www.honeycomb.io/ du pauvre


### Graylog is easier

Graylog est plus facile à mettre en place d’après mon expérience.



### Prometheus take some tuning


Je suis globalement satisfait de Prometheus pour les métriques. Les alertes demandent un certain réglage, mais sont plutôt bonnes. Cela dépend de votre application. Je pense qu’il vaut mieux alerter sur des conditions visibles par l’utilisateur final, pas sur les causes sous-jacentes. Par exemple, le temps de chargement d’une page est bon, le nombre de requêtes par seconde ne l’est pas. Même si zéro requête par seconde indique que quelque chose ne va pas.

L’avantage d’un service est qu’il offre une intelligence supplémentaire d’emblée. J’aime généralement Datadog. Les services peuvent être effroyablement chers si vous avez beaucoup de données, et ont parfois des modèles tarifaires qui ne sont pas adaptés au cloud, p. ex. une facturation par instance alors que les instances sont dynamiques. Il y a aussi une différence entre les services où chaque requête provient d’un utilisateur payant et ceux liés à la publicité, où seul un petit pourcentage des requêtes vous rapporte de l’argent. Vous pouvez vous retrouver avec beaucoup de données et pas tant de budget.

Je travaille sur des services qui reçoivent 1 milliard de requêtes par jour, il est donc logique d’héberger notre propre supervision et journalisation. Si vos volumes sont plus faibles, les services hébergés sont plus simples.


### AWS services are mixed

Mon expérience avec les services AWS est mitigée. Leur service Elasticsearch a été instable, nous faisons donc tourner nos propres instances pour cela. Les métriques CloudWatch sont chères, nous ne les utilisons donc généralement que pour des métriques de niveau « infrastructure » plutôt que l’application, c’est-à-dire des métriques liées à la santé où AWS peut mieux savoir ce qui se passe que le logiciel exécuté sur l’instance. Les journaux CloudWatch peuvent être lents à se mettre à jour et n’ont pas beaucoup de métadonnées. Faire tourner ELK aide là-dessus. Si je veux vraiment des données en temps réel, alors utiliser Kafka comme transport des journaux est préférable. Logstash le prend plutôt bien en charge. Gérer un cluster Kafka n’est cependant pas pour les cœurs sensibles, il y a beaucoup de tuyauterie exposée.


### Kafka

Commentaire : Kafka peut être super délicat parfois, ou Kafka peut être solide comme un roc et on oublie presque qu’il est là en train de tout relier. 


Commentaire : Kafka a été solide, mais le mettre en route a demandé une quantité de travail surprenante. Je le vois comme une base de données relationnelle où l’on ne travaille qu’au niveau « physique », p. ex. espaces de tables, fichiers et partitions. Au début, il y a eu des moments où les utilitaires de gestion manquaient, et nous avons dû écrire des programmes pour p. ex. réinitialiser un groupe de consommateurs. http://howfuckedismydatabase.com/nosql/

Commentaire : Nous utilisons Kafka comme « tampon » pour les messages de journal et comme endroit où nous pouvons faire du traitement de flux en temps réel sur des données provenant de plusieurs serveurs. Si nous subissons une attaque DDOS, nous avons besoin d’un moyen d’analyser des données sur plusieurs instances. Si nous consignons directement des serveurs vers ELK, la charge peut faire exploser le cluster Elasticsearch.

Commentaire : Kafka est bon pour nous parce que si nous subissons une attaque DDOS, nous avons besoin d’un moyen d’analyser des données sur plusieurs instances. Si nous consignons directement des serveurs vers ELK, la charge peut faire exploser le cluster Elasticsearch.


Commentaire : Kafka fait moins de travail et est plus efficace, il peut donc mieux gérer la charge. Et nous mettons le travail Kafka en file d’attente et réessayons. Et une surcharge de Kafka n’affecte pas les utilisateurs qui essaient de faire un travail interactif avec Kibana, comme ce serait le cas si Elasticsearch peinait.

Commentaire : Le traitement de flux consiste surtout à chercher des abus, p. ex. trop de trafic depuis une seule IP sur l’ensemble du cluster, puis à partager le blocage sur l’ensemble du cluster.

Commentaire : Le plugin logstash-output-kafka est cependant plutôt peu fiable en ce moment. J’ai été touché par plusieurs problèmes de sa page d’issues GitHub, qui semblent ne jamais être corrigés. Je veux arrêter de l’utiliser pour envoyer directement de nos applications vers Kafka.

Commentaire : Nous envoyons maintenant des événements structurés directement de l’application vers Kafka. La principale motivation était de toucher moins souvent les données de journal et d’éviter de lire et d’écrire plusieurs fois sur le disque. Dans les systèmes à gros volume, la journalisation peut demander plus de travail que l’application elle-même. Je réfléchis à faire envoyer aussi les journaux directement par journald, depuis un programme en C.


### Loki

Gardez un œil attentif sur Loki. Il n’est pas encore prêt, mais lorsqu’il le sera, je m’attends à ce qu’il s’intègre mieux dans cette pile. Loki est un agrégateur de journaux créé par grafana labs, qui utilise un scraping et une syntaxe d’étiquettes semblables à ceux de Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager pour les métriques. J’adore Prometheus.

Rollbar/Graylog pour la journalisation/le rapport d’erreurs (il y a un certain chevauchement ; un petit service n’a probablement pas besoin des deux).

Actuellement, les alertes vont simplement vers l’un de quelques canaux Slack pour lesquels les parties intéressées ont activé les notifications. Si nous prenions davantage au sérieux l’astreinte, elles iraient vers PagerDuty/VictorOps/etc.

Grafana pour les graphiques et les tableaux de bord. J’attends aussi avec impatience de voir si leurs futures fonctionnalités de journalisation rendront Graylog superflu.


### Thanos

Nous utilisons Thanos comme frontal de notre configuration haute disponibilité (HA). Il sait dédoublonner les paires HA.

Nous conservons actuellement 6 mois de données Prometheus locales. Cela fonctionne raisonnablement bien pour nous. Mais je suis en plein déploiement du stockage par buckets dans notre configuration Thanos pour le stockage de données à long terme. En théorie, le stockage GCS sera environ 30 % moins cher que le disque persistant standard GCE que nous utilisons actuellement.

Nous ne sauvegardons pas les données Prometheus pour l’instant. Les données ne sont pas vraiment importantes pour nous au-delà d’en avoir assez pour les alertes. Notre déploiement global de flotte change tellement d’une année à l’autre que des données historiques de plus de quelques mois ne sont tout simplement pas intéressantes. Il pourrait être intéressant d’avoir quelques statistiques clés d’année en année ; je pourrais mettre en place un ensemble de règles d’enregistrement de statistiques clés et les stocker avec la Federation, ou simplement laisser Thanos s’en charger.

MODIFICATION : petit avertissement, je suis développeur de Prometheus.


### Prometheus HA

La HA dans Prometheus se fait par duplication : on exécute plusieurs collecteurs, il existe des moyens d’en interroger plusieurs et de dédoublonner les données.

La mise à l’échelle se fait en décidant du réseau et en faisant interroger par différents Prometheus différentes parties du réseau.

Le stockage à long terme n’est pas le point fort de Prom, mais est délégué à quelque chose comme influx ou timescaledb (qui coche techniquement aussi la case HA) ; article que j’ai lu à ce sujet https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Je n’ai pas encore essayé le long terme car je ne fais encore qu’expérimenter et je l’utilise pour des graphiques à court terme pendant que librenms surveille mon réseau à long terme.


###  Datadog + PagerDuty + Threat Stack

Nous utilisons Datadog (avec PagerDuty) et Threat Stack et nous ne pourrions pas être plus satisfaits. Mon seul grief envers DD est le coût relativement élevé du stockage des métriques.


### Zabbix

Zabbix avec des scripts personnalisés pour superviser presque tout. Fonctionne à merveille.


### Outlyer

J’utilise Outlyer, mais je dois préciser que je travaille ici, et qu’utiliser son propre produit est impératif.

J’ai encore besoin de Graylog, Sentry et Statuscake pour compléter.

Cela paraît partial, mais après avoir exploité avec plaisir Nagios et d’autres systèmes de supervision en interne, j’achèterais une solution hébergée dans tout nouveau poste et me déchargerais de cette peine.


### Nagios + Nagiosgraph

Nous faisons tourner Nagios pour toute la supervision et les alertes. Les alertes passent par courriel (avertissements et notifications critiques) et par des notifications sonores d’application (pour les alertes critiques).

Nagiosgraph sert aux visualisations.

Cette configuration a été très efficace pour nous tenir informés de manière exhaustive de ce qui se passe dans notre environnement. Nous exploitons et surveillons environ 110 serveurs critiques et environ 760 points de données, et ce système matinal est en place depuis plus de sept ans.

J’aimerais aussi à un moment donné agréger les journaux avec Graylog ou ELK.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager via le formidable helm chart Prometheus Operator. Les journaux vont toujours vers le forfait birch de LogDNA car nous avons constaté qu’ELK est trop lourd pour nos humbles 3 à 5 nœuds sur GKE.


### DataDog + Sentry + PagerDuty.

J’exploitais auparavant toutes mes propres solutions de supervision avec toutes sortes de logiciels dont Nagios, Icinga, Zabbix, ELK, Greylog2, Influx et de nombreux autres outils, mais la vérité est qu’exploiter sa propre infrastructure de supervision demande trop d’efforts, surtout quand on peut payer si peu quelqu’un d’autre pour le faire à sa place !

Payer d’autres personnes pour exploiter l’infrastructure de supervision libère mes clients pour qu’ils se concentrent sur l’exploitation de leurs plateformes plutôt que sur la supervision de la supervision, ce qui signifie que la valeur qu’ils tirent de la stabilité de leur plateforme dépasse largement tout coût de la supervision en tant que service.


### Sensu + Graphite + ELK

Mon entreprise est très attachée à l’auto-hébergement.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager pour les alertes ; mon équipe croit qu’une supervision simple est une bonne supervision.

D’autres systèmes comme la journalisation et le traçage fourniront un contexte riche pour le diagnostic lorsque la personne d’astreinte reçoit une alerte, mais nous ne construisons jamais d’alertes sur ceux-ci.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Services instrumentés avec Prometheus => analyse et visualisation avec Circonus


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Nous utilisons les services ci-dessous :

icinga2 pour la supervision et VictorOps pour les alertes

NewRelic pour la supervision détaillée du service

Sentry pour le suivi des erreurs dans le service

Slack/courriel font partie des alertes déclenchées depuis NewRelic ou icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 avec intégration elasticsearch pour l’analyse et intégration graphite+grafana pour les graphiques.

grâce à la souplesse des règles apply d’icinga2, les développeurs ne voient que les services pour lesquels ils reçoivent des notifications.

et grâce à icinga2 director, les programmeurs peuvent facilement définir leurs propres vérifications (ce qu’ils font tous les quelques jours : 100 vérifications sortent, 100 autres entrent) à grande échelle et sans aucun tracas.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Ce que nous avons maintenant :

DataDog pour les métriques

New Relic pour la supervision des applications

ELK (Elastic Search + Logstash + Kibana) pour les journaux

Sentry (auto-hébergé) pour consigner les exceptions

Courriels + Slack + VictorOps pour les alertes (selon la gravité)

Ce que nous voulons avoir :

Prometheus pour les métriques (Grafana pour la visualisation)

New Relic (probablement Elastic Search APM) pour la supervision des applications

EFK (elastic search + fluentd + kibana) pour la journalisation. Probablement que Loki de Grafana sera prêt pour la production d’ici à ce que nous y arrivions

Sentry pour les exceptions

Alertmanager + courriel + VictorOps pour les alertes


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Avertissement : je travaille chez VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf pour les métriques serveur comme le CPU, le disque, la mémoire et le réseau. Nous utilisons aussi Telegraf pour la supervision SNMP de nos équipements réseau.

Prometheus pour les métriques applicatives. Nous codons des contrôles de santé dans notre application que Prometheus collecte.

InfluxDB pour le stockage de séries temporelles. C’est là que nos données Telegraf sont envoyées.

Grafana pour les tableaux de bord et les alertes. Le moteur d’alertes n’est pas très robuste, mais il fait le travail. Nous envoyons aussi des alertes dans Slack.

Ce que je n’ai pas actuellement, c’est une solution de journalisation centralisée. ELK est puissant mais difficile à installer et à gérer, et je ne connais pas d’alternatives gratuites assez proches pour valoir la peine d’être étudiées.


### Sematext + Logagent + Experience

Sematext pour les métriques, les journaux, les traces, bientôt aussi pour la supervision des utilisateurs réels. Plus simple/moins cher que d’utiliser N outils/services différents, à mon humble avis.

Pour l’expédition des journaux, nous utilisions rsyslog puis nous sommes passés à Logagent.

Pour le rapport de plantages front-end, nous utilisons Sentry, mais nous passerons bientôt à Experience.

Avertissement : je suis un Sematextien.


### Azure Monitor/Analytics + OpsGenie

J’aimerais que Log Analytics ait une meilleure interface. Nous nous éloignons de splunk, qui était bien plus facile à parcourir.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Vous ne voulez vraiment pas exploiter votre propre système de notification. Vous pouvez remplacer Splunk par ELK, sauf si votre équipe de sécurité préfère Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf comme collecteur, Prometheus + Alertmanager pour la supervision et les alertes, intégrés à des canaux slack et à pagerduty pour les alertes critiques. Grafana pour la visualisation des métriques d’hôtes.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus pour les métriques + alertes

Grafana pour les tableaux de bord Prometheus

Cloudwatch surveillant les instances Prometheus

sentry pour le suivi des exceptions

kibana + elasticsearch

graylog

prometheus Push Gateway pour les traitements par lots/tâches cron

SOP https://github.com/rapidloop/sop pour « pousser/transférer » des métriques d’une instance Prometheus à une autre

les clients utilisent soit les clients Prometheus. Nous essayons d’utiliser opencensus.io côté client


### PagerDuty + Monitis

PagerDuty + Monitis. Aussi quelques Azure Functions sur mesure pour tester la santé de certains services.

Nous comptons introduire Prometheus et Grafana cette année


### Prometheus + Grafana + Bosun

Prometheus pour stocker les données de séries temporelles. Grafana pour la visualisation. Bosun pour la gestion des alertes.


### Azure Monitor/Analytics/Insights/Dashboards

Entreprise 100 % Azure : Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana pour superviser les services en conteneurs dans Kubernetes via Prometheus

Monitis pour la supervision de services de bout en bout, principalement pour les API web et les applications web

OpsGenie pour la gestion des alertes

Slack pour obtenir des informations d’état de nos systèmes


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Ingénieur (dev)ops de longue date. J’ai grandi avec Nagios. J’aimerais avoir des avis sur mon SaaS autofinancé https://checklyhq.com. Nous faisons de la supervision d’API et de la supervision de transactions de site avec des alertes assez approfondies.

J’ai lancé Checkly parce que la supervision active / synthétique dans le domaine des API était un peu limitée (et chère). La supervision par navigateur / scriptée est encore plus propriétaire et coûteuse. Nous utilisons Puppeteer et gardons les prix aussi bas que possible.

Notre pile de supervision :

Checkly (en mangeant notre propre cuisine...)

AppOptics (graphiques personnalisés)

AWS Cloudwatch et SNS pour les SMS.

alertes Heroku intégrées.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana nous alerte dans slack des problèmes d’infrastructure ou de dégradation des performances, et nous avons configuré logz.io pour alerter dans slack à partir d’un certain volume de journaux de niveau erreur de la couche applicative.


### SignalFX + Splunk + PagerDuty + Slack

Actuellement : SignalFX, Splunk, PagerDuty et Slack. Je ne suis pas un grand fan de SignalFX, même si leur équipe d’assistance est super sympathique et réactive. J’aime Splunk (ça vaut le coup si vous pouvez le payer), PagerDuty et Slack.

J’utilisais la pile TICK où la plupart du C était en fait un G, c’est-à-dire Grafana, même si j’ai un peu utilisé Chronograf. C’était génial mais pénible à gérer. Le dilemme classique SaaS contre auto-hébergement.

J’ai utilisé DataDog, New Relic, Graylog, ELK et BugSnag. J’aime beaucoup DataDog et New Relic, Graylog est plutôt bon. Je ne suis pas un grand fan d’ELK. BugSnag est bien ; j’ai en fait l’impression que le suivi des erreurs/exceptions est un assez bon substitut à la supervision complète des journaux, dans bien des cas.


### ELK + Prometheus + Grafana

Comme d’autres, nous utilisons ELK pour les journaux et Prometheus+Grafana pour tout le reste.

Maintenir cette configuration est facile si vous vous donnez la permission de perdre occasionnellement des données. Par exemple, si notre base ElasticSearch tombe dans un creux (ce qui nous arrive malheureusement tous les 2-3 mois), nous ne nous embêtons pas avec la HA et préférons vider les données et continuer notre vie. Si vous avez absolument besoin de HA ou de rétention à long terme, bonne chance.


### Datadog + Prometheus + Grafana

J’ai mis en place Datadog au mois le mois parce qu’à mon arrivée, il n’y avait ni supervision ni alertes. Seuls quelques-uns de nos sites étaient surveillés toutes les 5 minutes pour la disponibilité. Datadog est de loin le plus facile à installer. Quand j’aurai fini de traiter tous les autres problèmes, je passerai à Prometheus+Grafana. Pas encore décidé à 100 % sur la gestion des journaux.

### Nagios + ELK

Nous prenons en charge plus de 100 produits.

Pour le sur site, c’est surtout Nagios et ELK. Pour le cloud, nous migrons de DataDog vers NewRelic.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Nous utilisions datadog mais l’avons trouvé bien trop cher pour nos besoins. Ne vous méprenez pas, il est génial, mais il a un coût énorme. Nous avons pu mettre en place site24x7.com avec un abonnement annuel pour environ 2-3 mois du coût de DD.

Notre pile de supervision :

Site24x7 - APM, supervision d’URL externes, supervision du flux de courriels SMTP, expirations ssl et supervision de processus.

StatusCake - pour la supervision et la confirmation d’URL - c’est notre sauvegarde au cas où site24x7 manquerait quelque chose (ce n’est pas le cas) mais SC est plus flexible pour la supervision de ports et de services externes pour nos besoins.

Les deux outils escaladent vers PagerDuty, puis nous recevons nos escalades dans slack.

SumoLogic - pour la supervision des journaux (c’est un excellent outil mais un peu compliqué pour nos besoins)

Depuis slack, nous pouvons acquitter (ack) ou remédier à l’alerte.

Nous avons ensuite beaucoup d’automatisations site24x7 qui se connectent à commando.io pour ce que nous appelons « BedOps » : lorsqu’une alerte se déclenche, nous lançons quelques scripts ou automatisations pour tenter de remédier à la situation (99 % du temps, l’automatisation + nos scripts nous évitent les ennuis).

Nous avons des runbooks internes dans notre base de connaissances pour les cas où les automatisations échouent ou quand il y a quelque chose hors du champ qui doit être corrigé.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana pour les métriques dans nos clusters GKE et nos VM.

Google Stackdriver pour les journaux (car il est inclus, actif par défaut et suffisant pour nos besoins actuels).


### Zabbix

Zabbix pour tout. Aucun logiciel supplémentaire nécessaire.
