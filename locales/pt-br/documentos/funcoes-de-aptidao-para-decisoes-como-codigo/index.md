# Funções de aptidão para decisões como código

Funções de aptidão são verificações automatizadas objetivas, escritas com código de programação, que verificam se as decisões estão sendo mantidas.

- Funções de aptidão tornam as decisões testáveis e asseguráveis.

- Funções de aptidão para decisões podem ajudar muito a garantia de qualidade, processos regulatórios e objetivos de governança.

## Como funções de aptidão se conectam às decisões

Um registro de decisão documenta a decisão, enquanto uma função de aptidão assegura a decisão.

- Exemplo de decisão: usamos event sourcing para requisitos de auditoria.

- Exemplo de função de aptidão: usamos o servidor de integração contínua para testar que todas as mudanças de estado devem produzir eventos.

## Por que funções de aptidão ajudam decisões

Medições objetivas: funções de aptidão passam ou falham, portanto o trabalho é visível e claro.

Uso contínuo: funções de aptidão são suas regras vivas, executadas em cada commit e build.

Confiança para refatorar: funções de aptidão capturam automaticamente erros em regras de decisão.

Governança escalável: funções de aptidão asseguram padrões sem criar gargalos.

## Funções de aptidão podem usar IA?

Funções de aptidão podem aproveitar LLMs de IA para decisões fazendo perguntas sobre seu trabalho,
como seus planos, código, schemas, APIs e mais:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Testes unitários de arquitetura

[ArchUnit](https://www.archunit.org/): verifica regras de arquitetura de código Java usando qualquer framework simples de testes unitários em Java.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): verifica regras de arquitetura de código TypeScript e código JavaScript usando Jest, Vitest, Jasmine etc.
