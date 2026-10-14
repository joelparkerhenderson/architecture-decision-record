# Format stempel waktu

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
  * [Implikasi](#implikasi)
* [Terkait](#terkait)
  * [Keputusan terkait](#keputusan-terkait)
  * [Persyaratan terkait](#persyaratan-terkait)
  * [Artefak terkait](#artefak-terkait)
  * [Prinsip terkait](#prinsip-terkait)
* [Catatan](#catatan)


## Ringkasan


### Isu

Kami ingin dapat melacak kapan sesuatu terjadi dengan menggunakan stempel waktu dan dengan menggunakan format stempel waktu yang konsisten yang bekerja dengan baik di semua sistem kami dan sistem pihak ketiga.

Kami berinteraksi dengan sistem yang memiliki format stempel waktu yang berbeda:

* Pesan JSON tidak memiliki format stempel waktu bawaan, sehingga kami perlu memilih cara mengonversi stempel waktu menjadi string, dan mengonversi string menjadi stempel waktu, yaitu cara melakukan serialisasi/deserialisasi.

* Beberapa aplikasi diatur untuk menggunakan waktu lokal, bukan waktu UTC. Hal ini dapat memudahkan proyek yang harus menyesuaikan dengan waktu lokal, seperti proyek yang memicu event berdasarkan waktu lokal.

* Beberapa sistem memiliki kebutuhan dan kemampuan presisi waktu yang berbeda, seperti menggunakan resolusi waktu detik vs. milidetik vs. nanodetik. Misalnya, perintah `date` sistem operasi Linux menggunakan presisi waktu bawaan detik, sedangkan bursa saham Nasdaq menginginkan presisi waktu bawaan nanodetik.


### Keputusan

Kami memilih format standar stempel waktu ISO 8601 dengan presisi nanodetik, khususnya "YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ".

Format ini menunjukkan tahun, bulan, hari, jam, menit, detik, nanodetik, dan zona waktu Zulu alias UTC, GMT.


### Status

Diputuskan.


## Rincian


### Asumsi

Kami perlu menangani string teks stempel waktu ini, untuk mengonversi dari stempel waktu ke string (alias serialisasi) dan mengonversi dari string ke stempel waktu (alias deserialisasi).

Kami menginginkan format yang secara umum mudah digunakan, mudah dikonversi, dan mudah dibaca oleh manusia.

Kami menginginkan kompatibilitas dengan beragam sistem eksternal yang tidak dapat kami kendalikan, seperti sistem analitik, sistem basis data, sistem keuangan.


### Batasan

Beberapa sistem memiliki keterbatasan presisi waktu. Misalnya, perintah `date` sistem operasi macOS dapat mencetak presisi waktu dalam detik, tetapi tidak dalam nanodetik.


### Posisi

Kami mempertimbangkan berbagai opsi:

* Unix epoch yaitu satu angka yang bertambah.

* Format teks ringkas "YYYYMMDDTHHMMSSNNNNNNNNN".

* Menggunakan zona waktu lokal vs. zona waktu UTC.


### Argumen

Untuk penggunaan yang umum, kami menghargai kemudahan membaca/menulis oleh manusia, lebih dari kecepatan/ukuran mentah.

Untuk penggunaan yang umum, kami menginginkan format yang bekerja dengan baik di sistem mesin, dan juga bekerja dengan baik secara manual, seperti menulis data contoh, membaca keluaran JSON, melakukan grep pada file log, dll.

Untuk penggunaan yang tidak umum, seperti komputasi kinerja tinggi, kami memperkirakan kami akan ingin mengoptimalkan format teks apa pun yang kami pilih dengan mengonversi teks menjadi format yang lebih cepat, seperti tipe objek tanggal bawaan bahasa pemrograman. Jadi format teks tidak terlalu penting untuk HPC.


### Implikasi

Berbagai sistem teks dan sistem waktu kami akan menyatu pada format ini.


## Terkait


### Keputusan terkait

Kami mungkin menginginkan cara yang cepat/mudah untuk juga melacak selisih waktu alias durasi. Ini mudah dilakukan dengan stempel waktu Unix epoch.


### Persyaratan terkait

Kami mungkin ingin menyesuaikan keputusan kami misalnya jika kami memiliki persyaratan terkait untuk jenis stempel pesan log tertentu, seperti untuk Splunk, Sumo, ELK, dll.


### Artefak terkait

Pemformat dan pengurai bahasa:

  * [date-fns: Modern JavaScript date utility library](https://date-fns.org/)
  * [Crono: date and time library for Rust](https://github.com/chronotope/chron)
  
Contoh Rosetta Code:

  * [System time](https://www.rosettacode.org/wiki/System_time)
  * [Data format](https://www.rosettacode.org/wiki/Date_format)
  * [Show the epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Contoh SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Prinsip terkait

Mudah dibatalkan. Kami dapat beralih dengan cukup mudah ke format yang berbeda, seperti Unix epoch.

Tunda optimasi prematur. Untuk penggunaan yang umum kami tidak terlalu peduli dengan beberapa karakter tambahan seperti format yang menggunakan tanda hubung dan titik dua.


## Catatan

Tambahkan catatan di sini.
