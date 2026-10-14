# Proses Catatan Keputusan Arsitektur AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Catatan keputusan arsitektur (architectural decision record, ADR) adalah dokumen yang menjelaskan pilihan yang dibuat tim mengenai aspek penting dari arsitektur perangkat lunak yang sedang mereka rencanakan. Setiap ADR menjelaskan keputusan arsitektur, konteksnya, dan konsekuensinya. ADR memiliki status sehingga mengikuti sebuah siklus hidup. Untuk contoh ADR, lihat lampiran.

Proses ADR menghasilkan kumpulan catatan keputusan arsitektur. Kumpulan ini membentuk log keputusan. Log keputusan memberikan konteks proyek serta informasi rinci tentang implementasi dan desain. Anggota proyek membaca sekilas judul setiap ADR untuk mendapatkan gambaran umum konteks proyek. Mereka membaca ADR untuk mendalami implementasi proyek dan pilihan desain.

Ketika tim menerima sebuah ADR, ADR tersebut menjadi tidak dapat diubah. Jika wawasan baru menuntut keputusan yang berbeda, tim mengusulkan ADR baru. Ketika tim menerima ADR baru tersebut, ADR baru itu menggantikan ADR sebelumnya.

## Lingkup proses ADR

Anggota proyek sebaiknya membuat ADR untuk setiap keputusan yang signifikan secara arsitektur dan memengaruhi proyek atau produk perangkat lunak, termasuk hal-hal berikut (Richards dan Ford 2020):

* Struktur (misalnya, pola seperti microservices)

* Persyaratan nonfungsional (keamanan, ketersediaan tinggi, dan toleransi kesalahan)

* Dependensi (keterkaitan antarkomponen)

* Antarmuka (API dan kontrak yang dipublikasikan)

* Teknik konstruksi (pustaka, kerangka kerja, alat, dan proses)

* Persyaratan fungsional dan nonfungsional adalah masukan yang paling umum untuk proses ADR.


## Isi ADR

Ketika tim mengidentifikasi kebutuhan akan sebuah ADR, seorang anggota tim mulai menulis ADR berdasarkan templat yang berlaku untuk seluruh proyek. (Lihat organisasi ADR di GitHub untuk contoh templat.) Templat menyederhanakan pembuatan ADR dan memastikan ADR memuat semua informasi yang relevan. Paling sedikit, setiap ADR harus mendefinisikan konteks keputusan, keputusan itu sendiri, serta konsekuensi keputusan bagi proyek dan hasil kerjanya. (Untuk contoh bagian-bagian ini, lihat lampiran.) Salah satu aspek paling kuat dari struktur ADR adalah fokusnya pada alasan di balik keputusan, bukan pada cara tim mengimplementasikannya. Memahami mengapa tim membuat keputusan tersebut membuat anggota tim lain lebih mudah menerimanya, dan mencegah arsitek lain yang tidak terlibat dalam proses pengambilan keputusan membatalkan keputusan itu di kemudian hari.


## Proses adopsi ADR

Setiap anggota tim dapat membuat ADR, tetapi tim sebaiknya menetapkan definisi kepemilikan untuk sebuah ADR. Setiap penulis yang menjadi pemilik ADR harus secara aktif memelihara dan mengomunikasikan isi ADR. Untuk memperjelas kepemilikan ini, panduan ini menyebut penulis ADR sebagai pemilik ADR pada bagian-bagian berikut. Anggota tim lain selalu dapat berkontribusi pada sebuah ADR. Jika isi ADR berubah sebelum tim menerimanya, pemilik harus menyetujui perubahan tersebut.

Setelah tim mengidentifikasi sebuah keputusan arsitektur dan pemiliknya, pemilik ADR menyerahkan ADR dalam status **Proposed** (Diusulkan) pada awal proses. ADR dalam status Proposed siap untuk ditinjau.

Pemilik ADR kemudian memulai proses tinjauan untuk ADR tersebut. Tujuan proses tinjauan ADR adalah memutuskan apakah tim menerima ADR, menyimpulkan bahwa ADR perlu diperbaiki, atau menolak ADR. Tim proyek, termasuk pemilik, meninjau ADR. Rapat tinjauan sebaiknya dimulai dengan waktu khusus untuk membaca ADR. Rata-rata, 10 hingga 15 menit sudah cukup. Selama waktu ini, setiap anggota tim membaca dokumen dan menambahkan komentar serta pertanyaan untuk menandai topik yang tidak jelas. Setelah fase tinjauan, pemilik ADR membacakan dan membahas setiap komentar bersama tim.

Jika tim menemukan butir tindakan untuk memperbaiki ADR, status ADR tetap **Proposed**. Pemilik ADR merumuskan tindakan tersebut dan, bersama tim, menetapkan penanggung jawab untuk setiap tindakan. Setiap anggota tim dapat berkontribusi dan menyelesaikan butir tindakan. Pemilik ADR bertanggung jawab menjadwalkan ulang proses tinjauan.

Tim juga dapat memutuskan untuk menolak ADR. Dalam hal ini, pemilik ADR menambahkan alasan penolakan untuk mencegah diskusi berulang tentang topik yang sama. Pemilik mengubah status ADR menjadi **Rejected** (Ditolak).

Jika tim menyetujui ADR, pemilik menambahkan stempel waktu, versi, dan daftar pemangku kepentingan. Pemilik kemudian memperbarui status menjadi **Accepted** (Diterima).

ADR dan log keputusan yang dibentuknya mewakili keputusan yang dibuat oleh tim dan menyediakan riwayat semua keputusan. Tim menggunakan ADR sebagai acuan selama tinjauan kode dan arsitektur jika memungkinkan. Selain melakukan tinjauan kode, tugas desain, dan tugas implementasi, anggota tim sebaiknya merujuk ADR untuk keputusan strategis produk.

Sebagai praktik yang baik, setiap perubahan perangkat lunak harus melalui tinjauan sejawat dan memerlukan setidaknya satu persetujuan. Selama tinjauan kode, peninjau kode mungkin menemukan perubahan yang melanggar satu atau lebih ADR. Dalam hal ini, peninjau meminta penulis perubahan kode untuk memperbarui kodenya, dan membagikan tautan ke ADR tersebut. Ketika penulis memperbarui kode, kode itu disetujui oleh peninjau sejawat dan digabungkan ke basis kode utama.


## Proses tinjauan ADR

Tim sebaiknya memperlakukan ADR sebagai dokumen yang tidak dapat diubah setelah tim menerima atau menolaknya. Perubahan pada ADR yang sudah ada mengharuskan pembuatan ADR baru, penetapan proses tinjauan untuk ADR baru, dan persetujuan ADR tersebut. Jika tim menyetujui ADR baru, pemilik harus mengubah status ADR lama menjadi **Superseded** (Digantikan). 
