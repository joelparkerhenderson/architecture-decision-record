# Lignes directrices pour des décisions durables

<https://www.infoq.com/articles/sustainable-architectural-design-decisions/>

Nous avons tiré de notre travail les enseignements suivants, qui peuvent servir de lignes directrices et d’évaluation pour parvenir à des décisions durables :

1. Adoptez une approche allégée et minimaliste pour la documentation initiale des décisions.

2. Hiérarchisez et consignez toutes les décisions importantes qui sont suffisamment pertinentes pour documenter et comprendre l’architecture cible.

3. Ne détaillez les décisions particulièrement importantes avec des modèles complets qu’une fois le travail initial terminé (c’est-à-dire lorsque les décideurs sont satisfaits des décisions d’architecture prises et convaincus qu’elles n’auront pas à être révisées de sitôt).

4. Utilisez les versions allégées et minimalistes de l’étape 1 comme version courte des décisions documentées, avec le bon niveau de granularité pour donner une vue d’ensemble des décisions détaillées, ainsi que pour les décisions triviales ou évidentes.

5. Dans la mesure du possible, utilisez les connaissances d’architecture existantes, qu’elles proviennent de modèles d’orientation ou d’autres sources. Passez-les en revue, étendez-les et adaptez-les au contexte de la décision spécifique.

6. Veillez à établir des liens de traçabilité entre les décisions et à la fois les exigences et les conceptions/le code d’architecture.

7. Prévoyez une vérification de cohérence automatisée pour garantir que les liens de traçabilité restent synchronisés après un changement. Limitez le nombre de dépendances entre les décisions et les autres artefacts logiciels.

8. Appliquez les lignes directrices relatives aux justifications de manière conséquente et résolue : ce sont la partie la plus importante de la documentation des décisions, car elles donnent la raison d’être.
