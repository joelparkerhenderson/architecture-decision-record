# Catatan keputusan arsitektur (ADR)

Catatan keputusan arsitektur (ADR) adalah dokumen yang merekam keputusan arsitektur penting yang diambil beserta konteks dan konsekuensinya.

> [!IMPORTANT]
> Lakukan uji tuntas Anda sendiri terhadap sumber daya ini sebelum menggunakannya di sistem kritis apa pun.

Daftar isi:

- [Apa itu catatan keputusan arsitektur?](#apa-itu-catatan-keputusan-arsitektur)
- [Cara mulai menggunakan ADR](#cara-mulai-menggunakan-adr)
- [Cara mulai menggunakan ADR dengan alat](#cara-mulai-menggunakan-adr-dengan-alat)
- [Cara mulai menggunakan ADR dengan git](#cara-mulai-menggunakan-adr-dengan-git)
- [Skill Claude Code untuk ADR](#skill-claude-code-untuk-adr)
- [Konvensi nama file](#konvensi-nama-file)
- [Saran menulis ADR yang baik](#saran-menulis-adr-yang-baik)
- [Templat contoh ADR](#templat-contoh-adr)
- [Saran kerja sama tim untuk ADR](#saran-kerja-sama-tim-untuk-adr)
- [Pertanyaan kerja sama tim untuk ADR](#pertanyaan-kerja-sama-tim-untuk-adr)
- [Konsep langkah berikutnya untuk ADR](#konsep-langkah-berikutnya-untuk-adr)
- [Diagram, tampilan, dan sudut pandang arsitektur](#diagram-tampilan-dan-sudut-pandang-arsitektur)
- [Fitness function untuk keputusan sebagai kode](#fitness-function-untuk-keputusan-sebagai-kode)
- [Pagar pengaman keputusan untuk pull request](#pagar-pengaman-keputusan-untuk-pull-request)
- [Untuk informasi lebih lanjut](#untuk-informasi-lebih-lanjut)

Templat:

- [Templat catatan keputusan oleh Jeff Tyree dan Art Akerman](templat/templat-catatan-keputusan-oleh-jeff-tyree-dan-art-akerman/)
- [Templat catatan keputusan oleh Michael Nygard](templat/templat-catatan-keputusan-oleh-michael-nygard/)
- [Templat catatan keputusan oleh EdgeX](templat/templat-catatan-keputusan-oleh-edgex/)
- [Templat catatan keputusan oleh arc42](templat/templat-catatan-keputusan-oleh-arc42/)
- [Templat catatan keputusan untuk pola Alexandrian](templat/templat-catatan-keputusan-untuk-pola-alexandrian/)
- [Templat catatan keputusan untuk kasus bisnis](templat/templat-catatan-keputusan-untuk-kasus-bisnis/)
- [Templat catatan keputusan proyek MADR](templat/templat-catatan-keputusan-proyek-madr/)
- [Templat catatan keputusan menggunakan Planguage](templat/templat-catatan-keputusan-menggunakan-planguage/)
- [Templat catatan keputusan oleh Paulo Merson](https://github.com/pmerson/ADR-template)
- [Templat catatan keputusan oleh Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Templat catatan keputusan oleh Gareth Morgan](templat/templat-catatan-keputusan-oleh-gareth-morgan/)
- [Templat catatan keputusan oleh GIG Cymru NHS Wales](templat/templat-catatan-keputusan-oleh-gig-cymru-nhs-wales/)
- [Templat catatan keputusan untuk Keputusan Teknis Penting (ITD) oleh Ignacio Larrañaga](templat/templat-catatan-keputusan-untuk-keputusan-teknis-penting/)

Contoh:

- [Kerangka CSS](contoh/kerangka-css/)
- [Konfigurasi variabel lingkungan](contoh/konfigurasi-variabel-lingkungan/)
- [Metrik, monitor, peringatan](contoh/metrik-monitor-peringatan/)
- [Microsoft Azure DevOps](contoh/microsoft-azure-devops/)
- [Monorepo vs multirepo](contoh/monorepo-vs-multirepo/)
- [Bahasa pemrograman](contoh/bahasa-pemrograman/)
- [Penyimpanan rahasia](contoh/penyimpanan-rahasia/)
- [Format stempel waktu](contoh/format-stempel-waktu/)
- [Masih banyak lagi...](contoh/)

## Apa itu catatan keputusan arsitektur?

**Catatan keputusan arsitektur** (architecture decision record, ADR) adalah dokumen yang menangkap sebuah keputusan arsitektur penting yang dibuat beserta konteks dan konsekuensinya.

**Keputusan arsitektur** (architecture decision, AD) adalah pilihan desain perangkat lunak yang menjawab persyaratan yang signifikan.

**Log keputusan arsitektur** (architecture decision log, ADL) adalah kumpulan semua ADR yang dibuat dan dipelihara untuk proyek (atau organisasi) tertentu.

**Persyaratan yang signifikan secara arsitektur** (architecturally-significant requirement, ASR) adalah persyaratan yang memiliki efek terukur pada arsitektur sistem perangkat lunak.

Semua ini berada dalam topik **manajemen pengetahuan arsitektur** (architecture knowledge management, AKM).

Tujuan dokumen ini adalah memberikan gambaran umum yang cepat tentang ADR, cara membuatnya, dan di mana mencari informasi lebih lanjut.

Singkatan:

  * **AD**: keputusan arsitektur

  * **ADL**: log keputusan arsitektur

  * **ADR**: catatan keputusan arsitektur

  * **AKM**: manajemen pengetahuan arsitektur

  * **ASR**: persyaratan yang signifikan secara arsitektur

## Cara mulai menggunakan ADR

Untuk mulai menggunakan ADR, bicarakan area-area berikut dengan rekan tim Anda.

Identifikasi keputusan:

  * Seberapa mendesak dan seberapa penting AD tersebut?

  * Apakah harus dibuat sekarang, atau dapat menunggu sampai lebih banyak hal diketahui?

  * Baik pengalaman pribadi maupun kolektif, serta metode dan praktik desain yang diakui, dapat membantu identifikasi keputusan.

  * Idealnya pertahankan daftar tugas keputusan yang melengkapi daftar tugas produk.

Pengambilan keputusan:

  * Ada sejumlah teknik pengambilan keputusan, baik yang umum maupun yang khusus untuk arsitektur perangkat lunak, misalnya dialogue mapping.

  * Pengambilan keputusan secara berkelompok adalah topik penelitian yang aktif.

Pemberlakuan dan penegakan keputusan:

  * AD digunakan dalam desain perangkat lunak; karena itu AD harus dikomunikasikan kepada, dan diterima oleh, para pemangku kepentingan sistem yang mendanai, mengembangkan, dan mengoperasikannya.

  * Gaya penulisan kode yang jelas secara arsitektur dan tinjauan kode yang berfokus pada isu dan keputusan arsitektur adalah dua praktik yang terkait.

  * AD juga harus (kembali) dipertimbangkan ketika memodernisasi sistem perangkat lunak dalam evolusi perangkat lunak.

Berbagi keputusan (opsional):

  * Banyak AD berulang di berbagai proyek.

  * Karena itu, pengalaman dengan keputusan masa lalu, baik yang baik maupun buruk, dapat menjadi aset yang berharga dan dapat digunakan kembali ketika menerapkan strategi manajemen pengetahuan yang eksplisit.

Dokumentasi keputusan:

  * Banyak templat dan alat untuk mencatat keputusan tersedia.

  * Lihat komunitas agile, misalnya ADR dari M. Nygard.

  * Lihat proses rekayasa perangkat lunak dan desain arsitektur tradisional, misalnya tata letak tabel yang disarankan oleh IBM UMF dan oleh Tyree dan Akerman dari CapitalOne.

Untuk informasi lebih lanjut:

  * Langkah-langkah di atas diadopsi dari entri Wikipedia tentang [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Cara mulai menggunakan ADR dengan alat

- [MySpec](https://myspec.dev) — Platform spesifikasi dan keputusan arsitektur otomatis yang menyusun konstitusi proyek, arsitektur teknis, dan ADR ke dalam Markdown yang bersih yang disajikan melalui MCP.

Anda dapat mulai menggunakan ADR dengan alat apa pun sesuai keinginan Anda.

Contohnya:

  * Jika Anda suka menggunakan Google Drive dan penyuntingan daring, Anda dapat membuat Google Doc atau Google Sheet.

  * Jika Anda suka menggunakan kontrol versi kode sumber, seperti git, Anda dapat membuat satu file untuk setiap ADR.

  * Jika Anda suka menggunakan alat perencanaan proyek, seperti Atlassian Jira, Anda dapat menggunakan pelacak perencanaan dari alat tersebut.

  * Jika Anda suka menggunakan wiki, seperti MediaWiki, Anda dapat membuat wiki ADR.

## Cara mulai menggunakan ADR dengan git

Jika Anda suka menggunakan kontrol versi git, berikut cara kami memulai penggunaan ADR dengan git untuk proyek perangkat lunak umum yang memiliki kode sumber.

Buat direktori untuk file ADR:

```sh
$ mkdir adr
```

Untuk setiap ADR, buat file teks, seperti `database.txt`:

```sh
$ vi database.txt
```

Tulis apa pun yang Anda inginkan di dalam ADR. Lihat templat di repositori ini untuk mendapatkan ide.

Commit ADR tersebut ke repositori git Anda.

## Skill Claude Code untuk ADR

Repositori ini menyertakan dua skill [Claude Code](https://claude.com/claude-code) di bawah [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), agar agen pengodean AI dapat menulis dan memelihara ADR sesuai anjuran proyek ini:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — serbaguna, untuk siapa pun yang menulis ADR di proyek mana pun. Membantu memutuskan apakah suatu keputusan memerlukan ADR, menyiapkan direktori `adr/` atau `decisions/`, menamai berkas, memilih templat dari sebelas kerangka yang disertakan, dan menulis bagian Konteks/Keputusan/Konsekuensi yang solid.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — khusus untuk pemelihara repositori ini. Mendokumentasikan tata letak repositori, konvensi pencerminan README/locales, dan langkah-langkah persis untuk menambahkan templat, contoh, atau tautan alat baru.

Untuk menggunakan sebuah skill, salin foldernya ke `.claude/skills/` di akar repositori yang sedang Anda kerjakan (atau ke `~/.claude/skills/` agar tersedia di setiap proyek), lalu minta Claude Code menulis atau meninjau ADR.

## Konvensi nama file

Jika Anda memilih membuat ADR menggunakan file teks biasa, Anda mungkin ingin menetapkan konvensi nama file ADR Anda sendiri.

Kami lebih suka menggunakan konvensi nama file yang memiliki format tertentu.

Contoh:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Konvensi nama file kami:

  * Nama berisi frasa kata kerja imperatif dalam bentuk kini. Hal ini membantu keterbacaan dan sesuai dengan format pesan commit kami.

  * Nama menggunakan huruf kecil dan tanda hubung (sama seperti repositori ini). Ini adalah keseimbangan antara keterbacaan dan kegunaan sistem.

  * Ekstensinya adalah markdown. Hal ini berguna untuk pemformatan yang mudah.

## Saran menulis ADR yang baik

Ciri-ciri ADR yang baik:

* Alasan: Jelaskan alasan melakukan AD tertentu tersebut. Ini dapat mencakup konteks (lihat di bawah), kelebihan dan kekurangan berbagai pilihan yang mungkin, perbandingan fitur, pembahasan biaya/manfaat, dan lainnya.

* Spesifik: Setiap ADR sebaiknya membahas satu AD, bukan beberapa AD.

* Stempel waktu: Tandai kapan setiap butir dalam ADR ditulis. Ini sangat penting untuk aspek yang dapat berubah dari waktu ke waktu, seperti biaya, jadwal, penskalaan, dan sejenisnya.

* Tidak dapat diubah: Jangan mengubah informasi yang ada dalam ADR. Sebagai gantinya, ubah ADR dengan menambahkan informasi baru, atau gantikan ADR dengan membuat ADR baru.

Ciri-ciri bagian "Konteks" yang baik dalam ADR:

* Jelaskan situasi organisasi Anda dan prioritas bisnisnya.

* Sertakan alasan dan pertimbangan berdasarkan komposisi sosial dan keterampilan tim Anda.

* Sertakan kelebihan dan kekurangan yang relevan, dan jelaskan dengan istilah yang selaras dengan kebutuhan dan tujuan Anda.

Ciri-ciri bagian "Konsekuensi" yang baik dalam ADR:

* Jelaskan apa yang terjadi setelah keputusan dibuat. Ini dapat mencakup dampak, hasil, keluaran, tindak lanjut, dan lainnya.

* Sertakan informasi tentang ADR berikutnya. Cukup umum bahwa satu ADR memicu kebutuhan akan ADR lain, misalnya ketika satu ADR membuat pilihan besar yang menyeluruh, yang pada gilirannya menimbulkan kebutuhan akan keputusan-keputusan yang lebih kecil.

* Sertakan proses tinjauan pascatindakan apa pun. Biasanya tim meninjau setiap ADR satu bulan kemudian, untuk membandingkan informasi ADR dengan apa yang terjadi dalam praktik sebenarnya, agar dapat belajar dan berkembang.

ADR baru dapat menggantikan ADR sebelumnya:

* Ketika sebuah AD dibuat yang menggantikan atau membatalkan ADR sebelumnya, maka ADR baru harus dibuat

## Templat contoh ADR

Templat contoh ADR yang kami kumpulkan dari internet:

- [Templat ADR oleh Michael Nygard](templat/templat-catatan-keputusan-oleh-michael-nygard/) (sederhana dan populer)

- [Templat ADR oleh Jeff Tyree dan Art Akerman](templat/templat-catatan-keputusan-oleh-jeff-tyree-dan-art-akerman/) (lebih canggih)

- [Templat ADR untuk pola Alexandrian](templat/templat-catatan-keputusan-untuk-pola-alexandrian/) (sederhana dengan rincian konteks)

- [Templat ADR untuk studi kelayakan bisnis](templat/templat-catatan-keputusan-untuk-kasus-bisnis/) (lebih berorientasi MBA, dengan biaya, SWOT, dan lebih banyak opini)

- [Templat ADR proyek Markdown Any Decision Records (MADR)](templat/templat-catatan-keputusan-proyek-madr/) (versi sederhana dan versi lengkap; yang terakhir menekankan opsi beserta kelebihan dan kekurangannya)

- [Templat ADR yang menggunakan Planguage](templat/templat-catatan-keputusan-menggunakan-planguage/) (lebih berorientasi penjaminan mutu)

- [Templat untuk Keputusan Teknis Penting (ITD) oleh Ignacio Larrañaga](templat/templat-catatan-keputusan-untuk-keputusan-teknis-penting/) (ramping dan mengutamakan keputusan, dioptimalkan untuk tinjauan eksekutif yang cepat)

## Saran kerja sama tim untuk ADR

Jika Anda mempertimbangkan untuk menggunakan catatan keputusan bersama tim Anda, berikut beberapa saran yang kami pelajari dari bekerja dengan banyak tim.

Anda memiliki kesempatan untuk memimpin rekan tim Anda dengan membicarakan "mengapa" bersama-sama, alih-alih mewajibkan "apa". Misalnya, catatan keputusan adalah cara bagi tim untuk berpikir lebih cerdas dan berkomunikasi lebih baik; catatan keputusan tidak bernilai jika hanya menjadi kewajiban administrasi yang dipaksakan setelah kejadian.

Beberapa tim jauh lebih menyukai nama "keputusan" (decisions) daripada singkatan "ADR". Ketika beberapa tim menggunakan nama direktori "decisions", seolah-olah sebuah lampu menyala, dan tim mulai memasukkan lebih banyak informasi ke dalam direktori tersebut, seperti keputusan vendor, keputusan perencanaan, keputusan penjadwalan, dan sebagainya. Semua jenis informasi ini dapat menggunakan templat yang sama. Kami berhipotesis bahwa orang belajar lebih cepat dengan kata ("keputusan") daripada singkatan ("ADR"), dan orang lebih termotivasi untuk menulis dokumen yang sedang dikerjakan ketika kata "catatan" dihilangkan, dan juga sebagian pengembang dan sebagian manajer tidak menyukai kata "arsitektur".

Secara teori, sifat tidak dapat diubah adalah yang ideal. Dalam praktik, sifat dapat diubah bekerja lebih baik untuk tim kami. Kami menyisipkan informasi baru ke dalam ADR yang ada, dengan stempel tanggal, dan catatan bahwa informasi tersebut datang setelah keputusan. Pendekatan semacam ini menghasilkan "dokumen hidup" yang dapat kami perbarui bersama. Pembaruan yang umum terjadi ketika kami memperoleh informasi berkat rekan tim baru, atau penawaran baru, atau hasil nyata dari penggunaan kami, atau perubahan pihak ketiga setelah kejadian seperti kemampuan vendor, paket harga, perjanjian lisensi, dan sebagainya.

## Pertanyaan kerja sama tim untuk ADR

### Siapa yang dapat membuat ADR?

Pertimbangkan area seperti orang tertentu, atau peran tertentu, atau tim tertentu, atau departemen tertentu; pertimbangkan juga apakah ada orang, peran, tim, atau departemen yang dapat memesan sebuah ADR, artinya mereka meminta satu ADR yang akan ditulis oleh orang lain. 

Contoh jawaban: Siapa pun di organisasi kami yang telah membaca halaman README catatan keputusan arsitektur dapat mengusulkan ADR, artinya orang tersebut dapat mulai menulisnya, dan membagikannya kepada tim.

### Apa yang membenarkan pembuatan ADR?

Pertimbangkan area seperti cara kerja tim organisasi Anda, struktur sistem perangkat lunak Anda, koordinasi lintas tim, kemudahan pemeliharaan jangka panjang, antarmuka eksternal, siapa yang ingin Anda beri manfaat, dan sejenisnya. 

Contoh jawaban: Kami ingin membuat ADR ketika kami ingin pengembang di masa depan memahami "mengapa" dari apa yang kami lakukan.

### Apa yang membenarkan tidak membuat ADR?

Pertimbangkan area seperti keputusan yang bukan tentang arsitektur, atau yang sangat kecil seperti berisiko minimal atau mandiri atau untuk satu pengembang, atau yang sudah sepenuhnya tercakup di tempat lain seperti oleh standar atau kebijakan atau dokumentasi, atau yang bersifat sementara seperti solusi sementara atau bukti konsep atau eksperimen. 

Contoh jawaban: Kami ingin melewatkan ADR ketika sebuah keputusan terbatas dalam lingkup dan waktu dan risiko dan biaya, atau sudah tercakup di tempat lain.

### Apa siklus hidup sebuah ADR?

Pertimbangkan area seperti proses pembuatan, proses riset, proses pengambilan keputusan, proses implementasi, dan proses penghentian. Pertimbangkan bagaimana melacak siklus hidup ADR dari waktu ke waktu, seperti bagaimana memindahkan ADR dari satu status ke status berikutnya, dan juga bagaimana mengomunikasikannya kepada para pemangku kepentingan. 

Contoh jawaban: Kami ingin ADR memiliki lima tahap siklus hidup: Memulai (Initiating) → Meneliti (Researching) → Mengevaluasi (Evaluating) → Mengimplementasikan (Implementing) → Memelihara (Maintaining) → Menghentikan (Sunsetting).

### Apa kriteria untuk langkah-langkah siklus hidup sebuah ADR?

Pertimbangkan area seperti kriteria penerimaan untuk sebuah ADR, artinya bagaimana Anda tahu ADR sudah cukup baik untuk maju dari satu langkah siklus hidup ke langkah berikutnya? Apakah masalahnya telah diartikulasikan dengan jelas? Apakah alternatif telah dipertimbangkan? Apakah trade-off sudah cukup dipahami dan didokumentasikan?
Apakah semua konteks yang relevan sudah tersedia? Apakah semua pemangku kepentingan yang relevan terlibat? Apakah semua umpan balik sudah dimasukkan? 

Contoh jawaban: Kami ingin ADR dipilih melalui pemungutan suara oleh para pemangku kepentingan ketika tim aktif telah 1) menyelesaikan riset mereka, 2) menyelesaikan evaluasi mereka, 3) mempublikasikan usulan ADR kepada para pemangku kepentingan dengan permintaan komentar dan batas waktu satu minggu, 4) semua komentar pemangku kepentingan telah dimasukkan dan ditanggapi.

### Peran dan tanggung jawab apa yang berinteraksi dengan sebuah ADR?

Pertimbangkan peran seperti pengusul, peneliti, evaluator, peninjau, penyetuju, pemelihara, dan sejenisnya. Pertimbangkan tanggung jawab seperti komunikasi dengan pemangku kepentingan, memastikan ekspektasi terpenuhi, berbagi di situs web atau intranet, dan meninjau pekerjaan secara berkala dan terutama ketika terjadi perubahan yang relevan.

Contoh jawaban: Kami ingin setiap ADR selalu memiliki satu orang kontak utama, satu orang kontak sekunder, dan satu tim yang akuntabel; mereka bertanggung jawab atas komunikasi, publikasi, pemeliharaan, tinjauan berkala minimal setahun sekali, dan penghentian akhir jika diperlukan.

### Bagaimana tata kelola berinteraksi dengan sebuah ADR?

Pertimbangkan area seperti cara kerja organisasi Anda, kebutuhan kepatuhan khusus seperti untuk aspek hukum atau aspek sumber daya manusia, bagaimana Anda ingin menangani konsensus versus konflik versus eskalasi. Apakah ada area atau orang atau tim yang dapat memiliki pengaruh lebih besar daripada yang lain terkait sebuah ADR, seperti dapat menyetujuinya, atau memberikan suara atasnya, atau memvetonya?

Contoh jawaban: Tata kelola sebuah ADR mengikuti urutan prioritas ini: CEO, CTO, CLO, tim yang mengimplementasikan ADR, para ahli di tim yang paling berpengetahuan tentang ADD. Tidak ada orang lain yang memiliki tata kelola kecuali dijelaskan dalam ADR. 

### Prinsip apa yang berinteraksi dengan sebuah ADR?

Pertimbangkan area seperti cara kerja organisasi Anda yang mencakup bergerak cepat versus bergerak lambat, untuk konsensus keputusan versus konflik keputusan, dan untuk preferensi risiko versus preferensi keselamatan, diskusi publik versus diskusi privat, dan sejenisnya.

Contoh jawaban: Kami menggunakan prinsip kepemimpinan bias for action, disagree-and-commit, estimasi 70% sudah cukup baik untuk keputusan yang mudah dibatalkan dan mudah diisolasi, dan cara kerja publik kecuali untuk informasi rahasia seperti dijelaskan dalam perjanjian kerahasiaan organisasi kami.

## Konsep langkah berikutnya untuk ADR

[Arc42](https://arc42.org/) menjawab dua pertanyaan secara pragmatis dan dapat disesuaikan dengan kebutuhan Anda. Apa yang sebaiknya Anda dokumentasikan/komunikasikan tentang arsitektur Anda? Bagaimana sebaiknya mendokumentasikan/mengomunikasikannya? Arc42 mencakup catatan keputusan arsitektur serta panduan tentang tujuan, batasan, konteks, kualitas, risiko, dan lainnya.

[Model C4](https://c4model.com/) adalah pendekatan yang mudah dipelajari dan ramah pengembang untuk membuat diagram arsitektur perangkat lunak. C4 adalah kumpulan diagram hierarkis untuk konteks, kontainer, komponen, dan kode, ditambah diagram pendukung untuk lanskap sistem, dinamis, dan penerapan.

## Diagram, tampilan, dan sudut pandang arsitektur

Diagram arsitektur disebut "tampilan arsitektur".

"Tampilan arsitektur" adalah contoh dari "sudut pandang arsitektur".

"Sudut pandang arsitektur" memperhatikan audiens tertentu dengan kepedulian tertentu.

Contoh sudut pandang, tampilan, dan diagram arsitektur:

- Kapabilitas bisnis

- Proses bisnis tingkat tinggi

- [Aliran nilai](https://en.wikipedia.org/wiki/Value_stream)

- Fungsi perangkat lunak yang dipetakan ke komponen aplikasi

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Diagram konteks (TO-BE / AS-IS)

- [C4 Model](https://en.wikipedia.org/wiki/C4_model) Diagram kontainer (TO-BE / AS-IS)

- [Diagram entitas-relasi](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) untuk memetakan entitas data ke komponen aplikasi

- [Diagram urutan](https://en.wikipedia.org/wiki/Sequence_diagram) untuk menggambarkan alur fungsional di dalam sistem dan untuk integrasi

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagram untuk menggambarkan aliran data antarkomponen aplikasi

- [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) diagram untuk menggambarkan proses bisnis / skenario pengguna

- [Manajemen Identitas dan Akses](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM) diagram

- [Kontrol Akses Berbasis Peran](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) diagram dengan peran per komponen aplikasi

- [Kontrol Akses Berbasis Atribut](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) diagram dengan atribut per komponen aplikasi

- Diagram privasi

Diagram terkait:

- Diagram kasus penggunaan menunjukkan kasus penggunaan kepada manajemen/pelanggan, yang mendahului kebutuhan, yang mendahului arsitektur perangkat lunak.

- Diagram penerapan menunjukkan perangkat keras/komputer fisik tempat komponen perangkat lunak diterapkan.
- Diagram alir data menunjukkan bagaimana data bergerak melalui sistem dan diubah.
- Diagram urutan digunakan untuk menunjukkan cara kerja protokol seperti HTTP pada sumbu waktu.

- Diagram aktivitas menggambarkan alur kerja aktivitas yang dilakukan sistem perangkat lunak, seperti AI NPC.

## Fitness function untuk keputusan sebagai kode

Fitness function adalah pemeriksaan otomatis yang objektif, ditulis dengan kode pemrograman, yang memverifikasi bahwa keputusan tetap dipertahankan.

- Fitness function membuat keputusan dapat diuji dan terjamin.

- Fitness function untuk keputusan dapat sangat membantu penjaminan mutu, proses regulasi, dan tujuan tata kelola.

### Bagaimana fitness function terhubung dengan keputusan

Catatan keputusan mendokumentasikan keputusan, sedangkan fitness function menjamin keputusan tersebut.

- Contoh keputusan: Kami menggunakan event sourcing untuk memenuhi persyaratan audit.

- Contoh fitness function: Kami menggunakan server integrasi berkelanjutan untuk menguji bahwa semua perubahan status harus menghasilkan event.

### Mengapa fitness function membantu keputusan

Pengukuran objektif: Fitness function lulus atau gagal, sehingga pekerjaan terlihat dan jelas.

Penggunaan berkelanjutan: Fitness function adalah aturan hidup Anda, dijalankan pada setiap commit dan build.

Percaya diri untuk melakukan refactoring: Fitness function secara otomatis menangkap kesalahan aturan keputusan.

Tata kelola yang dapat diskalakan: Fitness function menjamin standar tanpa menciptakan hambatan.

### Dapatkah fitness function menggunakan AI?

Fitness function dapat memanfaatkan LLM AI untuk keputusan dengan mengajukan pertanyaan tentang pekerjaan Anda,
seperti rencana, kode, skema, API, dan lainnya:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

### Pengujian unit arsitektur

[ArchUnit](https://www.archunit.org/): memeriksa aturan arsitektur kode Java dengan menggunakan kerangka pengujian unit Java biasa apa pun.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): memeriksa aturan arsitektur kode TypeScript dan kode JavaScript dengan menggunakan Jest, Vitest, Jasmine, dan sebagainya.

## Pagar pengaman keputusan untuk pull request

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
otomatis memunculkan catatan keputusan yang tepat pada saat yang tepat, yaitu ketika
pengembang sedang mengubah kode yang dicakup keputusan tersebut. Alih-alih berharap pengembang
membaca folder dokumen sebelum menggabungkan, konteks yang relevan muncul langsung di pull request.

Ini berlaku untuk semua jenis catatan keputusan: keputusan arsitektur, keputusan data, keputusan kepatuhan, keputusan klinis dan medis, keputusan keamanan, dan lainnya.

Bekerja dengan sistem CI apa pun (GitLab, Jenkins, CircleCI) dan sebagai hook pre-commit.
Sumber terbuka. Lisensi MIT.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) adalah GitHub
Action yang menggagalkan pull request ketika jalur kode yang dipantau berubah tanpa catatan keputusan arsitektur yang ditambahkan atau diperbarui. Pengecualian bersifat eksplisit: baris
`ADR-Exempt:` beserta alasan meloloskan gerbang dan ditulis ke ringkasan job. Tidak terikat templat, tanpa dependensi. Sumber terbuka. Lisensi MIT.

## Untuk informasi lebih lanjut

Pengantar:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Templat:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Mendalam:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - pelajaran arsitektur perangkat lunak bulanan gratis

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Alat:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Panduan khusus perusahaan:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Contoh:

- [Repository of Architecture Decision Records made for the Arachne Framework](https://github.com/arachne-framework/architecture)

Video:

- [An introduction to arc42 with Savvas Kleanthous](https://www.youtube.com/watch?v=V5clR8c6D7o)

- [The C4 model for visualising software architecture - by Simon Brown](https://www.youtube.com/watch?v=KvoBrUd1-5E)

Podcast:

- [Software Architecture Bookclub Podcast](https://www.developertoarchitect.com/bookclub-podcast.html)

Buku:

- [Software Architecture Metrics: Case Studies to Improve the Quality of Your Architecture - by Christian Ciceri, Dave Farley, Neal Ford, Andrew Harmel-Law, Michael Keeling and Carola Lilienthal](https://www.amazon.com/Software-Architecture-Metrics-Christian-Ciceri-ebook/dp/B0B1NZ8Z5V)

- [Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives - by Nick Rozanski and Eoin Woods](https://www.amazon.com/Software-Systems-Architecture-Stakeholders-Perspectives/dp/032171833X)

- [Software Architecture in Practice (SEI Series in Software Engineering)](https://www.amazon.com/Software-Architecture-Practice-SEI-Engineering-ebook/dp/B094CPJ96B)

- [Documenting Software Architectures: Views and Beyond (SEI Series in Software Engineering)](https://www.amazon.com/Documenting-Software-Architectures-Beyond-Engineering-ebook/dp/B0046XS3RO)

- [The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise](https://www.amazon.com/Software-Architect-Elevator-Redefining-Architects-ebook/dp/B086WQ9XL1)

- [Fundamentals of Software Architecture: An Engineering Approach - by Mark Richards and Neal Ford](https://www.amazon.com/Fundamentals-Software-Architecture-Engineering-Approach-ebook/dp/B0849MPK73)

- [Building Evolutionary Architectures - by Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage](https://www.amazon.com/Building-Evolutionary-Architectures-Neal-Ford-ebook/dp/B0BN4T1P27?crid=37FA31IFLAS0Z)

- [Foundations of Decision Analysis by Ronald Howard and Ali Abbas](https://www.amazon.com/Foundations-Decision-Analysis-Ronald-Howard-ebook/dp/B00SZECJTI?crid=14BK5SDP76UN6)

- [Head First Software Architecture - by Raju Gandhi, Neal Ford and Mark Richards](https://www.amazon.com/Head-First-Software-Architecture-Architectural-ebook/dp/B0CW1JMNF2)

- [Communication Patterns: A Guide for Developers and Architects - by Jacqui Read](https://www.amazon.com/Communication-Patterns-Guide-Developers-Architects/dp/1098140540)

Lihat juga:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Format YAML/JSON yang netral terhadap vendor dan dapat dibaca mesin untuk merepresentasikan keputusan dengan penalaran eksplisit, asumsi, keadaan kognitif, dan pertukaran. Melengkapi ADR dengan menambahkan penalaran terstruktur yang dapat divalidasi ke dokumentasi keputusan.
