# Modèle d’enregistrement de décision d’arc42

<https://arc42.org/overview>

## 1. Introduction et objectifs

Brève description des exigences, des forces motrices, extrait (ou résumé) des exigences. Les trois (cinq au maximum) objectifs de qualité principaux de l’architecture qui ont la plus haute priorité pour les principales parties prenantes. Un tableau des parties prenantes importantes avec leurs attentes à l’égard de l’architecture.

## 1.1 Vue d’ensemble des exigences

### Contenu

Brève description des exigences fonctionnelles, des forces motrices, extrait (ou résumé) des exigences. Liens vers les documents d’exigences (qui existent, on l’espère), avec l’indication de l’endroit où les trouver. 

### Motivation

Du point de vue des utilisateurs finaux, un système est créé ou modifié pour mieux soutenir une activité métier et/ou améliorer la qualité. 

### Forme

Courte description textuelle, probablement au format tabulaire de cas d’usage. Si des documents d’exigences existent, cette vue d’ensemble doit y renvoyer.

Gardez ces extraits aussi courts que possible. Équilibrez la lisibilité de ce document avec la redondance potentielle par rapport aux documents d’exigences. 

## 1.2 Objectifs de qualité

### Contenu

Les trois (cinq au maximum) objectifs de qualité principaux de l’architecture dont la réalisation est de la plus haute importance pour les principales parties prenantes. Nous parlons bien d’objectifs de qualité de l’architecture. Ne les confondez pas avec les objectifs du projet. Ils ne sont pas nécessairement identiques. La norme ISO 25010 offre un bon aperçu des sujets d’intérêt potentiels.

### Motivation

Vous devez connaître les objectifs de qualité de vos parties prenantes les plus importantes, car ils influenceront les décisions d’architecture fondamentales. Soyez très concret sur ces qualités, évitez les mots à la mode. Si vous, en tant qu’architecte, ne savez pas comment la qualité de votre travail sera jugée …

### Forme

Un tableau des objectifs de qualité les plus importants et de scénarios concrets, classés par priorité.

## 1.3 Parties prenantes

### Contenu

Vue d’ensemble explicite des parties prenantes du système, c’est-à-dire toutes les personnes, tous les rôles ou toutes les organisations qui

- doivent connaître l’architecture

- doivent être convaincus de l’architecture

- doivent travailler avec l’architecture ou avec le code

- ont besoin de la documentation de l’architecture pour leur travail

- doivent prendre des décisions concernant le système ou son développement

### Motivation

Vous devez connaître toutes les parties impliquées dans le développement du système ou affectées par celui-ci. Sinon, vous risquez de mauvaises surprises plus tard dans le processus de développement. Ces parties prenantes déterminent l’étendue et le niveau de détail de votre travail et de ses résultats.

### Forme

Tableau avec les noms des rôles, les noms des personnes et leurs attentes à l’égard de l’architecture et de sa documentation.

## 2. Contraintes

Tout ce qui contraint les équipes dans leurs décisions de conception et de mise en œuvre ou dans leurs décisions relatives aux processus connexes. Peut parfois dépasser les systèmes individuels et valoir pour des organisations et des entreprises entières.

### Contenu

Toute exigence qui limite la liberté des architectes logiciels dans leurs décisions de conception et de mise en œuvre ou dans leurs décisions relatives au processus de développement. Ces contraintes dépassent parfois les systèmes individuels et valent pour des organisations et des entreprises entières.

### Motivation

Les architectes doivent savoir exactement où ils sont libres dans leurs décisions de conception et où ils doivent respecter des contraintes. Les contraintes doivent toujours être traitées ; elles peuvent toutefois être négociables.

### Forme

Tableaux simples de contraintes avec explications. Si nécessaire, vous pouvez les subdiviser en contraintes techniques, contraintes organisationnelles et politiques, et conventions (p. ex. lignes directrices de programmation ou de gestion de versions, conventions de documentation ou de nommage)

## 3. Contexte et portée

Délimite votre système par rapport à ses partenaires de communication (externes) (systèmes voisins et utilisateurs). Spécifie les interfaces externes. Présenté d’un point de vue métier/domaine (toujours) ou d’un point de vue technique (facultatif)

### Contenu

La portée et le contexte du système, comme son nom l’indique, délimitent votre système (c’est-à-dire votre portée) par rapport à tous ses partenaires de communication (systèmes voisins et utilisateurs, c’est-à-dire le contexte de votre système). Il spécifie ainsi les interfaces externes.

Si nécessaire, distinguez le contexte métier (entrées et sorties propres au domaine) du contexte technique (canaux, protocoles, matériel).

### Motivation

Les interfaces de domaine et les interfaces techniques avec les partenaires de communication comptent parmi les aspects les plus critiques de votre système. Assurez-vous de les comprendre parfaitement.

### Forme

- Divers diagrammes de contexte

- Listes de partenaires de communication et de leurs interfaces.

## 3.1 Contexte métier

### Contenu

Spécification de tous les partenaires de communication (utilisateurs, systèmes informatiques, …) avec des explications sur les entrées et sorties ou interfaces propres au domaine. Vous pouvez éventuellement ajouter des formats propres au domaine ou des protocoles de communication.

### Motivation

Toutes les parties prenantes doivent comprendre quelles données sont échangées avec l’environnement du système.

### Forme

Toutes sortes de diagrammes qui montrent le système comme une boîte noire et spécifient les interfaces de domaine avec les partenaires de communication.

Vous pouvez aussi (ou en plus) utiliser un tableau. Le titre du tableau est le nom de votre système ; les trois colonnes contiennent le nom du partenaire de communication, les entrées et les sorties.

## 3.2 Contexte technique

### Contenu

Interfaces techniques (canaux et supports de transmission) reliant votre système à son environnement. En outre, une correspondance entre les entrées/sorties propres au domaine et les canaux, c’est-à-dire une explication de quel canal utilise quelle E/S.

### Motivation

De nombreuses parties prenantes prennent des décisions d’architecture fondées sur les interfaces techniques entre le système et son contexte. Ce sont notamment les concepteurs d’infrastructure ou de matériel qui décident de ces interfaces techniques.

### Forme

Par exemple, un diagramme de déploiement UML décrivant les canaux vers les systèmes voisins, accompagné d’un tableau de correspondance montrant les relations entre les canaux et les entrées/sorties.

## 4. Stratégie de solution

Résumé des décisions fondamentales et des stratégies de solution qui façonnent l’architecture. Peut inclure la technologie, la décomposition de haut niveau, les approches pour atteindre les principaux objectifs de qualité et les décisions organisationnelles pertinentes.

### Contenu

Un bref résumé et une explication des décisions fondamentales et des stratégies de solution qui façonnent l’architecture du système. Celles-ci comprennent

- les décisions technologiques

- les décisions sur la décomposition de haut niveau du système, p. ex. l’utilisation d’un patron d’architecture ou d’un patron de conception

- les décisions sur la manière d’atteindre les objectifs de qualité clés

- les décisions organisationnelles pertinentes, p. ex. le choix d’un processus de développement ou la délégation de certaines tâches à des tiers.

### Motivation

Ces décisions constituent les pierres angulaires de votre architecture. Elles sont le fondement de nombreuses autres décisions détaillées ou règles de mise en œuvre.

### Forme

Gardez brève l’explication de ces décisions clés.

Motivez ce que vous avez décidé et pourquoi vous l’avez décidé ainsi, en vous appuyant sur votre énoncé de problème, les objectifs de qualité et les contraintes clés. Renvoyez aux détails dans les sections suivantes (section 5 pour les détails structurels, section 8 pour les concepts transversaux).

Vous pouvez utiliser une liste d’approches de solution ou un tableau.

## 5. Vue des blocs de construction

Décomposition statique du système, abstractions du code source, présentées comme une hiérarchie de boîtes blanches (contenant des boîtes noires), jusqu’au niveau de détail approprié.

### Contenu

La vue des blocs de construction montre la décomposition statique du système en blocs de construction (modules, composants, sous-systèmes, classes, interfaces, paquets, bibliothèques, frameworks, couches, partitions, niveaux, fonctions, macros, opérations, structures de données, …) ainsi que leurs dépendances (relations, associations, …)

Cette vue est obligatoire pour toute documentation d’architecture. Par analogie avec une maison, c’est le plan d’étage.

### Motivation

Gardez une vue d’ensemble de votre code source en rendant sa structure compréhensible par l’abstraction.

Cela vous permet de communiquer avec vos parties prenantes à un niveau abstrait sans divulguer les détails de mise en œuvre.

### Forme

La vue des blocs de construction est une collection hiérarchique de boîtes noires et de boîtes blanches (voir la figure ci-dessous) et de leurs descriptions.

## 5.1 Boîte blanche du système global

Ici, vous décrivez la décomposition du système global à l’aide du modèle de boîte blanche suivant. Il contient

- un diagramme d’ensemble

- une motivation de la décomposition

- des descriptions en boîte noire des blocs de construction contenus. Pour cela, nous vous proposons des alternatives :

  - utiliser un tableau pour un aperçu court et pragmatique de tous les blocs de construction contenus et de leurs interfaces

  - utiliser une liste de descriptions en boîte noire des blocs de construction selon le modèle de boîte noire (voir ci-dessous). Selon l’outil que vous choisissez, cette liste pourrait être constituée de sous-chapitres (dans des fichiers texte), de sous-pages (dans un wiki) ou d’éléments imbriqués (dans un outil de modélisation).

  - (facultatif :) interfaces importantes qui ne sont pas expliquées dans les modèles de boîte noire d’un bloc de construction, mais qui sont très importantes pour comprendre la boîte blanche.

Comme il existe tant de façons de spécifier les interfaces, nous ne fournissons pas de modèle spécifique pour elles.

Dans le meilleur des cas, vous vous en sortirez avec des exemples ou de simples signatures.

## 5.2 Niveau 2

Ici, vous pouvez spécifier la structure interne de (certains) blocs de construction du niveau 1 sous forme de boîtes blanches.

Vous devez décider quels blocs de construction de votre système sont assez importants pour justifier une description aussi détaillée. Privilégiez la pertinence à l’exhaustivité. Spécifiez les blocs de construction importants, surprenants, risqués, complexes ou volatils. Laissez de côté les parties normales, simples, ennuyeuses ou standardisées de votre système

### 5.2.1 Boîte blanche du bloc de construction 1

Spécifie la structure interne du bloc de construction 1.

Utilisez le modèle de boîte blanche (voir ci-dessus).

## 6. Vue d’exécution

Comportement des blocs de construction sous forme de scénarios, couvrant les cas d’usage ou fonctionnalités importants, les interactions aux interfaces externes critiques, l’exploitation et l’administration, ainsi que le comportement en cas d’erreur et d’exception.

### Contenu

La vue d’exécution décrit le comportement concret et les interactions des blocs de construction du système sous forme de scénarios issus des domaines suivants :

- cas d’usage ou fonctionnalités importants : comment les blocs de construction les exécutent-ils ?

- interactions aux interfaces externes critiques : comment les blocs de construction coopèrent-ils avec les utilisateurs et les systèmes voisins ?

- exploitation et administration : lancement, démarrage, arrêt

- scénarios d’erreur et d’exception

Remarque : le principal critère de choix des scénarios possibles (séquences, flux de travail) est leur pertinence architecturale. Il n’est pas important de décrire un grand nombre de scénarios. Vous devriez plutôt documenter une sélection représentative.

### Motivation

Vous devez comprendre comment les (instances de) blocs de construction de votre système accomplissent leur tâche et communiquent à l’exécution. Vous consignerez principalement des scénarios dans votre documentation pour communiquer votre architecture aux parties prenantes moins disposées ou moins aptes à lire et comprendre les modèles statiques (vue des blocs de construction, vue de déploiement).

### Forme

Il existe de nombreuses notations pour décrire des scénarios, p. ex.


- liste numérotée d’étapes (en langage naturel)

- diagrammes d’activité ou organigrammes

- diagrammes de séquence

- BPMN ou EPC (chaînes de processus événementielles)

- machines à états

- etc.

## 6.n Scénario d’exécution n (1, 2, 3, etc.)

Insérez un diagramme d’exécution ou une description textuelle du scénario.

Insérez une description des aspects notables des interactions entre les instances de blocs de construction représentées dans ce diagramme.

## 7. Vue de déploiement

Infrastructure technique avec environnements, ordinateurs, processeurs, topologies. Correspondance entre les blocs de construction (logiciels) et les éléments d’infrastructure.

### Contenu

La vue de déploiement décrit :

- l’infrastructure technique utilisée pour exécuter votre système, avec des éléments d’infrastructure comme les emplacements géographiques, les environnements, les ordinateurs, les processeurs, les canaux et les topologies de réseau, ainsi que d’autres éléments d’infrastructure, et

- la correspondance entre les blocs de construction (logiciels) et ces éléments d’infrastructure.

Les systèmes sont souvent exécutés dans différents environnements, p. ex. environnement de développement, environnement de test, environnement de production. Dans de tels cas, vous devez documenter tous les environnements pertinents.

Documentez en particulier la vue de déploiement lorsque votre logiciel est exécuté comme un système distribué avec plus d’un ordinateur, processeur, serveur ou conteneur, ou lorsque vous concevez et construisez vos propres processeurs et puces matériels.

D’un point de vue logiciel, il suffit de recenser les éléments d’infrastructure nécessaires pour montrer le déploiement de vos blocs de construction. Les architectes matériels peuvent aller au-delà et décrire l’infrastructure avec le niveau de détail qu’ils ont besoin de consigner. 

### Motivation

Un logiciel ne fonctionne pas sans matériel. Cette infrastructure sous-jacente peut influencer, et influencera, votre système et/ou certains concepts transversaux. Vous devez donc connaître l’infrastructure.

### Forme

Le diagramme de déploiement de plus haut niveau figure peut-être déjà à la section 3.2 en tant que contexte technique, avec votre propre infrastructure comme UNE boîte noire. Dans cette section, vous zoomerez sur cette boîte noire à l’aide de diagrammes de déploiement supplémentaires.

- UML propose des diagrammes de déploiement pour exprimer cette vue. Utilisez-les, probablement avec des diagrammes imbriqués, lorsque votre infrastructure est plus complexe.

- Lorsque vos parties prenantes (matériel) préfèrent d’autres types de diagrammes plutôt que le diagramme de déploiement UML, laissez-les utiliser tout type capable de montrer les nœuds et les canaux de l’infrastructure.

## 7.1 Infrastructure, niveau 1

Décrivez (généralement par une combinaison de diagrammes, de tableaux et de texte) :

- la distribution de votre système sur plusieurs emplacements, environnements, ordinateurs, processeurs, .. ainsi que les connexions physiques entre eux

- la justification ou la motivation importante de cette structure de déploiement

- les caractéristiques de qualité et/ou de performance de l’infrastructure

- la correspondance entre les artefacts logiciels (blocs de construction) et les éléments de l’infrastructure

Pour plusieurs environnements ou déploiements alternatifs, veuillez copier cette section d’arc42 pour tous les environnements pertinents. **

## 7.2 Infrastructure, niveau 2

Ici, vous pouvez inclure la structure interne de (certains) éléments d’infrastructure du niveau 1.

Veuillez copier la structure du niveau 1 pour chaque élément choisi.

## 8. Concepts transversaux

Dans l’ensemble, les réglementations principales et les approches de solution pertinentes dans plusieurs parties (→ transversales) du système. Les concepts sont souvent liés à plusieurs blocs de construction. Incluez des sujets variés comme les modèles de domaine, les patrons et styles d’architecture, les règles d’utilisation de technologies spécifiques et les règles de mise en œuvre.

### Contenu

Cette section décrit les concepts transversaux (pratiques, patrons, réglementations ou idées de solution). Ces concepts sont souvent liés à plusieurs blocs de construction. Ils peuvent couvrir de nombreux sujets différents.

### Motivation

Les concepts forment la base de l’intégrité conceptuelle (cohérence, homogénéité) de l’architecture. Ils contribuent donc de manière importante à atteindre les qualités internes de votre système.

C’est l’endroit du modèle que nous avons prévu pour une spécification cohérente de ces concepts.

Beaucoup de ces concepts se rapportent à plusieurs de vos blocs de construction ou les influencent.

### Forme

La forme peut varier :

- des documents de concept avec n’importe quelle structure

- des exemples de mise en œuvre, en particulier pour les concepts techniques

- des extraits de modèles transversaux ou des scénarios utilisant les notations des vues d’architecture

### Structure de cette section

Ne choisissez que les sujets les plus nécessaires pour votre système et attribuez à chacun un titre de niveau 2 dans cette section (p. ex. 8.1, 8.2, etc.).

- N’ESSAYEZ PAS de couvrir tous les sujets du diagramme mentionné.

### Contexte

Certains sujets au sein des systèmes concernent souvent plusieurs blocs de construction, éléments matériels ou processus de développement. Il peut être plus facile de communiquer ou de documenter de tels sujets transversaux à un endroit central, plutôt que de les répéter dans la description des blocs de construction, des éléments matériels ou des processus de développement concernés.

Certains concepts peuvent concerner tous les éléments d’un système, d’autres ne seront pertinents que pour quelques-uns.

## 9. Décisions d’architecture

Décisions d’architecture importantes, coûteuses, critiques, de grande envergure ou risquées, avec leurs justifications.

### Contenu

Décisions d’architecture importantes, coûteuses, de grande envergure ou risquées, avec leurs justifications. Par « décisions », nous entendons le choix d’une alternative selon des critères donnés.

Utilisez votre jugement pour décider si une décision d’architecture doit être documentée ici, dans cette section centrale, ou s’il vaut mieux la documenter localement (p. ex. dans le modèle de boîte blanche d’un bloc de construction). Évitez les textes redondants. Renvoyez à la section 4, où vous avez déjà consigné les décisions les plus importantes de votre architecture.

### Motivation

Les parties prenantes de votre système doivent pouvoir comprendre et retracer vos décisions.

### Forme

- ADR (enregistrement de décision d’architecture) pour chaque décision importante

- liste ou tableau, classés par importance et conséquences, ou

- de façon plus détaillée, sous forme de sections séparées par décision

### Contexte (sur les ADR)

Des morceaux de documentation plus petits sont plus faciles à lire, à créer et à maintenir. En ce qui concerne les décisions d’architecture, les équipes de développement :

- connaissent souvent la décision, car elle est visible p. ex. dans le code source, mais

- ignorent la motivation qui la sous-tend (voir Nygard 2011)

Vous devriez donc documenter quelques décisions importantes avec leur motivation et leur raisonnement

### Notre proposition concernant les décisions

Conservez une collection de décisions architecturalement significatives, c’est-à-dire celles qui affectent la structure, les caractéristiques de qualité, les dépendances et interfaces importantes (en particulier externes) ou les techniques de construction (merci à Michael Nygard pour cette proposition).

## 10. Exigences de qualité

Exigences de qualité sous forme de scénarios, avec un arbre de qualité pour offrir une vue d’ensemble de haut niveau. Les objectifs de qualité les plus importants devraient avoir été décrits à la section 1.2 (objectifs de qualité).

### Contenu

Cette section contient toutes les exigences de qualité pertinentes.

Les plus importantes de ces exigences ont déjà été décrites à la section 1.2 (objectifs de qualité) ; elles ne doivent donc être que référencées ici. Dans cette section 10, vous devriez aussi consigner les exigences de qualité de moindre importance, qui ne créeront pas de risques élevés si elles ne sont pas pleinement atteintes (mais qui seraient souhaitables).

### Motivation

Comme les exigences de qualité auront beaucoup d’influence sur les décisions d’architecture, vous devez savoir quelles qualités sont réellement importantes pour vos parties prenantes, de manière spécifique et mesurable.

### Plus d’informations

Voir le modèle de qualité Q42, très complet, sur https://quality.arc42.org.

## 10.1 Vue d’ensemble des exigences de qualité

### Contenu

Un aperçu ou un résumé des exigences de qualité.

### Motivation

Nous rencontrons souvent des dizaines (voire des centaines) d’exigences de qualité détaillées. Dans cette section de vue d’ensemble, vous devriez essayer de les résumer, p. ex. en décrivant des catégories ou des sujets (comme le suggèrent ISO 25010:2023 ou Q42

Si ces descriptions résumées sont déjà précises, assez spécifiques et mesurables, vous pouvez omettre la section 10.2.

### Forme

Utilisez un tableau simple dont chaque ligne contient une catégorie ou un sujet et une brève description de l’exigence de qualité. Vous pouvez aussi utiliser une carte mentale pour structurer ces exigences de qualité.

Dans la littérature, l’idée d’un arbre d’attributs de qualité a également été décrite : il place le terme générique « qualité » à la racine et utilise un raffinement arborescent du terme « qualité ». [Bass+21] a introduit pour cela le terme « Quality Attribute Utility Tree ».

## 10.2 Scénarios de qualité

### Contenu

Les scénarios de qualité rendent les exigences de qualité concrètes et permettent de décider si elles sont satisfaites (au sens de critères d’acceptation). Veillez à ce que vos scénarios soient spécifiques et mesurables.

Deux types de scénarios sont particulièrement utiles :

- Les scénarios d’usage (aussi appelés scénarios applicatifs ou scénarios de cas d’usage) décrivent la réaction du système à l’exécution face à un certain stimulus. Cela inclut aussi les scénarios qui décrivent l’efficacité ou la performance du système. Exemple : le système réagit à la requête d’un utilisateur en une seconde.

- Les scénarios de changement décrivent l’effet souhaité d’une modification ou d’une extension du système ou de son environnement immédiat. Exemple : une fonctionnalité supplémentaire est mise en œuvre ou les exigences d’un attribut de qualité changent, et l’effort ou la durée du changement est mesuré.

### Forme

Les informations typiques des scénarios détaillés comprennent les éléments suivants :

Forme courte (privilégiée dans le modèle Q42) :

- Contexte/arrière-plan : quel type de système ou de composant, quel est l’environnement ou la situation ?

- Source/stimulus : qui ou quoi déclenche un comportement, une réaction ou une action.

- Métrique/critères d’acceptation : une réponse incluant une mesure ou une métrique

La forme longue des scénarios (privilégiée par le SEI et [Bass+21]) est plus détaillée et comprend les informations suivantes :

- ID du scénario : un identifiant unique pour le scénario.

- Nom du scénario : un nom court et descriptif pour le scénario.

- Source : l’entité (utilisateur, système ou événement) qui déclenche le scénario.

- Stimulus : l’événement ou la condition déclencheur que le système doit traiter.

- Environnement : le contexte opérationnel ou la condition dans lequel le système subit le stimulus.

- Artefact : les blocs de construction ou autres éléments du système affectés par le stimulus.

- Réponse : le résultat ou le comportement que le système affiche en réaction au stimulus.

- Mesure de la réponse : le critère ou la métrique selon lequel la réponse du système est évaluée.

### Voir aussi

Depuis janvier 2023, arc42 propose un modèle de qualité pragmatique, qui suggère d’étiqueter les exigences de qualité avec des hashtags ou des étiquettes comme #flexible, #efficient, #usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Risques et dette technique

Risques techniques ou dette technique connus. Quels problèmes potentiels existent au sein du système ou autour de lui ? Qu’est-ce qui rend l’équipe de développement malheureuse ?

### Contenu

Une liste des risques techniques ou des dettes techniques identifiés, classés par priorité

### Motivation

« La gestion des risques est la gestion de projet pour les adultes » (Tim Lister, Atlantic Systems Guild).

Ce devrait être votre devise pour la détection et l’évaluation systématiques des risques et des dettes techniques de l’architecture, dont les parties prenantes de la gestion (p. ex. chefs de projet, responsables produit) auront besoin dans le cadre de l’analyse globale des risques et de la planification des mesures.

### Forme

Liste de risques et/ou de dettes techniques, incluant probablement des mesures suggérées pour minimiser, atténuer ou éviter les risques ou réduire les dettes techniques.
