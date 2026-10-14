## Catatan keputusan arsitektur: kerangka otomatisasi browser untuk pengujian E2E (Playwright vs Selenium)

### 1. **Konteks**

Kami sedang dalam proses memilih kerangka otomatisasi browser untuk pipeline pengujian end-to-end (E2E) kami. Kerangka ini akan menjadi bagian integral dari proses CI/CD kami, menjalankan pengujian yang mensimulasikan interaksi pengguna nyata pada platform kami. Secara khusus, pengujian akan mencakup skenario seperti pendaftaran/masuk pengguna, unggah file, interaksi dasbor, dan pengunduhan laporan.

Sebagai **startup**, fokus kami adalah **pengembangan agile**, dengan kebutuhan untuk beriterasi dan berkembang dengan cepat. Tim kami terutama bekerja dengan **TypeScript** dan **Python**, dan kemampuan menulis pengujian dalam bahasa-bahasa ini sangat penting. Selain itu, platform ini memiliki **bagan dan dasbor interaktif**, sehingga sangat penting agar alat otomatisasi mendukung UI yang kaya dan dinamis dengan baik.

Dua kandidat untuk tugas ini adalah **Playwright** dan **Selenium**, masing-masing dengan kekuatan dan trade-off tersendiri. Kami perlu mengevaluasi kerangka-kerangka ini berdasarkan fitur dan persyaratan yang diuraikan di bawah.

### 2. **Opsi yang Dipertimbangkan**

- **Playwright** (oleh Microsoft)
- **Selenium** (oleh Selenium Project)

### 3. **Pendorong Keputusan**

Faktor-faktor yang memengaruhi keputusan kami adalah sebagai berikut:

1. **Pengembangan Agile**: Alat yang dipilih harus memungkinkan siklus pengembangan yang cepat dan fleksibel.
2. **Dukungan Bahasa**: Tim kami memerlukan dukungan untuk **TypeScript** dan **Python**.
3. **Pengujian UI Interaktif**: Kemampuan menguji bagan, dasbor, dan elemen dinamis yang interaktif secara andal sangat penting.
4. **Kecepatan Waktu Proses**: Meskipun bukan perhatian utama, kinerja dalam pipeline CI/CD menjadi pertimbangan.
5. **Skalabilitas**: Kami tidak merencanakan penskalaan besar-besaran dalam waktu dekat, tetapi kami ingin memastikan solusi dapat menangani pertumbuhan di masa depan.
6. **Kompatibilitas Mundur**: Sistem lama dan kompatibilitas dengan browser lama tidak kritis bagi proyek kami saat ini.
7. **Pengujian Seluler**: Meskipun bukan fokus langsung, kerangka ini harus mampu menguji fitur responsif seluler atau dapat diperluas untuk kasus penggunaan tersebut.
8. **Pengujian Multi-monitor**: Dukungan untuk konfigurasi multi-monitor adalah persyaratan sekunder, terutama jika suatu saat kami meningkat ke pengujian alur kerja pengguna yang lebih kompleks.
9. **Pengujian Unggah File**: Kerangka ini harus menangani unggah file secara efisien, yang merupakan persyaratan inti dari kebutuhan pengujian kami.

### 4. **Kriteria Evaluasi**

- **Kemudahan Penggunaan**: Seberapa mudah menulis dan memelihara pengujian?
- **Dukungan Bahasa**: Apakah kerangka ini mendukung TypeScript dan Python, dua bahasa yang paling sering digunakan tim kami?
- **Pengujian UI Interaktif**: Seberapa baik kerangka ini menangani antarmuka pengguna yang kompleks dan interaktif seperti bagan, unggah file, dan data dinamis?
- **Integrasi CI/CD**: Seberapa baik kerangka ini terintegrasi ke dalam alat dan layanan CI/CD yang umum?
- **Dukungan Lintas Browser**: Browser apa yang didukung dan seberapa baik kinerjanya?
- **Kinerja dan Kecepatan**: Seberapa cepat pengujian berjalan, terutama dalam pipeline CI/CD?
- **Skalabilitas**: Seberapa baik kerangka ini dapat diskalakan jika lebih banyak pengujian atau skenario yang lebih kompleks ditambahkan?
- **Komunitas dan Ekosistem**: Seberapa aktif komunitas kerangka ini? Apakah banyak integrasi dan ekstensi tersedia?

### 5. **Pertimbangan**

#### 5.1 **Playwright**

##### **Kelebihan**:
1. **API yang Lebih Cerdas untuk Unggah File Lokal**: API Playwright untuk berinteraksi dengan file lokal dan melakukan unggah file lebih sederhana dan intuitif. Hal ini akan memudahkan implementasi dan pemeliharaan pengujian unggah file.
2. **Sintaksis dan Pembuatan Kode**: Playwright memiliki sintaksis yang lebih pendek dan ringkas. Hal ini menghasilkan lebih sedikit kode boilerplate, yang meningkatkan kemudahan pemeliharaan dan efisiensi pengembang. Selain itu, sintaksis yang lebih pendek ini meningkatkan kualitas pembuatan kode oleh OpenAI, sehingga lebih mudah menghasilkan skrip pengujian secara otomatis.
3. **Pengujian UI Interaktif**: Playwright unggul dalam menguji aplikasi web yang dinamis dan interaktif, seperti yang memiliki bagan yang kaya, interaksi pengguna yang kompleks, dan pembaruan real-time. Playwright menangani WebSockets, WebRTC, shadow DOM, dan teknologi web modern lainnya dengan sangat efektif.
4. **Dukungan Lintas Browser**: Playwright mendukung **Chromium**, **WebKit**, dan **Firefox**. Kinerjanya konsisten di seluruh browser ini, yang seharusnya mencakup sebagian besar kebutuhan pengujian kami.
5. **Integrasi CI/CD**: Playwright terintegrasi mulus dengan platform CI/CD modern (GitHub Actions, Jenkins, dll.). Playwright dapat menjalankan pengujian secara paralel di berbagai browser, mengoptimalkan waktu eksekusi pengujian dan menjadikannya cocok untuk pengembangan cepat.
6. **Cepat dan Andal**: Playwright umumnya lebih cepat daripada Selenium, terutama dalam mode headless, dan lebih tangguh dalam menangani elemen web asinkron.

##### **Kekurangan**:
1. **Pengujian Seluler Terbatas**: Meskipun Playwright mendukung emulasi seluler untuk browser, Playwright tidak memiliki kemampuan pengujian seluler native seperti integrasi Selenium dengan Appium untuk pengujian seluler sejati.
2. **Ekosistem Lebih Kecil**: Playwright masih lebih baru dan kurang mapan dibandingkan Selenium. Meskipun memiliki komunitas yang berkembang pesat dan dokumentasi yang baik, Playwright mungkin belum memiliki ekosistem plugin dan integrasi seluas yang ditawarkan Selenium.
3. **Dukungan Browser Terbatas**: Meskipun Playwright mencakup browser modern utama (Chrome, Safari, Firefox), dukungannya untuk browser lama (misalnya Internet Explorer) tidak sekuat Selenium.

#### 5.2 **Selenium**

##### **Kelebihan**:
1. **Sejarah Lebih Panjang dan Kematangan**: Selenium sudah ada sejak lama dan memiliki rekam jejak yang terbukti. Selenium banyak digunakan oleh berbagai tim dan industri, yang telah menghasilkan ekosistem plugin, integrasi, dan sumber daya yang luas.
2. **Dukungan Lintas Browser dan Lintas Platform**: Selenium mendukung **beragam browser** dan versi, termasuk **Internet Explorer**, dan juga dapat diintegrasikan dengan berbagai alat seperti **Docker**, **Selenium Grid**, dan **layanan cloud** untuk pengujian terdistribusi.
3. **Pengujian Seluler**: Selenium, melalui integrasinya dengan **Appium**, jauh lebih tangguh untuk pengujian seluler, termasuk aplikasi Android maupun iOS. Hal ini menjadikannya pilihan yang lebih baik untuk proyek yang mengutamakan seluler atau sangat bergantung pada seluler.
4. **Pengujian Multi-monitor**: Selenium memberikan dukungan yang lebih baik untuk skenario yang melibatkan **banyak monitor** atau interaksi multi-jendela yang kompleks.

##### **Kekurangan**:
1. **Kompleksitas**: API Selenium lebih panjang dan eksplisit. Meskipun hal ini bisa menjadi keuntungan dalam beberapa kasus, artinya lebih banyak kode yang harus ditulis dan dipelihara, yang dapat mengurangi ketangkasan pengembang, terutama penting di lingkungan startup.
2. **Kinerja**: Selenium umumnya berjalan lebih lambat daripada Playwright, terutama dalam mode headless. Hal ini dapat memengaruhi pipeline CI/CD, terutama seiring bertambahnya jumlah pengujian.
3. **Pengujian UI Interaktif**: Selenium tidak semulus Playwright dalam menguji UI web modern yang interaktif, terutama dengan bagan dan pembaruan data real-time. Selenium memerlukan lebih banyak penyiapan dan penanganan untuk berinteraksi secara andal dengan konten dinamis.

### 6. **Ringkasan Perbandingan**

| Fitur                          | Playwright                                    | Selenium                                   |
|-----------------------------------|-----------------------------------------------|-------------------------------------------|
| **Kemudahan Penggunaan**                   | Sintaksis lebih pendek, lebih intuitif untuk UI modern | Lebih eksplisit, memerlukan lebih banyak boilerplate  |
| **Dukungan Bahasa**              | TypeScript, Python, JavaScript                | TypeScript, Python, Java, Ruby, C#        |
| **Pengujian UI Interaktif**        | Sangat baik untuk UI dinamis dan real-time          | Menangani UI dasar, tetapi lebih panjang dan kompleks untuk interaksi yang kaya |
| **Pengujian Unggah File**           | API yang lebih cerdas untuk unggah file                  | Lebih panjang, API kurang intuitif         |
| **Integrasi CI/CD**             | Integrasi mudah dengan GitHub Actions, Jenkins | Integrasi kuat dengan banyak alat CI    |
| **Pengujian Seluler**                | Terbatas, hanya emulasi                       | Dukungan penuh melalui Appium               |
| **Dukungan Lintas Browser**         | Chromium, WebKit, Firefox                     | Dukungan penuh di browser utama dan lama |
| **Kinerja**                   | Cepat, dioptimalkan untuk pengujian headless          | Lebih lambat, terutama dalam mode headless       |
| **Pengujian Multi-monitor**         | Terbatas                                       | Dukungan baik untuk penyiapan multi-monitor    |
| **Komunitas dan Ekosistem**       | Berkembang, dokumentasi baik                   | Besar, matang, ekosistem luas       |

### 7. **Keputusan**

Setelah mempertimbangkan persyaratan dan trade-off, **Playwright** adalah pilihan yang lebih baik untuk kebutuhan kami saat ini. API-nya yang lebih cerdas untuk pengujian unggah file lokal, sintaksis yang ringkas, dan dukungan kuat untuk pengujian UI interaktif menjadikannya sangat cocok untuk siklus pengembangan agile kami. Fakta bahwa Playwright mendukung **TypeScript** dan **Python** sangat penting bagi tim kami, dan pendekatan modern kerangka ini terhadap pengujian akan memungkinkan kami menulis kode yang bersih dan mudah dipelihara.

Meskipun **Selenium** tetap menjadi alat yang hebat, terutama untuk pengujian seluler, dukungan browser lama, dan penyiapan multi-monitor, Selenium kurang cocok untuk kebutuhan kami saat ini. Kepanjangannya, kinerja yang lebih lambat, dan penanganan UI dinamis seperti bagan yang lebih kompleks membuatnya kurang optimal untuk kasus penggunaan kami.

### 8. **Konsekuensi**

- **Tindakan Segera**: Kami akan mengadopsi **Playwright** untuk pengujian E2E kami, dengan berfokus pada pengujian alur pengguna yang melibatkan pendaftaran, masuk, unggah file, dasbor, dan pengunduhan laporan.
- **Pertimbangan Jangka Panjang**: Kami akan memantau perkembangan ekosistem Playwright. Jika kebutuhan kami berubah, terutama terkait pengujian seluler atau dukungan browser lama, kami mungkin meninjau kembali Selenium.
- **Pelatihan dan Dokumentasi**: Tim pengembangan perlu membiasakan diri dengan API Playwright, terutama untuk menangani UI dinamis dan unggah file.
- **Migrasi**: Pengujian Selenium yang sudah ada (jika ada) akan dimigrasikan secara bertahap ke Playwright.

### 9. **Pertimbangan Masa Depan**
