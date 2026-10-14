# Registro de decisão de arquitetura: kit de ferramentas de biblioteca de gráficos para visualização de dados com TypeScript e JSON

<!--

ChatGPT prompt:

Long software architecture decision record 
chart library toolkit for data visualization using TypeScript and JSON

Evaluate Charts: Apache ECharts, Chart.js, ApexCharts, AG Charts, Highcharts, Carbon Charts, Layer Cake, D3.

Primary need: advanced interactive charts, especially for financial data, scientific data, and government data.

High importance: 1. Agile development because this is for a startup. 2. Doughnut Chart, Radar Chart, Clustering Process
Chart, Area Chart with Time Axis, Candlestick Chart, Nightingale Chart, Geo SVG Map. 3. Free open source.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Objetivo principal:**  
Selecionar um kit de ferramentas de gráficos avançado para criar visualizações interativas, com foco em dados financeiros, dados científicos e dados governamentais, usando TypeScript e JSON. A biblioteca deve oferecer recursos robustos, flexibilidade e ser de código aberto. 

### Contexto e requisitos:

1. **Desenvolvimento ágil (alta prioridade)**: como startup, a iteração rápida, a prototipagem e a flexibilidade no desenvolvimento são essenciais. A biblioteca de gráficos deve permitir ciclos de desenvolvimento rápidos.
   
2. **Tipos de gráficos (alta prioridade)**:
   - **Gráfico de rosca (Doughnut Chart)**
   - **Gráfico de radar (Radar Chart)**
   - **Gráfico de processo de agrupamento (Clustering Process Chart)**
   - **Gráfico de área com eixo de tempo (Area Chart with Time Axis)**
   - **Gráfico de velas (Candlestick Chart)**
   - **Gráfico de Nightingale (Nightingale Chart)**
   - **Mapa SVG geográfico (Geo SVG Map)**
   
   Esses tipos de gráficos são especificamente importantes para visualizar conjuntos de dados complexos, como tendências financeiras, métricas científicas e informações geográficas.

3. **Gratuita e de código aberto (alta prioridade)**: o kit de ferramentas deve ser de código aberto para evitar custos de licenciamento, oferecer transparência e flexibilidade de personalização.

4. **Critérios de baixa importância**:
   - **Velocidade de execução**: embora o desempenho seja importante, não é uma prioridade máxima para esta decisão.
   - **Escalabilidade**: embora a escalabilidade seja em geral importante, a necessidade imediata é construir um MVP que possa crescer com o tempo. As preocupações com escalabilidade podem ser tratadas depois.
   - **Compatibilidade retroativa**: não é uma preocupação primária para a construção inicial, desde que a biblioteca seja moderna e mantida ativamente.

### Bibliotecas avaliadas:

1. **Apache ECharts**
2. **Chart.js**
3. **ApexCharts**
4. **AG Charts**
5. **Highcharts**
6. **Carbon Charts**
7. **Layer Cake**
8. **D3.js**

---

### 1. **Apache ECharts**

**Visão geral**:  
O Apache ECharts é uma biblioteca de gráficos poderosa e flexível para visualizações interativas e personalizáveis. Oferece suporte a uma ampla variedade de gráficos e é particularmente forte em visualizações complexas e dinâmicas.

**Pontos fortes**:
- **Interatividade avançada**: o ECharts se destaca em fornecer gráficos interativos, oferecendo recursos como zoom, panorâmica e atualizações dinâmicas de dados.
- **Rosca, radar, velas, mapas SVG geográficos**: o ECharts dá suporte a muitos dos tipos de gráficos necessários, incluindo rosca, radar, velas e visualizações de mapas geográficos.
- **Gratuito e de código aberto**: o ECharts é uma biblioteca de código aberto, o que se adequa à natureza econômica de uma startup e dá liberdade para modificar o código.
- **Flexibilidade e extensibilidade**: altamente personalizável, com amplo suporte a animações, visualizações personalizadas e técnicas avançadas de gráficos.
  
**Pontos fracos**:
- **Curva de aprendizado**: o ECharts, embora poderoso, pode ter uma curva de aprendizado mais íngreme devido à sua flexibilidade e à API extensa.
- **Complexidade da documentação**: a documentação é abrangente, mas pode ser sufocante para desenvolvedores que estão apenas começando a usá-la.

**Veredito**:  
O ECharts é muito adequado ao projeto por seu suporte a gráficos interativos, incluindo todos os tipos necessários, como gráficos de velas, gráficos de radar e mapas geográficos. Sua natureza de código aberto se alinha à necessidade do projeto de flexibilidade e custo-benefício.

---

### 2. **Chart.js**

**Visão geral**:  
O Chart.js é uma biblioteca de gráficos simples e fácil de usar para construir tipos de gráficos comuns. É conhecida por sua simplicidade e facilidade de integração.

**Pontos fortes**:
- **Facilidade de uso**: o Chart.js é muito simples de configurar e usar, com curva de aprendizado mínima.
- **Código aberto**: o Chart.js é gratuito e de código aberto, o que é crítico para reduzir custos.
- **Tipos de gráficos comuns**: dá suporte a gráficos básicos como rosca, área, radar e linha, que cobrem a maior parte das necessidades primárias.

**Pontos fracos**:
- **Gráficos avançados limitados**: o Chart.js não oferece suporte nativo a tipos de gráficos complexos, como gráficos de velas, mapas SVG geográficos ou gráficos de processo de agrupamento. Embora esses recursos possam ser adicionados por meio de plugins ou personalização, isso não é tão direto quanto em outras bibliotecas.
- **Interatividade**: embora o Chart.js dê suporte a interatividade básica (p. ex., dicas de ferramenta e efeitos ao passar o mouse), não oferece recursos tão avançados quanto o ECharts ou o D3.js.

**Veredito**:  
O Chart.js é ótimo para projetos simples e rápidos, mas a falta de suporte a tipos de gráficos complexos o torna inadequado para uma aplicação intensiva em dados com necessidades avançadas, como gráficos de velas e mapas geográficos. É uma boa escolha para prototipagem, mas, para os tipos de gráficos necessários, ferramentas mais avançadas são recomendadas.

---

### 3. **ApexCharts**

**Visão geral**:  
O ApexCharts é uma biblioteca de gráficos moderna que fornece uma variedade de tipos de gráficos e se concentra em visualizações interativas com uma API fácil de usar.

**Pontos fortes**:
- **Recursos interativos**: o ApexCharts oferece gráficos interativos com dicas de ferramenta, zoom, panorâmica e atualizações.
- **Suporte a gráficos financeiros e científicos**: dá suporte a uma ampla variedade de tipos de gráficos, incluindo gráficos de velas, de radar e de área.
- **Facilidade de uso**: tem uma API direta e é simples de integrar a um projeto.
- **Gratuito e de código aberto**: o ApexCharts oferece uma versão de código aberto gratuita adequada a muitos casos de uso.
  
**Pontos fracos**:
- **Personalização complexa**: embora ofereça muitos recursos, as opções de personalização não são tão flexíveis quanto as do ECharts ou do D3.js para necessidades de gráficos altamente complexas ou personalizadas.
- **Mapas geográficos**: o ApexCharts não oferece suporte nativo a mapas geográficos nem a gráficos de processo de agrupamento, que são necessários para este projeto.

**Veredito**:  
O ApexCharts é um forte concorrente por sua facilidade de uso e interatividade, mas fica aquém em certos tipos de gráficos avançados, particularmente na necessidade de mapas geográficos e gráficos de agrupamento. É uma boa opção para gráficos mais simples, mas carece de alguns recursos necessários.

---

### 4. **AG Charts**

**Visão geral**:  
O AG Charts é uma biblioteca de gráficos de nível comercial projetada para desempenho e precisão. É muito adequada para criar painéis financeiros, científicos e de negócios.

**Pontos fortes**:
- **Tipos de gráficos avançados**: o AG Charts dá suporte a muitos tipos de gráficos avançados, incluindo gráficos de velas, de área, de radar e mais. Também oferece integração profunda com outros produtos AG-Grid.
- **Alto desempenho**: oferece excelente desempenho, especialmente ao lidar com grandes conjuntos de dados.
- **Interatividade**: o AG Charts dá suporte a vários recursos interativos, como zoom, dicas de ferramenta e atualizações dinâmicas.

**Pontos fracos**:
- **Não totalmente gratuito**: embora o AG Charts ofereça uma versão gratuita, a versão completa em recursos é paga, o que pode ser uma barreira para startups que querem minimizar custos.
- **Complexidade**: embora a biblioteca seja rica em recursos, pode ser um exagero para projetos mais simples e pode exigir mais configuração em comparação com as outras opções.

**Veredito**:  
O AG Charts é poderoso e rico em recursos, mas pode não ser o melhor ajuste devido à sua natureza comercial e à estrutura de custos. Sua adequação depende de o orçamento comportar as versões pagas ou de se preferem alternativas de código aberto.

---

### 5. **Highcharts**

**Visão geral**:  
O Highcharts é uma biblioteca de gráficos popular, conhecida por sua ampla gama de tipos de gráficos e poderosas opções de personalização.

**Pontos fortes**:
- **Tipos de gráficos abrangentes**: o Highcharts dá suporte a uma ampla variedade de gráficos, incluindo velas, radar, área e mapas geográficos.
- **Interativo e dinâmico**: o Highcharts fornece recursos interativos ricos, incluindo drill-downs, zoom e panorâmica.
- **Facilidade de uso**: tem uma API amigável e boa documentação, facilitando o início.

**Pontos fracos**:
- **Licença comercial**: embora o Highcharts ofereça uma versão gratuita para uso não comercial, a licença comercial é cara, o que pode ser uma desvantagem significativa para startups.
- **Curva de aprendizado**: embora não seja tão íngreme quanto a do ECharts, a curva de aprendizado do Highcharts ainda pode ser desafiadora para iniciantes.

**Veredito**:  
O Highcharts é uma biblioteca rica em recursos, mas seu licenciamento comercial o torna menos adequado para projetos de código aberto sensíveis a custos. Suas opções abrangentes de gráficos são um ponto positivo, mas a questão do licenciamento limita seu apelo neste caso de uso.

---

### 6. **Carbon Charts**

**Visão geral**:  
O Carbon Charts é uma biblioteca de gráficos desenvolvida pela IBM, projetada para criar gráficos visualmente atraentes e altamente personalizáveis.

**Pontos fortes**:
- **Personalização**: o Carbon Charts permite ampla personalização da aparência e do comportamento dos gráficos.
- **Código aberto**: é gratuito e de código aberto, o que se alinha ao requisito do projeto de soluções econômicas.
- **Suporte a gráficos comuns**: dá suporte a tipos de gráficos comuns, como rosca, radar e área, embora não tenha suporte a tipos mais avançados, como mapas geográficos ou gráficos de velas.

**Pontos fracos**:
- **Tipos de gráficos avançados limitados**: não dá suporte a mapas geográficos, gráficos de processo de agrupamento nem gráficos de velas, todos essenciais para o projeto.
- **Ecossistema menor**: o Carbon Charts tem uma comunidade e um ecossistema menores em comparação com bibliotecas de gráficos maiores, como ECharts ou Highcharts.

**Veredito**:  
O Carbon Charts é de código aberto e personalizável, mas carece de suporte aos tipos de gráficos mais complexos necessários para este projeto. É mais adequado a necessidades de gráficos mais simples.

---

### 7. **Layer Cake**

**Visão geral**:  
O Layer Cake é uma biblioteca de visualização de dados projetada para criar visualizações flexíveis e em camadas.

**Pontos fortes**:
- **Camadas personalizáveis**: oferece poderosas opções de camadas para visualizações complexas.
- **Código aberto**: é gratuito e de código aberto, o que o torna uma opção viável para projetos com orçamento restrito.

**Pontos fracos**:
- **Documentação limitada**: o Layer Cake carece de documentação extensa e de apoio da comunidade, tornando-o mais difícil de trabalhar em comparação com bibliotecas mais estabelecidas.
- **Não foi feito para gráficos**: o Layer Cake é mais adequado para visualizações que não são gráficos, então suas opções de gráficos prontas são limitadas.

**Veredito**:  
Embora interessante para visualizações únicas, o Layer Cake não é ideal para requisitos tradicionais de gráficos, como gráficos de velas ou gráficos de radar. É mais adequado a visualizações personalizadas fora do escopo de gráficos padrão.

---

### 8. **D3.js**

**Visão geral**:  
O D3.js é uma poderosa biblioteca JavaScript para criar visualizações orientadas a dados por meio de HTML, SVG e CSS.

**Pontos fortes**:
- **Flexibilidade incomparável**: o D3.js permite criar praticamente qualquer tipo de visualização personalizada, tornando-o muito poderoso para gráficos avançados e interativos.
- **Recursos extensos**: dá suporte a todos os tipos de gráficos necessários, incluindo mapas geográficos, gráficos de agrupamento e mais.
- **Personalizável**: o nível de personalização do D3.js é incomparável, permitindo aos desenvolvedores construir visualizações altamente sob medida.

**Pontos fracos**:
- **Curva de aprendizado íngreme**: o D3.js tem uma curva de aprendizado íngreme e é mais complexo de integrar em comparação com outras bibliotecas.
- **Consome tempo**: construir gráficos no D3.js pode consumir muito tempo, especialmente para gráficos comuns, como de velas ou de rosca.

**Veredito**:  
O D3.js é incrivelmente poderoso para gráficos avançados e personalizados, mas é um exagero para muitos casos de uso típicos devido à curva de aprendizado íngreme e ao tempo de desenvolvimento. É melhor para situações em que as outras bibliotecas de gráficos não oferecem o nível de personalização necessário.

---

### Conclusão

Depois de avaliar as bibliotecas com base nas necessidades do projeto, o **Apache ECharts** se destaca como a melhor opção. Ele dá suporte à gama completa de gráficos necessários, incluindo mapas geográficos, gráficos de velas e gráficos de agrupamento. É de código aberto, rico em recursos e altamente interativo, o que se alinha perfeitamente aos objetivos do projeto. Embora o **D3.js** ofereça a maior flexibilidade, sua complexidade e o investimento de tempo o tornam menos ideal para uma startup que busca iterar rapidamente. O **ApexCharts** e o **Chart.js** são boas alternativas para projetos mais simples, mas carecem de suporte a tipos de gráficos avançados.
