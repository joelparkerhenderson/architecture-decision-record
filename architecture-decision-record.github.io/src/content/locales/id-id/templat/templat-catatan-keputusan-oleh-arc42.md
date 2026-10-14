# Templat catatan keputusan oleh arc42

<https://arc42.org/overview>

## 1. Pendahuluan dan Tujuan

Deskripsi singkat tentang persyaratan, kekuatan pendorong, ekstrak (atau abstrak) dari
persyaratan. Tiga (maksimal lima) tujuan kualitas teratas untuk arsitektur yang memiliki
prioritas tertinggi bagi para pemangku kepentingan utama. Tabel pemangku kepentingan penting
beserta harapan mereka terhadap arsitektur.

## 1.1 Gambaran Umum Persyaratan

### Isi

Deskripsi singkat tentang persyaratan fungsional, kekuatan pendorong, ekstrak (atau
abstrak) dari persyaratan. Tautan ke dokumen persyaratan (yang semoga sudah ada), dengan informasi tentang di mana menemukannya. 

### Motivasi

Dari sudut pandang pengguna akhir, sebuah sistem dibuat atau dimodifikasi untuk
meningkatkan dukungan terhadap suatu aktivitas bisnis dan/atau meningkatkan kualitas. 

### Bentuk

Deskripsi tekstual singkat, mungkin dalam format kasus penggunaan berbentuk tabel. Jika dokumen
persyaratan sudah ada, gambaran umum ini harus merujuk ke dokumen-dokumen tersebut.

Buatlah kutipan ini sesingkat mungkin. Seimbangkan keterbacaan dokumen ini
dengan potensi redundansi terhadap dokumen persyaratan. 

## 1.2 Tujuan kualitas

### Isi

Tiga (maksimal lima) tujuan kualitas teratas untuk arsitektur yang pemenuhannya
sangat penting bagi para pemangku kepentingan utama. Yang kami maksud adalah benar-benar tujuan kualitas
untuk arsitektur. Jangan mengacaukannya dengan tujuan proyek. Keduanya tidak
selalu identik. Standar ISO 25010 memberikan gambaran umum yang bagus tentang
topik-topik potensial yang menarik.

### Motivasi

Anda harus mengetahui tujuan kualitas para pemangku kepentingan terpenting Anda, karena
tujuan tersebut akan memengaruhi keputusan arsitektur yang mendasar. Pastikan untuk sangat
konkret mengenai kualitas-kualitas ini, hindari kata-kata jargon. Jika Anda sebagai arsitek tidak
tahu bagaimana kualitas pekerjaan Anda akan dinilai …

### Bentuk

Tabel berisi tujuan kualitas terpenting dan skenario konkret, diurutkan berdasarkan prioritas.

## 1.3 Pemangku kepentingan

### Isi

Gambaran umum eksplisit tentang pemangku kepentingan sistem, yaitu semua orang, peran, atau
organisasi yang

- harus mengetahui arsitektur

- harus diyakinkan tentang arsitektur

- harus bekerja dengan arsitektur atau dengan kode

- membutuhkan dokumentasi arsitektur untuk pekerjaan mereka

- harus membuat keputusan tentang sistem atau pengembangannya

### Motivasi

Anda harus mengetahui semua pihak yang terlibat dalam pengembangan sistem atau terdampak oleh
sistem. Jika tidak, Anda mungkin mendapat kejutan yang tidak menyenangkan di kemudian hari dalam proses
pengembangan. Para pemangku kepentingan ini menentukan cakupan dan tingkat detail dari
pekerjaan Anda dan hasilnya.

### Bentuk

Tabel dengan nama peran, nama orang, dan harapan mereka terhadap
arsitektur dan dokumentasinya.

## 2. Batasan

Segala sesuatu yang membatasi tim dalam keputusan desain dan implementasi atau
keputusan tentang proses terkait. Terkadang dapat melampaui sistem individual dan
berlaku untuk seluruh organisasi dan perusahaan.

### Isi

Setiap persyaratan yang membatasi kebebasan arsitek perangkat lunak dalam keputusan desain
dan implementasi atau keputusan tentang proses pengembangan. Batasan-batasan
ini terkadang melampaui sistem individual dan berlaku untuk seluruh
organisasi dan perusahaan.

### Motivasi

Arsitek harus tahu persis di mana mereka bebas dalam keputusan desain mereka dan
di mana mereka harus mematuhi batasan. Batasan harus selalu ditangani;
meskipun demikian, batasan mungkin dapat dinegosiasikan.

### Bentuk

Tabel batasan sederhana beserta penjelasannya. Jika perlu, Anda dapat membaginya
menjadi batasan teknis, batasan organisasi dan politik, serta
konvensi (misalnya pedoman pemrograman atau pemberian versi, konvensi dokumentasi atau penamaan)

## 3. Konteks dan Lingkup

Membatasi sistem Anda dari mitra komunikasinya (eksternal) (sistem
tetangga dan pengguna). Menentukan antarmuka eksternal. Ditampilkan dari
perspektif bisnis/domain (selalu) atau perspektif teknis (opsional)

### Isi

Lingkup dan konteks sistem - seperti namanya - membatasi sistem Anda (yaitu
lingkup Anda) dari semua mitra komunikasinya (sistem tetangga dan pengguna,
yaitu konteks sistem Anda). Dengan demikian ia menentukan antarmuka eksternal.

Jika perlu, bedakan konteks bisnis (masukan dan keluaran khusus domain) dari konteks teknis (saluran, protokol, perangkat keras).

### Motivasi

Antarmuka domain dan antarmuka teknis ke mitra komunikasi termasuk
aspek paling kritis dari sistem Anda. Pastikan Anda memahaminya sepenuhnya.

### Bentuk

- Berbagai diagram konteks

- Daftar mitra komunikasi dan antarmuka mereka.

## 3.1 Konteks bisnis

### Isi

Spesifikasi semua mitra komunikasi (pengguna, sistem TI, …) dengan
penjelasan masukan dan keluaran atau antarmuka khusus domain. Secara opsional Anda
dapat menambahkan format khusus domain atau protokol komunikasi.

### Motivasi

Semua pemangku kepentingan harus memahami data apa yang dipertukarkan dengan lingkungan
sistem.

### Bentuk

Semua jenis diagram yang menampilkan sistem sebagai kotak hitam dan menentukan antarmuka
domain ke mitra komunikasi.

Atau (atau sebagai tambahan) Anda dapat menggunakan tabel. Judul tabel adalah
nama sistem Anda, ketiga kolom berisi nama mitra
komunikasi, masukan, dan keluaran.

## 3.2 Konteks teknis

### Isi

Antarmuka teknis (saluran dan media transmisi) yang menghubungkan sistem Anda dengan
lingkungannya. Selain itu pemetaan masukan/keluaran khusus domain ke
saluran, yaitu penjelasan masukan/keluaran mana yang menggunakan saluran mana.

### Motivasi

Banyak pemangku kepentingan membuat keputusan arsitektur berdasarkan antarmuka teknis
antara sistem dan konteksnya. Terutama perancang infrastruktur atau perangkat keras
yang menentukan antarmuka teknis ini.

### Bentuk

Misalnya diagram deployment UML yang menjelaskan saluran ke sistem tetangga, bersama
dengan tabel pemetaan yang menunjukkan hubungan antara saluran dan
masukan/keluaran.

## 4. Strategi Solusi

Ringkasan keputusan mendasar dan strategi solusi yang membentuk
arsitektur. Dapat mencakup teknologi, dekomposisi tingkat atas, pendekatan untuk
mencapai tujuan kualitas utama, dan keputusan organisasi yang relevan.

### Isi

Ringkasan singkat dan penjelasan tentang keputusan mendasar dan strategi solusi yang membentuk arsitektur sistem. Ini mencakup

- keputusan teknologi

- keputusan tentang dekomposisi tingkat atas sistem, misalnya penggunaan pola arsitektur atau pola desain

- keputusan tentang cara mencapai tujuan kualitas utama

- keputusan organisasi yang relevan, misalnya memilih proses pengembangan atau mendelegasikan tugas tertentu kepada pihak ketiga.

### Motivasi

Keputusan-keputusan ini membentuk batu penjuru bagi arsitektur Anda. Keputusan ini menjadi dasar
bagi banyak keputusan rinci atau aturan implementasi lainnya.

### Bentuk

Buatlah penjelasan keputusan-keputusan kunci ini singkat.

Jelaskan motivasi dari apa yang Anda putuskan dan mengapa Anda memutuskan demikian, berdasarkan
pernyataan masalah, tujuan kualitas, dan batasan utama Anda. Rujuklah detail pada
bagian-bagian berikut (bagian 5 untuk detail struktural, bagian 8 untuk
konsep lintas bidang).

Anda dapat menggunakan daftar pendekatan solusi atau tabel.

## 5. Tampilan Blok Bangunan

Dekomposisi statis sistem, abstraksi kode sumber, ditampilkan sebagai
hierarki kotak putih (yang berisi kotak hitam), hingga tingkat detail yang
sesuai.

### Isi

Tampilan blok bangunan menunjukkan dekomposisi statis sistem menjadi
blok bangunan (modul, komponen, subsistem, kelas, antarmuka, paket,
pustaka, kerangka kerja, lapisan, partisi, tingkatan, fungsi, makro, operasi,
struktur data, …) serta dependensinya (hubungan, asosiasi,
…)

Tampilan ini wajib ada untuk setiap dokumentasi arsitektur. Dalam analogi dengan
sebuah rumah, ini adalah denah lantai.

### Motivasi

Pertahankan gambaran umum kode sumber Anda dengan membuat strukturnya dapat dipahami
melalui abstraksi.

Hal ini memungkinkan Anda berkomunikasi dengan pemangku kepentingan pada tingkat abstrak
tanpa mengungkapkan detail implementasi.

### Bentuk

Tampilan blok bangunan adalah kumpulan hierarkis kotak hitam dan kotak putih
(lihat gambar di bawah) beserta deskripsinya.

## 5.1 Kotak Putih Sistem Keseluruhan

Di sini Anda menjelaskan dekomposisi sistem keseluruhan menggunakan templat kotak putih berikut. Isinya mencakup

- diagram gambaran umum

- motivasi untuk dekomposisi

- deskripsi kotak hitam dari blok bangunan yang terkandung. Untuk ini kami menawarkan alternatif:

  - gunakan satu tabel untuk gambaran umum yang singkat dan pragmatis dari semua blok bangunan yang terkandung dan antarmukanya

  - gunakan daftar deskripsi kotak hitam dari blok bangunan sesuai dengan templat kotak hitam (lihat di bawah). Tergantung pilihan alat Anda, daftar ini dapat berupa subbab (dalam file teks), subhalaman (dalam Wiki) atau elemen bersarang (dalam alat pemodelan).

  - (opsional:) antarmuka penting yang tidak dijelaskan dalam templat kotak hitam sebuah blok bangunan, tetapi sangat penting untuk memahami kotak putih.

Karena ada begitu banyak cara untuk menentukan antarmuka, kami tidak menyediakan templat khusus untuk itu.

Dalam kasus terbaik, Anda cukup memberikan contoh atau tanda tangan sederhana.

## 5.2 Tingkat 2

Di sini Anda dapat menentukan struktur internal (beberapa) blok bangunan dari tingkat 1
sebagai kotak putih.

Anda harus memutuskan blok bangunan mana dari sistem Anda yang cukup penting untuk
membenarkan deskripsi sedetail itu. Utamakan relevansi daripada kelengkapan.
Tentukan blok bangunan yang penting, mengejutkan, berisiko, kompleks, atau mudah berubah. Lewati
bagian sistem Anda yang normal, sederhana, membosankan, atau terstandardisasi

### 5.2.1 Kotak Putih untuk blok bangunan 1

Menentukan struktur internal blok bangunan 1.

Gunakan templat kotak putih (lihat di atas).

## 6. Tampilan Waktu Proses

Perilaku blok bangunan sebagai skenario, mencakup kasus penggunaan atau
fitur penting, interaksi pada antarmuka eksternal yang kritis, operasi dan
administrasi serta perilaku kesalahan dan pengecualian.

### Isi

Tampilan waktu proses (runtime) menjelaskan perilaku konkret dan interaksi blok bangunan sistem dalam bentuk skenario dari area-area berikut:

- kasus penggunaan atau fitur penting: bagaimana blok bangunan mengeksekusinya?

- interaksi pada antarmuka eksternal yang kritis: bagaimana blok bangunan bekerja sama dengan pengguna dan sistem tetangga?

- operasi dan administrasi: peluncuran, penyalaan, penghentian

- skenario kesalahan dan pengecualian

Catatan: Kriteria utama untuk memilih skenario yang mungkin (urutan, alur kerja) adalah relevansi arsitekturalnya. Tidak penting menjelaskan sejumlah besar skenario. Sebaiknya dokumentasikan pilihan yang representatif.

### Motivasi

Anda harus memahami bagaimana (instans) blok bangunan sistem Anda menjalankan tugasnya dan berkomunikasi pada waktu proses. Anda terutama akan menangkap skenario dalam dokumentasi untuk mengomunikasikan arsitektur Anda kepada pemangku kepentingan yang kurang bersedia atau mampu membaca dan memahami model statis (tampilan blok bangunan, tampilan deployment).

### Bentuk

Ada banyak notasi untuk menjelaskan skenario, misalnya


- daftar langkah bernomor (dalam bahasa alami)

- diagram aktivitas atau diagram alir

- diagram urutan

- BPMN atau EPC (event process chains)

- mesin status

- dll.

## 6.n Skenario Waktu Proses n (1, 2, 3, dst.)

Sisipkan diagram waktu proses atau deskripsi tekstual skenario.

Sisipkan deskripsi aspek-aspek penting dari interaksi antara instans blok bangunan yang digambarkan dalam diagram ini.

## 7. Tampilan Deployment

Infrastruktur teknis dengan lingkungan, komputer, prosesor, topologi.
Pemetaan blok bangunan (perangkat lunak) ke elemen infrastruktur.

### Isi

Tampilan deployment menjelaskan:

- infrastruktur teknis yang digunakan untuk menjalankan sistem Anda, dengan elemen
  infrastruktur seperti lokasi geografis, lingkungan, komputer, prosesor,
  saluran dan topologi jaringan serta elemen infrastruktur lainnya dan

- pemetaan blok bangunan (perangkat lunak) ke elemen infrastruktur tersebut.

Sering kali sistem dijalankan di lingkungan yang berbeda, misalnya lingkungan
pengembangan, lingkungan pengujian, lingkungan produksi. Dalam kasus seperti itu Anda harus
mendokumentasikan semua lingkungan yang relevan.

Dokumentasikan tampilan deployment terutama ketika perangkat lunak Anda dijalankan sebagai
sistem terdistribusi dengan lebih dari satu komputer, prosesor, server atau kontainer
atau ketika Anda merancang dan membangun prosesor dan chip perangkat keras Anda sendiri.

Dari perspektif perangkat lunak, cukup menangkap elemen-elemen
infrastruktur yang diperlukan untuk menunjukkan deployment blok bangunan Anda.
Arsitek perangkat keras dapat melampaui itu dan menjelaskan infrastruktur hingga tingkat
detail apa pun yang perlu mereka tangkap. 

### Motivasi

Perangkat lunak tidak berjalan tanpa perangkat keras. Infrastruktur yang mendasarinya dapat dan
akan memengaruhi sistem Anda dan/atau beberapa konsep lintas bidang. Karena itu, Anda
perlu mengetahui infrastrukturnya.

### Bentuk

Mungkin diagram deployment tingkat tertinggi sudah ada di bagian 3.2 sebagai konteks teknis dengan infrastruktur Anda sendiri sebagai SATU kotak hitam. Di bagian ini Anda akan memperbesar kotak hitam tersebut menggunakan diagram deployment tambahan.

- UML menawarkan diagram deployment untuk mengekspresikan tampilan tersebut. Gunakan, mungkin dengan diagram bersarang, ketika infrastruktur Anda lebih kompleks.

- Ketika pemangku kepentingan (perangkat keras) Anda lebih menyukai jenis diagram lain daripada
  diagram deployment UML, biarkan mereka menggunakan jenis apa pun yang mampu menunjukkan node dan
  saluran infrastruktur.

## 7.1 Infrastruktur Tingkat 1

Jelaskan (biasanya dalam kombinasi diagram, tabel, dan teks):

- distribusi sistem Anda ke beberapa lokasi, lingkungan, komputer, prosesor, .. serta koneksi fisik di antaranya

- justifikasi atau motivasi penting untuk struktur deployment ini

- fitur kualitas dan/atau kinerja infrastruktur

- pemetaan artefak perangkat lunak (blok bangunan) ke elemen infrastruktur

Untuk beberapa lingkungan atau deployment alternatif, silakan salin bagian arc42 itu untuk semua lingkungan yang relevan. **

## 7.2 Infrastruktur Tingkat 2

Di sini Anda dapat menyertakan struktur internal (beberapa) elemen infrastruktur dari infrastruktur tingkat 1.

Silakan salin struktur dari tingkat 1 untuk setiap elemen yang dipilih.

## 8. Konsep Lintas Bidang

Secara keseluruhan, regulasi utama dan pendekatan solusi yang relevan di beberapa
bagian (→ lintas bidang) sistem. Konsep sering berkaitan dengan beberapa
blok bangunan. Sertakan berbagai topik seperti model domain, pola dan gaya
arsitektur, aturan penggunaan teknologi tertentu, dan aturan
implementasi.

### Isi

Bagian ini menjelaskan konsep lintas bidang (praktik, pola, regulasi
atau ide solusi). Konsep semacam itu sering berkaitan dengan beberapa blok bangunan.
Konsep dapat mencakup banyak topik yang berbeda.

### Motivasi

Konsep membentuk dasar integritas konseptual (konsistensi, homogenitas) dari
arsitektur. Dengan demikian, konsep merupakan kontribusi penting untuk mencapai kualitas
internal sistem Anda.

Inilah tempat dalam templat yang kami sediakan untuk spesifikasi yang kohesif
dari konsep-konsep tersebut.

Banyak dari konsep ini berkaitan dengan atau memengaruhi beberapa blok bangunan Anda.

### Bentuk

Bentuknya dapat bervariasi:

- makalah konsep dengan struktur apa pun

- contoh implementasi, terutama untuk konsep teknis

- kutipan model lintas bidang atau skenario yang menggunakan notasi tampilan arsitektur

### Struktur bagian ini

Pilih hanya topik yang paling dibutuhkan untuk sistem Anda dan beri masing-masing judul tingkat 2 di bagian ini (misalnya 8.1, 8.2 dst).

- JANGAN MENCOBA mencakup semua topik dari diagram yang disebutkan di atas.

### Latar belakang

Beberapa topik dalam sistem sering menyangkut beberapa blok bangunan, elemen
perangkat keras, atau proses pengembangan. Mungkin lebih mudah mengomunikasikan atau mendokumentasikan
topik lintas bidang seperti itu di satu lokasi pusat, daripada mengulanginya dalam
deskripsi blok bangunan, elemen perangkat keras, atau proses
pengembangan yang bersangkutan.

Konsep tertentu mungkin menyangkut semua elemen sistem, yang lain mungkin hanya
relevan bagi sebagian kecil.

## 9. Keputusan Arsitektur

Keputusan arsitektur yang penting, mahal, kritis, berskala besar, atau berisiko
beserta alasannya.

### Isi

Keputusan arsitektur yang penting, mahal, berskala besar, atau berisiko beserta
alasannya. Dengan “keputusan” yang kami maksud adalah memilih satu alternatif berdasarkan
kriteria yang diberikan.

Gunakan pertimbangan Anda untuk memutuskan apakah suatu keputusan arsitektur sebaiknya
didokumentasikan di sini pada bagian pusat ini atau sebaiknya didokumentasikan
secara lokal (misalnya dalam templat kotak putih sebuah blok bangunan). Hindari
teks yang berulang. Rujuklah bagian 4, tempat Anda sudah menangkap keputusan
terpenting dari arsitektur Anda.

### Motivasi

Para pemangku kepentingan sistem Anda harus dapat memahami dan menelusuri kembali
keputusan Anda.

### Bentuk

- ADR (catatan keputusan arsitektur) untuk setiap keputusan penting

- daftar atau tabel, diurutkan berdasarkan kepentingan dan konsekuensi atau

- lebih rinci dalam bentuk bagian terpisah untuk setiap keputusan

### Latar belakang (tentang ADR)

Potongan dokumentasi yang lebih kecil lebih mudah dibaca, dibuat, dan dipelihara. Dalam hal
keputusan arsitektur, tim pengembangan sering kali:

- mengetahui keputusan tersebut, karena terlihat misalnya di kode sumber, tetapi

- tidak mengetahui motivasi di balik keputusan itu (lihat Nygard 2011)

Karena itu Anda harus mendokumentasikan beberapa keputusan penting bersama dengan
motivasi dan penalarannya

### Usulan kami mengenai keputusan

Simpan kumpulan keputusan yang signifikan secara arsitektur, yaitu keputusan yang
memengaruhi struktur, karakteristik kualitas, dependensi dan antarmuka penting (terutama eksternal),
atau teknik konstruksi (terima kasih kepada Michael
Nygard atas usulan ini).

## 10. Persyaratan Kualitas

Persyaratan kualitas sebagai skenario, dengan pohon kualitas untuk memberikan gambaran
umum tingkat tinggi. Tujuan kualitas terpenting seharusnya sudah dijelaskan di bagian
1.2. (tujuan kualitas).

### Isi

Bagian ini berisi semua persyaratan kualitas yang relevan.

Yang terpenting dari persyaratan ini sudah dijelaskan di bagian
1.2. (tujuan kualitas), sehingga di sini hanya perlu dirujuk. Di bagian
10 ini Anda juga sebaiknya menangkap persyaratan kualitas yang kurang penting,
yang tidak akan menimbulkan risiko tinggi jika tidak sepenuhnya tercapai (tetapi mungkin
akan menyenangkan jika ada).

### Motivasi

Karena persyaratan kualitas akan sangat memengaruhi keputusan
arsitektur, Anda harus mengetahui kualitas apa yang benar-benar penting bagi
para pemangku kepentingan Anda, dengan cara yang spesifik dan terukur.

### Informasi Lebih Lanjut

Lihat model kualitas Q42 yang lengkap di https://quality.arc42.org.

## 10.1 Gambaran Umum Persyaratan Kualitas

### Isi

Gambaran umum atau ringkasan persyaratan kualitas.

### Motivasi

Sering kali kita menemui puluhan (bahkan ratusan) persyaratan kualitas yang rinci.
Di bagian gambaran umum ini Anda sebaiknya mencoba meringkas, misalnya dengan menjelaskan
kategori atau topik (seperti yang disarankan oleh ISO 25010:2023 atau Q42

Jika deskripsi ringkasan ini sudah tepat, cukup spesifik, dan
terukur, Anda dapat melewati bagian 10.2.

### Bentuk

Gunakan tabel sederhana di mana setiap baris berisi kategori atau topik dan deskripsi
singkat persyaratan kualitas. Atau, Anda dapat menggunakan peta pikiran untuk
menyusun persyaratan kualitas ini.

Dalam literatur, gagasan pohon atribut kualitas juga telah dijelaskan,
yang menempatkan istilah umum “kualitas” sebagai akar dan menggunakan penghalusan istilah
“kualitas” berbentuk pohon. [Bass+21] memperkenalkan istilah “Quality
Attribute Utility Tree” untuk tujuan ini.

## 10.2 Skenario Kualitas

### Isi

Skenario kualitas membuat persyaratan kualitas menjadi konkret dan memungkinkan untuk memutuskan apakah
persyaratan tersebut terpenuhi (dalam arti kriteria penerimaan). Pastikan skenario
Anda spesifik dan terukur.

Dua jenis skenario sangat berguna:

- Skenario penggunaan (disebut juga skenario aplikasi atau skenario kasus penggunaan)
  menjelaskan reaksi sistem pada waktu proses terhadap stimulus tertentu. Ini juga
  mencakup skenario yang menjelaskan efisiensi atau kinerja sistem.
  Contoh: Sistem bereaksi terhadap permintaan pengguna dalam waktu satu detik.

- Skenario perubahan menjelaskan efek yang diinginkan dari modifikasi atau perluasan
  sistem atau lingkungan terdekatnya. Contoh: Fungsionalitas tambahan
  diimplementasikan atau persyaratan atribut kualitas berubah, dan upaya atau
  durasi perubahan tersebut diukur.

### Bentuk

Informasi umum untuk skenario terperinci mencakup hal-hal berikut:

Dalam bentuk singkat (disukai dalam model Q42):

- Konteks/Latar Belakang: Sistem atau komponen macam apa, apa lingkungan atau situasinya?

- Sumber/Stimulus: Siapa atau apa yang memulai atau memicu suatu perilaku, reaksi, atau tindakan.

- Metrik/Kriteria Penerimaan: Respons yang mencakup ukuran atau metrik

Bentuk panjang skenario (disukai oleh SEI dan [Bass+21]) lebih rinci dan mencakup informasi berikut:

- ID Skenario: Pengenal unik untuk skenario.

- Nama Skenario: Nama singkat yang deskriptif untuk skenario.

- Sumber: Entitas (pengguna, sistem, atau peristiwa) yang memulai skenario.

- Stimulus: Peristiwa atau kondisi pemicu yang harus ditangani sistem.

- Lingkungan: Konteks operasional atau kondisi di mana sistem mengalami stimulus.

- Artefak: Blok bangunan atau elemen lain dari sistem yang terdampak oleh stimulus.

- Respons: Hasil atau perilaku yang ditunjukkan sistem sebagai reaksi terhadap stimulus.

- Ukuran Respons: Kriteria atau metrik untuk mengevaluasi respons sistem.

### Lihat juga

Sejak Januari 2023, arc42 menyediakan model kualitas pragmatis, yang mengusulkan untuk
melabeli persyaratan kualitas dengan tagar atau label seperti #flexible, #efficient,
#usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Risiko dan Utang Teknis

Risiko teknis atau utang teknis yang diketahui. Masalah potensial apa yang ada di dalam atau
di sekitar sistem? Apa yang membuat tim pengembangan merasa sengsara?

### Isi

Daftar risiko teknis atau utang teknis yang teridentifikasi, diurutkan berdasarkan prioritas

### Motivasi

“Manajemen risiko adalah manajemen proyek untuk orang dewasa” (Tim Lister, Atlantic
Systems Guild.)

Ini harus menjadi motto Anda untuk deteksi dan evaluasi sistematis risiko dan
utang teknis dalam arsitektur, yang akan dibutuhkan oleh pemangku kepentingan manajemen (misalnya manajer proyek, pemilik produk) sebagai bagian dari analisis
risiko keseluruhan dan perencanaan pengukuran.

### Bentuk

Daftar risiko dan/atau utang teknis, mungkin termasuk tindakan yang disarankan untuk
meminimalkan, memitigasi, atau menghindari risiko atau mengurangi utang teknis.

