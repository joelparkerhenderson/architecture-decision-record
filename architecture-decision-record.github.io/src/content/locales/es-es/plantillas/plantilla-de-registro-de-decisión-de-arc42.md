# Plantilla de registro de decisión de arc42

<https://arc42.org/overview>

## 1. Introducción y objetivos

Breve descripción de los requisitos, las fuerzas impulsoras y un extracto (o resumen) de los requisitos. Los tres (como máximo cinco) objetivos de calidad principales de la arquitectura que tienen la mayor prioridad para las principales partes interesadas. Una tabla de las partes interesadas importantes con sus expectativas respecto de la arquitectura.

## 1.1 Visión general de los requisitos

### Contenido

Breve descripción de los requisitos funcionales, las fuerzas impulsoras y un extracto (o resumen) de los requisitos. Enlaces a los documentos de requisitos (que ojalá existan), indicando dónde encontrarlos. 

### Motivación

Desde el punto de vista de los usuarios finales, un sistema se crea o se modifica para mejorar el apoyo a una actividad de negocio o mejorar su calidad. 

### Forma

Breve descripción textual, probablemente en formato tabular de casos de uso. Si existen documentos de requisitos, esta visión general debe remitir a ellos.

Mantenga estos extractos lo más breves posible. Equilibre la legibilidad de este documento con la posible redundancia respecto de los documentos de requisitos. 

## 1.2 Objetivos de calidad

### Contenido

Los tres (como máximo cinco) objetivos de calidad principales de la arquitectura cuyo cumplimiento es de la mayor importancia para las principales partes interesadas. Nos referimos realmente a objetivos de calidad de la arquitectura. No los confunda con los objetivos del proyecto. No son necesariamente idénticos. La norma ISO 25010 ofrece una buena panorámica de los temas de posible interés.

### Motivación

Debe conocer los objetivos de calidad de sus partes interesadas más importantes, ya que influirán en las decisiones fundamentales de arquitectura. Sea muy concreto sobre estas cualidades y evite las palabras de moda. Si usted, como arquitecto, no sabe cómo se juzgará la calidad de su trabajo …

### Forma

Una tabla con los objetivos de calidad más importantes y escenarios concretos, ordenada por prioridades.

## 1.3 Partes interesadas

### Contenido

Panorámica explícita de las partes interesadas del sistema, es decir, todas las personas, roles u organizaciones que

- deben conocer la arquitectura

- deben quedar convencidas de la arquitectura

- tienen que trabajar con la arquitectura o con el código

- necesitan la documentación de la arquitectura para su trabajo

- tienen que tomar decisiones sobre el sistema o su desarrollo

### Motivación

Debe conocer a todas las partes implicadas en el desarrollo del sistema o afectadas por él. De lo contrario, podría llevarse desagradables sorpresas más adelante en el proceso de desarrollo. Estas partes interesadas determinan el alcance y el nivel de detalle de su trabajo y de sus resultados.

### Forma

Tabla con los nombres de los roles, los nombres de las personas y sus expectativas respecto de la arquitectura y su documentación.

## 2. Restricciones

Todo aquello que limita a los equipos en las decisiones de diseño e implementación o en las decisiones sobre procesos relacionados. A veces puede ir más allá de los sistemas individuales y ser válido para organizaciones y empresas enteras.

### Contenido

Cualquier requisito que limite la libertad de los arquitectos de software en las decisiones de diseño e implementación o en las decisiones sobre el proceso de desarrollo. Estas restricciones a veces van más allá de los sistemas individuales y son válidas para organizaciones y empresas enteras.

### Motivación

Los arquitectos deben saber exactamente dónde tienen libertad en sus decisiones de diseño y dónde deben atenerse a restricciones. Las restricciones siempre deben tratarse; sin embargo, pueden ser negociables.

### Forma

Tablas sencillas de restricciones con explicaciones. Si es necesario, puede subdividirlas en restricciones técnicas, restricciones organizativas y políticas, y convenciones (p. ej., directrices de programación o de control de versiones, convenciones de documentación o de nomenclatura)

## 3. Contexto y alcance

Delimita su sistema respecto de sus interlocutores de comunicación (externos) (sistemas vecinos y usuarios). Especifica las interfaces externas. Se muestra desde una perspectiva de negocio o dominio (siempre) o desde una perspectiva técnica (opcional)

### Contenido

El alcance y el contexto del sistema, como su nombre indica, delimitan su sistema (es decir, su alcance) respecto de todos sus interlocutores de comunicación (sistemas vecinos y usuarios, es decir, el contexto de su sistema). De este modo especifica las interfaces externas.

Si es necesario, distinga el contexto de negocio (entradas y salidas específicas del dominio) del contexto técnico (canales, protocolos, hardware).

### Motivación

Las interfaces de dominio y las interfaces técnicas con los interlocutores de comunicación figuran entre los aspectos más críticos de su sistema. Asegúrese de comprenderlas por completo.

### Forma

- Diversos diagramas de contexto

- Listas de interlocutores de comunicación y sus interfaces.

## 3.1 Contexto de negocio

### Contenido

Especificación de todos los interlocutores de comunicación (usuarios, sistemas de TI, …) con explicaciones de las entradas y salidas o interfaces específicas del dominio. Opcionalmente puede añadir formatos específicos del dominio o protocolos de comunicación.

### Motivación

Todas las partes interesadas deben entender qué datos se intercambian con el entorno del sistema.

### Forma

Todo tipo de diagramas que muestren el sistema como una caja negra y especifiquen las interfaces de dominio con los interlocutores de comunicación.

Alternativamente (o además) puede usar una tabla. El título de la tabla es el nombre de su sistema, y las tres columnas contienen el nombre del interlocutor de comunicación, las entradas y las salidas.

## 3.2 Contexto técnico

### Contenido

Interfaces técnicas (canales y medios de transmisión) que vinculan su sistema con su entorno. Además, una asignación de las entradas y salidas específicas del dominio a los canales, es decir, una explicación de qué E/S usa qué canal.

### Motivación

Muchas partes interesadas toman decisiones de arquitectura basadas en las interfaces técnicas entre el sistema y su contexto. En especial, los diseñadores de infraestructura o de hardware deciden estas interfaces técnicas.

### Forma

P. ej., un diagrama de despliegue UML que describa los canales hacia los sistemas vecinos, junto con una tabla de asignación que muestre las relaciones entre los canales y las entradas y salidas.

## 4. Estrategia de solución

Resumen de las decisiones fundamentales y las estrategias de solución que dan forma a la arquitectura. Puede incluir tecnología, descomposición de nivel superior, enfoques para lograr los objetivos de calidad principales y decisiones organizativas pertinentes.

### Contenido

Un breve resumen y explicación de las decisiones fundamentales y las estrategias de solución que dan forma a la arquitectura del sistema. Estas incluyen

- decisiones tecnológicas

- decisiones sobre la descomposición de nivel superior del sistema, p. ej., el uso de un patrón de arquitectura o un patrón de diseño

- decisiones sobre cómo lograr los objetivos de calidad clave

- decisiones organizativas pertinentes, p. ej., seleccionar un proceso de desarrollo o delegar ciertas tareas en terceros.

### Motivación

Estas decisiones constituyen los pilares de su arquitectura. Son la base de muchas otras decisiones detalladas o reglas de implementación.

### Forma

Mantenga breve la explicación de estas decisiones clave.

Motive lo que ha decidido y por qué lo decidió así, a partir de su planteamiento del problema, los objetivos de calidad y las restricciones clave. Remita a los detalles en las secciones siguientes (sección 5 para los detalles estructurales, sección 8 para los conceptos transversales).

Puede usar una lista de enfoques de solución o una tabla.

## 5. Vista de bloques de construcción

Descomposición estática del sistema, abstracciones del código fuente, mostradas como una jerarquía de cajas blancas (que contienen cajas negras), hasta el nivel de detalle adecuado.

### Contenido

La vista de bloques de construcción muestra la descomposición estática del sistema en bloques de construcción (módulos, componentes, subsistemas, clases, interfaces, paquetes, bibliotecas, frameworks, capas, particiones, niveles, funciones, macros, operaciones, estructuras de datos, …) así como sus dependencias (relaciones, asociaciones, …)

Esta vista es obligatoria en toda documentación de arquitectura. Por analogía con una casa, es el plano de planta.

### Motivación

Mantenga una visión general de su código fuente haciendo comprensible su estructura mediante la abstracción.

Esto le permite comunicarse con sus partes interesadas en un nivel abstracto sin revelar detalles de implementación.

### Forma

La vista de bloques de construcción es una colección jerárquica de cajas negras y cajas blancas (véase la figura siguiente) y sus descripciones.

## 5.1 Caja blanca del sistema completo

Aquí describe la descomposición del sistema completo usando la siguiente plantilla de caja blanca. Contiene

- un diagrama general

- una motivación de la descomposición

- descripciones de caja negra de los bloques de construcción contenidos. Para ello le ofrecemos alternativas:

  - usar una tabla para obtener una visión breve y pragmática de todos los bloques de construcción contenidos y sus interfaces

  - usar una lista de descripciones de caja negra de los bloques de construcción según la plantilla de caja negra (véase más abajo). Según la herramienta que elija, esta lista podría ser de subcapítulos (en archivos de texto), subpáginas (en un wiki) o elementos anidados (en una herramienta de modelado).

  - (opcional:) interfaces importantes que no se explican en las plantillas de caja negra de un bloque de construcción, pero que son muy importantes para entender la caja blanca.

Dado que hay tantas formas de especificar interfaces, no ofrecemos una plantilla específica para ellas.

En el mejor de los casos bastará con ejemplos o firmas sencillas.

## 5.2 Nivel 2

Aquí puede especificar la estructura interna de (algunos) bloques de construcción del nivel 1 como cajas blancas.

Debe decidir qué bloques de construcción de su sistema son lo bastante importantes como para justificar una descripción tan detallada. Prefiera la relevancia a la exhaustividad. Especifique los bloques de construcción importantes, sorprendentes, arriesgados, complejos o volátiles. Omita las partes normales, simples, aburridas o estandarizadas de su sistema

### 5.2.1 Caja blanca del bloque de construcción 1

Especifica la estructura interna del bloque de construcción 1.

Use la plantilla de caja blanca (véase más arriba).

## 6. Vista de tiempo de ejecución

Comportamiento de los bloques de construcción en forma de escenarios, que cubren casos de uso o funcionalidades importantes, interacciones en interfaces externas críticas, operación y administración, además del comportamiento ante errores y excepciones.

### Contenido

La vista de tiempo de ejecución describe el comportamiento concreto y las interacciones de los bloques de construcción del sistema en forma de escenarios de las siguientes áreas:

- casos de uso o funcionalidades importantes: ¿cómo los ejecutan los bloques de construcción?

- interacciones en interfaces externas críticas: ¿cómo cooperan los bloques de construcción con los usuarios y los sistemas vecinos?

- operación y administración: lanzamiento, arranque, parada

- escenarios de error y de excepción

Observación: el criterio principal para elegir los posibles escenarios (secuencias, flujos de trabajo) es su relevancia para la arquitectura. No es importante describir un gran número de escenarios. Es preferible documentar una selección representativa.

### Motivación

Debe entender cómo (las instancias de) los bloques de construcción de su sistema realizan su trabajo y se comunican en tiempo de ejecución. Documentará principalmente escenarios para comunicar su arquitectura a las partes interesadas que están menos dispuestas o menos capacitadas para leer y entender los modelos estáticos (vista de bloques de construcción, vista de despliegue).

### Forma

Existen muchas notaciones para describir escenarios, p. ej.


- lista numerada de pasos (en lenguaje natural)

- diagramas de actividad o diagramas de flujo

- diagramas de secuencia

- BPMN o EPC (cadenas de procesos de eventos)

- máquinas de estados

- etc.

## 6.n Escenario de tiempo de ejecución n (1, 2, 3, etc.)

Inserte un diagrama de tiempo de ejecución o una descripción textual del escenario.

Inserte una descripción de los aspectos destacables de las interacciones entre las instancias de bloques de construcción representadas en este diagrama.

## 7. Vista de despliegue

Infraestructura técnica con entornos, computadoras, procesadores y topologías. Asignación de bloques de construcción (de software) a elementos de la infraestructura.

### Contenido

La vista de despliegue describe:

- la infraestructura técnica utilizada para ejecutar su sistema, con elementos de infraestructura como ubicaciones geográficas, entornos, computadoras, procesadores, canales y topologías de red, así como otros elementos de infraestructura, y

- la asignación de bloques de construcción (de software) a esos elementos de infraestructura.

A menudo los sistemas se ejecutan en distintos entornos, p. ej., entorno de desarrollo, entorno de pruebas, entorno de producción. En tales casos debe documentar todos los entornos pertinentes.

Documente en especial la vista de despliegue cuando su software se ejecute como un sistema distribuido con más de una computadora, procesador, servidor o contenedor, o cuando diseñe y construya sus propios procesadores y chips de hardware.

Desde una perspectiva de software, basta con capturar aquellos elementos de la infraestructura que se necesitan para mostrar el despliegue de sus bloques de construcción. Los arquitectos de hardware pueden ir más allá y describir la infraestructura con el nivel de detalle que necesiten reflejar. 

### Motivación

El software no funciona sin hardware. Esta infraestructura subyacente puede influir, y de hecho influirá, en su sistema y en algunos conceptos transversales. Por lo tanto, necesita conocer la infraestructura.

### Forma

Quizá el diagrama de despliegue de nivel más alto ya esté contenido en la sección 3.2 como contexto técnico, con su propia infraestructura como UNA caja negra. En esta sección ampliará esa caja negra mediante diagramas de despliegue adicionales.

- UML ofrece diagramas de despliegue para expresar esa vista. Úselos, probablemente con diagramas anidados, cuando su infraestructura sea más compleja.

- Cuando sus partes interesadas (de hardware) prefieran otros tipos de diagramas en lugar del diagrama de despliegue UML, permítales usar cualquier tipo que pueda mostrar nodos y canales de la infraestructura.

## 7.1 Infraestructura, nivel 1

Describa (normalmente con una combinación de diagramas, tablas y texto):

- la distribución de su sistema en múltiples ubicaciones, entornos, computadoras, procesadores, .. así como las conexiones físicas entre ellos

- la justificación o motivación importante de esta estructura de despliegue

- las características de calidad o rendimiento de la infraestructura

- la asignación de artefactos de software (bloques de construcción) a elementos de la infraestructura

Para múltiples entornos o despliegues alternativos, copie esa sección de arc42 para todos los entornos pertinentes. **

## 7.2 Infraestructura, nivel 2

Aquí puede incluir la estructura interna de (algunos) elementos de infraestructura del nivel 1 de infraestructura.

Copie la estructura del nivel 1 para cada elemento seleccionado.

## 8. Conceptos transversales

En conjunto, las regulaciones principales y los enfoques de solución pertinentes en varias partes (→ transversales) del sistema. Los conceptos suelen estar relacionados con varios bloques de construcción. Incluya temas diversos como modelos de dominio, patrones y estilos de arquitectura, reglas para el uso de tecnologías específicas y reglas de implementación.

### Contenido

Esta sección describe conceptos transversales (prácticas, patrones, regulaciones o ideas de solución). Tales conceptos suelen estar relacionados con varios bloques de construcción. Pueden abarcar muchos temas distintos.

### Motivación

Los conceptos constituyen la base de la integridad conceptual (coherencia, homogeneidad) de la arquitectura. Por lo tanto, contribuyen de forma importante a lograr las cualidades internas de su sistema.

Este es el lugar de la plantilla que hemos previsto para una especificación cohesionada de tales conceptos.

Muchos de estos conceptos se relacionan con varios de sus bloques de construcción o influyen en ellos.

### Forma

La forma puede variar:

- documentos conceptuales con cualquier tipo de estructura

- implementaciones de ejemplo, especialmente para conceptos técnicos

- extractos de modelos transversales o escenarios con las notaciones de las vistas de arquitectura

### Estructura de esta sección

Elija solo los temas más necesarios para su sistema y asigne a cada uno un encabezado de nivel 2 en esta sección (p. ej., 8.1, 8.2, etc.).

- NO INTENTE cubrir todos los temas del diagrama mencionado.

### Antecedentes

Algunos temas dentro de los sistemas afectan con frecuencia a varios bloques de construcción, elementos de hardware o procesos de desarrollo. Puede ser más fácil comunicar o documentar estos temas transversales en un lugar central, en lugar de repetirlos en la descripción de los bloques de construcción, elementos de hardware o procesos de desarrollo afectados.

Ciertos conceptos pueden afectar a todos los elementos de un sistema, otros pueden ser pertinentes solo para unos pocos.

## 9. Decisiones de arquitectura

Decisiones de arquitectura importantes, costosas, críticas, de gran escala o arriesgadas, incluidas sus justificaciones.

### Contenido

Decisiones de arquitectura importantes, costosas, de gran escala o arriesgadas, incluidas sus justificaciones. Por «decisiones» entendemos seleccionar una alternativa en función de unos criterios dados.

Use su criterio para decidir si una decisión de arquitectura debe documentarse aquí, en esta sección central, o si es mejor documentarla localmente (p. ej., dentro de la plantilla de caja blanca de un bloque de construcción). Evite los textos redundantes. Remita a la sección 4, donde ya registró las decisiones más importantes de su arquitectura.

### Motivación

Las partes interesadas de su sistema deben poder comprender y reconstruir sus decisiones.

### Forma

- ADR (registro de decisión de arquitectura) para cada decisión importante

- lista o tabla, ordenada por importancia y consecuencias, o

- con más detalle, en forma de secciones separadas por decisión

### Antecedentes (sobre los ADR)

Las piezas de documentación más pequeñas son más fáciles de leer, crear y mantener. En lo que respecta a las decisiones de arquitectura, los equipos de desarrollo a menudo:

- conocen la decisión, ya que es visible, p. ej., en el código fuente, pero

- desconocen la motivación detrás de esa decisión (véase Nygard 2011)

Por ello debe documentar unas pocas decisiones importantes junto con su motivación y razonamiento

### Nuestra propuesta sobre las decisiones

Mantenga una colección de decisiones significativas para la arquitectura, es decir, aquellas decisiones que afectan a la estructura, a las características de calidad, a las dependencias e interfaces importantes (especialmente externas) o a las técnicas de construcción (gracias a Michael Nygard por esta propuesta).

## 10. Requisitos de calidad

Requisitos de calidad como escenarios, con un árbol de calidad que ofrezca una visión general de alto nivel. Los objetivos de calidad más importantes deberían haberse descrito en la sección 1.2. (objetivos de calidad).

### Contenido

Esta sección contiene todos los requisitos de calidad pertinentes.

Los más importantes de estos requisitos ya se han descrito en la sección 1.2. (objetivos de calidad), por lo que aquí solo deben referenciarse. En esta sección 10 también debe recoger los requisitos de calidad de menor importancia, que no crearán riesgos elevados si no se logran por completo (pero que serían deseables).

### Motivación

Dado que los requisitos de calidad tendrán mucha influencia en las decisiones de arquitectura, debe saber qué cualidades son realmente importantes para sus partes interesadas, de manera específica y medible.

### Más información

Consulte el extenso modelo de calidad Q42 en https://quality.arc42.org.

## 10.1 Visión general de los requisitos de calidad

### Contenido

Una visión general o resumen de los requisitos de calidad.

### Motivación

A menudo nos encontramos con docenas (o incluso cientos) de requisitos de calidad detallados. En esta sección de visión general debería intentar resumirlos, p. ej., describiendo categorías o temas (como sugieren ISO 25010:2023 o Q42

Si estas descripciones resumidas ya son precisas, lo bastante específicas y medibles, puede omitir la sección 10.2.

### Forma

Use una tabla sencilla en la que cada línea contenga una categoría o tema y una breve descripción del requisito de calidad. Alternativamente, puede usar un mapa mental para estructurar estos requisitos de calidad.

En la bibliografía también se ha descrito la idea de un árbol de atributos de calidad, que sitúa el término genérico «calidad» como raíz y utiliza un refinamiento en forma de árbol del término «calidad». [Bass+21] introdujo con este fin el término «Quality Attribute Utility Tree».

## 10.2 Escenarios de calidad

### Contenido

Los escenarios de calidad concretan los requisitos de calidad y permiten decidir si se cumplen (en el sentido de criterios de aceptación). Asegúrese de que sus escenarios sean específicos y medibles.

Dos tipos de escenarios son especialmente útiles:

- Los escenarios de uso (también llamados escenarios de aplicación o escenarios de casos de uso) describen la reacción del sistema en tiempo de ejecución ante cierto estímulo. Esto incluye también los escenarios que describen la eficiencia o el rendimiento del sistema. Ejemplo: el sistema reacciona a la solicitud de un usuario en un segundo.

- Los escenarios de cambio describen el efecto deseado de una modificación o ampliación del sistema o de su entorno inmediato. Ejemplo: se implementa una funcionalidad adicional o cambian los requisitos de un atributo de calidad, y se mide el esfuerzo o la duración del cambio.

### Forma

La información típica de los escenarios detallados incluye lo siguiente:

En forma corta (preferida en el modelo Q42):

- Contexto/antecedentes: ¿qué tipo de sistema o componente, cuál es el entorno o la situación?

- Fuente/estímulo: quién o qué inicia o desencadena un comportamiento, una reacción o una acción.

- Métrica/criterios de aceptación: una respuesta que incluye una medida o métrica

La forma larga de los escenarios (preferida por el SEI y [Bass+21]) es más detallada e incluye la siguiente información:

- ID del escenario: un identificador único del escenario.

- Nombre del escenario: un nombre breve y descriptivo del escenario.

- Fuente: la entidad (usuario, sistema o evento) que inicia el escenario.

- Estímulo: el evento o la condición desencadenante que el sistema debe atender.

- Entorno: el contexto operativo o la condición en que el sistema experimenta el estímulo.

- Artefacto: los bloques de construcción u otros elementos del sistema afectados por el estímulo.

- Respuesta: el resultado o comportamiento que muestra el sistema en reacción al estímulo.

- Medida de la respuesta: el criterio o la métrica con que se evalúa la respuesta del sistema.

### Véase también

Desde enero de 2023, arc42 ofrece un modelo de calidad pragmático, que propone etiquetar los requisitos de calidad con hashtags o etiquetas como #flexible, #efficient, #usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Riesgos y deuda técnica

Riesgos técnicos o deuda técnica conocidos. ¿Qué problemas potenciales existen dentro del sistema o a su alrededor? ¿Qué es lo que más incomoda al equipo de desarrollo?

### Contenido

Una lista de riesgos técnicos o deudas técnicas identificados, ordenada por prioridad

### Motivación

«La gestión de riesgos es la gestión de proyectos para adultos» (Tim Lister, Atlantic Systems Guild).

Este debe ser su lema para la detección y evaluación sistemáticas de los riesgos y las deudas técnicas de la arquitectura, que necesitarán las partes interesadas de gestión (p. ej., directores de proyecto, responsables de producto) como parte del análisis global de riesgos y de la planificación de medidas.

### Forma

Lista de riesgos o deudas técnicas, que probablemente incluya medidas sugeridas para minimizar, mitigar o evitar riesgos o reducir deudas técnicas.
