# AWS-Prozess fir Architektur-Decisiounsopzeechnungen

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Eng Architektur-Decisiounsopzeechnung (ADR) ass en Dokument, dat eng Wiel beschreift, déi d'Team iwwer e wesentlechen Aspekt vun der Softwarearchitektur mécht, déi et plangt ze bauen. All ADR beschreift d'Architekturdecisioun, hire Kontext an hir Konsequenzen. ADR hunn Zoustänn a verfollegen dofir e Lifecycle. Fir e Beispill fir en ADR, kuckt den Annex.

Den ADR-Prozess produzéiert eng Sammlung vun Architektur-Decisiounsopzeechnungen. Dës Sammlung bildet de Decisiounsprotokoll. De Decisiounsprotokoll liwwert de Projetskontext souwéi detailléiert Ëmsetzungs- an Designinformatioun. Projetsmemberen iwwerfléie d'Iwwerschrëfte vun all ADR, fir en Iwwerbléck iwwer de Projetskontext ze kréien. Si liesen d'ADR, fir déif an d'Projetsëmsetzungen an d'Designwalen anzedauchen.

Wann d'Team en ADR akzeptéiert, gëtt en onverännerbar. Wann nei Erkenntnisser eng aner Decisioun erfuerderen, schléit d'Team en neien ADR vir. Wann d'Team den neien ADR akzeptéiert, ersetzt en de fréiere ADR.

## Ëmfang vum ADR-Prozess

Projetsmemberen sollen en ADR fir all architekturrelevant Decisioun erstellen, déi dat Softwareprojet oder -produkt beaflosst, dorënner déi folgend (Richards a Ford 2020):

* Struktur (zum Beispill Muster wéi Microservices)

* Net-funktionell Ufuerderungen (Sécherheet, Héichverfügbarkeet a Feelertoleranz)

* Ofhängegkeeten (Kopplung vu Komponenten)

* Schnëttstellen (APIen a publizéiert Kontrakter)

* Konstruktiounstechniken (Bibliothéiken, Frameworks, Tools a Prozesser)

* Funktionell an net-funktionell Ufuerderunge sinn déi heefegst Inputs fir den ADR-Prozess.


## ADR-Inhalt

Wann d'Team e Besoin fir en ADR identifizéiert, fänkt e Teammember un, den ADR op Basis vun engem projetsweite Virlag ze schreiwen. (Kuckt d'ADR-GitHub-Organisatioun fir Beispillvirlagen.) De Virlag vereinfacht d'Erstelle vum ADR a stellt sécher, datt den ADR all relevant Informatioun erfaasst. Op d'mannst soll all ADR de Kontext vun der Decisioun, d'Decisioun selwer an d'Konsequenze vun der Decisioun fir de Projet a seng Liwwerergebnisser definéieren. (Fir Beispiller vun dëse Rubriken, kuckt den Annex.) Ee vun de mächtegsten Aspekter vun der ADR-Struktur ass, datt se sech op de Grond fir d'Decisioun konzentréiert a net drop, wéi d'Team se ëmgesat huet. Wann ee versteet, firwat d'Team d'Decisioun getroffen huet, ass et méi einfach fir aner Teammemberen, d'Decisioun unzehuelen, an anere Architekten, déi net um Decisiounsprozess bedeelegt waren, gëtt et verhënnert, dës Decisioun an Zukunft ze iwwerstëmmen.


## ADR-Adoptiounsprozess

All Teammember kann en ADR erstellen, awer d'Team soll eng Definitioun vun Ownership fir en ADR festleeën. All Auteur, deen den Owner vun engem ADR ass, soll den ADR-Inhalt aktiv erhalen a kommunizéieren. Fir dës Ownership ze klären, bezitt dës Guide sech an de folgende Rubriken op ADR-Auteuren als ADR-Owner. Aner Teammemberen kënnen ëmmer zu engem ADR bäidroen. Wann sech den Inhalt vun engem ADR ännert, ier d'Team den ADR akzeptéiert, soll den Owner dës Ännerunge genehmegen.

Nodeem d'Team eng Architekturdecisioun a säin Owner identifizéiert huet, stellt den ADR-Owner den ADR um Ufank vum Prozess am Zoustand **Proposed** (Virgeschloen) zur Verfügung. ADR am Zoustand Proposed si prett fir d'Review.

Den ADR-Owner start dann de Review-Prozess fir den ADR. D'Zil vum ADR-Review-Prozess ass et, ze entscheeden, ob d'Team den ADR akzeptéiert, feststellt, datt e Nobesserung brauch, oder den ADR ofleent. D'Projetsteam, dorënner den Owner, iwwerpréift den ADR. D'Review-Meeting soll mat engem dedizéierte Zäitfënster ufänken, fir den ADR ze liesen. Am Duerchschnëtt sollen 10 bis 15 Minutte genuch sinn. An dëser Zäit liest all Teammember dat Dokument a füügt Kommentarer a Froen derbäi, fir onkloer Themen ze markéieren. No der Review-Phas liest den ADR-Owner all Kommentar vir a diskutéiert en mam Team.

Wann d'Team Aktiounspunkte fënnt, fir den ADR ze verbesseren, bleift den Zoustand vum ADR **Proposed**. Den ADR-Owner formuléiert d'Aktiounen a füügt, a Zesummenaarbecht mam Team, all Aktioun een Zoustännegen derbäi. All Teammember kann zu den Aktiounspunkten bäidroen a se léisen. Et ass d'Responsabilitéit vum ADR-Owner, de Review-Prozess nei ze plangen.

D'Team kann och décidéieren, den ADR ofzeleenen. An dësem Fall füügt den ADR-Owner e Grond fir d'Oflehnung derbäi, fir zukünfteg Diskussiounen iwwer dat selwecht Thema ze verhënneren. Den Owner ännert den ADR-Zoustand op **Rejected** (Offgelehnt).

Wann d'Team den ADR genehmegt, füügt den Owner en Zäitstempel, eng Versioun an eng Lëscht vu Stakeholder derbäi. Den Owner aktualiséiert dann den Zoustand op **Accepted** (Akzeptéiert).

ADR an de Decisiounsprotokoll, deen si erstellen, representéieren Decisiounen, déi d'Team getroffen huet, a bidden eng Geschicht vun alle Decisiounen. D'Team benotzt d'ADR, wou méiglech, als Referenz wärend Code- an Architektur-Reviews. Zousätzlech zu Code-Reviews, Design-Aufgaben an Ëmsetzungsaufgabe sollen d'Teammemberen d'ADR fir strategesch Decisioune fir d'Produkt consultéieren.

Als gutt Praxis soll all Softwareännerung duerch Peer-Reviews goen an op d'mannst eng Genehmegung erfuerderen. Wärend der Code-Review kann e Code-Reviewer Ännerungen entdecken, déi géint ee oder méi ADR verstoussen. An dësem Fall freet de Reviewer den Auteur vun der Codeännerung, de Code ze aktualiséieren, an deelt e Link zum ADR. Wann den Auteur de Code aktualiséiert, gëtt en vun de Peer-Reviewer genehmegt an an d'Haapt-Codebasis gemergt.


## ADR-Review-Prozess

D'Team soll ADR als onverännerbar Dokumenter behandelen, nodeems d'Team se akzeptéiert oder oflehnt. Ännerunge vun engem bestoenden ADR erfuerderen, en neien ADR ze erstellen, e Review-Prozess fir den neien ADR opzeriichten an den ADR ze genehmegen. Wann d'Team den neien ADR genehmegt, soll den Owner den Zoustand vum aalen ADR op **Superseded** (Ersat) änneren.
