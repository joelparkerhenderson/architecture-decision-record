# Bahasa pemrograman

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

Kami perlu memilih bahasa pemrograman untuk perangkat lunak kami. Kami memiliki dua kebutuhan utama: bahasa pemrograman front-end yang cocok untuk aplikasi web, dan bahasa pemrograman back-end yang cocok untuk aplikasi server.


### Keputusan

Kami memilih TypeScript untuk front-end.

Kami memilih Rust untuk back-end.


### Status

Diputuskan. Kami terbuka terhadap alternatif baru seiring kemunculannya.


## Rincian


### Asumsi

Aplikasi front-end bersifat umum:

  * Pengguna dan interaksi yang umum

  * Browser dan sistem yang umum

  * Pengembangan dan deployment yang umum

Aplikasi front-end kemungkinan akan berkembang dengan cepat:

  * Kami ingin memastikan pengembangan, deployment, iterasi, dll. yang cepat dan mudah.

  * Kami menghargai kemampuan pembuktian, seperti keamanan tipe, dan kami tidak keberatan mengerjakan sedikit lebih banyak untuk mencapainya.

  * Kami tidak membutuhkan kompatibilitas lama.

Aplikasi back-end berada di atas rata-rata:

  * Tujuan yang lebih tinggi dari biasanya untuk kualitas, terutama kemampuan pembuktian, keandalan, keamanan, dll.

  * Tujuan yang lebih tinggi dari biasanya untuk mendekati real-time, yaitu kami tidak menginginkan jeda akibat garbage collection mesin virtual.

  * Tujuan yang lebih tinggi dari biasanya untuk pemrograman fungsional, terutama untuk paralelisasi, pemrosesan multi-inti, dan keamanan memori.

Kami menerima kecepatan waktu kompilasi yang lebih rendah demi keamanan waktu kompilasi dan kecepatan waktu proses.


### Batasan

Kami memiliki batasan yang kuat pada bahasa yang dapat digunakan dengan layanan fungsi dari penyedia cloud utama, seperti Amazon Lambda.


### Posisi

Kami mempertimbangkan bahasa-bahasa berikut:

  * C

  * C++

  * Clojure
  
  * Elixir
  
  * Erlang
  
  * Elm
  
  * Flow
  
  * Go
  
  * Haskell
  
  * Java
  
  * JavaScript
  
  * Kotlin
  
  * Python
  
  * Ruby
  
  * Rust
  
  * TypeScript



### Argumen

Ringkasan per bahasa:

  * C: ditolak karena keamanannya rendah; Rust dapat melakukan hampir semuanya dengan lebih baik.

  * C++: ditolak karena berantakan; Rust dapat melakukan hampir semuanya dengan lebih baik.

  * Clojure: pemodelan yang sangat baik; pendekatan Lisp terbaik; waktu proses yang hebat di JVM.
  
  * Elixir: waktu proses yang sangat baik termasuk kemampuan deployment dan konkurensi; pengalaman pengembang yang sangat baik; ekosistem yang relatif kecil.

  * Erlang: waktu proses yang sangat baik termasuk kemampuan deployment dan konkurensi; pengalaman pengembang yang menantang; ekosistem yang relatif kecil.

  * Elm: tampak sangat menjanjikan; IBM menerbitkan studi kasus besar dengan hasil yang baik; ekosistem lebih kecil.

  * Flow: peningkatan yang menarik atas JavaScript; namun, para pengembang mulai meninggalkannya.

  * Go: pengalaman pengembang yang sangat baik; konkurensi yang sangat baik; tetapi memiliki rekam jejak keputusan buruk yang melumpuhkan bahasa tersebut.

  * Haskell: bahasa fungsional terbaik; komunitas pengembang lebih kecil; belum mencapai cukup banyak keberhasilan produksi yang dipublikasikan.

  * Java: waktu proses yang sangat baik; ekosistem yang sangat baik; pengalaman pengembang di bawah standar.

  * JavaScript: bahasa terpopuler sepanjang masa; ekosistem terluas.

  * Kotlin: memperbaiki begitu banyak hal dari Java; dukungan luar biasa dari JetBrains; kasus-kasus yang dipublikasikan tentang porting dari Java ke Kotlin cukup baik.
  
  * Python: bahasa terpopuler untuk administrasi sistem; perangkat analitik yang hebat; kerangka web yang baik; tetapi ditinggalkan oleh Google demi Go.

  * Ruby: pengalaman pengembang terbaik sepanjang masa; kerangka web terbaik; komunitas paling ramah; tetapi sangat lambat; agak sulit dikemas.

  * Rust: bahasa baru terbaik; menekankan nol abstraksi; menekankan konkurensi; namun ekosistemnya relatif kecil; dan memiliki batasan yang disengaja pada beberapa jenis akselerasi kompiler, misalnya akses memori langsung harus ditandai secara eksplisit sebagai tidak aman.

  * TypeScript: menambahkan tipe ke JavaScript; transpiler yang hebat; meningkatnya penekanan pengembang pada porting dari JavaScript ke TypeScript; dukungan kuat dari Microsoft.

Kami memutuskan bahwa VM memiliki serangkaian trade-off yang tidak kami butuhkan saat ini, seperti kompleksitas tambahan yang menyediakan kemampuan waktu proses.

Kami yakin keputusan inti kami didorong oleh dua kekhawatiran lintas bidang:

  * Untuk kecepatan waktu proses tercepat dan akses sistem terketat, kami akan memilih JavaScript dan C.

  * Untuk kecepatan waktu proses mendekati tercepat dan akses sistem mendekati terketat, kami memilih TypeScript dan Rust.

Penghargaan khusus diberikan kepada bahasa VM dan kerangka web yang akan kami pilih jika kami menginginkan bahasa VM:

  * Clojure dan Luminus

  * Java dan Spring

  * Elixir dan Phoenix


### Implikasi

Pengembang front-end perlu mempelajari TypeScript. Ini kemungkinan kurva belajar yang mudah jika pengalaman utama pengembang adalah menggunakan JavaScript.

Pengembang back-end perlu mempelajari Rust. Ini kemungkinan kurva belajar yang sedang jika pengalaman utama pengembang adalah menggunakan C/C++, dan kurva belajar yang sulit jika pengalaman utama pengembang adalah menggunakan Java, Python, Ruby, atau bahasa berkelola memori serupa. 

TypeScript dan Rust keduanya relatif baru. Ini berarti banyak alat belum memiliki dokumentasi untuk bahasa-bahasa ini. Misalnya, pipeline devops perlu disiapkan untuk bahasa-bahasa ini, dan sejauh ini, tidak ada alat devops yang kami evaluasi yang memiliki contoh bawaan untuk bahasa-bahasa ini.

Waktu kompilasi untuk TypeScript dan Rust cukup lambat. Sebagian mungkin disebabkan oleh barunya bahasa-bahasa tersebut. Kami mungkin perlu mencari cara mengurangi waktu kompilasi yang lambat, seperti kompilasi sesuai permintaan, konkurensi kompilasi, dll.

Dukungan IDE untuk bahasa-bahasa ini belum merata dan belum kelas satu. Misalnya, JetBrains menjual IDE PyCharm untuk dukungan kelas satu bagi Python, tetapi tidak menjual IDE dengan dukungan kelas satu untuk Rust; sebagai gantinya, JetBrains dapat menggunakan plugin Rust yang menyediakan mungkin 80% dukungan bahasa Rust dibandingkan dukungan bahasa Python.


## Terkait


### Keputusan terkait

Kami akan mengarahkan pilihan ekosistem yang selaras dengan bahasa-bahasa ini.

Misalnya, kami ingin memilih IDE yang memiliki kemampuan baik untuk bahasa-bahasa ini.

Misalnya, untuk kerangka web front-end kami, kami lebih mungkin memutuskan kerangka yang cenderung mengarah ke TypeScript (misalnya Vue) daripada kerangka yang cenderung mengarah ke JavaScript biasa (misalnya React).


### Persyaratan terkait

Seluruh rantai alat kami harus mendukung bahasa-bahasa ini.


### Artefak terkait

Kami memperkirakan kami mungkin mengekspor beberapa rahasia ke variabel lingkungan.


### Prinsip terkait

Ukur dua kali, bangun sekali. Kami memprioritaskan sedikit keamanan di atas sedikit kecepatan.

Waktu proses lebih berharga daripada waktu kompilasi. Kami memprioritaskan penggunaan oleh pelanggan di atas penggunaan oleh pengembang.


## Catatan

Catatan apa pun di sini.
