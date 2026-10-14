# Enregistrement de décision d’architecture : choix d’une technologie de base de données

## État

Accepté

## Contexte

Nous concevons une nouvelle application qui doit stocker et récupérer des données de manière évolutive et performante. Nous avons identifié trois types de technologies de base de données couramment utilisées : les bases de données relationnelles, les bases de données documentaires et les bases de données d’événements.

Les bases de données relationnelles stockent les données dans des tables aux schémas fixes et appliquent des contraintes strictes d’intégrité des données. Elles conviennent aux applications qui requièrent des relations de données complexes et des transactions. Parmi les exemples : MySQL, PostgreSQL et Oracle.

Les bases de données documentaires stockent les données dans des documents de type JSON et n’ont pas de schéma. Elles conviennent bien aux applications qui requièrent des modèles de données flexibles et une mise à l’échelle horizontale. Parmi les exemples : MongoDB, Couchbase et Amazon DynamoDB.

Les bases de données d’événements stockent les données sous forme de suite d’événements, enregistrant chaque modification des données. Elles conviennent aux applications qui requièrent de l’audit, de l’event sourcing et un traitement de données complexe. Parmi les exemples : Apache Kafka, Apache Pulsar et AWS Kinesis.

## Décision

Après avoir soigneusement évalué les exigences et les contraintes de notre application, nous avons décidé d’utiliser une base de données documentaire.

## Justification

Nous avons choisi une base de données documentaire parce que :

1. Notre application requiert un modèle de données flexible capable d’évoluer dans le temps. Les bases de données documentaires nous permettent de stocker les données dans un format sans schéma, ce qui signifie que nous pouvons ajouter de nouveaux champs ou modifier la structure de documents existants sans modifier le schéma de la base de données.

2. Notre application doit monter en charge horizontalement pour traiter de gros volumes de données et de trafic. Les bases de données documentaires offrent une prise en charge native du partitionnement (sharding) et de la réplication, ce qui nous permet de répartir les données sur plusieurs serveurs et de gérer un débit élevé de lectures et d’écritures.

3. Notre application requiert une récupération des données rapide et efficace. Les bases de données documentaires offrent de puissantes capacités d’indexation et d’interrogation qui nous permettent de récupérer les données rapidement et efficacement.

4. Notre application n’a pas besoin de transactions complexes ni de relations de données. Si les bases de données relationnelles excellent à appliquer des contraintes d’intégrité des données et à gérer des transactions complexes, notre application n’a pas de telles exigences. Les bases de données documentaires peuvent offrir des garanties de cohérence et de durabilité suffisantes pour notre cas d’usage.

## Conséquences

En choisissant une base de données documentaire, nous devrons investir dans l’apprentissage et la compréhension de la technologie précise que nous choisirons. De plus, nous devrons veiller à ce que le modèle de données de notre application s’accorde bien avec celui de la base documentaire pour maximiser la performance et l’évolutivité.

Toutefois, nous pensons que les avantages d’une base de données documentaire l’emportent sur les coûts, et qu’elle est la mieux adaptée aux exigences et aux contraintes de notre application.
