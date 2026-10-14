# Plantilla de registro de decisión para decisiones técnicas importantes (ITD)

Esta es la plantilla de decisiones técnicas importantes (Important Technical Decisions, ITD) descrita en
[ITDs: a lean ADR for executive technical decision-making at scale - Ignacio Larrañaga](https://ignaciolarranaga.medium.com/itds-a-lean-adr-for-executive-technical-decision-making-at-scale-e18bb3f6a563).

Los ITD son una evolución enfocada de los ADR, optimizada para la rapidez, la claridad y la validación ejecutiva. Mientras que un ADR documenta lo que se decidió, un ITD es un artefacto ligero que pone la decisión en primer lugar y la hace revisable, de modo que las partes interesadas puedan examinarla rápidamente y cuestionarla con facilidad. Los ITD son adecuados para decisiones técnicas que no son estrictamente de arquitectura, como elegir un modelo, una biblioteca o una estrategia de CI/CD.

En cada archivo ITD, escriba estas secciones:

# Título

Enuncie la decisión en sí, no una descripción del tema.
Por ejemplo, «Usar Qwen2.5 1.5B Instruct para la traducción en el dispositivo».

## El problema

Una frase que indique qué intentamos resolver.

## Opciones consideradas

Las alternativas que estaban sobre la mesa, con la opción seleccionada en **negrita**.

## Justificación

Solo los factores decisivos que llevaron a la elección, no una lista exhaustiva de todas las ventajas y desventajas.

## Notas

Opcional. Cualquier contexto adicional que valga la pena registrar, como restricciones, supuestos o enlaces.
