# Cathetan Keputusan Arsitektur: Milih Teknologi Basis Data

## Status

Ditampa

## Konteks

Kita lagi ngrancang aplikasi anyar sing mbutuhake panyimpenan lan pamundhutan data kanthi cara sing bisa mundhak lan kinerja apik. Kita wis ngenali telung jinis teknologi basis data sing umum digunakake: basis data relasional, basis data dokumen, lan basis data event.

Basis data relasional nyimpen data ing tabel kanthi skema tetep lan nerapake watesan integritas data sing ketat. Cocog kanggo aplikasi sing mbutuhake hubungan data lan transaksi sing kompleks. Conto kalebu MySQL, PostgreSQL, lan Oracle.

Basis data dokumen nyimpen data ing dokumen kaya JSON lan ora nganggo skema. Cocog banget kanggo aplikasi sing mbutuhake model data sing fleksibel lan skala horisontal. Conto kalebu MongoDB, Couchbase, lan Amazon DynamoDB.

Basis data event nyimpen data minangka rangkaian event, nyathet saben owah-owahan marang data. Cocog kanggo aplikasi sing mbutuhake audit, event sourcing, lan pangolahan data kompleks. Conto kalebu Apache Kafka, Apache Pulsar, lan AWS Kinesis.
Keputusan

Sawise nliti kanthi teliti kabutuhan lan watesan aplikasi kita, kita mutusake nggunakake basis data dokumen.

## Alasan

Kita milih basis data dokumen amarga:

1. Aplikasi kita mbutuhake model data fleksibel sing bisa berkembang saka wektu. Basis data dokumen ngidini kita nyimpen data ing format tanpa skema, tegese kita bisa nambah kolom anyar utawa ngowahi struktur dokumen sing wis ana tanpa kudu ngowahi skema basis data.

2. Aplikasi kita kudu bisa mundhak sacara horisontal kanggo nangani volume data lan lalu lintas gedhe. Basis data dokumen nyedhiyakake dhukungan bawaan kanggo sharding lan replikasi, sing ngidini kita nyebar data ing pirang-pirang server lan nangani throughput maca lan nulis sing dhuwur.

3. Aplikasi kita mbutuhake pamundhutan data sing cepet lan efisien. Basis data dokumen nyedhiyakake kemampuan pengindeksan lan kueri sing kuwat sing ngidini kita njupuk data kanthi cepet lan efisien.

4. Aplikasi kita ora mbutuhake transaksi utawa hubungan data sing kompleks. Sanajan basis data relasional unggul ing nerapake watesan integritas data lan nangani transaksi kompleks, aplikasi kita ora nduwe kabutuhan kaya mangkono. Basis data dokumen bisa nyedhiyakake jaminan konsistensi lan daya tahan sing cukup kanggo kasus panggunaan kita.

## Akibat

Kanthi milih basis data dokumen, kita kudu nandur modal ing sinau lan mangerteni teknologi tartamtu sing dipilih. Saliyane iku, kita kudu mesthekake yen model data aplikasi kita cocog karo model data basis data dokumen supaya kinerja lan skalabilitas maksimal.

Nanging, kita pitados yen kaluwihan nggunakake basis data dokumen ngungkuli biayane, lan iku sing paling cocog karo kabutuhan lan watesan aplikasi kita.
