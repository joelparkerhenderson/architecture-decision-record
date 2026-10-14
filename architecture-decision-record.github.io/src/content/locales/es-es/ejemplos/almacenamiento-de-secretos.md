# Almacenamiento de secretos

Contenido:

* [Resumen](#resumen)
  * [Asunto](#asunto)
  * [Decisión](#decisión)
  * [Estado](#estado)
* [Detalles](#detalles)
  * [Supuestos](#supuestos)
  * [Restricciones](#restricciones)
  * [Posiciones](#posiciones)
  * [Argumento](#argumento)
  * [Implicaciones](#implicaciones)
* [Relacionado](#relacionado)
  * [Decisiones relacionadas](#decisiones-relacionadas)
  * [Requisitos relacionados](#requisitos-relacionados)
  * [Artefactos relacionados](#artefactos-relacionados)
  * [Principios relacionados](#principios-relacionados)
* [Notas](#notas)
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Resumen


### Asunto

Necesitamos almacenar secretos, como contraseñas, claves privadas, tokens de autenticación, etc.

Algunos de los secretos están orientados al usuario. Por ejemplo, nuestro desarrollador quiere poder usar su teléfono móvil para consultar la contraseña de un servicio.

Algunos de los secretos están orientados al sistema. Por ejemplo, nuestra canalización de entrega continua necesita poder consultar las credenciales de nuestro alojamiento en la nube.


### Decisión

Bitwarden para los secretos orientados al usuario.

Vault by HashiCorp para los secretos orientados al sistema.


### Estado

Decidido. Estamos abiertos a nuevas alternativas a medida que surjan.


## Detalles


### Supuestos

Para este propósito, y en nuestro estado actual, valoramos la comodidad orientada al usuario, como las aplicaciones móviles utilizables.

  * Queremos asegurar un acceso rápido y fácil en cualquier lugar, como para un desarrollador que realiza ingeniería de fiabilidad de sistemas con guardia.

  * Queremos poder compartir algunos secretos entre personas seleccionadas, como un equipo.

No intentamos resolver el caso de un único proveedor, como almacenar todos los secretos exclusivamente en Amazon, Azure o Google.

No queremos enfoques improvisados como «recuérdalo», «apúntalo en una nota» o «averigua tu propia forma de almacenarlo».

Nuestro modelo de seguridad para este propósito está de acuerdo con usar proveedores COTS (productos comerciales listos para usar) de buena reputación, como las herramientas de gestión de contraseñas SaaS.


### Restricciones

Ahora mismo queremos algo que sea fácil, es decir, sin necesidad de escribir código, sin necesidad de instalar servidores, sin necesidad de asumir un compromiso importante, sin necesidad de estandarizar a todo el mundo.


### Posiciones

Consideramos:

1. Gestores de contraseñas listos para usar orientados al usuario: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG, etc.

2. Gestores de contraseñas COTS orientados al sistema: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Enfoques orientados a compartir: usar un documento de Google compartido, o un canal de Slack compartido, o una carpeta de red compartida, etc.

4. Enfoques improvisados de baja tecnología, como recordar, escribir una nota o confiar en que cada usuario averigüe su propio enfoque.


### Argumento

Bitwarden, LastPass, 1Password y Dashlane son todos productos comerciales listos para usar.

  * Tipos de funciones similares para usuarios, equipos, organizaciones, etc.

  * Capacidad de escritorio para Windows y Mac, y capacidad móvil para Android e iOS.

  * Extensiones de navegador para Chrome y Firefox, para el autocompletado de formularios, etc.

Bitwarden tiene dos ventajas sobre los demás:

  * Bitwarden es de código abierto, lo que significa que su seguridad puede ser revisada por pares y que la empresa es muy apreciada por los desarrolladores orientados a la seguridad.

  * Las anécdotas de trabajadores del software describen una preferencia significativa por Bitwarden frente a los demás.

Un ejemplo típico de buen artículo: https://jcs.org/2017/11/17/bitwarden

Un sitio típico de votación comparativa: https://stackshare.io/stackups/bitwarden-vs-dashlane

Aplazamos KeyPass, pass, GPG, etc. porque hay una complejidad adicional. Todos ellos parecen soluciones excelentes para usuarios técnicos. GPG parece especialmente bueno para usuarios técnicos que quieren capacidades orientadas a la línea de comandos entre sistemas.

Aplazamos KMS porque implica dependencia de un único proveedor.

Elegimos Vault para las necesidades orientadas al sistema, porque las opiniones son asombrosamente positivas y porque HashiCorp tiene un excelente historial de software y soporte de primera calidad.

Vetamos los enfoques orientados a compartir, como mediante documentos compartidos, canales compartidos, carpetas de red compartidas, etc. Estos no ofrecen las cualidades de seguridad que queremos.

Vetamos los enfoques improvisados de baja tecnología, porque todos coincidimos en que no es un camino a largo plazo.


### Implicaciones

Es posible que los desarrolladores tengan que hacer seguimiento de los secretos en dos lugares: Bitwarden para el acceso orientado al usuario y Vault para el acceso orientado al sistema.


## Relacionado


### Decisiones relacionadas

La decisión sobre qué servidor de CI/CD usar debe incluir la prueba de su capacidad para acceder a los secretos.

Tendremos que decidir cómo gestionar los secretos, en términos de políticas, rotaciones, organizaciones, etc.


### Requisitos relacionados

Los secretos tendrán requisitos relacionados con el cumplimiento normativo, la auditoría y la incorporación y salida de personal de RR. HH.


### Artefactos relacionados

Esperamos poder exportar algunos secretos a variables de entorno.


### Principios relacionados

Fácilmente reversible.

Fácilmente paralelo, es decir, es fácil usar una variedad de gestores de contraseñas.

Barato de probar, es decir, hay una prueba gratuita y ningún compromiso.


## Notas

Notas de evaluación aquí. Las notas son todas comentarios públicos en varios foros de devops.


### Vault by HashiCorp

Vault es exactamente lo que quieres aquí. 

Sin embargo, no pongas Vault directamente en producción: levántalo primero en un entorno de pruebas, porque la documentación de HashiCorp puede ser bastante deficiente aunque sus productos sean asombrosos.

Curva de aprendizaje muy pronunciada y no es trivial de levantar. 

La configuración inicial es un poco engorrosa. Aun así vale la pena, y la comunidad lo apoyará lo suficiente como para que te las arregles.

Documentación horrible, pero hay muchas guías en línea de personas que lo configuran y, si combinas unas cuantas, tendrás una configuración que funcione.

La configuración inicial exigió trastear con sus helm charts (vault y consul). Aunque técnicamente puedes usar muchos otros back ends, de verdad no lo recomiendo. El back end/consul puede ser diminuto si no tienes muchos datos que almacenar.

Definitivamente familiarízate y acostúmbrate a usar la CLI, porque la GUI es más bien una prueba de concepto o un portal publicitario de su edición empresarial.

El hecho de que no puedas simplemente «rellenarlo» es una lata. Por ejemplo, si tienes 5 campos, tienes que añadir manualmente cada campo para cada elemento. Así que no es que predefinas campos para una categoría específica y rellenes esos campos para todos los elementos de esa categoría, sino más bien «generas todo cada vez», lo que (en mi opinión) es un fastidio.

Quizá también quieras echar un vistazo a goldfish como interfaz de usuario sobre vault. Hace bastante agradable convencer a tu equipo. También tienen una demo. 1. Configura consul. 2. Configura vault apuntando a consul. 3. Configura goldfish apuntando a vault. 3. Configura algún trabajo cron para ejecutar consul snapshot para las copias de seguridad.



### LastPass

LastPass Teams. Lo usamos, tiene plantillas personalizadas, ACL, no falta nada en mi opinión.

Implementé LastPass en mi organización y le doy un C+/B-. El mayor problema últimamente es la falta de fiabilidad. En los últimos 90 días ha habido varias horas en las que las cajas fuertes (vaults) se vieron forzadas a pasar al modo sin conexión. Esto no es lo ideal para mi organización porque tenemos, literalmente, más de 4000 contraseñas almacenadas en más de 20 carpetas compartidas. Como puedes imaginar, con tantas contraseñas, al menos algunas se actualizan o se añaden a diario. Tenemos un plan de recuperación ante desastres si los problemas duran más de una o dos horas: un script firma y cifra cada noche un volcado CSV de la caja fuerte que puede importarse a keepass.

LastPass ha tenido episodios no reportados de servicio degradado: el inicio de sesión «funciona» pero no trae los sitios, funciones aleatorias rotas en el panel de administración y no se comparten correctamente las claves de las nuevas carpetas compartidas de nivel superior. Tengo un usuario específico de «envío de claves»/copia de seguridad que está en todos los grupos. Normalmente iniciar sesión como ese usuario soluciona cualquier problema de uso compartido de claves, pero no cuando el servicio está degradado, diga lo que diga la página de estado...

Para la integración puede ser fácil si tienes ACL adecuadas con un modelo de mínimo privilegio, p. ej., si un usuario tiene lectura y escritura y solo lectura sobre una entrada o carpeta, solo obtiene permisos de solo lectura. Lamentablemente las ACL de mi organización no son las mejores, así que terminé usando la API de aprovisionamiento JSON y ~500 líneas de python porque la naturaleza dependiente de nuestras cientos de ACL no se ajustaba bien al modelo de mínimo privilegio. Acabé obteniendo todas las ACL en las que estaba un usuario y haciendo una especie de recorrido de dependencias.

Si tu estructura de ACL o de grupos ya está construida pensando en una estructura de mínimo privilegio, la herramienta de sincronización AD/LDAP para Windows funcionará bien.

Ponte en contacto con su equipo de ventas y pueden ofrecerte una prueba empresarial más larga. Asegúrate de entender por completo sus limitaciones antes de apretar el gatillo. Tuvimos bastantes dolores de crecimiento, pero, aparte de las interrupciones o los deterioros del lado del servidor, ha sido increíblemente fluido.


### Bitwarden

Bitwarden tiene unas buenas herramientas a su alrededor (interfaz web, CLI, móvil, escritorio). Autoalojable y bastante fácil de configurar. Documentación bastante buena y herramienta recomendada por PrivacyTools.


### EnvKey

https://www.envkey.com/ es un SaaS. Muy fácil de implementar, integrar y gestionar.

Funciones:

  * Proteger claves de API y credenciales.

  * Mantener la configuración sincronizada en todas partes.

  * Gestión inteligente de configuración y secretos cifrada de extremo a extremo. 

  * Evitar el uso compartido inseguro y la proliferación de configuraciones. 

  * Integrar en minutos.

Capacidades:

  * Gestionar la configuración y los niveles de acceso de todas tus aplicaciones, entornos y equipos en un solo lugar.

  * Configurar cualquier entorno de desarrollo o de servidor con una sola variable de entorno.

Ventajas:

  * Buena página de inicio.

  * Propuesta de valor clara.

  * Aplicación web visualmente excelente.

  * Datos de ejemplo superiores, p. ej., Algolia, AWS, Datadog, GitHub, Stripe, etc.

  * Hablé con el fundador durante 30 minutos sobre la empresa, la interfaz de usuario, etc. Dane parece bien informado, honesto sobre los pros y los contras, y un socio viable.

  * La empresa es esencialmente una empresa típica de Y Combinator, con 1 fundador. Recaudó 120 000 USD en 2018-01.

  * El foco está en llegar a las funciones empresariales, en especial pasar del alojamiento en la nube de EnvKey a la instalación local (on-prem) o a BYOC.

  * Posible camino a seguir: empezar con EnvKey por su facilidad de uso y luego (o en paralelo) añadir Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant es un servicio de gestión de secretos de código abierto que ofrece un almacenamiento y un acceso fáciles de usar a los secretos de forma segura, de los desarrolladores de Lyft.

Autenticación KMS: Confidant resuelve el problema de la autenticación del «huevo y la gallina» usando AWS KMS e IAM para permitir que los roles de IAM generen tokens de autenticación seguros que Confidant puede verificar. Confidant también gestiona las concesiones de KMS para sus roles de IAM, lo que permite que los roles de IAM generen tokens que pueden usarse para la autenticación de servicio a servicio o para pasar mensajes cifrados entre servicios.

Cifrado en reposo de secretos versionados: Confidant almacena los secretos de forma que solo se pueden añadir datos (append-only) en DynamoDB, y genera una clave de datos KMS única para cada revisión de cada secreto, usando criptografía simétrica autenticada Fernet.

Una interfaz web fácil de usar para gestionar secretos: Confidant ofrece una interfaz web en AngularJS que permite a los usuarios finales gestionar fácilmente los secretos, las asignaciones de secretos a servicios y el historial de cambios.


### Devolutions Password Server

https://server.devolutions.net/

Proteja, gestione y supervise el acceso a cuentas y sesiones con privilegios.

Una caja fuerte de contraseñas completa y de alta seguridad que le permite controlar el acceso a sus cuentas con privilegios, a la vez que mejora la visibilidad general de la red para los administradores de sistemas y ofrece una experiencia fluida a los usuarios finales.

Funciones: caja fuerte de contraseñas centralizada de la organización, caja fuerte privada específica de cada usuario, gestor de contraseñas, inyección de credenciales,
integración con Active Directory, control de acceso basado en roles, autenticación de dos factores, listo para la empresa, restricciones por IP, capacidades de gestión, generador automático de contraseñas, acceso desde aplicación móvil, historial de contraseñas, informes de acceso, alertas por correo electrónico.

  * admite el cifrado de datos

  * admite múltiples esquemas de autenticación, incluidos LDAP, O365 y usuarios locales, CON compatibilidad con MFA de múltiples fuentes

  * múltiples repositorios o cajas fuertes con controles de acceso de grano fino para varios equipos

  * interfaz web moderna

  * cajas fuertes privadas de credenciales y de conexiones para credenciales y conexiones personales

  * aplicaciones móviles para iOS/Android

  * registros de auditoría de cada entrada, quién, qué y cuándo, con un aviso opcional para indicar por qué acceden

  * plantillas personalizables (aunque admiten de forma nativa cientos de tipos de conexión)

  * muchísimas más funciones y un cliente pesado para Windows/Mac (Remote Desktop Manager) con el que puedes sincronizar y que amplía enormemente las opciones... conexiones con un clic

  * el precio no está tan mal: hasta 15 usuarios cuesta 500 USD al año el servidor de contraseñas


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Funciones de la versión local (on-premise): 

  * Control total sobre sus sistemas e infraestructura de seguridad de extremo a extremo

  * Despliegue el software dentro de su centro de datos local o de su propia instancia de nube privada virtual

  * Cumpla las obligaciones legales y regulatorias que exigen que todos los datos y sistemas residan en las instalaciones

Funciones de la versión en la nube:

  * El modelo de software como servicio permite registrarse y empezar de inmediato

  * Escalabilidad elástica a medida que crece

  * Controles y redundancia proporcionados por Azure con un SLA de disponibilidad del 99,9 %

Comentarios de usuarios:

  * Antes usábamos ese producto. Era tan fácil de eludir y las reglas solo funcionan para gente lista. Los usuarios perezosos o torpes pueden estropearlo fácilmente en un área de equipo. Los precios son negociables cuando hablas con ellos.

  * Puedes ejecutarlo con SQL express y una máquina con Win 7. 

  * Barato.
