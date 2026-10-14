# Microsoft Azure DevOps

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
  * [Microsoft Devops CI: An Unsatisfying Adventure](#microsoft-devops-ci-an-unsatisfying-adventure)
  * [Sorotan diskusi Hacker News](#sorotan-diskusi-hacker-news)
  * [Windows Development MVP](#windows-development-mvp)
  * [Ringkasan Edward Thomson (Azure PM)](#ringkasan-edward-thomson-azure-pm)


## Ringkasan


### Isu

Kami ingin menggunakan devops untuk membangun, mengintegrasikan, men-deploy, dan meng-host proyek kami. Kami mempertimbangkan Microsoft Azure DevOps.

  * Kami ingin pengalaman pengembang yang cepat dan andal, baik untuk penyiapan devops, misalnya konfigurasi, maupun penggunaan berkelanjutan, misalnya waktu build yang cepat.
  
  * Kami ingin mempertimbangkan penggunaan Microsoft Azure secara keseluruhan, untuk meng-host aplikasi proyek, basis data, dll.


### Keputusan

Memutuskan untuk tidak menggunakan Microsoft Azure DevOps.


### Status

Diputuskan. Terbuka untuk ditinjau kembali jika/ketika informasi penting yang baru datang.


## Rincian


### Asumsi

Semua asumsi devops yang biasa, seperti dalam buku Accelerate.

  * Build yang cepat sangat membantu. Ini mempercepat putaran umpan balik.

  * Kami dapat menukar masuk/keluar bagian dari vendor alternatif, yaitu kami mungkin ingin membawa server build berkecepatan lebih tinggi milik kami sendiri, atau menggunakan sistem kontrol versi pilihan kami sendiri, atau berkoordinasi dengan server integrasi berkelanjutan yang di-hosting sendiri.
  
  * Kemudahan penggunaan yang efisien sangat membantu, untuk pengalaman pengembang, dan pada gilirannya untuk area yang halus seperti konsistensi, kejelasan, keamanan, dan kemudahan kurva belajar.

  * Ketika ada yang rusak atau bermasalah, kami menginginkan cara yang efektif untuk melaporkan masalah tersebut. Ini sangat penting untuk masalah apa pun yang berkaitan dengan keamanan.


### Batasan

Tidak ada yang diketahui. Azure memiliki komitmen yang dipublikasikan untuk bekerja baik dengan alat eksternal.


### Posisi

Kami mempertimbangkan penggunaan Microsoft Azure Devops vs. AWS yang merupakan petahana.

Kami bereksperimen dengan Azure DevOps, Azure Pipelines, Azure Repo, dan peluncuran server baru Azure melalui Terraform.

Kami bereksperimen dengan mendapatkan dukungan dari perwakilan Microsoft.

Kami mengumpulkan informasi dari rekan sejawat di blog dan Hacker News.


### Argumen

Azure DevOps mengiklankan serangkaian penawaran yang luar biasa, tetapi tidak sesuai kenyataan, tidak bekerja dengan baik bersama-sama, dan dukungannya buruk.

Pengalaman langsung kami:

  * Penyiapan Azure adalah kekacauan UI, beberapa di antaranya tumpang tindih dengan akun Microsoft, beberapa tidak. Misalnya ada masuk Azure, masuk Microsoft.com, masuk Live.com, dll. dan semuanya berlaku secara bersamaan.

  * Kami menemukan masalah keamanan kecil selama penyiapan, dan tidak menemukan penyelesaian. Kami mencoba banyak cara untuk melaporkannya, kepada banyak perwakilan Microsoft, tanpa hasil. Kami berhasil melaporkannya kepada tim keamanan Microsoft, yang membalas dengan won't fix.

  * Dokumentasi sering kali salah atau sudah usang. Setidaknya sebagian dari ini disebabkan oleh mesin pencari Microsoft yang buruk, dan sebagian disebabkan oleh SEO yang di bawah standar.
  
  * Penyiapan Terraform terdokumentasi dengan baik, dan berfungsi. Namun, dukungan Terraform lemah dibandingkan AWS karena Microsoft sedang membangun hubungan bisnis dengan vendor untuk membuat contoh penyiapan Terraform berantai.

Pengalaman rekan sejawat kami:

  * Setelah kami melakukan penilaian buta sendiri, kami mencari pengalaman rekan sejawat. Apa yang kami temukan mengonfirmasi pengalaman kami.

  * Rekan sejawat melaporkan masalah tambahan dengan waktu build, dan masalah dengan server build bawa-sendiri. Masalah ini jauh lebih parah daripada masalah UI, karena melakukan build adalah tujuan inti pipeline build, dan kami berharap melakukan banyak build per hari.

  * Kami menemukan partisipasi yang sangat baik dari rekan tim Azure di area diskusi. Penghargaan untuk Microsoft untuk hal ini. Kami sangat terkesan dengan Edward Thomson, PM dan pembuat kode Azure, karena partisipasinya, keterusterangannya, dan penjelasan teknisnya.


### Implikasi

Memilih Microsoft Azure DevOps tampaknya akan lebih mahal (~3x) dalam waktu dan biaya dibandingkan tidak memilih Azure.


## Terkait


### Keputusan terkait

Jika kami memilih Azure DevOps, ada banyak penawaran terkait, termasuk Azure Repo, Azure Pipeline, dll. Kami yakin bahwa jika kami memilih Azure Devops, hal ini mungkin memudahkan penggunaan lebih banyak kemampuan Azure, atau mungkin mempersulit penggunaan kemampuan vendor lain.

Kami yakin Microsoft membuat kemajuan besar dalam pengalaman pengembang, dan kami melihat Microsoft melakukan akuisisi besar atas alat pengembang (misalnya GitHub) dan dependensi (misalnya Citus).

Jika kami memilih Azure DevOps, kami mungkin ingin menekankan pemilihan penawaran hasil akuisisi Microsoft, dan kami juga mungkin ingin mendekati penawaran hasil akuisisi dengan lebih hati-hati/penilaian karena potensi penolakan jaringan, misalnya risiko pergantian staf.


### Persyaratan terkait

Kami ingin waktu build sangat cepat. Kami bersedia membayar premi tinggi untuk ini. Hal ini karena kami ingin beriterasi dengan sangat cepat.

Kami ingin keandalan sangat tinggi. Kami bersedia membayar premi tinggi untuk ini. Hal ini karena kami menguji kasus penggunaan bernilai tinggi, termasuk transaksi keuangan, transaksi rahasia, dll.

4 KPI devops teratas kami mencakup waktu rata-rata pemulihan, yang mengharuskan build cepat dan keandalan tinggi.


### Artefak terkait

Kami ingin sistem build menghasilkan artefak yang cocok untuk digunakan di sistem lain, seperti Artifactory.


### Prinsip terkait

Mudah dibatalkan. Kami dapat mengevaluasi Azure DevOps secara paralel dengan AWS yang merupakan petahana.


## Catatan


### Microsoft Devops CI: An Unsatisfying Adventure

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Pos blog.

"Sebagai pengembang perangkat lunak, saya tahu secara langsung betapa sulitnya membangun produk berkualitas dengan cepat dan murah. Ini adalah bentuk seni yang kadang kami lakukan dengan benar, dan di lain waktu berubah menjadi sesuatu seperti situs web pemerintah layanan kesehatan era Obama. Tingkat kendali kami atas produk yang dihasilkan bervariasi, dan kesalahan atas kegagalan sering kali jatuh pada orang yang salah dalam hierarki pengambilan keputusan. Azure DevOps milik Microsoft (sebelumnya dikenal sebagai Visual Studio Team Services), meskipun jelas berniat baik, adalah badai sempurna dari keputusan buruk dan eksekusi yang buruk."


### Sorotan diskusi Hacker News

https://news.ycombinator.com/item?id=18983586

"Kami menggunakan Azure DevOps secara ekstensif di tempat kerja saya dan, setelah menggunakan GitHub, Gitlab, solusi yang di-hosting sendiri, Jenkins, TeamCity... Azure DevOps berada di peringkat paling akhir."

"UI-nya sangat kaku di mana-mana. Yang terburuk bagi saya adalah pull request. Sangat sulit bekerja dengan orang lain pada sebuah pull request. Saya bahkan tidak bisa menunjuk satu masalah tertentu - bagi kami semuanya rusak di mana-mana."

"Azure Devops adalah sesuatu yang ingin saya cintai. UI-nya terus berubah, tetapi tidak memperbaiki bug mendasar yang sudah ada sejak lama."

"Alat-alatnya tidak terintegrasi dengan baik, UI-nya sangat lambat, tidak ada tampilan dasbor pull request, build, rilis, dll. yang aktif untuk repo favorit saya. Waktu Build/Deploy sangat lambat."

"Kami juga mencoba menggunakan Azure Boards (Work Items, Boards, Backlogs, dll). Aduh. UI-nya adalah kekacauan total dari gagasan-gagasan yang terputus-putus. Alih-alih mengimplementasikan satu hal dengan baik, mereka mengimplementasikan dua lusin hal dengan buruk."


### Windows Development MVP

Saya MVP Windows Development di sini. Saya merasa harus memikul sebagian tanggung jawab karena tidak lebih lantang menyuarakan masalah-masalah ini. Tetapi harus saya katakan, saya kecewa mendengar Anda "terkejut" dengan masalah UX tersebut. Saya sudah memberi tahu tim Anda bahwa UX-nya mengerikan (misalnya sejak sebelum peluncuran) dan terus mendengar jawaban "kami tahu, kami sedang memperbaikinya". Saya akan mulai memformalkan umpan balik dan mendorongnya melalui saluran, tunggu kabar selanjutnya. Saya juga tinggal di dekat sana (Bellevue), ingin sekali datang dan mencoba membuat pipeline untuk aplikasi oss .net/wpf/uwp kami yang relatif sederhana. Saya menduga ini akan membuka mata kita berdua.

Beberapa contoh:

* Anda tidak dapat membangun pipeline dengan repo git yang berisi submodule

* Saya merasa mustahil menyunting PATH untuk beberapa alat kustom

* Pengalaman Pipeline Baru sama sekali tidak masuk akal, pengguna baru yang mengeklik ke sana kemari pada akhirnya akan sampai ke Docs yang salah.


### Ringkasan Edward Thomson (Azure PM)

Saya menulis kode yang menggabungkan pull request Anda. Program Manager di Microsoft untuk Azure DevOps; sebelumnya software engineer pada alat kontrol versi di GitHub, Microsoft, SourceGear.

https://www.edwardthomson.com/

Ko-maintainer libgit2. https://libgit2.github.io

Ko-pembawa acara All Things Git, Podcast tentang Git. https://www.allthingsgit.com/

Kurator Developer Tools Weekly, buletin tentang alat pengembangan. https://developertoolsweekly.com/
