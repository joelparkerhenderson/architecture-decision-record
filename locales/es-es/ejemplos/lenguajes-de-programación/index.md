# Lenguajes de programación

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

Necesitamos elegir lenguajes de programación para nuestro software. Tenemos dos necesidades principales: un lenguaje de programación de front end adecuado para aplicaciones web y un lenguaje de programación de back end adecuado para aplicaciones de servidor.


### Decisión

Elegimos TypeScript para el front end.

Elegimos Rust para el back end.


### Estado

Decidido. Estamos abiertos a nuevas alternativas a medida que surjan.


## Detalles


### Supuestos

Las aplicaciones de front end son típicas:

  * Usuarios e interacciones típicos

  * Navegadores y sistemas típicos

  * Desarrollos y despliegues típicos

Es probable que las aplicaciones de front end evolucionen con rapidez:

  * Queremos asegurar desarrollos, despliegues, iteraciones, etc., rápidos y sencillos.

  * Valoramos la demostrabilidad, como la seguridad de tipos, y estamos dispuestos a trabajar un poco más para lograrla.

  * No necesitamos compatibilidad con sistemas heredados.

Las aplicaciones de back end exigen más de lo típico:

  * Objetivos de calidad superiores a los típicos, especialmente en demostrabilidad, fiabilidad, seguridad, etc.

  * Objetivos de casi tiempo real superiores a los típicos, es decir, no queremos pausas por la recolección de basura de la máquina virtual.

  * Objetivos de programación funcional superiores a los típicos, especialmente para la paralelización, el procesamiento multinúcleo y la seguridad de memoria.

Aceptamos velocidades de compilación más bajas a favor de la seguridad en tiempo de compilación y de la velocidad en tiempo de ejecución.


### Restricciones

Tenemos una fuerte restricción respecto de los lenguajes que pueden usarse con los servicios de funciones de los principales proveedores de nube, como Amazon Lambda.


### Posiciones

Consideramos estos lenguajes:

  * C

  * C++

  * Clojure
  
  * Elixir
  
  * Erlang
  
  * Elm
  
  * Flow
  
  * Go
  
  * Haskell
  
  * Java
  
  * JavaScript
  
  * Kotlin
  
  * Python
  
  * Ruby
  
  * Rust
  
  * TypeScript



### Argumento

Resumen por lenguaje:

  * C: rechazado por su baja seguridad; Rust puede hacer casi todo mejor.

  * C++: rechazado porque es un desastre; Rust puede hacer casi todo mejor.

  * Clojure: excelente modelado; la mejor aproximación a Lisp; gran entorno de ejecución en la JVM.
  
  * Elixir: excelente entorno de ejecución, incluidas la facilidad de despliegue y la concurrencia; excelente experiencia de desarrollo; ecosistema relativamente pequeño.

  * Erlang: excelente entorno de ejecución, incluidas la facilidad de despliegue y la concurrencia; experiencia de desarrollo difícil; ecosistema relativamente pequeño.

  * Elm: parece muy prometedor; IBM está publicando importantes casos de estudio con buenos resultados; ecosistema más pequeño.

  * Flow: mejora interesante sobre JavaScript; sin embargo, los desarrolladores se están alejando de él.

  * Go: excelente experiencia de desarrollo; excelente concurrencia; pero con un historial de malas decisiones que lisian el lenguaje.

  * Haskell: el mejor lenguaje funcional; comunidad de desarrolladores más pequeña; no ha logrado suficientes éxitos publicados en producción.

  * Java: excelente entorno de ejecución; excelente ecosistema; experiencia de desarrollo mediocre.

  * JavaScript: el lenguaje más popular de la historia; el ecosistema más extendido.

  * Kotlin: corrige gran parte de Java; excelente respaldo de JetBrains; buenos casos publicados de migración de Java a Kotlin.
  
  * Python: el lenguaje más popular para la administración de sistemas; gran herramienta de analítica; buenos frameworks web; pero abandonado por Google en favor de Go.

  * Ruby: la mejor experiencia de desarrollo de la historia; los mejores frameworks web; la comunidad más agradable; pero muy lento; algo difícil de empaquetar.

  * Rust: el mejor lenguaje nuevo; énfasis en cero abstracción; énfasis en la concurrencia; sin embargo, ecosistema relativamente pequeño; y tiene límites deliberados en algunos tipos de aceleraciones del compilador, p. ej., el acceso directo a la memoria debe ser explícitamente inseguro (unsafe).

  * TypeScript: añade tipos a JavaScript; gran transpilador; creciente énfasis de los desarrolladores en migrar de JavaScript a TypeScript; sólido respaldo de Microsoft.

Decidimos que las máquinas virtuales tienen un conjunto de contrapartidas que no necesitamos ahora, como una complejidad adicional que ofrece capacidades de tiempo de ejecución.

Creemos que nuestra decisión central está impulsada por dos preocupaciones transversales:

  * Para obtener la máxima velocidad de ejecución y el acceso más estrecho al sistema, elegiríamos JavaScript y C.

  * Para obtener una velocidad de ejecución cercana a la máxima y un acceso al sistema cercano al más estrecho, elegimos TypeScript y Rust.

Las menciones de honor van para los lenguajes de máquina virtual y los frameworks web que elegiríamos si quisiéramos un lenguaje de máquina virtual:

  * Clojure y Luminus

  * Java y Spring

  * Elixir y Phoenix


### Implicaciones

Los desarrolladores de front end tendrán que aprender TypeScript. Probablemente sea una curva de aprendizaje fácil si la experiencia principal del desarrollador es el uso de JavaScript.

Los desarrolladores de back end tendrán que aprender Rust. Probablemente sea una curva de aprendizaje moderada si la experiencia principal del desarrollador es el uso de C/C++, y una curva de aprendizaje difícil si su experiencia principal es el uso de Java, Python, Ruby o lenguajes similares con gestión automática de memoria. 

TypeScript y Rust son ambos relativamente nuevos. Esto significa que muchas herramientas aún no tienen documentación para estos lenguajes. Por ejemplo, la canalización de devops tendrá que configurarse para estos lenguajes, y hasta ahora ninguna de las herramientas de devops que estamos evaluando tiene ejemplos predeterminados para ellos.

Los tiempos de compilación de TypeScript y Rust son bastante lentos. Parte de esto puede deberse a la novedad de los lenguajes. Quizá queramos ver cómo mitigar los tiempos de compilación lentos, por ejemplo mediante compilación bajo demanda, compilación concurrente, etc.

La compatibilidad de los IDE con estos lenguajes aún no es omnipresente ni de primera clase. Por ejemplo, JetBrains vende el IDE PyCharm con compatibilidad de primera clase para Python, pero no vende un IDE con compatibilidad de primera clase para Rust; en su lugar, JetBrains puede usar un complemento de Rust que ofrece quizá el 80 % de la compatibilidad con el lenguaje Rust frente a la compatibilidad con el lenguaje Python.


## Relacionado


### Decisiones relacionadas

Tenderemos hacia elecciones de ecosistema que se alineen con estos lenguajes.

Por ejemplo, queremos elegir un IDE que tenga buenas capacidades para estos lenguajes.

Por ejemplo, para nuestro framework web de front end, es más probable que nos decidamos por un framework que tienda hacia TypeScript (p. ej., Vue) que por un framework que tienda hacia JavaScript simple (p. ej., React).


### Requisitos relacionados

Toda nuestra cadena de herramientas debe ser compatible con estos lenguajes.


### Artefactos relacionados

Esperamos poder exportar algunos secretos a variables de entorno.


### Principios relacionados

Mida dos veces, construya una. Priorizamos cierta seguridad sobre cierta velocidad.

El tiempo de ejecución es más valioso que el tiempo de compilación. Priorizamos el uso por parte de los clientes sobre el uso por parte de los desarrolladores.


## Notas

Cualquier nota aquí.
