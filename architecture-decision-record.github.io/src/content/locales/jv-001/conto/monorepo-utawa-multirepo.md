# Monorepo utawa multirepo

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


## Ringkesan


### Masalah

Proyek kita nglibatake pangembangan telung kategori utama piranti lunak:

  * GUI front-end
  * Layanan middleware
  * Server back-end

Nalika ngembangake, sistem kontrol versi (VCS) manajemen kode sumber (SCM) kita yaiku git.

Kita kudu milih carane nggunakake git kanggo ngatur kode kita.

Pilihan tingkat paling dhuwur yaiku ngatur minangka "monorepo" utawa "polyrepo" utawa "hibrida":

  * Monorepo tegese kita nglebokake kabeh bagean ing siji repo gedhe
  * Polyrepo tegese kita nglebokake saben bagean ing repo dhewe-dhewe
  * Hibrida tegese campuran monorepo lan polyrepo

Kanggo informasi luwih akeh deleng https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Keputusan

Monorepo nalika organisasi/tim/proyek relatif cilik, lan iterasi cepet luwih dhuwur prioritase tinimbang njaga stabilitas.

Polyrepo nalika organisasi/tim/proyek relatif gedhe, lan njaga stabilitas luwih dhuwur prioritase tinimbang iterasi cepet.


### Status

Wis diputuske. Terbuka kanggo ditimbang maneh yen/nalika piranti anyar kanggo ngatur monorepo lan/utawa polyrepo kasedhiya.


## Rincian


### Anggepan

Kabeh kode sing kita kembangake yaiku kanggo tawaran siji organisasi, dudu kanggo masarakat umum. Yaiku Broker-Dealer ora ngarahake nduwe pangembang sukarelawan masarakat umum.


### Watesan

Watesan didokumentasi kanthi apik ing https://github.com/joelparkerhenderson/monorepo-vs-polyrepo


### Posisi

Kita nimbang monorepo kaya gaya Google, Facebook, lan sapanunggalane. Kita nganggep masalah skala monorepo isih adoh ing mbesuk, mula kita bakal bisa nggunakake praktik sing padha karo Google lan Facebook, nalika kita mbutuhake.

Kita nimbang polyrepo kaya gaya proyek open source Git sing khas, kayata Google Android, Facebook React, lan sapanunggalane. Kita nganggep iki pilihan paling apik kanggo partisipasi masarakat umum (upamane sapa wae ing donya bisa makarya ing kode) lan kasedhiyan individu (upamane proyek digunakake dhewekan, tanpa bagean liya).


### Argumentasi

Nalika organisasi/tim/proyek relatif cilik, kita milih monorepo, amarga iterasi cepet prioritase luwih dhuwur banget tinimbang njaga stabilitas

Nalika organisasi/tim/proyek relatif gedhe, kita milih polyrepo, amarga njaga stabilitas prioritase luwih dhuwur banget tinimbang iterasi cepet.


### Implikasi

Yen wis ana pipeline kanggo CI+CD, mbok menawa kita kudu nyesuekake kanggo nes pirang-pirang proyek ing siji repo.

CI+CD bisa mbutuhake wektu luwih akeh kanggo build lengkap monorepo, amarga CI+CD bisa mbangun kabeh proyek ing monorepo.

Yen organisasi/tim/proyek tuwuh, monorepo bakal nduwe masalah skala.

Masalah skala monorepo bisa ndadekake transisi menyang polyrepo saya aji.

Transisi saka monorepo menyang polyrepo yaiku tugas devops sing penting, lan kudu direncanakake, diatur, lan diprogram.


## Gegayutan


### Keputusan gegayutan

Kita bakal nggawe keputusan kanggo piranti gegayutan kanggo ngatur monorepo (upamane Google Bazel) lan polyrepo (upamane Lyft Refactorator).


### Kabutuhan gegayutan

Kita kudu ngembangake pipeline CI+CD supaya makarya apik karo git.


### Artefak gegayutan

Kita ngarepake organisasi repo duwe artefak gegayutan kanggo provisioning, manajemen konfigurasi, tes, lan bidang devops sing padha. 


### Prinsip gegayutan

Gampang dibatalake. Yen monorepo ora makarya ing praktik, utawa ora dikarepake pimpinan, gampang diganti dadi polyrepo.

Obsesi Pelanggan. Kita ngajeni nyedhiyakake proyek marang pelanggan, lan kita pitados yen monorepo bisa nuntun kita menyang kana luwih cepet tinimbang polyrepo, lan uga mbiyantu iterasi luwih cepet.

Mikir gedhe. Google lan Facebook yaiku panyengkuyung kuwat monorepo tinimbang polyrepo, amarga kabeh tawaran inti bisa dikembangake/dites/disebar bebarengan.


## Cathetan

Tambahna cathetan apa wae ing kene.
