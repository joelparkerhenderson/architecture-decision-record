# Format d’horodatage

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

Nous voulons pouvoir suivre le moment où les choses se produisent en utilisant des horodatages et un format d’horodatage cohérent qui fonctionne bien dans l’ensemble de nos systèmes et des systèmes tiers.

Nous interagissons avec des systèmes dont les formats d’horodatage diffèrent :

* Les messages JSON n’ont pas de format d’horodatage natif ; nous devons donc choisir comment convertir un horodatage en chaîne et une chaîne en horodatage, c’est-à-dire comment sérialiser/désérialiser.

* Certaines applications sont configurées pour utiliser l’heure locale plutôt que l’heure UTC. Cela peut être pratique pour les projets qui doivent s’ajuster à l’heure locale, comme ceux qui déclenchent des événements fondés sur l’heure locale.

* Certains systèmes ont des besoins et des capacités de précision temporelle différents, comme l’utilisation d’une résolution de secondes, de millisecondes ou de nanosecondes. Par exemple, la commande `date` du système d’exploitation Linux utilise par défaut une précision de secondes, alors que la bourse Nasdaq veut par défaut une précision de nanosecondes.


### Décision

Nous choisissons le format d’horodatage standard ISO 8601 avec une précision à la nanoseconde, plus précisément « AAAA-MM-JJTHH:MM:SS.NNNNNNNNNZ ».

Le format indique l’année, le mois, le jour, l’heure, la minute, la seconde, les nanosecondes et le fuseau horaire Zoulou, alias UTC, GMT.


### État

Décidé.


## Détails


### Hypothèses

Nous devons gérer ces chaînes de texte d’horodatage, pour convertir un horodatage en chaîne (alias sérialiser) et une chaîne en horodatage (alias désérialiser).

Nous voulons un format généralement facile à utiliser, facile à convertir et facile à lire pour une personne.

Nous voulons une compatibilité avec un large éventail de systèmes externes que nous ne pouvons pas contrôler, comme des systèmes d’analyse, des systèmes de bases de données, des systèmes financiers.


### Contraintes

Certains systèmes ont des limites de précision temporelle. Par exemple, la commande `date` du système d’exploitation macOS peut afficher une précision en secondes, mais pas en nanosecondes.


### Positions

Nous avons envisagé une série d’options :

* L’epoch Unix, c’est-à-dire un seul nombre croissant.

* Un format de texte concis « AAAAMMJJTHHMMSSNNNNNNNNN ».

* Utiliser un fuseau horaire local ou le fuseau horaire UTC.


### Argument

Pour un usage typique, nous valorisons la facilité de lecture/écriture par des humains plus que la vitesse ou la taille brutes.

Pour un usage typique, nous voulons un format qui fonctionne bien dans les systèmes machine, et qui fonctionne aussi bien manuellement, par exemple pour écrire des données d’exemple, lire une sortie JSON, faire un grep dans un fichier journal, etc.

Pour un usage atypique, comme le calcul haute performance, nous nous attendons à vouloir optimiser tout format de texte retenu en convertissant le texte vers un format plus rapide, comme le type d’objet date intégré d’un langage de programmation. Le format de texte importe donc peu pour le HPC.


### Implications

Nos divers systèmes de texte et systèmes horaires convergeront vers ce format.


## Connexe


### Décisions connexes

Nous pourrions vouloir aussi un moyen rapide/facile de suivre les écarts de temps, alias durées. C’est facile avec les horodatages epoch Unix.


### Exigences connexes

Nous pourrions vouloir ajuster notre décision, par exemple si nous avons une exigence connexe pour un type précis d’horodatage de message de journalisation, comme pour Splunk, Sumo, ELK, etc.


### Artefacts connexes

Formateurs et analyseurs syntaxiques de langages :

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Exemples Rosetta Code :

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Exemples SixArm :

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Principes connexes

Facilement réversible. Nous pouvons passer assez facilement à un format différent, comme l’epoch Unix.

Différer l’optimisation prématurée. Pour un usage typique, nous ne nous soucions pas beaucoup de quelques caractères supplémentaires, comme dans un format qui utilise des tirets et des deux-points.


## Notes

Ajoutez des notes ici.
