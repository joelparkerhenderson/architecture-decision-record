# Enregistrement de décision d’architecture : framework d’applications web tout inclus (batteries included), full stack, pour un produit de startup

<!-- 

ChatGPT prompt

Long software architecture decision record 
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports. 

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Objectif principal :**  
Construire une application web permettant à des clients payants de se connecter, de téléverser des fichiers, de traiter des données et de consulter des rapports, en mettant l’accent sur le développement agile, la fonctionnalité full stack et une forte compatibilité avec les outils d’IA/ML, notamment les notebooks Project Jupyter.

### Contexte et exigences :

1. **Développement agile (priorité haute)** : en tant que startup, nous avons besoin d’itération rapide et de flexibilité. Les pratiques agiles, comme le prototypage rapide, le développement itératif et l’adaptabilité au changement, sont essentielles à notre cycle de développement.

2. **Framework full stack (priorité haute)** : nous visons à minimiser la surcharge en choisissant un framework capable de gérer efficacement le back-end et le front-end, réduisant le besoin de frameworks front-end séparés.

3. **Compatibilité avec les outils d’IA/ML (priorité haute)** : la capacité de s’intégrer facilement à des outils d’analyse de données comme les notebooks Jupyter et à l’écosystème de science des données de Python (NumPy, Pandas, TensorFlow, etc.) est essentielle. Cela faciliterait un traitement de données et une production de rapports efficaces.

4. **Critères de faible importance** :
   - **Vitesse d’exécution** : bien que la performance soit pertinente, ce n’est pas le facteur le plus critique au départ car nous nous soucions davantage de la vitesse de développement et de l’exhaustivité des fonctionnalités.
   - **Évolutivité** : nous anticipons une croissance, mais les préoccupations d’évolutivité peuvent être traitées plus tard, et ce n’est pas une exigence principale pour l’instant.
   - **Rétrocompatibilité** : nous nous concentrons sur les technologies actuelles et ne sommes pas très préoccupés par la rétrocompatibilité avec les systèmes hérités.

### Frameworks évalués :

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Aperçu** :  
Django est un framework web de haut niveau pour Python qui favorise le développement rapide et une conception propre et pragmatique. Il est connu pour sa philosophie « tout inclus » (batteries included), ce qui signifie qu’il intègre d’emblée de nombreuses fonctionnalités telles que l’authentification, le routage, l’ORM et la gestion de formulaires.

**Forces** :  
- **Full stack** : Django est un framework complet et full stack qui peut répondre aux besoins du back-end comme du front-end avec des fonctionnalités intégrées (p. ex. moteur de gabarits, interface d’administration).
- **Développement agile** : la structure et les conventions bien définies de Django permettent un développement rapide et de l’adaptabilité, cruciaux dans un environnement de startup. Le framework est livré avec une excellente documentation et un riche écosystème de paquets tiers, ce qui accélère le développement.
- **Intégration IA/ML** : l’écosystème de Python est inégalé en science des données et en apprentissage automatique. Django, étant fondé sur Python, s’intègre de façon transparente avec des outils comme les notebooks Jupyter, Pandas, NumPy, TensorFlow et scikit-learn.
- **Communauté et écosystème** : Django possède une vaste communauté, une documentation solide et un large éventail de plugins et d’extensions, ce qui accélère considérablement le développement et le dépannage.
  
**Faiblesses** :  
- **Vitesse d’exécution** : Python tend à être plus lent que des langages comme Rust ou Elixir. Toutefois, pour ce cas d’usage, où la performance n’est pas la préoccupation principale, cela peut ne pas être rédhibitoire.
- **Évolutivité** : bien que Django soit très évolutif, il peut y avoir des difficultés à très grande échelle sans optimisation soignée (p. ex. lors du traitement de nombreuses requêtes concurrentes). Néanmoins, Django peut tout de même être mis à l’échelle efficacement grâce à des techniques d’équilibrage de charge et de mise en cache.

**Verdict** :  
Django s’aligne bien avec les exigences de développement agile, de prise en charge full stack et de compatibilité IA/ML. Son intégration avec Python offre un accès fluide aux outils et bibliothèques de science des données nécessaires à l’application.

---

### 2. **Ruby on Rails (Ruby)**

**Aperçu** :  
Ruby on Rails (RoR) est un framework d’applications web mature et full stack, connu pour son approche de la convention plutôt que de la configuration, qui facilite le développement rapide.

**Forces** :  
- **Full stack** : RoR est livré avec des outils intégrés pour le développement back-end et front-end (p. ex. vues, gabarits, échafaudage), et sa riche bibliothèque de gems permet de mettre en œuvre rapidement diverses fonctionnalités.
- **Développement agile** : Ruby on Rails est particulièrement connu pour ses cycles d’itération rapides, ce qui est avantageux pour les startups qui veulent itérer rapidement sur les fonctionnalités. RoR prend en charge le développement piloté par les tests (TDD) et dispose d’un écosystème établi pour les flux de travail agiles.
- **Communauté et écosystème** : RoR a une communauté solide et bien établie et un large éventail de gems qui peuvent accélérer le développement.
- **Facilité d’utilisation** : Rails a une syntaxe très conviviale pour les développeurs et est connu pour rendre rapides et simples des tâches comme les migrations de base de données, l’architecture modèle-vue-contrôleur (MVC) et la gestion des routes.

**Faiblesses** :  
- **Performance** : Ruby tend à avoir une performance d’exécution plus lente que Python ou Elixir. Bien que RoR puisse monter en charge avec la bonne infrastructure, la performance de Ruby pourrait devenir un goulot d’étranglement pour les applications qui exigent beaucoup de traitement en temps réel ou un trafic concurrent élevé.
- **Intégration IA/ML** : bien que Ruby ait quelques bibliothèques d’apprentissage automatique, il n’est pas aussi largement adopté que Python dans la communauté IA/ML. L’intégration avec des outils comme les notebooks Jupyter est moins fluide, ce qui fait de Python un choix plus solide pour les applications riches en données.
  
**Verdict** :  
Si Ruby on Rails excelle dans le développement agile et le prototypage rapide, il reste en deçà de Python (Django) en matière de compatibilité IA/ML. C’est un choix viable pour les startups qui privilégient l’itération rapide à l’intégration poussée d’analyse de données.

---

### 3. **Phoenix (Elixir)**

**Aperçu** :  
Phoenix est un framework web construit avec Elixir, un langage de programmation fonctionnel conçu pour l’évolutivité et la concurrence. Phoenix tire parti de la machine virtuelle Erlang, connue pour gérer une concurrence massive et des systèmes tolérants aux pannes.

**Forces** :  
- **Évolutivité et performance** : Phoenix brille par son évolutivité et sa gestion d’une forte concurrence. Il est construit sur la machine virtuelle Erlang, qui peut prendre en charge des milliers (voire des millions) de connexions concurrentes, ce qui en fait un candidat solide pour les applications nécessitant un traitement de données en temps réel ou un trafic à fort volume.
- **Full stack** : Phoenix inclut tout ce qu’il faut pour construire le back-end et le front-end d’une application. Il prend en charge les vues en direct (live views) pour les mises à jour interactives de l’interface utilisateur et inclut un moteur de gabarits.
- **Développement agile** : Phoenix est très modulaire, ce qui permet d’itérer rapidement sur les fonctionnalités. Il est bien adapté aux startups qui doivent aller vite.
- **Compatibilité IA/ML** : bien qu’Elixir ait des bibliothèques d’apprentissage automatique émergentes, il n’est pas aussi largement pris en charge pour les tâches d’IA/ML que Python. L’intégration avec des outils comme les notebooks Jupyter exigerait des contournements, car l’écosystème d’Elixir pour la science des données n’est pas aussi mature que celui de Python.

**Faiblesses** :  
- **Écosystème IA/ML** : Elixir n’est pas le langage principal utilisé en science des données ou en apprentissage automatique, et son écosystème n’est pas aussi mature que celui de Python. L’intégration avec des outils comme les notebooks Jupyter ou des bibliothèques d’IA populaires (TensorFlow, PyTorch) sera donc laborieuse.
- **Courbe d’apprentissage** : si l’équipe n’est pas familiarisée avec la programmation fonctionnelle et Elixir, la courbe d’apprentissage peut être plus raide.

**Verdict** :  
Phoenix est un excellent choix si l’évolutivité et la concurrence sont une préoccupation principale. Toutefois, compte tenu de la priorité accordée à la compatibilité IA/ML, Phoenix n’est peut-être pas le meilleur choix en raison de l’écosystème limité d’Elixir dans ce domaine.

---

### 4. **Loco (Rust)**

**Aperçu** :  
Loco est un framework web construit avec Rust, un langage de programmation système connu pour sa performance, sa sécurité mémoire et sa concurrence. Rust est de plus en plus populaire pour construire des applications hautes performances.

**Forces** :  
- **Performance** : la principale force de Rust réside dans sa haute performance et sa sécurité mémoire, ce qui en fait un excellent choix pour les applications exigeant un contrôle de bas niveau ou une performance extrêmement élevée.
- **Concurrence** : le système de propriété de Rust garantit la sécurité mémoire tout en permettant une programmation concurrente sûre, ce qui le rend idéal pour les systèmes qui doivent monter en charge efficacement et gérer le parallélisme.

**Faiblesses** :  
- **Développement full stack** : Loco, bien que prometteur, n’est pas aussi mature que les autres frameworks pour fournir une solution full stack complète. Il convient mieux au développement back-end, et l’écosystème front-end autour de Rust est encore émergent.
- **Développement agile** : développer avec Rust peut être plus lent qu’avec des langages de plus haut niveau comme Python ou Ruby, en raison de sa nature de bas niveau et de sa courbe d’apprentissage plus raide.
- **Écosystème IA/ML** : Rust n’a pas un écosystème aussi étendu pour l’IA/ML que Python. Bien qu’il existe des bibliothèques de plus en plus nombreuses en Rust pour le calcul numérique, elles sont bien moins matures que les offres de Python, comme les notebooks Jupyter ou les frameworks d’apprentissage automatique.
  
**Verdict** :  
Bien que Rust et son framework Loco offrent une performance exceptionnelle, l’absence de prise en charge full stack, d’avantages pour le développement agile et d’écosystème IA/ML le rend moins idéal pour ce cas d’usage précis. Il convient mieux aux applications critiques en matière de performance qu’au développement web rapide avec des outils de science des données intégrés.

---

### Conclusion

Après avoir évalué les options selon les exigences du projet, **Django (Python)** est le choix le plus approprié. Il offre les avantages suivants :

- **Capacités full stack** : Django est un framework full stack qui intègre le développement back-end et front-end.
- **Développement agile** : le framework est bien adapté au prototypage et à l’itération rapides, essentiels dans un environnement de startup.
- **Compatibilité IA/ML** : Python est le langage de référence en IA/ML, et la compatibilité de Django avec des bibliothèques comme les notebooks Jupyter garantit une intégration fluide pour l’analyse et le traitement des données.
- **Communauté et écosystème** : le solide soutien de la communauté de Django et son vaste écosystème de bibliothèques fournissent de nombreux outils pour accélérer le développement.

Bien que **Ruby on Rails** soit aussi un concurrent sérieux pour le développement agile, sa prise en charge limitée de l’IA/ML le rend moins idéal pour ce cas d’usage précis. **Phoenix (Elixir)** et **Loco (Rust)**, bien qu’excellents en évolutivité et en performance, sont en deçà pour l’intégration IA/ML et le développement full stack. Django est donc le framework recommandé pour ce projet.
