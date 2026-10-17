# Configuration par variables d’environnement

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


## Résumé


### Question

Nous voulons que nos applications soient configurables au-delà des artefacts, des binaires et du code source, de sorte qu’un même build puisse se comporter différemment selon son environnement de déploiement.

  * Pour y parvenir, nous voulons utiliser la configuration par variables d’environnement.

  * Nous voulons gérer la configuration à l’aide de fichiers que nous pouvons placer sous contrôle de version.

  * Nous voulons offrir un certain confort d’ergonomie au développeur, par exemple savoir ce qui peut être configuré et quelles sont les valeurs par défaut pertinentes.


### Décision

Choix de fichiers .env avec un fichier de valeurs par défaut et un fichier de schéma associés.


### État

Décidé. Ouverts à l’examen de nouvelles capacités au fur et à mesure qu’elles apparaissent.


## Détails


### Hypothèses

Nous privilégions la séparation du code applicatif et du code d’environnement. Nous supposons que l’application doit fonctionner différemment selon les environnements, comme un environnement de développement, un environnement de test, un environnement de démonstration, un environnement de production, etc.

Nous privilégions la pratique du secteur dite « application à 12 facteurs » (12 factor app) et plus encore la pratique connexe de l’« application à 15 facteurs » (15 factor app).

Beaucoup de nos projets précédents ont utilisé la convention d’un fichier `.env` ou d’un répertoire `.env` similaire. Il est courant de les garder hors du contrôle de version et d’utiliser une autre méthode pour les déployer, les versionner et les gérer.


### Contraintes

Nous voulons garder les secrets hors de notre système de contrôle de version (VCS) de gestion du code source (SCM).

Nous voulons viser la compatibilité avec les frameworks et bibliothèques logiciels populaires. Par exemple, Node dispose d’un module « dotenv » pour lire la configuration par variables d’environnement.


### Positions

Nous avons envisagé quelques approches :

  * Stocker la configuration dans l’application, par exemple dans un fichier `config.js`.

  * Stocker la configuration dans l’environnement, par exemple dans un fichier `.env`.

  * Récupérer la configuration depuis un emplacement connu, comme un serveur de licences.


### Argument

Nous avons retenu l’approche d’un fichier .env parce que :

  * Elle est populaire, y compris chez les experts.

  * Elle suit le patron des fichiers `.env`, que nos équipes ont utilisé avec succès de nombreuses fois sur de nombreux projets.

  * Elle est simple. Notamment, nous nous accommodons pour l’instant des compromis importants que nous voyons, comme l’absence de capacités d’audit par rapport à une approche de serveur de licences.


### Implications

Nous devons trouver un moyen de séparer la configuration par variables d’environnement qui est publique de toute gestion de secrets.


## Connexe


### Décisions connexes

Nous nous attendons à ce que toutes nos applications utilisent cette approche.

Nous prévoirons de mettre à niveau toutes nos applications qui utilisent une approche moins capable, comme le codage en dur dans un binaire ou dans le code source.

Nous conserverons en l’état toutes nos applications qui utilisent une approche plus capable, comme un serveur de licences.


### Exigences connexes

Nous ajouterons des capacités devops pour les fichiers, y compris des hooks, des tests et de l’intégration continue.

Nous devons former tous les coéquipiers développeurs à cette décision.



### Artefacts connexes

Chaque zone où nous déployons aura besoin de son propre fichier .env et de fichiers associés.


### Principes connexes

Facilement réversible.


## Notes


Exemple de fichier `.env` :

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Exemple de fichier `.env.defaults` :

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Exemple de fichier `.env.schema` avec seulement les clés :

```env
NAME
EMAIL
```
