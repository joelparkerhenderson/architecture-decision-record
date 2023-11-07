# Processus des dossiers de décision architecturale AWS

https://docs.aws.amazon.com/prescriptive-uidance/latest/architectural-decision-records/adr-process.html

Un dossier de décision architecturale (ADR) est un document qui décrit un choix que l'équipe fait sur un aspect important de l'architecture logicielle qu'il prévoit de construire. Chaque ADR décrit la décision architecturale, son contexte et ses conséquences. Les ADR ont des États et suivent donc un cycle de vie. Pour un exemple d'ADR, voir l'annexe.

Le processus ADR publie une collection de dossiers de décision architecturale. Cette collection crée le journal de décision. Le journal de décision fournit le contexte du projet ainsi que des informations détaillées sur la mise en œuvre et la conception. Les membres du projet font les gros titres de chaque ADR pour obtenir un aperçu du contexte du projet. Ils ont lu les ADR pour plonger profondément dans les implémentations du projet et les choix de conception.

Lorsque l'équipe accepte une ADR, elle devient immuable. Si de nouvelles informations nécessitent une décision différente, l'équipe propose un nouvel ADR. Lorsque l'équipe accepte le nouvel ADR, il remplace l'ADR précédent.

## Portée du processus ADR

Les membres du projet doivent créer un ADR pour chaque décision architecturale significative qui affecte le projet ou le produit logiciel, y compris les suivants (Richards et Ford 2020):

* Structure (par exemple, des modèles tels que les microservices)

* Exigences non fonctionnelles (sécurité, haute disponibilité et tolérance aux défauts)

* Dépendances (couplage des composants)

* Interfaces (API et contrats publiés)

* Techniques de construction (bibliothèques, cadres, outils et processus)

* Les exigences fonctionnelles et non fonctionnelles sont les entrées les plus courantes du processus ADR.


## Contenu ADR

Lorsque l'équipe identifie le besoin d'un ADR, un membre de l'équipe commence à écrire l'ADR en fonction d'un modèle à l'échelle du projet. (Voir l'organisation ADR GitHub par exemple les modèles.) Le modèle simplifie la création de l'ADR et garantit que l'ADR capture toutes les informations pertinentes. Au minimum, chaque ADR devrait définir le contexte de la décision, la décision elle-même et les conséquences de la décision pour le projet et ses livrables. (Pour des exemples de ces sections, voir l'annexe.) L'un des aspects les plus puissants de la structure ADR est qu'il se concentre sur la raison de la décision plutôt que sur la façon dont l'équipe l'a mise en œuvre. Comprendre pourquoi l'équipe a pris la décision permet aux autres membres de l'équipe d'adopter plus facilement la décision et empêche d'autres architectes qui n'ont pas été impliqués dans le processus décisionnel pour annuler cette décision à l'avenir.


## Processus d'adoption de l'ADR

Chaque membre de l'équipe peut créer une ADR, mais l'équipe doit établir une définition de la propriété pour un ADR. Chaque auteur qui est propriétaire d'un ADR doit conserver et communiquer activement le contenu ADR. Pour clarifier cette propriété, ce guide fait référence aux auteurs de l'ADR en tant que propriétaires de ADR dans les sections suivantes. D'autres membres de l'équipe peuvent toujours contribuer à un ADR. Si le contenu d'un ADR change avant que l'équipe n'accepte l'ADR, le propriétaire doit approuver ces modifications.

Après que l'équipe ait identifié une décision architecturale et son propriétaire, le propriétaire de l'ADR fournit l'ADR dans l'état ** proposé ** au début du processus. Les ADR dans l'État proposé sont prêts à être révisés.

Le propriétaire de l'ADR initie ensuite le processus d'examen de l'ADR. L'objectif du processus d'examen ADR est de décider si l'équipe accepte l'ADR, détermine qu'il doit être retravaillé ou rejette l'ADR. L'équipe de projet, y compris le propriétaire, passe en revue l'ADR. La réunion d'examen devrait commencer par un créneau horaire dédié pour lire l'ADR. En moyenne, 10 à 15 minutes devraient suffire. Pendant ce temps, chaque membre de l'équipe lit le document et ajoute des commentaires et des questions pour signaler des sujets peu clairs. Après la phase d'examen, le propriétaire de l'ADR lit et discute de chaque commentaire avec l'équipe.

Si l'équipe trouve des points d'action pour améliorer l'ADR, l'état de l'ADR reste ** proposé **. Le propriétaire de l'ADR formule les actions et, en collaboration avec l'équipe, ajoute un cessionnaire à chaque action. Chaque membre de l'équipe peut contribuer et résoudre les points d'action. Il est de la responsabilité du propriétaire de l'ADR de reprogrammer le processus d'examen.

L'équipe peut également décider de rejeter l'ADR. Dans ce cas, le propriétaire de l'ADR ajoute une raison pour le rejet pour empêcher les discussions futures sur le même sujet. Le propriétaire modifie l'état ADR en ** rejeté **.

Si l'équipe approuve l'ADR, le propriétaire ajoute un horodatage, une version et une liste des parties prenantes. Le propriétaire met ensuite à jour l'état à ** accepté **.

Les ADR et le journal de décision qu'ils créent représentent les décisions prises par l'équipe et fournissent une histoire de toutes les décisions. L'équipe utilise les ADR comme référence pendant le code et les revues architecturales dans la mesure du possible. En plus d'effectuer des avis de code, des tâches de conception et des tâches de mise en œuvre, les membres de l'équipe doivent consulter les ADR pour des décisions stratégiques pour le produit.

En tant que bonne pratique, chaque changement de logiciel devrait passer par les examens par les pairs et nécessiter au moins une approbation. Au cours de l'examen du code, un réviseur de code peut trouver des modifications qui violent un ou plusieurs ADR. Dans ce cas, le réviseur demande à l'auteur de la modification du code pour mettre à jour le code et partage un lien vers l'ADR. Lorsque l'auteur met à jour le code, il est approuvé par les pairs examinateurs et fusionné dans la base de code principale.


## Processus d'examen ADR

L'équipe doit traiter les ADR comme des documents immuables après que l'équipe les a acceptés ou les a rejetés. Les modifications à un ADR existant nécessitent la création d'un nouveau ADR, l'établissement d'un processus d'examen pour la nouvelle ADR et l'approbation de l'ADR. Si l'équipe approuve la nouvelle ADR, le propriétaire doit changer l'état de l'ancien ADR en ** remplacé **.
