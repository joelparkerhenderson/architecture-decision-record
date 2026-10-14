# [000] Judul
*Beri setiap ADR sebuah nomor agar mudah dirujuk dan dikatalogkan* \
*CATATAN: Semua teks miring berisi petunjuk dan harus dihapus untuk versi produksi*

## Status - DRAFT / ACTIVE /  DEPRECATED by [000] / SUPERSEDES [000]

## Konteks
*Jelaskan secara singkat masalah yang ingin ditangani ADR ini, dan mengapa masalah tersebut ada.*

## Pendekatan yang Diputuskan
*Rincikan keputusan yang signifikan secara arsitektur yang telah / akan dibuat dan jelaskan bagaimana keputusan itu menangani masalah yang diuraikan pada bagian Konteks.*

## Konsekuensi
*Apa dampak keputusan ini terhadap karakteristik arsitektur dan persyaratan fungsional sistem?*

## Tata Kelola
*Bagaimana hasil keputusan ini akan dipantau?* \
*Bagaimana kepatuhan terhadap keputusan ini akan dipastikan?*

## Analisis Opsi
*Jika berlaku, sertakan atau tautkan analisis trade-off apa pun yang telah dilakukan untuk sampai pada keputusan dalam dokumen ini.*

### Legenda
*Opsional: Sediakan alat bantu visual bagi para pemangku kepentingan yang dapat membantu menemukan dengan cepat trade-off positif dan negatif - misalnya sorotan lampu lalu lintas sederhana dengan awalan positif atau negatif.*

Latar belakang <span style="background-color:#4bce97; color:black;">hijau</span> menunjukkan kecocokan yang baik, memburuk menjadi <span style="background-color:#f1c232; color:black;">kuning</span>, dengan <span style="background-color:#e06666; color:black;">merah</span> sebagai kecocokan terburuk. \
\+ menunjukkan komentar yang berdampak positif \
\- menunjukkan komentar yang berdampak negatif

### Ringkasan Tingkat Tinggi
*Seberapa baik setiap opsi cocok dengan konteks masalah secara sekilas?*

<table>
  <thead>
    <tr>
      <th>Ringkasan</th>
      <th>Opsi 1</th>
      <th>Opsi 2</th>
      <th>Opsi 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Kemudahan Implementasi</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Sangat mudah
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Rumit
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Implementasi besar yang memerlukan pengetahuan ahli
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Jangka Waktu</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Sangat cepat
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Cukup lambat
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Sangat lambat
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Nilai Strategis</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Tidak ada nilai strategis, murni taktis
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Sedikit meningkatkan pengalaman orientasi pelanggan
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ideal untuk merger yang akan datang
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Persyaratan Fungsional
*Seberapa baik setiap opsi yang mungkin cocok dengan persyaratan fungsional yang diinginkan?*

<table>
  <thead>
    <tr>
      <th>Skenario</th>
      <th><i>Opsi 1</i></th>
      <th><i>Opsi 2</i></th>
      <th><i>Opsi 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Skenario 1</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Skenario 2</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Skenario 3</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Opsional: Tambahkan baris / tabel lain untuk mencakup skenario masa depan yang sudah diketahui.*

### Persyaratan Nonfungsional
*Seberapa baik setiap opsi yang mungkin cocok dengan karakteristik arsitektur yang diinginkan?
Catatan: ‘Karakteristik Arsitektur’ akan menjadi judul yang lebih tepat, tetapi sesuaikan dengan bahasa yang familier untuk domain bisnis Anda.*

<table>
  <thead>
    <tr>
      <th>Karakteristik </br> Arsitektur</th>
      <th><i>Opsi 1</i></th>
      <th><i>Opsi 2</i></th>
      <th><i>Opsi 3</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Skalabilitas</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Kinerja</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><i>Ketersediaan</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Opsional: Tambahkan atau tautkan definisi karakteristik arsitektur sebagaimana berkaitan dengan bisnis / produk Anda.*
