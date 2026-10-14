# [000] Título
*Atribua um número a cada ADR para facilitar a referência e a catalogação* \
*NOTA: todo o texto em itálico fornece dicas e deve ser removido para uso em produção*

## Estado - DRAFT / ACTIVE /  DEPRECATED by [000] / SUPERSEDES [000]

## Contexto
*Descreva brevemente o(s) problema(s) que este ADR pretende abordar e por que os problemas existem.*

## Abordagem decidida
*Detalhe a decisão arquiteturalmente significativa que foi/será tomada e descreva como ela aborda os problemas descritos na seção Contexto.*

## Consequências
*Qual é o impacto desta decisão nas características de arquitetura e nos requisitos funcionais do sistema?*

## Governança
*Como os resultados desta decisão serão monitorados?* \
*Como a conformidade com esta decisão será garantida?*

## Análise de opções
*Se aplicável, inclua ou vincule qualquer análise de trade-offs que tenha sido realizada para chegar à decisão tomada neste documento.*

### Legenda
*Opcional: forneça auxílios visuais às partes interessadas que ajudem a identificar rapidamente os trade-offs positivos e negativos, por exemplo, destaques simples em semáforo com prefixos positivos ou negativos.*

Um fundo <span style="background-color:#4bce97; color:black;">verde</span> indica um bom ajuste, piorando por <span style="background-color:#f1c232; color:black;">âmbar</span>, sendo o <span style="background-color:#e06666; color:black;">vermelho</span> o pior ajuste. \
\+ indica um comentário de impacto positivo \
\- indica um comentário de impacto negativo

### Visão geral de alto nível
*Quão bem cada opção se ajusta ao contexto do problema, à primeira vista?*

<table>
  <thead>
    <tr>
      <th>Resumo</th>
      <th>Opção 1</th>
      <th>Opção 2</th>
      <th>Opção 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Facilidade de implementação</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Facílimo
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Complicado
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Implementação grande que exige conhecimento especializado
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Prazos</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Muito rápido
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Bastante lento
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Muito lento
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Valor estratégico</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Sem valor estratégico, puramente tático
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Melhora levemente a experiência de integração do cliente
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ideal para a fusão iminente
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Requisitos funcionais
*Quão bem cada opção potencial se ajusta aos requisitos funcionais desejados?*

<table>
  <thead>
    <tr>
      <th>Cenário</th>
      <th><i>Opção 1</i></th>
      <th><i>Opção 2</i></th>
      <th><i>Opção 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Cenário 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Cenário 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Cenário 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Opcional: adicione linhas / outra tabela para cobrir cenários futuros conhecidos.*

### Requisitos não funcionais
*Quão bem cada opção potencial se ajusta às características de arquitetura desejadas?
Nota: ‘Características de arquitetura’ seria um título mais apropriado, mas adapte-o à linguagem familiar do seu domínio de negócio.*

<table>
  <thead>
    <tr>
      <th>Característica </br> de arquitetura</th>
      <th><i>Opção 1</i></th>
      <th><i>Opção 2</i></th>
      <th><i>Opção 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Escalabilidade</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Desempenho</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Disponibilidade</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Opcional: inclua ou vincule definições das características de arquitetura conforme se aplicam ao seu negócio / produto.*
