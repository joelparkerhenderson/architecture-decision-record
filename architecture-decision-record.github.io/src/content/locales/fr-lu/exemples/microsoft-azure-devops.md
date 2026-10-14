# Microsoft Azure DevOps

Sommaire :

* [Résumé](#résumé)
  * [Question](#question)
  * [Décision](#décision)
  * [État](#état)
* [Détails](#détails)
  * [Hypothèses](#hypothèses)
  * [Contraintes](#contraintes)
  * [Positions](#positions)
  * [Argument](#argument)
  * [Implications](#implications)
* [Connexe](#connexe)
  * [Décisions connexes](#décisions-connexes)
  * [Exigences connexes](#exigences-connexes)
  * [Artefacts connexes](#artefacts-connexes)
  * [Principes connexes](#principes-connexes)
* [Notes](#notes)
  * [Microsoft Devops CI : une aventure insatisfaisante](#microsoft-devops-ci--une-aventure-insatisfaisante)
  * [Points saillants de la discussion sur Hacker News](#points-saillants-de-la-discussion-sur-hacker-news)
  * [MVP du développement Windows](#mvp-du-développement-windows)
  * [Résumé d’Edward Thomson (PM Azure)](#résumé-dedward-thomson-pm-azure)


## Résumé


### Question

Nous voulons utiliser le devops pour construire, intégrer, déployer et héberger nos projets. Nous envisageons Microsoft Azure DevOps.

  * Nous voulons que l’expérience développeur soit rapide et fiable, tant pour la mise en place du devops, p. ex. la configuration, que pour l’usage continu, p. ex. des temps de build rapides.
  
  * Nous voulons envisager d’utiliser Microsoft Azure dans son ensemble, pour héberger les applications du projet, les bases de données, etc.


### Décision

Décision contre Microsoft Azure DevOps.


### État

Décidé. Ouverts à un réexamen si et quand de nouvelles informations importantes arriveront.


## Détails


### Hypothèses

Toutes les hypothèses devops habituelles, comme dans le livre Accelerate.

  * Des builds rapides sont une aide importante. Cela accélère les boucles de rétroaction.

  * Nous pouvons remplacer ou ajouter des éléments provenant d’autres fournisseurs, c’est-à-dire que nous pouvons vouloir apporter nos serveurs de build à plus haute vitesse, ou utiliser le système de contrôle de version de notre choix, ou nous coordonner avec un serveur d’intégration continue auto-hébergé.
  
  * Une facilité d’utilisation rationalisée est une aide importante, pour l’expérience développeur, et par ricochet pour des domaines subtils comme la cohérence, la clarté, la sécurité et la facilité de la courbe d’apprentissage.

  * Quand quelque chose est cassé ou problématique, nous voulons un moyen efficace de signaler le problème. C’est particulièrement important pour tout problème lié à la sécurité.


### Contraintes

Aucune connue. Azure a publié l’engagement de bien s’entendre avec des outils externes.


### Positions

Nous avons envisagé Microsoft Azure Devops par rapport à AWS, qui est le fournisseur en place.

Nous avons expérimenté avec Azure DevOps, Azure Pipelines, Azure Repo et le démarrage d’un nouveau serveur Azure via Terraform.

Nous avons expérimenté l’obtention d’assistance auprès de représentants de Microsoft.

Nous avons recueilli des informations auprès de pairs sur des blogs et sur Hacker News.


### Argument

Azure DevOps annonce un excellent ensemble d’offres, mais elles ne tiennent pas leurs promesses, elles ne fonctionnent pas bien ensemble, et l’assistance est médiocre.

Notre expérience de première main :

  * La configuration d’Azure est un fouillis d’interfaces utilisateur, dont certaines recoupent les comptes Microsoft et d’autres non. P. ex. il y a une connexion Azure, une connexion Microsoft.com, une connexion Live.com, etc., et toutes sont en jeu simultanément.

  * Nous avons rencontré un problème de sécurité mineur pendant la configuration, et n’avons trouvé aucune résolution. Nous avons essayé de nombreuses façons de le signaler, à de nombreux représentants de Microsoft, sans succès. Nous l’avons signalé avec succès à la sécurité de Microsoft, qui a répondu won't fix (ne sera pas corrigé).

  * La documentation est souvent soit erronée, soit périmée. Au moins une partie de cela est due au mauvais moteur de recherche de Microsoft, et une autre au SEO médiocre.
  
  * La configuration de Terraform est bien documentée et fonctionne. Cependant, la prise en charge de Terraform est faible par rapport à AWS, parce que Microsoft construit des relations commerciales avec des fournisseurs pour fournir des exemples de configuration Terraform enchaînés.

Les expériences de nos pairs :

  * Après avoir fait notre propre évaluation à l’aveugle, nous avons cherché des expériences de pairs. Ce que nous avons trouvé a confirmé nos expériences.

  * Des pairs ont signalé des problèmes supplémentaires avec les temps de build, et des problèmes avec l’utilisation de son propre serveur de build. Ces problèmes sont nettement plus graves que les problèmes d’interface, parce que faire des builds est la finalité première d’une chaîne de build, et nous comptons en faire beaucoup par jour.

  * Nous avons constaté une excellente participation des coéquipiers d’Azure dans les espaces de discussion. Bravo à Microsoft pour cela. Nous sommes particulièrement impressionnés par Edward Thomson, PM et développeur Azure, pour sa participation, sa franchise et ses explications techniques.


### Implications

Choisir Microsoft Azure DevOps semble susceptible d’être plus coûteux (~3x) en temps et en argent que de ne pas choisir Azure.


## Connexe


### Décisions connexes

Si nous choisissons Azure DevOps, il existe de nombreuses offres connexes, dont Azure Repo, Azure Pipeline, etc. Nous pensons que, si nous choisissons Azure Devops, cela peut faciliter l’utilisation de davantage de capacités Azure, ou rendre plus difficile l’utilisation des capacités d’autres fournisseurs.

Nous pensons que Microsoft réalise de grands progrès en matière d’expérience développeur, et nous voyons Microsoft procéder à de grandes acquisitions d’outils pour développeurs (p. ex. GitHub) et de dépendances (p. ex. Citus).

Si nous choisissons Azure DevOps, nous pourrions vouloir mettre l’accent sur le choix des offres issues d’acquisitions de Microsoft, et nous pourrions aussi vouloir aborder ces offres acquises avec plus de soin/d’évaluation en raison d’un éventuel rejet de greffe, p. ex. le risque de départ du personnel.


### Exigences connexes

Nous voulons des temps de build très rapides. Nous acceptons de payer une prime élevée pour cela. C’est parce que nous voulons itérer très vite.

Nous voulons une fiabilité très élevée. Nous acceptons de payer une prime élevée pour cela. C’est parce que nous testons des cas d’usage à forte valeur, notamment des transactions financières, des transactions confidentielles, etc.

Nos 4 principaux KPI devops comprennent le temps moyen de rétablissement, qui exige des builds rapides et une grande fiabilité.


### Artefacts connexes

Nous voulons que le système de build produise des artefacts utilisables dans d’autres systèmes, comme Artifactory.


### Principes connexes

Facilement réversible. Nous pouvons évaluer Azure DevOps en parallèle avec AWS, le fournisseur en place.


## Notes


### Microsoft Devops CI : une aventure insatisfaisante

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Article de blog.

« En tant que développeur de logiciels, je sais par expérience directe combien il est difficile de construire rapidement et à moindre coût des produits de qualité. C’est un art que nous réussissons parfois, et que d’autres fois dégénère en quelque chose qui ressemble au site gouvernemental de santé de l’ère Obama. Notre niveau de contrôle sur le produit final varie, et le blâme de l’échec retombe souvent sur les mauvaises personnes de la hiérarchie décisionnelle. Azure DevOps de Microsoft (anciennement Visual Studio Team Services), malgré de clairement bonnes intentions, est une tempête parfaite de mauvaises décisions et d’une exécution médiocre. »


### Points saillants de la discussion sur Hacker News

https://news.ycombinator.com/item?id=18983586

« Nous utilisons Azure DevOps intensivement dans mon travail et, après avoir utilisé GitHub, Gitlab, des solutions auto-hébergées, Jenkins, TeamCity... Azure DevOps arrive bon dernier. »

« L’interface utilisateur est terriblement maladroite partout. Le pire pour moi, ce sont les demandes de fusion (pull requests). Il est incroyablement difficile de travailler avec d’autres personnes sur une pull request. Je ne peux même pas pointer "un" problème particulier : pour nous, c’est cassé partout. »

« Azure Devops est quelque chose que je voudrais adorer. L’interface change sans cesse, mais ne corrige pas les bogues sous-jacents qui existent depuis une éternité. »

« Les outils ne sont pas bien intégrés, l’interface est vraiment lente, il n’y a pas de vue tableau de bord des pull requests actives, des builds, des versions, etc. pour mes dépôts favoris. Les temps de build/déploiement sont d’une lenteur démente. »

« Nous avons aussi essayé d’utiliser Azure Boards (éléments de travail, tableaux, backlogs, etc.). Aïe. C’est un fouillis complet d’interface faite d’idées décousues. Au lieu de bien implémenter une seule chose, ils en ont implémenté deux douzaines de façon lamentable. »


### MVP du développement Windows

Je suis MVP du développement Windows. J’ai l’impression de devoir assumer une part de responsabilité pour ne pas avoir été plus bruyant au sujet de ces problèmes. Mais je dois dire que je suis déçu d’apprendre que vous êtes « surpris » par les problèmes d’expérience utilisateur. J’ai dit à vos équipes que l’expérience utilisateur est épouvantable (p. ex. dès avant le lancement) et j’ai continué d’entendre en réponse « on sait, on est en train de corriger ». Je vais commencer à formaliser les retours et à les faire remonter par les canaux, restez à l’écoute. Je suis aussi local (Bellevue), et j’adorerais venir essayer de mettre en pipeline notre application open source .net/wpf/uwp relativement simple. Je soupçonne que cela nous ouvrira les yeux à tous les deux.

Quelques exemples :

* On ne peut pas construire un pipeline avec un dépôt git contenant des sous-modules

* J’ai trouvé impossible de modifier le PATH pour certains outils personnalisés

* L’expérience New Pipeline n’a pas beaucoup de sens, les nouveaux utilisateurs qui cliquent un peu partout finiront par atterrir sur la mauvaise documentation.


### Résumé d’Edward Thomson (PM Azure)

J’ai écrit le code qui fusionne vos pull requests. Program Manager chez Microsoft pour Azure DevOps ; auparavant ingénieur logiciel sur les outils de contrôle de version chez GitHub, Microsoft et SourceGear.

https://www.edwardthomson.com/

Co-mainteneur de libgit2. https://libgit2.github.io

Co-animateur de All Things Git, le podcast sur Git. https://www.allthingsgit.com/

Curateur de Developer Tools Weekly, une infolettre sur les outils de développement. https://developertoolsweekly.com/
