# Registro de decisión de arquitectura: orquestación de contenedores con Kubernetes

## Planteamiento del problema 

Necesitamos seleccionar una plataforma de orquestación de contenedores para nuestro creciente portafolio de aplicaciones nativas de la nube. Nuestro despliegue actual en la plataforma heredada es demasiado lento y no es lo bastante ágil para seguir el ritmo de nuestras crecientes necesidades. Buscamos un sistema que nos permita escalar nuestros servicios de la manera más eficiente posible sin renunciar a la agilidad ni a la facilidad de uso.

## Alternativas consideradas

1. Docker Swarm

2. Kubernetes

3. Apache Mesos

## Decisión tomada

Tras realizar un análisis exhaustivo de cada plataforma de orquestación de contenedores, hemos decidido adoptar Kubernetes como la mejor opción para las necesidades de nuestra empresa. Nuestras razones para elegir Kubernetes son las siguientes:

1. **Escalabilidad:**  El diseño singular de Kubernetes es perfecto para escalar aplicaciones y, a medida que evolucionen con el tiempo nuestros requisitos de escalabilidad, Kubernetes tiene la capacidad integrada de atender estos cambios sin problemas.

2. **Arquitectura descentralizada:**  La topología maestro-trabajador (master-worker) de Kubernetes asegura una arquitectura descentralizada que garantiza que no haya un único punto de fallo.

3. **Apoyo de la comunidad:**  Kubernetes tiene la comunidad de código abierto más grande y activa, lo que significa que cuenta con un gran número de colaboradores, desarrolladores y proveedores, lo que nos facilita obtener ayuda y encontrar recursos.

4. **Apoyo del ecosistema:**  Kubernetes tiene un ecosistema en crecimiento con una variedad de herramientas de terceros, integraciones con registros de contenedores, canalizaciones de CI/CD, almacenamiento de datos y más.

Por lo tanto, hemos decidido adoptar Kubernetes como nuestra plataforma de orquestación de contenedores para el presente y el futuro inmediato.

<h6>Crédito: esta página fue generada por ChatGPT y luego editada para mejorar la claridad y el formato.</h6>
