# Cathetan keputusan arsitektur (ADR)

Cathetan keputusan arsitektur (ADR) yaiku dokumen sing nyathet keputusan arsitektur penting bebarengan karo konteks lan akibate.

> [!IMPORTANT]
> Lakokna uji tuntas dhewe marang sumber daya iki sadurunge nggunakake ing sistem kritis apa wae.

Isi:

- [Apa iku cathetan keputusan arsitektur?](#apa-iku-cathetan-keputusan-arsitektur)
- [Carane miwiti nggunakake ADR](#carane-miwiti-nggunakake-adr)
- [Carane miwiti nggunakake ADR nganggo piranti](#carane-miwiti-nggunakake-adr-nganggo-piranti)
- [Carane miwiti nggunakake ADR nganggo git](#carane-miwiti-nggunakake-adr-nganggo-git)
- [Skill Claude Code kanggo ADR](#skill-claude-code-kanggo-adr)
- [Aturan jeneng berkas kanggo ADR](#aturan-jeneng-berkas-kanggo-adr)
- [Saran kanggo nulis ADR sing apik](#saran-kanggo-nulis-adr-sing-apik)
- [Cithakan conto ADR](#cithakan-conto-adr)
- [Pitutur gotong royong tim kanggo ADR](#pitutur-gotong-royong-tim-kanggo-adr)
- [Pitakon gotong royong tim kanggo ADR](#pitakon-gotong-royong-tim-kanggo-adr)
- [Konsep langkah sabanjure kanggo ADR](#konsep-langkah-sabanjure-kanggo-adr)
- [Diagram, tampilan, lan sudut pandang arsitektur](#diagram-tampilan-lan-sudut-pandang-arsitektur)
- [Fungsi kebugaran kanggo keputusan minangka kode](#fungsi-kebugaran-kanggo-keputusan-minangka-kode)
- [Pagar pengaman keputusan kanggo pull request](#pagar-pengaman-keputusan-kanggo-pull-request)
- [Kanggo informasi luwih akeh](#kanggo-informasi-luwih-akeh)

Cithakan:

- [Cithakan cathetan keputusan saka Jeff Tyree lan Art Akerman](cithakan/cithakan-cathetan-keputusan-saka-jeff-tyree-lan-art-akerman/)
- [Cithakan cathetan keputusan saka Michael Nygard](cithakan/cithakan-cathetan-keputusan-saka-michael-nygard/)
- [Cithakan cathetan keputusan saka EdgeX](cithakan/cithakan-cathetan-keputusan-saka-edgex/)
- [Cithakan cathetan keputusan saka arc42](cithakan/cithakan-cathetan-keputusan-saka-arc42/)
- [Cithakan cathetan keputusan kanggo pola Alexandrian](cithakan/cithakan-cathetan-keputusan-kanggo-pola-alexandrian/)
- [Cithakan cathetan keputusan kanggo kasus bisnis](cithakan/cithakan-cathetan-keputusan-kanggo-kasus-bisnis/)
- [Cithakan cathetan keputusan saka Proyek MADR](cithakan/cithakan-cathetan-keputusan-saka-proyek-madr/)
- [Cithakan cathetan keputusan nganggo Planguage](cithakan/cithakan-cathetan-keputusan-nganggo-planguage/)
- [Cithakan cathetan keputusan saka Paulo Merson](https://github.com/pmerson/ADR-template)
- [Cithakan cathetan keputusan saka Olaf Zimmermann](https://medium.com/olzzio/y-statements-10eb07b5a177)
- [Cithakan cathetan keputusan saka Gareth Morgan](cithakan/cithakan-cathetan-keputusan-saka-gareth-morgan/)
- [Cithakan cathetan keputusan saka GIG Cymru NHS Wales](cithakan/cithakan-cathetan-keputusan-saka-gig-cymru-nhs-wales/)
- [Cithakan cathetan keputusan kanggo Keputusan Teknis Penting (ITD) saka Ignacio Larrañaga](cithakan/cithakan-cathetan-keputusan-kanggo-keputusan-teknis-penting/)

Conto:

- [Framework CSS](conto/framework-css/)
- [Konfigurasi variabel lingkungan](conto/konfigurasi-variabel-lingkungan/)
- [Metrik, monitor, pangeling](conto/metrik-monitor-pangeling/)
- [Microsoft Azure DevOps](conto/microsoft-azure-devops/)
- [Monorepo utawa multirepo](conto/monorepo-utawa-multirepo/)
- [Basa-basa pamrograman](conto/basa-basa-pamrograman/)
- [Panyimpenan rahasia](conto/panyimpenan-rahasia/)
- [Format cap wektu](conto/format-cap-wektu/)
- [Isih akeh liyane...](conto/)

## Apa iku cathetan keputusan arsitektur?

**Cathetan keputusan arsitektur** (ADR) yaiku dokumen sing nyathet sawijining keputusan arsitektur penting bebarengan karo konteks lan akibat-akibate.

**Keputusan arsitektur** (AD) yaiku pilihan desain piranti lunak sing nanggapi sawijining kabutuhan penting.

**Log keputusan arsitektur** (ADL) yaiku kumpulan kabeh ADR sing digawe lan dijaga kanggo sawijining proyek (utawa organisasi) tartamtu.

**Kabutuhan penting kanggo arsitektur** (ASR) yaiku kabutuhan sing nduwe pengaruh sing bisa diukur marang arsitektur sistem piranti lunak.

Kabeh iku mlebu ing topik **manajemen kawruh arsitektur** (AKM).

Tujuane dokumen iki yaiku menehi ringkesan cepet babagan ADR, carane nggawe, lan ing ngendi golek informasi luwih akeh.

Singkatan:

  * **AD**: keputusan arsitektur

  * **ADL**: log keputusan arsitektur

  * **ADR**: cathetan keputusan arsitektur

  * **AKM**: manajemen kawruh arsitektur

  * **ASR**: kabutuhan penting kanggo arsitektur

## Carane miwiti nggunakake ADR

Kanggo miwiti nggunakake ADR, rembugan karo kanca-kanca timmu babagan bidang-bidang iki.

Identifikasi keputusan:

  * Sepira urgen lan sepira penting AD kuwi?

  * Apa kudu diputuske saiki, utawa bisa ngenteni nganti luwih akeh sing dingerteni?

  * Pengalaman pribadi lan bebarengan, uga metode lan praktik desain sing diakoni, bisa mbiyantu identifikasi keputusan.

  * Luwih becik njaga dhaptar tugas keputusan sing nglengkapi dhaptar tugas produk.

Nggawe keputusan:

  * Ana akeh teknik nggawe keputusan, sing umum lan sing khusus arsitektur piranti lunak, upamane pemetaan dialog.

  * Nggawe keputusan sacara kelompok iku topik riset sing aktif.

Nglakokake lan negakake keputusan:

  * AD dipigunakake ing desain piranti lunak; mula kudu dikabarake marang, lan ditampa dening, para pemangku kepentingan sistem sing mbiayai, ngembangake, lan ngoperasekake sistem kuwi.

  * Gaya penulisan kode sing arsitekture katon cetha lan review kode sing fokus ing perkara lan keputusan arsitektur iku rong praktik sing gegayutan.

  * AD uga kudu dipikirake (maneh) nalika modernisasi sistem piranti lunak ing evolusi piranti lunak.

Nuduhake keputusan (opsional):

  * Akeh AD sing bola-bali ing sawetara proyek.

  * Mula, pengalaman karo keputusan jaman biyen, sing apik lan sing ala, bisa dadi aset sing aji lan bisa dipigunakake maneh nalika nggunakake strategi manajemen kawruh sing cetha.

Dokumentasi keputusan:

  * Ana akeh cithakan lan piranti kanggo nyathet keputusan.

  * Delengen komunitas agile, upamane ADR saka M. Nygard.

  * Delengen proses rekayasa piranti lunak lan desain arsitektur tradisional, upamane tata letak tabel sing disaranake dening IBM UMF lan dening Tyree lan Akerman saka CapitalOne.

Kanggo informasi luwih akeh:

  * Langkah-langkah ing ndhuwur dijupuk saka entri Wikipedia babagan [Architectural Decision](https://en.wikipedia.org/wiki/Architectural_decision)

## Carane miwiti nggunakake ADR nganggo piranti

- [MySpec](https://myspec.dev) — Platform spesifikasi lan keputusan arsitektur otomatis sing nata konstitusi proyek, arsitektur teknis, lan ADR dadi Markdown sing rapi lan disuguhake liwat MCP.

Kowe bisa miwiti nggunakake ADR nganggo piranti kanthi cara apa wae sing dikarepake.

Upamane:

  * Yen kowe seneng nggunakake Google Drive lan nyunting online, kowe bisa nggawe Google Doc, utawa Google Sheet.

  * Yen kowe seneng nggunakake kontrol versi kode sumber, kayata git, kowe bisa nggawe siji berkas kanggo saben ADR.

  * Yen kowe seneng nggunakake piranti perencanaan proyek, kayata Atlassian Jira, kowe bisa nggunakake pelacak perencanaan piranti kuwi.

  * Yen kowe seneng nggunakake wiki, kayata MediaWiki, kowe bisa nggawe wiki ADR.

## Carane miwiti nggunakake ADR nganggo git

Yen kowe seneng nggunakake kontrol versi git, mangkene carane kita seneng miwiti nggunakake ADR nganggo git kanggo proyek piranti lunak biasa sing nduwe kode sumber.

Gawe direktori kanggo berkas ADR:

```sh
$ mkdir adr
```

Kanggo saben ADR, gawe berkas teks, kayata `choose-database.md`:

```sh
$ vi choose-database.md
```

Tulisen apa wae sing dikarepake ing ADR. Deleng cithakan-cithakan ing repositori iki kanggo gagasan.

Commit ADR menyang repo git-mu.

## Skill Claude Code kanggo ADR

Repositori iki nyedhiyakake rong skill [Claude Code](https://claude.com/claude-code) ing [`skills/`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/), supaya agen pamrograman AI bisa nulis lan njaga ADR kaya sing disaranake proyek iki:

- [`architecture-decision-record-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-skill/) — kanggo panggunaan umum, kanggo sapa wae sing nulis ADR ing proyek apa wae. Mbiyantu mutusake apa sawijining keputusan butuh ADR, nyiyapake direktori `adr/` utawa `decisions/`, nemtokake jeneng berkas, milih cithakan saka sewelas kerangka sing kalebu, lan nulis bagean Konteks/Keputusan/Akibat kanthi apik.

- [`architecture-decision-record-maintainer-skill`](https://github.com/architecture-decision-record/architecture-decision-record/tree/main/skills/architecture-decision-record-maintainer-skill/) — khusus kanggo para pangopèn repositori iki. Nyathet tata letak repositori, konvensi pangiriman README/locales, lan langkah-langkah persis kanggo nambah cithakan, conto, utawa link piranti anyar.

Kanggo nggunakake skill, salinen folder-e menyang `.claude/skills/` ing oyod repositori sing lagi kok garap (utawa menyang `~/.claude/skills/` supaya kasedhiya ing saben proyek), banjur njaluka Claude Code nulis utawa mriksa ADR.

## Aturan jeneng berkas kanggo ADR

Yen kowe milih nggawe ADR nganggo berkas teks biasa, kowe mbok menawa pengin nentokake aturan jeneng berkas ADR dhewe.

Kita luwih seneng nggunakake aturan jeneng berkas sing nduwe format tartamtu.

Conto:

  * choose-database.md

  * format-timestamps.md

  * manage-passwords.md

  * handle-exceptions.md

Aturan jeneng berkas kita:

  * Jeneng nggunakake frasa kriya imperatif wektu saiki. Iki mbiyantu keterbacaan lan cocog karo format pesen commit kita.

  * Jeneng nggunakake huruf cilik lan garis-sambung (padha karo repo iki). Iki imbangan antarane keterbacaan lan kegunaan sistem.

  * Ekstensine yaiku markdown. Iki bisa migunani kanggo format sing gampang.

## Saran kanggo nulis ADR sing apik

Ciri-ciri ADR sing apik:

* Alasan: Jlentrehake alasan nglakokake AD tartamtu kuwi. Iki bisa kalebu konteks (deleng ing ngisor), kaluwihan lan kekurangan saka macem-macem pilihan, perbandingan fitur, rembugan biaya/manfaat, lan liya-liyane.

* Spesifik: Saben ADR kudu babagan siji AD, ora pirang-pirang AD.

* Cap wektu: Tandhani kapan saben bab ing ADR ditulis. Iki penting banget kanggo aspek sing bisa owah saka wektu, kayata biaya, jadwal, skala, lan sapanunggalane.

* Ora owah: Aja ngowahi informasi sing wis ana ing ADR. Luwih becik, ganti ADR kanthi nambah informasi anyar, utawa gantinen ADR kanthi nggawe ADR anyar.

Ciri-ciri bagean "Konteks" sing apik ing ADR:

* Jlentrehake kahanan organisasimu lan prioritas bisnis.

* Lebokna alasan lan pertimbangan adhedhasar susunan sosial lan katrampilan tim-timmu.

* Lebokna kaluwihan lan kekurangan sing gegayutan, lan gambarake kanthi istilah sing cocog karo kabutuhan lan tujuanmu.

Ciri-ciri bagean "Akibat" sing apik ing ADR:

* Jlentrehake apa sing ana sawise keputusan digawe. Iki bisa kalebu efek, asil, output, tindak lanjut, lan liya-liyane.

* Lebokna informasi babagan ADR-ADR sabanjure. Pancen umum yen siji ADR nuwuhake kabutuhan ADR liyane, kayata nalika siji ADR nggawe pilihan gedhe sing nyakup, sing banjur nuwuhake kabutuhan keputusan-keputusan sing luwih cilik.

* Lebokna proses review sawise tindakan. Biasane tim mriksa saben ADR sewulan sabanjure, kanggo mbandhingake informasi ADR karo apa sing kedadeyan ing praktik nyata, supaya sinau lan berkembang.

ADR anyar bisa nggantekake ADR sadurunge:

* Nalika AD digawe sing nggantekake utawa mbatalake ADR sadurunge, ADR anyar kudu digawe

## Cithakan conto ADR

Cithakan conto ADR sing wis kita kumpulake saka internet:

- [Cithakan ADR saka Michael Nygard](cithakan/cithakan-cathetan-keputusan-saka-michael-nygard/) (prasaja lan populer)

- [Cithakan ADR saka Jeff Tyree lan Art Akerman](cithakan/cithakan-cathetan-keputusan-saka-jeff-tyree-lan-art-akerman/) (luwih canggih)

- [Cithakan ADR kanggo pola Alexandrian](cithakan/cithakan-cathetan-keputusan-kanggo-pola-alexandrian/) (prasaja kanthi rincian konteks)

- [Cithakan ADR kanggo kasus bisnis](cithakan/cithakan-cathetan-keputusan-kanggo-kasus-bisnis/) (luwih berorientasi MBA, kanthi biaya, SWOT, lan panemu liyane)

- [Cithakan ADR saka proyek Markdown Any Decision Records (MADR)](cithakan/cithakan-cathetan-keputusan-saka-proyek-madr/) (versi prasaja lan versi rinci; sing kapindho nandheske pilihan lan kaluwihan-kekurangane)

- [Cithakan ADR nganggo Planguage](cithakan/cithakan-cathetan-keputusan-nganggo-planguage/) (luwih berorientasi jaminan kualitas)

- [Cithakan kanggo Keputusan Teknis Penting (ITD) saka Ignacio Larrañaga](cithakan/cithakan-cathetan-keputusan-kanggo-keputusan-teknis-penting/) (ramping lan keputusan-dhisik, dioptimalake kanggo tinjauan eksekutif sing cepet)

## Pitutur gotong royong tim kanggo ADR

Yen kowe lagi nimbang nggunakake cathetan keputusan karo timmu, iki pitutur sing wis kita sinaoni saka makarya karo akeh tim.

Kowe duwe kesempatan mimpin kanca-kanca timmu, kanthi rembugan bareng babagan "kenapa", tinimbang meksa "apa". Upamane, cathetan keputusan iku cara supaya tim bisa mikir luwih pinter lan komunikasi luwih apik; cathetan keputusan ora aji yen mung dadi syarat urusan kertas sing dipeksa sawise kedadeyan.

Sawetara tim luwih seneng jeneng "keputusan" tinimbang singkatan "ADR". Nalika sawetara tim nggunakake jeneng direktori "decisions", kaya lampu murup, lan tim wiwit nglebokake informasi luwih akeh ing direktori kuwi, kayata keputusan vendor, keputusan perencanaan, keputusan jadwal, lan sapanunggalane. Kabeh jinis informasi iki bisa nggunakake cithakan sing padha. Kita duga manungsa sinau luwih cepet nganggo tembung ("keputusan") tinimbang singkatan ("ADR"), manungsa luwih semangat nulis dokumen sing lagi dikerjakake yen tembung "cathetan" dicopot, lan uga sawetara pangembang lan sawetara manajer ora seneng tembung "arsitektur".

Ing teori, ora owah iku ideal. Ing praktik, bisa owah luwih cocog kanggo tim-tim kita. Kita nglebokake informasi anyar ing ADR sing wis ana, nganggo cap tanggal, lan cathetan yen informasi kuwi teka sawise keputusan. Pendekatan iki nuwuhake "dokumen urip" sing bisa dianyari kabeh. Pembaruan sing umum yaiku nalika kita entuk informasi amarga anggota tim anyar, tawaran anyar, asil nyata saka panggunaan kita, utawa owah-owahan pihak katelu sawise keputusan kayata kemampuan vendor, rencana rega, perjanjian lisensi, lan sapanunggalane.

## Pitakon gotong royong tim kanggo ADR

### Sapa sing bisa nggawe ADR?

Pikirake bidang kayata wong tartamtu, peran tartamtu, tim tartamtu, utawa departemen tartamtu; uga pikirake apa ana wong, peran, tim, utawa departemen sing bisa mesen ADR, tegese njaluk ADR sing bakal ditulis wong liya.

Conto wangsulan: Sapa wae ing organisasi kita sing wis maca kaca README cathetan keputusan arsitektur bisa ngusulake ADR, tegese wong kuwi bisa miwiti nulis lan nuduhake menyang tim.

### Apa sing mbenerake nggawe ADR?

Pikirake bidang kayata cara kerja tim ing organisasimu, struktur sistem piranti lunakmu, koordinasi antar tim, kemampuan perawatan jangka dawa, antarmuka njaba, sapa sing dikarepake entuk manfaat, lan sapanunggalane.

Conto wangsulan: Kita pengin nggawe ADR nalika kita pengin pangembang mbesuk ngerti "kenapa" saka apa sing lagi kita lakoni.

### Apa sing mbenerake ora nggawe ADR?

Pikirake keputusan sing dudu babagan arsitektur, utawa cilik banget kayata resikone minimal utawa mandhiri utawa mung siji pangembang, utawa wis kebak diliputi ing papan liya kayata dening standar utawa kabijakan utawa dokumentasi, utawa sauntara kayata solusi sauntara utawa bukti konsep utawa eksperimen.

Conto wangsulan: Kita pengin nglewati ADR nalika keputusan winates ing lingkup lan wektu lan resiko lan biaya, utawa wis diliputi ing papan liya.

### Kepriye daur urip ADR?

Pikirake bidang kayata proses nggawe, proses riset, proses nggawe keputusan, proses implementasi, lan proses pensiun. Pikirake carane nglacak daur urip ADR saka wektu, kayata carane mindhahake ADR saka siji kahanan menyang kahanan sabanjure, lan uga carane ngabarake iki marang pemangku kepentingan.

Conto wangsulan: Kita pengin ADR nduwe lima tahap daur urip: Miwiti → Riset → Evaluasi → Implementasi → Pangopènan → Pensiun.

### Apa kriteria kanggo langkah daur urip ADR?

Pikirake bidang kayata kriteria panrima kanggo ADR, tegese kepriye kowe ngerti ADR wis cukup apik kanggo maju saka siji langkah daur urip menyang langkah sabanjure? Apa masalahe wis diterangake kanthi cetha? Apa alternatif wis dipikirake? Apa kompromi wis dingerteni lan didokumentasi cukup apik?
Apa kabeh konteks sing gegayutan wis ana? Apa kabeh pemangku kepentingan sing gegayutan melu? Apa kabeh umpan balik wis dilebokake?

Conto wangsulan: Kita pengin ADR dipilih dening pemangku kepentingan nalika tim aktif wis 1) rampung risete, 2) rampung evaluasine, 3) nerbitake usulan ADR marang pemangku kepentingan kanthi panjaluk komentar lan wektu sak minggu, 4) kabeh komentar pemangku kepentingan wis dilebokake lan ditanggapi.

### Peran lan tanggung jawab apa sing berinteraksi karo ADR?

Pikirake peran kayata pengusul, peneliti, evaluator, peninjau, panyetuju, pangopèn, lan sapanunggalane. Pikirake tanggung jawab kayata komunikasi karo pemangku kepentingan, mesthekake pangarep-arep kaleksanan, nuduhake ing situs web utawa intranet, lan mriksa pagaweyan kanthi periodik lan utamane nalika ana owah-owahan sing gegayutan.

Conto wangsulan: Kita pengin saben ADR tansah nduwe wong kontak utama, wong kontak kapindho, lan tim sing tanggung jawab; iki tanggung jawab kanggo komunikasi, publikasi, pangopènan, review periodik paling ora setaun sapisan, lan pensiun pungkasan yen perlu.

### Kepriye tata kelola berinteraksi karo ADR?

Pikirake bidang kayata cara kerja organisasimu, kabutuhan kepatuhan khusus kayata aspek hukum utawa sumber daya manungsa, kepriye kowe pengin nangani konsensus lawan konflik lawan eskalasi. Apa ana bidang utawa wong utawa tim sing bisa nduwe pengaruh luwih akeh tinimbang liyane babagan ADR, kayata bisa nyetujoni, utawa milih, utawa veto?

Conto wangsulan: Tata kelola ADR miturut urutan prioritas iki: CEO, CTO, CLO, tim sing nglakokake ADR, para ahli ing tim sing paling ngerti babagan AD. Ora ana wong liya sing nduwe tata kelola kajaba diterangake ing ADR.

### Prinsip apa sing berinteraksi karo ADR?

Pikirake cara kerja organisasimu sing kalebu obah cepet lawan alon, konsensus keputusan lawan konflik keputusan, preferensi resiko lawan preferensi keamanan, rembugan umum lawan rembugan pribadi, lan sapanunggalane.

Conto wangsulan: Kita nggunakake prinsip kepemimpinan condong tumindak, ora setuju-nanging-manut, perkiraan 70% wis cukup kanggo keputusan sing gampang dibatalake lan gampang diisolasi, lan cara kerja umum kajaba informasi rahasia sing diterangake ing perjanjian kerahasiaan organisasi kita.

## Konsep langkah sabanjure kanggo ADR

[Arc42](https://arc42.org/) mangsuli rong pitakon kanthi cara pragmatis lan bisa disesuekake karo kabutuhan khususmu. Apa sing kudu kok dokumentasi/komunikasikake babagan arsitekturmu? Kepriye carane dokumentasi/komunikasi? Arc42 kalebu cathetan keputusan arsitektur plus pandhuan babagan tujuan, watesan, konteks, kualitas, resiko, lan liya-liyane.

[Model C4](https://c4model.com/) yaiku pendekatan gampang disinaoni lan ramah pangembang kanggo nggambar diagram arsitektur piranti lunak. C4 yaiku sakumpulan diagram hirarkis kanggo konteks, kontainer, komponen, kode, plus diagram pendukung kanggo lanskap sistem, dinamis, lan deployment.

## Diagram, tampilan, lan sudut pandang arsitektur

Diagram arsitektur diarani "tampilan arsitektur".

"Tampilan arsitektur" yaiku instans saka "sudut pandang arsitektur".

"Sudut pandang arsitektur" nduwe pamirsa tartamtu kanthi kuwatir tartamtu ing pikiran.

Conto sudut pandang arsitektur, conto tampilan, lan conto diagram:

- Kapabilitas Bisnis (Business Capabilities)

- Proses Bisnis tingkat dhuwur

- [Value Streams](https://en.wikipedia.org/wiki/Value_stream)

- Fungsi Piranti Lunak sing dipetakake menyang komponen aplikasi

- Diagram Konteks [Model C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- Diagram Kontainer [Model C4](https://en.wikipedia.org/wiki/C4_model) (TO-BE / AS-IS)

- [Diagram Entity-relationship](https://en.wikipedia.org/w/index.php?title=Entity_relationship_diagram) (ERD) kanggo mapake entitas data menyang komponen aplikasi

- [Diagram Urutan (Sequence Diagrams)](https://en.wikipedia.org/wiki/Sequence_diagram) kanggo njlentrehake alur fungsional ing njero sistem lan kanggo integrasi

- Diagram [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) kanggo njlentrehake alur data ing komponen aplikasi

- Diagram [Business Process Model and Notation](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) (BPMN) kanggo njlentrehake proses bisnis / skenario pangguna

- Diagram [Identity and Access Management](https://en.wikipedia.org/wiki/Identity_and_access_management) (IAM)

- Diagram [Role-Based Access Control](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) kanthi peran saben komponen aplikasi

- Diagram [Attribute-Based Access Control](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) kanthi atribut saben komponen aplikasi

- Diagram privasi

Diagram gegayutan:

- Diagram Kasus Panggunaan (Use Case Diagram) nuduhake kasus panggunaan marang manajemen/pelanggan, sing ndhisiki kabutuhan, sing ndhisiki arsitektur piranti lunak.

- Diagram Deployment (Deployment Diagram) nuduhake hardware/komputer fisik ing ngendi komponen piranti lunak disebar.
- Diagram Alur Data (Data Flow Diagram) nuduhake carane data obah liwat sistem lan diowahi.
- Diagram Urutan (Sequence Diagram) digunakake kanggo nuduhake carane protokol kayata HTTP makarya ing sumbu wektu.

- Diagram Aktivitas (Activity Diagram) nggambarake alur kerja aktivitas sing ditindakake sistem piranti lunak, kaya NPC AI.

## Fungsi kebugaran kanggo keputusan minangka kode

Fungsi kebugaran yaiku pamriksan otomatis lan objektif, ditulis nganggo kode pamrograman, sing mesthekake yen keputusan tetep dilakoni.

- Fungsi kebugaran ndadekake keputusan bisa dites lan dijamin.

- Fungsi kebugaran kanggo keputusan bisa mbiyantu banget jaminan kualitas, proses regulasi, lan tujuan tata kelola.

### Kepriye fungsi kebugaran nyambung karo keputusan

Cathetan keputusan nyathet keputusan, dene fungsi kebugaran njamin keputusan.

- Conto keputusan: Kita nggunakake event sourcing kanggo kabutuhan audit.

- Conto fungsi kebugaran: Kita nggunakake server integrasi terus-menerus kanggo nes yen kabeh owah-owahan status kudu ngasilake event.

### Kenapa fungsi kebugaran mbiyantu keputusan

Pangukuran objektif: Fungsi kebugaran lulus utawa gagal, dadi pagaweyan katon lan cetha.

Panggunaan terus-terusan: Fungsi kebugaran yaiku aturan urip sampeyan, dilakokake ing saben commit lan build.

Kapercayan kanggo refaktor: Fungsi kebugaran otomatis nyekel kesalahan aturan keputusan.

Tata kelola sing bisa mundhak: Fungsi kebugaran njamin standar tanpa nggawe bottleneck.

### Apa fungsi kebugaran bisa nggunakake AI?

Fungsi kebugaran bisa nggunakake LLM AI kanggo keputusan kanthi takon babagan pagaweyanmu, kayata rencana, kode, skema, API, lan liya-liyane:

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

[ArchUnit](https://www.archunit.org/): priksa aturan arsitektur kode Java nganggo framework uji unit Java biasa apa wae.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): priksa aturan arsitektur kode TypeScript lan kode JavaScript nganggo Jest, Vitest, Jasmine, lan liya-liyane.

## Pagar pengaman keputusan kanggo pull request

[Decision Guardian](https://github.com/DecispherHQ/decision-guardian)
kanthi otomatis nampilake cathetan keputusan sing bener ing wektu sing bener — nalika
pangembang lagi aktif ngowahi kode sing dicakup keputusan kuwi. Tinimbang
ngarep-arep pangembang maca folder dokumen sadurunge merge, konteks sing gegayutan
katon langsung ing pull request.

Iki makarya kanggo saben jinis cathetan keputusan: keputusan arsitektur, keputusan
data, keputusan kepatuhan, keputusan klinis lan medis, keputusan keamanan, lan liya-liyane.

Makarya karo sistem CI apa wae (GitLab, Jenkins, CircleCI) lan minangka pre-commit hook.
Open source. Lisensi MIT.

[ADR Guard](https://github.com/chohan-sarmad-ali/delivery-gates) yaiku GitHub
Action sing nggagalake pull request nalika dalan kode sing diawasi owah tanpa
cathetan keputusan arsitektur ditambah utawa dianyari. Pangecualian iku eksplisit: baris
`ADR-Exempt:` kanthi alesan nglewati gerbang lan ditulis ing ringkesan job.
Netral marang cithakan, tanpa dependensi. Open source. Lisensi MIT.

## Kanggo informasi luwih akeh

Bubuka:

- [Architectural decision (wikipedia.org)](https://wikipedia.org/wiki/Architectural_decision)

- [Architecturally significant requirements (wikipedia.org)](https://wikipedia.org/wiki/Architecturally_significant_requirements)

Cithakan:

- [Documenting architecture decisions - Michael Nygard (thinkrelevance.com)](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)

- [Markdown Architectural Decision Records (adr.github.io)](https://adr.github.io/madr/)

- [Template for documenting architecture alternatives and decisions (stackoverflow.com)](http://stackoverflow.com/questions/7104735/template-for-documenting-architecture-alternatives-and-decisions)

Luwih jero:

- [ADMentor XML project (github.com)](https://github.com/IFS-HSR/ADMentor)

- [Architectural Decision Guidance across Projects: Problem Space Modeling, Decision Backlog Management and Cloud Computing Knowledge (ifs.hsr.ch)](https://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf)

- [The Decision View's Role in Software Architecture Practice (computer.org)](https://www.computer.org/csdl/mags/so/2009/02/mso2009020036-abs.html)

- [Documenting Software Architectures: Views and Beyond (resources.sei.cmu.edu)](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386)

- [Architecture Decisions: Demystifying Architecture (utdallas.edu)](https://www.utdallas.edu/~chung/SA/zz-Impreso-architecture_decisions-tyree-05.pdf)

- [ThoughtWorks Technology Radar: Lightweight Architecture Decision Records (thoughtworks.com)](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

- [A Skeptic’s Guide to Software Architecture Decisions (infoq.com)](https://www.infoq.com/articles/architecture-skeptics-guide/)

- [Architectural Decisions — The Making Of](https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html)

- [Architectural Retrospectives: the Key to Getting Better at Architecting](https://www.infoq.com/articles/architectural-retrospectives/)

- [Software Architecture Monday with Mark Richards](https://developertoarchitect.com/lessons/) - pelajaran arsitektur piranti lunak bulanan gratis

- [Solution Architecture Decisions - By Gareth Morgan](https://www.linkedin.com/pulse/solution-architecture-decisions-gareth-morgan-0r5xe/)

- ["Keep the Why: Code Becomes Legacy When Nobody Remembers Why"](https://blog.technopathy.club/keep-the-why-code-becomes-legacy-when-nobody-remembers-why)

Piranti:

- [Command-line tools for working with Architecture Decision Records](https://github.com/npryce/adr-tools)

- [Command line tools with python - by Victor Sluiter](https://bitbucket.org/tinkerer_/adr-tools-python/src/master/)

- [Architectural Design Decision Support Framework (ADvISE)](https://swa.univie.ac.at/Software_Architecture/research-projects/architectural-design-decision-support-framework-advise/)

- [Decision Guardian](https://github.com/DecispherHQ/decision-guardian)

- [Mneme HQ - ADR enforcement for AI coding agents](https://github.com/TheoV823/mneme)

- [Keep the Why - a repo-native convention and agent skill that continuously captures, or retrospectively recovers, the reasoning behind a codebase](https://github.com/oliver-zehentleitner/keep-the-why)

- [ADR Guard - GitHub Action that fails a pull request changing watched code without an architecture decision record](https://github.com/chohan-sarmad-ali/delivery-gates)

- [kgai - append-only decision log for AI coding agents, a machine-readable companion to ADR files](https://github.com/kgaidev/kgai)

Pandhuan khusus perusahaan:

- [Amazon: AWS Prescriptive Guidance: ADR Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)

- [GitHub: ADR GitHub organization](https://adr.github.io/)

- [RedHat: Why you should use ADRs](https://www.redhat.com/architect/architecture-decision-records)

Conto:

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

Deleng uga:

- REMAP (Representation and Maintenance of Process Knowledge)

- DRL (Decision Representation Language)

- IBIS (Issue-Based Information System)

- QOC (Questions, Options, and Criteria)

- IBM’s e-Business Reference Architecture Framework

- [Decision Reasoning Format (DRF)](https://github.com/reasoning-formats/reasoning-formats) - Format YAML/JSON netral vendor lan bisa diwaca mesin kanggo makili keputusan kanthi nalar eksplisit, anggepan, kahanan kognitif, lan kompromi. Nglengkapi ADR kanthi nambah nalar terstruktur lan bisa divalidasi menyang dokumentasi keputusan.
