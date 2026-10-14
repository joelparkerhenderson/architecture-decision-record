# Enregistrement de décision d’architecture : snake_case ou camelCase pour une API REST ?

Décision : la convention de nommage snake_case sera utilisée pour les points de terminaison (endpoints) de l’API REST

État : Accepté

## Contexte

Dans les conventions de nommage des API REST, il existe deux formats populaires : snake_case et camelCase. Le format snake_case sépare chaque mot du nom par des traits de soulignement, alors que camelCase met le premier mot du nom en minuscules et met en majuscule la première lettre des mots suivants. Cette décision déterminera quelle convention de nommage doit être utilisée pour une API REST.

## Facteurs de décision

- Cohérence avec les conventions de nommage existantes du projet

- Lisibilité et clarté pour toute personne susceptible de travailler sur l’API

- Alignement sur les bonnes pratiques du secteur en matière de conventions de nommage d’API REST

- Facilité de mise en œuvre et de maintenance

## Décision

La convention de nommage snake_case sera utilisée pour les points de terminaison de l’API REST. Ce choix repose sur les facteurs suivants :

1. **Cohérence** : le projet utilise déjà la convention de nommage snake_case pour tous les points de terminaison, et il serait bénéfique de maintenir cette convention pour assurer la cohérence de l’ensemble du projet.

2. **Lisibilité et clarté** : la convention snake_case est plus lisible et plus facile à comprendre. Les traits de soulignement offrent une séparation claire entre les mots, ce qui facilite l’analyse et la compréhension du sens du nom.

3. **Alignement sur les bonnes pratiques du secteur** : la convention snake_case est largement utilisée dans le secteur et est considérée comme une bonne pratique pour les API REST, ce qui en fait un bon choix pour le projet.

4. **Facilité de mise en œuvre et de maintenance** : conserver la convention de nommage existante est plus facile à mettre en œuvre et à maintenir, car tout le code et toute la documentation existants devraient être mis à jour si une nouvelle convention était choisie.

## Conséquences

Cette décision a des conséquences potentielles. 

* Si de nouveaux membres de l’équipe qui rejoignent le projet ne connaissent pas la convention de nommage snake_case, cela pourrait entraîner de la confusion et des erreurs de développement. Toutefois, comme snake_case est une convention largement utilisée, ce risque est minime. 
  
* Si d’autres outils ou frameworks fortement basés sur la convention camelCase sont utilisés dans le projet, un effort supplémentaire peut être nécessaire pour convertir entre conventions de nommage. Ce n’est cependant pas une préoccupation importante, puisque le projet a normalisé la convention snake_case. 
 
Dans l’ensemble, la décision d’utiliser la convention de nommage snake_case pour les points de terminaison de l’API REST aboutit à une approche cohérente, lisible et conforme aux normes du secteur, tout en étant facile à mettre en œuvre et à maintenir.

<h6>Crédit : cette page a été générée par ChatGPT, puis modifiée pour la clarté et la mise en forme.</h6>
