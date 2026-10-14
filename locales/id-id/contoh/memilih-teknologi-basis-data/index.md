# Catatan Keputusan Arsitektur: Memilih Teknologi Basis Data

## Status

Diterima

## Konteks

Kami sedang merancang aplikasi baru yang memerlukan penyimpanan dan pengambilan data secara skalabel dan berkinerja baik. Kami telah mengidentifikasi tiga jenis teknologi basis data yang umum digunakan: basis data relasional, basis data dokumen, dan basis data event.

Basis data relasional menyimpan data dalam tabel dengan skema tetap dan menerapkan batasan integritas data yang ketat. Basis data ini cocok untuk aplikasi yang membutuhkan relasi data dan transaksi yang kompleks. Contohnya termasuk MySQL, PostgreSQL, dan Oracle.

Basis data dokumen menyimpan data dalam dokumen mirip JSON dan tanpa skema. Basis data ini sangat cocok untuk aplikasi yang membutuhkan model data fleksibel dan penskalaan horizontal. Contohnya termasuk MongoDB, Couchbase, dan Amazon DynamoDB.

Basis data event menyimpan data sebagai serangkaian event, yang menangkap setiap perubahan pada data. Basis data ini cocok untuk aplikasi yang membutuhkan audit, event sourcing, dan pemrosesan data yang kompleks. Contohnya termasuk Apache Kafka, Apache Pulsar, dan AWS Kinesis.
Keputusan

Setelah mengevaluasi dengan cermat persyaratan dan batasan aplikasi kami, kami memutuskan untuk menggunakan basis data dokumen.

## Alasan

Kami memilih basis data dokumen karena:

1. Aplikasi kami membutuhkan model data yang fleksibel dan dapat berkembang seiring waktu. Basis data dokumen memungkinkan kami menyimpan data dalam format tanpa skema, yang berarti kami dapat menambahkan bidang baru atau mengubah struktur dokumen yang ada tanpa harus mengubah skema basis data.

2. Aplikasi kami perlu diskalakan secara horizontal untuk menangani volume data dan lalu lintas yang besar. Basis data dokumen menyediakan dukungan bawaan untuk sharding dan replikasi, yang memungkinkan kami mendistribusikan data ke beberapa server dan menangani throughput baca dan tulis yang tinggi.

3. Aplikasi kami membutuhkan pengambilan data yang cepat dan efisien. Basis data dokumen menyediakan kemampuan pengindeksan dan kueri yang kuat yang memungkinkan kami mengambil data dengan cepat dan efisien.

4. Aplikasi kami tidak memerlukan transaksi atau relasi data yang kompleks. Meskipun basis data relasional unggul dalam menerapkan batasan integritas data dan menangani transaksi yang kompleks, aplikasi kami tidak memiliki persyaratan semacam itu. Basis data dokumen dapat memberikan jaminan konsistensi dan ketahanan yang memadai untuk kasus penggunaan kami.

## Konsekuensi

Dengan memilih basis data dokumen, kami perlu berinvestasi dalam mempelajari dan memahami teknologi spesifik yang kami pilih. Selain itu, kami perlu memastikan bahwa model data aplikasi kami cocok dengan model data basis data dokumen untuk memaksimalkan kinerja dan skalabilitas.

Namun, kami yakin bahwa manfaat menggunakan basis data dokumen lebih besar daripada biayanya, dan bahwa basis data dokumen adalah yang paling sesuai dengan persyaratan dan batasan aplikasi kami.
