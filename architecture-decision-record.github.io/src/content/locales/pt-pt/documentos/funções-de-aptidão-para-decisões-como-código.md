# Funções de aptidão para decisões como código

Funções de aptidão (fitness functions) são verificações automatizadas e objetivas, escritas com código de programação, que verificam se as decisões estão sendo mantidas.

- As funções de aptidão tornam as decisões testáveis e asseguráveis.

- As funções de aptidão para decisões podem ajudar muito a garantia de qualidade, os processos regulatórios e os objetivos de governança.

## Como as funções de aptidão se conectam às decisões

Um registro de decisão documenta a decisão, enquanto uma função de aptidão a assegura.

- Exemplo de decisão: usamos event sourcing para requisitos de auditoria.

- Exemplo de função de aptidão: usamos o servidor de integração contínua para testar que toda mudança de estado deve produzir eventos.

## Por que as funções de aptidão ajudam as decisões

Medições objetivas: as funções de aptidão passam ou falham, então o trabalho fica visível e claro.

Uso contínuo: as funções de aptidão são suas regras vivas, executadas a cada commit e build.

Confiança para refatorar: as funções de aptidão detectam automaticamente erros nas regras de decisão.

Governança escalável: as funções de aptidão asseguram padrões sem criar gargalos.

## As funções de aptidão podem usar IA?

As funções de aptidão podem aproveitar LLMs de IA para decisões, fazendo perguntas sobre o seu trabalho,
como seus planos, código, esquemas, APIs e mais:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Teste unitário de arquitetura

[ArchUnit](https://www.archunit.org/): verifique regras de arquitetura de código Java usando qualquer framework de teste unitário Java comum.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): verifique regras de arquitetura de código TypeScript e JavaScript usando Jest, Vitest, Jasmine etc.
