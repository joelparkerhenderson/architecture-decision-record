# Stockage des secrets

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
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Résumé


### Question

Nous devons stocker des secrets, comme des mots de passe, des clés privées, des jetons d’authentification, etc.

Certains secrets sont orientés utilisateur. Par exemple, notre développeur veut pouvoir utiliser son téléphone mobile pour retrouver le mot de passe d’un service.

Certains secrets sont orientés système. Par exemple, notre chaîne de livraison continue doit pouvoir retrouver les identifiants de notre hébergement cloud.


### Décision

Bitwarden pour les secrets orientés utilisateur.

Vault by HashiCorp pour les secrets orientés système.


### État

Décidé. Nous sommes ouverts à de nouvelles alternatives au fur et à mesure de leur apparition.


## Détails


### Hypothèses

Pour cet objectif, et dans notre état actuel, nous accordons de la valeur à la commodité orientée utilisateur, comme des applications mobiles utilisables.

  * Nous voulons garantir un accès rapide et facile en déplacement, par exemple pour un développeur qui fait de l’ingénierie de fiabilité des systèmes en astreinte.

  * Nous voulons pouvoir partager certains secrets entre des personnes choisies, comme une équipe.

Nous ne cherchons pas à résoudre le cas d’un fournisseur unique, comme stocker tous les secrets exclusivement chez Amazon, Azure ou Google.

Nous ne voulons pas d’approches improvisées comme « retiens-le », « note-le sur un papier » ou « débrouille-toi pour le stocker à ta façon ».

Notre modèle de sécurité pour cet objectif s’accommode de l’utilisation de fournisseurs COTS (produits commerciaux sur étagère) réputés, comme les outils de gestion de mots de passe SaaS.


### Contraintes

Pour l’instant, nous voulons quelque chose de facile, c’est-à-dire sans code à écrire, sans serveur à installer, sans engagement majeur à prendre, sans nécessité de standardiser tout le monde.


### Positions

Nous avons envisagé :

1. Des gestionnaires de mots de passe sur étagère orientés utilisateur : LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG, etc.

2. Des gestionnaires de mots de passe COTS orientés système : AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Des approches orientées partage : utiliser un document Google partagé, ou un canal Slack partagé, ou un dossier réseau partagé, etc.

4. Des approches improvisées peu technologiques, comme mémoriser, écrire une note ou compter sur chaque utilisateur pour trouver sa propre approche.


### Argument

Bitwarden, LastPass, 1Password et Dashlane sont tous des produits commerciaux sur étagère.

  * Types de fonctionnalités similaires pour les utilisateurs, les équipes, les organisations, etc.

  * Capacité de bureau pour Windows et Mac, et capacité mobile pour Android et iOS.

  * Extensions de navigateur pour Chrome et Firefox, pour le remplissage automatique de formulaires, etc.

Bitwarden a deux avantages sur les autres :

  * Bitwarden est open source, ce qui signifie que la sécurité peut être examinée par des pairs et que l’entreprise est largement appréciée des développeurs axés sur la sécurité.

  * Des anecdotes de professionnels du logiciel décrivent une préférence marquée pour Bitwarden par rapport aux autres.

Un exemple typique de bon article : https://jcs.org/2017/11/17/bitwarden

Un exemple typique de site de vote comparatif : https://stackshare.io/stackups/bitwarden-vs-dashlane

Nous reportons KeyPass, pass, GPG, etc., car ils ajoutent de la complexité. Tous semblent être de bonnes solutions pour des utilisateurs techniques. GPG semble particulièrement intéressant pour les utilisateurs techniques qui veulent des capacités en ligne de commande entre systèmes.

Nous reportons KMS parce qu’il implique une dépendance à un fournisseur unique.

Nous choisissons Vault pour les besoins orientés système, parce que les avis sont étonnamment positifs, et parce que HashiCorp a un excellent historique de logiciels et d’assistance de très haute qualité.

Nous opposons notre veto aux approches de partage, par exemple via des documents partagés, des canaux partagés, des dossiers réseau partagés, etc. Elles n’offrent pas les qualités de sécurité que nous voulons.

Nous opposons notre veto aux approches improvisées peu technologiques, parce que nous sommes tous d’accord que ce n’est pas une voie à long terme.


### Implications

Les développeurs peuvent avoir à suivre les secrets à deux endroits : Bitwarden pour l’accès orienté utilisateur et Vault pour l’accès orienté système.


## Connexe


### Décisions connexes

La décision sur le serveur CI/CD à retenir doit inclure une preuve de sa capacité à accéder aux secrets.

Nous devrons décider comment gérer les secrets, en termes de politiques, de rotations, d’organisations, etc.


### Exigences connexes

Les secrets auront des exigences connexes en matière de conformité, d’audit et d’arrivée/départ du personnel côté RH.


### Artefacts connexes

Nous nous attendons à pouvoir exporter certains secrets vers des variables d’environnement.


### Principes connexes

Facilement réversible.

Facilement parallélisable, c’est-à-dire qu’il est facile d’utiliser une variété de gestionnaires de mots de passe.

Peu coûteux à essayer, c’est-à-dire qu’il y a un essai gratuit et aucun engagement.


## Notes

Notes d’évaluation ici. Les notes sont toutes des commentaires publics sur divers forums devops.


### Vault by HashiCorp

Vault est exactement ce que vous voulez ici. 

Ne mettez pas Vault directement en production, cependant : montez-le d’abord dans un environnement de test, car la documentation de HashiCorp peut être assez lacunaire même si leurs produits sont étonnants.

Courbe d’apprentissage très raide et mise en place non triviale. 

La configuration initiale est un peu pénible. Cela vaut tout à fait la peine, et la communauté le soutient assez pour que vous vous en sortiez.

Documentation épouvantable, mais il existe de nombreux guides en ligne de personnes qui l’ont installé, et si vous en combinez quelques-uns vous obtiendrez une installation fonctionnelle.

La configuration initiale a demandé de bricoler avec leurs helm charts (vault et consul). Bien que techniquement vous puissiez utiliser de nombreux autres back-ends, je ne le recommande vraiment pas. Le back-end/consul peut être minuscule si vous n’avez pas beaucoup de données à stocker.

Familiarisez-vous absolument avec la CLI, car l’interface graphique ressemble davantage à une preuve de concept / un portail publicitaire pour leur édition entreprise.

Le fait qu’on ne puisse pas simplement le « remplir » est pénible. Par exemple, si vous avez 5 champs, vous devez ajouter manuellement chaque champ pour chaque élément. Ce n’est donc pas comme si vous prédéfinissiez des champs pour une catégorie précise et remplissiez ces champs pour tous les éléments de cette catégorie, c’est plutôt « vous générez tout à chaque fois », ce qui (à mon avis) est une plaie.

Vous voudrez peut-être aussi regarder goldfish comme interface utilisateur par-dessus vault. Cela rend assez agréable l’adhésion de votre équipe. Ils ont aussi une démo. 1. Installez consul. 2. Installez vault pointant vers consul. 3. Installez goldfish pointant vers vault. 3. Configurez une tâche cron pour lancer consul snapshot pour les sauvegardes.



### LastPass

LastPass Teams. Nous l’utilisons, il a des modèles personnalisés, des ACL, rien ne manque à mon avis.

J’ai mis en place LastPass dans mon organisation et je lui donne un C+/B-. Le plus gros problème ces derniers temps est le manque de fiabilité. Au cours des 90 derniers jours, il y a eu plusieurs heures pendant lesquelles les coffres-forts (vaults) ont été forcés en mode hors ligne. Ce n’est pas idéal pour mon organisation car nous avons, littéralement, plus de 4 000 mots de passe stockés dans plus de 20 dossiers partagés. Comme vous pouvez l’imaginer, avec autant de mots de passe, au moins quelques-uns sont mis à jour ou ajoutés chaque jour. Nous avons un plan de reprise après sinistre si les problèmes durent plus d’une heure ou deux : un script signe et chiffre chaque nuit un export CSV du coffre-fort qui peut être importé dans keepass.

LastPass a eu des épisodes non signalés de service dégradé : la connexion « fonctionne » mais ne récupère pas les sites, des fonctionnalités aléatoires sont cassées dans le panneau d’administration, et les clés ne sont pas correctement partagées pour les nouveaux dossiers partagés de premier niveau. J’ai un utilisateur spécifique de « poussée de clés » / sauvegarde qui est dans tous les groupes. Normalement, se connecter en tant que cet utilisateur résout tout problème de partage de clés, mais pas quand le service est dégradé, quoi que dise la page d’état...

Pour l’intégration, cela peut être facile si vous avez des ACL appropriées avec un modèle de moindre privilège, p. ex. si un utilisateur a lecture-écriture et lecture seule sur une entrée ou un dossier, il n’obtient que les permissions de lecture seule. Malheureusement, les ACL de mon organisation ne sont pas les meilleures, et j’ai donc fini par utiliser l’API de provisionnement JSON et ~500 lignes de python parce que la nature dépendante de nos centaines d’ACL ne correspondait pas bien au modèle de moindre privilège. J’ai fini par récupérer toutes les ACL dont un utilisateur faisait partie et par faire une sorte de parcours de dépendances.

Si votre structure d’ACL ou de groupes est déjà conçue avec une structure de moindre privilège en tête, l’outil de synchronisation AD/LDAP pour Windows fonctionnera bien.

Contactez leur équipe commerciale et ils peuvent vous procurer un essai Entreprise plus long. Assurez-vous de bien comprendre ses limites avant de vous lancer. Nous avons eu pas mal de douleurs de croissance, mais hormis les pannes ou dégradations côté serveur, tout s’est passé de façon incroyablement fluide.


### Bitwarden

Bitwarden dispose d’un bon outillage autour (interface web, CLI, mobile, bureau). Auto-hébergeable et assez facile à installer. Documentation assez bonne et outil recommandé par PrivacyTools.


### EnvKey

https://www.envkey.com/ est un SaaS. Très facile à mettre en œuvre, à intégrer et à gérer.

Fonctionnalités :

  * Protéger les clés d’API et les identifiants.

  * Garder la configuration synchronisée partout.

  * Gestion de la configuration et des secrets intelligente et chiffrée de bout en bout. 

  * Empêcher le partage non sécurisé et la prolifération de configurations. 

  * Intégrer en quelques minutes.

Capacités :

  * Gérer la configuration et les niveaux d’accès de toutes vos applications, environnements et équipes en un seul endroit.

  * Configurer n’importe quel environnement de développement ou de serveur avec une seule variable d’environnement.

Avantages :

  * Bonne page d’accueil.

  * Proposition de valeur claire.

  * Application web visuellement excellente.

  * Données d’exemple supérieures, p. ex. Algolia, AWS, Datadog, GitHub, Stripe, etc.

  * J’ai parlé avec le fondateur pendant 30 minutes de l’entreprise, de l’interface, etc. Dane semble bien informé, honnête sur le pour et le contre, et un partenaire viable.

  * L’entreprise est essentiellement une entreprise Y Combinator typique, avec 1 fondateur. A levé 120 000 $ en 2018-01.

  * L’accent est mis sur l’atteinte de fonctionnalités entreprise, notamment le passage de l’hébergement cloud d’EnvKey vers du sur site ou du BYOC.

  * Voie possible : commencer avec EnvKey pour la facilité d’utilisation, puis (plus tard ou en parallèle) ajouter Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant est un service open source de gestion de secrets qui offre un stockage et un accès conviviaux aux secrets de façon sécurisée, créé par les développeurs de Lyft.

Authentification KMS : Confidant résout le problème d’authentification de l’œuf et de la poule en utilisant AWS KMS et IAM pour permettre aux rôles IAM de générer des jetons d’authentification sécurisés que Confidant peut vérifier. Confidant gère aussi les autorisations KMS pour vos rôles IAM, ce qui permet aux rôles IAM de générer des jetons utilisables pour l’authentification de service à service ou pour transmettre des messages chiffrés entre services.

Chiffrement au repos de secrets versionnés : Confidant stocke les secrets en mode ajout seul dans DynamoDB, en générant une clé de données KMS unique pour chaque révision de chaque secret, avec la cryptographie symétrique authentifiée Fernet.

Une interface web conviviale pour gérer les secrets : Confidant fournit une interface web AngularJS qui permet aux utilisateurs finaux de gérer facilement les secrets, les correspondances entre secrets et services, et l’historique des modifications.


### Devolutions Password Server

https://server.devolutions.net/

Sécurisez, gérez et surveillez l’accès aux comptes et sessions privilégiés.

Un coffre-fort de mots de passe complet et hautement sécurisé qui vous permet de contrôler l’accès à vos comptes privilégiés, tout en améliorant la visibilité globale du réseau pour les administrateurs système et en offrant une expérience fluide aux utilisateurs finaux.

Fonctionnalités : coffre-fort de mots de passe centralisé de l’organisation, coffre-fort privé propre à chaque utilisateur, gestionnaire de mots de passe, injection d’identifiants,
intégration Active Directory, contrôle d’accès basé sur les rôles, authentification à deux facteurs, prêt pour l’entreprise, restrictions par IP, capacités de gestion, générateur automatique de mots de passe, accès par application mobile, historique des mots de passe, rapports d’accès, alertes par courriel.

  * prend en charge le chiffrement des données

  * prend en charge plusieurs schémas d’authentification, dont LDAP, O365 et utilisateurs locaux AVEC prise en charge du MFA depuis plusieurs sources

  * plusieurs dépôts/coffres-forts avec contrôles d’accès fins pour plusieurs équipes

  * interface web moderne

  * coffres-forts privés d’identifiants et de connexions pour les identifiants/connexions personnels

  * applications mobiles pour iOS/Android

  * journaux d’audit pour chaque entrée, qui/quoi/quand, avec une invite facultative demandant pourquoi on y accède

  * modèles personnalisables (bien qu’ils prennent en charge nativement des centaines de types de connexion)

  * des tonnes d’autres fonctionnalités et un client lourd Windows/Mac (Remote Desktop Manager) avec lequel vous pouvez synchroniser et qui élargit considérablement les options... connexions en un clic

  * le prix n’est pas si mauvais - jusqu’à 15 utilisateurs, c’est 500 $ par an pour le serveur de mots de passe


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Fonctionnalités de la version sur site (on-premise) : 

  * Contrôle total sur vos systèmes et votre infrastructure de sécurité de bout en bout

  * Déployez le logiciel dans votre centre de données sur site ou dans votre propre instance de cloud privé virtuel

  * Satisfaites les obligations légales et réglementaires qui exigent que toutes les données et tous les systèmes résident sur site

Fonctionnalités de la version cloud :

  * Le modèle de logiciel en tant que service vous permet de vous inscrire et de commencer tout de suite

  * Évolutivité élastique à mesure que vous grandissez

  * Contrôles et redondance fournis par Azure avec un SLA de disponibilité de 99,9 %

Retours d’utilisateurs :

  * Nous utilisions ce produit. Il était si facile à contourner et les règles ne fonctionnent que pour les gens intelligents. Les utilisateurs paresseux ou peu doués peuvent facilement tout gâcher dans une zone d’équipe. Les prix sont négociables quand on leur parle.

  * Vous pouvez le faire tourner avec SQL express et une machine Win 7. 

  * Pas cher.
