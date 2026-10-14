## Registro de decisão de arquitetura: framework de automação de navegador para testes E2E (Playwright ou Selenium)

### 1. **Contexto**

Estamos no processo de selecionar um framework de automação de navegador para o nosso pipeline de testes de ponta a ponta (E2E). Esse framework será parte integrante dos nossos processos de CI/CD, executando testes que simulam interações reais de usuários em nossa plataforma. Especificamente, os testes cobrirão cenários como cadastro/login de usuários, upload de arquivos, interações com painéis e download de relatórios.

Como **startup**, nosso foco é o **desenvolvimento ágil**, com necessidade de iterar e evoluir rapidamente. Nossa equipe trabalha predominantemente com **TypeScript** e **Python**, e a capacidade de escrever testes nessas linguagens é essencial. Além disso, a plataforma contém **gráficos e painéis interativos**, o que torna crítico que a ferramenta de automação dê bom suporte a UIs ricas e dinâmicas.

Os dois concorrentes para essa tarefa são o **Playwright** e o **Selenium**, cada um com seus pontos fortes e trade-offs. Precisamos avaliar esses frameworks com base nos recursos e requisitos descritos abaixo.

### 2. **Opções consideradas**

- **Playwright** (da Microsoft)
- **Selenium** (do Selenium Project)

### 3. **Fatores da decisão**

Os fatores que influenciam a nossa decisão são os seguintes:

1. **Desenvolvimento ágil**: a ferramenta escolhida deve possibilitar ciclos de desenvolvimento rápidos e flexíveis.
2. **Suporte a linguagens**: nossa equipe precisa de suporte tanto a **TypeScript** quanto a **Python**.
3. **Teste de UI interativa**: é essencial a capacidade de testar com confiabilidade gráficos interativos, painéis e elementos dinâmicos.
4. **Velocidade de execução**: embora não seja uma preocupação principal, o desempenho em pipelines de CI/CD é uma consideração.
5. **Escalabilidade**: não estamos planejando uma escala massiva no futuro imediato, mas queremos garantir que a solução consiga lidar com o crescimento futuro.
6. **Compatibilidade retroativa**: sistemas legados e compatibilidade com navegadores mais antigos não são críticos para o nosso projeto neste momento.
7. **Teste em dispositivos móveis**: embora não seja um foco imediato, o framework deve ser capaz de testar recursos responsivos para dispositivos móveis ou ser extensível para tais casos de uso.
8. **Teste com vários monitores**: o suporte a configurações com vários monitores é um requisito secundário, especialmente se um dia ampliarmos o teste para fluxos de trabalho de usuário mais complexos.
9. **Teste de upload de arquivos**: o framework deve lidar com uploads de arquivos de forma eficiente, um requisito central das nossas necessidades de teste.

### 4. **Critérios de avaliação**

- **Facilidade de uso**: quão fácil é escrever e manter testes?
- **Suporte a linguagens**: o framework dá suporte a TypeScript e Python, as duas linguagens que nossa equipe mais usa?
- **Teste de UI interativa**: quão bem o framework lida com interfaces de usuário complexas e interativas, como gráficos, uploads de arquivos e dados dinâmicos?
- **Integração com CI/CD**: quão bem o framework se integra a ferramentas e serviços comuns de CI/CD?
- **Suporte a vários navegadores**: quais navegadores são suportados e qual o desempenho deles?
- **Desempenho e velocidade**: com que rapidez os testes são executados, especialmente em um pipeline de CI/CD?
- **Escalabilidade**: quão bem o framework consegue escalar se mais testes ou cenários mais complexos forem adicionados?
- **Comunidade e ecossistema**: quão ativa é a comunidade do framework? Há muitas integrações e extensões disponíveis?

### 5. **Considerações**

#### 5.1 **Playwright**

##### **Prós**:
1. **API mais inteligente para uploads de arquivos locais**: a API do Playwright para interagir com arquivos locais e realizar uploads de arquivos é mais simples e intuitiva. Isso tornaria os testes de upload de arquivos mais fáceis de implementar e manter.
2. **Sintaxe e geração de código**: o Playwright tem uma sintaxe mais curta e concisa. Isso resulta em menos código repetitivo, o que melhora a manutenibilidade e a eficiência do desenvolvedor. Além disso, essa sintaxe mais curta melhora a qualidade da geração de código pela OpenAI, facilitando a geração automática de scripts de teste.
3. **Teste de UI interativa**: o Playwright se destaca no teste de aplicações web dinâmicas e interativas, como as que têm gráficos ricos, interações complexas de usuário e atualizações em tempo real. Ele lida com muita eficácia com WebSockets, WebRTC, shadow DOMs e outras tecnologias web modernas.
4. **Suporte a vários navegadores**: o Playwright dá suporte a **Chromium**, **WebKit** e **Firefox**. Tem desempenho consistente nesses navegadores, o que deve cobrir a maior parte das nossas necessidades de teste.
5. **Integração com CI/CD**: o Playwright se integra perfeitamente a plataformas modernas de CI/CD (GitHub Actions, Jenkins etc.). Pode executar testes em paralelo em diferentes navegadores, otimizando os tempos de execução dos testes e tornando-o adequado para o desenvolvimento rápido.
6. **Rápido e confiável**: o Playwright é em geral mais rápido que o Selenium, especialmente no modo headless, e mais resiliente ao lidar com elementos web assíncronos.

##### **Contras**:
1. **Teste móvel limitado**: embora o Playwright ofereça emulação móvel para navegadores, ele não tem capacidades nativas de teste móvel, como a integração do Selenium com o Appium para teste móvel de verdade.
2. **Ecossistema menor**: o Playwright ainda é mais novo e menos estabelecido que o Selenium. Embora tenha uma comunidade em rápido crescimento e boa documentação, pode ainda não ter o vasto ecossistema de plugins e integrações que o Selenium oferece.
3. **Suporte limitado a navegadores**: embora o Playwright cubra os principais navegadores modernos (Chrome, Safari, Firefox), seu suporte a navegadores legados (p. ex., Internet Explorer) não é tão robusto quanto o do Selenium.

#### 5.2 **Selenium**

##### **Prós**:
1. **Histórico mais longo e maturidade**: o Selenium existe há muito tempo e tem um histórico comprovado. É amplamente usado por muitas equipes e setores, o que levou a um vasto ecossistema de plugins, integrações e recursos.
2. **Suporte a vários navegadores e plataformas**: o Selenium dá suporte a uma **grande variedade de navegadores** e versões, incluindo o **Internet Explorer**, e também pode ser integrado a várias ferramentas, como **Docker**, **Selenium Grid** e **serviços em nuvem**, para testes distribuídos.
3. **Teste móvel**: o Selenium, por meio de sua integração com o **Appium**, é muito mais robusto para teste móvel, tanto para aplicações Android quanto iOS. Isso o torna a melhor escolha para projetos com foco em dispositivos móveis ou dependência pesada deles.
4. **Teste com vários monitores**: o Selenium oferece melhor suporte a cenários que envolvem **vários monitores** ou interações complexas com várias janelas.

##### **Contras**:
1. **Complexidade**: a API do Selenium é mais verbosa e explícita. Embora isso possa ser uma vantagem em alguns casos, significa mais código para escrever e manter, o que pode reduzir a agilidade do desenvolvedor, especialmente importante em um ambiente de startup.
2. **Desempenho**: o Selenium geralmente roda mais devagar que o Playwright, especialmente no modo headless. Isso poderia afetar pipelines de CI/CD, em particular à medida que o número de testes cresce.
3. **Teste de UI interativa**: o Selenium não é tão fluido quanto o Playwright ao testar UIs web modernas e interativas, particularmente com gráficos e atualizações de dados em tempo real. Ele exige mais configuração e tratamento para interagir de forma confiável com conteúdo dinâmico.

### 6. **Resumo da comparação**

| Recurso                          | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Facilidade de uso**                   | Sintaxe mais curta, mais intuitiva para UIs modernas | Mais explícito, exige mais código repetitivo  |
| **Suporte a linguagens**              | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Teste de UI interativa**        | Excelente para UIs dinâmicas e em tempo real          | Lida com UIs básicas, mas mais verboso e complexo para interações ricas |
| **Teste de upload de arquivos**           | API mais inteligente para uploads de arquivos                  | Mais verboso, API menos intuitiva         |
| **Integração com CI/CD**             | Integração fácil com GitHub Actions, Jenkins | Forte integração com muitas ferramentas de CI    |
| **Teste móvel**                | Limitado, apenas emulação                       | Suporte completo via Appium               |
| **Suporte a vários navegadores**         | Chromium, WebKit, Firefox                     | Suporte completo a navegadores principais e legados |
| **Desempenho**                   | Rápido, otimizado para teste headless          | Mais lento, especialmente no modo headless       |
| **Teste com vários monitores**         | Limitado                                       | Bom suporte a configurações com vários monitores    |
| **Comunidade e ecossistema**       | Em crescimento, boa documentação                   | Grande, madura, ecossistema extenso       |

### 7. **Decisão**

Após considerar os requisitos e os trade-offs, o **Playwright** é a melhor escolha para as nossas necessidades atuais. Sua API mais inteligente para testes de upload de arquivos locais, a sintaxe concisa e o forte suporte a testes de UI interativa o tornam ideal para o nosso ciclo de desenvolvimento ágil. O fato de dar suporte tanto a **TypeScript** quanto a **Python** é crítico para a nossa equipe, e a abordagem moderna do framework para testes nos permitirá escrever código limpo e de fácil manutenção.

Embora o **Selenium** continue sendo uma ótima ferramenta, particularmente para teste móvel, suporte a navegadores legados e configurações com vários monitores, ele é menos adequado às nossas necessidades atuais. Sua verbosidade, desempenho mais lento e tratamento mais complexo de UIs dinâmicas, como gráficos, o tornam menos ideal para o nosso caso de uso.

### 8. **Consequências**

- **Ação imediata**: adotaremos o **Playwright** para os nossos testes E2E, focando em testar fluxos de usuário que envolvem cadastro, login, upload de arquivos, painéis e download de relatórios.
- **Considerações de longo prazo**: ficaremos de olho na evolução do ecossistema do Playwright. Se nossas necessidades mudarem, particularmente quanto a teste móvel ou suporte a navegadores legados, poderemos revisitar o Selenium.
- **Treinamento e documentação**: as equipes de desenvolvimento precisarão se familiarizar com a API do Playwright, particularmente para lidar com UIs dinâmicas e uploads de arquivos.
- **Migração**: os testes existentes em Selenium (se houver) serão gradualmente migrados para o Playwright.

### 9. **Considerações futuras**
