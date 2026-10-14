# Criterios de sostenibilidad de las decisiones

<https://www.infoq.com/articles/sustainable-architectural-design-decisions/>

Para definir en detalle la sostenibilidad de las decisiones, derivamos cinco criterios clave.

## Estratégica

Al tomar una decisión, quien examine las consecuencias estratégicas debe considerar aspectos como el impacto a largo plazo de las decisiones, por ejemplo, el esfuerzo futuro de operación y mantenimiento.

## Medible y gestionable

Es posible medir y evaluar el resultado de una decisión a lo largo del tiempo según criterios objetivos, idealmente numéricos (como los que promueven, por ejemplo, los escenarios de atributos de calidad y los talleres). No es posible capturar todas las decisiones de grano fino, por lo que los arquitectos deben limitar la granularidad de las decisiones a cierto nivel de detalle (como crear una clase de diseño). Esto conducirá a un conjunto de decisiones más sostenible y a menos vínculos de trazabilidad. Además, limitar el número de dependencias entre decisiones reduce el efecto dominó de los cambios.

## Alcanzable y realista

El fundamento para ajustar la solución al problema debe elegirse de forma pragmática y hacerse explícito. Por ejemplo, los arquitectos pueden indicar que se han cuidado de evitar la sobreingeniería o la subingeniería (es decir, deben aplicar el enfoque de «suficientemente bueno»).

## Arraigada en los requisitos

La toma de decisiones debe basarse en la experiencia y el contexto de arquitectura propios del dominio. Debe tener en cuenta el entorno de la empresa, así como los requisitos y las restricciones del proyecto, incluidos las habilidades actuales del equipo de desarrollo, el presupuesto de capacitación y el proceso.

## Atemporal

Las decisiones deben basarse en experiencia y conocimiento que probablemente no queden obsoletos pronto. Por ejemplo, los arquitectos pueden elegir patrones o tácticas de arquitectura independientes de la plataforma.
