# Proses cathetan keputusan arsitektur AWS

https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

Cathetan keputusan arsitektur (ADR) yaiku dokumen sing nerangake pilihan sing dijupuk tim babagan aspek penting arsitektur piranti lunak sing direncanakake dibangun. Saben ADR nerangake keputusan arsitektur, konteks, lan akibate. ADR nduwe status mula nuruti daur urip. Kanggo conto ADR, deleng lampiran.

Proses ADR ngasilake kumpulan cathetan keputusan arsitektur. Kumpulan iki mbentuk log keputusan. Log keputusan nyedhiyakake konteks proyek uga informasi implementasi lan desain sing rinci. Anggota proyek mbaca sepintas judhul saben ADR kanggo entuk ringkesan konteks proyek. Padha maca ADR kanggo nyelehi jero implementasi lan pilihan desain proyek.

Nalika tim nampa ADR, ADR dadi ora owah. Yen wawasan anyar mbutuhake keputusan beda, tim ngusulake ADR anyar. Nalika tim nampa ADR anyar, ADR anyar nggantekake ADR sadurunge.

## Lingkup proses ADR

Anggota proyek kudu nggawe ADR kanggo saben keputusan sing penting sacara arsitektur sing mengaruhi proyek utawa produk piranti lunak, kalebu:

* Struktur (upamane, pola kayata microservices)

* Kabutuhan non-fungsional (keamanan, ketersediaan dhuwur, lan toleransi kesalahan)

* Dependensi (kopling komponen)

* Antarmuka (API lan kontrak sing diterbitake)

* Teknik konstruksi (pustaka, framework, piranti, lan proses)

* Kabutuhan fungsional lan non-fungsional iku input paling umum kanggo proses ADR.


## Isi ADR

Nalika tim ngenali kabutuhan ADR, anggota tim miwiti nulis ADR adhedhasar cithakan sak proyek. (Deleng organisasi GitHub ADR kanggo cithakan conto.) Cithakan nyederhanakake nggawe ADR lan mesthekake yen ADR nyathet kabeh informasi sing gegayutan. Paling ora, saben ADR kudu nemtokake konteks keputusan, keputusane dhewe, lan akibat keputusan kanggo proyek lan deliverables-e. (Kanggo conto bagean-bagean iki, deleng lampiran.) Salah sijine aspek paling kuwat saka struktur ADR yaiku fokus ing alasan keputusan, dudu carane tim ngimplementasikake. Mangerteni kenapa tim nggawe keputusan nggampangake anggota tim liyane nampa keputusan kuwi, lan nyegah arsitek liya sing ora melu proses nggawe keputusan supaya ora mbatalake keputusan kuwi ing mbesuk.


## Proses nampa ADR

Saben anggota tim bisa nggawe ADR, nanging tim kudu netepake definisi kepemilikan kanggo ADR. Saben penulis sing dadi pemilik ADR kudu aktif njaga lan ngomunikasikake isi ADR. Kanggo njlentrehake kepemilikan iki, pandhuan iki nyebut penulis ADR minangka pemilik ADR ing bagean-bagean sabanjure. Anggota tim liyane tansah bisa nyumbang marang ADR. Yen isi ADR owah sadurunge tim nampa ADR, pemilik kudu nyetujoni owah-owahan kuwi.

Sawise tim ngenali keputusan arsitektur lan pemiliké, pemilik ADR nyediakake ADR ing status **Diusulake** (Proposed) ing wiwitan proses. ADR ing status Diusulake wis siap kanggo review.

Pemilik ADR banjur miwiti proses review kanggo ADR. Tujuan proses review ADR yaiku mutusake apa tim nampa ADR, nemtokake yen perlu dikerjakake maneh, utawa nolak ADR. Tim proyek, kalebu pemilik, mriksa ADR. Rapat review kudu diwiwiti nganggo slot wektu khusus kanggo maca ADR. Rata-rata, 10 nganti 15 menit kudu cukup. Sajrone wektu iki, saben anggota tim maca dokumen lan nambah komentar lan pitakon kanggo nandhani topik sing durung cetha. Sawise fase review, pemilik ADR maca lan ngrembug saben komentar karo tim.

Yen tim nemokake butir tindakan kanggo nambahi ADR, status ADR tetep **Diusulake**. Pemilik ADR nyusun tindakan-tindakan, lan, bebarengan karo tim, nambah penanggung jawab kanggo saben tindakan. Saben anggota tim bisa nyumbang lan ngrampungake butir tindakan. Dadi tanggung jawab pemilik ADR kanggo njadwalake maneh proses review.

Tim uga bisa mutusake kanggo nolak ADR. Ing kasus iki, pemilik ADR nambahake alasan penolakan kanggo nyegah rembugan ing mbesuk babagan topik sing padha. Pemilik ngowahi status ADR dadi **Ditolak** (Rejected).

Yen tim nyetujoni ADR, pemilik nambah cap wektu, versi, lan dhaptar pemangku kepentingan. Pemilik banjur nganyari status dadi **Ditampa** (Accepted).

ADR lan log keputusan sing digawe makili keputusan sing dijupuk tim lan nyedhiyakake sejarah kabeh keputusan. Tim nggunakake ADR minangka rujukan nalika review kode lan arsitektur menawa bisa. Saliyane nindakake review kode, tugas desain, lan tugas implementasi, anggota tim kudu ngrujuk ADR kanggo keputusan strategis produk.

Minangka praktik apik, saben owah-owahan piranti lunak kudu ngliwati review kanca lan mbutuhake paling ora siji persetujuan. Sajrone review kode, peninjau kode bisa nemokake owah-owahan sing nglanggar siji utawa luwih ADR. Ing kasus iki, peninjau njaluk penulis owah-owahan kode nganyari kode, lan nuduhake link menyang ADR. Nalika penulis nganyari kode, kode disetujoni dening peninjau kanca lan digabung menyang basis kode utama.


## Proses review ADR

Tim kudu nganggep ADR minangka dokumen sing ora owah sawise tim nampa utawa nolak. Owah-owahan marang ADR sing wis ana mbutuhake nggawe ADR anyar, netepake proses review kanggo ADR anyar, lan nyetujoni ADR. Yen tim nyetujoni ADR anyar, pemilik kudu ngowahi status ADR lawas dadi **Digantekake** (Superseded).
