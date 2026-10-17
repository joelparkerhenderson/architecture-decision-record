# Cathetan Keputusan Arsitektur: Orkestrasi kontainer Kubernetes

## Pernyataan Masalah 

Kita kudu milih platform orkestrasi kontainer kanggo portofolio aplikasi cloud-native kita sing saya gedhe. Deployment platform lawas kita saiki alon banget, lan ora cukup gesit kanggo ngoyak kabutuhan kita sing saya akeh. Kita nggoleki sistem sing bakal ngidini kita ngukur layanan kita kanthi cara paling efisien tanpa ngorbanake kegesitan utawa gampange panggunaan.

## Alternatif sing Dipikirake

1. Docker Swarm

2. Kubernetes

3. Apache Mesos

## Keputusan sing Dijupuk

Sawise nindakake analisis sing teliti marang saben platform orkestrasi kontainer, kita mutusake nggunakake Kubernetes minangka pilihan paling apik kanggo kabutuhan perusahaan kita. Alasan kita milih Kubernetes yaiku:

1. **Skalabilitas:**  Desain unik Kubernetes sampurna kanggo ngukur aplikasi, lan nalika kabutuhan skalabilitas kita berkembang saka wektu, Kubernetes nduwe kemampuan bawaan kanggo nuhoni owah-owahan iki tanpa masalah.

2. **Arsitektur Terdesentralisasi:**  Topologi master-worker Kubernetes mesthekake arsitektur terdesentralisasi sing mesthekake ora ana titik kegagalan tunggal.

3. **Dhukungan Komunitas:**  Kubernetes nduwe komunitas open-source paling gedhe lan paling aktif, tegese nduwe akeh kontributor, pangembang, lan vendor sing nggawe luwih gampang kanggo kita entuk bantuan lan nemokake sumber daya.

4. **Dhukungan Ekosistem:**  Kubernetes nduwe ekosistem sing saya berkembang karo macem-macem piranti pihak katelu, integrasi karo registri kontainer, pipeline CI/CD, panyimpenan data, lan liya-liyane.

Mula, kita mutusake nggunakake Kubernetes minangka platform orkestrasi kontainer kita kanggo saiki lan mbesuk cedhak.

<h6>Kredit: kaca iki digawe dening ChatGPT, banjur disunting kanggo kajelasan lan format.</h6>
