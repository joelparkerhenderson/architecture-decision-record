# Plantilla de registro de decisiones de Jeff Tyree y Art Akerman

Esta es la plantilla de descripción de decisiones arquitectónicas publicada en ["Architecture Decisions: Demystifying Architecture" por Jeff Tyree y Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions- neumático-05.pdf).

* **Problema**: Describa el problema de diseño arquitectónico que está abordando, sin dejar preguntas sobre por qué está abordando este problema ahora. Siguiendo un enfoque minimalista, aborde y documente sólo los problemas que deban abordarse en distintos puntos del ciclo de vida.

* **Decisión**: Indique claramente la dirección de la arquitectura, es decir, la posición que ha seleccionado.

* **Estado**: el estado de la decisión, como pendiente, decidida o aprobada.

* **Grupo**: puede utilizar una agrupación simple (como integración, presentación, datos, etc.) para ayudar a organizar el conjunto de decisiones. También se podría utilizar una ontología de arquitectura más sofisticada, como la de John Kyaruzi y Jan van Katwijk, que incluye categorías más abstractas como evento, calendario y ubicación. Por ejemplo, al utilizar esta ontología, agruparía decisiones que se ocupan de sucesos en los que el sistema requiere información bajo el evento.

* **Supuestos**: describa claramente los supuestos subyacentes en el entorno en el que está tomando la decisión: costo, cronograma, tecnología, etc. Tenga en cuenta que las limitaciones ambientales (como estándares tecnológicos aceptados, arquitectura empresarial, patrones comúnmente empleados, etc.) pueden limitar las alternativas que considere.

* **Restricciones**: Capture cualquier restricción adicional al entorno que la alternativa elegida (la decisión) pueda plantear.

* **Posiciones**: Enumere las posiciones (opciones viables o alternativas) que consideró. Estos suelen requerir largas explicaciones, a veces incluso modelos y diagramas. Esta no es una lista exhaustiva. Sin embargo, no querrás escuchar la pregunta "¿Pensaste en...?" durante una revisión final; esto conduce a la pérdida de credibilidad y al cuestionamiento de otras decisiones arquitectónicas. Esta sección también ayuda a garantizar que haya escuchado las opiniones de los demás; Expresar explícitamente otras opiniones ayuda a involucrar a sus defensores en su decisión.

* **Argumento**: describa por qué seleccionó un puesto, incluidos elementos como el costo de implementación, el costo total de propiedad, el tiempo de comercialización y la disponibilidad de los recursos de desarrollo necesarios. Probablemente esto sea tan importante como la decisión misma.

* **Implicaciones**: Una decisión tiene muchas implicaciones, como lo indica el metamodelo REMAP. Por ejemplo, una decisión podría introducir la necesidad de tomar otras decisiones, crear nuevos requisitos o modificar requisitos existentes; plantear limitaciones adicionales al medio ambiente; requerir renegociar el alcance o el cronograma con los clientes; o requerir capacitación adicional del personal. Comprender y expresar claramente las implicaciones de su decisión puede ser muy eficaz para lograr aceptación y crear una hoja de ruta para la ejecución de la arquitectura.

* **Decisiones relacionadas**: Es obvio que muchas decisiones están relacionadas; puedes enumerarlos aquí. Sin embargo, hemos descubierto que, en la práctica, una matriz de trazabilidad, árboles de decisión o metamodelos son más útiles. Los metamodelos son útiles para mostrar relaciones complejas en forma de diagramas (como los modelos Rose).

* **Requisitos relacionados**: Las decisiones deben estar impulsadas por el negocio. Para mostrar responsabilidad, asigne explícitamente sus decisiones a los objetivos o requisitos. Puede enumerar estos requisitos relacionados aquí, pero nos ha resultado más conveniente hacer referencia a una matriz de trazabilidad. Puede evaluar la contribución de cada decisión de arquitectura para cumplir cada requisito y luego evaluar qué tan bien se cumple el requisito en todas las decisiones. Si una decisión no contribuye a cumplir un requisito, no tome esa decisión.

* **Artefactos relacionados**: enumere los documentos de arquitectura, diseño o alcance relacionados a los que afecta esta decisión.

* **Principios relacionados**: si la empresa tiene un conjunto de principios acordados, asegúrese de que la decisión sea coherente con uno o más de ellos. Esto ayuda a garantizar la alineación entre dominios o sistemas.

* **Notas**: Debido a que el proceso de toma de decisiones puede llevar semanas, nos resultó útil capturar notas y temas que el equipo analiza durante el proceso de socialización.