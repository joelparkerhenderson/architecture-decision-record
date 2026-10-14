# Modèle d’enregistrement de décision d’architecture (ADR) <!-- Remplacer par le titre de l’ADR -->

Ceci est un modèle pour les ADR d’EdgeX Foundry.

Source : https://docs.edgexfoundry.org/2.3/design/adr/template/


### Auteurs de la soumission

Listez les personnes qui soumettent l’ADR.

Format :

- Nom (Organisation)


## Journal des modifications

Listez les modifications apportées au document, y compris l’état, la date et l’URL de la PR.

L’état est l’un des suivants : pending (en attente), approved (approuvé), amended (amendé), deprecated (obsolète).

La date est une chaîne ISO 8601 (AAAA-MM-JJ).

La PR est la demande de fusion (pull request) qui a soumis la modification, avec des informations telles que le diff, les contributeurs et les relecteurs.

Format :

- \[État de l’ADR, p. ex. approved, amended, etc.\]\(URL de la demande de fusion\) AAAA-MM-JJ


## Cas d’usage référencés

Listez tous les documents de cas d’usage et d’exigences pertinents.

L’ADR exige au moins un cas d’usage pertinent et approuvé.

Format :

- \[Nom du cas d’usage\]\(URL\)

Ajoutez des explications si l’ADR ne couvre pas toutes les exigences d’un cas d’usage.


## Contexte

Décrivez :

- en quoi la conception est architecturalement significative et justifie un ADR (plutôt qu’un simple ticket et une PR pour corriger un problème)

- l’approche de conception de haut niveau (les détails sont décrits dans la conception proposée ci-dessous)


## Conception proposée

Détails de la conception (sans entrer dans la mise en œuvre dans la mesure du possible).

Plan :

- services/modules touchés (modifiés)

- nouveaux services/modules à ajouter

- impact sur le modèle et les DTO (modifications/ajouts/suppressions)

- impact sur les API (modifications/ajouts/suppressions)

- impact sur la configuration générale (création de nouvelles sections, modifications/ajouts/suppressions)

- impact sur le devops


## Considérations

Documentez les alternatives, les préoccupations, les questions annexes ou connexes et les interrogations soulevées lors du débat sur l’ADR. 

Indiquez si et comment elles ont été résolues ou atténuées.


## Décision

Documentez tout détail de mise en œuvre important sur lequel on s’est accordé, les réserves, les considérations futures, ainsi que les questions de conception restantes ou reportées.

Documentez toute partie des exigences non satisfaite par la conception proposée.


## Autres ADR connexes

Listez les ADR pertinents, comme une décision de conception pour un sous-composant d’une fonctionnalité, une conception rendue obsolète par celle-ci, etc. 

Format :

- \[Titre de l’ADR\]\(URL\) - Pertinence


## Références

Listez des références supplémentaires.

Format :

- \[Titre\]\(URL\)
