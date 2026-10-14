# Registro de Decisão de Arquitetura: Escolha de uma tecnologia de banco de dados

## Status

Aceito

## Contexto

Estamos projetando uma nova aplicação que requer armazenar e recuperar dados de maneira escalável e performática. Identificamos três tipos de tecnologias de banco de dados que são comumente usadas: bancos de dados relacionais, bancos de dados de documentos e bancos de dados de eventos.

Bancos de dados relacionais armazenam dados em tabelas com esquemas fixos e impõem restrições rígidas de integridade de dados. Eles são adequados para aplicações que exigem relacionamentos de dados complexos e transações. Exemplos incluem MySQL, PostgreSQL e Oracle.

Bancos de dados de documentos armazenam dados em documentos semelhantes a JSON e não têm esquema. Eles são bem adequados para aplicações que exigem modelos de dados flexíveis e escala horizontal. Exemplos incluem MongoDB, Couchbase e Amazon DynamoDB.

Bancos de dados de eventos armazenam dados como uma série de eventos, capturando cada mudança nos dados. Eles são adequados para aplicações que exigem auditoria, event sourcing e processamento de dados complexo. Exemplos incluem Apache Kafka, Apache Pulsar e AWS Kinesis.
Decisão

Depois de avaliar cuidadosamente os requisitos e restrições da nossa aplicação, decidimos usar um banco de dados de documentos.

## Justificativa

Escolhemos um banco de dados de documentos porque:

1. Nossa aplicação exige um modelo de dados flexível que possa evoluir com o tempo. Bancos de dados de documentos nos permitem armazenar dados em um formato sem esquema, o que significa que podemos adicionar novos campos ou alterar a estrutura de documentos existentes sem ter que modificar o esquema do banco de dados.

2. Nossa aplicação precisa escalar horizontalmente para lidar com grandes volumes de dados e tráfego. Bancos de dados de documentos fornecem suporte integrado a sharding e replicação, o que nos permite distribuir dados entre múltiplos servidores e lidar com alta vazão de leitura e escrita.

3. Nossa aplicação exige recuperação de dados rápida e eficiente. Bancos de dados de documentos fornecem recursos poderosos de indexação e consulta que nos permitem recuperar dados de forma rápida e eficiente.

4. Nossa aplicação não exige transações ou relacionamentos de dados complexos. Embora bancos de dados relacionais se destaquem ao impor restrições de integridade de dados e lidar com transações complexas, nossa aplicação não tem tais requisitos. Bancos de dados de documentos podem fornecer garantias suficientes de consistência e durabilidade para nosso caso de uso.

## Consequências

Ao escolher um banco de dados de documentos, precisaremos investir em aprender e entender a tecnologia específica que escolhermos usar. Além disso, precisaremos garantir que o modelo de dados da nossa aplicação se encaixe bem no modelo de dados do banco de dados de documentos para maximizar performance e escalabilidade.

No entanto, acreditamos que os benefícios de usar um banco de dados de documentos superam os custos e que ele é o melhor ajuste para os requisitos e restrições da nossa aplicação.
