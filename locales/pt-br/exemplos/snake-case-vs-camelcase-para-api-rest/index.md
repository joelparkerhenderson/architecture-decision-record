# Registro de decisão de arquitetura: snake_case v. camelCase para uma API REST?

Decisão: a convenção de nomenclatura snake_case será usada para endpoints de API REST

Status: Aceito

## Contexto

Em convenções de nomenclatura para APIs REST, há dois formatos populares: snake_case e camelCase. O formato snake_case é aquele em que cada palavra no nome é separada por underscores, enquanto camelCase é aquele em que a primeira palavra do nome fica em minúsculas e as palavras subsequentes têm a primeira letra em maiúscula. Esta decisão determinará qual convenção de nomenclatura deve ser usada para uma API REST.

## Direcionadores da decisão

- Consistência com convenções de nomenclatura existentes no projeto

- Legibilidade e clareza para qualquer pessoa que possa trabalhar na API

- Alinhamento com melhores práticas do setor para convenções de nomenclatura de APIs REST

- Facilidade de implementação e manutenção

## Decisão

A convenção de nomenclatura snake_case será usada para endpoints de API REST. Essa escolha é direcionada pelos seguintes fatores:

1. **Consistência**: O projeto já usa a convenção de nomenclatura snake_case para todos os endpoints, e seria benéfico manter essa convenção para garantir consistência em todo o projeto.

2. **Legibilidade e clareza**: A convenção snake_case é mais legível e fácil de entender. Os underscores fornecem uma separação clara entre palavras, facilitando analisar e entender o significado do nome.

3. **Alinhamento com melhores práticas do setor**: A convenção snake_case é amplamente usada no setor e é considerada uma melhor prática para APIs REST, tornando-se uma boa escolha para o projeto.

4. **Facilidade de implementação e manutenção**: Manter a convenção de nomenclatura existente é mais fácil de implementar e manter, pois todo o código e documentação existentes precisariam ser atualizados se uma nova convenção fosse escolhida.

## Consequências

Há consequências potenciais desta decisão.

* Se algum novo membro da equipe que entrar no projeto não estiver familiarizado com a convenção de nomenclatura snake_case, isso poderia levar a confusão e erros no desenvolvimento. Entretanto, como snake_case é uma convenção amplamente usada, esse risco é mínimo.

* Se outras ferramentas ou frameworks forem usados no projeto e forem fortemente baseados na convenção camelCase, pode ser necessário esforço adicional para converter entre convenções de nomenclatura. Entretanto, isso não é uma preocupação significativa, pois o projeto padronizou na convenção snake_case.

De modo geral, a decisão de usar a convenção de nomenclatura snake_case para endpoints de API REST resulta em uma abordagem consistente, legível e padrão do setor, além de ser fácil de implementar e manter.

<h6>Crédito: esta página é gerada pelo ChatGPT e depois editada para clareza e formato.</h6>
