# Monorepo vs multirepo

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

Proyek kami melibatkan pengembangan tiga kategori utama perangkat lunak:

  * GUI front-end
  * Layanan middleware
  * Server back-end

Saat kami mengembangkan, sistem kontrol versi (VCS) manajemen kode sumber (SCM) kami adalah git.

Kami perlu memilih bagaimana menggunakan git untuk mengorganisasi kode kami.

Pilihan tingkat atas adalah mengorganisasi sebagai "monorepo" atau "polyrepo" atau "hibrida":

  * Monorepo berarti kami menaruh semua bagian ke dalam satu repo besar
  * Polyrepo berarti kami menaruh setiap bagian di repo-nya sendiri
  * Hibrida berarti campuran antara monorepo dan polyrepo

Untuk informasi lebih lanjut silakan lihat https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Keputusan

Monorepo ketika organisasi/tim/proyek relatif kecil, dan iterasi cepat lebih diprioritaskan daripada menjaga stabilitas.

Polyrepo ketika organisasi/tim/proyek relatif besar, dan menjaga stabilitas lebih diprioritaskan daripada iterasi cepat.


### Status

Diputuskan. Terbuka untuk ditinjau kembali jika/ketika alat baru tersedia untuk mengelola monorepo dan/atau polyrepo.


## Rincian


### Asumsi

Semua kode yang kami kembangkan adalah untuk produk satu organisasi, dan bukan untuk masyarakat umum. Artinya Broker-Dealer tidak bertujuan memiliki sesuatu seperti pengembang sukarelawan dari masyarakat umum.


### Batasan

Batasan terdokumentasi dengan baik di https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Posisi

Kami mempertimbangkan monorepo ala Google, Facebook, dsb. Kami menilai masalah penskalaan monorepo masih sangat jauh di masa depan sehingga kami akan dapat memanfaatkan praktik yang sama seperti Google dan Facebook, ketika saatnya kami membutuhkannya.

Kami mempertimbangkan polyrepo ala proyek sumber terbuka Git pada umumnya, seperti Google Android, Facebook React, dsb. Kami menilai ini adalah pilihan terbaik untuk partisipasi masyarakat umum (misalnya siapa pun di dunia dapat mengerjakan kode) dan ketersediaan individual (misalnya proyek digunakan sendiri, tanpa bagian lain apa pun).


### Argumen

Ketika organisasi/tim/proyek relatif kecil, kami memilih monorepo, karena iterasi cepat jauh lebih diprioritaskan daripada menjaga stabilitas

Ketika organisasi/tim/proyek relatif besar, kami memilih polyrepo, karena menjaga stabilitas jauh lebih diprioritaskan daripada iterasi cepat.


### Implikasi

Jika sudah ada pipeline untuk CI+CD, kami mungkin perlu menyesuaikannya untuk menguji beberapa proyek dalam satu repo.

CI+CD dapat memerlukan waktu lebih lama untuk build penuh pada monorepo, karena CI+CD dapat membangun semua proyek dalam monorepo.

Jika organisasi/tim/proyek berkembang, monorepo akan mengalami masalah penskalaan.

Masalah penskalaan monorepo dapat membuat transisi ke polyrepo semakin bernilai.

Transisi dari monorepo ke polyrepo adalah tugas devops yang signifikan, dan perlu direncanakan, dikelola, dan diprogram.


## Terkait


### Keputusan terkait

Kami akan membuat keputusan untuk alat terkait guna mengelola monorepo (misalnya Google Bazel) dan polyrepo (misalnya Lyft Refactorator).


### Persyaratan terkait

Kami perlu mengembangkan pipeline CI+CD agar bekerja dengan baik bersama git.


### Artefak terkait

Kami mengharapkan organisasi repo memiliki artefak terkait untuk provisioning, manajemen konfigurasi, pengujian, dan area devops serupa. 


### Prinsip terkait

Mudah dibatalkan. Jika monorepo tidak berfungsi dalam praktik, atau tidak diinginkan oleh pimpinan, mudah untuk beralih ke polyrepo.

Obsesi Pelanggan. Kami menghargai menghadirkan proyek ke tangan pelanggan, dan kami yakin monorepo dapat membawa kami ke sana lebih cepat daripada polyrepo, dan juga membantu kami beriterasi lebih cepat.

Berpikir besar. Google dan Facebook adalah pendukung yang sangat kuat monorepo dibandingkan polyrepo, karena semua produk inti dapat dikembangkan/diuji/di-deploy secara selaras.


## Catatan

Tambahkan catatan apa pun di sini.
