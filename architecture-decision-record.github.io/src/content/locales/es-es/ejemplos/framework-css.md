# Registro de decisión de arquitectura: framework CSS

Contenido:

- [Resumen](#resumen)
  - [Asunto](#asunto)
  - [Decisión](#decisión)
  - [Estado](#estado)
- [Detalles](#detalles)
  - [Supuestos](#supuestos)
  - [Restricciones](#restricciones)
  - [Posiciones](#posiciones)
  - [Argumento](#argumento)
  - [Implicaciones](#implicaciones)
- [Relacionado](#relacionado)
  - [Decisiones relacionadas](#decisiones-relacionadas)
  - [Requisitos relacionados](#requisitos-relacionados)
  - [Artefactos relacionados](#artefactos-relacionados)
  - [Principios relacionados](#principios-relacionados)
- [Notas](#notas)


## Resumen


### Asunto

Queremos usar un framework CSS para crear nuestras aplicaciones web:

  * Queremos que la experiencia de usuario sea rápida y fiable, en todos los navegadores y tamaños de pantalla populares.

  * Queremos iterar rápidamente en el diseño, la maquetación, la UI/UX, etc.

  * Queremos aplicaciones adaptables (responsive), especialmente para pantallas más pequeñas, como las de los dispositivos móviles, pantallas más grandes, como las panorámicas 4K, y pantallas dinámicas, como las pantallas giratorias.  


### Decisión

Se decidió por Bulma.


### Estado

Se decidió por Bulma. Abiertos a nuevas opciones de framework CSS a medida que vayan apareciendo.


## Detalles


### Supuestos

Queremos crear aplicaciones web modernas, rápidas, fiables, adaptables, etc.

Las aplicaciones web modernas típicas están reduciendo o eliminando el uso de jQuery por varias razones: 

  * El JavaScript moderno va incorporando poco a poco muchas capacidades que jQuery ha proporcionado, por lo que jQuery es menos necesario, y existen módulos mejores, más rápidos y más pequeños que ofrecen implementaciones específicas

  * El enfoque general de jQuery es manipular directamente el DOM, lo cual es un antipatrón para los frameworks modernos de JavaScript (p. ej., React, Vue, Svelte)

  * jQuery interfiere consigo mismo si se carga dos veces, etc.


### Restricciones

Si elegimos un framework CSS que usa jQuery, nos vemos obligados a importar jQuery. Por ejemplo, Semantic UI usa jQuery y Tachyons no.

Si elegimos un framework CSS mínimo, renunciamos a componentes del framework que podríamos querer ahora o pronto. Por ejemplo, Semantic UI ofrece un carrusel de imágenes y Tachyons no.


### Posiciones

Consideramos no usar ningún framework. Esto todavía parece viable, sobre todo porque CSS grid ofrece gran parte de lo que necesita nuestro proyecto.

Consideramos muchos frameworks CSS mediante una rápida clasificación de una lista corta: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons, etc. Nuestras dos selecciones para una revisión más profunda son Semantic UI (porque tiene el enfoque más semántico) y Bulma (porque tiene el enfoque más ligero que proporciona los componentes que queremos ahora).

Consideramos Semantic UI. Ofrece muchos componentes, incluidos algunos que queremos para nuestro proyecto: pestañas, cuadrículas, botones, etc. Hicimos un piloto con Semantic UI de dos maneras: usando archivos CDN típicos y usando repositorios NPM. Tuvimos éxito con Semantic UI en una página HTML estática, pero no lo logramos dentro de nuestro plazo para construir una SPA de JavaScript (principalmente por problemas de carga de jQuery). Descubrimos que otros programadores han estado pidiendo a los desarrolladores de Semantic UI que creen una versión sin jQuery, por las mismas razones que nosotros. Otros programadores llevan muchos años solicitando una versión sin jQuery, pero los desarrolladores han dicho que no y han afirmado que cualquier versión sin jQuery sería demasiado difícil de escribir, p. ej., ~«el proyecto Semantic UI tiene más de 22.000 puntos de contacto que usan jQuery».

Ejemplo con Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Consideramos Bulma. Bulma tiene muchas capacidades similares a las de Semantic UI, aunque no tantos componentes sofisticados. Bulma está construido con técnicas modernas, como no usar jQuery. Bulma tiene algunos componentes de terceros, algunos de los cuales podríamos querer usar.


Ejemplo con Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argumento

Como se indicó arriba.

En concreto, Semantic UI parece tener una señal de precaución tanto en términos de tecnología (es decir, tantos puntos de contacto con jQuery) como en términos de liderazgo (es decir, una versión sin jQuery fue un no rotundo, en lugar de intentar una hoja de ruta, una mejora continua o una recaudación de donaciones, etc.).


### Implicaciones

Si encontramos un buen framework CSS sin jQuery, esto es en general útil y positivo.


## Relacionado


### Decisiones relacionadas

El framework CSS que elijamos puede afectar a la capacidad de prueba.


### Requisitos relacionados

Queremos lanzar con rapidez una aplicación puramente moderna. 

No queremos dedicar tiempo a trabajar con frameworks más antiguos (especialmente Semantic UI) que usan dependencias más antiguas (especialmente jQuery).


### Artefactos relacionados

Afecta a todo el HTML típico que usará el CSS.


### Principios relacionados

Fácilmente reversible.

Necesidad de velocidad.


## Notas

Cualquier nota aquí.
