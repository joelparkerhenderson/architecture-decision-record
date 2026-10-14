# Templat catatan keputusan untuk Keputusan Teknis Penting (ITD)

Ini adalah templat Keputusan Teknis Penting (Important Technical Decisions, ITD) yang dijelaskan dalam
[ITDs: a lean ADR for executive technical decision-making at scale - Ignacio Larrañaga](https://ignaciolarranaga.medium.com/itds-a-lean-adr-for-executive-technical-decision-making-at-scale-e18bb3f6a563).

ITD adalah evolusi terfokus dari ADR, dioptimalkan untuk kecepatan, kejelasan, dan
validasi eksekutif. Jika ADR mendokumentasikan apa yang diputuskan, ITD adalah
artefak ramping yang mengutamakan keputusan, yang membuat keputusan itu sendiri dapat ditinjau, sehingga
para pemangku kepentingan dapat memindainya dengan cepat dan menantangnya dengan mudah. ITD sangat cocok
untuk keputusan teknis yang tidak sepenuhnya bersifat arsitektural, seperti memilih
model, pustaka, atau strategi CI/CD.

Di setiap file ITD, tulis bagian-bagian berikut:

# Judul

Nyatakan keputusan itu sendiri, bukan deskripsi topiknya.
Misalnya, "Gunakan Qwen2.5 1.5B Instruct untuk penerjemahan di perangkat".

## Masalah

Satu kalimat yang menyatakan apa yang ingin kita selesaikan.

## Opsi yang Dipertimbangkan

Alternatif yang ada di meja, dengan opsi yang dipilih dicetak **tebal**.

## Alasan

Hanya faktor-faktor penentu yang mengarah pada pilihan tersebut, bukan daftar lengkap
setiap kelebihan dan kekurangan.

## Catatan

Opsional. Konteks tambahan apa pun yang layak dicatat, seperti batasan,
asumsi, atau tautan.
