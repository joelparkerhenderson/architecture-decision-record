# Registro de decisão de arquitetura: escolhendo uma tecnologia de banco de dados

## Estado

Aceito

## Contexto

Estamos projetando uma nova aplicação que exige armazenar e recuperar dados de forma escalável e com bom desempenho. Identificamos três tipos de tecnologias de banco de dados comumente usadas: bancos de dados relacionais, bancos de dados de documentos e bancos de dados de eventos.

Os bancos de dados relacionais armazenam dados em tabelas com esquemas fixos e impõem restrições rígidas de integridade de dados. São adequados para aplicações que exigem relacionamentos de dados complexos e transações. Exemplos incluem MySQL, PostgreSQL e Oracle.

Os bancos de dados de documentos armazenam dados em documentos semelhantes a JSON e não têm esquema. São bem adequados para aplicações que exigem modelos de dados flexíveis e escalabilidade horizontal. Exemplos incluem MongoDB, Couchbase e Amazon DynamoDB.

Os bancos de dados de eventos armazenam dados como uma série de eventos, capturando cada mudança nos dados. São adequados para aplicações que exigem auditoria, event sourcing e processamento de dados complexo. Exemplos incluem Apache Kafka, Apache Pulsar e AWS Kinesis.

## Decisão

Após avaliar cuidadosamente os requisitos e as restrições da nossa aplicação, decidimos usar um banco de dados de documentos.

## Justificativa

Escolhemos um banco de dados de documentos porque:

1. Nossa aplicação exige um modelo de dados flexível que possa evoluir com o tempo. Os bancos de dados de documentos nos permitem armazenar dados em um formato sem esquema, o que significa que podemos adicionar novos campos ou alterar a estrutura de documentos existentes sem precisar modificar o esquema do banco de dados.

2. Nossa aplicação precisa escalar horizontalmente para lidar com grandes volumes de dados e tráfego. Os bancos de dados de documentos oferecem suporte integrado a sharding e replicação, o que nos permite distribuir dados por vários servidores e lidar com alta vazão de leitura e escrita.

3. Nossa aplicação exige recuperação de dados rápida e eficiente. Os bancos de dados de documentos oferecem poderosos recursos de indexação e consulta que nos permitem recuperar dados de forma rápida e eficiente.

4. Nossa aplicação não exige transações complexas nem relacionamentos de dados. Embora os bancos de dados relacionais se destaquem em impor restrições de integridade de dados e lidar com transações complexas, nossa aplicação não tem esses requisitos. Os bancos de dados de documentos podem fornecer garantias suficientes de consistência e durabilidade para o nosso caso de uso.

## Consequências

Ao escolher um banco de dados de documentos, precisaremos investir em aprender e entender a tecnologia específica que escolhermos usar. Além disso, precisaremos garantir que o modelo de dados da nossa aplicação se ajuste bem ao modelo de dados do banco de dados de documentos, para maximizar o desempenho e a escalabilidade.

No entanto, acreditamos que os benefícios de usar um banco de dados de documentos superam os custos e que ele é a melhor opção para os requisitos e as restrições da nossa aplicação.
