# Proceso de registros de decisiones de arquitectura de AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Un registro de decisión de arquitectura (ADR) es un documento que describe una elección que el equipo hace sobre un aspecto significativo de la arquitectura de software que planea construir. Cada ADR describe la decisión de arquitectura, su contexto y sus consecuencias. Los ADR tienen estados y, por lo tanto, siguen un ciclo de vida. Para ver un ejemplo de ADR, consulte el apéndice.

El proceso de ADR genera una colección de registros de decisiones de arquitectura. Esta colección forma el registro de decisiones (decision log). El registro de decisiones aporta el contexto del proyecto, así como información detallada de implementación y de diseño. Los miembros del proyecto hojean los titulares de cada ADR para obtener una visión general del contexto del proyecto. Leen los ADR para profundizar en las implementaciones y las opciones de diseño del proyecto.

Cuando el equipo acepta un ADR, este pasa a ser inmutable. Si nuevos conocimientos exigen una decisión diferente, el equipo propone un nuevo ADR. Cuando el equipo acepta el nuevo ADR, este sustituye al ADR anterior.

## Alcance del proceso de ADR

Los miembros del proyecto deben crear un ADR para cada decisión significativa para la arquitectura que afecte al proyecto o producto de software, incluidas las siguientes (Richards y Ford 2020):

* Estructura (por ejemplo, patrones como los microservicios)

* Requisitos no funcionales (seguridad, alta disponibilidad y tolerancia a fallos)

* Dependencias (acoplamiento de componentes)

* Interfaces (API y contratos publicados)

* Técnicas de construcción (bibliotecas, frameworks, herramientas y procesos)

* Los requisitos funcionales y no funcionales son las entradas más comunes del proceso de ADR.


## Contenido del ADR

Cuando el equipo identifica la necesidad de un ADR, un miembro del equipo empieza a redactarlo a partir de una plantilla común a todo el proyecto. (Consulte la organización ADR en GitHub para ver plantillas de ejemplo.) La plantilla simplifica la creación del ADR y garantiza que recoja toda la información relevante. Como mínimo, cada ADR debe definir el contexto de la decisión, la decisión en sí y las consecuencias de la decisión para el proyecto y sus entregables. (Para ver ejemplos de estas secciones, consulte el apéndice.) Uno de los aspectos más potentes de la estructura del ADR es que se centra en el motivo de la decisión y no en cómo la implementó el equipo. Comprender por qué el equipo tomó la decisión facilita que otros miembros del equipo la adopten, y evita que otros arquitectos que no participaron en el proceso de toma de decisiones la anulen en el futuro.


## Proceso de adopción del ADR

Cualquier miembro del equipo puede crear un ADR, pero el equipo debe establecer una definición de propiedad para los ADR. Cada autor que sea propietario de un ADR debe mantener y comunicar activamente el contenido del ADR. Para aclarar esta propiedad, esta guía se refiere en las secciones siguientes a los autores de ADR como propietarios del ADR. Otros miembros del equipo siempre pueden contribuir a un ADR. Si el contenido de un ADR cambia antes de que el equipo lo acepte, el propietario debe aprobar estos cambios.

Una vez que el equipo identifica una decisión de arquitectura y a su propietario, el propietario del ADR presenta el ADR en el estado **Propuesto** (Proposed) al comienzo del proceso. Los ADR en estado Propuesto están listos para su revisión.

A continuación, el propietario del ADR inicia el proceso de revisión del ADR. El objetivo del proceso de revisión es decidir si el equipo acepta el ADR, determina que necesita ajustes o lo rechaza. El equipo del proyecto, incluido el propietario, revisa el ADR. La reunión de revisión debe comenzar con un tiempo dedicado a leer el ADR. En promedio, de 10 a 15 minutos deberían bastar. Durante ese tiempo, cada miembro del equipo lee el documento y añade comentarios y preguntas para señalar los temas poco claros. Tras la fase de revisión, el propietario del ADR lee en voz alta y comenta cada comentario con el equipo.

Si el equipo encuentra puntos de acción para mejorar el ADR, el estado del ADR sigue siendo **Propuesto**. El propietario del ADR formula las acciones y, en colaboración con el equipo, asigna un responsable a cada una. Cada miembro del equipo puede contribuir y resolver los puntos de acción. Es responsabilidad del propietario del ADR reprogramar el proceso de revisión.

El equipo también puede decidir rechazar el ADR. En ese caso, el propietario del ADR añade el motivo del rechazo para evitar discusiones futuras sobre el mismo tema. El propietario cambia el estado del ADR a **Rechazado** (Rejected).

Si el equipo aprueba el ADR, el propietario añade una marca de tiempo, una versión y una lista de partes interesadas. Luego el propietario actualiza el estado a **Aceptado** (Accepted).

Los ADR y el registro de decisiones que crean representan las decisiones tomadas por el equipo y ofrecen un historial de todas ellas. El equipo usa los ADR como referencia durante las revisiones de código y de arquitectura siempre que es posible. Además de realizar revisiones de código, tareas de diseño y tareas de implementación, los miembros del equipo deben consultar los ADR para conocer las decisiones estratégicas del producto.

Como buena práctica, cada cambio de software debe pasar por revisiones entre pares y requerir al menos una aprobación. Durante la revisión de código, un revisor puede encontrar cambios que infringen uno o más ADR. En ese caso, el revisor pide al autor del cambio de código que lo actualice y comparte un enlace al ADR. Cuando el autor actualiza el código, los revisores pares lo aprueban y se fusiona en la base de código principal.


## Proceso de revisión del ADR

El equipo debe tratar los ADR como documentos inmutables después de aceptarlos o rechazarlos. Modificar un ADR existente requiere crear un nuevo ADR, establecer un proceso de revisión para el nuevo ADR y aprobarlo. Si el equipo aprueba el nuevo ADR, el propietario debe cambiar el estado del ADR antiguo a **Sustituido** (Superseded).
