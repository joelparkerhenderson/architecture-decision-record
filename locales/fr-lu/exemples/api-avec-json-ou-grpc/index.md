# Enregistrement de décision d’architecture : API avec JSON ou gRPC

## État

Accepté

## Contexte

Nous concevons une API pour un nouveau service qui sera utilisé par plusieurs clients. Nous avons envisagé deux options pour mettre en œuvre l’API : utiliser JSON sur HTTP ou utiliser gRPC.

JSON sur HTTP est une approche largement utilisée pour construire des API, et elle est prise en charge par de nombreux langages de programmation et frameworks. Cette approche est simple, légère et facile à comprendre, ce qui en fait un bon choix pour de nombreux projets. Cependant, elle peut être moins efficace que d’autres options, surtout pour le traitement de grandes quantités de données.

gRPC, en revanche, est une technologie plus récente qui offre une manière plus efficace de construire des API. Elle utilise la sérialisation binaire pour transférer les données, ce qui peut être plus rapide et plus compact que JSON. gRPC prend aussi en charge le streaming bidirectionnel, ce qui en fait un bon choix pour les applications en temps réel.

## Décision

Après avoir examiné les avantages et les inconvénients des deux options, nous avons décidé d’utiliser gRPC pour notre API. Bien que JSON sur HTTP soit une option plus simple, nous pensons que gRPC fournira une solution plus efficace et plus évolutive pour notre service. Nous prévoyons aussi que notre API traitera une grande quantité de données, et la sérialisation binaire de gRPC sera plus efficace pour ce cas d’usage.

En outre, nous pensons que la prise en charge du streaming bidirectionnel par gRPC sera bénéfique pour les applications en temps réel que nous pourrions développer à l’avenir.

## Conséquences

En choisissant gRPC, nous devrons utiliser un ensemble d’outils et de bibliothèques différent pour construire notre API, par rapport à JSON sur HTTP. Cela peut exiger du temps et des efforts supplémentaires pour apprendre et mettre en œuvre ces technologies. De plus, les clients qui voudront utiliser notre API devront employer des bibliothèques compatibles gRPC, qui peuvent ne pas être aussi largement prises en charge que les bibliothèques JSON sur HTTP.

Cependant, nous pensons que les avantages de gRPC l’emportent sur ces inconvénients potentiels, et nous sommes convaincus que cette décision donnera une API plus efficace et plus évolutive.
