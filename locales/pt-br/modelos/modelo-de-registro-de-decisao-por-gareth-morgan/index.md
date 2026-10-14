# [000] Título
*Atribua um número a cada ADR para facilitar referência e catalogação* \
*NOTA: Todo texto em itálico fornece dicas e deve ser removido na produção*

## Status - RASCUNHO / ATIVO / OBSOLETO por [000] / SUBSTITUI [000]

## Contexto
*Descreva brevemente o(s) problema(s) que esta ADR pretende abordar e por que esses problemas existem.*

## Abordagem decidida
*Detalhe a decisão arquiteturalmente significativa que foi / será tomada e descreva como ela aborda os problemas descritos na seção Contexto.*

## Consequências
*Qual é o impacto desta decisão nas características de arquitetura e nos requisitos funcionais do sistema?*

## Governança
*Como os resultados desta decisão serão monitorados?* \
*Como a conformidade com esta decisão será assegurada?*

## Análise de opções
*Se aplicável, inclua ou vincule qualquer análise de trade-offs realizada para chegar à decisão tomada neste documento.*

### Chave
*Opcional: Forneça auxílios visuais para as partes interessadas que possam ajudar a identificar rapidamente os trade-offs positivos e negativos - por exemplo, destaques simples de semáforo com prefixos positivos ou negativos.*

Um fundo <span style="background-color:#4bce97; color:black;">verde</span> indica um bom encaixe, piorando até <span style="background-color:#f1c232; color:black;">âmbar</span>, com <span style="background-color:#e06666; color:black;">vermelho</span> sendo o pior encaixe. \
\+ indica um comentário de impacto positivo \
\- indica um comentário de impacto negativo

### Visão geral de alto nível
*Em uma olhada, quão bem cada opção se ajusta ao contexto do problema?*

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
          + Muito fácil
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Trabalhosa
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Grande implementação que exige conhecimento especializado
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
            - Relativamente lento
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
            + Melhora ligeiramente a experiência de onboarding do cliente
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ideal para a próxima fusão
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Requisitos funcionais
*Quão bem cada opção potencial atende aos requisitos funcionais desejados?*

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

*Opcional: Adicione linhas / outra tabela para cobrir cenários futuros conhecidos.*

### Requisitos não funcionais
*Quão bem cada opção potencial atende às características de arquitetura desejadas?
Nota: 'Características de arquitetura' seria um título mais apropriado, mas adapte isto à linguagem familiar ao seu domínio de negócio.*

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

*Opcional: Adicione ou vincule definições das características de arquitetura conforme se aplicam ao seu negócio / produto.*
