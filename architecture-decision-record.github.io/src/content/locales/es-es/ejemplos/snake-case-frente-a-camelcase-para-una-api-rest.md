# Registro de decisión de arquitectura: ¿snake_case o camelCase para una API REST?

Decisión: se usará la convención de nomenclatura snake_case para los endpoints de la API REST

Estado: Aceptado

## Contexto

En las convenciones de nomenclatura para las API REST hay dos formatos populares: snake_case y camelCase. En el formato snake_case, cada palabra del nombre se separa con guiones bajos, mientras que en camelCase la primera palabra del nombre va en minúscula y las palabras siguientes tienen en mayúscula su primera letra. Esta decisión determinará qué convención de nomenclatura debe usarse para una API REST.

## Factores de la decisión

- Coherencia con las convenciones de nomenclatura existentes en el proyecto

- Legibilidad y claridad para cualquier persona que pueda trabajar en la API

- Alineación con las mejores prácticas del sector para las convenciones de nomenclatura de las API REST

- Facilidad de implementación y mantenimiento

## Decisión

Se usará la convención de nomenclatura snake_case para los endpoints de la API REST. Esta elección responde a los siguientes factores:

1. **Coherencia**: el proyecto ya usa la convención de nomenclatura snake_case para todos los endpoints, y sería beneficioso mantener esta convención para garantizar la coherencia en todo el proyecto.

2. **Legibilidad y claridad**: la convención snake_case es más legible y más fácil de entender. Los guiones bajos proporcionan una separación clara entre las palabras, lo que facilita analizar y entender el significado del nombre.

3. **Alineación con las mejores prácticas del sector**: la convención snake_case se usa ampliamente en el sector y se considera una mejor práctica para las API REST, lo que la convierte en una buena opción para el proyecto.

4. **Facilidad de implementación y mantenimiento**: mantener la convención de nomenclatura existente es más fácil de implementar y mantener, ya que habría que actualizar todo el código y la documentación existentes si se eligiera una convención nueva.

## Consecuencias

Esta decisión tiene posibles consecuencias. 

* Si los nuevos miembros del equipo que se incorporen al proyecto no están familiarizados con la convención de nomenclatura snake_case, podría generarse confusión y errores en el desarrollo. Sin embargo, dado que snake_case es una convención muy utilizada, ese riesgo es mínimo. 
  
* Si en el proyecto se usan otras herramientas o frameworks basados en gran medida en la convención camelCase, puede requerirse un esfuerzo adicional para convertir entre convenciones de nomenclatura. Sin embargo, no es una preocupación significativa, ya que el proyecto ha estandarizado la convención snake_case. 
 
En general, la decisión de usar la convención de nomenclatura snake_case para los endpoints de la API REST da como resultado un enfoque coherente, legible y conforme a los estándares del sector, y a la vez fácil de implementar y mantener.

<h6>Crédito: esta página fue generada por ChatGPT y luego editada para mejorar la claridad y el formato.</h6>
