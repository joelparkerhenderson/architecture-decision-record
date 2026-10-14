# Registro de decisión de arquitectura: editores de código de programación

## Contexto

Los editores de código de programación son una herramienta esencial para que los desarrolladores escriban y editen código. Hay numerosos editores de código disponibles, cada uno con su propio conjunto de funciones, ventajas y desventajas. El propósito de este ADR es documentar las decisiones de arquitectura adoptadas para los editores de código de programación.

## Prioridades

La arquitectura de los editores de código de programación debe priorizar lo siguiente:

* **Modularidad**: el editor de código debe diseñarse de forma modular, de modo que los desarrolladores puedan personalizarlo y ampliarlo según sea necesario. Esto permite una arquitectura flexible que puede adaptarse a las necesidades de distintos desarrolladores y equipos.

* **Rendimiento**: el editor de código debe tener buen rendimiento y responder con rapidez, de modo que los desarrolladores puedan trabajar con eficiencia sin que la herramienta que usan los frene.

* **Interfaz de usuario**: la interfaz de usuario debe ser intuitiva y fácil de usar, de modo que los desarrolladores puedan concentrarse en su código en lugar de luchar con el editor.

* **Extensibilidad**: el editor de código debe diseñarse para permitir una fácil ampliación con complementos e integraciones de terceros.

* **Compatibilidad**: el editor de código debe ser compatible con una amplia gama de lenguajes de programación y tecnologías, lo que lo convierte en una herramienta útil para una amplia gama de desarrolladores.

## Decisión

Con base en estas prioridades, la arquitectura de los editores de código de programación debe diseñarse con los siguientes componentes:

* **Núcleo**: este componente proporciona la funcionalidad básica del editor de código, como el resaltado de sintaxis, la edición de texto y la gestión de archivos.

* **UI**: este componente proporciona la interfaz de usuario del editor de código, incluidos menús, barras de herramientas y atajos de teclado.

* **Complementos**: este componente permite a los desarrolladores ampliar la funcionalidad del editor de código instalando complementos de terceros. Los complementos pueden aportar funciones adicionales, como autocompletado de código, linting o depuración.

* **Integraciones**: este componente permite que el editor de código se integre con otras herramientas y tecnologías, como sistemas de control de versiones, sistemas de compilación o herramientas de depuración.

## Justificación

La modularidad del editor de código permite a los desarrolladores personalizarlo y ampliarlo según sea necesario. Esto es importante porque distintos desarrolladores y equipos tienen necesidades y flujos de trabajo diferentes, y una arquitectura flexible puede dar cabida a estas diferencias.

* **Rendimiento**: crucial porque los desarrolladores necesitan poder trabajar con eficiencia sin que sus herramientas los frenen. Un editor de código con buen rendimiento es esencial para la productividad y puede ayudar a los desarrolladores a mantener su enfoque y concentración.

* **UI**: importante porque permite a los desarrolladores concentrarse en su código en lugar de luchar con el editor. Esto puede traducirse en mayor productividad y menos frustración para los desarrolladores.

* **Extensibilidad**: poderosa porque permite adaptar el editor de código a distintas necesidades y flujos de trabajo. Los complementos e integraciones de terceros pueden aportar funciones y capacidades adicionales que no se incluyen en el editor base.

* **Compatibilidad**: valiosa porque permite usar el editor de código con una amplia gama de lenguajes de programación y tecnologías. Esto convierte al editor en una herramienta más útil para una amplia gama de desarrolladores.

Los componentes de núcleo, complementos, integraciones y UI proporcionan una clara separación de responsabilidades y permiten una arquitectura modular que puede ampliarse y personalizarse fácilmente. Esta arquitectura es flexible, tiene buen rendimiento y es compatible con una amplia gama de lenguajes de programación y tecnologías, lo que la convierte en una herramienta útil para los desarrolladores.
