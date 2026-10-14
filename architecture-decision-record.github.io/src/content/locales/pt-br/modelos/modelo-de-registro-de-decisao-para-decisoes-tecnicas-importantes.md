# Modelo de registro de decisão para Decisões Técnicas Importantes (ITDs)

Este é o modelo de Decisões Técnicas Importantes (ITD) descrito em
[ITDs: a lean ADR for executive technical decision-making at scale - Ignacio Larrañaga](https://ignaciolarranaga.medium.com/itds-a-lean-adr-for-executive-technical-decision-making-at-scale-e18bb3f6a563).

ITDs são uma evolução focada das ADRs, otimizadas para velocidade, clareza e
validação executiva. Enquanto uma ADR documenta o que foi decidido, uma ITD é um
artefato enxuto, orientado primeiro à decisão, que torna a própria decisão
revisável, para que as partes interessadas possam examiná-la rapidamente e
questioná-la com facilidade. ITDs são adequadas para decisões técnicas que não
são estritamente arquiteturais, como escolher um modelo, uma biblioteca ou uma
estratégia de CI/CD.

Em cada arquivo de ITD, escreva estas seções:

# Título

Declare a decisão em si, não uma descrição do tópico.
Por exemplo, "Usar Qwen2.5 1.5B Instruct para tradução no dispositivo".

## O problema

Uma frase declarando o que estamos tentando resolver.

## Opções consideradas

As alternativas que estavam na mesa, com a opção selecionada em **negrito**.

## Justificativa

Somente os fatores decisivos que levaram à escolha, não uma lista exaustiva de
todos os prós e contras.

## Notas

Opcional. Qualquer contexto adicional que valha registrar, como restrições,
premissas ou links.
