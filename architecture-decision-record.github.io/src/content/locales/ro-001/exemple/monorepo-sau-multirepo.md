# Monorepo sau multirepo

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


## Rezumat


### Problemă

Proiectul nostru implică dezvoltarea a trei categorii majore de software:

  * Interfețe grafice front-end
  * Servicii middleware
  * Servere back-end

Când dezvoltăm, sistemul nostru de control al versiunilor (VCS) pentru gestionarea codului sursă (SCM) este git.

Trebuie să alegem cum folosim git pentru a ne organiza codul.

Alegerea de la nivelul cel mai înalt este organizarea ca „monorepo”, „polyrepo” sau „hibrid”:

  * Monorepo înseamnă că punem toate componentele într-un singur depozit mare
  * Polyrepo înseamnă că punem fiecare componentă în propriul depozit
  * Hibrid înseamnă un amestec de monorepo și polyrepo

Pentru mai multe informații, vezi https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Decizie

Monorepo atunci când o organizație/echipă/un proiect este relativ mic(ă), iar iterarea rapidă are prioritate mai mare decât menținerea stabilității.

Polyrepo atunci când o organizație/echipă/un proiect este relativ mare, iar menținerea stabilității are prioritate mai mare decât iterarea rapidă.


### Stare

Decis. Suntem deschiși să revenim dacă/atunci când apar instrumente noi pentru gestionarea monorepo-urilor și/sau polyrepo-urilor.


## Detalii


### Ipoteze

Tot codul pe care îl dezvoltăm este pentru ofertele unei singure organizații, nu pentru publicul larg. Adică firma de brokeraj nu urmărește să aibă ceva de genul unor dezvoltatori voluntari din publicul larg.


### Constrângeri

Constrângerile sunt bine documentate la https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Poziții

Am luat în considerare monorepo-uri în stilul Google, Facebook etc. Credem că orice probleme de scalare ale monorepo-urilor sunt atât de departe în viitor încât, până când vom avea nevoie de ele, vom putea valorifica aceleași practici ca Google și Facebook.

Am luat în considerare polyrepo-uri în stilul proiectelor open source Git tipice, precum Google Android, Facebook React etc. Credem că acestea sunt cea mai bună alegere pentru participarea publicului larg (de exemplu, oricine din lume poate lucra la cod) și pentru disponibilitate individuală (de exemplu, proiectul este folosit de sine stătător, fără alte componente).


### Argument

Când o organizație/echipă/un proiect este relativ mic(ă), alegem monorepo, deoarece iterarea rapidă are o prioritate semnificativ mai mare decât menținerea stabilității

Când o organizație/echipă/un proiect este relativ mare, alegem polyrepo, deoarece menținerea stabilității are o prioritate semnificativ mai mare decât iterarea rapidă.


### Implicații

Dacă există un flux CI+CD, poate fi nevoie să-l ajustăm pentru testarea mai multor proiecte într-un singur depozit.

CI+CD ar putea dura mai mult pentru un build complet al unui monorepo, deoarece CI+CD ar putea construi toate proiectele din monorepo.

Dacă organizația/echipa/proiectul crește, un monorepo va avea probleme de scalare.

Problemele de scalare ale monorepo-ului pot face din ce în ce mai valoroasă tranziția la un polyrepo.

Tranziția de la monorepo la polyrepo este o sarcină devops semnificativă și va trebui planificată, gestionată și programată.


## Conexe


### Decizii conexe

Vom crea decizii pentru instrumentele conexe de gestionare a monorepo-urilor (de exemplu Google Bazel) și a polyrepo-urilor (de exemplu Lyft Refactorator).


### Cerințe conexe

Trebuie să dezvoltăm fluxul CI+CD astfel încât să funcționeze bine cu git.


### Artefacte conexe

Ne așteptăm ca organizarea depozitelor să aibă artefacte conexe pentru aprovizionare, gestionarea configurației, testare și domenii devops similare. 


### Principii conexe

Ușor reversibil. Dacă monorepo nu funcționează în practică sau nu este dorit de conducere, este simplu să se treacă la polyrepo.

Obsesia pentru client. Prețuim punerea proiectului în mâinile clienților și credem că un monorepo ne poate duce acolo mai repede decât un polyrepo și ne poate ajuta, de asemenea, să iterăm mai repede.

Gândește în mare. Google și Facebook sunt susținători foarte puternici ai monorepo-urilor în fața polyrepo-urilor, deoarece toate ofertele de bază pot fi dezvoltate/testate/implementate în concert.


## Note

Adaugă aici orice note.
