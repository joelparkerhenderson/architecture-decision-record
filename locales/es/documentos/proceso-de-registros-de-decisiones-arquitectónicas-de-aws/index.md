# Proceso de registros de decisiones arquitectónicas de AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Un registro de decisión arquitectónica (ADR) es un documento que describe una elección que el equipo hace sobre un aspecto significativo de la arquitectura de software que planean construir. Cada ADR describe la decisión arquitectónica, su contexto y sus consecuencias. Los ADR tienen estados y, por lo tanto, siguen un ciclo de vida. Para un ejemplo de un ADR, consulte el apéndice.

El proceso ADR genera una colección de registros de decisión arquitectónica. Esta colección crea el registro de decisiones. El registro de decisiones proporciona el contexto del proyecto, así como información detallada de implementación y diseño. Los miembros del proyecto escabullen los titulares de cada ADR para obtener una visión general del contexto del proyecto. Leen los ADR para sumergirse profundamente en las implementaciones del proyecto y las opciones de diseño.

Cuando el equipo acepta un ADR, se vuelve inmutable. Si las nuevas ideas requieren una decisión diferente, el equipo propone un nuevo ADR. Cuando el equipo acepta el nuevo ADR, reemplaza al ADR anterior.

## alcance del proceso ADR

Los miembros del proyecto deben crear un ADR para cada decisión arquitectónicamente significativa que afecte el proyecto o producto de software, incluido el siguiente (Richards y Ford 2020):

* Estructura (por ejemplo, patrones como microservicios)

* Requisitos no funcionales (seguridad, alta disponibilidad y tolerancia a fallas)

* Dependencias (acoplamiento de componentes)

* Interfaces (API y contratos publicados)

* Técnicas de construcción (bibliotecas, marcos, herramientas y procesos)

* Los requisitos funcionales y no funcionales son las entradas más comunes para el proceso ADR.


## Contenido ADR

Cuando el equipo identifica la necesidad de un ADR, un miembro del equipo comienza a escribir el ADR basado en una plantilla en todo el proyecto. (Consulte la organización ADR Github, por ejemplo, plantillas.) La plantilla simplifica la creación de ADR y asegura que el ADR capture toda la información relevante. Como mínimo, cada ADR debe definir el contexto de la decisión, la decisión en sí y las consecuencias de la decisión para el proyecto y sus entregables. (Para ejemplos de estas secciones, consulte el Apéndice). Uno de los aspectos más poderosos de la estructura ADR es que se centra en la razón de la decisión en lugar de cómo la implementó el equipo. Comprender por qué el equipo tomó la decisión facilita que otros miembros del equipo adopten la decisión y evite que otros arquitectos que no estuvieran involucrados en el proceso de toma de decisiones anulen esa decisión en el futuro.


## Proceso de adopción de ADR

Cada miembro del equipo puede crear un ADR, pero el equipo debe establecer una definición de propiedad para un ADR. Cada autor que es el propietario de un ADR debe mantener y comunicar activamente el contenido de ADR. Para aclarar esta propiedad, esta guía se refiere a los autores de ADR como propietarios de ADR en las siguientes secciones. Otros miembros del equipo siempre pueden contribuir a un ADR. Si el contenido de un ADR cambia antes de que el equipo acepte el ADR, el propietario debe aprobar estos cambios.

Después de que el equipo identifica una decisión arquitectónica y su propietario, el propietario de la ADR proporciona el ADR en el estado ** propuesto ** al comienzo del proceso. Los ADR en el estado propuesto están listos para su revisión.

El propietario de ADR luego inicia el proceso de revisión para el ADR. El objetivo del proceso de revisión de ADR es decidir si el equipo acepta el ADR, determina que necesita reelaborar o rechaza el ADR. El equipo del proyecto, incluido el propietario, revisa el ADR. La reunión de revisión debe comenzar con un horario dedicado para leer el ADR. En promedio, de 10 a 15 minutos deberían ser suficientes. Durante este tiempo, cada miembro del equipo lee el documento y agrega comentarios y preguntas para marcar temas poco claros. Después de la fase de revisión, el propietario de ADR lee y discute cada comentario con el equipo.

Si el equipo encuentra puntos de acción para mejorar el ADR, el estado del ADR permanece ** propuesto **. El propietario de ADR formula las acciones y, en colaboración con el equipo, agrega un cesionario a cada acción. Cada miembro del equipo puede contribuir y resolver los puntos de acción. Es responsabilidad del propietario de ADR reprogramar el proceso de revisión.

El equipo también puede decidir rechazar el ADR. En este caso, el propietario de ADR agrega una razón para el rechazo para evitar futuras discusiones sobre el mismo tema. El propietario cambia el estado ADR a ** rechazado **.

Si el equipo aprueba el ADR, el propietario agrega una marca de tiempo, la versión y la lista de partes interesadas. El propietario luego actualiza el estado a ** aceptado **.

Los ADR y el registro de decisiones que crean representan decisiones tomadas por el equipo y proporcionan un historial de todas las decisiones. El equipo usa el ADR como referencia durante el código y las revisiones arquitectónicas cuando sea posible. Además de realizar revisiones de código, tareas de diseño y tareas de implementación, los miembros del equipo deben consultar a los ADR para decisiones estratégicas para el producto.

Como buena práctica, cada cambio de software debe pasar por revisiones por pares y requiere al menos una aprobación. Durante la revisión del código, un revisor de código puede encontrar cambios que violen uno o más ADR. En este caso, el revisor solicita al autor del cambio de código que actualice el código y comparte un enlace al ADR. Cuando el autor actualiza el código, es aprobado por los revisores de pares y se fusiona con la base del código principal.


## Proceso de revisión de ADR

El equipo debe tratar a los ADR como documentos inmutables después de que el equipo los acepta o rechaza. Los cambios en un ADR existente requieren crear un nuevo ADR, establecer un proceso de revisión para el nuevo ADR y aprobar el ADR. Si el equipo aprueba el nuevo ADR, el propietario debe cambiar el estado del antiguo ADR a ** reemplazado **.
