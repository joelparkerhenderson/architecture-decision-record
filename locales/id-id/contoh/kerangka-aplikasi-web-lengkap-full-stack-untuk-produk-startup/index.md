# Catatan Keputusan Arsitektur: kerangka aplikasi web, lengkap (batteries included), full stack, untuk produk startup

<!-- 

ChatGPT prompt

Long software architecture decision record 
for a web application framework, batteries included, full stack, for a startup product.

Evaluate Python Django, Ruby on Rails, Phoenix Elixir, Rust Loco.

Primary need: web application for paying customers to sign in, upload files, process data, and view reports. 

High importance: 1. Agile development because this is for a startup. 2. Full-stack because we do not want to spend extra time on a separate front-end. 3. Works well with AI/ML tools for data analysis, such as Project Jupyter notebooks.

Low importance: 1. Runtime speed. 2. Scalability. 3. Backwards compatibility.

-->

**Tujuan Utama:**  
Membangun aplikasi web bagi pelanggan berbayar untuk masuk, mengunggah file, memproses data, dan melihat laporan, dengan fokus pada pengembangan agile, fungsionalitas full-stack, dan kompatibilitas yang kuat dengan alat AI/ML, terutama notebook Project Jupyter.

### Konteks dan Persyaratan:

1. **Pengembangan Agile (Prioritas Tinggi)**: Sebagai startup, kami membutuhkan iterasi cepat dan fleksibilitas. Praktik agile, seperti pembuatan prototipe cepat, pengembangan iteratif, dan kemampuan beradaptasi terhadap perubahan, adalah kunci siklus pengembangan kami.

2. **Kerangka Full-Stack (Prioritas Tinggi)**: Kami bertujuan meminimalkan overhead dengan memilih kerangka yang dapat menangani backend dan frontend secara efisien, sehingga mengurangi kebutuhan akan kerangka front-end terpisah.

3. **Kompatibilitas dengan Alat AI/ML (Prioritas Tinggi)**: Kemampuan berintegrasi dengan mudah dengan alat analisis data seperti notebook Jupyter dan ekosistem ilmu data Python (NumPy, Pandas, TensorFlow, dll.) sangat penting. Hal ini akan memfasilitasi pemrosesan dan pelaporan data yang efisien.

4. **Kriteria Prioritas Rendah**:
   - **Kecepatan Waktu Proses**: Meskipun kinerja relevan, ini bukan faktor paling kritis pada awalnya karena kami lebih memperhatikan kecepatan pengembangan dan kelengkapan fitur.
   - **Skalabilitas**: Kami mengantisipasi pertumbuhan, tetapi masalah skalabilitas dapat ditangani nanti, dan ini bukan persyaratan utama saat ini.
   - **Kompatibilitas Mundur**: Kami berfokus pada teknologi saat ini dan tidak terlalu mengkhawatirkan kompatibilitas mundur dengan sistem lama.

### Kerangka yang Dievaluasi:

1. **Django (Python)**  
2. **Ruby on Rails (Ruby)**  
3. **Phoenix (Elixir)**  
4. **Loco (Rust)**

---

### 1. **Django (Python)**

**Gambaran Umum**:  
Django adalah kerangka web tingkat tinggi untuk Python yang mendorong pengembangan cepat serta desain yang bersih dan pragmatis. Django dikenal dengan filosofi “batteries included”, artinya Django menyertakan banyak fitur seperti autentikasi, routing, ORM, dan penanganan formulir langsung dari awal.

**Kekuatan**:  
- **Full-Stack**: Django adalah kerangka full-stack yang komprehensif yang dapat menangani kebutuhan backend dan frontend dengan fitur terintegrasi (misalnya mesin templat, antarmuka admin).
- **Pengembangan Agile**: Struktur dan konvensi Django yang terdefinisi dengan baik memungkinkan pengembangan cepat dan kemampuan beradaptasi, yang sangat penting untuk lingkungan startup. Kerangka ini hadir dengan dokumentasi yang sangat baik dan ekosistem paket pihak ketiga yang kaya, yang mempercepat pengembangan.
- **Integrasi AI/ML**: Ekosistem Python tidak tertandingi dalam hal ilmu data dan pembelajaran mesin. Django, yang berbasis Python, terintegrasi mulus dengan alat seperti notebook Jupyter, Pandas, NumPy, TensorFlow, dan scikit-learn.
- **Komunitas dan Ekosistem**: Django memiliki komunitas yang luas, dokumentasi yang tangguh, dan beragam plugin dan ekstensi, yang secara signifikan mempercepat pengembangan dan pemecahan masalah.
  
**Kelemahan**:  
- **Kecepatan Waktu Proses**: Python cenderung lebih lambat dibandingkan bahasa seperti Rust atau Elixir. Namun, untuk kasus penggunaan ini, di mana kinerja bukan perhatian utama, hal ini mungkin bukan penghalang.
- **Skalabilitas**: Meskipun Django sangat skalabel, mungkin ada tantangan pada skala yang sangat tinggi tanpa optimasi yang cermat (misalnya, ketika menangani permintaan konkuren yang berat). Namun, Django tetap dapat diskalakan secara efektif menggunakan teknik penyeimbangan beban dan caching.

**Penilaian**:  
Django selaras dengan baik dengan persyaratan pengembangan agile, dukungan full-stack, dan kompatibilitas AI/ML. Integrasi Python-nya menawarkan akses mulus ke alat dan pustaka ilmu data yang diperlukan untuk aplikasi.

---

### 2. **Ruby on Rails (Ruby)**

**Gambaran Umum**:  
Ruby on Rails (RoR) adalah kerangka aplikasi web full-stack yang matang dan dikenal dengan pendekatan konvensi-di-atas-konfigurasi, yang memfasilitasi pengembangan cepat.

**Kekuatan**:  
- **Full-Stack**: RoR hadir dengan alat bawaan untuk pengembangan backend dan frontend (misalnya view, templat, scaffolding), dan pustaka gem-nya yang kaya memungkinkan implementasi cepat berbagai fitur.
- **Pengembangan Agile**: Ruby on Rails terutama dikenal dengan siklus iterasinya yang cepat, yang menguntungkan bagi startup yang ingin beriterasi dengan cepat pada fitur. RoR mendukung test-driven development (TDD) dan memiliki ekosistem yang mapan untuk alur kerja agile.
- **Komunitas dan Ekosistem**: RoR memiliki komunitas yang mapan dan kuat serta beragam gem yang dapat mempercepat pengembangan.
- **Kemudahan Penggunaan**: Rails memiliki sintaksis yang sangat ramah pengembang dan dikenal membuat tugas seperti migrasi basis data, arsitektur model-view-controller (MVC), dan penanganan rute menjadi cepat dan sederhana.

**Kelemahan**:  
- **Kinerja**: Ruby cenderung memiliki kinerja waktu proses yang lebih lambat dibandingkan Python atau Elixir. Meskipun RoR dapat diskalakan dengan infrastruktur yang tepat, kinerja Ruby dapat menjadi hambatan bagi aplikasi yang memerlukan pemrosesan real-time yang berat atau lalu lintas konkuren yang tinggi.
- **Integrasi AI/ML**: Meskipun Ruby memiliki beberapa pustaka pembelajaran mesin, Ruby tidak banyak diadopsi di komunitas AI/ML seperti Python. Integrasi dengan alat seperti notebook Jupyter tidak semulus itu, sehingga Python menjadi pilihan yang lebih kuat untuk aplikasi yang sarat data.
  
**Penilaian**:  
Meskipun Ruby on Rails unggul dalam pengembangan agile dan pembuatan prototipe cepat, Ruby on Rails kalah dalam hal kompatibilitas AI/ML dibandingkan Python (Django). Ini adalah pilihan yang layak bagi startup yang memprioritaskan iterasi cepat daripada integrasi analisis data yang mendalam.

---

### 3. **Phoenix (Elixir)**

**Gambaran Umum**:  
Phoenix adalah kerangka web yang dibangun dengan Elixir, bahasa pemrograman fungsional yang dirancang untuk skalabilitas dan konkurensi. Phoenix memanfaatkan Erlang VM, yang dikenal mampu menangani konkurensi masif dan sistem yang toleran terhadap kesalahan.

**Kekuatan**:  
- **Skalabilitas dan Kinerja**: Phoenix bersinar dalam skalabilitas dan penanganan konkurensi tinggi. Phoenix dibangun di atas Erlang VM, yang dapat mendukung ribuan (bahkan jutaan) koneksi konkuren, menjadikannya kandidat yang kuat untuk aplikasi yang memerlukan pemrosesan data real-time atau lalu lintas bervolume tinggi.
- **Full-Stack**: Phoenix mencakup semua yang diperlukan untuk membangun backend dan frontend aplikasi. Phoenix mendukung live view untuk pembaruan UI interaktif dan menyertakan mesin templat.
- **Pengembangan Agile**: Phoenix sangat modular, memungkinkan iterasi cepat pada fitur. Phoenix sangat cocok untuk startup yang perlu bergerak cepat.
- **Kompatibilitas AI/ML**: Meskipun Elixir memiliki pustaka pembelajaran mesin yang sedang berkembang, Elixir tidak didukung seluas Python untuk tugas AI/ML. Mengintegrasikan dengan alat seperti notebook Jupyter memerlukan solusi alternatif, karena ekosistem Elixir untuk ilmu data tidak sematang Python.

**Kelemahan**:  
- **Ekosistem AI/ML**: Elixir bukan bahasa utama yang digunakan dalam ilmu data atau pembelajaran mesin, dan ekosistemnya tidak semapan Python. Dengan demikian, integrasi dengan alat seperti notebook Jupyter atau pustaka AI populer (TensorFlow, PyTorch) akan merepotkan.
- **Kurva Belajar**: Jika tim tidak familier dengan pemrograman fungsional dan Elixir, mungkin ada kurva belajar yang lebih curam.

**Penilaian**:  
Phoenix adalah pilihan yang sangat baik jika skalabilitas dan konkurensi menjadi perhatian utama. Namun, mengingat prioritas pada kompatibilitas AI/ML, Phoenix mungkin bukan yang paling cocok karena ekosistem Elixir yang terbatas di bidang ini.

---

### 4. **Loco (Rust)**

**Gambaran Umum**:  
Loco adalah kerangka web yang dibangun dengan Rust, bahasa pemrograman sistem yang dikenal dengan kinerja, keamanan memori, dan konkurensinya. Rust semakin populer untuk membangun aplikasi berkinerja tinggi.

**Kekuatan**:  
- **Kinerja**: Kekuatan utama Rust terletak pada kinerja tinggi dan keamanan memorinya, menjadikannya pilihan yang sangat baik untuk aplikasi yang memerlukan kendali tingkat rendah atau kinerja yang sangat tinggi.
- **Konkurensi**: Sistem kepemilikan (ownership) Rust memastikan keamanan memori sambil memungkinkan pemrograman konkuren yang aman, sehingga ideal untuk sistem yang perlu diskalakan secara efisien dan menangani paralelisme.

**Kelemahan**:  
- **Pengembangan Full-Stack**: Loco, meskipun menjanjikan, tidak semapan kerangka lain dalam hal menyediakan solusi full-stack yang lengkap. Loco lebih cocok untuk pengembangan backend, dan ekosistem front-end di sekitar Rust masih berkembang.
- **Pengembangan Agile**: Pengembangan dengan Rust bisa lebih lambat dibandingkan bahasa tingkat lebih tinggi seperti Python atau Ruby karena sifatnya yang lebih tingkat rendah dan kurva belajar yang lebih curam.
- **Ekosistem AI/ML**: Rust tidak memiliki ekosistem seluas Python untuk AI/ML. Meskipun ada pustaka yang berkembang di Rust untuk komputasi numerik, pustaka tersebut jauh kurang matang dibandingkan penawaran Python, seperti notebook Jupyter atau kerangka pembelajaran mesin.
  
**Penilaian**:  
Meskipun Rust dan kerangkanya Loco menawarkan kinerja yang luar biasa, kurangnya dukungan full-stack, manfaat pengembangan agile, dan ekosistem AI/ML membuatnya kurang ideal untuk kasus penggunaan khusus ini. Rust lebih cocok untuk aplikasi yang kritis terhadap kinerja daripada pengembangan web cepat dengan alat ilmu data terintegrasi.

---

### Kesimpulan

Setelah mengevaluasi opsi-opsi berdasarkan persyaratan proyek, **Django (Python)** adalah pilihan yang paling sesuai. Django menawarkan keunggulan berikut:

- **Kemampuan Full-Stack**: Django adalah kerangka full-stack yang mengintegrasikan pengembangan backend dan frontend.
- **Pengembangan Agile**: Kerangka ini sangat cocok untuk pembuatan prototipe dan iterasi cepat, yang sangat penting untuk lingkungan startup.
- **Kompatibilitas AI/ML**: Python adalah bahasa terdepan dalam AI/ML, dan kompatibilitas Django dengan pustaka seperti notebook Jupyter memastikan integrasi yang mulus untuk analisis dan pemrosesan data.
- **Komunitas dan Ekosistem**: Dukungan komunitas Django yang kuat dan ekosistem pustaka yang luas menyediakan banyak alat untuk mempercepat pengembangan.

Meskipun **Ruby on Rails** juga merupakan pesaing yang kuat untuk pengembangan agile, dukungan AI/ML-nya yang terbatas membuatnya kurang ideal untuk kasus penggunaan khusus ini. **Phoenix (Elixir)** dan **Loco (Rust)**, meskipun sangat baik untuk skalabilitas dan kinerja, kurang dalam integrasi AI/ML dan pengembangan full-stack. Oleh karena itu, Django adalah kerangka yang direkomendasikan untuk proyek ini.
