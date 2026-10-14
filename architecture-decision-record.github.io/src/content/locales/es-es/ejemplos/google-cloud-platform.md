# Registro de decisión de arquitectura para Google Cloud Platform

## Contexto

Google Cloud Platform (GCP) es una destacada plataforma de computación en la nube que ofrece diversos servicios, como soluciones de cómputo, almacenamiento y redes. Este ADR tiene como objetivo documentar las decisiones de arquitectura adoptadas para desarrollar e implementar una infraestructura basada en GCP para nuestra organización.

## Decisión

Nuestra organización ha decidido usar Google Cloud Platform como infraestructura en la nube para nuestra aplicación. Las principales consideraciones de esta decisión son:

   - Rentabilidad

   - Escalabilidad

   - Fiabilidad

   - Flexibilidad

## Selecciones

Se han seleccionado los siguientes servicios de GCP para satisfacer nuestros requisitos:

   - Compute Engine para máquinas virtuales y recursos de cómputo

   - Cloud Storage para almacenamiento de objetos y alojamiento de archivos

   - Cloud SQL como servicio de base de datos administrado

   - Firebase para el desarrollo y alojamiento de aplicaciones

## Justificación

   - Rentabilidad: Google Cloud Platform es muy rentable en comparación con otras plataformas en la nube, lo que la convierte en una opción atractiva para organizaciones con limitaciones presupuestarias.

   - Escalabilidad: la infraestructura de GCP, fácil de escalar, permite manejar cualquier cantidad de tráfico en tiempo real.

   - Fiabilidad: los servicios administrados de GCP ofrecen una alta fiabilidad, con copias de seguridad automatizadas y capacidades de recuperación ante desastres que garantizan una alta disponibilidad de recursos y datos.

   - Flexibilidad: la plataforma ofrece diversas herramientas y servicios en distintos ámbitos, como IA, análisis de datos e IoT, lo que la hace muy versátil.

## Consecuencias

Migrar a Google Cloud Platform requerirá capacitar a nuestros equipos en los servicios de GCP, rediseñar la arquitectura de la aplicación para que sea compatible con los servicios seleccionados y actualizar el código de infraestructura para admitir los servicios de GCP. Sin embargo, se espera que, una vez completada la migración, contemos con una infraestructura muy escalable, fiable y rentable para alojar nuestra aplicación. Además, tendremos que gestionar los costos continuos de aprovisionar recursos en GCP.

## Conclusión

Google Cloud Platform es una excelente opción para nuestra infraestructura en la nube por su rentabilidad, escalabilidad, fiabilidad y flexibilidad. Al utilizar los servicios seleccionados, podemos ofrecer una infraestructura muy disponible y sólida para nuestra aplicación.
