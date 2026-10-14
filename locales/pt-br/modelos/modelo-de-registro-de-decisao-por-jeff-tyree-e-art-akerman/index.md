# Modelo de registro de decisão por Jeff Tyree e Art Akerman

Este é o modelo de descrição de decisão de arquitetura publicado em ["Architecture Decisions: Demystifying Architecture" por Jeff Tyree e Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Questão**: Descreva a questão de design de arquitetura que você está abordando, sem deixar dúvidas sobre por que você está abordando esta questão agora. Seguindo uma abordagem minimalista, aborde e documente apenas as questões que precisam ser tratadas em vários pontos do ciclo de vida.

* **Decisão**: Declare claramente a direção da arquitetura, ou seja, a posição que você selecionou.

* **Status**: O status da decisão, como pendente, decidida ou aprovada.

* **Grupo**: Você pode usar um agrupamento simples, como integração, apresentação, dados e assim por diante, para ajudar a organizar o conjunto de decisões. Você também poderia usar uma ontologia de arquitetura mais sofisticada, como a de John Kyaruzi e Jan van Katwijk, que inclui categorias mais abstratas, como evento, calendário e localização. Por exemplo, usando essa ontologia, você agruparia sob evento as decisões que lidam com ocorrências em que o sistema exige informações.

* **Premissas**: Descreva claramente as premissas subjacentes no ambiente em que você está tomando a decisão: custo, cronograma, tecnologia e assim por diante. Observe que restrições ambientais (como padrões de tecnologia aceitos, arquitetura corporativa, padrões comumente empregados e assim por diante) podem limitar as alternativas que você considera.

* **Restrições**: Capture quaisquer restrições adicionais ao ambiente que a alternativa escolhida (a decisão) possa impor.

* **Posições**: Liste as posições (opções ou alternativas viáveis) que você considerou. Elas frequentemente exigem explicações longas, às vezes até modelos e diagramas. Esta não é uma lista exaustiva. No entanto, você não quer ouvir a pergunta "Você pensou em...?" durante uma revisão final; isso leva à perda de credibilidade e ao questionamento de outras decisões de arquitetura. Esta seção também ajuda a assegurar que você ouviu as opiniões de outras pessoas; declarar explicitamente outras opiniões ajuda a envolver seus defensores na sua decisão.

* **Argumento**: Esboce por que você selecionou uma posição, incluindo itens como custo de implementação, custo total de propriedade, time to market e disponibilidade dos recursos de desenvolvimento necessários. Isto provavelmente é tão importante quanto a decisão em si.

* **Implicações**: Uma decisão vem com muitas implicações, como denota o metamodelo REMAP. Por exemplo, uma decisão pode introduzir a necessidade de tomar outras decisões, criar novos requisitos ou modificar requisitos existentes; impor restrições adicionais ao ambiente; exigir renegociação de escopo ou cronograma com clientes; ou exigir treinamento adicional da equipe. Entender e declarar claramente as implicações da sua decisão pode ser muito eficaz para obter adesão e criar um roadmap para a execução da arquitetura.

* **Decisões relacionadas**: É óbvio que muitas decisões são relacionadas; você pode listá-las aqui. No entanto, constatamos que, na prática, uma matriz de rastreabilidade, árvores de decisão ou metamodelos são mais úteis. Metamodelos são úteis para mostrar relacionamentos complexos de forma diagramática (como modelos Rose).

* **Requisitos relacionados**: Decisões devem ser orientadas pelo negócio. Para mostrar responsabilização, mapeie explicitamente suas decisões aos objetivos ou requisitos. Você pode enumerar estes requisitos relacionados aqui, mas constatamos que é mais conveniente referenciar uma matriz de rastreabilidade. Você pode avaliar a contribuição de cada decisão de arquitetura para atender a cada requisito e, em seguida, avaliar quão bem o requisito é atendido em todas as decisões. Se uma decisão não contribui para atender a um requisito, não tome essa decisão.

* **Artefatos relacionados**: Liste os documentos relacionados de arquitetura, design ou escopo que esta decisão impacta.

* **Princípios relacionados**: Se a empresa tiver um conjunto acordado de princípios, assegure-se de que a decisão seja consistente com um ou mais deles. Isso ajuda a assegurar alinhamento entre domínios ou sistemas.

* **Notas**: Como o processo de tomada de decisão pode levar semanas, constatamos que é útil capturar notas e questões que a equipe discute durante o processo de socialização.
