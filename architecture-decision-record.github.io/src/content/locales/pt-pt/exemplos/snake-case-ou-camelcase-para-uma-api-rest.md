# Registro de decisão de arquitetura: snake_case ou camelCase para uma API REST?

Decisão: a convenção de nomenclatura snake_case será usada para os endpoints da API REST

Estado: aceito

## Contexto

Nas convenções de nomenclatura para APIs REST, há dois formatos populares: snake_case e camelCase. No formato snake_case, cada palavra do nome é separada por sublinhados, enquanto no camelCase a primeira palavra do nome fica em minúsculas e as palavras seguintes têm a primeira letra maiúscula. Esta decisão determinará qual convenção de nomenclatura deve ser usada para uma API REST.

## Fatores da decisão

- Consistência com as convenções de nomenclatura existentes no projeto

- Legibilidade e clareza para qualquer pessoa que possa trabalhar na API

- Alinhamento com as melhores práticas do setor para convenções de nomenclatura de APIs REST

- Facilidade de implementação e manutenção

## Decisão

A convenção de nomenclatura snake_case será usada para os endpoints da API REST. Essa escolha é motivada pelos seguintes fatores:

1. **Consistência**: o projeto já usa a convenção de nomenclatura snake_case para todos os endpoints, e seria benéfico manter essa convenção para garantir consistência em todo o projeto.

2. **Legibilidade e clareza**: a convenção snake_case é mais legível e fácil de entender. Os sublinhados fornecem uma separação clara entre as palavras, facilitando a análise e a compreensão do significado do nome.

3. **Alinhamento com as melhores práticas do setor**: a convenção snake_case é amplamente usada no setor e é considerada uma boa prática para APIs REST, o que a torna uma boa escolha para o projeto.

4. **Facilidade de implementação e manutenção**: manter a convenção de nomenclatura existente é mais fácil de implementar e manter, já que todo o código e a documentação existentes precisariam ser atualizados se uma nova convenção fosse escolhida.

## Consequências

Há consequências potenciais desta decisão. 

* Se novos membros da equipe que ingressarem no projeto não estiverem familiarizados com a convenção de nomenclatura snake_case, isso pode levar a confusão e erros no desenvolvimento. No entanto, como o snake_case é uma convenção amplamente usada, esse risco é mínimo. 
  
* Se outras ferramentas ou frameworks forem usados no projeto e se baseiarem fortemente na convenção camelCase, pode ser necessário esforço extra para converter entre as convenções de nomenclatura. No entanto, isso não é uma preocupação significativa, pois o projeto padronizou a convenção snake_case. 
 
No geral, a decisão de usar a convenção de nomenclatura snake_case para os endpoints da API REST resulta em uma abordagem consistente, legível e alinhada aos padrões do setor, além de ser fácil de implementar e manter.

<h6>Crédito: esta página foi gerada pelo ChatGPT e depois editada quanto à clareza e ao formato.</h6>
