# Format cap wektu

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

Kita pengin bisa nglacak kapan perkara kedadeyan kanthi nggunakake cap wektu lan nggunakake format cap wektu sing konsisten sing makarya apik ing kabeh sistem kita lan sistem pihak katelu.

Kita berinteraksi karo sistem sing nduwe format cap wektu beda-beda:

* Pesen JSON ora nduwe format cap wektu asli, mula kita kudu milih carane ngonversi cap wektu dadi string, lan ngonversi string dadi cap wektu, yaiku carane serialisasi/deserialisasi.

* Sawetara aplikasi disetel nggunakake wektu lokal, tinimbang wektu UTC. Iki bisa trep kanggo proyek sing kudu nyesuekake karo wektu lokal, kayata proyek sing nggugah event adhedhasar wektu lokal.

* Sawetara sistem nduwe kabutuhan lan kemampuan presisi wektu sing beda, kayata nggunakake resolusi wektu detik utawa milidetik utawa nanodetik. Upamane, prentah `date` sistem operasi Linux nggunakake presisi wektu bawaan detik, dene bursa saham Nasdaq pengin presisi wektu bawaan nanodetik.


### Keputusan

Kita milih format standar cap wektu ISO 8601 kanthi presisi nanodetik, khususe "YYYY-MM-DDTHH:MM:SS.NNNNNNNNNZ".

Format nuduhake taun, sasi, tanggal, jam, menit, detik, nanodetik, lan zona wektu Zulu alias UTC, GMT.


### Status

Wis diputuske.


## Rincian


### Anggepan

Kita kudu nangani string teks cap wektu iki, kanggo ngonversi saka cap wektu dadi string (alias serialisasi) lan ngonversi saka string dadi cap wektu (alias deserialisasi).

Kita pengin format sing umume gampang digunakake, gampang dikonversi, lan gampang diwaca manungsa.

Kita pengin kompatibilitas karo macem-macem sistem njaba sing ora bisa kita kontrol, kayata sistem analitik, sistem basis data, sistem finansial.


### Watesan

Sawetara sistem nduwe watesan presisi wektu. Upamane, prentah `date` sistem operasi macOS bisa nyithak presisi wektu ing detik, nanging ora ing nanodetik.


### Posisi

Kita nimbang macem-macem pilihan:

* Unix epoch yaiku siji nomer sing mundhak.

* Format teks ringkes "YYYYMMDDTHHMMSSNNNNNNNNN".

* Nggunakake zona wektu lokal utawa zona wektu UTC.


### Argumentasi

Kanggo panggunaan khas, kita ngajeni gampang diwaca/ditulis manungsa, luwih saka kacepetan/ukuran mentah.

Kanggo panggunaan khas, kita pengin format sing makarya apik ing sistem mesin, lan uga makarya apik sacara manual, kayata nulis data conto, maca output JSON, nggrep berkas log, lan sapanunggalane.

Kanggo panggunaan ora khas, kayata komputasi kinerja dhuwur, kita ngarepake kita bakal pengin ngoptimalake format teks apa wae sing kita pilih kanthi ngonversi teks dadi format sing luwih cepet, kayata jinis obyek tanggal bawaan basa pamrograman. Dadi format teks ora ndadekake bedane akeh kanggo HPC.


### Implikasi

Macem-macem sistem teks lan sistem wektu kita bakal konvergen ing format iki.


## Gegayutan


### Keputusan gegayutan

Kita mbok menawa pengin cara cepet/gampang kanggo uga nglacak delta wektu alias durasi. Iki gampang karo cap wektu Unix epoch.


### Kabutuhan gegayutan

Kita mbok menawa pengin ngowahi keputusan kita, upamane yen kita duwe kabutuhan gegayutan kanggo jinis cap pesen logging tartamtu, kayata kanggo Splunk, Sumo, ELK, lan sapanunggalane.


### Artefak gegayutan

Formatter lan parser basa:

  * [date-fns: Pustaka utilitas tanggal JavaScript modern](https://date-fns.org/)
  * [Crono: pustaka tanggal lan wektu kanggo Rust](https://github.com/chronotope/chron)
  
Conto Rosetta Code:

  * [Wektu sistem](https://www.rosettacode.org/wiki/System_time)
  * [Format data](https://www.rosettacode.org/wiki/Date_format)
  * [Nuduhake epoch](https://www.rosettacode.org/wiki/Show_the_epoch)

Conto SixArm:

  * [now_string](https://github.com/SixArm/rosetta_code/tree/master/tasks/now_string)


### Prinsip gegayutan

Gampang dibatalake. Kita bisa ngowahi kanthi gampang menyang format beda, kayata Unix epoch.

Tundha optimasi prematur. Kanggo panggunaan khas kita ora peduli akeh babagan sawetara karakter ekstra kayata format sing nggunakake garis sambung lan titik loro.


## Cathetan

Tambahna cathetan ing kene.
