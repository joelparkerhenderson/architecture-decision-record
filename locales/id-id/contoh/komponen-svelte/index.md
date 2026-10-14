# Catatan Keputusan Arsitektur (ADR) untuk Komponen Svelte

<!--

Prompt:

Architecture decision record for Svelte components.

Compare options: SVAR, Carbon, Flowbite, SkeletonUI, MeltUI, SvelteUI, shadcn-svelte

The goal is full features for table, charts, lists, grids, gantt, 

-->

## Konteks

Kami sedang memilih pustaka komponen UI Svelte untuk menyediakan fitur lengkap bagi:
- **Tabel**
- **Bagan**
- **Daftar**
- **Grid**
- **Bagan Gantt**

Tujuannya adalah memilih pustaka yang menyeimbangkan kemudahan integrasi, dukungan fitur lengkap, kinerja, dan kemudahan pemeliharaan jangka panjang. Opsi yang dipertimbangkan adalah:

1. **SVAR**
2. **Carbon**
3. **Flowbite**
4. **SkeletonUI**
5. **MeltUI**
6. **SvelteUI**
7. **shadcn-svelte**

## Analisis Opsi

### 1. **SVAR**
- **Gambaran umum**: SVAR adalah pustaka komponen modern yang kaya fitur untuk Svelte, dengan fokus pada sistem desain dan komponen siap perusahaan.
- **Kelebihan**:
  - Komponen berfitur lengkap, termasuk tabel, formulir, dan bagan.
  - Opsi kustomisasi tinggi dengan dukungan tema bawaan.
  - Dukungan bawaan untuk aksesibilitas dan responsivitas.
  - Terdokumentasi dengan baik dengan kontribusi komunitas.
- **Kekurangan**:
  - Mungkin lebih berat dibandingkan pustaka lain yang lebih sederhana.
  - Dukungan terbatas untuk komponen tertentu seperti bagan Gantt dan grid lanjutan.
- **Paling cocok untuk**: Aplikasi tingkat perusahaan yang membutuhkan sistem desain berfitur lengkap.
- **Dukungan Tabel/Bagan**: Sedang hingga baik.
- **Dukungan Grid/Gantt**: Minimal.

### 2. **Carbon**
- **Gambaran umum**: Carbon Design System adalah sistem desain sumber terbuka dari IBM, yang menawarkan serangkaian komponen UI yang tangguh.
- **Kelebihan**:
  - Desain berkualitas tinggi dan halus dengan dokumentasi yang luas.
  - Sangat mudah diakses dan responsif.
  - Pustaka komponen besar, termasuk grid, tabel, dan kontrol formulir.
- **Kekurangan**:
  - Tidak berfokus pada Svelte, sehingga integrasi bisa merepotkan.
  - Mungkin memerlukan kustomisasi tambahan untuk kompatibilitas penuh dengan Svelte.
  - Tidak ada dukungan bawaan untuk komponen lanjutan seperti bagan Gantt atau bagan kompleks.
- **Paling cocok untuk**: Proyek skala besar yang membutuhkan UI yang konsisten dan halus.
- **Dukungan Tabel/Bagan**: Baik (dengan integrasi pustaka bagan).
- **Dukungan Grid/Gantt**: Baik (dukungan Grid tersedia, tetapi tidak ada bagan Gantt).

### 3. **Flowbite**
- **Gambaran umum**: Flowbite adalah pustaka komponen yang dibangun dengan Tailwind CSS, menawarkan berbagai komponen dan elemen UI.
- **Kelebihan**:
  - Berbasis Tailwind CSS, sehingga mudah dikustomisasi.
  - Mudah diintegrasikan dan digunakan dengan Svelte.
  - Menyediakan komponen yang kaya seperti tabel, bagan, dan kontrol UI.
- **Kekurangan**:
  - Tidak memiliki fitur lanjutan (misalnya bagan Gantt atau grid kompleks).
  - Tidak memiliki komponen bagan bawaan; bergantung pada pustaka eksternal.
- **Paling cocok untuk**: Proyek yang membutuhkan pengembangan cepat dengan fokus pada integrasi Tailwind CSS.
- **Dukungan Tabel/Bagan**: Baik (memerlukan integrasi dengan pustaka bagan pihak ketiga).
- **Dukungan Grid/Gantt**: Minimal.

### 4. **SkeletonUI**
- **Gambaran umum**: SkeletonUI adalah pustaka komponen ringan untuk Svelte, yang berfokus pada kesederhanaan dan minimalisme.
- **Kelebihan**:
  - Sangat ringan dan cepat.
  - API sederhana dan intuitif.
  - Bagus untuk proyek kecil atau ketika kinerja sangat penting.
- **Kekurangan**:
  - Sangat sedikit komponen yang disertakan, sehingga tidak kaya fitur.
  - Tidak memiliki komponen tabel/grid/bagan/Gantt lanjutan.
  - Dukungan komunitas terbatas dan dokumentasi kurang lengkap.
- **Paling cocok untuk**: Proyek yang membutuhkan komponen ringan dengan overhead minimal.
- **Dukungan Tabel/Bagan**: Minimal.
- **Dukungan Grid/Gantt**: Minimal.

### 5. **MeltUI**
- **Gambaran umum**: MeltUI adalah kumpulan komponen UI yang mudah diakses untuk Svelte, yang berfokus pada kesederhanaan dan kemampuan komposisi.
- **Kelebihan**:
  - Ringan dan dapat dikustomisasi sepenuhnya.
  - Fitur aksesibilitas yang baik secara bawaan.
  - Desain modern dan minimalis.
- **Kekurangan**:
  - Kurang kaya fitur dibandingkan pustaka lain.
  - Tidak memiliki komponen grid dan tabel lanjutan.
  - Tidak ada bagan Gantt atau opsi bagan kompleks.
- **Paling cocok untuk**: Desain minimalis yang memprioritaskan aksesibilitas dan kinerja.
- **Dukungan Tabel/Bagan**: Minimal.
- **Dukungan Grid/Gantt**: Minimal.

### 6. **SvelteUI**
- **Gambaran umum**: SvelteUI adalah pustaka komponen UI yang komprehensif dan dapat dikustomisasi untuk Svelte, dirancang untuk membangun aplikasi web modern dengan UI yang elegan.
- **Kelebihan**:
  - Kumpulan komponen yang komprehensif, termasuk tabel, grid, bagan, dan formulir.
  - Menyediakan dukungan mode terang dan gelap.
  - Sangat dapat dikustomisasi dan mudah diperluas.
  - Integrasi bawaan untuk pustaka bagan seperti `chart.js` atau `d3.js`.
- **Kekurangan**:
  - Bisa lebih berat daripada pustaka komponen yang lebih sederhana.
  - Memerlukan sedikit penyiapan untuk mengintegrasikan pustaka eksternal bagi fitur yang lebih kompleks seperti bagan Gantt.
- **Paling cocok untuk**: Proyek yang membutuhkan kumpulan komponen yang komprehensif dan dapat dikustomisasi.
- **Dukungan Tabel/Bagan**: Sangat baik (pustaka bagan didukung).
- **Dukungan Grid/Gantt**: Baik (komponen Grid tersedia; Gantt memerlukan integrasi eksternal).

### 7. **shadcn-svelte**
- **Gambaran umum**: Versi Svelte dari ShadCN, yang berfokus pada desain yang mengutamakan utilitas dan menyediakan komponen modern yang sudah bergaya.
- **Kelebihan**:
  - Desain yang mengutamakan utilitas, dibangun di atas Tailwind CSS, sehingga mudah dikustomisasi.
  - Kumpulan komponen yang kaya dan sepenuhnya bergaya secara bawaan.
  - Mudah diintegrasikan dengan pustaka lain.
- **Kekurangan**:
  - Tidak selengkap beberapa pustaka lain dalam hal elemen UI lanjutan.
  - Tidak memiliki dukungan bawaan untuk tabel, bagan, atau grid.
  - Tidak ada dukungan bawaan untuk bagan Gantt.
- **Paling cocok untuk**: Proyek kecil hingga menengah yang membutuhkan pendekatan yang mengutamakan utilitas dan dapat dikustomisasi.
- **Dukungan Tabel/Bagan**: Minimal.
- **Dukungan Grid/Gantt**: Minimal.

## Keputusan

### Opsi yang Direkomendasikan: **SvelteUI**

- **Alasan**: SvelteUI menawarkan rangkaian komponen yang lengkap dan komprehensif yang memenuhi kebutuhan akan tabel, bagan, grid, dan formulir. SvelteUI sangat dapat dikustomisasi, terintegrasi dengan baik dengan pustaka bagan lain (seperti `chart.js` dan `d3.js`), dan memiliki keseimbangan yang baik antara kinerja ringan dan kekayaan fitur. Meskipun mungkin tidak menyediakan dukungan bagan Gantt bawaan, SvelteUI dapat dengan mudah diperluas dengan integrasi pihak ketiga, sehingga ideal untuk solusi berfitur lengkap dan skalabel.
  
  - **Kelebihan**:
    - Dukungan tabel dan bagan yang sangat baik.
    - Komponen grid dan tata letak yang lengkap.
    - Dapat dikustomisasi dan terintegrasi dengan baik dengan pustaka bagan eksternal.
    - Komunitas dan dokumentasi yang baik.
  
  - **Kekurangan**:
    - Lebih berat daripada beberapa pustaka minimalis lainnya.
    - Memerlukan integrasi eksternal untuk bagan kompleks seperti bagan Gantt.
  
### Alternatif: **Flowbite** atau **Carbon** (untuk proyek perusahaan yang lebih besar)
- Jika diperlukan sistem desain yang halus, berbasis Tailwind, atau lebih konsisten, **Flowbite** (dengan Tailwind CSS) atau **Carbon** (untuk solusi tingkat perusahaan) dapat menjadi alternatif yang cocok. Namun, keduanya mungkin memerlukan upaya ekstra untuk integrasi dengan bagan dan komponen yang lebih kompleks.

## Kesimpulan

Pilihan yang paling sesuai untuk kebutuhan Anda (fitur lengkap untuk tabel, bagan, daftar, grid, Gantt) adalah **SvelteUI**, diikuti oleh **Flowbite** dan **Carbon** tergantung pada kebutuhan proyek dan preferensi desain.
