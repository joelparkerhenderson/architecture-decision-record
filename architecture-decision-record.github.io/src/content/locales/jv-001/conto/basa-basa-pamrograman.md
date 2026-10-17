# Basa-basa pamrograman

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

Kita kudu milih basa pamrograman kanggo piranti lunak kita. Kita nduwe rong kabutuhan utama: basa pamrograman front-end sing cocog kanggo aplikasi web, lan basa pamrograman back-end sing cocog kanggo aplikasi server.


### Keputusan

Kita milih TypeScript kanggo front-end.

Kita milih Rust kanggo back-end.


### Status

Wis diputuske. Kita terbuka kanggo alternatif anyar nalika muncul.


## Rincian


### Anggepan

Aplikasi front-end iku khas:

  * Pangguna lan interaksi sing khas

  * Browser lan sistem sing khas

  * Pangembangan lan deployment sing khas

Aplikasi front-end mbok menawa bakal berkembang cepet:

  * Kita pengin mesthekake pangembangan, deployment, iterasi, lan sapanunggalane sing cepet lan gampang.

  * Kita ngajeni kemampuan dibuktekake, kayata keamanan tipe, lan kita ora masalah nindakake pagaweyan luwih akeh kanggo entuk.

  * Kita ora butuh kompatibilitas warisan.

Aplikasi back-end luwih dhuwur tinimbang biasa:

  * Tujuan kualitas sing luwih dhuwur tinimbang biasa, utamane kemampuan dibuktekake, keandalan, keamanan, lan sapanunggalane.

  * Tujuan near-real-time sing luwih dhuwur tinimbang biasa, yaiku kita ora pengin jeda amarga garbage collection mesin virtual.

  * Tujuan pamrograman fungsional sing luwih dhuwur tinimbang biasa, utamane kanggo paralelisasi, pangolahan multi-inti, lan keamanan memori.

Kita nampa kacepetan compile-time sing luwih andhap kanggo ngutamakake keamanan compile-time lan kacepetan runtime.


### Watesan

Kita nduwe watesan kuwat marang basa sing bisa digunakake karo layanan panyedhia cloud utama kanggo fungsi, kayata Amazon Lambda.


### Posisi

Kita nimbang basa-basa iki:

  * C

  * C++

  * Clojure
  
  * Elixir
  
  * Erlang
  
  * Elm
  
  * Flow
  
  * Go
  
  * Haskell
  
  * Java
  
  * JavaScript
  
  * Kotlin
  
  * Python
  
  * Ruby
  
  * Rust
  
  * TypeScript



### Argumentasi

Ringkesan saben basa:

  * C: ditolak amarga keamanan sing kurang; Rust bisa nindakake meh kabeh luwih apik.

  * C++: ditolak amarga kekacauan; Rust bisa nindakake meh kabeh luwih apik.

  * Clojure: pemodelan apik banget; pendekatan Lisp paling apik; runtime apik ing JVM.
  
  * Elixir: runtime apik banget kalebu deployability lan konkurensi; pengalaman pangembang apik banget; ekosistem relatif cilik.

  * Erlang: runtime apik banget kalebu deployability lan konkurensi; pengalaman pangembang sing nantang; ekosistem relatif cilik.

  * Elm: katon janjeni banget; IBM nerbitake studi kasus gedhe kanthi asil apik; ekosistem luwih cilik.

  * Flow: perbaikan menarik tinimbang JavaScript; nanging, pangembang lagi ninggalake.

  * Go: pengalaman pangembang apik banget; konkurensi apik banget; nanging ana rekam jejak keputusan ala sing nglumpuhake basa.

  * Haskell: basa fungsional paling apik; komunitas pangembang luwih cilik; durung entuk cukup kasil produksi sing diterbitake.

  * Java: runtime apik banget; ekosistem apik banget; pengalaman pangembang ora apik.

  * JavaScript: basa paling populer sakabèhé; ekosistem paling amba.

  * Kotlin: ndandani akeh banget saka Java; dhukungan apik banget saka JetBrains; ana kasus sing diterbitake babagan porting saka Java menyang Kotlin.
  
  * Python: basa paling populer kanggo administrasi sistem; piranti analitik apik; framework web apik; nanging ditinggalake Google kanggo Go.

  * Ruby: pengalaman pangembang paling apik; framework web paling apik; komunitas paling ramah; nanging alon banget; rada angel dipaketake.

  * Rust: basa anyar paling apik; nandheske zero-abstraction; nandheske konkurensi; nanging ekosistem relatif cilik; lan nduwe watesan sengaja marang sawetara akselerasi compiler, upamane akses memori langsung kudu eksplisit unsafe.

  * TypeScript: nambah tipe menyang JavaScript; transpiler apik; pangembang saya akeh sing porting saka JavaScript menyang TypeScript; dhukungan kuwat saka Microsoft.

Kita mutusake yen VM nduwe kumpulan kompromi sing durung kita butuhake saiki, kayata kerumitan tambahan sing nyedhiyakake kemampuan runtime.

Kita pitados yen keputusan inti kita didorong dening rong kuwatir lintas-bidang:

  * Kanggo kacepetan runtime paling cepet lan akses sistem paling rapet, kita bakal milih JavaScript lan C.

  * Kanggo kacepetan runtime meh paling cepet lan akses sistem meh paling rapet, kita milih TypeScript lan Rust.

Panyebutan kehormatan kanggo basa VM lan framework web sing bakal kita pilih yen kita pengin basa VM:

  * Clojure lan Luminus

  * Java lan Spring

  * Elixir lan Phoenix


### Implikasi

Pangembang front-end kudu sinau TypeScript. Iki mbok menawa kurva sinau sing gampang yen pengalaman utama pangembang yaiku nggunakake JavaScript.

Pangembang back-end kudu sinau Rust. Iki mbok menawa kurva sinau sedhengan yen pengalaman utama pangembang yaiku nggunakake C/C++, lan kurva sinau angel yen pengalaman utama pangembang yaiku nggunakake Java, Python, Ruby, utawa basa sing diatur memori sing padha. 

TypeScript lan Rust loro-lorone relatif anyar. Iki tegese akeh piranti durung nduwe dokumentasi kanggo basa-basa iki. Upamane, pipeline devops kudu disetel kanggo basa-basa iki, lan nganti saiki, ora ana piranti devops sing kita evaluasi sing nduwe conto bawaan kanggo basa-basa iki.

Wektu compile kanggo TypeScript lan Rust cukup alon. Sebagian saka iki mbok menawa amarga basa-basa iki isih anyar. Kita mbok menawa kudu ndeleng carane nyuda wektu compile sing alon, kayata compile-on-demand, compile-concurrency, lan sapanunggalane.

Dhukungan IDE kanggo basa-basa iki durung ana ing ngendi-endi lan durung kelas siji. Upamane, JetBrains adol IDE PyCharm kanggo dhukungan kelas siji kanggo Python, nanging ora adol IDE kanthi dhukungan kelas siji kanggo Rust; sakjane, JetBrains bisa nggunakake plug-in Rust sing nyedhiyakake mbok menawa 80% dhukungan basa Rust dibandhingake dhukungan basa Python.


## Gegayutan


### Keputusan gegayutan

Kita bakal ngarahake pilihan ekosistem sing selaras karo basa-basa iki.

Upamane, kita pengin milih IDE sing nduwe kemampuan apik kanggo basa-basa iki.

Upamane, kanggo framework web front-end kita, kita luwih mungkin mutusake framework sing cenderung ngarah menyang TypeScript (upamane Vue) tinimbang framework sing cenderung ngarah menyang JavaScript biasa (upamane React).


### Kabutuhan gegayutan

Kabeh toolchain kita kudu ndhukung basa-basa iki.


### Artefak gegayutan

Kita ngarepake kita mbok menawa bakal ngekspor sawetara rahasia menyang variabel lingkungan.


### Prinsip gegayutan

Ukur kaping pindho, bangun sepisan. Kita ngutamakake sawetara keamanan tinimbang sawetara kacepetan.

Runtime luwih aji tinimbang wektu compile. Kita ngutamakake panggunaan pelanggan tinimbang panggunaan pangembang.


## Cathetan

Cathetan apa wae ing kene.
