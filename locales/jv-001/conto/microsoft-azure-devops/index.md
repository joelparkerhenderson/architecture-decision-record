# Microsoft Azure DevOps

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
  * [Microsoft Devops CI: Petualangan sing Ora Marahi](#microsoft-devops-ci-petualangan-sing-ora-marahi)
  * [Sorotan rembugan Hacker News](#sorotan-rembugan-hacker-news)
  * [Windows Development MVP](#windows-development-mvp)
  * [Ringkesan Edward Thomson (Azure PM)](#ringkesan-edward-thomson-azure-pm)


## Ringkesan


### Masalah

Kita pengin nggunakake devops kanggo mbangun, ngintegrasi, nyebar, lan ngosting proyek-proyek kita. Kita lagi nimbang Microsoft Azure DevOps.

  * Kita pengin pengalaman pangembang cepet lan bisa dipercaya, kanggo setelan devops kayata konfigurasi uga panggunaan terus-terusan kayata wektu build sing cepet.
  
  * Kita pengin nimbang nggunakake Microsoft Azure sakabèhé, kanggo ngosting aplikasi proyek, basis data, lan sapanunggalane.


### Keputusan

Mutusake ora nggunakake Microsoft Azure DevOps.


### Status

Wis diputuske. Terbuka kanggo ditimbang maneh yen/nalika informasi penting anyar teka.


## Rincian


### Anggepan

Kabeh anggepan devops sing umum, kayata ing buku Accelerate.

  * Build sing cepet iku bantuan sing penting. Iki nyepetake daur umpan balik.

  * Kita bisa nuku/nyopot bagean saka vendor alternatif, yaiku kita mbok menawa pengin nggawa server build berkecepatan luwih dhuwur dhewe, nggunakake sistem kontrol versi pilihan dhewe, utawa koordinasi karo server integrasi terus-menerus sing dihosting dhewe.
  
  * Kegunaan sing ringkes iku bantuan sing penting, kanggo pengalaman pangembang, lan sabanjure kanggo bidang sing alus kayata konsistensi, kajelasan, keamanan, lan gampange kurva sinau.

  * Nalika ana sing rusak utawa bermasalah, kita pengin cara sing efektif kanggo nglaporake masalah. Iki utamane penting kanggo masalah sing gegayutan karo keamanan.


### Watesan

Ora ana sing dikenal. Azure nduwe komitmen sing diterbitake kanggo makarya kanthi apik karo piranti njaba.


### Posisi

Kita nimbang nggunakake Microsoft Azure Devops tinimbang AWS sing wis dadi petahana.

Kita nyoba Azure DevOps, Azure Pipelines, Azure Repo, lan nyiyapake server anyar liwat Terraform ing Azure.

Kita nyoba njaluk dhukungan saka perwakilan Microsoft.

Kita ngumpulake informasi saka kanca-kanca ing blog lan Hacker News.


### Argumentasi

Azure DevOps ngiklanake rangkaian tawaran sing apik banget, nanging ora kabukten, ora makarya apik bebarengan, lan dhukungane ala.

Pengalaman langsung kita:

  * Setelan Azure iku kekacauan UI, sawetara tumpang tindih karo akun Microsoft, sawetara ora. Upamane ana mlebu Azure, mlebu Microsoft.com, mlebu Live.com, lan sapanunggalane, lan kabeh dienggo bebarengan.

  * Kita nemoni masalah keamanan cilik nalika setelan, lan ora nemokake penyelesaian. Kita nyoba pirang-pirang cara kanggo nglaporake, marang akeh perwakilan Microsoft, tanpa kasil. Kita kasil nglaporake marang keamanan Microsoft, sing mangsuli ora bakal didandani.

  * Dokumentasi asring salah utawa wis kedaluwarsa. Paling ora sebagian saka iki amarga mesin telusur Microsoft sing ala, lan sebagian amarga SEO sing ora apik.
  
  * Setelan Terraform didokumentasi kanthi apik, lan bisa mlaku. Nanging, dhukungan Terraform ringkih dibandhingake AWS amarga Microsoft lagi mbangun hubungan bisnis karo vendor kanggo nggawe conto setelan Terraform bersambung.

Pengalaman kanca-kanca:

  * Sawise kita nindakake penilaian buta dhewe, kita nggoleki pengalaman kanca-kanca. Sing kita temokake nguatake pengalaman kita.

  * Kanca-kanca nglaporake masalah tambahan karo wektu build, lan masalah karo server build gawa-dhewe. Masalah-masalah iki luwih abot banget tinimbang masalah UI, amarga nindakake build iku tujuan inti saka pipeline build, lan kita ngarepake akeh saben dina.

  * Kita nemokake partisipasi apik banget saka kanca-kanca tim Azure ing area rembugan. Matur nuwun kanggo Microsoft. Kita utamane kesengsem karo Edward Thomson, PM lan koder Azure, amarga partisipasi, kelugasan, lan panjelasan teknise.


### Implikasi

Milih Microsoft Azure DevOps katon bakal luwih larang (~3x) ing wektu lan biaya tinimbang ora milih Azure.


## Gegayutan


### Keputusan gegayutan

Yen kita milih Azure DevOps, ana akeh tawaran gegayutan, kalebu Azure Repo, Azure Pipeline, lan sapanunggalane. Kita pitados yen kita milih Azure Devops, iki mbok menawa nggampangake nggunakake luwih akeh kemampuan Azure, utawa nyulitake nggunakake kemampuan vendor liya.

Kita pitados yen Microsoft nggawe kemajuan gedhe ing pengalaman pangembang, lan kita ndeleng Microsoft nindakake akuisisi gedhe piranti pangembang (upamane GitHub) lan dependensi (upamane Citus).

Yen kita milih Azure DevOps, mbok menawa kita pengin nandheske milih tawaran akuisisi Microsoft, lan mbok menawa uga pengin nyedhaki tawaran akuisisi kanthi luwih ati-ati/penilaian amarga potensi penolakan jaringan, upamane resiko pergantian staf.


### Kabutuhan gegayutan

Kita pengin wektu build cepet banget. Kita nampa mbayar premi dhuwur kanggo iki. Iki amarga kita pengin iterasi cepet banget.

Kita pengin keandalan dhuwur banget. Kita nampa mbayar premi dhuwur kanggo iki. Iki amarga kita nes kasus panggunaan bernilai dhuwur, kalebu transaksi finansial, transaksi rahasia, lan sapanunggalane.

4 KPI devops paling dhuwur kita kalebu mean time to recovery, sing mbutuhake build cepet lan keandalan dhuwur.


### Artefak gegayutan

Kita pengin sistem build ngasilake artefak sing cocog kanggo digunakake ing sistem liyane, kayata Artifactory.


### Prinsip gegayutan

Gampang dibatalake. Kita bisa ngevaluasi Azure DevOps sacara paralel karo AWS sing wis dadi petahana.


## Cathetan


### Microsoft Devops CI: Petualangan sing Ora Marahi

https://toxicbakery.github.io/vsts-devops/microsoft-devops-ci/

Kiriman blog.

"Minangka pangembang piranti lunak, aku ngerti langsung angel banget mbangun produk kualitas kanthi cepet lan murah. Iki seni sing kadhang kita lakoni kanthi bener, lan kadhang malah dadi kaya situs web pamarentah layanan kesehatan jaman Obama. Tingkat kontrol kita marang produk sing diasilake beda-beda, lan nyalahake kegagalan asring tiba marang wong sing salah ing hirarki pengambilan keputusan. Microsoft Azure DevOps (biyen dikenal minangka Visual Studio Team Services), sanajan kanthi niat sing jelas apik, yaiku badai sampurna saka keputusan ala lan eksekusi sing ora apik."


### Sorotan rembugan Hacker News

https://news.ycombinator.com/item?id=18983586

"Kita nggunakake Azure DevOps kanthi ekstensif ing kantorku lan, sawise nggunakake GitHub, Gitlab, solusi self-hosted, Jenkins, TeamCity... Azure DevOps ranking paling buri."

"UI-ne kikuk banget ing ngendi-endi. Sing paling ala kanggoku yaiku pull request. Angel banget makarya karo wong ing pull request. Aku ora bisa nuduhake "siji" masalah tartamtu - kanggo kita iku rusak ing ngendi-endi."

"Azure Devops yaiku sing aku pengin tresnani. UI-ne terus owah, nanging ora ndandani bug dhasar sing wis pirang-pirang taun."

"Piranti-pirantine ora terintegrasi apik, UI-ne alon banget, ora ana tampilan dashboard pull request aktif, build, rilis, lan sapanunggalane kanggo repo favoritku. Wektu Build/Deploy alon banget."

"Kita uga nyoba nggunakake Azure Boards (Work Items, Boards, Backlogs, lan sapanunggalane). Aduh. Iku kekacauan UI saka gagasan-gagasan sing ora nyambung. Tinimbang ngimplementasikake siji perkara kanthi apik, dheweke ngimplementasikake rong lusin perkara kanthi ala."


### Windows Development MVP

Aku MVP Windows Development. Aku rumangsa kudu nanggung sebagian tanggung jawab kanggo ora luwih sora babagan masalah-masalah iki. Nanging aku kudu ngomong, aku kuciwa krungu kowe "kaget" babagan masalah UX. Aku wis ngandhani tim-timmu yen UX-e nggegirisi (upamane wiwit sadurunge peluncuran) lan terus krungu wangsulan "kita ngerti, kita lagi ndandani". Aku bakal miwiti ngresmekake umpan balik lan nyurung liwat saluran, ngenteni kabare. Aku uga lokal (Bellevue), aku seneng teka lan nyoba pipeline aplikasi oss .net/wpf/uwp kita sing relatif prasaja. Aku curiga bakal mbukak mata kita loro.

Sawetara conto:

* Kowe ora bisa nggawe pipeline karo repo git sing ngemot submodule

* Nemokake ora mungkin ngowahi PATH kanggo sawetara piranti khusus

* Pengalaman Pipeline Anyar ora ana logike, pangguna anyar sing ngeklik-ngeklik pungkasane bakal tekan Docs sing salah.


### Ringkesan Edward Thomson (Azure PM)

Aku sing nulis kode sing nggabungake pull request-mu. Program Manager ing Microsoft kanggo Azure DevOps; biyen insinyur piranti lunak ing piranti kontrol versi ing GitHub, Microsoft, SourceGear.

https://www.edwardthomson.com/

Co-maintainer libgit2. https://libgit2.github.io

Co-host All Things Git, Podcast babagan Git. https://www.allthingsgit.com/

Kurator Developer Tools Weekly, newsletter babagan piranti pangembangan. https://developertoolsweekly.com/
