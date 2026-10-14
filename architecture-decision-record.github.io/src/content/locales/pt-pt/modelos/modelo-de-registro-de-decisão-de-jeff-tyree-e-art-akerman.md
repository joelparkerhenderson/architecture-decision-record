# Modelo de registro de decisão de Jeff Tyree e Art Akerman

Este é o modelo de descrição de decisão de arquitetura publicado em ["Architecture Decisions: Demystifying Architecture" by Jeff Tyree and Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Questão (Issue)**: descreva a questão de design de arquitetura que você está abordando, sem deixar dúvidas sobre por que está abordando essa questão agora. Seguindo uma abordagem minimalista, aborde e documente apenas as questões que precisam ser tratadas em vários pontos do ciclo de vida.

* **Decisão (Decision)**: declare claramente a direção da arquitetura, ou seja, a posição que você selecionou.

* **Estado (Status)**: o estado da decisão, como pending, decided ou approved.

* **Grupo (Group)**: você pode usar um agrupamento simples, como integração, apresentação, dados e assim por diante, para ajudar a organizar o conjunto de decisões. Também pode usar uma ontologia de arquitetura mais sofisticada, como a de John Kyaruzi e Jan van Katwijk, que inclui categorias mais abstratas como evento, calendário e local. Por exemplo, usando essa ontologia, você agruparia sob evento as decisões que tratam de ocorrências em que o sistema requer informações.

* **Premissas (Assumptions)**: descreva claramente as premissas subjacentes do ambiente em que você está tomando a decisão — custo, cronograma, tecnologia e assim por diante. Observe que restrições ambientais (como padrões tecnológicos aceitos, arquitetura corporativa, padrões comumente empregados e assim por diante) podem limitar as alternativas que você considera.

* **Restrições (Constraints)**: capture quaisquer restrições adicionais ao ambiente que a alternativa escolhida (a decisão) possa impor.

* **Posições (Positions)**: liste as posições (opções ou alternativas viáveis) que você considerou. Muitas vezes exigem longas explicações, às vezes até modelos e diagramas. Esta não é uma lista exaustiva. No entanto, você não quer ouvir a pergunta “Você pensou em...?” durante uma revisão final; isso leva à perda de credibilidade e ao questionamento de outras decisões de arquitetura. Esta seção também ajuda a garantir que você ouviu as opiniões dos outros; declarar explicitamente outras opiniões ajuda a engajar seus defensores na sua decisão.

* **Argumento (Argument)**: descreva por que você selecionou uma posição, incluindo itens como custo de implementação, custo total de propriedade, tempo de chegada ao mercado e disponibilidade dos recursos de desenvolvimento necessários. Isso provavelmente é tão importante quanto a própria decisão.

* **Implicações (Implications)**: uma decisão vem com muitas implicações, como denota o metamodelo REMAP. Por exemplo, uma decisão pode criar a necessidade de tomar outras decisões, criar novos requisitos ou modificar requisitos existentes; impor restrições adicionais ao ambiente; exigir renegociar escopo ou cronograma com clientes; ou exigir treinamento adicional da equipe. Compreender e declarar claramente as implicações da sua decisão pode ser muito eficaz para obter adesão e criar um roteiro para a execução da arquitetura.

* **Decisões relacionadas (Related decisions)**: é óbvio que muitas decisões são relacionadas; você pode listá-las aqui. No entanto, descobrimos que, na prática, uma matriz de rastreabilidade, árvores de decisão ou metamodelos são mais úteis. Metamodelos são úteis para mostrar relações complexas de forma diagramática (como modelos Rose).

* **Requisitos relacionados (Related requirements)**: as decisões devem ser orientadas pelo negócio. Para mostrar responsabilização, mapeie explicitamente suas decisões para os objetivos ou requisitos. Você pode enumerar esses requisitos relacionados aqui, mas achamos mais conveniente referenciar uma matriz de rastreabilidade. Você pode avaliar a contribuição de cada decisão de arquitetura para atender a cada requisito e, em seguida, avaliar quão bem o requisito é atendido em todas as decisões. Se uma decisão não contribui para atender a um requisito, não tome essa decisão.

* **Artefatos relacionados (Related artifacts)**: liste os documentos de arquitetura, design ou escopo relacionados que esta decisão impacta.

* **Princípios relacionados (Related principles)**: se a empresa tem um conjunto acordado de princípios, certifique-se de que a decisão seja consistente com um ou mais deles. Isso ajuda a garantir alinhamento entre domínios ou sistemas.

* **Notas (Notes)**: como o processo de tomada de decisão pode levar semanas, achamos útil capturar notas e questões que a equipe discute durante o processo de socialização.
