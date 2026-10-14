# Modèle d’enregistrement de décision pour les décisions techniques importantes (ITD)

Ceci est le modèle de décisions techniques importantes (Important Technical Decisions, ITD) décrit dans
[ITDs: a lean ADR for executive technical decision-making at scale - Ignacio Larrañaga](https://ignaciolarranaga.medium.com/itds-a-lean-adr-for-executive-technical-decision-making-at-scale-e18bb3f6a563).

Les ITD sont une évolution ciblée des ADR, optimisée pour la rapidité, la clarté et la validation par la direction. Là où un ADR documente ce qui a été décidé, un ITD est un artefact allégé, centré sur la décision, qui rend la décision elle-même révisable, afin que les parties prenantes puissent le parcourir rapidement et le contester facilement. Les ITD conviennent bien aux décisions techniques qui ne sont pas strictement architecturales, comme le choix d’un modèle, d’une bibliothèque ou d’une stratégie CI/CD.

Dans chaque fichier ITD, rédigez ces sections :

# Titre

Énoncez la décision elle-même, et non une description du sujet.
Par exemple : « Utiliser Qwen2.5 1.5B Instruct pour la traduction sur l’appareil ».

## Le problème

Une phrase indiquant ce que nous essayons de résoudre.

## Options envisagées

Les alternatives qui étaient sur la table, l’option retenue étant en **gras**.

## Justification

Uniquement les facteurs décisifs qui ont conduit au choix, et non une liste exhaustive de tous les avantages et inconvénients.

## Notes

Facultatif. Tout contexte supplémentaire utile à consigner, comme des contraintes, des hypothèses ou des liens.
