# Modelo de registro de decisão para decisões técnicas importantes (ITDs)

Este é o modelo de Decisões Técnicas Importantes (ITD) descrito em
[ITDs: a lean ADR for executive technical decision-making at scale - Ignacio Larrañaga](https://ignaciolarranaga.medium.com/itds-a-lean-adr-for-executive-technical-decision-making-at-scale-e18bb3f6a563).

Os ITDs são uma evolução focada dos ADRs, otimizada para velocidade, clareza e
validação executiva. Enquanto um ADR documenta o que foi decidido, um ITD é um
artefato enxuto, centrado primeiro na decisão, que torna a própria decisão revisável, de modo que
as partes interessadas possam examiná-la rapidamente e questioná-la com facilidade. Os ITDs são adequados
a decisões técnicas que não são estritamente arquiteturais, como escolher
um modelo, uma biblioteca ou uma estratégia de CI/CD.

Em cada arquivo de ITD, escreva estas seções:

# Título

Declare a própria decisão, não uma descrição do tema.
Por exemplo, “Usar o Qwen2.5 1.5B Instruct para tradução no dispositivo”.

## O problema

Uma frase declarando o que estamos tentando resolver.

## Opções consideradas

As alternativas que estavam em pauta, com a opção selecionada em **negrito**.

## Justificativa

Apenas os fatores decisivos que levaram à escolha, não uma lista exaustiva de
todos os prós e contras.

## Notas

Opcional. Qualquer contexto adicional que valha a pena registrar, como restrições,
premissas ou links.
