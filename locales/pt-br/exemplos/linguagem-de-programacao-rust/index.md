# Registro de decisão de arquitetura: linguagem de programação Rust

Número da decisão: AR-001

Título da decisão: Adoção da linguagem de programação Rust

Data: 1 de dezembro de 2021

Status: Aceito

### Declaração do problema

À medida que continuamos a desenvolver aplicações de software, observamos que é cada vez mais desafiador mitigar possíveis vulnerabilidades de segurança e prevenir erros de runtime. Com as linguagens de programação existentes, como C e C++, continuamos a enfrentar problemas como buffer overflows, vazamentos de memória e comportamento indefinido que levam a crashes das aplicações. Precisamos de uma linguagem de programação que forneça garantias de segurança de memória e seja eficiente o bastante para dar suporte a aplicações críticas em performance.

### Considerações

Várias linguagens de programação são projetadas para tratar os problemas existentes. Entre elas, a linguagem de programação Rust ganhou atenção significativa da comunidade de desenvolvedores devido aos seus recursos de design únicos. As considerações incluem:

1. Segurança de memória e segurança

2. Performance e eficiência

3. Suporte e adoção da comunidade

4. Curva de aprendizado

5. Ferramentas e ecossistema

6. Compatibilidade com sistemas de software existentes.

### Restrições

Adotar uma nova linguagem de programação exige retreinar desenvolvedores, o que consome tempo e recursos. Integrar a linguagem ao fluxo de desenvolvimento existente pode ser um desafio. Precisamos garantir compatibilidade com os sistemas existentes e evitar breaking changes para manter a continuidade.

### Implementação

1. Nossa equipe de desenvolvimento passará por treinamento para aprender e se familiarizar com a linguagem de programação Rust.

2. Criaremos um novo projeto usando Rust em caráter experimental para avaliar sua compatibilidade e adequação aos nossos propósitos de desenvolvimento.

3. Migraremos gradualmente sistemas existentes escritos em C e C++ para Rust.

4. Colaboraremos com a comunidade Rust para explorar as ferramentas e bibliotecas disponíveis que podem aprimorar nosso fluxo de desenvolvimento.

5. Monitoraremos a performance de Rust e a compararemos regularmente com a performance das linguagens de programação existentes.

6. Adotaremos uma abordagem de longo prazo que equilibra os custos de treinamento, integração e benefícios potenciais do uso de Rust.

### Justificativa

Adotamos Rust devido aos seus recursos únicos, projetados para fornecer garantias de segurança de memória e segurança enquanto mantém performance e eficiência. O sistema de tipos robusto, o borrow checker e os conceitos de segurança de memória de Rust fazem dela uma linguagem altamente adequada para desenvolver aplicações críticas em performance e críticas em segurança. Além disso, Rust tem uma comunidade significativa de desenvolvedores, permitindo que acessemos uma ampla variedade de ferramentas, bibliotecas e ecossistema que dão suporte ao nosso fluxo de desenvolvimento. Embora Rust venha com uma curva de aprendizado, acreditamos que os benefícios de adotar Rust superam os custos e fornecem uma excelente oportunidade para crescimento e inovação contínuos.

### Consequências

1. A adoção de Rust exigirá um investimento significativo em tempo e recursos para treinar desenvolvedores e integrar a linguagem ao fluxo de desenvolvimento existente.

2. Adotar Rust pode causar algum grau de problemas de compatibilidade com sistemas existentes, exigindo refatoração e modificações.

3. A adoção de Rust pode aumentar o número de desenvolvedores que podem contribuir para nosso projeto ao atrair desenvolvedores Rust que queiram trabalhar em projetos empolgantes.

4. A adoção poderia levar a melhor performance, eficiência e segurança em comparação com as linguagens existentes.

5. Finalmente, adotar Rust traz o benefício potencial de reduzir vulnerabilidades de segurança em nossas aplicações.

<h6>Crédito: esta página é gerada pelo ChatGPT e depois editada para clareza e formato.</h6>
