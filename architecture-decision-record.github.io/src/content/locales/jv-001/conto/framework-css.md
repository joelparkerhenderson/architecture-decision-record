# Cathetan Keputusan Arsitektur: Framework CSS

Isi:

- [Ringkesan](#ringkesan)
  - [Masalah](#masalah)
  - [Keputusan](#keputusan)
  - [Status](#status)
- [Rincian](#rincian)
  - [Anggepan](#anggepan)
  - [Watesan](#watesan)
  - [Posisi](#posisi)
  - [Argumentasi](#argumentasi)
  - [Implikasi](#implikasi)
- [Gegayutan](#gegayutan)
  - [Keputusan gegayutan](#keputusan-gegayutan)
  - [Kabutuhan gegayutan](#kabutuhan-gegayutan)
  - [Artefak gegayutan](#artefak-gegayutan)
  - [Prinsip gegayutan](#prinsip-gegayutan)
- [Cathetan](#cathetan)


## Ringkesan


### Masalah

Kita pengin nggunakake framework CSS kanggo nggawe aplikasi web kita:

  * Kita pengin pengalaman pangguna cepet lan bisa dipercaya, ing kabeh browser populer lan ukuran layar.

  * Kita pengin iterasi cepet ing desain, tata letak, UI/UX, lan sapanunggalane.

  * Kita pengin aplikasi responsif, utamane kanggo layar cilik kayata ing piranti seluler, layar gedhe kayata ing widescreen 4K, lan layar dinamis kayata tampilan sing bisa diputer.  


### Keputusan

Milih Bulma.


### Status

Milih Bulma. Terbuka kanggo pilihan framework CSS anyar nalika muncul.


## Rincian


### Anggepan

Kita pengin nggawe aplikasi web sing modern, cepet, bisa dipercaya, responsif, lan sapanunggalane.

Aplikasi web modern biasane nyuda/ngilangi panggunaan jQuery amarga pirang-pirang alasan: 

  * JavaScript modern lagi nambahake akeh kemampuan sing biyen disedhiyakake jQuery, mula jQuery kurang dibutuhake, lan ana modul sing luwih apik/luwih cepet/luwih cilik sing nyedhiyakake implementasi khusus

  * Pendekatan jQuery sing amba yaiku manipulasi DOM langsung, sing dadi anti-pola kanggo framework JavaScript modern (upamane React, Vue, Svelte)

  * jQuery ngganggu awake dhewe yen dimuat kaping pindho, lan sapanunggalane


### Watesan

Yen kita milih framework CSS sing nggunakake jQuery, kita kepeksa ngimpor jQuery. Upamane, Semantic UI nggunakake jQuery, lan Tachyons ora.

Yen kita milih framework CSS sing minimalis, kita ngeculake komponen framework sing mbok menawa kita karepake saiki utawa enggal. Upamane, Semantic UI nyedhiyakake carousel gambar, lan Tachyons ora.


### Posisi

Kita nimbang ora nggunakake framework. Iki isih katon bisa ditindakake, utamane amarga CSS grid nyedhiyakake akeh sing dibutuhake proyek kita..

Kita nimbang akeh framework CSS kanthi triase dhaptar cendhak cepet: Bootstrap, Bulma, Foundation, Materialize, Semantic UI, Tachyons, lan sapanunggalane. Rong pilihan kita kanggo review luwih jero yaiku Semantic UI (amarga nduwe pendekatan paling semantik) lan Bulma (amarga nduwe pendekatan paling entheng sing nyedhiyakake komponen sing kita butuhake saiki).

Kita nimbang Semantic UI. Iki nyedhiyakake akeh komponen, kalebu sing kita karepake kanggo proyek kita: tab, grid, tombol, lan sapanunggalane. Kita nindakake pilot karo Semantic UI kanthi rong cara: nggunakake berkas CDN biasa, lan nggunakake repo NPM. Kita kasil nggunakake Semantic UI ing kaca HTML statis, nanging ora kasil ing wektu sing wis ditemtokake kanggo mbangun SPA JavaScript (utamane amarga masalah pemuatan jQuery). Kita nemokake yen koder liyane wis njaluk marang pangembang Semantic UI supaya nggawe versi tanpa jQuery, kanthi alasan sing padha karo kita. Koder liyane wis pirang-pirang taun njaluk versi tanpa jQuery, nanging pangembang wis ngomong ora, lan ngandhakake yen versi tanpa jQuery apa wae bakal angel banget ditulis, upamane ~"proyek Semantic UI nduwe luwih saka 22.000 titik kontak sing nggunakake jQuery".

Conto karo Semantic:

```html
<div class="ui top attached tabular menu">
  <a class="item">Alpha</a>
  <a class="item">Bravo</a>
</div>
```

Kita nimbang Bulma. Bulma nduwe akeh kemampuan sing padha karo Semantic UI, sanajan ora akeh komponen canggih. Bulma dibangun nganggo teknik modern, kayata tanpa jQuery. Bulma nduwe sawetara komponen pihak katelu, sing sawetara mbok menawa pengin kita gunakake.


Conto karo Bulma:
```html
<div class="tabs">
  <ul>
    <li><a>Alpha</a></li>
    <li><a>Bravo</a></li>
  </ul>
</div>
```


### Argumentasi

Kaya ing ndhuwur.

Khusus, Semantic UI katon nduwe gendera ati-ati ing babagan teknologi (yaiku akeh banget titik kontak jQuery) lan uga ing babagan kepemimpinan (yaiku tanpa jQuery iku tolakan keras, tinimbang nyoba peta dalan, utawa perbaikan terus-terusan, utawa penggalangan dana, lan sapanunggalane).


### Implikasi

Yen kita nemokake framework CSS non-jQuery sing apik, iki umume migunani lan apik sakabèhé.


## Gegayutan


### Keputusan gegayutan

Framework CSS sing kita pilih bisa mengaruhi kemampuan diuji.


### Kabutuhan gegayutan

Kita pengin ngirim aplikasi modern murni kanthi cepet. 

Kita ora pengin nglampahi wektu makarya ing framework lawas (utamane Semantic UI) sing nggunakake dependensi lawas (utamane jQuery).


### Artefak gegayutan

Mengaruhi kabeh HTML biasa sing bakal nggunakake CSS.


### Prinsip gegayutan

Gampang dibatalake.

Perlu kacepetan.


## Cathetan

Cathetan apa wae ing kene.
