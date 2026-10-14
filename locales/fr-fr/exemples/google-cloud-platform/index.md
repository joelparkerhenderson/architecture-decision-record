# Enregistrement de décision d’architecture pour Google Cloud Platform

## Contexte

Google Cloud Platform (GCP) est une plateforme de cloud computing de premier plan qui propose divers services cloud, notamment des solutions de calcul, de stockage et de réseau. Cet ADR vise à documenter les décisions d’architecture prises pour développer et mettre en œuvre une infrastructure fondée sur GCP pour notre organisation.

## Décision

Notre organisation a décidé d’utiliser Google Cloud Platform comme infrastructure cloud pour son application. Les principales considérations de cette décision sont :

   - Rentabilité

   - Évolutivité

   - Fiabilité

   - Flexibilité

## Choix

Les services GCP suivants ont été retenus pour répondre à nos exigences :

   - Compute Engine pour les machines virtuelles et les ressources de calcul

   - Cloud Storage pour le stockage d’objets et l’hébergement de fichiers

   - Cloud SQL comme service de base de données géré

   - Firebase pour le développement et l’hébergement d’applications

## Justification

   - Rentabilité : Google Cloud Platform est très rentable par rapport aux autres plateformes cloud, ce qui en fait une option attrayante pour les organisations aux contraintes budgétaires.

   - Évolutivité : l’infrastructure de GCP, facile à faire évoluer, permet de gérer n’importe quelle quantité de trafic en temps réel.

   - Fiabilité : les services gérés de GCP offrent une grande fiabilité, avec des sauvegardes automatisées et des capacités de reprise après sinistre qui garantissent la haute disponibilité des ressources et des données.

   - Flexibilité : la plateforme fournit divers outils et services dans différents domaines tels que l’IA, l’analyse de données et l’IoT, ce qui la rend très polyvalente.

## Conséquences

La migration vers Google Cloud Platform nécessitera de former nos équipes aux services GCP, de repenser l’architecture de l’application pour la rendre compatible avec les services retenus, et de mettre à jour le code d’infrastructure pour prendre en charge les services GCP. Cependant, il est attendu qu’une fois la migration terminée, nous disposerons d’une infrastructure très évolutive, fiable et rentable pour héberger notre application. De plus, nous devrons gérer les coûts continus de provisionnement des ressources sur GCP.

## Conclusion

Google Cloud Platform est un excellent choix pour notre infrastructure cloud en raison de sa rentabilité, de son évolutivité, de sa fiabilité et de sa flexibilité. En utilisant les services retenus, nous pouvons fournir une infrastructure hautement disponible et robuste pour notre application.
