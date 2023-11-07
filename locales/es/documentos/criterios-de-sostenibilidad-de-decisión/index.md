# Criterios de sostenibilidad de decisión

<https://www.infoq.com/articles/sustainable-architectural-design-decisions/>

Para definir la sostenibilidad de la decisión en detalle, derivamos cinco criterios clave.

## estratégico

Durante la toma de decisiones, alguien que analice las consecuencias estratégicas debe considerar cosas como el impacto a largo plazo de las decisiones, por ejemplo, operaciones futuras y esfuerzos de mantenimiento.

## Medible y manejable

Puede medir y evaluar el resultado de una decisión a lo largo del tiempo de acuerdo con los criterios objetivos, idealmente numéricos (como, por ejemplo, propagados por escenarios de atributos de calidad y talleres4). La captura de todas las decisiones de grano fino no es posible, por lo que los arquitectos deben limitar la granularidad de las decisiones a un cierto nivel de detalle (como crear una clase de diseño). Esto conducirá a un conjunto de decisiones más sostenible y menos enlaces de trazabilidad. Además, limitar el número de dependencias entre las decisiones reduce el efecto de dominio de los cambios.

## alcanzable y realista

La justificación para ajustar la solución al problema debe elegirse pragmáticamente y hacerse explícito. Por ejemplo, los arquitectos pueden indicar que han tenido cuidado de evitar la sobrenadería o subenvenimiento (es decir, deben aplicar el enfoque "lo suficientemente bueno").

## arraigado en requisitos

La toma de decisiones debe basarse en la experiencia y el contexto de arquitectura específica del dominio. Debe tener en cuenta el entorno de la empresa, así como los requisitos y limitaciones del proyecto, incluidas las habilidades actuales, el presupuesto de capacitación y el proceso del equipo de desarrollo.

## atemporal

Las decisiones deben basarse en la experiencia y el conocimiento que probablemente no estarán anticuados pronto. Por ejemplo, los arquitectos pueden elegir patrones de arquitectura neutrales de plataforma o tácticas.