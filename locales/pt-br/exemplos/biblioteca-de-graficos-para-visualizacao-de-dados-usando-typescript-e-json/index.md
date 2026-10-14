# Registro de Decisão de Arquitetura: biblioteca de gráficos para visualização de dados usando TypeScript e JSON

<!--

Prompt do ChatGPT:

Registro longo de decisão de arquitetura de software
biblioteca de gráficos para visualização de dados usando TypeScript e JSON

Avalie gráficos: Apache ECharts, Chart.js, ApexCharts, AG Charts, Highcharts, Carbon Charts, Layer Cake, D3.

Necessidade primária: gráficos interativos avançados, especialmente para dados financeiros, dados científicos e dados governamentais.

Alta importância: 1. Desenvolvimento ágil porque isto é para uma startup. 2. Doughnut Chart, Radar Chart, Clustering Process
Chart, Area Chart with Time Axis, Candlestick Chart, Nightingale Chart, Geo SVG Map. 3. Código aberto gratuito.

Baixa importância: 1. Velocidade em tempo de execução. 2. Escalabilidade. 3. Compatibilidade retroativa.

-->

**Objetivo primário:**
Selecionar uma biblioteca avançada de gráficos para criar visualizações interativas, com foco em dados financeiros, dados científicos e dados governamentais usando TypeScript e JSON. A biblioteca deve fornecer funcionalidades robustas, flexibilidade e ser open-source.

### Contexto e requisitos:

1. **Desenvolvimento ágil (alta prioridade)**: Como uma startup, iteração rápida, prototipação e flexibilidade no desenvolvimento são essenciais. A biblioteca de gráficos deve permitir ciclos de desenvolvimento rápidos.

2. **Tipos de gráfico (alta prioridade)**:
   - **Doughnut Chart**
   - **Radar Chart**
   - **Clustering Process Chart**
   - **Area Chart with Time Axis**
   - **Candlestick Chart**
   - **Nightingale Chart**
   - **Geo SVG Map**

   Esses tipos de gráfico são especificamente importantes para visualizar conjuntos de dados complexos, como tendências financeiras, métricas científicas e informações geográficas.

3. **Gratuito e open source (alta prioridade)**: A biblioteca deve ser open-source para evitar custos de licenciamento, fornecer transparência e oferecer flexibilidade para customização.

4. **Critérios de baixa importância**:
   - **Velocidade em tempo de execução**: Embora performance seja importante, ela não é uma prioridade principal para esta decisão.
   - **Escalabilidade**: Embora escalabilidade seja geralmente importante, a necessidade imediata é construir um MVP que possa crescer com o tempo. Preocupações de escalabilidade podem ser tratadas mais tarde.
   - **Compatibilidade retroativa**: Não é uma preocupação primária para a construção inicial, desde que a biblioteca seja moderna e mantida ativamente.

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
Apache ECharts é uma biblioteca de gráficos poderosa e flexível para visualizações interativas e customizáveis. Ela fornece suporte a uma ampla variedade de gráficos e é particularmente forte em visualizações complexas e dinâmicas.

**Pontos fortes**:
- **Interatividade avançada**: ECharts se destaca ao fornecer gráficos interativos, oferecendo recursos como zoom, pan e atualizações dinâmicas de dados.
- **Doughnut, Radar, Candlestick, Geo SVG Maps**: ECharts suporta muitos dos tipos de gráfico necessários, incluindo doughnut, radar, candlestick e visualizações de mapas geográficos.
- **Gratuito e open source**: ECharts é uma biblioteca open-source, o que se ajusta à natureza consciente de orçamento de uma startup e fornece liberdade para modificar o código.
- **Flexibilidade e extensibilidade**: Altamente customizável, com amplo suporte a animações, visualizações customizadas e técnicas avançadas de gráficos.

**Pontos fracos**:
- **Curva de aprendizado**: ECharts, embora poderoso, pode ter uma curva de aprendizado mais íngreme devido à sua flexibilidade e API extensa.
- **Complexidade da documentação**: A documentação é abrangente, mas pode ser excessiva para desenvolvedores que estão apenas começando com a biblioteca.

**Veredito**:
ECharts é altamente adequado para o projeto devido ao seu suporte a gráficos interativos, incluindo todos os tipos necessários, como gráficos candlestick, gráficos radar e mapas geográficos. Sua natureza open-source se alinha à necessidade do projeto por flexibilidade e custo-benefício.

---

### 2. **Chart.js**

**Visão geral**:
Chart.js é uma biblioteca de gráficos simples e fácil de usar para construir tipos comuns de gráficos. Ela é conhecida por sua simplicidade e facilidade de integração.

**Pontos fortes**:
- **Facilidade de uso**: Chart.js é muito simples de configurar e usar, com uma curva de aprendizado mínima.
- **Open source**: Chart.js é gratuito e open-source, o que é crítico para reduzir custos.
- **Tipos comuns de gráficos**: Ele suporta gráficos básicos como doughnut, área, radar e linha, que cobrem a maior parte das necessidades primárias.

**Pontos fracos**:
- **Gráficos avançados limitados**: Chart.js não suporta nativamente tipos de gráfico complexos como candlestick charts, geo SVG maps ou clustering process charts. Embora esses recursos possam ser adicionados por meio de plugins ou customização, isso não é tão direto quanto com outras bibliotecas.
- **Interatividade**: Embora Chart.js suporte interatividade básica (por exemplo, tooltips e efeitos de hover), ele não oferece recursos tão avançados quanto ECharts ou D3.js.

**Veredito**:
Chart.js é ótimo para projetos simples e rápidos, mas sua falta de suporte a tipos de gráfico complexos o torna inadequado para uma aplicação intensiva em dados com necessidades avançadas como candlestick charts e geo maps. É uma boa escolha para prototipação, mas, para os tipos de gráfico necessários, ferramentas mais avançadas são recomendadas.

---

### 3. **ApexCharts**

**Visão geral**:
ApexCharts é uma biblioteca moderna de gráficos que fornece uma variedade de tipos de gráfico e se concentra em visualizações interativas com uma API fácil de usar.

**Pontos fortes**:
- **Recursos interativos**: ApexCharts oferece gráficos interativos com tooltips, zoom, pan e atualizações.
- **Suporte a gráficos financeiros e científicos**: Ele suporta uma ampla variedade de tipos de gráfico, incluindo candlestick charts, radar charts e area charts.
- **Facilidade de uso**: Ele tem uma API direta e é simples de integrar a um projeto.
- **Gratuito e open source**: ApexCharts oferece uma versão open-source gratuita que é adequada para muitos casos de uso.

**Pontos fracos**:
- **Customização complexa**: Embora forneça muitos recursos, as opções de customização não são tão flexíveis quanto ECharts ou D3.js para necessidades de gráficos altamente complexas ou customizadas.
- **Geo Maps**: ApexCharts não suporta nativamente geo maps ou clustering process charts, que são necessários para este projeto.

**Veredito**:
ApexCharts é um candidato forte devido à sua facilidade de uso e interatividade, mas fica aquém em certos tipos de gráfico avançados, particularmente a necessidade de geo maps e clustering charts. É uma boa opção para gráficos mais simples, mas carece de alguns recursos necessários.

---

### 4. **AG Charts**

**Visão geral**:
AG Charts é uma biblioteca de gráficos de nível comercial projetada para performance e precisão. Ela é altamente adequada para criar dashboards financeiros, científicos e de negócios.

**Pontos fortes**:
- **Tipos de gráfico avançados**: AG Charts suporta muitos tipos de gráfico avançados, incluindo candlestick charts, area charts, radar charts e outros. Ela também oferece integração profunda com outros produtos AG-Grid.
- **Alta performance**: Ela oferece excelente performance, especialmente ao lidar com grandes conjuntos de dados.
- **Interatividade**: AG Charts suporta uma variedade de recursos interativos como zoom, tooltips e atualizações dinâmicas.

**Pontos fracos**:
- **Não totalmente gratuita**: Embora AG Charts ofereça uma versão gratuita, a versão completa é paga, o que pode ser uma barreira para startups que procuram minimizar custos.
- **Complexidade**: Embora a biblioteca seja rica em recursos, pode ser excessiva para projetos mais simples e pode exigir mais configuração em comparação com outras opções.

**Veredito**:
AG Charts é poderosa e rica em recursos, mas pode não ser a melhor opção devido à sua natureza comercial e estrutura de custos. Sua adequação depende de o orçamento poder acomodar versões pagas ou de alternativas open-source serem preferidas.

---

### 5. **Highcharts**

**Visão geral**:
Highcharts é uma biblioteca de gráficos popular conhecida por sua ampla variedade de tipos de gráfico e opções poderosas de customização.

**Pontos fortes**:
- **Tipos de gráfico abrangentes**: Highcharts suporta uma ampla variedade de gráficos, incluindo candlestick, radar, área e geo maps.
- **Interativo e dinâmico**: Highcharts fornece recursos interativos ricos, incluindo drill-downs, zoom e pan.
- **Facilidade de uso**: Ele tem uma API amigável e boa documentação, o que facilita começar.

**Pontos fracos**:
- **Licença comercial**: Embora Highcharts ofereça uma versão gratuita para uso não comercial, a licença comercial é cara, o que pode ser uma desvantagem significativa para startups.
- **Curva de aprendizado**: Embora não seja tão íngreme quanto ECharts, a curva de aprendizado do Highcharts ainda pode ser desafiadora para iniciantes.

**Veredito**:
Highcharts é uma biblioteca rica em recursos, mas seu licenciamento comercial a torna menos adequada para projetos open-source e sensíveis a custo. Suas opções abrangentes de gráficos são um ponto positivo, mas a questão de licenciamento limita seu apelo para este caso de uso.

---

### 6. **Carbon Charts**

**Visão geral**:
Carbon Charts é uma biblioteca de gráficos desenvolvida pela IBM, projetada para criar gráficos visualmente atraentes e altamente customizáveis.

**Pontos fortes**:
- **Customização**: Carbon Charts permite ampla customização da aparência e do comportamento dos gráficos.
- **Open source**: Ela é gratuita e open-source, o que se alinha ao requisito do projeto por soluções amigáveis ao orçamento.
- **Suporte a gráficos comuns**: Ela suporta tipos comuns de gráfico como doughnut, radar e area charts, embora careça de suporte a tipos mais avançados como geo maps ou candlestick charts.

**Pontos fracos**:
- **Tipos de gráfico avançados limitados**: Ela não suporta geo maps, clustering process charts ou candlestick charts, que são essenciais para o projeto.
- **Ecossistema menor**: Carbon Charts tem uma comunidade e um ecossistema menores em comparação com bibliotecas de gráficos maiores, como ECharts ou Highcharts.

**Veredito**:
Carbon Charts é open-source e customizável, mas carece de suporte aos tipos de gráfico mais complexos necessários para este projeto. Ela é mais adequada para necessidades de gráficos mais simples.

---

### 7. **Layer Cake**

**Visão geral**:
Layer Cake é uma biblioteca de visualização de dados projetada para criar visualizações flexíveis e em camadas.

**Pontos fortes**:
- **Camadas customizáveis**: Ela fornece opções poderosas de camadas para visualizações complexas.
- **Open source**: Ela é gratuita e open-source, tornando-se uma opção viável para projetos conscientes de orçamento.

**Pontos fracos**:
- **Documentação limitada**: Layer Cake carece de documentação extensa e suporte da comunidade, o que a torna mais difícil de usar em comparação com bibliotecas mais estabelecidas.
- **Não construída para gráficos**: Layer Cake é mais adequada para visualizações que não são gráficos, portanto suas opções de gráficos prontas para uso são limitadas.

**Veredito**:
Embora interessante para visualizações únicas, Layer Cake não é ideal para requisitos tradicionais de gráficos, como candlestick charts ou radar charts. Ela é mais adequada para visualizações customizadas fora do escopo de gráficos padrão.

---

### 8. **D3.js**

**Visão geral**:
D3.js é uma poderosa biblioteca JavaScript para criar visualizações orientadas por dados por meio de HTML, SVG e CSS.

**Pontos fortes**:
- **Flexibilidade incomparável**: D3.js permite criar virtualmente qualquer tipo de visualização customizada, tornando-o altamente poderoso para gráficos avançados e interativos.
- **Recursos extensos**: Ele suporta todos os tipos de gráfico necessários, incluindo geo maps, clustering charts e outros.
- **Customizável**: O nível de customização em D3.js é incomparável, permitindo que desenvolvedores criem visualizações altamente sob medida.

**Pontos fracos**:
- **Curva de aprendizado íngreme**: D3.js tem uma curva de aprendizado íngreme e é mais complexo de integrar em comparação com outras bibliotecas.
- **Consome tempo**: Construir gráficos em D3.js pode consumir tempo, especialmente para gráficos comuns como candlestick ou doughnut charts.

**Veredito**:
D3.js é incrivelmente poderoso para gráficos avançados e customizados, mas é excessivo para muitos casos de uso típicos devido à sua curva de aprendizado íngreme e ao tempo de desenvolvimento. Ele é melhor para situações em que as outras bibliotecas de gráficos não fornecem o nível de customização necessário.

---

### Conclusão

Depois de avaliar as bibliotecas com base nas necessidades do projeto, **Apache ECharts** se destaca como a melhor opção. Ele suporta toda a gama de gráficos necessários, incluindo geo maps, candlestick charts e clustering charts. É open-source, rico em recursos e altamente interativo, o que se alinha perfeitamente aos objetivos do projeto. Embora **D3.js** ofereça a maior flexibilidade, sua complexidade e investimento de tempo o tornam menos ideal para uma startup que procura iterar rapidamente. **ApexCharts** e **Chart.js** são boas alternativas para projetos mais simples, mas carecem de suporte a tipos de gráfico avançados.
