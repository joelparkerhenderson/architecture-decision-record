# Fitness function untuk keputusan sebagai kode

Fitness function adalah pemeriksaan otomatis yang objektif, ditulis dengan kode pemrograman, yang memverifikasi bahwa keputusan tetap dipertahankan.

- Fitness function membuat keputusan dapat diuji dan terjamin.

- Fitness function untuk keputusan dapat sangat membantu penjaminan mutu, proses regulasi, dan tujuan tata kelola.

## Bagaimana fitness function terhubung dengan keputusan

Catatan keputusan mendokumentasikan keputusan, sedangkan fitness function menjamin keputusan tersebut.

- Contoh keputusan: Kami menggunakan event sourcing untuk memenuhi persyaratan audit.

- Contoh fitness function: Kami menggunakan server integrasi berkelanjutan untuk menguji bahwa semua perubahan status harus menghasilkan event.

## Mengapa fitness function membantu keputusan

Pengukuran objektif: Fitness function lulus atau gagal, sehingga pekerjaan terlihat dan jelas.

Penggunaan berkelanjutan: Fitness function adalah aturan hidup Anda, dijalankan pada setiap commit dan build.

Percaya diri untuk melakukan refactoring: Fitness function secara otomatis menangkap kesalahan aturan keputusan.

Tata kelola yang dapat diskalakan: Fitness function menjamin standar tanpa menciptakan hambatan.

## Dapatkah fitness function menggunakan AI?

Fitness function dapat memanfaatkan LLM AI untuk keputusan dengan mengajukan pertanyaan tentang pekerjaan Anda,
seperti rencana, kode, skema, API, dan lainnya:

```txt
IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning.
IMPORTANT: Turn on extended thinking. Turn on expert advice. Turn on search.

This is a fitness function to evaluate if our work is
using all our decisions, and is correct and accurate.

- Our decisions are here: {url}
- Our work to evaluate is here: {url}

Explain any errors, problems, gaps, weaknesses. Be direct. Be decisive.
```

## Pengujian unit arsitektur

[ArchUnit](https://www.archunit.org/): memeriksa aturan arsitektur kode Java dengan menggunakan kerangka pengujian unit Java biasa apa pun.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): memeriksa aturan arsitektur kode TypeScript dan kode JavaScript dengan menggunakan Jest, Vitest, Jasmine, dan sebagainya.
