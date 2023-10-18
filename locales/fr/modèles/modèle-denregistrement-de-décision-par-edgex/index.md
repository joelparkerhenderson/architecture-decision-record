# Modèle d'enregistrement de décision d'architecture (ADR) <!-- Remplacer par le titre ADR -->

Il s'agit d'un modèle pour EdgeX Foundry ADR.

Source : https://docs.edgexfoundry.org/2.3/design/adr/template/


### Soumissionnaires

Répertoriez les demandeurs d’ADR.

Format:

- Nom (Organisation)


## Journal des modifications

Répertoriez les modifications apportées au document, incl. état, date et URL PR.

L'état est l'un des suivants : en attente, approuvé, modifié, obsolète.

La date est une chaîne ISO 8601 (AAAA-MM-JJ).

PR est la pull request qui a soumis la modification, y compris des informations telles que la différence, les contributeurs et les réviseurs.

Format:

- \[Statut de l'ADR, par ex. approuvé, modifié, etc.\]\(URL de la demande d'extraction\) AAAA-MM-JJ


## Cas d'utilisation référencés

Répertoriez tous les cas d’utilisation/documents d’exigences pertinents.

L’ADR nécessite au moins un cas d’utilisation pertinent et approuvé.

Format:

- \[Nom du cas d'utilisation\]\(URL\)

Ajoutez des explications si l’ADR ne répond pas à toutes les exigences d’un cas d’utilisation.


## Contexte

Décrire:

- comment la conception est significative sur le plan architectural - justifiant un ADR (par rapport à un simple problème et un PR pour résoudre un problème)

- l'approche de conception de haut niveau (détails décrits dans la conception proposée ci-dessous)


## Conception proposée

Détails de la conception (sans entrer dans la mise en œuvre lorsque cela est possible).

Contour:

- services/modules à impacter (modifiés)

- nouveaux services/modules à ajouter

- impact modèle et DTO (modifications/ajouts/suppressions)

- Impact API (modifications/ajouts/suppressions)

- impact sur la configuration générale (création de nouvelles sections, modifications/ajouts/suppressions)

- impact sur les développeurs


## Considérations

Documenter les alternatives, les préoccupations, les questions accessoires ou connexes, les questions soulevées lors du débat sur l'ADR.

Indiquez si/comment ils ont été résolus ou apaisés.


## Décision

Documentez tous les détails de mise en œuvre importants convenus, les mises en garde, les considérations futures, les problèmes de conception restants ou différés.

Documentez toute partie des exigences non satisfaites par la conception proposée.


## Autres ADR associés

Répertoriez tous les ADR pertinents - comme une décision de conception pour un sous-composant d'une fonctionnalité, une conception obsolète en raison de cette conception, etc.

Format:

- \[Titre ADR\]\(URL\) - Pertinence


## Les références

Énumérez les références supplémentaires.

Format:

- \[Titre\]\(URL\)