## Registro de decisión de arquitectura: framework de automatización de navegador para pruebas E2E (Playwright frente a Selenium)

### 1. **Contexto**

Estamos en el proceso de seleccionar un framework de automatización de navegador para nuestra canalización de pruebas de extremo a extremo (E2E). Este framework será parte integral de nuestros procesos de CI/CD, y ejecutará pruebas que simulan interacciones reales de usuarios en nuestra plataforma. En concreto, las pruebas cubrirán escenarios como el registro e inicio de sesión de usuarios, la carga de archivos, las interacciones con paneles y la descarga de informes.

Como **startup**, nuestro enfoque es el **desarrollo ágil**, con la necesidad de iterar y evolucionar con rapidez. Nuestro equipo trabaja sobre todo con **TypeScript** y **Python**, y es esencial poder escribir pruebas en estos lenguajes. Además, la plataforma contiene **gráficos interactivos y paneles**, por lo que es fundamental que la herramienta de automatización sea compatible con interfaces ricas y dinámicas.

Los dos contendientes para esta tarea son **Playwright** y **Selenium**, cada uno con sus puntos fuertes y sus contrapartidas. Necesitamos evaluar estos frameworks según las funciones y los requisitos que se describen a continuación.

### 2. **Opciones consideradas**

- **Playwright** (de Microsoft)
- **Selenium** (del Proyecto Selenium)

### 3. **Factores de la decisión**

Los factores que influyen en nuestra decisión son los siguientes:

1. **Desarrollo ágil**: la herramienta elegida debe permitir ciclos de desarrollo rápidos y flexibles.
2. **Compatibilidad con lenguajes**: nuestro equipo necesita compatibilidad con **TypeScript** y **Python**.
3. **Pruebas de interfaz de usuario interactiva**: es esencial la capacidad de probar de manera fiable gráficos interactivos, paneles y elementos dinámicos.
4. **Velocidad de ejecución**: aunque no es una preocupación principal, el rendimiento en las canalizaciones de CI/CD es una consideración.
5. **Escalabilidad**: no planeamos una escala masiva en el futuro inmediato, pero queremos asegurarnos de que la solución pueda manejar el crecimiento futuro.
6. **Compatibilidad hacia atrás**: los sistemas heredados y la compatibilidad con navegadores antiguos no son críticos para nuestro proyecto en este momento.
7. **Pruebas en móviles**: aunque no es un foco inmediato, el framework debería poder probar funciones adaptables a móviles o ser extensible para tales casos de uso.
8. **Pruebas con varios monitores**: la compatibilidad con configuraciones de varios monitores es un requisito secundario, especialmente si algún día escalamos a probar flujos de trabajo de usuario más complejos.
9. **Pruebas de carga de archivos**: el framework debe manejar la carga de archivos de manera eficiente, un requisito central de nuestras necesidades de pruebas.

### 4. **Criterios de evaluación**

- **Facilidad de uso**: ¿qué tan fácil es escribir y mantener pruebas?
- **Compatibilidad con lenguajes**: ¿el framework admite TypeScript y Python, los dos lenguajes que más usa nuestro equipo?
- **Pruebas de interfaz de usuario interactiva**: ¿qué tan bien maneja el framework interfaces de usuario complejas e interactivas, como gráficos, cargas de archivos y datos dinámicos?
- **Integración con CI/CD**: ¿qué tan bien se integra el framework con las herramientas y servicios comunes de CI/CD?
- **Compatibilidad entre navegadores**: ¿qué navegadores son compatibles y qué rendimiento tienen?
- **Rendimiento y velocidad**: ¿con qué rapidez se ejecutan las pruebas, especialmente en una canalización de CI/CD?
- **Escalabilidad**: ¿qué tan bien puede escalar el framework si se añaden más pruebas o escenarios más complejos?
- **Comunidad y ecosistema**: ¿qué tan activa es la comunidad del framework? ¿Hay muchas integraciones y extensiones disponibles?

### 5. **Consideraciones**

#### 5.1 **Playwright**

##### **Ventajas**:
1. **API más inteligente para cargas de archivos locales**: la API de Playwright para interactuar con archivos locales y realizar cargas de archivos es más simple e intuitiva. Esto facilitaría implementar y mantener las pruebas de carga de archivos.
2. **Sintaxis y generación de código**: Playwright tiene una sintaxis más corta y concisa. Esto da como resultado menos código repetitivo, lo que mejora la mantenibilidad y la eficiencia del desarrollador. Además, esta sintaxis más corta mejora la calidad de la generación de código con OpenAI, lo que facilita generar guiones de prueba automáticamente.
3. **Pruebas de interfaz de usuario interactiva**: Playwright destaca en la prueba de aplicaciones web dinámicas e interactivas, como las que tienen gráficos ricos, interacciones de usuario complejas y actualizaciones en tiempo real. Maneja con gran eficacia WebSockets, WebRTC, shadow DOM y otras tecnologías web modernas.
4. **Compatibilidad entre navegadores**: Playwright es compatible con **Chromium**, **WebKit** y **Firefox**. Tiene un rendimiento coherente en estos navegadores, lo que debería cubrir la mayor parte de nuestras necesidades de pruebas.
5. **Integración con CI/CD**: Playwright se integra sin problemas con las plataformas modernas de CI/CD (GitHub Actions, Jenkins, etc.). Puede ejecutar pruebas en paralelo en distintos navegadores, lo que optimiza los tiempos de ejecución de las pruebas y lo hace adecuado para el desarrollo rápido.
6. **Rápido y fiable**: Playwright es en general más rápido que Selenium, especialmente en modo sin interfaz (headless), y más resistente al tratar con elementos web asíncronos.

##### **Desventajas**:
1. **Pruebas en móviles limitadas**: aunque Playwright admite la emulación móvil para navegadores, carece de capacidades de prueba móvil nativas como la integración de Selenium con Appium para pruebas móviles reales.
2. **Ecosistema más pequeño**: Playwright es todavía más nuevo y menos consolidado que Selenium. Aunque tiene una comunidad de rápido crecimiento y buena documentación, puede que aún no tenga el vasto ecosistema de complementos e integraciones que ofrece Selenium.
3. **Compatibilidad limitada con navegadores**: aunque Playwright cubre los principales navegadores modernos (Chrome, Safari, Firefox), su compatibilidad con navegadores heredados (p. ej., Internet Explorer) no es tan sólida como la de Selenium.

#### 5.2 **Selenium**

##### **Ventajas**:
1. **Mayor trayectoria y madurez**: Selenium existe desde hace mucho tiempo y tiene un historial comprobado. Se usa ampliamente en muchos equipos y sectores, lo que ha dado lugar a un vasto ecosistema de complementos, integraciones y recursos.
2. **Compatibilidad entre navegadores y plataformas**: Selenium admite una **amplia variedad de navegadores** y versiones, incluido **Internet Explorer**, y también puede integrarse con diversas herramientas como **Docker**, **Selenium Grid** y **servicios en la nube** para pruebas distribuidas.
3. **Pruebas en móviles**: Selenium, mediante su integración con **Appium**, es mucho más sólido para las pruebas móviles, tanto de aplicaciones Android como iOS. Esto lo convierte en la mejor opción para proyectos con un enfoque móvil primero o muy centrado en móviles.
4. **Pruebas con varios monitores**: Selenium ofrece mejor compatibilidad con escenarios que implican **varios monitores** o interacciones complejas con varias ventanas.

##### **Desventajas**:
1. **Complejidad**: la API de Selenium es más verbosa y explícita. Aunque esto puede ser una ventaja en algunos casos, significa más código que escribir y mantener, lo que puede reducir la agilidad del desarrollador, algo especialmente importante en un entorno de startup.
2. **Rendimiento**: Selenium generalmente se ejecuta más despacio que Playwright, especialmente en modo sin interfaz (headless). Esto podría afectar a las canalizaciones de CI/CD, en particular a medida que crece el número de pruebas.
3. **Pruebas de interfaz de usuario interactiva**: Selenium no es tan fluido como Playwright al probar interfaces web modernas e interactivas, en especial con gráficos y actualizaciones de datos en tiempo real. Requiere más configuración y manejo para interactuar de manera fiable con el contenido dinámico.

### 6. **Resumen comparativo**

| Característica                    | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Facilidad de uso**              | Sintaxis más corta, más intuitiva para interfaces modernas | Más explícita, requiere más código repetitivo |
| **Compatibilidad con lenguajes**  | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Pruebas de interfaz interactiva** | Excelente para interfaces dinámicas y en tiempo real | Maneja interfaces básicas, pero más verbosa y compleja para interacciones ricas |
| **Pruebas de carga de archivos**  | API más inteligente para cargas de archivos   | Más verbosa, API menos intuitiva         |
| **Integración con CI/CD**         | Fácil integración con GitHub Actions, Jenkins | Sólida integración con muchas herramientas de CI |
| **Pruebas en móviles**            | Limitada, solo emulación                      | Compatibilidad total mediante Appium      |
| **Compatibilidad entre navegadores** | Chromium, WebKit, Firefox                  | Compatibilidad total con navegadores principales y heredados |
| **Rendimiento**                   | Rápido, optimizado para pruebas sin interfaz  | Más lento, especialmente en modo sin interfaz |
| **Pruebas con varios monitores**  | Limitada                                      | Buena compatibilidad con configuraciones de varios monitores |
| **Comunidad y ecosistema**        | En crecimiento, buena documentación           | Grande, madura, ecosistema extenso       |

### 7. **Decisión**

Tras considerar los requisitos y las contrapartidas, **Playwright** es la mejor opción para nuestras necesidades actuales. Su API más inteligente para las pruebas de carga de archivos locales, su sintaxis concisa y su sólida compatibilidad con las pruebas de interfaz de usuario interactiva lo convierten en una opción ideal para nuestro ciclo de desarrollo ágil. El hecho de que admita tanto **TypeScript** como **Python** es fundamental para nuestro equipo, y el enfoque moderno del framework para las pruebas nos permitirá escribir código limpio y mantenible.

Aunque **Selenium** sigue siendo una gran herramienta, en particular para las pruebas en móviles, la compatibilidad con navegadores heredados y las configuraciones con varios monitores, se adapta peor a nuestras necesidades actuales. Su verbosidad, su menor rendimiento y su manejo más complejo de interfaces dinámicas como los gráficos lo hacen menos óptimo para nuestro caso de uso.

### 8. **Consecuencias**

- **Acción inmediata**: adoptaremos **Playwright** para nuestras pruebas E2E, centrándonos en probar los flujos de usuario que implican registro, inicio de sesión, carga de archivos, paneles y descarga de informes.
- **Consideraciones a largo plazo**: estaremos atentos a la evolución del ecosistema de Playwright. Si nuestras necesidades cambian, en particular en torno a las pruebas en móviles o la compatibilidad con navegadores heredados, podríamos volver a considerar Selenium.
- **Capacitación y documentación**: los equipos de desarrollo tendrán que familiarizarse con la API de Playwright, en especial para manejar interfaces dinámicas y cargas de archivos.
- **Migración**: las pruebas existentes de Selenium (si las hay) se migrarán gradualmente a Playwright.

### 9. **Consideraciones futuras**
