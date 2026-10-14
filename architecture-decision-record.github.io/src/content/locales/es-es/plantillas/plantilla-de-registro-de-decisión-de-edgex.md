# Plantilla de registro de decisión de arquitectura (ADR) <!-- Reemplazar por el título del ADR -->

Esta es una plantilla para los ADR de EdgeX Foundry.

Fuente: https://docs.edgexfoundry.org/2.3/design/adr/template/


### Autores del envío

Enumere a quienes presentan el ADR.

Formato:

- Nombre (Organización)


## Registro de cambios

Enumere los cambios en el documento, incluidos el estado, la fecha y la URL del PR.

El estado es uno de: pending (pendiente), approved (aprobado), amended (enmendado), deprecated (obsoleto).

La fecha es una cadena ISO 8601 (AAAA-MM-DD).

El PR es la solicitud de incorporación de cambios (pull request) que presentó el cambio, con información como las diferencias, los colaboradores y los revisores.

Formato:

- \[Estado del ADR, p. ej. approved, amended, etc.\]\(URL de la solicitud de incorporación de cambios\) AAAA-MM-DD


## Casos de uso referenciados

Enumere todos los documentos de casos de uso y requisitos pertinentes.

El ADR requiere al menos un caso de uso pertinente y aprobado.

Formato:

- \[Nombre del caso de uso\]\(URL\)

Añada explicaciones si el ADR no atiende todos los requisitos de un caso de uso.


## Contexto

Describa:

- por qué el diseño es significativo para la arquitectura y justifica un ADR (frente a una simple incidencia y un PR para corregir un problema)

- el enfoque de diseño de alto nivel (los detalles se describen en el diseño propuesto más abajo)


## Diseño propuesto

Detalles del diseño (sin entrar en la implementación siempre que sea posible).

Esquema:

- servicios o módulos que se verán afectados (modificados)

- servicios o módulos nuevos que se añadirán

- impacto en el modelo y los DTO (cambios, adiciones, eliminaciones)

- impacto en las API (cambios, adiciones, eliminaciones)

- impacto en la configuración general (creación de nuevas secciones, cambios, adiciones, eliminaciones)

- impacto en devops


## Consideraciones

Documente las alternativas, inquietudes, asuntos accesorios o relacionados, y preguntas que surgieron en el debate del ADR. 

Indique si se resolvieron o se atenuaron y cómo.


## Decisión

Documente cualquier detalle de implementación importante acordado, salvedades, consideraciones futuras y cuestiones de diseño pendientes o aplazadas.

Documente cualquier parte de los requisitos que el diseño propuesto no satisfaga.


## Otros ADR relacionados

Enumere los ADR pertinentes, como una decisión de diseño sobre un subcomponente de una funcionalidad, un diseño que quedó obsoleto como resultado de este diseño, etc. 

Formato:

- \[Título del ADR\]\(URL\) - Relevancia


## Referencias

Enumere referencias adicionales.

Formato:

- \[Título\]\(URL\)
