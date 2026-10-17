# Panyimpenan rahasia

Isi:

* [Ringkesan](#ringkesan)
  * [Masalah](#masalah)
  * [Keputusan](#keputusan)
  * [Status](#status)
* [Rincian](#rincian)
  * [Anggepan](#anggepan)
  * [Watesan](#watesan)
  * [Posisi](#posisi)
  * [Argumentasi](#argumentasi)
  * [Implikasi](#implikasi)
* [Gegayutan](#gegayutan)
  * [Keputusan gegayutan](#keputusan-gegayutan)
  * [Kabutuhan gegayutan](#kabutuhan-gegayutan)
  * [Artefak gegayutan](#artefak-gegayutan)
  * [Prinsip gegayutan](#prinsip-gegayutan)
* [Cathetan](#cathetan)
  * [Vault saka HashiCorp](#vault-saka-hashicorp)
  * [LastPass](#lastpass)
  * [Bitwarden](#bitwarden)
  * [EnvKey](#envkey)
  * [Confidant saka Lyft](#confidant-saka-lyft)
  * [Devolutions Password Server](#devolutions-password-server)
  * [Secret Server saka Thycotic](#secret-server-saka-thycotic)


## Ringkesan


### Masalah

Kita kudu nyimpen rahasia, kayata sandi, kunci pribadi, token autentikasi, lan sapanunggalane.

Sawetara rahasia iku berorientasi pangguna. Upamane, pangembang kita pengin bisa nggunakake telpon seluler kanggo nggoleki sandi menyang sawijining layanan.

Sawetara rahasia iku berorientasi sistem. Upamane, pipeline continuous delivery kita kudu bisa nggoleki kredensial kanggo hosting cloud kita.


### Keputusan

Bitwarden kanggo rahasia berorientasi pangguna

Vault saka HashiCorp kanggo rahasia berorientasi sistem.


### Status

Wis diputuske. Kita terbuka kanggo alternatif anyar nalika muncul.


## Rincian


### Anggepan

Kanggo tujuan iki, lan kahanan kita saiki, kita ngajeni kenyamanan berorientasi pangguna, kayata aplikasi seluler sing gampang digunakake.

  * Kita pengin mesthekake akses cepet lan gampang nalika lagi lunga, kayata kanggo pangembang sing nindakake rekayasa keandalan sistem on-call.

  * Kita pengin bisa nuduhake sawetara rahasia ing antarane wong-wong sing dipilih, kayata sawijining tim.

Kita ora nyoba ngrampungake kanggo panyedhia tunggal, kayata nyimpen kabeh rahasia mung ing Amazon utawa Azure utawa Google.

Kita ora pengin pendekatan ad-hoc kayata "eling-elingen" utawa "tulisen ing cathetan" utawa "golekana cara dhewe kanggo nyimpen".

Model keamanan kita kanggo tujuan iki ora masalah nggunakake vendor COTS sing dihormati, kayata piranti manajemen sandi SaaS.


### Watesan

Saiki kita pengin sing gampang yaiku ora perlu nulis kode, ora perlu nginstal server, ora perlu komitmen gedhe, ora perlu nstandarisasi kabeh wong.


### Posisi

Kita nimbang:

1. Manajer sandi siap-pakai berorientasi pangguna: LastPass, 1Password, Bitwarden, Dashlane, KeePass, pass, GPG, lan sapanunggalane.

2. Manajer sandi COTS berorientasi sistem: AWS KMS, Vault saka HashiCorp, EnvKey, Secret Server saka Thycotic, Devolutions Password Server, Confidant saka Lyft.

3. Pendekatan berorientasi nuduhake: nggunakake dokumen Google bareng, utawa saluran Slack bareng, utawa folder jaringan bareng, lan sapanunggalane.

4. Pendekatan ad-hoc teknologi andhap, kayata eling-elingen, nulis cathetan, utawa gumantung marang saben pangguna golek cara dhewe.


### Argumentasi

Bitwarden, LastPass, 1Password, lan Dashlane kabeh yaiku produk komersial siap-pakai.

  * Jinis fitur sing padha kanggo pangguna, tim, organisasi, lan sapanunggalane.

  * Kemampuan desktop kanggo Windows lan Mac, lan kemampuan seluler kanggo Android lan iOS.

  * Ekstensi browser kanggo Chrome lan Firefox, kanggo ngisi formulir otomatis, lan sapanunggalane.

Bitwarden nduwe rong kaluwihan tinimbang liyane:

  * Bitwarden iku open source, tegese keamanane bisa ditinjau kanca sejawat lan perusahaane uga disenengi akeh dening pangembang sing berorientasi keamanan.

  * Anekdot saka para pekerja piranti lunak nggambarake preferensi sing signifikan marang Bitwarden tinimbang liyane.

Conto tulisan apik sing khas: https://jcs.org/2017/11/17/bitwarden

Situs voting sisih-sisihan sing khas: https://stackshare.io/stackups/bitwarden-vs-dashlane

Kita nundha KeyPass, pass, GPG, lan sapanunggalane amarga ana kerumitan tambahan. Kabeh iki katon minangka solusi apik kanggo pangguna teknis. GPG katon apik banget kanggo pangguna teknis sing pengin kemampuan berorientasi perintah lintas-sistem.

Kita nundha KMS amarga nduwe lock-in panyedhia tunggal.

Kita milih Vault kanggo kabutuhan berorientasi sistem, amarga ulasane positif banget, lan amarga HashiCorp nduwe rekam jejak apik banget kanggo piranti lunak lan dhukungan kualitas dhuwur.

Kita veto pendekatan nuduhake kayata liwat dokumen bareng, saluran bareng, folder jaringan bareng, lan sapanunggalane. Iki ora nyedhiyakake kualitas keamanan sing kita karepake.

Kita veto pendekatan ad-hoc teknologi andhap, amarga kita kabeh setuju yen iku dudu dalan maju jangka dawa.


### Implikasi

Pangembang mbok menawa kudu nglacak rahasia ing rong panggonan: Bitwarden kanggo akses berorientasi pangguna, lan Vault kanggo akses berorientasi sistem.


## Gegayutan


### Keputusan gegayutan

Keputusan server CI/CD endi kudu kalebu bukti kemampuan kanggo ngakses rahasia.

Kita bakal kudu mutusake carane ngatur rahasia, babagan kabijakan, rotasi, organisasi, lan sapanunggalane.


### Kabutuhan gegayutan

Rahasia bakal nduwe kabutuhan gegayutan kanggo kepatuhan, audit, lan onboarding/offboarding SDM.


### Artefak gegayutan

Kita ngarepake kita mbok menawa bakal ngekspor sawetara rahasia menyang variabel lingkungan.


### Prinsip gegayutan

Gampang dibatalake.

Gampang paralel yaiku gampang nggunakake macem-macem manajer sandi.

Murah dicoba yaiku ana uji coba gratis lan tanpa komitmen.


## Cathetan

Cathetan evaluasi ing kene. Cathetan-cathetan iki kabeh komentar umum ing macem-macem papan rembugan devops.


### Vault saka HashiCorp

Vault persis apa sing kowe butuhake ing kene. 

Aja mung nglebokake Vault menyang produksi, setelen dhisik ing lingkungan tes, amarga dokumentasi HashiCorp bisa cukup kurang sanajan produke apik banget.

Kurva sinau curam banget lan ora sepele kanggo nyetel. 

Setelan wiwitan rada ngrepotake. Nanging sepadan banget, lan komunitas bakal ndhukung cukup apik supaya kowe bisa mlaku.

Dokumentasi nggegirisi nanging ana akeh panuntun online saka wong-wong sing nyetel, lan yen kowe nggabungake sawetara, kowe bakal duwe setelan sing bisa mlaku.

Setelan wiwitan mbutuhake utak-atik helm chart-e (vault lan consul). Sanajan sacara teknis kowe bisa nggunakake akeh back-end liyane, aku tenan ora nyaranake. Back-end/consul bisa cilik banget yen kowe ora duwe data akeh kanggo disimpen.

Mesthi dadi kenal/akrab nggunakake CLI, amarga GUI-ne luwih kaya bukti-konsep/portal iklan kanggo edisi enterprise-e.

Kasunyatan yen kowe ora bisa mung "ngisi" iku ngrepotake. Upamane yen kowe duwe 5 kolom, kowe kudu nambah manual saben kolom kanggo saben item. Dadi ora kaya kowe nemtokake kolom ing awal kanggo kategori tartamtu, lan ngisi kolom-kolom kuwi kanggo kabeh item ing kategori kuwi, luwih kaya "kowe nggawe kabeh saben wektu", sing (miturut panemuku) nggegirisi.

Kowe mbok menawa uga pengin ndeleng goldfish minangka UI ing ndhuwur vault. Nggawe luwih apik kanggo ngajak timmu. Dheweke uga duwe demo. 1. Setel consul. 2. Setel vault sing nuding consul. 3. Setel goldfish sing nuding vault. 3. Setel sawetara cron job kanggo nglakokake consul snapshot kanggo backup.



### LastPass

LastPass Teams. Kita nggunakake, nduwe cithakan khusus, ACL, ora ana sing kurang miturut panemuku.

Aku ngimplementasikake LastPass ing organisasiku lan menehi nilai C+/B-. Masalah paling gedhe akhir-akhir iki yaiku kurang keandalan. Ing 90 dina pungkasan ana pirang-pirang jam ing ngendi vault dipeksa mlebu mode offline. Iki ora ideal kanggo organisasiku amarga nduwe, secara harfiah, luwih saka 4.000 sandi sing disimpen ing luwih saka 20 folder bareng. Kaya sing bisa kok bayangake karo sandi sakmono akehe, paling ora sawetara dianyari utawa ditambah saben dina. Kita nduwe rencana DR yen masalah luwih saka sajam utawa rong jam: skrip nandatangani lan ngenkripsi dump CSV vault saben wengi sing bisa diimpor menyang keepass.

LastPass nate ngalami gangguan layanan sing ora dilaporake: login 'bisa' nanging ora narik situs, fitur acak rusak ing panel admin, lan ora nuduhake kunci kanthi bener kanggo folder bareng tingkat dhuwur anyar. Aku duwe pangguna 'key push'/backup khusus sing ana ing saben grup. Biasane mlebu minangka pangguna kuwi bakal ndandani masalah nuduhake kunci nanging ora nalika layanan degradasi sanajan apa sing diandharake kaca status...

Kanggo integrasi bisa gampang yen kowe nduwe ACL sing bener karo model hak istimewa paling sithik, upamane yen pangguna nduwe maca & nulis lan mung maca ing sawijining entri utawa folder, dheweke mung entuk idin mung maca. Sayange ACL organisasiku ora paling apik, mula aku pungkasane nggunakake API provisioning JSON lan ~500 baris python amarga sifat gumantung atusan ACL kita ora cocog karo model hak istimewa paling sithik. Aku pungkasane njupuk kabeh ACL sing diikuti pangguna lan nindakake sejenis penelusuran dependensi.

Yen struktur ACL utawa grupmu wis dibangun kanthi struktur hak istimewa paling sithik, piranti sinkronisasi AD/LDAP kanggo Windows bakal makarya apik.

Hubungi tim penjualane lan dheweke bisa nyambungake kowe karo uji coba Enterprise sing luwih dawa. Pesthekna kowe mangerteni watesane kanthi lengkap sadurunge nggawe keputusan. Kita ngalami akeh kasusahan nalika tuwuh nanging saliyane gangguan utawa gangguan ing sisih server, wis dadi lancar banget.


### Bitwarden

Bitwarden nduwe piranti sing apik ing sakubenge (WebUI, CLI, Seluler, Desktop). Bisa dihosting dhewe lan cukup gampang disetel. Dokumentasi cukup apik lan piranti sing disaranake dening PrivacyTools.


### EnvKey

https://www.envkey.com/ yaiku saas. Gampang banget diimplementasikake, diintegrasi, lan diatur.

Fitur:

  * Nglindhungi kunci API lan kredensial.

  * Njaga konfigurasi tetep sinkron ing ngendi-endi.

  * Manajemen konfigurasi lan rahasia sing cerdas lan dienkripsi end-to-end. 

  * Nyegah nuduhake sing ora aman lan sebaran konfigurasi. 

  * Integrasi sajrone sawetara menit.

Kemampuan:

  * Ngatur konfigurasi lan tingkat akses kanggo kabeh aplikasi, lingkungan, lan tim ing siji panggonan.

  * Ngonfigurasi lingkungan pangembangan utawa server apa wae kanthi mung siji variabel lingkungan.

Kaluwihan:

  * Kaca ngarep apik.

  * Proposisi nilai cetha.

  * Aplikasi web apik banget sacara visual.

  * Data conto unggul, upamane Algolia, AWS, Datadog, GitHub, Stripe, lan sapanunggalane.

  * Ngobrol karo pendiri 30 menit babagan perusahaan, UI, lan sapanunggalane. Dane katon ngerti, jujur babagan kaluwihan/kekurangan, lan mitra sing bisa dipercaya.

  * Perusahaan iki intine perusahaan Y Combinator sing khas, kanthi 1 pendiri. Ngunpulake $120K ing 2018-01.

  * Fokus ing nggayuh fitur enterprise, utamane pindhah saka hosting cloud EnvKey menyang on-prem utawa BYOC.

  * Dalan maju potensial miwiti karo EnvKey kanggo gampang digunakake, banjur mengko (utawa paralel) nambah Vault. 


### Confidant saka Lyft

https://lyft.github.io/confidant/

Confidant yaiku layanan manajemen rahasia open source sing nyedhiyakake panyimpenan lan akses rahasia sing ramah pangguna kanthi cara aman, saka para pangembang ing Lyft.

Autentikasi KMS: Confidant ngrampungake masalah endhog-lan-pitik autentikasi kanthi nggunakake AWS KMS lan IAM supaya peran IAM bisa nggawe token autentikasi aman sing bisa diverifikasi dening Confidant. Confidant uga ngatur hibah KMS kanggo peran IAM-mu, sing ngidini peran IAM nggawe token sing bisa digunakake kanggo autentikasi layanan-menyang-layanan, utawa kanggo ngirim pesen enkripsi ing antarane layanan.

Enkripsi at-rest kanggo rahasia sing diversi: Confidant nyimpen rahasia kanthi cara append-only ing DynamoDB, nggawe kunci data KMS unik kanggo saben revisi saben rahasia, nggunakake kriptografi autentikasi simetris Fernet.

Antarmuka web ramah pangguna kanggo ngatur rahasia: Confidant nyedhiyakake antarmuka web AngularJS sing ngidini pangguna pungkasan kanthi gampang ngatur rahasia, pemetaan rahasia menyang layanan lan riwayat owah-owahan.


### Devolutions Password Server

https://server.devolutions.net/

Ngamanake, ngatur, lan ngawasi akses menyang akun lan sesi istimewa.

Vault sandi lengkap sing diamanake banget sing ngidini kowe ngontrol akses menyang akun istimewamu, nalika uga nambah visibilitas jaringan sakabèhé kanggo sysadmin lan menehi pengalaman mulus kanggo pangguna pungkasan.

Fitur: vault sandi organisasi terpusat, vault pribadi khusus pangguna, manajer sandi, injeksi kredensial,
integrasi Active Directory, kontrol akses adhedhasar peran, autentikasi rong faktor, siap enterprise, watesan IP, kemampuan manajemen, generator sandi otomatis, akses aplikasi seluler, riwayat sandi, laporan akses, pangeling email.

  * ndhukung enkripsi data

  * ndhukung macem-macem skema Autentikasi kalebu LDAP, O365, lan pangguna Lokal KARO dhukungan MFA saka pirang-pirang sumber

  * pirang-pirang repositori/vault kanthi kontrol akses rinci kanggo pirang-pirang tim

  * UI Web modern

  * vault kredensial lan sambungan pribadi kanggo kredensial/sambungan pribadi

  * aplikasi seluler kanggo iOS/Android

  * log audit kanggo saben entri, sapa/apa/kapan kanthi pitakon opsional kenapa dheweke ngakses

  * cithakan sing bisa disesuekake (sanajan dheweke ndhukung atusan jinis sambungan sacara asli)

  * akeh banget fitur liyane lan klien tebal Windows/Mac (Remote Desktop Manager) sing bisa kok sinkronake sing ngluwihi pilihan kanthi amba...sambungan sak klik

  * rega ora kurang ala - nganti 15 pangguna yaiku $500 setahun kanggo password server


### Secret Server saka Thycotic

https://thycotic.com/products/secret-server/

Fitur versi on-premise: 

  * Kontrol total marang sistem lan infrastruktur keamanan end-to-end-mu

  * Nyebar piranti lunak ing pusat data on-premise utawa instans virtual private cloud dhewe

  * Nuhoni kewajiban hukum lan regulasi sing mbutuhake kabeh data lan sistem manggon on-premise

Fitur versi cloud:

  * Model software-as-a-service ngidini kowe ndaftar lan miwiti langsung

  * Skalabilitas elastis nalika kowe tuwuh

  * Kontrol lan redundansi sing diwenehake dening Azure kanthi SLA uptime 99,9%

Umpan balik pangguna:

  * Kita biyen nggunakake produk kuwi. Gampang banget dilewati lan aturane mung makarya kanggo wong pinter. Pangguna kesed utawa bodho bisa gampang ngrusak ing area tim. Rega bisa ditawar nalika kowe ngobrol karo dheweke.

  * Kowe bisa nglakokake nganggo SQL express lan kothak Win 7. 

  * Murah.
