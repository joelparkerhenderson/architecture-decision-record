# Registro de decisão de arquitetura (ADR) para componentes Svelte

<!--

Prompt:

Architecture decision record for Svelte components.

Compare options: SVAR, Carbon, Flowbite, SkeletonUI, MeltUI, SvelteUI, shadcn-svelte

The goal is full features for table, charts, lists, grids, gantt, 

-->

## Contexto

Estamos selecionando uma biblioteca de componentes de UI Svelte que ofereça recursos completos para:
- **Tabelas**
- **Gráficos**
- **Listas**
- **Grades**
- **Gráficos de Gantt**

O objetivo é escolher uma biblioteca que equilibre facilidade de integração, suporte completo a recursos, desempenho e manutenibilidade de longo prazo. As opções em consideração são:

1. **SVAR**
2. **Carbon**
3. **Flowbite**
4. **SkeletonUI**
5. **MeltUI**
6. **SvelteUI**
7. **shadcn-svelte**

## Análise das opções

### 1. **SVAR**
- **Visão geral**: o SVAR é uma biblioteca de componentes moderna e rica em recursos para Svelte, com foco em sistemas de design e componentes prontos para o ambiente corporativo.
- **Prós**:
  - Componentes completos em recursos, incluindo tabelas, formulários e gráficos.
  - Altas opções de personalização com suporte integrado a temas.
  - Suporte integrado a acessibilidade e responsividade.
  - Bem documentado, com contribuições da comunidade.
- **Contras**:
  - Pode ser mais pesado em comparação com outras bibliotecas mais simples.
  - Suporte limitado a componentes específicos, como gráficos de Gantt e grades avançadas.
- **Melhor para**: aplicações de nível corporativo em que um sistema de design completo em recursos é necessário.
- **Suporte a tabelas/gráficos**: moderado a bom.
- **Suporte a grades/Gantt**: mínimo.

### 2. **Carbon**
- **Visão geral**: o Carbon Design System é um sistema de design de código aberto da IBM, que oferece um conjunto robusto de componentes de UI.
- **Prós**:
  - Design polido e de alta qualidade, com documentação extensa.
  - Muito acessível e responsivo.
  - Grande biblioteca de componentes, incluindo grades, tabelas e controles de formulário.
- **Contras**:
  - Não é focado em Svelte, então a integração pode ser trabalhosa.
  - Pode exigir personalização adicional para compatibilidade total com o Svelte.
  - Sem suporte pronto para componentes avançados, como gráficos de Gantt ou gráficos complexos.
- **Melhor para**: projetos de grande escala que exigem uma UI consistente e polida.
- **Suporte a tabelas/gráficos**: bom (com integrações de bibliotecas de gráficos).
- **Suporte a grades/Gantt**: bom (suporte a grades disponível, mas sem gráficos de Gantt).

### 3. **Flowbite**
- **Visão geral**: o Flowbite é uma biblioteca de componentes construída com Tailwind CSS, que oferece vários componentes e elementos de UI.
- **Prós**:
  - Baseado em Tailwind CSS, o que facilita a personalização.
  - Fácil de integrar e usar com o Svelte.
  - Fornece componentes ricos, como tabelas, gráficos e controles de UI.
- **Contras**:
  - Carece de recursos avançados (p. ex., gráficos de Gantt ou grades complexas).
  - Não tem componentes de gráficos nativos; depende de bibliotecas externas.
- **Melhor para**: projetos que exigem desenvolvimento rápido com foco na integração com Tailwind CSS.
- **Suporte a tabelas/gráficos**: bom (requer integração com bibliotecas de gráficos de terceiros).
- **Suporte a grades/Gantt**: mínimo.

### 4. **SkeletonUI**
- **Visão geral**: o SkeletonUI é uma biblioteca de componentes leve para Svelte, com foco em simplicidade e minimalismo.
- **Prós**:
  - Extremamente leve e rápida.
  - API simples e intuitiva.
  - Boa para projetos pequenos ou em que o desempenho é crítico.
- **Contras**:
  - Poucos componentes estão incluídos, então não é rica em recursos.
  - Carece de componentes avançados de tabela/grade/gráfico/Gantt.
  - Apoio limitado da comunidade e documentação menos abrangente.
- **Melhor para**: projetos que exigem componentes leves com sobrecarga mínima.
- **Suporte a tabelas/gráficos**: mínimo.
- **Suporte a grades/Gantt**: mínimo.

### 5. **MeltUI**
- **Visão geral**: o MeltUI é uma coleção de componentes de UI acessíveis para Svelte, com foco em simplicidade e composabilidade.
- **Prós**:
  - Leve e totalmente personalizável.
  - Bons recursos de acessibilidade prontos para uso.
  - Design moderno e minimalista.
- **Contras**:
  - Menos rica em recursos em comparação com outras bibliotecas.
  - Carece de componentes avançados de grade e tabela.
  - Sem gráficos de Gantt nem opções de gráficos complexos.
- **Melhor para**: designs minimalistas que priorizam acessibilidade e desempenho.
- **Suporte a tabelas/gráficos**: mínimo.
- **Suporte a grades/Gantt**: mínimo.

### 6. **SvelteUI**
- **Visão geral**: o SvelteUI é uma biblioteca de componentes de UI abrangente e personalizável para Svelte, projetada para construir apps web modernos com uma UI elegante.
- **Prós**:
  - Conjunto abrangente de componentes, incluindo tabelas, grades, gráficos e formulários.
  - Oferece suporte aos modos claro e escuro.
  - Altamente personalizável e fácil de estender.
  - Integrações integradas para bibliotecas de gráficos como `chart.js` ou `d3.js`.
- **Contras**:
  - Pode ser mais pesada que bibliotecas de componentes mais simples.
  - Requer alguma configuração para integrar bibliotecas externas para recursos mais complexos, como gráficos de Gantt.
- **Melhor para**: projetos que precisam de um conjunto abrangente e personalizável de componentes.
- **Suporte a tabelas/gráficos**: excelente (bibliotecas de gráficos suportadas).
- **Suporte a grades/Gantt**: bom (componentes de grade disponíveis; o Gantt precisa de integração externa).

### 7. **shadcn-svelte**
- **Visão geral**: uma versão Svelte do ShadCN, que se concentra em design utility-first e fornece componentes modernos e estilizados.
- **Prós**:
  - Design utility-first, construído sobre o Tailwind CSS, o que facilita a personalização.
  - Rico conjunto de componentes, totalmente estilizados e prontos para uso.
  - Fácil de integrar com outras bibliotecas.
- **Contras**:
  - Não é tão completa em recursos quanto algumas outras em termos de elementos de UI avançados.
  - Carece de suporte integrado para tabelas, gráficos ou grades.
  - Sem suporte pronto para gráficos de Gantt.
- **Melhor para**: projetos pequenos a médios que exigem uma abordagem utility-first e personalizável.
- **Suporte a tabelas/gráficos**: mínimo.
- **Suporte a grades/Gantt**: mínimo.

## Decisão

### Opção recomendada: **SvelteUI**

- **Justificativa**: o SvelteUI oferece um conjunto completo e abrangente de componentes que atende à necessidade de tabelas, gráficos, grades e formulários. É altamente personalizável, integra-se bem com outras bibliotecas de gráficos (como `chart.js` e `d3.js`) e tem um bom equilíbrio entre desempenho leve e riqueza de recursos. Embora possa não oferecer suporte pronto a gráficos de Gantt, pode ser facilmente estendido com integrações de terceiros, o que o torna ideal para uma solução completa em recursos e escalável.
  
  - **Prós**:
    - Excelente suporte a tabelas e gráficos.
    - Componentes completos de grade e layout.
    - Personalizável e integra-se bem com bibliotecas de gráficos externas.
    - Boa comunidade e documentação.
  
  - **Contras**:
    - Mais pesado que algumas outras bibliotecas minimalistas.
    - Precisa de integração externa para gráficos complexos, como gráficos de Gantt.
  
### Alternativa: **Flowbite** ou **Carbon** (para projetos corporativos maiores)
- Se um sistema de design polido, baseado em Tailwind ou mais consistente for necessário, o **Flowbite** (com Tailwind CSS) ou o **Carbon** (para soluções de nível corporativo) podem ser alternativas adequadas. No entanto, podem exigir esforço extra para integrações com gráficos e componentes mais complexos.

## Conclusão

A melhor opção para os seus requisitos (recursos completos para tabelas, gráficos, listas, grades, Gantt) é o **SvelteUI**, seguido por **Flowbite** e **Carbon**, dependendo das necessidades do projeto e das preferências de design.
