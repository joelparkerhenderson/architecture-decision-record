# Critères de durabilité des décisions

<https://www.infoq.com/articles/sustainable-architectural-design-decisions/>

Pour définir en détail la durabilité des décisions, nous avons dégagé cinq critères clés.

## Stratégique

Lors de la prise de décision, la personne qui examine les conséquences stratégiques doit tenir compte d’éléments tels que l’impact à long terme des décisions, par exemple l’effort futur d’exploitation et de maintenance.

## Mesurable et gérable

Vous pouvez mesurer et évaluer le résultat d’une décision dans le temps selon des critères objectifs, idéalement numériques (comme le préconisent, par exemple, les scénarios d’attributs de qualité et les ateliers). Il est impossible de consigner toutes les décisions à granularité fine ; les architectes doivent donc limiter la granularité des décisions à un certain niveau de détail (comme la création d’une classe de conception). Cela conduira à un ensemble de décisions plus durable et à moins de liens de traçabilité. En outre, limiter le nombre de dépendances entre décisions réduit l’effet d’entraînement des changements.

## Réalisable et réaliste

La justification de l’adéquation de la solution au problème doit être choisie de façon pragmatique et rendue explicite. Par exemple, les architectes peuvent indiquer qu’ils ont veillé à éviter la sur-ingénierie ou la sous-ingénierie (c’est-à-dire qu’ils doivent appliquer l’approche du « suffisamment bon »).

## Ancrée dans les exigences

La prise de décision doit s’appuyer sur l’expérience et le contexte d’architecture propres au domaine. Elle doit tenir compte de l’environnement de l’entreprise ainsi que des exigences et contraintes du projet, y compris les compétences actuelles de l’équipe de développement, le budget de formation et le processus.

## Intemporelle

Les décisions doivent reposer sur une expérience et des connaissances peu susceptibles de devenir rapidement obsolètes. Par exemple, les architectes peuvent choisir des patrons ou des tactiques d’architecture indépendants de la plateforme.
