# Registro de Decisão de Arquitetura: API usando JSON vs. gRPC

## Status

Aceito

## Contexto

Estamos projetando uma API para um novo serviço que será usado por múltiplos clientes. Consideramos duas opções para implementar a API: usar JSON sobre HTTP ou usar gRPC.

JSON sobre HTTP é uma abordagem amplamente usada para criar APIs e é suportada por muitas linguagens de programação e frameworks. Essa abordagem é simples, leve e fácil de entender, o que a torna uma boa escolha para muitos projetos. No entanto, ela pode ser menos eficiente do que outras opções, especialmente quando se trata de lidar com grandes quantidades de dados.

gRPC, por outro lado, é uma tecnologia mais nova que oferece uma forma mais eficiente de criar APIs. Ele usa serialização binária para transferir dados, que pode ser mais rápida e mais compacta do que usar JSON. gRPC também suporta streaming bidirecional, tornando-o uma boa escolha para aplicações em tempo real.

## Decisão

Depois de considerar os prós e contras de ambas as opções, decidimos usar gRPC para nossa API. Embora JSON sobre HTTP seja uma opção mais simples, acreditamos que gRPC fornecerá uma solução mais eficiente e escalável para nosso serviço. Também prevemos que nossa API lidará com uma grande quantidade de dados, e a serialização binária do gRPC será mais eficiente para este caso de uso.

Além disso, acreditamos que o suporte do gRPC a streaming bidirecional será benéfico para aplicações em tempo real que possamos desenvolver no futuro.

## Consequências

Ao escolher gRPC, precisaremos usar um conjunto diferente de ferramentas e bibliotecas para criar nossa API em comparação com o uso de JSON sobre HTTP. Isso pode exigir tempo e esforço adicionais para aprender e implementar essas tecnologias. Além disso, clientes que queiram usar nossa API precisarão usar bibliotecas compatíveis com gRPC, que podem não ter suporte tão amplo quanto bibliotecas JSON sobre HTTP.

No entanto, acreditamos que os benefícios de usar gRPC superam essas possíveis desvantagens, e estamos confiantes de que esta decisão resultará em uma API mais eficiente e escalável.
