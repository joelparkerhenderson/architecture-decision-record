# Registro de decisión de arquitectura: API con JSON frente a gRPC

## Estado

Aceptado

## Contexto

Estamos diseñando una API para un nuevo servicio que usarán varios clientes. Hemos considerado dos opciones para implementar la API: usar JSON sobre HTTP o usar gRPC.

JSON sobre HTTP es un enfoque muy utilizado para construir API, y es compatible con muchos lenguajes de programación y frameworks. Este enfoque es simple, ligero y fácil de entender, lo que lo convierte en una buena opción para muchos proyectos. Sin embargo, puede ser menos eficiente que otras opciones, sobre todo cuando se trata de manejar grandes cantidades de datos.

gRPC, por otro lado, es una tecnología más reciente que ofrece una forma más eficiente de construir API. Usa serialización binaria para transferir datos, que puede ser más rápida y compacta que usar JSON. gRPC también admite la transmisión bidireccional (streaming), lo que lo convierte en una buena opción para aplicaciones en tiempo real.

## Decisión

Tras considerar los pros y los contras de ambas opciones, hemos decidido usar gRPC para nuestra API. Aunque JSON sobre HTTP es una opción más simple, creemos que gRPC ofrecerá una solución más eficiente y escalable para nuestro servicio. También prevemos que nuestra API manejará una gran cantidad de datos, y la serialización binaria de gRPC será más eficiente para este caso de uso.

Además, creemos que la compatibilidad de gRPC con la transmisión bidireccional será beneficiosa para las aplicaciones en tiempo real que podamos desarrollar en el futuro.

## Consecuencias

Al elegir gRPC, tendremos que usar un conjunto distinto de herramientas y bibliotecas para construir nuestra API, en comparación con usar JSON sobre HTTP. Esto puede requerir tiempo y esfuerzo adicionales para aprender e implementar estas tecnologías. Además, los clientes que quieran usar nuestra API tendrán que usar bibliotecas compatibles con gRPC, que pueden no tener un soporte tan amplio como las bibliotecas de JSON sobre HTTP.

Sin embargo, creemos que los beneficios de usar gRPC superan estos posibles inconvenientes, y confiamos en que esta decisión dará como resultado una API más eficiente y escalable.
