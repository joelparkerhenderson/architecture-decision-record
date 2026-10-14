# Metriche, monitoraggio, avvisi

Indice:

* [Riepilogo](#riepilogo)
  * [Questione](#questione)
  * [Decisione](#decisione)
  * [Stato](#stato)
* [Dettagli](#dettagli)
  * [Ipotesi](#ipotesi)
  * [Vincoli](#vincoli)
  * [Posizioni](#posizioni)
  * [Argomento](#argomento)
  * [Implicazioni](#implicazioni)
* [Correlato](#correlato)
  * [Decisioni correlate](#decisioni-correlate)
  * [Requisiti correlati](#requisiti-correlati)
  * [Artefatti correlati](#artefatti-correlati)
  * [Principi correlati](#principi-correlati)
* [Note](#note)
  * [Messaggi in testo libero rispetto a messaggi di evento strutturati](#messaggi-in-testo-libero-rispetto-a-messaggi-di-evento-strutturati)
  * [Graylog è più semplice](#graylog-è-più-semplice)
  * [Prometheus ha bisogno di un po' di messa a punto](#prometheus-ha-bisogno-di-un-po-di-messa-a-punto)
  * [I servizi AWS sono contrastanti](#i-servizi-aws-sono-contrastanti)
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
  * [Datadog rispetto a Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack](#datadog-rispetto-a-site24x7--statuscake--pagerduty--sumologic--slack)
  * [Prometheus + AlertManager + Grafana + Stackdriver](#prometheus--alertmanager--grafana--stackdriver)
  * [Zabbix](#zabbix-1)


## Riepilogo


### Questione

Vogliamo usare metriche, monitoraggio e avvisi, perché vogliamo sapere quanto bene funzionano le nostre applicazioni e sapere quando c'è un problema.


### Decisione

WIP.


### Stato

Raccolta di informazioni. Iniziamo dagli estremi ragionevoli dello spettro: lo strumento gratuito più vecchio più raccomandato (Nagios) e lo strumento a pagamento più recente più raccomandato (New Relic).


## Dettagli


### Ipotesi

Vogliamo creare app web moderne, veloci, affidabili, responsive ecc.

Vogliamo comprare anziché costruire.


### Vincoli

Vogliamo strumenti che funzionino bene con la nostra pipeline devops e con i nostri cloud di deployment.


### Posizioni

Stiamo attualmente esaminando le posizioni.


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

  
### Argomento

Finora, Nagios e New Relic sono gli estremi dello spettro. Nagios è lo strumento più vecchio, più semplice, gratuito e praticabile. New Relic è lo strumento con le funzionalità più recenti, il più completo, a pagamento e praticabile. Iniziamo con le valutazioni di questi. Secondo necessità, ci muoviamo verso l'interno dello spettro.  

Finora Zabbix ha le migliori raccomandazioni e offre anche le capacità più complete.

Finora ELK ha la migliore popolarità tra l'open source, costruire-da-soli-anziché-comprare.

Finora Prometheus + Graphana ha la migliore popolarità.


### Implicazioni

TODO.


## Correlato


### Decisioni correlate

Le scelte influenzeranno testabilità, telemetria e probabilmente altri sistemi, per esempio per l'assistenza clienti, la site reliability engineering ecc.


### Requisiti correlati

TODO.


### Artefatti correlati

TODO.


### Principi correlati

Facilmente reversibile.

Necessità di velocità.


## Note


Uno stack open source abbastanza buono è:

* Prometheus per le metriche e gli avvisi basati sulle metriche

* Grafana per mostrare le metriche

* Elasticsearch/Logstash/Kibana (ELK) per log ed eventi strutturati

* Pushover per le notifiche mobili


### Messaggi in testo libero rispetto a messaggi di evento strutturati

Messaggi in testo libero: per esempio il tipo di cose casuali che trovi in /var/log/messages, e qualcosa generato intenzionalmente dall'applicazione. I messaggi sono utili per identificare altre cose che accadono sulla macchina come memoria esaurita o guasti hardware, ma contengono molta spazzatura. 

Messaggi di evento strutturati: generati dall'applicazione, con un insieme fisso o dinamico di attributi, per esempio un log delle richieste HTTP, un log contabile, un accesso utente.

In generale, è bello registrare i dettagli di ogni richiesta in un modo che ti permetta di approfondire in base agli attributi. Quindi aggiungere per esempio un userid o un sessionid a tutto ti permette di tracciare. Anche la tracciatura esplicita è naturalmente buona. Usare ELK per questo è una specie di https://www.honeycomb.io/ da poveri


### Graylog è più semplice

Graylog è più semplice da configurare secondo la mia esperienza.



### Prometheus ha bisogno di un po' di messa a punto


Sono in generale soddisfatto di Prometheus per le metriche. Gli avvisi hanno bisogno di un po' di messa a punto, ma sono abbastanza buoni. Dipende dalla tua applicazione. Penso che sia meglio avvisare su condizioni visibili agli utenti finali, non su cause sottostanti. Per esempio il tempo di caricamento della pagina va bene, il numero di richieste al secondo no. Anche se zero richieste al secondo indica che c'è qualcosa che non va.

Il vantaggio di un servizio è che offrono intelligenza aggiuntiva pronta all'uso. In generale mi piace Datadog. I servizi possono essere spaventosamente costosi se hai molti dati e hanno a volte modelli di prezzo che non sono adatti al cloud, per esempio addebitare per istanza, quando le istanze sono dinamiche. C'è anche una differenza tra i servizi in cui ogni richiesta proviene da un utente pagante e quelli legati alla pubblicità, per cui solo una piccola percentuale delle richieste ti fa guadagnare. Puoi finire con molti dati e non tanto budget.

Lavoro su alcuni servizi che ricevono 1 miliardo di richieste al giorno, quindi è ragionevole ospitare il nostro monitoraggio e la nostra registrazione. Se i tuoi volumi sono più bassi, i servizi ospitati sono più semplici.


### I servizi AWS sono contrastanti

La mia esperienza con i servizi AWS è stata contrastante. Il loro servizio Elasticsearch è stato instabile, quindi gestiamo le nostre istanze per quello. Le metriche CloudWatch sono costose, quindi in generale le usiamo solo per le metriche a "livello di infrastruttura" anziché per l'applicazione, cioè metriche legate alla salute dove AWS può sapere meglio cosa sta succedendo del software in esecuzione sull'istanza. I CloudWatch Logs possono essere lenti da aggiornare e non hanno molti metadati. Eseguire ELK aiuta in questo. Se voglio davvero dati in tempo reale, è meglio usare Kafka come trasporto per i log. È supportato abbastanza bene da Logstash. Gestire un cluster Kafka non è per i deboli di cuore, c'è molto impianto idraulico nudo.


### Kafka

Commento: Kafka può essere super difficile a volte, oppure Kafka può essere stabile come la roccia al punto che quasi dimentichi che è lì e lega tutto insieme. 


Commento: Kafka è stato stabile, ma ci è voluto sorprendentemente molto lavoro per farlo funzionare. Lo considero come un database relazionale ma lavori solo sul livello "fisico", per esempio tablespace, file e partizioni. Ci sono stati momenti all'inizio in cui mancavano strumenti di gestione e abbiamo dovuto scrivere programmi per, per esempio, reimpostare un gruppo di consumatori. http://howfuckedismydatabase.com/nosql/

Commento: Usiamo Kafka come "buffer" per i messaggi di log e come luogo dove possiamo fare elaborazione di flussi in tempo reale sui dati provenienti da più server. Se riceviamo un attacco DDOS, ci serve un modo per analizzare i dati su più istanze. Se registriamo direttamente dai server in ELK, il carico può far esplodere il cluster Elasticsearch.

Commento: Kafka è buono per noi perché se riceviamo un attacco DDOS, ci serve un modo per analizzare i dati su più istanze. Se registriamo direttamente dai server in ELK, il carico può far esplodere il cluster Elasticsearch.


Commento: Kafka fa meno lavoro ed è più efficiente, quindi può gestire meglio il carico. E mettiamo in coda il lavoro di Kafka e riproviamo. E il fatto che Kafka sia sovraccarico non influisce sugli utenti che cercano di fare lavoro interattivo con Kibana, come accadrebbe se Elasticsearch è in difficoltà.

Commento:  L'elaborazione di flussi cerca soprattutto abusi, per esempio troppo traffico da un singolo IP in tutto il cluster, e poi condivide il blocco in tutto il cluster.

Commento: Il plugin logstash-output-kafka è però abbastanza inaffidabile in questo momento. Sono stato colpito da diversi dei problemi sulla sua pagina delle issue su GitHub, che non sembrano mai essere corretti. Voglio smettere di usarlo e passare a inviare direttamente dalle nostre app a Kafka.

Commento: Ora inviamo eventi strutturati direttamente dall'app a Kafka. La motivazione principale era toccare i dati di log meno volte ed evitare di leggere e scrivere il disco più volte. Nei sistemi ad alto volume, la registrazione può richiedere più lavoro dell'app stessa. Sto pensando di far inviare i log direttamente anche a journald, da un programma C.


### Loki

Tieni d'occhio Loki. Non è ancora pronto ma quando lo sarà mi aspetto che si adatti meglio a questo stack. Loki è un aggregatore di log creato da grafana labs, usa una sintassi di scraping e di tag simile a Prometheus.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager per le metriche. Amo Prometheus.

Rollbar/Graylog per la registrazione/segnalazione degli errori (c'è qualche sovrapposizione qui; un piccolo servizio probabilmente non ha bisogno di entrambi).

Al momento gli avvisi vanno solo a uno di alcuni canali Slack per cui le parti interessate hanno attivato le notifiche. Se fossimo più seri sulla reperibilità, andrebbero a PagerDuty/VictorOps/ecc.

Grafana per grafici e dashboard. Non vedo l'ora di vedere anche se le loro prossime funzionalità di registrazione renderanno Graylog ridondante.


### Thanos

Usiamo Thanos come front-end per la nostra configurazione HA. Sa come deduplicare le coppie HA.

Al momento conserviamo 6 mesi di dati Prometheus locali. Funziona abbastanza bene per noi. Ma sono nel bel mezzo del rollout dell'archiviazione su bucket per la nostra configurazione Thanos per l'archiviazione dei dati a lungo termine. In teoria l'archiviazione GCS sarà circa il 30% più economica del disco persistente standard GCE che usiamo ora.

Al momento non facciamo backup dei dati Prometheus. I dati semplicemente non sono molto importanti per noi oltre ad averne abbastanza per gli avvisi. Il nostro deployment complessivo della flotta cambia così tanto di anno in anno che i dati storici più vecchi di qualche mese semplicemente non sono così interessanti. Potrebbe essere interessante avere alcune statistiche chiave anno su anno, magari configuro un insieme di regole di registrazione per le statistiche chiave e le archivio con Federation o lascio semplicemente che Thanos le gestisca.

EDIT: Un piccolo chiarimento, sono uno sviluppatore Prometheus.


### Prometheus HA

L'HA in Prometheus si fa tramite duplicazione: esegui più raccoglitori, ci sono modi per interrogarne più di uno e deduplicare i dati.

La scalabilità avviene decidendo le reti e facendo interrogare a diversi Prometheus parti diverse della rete.

L'archiviazione a lungo termine non è il punto di forza di Prometheus ma viene delegata a qualcosa come influx o timescaledb (che tecnicamente spunta anche HA). Un articolo che ho letto a riguardo https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Non ho ancora provato la parte a lungo termine perché sto ancora solo sperimentando e lo uso per grafici a breve termine mentre librenms monitora la mia rete nel lungo periodo


###  Datadog + PagerDuty + Threat Stack

Usiamo Datadog (con PagerDuty) e Threat Stack e non potremmo essere più soddisfatti. La mia unica lamentela su DD è il costo relativamente alto dell'archiviazione delle metriche.


### Zabbix

Zabbix con script personalizzati per monitorare quasi tutto. Funziona come un sogno.


### Outlyer

Uso Outlyer, ma devo chiarire che lavoro qui e che mangiare il proprio cibo per cani (dogfooding) è un must.

Ho ancora bisogno di Graylog, Sentry e Statuscake per migliorare.

Suona di parte, ma dopo aver gestito con piacere Nagios e altri sistemi di monitoraggio internamente, comprerei una soluzione ospitata a ogni nuovo lavoro ed esternalizzerei quel dolore.


### Nagios + Nagiosgraph

Gestiamo Nagios per tutto il monitoraggio e gli avvisi. Gli avvisi avvengono tramite email (avvisi di warning e notifiche critiche) e notifiche acustiche dell'app (per gli avvisi critici).

Nagiosgraph è usato per le visualizzazioni.

Questa configurazione è stata molto efficace nel tenerci informati in modo completo su ciò che accade nel nostro ambiente. Gestiamo e monitoriamo circa 110 server critici per l'attività e circa 760 punti dati, e abbiamo questo sistema mattutino in funzione da oltre sette anni.

Mi piacerebbe anche aggregare i log con Graylog o ELk a un certo punto.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager tramite il fantastico helm chart Prometheus Operator. I log vanno ancora al piano birch di LogDNA perché abbiamo notato che ELK è troppo pesante per il nostro modesto cluster con min 3 max 5 nodi su GKE.


### DataDog + Sentry + PagerDuty.

Gestivo tutte le mie soluzioni di monitoraggio con ogni tipo di software, tra cui Nagios, Icinga, Zabbix, ELK, Greylog2, Influx e molti altri strumenti, ma la verità è che è fin troppo lavoro gestire la propria infrastruttura di monitoraggio, specialmente quando puoi pagare qualcun altro a prezzi così bassi per farlo per te!

Pagare altri per gestire l'infrastruttura di monitoraggio libera i miei clienti di concentrarsi sull'esecuzione delle loro piattaforme anziché monitorare il monitoraggio, il che significa che il valore che ottengono dalla stabilità della loro piattaforma supera di gran lunga qualsiasi costo del monitoraggio come servizio.


### Sensu + Graphite + ELK

La mia azienda è molto a favore delle cose self-hosted.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager per gli avvisi, il mio team crede che un monitoraggio semplice sia un buon monitoraggio.

Altri sistemi come registrazione e tracciatura forniscono contesto ricco per la diagnosi quando il reperibile riceve un avviso, ma non costruiamo mai avvisi su di essi.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Servizi strumentati con Prometheus => analisi e visualizzazione di Circonus


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Usiamo i seguenti servizi:

icinga2 per il monitoraggio e VictorOps per gli avvisi

NewRelic per il monitoraggio dettagliato del servizio

Sentry per il tracciamento degli errori nel servizio

Slack/email fanno parte degli avvisi attivati da NewRelic o icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 con integrazione elasticsearch per l'analisi e integrazione graphite+grafana per i grafici.

grazie alla flessibilità delle regole apply in icinga2, gli sviluppatori possono vedere solo i servizi per cui ricevono notifiche.

e tramite icinga2 director i programmatori possono facilmente definire i propri controlli (cosa che fanno, a distanza di pochi giorni – 100 controlli escono, 100 altri controlli entrano) su larga scala senza problemi.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Cosa abbiamo ora:

DataDog per le metriche

New Relic per il monitoraggio delle applicazioni

ELK (Elastic Search + Logstash + Kibana) per i log

Sentry (self-hosted) per la registrazione delle eccezioni

Email + Slack + VictorOps per gli avvisi (in base alla gravità)

Cosa vogliamo:

Prometheus per le metriche (Grafana per la visualizzazione)

New Relic (probabilmente Elastic Search APM) per il monitoraggio delle applicazioni

EFK (elastic search + fluentd + kibana) per la registrazione. Probabilmente Loki di Grafana sarà pronto per la produzione quando ci arriveremo

Sentry per le eccezioni

Alertmanager + email + VictorOps per gli avvisi


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (chiarimento: lavoro in VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf per le metriche dei server come CPU, disco, memoria e rete. Usiamo Telegraf anche per il monitoraggio SNMP dei nostri dispositivi di rete.

Prometheus per le metriche delle applicazioni. Codifichiamo controlli di salute nella nostra applicazione che Prometheus raccoglie.

InfluxDB per l'archiviazione di serie temporali. Qui vanno i nostri dati Telegraf.

Grafana per dashboard e avvisi. Il motore di avvisi non è super robusto ma fa il suo lavoro. Inviamo gli avvisi anche a Slack.

Quello che non ho in questo momento è una soluzione di registrazione centralizzata. ELK è potente ma difficile da configurare e gestire e non conosco alternative gratuite abbastanza vicine da valerne la pena.


### Sematext + Logagent + Experience

Sematext per le metriche, per i log, per le tracce e presto anche per il monitoraggio degli utenti reali. Più semplice/economico rispetto all'uso di N strumenti/servizi diversi, secondo la mia umile opinione.

Per l'invio dei log usavamo rsyslog e poi siamo passati a Logagent.

Per la segnalazione dei crash del front-end usiamo Sentry, ma presto passeremo a Experience.

Chiarimento: sono un Sematextiano.


### Azure Monitor/Analytics + OpsGenie

Vorrei che Log Analytics avesse un'interfaccia migliore. Ci stiamo allontanando da splunk, che era molto più facile da navigare.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Non vuoi davvero gestire il tuo sistema di notifica. Puoi sostituire Splunk con ELK a meno che il tuo team di sicurezza non preferisca Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf come raccoglitore, Prometheus + Alertmanager per il monitoraggio e gli avvisi, integrati con canali slack e pagerduty per gli avvisi critici. Grafana per la visualizzazione delle metriche degli host.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus per metriche + avvisi

Grafana per le dashboard di Prometheus

Cloudwatch monitora le istanze Prometheus

sentry per il tracciamento delle eccezioni

kibana + elasticsearch

graylog

prometheus Push Gateway per batch/cronjob

SOP https://github.com/rapidloop/sop per "spingere/inoltrare" metriche da 1 istanza Prometheus a un'altra

i client usano i client Prometheus. Stiamo cercando di usare opencensus.io lato client


### PagerDuty + Monitis

PagerDuty + Monitis. Anche alcune Azure Functions su misura per testare la salute di certi servizi.

Spero di poter adottare Prometheus e Grafana quest'anno


### Prometheus + Grafana + Bosun

Prometheus per archiviare i dati delle serie temporali. Grafana per la visualizzazione. Bosun per la gestione degli avvisi.


### Azure Monitor/Analytics/Insights/Dashboards

Solo Azure: Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana per monitorare i servizi container in Kubernetes tramite Prometheus

Monitis per il monitoraggio end-to-end dei servizi, principalmente per API web e applicazioni web

OpsGenie per la gestione degli avvisi

Slack per ricevere informazioni di stato dai nostri sistemi


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Ingegnere (dev)ops di lunga data qui. Cresciuto con Nagios. Mi piacerebbe sentire opinioni sul mio SaaS autofinanziato https://checklyhq.com. Facciamo monitoraggio delle API e monitoraggio delle transazioni dei siti web con avvisi abbastanza approfonditi.

Ho avviato Checkly perché il monitoraggio attivo / sintetico nello spazio delle API era un po' limitato (e costoso). Il monitoraggio basato su browser / con script è ancora più proprietario e costoso. Usiamo Puppeteer e manteniamo i prezzi il più bassi possibile.

Il nostro stack di monitoraggio:

Checkly (dogfooding...)

AppOptics (grafici personalizzati)

AWS Cloudwatch & SNS per i messaggi SMS.

avvisi integrati di Heroku.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana ci avvisa in slack di problemi di infrastruttura o degrado delle prestazioni e abbiamo configurato logz.io per avvisare in slack a un certo volume di log a livello di errore dal livello applicativo.


### SignalFX + Splunk + PagerDuty + Slack

Uso attualmente: SignalFX, Splunk, PagerDuty e Slack. Non sono un grande fan di SignalFX anche se il loro team di supporto è super amichevole e reattivo. Mi piace Splunk (vale la pena se puoi permettertelo), PagerDuty e Slack.

Usavo lo stack TICK dove la maggior parte della C era in realtà G, cioè Grafana, anche se ho usato un po' anche Chronograf. Era fantastico ma una seccatura da gestire. La classica domanda dilemma SaaS contro self-hosting.

Ho usato DataDog, New Relic, Graylog, ELK e BugSnag. Mi piacciono molto DataDog e New Relic, Graylog è abbastanza buono. Non sono un grande fan di ELK. BugSnag è bello, mi sembra in realtà che il tracciamento di errori/eccezioni in molti casi sia una sostituzione abbastanza buona del monitoraggio completo dei log.


### ELK + Prometheus + Grafana

Come altri, usiamo ELK per i log e Prometheus+Grafana per tutto il resto.

Mantenere questa configurazione è semplice se ti permetti di perdere occasionalmente dei dati. Se per esempio il nostro database ElasticSearch finisce in un calo (cosa che purtroppo ci accade ogni 2-3 mesi), non ci preoccupiamo dell'HA ma buttiamo via i dati e andiamo avanti con le nostre vite. Se hai assolutamente bisogno di HA o di archiviazione a lungo termine, buona fortuna.


### Datadog + Prometheus + Grafana

Ho configurato Datadog su base mensile perché quando sono arrivato qui non c'era né monitoraggio né avvisi. Solo un paio dei nostri siti venivano monitorati ogni 5 minuti per l'uptime. Datadog è di gran lunga il più facile da configurare. Quando avrò finito di affrontare tutti gli altri problemi, passerò a Prometheus+Grafana. Non ancora sicuro al 100% sulla gestione dei log.

### Nagios + ELK

Supportiamo oltre 100+ prodotti.

Per l'on-prem è per lo più Nagios ed ELK. Per il cloud stiamo migrando da DataDog a NewRelic.


### Datadog rispetto a Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Usavamo datadog ma l'abbiamo trovato troppo costoso per le nostre esigenze. Non fraintendermi, è fantastico ma ha un costo enorme. Siamo riusciti a configurare site24x7.com con un abbonamento annuale per circa 2-3 mesi di costo di DD.

Il nostro stack di monitoraggio:

Site24x7 - APM, monitoraggio di URL esterni, monitoraggio del flusso di posta SMTP, data di scadenza ssl e monitoraggio dei processi.

StatusCake - per il monitoraggio e la conferma degli URL - È il nostro backup nel caso site24x7 si lasci sfuggire qualcosa (non lo fa) ma SC è più flessibile per il monitoraggio di porte e servizi esterni per le nostre esigenze.

Entrambi gli strumenti scalano a PagerDuty e poi riceviamo le nostre escalation in slack.

SumoLogic - per il monitoraggio dei log (è uno strumento fantastico ma un po' complicato per le nostre esigenze)

Da slack possiamo confermare (ack) o risolvere l'avviso.

Poi abbiamo molte automazioni site24x7 che si collegano a commando.io per quello che chiamiamo 'BedOps' - dove un avviso si attiva avviamo alcuni script o automazioni nel tentativo di rimediare alla situazione (il 99% delle volte l'automazione + i nostri script ci tengono fuori dai guai).

Abbiamo runbook interni nella nostra KB per quando le automazioni falliscono o se c'è qualcosa fuori ambito che deve essere risolto.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana per le metriche nei nostri cluster GKE e VM.

Google Stackdriver per i log (perché è incluso e attivo per impostazione predefinita e per ora è sufficiente per le nostre esigenze).


### Zabbix

Zabbix per tutto. Non serve altro software.
