# Catatan Keputusan Arsitektur: toolkit pustaka bagan untuk visualisasi data menggunakan TypeScript dan JSON

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
Memilih toolkit pembuatan bagan tingkat lanjut untuk membuat visualisasi interaktif, dengan fokus pada data keuangan, data ilmiah, dan data pemerintah menggunakan TypeScript dan JSON. Pustaka ini harus menyediakan fitur yang tangguh, fleksibilitas, dan bersifat sumber terbuka. 

### Konteks dan Persyaratan:

1. **Pengembangan Agile (Prioritas Tinggi)**: Sebagai startup, iterasi cepat, pembuatan prototipe, dan fleksibilitas dalam pengembangan sangat penting. Pustaka bagan harus memungkinkan siklus pengembangan yang cepat.
   
2. **Jenis Bagan (Prioritas Tinggi)**:
   - **Bagan Donat (Doughnut Chart)**
   - **Bagan Radar (Radar Chart)**
   - **Bagan Proses Pengelompokan (Clustering Process Chart)**
   - **Bagan Area dengan Sumbu Waktu (Area Chart with Time Axis)**
   - **Bagan Candlestick (Candlestick Chart)**
   - **Bagan Nightingale (Nightingale Chart)**
   - **Peta SVG Geografis (Geo SVG Map)**
   
   Jenis-jenis bagan ini secara khusus penting untuk memvisualisasikan kumpulan data yang kompleks, seperti tren keuangan, metrik ilmiah, dan informasi geografis.

3. **Gratis dan Sumber Terbuka (Prioritas Tinggi)**: Toolkit harus bersumber terbuka untuk menghindari biaya lisensi, menyediakan transparansi, dan menawarkan fleksibilitas untuk kustomisasi.

4. **Kriteria Prioritas Rendah**:
   - **Kecepatan Waktu Proses**: Meskipun kinerja penting, ini bukan prioritas utama untuk keputusan ini.
   - **Skalabilitas**: Meskipun skalabilitas umumnya penting, kebutuhan mendesak adalah membangun MVP yang dapat berkembang seiring waktu. Masalah skalabilitas dapat ditangani nanti.
   - **Kompatibilitas Mundur**: Bukan perhatian utama untuk pembangunan awal, selama pustaka tersebut modern dan dipelihara secara aktif.

### Pustaka yang Dievaluasi:

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

**Gambaran Umum**:  
Apache ECharts adalah pustaka bagan yang kuat dan fleksibel untuk visualisasi interaktif yang dapat dikustomisasi. Pustaka ini mendukung beragam jenis bagan dan sangat kuat dalam visualisasi yang kompleks dan dinamis.

**Kekuatan**:
- **Interaktivitas Lanjutan**: ECharts unggul dalam menyediakan bagan interaktif, menawarkan fitur seperti zoom, pan, dan pembaruan data dinamis.
- **Donat, Radar, Candlestick, Peta SVG Geografis**: ECharts mendukung banyak jenis bagan yang dibutuhkan, termasuk visualisasi donat, radar, candlestick, dan peta geografis.
- **Gratis dan Sumber Terbuka**: ECharts adalah pustaka sumber terbuka, yang sesuai dengan sifat startup yang sadar anggaran dan memberikan kebebasan untuk memodifikasi kode.
- **Fleksibilitas dan Ekstensibilitas**: Sangat dapat dikustomisasi, dengan dukungan luas untuk animasi, visualisasi kustom, dan teknik pembuatan bagan tingkat lanjut.
  
**Kelemahan**:
- **Kurva Belajar**: ECharts, meskipun kuat, dapat memiliki kurva belajar yang lebih curam karena fleksibilitas dan API-nya yang luas.
- **Kompleksitas Dokumentasi**: Dokumentasinya komprehensif tetapi bisa membuat kewalahan bagi pengembang yang baru mulai menggunakannya.

**Penilaian**:  
ECharts sangat cocok untuk proyek ini karena dukungannya untuk bagan interaktif, termasuk semua jenis yang dibutuhkan seperti bagan candlestick, bagan radar, dan peta geografis. Sifat sumber terbukanya selaras dengan kebutuhan proyek akan fleksibilitas dan efektivitas biaya.

---

### 2. **Chart.js**

**Gambaran Umum**:  
Chart.js adalah pustaka bagan yang sederhana dan mudah digunakan untuk membangun jenis bagan yang umum. Pustaka ini dikenal karena kesederhanaan dan kemudahan integrasinya.

**Kekuatan**:
- **Kemudahan Penggunaan**: Chart.js sangat sederhana untuk disiapkan dan digunakan, dengan kurva belajar minimal.
- **Sumber Terbuka**: Chart.js gratis dan bersumber terbuka, yang penting untuk mengurangi biaya.
- **Jenis Bagan Umum**: Pustaka ini mendukung bagan dasar seperti donat, area, radar, dan garis, yang mencakup sebagian besar kebutuhan utama.

**Kelemahan**:
- **Bagan Lanjutan Terbatas**: Chart.js tidak mendukung secara native jenis bagan kompleks seperti bagan candlestick, peta SVG geografis, atau bagan proses pengelompokan. Meskipun fitur-fitur ini dapat ditambahkan melalui plugin atau kustomisasi, hal itu tidak semudah pada pustaka lain.
- **Interaktivitas**: Meskipun Chart.js mendukung interaktivitas dasar (misalnya tooltip dan efek hover), pustaka ini tidak menawarkan fitur selengkap ECharts atau D3.js.

**Penilaian**:  
Chart.js sangat bagus untuk proyek yang sederhana dan cepat, tetapi kurangnya dukungan untuk jenis bagan kompleks membuatnya tidak cocok untuk aplikasi padat data dengan kebutuhan lanjutan seperti bagan candlestick dan peta geografis. Ini adalah pilihan yang baik untuk pembuatan prototipe, tetapi untuk jenis bagan yang dibutuhkan, alat yang lebih canggih direkomendasikan.

---

### 3. **ApexCharts**

**Gambaran Umum**:  
ApexCharts adalah pustaka bagan modern yang menyediakan berbagai jenis bagan dan berfokus pada visualisasi interaktif dengan API yang mudah digunakan.

**Kekuatan**:
- **Fitur Interaktif**: ApexCharts menawarkan bagan interaktif dengan tooltip, zoom, pan, dan pembaruan.
- **Dukungan untuk Bagan Keuangan dan Ilmiah**: Pustaka ini mendukung beragam jenis bagan, termasuk bagan candlestick, bagan radar, dan bagan area.
- **Kemudahan Penggunaan**: Pustaka ini memiliki API yang lugas dan mudah diintegrasikan ke dalam proyek.
- **Gratis dan Sumber Terbuka**: ApexCharts menawarkan versi sumber terbuka gratis yang cocok untuk banyak kasus penggunaan.
  
**Kelemahan**:
- **Kustomisasi Kompleks**: Meskipun menyediakan banyak fitur, opsi kustomisasinya tidak sefleksibel ECharts atau D3.js untuk kebutuhan pembuatan bagan yang sangat kompleks atau kustom.
- **Peta Geografis**: ApexCharts tidak mendukung secara native peta geografis atau bagan proses pengelompokan, yang dibutuhkan untuk proyek ini.

**Penilaian**:  
ApexCharts adalah kandidat yang kuat karena kemudahan penggunaan dan interaktivitasnya, tetapi kurang pada jenis bagan lanjutan tertentu, terutama kebutuhan akan peta geografis dan bagan pengelompokan. Ini adalah opsi yang baik untuk bagan yang lebih sederhana tetapi kekurangan beberapa fitur yang dibutuhkan.

---

### 4. **AG Charts**

**Gambaran Umum**:  
AG Charts adalah pustaka bagan kelas komersial yang dirancang untuk kinerja dan presisi. Pustaka ini sangat cocok untuk membuat dasbor keuangan, ilmiah, dan bisnis.

**Kekuatan**:
- **Jenis Bagan Lanjutan**: AG Charts mendukung banyak jenis bagan lanjutan, termasuk bagan candlestick, bagan area, bagan radar, dan lainnya. Pustaka ini juga menawarkan integrasi mendalam dengan produk AG-Grid lainnya.
- **Kinerja Tinggi**: Pustaka ini menawarkan kinerja yang sangat baik, terutama saat menangani kumpulan data besar.
- **Interaktivitas**: AG Charts mendukung berbagai fitur interaktif seperti zoom, tooltip, dan pembaruan dinamis.

**Kelemahan**:
- **Tidak Sepenuhnya Gratis**: Meskipun AG Charts menawarkan versi gratis, versi berfitur lengkap berbayar, yang dapat menjadi hambatan bagi startup yang ingin meminimalkan biaya.
- **Kompleksitas**: Meskipun pustaka ini kaya fitur, pustaka ini mungkin berlebihan untuk proyek yang lebih sederhana dan dapat memerlukan lebih banyak penyiapan dan konfigurasi dibandingkan opsi lain.

**Penilaian**:  
AG Charts kuat dan kaya fitur tetapi mungkin bukan yang paling cocok karena sifat komersial dan struktur biayanya. Kesesuaiannya bergantung pada apakah anggaran dapat menampung versi berbayar atau apakah alternatif sumber terbuka lebih disukai.

---

### 5. **Highcharts**

**Gambaran Umum**:  
Highcharts adalah pustaka bagan populer yang dikenal dengan beragam jenis bagan dan opsi kustomisasi yang kuat.

**Kekuatan**:
- **Jenis Bagan Komprehensif**: Highcharts mendukung beragam bagan, termasuk candlestick, radar, area, dan peta geografis.
- **Interaktif dan Dinamis**: Highcharts menyediakan fitur interaktif yang kaya, termasuk drill-down, zoom, dan pan.
- **Kemudahan Penggunaan**: Pustaka ini memiliki API yang ramah pengguna dan dokumentasi yang baik, sehingga mudah untuk memulai.

**Kelemahan**:
- **Lisensi Komersial**: Meskipun Highcharts menawarkan versi gratis untuk penggunaan nonkomersial, lisensi komersialnya mahal, yang dapat menjadi kerugian signifikan bagi startup.
- **Kurva Belajar**: Meskipun tidak securam ECharts, kurva belajar Highcharts masih bisa menantang bagi pemula.

**Penilaian**:  
Highcharts adalah pustaka yang kaya fitur, tetapi lisensi komersialnya membuatnya kurang cocok untuk proyek sumber terbuka yang sensitif terhadap biaya. Opsi pembuatan bagannya yang komprehensif adalah nilai tambah, tetapi masalah lisensi membatasi daya tariknya untuk kasus penggunaan ini.

---

### 6. **Carbon Charts**

**Gambaran Umum**:  
Carbon Charts adalah pustaka bagan yang dikembangkan oleh IBM, dirancang untuk membuat bagan yang menarik secara visual dan sangat dapat dikustomisasi.

**Kekuatan**:
- **Kemampuan Kustomisasi**: Carbon Charts memungkinkan kustomisasi luas atas tampilan dan perilaku bagan.
- **Sumber Terbuka**: Pustaka ini gratis dan bersumber terbuka, yang selaras dengan persyaratan proyek akan solusi yang ramah anggaran.
- **Dukungan untuk Bagan Umum**: Pustaka ini mendukung jenis bagan umum seperti donat, radar, dan bagan area, meskipun tidak mendukung jenis yang lebih canggih seperti peta geografis atau bagan candlestick.

**Kelemahan**:
- **Jenis Bagan Lanjutan Terbatas**: Pustaka ini tidak mendukung peta geografis, bagan proses pengelompokan, atau bagan candlestick, yang penting untuk proyek ini.
- **Ekosistem Lebih Kecil**: Carbon Charts memiliki komunitas dan ekosistem yang lebih kecil dibandingkan pustaka bagan yang lebih besar seperti ECharts atau Highcharts.

**Penilaian**:  
Carbon Charts bersumber terbuka dan dapat dikustomisasi tetapi tidak memiliki dukungan untuk jenis bagan yang lebih kompleks yang dibutuhkan proyek ini. Pustaka ini lebih cocok untuk kebutuhan pembuatan bagan yang lebih sederhana.

---

### 7. **Layer Cake**

**Gambaran Umum**:  
Layer Cake adalah pustaka visualisasi data yang dirancang untuk membuat visualisasi berlapis yang fleksibel.

**Kekuatan**:
- **Lapisan yang Dapat Dikustomisasi**: Pustaka ini menyediakan opsi pelapisan yang kuat untuk visualisasi yang kompleks.
- **Sumber Terbuka**: Pustaka ini gratis dan bersumber terbuka, menjadikannya opsi yang layak untuk proyek yang sadar anggaran.

**Kelemahan**:
- **Dokumentasi Terbatas**: Layer Cake tidak memiliki dokumentasi dan dukungan komunitas yang luas, sehingga lebih sulit digunakan dibandingkan pustaka yang lebih mapan.
- **Tidak Dibuat untuk Bagan**: Layer Cake lebih cocok untuk visualisasi non-bagan, sehingga opsi pembuatan bagan bawaannya terbatas.

**Penilaian**:  
Meskipun menarik untuk visualisasi yang unik, Layer Cake tidak ideal untuk kebutuhan pembuatan bagan tradisional seperti bagan candlestick atau bagan radar. Pustaka ini lebih cocok untuk visualisasi kustom di luar lingkup bagan standar.

---

### 8. **D3.js**

**Gambaran Umum**:  
D3.js adalah pustaka JavaScript yang kuat untuk membuat visualisasi berbasis data melalui HTML, SVG, dan CSS.

**Kekuatan**:
- **Fleksibilitas Tak Tertandingi**: D3.js memungkinkan pembuatan hampir semua jenis visualisasi kustom, menjadikannya sangat kuat untuk bagan lanjutan dan interaktif.
- **Fitur Luas**: Pustaka ini mendukung semua jenis bagan yang dibutuhkan, termasuk peta geografis, bagan pengelompokan, dan lainnya.
- **Dapat Dikustomisasi**: Tingkat kustomisasi di D3.js tidak tertandingi, memungkinkan pengembang membangun visualisasi yang sangat disesuaikan.

**Kelemahan**:
- **Kurva Belajar yang Curam**: D3.js memiliki kurva belajar yang curam dan lebih kompleks untuk diintegrasikan dibandingkan pustaka lain.
- **Memakan Waktu**: Membuat bagan di D3.js bisa memakan waktu, terutama untuk bagan umum seperti candlestick atau donat.

**Penilaian**:  
D3.js sangat kuat untuk bagan lanjutan yang disesuaikan tetapi berlebihan untuk banyak kasus penggunaan yang umum karena kurva belajarnya yang curam dan waktu pengembangannya. Pustaka ini paling cocok untuk situasi di mana pustaka bagan lain tidak menyediakan tingkat kustomisasi yang dibutuhkan.

---

### Kesimpulan

Setelah mengevaluasi pustaka berdasarkan kebutuhan proyek, **Apache ECharts** menonjol sebagai opsi terbaik. Pustaka ini mendukung rangkaian lengkap bagan yang dibutuhkan, termasuk peta geografis, bagan candlestick, dan bagan pengelompokan. Pustaka ini bersumber terbuka, kaya fitur, dan sangat interaktif, yang selaras sempurna dengan tujuan proyek. Meskipun **D3.js** menawarkan fleksibilitas paling besar, kompleksitas dan investasi waktunya membuatnya kurang ideal bagi startup yang ingin beriterasi dengan cepat. **ApexCharts** dan **Chart.js** adalah alternatif yang baik untuk proyek yang lebih sederhana tetapi tidak memiliki dukungan untuk jenis bagan lanjutan.
