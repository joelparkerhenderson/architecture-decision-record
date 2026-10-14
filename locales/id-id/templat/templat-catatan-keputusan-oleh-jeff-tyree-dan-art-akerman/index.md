# Templat catatan keputusan oleh Jeff Tyree dan Art Akerman

Ini adalah templat deskripsi keputusan arsitektur yang dipublikasikan dalam ["Architecture Decisions: Demystifying Architecture" oleh Jeff Tyree dan Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Isu**: Jelaskan isu desain arsitektur yang Anda tangani, tanpa menyisakan pertanyaan tentang mengapa Anda menangani isu ini sekarang. Dengan pendekatan minimalis, tangani dan dokumentasikan hanya isu yang perlu ditangani pada berbagai titik dalam siklus hidup.

* **Keputusan**: Nyatakan dengan jelas arah arsitektur, yaitu posisi yang telah Anda pilih.

* **Status**: Status keputusan, seperti pending, decided, atau approved.

* **Grup**: Anda dapat menggunakan pengelompokan sederhana, seperti integrasi, presentasi, data, dan sebagainya, untuk membantu mengorganisasi kumpulan keputusan. Anda juga dapat menggunakan ontologi arsitektur yang lebih canggih, seperti milik John Kyaruzi dan Jan van Katwijk, yang mencakup kategori yang lebih abstrak seperti event, calendar, dan location. Misalnya, dengan ontologi ini, Anda akan mengelompokkan keputusan yang berkaitan dengan kejadian di mana sistem membutuhkan informasi di bawah event.

* **Asumsi**: Jelaskan dengan jelas asumsi yang mendasari lingkungan tempat Anda membuat keputusan, seperti biaya, jadwal, teknologi, dan sebagainya. Perhatikan bahwa batasan lingkungan (seperti standar teknologi yang diterima, arsitektur perusahaan, pola yang umum digunakan, dan sebagainya) dapat membatasi alternatif yang Anda pertimbangkan.

* **Batasan**: Catat setiap batasan tambahan terhadap lingkungan yang mungkin ditimbulkan oleh alternatif yang dipilih (keputusan).

* **Posisi**: Daftarkan posisi (opsi atau alternatif yang layak) yang Anda pertimbangkan. Ini sering membutuhkan penjelasan panjang, kadang bahkan model dan diagram. Ini bukan daftar yang menyeluruh. Namun, Anda tidak ingin mendengar pertanyaan "Apakah Anda sudah memikirkan...?" saat tinjauan akhir; hal ini menyebabkan hilangnya kredibilitas dan keraguan terhadap keputusan arsitektur lainnya. Bagian ini juga membantu memastikan bahwa Anda telah mendengar pendapat orang lain; menyatakan pendapat lain secara eksplisit membantu melibatkan para pendukungnya dalam keputusan Anda.

* **Argumen**: Uraikan mengapa Anda memilih suatu posisi, termasuk hal-hal seperti biaya implementasi, total biaya kepemilikan, waktu ke pasar, dan ketersediaan sumber daya pengembangan yang diperlukan. Ini mungkin sama pentingnya dengan keputusan itu sendiri.

* **Implikasi**: Sebuah keputusan membawa banyak implikasi, seperti yang ditunjukkan oleh metamodel REMAP. Misalnya, sebuah keputusan dapat menimbulkan kebutuhan untuk membuat keputusan lain, menciptakan persyaratan baru, atau mengubah persyaratan yang ada; menimbulkan batasan tambahan terhadap lingkungan; memerlukan negosiasi ulang lingkup atau jadwal dengan pelanggan; atau memerlukan pelatihan staf tambahan. Memahami dan menyatakan implikasi keputusan Anda dengan jelas dapat sangat efektif untuk memperoleh dukungan dan menciptakan peta jalan bagi pelaksanaan arsitektur.

* **Keputusan terkait**: Jelas bahwa banyak keputusan saling terkait; Anda dapat mendaftarkannya di sini. Namun, kami menemukan bahwa dalam praktiknya, matriks keterlacakan, pohon keputusan, atau metamodel lebih berguna. Metamodel berguna untuk menunjukkan hubungan yang kompleks secara diagramatik (seperti model Rose).

* **Persyaratan terkait**: Keputusan harus digerakkan oleh bisnis. Untuk menunjukkan akuntabilitas, petakan keputusan Anda secara eksplisit ke tujuan atau persyaratan. Anda dapat menyebutkan persyaratan terkait ini di sini, tetapi kami menemukan lebih praktis untuk merujuk ke matriks keterlacakan. Anda dapat menilai kontribusi setiap keputusan arsitektur dalam memenuhi setiap persyaratan, lalu menilai seberapa baik persyaratan tersebut terpenuhi di seluruh keputusan. Jika sebuah keputusan tidak berkontribusi untuk memenuhi suatu persyaratan, jangan buat keputusan itu.

* **Artefak terkait**: Daftarkan dokumen arsitektur, desain, atau lingkup terkait yang terdampak oleh keputusan ini.

* **Prinsip terkait**: Jika perusahaan memiliki seperangkat prinsip yang telah disepakati, pastikan keputusan tersebut konsisten dengan satu atau lebih prinsip itu. Hal ini membantu memastikan keselarasan di seluruh domain atau sistem.

* **Catatan**: Karena proses pengambilan keputusan dapat memakan waktu berminggu-minggu, kami menemukan bahwa mencatat catatan dan isu yang dibahas tim selama proses sosialisasi sangat berguna.

