# Microsoft Azure DevOps

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
  * [Microsoft Devops CI: una aventura insatisfactoria](#microsoft-devops-ci-una-aventura-insatisfactoria)
  * [Aspectos destacados de la discusión en Hacker News](#aspectos-destacados-de-la-discusión-en-hacker-news)
  * [MVP de desarrollo para Windows](#mvp-de-desarrollo-para-windows)
  * [Resumen de Edward Thomson (PM de Azure)](#resumen-de-edward-thomson-pm-de-azure)


## Resumen


### Asunto

Queremos usar devops para compilar, integrar, desplegar y alojar nuestros proyectos. Estamos considerando Microsoft Azure DevOps.

  * Queremos que la experiencia del desarrollador sea rápida y fiable, tanto en la configuración inicial de devops, p. ej., la configuración, como en el uso continuo, p. ej., tiempos de compilación rápidos.
  
  * Queremos considerar usar Microsoft Azure en su conjunto, para alojar las aplicaciones del proyecto, las bases de datos, etc.


### Decisión

Decidido en contra de Microsoft Azure DevOps.


### Estado

Decidido. Abiertos a revisarlo si y cuando llegue nueva información significativa.


## Detalles


### Supuestos

Todos los supuestos habituales de devops, como los del libro Accelerate.

  * Las compilaciones rápidas son una gran ayuda. Aceleran los ciclos de retroalimentación.

  * Podemos sustituir o incorporar piezas de otros proveedores, es decir, podemos querer traer nuestros servidores de compilación de mayor velocidad, o usar el sistema de control de versiones que elijamos, o coordinarnos con un servidor de integración continua alojado por nosotros.
  
  * La usabilidad optimizada es una gran ayuda, para la experiencia del desarrollador y, a su vez, para áreas sutiles como la coherencia, la claridad, la seguridad y la facilidad de la curva de aprendizaje.

  * Cuando algo esté roto o sea problemático, queremos una forma eficaz de informar del problema. Esto es especialmente importante para cualquier problema relacionado con la seguridad.


### Restricciones

Ninguna conocida. Azure tiene un compromiso publicado de llevarse bien con herramientas externas.


### Posiciones

Consideramos usar Microsoft Azure Devops frente a AWS, que es el proveedor actual.

Experimentamos con Azure DevOps, Azure Pipelines, Azure Repo y la puesta en marcha en Azure de un servidor nuevo mediante Terraform.

Experimentamos con obtener soporte de representantes de Microsoft.

Reunimos información de colegas en blogs y en Hacker News.


### Argumento

Azure DevOps anuncia un excelente conjunto de ofertas, pero no cumplen lo prometido, no funcionan bien juntas y el soporte es deficiente.

Nuestra experiencia de primera mano:

  * La configuración de Azure es un lío de interfaces de usuario, algunas de las cuales se solapan con las cuentas de Microsoft y otras no. P. ej., hay un inicio de sesión de Azure, un inicio de sesión de Microsoft.com, un inicio de sesión de Live.com, etc., y todos están en juego a la vez.

  * Encontramos un problema de seguridad menor durante la configuración y no hallamos solución. Probamos muchas maneras de informar de ello, a muchos representantes de Microsoft, sin éxito. Lo informamos con éxito al equipo de seguridad de Microsoft, que respondió con won't fix (no se corregirá).

  * La documentación suele estar equivocada o desactualizada. Al menos parte de esto se debe al deficiente motor de búsqueda de Microsoft, y parte a un SEO mediocre.
  
  * La configuración de Terraform está bien documentada y funciona. Sin embargo, el soporte de Terraform es débil en comparación con AWS porque Microsoft está construyendo relaciones comerciales con proveedores para ofrecer ejemplos de configuración de Terraform encadenados.

Las experiencias de nuestros colegas:

  * Después de hacer nuestra propia evaluación a ciegas, buscamos experiencias de colegas. Lo que encontramos confirmó nuestras experiencias.

  * Los colegas informaron de problemas adicionales con los tiempos de compilación y con traer su propio servidor de compilación. Estos problemas son significativamente más graves que los de la interfaz de usuario, porque hacer compilaciones es el propósito central de una canalización de compilación, y esperamos hacer muchas por día.

  * Encontramos una excelente participación de los compañeros de Azure en las áreas de debate. Un reconocimiento a Microsoft por ello. Nos impresionó especialmente Edward Thomson, PM y programador de Azure, por su participación, su franqueza y sus explicaciones técnicas.


### Implicaciones

Elegir Microsoft Azure DevOps parece que probablemente sea más caro (~3 veces) en tiempo y costo que no elegir Azure.


## Relacionado


### Decisiones relacionadas

Si elegimos Azure DevOps, hay muchas ofertas relacionadas, como Azure Repo, Azure Pipeline, etc. Creemos que, si elegimos Azure Devops, esto puede facilitar el uso de más capacidades de Azure, o puede dificultar el uso de las capacidades de otros proveedores.

Creemos que Microsoft está dando grandes pasos en la experiencia del desarrollador, y vemos que Microsoft realiza grandes adquisiciones de herramientas para desarrolladores (p. ej., GitHub) y de dependencias (p. ej., Citus).

Si elegimos Azure DevOps, podríamos querer hacer hincapié en elegir las ofertas procedentes de adquisiciones de Microsoft, y también podríamos querer abordar esas ofertas adquiridas con más cuidado y evaluación por el posible rechazo de tejido, p. ej., el riesgo de rotación de personal.


### Requisitos relacionados

Queremos que los tiempos de compilación sean muy rápidos. Aceptamos pagar una prima alta por esto. Esto se debe a que queremos iterar muy rápido.

Queremos que la fiabilidad sea muy alta. Aceptamos pagar una prima alta por esto. Esto se debe a que estamos probando casos de uso de alto valor, incluidas transacciones financieras, transacciones confidenciales, etc.

Nuestros 4 principales KPI de devops incluyen el tiempo medio de recuperación, que exige compilaciones rápidas y alta fiabilidad.


### Artefactos relacionados

Queremos que el sistema de compilación produzca artefactos adecuados para usarse en otros sistemas, como Artifactory.


### Principios relacionados

Fácilmente reversible. Podemos evaluar Azure DevOps en paralelo con AWS, el proveedor actual.


## Notas


### Microsoft Devops CI: una aventura insatisfactoria

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Publicación de blog.

«Como desarrollador de software, sé de primera mano lo difícil que es construir productos de calidad con rapidez y a bajo costo. Es un arte que a veces logramos, y otras veces degenera en algo parecido al sitio web gubernamental de atención médica de la era Obama. Nuestro nivel de control sobre el producto resultante varía, y la culpa del fracaso recae a menudo en las personas equivocadas de la jerarquía de toma de decisiones. Azure DevOps de Microsoft (antes conocido como Visual Studio Team Services), a pesar de sus claras buenas intenciones, es una tormenta perfecta de malas decisiones y mala ejecución».


### Aspectos destacados de la discusión en Hacker News

https://news.ycombinator.com/item?id=18983586

«Usamos Azure DevOps de forma intensiva en mi trabajo y, después de haber usado GitHub, Gitlab, soluciones autoalojadas, Jenkins, TeamCity... Azure DevOps queda en último lugar».

«La interfaz de usuario es terriblemente torpe en todas partes. Lo peor para mí son las solicitudes de incorporación de cambios (pull requests). Es increíblemente difícil trabajar con otras personas en una pull request. Ni siquiera puedo señalar un problema "concreto": para nosotros está roto en todas partes».

«Azure Devops es algo que quiero amar. La interfaz de usuario cambia constantemente, pero no arregla los errores de fondo que llevan ahí muchísimo tiempo».

«Las herramientas no están bien integradas, la interfaz de usuario es realmente lenta, no hay una vista de panel de las pull requests activas, compilaciones, versiones, etc., de mis repositorios favoritos. Los tiempos de compilación y despliegue son increíblemente lentos».

«También intentamos usar Azure Boards (elementos de trabajo, tableros, backlogs, etc.). Uf. Es un completo lío de interfaz de usuario de ideas inconexas. En lugar de implementar bien una sola cosa, implementaron dos docenas de cosas pésimamente».


### MVP de desarrollo para Windows

Soy MVP de desarrollo para Windows. Siento que debo asumir parte de la responsabilidad por no haber sido más enfático sobre estos problemas. Pero debo decir que me decepciona oír que les «sorprenden» los problemas de experiencia de usuario. Les he dicho a los suyos que la experiencia de usuario es espantosa (p. ej., desde antes del lanzamiento) y siempre escuchaba como respuesta «lo sabemos, lo estamos arreglando». Empezaré a formalizar los comentarios y a hacerlos llegar por los canales, estén atentos. También soy de la zona (Bellevue) y me encantaría ir y probar a canalizar nuestra aplicación .net/wpf/uwp de código abierto relativamente sencilla. Sospecho que nos abrirá los ojos a ambos.

Algunos ejemplos:

* No se puede crear una canalización con un repositorio git que contenga submódulos

* Me resultó imposible editar el PATH para algunas herramientas personalizadas

* La experiencia de New Pipeline no tiene mucho sentido: los usuarios nuevos que hacen clic por ahí terminarán en la documentación equivocada.


### Resumen de Edward Thomson (PM de Azure)

Escribí el código que fusiona sus pull requests. Program Manager en Microsoft para Azure DevOps; antes ingeniero de software en herramientas de control de versiones en GitHub, Microsoft y SourceGear.

https://www.edwardthomson.com/

Comantenedor de libgit2. https://libgit2.github.io

Copresentador de All Things Git, el pódcast sobre Git. https://www.allthingsgit.com/

Curador de Developer Tools Weekly, un boletín sobre herramientas de desarrollo. https://developertoolsweekly.com/
