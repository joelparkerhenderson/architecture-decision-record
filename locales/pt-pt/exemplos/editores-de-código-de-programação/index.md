# Registro de decisão de arquitetura: editores de código de programação

## Contexto

Os editores de código de programação são uma ferramenta essencial para os desenvolvedores escreverem e editarem código. Há inúmeros editores de código disponíveis, cada um com seu próprio conjunto de recursos, vantagens e desvantagens. O objetivo deste ADR é documentar as decisões de arquitetura tomadas para editores de código de programação.

## Prioridades

A arquitetura dos editores de código de programação deve priorizar o seguinte:

* **Modularidade**: o editor de código deve ser projetado de forma modular, permitindo que os desenvolvedores o personalizem e estendam conforme necessário. Isso possibilita uma arquitetura flexível que pode se adaptar às necessidades de diferentes desenvolvedores e equipes.

* **Desempenho**: o editor de código deve ter bom desempenho e ser responsivo, permitindo que os desenvolvedores trabalhem com eficiência sem serem atrasados pela ferramenta que estão usando.

* **Interface do usuário**: a interface do usuário deve ser intuitiva e fácil de usar, permitindo que os desenvolvedores se concentrem em seu código em vez de lutar com o editor.

* **Extensibilidade**: o editor de código deve ser projetado para permitir fácil extensão com plugins e integrações de terceiros.

* **Compatibilidade**: o editor de código deve ser compatível com uma ampla gama de linguagens de programação e tecnologias, tornando-o uma ferramenta útil para um amplo conjunto de desenvolvedores.

## Decisão

Com base nessas prioridades, a arquitetura dos editores de código de programação deve ser projetada com os seguintes componentes:

* **Núcleo**: este componente fornece a funcionalidade básica do editor de código, como realce de sintaxe, edição de texto e gerenciamento de arquivos.

* **UI**: este componente fornece a interface do usuário do editor de código, incluindo menus, barras de ferramentas e atalhos de teclado.

* **Plugins**: este componente permite que os desenvolvedores estendam a funcionalidade do editor de código instalando plugins de terceiros. Os plugins podem fornecer recursos adicionais, como autocompletar código, linting ou depuração.

* **Integrações**: este componente permite que o editor de código se integre a outras ferramentas e tecnologias, como sistemas de controle de versão, sistemas de build ou ferramentas de depuração.

## Justificativa

A modularidade do editor de código permite que os desenvolvedores o personalizem e estendam conforme necessário. Isso é importante porque diferentes desenvolvedores e equipes têm necessidades e fluxos de trabalho diferentes, e uma arquitetura flexível pode acomodar essas diferenças.

* **Desempenho**: crucial porque os desenvolvedores precisam trabalhar com eficiência sem serem atrasados por suas ferramentas. Um editor de código com bom desempenho é essencial para a produtividade e pode ajudar os desenvolvedores a manter o foco e a concentração.

* **UI**: importante porque permite que os desenvolvedores se concentrem em seu código em vez de lutar com o editor. Isso pode levar a maior produtividade e menos frustração para os desenvolvedores.

* **Extensibilidade**: poderosa porque permite que o editor de código seja adaptado a diferentes necessidades e fluxos de trabalho. Plugins e integrações de terceiros podem fornecer recursos e capacidades adicionais que não estão incluídos no editor principal.

* **Compatibilidade**: valiosa porque permite que o editor de código seja usado com uma ampla gama de linguagens de programação e tecnologias. Isso torna o editor uma ferramenta mais útil para um amplo conjunto de desenvolvedores.

Os componentes de núcleo, plugins, integrações e UI proporcionam uma separação clara de responsabilidades e permitem uma arquitetura modular que pode ser facilmente estendida e personalizada. Essa arquitetura é flexível, tem bom desempenho e é compatível com uma ampla gama de linguagens de programação e tecnologias, tornando-a uma ferramenta útil para os desenvolvedores.
