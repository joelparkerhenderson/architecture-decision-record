# Registro de decisión de arquitectura: opciones de autenticación y autorización

<!--

ChatGPT prompt:

Explain web application authentication authorization. 

Describe:  OAuth, OpenID Connect, SAML, WS-Federation, LDAP, Social SSO Providers.

-->

La autenticación y la autorización de aplicaciones web son dos conceptos cruciales para proteger el acceso a aplicaciones y servicios. Ambos tratan sobre la identidad de los usuarios y la forma en que se conceden los permisos, pero se centran en aspectos distintos:

- La **autenticación** es el proceso de verificar la identidad de un usuario o sistema.
- La **autorización** es el proceso de determinar a qué recursos o acciones puede acceder el usuario o sistema autenticado.

Veamos ahora los protocolos y tecnologías específicos que ha mencionado, de uso común en las aplicaciones web modernas para gestionar la autenticación y la autorización.

### 1. **OAuth (Open Authorization)**

**OAuth** es un estándar abierto de autorización. Permite que un usuario conceda a una aplicación de terceros un acceso limitado a sus recursos sin compartir sus credenciales. La idea clave es el **acceso delegado**. OAuth se usa a menudo en situaciones en las que los usuarios pueden iniciar sesión en un servicio de terceros (p. ej., iniciar sesión con Google) sin proporcionar directamente su nombre de usuario y contraseña al tercero.

- **Flujo**: OAuth suele seguir un flujo **basado en tokens**, en el que un servidor de autorización emite un token de acceso a la aplicación de terceros. Este token representa los permisos del usuario, y la aplicación lo usa para acceder a los datos o recursos del usuario desde una API.
- **Ejemplo**: un usuario inicia sesión en una aplicación de terceros con su cuenta de Google. Google verifica la identidad del usuario y luego concede un token que permite a la aplicación de terceros acceder a algunos datos de Google (p. ej., Google Calendar).

OAuth **no** gestiona la autenticación directamente; trata de conceder acceso. Para la autenticación, OAuth suele combinarse con otros protocolos, como **OpenID Connect**.

### 2. **OpenID Connect (OIDC)**

**OpenID Connect (OIDC)** es una capa de identidad construida sobre **OAuth 2.0** que añade autenticación a las capacidades de autorización de OAuth. En esencia, OpenID Connect extiende OAuth para gestionar la **autenticación de usuarios** y ofrece una forma estandarizada para que las aplicaciones verifiquen la identidad de un usuario.

- **Flujo**: cuando un usuario inicia sesión mediante OpenID Connect, la aplicación de terceros solicita un token de ID (además del token de acceso de OAuth). El token de ID contiene información sobre el usuario (como su nombre de usuario, su correo electrónico y otras declaraciones). Esto permite que la aplicación sepa quién es el usuario y si está autenticado.
- **Ejemplo**: iniciar sesión en un servicio como Slack con su cuenta de Google (siendo Google el proveedor de OpenID Connect) implica autenticación mediante OpenID Connect, mientras que OAuth gestiona el acceso a sus recursos de Google.

OIDC facilita que las aplicaciones de terceros **autentiquen a los usuarios** y, al mismo tiempo, permite un control de grano fino sobre a qué recursos pueden acceder esas aplicaciones.

### 3. **SAML (Security Assertion Markup Language)**

**SAML** es un estándar más antiguo, basado en XML, que se usa para intercambiar datos de autenticación y autorización entre las partes, en particular en escenarios de **inicio de sesión único (SSO)**. Se usa principalmente en entornos empresariales para que los usuarios se autentiquen una vez y accedan a varias aplicaciones sin volver a introducir sus credenciales.

- **Flujo**: el usuario se autentica primero con un proveedor de identidad (IdP). El IdP genera una **aserción SAML** firmada que incluye la identidad del usuario y los atributos relacionados. La aserción se envía al proveedor de servicios (SP), que la usa para autorizar el acceso a la aplicación.
- **Ejemplo**: un empleado inicia sesión en el portal de su empresa (el IdP) y se le inicia sesión automáticamente en otros sistemas, como el correo electrónico, el CRM, etc., sin volver a introducir sus credenciales. El proceso de autenticación se basa en la aserción SAML enviada por el IdP.

SAML se usa habitualmente en **soluciones empresariales de SSO** y funciona bien para aplicaciones web en entornos corporativos, pero es menos apto para dispositivos móviles que OAuth/OIDC.

### 4. **WS-Federation (Web Services Federation)**

**WS-Federation** es otro protocolo usado para el **inicio de sesión único (SSO)**, especialmente en entornos empresariales basados en Microsoft. Forma parte de la familia de especificaciones **WS-* (Web Services)** y permite la federación de identidades entre distintos dominios de seguridad (como entre distintas organizaciones o entre distintos servicios).

- **Flujo**: WS-Federation permite que un **proveedor de identidad (IdP) de confianza** autentique a los usuarios y emita tokens que el proveedor de servicios pueda usar para la autorización. Es similar a SAML, pero suele usarse en escenarios que dependen en gran medida de tecnologías de Microsoft.
- **Ejemplo**: un usuario inicia sesión en una aplicación empresarial alojada en Microsoft Azure Active Directory (AD), y su identidad puede usarse para acceder a otros servicios federados, incluidas aplicaciones alojadas por proveedores externos.

Aunque en muchos entornos web modernos WS-Federation ha sido sustituido en gran medida por protocolos más nuevos como OAuth 2.0 y OpenID Connect, todavía se usa en sistemas heredados, especialmente en empresas centradas en Microsoft.

### 5. **LDAP (Lightweight Directory Access Protocol)**

**LDAP** es un protocolo usado para acceder a servicios de directorio y gestionarlos, comúnmente utilizado para **almacenar credenciales de usuario** y gestionar el control de acceso en un directorio centralizado (a menudo llamado **servicio de directorio**). LDAP no trata específicamente de autenticación ni de autorización, sino que se usa para almacenar y recuperar datos de identidad, que luego se emplean en esos procesos.

- **Autenticación**: LDAP permite que una aplicación autentique a los usuarios consultando al servicio de directorio las credenciales (como las contraseñas).
- **Autorización**: también gestiona los roles y permisos de los usuarios, lo que ayuda a determinar si un usuario tiene acceso a ciertos recursos.
- **Ejemplo**: muchas empresas usan directorios basados en LDAP (p. ej., **Active Directory**) para la autenticación y la autorización, especialmente en entornos Windows.

LDAP es fundamental para que las empresas gestionen el acceso de los usuarios a los sistemas internos, pero en un contexto web moderno, LDAP suele integrarse con otros protocolos como SAML u OAuth para una gestión de identidades más completa.

### 6. **Proveedores de SSO social**

Los proveedores de **inicio de sesión único (SSO)** social, como **Facebook**, **Google**, **Twitter**, **GitHub** y otros, permiten a los usuarios autenticarse en aplicaciones de terceros con sus credenciales de redes sociales. Es un tipo de **autenticación basada en OAuth** en la que el servicio de terceros (p. ej., Google) es el proveedor de identidad.

- **Flujo**: el usuario hace clic en «Iniciar sesión con Google» (por ejemplo). La aplicación redirige a Google, donde el usuario inicia sesión (si aún no lo ha hecho). Luego Google proporciona un token de acceso o un token de ID a la aplicación de terceros, que puede usarse para autenticar al usuario y, posiblemente, acceder a sus datos.
- **Ejemplo**: muchas aplicaciones permiten iniciar sesión con sus credenciales de Google o Facebook. La aplicación usará OAuth u OpenID Connect entre bastidores para verificar su identidad y, en algunos casos, acceder a determinados datos de redes sociales.

El SSO social es un método cómodo y ampliamente adoptado de autenticación, porque reduce la fricción para los usuarios, que quizá no quieran crear otro nombre de usuario y otra contraseña más.

---

### Resumen de las diferencias:

- **OAuth**: se usa para la autorización; permite que las aplicaciones de terceros accedan a los datos del usuario sin exponer sus credenciales.
- **OpenID Connect**: extiende OAuth para proporcionar autenticación, lo que permite a las aplicaciones verificar la identidad del usuario.
- **SAML**: protocolo basado en XML usado para SSO, a menudo en entornos empresariales.
- **WS-Federation**: protocolo específico de Microsoft para la federación de identidades, usado en sistemas heredados.
- **LDAP**: protocolo para consultar servicios de directorio con el fin de autenticar usuarios y gestionar la autorización.
- **Proveedores de SSO social**: sistemas basados en OAuth (como Google y Facebook) que permiten a las aplicaciones de terceros autenticar a los usuarios con sus credenciales de redes sociales.

Cada una de estas tecnologías tiene sus propios puntos fuertes y casos de uso, y en las aplicaciones modernas es posible ver que se utiliza una combinación de ellas para distintos aspectos de la seguridad (p. ej., OAuth/OIDC para el acceso a API, SAML para el SSO empresarial).
