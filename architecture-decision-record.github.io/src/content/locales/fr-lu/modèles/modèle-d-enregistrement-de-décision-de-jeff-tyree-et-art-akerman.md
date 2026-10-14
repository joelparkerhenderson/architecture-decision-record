# Modèle d’enregistrement de décision de Jeff Tyree et Art Akerman

Ceci est le modèle de description de décision d’architecture publié dans ["Architecture Decisions: Demystifying Architecture" de Jeff Tyree et Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Question (Issue)** : décrivez la question de conception d’architecture que vous traitez, sans laisser d’interrogation sur la raison pour laquelle vous la traitez maintenant. Suivant une approche minimaliste, ne traitez et ne documentez que les questions qui doivent l’être à différents moments du cycle de vie.

* **Décision (Decision)** : énoncez clairement l’orientation de l’architecture, c’est-à-dire la position que vous avez retenue.

* **État (Status)** : l’état de la décision, par exemple en attente, décidée ou approuvée.

* **Groupe (Group)** : vous pouvez utiliser un regroupement simple, comme intégration, présentation, données, etc., pour aider à organiser l’ensemble des décisions. Vous pouvez aussi utiliser une ontologie d’architecture plus sophistiquée, comme celle de John Kyaruzi et Jan van Katwijk, qui comprend des catégories plus abstraites telles qu’événement, calendrier et lieu. Par exemple, avec cette ontologie, vous regrouperiez sous événement les décisions portant sur des occurrences pour lesquelles le système requiert de l’information.

* **Hypothèses (Assumptions)** : décrivez clairement les hypothèses sous-jacentes de l’environnement dans lequel vous prenez la décision : coût, calendrier, technologie, etc. Notez que les contraintes de l’environnement (comme les normes technologiques acceptées, l’architecture d’entreprise, les patrons couramment employés, etc.) peuvent limiter les alternatives que vous envisagez.

* **Contraintes (Constraints)** : consignez toute contrainte supplémentaire que l’alternative choisie (la décision) pourrait imposer à l’environnement.

* **Positions (Positions)** : listez les positions (options ou alternatives viables) que vous avez envisagées. Elles nécessitent souvent de longues explications, parfois même des modèles et des diagrammes. Ce n’est pas une liste exhaustive. Cependant, vous ne voulez pas entendre la question « Avez-vous pensé à... ? » lors d’une revue finale ; cela entraîne une perte de crédibilité et une remise en question d’autres décisions d’architecture. Cette section aide aussi à garantir que vous avez entendu les avis des autres ; énoncer explicitement d’autres opinions aide à rallier leurs défenseurs à votre décision.

* **Argument (Argument)** : exposez pourquoi vous avez retenu une position, notamment le coût de mise en œuvre, le coût total de possession, le délai de mise sur le marché et la disponibilité des ressources de développement requises. C’est probablement aussi important que la décision elle-même.

* **Implications (Implications)** : une décision s’accompagne de nombreuses implications, comme le dénote le métamodèle REMAP. Par exemple, une décision peut introduire la nécessité de prendre d’autres décisions, créer de nouvelles exigences ou modifier des exigences existantes, imposer des contraintes supplémentaires à l’environnement, exiger de renégocier la portée ou le calendrier avec les clients, ou nécessiter une formation supplémentaire du personnel. Comprendre et énoncer clairement les implications de votre décision peut être très efficace pour obtenir l’adhésion et créer une feuille de route d’exécution de l’architecture.

* **Décisions connexes (Related decisions)** : il est évident que de nombreuses décisions sont liées ; vous pouvez les lister ici. Cependant, nous avons constaté qu’en pratique une matrice de traçabilité, des arbres de décision ou des métamodèles sont plus utiles. Les métamodèles sont utiles pour montrer des relations complexes sous forme de diagrammes (comme les modèles Rose).

* **Exigences connexes (Related requirements)** : les décisions doivent être guidées par le métier. Pour démontrer la responsabilité, reliez explicitement vos décisions aux objectifs ou aux exigences. Vous pouvez énumérer ici ces exigences connexes, mais nous avons trouvé plus commode de renvoyer à une matrice de traçabilité. Vous pouvez évaluer la contribution de chaque décision d’architecture à la satisfaction de chaque exigence, puis évaluer dans quelle mesure l’exigence est satisfaite par l’ensemble des décisions. Si une décision ne contribue à satisfaire aucune exigence, ne prenez pas cette décision.

* **Artefacts connexes (Related artifacts)** : listez les documents d’architecture, de conception ou de portée connexes sur lesquels cette décision a un impact.

* **Principes connexes (Related principles)** : si l’entreprise dispose d’un ensemble de principes convenus, assurez-vous que la décision est cohérente avec l’un ou plusieurs d’entre eux. Cela aide à garantir l’alignement entre domaines ou systèmes.

* **Notes (Notes)** : comme le processus de décision peut prendre des semaines, nous avons trouvé utile de consigner les notes et les questions que l’équipe discute pendant le processus de socialisation.
