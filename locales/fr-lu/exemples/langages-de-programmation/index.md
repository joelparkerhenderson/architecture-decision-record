# Langages de programmation

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


## Résumé


### Question

Nous devons choisir des langages de programmation pour notre logiciel. Nous avons deux besoins majeurs : un langage de programmation front-end adapté aux applications web et un langage de programmation back-end adapté aux applications serveur.


### Décision

Nous choisissons TypeScript pour le front-end.

Nous choisissons Rust pour le back-end.


### État

Décidé. Nous sommes ouverts à de nouvelles alternatives au fur et à mesure de leur apparition.


## Détails


### Hypothèses

Les applications front-end sont typiques :

  * Utilisateurs et interactions typiques

  * Navigateurs et systèmes typiques

  * Développements et déploiements typiques

Les applications front-end sont susceptibles d’évoluer rapidement :

  * Nous voulons garantir des développements, déploiements, itérations, etc. rapides et faciles.

  * Nous accordons de la valeur à la démontrabilité, comme la sûreté de typage, et nous acceptons de fournir un peu plus de travail pour l’obtenir.

  * Nous n’avons pas besoin de compatibilité avec les systèmes hérités.

Les applications back-end sont plus exigeantes que la moyenne :

  * Objectifs de qualité supérieurs à la moyenne, en particulier la démontrabilité, la fiabilité, la sécurité, etc.

  * Objectifs de quasi-temps réel supérieurs à la moyenne, c’est-à-dire que nous ne voulons pas de pauses dues au ramasse-miettes de la machine virtuelle.

  * Objectifs de programmation fonctionnelle supérieurs à la moyenne, en particulier pour la parallélisation, le traitement multicœur et la sécurité mémoire.

Nous acceptons des vitesses de compilation plus faibles en faveur de la sûreté à la compilation et de la vitesse d’exécution.


### Contraintes

Nous avons une forte contrainte sur les langages utilisables avec les services de fonctions des principaux fournisseurs cloud, tels qu’Amazon Lambda.


### Positions

Nous avons envisagé ces langages :

  * C

  * C++

  * Clojure
  
  * Elixir
  
  * Erlang
  
  * Elm
  
  * Flow
  
  * Go
  
  * Haskell
  
  * Java
  
  * JavaScript
  
  * Kotlin
  
  * Python
  
  * Ruby
  
  * Rust
  
  * TypeScript



### Argument

Résumé par langage :

  * C : rejeté en raison de sa faible sûreté ; Rust peut faire presque tout mieux.

  * C++ : rejeté parce que c’est un fouillis ; Rust peut faire presque tout mieux.

  * Clojure : excellente modélisation ; meilleure approximation de Lisp ; excellent environnement d’exécution sur la JVM.
  
  * Elixir : excellent environnement d’exécution, y compris pour la facilité de déploiement et la concurrence ; excellente expérience développeur ; écosystème relativement petit.

  * Erlang : excellent environnement d’exécution, y compris pour la facilité de déploiement et la concurrence ; expérience développeur exigeante ; écosystème relativement petit.

  * Elm : semble très prometteur ; IBM publie des études de cas majeures aux bons résultats ; écosystème plus petit.

  * Flow : amélioration intéressante par rapport à JavaScript ; cependant, les développeurs s’en détournent.

  * Go : excellente expérience développeur ; excellente concurrence ; mais un historique de mauvaises décisions qui handicapent le langage.

  * Haskell : le meilleur langage fonctionnel ; communauté de développeurs plus petite ; n’a pas obtenu assez de succès publiés en production.

  * Java : excellent environnement d’exécution ; excellent écosystème ; expérience développeur médiocre.

  * JavaScript : le langage le plus populaire de tous les temps ; l’écosystème le plus répandu.

  * Kotlin : corrige une grande partie de Java ; excellent soutien de JetBrains ; bons cas publiés de portage de Java vers Kotlin.
  
  * Python : le langage le plus populaire pour l’administration système ; excellents outils d’analyse ; bons frameworks web ; mais abandonné par Google au profit de Go.

  * Ruby : la meilleure expérience développeur qui soit ; les meilleurs frameworks web ; la communauté la plus sympathique ; mais très lent ; un peu difficile à empaqueter.

  * Rust : le meilleur nouveau langage ; accent sur zéro abstraction ; accent sur la concurrence ; cependant écosystème relativement petit ; et il impose des limites délibérées à certains types d’accélérations du compilateur, p. ex. l’accès direct à la mémoire doit être explicitement non sûr (unsafe).

  * TypeScript : ajoute des types à JavaScript ; excellent transpileur ; accent croissant des développeurs sur le portage de JavaScript vers TypeScript ; solide soutien de Microsoft.

Nous avons décidé que les machines virtuelles comportent un ensemble de compromis dont nous n’avons pas besoin pour l’instant, comme une complexité supplémentaire qui fournit des capacités d’exécution.

Nous pensons que notre décision centrale est guidée par deux préoccupations transversales :

  * Pour la vitesse d’exécution maximale et l’accès système le plus étroit, nous choisirions JavaScript et C.

  * Pour une vitesse d’exécution proche du maximum et un accès système proche du plus étroit, nous choisissons TypeScript et Rust.

Mentions honorables aux langages à machine virtuelle et aux frameworks web que nous choisirions si nous voulions un langage à machine virtuelle :

  * Clojure et Luminus

  * Java et Spring

  * Elixir et Phoenix


### Implications

Les développeurs front-end devront apprendre TypeScript. C’est probablement une courbe d’apprentissage facile si l’expérience principale du développeur est l’utilisation de JavaScript.

Les développeurs back-end devront apprendre Rust. C’est probablement une courbe d’apprentissage modérée si l’expérience principale du développeur est l’utilisation de C/C++, et une courbe d’apprentissage difficile si son expérience principale est l’utilisation de Java, Python, Ruby ou de langages similaires à gestion automatique de la mémoire. 

TypeScript et Rust sont tous deux relativement récents. Cela signifie que de nombreux outils n’ont pas encore de documentation pour ces langages. Par exemple, la chaîne devops devra être configurée pour ces langages, et jusqu’à présent, aucun des outils devops que nous évaluons n’a d’exemples par défaut pour eux.

Les temps de compilation de TypeScript et de Rust sont assez lents. Une partie de cela peut être due à la nouveauté des langages. Nous voudrons peut-être examiner comment atténuer les temps de compilation lents, par exemple par la compilation à la demande, la compilation concurrente, etc.

La prise en charge de ces langages par les IDE n’est pas encore omniprésente ni de premier ordre. Par exemple, JetBrains vend l’IDE PyCharm avec une prise en charge de premier ordre de Python, mais ne vend pas d’IDE avec une prise en charge de premier ordre de Rust ; à la place, JetBrains peut utiliser un plugin Rust qui fournit peut-être 80 % de la prise en charge du langage Rust par rapport à la prise en charge du langage Python.


## Connexe


### Décisions connexes

Nous viserons des choix d’écosystème alignés sur ces langages.

Par exemple, nous voulons choisir un IDE doté de bonnes capacités pour ces langages.

Par exemple, pour notre framework web front-end, nous sommes plus susceptibles de décider d’un framework qui tend vers TypeScript (p. ex. Vue) que d’un framework qui tend vers du JavaScript simple (p. ex. React).


### Exigences connexes

Toute notre chaîne d’outils doit prendre en charge ces langages.


### Artefacts connexes

Nous nous attendons à pouvoir exporter certains secrets vers des variables d’environnement.


### Principes connexes

Mesurer deux fois, construire une fois. Nous donnons la priorité à une certaine sûreté sur une certaine vitesse.

L’exécution est plus précieuse que la compilation. Nous donnons la priorité à l’usage par les clients sur l’usage par les développeurs.


## Notes

Toute note ici.
