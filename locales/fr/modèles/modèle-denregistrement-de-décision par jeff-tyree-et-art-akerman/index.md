# Modèle d'enregistrement de décision par Jeff Tyree et Art Akerman

Il s'agit du modèle de description de décision d'architecture publié dans ["Architecture Decisions: Demystifying Architecture" par Jeff Tyree et Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions- pneu-05.pdf).

* **Problème** : décrivez le problème de conception architecturale que vous abordez, sans laisser de questions sur la raison pour laquelle vous abordez ce problème maintenant. En suivant une approche minimaliste, abordez et documentez uniquement les problèmes qui doivent être résolus à différents stades du cycle de vie.

* **Décision** : indiquez clairement l'orientation de l'architecture, c'est-à-dire la position que vous avez sélectionnée.

* **Statut** : le statut de la décision, par exemple en attente, décidé ou approuvé.

* **Groupe** : vous pouvez utiliser un regroupement simple (tel que l'intégration, la présentation, les données, etc.) pour vous aider à organiser l'ensemble des décisions. Vous pouvez également utiliser une ontologie d'architecture plus sophistiquée, telle que celle de John Kyaruzi et Jan van Katwijk, qui comprend des catégories plus abstraites telles que l'événement, le calendrier et le lieu. Par exemple, en utilisant cette ontologie, vous regrouperiez les décisions qui traitent des occurrences pour lesquelles le système nécessite des informations sous un événement.

* **Hypothèses** : décrivez clairement les hypothèses sous-jacentes à l'environnement dans lequel vous prenez la décision : coût, calendrier, technologie, etc. Notez que les contraintes environnementales (telles que les normes technologiques acceptées, l'architecture d'entreprise, les modèles couramment utilisés, etc.) peuvent limiter les alternatives que vous envisagez.

* **Contraintes** : capturez toutes les contraintes supplémentaires à l'environnement que l'alternative choisie (la décision) pourrait poser.

* **Positions** : répertoriez les postes (options ou alternatives viables) que vous avez envisagés. Celles-ci nécessitent souvent de longues explications, parfois même des modèles et des diagrammes. Il ne s’agit pas d’une liste exhaustive. Cependant, vous ne voulez pas entendre la question « Avez-vous pensé à… ? lors d'un examen final ; cela conduit à une perte de crédibilité et à une remise en question des autres décisions architecturales. Cette section permet également de garantir que vous avez entendu les opinions des autres ; exprimer explicitement d’autres opinions aide à inscrire leurs défenseurs dans votre décision.

* **Argument** : expliquez pourquoi vous avez sélectionné un poste, y compris des éléments tels que le coût de mise en œuvre, le coût total de possession, le délai de mise sur le marché et la disponibilité des ressources de développement requises. C’est probablement aussi important que la décision elle-même.

* **Implications** : une décision a de nombreuses implications, comme l'indique le métamodèle REMAP. Par exemple, une décision peut introduire le besoin de prendre d’autres décisions, de créer de nouvelles exigences ou de modifier des exigences existantes ; imposent des contraintes supplémentaires à l'environnement ; exiger une renégociation de la portée ou du calendrier avec les clients ; ou nécessitent une formation supplémentaire du personnel. Comprendre et énoncer clairement les implications de votre décision peut être très efficace pour obtenir l’adhésion et créer une feuille de route pour l’exécution de l’architecture.

* **Décisions liées** : Il est évident que de nombreuses décisions sont liées ; vous pouvez les lister ici. Cependant, nous avons constaté qu’en pratique, une matrice de traçabilité, des arbres de décision ou des métamodèles sont plus utiles. Les métamodèles sont utiles pour représenter schématiquement des relations complexes (comme les modèles Rose).

* **Exigences associées** : les décisions doivent être motivées par l'entreprise. Pour faire preuve de responsabilité, associez explicitement vos décisions aux objectifs ou aux exigences. Vous pouvez énumérer ces exigences connexes ici, mais nous avons trouvé plus pratique de référencer une matrice de traçabilité. Vous pouvez évaluer la contribution de chaque décision d’architecture à la satisfaction de chaque exigence, puis évaluer dans quelle mesure l’exigence est satisfaite dans toutes les décisions. Si une décision ne contribue pas à répondre à une exigence, ne prenez pas cette décision.

* **Artefacts associés** : répertoriez les documents d'architecture, de conception ou de portée associés sur lesquels cette décision a un impact.

* **Principes associés** : si l'entreprise a convenu d'un ensemble de principes, assurez-vous que la décision est cohérente avec un ou plusieurs d'entre eux. Cela permet de garantir l’alignement entre les domaines ou les systèmes.

* **Notes** : étant donné que le processus de prise de décision peut prendre des semaines, nous avons trouvé utile de capturer les notes et les problèmes dont l'équipe discute au cours du processus de socialisation.
