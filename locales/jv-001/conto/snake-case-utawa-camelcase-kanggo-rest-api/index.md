# Cathetan Keputusan Arsitektur: snake_case utawa camelCase kanggo REST API?

Keputusan: konvensi panamaan snake_case bakal digunakake kanggo endpoint REST API

Status: Ditampa

## Konteks

Ing konvensi panamaan kanggo REST API, ana rong format populer: snake_case lan camelCase. Format snake_case yaiku ing ngendi saben tembung ing jeneng dipisahake dening garis ngisor, dene camelCase yaiku ing ngendi tembung pisanan jeneng nganggo huruf cilik, lan tembung-tembung sabanjure aksara pisanane dikapitalisasi. Keputusan iki bakal nemtokake konvensi panamaan endi sing kudu digunakake kanggo REST API.

## Pendorong Keputusan

- Konsistensi karo konvensi panamaan sing wis ana ing proyek

- Keterbacaan lan kajelasan kanggo sapa wae sing makarya ing API

- Keselarasan karo praktik paling apik industri kanggo konvensi panamaan REST API

- Gampang diimplementasikake lan dijaga

## Keputusan

Konvensi panamaan snake_case bakal digunakake kanggo endpoint REST API. Pilihan iki didorong dening faktor-faktor ing ngisor iki:

1. **Konsistensi**: Proyek wis nggunakake konvensi panamaan snake_case kanggo kabeh endpoint, lan migunani kanggo njaga konvensi iki supaya konsisten ing kabeh proyek.

2. **Keterbacaan lan kajelasan**: Konvensi snake_case luwih gampang diwaca lan dimangerteni. Garis ngisor nyedhiyakake pamisahan cetha antarane tembung, nggampangake nguraikan lan mangerteni teges jeneng.

3. **Keselarasan karo praktik paling apik industri**: Konvensi snake_case akeh digunakake ing industri lan dianggep minangka praktik paling apik kanggo REST API, ndadekake pilihan apik kanggo proyek.

4. **Gampang diimplementasikake lan dijaga**: Njaga konvensi panamaan sing wis ana luwih gampang diimplementasikake lan dijaga amarga kabeh kode lan dokumentasi sing wis ana kudu dianyari yen konvensi anyar dipilih.

## Akibat

Ana akibat potensial saka keputusan iki. 

* Yen ana anggota tim anyar sing gabung ing proyek ora kenal karo konvensi panamaan snake_case, bisa nuntun marang bingung lan kesalahan ing pangembangan. Nanging, amarga snake_case yaiku konvensi sing akeh digunakake, resiko kaya mangkono minimal. 
  
* Yen piranti utawa framework liyane digunakake ing proyek sing adhedhasar banget marang konvensi camelCase, mbok menawa mbutuhake upaya tambahan kanggo ngonversi antarane konvensi panamaan. Nanging, iki dudu kuwatir signifikan amarga proyek wis nstandarisasi konvensi snake_case. 
 
Sakabèhé, keputusan nggunakake konvensi panamaan snake_case kanggo endpoint REST API ngasilake pendekatan sing konsisten, bisa diwaca, lan standar industri nalika gampang diimplementasikake lan dijaga.

<h6>Kredit: kaca iki digawe dening ChatGPT, banjur disunting kanggo kajelasan lan format.</h6>
