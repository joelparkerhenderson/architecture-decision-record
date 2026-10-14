# Konfigurasi variabel lingkungan

Daftar isi:

* [Ringkasan](#ringkasan)
  * [Isu](#isu)
  * [Keputusan](#keputusan)
  * [Status](#status)
* [Rincian](#rincian)
  * [Asumsi](#asumsi)
  * [Batasan](#batasan)
  * [Posisi](#posisi)
  * [Argumen](#argumen)
  * [Implikasi ](#implikasi)
* [Terkait](#terkait)
  * [Keputusan terkait](#keputusan-terkait)
  * [Persyaratan terkait](#persyaratan-terkait)
  * [Artefak terkait](#artefak-terkait)
  * [Prinsip terkait](#prinsip-terkait)
* [Catatan](#catatan)


## Ringkasan


### Isu

Kami ingin aplikasi kami dapat dikonfigurasi di luar artefak/biner/kode sumber, sehingga satu build dapat berperilaku berbeda tergantung pada lingkungan deployment-nya.

  * Untuk mencapai hal ini, kami ingin menggunakan konfigurasi variabel lingkungan.

  * Kami ingin mengelola konfigurasi dengan menggunakan file yang dapat kami kontrol versinya.

  * Kami ingin menyediakan ergonomi pengalaman pengembang, seperti mengetahui apa yang dapat dikonfigurasi dan nilai bawaan yang relevan.


### Keputusan

Memutuskan file .env dengan file nilai bawaan dan file skema yang terkait.


### Status

Diputuskan. Terbuka untuk mempertimbangkan kemampuan baru seiring kemunculannya.


## Rincian


### Asumsi

Kami lebih menyukai pemisahan kode aplikasi dan kode lingkungan. Kami berasumsi aplikasi perlu bekerja secara berbeda di lingkungan yang berbeda, seperti lingkungan pengembangan, lingkungan pengujian, lingkungan demo, lingkungan produksi, dll.

Kami menyukai praktik industri "12 factor app" dan terlebih lagi praktik terkait "15 factor app".

Banyak proyek kami sebelumnya menggunakan konvensi file `.env` atau direktori `.env` yang serupa. Ada praktik umum untuk menjaga file-file ini di luar kontrol versi, dan sebagai gantinya menggunakan cara lain untuk men-deploy, memberi versi, dan mengelolanya.


### Batasan

Kami ingin menjaga rahasia di luar sistem kontrol versi (VCS) manajemen kode sumber (SCM) kami.

Kami ingin mengupayakan kompatibilitas dengan kerangka kerja dan pustaka perangkat lunak yang populer. Misalnya, Node memiliki modul "dotenv" untuk membaca konfigurasi variabel lingkungan.


### Posisi

Kami mempertimbangkan beberapa pendekatan:

  * Menyimpan konfigurasi di dalam aplikasi, seperti dalam file `config.js`.

  * Menyimpan konfigurasi di lingkungan, seperti dalam file `.env`.

  * Mengambil konfigurasi dari lokasi yang diketahui, seperti server lisensi.


### Argumen

Kami memilih pendekatan file .env karena:

  * Populer, termasuk di kalangan para ahli.

  * Mengikuti pola file `.env` yang telah berhasil digunakan tim kami berkali-kali pada banyak proyek.

  * Sederhana. Perlu dicatat, saat ini kami dapat menerima trade-off signifikan yang kami lihat, seperti tidak adanya kemampuan audit dibandingkan dengan pendekatan server lisensi.


### Implikasi 

Kami perlu mencari cara untuk memisahkan konfigurasi variabel lingkungan yang bersifat publik dari manajemen rahasia apa pun.


## Terkait


### Keputusan terkait

Kami mengharapkan semua aplikasi kami menggunakan pendekatan ini.

Kami akan merencanakan peningkatan setiap aplikasi kami yang menggunakan pendekatan yang kurang mampu, seperti hardcoding dalam biner atau dalam kode sumber.

Kami akan mempertahankan apa adanya setiap aplikasi kami yang menggunakan pendekatan yang lebih mampu, seperti server lisensi.


### Persyaratan terkait

Kami akan menambahkan kemampuan devops untuk file-file tersebut, termasuk hook, pengujian, dan integrasi berkelanjutan.

Kami perlu melatih semua rekan tim pengembang tentang keputusan ini.



### Artefak terkait

Setiap area tempat kami men-deploy akan memerlukan file .env dan file terkait miliknya sendiri.


### Prinsip terkait

Mudah dibatalkan.


## Catatan


Contoh file `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Contoh file `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Contoh file `.env.schema` hanya dengan kunci:

```env
NAME
EMAIL
```
