# Registro de decisão de arquitetura: editores de código de programação

## Contexto

Editores de código de programação são uma ferramenta essencial para desenvolvedores escreverem e editarem código. Existem numerosos editores de código disponíveis, cada um com seu próprio conjunto de recursos, vantagens e desvantagens. O propósito desta ADR é documentar as decisões de arquitetura tomadas para editores de código de programação.

## Prioridades

A arquitetura para editores de código de programação deve priorizar o seguinte:

* **Modularidade**: O editor de código deve ser projetado de forma modular, permitindo que desenvolvedores o personalizem e estendam conforme necessário. Isso permite uma arquitetura flexível que pode se adaptar às necessidades de diferentes desenvolvedores e equipes.

* **Performance**: O editor de código deve ser performático e responsivo, permitindo que desenvolvedores trabalhem com eficiência sem serem desacelerados pela ferramenta que estão usando.

* **Interface de usuário**: A interface de usuário deve ser intuitiva e fácil de usar, permitindo que desenvolvedores foquem no código em vez de terem dificuldades com o editor.

* **Extensibilidade**: O editor de código deve ser projetado para permitir extensão fácil com plugins e integrações de terceiros.

* **Compatibilidade**: O editor de código deve ser compatível com uma ampla variedade de linguagens de programação e tecnologias, tornando-se uma ferramenta útil para um conjunto amplo de desenvolvedores.

## Decisão

Com base nessas prioridades, a arquitetura para editores de código de programação deve ser projetada com os seguintes componentes:

* **Core**: Este componente fornece a funcionalidade básica do editor de código, como realce de sintaxe, edição de texto e gerenciamento de arquivos.

* **UI**: Este componente fornece a interface de usuário para o editor de código, incluindo menus, barras de ferramentas e atalhos de teclado.

* **Plugins**: Este componente permite que desenvolvedores estendam a funcionalidade do editor de código instalando plugins de terceiros. Plugins podem fornecer recursos adicionais, como autocompletar código, linting ou depuração.

* **Integrações**: Este componente permite que o editor de código se integre a outras ferramentas e tecnologias, como sistemas de controle de versão, sistemas de build ou ferramentas de depuração.

## Justificativa

A modularidade do editor de código permite que desenvolvedores o personalizem e estendam conforme necessário. Isso é importante porque diferentes desenvolvedores e equipes têm necessidades e fluxos de trabalho diferentes, e uma arquitetura flexível pode acomodar essas diferenças.

* **Performance**: crucial porque desenvolvedores precisam conseguir trabalhar com eficiência sem serem desacelerados por suas ferramentas. Um editor de código performático é essencial para a produtividade e pode ajudar desenvolvedores a manter foco e concentração.

* **UI**: importante porque permite que desenvolvedores foquem no código em vez de terem dificuldades com o editor. Isso pode levar a melhor produtividade e menos frustração para desenvolvedores.

* **Extensibilidade**: poderosa porque permite que o editor de código seja adaptado a diferentes necessidades e fluxos de trabalho. Plugins e integrações de terceiros podem fornecer recursos e capacidades adicionais que não estão incluídos no editor core.

* **Compatibilidade**: valiosa porque permite que o editor de código seja usado com uma ampla variedade de linguagens de programação e tecnologias. Isso torna o editor uma ferramenta mais útil para um conjunto amplo de desenvolvedores.

Os componentes core, plugins, integrações e UI fornecem uma separação clara de responsabilidades e permitem uma arquitetura modular que pode ser facilmente estendida e personalizada. Essa arquitetura é flexível, performática e compatível com uma ampla variedade de linguagens de programação e tecnologias, tornando-se uma ferramenta útil para desenvolvedores.
