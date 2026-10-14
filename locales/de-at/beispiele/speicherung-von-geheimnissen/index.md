# Speicherung von Geheimnissen

Inhalt:

* [Zusammenfassung](#zusammenfassung)
  * [Problem](#problem)
  * [Entscheidung](#entscheidung)
  * [Status](#status)
* [Details](#details)
  * [Annahmen](#annahmen)
  * [Einschränkungen](#einschränkungen)
  * [Positionen](#positionen)
  * [Argument](#argument)
  * [Implikationen](#implikationen)
* [Zugehöriges](#zugehöriges)
  * [Zugehörige Entscheidungen](#zugehörige-entscheidungen)
  * [Zugehörige Anforderungen](#zugehörige-anforderungen)
  * [Zugehörige Artefakte](#zugehörige-artefakte)
  * [Zugehörige Prinzipien](#zugehörige-prinzipien)
* [Notizen](#notizen)
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Zusammenfassung


### Problem

Wir müssen Geheimnisse speichern, etwa Passwörter, private Schlüssel, Authentifizierungstoken usw.

Manche Geheimnisse sind benutzerorientiert. Zum Beispiel möchte unser Entwickler mit seinem Mobiltelefon ein Passwort für einen Dienst nachschlagen können.

Manche Geheimnisse sind systemorientiert. Zum Beispiel muss unsere Continuous-Delivery-Pipeline die Zugangsdaten für unser Cloud-Hosting nachschlagen können.


### Entscheidung

Bitwarden für benutzerorientierte Geheimnisse

Vault by HashiCorp für systemorientierte Geheimnisse.


### Status

Entschieden. Wir sind offen für neue Alternativen, sobald sie aufkommen.


## Details


### Annahmen

Für diesen Zweck und unseren aktuellen Stand legen wir Wert auf benutzerorientierten Komfort, etwa brauchbare mobile Apps.

  * Wir möchten schnellen, einfachen Zugriff unterwegs sicherstellen, etwa für einen Entwickler, der Site Reliability Engineering im Bereitschaftsdienst leistet.

  * Wir möchten einige Geheimnisse mit ausgewählten Personen, etwa einem Team, teilen können.

Wir versuchen nicht, für einen einzelnen Anbieter zu lösen, etwa alle Geheimnisse ausschließlich bei Amazon oder Azure oder Google zu speichern.

Wir wollen keine Ad-hoc-Ansätze wie „merk es dir“ oder „schreib es auf einen Zettel“ oder „finde selbst heraus, wie du es speicherst“.

Unser Sicherheitsmodell für diesen Zweck ist damit einverstanden, angesehene COTS-Anbieter zu verwenden, etwa SaaS-Passwortverwaltungswerkzeuge.


### Einschränkungen

Im Moment wollen wir etwas Einfaches, das heißt, ohne Code schreiben zu müssen, ohne Server installieren zu müssen, ohne eine große Verpflichtung einzugehen, ohne alle standardisieren zu müssen.


### Positionen

Wir haben erwogen:

1. Benutzerorientierte Standard-Passwortmanager: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG usw.

2. Systemorientierte COTS-Passwortmanager: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Auf Teilen ausgerichtete Ansätze: ein gemeinsames Google-Dokument, ein gemeinsamer Slack-Kanal, ein gemeinsamer Netzwerkordner usw.

4. Low-Tech-Ad-hoc-Ansätze, etwa Merken, einen Zettel schreiben oder sich darauf verlassen, dass jeder Benutzer seinen eigenen Weg findet.


### Argument

Bitwarden, LastPass, 1Password und Dashlane sind allesamt kommerzielle Standardprodukte.

  * Ähnliche Arten von Funktionen für Benutzer, Teams, Organisationen usw.

  * Desktop-Fähigkeit für Windows und Mac und mobile Fähigkeit für Android und iOS.

  * Browser-Erweiterungen für Chrome und Firefox, für automatisches Ausfüllen von Formularen usw.

Bitwarden hat zwei Vorteile gegenüber den anderen:

  * Bitwarden ist Open Source, das heißt, die Sicherheit kann von Fachleuten überprüft werden, und das Unternehmen wird von sicherheitsorientierten Entwicklern weithin geschätzt.

  * Anekdoten von Softwareleuten beschreiben eine deutliche Präferenz für Bitwarden gegenüber den anderen.

Ein typischer guter Erfahrungsbericht: https://jcs.org/2017/11/17/bitwarden

Eine typische Abstimmungsseite im direkten Vergleich: https://stackshare.io/stackups/bitwarden-vs-dashlane

Wir stellen KeyPass, pass, GPG usw. zurück, weil es zusätzliche Komplexität gibt. Alle sehen aus wie gute Lösungen für technische Benutzer. GPG sieht besonders gut aus für technische Benutzer, die systemübergreifende befehlsorientierte Fähigkeiten wollen.

Wir stellen KMS zurück, weil es die Bindung an einen einzelnen Anbieter (Lock-in) hat.

Wir wählen Vault für systemorientierte Bedürfnisse, weil die Bewertungen erstaunlich positiv sind und weil HashiCorp eine hervorragende Erfolgsbilanz bei erstklassiger Software und Support hat.

Wir legen ein Veto gegen die Ansätze des Teilens ein, etwa über gemeinsame Dokumente, gemeinsame Kanäle, gemeinsame Netzwerkordner usw. Diese bieten nicht die Sicherheitsqualitäten, die wir wollen.

Wir legen ein Veto gegen die Low-Tech-Ad-hoc-Ansätze ein, weil wir uns alle einig sind, dass das kein langfristiger Weg nach vorn ist.


### Implikationen

Entwickler müssen Geheimnisse möglicherweise an zwei Orten verfolgen: Bitwarden für benutzerorientierten Zugriff und Vault für systemorientierten Zugriff.


## Zugehöriges


### Zugehörige Entscheidungen

Die Entscheidung, welcher CI/CD-Server gewählt wird, muss einen Nachweis der Fähigkeit zum Zugriff auf Geheimnisse enthalten.

Wir müssen entscheiden, wie die Geheimnisse verwaltet werden, im Hinblick auf Richtlinien, Rotationen, Organisationen usw.


### Zugehörige Anforderungen

Die Geheimnisse haben zugehörige Anforderungen für Compliance, Auditierung und das Onboarding/Offboarding von Personal.


### Zugehörige Artefakte

Wir erwarten, dass wir einige Geheimnisse in Umgebungsvariablen exportieren könnten.


### Zugehörige Prinzipien

Leicht umkehrbar.

Leicht parallelisierbar, das heißt, es ist einfach, eine Vielzahl von Passwortmanagern zu verwenden.

Billig auszuprobieren, das heißt, es gibt eine kostenlose Testversion und keine Verpflichtung.


## Notizen

Bewertungsnotizen hier. Die Notizen sind allesamt öffentliche Kommentare auf verschiedenen DevOps-Diskussionsforen.


### Vault by HashiCorp

Vault ist genau das, was Sie hier wollen. 

Werfen Sie Vault aber nicht einfach in die Produktion, bauen Sie es zuerst in einer Testumgebung auf, weil die Dokumentation von HashiCorp ziemlich mangelhaft sein kann, auch wenn ihre Produkte großartig sind.

Sehr steile Lernkurve, und es ist nicht trivial aufzusetzen. 

Die Ersteinrichtung ist etwas mühsam. Sie lohnt sich aber, und die Community wird sie gut genug unterstützen, dass Sie zurechtkommen.

Schreckliche Dokumentation, aber es gibt viele Anleitungen online von Leuten, die es eingerichtet haben, und wenn Sie ein paar davon kombinieren, haben Sie eine funktionierende Einrichtung.

Die Ersteinrichtung erforderte Herumbasteln an ihren Helm-Charts (vault und consul). Technisch kann man viele andere Backends verwenden, aber ich rate wirklich, wirklich davon ab. Das Backend/consul kann winzig klein sein, wenn man nicht viele Daten zu speichern hat.

Machen Sie sich unbedingt mit der CLI vertraut, denn die GUI ist eher ein Proof-of-Concept/Werbeportal für ihre Enterprise-Edition.

Die Tatsache, dass man es nicht einfach „befüllen“ kann, ist mühsam. Wenn man zum Beispiel 5 Felder hat, muss man für jedes Element jedes Feld manuell hinzufügen. Es ist also nicht so, dass man Felder für eine bestimmte Kategorie vordefiniert und diese Felder für alle Elemente dieser Kategorie ausfüllt, sondern eher „man erzeugt jedes Mal alles“, was (meiner Meinung nach) eine Zumutung ist.

Sie sollten sich vielleicht auch goldfish als UI auf vault ansehen. Es macht es ziemlich angenehm, Ihr Team dafür zu gewinnen. Sie haben auch eine Demo. 1. consul einrichten. 2. vault einrichten, das auf consul zeigt. 3. goldfish einrichten, das auf vault zeigt. 3. Einen Cron-Job einrichten, der consul snapshot für Sicherungen ausführt.



### LastPass

LastPass Teams. Wir nutzen es, hat benutzerdefinierte Vorlagen, ACLs, meiner Meinung nach fehlt nichts.

Ich habe LastPass in meiner Organisation eingeführt und gebe ihm ein C+/B-. Das größte Problem ist in letzter Zeit mangelnde Zuverlässigkeit. In den vergangenen 90 Tagen gab es mehrere Stunden, in denen Tresore in den Offline-Modus gezwungen wurden. Das ist für meine Organisation nicht ideal, weil wir buchstäblich 4.000+ Passwörter in 20+ gemeinsamen Ordnern gespeichert haben. Wie Sie sich vorstellen können, werden bei so vielen Passwörtern täglich mindestens einige aktualisiert oder hinzugefügt. Wir haben einen DR-Plan, falls Probleme länger als ein bis zwei Stunden andauern: Ein Skript signiert und verschlüsselt jede Nacht einen CSV-Dump des Tresors, der in keepass importiert werden kann.

LastPass hatte nicht gemeldete kurze Aussetzer bei der Dienstqualität: Die Anmeldung „funktioniert“, lädt aber keine Seiten, zufällige Funktionen im Admin-Bereich sind kaputt, und Schlüssel für neue gemeinsame Ordner der obersten Ebene werden nicht richtig geteilt. Ich habe einen speziellen „Key-Push“-/Backup-Benutzer, der in jeder Gruppe ist. Normalerweise behebt die Anmeldung als dieser Benutzer alle Probleme beim Schlüsselteilen, aber nicht, wenn der Dienst beeinträchtigt ist, egal was die Statusseite sagt...

Für die Integration kann es einfach sein, wenn Sie passende ACLs mit einem Modell der geringsten Rechte haben, z. B. wenn ein Benutzer sowohl Lesen & Schreiben als auch nur Lesen für einen Eintrag oder Ordner hat, erhält er nur Leseberechtigungen. Leider sind die ACLs meiner Organisation nicht die besten, daher habe ich am Ende die JSON-Provisionierungs-API und ~500 Zeilen Python verwendet, weil sich die abhängige Natur unserer Hunderte von ACLs nicht gut auf das Modell der geringsten Rechte abbilden ließ. Am Ende habe ich alle ACLs eines Benutzers abgerufen und eine Art Abhängigkeitsdurchlauf gemacht.

Wenn Ihre ACL- oder Gruppenstruktur bereits mit einer Struktur der geringsten Rechte im Hinterkopf aufgebaut ist, wird das AD/LDAP-Synchronisierungswerkzeug für Windows gut funktionieren.

Wenden Sie sich an das Vertriebsteam, dann kann man Ihnen eine längere Enterprise-Testversion verschaffen. Stellen Sie sicher, dass Sie die Einschränkungen vollständig verstehen, bevor Sie sich entscheiden. Wir hatten ziemlich viele Wachstumsschmerzen, aber abgesehen von Ausfällen oder Beeinträchtigungen auf Serverseite lief es unglaublich reibungslos.


### Bitwarden

Bitwarden hat gute Werkzeuge drumherum (WebUI, CLI, Mobil, Desktop). Selbst hostbar und ziemlich einfach einzurichten. Recht gute Dokumentation und ein von PrivacyTools empfohlenes Werkzeug.


### EnvKey

https://www.envkey.com/ ist ein SaaS. Wirklich einfach zu implementieren, zu integrieren und zu verwalten.

Funktionen:

  * API-Schlüssel und Zugangsdaten schützen.

  * Konfiguration überall synchron halten.

  * Intelligente, Ende-zu-Ende-verschlüsselte Verwaltung von Konfiguration und Geheimnissen. 

  * Unsicheres Teilen und Konfigurations-Wildwuchs verhindern. 

  * In Minuten integrieren.

Fähigkeiten:

  * Konfiguration und Zugriffsebenen für alle Ihre Apps, Umgebungen und Teams an einem Ort verwalten.

  * Jede Entwicklungs- oder Serverumgebung mit nur einer einzigen Umgebungsvariablen konfigurieren.

Pluspunkte:

  * Gute Startseite.

  * Klares Wertversprechen.

  * Optisch hervorragende Web-App.

  * Überlegene Beispieldaten, z. B. Algolia, AWS, Datadog, GitHub, Stripe usw.

  * Habe 30 Minuten mit dem Gründer über das Unternehmen, die UI usw. gesprochen. Dane klingt gut informiert, ehrlich in Bezug auf Vor-/Nachteile und wie ein tragfähiger Partner.

  * Das Unternehmen ist im Wesentlichen ein typisches Y-Combinator-Unternehmen mit 1 Gründer. Hat 2018-01 $120K eingesammelt.

  * Der Fokus liegt darauf, zu Enterprise-Funktionen zu gelangen, besonders vom EnvKey-Cloud-Hosting zu On-Prem oder BYOC zu wechseln.

  * Möglicher Weg nach vorn: mit EnvKey wegen der Benutzerfreundlichkeit beginnen, dann später (oder parallel) Vault hinzufügen. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant ist ein Open-Source-Dienst zur Verwaltung von Geheimnissen, der von den Entwicklern bei Lyft stammt und eine benutzerfreundliche Speicherung und einen benutzerfreundlichen Zugriff auf Geheimnisse auf sichere Weise bietet.

KMS-Authentifizierung: Confidant löst das „Henne-Ei“-Problem der Authentifizierung, indem es AWS KMS und IAM nutzt, damit IAM-Rollen sichere Authentifizierungstoken erzeugen können, die Confidant überprüfen kann. Confidant verwaltet außerdem KMS-Grants für Ihre IAM-Rollen, wodurch die IAM-Rollen Token erzeugen können, die für die Dienst-zu-Dienst-Authentifizierung oder zum Übermitteln verschlüsselter Nachrichten zwischen Diensten verwendet werden können.

Verschlüsselung versionierter Geheimnisse im Ruhezustand: Confidant speichert Geheimnisse in DynamoDB nur anfügend (append-only) und erzeugt für jede Revision jedes Geheimnisses einen eindeutigen KMS-Datenschlüssel, unter Verwendung der symmetrischen authentifizierten Kryptografie Fernet.

Eine benutzerfreundliche Weboberfläche zur Verwaltung von Geheimnissen: Confidant bietet eine AngularJS-Weboberfläche, mit der Endbenutzer Geheimnisse, die Zuordnungen von Geheimnissen zu Diensten und den Änderungsverlauf leicht verwalten können.


### Devolutions Password Server

https://server.devolutions.net/

Zugriff auf privilegierte Konten und Sitzungen sichern, verwalten und überwachen.

Ein umfassender, hochgesicherter Passworttresor, mit dem Sie den Zugriff auf Ihre privilegierten Konten kontrollieren und zugleich die Gesamtsichtbarkeit des Netzwerks für Systemadministratoren verbessern und Endbenutzern ein nahtloses Erlebnis bieten können.

Funktionen: zentraler Organisations-Passworttresor, benutzerspezifischer privater Tresor, Passwortmanager, Einschleusen von Zugangsdaten,
Active-Directory-Integration, rollenbasierte Zugriffskontrolle, Zwei-Faktor-Authentifizierung, unternehmenstauglich, IP-Beschränkungen, Verwaltungsfähigkeiten, automatischer Passwortgenerator, Zugriff per mobiler App, Passwortverlauf, Zugriffsberichte, E-Mail-Warnungen.

  * unterstützt Datenverschlüsselung

  * unterstützt mehrere Authentifizierungsschemata, einschließlich LDAP, O365 und lokaler Benutzer MIT Unterstützung für MFA aus mehreren Quellen

  * mehrere Repositories/Tresore mit fein abgestuften Zugriffskontrollen für mehrere Teams

  * moderne Web-UI

  * private Zugangsdaten- und Verbindungstresore für persönliche Zugangsdaten/Verbindungen

  * mobile Apps für iOS/Android

  * Audit-Protokolle für jeden Eintrag, wer/was/wann, mit einer optionalen Abfrage, warum zugegriffen wird

  * anpassbare Vorlagen (obwohl sie Hunderte von Verbindungstypen nativ unterstützen)

  * Unmengen weiterer Funktionen und ein Windows/Mac-Thick-Client (Remote Desktop Manager), mit dem man sich synchronisieren kann und der die Optionen stark erweitert... Ein-Klick-Verbindungen

  * Der Preis ist gar nicht so schlecht – bis zu 15 Benutzer kosten $500 pro Jahr für den Passwortserver


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Funktionen der On-Premise-Version: 

  * Vollständige Kontrolle über Ihre Ende-zu-Ende-Sicherheitssysteme und -Infrastruktur

  * Software in Ihrem On-Premise-Rechenzentrum oder in Ihrer eigenen Virtual-Private-Cloud-Instanz bereitstellen

  * Rechtliche und regulatorische Verpflichtungen erfüllen, die verlangen, dass alle Daten und Systeme On-Premise liegen

Funktionen der Cloud-Version:

  * Das Software-as-a-Service-Modell erlaubt Ihnen, sich anzumelden und sofort loszulegen

  * Elastische Skalierbarkeit, wenn Sie wachsen

  * Kontrollen und Redundanz, bereitgestellt von Azure mit 99,9 % Verfügbarkeits-SLA

Benutzerfeedback:

  * Wir haben dieses Produkt früher verwendet. Es war so leicht zu umgehen, und die Regeln funktionieren nur bei klugen Leuten. Faule oder dumme Benutzer können es in einem Teambereich leicht ruinieren. Die Preise sind verhandelbar, wenn man mit ihnen spricht.

  * Man kann es mit SQL Express und einem Win-7-Rechner betreiben. 

  * Billig.
