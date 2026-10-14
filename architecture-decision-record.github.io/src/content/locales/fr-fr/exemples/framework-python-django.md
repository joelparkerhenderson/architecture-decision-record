# Enregistrement de décision d’architecture pour le framework Python Django

Date de la décision : 2021-07-15

État : Accepté

## Contexte

Notre organisation prévoit de développer une application web qui gère des données clients. Nous avons choisi Python comme langage de programmation et envisageons Django comme framework web pour le développement de l’application.

## Décision

Nous avons décidé d’utiliser le framework web Django pour le développement de l’application web. Django fournit un ensemble robuste d’outils et de fonctionnalités pour construire des applications web rapidement et efficacement. 

## Facteurs

Voici quelques-uns des facteurs qui ont influencé notre décision :

1. Mapping objet-relationnel (ORM) : Django dispose d’un ORM intégré qui nous permet d’interagir avec la base de données sans écrire de requêtes SQL. Cela facilite le développement de l’application et sa maintenance à long terme.

2. Framework MVC : Django suit une architecture Modèle-Vue-Contrôleur (MVC), ce qui facilite la séparation de la logique métier et des couches de présentation de l’application.

3. Évolutivité : Django est connu pour ses capacités d’évolutivité, ce qui en fait un excellent choix pour développer des applications à grande échelle.

4. Sécurité : Django dispose de fonctionnalités de sécurité intégrées, comme la protection contre les attaques web courantes telles que le cross-site scripting (XSS) et l’injection SQL.

5. Soutien de la communauté : Django dispose d’une communauté vaste et active qui apporte son soutien et contribue au développement du framework.

## Alternatives envisagées

Nous avons envisagé d’autres frameworks web comme Flask et Pyramid. Cependant, nous avons constaté que Django est un framework plus mature et mieux établi, doté d’un ensemble robuste de fonctionnalités.

Nous avons aussi discuté du développement de l’application sans framework web, en utilisant des bibliothèques comme SQLAlchemy et Flask-RESTful. Cependant, nous avons constaté que Django offre des fonctionnalités plus larges, ce qui en fait un meilleur choix pour une application web complète.

## Conséquences

L’adoption de Django aura les conséquences suivantes :

1. Il sera plus facile de développer et de maintenir l’application grâce aux outils et fonctionnalités intégrés de Django.

2. Séparation de la logique métier et de la couche de présentation, ce qui donne un code mieux organisé et plus facile à maintenir.

3. Évolutivité et robustesse de l’application.

4. Fonctionnalités de sécurité intégrées qui aident à protéger l’application contre les attaques web courantes.

5. Accès à une communauté vaste et active pour obtenir de l’aide.

Nous comprenons que Django a une courbe d’apprentissage plus raide que d’autres frameworks, mais nous estimons que l’investissement en vaut la peine au regard des avantages à long terme qu’il procure.

## Conclusion

Sur la base des facteurs examinés, nous avons décidé d’utiliser le framework web Django pour le développement de l’application web. Nous pensons que les fonctionnalités, le soutien de la communauté et les capacités d’évolutivité de Django en font le meilleur choix pour construire une application web complète. Nous formerons nos développeurs à l’utilisation de Django afin de garantir que le framework est utilisé de manière efficace et efficiente.
