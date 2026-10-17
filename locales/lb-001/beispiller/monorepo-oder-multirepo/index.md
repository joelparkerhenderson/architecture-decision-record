# Monorepo oder Multirepo

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


## Zesummefaassung


### Problem

Eise Projet beinhalt d'Entwécklung vun dräi Haaptkategorien u Software:

  * Front-End-GUIen
  * Middleware-Servicer
  * Back-End-Server

Wa mir entwéckelen, ass eist Quellcode-Management-(SCM)-Versiounskontrollsystem (VCS) Git.

Mir mussen entscheeden, wéi mir Git benotzen, fir eise Code ze organiséieren.

Déi Top-Level-Wiel ass, als "Monorepo" oder "Polyrepo" oder "Hybrid" ze organiséieren:

  * Monorepo bedeit, mir setzen all Deeler an ee groussen Repo
  * Polyrepo bedeit, mir setzen all Deel a säin eegene Repo
  * Hybrid bedeit eng Mëschung aus Monorepo a Polyrepo

Fir méi kuckt w.e.g. https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Decisioun

Monorepo, wann eng Organisatioun/e Team/e Projet relativ kleng ass, a séier Iteratioun eng méi héich Prioritéit huet wéi d'Erhale vun der Stabilitéit.

Polyrepo, wann eng Organisatioun/e Team/e Projet relativ grouss ass, an d'Erhale vun der Stabilitéit eng méi héich Prioritéit huet wéi séier Iteratioun.


### Zoustand

Decidéiert. Oppe fir eng nei Iwwerleeung, wann/wa neit Tooling fir d'Verwalte vu Monorepos an/oder Polyrepos verfügbar gëtt.


## Detailer


### Viraussetzungen

All de Code, deen mir entwéckelen, ass fir d'Offere vun enger Organisatioun, an net fir d'allgemeng Ëffentlechkeet. Dat heescht, de Broker-Dealer zielt net drop of, eppes wéi fräiwëlleg Entwéckler aus der allgemenger Ëffentlechkeet ze hunn.


### Restriktiounen

D'Restriktioune si gutt dokumentéiert op https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Positiounen

Mir hu Monorepos am Stil vu Google, Facebook, asw. iwwerluecht. Mir mengen, datt all Monorepo-Skaléierungsprobleem esou wäit an der Zukunft läit, datt mir déi selwecht Praktike wéi Google a Facebook notze kënnen, bis mir se brauchen.

Mir hu Polyrepos am Stil vun typesche Git-Open-Source-Projeten iwwerluecht, wéi Google Android, Facebook React, asw. Mir mengen, datt dës déi bescht Wiel fir d'Participatioun vun der allgemenger Ëffentlechkeet (z.B. jiddereen op der Welt ka um Code schaffen) an individuell Verfügbarkeet sinn (z.B. de Projet gëtt eleng benotzt, ouni aner Deeler).


### Argument

Wann eng Organisatioun/e Team/e Projet relativ kleng ass, wielen mir Monorepo, well séier Iteratioun däitlech méi héich an der Prioritéit ass wéi d'Erhale vun der Stabilitéit

Wann eng Organisatioun/e Team/e Projet relativ grouss ass, wielen mir Polyrepo, well d'Erhale vun der Stabilitéit däitlech méi héich an der Prioritéit ass wéi séier Iteratioun.


### Implikatiounen

Wann et eng bestoend Pipeline fir CI+CD gëtt, da mussen mir se eventuell upassen, fir verschidde Projeten an engem Repo ze testen.

CI+CD kéint méi Zäit fir e komplette Build vun engem Monorepo brauchen, well CI+CD all Projete am Monorepo kéint bauen.

Wann eng Organisatioun/e Team/e Projet wiisst, da wäert e Monorepo Skaléierungsproblemer hunn.

Monorepo-Skaléierungsproblemer kënnen et ëmmer méi wäertvoll maachen, op e Polyrepo ëmzewiesselen.

D'Ëmstellung vu Monorepo op Polyrepo ass eng bedeitend Devops-Aufgab a muss geplangt, verwalt a programméiert ginn.


## Verwandt


### Verwandt Decisiounen

Mir erstellen Decisiounen fir verwandt Tooling, fir Monorepos (z.B. Google Bazel) a Polyrepos (z.B. Lyft Refactorator) ze verwalten.


### Verwandt Ufuerderungen

Mir mussen d'CI+CD-Pipeline entwéckelen, sou datt se gutt mat Git funktionéiert.


### Verwandt Artefakten

Mir erwaarden, datt d'Repo-Organisatioun verwandt Artefakten fir Provisioning, Konfiguratiounsmanagement, Testen an ähnlech Devops-Beräicher huet. 


### Verwandt Prinzipien

Einfach réckgängeg ze maachen. Wann de Monorepo a Praxis net funktionéiert, oder net vun der Féierung gewënscht ass, ass et einfach, op Polyrepo ze wiesselen.

Clientenobsessioun. Mir schätzen et, de Projet an d'Hänn vun de Clienten ze kréien, a mir gleewen, datt e Monorepo eis méi séier dohinner bréngt wéi e Polyrepo, a eis och hëlleft, méi séier ze iteréieren.

Denkt grouss. Google a Facebook si ganz staark Befürworter vu Monorepos géintiwwer Polyrepos, well all Kärofferen zesumme kënne entwéckelt/getest/deployt ginn.


## Notizen

Füügt hei all Notizen derbäi.
