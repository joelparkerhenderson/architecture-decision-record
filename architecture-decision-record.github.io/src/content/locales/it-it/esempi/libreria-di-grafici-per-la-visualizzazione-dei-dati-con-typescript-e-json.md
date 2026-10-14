# Registro delle decisioni architetturali: libreria di grafici per la visualizzazione dei dati con TypeScript e JSON

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

**Obiettivo principale:**  
Selezionare un toolkit di grafici avanzato per creare visualizzazioni interattive, con particolare attenzione a dati finanziari, dati scientifici e dati governativi con TypeScript e JSON. La libreria dovrebbe offrire funzionalità robuste e flessibilità ed essere open source. 

### Contesto e requisiti:

1. **Sviluppo agile (priorità alta)**: come startup, l'iterazione rapida, la prototipazione e la flessibilità nello sviluppo sono cruciali. La libreria di grafici deve consentire cicli di sviluppo rapidi.
   
2. **Tipi di grafici (priorità alta)**:
   - **Grafico ad anello (Doughnut Chart)**
   - **Grafico radar (Radar Chart)**
   - **Grafico del processo di clustering (Clustering Process Chart)**
   - **Grafico ad area con asse temporale (Area Chart with Time Axis)**
   - **Grafico a candela (Candlestick Chart)**
   - **Grafico di Nightingale (Nightingale Chart)**
   - **Mappa Geo SVG (Geo SVG Map)**
   
   Questi tipi di grafici sono particolarmente importanti per visualizzare insiemi di dati complessi, come tendenze finanziarie, metriche scientifiche e informazioni geografiche.

3. **Gratuita e open source (priorità alta)**: lo strumento dovrebbe essere open source per evitare costi di licenza, offrire trasparenza e fornire flessibilità per la personalizzazione.

4. **Criteri a bassa priorità**:
   - **Velocità di runtime**: sebbene le prestazioni siano importanti, non sono la priorità più alta per questa decisione.
   - **Scalabilità**: sebbene la scalabilità sia in generale importante, l'esigenza immediata è costruire un MVP che possa crescere nel tempo. Le questioni di scalabilità possono essere affrontate in seguito.
   - **Compatibilità all'indietro**: non è una preoccupazione primaria per la costruzione iniziale, purché la libreria sia moderna e attivamente mantenuta.

### Librerie valutate:

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

**Panoramica**:  
Apache ECharts è una libreria di grafici potente e flessibile per visualizzazioni interattive e personalizzabili. Supporta un'ampia gamma di grafici ed è particolarmente forte nelle visualizzazioni complesse e dinamiche.

**Punti di forza**:
- **Interattività avanzata**: ECharts eccelle nel fornire grafici interattivi e offre funzionalità come zoom, panoramica e aggiornamenti dinamici dei dati.
- **Grafici ad anello, radar, a candela, mappe Geo SVG**: ECharts supporta molti dei tipi di grafici necessari, comprese le visualizzazioni di grafici ad anello, radar, a candela e mappe geografiche.
- **Gratuita e open source**: ECharts è una libreria open source, il che si adatta alla natura attenta al budget di una startup e dà la libertà di modificare il codice.
- **Flessibilità ed estensibilità**: altamente personalizzabile, con ampio supporto per animazioni, visualizzazioni personalizzate e tecniche di grafici avanzate.
  
**Punti deboli**:
- **Curva di apprendimento**: ECharts, sebbene potente, può avere una curva di apprendimento più ripida a causa della sua flessibilità e della sua API estesa.
- **Complessità della documentazione**: la documentazione è estesa ma può essere opprimente per gli sviluppatori che stanno appena iniziando.

**Giudizio**:  
ECharts è molto adatta al progetto grazie al suo supporto per i grafici interattivi, inclusi tutti i tipi necessari come grafici a candela, grafici radar e mappe geografiche. La sua natura open source è in linea con la necessità del progetto di flessibilità ed efficienza dei costi.

---

### 2. **Chart.js**

**Panoramica**:  
Chart.js è una libreria di grafici semplice e facile da usare per costruire tipi di grafici comuni. È nota per la sua semplicità e la facile integrazione.

**Punti di forza**:
- **Facilità d'uso**: Chart.js è molto facile da configurare e usare, con una curva di apprendimento minima.
- **Open source**: Chart.js è gratuita e open source, il che è cruciale per ridurre i costi.
- **Tipi di grafici comuni**: supporta grafici di base come grafici ad anello, ad area, radar e a linee, che coprono la maggior parte delle esigenze primarie.

**Punti deboli**:
- **Grafici avanzati limitati**: Chart.js non supporta in modo nativo tipi di grafici complessi come grafici a candela, mappe Geo SVG o grafici del processo di clustering. Sebbene queste funzionalità possano essere aggiunte tramite plugin o personalizzazione, non è semplice come con altre librerie.
- **Interattività**: sebbene Chart.js supporti l'interattività di base (per esempio suggerimenti ed effetti al passaggio del mouse), non offre funzionalità avanzate come ECharts o D3.js.

**Giudizio**:  
Chart.js è eccellente per progetti semplici e rapidi, ma la mancanza di supporto per tipi di grafici complessi la rende inadatta a un'applicazione ricca di dati con esigenze avanzate come grafici a candela e mappe geografiche. È una buona scelta per la prototipazione, ma per i tipi di grafici necessari si raccomandano strumenti più avanzati.

---

### 3. **ApexCharts**

**Panoramica**:  
ApexCharts è una libreria di grafici moderna che offre una gamma di tipi di grafici e si concentra su visualizzazioni interattive con un'API facile da usare.

**Punti di forza**:
- **Funzionalità interattive**: ApexCharts offre grafici interattivi con suggerimenti, zoom, panoramica e aggiornamenti.
- **Supporto per grafici finanziari e scientifici**: supporta un'ampia gamma di tipi di grafici, inclusi grafici a candela, grafici radar e grafici ad area.
- **Facilità d'uso**: ha un'API semplice ed è facile da integrare in un progetto.
- **Gratuita e open source**: ApexCharts offre una versione gratuita e open source adatta a molti casi d'uso.
  
**Punti deboli**:
- **Personalizzazione complessa**: sebbene offra molte funzionalità, le opzioni di personalizzazione non sono flessibili come ECharts o D3.js per esigenze di grafici molto complesse o personalizzate.
- **Mappe geografiche**: ApexCharts non supporta in modo nativo mappe geografiche o grafici del processo di clustering, che sono richiesti per questo progetto.

**Giudizio**:  
ApexCharts è un forte candidato grazie alla sua facilità d'uso e interattività, ma è carente in alcuni tipi di grafici avanzati, in particolare l'esigenza di mappe geografiche e grafici di clustering. È una buona alternativa per grafici più semplici ma manca di alcune funzionalità necessarie.

---

### 4. **AG Charts**

**Panoramica**:  
AG Charts è una libreria di grafici di qualità commerciale, progettata per prestazioni e precisione. È molto adatta a creare dashboard finanziarie, scientifiche e aziendali.

**Punti di forza**:
- **Tipi di grafici avanzati**: AG Charts supporta molti tipi di grafici avanzati, inclusi grafici a candela, grafici ad area, grafici radar e altro. Offre anche una profonda integrazione con altri prodotti AG-Grid.
- **Alte prestazioni**: offre prestazioni eccellenti, specialmente nella gestione di grandi insiemi di dati.
- **Interattività**: AG Charts supporta una serie di funzionalità interattive come zoom, suggerimenti e aggiornamenti dinamici.

**Punti deboli**:
- **Non del tutto gratuita**: sebbene AG Charts offra una versione gratuita, la versione completa è a pagamento, il che può essere un ostacolo per le startup che vogliono ridurre al minimo i costi.
- **Complessità**: sebbene la libreria sia ricca di funzionalità, può essere eccessiva per progetti più semplici e può richiedere più configurazione e impostazione rispetto ad altre opzioni.

**Giudizio**:  
AG Charts è potente e ricca di funzionalità, ma potrebbe non essere la scelta migliore a causa della sua natura commerciale e della struttura dei costi. La sua idoneità dipende dal fatto che il budget possa accogliere versioni a pagamento o che si preferiscano alternative open source.

---

### 5. **Highcharts**

**Panoramica**:  
Highcharts è una popolare libreria di grafici nota per la sua ampia gamma di tipi di grafici e le potenti opzioni di personalizzazione.

**Punti di forza**:
- **Tipi di grafici completi**: Highcharts supporta un'ampia gamma di grafici, inclusi grafici a candela, radar, ad area e mappe geografiche.
- **Interattiva e dinamica**: Highcharts offre ricche funzionalità interattive, inclusi drill-down, zoom e panoramica.
- **Facilità d'uso**: ha un'API amichevole e una buona documentazione, il che rende facile iniziare.

**Punti deboli**:
- **Licenza commerciale**: sebbene Highcharts offra una versione gratuita per uso non commerciale, la licenza commerciale è costosa, il che può essere uno svantaggio significativo per le startup.
- **Curva di apprendimento**: sebbene non sia ripida come quella di ECharts, la curva di apprendimento di Highcharts può comunque essere impegnativa per i principianti.

**Giudizio**:  
Highcharts è una libreria ricca di funzionalità, ma la sua licenza commerciale la rende meno adatta a progetti open source sensibili ai costi. Le sue ampie opzioni di grafici sono un punto a favore, ma la questione della licenza ne limita l'attrattiva per questo caso d'uso.

---

### 6. **Carbon Charts**

**Panoramica**:  
Carbon Charts è una libreria di grafici sviluppata da IBM, progettata per creare grafici visivamente accattivanti e altamente personalizzabili.

**Punti di forza**:
- **Personalizzabilità**: Carbon Charts consente un'ampia personalizzazione dell'aspetto e del comportamento dei grafici.
- **Open source**: è gratuita e open source, il che è in linea con il requisito del progetto di soluzioni economiche.
- **Supporto per grafici comuni**: supporta tipi di grafici comuni come grafici ad anello, radar e ad area, ma manca di supporto per tipi più avanzati come mappe geografiche o grafici a candela.

**Punti deboli**:
- **Tipi di grafici avanzati limitati**: non supporta mappe geografiche, grafici del processo di clustering o grafici a candela, che sono necessari per il progetto.
- **Ecosistema più piccolo**: Carbon Charts ha una comunità e un ecosistema più piccoli rispetto a librerie di grafici più grandi come ECharts o Highcharts.

**Giudizio**:  
Carbon Charts è open source e personalizzabile ma manca di supporto per i tipi di grafici più complessi necessari per questo progetto. È più adatta a esigenze di grafici più semplici.

---

### 7. **Layer Cake**

**Panoramica**:  
Layer Cake è una libreria di visualizzazione dei dati progettata per creare visualizzazioni flessibili e stratificate.

**Punti di forza**:
- **Livelli personalizzabili**: offre potenti opzioni di stratificazione per visualizzazioni complesse.
- **Open source**: è gratuita e open source, il che la rende un'opzione praticabile per progetti attenti al budget.

**Punti deboli**:
- **Documentazione limitata**: Layer Cake manca di documentazione estesa e di supporto della comunità, il che la rende più difficile da usare rispetto a librerie più consolidate.
- **Non costruita per i grafici**: Layer Cake è più adatta a visualizzazioni che non sono grafici, quindi le sue opzioni di grafici pronte all'uso sono limitate.

**Giudizio**:  
Sebbene interessante per visualizzazioni uniche, Layer Cake non è ideale per i requisiti tradizionali di grafici come grafici a candela o grafici radar. È più adatta a visualizzazioni personalizzate al di fuori dell'ambito dei grafici standard.

---

### 8. **D3.js**

**Panoramica**:  
D3.js è una potente libreria JavaScript per creare visualizzazioni basate sui dati tramite HTML, SVG e CSS.

**Punti di forza**:
- **Flessibilità ineguagliata**: D3.js consente di creare praticamente qualsiasi tipo di visualizzazione personalizzata, il che la rende molto potente per grafici avanzati e interattivi.
- **Funzionalità complete**: supporta tutti i tipi di grafici necessari, comprese mappe geografiche, grafici di clustering e altro.
- **Personalizzabile**: il livello di personalizzazione in D3.js è ineguagliato, il che permette agli sviluppatori di costruire visualizzazioni molto su misura.

**Punti deboli**:
- **Curva di apprendimento ripida**: D3.js ha una curva di apprendimento ripida ed è più complessa da integrare rispetto ad altre librerie.
- **Richiede tempo**: costruire grafici in D3.js può richiedere molto tempo, specialmente per grafici comuni come grafici a candela o ad anello.

**Giudizio**:  
D3.js è incredibilmente potente per grafici avanzati e personalizzati, ma eccessiva per molti casi d'uso tipici a causa della sua curva di apprendimento ripida e del tempo di sviluppo. È ideale per situazioni in cui le altre librerie di grafici non offrono il livello di personalizzazione necessario.

---

### Conclusione

Dopo aver valutato le librerie in base alle esigenze del progetto, **Apache ECharts** emerge come l'opzione migliore. Supporta l'intero spettro di grafici necessari, comprese mappe geografiche, grafici a candela e grafici di clustering. È open source, ricca di funzionalità e altamente interattiva, il che si allinea perfettamente con gli obiettivi del progetto. Sebbene **D3.js** offra la massima flessibilità, la sua complessità e l'investimento di tempo la rendono meno ideale per una startup che vuole iterare rapidamente. **ApexCharts** e **Chart.js** sono buone alternative per progetti più semplici ma mancano di supporto per tipi di grafici avanzati.
