# Enregistrement de décision d’architecture : framework CSS

Sommaire :

- [Résumé](#résumé)
  - [Question](#question)
  - [Décision](#décision)
  - [État](#état)
- [Détails](#détails)
  - [Hypothèses](#hypothèses)
  - [Contraintes](#contraintes)
  - [Positions](#positions)
  - [Argument](#argument)
  - [Implications](#implications)
- [Connexe](#connexe)
  - [Décisions connexes](#décisions-connexes)
  - [Exigences connexes](#exigences-connexes)
  - [Artefacts connexes](#artefacts-connexes)
  - [Principes connexes](#principes-connexes)
- [Notes](#notes)


## Résumé


### Question

Nous voulons utiliser un framework CSS pour créer nos applications web :

  * Nous voulons que l’expérience utilisateur soit rapide et fiable, sur tous les navigateurs et toutes les tailles d’écran courants.

  * Nous voulons itérer rapidement sur la conception, la mise en page, l’UI/UX, etc.

  * Nous voulons des applications adaptatives (responsive), en particulier pour les petits écrans comme ceux des appareils mobiles, les grands écrans comme les écrans larges 4K, et les écrans dynamiques comme les affichages rotatifs.  


### Décision

Choix de Bulma.


### État

Choix de Bulma. Ouverts à de nouveaux choix de frameworks CSS au fur et à mesure de leur arrivée.


## Détails


### Hypothèses

Nous voulons créer des applications web modernes, rapides, fiables, adaptatives, etc.

Les applications web modernes typiques réduisent ou éliminent l’usage de jQuery pour plusieurs raisons : 

  * Le JavaScript moderne intègre progressivement de nombreuses capacités que jQuery fournissait, donc jQuery est moins nécessaire, et il existe de meilleurs modules, plus rapides et plus petits, qui fournissent des mises en œuvre spécifiques

  * L’approche générale de jQuery consiste à manipuler directement le DOM, ce qui est un anti-patron pour les frameworks JavaScript modernes (p. ex. React, Vue, Svelte)

  * jQuery interfère avec lui-même s’il est chargé deux fois, etc.


### Contraintes

Si nous choisissons un framework CSS qui utilise jQuery, nous sommes obligés d’importer jQuery. Par exemple, Semantic UI utilise jQuery, alors que Tachyons non.

Si nous choisissons un framework CSS minimal, nous renonçons à des composants du framework que nous pourrions vouloir maintenant ou bientôt. Par exemple, Semantic UI fournit un carrousel d’images, alors que Tachyons non.


### Positions

Nous avons envisagé de ne pas utiliser de framework. Cela semble encore viable, notamment parce que CSS grid fournit l’essentiel de ce dont notre projet a besoin.

Nous avons envisagé de nombreux frameworks CSS par un tri rapide d’une présélection : Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons, etc. Nos deux choix pour un examen plus approfondi sont Semantic UI (parce que c’est l’approche la plus sémantique) et Bulma (parce que c’est l’approche la plus légère qui fournit les composants que nous voulons maintenant).

Nous avons envisagé Semantic UI. Il fournit de nombreux composants, y compris ceux que nous voulons pour notre projet : onglets, grilles, boutons, etc. Nous avons fait un pilote avec Semantic UI de deux manières : avec des fichiers CDN classiques et avec des dépôts NPM. Nous avons réussi avec Semantic UI dans une page HTML statique, mais pas dans le délai imparti pour construire une SPA JavaScript (principalement à cause de problèmes de chargement de jQuery). Nous avons découvert que d’autres développeurs demandent aux développeurs de Semantic UI de créer une version sans jQuery, pour les mêmes raisons que nous. D’autres développeurs réclament depuis de nombreuses années une version sans jQuery, mais les développeurs ont dit non, et ont affirmé que toute version sans jQuery serait trop difficile à écrire, p. ex. ~« le projet Semantic UI compte plus de 22 000 points de contact qui utilisent jQuery ».

Exemple avec Semantic :

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Nous avons envisagé Bulma. Bulma a de nombreuses capacités similaires à celles de Semantic UI, mais moins de composants sophistiqués. Bulma est construit avec des techniques modernes, par exemple sans jQuery. Bulma dispose de quelques composants tiers, dont certains que nous pourrions vouloir utiliser.


Exemple avec Bulma :
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argument

Comme ci-dessus.

Plus précisément, Semantic UI semble porter un drapeau d’avertissement à la fois sur le plan technologique (c’est-à-dire tant de points de contact avec jQuery) et sur le plan du leadership (c’est-à-dire que l’absence de jQuery a été un refus net, plutôt que d’essayer une feuille de route, une amélioration continue ou une collecte de dons, etc.).


### Implications

Si nous trouvons un bon framework CSS sans jQuery, c’est en général utile et positif.


## Connexe


### Décisions connexes

Le framework CSS que nous choisissons peut affecter la testabilité.


### Exigences connexes

Nous voulons livrer rapidement une application purement moderne. 

Nous ne voulons pas passer de temps à travailler sur des frameworks plus anciens (en particulier Semantic UI) qui utilisent des dépendances plus anciennes (en particulier jQuery).


### Artefacts connexes

Affecte tout le HTML typique qui utilisera le CSS.


### Principes connexes

Facilement réversible.

Besoin de vitesse.


## Notes

Toute note ici.
