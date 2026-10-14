# Templat Catatan Keputusan Arsitektur (ADR) <!-- Replace with ADR title -->

Ini adalah templat untuk ADR EdgeX Foundry.

Sumber: https://docs.edgexfoundry.org/2.3/design/adr/template/


### Pengaju

Daftarkan para pengaju ADR.

Format:

- Nama (Organisasi)


## Log Perubahan

Daftarkan perubahan pada dokumen, termasuk status, tanggal, dan URL PR.

Status adalah salah satu dari: pending, approved, amended, deprecated.

Tanggal adalah string ISO 8601 (YYYY-MM-DD).

PR adalah pull request yang mengajukan perubahan, termasuk informasi seperti diff, kontributor, dan peninjau.

Format:

- \[Status ADR, misalnya approved, amended, dll.\]\(URL pull request\) YYYY-MM-DD


## Kasus Penggunaan yang Dirujuk

Daftarkan semua dokumen kasus penggunaan / persyaratan yang relevan.

ADR memerlukan setidaknya satu kasus penggunaan yang relevan dan telah disetujui.

Format:

- \[Nama Kasus Penggunaan\]\(URL\)

Tambahkan penjelasan jika ADR tidak menangani semua persyaratan dari sebuah kasus penggunaan.


## Konteks

Jelaskan:

- bagaimana desain tersebut signifikan secara arsitektur sehingga memerlukan ADR (dibandingkan isu dan PR sederhana untuk memperbaiki masalah)

- pendekatan desain tingkat tinggi (detailnya dijelaskan dalam desain yang diusulkan di bawah)


## Desain yang Diusulkan

Detail desain (tanpa masuk ke implementasi jika memungkinkan).

Garis besar:

- layanan/modul yang akan terdampak (berubah)

- layanan/modul baru yang akan ditambahkan

- dampak pada model dan DTO (perubahan/penambahan/penghapusan)

- dampak pada API (perubahan/penambahan/penghapusan)

- dampak pada konfigurasi umum (pembuatan bagian baru, perubahan/penambahan/penghapusan)

- dampak pada devops


## Pertimbangan

Dokumentasikan alternatif, kekhawatiran, isu pendukung atau terkait, dan pertanyaan yang muncul dalam perdebatan tentang ADR.

Tunjukkan apakah/bagaimana hal tersebut diselesaikan atau diredakan.


## Keputusan

Dokumentasikan detail implementasi penting yang telah disepakati, catatan peringatan, pertimbangan di masa depan, serta isu desain yang tersisa atau ditunda.

Dokumentasikan bagian persyaratan yang tidak dipenuhi oleh desain yang diusulkan.


## ADR Terkait Lainnya

Daftarkan ADR yang relevan, seperti keputusan desain untuk subkomponen dari sebuah fitur, desain yang dinyatakan usang akibat desain ini, dan sebagainya.

Format:

- \[Judul ADR\]\(URL\) - Relevansi


## Referensi

Daftarkan referensi tambahan.

Format:

- \[Judul\]\(URL\)

