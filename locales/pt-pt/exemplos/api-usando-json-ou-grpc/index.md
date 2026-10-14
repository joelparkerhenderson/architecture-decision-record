# Registro de decisão de arquitetura: API usando JSON ou gRPC

## Estado

Aceito

## Contexto

Estamos projetando uma API para um novo serviço que será usado por vários clientes. Estamos considerando duas opções para implementar a API: usar JSON sobre HTTP ou usar gRPC.

JSON sobre HTTP é uma abordagem amplamente usada para construir APIs e é suportada por muitas linguagens de programação e frameworks. Essa abordagem é simples, leve e fácil de entender, o que a torna uma boa escolha para muitos projetos. No entanto, ela pode ser menos eficiente do que outras opções, especialmente ao lidar com grandes quantidades de dados.

O gRPC, por outro lado, é uma tecnologia mais nova que oferece uma forma mais eficiente de construir APIs. Ele usa serialização binária para transferir dados, o que pode ser mais rápido e compacto do que usar JSON. O gRPC também oferece suporte a streaming bidirecional, o que o torna uma boa escolha para aplicações em tempo real.

## Decisão

Após considerar os prós e os contras de ambas as opções, decidimos usar o gRPC para a nossa API. Embora JSON sobre HTTP seja uma opção mais simples, acreditamos que o gRPC fornecerá uma solução mais eficiente e escalável para o nosso serviço. Também prevemos que a nossa API tratará uma grande quantidade de dados, e a serialização binária do gRPC será mais eficiente para esse caso de uso.

Além disso, acreditamos que o suporte do gRPC a streaming bidirecional será benéfico para aplicações em tempo real que possamos desenvolver no futuro.

## Consequências

Ao escolher o gRPC, precisaremos usar um conjunto diferente de ferramentas e bibliotecas para construir a nossa API em comparação com o uso de JSON sobre HTTP. Isso pode exigir tempo e esforço adicionais para aprender e implementar essas tecnologias. Além disso, os clientes que quiserem usar a nossa API precisarão usar bibliotecas compatíveis com gRPC, que podem não ser tão amplamente suportadas quanto as bibliotecas de JSON sobre HTTP.

No entanto, acreditamos que os benefícios de usar o gRPC superam essas possíveis desvantagens, e estamos confiantes de que essa decisão resultará em uma API mais eficiente e escalável.
