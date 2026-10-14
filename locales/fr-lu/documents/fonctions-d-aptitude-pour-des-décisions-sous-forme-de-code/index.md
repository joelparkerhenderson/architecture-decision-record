# Fonctions d’aptitude pour des décisions sous forme de code

Les fonctions d’aptitude (fitness functions) sont des vérifications automatisées et objectives, écrites en code de programmation, qui contrôlent que les décisions sont respectées.

- Les fonctions d’aptitude rendent les décisions testables et vérifiables.

- Les fonctions d’aptitude pour les décisions peuvent grandement faciliter l’assurance qualité, les processus réglementaires et les objectifs de gouvernance.

## Comment les fonctions d’aptitude se rattachent aux décisions

Un enregistrement de décision documente la décision, tandis qu’une fonction d’aptitude la garantit.

- Exemple de décision : nous utilisons l’event sourcing pour les exigences d’audit.

- Exemple de fonction d’aptitude : nous utilisons le serveur d’intégration continue pour vérifier que tous les changements d’état doivent produire des événements.

## Pourquoi les fonctions d’aptitude aident les décisions

Mesures objectives : les fonctions d’aptitude réussissent ou échouent, de sorte que le travail est visible et clair.

Usage continu : les fonctions d’aptitude sont vos règles vivantes, exécutées à chaque commit et à chaque build.

Confiance pour refactoriser : les fonctions d’aptitude détectent automatiquement les erreurs dans les règles de décision.

Gouvernance évolutive : les fonctions d’aptitude garantissent les normes sans créer de goulots d’étranglement.

## Les fonctions d’aptitude peuvent-elles utiliser l’IA ?

Les fonctions d’aptitude peuvent tirer parti des LLM d’IA pour les décisions en posant des questions sur votre travail, comme vos plans, votre code, vos schémas, vos API, etc. :

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Tests unitaires d’architecture

[ArchUnit](https://www.archunit.org/) : vérifie les règles d’architecture du code Java à l’aide de n’importe quel framework de tests unitaires Java ordinaire.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS) : vérifie les règles d’architecture du code TypeScript et JavaScript à l’aide de Jest, Vitest, Jasmine, etc.
