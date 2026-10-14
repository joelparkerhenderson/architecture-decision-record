# Enregistrement de décision d’architecture (ADR)

Un enregistrement de décision d’architecture (ADR) est un document qui consigne une décision d’architecture importante, avec son contexte et ses conséquences.

> [!IMPORTANT]
> Effectuez vos propres vérifications préalables sur ces ressources avant de les utiliser dans des systèmes critiques.

Sommaire :

- [Qu’est-ce qu’un enregistrement de décision d’architecture ?](#quest-ce-quun-enregistrement-de-décision-darchitecture-)
- [Comment commencer à utiliser les ADR](#comment-commencer-à-utiliser-les-adr)
- [Comment commencer à utiliser les ADR avec des outils](#comment-commencer-à-utiliser-les-adr-avec-des-outils)
- [Comment commencer à utiliser les ADR avec git](#comment-commencer-à-utiliser-les-adr-avec-git)
- [Compétences Claude Code pour les ADR](#compétences-claude-code-pour-les-adr)
- [Conventions de nommage des fichiers](#conventions-de-nommage-des-fichiers)
- [Conseils pour rédiger de bons ADR](#conseils-pour-rédiger-de-bons-adr)
- [Modèles d’exemple d’ADR](#modèles-dexemple-dadr)
- [Conseils de travail d’équipe pour les ADR](#conseils-de-travail-déquipe-pour-les-adr)
- [Questions de travail d’équipe pour les ADR](#questions-de-travail-déquipe-pour-les-adr)
- [Concepts de l’étape suivante pour les ADR](#concepts-de-létape-suivante-pour-les-adr)
- [Diagrammes, vues et points de vue d’architecture](#diagrammes-vues-et-points-de-vue-darchitecture)
- [Fonctions d’aptitude pour des décisions sous forme de code](#fonctions-daptitude-pour-des-décisions-sous-forme-de-code)
- [Garde-fous de décision pour les pull requests](#garde-fous-de-décision-pour-les-pull-requests)
- [Pour plus d’informations](#pour-plus-dinformations)

Modèles :

- [Modèle d’enregistrement de décision de Jeff Tyree et Art Akerman](modèles/modèle-d-enregistrement-de-décision-de-jeff-tyree-et-art-akerman/)
- [Modèle d’enregistrement de décision de Michael Nygard](modèles/modèle-d-enregistrement-de-décision-de-michael-nygard/)
- [Modèle d’enregistrement de décision d’EdgeX](modèles/modèle-d-enregistrement-de-décision-d-edgex/)
- [Modèle d’enregistrement de décision d’arc42](modèles/modèle-d-enregistrement-de-décision-d-arc42/)
- [Modèle d’enregistrement de décision pour le patron alexandrin](modèles/modèle-d-enregistrement-de-décision-pour-le-patron-alexandrin/)
- [Modèle d’enregistrement de décision pour une analyse de rentabilité](modèles/modèle-d-enregistrement-de-décision-pour-une-analyse-de-rentabilité/)
- [Modèle d’enregistrement de décision du projet MADR](modèles/modèle-d-enregistrement-de-décision-du-projet-madr/)
- [Modèle d’enregistrement de décision avec Planguage](modèles/modèle-d-enregistrement-de-décision-avec-planguage/)
- [Modèle d’enregistrement de décision de Paulo Merson](https://github.com/pmerson/ADR-template)
- [Modèle d’enregistrement de décision d’Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Modèle d’enregistrement de décision de Gareth Morgan](modèles/modèle-d-enregistrement-de-décision-de-gareth-morgan/)
- [Modèle d’enregistrement de décision de GIG Cymru NHS Wales](modèles/modèle-d-enregistrement-de-décision-de-gig-cymru-nhs-wales/)
- [Modèle d’enregistrement de décision pour les décisions techniques importantes (ITD) d’Ignacio Larrañaga](modèles/modèle-d-enregistrement-de-décision-pour-les-décisions-techniques-importantes/)

Exemples :

- [Framework CSS](exemples/framework-css/)
- [Configuration par variables d’environnement](exemples/configuration-par-variables-d-environnement/)
- [Métriques, moniteurs, alertes](exemples/métriques-moniteurs-alertes/)
- [Microsoft Azure DevOps](exemples/microsoft-azure-devops/)
- [Monorepo ou multirepo](exemples/monorepo-ou-multirepo/)
- [Langages de programmation](exemples/langages-de-programmation/)
- [Stockage des secrets](exemples/stockage-des-secrets/)
- [Format d’horodatage](exemples/format-d-horodatage/)
- [Bien d’autres...](exemples/)

## Qu’est-ce qu’un enregistrement de décision d’architecture ?

Un **enregistrement de décision d’architecture** (architecture decision record, ADR) est un document qui consigne une décision d’architecture importante, ainsi que son contexte et ses conséquences.

Une **décision d’architecture** (architecture decision, AD) est un choix de conception logicielle qui répond à une exigence significative.

Un **journal des décisions d’architecture** (architecture decision log, ADL) est l’ensemble de tous les ADR créés et maintenus pour un projet (ou une organisation) donné.

Une **exigence architecturalement significative** (architecturally-significant requirement, ASR) est une exigence qui a un effet mesurable sur l’architecture d’un système logiciel.

Tout cela relève de la **gestion des connaissances en architecture** (architecture knowledge management, AKM).

L’objectif de ce document est de donner un aperçu rapide des ADR, de la façon de les créer et des endroits où trouver davantage d’informations.

Abréviations :

  * **AD** : décision d’architecture

  * **ADL** : journal des décisions d’architecture

  * **ADR** : enregistrement de décision d’architecture

  * **AKM** : gestion des connaissances en architecture

  * **ASR** : exigence architecturalement significative

## Comment commencer à utiliser les ADR

Pour commencer à utiliser les ADR, discutez avec vos coéquipiers des domaines suivants.

Identification des décisions :

  * Quel est le degré d’urgence et d’importance de l’AD ?

  * Doit-elle être prise maintenant, ou peut-elle attendre d’en savoir davantage ?

  * L’expérience personnelle et collective, ainsi que les méthodes et pratiques de conception reconnues, peuvent aider à identifier les décisions.

  * Idéalement, tenez une liste de décisions à prendre qui complète la liste des tâches du produit.

Prise de décision :

  * Il existe de nombreuses techniques de prise de décision, tant générales que propres à l’architecture logicielle, par exemple la cartographie de dialogue.

  * La prise de décision en groupe est un sujet de recherche actif.

Mise en œuvre et application des décisions :

  * Les AD sont utilisées dans la conception logicielle ; elles doivent donc être communiquées aux parties prenantes du système qui le financent, le développent et l’exploitent, et être acceptées par elles.

  * Les styles de codage architecturalement explicites et les revues de code centrées sur les préoccupations et décisions d’architecture sont deux pratiques connexes.

  * Les AD doivent aussi être (ré)examinées lors de la modernisation d’un système logiciel au fil de son évolution.

Partage des décisions (facultatif) :

  * De nombreuses AD se répètent d’un projet à l’autre.

  * Par conséquent, l’expérience acquise avec des décisions passées, bonnes comme mauvaises, peut constituer un atout précieux et réutilisable lorsqu’on applique une stratégie explicite de gestion des connaissances.

Documentation des décisions :

  * De nombreux modèles et outils existent pour consigner les décisions.

  * Voir les communautés agiles, par exemple les ADR de M. Nygard.

  * Voir les processus traditionnels d’ingénierie logicielle et de conception d’architecture, par exemple les mises en page de tableaux suggérées par IBM UMF et par Tyree et Akerman de CapitalOne.

Pour en savoir plus :

  * Les étapes ci-dessus sont reprises de l’article de Wikipédia sur la [décision architecturale](https://en.wikipedia.org/wiki/Architectural_decision)

## Comment commencer à utiliser les ADR avec des outils

- [MySpec](https://myspec.dev) — Plateforme automatisée de spécification et de décision d’architecture qui structure la constitution du projet, l’architecture technique et les ADR en Markdown propre, servi via MCP.

Vous pouvez commencer à utiliser les ADR avec des outils de la manière qui vous convient.

Par exemple :

  * Si vous aimez utiliser Google Drive et l’édition en ligne, vous pouvez créer un Google Doc ou un Google Sheet.

  * Si vous aimez utiliser le contrôle de version du code source, comme git, vous pouvez créer un fichier pour chaque ADR.

  * Si vous aimez utiliser des outils de planification de projet, comme Atlassian Jira, vous pouvez utiliser le suivi de planification de l’outil.

  * Si vous aimez les wikis, comme MediaWiki, vous pouvez créer un wiki d’ADR.

## Comment commencer à utiliser les ADR avec git

Si vous aimez utiliser le contrôle de version git, voici comment nous aimons commencer à utiliser les ADR avec git pour un projet logiciel typique doté de code source.

Créez un répertoire pour les fichiers ADR :

```sh
$ mkdir adr
```

Pour chaque ADR, créez un fichier texte, par exemple `choose-database.md` :

```sh
$ vi choose-database.md
```

Écrivez dans l’ADR ce que vous voulez. Consultez les modèles de ce dépôt pour vous inspirer.

Validez (commit) l’ADR dans votre dépôt git.

## Compétences Claude Code pour les ADR

Ce dépôt fournit deux compétences (skills) [Claude Code](https://claude.com/claude-code) dans [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), afin qu’un agent de codage IA puisse rédiger et maintenir des ADR comme le recommande ce projet :

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — à usage général, pour quiconque rédige un ADR dans n’importe quel projet. Aide à décider si une décision nécessite un ADR, crée un répertoire `adr/` ou `decisions/`, nomme le fichier, choisit un modèle parmi les onze squelettes fournis et rédige de solides sections Contexte/Décision/Conséquences.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — spécifiquement pour les mainteneurs de ce dépôt. Documente l’organisation du dépôt, la convention de miroir entre README et locales, et les étapes exactes pour ajouter un nouveau modèle, exemple ou lien d’outil.

Pour utiliser une compétence, copiez son dossier dans `.claude/skills/` à la racine du dépôt sur lequel vous travaillez (ou dans `~/.claude/skills/` pour la rendre disponible dans tous les projets), puis demandez à Claude Code de rédiger ou de relire un ADR.

## Conventions de nommage des fichiers

Si vous choisissez de créer vos ADR avec des fichiers texte ordinaires, vous voudrez peut-être définir votre propre convention de nommage des fichiers ADR.

Nous préférons une convention de nommage des fichiers qui suit un format précis.

Exemples :

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Notre convention de nommage des fichiers :

  * Le nom comporte une locution verbale à l’impératif présent. Cela facilite la lecture et correspond à notre format de messages de commit.

  * Le nom utilise des minuscules et des tirets (comme ce dépôt). C’est un compromis entre lisibilité et facilité d’utilisation côté système.

  * L’extension est markdown. Cela peut être utile pour une mise en forme facile.

## Conseils pour rédiger de bons ADR

Caractéristiques d’un bon ADR :

* Justification (Rationale) : expliquez les raisons de prendre cette AD en particulier. Cela peut inclure le contexte (voir ci-dessous), les avantages et inconvénients des différents choix possibles, des comparaisons de fonctionnalités, des analyses coûts-avantages, et plus encore.

* Spécifique (Specific) : chaque ADR doit porter sur une seule AD, pas sur plusieurs.

* Horodatage (Timestamps) : indiquez quand chaque élément de l’ADR a été rédigé. C’est particulièrement important pour les aspects susceptibles d’évoluer dans le temps, comme les coûts, les calendriers, le passage à l’échelle, etc.

* Immuable (Immutable) : ne modifiez pas les informations existantes d’un ADR. Amendez plutôt l’ADR en ajoutant de nouvelles informations, ou remplacez-le en créant un nouvel ADR.

Caractéristiques d’une bonne section « Contexte » dans un ADR :

* Expliquez la situation de votre organisation et ses priorités métier.

* Incluez la justification et les considérations fondées sur la composition sociale et les compétences de vos équipes.

* Incluez les avantages et inconvénients pertinents, et décrivez-les dans des termes qui correspondent à vos besoins et à vos objectifs.

Caractéristiques d’une bonne section « Conséquences » dans un ADR :

* Expliquez ce qui découle de la prise de décision. Cela peut inclure les effets, les résultats, les livrables, les suites à donner, et plus encore.

* Incluez des informations sur les ADR ultérieurs. Il est relativement courant qu’un ADR entraîne la nécessité d’autres ADR, par exemple lorsqu’un ADR fait un grand choix d’ensemble qui crée à son tour le besoin de décisions plus petites.

* Incluez les processus de revue après action. Il est habituel que les équipes revoient chaque ADR un mois plus tard, afin de comparer les informations de l’ADR avec ce qui s’est passé en pratique, pour apprendre et progresser.

Un nouvel ADR peut remplacer un ADR précédent :

* Lorsqu’une AD est prise qui remplace ou invalide un ADR précédent, un nouvel ADR doit être créé

## Modèles d’exemple d’ADR

Modèles d’exemple d’ADR que nous avons rassemblés sur le web :

- [Modèle d’ADR de Michael Nygard](modèles/modèle-d-enregistrement-de-décision-de-michael-nygard/) (simple et populaire)

- [Modèle d’ADR de Jeff Tyree et Art Akerman](modèles/modèle-d-enregistrement-de-décision-de-jeff-tyree-et-art-akerman/) (plus sophistiqué)

- [Modèle d’ADR pour le motif Alexandrian](modèles/modèle-d-enregistrement-de-décision-pour-le-patron-alexandrin/) (simple, avec des précisions sur le contexte)

- [Modèle d’ADR pour un dossier d’affaires](modèles/modèle-d-enregistrement-de-décision-pour-une-analyse-de-rentabilité/) (plus orienté MBA, avec coûts, SWOT et davantage d’opinions)

- [Modèle d’ADR du projet Markdown Any Decision Records (MADR)](modèles/modèle-d-enregistrement-de-décision-du-projet-madr/) (version simple et version détaillée ; cette dernière met l’accent sur les options et leurs avantages et inconvénients)

- [Modèle d’ADR utilisant Planguage](modèles/modèle-d-enregistrement-de-décision-avec-planguage/) (plus orienté assurance qualité)

- [Modèle pour les décisions techniques importantes (ITD) d’Ignacio Larrañaga](modèles/modèle-d-enregistrement-de-décision-pour-les-décisions-techniques-importantes/) (léger et centré sur la décision, optimisé pour une revue rapide par la direction)

## Conseils de travail d’équipe pour les ADR

Si vous envisagez d’utiliser des enregistrements de décision avec votre équipe, voici quelques conseils que nous avons appris en travaillant avec de nombreuses équipes.

Vous avez l’occasion de guider vos coéquipiers en discutant ensemble du « pourquoi » plutôt qu’en imposant le « quoi ». Par exemple, les enregistrements de décision sont un moyen pour les équipes de mieux réfléchir et de mieux communiquer ; ils n’ont aucune valeur s’ils ne sont qu’une formalité administrative imposée après coup.

Certaines équipes préfèrent de loin le nom « décisions » à l’abréviation « ADR ». Lorsque certaines équipes utilisent « decisions » comme nom de répertoire, c’est comme si une ampoule s’allumait, et l’équipe se met à y déposer davantage d’informations, comme des décisions relatives aux fournisseurs, à la planification, au calendrier, etc. Tous ces types d’information peuvent utiliser le même modèle. Notre hypothèse est que les gens apprennent plus vite avec des mots (« décisions ») qu’avec des abréviations (« ADR »), qu’ils sont plus motivés pour rédiger des documents de travail en cours lorsque le mot « enregistrement » est retiré, et aussi que certains développeurs et certains managers n’aiment pas le mot « architecture ».

En théorie, l’immuabilité est idéale. En pratique, la mutabilité a mieux fonctionné pour nos équipes. Nous insérons les nouvelles informations dans l’ADR existant, avec un horodatage et une note précisant que l’information est arrivée après la décision. Ce type d’approche mène à un « document vivant » que nous pouvons tous mettre à jour. Les mises à jour typiques surviennent lorsque nous recevons des informations grâce à de nouveaux coéquipiers, à de nouvelles offres, aux résultats concrets de nos usages, ou après des changements ultérieurs chez des tiers, tels que les capacités des fournisseurs, les formules tarifaires, les contrats de licence, etc.

## Questions de travail d’équipe pour les ADR

### Qui peut créer un ADR ?

Envisagez des aspects comme des personnes précises, des rôles précis, des équipes précises ou des services précis ; envisagez aussi s’il existe des personnes, rôles, équipes ou services pouvant commander un ADR, c’est-à-dire en demander un qu’une autre personne rédigera.

Exemple de réponse : toute personne de notre organisation ayant lu la page README sur l’enregistrement de décision d’architecture peut proposer un ADR, c’est-à-dire qu’elle peut commencer à le rédiger et le partager avec l’équipe.

### Qu’est-ce qui justifie de lancer un ADR ?

Envisagez des aspects comme les méthodes de travail des équipes de votre organisation, la structure de votre système logiciel, la coordination entre équipes, la maintenabilité à long terme, les interfaces externes, les personnes que vous voulez faire bénéficier, etc.

Exemple de réponse : nous voulons créer un ADR lorsque nous voulons que les futurs développeurs comprennent le « pourquoi » de ce que nous faisons.

### Qu’est-ce qui justifie de ne pas lancer d’ADR ?

Envisagez des aspects comme les décisions qui ne concernent pas l’architecture, ou qui sont minimes, par exemple à risque minimal, autonomes ou limitées à un seul développeur, ou qui sont déjà entièrement couvertes ailleurs, par exemple par des normes, des politiques ou de la documentation, ou qui sont temporaires, comme des solutions de contournement, des preuves de concept ou des expériences.

Exemple de réponse : nous voulons nous passer d’ADR lorsqu’une décision est limitée en portée, en durée, en risque et en coût, ou est déjà couverte ailleurs.

### Quel est le cycle de vie d’un ADR ?

Envisagez des aspects comme le processus de création, le processus de recherche, le processus de décision, le processus de mise en œuvre et le processus de retrait. Envisagez comment suivre le cycle de vie de l’ADR dans le temps, par exemple comment faire passer l’ADR d’un état au suivant, et comment le communiquer aux parties prenantes.

Exemple de réponse : nous voulons qu’un ADR ait cinq étapes de cycle de vie : Initiation → Recherche → Évaluation → Mise en œuvre → Maintenance → Retrait.

### Quels sont les critères des étapes du cycle de vie d’un ADR ?

Envisagez des aspects comme les critères d’acceptation d’un ADR, c’est-à-dire : comment savez-vous qu’il est assez bon pour passer d’une étape du cycle de vie à la suivante ? Le problème est-il clairement formulé ? Les alternatives ont-elles été examinées ? Les compromis (trade-offs) sont-ils suffisamment compris et documentés ? Tout le contexte pertinent est-il en place ? Toutes les parties prenantes concernées sont-elles impliquées ? Tous les retours ont-ils été pris en compte ?

Exemple de réponse : nous voulons qu’un ADR soit soumis au vote des parties prenantes lorsque l’équipe active a 1) terminé sa recherche, 2) terminé son évaluation, 3) publié la proposition d’ADR aux parties prenantes avec une demande de commentaires et un délai d’une semaine, 4) intégré et traité tous les commentaires des parties prenantes.

### Quels rôles et responsabilités interviennent dans un ADR ?

Envisagez des rôles tels que proposant, chercheur, évaluateur, relecteur, approbateur, mainteneur, etc. Envisagez des responsabilités telles que la communication avec les parties prenantes, la garantie que les attentes sont satisfaites, le partage sur le site web ou l’intranet, et la revue périodique du travail, en particulier lorsque des changements pertinents surviennent.

Exemple de réponse : nous voulons que chaque ADR ait toujours une personne de contact principale, une personne de contact secondaire et une équipe responsable ; ceux-ci sont responsables des communications, des publications, de la maintenance, de la revue périodique au moins une fois par an et, le cas échéant, du retrait final.

### Comment la gouvernance intervient-elle dans un ADR ?

Envisagez des aspects comme les méthodes de travail de votre organisation, d’éventuels besoins spéciaux de conformité, par exemple sur le plan juridique ou des ressources humaines, et la manière dont vous voulez gérer consensus, conflit et escalade. Existe-t-il des domaines, des personnes ou des équipes qui peuvent avoir plus d’influence que d’autres sur un ADR, par exemple en pouvant l’approuver, voter dessus ou y opposer leur veto ?

Exemple de réponse : la gouvernance d’un ADR suit cet ordre de priorité : le PDG, le directeur technique (CTO), le directeur juridique (CLO), l’équipe qui met en œuvre un ADR, les experts de l’équipe les plus compétents sur l’ADD. Personne d’autre n’a de pouvoir de gouvernance, sauf mention contraire dans l’ADR.

### Quels principes interviennent dans un ADR ?

Envisagez des aspects comme les méthodes de travail de votre organisation, notamment avancer vite ou lentement, consensus ou conflit sur les décisions, préférences en matière de risque ou de sécurité, discussion publique ou privée, etc.

Exemple de réponse : nous appliquons les principes de leadership que sont le biais pour l’action, le désaccord suivi d’engagement (disagree-and-commit), des estimations à 70 % suffisamment bonnes pour les décisions facilement réversibles et facilement isolables, et des méthodes de travail publiques, à l’exception des informations confidentielles telles que décrites dans l’accord de confidentialité de notre organisation.

## Concepts de l’étape suivante pour les ADR

[Arc42](https://arc42.org/) répond de façon pragmatique à deux questions et peut être adapté à vos besoins. Que faut-il documenter/communiquer sur votre architecture ? Comment faut-il le documenter/communiquer ? Arc42 comprend des enregistrements de décision d’architecture ainsi que des conseils sur les objectifs, les contraintes, les contextes, la qualité, les risques, etc.

[Le modèle C4](https://c4model.com/) est une approche facile à apprendre et conviviale pour les développeurs de diagrammes d’architecture logicielle. C4 est un ensemble de diagrammes hiérarchiques pour le contexte, les conteneurs, les composants et le code, avec des diagrammes complémentaires pour le paysage système, la dynamique et le déploiement.

## Diagrammes, vues et points de vue d’architecture

Un diagramme d’architecture s’appelle une « vue d’architecture ».

Une « vue d’architecture » est une instance d’un « point de vue d’architecture ».

Un « point de vue d’architecture » cible un public précis ayant des préoccupations précises.

Exemples de points de vue, de vues et de diagrammes d’architecture :

- Capacités métier

- Processus métier de haut niveau

- [Flux de valeur](https://en.wikipedia.org/wiki/Value_stream)

- Fonctions logicielles associées aux composants applicatifs

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Diagramme de contexte (TO-BE / AS-IS)

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Diagramme de conteneurs (TO-BE / AS-IS)

- [Diagramme entité-relation](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) pour associer les entités de données aux composants applicatifs

- [Diagrammes de séquence](https://en.wikipedia.org/wiki/Sequence_diagram) pour décrire les flux fonctionnels au sein des systèmes et pour les intégrations

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagrammes pour décrire les flux de données entre composants applicatifs

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagrammes pour décrire les processus métier / scénarios utilisateur

- [Gestion des identités et des accès](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) diagrammes

- [Contrôle d’accès basé sur les rôles](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) diagrammes avec les rôles par composant applicatif

- [Contrôle d’accès basé sur les attributs](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) diagrammes avec les attributs par composant applicatif

- Diagrammes de confidentialité

Diagrammes associés :

- Un diagramme de cas d’utilisation présente les cas d’utilisation à la direction/aux clients ; il précède les exigences, qui précèdent l’architecture logicielle.

- Un diagramme de déploiement montre le matériel/les ordinateurs physiques sur lesquels les composants logiciels sont déployés.
- Un diagramme de flux de données montre comment les données circulent dans le système et sont transformées.
- Un diagramme de séquence sert à montrer comment des protocoles comme HTTP fonctionnent sur un axe temporel.

- Un diagramme d’activité représente le flux de travail des activités qu’exécute un système logiciel, comme une IA de PNJ.

## Fonctions d’aptitude pour des décisions sous forme de code

Les fonctions d’aptitude (fitness functions) sont des vérifications automatisées et objectives, écrites en code de programmation, qui contrôlent que les décisions sont respectées.

- Les fonctions d’aptitude rendent les décisions testables et vérifiables.

- Les fonctions d’aptitude pour les décisions peuvent grandement faciliter l’assurance qualité, les processus réglementaires et les objectifs de gouvernance.

### Comment les fonctions d’aptitude se rattachent aux décisions

Un enregistrement de décision documente la décision, tandis qu’une fonction d’aptitude la garantit.

- Exemple de décision : nous utilisons l’event sourcing pour les exigences d’audit.

- Exemple de fonction d’aptitude : nous utilisons le serveur d’intégration continue pour vérifier que tous les changements d’état doivent produire des événements.

### Pourquoi les fonctions d’aptitude aident les décisions

Mesures objectives : les fonctions d’aptitude réussissent ou échouent, de sorte que le travail est visible et clair.

Usage continu : les fonctions d’aptitude sont vos règles vivantes, exécutées à chaque commit et à chaque build.

Confiance pour refactoriser : les fonctions d’aptitude détectent automatiquement les erreurs dans les règles de décision.

Gouvernance évolutive : les fonctions d’aptitude garantissent les normes sans créer de goulots d’étranglement.

### Les fonctions d’aptitude peuvent-elles utiliser l’IA ?

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

### Tests unitaires d’architecture

[ArchUnit](https://www.archunit.org/) : vérifie les règles d’architecture du code Java à l’aide de n’importe quel framework de tests unitaires Java ordinaire.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS) : vérifie les règles d’architecture du code TypeScript et JavaScript à l’aide de Jest, Vitest, Jasmine, etc.

## Garde-fous de décision pour les pull requests

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
fait apparaître automatiquement les bons enregistrements de décision au bon moment, c’est-à-dire lorsqu’un
développeur modifie activement le code que ces décisions couvrent. Au lieu d’espérer que les développeurs
lisent un dossier de documents avant de fusionner, le contexte pertinent apparaît directement dans la pull request.

Cela fonctionne pour tout type d’enregistrement de décision : décisions d’architecture, de données, de conformité, cliniques et médicales, de sécurité, etc.

Fonctionne avec n’importe quel système de CI (GitLab, Jenkins, CircleCI) et comme hook de pre-commit.
Open source. Licence MIT.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) est une GitHub
Action qui fait échouer une pull request lorsque des chemins de code surveillés changent sans qu’un
enregistrement de décision d’architecture soit ajouté ou mis à jour. Les dérogations sont explicites : une ligne
`ADR-Exempt:` accompagnée d’une raison franchit la barrière et est inscrite dans le résumé du job. Indépendant des modèles, sans dépendances. Open source. Licence MIT.

## Pour plus d’informations

Introduction :

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Modèles :

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Approfondissement :

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - leçon mensuelle gratuite d’architecture logicielle

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Outils :

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Conseils propres à des entreprises :

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Exemples :

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Vidéos :

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcasts :

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Livres :

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

Voir aussi :

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Un format YAML/JSON indépendant des fournisseurs et lisible par machine pour représenter les décisions avec raisonnement explicite, hypothèses, état cognitif et compromis. Complète les ADR en ajoutant un raisonnement structuré et validable à la documentation des décisions.
