# Critérios de sustentabilidade da decisão

<https://www.infoq.com/articles/sustainable-architectural-design-decisions/>

Para definir a sustentabilidade da decisão em detalhes, derivamos cinco critérios principais.

## Estratégico

Durante a tomada de decisão, alguém que analisa consequências estratégicas deve considerar fatores como o impacto de longo prazo das decisões, por exemplo, operações futuras e esforço de manutenção.

## Mensurável e gerenciável

Você pode medir e avaliar o resultado de uma decisão ao longo do tempo de acordo com critérios objetivos, idealmente numéricos (como, por exemplo, os propagados por cenários de atributos de qualidade e workshops4). Capturar todas as decisões granulares não é possível, portanto arquitetos devem limitar a granularidade das decisões a certo nível de detalhe (como criar uma classe de design). Isso levará a um conjunto de decisões mais sustentável e a menos links de rastreabilidade. Além disso, limitar o número de dependências entre decisões reduz o efeito cascata das mudanças.

## Alcançável e realista

A justificativa para ajustar a solução ao problema deve ser escolhida pragmaticamente e explicitada. Por exemplo, arquitetos podem indicar que tomaram cuidado para evitar overengineering ou underengineering (isto é, devem aplicar a abordagem "boa o suficiente").

## Enraizado em requisitos

A tomada de decisão deve ser fundamentada em experiência e contexto de arquitetura específicos do domínio. Ela deve levar em conta o ambiente da empresa, bem como requisitos e restrições do projeto, incluindo as habilidades atuais da equipe de desenvolvimento, o orçamento de treinamento e o processo.

## Atemporal

As decisões devem se basear em experiência e conhecimento que provavelmente não ficarão desatualizados em breve. Por exemplo, arquitetos podem escolher padrões ou táticas de arquitetura neutros em relação à plataforma.
