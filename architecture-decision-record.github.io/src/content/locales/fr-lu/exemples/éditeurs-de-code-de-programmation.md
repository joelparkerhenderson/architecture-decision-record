# Enregistrement de décision d’architecture : éditeurs de code de programmation

## Contexte

Les éditeurs de code de programmation sont un outil essentiel pour que les développeurs écrivent et modifient du code. De nombreux éditeurs de code sont disponibles, chacun avec son propre ensemble de fonctionnalités, d’avantages et d’inconvénients. L’objectif de cet ADR est de documenter les décisions d’architecture prises pour les éditeurs de code de programmation.

## Priorités

L’architecture des éditeurs de code de programmation doit privilégier les points suivants :

* **Modularité** : l’éditeur de code doit être conçu de manière modulaire, afin que les développeurs puissent le personnaliser et l’étendre selon leurs besoins. Cela permet une architecture flexible qui peut s’adapter aux besoins de différents développeurs et équipes.

* **Performance** : l’éditeur de code doit être performant et réactif, afin que les développeurs puissent travailler efficacement sans être ralentis par l’outil qu’ils utilisent.

* **Interface utilisateur** : l’interface utilisateur doit être intuitive et facile à utiliser, afin que les développeurs puissent se concentrer sur leur code plutôt que de lutter avec l’éditeur.

* **Extensibilité** : l’éditeur de code doit être conçu pour permettre une extension facile par des plugins et des intégrations tiers.

* **Compatibilité** : l’éditeur de code doit être compatible avec un large éventail de langages de programmation et de technologies, ce qui en fait un outil utile pour un large éventail de développeurs.

## Décision

Sur la base de ces priorités, l’architecture des éditeurs de code de programmation doit être conçue avec les composants suivants :

* **Noyau** : ce composant fournit les fonctionnalités de base de l’éditeur de code, comme la coloration syntaxique, l’édition de texte et la gestion de fichiers.

* **UI** : ce composant fournit l’interface utilisateur de l’éditeur de code, y compris les menus, les barres d’outils et les raccourcis clavier.

* **Plugins** : ce composant permet aux développeurs d’étendre les fonctionnalités de l’éditeur de code en installant des plugins tiers. Les plugins peuvent fournir des fonctionnalités supplémentaires, comme la complétion de code, le linting ou le débogage.

* **Intégrations** : ce composant permet à l’éditeur de code de s’intégrer à d’autres outils et technologies, comme les systèmes de contrôle de version, les systèmes de build ou les outils de débogage.

## Justification

La modularité de l’éditeur de code permet aux développeurs de le personnaliser et de l’étendre selon leurs besoins. C’est important parce que les développeurs et les équipes ont des besoins et des flux de travail différents, et qu’une architecture flexible peut s’accommoder de ces différences.

* **Performance** : cruciale parce que les développeurs doivent pouvoir travailler efficacement sans être ralentis par leurs outils. Un éditeur de code performant est essentiel à la productivité et peut aider les développeurs à garder leur concentration.

* **UI** : importante parce qu’elle permet aux développeurs de se concentrer sur leur code plutôt que de lutter avec l’éditeur. Cela peut améliorer la productivité et réduire la frustration des développeurs.

* **Extensibilité** : puissante parce qu’elle permet d’adapter l’éditeur de code à différents besoins et flux de travail. Les plugins et intégrations tiers peuvent fournir des fonctionnalités et capacités supplémentaires qui ne figurent pas dans l’éditeur de base.

* **Compatibilité** : précieuse parce qu’elle permet d’utiliser l’éditeur de code avec un large éventail de langages de programmation et de technologies. Cela fait de l’éditeur un outil plus utile pour un large éventail de développeurs.

Les composants noyau, plugins, intégrations et UI assurent une séparation claire des préoccupations et permettent une architecture modulaire qui peut être facilement étendue et personnalisée. Cette architecture est flexible, performante et compatible avec un large éventail de langages de programmation et de technologies, ce qui en fait un outil utile pour les développeurs.
