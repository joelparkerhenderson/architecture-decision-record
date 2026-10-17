# Cithakan cathetan keputusan saka arc42

<https://arc42.org/overview>

## 1. Bubuka lan Tujuan

Katrangan cendhak babagan kabutuhan, daya pendorong, ekstrak (utawa abstrak) kabutuhan. Telung (paling akeh lima) tujuan kualitas paling dhuwur kanggo arsitektur sing nduwe prioritas
paling dhuwur kanggo pemangku kepentingan utama. Tabel pemangku kepentingan penting
karo pangarep-arep babagan arsitektur.

## 1.1 Ringkesan Kabutuhan

### Isi

Katrangan cendhak babagan kabutuhan fungsional, daya pendorong, ekstrak (utawa
abstrak) kabutuhan. Link menyang dokumen kabutuhan (muga-muga ana), kanthi informasi ing ngendi nemokake. 

### Motivasi

Saka sudut pandang pangguna pungkasan, sawijining sistem digawe utawa diowahi kanggo
nambah dhukungan kegiatan bisnis lan/utawa nambah kualitas. 

### Wujud

Katrangan teks cendhak, mbok menawa ing format kasus panggunaan tabel. Yen dokumen kabutuhan
ana, ringkesan iki kudu ngrujuk dokumen-dokumen kuwi.

Jagaa kutipan-kutipan iki sacendhak-cendhake. Imbangna keterbacaan dokumen iki
karo redundansi potensial marang dokumen kabutuhan. 

## 1.2 Tujuan kualitas

### Isi

Telung (paling akeh lima) tujuan kualitas paling dhuwur kanggo arsitektur sing keleksanane
paling penting kanggo pemangku kepentingan utama. Sing dimaksud tenan yaiku tujuan kualitas
kanggo arsitektur. Aja dicampur karo tujuan proyek. Ora kudu
padha. Standar ISO 25010 menehi ringkesan apik babagan topik potensial sing narik kawigaten.

### Motivasi

Kowe kudu ngerti tujuan kualitas pemangku kepentingan paling pentingmu, amarga
iku bakal mengaruhi keputusan arsitektur dhasar. Cetha banget babagan kualitas-kualitas iki, singkiri tembung-tembung muluk. Yen kowe minangka arsitek ora
ngerti kepriye kualitas karyamu bakal dijajaki …

### Wujud

Tabel kanthi tujuan kualitas paling penting lan skenario konkret, diurutake miturut prioritas.

## 1.3 Pemangku kepentingan

### Isi

Ringkesan eksplisit pemangku kepentingan sistem, yaiku kabeh wong, peran, utawa
organisasi sing

- kudu ngerti arsitektur

- kudu diyakinake babagan arsitektur

- kudu makarya karo arsitektur utawa kode

- butuh dokumentasi arsitektur kanggo pagaweyane

- kudu nggawe keputusan babagan sistem utawa pangembangane

### Motivasi

Kowe kudu ngerti kabeh pihak sing melu ing pangembangan sistem utawa sing kena pengaruh
sistem. Yen ora, kowe bisa nampa kejutan sing ora nyenengake mengko ing proses
pangembangan. Pemangku kepentingan iki nemtokake jembar lan tingkat rincian
pagaweyanmu lan asile.

### Wujud

Tabel kanthi jeneng peran, jeneng wong, lan pangarep-arep babagan
arsitektur lan dokumentasie.

## 2. Watesan

Apa wae sing mbatesi tim ing keputusan desain lan implementasi utawa keputusan babagan proses sing gegayutan. Kadhang bisa ngluwihi sistem individual lan
bener kanggo kabeh organisasi lan perusahaan.

### Isi

Kabutuhan apa wae sing mbatesi arsitek piranti lunak ing kabebasan desain lan keputusan implementasi utawa keputusan babagan proses pangembangan. Watesan-watesan iki
kadhang ngluwihi sistem individual lan bener kanggo kabeh
organisasi lan perusahaan.

### Motivasi

Arsitek kudu ngerti persis ing ngendi dheweke bebas ing keputusan desaine lan
ing ngendi dheweke kudu manut watesan. Watesan tansah kudu ditangani;
nanging bisa uga bisa dirundhingake.

### Wujud

Tabel sederhana watesan karo katrangan. Yen perlu kowe bisa mbagi dadi
watesan teknis, watesan organisasi lan politik, lan konvensi (upamane pandhuan pamrograman utawa versioning, konvensi dokumentasi utawa panamaan)

## 3. Konteks lan Lingkup

Misahake sistemmu saka mitra komunikasi (njaba) (sistem tetangga
lan pangguna). Nemtokake antarmuka njaba. Ditampilake saka perspektif
bisnis/domain (tansah) utawa perspektif teknis (opsional)

### Isi

Lingkup lan konteks sistem - kaya jenenge - misahake sistemmu (yaiku
lingkupmu) saka kabeh mitra komunikasie (sistem tetangga lan pangguna,
yaiku konteks sistemmu). Kanthi mangkono nemtokake antarmuka njaba.

Yen perlu, bedakake konteks bisnis (input lan output khusus domain) saka konteks teknis (saluran, protokol, hardware).

### Motivasi

Antarmuka domain lan antarmuka teknis marang mitra komunikasi
kalebu aspek paling kritis sistemmu. Pesthekna yen kowe mangerteni
kanthi lengkap.

### Wujud

- Macem-macem diagram konteks

- Dhaptaren mitra komunikasi lan antarmukane.

## 3.1 Konteks bisnis

### Isi

Spesifikasi kabeh mitra komunikasi (pangguna, sistem TI, …) karo
panjelasan input lan output utawa antarmuka khusus domain. Opsional kowe
bisa nambah format khusus domain utawa protokol komunikasi.

### Motivasi

Kabeh pemangku kepentingan kudu mangerteni data apa sing ditukar karo lingkungan
sistem.

### Wujud

Kabeh jinis diagram sing nuduhake sistem minangka kothak ireng lan nemtokake antarmuka
domain marang mitra komunikasi.

Utawa (utawa tambahan) kowe bisa nggunakake tabel. Judhul tabel yaiku
jeneng sistemmu, telung kolom ngemot jeneng mitra komunikasi,
input, lan output.

## 3.2 Konteks teknis

### Isi

Antarmuka teknis (saluran lan media transmisi) sing nyambungake sistemmu menyang
lingkungane. Tambahan pemetaan input/output khusus domain menyang
saluran, yaiku panjelasan I/O endi sing nggunakake saluran endi.

### Motivasi

Akeh pemangku kepentingan nggawe keputusan arsitektur adhedhasar antarmuka teknis
antarane sistem lan konteksé. Utamane desainer infrastruktur utawa hardware sing nemtokake antarmuka teknis iki.

### Wujud

Upamane diagram deployment UML sing njlentrehake saluran menyang sistem tetangga, bebarengan karo
tabel pemetaan sing nuduhake hubungan antarane saluran lan
input/output.

## 4. Strategi Solusi

Ringkesan keputusan dhasar lan strategi solusi sing mbentuk
arsitektur. Bisa kalebu teknologi, dekomposisi tingkat dhuwur, pendekatan kanggo
entuk tujuan kualitas utama lan keputusan organisasi sing gegayutan.

### Isi

Ringkesan lan panjelasan cendhak keputusan dhasar lan strategi solusi, sing mbentuk arsitektur sistem. Iki kalebu

- keputusan teknologi

- keputusan babagan dekomposisi tingkat dhuwur sistem, upamane panggunaan pola arsitektur utawa pola desain

- keputusan babagan carane entuk tujuan kualitas utama

- keputusan organisasi sing gegayutan, upamane milih proses pangembangan utawa nyerahake tugas tartamtu marang pihak katelu.

### Motivasi

Keputusan-keputusan iki dadi watu pondasi arsitekturmu. Iki dadi dhasar
kanggo akeh keputusan rinci liyane utawa aturan implementasi.

### Wujud

Jagaa panjelasan keputusan kunci iki cendhak.

Wenehana motivasi babagan apa sing wis kok putuske lan kenapa kowe mutusake kaya mangkono, adhedhasar
pernyataan masalahmu, tujuan kualitas, lan watesan utama. Rujuk rincian ing
bagean sabanjure (bagean 5 kanggo rincian struktural, bagean 8 kanggo
konsep lintas-bidang).

Kowe bisa nggunakake dhaptar pendekatan solusi utawa tabel.

## 5. Tampilan Blok Bangunan

Dekomposisi statis sistem, abstraksi kode sumber, ditampilake minangka
hirarki kothak putih (ngemot kothak ireng), nganti tingkat rincian
sing cocog.

### Isi

Tampilan blok bangunan nuduhake dekomposisi statis sistem dadi
blok bangunan (modul, komponen, subsistem, kelas, antarmuka, paket,
pustaka, framework, lapisan, partisi, tingkat, fungsi, makro, operasi,
struktur data, …) uga dependensine (hubungan, asosiasi,
…)

Tampilan iki wajib kanggo saben dokumentasi arsitektur. Kaya omah, iki
denah lantaine.

### Motivasi

Njaga ringkesan kode sumbermu kanthi nggawe strukture bisa dimangerteni
liwat abstraksi.

Iki ngidini kowe komunikasi karo pemangku kepentinganmu ing tingkat abstrak
tanpa mbukak rincian implementasi.

### Wujud

Tampilan blok bangunan yaiku kumpulan hirarkis kothak ireng lan kothak
putih (deleng gambar ing ngisor) lan deskripsine.

## 5.1 Kothak Putih Sistem Sakabèhé

Ing kene kowe njlentrehake dekomposisi sistem sakabèhé nganggo cithakan kothak putih ing ngisor. Isine

- diagram ringkesan

- motivasi kanggo dekomposisi

- deskripsi kothak ireng saka blok bangunan sing ana. Kanggo iki kita nawakake alternatif:

  - gunakna siji tabel kanggo ringkesan cendhak lan praktis kabeh blok bangunan sing ana lan antarmukane

  - gunakna dhaptar deskripsi kothak ireng blok bangunan miturut cithakan kothak ireng (deleng ing ngisor). Gumantung pilihan piranti, dhaptar iki bisa dadi sub-bab (ing berkas teks), sub-kaca (ing Wiki) utawa unsur bersarang (ing piranti pemodelan).

  - (opsional:) antarmuka penting sing ora dijlentrehake ing cithakan kothak ireng blok bangunan, nanging penting banget kanggo mangerteni kothak putih.

Amarga ana akeh cara kanggo nemtokake antarmuka, kita ora nyedhiyakake cithakan khusus kanggo iku.

Ing kasus paling apik, kowe cukup nganggo conto utawa tandha tangan sederhana.

## 5.2 Tingkat 2

Ing kene kowe bisa nemtokake struktur njero (sawetara) blok bangunan saka tingkat 1
minangka kothak putih.

Kowe kudu mutusake blok bangunan sistemmu endi sing cukup penting kanggo
mbenerake deskripsi rinci kaya mangkono. Luwih utamakake relevansi tinimbang kelengkapan.
Tentokna blok bangunan sing penting, ngageti, beresiko, kompleks utawa ora stabil. Linggihna
bagean sistemmu sing biasa, sederhana, mbosenake utawa standar

### 5.2.1 Kothak Putih kanggo blok bangunan 1

Nemtokake struktur njero blok bangunan 1.

Gunakna cithakan kothak putih (deleng ing ndhuwur).

## 6. Tampilan Runtime

Prilaku blok bangunan minangka skenario, nyakup kasus panggunaan utawa
fitur penting, interaksi ing antarmuka njaba kritis, operasi lan
administrasi plus prilaku kesalahan lan pengecualian.

### Isi

Tampilan runtime njlentrehake prilaku lan interaksi konkret blok bangunan sistem ing wujud skenario saka bidang-bidang ing ngisor:

- kasus panggunaan utawa fitur penting: kepriye blok bangunan nglakokake?

- interaksi ing antarmuka njaba kritis: kepriye blok bangunan kerja sama karo pangguna lan sistem tetangga?

- operasi lan administrasi: peluncuran, start-up, mandheg

- skenario kesalahan lan pengecualian

Cathetan: Kriteria utama kanggo milih skenario (urutan, alur kerja) yaiku relevansi arsitekture. Ora penting njlentrehake akeh skenario. Luwih becik dokumentasi pilihan sing representatif.

### Motivasi

Kowe kudu mangerteni carane (instans) blok bangunan sistemmu nindakake tugase lan komunikasi nalika runtime. Kowe biasane bakal nyathet skenario ing dokumentasimu kanggo komunikasi arsitekturmu marang pemangku kepentingan sing kurang gelem utawa bisa maca lan mangerteni model statis (tampilan blok bangunan, tampilan deployment).

### Wujud

Ana akeh notasi kanggo njlentrehake skenario, upamane


- dhaptar langkah bernomor (nganggo basa alami)

- diagram aktivitas utawa flow chart

- diagram urutan

- BPMN utawa EPC (rantai proses event)

- mesin status

- lan sapanunggalane.

## 6.n Skenario Runtime n (1, 2, 3, lan sapanunggalane)

Lebokna diagram runtime utawa deskripsi tekstual skenario.

Lebokna deskripsi aspek-aspek sing nggatekake saka interaksi antarane instans blok bangunan sing digambarake ing diagram iki.

## 7. Tampilan Deployment

Infrastruktur teknis kanthi lingkungan, komputer, prosesor, topologi.
Pemetaan blok bangunan (piranti lunak) menyang unsur infrastruktur.

### Isi

Tampilan deployment njlentrehake:

- infrastruktur teknis sing digunakake kanggo nglakokake sistemmu, kanthi unsur infrastruktur
  kayata lokasi geografis, lingkungan, komputer, prosesor,
  saluran lan topologi jaringan uga unsur infrastruktur liyane lan

- pemetaan blok bangunan (piranti lunak) menyang unsur infrastruktur kuwi.

Asring sistem dilakokake ing lingkungan sing beda, upamane lingkungan
pangembangan, lingkungan tes, lingkungan produksi. Ing kasus kaya mangkono kowe kudu
dokumentasi kabeh lingkungan sing gegayutan.

Dokumentasi tampilan deployment utamane nalika piranti lunakmu dilakokake minangka sistem
terdistribusi karo luwih saka siji komputer, prosesor, server utawa kontainer
utawa nalika kowe ngrancang lan mbangun prosesor lan chip hardware dhewe.

Saka perspektif piranti lunak, cukup nyathet unsur-unsur infrastruktur sing dibutuhake kanggo nuduhake deployment blok bangunanmu.
Arsitek hardware bisa ngluwihi iku lan njlentrehake infrastruktur nganti tingkat rincian apa wae sing dibutuhake kanggo nyathet. 

### Motivasi

Piranti lunak ora bisa mlaku tanpa hardware. Infrastruktur dhasar iki bisa lan bakal mengaruhi sistemmu lan/utawa sawetara konsep lintas-bidang. Mula, kowe
kudu ngerti infrastrukture.

### Wujud

Mbok menawa diagram deployment tingkat paling dhuwur wis kalebu ing bagean 3.2 minangka konteks teknis karo infrastruktur dhewe minangka SIJI kothak ireng. Ing bagean iki kowe bakal nggedhekake kothak ireng iki nganggo diagram deployment tambahan.

- UML nawakake diagram deployment kanggo nyatakake tampilan kuwi. Gunakna, mbok menawa nganggo diagram bersarang, nalika infrastrukturmu luwih kompleks.

- Nalika pemangku kepentingan (hardware) luwih seneng jinis diagram liyane tinimbang
  diagram deployment UML, wenehana nggunakake jinis apa wae sing bisa nuduhake simpul lan saluran infrastruktur.

## 7.1 Infrastruktur Tingkat 1

Jlentrehake (biasane kanthi gabungan diagram, tabel, lan teks):

- distribusi sistemmu menyang pirang-pirang lokasi, lingkungan, komputer, prosesor, .. uga sambungan fisik antarane

- pembenaran utawa motivasi penting kanggo struktur deployment iki

- fitur kualitas lan/utawa kinerja infrastruktur

- pemetaan artefak piranti lunak (blok bangunan) menyang unsur infrastruktur

Kanggo pirang-pirang lingkungan utawa deployment alternatif, tulung salin bagean arc42 kuwi kanggo kabeh lingkungan sing gegayutan. **

## 7.2 Infrastruktur Tingkat 2

Ing kene kowe bisa nglebokake struktur njero (sawetara) unsur infrastruktur saka infrastruktur tingkat 1.

Tulung salin struktur saka tingkat 1 kanggo saben unsur sing dipilih.

## 8. Konsep Lintas-Bidang

Sakabèhé, aturan utama lan pendekatan solusi sing gegayutan ing pirang-pirang
bagean (→ lintas-bidang) sistem. Konsep asring gegayutan karo pirang-pirang
blok bangunan. Lebokna topik beda-beda kayata model domain, pola lan
gaya arsitektur, aturan nggunakake teknologi tartamtu lan aturan
implementasi.

### Isi

Bagean iki njlentrehake konsep lintas-bidang (praktik, pola, aturan
utawa gagasan solusi). Konsep kaya mangkono asring gegayutan karo pirang-pirang blok bangunan.
Bisa kalebu akeh topik sing beda-beda.

### Motivasi

Konsep mbentuk dhasar integritas konseptual (konsistensi, homogenitas)
arsitektur. Mula, iku kontribusi penting kanggo entuk kualitas njero sistemmu.

Iki papan ing cithakan sing kita sediyakake kanggo spesifikasi kohesif
konsep-konsep kaya mangkono.

Akeh konsep iki gegayutan utawa mengaruhi sawetara blok bangunanmu.

### Wujud

Wujude bisa maneka warna:

- makalah konsep kanthi struktur apa wae

- implementasi conto, utamane kanggo konsep teknis

- kutipan model lintas-bidang utawa skenario nganggo notasi saka tampilan arsitektur

### Struktur bagean iki

Pilihen mung topik sing paling dibutuhake kanggo sistemmu lan wenehana saben judhul tingkat 2 ing bagean iki (upamane 8.1, 8.2 lan sapanunggalane).

- AJA COBA nyakup kabeh topik saka diagram ing ndhuwur.

### Latar Mburi

Sawetara topik ing sistem asring gegayutan karo pirang-pirang blok bangunan, unsur hardware
utawa proses pangembangan. Mbok menawa luwih gampang komunikasi utawa dokumentasi
topik lintas-bidang kaya mangkono ing lokasi sentral, tinimbang mbaleni ing
deskripsi blok bangunan, unsur hardware utawa proses pangembangan sing gegayutan.

Sawetara konsep bisa gegayutan karo kabeh unsur sistem, liyane mung
relevan kanggo sawetara.

## 9. Keputusan Arsitektur

Keputusan arsitektur sing penting, larang, kritis, skala gedhe utawa beresiko
kalebu alasane.

### Isi

Keputusan arsitektur sing penting, larang, skala gedhe utawa beresiko kalebu
alasane. Sing dimaksud "keputusan" yaiku milih siji alternatif adhedhasar
kriteria sing diwenehake.

Tulung gunakna pertimbanganmu kanggo mutusake apa keputusan arsitektur kudu
didokumentasi ing bagean sentral iki utawa luwih becik didokumentasi
sacara lokal (upamane ing cithakan kothak putih saka siji blok bangunan). Singkiri teks
redundan. Rujuk bagean 4, ing ngendi kowe wis nyathet keputusan
paling penting saka arsitekturmu.

### Motivasi

Pemangku kepentingan sistemmu kudu bisa mangerteni lan nelusuri keputusanmu.

### Wujud

- ADR (cathetan keputusan arsitektur) kanggo saben keputusan penting

- dhaptar utawa tabel, diurutake miturut pentinge lan akibat utawa

- luwih rinci ing wujud bagean kapisah saben keputusan

### Latar Mburi (babagan ADR)

Potongan dokumentasi sing luwih cilik luwih gampang dibaca, digawe lan dijaga. Nalika
nganti keputusan arsitektur, tim pangembang asring:

- ngerti babagan keputusan, amarga katon upamane ing kode sumber, nanging

- ora ngerti motivasi ing mburi keputusan kuwi (deleng Nygard 2011)

Mula kowe kudu dokumentasi sawetara keputusan penting bebarengan karo motivasi, penalarane

### Usul kita babagan keputusan

Jagaa kumpulan keputusan penting sacara arsitektural, yaiku keputusan sing
mengaruhi struktur, karakteristik kualitas, dependensi lan antarmuka penting (utamane njaba),
utawa teknik konstruksi (matur nuwun marang Michael
Nygard kanggo usul iki).

## 10. Kabutuhan Kualitas

Kabutuhan kualitas minangka skenario, karo wit kualitas kanggo menehi ringkesan
tingkat dhuwur. Tujuan kualitas paling penting kudu wis dijlentrehake ing bagean
1.2. (tujuan kualitas).

### Isi

Bagean iki ngemot kabeh kabutuhan kualitas sing gegayutan.

Sing paling penting saka kabutuhan iki wis dijlentrehake ing bagean
1.2. (tujuan kualitas), mula mung kudu dirujuk ing kene. Ing bagean 10 iki
kowe uga kudu nyathet kabutuhan kualitas sing kurang penting,
sing ora bakal nuwuhake resiko gedhe yen ora kaleksanan kebak (nanging apik yen ana).

### Motivasi

Amarga kabutuhan kualitas bakal duwe pengaruh akeh marang keputusan arsitektur, kowe kudu ngerti kualitas apa sing bener-bener penting kanggo
pemangku kepentinganmu, kanthi cara spesifik lan bisa diukur.

### Informasi Luwih Akeh

Deleng model kualitas Q42 sing ekstensif ing https://quality.arc42.org.

## 10.1 Ringkesan Kabutuhan Kualitas

### Isi

Ringkesan utawa kesimpulan kabutuhan kualitas.

### Motivasi

Asring kita nemoni puluhan (utawa malah atusan) kabutuhan kualitas rinci.
Ing bagean ringkesan iki kowe kudu nyoba ngringkes, upamane kanthi njlentrehake
kategori utawa topik (kaya sing disaranake ISO 25010:2023 utawa Q42

Yen deskripsi ringkesan iki wis tepat, cukup spesifik lan
bisa diukur, kowe bisa nglewati bagean 10.2.

### Wujud

Gunakna tabel sederhana ing ngendi saben larik ngemot kategori utawa topik lan deskripsi
cendhak kabutuhan kualitas. Utawa, kowe bisa nggunakake mindmap kanggo
nata kabutuhan kualitas iki.

Ing literatur, gagasan wit atribut kualitas uga wis diterangake,
sing nempatake istilah umum "kualitas" minangka oyod lan nggunakake panyempurnaan kaya wit
saka istilah "kualitas". [Bass+21] ngenalake istilah "Quality
Attribute Utility Tree" kanggo tujuan iki.

## 10.2 Skenario Kualitas

### Isi

Skenario kualitas ndadekake kabutuhan kualitas konkret lan ngidini mutusake apa
wis kaleksanan (ing pangertian kriteria panrima). Pesthekna yen
skenariomu spesifik lan bisa diukur.

Rong jinis skenario utamane migunani:

- Skenario panggunaan (uga diarani skenario aplikasi utawa skenario kasus panggunaan)
  njlentrehake reaksi runtime sistem marang stimulus tartamtu. Iki uga kalebu
  skenario sing njlentrehake efisiensi utawa kinerja sistem.
  Conto: Sistem nanggapi panjalukan pangguna sajrone sak detik.

- Skenario owah-owahan njlentrehake efek sing dikarepake saka modifikasi utawa ekstensi
  sistem utawa lingkungan sing cedhak. Conto: Fungsionalitas tambahan
  diimplementasikake utawa kabutuhan atribut kualitas owah, lan upaya
  utawa durasi owah-owahan diukur.

### Wujud

Informasi khas kanggo skenario rinci kalebu ing ngisor iki:

Ing wujud cendhak (disenengi ing model Q42):

- Konteks/Latar Mburi: Sistem utawa komponen jinis apa, lingkungan utawa kahanane kepriye?

- Sumber/Stimulus: Sapa utawa apa sing miwiti utawa nggugah prilaku, reaksi utawa tindakan.

- Metrik/Kriteria Panrima: Tanggapan kalebu ukuran utawa metrik

Wujud dawa skenario (disenengi dening SEI lan [Bass+21]) luwih rinci lan kalebu informasi ing ngisor iki:

- ID Skenario: Pengenal unik kanggo skenario.

- Jeneng Skenario: Jeneng cendhak lan deskriptif kanggo skenario.

- Sumber: Entitas (pangguna, sistem, utawa event) sing miwiti skenario.

- Stimulus: Event utawa kahanan pemicu sing kudu ditanggapi sistem.

- Lingkungan: Konteks operasional utawa kahanan ing ngendi sistem ngalami stimulus.

- Artefak: Blok bangunan utawa unsur sistem liyane sing kena pengaruh stimulus.

- Tanggapan: Asil utawa prilaku sing ditampilake sistem minangka reaksi marang stimulus.

- Ukuran Tanggapan: Kriteria utawa metrik sing dinggo ngevaluasi tanggapan sistem.

### Deleng uga

Wiwit Januari 2023, arc42 nyedhiyakake model kualitas pragmatis, sing nyaranake kanggo
menehi label kabutuhan kualitas, nganggo hashtag utawa label kayata #flexible, #efficient,
#usable, #operable, #testable, #secure, #safe, #reliable.

## 11. Resiko lan Utang Teknis

Resiko teknis utawa utang teknis sing dikenal. Masalah potensial apa sing ana ing njero utawa
sakubenge sistem? Apa sing marakake tim pangembang rumangsa nandhang susah?

### Isi

Dhaptar resiko teknis utawa utang teknis sing wis diidentifikasi, diurutake miturut prioritas

### Motivasi

"Manajemen resiko iku manajemen proyek kanggo wong diwasa" (Tim Lister, Atlantic
Systems Guild.)

Iki kudu dadi mottomu kanggo deteksi lan evaluasi sistematis resiko lan utang teknis ing arsitektur, sing bakal dibutuhake dening pemangku kepentingan manajemen
(upamane manajer proyek, pemilik produk) minangka bagean saka analisis resiko lan
perencanaan pangukuran sakabèhé.

### Wujud

Dhaptar resiko lan/utawa utang teknis, mbok menawa kalebu ukuran sing disaranake kanggo
nyuda, nglunakake utawa nyingkiri resiko utawa nyuda utang teknis.
