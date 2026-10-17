# Cithakan cathetan keputusan saka Jeff Tyree lan Art Akerman

Iki cithakan deskripsi keputusan arsitektur sing diterbitake ing ["Architecture Decisions: Demystifying Architecture" dening Jeff Tyree lan Art Akerman, Capital One Financial](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf).

* **Masalah (Issue)**: Jlentrehake masalah desain arsitektur sing lagi kok tanggapi, tanpa ninggal pitakon babagan kenapa kowe nanggapi masalah iki saiki. Kanthi pendekatan minimalis, mung tanggapi lan dokumentasi masalah sing perlu ditanggapi ing macem-macem titik daur urip.

* **Keputusan (Decision)**: Pratelakake kanthi cetha arah arsitektur—yaiku, posisi sing wis kok pilih.

* **Status**: Status keputusan, kayata pending, wis diputuske, utawa disetujoni.

* **Grup (Group)**: Kowe bisa nggunakake pengelompokan sederhana—kayata integrasi, presentasi, data, lan sapanunggalane—kanggo mbiyantu ngatur kumpulan keputusan. Kowe uga bisa nggunakake ontologi arsitektur sing luwih canggih, kayata kagungane John Kyaruzi lan Jan van Katwijk, sing nduwe kategori sing luwih abstrak kayata event, kalender, lan lokasi. Upamane, nganggo ontologi iki, kowe bakal ngelompokake keputusan sing nangani kedadeyan ing ngendi sistem mbutuhake informasi ing event.

* **Anggepan (Assumptions)**: Jlentrehake kanthi cetha anggepan dhasar ing lingkungan ing ngendi kowe nggawe keputusan—biaya, jadwal, teknologi, lan sapanunggalane. Elinga yen watesan lingkungan (kayata standar teknologi sing ditampa, arsitektur perusahaan, pola sing umum digunakake, lan sapanunggalane) bisa mbatesi alternatif sing kok pikirake.

* **Watesan (Constraints)**: Cathet watesan tambahan marang lingkungan sing bisa ditimbulake dening alternatif sing dipilih (keputusan).

* **Posisi (Positions)**: Dhaptaren posisi (pilihan utawa alternatif sing bisa ditindakake) sing wis kok pikirake. Iki asring mbutuhake panjelasan dawa, kadhang malah model lan diagram. Iki dudu dhaptar lengkap. Nanging, kowe ora pengin krungu pitakon "Apa kowe wis mikir babagan...?" nalika review pungkasan; iki nyebabake ilange kapercayan lan dipitakonake keputusan arsitektur liyane. Bagean iki uga mbiyantu mesthekake yen kowe wis ngrungokake panemune wong liya; nyatakake panemu liya kanthi tegas mbiyantu ngrekrut para panyengkuyunge menyang keputusanmu.

* **Argumentasi (Argument)**: Jlentrehake kenapa kowe milih sawijining posisi, kalebu perkara kayata biaya implementasi, biaya total kepemilikan, wektu menyang pasar, lan kasedhiyan sumber daya pangembangan sing dibutuhake. Iki mbok menawa penting kaya keputusan kuwi dhewe.

* **Implikasi (Implications)**: Keputusan nggawa akeh implikasi, kaya sing ditunjukake dening metamodel REMAP. Upamane, keputusan bisa nuwuhake kabutuhan nggawe keputusan liyane, nggawe kabutuhan anyar, utawa ngowahi kabutuhan sing wis ana; menehi watesan tambahan marang lingkungan; mbutuhake negosiasi maneh lingkup utawa jadwal karo pelanggan; utawa mbutuhake pelatihan staf tambahan. Mangerteni lan nyatakake implikasi keputusanmu kanthi cetha bisa efektif banget kanggo entuk dhukungan lan nggawe peta dalan kanggo eksekusi arsitektur.

* **Keputusan gegayutan (Related decisions)**: Cetha yen akeh keputusan sing gegayutan; kowe bisa nyathet ing kene. Nanging, ing praktik kita nemokake yen matriks telusur, wit keputusan, utawa metamodel luwih migunani. Metamodel migunani kanggo nuduhake hubungan kompleks kanthi diagram (kayata model Rose).

* **Kabutuhan gegayutan (Related requirements)**: Keputusan kudu didorong bisnis. Kanggo nuduhake akuntabilitas, petakna keputusanmu kanthi tegas marang tujuan utawa kabutuhan. Kowe bisa nyathet kabutuhan gegayutan iki ing kene, nanging kita nemokake luwih trep ngrujuk matriks telusur. Kowe bisa ngevaluasi kontribusi saben keputusan arsitektur kanggo nyukupi saben kabutuhan, banjur ngevaluasi sepira apik kabutuhan kuwi dituhoni ing kabeh keputusan. Yen sawijining keputusan ora nyumbang kanggo nyukupi kabutuhan, aja nggawe keputusan kuwi.

* **Artefak gegayutan (Related artifacts)**: Dhaptaren dokumen arsitektur, desain, utawa lingkup sing kena pengaruh keputusan iki.

* **Prinsip gegayutan (Related principles)**: Yen perusahaan nduwe kumpulan prinsip sing wis disepakati, pesthekna yen keputusan konsisten karo siji utawa luwih saka prinsip kuwi. Iki mbiyantu mesthekake keselarasan ing domain utawa sistem.

* **Cathetan (Notes)**: Amarga proses nggawe keputusan bisa mbutuhake pirang-pirang minggu, kita nemokake migunani nyathet cathetan lan masalah sing dirembug tim sajrone proses sosialisasi.
