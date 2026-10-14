# Plantilla de registro de decisión de Jeff Tyree y Art Akerman

Esta es la plantilla de descripción de decisiones de arquitectura publicada en ["Architecture Decisions: Demystifying Architecture" de Jeff Tyree y Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Asunto (Issue)**: describa el problema de diseño de arquitectura que está abordando, sin dejar dudas sobre por qué lo aborda ahora. Siguiendo un enfoque minimalista, aborde y documente solo los asuntos que necesitan atención en distintos momentos del ciclo de vida.

* **Decisión (Decision)**: indique con claridad la dirección de la arquitectura, es decir, la posición que ha seleccionado.

* **Estado (Status)**: el estado de la decisión, como pendiente, decidida o aprobada.

* **Grupo (Group)**: puede usar una agrupación sencilla, como integración, presentación, datos, etc., para ayudar a organizar el conjunto de decisiones. También podría usar una ontología de arquitectura más sofisticada, como la de John Kyaruzi y Jan van Katwijk, que incluye categorías más abstractas como evento, calendario y ubicación. Por ejemplo, con esta ontología, agruparía bajo evento las decisiones que tratan de sucesos en los que el sistema requiere información.

* **Supuestos (Assumptions)**: describa con claridad los supuestos subyacentes del entorno en el que toma la decisión: costo, calendario, tecnología, etc. Tenga en cuenta que las restricciones del entorno (como los estándares tecnológicos aceptados, la arquitectura empresarial, los patrones de uso común, etc.) pueden limitar las alternativas que considere.

* **Restricciones (Constraints)**: registre cualquier restricción adicional al entorno que la alternativa elegida (la decisión) pueda imponer.

* **Posiciones (Positions)**: enumere las posiciones (opciones o alternativas viables) que consideró. A menudo requieren explicaciones extensas, a veces incluso modelos y diagramas. No es una lista exhaustiva. Sin embargo, no querrá oír la pregunta «¿Pensó en...?» durante una revisión final; esto genera pérdida de credibilidad y cuestionamiento de otras decisiones de arquitectura. Esta sección también ayuda a asegurar que haya escuchado las opiniones de otros; enunciar explícitamente otras opiniones ayuda a sumar a sus defensores a su decisión.

* **Argumento (Argument)**: resuma por qué seleccionó una posición, incluidos aspectos como el costo de implementación, el costo total de propiedad, el tiempo de salida al mercado y la disponibilidad de los recursos de desarrollo necesarios. Probablemente sea tan importante como la decisión misma.

* **Implicaciones (Implications)**: una decisión conlleva muchas implicaciones, como indica el metamodelo REMAP. Por ejemplo, una decisión puede generar la necesidad de tomar otras decisiones, crear requisitos nuevos o modificar los existentes, imponer restricciones adicionales al entorno, exigir renegociar el alcance o el calendario con los clientes o requerir capacitación adicional del personal. Comprender y enunciar con claridad las implicaciones de su decisión puede ser muy eficaz para obtener respaldo y crear una hoja de ruta para la ejecución de la arquitectura.

* **Decisiones relacionadas (Related decisions)**: es evidente que muchas decisiones están relacionadas; puede enumerarlas aquí. Sin embargo, hemos comprobado que, en la práctica, son más útiles una matriz de trazabilidad, árboles de decisión o metamodelos. Los metamodelos son útiles para mostrar relaciones complejas mediante diagramas (como los modelos de Rose).

* **Requisitos relacionados (Related requirements)**: las decisiones deben estar guiadas por el negocio. Para demostrar responsabilidad, relacione explícitamente sus decisiones con los objetivos o requisitos. Puede enumerar aquí estos requisitos relacionados, pero hemos comprobado que resulta más cómodo hacer referencia a una matriz de trazabilidad. Puede evaluar la contribución de cada decisión de arquitectura al cumplimiento de cada requisito y, luego, evaluar qué tan bien se cumple el requisito en todas las decisiones. Si una decisión no contribuye a cumplir un requisito, no tome esa decisión.

* **Artefactos relacionados (Related artifacts)**: enumere los documentos de arquitectura, diseño o alcance relacionados a los que afecta esta decisión.

* **Principios relacionados (Related principles)**: si la empresa tiene un conjunto de principios acordados, asegúrese de que la decisión sea coherente con uno o más de ellos. Esto ayuda a garantizar la alineación entre dominios o sistemas.

* **Notas (Notes)**: dado que el proceso de toma de decisiones puede durar semanas, hemos comprobado que es útil registrar las notas y los asuntos que el equipo discute durante el proceso de socialización.
