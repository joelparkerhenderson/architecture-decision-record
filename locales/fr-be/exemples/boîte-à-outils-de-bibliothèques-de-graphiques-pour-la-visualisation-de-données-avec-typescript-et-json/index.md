# Enregistrement de décision d’architecture : boîte à outils de bibliothèques de graphiques pour la visualisation de données avec TypeScript et JSON

<!--

ChatGPT prompt:

Long software architecture decision record 
chart library toolkit for data visualization using TypeScript and JSON

Evaluate Charts: Apache ECharts, Chart.js, ApexCharts, AG Charts, Highcharts, Carbon Charts, Layer Cake, D3.

Primary need: advanced interactive charts, especially for financial data, scientific data, and government data.

High importance: 1. Agile development because this is for a startup. 2. Doughnut Chart, Radar Chart, Clustering Process
Chart, Area Chart with Time Axis, Candlestick Chart, Nightingale Chart, Geo SVG Map. 3. Free open source.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Objectif principal :**  
Sélectionner une boîte à outils de graphiques avancée pour créer des visualisations interactives, axée sur les données financières, scientifiques et gouvernementales, avec TypeScript et JSON. La bibliothèque doit offrir des fonctionnalités robustes, de la flexibilité, et être open source. 

### Contexte et exigences :

1. **Développement agile (priorité haute)** : en tant que startup, l’itération rapide, le prototypage et la flexibilité dans le développement sont essentiels. La bibliothèque de graphiques doit permettre des cycles de développement rapides.
   
2. **Types de graphiques (priorité haute)** :
   - **Graphique en anneau (Doughnut Chart)**
   - **Graphique radar (Radar Chart)**
   - **Graphique de processus de regroupement (Clustering Process Chart)**
   - **Graphique en aires avec axe temporel (Area Chart with Time Axis)**
   - **Graphique en chandeliers (Candlestick Chart)**
   - **Graphique de Nightingale (Nightingale Chart)**
   - **Carte géographique SVG (Geo SVG Map)**
   
   Ces types de graphiques sont particulièrement importants pour visualiser des jeux de données complexes, comme les tendances financières, les indicateurs scientifiques et l’information géographique.

3. **Gratuit et open source (priorité haute)** : la boîte à outils doit être open source afin d’éviter les coûts de licence, d’offrir de la transparence et de laisser de la flexibilité pour la personnalisation.

4. **Critères de faible importance** :
   - **Vitesse d’exécution** : bien que la performance soit importante, elle n’est pas une priorité absolue pour cette décision.
   - **Évolutivité** : bien que l’évolutivité soit généralement importante, le besoin immédiat est de construire un MVP susceptible de croître avec le temps. Les préoccupations d’évolutivité peuvent être traitées plus tard.
   - **Rétrocompatibilité** : pas une préoccupation principale pour la construction initiale, pourvu que la bibliothèque soit moderne et activement maintenue.

### Bibliothèques évaluées :

1. **Apache ECharts**
2. **Chart.js**
3. **ApexCharts**
4. **AG Charts**
5. **Highcharts**
6. **Carbon Charts**
7. **Layer Cake**
8. **D3.js**

---

### 1. **Apache ECharts**

**Aperçu** :  
Apache ECharts est une bibliothèque de graphiques puissante et flexible pour des visualisations interactives et personnalisables. Elle prend en charge une grande variété de graphiques et est particulièrement solide pour les visualisations complexes et dynamiques.

**Forces** :
- **Interactivité avancée** : ECharts excelle à fournir des graphiques interactifs, avec des fonctionnalités comme le zoom, le panoramique et les mises à jour dynamiques des données.
- **Anneau, radar, chandeliers, cartes géographiques SVG** : ECharts prend en charge bon nombre des types de graphiques requis, y compris les visualisations en anneau, radar, chandeliers et cartes géographiques.
- **Gratuite et open source** : ECharts est une bibliothèque open source, ce qui convient à la nature soucieuse du budget d’une startup et offre la liberté de modifier le code.
- **Flexibilité et extensibilité** : très personnalisable, avec une vaste prise en charge des animations, des visualisations personnalisées et des techniques de graphiques avancées.
  
**Faiblesses** :
- **Courbe d’apprentissage** : ECharts, bien que puissante, peut avoir une courbe d’apprentissage plus raide en raison de sa flexibilité et de son vaste API.
- **Complexité de la documentation** : la documentation est complète mais peut être écrasante pour les développeurs qui débutent avec elle.

**Verdict** :  
ECharts convient très bien au projet en raison de sa prise en charge des graphiques interactifs, y compris tous les types requis comme les graphiques en chandeliers, les graphiques radar et les cartes géographiques. Sa nature open source s’aligne sur le besoin de flexibilité et de rentabilité du projet.

---

### 2. **Chart.js**

**Aperçu** :  
Chart.js est une bibliothèque de graphiques simple et facile à utiliser pour construire des types de graphiques courants. Elle est connue pour sa simplicité et sa facilité d’intégration.

**Forces** :
- **Facilité d’utilisation** : Chart.js est très simple à configurer et à utiliser, avec une courbe d’apprentissage minimale.
- **Open source** : Chart.js est gratuite et open source, ce qui est essentiel pour réduire les coûts.
- **Types de graphiques courants** : elle prend en charge des graphiques de base comme les graphiques en anneau, en aires, radar et en courbes, qui couvrent la plupart des besoins principaux.

**Faiblesses** :
- **Graphiques avancés limités** : Chart.js ne prend pas en charge nativement les types de graphiques complexes comme les graphiques en chandeliers, les cartes géographiques SVG ou les graphiques de processus de regroupement. Bien que ces fonctionnalités puissent être ajoutées par des plugins ou de la personnalisation, ce n’est pas aussi direct qu’avec d’autres bibliothèques.
- **Interactivité** : bien que Chart.js prenne en charge une interactivité de base (p. ex. infobulles et effets de survol), elle n’offre pas des fonctionnalités aussi avancées qu’ECharts ou D3.js.

**Verdict** :  
Chart.js est excellente pour des projets simples et rapides, mais son manque de prise en charge des types de graphiques complexes la rend inadaptée à une application riche en données aux besoins avancés comme les graphiques en chandeliers et les cartes géographiques. C’est un bon choix pour le prototypage, mais pour les types de graphiques requis, des outils plus avancés sont recommandés.

---

### 3. **ApexCharts**

**Aperçu** :  
ApexCharts est une bibliothèque de graphiques moderne qui propose une variété de types de graphiques et se concentre sur des visualisations interactives avec un API facile à utiliser.

**Forces** :
- **Fonctionnalités interactives** : ApexCharts offre des graphiques interactifs avec infobulles, zoom, panoramique et mises à jour.
- **Prise en charge de graphiques financiers et scientifiques** : elle prend en charge une grande variété de types de graphiques, y compris les graphiques en chandeliers, radar et en aires.
- **Facilité d’utilisation** : elle dispose d’un API direct et est simple à intégrer dans un projet.
- **Gratuite et open source** : ApexCharts propose une version open source gratuite adaptée à de nombreux cas d’usage.
  
**Faiblesses** :
- **Personnalisation complexe** : bien qu’elle offre de nombreuses fonctionnalités, ses options de personnalisation ne sont pas aussi flexibles que celles d’ECharts ou de D3.js pour des besoins de graphiques très complexes ou sur mesure.
- **Cartes géographiques** : ApexCharts ne prend pas en charge nativement les cartes géographiques ni les graphiques de processus de regroupement, qui sont requis pour ce projet.

**Verdict** :  
ApexCharts est un concurrent sérieux grâce à sa facilité d’utilisation et à son interactivité, mais elle est en deçà pour certains types de graphiques avancés, notamment le besoin de cartes géographiques et de graphiques de regroupement. C’est une bonne option pour des graphiques plus simples mais il lui manque certaines fonctionnalités requises.

---

### 4. **AG Charts**

**Aperçu** :  
AG Charts est une bibliothèque de graphiques de qualité commerciale conçue pour la performance et la précision. Elle convient très bien à la création de tableaux de bord financiers, scientifiques et d’entreprise.

**Forces** :
- **Types de graphiques avancés** : AG Charts prend en charge de nombreux types de graphiques avancés, notamment les graphiques en chandeliers, en aires, radar, et plus encore. Elle offre aussi une intégration profonde avec d’autres produits AG-Grid.
- **Haute performance** : elle offre d’excellentes performances, surtout pour le traitement de grands jeux de données.
- **Interactivité** : AG Charts prend en charge diverses fonctionnalités interactives comme le zoom, les infobulles et les mises à jour dynamiques.

**Faiblesses** :
- **Pas entièrement gratuite** : bien qu’AG Charts propose une version gratuite, la version complète est payante, ce qui pourrait être un obstacle pour les startups cherchant à minimiser les coûts.
- **Complexité** : bien que la bibliothèque soit riche en fonctionnalités, elle peut être excessive pour des projets plus simples et peut exiger plus de configuration que d’autres options.

**Verdict** :  
AG Charts est puissante et riche en fonctionnalités mais n’est peut-être pas la mieux adaptée en raison de sa nature commerciale et de sa structure de coûts. Son adéquation dépend de la capacité du budget à absorber des versions payantes ou de la préférence pour des alternatives open source.

---

### 5. **Highcharts**

**Aperçu** :  
Highcharts est une bibliothèque de graphiques populaire, connue pour sa large gamme de types de graphiques et ses puissantes options de personnalisation.

**Forces** :
- **Types de graphiques complets** : Highcharts prend en charge une grande variété de graphiques, y compris les chandeliers, radar, aires et cartes géographiques.
- **Interactive et dynamique** : Highcharts fournit de riches fonctionnalités interactives, notamment l’exploration en profondeur (drill-down), le zoom et le panoramique.
- **Facilité d’utilisation** : elle dispose d’un API convivial et d’une bonne documentation, ce qui facilite la prise en main.

**Faiblesses** :
- **Licence commerciale** : bien que Highcharts propose une version gratuite pour un usage non commercial, la licence commerciale est coûteuse, ce qui pourrait être un inconvénient important pour les startups.
- **Courbe d’apprentissage** : bien que moins raide que celle d’ECharts, la courbe d’apprentissage de Highcharts peut rester difficile pour les débutants.

**Verdict** :  
Highcharts est une bibliothèque riche en fonctionnalités, mais sa licence commerciale la rend moins adaptée aux projets open source et sensibles aux coûts. Ses options de graphiques complètes sont un atout, mais la question de la licence limite son attrait pour ce cas d’usage.

---

### 6. **Carbon Charts**

**Aperçu** :  
Carbon Charts est une bibliothèque de graphiques développée par IBM, conçue pour créer des graphiques visuellement attrayants et hautement personnalisables.

**Forces** :
- **Personnalisabilité** : Carbon Charts permet une personnalisation poussée de l’apparence et du comportement des graphiques.
- **Open source** : elle est gratuite et open source, ce qui s’aligne sur l’exigence du projet de solutions économiques.
- **Prise en charge des graphiques courants** : elle prend en charge des types de graphiques courants comme les graphiques en anneau, radar et en aires, mais pas des types plus avancés comme les cartes géographiques ou les graphiques en chandeliers.

**Faiblesses** :
- **Types de graphiques avancés limités** : elle ne prend pas en charge les cartes géographiques, les graphiques de processus de regroupement ni les graphiques en chandeliers, qui sont essentiels pour le projet.
- **Écosystème plus petit** : Carbon Charts a une communauté et un écosystème plus petits que de plus grandes bibliothèques de graphiques comme ECharts ou Highcharts.

**Verdict** :  
Carbon Charts est open source et personnalisable, mais ne prend pas en charge les types de graphiques plus complexes nécessaires à ce projet. Elle convient mieux à des besoins de graphiques plus simples.

---

### 7. **Layer Cake**

**Aperçu** :  
Layer Cake est une bibliothèque de visualisation de données conçue pour créer des visualisations flexibles et en couches.

**Forces** :
- **Couches personnalisables** : elle offre de puissantes options de superposition de couches pour les visualisations complexes.
- **Open source** : elle est gratuite et open source, ce qui en fait une option viable pour les projets soucieux du budget.

**Faiblesses** :
- **Documentation limitée** : Layer Cake manque de documentation étendue et de soutien de la communauté, ce qui la rend plus difficile à utiliser que des bibliothèques plus établies.
- **Non conçue pour les graphiques** : Layer Cake convient mieux aux visualisations qui ne sont pas des graphiques ; ses options de graphiques prêtes à l’emploi sont donc limitées.

**Verdict** :  
Bien qu’intéressante pour des visualisations uniques, Layer Cake n’est pas idéale pour les exigences de graphiques traditionnelles comme les graphiques en chandeliers ou radar. Elle convient mieux aux visualisations personnalisées en dehors du champ des graphiques standard.

---

### 8. **D3.js**

**Aperçu** :  
D3.js est une puissante bibliothèque JavaScript pour créer des visualisations pilotées par les données via HTML, SVG et CSS.

**Forces** :
- **Flexibilité inégalée** : D3.js permet de créer pratiquement n’importe quel type de visualisation personnalisée, ce qui la rend très puissante pour les graphiques avancés et interactifs.
- **Fonctionnalités étendues** : elle prend en charge tous les types de graphiques requis, y compris les cartes géographiques, les graphiques de regroupement, et plus encore.
- **Personnalisable** : le niveau de personnalisation de D3.js est sans égal, permettant aux développeurs de construire des visualisations hautement sur mesure.

**Faiblesses** :
- **Courbe d’apprentissage raide** : D3.js a une courbe d’apprentissage raide et est plus complexe à intégrer que d’autres bibliothèques.
- **Chronophage** : construire des graphiques avec D3.js peut prendre du temps, surtout pour des graphiques courants comme les chandeliers ou les anneaux.

**Verdict** :  
D3.js est incroyablement puissante pour des graphiques avancés et personnalisés, mais elle est excessive pour de nombreux cas d’usage typiques en raison de sa courbe d’apprentissage raide et de son temps de développement. Elle convient mieux aux situations où les autres bibliothèques de graphiques n’offrent pas le niveau de personnalisation requis.

---

### Conclusion

Après avoir évalué les bibliothèques selon les besoins du projet, **Apache ECharts** se distingue comme la meilleure option. Elle prend en charge toute la gamme de graphiques requis, y compris les cartes géographiques, les graphiques en chandeliers et les graphiques de regroupement. Elle est open source, riche en fonctionnalités et très interactive, ce qui s’aligne parfaitement sur les objectifs du projet. Bien que **D3.js** offre la plus grande flexibilité, sa complexité et l’investissement en temps la rendent moins idéale pour une startup qui souhaite itérer rapidement. **ApexCharts** et **Chart.js** sont de bonnes alternatives pour des projets plus simples mais manquent de prise en charge des types de graphiques avancés.
