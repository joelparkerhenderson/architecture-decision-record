# Fungsi kebugaran kanggo keputusan minangka kode

Fungsi kebugaran yaiku pamriksan otomatis lan objektif, ditulis nganggo kode pamrograman, sing mesthekake yen keputusan tetep dilakoni.

- Fungsi kebugaran ndadekake keputusan bisa dites lan dijamin.

- Fungsi kebugaran kanggo keputusan bisa mbiyantu banget jaminan kualitas, proses regulasi, lan tujuan tata kelola.

## Kepriye fungsi kebugaran nyambung karo keputusan

Cathetan keputusan nyathet keputusan, dene fungsi kebugaran njamin keputusan.

- Conto keputusan: Kita nggunakake event sourcing kanggo kabutuhan audit.

- Conto fungsi kebugaran: Kita nggunakake server integrasi terus-menerus kanggo nes yen kabeh owah-owahan status kudu ngasilake event.

## Kenapa fungsi kebugaran mbiyantu keputusan

Pangukuran objektif: Fungsi kebugaran lulus utawa gagal, dadi pagaweyan katon lan cetha.

Panggunaan terus-terusan: Fungsi kebugaran yaiku aturan urip sampeyan, dilakokake ing saben commit lan build.

Kapercayan kanggo refaktor: Fungsi kebugaran otomatis nyekel kesalahan aturan keputusan.

Tata kelola sing bisa mundhak: Fungsi kebugaran njamin standar tanpa nggawe bottleneck.

## Apa fungsi kebugaran bisa nggunakake AI?

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

## Pengujian unit arsitektur

[ArchUnit](https://www.archunit.org/): priksa aturan arsitektur kode Java nganggo framework uji unit Java biasa apa wae.

[ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS): priksa aturan arsitektur kode TypeScript lan kode JavaScript nganggo Jest, Vitest, Jasmine, lan liya-liyane.
