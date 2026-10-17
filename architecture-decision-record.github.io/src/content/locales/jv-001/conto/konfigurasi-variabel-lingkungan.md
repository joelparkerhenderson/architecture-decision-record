# Konfigurasi variabel lingkungan

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

Kita pengin aplikasi kita bisa dikonfigurasi ngluwihi artefak/binar/sumber, supaya siji build bisa tumindak beda gumantung lingkungan deployment-e.

  * Kanggo nggayuh iki, kita pengin nggunakake konfigurasi variabel lingkungan.

  * Kita pengin ngatur konfigurasi kanthi nggunakake berkas sing bisa kita kontrol versine.

  * Kita pengin nyedhiyakake sawetara kenyamanan pengalaman pangembang, kayata ngerti apa sing bisa dikonfigurasi lan nilai bawaan sing gegayutan.


### Keputusan

Milih berkas .env karo berkas bawaan lan berkas skema sing gegayutan.


### Status

Wis diputuske. Terbuka kanggo nimbang kemampuan anyar nalika muncul.


## Rincian


### Anggepan

Kita luwih seneng misahake kode aplikasi lan kode lingkungan. Kita nganggep aplikasi kudu tumindak beda ing lingkungan beda, kayata lingkungan pangembangan, lingkungan tes, lingkungan demo, lingkungan produksi, lan sapanunggalane.

Kita luwih seneng praktik industri "12 factor app" lan malah luwih seneng praktik sing gegayutan "15 factor app".

Akeh proyek kita sadurunge nggunakake konvensi berkas `.env` utawa direktori `.env` sing padha. Ana praktik umum njaga iki saka kontrol versi, lan nggunakake cara liya kanggo nyebar, ngontrol versi, lan ngatur.


### Watesan

Kita pengin njaga rahasia saka sistem kontrol versi (VCS) manajemen kode sumber (SCM) kita.

Kita pengin ngarahake kompatibilitas karo framework lan pustaka piranti lunak sing populer. Upamane, Node nduwe modul "dotenv" kanggo maca konfigurasi variabel lingkungan.


### Posisi

Kita nimbang sawetara pendekatan:

  * Nyimpen konfigurasi ing aplikasi kayata ing berkas `config.js`.

  * Nyimpen konfigurasi ing lingkungan kayata ing berkas `.env`.

  * Njupuk konfigurasi saka lokasi sing dikenal kayata server lisensi.


### Argumentasi

Kita milih pendekatan berkas .env amarga:

  * Populer, kalebu ing antarane para ahli.

  * Ngetutake pola berkas `.env` sing wis kasil digunakake tim-tim kita kaping pirang-pirang ing akeh proyek.

  * Prasaja. Utamane, kita ora masalah saiki karo kompromi gedhe sing kita deleng, kayata ora ana kemampuan audit dibandhingake pendekatan server lisensi.


### Implikasi 

Kita kudu golek cara kanggo misahake konfigurasi variabel lingkungan sing umum saka manajemen rahasia.


## Gegayutan


### Keputusan gegayutan

Kita ngarepake kabeh aplikasi kita nggunakake pendekatan iki.

Kita bakal ngrencanakake nganyari aplikasi apa wae sing nggunakake pendekatan sing kurang mampu, kayata hardcode ing binar utawa ing kode sumber.

Kita bakal njaga aplikasi apa wae sing nggunakake pendekatan sing luwih mampu, kayata server lisensi.


### Kabutuhan gegayutan

Kita bakal nambah kemampuan devops kanggo berkas-berkas, kalebu hook, tes, lan integrasi terus-menerus.

Kita kudu nglatih kabeh kanca pangembang babagan keputusan iki.



### Artefak gegayutan

Saben wilayah ing ngendi kita nyebar bakal mbutuhake berkas .env dhewe lan berkas gegayutan.


### Prinsip gegayutan

Gampang dibatalake.


## Cathetan


Conto berkas `.env`:

```env
NAME=Alice Anderson
EMAIL=alice@example.com
```

Conto berkas `.env.defaults`:

```env
NAME=Joe Doe
EMAIL=joe@example.com
```

Conto berkas `.env.schema` mung karo kunci:

```env
NAME
EMAIL
```
