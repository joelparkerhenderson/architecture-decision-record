# [000] Titre
*Attribuez un numéro à chaque ADR pour faciliter la référence et le catalogage* \
*REMARQUE : tout le texte en italique constitue des conseils et doit être supprimé pour la version finale*

## État - BROUILLON (DRAFT) / ACTIF (ACTIVE) / OBSOLÈTE (DEPRECATED) par [000] / REMPLACE (SUPERSEDES) [000]

## Contexte
*Décrivez brièvement le ou les problèmes que cet ADR vise à traiter, et pourquoi ils existent.*

## Approche retenue
*Détaillez la décision architecturalement significative qui a été / sera prise et décrivez comment elle traite les problèmes exposés dans la section Contexte.*

## Conséquences
*Quel est l’impact de cette décision sur les caractéristiques d’architecture et sur les exigences fonctionnelles du système ?*

## Gouvernance
*Comment les résultats de cette décision seront-ils suivis ?* \
*Comment la conformité à cette décision sera-t-elle assurée ?*

## Analyse des options
*Le cas échéant, incluez ou référencez toute analyse de compromis (trade-off) réalisée pour aboutir à la décision prise dans ce document.*

### Légende
*Facultatif : fournissez aux parties prenantes des aides visuelles qui permettent de repérer rapidement les compromis positifs et négatifs, par exemple de simples surlignages de type feu tricolore avec des préfixes positifs ou négatifs.*

Un fond <span style="background-color:#4bce97; color:black;">vert</span> indique une bonne adéquation, qui se dégrade en passant par l’<span style="background-color:#f1c232; color:black;">ambre</span>, le <span style="background-color:#e06666; color:black;">rouge</span> étant la pire adéquation. \
\+ indique un commentaire à impact positif \
\- indique un commentaire à impact négatif

### Vue d’ensemble
*Dans quelle mesure chaque option est-elle adaptée au contexte du problème, en un coup d’œil ?*

<table>
  <thead>
    <tr>
      <th>Synthèse</th>
      <th>Option 1</th>
      <th>Option 2</th>
      <th>Option 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Facilité de mise en œuvre</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Très facile
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Délicate
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Mise en œuvre importante nécessitant une expertise
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Délais</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Très rapide
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Assez lente
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Très lente
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Valeur stratégique</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Aucune valeur stratégique, purement tactique
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Améliore légèrement l’expérience d’intégration des clients
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Idéale pour la fusion à venir
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Exigences fonctionnelles
*Dans quelle mesure chaque option possible répond-elle aux exigences fonctionnelles souhaitées ?*

<table>
  <thead>
    <tr>
      <th>Scénario</th>
      <th><i>Option 1</i></th>
      <th><i>Option 2</i></th>
      <th><i>Option 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Scénario 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scénario 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Scénario 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Facultatif : ajoutez des lignes / un autre tableau pour couvrir les scénarios futurs connus.*

### Exigences non fonctionnelles
*Dans quelle mesure chaque option possible répond-elle aux caractéristiques d’architecture souhaitées ?
Remarque : « Caractéristiques d’architecture » serait un titre plus approprié, mais adaptez-le au vocabulaire familier de votre domaine d’activité.*

<table>
  <thead>
    <tr>
      <th>Caractéristique </br> d’architecture</th>
      <th><i>Option 1</i></th>
      <th><i>Option 2</i></th>
      <th><i>Option 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Évolutivité</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Performance</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Disponibilité</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Facultatif : ajoutez ou référencez les définitions des caractéristiques d’architecture telles qu’elles s’appliquent à votre activité / produit.*
