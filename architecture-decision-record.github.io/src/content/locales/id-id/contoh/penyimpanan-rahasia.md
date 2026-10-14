# Penyimpanan rahasia

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
  * [Vault by HashiCorp](#vault-by-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant by Lyft](#confidant-by-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server by Thycotic](#secret-server-by-thycotic)


## Ringkasan


### Isu

Kami perlu menyimpan rahasia, seperti kata sandi, kunci privat, token autentikasi, dll.

Sebagian rahasia berorientasi pengguna. Misalnya, pengembang kami ingin dapat menggunakan ponselnya untuk mencari kata sandi suatu layanan.

Sebagian rahasia berorientasi sistem. Misalnya, pipeline continuous delivery kami perlu dapat mencari kredensial untuk hosting cloud kami.


### Keputusan

Bitwarden untuk rahasia berorientasi pengguna

Vault by HashiCorp untuk rahasia berorientasi sistem.


### Status

Diputuskan. Kami terbuka terhadap alternatif baru seiring kemunculannya.


## Rincian


### Asumsi

Untuk tujuan ini, dan dalam kondisi kami saat ini, kami menghargai kenyamanan berorientasi pengguna, seperti aplikasi seluler yang dapat digunakan.

  * Kami ingin memastikan akses cepat dan mudah saat bepergian, seperti untuk pengembang yang melakukan rekayasa keandalan sistem saat bertugas siaga (on-call).

  * Kami ingin dapat berbagi sebagian rahasia di antara orang-orang tertentu, seperti sebuah tim.

Kami tidak mencoba menyelesaikan untuk satu penyedia saja, seperti menyimpan semua rahasia secara eksklusif di Amazon atau Azure atau Google.

Kami tidak menginginkan pendekatan ad-hoc seperti "ingat saja" atau "tulis di catatan" atau "cari sendiri cara menyimpannya".

Model keamanan kami untuk tujuan ini tidak masalah dengan menggunakan vendor COTS yang sangat dihormati, seperti alat manajemen kata sandi SaaS.


### Batasan

Saat ini kami menginginkan sesuatu yang mudah, yaitu tidak perlu menulis kode, tidak perlu memasang server, tidak perlu membuat komitmen besar, tidak perlu menstandarkan semua orang.


### Posisi

Kami mempertimbangkan:

1. Pengelola kata sandi siap pakai yang berorientasi pengguna: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG, dll.

2. Pengelola kata sandi COTS yang berorientasi sistem: AWS KMS, Vault by HashiCorp, EnvKey, Secret Server by Thycotic, Devolutions Password Server, Confidant by Lyft.

3. Pendekatan berorientasi berbagi: menggunakan dokumen Google bersama, atau saluran Slack bersama, atau folder jaringan bersama, dll.

4. Pendekatan ad-hoc berteknologi rendah, seperti mengingat, menulis catatan, atau mengandalkan setiap pengguna untuk menemukan caranya sendiri.


### Argumen

Bitwarden, LastPass, 1Password, dan Dashlane semuanya adalah produk komersial siap pakai.

  * Jenis fitur yang serupa untuk pengguna, tim, organisasi, dll.

  * Kemampuan desktop untuk Windows dan Mac, dan kemampuan seluler untuk Android dan iOS.

  * Ekstensi browser untuk Chrome dan Firefox, untuk pengisian formulir otomatis, dll.

Bitwarden memiliki dua keunggulan dibandingkan yang lain:

  * Bitwarden bersumber terbuka, yang berarti keamanannya dapat ditinjau oleh rekan sejawat dan juga perusahaannya sangat dihargai oleh pengembang yang berorientasi keamanan.

  * Anekdot dari para pekerja perangkat lunak menggambarkan preferensi yang signifikan terhadap Bitwarden dibandingkan yang lain.

Contoh tulisan bagus yang umum: https://jcs.org/2017/11/17/bitwarden

Contoh situs pemungutan suara berdampingan yang umum: https://stackshare.io/stackups/bitwarden-vs-dashlane

Kami menunda KeyPass, pass, GPG, dll. karena ada kompleksitas tambahan. Semuanya tampak seperti solusi yang baik untuk pengguna teknis. GPG tampak sangat baik untuk pengguna teknis yang menginginkan kemampuan berorientasi perintah lintas sistem.

Kami menunda KMS karena memiliki keterikatan pada satu penyedia (vendor lock-in).

Kami memilih Vault untuk kebutuhan berorientasi sistem, karena ulasannya sangat positif, dan karena HashiCorp memiliki rekam jejak yang sangat baik untuk perangkat lunak dan dukungan berkualitas tinggi.

Kami memveto pendekatan berbagi seperti melalui dokumen bersama, saluran bersama, folder jaringan bersama, dll. Pendekatan ini tidak menyediakan kualitas keamanan yang kami inginkan.

Kami memveto pendekatan ad-hoc berteknologi rendah, karena kami semua sepakat ini bukan jalan ke depan jangka panjang.


### Implikasi

Pengembang mungkin perlu melacak rahasia di dua tempat: Bitwarden untuk akses berorientasi pengguna, dan Vault untuk akses berorientasi sistem.


## Terkait


### Keputusan terkait

Keputusan tentang server CI/CD mana yang dipilih harus menyertakan bukti kemampuan untuk mengakses rahasia.

Kami perlu memutuskan bagaimana mengelola rahasia, dalam hal kebijakan, rotasi, organisasi, dll.


### Persyaratan terkait

Rahasia akan memiliki persyaratan terkait untuk kepatuhan, audit, dan orientasi/offboarding SDM.


### Artefak terkait

Kami memperkirakan kami mungkin mengekspor beberapa rahasia ke variabel lingkungan.


### Prinsip terkait

Mudah dibatalkan.

Mudah dijalankan secara paralel, yaitu mudah menggunakan berbagai pengelola kata sandi.

Murah untuk dicoba, yaitu ada uji coba gratis dan tanpa komitmen.


## Catatan

Catatan evaluasi di sini. Semua catatan adalah komentar publik di berbagai papan diskusi devops.


### Vault by HashiCorp

Vault persis seperti yang Anda inginkan di sini. 

Namun jangan langsung menaruh Vault ke produksi, siapkan dulu di lingkungan pengujian, karena dokumentasi HashiCorp bisa sangat kurang meskipun produk mereka luar biasa.

Kurva belajarnya sangat curam dan penyiapannya tidak sepele. 

Penyiapan awal agak menyakitkan. Namun sangat sepadan, dan komunitas akan mendukungnya cukup baik agar Anda bisa bertahan.

Dokumentasi mengerikan tetapi ada banyak panduan daring dari orang-orang yang menyiapkannya dan jika Anda menggabungkan beberapa di antaranya Anda akan memiliki penyiapan yang berfungsi.

Penyiapan awal memerlukan utak-atik helm chart mereka (vault dan consul). Meskipun secara teknis Anda dapat menggunakan banyak back-end lain, saya benar-benar tidak menyarankannya. Back-end/consul bisa sangat kecil jika Anda tidak memiliki banyak data untuk disimpan.

Pastikan Anda terbiasa/familier menggunakan CLI, karena GUI lebih seperti portal bukti konsep/iklan untuk edisi enterprise mereka.

Fakta bahwa Anda tidak bisa begitu saja "mengisinya" itu menyakitkan. Misalnya jika Anda memiliki 5 bidang, Anda harus menambahkan setiap bidang secara manual untuk setiap item. Jadi bukan seperti Anda menentukan bidang di awal untuk kategori tertentu, dan mengisi bidang tersebut untuk semua item dalam kategori itu, lebih seperti "Anda membuat segalanya setiap kali", yang (menurut saya) sangat menyebalkan.

Anda mungkin juga ingin melihat goldfish sebagai UI di atas vault. Ini membuatnya cukup menyenangkan untuk membuat tim Anda mau menggunakannya. Mereka juga memiliki demo. 1. Siapkan consul. 2. Siapkan vault yang mengarah ke consul. 3. Siapkan goldfish yang mengarah ke vault. 3. Siapkan cron job untuk menjalankan consul snapshot sebagai cadangan.



### LastPass

LastPass Teams. Kami menggunakannya, memiliki templat kustom, ACL, tidak ada yang kurang menurut saya.

Saya menerapkan LastPass di organisasi saya dan memberinya nilai C+/B-. Masalah terbesar akhir-akhir ini adalah kurangnya keandalan. Dalam 90 hari terakhir ada beberapa jam di mana vault dipaksa masuk ke mode offline. Ini tidak ideal bagi organisasi saya karena kami secara harfiah menyimpan 4.000+ kata sandi di 20+ folder bersama. Seperti yang dapat Anda bayangkan dengan kata sandi sebanyak itu setidaknya beberapa diperbarui atau ditambahkan setiap hari. Kami memiliki rencana DR jika masalah berlangsung lebih dari satu atau dua jam: sebuah skrip menandatangani dan mengenkripsi dump CSV vault setiap malam yang dapat diimpor ke keepass.

LastPass pernah mengalami penurunan layanan sesaat yang tidak dilaporkan: login 'berhasil' tetapi tidak menarik situs, fitur acak rusak di panel admin, dan tidak membagikan kunci dengan benar untuk folder bersama tingkat atas yang baru. Saya memiliki pengguna 'key push'/cadangan khusus yang ada di setiap grup. Biasanya masuk sebagai pengguna itu akan memperbaiki masalah berbagi kunci apa pun tetapi tidak ketika layanan sedang menurun meskipun halaman status mengatakan apa pun...

Untuk integrasi, bisa mudah jika Anda memiliki ACL yang tepat dengan model hak istimewa paling sedikit, misalnya jika pengguna memiliki baca & tulis dan hanya baca pada suatu entri atau folder, mereka hanya mendapatkan izin hanya baca. Sayangnya ACL organisasi saya tidak yang terbaik, jadi saya akhirnya menggunakan API provisioning JSON dan ~500 baris python karena sifat ketergantungan ratusan ACL kami tidak terpetakan dengan baik ke model hak istimewa paling sedikit. Akhirnya saya mengambil semua ACL tempat seorang pengguna berada dan melakukan semacam penelusuran dependensi.

Jika struktur ACL atau grup Anda sudah dibangun dengan struktur hak istimewa paling sedikit dalam pikiran, alat sinkronisasi AD/LDAP untuk Windows akan bekerja dengan baik.

Hubungi tim penjualan mereka dan mereka dapat memberi Anda uji coba Enterprise yang lebih lama. Pastikan Anda memahami sepenuhnya keterbatasannya sebelum mengambil keputusan. Kami mengalami cukup banyak rasa sakit pertumbuhan tetapi selain gangguan atau penurunan di sisi server, semuanya sangat mulus.


### Bitwarden

Bitwarden memiliki perangkat yang bagus di sekitarnya (WebUI, CLI, Seluler, Desktop). Dapat di-hosting sendiri dan cukup mudah disiapkan. Dokumentasi cukup baik dan merupakan alat yang direkomendasikan oleh PrivacyTools.


### EnvKey

https://www.envkey.com/ adalah saas. Sangat mudah diimplementasikan, diintegrasikan, dan dikelola.

Fitur:

  * Melindungi kunci API dan kredensial.

  * Menjaga konfigurasi tetap sinkron di mana-mana.

  * Manajemen konfigurasi dan rahasia yang cerdas dan terenkripsi end-to-end. 

  * Mencegah berbagi yang tidak aman dan penyebaran konfigurasi yang tak terkendali. 

  * Integrasi dalam hitungan menit.

Kemampuan:

  * Kelola konfigurasi dan tingkat akses untuk semua aplikasi, lingkungan, dan tim Anda di satu tempat.

  * Konfigurasikan lingkungan pengembangan atau server apa pun hanya dengan satu variabel lingkungan.

Kelebihan:

  * Beranda yang bagus.

  * Proposisi nilai yang jelas.

  * Aplikasi web yang sangat baik secara visual.

  * Data contoh yang unggul, misalnya Algolia, AWS, Datadog, GitHub, Stripe, dll.

  * Berbicara dengan pendiri selama 30 menit tentang perusahaan, UI, dll. Dane terdengar berwawasan, jujur tentang kelebihan/kekurangan, dan mitra yang layak.

  * Perusahaan ini pada dasarnya adalah perusahaan Y Combinator yang umum, dengan 1 pendiri. Mengumpulkan $120K pada 2018-01.

  * Fokusnya adalah mencapai fitur enterprise, terutama beralih dari hosting cloud EnvKey ke on-prem atau BYOC.

  * Jalur ke depan yang potensial dimulai dengan EnvKey demi kemudahan penggunaan, lalu kemudian (atau secara paralel) menambahkan Vault. 


### Confidant by Lyft

https://lyft.github.io/confidant/

Confidant adalah layanan manajemen rahasia sumber terbuka yang menyediakan penyimpanan dan akses rahasia yang ramah pengguna dengan cara yang aman, dari para pengembang di Lyft.

Autentikasi KMS: Confidant memecahkan masalah "ayam dan telur" autentikasi dengan menggunakan AWS KMS dan IAM agar peran IAM dapat menghasilkan token autentikasi aman yang dapat diverifikasi oleh Confidant. Confidant juga mengelola grant KMS untuk peran IAM Anda, yang memungkinkan peran IAM menghasilkan token yang dapat digunakan untuk autentikasi layanan ke layanan, atau untuk meneruskan pesan terenkripsi antarlayanan.

Enkripsi saat diam (at-rest) untuk rahasia berversi: Confidant menyimpan rahasia dengan cara hanya-tambah di DynamoDB, menghasilkan kunci data KMS yang unik untuk setiap revisi dari setiap rahasia, menggunakan kriptografi terautentikasi simetris Fernet.

Antarmuka web yang ramah pengguna untuk mengelola rahasia: Confidant menyediakan antarmuka web AngularJS yang memungkinkan pengguna akhir dengan mudah mengelola rahasia, pemetaan rahasia ke layanan, dan riwayat perubahan.


### Devolutions Password Server

https://server.devolutions.net/

Amankan, kelola, dan pantau akses ke akun dan sesi istimewa.

Brankas kata sandi yang komprehensif dan sangat aman yang memungkinkan Anda mengendalikan akses ke akun istimewa Anda, sekaligus meningkatkan visibilitas jaringan secara keseluruhan bagi sysadmin dan menyediakan pengalaman yang mulus bagi pengguna akhir.

Fitur: brankas kata sandi organisasi terpusat, brankas pribadi khusus pengguna, pengelola kata sandi, injeksi kredensial,
integrasi Active Directory, kontrol akses berbasis peran, autentikasi dua faktor, siap untuk enterprise, pembatasan IP, kemampuan manajemen, pembuat kata sandi otomatis, akses aplikasi seluler, riwayat kata sandi, laporan akses, peringatan email.

  * mendukung enkripsi data

  * mendukung beberapa skema Autentikasi termasuk LDAP, O365, dan pengguna Lokal DENGAN dukungan MFA dari beberapa sumber

  * beberapa repositori/brankas dengan kontrol akses terperinci untuk beberapa tim

  * Web UI modern

  * brankas kredensial dan koneksi pribadi untuk kredensial/koneksi pribadi

  * aplikasi seluler untuk IOS/Android

  * log audit untuk setiap entri, siapa/apa/kapan dengan permintaan opsional mengapa mereka mengaksesnya

  * templat yang dapat dikustomisasi (meskipun mereka mendukung ratusan jenis koneksi secara native)

  * masih banyak fitur lainnya dan klien tebal Windows/Mac (Remote Desktop Manager) yang dapat Anda sinkronkan dan yang sangat memperluas opsi...koneksi satu klik

  * harganya tidak terlalu buruk - hingga 15 pengguna adalah $500 per tahun untuk password server


### Secret Server by Thycotic

https://thycotic.com/products/secret-server/

Fitur versi on-premise: 

  * Kendali total atas sistem dan infrastruktur keamanan end-to-end Anda

  * Deploy perangkat lunak di dalam pusat data on-premise Anda atau instans virtual private cloud Anda sendiri

  * Memenuhi kewajiban hukum dan regulasi yang mewajibkan semua data dan sistem berada di on-premise

Fitur versi cloud:

  * Model perangkat lunak sebagai layanan memungkinkan Anda mendaftar dan segera memulai

  * Skalabilitas elastis seiring pertumbuhan Anda

  * Kontrol dan redundansi yang disediakan oleh Azure dengan SLA uptime 99,9%

Umpan balik pengguna:

  * Kami dulu menggunakan produk itu. Sangat mudah dilewati dan aturannya hanya berfungsi untuk orang pintar. Pengguna yang malas atau bodoh dapat dengan mudah merusaknya di area tim. Harga dapat dinegosiasikan ketika Anda berbicara dengan mereka.

  * Anda dapat menjalankannya menggunakan SQL express dan mesin Win 7. 

  * Murah.
