# Registro de decisión de arquitectura: elección de una tecnología de base de datos

## Estado

Aceptado

## Contexto

Estamos diseñando una nueva aplicación que requiere almacenar y recuperar datos de manera escalable y con buen rendimiento. Hemos identificado tres tipos de tecnologías de base de datos de uso común: bases de datos relacionales, bases de datos de documentos y bases de datos de eventos.

Las bases de datos relacionales almacenan los datos en tablas con esquemas fijos y aplican restricciones estrictas de integridad de datos. Son adecuadas para aplicaciones que requieren relaciones de datos complejas y transacciones. Algunos ejemplos son MySQL, PostgreSQL y Oracle.

Las bases de datos de documentos almacenan los datos en documentos similares a JSON y no tienen esquema. Son muy adecuadas para aplicaciones que requieren modelos de datos flexibles y escalado horizontal. Algunos ejemplos son MongoDB, Couchbase y Amazon DynamoDB.

Las bases de datos de eventos almacenan los datos como una serie de eventos, registrando cada cambio en los datos. Son adecuadas para aplicaciones que requieren auditoría, event sourcing y procesamiento de datos complejo. Algunos ejemplos son Apache Kafka, Apache Pulsar y AWS Kinesis.

## Decisión

Tras evaluar cuidadosamente los requisitos y las restricciones de nuestra aplicación, hemos decidido usar una base de datos de documentos.

## Justificación

Hemos elegido una base de datos de documentos porque:

1. Nuestra aplicación requiere un modelo de datos flexible que pueda evolucionar con el tiempo. Las bases de datos de documentos nos permiten almacenar los datos en un formato sin esquema, lo que significa que podemos añadir campos nuevos o cambiar la estructura de los documentos existentes sin modificar el esquema de la base de datos.

2. Nuestra aplicación necesita escalar horizontalmente para manejar grandes volúmenes de datos y de tráfico. Las bases de datos de documentos ofrecen compatibilidad integrada con la fragmentación (sharding) y la replicación, lo que nos permite distribuir los datos entre varios servidores y manejar un alto rendimiento de lectura y escritura.

3. Nuestra aplicación requiere una recuperación de datos rápida y eficiente. Las bases de datos de documentos ofrecen potentes capacidades de indexación y consulta que nos permiten recuperar datos de forma rápida y eficiente.

4. Nuestra aplicación no requiere transacciones complejas ni relaciones de datos. Si bien las bases de datos relacionales sobresalen en la aplicación de restricciones de integridad de datos y en el manejo de transacciones complejas, nuestra aplicación no tiene tales requisitos. Las bases de datos de documentos pueden ofrecer garantías suficientes de consistencia y durabilidad para nuestro caso de uso.

## Consecuencias

Al elegir una base de datos de documentos, tendremos que invertir en aprender y comprender la tecnología específica que elijamos usar. Además, tendremos que asegurarnos de que el modelo de datos de nuestra aplicación encaje bien con el modelo de datos de la base de datos de documentos para maximizar el rendimiento y la escalabilidad.

Sin embargo, creemos que los beneficios de usar una base de datos de documentos superan los costos, y que es la mejor opción para los requisitos y las restricciones de nuestra aplicación.
