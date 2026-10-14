# Registro de decisión de arquitectura: kit de bibliotecas de gráficos para visualización de datos con TypeScript y JSON

<!--

ChatGPT prompt:

Long software architecture decision record 
chart library toolkit for data visualization using TypeScript and JSON

Evaluate Charts: Apache ECharts, Chart.js, ApexCharts, AG Charts, Highcharts, Carbon Charts, Layer Cake, D3.

Primary need: advanced interactive charts, especially for financial data, scientific data, and government data.

High importance: 1. Agile development because this is for a startup. 2. Doughnut Chart, Radar Chart, Clustering Process
Chart, Area Chart with Time Axis, Candlestick Chart, Nightingale Chart, Geo SVG Map. 3. Free open source.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Objetivo principal:**  
Seleccionar un kit de gráficos avanzado para crear visualizaciones interactivas, centrado en datos financieros, datos científicos y datos gubernamentales con TypeScript y JSON. La biblioteca debe ofrecer funciones sólidas y flexibilidad, y ser de código abierto. 

### Contexto y requisitos:

1. **Desarrollo ágil (prioridad alta)**: como startup, son esenciales la iteración rápida, el prototipado y la flexibilidad en el desarrollo. La biblioteca de gráficos debe permitir ciclos de desarrollo rápidos.
   
2. **Tipos de gráficos (prioridad alta)**:
   - **Gráfico de anillos (Doughnut Chart)**
   - **Gráfico de radar (Radar Chart)**
   - **Gráfico de proceso de agrupamiento (Clustering Process Chart)**
   - **Gráfico de áreas con eje temporal (Area Chart with Time Axis)**
   - **Gráfico de velas (Candlestick Chart)**
   - **Gráfico de Nightingale (Nightingale Chart)**
   - **Mapa geográfico SVG (Geo SVG Map)**
   
   Estos tipos de gráficos son especialmente importantes para visualizar conjuntos de datos complejos, como tendencias financieras, métricas científicas e información geográfica.

3. **Gratuito y de código abierto (prioridad alta)**: el kit debe ser de código abierto para evitar costos de licencia, ofrecer transparencia y brindar flexibilidad de personalización.

4. **Criterios de baja importancia**:
   - **Velocidad de ejecución**: aunque el rendimiento es importante, no es una prioridad máxima para esta decisión.
   - **Escalabilidad**: aunque la escalabilidad suele ser importante, la necesidad inmediata es construir un MVP que pueda crecer con el tiempo. Las preocupaciones de escalabilidad pueden atenderse más adelante.
   - **Compatibilidad hacia atrás**: no es una preocupación principal para la construcción inicial, siempre que la biblioteca sea moderna y se mantenga activamente.

### Bibliotecas evaluadas:

1. **Apache ECharts**
2. **Chart.js**
3. **ApexCharts**
4. **AG Charts**
5. **Highcharts**
6. **Carbon Charts**
7. **Layer Cake**
8. **D3.js**

---

### 1. **Apache ECharts**

**Visión general**:  
Apache ECharts es una biblioteca de gráficos potente y flexible para visualizaciones interactivas y personalizables. Admite una gran variedad de gráficos y es especialmente sólida en visualizaciones complejas y dinámicas.

**Puntos fuertes**:
- **Interactividad avanzada**: ECharts destaca por ofrecer gráficos interactivos, con funciones como zoom, desplazamiento y actualizaciones dinámicas de datos.
- **Anillos, radar, velas, mapas geográficos SVG**: ECharts admite muchos de los tipos de gráficos requeridos, incluidos las visualizaciones de anillos, de radar, de velas y de mapas geográficos.
- **Gratuita y de código abierto**: ECharts es una biblioteca de código abierto, lo que se ajusta al carácter atento al presupuesto de una startup y ofrece libertad para modificar el código.
- **Flexibilidad y extensibilidad**: muy personalizable, con amplia compatibilidad con animaciones, visualizaciones personalizadas y técnicas avanzadas de gráficos.
  
**Puntos débiles**:
- **Curva de aprendizaje**: ECharts, aunque potente, puede tener una curva de aprendizaje más pronunciada por su flexibilidad y su extensa API.
- **Complejidad de la documentación**: la documentación es completa, pero puede resultar abrumadora para los desarrolladores que apenas empiezan a usarla.

**Veredicto**:  
ECharts es muy adecuada para el proyecto por su compatibilidad con gráficos interactivos, incluidos todos los tipos requeridos, como gráficos de velas, gráficos de radar y mapas geográficos. Su naturaleza de código abierto se alinea con la necesidad del proyecto de flexibilidad y rentabilidad.

---

### 2. **Chart.js**

**Visión general**:  
Chart.js es una biblioteca de gráficos simple y fácil de usar para construir tipos de gráficos comunes. Es conocida por su simplicidad y su facilidad de integración.

**Puntos fuertes**:
- **Facilidad de uso**: Chart.js es muy sencilla de configurar y usar, con una curva de aprendizaje mínima.
- **Código abierto**: Chart.js es gratuita y de código abierto, lo que es fundamental para reducir costos.
- **Tipos de gráficos comunes**: admite gráficos básicos como los de anillos, de áreas, de radar y de líneas, que cubren la mayoría de las necesidades principales.

**Puntos débiles**:
- **Gráficos avanzados limitados**: Chart.js no admite de forma nativa tipos de gráficos complejos como los gráficos de velas, los mapas geográficos SVG o los gráficos de proceso de agrupamiento. Aunque estas funciones pueden añadirse mediante complementos o personalización, no es tan directo como con otras bibliotecas.
- **Interactividad**: aunque Chart.js admite una interactividad básica (p. ej., información sobre herramientas y efectos al pasar el cursor), no ofrece funciones tan avanzadas como ECharts o D3.js.

**Veredicto**:  
Chart.js es excelente para proyectos simples y rápidos, pero su falta de compatibilidad con tipos de gráficos complejos la hace inadecuada para una aplicación con gran carga de datos y con necesidades avanzadas como gráficos de velas y mapas geográficos. Es una buena opción para el prototipado, pero para los tipos de gráficos requeridos se recomiendan herramientas más avanzadas.

---

### 3. **ApexCharts**

**Visión general**:  
ApexCharts es una biblioteca de gráficos moderna que ofrece una variedad de tipos de gráficos y se centra en visualizaciones interactivas con una API fácil de usar.

**Puntos fuertes**:
- **Funciones interactivas**: ApexCharts ofrece gráficos interactivos con información sobre herramientas, zoom, desplazamiento y actualizaciones.
- **Compatibilidad con gráficos financieros y científicos**: admite una amplia variedad de tipos de gráficos, incluidos los gráficos de velas, de radar y de áreas.
- **Facilidad de uso**: tiene una API directa y es sencilla de integrar en un proyecto.
- **Gratuita y de código abierto**: ApexCharts ofrece una versión gratuita de código abierto adecuada para muchos casos de uso.
  
**Puntos débiles**:
- **Personalización compleja**: aunque ofrece muchas funciones, las opciones de personalización no son tan flexibles como las de ECharts o D3.js para necesidades de gráficos muy complejas o personalizadas.
- **Mapas geográficos**: ApexCharts no admite de forma nativa mapas geográficos ni gráficos de proceso de agrupamiento, que son necesarios para este proyecto.

**Veredicto**:  
ApexCharts es un contendiente fuerte por su facilidad de uso y su interactividad, pero se queda corta en ciertos tipos de gráficos avanzados, en particular la necesidad de mapas geográficos y gráficos de agrupamiento. Es una buena opción para gráficos más simples, pero carece de algunas funciones requeridas.

---

### 4. **AG Charts**

**Visión general**:  
AG Charts es una biblioteca de gráficos de nivel comercial diseñada para el rendimiento y la precisión. Es muy adecuada para crear paneles financieros, científicos y empresariales.

**Puntos fuertes**:
- **Tipos de gráficos avanzados**: AG Charts admite muchos tipos de gráficos avanzados, incluidos gráficos de velas, de áreas, de radar y más. También ofrece una integración profunda con otros productos de AG-Grid.
- **Alto rendimiento**: ofrece un excelente rendimiento, en especial al trabajar con conjuntos de datos grandes.
- **Interactividad**: AG Charts admite diversas funciones interactivas como zoom, información sobre herramientas y actualizaciones dinámicas.

**Puntos débiles**:
- **No es totalmente gratuita**: aunque AG Charts ofrece una versión gratuita, la versión con todas las funciones es de pago, lo que podría ser un obstáculo para las startups que buscan minimizar los costos.
- **Complejidad**: aunque la biblioteca es rica en funciones, puede ser excesiva para proyectos más simples y puede requerir más configuración que otras opciones.

**Veredicto**:  
AG Charts es potente y rica en funciones, pero puede que no sea la mejor opción por su naturaleza comercial y su estructura de costos. Su idoneidad depende de si el presupuesto puede asumir versiones de pago o si se prefieren alternativas de código abierto.

---

### 5. **Highcharts**

**Visión general**:  
Highcharts es una popular biblioteca de gráficos conocida por su amplia gama de tipos de gráficos y sus potentes opciones de personalización.

**Puntos fuertes**:
- **Tipos de gráficos completos**: Highcharts admite una amplia variedad de gráficos, incluidos los de velas, de radar, de áreas y los mapas geográficos.
- **Interactiva y dinámica**: Highcharts ofrece ricas funciones interactivas, como el desglose (drill-down), el zoom y el desplazamiento.
- **Facilidad de uso**: tiene una API fácil de usar y buena documentación, lo que facilita comenzar.

**Puntos débiles**:
- **Licencia comercial**: aunque Highcharts ofrece una versión gratuita para uso no comercial, la licencia comercial es cara, lo que podría ser un inconveniente importante para las startups.
- **Curva de aprendizaje**: aunque no tan pronunciada como la de ECharts, la curva de aprendizaje de Highcharts puede seguir siendo difícil para los principiantes.

**Veredicto**:  
Highcharts es una biblioteca rica en funciones, pero su licencia comercial la hace menos adecuada para proyectos de código abierto y sensibles a los costos. Sus completas opciones de gráficos son un punto a favor, pero el tema de la licencia limita su atractivo para este caso de uso.

---

### 6. **Carbon Charts**

**Visión general**:  
Carbon Charts es una biblioteca de gráficos desarrollada por IBM, diseñada para crear gráficos visualmente atractivos y muy personalizables.

**Puntos fuertes**:
- **Personalizabilidad**: Carbon Charts permite una amplia personalización del aspecto y el comportamiento de los gráficos.
- **Código abierto**: es gratuita y de código abierto, lo que se alinea con el requisito del proyecto de soluciones económicas.
- **Compatibilidad con gráficos comunes**: admite tipos de gráficos comunes como los de anillos, de radar y de áreas, aunque no admite tipos más avanzados como los mapas geográficos o los gráficos de velas.

**Puntos débiles**:
- **Tipos de gráficos avanzados limitados**: no admite mapas geográficos, gráficos de proceso de agrupamiento ni gráficos de velas, que son esenciales para el proyecto.
- **Ecosistema más pequeño**: Carbon Charts tiene una comunidad y un ecosistema más pequeños en comparación con bibliotecas de gráficos más grandes como ECharts o Highcharts.

**Veredicto**:  
Carbon Charts es de código abierto y personalizable, pero carece de compatibilidad con los tipos de gráficos más complejos que necesita este proyecto. Es más adecuada para necesidades de gráficos más simples.

---

### 7. **Layer Cake**

**Visión general**:  
Layer Cake es una biblioteca de visualización de datos diseñada para crear visualizaciones flexibles y en capas.

**Puntos fuertes**:
- **Capas personalizables**: ofrece potentes opciones de capas para visualizaciones complejas.
- **Código abierto**: es gratuita y de código abierto, lo que la convierte en una opción viable para proyectos atentos al presupuesto.

**Puntos débiles**:
- **Documentación limitada**: Layer Cake carece de documentación extensa y de apoyo de la comunidad, lo que hace más difícil trabajar con ella en comparación con bibliotecas más consolidadas.
- **No está pensada para gráficos**: Layer Cake es más adecuada para visualizaciones que no son gráficos, por lo que sus opciones de gráficos listas para usar son limitadas.

**Veredicto**:  
Aunque es interesante para visualizaciones únicas, Layer Cake no es ideal para requisitos de gráficos tradicionales como los gráficos de velas o los gráficos de radar. Es más adecuada para visualizaciones personalizadas fuera del alcance de los gráficos estándar.

---

### 8. **D3.js**

**Visión general**:  
D3.js es una potente biblioteca de JavaScript para crear visualizaciones basadas en datos mediante HTML, SVG y CSS.

**Puntos fuertes**:
- **Flexibilidad inigualable**: D3.js permite crear prácticamente cualquier tipo de visualización personalizada, lo que la hace muy potente para gráficos avanzados e interactivos.
- **Funciones extensas**: admite todos los tipos de gráficos requeridos, incluidos mapas geográficos, gráficos de agrupamiento y más.
- **Personalizable**: el nivel de personalización de D3.js no tiene parangón, y permite a los desarrolladores construir visualizaciones muy a medida.

**Puntos débiles**:
- **Curva de aprendizaje pronunciada**: D3.js tiene una curva de aprendizaje pronunciada y es más compleja de integrar que otras bibliotecas.
- **Consume mucho tiempo**: construir gráficos en D3.js puede llevar mucho tiempo, sobre todo para gráficos comunes como los de velas o los de anillos.

**Veredicto**:  
D3.js es increíblemente potente para gráficos avanzados y personalizados, pero es excesiva para muchos casos de uso típicos por su curva de aprendizaje pronunciada y su tiempo de desarrollo. Es lo mejor para situaciones en las que las demás bibliotecas de gráficos no ofrecen el nivel de personalización requerido.

---

### Conclusión

Tras evaluar las bibliotecas según las necesidades del proyecto, **Apache ECharts** destaca como la mejor opción. Admite toda la gama de gráficos requeridos, incluidos mapas geográficos, gráficos de velas y gráficos de agrupamiento. Es de código abierto, rica en funciones y muy interactiva, lo que se alinea perfectamente con los objetivos del proyecto. Aunque **D3.js** ofrece la mayor flexibilidad, su complejidad y la inversión de tiempo la hacen menos ideal para una startup que busca iterar con rapidez. **ApexCharts** y **Chart.js** son buenas alternativas para proyectos más simples, pero carecen de compatibilidad con tipos de gráficos avanzados.
