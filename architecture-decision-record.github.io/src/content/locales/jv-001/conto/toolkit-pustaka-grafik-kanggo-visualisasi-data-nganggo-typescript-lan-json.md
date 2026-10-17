# Cathetan Keputusan Arsitektur: toolkit pustaka grafik kanggo visualisasi data nganggo TypeScript lan JSON

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

**Tujuan Utama:**  
Milih toolkit grafik canggih kanggo nggawe visualisasi interaktif, kanthi fokus ing data finansial, data ilmiah, lan data pamarentah nganggo TypeScript lan JSON. Pustaka kudu nyedhiyakake fitur kuwat, keluwesan, lan open-source. 

### Konteks lan Kabutuhan:

1. **Pangembangan Gesit (Prioritas Dhuwur)**: Minangka startup, iterasi cepet, prototipe, lan keluwesan ing pangembangan iku penting. Pustaka grafik kudu ngidini siklus pangembangan sing cepet.
   
2. **Jinis Grafik (Prioritas Dhuwur)**:
   - **Grafik Doughnut**
   - **Grafik Radar**
   - **Grafik Proses Clustering**
   - **Grafik Area nganggo Sumbu Wektu**
   - **Grafik Candlestick**
   - **Grafik Nightingale**
   - **Peta SVG Geo**
   
   Jinis-jinis grafik iki utamane penting kanggo visualisasi dataset kompleks, kayata tren finansial, metrik ilmiah, lan informasi geografis.

3. **Gratis lan Open Source (Prioritas Dhuwur)**: Toolkit kudu open-source kanggo nyingkiri biaya lisensi, menehi transparansi, lan nawakake keluwesan kanggo kustomisasi.

4. **Kriteria Prioritas Andhap**:
   - **Kacepetan Runtime**: Sanajan kinerja penting, dudu prioritas paling dhuwur kanggo keputusan iki.
   - **Skalabilitas**: Sanajan skalabilitas umume penting, kabutuhan langsung yaiku mbangun MVP sing bisa tuwuh saka wektu. Kuwatir skalabilitas bisa ditanggapi mengko.
   - **Kompatibilitas Mundur**: Dudu kuwatir utama kanggo pambangunan wiwitan, salawase pustaka modern lan dirawat aktif.

### Pustaka sing Dievaluasi:

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

**Ringkesan**:  
Apache ECharts yaiku pustaka grafik sing kuwat lan fleksibel kanggo visualisasi interaktif lan bisa disesuekake. Dheweke ndhukung macem-macem grafik lan utamane kuwat ing visualisasi dinamis sing kompleks.

**Kekuwatan**:
- **Interaktivitas Canggih**: ECharts unggul ing nyedhiyakake grafik interaktif, nawakake fitur kayata zoom, panning, lan pembaruan data dinamis.
- **Doughnut, Radar, Candlestick, Peta SVG Geo**: ECharts ndhukung akeh jinis grafik sing dibutuhake, kalebu doughnut, radar, candlestick, lan visualisasi peta geografis.
- **Gratis lan Open Source**: ECharts yaiku pustaka open-source, sing cocog karo sifat hemat anggaran startup lan menehi kebebasan ngowahi kode.
- **Keluwesan lan Kemampuan Ekstensi**: Bisa disesuekake banget, kanthi dhukungan ekstensif kanggo animasi, visualisasi khusus, lan teknik grafik canggih.
  
**Kelemahan**:
- **Kurva Sinau**: ECharts, sanajan kuwat, bisa nduwe kurva sinau sing luwih curam amarga keluwesan lan API sing ekstensif.
- **Kerumitan Dokumentasi**: Dokumentasi lengkap nanging bisa mbebayani kanggo pangembang sing lagi miwiti.

**Putusan**:  
ECharts cocog banget kanggo proyek amarga dhukungan grafik interaktif, kalebu kabeh jinis sing dibutuhake kayata grafik candlestick, grafik radar, lan peta geo. Sifat open-source cocog karo kabutuhan proyek kanggo keluwesan lan efektivitas biaya.

---

### 2. **Chart.js**

**Ringkesan**:  
Chart.js yaiku pustaka grafik prasaja lan gampang digunakake kanggo mbangun jinis grafik umum. Dikenal amarga kasederhanan lan gampang diintegrasi.

**Kekuwatan**:
- **Gampang Digunakake**: Chart.js prasaja banget disetel lan digunakake, kanthi kurva sinau minimal.
- **Open Source**: Chart.js gratis lan open-source, sing kritis kanggo nyuda biaya.
- **Jinis Grafik Umum**: Dheweke ndhukung grafik dhasar kayata doughnut, area, radar, lan grafik garis, sing nyakup umume kabutuhan utama.

**Kelemahan**:
- **Grafik Canggih sing Winates**: Chart.js ora ndhukung sacara asli jinis grafik kompleks kayata grafik candlestick, peta SVG geo, utawa grafik proses clustering. Sanajan fitur-fitur iki bisa ditambah liwat plugin utawa kustomisasi, ora sagampang karo pustaka liyane.
- **Interaktivitas**: Sanajan Chart.js ndhukung interaktivitas dhasar (upamane tooltip lan efek hover), dheweke ora nawakake fitur sacanggih ECharts utawa D3.js.

**Putusan**:  
Chart.js apik kanggo proyek prasaja lan cepet, nanging kurang dhukungan kanggo jinis grafik kompleks ndadekake dheweke ora cocog kanggo aplikasi abot data kanthi kabutuhan canggih kayata grafik candlestick lan peta geo. Iki pilihan apik kanggo prototipe, nanging kanggo jinis grafik sing dibutuhake, piranti sing luwih canggih disaranake.

---

### 3. **ApexCharts**

**Ringkesan**:  
ApexCharts yaiku pustaka grafik modern sing nyedhiyakake macem-macem jinis grafik lan fokus ing visualisasi interaktif kanthi API sing gampang digunakake.

**Kekuwatan**:
- **Fitur Interaktif**: ApexCharts nawakake grafik interaktif kanthi tooltip, zoom, panning, lan pembaruan.
- **Dhukungan kanggo Grafik Finansial lan Ilmiah**: Dheweke ndhukung macem-macem jinis grafik, kalebu grafik candlestick, grafik radar, lan grafik area.
- **Gampang Digunakake**: Nduwe API sing lugas lan gampang diintegrasi menyang proyek.
- **Gratis lan Open Source**: ApexCharts nawakake versi open-source gratis sing cocog kanggo akeh kasus panggunaan.
  
**Kelemahan**:
- **Kustomisasi Kompleks**: Sanajan nyedhiyakake akeh fitur, pilihan kustomisasi ora sakfleksibel ECharts utawa D3.js kanggo kabutuhan grafik sing kompleks utawa khusus banget.
- **Peta Geo**: ApexCharts ora ndhukung sacara asli peta geo utawa grafik proses clustering, sing dibutuhake kanggo proyek iki.

**Putusan**:  
ApexCharts yaiku calon kuwat amarga gampang digunakake lan interaktivitase, nanging kurang ing jinis grafik canggih tartamtu, utamane kabutuhan peta geo lan grafik clustering. Iki pilihan apik kanggo grafik sing luwih prasaja nanging kurang sawetara fitur sing dibutuhake.

---

### 4. **AG Charts**

**Ringkesan**:  
AG Charts yaiku pustaka grafik kelas komersial sing dirancang kanggo kinerja lan presisi. Cocog banget kanggo nggawe dashboard finansial, ilmiah, lan bisnis.

**Kekuwatan**:
- **Jinis Grafik Canggih**: AG Charts ndhukung akeh jinis grafik canggih, kalebu grafik candlestick, grafik area, grafik radar, lan liya-liyane. Dheweke uga nawakake integrasi jero karo produk AG-Grid liyane.
- **Kinerja Dhuwur**: Dheweke nawakake kinerja apik banget, utamane nalika nangani dataset gedhe.
- **Interaktivitas**: AG Charts ndhukung macem-macem fitur interaktif kayata zoom, tooltip, lan pembaruan dinamis.

**Kelemahan**:
- **Ora Gratis Kebak**: Sanajan AG Charts nawakake versi gratis, versi sugih fitur mbayar, sing bisa dadi alangan kanggo startup sing pengin nyuda biaya.
- **Kerumitan**: Sanajan pustaka sugih fitur, mbok menawa kakehan kanggo proyek prasaja lan bisa mbutuhake setelan lan konfigurasi luwih akeh dibandhingake pilihan liyane.

**Putusan**:  
AG Charts kuwat lan sugih fitur nanging mbok menawa dudu sing paling cocog amarga sifat komersial lan struktur biayane. Kecocogane gumantung apa anggaran bisa nampung versi mbayar utawa alternatif open-source luwih disenengi.

---

### 5. **Highcharts**

**Ringkesan**:  
Highcharts yaiku pustaka grafik populer sing dikenal amarga macem-macem jinis grafik lan pilihan kustomisasi sing kuwat.

**Kekuwatan**:
- **Jinis Grafik Lengkap**: Highcharts ndhukung macem-macem grafik, kalebu candlestick, radar, area, lan peta geo.
- **Interaktif lan Dinamis**: Highcharts nyedhiyakake fitur interaktif sing sugih, kalebu drill-down, zoom, lan panning.
- **Gampang Digunakake**: Nduwe API ramah pangguna lan dokumentasi apik, nggampangake miwiti.

**Kelemahan**:
- **Lisensi Komersial**: Sanajan Highcharts nawakake versi gratis kanggo panggunaan non-komersial, lisensi komersial larang, sing bisa dadi kekurangan signifikan kanggo startup.
- **Kurva Sinau**: Sanajan ora sacuram ECharts, kurva sinau Highcharts isih bisa nantang kanggo pamula.

**Putusan**:  
Highcharts yaiku pustaka sugih fitur, nanging lisensi komersiale ndadekake dheweke kurang cocog kanggo proyek open-source sing sensitif biaya. Pilihan grafik sing lengkap iku kaluwihan, nanging masalah lisensi mbatesi daya tarike kanggo kasus panggunaan iki.

---

### 6. **Carbon Charts**

**Ringkesan**:  
Carbon Charts yaiku pustaka grafik sing dikembangake dening IBM, dirancang kanggo nggawe grafik sing narik kawigaten sacara visual lan bisa disesuekake banget.

**Kekuwatan**:
- **Bisa Disesuekake**: Carbon Charts ngidini kustomisasi ekstensif marang tampilan lan prilaku grafik.
- **Open Source**: Gratis lan open-source, sing cocog karo kabutuhan proyek kanggo solusi hemat anggaran.
- **Dhukungan kanggo Grafik Umum**: Dheweke ndhukung jinis grafik umum kayata doughnut, radar, lan grafik area, sanajan kurang dhukungan kanggo jinis sing luwih canggih kayata peta geo utawa grafik candlestick.

**Kelemahan**:
- **Jinis Grafik Canggih sing Winates**: Dheweke ora ndhukung peta geo, grafik proses clustering, utawa grafik candlestick, sing penting kanggo proyek.
- **Ekosistem Luwih Cilik**: Carbon Charts nduwe komunitas lan ekosistem sing luwih cilik dibandhingake pustaka grafik sing luwih gedhe kayata ECharts utawa Highcharts.

**Putusan**:  
Carbon Charts open-source lan bisa disesuekake nanging kurang dhukungan kanggo jinis grafik sing luwih kompleks sing dibutuhake kanggo proyek iki. Dheweke luwih cocog kanggo kabutuhan grafik sing luwih prasaja.

---

### 7. **Layer Cake**

**Ringkesan**:  
Layer Cake yaiku pustaka visualisasi data sing dirancang kanggo nggawe visualisasi fleksibel lan berlapis.

**Kekuwatan**:
- **Lapisan sing Bisa Disesuekake**: Dheweke nyedhiyakake pilihan pelapisan sing kuwat kanggo visualisasi kompleks.
- **Open Source**: Gratis lan open-source, ndadekake pilihan sing bisa dilakoni kanggo proyek hemat anggaran.

**Kelemahan**:
- **Dokumentasi sing Winates**: Layer Cake kurang dokumentasi ekstensif lan dhukungan komunitas, ndadekake luwih angel makarya dibandhingake pustaka sing luwih mapan.
- **Ora Dibangun kanggo Grafik**: Layer Cake luwih cocog kanggo visualisasi non-grafik, mula pilihan grafik langsung saka kothak winates.

**Putusan**:  
Sanajan menarik kanggo visualisasi unik, Layer Cake ora ideal kanggo kabutuhan grafik tradisional kayata grafik candlestick utawa grafik radar. Dheweke luwih cocog kanggo visualisasi khusus ing njaba cakupan grafik standar.

---

### 8. **D3.js**

**Ringkesan**:  
D3.js yaiku pustaka JavaScript sing kuwat kanggo nggawe visualisasi sing didorong data liwat HTML, SVG, lan CSS.

**Kekuwatan**:
- **Keluwesan Tanpa Tandhingan**: D3.js ngidini nggawe meh sembarang jinis visualisasi khusus, ndadekake kuwat banget kanggo grafik canggih lan interaktif.
- **Fitur Ekstensif**: Dheweke ndhukung kabeh jinis grafik sing dibutuhake, kalebu peta geo, grafik clustering, lan liya-liyane.
- **Bisa Disesuekake**: Tingkat kustomisasi ing D3.js ora ana tandhingane, ngidini pangembang mbangun visualisasi sing disesuekake banget.

**Kelemahan**:
- **Kurva Sinau Curam**: D3.js nduwe kurva sinau sing curam lan luwih rumit diintegrasi dibandhingake pustaka liyane.
- **Mbutuhake Wektu**: Mbangun grafik ing D3.js bisa mbutuhake wektu akeh, utamane kanggo grafik umum kayata grafik candlestick utawa doughnut.

**Putusan**:  
D3.js kuwat banget kanggo grafik canggih lan khusus nanging kakehan kanggo akeh kasus panggunaan khas amarga kurva sinau sing curam lan wektu pangembangan. Paling apik kanggo kahanan ing ngendi pustaka grafik liyane ora nyedhiyakake tingkat kustomisasi sing dibutuhake.

---

### Kesimpulan

Sawise ngevaluasi pustaka-pustaka adhedhasar kabutuhan proyek, **Apache ECharts** katon minangka pilihan paling apik. Dheweke ndhukung rangkaian lengkap grafik sing dibutuhake, kalebu peta geo, grafik candlestick, lan grafik clustering. Open-source, sugih fitur, lan interaktif banget, sing cocog sampurna karo tujuan proyek. Sanajan **D3.js** nawakake keluwesan paling akeh, kerumitan lan investasi wektune ndadekake dheweke kurang ideal kanggo startup sing pengin iterasi kanthi cepet. **ApexCharts** lan **Chart.js** yaiku alternatif apik kanggo proyek sing luwih prasaja nanging kurang dhukungan kanggo jinis grafik canggih.
