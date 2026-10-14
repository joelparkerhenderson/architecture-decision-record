# Registro de decisión de arquitectura: lenguaje de programación Rust

Número de decisión: AR-001

Título de la decisión: adopción del lenguaje de programación Rust

Fecha: 1 de diciembre de 2021

Estado: Aceptado

### Planteamiento del problema

A medida que seguimos desarrollando aplicaciones de software, hemos observado que resulta cada vez más difícil mitigar posibles vulnerabilidades de seguridad y evitar errores en tiempo de ejecución. Con los lenguajes de programación existentes, como C y C++, seguimos teniendo problemas como desbordamientos de búfer, fugas de memoria y comportamiento indefinido que provoca fallos en las aplicaciones. Necesitamos un lenguaje de programación que ofrezca garantías de seguridad de memoria y que sea lo bastante eficiente para respaldar aplicaciones críticas en cuanto a rendimiento.

### Consideraciones

Varios lenguajes de programación están diseñados para abordar los problemas existentes. Entre ellos, el lenguaje de programación Rust ha ganado una atención significativa en la comunidad de desarrolladores por sus características de diseño singulares. Las consideraciones incluyen:

1. Seguridad de memoria y seguridad en general

2. Rendimiento y eficiencia

3. Apoyo de la comunidad y adopción

4. Curva de aprendizaje

5. Herramientas y ecosistema

6. Compatibilidad con los sistemas de software existentes.

### Restricciones

Adoptar un nuevo lenguaje de programación requiere reentrenar a los desarrolladores, lo que consume tiempo y recursos. Integrar el lenguaje en el flujo de trabajo de desarrollo existente puede ser un desafío. Debemos garantizar la compatibilidad con los sistemas existentes y evitar cambios incompatibles para mantener la continuidad.

### Implementación

1. Nuestro equipo de desarrollo recibirá capacitación para aprender y familiarizarse con el lenguaje de programación Rust.

2. Crearemos un nuevo proyecto con Rust de forma experimental para evaluar su compatibilidad e idoneidad para nuestros fines de desarrollo.

3. Migraremos gradualmente a Rust los sistemas existentes escritos en C y C++.

4. Colaboraremos con la comunidad de Rust para explorar las herramientas y bibliotecas disponibles que puedan mejorar nuestro flujo de trabajo de desarrollo.

5. Supervisaremos el rendimiento de Rust y lo compararemos periódicamente con el de los lenguajes de programación existentes.

6. Adoptaremos un enfoque a largo plazo que equilibre los costos de capacitación e integración con los posibles beneficios de usar Rust.

### Justificación

Hemos adoptado Rust por sus características singulares, diseñadas para ofrecer garantías de seguridad de memoria y de seguridad en general, manteniendo el rendimiento y la eficiencia. El sólido sistema de tipos de Rust, su verificador de préstamos (borrow checker) y sus conceptos de seguridad de memoria lo hacen muy adecuado para desarrollar aplicaciones críticas en rendimiento y en seguridad. Además, Rust tiene una comunidad significativa de desarrolladores, lo que nos permite acceder a una amplia gama de herramientas, bibliotecas y ecosistema que respaldan nuestro flujo de trabajo de desarrollo. Aunque Rust conlleva una curva de aprendizaje, creemos que los beneficios de adoptarlo superan los costos y ofrecen una excelente oportunidad de crecimiento e innovación continuos.

### Consecuencias

1. La adopción de Rust requerirá una inversión significativa de tiempo y recursos para capacitar a los desarrolladores e integrar el lenguaje en el flujo de trabajo de desarrollo existente.

2. Adoptar Rust puede causar cierto grado de problemas de compatibilidad con los sistemas existentes, lo que requerirá refactorización y modificaciones.

3. La adopción de Rust puede aumentar el número de desarrolladores que pueden contribuir a nuestro proyecto al atraer a desarrolladores de Rust que quieren trabajar en proyectos interesantes.

4. La adopción podría traducirse en una mejora del rendimiento, la eficiencia y la seguridad en comparación con los lenguajes existentes.

5. Por último, adoptar Rust conlleva el posible beneficio de reducir las vulnerabilidades de seguridad en nuestras aplicaciones.
   
<h6>Crédito: esta página fue generada por ChatGPT y luego editada para mejorar la claridad y el formato.</h6>
