# Funciones de aptitud para decisiones como código

Las funciones de aptitud (fitness functions) son comprobaciones automatizadas y objetivas, escritas con código de programación, que verifican que las decisiones se mantienen.

- Las funciones de aptitud hacen que las decisiones sean comprobables y verificables.

- Las funciones de aptitud para decisiones pueden ayudar mucho a los objetivos de aseguramiento de la calidad, de los procesos regulatorios y de gobernanza.

## Cómo se relacionan las funciones de aptitud con las decisiones

Un registro de decisión documenta la decisión, mientras que una función de aptitud la asegura.

- Decisión de ejemplo: usamos event sourcing para los requisitos de auditoría.

- Función de aptitud de ejemplo: usamos el servidor de integración continua para comprobar que todos los cambios de estado deben producir eventos.

## Por qué las funciones de aptitud ayudan a las decisiones

Mediciones objetivas: las funciones de aptitud pasan o fallan, por lo que el trabajo es visible y claro.

Uso continuo: las funciones de aptitud son sus reglas vivas, y se ejecutan en cada commit y en cada compilación.

Confianza para refactorizar: las funciones de aptitud detectan automáticamente los errores en las reglas de decisión.

Gobernanza escalable: las funciones de aptitud aseguran los estándares sin crear cuellos de botella.

## ¿Pueden las funciones de aptitud usar IA?

Las funciones de aptitud pueden aprovechar los LLM de IA para las decisiones, haciendo preguntas sobre su trabajo, como sus planes, código, esquemas, API y más:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Pruebas unitarias de arquitectura

[ArchUnit](https://www.archunit.org/): comprueba las reglas de arquitectura del código Java usando cualquier framework de pruebas unitarias de Java.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): comprueba las reglas de arquitectura del código TypeScript y JavaScript usando Jest, Vitest, Jasmine, etc.
