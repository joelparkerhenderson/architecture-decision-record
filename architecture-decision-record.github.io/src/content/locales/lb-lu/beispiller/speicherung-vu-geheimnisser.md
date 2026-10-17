# Späicherung vu Geheimnisser

Inhalt:

* [Zesummefaassung](#zesummefaassung)
  * [Problem](#problem)
  * [Decisioun](#decisioun)
  * [Zoustand](#zoustand)
* [Detailer](#detailer)
  * [Viraussetzungen](#viraussetzungen)
  * [Restriktiounen](#restriktiounen)
  * [Positiounen](#positiounen)
  * [Argument](#argument)
  * [Implikatiounen](#implikatiounen)
* [Verwandt](#verwandt)
  * [Verwandt Decisiounen](#verwandt-decisiounen)
  * [Verwandt Ufuerderungen](#verwandt-ufuerderungen)
  * [Verwandt Artefakten](#verwandt-artefakten)
  * [Verwandt Prinzipien](#verwandt-prinzipien)
* [Notizen](#notizen)
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Zesummefaassung


### Problem

Mir mussen Geheimnisser späichere, wéi Passwierder, privat Schlësselen, Authentifikatiounstokens, asw.

E puer vun de Geheimnisser si benotzerorientéiert. Zum Beispill wëll eisen Entwéckler säin Handy kënne benotzen, fir e Passwuert zu engem Service nozeschloen.

E puer vun de Geheimnisser si systemorientéiert. Zum Beispill muss eis Continuous-Delivery-Pipeline fäeg sinn, d'Umeldedaten fir eist Cloud-Hosting nozeschloen.


### Decisioun

Bitwarden fir benotzerorientéiert Geheimnisser

Vault vun HashiCorp fir systemorientéiert Geheimnisser.


### Zoustand

Decidéiert. Mir si fir nei Alternativen op, soubal se opkommen.


## Detailer


### Viraussetzungen

Fir dësen Zweck, an eisen aktuellen Zoustand, schätze mir benotzerorientéiert Bequemlechkeet, wéi benotzbar mobil Apps.

  * Mir wëllen einfachen Zougang ënnerwee suergen, zum Beispill fir en Entwéckler, deen On-Call-System-Reliability-Engineering mécht.

  * Mir wëllen fäeg sinn, e puer Geheimnisser ënnert ausgewielte Leit ze deelen, wéi engem Team.

Mir probéieren net, fir een eenzege Provider ze léisen, wéi all Geheimnisser exklusiv bei Amazon oder Azure oder Google ze späicheren.

Mir wëllen keng Ad-hoc-Usätz wéi "behal et" oder "schreif et op eng Notiz" oder "fënn deng eege Manéier, et ze späicheren".

Eise Sécherheetsmodell fir dësen Zweck ass domat zefridden, gutt ugesinn COTS-Vendoren ze benotzen, wéi SaaS-Passwuertverwaltungstools.


### Restriktiounen

Momentan wëlle mir eppes, dat einfach ass, dat heescht kee Code ze schreiwen, keng Server z'installéieren, keen décke Commitment, keen Standardiséieren vu jidderengem.


### Positiounen

Mir hunn berécksiichtegt:

1. Benotzerorientéiert Off-the-Shelf-Passwuertmanager: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG, asw.

2. Systemorientéiert COTS-Passwuertmanager: AWS KMS, Vault vun HashiCorp, EnvKy, Secret Server vun Thycotic, Devolutions Password Server, Confidant vu Lyft.

3. Deelungsorientéiert Usätz: e gedeelt Google-Dokument, e gedeelte Slack-Kanal, e gedeelten Netzwierkuerdner, asw.

4. Low-Tech-Ad-hoc-Usätz, wéi sech et ze merken, eng Notiz ze schreiwen, oder sech drop ze verloossen, datt jiddere Benotzer säin eegene Wee fënnt.


### Argument

Bitwarden, LastPass, 1Password an Dashlane sinn all kommerziell Off-the-Shelf-Produkter.

  * Ähnlech Zorte vu Funktioune fir Benotzer, Teams, Organisatiounen, asw.

  * Desktop-Fäegkeet fir Windows a Mac, a mobil Fäegkeet fir Android an iOS.

  * Browser-Extensiounen fir Chrome a Firefox, fir automatescht Ausfëlle vu Formulairen, asw.

Bitwarden huet zwee Virdeeler géintiwwer den anere:

  * Bitwarden ass Open Source, wat bedeit, datt d'Sécherheet vu Kolleege kann iwwerpréift ginn an d'Firma och vu sécherheetsorientéierten Entwéckler wäit geschätzt gëtt.

  * Anekdoten vu Softwareaarbechter beschreiwen eng bedeitend Präferenz fir Bitwarden iwwer d'anerer.

E typesche gudde Beispill-Artikel: https://jcs.org/2017/11/17/bitwarden

Eng typesch Side-by-Side-Ofstëmmungssäit: https://stackshare.io/stackups/bitwarden-vs-dashlane

Mir verschiebe KeyPass, pass, GPG, asw., well et zousätzlech Komplexitéit gëtt. All dës gesinn aus wéi gutt Léisunge fir technesch Benotzer. GPG gesäit besonnesch gutt aus fir technesch Benotzer, déi systemiwwergräifend kommandoorientéiert Fäegkeete wëllen.

Mir verschiebe KMS, well et Single-Provider-Lock-in huet.

Mir wielen Vault fir systemorientéiert Bedierfnisser, well d'Reviewe verbléffend positiv sinn, a well HashiCorp eng exzellent Erfolleg fir Software an Ënnerstëtzung vun der Top-Qualitéit huet.

Mir leeën Veto géint d'Deelungsusätz an, wéi duerch gedeelt Dokumenter, gedeelte Kanäl, gedeelt Netzwierkuerdner, asw. Dës bidden net d'Sécherheetsqualitéiten, déi mir wëllen.

Mir leeën Veto géint d'Ad-hoc-Low-Tech-Usätz an, well mir all averstane sinn, datt et kee laangfristege Wee no vir ass.


### Implikatiounen

Entwéckler mussen eventuell Geheimnisser op zwou Plazen verfollegen: Bitwarden fir benotzerorientéierten Zougang, a Vault fir systemorientéierten Zougang.


## Verwandt


### Verwandt Decisiounen

D'Decisioun, wéi eng CI/CD-Server, muss de Beweis vu Fäegkeet fir den Zougang zu Geheimnisser enthalen.

Mir mussen entscheeden, wéi mir d'Geheimnisser verwalten, a Bezuch op Politiken, Rotatiounen, Organisatiounen, asw.


### Verwandt Ufuerderungen

D'Geheimnisser wäerte verwandt Ufuerderunge fir Compliance, Auditing an HR-Onboarding/-Offboarding hunn.


### Verwandt Artefakten

Mir erwaarden, datt mir eventuell e puer Geheimnisser an Emgebungsvariabele exportéieren.


### Verwandt Prinzipien

Einfach réckgängeg ze maachen.

Einfach parallel, dat heescht, et ass einfach, eng Varietéit vu Passwuertmanager ze benotzen.

Bëlleg ze probéieren, dat heescht, et gëtt eng gratis Testversioun a kee Commitment.


## Notizen

Evaluatiounsnotizen hei. D'Notizen sinn all ëffentlech Kommentarer op verschiddene Devops-Diskussiounsboards.


### Vault by HashiCorp

Vault ass genau dat, wat Dir hei wëllt. 

Setzt Vault awer net einfach an d'Produktioun, installéiert en éischt an engem Testëmfeld, well dem HashiCorp seng Dokumentatioun ka ganz mager sinn, och wann hir Produkter geil sinn.

Ganz steil Léierkurve an et ass net trivial opzesetzen. 

Den initialen Setup ass e bëssen e Péng. Et ass et awer voll wäert, an d'Communautéit ënnerstëtzt et gutt genuch, fir datt Dir duerchkënnt.

Schrecklech Docs, awer et gëtt vill Guiden online vu Leit, déi et opgesat hunn, a wann Dir e puer dovunner zesummesetzt, hutt Dir en funktionéierende Setup.

Den initialen Setup huet Gefummel mat hire Helm Charts (vault a consul) gebraucht. Och wann Dir technesch vill aner Back-Ends benotze kënnt, recommandéieren ech et wierklech wierklech net. De Back-End/Consul ka ganz kleng sinn, wann Dir net vill Daten ze späichere hutt.

Maacht Iech definitiv mat der CLI vertraut, well d'GUI méi e Proof-of-Concept-/Reklammportal fir hir Enterprise-Editioun ass.

D'Tatsaach, datt een et net einfach "fëllen" kann, ass e Péng. Zum Beispill wann Dir 5 Felder hutt, musst Dir all Feld manuell fir all Element derbäisetzen. Et ass also net sou, datt Dir Felder fir eng spezifesch Kategorie virdefinéiert a déi Felder fir all Elementer an där Kategorie fëllt, et ass méi wéi "Dir generéiert all Kéier alles", wat (menger Meenung no) e Péng am Aarsch ass.

Dir wëllt vläicht och Goldfish als UI uewen op Vault ukucken. Mécht et zimlech flott, fir Äert Team domat ze begeeschteren. Si hunn och eng Demo. 1. Consul opsetzen. 2. Vault opsetzen, dat op Consul weist. 3. Goldfish opsetzen, dat op Vault weist. 3. E Cron-Job opsetzen, fir Consul-Snapshot fir Backups auszeféieren.



### LastPass

LastPass Teams. Mir benotzen et, huet Custom-Templates, ACL, et fehlt näischt menger Meenung no.

Ech hunn LastPass an menger Organisatioun implementéiert a gi him C+/B-. De gréisste Problem an der leschter Zäit ass e Mangel un Zouverlässegkeet. An de leschte 90 Deeg waren et méi Stonnen, an deenen Vaults an de Offline-Modus gezwongen goufen. Dat ass fir meng Organisatioun net ideal, well ech wuertwiertlech 4.000+ Passwierder iwwer 20+ gedeelte Ordner gespäichert hunn. Wéi Dir Iech virstelle kënnt, gi bei sou vill Passwierder op d'mannst e puer all Dag aktualiséiert oder derbäigesat. Mir hunn e DR-Plang, wann d'Problemer méi wéi eng Stonn oder zwou daueren: e Script ënnerschreift an verschlësselt all Nuecht e CSV-Dump vum Vault, deen a keepass importéiert ka ginn.

LastPass hat onberichte Schluckaufer vu verschlechtertem Service: d'Umeldung 'funktionéiert', zitt awer keng Siten, zoufälleg Funktiounen am Admin-Panel si futti, a Schlësselen ginn net richteg fir nei gedeelt Top-Level-Ordner gedeelt. Ech hunn e spezifesche 'Key Push'-/Backup-Benotzer, deen an all Grupp ass. Normalerweis behieft d'Umeldung als dëse Benotzer all Probleemer mam Schlësseldeele, awer net, wann de Service verschlechtert ass, egal wat d'Statussäit seet...

Fir d'Integratioun kann et einfach sinn, wann Dir ordentlech ACLs mat engem Least-Privilege-Modell hutt, z.B. wann e Benotzer Read & Write a Read Only op engem Eintrag oder Ordner huet, kritt hien nëmmen Read-Only-Rechter. Leider sinn d'ACLs vu menger Organisatioun net déi bescht, dofir hunn ech um Enn d'JSON-Provisioning-API an ~500 Zeile Python benotzt, well d'ofhängeg Natur vun eise Honnerte vun ACLs net gutt op d'Least-Privilege-Modell mappt. Ech hunn um Enn all ACLs gesammelt, an deene e Benotzer war, an eng Aart Ofhängegkeetsduerchlaf gemaach.

Wann Är ACL- oder Gruppestruktur schonn mat enger Least-Privilege-Struktur am Kapp opgebaut ass, funktionéiert den AD/LDAP-Sync-Tool fir Windows gutt.

Wendt Iech u hiert Sales-Team, an si kënnen Iech eng méi laang Enterprise-Test ginn. Stellt sécher, datt Dir seng Limitatioune voll versteet, ier Dir de Schrëtt wagt. Mir haten eng gutt Zuel u Wuesstumsschmerzen, awer ausser Ausfäll oder Beariichtegungen op der Serversäit ass et onheemlech glat gelaf.


### Bitwarden

Bitwarden huet flott Tooling dorëms (WebUI, CLI, Mobil, Desktop). Self-Hosted a zimlech einfach opzesetzen. Zimlech gutt Dokumentatioun an e recommandéiert Tool vu PrivacyTools.


### EnvKey

https://www.envkey.com/ Ass e SaaS. Wierklech einfach ze implementéieren, ze integréieren an ze verwalten.

Funktiounen:

  * Schützt API-Schlësselen an Umeldedaten.

  * Hält d'Konfiguratioun iwwerall synchron.

  * Intelligent, end-to-end verschlësselt Konfiguratioun- a Geheimnisverwaltung. 

  * Verhënnert onsécher Deele a Konfiguratiounswuchs. 

  * An e puer Minutten integréieren.

Fäegkeeten:

  * Verwaltet Konfiguratioun an Zougangsniveauen fir all Är Apps, Ëmfelder a Teams un enger Plaz.

  * Konfiguréiert all Entwécklungs- oder Serverëmfeld mat just enger eenzeger Emgebungsvariabel.

Pros:

  * Gutt Startsäit.

  * Kloer Value Proposition.

  * Visuell exzellent Web-App.

  * Superieur Beispilldaten z.B. Algolia, AWS, Datadog, GitHub, Stripe, asw.

  * 30 Min. mam Grënner iwwer d'Firma, d'UI, asw. geschwat. Dane kléngt gutt informéiert, éierlech iwwer d'Pros/Cons, an e machbare Partner.

  * D'Firma ass am Wesentlechen eng typesch Y-Combinator-Firma, mat 1 Grënner. Huet 120.000 $ am Januar 2018 opgeholl.

  * De Fokus läit drop, op Enterprise-Funktiounen ze kommen, besonnesch vum EnvKey-Cloud-Hosting entweder op On-Prem oder BYOC ze plënneren.

  * Méiglechen Wee no vir, mat EnvKey fir einfach Notzung unzefänken, dann méi spéit (oder parallel) Vault derbäizesetzen. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant ass e Open-Source-Geheimnisverwaltungsservice, dee benotzerfrëndlech Späicherung an Zougang zu Geheimnisser op eng sécher Aart bitt, vun den Entwéckler bei Lyft.

KMS-Authentifikatioun: Confidant léist de Poulet-a-Ee-Problem vun der Authentifikatioun, andeems et AWS KMS an IAM benotzt, fir IAM-Rollen z'erlaben, sécher Authentifikatiounstokens ze generéieren, déi vu Confidant verifizéiert kënne ginn. Confidant verwalt och KMS-Grants fir Är IAM-Rollen, wat den IAM-Rollen erlaabt, Tokens ze generéieren, déi fir d'Service-zu-Service-Authentifikatioun benotzt kënne ginn, oder fir verschlësselt Messagen tëscht Servicer ze schécken.

At-Rest-Verschlësselung vu versionéierte Geheimnisser: Confidant späichert Geheimnisser Append-only an DynamoDB, a generéiert fir all Revisioun vun all Geheimnis e eenzegaartege KMS-Datenschlëssel, mat Fernet symmetrescher authentifizéierter Kryptografie.

Eng benotzerfrëndlech Web-Interface fir d'Verwaltung vu Geheimnisser: Confidant bitt eng AngularJS-Web-Interface, déi et Endbenotzer erlaabt, einfach Geheimnisser, d'Zouuerdnunge vu Geheimnisser zu Servicer an d'Geschicht vun den Ännerungen ze verwalten.


### Devolutions Password Server

https://server.devolutions.net/

Sécher, verwalt an iwwerwaacht Zougang zu privilegiéierte Konten a Sessiounen.

E ëmfaassenden, héich gesécherte Passwuert-Vault, dee Iech erlaabt, den Zougang zu Äre privilegiéierte Konten ze kontrolléieren, a gläichzäiteg d'Gesamt-Netzwierk-Visibilitéit fir Sysadmins verbessert a eng nahtlos Erfahrung fir Endbenotzer bitt.

Funktiounen: zentralen Organisatiouns-Passwuert-Vault, benotzerspezifesche privaten Vault, Passwuertmanager, Credential Injection,
Active-Directory-Integratioun, rollenbaséiert Zougangskontroll, Zwee-Faktor-Authentifikatioun, enterprise-prett, IP-Restriktiounen, Management-Fäegkeeten, automatiséierte Passwuertgenerator, Zougang iwwer mobil App, Passwuert-Geschicht, Zougangsrapporten, E-Mail-Alarmer.

  * ënnerstëtzt Datenverschlësselung

  * ënnerstëtzt verschidde Authentifikatiounsschemaen, dorënner LDAP, O365 a lokal Benotzer MAT Ënnerstëtzung fir MFA vu verschiddene Quellen

  * verschidde Repositories/Vaults mat fein granulare Zougangskontrolle fir verschidde Teams

  * modern Web-UI

  * privat Credential- a Connection-Vaults fir perséinlech Credentials/Verbindungen

  * mobil Apps fir iOS/Android

  * Audit-Logs fir all Eintrag, wien/wat/wéini mat enger optionaler Ufro fir firwat se zougräifen

  * upassbar Templates (och wann se Honnerte vu Verbindungstypen nativ ënnerstëtzen)

  * Tonnen a méi Funktiounen an e Windows-/Mac-Thick-Client (Remote Desktop Manager), mat deem Dir synchroniséiere kënnt, wat d'Optiounen immens erweidert...Een-Klick-Verbindungen

  * de Präis ass net sou schlecht - bis zu 15 Benotzer sinn 500 $ d'Joer fir de Passwuertserver


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Funktioune vun der On-Premise-Versioun: 

  * Total Kontroll iwwer Är End-to-End-Sécherheetssystemer an Infrastruktur

  * Software an Ärem On-Premise-Rechenzenter oder Ärer eegener Virtual-Private-Cloud-Instanz deployen

  * Juristesch a regulatoresch Verflichtunge erfëllen, déi verlaangen, datt all Daten a Systemer on-premise bleiwen

Funktioune vun der Cloud-Versioun:

  * Software-as-a-Service-Modell léisst Iech umellen a direkt unfänken

  * Elastesch Skaléierbarkeet, wéi Dir wuessst

  * Kontrollen a Redundanz vun Azure geliwwert mat 99,9% Uptime-SLA

Benotzer-Feedback:

  * Mir hunn dëst Produkt benotzt. Et gouf esou einfach ëmgaangen an d'Reegele funktionéieren nëmme fir intelligent Leit. Faul oder domm Benotzer kënnen et an engem Teamberäich einfach verbockelen. D'Präisser sinn verhandelbar, wann Dir mat hinne schwätzt.

  * Dir kënnt et mat SQL Express an enger Win-7-Këscht lafen.

  * Bëlleg.
