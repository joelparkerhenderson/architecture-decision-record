## Enregistrement de décision d’architecture : framework d’automatisation de navigateur pour les tests E2E (Playwright ou Selenium)

### 1. **Contexte**

Nous sommes en train de choisir un framework d’automatisation de navigateur pour notre chaîne de tests de bout en bout (E2E). Ce framework fera partie intégrante de nos processus CI/CD, en exécutant des tests qui simulent de vraies interactions d’utilisateurs sur notre plateforme. Plus précisément, les tests couvriront des scénarios tels que l’inscription et la connexion des utilisateurs, le téléversement de fichiers, les interactions avec les tableaux de bord et le téléchargement de rapports.

En tant que **startup**, nous nous concentrons sur le **développement agile**, avec le besoin d’itérer et d’évoluer rapidement. Notre équipe travaille principalement avec **TypeScript** et **Python**, et la possibilité d’écrire des tests dans ces langages est essentielle. De plus, la plateforme contient des **graphiques et tableaux de bord interactifs**, ce qui rend crucial que l’outil d’automatisation prenne bien en charge des interfaces riches et dynamiques.

Les deux candidats pour cette tâche sont **Playwright** et **Selenium**, chacun avec ses forces et ses compromis. Nous devons évaluer ces frameworks selon les fonctionnalités et exigences exposées ci-dessous.

### 2. **Options envisagées**

- **Playwright** (de Microsoft)
- **Selenium** (du projet Selenium)

### 3. **Facteurs de décision**

Les facteurs qui influencent notre décision sont les suivants :

1. **Développement agile** : l’outil choisi doit permettre des cycles de développement rapides et flexibles.
2. **Prise en charge des langages** : notre équipe a besoin de la prise en charge de **TypeScript** et de **Python**.
3. **Tests d’interface utilisateur interactive** : la capacité de tester de façon fiable des graphiques interactifs, des tableaux de bord et des éléments dynamiques est essentielle.
4. **Vitesse d’exécution** : bien que ce ne soit pas une préoccupation principale, la performance dans les chaînes CI/CD est à considérer.
5. **Évolutivité** : nous ne prévoyons pas de montée en charge massive dans l’immédiat, mais nous voulons nous assurer que la solution peut gérer la croissance future.
6. **Rétrocompatibilité** : les systèmes hérités et la compatibilité avec les anciens navigateurs ne sont pas critiques pour notre projet pour le moment.
7. **Tests mobiles** : bien que ce ne soit pas une priorité immédiate, le framework devrait pouvoir tester des fonctionnalités adaptées au mobile ou être extensible pour de tels usages.
8. **Tests multi-écrans** : la prise en charge de configurations multi-écrans est une exigence secondaire, surtout si nous passons un jour à des parcours utilisateurs plus complexes.
9. **Tests de téléversement de fichiers** : le framework doit gérer efficacement les téléversements de fichiers, une exigence centrale de nos besoins de test.

### 4. **Critères d’évaluation**

- **Facilité d’utilisation** : est-il facile d’écrire et de maintenir des tests ?
- **Prise en charge des langages** : le framework prend-il en charge TypeScript et Python, les deux langages que notre équipe utilise le plus ?
- **Tests d’interface utilisateur interactive** : dans quelle mesure le framework gère-t-il des interfaces utilisateur complexes et interactives comme des graphiques, des téléversements de fichiers et des données dynamiques ?
- **Intégration CI/CD** : dans quelle mesure le framework s’intègre-t-il aux outils et services CI/CD courants ?
- **Prise en charge multi-navigateurs** : quels navigateurs sont pris en charge et quelle est leur performance ?
- **Performance et vitesse** : à quelle vitesse les tests s’exécutent-ils, surtout dans une chaîne CI/CD ?
- **Évolutivité** : dans quelle mesure le framework peut-il monter en charge si l’on ajoute plus de tests ou des scénarios plus complexes ?
- **Communauté et écosystème** : la communauté du framework est-elle active ? Existe-t-il beaucoup d’intégrations et d’extensions ?

### 5. **Considérations**

#### 5.1 **Playwright**

##### **Avantages** :
1. **API plus intelligente pour le téléversement de fichiers locaux** : l’API de Playwright pour interagir avec des fichiers locaux et effectuer des téléversements est plus simple et plus intuitive. Cela faciliterait la mise en œuvre et la maintenance des tests de téléversement de fichiers.
2. **Syntaxe et génération de code** : Playwright a une syntaxe plus courte et plus concise. Il en résulte moins de code passe-partout, ce qui améliore la maintenabilité et l’efficacité des développeurs. En outre, cette syntaxe plus courte améliore la qualité de la génération de code par OpenAI, ce qui facilite la génération automatique de scripts de test.
3. **Tests d’interface utilisateur interactive** : Playwright excelle dans le test d’applications web dynamiques et interactives, comme celles dotées de graphiques riches, d’interactions utilisateur complexes et de mises à jour en temps réel. Il gère très efficacement WebSockets, WebRTC, shadow DOM et d’autres technologies web modernes.
4. **Prise en charge multi-navigateurs** : Playwright prend en charge **Chromium**, **WebKit** et **Firefox**. Il a une performance constante sur ces navigateurs, ce qui devrait couvrir la plupart de nos besoins de test.
5. **Intégration CI/CD** : Playwright s’intègre de façon transparente aux plateformes CI/CD modernes (GitHub Actions, Jenkins, etc.). Il peut exécuter des tests en parallèle sur différents navigateurs, optimisant les temps d’exécution des tests et le rendant adapté au développement rapide.
6. **Rapide et fiable** : Playwright est généralement plus rapide que Selenium, surtout en mode sans interface (headless), et plus résilient face aux éléments web asynchrones.

##### **Inconvénients** :
1. **Tests mobiles limités** : bien que Playwright prenne en charge l’émulation mobile pour les navigateurs, il n’a pas de capacités natives de test mobile comme l’intégration de Selenium avec Appium pour de vrais tests mobiles.
2. **Écosystème plus petit** : Playwright est encore plus récent et moins établi que Selenium. Bien qu’il dispose d’une communauté en croissance rapide et d’une bonne documentation, il n’a peut-être pas encore le vaste écosystème de plugins et d’intégrations que propose Selenium.
3. **Prise en charge des navigateurs limitée** : bien que Playwright couvre les principaux navigateurs modernes (Chrome, Safari, Firefox), sa prise en charge des navigateurs hérités (p. ex. Internet Explorer) n’est pas aussi solide que celle de Selenium.

#### 5.2 **Selenium**

##### **Avantages** :
1. **Plus longue histoire et maturité** : Selenium existe depuis longtemps et a fait ses preuves. Il est largement utilisé dans de nombreuses équipes et de nombreux secteurs, ce qui a donné naissance à un vaste écosystème de plugins, d’intégrations et de ressources.
2. **Prise en charge multi-navigateurs et multiplateformes** : Selenium prend en charge une **grande variété de navigateurs** et de versions, y compris **Internet Explorer**, et peut aussi être intégré à divers outils comme **Docker**, **Selenium Grid** et des **services cloud** pour les tests distribués.
3. **Tests mobiles** : Selenium, grâce à son intégration avec **Appium**, est bien plus robuste pour les tests mobiles, tant pour les applications Android qu’iOS. Cela en fait le meilleur choix pour les projets orientés mobile d’abord ou fortement mobiles.
4. **Tests multi-écrans** : Selenium offre une meilleure prise en charge des scénarios impliquant **plusieurs écrans** ou des interactions complexes à fenêtres multiples.

##### **Inconvénients** :
1. **Complexité** : l’API de Selenium est plus verbeuse et plus explicite. Si cela peut être un avantage dans certains cas, cela signifie plus de code à écrire et à maintenir, ce qui peut réduire l’agilité des développeurs, un point particulièrement important en environnement de startup.
2. **Performance** : Selenium s’exécute généralement plus lentement que Playwright, surtout en mode sans interface (headless). Cela pourrait affecter les chaînes CI/CD, notamment à mesure que le nombre de tests augmente.
3. **Tests d’interface utilisateur interactive** : Selenium n’est pas aussi fluide que Playwright pour tester des interfaces web modernes et interactives, en particulier avec des graphiques et des mises à jour de données en temps réel. Il exige plus de configuration et de traitement pour interagir de façon fiable avec du contenu dynamique.

### 6. **Synthèse comparative**

| Fonctionnalité                    | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Facilité d’utilisation**        | Syntaxe plus courte, plus intuitive pour les interfaces modernes | Plus explicite, exige plus de code passe-partout |
| **Prise en charge des langages**  | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Tests d’interface interactive** | Excellent pour les interfaces dynamiques et en temps réel | Gère les interfaces de base, mais plus verbeux et complexe pour des interactions riches |
| **Tests de téléversement de fichiers** | API plus intelligente pour les téléversements | Plus verbeux, API moins intuitive        |
| **Intégration CI/CD**             | Intégration facile avec GitHub Actions, Jenkins | Intégration solide avec de nombreux outils CI |
| **Tests mobiles**                 | Limités, émulation seulement                  | Prise en charge complète via Appium       |
| **Prise en charge multi-navigateurs** | Chromium, WebKit, Firefox                 | Prise en charge complète des navigateurs principaux et hérités |
| **Performance**                   | Rapide, optimisé pour les tests sans interface | Plus lent, surtout en mode sans interface |
| **Tests multi-écrans**            | Limités                                       | Bonne prise en charge des configurations multi-écrans |
| **Communauté et écosystème**      | En croissance, bonne documentation            | Grande, mature, écosystème étendu        |

### 7. **Décision**

Après avoir examiné les exigences et les compromis, **Playwright** est le meilleur choix pour nos besoins actuels. Son API plus intelligente pour les tests de téléversement de fichiers locaux, sa syntaxe concise et sa solide prise en charge des tests d’interface utilisateur interactive en font un choix idéal pour notre cycle de développement agile. Le fait qu’il prenne en charge à la fois **TypeScript** et **Python** est essentiel pour notre équipe, et l’approche moderne du framework en matière de tests nous permettra d’écrire un code propre et maintenable.

Bien que **Selenium** reste un excellent outil, en particulier pour les tests mobiles, la prise en charge des navigateurs hérités et les configurations multi-écrans, il est moins bien adapté à nos besoins actuels. Sa verbosité, sa performance plus lente et sa gestion plus complexe des interfaces dynamiques comme les graphiques le rendent moins optimal pour notre cas d’usage.

### 8. **Conséquences**

- **Action immédiate** : nous adopterons **Playwright** pour nos tests E2E, en nous concentrant sur le test des parcours utilisateurs impliquant l’inscription, la connexion, le téléversement de fichiers, les tableaux de bord et le téléchargement de rapports.
- **Considérations à long terme** : nous surveillerons l’évolution de l’écosystème Playwright. Si nos besoins changent, en particulier autour des tests mobiles ou de la prise en charge des navigateurs hérités, nous pourrions reconsidérer Selenium.
- **Formation et documentation** : les équipes de développement devront se familiariser avec l’API de Playwright, en particulier pour gérer les interfaces dynamiques et les téléversements de fichiers.
- **Migration** : les tests Selenium existants (le cas échéant) seront progressivement migrés vers Playwright.

### 9. **Considérations futures**
