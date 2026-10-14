# Monorepo frente a multirepo

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

Nuestro proyecto implica desarrollar tres grandes categorías de software:

  * Interfaces gráficas de usuario (GUI) de front end
  * Servicios de middleware
  * Servidores de back end

Cuando desarrollamos, nuestro sistema de control de versiones (VCS) de gestión del código fuente (SCM) es git.

Necesitamos elegir cómo usamos git para organizar nuestro código.

La elección de nivel superior es organizar como «monorepo», «polirepo» o «híbrido»:

  * Monorepo significa que ponemos todas las piezas en un único repositorio grande
  * Polirepo significa que ponemos cada pieza en su propio repositorio
  * Híbrido significa alguna combinación de monorepo y polirepo

Para más información, consulte https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Decisión

Monorepo cuando una organización, equipo o proyecto es relativamente pequeño y la iteración rápida tiene mayor prioridad que mantener la estabilidad.

Polirepo cuando una organización, equipo o proyecto es relativamente grande y mantener la estabilidad tiene mayor prioridad que la iteración rápida.


### Estado

Decidido. Abiertos a revisarlo si y cuando haya nuevas herramientas disponibles para gestionar monorepos y/o polirepos.


## Detalles


### Supuestos

Todo el código que desarrollamos es para las ofertas de una sola organización y no para el público en general. Es decir, el corredor-distribuidor (Broker-Dealer) no aspira a contar con nada parecido a desarrolladores voluntarios del público en general.


### Restricciones

Las restricciones están bien documentadas en https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Posiciones

Consideramos monorepos al estilo de Google, Facebook, etc. Creemos que los problemas de escalado de un monorepo están tan lejos en el futuro que, para cuando los necesitemos, podremos aprovechar las mismas prácticas que Google y Facebook.

Consideramos polirepos al estilo de los típicos proyectos de código abierto de Git, como Google Android, Facebook React, etc. Creemos que son la mejor opción para la participación del público en general (p. ej., cualquier persona en el mundo puede trabajar en el código) y para la disponibilidad individual (p. ej., el proyecto se usa por sí solo, sin ninguna otra pieza).


### Argumento

Cuando una organización, equipo o proyecto es relativamente pequeño, elegimos monorepo, porque la iteración rápida tiene una prioridad significativamente mayor que mantener la estabilidad.

Cuando una organización, equipo o proyecto es relativamente grande, elegimos polirepo, porque mantener la estabilidad tiene una prioridad significativamente mayor que la iteración rápida.


### Implicaciones

Si ya existe una canalización de CI+CD, es posible que debamos ajustarla para probar varios proyectos dentro de un mismo repositorio.

El CI+CD podría tardar más en una compilación completa de un monorepo, porque podría compilar todos los proyectos del monorepo.

Si una organización, equipo o proyecto crece, el monorepo tendrá problemas de escalado.

Los problemas de escalado del monorepo pueden hacer cada vez más valioso pasar a un polirepo.

La transición de monorepo a polirepo es una tarea de devops importante, y habrá que planificarla, gestionarla y programarla.


## Relacionado


### Decisiones relacionadas

Crearemos decisiones sobre las herramientas relacionadas para gestionar monorepos (p. ej., Google Bazel) y polirepos (p. ej., Lyft Refactorator).


### Requisitos relacionados

Necesitamos desarrollar la canalización de CI+CD para que funcione bien con git.


### Artefactos relacionados

Esperamos que la organización del repositorio tenga artefactos relacionados para el aprovisionamiento, la gestión de la configuración, las pruebas y áreas de devops similares. 


### Principios relacionados

Fácilmente reversible. Si el monorepo no funciona en la práctica, o la dirección no lo quiere, es sencillo cambiar a polirepo.

Obsesión por el cliente. Valoramos poner el proyecto en manos de los clientes, y creemos que un monorepo puede llevarnos allí más rápido que un polirepo, y ayudarnos también a iterar más rápido.

Pensar en grande. Google y Facebook son defensores muy firmes de los monorepos frente a los polirepos, porque todas las ofertas principales pueden desarrollarse, probarse y desplegarse en conjunto.


## Notas

Añada aquí cualquier nota.
