# Formato de marca de tiempo

Contenido:

* [Resumen](#resumen)
  * [Asunto](#asunto)
  * [Decisión](#decisión)
  * [Estado](#estado)
* [Detalles](#detalles)
  * [Supuestos](#supuestos)
  * [Restricciones](#restricciones)
  * [Posiciones](#posiciones)
  * [Argumento](#argumento)
  * [Implicaciones](#implicaciones)
* [Relacionado](#relacionado)
  * [Decisiones relacionadas](#decisiones-relacionadas)
  * [Requisitos relacionados](#requisitos-relacionados)
  * [Artefactos relacionados](#artefactos-relacionados)
  * [Principios relacionados](#principios-relacionados)
* [Notas](#notas)


## Resumen


### Asunto

Queremos poder registrar cuándo ocurren las cosas mediante marcas de tiempo y mediante un formato de marca de tiempo coherente que funcione bien en todos nuestros sistemas y en los sistemas de terceros.

Interactuamos con sistemas que tienen formatos de marca de tiempo distintos:

* Los mensajes JSON no tienen un formato nativo de marca de tiempo, por lo que debemos elegir cómo convertir una marca de tiempo en una cadena y una cadena en una marca de tiempo, es decir, cómo serializar y deserializar.

* Algunas aplicaciones están configuradas para usar la hora local en lugar de la hora UTC. Esto puede ser conveniente para proyectos que deben ajustarse a la hora local, como los que activan eventos basados en la hora local.

* Algunos sistemas tienen necesidades y capacidades de precisión temporal diferentes, como usar una resolución de segundos, de milisegundos o de nanosegundos. Por ejemplo, el comando `date` del sistema operativo Linux usa por defecto una precisión de segundos, mientras que la bolsa de valores Nasdaq quiere una precisión de nanosegundos por defecto.


### Decisión

Elegimos el formato estándar de marca de tiempo ISO 8601 con precisión de nanosegundos, en concreto «AAAA-MM-DDTHH:MM:SS.NNNNNNNNNZ».

El formato muestra el año, el mes, el día, la hora, el minuto, el segundo, los nanosegundos y la zona horaria Zulu, también conocida como UTC o GMT.


### Estado

Decidido.


## Detalles


### Supuestos

Necesitamos manejar estas cadenas de texto de marca de tiempo, para convertir de marca de tiempo a cadena (es decir, serializar) y de cadena a marca de tiempo (es decir, deserializar).

Queremos un formato que en general sea fácil de usar, fácil de convertir y fácil de leer para una persona.

Queremos compatibilidad con una amplia gama de sistemas externos que no podemos controlar, como sistemas de analítica, sistemas de bases de datos y sistemas financieros.


### Restricciones

Algunos sistemas tienen limitaciones de precisión temporal. Por ejemplo, el comando `date` del sistema operativo macOS puede imprimir la precisión temporal en segundos, pero no en nanosegundos.


### Posiciones

Consideramos una serie de opciones:

* Época Unix (Unix epoch), es decir, un único número incremental.

* Formato de texto escueto «AAAAMMDDTHHMMSSNNNNNNNNN».

* Usar una zona horaria local frente a la zona horaria UTC.


### Argumento

Para el uso típico, valoramos más que sea fácil de leer y escribir por personas que la velocidad o el tamaño en bruto.

Para el uso típico, queremos un formato que funcione bien en los sistemas de máquinas y que también funcione bien de forma manual, como al escribir datos de muestra, leer la salida JSON, buscar con grep en un archivo de registro, etc.

Para el uso atípico, como la computación de alto rendimiento, esperamos que querremos optimizar cualquier formato de texto que elijamos convirtiendo el texto a un formato más rápido, como el tipo de objeto de fecha integrado de un lenguaje de programación. Por lo tanto, el formato de texto no importa mucho para la HPC.


### Implicaciones

Nuestros diversos sistemas de texto y sistemas de tiempo convergerán en este formato.


## Relacionado


### Decisiones relacionadas

Es posible que queramos también una forma rápida y fácil de hacer seguimiento de las diferencias de tiempo, es decir, las duraciones. Con las marcas de tiempo de época Unix esto es sencillo.


### Requisitos relacionados

Es posible que queramos ajustar nuestra decisión, por ejemplo, si tenemos un requisito relacionado con un tipo específico de sello de mensaje de registro, como para Splunk, Sumo, ELK, etc.


### Artefactos relacionados

Formateadores y analizadores sintácticos de lenguajes:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Ejemplos de Rosetta Code:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Ejemplos de SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Principios relacionados

Fácilmente reversible. Podemos cambiar con bastante facilidad a un formato diferente, como la época Unix.

Aplazar la optimización prematura. Para el uso típico no nos importa mucho un puñado de caracteres adicionales, como en un formato que usa guiones y dos puntos.


## Notas

Añada notas aquí.
