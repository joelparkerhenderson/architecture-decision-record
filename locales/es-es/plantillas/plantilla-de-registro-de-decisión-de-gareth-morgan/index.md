# [000] Título
*Asigne un número a cada ADR para facilitar su referencia y catalogación* \
*NOTA: todo el texto en cursiva son sugerencias y debe eliminarse en la versión definitiva*

## Estado - BORRADOR (DRAFT) / ACTIVO (ACTIVE) / OBSOLETO (DEPRECATED) por [000] / SUSTITUYE (SUPERSEDES) a [000]

## Contexto
*Describa brevemente el o los problemas que este ADR pretende abordar y por qué existen.*

## Enfoque decidido
*Detalle la decisión significativa para la arquitectura que se ha tomado o se tomará y describa cómo aborda los problemas descritos en la sección Contexto.*

## Consecuencias
*¿Cuál es el impacto de esta decisión en las características de arquitectura y en los requisitos funcionales del sistema?*

## Gobernanza
*¿Cómo se supervisarán los resultados de esta decisión?* \
*¿Cómo se garantizará el cumplimiento de esta decisión?*

## Análisis de opciones
*Si corresponde, incluya o enlace cualquier análisis de compensaciones (trade-offs) realizado para llegar a la decisión tomada en este documento.*

### Leyenda
*Opcional: proporcione ayudas visuales a las partes interesadas que permitan detectar rápidamente las compensaciones positivas y negativas, por ejemplo, resaltes sencillos tipo semáforo con prefijos positivos o negativos.*

Un fondo <span style="background-color:#4bce97; color:black;">verde</span> indica un buen ajuste, que empeora pasando por el <span style="background-color:#f1c232; color:black;">ámbar</span>, y el <span style="background-color:#e06666; color:black;">rojo</span> es el peor ajuste. \
\+ indica un comentario de impacto positivo \
\- indica un comentario de impacto negativo

### Visión general
*A simple vista, ¿qué tan bien se ajusta cada opción al contexto del problema?*

<table>
  <thead>
    <tr>
      <th>Resumen</th>
      <th>Opción 1</th>
      <th>Opción 2</th>
      <th>Opción 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Facilidad de implementación</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Muy fácil
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Complicada
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Implementación grande que requiere conocimientos de expertos
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Plazos</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Muy rápida
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Bastante lenta
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Muy lenta
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Valor estratégico</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Sin valor estratégico, puramente táctica
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Mejora ligeramente la experiencia de incorporación de clientes
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ideal para la fusión próxima
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Requisitos funcionales
*¿Qué tan bien se ajusta cada posible opción a los requisitos funcionales deseados?*

<table>
  <thead>
    <tr>
      <th>Escenario</th>
      <th><i>Opción 1</i></th>
      <th><i>Opción 2</i></th>
      <th><i>Opción 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Escenario 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Escenario 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Escenario 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Opcional: añada filas o otra tabla para cubrir escenarios futuros conocidos.*

### Requisitos no funcionales
*¿Qué tan bien se ajusta cada posible opción a las características de arquitectura deseadas?
Nota: «Características de arquitectura» sería un título más apropiado, pero adáptelo al lenguaje que le resulte familiar en su dominio de negocio.*

<table>
  <thead>
    <tr>
      <th>Característica </br> de arquitectura</th>
      <th><i>Opción 1</i></th>
      <th><i>Opción 2</i></th>
      <th><i>Opción 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Escalabilidad</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Rendimiento</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Disponibilidad</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Opcional: incluya o enlace las definiciones de las características de arquitectura tal como se aplican a su negocio o producto.*
