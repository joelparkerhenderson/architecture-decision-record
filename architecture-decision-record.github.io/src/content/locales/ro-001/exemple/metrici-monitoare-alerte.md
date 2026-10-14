# Metrici, monitoare, alerte

Cuprins:

* [Rezumat](#rezumat)
  * [Problemă](#problemă)
  * [Decizie](#decizie)
  * [Stare](#stare)
* [Detalii](#detalii)
  * [Ipoteze](#ipoteze)
  * [Constrângeri](#constrângeri)
  * [Poziții](#poziții)
  * [Argument](#argument)
  * [Implicații](#implicații)
* [Conexe](#conexe)
  * [Decizii conexe](#decizii-conexe)
  * [Cerințe conexe](#cerințe-conexe)
  * [Artefacte conexe](#artefacte-conexe)
  * [Principii conexe](#principii-conexe)
* [Note](#note)
  * [Mesaje text liber față de mesaje de eveniment structurate](#mesaje-text-liber-față-de-mesaje-de-eveniment-structurate)
  * [Graylog este mai ușor](#graylog-este-mai-ușor)
  * [Prometheus necesită ceva reglaj](#prometheus-necesită-ceva-reglaj)
  * [Serviciile AWS lasă impresii amestecate](#serviciile-aws-lasă-impresii-amestecate)
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


## Rezumat


### Problemă

Vrem să folosim metrici, monitoare și alerte, pentru că vrem să știm cât de bine funcționează aplicațiile noastre și să aflăm când apare o problemă.


### Decizie

În lucru (WIP).


### Stare

Colectăm informații. Începem cu capetele plauzibile ale spectrului: cel mai recomandat instrument gratuit mai vechi (Nagios) și cel mai recomandat instrument plătit mai nou (New Relic).


## Detalii


### Ipoteze

Vrem să creăm aplicații web moderne, rapide, fiabile, responsive etc.

Vrem să cumpărăm, nu să construim.


### Constrângeri

Vrem instrumente care funcționează bine cu fluxul nostru devops și cu cloud-urile noastre de implementare.


### Poziții

Cercetăm acum pozițiile.


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

Până acum, Nagios și New Relic sunt capetele spectrului. Nagios este cel mai vechi, cel mai simplu, gratuit și viabil instrument. New Relic este instrumentul cu cele mai noi funcții, cel mai complet, plătit și viabil. Vom începe cu evaluări ale acestora. La nevoie, vom trece spre interiorul spectrului.  

Până acum, Zabbix are cele mai bune recomandări și oferă și cele mai complete capabilități.

Până acum, ELK are cea mai bună popularitate în rândul soluțiilor open source construite în locul celor cumpărate.

Până acum, Prometheus + Grafana au cea mai bună popularitate.


### Implicații

De făcut.


## Conexe


### Decizii conexe

Alegerile vor afecta testabilitatea, telemetria și, probabil, alte sisteme, precum cele pentru serviciul clienți, ingineria fiabilității site-urilor (SRE) etc.


### Cerințe conexe

De făcut.


### Artefacte conexe

De făcut.


### Principii conexe

Ușor reversibil.

Nevoia de viteză.


## Note


Un stack open source destul de bun este:

* Prometheus pentru metrici și alertare bazată pe metrici

* Grafana pentru afișarea metricilor

* Elasticsearch/Logstash/Kibana (ELK) pentru loguri și evenimente structurate

* Pushover pentru notificări mobile


### Mesaje text liber față de mesaje de eveniment structurate

Mesaje text liber: de exemplu, genul de lucruri aleatorii pe care le găsești în /var/log/messages și ceva generat intenționat de aplicație. Mesajele sunt utile pentru identificarea altor lucruri care se întâmplă pe mașină, precum lipsa de memorie sau erorile hardware, dar conțin multe gunoaie. 

Mesaje de eveniment structurate: generate de aplicație, cu un set fix sau dinamic de atribute, de exemplu un jurnal de cereri HTTP, un jurnal contabil, o autentificare de utilizator.

În general, este bine să logăm detalii despre fiecare cerere într-un mod în care să putem explora după atribute. Adăugarea, de exemplu, a unui userid sau sessionid la tot permite urmărirea. Urmărirea explicită (tracing) este, desigur, de asemenea bună. Folosirea ELK pentru aceasta este un fel de variantă a săracului pentru https://www.honeycomb.io/


### Graylog este mai ușor

Din experiența mea, Graylog este mai ușor de pus în funcțiune.



### Prometheus necesită ceva reglaj


În general sunt mulțumit de Prometheus pentru metrici. Alertarea necesită ceva reglaj, dar este destul de bună. Depinde de aplicația ta. Cred că cel mai bine este să alertezi pe condiții vizibile utilizatorului final, nu pe cauze subiacente. De exemplu, timpul de încărcare a paginii este bun, numărul de cereri pe secundă nu. Deși zero cereri pe secundă indică faptul că ceva nu este în regulă.

Avantajul unui serviciu este că oferă inteligență suplimentară din start. În general îmi place Datadog. Serviciile pot fi înfricoșător de scumpe dacă ai multe date și uneori au modele de preț care nu sunt prietenoase cu cloud-ul, de exemplu taxare per instanță, când instanțele sunt dinamice. Există și o diferență între serviciile în care fiecare cerere provine de la un utilizator plătitor și cele legate de publicitate, unde doar un mic procent din cereri aduce bani. Poți ajunge cu multe date și un buget nu prea mare.

Lucrez la câteva servicii care primesc 1 mld. de cereri pe zi, deci are sens să ne găzduim propriul monitoring și logare. Dacă volumele tale sunt mai mici, serviciile găzduite sunt mai ușoare.


### Serviciile AWS lasă impresii amestecate

Experiența mea cu serviciile AWS a fost amestecată. Serviciul lor Elasticsearch a fost instabil, așa că rulăm propriile instanțe pentru asta. Metricile CloudWatch sunt scumpe, așa că le folosim de obicei doar pentru metrici la nivel de „infrastructură”, nu de aplicație, adică metrici legate de sănătate, unde AWS poate ști mai bine ce se întâmplă decât software-ul care rulează pe instanță. Logurile CloudWatch pot fi lente la actualizare și nu au prea multe metadate. Rularea ELK ajută în acest sens. Dacă vreau cu adevărat date în timp real, folosirea Kafka ca transport pentru loguri este mai bună. Este bine suportat de Logstash. Administrarea unui cluster Kafka nu este totuși pentru cei slabi de înger, există multă instalație expusă.


### Kafka

Comentariu: Kafka poate fi uneori extrem de dificil sau poate fi solid ca piatra, încât aproape uiți că există și că leagă totul laolaltă. 


Comentariu: Kafka a fost solid, dar a fost surprinzător de multă muncă să-l punem în funcțiune. Mă gândesc la el ca la o bază de date relațională, dar în care lucrezi doar la nivelul „fizic”, de exemplu spații de tabele, fișiere și partiții. La început au fost momente în care lipseau utilitarele de administrare și a trebuit să scriem programe, de exemplu pentru resetarea unui grup de consumatori. http://howfuckedismydatabase.com/nosql/

Comentariu: Folosim Kafka ca „tampon” pentru mesajele de log și ca loc unde putem face procesare de flux în timp real a datelor care vin de la mai multe servere. Dacă primim un atac DDOS, avem nevoie de o modalitate de a analiza datele de pe mai multe instanțe. Dacă logăm direct de pe servere în ELK, încărcarea poate prăbuși clusterul Elasticsearch.

Comentariu: Kafka este bun pentru noi pentru că, dacă primim un atac DDOS, avem nevoie de o modalitate de a analiza datele de pe mai multe instanțe. Dacă logăm direct de pe servere în ELK, încărcarea poate prăbuși clusterul Elasticsearch.


Comentariu: Kafka face mai puțină muncă și este mai eficient, deci poate gestiona mai bine încărcarea. Iar munca Kafka o punem în coadă și o reîncercăm. Iar faptul că Kafka este supraîncărcat nu afectează utilizatorii care încearcă să lucreze interactiv cu Kibana, așa cum ar face-o dacă Elasticsearch ar fi în dificultate.

Comentariu:  Procesarea de flux caută în principal abuzuri, de exemplu prea mult trafic de la o singură adresă IP în tot clusterul, apoi partajează blocarea în tot clusterul.

Comentariu: Pluginul logstash-output-kafka este însă destul de nefiabil în prezent. M-am lovit de mai multe dintre problemele de pe pagina lui de issues de pe GitHub, care par să nu fie niciodată rezolvate. Vreau să renunț la el și să trimit direct din aplicațiile noastre către Kafka.

Comentariu: Acum trimitem evenimente structurate direct din aplicație către Kafka. Motivația principală a fost atingerea datelor de log de mai puține ori și evitarea citirii și scrierii pe disc de mai multe ori. În sistemele cu volum mare, logarea poate necesita mai multă muncă decât aplicația însăși. Mă gândesc să fac ca journald să trimită direct și el logurile, dintr-un program C.


### Loki

Ține un ochi pe Loki. Nu este încă gata, dar când va fi, mă aștept să se potrivească mai bine în acest stack. Loki este un agregator de loguri creat de Grafana Labs, care folosește o sintaxă similară cu cea a Prometheus pentru colectare și etichete.


### Prometheus + alertmanager + Rollbar + Graylog + Grafana

 Prometheus + alertmanager pentru metrici. <3 Prometheus.

Rollbar/Graylog pentru logare/raportarea erorilor (există o suprapunere aici; un serviciu mic probabil nu le are nevoie pe amândouă).

În prezent, alertele merg doar pe unul dintre câteva canale Slack pentru care părțile interesate au notificările activate. Dacă am fi mai serioși cu privire la permanență (on-call), ar merge la PagerDuty/VictorOps etc.

Grafana pentru grafice și tablouri de bord. Aștept cu nerăbdare să văd dacă viitoarele lor funcții de logare vor face Graylog inutil.


### Thanos

Folosim Thanos ca front-end pentru configurația noastră HA. Știe să deduplice perechile HA.

În prezent păstrăm 6 luni de date locale Prometheus. Funcționează rezonabil de bine pentru noi. Dar sunt chiar în mijlocul implementării stocării de tip bucket în configurația noastră Thanos pentru stocarea datelor pe termen lung. În teorie, stocarea GCS va fi cu aproximativ 30% mai ieftină decât discul persistent standard GCE pe care îl folosim acum.

Momentan nu facem copii de siguranță ale datelor Prometheus. Datele pur și simplu nu sunt foarte importante pentru noi dincolo de a avea suficiente pentru alertare. Implementarea noastră generală a flotei se schimbă atât de mult de la an la an, încât datele istorice mai vechi de câteva luni nu sunt prea interesante. Ar putea fi interesant să avem câteva statistici de bază de la an la an; aș putea configura un set de reguli de înregistrare pentru statisticile de bază și să le stochez cu Federation sau să las pur și simplu Thanos să se ocupe.

EDIT: O mică precizare: sunt dezvoltator Prometheus.


### Prometheus HA

HA în Prometheus se face prin duplicare — rulezi mai multe instanțe de colectare și există modalități de a interoga mai multe și de a deduplica datele

Scalarea se face prin împărțirea rețelei și interogarea diferitelor părți ale rețelei de către instanțe Prometheus diferite

Stocarea pe termen lung nu este punctul forte al Prometheus, ci este delegată unor soluții precum Influx sau timescaledb (care, tehnic, bifează și el HA) articolul pe care l-am citit despre aceasta https://blog.timescale.com/prometheus-ha-postgresql-8de68d19b6f5?gi=7df160f10e07

Nu am încercat încă soluțiile pe termen lung, pentru că încă doar experimentez și îl folosesc pentru grafice pe termen scurt, în timp ce librenms îmi monitorizează rețeaua pe termen lung


###  Datadog + PagerDuty + Threat Stack

Folosim Datadog (cu PagerDuty) și Threat Stack și nu am putea fi mai mulțumiți. Singura mea nemulțumire față de DD este costul relativ ridicat al stocării metricilor.


### Zabbix

Zabbix cu scripturi proprii pentru a monitoriza aproape orice. Funcționează de minune.


### Outlyer

Folosesc Outlyer, dar trebuie să precizez că lucrez aici, iar folosirea propriului produs este obligatorie.

Mai am nevoie de Graylog, Sentry și Statuscake pentru completare.

Sună părtinitor, dar, după ce am rulat cu plăcere Nagios și alte sisteme de monitorizare intern, la orice nou loc de muncă aș cumpăra o soluție găzduită și aș scăpa de acea durere.


### Nagios + Nagiosgraph

Rulăm Nagios pentru toată monitorizarea și alertarea. Alertele se fac prin e-mail (avertismente și notificări critice) și notificări sonore ale aplicației (pentru alertele critice).

Nagiosgraph este folosit pentru vizualizări.

Această configurație a fost foarte eficientă în a ne ține pe deplin informați despre ce se întâmplă în mediul nostru. Rulăm și monitorizăm aproximativ 110 servere esențiale pentru misiune și aproximativ 760 de puncte de date și avem acest sistem în funcțiune de peste șapte ani.

Aș vrea, de asemenea, să agregăm la un moment dat logurile cu Graylog sau ELK.


### Prometheus + Grafana + AlertManager

Prometheus + Grafana + AlertManager prin grafic helm-ul grozav Prometheus Operator. Logurile merg în continuare la planul birch LogDNA, deoarece am observat că ELK este prea greu pentru modestul nostru cluster cu min. 3 și max. 5 noduri pe GKE.


### DataDog + Sentry + PagerDuty.

Obișnuiam să rulez toate soluțiile mele de monitorizare, folosind tot felul de software, inclusiv Nagios, Icinga, Zabbix, ELK, Greylog2, Influx și multe alte instrumente, dar adevărul este că e prea mult efort să-ți rulezi propria infrastructură de monitorizare, mai ales când poți plăti pe altcineva cu tarife atât de mici ca să o facă în locul tău!

Plătind pe alții să ruleze infrastructura de monitorizare, clienții mei sunt eliberați să se concentreze pe rularea platformelor lor, nu pe monitorizarea monitorizării, ceea ce înseamnă că valoarea pe care o obțin din stabilitatea platformei depășește cu mult orice costuri ale monitorizării ca serviciu.


### Sensu + Graphite + ELK

Compania mea pune mare accent pe soluții găzduite propriu.

Sensu -> PagerDuty

Graphite/Grafana

ELK (Elasticsearch, Logstash, Kibana)


### Prometheus + Alertmanager

Prometheus + Alertmanager pentru alertare; echipa mea crede că o monitorizare simplă este o monitorizare bună.

Alte sisteme, precum logarea și urmărirea, oferă context bogat pentru diagnostic atunci când cel de serviciu primește o alertă, dar nu construim niciodată alerte pe baza acestora.


### Sensu + Grafana + Graylog + Kibana + NewRelic.

Sensu, grafana, graylog, kibana, newrelic.


### Prometheus + Circonus

Servicii instrumentate cu Prometheus => analiză și vizualizare Circonus


### icinga2 + VictorOps + NewRelic + Sentry + Slack

Folosim serviciile de mai jos:

icinga2 pentru monitorizare și VictorOps pentru alertare

NewRelic pentru monitorizarea detaliată a serviciului

Sentry pentru urmărirea erorilor din serviciu

Slack/e-mail fac parte din alertare, declanșată de NewRelic sau icinga2


### AppDynamics + Papertrail + PagerDuty + Healthchecks.io + Stackdriver

AppDynamics

Papertrail

PagerDuty

Healthchecks.io

Stackdriver


### icinga2 + elasticsearch

icinga2 cu integrare elasticsearch pentru analiză și integrare graphite+grafana pentru grafice.

datorită flexibilității regulilor apply din icinga2, dezvoltatorii văd doar serviciile pentru care primesc notificări.

iar prin icinga2 director, programatorii își pot defini ușor propriile verificări (ceea ce fac, la fiecare câteva zile — 100 de verificări ies, alte 100 intră) la scară mare, fără bătăi de cap.


### DataDog + New Relic + ELK + EFK + Sentry + Alertmanager + VictorOps

Ce avem acum:

DataDog pentru metrici

New Relic pentru monitorizarea aplicațiilor

ELK (Elastic Search + Logstash + Kibana) pentru loguri

Sentry (găzduit propriu) pentru logarea excepțiilor

E-mailuri + Slack + VictorOps pentru alertare (în funcție de severitate)

Ce vrem să avem:

Prometheus pentru metrici (Grafana pentru vizualizare)

New Relic (probabil Elastic Search APM) pentru monitorizarea aplicațiilor

EFK (elastic search + fluentd + kibana) pentru logare. Probabil Loki de la Grafana va fi gata de producție până ajungem acolo

Sentry pentru excepții

Alertmanager + e-mail + VictorOps pentru alerte


### Wavefront + Scalyr + PagerDuty + Stackstorm + Slack

Wavefront + Scalyr + PagerDuty + Stackstorm + Slack (Precizare: lucrez la VMware)


### Telegraf + Prometheus + InfluxDB + Grafana

Telegraf pentru metricile serverului, precum CPU, disc, memorie și rețea. Folosim Telegraf și pentru monitorizarea SNMP a dispozitivelor noastre de rețea.

Prometheus pentru metricile aplicației. Încorporăm în aplicație verificări de stare pe care Prometheus le colectează.

InfluxDB pentru stocarea seriilor de timp. Acolo sunt trimise datele Telegraf.

Grafana pentru tablouri de bord și alerte. Motorul de alertare nu este foarte robust, dar își face treaba. Trimitem alerte și pe Slack.

Ce nu am acum este o soluție centralizată de logare. ELK este puternic, dar dificil de configurat și administrat și nu cunosc alternative gratuite suficient de apropiate pentru a le explora.


### Sematext + Logagent + Experience

Sematext pentru metrici, pentru loguri, pentru urme, în curând și pentru monitorizarea utilizatorilor reali. Mai simplu/mai ieftin decât folosirea a N instrumente/servicii diferite, după părerea mea.

Pentru expedierea logurilor obișnuiam să folosim rsyslog, apoi am trecut la Logagent.

Pentru raportarea blocărilor front-end folosim Sentry, dar vom trece în curând la Experience.

Precizare: sunt un Sematextan (angajat Sematext).


### Azure Monitor/Analytics + OpsGenie

Mi-aș dori ca Log Analytics să aibă o interfață mai bună. Ne îndepărtăm de Splunk, care era mult mai ușor de navigat.


### Prometheus + Alertmanager + Grafana + Splunk + PagerDuty

Prometheus, Alertmanager, Grafana, Splunk, PagerDuty

Chiar nu vrei să-ți rulezi propriul sistem de notificări. Poți înlocui Splunk cu ELK, cu excepția cazului în care echipa ta de securitate preferă Splunk.


### Telegraf + Prometheus + Grafana + Alertmanager

Telegraf ca colector, Prometheus + Alertmanager pentru monitorizare și alertare, integrate cu canale Slack și pagerduty pentru alerte critice. Grafana pentru vizualizarea metricilor gazdelor.


### Prometheus + Grafana + Cloudwatch + sentry + kibana + elasticsearch

Prometheus pentru metrici + alerte

Grafana pentru tablourile de bord Prometheus

Cloudwatch monitorizând instanțele Prometheus

sentry pentru urmărirea excepțiilor

kibana + elasticsearch

graylog

prometheus Push Gateway pentru joburi batch/cronjob-uri

SOP https://github.com/rapidloop/sop pentru a „împinge/redirecționa“ metrici de la o instanță Prometheus la alta

clienții folosesc clienții Prometheus. Încercăm să folosim opencensus.io pe partea de client


### PagerDuty + Monitis

PagerDuty + Monitis. Plus câteva Azure Functions proprii pentru testarea stării unor servicii.

Intenționăm să introducem Prometheus și Grafana anul acesta


### Prometheus + Grafana + Bosun

Prometheus pentru stocarea datelor de serii de timp. Grafana pentru vizualizare. Bosun pentru gestionarea alertelor.


### Azure Monitor/Analytics/Insights/Dashboards

Companie exclusiv Azure: Azure Monitor, Log Analytics, App Insights, Azure Dashboards + Pager Duty


### Grafana + Monitis + OpsGenie + Slack

Grafana pentru monitorizarea serviciilor din containere în Kubernetes prin Prometheus

Monitis pentru monitorizarea end-to-end a serviciilor, în principal pentru API-uri web și aplicații web

OpsGenie pentru gestionarea alertelor

Slack pentru a primi informații despre starea sistemelor noastre


### Checkly + AppOptics + Cloudwatch + Heroku + Pagerduty + Papertrail

Sunt de mult timp inginer (dev)ops. Am crescut cu Nagios. Mi-ar plăcea să aud opinii despre SaaS-ul meu bootstrapped https://checklyhq.com. Facem monitorizare de API-uri și de tranzacții pe site, cu alertare destul de aprofundată.

Am început Checkly pentru că monitorizarea activă / sintetică în zona API-urilor era cam limitată (și scumpă). Monitorizarea bazată pe browser / scripturi este și mai proprietară și mai scumpă. Folosim Puppeteer și ținem prețurile cât mai mici.

Stack-ul nostru de monitorizare:

Checkly (folosim propriul produs...)

AppOptics (grafice personalizate)

AWS Cloudwatch și SNS pentru mesaje SMS.

alertare integrată Heroku.

Pagerduty

Papertrail


### Instana + Logz.io + slack

Instana ne alertează pe Slack despre probleme de infrastructură sau degradarea performanței, iar logz.io l-am configurat să alerteze pe Slack la un anumit volum de loguri de nivel eroare din stratul aplicației.


### SignalFX + Splunk + PagerDuty + Slack

În prezent folosim: SignalFX, Splunk, PagerDuty și Slack. Nu sunt un mare fan SignalFX, deși echipa lor de suport este super prietenoasă și receptivă. Îmi place Splunk (merită dacă îți permiți să plătești), PagerDuty și Slack.

Obișnuiam să folosesc stack-ul TICK, în care majoritatea lui C era de fapt G, adică Grafana, deși am folosit puțin și Chronograf. Era grozav, dar greu de administrat. Dilema clasică SaaS versus găzduire proprie.

Am folosit DataDog, New Relic, Graylog, ELK și BugSnag. Îmi plac mult DataDog și New Relic, Graylog este destul de bun. Nu sunt un mare fan ELK. BugSnag este drăguț, de fapt simt că urmărirea erorilor/excepțiilor este, în multe cazuri, un înlocuitor destul de bun pentru monitorizarea completă a logurilor.


### ELK + Prometheus + Grafana

Ca și alții, folosim ELK pentru loguri și Prometheus+Grafana pentru tot restul.

Întreținerea acestei configurații este ușoară dacă îți dai voie să pierzi ocazional date. De exemplu, dacă baza noastră de date ElasticSearch intră într-o pasă proastă (ceea ce, din păcate, se întâmplă la noi la fiecare 2-3 luni), nu ne mai batem capul cu HA, ci aruncăm datele și mergem mai departe. Dacă ai absolut nevoie de HA sau de retenție pe termen lung, succes.


### Datadog + Prometheus + Grafana

Am configurat Datadog lunar, pentru că atunci când am ajuns aici nu exista monitorizare și nici alertare. Doar câteva dintre site-urile noastre erau monitorizate la fiecare 5 minute pentru disponibilitate. Datadog este, fără discuție, cel mai ușor de configurat. Când termin de rezolvat toate celelalte probleme, voi trece la Prometheus+Grafana. Încă nu sunt 100% hotărât în privința managementului logurilor.

### Nagios + ELK

Suportăm peste 100 de produse.

Local (on-prem) este în mare parte Nagios și ELK. În cloud, migrăm de la DataDog la NewRelic.


### Datadog vs. Site24x7 + StatusCake + PagerDuty + SumoLogic + Slack

Obișnuiam să folosim datadog, dar l-am găsit mult prea scump pentru nevoile noastre. Să nu mă înțelegeți greșit, este uimitor, dar are un cost uriaș. Am reușit să configurăm site24x7.com cu un abonament anual de aproximativ 2-3 luni din costul DD.

Stack-ul nostru de monitorizare:

Site24x7 - APM, monitorizarea URL-urilor externe, monitorizarea fluxului de poștă SMTP, expirarea certificatelor ssl și monitorizarea proceselor.

StatusCake - pentru monitorizarea și confirmarea URL-urilor - este copia noastră de siguranță în caz că site24x7 ratează ceva (nu ratează), dar SC este mai flexibil pentru monitorizarea porturilor și serviciilor externe, pentru nevoile noastre.

Ambele instrumente escaladează către PagerDuty, apoi primim escaladările pe Slack.

SumoLogic - pentru monitorizarea logurilor (este un instrument grozav, dar puțin complicat pentru nevoile noastre)

Din Slack putem confirma sau remedia alerta.

Avem apoi multe automatizări site24x7 care se conectează la commando.io pentru „BedOps”, cum îi spunem noi — când se declanșează o alertă, pornim câteva scripturi sau automatizări pentru a încerca să remediem situația (în 99% din cazuri automatizarea + scripturile noastre ne țin departe de probleme).

Avem runbook-uri interne în baza noastră de cunoștințe pentru cazul în care automatele eșuează sau există ceva în afara domeniului care trebuie reparat.


### Prometheus + AlertManager + Grafana + Stackdriver

Prometheus (Operator) / AlertManager / Grafana pentru metrici în clusterele noastre GKE și în mașinile virtuale.

Google Stackdriver pentru loguri (deoarece este inclus și activ implicit și în prezent este suficient pentru nevoile noastre).


### Zabbix

Zabbix pentru tot. Nu este nevoie de niciun software suplimentar.


