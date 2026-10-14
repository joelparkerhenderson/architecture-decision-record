# Registro de decisión de arquitectura (ADR)

Un registro de decisión de arquitectura (ADR) es un documento que recoge una decisión de arquitectura importante junto con su contexto y sus consecuencias.

> [!IMPORTANT]
> Haz tu propia diligencia debida sobre estos recursos antes de usarlos en cualquier sistema crítico.

Contenido:

- [¿Qué es un registro de decisión de arquitectura?](#qué-es-un-registro-de-decisión-de-arquitectura)
- [Cómo empezar a usar ADR](#cómo-empezar-a-usar-adr)
- [Cómo empezar a usar ADR con herramientas](#cómo-empezar-a-usar-adr-con-herramientas)
- [Cómo empezar a usar ADR con git](#cómo-empezar-a-usar-adr-con-git)
- [Habilidades de Claude Code para ADR](#habilidades-de-claude-code-para-adr)
- [Convenciones de nombres de archivo](#convenciones-de-nombres-de-archivo)
- [Sugerencias para escribir buenos ADR](#sugerencias-para-escribir-buenos-adr)
- [Plantillas de ejemplo de ADR](#plantillas-de-ejemplo-de-adr)
- [Consejos de trabajo en equipo para ADR](#consejos-de-trabajo-en-equipo-para-adr)
- [Preguntas de trabajo en equipo para ADR](#preguntas-de-trabajo-en-equipo-para-adr)
- [Conceptos del siguiente paso para ADR](#conceptos-del-siguiente-paso-para-adr)
- [Diagramas, vistas y puntos de vista de arquitectura](#diagramas-vistas-y-puntos-de-vista-de-arquitectura)
- [Funciones de aptitud para decisiones como código](#funciones-de-aptitud-para-decisiones-como-código)
- [Barreras de decisión para pull requests](#barreras-de-decisión-para-pull-requests)
- [Para más información](#para-más-información)

Plantillas:

- [Plantilla de registro de decisión de Jeff Tyree y Art Akerman](plantillas/plantilla-de-registro-de-decisión-de-jeff-tyree-y-art-akerman/)
- [Plantilla de registro de decisión de Michael Nygard](plantillas/plantilla-de-registro-de-decisión-de-michael-nygard/)
- [Plantilla de registro de decisión de EdgeX](plantillas/plantilla-de-registro-de-decisión-de-edgex/)
- [Plantilla de registro de decisión de arc42](plantillas/plantilla-de-registro-de-decisión-de-arc42/)
- [Plantilla de registro de decisión para el patrón alejandrino](plantillas/plantilla-de-registro-de-decisión-para-el-patrón-alejandrino/)
- [Plantilla de registro de decisión para un caso de negocio](plantillas/plantilla-de-registro-de-decisión-para-caso-de-negocio/)
- [Plantilla de registro de decisión del proyecto MADR](plantillas/plantilla-de-registro-de-decisión-del-proyecto-madr/)
- [Plantilla de registro de decisión usando Planguage](plantillas/plantilla-de-registro-de-decisión-usando-planguage/)
- [Plantilla de registro de decisión de Paulo Merson](https://github.com/pmerson/ADR-template)
- [Plantilla de registro de decisión de Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Plantilla de registro de decisión de Gareth Morgan](plantillas/plantilla-de-registro-de-decisión-de-gareth-morgan/)
- [Plantilla de registro de decisión de GIG Cymru NHS Wales](plantillas/plantilla-de-registro-de-decisión-de-gig-cymru-nhs-wales/)
- [Plantilla de registro de decisión para decisiones técnicas importantes (ITD) de Ignacio Larrañaga](plantillas/plantilla-de-registro-de-decisión-para-decisiones-técnicas-importantes/)

Ejemplos:

- [Framework CSS](ejemplos/framework-css/)
- [Configuración con variables de entorno](ejemplos/configuración-con-variables-de-entorno/)
- [Métricas, monitores, alertas](ejemplos/métricas-monitores-alertas/)
- [Microsoft Azure DevOps](ejemplos/microsoft-azure-devops/)
- [Monorepo frente a multirepo](ejemplos/monorepo-frente-a-multirepo/)
- [Lenguajes de programación](ejemplos/lenguajes-de-programación/)
- [Almacenamiento de secretos](ejemplos/almacenamiento-de-secretos/)
- [Formato de marca de tiempo](ejemplos/formato-de-marca-de-tiempo/)
- [Muchos más...](ejemplos/)

## ¿Qué es un registro de decisión de arquitectura?

Un **registro de decisión de arquitectura** (architecture decision record, ADR) es un documento que recoge una decisión de arquitectura importante junto con su contexto y sus consecuencias.

Una **decisión de arquitectura** (architecture decision, AD) es una elección de diseño de software que responde a un requisito significativo.

Un **registro de decisiones de arquitectura** (architecture decision log, ADL) es el conjunto de todos los ADR creados y mantenidos para un proyecto (u organización) determinado.

Un **requisito significativo para la arquitectura** (architecturally-significant requirement, ASR) es un requisito que tiene un efecto medible en la arquitectura de un sistema de software.

Todo ello pertenece al tema de la **gestión del conocimiento de arquitectura** (architecture knowledge management, AKM).

El objetivo de este documento es ofrecer una visión rápida de los ADR, de cómo crearlos y de dónde buscar más información.

Abreviaturas:

  * **AD**: decisión de arquitectura

  * **ADL**: registro de decisiones de arquitectura

  * **ADR**: registro de decisión de arquitectura

  * **AKM**: gestión del conocimiento de arquitectura

  * **ASR**: requisito significativo para la arquitectura

## Cómo empezar a usar ADR

Para empezar a usar ADR, converse con sus compañeros de equipo sobre estas áreas.

Identificación de decisiones:

  * ¿Qué tan urgente y qué tan importante es la AD?

  * ¿Debe tomarse ahora o puede esperar hasta que se conozca más?

  * La experiencia personal y colectiva, así como los métodos y prácticas de diseño reconocidos, pueden ayudar a identificar decisiones.

  * Lo ideal es mantener una lista de decisiones pendientes que complemente la lista de tareas pendientes del producto.

Toma de decisiones:

  * Existen varias técnicas de toma de decisiones, tanto generales como específicas de la arquitectura de software, por ejemplo, el mapeo de diálogos.

  * La toma de decisiones en grupo es un tema de investigación activo.

Puesta en práctica y cumplimiento de las decisiones:

  * Las AD se usan en el diseño de software; por lo tanto, deben comunicarse a las partes interesadas del sistema que lo financian, desarrollan y operan, y ser aceptadas por ellas.

  * Los estilos de codificación con arquitectura evidente y las revisiones de código centradas en cuestiones y decisiones de arquitectura son dos prácticas relacionadas.

  * Las AD también deben (re)considerarse al modernizar un sistema de software durante su evolución.

Compartir decisiones (opcional):

  * Muchas AD se repiten entre proyectos.

  * Por ello, las experiencias con decisiones pasadas, buenas y malas, pueden ser activos reutilizables valiosos cuando se emplea una estrategia explícita de gestión del conocimiento.

Documentación de decisiones:

  * Existen muchas plantillas y herramientas para registrar decisiones.

  * Consulte las comunidades ágiles, por ejemplo, los ADR de M. Nygard.

  * Consulte los procesos tradicionales de ingeniería de software y diseño de arquitectura, por ejemplo, los diseños de tabla sugeridos por IBM UMF y por Tyree y Akerman, de CapitalOne.

Para más información:

  * Los pasos anteriores se han adoptado de la entrada de Wikipedia sobre [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Cómo empezar a usar ADR con herramientas

- [MySpec](https://myspec.dev) — Plataforma automatizada de especificaciones y decisiones de arquitectura que estructura la constitución del proyecto, la arquitectura técnica y los ADR en Markdown limpio servido mediante MCP.

Puede empezar a usar ADR con herramientas de la manera que prefiera.

Por ejemplo:

  * Si le gusta usar Google Drive y la edición en línea, puede crear un documento de Google Docs o una hoja de cálculo de Google Sheets.

  * Si le gusta usar el control de versiones del código fuente, como git, puede crear un archivo para cada ADR.

  * Si le gusta usar herramientas de planificación de proyectos, como Atlassian Jira, puede usar el seguimiento de planificación de la herramienta.

  * Si le gustan los wikis, como MediaWiki, puede crear un wiki de ADR.

## Cómo empezar a usar ADR con git

Si le gusta usar el control de versiones git, esta es la forma en que preferimos empezar a usar ADR con git en un proyecto de software típico con código fuente.

Cree un directorio para los archivos ADR:

```sh
$ mkdir adr
```

Para cada ADR, cree un archivo de texto, como `database.txt`:

```sh
$ vi database.txt
```

Escriba en el ADR lo que quiera. Consulte las plantillas de este repositorio para obtener ideas.

Confirme (commit) el ADR en su repositorio git.

## Habilidades de Claude Code para ADR

Este repositorio incluye dos habilidades (skills) de [Claude Code](https://claude.com/claude-code) en [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), para que un agente de programación con IA pueda escribir y mantener ADR como recomienda este proyecto:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — de uso general, para cualquiera que escriba un ADR en cualquier proyecto. Ayuda a decidir si una decisión necesita un ADR, crea un directorio `adr/` o `decisions/`, nombra el archivo, elige una plantilla entre los once esqueletos incluidos y redacta secciones sólidas de contexto, decisión y consecuencias.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — específicamente para quienes mantienen este repositorio. Documenta la estructura del repositorio, la convención de reflejar README y locales, y los pasos exactos para añadir una plantilla, un ejemplo o un enlace de herramienta.

Para usar una habilidad, copia su carpeta en `.claude/skills/` en la raíz del repositorio en el que trabajas (o en `~/.claude/skills/` para tenerla disponible en todos los proyectos) y luego pide a Claude Code que escriba o revise un ADR.

## Convenciones de nombres de archivo

Si decide crear sus ADR con archivos de texto comunes, quizá quiera definir su propia convención de nombres de archivo para los ADR.

Preferimos una convención de nombres de archivo con un formato específico.

Ejemplos:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Nuestra convención de nombres de archivo:

  * El nombre contiene una frase verbal en imperativo y en tiempo presente. Esto facilita la lectura y coincide con nuestro formato de mensajes de commit.

  * El nombre usa minúsculas y guiones (igual que este repositorio). Es un equilibrio entre legibilidad y facilidad de uso en el sistema.

  * La extensión es markdown. Esto puede ser útil para dar formato fácilmente.

## Sugerencias para escribir buenos ADR

Características de un buen ADR:

* Justificación (Rationale): explique las razones para tomar esa AD en particular. Puede incluir el contexto (véase más abajo), las ventajas y desventajas de las distintas opciones posibles, comparaciones de funcionalidades, análisis de costo-beneficio y más.

* Específico (Specific): cada ADR debe tratar sobre una sola AD, no sobre varias.

* Marcas de tiempo (Timestamps): indique cuándo se escribió cada elemento del ADR. Esto es especialmente importante para los aspectos que pueden cambiar con el tiempo, como costos, calendarios, escalado y similares.

* Inmutable (Immutable): no modifique la información existente en un ADR. En su lugar, enmiende el ADR añadiendo información nueva, o sustitúyalo creando un nuevo ADR.

Características de una buena sección de «Contexto» en un ADR:

* Explique la situación y las prioridades de negocio de su organización.

* Incluya justificaciones y consideraciones basadas en la composición social y de habilidades de sus equipos.

* Incluya ventajas y desventajas pertinentes, y descríbalas en términos que se alineen con sus necesidades y objetivos.

Características de una buena sección de «Consecuencias» en un ADR:

* Explique lo que se deriva de tomar la decisión. Esto puede incluir efectos, resultados, productos, seguimientos y más.

* Incluya información sobre cualquier ADR posterior. Es relativamente común que un ADR genere la necesidad de más ADR, por ejemplo, cuando un ADR toma una gran decisión general que a su vez crea la necesidad de decisiones menores.

* Incluya los procesos de revisión posterior a la acción. Es habitual que los equipos revisen cada ADR un mes después, para comparar la información del ADR con lo ocurrido en la práctica y así aprender y mejorar.

Un nuevo ADR puede sustituir a un ADR anterior:

* Cuando se toma una AD que reemplaza o invalida un ADR anterior, debe crearse un nuevo ADR

## Plantillas de ejemplo de ADR

Plantillas de ejemplo de ADR que hemos recopilado en la red:

- [Plantilla de ADR de Michael Nygard](plantillas/plantilla-de-registro-de-decisión-de-michael-nygard/) (sencilla y popular)

- [Plantilla de ADR de Jeff Tyree y Art Akerman](plantillas/plantilla-de-registro-de-decisión-de-jeff-tyree-y-art-akerman/) (más sofisticada)

- [Plantilla de ADR para el patrón Alexandrian](plantillas/plantilla-de-registro-de-decisión-para-el-patrón-alejandrino/) (sencilla, con detalles de contexto)

- [Plantilla de ADR para un caso de negocio](plantillas/plantilla-de-registro-de-decisión-para-caso-de-negocio/) (más orientada a MBA, con costes, SWOT y más opiniones)

- [Plantilla de ADR del proyecto Markdown Any Decision Records (MADR)](plantillas/plantilla-de-registro-de-decisión-del-proyecto-madr/) (versión sencilla y versión elaborada; esta última destaca las opciones y sus pros y contras)

- [Plantilla de ADR con Planguage](plantillas/plantilla-de-registro-de-decisión-usando-planguage/) (más orientada al aseguramiento de la calidad)

- [Plantilla para Decisiones Técnicas Importantes (ITD) de Ignacio Larrañaga](plantillas/plantilla-de-registro-de-decisión-para-decisiones-técnicas-importantes/) (ligera y con la decisión primero, optimizada para una revisión ejecutiva rápida)

## Consejos de trabajo en equipo para ADR

Si está considerando usar registros de decisión con su equipo, estos son algunos consejos que hemos aprendido trabajando con muchos equipos.

Tiene la oportunidad de liderar a sus compañeros conversando juntos sobre el «porqué», en lugar de imponer el «qué». Por ejemplo, los registros de decisión son una forma de que los equipos piensen mejor y se comuniquen mejor; no tienen valor si son solo un requisito burocrático forzado después de los hechos.

A algunos equipos les gusta mucho más el nombre «decisiones» que la abreviatura «ADR». Cuando algunos equipos usan «decisions» como nombre de directorio, es como si se encendiera una bombilla, y el equipo empieza a poner más información en el directorio, como decisiones de proveedores, decisiones de planificación, decisiones de calendario, etc. Todos estos tipos de información pueden usar la misma plantilla. Planteamos como hipótesis que las personas aprenden más rápido con palabras («decisiones») que con abreviaturas («ADR»), que se motivan más a escribir documentos de trabajo en curso cuando se elimina la palabra «registro», y que además a algunos desarrolladores y algunos gerentes no les gusta la palabra «arquitectura».

En teoría, la inmutabilidad es lo ideal. En la práctica, la mutabilidad ha funcionado mejor para nuestros equipos. Insertamos la información nueva en el ADR existente, con una marca de fecha y una nota que indica que la información llegó después de la decisión. Este tipo de enfoque da lugar a un «documento vivo» que todos podemos actualizar. Las actualizaciones típicas se producen cuando obtenemos información gracias a nuevos compañeros, a nuevas ofertas o a resultados reales de nuestros usos, o después de cambios de terceros, como las capacidades de los proveedores, los planes de precios, los acuerdos de licencia, etc.

## Preguntas de trabajo en equipo para ADR

### ¿Quién puede crear un ADR?

Considere aspectos como personas específicas, roles específicos, equipos específicos o departamentos específicos; considere también si hay personas, roles, equipos o departamentos que puedan encargar un ADR, es decir, solicitar uno que otra persona redactará.

Respuesta de ejemplo: cualquier persona de nuestra organización que haya leído la página README del registro de decisión de arquitectura puede proponer un ADR, es decir, puede empezar a redactarlo y compartirlo con el equipo.

### ¿Qué justifica elaborar un ADR?

Considere aspectos como las formas de trabajo de los equipos de su organización, la estructura de su sistema de software, la coordinación entre equipos, la mantenibilidad a largo plazo, las interfaces externas, a quién quiere beneficiar y similares.

Respuesta de ejemplo: queremos crear un ADR cuando queremos que los futuros desarrolladores comprendan el «porqué» de lo que hacemos.

### ¿Qué justifica no elaborar un ADR?

Considere aspectos como las decisiones que no son de arquitectura, o que son pequeñas, por ejemplo de riesgo mínimo, autocontenidas o de un solo desarrollador, o que ya están totalmente cubiertas en otro lugar, como en estándares, políticas o documentación, o que son temporales, como soluciones provisionales, pruebas de concepto o experimentos.

Respuesta de ejemplo: queremos omitir un ADR cuando una decisión tiene alcance, tiempo, riesgo y costo limitados, o ya está cubierta en otro lugar.

### ¿Cuál es el ciclo de vida de un ADR?

Considere aspectos como el proceso de creación, el proceso de investigación, el proceso de decisión, el proceso de implementación y el proceso de retiro. Considere cómo hacer el seguimiento del ciclo de vida del ADR a lo largo del tiempo, por ejemplo, cómo pasar el ADR de un estado al siguiente, y también cómo comunicarlo a las partes interesadas.

Respuesta de ejemplo: queremos que un ADR tenga cinco etapas de ciclo de vida: Inicio → Investigación → Evaluación → Implementación → Mantenimiento → Retiro.

### ¿Cuáles son los criterios para las etapas del ciclo de vida de un ADR?

Considere aspectos como los criterios de aceptación de un ADR, es decir, ¿cómo sabe que es lo bastante bueno para pasar de una etapa del ciclo de vida a la siguiente? ¿Se ha expresado el problema con claridad? ¿Se han considerado las alternativas? ¿Se comprenden y documentan lo bastante bien las compensaciones (trade-offs)? ¿Está presente todo el contexto relevante? ¿Participan todas las partes interesadas relevantes? ¿Se ha incorporado todo el feedback?

Respuesta de ejemplo: queremos que las partes interesadas voten un ADR cuando el equipo activo haya 1) completado su investigación, 2) completado su evaluación, 3) publicado la propuesta de ADR para las partes interesadas con una solicitud de comentarios y un plazo de una semana, 4) incorporado y atendido todos los comentarios de las partes interesadas.

### ¿Qué roles y responsabilidades interactúan con un ADR?

Considere roles como proponente, investigador, evaluador, revisor, aprobador, mantenedor y similares. Considere responsabilidades como la comunicación con las partes interesadas, asegurar que se cumplan las expectativas, compartir en el sitio web o la intranet, y revisar el trabajo periódicamente y, en especial, cuando ocurran cambios relevantes.

Respuesta de ejemplo: queremos que cada ADR tenga siempre una persona de contacto principal, una persona de contacto secundaria y un equipo responsable; estos se encargan de las comunicaciones, las publicaciones, el mantenimiento, la revisión periódica al menos una vez al año y, llegado el caso, el retiro final.

### ¿Cómo interactúa la gobernanza con un ADR?

Considere aspectos como las formas de trabajo de su organización, cualquier necesidad especial de cumplimiento, por ejemplo en aspectos legales o de recursos humanos, y cómo quiere manejar el consenso frente al conflicto frente a la escalación. ¿Hay áreas, personas o equipos que puedan tener más influencia que otros respecto de un ADR, por ejemplo, poder aprobarlo, votarlo o vetarlo?

Respuesta de ejemplo: la gobernanza de un ADR sigue este orden de prioridad: el CEO, el CTO, el CLO, el equipo que implementa un ADR, los expertos del equipo que más conocen el ADD. Nadie más tiene gobernanza, a menos que se describa en el ADR.

### ¿Qué principios interactúan con un ADR?

Considere aspectos como las formas de trabajo de su organización que incluyen avanzar rápido frente a avanzar despacio, consenso en las decisiones frente a conflicto en las decisiones, preferencias de riesgo frente a preferencias de seguridad, discusión pública frente a discusión privada y similares.

Respuesta de ejemplo: usamos los principios de liderazgo de sesgo hacia la acción, disentir y comprometerse (disagree-and-commit), estimaciones del 70 % suficientes para decisiones fáciles de revertir y de aislar, y formas de trabajo públicas, con excepción de la información confidencial según se describe en el acuerdo de confidencialidad de nuestra organización.

## Conceptos del siguiente paso para ADR

[Arc42](https://arc42.org/) responde a dos preguntas de forma pragmática y se puede adaptar a tus necesidades. ¿Qué deberías documentar/comunicar sobre tu arquitectura? ¿Cómo deberías documentarlo/comunicarlo? Arc42 incluye registros de decisiones de arquitectura y orientación sobre objetivos, restricciones, contextos, calidad, riesgos y más.

[El modelo C4](https://c4model.com/) es un enfoque fácil de aprender y amigable para desarrolladores para diagramar la arquitectura de software. C4 es un conjunto de diagramas jerárquicos de contexto, contenedores, componentes y código, además de diagramas de apoyo para el panorama de sistemas, la dinámica y el despliegue.

## Diagramas, vistas y puntos de vista de arquitectura

Un diagrama de arquitectura se llama "vista de arquitectura".

Una "vista de arquitectura" es una instancia de un "punto de vista de arquitectura".

Un "punto de vista de arquitectura" tiene en cuenta a un público específico con preocupaciones específicas.

Ejemplos de puntos de vista, vistas y diagramas de arquitectura:

- Capacidades de negocio

- Procesos de negocio de alto nivel

- [Flujos de valor](https://en.wikipedia.org/wiki/Value_stream)

- Funciones de software asignadas a componentes de aplicación

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Diagrama de contexto (TO-BE / AS-IS)

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Diagrama de contenedores (TO-BE / AS-IS)

- [Diagrama entidad-relación](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) para asignar entidades de datos a componentes de aplicación

- [Diagramas de secuencia](https://en.wikipedia.org/wiki/Sequence_diagram) para describir flujos funcionales dentro de los sistemas y en las integraciones

- [Notación y Modelo de Procesos de Negocio](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagramas para describir flujos de datos entre componentes de aplicación

- [Notación y Modelo de Procesos de Negocio](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagramas para describir procesos de negocio / escenarios de usuario

- [Gestión de Identidades y Accesos](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) diagramas

- [Control de Acceso Basado en Roles](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) diagramas con roles por componente de aplicación

- [Control de Acceso Basado en Atributos](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) diagramas con atributos por componente de aplicación

- Diagramas de privacidad

Diagramas relacionados:

- Un diagrama de casos de uso muestra casos de uso a la dirección/los clientes, lo que precede a los requisitos, que preceden a la arquitectura de software.

- Un diagrama de despliegue muestra el hardware/los equipos físicos en los que se despliegan los componentes de software.
- Un diagrama de flujo de datos muestra cómo se mueven y se transforman los datos en el sistema.
- Un diagrama de secuencia se usa para mostrar cómo funcionan protocolos como HTTP sobre un eje temporal.

- Un diagrama de actividades representa el flujo de trabajo de las actividades que realiza un sistema de software, como una IA de NPC.

## Funciones de aptitud para decisiones como código

Las funciones de aptitud (fitness functions) son comprobaciones automatizadas y objetivas, escritas con código de programación, que verifican que las decisiones se mantienen.

- Las funciones de aptitud hacen que las decisiones sean comprobables y verificables.

- Las funciones de aptitud para decisiones pueden ayudar mucho a los objetivos de aseguramiento de la calidad, de los procesos regulatorios y de gobernanza.

### Cómo se relacionan las funciones de aptitud con las decisiones

Un registro de decisión documenta la decisión, mientras que una función de aptitud la asegura.

- Decisión de ejemplo: usamos event sourcing para los requisitos de auditoría.

- Función de aptitud de ejemplo: usamos el servidor de integración continua para comprobar que todos los cambios de estado deben producir eventos.

### Por qué las funciones de aptitud ayudan a las decisiones

Mediciones objetivas: las funciones de aptitud pasan o fallan, por lo que el trabajo es visible y claro.

Uso continuo: las funciones de aptitud son sus reglas vivas, y se ejecutan en cada commit y en cada compilación.

Confianza para refactorizar: las funciones de aptitud detectan automáticamente los errores en las reglas de decisión.

Gobernanza escalable: las funciones de aptitud aseguran los estándares sin crear cuellos de botella.

### ¿Pueden las funciones de aptitud usar IA?

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

### Pruebas unitarias de arquitectura

[ArchUnit](https://www.archunit.org/): comprueba las reglas de arquitectura del código Java usando cualquier framework de pruebas unitarias de Java.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): comprueba las reglas de arquitectura del código TypeScript y JavaScript usando Jest, Vitest, Jasmine, etc.

## Barreras de decisión para pull requests

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
muestra automáticamente los registros de decisión adecuados en el momento adecuado: cuando un
desarrollador modifica activamente el código que esas decisiones cubren. En lugar de esperar que los desarrolladores
lean una carpeta de documentos antes de fusionar, el contexto relevante aparece directamente en el pull request.

Esto funciona con cualquier tipo de registro de decisión: decisiones de arquitectura, de datos, de cumplimiento normativo, clínicas y médicas, de seguridad y más.

Funciona con cualquier sistema de CI (GitLab, Jenkins, CircleCI) y como hook de pre-commit.
Código abierto. Licencia MIT.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) es una GitHub
Action que hace fallar un pull request cuando cambian rutas de código vigiladas sin que se añada o actualice un
registro de decisión de arquitectura. Las excepciones son explícitas: una línea
`ADR-Exempt:` con un motivo supera la puerta y se escribe en el resumen del trabajo. Independiente de la plantilla, sin dependencias. Código abierto. Licencia MIT.

## Para más información

Introducción:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Plantillas:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

En profundidad:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - lección mensual gratuita de arquitectura de software

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Herramientas:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Orientación específica de empresas:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Ejemplos:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Vídeos:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Pódcast:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Libros:

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

Véase también:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Un formato YAML/JSON neutral respecto a proveedores y legible por máquinas para representar decisiones con razonamiento explícito, supuestos, estado cognitivo y compromisos. Complementa los ADR añadiendo razonamiento estructurado y validable a la documentación de decisiones.
