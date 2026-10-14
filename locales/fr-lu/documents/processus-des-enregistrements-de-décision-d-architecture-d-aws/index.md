# Processus des enregistrements de décision d’architecture d’AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Un enregistrement de décision d’architecture (ADR) est un document qui décrit un choix que l’équipe fait à propos d’un aspect significatif de l’architecture logicielle qu’elle prévoit de construire. Chaque ADR décrit la décision d’architecture, son contexte et ses conséquences. Les ADR ont des états et suivent donc un cycle de vie. Pour un exemple d’ADR, consultez l’annexe.

Le processus ADR produit une collection d’enregistrements de décision d’architecture. Cette collection forme le journal des décisions. Le journal des décisions fournit le contexte du projet ainsi que des informations détaillées de mise en œuvre et de conception. Les membres du projet parcourent les titres de chaque ADR pour se faire une idée du contexte du projet. Ils lisent les ADR pour approfondir les mises en œuvre et les choix de conception du projet.

Lorsque l’équipe accepte un ADR, il devient immuable. Si de nouvelles connaissances exigent une décision différente, l’équipe propose un nouvel ADR. Lorsque l’équipe accepte le nouvel ADR, il remplace l’ADR précédent.

## Portée du processus ADR

Les membres du projet doivent créer un ADR pour chaque décision architecturalement significative qui touche le projet ou le produit logiciel, notamment les suivantes (Richards et Ford 2020) :

* Structure (par exemple, des patrons tels que les microservices)

* Exigences non fonctionnelles (sécurité, haute disponibilité et tolérance aux pannes)

* Dépendances (couplage des composants)

* Interfaces (API et contrats publiés)

* Techniques de construction (bibliothèques, frameworks, outils et processus)

* Les exigences fonctionnelles et non fonctionnelles sont les entrées les plus courantes du processus ADR.


## Contenu de l’ADR

Lorsque l’équipe identifie un besoin d’ADR, un membre de l’équipe commence à rédiger l’ADR à partir d’un modèle commun à tout le projet. (Voir l’organisation ADR sur GitHub pour des exemples de modèles.) Le modèle simplifie la création de l’ADR et garantit qu’il recueille toutes les informations pertinentes. Au minimum, chaque ADR doit définir le contexte de la décision, la décision elle-même et les conséquences de la décision pour le projet et ses livrables. (Pour des exemples de ces sections, consultez l’annexe.) L’un des aspects les plus puissants de la structure de l’ADR est qu’elle se concentre sur la raison de la décision plutôt que sur la manière dont l’équipe l’a mise en œuvre. Comprendre pourquoi l’équipe a pris la décision facilite son adoption par les autres membres de l’équipe, et empêche d’autres architectes qui n’ont pas participé au processus de décision de la remettre en cause à l’avenir.


## Processus d’adoption de l’ADR

Chaque membre de l’équipe peut créer un ADR, mais l’équipe doit établir une définition de la propriété d’un ADR. Chaque auteur propriétaire d’un ADR doit activement maintenir et communiquer le contenu de l’ADR. Pour clarifier cette propriété, le présent guide désigne les auteurs d’ADR comme propriétaires d’ADR dans les sections suivantes. Les autres membres de l’équipe peuvent toujours contribuer à un ADR. Si le contenu d’un ADR change avant que l’équipe ne l’accepte, le propriétaire doit approuver ces changements.

Après que l’équipe a identifié une décision d’architecture et son propriétaire, le propriétaire de l’ADR présente l’ADR à l’état **Proposé** (Proposed) au début du processus. Les ADR à l’état Proposé sont prêts à être revus.

Le propriétaire de l’ADR lance ensuite le processus de revue de l’ADR. L’objectif du processus de revue est de décider si l’équipe accepte l’ADR, détermine qu’il doit être retravaillé ou le rejette. L’équipe projet, propriétaire compris, passe l’ADR en revue. La réunion de revue doit commencer par un créneau dédié à la lecture de l’ADR. En moyenne, 10 à 15 minutes devraient suffire. Pendant ce temps, chaque membre de l’équipe lit le document et ajoute des commentaires et des questions pour signaler les sujets peu clairs. Après la phase de revue, le propriétaire de l’ADR lit à voix haute et discute chaque commentaire avec l’équipe.

Si l’équipe trouve des points d’action pour améliorer l’ADR, l’état de l’ADR reste **Proposé**. Le propriétaire de l’ADR formule les actions et, en collaboration avec l’équipe, attribue un responsable à chaque action. Chaque membre de l’équipe peut contribuer aux points d’action et les résoudre. Il incombe au propriétaire de l’ADR de reprogrammer le processus de revue.

L’équipe peut aussi décider de rejeter l’ADR. Dans ce cas, le propriétaire de l’ADR ajoute le motif du rejet afin d’éviter de futures discussions sur le même sujet. Le propriétaire fait passer l’ADR à l’état **Rejeté** (Rejected).

Si l’équipe approuve l’ADR, le propriétaire ajoute un horodatage, une version et la liste des parties prenantes. Le propriétaire met ensuite l’état à **Accepté** (Accepted).

Les ADR et le journal des décisions qu’ils forment représentent les décisions prises par l’équipe et fournissent un historique de toutes les décisions. L’équipe utilise les ADR comme référence lors des revues de code et d’architecture lorsque c’est possible. En plus de réaliser des revues de code, des tâches de conception et des tâches de mise en œuvre, les membres de l’équipe doivent consulter les ADR pour les décisions stratégiques relatives au produit.

Par bonne pratique, chaque changement logiciel doit passer par des revues par les pairs et exiger au moins une approbation. Lors de la revue de code, un relecteur peut trouver des changements qui enfreignent un ou plusieurs ADR. Dans ce cas, le relecteur demande à l’auteur du changement de code de le mettre à jour et partage un lien vers l’ADR. Lorsque l’auteur met le code à jour, il est approuvé par les relecteurs pairs et fusionné dans la base de code principale.


## Processus de revue de l’ADR

L’équipe doit traiter les ADR comme des documents immuables après les avoir acceptés ou rejetés. Modifier un ADR existant exige de créer un nouvel ADR, d’établir un processus de revue pour ce nouvel ADR et de l’approuver. Si l’équipe approuve le nouvel ADR, le propriétaire doit faire passer l’ancien ADR à l’état **Remplacé** (Superseded).
