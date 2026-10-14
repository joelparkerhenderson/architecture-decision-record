# Configuración con variables de entorno

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

Queremos que nuestras aplicaciones sean configurables más allá de los artefactos, binarios y código fuente, de modo que una misma compilación pueda comportarse de manera distinta según su entorno de despliegue.

  * Para lograrlo, queremos usar la configuración con variables de entorno.

  * Queremos gestionar la configuración mediante archivos que podamos poner bajo control de versiones.

  * Queremos ofrecer cierta ergonomía en la experiencia del desarrollador, como saber qué se puede configurar y cuáles son los valores predeterminados pertinentes.


### Decisión

Se decidió por archivos .env con su archivo de valores predeterminados y su archivo de esquema.


### Estado

Decidido. Abiertos a considerar nuevas capacidades a medida que vayan surgiendo.


## Detalles


### Supuestos

Preferimos separar el código de la aplicación y el código del entorno. Suponemos que la aplicación debe funcionar de manera distinta en entornos distintos, como un entorno de desarrollo, un entorno de pruebas, un entorno de demostración, un entorno de producción, etc.

Preferimos la práctica del sector de la «aplicación de 12 factores» (12 factor app) y, más aún, la práctica relacionada de la «aplicación de 15 factores» (15 factor app).

Muchos de nuestros proyectos anteriores han usado la convención de un archivo `.env` o un directorio `.env` similar. Es una práctica habitual mantenerlos fuera del control de versiones y, en su lugar, usar otra forma de desplegarlos, versionarlos y gestionarlos.


### Restricciones

Queremos mantener los secretos fuera de nuestro sistema de control de versiones (VCS) de gestión del código fuente (SCM).

Queremos buscar la compatibilidad con los frameworks y bibliotecas de software populares. Por ejemplo, Node tiene un módulo «dotenv» para leer la configuración con variables de entorno.


### Posiciones

Consideramos algunos enfoques:

  * Almacenar la configuración en la aplicación, por ejemplo en un archivo `config.js`.

  * Almacenar la configuración en el entorno, por ejemplo en un archivo `.env`.

  * Obtener la configuración desde una ubicación conocida, como un servidor de licencias.


### Argumento

Seleccionamos el enfoque de un archivo .env porque:

  * Es popular, también entre los expertos.

  * Sigue el patrón de los archivos `.env`, que nuestros equipos han usado con éxito muchas veces en muchos proyectos.

  * Es simple. En particular, por ahora aceptamos las importantes contrapartidas que vemos, como la falta de capacidades de auditoría en comparación con un enfoque de servidor de licencias.


### Implicaciones

Necesitamos encontrar una forma de separar la configuración con variables de entorno que es pública de cualquier gestión de secretos.


## Relacionado


### Decisiones relacionadas

Esperamos que todas nuestras aplicaciones usen este enfoque.

Planificaremos actualizar las aplicaciones que usen un enfoque menos capaz, como el código fijo en un binario o en el código fuente.

Mantendremos tal cual las aplicaciones que usen un enfoque más capaz, como un servidor de licencias.


### Requisitos relacionados

Añadiremos capacidades de devops para los archivos, incluidos hooks, pruebas e integración continua.

Necesitamos capacitar a todos los compañeros desarrolladores sobre esta decisión.



### Artefactos relacionados

Cada área donde desplegamos necesitará su propio archivo .env y archivos relacionados.


### Principios relacionados

Fácilmente reversible.


## Notas


Archivo de ejemplo `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Archivo de ejemplo `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Archivo de ejemplo `.env.schema` solo con las claves:

```env
NAME
EMAIL
```
