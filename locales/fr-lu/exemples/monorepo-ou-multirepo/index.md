# Monorepo ou multirepo

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

Notre projet consiste à développer trois grandes catégories de logiciels :

  * Interfaces graphiques (GUI) front-end
  * Services d’intergiciel (middleware)
  * Serveurs back-end

Lorsque nous développons, notre système de contrôle de version (VCS) de gestion du code source (SCM) est git.

Nous devons choisir comment utiliser git pour organiser notre code.

Le choix de plus haut niveau est d’organiser en « monorepo », en « polyrepo » ou en « hybride » :

  * Monorepo signifie que nous mettons toutes les pièces dans un seul grand dépôt
  * Polyrepo signifie que nous mettons chaque pièce dans son propre dépôt
  * Hybride signifie un mélange de monorepo et de polyrepo

Pour en savoir plus, voir https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Décision

Monorepo lorsqu’une organisation/équipe/un projet est relativement petit(e) et que l’itération rapide est une priorité plus élevée que le maintien de la stabilité.

Polyrepo lorsqu’une organisation/équipe/un projet est relativement grand(e) et que le maintien de la stabilité est une priorité plus élevée que l’itération rapide.


### État

Décidé. Ouverts à un réexamen si et quand de nouveaux outils seront disponibles pour gérer les monorepos et/ou les polyrepos.


## Détails


### Hypothèses

Tout le code que nous développons est destiné aux offres d’une seule organisation, et non au grand public. Autrement dit, le courtier-négociant (Broker-Dealer) ne vise pas à avoir quoi que ce soit qui ressemble à des développeurs bénévoles issus du grand public.


### Contraintes

Les contraintes sont bien documentées sur https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Positions

Nous avons envisagé des monorepos à la manière de Google, Facebook, etc. Nous pensons que les problèmes de mise à l’échelle d’un monorepo sont si lointains que, le moment venu, nous pourrons mettre à profit les mêmes pratiques que Google et Facebook.

Nous avons envisagé des polyrepos à la manière des projets open source Git typiques, tels que Google Android, Facebook React, etc. Nous pensons qu’ils sont le meilleur choix pour la participation du grand public (p. ex. n’importe qui dans le monde peut travailler sur le code) et pour la disponibilité individuelle (p. ex. le projet est utilisé seul, sans aucune autre pièce).


### Argument

Lorsqu’une organisation/équipe/un projet est relativement petit(e), nous choisissons le monorepo, car l’itération rapide a une priorité nettement plus élevée que le maintien de la stabilité.

Lorsqu’une organisation/équipe/un projet est relativement grand(e), nous choisissons le polyrepo, car le maintien de la stabilité a une priorité nettement plus élevée que l’itération rapide.


### Implications

S’il existe déjà une chaîne CI+CD, nous devrons peut-être l’ajuster pour tester plusieurs projets au sein d’un même dépôt.

La CI+CD pourrait prendre plus de temps pour un build complet d’un monorepo, car elle pourrait construire tous les projets du monorepo.

Si une organisation/équipe/un projet grandit, le monorepo connaîtra des problèmes de mise à l’échelle.

Les problèmes de mise à l’échelle du monorepo peuvent rendre de plus en plus précieuse la transition vers un polyrepo.

La transition d’un monorepo vers un polyrepo est une tâche devops importante, qui devra être planifiée, gérée et programmée.


## Connexe


### Décisions connexes

Nous créerons des décisions pour les outils connexes de gestion des monorepos (p. ex. Google Bazel) et des polyrepos (p. ex. Lyft Refactorator).


### Exigences connexes

Nous devons développer la chaîne CI+CD pour qu’elle fonctionne bien avec git.


### Artefacts connexes

Nous nous attendons à ce que l’organisation du dépôt comporte des artefacts connexes pour le provisionnement, la gestion de configuration, les tests et des domaines devops similaires. 


### Principes connexes

Facilement réversible. Si le monorepo ne fonctionne pas en pratique, ou si la direction n’en veut pas, il est simple de passer au polyrepo.

Obsession du client. Nous accordons de la valeur au fait de mettre le projet entre les mains des clients, et nous pensons qu’un monorepo peut nous y amener plus vite qu’un polyrepo, et aussi nous aider à itérer plus vite.

Voir grand. Google et Facebook sont de très fervents partisans des monorepos plutôt que des polyrepos, car toutes les offres principales peuvent être développées, testées et déployées de concert.


## Notes

Ajoutez des notes ici.
