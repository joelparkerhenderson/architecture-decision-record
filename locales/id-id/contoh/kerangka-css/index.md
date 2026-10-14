# Catatan Keputusan Arsitektur: Kerangka CSS

Daftar isi:

- [Ringkasan](#ringkasan)
  - [Isu](#isu)
  - [Keputusan](#keputusan)
  - [Status](#status)
- [Rincian](#rincian)
  - [Asumsi](#asumsi)
  - [Batasan](#batasan)
  - [Posisi](#posisi)
  - [Argumen](#argumen)
  - [Implikasi](#implikasi)
- [Terkait](#terkait)
  - [Keputusan terkait](#keputusan-terkait)
  - [Persyaratan terkait](#persyaratan-terkait)
  - [Artefak terkait](#artefak-terkait)
  - [Prinsip terkait](#prinsip-terkait)
- [Catatan](#catatan)


## Ringkasan


### Isu

Kami ingin menggunakan kerangka CSS untuk membuat aplikasi web kami:

  * Kami ingin pengalaman pengguna yang cepat dan andal, di semua browser dan ukuran layar yang populer.

  * Kami ingin iterasi cepat pada desain, tata letak, UI/UX, dll.

  * Kami ingin aplikasi yang responsif, terutama untuk layar yang lebih kecil seperti di perangkat seluler, layar yang lebih besar seperti pada layar lebar 4K, dan layar dinamis seperti tampilan yang dapat diputar.  


### Keputusan

Memutuskan Bulma.


### Status

Memutuskan Bulma. Terbuka untuk pilihan kerangka CSS baru seiring kemunculannya.


## Rincian


### Asumsi

Kami ingin membuat aplikasi web yang modern, cepat, andal, responsif, dll.

Aplikasi web modern yang umum mengurangi/menghilangkan penggunaan jQuery karena beberapa alasan: 

  * JavaScript modern secara bertahap menghadirkan banyak kemampuan yang sebelumnya disediakan jQuery, sehingga jQuery semakin tidak dibutuhkan, dan ada modul yang lebih baik/lebih cepat/lebih kecil yang menyediakan implementasi spesifik

  * Pendekatan luas jQuery adalah memanipulasi DOM secara langsung, yang merupakan anti-pola bagi kerangka JavaScript modern (misalnya React, Vue, Svelte)

  * jQuery saling mengganggu dirinya sendiri jika dimuat dua kali, dll.


### Batasan

Jika kami memilih kerangka CSS yang menggunakan jQuery, maka kami terpaksa mengimpor jQuery. Misalnya, Semantic UI menggunakan jQuery, sedangkan Tachyons tidak.

Jika kami memilih kerangka CSS yang minimal, maka kami melepaskan komponen kerangka yang mungkin kami inginkan sekarang atau segera. Misalnya, Semantic UI menyediakan carousel gambar, sedangkan Tachyons tidak.


### Posisi

Kami mempertimbangkan untuk tidak menggunakan kerangka apa pun. Ini masih tampak layak, terutama karena CSS grid menyediakan banyak hal yang kami butuhkan untuk proyek kami..

Kami mempertimbangkan banyak kerangka CSS menggunakan triase daftar pendek yang cepat: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons, dll. Dua pilihan kami untuk tinjauan lebih mendalam adalah Semantic UI (karena memiliki pendekatan yang paling semantik) dan Bulma (karena memiliki pendekatan paling ringan yang menyediakan komponen yang kami inginkan sekarang).

Kami mempertimbangkan Semantic UI. Kerangka ini menyediakan banyak komponen, termasuk yang kami inginkan untuk proyek kami: tab, grid, tombol, dll. Kami melakukan percontohan dengan Semantic UI dengan dua cara: menggunakan file CDN biasa, dan menggunakan repo NPM. Kami berhasil dengan Semantic UI pada halaman HTML statis, tetapi tidak berhasil dalam batas waktu kami untuk membangun SPA JavaScript (terutama karena masalah pemuatan jQuery). Kami menemukan bahwa pembuat kode lain telah meminta para pengembang Semantic UI untuk membuat versi tanpa jQuery, dengan alasan yang sama seperti kami. Pembuat kode lain telah meminta versi tanpa jQuery selama bertahun-tahun, namun para pengembang menjawab tidak, dan menyatakan bahwa versi tanpa jQuery apa pun akan terlalu sulit ditulis, misalnya ~"proyek Semantic UI memiliki lebih dari 22.000 titik sentuh yang menggunakan jQuery".

Contoh dengan Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Kami mempertimbangkan Bulma. Bulma memiliki banyak kemampuan yang serupa dengan Semantic UI, meskipun tidak sebanyak komponen yang canggih. Bulma dibangun dengan teknik modern, seperti tanpa jQuery. Bulma memiliki beberapa komponen pihak ketiga, sebagian di antaranya mungkin ingin kami gunakan.


Contoh dengan Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argumen

Seperti di atas.

Secara khusus, Semantic UI tampaknya memiliki bendera peringatan baik dari segi teknologi (yaitu begitu banyak titik sentuh jQuery) maupun dari segi kepemimpinan (yaitu tanpa jQuery adalah penolakan tegas, alih-alih mencoba membuat peta jalan, atau perbaikan berkelanjutan, atau penggalangan donasi, dll.).


### Implikasi

Jika kami menemukan kerangka CSS non-jQuery yang baik, hal ini secara umum membantu dan baik secara keseluruhan.


## Terkait


### Keputusan terkait

Kerangka CSS yang kami pilih dapat memengaruhi kemampuan pengujian.


### Persyaratan terkait

Kami ingin merilis aplikasi yang murni modern dengan cepat. 

Kami tidak ingin menghabiskan waktu mengerjakan kerangka yang lebih lama (terutama Semantic UI) yang menggunakan dependensi yang lebih lama (terutama jQuery).


### Artefak terkait

Memengaruhi semua HTML umum yang akan menggunakan CSS tersebut.


### Prinsip terkait

Mudah dibatalkan.

Kebutuhan akan kecepatan.


## Catatan

Catatan apa pun di sini.
