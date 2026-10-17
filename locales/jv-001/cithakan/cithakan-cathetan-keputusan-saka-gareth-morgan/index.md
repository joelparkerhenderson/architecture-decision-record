# [000] Judhul
*Wenehana saben ADR nomer supaya gampang dirujuk lan didhaptar* \
*CATHETAN: Kabeh teks miring menehi pitunjuk lan kudu dibusak kanggo produksi*

## Status - DRAF / AKTIF /  DIGANTEKAKE DENING [000] / NGGANTEKAKE [000]

## Konteks
*Jlentrehake kanthi cendhak masalah sing arep ditanggapi ADR iki, lan kenapa masalah kuwi ana.*

## Pendekatan sing Diputuske
*Rincenana keputusan penting sacara arsitektural sing wis / bakal dijupuk lan jlentrehake carane nanggapi masalah sing kasebut ing bagean Konteks.*

## Akibat
*Apa pengaruh keputusan iki marang karakteristik arsitektur lan kabutuhan fungsional sistem?*

## Tata Kelola
*Kepriye asil keputusan iki bakal dipantau?* \
*Kepriye kepatuhan marang keputusan iki bakal dipesthekake?*

## Analisis Pilihan
*Yen ana, lebokna utawa link menyang analisis kompromi apa wae sing wis ditindakake kanggo tekan keputusan ing dokumen iki.*

### Kunci
*Opsional: Sedhiyakna piranti visual kanggo pemangku kepentingan sing bisa mbiyantu kanthi cepet ndeteksi kompromi positif lan negatif - upamane sorotan lampu lalu lintas sederhana nganggo awalan positif utawa negatif.*

Latar <span style="background-color:#4bce97; color:black;">ijo</span> nuduhake kecocogan sing apik, saya ala liwat <span style="background-color:#f1c232; color:black;">kuning</span>, lan <span style="background-color:#e06666; color:black;">abang</span> yaiku kecocogan paling ala. \
\+ nuduhake komentar sing duwe pengaruh positif \
\- nuduhake komentar sing duwe pengaruh negatif

### Ringkesan Tingkat Dhuwur
*Sepira cocog saben pilihan karo konteks masalah sepintas?*

<table>
  <thead>
    <tr>
      <th>Ringkesan</th>
      <th>Pilihan 1</th>
      <th>Pilihan 2</th>
      <th>Pilihan 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i>Gampang diimplementasikake</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
          + Gampang banget
        </span>
      </td>
      <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Rumit
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Implementasi gedhe sing mbutuhake kawruh ahli
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Jadwal</i></td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Cepet banget
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            - Lumayan alon
        </span>
      </td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Alon banget
        </span>
      </td>
    </tr>
    <tr>
      <td><i>Nilai Strategis</i></td>
      <td>
        <span style="background-color:#e06666; color:black; padding-right:5px">
            - Ora ana nilai strategis, mung taktis
        </span>
      </td>
       <td>
        <span style="background-color:#f1c232; color:black; padding-right:5px">
            + Rada nambah pengalaman onboarding pelanggan
        </span>
      </td>
      <td>
        <span style="background-color:#4bce97; color:black; padding-right:5px">
            + Ideal kanggo merger sing bakal teka
        </span>
      </td>
    </tr>
  </tbody>
</table>

### Kabutuhan Fungsional
*Sepira cocog saben pilihan potensial karo kabutuhan fungsional sing dikarepake?*

<table>
  <thead>
    <tr>
      <th>Skenario</th>
      <th><i>Pilihan 1</i></th>
      <th><i>Pilihan 2</i></th>
      <th><i>Pilihan 3</i></th>
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

*Opsional: Tambahna larik / tabel liyane kanggo nyakup skenario mbesuk sing wis dingerteni.*

### Kabutuhan Non-Fungsional
*Sepira cocog saben pilihan potensial karo karakteristik arsitektur sing dikarepake?
Cathetan: ‘Karakteristik Arsitektur’ bakal dadi judhul sing luwih cocog, nanging cocogna karo basa sing akrab kanggo domain bisnismu.*

<table>
  <thead>
    <tr>
      <th>Karakteristik </br> Arsitektur</th>
      <th><i>Pilihan 1</i></th>
      <th><i>Pilihan 2</i></th>
      <th><i>Pilihan 3</i></th>
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
      <td><i>Kasedhiyan</i></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

*Opsional: Tambahna utawa link menyang definisi karakteristik arsitektur kaya sing gegayutan karo bisnis / produkmu.*
